# P1 Wave B — Judge C: Value / Diversity / Failure-Mode Audit (Windows14)

- **Task:** `p1_wave1_judge_C`
- **Role:** `judge_C_value_diversity` (high-value anomalies, contrarian ideas, failure-mode ideas, mode-collapse risks, missing territories)
- **Independence:** produced without reading Judge A or Judge B outputs.
- **Inputs (read-only, fetched from remote branches):**
  - `origin/cursor/windows14-p1-wave-a-worker-a-e978` → `Windows14/_state/tasks/p1/wave1/worker_A.ideas.jsonl` (132 ideas, territory: SAM / Foundation Model adaptation / PEFT, 22 clusters)
  - `origin/cursor/windows14-p1-wave-a-worker-b-c6ba` → `Windows14/_state/tasks/p1/wave1/worker_B.ideas.jsonl` (126 ideas, territory: Medical segmentation, 11 clusters)
  - `origin/cursor/windows14-p1-wave-a-worker-c-4be5` → `Windows14/_state/tasks/p1/wave1/worker_C.ideas.jsonl` (124 ideas, territory: Smoke / fire / ambiguous (transparent) segmentation + failure mining, 14 clusters)
- **Total ideas reviewed:** 382. All parsed as valid JSONL with a consistent 15-field schema; 0 duplicate `id_seed`s within any shard; all `evidence_status = HYPOTHESIS`.
- **No canonical files touched** (`window.lock.json`, `research_state.json`, `ideas_master.jsonl` untouched). Windows14 remains LOCKED.

## Scope and non-claims

This audit flags ideas for *potential* value. **No novelty is verified here**: no literature search was performed, no papers are cited, and no flag below should be read as a claim that an idea is new. Flags are inputs to the consolidator's ranking, to be reconciled with Judges A and B.

## 1. High-value / contrarian / failure-mode flags (36 ideas)

Selection criteria: (a) field-level leverage if the hypothesis survives (meta-science, evaluation validity, safety); (b) contrarian against a stated default belief with a cheap decisive falsification; (c) failure-mode discoveries with deployment consequences; (d) unifying claims that connect multiple shards. Full machine-readable records in `judge_C.flags.jsonl` (type `high_value`).

### Worker A (SAM / PEFT) — 12 flags

| id | why flagged |
|---|---|
| w14A-019 | Structural inability to output "nothing here" — safety-relevant architectural failure mode, cheap to demonstrate. |
| w14A-041 | Meta-science: contradictory LoRA-on-SAM literature explained by one confound (alpha/rank scale). High leverage if true. |
| w14A-046 | Decisive negative-result audit: BN-based TTA family silently no-ops on LayerNorm models. Falsifiable in hours. |
| w14A-061 | "Closed-region prior" with fractal-dimension threshold — unifies with Worker C's entire amorphous territory; strong cross-shard hypothesis. |
| w14A-062 | "Stuff blindness" as prompt-language insufficiency — a conceptual expressivity boundary, not a benchmark increment. |
| w14A-080 | Embarrassing baseline: static per-deployment spatial prior may explain much of reported fixed-camera "adaptation" gain. Contrarian, cheap. |
| w14A-091 | SAM logits secretly contain alpha mattes — converges with w14p1c-041/110 from an independent shard; convergence raises prior. |
| w14A-099 | Universal half-pixel boundary offset — a one-parameter correction affecting every SAM result; tiny, decisive, broadly consequential. |
| w14A-106 | Adapter backdoors — a novel threat model for the emerging adapter-sharing ecosystem; safety value independent of benchmark gains. |
| w14A-115 | Freezing-bug audit — meta-scientific; if a nontrivial share of "frozen backbone" results train unintended parameters, many papers are affected. |
| w14A-120 | Decoder transplant onto a different frozen encoder ("promptability as a portable interface") — architecturally ambitious, clean falsification. |
| w14A-127 | Challenges the universally inherited frozen-prompt-encoder convention — contrarian against a default nobody tests. |

### Worker B (Medical) — 12 flags

