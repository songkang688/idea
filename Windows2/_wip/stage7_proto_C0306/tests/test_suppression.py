"""Tests of the coverage-preserving suppression (CPS) sketch.

The load-bearing test is the *deterministic theorem check*: on arbitrary
scenes, every GT covered at tau_cal = tau + (1 - kappa) by the conformal
prediction set must remain covered at tau after CPS. This holds per scene,
exactly, by the Jaccard-distance triangle inequality — not just on average.
"""

import numpy as np

from conformal_nms.boxes import iou_matrix
from conformal_nms.pipelines import run_cps, run_keep_all, run_precalib_then_nms
from conformal_nms.suppression import (
    coverage_preserving_suppression,
    required_calibration_iou,
)
from conformal_nms.synthetic import CrowdConfig, DetectorConfig, generate_dataset

TAU = 0.5
KAPPA = 0.75


def _crowded_scenes(seed, n):
    rng = np.random.default_rng(seed)
    crowd = CrowdConfig(
        objects_per_scene=12.0, cluster_fraction=0.8, max_cluster_size=5,
        cluster_spread=0.3,
    )
    return generate_dataset(rng, n, crowd, DetectorConfig())


def test_required_calibration_iou():
    assert np.isclose(required_calibration_iou(0.5, 0.85), 0.65)
    try:
        required_calibration_iou(0.9, 0.5)  # tau_cal = 1.4 -> invalid
        raise AssertionError("expected ValueError")
    except ValueError:
        pass


def test_kept_is_subset_and_nonempty_per_cluster():
    scenes = _crowded_scenes(0, 20)
    for scene in scenes:
        if scene.cand_boxes.shape[0] == 0:
            continue
        mask = scene.cand_scores >= 0.3
        kept = coverage_preserving_suppression(
            scene.cand_boxes, scene.cand_scores, mask, KAPPA
        )
        assert set(kept).issubset(set(np.flatnonzero(mask)))
        if mask.any():
            assert kept.size >= 1
        # Every suppressed member must have IoU >= kappa with some kept box
        # (the property the coverage proof rests on).
        suppressed = np.setdiff1d(np.flatnonzero(mask), kept)
        if suppressed.size and kept.size:
            ious = iou_matrix(scene.cand_boxes[suppressed], scene.cand_boxes[kept])
            assert (ious.max(axis=1) >= KAPPA - 1e-12).all()


def test_theorem_coverage_transfer_exact():
    """Deterministic invariant: GT covered at tau_cal pre-CPS => covered at tau post-CPS."""
    tau_cal = required_calibration_iou(TAU, KAPPA)
    scenes = _crowded_scenes(1, 40)
    for scene in scenes:
        if scene.cand_boxes.shape[0] == 0 or scene.gt_boxes.shape[0] == 0:
            continue
        for thresh in (0.2, 0.4, 0.6):
            mask = scene.cand_scores >= thresh
            if not mask.any():
                continue
            kept = coverage_preserving_suppression(
                scene.cand_boxes, scene.cand_scores, mask, KAPPA
            )
            set_idx = np.flatnonzero(mask)
            pre = (
                iou_matrix(scene.gt_boxes, scene.cand_boxes[set_idx]) >= tau_cal
            ).any(axis=1)
            post = (
                (iou_matrix(scene.gt_boxes, scene.cand_boxes[kept]) >= TAU - 1e-9)
                .any(axis=1)
                if kept.size
                else np.zeros(scene.gt_boxes.shape[0], bool)
            )
            assert (post[pre]).all(), "CPS theorem invariant violated"


def test_redundancy_budget():
    # Three near-identical boxes; redundancy=1 keeps 1, redundancy=2 keeps 2.
    base = np.array([0.1, 0.1, 0.5, 0.5])
    boxes = np.stack([base, base + 1e-4, base + 2e-4])
    scores = np.array([0.9, 0.8, 0.7])
    mask = np.ones(3, bool)
    k1 = coverage_preserving_suppression(boxes, scores, mask, 0.85, redundancy=1)
    k2 = coverage_preserving_suppression(boxes, scores, mask, 0.85, redundancy=2)
    assert k1.size == 1 and k2.size == 2


def test_end_to_end_cps_beats_broken_pipeline():
    """On crowded synthetic data: CPS coverage ~ nominal and >= pipeline B,
    with sets smaller than keep-all."""
    scenes = _crowded_scenes(2, 240)
    calib, test = scenes[:120], scenes[120:]
    alpha = 0.1
    a = run_keep_all(calib, test, alpha, TAU)
    b = run_precalib_then_nms(calib, test, alpha, TAU, nms_iou=0.5, score_floor=0.05)
    d = run_cps(calib, test, alpha, TAU, kappa=KAPPA, redundancy=1)
    assert d.coverage >= 1 - alpha - 0.04, f"CPS coverage too low: {d.coverage}"
    assert d.coverage > b.coverage, "CPS should beat the broken pipeline"
    assert d.mean_set_size < a.mean_set_size, "CPS should shrink the keep-all set"
    assert d.duplicates_per_covered_gt < a.duplicates_per_covered_gt
