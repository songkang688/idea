# Idea_01 — Experiment cards

> **STATUS OF EVERY CARD BELOW: NOT RUN**, except E0, which runs on synthetic
> data and can only validate the harness. Windows6 has **zero ACTUAL RESULTS**.
> Every budget is **HYPOTHESIS**. Every predicted trend is **EXPECTED RESULT**.

## Epistemic labels used here

`EXPECTED` = pre-registered hypothesised trend. `ACTUAL` = a number produced by
running something on real data with real weights — **there are none**. Where a
card prints numbers today, they come from a synthetic phantom and a
threshold-connected-component stand-in, and the script says so at runtime.

## Card index and execution order

| Card | Name | Gate it decides | Budget (HYPOTHESIS) | Status |
|---|---|---|---|---|
| **E0** | Harness validation (synthetic, CPU) | Is the instrument usable? | ~0, CPU seconds | **RUN — harness PASS** |
| **E1** | **KILLER**: correlational arm, one window | H1 | ≈2 GPU-h | NOT RUN |
| **E2** | Window sweep × AMG grid | H3 | ≈8–20 GPU-h | NOT RUN |
| **E3** | **RESIDUAL**: intensity vs texture counterfactuals | H2 | ≈2–4 GPU-h | NOT RUN |
| **E4** | COCO specificity control | H4 | ≈2 GPU-h | NOT RUN |
| **E5** | SAM2 generality (optional) | scope | ≈4–8 GPU-h | NOT RUN |
| **E6** | Failure-case qualitative pass | presentation | ≈1 GPU-h | NOT RUN |

Order is E0 → E1 → E2 → E3 → E4, with E5/E6 optional. **E2 and E3 can run in
parallel** once E1 passes; they share no state. E4 must wait for E3, because
there is no point controlling the specificity of an effect that has not earned
its mechanism.

---

## E0 — Harness validation (synthetic, CPU) — STATUS: RUN, PASS

**Purpose.** Prove the instrument is not broken before spending a GPU-hour.
This card **cannot confirm the science**; it can only fail the harness.

**Input.** `data.synthetic_ct` — a piecewise-constant HU phantom (air / fat /
soft tissue / liver / bone plateaus) with additive texture, windowed through a
documented W/L pair. No real data, no weights.

**Run.**

```bash
python Idea_01/src/run_smoke.py --seed 0
python -m unittest discover -s Idea_01/tests
```

**Metrics.** All three pre-registered metrics (§ `proposal.md` 15) plus the two
cardinality diagnostics.

**Decision threshold (FACT, the original rule):** *"If even on synthetic blobs
AMG-mock does not beat SLIC, the **implementation** is wrong — fix before real
SAM."* Implemented literally: `run_smoke.py` exits non-zero when the intensity
baselines fail to beat `slic_lite` on all three metrics.

**Branch.** FAIL → fix the implementation. This is never a scientific
conclusion. PASS → proceed to E1.

**Two harness defects this card caught during W6-T3** (recorded because they
are exactly what E0 is for, and both would have silently voided a hypothesis):

1. **The AMG stand-in was thresholding at quantiles**, which are invariant to
   any monotone intensity remap. The H2 intensity arm therefore scored a perfect
   1.000 self-agreement *by construction* and could never have moved. Fixed by
   using absolute thresholds on the windowed image; guarded by
   `test_amg_mock_is_not_invariant_to_monotone_remap`.
2. **Hungarian IoU was normalised by |A|**, conflating match quality with the
   cardinality gap between a nested AMG inventory and a k-way partition. It
   reported ~0.03 agreement for structurally similar mask sets. Fixed by
   normalising over `min(|A|,|B|)` and reporting `cardinality_ratio` and
   `coverage_iou` separately.

**What E0 does NOT show.** Nothing about SAM, and nothing about H2 — the
stand-in fragments under per-pixel noise for reasons unrelated to objectness, so
its texture-arm behaviour is not informative. `run_smoke.py` prints this caveat
next to the numbers.

---

## E1 — KILLER: correlational arm, one window — STATUS: NOT RUN

**Purpose.** Decide H1 as cheaply as possible.

