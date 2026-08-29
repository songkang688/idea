"""The comparison that H1 and H2 are decided on.

`agreement_profile` answers H1 (does AMG look more like intensity clustering
than like a spatial/texture baseline?). `counterfactual_profile` answers H2
(does AMG move under intensity change but not under texture change?).

Neither function returns a verdict. Verdicts are pre-registered thresholds in
`Idea_01/experiments.md`, applied by the caller, so that no threshold can be
quietly tuned inside the analysis code.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .config import Config
from .interventions import (
    check_remap_is_monotone,
    check_shuffle_preserves_tile_means,
    intensity_remap,
    texture_shuffle,
)
from .metrics import (
    adjusted_rand_index,
    boundary_f,
    cardinality_ratio,
    coverage_iou,
    hungarian_iou,
    masks_to_label_map,
)
from .segmenters import amg_mock, gmm_1d, kmeans_1d, multi_otsu, slic_lite


@dataclass
class AgreementProfile:
    """Agreement of one AMG mask set against each baseline.

    Carries the three pre-registered metrics plus the two diagnostics that stop
    a cardinality mismatch from masquerading as (dis)agreement.
    """

    hungarian_iou: dict[str, float]
    ari: dict[str, float]
    boundary_f: dict[str, float]
    coverage_iou: dict[str, float]
    cardinality_ratio: dict[str, float]

    def as_rows(self) -> list[tuple[str, float, float, float, float, float]]:
        return [
            (
                name,
                self.hungarian_iou[name],
                self.ari[name],
                self.boundary_f[name],
                self.coverage_iou[name],
                self.cardinality_ratio[name],
            )
            for name in self.hungarian_iou
        ]


def _baseline_label_maps(img: np.ndarray, cfg: Config, rng: np.random.Generator) -> dict[str, np.ndarray]:
    k = cfg.k_means[0]
    return {
        f"kmeans_k{k}": kmeans_1d(img, k, rng),
        f"multi_otsu_k{min(k, 5)}": multi_otsu(img, min(k, 5)),
        f"gmm_k{min(k, 5)}": gmm_1d(img, min(k, 5), rng),
        "slic_lite": slic_lite(img, cfg.slic_n_segments, cfg.slic_compactness, rng),
    }


def agreement_profile(img: np.ndarray, cfg: Config, rng: np.random.Generator) -> AgreementProfile:
    """H1: agreement of the AMG mask set with every baseline, all three metrics."""
    masks = amg_mock(img)
    amg_labels = masks_to_label_map(masks, img.shape)
    baselines = _baseline_label_maps(img, cfg, rng)

    iou: dict[str, float] = {}
    ari: dict[str, float] = {}
    bf: dict[str, float] = {}
    cov: dict[str, float] = {}
    card: dict[str, float] = {}
    for name, labels in baselines.items():
        baseline_masks = [labels == v for v in np.unique(labels)]
        iou[name] = hungarian_iou(masks, baseline_masks)
        ari[name] = adjusted_rand_index(amg_labels, labels)
        bf[name] = boundary_f(amg_labels, labels, cfg.boundary_tolerance_px)
        cov[name] = coverage_iou(masks, baseline_masks)
        card[name] = cardinality_ratio(masks, baseline_masks)
    return AgreementProfile(
        hungarian_iou=iou, ari=ari, boundary_f=bf, coverage_iou=cov, cardinality_ratio=card
    )


def counterfactual_profile(img: np.ndarray, cfg: Config, rng: np.random.Generator) -> dict[str, float]:
    """H2: how much does the AMG mask set move under each intervention?

    Returns self-agreement (1.0 = intervention changed nothing). The mechanistic
    claim needs `intensity_remap` **lower** than `texture_shuffle`.
    """
    base_masks = amg_mock(img)

    remapped = intensity_remap(img, cfg.remap_gamma)
    shuffled = texture_shuffle(img, cfg.shuffle_tile, rng)

    if not check_remap_is_monotone(img, remapped):
        raise RuntimeError("intensity arm invalid: remap is not monotone; result is not evidence")
    if not check_shuffle_preserves_tile_means(img, shuffled, cfg.shuffle_tile):
        raise RuntimeError("texture arm invalid: tile means not preserved; result is not evidence")

    return {
        "self_agreement_intensity_remap": hungarian_iou(base_masks, amg_mock(remapped)),
        "self_agreement_texture_shuffle": hungarian_iou(base_masks, amg_mock(shuffled)),
    }
