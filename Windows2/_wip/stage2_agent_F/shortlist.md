# Windows2 Stage-2 Agent F — Shortlist (Batch A)

Reviewer: Cloud Sub-Agent F (Independent Reviewer + Novelty Assassin). Scope: batch A only (W2-A-0001..0352).

**75 keeps** out of 352 (51 killed, 226 borderline). Selection was NOT by score average: high-risk/high-reward, simple counter-intuitive, cheap-to-falsify, and disagreement-prone ideas were protected explicitly. Tier membership reflects my confidence that the idea is (a) a real scientific question, (b) not already published, and (c) worth a PhD-student-year — in that priority order.

Ideas attacked in `prior_work_attack.md` were web-searched; verdicts there override first-pass optimism. One idea (W2-A-0017) was demoted from this shortlist after its attack found a direct prior-work hit (see 'Post-attack demotion' below).

## Tier A — Highest conviction (17)

The strongest combination of novelty, significance, upside and ROI in the batch. Most are measurement/forensics designs whose value survives either experimental outcome.

- **W2-A-0074** (C03) — Volume measurements inherit uncalibrated uncertainty from segmentation: are downstream tumor-volume confidence intervals valid even when masks look good?
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk2 Feas4 | Flags: `clinical-safety,cheap-falsify`
  - Why kept: Anti-conservative volume CIs from boundary-correlated errors is a precise, checkable, clinically consequential claim with a constructive fix; synthetic-lesion anchor kills the GT-uncertainty objection. Top-3 in batch A.

- **W2-A-0121** (C05) — Puddles are mirrors on the road: wet-surface reflections are systematically mislabeled and cause phantom-object segmentation in driving scenes.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `forensic,clinical-safety-analog,signed-bias`
  - Why kept: Geometrically-verified phantom objects in puddles is a hidden, safety-relevant, metric-invisible error class with a built-in verification method (mirror symmetry about the road plane); best forensic idea in C05.

- **W2-A-0148** (C06) — Human-AI teaming for camouflage search: model proposals + human verification exceeds either alone, but only if model uncertainty is exposed.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas3 | Flags: `counter-intuitive,human-study`
  - Why kept: Lit-attacked: soft-vs-hard highlighting literature (NSF visual-search studies) already shows soft/graded confidence beats hard binary highlights and hard highlighting can mask non-highlighted targets. Surviving mutation: camouflage/COD-specific teaming with calibration quality as moderator and segmentation-mask anchoring mechanism. MUTATE but keep.

- **W2-A-0150** (C06) — Ambiguous boundaries drift with image resolution: the same object gets objectively different 'correct' boundaries at different scales - boundary GT is scale-relative.
  - Scores: N5 S5 U5 ROI5 Unpub5 Risk3 Feas4 | Flags: `disagreement-prone,annotation-theory,counter-intuitive`
  - Why kept: Scale-relativity of boundary ground truth attacks an unexamined axiom (that a single correct boundary exists independent of viewing scale); if the systematic shift is real, mixed-resolution training is provably mis-specified. Interface controls are essential.

- **W2-A-0163** (C07) — Stuff-stuff boundaries are measure-zero fictions: grass-to-sidewalk transitions are physically bands, and the label model should say so.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk2 Feas4 | Flags: `metric-audit,disagreement-prone,annotation-theory`
  - Why kept: 'Stuff-stuff boundaries are measure-zero fictions' is a sharp ontological claim with a cheap multi-annotator test and a concrete evaluation reform (band-aware scoring); the band-vs-edge classifier is the honest prerequisite.

- **W2-A-0175** (C07) — Photograph printed calibration shapes to get camera-true boundary ground truth with exact sub-pixel geometry - the first zero-annotation boundary benchmark.
  - Scores: N5 S5 U5 ROI5 Unpub5 Risk2 Feas4 | Flags: `metrology,new-instrument`
  - Why kept: Physical ground truth below annotation noise opens a measurement regime segmentation has never had; ecological-validity complaint is anticipated and answered by textured/embedded variants. Flagship-quality idea.

- **W2-A-0199** (C08) — Rare-context hallucination: models paint plausible-but-absent stuff classes (water under bridges, sky through gaps) driven by context priors overpowering evidence.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `counter-intuitive,curation-heavy`
  - Why kept: Context-completion hallucination with association-strength dose-response is the segmentation analogue of LLM hallucination, quantified; dry-canal/drained-pool curation is tedious but entirely doable.

- **W2-A-0205** (C09) — Verification bias: annotators accept wrong-but-plausible machine masks at high rates, and the accepted errors are systematically correlated with model style.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `ecosystem-inbreeding,human-study`
  - Why kept: Correlated (not independent) contamination from verify-workflows breaks the noise assumptions of the entire label-noise literature; the train-on-verified inheritance leg makes it causal. Core of the inbreeding thesis with 0206.

