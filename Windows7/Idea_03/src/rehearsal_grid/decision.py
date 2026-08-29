"""The pre-registered decision rule: P1 (mechanism), P2 (content), P3 (stratified).

The rule reads absolute deltas as co-primary with retention ratios. Where the ratio
form is unstable -- P1 is a ratio of differences, and its denominator is the very
quantity P0 just showed to be small -- the rule refuses to interpret it rather than
reporting a number it cannot support.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .power import StratumScores

BALANCE_SHARE_THRESHOLD = 0.8
CONTENT_HIGH = 0.5
CONTENT_LOW = 0.2
MIN_CAPABILITIES_FOR_P1 = 3


@dataclass(frozen=True)
class Effects:
    capability: str
    total: float
    balance: float
    content: float
    interpretable: bool
    reason: str = ""

    @property
    def balance_share(self) -> float:
        if not self.interpretable:
            return float("nan")
        return self.balance / self.total

    @property
    def content_share(self) -> float:
        if not self.interpretable:
            return float("nan")
        return self.content / self.total


@dataclass
class Decision:
    effects: dict[str, Effects] = field(default_factory=dict)
    mde: float = 0.0

    @property
    def interpretable(self) -> dict[str, Effects]:
        return {k: v for k, v in self.effects.items() if v.interpretable}

    @property
    def p1_mechanism(self) -> bool:
        ok = [
            e for e in self.interpretable.values()
            if e.balance_share >= BALANCE_SHARE_THRESHOLD
        ]
        return len(ok) >= MIN_CAPABILITIES_FOR_P1

    @property
    def p2_content(self) -> bool:
        """Every capability: random web rehearsal is no better than none at all."""
        return bool(self.effects) and all(e.balance <= 0.0 for e in self.effects.values())

    @property
    def p3_stratified(self) -> bool:
        i = self.interpretable
        know = i.get("knowledge")
        flu = i.get("fluency")
        if know is None or flu is None:
            return False
        return know.content_share > CONTENT_HIGH and flu.content_share < CONTENT_LOW

    @property
    def underpowered(self) -> bool:
        """No capability cleared the declared MDE.

        This is P0 failing, seen from the decision rule's side. It has to be checked
        before the branches, or a world with no effect at all falls through to
        "MIXED" and reads as an inconclusive result rather than as the gate working.
        """
        return bool(self.effects) and not self.interpretable

    def verdict(self) -> str:
        if self.underpowered:
            return (
                f"NO POWER -- every total effect is below the declared MDE ({self.mde:.3f}). "
                "The rule declines to answer. Stop for <1K A100-h and publish the power "
                "analysis: it bounds how large multimodal linguistic forgetting actually is."
            )
        if self.p2_content:
            return (
                "P2 -- CONTENT CAMP. Content-free rehearsal does not help anywhere. "
                "First controlled refutation of pseudo-rehearsal in the multimodal regime."
            )
        if self.p1_mechanism:
            return (
                "P1 -- MECHANISM. Rehearsal is gradient rebalancing; curation budgets "
                "are misdirected and a balance term should suffice."
            )
        if self.p3_stratified:
            return (
                "P3 -- STRATIFIED. Fluency runs on any text-shaped gradient, knowledge "
                "needs real content. Fund the mixture sweep (E4) for the dosing recipe."
            )
        return (
            "MIXED -- no pre-registered branch fires cleanly. Report the decomposition "
            "and the mixture sweep; do not retrofit a rule."
        )

    def render(self) -> str:
        lines = [
            f"{'capability':<18}{'total':>9}{'balance':>9}{'content':>9}"
            f"{'bal%':>8}{'cont%':>8}  note",
        ]
        for cap, e in self.effects.items():
            if e.interpretable:
                lines.append(
                    f"{cap:<18}{e.total:>+9.4f}{e.balance:>+9.4f}{e.content:>+9.4f}"
                    f"{e.balance_share:>8.2f}{e.content_share:>8.2f}"
                )
            else:
                lines.append(
                    f"{cap:<18}{e.total:>+9.4f}{e.balance:>+9.4f}{e.content:>+9.4f}"
                    f"{'--':>8}{'--':>8}  {e.reason}"
                )
        lines += [
            "",
            f"P1 mechanism  : {self.p1_mechanism}",
            f"P2 content    : {self.p2_content}",
            f"P3 stratified : {self.p3_stratified}",
            "",
            self.verdict(),
        ]
        return "\n".join(lines)


def evaluate(
    a0: dict[str, StratumScores],
    a1: dict[str, StratumScores],
    a2: dict[str, StratumScores],
    *,
    mde: float,
) -> Decision:
    """Compute the three effects per capability and apply the frozen rule.

    Everything is in absolute score points. The shares are ratios of those, and are
    left uncomputed for any capability whose total effect is below the declared MDE:
    dividing by a gap the power analysis just called indistinguishable from zero
    produces a share that swings between -8 and +8 on seed noise.
    """
    decision = Decision(mde=mde)
    for cap in a0:
        if cap not in a1 or cap not in a2:
            continue
        total = a1[cap].mean - a0[cap].mean
        balance = a2[cap].mean - a0[cap].mean
        content = a1[cap].mean - a2[cap].mean
        ok = abs(total) >= mde
        decision.effects[cap] = Effects(
            capability=cap,
            total=total,
            balance=balance,
            content=content,
            interpretable=ok,
            reason="" if ok else f"|total| < MDE {mde:.3f}; shares uninterpretable",
        )
    return decision


def bootstrap_share(
    numer_seeds: list[float],
    denom_seeds: list[float],
    *,
    n_boot: int = 10_000,
    seed: int = 0,
) -> tuple[float, float, float]:
    """Percentile CI for a share, resampling seeds jointly.

    With three seeds this interval is wide and honest rather than precise. Reporting
    it is what keeps `balance_share = 0.83` from being read as a measurement when it
    is really 0.83 [0.31, 1.42].
    """
    rng = np.random.default_rng(seed)
    n = min(len(numer_seeds), len(denom_seeds))
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    num = np.asarray(numer_seeds[:n], dtype=float)
    den = np.asarray(denom_seeds[:n], dtype=float)
    idx = rng.integers(0, n, size=(n_boot, n))
    shares = num[idx].mean(axis=1) / (den[idx].mean(axis=1) + 1e-12)
    point = float(num.mean() / (den.mean() + 1e-12))
    return point, float(np.percentile(shares, 2.5)), float(np.percentile(shares, 97.5))
