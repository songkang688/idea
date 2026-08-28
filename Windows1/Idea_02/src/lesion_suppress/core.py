from __future__ import annotations

import numpy as np
from scipy.ndimage import gaussian_filter


def insert_gaussian_lesion(
    image: np.ndarray,
    cy: int,
    cx: int,
    sigma: float,
    cnr: float,
    noise_std: float | None = None,
) -> np.ndarray:
    """Add a 2D Gaussian blob with approximate CNR = peak / noise_std."""
    img = image.astype(np.float32).copy()
    if noise_std is None:
        noise_std = float(img.std() + 1e-6)
    peak = cnr * noise_std
    yy, xx = np.mgrid[0 : img.shape[0], 0 : img.shape[1]]
    blob = peak * np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * sigma**2))
    return img + blob.astype(np.float32)


def simple_denoise(image: np.ndarray, strength: float) -> np.ndarray:
    """Placeholder enhancement: Gaussian blur. Replace with DnCNN in real runs."""
    return gaussian_filter(image.astype(np.float32), sigma=float(strength))


def detect_blob(image: np.ndarray, cy: int, cx: int, radius: int, thresh: float) -> bool:
    y0, y1 = max(0, cy - radius), min(image.shape[0], cy + radius + 1)
    x0, x1 = max(0, cx - radius), min(image.shape[1], cx + radius + 1)
    return float(image[y0:y1, x0:x1].max()) >= thresh


def suppression_event(
    raw: np.ndarray,
    enhanced: np.ndarray,
    cy: int,
    cx: int,
    radius: int,
    thresh: float,
) -> bool:
    return detect_blob(raw, cy, cx, radius, thresh) and not detect_blob(
        enhanced, cy, cx, radius, thresh
    )


def kendall_tau(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a).ravel()
    b = np.asarray(b).ravel()
    n = len(a)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            da, db = np.sign(a[i] - a[j]), np.sign(b[i] - b[j])
            if da * db > 0:
                conc += 1
            elif da * db < 0:
                disc += 1
    den = conc + disc
    return 0.0 if den == 0 else (conc - disc) / den
