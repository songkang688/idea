# P1 Wave B — w4 Judge A (dedup) — Windows13 — wave K+L+M

- **Branch:** `cursor/p1-wave-b-w4-judge-a-dedup-4008`  |  **Generated:** 2026-08-29T00:49:33Z
- **Scope:** gen_k (105) + gen_l (100) + gen_m (100) = 305 ideas. N/P/O enumerated for collision flags only. No new ideas, no invented numbers, no citations. Canonical master READ-ONLY.
- **Canonical collision target:** the w3 consolidator was COMPLETE at judge time — `origin/cursor/p1-wave-b-consolidator-w3-bf20` `ideas_master.jsonl` (592 = 494 w2 + 98 gen_j). w3-accepted gen_g/gen_h (GATE-5 remand lane) were treated as accepted-context and flagged as `w3-accepted:*`. The finalize-time re-fetch found the GATE-5 repair tip `origin/cursor/p1-wave-b-w3-gate5-repair-f611` (638-line master = 592 + 46 repaired G/H); the judge re-collided against the 638 superset — the 6 records new to its context (G-003, G-012, G-057, G-087, H-050, H-084) produced one flag (H-050 on `L-059`); all six `w3-accepted:*` flag targets remain in the still-remanded 127.

## Verdict summary

| shard | input | keep | kill_or_merge |
|---|---|---|---|
| gen_k | 105 | 99 | 6 |
| gen_l | 100 | 94 | 6 |
| gen_m | 100 | 95 | 5 |
| **total** | **305** | **288** | **17** |

14 within-wave duplicate groups (all pairwise; 8 fired the family/cell cap or the w2 equalization guard), 3 master-collision kills, 0 cross-shard merges (3 cross-shard families flagged instead: effective_sample_correlation, iterated_self_labeling_drift, depth_target_parameterization).

## Method (short)

Hypothesis-level comparison (mechanism + falsification design), not lexical: the max Jaccard anywhere was 0.239, so every verdict is a manual hypothesis judgment. Merge rule: same mechanism + same falsification design, substrate/X-slot swap only. Family membership = merge trigger with the <=6 cap applied per unique fingerprint cell (manipulated-variable x measurement-family); families whose members occupy distinct cells are flagged, not merged (w3 precedent). Master ports killed on the w3 mg-precedent standard.

## Within-wave duplicate groups