- **W2-A-0206** (C09) — Detect the SAM fingerprint: datasets annotated with SAM assistance carry identifiable boundary-style signatures that future models inbreed on.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `ecosystem-inbreeding,forensic`
  - Why kept: SAM-fingerprint detection plus inheritance measurement is the flagship of the data-genetics agenda: forensic, timely, and consequential for every dataset built since 2023. Mixed-provenance blurring is the technical fight. Lit-attacked below.

- **W2-A-0237** (C10) — Annotation-convention shift masquerades as domain shift: cross-country dataset gaps are partly label-sociology gaps.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `disagreement-prone,metric-audit`
  - Why kept: 'Adaptation methods get credit for learning label conventions' is a devastating possibility testable with 300 re-annotations; if the >25% figure holds for even one canonical pair, every UDA table needs a footnote.

- **W2-A-0249** (C10) — Part of every 'domain gap' is an annotation-quality gap: target-domain labels are often worse, inflating measured shift.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: Reference-quality asymmetry inflating measured domain gaps, with a no-reannotation diagnostic, converts a suspicion into an instrument; survey-then-reannotate protocol (own note) is exactly the right design.

- **W2-A-0300** (C12) — If all strong models converge, ensembles die: test whether dense-model ensemble gains are collapsing generation by generation.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `monoculture,metric-audit`
  - Why kept: The convergence tax on ensembles, measured longitudinally by cohort era, quantifies a reliability-engineering consequence of ecosystem monoculture nobody has priced; era-vs-scale confounding is handled by scale-matched cohorts.

- **W2-A-0326** (C14) — 'More context always helps' is false for boundaries: context-size sweeps show boundary precision peaks at small context and degrades with more.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas5 | Flags: `counter-intuitive,cheap-falsify`
  - Why kept: Signed, property-resolved context-value curves attack a monotonicity assumption baked into a decade of architecture design; the retrained-variant arm answers the off-manifold objection. A week of compute, decade of consequences. Lit-attacked below.

- **W2-A-0331** (C14) — Dice's gradient pathology on multi-instance images: the loss concentrates learning on the largest lesion and starves the rest - diagnose, don't re-loss.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk2 Feas4 | Flags: `mechanistic,clinical-safety`
  - Why kept: Direct gradient-flow instrumentation of Dice's per-instance starvation, with a data-side fix validating the mechanism, is instrument-level science on a loss the entire medical field uses; 2D-first scoping keeps it tractable. Top-5 in batch A.

- **W2-A-0334** (C14) — Class-agnostic masks leak semantics: mask shape alone predicts object category - with privacy and 'semantic-free' claim consequences.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `counter-intuitive,privacy,cheap-falsify`
  - Why kept: Shape-only semantic leakage with a privacy demonstration (scene/activity recovery from 'anonymized' masks) lands in both science and policy; cheap, decisive, and nobody has quantified it at scale.

- **W2-A-0349** (C14) — Human boundary conventions encode function, not photometry: models place boundaries where image evidence says, humans where object USE says - measure the systematic divergence.
  - Scores: N5 S5 U5 ROI5 Unpub5 Risk3 Feas4 | Flags: `disagreement-prone,annotation-theory,counter-intuitive`
  - Why kept: 'Part of boundary error is an unresolved disagreement about what boundaries MEAN' (functional vs photometric) reframes evaluation itself; the signed per-junction-type offset is measurable and the affordance grounding disciplines the taxonomy. Among the deepest ideas in the batch.

- **W2-A-0352** (C14) — Segmentation-free measurement: for many 'segmentation' applications (area, count, growth-rate), direct regression from images beats segment-then-measure - test when the mask is an unnecessary middleman.
  - Scores: N5 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `counter-intuitive,reformulation`
  - Why kept: 'When is the mask an unnecessary middleman' deflates segmentation's assumed universality with a matched-budget three-task test and an auditability-aware decision rule; the honest framing of regression's auditability loss preempts the obvious rebuttal.

## Tier B — High conviction (31)

- **W2-A-0058** (C03) — Tumor boundary uncertainty is directionally structured (infiltration axes); isotropic uncertainty models are wrong in a measurable way.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk4 Feas2 | Flags: `high-risk-high-reward,clinical-safety`
  - Why kept: Directional uncertainty vs isotropic models, anchored to radiotherapy margins, is a genuinely new axis; data scarcity (multi-rater glioma + orientation fields) is the tax. Protect as HRHR.

- **W2-A-0061** (C03) — Vessel and airway models optimize Dice but break topology: measure the Dice-topology Pareto frontier and show current models sit at its wrong end.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `cheap-falsify,counter-intuitive`
  - Why kept: 'Topology is lost at checkpoint-selection time, not training time' is a sharp, cheap, actionable reframing of the clDice line; every checkpoint is already logged in a normal run. Best of C03.

