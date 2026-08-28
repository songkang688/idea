"""Config loading with dotted-key overrides.

`--override a.b.c=value` mirrors the README usage; values parse as YAML scalars.
The thresholds block is the pre-registration artifact: eval refuses to run if any
threshold key is overridden (no post-hoc threshold motion — roadmap.md standing rule)."""

from __future__ import annotations

from typing import Dict, List

import yaml

_FROZEN_PREFIX = "thresholds."


def load_config(path: str, overrides: List[str] | None = None) -> Dict:
    with open(path) as f:
        cfg = yaml.safe_load(f)
    for ov in overrides or []:
        if "=" not in ov:
            raise ValueError(f"override must be key=value, got: {ov}")
        key, val = ov.split("=", 1)
        if key.startswith(_FROZEN_PREFIX):
            raise ValueError(
                f"refusing to override '{key}': thresholds are pre-registered and frozen "
                "(proposal §15, roadmap.md standing rules)"
            )
        node = cfg
        parts = key.split(".")
        for p in parts[:-1]:
            node = node[p]
        node[parts[-1]] = yaml.safe_load(val)
    return cfg
