"""A deliberately tiny stand-in detector, and a refusal for the real one."""

from __future__ import annotations

import numpy as np


class TinyDetector:
    """Logistic regression on frame features. A placeholder, not a detector.

    It exists so the split machinery has something to score with. It has no
    convolution, no image input and no localisation, so it cannot produce mAP
    and does not pretend to: `run_protocol` reports image-level AP and FAR.
    """

    def __init__(self, lr: float = 0.2, steps: int = 300, l2: float = 1e-3) -> None:
        self.lr = lr
        self.steps = steps
        self.l2 = l2
        self.w: np.ndarray | None = None
        self.b: float = 0.0

    def fit(self, x: np.ndarray, y: np.ndarray) -> "TinyDetector":
        x = np.asarray(x, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)
        self.w = np.zeros(x.shape[1])
        self.b = 0.0
        for _ in range(self.steps):
            p = self.predict_proba(x)
            grad_w = x.T @ (p - y) / len(y) + self.l2 * self.w
            self.w -= self.lr * grad_w
            self.b -= self.lr * float((p - y).mean())
        return self

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        if self.w is None:
            raise RuntimeError("fit() before predict_proba()")
        z = np.asarray(x, dtype=np.float64) @ self.w + self.b
        return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


def train_real_detector(*_args, **_kwargs):
    """Real detector training. Not implemented here on purpose."""
    raise NotImplementedError(
        "Card E1 in Idea_02/experiments.md calls for YOLOv8n on a real smoke "
        "corpus, 1 seed x 3 protocols, ~10 GPU-h (HYPOTHESIS). Neither the "
        "weights nor the data ship here, and GATE-A is still OPEN. "
        "Windows6 has produced NO smoke mAP; Idea_02/proposal.md states "
        "'We have not trained a detector here.'"
    )