- **dg01_effective_diversity_not_count** — primary `W13-P1-K-054` absorbs `W13-P1-K-014` *(family/cell-cap trigger)*: Same law: geometry-model performance is governed by effective scene/layout diversity, not raw image/frame count (correlated frames and layout-redundant images inflate nominal counts). K-054 states the compute-matched scaling form (unique-scene count vs frames-per-scene vs parameters); K-014's layout-stratified-subset replication of full-data depth performance is the subset-selection arm of the same falsification. Cell cap fired (effective-diversity cell); K-014's layout-coverage-saturation arm preserved. Both collide with gen_n scaling territory (N-027/N-014) — flagged.
- **dg02_densification_capacity_null** — primary `W13-P1-K-037` absorbs `W13-P1-K-043` *(family/cell-cap trigger)*: Same null hypothesis with two replacement arms: the celebrated adaptive densify-split-prune machinery of Gaussian splatting is not the active ingredient — K-037 claims a blind capacity schedule (annealing) matches it, K-043 claims overcomplete-init-then-prune (capacity-then-selection) matches it. One matched-budget falsification decides both; same subject_system and measurement_family (matched-budget NVS quality). K-043 kept as the grow-vs-prune arm.
- **dg03_frame_subset_information_locality** — primary `W13-P1-K-067` absorbs `W13-P1-K-070`: One information-locality measurement, two arms: K-070's oracle frame-subset audit (benchmarks answerable from <1% of frames => they measure retrieval) is the oracle arm of K-067's learned query-conditioned selector claim (10% budget retains nearly all accuracy). Same benchmarks, same sufficiency-vs-budget instrument; the oracle audit is the selector study's mandatory baseline. K-070's benchmark-critique deliverable preserved as an arm.
- **dg04_interface_ceiling_and_recovery** — primary `W13-P1-L-015` absorbs `W13-P1-L-011`: One falsification unit: L-011 measures the text-interface information ceiling (probe on textual intermediates plateaus below probe on raw tool outputs); L-015 recovers it with a soft-token adapter, isolating discretization as the binding constraint. Measuring the recovery fraction (L-015) requires measuring the gap (L-011) as its control arm. Same mechanism (verbalization discards spatial detail), same probe instrument. HIGH master adjacency E-041 flagged.
- **dg05_shared_percept_sampling_regime** — primary `W13-P1-L-030` absorbs `W13-P1-L-021` *(family/cell-cap trigger)*: L-021's saturation curve (self-consistency voting flattens by k=4 on perception-bound questions because samples share the same wrong percept) is the direct corollary measurement of L-030's regime law (cross-sample variance under cheap sampling detects compute-limited vs representation-limited instances and predicts loop-gain sign). Family-cap trigger (shared_percept_decorrelation): merging L-021 keeps the family's kept cells at the cap. Saturation-curve arm preserved.
- **dg06_measured_competence_conditioning** — primary `W13-P1-L-009` absorbs `W13-P1-L-047`: Same intervention and claim, X-slot swap: inject empirically measured per-tool reliability profiles into the controller/planner prompt and decision quality beats description/signature conditioning. L-009 = router instance (competence cards vs descriptions), L-047 = program-synthesis instance (error profiles vs signatures). One probe-suite-then-condition design; L-047's plan-structure-shift predictions preserved as an arm.
- **dg07_guideline_interpretation_noise** — primary `W13-P1-L-059` absorbs `W13-P1-L-054`: One mechanism (guideline interpretation is the dominant label-noise source in agent annotation), audit arm + fix arm: L-054 shows paraphrasing guidelines shifts label distributions as much as swapping the model; L-059 removes the interpretation step by compiling guidelines into executable checklists and claims the variance reduction beats a model upgrade. Same boundary-case locus, same noise-attribution design. L-054's publish-and-version-guidelines reproducibility arm preserved.
- **dg08_pipeline_variance_decomposition** — primary `W13-P1-L-097` absorbs `W13-P1-L-069`: Near-verbatim within-shard duplicate: both run the same nested/single-source seed-toggling variance-attribution design on vision-agent pipelines and both conclude controller token-sampling dominates end-answer variance, with the same freeze-the-top-component deliverable. L-069 is the active-viewing instance (adds a crop-selection component) of L-097's general pipeline law; crop-selection component preserved as an arm.
- **dg09_iso_compute_equalization_null** — primary `W13-P1-L-092` absorbs `W13-P1-L-074` *(family/cell-cap trigger)*: w2 equalization-null guard (<=3 per shard) fired: gen_l carries four matched-budget-null ideas (L-002, L-061, L-074, L-092). L-074 (majority voting matches debate/arbitration at iso-compute; deliberation is compute repackaged) is the protocol-comparison arm of L-092's iso-cost accounting protocol (loop vs bigger single model; a large share of loop gains is purchased compute). Same normalization design, same shrinkage measurement. L-074's protocol-spread arm preserved; tension with kept L-071 (mixed-encoder debate gains) recorded.
- **dg10_depth_target_gradient_allocation** — primary `W13-P1-M-001` absorbs `W13-P1-M-002` *(family/cell-cap trigger)*: Same cell (monocular depth regression targets x AbsRel/delta1 + gradient statistics): the target parameterization (metric/log/inverse) acts as a per-pixel gradient preconditioner, not a representational change. M-001 states the law (log wins exactly on wide depth-range scenes, with a predictable threshold); M-002 is the equivalence control (explicit 1/z^2 Jacobian rescaling reproduces the inverse-depth advantage without changing target space). One falsification: manipulate parameterization and matched gradient rescaling, decompose. Constructive recipe arm preserved.
- **dg11_budget_crossover_reweighting** — primary `W13-P1-M-015` absorbs `W13-P1-M-010` *(family/cell-cap trigger)*: Same law, spatial vs spectral statement: default gradient allocation starves boundary/high-frequency structure until interiors saturate, so emphasis reweighting (boundary emphasis in M-015, wavelet/Fourier band boosting in M-010) only helps under truncated budgets, with a measurable crossover budget where the benefit vanishes. Boundary bands ARE the high-frequency content; both designs sweep reweighting x budget and read band/region-resolved error vs budget. Cell cap fired; M-010's frequency-basis instrument preserved as an arm.
- **dg12_conflict_localized_decoder_splitting** — primary `W13-P1-M-061` absorbs `W13-P1-M-062`: Same instrument and claim, population-slot swap: measure layer-resolved gradient-conflict profiles between two demand populations sharing decoder features, then place the architectural split at the measured conflict onset and capture the full-split benefit at a fraction of parameters. M-061 = intra-task populations (boundary vs interior pixels), M-062 = inter-task (segmentation vs depth). Identical measurement family (conflict profiles + split-recovery fraction). M-061 kept primary for the fresher intra-task claim; M-062's multi-task folklore-replacement arm preserved.
- **dg13_confusable_pair_zero_sum** — primary `W13-P1-M-009` absorbs `W13-P1-M-066` *(family/cell-cap trigger)*: M-066's observed law (confusable class pairs show anti-correlated late-phase accuracy fluctuations because shared evidence makes boundary updates zero-sum) is exactly the signature M-009 predicts and causally manipulates via output coupling (softmax couples logits zero-sum; sigmoid decouples). Same measurement family (pairwise fluctuation anti-correlation + boundary confusion); M-009 holds the causal arm, M-066's redistribution-vs-undertraining diagnostic preserved. Cell cap fired.
- **dg14_weight_averaging_boundary_failure** — primary `W13-P1-M-039` absorbs `W13-P1-M-100` *(family/cell-cap trigger)*: Same mechanism and verdict on two instances of iterate averaging: weight-space averaging equals LR decay only where the local loss is quadratic/affine-compatible, and dense boundary directions violate that, so averaging matches decayed schedules on interiors but fails on boundary placement. M-039 = constant-LR+EMA (schedule-free) instance; M-100 = SWA tail-averaging instance with the boundary-disagreement adoption criterion. One region-decomposed parity design; M-100's disagreement-decomposition criterion preserved as the adoption-rule arm. Cell cap fired. Tension with kept M-035 (prediction-space snapshot averaging HELPS boundaries) recorded.

