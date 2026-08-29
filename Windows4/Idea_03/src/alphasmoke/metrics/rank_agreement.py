"""Rank agreement for the P096 tau matrix (metrics_protocol.md section 3).

Pipeline
--------
1. Per-image scores per (checkpoint, metric) -> dataset score per checkpoint.
2. Sign alignment: lower-better metrics are negated so tau = +1 always means
   "identical quality ordering".
3. Tie-aware Kendall tau-b for every metric pair -> symmetric tau matrix.
4. Top-k reversal enumeration (the qualitative payload: which models are top-3 under
   one metric but not the other).
5. Image-level bootstrap CIs for tau.

Pre-registered kill conditions consuming this module (experiments.md section 2):
K-B1 (mMse-on-binary vs alpha-MAE cell), K-B2 (all binary<->alpha cells), K-B3
(synthetic-vs-measured ranking agreement).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import stats

# Direction registry: +1 = higher is better, -1 = lower is better.
# Any metric fed to tau_matrix must be registered here or passed explicitly —
# a silent wrong sign would fabricate reversals.
METRIC_DIRECTIONS: dict[str, int] = {
    "iou": +1,
    "dice": +1,
    "f_beta": +1,
    "boundary_f": +1,
    "mmse": -1,
    "mae": -1,
    "sad": -1,
    "mse": -1,
    "grad": -1,
    "conn": -1,
}


def _aligned(scores: np.ndarray, metric: str, directions: dict[str, int]) -> np.ndarray:
    if metric not in directions:
        raise KeyError(
            f"metric '{metric}' has no registered direction; add it to METRIC_DIRECTIONS "
            "or pass `directions` explicitly"
        )
    return scores * directions[metric]


def kendall_tau(
    scores_a: np.ndarray,
    scores_b: np.ndarray,
    metric_a: str,
    metric_b: str,
    directions: dict[str, int] | None = None,
) -> float:
    """Sign-aligned Kendall tau-b between two per-checkpoint score vectors."""
    directions = METRIC_DIRECTIONS if directions is None else directions
    a = _aligned(np.asarray(scores_a, dtype=float), metric_a, directions)
    b = _aligned(np.asarray(scores_b, dtype=float), metric_b, directions)
    if a.shape != b.shape or a.ndim != 1:
        raise ValueError("score vectors must be 1-D and same length (one entry per checkpoint)")
    if len(a) < 3:
        raise ValueError("tau over fewer than 3 checkpoints is not meaningful")
    tau, _ = stats.kendalltau(a, b)
    return float(tau)


def tau_matrix(
    dataset_scores: dict[str, np.ndarray],
    directions: dict[str, int] | None = None,
) -> tuple[list[str], np.ndarray]:
    """Symmetric tau matrix over all metric pairs.

    Parameters
    ----------
    dataset_scores : {metric_name: array of shape (n_checkpoints,)}
        Dataset-level score per checkpoint under each metric (same checkpoint order
        in every vector).

    Returns
    -------
    (metric_names, matrix) with matrix[i, j] = tau(metric_i, metric_j).
    """
    metrics = sorted(dataset_scores)
    n = len(metrics)
    m = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            t = kendall_tau(
                dataset_scores[metrics[i]],
                dataset_scores[metrics[j]],
                metrics[i],
                metrics[j],
                directions,
            )
            m[i, j] = m[j, i] = t
    return metrics, m


@dataclass
class Reversal:
    """A checkpoint in the top-k under metric_a but not under metric_b."""

    checkpoint: str
    metric_a: str
    metric_b: str
    rank_a: int  # 1-based rank under metric_a (quality order)
    rank_b: int  # 1-based rank under metric_b


def _quality_ranks(scores: np.ndarray, metric: str, directions: dict[str, int]) -> np.ndarray:
    """1-based ranks, rank 1 = best, after sign alignment."""
    aligned = _aligned(np.asarray(scores, dtype=float), metric, directions)
    order = np.argsort(-aligned, kind="stable")
    ranks = np.empty(len(aligned), dtype=int)
    ranks[order] = np.arange(1, len(aligned) + 1)
    return ranks


def top_k_reversals(
    dataset_scores: dict[str, np.ndarray],
    checkpoint_names: list[str],
    metric_a: str,
    metric_b: str,
    k: int = 3,
    directions: dict[str, int] | None = None,
) -> list[Reversal]:
    """Checkpoints in the top-k under metric_a but outside the top-k under metric_b.

    Run in both directions ((a,b) and (b,a)) at report time; this function returns
    the a->b direction only, so the caller controls the table layout.
    """
    directions = METRIC_DIRECTIONS if directions is None else directions
    ra = _quality_ranks(dataset_scores[metric_a], metric_a, directions)
    rb = _quality_ranks(dataset_scores[metric_b], metric_b, directions)
    out: list[Reversal] = []
    for idx, name in enumerate(checkpoint_names):
        if ra[idx] <= k < rb[idx]:
            out.append(Reversal(name, metric_a, metric_b, int(ra[idx]), int(rb[idx])))
    return sorted(out, key=lambda r: r.rank_a)


def bootstrap_tau(
    per_image_scores: dict[str, np.ndarray],
    metric_a: str,
    metric_b: str,
    n_boot: int = 10_000,
    ci: float = 0.95,
    directions: dict[str, int] | None = None,
    aggregate=np.mean,
    rng: np.random.Generator | None = None,
) -> dict:
    """Image-level bootstrap CI for tau between two metrics.

    Parameters
    ----------
    per_image_scores : {metric_name: array of shape (n_checkpoints, n_images)}
        Per-image scores; images are the resampling unit (experiments.md
        section 5).

    Returns
    -------
    dict with point estimate, (lo, hi) percentile CI, and n_boot.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    a = np.asarray(per_image_scores[metric_a], dtype=float)
    b = np.asarray(per_image_scores[metric_b], dtype=float)
    if a.shape != b.shape or a.ndim != 2:
        raise ValueError("per-image scores must be (n_checkpoints, n_images) and matched")
    n_images = a.shape[1]

    point = kendall_tau(aggregate(a, axis=1), aggregate(b, axis=1), metric_a, metric_b, directions)
    taus = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n_images, size=n_images)
        taus[i] = kendall_tau(
            aggregate(a[:, idx], axis=1),
            aggregate(b[:, idx], axis=1),
            metric_a,
            metric_b,
            directions,
        )
    alpha_tail = (1 - ci) / 2
    lo, hi = np.quantile(taus, [alpha_tail, 1 - alpha_tail])
    return {"tau": point, "ci": (float(lo), float(hi)), "n_boot": n_boot}
