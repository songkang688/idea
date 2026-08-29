"""Binary-overlap metric suite: IoU, Dice, F-beta, boundary-F.

Conventions (metrics_protocol.md section 2)
-------------------------------------------
- Inputs are boolean masks (or {0,1} arrays) unless stated otherwise.
- Empty-union-empty convention: when prediction and GT are both empty the score is
  1.0 for IoU/Dice/F-beta/boundary-F (smoke test sets contain no-smoke frames; the
  convention is printed in the paper).
- ``f_beta`` defaults to beta2 = 0.3, the saliency convention used by the SMOKE5K
  line (FoSp AAAI 2024 [V]) — binding obligation B4. The thresholding rule that turns
  soft maps into masks lives in the caller and is frozen protocol-wide (tau_op).
"""

from __future__ import annotations

import numpy as np
from scipy import ndimage


def _as_bool(x: np.ndarray, name: str) -> np.ndarray:
    x = np.asarray(x)
    if x.dtype == bool:
        return x
    uniq = np.unique(x)
    if not np.all(np.isin(uniq, (0, 1))):
        raise ValueError(f"{name} must be binary (bool or {{0,1}}), got values {uniq[:5]}")
    return x.astype(bool)


def iou(pred: np.ndarray, gt: np.ndarray) -> float:
    pred = _as_bool(pred, "pred")
    gt = _as_bool(gt, "gt")
    union = np.logical_or(pred, gt).sum()
    if union == 0:
        return 1.0
    return float(np.logical_and(pred, gt).sum() / union)


def dice(pred: np.ndarray, gt: np.ndarray) -> float:
    pred = _as_bool(pred, "pred")
    gt = _as_bool(gt, "gt")
    denom = pred.sum() + gt.sum()
    if denom == 0:
        return 1.0
    return float(2.0 * np.logical_and(pred, gt).sum() / denom)


def f_beta(pred: np.ndarray, gt: np.ndarray, beta2: float = 0.3) -> float:
    """F-beta with beta^2 = ``beta2`` (default 0.3, saliency/smoke convention, B4).

    VERIFY-AGAINST (R1): whether the field's protocol computes the dataset aggregate
    as mean-of-per-image-F or F-of-pooled-counts, and its adaptive-threshold rule.
    This function is per-image on already-binarized input.
    """
    pred = _as_bool(pred, "pred")
    gt = _as_bool(gt, "gt")
    tp = float(np.logical_and(pred, gt).sum())
    fp = float(np.logical_and(pred, ~gt).sum())
    fn = float(np.logical_and(~pred, gt).sum())
    if tp == 0 and fp == 0 and fn == 0:
        return 1.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    denom = beta2 * precision + recall
    if denom == 0:
        return 0.0
    return float((1 + beta2) * precision * recall / denom)


def _boundary(mask: np.ndarray) -> np.ndarray:
    """8-neighborhood inner boundary of a boolean mask."""
    if not mask.any():
        return np.zeros_like(mask, dtype=bool)
    eroded = ndimage.binary_erosion(mask, structure=np.ones((3, 3)), border_value=0)
    return mask & ~eroded


def boundary_f(pred: np.ndarray, gt: np.ndarray, tolerance_px: float = 2.0) -> float:
    """BF-style boundary F1 with a pixel-distance tolerance.

    Boundary pixels of pred/gt are matched if within ``tolerance_px`` (Euclidean, via
    distance transforms). Primary-endpoint component at 2 px (B2); report 1 px and
    5 px variants in the appendix.

    VERIFY-AGAINST (R1): BSDS/DAVIS-style ports differ in boundary extraction
    (4- vs 8-neighborhood) and in whether matching is one-to-one; this implementation
    uses 8-neighborhood boundaries and distance-threshold (many-to-many) matching,
    the common fast approximation.
    """
    pred = _as_bool(pred, "pred")
    gt = _as_bool(gt, "gt")
    bp = _boundary(pred)
    bg = _boundary(gt)
    if not bp.any() and not bg.any():
        return 1.0
    if not bp.any() or not bg.any():
        return 0.0
    # Distance from every pixel to the nearest boundary pixel of the other mask.
    dist_to_gt = ndimage.distance_transform_edt(~bg)
    dist_to_pred = ndimage.distance_transform_edt(~bp)
    precision = float((dist_to_gt[bp] <= tolerance_px).mean())
    recall = float((dist_to_pred[bg] <= tolerance_px).mean())
    if precision + recall == 0:
        return 0.0
    return float(2 * precision * recall / (precision + recall))


def binary_metric_report(
    pred_mask: np.ndarray,
    gt_mask: np.ndarray,
    beta2: float = 0.3,
    boundary_tolerance_px: float = 2.0,
) -> dict:
    """All binary-family metrics for one image (on already-binarized prediction)."""
    return {
        "iou": iou(pred_mask, gt_mask),
        "dice": dice(pred_mask, gt_mask),
        "f_beta": f_beta(pred_mask, gt_mask, beta2=beta2),
        "boundary_f": boundary_f(pred_mask, gt_mask, tolerance_px=boundary_tolerance_px),
    }
