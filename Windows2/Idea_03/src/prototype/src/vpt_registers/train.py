"""Backbone pretraining and per-arm dense training.

Backbone variants
-----------------
- ``register_free``:      no register slots. The global pretraining
  objectives can only be satisfied by aggregating scene statistics *inside
  patch tokens* (pooling is over patch tokens). This deliberately builds the
  invariance-breaking leak the hypothesis talks about into the sandbox.
- ``register_equipped``:  R register slots; the global heads pool over the
  register outputs instead, so global computation has a dedicated home and
  patch tokens stay comparatively clean.

The backbone is frozen (requires_grad=False, eval mode) before any arm runs.

Arms (all share DenseHead; only token treatment differs)
--------------------------------------------------------
- ``no_token``       (arm 4 / VPT baseline "d"): dense readout on frozen
                     patch features, no injected tokens.
- ``frozen_random``  (arm 1 / "b"): K tokens ~ N(0, 0.02), never trained.
                     Head trained. Any gain over no_token is *insertion /
                     register-geometry* effect (confounded with the softmax-
                     temperature effect H flagged — see sink_only).
- ``learned``        (arm 2 / "a", full VPT-shallow): tokens + head trained
                     jointly.
- ``learned_frozen`` (arm 3): tokens copied from the *learned* arm of the
                     same (backbone, seed) cell, frozen; a fresh head is
                     trained from scratch. Tests whether the learned
                     embedding *content* transfers without head
                     co-adaptation.
- ``sink_only``      (optional, H's attention-bias control): trainable keys,
                     values forced to zero every layer — the token can bend
                     attention geometry but cannot inject content.
"""

from __future__ import annotations

import zlib
from dataclasses import dataclass, replace

import torch
import torch.nn.functional as F

from .config import ExperimentConfig
from .synthetic_data import DataConfig, SceneBatch, generate_batch
from .tiny_vit import DenseHead, PretrainHeads, TinyViT, ViTConfig


@dataclass
class SeedData:
    """All scenes for one seed, shared across backbones and arms."""

    train: SceneBatch
    val: SceneBatch
    paired: SceneBatch  # val-like scenes rendered twice under independent g


def make_seed_data(cfg: ExperimentConfig, seed: int) -> SeedData:
    d = cfg.data
    t = cfg.train
    return SeedData(
        train=generate_batch(d, t.train_scenes, seed, split="train"),
        val=generate_batch(d, t.val_scenes, seed, split="val"),
        paired=generate_batch(d, t.paired_scenes, seed, split="test", paired_g=True),
    )


def _batches(batch: SceneBatch, batch_size: int, steps: int, gen: torch.Generator):
    n = batch.images.shape[0]
    for _ in range(steps):
        idx = torch.randint(0, n, (batch_size,), generator=gen)
        yield batch.images[idx], batch.pixel_labels[idx], batch.g[idx], batch.patch_labels[idx]


def pretrain_backbone(
    cfg: ExperimentConfig, variant: str, seed: int, data: SeedData
) -> TinyViT:
    """Pretrain on global-only objectives, then freeze."""
    torch.manual_seed(seed)
    n_reg = cfg.num_registers if variant == "register_equipped" else 0
    vit_cfg = replace(cfg.model, num_registers=n_reg)
    model = TinyViT(vit_cfg)
    heads = PretrainHeads(vit_cfg.dim, cfg.data.num_classes)
    opt = torch.optim.Adam(
        list(model.parameters()) + list(heads.parameters()), lr=cfg.train.pretrain_lr
    )
    gen = torch.Generator().manual_seed(seed)
    model.train()
    for imgs, pix_labels, g, _ in _batches(
        data.train, cfg.train.batch_size, cfg.train.pretrain_steps, gen
    ):
        out = model(imgs)
        if n_reg > 0:
            pooled = out["register_out"].mean(dim=1)
        else:
            pooled = out["patch_tokens"].mean(dim=1)
        g_pred, presence_logits = heads(pooled)
        presence = torch.zeros(imgs.shape[0], cfg.data.num_classes)
        for c in range(1, cfg.data.num_classes + 1):
            presence[:, c - 1] = (pix_labels == c).flatten(1).any(dim=1).float()
        loss = F.mse_loss(g_pred, g) + F.binary_cross_entropy_with_logits(
            presence_logits, presence
        )
        opt.zero_grad()
        loss.backward()
        opt.step()
    model.eval()
    for p in model.parameters():
        p.requires_grad_(False)
    return model


@dataclass
class ArmResult:
    arm: str
    backbone: str
    seed: int
    miou: float
    pixel_acc: float
    tokens: torch.Tensor | None  # final prompt tokens (K, D) or None
    head: DenseHead
    prompt_is_sink: bool


def _init_prompts(num_prompts: int, dim: int, seed: int) -> torch.Tensor:
    gen = torch.Generator().manual_seed(seed + 777)
    return torch.randn(num_prompts, dim, generator=gen) * 0.02


def train_arm(
    cfg: ExperimentConfig,
    backbone: TinyViT,
    variant: str,
    arm: str,
    seed: int,
    data: SeedData,
    learned_tokens: torch.Tensor | None = None,
) -> ArmResult:
    """Train one arm's head (and tokens, if the arm learns them)."""
    from .metrics import evaluate_dense  # local import avoids cycle

    # zlib.crc32 is deterministic across processes (builtin hash() is salted)
    torch.manual_seed(seed * 1000 + zlib.crc32(arm.encode()) % 1000)
    dim = backbone.cfg.dim
    prompt_is_sink = arm == "sink_only"

    if arm == "no_token":
        prompt = None
    elif arm == "learned_frozen":
        assert learned_tokens is not None, "learned_frozen needs the learned arm's tokens"
        prompt = learned_tokens.detach().clone().requires_grad_(False)
    else:
        prompt = _init_prompts(cfg.num_prompts, dim, seed).requires_grad_(
            arm in ("learned", "sink_only")
        )

    head = DenseHead(dim, cfg.data.num_labels, cfg.data.patch_size, cfg.head_kind)
    params = list(head.parameters())
    if prompt is not None and prompt.requires_grad:
        params.append(prompt)
    opt = torch.optim.Adam(params, lr=cfg.train.arm_lr)

    gen = torch.Generator().manual_seed(seed)
    for imgs, pix_labels, _, _ in _batches(
        data.train, cfg.train.batch_size, cfg.train.arm_steps, gen
    ):
        out = backbone(imgs, prompt=prompt, prompt_is_sink=prompt_is_sink)
        logits = head(out["patch_tokens"], backbone.cfg.grid)
        loss = F.cross_entropy(logits, pix_labels)
        opt.zero_grad()
        loss.backward()
        opt.step()

    miou, acc = evaluate_dense(
        backbone, head, prompt, prompt_is_sink, data.val, cfg
    )
    return ArmResult(
        arm=arm,
        backbone=variant,
        seed=seed,
        miou=miou,
        pixel_acc=acc,
        tokens=None if prompt is None else prompt.detach().clone(),
        head=head,
        prompt_is_sink=prompt_is_sink,
    )
