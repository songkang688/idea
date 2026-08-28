# P1 Wave A — Generator B Shard: Hard-Domain Dense Prediction Failure Modes

- **task_id:** `p1_gen_b_hard_domain_dense_prediction`
- **role:** generator (Wave A, candidate generation only)
- **windows_id:** Windows13 (LOCKED — canonical state untouched)
- **territory:** Medical / smoke-fire / transparent / ambiguous dense prediction failure modes. Scientific questions and foundation-model failure modes, NOT "apply method X to domain Y".
- **idea_count:** 96 (target band 80–120)
- **id range:** `W13-P1-B-001` … `W13-P1-B-096`
- **status of all ideas:** `candidate`, `novelty_verified: false`. No novelty claims are made. `why_possibly_novel` fields are explicitly labeled MODEL SPECULATION and are unverified.
- **canonical files NOT modified:** `ideas_master.jsonl`, `research_state.json`, `window.lock.json`.

## Epistemic policy

Every idea uses inline labels inside its fields:

- **KNOWN FACT** — uncontroversial physics / math / field-practice facts (e.g., Beer-Lambert attenuation, partial volume effect, patch tokenization in ViTs).
- **VERIFIED PRIOR WORK - general** — prior work referenced only at the level of well-known general practice (e.g., boundary losses are widely used; SAM-style promptable models exist). No specific citations, numbers, datasets, or results are asserted anywhere.
- **EVIDENCE** — reserved; not used for unowned claims in this shard.
- **HYPOTHESIS** — the core falsifiable claim of each idea.
- **MODEL SPECULATION** — novelty guesses and characterizations of community consensus (both inherently unverified from this seat).

No fake citations, benchmark numbers, dataset details, or experimental results appear in this shard. Where a dataset class is needed, ideas refer generically (e.g., "any multi-rater medical dataset", "synthetic renders with known density").

## Cluster map (12 clusters × 8 ideas)

| Cluster | IDs | Theme |
|---|---|---|
| `amorphous_boundary_ontology` | 001–008 | Whether binary masks are a category error for smoke/fire; penumbra error structure, annotator thresholds, exposure-dependence of flame extent, blob priors, ranking instability under soft metrics, definitional vs perceptual ambiguity. |
| `transparent_object_perception` | 009–016 | Background-dominated features inside glass, contour/context reliance, refraction and highlight cue ablations, two-surface label conflicts, depth-prior inheritance, glass-vs-smoke failure signatures, static-image information ceilings. |
| `medical_ambiguity_ground_truth` | 017–024 | Single-rater vs consensus training bias, loss-determined size bias laws, uncertainty vs rater-disagreement misalignment, nestedness validity of quantile contours, institution-style leakage into masks, ambiguity vs difficulty populations, Dice vs lesion-detection selection pressure, partial-volume regression. |
| `foundation_model_failure_modes` | 025–032 | Prompt-basin snapping on amorphous targets, prompt-jitter variance as an ambiguity meter, gradient snapping coefficients, scale-prior mismatch, scaling plateaus from label-ontology gaps, mass-noun vs count-noun grounding, linear-separability audits, bimodal all-or-nothing behavior under ambiguity. |
| `evaluation_metric_pathologies` | 033–040 | Oracle-threshold decoupling of IoU, boundary-metric collapse on fractal boundaries, loss-fingerprint forensics from masks, bimodal per-case score distributions, downstream-utility validity of metrics, statistical power audits of hard subsets, annotation-quality ceilings, anti-calibration selection pressure of thresholded scoring. |
| `shortcut_and_cue_reliance` | 041–048 | Global haze-statistics shortcuts, sensor-saturation dependence of fire models, intensity-vs-shape cue conflicts in medical, context-induced smoke hallucination, codec artifacts as learned cues, boundary-amplified texture bias, motion-blur leakage into single-frame benchmarks, smoke/steam/fog confusability. |
| `uncertainty_and_calibration` | 049–056 | Pixel-vs-extent calibration gaps under correlated errors, feature-distance vs confidence crossover, aleatoric-term validity against rater variance, ensemble collapse on structured ambiguity, marginal-vs-joint conformal coverage, soft-map vs mask-set dissociation by ambiguity modality, confidence sign inversion on glass, spatial cost-calibrated thresholds. |
| `physics_priors_and_image_formation` | 057–064 | Log-transmittance target parameterization, single-vs-multiple scattering regimes, emissive-vs-reflective prior violations near flames, polarization information gaps, PSF-aware likelihoods for boundary bias, scattering-parameter regression vs media classification, smoke shadows as unused evidence, background-structure decoupling as physics-blindness audit. |
| `temporal_process_vs_object` | 065–072 | Compute-matched temporal-vs-scale adjudication, flicker-based hard-negative rejection, variance-decay diagnostics of structured ambiguity, anti-correlated flow pseudo-labels through media, spread-rate fields as annotator-stable targets, object-permanence harm on dissipating media, event-camera separation of flames from reflections, longitudinal context collapsing medical margin ambiguity. |
| `representation_and_output_space` | 073–080 | Two-layer (medium+background) error accounting, low-dimensional ambiguity in signed-distance space, occupancy/opacity criterion conflation, decoder frequency-response mismatch, patch-quantized extent errors, coverage-vs-uncertainty disentanglement, query-decoder fragmentation of uncountable media, nested level-set supervision. |
| `data_and_annotation_protocols` | 081–088 | Annotation-tool signatures and inheritance, opacity-stratified sim-to-real gaps, sparse physical-sensor labels vs dense human labels, dont-know-band elicitation vs multi-rater budgets, label-convention share of cross-site drops, ambiguity tax on active learning, physical invalidity of copy-paste for media, near-duplicate split leakage audits. |
| `unifying_failure_structure` | 089–096 | Boundary-evidence-type taxonomy via blind clustering, ambiguity-type vs domain-appearance transfer, label-entropy floor estimation, cross-domain adversarial transfer as shared-mechanism probe, human-model failure complementarity, three-way error partition protocol (information-absent / information-unused / definition-absent), distribution-matching re-scoring, loss-caused directional asymmetry. |

