"""Compatibility shim — metrics now live in alphasmoke.metrics.

The full protocol suite (alpha: MAE/SAD/MSE/mMse/Grad/Conn; binary: IoU/Dice/
F-beta/boundary-F; rank agreement: sign-aligned Kendall tau, reversals, bootstrap)
is in the package; this shim keeps the skeleton's entry points importable.
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))

from alphasmoke.metrics import (  # noqa: E402,F401
    alpha_metric_report,
    binary_metric_report,
    dice,
    f_beta,
    iou,
    kendall_tau,
    mae,
    mmse_per_image,
    tau_matrix,
)


def mmse_alpha(pred: np.ndarray, gt: np.ndarray) -> float:
    """Skeleton-compatible name: per-image MSE of soft pred vs binary GT."""
    return mmse_per_image(np.clip(np.asarray(pred, dtype=np.float64), 0, 1), gt)
