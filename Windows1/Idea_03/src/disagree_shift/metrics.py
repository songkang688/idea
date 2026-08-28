from __future__ import annotations

import numpy as np
import torch
import torch.nn.functional as F


def pixel_frequency(rater_masks: torch.Tensor) -> torch.Tensor:
    """rater_masks: (R,B,1,H,W) in {0,1} -> (B,1,H,W) frequencies."""
    return rater_masks.float().mean(dim=0)


def bce_soft(logits: torch.Tensor, freq: torch.Tensor) -> torch.Tensor:
    return F.binary_cross_entropy_with_logits(logits, freq)


def temperature_scale(logits: torch.Tensor, temperature: float) -> torch.Tensor:
    return logits / max(temperature, 1e-6)


def sparsification_curve(
    error_map: np.ndarray,
    uncertainty: np.ndarray,
    fractions: np.ndarray | None = None,
) -> np.ndarray:
    """error_map/uncertainty: (H,W). Return mean residual error after removing top-u pixels."""
    if fractions is None:
        fractions = np.linspace(0.0, 0.5, 11)
    flat_e = error_map.ravel()
    flat_u = uncertainty.ravel()
    order = np.argsort(-flat_u)
    out = []
    n = len(flat_e)
    for f in fractions:
        k = int(f * n)
        remain = np.ones(n, dtype=bool)
        remain[order[:k]] = False
        out.append(float(flat_e[remain].mean()) if remain.any() else 0.0)
    return np.asarray(out)


def aurc(curve: np.ndarray, fractions: np.ndarray | None = None) -> float:
    if fractions is None:
        fractions = np.linspace(0.0, 0.5, len(curve))
    return float(np.trapezoid(curve, fractions))
