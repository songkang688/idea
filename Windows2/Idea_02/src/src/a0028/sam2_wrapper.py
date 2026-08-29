"""Thin, env-gated adapter that WOULD run the probe on real SAM2.

DISABLED BY DEFAULT. Nothing in the synthetic runner or the tests touches real
SAM2. The gate exists so that a researcher WITH a GPU and SAM2 weights can
point the same stimulus generator at the real model later; it is a stub of the
exp_07 'subject models' module, not a claim that any SAM2 number was produced
by this prototype.

To enable (all three required):

    export A0028_USE_REAL_SAM2=1
    export A0028_SAM2_CHECKPOINT=/path/to/sam2_hiera_*.pt
    export A0028_SAM2_MODEL_CFG=sam2_hiera_l.yaml        # config name for build_sam2_video_predictor

plus ``pip install torch sam2`` (see https://github.com/facebookresearch/sam2).

Rendering: the abstract world is rasterized into RGB frames (colored disks on
a gray background) so the real model receives an actual video. This is the
minimal cut-paste analog; the full exp_07 protocol uses COCO/LVIS crops with
Poisson blending and a paste-artifact placebo arm.
"""

from __future__ import annotations

import os
from typing import List, Tuple

import numpy as np

from .world import Trial

ENV_FLAG = "A0028_USE_REAL_SAM2"
ENV_CHECKPOINT = "A0028_SAM2_CHECKPOINT"
ENV_MODEL_CFG = "A0028_SAM2_MODEL_CFG"

OBJECT_RADIUS = 12


def real_sam2_enabled() -> bool:
    return os.environ.get(ENV_FLAG, "0") == "1"


def render_trial_frames(trial: Trial, size: int = 256) -> Tuple[np.ndarray, Tuple[int, int]]:
    """Rasterize a synthetic trial to (T, H, W, 3) uint8 frames.

    Each candidate becomes a filled disk whose color is a deterministic
    function of its appearance embedding (first three components -> RGB), so
    appearance similarity in embedding space maps to color similarity on
    screen. Returns the frames and the frame-0 target center (x, y) to use as
    the point prompt.
    """
    frames = np.full((len(trial.frames), size, size, 3), 96, dtype=np.uint8)
    yy, xx = np.mgrid[0:size, 0:size]
    prompt_xy = None
    for t, frame in enumerate(trial.frames):
        for cand in frame.candidates:
            color = (np.clip(cand.app[:3], -0.5, 0.5) + 0.5) * 255.0
            cx, cy = float(cand.loc[0]), float(cand.loc[1])
            mask = (xx - cx) ** 2 + (yy - cy) ** 2 <= OBJECT_RADIUS**2
            frames[t][mask] = color.astype(np.uint8)
            if t == 0 and cand.ident == "target":
                prompt_xy = (int(round(cx)), int(round(cy)))
    assert prompt_xy is not None
    return frames, prompt_xy


class RealSAM2Adapter:
    """Instantiates only when the env gate is open AND sam2/torch import."""

    def __init__(self) -> None:
        if not real_sam2_enabled():
            raise RuntimeError(
                f"Real-SAM2 path is disabled (default). Set {ENV_FLAG}=1, "
                f"{ENV_CHECKPOINT}, and {ENV_MODEL_CFG} to enable it. The "
                "synthetic prototype never requires it."
            )
        checkpoint = os.environ.get(ENV_CHECKPOINT, "")
        model_cfg = os.environ.get(ENV_MODEL_CFG, "")
        if not checkpoint or not os.path.exists(checkpoint):
            raise RuntimeError(
                f"{ENV_CHECKPOINT} must point to an existing SAM2 checkpoint "
                f"(got {checkpoint!r})."
            )
        if not model_cfg:
            raise RuntimeError(f"{ENV_MODEL_CFG} must name a SAM2 model config.")
        try:
            import torch  # noqa: F401
            from sam2.build_sam import build_sam2_video_predictor
        except ImportError as e:
            raise RuntimeError(
                "Real-SAM2 path requires `pip install torch sam2` "
                "(https://github.com/facebookresearch/sam2)."
            ) from e
        self._predictor = build_sam2_video_predictor(model_cfg, checkpoint)

    def track(self, frames: np.ndarray, prompt_xy: Tuple[int, int]) -> List[np.ndarray]:
        """Prompt on frame 0 with a positive point, propagate through the clip,
        return one boolean mask per frame. Follows the sam2 video-predictor
        API; requires frames on disk as JPEGs (the format init_state expects).
        """
        import tempfile

        try:
            from PIL import Image
        except ImportError as e:
            raise RuntimeError("Real-SAM2 path requires `pip install pillow`.") from e

        import torch

        with tempfile.TemporaryDirectory() as tmp:
            for i, frame in enumerate(frames):
                Image.fromarray(frame).save(os.path.join(tmp, f"{i:05d}.jpg"))
            with torch.inference_mode():
                state = self._predictor.init_state(video_path=tmp)
                self._predictor.add_new_points_or_box(
                    inference_state=state,
                    frame_idx=0,
                    obj_id=1,
                    points=np.array([prompt_xy], dtype=np.float32),
                    labels=np.array([1], dtype=np.int32),
                )
                masks: List[np.ndarray] = [None] * len(frames)  # type: ignore[list-item]
                for frame_idx, _obj_ids, mask_logits in self._predictor.propagate_in_video(
                    state
                ):
                    masks[frame_idx] = (mask_logits[0, 0] > 0).cpu().numpy()
        return masks
