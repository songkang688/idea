"""Alpha-error metric suite (Rhemann et al., CVPR 2009 conventions) + smoke mMse.

Implements: MAE, SAD, MSE, per-image mMse, Gradient error, Connectivity error.

Conventions
-----------
- ``pred`` and ``gt`` are float arrays in [0, 1], shape (H, W).
- ``region`` (optional) is a boolean mask restricting evaluation (e.g. a trimap
  unknown region). Smoke benchmarks have no trimap, so the default is the full frame.
- SAD is returned raw; matting papers usually report SAD / 1000 — do the division at
  table-formatting time, not here, so the raw statistic stays inspectable.
- VERIFY-AGAINST notes: Gradient (sigma, normalization) and mMse (scaling, soft-vs-
  binarized input) must be reconciled with the released benchmark eval code at
  runbook step R1 before reporting (metrics_protocol.md sections 1, 2.3).
"""

from __future__ import annotations

import numpy as np
from scipy import ndimage


def _validate(pred: np.ndarray, gt: np.ndarray, region: np.ndarray | None):
    pred = np.asarray(pred, dtype=np.float64)
    gt = np.asarray(gt, dtype=np.float64)
    if pred.shape != gt.shape:
        raise ValueError(f"shape mismatch: pred {pred.shape} vs gt {gt.shape}")
    if pred.ndim != 2:
        raise ValueError(f"expected 2-D maps, got ndim={pred.ndim}")
    if region is None:
        region = np.ones_like(pred, dtype=bool)
    else:
        region = np.asarray(region, dtype=bool)
        if region.shape != pred.shape:
            raise ValueError("region shape mismatch")
    if pred.min() < -1e-6 or pred.max() > 1 + 1e-6:
        raise ValueError("pred must lie in [0, 1]")
    if gt.min() < -1e-6 or gt.max() > 1 + 1e-6:
        raise ValueError("gt must lie in [0, 1]")
    return pred, gt, region


def mae(pred: np.ndarray, gt: np.ndarray, region: np.ndarray | None = None) -> float:
    """Mean absolute error over the evaluation region."""
    pred, gt, region = _validate(pred, gt, region)
    if not region.any():
        raise ValueError("empty evaluation region")
    return float(np.abs(pred - gt)[region].mean())


def sad(pred: np.ndarray, gt: np.ndarray, region: np.ndarray | None = None) -> float:
    """Sum of absolute differences (raw; divide by 1000 for the matting convention)."""
    pred, gt, region = _validate(pred, gt, region)
    return float(np.abs(pred - gt)[region].sum())


def mse(pred: np.ndarray, gt: np.ndarray, region: np.ndarray | None = None) -> float:
    """Mean squared error over the evaluation region."""
    pred, gt, region = _validate(pred, gt, region)
    if not region.any():
        raise ValueError("empty evaluation region")
    return float(((pred - gt) ** 2)[region].mean())


def mmse_per_image(pred: np.ndarray, gt_binary: np.ndarray) -> float:
    """Per-image mMse component: MSE between the *soft* prediction and *binary* GT.

    The SMOKE5K-line protocol (Yan et al. AAAI 2022 [S3]; FoSp AAAI 2024 [V]) reports
    mMse = dataset mean of this per-image quantity. This is binding obligation B4:
    the mMse column enters the tau matrix so pre-registered kill K-B1 can test whether
    mMse-on-binary-GT already rank-agrees with alpha-MAE-on-alpha-GT.

    VERIFY-AGAINST (R1): released eval code — whether predictions are used soft (as
    here) or binarized, and whether a x100 scaling is applied in reported tables.
    """
    gt_binary = np.asarray(gt_binary)
    uniq = np.unique(gt_binary)
    if not np.all(np.isin(uniq, (0, 1))):
        raise ValueError("mmse_per_image expects binary GT (values in {0,1})")
    return mse(pred, gt_binary.astype(np.float64))


def _gauss_gradient_magnitude(x: np.ndarray, sigma: float) -> np.ndarray:
    gx = ndimage.gaussian_filter(x, sigma=sigma, order=(0, 1), mode="nearest")
    gy = ndimage.gaussian_filter(x, sigma=sigma, order=(1, 0), mode="nearest")
    return np.hypot(gx, gy)


def gradient_error(
    pred: np.ndarray,
    gt: np.ndarray,
    region: np.ndarray | None = None,
    sigma: float = 1.4,
) -> float:
    """Rhemann gradient error: sum of squared differences of Gaussian-derivative
    gradient magnitudes (sigma = 1.4 by convention).

    VERIFY-AGAINST (R1): community ports differ in sigma and in whether the sum is
    normalized by region size; this implementation returns the raw sum.
    """
    pred, gt, region = _validate(pred, gt, region)
    gp = _gauss_gradient_magnitude(pred, sigma)
    gg = _gauss_gradient_magnitude(gt, sigma)
    return float(((gp - gg) ** 2)[region].sum())


def _largest_cc(mask: np.ndarray) -> np.ndarray:
    """Largest 4-connected component of a boolean mask (empty-safe)."""
    labels, n = ndimage.label(mask, structure=np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
    if n == 0:
        return np.zeros_like(mask, dtype=bool)
    sizes = ndimage.sum_labels(np.ones_like(labels), labels, index=np.arange(1, n + 1))
    return labels == (int(np.argmax(sizes)) + 1)


def connectivity_error(
    pred: np.ndarray,
    gt: np.ndarray,
    region: np.ndarray | None = None,
    step: float = 0.1,
    theta: float = 0.15,
) -> float:
    """Rhemann connectivity error (standard Python port of the benchmark definition).

    For a threshold ladder t in {step, 2*step, ..., 1}, track for each pixel the last
    level at which it belonged to the largest connected component of
    (pred >= t) & (gt >= t); the degree of connectedness is penalized through the
    theta-soft distance phi. Returns the raw sum over the region.

    VERIFY-AGAINST (R1): the community port's conventions (4-connectivity, theta=0.15,
    step=0.1) are followed; the original benchmark used an equivalent MATLAB routine.
    """
    pred, gt, region = _validate(pred, gt, region)
    thresh_steps = np.arange(0.0, 1.0 + step / 2, step)
    l_map = -np.ones_like(pred)
    for i in range(1, len(thresh_steps)):
        t = thresh_steps[i]
        joint = (pred >= t) & (gt >= t)
        omega = _largest_cc(joint)
        newly_out = (l_map == -1) & (~omega)
        l_map[newly_out] = thresh_steps[i - 1]
    l_map[l_map == -1] = 1.0

    pred_d = pred - l_map
    gt_d = gt - l_map
    pred_phi = 1.0 - pred_d * (pred_d >= theta)
    gt_phi = 1.0 - gt_d * (gt_d >= theta)
    return float(np.abs(pred_phi - gt_phi)[region].sum())


def alpha_metric_report(
    pred: np.ndarray,
    gt_alpha: np.ndarray,
    region: np.ndarray | None = None,
    gt_binary: np.ndarray | None = None,
) -> dict:
    """All alpha-family metrics for one image; adds mMse if binary GT is supplied."""
    out = {
        "mae": mae(pred, gt_alpha, region),
        "sad": sad(pred, gt_alpha, region),
        "mse": mse(pred, gt_alpha, region),
        "grad": gradient_error(pred, gt_alpha, region),
        "conn": connectivity_error(pred, gt_alpha, region),
    }
    if gt_binary is not None:
        out["mmse"] = mmse_per_image(pred, gt_binary)
    return out
