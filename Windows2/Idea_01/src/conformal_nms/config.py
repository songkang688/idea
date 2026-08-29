"""YAML config loading into the generator/experiment dataclasses."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .synthetic import CrowdConfig, DetectorConfig


@dataclass
class ExperimentConfig:
    seed: int = 0
    n_scenes: int = 400              # per crowd level
    calib_fraction: float = 0.5
    alpha: float = 0.1
    tau_iou: float = 0.5             # coverage IoU threshold
    nms_iou_grid: list = field(default_factory=lambda: [0.3, 0.5, 0.7])
    nms_deploy_iou: float = 0.5
    nms_score_floor: float = 0.05
    cps_kappa: float = 0.85
    cps_redundancy: int = 1
    crowd_levels: dict = field(default_factory=dict)   # name -> CrowdConfig
    detector: DetectorConfig = field(default_factory=DetectorConfig)


def _build(cls, d: dict | None):
    d = d or {}
    known = {f for f in cls.__dataclass_fields__}
    unknown = set(d) - known
    if unknown:
        raise KeyError(f"unknown {cls.__name__} keys: {sorted(unknown)}")
    return cls(**d)


def load_config(path: str | Path) -> ExperimentConfig:
    raw = yaml.safe_load(Path(path).read_text())
    crowd_levels = {
        name: _build(CrowdConfig, level_cfg)
        for name, level_cfg in (raw.pop("crowd_levels", None) or {}).items()
    }
    if not crowd_levels:
        crowd_levels = {"default": CrowdConfig()}
    detector = _build(DetectorConfig, raw.pop("detector", None))
    cfg = _build(ExperimentConfig, raw)
    cfg.crowd_levels = crowd_levels
    cfg.detector = detector
    return cfg
