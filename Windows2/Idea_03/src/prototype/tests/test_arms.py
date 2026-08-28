import pytest
import torch

from vpt_registers.config import ExperimentConfig
from vpt_registers.train import pretrain_backbone, train_arm


@pytest.fixture(scope="module")
def backbones(tiny_cfg, seed_data):
    return {
        v: pretrain_backbone(tiny_cfg, v, seed=0, data=seed_data)
        for v in tiny_cfg.backbones
    }


def test_backbone_variants(backbones, tiny_cfg):
    assert backbones["register_free"].cfg.num_registers == 0
    assert backbones["register_equipped"].cfg.num_registers == tiny_cfg.num_registers
    for m in backbones.values():
        assert all(not p.requires_grad for p in m.parameters()), "backbone must be frozen"


def test_all_five_arms_run_and_token_ownership(backbones, tiny_cfg, seed_data):
    bb = backbones["register_free"]
    before = {k: v.clone() for k, v in bb.state_dict().items()}
    results = {}
    learned_tokens = None
    for arm in ["no_token", "frozen_random", "learned", "learned_frozen", "sink_only"]:
        res = train_arm(
            tiny_cfg, bb, "register_free", arm, seed=0, data=seed_data,
            learned_tokens=learned_tokens if arm == "learned_frozen" else None,
        )
        if arm == "learned":
            learned_tokens = res.tokens
        results[arm] = res
        assert 0.0 <= res.miou <= 1.0
        assert 0.0 <= res.pixel_acc <= 1.0
    # backbone untouched by any arm
    for k, v in bb.state_dict().items():
        assert torch.equal(before[k], v), f"backbone param {k} changed during arm training"
    # token ownership semantics
    assert results["no_token"].tokens is None
    assert results["learned_frozen"].tokens is not None
    assert torch.equal(results["learned_frozen"].tokens, results["learned"].tokens), (
        "learned_frozen must reuse the learned arm's tokens verbatim"
    )
    assert results["sink_only"].prompt_is_sink
    assert not results["learned"].prompt_is_sink


def test_frozen_random_tokens_are_never_trained(backbones, tiny_cfg, seed_data):
    bb = backbones["register_free"]
    res = train_arm(tiny_cfg, bb, "register_free", "frozen_random", seed=0, data=seed_data)
    from vpt_registers.train import _init_prompts

    init = _init_prompts(tiny_cfg.num_prompts, bb.cfg.dim, seed=0)
    assert torch.equal(res.tokens, init), "frozen_random tokens must equal their init"


def test_learned_tokens_actually_move(backbones, tiny_cfg, seed_data):
    bb = backbones["register_free"]
    res = train_arm(tiny_cfg, bb, "register_free", "learned", seed=0, data=seed_data)
    from vpt_registers.train import _init_prompts

    init = _init_prompts(tiny_cfg.num_prompts, bb.cfg.dim, seed=0)
    assert not torch.allclose(res.tokens, init), "learned tokens must be updated"


def test_learned_frozen_requires_learned():
    with pytest.raises(ValueError, match="learned_frozen"):
        ExperimentConfig(arms=["no_token", "learned_frozen"])


def test_training_learns_something(backbones, tiny_cfg, seed_data):
    """Even the tiny test budget must beat uniform-random mIoU on the
    no_token arm (4 labels => random ~ mIoU 0.1)."""
    bb = backbones["register_free"]
    res = train_arm(tiny_cfg, bb, "register_free", "no_token", seed=0, data=seed_data)
    assert res.miou > 0.12, f"no_token mIoU suspiciously low: {res.miou}"
