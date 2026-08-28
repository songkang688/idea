# P1 Wave B — Judge B: Feasibility / Experimental Falsifiability / Cheap-Kill Design (Wave 2: Generators D+E+F)

- **task_id:** `p1_wave_b_w2` | **role:** `judge_B_feasibility` | **windows_id:** `Windows13` (locked, `windows_path: Windows13`, `window_locked: true`)
- **branch:** `cursor/p1-wave-b-w2-judge-b-feasibility-64ff`
- **Scope:** independent second judging pass over the same 302 wave-2 ideas Judge A saw (generators D+E+F only). I re-read all three generator shards myself and formed my own keep/merge/kill lists; the wave-1 accepted master (`ideas_master.jsonl` from the wave-1 Consolidator branch) was read ONLY for cross-wave collision notes, and Judge A's wave-2 shard was consulted only afterwards as a reference — every agreement or disagreement below is informational for the Consolidator, not a reconciliation. Canonical state (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched.
- **Epistemic status:** NO novelty verified for any idea. Every prior-art / known-result remark is this judge's unverified hypothesis. No citations asserted or invented.

## 1. Inputs

| Shard | Branch | Ideas |
|---|---|---|
| gen_d_object_detection | `cursor/p1-gen-d-object-detection-07a3` | 100 (W13-P1-D-001..100) |
| gen_e_vlm_dense_prediction | `cursor/w13-p1-gen-e-vlm-dense-9412` | 100 (W13-P1-E-001..100) |
| gen_f_synthetic_data | `cursor/w13-p1-gen-f-synthetic-data-3a94` | 102 (W13-P1-F-001..102) |
| wave-1 accepted master (read-only, collision notes) | `cursor/p1-wave-b-consolidator-w1-7a58` | 248 accepted A/B/C ids |
| judge_A wave-2 (reference only, read after) | `cursor/p1-wave-b-w2-judge-a-dedup-13e5` | 248-keep dedup pass |

All 302 lines parsed; every id assigned exactly one verdict.

## 2. Method — what this judge scored

Each idea was tiered on the cost of its **decisive** falsification (not its aspirational full study):

- **T1 — inference/analysis only** (frozen public models, cached predictions, photographed/composited stimuli, small annotation audits; hours-to-days): the cheap-kill gold standard.
- **T2 — small training or light collection** (short fine-tunes, probes, resample-and-retrain grids, small human pilots): one GPU plus modest labor.
- **T3 — gated or expensive** (proprietary data/orgs, pretraining-scale compute): kept only when the hypothesis justifies waiting for the gate.

Additional axes: is the falsification **runnable as stated** (public assets exist?), is the idea a **template permutation** (schema stamped across substrates with no belief at risk), and is it **too vague** (no crisp failure criterion). Duplicate/co-run structure was assessed independently of Judge A; the wave-1 master was consulted only to flag cross-wave collisions.

## 3. Verdict Counts

| Quantity | Value |
|---|---|
| Input total | 302 (D: 100, E: 100, F: 102) |
| **Keep** | **255** (D: 83, E: 83, F: 89) |
| Merge (with explicit targets) | 44 — 34 in-wave (29 duplicate groups) + 10 cross-wave into accepted wave-1 ids |
| Kill (standalone) | 3 (E-035, F-023, F-053) |
| Kept at T1 (inference/analysis only) | 175 |
| Kept at T2 | 79 |
| Kept at T3 (gated; do not schedule until gate confirmed) | 1 (F-099) |
| Score-5 keeps (afternoon-scale decisive kills) | 76 |
| High-value anomalies protected | 20 |
| Co-run infrastructure clusters (not merges) | 10 |
| Recorded disagreements vs Judge A | 19 |

Wave 2 is dramatically more feasibility-friendly than wave 1: shards D and E are dominated by cached-prediction analyses and small stimulus batteries (T1), and shard F's training experiments are mostly two-to-four short runs (T2). Hence 3 kills here vs 13 in wave 1 — there is simply less hardware-gating and less compute-wall exposure in this wave. My keep count (255) exceeds Judge A's (248) because several of his merges are, on feasibility grounds, distinct cheap experiments that I keep and co-run instead (§7).

