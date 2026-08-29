# Stage-2 Shortlist — Batch B (Agent E, Independent Reviewer)

**Scope:** all 345 batch-B ideas (W2-B-0001..0345), scored on 14 dimensions in `scores.jsonl`.
**Result:** **77 keeps / 268 kills**, of which **31 keeps carry an explicit protection tag**.

## How this list was built (and how NOT to read it)

- Ranking is **not** by mean score. The mean in `scores.jsonl` is provided for transparency only.
  A high-variance idea (Novelty 5, Risk 2) can outrank a safe idea with a higher mean.
- Four classes were deliberately **protected** even where a mean-ranker would drop them:
  - **CI** = counter-intuitive (simple claim that inverts a community default)
  - **CF** = cheap-to-falsify (a weekend-to-two-weeks decisive experiment)
  - **DP** = disagreement-prone (senior researchers would split; either outcome moves the field)
  - **HRHR** = high-risk / high-reward (probable null, paradigm-level payoff if positive)
- Verdicts already incorporate the adversarial prior-work attack (`prior_work_attack.md`):
  three originally-kept ideas (0136, 0175, 0279) were killed there, and several keeps survive only
  in **mutated** form (0042, 0098, 0101, 0145, 0154, 0163, 0172, 0200, 0203, 0213, 0226, 0254, 0339).

## Top tier — highest-conviction keeps (unordered within tier)

These are the ideas I would defend in a fight. Not a "final 3" — that is the PI's call.

| ID | Why it is top tier |
|---|---|
| W2-B-0001 | Register/high-norm artifact as a free per-pixel error predictor. Survived attack; the registers literature stops at "artifacts exist / hurt dense tasks" — nobody sells the norm map as an uncertainty channel. |
| W2-B-0074 | Modality-gap **collapse as a phase transition** during fine-tuning that predicts zero-shot robustness loss. Gap statics are heavily published; the fine-tuning **dynamics** are open. |
| W2-B-0104 | PEFT inherits pretrained invariances that dense tasks must break — a mechanism *and* a predictor of when LoRA fails. Positions cleanly against intruder-dimension work. |
| W2-B-0114 | VPT prompt tokens are trainable **registers**. Frozen-random-token control is nearly free and decisive; two hot literatures (VPT, registers) have not been connected. |
| W2-B-0304 | Language **quantizes** shape space: morph-trajectory discontinuities in CLIP-lineage but not SSL features. Psychophysics-grade design; flagship of the geometry family. |
| W2-B-0323 | Mention bias: unmentioned-but-visible content is decodability-poor in language-aligned models, SSL-normalized. Direct supervision-weighting imprint; reporting-bias lit never did the dense/decodability version. |
| W2-B-0307 | Causal version of "language costs metric depth": matched-data matched-architecture pretraining isolates the alignment term that Probing-3D-Awareness left correlational. |
| W2-B-0213 | Resolution confound overturns published VFM dense rankings (protected DP). Mutated post-attack to the resolution axis specifically, extending Kerssies et al. CVPRW'24; re-evaluation science, expect fights. |
| W2-B-0226 | Shift budgets: frozen features degrade gracefully, tuned sharply. Mutated to per-model budget-curve quantification for dense prediction; the LP-FT literature proved the direction, not the curve. |
| W2-B-0101 | Task-indexed required-rank law for PEFT: dense tasks need higher update rank, and accuracy tracks captured spectral mass. Mutated from binary claim to quantitative law. |
| W2-B-0268 | Synthetic-image contamination of web-collected benchmarks measurably distorts method rankings. Eval-integrity result with a deadline — worth doing *now*. |
| W2-B-0332 | Visual chain-of-thought as post-hoc theater, tested by artifact-swap causal intervention. VLM CoT-faithfulness literature exists but the visual-evidence intervention is the fresh weapon. |

## Full keep list by cluster (77)

Protection tags: CI = counter-intuitive, CF = cheap-to-falsify, DP = disagreement-prone, HRHR = high-risk/high-reward.

### vfm_failure (8 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0001 | CF | 4.43 | register-artifact -> per-pixel error map; free uncertainty; cheap and decisive; needs lit check vs register papers |
| W2-B-0005 | — | 3.93 | attention-entropy collapse as cause of resolution extrapolation failure; causal intervention angle is fresh |
| W2-B-0013 | CI | 4.21 | inverse scaling for sub-patch objects; counter-intuitive, cheap, size-binned eval is decisive |
| W2-B-0018 | CF | 4.29 | Nyquist-style law for thin structures; parametric synthetic sweep; law-like, cheap, useful either way |
| W2-B-0023 | — | 3.93 | psychophysical acuity battery for LVLMs; strong measurement idea; must cite BLINK/V*/Eyes-Wide-Shut as adjacent |
| W2-B-0025 | DP | 3.93 | PROTECTED: are emergent attention maps epiphenomenal? intervention design fragile but community-splitting either way |
| W2-B-0026 | — | 3.79 | nameability predicts language-aligned dense errors; bridges psycholinguistics; flagship of nameability family |
| W2-B-0033 | DP | 3.79 | PROTECTED: pretraining seed variance vs published VFM gaps; expensive but field-correcting reproducibility science |

