import numpy as np
import pytest

from conformal_nms.boxes import box_area, iou_matrix


def test_identical_boxes_have_iou_one():
    b = np.array([[0.1, 0.1, 0.5, 0.5]])
    assert iou_matrix(b, b)[0, 0] == pytest.approx(1.0)


def test_disjoint_boxes_have_iou_zero():
    a = np.array([[0.0, 0.0, 0.2, 0.2]])
    b = np.array([[0.5, 0.5, 0.9, 0.9]])
    assert iou_matrix(a, b)[0, 0] == 0.0


def test_known_overlap_value():
    # a = [0,0,2,2] area 4; b = [1,0,3,2] area 4; inter = 1x2 = 2; union = 6.
    a = np.array([[0.0, 0.0, 2.0, 2.0]])
    b = np.array([[1.0, 0.0, 3.0, 2.0]])
    assert iou_matrix(a, b)[0, 0] == pytest.approx(2.0 / 6.0)


def test_symmetry_and_shape():
    rng = np.random.default_rng(0)
    a = np.sort(rng.uniform(0, 1, size=(7, 2, 2)), axis=1).reshape(7, 4)
    a = a[:, [0, 2, 1, 3]]  # xyxy
    b = np.sort(rng.uniform(0, 1, size=(5, 2, 2)), axis=1).reshape(5, 4)
    b = b[:, [0, 2, 1, 3]]
    m = iou_matrix(a, b)
    assert m.shape == (7, 5)
    np.testing.assert_allclose(m, iou_matrix(b, a).T)
    assert (m >= 0).all() and (m <= 1 + 1e-12).all()


def test_degenerate_box_area_and_iou():
    a = np.array([[0.5, 0.5, 0.5, 0.9]])  # zero width
    assert box_area(a)[0] == 0.0
    b = np.array([[0.0, 0.0, 1.0, 1.0]])
    assert iou_matrix(a, b)[0, 0] == 0.0


def test_empty_inputs():
    a = np.zeros((0, 4))
    b = np.array([[0.0, 0.0, 1.0, 1.0]])
    assert iou_matrix(a, b).shape == (0, 1)
    assert iou_matrix(b, a).shape == (1, 0)
