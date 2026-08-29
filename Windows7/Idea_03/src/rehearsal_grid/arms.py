"""The five rehearsal arms, as content-destruction transforms over a token stream.

Documents are lists of integer token ids -- what the tokenizer hands the trainer.
Operating at the token level rather than on strings is deliberate: A3 has to
preserve the *unigram distribution and the length* exactly, and a string-level
word shuffle followed by re-tokenization would not.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np

Doc = list[int]


@dataclass(frozen=True)
class Arm:
    name: str
    destroys: str
    preserves: str


ARMS: tuple[Arm, ...] = (
    Arm("A0_none", "everything (no rehearsal at all)", "nothing -- forgetting floor"),
    Arm("A1_curated", "nothing", "content, syntax, diversity"),
    Arm("A2_random_web", "curation", "content, syntax, diversity"),
    Arm("A3_shuffled", "syntax and content", "unigram statistics and length"),
    Arm("A4_single_doc", "diversity", "content and syntax of one document"),
)

ARM_NAMES = tuple(a.name for a in ARMS)


def _identity(docs: Sequence[Doc], rng: np.random.Generator) -> list[Doc]:
    return [list(d) for d in docs]


def _shuffle_within_docs(docs: Sequence[Doc], rng: np.random.Generator) -> list[Doc]:
    """A3: permute tokens inside each document.

    Within-document rather than corpus-wide, so per-document length and per-document
    unigram statistics are both preserved exactly. A corpus-wide shuffle would leak
    an extra confound (document composition changes too) into an arm whose whole job
    is to change exactly one thing.
    """
    out = []
    for d in docs:
        arr = np.array(d, dtype=np.int64)
        rng.shuffle(arr)
        out.append(arr.tolist())
    return out


def _repeat_single(docs: Sequence[Doc], rng: np.random.Generator) -> list[Doc]:
    """A4: one document, repeated for the whole rehearsal budget."""
    if not docs:
        return []
    chosen = list(docs[int(rng.integers(len(docs)))])
    return [list(chosen) for _ in docs]


_TRANSFORMS: dict[str, Callable[[Sequence[Doc], np.random.Generator], list[Doc]]] = {
    "A0_none": lambda docs, rng: [],
    "A1_curated": _identity,
    "A2_random_web": _identity,
    "A3_shuffled": _shuffle_within_docs,
    "A4_single_doc": _repeat_single,
}


def destroy(arm: str, docs: Sequence[Doc], rng: np.random.Generator) -> list[Doc]:
    """Apply arm `arm` to a rehearsal corpus.

    A1 and A2 are both identity transforms -- they differ in the *source corpus*
    (curated instruction text vs raw C4), not in any operation applied here. Keeping
    that distinction in the caller rather than in the transform is what stops the
    two arms from silently becoming the same run.
    """
    if arm not in _TRANSFORMS:
        raise KeyError(f"unknown arm {arm!r}; expected one of {ARM_NAMES}")
    return _TRANSFORMS[arm](docs, rng)


def unigram_preserved(before: Sequence[Doc], after: Sequence[Doc]) -> bool:
    """A3's defining property, checked rather than assumed."""
    return Counter(t for d in before for t in d) == Counter(t for d in after for t in d)


def bigram_destroyed(before: Sequence[Doc], after: Sequence[Doc], tol: float = 0.05) -> bool:
    """A3 must actually break local structure, not just claim to.

    A short document over a small vocabulary can survive a permutation nearly intact,
    which would make A3 a much weaker control than the design assumes. This is the
    check E0b exists to run for real; here it guards the synthetic demo.
    """

    def bigrams(docs: Sequence[Doc]) -> Counter:
        return Counter(
            (d[i], d[i + 1]) for d in docs for i in range(len(d) - 1)
        )

    b0, b1 = bigrams(before), bigrams(after)
    total = sum(b0.values())
    if total == 0:
        return True
    overlap = sum((b0 & b1).values()) / total
    return overlap < tol + 1.0 / max(len(set(t for d in before for t in d)), 1)
