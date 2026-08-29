"""Operational metrics: AP, FAR at a fixed recall, and event-clustered CIs.

`Idea_02/experiments.md` makes image-level AP and FAR@recall primary and IoU
secondary, because the operational question for a wildfire tower is "how many
false alarms at the recall we must hit", not "how tight is the box".
"""

from __future__ import annotations

import numpy as np


def average_precision(scores: np.ndarray, labels: np.ndarray) -> float:
    """Image-level AP by the step-wise precision-recall sum."""
    scores = np.asarray(scores, dtype=np.float64)
    labels = np.asarray(labels).astype(int)
    if labels.sum() == 0:
        return float("nan")
    order = np.argsort(-scores, kind="stable")
    y = labels[order]
    tp = np.cumsum(y)
    fp = np.cumsum(1 - y)
    recall = tp / labels.sum()
    precision = tp / np.maximum(tp + fp, 1)
    ap = 0.0
    prev_recall = 0.0
    for p, r in zip(precision, recall):
        ap += p * (r - prev_recall)
        prev_recall = r
    return float(ap)


def far_at_recall(scores: np.ndarray, labels: np.ndarray, target_recall: float = 0.8) -> float:
    """False-alarm rate among negatives at the threshold reaching target recall.

    Returns nan when the target recall is unreachable, rather than silently
    returning the closest achievable operating point.
    """
    scores = np.asarray(scores, dtype=np.float64)
    labels = np.asarray(labels).astype(int)
    n_pos, n_neg = int(labels.sum()), int((1 - labels).sum())
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    order = np.argsort(-scores, kind="stable")
    y = labels[order]
    tp = np.cumsum(y)
    fp = np.cumsum(1 - y)
    recall = tp / n_pos
    reached = np.where(recall >= target_recall)[0]
    if reached.size == 0:
        return float("nan")
    return float(fp[reached[0]] / n_neg)


def cluster_bootstrap_ci(
    values: np.ndarray,
    clusters: np.ndarray,
    rng: np.random.Generator,
    resamples: int = 200,
    alpha: float = 0.05,
) -> tuple[float, float]:
    """Percentile CI resampling whole clusters, not individual frames.

    Frames inside one event are heavily correlated — consecutive frames of the
    same plume from the same tower. A frame-level bootstrap would treat them as
    independent and report a CI several times too narrow, which is the specific
    way this kind of audit overstates its confidence. Resample events.
    """
    values = np.asarray(values, dtype=np.float64)
    clusters = np.asarray(clusters)
    unique = np.unique(clusters)
    if unique.size < 2:
        return (float("nan"), float("nan"))
    means = []
    for _ in range(resamples):
        drawn = rng.choice(unique, size=unique.size, replace=True)
        pooled = np.concatenate([values[clusters == c] for c in drawn])
        if pooled.size:
            means.append(pooled.mean())
    if not means:
        return (float("nan"), float("nan"))
    lo, hi = np.percentile(means, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return (float(lo), float(hi))
