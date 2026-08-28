"""Single-instance demo: run one instance through every condition and save a visual
contact sheet (intact / object-out / swap, with predicted mask outlines).

Usage:
    python -m src.inference --config configs/default.yaml [--seed 3] [--out artifacts/demo]
"""

from __future__ import annotations

import argparse
import os

import numpy as np

from .config import load_config
from .dataset import make_synthetic_instance
from .interventions import boxfill_null, convexity_matched_mask
from .model_sam import build_eval_models
from .utils import HAS_CV2, dice, ensure_dir, fill_fraction_in_box, pad_box, to_uint8_gray

if HAS_CV2:
    import cv2  # type: ignore


def _panel(image: np.ndarray, mask: np.ndarray, label: str) -> np.ndarray:
    img = to_uint8_gray(image)
    rgb = np.stack([img, img, img], axis=-1)
    if mask is not None and mask.any() and HAS_CV2:
        cont, _ = cv2.findContours(
            mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        cv2.drawContours(rgb, cont, -1, (0, 0, 255), 1)
        cv2.putText(rgb, label, (4, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
    return rgb


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--out", default="artifacts/demo")
    ap.add_argument("--override", nargs="*", default=[])
    args = ap.parse_args(argv)
    cfg = load_config(args.config, args.override)

    ds = cfg["dataset"]
    inst = make_synthetic_instance(
        seed=args.seed,
        image_size=int(ds["image_size"]),
        contrast=float(ds["contrast_levels"]["high"]),
        spikiness=float(ds["solidity_levels"]["low"]),
        noise_sigma=float(ds.get("noise_sigma", 0.02)),
        labels={"contrast_level": "high", "solidity_level": "low"},
    )
    b0 = pad_box(inst.box, int(cfg["conditions"]["primary_padding_px"]), inst.image.shape)

    out_dir = ensure_dir(args.out)
    for model in build_eval_models(cfg):
        m_intact = model.predict(inst.image, b0)
        m_out = model.predict(inst.background, b0)
        m_swap = model.predict(inst.swap_image, b0)
        nulls = {
            "boxfill": boxfill_null(b0, inst.image.shape[:2]),
            "convexity": convexity_matched_mask(
                b0, inst.image.shape[:2], fill_fraction_in_box(inst.gt_mask, b0)
            ),
        }
        print(
            f"[demo] {model.name}: Dice intact={dice(m_intact, inst.gt_mask):.3f} "
            f"out-persistence={dice(m_out, m_intact):.3f} "
            f"swap-tracking={dice(m_swap, inst.swap_mask):.3f} "
            f"nulls={{{', '.join(f'{k}:{dice(v, inst.gt_mask):.3f}' for k, v in nulls.items())}}}"
        )
        if HAS_CV2:
            sheet = np.concatenate(
                [
                    _panel(inst.image, m_intact, f"{model.name} intact"),
                    _panel(inst.background, m_out, "object-out"),
                    _panel(inst.swap_image, m_swap, "object-swap"),
                    _panel(inst.image, nulls["convexity"], "convexity-null"),
                ],
                axis=1,
            )
            path = os.path.join(out_dir, f"demo_{model.name}_seed{args.seed}.png")
            cv2.imwrite(path, sheet)
            print(f"[demo] wrote {path}")


if __name__ == "__main__":
    main()
