# Idea_02 — Roadmap

All budgets are **HYPOTHESIS** (estimates from
`selection_history/evolution_summary.md` and `experiments.md`). None is a
measured runtime. **No detector has been trained**; Windows6 has no smoke mAP.

Ordering principle: **the free check that can kill the project runs first.**
Idea_02 is the most expensive member of the Final 3 per unit of evidence — the
only one requiring training — and its existence depends on a dataset property
nobody has verified.

## Phase 0 — GATE-A: camera inventory (no GPU, hours) — **BLOCKING**

| | |
|---|---|
| **Work** | Card E-A. Inventory camera IDs on PYRONEAR-2025 / FIgLib: do they exist, how many cameras, how many events per camera, are there empty frames on both sides |
| **Cost** | Hours of desk work. **No GPU** |
| **Status** | **NOT RUN. This is GATE-A from `stage6_battle.md` §5, and it is why the Final 3 remain PROVISIONAL** |
| **Branch** | ≥10 cameras → Phase 1 · 1–9 cameras → **pivot** to event-disjoint only, forfeiting H2, and re-argue the Final-3 slot · no metadata → **KILL** by Idea_02's own stop rule |

**Do not skip to Phase 2 "just to see".** A ≈10 GPU-h run on a corpus without
camera IDs produces nothing, and the check costs an afternoon.

## Phase 1 — Harness validation (CPU, done in this package)

| | |
|---|---|
| **Work** | Card E0. `python Idea_02/src/run_smoke.py`, `python -m unittest discover -s Idea_02/tests` |
| **Cost** | CPU seconds |
| **Exit** | Split structure gate PASS and 24 self-checks green |
| **Status** | **DONE.** It caught two protocol defects — a random-split camera probe that was really measuring event memorisation, and an empty-frame comparison with no seen-camera side. Both would have produced publishable-looking but wrong results. See `experiments.md` E0 |

## Phase 2 — Bring-up (first GPU session)

| | |
|---|---|
| **Work** | Wire `data.load_real_corpus` to the real corpus and `detector.train_real_detector` to YOLOv8n. Both currently raise `NotImplementedError` with instructions rather than returning fake output. Build and **freeze** the three splits; publish the overlap counts before training anything |
| **Cost** | ≈2 GPU-h (**HYPOTHESIS**) |
| **Exit** | The three protocols reproduce the E0 overlap structure **on real data**. If event-disjoint comes out camera-disjoint on this corpus, H2 is unfalsifiable here — stop and reconsider the dataset |

## Phase 3 — E1 killer ‖ E3 probe control

These run **in parallel**: E3 needs only a frozen ImageNet backbone, no detector
training, so it costs almost nothing and pre-empts an obvious question.

| Card | Work | Cost (**HYPOTHESIS**) | Branch |
|---|---|---|---|
| **E1** | 1 seed × 3 protocols + camera probe (event-disjoint) + empty-frame FPR | ≈10 GPU-h | event-disjoint ≈ camera-disjoint → **KILL** · probe at chance → **KILL H3** · no empty-frame gap → **fatal to the framing** |
| **E3** | Same probe on an ImageNet backbone never trained on smoke | ≈1 GPU-h | detector ≫ ImageNet → strong reading · both high → H3 weakens to "information is available", report honestly · both at chance → **KILL H3** |

**E1 is the decision point.** Do not start Phase 4 before it resolves.

## Phase 4 — E2 three seeds and honest CIs

| | |
|---|---|
| **Work** | Repeat E1 with 3 seeds; bootstrap CIs resampled over **events** |
| **Cost** | ≈30 GPU-h (**HYPOTHESIS**) |
| **Continue if** | H1 and H2 gaps survive with CIs excluding 0 |
| **Stop if** | Gaps inside seed noise **and** probe ≈ chance **and** no empty-FPR gap — confirm with 2 further seeds before declaring |
| **If CIs are wide** | Add seeds before adding claims |

## Phase 5 — E4 dedup rerun (the confound that could take the paper)

| | |
|---|---|
| **Work** | pHash dedup, rebuild all splits, rerun E1 |
| **Cost** | ≈10 GPU-h (**HYPOTHESIS**) |
| **Branch** | Gap survives → camera signature, strongest form of the result · gap disappears → **downgrade** to a near-duplicate audit, which restates the Voxel51 blog with numbers · gap shrinks → report both and attribute the share |

Pre-committing these branches matters: after seeing a shrunken gap it is very
tempting to describe it as "partially explained by duplicates" and move on.

## Phase 6 — E5 second dataset

≈30 GPU-h (**HYPOTHESIS**). `proposal.md` §20 requires H1 and H4 on ≥2 datasets
to CONTINUE. Each new corpus needs its own GATE-A inventory first. If only one
corpus has camera IDs, the title names it — honest scope over implied
generality.

## Phase 7 — Paper & release

Dataset-audit paper. **The camera-aware re-split indices are the deliverable**,
alongside the probe and empty-frame protocol as reusable code. Camera IDs are
released as opaque indices, never coordinates; no imagery is redistributed.

**Candidate titles.** *Event-Disjoint Is Not Camera-Disjoint: Measuring Smoke
Benchmark Inflation* · *What Do Wildfire Detectors Memorize — Plumes or
Towers?* · *A Camera-Aware Re-split of Public Smoke Benchmarks*

## Budget summary

| Path | Total (**HYPOTHESIS**) |
|---|---|
| Kill at GATE-A | **0 GPU-h** |
| Kill at E1 | ≈13 GPU-h |
| Through E2 | ≈43 GPU-h |
| Full program with dedup and a second dataset | ≈83 GPU-h |

Day-1 is ≈10 GPU-h, the figure recorded in `evolution_summary.md` — an
estimate, not a measurement.

## Standing rules

1. **GATE-A before any GPU.**
2. Freeze and publish the splits, with overlap counts, before training.
3. The camera probe is always evaluated event-disjoint.
4. Empty frames are never trained on.
5. CIs cluster over events, never frames.
6. Never cite an inflation number we did not compute.
7. Budgets stay labelled **HYPOTHESIS** wherever quoted.

## Dependency graph

```
Phase 0 (GATE-A inventory, no GPU)  --no camera IDs--> KILL
   |                                --<10 cameras---> PIVOT (H2 forfeited)
   |>=10 cameras
Phase 1 (E0 harness, CPU, DONE)
   |
Phase 2 (bring-up; verify overlap structure on REAL data)
   |
   +---------------------+
   |                     |
Phase 3a (E1 killer)     Phase 3b (E3 probe control)   <-- parallel
   |                     |
   +----------+----------+
              |
      Phase 4 (E2, 3 seeds + CIs) --inside seed noise--> STOP
              |
      Phase 5 (E4 dedup) --gap is all duplicates--> DOWNGRADE
              |
      Phase 6 (E5 second dataset)
              |
      Phase 7 (paper + re-split release)
```
