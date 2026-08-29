# Idea_01 — Is SAM AMG intensity clustering on CT? (Windows6 / F-067)

> **Epistemic status of this entire document.** No experiment in it has been
> run. Every quantity is **HYPOTHESIS** or **EXPECTED RESULT**. Windows6 has
> produced **zero ACTUAL RESULTS**; `Windows6/README.md` records *"no real SAM
> numbers"*. Citations are **VERIFIED PRIOR WORK** only where they already
> appear in `selection_history/literature_anchors.md` or `literature.md`;
> anything else is marked `CITATION NEEDED — 待人工核验`.

## 1. Title & identifiers

| Field | Value |
|---|---|
| Working title | *Is SAM's Automatic Mask Generation Just Intensity Clustering on CT?* |
| Windows6 ID | `Idea_01` |
| Stage-1 origin | `F-067` (`stage1_pool/F_001_080.jsonl`, seed `amg`, mutation `cheaper`) |
| Stage-3 record | `sam-amg-intensity-clustering`, `continue: keep`, `novelty_confidence: 0.6` |
| Stage-4 record | `AMG-HU-clustering`, `continue: survive`, `advance: true` |
| Auditor | protected keep (`auditor_overlay.md`) |
| Selection status | Final 3, **PROVISIONAL** — see `selection_history/stage6_battle.md` §5 |
| Paper type | analysis / short — **not** a new decoder |

## 2. One-sentence claim

**HYPOTHESIS.** On windowed CT, the mask inventory SAM's Automatic Mask
Generation (AMG) returns is approximately a clustering of Hounsfield-unit
intensity, and this can be established causally rather than correlationally by
showing AMG tracks intensity-only interventions while ignoring
intensity-preserving texture interventions.

## 3. Abstract

**HYPOTHESIS, not measured.** Foundation promptable segmenters are routinely
used as automatic proposal generators on CT. Prior evaluations show SAM/SAM2
are sensitive to windowing and weak on low-contrast CT (**VERIFIED PRIOR
WORK**, arXiv 2408.04212, arXiv 2408.11210). That observation is *consistent
with* — but does not establish — the stronger claim that AMG's mask inventory
is approximately equivalent to clustering in HU (or windowed 8-bit) space. We
specify a pre-registered equivalence test plus the causal counterfactuals
Reviewer #2 made binding: edge-preserving intensity remaps versus
intensity-preserving texture randomisation. The paper's contribution is the
**counterfactual**, not the correlation. **No experimental numbers are
claimed.**

## 4. Background & motivation

AMG is used as if it produced semantic object proposals. On natural images that
framing is at least arguable. On CT it may be closer to a threshold: CT is a
calibrated single-channel modality whose "objects" are largely defined by HU
plateaus after a window/level map, and a segmenter with no anatomical prior may
have nothing to go on but those plateaus.

If the equivalence holds, three consequences follow (**SPECULATION** — these are
the stakes, not findings):

1. Papers using AMG as semantic pseudo-labels on CT are injecting intensity
   superpixels and calling them objectness.
2. MedSAM-style adaptation may be fighting the wrong failure — improving a
   decoder whose CT behaviour is dominated by the input histogram.
3. A one-line classical baseline (k-means on HU) belongs in every SAM-on-CT
   table, and its absence is a reviewing failure.

**Why now.** The cheap-killer pass (`stage3_prior_work_kill_cheap.jsonl`) put
novelty confidence at **0.6** — the highest in Windows6 — with remaining
novelty *"Mechanistic AMG vs HU k-means equivalence on CT not found"*.

## 5. Problem statement & research questions

Let \(I\) be a CT slice in HU and \(W\) a documented window/level map. AMG
produces a mask inventory \(\mathcal{M}_{\mathrm{AMG}}\) over \(W(I)\). An
intensity clusterer \(C\) (k-means, multi-Otsu, GMM) produces
\(\mathcal{M}_C\); a spatial/texture superpixel method \(S\) (SLIC) produces
\(\mathcal{M}_S\).

