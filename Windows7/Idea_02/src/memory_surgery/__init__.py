"""MemorySurgeon -- causal memory surgery as a decomposition instrument for SAM2.

Windows7 / Idea_02 (internal ID A-0017). See ../../proposal.md.

The package implements the five surgical arms, the failure-harvesting protocol,
the replay-determinism gate, and the difficulty-partialled validity statistics.
The two pieces that Stage 6 forced into the design -- the temporal-encoding sham
arm and the min-over-frozen-comparators partial correlation -- live in
`surgeon.py` and `validity.py` respectively.
"""

from .bank import MemoryBank, MemoryEntry, build_bank
from .harvest import FailureEvent, harvest, recovered, reversible_fraction
from .replay import (
    ReplayDeterminismError,
    bootstrap_arm_gap,
    check_replay_determinism,
    recovery_rates,
    run_arms,
)
from .simulate import SimConfig, SimulatedTracker
from .surgeon import ARMS, apply_arm
from .validity import ValidityVerdict, evaluate_validity, partial_correlation

__all__ = [
    "ARMS",
    "FailureEvent",
    "MemoryBank",
    "MemoryEntry",
    "ReplayDeterminismError",
    "SimConfig",
    "SimulatedTracker",
    "ValidityVerdict",
    "apply_arm",
    "bootstrap_arm_gap",
    "build_bank",
    "check_replay_determinism",
    "evaluate_validity",
    "harvest",
    "partial_correlation",
    "recovered",
    "recovery_rates",
    "reversible_fraction",
    "run_arms",
]

__version__ = "0.1.0"
