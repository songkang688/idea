from pathlib import Path

import pytest

from vpt_registers.config import ExperimentConfig, load_config

CONFIGS = Path(__file__).parent.parent / "configs"


def test_all_committed_configs_load():
    for f in sorted(CONFIGS.glob("*.yaml")):
        cfg = load_config(f)
        assert cfg.seeds and cfg.arms and cfg.backbones, f.name
        # data/model geometry kept consistent by __post_init__
        assert cfg.model.image_size == cfg.data.image_size
        assert cfg.model.patch_size == cfg.data.patch_size


def test_default_config_has_the_four_mandated_arms():
    cfg = load_config(CONFIGS / "default.yaml")
    assert cfg.arms == ["no_token", "frozen_random", "learned", "learned_frozen"]


def test_with_sink_config_adds_the_h_control():
    cfg = load_config(CONFIGS / "with_sink.yaml")
    assert "sink_only" in cfg.arms


def test_invalid_arm_rejected():
    with pytest.raises(ValueError, match="unknown arm"):
        ExperimentConfig(arms=["no_token", "warp_drive"])


def test_invalid_backbone_rejected():
    with pytest.raises(ValueError, match="unknown backbone"):
        ExperimentConfig(backbones=["resnet50"])