| id | why flagged |
|---|---|
| w14_p1b_002 | Models most confidently wrong exactly where raters disagree most — clinically critical confidence inversion. |
| w14_p1b_019 | Dose reduction degrades models before human-perceptible image quality — inverts an assumed safety margin; high-stakes contrarian. |
| w14_p1b_021 | 8-bit conversion erases low-contrast lesions → hard recall ceiling invisible to aggregate metrics. Silent-pipeline failure with deployment reach. |
| w14_p1b_030 | Isotropic resampling harmful on native anisotropic data — directly contradicts standard practice; cheap paired test. |
| w14_p1b_050 | Burned-in overlays (rulers, text) act as spatial anchors: moving them moves masks. Vivid, decisive shortcut failure. |
| w14_p1b_060 | TTA raises average Dice while increasing *undetected catastrophic* failures — mean-vs-tail safety inversion; reframes TTA evaluation. |
| w14_p1b_083 | Model-version churn exceeds rescan test-retest variation — identifies churn, not accuracy, as the binding constraint for longitudinal use. |
| w14_p1b_093 | Hallucinating surgically removed organs via contextual expectation — dramatic, cheap-to-test failure mode with a clean context-ablation design. |
| w14_p1b_104 | Federated adapter weights invertible to site statistics — privacy attack undermining the rationale for adapter sharing. |
| w14_p1b_107 | Above a quality threshold, Dice ranking decouples from margin-critical clinical error — attacks leaderboard validity where models now operate. |
| w14_p1b_111 | Medical test sets statistically underpowered for claimed deltas — computable by resampling alone; potentially field-changing meta-science. |
| w14_p1b_117 | "Expert-level" claims depend on the human annotation time budget — contrarian audit of the field's headline claim. |

### Worker C (Smoke / fire / transparent) — 12 flags

| id | why flagged |
|---|---|
| w14p1c-002 | IoU head *anti-informative* on smoke (ranks its own worst mask first) — sharp, falsifiable failure claim, stronger than mere miscalibration. |
| w14p1c-004 | SAM "sees through" thin smoke and segments the occluded background — signature amorphous-target failure mode. |
| w14p1c-022 | Refraction-induced background warp as the strongest transparent-object cue, and ViTs nearly blind to it — deep representational-gap claim. |
| w14p1c-024 | Two-axis failure taxonomy (glass fails interior, smoke fails boundary) predicting which fix works — unifying framework for the shard. |
| w14p1c-041 | Binary masks as a *category error* for smoke; matting formulation wins even on binary IoU — task-reformulation contrarianism; converges with w14A-091. |
| w14p1c-044 | Frozen dehazing network's transmission map as a zero-training smoke segmenter — embarrassing-baseline attack on the subfield. |
| w14p1c-051 | Thresholded temporal-variance map beats zero-shot SAM on static cameras — the skipped trivial baseline; audit value high. |
| w14p1c-057 | IoU and alarm latency nearly uncorrelated — the field's metric does not measure the product objective; deployment-critical. |
| w14p1c-078 | SAM-mined failures transfer across other vision foundation models — turns failure mining into transferable science about shared pretraining blind spots. |
| w14p1c-084 | Active-learning acquisition logic inverts on amorphous targets (most-ambiguous labeling is harmful) — contrarian against AL orthodoxy. |
| w14p1c-118 | Standard weather augmentation is label poison for smoke training (injects unlabeled positives into negatives) — failure of a common practice. |
| w14p1c-121 | Auto-exposure makes fires self-hiding — system-level failure invisible to model-centric research; alarm latency governed by camera policy. |

## 2. Cross-worker convergence (8 flags — dual-signal: value AND dedup risk)

Independent shards converging on one hypothesis both raises its prior and creates consolidation-time duplication risk. The consolidator should merge each family into one canonical idea with domain-specific instantiations, not admit N near-clones into `ideas_master.jsonl`.

| family | members (worker-spanning) | note |
|---|---|---|
| Prompt-perturbation sensitivity as a diagnostic/uncertainty signal | 11 ideas: w14A-010/057/081/123, w14_p1b_005/037/069, w14p1c-001/010/061/083 | Largest convergent family; strongest dedup target. |
| Confidence / IoU-head miscalibration inversion | 18 ideas: w14A-010/012/056/125, w14_p1b_002/008/017/058/067/070/076, w14p1c-002/026/047/060/062/064/065 | Same core phenomenon ("confident where wrong") instantiated per domain. |
| Patch/tokenization resolution floor for small/thin targets | w14A-021, w14_p1b_061, w14_p1b_062, w14p1c-105 | Identical architectural-floor hypothesis in 3 domains; merge into one testable law. |
| Multimask/ambiguity-distribution collapse | w14A-054, w14A-059, w14_p1b_003, w14p1c-009 | Same "hypothesis diversity collapses" claim from 3 angles. |
| Token pruning/merging preferentially discards rare targets | w14A-073, w14_p1b_035, w14p1c-109 | Near-identical hypothesis; note w14A-073 claims the *opposite sign* (pruning as regularizer) — a designed disagreement worth preserving. |
| Negation blindness in text-guided segmentation | w14_p1b_122, w14p1c-092 | Same failure, two domains. |
| Annotation convention / rater style dominates model differences | 21 ideas incl. w14_p1b_112/115, w14p1c-039/068/072, w14A-063 | Healthy convergence but heavy overlap; consolidator should keep the sharpest 3–5 variants. |
| Benchmark contamination / leakage | w14_p1b_097/100/102/105/106, w14p1c-073, w14A-063 | Coherent meta-science family; w14_p1b_106 (lesion-vs-organ contamination asymmetry) is the most distinctive member. |

