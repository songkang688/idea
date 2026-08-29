"""Interleaved rehearsal sampling and token-budget accounting.

Reviewer attack A1 is settled here, not in prose. LLaVA-1.5's published mix already
contains a text-only ShareGPT slice, so an honest A0 requires stripping it -- which
removes tokens from the base mix. Unless every arm is re-matched to the same total
token budget afterwards, arm differences are partly a training-length difference and
the whole grid is confounded.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Sequence

import numpy as np


@dataclass(frozen=True)
class TokenBudget:
    """Token accounting for one arm.

    `multimodal_tokens` is measured on the TEXT-STRIPPED mix. `rehearsal_fraction`
    is a share of the total, so the multimodal stream shrinks slightly as rehearsal
    grows -- which is the point: the comparison is at fixed total compute, not fixed
    multimodal compute.
    """

    total_tokens: int
    rehearsal_fraction: float

    @property
    def rehearsal_tokens(self) -> int:
        return int(round(self.total_tokens * self.rehearsal_fraction))

    @property
    def multimodal_tokens(self) -> int:
        return self.total_tokens - self.rehearsal_tokens

    def matches(self, other: "TokenBudget", tol: float = 1e-3) -> bool:
        return abs(self.total_tokens - other.total_tokens) <= tol * self.total_tokens


def build_matched_budgets(
    stripped_mix_tokens: int,
    rehearsal_fraction: float,
    arms: Sequence[str],
) -> dict[str, TokenBudget]:
    """One budget per arm, all with identical totals.

    A0 has no rehearsal stream, so to hit the same total it must draw more
    multimodal tokens. Not doing this is the single easiest way to make A0 look
    worse than it is, since it would also be the shortest run.
    """
    total = int(round(stripped_mix_tokens / (1.0 - rehearsal_fraction)))
    out: dict[str, TokenBudget] = {}
    for arm in arms:
        frac = 0.0 if arm == "A0_none" else rehearsal_fraction
        out[arm] = TokenBudget(total_tokens=total, rehearsal_fraction=frac)
    return out


class InterleavedSampler:
    """Emit one text batch per `interleave` multimodal batches.

    Batch-level interleaving (rather than mixing modalities inside a batch) is what
    makes gradient matching well-defined: a text batch produces a language-tower
    gradient that can be measured and scaled on its own.
    """

    def __init__(
        self,
        n_multimodal_batches: int,
        interleave: int = 9,
        seed: int = 0,
    ) -> None:
        if interleave < 1:
            raise ValueError("interleave must be >= 1")
        self.n_multimodal_batches = n_multimodal_batches
        self.interleave = interleave
        self.rng = np.random.default_rng(seed)

    def __iter__(self) -> Iterator[str]:
        seen = 0
        for _ in range(self.n_multimodal_batches):
            yield "multimodal"
            seen += 1
            if seen % self.interleave == 0:
                yield "text"

    @property
    def n_text_batches(self) -> int:
        return self.n_multimodal_batches // self.interleave

    def realised_fraction(self) -> float:
        """The rehearsal share this schedule actually produces, in batches.

        Checked against the intended fraction rather than assumed equal: 1-in-9
        interleaving gives 1/10 of batches, which is only 10% of *tokens* if the two
        batch types carry the same token count. They usually do not.
        """
        total = self.n_multimodal_batches + self.n_text_batches
        return self.n_text_batches / total if total else 0.0
