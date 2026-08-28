"""Synthetic dense-prediction scenes with a *global* nuisance factor.

Design goal (why this generator looks the way it does):

B-0114's mechanism question is whether prompt tokens help dense tasks by
acting as *registers* (global-aggregation workspace) rather than by carrying
learned task content. For that question to be instrumentable at all, the
synthetic dense task must actually *need* global context — a task solvable
from a 4x4 patch alone would give every arm the same score and the
decomposition would be vacuous.

Construction:

- Each scene is a HxW RGB image containing K_shapes axis-aligned rectangles
  drawn from C semantic classes on a textured background (class 0).
- Each class c has a fixed base color palette[c].
- A scene-global illumination vector g (per-channel gain) multiplies every
  pixel. Class identity is recoverable only *relative to* g: the same class
  looks different across scenes, and different classes can collide in raw
  RGB under different g. A purely local readout therefore hits a ceiling;
  undoing g requires aggregating global scene statistics — the kind of
  computation register tokens are hypothesised to host.
- Per-pixel label = class index (0 = background). Labels are emitted both at
  pixel resolution and at patch resolution (majority vote) so heads can be
  scored consistently.

Paired-nuisance API: `generate_batch(..., paired_g=True)` returns two
renderings of the *same* layouts under independent g draws. The invariance
metric (signatures.nuisance_sensitivity) uses these pairs to measure how much
patch features move when only the global nuisance moves — the dense-task
"invariance breaking" axis of the hypothesis.

Everything is deterministic given (seed, split) — train/val/test use
disjoint seed offsets.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch

# Fixed palette: base colors for background + up to 6 foreground classes.
# Chosen so classes are separated in *illumination-normalized* color space
# but overlap in raw RGB once per-channel gain in [0.4, 1.6] is applied.
_PALETTE = np.array(
    [
        [0.35, 0.35, 0.35],  # 0 background (grey)
        [0.80, 0.25, 0.25],  # 1 red-ish
        [0.25, 0.80, 0.25],  # 2 green-ish
        [0.25, 0.25, 0.80],  # 3 blue-ish
        [0.75, 0.75, 0.20],  # 4 yellow-ish
        [0.70, 0.25, 0.70],  # 5 magenta-ish
        [0.20, 0.70, 0.70],  # 6 cyan-ish
    ],
    dtype=np.float32,
)

_SPLIT_SEED_OFFSET = {"train": 0, "val": 100_000, "test": 200_000}


@dataclass
class SceneBatch:
    """One batch of synthetic scenes.

    images:       (B, 3, H, W) float32
    pixel_labels: (B, H, W) int64, values in [0, num_classes]
    patch_labels: (B, Hp, Wp) int64 majority label per patch
    g:            (B, 3) the global illumination vector actually applied
    images_alt:   optional second rendering of the same layouts under an
                  independent g draw (present iff paired_g=True)
    g_alt:        illumination of the alt rendering
    """

    images: torch.Tensor
    pixel_labels: torch.Tensor
    patch_labels: torch.Tensor
    g: torch.Tensor
    images_alt: torch.Tensor | None = None
    g_alt: torch.Tensor | None = None


def _sample_layout(rng: np.random.Generator, cfg: "DataConfig") -> np.ndarray:
    """Return (H, W) int label map with random rectangles over background."""
    labels = np.zeros((cfg.image_size, cfg.image_size), dtype=np.int64)
    n_shapes = rng.integers(cfg.min_shapes, cfg.max_shapes + 1)
    for _ in range(n_shapes):
        cls = int(rng.integers(1, cfg.num_classes + 1))
        h = int(rng.integers(cfg.min_shape_px, cfg.max_shape_px + 1))
        w = int(rng.integers(cfg.min_shape_px, cfg.max_shape_px + 1))
        y = int(rng.integers(0, cfg.image_size - h + 1))
        x = int(rng.integers(0, cfg.image_size - w + 1))
        labels[y : y + h, x : x + w] = cls
    return labels


def _render(
    labels: np.ndarray, g: np.ndarray, rng: np.random.Generator, cfg: "DataConfig"
) -> np.ndarray:
    """Render a label map to (3, H, W) under illumination g."""
    base = _PALETTE[labels]  # (H, W, 3)
    tex = rng.normal(0.0, cfg.texture_noise, size=base.shape).astype(np.float32)
    img = (base + tex) * g[None, None, :]
    img += rng.normal(0.0, cfg.pixel_noise, size=img.shape).astype(np.float32)
    return np.clip(img, 0.0, 2.0).transpose(2, 0, 1).astype(np.float32)


def _patch_majority(labels: np.ndarray, patch: int) -> np.ndarray:
    """Majority-vote label per non-overlapping patch."""
    H, W = labels.shape
    hp, wp = H // patch, W // patch
    tiles = labels.reshape(hp, patch, wp, patch).transpose(0, 2, 1, 3).reshape(hp, wp, -1)
    out = np.zeros((hp, wp), dtype=np.int64)
    for i in range(hp):
        for j in range(wp):
            out[i, j] = np.bincount(tiles[i, j]).argmax()
    return out


@dataclass
class DataConfig:
    image_size: int = 32
    patch_size: int = 4
    num_classes: int = 4  # foreground classes; labels are 0..num_classes
    min_shapes: int = 2
    max_shapes: int = 5
    min_shape_px: int = 6
    max_shape_px: int = 14
    g_low: float = 0.4
    g_high: float = 1.6
    texture_noise: float = 0.03
    pixel_noise: float = 0.02

    @property
    def num_labels(self) -> int:
        return self.num_classes + 1


def generate_batch(
    cfg: DataConfig,
    batch_size: int,
    seed: int,
    split: str = "train",
    paired_g: bool = False,
) -> SceneBatch:
    """Deterministically generate a batch for the given (seed, split)."""
    rng = np.random.default_rng(seed + _SPLIT_SEED_OFFSET[split])
    imgs, alts, pix, pat, gs, gs_alt = [], [], [], [], [], []
    for _ in range(batch_size):
        layout = _sample_layout(rng, cfg)
        g = rng.uniform(cfg.g_low, cfg.g_high, size=3).astype(np.float32)
        imgs.append(_render(layout, g, rng, cfg))
        gs.append(g)
        pix.append(layout)
        pat.append(_patch_majority(layout, cfg.patch_size))
        if paired_g:
            g2 = rng.uniform(cfg.g_low, cfg.g_high, size=3).astype(np.float32)
            alts.append(_render(layout, g2, rng, cfg))
            gs_alt.append(g2)
    batch = SceneBatch(
        images=torch.from_numpy(np.stack(imgs)),
        pixel_labels=torch.from_numpy(np.stack(pix)),
        patch_labels=torch.from_numpy(np.stack(pat)),
        g=torch.from_numpy(np.stack(gs)),
    )
    if paired_g:
        batch.images_alt = torch.from_numpy(np.stack(alts))
        batch.g_alt = torch.from_numpy(np.stack(gs_alt))
    return batch
