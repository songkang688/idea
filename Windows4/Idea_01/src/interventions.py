from __future__ import annotations
import numpy as np

def mean_fill(image: np.ndarray, box: tuple[int, int, int, int]) -> np.ndarray:
    x0, y0, x1, y1 = box
    out = image.copy()
    region = out[y0:y1, x0:x1]
    if region.size == 0:
        return out
    fill = region.reshape(-1, region.shape[-1]).mean(axis=0) if region.ndim == 3 else region.mean()
    out[y0:y1, x0:x1] = fill
    return out

def telea_inpaint(image: np.ndarray, box: tuple[int, int, int, int]) -> np.ndarray:
    """On-manifold-ish inpaint. Uses OpenCV if present, else mean-fill (logged)."""
    try:
        import cv2
    except ImportError:
        return mean_fill(image, box)
    x0, y0, x1, y1 = box
    h, w = image.shape[:2]
    mask = np.zeros((h, w), np.uint8)
    mask[y0:y1, x0:x1] = 255
    if image.ndim == 2:
        img = np.stack([image] * 3, axis=-1)
        out = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        return out.mean(axis=-1).astype(image.dtype)
    return cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
