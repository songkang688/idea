import numpy as np

from a0028.tracker import (
    MemoryBankTracker,
    appearance_matcher_tracker,
    location_prior_tracker,
)
from a0028.world import Candidate, unit_vector


def mk(ident, app, loc):
    return Candidate(ident, app, np.asarray(loc, dtype=float))


def test_memory_absorbs_selected_appearance():
    rng = np.random.default_rng(0)
    a, b = unit_vector(rng, 32), unit_vector(rng, 32)
    tr = MemoryBankTracker(lambda_loc=0.0, score_noise=0.0, rng=rng)
    tr.prompt(mk("target", a, [0, 0]))
    # feed frames of only 'b' at the same spot; appearance-only tracker accepts
    for _ in range(5):
        sel = tr.step([mk("distractor", b, [0, 0])])
    assert sel == "distractor"
    # template rebinds toward b (memory pollution mechanism)
    tpl = tr.template()
    assert float(tpl.dot(b)) > float(tpl.dot(a))


def test_frozen_memory_does_not_rebind():
    rng = np.random.default_rng(1)
    a, b = unit_vector(rng, 32), unit_vector(rng, 32)
    tr = MemoryBankTracker(lambda_loc=0.0, score_noise=0.0, update_memory=False, rng=rng)
    tr.prompt(mk("target", a, [0, 0]))
    for _ in range(5):
        tr.step([mk("distractor", b, [0, 0])])
    tpl = tr.template()
    assert np.allclose(tpl, a)


def test_location_dummy_follows_place():
    rng = np.random.default_rng(2)
    a, b = unit_vector(rng, 32), unit_vector(rng, 32)
    tr = location_prior_tracker(rng)
    tr.prompt(mk("target", a, [10, 10]))
    # target teleports far away; distractor lands on the old spot
    sel = tr.step([mk("target", a, [200, 200]), mk("distractor", b, [10, 10])])
    assert sel == "distractor"


def test_appearance_dummy_follows_object():
    rng = np.random.default_rng(3)
    a = unit_vector(rng, 32)
    from a0028.world import vector_with_cosine

    b = vector_with_cosine(rng, a, 0.5)
    tr = appearance_matcher_tracker(rng)
    tr.prompt(mk("target", a, [10, 10]))
    sel = tr.step([mk("target", a, [200, 200]), mk("distractor", b, [10, 10])])
    assert sel == "target"


def test_lost_when_below_threshold():
    rng = np.random.default_rng(4)
    a = unit_vector(rng, 32)
    tr = MemoryBankTracker(
        lambda_loc=0.5, accept_threshold=0.9, score_noise=0.0, rng=rng
    )
    tr.prompt(mk("target", a, [0, 0]))
    # far away and near-orthogonal appearance: score ~ 0.25 < 0.9
    sel = tr.step([mk("junk", unit_vector(rng, 32), [500, 500])])
    assert sel is None