- **RQ1 (correlational).** Is \(\mathcal{M}_{\mathrm{AMG}}\) closer to
  \(\mathcal{M}_C\) than to \(\mathcal{M}_S\)?
- **RQ2 (causal).** Does \(\mathcal{M}_{\mathrm{AMG}}\) *track* intensity-only
  interventions and ignore texture-only interventions?
- **RQ3 (scope).** Is any RQ1 effect stable across windows and AMG
  hyperparameters, or manufactured by one preprocessing choice?
- **RQ4 (specificity).** Is the effect CT-specific, or does the same
  equivalence appear on natural images, in which case it says nothing about CT?

## 6. Hypotheses (pre-registered)

- **H1.** After a fixed clinical window, matched mean
  IoU(\(\mathcal{M}_{\mathrm{AMG}}, \mathcal{M}_{k\text{-means}}\)) >
  IoU(\(\mathcal{M}_{\mathrm{AMG}}, \mathcal{M}_{\mathrm{SLIC}}\)) on a
  pre-registered CT subset, on **all three** metrics of §15.
- **H2 (causal).** An edge-preserving intensity remap changes AMG **more** than
  an intensity-preserving texture shuffle with the same edge map.
- **H3 (scope).** The H1 gap holds across an AMG hyperparameter grid and ≥2 of
  3 windows. If it holds on exactly one window, the finding is a **setting
  artifact** → pivot or kill.
