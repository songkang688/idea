"""Synthetic anti-calibration demo. Does not use SAM. Illustrates the intended analysis."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import yaml


def ece(conf: np.ndarray, acc: np.ndarray, bins: int = 10) -> float:
    edges = np.linspace(0, 1, bins + 1)
    tot = 0.0
    for i in range(bins):
        m = (conf >= edges[i]) & (conf < edges[i + 1])
        if m.any():
            tot += m.mean() * abs(conf[m].mean() - acc[m].mean())
    return float(tot)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/killer_e0.yaml")
    args = p.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    rng = np.random.default_rng(cfg["seed"])
    # OBJECT: tokens track IoU
    true_o = rng.uniform(0.4, 0.95, cfg["n_obj"])
    tok_o = np.clip(true_o + rng.normal(0, 0.05, cfg["n_obj"]), 0, 1)
    # AMORPHOUS: anti-correlated (HYPOTHESIS illustration)
    true_a = rng.uniform(0.1, 0.7, cfg["n_amorph"])
    tok_a = np.clip(0.9 - true_a + rng.normal(0, 0.05, cfg["n_amorph"]), 0, 1)
    rho_o = float(np.corrcoef(tok_o, true_o)[0, 1])
    rho_a = float(np.corrcoef(tok_a, true_a)[0, 1])
    out = Path(cfg["out_dir"])
    out.mkdir(parents=True, exist_ok=True)
    txt = (
        "SYNTHETIC illustration of H1/H2. NOT measured on SAM.\n"
        f"rho_object={rho_o:.3f} rho_amorphous={rho_a:.3f}\n"
        f"ece_object={ece(tok_o, true_o):.3f} ece_amorphous={ece(tok_a, true_a):.3f}\n"
        f"reject_tau={cfg['tau']} amorphous_reject_rate={(tok_a<cfg['tau']).mean():.3f}\n"
    )
    (out / "toy_report.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
