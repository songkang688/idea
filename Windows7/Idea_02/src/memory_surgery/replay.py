"""Replay harness and the determinism gate.

Nothing in this project is interpretable unless the no-op arm reproduces the
original failure exactly. If replaying from t_r without any intervention gives a
different outcome than the original pass, then every arm difference is partly
harness noise. SAM2's video predictor caches make this a real risk rather than a
formality, so it is the first gate in the roadmap (E0) and it runs before any
science.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np

from .bank import MemoryBank
from .surgeon import ARMS, apply_arm


class ReplayDeterminismError(RuntimeError):
    """Raised when the no-op arm fails to reproduce the original outcome."""


@dataclass(frozen=True)
class ArmOutcome:
    arm: str
    recovered: bool
    bank_size: int
    mean_corruption: float


def check_replay_determinism(
    bank: MemoryBank,
    replay_fn: Callable[[MemoryBank], bool],
    *,
    n_repeats: int = 5,
) -> None:
    """The gate. Replaying an untouched bank must give one stable answer."""
    outcomes = {replay_fn(bank.copy()) for _ in range(n_repeats)}
    if len(outcomes) != 1:
        raise ReplayDeterminismError(
            f"no-op replay produced {outcomes} across {n_repeats} repeats; "
            "arm differences would be partly harness noise. Fix caching before proceeding."
        )
    if bank.signature() != bank.copy().signature():
        raise ReplayDeterminismError("bank copy is not faithful; surgery would be unsound")


def run_arms(
    bank: MemoryBank,
    replay_fn: Callable[[MemoryBank], bool],
    *,
    t_f: int,
    t_r: int,
    rng: np.random.Generator,
    arms: Sequence[str] = ARMS,
) -> dict[str, ArmOutcome]:
    """Apply every arm to the same failure state and replay each."""
    out: dict[str, ArmOutcome] = {}
    for arm in arms:
        surgered = apply_arm(arm, bank, t_f=t_f, t_r=t_r, rng=rng)
        out[arm] = ArmOutcome(
            arm=arm,
            recovered=replay_fn(surgered),
            bank_size=len(surgered),
            mean_corruption=surgered.mean_corruption(),
        )
    return out


def recovery_rates(results: Sequence[dict[str, ArmOutcome]]) -> dict[str, float]:
    if not results:
        return {}
    arms = list(results[0].keys())
    return {a: float(np.mean([r[a].recovered for r in results])) for a in arms}


def bootstrap_arm_gap(
    results: Sequence[dict[str, ArmOutcome]],
    arm_a: str,
    arm_b: str,
    *,
    n_boot: int = 10_000,
    alpha: float = 0.05,
    seed: int = 0,
) -> tuple[float, float, float]:
    """Paired bootstrap over failures for the arm_a - arm_b recovery gap."""
    a = np.array([r[arm_a].recovered for r in results], dtype=float)
    b = np.array([r[arm_b].recovered for r in results], dtype=float)
    if a.size == 0:
        return float("nan"), float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, a.size, size=(n_boot, a.size))
    boots = a[idx].mean(axis=1) - b[idx].mean(axis=1)
    lo, hi = np.quantile(boots, [alpha / 2, 1 - alpha / 2])
    return float(a.mean() - b.mean()), float(lo), float(hi)
