# Windows6 research summary

## Pipeline actually executed

**FACT.** The intended ladder was `1000→200→50→20→5→3`. Windows6 did not run it. What ran:

| Rung | Standard | Windows6 actual |
|---|---|---|
| Raw pool | 1000+ | **1080 raw / 1062 live** (S-series 600 + A–F 480) |
| → 200 | 200 | **≈142** scored survivors (78 ABCF + 64 DE, out of 480 reviewed) |
| → 50 | 50 | *never produced* |
| → 20 | 20 | *never produced* |
| → 5 | 20 → 5 | 10 DE verdicts ‖ 12 cheap-cluster verdicts → **cheap-5** |
| → 3 | 5 → 3 | Reviewer #2 → **3 survive** |

Two deviations must not be glossed: **there was no 200-band, no 50-band and no true 20-band**, and the **600 S-series ideas were never Stage-2 scored** — 55% of the raw pool never entered scoring. Wave-1 timeouts interrupted the funnel and it was closed out through a narrow "cheap" channel. Full deviation table with line-item verification: [`selection_history/stage5_top5.md`](selection_history/stage5_top5.md) §1.

## Final 3 — **PROVISIONAL, not locked**

Adjudication and lock verdict: [`selection_history/stage6_battle.md`](selection_history/stage6_battle.md). Three gates are open — **GATE-A** (camera metadata on a public smoke set unverified), **GATE-B** (no base/chat checkpoint pair verified to share vision encoder and coordinate tokenization), **GATE-C** (the survivors were never ranked against the parked extensions `D-008`/`D-060`/`E-025` on a common scale). **GATE-D** (status coherence + package depth) was closed by W6-T3.

The three (see `Idea_01`–`Idea_03`):

1. SAM AMG as intensity clustering (mechanistic)
2. Smoke/fire camera-ID leakage quantification
3. VLM alignment tax on localization (mutated, format+probe)

Killed after Reviewer #2: empty-slice FPR–Dice “uncorrelation” audit; atlas-centroid vs CLIP text substitution.

All quantitative claims in packages are **EXPECTED/HYPOTHESIS** unless labeled otherwise. Prototypes are synthetic. **ACTUAL RESULT count for the whole round: zero.** W6-T3 thickened the three packages to executable depth and made each `src/` runnable with smoke tests; it produced no measurements, and every script prints a synthetic-output banner before its numbers.
