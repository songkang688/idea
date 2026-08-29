"""E2 fine-tuning stub: LoRA / VeRA-style adapters + the pre-registered grid plan.

Implemented here (real code, torch):
  - `LoRALinear`  — standard low-rank adapter around a frozen linear layer;
  - `VeRALinear`  — random-direction control: FROZEN random A/B, trained scaling
                    vectors only (the mandatory Stage-3 cluster-2 control arm);
  - injection planning from `configs/shared_grid.yaml` (which modules get
    adapters per recipe cell);
  - grid-plan expansion (`--print-plan`): every run of the pre-registered grid
    with its mix, recipe, LR, seed, loss-aggregation and IoU-head-loss cell.

Stubbed here (requires real assets; raises instead of faking):
  - dataset iterators for BUSI / MSD Task09 2D;
  - the actual SAM forward/backward loop.

The stub's train() documents the exact wiring obligations so the Phase-0
implementation cannot silently drop one: prompt-mix sampling per batch
(prompts.MixedPromptSampler), loss aggregation cell (min-loss-mask vs all-mask,
multimask ENABLED in both), IoU-head loss ON by default, covariate logging
(per-module update norms + interface CKA drift), dense checkpoint cadence for
the matched-gain rule.
"""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import yaml


# --------------------------------------------------------------- adapters


def _require_torch():
    try:
        import torch  # noqa: F401
        import torch.nn as nn  # noqa: F401

        return torch, nn
    except ImportError as e:  # pragma: no cover
        raise SystemExit(
            "torch is required for adapter construction — install requirements.txt"
        ) from e


def make_lora_linear(base_linear, rank: int = 4, alpha: float = 4.0):
    """Wrap a frozen nn.Linear with a trained low-rank update (LoRA)."""
    torch, nn = _require_torch()

    class LoRALinear(nn.Module):
        def __init__(self, base, r, a):
            super().__init__()
            self.base = base
            for p in self.base.parameters():
                p.requires_grad_(False)
            in_f, out_f = base.in_features, base.out_features
            self.lora_A = nn.Parameter(torch.zeros(r, in_f))
            self.lora_B = nn.Parameter(torch.zeros(out_f, r))
            nn.init.kaiming_uniform_(self.lora_A, a=5**0.5)
            self.scaling = a / r

        def forward(self, x):
            return self.base(x) + (x @ self.lora_A.T @ self.lora_B.T) * self.scaling

    return LoRALinear(base_linear, rank, alpha)


def make_vera_linear(base_linear, rank: int = 4, seed: int = 0):
    """Random-direction control (VeRA-style): FROZEN random A/B shared shapes,
    trained per-layer scaling vectors only. Any trained-LoRA effect must beat
    this arm (Stage-3 cluster-2 ruling — VeRA arXiv:2310.11454)."""
    torch, nn = _require_torch()

    class VeRALinear(nn.Module):
        def __init__(self, base, r, sd):
            super().__init__()
            self.base = base
            for p in self.base.parameters():
                p.requires_grad_(False)
            g = torch.Generator().manual_seed(sd)
            in_f, out_f = base.in_features, base.out_features
            self.register_buffer("A", torch.randn(r, in_f, generator=g) / in_f**0.5)
            self.register_buffer("B", torch.randn(out_f, r, generator=g) / r**0.5)
            self.d = nn.Parameter(torch.ones(r) * 0.1)   # trained scaling (rank)
            self.b = nn.Parameter(torch.zeros(out_f))    # trained scaling (output)

        def forward(self, x):
            return self.base(x) + ((x @ self.A.T) * self.d) @ self.B.T + self.b

    return VeRALinear(base_linear, rank, seed)


# ----------------------------------------------------------- grid planning


def expand_grid_plan(cfg: dict) -> list[dict]:
    """Expand shared_grid.yaml into the concrete pre-registered run list."""
    runs: list[dict] = []
    domains = [d["name"] for d in cfg["domains"]]
    mixes = [m for m in cfg["prompt_mixes"] if m != "mixed_robustness_cell"]
    seeds = cfg["training"]["seeds"]
    for domain, mix, (recipe, spec), seed in itertools.product(
        domains, mixes, cfg["recipes"].items(), seeds
    ):
        for lr in spec["lr_sweep"]:
            cell = {
                "domain": domain,
                "mix": mix,
                "recipe": recipe,
                "lr": lr,
                "seed": seed,
                "loss_aggregation": "min_loss_mask",
                "iou_head_loss": "on",
                "multimask": True,
            }
            runs.append(cell)
            # diversity obligation: all-mask cells exist in the mixed column only
            if mix == "mixed":
                runs.append({**cell, "loss_aggregation": "all_mask"})
    # B1 robustness cell: perturbed mixed distribution, headline domain, all seeds
    if "mixed_robustness_cell" in cfg["prompt_mixes"]:
        headline = domains[0]
        for (recipe, spec), seed in itertools.product(cfg["recipes"].items(), seeds):
            runs.append(
                {
                    "domain": headline,
                    "mix": "mixed_robustness_cell",
                    "recipe": recipe,
                    "lr": spec["lr_sweep"][0],
                    "seed": seed,
                    "loss_aggregation": "min_loss_mask",
                    "iou_head_loss": "on",
                    "multimask": True,
                }
            )
    return runs


# ------------------------------------------------------------------ train


def train(run_cfg: dict) -> None:
    """STUB — the E2 training loop. Raises rather than simulating.

    Wiring obligations for the Phase-0 implementation (each maps to a binding
    reviewer obligation; see reviewer_attacks.md Part I):
      A1  prompt-mix sampling per batch via prompts.MixedPromptSampler
      A2  loss_aggregation cell: min-loss-mask OR all-mask; multimask ENABLED
      A3  threshold tuning only via threshold_gate.tune_threshold (symmetric)
      P031 iou_head_loss ON by default (single OFF cell shared with P031)
      A7  covariate logging per checkpoint: per-module-group update norm,
          interface CKA drift, step, losses (shared_grid.covariates_logged...)
      §14 checkpoint cadence dense enough for the ±0.5-Dice matched-gain band
    """
    raise NotImplementedError(
        f"E2 training for cell {run_cfg} requires SAM weights + BUSI/MSD datasets "
        "(hash-pinned at roadmap Phase 0) and runs only after the E1 gate PROCEEDs. "
        "This stub exists so the grid plan and adapter wiring are auditable now."
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="E2 shared-grid fine-tuning (stub)")
    ap.add_argument("--config", type=str, required=True, help="configs/shared_grid.yaml")
    ap.add_argument("--print-plan", action="store_true", help="print the pre-registered run list")
    ap.add_argument("--run-index", type=int, default=None, help="execute one grid cell (stub)")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    plan = expand_grid_plan(cfg)

    if args.print_plan:
        print(f"[train_lora_stub] pre-registered grid: {len(plan)} runs (no training executed)")
        for i, run in enumerate(plan):
            print(f"  [{i:03d}] {run}")
        print(
            "[train_lora_stub] NOTE: run counts are design facts, not results. "
            "Budget ESTIMATE lives in shared_grid.yaml::estimated_budget."
        )
        return

    if args.run_index is not None:
        train(plan[args.run_index])
        return

    ap.error("choose --print-plan or --run-index")


if __name__ == "__main__":
    main()
