import numpy as np
import torch

from vpt_registers.synthetic_data import DataConfig, generate_batch


def test_shapes_and_dtypes():
    cfg = DataConfig(image_size=16, patch_size=4, num_classes=3)
    b = generate_batch(cfg, 8, seed=0)
    assert b.images.shape == (8, 3, 16, 16)
    assert b.pixel_labels.shape == (8, 16, 16)
    assert b.patch_labels.shape == (8, 4, 4)
    assert b.images.dtype == torch.float32
    assert b.pixel_labels.dtype == torch.int64
    assert b.pixel_labels.min() >= 0
    assert b.pixel_labels.max() <= cfg.num_classes


def test_determinism_per_seed_and_split():
    cfg = DataConfig()
    a = generate_batch(cfg, 4, seed=7, split="train")
    b = generate_batch(cfg, 4, seed=7, split="train")
    assert torch.equal(a.images, b.images)
    assert torch.equal(a.pixel_labels, b.pixel_labels)
    c = generate_batch(cfg, 4, seed=7, split="val")
    assert not torch.equal(a.images, c.images)
    d = generate_batch(cfg, 4, seed=8, split="train")
    assert not torch.equal(a.images, d.images)


def test_paired_g_same_layout_different_illumination():
    cfg = DataConfig()
    b = generate_batch(cfg, 4, seed=3, paired_g=True)
    assert b.images_alt is not None and b.g_alt is not None
    # identical layouts => identical labels; different g => different pixels
    assert b.images_alt.shape == b.images.shape
    assert not torch.equal(b.g, b.g_alt)
    assert not torch.allclose(b.images, b.images_alt)


def test_global_nuisance_actually_moves_pixels():
    """The class identity must not be readable from raw color alone: the
    same class under different g must differ more than texture noise."""
    cfg = DataConfig(texture_noise=0.0, pixel_noise=0.0)
    b = generate_batch(cfg, 8, seed=1, paired_g=True)
    diff = (b.images - b.images_alt).abs().mean().item()
    assert diff > 0.05


def test_patch_majority_consistent_with_pixels():
    cfg = DataConfig(image_size=16, patch_size=4)
    b = generate_batch(cfg, 4, seed=2)
    p = cfg.patch_size
    for i in range(4):
        for y in range(4):
            for x in range(4):
                tile = b.pixel_labels[i, y * p : (y + 1) * p, x * p : (x + 1) * p]
                maj = np.bincount(tile.flatten().numpy()).argmax()
                assert b.patch_labels[i, y, x].item() == maj
