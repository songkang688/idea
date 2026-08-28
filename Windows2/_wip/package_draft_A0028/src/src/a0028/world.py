"""Synthetic teleport-probe world.

Generates short abstract "videos" for the A-0028 dissociation probe. A frame is
a set of candidates (id, appearance embedding, 2-D location). Two objects — a
target and a distractor at parametric appearance similarity — move smoothly,
then a controlled manipulation is injected on one frame:

  - ``swap``            target and distractor exchange positions (identity swap /
                        the canonical teleport probe from exp_07)
  - ``jump``            target jumps a controlled displacement; a static
                        background "phantom" candidate occupies the old location
  - ``appearance_flip`` target appearance changes abruptly, locations continue
                        smoothly (appearance discontinuity)
  - ``placebo``         paste-artifact-only control: a small appearance
                        perturbation is applied to BOTH objects, nothing moves.
                        Reviewer-2 control — if a tracker is disrupted here, the
                        probe measures paste artifacts, not arbitration.

Temporal gap g: the world evolves g unobserved steps (motion + appearance
drift) between the last prefix frame and the manipulation frame, so memory is
g steps stale at the decision point. Appearance drift lives in the WORLD (the
objects genuinely change), not in the tracker — any gap effect on arbitration
is emergent, not hard-coded.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np

TARGET = "target"
DISTRACTOR = "distractor"
PHANTOM = "phantom"

CONDITIONS = ("swap", "jump", "appearance_flip", "placebo")


@dataclass
class Candidate:
    ident: str
    app: np.ndarray  # unit-norm appearance embedding
    loc: np.ndarray  # 2-D location in arena coordinates


@dataclass
class Frame:
    time: int  # world time (so the tracker knows elapsed steps across the gap)
    candidates: List[Candidate]


@dataclass
class Trial:
    frames: List[Frame]  # observed frames only (prefix, manipulation, post)
    manipulation_idx: int  # index into ``frames`` of the manipulation frame
    condition: str
    place_ident: Optional[str]  # candidate occupying the pre-manipulation
    # target location at the manipulation frame (None when no spatial
    # dissociation exists: appearance_flip / placebo)
    params: dict = field(default_factory=dict)


@dataclass
class WorldParams:
    arena: float = 256.0
    app_dim: int = 32
    n_prefix: int = 6
    n_post: int = 8
    step_sigma: float = 1.5  # per-step random-walk motion (px)
    drift_rate: float = 0.12  # per-step appearance drift (world property)
    placebo_eps: float = 0.05  # paste-artifact appearance perturbation
    jump_distractor_dist: float = 150.0  # distractor offset in jump condition

    @classmethod
    def from_dict(cls, d: dict) -> "WorldParams":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


def unit_vector(rng: np.random.Generator, dim: int) -> np.ndarray:
    v = rng.normal(size=dim)
    return v / np.linalg.norm(v)


def vector_with_cosine(
    rng: np.random.Generator, base: np.ndarray, cos_target: float
) -> np.ndarray:
    """Unit vector with cosine similarity ``cos_target`` to unit vector ``base``."""
    noise = rng.normal(size=base.shape)
    noise -= noise.dot(base) * base
    noise /= np.linalg.norm(noise)
    v = cos_target * base + np.sqrt(max(0.0, 1.0 - cos_target**2)) * noise
    return v / np.linalg.norm(v)


def drift_appearance(
    rng: np.random.Generator, app: np.ndarray, rate: float, steps: int = 1
) -> np.ndarray:
    """World-side appearance drift: mix toward random directions, renormalize."""
    out = app
    for _ in range(steps):
        out = (1.0 - rate) * out + rate * unit_vector(rng, out.shape[0])
        out = out / np.linalg.norm(out)
    return out


def _rand_dir2(rng: np.random.Generator) -> np.ndarray:
    theta = rng.uniform(0.0, 2.0 * np.pi)
    return np.array([np.cos(theta), np.sin(theta)])


def generate_trial(
    condition: str,
    displacement: float,
    gap: int,
    similarity: float,
    rng: np.random.Generator,
    world: WorldParams | None = None,
) -> Trial:
    """Build one probe trial.

    ``displacement`` — distance of the location discontinuity at the
    manipulation frame (and target–distractor separation in swap).
    ``gap`` — unobserved world steps before the manipulation frame.
    ``similarity`` — cosine similarity of the distractor's initial appearance
    to the target's initial appearance.
    """
    if condition not in CONDITIONS:
        raise ValueError(f"unknown condition {condition!r}; expected one of {CONDITIONS}")
    w = world or WorldParams()

    t_app = unit_vector(rng, w.app_dim)
    d_app = vector_with_cosine(rng, t_app, similarity)
    phantom_app = unit_vector(rng, w.app_dim)  # background content, unrelated

    center, spread = w.arena / 2.0, w.arena / 8.0
    t_loc = center + rng.uniform(-spread, spread, size=2)
    offset_dist = w.jump_distractor_dist if condition == "jump" else displacement
    offset_dir = _rand_dir2(rng)
    d_loc = t_loc + offset_dist * offset_dir

    frames: List[Frame] = []
    time = 0

    def snapshot(extra: Optional[Candidate] = None) -> None:
        cands = [
            Candidate(TARGET, t_app.copy(), t_loc.copy()),
            Candidate(DISTRACTOR, d_app.copy(), d_loc.copy()),
        ]
        if extra is not None:
            cands.append(extra)
        frames.append(Frame(time, cands))

    def evolve(steps: int, rigid: bool) -> None:
        nonlocal t_app, d_app, t_loc, d_loc, time
        for _ in range(steps):
            t_loc = t_loc + rng.normal(scale=w.step_sigma, size=2)
            if rigid:
                # pre-manipulation the distractor keeps its rigid offset (plus
                # jitter) so the swap displacement stays controlled
                d_loc = t_loc + offset_dist * offset_dir + rng.normal(scale=0.5, size=2)
            else:
                d_loc = d_loc + rng.normal(scale=w.step_sigma, size=2)
            t_app = drift_appearance(rng, t_app, w.drift_rate)
            d_app = drift_appearance(rng, d_app, w.drift_rate)
            time += 1

    # --- prefix: smooth, observed ---
    snapshot()
    for _ in range(w.n_prefix - 1):
        evolve(1, rigid=True)
        snapshot()

    # --- unobserved gap: world keeps evolving, memory goes stale ---
    evolve(gap, rigid=True)

    # --- manipulation frame ---
    old_t_loc = t_loc.copy()
    phantom: Optional[Candidate] = None
    place_ident: Optional[str]
    if condition == "swap":
        t_loc, d_loc = d_loc.copy(), t_loc.copy()
        place_ident = DISTRACTOR
    elif condition == "jump":
        t_loc = t_loc + displacement * _rand_dir2(rng)
        phantom = Candidate(PHANTOM, phantom_app.copy(), old_t_loc.copy())
        place_ident = PHANTOM
    elif condition == "appearance_flip":
        evolve(1, rigid=True)
        t_app = unit_vector(rng, w.app_dim)
        place_ident = None
    else:  # placebo: paste-artifact perturbation on both objects, no move
        evolve(1, rigid=True)
        for name in ("t", "d"):
            app = t_app if name == "t" else d_app
            app = (1.0 - w.placebo_eps) * app + w.placebo_eps * unit_vector(rng, w.app_dim)
            app = app / np.linalg.norm(app)
            if name == "t":
                t_app = app
            else:
                d_app = app
        place_ident = None
    if condition in ("swap", "jump"):
        time += 1
    snapshot(extra=phantom)
    manipulation_idx = len(frames) - 1

    # --- post frames: smooth again, objects independent; phantom is static ---
    for _ in range(w.n_post):
        evolve(1, rigid=False)
        still_phantom = (
            Candidate(PHANTOM, phantom_app.copy(), old_t_loc.copy())
            if phantom is not None
            else None
        )
        snapshot(extra=still_phantom)

    return Trial(
        frames=frames,
        manipulation_idx=manipulation_idx,
        condition=condition,
        place_ident=place_ident,
        params={
            "displacement": displacement,
            "gap": gap,
            "similarity": similarity,
        },
    )
