"""Localization metrics.

`parse_failure_rate` is reported separately from IoU, always. Folding unparseable
outputs into the IoU mean as zeros is what makes a chat model look like it
cannot localise when it merely talks: the two failures need different fixes and
support different conclusions.
"""

from __future__ import annotations

import numpy as np

from .boxes import iou, parse_box


def _parsed(outputs: list[str]) -> list[np.ndarray | None]:
    return [parse_box(o) for o in outputs]


def parse_failure_rate(outputs: list[str]) -> float:
    """Fraction of outputs from which no box could be extracted."""
    if not outputs:
        return float("nan")
    return float(sum(p is None for p in _parsed(outputs)) / len(outputs))


def mean_iou(outputs: list[str], gold: np.ndarray, count_failures: bool = True) -> float:
    """Mean IoU. With `count_failures=False`, scores only parseable outputs.

    Report both. The difference between them IS the format tax, quantified:
    if `count_failures=True` shows a gap and `False` does not, the checkpoint
    localises fine and is being punished for prose.
    """
    parsed = _parsed(outputs)
    values = []
    for p, g in zip(parsed, np.asarray(gold, dtype=np.float64)):
        if p is None:
            if count_failures:
                values.append(0.0)
            continue
        values.append(iou(p, g))
    return float(np.mean(values)) if values else float("nan")


def acc_at_iou(outputs: list[str], gold: np.ndarray, threshold: float = 0.5) -> float:
    """Fraction of examples localised at or above `threshold`. Failures count as misses."""
    parsed = _parsed(outputs)
    hits = 0
    for p, g in zip(parsed, np.asarray(gold, dtype=np.float64)):
        if p is not None and iou(p, g) >= threshold:
            hits += 1
    return float(hits / len(parsed)) if parsed else float("nan")


def rank_accuracy(correct: list[bool]) -> float:
    """Top-1 accuracy of the gold box against shared distractors."""
    if not correct:
        return float("nan")
    return float(np.mean(np.asarray(correct, dtype=np.float64)))
