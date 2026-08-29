"""The four coverage pipelines compared by the prototype.

  A  keep_all            : conformal on the full pre-NMS candidate cache
                           (validity check + set-size upper bound; baseline 5
                           of exp_05).
  B  precalib_then_nms   : calibrate pre-NMS, then run standard NMS at deploy
                           time and apply the same threshold to the survivors.
                           This is the pipeline whose coverage the C-0306
                           claim says silently breaks.
  C  conformal_after_nms : SeqCRC-style — treat NMS as part of the model and
                           calibrate on the post-NMS lists. Marginally valid
                           *only if* blind-spot + miss rate <= alpha; when it
                           is not, q_hat = +inf (the calibration itself
                           certifies that nominal coverage is unachievable at
                           any threshold).
  D  cps                 : coverage-preserving suppression — calibrate on the
                           full cache at the stricter tau_cal = tau + (1-kappa),
                           then suppress within the prediction set at merge
                           threshold kappa (provable transfer of the guarantee;
                           see suppression.py).

All pipelines are calibrated on the calibration split and evaluated on the
test split; coverage is always evaluated at IoU >= tau against GT.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np

from .conformal import (
    covering_score_per_gt,
    nonconformity_scores,
    object_coverage,
    prediction_mask,
    split_conformal_qhat,
)
from .nms import greedy_nms
from .suppression import coverage_preserving_suppression, required_calibration_iou
from .synthetic import Scene

INF = float("inf")


@dataclass
class PipelineResult:
    name: str
    nominal: float
    coverage: float
    coverage_se: float
    n_test_gt: int
    qhat: float
    achievable_cap: float          # max coverage any threshold could reach on calib pool
    mean_set_size: float           # boxes per scene in the final output set
    duplicates_per_covered_gt: float
    blind_stratum_coverage: float | None = None  # coverage on post-NMS-blind GTs
    blind_stratum_n: int = 0
    notes: str = ""


def _binomial_se(p: float, n: int) -> float:
    return math.sqrt(max(p * (1.0 - p), 1e-12) / n) if n > 0 else 0.0


def _evaluate(
    name: str,
    test_scenes: list[Scene],
    qhat: float,
    tau_eval: float,
    alpha: float,
    achievable_cap: float,
    test_pool_fn,
    suppress_fn=None,
    blind_flags: list[np.ndarray] | None = None,
    notes: str = "",
) -> PipelineResult:
    """Shared evaluation: build per-scene output sets, pool per-GT coverage."""
    covered_all: list[np.ndarray] = []
    set_sizes: list[int] = []
    dup_total = 0
    covered_gt_total = 0

    for scene in test_scenes:
        pool_idx = np.asarray(test_pool_fn(scene), dtype=np.int64)
        boxes = scene.cand_boxes[pool_idx]
        scores = scene.cand_scores[pool_idx]
        mask = prediction_mask(scores, qhat)
        if suppress_fn is not None:
            kept_local = suppress_fn(boxes, scores, mask)
            final_idx = pool_idx[kept_local]
        else:
            final_idx = pool_idx[np.flatnonzero(mask)]

        fboxes = scene.cand_boxes[final_idx]
        fscores = scene.cand_scores[final_idx]
        cov = object_coverage(
            scene.gt_boxes, fboxes, fscores, np.ones(final_idx.size, bool), tau_eval
        )
        covered_all.append(cov)
        set_sizes.append(int(final_idx.size))

        if scene.gt_boxes.shape[0] and final_idx.size:
            from .boxes import iou_matrix

            counts = (iou_matrix(scene.gt_boxes, fboxes) >= tau_eval).sum(axis=1)
            dup_total += int(np.clip(counts - 1, 0, None).sum())
            covered_gt_total += int((counts >= 1).sum())

    covered = np.concatenate(covered_all) if covered_all else np.zeros(0, bool)
    n_gt = covered.size
    coverage = float(covered.mean()) if n_gt else 0.0

    blind_cov = None
    blind_n = 0
    if blind_flags is not None:
        bf = np.concatenate(blind_flags) if blind_flags else np.zeros(0, bool)
        blind_n = int(bf.sum())
        if blind_n:
            blind_cov = float(covered[bf].mean())

    return PipelineResult(
        name=name,
        nominal=1.0 - alpha,
        coverage=coverage,
        coverage_se=_binomial_se(coverage, n_gt),
        n_test_gt=n_gt,
        qhat=qhat,
        achievable_cap=achievable_cap,
        mean_set_size=float(np.mean(set_sizes)) if set_sizes else 0.0,
        duplicates_per_covered_gt=(
            dup_total / covered_gt_total if covered_gt_total else 0.0
        ),
        blind_stratum_coverage=blind_cov,
        blind_stratum_n=blind_n,
        notes=notes,
    )


def _full_pool(scene: Scene) -> np.ndarray:
    return np.arange(scene.cand_boxes.shape[0], dtype=np.int64)


def _nms_pool_fn(nms_iou: float, score_floor: float):
    def fn(scene: Scene) -> np.ndarray:
        return greedy_nms(scene.cand_boxes, scene.cand_scores, nms_iou, score_floor)

    return fn


def _calibrate(
    calib_scenes: list[Scene], tau: float, alpha: float, candidate_filter=None
) -> tuple[float, float]:
    """Returns (q_hat, achievable coverage cap on the calibration pool)."""
    s = nonconformity_scores(calib_scenes, tau, candidate_filter)
    qhat = split_conformal_qhat(s, alpha)
    cap = float(np.isfinite(s).mean()) if s.size else 0.0
    return qhat, cap


def _blind_flags_for_test(
    test_scenes: list[Scene], tau: float, nms_iou: float, score_floor: float
) -> list[np.ndarray]:
    from .blind_spot import blind_spot_flags

    return [
        blind_spot_flags(sc, tau, nms_iou, score_floor)[1] for sc in test_scenes
    ]


def run_keep_all(calib, test, alpha, tau) -> PipelineResult:
    qhat, cap = _calibrate(calib, tau, alpha)
    return _evaluate(
        "A keep-all + conformal (pre-NMS)",
        test, qhat, tau, alpha, cap, _full_pool,
        notes="validity check; set-size upper bound",
    )


def run_precalib_then_nms(
    calib, test, alpha, tau, nms_iou, score_floor
) -> PipelineResult:
    qhat, cap = _calibrate(calib, tau, alpha)  # calibrated PRE-NMS
    return _evaluate(
        "B calibrate pre-NMS -> deploy NMS",
        test, qhat, tau, alpha, cap,
        _nms_pool_fn(nms_iou, score_floor),
        blind_flags=_blind_flags_for_test(test, tau, nms_iou, score_floor),
        notes=f"NMS iou={nms_iou} applied AFTER calibration (the broken pipeline)",
    )


def run_conformal_after_nms(
    calib, test, alpha, tau, nms_iou, score_floor
) -> PipelineResult:
    pool_fn = _nms_pool_fn(nms_iou, score_floor)
    qhat, cap = _calibrate(calib, tau, alpha, candidate_filter=pool_fn)
    notes = f"SeqCRC-style; NMS iou={nms_iou} inside model"
    if math.isinf(qhat):
        notes += (
            "; q_hat=inf -> nominal UNACHIEVABLE post-NMS "
            f"(achievable cap ~ {cap:.3f} < 1-alpha)"
        )
    return _evaluate(
        "C conformal AFTER NMS (SeqCRC-style)",
        test, qhat, tau, alpha, cap, pool_fn,
        blind_flags=_blind_flags_for_test(test, tau, nms_iou, score_floor),
        notes=notes,
    )


def run_cps(calib, test, alpha, tau, kappa, redundancy) -> PipelineResult:
    tau_cal = required_calibration_iou(tau, kappa)
    qhat, cap = _calibrate(calib, tau_cal, alpha)

    def suppress_fn(boxes, scores, mask):
        kept_global_order = coverage_preserving_suppression(
            boxes, scores, mask, kappa, redundancy
        )
        return kept_global_order

    return _evaluate(
        "D coverage-preserving suppression",
        test, qhat, tau, alpha, cap, _full_pool, suppress_fn=suppress_fn,
        notes=(
            f"calibrated at tau_cal={tau_cal:.2f}, merge kappa={kappa}, "
            f"redundancy={redundancy}; provable coverage transfer"
        ),
    )
