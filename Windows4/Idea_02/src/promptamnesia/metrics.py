"""Binary-mask metrics used across the battery. Fully implemented, numpy-only."""

from __future__ import annotations

import numpy as np


def dice(pred: np.ndarray, gt: np.ndarray, eps: float = 1e-7) -> float:
    """Dice coefficient between two binary masks (bool or {0,1})."""
    pred = pred.astype(bool)
    gt = gt.astype(bool)
    inter = np.logical_and(pred, gt).sum()
    denom = pred.sum() + gt.sum()
    if denom == 0:
        return 1.0  # both empty: conventional perfect agreement
    return float((2.0 * inter + eps) / (denom + eps))


def iou(pred: np.ndarray, gt: np.ndarray, eps: float = 1e-7) -> float:
    """Intersection-over-union between two binary masks."""
    pred = pred.astype(bool)
    gt = gt.astype(bool)
    inter = np.logical_and(pred, gt).sum()
    union = np.logical_or(pred, gt).sum()
    if union == 0:
        return 1.0
    return float((inter + eps) / (union + eps))


def binarize(soft: np.ndarray, threshold: float) -> np.ndarray:
    """Binarize a soft prediction (logits or probabilities) at a threshold.

    The threshold semantics (logit-space vs probability-space) must match the
    calibration sweep; `threshold_gate` always sweeps in the same space it
    receives, so callers must be consistent.
    """
    return soft > threshold
