import numpy as np
import pytest

from a0028 import sam2_wrapper
from a0028.world import WorldParams, generate_trial


def test_disabled_by_default(monkeypatch):
    monkeypatch.delenv(sam2_wrapper.ENV_FLAG, raising=False)
    assert not sam2_wrapper.real_sam2_enabled()
    with pytest.raises(RuntimeError, match="disabled"):
        sam2_wrapper.RealSAM2Adapter()


def test_enabled_but_missing_checkpoint_fails_cleanly(monkeypatch):
    monkeypatch.setenv(sam2_wrapper.ENV_FLAG, "1")
    monkeypatch.delenv(sam2_wrapper.ENV_CHECKPOINT, raising=False)
    with pytest.raises(RuntimeError, match="checkpoint"):
        sam2_wrapper.RealSAM2Adapter()


def test_render_trial_frames_shapes_and_prompt():
    rng = np.random.default_rng(0)
    trial = generate_trial(
        "swap", 32.0, gap=2, similarity=0.8, rng=rng, world=WorldParams(n_prefix=3, n_post=2)
    )
    frames, prompt_xy = sam2_wrapper.render_trial_frames(trial, size=256)
    assert frames.shape == (len(trial.frames), 256, 256, 3)
    assert frames.dtype == np.uint8
    x, y = prompt_xy
    assert 0 <= x < 256 and 0 <= y < 256
    # the prompt pixel is on the rendered target disk (not background gray)
    assert not np.array_equal(frames[0, y, x], np.array([96, 96, 96], dtype=np.uint8))
