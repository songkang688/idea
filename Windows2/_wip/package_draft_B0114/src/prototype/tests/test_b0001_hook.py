"""Tests for the quarantined B-0001 hook — including the dissociation
guarantees (the hook must be import-isolated from the B-0114 metrics)."""

import ast
from pathlib import Path

import numpy as np

from vpt_registers.b0001_hook import auroc, norm_error_auroc
from vpt_registers.train import pretrain_backbone, train_arm

SRC = Path(__file__).parent.parent / "src" / "vpt_registers"


def test_auroc_perfect_and_chance_and_inverted():
    scores = np.array([0.9, 0.8, 0.7, 0.2, 0.1])
    labels = np.array([1, 1, 1, 0, 0])
    assert auroc(scores, labels) == 1.0
    assert auroc(scores, 1 - labels) == 0.0
    rng = np.random.default_rng(0)
    s = rng.uniform(size=4000)
    l = rng.integers(0, 2, size=4000)
    assert abs(auroc(s, l) - 0.5) < 0.05


def test_auroc_degenerate_labels_nan():
    assert np.isnan(auroc(np.array([1.0, 2.0]), np.array([1, 1])))


def test_hook_runs_on_an_arm(tiny_cfg, seed_data):
    bb = pretrain_backbone(tiny_cfg, "register_free", seed=0, data=seed_data)
    res = train_arm(tiny_cfg, bb, "register_free", "no_token", seed=0, data=seed_data)
    out = norm_error_auroc(bb, res.head, res.tokens, res.prompt_is_sink, seed_data.val, tiny_cfg)
    assert 0.0 <= out["norm_error_auroc"] <= 1.0 or np.isnan(out["norm_error_auroc"])
    assert 0.0 <= out["patch_error_rate"] <= 1.0
    assert out["n_patches"] > 0


def _imports_of(module_path: Path) -> set[str]:
    tree = ast.parse(module_path.read_text())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def test_dissociation_no_b0114_module_imports_the_hook():
    """PI-binding guard: B-0114's own metrics/signatures/training/runner
    must not depend on the B-0001 hook module."""
    for mod in ("metrics.py", "signatures.py", "train.py", "tiny_vit.py", "config.py"):
        imports = _imports_of(SRC / mod)
        assert not any("b0001" in n for n in imports), f"{mod} imports the B-0001 hook"


def test_hook_is_flag_gated_in_runner():
    runner = (Path(__file__).parent.parent / "run_synthetic.py").read_text()
    tree = ast.parse(runner)
    # b0001 imports must only appear inside function bodies guarded by the
    # CLI flag, never at module top level
    top_level_imports = {
        n.module
        for n in tree.body
        if isinstance(n, ast.ImportFrom) and n.module
    } | {a.name for n in tree.body if isinstance(n, ast.Import) for a in n.names}
    assert not any("b0001" in (m or "") for m in top_level_imports)
    assert "--with-b0001-hook" in runner
