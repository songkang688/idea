"""Inference for the audit: episode bootstrap, the floor test, leaderboard shift.

The pre-registered decision rule (proposal.md section 17) has two legs, and both
are evaluated here. Leg (a) is a threshold on stratum-level retention. Leg (b) is
an overlap test between a method's correct-support accuracy and a support-free
floor. Leg (b) is run once per floor and never pooled, because pooling would hide
exactly the dependence reviewer attack A2 is about.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from .metrics import EpisodeMeasurement

DEFAULT_B = 10_000
RETENTION_THRESHOLD = 0.5  # killer experiment leg (a)


@dataclass(frozen=True)
class Interval:
    point: float
    lo: float
    hi: float

    def overlaps(self, other: "Interval") -> bool:
        return not (self.hi < other.lo or other.hi < self.lo)


def bootstrap_median(
    values: Sequence[float], *, n_boot: int = DEFAULT_B, alpha: float = 0.05, seed: int = 0
) -> Interval:
    """Percentile bootstrap over episodes, which is the resampling unit."""
    vals = np.asarray([v for v in values if np.isfinite(v)], dtype=float)
    if vals.size == 0:
        return Interval(float("nan"), float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, vals.size, size=(n_boot, vals.size))
    boots = np.median(vals[idx], axis=1)
    lo, hi = np.quantile(boots, [alpha / 2, 1 - alpha / 2])
    return Interval(float(np.median(vals)), float(lo), float(hi))


def bootstrap_mean(
    values: Sequence[float], *, n_boot: int = DEFAULT_B, alpha: float = 0.05, seed: int = 0
) -> Interval:
    vals = np.asarray([v for v in values if np.isfinite(v)], dtype=float)
    if vals.size == 0:
        return Interval(float("nan"), float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, vals.size, size=(n_boot, vals.size))
    boots = vals[idx].mean(axis=1)
    lo, hi = np.quantile(boots, [alpha / 2, 1 - alpha / 2])
    return Interval(float(vals.mean()), float(lo), float(hi))


def bootstrap_ratio_of_means(
    numer: Sequence[float],
    denom: Sequence[float],
    *,
    n_boot: int = DEFAULT_B,
    alpha: float = 0.05,
    seed: int = 0,
) -> Interval:
    """Aggregate retention: mean(wrong-support IoU) / mean(correct-support IoU).

    This is the PRIMARY stratum-level statistic and it is not the median of the
    per-episode ratios. The per-episode ratio distribution is strongly bimodal --
    a method either lands on the right object under a wrong support or it does
    not, so R(e) piles up near 0 and near 1 with little mass between. A median
    over such a distribution is a coin flip on which pile is larger: it reports
    1.000 or 0.000 and moves discontinuously with one episode. The ratio of means
    is stable, has the interpretation the paper actually wants ("what share of
    accuracy survives destroying the support"), and bootstraps cleanly because
    numerator and denominator are resampled on the same episode indices.

    The median of per-episode ratios is still reported as a secondary robust
    statistic, because the two disagreeing is itself diagnostic.
    """
    num = np.asarray(numer, dtype=float)
    den = np.asarray(denom, dtype=float)
    if num.shape != den.shape:
        raise ValueError("numerator and denominator must be paired per episode")
    ok = np.isfinite(num) & np.isfinite(den)
    num, den = num[ok], den[ok]
    if num.size == 0 or den.sum() <= 0:
        return Interval(float("nan"), float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, num.size, size=(n_boot, num.size))
    den_boot = den[idx].sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        boots = np.where(den_boot > 0, num[idx].sum(axis=1) / den_boot, np.nan)
    boots = boots[np.isfinite(boots)]
    if boots.size == 0:
        return Interval(float(num.sum() / den.sum()), float("nan"), float("nan"))
    lo, hi = np.quantile(boots, [alpha / 2, 1 - alpha / 2])
    return Interval(float(num.sum() / den.sum()), float(lo), float(hi))


@dataclass(frozen=True)
class StratumResult:
    method: str
    benchmark: str
    stratum: str
    n_episodes: int
    n_after_tau: int
    retention: Interval  # PRIMARY: ratio of means
    retention_median: Interval  # SECONDARY: median of per-episode ratios
    sss: float
    flip_rate: float
    acc_correct: Interval
    floor_strong: Interval
    floor_weak: Interval

    def fails_floor(self, which: str) -> bool:
        """Leg (b): correct-support accuracy indistinguishable from the floor."""
        floor = self.floor_strong if which == "strong" else self.floor_weak
        return self.acc_correct.overlaps(floor)

    @property
    def estimators_disagree(self) -> bool:
        """Primary and secondary retention landing far apart means the per-episode
        distribution is bimodal, which is reportable rather than a nuisance."""
        if not (np.isfinite(self.retention.point) and np.isfinite(self.retention_median.point)):
            return False
        return abs(self.retention.point - self.retention_median.point) > 0.2


def summarise(
    measurements: Sequence[EpisodeMeasurement],
    *,
    method: str,
    benchmark: str,
    stratum: str,
    tau: float,
    seed: int = 0,
) -> StratumResult:
    kept = [m for m in measurements if m.keep_for_retention(tau)]
    retention = bootstrap_ratio_of_means(
        [m.wrong_median for m in kept], [m.a_corr for m in kept], seed=seed
    )
    return StratumResult(
        method=method,
        benchmark=benchmark,
        stratum=stratum,
        n_episodes=len(measurements),
        n_after_tau=len(kept),
        retention=retention,
        retention_median=bootstrap_median([m.retention for m in kept], seed=seed),
        sss=1.0 - retention.point if np.isfinite(retention.point) else float("nan"),
        flip_rate=float(np.mean([m.flipped for m in kept])) if kept else float("nan"),
        acc_correct=bootstrap_mean([m.a_corr for m in measurements], seed=seed),
        floor_strong=bootstrap_mean([m.a_floor_strong for m in measurements], seed=seed),
        floor_weak=bootstrap_mean([m.a_floor_weak for m in measurements], seed=seed),
    )


def kendall_tau(order_a: Sequence[str], order_b: Sequence[str]) -> float:
    """Rank correlation between two leaderboards over the same method set."""
    if set(order_a) != set(order_b):
        raise ValueError("leaderboards must rank the same methods")
    rank_b = {m: i for i, m in enumerate(order_b)}
    n = len(order_a)
    if n < 2:
        return float("nan")
    concordant = discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = rank_b[order_a[i]] - rank_b[order_a[j]]
            if s < 0:
                concordant += 1
            elif s > 0:
                discordant += 1
    return (concordant - discordant) / (0.5 * n * (n - 1))


def positions_changed(order_a: Sequence[str], order_b: Sequence[str]) -> int:
    return sum(1 for i, m in enumerate(order_a) if order_b[i] != m)


@dataclass(frozen=True)
class KillerVerdict:
    leg_a_pass: bool
    leg_b_pass_strong: bool
    leg_b_pass_weak: bool
    n_specialists: int
    n_specialists_retaining: int
    detail: str

    @property
    def headline_survives(self) -> bool:
        """Both legs failing means the headline is dead and the certification
        result is published instead (proposal.md section 20)."""
        return self.leg_a_pass or self.leg_b_pass_strong or self.leg_b_pass_weak


def evaluate_killer(
    results: Sequence[StratumResult], specialist_methods: set[str]
) -> KillerVerdict:
    """Apply the pre-registered decision rule on the S3 distractor stratum."""
    spec = [r for r in results if r.method in specialist_methods]
    retaining = [r for r in spec if r.retention.point > RETENTION_THRESHOLD]
    leg_a = len(spec) > 0 and len(retaining) >= len(spec) / 2
    leg_b_strong = any(r.fails_floor("strong") for r in spec)
    leg_b_weak = any(r.fails_floor("weak") for r in spec)
    detail = (
        f"{len(retaining)}/{len(spec)} specialists retain R>{RETENTION_THRESHOLD}; "
        f"floor-overlap strong={leg_b_strong} weak={leg_b_weak}"
    )
    return KillerVerdict(
        leg_a_pass=leg_a,
        leg_b_pass_strong=leg_b_strong,
        leg_b_pass_weak=leg_b_weak,
        n_specialists=len(spec),
        n_specialists_retaining=len(retaining),
        detail=detail,
    )
