"""Pre-registered agreement metrics: Hungarian IoU, ARI, boundary-F.

All three are reported together, always. `Idea_01/reviewer_attacks.md` treats
reporting a subset as metric shopping, so no function here returns a "best"
metric and there is no ranking helper.
"""

from __future__ import annotations

import numpy as np

try:  # pragma: no cover - environment dependent
    from scipy.optimize import linear_sum_assignment as _scipy_lsa
except ImportError:  # pragma: no cover
    _scipy_lsa = None


def _hungarian_min(cost: np.ndarray) -> np.ndarray:
    """Optimal assignment minimising `cost`; returns col index per row.

    Pure-numpy O(n^3) augmenting-path (JV/e-maxx form) so that the metric is
    exact without scipy. Rows are padded to satisfy n <= m.
    """
    n, m = cost.shape
    if n > m:
        pad = np.full((n, n - m), cost.max() + 1.0)
        cost = np.concatenate([cost, pad], axis=1)
        m = cost.shape[1]

    inf = float("inf")
    u = np.zeros(n + 1)
    v = np.zeros(m + 1)
    p = np.zeros(m + 1, dtype=int)
    way = np.zeros(m + 1, dtype=int)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = np.full(m + 1, inf)
        used = np.zeros(m + 1, dtype=bool)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = inf
            j1 = 0
            for j in range(1, m + 1):
                if used[j]:
                    continue
                cur = cost[i0 - 1, j - 1] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1

    assignment = np.full(n, -1, dtype=int)
    for j in range(1, m + 1):
        if p[j] > 0:
            assignment[p[j] - 1] = j - 1
    return assignment


def _pairwise_iou(masks_a: list[np.ndarray], masks_b: list[np.ndarray]) -> np.ndarray:
    a = np.stack([m.reshape(-1).astype(bool) for m in masks_a])
    b = np.stack([m.reshape(-1).astype(bool) for m in masks_b])
    inter = (a.astype(np.int32) @ b.T.astype(np.int32)).astype(np.float64)
    area_a = a.sum(1)[:, None].astype(np.float64)
    area_b = b.sum(1)[None, :].astype(np.float64)
    union = area_a + area_b - inter
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(union > 0, inter / union, 0.0)


def hungarian_iou(masks_a: list[np.ndarray], masks_b: list[np.ndarray]) -> float:
    """Mean IoU over the optimal one-to-one matching, normalised by min(|A|,|B|).

    Normalising by min() rather than |A| is deliberate. AMG returns a nested
    *inventory* of tens of masks while a clusterer returns a partition of k, so
    dividing by |A| would mostly measure the cardinality gap and would report
    near-zero agreement even for a perfect subset match. Cardinality is a real
    difference, but it is a *separate* one: report it with `cardinality_ratio`
    and `coverage_iou`, not folded silently into the match quality.
    """
    if not masks_a or not masks_b:
        return 0.0
    iou = _pairwise_iou(masks_a, masks_b)
    if _scipy_lsa is not None:
        rows, cols = _scipy_lsa(-iou)
        matched = iou[rows, cols]
    else:
        assignment = _hungarian_min(-iou)
        matched = np.array(
            [iou[i, j] for i, j in enumerate(assignment) if 0 <= j < iou.shape[1]]
        )
    if matched.size == 0:
        return 0.0
    return float(matched.sum() / min(len(masks_a), len(masks_b)))


def coverage_iou(masks_a: list[np.ndarray], masks_b: list[np.ndarray]) -> float:
    """Directional set agreement (1/|A|) * sum_A max_B IoU(A, B).

    This is the formula in `references/math.md`. Many-to-one, so it asks "is
    every AMG mask explained by *some* cluster?" rather than "do the two mask
    sets pair up?". Directional: coverage_iou(A,B) != coverage_iou(B,A).
    """
    if not masks_a or not masks_b:
        return 0.0
    return float(_pairwise_iou(masks_a, masks_b).max(axis=1).mean())


