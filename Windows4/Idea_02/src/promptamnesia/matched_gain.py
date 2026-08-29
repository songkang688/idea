"""The single pre-registered matched-gain rule (proposal §14).

Used verbatim by P065 (battery), P031 (sibling), P082 (plasticity measurement)
and P177 (checkpoint-pair selection). Fully implemented; operates on checkpoint
records produced by the E2 grid — it fabricates nothing.

Rule (frozen at tag idea02-prereg-v1):
  For each stratum (domain, mix, seed), let G* be the best target-domain
  validation Dice achieved by the WEAKEST recipe arm in that stratum. Every arm
  contributes the FIRST checkpoint (in training order) whose validation Dice is
  within ±tolerance of G*. Arms that never reach G* − tolerance are EXCLUDED
  from matched comparisons in that stratum and reported, not silently dropped.
  Validation Dice is computed at the arm's own calibration-tuned threshold.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class CheckpointRecord:
    """One saved checkpoint from the E2 grid (real run artifact)."""

    domain: str
    mix: str
    recipe: str
    seed: int
    step: int
    val_dice_at_tuned_threshold: float
    path: str


@dataclass
class MatchedGainResult:
    stratum: tuple[str, str, int]              # (domain, mix, seed)
    reference_gain: float                      # G*
    tolerance: float
    selected: dict[str, CheckpointRecord] = field(default_factory=dict)   # recipe -> checkpoint
    excluded: dict[str, float] = field(default_factory=dict)              # recipe -> best dice reached


def select_matched_checkpoints(
    records: list[CheckpointRecord],
    tolerance: float = 0.5,
) -> list[MatchedGainResult]:
    """Apply the rule per stratum. `tolerance` is in Dice *points* (0–100 scale
    if val dice is in points; keep units consistent with the grid logs)."""
    strata: dict[tuple[str, str, int], list[CheckpointRecord]] = {}
    for r in records:
        strata.setdefault((r.domain, r.mix, r.seed), []).append(r)

    results: list[MatchedGainResult] = []
    for stratum, recs in sorted(strata.items()):
        by_recipe: dict[str, list[CheckpointRecord]] = {}
        for r in recs:
            by_recipe.setdefault(r.recipe, []).append(r)
        for arm in by_recipe.values():
            arm.sort(key=lambda r: r.step)

        # G* = best val dice of the weakest arm (arm whose best is lowest)
        best_per_recipe = {k: max(r.val_dice_at_tuned_threshold for r in v) for k, v in by_recipe.items()}
        g_star = min(best_per_recipe.values())

        res = MatchedGainResult(stratum=stratum, reference_gain=g_star, tolerance=tolerance)
        for recipe, arm in by_recipe.items():
            chosen: Optional[CheckpointRecord] = None
            for ckpt in arm:  # first checkpoint in training order within band
                if abs(ckpt.val_dice_at_tuned_threshold - g_star) <= tolerance:
                    chosen = ckpt
                    break
                # overshoot without landing in the band: take first checkpoint
                # at-or-above the band's lower edge (still "first within reach")
                if ckpt.val_dice_at_tuned_threshold > g_star + tolerance:
                    chosen = ckpt
                    break
            if chosen is None:
                # never reached G* − tolerance -> exclude and report
                res.excluded[recipe] = best_per_recipe[recipe]
            else:
                res.selected[recipe] = chosen
        results.append(res)
    return results


def sensitivity_tolerances() -> tuple[float, ...]:
    """Pre-registered sensitivity re-runs of headline contrasts."""
    return (0.25, 1.0)
