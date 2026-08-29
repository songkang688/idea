"""Split-conformal calibration for detection candidate sets.

Construction (the pre-suppression conformal layer, module 3 of exp_05,
following the candidate-set reading of SeqCRC-style conformal OD):

  * Exchangeable unit: one GT object (pooled over i.i.d. scenes; see the
    exchangeability caveat in README.md).
  * Nonconformity of GT g given an available candidate pool C:
        s(g) = 1 - max{ score(c) : c in C, IoU(c, g) >= tau }
    and s(g) = +inf if no candidate in C covers g at IoU >= tau (for the
    post-NMS pool this is exactly the blind spot / detector-miss event —
    NO threshold can recover such an object).
  * q_hat = the ceil((n + 1) (1 - alpha))-th smallest calibration score
    (the standard finite-sample split-conformal quantile); q_hat = +inf when
    the index exceeds n or when the quantile lands on an uncovered object.
  * Prediction set on a new scene: { c : score(c) >= 1 - q_hat }
    (everything if q_hat = +inf).

Guarantee (marginal, over exchangeable GT objects):
    P( GT is covered at IoU >= tau by the prediction set ) >= 1 - alpha,
where "covered" is evaluated against the same candidate pool used at
calibration time. The point of the whole prototype: NMS changes the pool
*after* calibration, so the guarantee silently stops applying.
"""

from __future__ import annotations

import math

import numpy as np

from .boxes import iou_matrix
from .synthetic import Scene

INF = float("inf")


def covering_score_per_gt(
    gt_boxes: np.ndarray,
    cand_boxes: np.ndarray,
    cand_scores: np.ndarray,
    tau: float,
) -> np.ndarray:
    """Per-GT max candidate score among candidates with IoU >= tau (-inf if none)."""
    gt_boxes = np.asarray(gt_boxes, dtype=np.float64).reshape(-1, 4)
    n_gt = gt_boxes.shape[0]
    out = np.full(n_gt, -INF, dtype=np.float64)
    if n_gt == 0 or len(cand_boxes) == 0:
        return out
    ious = iou_matrix(gt_boxes, cand_boxes)  # (G, C)
    covers = ious >= tau
    scores = np.asarray(cand_scores, dtype=np.float64)
    for g in range(n_gt):
        idx = np.flatnonzero(covers[g])
        if idx.size:
            out[g] = float(scores[idx].max())
    return out


def nonconformity_scores(
    scenes: list[Scene],
    tau: float,
    candidate_filter=None,
) -> np.ndarray:
    """Pooled per-GT nonconformity scores over a list of scenes.

    ``candidate_filter(scene) -> index array`` restricts the candidate pool
    (e.g. to NMS survivors); None means the full pre-NMS cache.
    """
    all_scores: list[np.ndarray] = []
    for scene in scenes:
        if candidate_filter is None:
            boxes, scores = scene.cand_boxes, scene.cand_scores
        else:
            idx = np.asarray(candidate_filter(scene), dtype=np.int64)
            boxes, scores = scene.cand_boxes[idx], scene.cand_scores[idx]
        best = covering_score_per_gt(scene.gt_boxes, boxes, scores, tau)
        s = np.where(np.isneginf(best), INF, 1.0 - best)
        all_scores.append(s)
    if not all_scores:
        return np.zeros(0)
    return np.concatenate(all_scores)


def split_conformal_qhat(scores: np.ndarray, alpha: float) -> float:
    """Finite-sample split-conformal quantile; +inf when unachievable."""
    scores = np.asarray(scores, dtype=np.float64)
    n = scores.size
    if n == 0:
        return INF
    k = math.ceil((n + 1) * (1.0 - alpha))
    if k > n:
        return INF
    return float(np.sort(scores)[k - 1])  # +inf entries sort last


def prediction_mask(cand_scores: np.ndarray, qhat: float) -> np.ndarray:
    """Boolean mask over candidates: which ones are in the prediction set."""
    cand_scores = np.asarray(cand_scores, dtype=np.float64)
    if math.isinf(qhat):
        return np.ones(cand_scores.shape[0], dtype=bool)
    return cand_scores >= 1.0 - qhat


def object_coverage(
    gt_boxes: np.ndarray,
    cand_boxes: np.ndarray,
    cand_scores: np.ndarray,
    mask: np.ndarray,
    tau: float,
) -> np.ndarray:
    """Per-GT bool: is the GT covered (IoU >= tau) by any set member?"""
    gt_boxes = np.asarray(gt_boxes, dtype=np.float64).reshape(-1, 4)
    n_gt = gt_boxes.shape[0]
    idx = np.flatnonzero(np.asarray(mask, dtype=bool))
    if n_gt == 0:
        return np.zeros(0, dtype=bool)
    if idx.size == 0:
        return np.zeros(n_gt, dtype=bool)
    ious = iou_matrix(gt_boxes, np.asarray(cand_boxes)[idx])
    return (ious >= tau).any(axis=1)
