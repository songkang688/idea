"""The audit driver: method-agnostic, floor-aware, stratified.

One pass over the episode list produces every quantity the paper reports. The
driver never sees a class name or a leaderboard position, so it cannot be tuned
toward a desired outcome.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Mapping, Sequence

import numpy as np

from .adapters import FSSAdapter
from .counterfactual import CounterfactualList
from .episodes import Episode, STRATA, stratum_counts
from .floors import Floor
from .metrics import EpisodeMeasurement, iou
from .stats import StratumResult, evaluate_killer, summarise

# Image loaders are injected so the harness can run against mock arrays, a cached
# tensor store, or the real datasets without changing this file.
ImageLoader = Callable[[str], np.ndarray]
MaskLoader = Callable[[str, int], np.ndarray]


@dataclass
class AuditConfig:
    tau: float = 0.2  # pre-registered episode filter
    seed: int = 0
    specialist_methods: set[str] = field(default_factory=set)


@dataclass
class AuditReport:
    config: AuditConfig
    stratum_counts: dict[str, int]
    measurements: list[EpisodeMeasurement]
    results: list[StratumResult]

    def killer_verdict(self, stratum: str = "S3_distractor_present"):
        subset = [r for r in self.results if r.stratum == stratum]
        return evaluate_killer(subset, self.config.specialist_methods)

    def leaderboard(self, benchmark: str, stratum: str, key: str = "acc") -> list[str]:
        rows = [r for r in self.results if r.benchmark == benchmark and r.stratum == stratum]
        if key == "acc":
            rows.sort(key=lambda r: r.acc_correct.point, reverse=True)
        elif key == "sss":
            rows.sort(key=lambda r: (r.sss if np.isfinite(r.sss) else -np.inf), reverse=True)
        else:
            raise ValueError(f"unknown leaderboard key: {key}")
        return [r.method for r in rows]


def run_audit(
    *,
    methods: Sequence[FSSAdapter],
    episodes: Sequence[Episode],
    counterfactuals: Mapping[str, CounterfactualList],
    floor_strong: Floor,
    floor_weak: Floor,
    load_image: ImageLoader,
    load_support_mask: MaskLoader,
    config: AuditConfig | None = None,
) -> AuditReport:
    """Score every method on every episode under correct and wrong supports."""
    config = config or AuditConfig()
    measurements: list[EpisodeMeasurement] = []

    # Floors are support-free, so they are computed once per query and reused for
    # every method. This is where most of the saved compute comes from.
    floor_cache: dict[str, tuple[float, float]] = {}

    for ep in episodes:
        query = load_image(ep.query_image_id)
        if ep.query_image_id not in floor_cache:
            floor_cache[ep.query_image_id] = (
                iou(floor_strong.predict(query), ep.query_gt),
                iou(floor_weak.predict(query), ep.query_gt),
            )
        fa, fb = floor_cache[ep.query_image_id]

        cf = counterfactuals.get(ep.episode_id)
        if cf is None:
            raise KeyError(
                f"no frozen counterfactual list for episode {ep.episode_id}; "
                "lists must be generated and committed before inference"
            )

        support_img = load_image(ep.support_image_id)
        for method in methods:
            pred_corr = method.segment(support_img, ep.support_mask, query)
            a_corr = iou(pred_corr, ep.query_gt)

            a_wrong, insens = [], []
            for ws in cf.wrong_supports:
                w_img = load_image(ws.support_image_id)
                w_mask = load_support_mask(ws.support_image_id, ws.class_id)
                pred_w = method.segment(w_img, w_mask, query)
                a_wrong.append(iou(pred_w, ep.query_gt))
                insens.append(iou(pred_w, pred_corr))

            measurements.append(
                EpisodeMeasurement(
                    episode_id=ep.episode_id,
                    method=method.name,
                    benchmark=ep.benchmark,
                    stratum=ep.stratum(),
                    a_corr=a_corr,
                    a_wrong=a_wrong,
                    insensitivity=insens,
                    a_floor_strong=fa,
                    a_floor_weak=fb,
                    n_area_relaxations=cf.n_relaxations,
                )
            )

    results = []
    for method in methods:
        for benchmark in sorted({e.benchmark for e in episodes}):
            for stratum in STRATA:
                subset = [
                    m
                    for m in measurements
                    if m.method == method.name
                    and m.benchmark == benchmark
                    and m.stratum == stratum
                ]
                if not subset:
                    continue
                results.append(
                    summarise(
                        subset,
                        method=method.name,
                        benchmark=benchmark,
                        stratum=stratum,
                        tau=config.tau,
                        seed=config.seed,
                    )
                )

    return AuditReport(
        config=config,
        stratum_counts=stratum_counts(episodes),
        measurements=measurements,
        results=results,
    )
