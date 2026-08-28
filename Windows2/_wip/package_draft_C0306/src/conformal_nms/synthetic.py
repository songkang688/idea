"""Synthetic detection-scene generator (tiny-COCO mock).

Generates i.i.d. scenes on the unit square. Each scene has:
  * ground-truth (GT) boxes — optionally placed in tight clusters so that
    neighbouring GT boxes overlap (the CrowdHuman-style regime where NMS
    blind spots are hypothesised to live, per exp_05 H1);
  * pre-NMS candidate boxes with scores — jittered copies of each GT box plus
    background false positives. Scores increase with candidate-to-GT IoU
    through a noisy sigmoid, plus a per-object difficulty offset, so the
    score ordering is informative but imperfect (as with a real detector).

The generator is the *stand-in* for the candidate-cache harvester of the real
killer experiment (module 1 in exp_05): any code downstream only consumes
(gt_boxes, cand_boxes, cand_scores) triples, so cached real-detector outputs
can be dropped in without touching the analysis code.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import numpy as np


@dataclass
class CrowdConfig:
    """Controls scene layout / crowdedness."""

    objects_per_scene: float = 5.0   # Poisson mean (min 1 object per scene)
    cluster_fraction: float = 0.3    # P(next spawn event is a cluster, not a single)
    max_cluster_size: int = 4        # cluster sizes drawn uniformly from {2..max}
    cluster_spread: float = 0.35     # centre offset sd inside a cluster, x box size
    size_mean: float = 0.14          # mean box side length (unit-square image)
    size_sigma: float = 0.25         # lognormal sigma of box side length


@dataclass
class DetectorConfig:
    """Controls the simulated detector's candidate cloud and score model."""

    candidates_per_object: float = 8.0  # Poisson mean per GT object
    center_jitter: float = 0.07         # centre offset sd, x box size
    scale_jitter: float = 0.07          # lognormal sigma on candidate w/h
    score_iou_gain: float = 6.0         # logit slope on candidate-to-source-GT IoU
    score_bias: float = -3.2            # logit intercept for object candidates
    score_noise: float = 0.7            # logit noise sd
    difficulty_sd: float = 0.6          # per-object logit offset sd (hard/easy objects)
    fp_per_scene: float = 12.0          # Poisson mean of background false positives
    fp_score_bias: float = -2.2         # logit intercept for false positives


@dataclass
class Scene:
    gt_boxes: np.ndarray     # (G, 4) xyxy
    cand_boxes: np.ndarray   # (C, 4) xyxy, pre-NMS candidate cache
    cand_scores: np.ndarray  # (C,) in (0, 1)


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def _center_to_xyxy(cx: float, cy: float, w: float, h: float) -> np.ndarray:
    return np.array([cx - w / 2.0, cy - h / 2.0, cx + w / 2.0, cy + h / 2.0])


def _clip_boxes(boxes: np.ndarray) -> np.ndarray:
    return np.clip(boxes, 0.0, 1.0)


def _iou_single(a: np.ndarray, b: np.ndarray) -> float:
    lt = np.maximum(a[:2], b[:2])
    rb = np.minimum(a[2:], b[2:])
    wh = np.clip(rb - lt, 0.0, None)
    inter = wh[0] * wh[1]
    area_a = max(a[2] - a[0], 0.0) * max(a[3] - a[1], 0.0)
    area_b = max(b[2] - b[0], 0.0) * max(b[3] - b[1], 0.0)
    union = area_a + area_b - inter
    return float(inter / union) if union > 0 else 0.0


def sample_gt_boxes(rng: np.random.Generator, cfg: CrowdConfig) -> np.ndarray:
    """Sample GT boxes for one scene; clusters produce overlapping neighbours."""
    n = max(1, int(rng.poisson(cfg.objects_per_scene)))
    boxes: list[np.ndarray] = []
    while len(boxes) < n:
        remaining = n - len(boxes)
        make_cluster = remaining >= 2 and rng.random() < cfg.cluster_fraction
        k = int(rng.integers(2, cfg.max_cluster_size + 1)) if make_cluster else 1
        k = min(k, remaining)
        cx, cy = rng.uniform(0.15, 0.85, size=2)
        w0 = cfg.size_mean * float(rng.lognormal(0.0, cfg.size_sigma))
        h0 = cfg.size_mean * float(rng.lognormal(0.0, cfg.size_sigma))
        for _ in range(k):
            dx = float(rng.normal(0.0, cfg.cluster_spread * w0)) if k > 1 else 0.0
            dy = float(rng.normal(0.0, cfg.cluster_spread * h0)) if k > 1 else 0.0
            # Members of a cluster share a base size (same object category/scale),
            # with mild per-instance variation.
            w = w0 * float(rng.lognormal(0.0, 0.10))
            h = h0 * float(rng.lognormal(0.0, 0.10))
            boxes.append(_center_to_xyxy(cx + dx, cy + dy, w, h))
    return _clip_boxes(np.stack(boxes))


def sample_candidates(
    rng: np.random.Generator, gt_boxes: np.ndarray, det: DetectorConfig
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate the pre-NMS candidate cache for one scene."""
    cand_boxes: list[np.ndarray] = []
    logits: list[float] = []

    for g in gt_boxes:
        w = float(g[2] - g[0])
        h = float(g[3] - g[1])
        cx = float(g[0] + g[2]) / 2.0
        cy = float(g[1] + g[3]) / 2.0
        difficulty = float(rng.normal(0.0, det.difficulty_sd))
        m = int(rng.poisson(det.candidates_per_object))
        for _ in range(m):
            ncx = cx + float(rng.normal(0.0, det.center_jitter * w))
            ncy = cy + float(rng.normal(0.0, det.center_jitter * h))
            nw = w * float(rng.lognormal(0.0, det.scale_jitter))
            nh = h * float(rng.lognormal(0.0, det.scale_jitter))
            box = _clip_boxes(_center_to_xyxy(ncx, ncy, nw, nh))
            iou = _iou_single(box, g)
            logit = (
                det.score_bias
                + det.score_iou_gain * iou
                + difficulty
                + float(rng.normal(0.0, det.score_noise))
            )
            cand_boxes.append(box)
            logits.append(logit)

    n_fp = int(rng.poisson(det.fp_per_scene))
    for _ in range(n_fp):
        fcx, fcy = rng.uniform(0.05, 0.95, size=2)
        fw = 0.12 * float(rng.lognormal(0.0, 0.4))
        fh = 0.12 * float(rng.lognormal(0.0, 0.4))
        box = _clip_boxes(_center_to_xyxy(fcx, fcy, fw, fh))
        logit = det.fp_score_bias + float(rng.normal(0.0, det.score_noise))
        cand_boxes.append(box)
        logits.append(logit)

    if not cand_boxes:
        return np.zeros((0, 4)), np.zeros(0)

    boxes_arr = np.stack(cand_boxes)
    scores_arr = _sigmoid(np.asarray(logits, dtype=np.float64))
    perm = rng.permutation(boxes_arr.shape[0])  # kill any ordering artefacts
    return boxes_arr[perm], scores_arr[perm]


def generate_dataset(
    rng: np.random.Generator,
    n_scenes: int,
    crowd: CrowdConfig,
    det: DetectorConfig,
) -> list[Scene]:
    """Generate ``n_scenes`` i.i.d. scenes (the exchangeable units for splits)."""
    scenes = []
    for _ in range(n_scenes):
        gt = sample_gt_boxes(rng, crowd)
        cand, scores = sample_candidates(rng, gt, det)
        scenes.append(Scene(gt_boxes=gt, cand_boxes=cand, cand_scores=scores))
    return scenes
