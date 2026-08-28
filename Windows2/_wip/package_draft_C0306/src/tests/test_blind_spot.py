import numpy as np

from conformal_nms.blind_spot import blind_spot_flags, blind_spot_table
from conformal_nms.synthetic import Scene


def _crafted_scene():
    """Two overlapping GTs; the only candidate covering g2 is suppressed by the
    higher-scoring candidate of g1 at aggressive NMS (iou 0.3).

    Geometry (unit square):
      g1 = [0.00, 0.0, 0.40, 0.4]
      g2 = [0.25, 0.0, 0.65, 0.4]        IoU(g1, g2) ~ 0.231
      c1 = [0.05, 0.0, 0.45, 0.4]  s=0.9 IoU(c1,g1)=0.778, IoU(c1,g2)=0.333
      c2 = [0.25, 0.0, 0.65, 0.4]  s=0.8 IoU(c2,g2)=1.0,   IoU(c1,c2)=0.333
    At nms_iou = 0.3: c1 kept, c2 suppressed -> g2 blind (covered pre, not post).
    At nms_iou = 0.5: both survive -> no blind spot.
    """
    gt = np.array([[0.00, 0.0, 0.40, 0.4], [0.25, 0.0, 0.65, 0.4]])
    cands = np.array([[0.05, 0.0, 0.45, 0.4], [0.25, 0.0, 0.65, 0.4]])
    scores = np.array([0.9, 0.8])
    return Scene(gt_boxes=gt, cand_boxes=cands, cand_scores=scores)


def test_crafted_blind_spot_at_aggressive_nms():
    scene = _crafted_scene()
    detected, blind = blind_spot_flags(scene, tau=0.5, nms_iou=0.3, score_floor=0.0)
    np.testing.assert_array_equal(detected, [True, True])
    np.testing.assert_array_equal(blind, [False, True])


def test_no_blind_spot_at_lenient_nms():
    scene = _crafted_scene()
    detected, blind = blind_spot_flags(scene, tau=0.5, nms_iou=0.5, score_floor=0.0)
    np.testing.assert_array_equal(detected, [True, True])
    assert not blind.any()


def test_table_rates_on_crafted_scene():
    rows = blind_spot_table([_crafted_scene()], 0.5, [0.3, 0.5], 0.0)
    by_iou = {r.nms_iou: r for r in rows}
    assert by_iou[0.3].blind_rate == 0.5
    assert by_iou[0.3].blind_given_detected == 0.5
    assert by_iou[0.3].miss_rate == 0.0
    assert by_iou[0.5].blind_rate == 0.0


def test_miss_is_not_blind():
    # A GT with no covering candidate at all is a miss, never a blind spot.
    gt = np.array([[0.0, 0.0, 0.2, 0.2]])
    cands = np.array([[0.7, 0.7, 0.9, 0.9]])
    scene = Scene(gt, cands, np.array([0.9]))
    detected, blind = blind_spot_flags(scene, 0.5, 0.5, 0.0)
    assert not detected[0] and not blind[0]
    row = blind_spot_table([scene], 0.5, [0.5], 0.0)[0]
    assert row.miss_rate == 1.0 and row.blind_rate == 0.0
