"""Minimal training loop sketch. Requires official SAM to be useful."""

from __future__ import annotations

import argparse
from pathlib import Path

import torch
import yaml

from retain_sam.losses import RetainObjective, wise_ft_state_dicts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", type=str, default="configs/killer_kvasir.yaml")
    args = p.parse_args()
    cfg_path = Path(args.config)
    cfg = yaml.safe_load(cfg_path.read_text()) if cfg_path.exists() else {}
    print("RetainSAM prototype. Load SAM weights and datasets before training.")
    print("config:", cfg)
    obj = RetainObjective(
        lambda_ret=float(cfg.get("lambda_ret", 1.0)),
        encoder_l2=float(cfg.get("encoder_l2", 0.0)),
    )
    print("objective", obj)
    # Interpolation demo on random tensors (NOT a model).
    a = {"w": torch.zeros(3)}
    b = {"w": torch.ones(3)}
    blended = wise_ft_state_dicts(a, b, [0.0, 0.5, 1.0])
    print("wise-ft demo means", [float(sd["w"].mean()) for _, sd in blended])


if __name__ == "__main__":
    main()
