"""Standard greedy non-maximum suppression (class-agnostic)."""

from __future__ import annotations

import numpy as np

from .boxes import iou_matrix


def greedy_nms(
    boxes: np.ndarray,
    scores: np.ndarray,
    iou_thresh: float,
    score_floor: float = 0.0,
) -> np.ndarray:
    """Greedy NMS. Returns indices of kept boxes, sorted by descending score.

    Semantics match the textbook algorithm: iterate candidates in descending
    score order; keep a box iff it is not suppressed; a kept box suppresses
    every lower-scoring box with IoU >= ``iou_thresh``. Boxes with score below
    ``score_floor`` are discarded up front (the usual deployment score cut).
    Only *kept* boxes suppress — suppression never chains through suppressed
    boxes. That property matters for the CPS coverage proof (suppression.py).
    """
    boxes = np.asarray(boxes, dtype=np.float64).reshape(-1, 4)
    scores = np.asarray(scores, dtype=np.float64).ravel()
    if boxes.shape[0] != scores.shape[0]:
        raise ValueError("boxes and scores length mismatch")

    valid = np.flatnonzero(scores >= score_floor)
    if valid.size == 0:
        return np.empty(0, dtype=np.int64)

    order = valid[np.argsort(-scores[valid], kind="stable")]
    ious = iou_matrix(boxes[order], boxes[order])

    suppressed = np.zeros(order.size, dtype=bool)
    keep_local: list[int] = []
    for i in range(order.size):
        if suppressed[i]:
            continue
        keep_local.append(i)
        suppressed[i + 1 :] |= ious[i, i + 1 :] >= iou_thresh
    return order[np.asarray(keep_local, dtype=np.int64)]