## Idea index (id — one line)

### amorphous_boundary_ontology
- **W13-P1-B-001** — Binary masks are a category error for smoke: error concentrates in a penumbra band tracking optical thickness, not annotation noise.
- **W13-P1-B-002** — Smoke annotators implicitly choose a personal opacity threshold; disagreement is predictable from local contrast alone.
- **W13-P1-B-003** — Boundary-aware losses presuppose boundaries exist; on amorphous classes they may actively harm learning.
- **W13-P1-B-004** — Fire extent in an image is partly a camera property: predictions may track exposure settings more than physical fire size.
- **W13-P1-B-005** — Soft alpha supervision changes what the encoder learns, not just what the head outputs.
- **W13-P1-B-006** — Models inherit a blob prior from annotators and erase the fractal fine structure of real smoke.
- **W13-P1-B-007** — Smoke/fire leaderboard rankings may invert under transmittance-aware evaluation — representation artifacts.
- **W13-P1-B-008** — Fixing an operational opacity threshold may collapse expert disagreement, showing ambiguity is definitional, not perceptual.

### transparent_object_perception
- **W13-P1-B-009** — Inside glass, foundation-model features may encode the background better than the object.
- **W13-P1-B-010** — Transparent segmentation may run on contour and context, collapsing disproportionately under silhouette occlusion.
- **W13-P1-B-011** — Do models use refraction at all? Index-of-refraction render ablations measure it directly.
- **W13-P1-B-012** — Specular highlights may be the load-bearing shortcut; cross-polarized imagery could collapse current models.
- **W13-P1-B-013** — A glass pixel belongs to two surfaces; part of measured error is single-label representational deficit.
- **W13-P1-B-014** — Depth models see through glass; shared-backbone segmentation may inherit the glass-invisible prior.
- **W13-P1-B-015** — Glass jitters, smoke smears: a two-axis failure taxonomy separable by error statistics.
- **W13-P1-B-016** — Static single-image transparent segmentation may sit near an information ceiling humans also cannot beat.

### medical_ambiguity_ground_truth
- **W13-P1-B-017** — Single-rater vs consensus training may shift boundary placement in a consistent direction, not just add noise.
- **W13-P1-B-018** — The direction of over/under-segmentation may be set by the loss in a size-dependent, transferable law.
- **W13-P1-B-019** — Model uncertainty maps may not correlate with where experts actually disagree.
- **W13-P1-B-020** — Rater-percentile contours as nested targets — and a test for when nesting is even valid.
- **W13-P1-B-021** — Annotating institution may be decodable from predicted masks alone: style learned as anatomy.
- **W13-P1-B-022** — Ambiguous pixels and difficult pixels are different populations; current methods conflate them.
- **W13-P1-B-023** — Lesion-detection ranking vs Dice ranking: metrics may have selected architectures that miss small lesions.
- **W13-P1-B-024** — Boundary voxels are physical mixtures: mixture-fraction regression may beat classification on phantoms.

