"""Shared utilities: metrics (Dice / IoU / boundary-F), box ops, shape statistics,
seeding, and small IO helpers. Pure numpy where possible; cv2 used when available with
documented fallbacks so the harness stays runnable in minimal environments.
"""

from __future__ import annotations

import json
import os
import random
from typing import Sequence, Tuple

import numpy as np

try:
    import cv2  # type: ignore

    HAS_CV2 = True
except Exception:  # pragma: no cover - environment-dependent
    cv2 = None
    HAS_CV2 = False

Box = Tuple[int, int, int, int]  # (x0, y0, x1, y1), half-open: image[y0:y1, x0:x1]

EPS = 1e-8


# ---------------------------------------------------------------- seeding / io

def set_seed(seed: int) -> np.random.Generator:
    random.seed(seed)
    np.random.seed(seed % (2**32 - 1))
    try:
        import torch

        torch.manual_seed(seed)
    except Exception:
        pass
    return np.random.default_rng(seed)


def ensure_dir(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def save_json(obj, path: str) -> None:
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True, default=_json_default)


def _json_default(o):
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.bool_,)):
        return bool(o)
    raise TypeError(f"not JSON serializable: {type(o)}")


# ------------------------------------------------------------------- images

def to_uint8_gray(img: np.ndarray) -> np.ndarray:
    if img.dtype == np.uint8:
        return img
    return np.clip(img * 255.0, 0, 255).astype(np.uint8)


def to_rgb_uint8(img: np.ndarray) -> np.ndarray:
    """Grayscale float [0,1] or uint8 -> HxWx3 uint8 (what official SAM expects)."""
    g = to_uint8_gray(img)
    if g.ndim == 2:
        return np.stack([g, g, g], axis=-1)
    return g


# ------------------------------------------------------------------- metrics

def dice(a: np.ndarray, b: np.ndarray) -> float:
    a = a.astype(bool)
    b = b.astype(bool)
    inter = np.logical_and(a, b).sum()
    s = a.sum() + b.sum()
    if s == 0:
        return 1.0
    return float(2.0 * inter / (s + EPS))


def iou(a: np.ndarray, b: np.ndarray) -> float:
    a = a.astype(bool)
    b = b.astype(bool)
    union = np.logical_or(a, b).sum()
    if union == 0:
        return 1.0
    return float(np.logical_and(a, b).sum() / (union + EPS))


def _boundary(mask: np.ndarray) -> np.ndarray:
    m = mask.astype(np.uint8)
    if HAS_CV2:
        er = cv2.erode(m, np.ones((3, 3), np.uint8))
    else:
        er = np.zeros_like(m)
        er[1:-1, 1:-1] = (
            m[1:-1, 1:-1]
            & m[:-2, 1:-1]
            & m[2:, 1:-1]
            & m[1:-1, :-2]
            & m[1:-1, 2:]
        )
    return (m.astype(bool)) & (~er.astype(bool))


def _dilate(mask: np.ndarray, r: int) -> np.ndarray:
    m = mask.astype(np.uint8)
    if r <= 0:
        return m.astype(bool)
    if HAS_CV2:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
        return cv2.dilate(m, k).astype(bool)
    out = m.astype(bool)
    for _ in range(r):
        nxt = out.copy()
        nxt[:-1, :] |= out[1:, :]
        nxt[1:, :] |= out[:-1, :]
        nxt[:, :-1] |= out[:, 1:]
        nxt[:, 1:] |= out[:, :-1]
        out = nxt
    return out


def boundary_f(pred: np.ndarray, gt: np.ndarray, tol: int = 2) -> float:
    """Boundary F-measure with pixel tolerance `tol` (secondary metric; see proposal §15)."""
    bp, bg = _boundary(pred), _boundary(gt)
    if bp.sum() == 0 and bg.sum() == 0:
        return 1.0
    if bp.sum() == 0 or bg.sum() == 0:
        return 0.0
    prec = float((bp & _dilate(bg, tol)).sum() / (bp.sum() + EPS))
    rec = float((bg & _dilate(bp, tol)).sum() / (bg.sum() + EPS))
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)


# ------------------------------------------------------------------- boxes

def mask_to_tight_box(mask: np.ndarray) -> Box:
    ys, xs = np.where(mask.astype(bool))
    if len(xs) == 0:
        raise ValueError("empty mask has no tight box")
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def pad_box(box: Box, pad: int, shape: Tuple[int, int]) -> Box:
    h, w = shape[:2]
    x0, y0, x1, y1 = box
    return (
        max(0, x0 - pad),
        max(0, y0 - pad),
        min(w, x1 + pad),
        min(h, y1 + pad),
    )


def box_area(box: Box) -> int:
    x0, y0, x1, y1 = box
    return max(0, x1 - x0) * max(0, y1 - y0)


def box_fill_mask(box: Box, shape: Tuple[int, int]) -> np.ndarray:
    m = np.zeros(shape[:2], dtype=bool)
    x0, y0, x1, y1 = box
    m[y0:y1, x0:x1] = True
    return m


# --------------------------------------------------------- shape statistics

def solidity(mask: np.ndarray) -> float:
    """Area / convex-hull area. cv2 hull when available; bounding-box fallback
    (documented: fallback overestimates hull, i.e. underestimates solidity)."""
    m = mask.astype(np.uint8)
    area = float(m.sum())
    if area == 0:
        return 0.0
    if HAS_CV2:
        pts = cv2.findNonZero(m)
        hull = cv2.convexHull(pts)
        hull_area = float(cv2.contourArea(hull))
        if hull_area <= 0:
            return 1.0
        return min(1.0, area / hull_area)
    return min(1.0, area / float(box_area(mask_to_tight_box(mask)) + EPS))


def fill_fraction_in_box(mask: np.ndarray, box: Box) -> float:
    x0, y0, x1, y1 = box
    a = box_area(box)
    if a == 0:
        return 0.0
    return float(mask[y0:y1, x0:x1].sum() / a)


def rms_contrast_in_box(image: np.ndarray, mask: np.ndarray, box: Box) -> float:
    """|mean(object) - mean(non-object within box)| — the low-contrast stratification
    variable (proposal §14; cf. Huang et al. arXiv:2304.14660)."""
    x0, y0, x1, y1 = box
    crop = image[y0:y1, x0:x1].astype(np.float64)
    mcrop = mask[y0:y1, x0:x1].astype(bool)
    if mcrop.sum() == 0 or (~mcrop).sum() == 0:
        return 0.0
    return float(abs(crop[mcrop].mean() - crop[~mcrop].mean()))


# ------------------------------------------------------------------ stats

def median(xs: Sequence[float]) -> float:
    return float(np.median(np.asarray(xs, dtype=np.float64))) if len(xs) else float("nan")


def bootstrap_ci_median(
    xs: Sequence[float], n_boot: int = 2000, alpha: float = 0.05, seed: int = 0
) -> Tuple[float, float]:
    """Percentile bootstrap CI on the median (BCa reserved for the real E1 analysis)."""
    xs = np.asarray(xs, dtype=np.float64)
    if len(xs) == 0:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    meds = np.median(
        xs[rng.integers(0, len(xs), size=(n_boot, len(xs)))], axis=1
    )
    lo, hi = np.quantile(meds, [alpha / 2, 1 - alpha / 2])
    return float(lo), float(hi)
