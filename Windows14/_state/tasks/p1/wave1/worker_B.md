# P1 Wave A — worker_B (Medical segmentation) — Windows14

- **Task:** `p1_gen_w1_b` (P1 Wave A generator, shard worker_B)
- **Territory:** Medical segmentation
- **Windows:** Windows14 (locked; identity taken verbatim from `Windows14/_state/window.lock.json`, `locked: true` verified before any work)
- **Status:** complete
- **Idea count:** 126 (target: at least 120)
- **Output shard:** `Windows14/_state/tasks/p1/wave1/worker_B.ideas.jsonl`

## Generation brief followed

Per the dispatcher instruction, generation prioritized **scientific questions and
falsifiable failure modes of foundation models in medical dense prediction**, and
deliberately avoided mechanical-transfer ideas of the form "apply existing method X
to medical dataset Y." Every idea is framed as a hypothesis about a mechanism,
a failure mode, a measurable law, or an evaluation-validity question, each with a
falsifiable prediction, a minimal falsification experiment, and a fastest-falsification
path (most are inference-only or analysis-only, executable without large training runs).

All 126 records carry `evidence_status = "HYPOTHESIS"`. No novelty is claimed as
verified: `why_possibly_novel` fields are worded as possibility statements pending a
later verification wave. No citations, benchmark numbers, dataset facts, or experimental
results were fabricated; references to prior work are generic and non-specific by design.

## Cluster map (126 ideas, 11 clusters)

| cluster | n | theme |
|---|---|---|
| `boundary_ambiguity` | 12 | Convention-defined vs edge-defined boundaries, inter-rater ambiguity, edge-snapping bias, contour-style memorization, sub-voxel information |
| `signal_physics` | 12 | HU calibration loss, windowing, MR sequence confusion, ultrasound speckle, artifacts, dose, undersampling, bit depth, kernels, contrast phases |
| `dimensionality_3d` | 12 | 2D-vs-3D inductive bias, through-plane topology defects, video-as-volume propagation, orthogonal-plane disagreement, anisotropic PSF, token pruning |
| `prompting_interaction` | 12 | Prompt-geometry priors, negative-click semantics, granularity ambiguity, click-simulation validity, human-model correlated failure |
| `shift_shortcuts` | 12 | Site fingerprints, overlays, position priors, pediatric scale, prevalence shift, pipeline fingerprints, shortcut hierarchies, TTA safety inversion |
| `small_structure_scaling` | 12 | Tokenization-set recall floors, size-stratified scaling, texture-vs-shape by scale, loss gradient ceilings, annotation-noise floor, calibration inversion |
| `uncertainty_calibration` | 12 | Uncertainty vs rater disagreement, epistemic/aleatoric misattribution, conformal conditional coverage, prompt-conditional uncertainty, churn |
| `anatomy_topology` | 12 | Topology-violation census, implicit atlas decodability, adjacency grammar, variant normalization bias, organ-absence hallucination |
| `memorization_contamination` | 10 | Benchmark contamination, mask-template memorization, feature re-identification, duplication inflation, robustness forgetting, adapter leakage |
| `evaluation_science` | 12 | Dice-rank collapse at the frontier, metric disagreement geography, statistical power, reference-dependence of rankings, metric gameability, human-baseline time budgets |
| `language_grounding` | 8 | Report-supervision plateaus, relational grounding, embedding collisions, negation blindness, laterality/flip heritage, register and cross-lingual fragility |

## Constraints honored

- Wrote only the three files listed below; did **not** touch `ideas_master.jsonl`,
  `window.lock.json`, or `research_state.json`.
- No max-Windows scan performed; windows identity used verbatim from the lock.
- Independent shard only; merging into `ideas_master.jsonl` is the consolidator's job.

## Files written

1. `Windows14/_state/tasks/p1/wave1/worker_B.ideas.jsonl` (126 lines, validated: every line parses as JSON, all 15 required fields present and non-empty, unique `id_seed` `w14_p1b_001` … `w14_p1b_126`, `territory = "Medical segmentation"`, `evidence_status = "HYPOTHESIS"` on every record)
2. `Windows14/_state/tasks/p1/wave1/worker_B.md` (this file)
3. `Windows14/_state/tasks/p1/wave1/worker_B.done.json`

## Unresolved items (for downstream waves)

- Cross-shard duplicate risk with worker_A (SAM/FM adaptation territory): overlap is most
  likely in `prompting_interaction` and `shift_shortcuts` clusters; dedup wave should
  compare these clusters against worker_A's shard first.
- Cross-shard duplicate risk with worker_C (ambiguous segmentation / failure mining):
  `boundary_ambiguity` and `uncertainty_calibration` clusters are the closest surfaces.
- All `why_possibly_novel` fields are unverified hypotheses; a P2-style novelty
  verification pass against real literature is required before any novelty claim.
- Several ideas require multi-rater or test-retest datasets (e.g. `w14_p1b_002`,
  `w14_p1b_069`, `w14_p1b_083`, `w14_p1b_114`); dataset availability should be checked
  during feasibility triage.
- A few ideas flag eventual human-subject components (e.g. `w14_p1b_047`, `w14_p1b_084`,
  `w14_p1b_117`); their minimal versions are deliberately proxy-based, but full versions
  need protocol review.

## Recommended next task type

`p1_wave_B_dedup` — merge and deduplicate the three worker shards.