## 4. Kills (3) — feasibility/triage grounds

All three are UNVERIFIED known-result-restatement assessments — cheap to run but low expected information per unit work; the novelty judge or Consolidator may resurrect any of them:

- **E-035** (high-norm outlier patch tokens; filter for free dense gains): the outlier/register-token phenomenon and its fixes are, to this judge's unverified knowledge, an actively published line; the residual "across methods" claim does not justify a slot. Judge A kept it with a high-risk flag — recorded as a disagreement.
- **F-023** (sim-to-real gap lives in normalization statistics): recomputing normalization statistics on unlabeled target data is an established test-time adaptation technique; what remains is a magnitude measurement with no community belief at risk. Resurrect only reframed as one decomposition bound inside F-094.
- **F-053** (model-collapse fears overstated under accumulate-vs-replace): restates a result this judge assesses as established. Independent agreement with Judge A's standalone kill.

## 5. Cheap-kill honor roll (run these first)

76 kept ideas are score-5 T1. The first batch I would schedule, because they are decisive, cheap, and load-bearing for other ideas:

- **D-071 (+absorbed D-004)** — oracle label-vs-box decomposition on cached predictions; its outcome reprices D-044, D-077, D-020, D-055 and the whole recognition-vs-localization cluster.
- **E-013 (+absorbed E-014/E-015/E-020)** — head-noun+salience baseline with distractor stratification; reprices the entire referring-expression cluster in one afternoon.
- **D-031** (reweighting = post-hoc calibration) — one validation-split recalibration; if it holds, a large slice of long-tail literature claims is repriced.
- **E-047 (+D-005)** — text-geometry forecast of dense confusions; gates the six-idea text-geometry toolkit cluster.
- **E-004** (attention surgery = spatial denoising) — four conditions, one afternoon; sub-additivity readout.
- **D-002/D-003 (+absorbed E-025/E-026/D-016)** — vocabulary-composition and abstention harness; two afternoons, four claims.
- **F-089** (batch decorrelation) — within-batch vs across-batch embedding similarity in hours; gates a free-gains training claim.
- **F-031/F-035** (cleaning deletes hard examples; confident-wrong survival) — pure label audits, no student training.
- **F-024** (translation corrupts dense labels) — one-afternoon overlay audit that should be mandatory before any translation-based sim-to-real claim.
- **F-010** (stuff-free/thing-costly transfer) — re-scoring an existing experiment; if absent there, the hybrid-pipeline idea dies without new training.
- **D-066** (MLLM coordinate tokenizer priors) — digit/aspect histograms from a few thousand generated boxes.
- **E-087/E-090/E-091 (+E-085)** — the logic-query battery; afternoon-scale each, collectively mapping the missing-operation frontier.

## 6. Duplicate groups, cross-wave collisions, co-run clusters

**29 in-wave duplicate groups** (34 merged ids) with primaries and reasons: `judge_B.json → duplicate_groups`. The biggest independent consolidations: E-013 ⊃ {E-014, E-015, E-020} (easy-regime referring); D-003 ⊃ {D-016, E-026} (abstention harness); F-090 ⊃ {F-011, F-016} (convention divergence); F-019 ⊃ {F-013, F-079} (sensor/pipeline statistics); D-060 ⊃ F-033 (correlated errors defeat ensembling); E-010 ⊃ E-073 (counterfactual-evidence stimuli).

**10 cross-wave merges into accepted wave-1 ids** (master read-only, untouched): D-035→C-047, D-056→A-102, D-087→C-077, D-092→C-028, D-100→C-069, E-021→C-020, E-037→B-046, E-066→C-045, E-070→C-024, F-039→C-058. Each is a near-verbatim substrate port of an already-accepted wave-1 hypothesis; reasons in `judge_B.json → merge_ids`.

