"""B-0001 dissociation hook — OFF BY DEFAULT, NOT part of B-0114's claims.

exp_02 (B-0001) asks a *different* question from this prototype: is the
patch-norm map a usable per-pixel **error predictor**? The PI binding treats
B-0114 x B-0001 as one bet unless the experiments dissociate; exp_02's
dissociation plan states that the B-0114 paper makes **no uncertainty
claims** and shares no headline metric with B-0001.

This module is therefore quarantined:

- It is invoked only with the explicit ``--with-b0001-hook`` flag.
- Its output is printed under a banner marking it B-0001 TERRITORY.
- Nothing in metrics.py / signatures.py imports it, and no B-0114 readout
  (decomposition, H2, signatures) depends on it.

What it computes (when explicitly asked): AUROC of the patch-token norm map
predicting per-patch prediction *error* of a given arm's head — the toy
skeleton of exp_02's predictor (a), with none of exp_02's mandatory
stratification or baselines. It exists so the merged-paper branch of the
decision rule has a code seam, not to make claims.
"""

from __future__ import annotations

import numpy as np
import torch

from .config import ExperimentConfig
from .synthetic_data import SceneBatch
from .tiny_vit import DenseHead, TinyViT

BANNER = (
    "B-0001 TERRITORY (norm-map-vs-error) — separate idea, separate metric hook.\n"
    "Not a B-0114 claim; enabled only because --with-b0001-hook was passed."
)


def auroc(scores: np.ndarray, labels: np.ndarray) -> float:
    """Rank-based AUROC (Mann-Whitney), no sklearn dependency."""
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    ranks = np.argsort(np.argsort(np.concatenate([pos, neg]))) + 1
    r_pos = ranks[: len(pos)].sum()
    u = r_pos - len(pos) * (len(pos) + 1) / 2
    return float(u / (len(pos) * len(neg)))


@torch.no_grad()
def norm_error_auroc(
    backbone: TinyViT,
    head: DenseHead,
    prompt: torch.Tensor | None,
    prompt_is_sink: bool,
    val: SceneBatch,
    cfg: ExperimentConfig,
) -> dict:
    """AUROC of patch-norm predicting per-patch error (patch-majority label
    vs the head's majority prediction inside that patch)."""
    bs = cfg.train.batch_size
    p = cfg.data.patch_size
    norms, errors = [], []
    for i in range(0, val.images.shape[0], bs):
        imgs = val.images[i : i + bs]
        patch_labels = val.patch_labels[i : i + bs]  # (B, Hp, Wp)
        out = backbone(imgs, prompt=prompt, prompt_is_sink=prompt_is_sink)
        feats = out["patch_tokens"]  # (B, N, D)
        pred_px = head(feats, backbone.cfg.grid).argmax(dim=1)  # (B, H, W)
        B, H, W = pred_px.shape
        hp, wp = H // p, W // p
        tiles = pred_px.reshape(B, hp, p, wp, p).permute(0, 1, 3, 2, 4).reshape(B, hp, wp, -1)
        pred_patch = tiles.mode(dim=-1).values  # majority prediction per patch
        err = (pred_patch != patch_labels).flatten().float()
        norms.append(feats.norm(dim=-1).flatten())
        errors.append(err)
    n = torch.cat(norms).numpy()
    e = torch.cat(errors).numpy()
    return {
        "norm_error_auroc": auroc(n, e),
        "patch_error_rate": float(e.mean()),
        "n_patches": int(e.size),
    }