- **W2-A-0071** (C03) — Benchmarks reporting Dice above the inter-rater ceiling are fitting annotator style: audit which medical leaderboards have crossed their own noise floor.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk3 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: 'Which leaderboards have crossed their own noise floor' is a field-level service with teeth; the style-vs-anatomy error decomposition is what elevates it above known single-dataset inter-rater studies.

- **W2-A-0075** (C03) — Consensus fusion (STAPLE-style) systematically erases minority-expert detections that are disproportionately correct on rare pathologies.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk4 Feas2 | Flags: `high-risk-high-reward,disagreement-prone,clinical-safety`
  - Why kept: Outcome-anchored test of consensus erasing the correct minority expert is the most ethically loaded finding available in this cluster; data access is the wall. Protect as HRHR. Lit-attacked below.

- **W2-A-0076** (C04) — Smoke has no true binary boundary: model rankings on smoke benchmarks flip when evaluated against density (alpha) labels instead of binary masks.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk2 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: 'Benchmarks measure style, not smoke' with a ranking-flip demonstration is a field-resetting audit; smoke-density/matting lines exist so the agreement-study leg must carry novelty. Lit-attacked below.

- **W2-A-0100** (C04) — Deduplicate smoke/fire benchmarks by video provenance: same-event frames in train and test inflate scores, and rankings change after cleanup.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk2 Feas5 | Flags: `cheap-falsify,contamination,metric-audit`
  - Why kept: Provenance-level leakage audit of smoke/fire benchmarks is cheap, decisive, and likely devastating; the genre exists in other domains, which helps rather than hurts the method's credibility.

- **W2-A-0145** (C06) — Findability bias: COD datasets contain only camouflage that FAILED (someone photographed it) - true camouflage performance is unbounded above benchmarks.
  - Scores: N5 S5 U5 ROI4 Unpub5 Risk4 Feas2 | Flags: `high-risk-high-reward,selection-bias`
  - Why kept: Datasets contain only failed camouflage - a selection-bias claim that bounds the unmeasurable, testable via telemetry-verified presence. Ecology collaboration is the wall; upside is a permanent asterisk on every COD number. Lit-attacked below.

- **W2-A-0151** (C07) — Three-way boundary error decomposition: how much reported boundary error is model, annotation, or metric artifact?
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk2 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: Per-benchmark boundary error budgets (model vs annotation vs metric) would recalibrate every sub-3px progress claim; sampling design from 200 objects to benchmark-wide claims is the statistical crux. Lit-attacked below.

- **W2-A-0152** (C07) — Size-stratified reporting flips leaderboards: mIoU improvements of recent methods concentrate entirely in large objects.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk2 Feas5 | Flags: `cheap-falsify,metric-audit`
  - Why kept: Inference-only longitudinal audit with a devastating potential headline ('five years of progress never reached the smallest decile'); reproduction of official numbers is the only gate.

- **W2-A-0164** (C07) — Below the annotation noise floor: SOTA claims on tiny-object benchmarks assert precision the labels cannot support.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas4 | Flags: `metric-audit,cheap-falsify,statistics`
  - Why kept: Minimum-evaluable-object-size per dataset, derived by propagating measured annotation jitter, is a permanent public good; 'statistically vacuous SOTA claims' is the kind of finding that survives every rebuttal.

- **W2-A-0183** (C08) — Anomaly-segmentation benchmarks are boundary detectors in disguise: SOTA methods flag object-background transitions, not anomalies.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `cheap-falsify,metric-audit`
  - Why kept: Boundary-band-excluded re-scoring of anomaly leaderboards is an afternoon of compute that could collapse a subfield's rankings; the both-views reporting requirement keeps it fair.

- **W2-A-0188** (C08) — Do uncertainty overlays help or hypnotize? Measure over-reliance dynamics when clinicians see model confidence maps.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk3 Feas3 | Flags: `human-study,clinical-safety,counter-intuitive`
  - Why kept: 'Uncertainty overlays can NET-INCREASE misses when calibration is poor' is a deployment-gating claim for the entire uncertainty-visualization agenda; automation bias is known in human factors but unmeasured here. Protect.

- **W2-A-0195** (C08) — Sub-10-example classes are retrieval, not generalization: feature-space nearest-neighbor tests reveal the memorization regime of the extreme tail.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `cheap-falsify,counter-intuitive`
  - Why kept: 'Benchmark tails measure dataset redundancy, not capability' is a cheap, decisive, uncomfortable audit; embedding-choice replication is the only methodological demand. High kill-power over long-tail SOTA claims.

