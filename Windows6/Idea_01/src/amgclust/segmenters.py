"""Segmenters under comparison: the AMG stand-in, intensity clusterers, superpixels.

The naming here is deliberately unflattering. `amg_mock` is a threshold
connected-component stand-in, not SAM. `slic_lite` is joint (x, y, intensity)
k-means, not the SLIC of the literature. Both must be swapped for the real
thing before any claim is made; `sam_amg` refuses to pretend.
"""

from __future__ import annotations

import numpy as np

try:  # pragma: no cover - environment dependent
    from scipy import ndimage as _ndimage
except ImportError:  # pragma: no cover
    _ndimage = None


def connected_components(binary: np.ndarray) -> np.ndarray:
    """4-connected labelling. Uses scipy when present, else union-find."""
    bw = np.asarray(binary, dtype=bool)
    if _ndimage is not None:
        labelled, _ = _ndimage.label(bw)
        return labelled.astype(np.int32)

    h, w = bw.shape
    labels = np.zeros((h, w), dtype=np.int32)
    parent: list[int] = [0]

    def find(x: int) -> int:
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[max(rx, ry)] = min(rx, ry)

    nxt = 1
    for y in range(h):
        for x in range(w):
            if not bw[y, x]:
                continue
            up = labels[y - 1, x] if y > 0 else 0
            left = labels[y, x - 1] if x > 0 else 0
            if up and left:
                labels[y, x] = min(up, left)
                union(up, left)
            elif up or left:
                labels[y, x] = up or left
            else:
                parent.append(nxt)
                labels[y, x] = nxt
                nxt += 1

    remap: dict[int, int] = {}
    out = np.zeros_like(labels)
    for y in range(h):
        for x in range(w):
            if labels[y, x]:
                root = find(labels[y, x])
                out[y, x] = remap.setdefault(root, len(remap) + 1)
    return out


def _labels_to_masks(labels: np.ndarray, min_area: int = 1) -> list[np.ndarray]:
    masks = []
    for value in np.unique(labels):
        if value == 0:
            continue
        m = labels == value
        if m.sum() >= min_area:
            masks.append(m)
    return masks


def kmeans_1d(img: np.ndarray, k: int, rng: np.random.Generator, iters: int = 40) -> np.ndarray:
    """1-D k-means on intensity. Quantile init makes it deterministic given rng."""
    x = np.asarray(img, dtype=np.float64).reshape(-1)
    centers = np.quantile(x, np.linspace(0.5 / k, 1 - 0.5 / k, k))
    centers = centers + rng.normal(scale=1e-6, size=k)
    labels = np.zeros_like(x, dtype=np.int32)
    for _ in range(iters):
        new_labels = np.abs(x[:, None] - centers[None, :]).argmin(axis=1).astype(np.int32)
        if np.array_equal(new_labels, labels):
            break
        labels = new_labels
        for j in range(k):
            sel = labels == j
            if sel.any():
                centers[j] = x[sel].mean()
    return labels.reshape(np.asarray(img).shape) + 1


def multi_otsu(img: np.ndarray, k: int, bins: int = 256) -> np.ndarray:
    """Exact multi-Otsu on a binned histogram via DP over between-class variance."""
    x = np.asarray(img, dtype=np.float64)
    lo, hi = float(x.min()), float(x.max())
    if hi - lo < 1e-12:
        return np.ones(x.shape, dtype=np.int32)
    hist, edges = np.histogram(x, bins=bins, range=(lo, hi))
    p = hist.astype(np.float64)
    centers = 0.5 * (edges[:-1] + edges[1:])
    cw = np.concatenate([[0.0], np.cumsum(p)])
    cs = np.concatenate([[0.0], np.cumsum(p * centers)])

    def between(a: int, b: int) -> float:
        w = cw[b + 1] - cw[a]
        if w <= 0:
            return 0.0
        s = cs[b + 1] - cs[a]
        return float(s * s / w)

    best = np.full((k + 1, bins), -np.inf)
    argbest = np.zeros((k + 1, bins), dtype=int)
    for b in range(bins):
        best[1, b] = between(0, b)
    for j in range(2, k + 1):
        for b in range(j - 1, bins):
            for a in range(j - 2, b):
                cand = best[j - 1, a] + between(a + 1, b)
                if cand > best[j, b]:
                    best[j, b] = cand
                    argbest[j, b] = a

    cuts: list[int] = []
    b = bins - 1
    for j in range(k, 1, -1):
        a = argbest[j, b]
        cuts.append(a)
        b = a
    thresholds = [edges[c + 1] for c in sorted(cuts)]
    return (np.digitize(x, thresholds) + 1).astype(np.int32)