### foundation_model_failure_modes
- **W13-P1-B-025** — Promptable models may show a snapping field: masks jump to the nearest high-contrast contour on amorphous targets.
- **W13-P1-B-026** — Prompt-output variance as a free zero-shot ambiguity detector.
- **W13-P1-B-027** — A gradient snapping coefficient quantifying boundary relocation onto photometric gradients.
- **W13-P1-B-028** — Hard-domain failure may be predictable from target-vs-pretraining scale-prior mismatch.
- **W13-P1-B-029** — Scaling may asymptote for transparency/smoke because the missing ingredient is label ontology, not pixels.
- **W13-P1-B-030** — Text-prompted segmentation may ground count nouns better than mass nouns, penalizing smoke and tissue linguistically.
- **W13-P1-B-031** — Linear-separability audit: is the hard-domain deficit in frozen features or in decoders?
- **W13-P1-B-032** — Under ambiguity, foundation segmenters may output bimodal all-or-nothing masks instead of graded responses.

### evaluation_metric_pathologies
- **W13-P1-B-033** — IoU on soft boundaries mostly measures whether the model guessed the annotator's threshold.
- **W13-P1-B-034** — Boundary metrics on fractal boundaries may rank smoothing hyperparameters, not models.
- **W13-P1-B-035** — Metric forensics: the training loss may leave identifiable morphological fingerprints in masks.
- **W13-P1-B-036** — Mean scores hide bimodal competence: models either nail or completely miss hard cases.
- **W13-P1-B-037** — Matting-style perceptual error may predict downstream utility of smoke masks better than IoU.
- **W13-P1-B-038** — Power audit: hard-domain benchmark subsets may be too small for published ranking differences to be meaningful.
- **W13-P1-B-039** — Some hard benchmarks may already sit below single-annotator disagreement: leaderboard gains as noise-fitting.
- **W13-P1-B-040** — Fixed-threshold evaluation penalizes calibrated soft predictions, selecting against honesty about ambiguity.

### shortcut_and_cue_reliance
- **W13-P1-B-041** — Smoke segmenters may be global haze-statistics detectors; histogram manipulation could flip masks.
- **W13-P1-B-042** — Fire segmentation may depend on sensor saturation; unclipped HDR imagery could break current models.
- **W13-P1-B-043** — In intensity-vs-shape cue conflicts, medical models may follow intensity, predicting isointense-lesion failure.
- **W13-P1-B-044** — Pasting fire context into clean scenes may conjure phantom smoke masks: context hallucination.
- **W13-P1-B-045** — Video-compression artifacts may be a learned smoke cue; recompression could move masks.
- **W13-P1-B-046** — Texture bias may be amplified at boundaries: per-pixel stylization tests can localize the shortcut.
- **W13-P1-B-047** — Single-frame smoke benchmarks may leak motion via blur signatures, inflating static capability claims.
- **W13-P1-B-048** — Smoke vs steam vs fog: a context-neutralized confusability audit of whether models perceive media identity at all.

### uncertainty_and_calibration
- **W13-P1-B-049** — Pixelwise calibration can coexist with wildly miscalibrated extent estimates under correlated errors.
- **W13-P1-B-050** — Feature-space distance may out-predict model confidence for errors specifically on hard domains.
- **W13-P1-B-051** — Learned aleatoric terms may not match observer disagreement; multi-rater data gives a direct validity test.
- **W13-P1-B-052** — Ensembles may agree on the same wrong crisp boundary, systematically underestimating structured ambiguity.
- **W13-P1-B-053** — Pixelwise conformal masks may give nominal marginal coverage with near-zero structure-level coverage.
- **W13-P1-B-054** — Soft maps vs mask sets: a double-dissociation matching representation to ambiguity modality.
- **W13-P1-B-055** — Confidence-correctness correlation may invert on glass: most confident exactly where fooled.
- **W13-P1-B-056** — Utility calibration may require spatially varying thresholds no global calibration can express.

### physics_priors_and_image_formation
- **W13-P1-B-057** — Beer-Lambert suggests log-transmittance, not alpha, as the natural smoke regression target.
- **W13-P1-B-058** — Thin and thick smoke are different scattering regimes; models may silently fail in one of them.
- **W13-P1-B-059** — Fire is an emitter, not a reflector: halo errors as the fingerprint of violated shading priors.
- **W13-P1-B-060** — Polarization may carry what RGB lacks: small polarization probes vs large RGB foundation models.
- **W13-P1-B-061** — Modeling the scanner PSF inside the label likelihood may remove a boundary bias data cannot fix.
- **W13-P1-B-062** — Smoke, fog, haze as points in scattering-parameter space: regression may generalize where classification cannot.
- **W13-P1-B-063** — Smoke shadows encode optical thickness; models likely ignore this free evidence channel.
- **W13-P1-B-064** — Structured backgrounds make glass physically easier; flat model performance would prove physics-blindness.