- **W2-A-0215** (C09) — Annotation protocol is a stronger treatment than architecture: same images labeled boundary-first vs region-first produce measurably different trained models.
  - Scores: N5 S5 U5 ROI4 Unpub5 Risk3 Feas3 | Flags: `disagreement-prone,high-risk-high-reward,annotation-theory`
  - Why kept: 'Protocol choice dominates the median architecture improvement' is the most subversive testable claim in C09; commissioning the dual-protocol corpus is expensive but the comparison design is airtight. Protect.

- **W2-A-0264** (C11) — SAM-generated panoptic pseudo-labels have a characteristic error anatomy: itemize it before the ecosystem trains a generation of models on it.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `ecosystem-inbreeding,forensic`
  - Why kept: Itemized error anatomy of SAM-pipeline labels, with inheritance measurement, is the constructive companion to 0206's fingerprint forensics; timely before the ecosystem finishes training a generation on such labels.

- **W2-A-0268** (C11) — Do semi-supervised methods still matter under DINOv2-grade features? Systematic re-evaluation of SSL-for-segmentation on top of modern foundations.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk3 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: Foundation-regime re-baselining that could obsolete a subfield's methodology; pre-registration and authors'-code discipline (own note) is what separates a service to the field from a flame war. High leverage per GPU.

- **W2-A-0272** (C11) — Layered source files (PSD/SVG) are the largest untapped mask corpus: design assets contain millions of human-made segmentations nobody trains on.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk3 Feas3 | Flags: `new-data-source`
  - Why kept: Design files as a mask corpus with professional boundary quality and different economics is the most original data idea in the batch; licensing and harvesting engineering are real but characterizable. Lit-attacked below.

- **W2-A-0276** (C12) — Dense-prediction scaling laws diverge from classification: boundary quality scales with a smaller exponent than region accuracy - fit both.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk3 Feas3 | Flags: `law-seeking,counter-intuitive`
  - Why kept: 'Scale buys WHAT, not HOW WELL you trace it' - property-decomposed scaling exponents would redirect boundary research away from scale; the label-noise-floor confound is real and is exactly why it pairs with 0175's physical GT.

- **W2-A-0278** (C12) — Sub-patch information is not lost - it hides in neighboring tokens: measure recoverable sub-tokenization detail across ViT foundations.
  - Scores: N5 S4 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `mechanistic,cheap-falsify`
  - Why kept: 'Foundations contain more sharpness than any decoder extracts' is a precise, testable, consequential claim; neighborhood decoding of sub-patch edge position is a clean probe with an obvious constructive sequel.

- **W2-A-0290** (C12) — Shared blind spots across the model zoo: pixels where ALL foundations fail mark data-ecosystem holes, not architecture limits.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `monoculture,decomposition`
  - Why kept: The shared-vs-unique error split (data-ecosystem holes vs architecture limits) is the actionable diagnosis the field needs before spending another year on architectures; lineage-overlap covariate handles the eroding-independence caveat.

- **W2-A-0297** (C12) — Object tokens or distributed objectness? Causal feature-surgery to locate WHERE promptable models represent each object.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk4 Feas4 | Flags: `mechanistic,high-risk-high-reward`
  - Why kept: Causal feature surgery (swap/ablate object subspaces, measure mask transfer) brings mechanistic-interpretability rigor to promptable vision, with the object-subspace rank as a capacity prediction; off-manifold intervention artifacts are the known trap.

- **W2-A-0301** (C13) — Did SA-1B swallow the test sets? Measure foundation-training contamination of segmentation benchmarks with near-duplicate forensics.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk3 Feas4 | Flags: `contamination`
  - Why kept: SA-1B/LAION-vs-test-set contamination forensics with memorization-signal stratification; NLP contamination studies provide the template, dense prediction lacks the audit. Closed-corpus bounds honesty (own note) is right. Lit-attacked below.

- **W2-A-0305** (C13) — Effective headroom estimation: how much of each benchmark's remaining error is model-fixable versus reference noise - the saturation audit.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk3 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: A published per-benchmark headroom table (model-fixable vs reference noise) would redirect where the field reports results - it even makes a testable sociological prediction; assumption-dependence is handled by reporting ranges.

- **W2-A-0313** (C13) — Statistical power audit of segmentation SOTA claims: how many published gains survive bootstrap significance testing on their own benchmarks?
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk2 Feas4 | Flags: `metric-audit,statistics,cheap-falsify`
  - Why kept: The metric-learning-reality-check playbook applied to segmentation SOTA claims; released-checkpoint restriction keeps it feasible, and the >30% within-noise prediction is concrete enough to be falsified. Norms-changing potential.

- **W2-A-0321** (C13) — LVIS federated annotation makes rare-class scores statistically fragile: put confidence intervals on every rare-class claim.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `statistics,cheap-falsify,metric-audit`
  - Why kept: 'Rare-class science runs below its own noise floor' - bootstrap CIs on LVIS rare classes plus the unverified-negative bias measurement is nearly-free statistics with direct consequences for a large literature. Own risk note ('none serious') is accurate.

