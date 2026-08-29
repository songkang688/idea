"""Measured-alpha recovery by compositing inversion against known backgrounds (B3).

Model (metrics_protocol.md section 4): on a static, exposure-locked camera,

    I(x) = alpha(x) * F + (1 - alpha(x)) * B(x)

with B(x) the per-pixel clean background (temporal median of pre-smoke frames) and F
the smoke color, assumed locally uniform per frame. Per-pixel least squares across
channels gives

    alpha(x) = <I(x) - B(x), F - B(x)> / ||F - B(x)||^2,  clipped to [0, 1].

This is the arm that breaks the synthetic-alpha circularity attack (R2 Set C, P096
attack 3): alpha is *measured from real smoke optics*, not authored by a compositor or
an annotator.

Binding exclusions (all from the Set-C verdict; defaults in configs/alpha_capture.yaml):
saturated pixels, ill-conditioned pixels (||F - B|| below threshold), and pixels whose
recovered alpha is sensitive to the smoke-color assumption beyond ``s_max``. Frames
failing exposure-lock QC never reach this module.

Honest scope note: locally-uniform F and single scattering are approximations
(MODEL SPECULATION where violated); the sensitivity mask converts the violation from
a silent bias into an explicit exclusion plus a released uncertainty map.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class AlphaRecovery:
    """Result of one frame's alpha recovery."""

    alpha: np.ndarray  # (H, W) float in [0, 1]; NaN outside valid mask
    valid: np.ndarray  # (H, W) bool — pixels passing all exclusions
    smoke_color: np.ndarray  # (3,) the F used
    sensitivity: np.ndarray | None = None  # (H, W) std of alpha under F perturbation
    exclusion_counts: dict = field(default_factory=dict)


def _check_image(x: np.ndarray, name: str) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    if x.ndim != 3 or x.shape[2] != 3:
        raise ValueError(f"{name} must be (H, W, 3), got {x.shape}")
    if x.min() < -1e-6 or x.max() > 1 + 1e-6:
        raise ValueError(f"{name} must be float in [0, 1]")
    return x


def estimate_background(pre_smoke_frames: list[np.ndarray] | np.ndarray) -> np.ndarray:
    """Per-pixel temporal median of >= 1 pre-smoke frames (protocol default K >= 10;
    the median suppresses transient motion such as birds/foliage)."""
    frames = np.stack([_check_image(f, "pre-smoke frame") for f in pre_smoke_frames], axis=0)
    return np.median(frames, axis=0)


def estimate_smoke_color(
    frame: np.ndarray, background: np.ndarray, dense_quantile: float = 0.02
) -> np.ndarray:
    """F estimate: mean color over the densest-smoke pixels (largest ||I - B||).

    Where a calibrated lab target is available, pass F directly to recover_alpha and
    skip this estimator (configs/alpha_capture.yaml -> smoke_color_source).
    """
    frame = _check_image(frame, "frame")
    background = _check_image(background, "background")
    diff = np.linalg.norm(frame - background, axis=2)
    n = max(1, int(round(dense_quantile * diff.size)))
    idx = np.argpartition(diff.ravel(), -n)[-n:]
    return frame.reshape(-1, 3)[idx].mean(axis=0)


def recover_alpha(
    frame: np.ndarray,
    background: np.ndarray,
    smoke_color: np.ndarray | None = None,
    saturation_eps: float = 2.0 / 255.0,
    conditioning_min: float = 0.08,
    compute_sensitivity: bool = True,
    sensitivity_delta: float = 0.05,
    sensitivity_max: float = 0.10,
) -> AlphaRecovery:
    """Recover per-pixel alpha for one exposure-locked frame.

    Parameters mirror metrics_protocol.md section 4.2; defaults are the protocol
    defaults and live in configs/alpha_capture.yaml.
    """
    frame = _check_image(frame, "frame")
    background = _check_image(background, "background")
    if frame.shape != background.shape:
        raise ValueError("frame/background shape mismatch")

    if smoke_color is None:
        smoke_color = estimate_smoke_color(frame, background)
    f = np.asarray(smoke_color, dtype=np.float64).reshape(3)

    # Exclusion 1: saturation in I or B (any channel outside [eps, 1 - eps]).
    sat_i = np.any((frame < saturation_eps) | (frame > 1 - saturation_eps), axis=2)
    sat_b = np.any((background < saturation_eps) | (background > 1 - saturation_eps), axis=2)
    not_saturated = ~(sat_i | sat_b)

    # Exclusion 2: conditioning — where F ~= B, alpha is unidentifiable.
    fb = f[None, None, :] - background  # (H, W, 3)
    fb_norm = np.linalg.norm(fb, axis=2)
    well_conditioned = fb_norm >= conditioning_min

    # Least squares across channels.
    ib = frame - background
    denom = np.maximum(fb_norm**2, 1e-12)
    alpha = np.clip(np.sum(ib * fb, axis=2) / denom, 0.0, 1.0)

    valid = not_saturated & well_conditioned
    sensitivity = None
    n_sens_excluded = 0
    if compute_sensitivity:
        sensitivity = sensitivity_to_smoke_color(
            frame, background, f, delta=sensitivity_delta
        )
        sens_ok = sensitivity <= sensitivity_max
        n_sens_excluded = int((valid & ~sens_ok).sum())
        valid = valid & sens_ok

    alpha_out = np.where(valid, alpha, np.nan)
    return AlphaRecovery(
        alpha=alpha_out,
        valid=valid,
        smoke_color=f,
        sensitivity=sensitivity,
        exclusion_counts={
            "saturated": int((sat_i | sat_b).sum()),
            "ill_conditioned": int((~well_conditioned).sum()),
            "sensitivity_excluded": n_sens_excluded,
            "valid": int(valid.sum()),
            "total": int(valid.size),
        },
    )


def sensitivity_to_smoke_color(
    frame: np.ndarray,
    background: np.ndarray,
    smoke_color: np.ndarray,
    delta: float = 0.05,
) -> np.ndarray:
    """Std of recovered alpha under +/-delta per-channel perturbations of F.

    Uses the 6 axis perturbations plus 2 uniform (all-channel) perturbations —
    8 total, matching the protocol default. High values flag pixels where the
    locally-uniform-F assumption drives the answer; those pixels are excluded and the
    map is released with the dataset.
    """
    frame = _check_image(frame, "frame")
    background = _check_image(background, "background")
    f = np.asarray(smoke_color, dtype=np.float64).reshape(3)

    perturbations = []
    for c in range(3):
        for sign in (+1.0, -1.0):
            p = f.copy()
            p[c] = np.clip(p[c] + sign * delta, 0.0, 1.0)
            perturbations.append(p)
    perturbations.append(np.clip(f + delta, 0.0, 1.0))
    perturbations.append(np.clip(f - delta, 0.0, 1.0))

    ib = frame - background
    alphas = []
    for p in perturbations:
        fb = p[None, None, :] - background
        denom = np.maximum(np.sum(fb * fb, axis=2), 1e-12)
        alphas.append(np.clip(np.sum(ib * fb, axis=2) / denom, 0.0, 1.0))
    return np.std(np.stack(alphas, axis=0), axis=0)