- **H4 (specificity, Reviewer #2 pre-emption).** The H1 gap is **absent or much
  smaller** on COCO under the identical protocol. If COCO reproduces it, the
  claim is about AMG in general, not about CT, and the paper loses its subject.

## 7. Key insight

Windowing is a **monotone intensity map**. A monotone map cannot create or
destroy edge *locations*, but it does redistribute contrast — so if the study
runs one window, "AMG ≈ clustering" can be manufactured by preprocessing alone.
That is the whole reason H2 exists.

The complementary insight is the design of the two arms. Correlation between
AMG and k-means is cheap to obtain and cheap to dismiss. What is not cheap to
dismiss is a **double dissociation**: one intervention that changes intensity
while freezing edges, and one that changes texture while freezing local mean
intensity. If AMG follows the first and ignores the second, "AMG is reading
intensity" stops being an interpretation and becomes a measurement.

## 8. Novelty statement

**VERIFIED PRIOR WORK.** The closest works *evaluate* SAM on CT — Dice against
organs, window sensitivity, prompt sensitivity (arXiv 2408.11210, arXiv
2408.04212). `literature_anchors.md` files the SAM2 CT evaluation explicitly
under *"Remaining-novelty targets"* precisely because it is a black-box
evaluation and **not** an AMG-versus-clustering test.

**Gap (FACT, quoted from `literature.md`):** *"no AMG vs k-means Hungarian/ARI
study with texture-vs-intensity counterfactuals."*

The novelty is therefore not "SAM is bad on CT" — that is known and this paper
must not claim it. The novelty is **mechanism plus pre-registered multi-metric
agreement plus a causal instrument**.

## 9. Relation to prior work (differentiation)

| Prior work | Status | What it establishes | Why it does not pre-empt us |
|---|---|---|---|
| Segment Anything, ICCV 2023 | **VERIFIED PRIOR WORK** | Defines AMG | Defines the object of study; makes no claim about CT mechanism |
| SAM2 CT review, arXiv 2408.11210 | **VERIFIED PRIOR WORK** | Black-box CT evaluation | Reports *that* performance varies, not *what* AMG is computing |
| SAM/SAM2 low-contrast CT, arXiv 2408.04212 | **VERIFIED PRIOR WORK** | Intensity/window dependence | This is our strongest adjacency. It shows sensitivity to intensity; it does not test equivalence to a clusterer, and runs no texture control |
| HQ-SAM, NeurIPS 2023, arXiv 2306.01567 | **VERIFIED PRIOR WORK** | Mask-quality refinement | Used in Stage 3 to kill the adjacent `F-012` filter claim. `literature.md` records the standing constraint: *"we do not claim filter=HQ"* |
| SAMRefiner, arXiv 2502.06756 | **VERIFIED PRIOR WORK** | Mask refinement | Same family as above; refinement, not mechanism |
| MedSAM CT notes, arXiv 2408.03322 | **VERIFIED PRIOR WORK** | Benchmark context | Cited by Reviewer #2 as context |
| Metrics Reloaded, Nature Methods 2024 | **VERIFIED PRIOR WORK** | Metric-selection guidance | Constrains *our* metric choice; it killed the sibling idea `F-022`, and we must not repeat that mistake by reporting a definitional property |
| SLIC superpixels | `CITATION NEEDED — 待人工核验` | Spatial superpixels | Our texture/spatial control |
| Multi-Otsu, GMM, k-means, ARI, Hungarian matching | `CITATION NEEDED — 待人工核验` | Classical baselines and metrics | Standard tooling; formal citations must be verified before submission |

## 10. Significance — who is wrong if we are right

- **If H1 + H2 hold:** every paper treating AMG output on CT as semantic
  proposals owes a k-means baseline. Reviewers gain a one-line check.
- **If H1 holds but H2 fails:** the honest output is an **evaluation note**
  (§20) — agreement without mechanism. This is the outcome Reviewer #2's
  residual explicitly anticipated.
- **If H1 fails:** AMG on CT is doing something beyond intensity, which is a
  more interesting positive result than the one we set out to find, and worth
  reporting as a negative result against our own hypothesis.

Note the payoff asymmetry honestly: the "AMG is clustering" direction is the
one many reviewers already half-believe, so it must be delivered causally or it
reads as confirmation of folklore.

## 11. Method overview

1. Window \(I\) with a documented W/L pair. Three clinical windows.
2. Run AMG over a hyperparameter grid.
3. Run the intensity clusterers and the spatial control.
4. Compute all three agreement metrics plus the two cardinality diagnostics
   (§15) for every (AMG setting × baseline × window) cell.
5. Apply both interventions, re-run AMG, measure self-agreement.
6. Repeat the whole protocol on COCO as the specificity control.

Implementation: `src/amgclust/`. `pipeline.agreement_profile` answers H1 and
`pipeline.counterfactual_profile` answers H2. Neither returns a verdict —
thresholds live in `experiments.md` and are applied by the caller, so no
threshold can be quietly tuned inside the analysis code.

## 12. Interventions (the causal instruments)

| Arm | Changes | Holds fixed | Validity check (must pass or the arm is not evidence) |
|---|---|---|---|
| **Intensity remap** | HU values, via a strictly monotone map | Edge locations (Sobel support) | `check_remap_is_monotone` — pixel-value order preserved |
| **Texture shuffle** | High-frequency residual inside each tile | Per-tile mean intensity | `check_shuffle_preserves_tile_means` — tile means equal to 1e-9 |

**Why monotonicity is load-bearing.** A non-monotone remap could create or
destroy edges, confounding the intensity arm with the edge structure it is
supposed to hold constant. `intensity_remap` raises on `gamma <= 0` rather than
silently producing a non-monotone map.

**Why mean-preservation is load-bearing.** If the texture arm changed local HU
level, any AMG response would be attributable to intensity, and the
dissociation would collapse. The tile-mean check is what licenses the phrase
"intensity-preserving".

`pipeline.counterfactual_profile` raises `RuntimeError` when either check fails.
A broken instrument produces no number at all, rather than a number that looks
publishable.

## 13. Null models & baselines

| Role | Method | Purpose |
|---|---|---|
| Intensity clusterer | k-means on scalar HU, k ∈ {8,16,32} | The hypothesis' positive control |
| Intensity clusterer | multi-Otsu | Threshold-family control; guards against "k-means is special" |
| Intensity clusterer | 1-D GMM | Soft-assignment control |
| Spatial / texture | SLIC | **The discriminative baseline.** Clustering must beat *superpixels*, not just beat chance |
| Specificity | The whole protocol on COCO | H4 |
| Sanity | Synthetic piecewise-constant phantom | Card E0; can only fail the harness |

**Reviewer #2's third attack is answered here:** "k-means is one of many cheap
baselines" — so Otsu, GMM and SLIC all run, and clustering must beat
superpixels rather than merely correlate with AMG.

## 14. Datasets

| Data | Role | Status |
|---|---|---|
| TotalSegmentator or MSD CT slices, n = 100 | Primary | Named in `experiments.md`. `CITATION NEEDED — 待人工核验` for the dataset papers |
| COCO subset | H4 specificity control | `CITATION NEEDED — 待人工核验` |
| Synthetic phantom (`data.synthetic_ct`) | Harness validation only | Ships in this package |

**FACT.** The `n` was inconsistent in the record: `README.md` and the killer
list said 50, the Stage-5 engineering block said 100. `stage6_battle.md` §4.7
logged it and §6 resolved it to **100**. This package uses 100 throughout.

No patient data is redistributed; only public dataset identifiers and derived
metrics.

## 15. Metrics & statistical analysis

**Pre-registered, all three reported always.** Reporting the flattering subset
is the metric-shopping attack (`reviewer_attacks.md` A4), so the code has no
"best metric" helper and `run_smoke.py` prints all three verdicts side by side.

| Metric | What it is sensitive to |
|---|---|
| **Hungarian IoU** | Optimal one-to-one match quality between mask sets |
| **ARI** on pixel label maps | Partition agreement, chance-corrected |
| **Boundary-F** at ±2 px | Contour placement rather than region overlap |

Plus two **diagnostics** that are reported but not hypothesis-bearing:

- **`coverage_iou`** — the directional \((1/|A|)\sum_A \max_B \mathrm{IoU}\)
  formula from `references/math.md`. Asks "is every AMG mask explained by
  *some* cluster?".
- **`cardinality_ratio`** — \(|A|/|B|\).

**Why the normalisation changed (W6-T3, and it matters).** Hungarian IoU is
normalised by \(\min(|A|,|B|)\), not \(|A|\). AMG returns a nested inventory of
tens of masks while a clusterer returns a partition of \(k\); dividing by
\(|A|\) would mostly measure the cardinality gap and would report near-zero
agreement even for a perfect subset match. Cardinality *is* a real difference —
which is why it is reported explicitly rather than folded silently into the
agreement number.

**Statistics.** Per-slice paired comparison (each slice sees every baseline),
bootstrap CI over slices, and the H1 verdict requires the same sign on all
three metrics. **No p-value is pre-registered as a threshold**; the decision
rules in §20 are effect-direction rules across conditions, which is harder to
game than a single significance test.

## 16. Killer experiment (run first)

`experiments.md` card **E1**. 100 CT slices, soft-tissue window, SAM ViT-B AMG
versus k-means / multi-Otsu / GMM / SLIC, all three metrics. Budget **≈2 GPU-h
(HYPOTHESIS**, transcribed from `evolution_summary.md`; not a measurement).

It is the killer because it is cheap, needs no training, needs no rare
checkpoint, and its failure mode (§20) ends the project rather than prompting a
patch.

## 17. Full experimental program

| Card | Content | Budget (HYPOTHESIS) |
|---|---|---|
| E0 | Synthetic harness validation, CPU | ~0 |
| E1 | Killer: correlational arm, one window | ≈2 GPU-h |
| E2 | Window sweep × AMG grid (H3) | ≈8–20 GPU-h |
| E3 | **Counterfactual arms (H2)** | ≈2–4 GPU-h |
| E4 | COCO specificity control (H4) | ≈2 GPU-h |
| E5 | SAM2 generality (optional) | ≈4–8 GPU-h |
| E6 | Failure-case qualitative pass (metal, contrast) | ≈1 GPU-h |

**FACT.** `experiments.md` records the full matrix as *"~40–80 GPU-h (windows ×
SAM variants × counterfactuals)"*. That is the outer bound; the decision tree
in §28 is designed so most of it is never spent.

