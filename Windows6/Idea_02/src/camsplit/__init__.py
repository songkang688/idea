"""camsplit — camera-ID leakage on smoke/fire benchmarks.

Windows6 / Idea_02. Every number this package can currently produce is
SYNTHETIC. No detector has been trained; `Idea_02/proposal.md` states
"We have not trained a detector here." There is no smoke mAP in Windows6.

Hard dependency: numpy.
"""

from .config import Config, load_config, set_seed
from .data import SyntheticCorpus, make_corpus, load_real_corpus
from .splits import (
    Split,
    camera_overlap,
    event_overlap,
    match_equal_n,
    split_camera_disjoint,
    split_event_disjoint,
    split_random,
)
from .metrics import average_precision, cluster_bootstrap_ci, far_at_recall
from .probe import camera_probe, chance_level
from .detector import TinyDetector, train_real_detector
from .pipeline import ProtocolResult, empty_frame_gap, run_protocol

PLACEHOLDER_BANNER = (
    "=" * 72
    + "\nSYNTHETIC / PLACEHOLDER OUTPUT — NOT A SCIENTIFIC RESULT.\n"
    + "No smoke dataset, no detector, no mAP. Features are generated with a\n"
    + "camera signature deliberately planted in them, so any leakage 'found'\n"
    + "below was put there by make_corpus(). These numbers test the split and\n"
    + "probe machinery, not the hypothesis. HYPOTHESIS, never ACTUAL RESULT.\n"
    + "=" * 72
)

__all__ = [
    "Config",
    "load_config",
    "set_seed",
    "SyntheticCorpus",
    "make_corpus",
    "load_real_corpus",
    "Split",
    "split_random",
    "split_event_disjoint",
    "split_camera_disjoint",
    "match_equal_n",
    "camera_overlap",
    "event_overlap",
    "average_precision",
    "far_at_recall",
    "cluster_bootstrap_ci",
    "camera_probe",
    "chance_level",
    "TinyDetector",
    "train_real_detector",
    "run_protocol",
    "empty_frame_gap",
    "ProtocolResult",
    "PLACEHOLDER_BANNER",
]
