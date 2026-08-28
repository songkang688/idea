# gen_n_scaling_memorization_data_laws — P1 Wave A shard (Windows13)

- **task_id:** p1_gen_n_scaling_memorization_data_laws
- **generator_id:** gen_n_scaling_memorization_data_laws
- **wave:** p1_wave_a_w3
- **id range:** W13-P1-N-001 .. W13-P1-N-100 (100 ideas)
- **novelty_status:** unverified (generation only; Wave B dedup + novelty verification pending)
- **queue source:** origin/cursor/p1-diversity-audit-consolidator-w1-25a0 `Windows13/_state/tasks/p1/diversity_audit_w1/decision.json`, priority-6 entry

## Territory

Scaling-law science of vision foundation models; memorization/privacy in discriminative/dense vision models; real-pretraining-data composition effects; contamination science as mechanism (not eval-critique); emergence at mechanism level (per Auditor C's request). Every idea names a data-level or scale-level intervention as the manipulated variable.

## Clusters (10 distinct, max 12% of shard)

| cluster | count | ids |
|---|---|---|
| model-compute-scaling-laws | 11 | N-001..N-011 |
| dense-transfer-scaling | 11 | N-012..N-022 |
| real-data-composition-laws | 12 | N-023..N-034 |
| repetition-and-unique-data | 9 | N-035..N-043 |
| emergence-mechanisms | 9 | N-044..N-052 |
| memorization-in-discriminative-models | 12 | N-053..N-064 |
| membership-inference-vision-fm | 10 | N-065..N-074 |
| dense-feature-privacy | 9 | N-075..N-083 |
| contamination-mechanism | 9 | N-084..N-092 |
| scaling-breakdowns-anomalies | 8 | N-093..N-100 |

## Genre mix

- constructive_capability: 25 (25%)
- characterization_law: 67 (67%)
- audit_debunk: 8 (8%, well under the 40% ceiling)

## Guard compliance (self-audit)

- **Anti-overlap with gen_f (synthetic data):** no synthetic-data-generation or curation-pipeline framings; the single occurrence of the word "synthetic" in the shard (N-043) is the phrase "synthetic duplication constructions", meaning controlled resampling of real images, not generated data. Occupied gen_f IDs (F-045, F-051, F-057, F-060, F-086, F-093, F-097, F-098, F-101) checked and not restated: all repetition/economics ideas here are synthetic-free (e.g., N-041 prices collection-vs-repetition of real data, with no synthetic arm, unlike F-101).
- **Manipulated variable:** every `family_fingerprint.manipulated_variable` is a data-level (composition, duplication, injection, resampling, share, redaction, release policy) or scale-level (model size, data size, compute, resolution, depth fraction) intervention.
- **SAM cap:** 1/100 records SAM/SA-1B-subject (N-020) = 1% <= 5%.
- **Calibration/uncertainty:** not a cluster; the token "calibrat-" does not appear in the shard.
- **Scattering-media ban:** no smoke/fire/fog/transparent/amorphous-scattering examples anywhere.
- **F1-F5 framings:** no PEFT-factorial-on-SAM, no SAM-component pathology, no internal-score-as-free-detector, no cue-ablation on scattering organisms, no published-deltas-are-noise primary framing (N-004 targets functional-form degeneracy of scaling fits, a different mechanism-level claim).
- **Segmentation-metric independence:** 99/100 falsification experiments do not depend on segmentation/mask metrics (only N-020, whose subject is the mask-supervised data axis itself).
- **Existing-master collisions checked:** C-023/C-024/C-059/C-069/C-102, B-029, E-070, G-071, K-100, H-043/H-098 reviewed; contamination ideas here are controlled-injection mechanism studies, not audit/eval-critiques; emergence ideas are mechanism/forecasting-level, not metric-artifact restatements; no restoration/SR memorization (gen_h), no diffusion-generator memorization (gen_j), no video/3D subjects (gen_k), no LLM-loop subjects (gen_l), no within-run optimizer/objective manipulations (gen_m), no TTA/efficiency (gen_q), no domain-shift-adaptation framings (gen_g).
- **Quality gates:** 100/100 falsifiable predictions carry an explicit numeric kill threshold and a "falsified if" clause; 100/100 structured evidence labels include prior_work_basis; 99/100 fastest-falsification experiments have a single-GPU time bound on public data (N-020 flagged needs_special_resources=true); no fabricated citations, datasets, or results — all prior-work mentions are well-known work labeled as unverified model recall.

## Sub-cluster one-line map

1. **model-compute-scaling-laws:** vision compute-optimal ratio vs language; resolution as third scaling axis; tokens-vs-params; functional-form degeneracy of published fits; Zipf-tail sets the data exponent; curve-fit pilots beat endpoint pilots; transfer ossification; N-vs-D error decomposition; transfer-optimal allocation shift; granularity sets exponents; architecture changes constants not exponents.
2. **dense-transfer-scaling:** upstream-downstream correlation knee; frozen-vs-finetuned gap law; dense-transfer exponent atlas; semantics scale faster than spatial precision; rare classes ride the data axis; pretraining-data-for-labels substitution law; small objects need resolution not scale; resolution-schedule confound audit; mask-data boundary-vs-region exponents (SAM-subject); generic-vs-specialized crossover forecasting; decoder scaling is dead compute.
3. **real-data-composition-laws:** mixture scaling law for real sources; text-in-image share drives OCR behaviors; geographic-share frontier; scene-vs-object-centric ratio; effective size = unique-cluster count; caption-specificity leverage; shared-exponent per-concept law; corpus scale-histogram prior; vintage decay law; people-share utility-vs-privacy decoupling; co-occurrence dose for contextual bias; log-additive mixture effects.
4. **repetition-and-unique-data:** vision repetition tolerance vs language lore; augmentation as scale-decaying data multiplier; targeted tail repetition; epochs buy fit, unique data buys coverage; one-epoch folklore is wrong; dedup hurts fine-grained tasks; collection-vs-repetition break-even rule; memorization onset precedes utility loss; duplication-spectrum effective-sample-size formula.
5. **emergence-mechanisms:** onsets set by exemplar counts; probe precursors forecast behavioral onset; attention-grouping as percolation; binding gated by decorrelated pairs; decomposability predicts abruptness; geometric early-warning signatures; universal data-determined onset order; exposure-vs-capacity classification of onsets; memorization-emergence vs generalization-emergence.
6. **memorization-in-discriminative-models:** deja-vu memorization capacity scaling; duplication dose-response knee; pre-training memorization risk prediction; region-level memorization in dense models; detector replay of memorized instances; forgetting-law scheduling mitigation; late scale gains are similarity-concentrated; supervised-vs-SSL memorization dissociation; persistence through fine-tuning; dosimetry canary standard; augmentation privacy frontier; incidental-bystander memorization and blurring.
7. **membership-inference-vision-fm:** capacity-to-data risk collapse; structured outputs leak more; low-FPR vulnerable tail; shadow-free audits from data statistics; cross-crawl membership transfer; distillation leaks teacher membership; joint-scaling risk inversion; collection-level audits; member/non-member distribution-mismatch audit; user-level exposure curves.
8. **dense-feature-privacy:** invertibility grows with scale; global-embedding linkage; redact-then-encode fails; features as location beacons; feature-release privacy frontier; split-inference depth-leakage law; output-only extraction from dense models; retroactive embedding-privacy decay; similarity-graph de-anonymization.
9. **contamination-mechanism:** dose-response inflation law; semantic-vs-exact inflation grows with scale; generalization halo; unlabeled transductive contamination; contamination half-life by stream position; memorization capacity per parameter; channel-dependent persistence through fine-tuning; caption-side vocabulary contamination; contamination as free rider in scaling exponents.
10. **scaling-breakdowns-anomalies:** vision inverse-scaling suite; movable U-shaped troughs; resolution floors collapse class exponents; tail exhaustion forecasting; nonstationary loss-to-capability exchange rate; slice-heterogeneous exponents; breaks are data-determined; minority-domain non-monotonicity under fixed mixture.