### vlm_dense_failure (7 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0036 | — | 4.36 | flip-consistency audit of relation grounding; must cite RES-bias lit (Cirik) but quantification is publishable |
| W2-B-0042 | — | 4.36 | synonym variance > model-generation variance; benchmark-shaking if true; cheap; attack for name-sensitivity lit |
| W2-B-0043 | — | 3.93 | attribute-object prototype snapping in dense grounding; compositionality lit is image-level, dense gap real |
| W2-B-0054 | CF | 4.21 | multiplicative error law for multi-hop referring; clean falsifiable functional form; deviations diagnostic |
| W2-B-0062 | CF | 4.07 | size adjectives read as pixel size not class-relative size; clean dissociation scenes; decisive and cheap |
| W2-B-0064 | — | 4.07 | part-whole containment violations as consistency metric; PACO makes it cheap; correlates with hallucination |
| W2-B-0068 | CF | 3.93 | grounding shadows/holes/reflections fails categorically; object-centric ontology exposure; annotate small+decisive |

### finetune_instability (7 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0074 | — | 4.21 | modality-gap collapse as phase transition predicting zero-shot loss; strongest FT-dynamics idea; attack for gap-dynamics lit |
| W2-B-0077 | CI | 4.07 | inverted layer-wise LR decay for dense tasks; cheap sweep; overturns default heuristic if true |
| W2-B-0078 | — | 3.64 | first-100-steps predict final OOD fate; early-diagnosis value; 50-run design is honest |
| W2-B-0087 | — | 3.86 | post-spike calibration scars; hysteresis framing fresh; natural-experiment design plausible |
| W2-B-0092 | CI | 3.93 | PROTECTED: inverse stability scaling with model size; counter-intuitive, expensive at L/H but 3-point ladder bounds it |
| W2-B-0095 | — | 3.93 | displacement-budget clipping reproduces PEFT stability; mechanism-attribution sibling of 0098 |
| W2-B-0098 | — | 4.21 | LoRA=rescaled-LR full FT in function space; capacity-myth killer; attack for LoRA-theory lit overlap |

### peft_limits (8 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0101 | — | 4.36 | dense tasks need higher update rank; task-indexed required-rank law; foundational for PEFT-on-dense claims |
| W2-B-0104 | — | 4.43 | invariance-inheritance ceiling of PEFT; mechanism + predictor; flagship; attack for invariance-transfer lit |
| W2-B-0105 | — | 4.0 | prompt-tuning gains vanish off-manifold; capability-boundary framing; pairs with 0128 gradient mechanism |
| W2-B-0108 | — | 4.0 | PEFT/full-FT calibration flips sign under shift; deployment-relevant interaction nobody measures |
| W2-B-0112 | — | 3.93 | shift-magnitude crossover LoRA vs full FT; actionable phase picture; robust-null friendly |
| W2-B-0114 | CF | 4.43 | VPT tokens = trainable registers; two hot literatures collide; frozen-random-token control is decisive and free |
| W2-B-0118 | — | 3.86 | PEFT hides subgroup gaps at matched average accuracy; capacity-fairness tradeoff; high stakes, understudied for dense |
| W2-B-0133 | CI | 3.79 | PROTECTED: LoRA memorizes more per-parameter (privacy inversion); if true, flips PEFT deployment advice; attack for PEFT-privacy lit |

### catastrophic_forgetting (6 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0137 | CI | 4.0 | beneficial forgetting: shedding typographic vulnerability; reframes forgetting as dial not disease |
| W2-B-0145 | CF | 4.14 | ATTACKED->MUTATE: 'Continual Calibration: Coverage Can Collapse Before Accuracy' (arXiv 2604.23987, LLMs) + 'Calibration of Continual Learning Models' (arXiv 2404.07817) publish the calibration-degrades-first ordering; mutated to dense-vision VFM single-task adaptation: per-region calibration vs accuracy decay curves along fine-tuning. |
| W2-B-0154 | — | 4.0 | MANDATED ATTACK: decoder capacity governs backbone forgetting; head-capacity dial; check LP-FT/CL-head lit |
| W2-B-0157 | — | 4.29 | prompt-template staleness inflates forgetting estimates; measurement-reform with immediate lit impact |
| W2-B-0163 | — | 4.14 | ATTACKED->MUTATE: LP-FT/Hidden-Costs/Reprogrammer lit covers 'FT hurts OOD while ID looks fine' for the DOWNSTREAM task; mutated to old-task forgetting-audit bias: ID-vs-OOD retention probe pairs, dose-response of the audit gap, pretrained-normalized metrics. |
| W2-B-0164 | CF | 4.14 | savings/relearning-speed paradigm imported to VFM forgetting; measures memory retention probes miss; near-free |

