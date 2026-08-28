# P1 Wave A Generator Report — batch_001 / gen_A (Windows15)

- Task: `p1_wave_a_batch001_gen_A`
- Role: generator (shard writer only — canonical `ideas_master.jsonl` untouched)
- Territory: **T01 SAM / Foundation Model adaptation / PEFT**
- Idea count: **100** (target 100; accepted range 80–120)
- ID range: `W15-B001-A-001` … `W15-B001-A-100` (contiguous, unique, validated)
- Output: `Windows15/_state/tasks/p1/batch_001/gen_A/ideas.jsonl` (one JSON object per line)

## Scientific bar applied

Every idea is framed as a distinct falsifiable hypothesis — a new observation, scientific question, failure mode, ignored assumption, counter-intuitive prediction, or systematic foundation-model defect. Explicitly avoided: module-A+B combinations, attention/loss/backbone swaps, blind method transfer to medical/smoke, more-params/data/compute proposals, and architecture engineering without a hypothesis. The few ideas touching architecture components (e.g., upsampling path, positional encodings) are framed as **error-budget / gap-localization measurements**, not as engineering proposals.

Each idea carries all 13 required fields, including `community_default_belief`, `why_that_may_be_wrong`, and `fastest_falsification`. `why_possibly_novel` is tagged `[HYPOTHESIS]` in every idea — **no verified-novelty claims anywhere** (checked programmatically).

## Evidence-class discipline

Factual claims inside idea fields are tagged inline with `[KNOWN FACT]`, `[VERIFIED PRIOR WORK]`, `[HYPOTHESIS]`, or `[MODEL SPECULATION]`. Only high-confidence prior work is named (SAM/SA-1B, SAM 2/Hiera, LoRA, BitFit-style bias tuning, VPT-style visual prompting, DoRA, MedSAM, SAMed, HQ-SAM, model soups/task arithmetic, Geirhos-style cue-conflict, intrinsic-dimensionality analyses). No invented citations, no invented benchmark numbers, no invented datasets, no claimed experimental results. Quantities in `falsifiable_prediction` fields are predictions, not reported results.

## Cluster map (12 clusters, 100 ideas)

| Cluster | Ideas | Theme |
|---|---|---|
| prompt_geometry | 001–010 (10) | Prompt-space defects: click-position granularity prior, box-as-scale-oracle, sub-patch aliasing, negative-click asymmetry, refinement limit cycles, dataset-prior ambiguity resolution, semantics in prompt tokens, prompt-tuning sufficiency, jitter-variance hardness, everything-mode sampling blind spots |
| peft_mechanism | 011–022 (12) | Where/how PEFT acts: update-location signatures of shift type, intrinsic task rank, init lottery, circuit reuse vs creation, first-layer modality gap, LN-only sufficiency, decoder vs encoder for conventions, gradient-conflict stability, rank-vs-regularization, LR-artifact audits of variants, rank prediction from unlabeled data, merge-interference certificates |
| capability_erosion | 023–032 (10) | What PEFT destroys: multimask-diversity collapse, calibration-first forgetting, part/whole loss, interference-by-similarity, boundary-sloppiness transfer, shallow-displacement forgetting, click-integration loss, texture-cue drift, learns-less/forgets-less crossover, cheap IoU-head repair |
| perceptual_defects | 033–044 (12) | Systematic SAM defects: no amodal completion, boundary snapping, tokenization-limited thin structures, annotator-morphology inheritance, polarity bias, noise-vs-blur asymmetry, transparency-as-convention, density ceilings, shadow binding, pre-prompt failure prediction, camouflage re-attribution, large-object brittleness |
| gap_localization | 045–050 (6) | Where the domain gap lives: encoder sufficiency for medical, convention portability via decoder, divergence-profile-prescribed placement, compute-starvation law, upsampling error budget, IoU-head as domain (not instance) meter |
| data_efficiency | 051–060 (10) | Adaptation data science: few-shot power law, coverage selection, rank-as-noise-filter, prompt-diversity budget axis, self-training plateau mechanism, box-workflow sufficiency, anti-curriculum, patient-leakage inflation, augmentation-rank exchange, disagreement-based acquisition |
| ambiguity_uncertainty | 061–067 (7) | Uncertainty as first-class: annotator-disagreement prediction, overconfidence as gap meter, jitter ensembles vs learned head, uncertainty-only adaptation, ambiguity conservation, aleatoric/epistemic split, runner-up dataset auditing |
| evaluation_methodology | 068–075 (8) | Literature defects: LR-confound audit, metric fragility, under-prompted baselines, box-prompt leakage, statistical power, missing frozen-feature null, matched-compute collapse, benchmark redundancy |
| counterintuitive_peft | 076–084 (9) | Counter-intuitive results: random-encoder control, foundation-model tax, soups-beat-rank, sign-only updates, three-timescale training, input-space-only adaptation, subtractive gating, PE-only scale fixes, prompt-consistency test-time adaptation |
| pretraining_provenance | 085–091 (7) | SA-1B defects: bootstrap error monoculture, mask-count prior, capability anisotropy vs content frequency, aesthetic-curation bias, convention-conflict active learning, privacy-blur shortcut learning, redundancy/coverage-vs-count |
| cross_modal_physics | 092–097 (6) | Physics-of-imaging gaps: speckle decomposition (ultrasound), 1-D thermal gap, pathology scale-lessness, depth-beats-RGB in clutter, coherence-supervised CT adaptation, orientation prior in remote sensing |
| peft_lifecycle | 098–100 (3) | Deployment lifecycle: LoRA re-basing across model generations, order-dependence of sequential adaptation, training-free domain routing |

## Notes for the Wave B dedup consolidator

- Several ideas intentionally reference each other as linked-but-distinct hypotheses (e.g., 009→050/055/063, 008→060/067/081, 012→059/078/079, 013→078/099, 022→099, 040→086, 037→093, 038→092/095, 083→097). Each has a distinct core hypothesis and falsification; they should not be collapsed on keyword overlap alone.
- Highest cross-generator collision risk is with T02 (Medical segmentation) for ideas 045, 056, 058, 061, 092–096 — these are framed from the SAM/PEFT mechanism side, but check gen_B's shard for medical-side duplicates.
- Evaluation-methodology ideas (068–075) are territory-adjacent to T07 (benchmark weaknesses) and T11 (negative results); flagged for batch_003/004 dedup awareness.

## Unresolved items

1. SA-1B privacy-blurring detail (used in idea 090) is tagged `[VERIFIED PRIOR WORK]` from the dataset's release documentation as remembered; a downstream verifier should confirm before that idea advances.
2. Cross-generator dedup against gen_B (T02) and gen_C (T03) shards is out of scope for a generator and left to `p1_wave_b_dedup_batch001`.
3. No novelty verification performed (by design): all `why_possibly_novel` fields are hypotheses; a P2-stage novelty check against literature is required before any idea is promoted.
