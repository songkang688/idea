"""Self-checks for Idea_03. Run with numpy alone:

    python -m unittest discover -s Idea_03/tests

The decision-logic tests are the important ones. `classify_outcome` is the
function that turns measurements into the paper's claim, so it is tested
against planted ground truth and against the case where it must refuse.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from aligntax import (  # noqa: E402
    Outcome,
    TaxMeasurements,
    chatty_generate,
    classify_outcome,
    constrained_generate,
    fit_box_probe,
    format_xyxy,
    iou,
    likelihood_rank,
    load_config,
    make_pair,
    mean_iou,
    parse_box,
    parse_failure_rate,
    probe_error,
    rank_accuracy,
    set_seed,
    verify_checkpoint_pair,
)
from aligntax.config import TAX_MODES, Config  # noqa: E402


class TestBoxParsing(unittest.TestCase):
    """Parsing must distinguish 'talked too much' from 'could not localise'."""

    def test_parses_bare_coordinates(self):
        np.testing.assert_allclose(parse_box("10 20 30 40"), [10, 20, 30, 40])

    def test_parses_chatty_wrapper(self):
        np.testing.assert_allclose(parse_box("Sure! Here it is: [10, 20, 30, 40]"), [10, 20, 30, 40])

    def test_returns_none_on_a_genuine_format_failure(self):
        self.assertIsNone(parse_box("The object is near the top-left, around (10,20)."))

    def test_normalises_inverted_corners(self):
        np.testing.assert_allclose(parse_box("30 40 10 20"), [10, 20, 30, 40])

    def test_round_trips_through_format(self):
        box = np.array([1.5, 2.5, 30.0, 40.0])
        np.testing.assert_allclose(parse_box(format_xyxy(box)), box)

    def test_takes_the_first_box_not_the_best(self):
        """Picking the best of several would flatter a rambling checkpoint."""
        np.testing.assert_allclose(parse_box("1 2 3 4 then maybe 90 90 99 99"), [1, 2, 3, 4])


class TestIoU(unittest.TestCase):
    def test_identity_is_one(self):
        b = np.array([0.0, 0.0, 10.0, 10.0])
        self.assertAlmostEqual(iou(b, b), 1.0, places=9)

    def test_disjoint_is_zero(self):
        self.assertAlmostEqual(
            iou(np.array([0.0, 0.0, 1.0, 1.0]), np.array([5.0, 5.0, 6.0, 6.0])), 0.0, places=9
        )

    def test_half_overlap(self):
        a = np.array([0.0, 0.0, 2.0, 1.0])
        b = np.array([1.0, 0.0, 3.0, 1.0])
        self.assertAlmostEqual(iou(a, b), 1.0 / 3.0, places=9)


class TestMetrics(unittest.TestCase):
    def test_parse_failures_are_reported_separately_from_iou(self):
        """Folding failures into IoU as zeros is what hides the format tax."""
        gold = np.array([[0.0, 0.0, 10.0, 10.0], [0.0, 0.0, 10.0, 10.0]])
        outputs = ["0 0 10 10", "It is somewhere near the middle."]
        self.assertAlmostEqual(parse_failure_rate(outputs), 0.5, places=9)
        self.assertAlmostEqual(mean_iou(outputs, gold, count_failures=True), 0.5, places=9)
        self.assertAlmostEqual(mean_iou(outputs, gold, count_failures=False), 1.0, places=9)

    def test_rank_accuracy_of_all_correct_is_one(self):
        self.assertAlmostEqual(rank_accuracy([True, True, True]), 1.0, places=9)


class TestDecodingModes(unittest.TestCase):
    def setUp(self):
        self.rng = set_seed(0)
        self.box = np.array([10.0, 10.0, 40.0, 40.0])

    def test_constrained_output_always_parses(self):
        for _ in range(50):
            out = constrained_generate(self.box, 0.1, self.rng, 100.0)
            self.assertIsNotNone(parse_box(out))

    def test_chatty_output_sometimes_fails_to_parse(self):
        outs = [chatty_generate(self.box, 0.6, 0.0, self.rng, 100.0) for _ in range(200)]
        self.assertGreater(parse_failure_rate(outs), 0.0)

    def test_chattiness_alone_does_not_move_the_likelihood_rank(self):
        """Mode 3 is generation-free, so prose cannot touch it."""
        rng = set_seed(1)
        distractors = self.box + rng.normal(scale=15.0, size=(16, 4))
        clean = [likelihood_rank(self.box, distractors, 0.0, rng, 100.0) for _ in range(50)]
        self.assertTrue(all(clean))


class TestProbe(unittest.TestCase):
    def test_probe_recovers_a_linearly_encoded_box(self):
        cfg = load_config()
        rng = set_seed(2)
        pair = make_pair(cfg, rng)
        train, test = np.arange(150), np.arange(150, len(pair))
        w = fit_box_probe(pair.tokens_base, pair.boxes, train)
        self.assertLess(probe_error(w, pair.tokens_base, pair.boxes, test), 2.0)

    def test_probe_degrades_when_representation_is_corrupted(self):
        cfg = load_config()
        cfg.tax_mode = "representation"
        rng = set_seed(3)
        pair = make_pair(cfg, rng)
        train, test = np.arange(150), np.arange(150, len(pair))
        base_w = fit_box_probe(pair.tokens_base, pair.boxes, train)
        chat_w = fit_box_probe(pair.tokens_chat, pair.boxes, train)
        self.assertGreater(
            probe_error(chat_w, pair.tokens_chat, pair.boxes, test),
            probe_error(base_w, pair.tokens_base, pair.boxes, test),
        )


class TestDecisionLogic(unittest.TestCase):
    """`classify_outcome` is the function that turns numbers into the claim."""

    def test_refuses_without_the_likelihood_mode(self):
        m = TaxMeasurements(freeform_gap=0.4, constrained_gap=0.3, likelihood_gap=None, probe_gap=0.0)
        with self.assertRaises(ValueError):
            classify_outcome(m)

    def test_gap_dying_under_likelihood_is_a_format_artifact(self):
        m = TaxMeasurements(freeform_gap=0.4, constrained_gap=0.3, likelihood_gap=0.0, probe_gap=0.0)
        self.assertEqual(classify_outcome(m), Outcome.FORMAT)

    def test_likelihood_gap_with_intact_probe_is_a_policy_tax(self):
        m = TaxMeasurements(freeform_gap=0.4, constrained_gap=0.3, likelihood_gap=0.2, probe_gap=0.0)
        self.assertEqual(classify_outcome(m), Outcome.POLICY)

    def test_probe_dropping_too_is_a_representation_tax(self):
        m = TaxMeasurements(freeform_gap=0.4, constrained_gap=0.3, likelihood_gap=0.2, probe_gap=0.1)
        self.assertEqual(classify_outcome(m), Outcome.REPRESENTATION)

    def test_no_gaps_anywhere_is_no_tax(self):
        m = TaxMeasurements(freeform_gap=0.0, constrained_gap=0.0, likelihood_gap=0.0, probe_gap=0.0)
        self.assertEqual(classify_outcome(m), Outcome.NO_TAX)


class TestRoundTrip(unittest.TestCase):
    """Every planted degradation must be recoverable from the measurements alone."""

    def test_each_planted_mode_is_recovered(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
        from run_smoke import _measure

        for mode in TAX_MODES:
            with self.subTest(mode=mode):
                cfg = load_config()
                cfg.tax_mode = mode
                rng = set_seed(cfg.seed)
                measured, _ = _measure(make_pair(cfg, rng), cfg, rng)
                self.assertEqual(classify_outcome(measured, cfg.gap_tolerance).value, mode)


class TestConfigAndRefusals(unittest.TestCase):
    def test_unknown_keys_are_rejected(self):
        with self.assertRaises(ValueError):
            Config.from_dict({"decode": "constrained_xyxy", "not_a_real_key": 1})

    def test_invalid_tax_mode_is_rejected(self):
        with self.assertRaises(ValueError):
            Config(tax_mode="wishful")

    def test_seed_is_reproducible(self):
        np.testing.assert_allclose(set_seed(11).normal(size=4), set_seed(11).normal(size=4))

    def test_checkpoint_verification_refuses_rather_than_faking(self):
        with self.assertRaises(NotImplementedError):
            verify_checkpoint_pair()


class TestEndToEnd(unittest.TestCase):
    def test_smoke_run_completes(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
        from run_smoke import main

        self.assertEqual(main(["--seed", "0"]), 0)


if __name__ == "__main__":
    unittest.main()
