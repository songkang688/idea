"""Dark-channel-prior transmission floor (He, Sun & Tang, CVPR 2009 [S3]) — B6.

Single-scattering haze model: I(x) = J(x) * t(x) + A * (1 - t(x)), where t is the
transmission and A the atmospheric (here: smoke-veil) light. The dark-channel prior
estimates t(x) = 1 - omega * dark(I / A); for a smoke-like medium the training-free
alpha floor is alpha_DC(x) = 1 - t(x).

KNOWN FACT: this is the standard haze formulation; using it for smoke assumes smoke
behaves as a homogeneous scattering veil (MODEL SPECULATION where multiple scattering
or emission dominates — that is precisely why this is a *floor*, not a method).

No training, no dataset-derived parameters. Guided-filter refinement is intentionally
omitted (keeps the floor dependency-free); an optional box smoothing is provided.
"""

from __future__ import annotations

import numpy as np
from scipy import ndimage


def dark_channel(img: np.ndarray, patch: int = 15) -> np.ndarray:
    """Dark channel: per-pixel min over channels, then min-filter over a patch."""
    img = np.asarray(img, dtype=np.float64)
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError(f"expected (H, W, 3) image, got {img.shape}")
    if patch < 1 or patch % 2 == 0:
        raise ValueError("patch must be a positive odd integer")
    per_pixel_min = img.min(axis=2)
    return ndimage.minimum_filter(per_pixel_min, size=patch, mode="nearest")


def estimate_atmospheric_light(
    img: np.ndarray, dark: np.ndarray, top_fraction: float = 0.001
) -> np.ndarray:
    """A = mean color of the brightest-in-dark-channel top fraction of pixels."""
    img = np.asarray(img, dtype=np.float64)
    flat_dark = dark.ravel()
    n = max(1, int(round(top_fraction * flat_dark.size)))
    idx = np.argpartition(flat_dark, -n)[-n:]
    flat_img = img.reshape(-1, 3)
    return flat_img[idx].mean(axis=0)


def transmission(
    img: np.ndarray,
    atmospheric: np.ndarray | None = None,
    omega: float = 0.95,
    patch: int = 15,
) -> np.ndarray:
    """t(x) = 1 - omega * darkChannel(I / A), clipped to [0, 1]."""
    img = np.asarray(img, dtype=np.float64)
    if atmospheric is None:
        atmospheric = estimate_atmospheric_light(img, dark_channel(img, patch))
    a = np.maximum(np.asarray(atmospheric, dtype=np.float64), 1e-6)
    normalized = np.clip(img / a[None, None, :], 0.0, 1.0)
    t = 1.0 - omega * dark_channel(normalized, patch)
    return np.clip(t, 0.0, 1.0)


def smoke_alpha_dark_channel(
    img: np.ndarray,
    omega: float = 0.95,
    patch: int = 15,
    smooth: int | None = None,
) -> np.ndarray:
    """Training-free smoke-alpha floor: alpha_DC = 1 - t(x), optional box smoothing.

    Scored under the identical protocol (same tau_op, same metrics) as every learned
    arm; enters every Part-A results cell and the Part-B checkpoint pool.
    """
    t = transmission(img, omega=omega, patch=patch)
    alpha = 1.0 - t
    if smooth is not None:
        if smooth < 1 or smooth % 2 == 0:
            raise ValueError("smooth must be a positive odd integer")
        alpha = ndimage.uniform_filter(alpha, size=smooth, mode="nearest")
    return np.clip(alpha, 0.0, 1.0)