**Input.** **100** CT slices from TotalSegmentator or MSD
(`CITATION NEEDED — 待人工核验` for the dataset papers), soft-tissue/abdomen
window (W/L 400/40), slice list **pre-registered before the run**.

> **FACT on the sample size.** The record disagreed with itself: `README.md`
> and the original killer list said 50, the Stage-5 engineering block said 100.
> `stage6_battle.md` §4.7 logged the discrepancy and §6 resolved it by taking
> the larger figure. **100** is used everywhere in this package.

**Arms.** SAM ViT-B AMG (`points_per_side = 32`) versus k-means (k ∈ {8,16,32}),
multi-Otsu, GMM, and SLIC.

**Metrics.** Hungarian IoU, ARI, boundary-F @ ±2 px — all three, always — plus
`coverage_iou` and `cardinality_ratio` as diagnostics. Per-slice paired
comparison; bootstrap CI over slices.

**Decision thresholds.**

| Observation | Action |
|---|---|
| Best intensity baseline > SLIC on **all three** metrics, CI excluding 0 | **CONTINUE** to E2 and E3 |
| Mixed across metrics | **CONTINUE but flag**; H1 must hold on all three at E2 or the claim is metric-dependent |
| SLIC ≥ every intensity baseline | **KILL** the project |

**Budget.** ≈2 GPU-h (**HYPOTHESIS**, from `evolution_summary.md`).

**Failure mode to watch.** If AMG returns tens of masks per slice and the
clusterers return `k`, `cardinality_ratio` will be large. That is expected and
is reported, not corrected away.

---

## E2 — Window sweep × AMG grid — STATUS: NOT RUN

**Purpose.** Decide H3: is the E1 effect a property of CT, or of one
preprocessing choice? This is Reviewer #2's attack #1 and it is fatal if unmet.

**Input.** Same 100 slices. Windows: abdomen (400/40), bone (2000/400), lung
(1500/−600) or documented equivalents. AMG `points_per_side` ∈ {16, 32}.
k ∈ {8, 16, 32}.

**Metrics.** As E1, per cell. Report the **full** 3 × 2 × 3 grid; no cell is
omitted for space.

**Decision thresholds.**

| Observation | Action |
|---|---|
| H1 direction holds on ≥2 of 3 windows **and** ≥2 AMG settings | **CONTINUE** |
| Holds on exactly 1 window | **PIVOT** — the paper becomes "windowing manufactures apparent objectness", which is a real but different finding |
| Holds on 0 windows once the grid is honest | **KILL** |

**EXPECTED (not measured).** The gap narrows in the lung window, where
air/tissue contrast is so strong that most methods agree. A narrowed gap there
is not a failure; a *reversed* gap there is a warning.

**Budget.** ≈8–20 GPU-h (**HYPOTHESIS**).

---

## E3 — RESIDUAL: intensity vs texture counterfactuals — STATUS: NOT RUN

> **This card is Reviewer #2's binding residual obligation, verbatim from
> `stage4_reviewer2_cheap5.jsonl`:**
>
> > `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`
>
> Nothing else in this package discharges it. Without E3 the contribution is an
> evaluation note (and see the unresolved severity conflict below).

**Purpose.** Decide H2 — the double dissociation that turns correlation into
mechanism.

### Arm A — intensity remap (changes intensity, freezes edges)

1. Compute the Sobel gradient support of the windowed slice and **freeze it as
   a reference**, so edge displacement can be measured rather than assumed.
2. Apply a **strictly monotone** remap to HU inside tissue
   (`interventions.intensity_remap`, `gamma` swept over {0.4, 0.5, 0.7, 1.4}).
3. **Validity gate:** `check_remap_is_monotone` must pass. A non-monotone map
   can create or destroy edges and would confound the arm with the very thing
   it holds fixed. The code raises rather than returning a number.
4. Re-run AMG. Measure self-agreement against the un-intervened AMG mask set.

### Arm B — texture shuffle (changes texture, freezes local intensity)

1. Partition the slice into tiles (`shuffle_tile` swept over {4, 8, 16}).
2. Within each tile, permute the high-frequency residual while preserving the
   tile mean (`interventions.texture_shuffle`).
