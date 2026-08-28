# Windows2 Research Summary (live ledger)

## Pipeline

1000+ ideas → 200 → 50 → 20 → 5 → 3 executable research packages.

## Current stage

**Stage 1 COMPLETE by count.** Original pool: **1042** ideas (A 352 + B 345 + C 345). Global 1000→200 cut waits for independent scores from D (C), E (B), F (A).

| Agent | Focus | Status | Count |
| --- | --- | --- | --- |
| A | SAM / medical / ambiguous-object segmentation | COMPLETE | 352 (`W2-A-0001`–`0352`) |
| B | VFM / VLM / PEFT / forgetting | COMPLETE | 345 (`W2-B-0001`–`0345`) |
| C | Detection / evaluation / unproven assumptions | COMPLETE | 345 (`W2-C-0001`–`0345`) |
| D | Review + prior-work on C | RUNNING | — |
| E | Review + prior-work on B | RUNNING | — |
| F | Review + prior-work on A | DISPATCHING | — |

## Shared scientific pattern (supervisor, pre-review)

All three generators independently skewed toward **measurement / audit / mechanism** ideas rather than new modules. That is desirable. Main risk: overlap with 2023–2026 analysis papers, and venue fit ("not a method paper").

Cross-batch threads to merge after D/E/F:
- Prompt/label sensitivity: A point-jitter; B synonym/open-vocab; C prompt-template vs architecture
- Annotation noise as ranking confounder: A seed-churn / boundary rasterization; C AP noise bands / missing FP tax
- Foundation-model priors: A SA-1B compact-region prior + contamination; B DINO artifacts / PEFT invariance; C SAM domain atlas
- Frozen vs adapted shift: B shift budget; C pretrain≠dense; A UDA rank-correlation across novel shifts

## Provisional watchlist

See evolution_summary.md. Not Stage-2 survivors until D/E/F return.

## Git safety

Owns **Windows2/** only.
