"""Configuration loading and seed control (same contract as Idea_01)."""

from __future__ import annotations

import os
import random
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

import numpy as np

try:  # pragma: no cover - environment dependent
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


@dataclass
class Config:
    """Run configuration. Defaults describe the synthetic smoke run."""

    split_types: list[str] = field(
        default_factory=lambda: ["random", "event_disjoint", "camera_disjoint"]
    )
    seeds: int = 3
    detector: str = "tiny_logreg"
    metrics: list[str] = field(default_factory=lambda: ["ap", "far_at_recall"])
    n_cameras: int = 12
    events_per_camera: int = 6
    frames_per_event: int = 10
    empty_frames_per_camera: int = 20
    feature_dim: int = 24
    camera_signature: float = 1.0
    test_cameras: int = 3
    target_recall: float = 0.8
    bootstrap_resamples: int = 200
    seed: int = 0
    data_root: str = ""

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Config":
        known = {f.name for f in fields(cls)}
        unknown = set(raw) - known
        if unknown:
            raise ValueError(
                f"unknown config keys {sorted(unknown)}; known keys are {sorted(known)}"
            )
        return cls(**raw)


def _parse_scalar(text: str) -> Any:
    text = text.strip()
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(p) for p in inner.split(",")]
    if text.lower() in {"true", "false"}:
        return text.lower() == "true"
    for caster in (int, float):
        try:
            return caster(text)
        except ValueError:
            pass
    return text.strip("'\"")


def _parse_flat_yaml(text: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line != line.lstrip():
            raise ValueError(
                f"line {lineno}: nested YAML is not supported by the fallback parser; "
                "install PyYAML or flatten the config"
            )
        if ":" not in line:
            raise ValueError(f"line {lineno}: expected 'key: value', got {raw_line!r}")
        key, value = line.split(":", 1)
        out[key.strip()] = _parse_scalar(value)
    return out


def load_config(path: str | os.PathLike[str] | None = None) -> Config:
    if path is None:
        return Config()
    text = Path(path).read_text(encoding="utf-8")
    raw = yaml.safe_load(text) if yaml is not None else _parse_flat_yaml(text)
    return Config.from_dict(raw or {})


def set_seed(seed: int) -> np.random.Generator:
    """Fix every reachable RNG and return an explicit Generator."""
    random.seed(seed)
    np.random.seed(seed % (2**32))
    os.environ.setdefault("PYTHONHASHSEED", str(seed))
    return np.random.default_rng(seed)
