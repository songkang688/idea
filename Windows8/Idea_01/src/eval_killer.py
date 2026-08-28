"""Evaluate a trained toy head. Same disclaimer: not SAM, not real data."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/killer_e0.yaml")
    args = p.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    report = Path(cfg["out_dir"]) / "toy_report.txt"
    print(report.read_text() if report.exists() else "Run train_density_head.py first.")


if __name__ == "__main__":
    main()
