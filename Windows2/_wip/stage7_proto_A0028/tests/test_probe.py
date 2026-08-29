import numpy as np

from a0028.metrics import spearman_rho, wilson_ci
from a0028.probe import OUTCOMES, run_cell, stable_seed
from a0028.tracker import (
    MemoryBankTracker,
    appearance_matcher_tracker,
    location_prior_tracker,
)
from a0028.world import WorldParams

W = WorldParams(n_prefix=4, n_post=4)


def factory(lam, **kw):
    def f(rng):
        return MemoryBankTracker(lambda_loc=lam, rng=rng, **kw)

    return f


def test_stable_seed_reproducible():
    assert stable_seed(1, "swap", 8, 2, 0.5, 0) == stable_seed(1, "swap", 8, 2, 0.5, 0)
    assert stable_seed(1, "swap", 8, 2, 0.5, 0) != stable_seed(1, "swap", 8, 2, 0.5, 1)


def test_rates_sum_to_one():
    cell = run_cell("swap", 16, 2, 0.5, 40, factory(0.5), W, base_seed=7)
    total = sum(cell["rates"][o]["k"] for o in OUTCOMES)
    assert total == cell["n_trials"] == 40


def test_dummies_bracket_the_swap_behavior():
    loc = run_cell(
        "swap", 32, 2, 0.5, 60, lambda rng: location_prior_tracker(rng), W, 11
    )
    app = run_cell(
        "swap", 32, 2, 0.5, 60, lambda rng: appearance_matcher_tracker(rng), W, 11
    )
    assert loc["rates"]["follow_place"]["rate"] > 0.95
    assert app["rates"]["follow_object"]["rate"] > 0.95


def test_follow_place_increases_from_easy_to_hard_cell():
    easy = run_cell("swap", 4, 1, 0.2, 200, factory(0.5), W, 13)
    hard = run_cell("swap", 64, 16, 0.9, 200, factory(0.5), W, 13)
    assert (
        hard["rates"]["follow_place"]["rate"]
        > easy["rates"]["follow_place"]["rate"] + 0.2
    )


def test_placebo_control_not_disruptive():
    cell = run_cell("placebo", 0.0, 4, 0.8, 100, factory(0.5), W, 17)
    assert cell["rates"]["follow_object"]["rate"] > 0.95


def test_memory_pollution_persists_wrong_identity():
    # location-leaning tracker at a hard swap cell: wrong picks happen and,
    # with memory update on, the wrong identity persists to the final frame
    cell = run_cell("swap", 64, 8, 0.9, 150, factory(0.8), W, 19)
    assert cell["wrong_at_manipulation"]["rate"] > 0.5
    persist = cell["wrong_persisted_given_wrong"]
    assert persist is not None and persist["rate"] > 0.8
    # representation-level: template rebinds toward the distractor
    assert cell["template_affinity_gap"]["mean"] > 0.0


def test_jump_condition_scores_phantom_as_place():
    cell = run_cell("jump", 64, 8, 0.5, 100, factory(0.9), W, 23)
    # a location-dominant tracker should mostly land on the background phantom
    assert cell["rates"]["follow_place"]["rate"] > 0.5


def test_wilson_ci_and_spearman():
    lo, hi = wilson_ci(50, 100)
    assert lo < 0.5 < hi
    assert wilson_ci(0, 0) == (0.0, 1.0)
    assert abs(spearman_rho([1, 2, 3, 4], [10, 20, 30, 40]) - 1.0) < 1e-9
    assert abs(spearman_rho([1, 2, 3, 4], [40, 30, 20, 10]) + 1.0) < 1e-9
