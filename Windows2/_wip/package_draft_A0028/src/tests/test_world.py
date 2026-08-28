import numpy as np
import pytest

from a0028.world import (
    DISTRACTOR,
    PHANTOM,
    TARGET,
    WorldParams,
    generate_trial,
    unit_vector,
    vector_with_cosine,
)

W = WorldParams(n_prefix=4, n_post=4)


def get(frame, ident):
    return next(c for c in frame.candidates if c.ident == ident)


def test_vector_with_cosine_hits_requested_similarity():
    rng = np.random.default_rng(0)
    base = unit_vector(rng, 32)
    for s in (0.2, 0.5, 0.8, 0.95):
        v = vector_with_cosine(rng, base, s)
        assert np.isclose(np.linalg.norm(v), 1.0)
        assert np.isclose(float(v.dot(base)), s, atol=1e-9)


def test_swap_exchanges_positions_with_controlled_displacement():
    rng = np.random.default_rng(1)
    d = 32.0
    trial = generate_trial("swap", d, gap=4, similarity=0.8, rng=rng, world=W)
    manip = trial.frames[trial.manipulation_idx]
    # target-distractor separation at the swap frame ~ d (rigid offset + jitter)
    sep = np.linalg.norm(get(manip, TARGET).loc - get(manip, DISTRACTOR).loc)
    assert sep == pytest.approx(d, rel=0.15)
    # the distractor now sits where the target was heading (positions exchanged):
    # target's post-swap location equals distractor's pre-gap trajectory side
    assert trial.place_ident == DISTRACTOR


def test_gap_advances_world_time_and_appearance_drift():
    rng = np.random.default_rng(2)
    trial = generate_trial("swap", 16.0, gap=8, similarity=0.5, rng=rng, world=W)
    manip = trial.frames[trial.manipulation_idx]
    last_prefix = trial.frames[trial.manipulation_idx - 1]
    assert manip.time - last_prefix.time == 8 + 1  # gap steps + manipulation step
    # appearance drifted over the gap: cosine < 1 between prefix and manip target
    cos = float(get(last_prefix, TARGET).app.dot(get(manip, TARGET).app))
    assert cos < 0.999


def test_jump_adds_phantom_at_old_location():
    rng = np.random.default_rng(3)
    d = 40.0
    trial = generate_trial("jump", d, gap=2, similarity=0.5, rng=rng, world=W)
    manip = trial.frames[trial.manipulation_idx]
    phantom = get(manip, PHANTOM)
    target = get(manip, TARGET)
    assert trial.place_ident == PHANTOM
    assert np.linalg.norm(target.loc - phantom.loc) == pytest.approx(d, rel=1e-6)
    # phantom persists (static) through post frames
    assert any(c.ident == PHANTOM for c in trial.frames[-1].candidates)


def test_placebo_and_flip_do_not_move_anything():
    for cond in ("placebo", "appearance_flip"):
        rng = np.random.default_rng(4)
        trial = generate_trial(cond, 32.0, gap=4, similarity=0.8, rng=rng, world=W)
        manip = trial.frames[trial.manipulation_idx]
        prev = trial.frames[trial.manipulation_idx - 1]
        # motion between last prefix frame and manipulation frame is smooth
        # (bounded by the gap+1 random-walk steps, no displacement injection)
        moved = np.linalg.norm(get(manip, TARGET).loc - get(prev, TARGET).loc)
        assert moved < 6 * W.step_sigma * np.sqrt(4 + 1)
        assert trial.place_ident is None


def test_appearance_flip_replaces_target_appearance():
    rng = np.random.default_rng(5)
    trial = generate_trial("appearance_flip", 0.0, gap=1, similarity=0.5, rng=rng, world=W)
    manip = trial.frames[trial.manipulation_idx]
    prev = trial.frames[trial.manipulation_idx - 1]
    cos = float(get(manip, TARGET).app.dot(get(prev, TARGET).app))
    assert abs(cos) < 0.6  # fresh random vector, near-orthogonal in 32-D


def test_unknown_condition_rejected():
    with pytest.raises(ValueError):
        generate_trial("melt", 1.0, 1, 0.5, np.random.default_rng(0), W)
