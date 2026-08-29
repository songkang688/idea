"""Datasets for SeeingInside.

Three sources, one Instance schema:

- SyntheticShapes (implemented, CPU): controllable contrast x solidity x size. Because the
  scene is generated, it provides *exact* counterfactuals for free: `background` is the
  identical scene rendered without the object (perfect object-out) and `swap_image` /
  `swap_mask` insert a donor object of a different shape family into the same box.
  Used for E0 decision-logic validation ONLY — never for scientific claims.

- COCO (interface): real natural instances. Requires pycocotools + the val2017 images;
  counterfactuals come from the diffusion inpainting pipeline at E1 time (interventions.py
  holds the prototype stand-ins).

- Medical (interface): MedSAM-protocol datasets; cohort rule pre-registered in
  configs/default.yaml (lowest two in-box contrast deciles). Loader is a documented stub
  until dataset selection is frozen in Phase 1 (roadmap.md).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np

from .utils import (
    HAS_CV2,
    Box,
    mask_to_tight_box,
    rms_contrast_in_box,
    solidity,
)

if HAS_CV2:
    import cv2  # type: ignore


@dataclass
class Instance:
    """One evaluation unit. `background`/`swap_*` are None for real datasets until the
    counterfactual factory (interventions.py / diffusion pipeline) fills them."""

    id: str
    image: np.ndarray                      # float32 [0,1], HxW (gray) or HxWx3
    gt_mask: np.ndarray                    # bool HxW
    box: Box                               # tight GT box
    background: Optional[np.ndarray] = None   # exact object-out counterfactual
    swap_image: Optional[np.ndarray] = None   # object-swap counterfactual
    swap_mask: Optional[np.ndarray] = None    # s_new: inserted object's mask
    meta: Dict = field(default_factory=dict)


# --------------------------------------------------------------- synthetic

def _smooth_noise(shape, rng: np.random.Generator, sigma: float) -> np.ndarray:
    n = rng.standard_normal(shape).astype(np.float32)
    if HAS_CV2:
        k = int(6 * sigma) | 1
        n = cv2.GaussianBlur(n, (k, k), sigma)
    else:  # crude separable box blur fallback
        r = max(1, int(sigma))
        kernel = np.ones(2 * r + 1, dtype=np.float32) / (2 * r + 1)
        n = np.apply_along_axis(lambda v: np.convolve(v, kernel, mode="same"), 0, n)
        n = np.apply_along_axis(lambda v: np.convolve(v, kernel, mode="same"), 1, n)
    n = (n - n.mean()) / (n.std() + 1e-8)
    return n


def _random_blob_mask(
    size: int,
    center,
    radius: float,
    spikiness: float,
    rng: np.random.Generator,
    n_points: int = 28,
) -> np.ndarray:
    """Star-convex blob; `spikiness` controls solidity (0.05 ~ smooth/convex,
    0.45 ~ spiky/low-solidity)."""
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    bumps = rng.uniform(-1.0, 1.0, n_points)
    # circular moving-average to keep the contour tame
    bumps = (bumps + np.roll(bumps, 1) + np.roll(bumps, -1)) / 3.0
    radii = radius * (1.0 + spikiness * bumps)
    xs = center[0] + radii * np.cos(angles)
    ys = center[1] + radii * np.sin(angles)
    mask = np.zeros((size, size), dtype=np.uint8)
    pts = np.stack([xs, ys], axis=1).astype(np.int32)
    if HAS_CV2:
        cv2.fillPoly(mask, [pts], 1)
    else:  # even-odd polygon fill fallback
        from matplotlib.path import Path  # last resort; not in requirements

        yy, xx = np.mgrid[0:size, 0:size]
        mask = (
            Path(pts).contains_points(np.stack([xx.ravel(), yy.ravel()], 1))
            .reshape(size, size)
            .astype(np.uint8)
        )
    return mask.astype(bool)


def make_synthetic_instance(
    seed: int,
    image_size: int = 192,
    contrast: float = 0.35,
    spikiness: float = 0.05,
    noise_sigma: float = 0.02,
    labels: Optional[Dict] = None,
) -> Instance:
    rng = np.random.default_rng(seed)
    s = image_size
    bg_level = 0.45
    texture = 0.06 * _smooth_noise((s, s), rng, sigma=10.0)
    pixel_noise = noise_sigma * rng.standard_normal((s, s)).astype(np.float32)
    background = np.clip(bg_level + texture + pixel_noise, 0, 1).astype(np.float32)

    center = rng.uniform(0.35 * s, 0.65 * s, size=2)
    radius = rng.uniform(0.12 * s, 0.22 * s)
    gt = _random_blob_mask(s, center, radius, spikiness, rng)

    sign = 1.0 if rng.uniform() < 0.5 else -1.0
    image = background.copy()
    image[gt] = np.clip(image[gt] + sign * contrast, 0, 1)

    box = mask_to_tight_box(gt)

    # donor object: different shape family (other spikiness), same box footprint
    donor_rng = np.random.default_rng(seed + 777)
    donor_spike = 0.45 if spikiness < 0.2 else 0.05
    x0, y0, x1, y1 = box
    donor_center = ((x0 + x1) / 2.0, (y0 + y1) / 2.0)
    donor_radius = 0.42 * min(x1 - x0, y1 - y0)
    swap_mask = _random_blob_mask(s, donor_center, donor_radius, donor_spike, donor_rng)
    swap_mask &= np.array(  # keep the donor inside the box
        _box_region_mask(box, (s, s))
    )
    donor_sign = 1.0 if donor_rng.uniform() < 0.5 else -1.0
    swap_image = background.copy()
    swap_image[swap_mask] = np.clip(swap_image[swap_mask] + donor_sign * contrast, 0, 1)

    meta = dict(labels or {})
    meta.update(
        solidity=solidity(gt),
        contrast_measured=rms_contrast_in_box(image, gt, box),
        size_frac=float(np.sqrt(gt.sum()) / s),
        seed=seed,
        domain="synthetic",
    )
    return Instance(
        id=f"syn-{seed}",
        image=image,
        gt_mask=gt,
        box=box,
        background=background,
        swap_image=swap_image,
        swap_mask=swap_mask,
        meta=meta,
    )


def _box_region_mask(box: Box, shape) -> np.ndarray:
    m = np.zeros(shape, dtype=bool)
    x0, y0, x1, y1 = box
    m[y0:y1, x0:x1] = True
    return m


def build_synthetic_eval_set(cfg: Dict) -> List[Instance]:
    """2x2 strata (contrast x solidity), n_eval instances round-robin across strata."""
    ds = cfg["dataset"]
    n = int(ds["n_eval"])
    offset = int(ds.get("eval_seed_offset", 0))
    contrasts = ds["contrast_levels"]     # {"low": c, "high": c}
    spikes = ds["solidity_levels"]        # {"high": spike, "low": spike}
    strata = [
        (ck, sk) for ck in sorted(contrasts) for sk in sorted(spikes)
    ]
    out: List[Instance] = []
    for i in range(n):
        ck, sk = strata[i % len(strata)]
        inst = make_synthetic_instance(
            seed=offset + i,
            image_size=int(ds["image_size"]),
            contrast=float(contrasts[ck]),
            spikiness=float(spikes[sk]),
            noise_sigma=float(ds.get("noise_sigma", 0.02)),
            labels={"contrast_level": ck, "solidity_level": sk},
        )
        out.append(inst)
    return out


def build_synthetic_train_pairs(cfg: Dict):
    """(box-geometry, in-box GT mask) pairs for the learned box->mask null.
    DISJOINT seed range from eval (pre-registered in configs)."""
    tn = cfg["train_null"]
    ds = cfg["dataset"]
    n = int(tn["n_train"])
    offset = int(tn["train_seed_offset"])
    contrasts = ds["contrast_levels"]
    spikes = ds["solidity_levels"]
    strata = [(ck, sk) for ck in sorted(contrasts) for sk in sorted(spikes)]
    pairs = []
    for i in range(n):
        ck, sk = strata[i % len(strata)]
        inst = make_synthetic_instance(
            seed=offset + i,
            image_size=int(ds["image_size"]),
            contrast=float(contrasts[ck]),
            spikiness=float(spikes[sk]),
            noise_sigma=float(ds.get("noise_sigma", 0.02)),
        )
        pairs.append((inst.box, inst.gt_mask, inst.image.shape[:2]))
    return pairs


# ----------------------------------------------------------- real datasets

def load_coco_instances(cfg: Dict) -> List[Instance]:
    """E1 natural arm. Stratified sample over solidity x size x in-box contrast quartiles
    (proposal §14). Requires pycocotools + images on disk; counterfactuals are attached
    later by the diffusion pipeline."""
    ds = cfg["dataset"]["coco"]
    if not ds.get("root") or not ds.get("ann_file"):
        raise FileNotFoundError(
            "COCO not configured: set dataset.coco.root and dataset.coco.ann_file in the "
            "config (Phase 1, roadmap.md). The prototype's scientific-logic tests use "
            "dataset.kind=synthetic."
        )
    try:
        from pycocotools.coco import COCO  # type: ignore
        from pycocotools import mask as mask_utils  # noqa: F401
    except ImportError as e:
        raise ImportError(
            "pycocotools is required for the COCO arm: pip install pycocotools"
        ) from e
    raise NotImplementedError(
        "COCO instance sampling is wired in Phase 1 after the instance list is frozen "
        "(pre-registration requires committing the list before any real-SAM forward)."
    )


def load_medical_instances(cfg: Dict) -> List[Instance]:
    """PRIMARY endpoint arm (MedSAM-protocol datasets; Ma et al. arXiv:2304.12306).
    Cohort rule: in-box RMS contrast in the lowest two deciles of the source dataset
    (pre-registered, configs/default.yaml)."""
    raise NotImplementedError(
        "Medical cohort loader lands in Phase 1 once the dataset list is frozen and "
        "committed (roadmap.md). Deliberately not stubbed with placeholder data: "
        "no fake instances, no fake results."
    )


def build_eval_instances(cfg: Dict) -> List[Instance]:
    kind = cfg["dataset"]["kind"]
    if kind == "synthetic":
        return build_synthetic_eval_set(cfg)
    if kind == "coco":
        return load_coco_instances(cfg)
    if kind == "medical":
        return load_medical_instances(cfg)
    raise ValueError(f"unknown dataset.kind: {kind}")