## 18. Ablations & controls

- **Window ablation:** 3 clinical windows — this *is* H3, not a nicety.
- **k ablation:** k ∈ {8,16,32}; the H1 gap must not depend on a lucky k.
- **AMG grid:** `points_per_side` ∈ {16,32}.
- **Metric ablation:** all three metrics, always.
- **Cardinality control:** report `|A|/|B|` so nobody can claim the agreement is
  a counting artifact.
- **Instrument ablation:** vary `remap_gamma` and `shuffle_tile`; if the H2
  direction flips with tile size, the texture arm is measuring tile size.
- **Domain control:** COCO (H4).

## 19. Expected results (all EXPECTED RESULT — nothing measured)

- **EXPECTED.** On the primary window, Hungarian IoU and ARI rank the intensity
  clusterers above SLIC; boundary-F is the least discriminative of the three
  because both families place edges at high-gradient locations.
- **EXPECTED.** The gap narrows in the lung window, where air/tissue contrast
  makes almost any method agree.
- **EXPECTED.** The H2 dissociation, if real, is smaller than the H1 gap —
  causal effects usually are — so E3 needs more slices than E1, not fewer.
- **SPECULATION.** COCO shows a much weaker gap. If it does not, see §20.

None of these has been observed. The synthetic run in `run_smoke.py` is a
harness check and its numbers carry no evidential weight.

