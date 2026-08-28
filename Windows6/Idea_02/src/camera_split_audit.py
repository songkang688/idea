"""
Synthetic camera-split inflation demo.

NOT a real detector result. Features are constructed so camera ID is
partially encoded; random splits leak camera identity into val.

Run: python camera_split_audit.py
"""
from __future__ import annotations

import numpy as np


def make_dataset(n_cam: int = 8, n_per: int = 40, d: int = 16, seed: int = 0):
    rng = np.random.default_rng(seed)
    X, cam, y = [], [], []
    for c in range(n_cam):
        proto = rng.normal(size=d)
        for i in range(n_per):
            x = proto + 0.25 * rng.normal(size=d)
            # label weakly depends on camera + noise (shortcut)
            lab = int((proto[0] + rng.normal() * 0.3) > 0)
            X.append(x)
            cam.append(c)
            y.append(lab)
    return np.stack(X), np.array(cam), np.array(y)


def split_random(n, seed=1, frac=0.3):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(n)
    k = int(n * frac)
    return idx[k:], idx[:k]


def split_camera(cam, seed=1, n_test_cam=2):
    rng = np.random.default_rng(seed)
    u = np.unique(cam)
    rng.shuffle(u)
    test_c = set(u[:n_test_cam])
    tr = np.where(~np.isin(cam, list(test_c)))[0]
    te = np.where(np.isin(cam, list(test_c)))[0]
    return tr, te


def fit_logreg(X, y, steps=80, lr=0.2):
    w = np.zeros(X.shape[1])
    b = 0.0
    for _ in range(steps):
        z = X @ w + b
        p = 1 / (1 + np.exp(-np.clip(z, -20, 20)))
        w -= lr * X.T @ (p - y) / len(y)
        b -= lr * (p - y).mean()
    return w, b


def acc(X, y, w, b):
    p = 1 / (1 + np.exp(-np.clip(X @ w + b, -20, 20)))
    return float(((p > 0.5) == y).mean())


def camera_probe_acc(X, cam, tr, te):
    # one-vs-rest on cameras seen in train; eval camera classification on train cams held-out frames
    # simplify: 2-class probe of cam0 vs cam1 using linear model on subset
    m = (cam == 0) | (cam == 1)
    y = (cam == 1).astype(np.float64)
    X, y = X[m], y[m]
    n = len(y)
    tr, te = split_random(n, seed=3)
    w, b = fit_logreg(X[tr], y[tr])
    return acc(X[te], y[te], w, b)


def main():
    X, cam, y = make_dataset()
    tr_r, te_r = split_random(len(y))
    tr_c, te_c = split_camera(cam)
    wr, br = fit_logreg(X[tr_r], y[tr_r].astype(np.float64))
    wc, bc = fit_logreg(X[tr_c], y[tr_c].astype(np.float64))
    print("HYPOTHESIS demo (synthetic features, NOT measured smoke mAP)")
    print("random-split acc:", round(acc(X[te_r], y[te_r], wr, br), 3))
    print("camera-disjoint acc:", round(acc(X[te_c], y[te_c], wc, bc), 3))
    print("EXPECTED: random > camera-disjoint if leakage exists")
    print("camera-ID probe acc (cam0 vs cam1):", round(camera_probe_acc(X, cam, tr_r, te_r), 3))


if __name__ == "__main__":
    main()
