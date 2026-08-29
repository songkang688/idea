"""aligntax — stage-isolated localization tax in aligned VLMs.

Windows6 / Idea_03. Every number this package can currently produce is
SYNTHETIC. `Windows6/README.md` records "no VLM eval". No checkpoint has been
loaded and no VLM has been run.

GATE-B is open: no base/chat checkpoint pair has been verified to share a
vision encoder and coordinate tokenization, which `experiments.md` calls a
"Hard gate".

Hard dependency: numpy.
"""

from .config import Config, load_config, set_seed
from .boxes import format_xyxy, iou, parse_box
from .data import SyntheticPair, make_pair, verify_checkpoint_pair
from .decoding import chatty_generate, constrained_generate, likelihood_rank
from .probe import fit_box_probe, probe_error
from .metrics import acc_at_iou, mean_iou, parse_failure_rate, rank_accuracy
from .pipeline import Outcome, TaxMeasurements, classify_outcome

PLACEHOLDER_BANNER = (
    "=" * 72
    + "\nSYNTHETIC / PLACEHOLDER OUTPUT — NOT A SCIENTIFIC RESULT.\n"
    + "No VLM, no checkpoint, no RefCOCO. The 'base' and 'chat' models below\n"
    + "are simulators whose degradation mode was CHOSEN by the config, so any\n"
    + "tax 'found' is the tax we planted. This exercises the O1/O2/O3 decision\n"
    + "logic, not the hypothesis. HYPOTHESIS, never ACTUAL RESULT.\n"
    + "=" * 72
)

__all__ = [
    "Config",
    "load_config",
    "set_seed",
    "parse_box",
    "iou",
    "format_xyxy",
    "SyntheticPair",
    "make_pair",
    "verify_checkpoint_pair",
    "chatty_generate",
    "constrained_generate",
    "likelihood_rank",
    "fit_box_probe",
    "probe_error",
    "mean_iou",
    "acc_at_iou",
    "parse_failure_rate",
    "rank_accuracy",
    "Outcome",
    "TaxMeasurements",
    "classify_outcome",
    "PLACEHOLDER_BANNER",
]