## 20. Falsifiability & kill conditions

| Trigger | Action |
|---|---|
| SLIC ≥ k-means agreement on **all** windows | **KILL** |
| Texture shuffle moves AMG about as much as the intensity remap | **KILL the mechanistic claim** → §20.1 |
| H1 holds on exactly 1 of 3 windows | **PIVOT** — report as a windowing artifact |
| AMG closer to ground truth than to k-means **and** texture shuffle moves AMG a lot | **KILL** (Stage-5 gate) |
| COCO reproduces the equivalence | **KILL the CT-specificity claim**; at most a general AMG note |
| An arm fails its validity check | **No result**; fix the instrument, do not report |

### 20.1 The downgrade path, and a conflict the record has not resolved

**FACT.** Reviewer #2's residual reads, verbatim: *"Must earn mechanistic via
intensity vs texture counterfactuals; **else evaluation note**"* — a downgrade.

**FACT.** `reviewer_attacks.md` in this package reads: *"If we cannot run the
causal arm, **do not submit**."* — a withhold.

These are different instructions for the same contingency and no artifact says
which governs. `stage6_battle.md` §4.4 logged the conflict as unresolved.
**It must be settled before writing, not during.** The two readings differ on
whether a failed H2 yields a shorter paper or no paper.

## 21. Confounders & mitigations

| Confounder | Mitigation |
|---|---|
| Windowing manufactures the agreement | 3-window sweep; H3 as a kill condition |
| AMG over-segments, inflating any matching score | Hungarian one-to-one + explicit `cardinality_ratio` |
| Texture shuffle changes local intensity | Tile-mean validity check, enforced in code |
| Intensity remap moves edges | Monotonicity check, enforced in code |
| Tile size drives the H2 result | Vary `shuffle_tile` (§18) |
| Metric shopping | Three pre-registered metrics, all reported |
| Slice selection favours easy anatomy | Pre-register the slice list before running |
| The effect is generic to AMG, not CT | COCO control (H4) |

## 22. Reviewer #2 compliance matrix (binding)

