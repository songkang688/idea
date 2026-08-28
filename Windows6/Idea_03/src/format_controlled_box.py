"""
Format-controlled box scoring vs a linear probe on fake visual tokens.

NOT a measurement of any real VLM.

Run: python format_controlled_box.py
"""
from __future__ import annotations

import numpy as np


def parse_box(s: str) -> np.ndarray | None:
    try:
        parts = [float(x) for x in s.replace(",", " ").split()]
        if len(parts) != 4:
            return None
        return np.array(parts)
    except ValueError:
        return None


def iou(a: np.ndarray, b: np.ndarray) -> float:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    ua = max(0, ax2 - ax1) * max(0, ay2 - ay1)
    ub = max(0, bx2 - bx1) * max(0, by2 - by1)
    den = ua + ub - inter
    return float(inter / den) if den else 0.0


def chatty_decode(box: np.ndarray, chat: bool, rng: np.random.Generator) -> str:
    if chat:
        # format tax: extra tokens, sometimes drop a number
        if rng.random() < 0.3:
            return f"The object is around ({box[0]:.0f},{box[1]:.0f})"
        return f"Sure! [{box[0]:.1f}, {box[1]:.1f}, {box[2]:.1f}, {box[3]:.1f}]"
    return f"{box[0]:.1f} {box[1]:.1f} {box[2]:.1f} {box[3]:.1f}"


def constrained(box: np.ndarray) -> str:
    return f"{box[0]:.1f} {box[1]:.1f} {box[2]:.1f} {box[3]:.1f}"


def probe_fit(V, boxes):
    # least squares V @ W ≈ boxes
    w, *_ = np.linalg.lstsq(V, boxes, rcond=None)
    return w


def main():
    rng = np.random.default_rng(0)
    n, d = 64, 8
    boxes = rng.uniform(0, 100, size=(n, 4))
    boxes[:, 2:] += boxes[:, :2]
    V = rng.normal(size=(n, d))
    # visual tokens contain box linearly + noise
    V[:, :4] = boxes / 100 + 0.01 * rng.normal(size=(n, 4))

    gen_iou_base, gen_iou_chat = [], []
    for i in range(n):
        gb = parse_box(constrained(boxes[i]))
        gc = parse_box(chatty_decode(boxes[i], True, rng))
        gen_iou_base.append(iou(gb, boxes[i]) if gb is not None else 0.0)
        gen_iou_chat.append(iou(gc, boxes[i]) if gc is not None else 0.0)

    w = probe_fit(V, boxes)
    pred = V @ w
    probe_err = np.mean(np.abs(pred - boxes))

    print("HYPOTHESIS demo (synthetic, NOT a real VLM)")
    print("constrained gen IoU (base-like):", round(float(np.mean(gen_iou_base)), 3))
    print("chatty gen IoU:", round(float(np.mean(gen_iou_chat)), 3))
    print("linear probe MAE on visual tokens:", round(float(probe_err), 3))
    print("EXPECTED pattern for format tax: chatty IoU drops, probe still OK")


if __name__ == "__main__":
    main()
