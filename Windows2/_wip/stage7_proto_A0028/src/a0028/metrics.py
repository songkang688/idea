"""Aggregation utilities: Wilson intervals, arbitration index, Spearman rho."""

from __future__ import annotations

import math
from typing import Dict, List, Sequence, Tuple


def wilson_ci(k: int, n: int, z: float = 1.96) -> Tuple[float, float]:
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    denom = 1.0 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    half = (z / denom) * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))
    return (max(0.0, center - half), min(1.0, center + half))


def rate_with_ci(k: int, n: int) -> Dict[str, float]:
    lo, hi = wilson_ci(k, n)
    return {"rate": (k / n) if n else 0.0, "ci_lo": lo, "ci_hi": hi, "k": k, "n": n}


def location_prior_index(follow_place_rates: Sequence[float]) -> float:
    """Scalar 'area under the arbitration curve': mean P(follow-place) over a
    fixed probe grid. Comparable across trackers only on the same grid."""
    if not follow_place_rates:
        return float("nan")
    return float(sum(follow_place_rates) / len(follow_place_rates))


def _ranks(xs: Sequence[float]) -> List[float]:
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        mean_rank = (i + j) / 2.0 + 1.0
        for t in range(i, j + 1):
            ranks[order[t]] = mean_rank
        i = j + 1
    return ranks


def spearman_rho(xs: Sequence[float], ys: Sequence[float]) -> float:
    """Spearman rank correlation (tie-aware, no scipy dependency)."""
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("need two equal-length sequences of length >= 2")
    rx, ry = _ranks(xs), _ranks(ys)
    mx = sum(rx) / len(rx)
    my = sum(ry) / len(ry)
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    vx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    vy = math.sqrt(sum((b - my) ** 2 for b in ry))
    if vx == 0 or vy == 0:
        return float("nan")
    return cov / (vx * vy)
