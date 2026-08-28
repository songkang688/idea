"""C1-061 diversity arm (E4): oracle best-of-3 vs IoU-head argmax decomposition.

Fully implemented, numpy-only. Consumes real per-probe candidate IoUs; nothing
here fabricates them. The decomposition verdicts are the pre-registered ones
(proposal §17 / experiments E4):

  oracle drops (incl. all-mask-loss cells)  -> CAPABILITY loss (claim stands)
  oracle intact, argmax drops               -> RANKING loss (transfer to P031)
  oracle drops only in min-loss-mask cells  -> LOSS-AGGREGATION artifact
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ProbeResult:
    """One ambiguity probe evaluated on one checkpoint.

    candidate_ious[k][g]: IoU of candidate k against valid GT mask g (>=2 GTs).
    iou_head_scores[k]: the model's own predicted-IoU ranking scores.
    """

    probe_id: str
    candidate_ious: np.ndarray   # shape (K, G), K=3 for SAM multimask
    iou_head_scores: np.ndarray  # shape (K,)


def oracle_best(probe: ProbeResult) -> float:
    """max over candidates of best-matching valid GT IoU (capability readout)."""
    return float(probe.candidate_ious.max())


def argmax_selected(probe: ProbeResult) -> float:
    """IoU (vs best-matching GT) of the candidate the IoU head ranks first."""
    k = int(np.argmax(probe.iou_head_scores))
    return float(probe.candidate_ious[k].max())


def oracle_argmax_gap(probe: ProbeResult) -> float:
    return oracle_best(probe) - argmax_selected(probe)


@dataclass(frozen=True)
class DiversitySummary:
    n_probes: int
    mean_oracle: float
    mean_argmax: float
    mean_gap: float


def summarize(probes: list[ProbeResult]) -> DiversitySummary:
    if not probes:
        raise ValueError("no probes — the ambiguity probe index must be built at Phase 0")
    oracles = np.array([oracle_best(p) for p in probes])
    argmaxes = np.array([argmax_selected(p) for p in probes])
    return DiversitySummary(
        n_probes=len(probes),
        mean_oracle=float(oracles.mean()),
        mean_argmax=float(argmaxes.mean()),
        mean_gap=float((oracles - argmaxes).mean()),
    )


def decompose(
    frozen: DiversitySummary,
    ft_all_mask_loss: DiversitySummary,
    ft_min_loss_mask: DiversitySummary,
    envelope_band: float,
) -> str:
    """Pre-registered O4 decomposition verdict for one arm.

    `envelope_band` is the P082 operative band for the ambiguity cell; drops
    inside the band are treated as null (no fabricated significance — the full
    hierarchical-bootstrap CI analysis runs in the stats notebook on real data,
    this function only encodes the verdict logic).
    """
    oracle_drop_allmask = frozen.mean_oracle - ft_all_mask_loss.mean_oracle
    oracle_drop_minloss = frozen.mean_oracle - ft_min_loss_mask.mean_oracle
    argmax_drop_allmask = frozen.mean_argmax - ft_all_mask_loss.mean_argmax

    oracle_real_allmask = oracle_drop_allmask > envelope_band
    oracle_real_minloss = oracle_drop_minloss > envelope_band
    argmax_real_allmask = argmax_drop_allmask > envelope_band

    if oracle_real_allmask:
        return "CAPABILITY_LOSS: diversity-forgetting claim stands (H4)"
    if oracle_real_minloss and not oracle_real_allmask:
        return "LOSS_AGGREGATION_ARTIFACT: report as recipe finding, not forgetting"
    if argmax_real_allmask:
        return "RANKING_LOSS: transfer observation to P031; withdraw from this paper"
    return "NULL: no diversity effect outside the noise floor — report as null"
