# Windows6 — Autonomous Research Idea Evolution

- **Windows ID:** Windows6
- **Created:** 2026-08-28 (UTC)
- **Supervisor:** Windows6
- **Branch:** `cursor/windows6-research-idea-evolution-b55d`
- **Status:** Stages 1–6 recorded. Final 3 are **PROVISIONAL — not locked.** Adjudication and the lock verdict are in [`selection_history/stage6_battle.md`](selection_history/stage6_battle.md).

### What is still missing before the Final 3 can be locked

Three gates from `stage6_battle.md` §5 are open. None needs a GPU; all are hours of desk work.

| Gate | What must be true | Fails if |
|------|-------------------|----------|
| **GATE-A** | Camera metadata confirmed to exist on ≥1 public smoke/fire set, with a camera **count** | <10 cameras forces the event-disjoint-only pivot and forfeits H2; no metadata at all **kills Idea_02** by its own stop rule |
| **GATE-B** | One base/chat checkpoint pair verified to share vision encoder **and** coordinate tokenization, license usable | Idea_03's stage-isolation claim is unavailable; it descopes to a format-artifact study |
| **GATE-C** | The three survivors ranked against `D-008` / `D-060` / `E-025` on one common rubric | Without it the round can only claim "these three survived the one channel that ran", not "these three beat the field" |

**GATE-D (status coherence + package depth) was closed by W6-T3** — see [`selection_history/status_reconciliation.md`](selection_history/status_reconciliation.md).

When A, B and C close, the Final 3 may be declared **LOCKED** and this line updated. Until then, no downstream document should cite Windows6 as having a locked Final 3.

## This round’s three Ideas (provisional — see gates above)

| # | Folder | Idea | Recommendation |
|---|--------|------|----------------|
| 1 | `Idea_01/` | SAM AMG ≈ HU clustering on CT (mechanistic + counterfactuals) | **#1 start here** — cheapest, falsifiable, no huge pretrain |
| 2 | `Idea_02/` | Camera-ID vs event-disjoint leakage on smoke/fire | Strong audit paper if two datasets |
| 3 | `Idea_03/` | Alignment tax on localization (format-controlled + probe) | Highest impact, highest concurrent-work risk |

## Most recommended

**Idea_01.** Reviewer #2 attacks all have cheap shut-up experiments; CPU prototype exists; does not depend on rare checkpoint triples.

## Next experiment

Run `Idea_01/src/amg_intensity_equiv.py` (CPU, synthetic, seconds), then **100 real CT slices** with SAM AMG vs k-means / multi-Otsu / GMM / SLIC (see `Idea_01/experiments.md`, cards E0 → E1 → E2).

This line previously said *50* slices. `Idea_01/experiments.md` gave both 50 (killer list) and 100 (Stage-5 engineering block); `stage6_battle.md` §4.7 logged the discrepancy and §6 resolved it by taking the larger figure. **100** is now used consistently.

## Project status

| Idea | Status |
|------|--------|
| Idea_01 | Executable-depth package + synthetic prototype + smoke tests; **no real SAM numbers** |
| Idea_02 | Executable-depth package + synthetic split probe + smoke tests; **no smoke mAP** |
| Idea_03 | Executable-depth package + format-vs-probe demo + smoke tests; **no VLM eval** |

W6-T3 thickened the documentation and made each `src/` runnable. **It produced no measurements.** Every number printed by any script in this round is synthetic and is labelled as such at runtime. There are **zero ACTUAL RESULTS** in Windows6.

## Funnel actually executed (not the standard ladder)

The policy in `selection_history/supervisor_log.md` is `1000→200→50→20→5→3`. That is **not** what ran:

`1080 raw / 1062 live` → **≈142 scored survivors** (78 ABCF + 64 DE) → Stage-3 ran as two unmerged branches (10 DE verdicts ‖ 12 cheap-cluster verdicts) → **cheap-5** → Reviewer #2 → **3 survive**.

There was **no 200-band, no 50-band and no true 20-band**, and the 600 S-series ideas were never Stage-2 scored. Full deviation table: [`selection_history/stage5_top5.md`](selection_history/stage5_top5.md) §1.