### temporal_process_vs_object
- **W13-P1-B-065** — Smoke is a process: tiny temporal models may beat huge single-frame models at matched compute.
- **W13-P1-B-066** — Combustion flicker dynamics: a mechanistic hard-negative decomposition frame models cannot pass.
- **W13-P1-B-067** — Temporal averaging convergence rates as a diagnostic separating structured ambiguity from noise.
- **W13-P1-B-068** — Optical-flow pseudo-labels may be anti-correlated with participating media: actively harmful supervision.
- **W13-P1-B-069** — Spread-rate fields may be more annotator-stable and decision-relevant than extent masks.
- **W13-P1-B-070** — Object-permanence priors may hold onto dissipated smoke: memory-induced phantom persistence.
- **W13-P1-B-071** — Event cameras may separate real flames from reflections via combustion microdynamics.
- **W13-P1-B-072** — Longitudinal context may collapse medical margin ambiguity: part of aleatoric is missing-context epistemic.

### representation_and_output_space
- **W13-P1-B-073** — A two-layer medium+background decomposition may resolve most single-label errors in media scenes.
- **W13-P1-B-074** — Boundary ambiguity may be low-dimensional in signed-distance space: few modes explain rater variance.
- **W13-P1-B-075** — Occupancy and opacity are conflated in smoke labels; decomposing them may resolve label inconsistency.
- **W13-P1-B-076** — Decoder upsampling may impose a high-frequency prior that fights soft-boundary targets.
- **W13-P1-B-077** — Patch tokenization may quantize extent estimates, leaving periodic fingerprints in error histograms.
- **W13-P1-B-078** — A soft value of one half can mean half-covered or fully-unknown; the two need different downstream actions.
- **W13-P1-B-079** — Query decoders presuppose countable instances; media may fragment into phantom instances.
- **W13-P1-B-080** — Nested level-set supervision: preserve ordering, not threshold, for amorphous targets.

### data_and_annotation_protocols
- **W13-P1-B-081** — The annotation tool is a hidden co-author: brush vs polygon signatures may be learned as target structure.
- **W13-P1-B-082** — The sim-to-real smoke gap may concentrate in the thin regime where renderers approximate hardest.
- **W13-P1-B-083** — Sparse physical sensor labels may beat dense human labels per unit cost for calibrated extent.
- **W13-P1-B-084** — Explicit dont-know bands may buy more calibration per annotation dollar than more raters.
- **W13-P1-B-085** — A share of cross-site medical drop may be label-convention shift, isolable by convention-matched re-contouring.
- **W13-P1-B-086** — Active learning may pay an ambiguity tax: acquisition wastes budget on irreducibly ambiguous pixels.
- **W13-P1-B-087** — Copy-paste augmentation is physically invalid for media and may teach compositing artifacts as the cue.
- **W13-P1-B-088** — Near-duplicate frames may contaminate smoke-fire benchmark splits; temporal-split audits measure the inflation.

### unifying_failure_structure
- **W13-P1-B-089** — A boundary-evidence spectrum may organize all hard domains: failures cluster by evidence type, not domain.
- **W13-P1-B-090** — Ambiguity-type transfer may beat domain-appearance transfer: smoke may help tumor margins more than crisp tumors do.
- **W13-P1-B-091** — Hard benchmarks may approach label-entropy floors: an estimable irreducibility bound separates headroom from noise.
- **W13-P1-B-092** — A shared contrast operator may underlie glass, smoke, and lesion failures: adversarial transfer as mechanism probe.
- **W13-P1-B-093** — Humans and models may fail complementarily on hard domains, giving maximal teaming headroom exactly here.
- **W13-P1-B-094** — Partition benchmark error into information-absent / information-unused / definition-absent components.
- **W13-P1-B-095** — Distribution-matching evaluation may re-score much persistent hard-domain error as acceptable expert-plausible answers.
- **W13-P1-B-096** — Directional under/over-segmentation asymmetry may be loss-induced, testable by loss-swap factorial designs.

## Guardrails observed

- No writes to `Windows13/_state/ideas_master.jsonl`, `Windows13/_state/research_state.json`, or `Windows13/_state/window.lock.json`.
- `windows_id` unchanged (Windows13); no scan for a different Windows performed.
- All output confined to `Windows13/_state/tasks/p1/generators/gen_b_hard_domain_dense_prediction/`.
- Recommended next task: `p1_wave_b_dedup` (cross-generator dedup and canonical merge is the consolidator's job, not this generator's).