## Master-collision kills (targets in the 592 master)

- **mg01_contamination_stratified_port** — `W13-P1-K-100` -> `W13-P1-C-024`: Near-verbatim cross-wave port (G-057 precedent): stratify test items by contamination/proximity to web-scale pretraining and show reported zero-shot generalization is concentrated on contaminated items — accepted C-024's seen-shot design with depth benchmarks in the substrate slot; C-023 (semantic near-duplicates evade dedup tools) already covers the same-physical-space near-duplicate mechanism K-100 leans on. No subject-native mechanism beyond the substrate swap. Contamination lawification is also gen_n territory (N-084 contamination inflation law) — recorded for the N judge.
- **mg02_backend_harness_variance_port** — `W13-P1-K-104` -> `W13-P1-C-077`: Near-verbatim port (mg05/w3 precedent that killed G-078 and H-058): pipeline-convention variance (here mesh fusion/post-processing backends on indoor-reconstruction leaderboards) moves scores by amounts comparable to claimed method deltas, exposed by standardized re-evaluation — accepted C-077's harness-variance claim and design with the reconstruction backend in the convention slot. Mesh-backend arm preserved in the flag.
- **mg03_occlusion_memory_horizon_port** — `W13-P1-K-079` -> `W13-P1-A-052`: Near-verbatim port: accepted A-052 already states the claim and protocol — reacquisition/permanence collapses at a critical occlusion duration set by memory capacity (a cliff, not a slope), measured by an occlusion-duration sweep. K-079 generalizes the subject slot from SAM2 to memory-based video systems and adds a constant-velocity dynamics-state baseline arm (preserved in this note; resurrection candidate if the consolidator wants the dynamics-vs-memory comparison as its own track). Mechanism, manipulated variable and measurement family are identical to A-052.

