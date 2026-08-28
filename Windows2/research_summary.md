# Windows2 Research Summary (live ledger)

## Pipeline

1000+ ideas → 200 → 50 → 20 → 5 → 3 executable research packages.

## Current stage

**Stage 1 closed (1042 ideas).** Stage 2 per-batch: **D and E complete.** F (batch A) still running. Global 1000→200 waits for F, then merge.

| Agent | Focus | Status | Result |
| --- | --- | --- | --- |
| A | SAM / medical / ambiguous seg | COMPLETE | 352 ideas |
| B | VFM / PEFT / VLM | COMPLETE | 345 ideas |
| C | Detection / eval science | COMPLETE | 345 ideas |
| D | Review + prior-work on C | COMPLETE | keep 107 (79+28) / mutate 58 / kill 180; mandatory-15: 7 survive / 8 mutate / 0 kill |
| E | Review + prior-work on B | COMPLETE | keep 77 / kill 268; mandatory-15: 6 survive / 7 mutate / 2 kill |
| F | Review + prior-work on A | RUNNING | — |
| G | Cross-batch B∪C merge + feasibility census | RUNNING | — |
| H | Reviewer #2 + freshness sweep on B top bets | DISPATCHING | — |

Provisional keep pool before A: **184** (107 C + 77 B), too fat and eval-skewed. D recommends capping C eval-audits at ~60% of C's contribution to the 200.

## Supervisor belief updates (EVIDENCE from D/E, not final ranking)

- **Eval-science family (C) is scientifically sharp but venue-fragile.** Many top C ideas share one infrastructure assumption: public per-instance predictions. That is now the #1 feasibility uncertainty.
- **B is more "method-adjacent mechanism" than C.** Strongest cheap bets: VPT-as-registers (0114), register-norm uncertainty (0001), modality-gap collapse dynamics (0074), PEFT invariance ceiling (0104).
- **Hard kills already (do not revive without new evidence):** B-0136 (forgetting=rotation; Davari CVPR'22), B-0175 (RClicks), B-0279 (DINOv3 medical benchmark).
- **C had zero hard kills on its flagship 15** — novelty lives in *mutations* (COCO-ReM, tinyBenchmarks, BoB, Hosang NMS, Elephant in the Room). Treat mutated forms as the candidates.
- **Portfolio bias:** both reviewers warn correlated bets (C: cached-pred audits; B: "upgrade correlation to causal/dynamics").

## Cross-batch collisions to resolve in G

- Prompt variance: B-0042 (mutated synonym ledger) ↔ C-0011 (OVD prompt vs architecture)
- Shift/transfer: B-0226 (shift budget) ↔ C-0081 (mutated within-family BoB)
- Contamination: B-0268 ↔ C benchmark-copy hashing (0298)
- Seed variance: B-0033 ↔ C-0136

## Git safety

Owns **Windows2/** only.
