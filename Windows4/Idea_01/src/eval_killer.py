"""Killer experiment: geometry null vs interior interventions.

Does not invent SAM Dice. If SAM is unavailable, writes ellipse/fill stats only.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np
try:
    from PIL import Image
except ImportError:
    Image = None

try:
    from .baselines import ellipse_mask
    from .interventions import mean_fill, telea_inpaint
    from .metrics import dice
    from .sam_wrapper import SamOrSkip
except ImportError:
    from baselines import ellipse_mask
    from interventions import mean_fill, telea_inpaint
    from metrics import dice
    from sam_wrapper import SamOrSkip

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--image", type=Path, help="Single RGB image for a smoke test")
    p.add_argument("--box", type=int, nargs=4, default=[10, 10, 80, 80], help="x0 y0 x1 y1")
    p.add_argument("--checkpoint", default="")
    p.add_argument("--out", type=Path, default=Path("killer_out.json"))
    args = p.parse_args()

    if args.image and args.image.exists() and Image is not None:
        img = np.array(Image.open(args.image).convert("RGB"))
    else:
        img = np.zeros((128, 128, 3), np.uint8)
        img[20:90, 20:90] = (200, 40, 40)
        print("No --image; using synthetic blob (not a benchmark).", file=sys.stderr)

    h, w = img.shape[:2]
    box = tuple(args.box)
    gt = ellipse_mask(h, w, box)
    filled = mean_fill(img, box)
    inpainted = telea_inpaint(img, box)
    ell = ellipse_mask(h, w, box)

    sam = SamOrSkip(args.checkpoint or None)
    rec = {
        "sam_available": sam.ok,
        "dice_ellipse_vs_gt": dice(ell, gt),
        "note": "ACTUAL: only this local run. EXPECTED trends are in experiments.md. "
        "ellipse vs GT is tautological if GT is the ellipse.",
        "epistemic": "ACTUAL_EXPERIMENTAL_RESULT only for dice_ellipse_vs_gt on this image",
    }
    if sam.ok:
        m0 = sam.predict_box(img, box)
        m1 = sam.predict_box(filled, box)
        m2 = sam.predict_box(inpainted, box)
        rec["dice_sam_original"] = None if m0 is None else dice(m0, gt)
        rec["dice_sam_fill"] = None if m1 is None else dice(m1, gt)
        rec["dice_sam_inpaint"] = None if m2 is None else dice(m2, gt)
    args.out.write_text(json.dumps(rec, indent=2))
    print(json.dumps(rec, indent=2))

if __name__ == "__main__":
    main()