def cardinality_ratio(masks_a: list[np.ndarray], masks_b: list[np.ndarray]) -> float:
    """|A| / |B|. Reported alongside agreement so a mismatch cannot hide."""
    if not masks_b:
        return float("inf")
    return len(masks_a) / len(masks_b)


def masks_to_label_map(masks: list[np.ndarray], shape: tuple[int, int]) -> np.ndarray:
    """Paint a mask set into an int label map; 0 means unassigned.

    Overlaps go to the smaller mask, which keeps nested AMG masks from being
    erased by their own parent.
    """
    out = np.zeros(shape, dtype=np.int32)
    order = sorted(range(len(masks)), key=lambda i: int(np.asarray(masks[i]).sum()), reverse=True)
    for rank, idx in enumerate(order, start=1):
        out[np.asarray(masks[idx]).astype(bool)] = rank
    return out


def adjusted_rand_index(labels_a: np.ndarray, labels_b: np.ndarray) -> float:
    """ARI between two pixel labellings. 1.0 identical, ~0.0 chance."""
    a = np.asarray(labels_a).reshape(-1)
    b = np.asarray(labels_b).reshape(-1)
    if a.shape != b.shape:
        raise ValueError("label maps must have the same shape")
    n = a.size
    if n < 2:
        return 0.0

    _, ai = np.unique(a, return_inverse=True)
    _, bi = np.unique(b, return_inverse=True)
    contingency = np.zeros((ai.max() + 1, bi.max() + 1), dtype=np.int64)
    np.add.at(contingency, (ai, bi), 1)

    def comb2(x: np.ndarray | int) -> np.ndarray | float:
        x = np.asarray(x, dtype=np.float64)
        return x * (x - 1.0) / 2.0

    sum_ij = comb2(contingency).sum()
    sum_i = comb2(contingency.sum(axis=1)).sum()
    sum_j = comb2(contingency.sum(axis=0)).sum()
    total = comb2(n)
    expected = sum_i * sum_j / total if total else 0.0
    maximum = 0.5 * (sum_i + sum_j)
    denom = maximum - expected
    if abs(denom) < 1e-12:
        return 1.0 if abs(sum_ij - expected) < 1e-12 else 0.0
    return float((sum_ij - expected) / denom)


def label_boundaries(labels: np.ndarray) -> np.ndarray:
    """Pixels whose 4-neighbourhood contains a different label."""
    lab = np.asarray(labels)
    edge = np.zeros(lab.shape, dtype=bool)
    edge[:-1, :] |= lab[:-1, :] != lab[1:, :]
    edge[1:, :] |= lab[:-1, :] != lab[1:, :]
    edge[:, :-1] |= lab[:, :-1] != lab[:, 1:]
    edge[:, 1:] |= lab[:, :-1] != lab[:, 1:]
    return edge


def _dilate(mask: np.ndarray, radius: int) -> np.ndarray:
    out = mask.copy()
    for _ in range(radius):
        grown = out.copy()
        grown[:-1, :] |= out[1:, :]
        grown[1:, :] |= out[:-1, :]
        grown[:, :-1] |= out[:, 1:]
        grown[:, 1:] |= out[:, :-1]
        out = grown
    return out


def boundary_f(labels_a: np.ndarray, labels_b: np.ndarray, tolerance: int = 2) -> float:
    """Boundary F-score between two labellings within `tolerance` pixels."""
    ba = label_boundaries(labels_a)
    bb = label_boundaries(labels_b)
    if not ba.any() and not bb.any():
        return 1.0
    if not ba.any() or not bb.any():
        return 0.0
    precision = float((ba & _dilate(bb, tolerance)).sum()) / float(ba.sum())
    recall = float((bb & _dilate(ba, tolerance)).sum()) / float(bb.sum())
    if precision + recall == 0.0:
        return 0.0
    return float(2 * precision * recall / (precision + recall))
