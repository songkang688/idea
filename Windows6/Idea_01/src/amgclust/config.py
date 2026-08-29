"""Configuration loading and seed control.

PyYAML is optional. When it is absent a restricted parser handles the flat
`key: value` / `key: [a, b, c]` subset that this package's configs use. The
parser deliberately refuses anything it does not understand rather than
guessing, so a config silently losing a field is impossible.
"""

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
    """Run configuration for an agreement experiment.

    Defaults describe the synthetic smoke run, not the real protocol. The
    real protocol lives in ``configs/e1_killer.yaml``.
    """

    window: str = "abdomen"
    k_means: list[int] = field(default_factory=lambda: [8, 16, 32])
    metrics: list[str] = field(default_factory=lambda: ["hungarian_iou", "ari", "boundary_f"])
    counterfactuals: list[str] = field(default_factory=lambda: ["intensity_remap", "texture_shuffle"])
    amg_points_per_side: list[int] = field(default_factory=lambda: [16, 32])
    n_slices: int = 100
    seed: int = 0
    boundary_tolerance_px: int = 2
    slic_n_segments: int = 64
    slic_compactness: float = 0.25
    remap_gamma: float = 0.5
    shuffle_tile: int = 8
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
    """Load a config, falling back to dataclass defaults when path is None."""
    if path is None:
        return Config()
    text = Path(path).read_text(encoding="utf-8")
    raw = yaml.safe_load(text) if yaml is not None else _parse_flat_yaml(text)
    return Config.from_dict(raw or {})


def set_seed(seed: int) -> np.random.Generator:
    """Fix every RNG this package can reach and return a fresh Generator.

    Returning the Generator is deliberate: functions take it explicitly rather
    than reading global state, so a run stays reproducible even if a caller
    reseeds midway.
    """
    random.seed(seed)
    np.random.seed(seed % (2**32))
    os.environ.setdefault("PYTHONHASHSEED", str(seed))
    return np.random.default_rng(seed)