## GATE record

- **gen_k schema drift (all 105 records):** separate `kill_threshold` field + plural `evidence_labels` — consolidator must normalize before master merge. Content is gate-compliant in 100/105; **5 keeps lack numerals** in their thresholds (K-035, K-039, K-065, K-083, K-094) and are marked `retrofit_needed` — no numbers invented here.
- **gen_l / gen_m:** fully compliant (100/100 each, embedded numeric kill conditions + evidence_label). gen_m carries provenance extras (source_shard, wave, novelty_status, seg_metric_dependent) — kept verbatim.
- **Genre vocabulary drift (GATE-6):** three vocabularies across shards; self-declared distributions: gen_k {'characterization': 44, 'debunk_audit': 27, 'constructive_capability': 34}, gen_l {'characterization': 48, 'debunk': 3, 'constructive-capability': 47, 'eval-critique': 2}, gen_m {'characterization_law': 58, 'constructive_capability': 26, 'audit_debunk': 16}. Re-audit phrasing before genre quotas.

## Flagged permutation families (kept members occupy distinct fingerprint cells)

- **monocular_metric_side_channels**: 6/6 kept — K-017, K-022, K-058, K-091, K-092, K-095
- **rolling_shutter_as_signal**: 2/2 kept — K-058, K-089
- **training_prior_overrides_evidence**: 4/4 kept — K-005, K-011, K-050, K-057
- **camera_projection_bias**: 6/6 kept — K-013, K-018, K-021, K-023, K-051, K-094
- **onpath_vs_offpath_extrapolation_cliff**: 4/4 kept — K-039, K-044, K-046, K-047
- **margin_over_trivial_baseline**: 3/4 kept — K-020, K-028, K-063, K-104
- **metric_choice_reorders_rankings**: 5/6 kept — K-031, K-090, K-099, K-101, K-102, K-104
- **stratified_hidden_regime**: 5/5 kept — K-016, K-024, K-025, K-036, K-103
- **temporal_understanding_is_shallow**: 5/6 kept — K-069, K-070, K-071, K-072, K-074, K-078
- **memory_keying_and_state**: 4/5 kept — K-055, K-068, K-073, K-079, K-080
- **occlusion_recovery**: 4/5 kept — K-029, K-032, K-036, K-079, K-080
- **densification_capacity_null**: 1/2 kept — K-037, K-043
- **effective_sample_correlation**: 8/9 kept — K-014, K-054, M-030, M-037, M-073, M-081, M-082, M-084, M-086
- **text_interface_information_loss**: 9/10 kept — L-011, L-012, L-013, L-014, L-015, L-016, L-017, L-018, L-019, L-020
- **shared_percept_decorrelation**: 9/10 kept — L-021, L-024, L-030, L-031, L-039, L-071, L-072, L-078, L-082, L-086
- **equalization_matched_budget_null**: 3/4 kept — L-002, L-061, L-074, L-092
- **self_training_on_filtered_traces**: 3/3 kept — L-006, L-029, L-049
- **verification_query_design**: 6/6 kept — L-033, L-034, L-036, L-038, L-040, L-075
- **annotation_agent_pathologies**: 7/8 kept — L-051, L-053, L-054, L-056, L-057, L-058, L-059, L-060
- **judge_reliability_engineering**: 7/7 kept — L-081, L-083, L-084, L-085, L-086, L-088, L-090
- **iterated_self_labeling_drift**: 3/3 kept — K-015, L-053, M-069
- **active_ingredient_equivalence**: 13/14 kept — M-002, M-007, M-008, M-013, M-019, M-023, M-024, M-027, M-047, M-063, M-071, M-078, M-080, M-089
- **measured_statistic_scheduling**: 8/8 kept — M-034, M-038, M-041, M-069, M-072, M-086, M-091, M-098
- **boundary_vs_interior_decomposition**: 10/12 kept — M-005, M-010, M-015, M-033, M-035, M-039, M-059, M-061, M-070, M-090, M-099, M-100
- **depth_target_parameterization**: 2/3 kept — K-023, M-001, M-002
- **regularizer_substitution_exchange**: 4/4 kept — M-025, M-077, M-087, M-093
- **acquisition_order_laws**: 8/8 kept — M-051, M-052, M-053, M-055, M-056, M-057, M-058, M-060
- **instability_pathological_subpopulation**: 6/6 kept — M-024, M-095, M-096, M-097, M-098, M-099
- **gradient_conflict_geometry**: 5/6 kept — M-016, M-017, M-061, M-062, M-067, M-068

