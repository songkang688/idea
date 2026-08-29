# PromptAmnesia prototype (`src/promptamnesia/`)

**Status: PROTOTYPE.** This code implements the package's *logic* (protocols, rules, decompositions) so
that the pre-registered procedures are executable and auditable. It contains **no experimental results and
generates no fake metrics**: paths that need model weights or datasets either require real assets or run
in `--dry-run` / `--print-plan` / `--self-test` modes whose outputs are explicitly labeled placeholders or
synthetic self-tests.

## Module map

| Module | Implements | Status |
|---|---|---|
| `prompts.py` | Box-jitter, point placement, iterative click protocol with negative clicks, mixed-prompt sampler (E2/E3 protocols) | fully implemented (numpy) |
| `matched_gain.py` | The single pre-registered matched-gain rule (proposal §14) | fully implemented |
| `threshold_gate.py` | Threshold sweep, symmetric tuning, P082 noise-floor envelope, gate decision (E1) | fully implemented (runs on real eval records; `--self-test` uses labeled synthetic data) |
| `diversity.py` | Oracle best-of-3 vs IoU-head argmax decomposition (E4, C1-061) | fully implemented |
| `eval_prompt_matrix.py` | Battery orchestration + result-matrix skeleton (E3) | orchestration implemented; model/data loading stubbed (`--dry-run` emits NaN skeleton) |
| `train_lora_stub.py` | LoRA/VeRA-style adapters, injection plan from `shared_grid.yaml`, prompt-mix + loss-aggregation wiring (E2) | adapter math + plan implemented; training loop is a stub (needs SAM + datasets) |
| `splice.py` | Module partition, both-direction swap, α-interpolation, capacity-capped stitch (E5, P177) | state-dict logic implemented; stitch fitting requires real checkpoints |
| `metrics.py` | Dice / IoU on binary masks | fully implemented |

## Quick start

```bash
# from Windows4/Idea_02/
pip install -r requirements.txt
cd src

# 1) P082 gate machinery self-test (synthetic data, labeled as such)
python -m promptamnesia.threshold_gate --config ../configs/p082_gate.yaml --self-test

# 2) Battery skeleton (NaN placeholders — the "no fake metrics" contract)
python -m promptamnesia.eval_prompt_matrix --config ../configs/p065_eval_battery.yaml --dry-run

# 3) Print the pre-registered fine-tuning grid plan (no training happens)
python -m promptamnesia.train_lora_stub --config ../configs/shared_grid.yaml --print-plan
```

## What is intentionally NOT here

- No dataset downloads, no checkpoint weights (hash-pinned at roadmap Phase 0).
- No result files: real runs must write artifacts carrying `{config_hash, seed, commit}`, enforced by
  `eval_prompt_matrix.RunArtifact`.
- No statistics beyond the pre-registered ones (contrast family O1–O5 lives in the config, not in code
  constants, so the freeze governs it).
