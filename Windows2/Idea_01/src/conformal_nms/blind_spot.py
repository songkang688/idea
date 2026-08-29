"""Blind-spot analyzer — the H1 killer-experiment measurement (exp_05).

For each GT object and each NMS operating point, classify:

  * detected pre-NMS : >= 1 candidate covers the GT at IoU >= tau in the full
    candidate cache (its negation is a plain detector miss — NMS-independent);
  * blind            : detected pre-NMS, but *zero* covering candidates
    survive NMS. For such objects no score threshold, calibration, or
    downstream conformal layer can restore coverage — the information is gone.

Reported per (nms_iou) operating point, pooled over scenes:

  miss_rate            = P(not detected pre-NMS)
  blind_rate           = P(detected pre-NMS and blind)         [unconditional]
  blind_given_detected = blind_rate / P(detected pre-NMS)
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .boxes import iou_matrix
from .nms import greedy_nms
from .synthetic import Scene


@dataclass
class BlindSpotRow:
    nms_iou: float
    n_gt: int
    miss_rate: float
    blind_rate: float
    blind_given_detected: float


def blind_spot_flags(
    scene: Scene, tau: float, nms_iou: float, score_floor: float
) -> tuple[np.ndarray, np.ndarray]:
    """Per-GT (detected_pre, blind) boolean arrays for one scene."""
    n_gt = scene.gt_boxes.shape[0]
    if n_gt == 0:
        z = np.zeros(0, dtype=bool)
        return z, z
    if scene.cand_boxes.shape[0] == 0:
        return np.zeros(n_gt, dtype=bool), np.zeros(n_gt, dtype=bool)

    ious = iou_matrix(scene.gt_boxes, scene.cand_boxes)  # (G, C)
    covers = ious >= tau
    detected_pre = covers.any(axis=1)

    keep = greedy_nms(scene.cand_boxes, scene.cand_scores, nms_iou, score_floor)
    covered_post = (
        covers[:, keep].any(axis=1) if keep.size else np.zeros(n_gt, dtype=bool)
    )
    blind = detected_pre & ~covered_post
    return detected_pre, blind


def blind_spot_table(
    scenes: list[Scene],
    tau: float,
    nms_iou_grid: list[float],
    score_floor: float,
) -> list[BlindSpotRow]:
    rows = []
    for nms_iou in nms_iou_grid:
        det_all: list[np.ndarray] = []
        blind_all: list[np.ndarray] = []
        for scene in scenes:
            d, b = blind_spot_flags(scene, tau, nms_iou, score_floor)
            det_all.append(d)
            blind_all.append(b)
        detected = np.concatenate(det_all) if det_all else np.zeros(0, dtype=bool)
        blind = np.concatenate(blind_all) if blind_all else np.zeros(0, dtype=bool)
        n_gt = detected.size
        n_det = int(detected.sum())
        rows.append(
            BlindSpotRow(
                nms_iou=nms_iou,
                n_gt=n_gt,
                miss_rate=1.0 - n_det / n_gt if n_gt else 0.0,
                blind_rate=float(blind.mean()) if n_gt else 0.0,
                blind_given_detected=float(blind.sum()) / n_det if n_det else 0.0,
            )
        )
    return rows
