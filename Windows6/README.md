# Windows6 — Autonomous Research Idea Evolution

- **Windows ID:** Windows6
- **Created:** 2026-08-28 (UTC)
- **Supervisor:** Windows6
- **Branch:** `cursor/windows6-research-idea-evolution-b55d`
- **Status:** Provisional Final 3 packaged; Stage 5/6 still confirming against DE-top10 assassin + auditor.

## This round’s three Ideas (provisional)

| # | Folder | Idea | Recommendation |
|---|--------|------|----------------|
| 1 | `Idea_01/` | SAM AMG ≈ HU clustering on CT (mechanistic + counterfactuals) | **#1 start here** — cheapest, falsifiable, no huge pretrain |
| 2 | `Idea_02/` | Camera-ID vs event-disjoint leakage on smoke/fire | Strong audit paper if two datasets |
| 3 | `Idea_03/` | Alignment tax on localization (format-controlled + probe) | Highest impact, highest concurrent-work risk |

## Most recommended

**Idea_01.** Reviewer #2 attacks all have cheap shut-up experiments; CPU prototype exists; does not depend on rare checkpoint triples.

## Next experiment

Run `Idea_01/src/amg_intensity_equiv.py`, then 50 real CT slices with SAM AMG vs k-means/SLIC (see `Idea_01/experiments.md`).

## Project status

| Idea | Status |
|------|--------|
| Idea_01 | Package + synthetic prototype; **no real SAM numbers** |
| Idea_02 | Package + synthetic split probe; **no smoke mAP** |
| Idea_03 | Package + format-vs-probe demo; **no VLM eval** |

Stage 1: 1080 raw / 1062 live. Stage 2: 78+64 scored. Stage 3–4: prior-work + Reviewer #2 on cheap cluster.
