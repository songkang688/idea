"""Smoke test: the runnable entry point executes end-to-end on both configs."""

import json
from pathlib import Path

import run_synthetic

ROOT = Path(run_synthetic.__file__).resolve().parent


def test_run_synthetic_quick_default(tmp_path, capsys):
    out_json = tmp_path / "res.json"
    levels = run_synthetic.main(
        [
            "--config", str(ROOT / "configs" / "default.yaml"),
            "--quick",
            "--json", str(out_json),
        ]
    )
    captured = capsys.readouterr().out
    assert "SYNTHETIC" in captured
    assert "EXPECTED vs MEASURED" in captured
    assert set(levels) == {"sparse", "medium", "crowded"}
    for blob in levels.values():
        assert len(blob["results"]) == 4
        for res in blob["results"]:
            assert 0.0 <= res.coverage <= 1.0
    payload = json.loads(out_json.read_text())
    assert payload["disclaimer"].startswith("SYNTHETIC")
    assert set(payload["levels"]) == {"sparse", "medium", "crowded"}


def test_run_synthetic_quick_crowded_aggressive(capsys):
    levels = run_synthetic.main(
        [
            "--config", str(ROOT / "configs" / "crowded_aggressive.yaml"),
            "--quick",
        ]
    )
    out = capsys.readouterr().out
    assert "SYNTHETIC" in out
    assert set(levels) == {"crowded", "very_crowded"}
