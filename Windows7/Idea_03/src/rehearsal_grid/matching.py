"""Gradient-norm matching: per-layer (primary) and global (secondary).

Stage 5 left the two conventions symmetric and said divergence between them would
itself be a finding. Stage 6 rejected that as unfalsifiable-adjacent -- with no
declared primary, every possible outcome becomes a result. Per-layer is the
pre-registered primary, because per-layer gradient disparity across modalities is
documented (arXiv:2606.17296) and a global match can leave individual blocks badly
mismatched while reporting a perfect overall ratio.
"""

from __future__ import annotations

import numpy as np

EPS = 1e-8
MAX_SCALE = 10.0


def global_norm_scale(
    ref_grads: dict[str, np.ndarray],
    txt_grads: dict[str, np.ndarray],
    *,
    max_scale: float = MAX_SCALE,
) -> float:
    """SECONDARY convention: one scalar from the whole-tower norm ratio."""
    ref = np.sqrt(sum(float(np.sum(g**2)) for g in ref_grads.values()))
    txt = np.sqrt(sum(float(np.sum(g**2)) for g in txt_grads.values()))
    return float(np.clip(ref / (txt + EPS), 0.0, max_scale))


def per_layer_scale(
    ref_grads: dict[str, np.ndarray],
    txt_grads: dict[str, np.ndarray],
    *,
    max_scale: float = MAX_SCALE,
) -> dict[str, float]:
    """PRIMARY convention: one scalar per transformer block."""
    out: dict[str, float] = {}
    for name, txt in txt_grads.items():
        ref = ref_grads.get(name)
        if ref is None:
            out[name] = 1.0
            continue
        rn = float(np.linalg.norm(ref))
        tn = float(np.linalg.norm(txt))
        out[name] = float(np.clip(rn / (tn + EPS), 0.0, max_scale))
    return out


def mismatch_under_global(
    ref_grads: dict[str, np.ndarray],
    txt_grads: dict[str, np.ndarray],
) -> dict[str, float]:
    """Per-layer residual mismatch left behind by the global convention.

    This is the diagnostic that justifies the choice of primary. If it is near 1.0
    everywhere the two conventions are interchangeable and H3 is uninteresting; the
    wider it spreads, the more the choice of convention could drive the headline --
    which is precisely why the choice is frozen in advance.
    """
    s = global_norm_scale(ref_grads, txt_grads)
    out: dict[str, float] = {}
    for name, txt in txt_grads.items():
        ref = ref_grads.get(name)
        if ref is None:
            continue
        rn = float(np.linalg.norm(ref))
        tn = float(np.linalg.norm(txt)) * s
        out[name] = tn / (rn + EPS)
    return out


def effective_lr_multiplier(scales: dict[str, float] | float) -> float:
    """How much the matching inflates the effective LR on the language tower.

    Scaling a loss to hit a target gradient norm changes the step size on those
    parameters. That is a real stability risk, so it gets logged as a number rather
    than waved off: a run whose language tower is silently training at 6x the
    nominal LR is not a clean rehearsal experiment.
    """
    if isinstance(scales, (int, float)):
        return float(scales)
    return float(np.mean(list(scales.values()))) if scales else 1.0
