"""A memory bank with explicit recency slots.

Recency is modelled explicitly rather than implied by list order, because it is
the thing reviewer attack A2 is about. SAM2's memory attention consumes recent
non-conditioning frames with recency-indexed temporal position encodings. When
post-error entries are deleted, the surviving pre-error entries slide into
recency slots they never occupied during training, so the surgered configuration
is off-distribution *independently of the content* of what was removed.

Making the slot assignment a first-class, inspectable field is what lets the sham
arm hold slots fixed while changing content, which is the only way to separate the
two explanations.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Iterator, Sequence


@dataclass(frozen=True)
class MemoryEntry:
    """One stored frame memory (or object pointer) in the bank."""

    frame_idx: int
    written_at: int
    is_conditioning: bool = False
    is_object_pointer: bool = False
    # Stand-in for the stored feature. In the real system this is a tensor; here a
    # scalar in [0, 1] where higher means "more corrupted by the tracking error".
    corruption: float = 0.0
    tag: str = ""

    @property
    def kind(self) -> str:
        if self.is_conditioning:
            return "conditioning"
        return "pointer" if self.is_object_pointer else "spatial"


@dataclass
class MemoryBank:
    """Conditioning-frame memory plus a bounded FIFO of recent entries.

    The conditioning frame is permanently retained and carries no recency
    encoding, which is exactly why it survives every surgical arm.
    """

    capacity: int = 7
    conditioning: MemoryEntry | None = None
    recent: list[MemoryEntry] = field(default_factory=list)
    pointers: list[MemoryEntry] = field(default_factory=list)

    def write(self, entry: MemoryEntry) -> None:
        if entry.is_conditioning:
            self.conditioning = entry
            return
        target = self.pointers if entry.is_object_pointer else self.recent
        target.append(entry)
        while len(target) > self.capacity:
            target.pop(0)

    def entries(self) -> list[MemoryEntry]:
        out = [self.conditioning] if self.conditioning is not None else []
        return out + list(self.recent) + list(self.pointers)

    def recency_slots(self) -> dict[int, MemoryEntry]:
        """Slot 0 is the most recent non-conditioning entry.

        This is the mapping the temporal position encoding indexes into, and the
        mapping that targeted deletion silently rewrites.
        """
        return {i: e for i, e in enumerate(reversed(self.recent))}

    def slot_of(self, entry: MemoryEntry) -> int | None:
        for slot, e in self.recency_slots().items():
            if e is entry:
                return slot
        return None

    def copy(self) -> "MemoryBank":
        return MemoryBank(
            capacity=self.capacity,
            conditioning=self.conditioning,
            recent=list(self.recent),
            pointers=list(self.pointers),
        )

    def __iter__(self) -> Iterator[MemoryEntry]:
        return iter(self.entries())

    def __len__(self) -> int:
        return len(self.entries())

    def signature(self) -> tuple:
        """Order-sensitive fingerprint, used by the replay-determinism check."""
        return tuple(
            (e.frame_idx, e.written_at, e.kind, round(e.corruption, 6))
            for e in self.entries()
        )

    def mean_corruption(self) -> float:
        non_cond = [e for e in self.entries() if not e.is_conditioning]
        if not non_cond:
            return 0.0
        return sum(e.corruption for e in non_cond) / len(non_cond)


def build_bank(entries: Sequence[MemoryEntry], capacity: int = 7) -> MemoryBank:
    bank = MemoryBank(capacity=capacity)
    for e in entries:
        bank.write(replace(e))
    return bank
