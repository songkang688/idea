# P1 Wave A (wave 2) — worker_C (Windows14)

- **Task:** `p1_gen_w2_c` (Stage P1 Massive Idea Exploration, Wave A generator, wave 2)
- **Territory:** Negative results + contrarian (things the community believes that may be false; published-method non-replication hypotheses; anti-scaling claims). Fairness/bias (JC-MT-07) and adversarial robustness (JC-MT-08) used as contrarian substrates per task notes.
- **Status:** complete
- **Window lock:** verified before writing — `Windows14/_state/window.lock.json` has `locked: true`, `windows_id: Windows14`, `windows_path: Windows14`. No Windows directories created, no numbering scan performed. `ideas_master.jsonl`, `research_state.json`, and `window.lock.json` were **not** touched.

## Output

- `Windows14/_state/tasks/p1/wave2/worker_C.ideas.jsonl` — **130 candidate ideas**, one JSON object per line.
- Every object carries the same 15-field schema as the wave-1 shards: `id_seed`, `one_line`, `cluster`, `problem`, `core_hypothesis`, `falsifiable_prediction`, `why_important`, `why_possibly_novel`, `minimal_falsification_experiment`, `main_risk`, `territory`, `evidence_status="HYPOTHESIS"`, `default_community_belief`, `why_it_might_be_wrong`, `fastest_falsification`.
- Machine-validated: all 130 lines parse as JSON, all 15 fields non-empty, no extra fields, ids `w14w2c-001` … `w14w2c-130` sequential with no duplicates, shard-unique prefix `w14w2c-` (JC-QA-01).
- Canonical ledger untouched; sibling shards (`worker_A`, `worker_B` under wave2) not written or modified.

## Generation stance

Every idea is framed as a contrarian or negative-result claim with three mandatory components: (1) `default_community_belief` — what the community currently treats as true; (2) `core_hypothesis` / `why_it_might_be_wrong` — why the belief may be false and how the contrarian claim itself could be refuted; (3) `fastest_falsification` — the cheapest experiment that could kill the claim. Per judge_C JC-MC-01, pure diagnostics/audit-genre ideas were minimized: benchmark-hygiene and metric claims (clusters `metric_belief_reversals`, parts of `data_quantity_myths`) each carry a constructive deliverable (a protocol, a corrected allocation rule, a decision rule, or a reusable evaluation artifact), not just an audit. Uncertainty/calibration was deliberately **not** used as a primary territory (capped per JC-MC-04); no idea has calibration as its main subject.

Numbers inside `falsifiable_prediction` fields are predicted thresholds (falsifiable commitments), not reported results. No papers, citations, datasets, or experimental outcomes were fabricated; well-known public benchmarks (ADE20K, Cityscapes, COCO-Stuff, LVIS-style long-tail sets) are referenced only as places to run experiments. Where adjacent VERIFIED PRIOR WORK plausibly exists (emergence-as-metric-artifact in language models, scratch-training for detection, streaming perception for detection, recipe-matched CNN/ViT comparisons for classification, anonymization studies), it is explicitly flagged inside `why_possibly_novel` and the segmentation/dense-specific claim is marked as the unverified HYPOTHESIS. **No literature search was performed; every novelty claim is an unverified hypothesis.**

## Cluster map (13 clusters, 130 ideas)

