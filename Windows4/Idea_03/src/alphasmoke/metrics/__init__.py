"""Metric implementations for the AlphaSmoke protocol (see metrics_protocol.md).

All functions operate on numpy arrays. Soft maps are float in [0, 1]; binary masks are
bool or {0, 1}. Definitions must be cross-checked against released benchmark eval code
(runbook step R1) before any paper-bound number is reported.
"""

from .alpha_metrics import (
    mae,
    sad,
    mse,
    mmse_per_image,
    gradient_error,
    connectivity_error,
    alpha_metric_report,
)
from .binary_metrics import (
    iou,
    dice,
    f_beta,
    boundary_f,
    binary_metric_report,
)
from .rank_agreement import (
    METRIC_DIRECTIONS,
    kendall_tau,
    tau_matrix,
    top_k_reversals,
    bootstrap_tau,
)

__all__ = [
    "mae",
    "sad",
    "mse",
    "mmse_per_image",
    "gradient_error",
    "connectivity_error",
    "alpha_metric_report",
    "iou",
    "dice",
    "f_beta",
    "boundary_f",
    "binary_metric_report",
    "METRIC_DIRECTIONS",
    "kendall_tau",
    "tau_matrix",
    "top_k_reversals",
    "bootstrap_tau",
]
