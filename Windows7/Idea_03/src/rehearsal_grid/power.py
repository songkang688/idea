"""Power gate and denominator adequacy -- the two checks that run BEFORE the grid.

Reviewer attack A2: Vicuna-7B is near-floor on GSM8K and weak on IFEval. Retention
is score/score(base), so a stratum whose base score is near zero produces a ratio
dominated by noise, and the >=3-of-4 decision rule can then be flipped by a single
unstable stratum. The original Stage-5 abort gate watched only seed variance on
A0/A1; it never asked whether a stratum's denominator was usable at all.

Both checks are applied before the 15 arms run, so a bad stratum is *replaced*
rather than explained away afterwards.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass(frozen=True)
class StratumScores:
    """Per-seed scores for one capability under one arm."""

    capability: str
    arm: str
    base_score: float
    scores: tuple[float, ...]

    @property
    def mean(self) -> float:
        return float(np.mean(self.scores))

    @property
    def sd(self) -> float:
        # Sample sd; with 2 seeds this is a crude estimate and the report says so.
        return float(np.std(self.scores, ddof=1)) if len(self.scores) > 1 else 0.0

    @property
    def absolute(self) -> float:
        """CO-PRIMARY: delta from the base model, in score points."""
        return self.mean - self.base_score

    @property
    def retention(self) -> float:
        """SECONDARY: ratio to the base model. Unstable near a zero denominator."""
        return self.mean / self.base_score if abs(self.base_score) > 1e-9 else float("nan")


@dataclass(frozen=True)
class DenominatorGate:
    """Is this stratum's base score far enough from floor to support a ratio?"""

    capability: str
    base_score: float
    chance_level: float
    seed_sd: float
    min_headroom: float = 0.10
    min_snr: float = 3.0

    @property
    def headroom(self) -> float:
        return self.base_score - self.chance_level

    @property
    def snr(self) -> float:
        return self.headroom / self.seed_sd if self.seed_sd > 1e-9 else float("inf")

    @property
    def usable(self) -> bool:
        return self.headroom >= self.min_headroom and self.snr >= self.min_snr

    def verdict(self) -> str:
        if self.usable:
            return "ok"
        if self.headroom < self.min_headroom:
            return f"FLOOR (headroom {self.headroom:+.3f} over chance {self.chance_level:.2f})"
        return f"NOISY (snr {self.snr:.1f} < {self.min_snr})"


@dataclass
class PowerReport:
    mde: float
    per_capability: dict[str, tuple[float, float, bool]] = field(default_factory=dict)

    @property
    def passes(self) -> bool:
        """P0 requires the gate-relevant strata to clear it."""
        return all(ok for _, _, ok in self.per_capability.values())

    def render(self) -> str:
        lines = [
            f"P0 power gate  (declared MDE = {self.mde:+.3f} absolute points)",
            f"{'capability':<22}{'A1-A0 (abs)':>14}{'2 x seed sd':>14}  verdict",
        ]
        for cap, (gap, thresh, ok) in self.per_capability.items():
            lines.append(
                f"{cap:<22}{gap:>+14.4f}{thresh:>14.4f}  {'PASS' if ok else 'FAIL'}"
            )
        lines.append(f"P0: {'PASS -- run the full grid' if self.passes else 'FAIL -- stop'}")
        return "\n".join(lines)


def power_check(
    a0: dict[str, StratumScores],
    a1: dict[str, StratumScores],
    *,
    mde: float,
    gate_capabilities: tuple[str, ...] = ("knowledge", "fluency"),
) -> PowerReport:
    """P0, on absolute deltas.

    `mde` is declared before the six E1 runs, not fitted to them. A gap must clear
    BOTH the declared minimum detectable effect and twice the observed seed spread:
    the first stops us from calling a trivially small effect real, the second stops
    us from calling a noisy one real.
    """
    report = PowerReport(mde=mde)
    for cap in gate_capabilities:
        if cap not in a0 or cap not in a1:
            report.per_capability[cap] = (float("nan"), float("nan"), False)
            continue
        gap = a1[cap].mean - a0[cap].mean
        pooled = float(np.sqrt(0.5 * (a0[cap].sd ** 2 + a1[cap].sd ** 2)))
        thresh = 2.0 * pooled
        report.per_capability[cap] = (gap, thresh, gap >= max(thresh, mde))
    return report
