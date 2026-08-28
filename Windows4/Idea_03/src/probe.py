"""Compatibility shim — the linear probe now lives in alphasmoke.probes.

Full implementation (encoder registry with documented checkpoint stubs, 1x1-conv
LinearProbeHead, training/eval loops wired to the protocol metrics, CLI):
``alphasmoke/probes/encoder_linear_probe.py``. Design: metrics_protocol.md §7;
gate K-A1: experiments.md §2. No pretrained weights and no scores are shipped —
checkpoint acquisition happens at runbook step R2.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass

sys.path.insert(0, os.path.dirname(__file__))

from alphasmoke.probes.encoder_linear_probe import (  # noqa: E402,F401
    ENCODER_REGISTRY,
    EncoderSpec,
    load_encoder,
)


@dataclass
class ProbeSpec:
    """Skeleton-compatible spec; resolve via alphasmoke's ENCODER_REGISTRY."""

    encoder_name: str
    frozen: bool = True
    note: str = "Checkpoints are documented stubs (runbook R2); no accuracies are invented."
