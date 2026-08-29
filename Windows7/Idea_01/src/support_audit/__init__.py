"""SupportAudit -- wrong-support counterfactual audit of few-shot segmentation.

Windows7 / Idea_01 (internal ID B-0121). See ../../proposal.md.

The package is deliberately inference-only and model-agnostic: it measures how
much of a few-shot segmenter's reported accuracy survives when the support image
is replaced by one of a class verified absent from the query.
"""

from .counterfactual import CounterfactualList, WrongSupport, sample_wrong_supports
from .episodes import Episode, Instance, STRATA, stratum_counts
from .floors import CentralLargestMaskFloor, SaliencyThresholdFloor
from .metrics import EpisodeMeasurement, iou, support_sensitivity_score
from .protocol import AuditConfig, AuditReport, run_audit
from .stats import evaluate_killer, kendall_tau, positions_changed, summarise

__all__ = [
    "AuditConfig",
    "AuditReport",
    "CentralLargestMaskFloor",
    "CounterfactualList",
    "Episode",
    "EpisodeMeasurement",
    "Instance",
    "STRATA",
    "SaliencyThresholdFloor",
    "WrongSupport",
    "evaluate_killer",
    "iou",
    "kendall_tau",
    "positions_changed",
    "run_audit",
    "sample_wrong_supports",
    "stratum_counts",
    "support_sensitivity_score",
]

__version__ = "0.1.0"