3. **Validity gate:** `check_shuffle_preserves_tile_means` must pass to 1e-9.
   This check is what licenses calling the arm "intensity-preserving"; without
   it, any AMG response could be an intensity response.
4. Re-run AMG. Measure self-agreement against the un-intervened AMG mask set.

### Read-out

Let \(s_{\mathrm{int}}\) and \(s_{\mathrm{tex}}\) be the two self-agreements
(1.0 = the intervention changed nothing).

| Observation | Interpretation | Action |
|---|---|---|
| \(s_{\mathrm{int}} \ll s_{\mathrm{tex}}\), holds on ≥2 windows and ≥2 AMG settings | AMG tracks intensity, ignores texture | **CONTINUE** — mechanistic paper |
| \(s_{\mathrm{int}} \approx s_{\mathrm{tex}}\) | No dissociation | **DOWNGRADE** to evaluation note — see below |
| \(s_{\mathrm{int}} > s_{\mathrm{tex}}\) | AMG tracks texture, not intensity | **KILL** the hypothesis; report the negative result |
| Direction flips with `shuffle_tile` | The arm measures tile size, not texture | **No result**; redesign the instrument |
| Either validity gate fails | Broken instrument | **No result**; fix, do not report |

**Also binding (Stage-5 gate, FACT):** **STOP** if AMG turns out closer to
ground truth than to k-means **and** the texture shuffle moves AMG a lot. That
combination says AMG is doing anatomy, and the hypothesis is simply wrong.

**Unresolved before writing (FACT, `stage6_battle.md` §4.4).** The Stage-4
record says a failed H2 means *"else evaluation note"* (downgrade); this
package's own `reviewer_attacks.md` says *"If we cannot run the causal arm, do
not submit"* (withhold). No artifact says which governs. **Settle it before
writing, not during.**

**Budget.** ≈2–4 GPU-h (**HYPOTHESIS**).

---

## E4 — COCO specificity control — STATUS: NOT RUN

**Purpose.** Decide H4. Reviewer #2 pre-emption recorded in the Stage-5
engineering block: *"same protocol on COCO; clustering equivalence must be
**CT-specific**."*

**Input.** A COCO subset (`CITATION NEEDED — 待人工核验`), converted to
single-channel intensity so the protocol is identical rather than merely
analogous.

**Metrics.** Identical to E1.

**Decision thresholds.**

| Observation | Action |
|---|---|
| COCO gap much smaller than the CT gap | **CONTINUE** — the effect is CT-specific |
| COCO reproduces the CT gap | **KILL the CT-specificity claim.** At most a general note about AMG on single-channel images; the CT paper does not exist |

**Why this matters more than it looks.** Without E4, a reviewer can say the
result is about grayscale images in general. That objection would land after
acceptance-critical time has been spent, so E4 is cheap insurance.

**Budget.** ≈2 GPU-h (**HYPOTHESIS**).

---

## E5 — SAM2 generality (optional) — STATUS: NOT RUN

Repeat E1 and E3 with SAM2. **CONTINUE** framing as "foundation segmenters" only
if both models show the dissociation; otherwise scope the claim to SAM ViT-B
explicitly and say so in the title. Related evaluation context:
arXiv 2408.11210 (**VERIFIED PRIOR WORK**). Budget ≈4–8 GPU-h (**HYPOTHESIS**).

## E6 — Failure-case qualitative pass — STATUS: NOT RUN

Metal artifacts, contrast-enhanced studies, very low-dose slices. Not
hypothesis-bearing; it exists so the paper shows where the equivalence breaks
rather than only where it holds. Budget ≈1 GPU-h (**HYPOTHESIS**).

---

## Cross-cutting rules

1. **Pre-register the slice list** before E1. Selecting slices after seeing
   results converts every subsequent card into confirmation.
2. **All three metrics, every card.** No card may report a subset.
3. **A failed validity gate produces no number.** `counterfactual_profile`
   raises rather than returning; this is deliberate.
4. **Budgets are HYPOTHESIS.** The `~2 GPU-h` figure comes from
   `evolution_summary.md` and is an estimate, never a measurement.
5. **No card may relabel EXPECTED as ACTUAL.** A number becomes ACTUAL only
   when produced by real weights on real data, and no such number exists yet.
