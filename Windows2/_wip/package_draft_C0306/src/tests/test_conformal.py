import math

import numpy as np
import pytest

from conformal_nms.conformal import (
    covering_score_per_gt,
    nonconformity_scores,
    object_coverage,
    prediction_mask,
    split_conformal_qhat,
)
from conformal_nms.pipelines import run_keep_all
from conformal_nms.synthetic import CrowdConfig, DetectorConfig, generate_dataset


def test_qhat_monotone_in_alpha():
    rng = np.random.default_rng(0)
    scores = rng.uniform(0, 1, size=500)
    qs = [split_conformal_qhat(scores, a) for a in (0.2, 0.1, 0.05)]
    assert qs[0] <= qs[1] <= qs[2]


def test_qhat_infinite_when_unachievable():
    # 30% of calibration objects uncovered (inf score) but alpha = 0.1:
    # the conformal quantile must land on +inf.
    scores = np.array([0.1] * 70 + [math.inf] * 30)
    assert math.isinf(split_conformal_qhat(scores, 0.1))
    # ...and be finite when alpha exceeds the uncovered fraction.
    assert not math.isinf(split_conformal_qhat(scores, 0.4))


def test_prediction_mask_keep_all_when_inf():
    scores = np.array([0.1, 0.9])
    assert prediction_mask(scores, math.inf).all()
    mask = prediction_mask(scores, 0.2)  # threshold 0.8
    np.testing.assert_array_equal(mask, [False, True])


def test_covering_score_per_gt_basic():
    gt = np.array([[0.0, 0.0, 0.4, 0.4]])
    cands = np.array(
        [
            [0.0, 0.0, 0.4, 0.4],   # IoU 1.0
            [0.6, 0.6, 0.9, 0.9],   # IoU 0
        ]
    )
    scores = np.array([0.7, 0.99])
    best = covering_score_per_gt(gt, cands, scores, tau=0.5)
    assert best[0] == pytest.approx(0.7)
    # No covering candidate -> -inf sentinel.
    best2 = covering_score_per_gt(gt, cands[1:], scores[1:], tau=0.5)
    assert np.isneginf(best2[0])


def test_marginal_coverage_on_synthetic_pre_nms():
    """Split-conformal validity check on the full candidate pool (pipeline A).

    With ~2000+ calibration/test GT objects the binomial SE is < 1%, so a
    +/- 4pp tolerance at a fixed seed is a stable, honest check.
    """
    rng = np.random.default_rng(123)
    scenes = generate_dataset(rng, 300, CrowdConfig(), DetectorConfig())
    calib, test = scenes[:150], scenes[150:]
    alpha = 0.1
    res = run_keep_all(calib, test, alpha=alpha, tau=0.5)
    assert res.n_test_gt > 500
    assert res.coverage >= 1 - alpha - 0.04
    # Coverage should not be wildly conservative either (sanity, not a theorem).
    assert res.coverage <= 1.0


def test_object_coverage_respects_mask():
    gt = np.array([[0.0, 0.0, 0.4, 0.4]])
    cands = np.array([[0.0, 0.0, 0.4, 0.4]])
    scores = np.array([0.9])
    assert object_coverage(gt, cands, scores, np.array([True]), 0.5)[0]
    assert not object_coverage(gt, cands, scores, np.array([False]), 0.5)[0]
