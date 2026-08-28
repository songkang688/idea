"""conformal_nms — minimal runnable prototype for C-0306.

Measures how much split-conformal candidate-set coverage standard greedy NMS
destroys in object detection (the "blind spot"), and sketches a
coverage-preserving suppression rule (CPS) with a provable coverage bound.

Everything here runs on CPU with synthetic data. No real-dataset numbers are
produced or implied. See README.md for the EXPECTED-vs-MEASURED discipline.
"""

from .boxes import box_area, iou_matrix
from .nms import greedy_nms
from .synthetic import CrowdConfig, DetectorConfig, Scene, generate_dataset
from .conformal import (
    covering_score_per_gt,
    nonconformity_scores,
    split_conformal_qhat,
    prediction_mask,
    object_coverage,
)
from .suppression import coverage_preserving_suppression, required_calibration_iou
from .blind_spot import blind_spot_table
from . import pipelines

__all__ = [
    "box_area",
    "iou_matrix",
    "greedy_nms",
    "CrowdConfig",
    "DetectorConfig",
    "Scene",
    "generate_dataset",
    "covering_score_per_gt",
    "nonconformity_scores",
    "split_conformal_qhat",
    "prediction_mask",
    "object_coverage",
    "coverage_preserving_suppression",
    "required_calibration_iou",
    "blind_spot_table",
    "pipelines",
]
