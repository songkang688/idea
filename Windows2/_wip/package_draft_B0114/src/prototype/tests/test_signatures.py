import torch

from vpt_registers.signatures import (
    collect_signatures,
    nuisance_sensitivity,
    sink_mass,
    token_norm_stats,
)
from vpt_registers.train import pretrain_backbone


def test_sink_mass_zero_without_tokens(tiny_cfg, seed_data):
    bb = pretrain_backbone(tiny_cfg, "register_free", seed=0, data=seed_data)
    s = sink_mass(bb, None, False, seed_data.val.images[:8])
    assert s["prompt_sink_mass_mean"] == 0.0
    assert s["register_sink_mass_mean"] == 0.0


def test_sink_mass_positive_with_tokens_and_bounded(tiny_cfg, seed_data):
    bb = pretrain_backbone(tiny_cfg, "register_equipped", seed=0, data=seed_data)
    prompt = torch.randn(tiny_cfg.num_prompts, bb.cfg.dim) * 0.02
    s = sink_mass(bb, prompt, False, seed_data.val.images[:8])
    assert 0.0 < s["prompt_sink_mass_mean"] < 1.0
    assert 0.0 < s["register_sink_mass_mean"] < 1.0
    assert len(s["prompt_sink_mass_per_layer"]) == bb.cfg.depth
    # masses onto disjoint slot groups can never exceed 1 combined
    for p, r in zip(s["prompt_sink_mass_per_layer"], s["register_sink_mass_per_layer"]):
        assert p + r <= 1.0 + 1e-6


def test_token_norm_stats_keys(tiny_cfg, seed_data):
    bb = pretrain_backbone(tiny_cfg, "register_free", seed=0, data=seed_data)
    s0 = token_norm_stats(bb, None, False, seed_data.val.images[:8])
    assert "prompt_norm_mean" not in s0
    assert 0.0 <= s0["patch_norm_outlier_frac"] <= 1.0
    prompt = torch.randn(2, bb.cfg.dim) * 0.02
    s1 = token_norm_stats(bb, prompt, False, seed_data.val.images[:8])
    assert s1["prompt_norm_mean"] > 0
    assert s1["prompt_to_patch_norm_ratio"] > 0


def test_nuisance_sensitivity_detects_global_dependence(tiny_cfg, seed_data):
    """A backbone pretrained on global objectives must show non-zero patch
    feature displacement under a pure global-nuisance swap; and the metric
    must be exactly 0 when comparing a batch against itself."""
    bb = pretrain_backbone(tiny_cfg, "register_free", seed=0, data=seed_data)
    s = nuisance_sensitivity(bb, None, False, seed_data.paired, tiny_cfg)
    assert s["nuisance_rel_displacement"] > 0.0

    same = type(seed_data.paired)(
        images=seed_data.paired.images,
        pixel_labels=seed_data.paired.pixel_labels,
        patch_labels=seed_data.paired.patch_labels,
        g=seed_data.paired.g,
        images_alt=seed_data.paired.images,  # identical rendering
        g_alt=seed_data.paired.g,
    )
    s0 = nuisance_sensitivity(bb, None, False, same, tiny_cfg)
    assert s0["nuisance_rel_displacement"] < 1e-6


def test_collect_signatures_bundle(tiny_cfg, seed_data):
    bb = pretrain_backbone(tiny_cfg, "register_free", seed=0, data=seed_data)
    prompt = torch.randn(2, bb.cfg.dim) * 0.02
    s = collect_signatures(bb, prompt, False, seed_data.val, seed_data.paired, tiny_cfg)
    for key in (
        "prompt_sink_mass_mean",
        "patch_norm_outlier_frac",
        "prompt_to_patch_norm_ratio",
        "nuisance_rel_displacement",
    ):
        assert key in s
