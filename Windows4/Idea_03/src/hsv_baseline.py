"""Cheap physics/color baseline — often the honest SOTA on white smoke."""
from __future__ import annotations
import numpy as np
try:
    from PIL import Image
except ImportError:
    Image = None

def hsv_smoke_mask(image_rgb: np.ndarray, sat_min: float = 0.08, val_min: float = 0.35) -> np.ndarray:
    """Heuristic: low saturation, mid-high value (gray/white plume). Not a learned model."""
    x = image_rgb.astype(np.float32) / 255.0
    mx = x.max(axis=-1)
    mn = x.min(axis=-1)
    sat = np.where(mx == 0, 0, (mx - mn) / np.clip(mx, 1e-6, None))
    val = mx
    return ((sat < sat_min) & (val > val_min)).astype(np.uint8)

if __name__ == "__main__":
    img = np.full((32, 32, 3), 220, dtype=np.uint8)
    print(float(hsv_smoke_mask(img).mean()))