| cluster | n | ids | focus |
|---|---|---|---|
| anti_scaling_dense | 10 | 001–010 | resolution-confounded scaling curves, dense-vs-classification data saturation decoupling, boundary anti-scaling, long-tail anti-scaling, emergence-as-metric-artifact, specialists-vs-generalist, protocol-bias annotation asymptote, over-pretraining, resolution as missing compute axis, ensembles-beat-scale OOD |
| nonreplication_method_families | 12 | 011–022 | boundary losses, mask-classification heads, TTA vs FLOP-matched inference, deep supervision, CRF/refinement flip point, plug-in modules, curricula, OHEM/rebalancing redundancy, self-distillation accounting, frequency-module compression shortcuts, contrastive-vs-MIM compute matching, DG-over-strong-aug |
| pretraining_transfer_myths | 10 | 023–032 | scratch-training crossover, SSL frozen-vs-finetune, depth negative transfer, linear-probe misranking, stuff-class VFM blind spot, protocol-vs-semantic transfer, frozen-backbone OOD collapse, video-pretraining null, taxonomy-conflict regressions, task-arithmetic breakdown |
| adversarial_robustness_contrarian | 12 | 033–044 | Lp-vs-physical proxy failure, gradient-masking inflation, vacuous boundary certification, weak dense transfer, epsilon-artifact tradeoff, synthetic-vs-real corruption misprediction, temporal aggregation vs patches, augmentation-vs-AT, natural dense robustness, region-targeted detector blindness, robustness non-transfer, prompt-agnostic attacks |
| fairness_bias_contrarian | 12 | 045–056 | photometric skin-tone gaps, annotation-quality vs rebalancing, boundary-disparity shell game, layout-vs-appearance geographic gaps, convention-flipped gaps, DRO noise amplification, clothing-contrast dominance, anonymization null, underpowered tradeoffs, scanner confounds (medical), generative-rebalancing backfire, benchmark-composition gaps |
| data_quantity_myths | 10 | 057–066 | repair-vs-collect, dedup effective size, dense-specific pruning, granularity-vs-count, cost-normalized sparse labels, balancing units, hard negatives, session leakage re-splits, verify-and-correct quality, head-boundary bottleneck for tail |
| augmentation_myths | 10 | 067–076 | pipeline-narrowing photometric aug, copy-paste boundary corruption, multi-scale redundancy, flip harm on oriented classes, color-jitter vs color-defined classes, consistency-as-ensembling, strength-vs-scale decay, elastic deformation null (medical), TTA per-image regressions, learned-policy negative transfer |
| architecture_narrative_reversals | 10 | 077–086 | recipe-artifact transformer verdict, skips-as-edge-carriers, dilation obsolescence, windowed-vs-global class taxonomy, decoder-first allocation, query shape memorization, positional layout shortcuts, guided-upsampling vs full resolution, normalization dominance, FPN redundancy regime |
| video_temporal_myths | 8 | 087–094 | consistency smoothness-accuracy trade, memory anti-scaling, flow propagation crossover, VOS protocol-bound rankings, frame-rate shortcuts, streaming rank inversions, per-frame + smoothing vs video architectures, propagation annotation savings accounting |
| weak_semi_supervision_myths | 10 | 095–104 | self-training gain decay, shifted unlabeled pools, CAM fair-tuning compression, tail erosion under confidence thresholds, unlabeled anti-scaling, AL-vs-random with modern init, correction-data fixed point, point-parity class structure, unlabeled-test leakage, foundation-teacher bias ceiling |
| metric_belief_reversals | 8 | 105–112 | GT noise floors vs leaderboard deltas, per-image regression rates, region-vs-boundary rank flips, small-object noise threshold, PQ recognition dominance, zero-shot contamination, taxonomy-mapping sensitivity, human-vs-mIoU preference |
| vlm_openvocab_contrarian | 10 | 113–122 | name-frequency prediction, decorative text heads, language-scale grounding null, relation blindness, nameability-vs-segmentability, template non-transfer, in-context appearance matching, negation scale-wall, synonym leakage / coined categories, agents-vs-end-to-end crossover |
| efficiency_compression_contrarian | 8 | 123–130 | quantization boundary damage, task-structured prunability, distillation error correlation, token-pruning small-object deletion, dynamic-compute misallocation, efficient-attention dense failure, resolution knees, compression-robustness interaction |

## Unresolved items (for downstream waves)

1. **No novelty verification performed** — every `why_possibly_novel` is an unverified hypothesis; Stage 2 must dedup against sibling shards and, later, against literature. Ideas explicitly flagging adjacent VERIFIED PRIOR WORK: 005 (emergence-as-mirage, LMs), 023 (scratch detection training), 052 (anonymization studies), 064 (classification test-set leakage), 077 (recipe-matched CNN/ViT for classification), 092 (streaming perception for detection).
2. **Expected cross-shard adjacency, flagged in-line:** 022 and 096 touch domain shift (wave2 worker_A territory); 055 touches synthetic data (worker_A); 054 and 074 use medical substrates (wave1 worker_B); 044 and 104 touch SAM/promptable models (wave1 workers A/C); 122 anticipates wave-3 LLM/agent territory. All are framed as negative-result/contrarian claims, but Wave B dedup should check them against those shards.
3. **Intra-shard near-neighbors to watch during dedup:** 002 vs 058 (data-scaling vs dedup effective size), 013 vs 075 (both TTA; FLOP-matching vs per-image regressions), 030 vs 090 (video pretraining vs VOS protocol), 064 vs 103 (train/test leakage vs unlabeled-pool leakage), 003 vs 123/128 (boundary-metric degradation under scale vs under compression), 007 vs 105 (protocol bias vs GT noise floor).
4. **Calibration-cap compliance:** no idea uses uncertainty/calibration as its primary subject; ideas 098 and 127 mention confidence signals only as mechanisms inside non-calibration claims. If Stage 2 judges disagree, those two are the ones to re-inspect.
5. Several minimal experiments share infrastructure (dual-protocol re-annotation, boundary-metric harness, matched-compute pretraining pairs, public-checkpoint zoo re-scoring); a consolidator could factor these into shared experimental platforms.

## Recommended next task type

`p1_wave_B_dedup` — merge/dedup the wave-2 shards (worker_A, worker_B, worker_C, and any additional shards) against each other and against the 366 accepted wave-1 ideas before any acceptance into `ideas_master.jsonl`.
