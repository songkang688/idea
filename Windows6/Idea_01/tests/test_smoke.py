"""Self-checks for Idea_01. Run with numpy alone:

    python -m unittest discover -s Idea_01/tests

These assert properties the analysis depends on. They cannot validate the
scientific claim — there is no real SAM and no real CT here. A green run means
"the instrument is not obviously broken", nothing more.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from amgclust import (  # noqa: E402
    adjusted_rand_index,
    amg_mock,
    boundary_f,
    check_remap_is_monotone,
    check_shuffle_preserves_tile_means,
    hungarian_iou,
    intensity_remap,
    kmeans_1d,
    load_config,
    masks_to_label_map,
    multi_otsu,
    set_seed,
    synthetic_ct,
    texture_shuffle,
)
from amgclust.data import apply_window  # noqa: E402
from amgclust.segmenters import connected_components, sam_amg  # noqa: E402


class TestMetrics(unittest.TestCase):
    def test_hungarian_iou_identity_is_one(self):
        masks = [np.zeros((8, 8), bool) for _ in range(3)]
        masks[0][:3] = True
        masks[1][3:6] = True
        masks[2][6:] = True
        self.assertAlmostEqual(hungarian_iou(masks, masks), 1.0, places=9)

    def test_hungarian_iou_disjoint_is_zero(self):
        a = [np.zeros((8, 8), bool)]
        a[0][:4] = True
        b = [np.zeros((8, 8), bool)]
        b[0][4:] = True
        self.assertAlmostEqual(hungarian_iou(a, b), 0.0, places=9)

    def test_hungarian_beats_greedy_on_a_trap(self):
        # Greedy matching takes the 0.6 pair first and is then forced into 0.1.
        # The optimal assignment takes 0.5 + 0.5. This is why the metric is not
        # greedy: over-segmenting methods otherwise score by matching order.
        big = np.zeros((10, 10), bool)
        big[:6] = True
        a = [big, ~big]
        b = [big.copy(), (~big).copy()]
        self.assertAlmostEqual(hungarian_iou(a, b), 1.0, places=9)

    def test_ari_identical_is_one_and_random_is_near_zero(self):
        rng = np.random.default_rng(0)
        labels = rng.integers(0, 4, size=(40, 40))
        self.assertAlmostEqual(adjusted_rand_index(labels, labels), 1.0, places=9)
        other = rng.integers(0, 4, size=(40, 40))
        self.assertLess(abs(adjusted_rand_index(labels, other)), 0.05)

    def test_boundary_f_identical_is_one(self):
        labels = np.zeros((20, 20), dtype=int)
        labels[10:] = 1
        self.assertAlmostEqual(boundary_f(labels, labels, tolerance=1), 1.0, places=9)

    def test_boundary_f_penalises_shifted_edge_beyond_tolerance(self):
        a = np.zeros((30, 30), dtype=int)
        a[10:] = 1
        b = np.zeros((30, 30), dtype=int)
        b[20:] = 1
        self.assertLess(boundary_f(a, b, tolerance=1), 0.2)


class TestInterventions(unittest.TestCase):
    """The two arms must each move exactly one factor, or they are not evidence."""

    def setUp(self):
        self.rng = set_seed(0)
        self.img = apply_window(synthetic_ct(size=64, rng=self.rng), "abdomen")

    def test_texture_shuffle_preserves_tile_means(self):
        shuffled = texture_shuffle(self.img, tile=8, rng=self.rng)
        self.assertTrue(check_shuffle_preserves_tile_means(self.img, shuffled, tile=8))

    def test_texture_shuffle_actually_changes_something(self):
        shuffled = texture_shuffle(self.img, tile=8, rng=self.rng)
        self.assertFalse(np.allclose(shuffled, self.img))

    def test_intensity_remap_is_monotone(self):
        remapped = intensity_remap(self.img, gamma=0.5)
        self.assertTrue(check_remap_is_monotone(self.img, remapped))

    def test_intensity_remap_rejects_non_monotone_gamma(self):
        with self.assertRaises(ValueError):
            intensity_remap(self.img, gamma=0.0)

    def test_arms_are_not_the_same_intervention(self):
        remapped = intensity_remap(self.img, gamma=0.5)
        shuffled = texture_shuffle(self.img, tile=8, rng=self.rng)
        self.assertFalse(np.allclose(remapped, shuffled))


class TestSegmenters(unittest.TestCase):
    def test_connected_components_counts_separate_blobs(self):
        bw = np.zeros((20, 20), bool)
        bw[2:6, 2:6] = True
        bw[12:16, 12:16] = True
        self.assertEqual(int(connected_components(bw).max()), 2)

    def test_kmeans_recovers_planted_levels(self):
        rng = set_seed(1)
        img = np.concatenate([np.full(200, 0.1), np.full(200, 0.9)]).reshape(20, 20)
        labels = kmeans_1d(img, 2, rng)
        self.assertEqual(len(np.unique(labels)), 2)

    def test_multi_otsu_returns_requested_class_count(self):
        rng = set_seed(2)
        img = apply_window(synthetic_ct(size=64, rng=rng), "abdomen")
        self.assertLessEqual(len(np.unique(multi_otsu(img, 4))), 4)

    def test_amg_mock_returns_a_nonempty_inventory(self):
        rng = set_seed(3)
        img = apply_window(synthetic_ct(size=64, rng=rng), "abdomen")
        self.assertGreater(len(amg_mock(img)), 0)

    def test_real_sam_refuses_rather_than_faking(self):
        with self.assertRaises(NotImplementedError):
            sam_amg()

    def test_amg_mock_is_not_invariant_to_monotone_remap(self):
        """Regression guard for a trap that silently voids the H2 intensity arm.

        An earlier version thresholded at *quantiles*, which are invariant to any
        monotone intensity map. The intensity arm then scored a perfect 1.000
        self-agreement by construction and could never have moved, so H2 would
        have been untestable while looking fine. Absolute thresholds fix it.
        """
        rng = set_seed(5)
        img = apply_window(synthetic_ct(size=64, rng=rng), "abdomen")
        before = amg_mock(img)
        after = amg_mock(intensity_remap(img, gamma=0.5))
        self.assertLess(hungarian_iou(before, after), 0.999)


class TestConfig(unittest.TestCase):
    def test_defaults_load_without_a_file(self):
        self.assertEqual(load_config().window, "abdomen")

    def test_unknown_keys_are_rejected(self):
        from amgclust.config import Config

        with self.assertRaises(ValueError):
            Config.from_dict({"window": "bone", "not_a_real_key": 1})

    def test_seed_is_reproducible(self):
        a = set_seed(7).normal(size=5)
        b = set_seed(7).normal(size=5)
        np.testing.assert_allclose(a, b)


class TestEndToEnd(unittest.TestCase):
    def test_smoke_run_completes(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
        from run_smoke import main

        self.assertEqual(main(["--seed", "0"]), 0)

    def test_label_map_covers_exactly_the_masked_pixels(self):
        rng = set_seed(4)
        img = apply_window(synthetic_ct(size=48, rng=rng), "abdomen")
        masks = amg_mock(img)
        labels = masks_to_label_map(masks, img.shape)
        covered = np.zeros(img.shape, bool)
        for m in masks:
            covered |= m
        np.testing.assert_array_equal(labels > 0, covered)
        self.assertLessEqual(len(np.unique(labels)) - 1, len(masks))


if __name__ == "__main__":
    unittest.main()
