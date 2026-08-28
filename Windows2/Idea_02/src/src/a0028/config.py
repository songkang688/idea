"""YAML config loading for the synthetic runner."""

from __future__ import annotations

from pathlib import Path

import yaml

from .world import WorldParams

REQUIRED_TOP_LEVEL = ("seed", "world", "tracker", "grid", "experiments")


def load_config(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    missing = [k for k in REQUIRED_TOP_LEVEL if k not in cfg]
    if missing:
        raise KeyError(f"config {path} missing keys: {missing}")
    cfg["world_params"] = WorldParams.from_dict(cfg["world"])
    return cfg
