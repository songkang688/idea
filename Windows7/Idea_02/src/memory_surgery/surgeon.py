"""The six surgical arms.

Arms exist to separate explanations, not to improve tracking:

  no_op         natural recovery baseline
  targeted      delete entries written in [t_f, t_r); keep conditioning + pre-error
  reset         keep the conditioning frame only -- the trivial "restart" baseline
  sham          THE VACUOUS CONTROL: delete a count-matched number of *pre-error*
                (uncorrupted) entries and leave every post-error entry in place
  slot_control  targeted, then refill the vacated recency slots with count-matched
                duplicates of pre-error entries
  random_k      delete k entries at random, count-matched to targeted

`targeted` beating `reset` is what makes the operation a decomposition rather than
a restart (hypothesis H2: pre-error memories are load-bearing).

`targeted` beating `sham` is what makes the gain attributable to removing corrupted
CONTENT rather than to the mechanical side effects of deleting anything at all.

A note on the sham's definition, because it differs from a literal reading of the
Stage-6 one-line instruction ("delete post-error entries but re-insert
count-matched pre-error duplicates at the same recency slots"). Implemented
literally, that arm still removes the corrupted entries, so it is not vacuous: it
performs the therapeutic action and would be expected to match `targeted` even
when the instrument is perfectly valid, which makes "targeted must beat sham"
unpassable by construction. The medical analogy settles it -- a sham operation
makes the incision and removes nothing. So `sham` here deletes the same NUMBER of
entries while leaving the corruption in place, and the literal Stage-6 arm is kept
separately as `slot_control`, which answers the different and also worthwhile
question of whether slot occupancy matters once content has been removed.

Both are cheap; the pilot runs all six arms for roughly 10 GPU-h.
"""

from __future__ import annotations

from dataclasses import replace

import numpy as np

from .bank import MemoryBank, MemoryEntry

ARMS = ("no_op", "targeted", "reset", "sham", "slot_control", "random_k")


def no_op(bank: MemoryBank) -> MemoryBank:
    return bank.copy()


def targeted(bank: MemoryBank, t_f: int, t_r: int) -> MemoryBank:
    """Delete post-error entries; keep the conditioning frame and pre-error memory.

    Note what this does to recency: the surviving pre-error entries slide forward
    into slots they never occupied. That side effect is the sham arm's target.
    """
    out = bank.copy()
    out.recent = [e for e in out.recent if not (t_f <= e.written_at < t_r)]
    out.pointers = [e for e in out.pointers if not (t_f <= e.written_at < t_r)]
    return out


def full_reset(bank: MemoryBank) -> MemoryBank:
    out = bank.copy()
    out.recent = []
    out.pointers = []
    return out


def sham(bank: MemoryBank, t_f: int, t_r: int, rng: np.random.Generator) -> MemoryBank:
    """The vacuous control: same incision, nothing therapeutic removed.

    Deletes a count-matched number of PRE-ERROR (uncorrupted) entries and leaves
    every post-error entry in place. Deletion count and the resulting slot churn
    match `targeted`; the corrupted content does not get removed.

    If `targeted` does not beat this, then the apparent benefit of memory surgery
    comes from the mechanical consequences of deleting entries -- crowding relief,
    recency re-indexing -- and not from the causal story the paper tells. That is
    the outcome that kills the instrument, and it costs about 10 GPU-h to find out.
    """
    out = bank.copy()
    n_post = sum(1 for e in out.recent if t_f <= e.written_at < t_r)
    pre_idx = [i for i, e in enumerate(out.recent) if e.written_at < t_f]
    if n_post == 0 or not pre_idx:
        return out
    k = min(n_post, len(pre_idx))
    drop = set(rng.choice(pre_idx, size=k, replace=False).tolist())
    out.recent = [e for i, e in enumerate(out.recent) if i not in drop]
    return out


def slot_control(
    bank: MemoryBank, t_f: int, t_r: int, rng: np.random.Generator
) -> MemoryBank:
    """The Stage-6 arm as literally specified: targeted, then refill the slots.

    Removes the same entries as `targeted`, then refills the vacated recency slots
    with count-matched duplicates of pre-error entries, so slot occupancy is
    restored while content stays uncorrupted.

    This does not test whether surgery works -- it removes the corruption too. It
    tests whether, once corruption is gone, it matters that the surviving entries
    slid into recency slots they never occupied during training. A large
    `slot_control` minus `targeted` gap means the recency encoding is doing real
    work and the reported ceiling is an underestimate.
    """
    out = targeted(bank, t_f, t_r)
    n_removed = sum(1 for e in bank.recent if t_f <= e.written_at < t_r)
    donors = [e for e in out.recent if e.written_at < t_f]
    if n_removed == 0 or not donors:
        return out
    idx = rng.integers(0, len(donors), size=n_removed)
    for k, j in enumerate(idx):
        d = donors[int(j)]
        out.recent.append(replace(d, written_at=t_f + k, tag=f"dup_of_{d.frame_idx}"))
    while len(out.recent) > out.capacity:
        out.recent.pop(0)
    return out


def random_k(bank: MemoryBank, k: int, rng: np.random.Generator) -> MemoryBank:
    """Count-matched random deletion: does it matter WHICH entries are removed?"""
    out = bank.copy()
    if k <= 0 or not out.recent:
        return out
    k = min(k, len(out.recent))
    drop = set(rng.choice(len(out.recent), size=k, replace=False).tolist())
    out.recent = [e for i, e in enumerate(out.recent) if i not in drop]
    return out


def apply_arm(
    arm: str, bank: MemoryBank, *, t_f: int, t_r: int, rng: np.random.Generator
) -> MemoryBank:
    if arm == "no_op":
        return no_op(bank)
    if arm == "targeted":
        return targeted(bank, t_f, t_r)
    if arm == "reset":
        return full_reset(bank)
    if arm == "sham":
        return sham(bank, t_f, t_r, rng)
    if arm == "slot_control":
        return slot_control(bank, t_f, t_r, rng)
    if arm == "random_k":
        k = sum(1 for e in bank.recent if t_f <= e.written_at < t_r)
        return random_k(bank, k, rng)
    raise ValueError(f"unknown arm: {arm!r}; expected one of {ARMS}")
