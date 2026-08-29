# Idea_01 — Roadmap

All budgets are **HYPOTHESIS** (estimates transcribed from
`selection_history/evolution_summary.md` and `experiments.md`). None is a
measured runtime. Windows6 has **zero ACTUAL RESULTS**.

Ordering principle: **cheapest kill first.** Every phase below is arranged so
that the experiment most likely to end the project is also the one that costs
least. Nothing expensive runs until the mechanism has been earned.

## Phase 0 — Harness validation (CPU, done in this package)

| | |
|---|---|
| **Work** | Card E0. `python Idea_01/src/run_smoke.py`, `python -m unittest discover -s Idea_01/tests` |
| **Cost** | CPU seconds. No GPU, no weights, no data |
| **Exit** | E0 gate PASS and 22 self-checks green |
| **Status** | **DONE.** Harness passes; it caught two defects (quantile-invariant AMG stand-in, and Hungarian IoU normalised by \|A\|) that would each have silently voided a hypothesis. See `experiments.md` E0 |

**What Phase 0 does not buy.** Nothing scientific. It only means the instrument
is not obviously broken.

## Phase 1 — Bring-up (first GPU session)

| | |
|---|---|
| **Work** | Wire `segmenters.sam_amg` to the real `SamAutomaticMaskGenerator`; wire `data.load_real_ct_slices` to nibabel/pydicom. Both currently raise `NotImplementedError` with instructions rather than returning fake output |
| **Also** | **Pre-register the 100-slice list and freeze it.** Do this before looking at any result |
| **Cost** | ≈1 GPU-h (**HYPOTHESIS**) |
| **Exit** | Real AMG runs end-to-end on 5 slices and the metric table populates |

## Phase 2 — E1 killer (H1)

| | |
|---|---|
| **Work** | Card E1: 100 slices, abdomen window, AMG vs k-means / multi-Otsu / GMM / SLIC, all three metrics |
| **Cost** | ≈2 GPU-h (**HYPOTHESIS**) |
| **Continue if** | Best intensity baseline beats SLIC on all three metrics, bootstrap CI excluding 0 |
| **Kill if** | SLIC ≥ every intensity baseline |
| **Flag if** | Metrics disagree — carry the flag into E2; H1 must hold on all three there or the claim is metric-dependent |

**This is the decision point for the whole project.** Do not start Phase 3
before it resolves.

## Phase 3 — E2 ‖ E3 (H3 and H2, in parallel)

These two cards **share no state and can run concurrently** on separate GPUs.
E3 is the scientifically decisive one; E2 is the one that protects it from
Reviewer #2's attack A1.

| Card | Work | Cost (**HYPOTHESIS**) | Branch |
|---|---|---|---|
| **E2** | 3 windows × 2 AMG settings × 3 k values, full grid reported | ≈8–20 GPU-h | ≥2/3 windows → continue · exactly 1 → **pivot** to a windowing-artifact paper · 0 → **kill** |
| **E3** | Intensity remap arm (γ ∈ {0.4,0.5,0.7,1.4}) and texture shuffle arm (tile ∈ {4,8,16}), both with enforced validity gates | ≈2–4 GPU-h | dissociation → mechanistic paper · \(s_{\mathrm{int}} \approx s_{\mathrm{tex}}\) → **downgrade** · \(s_{\mathrm{int}} > s_{\mathrm{tex}}\) → **kill**, report the negative · direction flips with tile size → **void**, redesign |

**Before E3 completes, resolve the standing severity conflict.** The Stage-4
record says a failed H2 means *"else evaluation note"* (downgrade); this
package's `reviewer_attacks.md` B1 says *do not submit* (withhold).
`stage6_battle.md` §4.4 logged it unresolved. It determines what happens on the
most likely branch, so it cannot be settled after the fact.

## Phase 4 — E4 specificity (H4)

| | |
|---|---|
| **Work** | Card E4: the identical protocol on a COCO subset |
| **Cost** | ≈2 GPU-h (**HYPOTHESIS**) |
| **Gate** | Runs **only after E3 succeeds.** There is no point controlling the specificity of an effect that has not earned its mechanism |
| **Kill if** | COCO reproduces the CT gap — the CT paper does not exist; at most a general note about AMG on single-channel images |

## Phase 5 — Optional strengthening

E5 (SAM2 generality, ≈4–8 GPU-h) and E6 (failure cases: metal, contrast,
low-dose, ≈1 GPU-h). Both **HYPOTHESIS**. Neither is on the critical path;
run them only if Phases 2–4 have produced a paper.

## Phase 6 — Paper & release

Short analysis paper. Release: code, configs, the pre-registered slice list,
per-slice metric CSVs. Derived metrics only — no patient imagery redistributed.

**Candidate titles.** *Is SAM AMG Just Intensity Clustering on CT?* ·
*Windowing, Superpixels, and the Objectness of Foundation Models* ·
*A Causal Test of SAM's CT Objectness*

## Budget summary

| Path | Total (**HYPOTHESIS**) |
|---|---|
| Kill at E1 | ≈3 GPU-h |
| Kill/downgrade at E3 | ≈15 GPU-h |
| Complete paper through E4 | ≈15–35 GPU-h |
| Outer bound of the full matrix | 40–80 GPU-h (`experiments.md`) |

The decision tree exists so the outer bound is never spent. Day-1 is ≈2 GPU-h,
the figure recorded in `evolution_summary.md` — again an estimate, not a
measurement.

## Standing rules

1. Cheapest kill first; nothing expensive before the mechanism is earned.
2. Pre-register before measuring — slice list, metrics, thresholds.
3. A failed validity gate produces no number at all.
4. Report all three metrics on every card, including the ones that disagree.
5. Budgets stay labelled **HYPOTHESIS** wherever they are quoted.

## Dependency graph

```
Phase 0 (E0, CPU, DONE)
   |
Phase 1 (bring-up + pre-register slice list)
   |
Phase 2 (E1 killer, H1) ---- kill ----> stop
   |
   +---------------+
   |               |
Phase 3a (E2, H3)  Phase 3b (E3, H2)  <-- parallel; E3 is the decisive one
   |               |
   +-------+-------+
           |
   Phase 4 (E4, H4) ---- COCO reproduces ----> kill CT-specificity
           |
   Phase 5 (E5/E6, optional)
           |
   Phase 6 (paper)
```