## HIGH master-collision keeps (novelty gate first-in-line)

- `W13-P1-K-004` -> W13-P1-C-046: HIGH: C-046 (linear-probe protocol assumptions rerank backbones) is the accepted probe-protocol-artifact ancestor; K-004's delta is the resolution/patch-density mechanism for 3D-awareness gaps specifically. Novelty gate first-in-line.
- `W13-P1-K-054` -> W13-P1-F-050, W13-P1-F-073: HIGH: distinct-unit scaling family — F-050 (synthetic utility scales with distinct-prompt count, not image count) and F-073 (graphics transfer scales with distinct assets) are accepted ancestors of 'unique-unit count, not raw count, governs scaling'; K-054's delta is the 3D substrate (unique scenes vs frames) and the compute-exponent consequence. Strong gen_n collision (N-027 unique-cluster law, N-014 dense-transfer atlas) — flagged for the N judge.
- `W13-P1-K-074` -> W13-P1-A-055: HIGH: A-055 (SAM2 preferred temporal sampling rate; accuracy non-monotone in fps peaking at training statistics) is the accepted ancestor of the baked-in frame-rate prior; K-074's delta is the multiplicative speed/duration bias law (bias = train/test fps ratio) on general video models. Novelty gate first-in-line.
- `W13-P1-K-076` -> W13-P1-F-003, W13-P1-A-061, W13-P1-E-060: HIGH: motion/viewpoint-statistics matching family — F-003 (matching motion statistics closes the flow syn-to-real gap), A-061 (viewpoint prior from licensed photography), E-060 (egocentric failure is viewpoint-distributional) all accepted; K-076's delta is the camera-motion-vs-content decomposition with motion-matched exocentric resampling as the intervention. Novelty gate first-in-line.
- `W13-P1-L-015` -> W13-P1-E-041, W13-P1-E-093: HIGH: E-041 (MLLM language outputs discard spatial detail their vision features contain; probes recover it) and E-093 (segmentation tokens are a low-bandwidth bottleneck) are accepted intra-model ancestors of the verbalization-bottleneck law; L-015's delta is the inter-module (tool-to-controller) locus and the soft-token adapter recovery instrument. Novelty gate first-in-line.
- `W13-P1-L-018` -> W13-P1-D-066: HIGH: D-066 (MLLM box coordinates cluster on round numbers — tokenizer priors) is the accepted ancestor of round-value output distortion; L-018's delta is the loop-depth dose-response (relay restatements quantize estimates progressively). Novelty gate first-in-line.
- `W13-P1-L-065` -> W13-P1-E-097: HIGH: E-097 (verbalized spatial doubts uncorrelated with actual boundary errors while internal signal exists) is the accepted ancestor of 'introspection is not verbalizable but is decodable'; L-065's delta is the stopping-policy substrate and the trained sufficiency head. Novelty gate first-in-line.
- `W13-P1-L-067` -> W13-P1-D-080, W13-P1-J-065, W13-P1-D-021: HIGH: counting family — D-080 (subitizing-plus-guessing signature), J-065 (count not represented beyond ~4), D-021 (density-dependent undercount) accepted; L-067's delta is the external-state enumeration loop (mark counted instances, re-query) as the working-memory fix, with a crossover-density claim. Novelty gate first-in-line.
- `W13-P1-L-072` -> W13-P1-D-060: HIGH: D-060 (shared-data-correlated errors defeat foundation-detector ensembling) is the accepted ancestor of encoder-diversity-governs-ensemble-gain; L-072's delta is the 2x2 encoder/LLM factorial isolating WHICH diversity axis matters in agent ensembles. Novelty gate first-in-line.
- `W13-P1-L-085` -> W13-P1-C-071: HIGH: C-071 documents judge self-preference; L-085's delta is the mechanism localization (style transplant at fixed content moves preference => bias lives in surface-form recognition). Novelty gate first-in-line.
- `W13-P1-L-092` -> W13-P1-D-091, W13-P1-C-045: HIGH: matched-budget-null ancestors D-091 (equal-inference-budget re-evaluation collapses architecture advantages) and C-045 (prompt-budget equalization) accepted; per w3 precedent (G-086 kept with flag) the field-specific iso-cost protocol for agent loops is kept as this wave's single umbrella (absorbed L-074). Also collides with w3-accepted G-086 (GATE-5 remand lane).

