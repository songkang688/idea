"""Configuration loading and seed control (same contract as Idea_01/Idea_02)."""

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

#: Which failure the synthetic pair simulates. The whole point of the smoke run
#: is that `classify_outcome` must recover the mode that was planted here.
TAX_MODES = ("none", "format", "policy", "representation")


@dataclass
class Config:
    """Run configuration. Defaults describe the synthetic smoke run."""

    checkpoints: list[str] = field(default_factory=lambda: ["base", "chat"])
    decode: str = "constrained_xyxy"
    probe: str = "linear_visual_tokens"
    optional: str = "text_only_dpo_lora"
    eval_modes: list[str] = field(
        default_factory=lambda: ["freeform", "constrained", "likelihood_rank"]
    )
    tax_mode: str = "policy"
    n_examples: int = 256
    token_dim: int = 16
    n_distractors: int = 16
    image_size: float = 100.0
    chatty_rate: float = 0.35
    policy_noise: float = 0.18
    representation_noise: float = 0.35
    iou_threshold: float = 0.5
    gap_tolerance: float = 0.02
    seed: int = 0
    data_root: str = ""

    def __post_init__(self) -> None:
        if self.tax_mode not in TAX_MODES:
            raise ValueError(f"tax_mode must be one of {TAX_MODES}, got {self.tax_mode!r}")

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
    random.seed(seed)
    np.random.seed(seed % (2**32))
    os.environ.setdefault("PYTHONHASHSEED", str(seed))
    return np.random.default_rng(seed)
