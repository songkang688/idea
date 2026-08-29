"""Linear probe on frozen visual tokens — the H2 instrument.

The probe answers "is the box still in the representation?" independently of
whether the model can say it. If generation degrades and the probe holds, the
tax is in the decoding policy; if the probe degrades too, alignment moved the
representation.

Ridge, not least squares: with a small train split and correlated token
dimensions, an unregularised fit can appear to recover the box from noise, and
the probe would then report "representation intact" for a checkpoint whose
representation was destroyed.
"""

from __future__ import annotations

import numpy as np


def fit_box_probe(
    tokens: np.ndarray, boxes: np.ndarray, train_idx: np.ndarray, ridge: float = 1e-2
) -> np.ndarray:
    """Fit tokens -> box with a bias column. Returns weights of shape (d+1, 4)."""
    x = np.asarray(tokens, dtype=np.float64)[train_idx]
    y = np.asarray(boxes, dtype=np.float64)[train_idx]
    x = np.concatenate([x, np.ones((len(x), 1))], axis=1)
    penalty = ridge * np.eye(x.shape[1])
    penalty[-1, -1] = 0.0  # never regularise the bias
    return np.linalg.solve(x.T @ x + penalty, x.T @ y)


def probe_error(
    weights: np.ndarray, tokens: np.ndarray, boxes: np.ndarray, test_idx: np.ndarray
) -> float:
    """Mean absolute coordinate error on held-out examples, in pixels."""
    x = np.asarray(tokens, dtype=np.float64)[test_idx]
    x = np.concatenate([x, np.ones((len(x), 1))], axis=1)
    pred = x @ weights
    return float(np.mean(np.abs(pred - np.asarray(boxes, dtype=np.float64)[test_idx])))