## Deliberate tensions (adjudicate by experiment — do NOT merge)

- `K-006` vs master J-010/J-005: diffusion/generative features carry genuine 3D structure vs their multi-view stability is texture-correlated appearance sensitivity. Adjudicate by the texture-controlled viewpoint sweep, not dedup.
- `K-071` vs master A-056: SAM2 shows a temporal-asymmetry artifact while K-071 claims near-zero arrow-of-time signal on physics content — compatible (artifact vs capability) but the physics-stratified probe should test both.
- `K-083` vs master J-005/J-011 (and kept K-006): generative priors supply genuine geometry vs only photorealism — the geometry-vs-photometrics decomposition adjudicates.
- `L-004` vs L-065 (and master E-097): marginal tool benefit is verbally elicitable (draft + expected-gain self-probe) vs sufficiency is not verbalizable and needs a trained head. Both kept; regime-mapping pair.
- `L-065` vs L-004 (see above); E-097 supports the not-verbalizable side.
- `L-071` vs L-092 (absorbed L-074): mixed-encoder debate recovers real perception errors vs protocol differences vanish under iso-compute accounting. The factorial (encoder diversity x protocol x matched compute) adjudicates.
- `L-092` vs L-071 (see above).
- `L-082` vs master D-065: no generator-verifier gap for perception vs MLLMs verify detections better than they produce them. Resolution hypothesis: D-065's gap is coordinate-production, not perception — exactly L-082's claimed boundary.
- `L-006` vs L-051/L-053: consistency-filtered traces are a usable self-supervision signal vs agent agreement is nearly uninformative about correctness and self-labeling amplifies bias. Same loop, opposite bets on agreement.
- `L-029` vs L-051/L-053 (same tension as L-006).
- `L-049` vs L-051/L-053 (same tension; L-049's procedural ground truth partially escapes it — the escape is the experiment).
- `L-051` vs L-006/L-029/L-049 (see above).
- `L-053` vs L-006/L-029/L-049 (see above).
- `M-071` vs M-076: BN batch-statistic noise is the harm frozen-BN avoids vs BN train-mode stochasticity is a load-bearing regularizer. Likely regime-dependent (fine-tuning atop converged features vs training); the noise-corrected-BN and noise-injection arms adjudicate.
- `M-076` vs M-071 (see above).
- `M-035` vs M-039 (absorbed M-100): prediction-space snapshot ensembling HELPS boundary placement (averages boundary hypotheses) vs weight-space averaging FAILS at boundaries (non-affine geometry). Complementary halves of one averaging theory — keep both.
- `M-039` vs M-035 (see above); also vs w3-accepted G-028 / killed G-068 on what weight averaging buys.
- `M-053` vs M-058: variance-per-exposure is the acquisition clock (so resampling should reorder variance-mismatched classes) vs acquisition order is optimization-forced and resampling-invariant. Directly contradictory predictions under engineered resampling — a decisive experiment exists.
- `M-058` vs M-053 (see above).

## Anomalies (protected)

- `K-027`: learned flow computes texture displacement, not motion: isoluminant/second-order stimuli that humans perceive expose a missing motion-energy computation — a biological-vision-grounded capability gap
- `K-042`: splat failures on mirrors are optimization pathologies, not representational limits: reflection-consistent initialization reaches virtual-image geometry that renders correctly
- `K-045`: floater artifacts are fossilized exposure/white-balance inconsistency, not sparse-view ambiguity — capture photometric consistency, not more views, removes them
- `K-050`: pointmap reconstructors output prior-consistent scale on miniatures/sets/macro — memorized scene scale masquerading as inferred geometry, with predictable error direction
- `K-058`: rolling-shutter skew and exposure blur are absolute-time-stamped measurements of image motion — a metric-scale side channel needing no IMU or intrinsics
- `K-071`: video foundation models near chance on arrow-of-time for physics-driven footage while passing semantic-cue clips — decisive for world-model claims and invisible to mainstream benchmarks
- `K-078`: pixel-space next-frame loss is dominated by texture advection; dynamics-decisive pixels contribute vanishing gradient share — quantitatively predicting why low-loss predictors fail physics probes
- `K-085`: near-forward camera motion makes object motion along the camera axis nearly indistinguishable from wrong-depth static geometry — a degeneracy affecting a large share of driving/walking footage, silently resolved by priors
- `K-089`: rolling-shutter row time makes every frame a temporal scan: modeling it super-resolves 3D trajectories beyond the nominal frame rate — an artifact converted into a measurement channel
- `K-091`: defocus gradients across the frame over-constrain focal length given a depth estimate — a physics-based single-image intrinsics oracle for structure-free scenes
- `K-092`: scenes are saturated with gravity witnesses; visual gravity estimation can reach IMU-competitive accuracy on ordinary footage, unlocking orientation-aware vision without inertial hardware
- `L-017`: persistent numbered visual IDs stamped at first detection eliminate cross-turn referring drift without model changes — identity decay located in the text channel, not the VLM
- `L-035`: verify-revise dynamics form attractor maps: a measurable fraction of instances converge to stable wrong answers from any start, and convergence speed carries no information about correctness
- `L-039`: blinding the verifier to the proposer's chain-of-thought RAISES perception-error detection — transcript exposure induces percept inheritance, reversing the more-context-is-better default
- `L-064`: a drafted answer in the transcript acts as an anchor that survives contradicting crop evidence; zoom-first ordering removes the anchor at identical compute
- `L-076`: hallucinated details become sticky after ~2 transcript repetitions (adoption probability crosses correction probability) — a quantified contagion threshold for multi-agent error lock-in
- `L-082`: the generator-verifier gap that powers code/math self-improvement is structurally missing for perception: judging needs the same percept as producing — bounding all same-model visual self-training
- `L-095`: failure-conditioned retries are measurably LESS grounded than first attempts on matched inputs — 'try harder' converts correct abstentions into confident confabulation
- `M-029`: when per-pixel-mean loss gradients approach Adam's epsilon, effective steps shrink nonuniformly — resolution-dependent silent undertraining with a one-line epsilon/reduction fix
- `M-046`: dense fine-tuning exits the linearly-connected basin of its initialization within hundreds of steps while classification stays connected — a sharp geometric signature of dense adaptation
- `M-054`: grokking-like delayed generalization exists in dense prediction: validation boundary quality jumps long after training loss saturates, with the delay controlled by weight decay
- `M-074`: fp16 underflow is class-selective: rare classes' sparse small-magnitude gradients fall below representable magnitude first — a precision tax invisible in mIoU
- `M-083`: within-epoch presentation order leaves a recency imprint at high LR: statistically identical images seen late in the final epoch are predicted better — an uncontrolled ordering bias
- `M-085`: within-image negatives make dense contrastive objectives satisfiable by position-encoding rather than content — a positional shortcut detectable by a position-decoding probe
- `M-095`: loss spikes replicate across seeds on the same image-crop-augmentation conjunctions — spike-trigger mining is a dataset diagnostic, not a stability mystery
- `M-097`: attention-entropy collapse in an identifiable set of heads precedes divergence by hundreds of steps, and clamping only those heads' temperature prevents the explosion — early warning plus causal intervention

## Off-master collision flags (for the N/P/O judges and the G/H remand lane)

- `K-002`: gen_p:P-058 (frequency-matched layer selection — principled layer choice for dense readout)
- `K-005`: gen_o:O-025 (physical pixel size stripped at training — scale blindness)
- `K-018`: gen_o:O-005 (flat-port refraction radial depth bias underwater — same projection-mismatch signature)
- `K-020`: gen_n:N-013 (frozen-probe vs fine-tuned scaling exponents)
- `K-027`: gen_o:O-006 (trackers follow caustic flicker — motion-carrier confound)
- `K-050`: gen_o:O-025 (scale-blindness territory)
- `K-054`: gen_n:N-027 (effective dataset size is unique-cluster count — same law, 2D substrate); gen_n:N-014 (dense-transfer scaling atlas); gen_n:N-006 (scaling-curve decisions); gen_o:O-096 (near-duplicate nominal sets, tiny effective diversity)
- `K-057`: gen_o:O-048 (chart models follow rendering-template priors; re-render collapses)
- `K-058`: gen_o:O-079 (wavelength attenuation as absolute range cue — physical metric side channel template)
- `K-061`: gen_o:O-082 (hillshade-azimuth overfitting); gen_o:O-016 (sensor gain-profile positional prior — sensor-signature shortcut template)
- `K-077`: gen_o:O-032 (pathology models encode scanner-compression fingerprints — same codec side-channel mechanism); w3-accepted:H-076/H-077 (temporal-aliasing exploitation of video SR; GATE-5 remand lane)
- `K-091`: gen_o:O-021 (defocus carries axial z information in microscopy — same physical cue)
- `K-094`: gen_o:O-005 (underwater radial depth bias — same fingerprinting instrument)
- `K-019`: w3-accepted:G-005 (TTA collapse-frequency protocol; GATE-5 remand lane)
- `L-057`: gen_n:N-068/N-072 (membership/provenance auditing territory)
- `L-089`: gen_u:(queued) adversarial/reward-hacking territory
- `L-092`: w3-accepted:G-086 (matched-budget reinvestment claim; GATE-5 remand lane)
- `L-099`: gen_o:O-100 (ground-sample-distance standardization closes cross-site gap — same standardization-recovery template)
- `M-008`: w3-accepted:H-091 (matched-recipe equalization template; GATE-5 remand lane)
- `M-015`: gen_p:P-058 (spatial-frequency-demand matching)
- `M-025`: w3-accepted:G-028 (weight-averaging gains as generic variance reduction; GATE-5 remand lane)
- `M-039`: w3-accepted:G-028 (averaging-as-variance-reduction adjacency; also note w3-killed G-068 tension on weight-averaging frontiers)
- `M-054`: gen_n:N-049 (representational reorganization precedes capability); gen_n:N-052 (emergence-as-memorization territory)
- `M-055`: gen_p:P-059 (anti-aliased patch embedding for thin structures); gen_p:P-062 (resolution-extrapolation recipes); gen_n:N-019 (resolution-schedule artifacts in scaling claims)
- `M-057`: gen_n:N-049 (early-warning reorganization signatures — same claim family, feature-geometry instrument)
- `M-059`: gen_n:(dynamics territory) epoch-wise non-monotonicity lawification
- `M-068`: gen_p:P-079 (context-matched rare-class transplantation — rare-class gradient-budget interventions)
- `M-069`: gen_n:N-070 (distilled students inherit membership secrets)
- `M-087`: gen_n:N-036 (augmentation as data multiplier with scale-decaying exchange rate — same exchange-rate template)

## Epistemic status

NO novelty verified for any kept idea. All prior-art and known-result remarks are the judge's unverified hypotheses (MODEL SPECULATION); no experimental numbers or citations were invented. kill_or_merge is a redundancy disposition, not a quality verdict; the Consolidator may resurrect any merged id (merge targets and preserved arms recorded per kill).
