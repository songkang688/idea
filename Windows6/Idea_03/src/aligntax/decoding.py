"""The three eval modes, which exist to separate format from localisation.

From `experiments.md`: "(1) free-form (2) grammar-constrained (3) likelihood
rank of GT vs <=16 shared distractor boxes."

The three are ordered by how much of the format confound they remove:

    freeform        includes the confound — a chatty model can lose points for
                    prose it was aligned to produce
    constrained     removes the wrapper, keeps the decoding path
    likelihood_rank removes generation entirely — the model only scores
                    candidates, so it cannot be penalised for how it talks

A gap that survives all three is not a formatting artifact. A gap that dies at
mode 3 is outcome **O1**, and `experiments.md` says to write the negative.
"""

from __future__ import annotations

import numpy as np

from .boxes import format_xyxy, iou


def chatty_generate(
    box: np.ndarray, chatty_rate: float, noise: float, rng: np.random.Generator, scale: float
) -> str:
    """Free-form decode. May wrap the answer in prose or truncate it."""
    predicted = box + noise * scale * rng.normal(size=4)
    roll = rng.random()
    if roll < chatty_rate * 0.4:
        # Prose with only two numbers: a genuine format failure, unparseable.
        return f"The object appears near the upper-left region, around ({predicted[0]:.0f},{predicted[1]:.0f})."
    if roll < chatty_rate:
        return f"Sure! Here it is: [{format_xyxy(predicted)}]"
    return format_xyxy(predicted)


def constrained_generate(
    box: np.ndarray, noise: float, rng: np.random.Generator, scale: float
) -> str:
    """Grammar-constrained decode: always four bare numbers, never prose.

    This is what removes the wrapper confound. Note it does NOT remove a
    decoding-policy shift — the model can still emit worse coordinates.
    """
    return format_xyxy(box + noise * scale * rng.normal(size=4))


def likelihood_rank(
    gold: np.ndarray,
    distractors: np.ndarray,
    noise: float,
    rng: np.random.Generator,
    scale: float,
) -> bool:
    """Score GT against shared distractors; True when GT ranks first.

    Generation-free, so it is immune to how the model phrases things. A
    surviving gap here cannot be a formatting artifact.

    The scorer is simulated as an internal box estimate whose quality degrades
    with `noise`; candidates are ranked by IoU against that estimate.
    """
    estimate = gold + noise * scale * rng.normal(size=4)
    candidates = np.concatenate([gold[None, :], np.asarray(distractors)], axis=0)
    scores = np.array([iou(estimate, c) for c in candidates])
    return bool(scores.argmax() == 0)