- **W2-A-0322** (C13) — Same dataset, different numbers: meta-analysis of score spread for identical model-benchmark pairs across papers reveals the reproduction noise floor.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas5 | Flags: `statistics,cheap-falsify,zero-gpu`
  - Why kept: A reproduction-noise table mined from the literature itself, zero GPUs, immediately usable by every reviewer; citation-provenance tracking (own note) prevents the spread underestimate. The cheapest high-value project in the batch.

- **W2-A-0329** (C14) — How far does per-frame + matching go on video segmentation? Establish the strong frame-independent baseline the VOS literature skips.
  - Scores: N4 S5 U5 ROI5 Unpub3 Risk2 Feas4 | Flags: `cheap-falsify,metric-audit`
  - Why kept: The strong frame-independent baseline the VOS literature skips, over foundation-era features; the gap decomposition (what temporal machinery is actually FOR) is the deliverable. High embarrassment potential, honestly designed with tuned+naive variants.

- **W2-A-0330** (C14) — Do boundary losses actually improve boundaries? Meta-analysis plus controlled reruns of the boundary-loss literature under noise-floor-aware evaluation.
  - Scores: N4 S5 U5 ROI5 Unpub4 Risk2 Feas4 | Flags: `metric-audit,cheap-falsify`
  - Why kept: Rerunning the boundary-loss literature under noise-floor-aware evaluation is the enforcement arm of the C07 metrology agenda; survival tabulation with CIs is the right format and released-code reproduction keeps it fair.

- **W2-A-0339** (C14) — Is 3D really harder than 2D? Per-supervision-bit accounting suggests volumetric segmentation may be intrinsically EASIER than the field believes.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk4 Feas4 | Flags: `counter-intuitive,high-risk-high-reward`
  - Why kept: '3D's difficulty reputation is an accounting artifact' - per-supervision-bit renormalization with the sparse-3D-beats-dense-2D corollary is a field-belief inversion with immediate annotation-budget consequences; fair bit-accounting (own note) is the entire fight. Protect.

- **W2-A-0341** (C14) — Prompt sensitivity may INCREASE with model scale on ambiguous objects: bigger promptable models represent more granularity hypotheses to flip between.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk4 Feas4 | Flags: `counter-intuitive,high-risk-high-reward`
  - Why kept: The sign-splitting scale-ambiguity interaction (scale changes the CHARACTER of instability, not its amount) is the most sophisticated claim in the prompt-sensitivity family; needs the controlled mini-SAM series to be clean. Protect.

- **W2-A-0351** (C14) — The two-annotator myth: pairwise agreement statistics systematically underestimate ambiguity because disagreement is multi-modal, not binary - remeasure with dense rater panels.
  - Scores: N5 S5 U5 ROI4 Unpub4 Risk3 Feas3 | Flags: `disagreement-prone,annotation-theory,high-risk-high-reward`
  - Why kept: Multi-modal (not noisy-binary) disagreement structure invalidating pairwise-agreement certification is foundational annotation theory; a 10-rater panel on 300 items is expensive but small compared to the claim's reach. Protect.

## Tier C — Kept on merit within crowded areas (21)

Very good ideas that sit in more crowded literature neighborhoods or carry heavier execution burdens; kept because the core question is real and unanswered.

- **W2-A-0022** (C01) — The Jacobian of SAM's mask w.r.t. prompt location is a label-free edge/structure detector - characterize what it computes.
  - Scores: N5 S4 U5 ROI4 Unpub4 Risk4 Feas4 | Flags: `high-risk-high-reward,new-readout`
  - Why kept: Differentiation w.r.t. the prompt as a readout channel is the most original mechanism in C01; noise at feasible grid resolution is the real risk and worth paying for.

- **W2-A-0042** (C02) — Micro-motion as a segmentation cue: can temporal aggregation segment objects invisible in any single frame (breathing, vibration)?
  - Scores: N5 S4 U5 ROI4 Unpub4 Risk4 Feas3 | Flags: `high-risk-high-reward,new-task`
  - Why kept: Segmenting what no single frame shows is a real capability gap with a constructive fix (motion amplification); data must be built, which is the price of a new task.

- **W2-A-0082** (C04) — Measure the annotator alpha-threshold distribution: at what transparency do humans stop labeling smoke, and how much benchmark variance does it explain?
  - Scores: N5 S4 U4 ROI5 Unpub5 Risk2 Feas4 | Flags: `measurement-science,disagreement-prone,cheap-falsify`
  - Why kept: Measuring the implicit alpha-cutoff distribution of annotators is original psychophysics with direct dataset-harmonization payoff; controlled alpha ramps make it decisive.

