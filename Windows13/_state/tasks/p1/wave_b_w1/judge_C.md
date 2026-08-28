# P1 Wave B — Judge C: Adversary / Audit / Anti-Mode-Collapse (Wave 1: Generators A+B+C)

- **task_id:** `p1_wave_b_w1` | **role:** `judge_C_adversary` | **windows_id:** `Windows13` (windows_path `Windows13`, window_locked `true`)
- **branch:** `cursor/p1-wave-b-judge-c-adversary-5030`
- **Scope:** adversarial audit of the 302 wave-1 generator ideas: mode-collapse and template detection, non-falsifiability and fake-novelty-tone attacks, missing-field audit, independent keep/merge/kill, and explicit protection of high-value contrarian anomalies. Canonical state (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched. A later Consolidator writes canonical state.
- **Independence:** verdicts were formed from the generator shards. `judge_A` output was read only after this judge's dispositions were drafted (format conventions and the divergence notes in section 9). Judge B output did not exist on the remote at judging time (searched for `p1-wave-b-judge-b*` refs); judged without it.
- **Epistemic status:** NO novelty is verified for any kept idea. Every prior-art remark is this judge's unverified hypothesis. No citations were invented.

## 1. Inputs

| Shard | Branch | Ideas |
|---|---|---|
| gen_a_sam_foundation_peft | `cursor/p1-gen-a-sam-foundation-peft-c8d4` | 102 (W13-P1-A-001..102) |
| gen_b_hard_domain_dense_prediction | `cursor/p1-gen-b-hard-domain-a13a` | 96 (W13-P1-B-001..096) |
| gen_c_contrarian_eval | `cursor/windows13-p0-init-implementation-d93f` | 104 (W13-P1-C-001..104) |
| **Total** | | **302** |

All 302 lines parsed; ids contiguous and unique per shard.

## 2. Method (attack passes)

1. **Field audit:** every idea checked for all 12 required fields, including `community_default_belief`, `why_it_might_be_wrong`, `fastest_falsification_experiment`; scans for fabricated citations and unhedged novelty tone.
2. **Template extraction:** meta-templates identified within and across shards (SAM+X, LoRA+X, loss+X, cue-ablation, hidden-variance-term, shortcut-solvable-benchmark, reweighting-instability, scale-null, convention-decodability, and others); families consolidated to paradigm primaries.
3. **Falsifiability and tone attack:** existence claims, measurement protocols dressed as hypotheses, strawman community beliefs, and hedged restatements of famous critiques flagged or killed.
4. **Anomaly protection:** unusual, contrarian, non-template ideas explicitly shielded from consolidation pressure.

Merge rule: two ideas fold only when they assert the **same mechanism testable by one experimental design**. Substrate permutations (swap the domain, metric, or technique slot) do not count as distinct hypotheses.

## 3. Verdict counts

| Quantity | Value |
|---|---|
| Input total | 302 (A: 102, B: 96, C: 104) |
| **Keep (accepted candidates this wave)** | **241** (A: 88, B: 83, C: 70) |
| Kill (outright) | 9 (A: 3 — A-077, A-085, A-089; C: 6 — C-016, C-036, C-055, C-059, C-062, C-104) |
| Merge (fold into a kept primary) | 52 (A: 11, B: 13, C: 28) |
| Template families flagged | 20 |
| Cross-shard mode attractors | 10 |
| High-value anomalies protected | 23 |

Machine-readable lists (keep_ids, kill_reasons, merge_map with targets and reasons, families, watchlists) are in `judge_C.json`; the kept candidates with per-idea flags are in `accepted_shard_C.jsonl`.

## 4. Mode-collapse findings (the adversary's main deliverable)

**4.1 Quota-uniformity signature.** gen_b emitted exactly 8 ideas in each of its 12 clusters. That regularity is a quota-filling signature, and it shows: inside several clusters the ideas are one experimental paradigm instantiated across cues or domains (see tf06, tf07 below).

**4.2 The 20 template families.** Full membership and dispositions in `judge_C.json → template_families`. The load-bearing ones:

- **tf10 hidden_variance_term (18 ids, worst offender, mostly shard C + A-072, B-038):** "unbudgeted variance source V rivals claimed effect sizes." Sixteen near-isomorphic instantiations (preprocessing, decode libraries, resolution, TTA, parser, normalization, prompt wording, support draws, seeds, power, harness, heads…). Consolidated to 7 primaries: C-073 (statistical-noise umbrella), C-077 (harness/protocol umbrella), C-045 (hidden search budget), C-054 (seed lottery), C-048 (head confound), C-025 (label error), A-072 (SAM prompt-protocol arm).
- **tf11 shortcut_solvable_benchmark (10 ids, shard C):** "ablate an input channel; benchmark still solved." Kept one primary per ablation paradigm: C-090 (image swap), C-091 (expression-blind), C-092 (transcription equalization), C-095 (single-input sufficiency, absorbing C-094), C-096 (prior decorrelation), C-089 (blind language priors, absorbing C-030).
- **tf04 sam_plus_x_ports (15 ids, shard A):** the definitional SAM+X collapse. Killed A-077 (typographic immunity — no held belief attacked), A-085 (early exit), A-089 (adaptation curriculum); merged A-074, A-094. Survivors (task arithmetic A-021, VPT A-022, registers A-039, cue-conflict A-035, subspace angles A-088, score-router A-086, …) carry mandatory prior-art flags — each is kept only because it states a falsifiable SAM-specific mechanism beyond "port X".
- **tf03 silent_capability_erosion (12 ids, shard A):** "adaptation silently destroys capability X." The shard's biggest attractor. Merged A-019→A-099 and A-064→A-015; the rest survive because the destroyed capabilities and mechanisms genuinely differ.
- **tf06 cue_ablation_shortcuts (10 ids, A+B):** one intervention paradigm × cues (specular highlights, saturation, haze statistics, compression, blur, context, intensity, texture). Merged B-041→B-048, B-046→A-035.
- **tf01 recalibration_not_relearning (5 ids, shard A):** one hypothesis — "domain gap is low-order photometric drift" — wearing four method costumes (histogram matching, BitFit, LayerNorm re-estimation, learned input stem). Kept the input-side and weight-side primaries (A-011, A-018), merged A-098, A-100.
- **tf12/tf16/tf17 (reweighting instability, distributional ground truth, contamination):** shard C's remaining big three; consolidated to 2, 3, and 7 primaries respectively.
- **tf15 scale_nulls (6 ids, shard C):** "X provides nothing at foundation scale once controlled" (SSL advantage, calibration-from-scale, curation, CoT, distillation, feature mixing). All kept — contrarian nulls are valuable and the techniques are distinct — but flagged as a single stylistic template whose members each need a sweep of existing controlled studies before Stage 2.
- **tf20 known_critique_restatement (8 ids, shard C, anti-pattern):** hedged restatements of famous critiques. Killed 6 (C-016 OOD-by-low-level-stats, C-036 mIoU-hides-boundaries, C-055 attention-faithfulness, C-059 emergence-as-metric-artifact, C-062 cross-threat non-transfer, C-104 adaptive evaluation), merged 2 (C-030, C-035).

**4.3 Cross-shard attractors (model-level mode collapse).** Ten hypothesis collisions across "independent" generators: bimodal failure (A-071/B-036), seen-shot contamination (A-070/C-024), head-vs-representation (A-014/B-031/C-048/C-087), convention decodability (A-012, A-063, A-095/B-021, B-081, B-085/C-067, C-072), cue-conflict (A-035/B-043, B-046), hidden-variance audits (A-072/B-038/C family), distributional ground truth (B-095/C-035, C-066, C-068, C-101), jitter-as-measurement (A-005/B-026), scale-prior mismatch (A-062/B-028), periodicity fingerprints (A-034, A-043, A-065/B-077). **Consolidator note:** convergence of three generations of the same underlying model is itself a prior-art warning — attractors tend to sit near the field's public discourse.

## 5. Kills (9, with reasons)

| Id | Reason (abridged; full text in judge_C.json) |
|---|---|
| A-077 | No held community belief attacked; immunity follows from the interface definition. SAM+X security permutation. |
| A-085 | Early-exit efficiency literature ported to SAM; the "mechanism" is that literature's premise. |
| A-089 | Generic curriculum permutation; metaphor-level mechanism; combinatorial falsification cost. |
| C-016 | Long-standing OOD-benchmark critique restated without new mechanism or protocol. |
| C-036 | Strawman default belief — the field already uses boundary metrics; manufactured contrarianism. |
| C-055 | Attention-faithfulness debate restated for ViTs; no new falsifiable twist. |
| C-059 | Metric-artifact account of emergence is a known position; the "visual" port changes nothing. |
| C-062 | Cross-threat non-transfer is well documented; the matrix is a replication catalog. |
| C-104 | Adaptive human-in-the-loop evaluation is established practice; no contested belief. |

kill ≠ worthless: several are true and useful statements — they are killed as *research ideas* because the field plausibly already owns them (unverified assessment; the prior-art gate can overturn).

## 6. Audit results

- **Missing fields:** none. All 302 ideas carry all 12 required fields with substantive content, including community_default_belief / why_it_might_be_wrong / fastest_falsification_experiment.
- **Fake citations:** none found. Three gen_a ideas (A-035, A-039, A-077) name real bodies of work (Geirhos cue-conflict, Darcet registers, Goh typographic attacks) inside hedged HYPOTHESIS statements — flagged as a convention risk (named references without a verification pass), not fabrication.
- **Novelty tone:** clean. Zero unhedged novelty assertions across 302 ideas; gen_b prefixes every hypothesis with [HYPOTHESIS].
- **Strawman community beliefs:** the worst cases were killed (C-036, C-104). B-023 is kept but flagged: its stated default belief overstates how much the medical-imaging community still trusts pure overlap metrics.
- **Weak falsifiability (kept, flagged):** B-089 (blind clustering has researcher-degrees-of-freedom risk), B-094 (a measurement protocol, not a hypothesis), C-037 (existence claim — "there exist generator modifications"), C-064 (style-similarity operationalization unclear), C-079 (implicit-query count may be unmeasurable), A-090 ("common operator" is an interpretive leap over a parameter-count result).
- **Compute/hardware flags:** A-032, C-056, C-058 need pretraining-scale compute; B-060, B-071, B-083 need nonstandard sensors.

## 7. Protected anomalies (23)

These are explicitly shielded from consolidation pressure; a risky anomaly with a thin experiment beats a polished template instance. Full protect-reasons in `judge_C.json → anomaly_notes`.

**Shard A (7):** A-031 (boundary/semantic anti-correlation — attacks "segmentation FM = visual FM"), A-044 (relational regions unreachable by prompt-as-locator), A-063 (guideline archaeology — models memorize policy), A-065 (SA-1B grid fingerprint), A-066 (mIoU anti-correlates with interactive usability), A-079 (modal/amodal instability law), A-087 (catastrophic remembering).

**Shard B (11):** B-016 (human-model glass gap as evaluation artifact), B-022 (ambiguity ≠ difficulty, possibly anti-correlated), B-029 (ontological, not statistical, scaling asymptote), B-030 (mass-noun penalty), B-054 (representation-ambiguity matching law), B-060 (polarization information gap vs model gap), B-069 (predict the spread-rate derivative), B-071 (event-camera combustion microdynamics), B-083 (sparse physical labels beat dense human labels), B-090 (ambiguity-type transfer beats domain transfer), B-093 (human-model complementarity largest on hard domains).

**Shard C (5):** C-032 (adaptive overfitting returning in the foundation era — would reverse the replication-era conclusion), C-069 (model-assisted annotation self-preference loops), C-072 (annotation-vendor convention leakage), C-074 (leaderboard winner's curse), C-075 (benchmark ecosystem low effective dimensionality).

## 8. Deliberate tensions kept (not redundancy)

1. **A-014 vs B-031** — the shifted-domain gap lives in the readout (A) vs in the features for hard domains (B). Designed head-to-head; C-048 is the confound-control arm.
2. **A-076 vs B-033** — thresholds hide recoverable competence vs thresholds manufacture fake competence differences. Complementary valences of one pathology.
3. **A-005 vs B-026** — prompt jitter as over-adaptation pathology vs as free ambiguity meter. Same measurement, opposite uses.
4. **A-058 vs B-006** — shape-prior monoculture from model-in-the-loop data vs from human blob priors. Convergent claim, different causal source; let the data decide.

## 9. Divergence from Judge A (post-hoc comparison)

Independent totals land close (241 kept here vs 245 by Judge A) but member-level dispositions differ; the Consolidator should diff the lists rather than assume agreement. Notable divergences: this judge **kills A-077** (Judge A kept it flagged) and **keeps A-086** (Judge A killed it — the zero-parameter router carries a falsifiable competence-signal claim); merges **A-064 into A-015** (general ambiguity-collapse umbrella) rather than into the distillation variant; merges **C-026 into C-023** and **B-088 into C-027** (Judge A kept C-026 separate and folded B-088 the same way); keeps **C-091 and C-096** as distinct ablation paradigms; and merges **C-100/C-076 into C-042** where Judge A's reweighting family drew slightly different lines. Agreements reached independently (bimodality, seen-shot, deterministic-beats-uncertainty, distributional ground truth, head-vs-features tension) should be treated as robust.

## 10. Handoff to the Consolidator

1. Nothing here verifies novelty. The `prior_art_risk_high` watchlist (34 kept ids) and every tf04/tf15 survivor go first through the search gate.
2. Merge targets are proposals; any merged id can be resurrected with a reason.
3. The 23 protected anomalies should survive consolidation unless a judge produces a concrete kill reason — "template-like" is not one, by construction.
4. Cross-shard attractor convergence = prior-art warning signal (section 4.3).
5. Feasibility/compute triage is not done here (Judge B's job); only coarse compute/hardware flags are attached.

- **recommended_next_task_type:** `p1_wave_b_consolidator_w1`
