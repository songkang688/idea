"""Corpus structure. Synthetic only — no smoke dataset ships here.

The corpus is deliberately built with three nested groupings, because the whole
argument of Idea_02 turns on them being different things:

    camera  >  event  >  frame

A *camera* is a fixed tower with a fixed background. An *event* is one fire
episode seen by one camera. Random splits break none of them; event-disjoint
splits break the event grouping but **not** the camera grouping; camera-disjoint
splits break both. H2 says the middle case still leaks.

Empty (no-smoke) frames are carried separately because they are the instrument
for H4: they contain no plume, so a seen-vs-unseen camera gap on negatives
cannot be a plume-appearance effect.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class SyntheticCorpus:
    """Frame-level features with camera/event provenance.

    `features` are NOT images and NOT detector embeddings. They are vectors with
    a camera signature planted by construction, used to exercise the split and
    probe machinery.
    """

    features: np.ndarray  # (n, d)
    labels: np.ndarray  # (n,) 1 = smoke present
    camera: np.ndarray  # (n,) camera id
    event: np.ndarray  # (n,) event id, unique per (camera, episode)
    is_empty: np.ndarray  # (n,) True for no-smoke frames from the empty pool

    def __len__(self) -> int:
        return len(self.labels)

    @property
    def n_cameras(self) -> int:
        return int(len(np.unique(self.camera)))

    @property
    def n_events(self) -> int:
        return int(len(np.unique(self.event)))


def make_corpus(cfg, rng: np.random.Generator) -> SyntheticCorpus:
    """Build a corpus with a planted camera signature.

    `cfg.camera_signature` scales how much of each feature vector is determined
    by the camera prototype. At 0.0 there is no camera information at all and
    every leakage measurement downstream must come out null — which is what
    `test_zero_signature_removes_the_gap` checks. Any "leakage" found at higher
    settings was put there on purpose and is not evidence about real data.
    """
    features: list[np.ndarray] = []
    labels: list[int] = []
    cameras: list[int] = []
    events: list[int] = []
    empties: list[bool] = []

    d = cfg.feature_dim
    event_id = 0
    for cam in range(cfg.n_cameras):
        background = rng.normal(size=d) * cfg.camera_signature
        for _ in range(cfg.events_per_camera):
            plume = rng.normal(size=d)
            for _ in range(cfg.frames_per_event):
                positive = rng.random() < 0.5
                vec = background + 0.3 * rng.normal(size=d)
                if positive:
                    vec = vec + 0.9 * plume
                features.append(vec)
                labels.append(int(positive))
                cameras.append(cam)
                events.append(event_id)
                empties.append(False)
            event_id += 1

        for _ in range(cfg.empty_frames_per_camera):
            features.append(background + 0.3 * rng.normal(size=d))
            labels.append(0)
            cameras.append(cam)
            events.append(-1)
            empties.append(True)

    return SyntheticCorpus(
        features=np.stack(features),
        labels=np.array(labels),
        camera=np.array(cameras),
        event=np.array(events),
        is_empty=np.array(empties),
    )


def load_real_corpus(*_args, **_kwargs) -> SyntheticCorpus:
    """Real smoke corpus loader. Not implemented here on purpose."""
    raise NotImplementedError(
        "No smoke/fire dataset ships with this repository, and GATE-A "
        "(stage6_battle.md 5) is still OPEN: it has never been verified that "
        "camera metadata exists on any public set. Idea_02's own first stop rule "
        "is 'Kill if no camera metadata'. Card E-A in Idea_02/experiments.md is "
        "the inventory that must run before this loader is worth writing. "
        "Windows6 has produced NO smoke mAP."
    )
