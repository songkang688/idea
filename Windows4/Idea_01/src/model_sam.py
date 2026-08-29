"""Model zoo behind one interface.

PromptableSegmenter.predict(image, box) -> bool mask. Backends:

- OfficialSAMWrapper : frozen SAM via the released `segment-anything` package + checkpoint.
  This is the ONLY backend whose outputs may ever be reported as scientific results.
- PromptOnlySAMNull  : SAM forward with the image embedding replaced by a dataset-mean
  embedding — "the interpolator claim in one number" (Stage-4 R2 missing-baseline 1).
- BoxFillBaseline    : stub; literal box->mask interpolator. Used when weights are absent
  and as the E0 negative control (must be classified 'interpolator').
- OracleThresholdBaseline : stub that genuinely consults pixels (Otsu inside the box).
  E0 positive control (must be classified 'seeing').
- LearnedBoxToMaskNull : tiny regressor, box geometry only, never sees pixels
  (Stage-4 R2 missing-baseline 2). Trained by src/train.py.

Embedding-level interior replacement (S-014 softened: dataset-mean vectors inside the box)
is exposed on OfficialSAMWrapper as `predict_with_interior_mean_embedding` — secondary
probe only (E2), unavailable on stubs by design.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

import numpy as np

from .utils import HAS_CV2, Box, to_rgb_uint8
from .interventions import boxfill_null

if HAS_CV2:
    import cv2  # type: ignore

try:
    import torch

    HAS_TORCH = True
except Exception:  # pragma: no cover
    torch = None
    HAS_TORCH = False


class PromptableSegmenter(ABC):
    name: str = "abstract"
    uses_image_evidence: Optional[bool] = None  # ground truth for E0 assertions

    @abstractmethod
    def predict(self, image: np.ndarray, box: Box) -> np.ndarray:
        """image: float [0,1] HxW or HxWx3; box: (x0,y0,x1,y1). Returns bool HxW mask."""


# ------------------------------------------------------------------ stubs

class BoxFillBaseline(PromptableSegmenter):
    """The literal interpolator. E0 must classify this as 'interpolator'."""

    name = "boxfill_stub"
    uses_image_evidence = False

    def predict(self, image: np.ndarray, box: Box) -> np.ndarray:
        return boxfill_null(box, image.shape[:2])


class OracleThresholdBaseline(PromptableSegmenter):
    """A model that genuinely 'sees': Otsu threshold inside the box, polarity chosen
    automatically, largest connected component kept. E0 must classify it as 'seeing'
    in at least one stratum (it degrades honestly at low contrast)."""

    name = "oracle_threshold_stub"
    uses_image_evidence = True

    def predict(self, image: np.ndarray, box: Box) -> np.ndarray:
        img = image if image.ndim == 2 else image.mean(axis=-1)
        x0, y0, x1, y1 = box
        crop = img[y0:y1, x0:x1].astype(np.float32)
        t = _otsu(crop)
        fg = crop > t
        # polarity: in a TIGHT box the object is the majority, so "minority = object"
        # fails; instead treat the box border ring as background reference
        border = np.zeros_like(fg)
        r = max(1, min(2, fg.shape[0] // 4, fg.shape[1] // 4))
        border[:r, :] = border[-r:, :] = border[:, :r] = border[:, -r:] = True
        if fg[border].mean() > 0.5:  # border mostly classified as fg -> flip
            fg = ~fg
        fg = _largest_component(fg)
        out = np.zeros(img.shape[:2], dtype=bool)
        out[y0:y1, x0:x1] = fg
        return out


def _otsu(x: np.ndarray) -> float:
    hist, edges = np.histogram(x, bins=64)
    centers = 0.5 * (edges[:-1] + edges[1:])
    total = hist.sum()
    best_t, best_var = centers[0], -1.0
    wb = 0.0
    sumb = 0.0
    sum_all = float((hist * centers).sum())
    for i in range(len(hist)):
        wb += hist[i]
        if wb == 0 or wb == total:
            continue
        sumb += hist[i] * centers[i]
        wf = total - wb
        mb, mf = sumb / wb, (sum_all - sumb) / wf
        var = wb * wf * (mb - mf) ** 2
        if var > best_var:
            best_var, best_t = var, centers[i]
    return float(best_t)


def _largest_component(mask: np.ndarray) -> np.ndarray:
    if not mask.any():
        return mask
    if HAS_CV2:
        n, lab = cv2.connectedComponents(mask.astype(np.uint8))
        if n <= 2:
            return mask
        sizes = [(lab == i).sum() for i in range(1, n)]
        return lab == (1 + int(np.argmax(sizes)))
    return mask  # fallback: keep all components


# ------------------------------------------------------------ learned null

class LearnedBoxToMaskNull(PromptableSegmenter):
    """Tiny regressor: normalized box geometry -> GxG in-box mask logits, warped into the
    box. Never receives pixels. If this matches (ablated) SAM, 'interpolation' is a
    property of label statistics, not of SAM (Stage-4 R2, verbatim obligation)."""

    name = "learned_boxmask_null"
    uses_image_evidence = False

    def __init__(self, ckpt_path: str, device: str = "cpu"):
        if not HAS_TORCH:
            raise RuntimeError("torch is required for the learned null: pip install torch")
        if not os.path.exists(ckpt_path):
            raise FileNotFoundError(
                f"learned-null checkpoint not found at {ckpt_path}; "
                "run `python -m src.train --config configs/default.yaml` first"
            )
        payload = torch.load(ckpt_path, map_location=device, weights_only=True)
        self.grid = int(payload["grid"])
        self.net = build_null_net(self.grid, payload["hidden"])
        self.net.load_state_dict(payload["state_dict"])
        self.net.eval()
        self.device = device

    @staticmethod
    def featurize(box: Box, shape) -> np.ndarray:
        h, w = shape[:2]
        x0, y0, x1, y1 = box
        bw, bh = (x1 - x0) / w, (y1 - y0) / h
        cx, cy = (x0 + x1) / (2 * w), (y0 + y1) / (2 * h)
        aspect = np.log((x1 - x0 + 1e-6) / (y1 - y0 + 1e-6))
        area = np.sqrt(max(bw * bh, 1e-8))
        return np.array([cx, cy, bw, bh, aspect, area], dtype=np.float32)

    def predict(self, image: np.ndarray, box: Box) -> np.ndarray:
        feats = torch.from_numpy(self.featurize(box, image.shape)).unsqueeze(0)
        with torch.no_grad():
            logits = self.net(feats).reshape(self.grid, self.grid)
            prob = torch.sigmoid(logits).numpy()
        x0, y0, x1, y1 = box
        bw, bh = max(1, x1 - x0), max(1, y1 - y0)
        if HAS_CV2:
            prob_up = cv2.resize(prob, (bw, bh), interpolation=cv2.INTER_LINEAR)
        else:
            yi = (np.arange(bh) * self.grid // bh).clip(0, self.grid - 1)
            xi = (np.arange(bw) * self.grid // bw).clip(0, self.grid - 1)
            prob_up = prob[np.ix_(yi, xi)]
        out = np.zeros(image.shape[:2], dtype=bool)
        out[y0:y1, x0:x1] = prob_up > 0.5
        return out


def build_null_net(grid: int, hidden: List[int]):
    """MLP 6 -> hidden -> grid*grid logits. Capacity cap per proposal §26 (<100k params)."""
    import torch.nn as nn

    dims = [6] + list(hidden)
    layers: list = []
    for a, b in zip(dims[:-1], dims[1:]):
        layers += [nn.Linear(a, b), nn.ReLU()]
    layers += [nn.Linear(dims[-1], grid * grid)]
    return nn.Sequential(*layers)


# ------------------------------------------------------------- official SAM

_SAM_INSTALL_HELP = (
    "Official SAM backend requested but unavailable.\n"
    "  pip install git+https://github.com/facebookresearch/segment-anything.git\n"
    "  download a checkpoint (e.g. sam_vit_b_01ec64.pth) from the repo's model zoo and\n"
    "  set model.sam_checkpoint in configs/default.yaml.\n"
    "Until then, use model.backend=stub (decision-logic validation only; no science)."
)


class OfficialSAMWrapper(PromptableSegmenter):
    """Frozen SAM (Kirillov et al., arXiv:2304.02643) with a box prompt.

    Notes for E1:
      - multimask=False fixes the output head (multimask+IoU-selection is a pre-registered
        sensitivity row, proposal §18).
      - predict() calls set_image per call for correctness; E1 batches by image via
        `predict_cached` to amortize the encoder.
    """

    name = "sam_official"
    uses_image_evidence = True

    def __init__(
        self,
        checkpoint: str,
        model_type: str = "vit_b",
        device: str = "cpu",
        multimask: bool = False,
    ):
        try:
            from segment_anything import SamPredictor, sam_model_registry  # type: ignore
        except ImportError as e:
            raise RuntimeError(_SAM_INSTALL_HELP) from e
        if not checkpoint or not os.path.exists(checkpoint):
            raise FileNotFoundError(f"SAM checkpoint not found: {checkpoint}\n{_SAM_INSTALL_HELP}")
        sam = sam_model_registry[model_type](checkpoint=checkpoint)
        sam.to(device)
        sam.eval()
        self.predictor = SamPredictor(sam)
        self.multimask = multimask
        self.name = f"sam_{model_type}"
        self._cached_key: Optional[str] = None

    def _set_image(self, image: np.ndarray, key: Optional[str] = None) -> None:
        if key is not None and key == self._cached_key:
            return
        self.predictor.set_image(to_rgb_uint8(image))
        self._cached_key = key

    def predict(self, image: np.ndarray, box: Box) -> np.ndarray:
        return self.predict_cached(image, box, key=None)

    def predict_cached(self, image: np.ndarray, box: Box, key: Optional[str]) -> np.ndarray:
        self._set_image(image, key)
        masks, scores, _ = self.predictor.predict(
            box=np.asarray(box, dtype=np.float32), multimask_output=self.multimask
        )
        idx = int(np.argmax(scores)) if self.multimask else 0
        return masks[idx].astype(bool)

    # ---- embedding-space hooks (secondary probes / prompt-only null) ----

    def get_image_embedding(self, image: np.ndarray) -> np.ndarray:
        self._set_image(image, key=None)
        return self.predictor.get_image_embedding().detach().cpu().numpy()

    def predict_with_embedding(self, embedding: np.ndarray, image_shape, box: Box) -> np.ndarray:
        """Forward with an arbitrary image embedding (prompt-only null / interior-mean
        probe). Requires a prior set_image on any image of the same size to populate
        predictor transforms; then overrides predictor.features."""
        self._set_image(np.zeros(image_shape[:2], dtype=np.float32), key="__override__")
        self.predictor.features = torch.from_numpy(embedding).to(
            self.predictor.model.device if hasattr(self.predictor.model, "device") else "cpu"
        )
        masks, scores, _ = self.predictor.predict(
            box=np.asarray(box, dtype=np.float32), multimask_output=self.multimask
        )
        self._cached_key = None
        idx = int(np.argmax(scores)) if self.multimask else 0
        return masks[idx].astype(bool)

    def predict_with_interior_mean_embedding(
        self, image: np.ndarray, box: Box, mean_embedding: np.ndarray
    ) -> np.ndarray:
        """S-014 softened (SECONDARY, E2 only): replace embedding vectors whose receptive
        centers fall inside the box with the dataset-mean vector (never zeros —
        zeros are maximally off-manifold, per the Stage-4 review)."""
        emb = self.get_image_embedding(image).copy()  # (1, C, He, We)
        _, _, He, We = emb.shape
        h, w = image.shape[:2]
        x0, y0, x1, y1 = box
        ex0, ex1 = int(x0 / w * We), max(int(x0 / w * We) + 1, int(np.ceil(x1 / w * We)))
        ey0, ey1 = int(y0 / h * He), max(int(y0 / h * He) + 1, int(np.ceil(y1 / h * He)))
        emb[:, :, ey0:ey1, ex0:ex1] = mean_embedding[:, :, ey0:ey1, ex0:ex1]
        return self.predict_with_embedding(emb, image.shape, box)


class PromptOnlySAMNull(PromptableSegmenter):
    """f(mean-embedding, box): the decoder receives the box prompt and its full positional
    scaffold, but a dataset-mean image embedding — the measured answer to R2 attack (iii)."""

    name = "sam_prompt_only_null"
    uses_image_evidence = False

    def __init__(self, sam: OfficialSAMWrapper, mean_embedding: np.ndarray, image_shape):
        self.sam = sam
        self.mean_embedding = mean_embedding
        self.image_shape = image_shape

    def predict(self, image: np.ndarray, box: Box) -> np.ndarray:
        return self.sam.predict_with_embedding(self.mean_embedding, self.image_shape, box)


def compute_mean_embedding(sam: OfficialSAMWrapper, images: List[np.ndarray]) -> np.ndarray:
    """Dataset-mean image embedding for the prompt-only null (computed once per cohort,
    on the SAME frozen split, before any counterfactual forward)."""
    acc = None
    for im in images:
        e = sam.get_image_embedding(im)
        acc = e if acc is None else acc + e
    return acc / float(len(images))


# ----------------------------------------------------------------- factory

def build_eval_models(cfg: Dict) -> List[PromptableSegmenter]:
    m = cfg["model"]
    if m["backend"] == "stub":
        registry = {
            "boxfill": BoxFillBaseline,
            "oracle_threshold": OracleThresholdBaseline,
        }
        return [registry[name]() for name in m["stub_models"]]
    if m["backend"] == "sam":
        return [
            OfficialSAMWrapper(
                checkpoint=m["sam_checkpoint"],
                model_type=m.get("sam_model_type", "vit_b"),
                device=m.get("device", "cpu"),
                multimask=bool(m.get("multimask", False)),
            )
        ]
    raise ValueError(f"unknown model.backend: {m['backend']}")
