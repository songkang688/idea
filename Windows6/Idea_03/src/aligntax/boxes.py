"""Box parsing and IoU.

Parsing is where the format confound lives. A chat model that answers
"Sure! The cat is at [12, 30, 44, 80]" has localised correctly and been scored
zero by a strict parser. `parse_box` is deliberately permissive about wrappers
and separators so that a *parsing* failure is distinguishable from a
*localisation* failure — the distinction the whole paper rests on.
"""

from __future__ import annotations

import re

import numpy as np

_NUMBER = re.compile(r"-?\d+(?:\.\d+)?")


def parse_box(text: str) -> np.ndarray | None:
    """Extract an (x1, y1, x2, y2) box from free text, or None.

    Permissive on purpose: strips prose, brackets, commas and labels. Returns
    None only when the output does not contain four numbers, which is a genuine
    format failure rather than a strict-parser artifact.

    Takes the FIRST four numbers. A model emitting several boxes is answering a
    different question than the one asked, and silently picking the best of them
    would flatter the chat checkpoint.
    """
    if text is None:
        return None
    found = _NUMBER.findall(text)
    if len(found) < 4:
        return None
    box = np.array([float(v) for v in found[:4]], dtype=np.float64)
    x1, y1, x2, y2 = box
    return np.array([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)])


def format_xyxy(box: np.ndarray, precision: int = 1) -> str:
    """Canonical bare `x1 y1 x2 y2` string — what constrained decoding emits."""
    return " ".join(f"{v:.{precision}f}" for v in np.asarray(box, dtype=np.float64))


def iou(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0.0, ix2 - ix1) * max(0.0, iy2 - iy1)
    area_a = max(0.0, a[2] - a[0]) * max(0.0, a[3] - a[1])
    area_b = max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])
    union = area_a + area_b - inter
    return float(inter / union) if union > 0 else 0.0
