"""E3 orchestrator: the prompt-type evaluation matrix (P065 battery).

Rows    = checkpoints (matched-gain manifest from E2 + the frozen floor)
Columns = battery protocols {box, one_click, iterative_5, multimask_ambiguity}
          × retention suites × {primary, alternative} click simulator

Implemented here: matrix construction, run-artifact enforcement, CSV/parquet
output, and the honest `--dry-run` mode that emits the full skeleton with NaN
placeholders (the package's no-fake-metrics contract).

Stubbed here (requires real assets pinned at roadmap Phase 0): model loading and
forward passes, dataset iterators. `ModelAdapter` documents the exact interface
a real backend must implement; a `segment_anything`-based adapter is the Phase-0
first coding task.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Protocol

import numpy as np
import pandas as pd
import yaml

BATTERY_COLUMNS = ("box", "one_click", "iterative_5", "multimask_ambiguity")
SIMULATORS = ("error_centroid_protocol", "uniform_interior")


# ------------------------------------------------------------ run artifacts


@dataclass(frozen=True)
class RunArtifact:
    """Provenance stamp without which no number may be reported (proposal §27)."""

    config_hash: str
    seed: int
    commit: str

    @staticmethod
    def create(config_path: Path, seed: int) -> "RunArtifact":
        cfg_hash = hashlib.sha256(config_path.read_bytes()).hexdigest()[:16]
        try:
            commit = subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"], text=True
            ).strip()
        except Exception:
            commit = "UNKNOWN"
        return RunArtifact(config_hash=cfg_hash, seed=seed, commit=commit)


# ------------------------------------------------------------ model interface


class ModelAdapter(Protocol):
    """Interface a real promptable-segmenter backend must implement."""

    def predict_soft(
        self,
        image: np.ndarray,
        boxes: Optional[np.ndarray],
        points: Optional[np.ndarray],
        point_labels: Optional[np.ndarray],
        multimask: bool,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Return (soft_masks [K,H,W], iou_head_scores [K])."""
        ...


def load_checkpoint_adapter(path: str) -> ModelAdapter:
    """STUB: build a segment_anything-based adapter for a real checkpoint.

    Deliberately unimplemented in the Stage-7 prototype: implementing it is the
    first coding task of roadmap Phase 0, after assets are hash-pinned. Raising
    here (instead of returning mock outputs) is what enforces the
    no-fake-metrics contract at the code level.
    """
    raise NotImplementedError(
        f"load_checkpoint_adapter({path!r}): real SAM weights + segment_anything required. "
        "Pin assets at roadmap Phase 0, then implement the adapter against ModelAdapter. "
        "Use --dry-run for the NaN skeleton meanwhile."
    )


# ------------------------------------------------------------ matrix skeleton


def build_matrix_skeleton(cfg: dict) -> pd.DataFrame:
    """Full pre-registered result matrix with NaN metric placeholders."""
    suites = [s if isinstance(s, str) else next(iter(s)) for s in cfg["retention_suites"]]
    checkpoints = ["frozen_sam_vit_b", "<matched_gain_manifest_rows>"]
    rows = []
    for ckpt, suite, column, sim in itertools.product(
        checkpoints, suites, BATTERY_COLUMNS, SIMULATORS
    ):
        if column in ("box", "multimask_ambiguity") and sim != SIMULATORS[0]:
            continue  # simulator axis applies to click-based columns only
        rows.append(
            {
                "checkpoint": ckpt,
                "retention_suite": suite,
                "battery_column": column,
                "click_simulator": sim if column in ("one_click", "iterative_5") else "n/a",
                "tuned_threshold": np.nan,
                "dice": np.nan,
                "miou": np.nan,
                "dice_at_click_curve": "" if column == "iterative_5" else "n/a",
                "oracle_best_of_3": np.nan if column == "multimask_ambiguity" else None,
                "argmax_iou": np.nan if column == "multimask_ambiguity" else None,
                "oracle_argmax_gap": np.nan if column == "multimask_ambiguity" else None,
                "n_images": 0,
                "config_hash": "",
                "seed": "",
                "commit": "",
                "epistemic_status": "PLACEHOLDER — NO RUN ARTIFACT",
            }
        )
    return pd.DataFrame(rows)


# ------------------------------------------------------------------- CLI


def main() -> None:
    ap = argparse.ArgumentParser(description="P065 prompt-type evaluation matrix (E3)")
    ap.add_argument("--config", type=str, required=True, help="configs/p065_eval_battery.yaml")
    ap.add_argument("--dry-run", action="store_true", help="emit NaN skeleton (no models needed)")
    ap.add_argument("--out", type=str, default="battery_matrix.csv")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())

    if args.dry_run:
        df = build_matrix_skeleton(cfg)
        out = Path(args.out)
        df.to_csv(out, index=False)
        print(f"[eval_prompt_matrix] DRY RUN: wrote {len(df)}-row skeleton to {out}")
        print(
            "[eval_prompt_matrix] Every metric cell is NaN by design: values may only be "
            "filled by real runs carrying a RunArtifact {config_hash, seed, commit}."
        )
        return

    # Real mode: enforce the artifact, then fail honestly until Phase 0 lands.
    artifact = RunArtifact.create(Path(args.config), seed=0)
    print(f"[eval_prompt_matrix] run artifact: {artifact}")
    raise SystemExit(
        "Real battery runs require: (1) hash-pinned checkpoints + datasets (roadmap Phase 0), "
        "(2) an implemented load_checkpoint_adapter, (3) the matched-gain manifest from E2. "
        "None may be faked. Use --dry-run for the skeleton."
    )


if __name__ == "__main__":
    main()