- **W2-A-0091** (C04) — IoU is the wrong loss surface for amorphous regions: measure human-judgment vs IoU ranking disagreement on smoke/fog masks.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk3 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: Human-preference validation of segmentation metrics for amorphous classes could reorder the subfield; per-use-case preference collection (own note) is the difference between a metric paper and an opinion poll.

- **W2-A-0097** (C04) — Heat shimmer (refractive turbulence) as a segmentable phenomenon: detecting invisible hot-air regions from background distortion alone.
  - Scores: N5 S4 U5 ROI4 Unpub4 Risk4 Feas3 | Flags: `high-risk-high-reward,new-task,physics-channel`
  - Why kept: Passive shimmer segmentation as a pre-smoke fire channel is the most original constructive idea in C04; wind/vibration confounds are real but controllable on fixed cameras. Protect as HRHR.

- **W2-A-0107** (C05) — Depth-sensor dropout is free glass supervision: mine LiDAR/ToF invalid-return masks as automatic transparent-surface labels at fleet scale.
  - Scores: N4 S5 U5 ROI4 Unpub3 Risk3 Feas4 | Flags: `free-supervision`
  - Why kept: Sensor-weakness-as-data-engine at fleet scale is the constructive flagship of C05; individual depth-invalidity cues are published, so the scaling claim and filtering recipe must carry it. Lit-attacked below.

- **W2-A-0110** (C05) — Day-night transmission/reflection flip: the same window changes optical class by time of day, and models trained on one phase fail on the other.
  - Scores: N5 S4 U4 ROI5 Unpub5 Risk2 Feas4 | Flags: `counter-intuitive,physics-channel,annotate-once`
  - Why kept: Physics-forced diurnal class flip inside a fixed scene, with annotate-once economics and a control-surface design; among the most elegant experimental setups in the batch.

- **W2-A-0136** (C06) — Train on disagreement maps directly: predicting WHERE annotators disagree transfers across datasets better than predicting masks.
  - Scores: N4 S5 U5 ROI4 Unpub3 Risk3 Feas4 | Flags: `disagreement-prone`
  - Why kept: 'Ambiguity is more domain-invariant than object identity' is a genuinely deep claim with a clean zero-shot test; must control protocol/skill confounds (own note) and dodge the multi-rater modeling literature by staying on the transfer question.

- **W2-A-0143** (C06) — Part-level ambiguity in camouflage: where the animal ends and the mimicked substrate begins is sometimes objectively undecidable - propose decision-theoretic annotation.
  - Scores: N5 S4 U5 ROI4 Unpub5 Risk3 Feas4 | Flags: `disagreement-prone,annotation-theory`
  - Why kept: Testing whether undecidability itself is reliably annotatable is a foundational annotation-theory question disguised as a COD study; the exclusion-mask retraining leg makes it constructive.

- **W2-A-0173** (C07) — Instance merging obeys a crowding law: adjacent-instance merge probability is a universal function of gap-to-size ratio, like human visual crowding.
  - Scores: N5 S4 U4 ROI5 Unpub5 Risk3 Feas4 | Flags: `law-seeking,counter-intuitive`
  - Why kept: A 'machine Bouma law' - dimensionless collapse of instance-merge probability - would be the first universal capability rating for dense scenes; curve collapse either happens or it doesn't, and both outcomes teach.

- **W2-A-0181** (C08) — The abstention cliff: models never predict classes below a training-frequency threshold, and the threshold is predictable from loss geometry.
  - Scores: N4 S5 U5 ROI4 Unpub3 Risk3 Feas4 | Flags: `law-seeking,counter-intuitive`
  - Why kept: Class death as a predictable phase transition (with the no-revival-by-longer-training corollary) is a strong falsifiable law; config-dependence of the cliff is the main threat to universality. Lit-attacked below.

- **W2-A-0198** (C08) — Seed-churn maps: pixels that flip between training runs form a free, model-intrinsic ambiguity atlas that matches human disagreement.
  - Scores: N4 S5 U5 ROI4 Unpub3 Risk3 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: Churn atlases matching human disagreement, plus the audit showing published gains concentrate on high-churn pixels, is a double-barreled result; churn is known in classification so the dense/audit legs carry novelty. Lit-attacked below.

- **W2-A-0225** (C09) — The 100-labeled-pixels challenge: map the extreme-low-budget frontier of segmentation to find where each supervision paradigm collapses.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk2 Feas4 | Flags: `regime-map,counter-intuitive`
  - Why kept: The extreme-budget phase map (paradigm rankings invert; consistency methods collapse below thresholds) directly indicts the field's habit of extrapolating efficiency claims downward; seed-variance demands make it compute-honest but bounded.

