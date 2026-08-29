"""Task metrics + the gain-decomposition table (the paper's main readout).

Decomposition (per backbone, per seed; means +/- sd across seeds reported):

    total VPT gain   = mIoU(learned)        - mIoU(no_token)
    insertion        = mIoU(frozen_random)  - mIoU(no_token)
    content transfer = mIoU(learned_frozen) - mIoU(frozen_random)
    co-adaptation    = mIoU(learned)        - mIoU(learned_frozen)
    sink geometry    = mIoU(sink_only)      - mIoU(no_token)   [optional arm]

insertion + content transfer + co-adaptation == total gain by construction
(telescoping), which is asserted in tests. The *hypothesis* (never claimed
as fact here) is that on dense tasks insertion / sink terms are non-zero,
unlike VPT Fig. 11's classification result where Prompt-Fixed ~= Linear.

H2 directional readout: total gain on register_free vs register_equipped.
"""

from __future__ import annotations

from collections import defaultdict

import numpy as np
import torch

from .config import ExperimentConfig
from .synthetic_data import SceneBatch
from .tiny_vit import DenseHead, TinyViT


@torch.no_grad()
def confusion_matrix(pred: torch.Tensor, target: torch.Tensor, num_labels: int) -> torch.Tensor:
    k = (target * num_labels + pred).flatten()
    return torch.bincount(k, minlength=num_labels**2).reshape(num_labels, num_labels)


def miou_from_confusion(cm: torch.Tensor) -> float:
    inter = cm.diag().float()
    union = cm.sum(0).float() + cm.sum(1).float() - inter
    present = union > 0
    return (inter[present] / union[present]).mean().item()


@torch.no_grad()
def evaluate_dense(
    backbone: TinyViT,
    head: DenseHead,
    prompt: torch.Tensor | None,
    prompt_is_sink: bool,
    val: SceneBatch,
    cfg: ExperimentConfig,
) -> tuple[float, float]:
    """Return (mIoU, pixel accuracy) on the val batch."""
    num_labels = cfg.data.num_labels
    cm = torch.zeros(num_labels, num_labels, dtype=torch.long)
    bs = cfg.train.batch_size
    correct, total = 0, 0
    for i in range(0, val.images.shape[0], bs):
        imgs = val.images[i : i + bs]
        labels = val.pixel_labels[i : i + bs]
        out = backbone(imgs, prompt=prompt, prompt_is_sink=prompt_is_sink)
        pred = head(out["patch_tokens"], backbone.cfg.grid).argmax(dim=1)
        cm += confusion_matrix(pred, labels, num_labels)
        correct += (pred == labels).sum().item()
        total += labels.numel()
    return miou_from_confusion(cm), correct / total


def aggregate(results: list) -> dict:
    """results: list[ArmResult] -> {backbone: {arm: (mean, sd, [per-seed])}}"""
    pool = defaultdict(lambda: defaultdict(list))
    for r in results:
        pool[r.backbone][r.arm].append(r.miou)
    out = {}
    for bb, arms in pool.items():
        out[bb] = {
            arm: (float(np.mean(v)), float(np.std(v)), list(map(float, v)))
            for arm, v in arms.items()
        }
    return out


def decomposition(agg_backbone: dict) -> dict:
    """Per-backbone decomposition from aggregate() output (per-seed, then
    mean +/- sd, so the components telescope seed-wise)."""

    def seeds(arm):
        return np.array(agg_backbone[arm][2])

    comps = {}
    have = set(agg_backbone)
    if {"learned", "no_token"} <= have:
        comps["total_vpt_gain"] = seeds("learned") - seeds("no_token")
    if {"frozen_random", "no_token"} <= have:
        comps["insertion"] = seeds("frozen_random") - seeds("no_token")
    if {"learned_frozen", "frozen_random"} <= have:
        comps["content_transfer"] = seeds("learned_frozen") - seeds("frozen_random")
    if {"learned", "learned_frozen"} <= have:
        comps["co_adaptation"] = seeds("learned") - seeds("learned_frozen")
    if {"sink_only", "no_token"} <= have:
        comps["sink_geometry"] = seeds("sink_only") - seeds("no_token")
    return {
        k: (float(v.mean()), float(v.std()), list(map(float, v))) for k, v in comps.items()
    }


def h2_gap(agg: dict) -> dict | None:
    """gain(VPT | register_free) - gain(VPT | register_equipped), per seed.

    Positive gap = the pre-registered H2 direction (VPT gains shrink when
    the backbone already has registers). Reported with seed sd; with the
    default 3 seeds this is a direction check, not a significance test.
    """
    need = {"register_free", "register_equipped"}
    if not need <= set(agg):
        return None
    gaps = []
    for bb in need:
        if not {"learned", "no_token"} <= set(agg[bb]):
            return None
    free = np.array(agg["register_free"]["learned"][2]) - np.array(
        agg["register_free"]["no_token"][2]
    )
    equipped = np.array(agg["register_equipped"]["learned"][2]) - np.array(
        agg["register_equipped"]["no_token"][2]
    )
    gaps = free - equipped
    return {
        "gain_register_free": (float(free.mean()), float(free.std())),
        "gain_register_equipped": (float(equipped.mean()), float(equipped.std())),
        "gap": (float(gaps.mean()), float(gaps.std()), list(map(float, gaps))),
        "direction_confirmed": bool(gaps.mean() > 0),
    }
