"""Dummy AURC demo — not LIDC."""

from __future__ import annotations

import numpy as np

from disagree_shift.metrics import aurc, sparsification_curve


def demo():
    rng = np.random.default_rng(0)
    err = rng.random((32, 32))
    # Well-ranked uncertainty ≈ error
    good_u = err + 0.05 * rng.random((32, 32))
    bad_u = rng.random((32, 32))
    c_good = sparsification_curve(err, good_u)
    c_bad = sparsification_curve(err, bad_u)
    print("AURC good (lower better, ILLUSTRATIVE)", aurc(c_good))
    print("AURC bad (ILLUSTRATIVE)", aurc(c_bad))


if __name__ == "__main__":
    demo()
