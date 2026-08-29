"""P177 mechanism arm (E5): module splice × trained stitch × α-interpolation.

Implemented here (pure state-dict logic, torch-tensor agnostic where possible):
  - module partition by parameter-name prefix (configs/p177_splice.yaml),
    including the set-difference rule for decoder_rest;
  - both-direction module swap between two checkpoints;
  - per-module-group α-interpolation (WiSE-FT-style continuous baseline);
  - capacity-capped stitch layers (per-channel affine; 1×1 linear secondary).

Stubbed (requires real checkpoints): stitch fitting (`fit_stitch`) and chimera
evaluation — both raise rather than fabricate.

BINDING (stage4_r2_setB.md §2 / cross-paper attack #3): every swap cell must be
run with AND without a trained stitch, in BOTH directions, alongside the
α-interpolation curves; verdicts must hold under both stitch families.
"""

from __future__ import annotations

import fnmatch
from typing import Dict, Iterable

MODULE_GROUPS: dict[str, list[str]] = {
    "image_encoder": ["image_encoder.*"],
    "prompt_encoder": ["prompt_encoder.*"],
    "decoder_cross_attn": [
        "mask_decoder.transformer.layers.*.cross_attn_token_to_image.*",
        "mask_decoder.transformer.layers.*.cross_attn_image_to_token.*",
        "mask_decoder.transformer.final_attn_token_to_image.*",
    ],
    # decoder_rest = everything under mask_decoder. MINUS decoder_cross_attn
    "decoder_rest": ["mask_decoder.*"],
}

StateDict = Dict[str, "object"]  # torch.Tensor values; typed loosely to stay import-light


def _matches(name: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(name, p) for p in patterns)


def assign_group(param_name: str) -> str | None:
    """Assign a parameter to its module group (cross-attn wins over decoder_rest)."""
    if _matches(param_name, MODULE_GROUPS["decoder_cross_attn"]):
        return "decoder_cross_attn"
    for group in ("image_encoder", "prompt_encoder"):
        if _matches(param_name, MODULE_GROUPS[group]):
            return group
    if _matches(param_name, MODULE_GROUPS["decoder_rest"]):
        return "decoder_rest"
    return None  # e.g. buffers outside the partition — reported, never silently swapped


def partition_report(state: StateDict) -> dict[str, int]:
    """Parameter-count per group — committed with the manifest so the partition
    is auditable (P177 obligation: exact parameter-name map)."""
    counts: dict[str, int] = {g: 0 for g in MODULE_GROUPS}
    counts["UNASSIGNED"] = 0
    for name in state:
        g = assign_group(name) or "UNASSIGNED"
        counts[g] = counts.get(g, 0) + 1
    return counts


def splice(host: StateDict, donor: StateDict, group: str) -> StateDict:
    """Chimera: host checkpoint with `group`'s parameters replaced by donor's.

    Directions (both mandatory):
      host=fine-tuned, donor=pre-FT  -> 'pre-FT module into FT model'
      host=pre-FT,     donor=FT      -> 'FT module into pre-FT model'
    """
    if set(host) != set(donor):
        raise ValueError("checkpoints have mismatched parameter sets — not spliceable")
    out = dict(host)
    n = 0
    for name in host:
        if assign_group(name) == group:
            out[name] = donor[name]
            n += 1
    if n == 0:
        raise ValueError(f"group {group!r} matched no parameters — check partition")
    return out


def alpha_interpolate(a: StateDict, b: StateDict, group: str, alpha: float) -> StateDict:
    """Per-module-group interpolation: group params = (1−α)·a + α·b, rest = a.

    α ∈ {0, .25, .5, .75, 1} pre-registered; the continuous superset the binary
    splice must beat for informativeness (WiSE-FT-style baseline).
    """
    import torch

    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be in [0, 1]")
    out = dict(a)
    for name in a:
        if assign_group(name) == group:
            ta, tb = a[name], b[name]
            if not (torch.is_tensor(ta) and torch.is_tensor(tb)):
                continue
            if ta.dtype.is_floating_point:
                out[name] = (1.0 - alpha) * ta + alpha * tb
    return out


# ------------------------------------------------------------------ stitches


def make_stitch(channels: int, family: str = "per_channel_affine"):
    """Capacity-capped stitch at a swapped interface (attack B8: family fixed at
    pre-registration; verdicts must hold under BOTH families)."""
    import torch.nn as nn

    if family == "per_channel_affine":

        class AffineStitch(nn.Module):
            def __init__(self, c):
                super().__init__()
                import torch

                self.scale = nn.Parameter(torch.ones(c))
                self.shift = nn.Parameter(torch.zeros(c))

            def forward(self, x):  # x: (B, C, H, W)
                return x * self.scale.view(1, -1, 1, 1) + self.shift.view(1, -1, 1, 1)

        return AffineStitch(channels)

    if family == "linear_1x1":
        import torch.nn as nn2

        return nn2.Conv2d(channels, channels, kernel_size=1, bias=True)

    raise ValueError(f"unknown stitch family {family!r} (pre-registered: per_channel_affine, linear_1x1)")


def fit_stitch(*args, **kwargs):
    """STUB — stitch training (≤500 steps, calibration split, everything else
    frozen; configs/p177_splice.yaml::stitch.training). Requires real chimera
    forward passes; raises rather than fabricating a fitted stitch."""
    raise NotImplementedError(
        "fit_stitch requires real checkpoints and the calibration split "
        "(roadmap Phase 4, after E2). Stitch-only calibration cells are mandatory."
    )


def restoration_fraction(metric_chimera: float, metric_ft: float, metric_frozen: float) -> float:
    """R = (chimera − FT) / (frozen − FT). Pre-registered E5 readout.

    Cells with a near-zero denominator (no zero-shot drop to restore) must be
    reported unnormalized (config: degenerate_denominator_policy).
    """
    denom = metric_frozen - metric_ft
    if abs(denom) < 1e-6:
        raise ZeroDivisionError(
            "near-zero zero-shot drop: report this cell unnormalized per "
            "p177_splice.yaml::degenerate_denominator_policy"
        )
    return (metric_chimera - metric_ft) / denom
