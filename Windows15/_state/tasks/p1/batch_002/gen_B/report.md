# P1 Wave A — batch_002 gen_B — T05 VLM / dense prediction

- **task_id:** `p1_wave_a_batch002_gen_B`
- **windows_id / windows_path:** `Windows15` / `Windows15` (lock respected; no canonical files touched)
- **territory:** T05 — vision-language models for dense prediction (segmentation / detection / depth)
- **idea_count:** 100 (target 100, minimum 80 — met)
- **idea_id range:** `W15-B002-B-001` … `W15-B002-B-100`
- **output_dir:** `Windows15/_state/tasks/p1/batch_002/gen_B/` (shard-only; canonical `ideas_master.jsonl` NOT modified)

## Scope and stance

All 100 entries are hypotheses about how VLMs behave (and fail) on dense prediction, about
assumptions the community makes without testing, and about evaluation-protocol weaknesses.
Per the territory brief, none of them is an "add a VLM decoder to task X" engineering idea:
each entry states a falsifiable claim with a minimal experiment and a fastest-falsification path.

**Novelty disclaimer (hard rule compliance):** every `why_possibly_novel` field is an
UNVERIFIED hypothesis about novelty, not a verified claim. No literature search was performed
to confirm novelty; Wave B dedup and later stages must treat these labels accordingly.
No citations, benchmark numbers, or experimental results were invented anywhere in the shard;
named model families (CLIP-style, SAM, LLaVA-style, AnyRes-style) appear only as generic
context, never with attributed results.

## Cluster histogram (14 clusters, 100 ideas)

| cluster | count |
| --- | --- |
| contrastive_pretraining_vs_localization | 8 |
| text_encoder_and_prompt_semantics | 8 |
| spatial_language_grounding | 7 |
| negation_absence_hallucination | 7 |
| vocabulary_frequency_and_caption_bias | 7 |
| resolution_scale_tokenization | 7 |
| autoregressive_dense_output_formats | 8 |
| depth_and_3d_from_vlms | 8 |
| evaluation_protocol_weaknesses | 8 |
| calibration_and_uncertainty | 7 |
| adaptation_forgetting_frozen_features | 8 |
| compositionality_attribute_binding | 7 |
| cross_domain_cross_lingual | 6 |
| referring_and_interactive_grounding | 4 |

## Angle coverage summary

- **Failure modes:** anti-grounded classes (003), negation-as-positive-evidence (024), absent-referent
  hallucination (025–027), attribute-binding swaps (084–086), perspective/frame bugs (018, 099),
  correction-turn statelessness (098), window/crop-seam artifacts (039, 043).
- **Ignored assumptions:** pixel exchangeability in conformal methods (070), threshold transfer across
  vocabularies (073), coordinate-token losslessness (045, 048), square-resize harmlessness (041),
  linear probes as capability arbiter (078), per-language parity implying code-switch robustness (096).
- **Evaluation weaknesses:** base/novel frequency leakage (061), string-matched scoring (062),
  grounding-vs-delineation conflation (063), contamination (064), background-convention variance (065),
  prompt curation as test leakage (066), missing negative-vocabulary queries (067), small-object
  annotation noise floor (068), spatial-QA as a false proxy for dense geometry (059).
- **Depth-specific hypotheses:** familiar-size prior failure (053), dead language pathway (054),
  piecewise-constant object depth (055), y-coordinate shortcut (056), prompt-injected scale (057),
  category-mediated depth (058), metadata-driven metric scale (060).
- **Mechanistic hypotheses:** outlier tokens (001), patch leakage (002), mid-layer information peak (004),
  norm-as-objectness (005), anisotropy vs prompt ensembling (008, 014), single-token mask bottleneck (052),
  sparse attribute channels (086), LoRA rank floor (080), abrupt alignment collapse (076).

## Hard-rule compliance checklist

- [x] 100 ideas (>= 80 minimum), each with all 13 required fields
- [x] `why_possibly_novel` phrased as unverified hypotheses throughout
- [x] No invented citations, numbers, or claimed experimental results
- [x] Wrote ONLY inside `Windows15/_state/tasks/p1/batch_002/gen_B/`
- [x] `window.lock.json`, `research_state.json`, `ideas_master.jsonl` untouched
- [x] No new Windows directories created

## Handoff

Shard is ready for Wave B dedup. Recommended next task type: `p1_wave_b_dedup_batch002`
(consolidate batch_002 gen_A/B/C shards against all previously accepted ideas; only the
consolidator appends to canonical `ideas_master.jsonl`).
