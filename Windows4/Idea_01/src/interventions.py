"""Counterfactual instruments and no-image null shapes (proposal §12–§13).

PRIMARY instruments (on-manifold; the claim rests on these at E1):
  - object_out_inpaint : remove the object, keep the box. The prototype implements
    classical inpainting (Telea / Navier-Stokes via cv2, mean-fill fallback) which is ALSO
    the pre-registered robustness arm at E1; the diffusion inpainter slots in behind the
    same signature at Phase 1 (roadmap.md). For synthetic data the dataset provides the
    exact counterfactual (`Instance.background`), which supersedes inpainting.
  - object swap        : provided by the dataset (synthetic) / diffusion pipeline (real).

CONTROL:
  - sham_inpaint       : equal-area edit OUTSIDE the box; bounds seam/global artifacts.

SECONDARY probes (off-manifold; demoted per Stage-4 R2 — convergence checks only):
  - patch_shuffle_in_box (S-604), matched_noise_in_box (S-014 family softened).
  - Embedding-level mean replacement lives in model_sam.py (needs SAM internals).

NULL SHAPES (no image evidence):
  - box-fill rectangle; per-instance convexity-matched superellipse fill.
"""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np

from .utils import HAS_CV2, Box, box_fill_mask, _dilate

if HAS_CV2:
    import cv2  # type: ignore


# ------------------------------------------------------------ object-out

def object_out_inpaint(
    image: np.ndarray,
    gt_mask: np.ndarray,
    dilate_px: int = 4,
    method: str = "telea",
) -> np.ndarray:
    """Remove the object region (dilated) and fill from context.

    method: 'telea' | 'ns' (cv2.inpaint) | 'mean' (numpy fallback: context mean + matched
    noise). At E1 the diffusion inpainter implements this same signature.
    """
    m = _dilate(gt_mask.astype(bool), max(0, int(dilate_px))).astype(np.uint8)
    if HAS_CV2 and method in ("telea", "ns"):
        img8 = np.clip(image * 255.0, 0, 255).astype(np.uint8)
        flag = cv2.INPAINT_TELEA if method == "telea" else cv2.INPAINT_NS
        out8 = cv2.inpaint(img8, m, inpaintRadius=5, flags=flag)
        return out8.astype(np.float32) / 255.0
    # mean-fill fallback: context statistics + matched noise
    out = image.astype(np.float32).copy()
    ctx = ~m.astype(bool)
    mu, sd = float(out[ctx].mean()), float(out[ctx].std())
    rng = np.random.default_rng(0)
    out[m.astype(bool)] = np.clip(
        mu + sd * 0.5 * rng.standard_normal(int(m.sum())), 0, 1
    )
    return out


def sham_inpaint(
    image: np.ndarray,
    gt_mask: np.ndarray,
    box: Box,
    dilate_px: int = 4,
    method: str = "telea",
) -> Optional[np.ndarray]:
    """Inpaint an equal-area region OUTSIDE the box; the object is untouched.
    Any Dice movement under this condition bounds the instrument-artifact contribution
    (proposal §18). Returns None if no non-overlapping placement exists."""
    h, w = image.shape[:2]
    x0, y0, x1, y1 = box
    ys, xs = np.where(gt_mask)
    mh, mw = ys.max() - ys.min() + 1, xs.max() - xs.min() + 1
    shape_local = np.zeros((mh, mw), dtype=bool)
    shape_local[ys - ys.min(), xs - xs.min()] = True

    rng = np.random.default_rng(int(gt_mask.sum()))
    for _ in range(64):
        ty = int(rng.integers(0, max(1, h - mh)))
        tx = int(rng.integers(0, max(1, w - mw)))
        # placement must not intersect the (padded) box
        if tx + mw <= x0 - dilate_px or tx >= x1 + dilate_px or ty + mh <= y0 - dilate_px or ty >= y1 + dilate_px:
            sham_mask = np.zeros((h, w), dtype=bool)
            sham_mask[ty : ty + mh, tx : tx + mw] = shape_local
            return object_out_inpaint(image, sham_mask, dilate_px=dilate_px, method=method)
    return None


# --------------------------------------------------- secondary (off-manifold)

def patch_shuffle_in_box(
    image: np.ndarray, box: Box, patch_px: int = 16, seed: int = 0
) -> np.ndarray:
    """S-604: permute patch_px-aligned tiles inside the box. Off-manifold; secondary."""
    out = image.copy()
    x0, y0, x1, y1 = box
    crop = out[y0:y1, x0:x1]
    ch, cw = crop.shape[:2]
    p = patch_px
    gh, gw = ch // p, cw // p
    if gh * gw >= 2:
        tiles = [
            crop[i * p : (i + 1) * p, j * p : (j + 1) * p].copy()
            for i in range(gh)
            for j in range(gw)
        ]
        rng = np.random.default_rng(seed)
        perm = rng.permutation(len(tiles))
        k = 0
        for i in range(gh):
            for j in range(gw):
                crop[i * p : (i + 1) * p, j * p : (j + 1) * p] = tiles[perm[k]]
                k += 1
    out[y0:y1, x0:x1] = crop
    return out


def matched_noise_in_box(image: np.ndarray, box: Box, seed: int = 0) -> np.ndarray:
    """Replace the box interior with luminance-matched Gaussian noise (mean/std of the
    interior preserved). Off-manifold; secondary."""
    out = image.copy()
    x0, y0, x1, y1 = box
    crop = out[y0:y1, x0:x1]
    mu, sd = float(crop.mean()), float(crop.std())
    rng = np.random.default_rng(seed)
    out[y0:y1, x0:x1] = np.clip(
        mu + sd * rng.standard_normal(crop.shape).astype(np.float32), 0, 1
    )
    return out


# ---------------------------------------------------------------- null shapes

def superellipse_mask(box: Box, shape: Tuple[int, int], p: float) -> np.ndarray:
    """|2(x-cx)/w|^p + |2(y-cy)/h|^p <= 1 inside the box. p=2 ellipse; p->inf rectangle;
    p<1 star-like (low fill)."""
    x0, y0, x1, y1 = box
    w, h = max(1, x1 - x0), max(1, y1 - y0)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = (w - 1) / 2.0, (h - 1) / 2.0
    u = np.abs(2 * (xx - cx) / w) ** p + np.abs(2 * (yy - cy) / h) ** p
    m = np.zeros(shape[:2], dtype=bool)
    m[y0:y1, x0:x1] = u <= 1.0
    return m


def convexity_matched_mask(
    box: Box, shape: Tuple[int, int], target_fill_fraction: float
) -> np.ndarray:
    """Per-instance matched null (Stage-4 R2 missing-baseline 3): the centered
    superellipse whose in-box fill fraction matches the instance's GT fill fraction.
    GT-informed by construction — it is a calibration null, not a model. The learned
    box->mask regressor (model_sam.py) is the no-GT counterpart."""
    target = float(np.clip(target_fill_fraction, 0.05, 0.999))
    lo, hi = 0.3, 40.0
    best = superellipse_mask(box, shape, 2.0)
    for _ in range(24):  # monotone in p -> binary search on rasterized fill
        mid = 0.5 * (lo + hi)
        m = superellipse_mask(box, shape, mid)
        frac = m[box[1] : box[3], box[0] : box[2]].mean() if m.any() else 0.0
        best = m
        if frac < target:
            lo = mid
        else:
            hi = mid
    return best


def boxfill_null(box: Box, shape: Tuple[int, int]) -> np.ndarray:
    """Literal interpolator floor (Stage-3 Cluster 12 reporting obligation)."""
    return box_fill_mask(box, shape)
