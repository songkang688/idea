# P1 Wave A — batch_001 gen_B Report

- **task_id:** p1_wave_a_batch001_gen_B
- **role:** generator (Wave A)
- **windows_path:** Windows15
- **territory:** T02 Medical segmentation
- **base branch:** origin/cursor/windows15-p1-state-reader-a5fa
- **output_dir:** Windows15/_state/tasks/p1/batch_001/gen_B/
- **idea_count:** 100 (target 100, contract range 80–120)
- **id range:** W15-B001-B-001 … W15-B001-B-100 (sequential, unique, machine-verified)

## What was generated

100 distinct scientific hypotheses about medical image segmentation. Per the scientific bar, each
idea is anchored in a new observation, falsifiable hypothesis, failure mode, ignored assumption,
counter-intuitive result, measurement critique, or foundation-model systematic defect — not
module-combination, loss/backbone swaps, or "port method X to medical" stamps. Each JSONL record
carries the full required schema: `idea_id`, `one_line`, `cluster`, `problem`, `core_hypothesis`,
`falsifiable_prediction`, `why_important`, `why_possibly_novel`, `minimal_falsification_experiment`,
`main_risk`, `community_default_belief`, `why_that_may_be_wrong`, `fastest_falsification`,
`evidence_class` (plus `territory` for downstream dedup convenience).

## Cluster distribution (12 clusters)

| Cluster | Count | Theme |
|---|---|---|
| annotation_noise_protocol | 12 | Structured (not random) label noise: rater style, protocol drift, interpolated GT, QC smoothing, memorization timing |
| evaluation_metrology | 12 | Metric pathologies: size confounds, HD95 instability, dose vs Dice, empty-case conventions, statistical power |
| learned_representations_shortcuts | 12 | What models actually use: texture vs shape vs position, HU shortcuts, healthy-prior inpainting, unused symmetry/3D context |
| geometry_resampling_3d | 8 | Anisotropy as information loss, SR hallucination, patch-training vs global constraints, framing/coordinate leakage, FOV truncation |
| distribution_shift_deployment | 8 | Prevalence vs scanner shift, harmonization harming pathology, label shift disguised as image shift, performance cliffs, TTA safety inversion |
| lesion_pathology_segmentation | 8 | Detection vs delineation decomposition, count instability, size-sensitivity dials, continuous involvement fields, indication leakage |
| human_ai_interaction | 7 | Automation bias in editing, edit-cost vs Dice, click policies, variance homogenization, vigilance decrement, plausibility-correctness dissociation |
| supervision_scale_labels | 8 | Partial-label suppression, self-training shape collapse, labeling-budget scaling laws, registration-imprinted bias, federated label semantics |
| uncertainty_safety_medical | 7 | Spatially structured miscalibration, ensembles as label-noise detectors, calibration-vs-accuracy decay rates, abstention rejecting the sick, conformal objects |
| foundation_model_defects_medical | 6 | Gradient-seeking boundary bias, prompt hierarchy ill-posedness, click-budget scaling, report-language grounding bias, contrast-based null models |
| topology_shape_downstream | 6 | Input-driven topology chaos, false-patency bridging, shape priors as rare-anatomy tax, mesh-extraction error budgets, absence detection |
| training_dynamics_optimization | 6 | Dice loss calibration collapse, augmentation-as-noise-regularization, agreement curricula, gradient interference, batch leakage, spatial overfitting |

## Evidence-class tag usage

measurement_critique 34 · falsifiable_hypothesis 34 · failure_mode 34 · ignored_assumption 26 ·
new_observation 25 · counterintuitive_result 20 · new_question 19 · foundation_model_defect 6
(each idea carries 1–2 tags).

## Hard-rule compliance

- **No verified-novelty claims:** every `why_possibly_novel` field is phrased as a hypothesis about
  the literature landscape, not a verified claim. Wave B / later stages must literature-check.
- **No invented citations, papers, benchmark numbers, datasets, or experimental results:** ideas
  reference only generic resource classes (e.g., "a public multi-rater dataset", "multi-site
  labeled corpus"). No numerical results are asserted anywhere; all numbers appear only inside
  falsifiable predictions as hypothesis parameters.
- **Shard-only writes:** only `Windows15/_state/tasks/p1/batch_001/gen_B/` was written.
  `window.lock.json`, `research_state.json`, `ideas_master.jsonl`, `research_ledger.md`, and other
  `gen_*` directories were not touched.

## Territory-boundary notes for the dedup consolidator

- Foundation-model ideas (083–088) were deliberately scoped to *systematic defects observable in
  medical segmentation*, not adaptation/PEFT methods, to minimize collision with T01 (gen_A).
  Flagging them anyway for cross-shard dedup attention.
- Uncertainty ideas (076–082) are medical-segmentation-specific (spatial calibration structure,
  clinical triage, rater-noise identity) but may neighbor T08 (uncertainty/calibration) shards in
  later batches.
- Evaluation-metrology ideas (013–024) may neighbor T07 (benchmark/dataset weaknesses); they are
  scoped to segmentation-metric science rather than dataset construction, but overlap-check is
  recommended.

## Unresolved items

1. Novelty is hypothesized only — no literature verification was performed by this generator (per contract).
2. Ideas 083–088 (foundation-model defects) should be cross-checked against batch_001 gen_A (T01) output during Wave B dedup.
3. Ideas 013–024 and 076–082 flagged as potential future-territory neighbors (T07, T08) for the dedup ledger.
4. Several minimal experiments assume access to multi-rater or repeat-scan data; feasibility triage deferred to later pipeline stages (200→50 selection).
