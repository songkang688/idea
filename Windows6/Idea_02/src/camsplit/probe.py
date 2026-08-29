"""Camera-ID probe (H3) — the number that turns "leakage" into a measurement.

If a linear probe on frozen features can name the camera, the representation
carries camera identity, and any split that shares cameras shares that
information with the test set. Reported against an explicit majority-class
chance level, because with unbalanced cameras raw accuracy flatters.
"""

from __future__ import annotations

import numpy as np


def chance_level(labels: np.ndarray) -> float:
    """Majority-class rate — the honest floor for a multi-class probe."""
    labels = np.asarray(labels)
    if labels.size == 0:
        return float("nan")
    _, counts = np.unique(labels, return_counts=True)
    return float(counts.max() / labels.size)


def _softmax(z: np.ndarray) -> np.ndarray:
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / np.clip(e.sum(axis=1, keepdims=True), 1e-12, None)


def camera_probe(
    features: np.ndarray,
    camera: np.ndarray,
    train_idx: np.ndarray,
    test_idx: np.ndarray,
    steps: int = 300,
    lr: float = 0.5,
    l2: float = 1e-3,
) -> dict[str, float]:
    """Multinomial logistic probe: features -> camera id.

    Returns accuracy alongside its chance level and the margin. A probe at
    chance kills H3.

    **The split matters more than the classifier.** Two constraints:

    1. Evaluate on held-out data from the *training* cameras. Asking a
       classifier to name a camera it never saw is meaningless, so
       camera-disjoint indices are the wrong input here.
    2. Evaluate **event-disjoint**. On a random split the same fire episode
       appears on both sides, and the probe can name the camera by recognising
       the episode rather than the tower. That measures event memorisation, not
       camera signature, and it inflates H3 for the wrong reason. Measured
       during W6-T3: with the camera signature switched off entirely, a
       random-split probe still beat chance by ~0.17 purely through shared
       events. `test_probe_is_near_chance_when_no_signature_exists` pins the
       event-disjoint version as the negative control.
    """
    x = np.asarray(features, dtype=np.float64)
    cams = np.asarray(camera)
    classes = np.unique(cams[train_idx])
    if classes.size < 2:
        return {"accuracy": float("nan"), "chance": float("nan"), "margin": float("nan")}

    lookup = {c: i for i, c in enumerate(classes)}
    keep_test = np.array([c in lookup for c in cams[test_idx]])
    test_idx = np.asarray(test_idx)[keep_test]
    if test_idx.size == 0:
        return {"accuracy": float("nan"), "chance": float("nan"), "margin": float("nan")}

    y_tr = np.array([lookup[c] for c in cams[train_idx]])
    y_te = np.array([lookup[c] for c in cams[test_idx]])
    onehot = np.eye(classes.size)[y_tr]

    w = np.zeros((x.shape[1], classes.size))
    b = np.zeros(classes.size)
    xt = x[train_idx]
    for _ in range(steps):
        p = _softmax(xt @ w + b)
        w -= lr * (xt.T @ (p - onehot) / len(y_tr) + l2 * w)
        b -= lr * (p - onehot).mean(axis=0)

    pred = (x[test_idx] @ w + b).argmax(axis=1)
    accuracy = float((pred == y_te).mean())
    chance = chance_level(y_te)
    return {"accuracy": accuracy, "chance": chance, "margin": accuracy - chance}
