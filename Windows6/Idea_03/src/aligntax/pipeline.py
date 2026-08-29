"""The O1/O2/O3 decision function.

From `experiments.md`, verbatim:

    Outcomes: O1 gap dies under likelihood -> format artifact (write negative).
              O2 gap in likelihood, probe OK -> policy tax.
              O3 probe also drops -> representation tax.

`classify_outcome` is a pure function of measurements with no model access, so
it is unit-testable against planted ground truth. The smoke run plants each of
the four modes in turn and checks that this function recovers them.

It **refuses to classify** without a likelihood measurement. That is the code
form of the kill rule "Kill if H1 fails under constrained decoding (formatting
confound)": a free-form gap alone is not evidence of anything, and the easiest
way to publish a wrong result here would be to skip mode 3 and report the gap.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Outcome(str, Enum):
    NO_TAX = "none"
    FORMAT = "format"
    POLICY = "policy"
    REPRESENTATION = "representation"


@dataclass
class TaxMeasurements:
    """base-minus-chat gaps. Positive means the chat checkpoint is worse.

    `likelihood_gap` is required. `freeform_gap` and `constrained_gap` are
    informative but never decisive, because both run through generation.
    """

    freeform_gap: float
    constrained_gap: float | None
    likelihood_gap: float | None
    probe_gap: float  # positive = chat probe error HIGHER, i.e. representation worse


def classify_outcome(m: TaxMeasurements, tolerance: float = 0.02) -> Outcome:
    """Map measured gaps onto O1/O2/O3, or refuse.

    Raises when the likelihood mode was not run. Without it, a free-form gap
    cannot be distinguished from the chat checkpoint being chatty, and any
    verdict would be unfounded.
    """
    if m.likelihood_gap is None:
        raise ValueError(
            "cannot classify without the likelihood-rank mode: a free-form or "
            "constrained gap alone cannot be separated from the format confound. "
            "experiments.md: 'Kill if H1 fails under constrained decoding.' Run "
            "eval mode 3 before asking for a verdict."
        )

    likelihood_tax = m.likelihood_gap > tolerance
    representation_tax = m.probe_gap > tolerance
    generation_tax = m.freeform_gap > tolerance or (
        m.constrained_gap is not None and m.constrained_gap > tolerance
    )

    if not likelihood_tax:
        # O1: the gap dies once generation is removed. Write the negative.
        return Outcome.FORMAT if generation_tax else Outcome.NO_TAX
    if representation_tax:
        return Outcome.REPRESENTATION  # O3
    return Outcome.POLICY  # O2
