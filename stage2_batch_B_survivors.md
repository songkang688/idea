# Stage 2 — Batch B Survivors (75 of 340)

**PI:** Windows5
**Stage:** 2 (selection: 340 → 75)
**Source:** `stage1_batch_B_ideas.md` (IDEA-B-0001 … IDEA-B-0340)
**Companion files:** `stage2_batch_B_scores.md` (all scores), `stage2_batch_B_killed.md` (elimination record)

Selection was **not** by mean score. Four protection classes overrode averages: high-risk/high-reward (HRHR), simple counter-intuitive claims (CI), disagreement magnets (DM), and cheap-to-falsify (CF). Ten survivors are protected HRHR bets: **0009, 0019, 0075, 0078, 0159, 0162, 0185, 0294, 0318, 0329**.

---

## Cluster 1 — Dataset Failure / Annotation Efficiency / Long-Tail (8 survivors)

### IDEA-B-0001 — Structured (non-i.i.d.) noise in SAM pseudo-labels breaks noise-robust learning theory
**One-line:** SAM pseudo-label noise is spatially structured and content-correlated, so noise-robust losses built for i.i.d. noise fail on it. `[CF]`
**Survival Reason:** Measures the noise model of the field's default auto-labeler. Every noise-robust training paper implicitly assumes i.i.d. noise; if SAM noise is low-entropy and learnable as a bias, a whole method family is inapplicable to the dominant data-generation pipeline.
**Major Risks:** At high pseudo-label quality the structured-vs-i.i.d. gap may be small — true but low-impact. The fitted spatial noise model may be dataset-specific.
**Unresolved Questions:** Is there a compact parametric family (offset + dilation per texture stratum) that captures SAM noise across datasets? Do any existing robust losses accidentally handle structured noise?
**Required Experiments:** On 2–3 expert-masked datasets: generate SAM pseudo-labels; fit spatial noise statistics; train identical students on clean / SAM / rate-matched i.i.d.-noise labels; compare robust-loss deltas between the two noise conditions.
**Reviewer Opinion:** The cleanest "noise model of the real pipeline" study in the batch. Even a null (robust losses hold up) is informative and publishable as an audit. Pair with 0191 for the multi-generation consequence.

### IDEA-B-0006 — Label-convention averaging: systematic boundary bias from multi-dataset fine-tuning
**One-line:** Pooling datasets with different annotation conventions produces an averaged boundary *bias*, not variance, removable with a one-token convention indicator. `[DM]`
**Survival Reason:** Attacks the field's default scaling recipe (pool everything) with a measurable bias term and a nearly free fix. A confirmed result means pooled models are systematically wrong everywhere while looking good on average — a genuine disagreement magnet.
**Major Risks:** Real conventions differ non-uniformly along boundaries; a scalar signed offset may be too coarse a summary. Controlled re-annotation is labor.
**Unresolved Questions:** Does convention conditioning survive when conventions are latent (unlabeled sources)? How does the bias interact with model scale?
**Required Experiments:** Re-annotate ~100 images under two written protocols; train on the union with/without convention token; measure signed boundary-offset distributions per test convention.
**Reviewer Opinion:** Small, sharp, and consequential for every merged-dataset effort (including MedSAM-style corpora). The one-token fix gives it an actionable ending most audit papers lack.

### IDEA-B-0009 — A geometric-stratum census of SA-1B that predicts fine-tuning gains
**One-line:** Per-stratum pretraining frequency vs capability, separating data-limited from architecture-limited failures. `[HRHR — protected]`
**Survival Reason:** The most consequential distinction in foundation-model planning: strata on the frequency-capability line need data; deviating strata need new architecture. Nothing else in the batch answers this, and LLM-style frequency-capability analysis has no dense-prediction analogue.
**Major Risks:** Automated stratum detectors are imperfect on exactly the hard strata being counted, biasing frequency estimates. Laborious census work; log-linear fit may be muddied by confounds between strata.
**Unresolved Questions:** What is the right stratum taxonomy (transparent / wiry / camouflaged / tiny / low-contrast)? How much manual verification makes the census trustworthy?
**Required Experiments:** Estimate stratum frequencies on a 100k-image SA-1B sample (detectors + manual verification); measure zero-shot and post-fine-tuning IoU per stratum on curated probes; fit and inspect the frequency-capability curve.
**Reviewer Opinion:** High effort, high risk, but this is the study that tells the field where scaling stops working. Protected precisely because its mean score is dragged down by feasibility while its upside is field-redirecting.

### IDEA-B-0012 — Near-duplicate inflation of annotation-efficiency claims
**One-line:** Near-duplicates (adjacent frames, same-patient slices) inflate few-shot medical claims; dedup-aware splits shrink them predictably. `[CF·DM]`
**Survival Reason:** Cheap, decisive, and directly attacks numbers now driving clinical adoption decisions. Dedup is standard for pretraining corpora but absent from dense few-shot evaluation protocols.
**Major Risks:** Missing patient metadata makes duplicate clustering approximate on some datasets; shrinkage magnitude may vary widely across datasets.
**Unresolved Questions:** Can the inflation be predicted from a dataset's duplicate-cluster size distribution alone (enabling correction without re-running)?
**Required Experiments:** Perceptual-hash + embedding duplicate clustering on 5 public medical datasets; re-evaluate a standard SAM fine-tuning recipe under naive vs dedup-aware splits; report gaps.
**Reviewer Opinion:** The kind of paper that changes reporting norms within a year. Should be run early — it recalibrates how the rest of the program reads the few-shot literature.

### IDEA-B-0017 — The missing-negative problem in transparent-object benchmarks
**One-line:** Transparency benchmarks contain almost no target-absent images, so FP behavior is unmeasured; ~500 curated negatives may invert rankings. `[CF]`
**Survival Reason:** Deployment harm is FP-dominated (hallucinated glass in robotics), yet the benchmarks penalize only misses. A ranking inversion on hard negatives (mirrors, water, gloss) is checkable with one curation pass and public checkpoints.
**Major Risks:** Defining "hard negative" without biasing toward particular failure styles; curation quality is the whole instrument.
**Unresolved Questions:** Do FP rates correlate with any property visible in the positive-set metrics, or is negative evaluation genuinely orthogonal information?
**Required Experiments:** Curate ~500 hard-negative images; evaluate public transparency checkpoints for FP area rate; correlate with published benchmark ranks.
**Reviewer Opinion:** Textbook cheap-to-falsify audit. Combine with 0088's methodology (killed as duplicate) for the general rare-event-FP framing.

### IDEA-B-0019 — Anchoring bias in correct-the-model annotation workflows
**One-line:** Annotators correcting SAM proposals under-correct systematic errors, so model-in-the-loop datasets inherit model-lineage bias. `[HRHR·DM — protected]`
**Survival Reason:** If true, the field's dominant annotation economy is quietly corrupting its own ground truth across model generations. Anchoring is documented in HCI for classification; the dense form and its multi-generation propagation are unmeasured.
**Major Risks:** Within-subject memory effects demand careful counterbalancing and washout; annotator recruitment cost; effect may be small for expert annotators.
**Unresolved Questions:** Does the inherited error signature survive a full retraining generation? Which interface designs (proposal hiding, delayed reveal) break anchoring?
**Required Experiments:** Within-subject study: same annotators label 150 images from scratch and (weeks later, shuffled) via correction; measure error alignment with proposals; train students on each corpus and test error-signature inheritance.
**Reviewer Opinion:** Protected as high-risk/high-reward: the human study is the risk, dataset-ecology corruption is the reward. Links directly to 0191 (amplification dynamics) — together they define the data-flywheel safety question.

### IDEA-B-0024 — Nearest-neighbor mask transfer as a baseline that beats few-shot fine-tuning
**One-line:** Below ~10 labels, retrieval + dense correspondence may beat fine-tuning a foundation segmenter, with a predictable crossover. `[DM·CF]`
**Survival Reason:** Installs the honest baseline the crowded few-shot medical-SAM literature never reports. A classical method dominating modern PEFT at small n is exactly the kind of deflationary result reviewers split on.
**Major Risks:** Correspondence quality collapses for pathological/deformed cases — precisely where value is highest; crossover may vary strongly by anatomy.
**Unresolved Questions:** Is the crossover n predictable from registration residuals alone? Does a retrieval + fine-tune hybrid dominate both?
**Required Experiments:** On 4 anatomies, sweep n ∈ {1,3,5,10,30}; DINO-feature correspondence transfer vs LoRA fine-tuning; locate crossovers; regress on registration residuals.
**Reviewer Opinion:** Cheap and immediately citable as the missing baseline. Should be an early kill-test; a negative (fine-tuning always wins) is also worth having on record.

### IDEA-B-0037 — An annotation-tolerance-derived IoU ceiling as a function of object size
**One-line:** Closed-form maximum achievable IoU given boundary tolerance and object size/shape; flags benchmark strata already at ceiling. `[CF]`
**Survival Reason:** Derivable on paper, validated in one evaluation pass, and reframes "progress" on small-object strata where methods may already be at the annotation-noise ceiling. Anchors the ceiling thread (0220 killed into it).
**Major Risks:** Real tolerance varies by annotator and structure; a single ±k px parameter may miss convention-driven asymmetries.
**Unresolved Questions:** How should leaderboards report stratum scores relative to ceiling rather than absolute?
**Required Experiments:** Derive the ceiling analytically for parametric shapes; estimate tolerance from multi-rater data; verify empirically; flag at-ceiling strata in 2–3 popular benchmarks.
**Reviewer Opinion:** The cheapest high-leverage item in Cluster 1. Everyone who evaluates small structures should have this number; publish as a short, sharp methods paper.

---

## Cluster 2 — Domain Shift / Cross-Domain Transfer (8 survivors)