- **W2-A-0228** (C10) — Night failure is mostly ISP failure: models degrade on processed JPEGs, not on darkness itself - RAW-domain evaluation separates the two.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk3 Feas3 | Flags: `counter-intuitive,signed-bias`
  - Why kept: 'Night robustness research is partly chasing vendor ISP artifacts' is a sharp attribution claim; RAW night data with GT is the scarce ingredient, and the vendor-varying recovered fraction is the headline figure.

- **W2-A-0245** (C10) — UDA methods overfit their development benchmark pair: rank correlation across novel shift pairs is the reproducibility number nobody reports.
  - Scores: N4 S5 U5 ROI4 Unpub3 Risk2 Feas4 | Flags: `metric-audit,disagreement-prone`
  - Why kept: Cross-pair rank-stability audit of UDA with frozen hyperparameters; the classification reality-check genre exists (Musgrave-style), which strengthens the method and narrows the novelty to segmentation + rank-stability framing. Lit-attacked below.

- **W2-A-0254** (C11) — Does object-centric data cause segmentation emergence in SSL? Train DINO-style models on scene-only crops and watch attention objects disappear (or not).
  - Scores: N4 S5 U5 ROI4 Unpub3 Risk4 Feas3 | Flags: `high-risk-high-reward,causal-design`
  - Why kept: 'Objects for free are inherited from photographic framing, not discovered' is a foundational causal question about SSL; scene-centric SSL studies exist but not the controlled de-object-centrification intervention. Scale ceiling on reruns is the honest risk.

- **W2-A-0292** (C12) — Can a segmentation foundation be trained on zero real images? Push procedural-data pretraining (fractals, formulas, simulations) to its dense-prediction limit.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk4 Feas3 | Flags: `high-risk-high-reward,causal-design`
  - Why kept: Ingredient-ablated procedural pretraining asks what dense pretraining actually needs from data (compositional structure vs semantics); the classification-side procedural line exists, the dense version with occlusion-layering ablations does not. Protect.

- **W2-A-0312** (C13) — Masks reveal their dataset: annotation-style leakage is strong enough to classify a mask's source benchmark from geometry alone.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk3 Feas4 | Flags: `forensic,ecosystem-inbreeding`
  - Why kept: 'Labels are dialects and models learn the dialect' unifies the 0156/0224/0303 forensic threads into the strongest single formulation, with the style-vs-content gap decomposition as the headline; shared-class matched-size controls answer the confound.

- **W2-A-0323** (C13) — Measure human mIoU: segmentation benchmarks lack the human-performance baselines that every claims discussion needs.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk3 Feas3 | Flags: `human-ceiling,disagreement-prone`
  - Why kept: The crossing profile (humans below SOTA on convention-diligence, far above on ambiguity and rare objects) would redefine what 'human-level segmentation' means; effort-curve reporting (own note) is the right format. Long overdue.

- **W2-A-0337** (C14) — Mask metrics don't predict task success: measure the mIoU-to-downstream correlation for grasping, measurement, and navigation consumers.
  - Scores: N4 S5 U5 ROI4 Unpub4 Risk3 Feas4 | Flags: `metric-audit,deployment-relevant`
  - Why kept: Metric-validity against instrumented consumers (grasping, measurement, navigation) is the study that decides whether benchmark rankings mean anything downstream; the small real-robot leg (own note) buys the credibility simulation lacks.

- **W2-A-0345** (C14) — Segmentation models are secret amodal completers: measure how often models segment plausibly-present-but-invisible object parts, and whether it helps or hurts.
  - Scores: N5 S4 U5 ROI4 Unpub4 Risk3 Feas4 | Flags: `counter-intuitive,emergent-capability`
  - Why kept: 'An emergent capability being actively trained away by modal supervision' is a striking, measurable thesis connecting amodal completion to tracking robustness; synthetic-composite scale plus real validation subsets is the right data strategy.

## Protected exceptions (6)

Would not survive on aggregate scores alone; protected under the high-risk/high-reward, counter-intuitive, cheap-to-falsify, or unpublished-likelihood mandates.

- **W2-A-0026** (C02) — Masklet drift rate in SAM2 is predictable from first-frame single-image ambiguity before any tracking happens.
  - Scores: N4 S4 U4 ROI4 Unpub3 Risk3 Feas5 | Flags: `cheap-falsify`
  - Why kept: Static-measurement-predicts-temporal-failure is a clean, useful claim; occlusion-event dominance is the honest failure mode. Lit-attacked below.

- **W2-A-0028** (C02) — Test whether SAM2 tracks appearance or location: teleport experiments separating the two.
  - Scores: N4 S4 U4 ROI5 Unpub4 Risk2 Feas5 | Flags: `cheap-falsify,counter-intuitive`
  - Why kept: Psychology-style teleport probe cleanly dissociates appearance-tracking from location-prior; either outcome is a finding. Among the best of C02.

