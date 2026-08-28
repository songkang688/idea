"""Tiny CPU ViT with prompt-token injection and register-slot bookkeeping.

The sequence layout is always::

    [ prompt slots (P) | register slots (R) | patch slots (N) ]

- Register slots exist only on the register-equipped backbone variant; their
  embeddings are learned during synthetic pretraining and frozen afterwards,
  mirroring "DINOv2 vs DINOv2-reg sibling" at toy scale.
- Prompt slots are injected per arm (VPT-shallow: prepended at the input and
  visible to every layer). Their parameters are owned by the *arm*, not by
  the backbone, so the backbone stays bit-identical across arms.
- ``prompt_is_sink=True`` implements H's attention-bias control: the prompt
  slots' *value* vectors are zeroed in every attention layer, so they can
  absorb attention mass (keys participate in the softmax, changing the
  denominator and the attention geometry) but can never inject content into
  patch tokens. This dissociates "token exists as a sink" from "token
  carries a learned embedding".

Attention is written out manually (no fused SDPA) so per-layer attention
probabilities can be captured for the register-signature metrics.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class ViTConfig:
    image_size: int = 32
    patch_size: int = 4
    dim: int = 48
    depth: int = 3
    heads: int = 4
    mlp_ratio: float = 2.0
    num_registers: int = 0  # >0 => register-equipped variant

    @property
    def num_patches(self) -> int:
        return (self.image_size // self.patch_size) ** 2

    @property
    def grid(self) -> int:
        return self.image_size // self.patch_size


class Attention(nn.Module):
    def __init__(self, dim: int, heads: int):
        super().__init__()
        assert dim % heads == 0
        self.heads = heads
        self.scale = (dim // heads) ** -0.5
        self.qkv = nn.Linear(dim, dim * 3, bias=True)
        self.proj = nn.Linear(dim, dim, bias=True)

    def forward(
        self, x: torch.Tensor, value_zero_slots: slice | None = None, capture: bool = False
    ):
        B, T, D = x.shape
        qkv = self.qkv(x).reshape(B, T, 3, self.heads, D // self.heads)
        q, k, v = qkv.permute(2, 0, 3, 1, 4)  # each (B, H, T, hd)
        if value_zero_slots is not None:
            v = v.clone()
            v[:, :, value_zero_slots, :] = 0.0
        attn = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)
        out = (attn @ v).transpose(1, 2).reshape(B, T, D)
        return self.proj(out), (attn.detach() if capture else None)


class Block(nn.Module):
    def __init__(self, cfg: ViTConfig):
        super().__init__()
        self.norm1 = nn.LayerNorm(cfg.dim)
        self.attn = Attention(cfg.dim, cfg.heads)
        self.norm2 = nn.LayerNorm(cfg.dim)
        hidden = int(cfg.dim * cfg.mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(cfg.dim, hidden), nn.GELU(), nn.Linear(hidden, cfg.dim)
        )

    def forward(self, x, value_zero_slots=None, capture=False):
        a, attn = self.attn(self.norm1(x), value_zero_slots, capture)
        x = x + a
        x = x + self.mlp(self.norm2(x))
        return x, attn


class TinyViT(nn.Module):
    """Backbone. ``num_registers`` distinguishes the two variants."""

    def __init__(self, cfg: ViTConfig):
        super().__init__()
        self.cfg = cfg
        self.patch_embed = nn.Conv2d(3, cfg.dim, cfg.patch_size, stride=cfg.patch_size)
        self.pos_embed = nn.Parameter(torch.randn(1, cfg.num_patches, cfg.dim) * 0.02)
        if cfg.num_registers > 0:
            self.register_tokens = nn.Parameter(
                torch.randn(1, cfg.num_registers, cfg.dim) * 0.02
            )
        else:
            self.register_tokens = None
        self.blocks = nn.ModuleList(Block(cfg) for _ in range(cfg.depth))
        self.norm = nn.LayerNorm(cfg.dim)

    def slot_layout(self, num_prompts: int) -> dict:
        R = self.cfg.num_registers
        P = num_prompts
        return {
            "prompt": slice(0, P),
            "register": slice(P, P + R),
            "patch": slice(P + R, P + R + self.cfg.num_patches),
        }

    def forward(
        self,
        images: torch.Tensor,
        prompt: torch.Tensor | None = None,
        prompt_is_sink: bool = False,
        capture_attn: bool = False,
    ) -> dict:
        """prompt: (P, dim) parameter tensor or None.

        Returns dict with per-slot final features, slot layout, and (if
        requested) per-layer attention probabilities.
        """
        B = images.shape[0]
        x = self.patch_embed(images).flatten(2).transpose(1, 2)  # (B, N, D)
        x = x + self.pos_embed
        parts = []
        P = 0
        if prompt is not None:
            P = prompt.shape[0]
            parts.append(prompt.unsqueeze(0).expand(B, -1, -1))
        if self.register_tokens is not None:
            parts.append(self.register_tokens.expand(B, -1, -1))
        parts.append(x)
        seq = torch.cat(parts, dim=1)
        layout = self.slot_layout(P)
        vzero = layout["prompt"] if (prompt_is_sink and P > 0) else None

        attns = []
        for blk in self.blocks:
            seq, attn = blk(seq, value_zero_slots=vzero, capture=capture_attn)
            if capture_attn:
                attns.append(attn)
        seq = self.norm(seq)
        return {
            "patch_tokens": seq[:, layout["patch"], :],
            "prompt_tokens": seq[:, layout["prompt"], :] if P > 0 else None,
            "register_out": seq[:, layout["register"], :]
            if self.cfg.num_registers > 0
            else None,
            "layout": layout,
            "attn": attns,
        }


class DenseHead(nn.Module):
    """Segmentation-style readout on the frozen patch-token feature map.

    ``linear``: per-patch linear D -> num_labels * patch^2, pixel-shuffled to
    full resolution (the dense analogue of a linear probe).
    ``conv``: reshape tokens to a (D, Hp, Wp) map, 3x3 conv, bilinear
    upsample, 1x1 conv (a light decoder).
    Same class for every arm so the decomposition is head-independent.
    """

    def __init__(self, dim: int, num_labels: int, patch_size: int, kind: str = "linear"):
        super().__init__()
        self.kind = kind
        self.patch_size = patch_size
        self.num_labels = num_labels
        if kind == "linear":
            self.proj = nn.Linear(dim, num_labels * patch_size * patch_size)
        elif kind == "conv":
            self.conv1 = nn.Conv2d(dim, dim, 3, padding=1)
            self.conv2 = nn.Conv2d(dim, num_labels, 1)
        else:
            raise ValueError(f"unknown head kind: {kind}")

    def forward(self, patch_tokens: torch.Tensor, grid: int) -> torch.Tensor:
        B, N, D = patch_tokens.shape
        assert N == grid * grid
        if self.kind == "linear":
            y = self.proj(patch_tokens)  # (B, N, L*p*p)
            y = y.view(B, grid, grid, self.num_labels, self.patch_size, self.patch_size)
            y = y.permute(0, 3, 1, 4, 2, 5).reshape(
                B, self.num_labels, grid * self.patch_size, grid * self.patch_size
            )
            return y
        fmap = patch_tokens.transpose(1, 2).reshape(B, D, grid, grid)
        y = F.gelu(self.conv1(fmap))
        y = F.interpolate(y, scale_factor=self.patch_size, mode="bilinear", align_corners=False)
        return self.conv2(y)


class PretrainHeads(nn.Module):
    """Global-only pretraining objectives (illumination regression + class
    presence). Both are *scene-level*: this is what creates the pressure to
    aggregate global information somewhere, which on the register-free
    variant can only be inside patch tokens (the invariance-breaking leak the
    hypothesis talks about) and on the register-equipped variant is pooled
    from the register slots.
    """

    def __init__(self, dim: int, num_classes: int):
        super().__init__()
        self.g_head = nn.Linear(dim, 3)
        self.presence_head = nn.Linear(dim, num_classes)

    def forward(self, pooled: torch.Tensor):
        return self.g_head(pooled), self.presence_head(pooled)