### prompt_sensitivity (5 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0168 | CF | 4.36 | template-engineering gains are mostly calibration; decomposition cheap; deflationary result with broad reach |
| W2-B-0169 | CI | 4.36 | negative points hurt beyond 2-3; inverts more-information intuition; response-surface design is clean |
| W2-B-0172 | CF | 4.36 | ATTACKED->MUTATE: ITACLIP (CVPRW'25, arXiv 2411.12044) reports LLM definitions/synonyms IMPROVE training-free OVSS (dataset-dependent choice); hypothesis contested, not settled. Mutated to auxiliary-text response-curve dissociation: when enrichment hurts dense while helping classification. |
| W2-B-0182 | CI | 3.86 | scale increases prompt sensitivity on rare classes; inverse-scaling interaction; two-family replication design |
| W2-B-0194 | CF | 4.36 | segmentation sycophancy: confidence rises with prompt count while accuracy doesn't; catchy, cheap, safety-relevant |

### representation_mismatch (7 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0196 | — | 4.07 | equivariance-deficit spectrum as transfer predictor; benchmark science with predictive teeth |
| W2-B-0200 | — | 4.5 | MANDATED ATTACK: linear probes misrank VFMs for dense use; attentive-probe lit adjacent; expect SURVIVE-with-citations or MUTATE |
| W2-B-0203 | — | 4.43 | MANDATED ATTACK: bilinear upsampling is the binding constraint; FeatUp/LiFT lit must be faced; expect MUTATE |
| W2-B-0208 | CF | 4.36 | occupancy-threshold recall law; closed-form, cross-validated, cheap; useful negative too |
| W2-B-0213 | DP | 4.14 | ATTACKED->MUTATE: Kerssies et al. 'How to Benchmark VFMs for Semantic Segmentation?' (CVPRW'24, arXiv 2404.12172) shows rankings shift with benchmark settings; mutated to the resolution axis specifically: train/eval resolution decoupling + per-model native-resolution normalization, ranking inversion quantified. |
| W2-B-0215 | — | 4.07 | text-aligned subspace vs complement carries dense info; explains text-mediated dense underperformance; testable decomposition |
| W2-B-0222 | — | 3.71 | video pretraining repairs equivariance deficit at matched semantics; timely (V-JEPA era); mediation design |

### crossdomain_frozen_vs_tuned (6 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0226 | — | 4.0 | MANDATED ATTACK: shift budgets frozen-vs-tuned; Andreassen/Taori/LP-FT terrain; expect MUTATE to budget-quantification |
| W2-B-0227 | CI | 3.86 | cleaner labels transfer worse; label-quality paradox; controlled noise ladders are cheap |
| W2-B-0234 | — | 3.79 | frozen-vs-tuned 2D phase boundary (data x gap); unifies 0112/0127/0226 family; grid is costly but bounded |
| W2-B-0241 | — | 3.93 | style-vs-content double dissociation frozen/tuned; clean regime map; generation-based shift suites exist |
| W2-B-0243 | — | 4.0 | nameability boundary for text-steered adaptation; parallel boundary in 0271 strengthens; falsifiable and cheap |
| W2-B-0252 | HRHR | 3.71 | PROTECTED: interpolation-frontier kinks = discrete mechanism transitions; if kinks reproduce, big mechanistic payoff; null likely but cheap-ish |

### synthetic_adaptation (6 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0254 | — | 4.0 | MANDATED ATTACK: synthetic data trades calibration for accuracy; check synthetic-training calibration lit; likely SURVIVE with citations |
| W2-B-0263 | CI | 4.0 | procedural corruptions beat realistic generated ones for robustness; structure-preservation mechanism; cheap and contrarian |
| W2-B-0264 | HRHR | 3.86 | PROTECTED: synthetic medical data launders privacy; downstream membership leakage; hard but field-defining if positive |
| W2-B-0268 | — | 4.0 | synthetic contamination of web-collected benchmarks distorts rankings; urgent eval-integrity result; detector-ensemble design |
| W2-B-0275 | — | 3.79 | dense metrics (boundary F1) as early canary for model collapse in generate-train loops; timely, decisive design |
| W2-B-0278 | HRHR | 3.71 | PROTECTED: spectral-coverage criterion predicts sign of synthetic-data effect; theory-grade if it works; encoder-dependence risk |

### medical_vfm_science (5 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0282 | CI | 4.0 | orientation invariance destroys laterality signals; robustness-as-bug; cheap radiograph battery |
| W2-B-0284 | CF | 4.14 | lesion-size/stride detection law with feasibility calculator; clinical triage value; law-like falsifiability |
| W2-B-0286 | — | 3.79 | site-of-origin decodability: natural VFMs more site-invariant than medical FMs; provocative, cheap, pairs with 0293 |
| W2-B-0293 | — | 3.86 | MANDATED ATTACK: matched-budget medical-FM ablation; DINOv2-vs-medical-FM evals exist; expect MUTATE to modality-resolved version |
| W2-B-0303 | — | 4.0 | fine-tuning degrades extreme-specificity ROC tails at matched AUC; screening-relevant; frozen-vs-tuned angle sharp |

### language_geometry_alignment (7 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0304 | — | 4.14 | language quantizes shape space (morph discontinuities); flagship of geometry family; psychophysics-grade design |
| W2-B-0305 | HRHR | 3.5 | PROTECTED: Whorfian imprint of English spatial categories; cross-linguistic probes; confound-heavy but paradigm-level if real |
| W2-B-0307 | — | 3.93 | MANDATED ATTACK: language degrades metric depth at matched data; Probing-3D-Awareness showed correlational version; causal matched-pretraining is the residual |
| W2-B-0317 | HRHR | 4.0 | PROTECTED: MIL identifiability theory predicts which concepts can never emerge densely; deepest theory idea in batch B |
| W2-B-0323 | — | 4.07 | mentioned-bias: unmentioned-but-visible content under-represented; direct supervision-weighting imprint; SSL-normalized design |
| W2-B-0325 | — | 3.93 | text-only counterfactual decomposes spatial errors into inherited-linguistic vs visual; blind-baseline lit exists but decomposition is new |
| W2-B-0326 | — | 4.0 | basic-level naming sets default segmentation granularity; psycholinguistic import; hierarchy datasets exist |

### agentic_vision_hypotheses (5 keeps)

| ID | Prot | Mean | Note |
|---|---|---|---|
| W2-B-0329 | — | 3.93 | agent confidence uncorrelated with tool-output quality; broken uncertainty chain; instrumentation is the contribution |
| W2-B-0332 | — | 4.14 | MANDATED ATTACK: visual CoT as post-hoc theater; artifact-swap intervention; CoT-faithfulness lit must be faced |
| W2-B-0338 | — | 3.86 | web-agent benchmark contamination via retrieval; blinding experiment decisive; eval-integrity urgency |
| W2-B-0339 | — | 3.93 | ATTACKED->MUTATE: VRA (arXiv 2509.16343) + LVLM test-time-scaling studies already publish generic agentic-vs-scale compute tradeoffs; mutated to the evidence-locality crossover predictor as the falsifiable object, matched-FLOP protocol as secondary. |
| W2-B-0342 | — | 3.71 | question-substitution drift in decompose-and-answer agents; attribute-substitution import; dissociated-pair design |

## Protected exceptions — kept against the mean

These would be dropped by naive mean-ranking; they are kept by mandate class.

| ID | Class | Why protected |
|---|---|---|
| W2-B-0025 | DP | Are emergent attention maps epiphenomenal? Intervention design is fragile, but either answer splits the community. |
| W2-B-0033 | DP | Pretraining seed variance vs published VFM gaps. Expensive and unglamorous; field-correcting if gaps are within seed noise. |
| W2-B-0092 | CI | Inverse stability scaling with model size. Probably wrong; a 3-point model ladder bounds the cost of finding out. |
| W2-B-0133 | CI | LoRA memorizes MORE per trainable parameter (privacy inversion). Flips PEFT deployment advice if true. |
| W2-B-0213 | DP | Resolution confound overturns published dense rankings. Guaranteed disagreement with benchmark authors; mutated post-attack to the resolution-specific axis. |
| W2-B-0252 | HRHR | Kinks in the interpolation frontier as discrete mechanism transitions. Null likely; mechanistic payoff large. |
| W2-B-0264 | HRHR | Synthetic medical data launders privacy (downstream membership leakage). Hard; field-defining if positive. |
| W2-B-0278 | HRHR | Spectral-coverage criterion predicting the SIGN of synthetic-data effects. Theory-grade if it works. |
| W2-B-0305 | HRHR | Whorfian imprint of English spatial categories in VLM spatial errors. Confound-heavy; paradigm-level if real. |
| W2-B-0317 | HRHR | Identifiability theory (MIL) for which concepts can never emerge densely from image-level supervision. Deepest theory bet in batch B. |

Remaining CI/CF-protected keeps (0001, 0013, 0018, 0054, 0062, 0068, 0077, 0114, 0137, 0145, 0164,
0168, 0169, 0172, 0182, 0194, 0208, 0227, 0263, 0282, 0284) are protected because a decisive,
cheap experiment exists — they are insurance against the portfolio skewing toward expensive bets.
