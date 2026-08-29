"""RehearsalGrid -- the content-free rehearsal experiment (C-0090).

Everything here runs on CPU with numpy alone. The point is that the parts of this
project that can be *wrong* -- the content-destruction transforms, the token-budget
accounting, the denominator-adequacy gate and the pre-registered decision rule --
are all testable before a single A100-hour is spent.

The 15 fine-tuning runs are the expensive part. The decision rule that reads them
is the part that has to be right first.
"""

from .arms import ARMS, Arm, destroy
from .sampler import InterleavedSampler, TokenBudget
from .matching import global_norm_scale, per_layer_scale
from .power import DenominatorGate, StratumScores, power_check
from .decision import Decision, evaluate

__all__ = [
    "ARMS",
    "Arm",
    "destroy",
    "InterleavedSampler",
    "TokenBudget",
    "global_norm_scale",
    "per_layer_scale",
    "DenominatorGate",
    "StratumScores",
    "power_check",
    "Decision",
    "evaluate",
]