- **W2-A-0063** (C03) — Annotation fatigue leaves order signatures in public medical datasets: label quality drifts within annotation sessions and is detectable post hoc.
  - Scores: N5 S4 U4 ROI4 Unpub5 Risk3 Feas4 | Flags: `forensic,cheap-falsify`
  - Why kept: Post-hoc fatigue forensics on public datasets is an original, label-free audit; quality-proxy indirectness is the weak joint, patched by small spot re-annotation.

- **W2-A-0085** (C04) — Smoke shadows are systematically mislabeled as smoke in aerial datasets: an audit with atmospheric-geometry verification.
  - Scores: N5 S4 U4 ROI4 Unpub5 Risk3 Feas4 | Flags: `forensic,signed-bias`
  - Why kept: Sun-geometry forensic verification of label errors is a genuinely new audit instrument (labels falsified by celestial mechanics); off-nadir overlap geometry is the technical hurdle.

- **W2-A-0117** (C05) — Caustics as transparent-object shadows: the bright patterns under glassware are a detection cue with known physics that no model uses.
  - Scores: N5 S3 U4 ROI3 Unpub4 Risk4 Feas3 | Flags: `high-risk-high-reward,physics-channel`
  - Why kept: Caustics as transparent-object shadows is the kind of physics-first idea nobody else will try; directional-lighting operating envelope honestly narrows scope. Protect as HRHR.

- **W2-A-0139** (C06) — COD models lack inhibition-of-return: they find one instance and stop, missing conspecific groups - measure multi-instance recall collapse.
  - Scores: N5 S4 U4 ROI4 Unpub5 Risk3 Feas4 | Flags: `counter-intuitive`
  - Why kept: Conditional recall after the first find (inhibition-of-return deficit) is an original behavioral probe borrowed from visual-search psychology; ecology relevance (herds) gives it real stakes.

## Post-attack demotion

- **W2-A-0017** — was Tier C; demoted to BORDERLINE after the adversarial search found Zhang et al., *Quantifying the Limits of Segmentation Foundation Models* (WACV 2026, arXiv:2412.04243), which quantifies wiry/tree-like failure, attributes it to SA-1B shape statistics, and already ran the targeted fine-tuning experiment (it fails — the limitation is architectural). The surviving sliver (formal prompt-output-space expressivity) should be merged into W2-A-0203.

## Protection audit

- High-risk/high-reward kept: 14 — W2-A-0058, W2-A-0075, W2-A-0145, W2-A-0215, W2-A-0297, W2-A-0339, W2-A-0341, W2-A-0351, W2-A-0022, W2-A-0042, W2-A-0097, W2-A-0254, W2-A-0292, W2-A-0117
- Counter-intuitive kept: 21 — W2-A-0148, W2-A-0150, W2-A-0199, W2-A-0326, W2-A-0334, W2-A-0349, W2-A-0352, W2-A-0061, W2-A-0188, W2-A-0195, W2-A-0276, W2-A-0339, W2-A-0341, W2-A-0110, W2-A-0173, W2-A-0181, W2-A-0225, W2-A-0228, W2-A-0345, W2-A-0028, W2-A-0139
- Cheap-to-falsify kept: 19 — W2-A-0074, W2-A-0326, W2-A-0334, W2-A-0061, W2-A-0100, W2-A-0152, W2-A-0164, W2-A-0183, W2-A-0195, W2-A-0278, W2-A-0313, W2-A-0321, W2-A-0322, W2-A-0329, W2-A-0330, W2-A-0082, W2-A-0026, W2-A-0028, W2-A-0063
- Disagreement-prone kept: 20 — W2-A-0150, W2-A-0163, W2-A-0237, W2-A-0249, W2-A-0349, W2-A-0071, W2-A-0075, W2-A-0076, W2-A-0151, W2-A-0215, W2-A-0268, W2-A-0305, W2-A-0351, W2-A-0082, W2-A-0091, W2-A-0136, W2-A-0143, W2-A-0198, W2-A-0245, W2-A-0323

Tier-2 demotions (53 ideas moved KEEP→BORDERLINE purely by shortlist budget, all flagged `tier-2-revivable` in scores.jsonl): W2-A-0003, 0007, 0008, 0010, 0015, 0016, 0018, 0020, 0021, 0025, 0029, 0034, 0036, 0043, 0045, 0046, 0062, 0065, 0068, 0081, 0088, 0090, 0099, 0101, 0106, 0111, 0118, 0126, 0135, 0153, 0155, 0160, 0170, 0178, 0189, 0200, 0203, 0209, 0220, 0226, 0233, 0239, 0252, 0255, 0259, 0266, 0283, 0286, 0309, 0310, 0315, 0343, 0348. Any of these is a legitimate rescue candidate if the PI's other reviewers disagree with my budget line.