## 3. Mode-collapse risks (4 flags)

1. **Genre monoculture — audit/measurement studies dominate.** A large majority of ideas are "measure X / expose Y / audit Z" diagnostics (85 ideas use "measurable", 52 "audit", 38 "predictable"); Worker B is nearly 100% audit-genre. Constructive contributions (new architectures, new task formulations, new datasets/benchmarks as artifacts, new training objectives) are underrepresented outside Worker A's `novel_peft_mechanism` cluster and scattered C entries. Wave-2 generators should be explicitly steered toward constructive/method genres or the final portfolio will skew toward negative-result papers.
2. **Single-model anchoring on SAM.** Worker A is 100% SAM/SAM2 by design, but Worker C also anchors most prompt/failure ideas on SAM, and Worker B's "foundation models" are functionally SAM-shaped (promptable, IoU-head, multimask). Other segmentation foundation lineages (self-supervised DINO-style features, text-driven segmenters, generative/diffusion segmenters, 3D-native models) appear only incidentally. Portfolio risk: results age with one model family.
3. **Recurring rhetorical templates.** High-frequency generative templates detected: "X is measurable/predictable" (~120 ideas), "free / zero-cost signal" (24), "linearly decodable" (5), "scaling/power law" (7), calibration-framing (67). Lexical near-duplicate analysis found no pair above Jaccard 0.28 (surface diversity is genuinely good), but the *template-level* repetition means wave-2 generation from the same prompts risks true collapse. Recommend giving wave-2 generators the template list as a negative constraint.
4. **Uncertainty/calibration overweight.** Three separate `uncertainty_calibration` clusters (A:6, B:12, C:8 = 26 ideas) plus the 18-idea confidence-inversion family ≈ 10% of the corpus on one theme. Cap this theme at consolidation.

## 4. Missing territories (10 flags — input for wave-2 dispatch)

Not covered (or only incidentally touched) by the three shards:

1. Remote sensing / aerial / satellite / SAR segmentation (only a passing mention in w14A-095).
2. Autonomous driving and 3D: LiDAR / point-cloud / mesh / neural-field (NeRF, Gaussian-splat) segmentation.
3. Microscopy / histopathology gigapixel WSI segmentation (Worker B is radiology-centric: CT/MR/US only).
4. Industrial defect & anomaly segmentation; agriculture; underwater imagery.
5. Video object segmentation science beyond SAM2 memory (streaming/online segmentation, long-horizon tracking); only 3 SAM2 ideas in A plus C's domain-specific temporal cluster.
6. Instance / panoptic / open-vocabulary panoptic task-formulation science (open-vocab appears only in C's smoke-confusion cluster).
7. Fairness and demographic bias (skin tone in dermatology, demographic shift in radiology; w14_p1b_052 touches pediatric scale only).
8. Adversarial robustness and safety certification beyond w14A-106/107; no adversarial ideas at all in B or C despite safety-critical domains.
9. Amodal segmentation and occlusion reasoning as a first-class topic (only w14p1c-038 incidentally).
10. Annotation economics at scale: labeling-cost models, human-in-the-loop pipelines, dataset curation/pruning for segmentation pretraining (touched by w14A-101/103 and w14p1c-042 but not owned by any shard).

## 5. QA issues for the consolidator (3 flags)

1. **Inconsistent `id_seed` schemes** across shards (`w14A-###`, `w14_p1b_###`, `w14p1c-###`). Normalize at merge; preserve original ids as provenance.
2. **Unverified-novelty phrasing.** 20 ideas contain "has never been measured/isolated" or "nobody has quantified" (e.g., w14A-009, w14A-041, w14_p1b_126, w14p1c-001). These are unverified absence-of-literature assertions made without search; the consolidator must downgrade them to "we did not verify prior work" and must not propagate them into `ideas_master.jsonl` as fact. Fields `why_possibly_novel` are generally hedged ("appears unexamined") — acceptable — but `problem` fields sometimes state absence as fact.
3. **Uniform `evidence_status: HYPOTHESIS` (382/382).** Correct and honest — but the consolidator must not infer any evidence gradient from this field; ranking must come from judge flags, not evidence_status.

## Counts

- Ideas reviewed: 382 (A:132, B:126, C:124)
- High-value flags: **36** (12 per worker)
- Collapse-related flags: **12** (8 cross-worker convergence/dedup + 4 mode-collapse risks)
- Missing-territory flags: 10
- QA flags: 3
- Total flag records in `judge_C.flags.jsonl`: 61

## Recommended next task

`p1_wave1_consolidator` — merge the three shards into `ideas_master.jsonl`, reconciling Judge A/B/C flags, deduplicating the 8 convergence families, normalizing id schemes, and carrying the missing-territory list into wave-2 generator dispatch.