### IDEA-B-0053 — Ontology shift disguised as appearance shift across endoscopy datasets
**One-line:** Part of the endoscopy cross-dataset "domain gap" is label-definition shift, measurable by a 150-image bridge re-annotation. `[DM]`
**Survival Reason:** Could show a chunk of the domain-adaptation literature has been fitting a label-definition gap with appearance machinery. The bridge re-annotation instrument is cheap and reusable across dataset pairs.
**Major Risks:** Written protocols may be too vague to reproduce faithfully; annotator training becomes part of the measurement.
**Unresolved Questions:** How does the decomposition (ontology vs appearance) vary across dataset pairs and target classes?
**Required Experiments:** Re-annotate 150 images from dataset B under A's written protocol; evaluate A-trained models against both label versions; report the gap decomposition.
**Reviewer Opinion:** Under-asked question with an unusually direct experiment. If the ontology fraction is large, it should reshape how endoscopy DA papers are reviewed.

### IDEA-B-0054 — Which domain-distance metric actually predicts fine-tuning gain?
**One-line:** Benchmark FID/MMD/spectral/token-space distances as predictors of realized fine-tuning gains; hypothesis: the segmenter's own token space wins.
**Survival Reason:** Turns adaptation planning into a pre-annotation measurement, validated against realized gains rather than proxy shift labels. Absorbs the killed siblings 0147 (density predictor) and 0293 (layer-resolved variant).
**Major Risks:** Gains depend on target-task difficulty, requiring careful normalization; 15+ fine-tuning runs are the cost of honest validation.
**Unresolved Questions:** Does the best predictor transfer across model families, or is it model-specific by construction?
**Required Experiments:** Assemble 15+ target datasets; fine-tune one fixed recipe on each; correlate pre-computed candidate distances with realized gains; report predictor rankings with confidence intervals.
**Reviewer Opinion:** Workmanlike but foundational — the validated predictor becomes infrastructure for every later-stage adaptation project in this program.

### IDEA-B-0055 — Fog as a negative domain: does adapting to fog worsen smoke detection?
**One-line:** Fog-invariance training may transfer to smoke-invariance — robustness and sensitivity in direct conflict for confusable phenomena. `[CI·DM]`
**Survival Reason:** Formalizes a class of shift ("negative domain") the robustness literature has no name for, in a safety-critical setting. Simple, counter-intuitive, and measurable as a tradeoff curve.
**Major Risks:** The effect may be avoidable with trivially better class separation, making the finding short-lived; fog/smoke test sets with verified labels are limited.
**Unresolved Questions:** Is the coupling symmetric (smoke-sensitivity training harms fog robustness)? Does it generalize to other confusable pairs (steam/smoke, shadow/lesion)?
**Required Experiments:** Fine-tune with fog augmentation/adaptation at varying strengths; measure smoke TPR/FPR shifts on fixed test sets; map the robustness-specificity curve.
**Reviewer Opinion:** The named concept ("negative domain") may outlive the specific numbers. Cheap enough to run as a side experiment; high citation surface in safety-adjacent robustness work.

