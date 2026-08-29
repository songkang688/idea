"""Inter-rater ceiling statistics + confrontation table (B5, metrics_protocol.md §5).

Study design: 3-5 raters x 150 images per benchmark (SMOKE5K-real, SSD), stratified
by smoke-density tercile; binary masks for all images, soft annotations on a subset.

Outputs:
- pairwise IoU (binary) and pairwise MAE (soft) over all rater pairs per image;
- distribution summaries (median, IQR) per stratum and pooled — means alone hide the
  bimodality the hyperspectral 3-rater study found (arXiv:2602.10858 [S3]);
- the confrontation table: published SOTA deltas flagged "sub-ceiling" when smaller
  than the annotation-disagreement gap on the same benchmark.

Pre-registered demotion K-B4: if the pooled median pairwise IoU exceeds 0.85, H4 is
dead and the pillar moves to an appendix (stage3/stage4 threshold, not ours).
"""

from __future__ import annotations

from itertools import combinations

import numpy as np

from ..metrics.binary_metrics import iou as _iou
from ..metrics.alpha_metrics import mae as _mae


def pairwise_iou_ceiling(rater_masks: list[np.ndarray]) -> dict:
    """Pairwise IoU across raters for ONE image.

    Parameters
    ----------
    rater_masks : list of (H, W) binary masks, one per rater (>= 2).

    Returns
    -------
    {"pairs": [(i, j, iou)], "mean": float, "min": float}
    """
    if len(rater_masks) < 2:
        raise ValueError("need >= 2 raters")
    pairs = [
        (i, j, _iou(rater_masks[i], rater_masks[j]))
        for i, j in combinations(range(len(rater_masks)), 2)
    ]
    vals = np.array([p[2] for p in pairs])
    return {"pairs": pairs, "mean": float(vals.mean()), "min": float(vals.min())}


def pairwise_mae_ceiling(rater_soft: list[np.ndarray]) -> dict:
    """Pairwise MAE across raters' soft annotations for ONE image (lower = closer)."""
    if len(rater_soft) < 2:
        raise ValueError("need >= 2 raters")
    pairs = [
        (i, j, _mae(rater_soft[i], rater_soft[j]))
        for i, j in combinations(range(len(rater_soft)), 2)
    ]
    vals = np.array([p[2] for p in pairs])
    return {"pairs": pairs, "mean": float(vals.mean()), "max": float(vals.max())}


def ceiling_summary(
    per_image_pairwise: list[float],
    strata: list[int] | None = None,
) -> dict:
    """Distribution summary of per-image pairwise agreement values.

    Parameters
    ----------
    per_image_pairwise : one agreement value per image (e.g. mean pairwise IoU).
    strata : optional stratum id per image (density terciles).

    Returns median/IQR pooled and per stratum; the demotion check K-B4 reads
    ``pooled["median"]``.
    """
    vals = np.asarray(per_image_pairwise, dtype=float)
    if vals.ndim != 1 or len(vals) == 0:
        raise ValueError("expected non-empty 1-D list of per-image values")

    def _summ(v: np.ndarray) -> dict:
        q1, med, q3 = np.quantile(v, [0.25, 0.5, 0.75])
        return {
            "n": int(len(v)),
            "median": float(med),
            "iqr": (float(q1), float(q3)),
            "mean": float(v.mean()),
        }

    out = {"pooled": _summ(vals)}
    if strata is not None:
        strata_arr = np.asarray(strata)
        if strata_arr.shape != vals.shape:
            raise ValueError("strata must align with per-image values")
        out["per_stratum"] = {
            int(s): _summ(vals[strata_arr == s]) for s in np.unique(strata_arr)
        }
    return out


def confront_with_published_deltas(
    ceiling_median_iou: float,
    published_deltas: list[dict],
) -> list[dict]:
    """Flag published deltas below the annotation ceiling gap.

    Parameters
    ----------
    ceiling_median_iou : pooled median pairwise inter-rater IoU on the benchmark.
    published_deltas : rows like
        {"benchmark": str, "method_pair": str, "delta_iou": float, "source": str}
        — populated ONLY from verifiable published tables
        (configs/eval_protocol.yaml -> published_deltas; datasets.md section 5:
        "No delta is invented").

    Returns the rows with ``ceiling_gap`` (1 - ceiling) and ``sub_ceiling`` flags.
    A sub-ceiling delta is compatible with annotation noise; it does NOT prove the
    methods equal (rater-ceiling discussion, proposal.md section 5.3).
    """
    if not (0.0 <= ceiling_median_iou <= 1.0):
        raise ValueError("ceiling must be an IoU in [0, 1]")
    gap = 1.0 - ceiling_median_iou
    out = []
    for row in published_deltas:
        if "delta_iou" not in row or "source" not in row:
            raise ValueError("each delta row needs 'delta_iou' and a verifiable 'source'")
        enriched = dict(row)
        enriched["ceiling_gap"] = gap
        enriched["sub_ceiling"] = bool(row["delta_iou"] < gap)
        out.append(enriched)
    return out