| # | Attack (`reviewer_attacks.md`) | Binding obligation | Where satisfied |
|---|---|---|---|
| 1 | Windowing manufactures the result | Sweep 3 windows, report all | E2 / H3 |
| 2 | Agreement ≠ mechanism | Intensity remap vs texture shuffle | E3 / H2 / §12 |
| 3 | k-means is one cheap baseline among many | Add Otsu, GMM, SLIC; beat superpixels | §13 |
| 4 | Metric shopping | Pre-register IoU + ARI + boundary-F | §15 |
| 5 | "SAM bad on CT" is known | Ship mechanism, not Dice tables | §8, §10 |
| 6 | Hyperparameter brittleness | AMG grid | §18 |

**Residual obligation (FACT, verbatim):** *"Must earn mechanistic via intensity
vs texture counterfactuals; else evaluation note."* Card **E3** is the whole of
it, which is why §28 refuses to submit before E3 resolves.

## 23. Scope boundaries

- **Not** a new decoder, loss, or adapter.
- **Not** a claim that SAM is bad on CT.
- **Not** a claim that a guided filter matches HQ-SAM — that was the adjacent
  `F-012`, and `stage2_ABCF_summary.md` explicitly forbids the framing.
- **Not** 3D. Single slices only; volumetric consistency is out of scope.
- **Not** a MedSAM comparison. Adaptation methods are context, not subject.

## 24. Compute & resource budget

**All HYPOTHESIS.** Day-1 ≈2 GPU-h (`evolution_summary.md`). Decision-tree
path to a complete paper ≈15–35 GPU-h. Outer bound of the full matrix 40–80
GPU-h (`experiments.md`). Card E0 is CPU-seconds and needs no GPU at all.

No training. No checkpoint triples. This is the cheapest of the Windows6 Final
3 and the reason `README.md` marks it *"#1 start here"*.

## 25. Reproducibility & release plan

- Seeds fixed through `config.set_seed`, which returns an explicit `Generator`
  so functions never read global RNG state.
- Configs are data (`configs/*.yaml`); unknown keys raise rather than being
  ignored, so a silently dropped field is impossible.
- `tests/test_smoke.py` runs on numpy alone — no scipy, no PyYAML, no weights.
- Release: code, configs, the pre-registered slice list, and per-slice metric
  CSVs. Derived metrics only; no patient data redistributed.

## 26. Risks & mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| H2 fails → downgrade to evaluation note | High | Accepted, but §20.1 must be settled first |
| Concurrent work publishes the equivalence | Medium | Cheap protocol; run E1+E3 early. Lower than Idea_03's exposure because our gap is structural, not absence-defined |
| AMG mask counts make matching unstable | Medium | Cardinality diagnostics; sensitivity to `min_area` |
| Only one window shows the effect | Medium | Pre-declared pivot (§20) |
| Reviewers read it as "SAM is bad on CT" | Medium | Framing discipline in §8, §23 |

## 27. Ethical & data considerations

Public, de-identified CT datasets under their own licences. No re-identification
is attempted and no patient imagery is redistributed. No clinical claim is made:
this is a study of a model's behaviour, not of diagnosis. If the finding holds,
the actionable message is a caution to method developers, not to clinicians.

## 28. Deliverables & decision tree

**Deliverables.** Short analysis paper; the harness; the pre-registered slice
list; per-slice metric tables.

```
E0 harness  ──fail──> fix implementation (never a scientific conclusion)
   │pass
E1 killer   ──SLIC ≥ intensity on all windows──> KILL
   │H1 holds
E2 windows  ──1/3 windows only──> PIVOT: windowing artifact
   │≥2/3 windows
E3 CAUSAL   ──shuffle ≈ remap──> DOWNGRADE to evaluation note (resolve §20.1 first)
   │dissociation holds
E4 COCO     ──COCO reproduces it──> KILL CT-specificity; general AMG note at most
   │CT-specific
   └─> mechanistic paper. E5/E6 optional strengthening.
```

**Candidate titles.** *Is SAM AMG Just Intensity Clustering on CT?* ·
*Windowing, Superpixels, and the Objectness of Foundation Models* ·
*A Causal Test of SAM's CT Objectness*
