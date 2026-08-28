# P1 Wave 2 — worker_E (VLM / dense prediction)

- **Task:** `p1_gen_w2_e` (Windows14, window locked, identity taken verbatim from `Windows14/_state/window.lock.json`; filling an empty dispatcher slot in Wave 2)
- **Status:** complete
- **Output shard:** `Windows14/_state/tasks/p1/wave2/worker_E.ideas.jsonl`
- **Idea count:** 125 (target was >=120)
- **Territory:** VLM / dense prediction — vision-language models for segmentation, detection, and grounding, focused on ignored assumptions and failure modes.

## Method

Generated candidate ideas by systematically walking the language-conditioned dense
prediction stack and, at each interface, asking what silent assumption the
community holds, what failure mode has no mechanistic account, what measurement
nobody runs, and what would falsify the default belief. Every idea is a
HYPOTHESIS anchored in a mechanism, an audit, or an ignored assumption, with a
concrete falsifiable prediction and a fastest-falsification path — most are
inference-only or 1–3 GPU-day experiments on frozen public models. No novelty
was verified against literature (flagged in `why_possibly_novel` as
"appears new/unexamined" hedges), and no citations, benchmark numbers, or
experimental results were fabricated.

Interfaces walked, with cluster names and counts:

1. **text_encoder_artifacts (10)** — BPE token-count score bias, polysemy sense
   priors, string-variant noise floors, multilingual localization decay, typo
   bimodality, jargon subword capture, compound orthography, synonym
   consistency as a missing metric, the literal word 'background' as negative
   class, frequency-keyed similarity-map sharpness.
2. **prompt_interface_fragility (10)** — classification templates misapplied to
   regions, ensembling's recognition/localization trade-off, determiner
   presuppositions, query-format sensitivity, template-collapse from synthetic
   expressions, prompt-tuning style overfit, register-inflated benchmarks,
   right-truncation of disambiguating clauses, sentence-order primacy,
   flip-TTA corrupting lateral language.
3. **spatial_language (8)** — frame-of-reference commitment, 2D proxies for
   depth prepositions, ordinal cliffs, pixel-absolute proximity kernels,
   spatial-word deletion audits, aspect-ratio distortion of shape words,
   egocentric deixis, flip-augmentation chirality loss.
4. **negation_absence_abstention (8)** — negation attraction (not just
   ignorance), empty-target abstention gap, prior-driven hallucination,
   counterfactual margins as free quality signals, complement queries vs
   self-inversion ceilings, vocabulary self-poisoning, small-vs-absent score
   inseparability, negated-attribute inversion ordering.
5. **counting_plurality (6)** — plural blob topology, universal quantifier
   drop, numeral invisibility, collective/distributive conflation, group
   density phase transitions, dual quantification ('both').
6. **attribute_binding_composition (10)** — swap-scene binding, projected-area
   size semantics, attribute-type hierarchies vs caption statistics,
   multiplicative constraint degradation, conflict-evidence hierarchies,
   parse-depth cliffs, clause-type blindness, action-word context shortcuts,
   salience-captured superlatives, knowledge-type gradients.
7. **language_prior_hallucination (7)** — typographic mask theft, read-vs-ground
   routing gaps, caption-subject bias, prompt-length-to-mask-area leaks,
   rare-word taxonomic substitution, hallucination position forensics, OOD
   prior takeover.
8. **alignment_mechanics (12)** — caption-salience recall ceilings, patch
   context contamination, discriminative-part attention gradients, shape-prior
   regression for novel words, fusion-scale bottlenecks, layer-choice
   trade-offs, bimodal similarity maps as error budgets, artifact-token
   phantom positions, modality-gap SNR, dense temperature retuning, signed
   upsampling bias, SSL-plus-adapter vs contrastive towers.
9. **calibration_scoring (8)** — per-prompt threshold incommensurability,
   paraphrase-variance uncertainty, AP vs thresholded-F1 inflation,
   specificity-score dilution, vagueness-blind sharpness, crop-score geometric
   blindness, referent-level overconfidence, lexical crispness calibration.
10. **architecture_resolution (7)** — patch-grid boundary ceilings, tiling vs
    globally-scoped language, anisotropic PE-interpolation decay, sub-stride
    ungroundable geometries, numeric-token coordinate snapping, box-stage
    topology filters, register-to-geometry leakage.
11. **open_vocab_detection (6)** — novelty-as-interpolation distance
    regressions, synonym-duplicate NMS leaks, vocabulary interference,
    hierarchical vocabulary score splitting, background-absorption error
    decomposition, softmax vs sigmoid under overlapping vocabularies.
12. **llm_dense_interface (6)** — mask-token capacity laws, reasoning-length
    mask drift, alignment tax on dense outputs, dialogue-history
    contamination, anaphora penalties, joint decoding of logically-related
    queries.
13. **benchmark_data_blindspots (10)** — discrimination-vs-description dataset
    imprints, granularity-mismatch error decomposition, crawl contamination
    audits, style-vocabulary entanglement, pseudo-label salience
    amplification, pooled-IoU size weighting, image-blind failure prediction,
    frequency-dominated per-class variance, stuff-thing caption debt,
    mislabeled residual floors.
14. **part_whole_granularity (7)** — part-whole gradient conflict seams,
    fallback-to-whole laws, non-compositional part-host pairs, modal/amodal
    evaluation incoherence, prompt-elicited amodal knowledge, thing-shaped
    priors on photometric referents, negative-space (gap) referents.
15. **robustness_domain_shift (6)** — corruption hierarchies over linguistic
    components, false-color palette hazards, language-amplified viewpoint
    bias, cross-modal sensitivity asymmetry, missing spatial near-miss
    negatives, frozen-text adaptation drift.
16. **temporal_video (4)** — predicate temporal validity, static shortcuts for
    motion words, state-change reference semantics, order-blindness via clip
    reversal.

## Constraints respected

- Wrote only the three worker_E files under `Windows14/_state/tasks/p1/wave2/`.
- Did not modify `window.lock.json`, `research_state.json`, or any
  `ideas_master.jsonl`.
- All 125 records carry `evidence_status="HYPOTHESIS"`; novelty is asserted
  only as "possibly novel" and unverified.
- Schema validated: 15 required fields present and non-empty on every line,
  ids `w14E-001` … `w14E-125` sequential and unique, JSONL parse-clean.

## Unresolved items

- Novelty screening against prior work is deferred to the dedup/prior-work
  stages of the pipeline; nothing here should be treated as verified-novel.
- Overlap with Wave 1 shards (worker_A SAM/PEFT, worker_B medical, worker_C
  smoke/fire) was avoided by territory scoping, but a consolidator should run
  cross-shard dedup on adjacent themes (e.g. patch-grid ceilings, TTA
  interactions, calibration audits) where mechanisms could rhyme across
  territories.
