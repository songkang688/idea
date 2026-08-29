"""Predictive validity, done the way Stage 6 forced.

The original design asked whether the per-sequence reversible fraction correlates
with prevention-method gains at r > 0.6. That test can pass with no instrument
validity at all: reversible fraction and prevention gains are BOTH downstream of
generic sequence difficulty (distractor density, occlusion count, failure count,
natural recovery rate). A shared-difficulty confound produces exactly that
correlation. The skeptical-PI pass called this the strongest attack on the idea
and it was fatal as originally specified.

Two changes fix it, and both live here.

1. Partial correlation. Regress out the difficulty covariates from both sides
   before correlating. The pre-registered bar drops from raw r > 0.6 to partial
   r > 0.4, because partialling removes the shared component that inflated it.
2. Minimum over a frozen comparator set. "SAMURAI *and* DAM4SAM at r > 0.6"
   silently permits picking whichever comparator carries the headline. The
   reported statistic is the MINIMUM partial r across a comparator set named
   before any comparator is run.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

PARTIAL_R_THRESHOLD = 0.4


def _ols_residuals(y: np.ndarray, X: np.ndarray) -> np.ndarray:
    """Residuals of y after regressing on X (intercept added)."""
    n = y.shape[0]
    design = np.column_stack([np.ones(n), X]) if X.size else np.ones((n, 1))
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    return y - design @ coef


def partial_correlation(
    y: Sequence[float], x: Sequence[float], covariates: np.ndarray
) -> float:
    """corr(y - ŷ(Z), x - x̂(Z)) -- Pearson on the residuals."""
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    Z = np.asarray(covariates, dtype=float)
    if Z.ndim == 1:
        Z = Z[:, None]
    if not (y.shape[0] == x.shape[0] == Z.shape[0]):
        raise ValueError("y, x and covariates must have the same number of sequences")
    if y.shape[0] < 4:
        return float("nan")
    ry, rx = _ols_residuals(y, Z), _ols_residuals(x, Z)
    if ry.std() < 1e-12 or rx.std() < 1e-12:
        return float("nan")
    return float(np.corrcoef(ry, rx)[0, 1])


def bootstrap_partial_correlation(
    y: Sequence[float],
    x: Sequence[float],
    covariates: np.ndarray,
    *,
    n_boot: int = 5000,
    alpha: float = 0.05,
    seed: int = 0,
) -> tuple[float, float, float]:
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    Z = np.asarray(covariates, dtype=float)
    if Z.ndim == 1:
        Z = Z[:, None]
    point = partial_correlation(y, x, Z)
    rng = np.random.default_rng(seed)
    boots = []
    for _ in range(n_boot):
        idx = rng.integers(0, y.shape[0], size=y.shape[0])
        r = partial_correlation(y[idx], x[idx], Z[idx])
        if np.isfinite(r):
            boots.append(r)
    if not boots:
        return point, float("nan"), float("nan")
    lo, hi = np.quantile(boots, [alpha / 2, 1 - alpha / 2])
    return point, float(lo), float(hi)


def nested_model_gain(
    gain: Sequence[float], rho: Sequence[float], covariates: np.ndarray
) -> float:
    """Increase in R^2 from adding rho to a difficulty-only model.

    Reported alongside the partial correlation. If difficulty alone already
    explains the prevention gains, this is near zero and the instrument adds
    nothing, regardless of what the raw correlation says.
    """
    g = np.asarray(gain, dtype=float)
    Z = np.asarray(covariates, dtype=float)
    if Z.ndim == 1:
        Z = Z[:, None]
    r = np.asarray(rho, dtype=float)[:, None]

    def r2(X):
        resid = _ols_residuals(g, X)
        tss = float(((g - g.mean()) ** 2).sum())
        return 1.0 - float((resid**2).sum()) / tss if tss > 0 else float("nan")

    return r2(np.column_stack([Z, r])) - r2(Z)


@dataclass(frozen=True)
class ValidityVerdict:
    per_comparator: dict[str, tuple[float, float, float]]  # name -> (r, lo, hi)
    nested_gain: dict[str, float]
    min_partial_r: float
    threshold: float
    frozen_set: tuple[str, ...]

    @property
    def passes(self) -> bool:
        return np.isfinite(self.min_partial_r) and self.min_partial_r > self.threshold

    def report(self) -> str:
        lines = [
            f"frozen comparator set: {', '.join(self.frozen_set)}",
            f"{'comparator':<16}{'partial r [95% CI]':>28}{'nested dR2':>12}",
        ]
        for name in self.frozen_set:
            r, lo, hi = self.per_comparator[name]
            lines.append(
                f"{name:<16}{f'{r:.3f} [{lo:.3f},{hi:.3f}]':>28}"
                f"{self.nested_gain[name]:>12.3f}"
            )
        lines.append(
            f"min partial r = {self.min_partial_r:.3f} "
            f"(threshold {self.threshold}) -> {'PASS' if self.passes else 'FAIL'}"
        )
        return "\n".join(lines)


def evaluate_validity(
    rho: Sequence[float],
    comparator_gains: Mapping[str, Sequence[float]],
    covariates: np.ndarray,
    *,
    frozen_set: Sequence[str],
    threshold: float = PARTIAL_R_THRESHOLD,
    seed: int = 0,
) -> ValidityVerdict:
    """Apply the pre-registered validity rule.

    `frozen_set` must be named before any comparator is run. Passing a comparator
    that is not in the frozen set is an error rather than a convenience, because
    that is precisely the post-hoc freedom the rule exists to remove.
    """
    missing = [c for c in frozen_set if c not in comparator_gains]
    if missing:
        raise KeyError(f"frozen comparators missing from results: {missing}")
    extra = [c for c in comparator_gains if c not in frozen_set]
    if extra:
        raise ValueError(
            f"comparators not in the frozen pre-registered set: {extra}. "
            "Add them to the pre-registration or report them separately as exploratory."
        )

    per, nested = {}, {}
    for name in frozen_set:
        per[name] = bootstrap_partial_correlation(
            rho, comparator_gains[name], covariates, seed=seed
        )
        nested[name] = nested_model_gain(comparator_gains[name], rho, covariates)

    finite = [per[c][0] for c in frozen_set if np.isfinite(per[c][0])]
    return ValidityVerdict(
        per_comparator=per,
        nested_gain=nested,
        min_partial_r=min(finite) if finite else float("nan"),
        threshold=threshold,
        frozen_set=tuple(frozen_set),
    )
