"""Synthetic 2D demo — NOT a clinical result."""

from __future__ import annotations

import numpy as np

from lesion_suppress.core import (
    insert_gaussian_lesion,
    kendall_tau,
    simple_denoise,
    suppression_event,
)


def demo(seed: int = 0) -> None:
    rng = np.random.default_rng(seed)
    rates_syn = []
    sizes = [2.0, 3.0, 5.0]
    strengths = [0.5, 1.0, 2.0]
    for sigma in sizes:
        for s in strengths:
            ev = []
            for _ in range(40):
                bg = rng.normal(0, 1, (64, 64)).astype(np.float32)
                cy, cx = 32, 32
                raw = insert_gaussian_lesion(bg, cy, cx, sigma=sigma, cnr=3.0, noise_std=1.0)
                enh = simple_denoise(raw, strength=s)
                ev.append(
                    suppression_event(raw, enh, cy, cx, radius=int(3 * sigma), thresh=2.0)
                )
            rates_syn.append(float(np.mean(ev)))
    # Fake "real" rates: monotone in strength, inverse in size — EXPECTED pattern only.
    fake_real = []
    for sigma in sizes:
        for s in strengths:
            fake_real.append(min(1.0, 0.15 * s / sigma))
    tau = kendall_tau(np.array(rates_syn), np.array(fake_real))
    print("demo suppression rates", rates_syn)
    print("kendall tau vs fake_real (ILLUSTRATIVE, not measured on LIDC)", tau)


if __name__ == "__main__":
    demo()
