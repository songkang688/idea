"""HSV / low-chroma color rule for smoke — training-free floor (B6).

Rationale (KNOWN FACT about the rule family, not a claim about performance): visible
smoke is predominantly achromatic — low saturation, low channel spread (R ~= G ~= B) —
with value in a mid-to-high band (gray-white plumes; dark smoke is handled by widening
the value band, see config). Classical color-rule smoke detection is a decades-old
family; the specific historical citation used in any draft is [M] until re-verified
(CITATIONS.md). This module is the *control*, not a contribution.

Protocol constraints (metrics_protocol.md section 6):
- Weights/thresholds are fixed a priori in configs/eval_protocol.yaml and are never
  tuned on any test set; tuning is allowed only on a held-out train split and logged.
- Output is a soft score in [0, 1]; it enters every Part-A table and the Part-B pool
  under the same operating threshold tau_op as every learned arm.
"""

from __future__ import annotations

import numpy as np


def rgb_to_hsv(img: np.ndarray) -> np.ndarray:
    """Vectorized RGB->HSV for float images in [0, 1]; returns (H, W, 3) with
    H in [0, 1) (fraction of the color wheel), S in [0, 1], V in [0, 1]."""
    img = np.asarray(img, dtype=np.float64)
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError(f"expected (H, W, 3) RGB image, got {img.shape}")
    if img.min() < -1e-6 or img.max() > 1 + 1e-6:
        raise ValueError("image must be float in [0, 1]")

    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    v = img.max(axis=2)
    c = v - img.min(axis=2)  # chroma

    s = np.where(v > 0, c / np.maximum(v, 1e-12), 0.0)

    h = np.zeros_like(v)
    nz = c > 1e-12
    rmax = nz & (v == r)
    gmax = nz & (v == g) & ~rmax
    bmax = nz & (v == b) & ~rmax & ~gmax
    cc = np.maximum(c, 1e-12)
    h[rmax] = (((g - b) / cc)[rmax]) % 6.0
    h[gmax] = (((b - r) / cc)[gmax]) + 2.0
    h[bmax] = (((r - g) / cc)[bmax]) + 4.0
    h = h / 6.0
    return np.stack([h, s, v], axis=2)


def _band_score(v: np.ndarray, lo: float, hi: float, soft: float) -> np.ndarray:
    """Soft indicator of v in [lo, hi]: 1 inside, linear rolloff of width `soft`."""
    below = np.clip((v - (lo - soft)) / max(soft, 1e-12), 0.0, 1.0)
    above = np.clip(((hi + soft) - v) / max(soft, 1e-12), 0.0, 1.0)
    return below * above


def hsv_smoke_score(
    img: np.ndarray,
    sat_max: float = 0.25,
    value_band: tuple[float, float] = (0.35, 0.95),
    value_soft: float = 0.15,
    spread_max: float = 0.12,
) -> np.ndarray:
    """Soft smoke-likelihood map in [0, 1] from achromaticity cues.

    score = lowSat * bandValue * lowSpread, where
      lowSat    = clip(1 - S / sat_max, 0, 1)
      bandValue = soft indicator of V in value_band
      lowSpread = clip(1 - (max(RGB) - min(RGB)) / spread_max, 0, 1)

    Defaults are the a-priori values frozen in configs/eval_protocol.yaml; they encode
    "gray, mid-bright, achromatic" and nothing else. No component is learned.
    """
    img = np.asarray(img, dtype=np.float64)
    hsv = rgb_to_hsv(img)
    s, v = hsv[..., 1], hsv[..., 2]
    spread = img.max(axis=2) - img.min(axis=2)

    low_sat = np.clip(1.0 - s / max(sat_max, 1e-12), 0.0, 1.0)
    band_v = _band_score(v, value_band[0], value_band[1], value_soft)
    low_spread = np.clip(1.0 - spread / max(spread_max, 1e-12), 0.0, 1.0)
    return low_sat * band_v * low_spread


def hsv_smoke_mask(img: np.ndarray, threshold: float = 0.5, **kwargs) -> np.ndarray:
    """Binarized rule output under the protocol operating threshold."""
    return hsv_smoke_score(img, **kwargs) >= threshold
