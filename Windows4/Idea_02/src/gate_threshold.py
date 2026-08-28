"""P082 gate: Dice vs binarization threshold. No fake SAM outputs."""
from __future__ import annotations
import argparse, json
import numpy as np

def dice_at_threshold(prob: np.ndarray, gt: np.ndarray, t: float) -> float:
    a = prob >= t
    b = gt.astype(bool)
    inter = np.logical_and(a, b).sum()
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2 * inter / s

def sweep(prob: np.ndarray, gt: np.ndarray) -> dict:
    ts = [i / 20 for i in range(1, 20)]
    return {str(t): dice_at_threshold(prob, gt, t) for t in ts}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="gate.json")
    args = p.parse_args()
    # Synthetic demonstration of the *code path*, not a scientific result.
    rng = np.random.default_rng(0)
    gt = rng.random((64, 64)) > 0.7
    logits = gt.astype(np.float32) * 0.9 + rng.random((64, 64)) * 0.1
    rec = {
        "epistemic": "ACTUAL only for this synthetic demo of sweep(); not a SAM experiment",
        "sweep": sweep(logits, gt),
    }
    open(args.out, "w").write(json.dumps(rec, indent=2))
    print(json.dumps(rec, indent=2))

if __name__ == "__main__":
    main()
