"""Compatibility shim — the HSV floor now lives in alphasmoke.baselines.color_hsv.

The initial skeleton shipped a minimal saturation/value rule here; the full protocol
implementation (soft score, frozen a-priori parameters, uint8 support via [0,1]
conversion) is in the package. This shim keeps the original entry point importable.
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))

from alphasmoke.baselines.color_hsv import (  # noqa: E402,F401
    hsv_smoke_mask as _hsv_smoke_mask_float,
    hsv_smoke_score,
    rgb_to_hsv,
)


def hsv_smoke_mask(image_rgb: np.ndarray, threshold: float = 0.5, **kwargs) -> np.ndarray:
    """Skeleton-compatible wrapper: accepts uint8 [0,255] or float [0,1] RGB."""
    img = np.asarray(image_rgb)
    if img.dtype == np.uint8:
        img = img.astype(np.float64) / 255.0
    return _hsv_smoke_mask_float(img, threshold=threshold, **kwargs).astype(np.uint8)


if __name__ == "__main__":
    gray_plume = np.full((32, 32, 3), 220, dtype=np.uint8)
    print(float(hsv_smoke_mask(gray_plume).mean()))
