import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from vpt_registers.config import ExperimentConfig, TrainConfig
from vpt_registers.synthetic_data import DataConfig
from vpt_registers.tiny_vit import ViTConfig
from vpt_registers.train import make_seed_data


@pytest.fixture(scope="session")
def tiny_cfg() -> ExperimentConfig:
    """Miniature everything so the whole suite runs in seconds on CPU."""
    return ExperimentConfig(
        name="test",
        seeds=[0],
        backbones=["register_free", "register_equipped"],
        arms=["no_token", "frozen_random", "learned", "learned_frozen", "sink_only"],
        num_prompts=2,
        num_registers=2,
        data=DataConfig(image_size=16, patch_size=4, num_classes=3),
        model=ViTConfig(dim=24, depth=2, heads=2),
        train=TrainConfig(
            pretrain_steps=20,
            arm_steps=25,
            batch_size=16,
            train_scenes=64,
            val_scenes=32,
            paired_scenes=16,
        ),
    )


@pytest.fixture(scope="session")
def seed_data(tiny_cfg):
    return make_seed_data(tiny_cfg, seed=0)