### IDEA-B-0057 — Token-statistics recalibration: a LayerNorm-era replacement for BN-based TTA
**One-line:** Matching per-layer token-population statistics to source values may recover shift loss for ViTs the way BN adaptation did for CNNs.
**Survival Reason:** If an affine token-statistic match recovers real shift loss, it is adopted everywhere within a year — a drop-in, optimization-free TTA primitive filling a genuine post-BN vacuum.
**Major Risks:** Affine corrections may be too weak for shifts altering token covariance structure; gains may concentrate on style-type shifts only (interacts with 0072's decomposition).
**Unresolved Questions:** Which layers' statistics matter? Does the mechanism remain stable on long test streams (vs TENT-style collapse)?
**Required Experiments:** Measure token-statistic drift across 5 shifts; apply per-layer affine matching; evaluate IoU recovery vs TENT and oracle fine-tuning.
**Reviewer Opinion:** The most immediately adoptable method-adjacent survivor in Cluster 2. Run together with 0072 to pre-classify which shifts it should work on.

### IDEA-B-0064 — Does classical UDA add anything on top of frozen foundation features?
**One-line:** Null-hypothesis audit: frozen-foundation baselines with pseudo-label filtering may match classic UDA machinery on most benchmark pairs. `[DM]`
**Survival Reason:** Could retire a heavily cited methodology where it no longer applies. Deflationary audits of this scale are rare, and the matched-budget design makes the null meaningful.
**Major Risks:** Benchmark selection bias — must include both stylistic and semantic shifts; UDA advocates will contest tuning fairness.
**Unresolved Questions:** Which shift types (identifiable in advance) still benefit from explicit UDA machinery?
**Required Experiments:** 6 UDA methods × 3 backbone regimes (scratch / supervised / foundation) × 4 benchmark pairs at matched compute; report marginal UDA gains per regime.
**Reviewer Opinion:** Expensive but decision-grade: the result directly reallocates effort for anyone doing segmentation DA after 2026. Strong workshop-keynote energy either way.

### IDEA-B-0072 — Amplitude-only adaptation: testing the "shift is style" hypothesis with Fourier-space adapters
**One-line:** A trainable amplitude-only Fourier filter as a capacity-constrained instrument measuring the "style fraction" of any domain shift. `[CI]`
**Survival Reason:** Turns folklore ("site shift is style") into a cheap standard diagnostic with a number attached. Doubles as a pre-screen for 0057 and for adaptation-method selection generally. Absorbs 0041 (frequency-band attribution).
**Major Risks:** Amplitude filters may capture semantic content via band-specific structures, blurring the interpretation; style fractions may be dataset-pair-idiosyncratic.
**Unresolved Questions:** Is the style fraction stable within shift families (all scanner pairs, all site pairs)? Can it be estimated without training (closed-form spectral statistic)?
**Required Experiments:** Train amplitude-filter-only adaptation across 6 shift pairs at matched budgets vs unrestricted LoRA; report gap-closure ratios as style fractions.
**Reviewer Opinion:** An instrument paper — the deliverable is a reusable measurement, not a method win. That is exactly what Stage 3 needs to route the other adaptation survivors.

### IDEA-B-0075 — Does SAM segment glass by its reflections? A reflection-swap diagnostic
**One-line:** Cue attribution by physical intervention: does transparency segmentation track reflected content (domain-fragile) or boundary cues (domain-stable)? `[HRHR·CI — protected]`
**Survival Reason:** Identifies the true generalization bottleneck for transparency perception; the answer redirects data collection (reflection diversity vs boundary diversity). Physical-intervention cue attribution is nearly absent from segmentation research.
**Major Risks:** Physical captures are labor-intensive; render-based substitutes may miss real reflection statistics; effect sizes may be object-dependent.
**Unresolved Questions:** Do polarizing-filter interventions and environment swaps agree? Does the cue mix shift with model scale?
**Required Experiments:** Capture the same transparent objects under varied reflection environments (or paired renders); evaluate frozen models; regress IoU on reflection-familiarity vs boundary-contrast measures.
**Reviewer Opinion:** Protected HRHR. The capture effort is real, but this is the rare experiment that yields a causal statement about what a foundation model uses. Coordinates with 0126 and 0159 as a transparency triad.

### IDEA-B-0078 — Language as a domain coordinate: text-described domains for zero-shot adaptation
**One-line:** Can a text description of a domain ("underwater, greenish turbidity") condition adaptation with zero target images? `[HRHR — protected]`
**Survival Reason:** Either opens a zero-data adaptation channel or measures the limit of language-vision domain alignment — both outcomes are valuable, and the question is basic science about VLM geometry, not a product pitch.
**Major Risks:** The method may learn generic robustness rather than description-specific adaptation; needs description-permutation controls. Highest R in Cluster 2.
**Unresolved Questions:** Which shift axes are language-describable (style yes, ontology no?); does describability correlate with the 0072 style fraction?
**Required Experiments:** Build text descriptions for 8 known shifts; train text-conditioned modulation on disjoint described domains; evaluate zero-shot on held-out described domains vs undescribed baselines with permuted-description controls.
**Reviewer Opinion:** Protected HRHR. The permutation control is the make-or-break design element — insist on it before any headline claim.

---

## Cluster 3 — Evaluation / Calibration / Uncertainty / Robustness (9 survivors)

### IDEA-B-0082 — A relabeling bootstrap for reporting rank stability under annotation noise
**One-line:** Resample plausible test-set relabelings from a fitted inter-rater noise model; report leaderboard rank-flip probabilities. `[CF·DM]`
**Survival Reason:** Gives the community an instrument to separate progress from noise — bootstrap over *label space*, which benchmarking practice simply lacks. Changes comparison norms, not just one paper. Absorbs 0013 and 0102.
**Major Risks:** Noise models fitted on multi-rater subsets may not represent the full test distribution; flip-probability thresholds are convention-setting and will be argued.
**Unresolved Questions:** How large must the multi-rater subset be for a stable noise model? Do flips concentrate among adjacent leaderboard pairs or reach deep?
**Required Experiments:** Fit boundary-noise models from multi-rater data on 2 benchmarks; resample 1,000 pseudo-labelings; recompute public-checkpoint rankings; report flip probabilities.
**Reviewer Opinion:** The single most norm-changing item in Cluster 3. Cheap, rigorous, and immediately reusable by every subsequent evaluation in this program.

### IDEA-B-0083 — Prompt-protocol sensitivity: how much do medical-SAM rankings depend on the click recipe?
**One-line:** Evaluate 8–10 public medical-SAM checkpoints under 5 prompt protocols; measure cross-protocol rank correlations. `[CF·DM]`
**Survival Reason:** Pure evaluation on public checkpoints; if rankings move materially, cross-paper comparison in this subfield is broken and a protocol-sensitivity index becomes mandatory reporting.
**Major Risks:** Some checkpoints embed protocol assumptions in preprocessing, complicating fair evaluation; the index itself needs a convention.
**Unresolved Questions:** Which protocol dimensions (point placement, box jitter, iteration policy) drive the instability?
**Required Experiments:** 8–10 checkpoints × 5 protocols × 3 datasets; cross-protocol rank correlations; per-method protocol-sensitivity index.
**Reviewer Opinion:** Run first — it is nearly free and its result conditions how every other prompted-model comparison here should be read. Complements 0089 (oracle inflation) and 0108 (hidden search).

### IDEA-B-0084 — Out-of-domain calibration of SAM's mask-quality head
**One-line:** SAM's predicted-IoU head gates auto-labeling and review pipelines everywhere and has never been audited off-domain. `[CF]`
**Survival Reason:** Load-bearing infrastructure with zero published calibration analysis. The transferable-recalibration hypothesis makes it constructive as well as critical.
**Major Risks:** Head behavior may differ across SAM versions/scales, fragmenting conclusions; recalibration transfer may fail for semantic (vs stylistic) shifts.
**Unresolved Questions:** Is overestimation smooth in shift magnitude (usable as a shift meter)? Does recalibration transfer across domains as hypothesized?
**Required Experiments:** Compare predicted vs actual IoU across 8 domains; fit shift-conditioned recalibration on 2; test transfer to the remaining 6.
**Reviewer Opinion:** An afternoon of compute against a dependency thousands of pipelines share. Highest ratio of affected-systems to experimental cost in the batch.

### IDEA-B-0089 — The oracle-prompt inflation factor in interactive segmentation reporting
**One-line:** GT-derived prompts (centroids, tight boxes) bound deployment performance from above by an unmeasured, task-dependent margin. `[DM]`
**Survival Reason:** Every interactive-segmentation number in the literature is an upper bound by an unknown factor; measuring and predicting that factor recalibrates the whole subfield. Absorbs 0004 and partially 0070.
**Major Risks:** User prompt quality varies with training and interface, adding variance; the predictive correction model may not transfer across tasks.
**Unresolved Questions:** Can the inflation factor be predicted from target-visibility statistics well enough to skip user studies per paper?
**Required Experiments:** Collect image-only prompts from users on 4 tasks; compute inflation factors; fit predictors from visibility features; validate on a held-out task.
**Reviewer Opinion:** The modest human-subjects cost is justified: this number converts an entire literature from optimistic to deployment-realistic. Coordinate prompt-log collection with 0193 to amortize cost.

### IDEA-B-0104 — Wrong-prompt behavior: does SAM fail loudly or silently under semantic prompt errors?
**One-line:** Under semantically wrong prompts, does confidence flag the mismatch or stay high (silent failure)? `[CF]`
**Survival Reason:** Defines and measures a safety property nobody reports; one evaluation pass produces the answer, and the auxiliary mismatch-detector gives a constructive follow-up.
**Major Risks:** "Intent" ground truth requires task context pure benchmarks lack; wrong-prompt suites must avoid strawman placements.
**Unresolved Questions:** Is silence architectural (conditional delineation by design) or trainable away? What consistency signal best flags mismatch?
**Required Experiments:** Build wrong-prompt suites with known intent labels; measure output-confidence distributions; train and evaluate a mismatch detector.
**Reviewer Opinion:** Should become a required safety table in interactive-model papers. Cheap, clean, and the "loud vs silent" framing is memorable enough to stick.

### IDEA-B-0108 — Honest zero-shot: quantifying hidden adaptation through validation-set prompt search
**One-line:** How much of "zero-shot" performance is validation-set prompt/hyperparameter search? Frozen universal settings may reorder leaderboards. `[DM]`
**Survival Reason:** Zero-shot claims drive deployment planning; this is the cheapest way to find out what they are worth. The corrected-bounds framing is constructive rather than purely accusatory.
**Major Risks:** Defining fair universal settings without disadvantaging any method family; authors will dispute the search-attribution accounting.
**Unresolved Questions:** How does the search contribution scale with validation-set size and domain gap?
**Required Experiments:** Re-evaluate public zero-shot pipelines under (a) published settings and (b) frozen universal settings chosen on disjoint domains; report the gap distribution.
**Reviewer Opinion:** A necessary hygiene audit with real teeth. Best published alongside 0083 as a two-part "what do reported numbers mean" study.

### IDEA-B-0110 — Efficient false-positive-rate estimation for rare-event monitoring via importance-sampled negatives
**One-line:** Stratified importance sampling over scene-condition space makes FP/day claims certifiable with orders-of-magnitude fewer labeled negatives.
**Survival Reason:** The gap between "demo" and "deployable" for rare-event systems is exactly this estimator. Reliability-engineering machinery imported to learned-vision certification — genuinely missing.
**Major Risks:** Unmodeled risk strata (unknown unknowns) escape the proposal distribution; validation requires at least one long-duration fully labeled log.
**Unresolved Questions:** How robust is the estimator to proposal misspecification? Can strata be discovered rather than hand-defined?
**Required Experiments:** Fit condition-strata proposals from unlabeled field video; run stratified evaluation; compare estimator variance/bias against exhaustive counts on a labeled long-duration subset.
**Reviewer Opinion:** Less flashy than its neighbors but the one insurers and regulators would actually use. Keep despite the field-data dependency; partial validation on public long videos is feasible.

### IDEA-B-0114 — Seed variance of PEFT fine-tuning versus reported effect sizes
**One-line:** If cross-seed variance rivals claimed inter-method gaps, the PEFT-variant literature is statistically unsupported — and this is measurable now. `[DM]`
**Survival Reason:** A fast-growing literature reports single-seed comparisons on small datasets; the variance audit with minimum-detectable-effect tables sets reporting standards with numbers, not exhortation.
**Major Risks:** Full grid compute cost (10 seeds × 4 methods × 4 sizes) — factorial subsampling may be needed; findings could be dismissed as dataset-specific.
**Unresolved Questions:** How does variance scale with dataset size and with PEFT parameter count? Are some PEFT families intrinsically lower-variance?
**Required Experiments:** 10 seeds × 4 PEFT methods × 4 dataset sizes; publish variance components and minimum detectable effects.
**Reviewer Opinion:** The methodological conscience of Cluster 8's whole topic area. Its tables will be cited defensively by everyone; that is impact.

### IDEA-B-0120 — Are SAM's multimask candidates a valid uncertainty sample?
**One-line:** Coverage-test candidate spread as an uncertainty interval; hypothesis: it collapses exactly where the model is most wrong (OOD). `[CF]`
**Survival Reason:** Either certifies a free uncertainty mechanism thousands of users already rely on, or documents its unsafe failure mode. Formal coverage testing of multimask spread has simply not been published. Anchors the killed 0092 thread.
**Major Risks:** Only 3 candidates per prompt limits distributional resolution; coverage tests need careful error-distribution definitions.
**Unresolved Questions:** Can candidate spread be recalibrated post hoc, or is the collapse informationless? How does it compare to conformal baselines per unit compute?
**Required Experiments:** In- and out-of-domain coverage of candidate-spread intervals against true error distributions; compare with ensembles and conformal methods.
**Reviewer Opinion:** Pairs naturally with 0337 (diffusion posteriors) as the "is free uncertainty real" duo. Cheap, safety-relevant, decision-grade.

---

## Cluster 4 — Representation Mismatch (7 survivors)

### IDEA-B-0122 — Angular aliasing: patch-grid anisotropy against thin oblique structures
**One-line:** Thin-structure quality may vary periodically with orientation relative to the ViT patch lattice, localizing to the embedding stage. `[CI·CF]`
**Survival Reason:** A lattice-induced bias would touch every ViT dense predictor on safety-critical thin targets (vessels, wires, catheters); synthetic controls make it cheap to establish or kill.
**Major Risks:** Real-image acquisition anisotropy may mask the lattice effect — synthetic controls are essential; effect may vanish above patch-width structures.
**Unresolved Questions:** Does rotation augmentation suppress or merely average the periodicity? Do overlapping-patch or anti-aliased stems fix it?
**Required Experiments:** Rotate-and-evaluate on synthetic and real thin structures across model families; fit orientation-response curves; ablate embedding variants.
**Reviewer Opinion:** Crisp physics-of-the-architecture question with a clean kill test. Coordinates with 0305 (resolution aliasing) as the "token lattice artifacts" pair.

### IDEA-B-0124 — Text-space collinearity predicts open-vocabulary confusion for amorphous classes
**One-line:** Smoke/steam/fog confusion may be upper-bounded by CLIP text-anchor geometry, not visual features — testable by anchor substitution. `[CF]`
**Survival Reason:** Localizes a safety-critical confusion to a specific, fixable component (text anchors vs visual encoder), redirecting effort from data collection to anchor engineering. Absorbs 0033's linguistic-tail thread.
**Major Risks:** Controlling for visual similarity requires a defensible independent visual metric; anchor substitution must not smuggle in extra supervision.
**Unresolved Questions:** Does the collinearity bound hold across text encoders? Can visually derived anchors be constructed without labeled confusion pairs?
**Required Experiments:** Measure confusion matrices for scattering-phenomena classes; regress on text similarity vs visual similarity; intervene by substituting anchor types.
**Reviewer Opinion:** The most surgical causal design in Cluster 4. A positive result gives smoke/steam discrimination a concrete fix; a negative exonerates text space and refocuses on features.

### IDEA-B-0126 — Can single-mask decoders represent layered scenes? Transparency as a representation test
**One-line:** If two-layer probes decode glass + transmitted background from frozen features, transparency failure is an output-format problem, not a feature problem. `[CI]`
**Survival Reason:** If confirmed, an entire research direction (better transparency features) is misallocated and the fix is layered output formats and supervision. Format-vs-representation is a genuinely underexamined axis.
**Major Risks:** Layered ground truth is scarce — may require purpose-built captures or renders; probe capacity must be controlled to avoid "probing proves anything" critiques.
**Unresolved Questions:** How much layered supervision does a production two-layer head need? Does the result extend to other layered phenomena (reflections, shadows, smoke-over-background)?
**Required Experiments:** Train small two-layer probes on frozen SAM/DINOv2 features on layered-annotated data; compare against full fine-tuning and chance controls.
**Reviewer Opinion:** High conceptual leverage per GPU-hour. With 0075 and 0159, forms a coherent transparency program with attribution, supervision, and format angles covered.

### IDEA-B-0128 — Is the prompt-to-mask map continuous? Lipschitz geometry of interactive segmentation
**One-line:** Map discontinuity manifolds of the click-to-mask function; discontinuity density may predict human interaction cost better than one-shot IoU. `[CF]`
**Survival Reason:** Defines a geometric usability property of promptable models that training could optimize but nobody measures. Absorbs 0281 (off-center clicks) and 0095's empirical half.
**Major Risks:** Dense prompt grids are compute-heavy; correlation with human effort needs interaction logs, adding a data dependency.
**Unresolved Questions:** Are discontinuities semantic (part-whole switches) or artifacts? Can training regularize them away without hurting ambiguity coverage?
**Required Experiments:** Dense prompt-grid evaluation on representative images; map basin structure; correlate discontinuity statistics with logged human interaction effort.
**Reviewer Opinion:** Elegant instrument; the usability-prediction claim is what elevates it beyond a curiosity. Sampling-strategy validation deserves early attention.

### IDEA-B-0129 — Small-structure failure: information absent or decoder-limited?
**One-line:** Oracle probes on frozen features split small-lesion failure into decoder-limited (fixable) vs information-absent (needs resolution) regimes.
**Survival Reason:** Splits two expensive research directions (better decoders vs higher resolution) with evidence instead of assumption. The crossover size is a directly actionable deliverable. Absorbs 0289 and 0313's territory.
**Major Risks:** Probe overfitting inflates decodability estimates — strict held-out validation required; crossover may vary across modalities.
**Unresolved Questions:** Is the crossover stable across encoder families and input resolutions? Does decoder-limited failure concentrate in specific error types?
**Required Experiments:** Train overparameterized pixel-level probes on frozen features across lesion-size strata; compare probe vs production-decoder recall curves; identify the crossover.
**Reviewer Opinion:** The program's compass for small-structure work: whichever regime dominates, several other survivors (0288, 0338) get their interpretation from this result.

### IDEA-B-0132 — Where do VLMs lose spatial detail? Layer-wise localization decay in vision-language models
**One-line:** Trace pixel-localizable information through LLaVA-style stacks to find where dense capacity is destroyed (projector? resampler?) and tap pre-collapse.
**Survival Reason:** Dense-capable VLMs are being built now on intuition; this replaces it with a decay map and validated tap points. Basic-science measurement with immediate engineering consumers.
**Major Risks:** Architecture heterogeneity across VLMs may resist a unified narrative; probing methodology choices will be contested.
**Unresolved Questions:** Is collapse abrupt (bottleneck stages) or gradual (through the LM)? Do tap-point heads recover boundary-grade localization or only coarse grounding?
**Required Experiments:** Probe boundary/mask decodability at every stage of 3 open VLMs; localize collapse; validate by attaching dense heads pre- vs post-collapse.
**Reviewer Opinion:** Timely and load-bearing for the field's biggest current engineering race. Publish the decay maps as reusable artifacts.

### IDEA-B-0136 — Luminance-only smoke: which color channels actually carry the signal?
**One-line:** Smoke perception may be achromatic — color channels mainly importing FP risk (sunsets, dust) — testable on frozen models first. `[CI·CF]`
**Survival Reason:** Counter-intuitive, immediately actionable for a deployed safety application, and testable in stages (frozen evaluation before retraining). Anchors the color-cue thread (0287 killed into it).
**Major Risks:** Some smoke types (chemical fires) have genuine chromatic signatures that luminance-only sacrifices; dataset color statistics may drive results.
**Unresolved Questions:** Does the conclusion hold across day/night and sensor types? Is decorrelated color (chroma-only) informative as a control?
**Required Experiments:** Evaluate and retrain on {RGB, luminance-only, chroma-only, decorrelated} inputs across smoke datasets with FP-stratified reporting.
**Reviewer Opinion:** The kind of one-figure result deployment teams act on immediately. Cheap; run early.

---

## Cluster 5 — Multimodal Supervision (7 survivors)

### IDEA-B-0156 — The exchange rate between radiology reports and pixel labels
**One-line:** Iso-performance grids price report-derived supervision in units of expert pixel labels, per finding type.
**Survival Reason:** Prices an idle hospital-scale data asset with a clean experimental design; directly changes annotation budget decisions. Absorbs 0014 and 0168.
**Major Risks:** Report-parsing errors contaminate the priced supervision; exchange rates may vary across institutions' reporting styles.
**Unresolved Questions:** How does the rate move with better report parsers (is it a floor or a ceiling)? Does it transfer across finding types as predicted (focal high, diffuse low)?
**Required Experiments:** On a dataset with reports and masks, train models across (n_masks × n_report-only) grids; fit iso-performance curves; derive exchange rates per finding type.
**Reviewer Opinion:** "Supervision pricing" is a framing with legs — expect follow-on work pricing other channels (this batch alone offers 0182's negations and 0159's depth-invalidity).

### IDEA-B-0159 — Missing depth as free supervision: exploiting RGB-D sensor failure for transparency
**One-line:** Invalid-depth pixels are physics-generated transparency labels; filtered and noise-characterized, they could yield the largest transparency corpus in existence. `[HRHR — protected]`
**Survival Reason:** Physics-generated labels at zero annotation cost, aimed at a label-starved problem. If the confounder filtering works, this changes transparency research's data economics permanently.
**Major Risks:** Confounder filtering (range limits, absorption, occlusion shadows) may remove most volume or leave structured noise that biases learned cues.
**Unresolved Questions:** What fraction of invalid-depth pixels are transparency-caused across public corpora? Is the residual noise structure learnable-around (connects to 0001's structured-noise result)?
**Required Experiments:** Harvest invalid-depth masks from public RGB-D corpora; characterize label noise against transparency-benchmark GT; train RGB models on harvested vs manual labels at matched scale.
**Reviewer Opinion:** Protected HRHR — the highest-expected-value data idea in the batch. Even partial success (noisy corpus + noise model) is a community resource.

### IDEA-B-0162 — Polarization-taught transparency: can physics-privileged training transfer to plain RGB?
**One-line:** Train with polarization as privileged supervision; measure the fraction of the polarization advantage that survives RGB-only inference. `[HRHR — protected]`
**Survival Reason:** Either yields a capture-once-deploy-everywhere recipe or proves the polarization cue has no RGB correlate — a clean, valuable dichotomy either way. Privileged-modality transfer quantification is missing for transparency.
**Major Risks:** The polarization advantage may reside in cues with no RGB correlate, yielding near-zero transfer (the honest null); paired data capture is nontrivial.
**Unresolved Questions:** Which RGB cues does the privileged model learn to weight (interpretability hook to 0075)? Does transfer fraction grow with corpus size?
**Required Experiments:** Capture or source paired polarization-RGB data; train privileged vs RGB-only models; evaluate both on RGB test sets; quantify transferred fraction.
**Reviewer Opinion:** Protected HRHR. Transfer-fraction-as-deliverable makes even a modest result quotable. Sequence after 0075 so the cue attribution informs what "transfer" should mean.

### IDEA-B-0174 — Does text supervision smooth away boundary precision? The semantic-blur hypothesis
**One-line:** Dose-response test: heavier language supervision may degrade boundary metrics at matched region accuracy — an objective-design artifact, not an inherent cost. `[CI·DM]`
**Survival Reason:** Names the unmeasured cost side of the rush toward language-native dense models, with a falsifiable dose-response and a proposed remedy (boundary auxiliaries) that turns critique into design guidance.
**Major Risks:** Boundary degradation may be confounded with mask-quality differences across supervision sources; dose ladders require multiple training runs.
**Unresolved Questions:** Is the effect monotone in text-loss weight? Does it interact with 0132's collapse points (same mechanism seen twice)?
**Required Experiments:** Train across a text-loss-weight ladder at matched data; measure region-vs-boundary metric divergence; add boundary-specific auxiliaries and re-measure.
**Reviewer Opinion:** The right skeptical question at the right time. The auxiliary-supervision arm is essential — without it this reads as anti-VLM; with it, as engineering guidance.

### IDEA-B-0182 — Absence statements as supervision: teaching models what is not there
**One-line:** Mine "no pneumothorax"-style certified negations from reports as class-specific hard-negative supervision against hallucinated segmentations.
**Survival Reason:** Report negations are free, expert-authored, and aimed precisely at the hallucinations that cause alarm fatigue. Negation mining exists for classification; dense hallucination control is untouched.
**Major Risks:** Negations are sometimes hedged or wrong; extraction quality bounds supervision purity; sensitivity must be monitored for over-suppression.
**Unresolved Questions:** What is the exchange rate of a certified absence vs a generic negative (connects to 0156's pricing framework)? Does the benefit persist under domain shift?
**Required Experiments:** Mine negative findings; train with/without absence losses; measure class-conditional FP rates on certified-absent cases plus overall sensitivity.
**Reviewer Opinion:** Practical, cheap where report corpora exist, and mechanistically clear. With 0017 and the killed 0308, forms the "what negatives teach" thread — this is its strongest member.

### IDEA-B-0184 — Contrast-enhancement differencing as automatic vessel ground truth — and its hidden bias
**One-line:** Contrast physics yields free vessel labels that are physiologically selective: models inherit blindness to non-enhancing (occluded) segments — the clinical cases that matter. `[CI·DM]`
**Survival Reason:** A paradigm case of physically generated labels whose bias directly opposes the clinical use, with the correction (fraction of expert pathological labels) priced by the same experiment.
**Major Risks:** Pre/post-contrast registration is error-prone near vessels, contaminating both the labels and the bias measurement.
**Unresolved Questions:** How large a pathological-label fraction disproportionately corrects the bias? Does the bias survive when enhancement labels are mixed with standard datasets?
**Required Experiments:** Build enhancement-derived labels; train and evaluate on healthy vs occlusion-rich strata; sweep the corrective expert-label fraction.
**Reviewer Opinion:** The cautionary counterpart to 0159's enthusiasm — physics-generated labels encode physics-generated selection biases. The pair should be read (and possibly published) together.

### IDEA-B-0185 — Knowledge conflict in VLM segmenters: when text priors contradict image evidence
**One-line:** Controlled conflicts (textbook anatomy vs diseased image) measure whether dense VLMs regress toward the prior exactly on abnormal cases. `[HRHR·DM — protected]`
**Survival Reason:** "Prior-conforming segmentation of abnormal anatomy" is the worst conceivable medical-VLM failure mode and is untested. Knowledge-conflict methodology from NLP ports naturally but nobody has done it densely.
**Major Risks:** Constructing convincing conflict cases requires clinical curation to avoid strawman stimuli; scale-trend claims need multiple model sizes.
**Unresolved Questions:** Is over-trust monotone in language-model scale? Can evidence-weighting be recalibrated without retraining?
**Required Experiments:** Assemble typical/atypical anatomy pairs with matched image-quality ladders; measure prior-conformity vs evidence strength; compare across model scales.
**Reviewer Opinion:** Protected HRHR·DM. If dense VLMs are heading to clinics, this experiment must exist first. The scale-dependence sub-claim could be its most explosive finding.

---

## Cluster 6 — Synthetic Data Pitfalls (6 survivors)

### IDEA-B-0186 — Does generative augmentation actually cover the tail it promises to fix?
**One-line:** Diffusion augmentation may concentrate near dataset modes — volume without coverage — leaving rare-presentation performance untouched. `[DM]`
**Survival Reason:** If synthesis reproduces the skew it is prescribed to fix, the field's main scarcity remedy is a placebo. Per-stratum (not mean) reporting is the methodological point, and it generalizes beyond medicine.
**Major Risks:** Defining clinically meaningful rarity strata requires expert partnership; coverage metrics in feature space are contestable.
**Unresolved Questions:** Can tail coverage be improved by conditioning/guidance, or is it a training-distribution ceiling (connects to 0191's dynamics)?
**Required Experiments:** Curate rarity-stratified references; compute generator coverage per stratum; train with synthetic augmentation; report per-stratum segmentation deltas.
**Reviewer Opinion:** The cluster's thesis statement. Its per-stratum reporting discipline should be imposed on every synthetic-data claim this program touches.

### IDEA-B-0189 — The inpainting fingerprint: do models learn the lesion or the paste?
**One-line:** A fingerprint classifier plus real-only test sets detect whether inpainting-augmented models learn synthesis artifacts instead of pathology. `[CI·CF]`
**Survival Reason:** A circularity flaw in a fast-spreading augmentation practice, detectable with a cheap classifier. Standard evaluation literally cannot see the failure; this audit can. Absorbs 0206.
**Major Risks:** Best-generator fingerprints may be undetectable (a reassuring but modest result); artifact-suppression arms multiply conditions.
**Unresolved Questions:** Does fingerprint reliance scale with augmentation fraction? Are frequency-space fingerprints the right detector family?
**Required Experiments:** Train fingerprint detectors on inpainted-vs-real patches; compare augmented-model performance on real vs synthetic test lesions; test noise-matched blending.
**Reviewer Opinion:** Cheap, decisive, and the "learn the paste" phrase will carry it. A mandatory pre-flight check for the whole inpainting-augmentation literature.

### IDEA-B-0190 — The synthetic poisoning threshold: robustness costs of synthetic fractions
**One-line:** Map OOD robustness vs synthetic training fraction; hypothesize a threshold where in-domain gains coexist with silent robustness decay.
**Survival Reason:** The monitoring instrument the field needs before synthetic-heavy training becomes irreversible practice. The probe-based threshold detector (no OOD labels needed) is the constructive deliverable.
**Major Risks:** Thresholds may vary so strongly across generators that only the methodology generalizes — acceptable but limits headline strength.
**Unresolved Questions:** Is the threshold predictable from generator-classifier probe accuracy alone? Does mixing generators move it (the killed 0215's question, answerable cheaply here)?
**Required Experiments:** Train across synthetic-fraction ladders with two generator families; evaluate in-domain, cross-site, and corruption metrics; validate the probe detector.
**Reviewer Opinion:** With 0186 and 0191, completes the synthetic-data safety triptych: coverage, dose, and dynamics. Fund as a unit.

### IDEA-B-0191 — Error amplification in self-consuming segmentation pipelines
**One-line:** Multi-generation auto-labeling loops: boundary biases may amplify geometrically while random errors wash out — with a measurable fresh-label injection rate that stabilizes.
**Survival Reason:** Defines the stability conditions of the data flywheel everyone is now building on. Generative-model collapse theory has no dense-prediction analogue; this builds it empirically.
**Major Risks:** Multi-generation training compute; dynamics may depend on loop details (filtering, thresholds), demanding a small design matrix.
**Unresolved Questions:** Which error taxonomy (bias/variance × boundary/region) best predicts amplification? Is the safe injection rate constant or generation-dependent?
**Required Experiments:** Run 5-generation loops on datasets with held-out truth; track error decomposition per generation; test fresh-data injection rates.
**Reviewer Opinion:** The most forward-looking item in the cluster — its stability conditions become design rules for every auto-labeling pipeline, including several proposed by other survivors (0320, 0329).

### IDEA-B-0193 — Programmatic prompts versus human clicks: the prompt-distribution gap in SAM-style training
**One-line:** Training with synthetic prompt sampling vs human-realistic prompt distributions — an unquantified domain gap inside the interaction channel, with a nearly free fix.
**Survival Reason:** A training-recipe variable nobody reports, aimed at the deployment gap inside the interface. The fix (learned human-prompt model at training time) costs nothing at annotation time. Absorbs 0292.
**Major Risks:** Human prompt distributions vary across tools and expertise; a single target distribution may not exist.
**Unresolved Questions:** How much prompt-log data suffices to fit a useful human-prompt model? Does the gap concentrate in early clicks on ambiguous targets as hypothesized?
**Required Experiments:** Collect human prompt logs; fit a prompt-distribution model; fine-tune segmenters with programmatic vs human-modeled prompts; evaluate under real human prompting.
**Reviewer Opinion:** Shares data collection with 0089 — run them as one user-study effort. Quietly important: it is the training-side mirror of 0089's evaluation-side claim.

### IDEA-B-0200 — Too-clean ground truth: when perfect synthetic labels teach the wrong tolerance
**One-line:** Pixel-perfect rendered labels may teach over-sharp boundary posteriors; degrading labels toward annotator statistics may *improve* real-data performance. `[CI]`
**Survival Reason:** Inverts a data-quality intuition and prescribes deliberately degrading labels — cheap to run, hard to ignore, and connects synthetic-data practice to the annotation-noise literature (0037, 0082).
**Major Risks:** The effect may be small relative to the synthetic-real appearance gap it rides on; annotator-noise models must be fitted per target dataset.
**Unresolved Questions:** Is the mechanism calibration (posterior sharpness) or accuracy? Does matched-noise training also improve downstream calibration under shift?
**Required Experiments:** Train on perfect vs annotator-noise-matched synthetic labels; evaluate accuracy and boundary-confidence calibration on human-annotated real data across noise models.
**Reviewer Opinion:** Small, surprising, and mechanistically clean. A good early win candidate for the synthetic-data thread.

---

## Cluster 7 — Detection Limitations (6 survivors)

### IDEA-B-0217 — The box-to-mask error transfer function
**One-line:** Characterize how detector box errors propagate through prompt conditioning into mask failure; train the segmenter under the detector's *measured* error distribution.
**Survival Reason:** Detect-then-segment is the dominant production architecture and its interface is unmodeled. The zero-inference-cost fix (noise-distribution matching at training time) makes this immediately deployable. Absorbs 0071 and 0103.
**Major Risks:** Detector error distributions drift over time, so the matching must be maintained; response surfaces may be strongly target-geometry-dependent.
**Unresolved Questions:** Where exactly is the small-target box-error "cliff"? Does matched-noise training generalize across detectors or overfit to one error profile?
**Required Experiments:** Measure detector error distributions; map mask-vs-box-perturbation response surfaces; retrain segmenters under matched vs default noise; compare end-to-end.
**Reviewer Opinion:** The most production-relevant survivor in Cluster 7. Its methodology (interface-error matching) generalizes to any composed pipeline, including 0331's SR-then-segment.

### IDEA-B-0219 — Is duplicate suppression the binding constraint for amorphous-target detection?
**One-line:** NMS assumes one box per discrete object; fragmenting plumes violate this, and oracle-suppression accounting can attribute the loss to the suppression stage. `[CI]`
**Survival Reason:** Attributes a chronic failure to a specific replaceable pipeline stage rather than to feature quality where effort currently goes. Suppression-stage attribution has never been isolated for non-discrete targets.
**Major Risks:** Instance ground truth for fragmenting plumes is itself convention-laden, complicating the "correct detection" definition.
**Unresolved Questions:** How much of the loss do set-prediction architectures actually recover at matched capacity? Is the loss monotone in fragmentation degree?
**Required Experiments:** Instrument pipelines to log pre/post-suppression candidates on fragmented-plume scenes; compute suppression-stage losses; compare against DETR-style models at matched capacity.
**Reviewer Opinion:** Clean pipeline-stage attribution with a deflationary flavor. If confirmed, redirects amorphous-detection effort from features to suppression design — a cheap redirection with large downstream savings.

### IDEA-B-0223 — Assigner-induced bias against elongated objects
**One-line:** Label-assignment rules (IoU thresholds, center sampling) starve extreme-aspect-ratio objects of gradient; ratio-conditional assignment may recover the gap with no architecture change. `[CI]`
**Survival Reason:** A training-logic fix, universal across detectors, for a safety-critical object family (catheters, wires) — and cheap to instrument via gradient-flow accounting.
**Major Risks:** Multiple assigner families exist; findings must replicate across them for generality; gains may partially overlap known anchor-design fixes.
**Unresolved Questions:** Does assignment starvation fully explain the cross-detector consistency of elongated-object failure, or only part?
**Required Experiments:** Instrument assignment statistics by aspect ratio across detector families; train with ratio-conditional assigners; compare per-shape performance at matched everything-else.
**Reviewer Opinion:** The rare mechanistic detection paper whose remedy costs nothing at inference. High acceptance odds; run the instrumentation pass first — it alone is publishable.

### IDEA-B-0226 — Detection recall as a function of boundary contrast: the camouflage-transparency continuum
**One-line:** Camouflage, transparency, and low-contrast lesion detection may lie on one contrast-recall law; curve collapse would merge three literatures. `[DM]`
**Survival Reason:** If the curves collapse, three separate communities should consolidate methods and benchmarks; if not, the differences become precise instead of anecdotal. Either outcome restructures how these problems are framed.
**Major Risks:** A single contrast measure may not capture the distinct physics of the three phenomena — the measure's construct validity is the paper's foundation.
**Unresolved Questions:** What is the right standardized boundary-contrast measure? Do method improvements in one literature actually shift the others' curves (the transfer test)?
**Required Experiments:** Compute standardized contrast measures across camouflage/transparency/lesion benchmarks; plot recall curves per method family; test curve collapse statistically.
**Reviewer Opinion:** Ambitious unification with real falsification criteria. The disagreement it will generate is a feature: even partial collapse forces the literatures to talk to each other.

### IDEA-B-0233 — What does a detector add over change detection for static-camera monitoring?
**One-line:** At matched FP budgets, background-model change detection may recover most true events on static cameras, relegating deep detection to change triage. `[DM·CI]`
**Survival Reason:** A deflationary question with large compute stakes that the monitoring literature has never asked cleanly. The change-gated architecture gives the audit a constructive output.
**Major Risks:** Modern PTZ and auto-exposure cameras violate static-background assumptions — results must be stratified by camera behavior; slow-onset events need careful handling.
**Unresolved Questions:** What fraction of detector-only detections are slow-onset events that defeat background models? How do the compute savings scale fleet-wide?
**Required Experiments:** Run background-model, detector-only, and change-gated pipelines on long-duration static-camera footage; decompose detections by discovering mechanism; compare compute and FP profiles.
**Reviewer Opinion:** The kind of role-decomposition study that saves deployments real money and embarrasses nobody who reads it carefully. Field-data access is the main scheduling constraint.

### IDEA-B-0241 — Prevalence-conditioned prompting: hallucinated detections under leading questions
**One-line:** "Find the smoke" in smoke-free images: hallucination grows with prompt assertiveness and exceeds what thresholding removes; absence-option protocols may cut it severalfold. `[CI·CF]`
**Survival Reason:** Text-driven monitoring is productizing now; this measures its worst failure mode before deployment norms solidify. Cheap (evaluation-only) with a directly testable protocol fix. Absorbs 0166's hallucination angle and complements 0104.
**Major Risks:** Distinguishing hallucination from genuine ultra-low-contrast detection requires rigorously verified absence — negative-set curation is the load-bearing work (shared with 0017).
**Unresolved Questions:** Is the leading-question effect model-scale-dependent? Do calibrated abstention options degrade sensitivity on true positives?
**Required Experiments:** Query detectors/VLMs on curated absent-target suites with prompt-assertiveness ladders; measure hallucination-rate curves; test absence-option protocols at fixed sensitivity.
**Reviewer Opinion:** Among the most urgent items in the batch given product timelines. Share negative-set curation with 0017 and 0110 to amortize the expensive part.

---

## Cluster 8 — Parameter Efficiency vs Quality (9 survivors)

### IDEA-B-0248 — Does PEFT protect zero-shot generality? The retention-adaptation frontier
**One-line:** At strictly matched target performance, does the low-rank constraint causally preserve zero-shot capability, or does "LoRA forgets less" just mean undertraining? `[DM]`
**Survival Reason:** Retention is the property that lets one foundation model serve many masters, and the folklore supporting current practice rests on confounded comparisons. The matched-target design plus rank-indexed retention law is the right instrument.
**Major Risks:** Matching target performance exactly across methods requires dense checkpointing and careful selection — the design's difficulty is its confound control.
**Unresolved Questions:** Is retention lawful in effective update rank as hypothesized? Does the law hold across domains and model scales?
**Required Experiments:** Adapt to 4 domains at swept budgets; select checkpoints at matched target IoU; evaluate zero-shot suites; fit retention-vs-effective-rank curves.
**Reviewer Opinion:** This is the study that turns adapter deployment from folklore to engineering. Its design discipline (matched-target selection) should be inherited by 0260 and 0272.

### IDEA-B-0251 — Predicting adapter-merging success from task-vector geometry
**One-line:** Merge degradation may be forecastable from subspace angles between adapter updates — merge-or-retrain decided from weights alone.
**Survival Reason:** Adapter consolidation is a routine operational need currently decided by trial and error; a validated weight-space predictor makes it a calculation. Anchors the killed composition thread (0065, 0254).
**Major Risks:** Geometry may predict interference but miss data-conflict effects (label-convention clashes) that also break merges — the 0006 result is the needed companion.
**Unresolved Questions:** Does orthogonalization-before-averaging rescue the risky regime as hypothesized? Do predictors transfer across ranks and model scales?
**Required Experiments:** Train adapters on 8 datasets; merge all pairs/triples; regress merge quality on geometric predictors; test orthogonalization rescue on worst cases.
**Reviewer Opinion:** Concrete, useful, and self-contained. The convention-clash caveat should be tested explicitly by including one deliberately convention-mismatched pair.

### IDEA-B-0253 — Attention adapts "where", MLP adapts "what": a causal placement test
**One-line:** Error-type-stratified evaluation of attention-only vs MLP-only adaptation, testing a double dissociation that would ground PEFT placement in mechanism.
**Survival Reason:** The placement debate is unresolved because it is asked with aggregate metrics — the wrong instrument. A double dissociation would explain contradictory prior findings and yield an error-profile-based placement rule. Anchors 0047/0247/0264.
**Major Risks:** Segmentation error taxonomies are imperfect; the dissociation may be partial, demanding careful statistics rather than a clean headline.
**Unresolved Questions:** Is the dissociation stable across architectures? Can the error-profile diagnostic be computed from zero-shot behavior alone?
**Required Experiments:** Adapt attention-only vs MLP-only across domains with error-typed evaluation suites; test the dissociation; validate the placement rule prospectively.
**Reviewer Opinion:** The most scientific framing of the placement question available. Even a partial dissociation converts placement from folklore into diagnosis.

### IDEA-B-0257 — The boundary tax of parameter efficiency
**One-line:** PEFT that matches full fine-tuning on mIoU may systematically underperform on boundary metrics — an equivalence artifact of region-dominated metrics. `[CI·DM]`
**Survival Reason:** Boundary precision is what medical and industrial users pay for; if the tax exists, PEFT equivalence claims systematically overpromise for exactly those users. Metric-stratified auditing with a frequency mechanism is cheap and decisive.
**Major Risks:** Boundary metrics are noisier, requiring larger evaluation sets for significance; the frequency-rank mechanism needs careful controls.
**Unresolved Questions:** Do boundary-targeted PEFT variants (higher rank in high-resolution pathways) eliminate the tax as hypothesized? How does the tax scale with rank?
**Required Experiments:** Adapt with a PEFT ladder vs full FT on boundary-critical tasks; report region and boundary metrics separately; test frequency-targeted variants.
**Reviewer Opinion:** The hidden-cost audit this literature owes its clinical users. Combine with 0114's variance tables for a definitive "how to report PEFT results" pair.

### IDEA-B-0260 — Do adapters overfit sites harder? Update locality and out-of-site transfer
**One-line:** At matched in-site IoU, concentrated low-rank updates may encode site shortcuts *more* sharply than full fine-tuning — inverting the conservatism folklore. `[CI·DM]`
**Survival Reason:** Determines safe deployment patterns for the dominant adaptation method in hospital networks. The predicted single-site/multi-site reversal and the fingerprint-alignment diagnostic make it mechanistic, not just observational.
**Major Risks:** Matching in-site performance while controlling optimization intensity is delicate; site-fingerprint directions must be defined defensibly.
**Unresolved Questions:** Does the effect reverse with multi-site adaptation data as predicted? Is the fingerprint-alignment diagnostic usable prospectively?
**Required Experiments:** Adapt via PEFT and full FT on single-site data to matched in-site IoU; evaluate across held-out sites; repeat with multi-site data; test the diagnostic.
**Reviewer Opinion:** The counter-intuitive sibling of 0248 — run them on shared infrastructure. If both hold, the field gets a two-axis (retention, transfer) characterization of update geometry.

### IDEA-B-0269 — Adapting the choice, not the masks: selection-head-only adaptation for granularity conventions
**One-line:** Many "domain gaps" may be convention gaps: the right candidate is generated but wrongly selected — fixable with tens of labels on the selection head. `[CI·CF]`
**Survival Reason:** The oracle-candidate audit is nearly free and could reclassify part of the medical-SAM adaptation literature as selection problems solved with generation-sized tools. The routing diagnostic (convention-type vs appearance-type gaps) is a lasting contribution. Absorbs 0093 and 0283.
**Major Risks:** Real domains mix gap types; the clean dichotomy may blur, demanding a continuous decomposition rather than a binary router.
**Unresolved Questions:** What fraction of published medical-SAM gaps are convention-type by the oracle audit? Does selection-only adaptation stay stable as conventions drift?
**Required Experiments:** Audit oracle-candidate performance across domains; adapt selection-only vs full on both gap types; validate the routing diagnostic prospectively.
**Reviewer Opinion:** The best effort-to-insight ratio in Cluster 8. The audit alone (before any adaptation) is a strong short paper; insist it be run across many public domains.

### IDEA-B-0270 — Is the input stem the whole story for modality shift? Stem-only adaptation
**One-line:** If stem-only adaptation recovers most of full adaptation for semantics-preserving modality shifts, the transformer is an input-agnostic computer and modality gap splits into interface vs semantics. `[CI]`
**Survival Reason:** A clean falsifiable decomposition with immediate practical consequence (stem engineering replaces whole-network adaptation for a definable shift class). Anchors 0042's grayscale thread.
**Major Risks:** Stem capacity choices (kernel structure) may drive results more than the interface principle — a stem-design ladder is needed as a control.
**Unresolved Questions:** Where exactly do "semantics-altering" shifts begin (windowed CT vs histology)? Does the recovery fraction predict from 0054's distance metrics?
**Required Experiments:** Adapt stem-only vs LoRA vs full across 6 modality shifts at matched data; decompose recovery fractions; correlate residuals with semantic-shift measures.
**Reviewer Opinion:** Conceptually the cleanest experiment in the cluster. Its interface/semantics split gives 0054, 0072, and 0253 a shared vocabulary for classifying shifts.

### IDEA-B-0272 — Capacity as regularization: are small adapters implicitly noise-robust?
**One-line:** Under label noise, the PEFT-vs-full-FT gap may reverse sign — constrained updates cannot fit structured annotation errors, making PEFT accuracy-optimal, not a compromise. `[CI]`
**Survival Reason:** Inverts how practitioners frame the efficiency-quality tradeoff exactly where medical labels are noisiest. Controlled noise injection with capacity ladders makes the reversal claim decisive, and the structured-noise mechanism connects to 0001's noise model.
**Major Risks:** Real annotation noise may differ from injected models enough to shift reversal points — 0001's fitted SAM-noise model is the right injection source.
**Unresolved Questions:** Is protection lawful in adapter capacity? Does it hold for the boundary-offset noise that 0257 says low-rank cannot express (a potential tension worth testing)?
**Required Experiments:** Fine-tune across noise-type × noise-level × capacity grids; locate gap reversals; test the structured-noise mechanism via noise-geometry manipulations.
**Reviewer Opinion:** Beautiful interlock with 0001 (noise source), 0257 (what low-rank can't express), and 0248 (what it protects). Together they form a real theory of constrained adaptation.

### IDEA-B-0279 — Label-free PEFT: distilling prompt-ensemble consensus into adapters
**One-line:** Prompt-perturbation agreement — a correctness signal unique to promptable models — as the distillation target for zero-label domain adaptation.
**Survival Reason:** The consistency anchor is structurally harder to game than entropy, addressing TTA's collapse problem at its root. If the collapse-rate claim holds, this is applied at essentially every promptable-model deployment. Anchors 0044 and 0317.
**Major Risks:** Consensus may be systematically wrong (all prompts sharing one shifted bias), capping reliability; consistency computation multiplies adaptation-time inference cost.
**Unresolved Questions:** On which shift types does consensus stay honest (connects to 0072's style fraction)? How does it compare to 0057's statistic matching in gains-per-FLOP?
**Required Experiments:** Distill consensus into adapters across 6 shifted domains; compare against supervised PEFT, TENT-style TTA, and self-training on gain and collapse-rate metrics.
**Reviewer Opinion:** The strongest label-free adaptation bet in the batch because its supervision signal is architecturally native. The collapse-rate metric — not peak gain — is the right headline.

---

## Cluster 9 — Surprising Empirical Phenomena (9 survivors)

### IDEA-B-0282 — Non-monotonic interactive refinement: when more clicks make masks worse
**One-line:** Correction clicks can degrade masks via decoder mode competition — measurable regression rates, attributable mechanism, and a stabilized-decoding fix. `[CI·CF]`
**Survival Reason:** Breaks the monotone-improvement contract that click-efficiency metrics and user trust are built on. Measurable at scale on frozen models, with candidate-trajectory logging pinning the mechanism. Absorbs 0153's saturation thread.
**Major Risks:** Regression rates may depend heavily on correction-simulation policy — human-log validation is required before headline claims.
**Unresolved Questions:** What fraction of regressions are mode switches vs noise? Does mode-stabilized decoding harm legitimate ambiguity resolution?
**Required Experiments:** Simulated and logged-human correction sequences at scale; measure regression rates and conditions; log candidate trajectories; prototype stabilized decoding.
**Reviewer Opinion:** The most immediately felt phenomenon in the cluster — every SAM user has seen it. Quantifying and fixing it is both good science and good citation economics.

### IDEA-B-0285 — Compression that helps: does JPEG act as a matched filter for smoke?
**One-line:** Mild compression may *improve* amorphous-target segmentation by deleting high-frequency clutter — non-monotonic quality curves with a spectral mechanism. `[CI·CF]`
**Survival Reason:** Beneficial degradation inverts preprocessing dogma and falsifies the robustness literature's monotone-degradation assumption for a target class. Frozen-model sweeps make the kill test nearly free; the spectral-separation predictor gives it a mechanism.
**Major Risks:** The effect may be dataset-specific (particular clutter types) rather than a general spectral phenomenon — multi-dataset replication is mandatory.
**Unresolved Questions:** Does the designed band-suppression filter dominate JPEG as the mechanism predicts? Does the optimum shift with target class as spectral separation predicts?
**Required Experiments:** Sweep compression strength across smoke and solid-object tasks; test non-monotonicity; compute spectral-separation predictors; compare against designed band filters.
**Reviewer Opinion:** The index's surprise pick, and it earns the slot: cheap, counter-intuitive, mechanistic. Also quietly important for robustness benchmarking norms (monotonicity is assumed everywhere).

### IDEA-B-0288 — Bigger models, smaller structures: an inverse scaling pocket for dense prediction?
**One-line:** Size-stratified evaluation may reveal a crossing where smaller variants beat larger ones on tiny structures — capacity reallocated to global coherence. `[CI·DM]`
**Survival Reason:** A verified crossing overturns scale-is-all procurement exactly for small-structure-critical deployments (early detection, lesions). Size-stratified ladders on public checkpoints are cheap; the attention-integration mechanism is probeable. Absorbs 0090.
**Major Risks:** Scale ladders confound capacity with training-data and recipe differences within some families — family selection is the design's weak point.
**Unresolved Questions:** Does the crossing replicate across model families? Is the mechanism attention override of weak local evidence, as hypothesized (connects to 0129's regime split)?
**Required Experiments:** Evaluate model-scale ladders on size-stratified suites across domains; test for crossings; run attention-rollout analyses on small-target failures.
**Reviewer Opinion:** "Inverse scaling" framing guarantees attention; the size-stratified evaluation discipline it introduces matters even if the crossing is family-specific.

### IDEA-B-0294 — Bimodal test losses: detecting pretraining contamination from loss distributions alone
**One-line:** Difficulty-adjusted loss residuals may be bimodal on contaminated benchmarks — a corpus-free contamination detector with per-image probabilities. `[HRHR — protected]`
**Survival Reason:** Contamination auditing currently requires corpus access nobody has; a behavioral detector would be applied to every existing benchmark and model. Web-duplicate validation gives it an external anchor. Absorbs 0086.
**Major Risks:** The difficulty regression may be too weak to separate modes, blurring memorization into natural easiness — the method lives or dies on this.
**Unresolved Questions:** How much of the mode separation survives across model families? Do contamination weights materially change any published benchmark conclusion?
**Required Experiments:** Fit difficulty models and residual mixtures across benchmarks and model families; validate mode membership against web-duplicate retrieval; re-evaluate benchmarks with contamination weights.
**Reviewer Opinion:** Protected HRHR: high failure probability, but success creates an instrument the whole field needs and cannot currently buy. Budget it as a bounded exploratory probe with a pre-registered kill criterion.

### IDEA-B-0304 — Style leaks through skips: do skip connections undermine cross-domain robustness?
**One-line:** Skips may pipe domain-specific low-level statistics straight into predictions, bypassing the invariance of the deep pathway — probeable, ablatable, and fixable with normalized skips. `[CI·DM]`
**Survival Reason:** Indicts the most standard dense-architecture component with a three-step causal design (pathway probing, ablation/swap, normalized-skip rescue). A robustness-preserving redesign would touch every U-Net descendant.
**Major Risks:** Skip value varies with decoder design — findings need replication across architecture families to avoid a "your U-Net only" verdict.
**Unresolved Questions:** Does skip normalization preserve the boundary precision skips exist for (interacts with 0257's boundary tax)? Is leakage predictable from 0072's style fraction?
**Required Experiments:** Probe domain decodability per pathway; run skip-ablation/normalization variants across cross-domain benchmarks; decompose robustness and sharpness effects.
**Reviewer Opinion:** Architecture-dogma audits rarely come with this clean an intervention set. High disagreement potential — which is exactly why it should be done carefully and first by us.

### IDEA-B-0305 — Periodic performance in input size: aliasing between resolution and patch grid
**One-line:** Segmentation quality may oscillate with input resolution at patch-size harmonics — a systematic artifact contaminating every resolution choice and cross-paper comparison, removable by anti-aliased resizing. `[CI·CF]`
**Survival Reason:** A free correction to a field-wide measurement artifact; 2–4 px resolution sweeps on frozen models settle it, and the fix is a preprocessing change. Anchors 0056, 0125, and 0299's threads.
**Major Risks:** Oscillation amplitude may be small relative to noise except for thin-structure strata — stratified analysis is mandatory, not optional.
**Unresolved Questions:** Does periodicity replicate across ViT families and patch sizes? How much published cross-resolution comparison noise does it explain?
**Required Experiments:** Dense resolution sweeps (2–4 px steps) with spectral periodicity tests; stratify by structure thinness; validate anti-aliasing fixes.
**Reviewer Opinion:** With 0122, forms the token-lattice artifact pair. Cheap, definitive, and the kind of finding that quietly improves everyone's numbers once known.

### IDEA-B-0306 — Less rank, more accuracy: the low-rank advantage on tiny datasets
**One-line:** Rank-1–2 LoRA may beat rank-8–16 below ~20 samples; optimal rank may scale with data size — a validated selection rule for the modal medical regime. `[CI·CF]`
**Survival Reason:** Rank defaults are data-size-agnostic while tiny-n fine-tuning is the most common real scenario; a rank-vs-n rule upgrades thousands of projects nearly for free. The chosen representative of the rank-law thread (0246, 0271, 0255 killed around it).
**Major Risks:** The interaction may be confounded by learning-rate coupling with rank — joint tuning per grid cell is the honest (and expensive) design.
**Unresolved Questions:** Is the optimum surface logarithmic as hypothesized? Does shift magnitude enter the rule as a second axis (connects to 0246's spectral predictor)?
**Required Experiments:** Grid rank × sample count across 6 tasks with exhaustive per-cell tuning; map the optimum surface; fit and prospectively validate the selection rule.
**Reviewer Opinion:** The most practitioner-facing survivor in the cluster. Insist on the per-cell tuning; without it the counter-intuitive claim will (rightly) be attributed to under-tuned baselines.

### IDEA-B-0310 — Confidence inversion: why soft-label training can produce harder predictions
**One-line:** Standard losses turn soft labels into confident mean prediction — softness in, sharpness out — misleading every consumer reading confidence as uncertainty. `[CI]`
**Survival Reason:** Corrects a widespread misunderstanding about what soft supervision achieves, with a loss-structure account testable by comparing mean-regression vs distribution-matching objectives on identical labels. Anchors 0008, 0025, 0099, and 0296.
**Major Risks:** Multiple soft-label semantics (ambiguity vs partial coverage) may require separate treatments, complicating one clean story.
**Unresolved Questions:** Which deployed pipelines (matting, multi-rater fusion) exhibit the inversion in the wild? Does distribution matching fix it without accuracy cost?
**Required Experiments:** Train on identical soft labels under mean-regression vs distribution-matching objectives; compare output confidence against rater-disagreement ground truth; verify the mechanism.
**Reviewer Opinion:** A quiet paradox with broad consequences for uncertainty consumers. The mechanism experiment is cheap; the survey of affected pipelines is the impact multiplier.

### IDEA-B-0315 — Five percent of elsewhere: out-of-domain data as a superior regularizer
**One-line:** A small anchor fraction of unrelated data may dominate optimally tuned weight decay/dropout for small-data fine-tuning, via gradient-subspace anchoring. `[CI]`
**Survival Reason:** A simple, turnkey, mechanism-backed regularizer for the modal fine-tuning scenario, with a dominance claim that is cheap to falsify against exhaustively tuned conventional baselines. Anchors 0080.
**Major Risks:** Anchor-source choice may matter enough to complicate the turnkey claim; "exhaustively tuned" baselines are expensive to make credible.
**Unresolved Questions:** Is the optimal anchor fraction lawful in target size as hypothesized? Does the subspace-anchoring mechanism survive verification (update-subspace analysis)?
**Required Experiments:** Compare anchor mixing against tuned conventional regularizers across target sizes and domains; verify the subspace mechanism; fit the anchor-fraction schedule.
**Reviewer Opinion:** Connects to 0248/0260's retention geometry — anchor data may be doing explicitly what low rank does implicitly. Worth testing that link directly in Stage 3.

---

## Cluster 10 — Genuinely Motivated Combinations (3 survivors)

### IDEA-B-0318 — Differentiable scattering: a physics head for volumetric smoke from single images
**One-line:** A differentiable single-scattering renderer in the loop lets ordinary 2D smoke masks supervise a 3D density field — physical quantification from existing labels. `[HRHR — protected]`
**Survival Reason:** Resolves the dimensional mismatch (2D labels, 3D medium) that pure segmentation cannot, and its validation (paired-view consistency, transmissometer correlation) is independent of the training labels. Either grounds smoke quantification physically or maps the limits of single-view inversion.
**Major Risks:** Single-scattering may be too crude for dense smoke; the inverse problem may be under-constrained from single views — both are honest failure modes worth documenting.
**Unresolved Questions:** How much does multi-view or temporal consistency constrain the inversion? Can density outputs be validated at deployment scale without instruments?
**Required Experiments:** Implement the differentiable scattering head; train on standard smoke datasets; validate density via paired-view consistency and available physical measurements.
**Reviewer Opinion:** Protected HRHR — the one physics-first bet kept from Cluster 10. Its binary-mask parity requirement (hypothesis a) is the cheap early kill test; run it before investing in physical validation.

### IDEA-B-0320 — Positive-unlabeled statistics for everything-mode auto-labeling
**One-line:** Everything-mode output is PU data (found = positive, unfound = unknown); PU-corrected training with audited stratum priors repairs the closed-world error.
**Survival Reason:** Repairs a foundational statistical flaw in the field's dominant auto-labeling pattern using the theory built for exactly this data shape. The tiny-audit prior estimation keeps it nearly free. Anchors 0007 and 0034.
**Major Risks:** PU corrections are sensitive to prior misestimation, and stratified priors multiply the estimation burden — audit-budget sensitivity analysis is essential.
**Unresolved Questions:** How fine must strata be before prior estimation noise cancels the correction's gains? Does the recall recovery concentrate on low-contrast/small strata as predicted?
**Required Experiments:** Auto-label with everything mode on datasets with held-out truth; train naive vs PU-corrected students; measure stratified recall recovery vs audit budget.
**Reviewer Opinion:** The most theoretically grounded fix in the batch — the rare case where the right statistics were sitting unused next to a mass practice. Coordinates with 0191 (loop dynamics) and 0329 (student ceilings).

### IDEA-B-0329 — Weak-to-strong generalization in dense prediction: does the student surpass the labeler?
**One-line:** Strong students on weak-teacher labels: surpass on variance-type errors, imitate bias-type errors — a decomposition that predicts when auto-labeling lifts vs caps quality. `[HRHR·DM — protected]`
**Survival Reason:** Determines the ceiling of the field's dominant dataset-construction strategy, and the dense instantiation of weak-to-strong is genuinely open. The bias/variance decomposition plus bias-breaking perturbations make it mechanistic and actionable.
**Major Risks:** Results may depend strongly on student pretraining overlap with evaluation domains — pretraining-controlled replications are needed.
**Unresolved Questions:** Do bias-breaking label perturbations unlock surpassing as predicted? How does the decomposition interact with 0191's generational amplification?
**Required Experiments:** Fine-tune strong models on weak-model labels across teacher-quality ladders with held-out truth; decompose student-vs-teacher deltas by error type; test bias-breaking interventions.
**Reviewer Opinion:** Protected HRHR·DM — the alignment-era question landed in dense prediction exactly when the field's data economics depend on the answer. With 0191 and 0320, forms the auto-labeling science program.

---

## Cluster 11 — SR / Restoration / Generation / Diffusion / LLM Agents (3 survivors)

### IDEA-B-0331 — The hallucination-utility frontier of super-resolution for downstream dense prediction
**One-line:** Map downstream segmentation quality vs SR generative strength (non-monotonic, task-type-dependent), plus a seed-ensemble hallucination detector needing no ground truth. `[DM]`
**Survival Reason:** Generative SR is entering medical and monitoring pipelines on visual-quality evidence; this supplies the boundary-fidelity evidence and a deployable audit before the practice embeds silently. Subsumes 0295 and 0333's territory.
**Major Risks:** Generative-strength knobs differ across SR architectures, complicating a unified frontier — per-architecture frontiers with a shared protocol may be the honest deliverable.
**Unresolved Questions:** Does seed-ensemble variance reliably flag fabricated boundaries across SR families? Where does the texture-task vs boundary-task optimum split fall?
**Required Experiments:** Sweep SR generative strength; measure downstream segmentation across task types; validate the seed-ensemble detector against known fabrications.
**Reviewer Opinion:** The safety-audit framing (detector included) is what elevates this above a benchmark paper. Medical imaging venues will care; so will regulators eventually.

### IDEA-B-0337 — Are diffusion mask priors valid posteriors? Testing generative uncertainty against ground truth ensembles
**One-line:** Coverage-test mask-diffusion sample spread against held-out rater distributions: diversity is not calibration, and the predicted failure structure is specific. `[CF·DM]`
**Survival Reason:** Generative uncertainty is being consumed as if calibrated in medical prototypes; rater-population reference distributions are the right instrument to settle its statistical status. Anchors the killed 0092/0099 conformal-validity thread alongside 0120.
**Major Risks:** Multi-rater datasets rich enough for distributional validation are scarce — the same bottleneck 0099 died of; here the evaluation-only design keeps it feasible on what exists.
**Unresolved Questions:** Are the failure modes as predicted (over-dispersed on easy regions, under-dispersed on genuine ambiguity)? Does calibration fine-tuning against rater distributions generalize across datasets?
**Required Experiments:** Train mask-diffusion on multi-rater datasets with held-out raters; run coverage and dispersion tests; test posterior-calibration fine-tuning.
**Reviewer Opinion:** With 0120, completes the "is free/generative uncertainty statistically real" pair. The rater-holdout design is the methodological contribution that outlives any specific model.

### IDEA-B-0338 — Noise as signal: does restoration destroy the forensic cues tiny-target detection relies on?
**One-line:** At the resolution limit, how a faint structure perturbs the sensor-noise field may be a real detection cue — and denoising deletes it, with a predictable size crossover. `[CI]`
**Survival Reason:** If restoration deletes the earliest detectable signal, uniform preprocessing practice is harming exactly the systems built for early detection (wildfire, screening). Matched-training controls (train on raw vs denoised respectively) make the comparison decisive. Anchors 0243.
**Major Risks:** The noise-interaction cue may be sensor-specific, limiting generality across cameras and scanners — multi-sensor replication decides whether it is a law or a quirk.
**Unresolved Questions:** Is the crossover predictable from target contrast-to-noise ratio as hypothesized? Does the cue survive compression (interacts with 0285's spectral account)?
**Required Experiments:** Train detectors on raw vs denoised inputs across target-size ladders with matched pipelines; locate the crossover; verify the mechanism via noise-resampling controls.
**Reviewer Opinion:** The sharpest deployment-relevant claim in Cluster 11: "image quality is target-relative" stated at the regime where it costs lives to get wrong. With 0285 and 0331, defines the preprocessing-skepticism thread.

---

## Survivor count: 75

By cluster: C1 8 · C2 8 · C3 9 · C4 7 · C5 7 · C6 6 · C7 6 · C8 9 · C9 9 · C10 3 · C11 3.
Protected HRHR (10): 0009, 0019, 0075, 0078, 0159, 0162, 0185, 0294, 0318, 0329.
