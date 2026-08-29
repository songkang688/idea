import numpy as np
import torch

from vpt_registers.metrics import (
    aggregate,
    confusion_matrix,
    decomposition,
    h2_gap,
    miou_from_confusion,
)
from vpt_registers.train import ArmResult


def _res(arm, backbone, seed, miou):
    return ArmResult(
        arm=arm, backbone=backbone, seed=seed, miou=miou, pixel_acc=0.5,
        tokens=None, head=None, prompt_is_sink=False,
    )


def test_confusion_and_miou_perfect():
    pred = torch.tensor([[0, 1], [2, 1]])
    cm = confusion_matrix(pred, pred, num_labels=3)
    assert cm.diag().sum() == 4
    assert miou_from_confusion(cm) == 1.0


def test_miou_ignores_absent_classes():
    pred = torch.tensor([0, 0, 1, 1])
    target = torch.tensor([0, 0, 1, 1])
    cm = confusion_matrix(pred, target, num_labels=5)
    assert miou_from_confusion(cm) == 1.0  # classes 2..4 absent -> excluded


def test_decomposition_telescopes():
    """insertion + content_transfer + co_adaptation must equal total gain,
    seed-wise, by construction."""
    rng = np.random.default_rng(0)
    results = []
    for seed in range(3):
        vals = dict(zip(
            ["no_token", "frozen_random", "learned_frozen", "learned"],
            sorted(rng.uniform(0.2, 0.8, size=4)),
        ))
        for arm, v in vals.items():
            results.append(_res(arm, "register_free", seed, v))
    agg = aggregate(results)
    d = decomposition(agg["register_free"])
    for i in range(3):
        total = d["total_vpt_gain"][2][i]
        parts = (
            d["insertion"][2][i]
            + d["content_transfer"][2][i]
            + d["co_adaptation"][2][i]
        )
        assert abs(total - parts) < 1e-9


def test_h2_gap_direction():
    results = []
    for seed in range(2):
        results += [
            _res("no_token", "register_free", seed, 0.30),
            _res("learned", "register_free", seed, 0.50),  # gain 0.20
            _res("no_token", "register_equipped", seed, 0.40),
            _res("learned", "register_equipped", seed, 0.45),  # gain 0.05
        ]
    h2 = h2_gap(aggregate(results))
    assert h2["direction_confirmed"]
    assert abs(h2["gap"][0] - 0.15) < 1e-9


def test_h2_gap_none_when_backbone_missing():
    results = [
        _res("no_token", "register_free", 0, 0.3),
        _res("learned", "register_free", 0, 0.5),
    ]
    assert h2_gap(aggregate(results)) is None
