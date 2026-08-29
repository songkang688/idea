# Idea_03 — Day-1 Access Checklist

**Status: TEMPLATE. Nothing below has been confirmed.**

## Compute

| Item | Status |
|---|---|
| 8×A100-80GB allocation, ~2,450 A100-h core budget | ☐ |
| Queue policy allows 12-hour runs | ☐ |
| Storage for 15 checkpoints + base | ☐ |

`KNOWN FACT` One full LLaVA-1.5-7B fine-tune ≈100 A100-h. If the allocation cannot absorb 800 A100-h
before a go/no-go, this project should not start.

## Repositories (pin by commit, not branch)

| Repo | Role | Cloned | Commit | Smoke test |
|---|---|---|---|---|
| `haotian-liu/LLaVA` | training harness | ☐ | | ☐ |
| `TRI-ML/prismatic-vlms` | fallback + E5 cross-family | ☐ | | ☐ |
| `EleutherAI/lm-evaluation-harness` | language strata | ☐ | | ☐ |
| `EvolvingLMMs-Lab/lmms-eval` | VL sanity strata | ☐ | | ☐ |

`KNOWN FACT` The LLaVA repo is in maintenance mode. Pin `transformers` and `deepspeed` explicitly;
the shipped configs assume versions that no longer install cleanly. Budget days, not weeks.

## Data and weights

| Item | Licence | Status |
|---|---|---|
| `llava_v1_5_mix665k` | mixed; ShareGPT provenance is scraped and legally murky | ☐ |
| LLaVA-1.5 projector weights | — | ☐ |
| Vicuna-7B | LLaMA-2 community licence, research use | ☐ |
| `allenai/c4` | ODC-BY | ☐ |
| Curated instruction text for `A1` | as above | ☐ |

The ShareGPT provenance issue is mitigated incidentally: we **strip** that slice from the base, which
reduces exposure. The published-recipe reference run still uses it, and a careful reviewer will note
that; the mitigation is disclosure, not avoidance.

## Measurements that must happen at E0

| Measurement | Why it cannot wait | Done |
|---|---|---|
| Exact token count of the ShareGPT slice | sets every arm's token budget | ☐ |
| Base-model score on every stratum | fixes every retention denominator | ☐ |
| Seed σ on the base evals | half of the P0 threshold | ☐ |
| Declared MDE | must precede the six E1 runs | ☐ |

## Freeze checklist — all before any arm runs

| Item | Committed |
|---|---|
| `configs/preregistration.yaml` fully populated | ☐ |
| Eval YAMLs pinned and committed | ☐ |
| Primary matching convention recorded (per-layer) | ☐ |
| MDE recorded | ☐ |
| Strata list final after the denominator gate | ☐ |

Freeze date: ______  Committed by: ______

## Gates

| Gate | Passed | Date |
|---|---|---|
| E0 reproduces LLaVA-1.5 within noise | ☐ | |
| Denominator gate applied; failing strata replaced | ☐ | |
| E0b `A3` produces a usable gradient | ☐ | |
| **E1 / P0 power gate** | ☐ | |
