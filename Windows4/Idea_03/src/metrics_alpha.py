from __future__ import annotations
import numpy as np

def dice(a: np.ndarray, b: np.ndarray) -> float:
    a, b = a.astype(bool), b.astype(bool)
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2 * np.logical_and(a, b).sum() / s

def mmse_alpha(pred: np.ndarray, gt: np.ndarray) -> float:
    p = pred.astype(np.float64)
    g = gt.astype(np.float64)
    return float(np.mean((p - g) ** 2))
