"""Prompt samplers for the E2 fine-tuning mixes and the E3 evaluation battery.

Fully implemented (numpy/scipy). These are the *pre-registered* protocols:
- jittered GT box;
- single positive point (two placement rules: primary = error-free interior via
  distance transform; alternative = uniform interior — the dual-simulator
  hygiene inherited from the Stage-3 RClicks/BREPS kills);
- iterative click protocol: click k+1 at the center of the largest error
  component, NEGATIVE click if that component is a false positive;
- mixed-prompt sampler for the licensing column of the factorial.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

import numpy as np
from scipy import ndimage


@dataclass
class BoxJitterSpec:
    """Relative-uniform box jitter (pre-registered in shared_grid.yaml)."""

    max_shift: float = 0.05  # fraction of box side
    max_scale: float = 0.10  # fraction of box side


@dataclass
class ClickEvent:
    y: int
    x: int
    positive: bool


def box_from_mask(mask: np.ndarray) -> Optional[tuple[int, int, int, int]]:
    """Tight (y0, x0, y1, x1) box around a binary mask; None if mask empty."""
    ys, xs = np.nonzero(mask)
    if ys.size == 0:
        return None
    return int(ys.min()), int(xs.min()), int(ys.max()), int(xs.max())


def jitter_box(
    box: tuple[int, int, int, int],
    shape: tuple[int, int],
    spec: BoxJitterSpec,
    rng: np.random.Generator,
) -> tuple[int, int, int, int]:
    """Apply relative-uniform shift+scale jitter, clipped to the image."""
    y0, x0, y1, x1 = box
    h, w = y1 - y0 + 1, x1 - x0 + 1
    dy = rng.uniform(-spec.max_shift, spec.max_shift) * h
    dx = rng.uniform(-spec.max_shift, spec.max_shift) * w
    sy = rng.uniform(-spec.max_scale, spec.max_scale) * h / 2.0
    sx = rng.uniform(-spec.max_scale, spec.max_scale) * w / 2.0
    ny0 = int(round(y0 + dy - sy))
    nx0 = int(round(x0 + dx - sx))
    ny1 = int(round(y1 + dy + sy))
    nx1 = int(round(x1 + dx + sx))
    H, W = shape
    ny0, ny1 = max(0, min(ny0, H - 2)), max(1, min(ny1, H - 1))
    nx0, nx1 = max(0, min(nx0, W - 2)), max(1, min(nx1, W - 1))
    if ny1 <= ny0:
        ny1 = ny0 + 1
    if nx1 <= nx0:
        nx1 = nx0 + 1
    return ny0, nx0, ny1, nx1


def sample_point(
    mask: np.ndarray,
    rng: np.random.Generator,
    rule: Literal["error_free_interior", "uniform_interior"] = "error_free_interior",
    min_boundary_dist: int = 5,
) -> Optional[ClickEvent]:
    """Sample a single positive point inside a binary mask.

    primary rule: maximum-distance-transform interior point (deterministic up to
    ties, tie broken by rng) — robust to thin structures;
    alternative rule: uniform over interior pixels ≥ min_boundary_dist from the
    boundary (falls back to any interior pixel for thin masks).
    """
    if mask.sum() == 0:
        return None
    if rule == "error_free_interior":
        dist = ndimage.distance_transform_edt(mask)
        maxd = dist.max()
        ys, xs = np.nonzero(dist >= maxd - 1e-9)
    else:
        dist = ndimage.distance_transform_edt(mask)
        ys, xs = np.nonzero(dist >= min_boundary_dist)
        if ys.size == 0:
            ys, xs = np.nonzero(mask)
    i = rng.integers(ys.size)
    return ClickEvent(y=int(ys[i]), x=int(xs[i]), positive=True)


def next_iterative_click(
    pred: np.ndarray, gt: np.ndarray, rng: np.random.Generator
) -> Optional[ClickEvent]:
    """Iterative-5 protocol step: center of the largest error component.

    False-negative component -> positive click; false-positive component ->
    NEGATIVE click (the column that carries contrast O2, A1-109/C1-071).
    Returns None if prediction is perfect.
    """
    pred = pred.astype(bool)
    gt = gt.astype(bool)
    fn = np.logical_and(gt, ~pred)
    fp = np.logical_and(~gt, pred)

    def largest_component(err: np.ndarray) -> tuple[int, Optional[np.ndarray]]:
        if err.sum() == 0:
            return 0, None
        labels, n = ndimage.label(err)
        sizes = ndimage.sum_labels(err, labels, index=np.arange(1, n + 1))
        k = int(np.argmax(sizes)) + 1
        return int(sizes[k - 1]), labels == k

    fn_size, fn_comp = largest_component(fn)
    fp_size, fp_comp = largest_component(fp)
    if fn_size == 0 and fp_size == 0:
        return None
    if fn_size >= fp_size:
        comp, positive = fn_comp, True
    else:
        comp, positive = fp_comp, False
    dist = ndimage.distance_transform_edt(comp)
    maxd = dist.max()
    ys, xs = np.nonzero(dist >= maxd - 1e-9)
    i = rng.integers(ys.size)
    return ClickEvent(y=int(ys[i]), x=int(xs[i]), positive=positive)


class MixedPromptSampler:
    """Pre-registered mixed distribution for the licensing column (E2).

    composition: mapping {"box_jittered": p, "single_positive_point": p,
    "iterative_protocol": p} summing to ~1 (shared_grid.yaml).
    """

    KINDS = ("box_jittered", "single_positive_point", "iterative_protocol")

    def __init__(self, composition: dict[str, float], seed: int):
        ps = np.array([composition[k] for k in self.KINDS], dtype=float)
        if not np.isclose(ps.sum(), 1.0, atol=1e-3):
            raise ValueError(f"mixed composition must sum to 1, got {ps.sum():.4f}")
        self._ps = ps / ps.sum()
        self._rng = np.random.default_rng(seed)

    def draw_kind(self) -> str:
        return self.KINDS[int(self._rng.choice(len(self.KINDS), p=self._ps))]

    @property
    def rng(self) -> np.random.Generator:
        return self._rng
