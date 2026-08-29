import numpy as np

from conformal_nms.boxes import iou_matrix
from conformal_nms.nms import greedy_nms


def reference_nms(boxes, scores, iou_thresh, score_floor=0.0):
    """Brute-force reference implementation (list-based, obviously correct)."""
    idx = [i for i in range(len(scores)) if scores[i] >= score_floor]
    idx.sort(key=lambda i: -scores[i])
    kept = []
    for i in idx:
        ok = True
        for j in kept:
            if iou_matrix(boxes[i : i + 1], boxes[j : j + 1])[0, 0] >= iou_thresh:
                ok = False
                break
        if ok:
            kept.append(i)
    return np.asarray(kept, dtype=np.int64)


def _random_boxes(rng, n):
    cxy = rng.uniform(0.1, 0.9, size=(n, 2))
    wh = rng.uniform(0.05, 0.3, size=(n, 2))
    return np.concatenate([cxy - wh / 2, cxy + wh / 2], axis=1)


def test_matches_reference_on_random_data():
    rng = np.random.default_rng(42)
    for trial in range(10):
        boxes = _random_boxes(rng, 120)
        scores = rng.uniform(0, 1, size=120)
        for thr in (0.3, 0.5, 0.7):
            got = greedy_nms(boxes, scores, thr)
            want = reference_nms(boxes, scores, thr)
            np.testing.assert_array_equal(got, want)


def test_kept_sorted_by_score_and_mutually_below_threshold():
    rng = np.random.default_rng(1)
    boxes = _random_boxes(rng, 80)
    scores = rng.uniform(0, 1, size=80)
    keep = greedy_nms(boxes, scores, 0.5)
    s = scores[keep]
    assert (s[:-1] >= s[1:]).all()
    ious = iou_matrix(boxes[keep], boxes[keep])
    np.fill_diagonal(ious, 0.0)
    assert (ious < 0.5).all()


def test_score_floor_filters():
    boxes = np.array([[0.0, 0.0, 0.2, 0.2], [0.5, 0.5, 0.7, 0.7]])
    scores = np.array([0.9, 0.01])
    keep = greedy_nms(boxes, scores, 0.5, score_floor=0.05)
    np.testing.assert_array_equal(keep, [0])


def test_single_and_empty():
    assert greedy_nms(np.zeros((0, 4)), np.zeros(0), 0.5).size == 0
    keep = greedy_nms(np.array([[0, 0, 1, 1.0]]), np.array([0.5]), 0.5)
    np.testing.assert_array_equal(keep, [0])
