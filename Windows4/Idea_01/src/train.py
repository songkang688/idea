"""Train the learned box->mask null (Stage-4 R2 missing-baseline 2).

The regressor sees ONLY normalized box geometry — never pixels — and predicts the in-box
GT mask on a GxG grid. Its Dice against GT estimates how much of the protocol's score is
supported by label statistics + box geometry alone. Trained on a seed range DISJOINT from
evaluation (pre-registered in configs/default.yaml).

Usage:
    python -m src.train --config configs/default.yaml
"""

from __future__ import annotations

import argparse

import numpy as np

from .config import load_config
from .dataset import build_synthetic_train_pairs
from .model_sam import LearnedBoxToMaskNull, build_null_net
from .utils import ensure_dir, set_seed

try:
    import torch
except Exception as e:  # pragma: no cover
    raise SystemExit(
        "src.train requires torch (pip install torch). The rest of the harness runs "
        "without it; eval simply skips the learned-null arm."
    ) from e

if True:  # keep cv2 import optional-consistent with the rest of the package
    from .utils import HAS_CV2

    if HAS_CV2:
        import cv2  # type: ignore


def _target_grid(gt_mask: np.ndarray, box, grid: int) -> np.ndarray:
    x0, y0, x1, y1 = box
    crop = gt_mask[y0:y1, x0:x1].astype(np.float32)
    if HAS_CV2:
        t = cv2.resize(crop, (grid, grid), interpolation=cv2.INTER_AREA)
    else:
        yi = (np.arange(grid) * crop.shape[0] // grid).clip(0, crop.shape[0] - 1)
        xi = (np.arange(grid) * crop.shape[1] // grid).clip(0, crop.shape[1] - 1)
        t = crop[np.ix_(yi, xi)]
    return (t > 0.5).astype(np.float32)


def main(argv=None) -> str:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--override", nargs="*", default=[])
    args = ap.parse_args(argv)
    cfg = load_config(args.config, args.override)

    tn = cfg["train_null"]
    set_seed(int(cfg["experiment"]["seed"]))

    if cfg["dataset"]["kind"] != "synthetic":
        raise SystemExit(
            "Prototype trains the null on synthetic pairs only; the COCO/medical training "
            "splits are wired in Phase 1 with frozen instance lists (roadmap.md)."
        )
    pairs = build_synthetic_train_pairs(cfg)

    grid = int(tn["grid"])
    feats = np.stack(
        [LearnedBoxToMaskNull.featurize(box, shape) for box, _, shape in pairs]
    )
    targets = np.stack([_target_grid(gt, box, grid) for box, gt, _ in pairs]).reshape(
        len(pairs), -1
    )

    from .losses import dice_bce_loss

    net = build_null_net(grid, list(tn["hidden"]))
    n_params = sum(p.numel() for p in net.parameters())
    opt = torch.optim.Adam(net.parameters(), lr=float(tn["lr"]))
    X = torch.from_numpy(feats.astype(np.float32))
    Y = torch.from_numpy(targets.astype(np.float32))

    n = len(X)
    n_val = max(8, n // 10)
    Xtr, Ytr, Xva, Yva = X[:-n_val], Y[:-n_val], X[-n_val:], Y[-n_val:]
    bs = int(tn["batch_size"])

    print(f"[train] learned box->mask null: {n_params} params, {len(Xtr)} train / {n_val} val pairs")
    for epoch in range(int(tn["epochs"])):
        net.train()
        perm = torch.randperm(len(Xtr))
        tot = 0.0
        for i in range(0, len(Xtr), bs):
            idx = perm[i : i + bs]
            opt.zero_grad()
            loss = dice_bce_loss(net(Xtr[idx]), Ytr[idx])
            loss.backward()
            opt.step()
            tot += float(loss.detach()) * len(idx)
        net.eval()
        with torch.no_grad():
            val = float(dice_bce_loss(net(Xva), Yva))
        if epoch % 5 == 0 or epoch == int(tn["epochs"]) - 1:
            print(f"[train] epoch {epoch:03d}  train_loss={tot/len(Xtr):.4f}  val_loss={val:.4f}")

    out_path = tn["ckpt_out"]
    ensure_dir(out_path.rsplit("/", 1)[0] if "/" in out_path else ".")
    torch.save(
        {"state_dict": net.state_dict(), "grid": grid, "hidden": list(tn["hidden"]),
         "n_params": n_params, "train_kind": cfg["dataset"]["kind"]},
        out_path,
    )
    print(f"[train] saved {out_path}  (train/val gap reported above per proposal §26)")
    return out_path


if __name__ == "__main__":
    main()
