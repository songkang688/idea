# P1 Wave B w3 GATE-5 Repair Report

- **task_id**: `p1_wave_b_w3_gate5_repair`
- **role**: gate5_repair
- **windows_id / windows_path**: Windows13 / Windows13 (window_locked: true; lock identity untouched)
- **branch**: `cursor/p1-wave-b-w3-gate5-repair-f611` (from `origin/cursor/p1-wave-b-consolidator-w3-bf20`)
- **input**: `Windows13/_state/tasks/p1/wave_b_w3/remand_gate5.jsonl` — 173 accepted gen_g/gen_h records remanded by the w3 consolidator for lacking a usable pre-registered numeric kill threshold (GATE-5)
- **completed_at_utc**: 2026-08-29T01:05:00Z

## Result

| | count |
|---|---|
| Remanded records in | 173 |
| Repaired + appended to `ideas_master.jsonl` | **46** (gen_g 30, gen_h 16) |
| Still remanded (no extractable number) | **127** (gen_g 54, gen_h 73) |
| Master before / after | 592 / **638** (592 base lines preserved verbatim; 638 unique id_seeds; every line JSON-parsed) |

Checksum: 46 + 127 = 173; 592 + 46 = 638.

## Repair rule (HARD: no invention)

A record was repaired **only** if its own `falsifiable_prediction` / `minimal_falsification_experiment` /
`fastest_falsification_experiment` text already contained an exact numeric commitment. The repair copies that
commitment into `falsifiable_prediction` as an explicit **"Falsified if:"** clause that restates the record's own
quantifier — it never tightens, loosens, or replaces it with a guessed magnitude. Where a hedged quantifier had a
strictly weaker exact core (e.g. "a **large** majority"), the kill uses the weakest literal reading (bare majority,
i.e. failing even >50% kills), so no strength the author did not commit to is added.

Four extraction classes were accepted (per-record class + source phrase recorded in `gate5_repair` and in
`evidence_label.kill_threshold_provenance`):

1. **exact_fraction_quantifier** (22 records) — "a majority of", "most of the \[gap / gain / variance / divergence /
   cases / inputs / tasks / types / pairs / sequences / content]", "the bulk of variance", "worst-decile (bottom 10%)",
   and share-dominance inside a two-way decomposition stated by the record itself ("phase-dominated", "textural
   variance dominating", "dominated by caption-induced cases"). All map to the literal >1/2 (or 10% decile) reading.
2. **null_scale_reference** (12) — the record names the null scale the effect must exceed: "above chance",
   "far above nominal" / "below nominal", "exceeding \[test-set resampling] noise", "within \[run-to-run / selection]
   noise", "exceed seed-induced variance", "larger than the spread among competing single-kernel estimators",
   "larger than the median between-method gap". Kill = effect fails to clear the named null scale.
3. **universal_zero_bound** (6) — explicit universal quantifier with single-counterexample kill semantics:
   "**never** degrading below the zero-shot baseline on **any** tested shift", "for **all** models", "beat **every**
   single fixed rate", "**uniformly** across the severity axis", "**consistently** above", "**strictly dominate** the
   precision-recall tradeoff".
4. **existential_zero_crossing** (6) — the record's committed claim is that **some** instances cross a named zero /
   baseline: "negative gains for **some** method-shift pairs", "**at least some** published methods will fall below the
   never-adapt baseline", "flip the sign for **some** methods", "**some** celebrated methods providing **no benefit**",
   "**some** methods degraded below the frozen baseline". Kill = **zero** such instances observed.

### What was NOT accepted (stays remanded, 127 records)

- Bare directional claims ("A will outperform / beat / match B") — zero-margin comparisons are exactly what the
  judges ruled unusable; treating them as thresholds would un-remand everything.
- Vague magnitudes: "substantial(ly)", "large fraction", "clear margin", "small margin", "near-zero", "comparable",
  "measurably", "markedly", "nontrivial fraction", "several times", "orders of magnitude" (plural, ambiguous 10x/100x).
- Trend-/correlation-sign claims ("grows with severity", "rank inversely", "correlation will be negative",
  "stay flat or rise") and significance-only claims ("no significant difference", "lose statistical significance").
- Effect-vs-effect comparisons ("framework differences smaller than curation differences") and single-point Pareto
  claims ("strictly inside the frontier") — no null scale, no quantifier.
- Digits that are design parameters, not outcome bounds: "2x2x2 factorial", "4x SR", "8-bit", "ten percent of each
  \[for fitting]", "half a day".

No numeric kill value absent from the record text was created — **no 0.5-nats / 2-dB style guesses**.

## Per-record changes on the 46 repaired records

- `falsifiable_prediction` += explicit `Falsified if: <threshold restating the in-text quantifier>`.
- `evidence_label` dict added (gen_j-style): problem = KNOWN FACT (high-confidence model recall, unverified);
  core_hypothesis = HYPOTHESIS; falsifiable_prediction = EXPECTED RESULT (threshold extracted from record's own text,
  no experiment run); community_default_belief / why_possibly_novel = MODEL SPECULATION; plus
  `kill_threshold_provenance` naming the exact source phrase, source field, and extraction class.
- `gate5_repaired: true`; `gate5_repair` provenance block; `status: accepted_stage1`; `gate5_deferred: false`.
- `gate5_missing` reduced to the untouched gaps: `gate4_named_public_dataset_and_model` (all 46) and gen_h's
  `gate3_explicit_time_cost_bound` — naming public datasets/models or costs was **not** done because it would invent
  assets. These remain flagged per-record for the experiment-design lane.
- Original judge votes, judge metas, dissents, merged_from, and the consolidator `remand` block preserved verbatim.

## The 127 still-remanded records

Written in full (with a `gate5_repair_scan` annotation: scanned fields, result `no_extractable_numeric_bound`,
policy "no thresholds invented") to `Windows13/_state/tasks/p1/wave_b_w3_gate5/remaining_remand.jsonl`. They remain
**accepted on content by the judge majority** and pending GATE-5; they need either (a) a generator-side re-spec pass
that states real thresholds, or (b) judge-panel authority to set thresholds — both out of scope for this repair lane
under the no-invention rule.

## State updates

- `Windows13/_state/ideas_master.jsonl`: 46 records appended (592 -> 638; base 592 lines byte-preserved).
- `Windows13/_state/research_state.json`: `total_ideas` 638; `stage1_accepted_total` 638;
  `stage1_accepted_pending_gate5_retrofit` 127; `by_wave.p1_wave_b_w3` shard/append counts updated;
  `exploration.wave_b_w3_gate5_repair` block added. Lock identity fields untouched.
- `Windows13/_state/research_ledger.md`: row 19 appended.
- `window.lock.json`: untouched.

## Recommended next task

`p1_wave_b` — judge waves + consolidation for the remaining shards (gen_k 105 on origin, gen_l / gen_m / gen_n /
gen_p on origin, gen_o / gen_u when pushed). The diversity audit remains due (the w3 consolidator flagged it; the
master has since grown 592 -> 638).
