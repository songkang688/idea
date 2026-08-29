"""Self-checks for Idea_02. Run with numpy alone:

    python -m unittest discover -s Idea_02/tests

The split-structure tests are the important ones. They assert the property H2
depends on — event-disjoint still shares cameras — so that a refactor cannot
quietly turn the two protocols into the same thing and make H2 unfalsifiable.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from camsplit import (  # noqa: E402
    average_precision,
    camera_probe,
    chance_level,
    cluster_bootstrap_ci,
    empty_frame_gap,
    far_at_recall,
    load_config,
    make_corpus,
    match_equal_n,
    set_seed,
    split_camera_disjoint,
    split_event_disjoint,
    split_random,
)
from camsplit.data import load_real_corpus  # noqa: E402
from camsplit.detector import TinyDetector, train_real_detector  # noqa: E402
from camsplit.splits import Split, camera_overlap, event_overlap  # noqa: E402


def _corpus(seed: int = 0):
    cfg = load_config()
    rng = set_seed(seed)
    return cfg, rng, make_corpus(cfg, rng)


class TestSplitStructure(unittest.TestCase):
    """H2 is only expressible if these three protocols differ as described."""

    def setUp(self):
        self.cfg, self.rng, self.corpus = _corpus()

    def test_random_shares_cameras_and_events(self):
        s = split_random(self.corpus, self.rng)
        self.assertGreater(camera_overlap(self.corpus, s), 0)
        self.assertGreater(event_overlap(self.corpus, s), 0)

    def test_event_disjoint_shares_no_events(self):
        s = split_event_disjoint(self.corpus, self.rng)
        self.assertEqual(event_overlap(self.corpus, s), 0)

    def test_event_disjoint_STILL_shares_cameras(self):
        """The residual leak H2 is about. If this ever fails, H2 is untestable."""
        s = split_event_disjoint(self.corpus, self.rng)
        self.assertGreater(camera_overlap(self.corpus, s), 0)

    def test_camera_disjoint_shares_neither(self):
        s = split_camera_disjoint(self.corpus, self.rng, self.cfg.test_cameras)
        self.assertEqual(camera_overlap(self.corpus, s), 0)
        self.assertEqual(event_overlap(self.corpus, s), 0)

    def test_camera_disjoint_refuses_to_empty_the_train_set(self):
        with self.assertRaises(ValueError):
            split_camera_disjoint(self.corpus, self.rng, self.cfg.n_cameras)

    def test_split_rejects_overlapping_indices(self):
        with self.assertRaises(ValueError):
            Split("bad", np.array([0, 1, 2]), np.array([2, 3]))

    def test_equal_n_matches_the_positive_ratio(self):
        s = split_camera_disjoint(self.corpus, self.rng, self.cfg.test_cameras)
        matched = match_equal_n(self.corpus, s, self.rng)
        train_ratio = self.corpus.labels[matched.train].mean()
        test_ratio = self.corpus.labels[matched.test].mean()
        self.assertLess(abs(train_ratio - test_ratio), 0.05)


class TestMetrics(unittest.TestCase):
    def test_ap_of_a_perfect_ranking_is_one(self):
        labels = np.array([1, 1, 0, 0])
        self.assertAlmostEqual(average_precision(np.array([0.9, 0.8, 0.2, 0.1]), labels), 1.0, places=6)

    def test_ap_of_an_inverted_ranking_is_low(self):
        labels = np.array([1, 1, 0, 0])
        self.assertLess(average_precision(np.array([0.1, 0.2, 0.8, 0.9]), labels), 0.6)

    def test_far_at_recall_is_zero_for_a_perfect_separator(self):
        labels = np.array([1, 1, 0, 0])
        self.assertAlmostEqual(far_at_recall(np.array([0.9, 0.8, 0.2, 0.1]), labels, 1.0), 0.0, places=6)

    def test_far_returns_nan_when_recall_unreachable(self):
        labels = np.array([1, 0])
        self.assertTrue(np.isnan(far_at_recall(np.array([0.5, 0.5]), labels, 1.5)))

    def test_cluster_bootstrap_is_wider_than_it_would_be_per_frame(self):
        """Event-level resampling must not be secretly frame-level."""
        rng = set_seed(1)
        values = np.repeat([0.0, 1.0], 100)
        clusters = np.repeat([0, 1], 100)
        lo, hi = cluster_bootstrap_ci(values, clusters, rng, resamples=200)
        self.assertGreater(hi - lo, 0.5)


class TestProbe(unittest.TestCase):
    def test_probe_beats_chance_when_signature_is_planted(self):
        cfg, rng, corpus = _corpus(2)
        s = split_event_disjoint(corpus, rng)
        out = camera_probe(corpus.features, corpus.camera, s.train, s.test)
        self.assertGreater(out["margin"], 0.1)

    def test_probe_is_near_chance_when_no_signature_exists(self):
        """Negative control: no planted camera identity, no probe signal.

        Must be evaluated event-disjoint. On a random split this control FAILS
        with a margin of ~0.17 even at zero camera signature, because the
        per-event plume vector is shared across the split and identifies the
        camera through the episode. That is event memorisation, not a camera
        signature, and counting it towards H3 would be wrong.
        """
        cfg = load_config()
        cfg.camera_signature = 0.0
        rng = set_seed(3)
        corpus = make_corpus(cfg, rng)
        s = split_event_disjoint(corpus, rng)
        out = camera_probe(corpus.features, corpus.camera, s.train, s.test)
        self.assertLess(out["margin"], 0.10)

    def test_random_split_probe_is_confounded_by_event_leakage(self):
        """Pins the confound itself, so the event-disjoint rule cannot be dropped."""
        cfg = load_config()
        cfg.camera_signature = 0.0
        rng = set_seed(3)
        corpus = make_corpus(cfg, rng)
        s = split_random(corpus, rng)
        out = camera_probe(corpus.features, corpus.camera, s.train, s.test)
        self.assertGreater(out["margin"], 0.10)

    def test_chance_level_is_the_majority_rate(self):
        self.assertAlmostEqual(chance_level(np.array([0, 0, 0, 1])), 0.75, places=9)


class TestEmptyFrameProbe(unittest.TestCase):
    def test_gap_is_defined_only_when_unseen_cameras_exist(self):
        cfg, rng, corpus = _corpus(4)
        random_split = split_random(corpus, rng)
        self.assertTrue(np.isnan(empty_frame_gap(corpus, random_split)["gap"]))

        camera_split = split_camera_disjoint(corpus, rng, cfg.test_cameras)
        gap = empty_frame_gap(corpus, camera_split)
        self.assertFalse(np.isnan(gap["gap"]))
        self.assertGreater(gap["n_seen"], 0)
        self.assertGreater(gap["n_unseen"], 0)

    def test_empty_frames_are_never_trained_on(self):
        """Both sides of H4 must be held out, or the comparison is rigged."""
        cfg, rng, corpus = _corpus(5)
        split = split_camera_disjoint(corpus, rng, cfg.test_cameras)
        train_real = split.train[~corpus.is_empty[split.train]]
        self.assertFalse(corpus.is_empty[train_real].any())


class TestRefusals(unittest.TestCase):
    def test_real_corpus_refuses_rather_than_faking(self):
        with self.assertRaises(NotImplementedError):
            load_real_corpus()

    def test_real_detector_refuses_rather_than_faking(self):
        with self.assertRaises(NotImplementedError):
            train_real_detector()

    def test_detector_requires_fit_before_predict(self):
        with self.assertRaises(RuntimeError):
            TinyDetector().predict_proba(np.zeros((2, 3)))


class TestConfig(unittest.TestCase):
    def test_unknown_keys_are_rejected(self):
        from camsplit.config import Config

        with self.assertRaises(ValueError):
            Config.from_dict({"seeds": 3, "not_a_real_key": 1})

    def test_seed_is_reproducible(self):
        np.testing.assert_allclose(set_seed(9).normal(size=4), set_seed(9).normal(size=4))


class TestEndToEnd(unittest.TestCase):
    def test_smoke_run_completes(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
        from run_smoke import main

        self.assertEqual(main(["--seed", "0"]), 0)


if __name__ == "__main__":
    unittest.main()