**10 co-run infrastructure clusters** (scheduling hints, not merges): compositing/counterfactual harness, vocabulary-sweep harness, bootstrap evaluator, density-array stimuli, synonym/phrasing harness, a shared multi-annotator re-annotation pool (the single largest labor cost in the wave — amortizes eight audits), text-geometry toolkit, layer-probe rig, resample-retrain grid for shard F, and a retrieval/contamination stack. Full membership: `judge_B.json → co_run_clusters`.

**Deliberate tensions kept** (adjudicate by experiment, not dedup): D-063 vs E-074; F-005 vs D-039; F-052 vs F-096; D-071 vs D-044; D-077 vs D-020; F-074 vs F-064.

## 7. Disagreements vs Judge A (19; informational — Consolidator resolves)

Full annotated list: `judge_B.json → disagreements_vs_judge_A`. The substantive ones:

1. **Kill vs keep:** E-035 and F-023 — A kept both with flags; I kill both as known-result restatements (unverified). Low cost either way; the question is slot economics, not feasibility.
2. **Keep vs merge (I keep what A merged), on distinct-instrument grounds:** D-009 (phrase composition ≠ synonym spread), D-032 (tail-CI vacuity ≠ headline-AP volatility; shared bootstrap harness co-run), D-062 (attribution masking ≠ paste composites), D-079 (routing rule ≠ crossover existence), D-084 (counting readout ≠ detection readout), E-001 (base observation E-046 presupposes), E-045 (template wording ≠ ensemble averaging), E-063 (leaderboard-validity claim, kept as primary absorbing D-006), E-065 (expression re-annotation ≠ box re-annotation), F-002 (convention-conflict mixing ≠ convention-matched noise), F-047 (pipeline-stage claim ≠ memorization mechanism).
3. **Merge vs keep (I merge what A kept):** D-016 → D-003 (same abstention harness), D-042 → E-029 (same synonym-spread measurement).
4. **Target-only differences:** D-006 (E-063 vs E-029), D-014 (single vs dual primary), D-035 (wave-1 C-047 directly vs in-wave D-085), F-029 (E-077 alone vs F-060+E-077 dual). No content at stake; Consolidator picks.

## 8. Anomalies protected (20)

D-029 (pattern completion in packed layouts), D-051 (nested-instance blind spot), D-066 (coordinate tokenizer priors — also score-5 cheap), D-069 (state-space frontier), D-083 (paradigm disagreement finds annotation errors), D-097 (detectors out-localize their labels), D-099 (contextual self-censorship), E-010 (masks survive object removal), E-041 (probes beat verbalized outputs), E-055 (frame-of-reference convention), E-084 (countability grammar controls topology), E-095 (reasoning tax on grounding), E-099 (overlay contamination), F-027 (pixel-perfect labels transfer worse), F-040 (quality filters anti-select dense value), F-060 (generator supply-chain forensics), F-069 (crawl-vintage drift), F-089 (i.i.d. violation in generation batches), F-091 (realism re-imports spurious correlations), F-096 (students exceed teachers via multi-view fusion).

## 9. Caveats / handoff

1. **kill/merge ≠ bad idea.** These are feasibility/triage dispositions; the Consolidator may resurrect anything; merge targets say where content folds (including the 10 wave-1 targets).
2. **The single T3 keep is conditional:** F-099 (true-cost accounting) needs proprietary project ledgers or a public cost-documented project; `runnable_as_stated: false`. Do not schedule until the gate is confirmed.
3. **scale_gap keeps** (F-051, F-057; mildly D-052, E-008): the recorded T2 tier covers a pilot-scale trend test; the decisive at-scale versions are effectively T3. Consolidator should weigh them accordingly.
4. **prior_art_risk flags are unverified** and concentrated in D-001/D-059/D-080/E-001/E-051/E-052/F-093/F-101 plus every wave1_flag carrier; a dedicated prior-art search pass must precede Stage-2 selection.
5. Per-id verdicts with tier, score (5 = cheapest kill), runnability, and flags: `judge_B.json → verdicts` (302 records). Kept ideas with judge annotations: `accepted_shard_B.jsonl` (255 lines).