def gmm_1d(img: np.ndarray, k: int, rng: np.random.Generator, iters: int = 30) -> np.ndarray:
    """1-D diagonal GMM by EM. Kept simple; it is a baseline, not a method."""
    x = np.asarray(img, dtype=np.float64).reshape(-1)
    mu = np.quantile(x, np.linspace(0.5 / k, 1 - 0.5 / k, k)) + rng.normal(scale=1e-6, size=k)
    var = np.full(k, max(float(x.var()), 1e-6) / k)
    pi = np.full(k, 1.0 / k)
    for _ in range(iters):
        d = x[:, None] - mu[None, :]
        logp = -0.5 * (d * d) / var[None, :] - 0.5 * np.log(2 * np.pi * var)[None, :]
        logp = logp + np.log(np.clip(pi, 1e-12, None))[None, :]
        logp -= logp.max(axis=1, keepdims=True)
        r = np.exp(logp)
        r /= np.clip(r.sum(axis=1, keepdims=True), 1e-12, None)
        nk = np.clip(r.sum(axis=0), 1e-12, None)
        pi = nk / len(x)
        mu = (r * x[:, None]).sum(axis=0) / nk
        var = np.clip((r * (x[:, None] - mu[None, :]) ** 2).sum(axis=0) / nk, 1e-9, None)
    return (r.argmax(axis=1).reshape(np.asarray(img).shape) + 1).astype(np.int32)


def slic_lite(
    img: np.ndarray,
    n_segments: int,
    compactness: float,
    rng: np.random.Generator,
    iters: int = 12,
) -> np.ndarray:
    """Grid-seeded k-means in (x, y, intensity). A texture/position baseline.

    This is the *spatial* control: unlike the intensity clusterers it can only
    group pixels that are near each other, so if AMG tracks intensity rather
    than locality this baseline should lose.
    """
    x = np.asarray(img, dtype=np.float64)
    h, w = x.shape
    step = max(int(np.sqrt(h * w / max(n_segments, 1))), 1)
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float64)
    seeds = [
        (float(cy), float(cx), float(x[int(cy), int(cx)]))
        for cy in range(step // 2, h, step)
        for cx in range(step // 2, w, step)
    ]
    if not seeds:
        return np.ones((h, w), dtype=np.int32)
    centers = np.array(seeds) + rng.normal(scale=1e-6, size=(len(seeds), 3))
    scale = compactness * step
    labels = np.zeros((h, w), dtype=np.int32)
    for _ in range(iters):
        d = (
            ((ys[..., None] - centers[:, 0]) / scale) ** 2
            + ((xs[..., None] - centers[:, 1]) / scale) ** 2
            + (x[..., None] - centers[:, 2]) ** 2
        )
        new_labels = d.argmin(axis=-1).astype(np.int32)
        if np.array_equal(new_labels, labels):
            break
        labels = new_labels
        for j in range(len(centers)):
            sel = labels == j
            if sel.any():
                centers[j] = [ys[sel].mean(), xs[sel].mean(), x[sel].mean()]
    return labels + 1


#: Absolute thresholds on a windowed [0, 1] image. NOT quantiles.
#:
#: Quantile thresholds would make this stand-in invariant to any monotone
#: intensity remap, which would silently guarantee that the H2 intensity arm
#: measures nothing. Real AMG thresholds objectness on absolute activations, so
#: absolute cut points are also the more faithful mock.
#: `tests/test_smoke.py::test_amg_mock_is_not_invariant_to_monotone_remap`
#: guards against this being changed back.
DEFAULT_AMG_THRESHOLDS = [0.3, 0.5, 0.7, 0.85]


def amg_mock(img: np.ndarray, thresholds: list[float] | None = None, min_area: int = 4) -> list[np.ndarray]:
    """Multi-threshold connected components as a stand-in for SAM AMG.

    AMG returns a nested, overlapping mask *inventory* rather than a partition,
    so a single threshold is the wrong shape. Sweeping absolute thresholds
    reproduces that structure well enough to exercise the metrics — and nothing
    more. It is not SAM and shares none of SAM's inductive biases.
    """
    x = np.asarray(img, dtype=np.float64)
    if thresholds is None:
        thresholds = list(DEFAULT_AMG_THRESHOLDS)
    masks: list[np.ndarray] = []
    for t in thresholds:
        masks.extend(_labels_to_masks(connected_components(x > t), min_area=min_area))
    return masks


def sam_amg(*_args, **_kwargs) -> list[np.ndarray]:
    """Real SAM AMG. Not implemented here on purpose."""
    raise NotImplementedError(
        "Real SAM AMG needs the segment-anything package and a ViT-B checkpoint, "
        "neither of which ships with this repository. Windows6 has produced NO real "
        "SAM measurements (see Windows6/README.md). Wire this to "
        "SamAutomaticMaskGenerator in the lab; until then use amg_mock and label "
        "every number HYPOTHESIS."
    )
