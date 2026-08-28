"""Experiment configuration: dataclasses + YAML loading."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .synthetic_data import DataConfig
from .tiny_vit import ViTConfig

VALID_ARMS = ("no_token", "frozen_random", "learned", "learned_frozen", "sink_only")
VALID_BACKBONES = ("register_free", "register_equipped")


@dataclass
class TrainConfig:
    pretrain_steps: int = 300
    pretrain_lr: float = 3e-3
    arm_steps: int = 400
    arm_lr: float = 3e-3
    batch_size: int = 32
    train_scenes: int = 512
    val_scenes: int = 192
    paired_scenes: int = 64  # scenes for the paired-nuisance invariance metric


@dataclass
class ExperimentConfig:
    name: str = "default"
    seeds: list[int] = field(default_factory=lambda: [0, 1, 2])
    backbones: list[str] = field(default_factory=lambda: ["register_free", "register_equipped"])
    arms: list[str] = field(
        default_factory=lambda: ["no_token", "frozen_random", "learned", "learned_frozen"]
    )
    num_prompts: int = 4
    num_registers: int = 4  # register count on the register_equipped variant
    head_kind: str = "linear"  # or "conv"
    data: DataConfig = field(default_factory=DataConfig)
    model: ViTConfig = field(default_factory=ViTConfig)
    train: TrainConfig = field(default_factory=TrainConfig)

    def __post_init__(self):
        for a in self.arms:
            if a not in VALID_ARMS:
                raise ValueError(f"unknown arm {a!r}; valid: {VALID_ARMS}")
        for b in self.backbones:
            if b not in VALID_BACKBONES:
                raise ValueError(f"unknown backbone {b!r}; valid: {VALID_BACKBONES}")
        if "learned_frozen" in self.arms and "learned" not in self.arms:
            raise ValueError("arm 'learned_frozen' requires arm 'learned' (it freezes its tokens)")
        # Keep the geometry consistent between data generator and model.
        self.model.image_size = self.data.image_size
        self.model.patch_size = self.data.patch_size


def load_config(path: str | Path) -> ExperimentConfig:
    raw = yaml.safe_load(Path(path).read_text()) or {}
    data = DataConfig(**raw.pop("data", {}))
    model = ViTConfig(**raw.pop("model", {}))
    train = TrainConfig(**raw.pop("train", {}))
    return ExperimentConfig(data=data, model=model, train=train, **raw)
