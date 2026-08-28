# Research Ledger — Supervisor Windows3

- **Supervisor identity:** Windows3
- **Repo:** `github.com/songkang688/idea`
- **Supervisor branch:** `cursor/idea-evolution-windows3-b534`
- **Date (UTC):** 2026-08-28
- **Current stage:** Stage 1 — Massive Idea Exploration (in flight)
- **Archival Windows folder:** TBD after inventory. Local `origin/main` has no `Windows*` directories; numbering will be `Windows{N+1}` at archival time and must not overwrite existing folders.

## Agent slots (max 3)

| Slot | Role | bcId | Cluster | Status |
|------|------|------|---------|--------|
| 1 | Stage 1 Cluster A: VFM / SAM / PEFT / VLM-dense | `bc-071184c9-32ca-5a84-817c-596774d344b0` | A | RUNNING |
| 2 | Stage 1 Cluster B: Medical / smoke / detection / shift | `bc-3e891857-0ea0-5e08-8f04-856627cc7ea7` | B | RUNNING |
| 3 | Stage 1 Cluster C: Synthetic / eval / surprising / adjacent | `bc-e28d0acc-fe06-5489-8e75-70774038e7d6` | C | RUNNING |

## Idea ID plan

- Cluster A: `W3-S1-0001`–`W3-S1-0360`
- Cluster B: `W3-S1-0361`–`W3-S1-0720`
- Cluster C: `W3-S1-0721`–`W3-S1-1080`
- Target pool size: **≥1000** raw ideas

## Pipeline (do not skip)

1. 1000+ ideas
2. 1000 → 200 (independent review, protect high-risk / cheap-falsify)
3. 200 → 50 (adversarial prior-work kill)
4. 50 → 20 (Reviewer #2; only keep if a real experiment can shut them up)
5. 20 → 5 (experimental engineering + killer experiment)
6. 5 → 3 (group battle; no fake consensus)
7. Final 3 full research packages
8. Git archival into new `WindowsN/` + commit + push + verify

## Checkpoint 2026-08-28T16:23Z

All 3 Stage 1 children still **RUNNING**. No branch, no diff, no dashboard events, `lastMessageActivity` still equals spawn time. Treat as in-flight, not failed. Do not open extra cloud slots (max 3).

Peer Windows runs on this repo (do not overwrite their folders): Windows2/4/6/8 branches exist; `origin/main` still only `README.md`.

## Stage 2 review rubric (queued; do not start until ≥1000 ideas exist)

Score independently (do not rank by mean):
Novelty, Significance, Scientific Question, Technical Soundness, Feasibility, Compute, Dataset Availability, Baseline Availability, Likelihood Already Published, Experimental Clarity, Venue potential, Risk, Upside, ROI.

Protect: high-risk/high-upside; simple counter-intuitive; high reviewer disagreement; cheap-to-falsify.

## Top candidates

_Empty until Stage 1 returns._

## Unresolved

- Stage 1 children have not produced files yet.
- Archival Windows number still TBD from latest `origin/main` inventory.
