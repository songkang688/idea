# Agent D Shortlist — Batch C keep-set

Independent Stage-2 review, all 345 C ideas scored (see `scores.jsonl`). **Not ranked by score average.** Selection logic: research ROI and upside dominate; explicitly protected classes (high-risk high-reward, simple counter-intuitive, reviewer-disagreement-prone, cheap-to-falsify) were shielded from average-score death. Verdict totals: 107 keep / 58 mutate / 180 kill.

The keep-set is tiered so the PI can take ~80 toward the future 200 without losing the reserve.

## Tier A — Core keep-set (79 ideas)

- **W2-C-0001** — Open-vocab rare-class AP driven by text-prior frequency, not visual grounding  
  roi 5 / upside 4 / risk 2 / novelty 4 — Cheap inference-only falsification with field-level implications for OVD claims.
- **W2-C-0007** — The annotation-noise floor for tiny objects: is sub-16px AP meaningful  
  roi 5 / upside 5 / risk 2 / novelty 4 — Cheap, decisive, undermines an active benchmark stratum.
- **W2-C-0011** — Prompt-engineering variance exceeds architecture deltas in open-vocab detection  
  roi 5 / upside 5 / risk 2 / novelty 4 — Inference-only, directly attacks how OVD papers claim wins.
- **W2-C-0020** — Zero-shot claims and caption leakage: measuring test-class exposure in pretraining  
  roi 5 / upside 5 / risk 3 / novelty 4 — Directly tests the semantics of zero-shot claims; strong venue fit.
- **W2-C-0040** — Episodic variance makes most few-shot detection deltas unreadable  
  roi 5 / upside 4 / risk 1 / novelty 4 — Cheap replication-style audit with high probability of a decisive negative.
- **W2-C-0042** — Deriving the IoU threshold from annotation noise instead of tradition  
  roi 5 / upside 4 / risk 2 / novelty 4 — Turns an arbitrary convention into a measured quantity; cheap and sharp.
- **W2-C-0043** — Dice on small structures is a coin flip: size-stratified segmentation reporting  
  roi 5 / upside 5 / risk 2 / novelty 4 — Decisive medical-eval claim on existing multi-annotator data.
- **W2-C-0046** — Annotation-noise-propagated confidence intervals for COCO AP  
  roi 5 / upside 5 / risk 2 / novelty 3 — Prior work close but the claim-level significance audit remains open; mutated framing required.
- **W2-C-0055** — A fresh i.i.d. test set for COCO: measuring a decade of adaptive overfitting  
  roi 4 / upside 5 / risk 4 / novelty 4 — High-cost high-reward; the single most informative missing artifact in detection evaluation. Protect.
- **W2-C-0057** — Missing annotations punish better detectors: the unlabeled-object tax  
  roi 5 / upside 5 / risk 2 / novelty 3 — Known phenomenon, unknown differential effect on rankings; cheap decisive design.
- **W2-C-0064** — Image-level vs instance-level bootstrap: which CI is right for detection  
  roi 5 / upside 4 / risk 1 / novelty 4 — Foundational statistics piece for every detection significance claim.
- **W2-C-0065** — A survey and re-analysis of significance testing in detection papers  
  roi 5 / upside 5 / risk 2 / novelty 4 — Meta-science with guaranteed signal and field-level consequence.
- **W2-C-0070** — Minimum detectable effect: power analysis tables for popular benchmarks  
  roi 5 / upside 5 / risk 1 / novelty 4 — Zero-risk, field-infrastructure deliverable; merge with 0302.
- **W2-C-0071** — Is SOTA above the human agreement ceiling, and what does that mean  
  roi 5 / upside 5 / risk 2 / novelty 4 — Benchmark-epistemology question with direct evidence design; pairs with 0338.
- **W2-C-0078** — Does benchmark AP predict downstream utility: grasping and safety as ground truth  
  roi 4 / upside 5 / risk 3 / novelty 4 — Utility-saturation curve is the field's missing cost-benefit evidence.
- **W2-C-0115** — Annotation quality vs quantity at fixed budget: the detection labeling exchange rate  
  roi 4 / upside 5 / risk 3 / novelty 4 — Practical decision rule with broad consequence; strong D&B fit.
- **W2-C-0119** — Rank stability under benign transforms predicts AP without labels  
  roi 5 / upside 4 / risk 3 / novelty 4 — High-utility label-free evaluation; classification priors make it plausible but unclaimed for detection.
- **W2-C-0122** — Train-test duplication in detection benchmarks: a contamination census  
  roi 5 / upside 5 / risk 2 / novelty 4 — Unaudited contamination in detection; certain-yield census with per-image causal check.
- **W2-C-0135** — Co-occurrence overrides appearance: keyboard detected beside monitor-shaped blobs  
  roi 5 / upside 4 / risk 2 / novelty 4 — Simple counterintuitive causal probe; protect. Absorbs 0222/0268.
- **W2-C-0136** — Seed variance vs published deltas: how much of the leaderboard is luck  
  roi 5 / upside 5 / risk 2 / novelty 4 — Foundational missing number for the field; survives prior-work attack (classification-only precedents).
- **W2-C-0145** — Vocabulary interference: longer class lists degrade detection of the same classes  
  roi 5 / upside 4 / risk 2 / novelty 4 — Cheap characterization of an OVD scaling law; deployment-relevant.
- **W2-C-0149** — Uncertainty methods do not improve detection decisions at matched cost  
  roi 5 / upside 5 / risk 3 / novelty 4 — High-stakes compute-matched UQ audit, unclaimed for detection.
- **W2-C-0150** — Domain adaptation for detection loses to 50 labeled target images  
  roi 5 / upside 5 / risk 2 / novelty 4 — Cheap kill-shot on a large subfield; high citation value either way.
- **W2-C-0158** — Temperature scaling does not survive NMS: post-processing breaks calibration  
  roi 5 / upside 4 / risk 2 / novelty 3 — Crisp mechanism question, zero compute; survives as the explanatory piece of the calibration-pitfalls story.
- **W2-C-0159** — Active learning for detection fails at realistic batch sizes: a multi-codebase replication  
  roi 5 / upside 5 / risk 2 / novelty 4 — Open replication gap with direct budget consequences; survives attack.
- **W2-C-0178** — Synthetic corruptions do not predict real degradation: a paired-camera study  
  roi 4 / upside 5 / risk 3 / novelty 4 — Falsifies or validates the field's robustness instrument; protect the capture budget.
- **W2-C-0188** — Multi-view consistency as a free robustness audit  
  roi 5 / upside 4 / risk 3 / novelty 4 — Free monitoring signal from existing data; pairs with 0119.
- **W2-C-0190** — Flicker predicts failure: temporal inconsistency as free uncertainty in video  
  roi 5 / upside 4 / risk 2 / novelty 4 — Free uncertainty signal with direct deployment use; cheap.
- **W2-C-0193** — Threshold drift under mild shift: the silent killer of deployed detectors  
  roi 5 / upside 5 / risk 2 / novelty 4 — High-impact deployment phenomenon, cheap and unclaimed.
- **W2-C-0206** — Feature-distance domain metrics do not predict AP drop  
  roi 5 / upside 4 / risk 2 / novelty 4 — Cheap falsification of a standard proxy plus a better one; strong ROI.
- **W2-C-0208** — Label conventions are a domain: quantifying annotation-style shift  
  roi 5 / upside 5 / risk 3 / novelty 4 — Reattribution claim with clean causal design; absorbs 0014/0134.
- **W2-C-0212** — Night is an ISP artifact: disentangling photons from processing  
  roi 5 / upside 4 / risk 3 / novelty 4 — Counterintuitive causal split of a canonical domain gap; cheap given raw data.
- **W2-C-0221** — Do foundation backbones retire detection UDA: a gap-closure audit  
  roi 5 / upside 5 / risk 2 / novelty 4 — Four runs to potentially retire a subfield's baseline practice.
- **W2-C-0226** — Does super-resolution help detection or just fool metrics  
  roi 5 / upside 5 / risk 2 / novelty 3 — Prior work strong but the GT-controlled hallucination accounting is the open, decisive design.
- **W2-C-0231** — Restoration erases small objects: measuring the object-destruction rate  
  roi 5 / upside 4 / risk 2 / novelty 4 — Unclaimed quantification of restoration harm; cheap and vivid.
- **W2-C-0236** — SR as test-time compute: does it ever beat native high-resolution inference  
  roi 5 / upside 4 / risk 2 / novelty 4 — Compute-matched allocation verdict; cheap and decision-relevant.
- **W2-C-0248** — Which way does SR lie: asymmetry of hallucinated additions vs deletions  
  roi 5 / upside 4 / risk 3 / novelty 4 — Cheap, sharp, protected as cheap-to-falsify; strongest of the SR sub-family after 0226.
- **W2-C-0252** — Geographic performance audit with a purpose-built geo-stratified test set  
  roi 4 / upside 5 / risk 3 / novelty 3 — High-significance fairness artifact; D&B-track material despite annotation cost.
- **W2-C-0253** — Class granularity is a hidden progress knob  
  roi 5 / upside 4 / risk 2 / novelty 4 — Protected: cheap-to-falsify re-analysis with leaderboard-level implications.
- **W2-C-0254** — Do LVIS-tuned long-tail methods survive contact with real deployment tails  
  roi 4 / upside 5 / risk 3 / novelty 4 — Field-level debunk potential; the long-tail literature's external validity is untested.
- **W2-C-0255** — Head-class sacrifice accounting: is total utility actually improved by long-tail methods  
  roi 5 / upside 4 / risk 3 / novelty 4 — Protected: reviewer-disagreement-prone utility argument, nearly free to run.
- **W2-C-0256** — Small and rare are confounded: disentangling size from frequency in long-tail claims  
  roi 5 / upside 4 / risk 2 / novelty 4 — Protected: cheap-to-falsify confound audit of an entire method family.
- **W2-C-0258** — Person-detection fairness with proper uncertainty: a benchmark that supports conclusions  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-integrity fairness contribution; either outcome (confirm or refute gaps) is publishable and important.
- **W2-C-0259** — What counts as an object: annotator salience bias in dataset construction  
  roi 5 / upside 5 / risk 2 / novelty 4 — Foundational dataset-construction epistemology at small annotation cost.
- **W2-C-0260** — Benchmark monoculture: does COCO ranking predict ranking anywhere else  
  roi 5 / upside 5 / risk 2 / novelty 4 — Anchor study for the batch; high venue potential at D&B.
- **W2-C-0261** — Which tail is the tail: image, instance, and pixel frequency define different problems  
  roi 5 / upside 4 / risk 2 / novelty 4 — Protected: cheap-to-falsify definitional audit with method-family implications.
- **W2-C-0264** — Duplicate concentration in the tail inflates rare-class metrics  
  roi 5 / upside 4 / risk 3 / novelty 4 — Protected: cheap-to-falsify contamination audit; either outcome informative.
- **W2-C-0269** — CLIP-filtered data inherits CLIP blind spots: curation bias propagation  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-significance curation-bias tracing; timely as CLIP filtering is ubiquitous.
- **W2-C-0271** — Instance-weighted AP lets dense images dominate: the averaging-axis audit  
  roi 5 / upside 4 / risk 2 / novelty 4 — Protected: cheap-to-falsify metric-convention audit with ranking stakes.
- **W2-C-0276** — The tail-progress illusion: are AP-rare gains concentrated in a few easy classes  
  roi 5 / upside 5 / risk 2 / novelty 4 — Protected: cheap-to-falsify; potentially narrative-changing for the long-tail subfield.
- **W2-C-0277** — Tracing one bias end-to-end: from pretraining statistics to detection errors  
  roi 4 / upside 5 / risk 4 / novelty 4 — Protected: high-risk high-reward mechanistic bias tracing.
- **W2-C-0279** — Open-vocab rarity should be measured against pretraining exposure, not dataset counts  
  roi 5 / upside 5 / risk 3 / novelty 4 — Anchor of the exposure-vs-rarity thread; merge with 0001 at proposal time.
- **W2-C-0282** — The same method across codebases: framework variance vs claimed deltas  
  roi 4 / upside 5 / risk 2 / novelty 4 — Foundational reproducibility constant; either magnitude is a citable result.
- **W2-C-0283** — Stale baselines: how much of reported progress is baseline decay  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-ROI flagship; prior-work attack found the genre exists but not the detection instantiation.
- **W2-C-0284** — How many seeds does detection research need: an empirical power standard  
  roi 4 / upside 5 / risk 2 / novelty 4 — Standards-setting artifact; converts a vague norm into a lookup rule.
- **W2-C-0285** — Shadow tuning: how tuning-budget asymmetry manufactures SOTA  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-ROI flagship with a pre-registrable, bounded design.
- **W2-C-0287** — Do published ablations replicate: sign-flip rates under reseeding  
  roi 4 / upside 5 / risk 3 / novelty 4 — Protected: reviewer-disagreement-prone rigor bomb with bounded scope.
- **W2-C-0291** — A reporting-practices census with teeth: re-experiments on the worst gaps  
  roi 4 / upside 5 / risk 3 / novelty 4 — The correlational teeth distinguish it from checkbox censuses; D&B material.
- **W2-C-0292** — Ten detection tricks under matched compute: which survive  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-value canonical-wisdom audit; expected nulls are the product.
- **W2-C-0298** — Silent benchmark mutations: a hash-audit of public dataset artifacts  
  roi 5 / upside 4 / risk 3 / novelty 5 — Protected: cheap-to-falsify forensic long-shot with scandal upside.
- **W2-C-0299** — Do published improvements stack: the composition test  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-leverage stacking audit; interference matrix is the durable contribution.
- **W2-C-0300** — Author-reported vs independently-measured: a systematic reproduction-gap meta-analysis  
  roi 4 / upside 5 / risk 3 / novelty 4 — Meta-analytic capstone for the rigor family; mostly data collection.
- **W2-C-0302** — Power tables for the field: minimum detectable effects across popular benchmarks  
  roi 5 / upside 5 / risk 2 / novelty 4 — Protected: cheap-to-falsify, standards-setting; anchor of the rigor family.
- **W2-C-0303** — Tuning on the benchmark generalizes worse: the simplicity dividend  
  roi 4 / upside 5 / risk 4 / novelty 4 — Protected: high-risk high-reward, inference-only; confound-control is the craft.
- **W2-C-0305** — Random configurations as the null hypothesis for architecture components  
  roi 4 / upside 5 / risk 3 / novelty 4 — Strong null-hypothesis audit; must position against NAS random-search literature explicitly.
- **W2-C-0306** — Coverage-preserving suppression: conformal prediction meets NMS  
  roi 5 / upside 5 / risk 3 / novelty 5 — Protected: cheap-to-falsify with genuine formal novelty; top-decile idea.
- **W2-C-0308** — Machine psychophysics: staircase procedures for measuring detector thresholds  
  roi 5 / upside 5 / risk 3 / novelty 5 — Protected: methodological transplant with high originality; inference-scale cost.
- **W2-C-0309** — Item response theory for detection benchmarks: separating instance difficulty from model ability  
  roi 5 / upside 5 / risk 2 / novelty 4 — Flagship analysis-only idea; prior IRT-benchmark work must be cited and differentiated.
- **W2-C-0311** — Metrology for CV: applying measurement-uncertainty standards to detection evaluation  
  roi 5 / upside 5 / risk 2 / novelty 5 — Umbrella synthesis with standards-body gravitas; mostly composition of existing measurements.
- **W2-C-0319** — Weak-to-strong generalization in dense prediction: when can weak teachers train stronger students  
  roi 4 / upside 5 / risk 4 / novelty 4 — Protected: high-risk high-reward; timely transplant with a controlled design.
- **W2-C-0321** — Behavioral contracts for detector updates: regression testing beyond AP  
  roi 4 / upside 5 / risk 3 / novelty 4 — Strong applied-science bid; must cite backward-compatibility literature and lead with contracts.
- **W2-C-0326** — Half the remaining COCO errors are not model errors  
  roi 5 / upside 5 / risk 2 / novelty 4 — Anchor annotation-quality claim; prior work erodes surprise, not value.
- **W2-C-0327** — 2015 architecture, 2026 recipe: how much progress is training practice  
  roi 4 / upside 5 / risk 3 / novelty 4 — High-ROI flagship; classification precedent raises confidence the effect is large.
- **W2-C-0328** — A 1k-image subset ranks detectors as well as the full benchmark  
  roi 5 / upside 4 / risk 2 / novelty 4 — Cheap and useful; should be the applied half of the IRT paper (0309).
- **W2-C-0330** — Augmentation is just data: gains recoverable by more images  
  roi 4 / upside 5 / risk 3 / novelty 4 — Deep equivalence question; strongest of the training-science trio after 0327.
- **W2-C-0338** — The small-object ceiling is human, not machine  
  roi 5 / upside 5 / risk 3 / novelty 5 — Protected: cheap-to-falsify, foundational; among the best of the whole batch.
- **W2-C-0341** — Batched inference cross-talk: your detections depend on your batchmates  
  roi 4 / upside 5 / risk 3 / novelty 5 — Original attack surface; cheap to demonstrate or refute.
- **W2-C-0344** — Instructions beat annotators: labeling-protocol effects exceed inter-annotator noise  
  roi 5 / upside 5 / risk 2 / novelty 5 — Protected: cheap-to-falsify, foundational dataset-epistemology; top-decile idea.
- **W2-C-0345** — Foundation-model detection advantage partly reduces to test-set exposure  
  roi 4 / upside 5 / risk 3 / novelty 4 — Timely contamination audit; the detection instantiation is still unclaimed.

## Tier B — Reserve keeps (28 ideas)

Kept, but behind Tier A on upside-per-cost. Pull from here if Tier A ideas die in later prior-work attacks.

- **W2-C-0013** — Small objects are detected from context, not appearance  
  roi 4 / upside 4 / risk 3 / novelty 4 — Simple counterintuitive causal test, cheap; protect.
- **W2-C-0080** — GT tightness conventions vary within single datasets: an intra-dataset audit  
  roi 4 / upside 4 / risk 3 / novelty 4 — Novel measurable mechanism of benchmark noise; cheap. Protect against average-score death.
- **W2-C-0116** — Detectors that see ghosts: hallucinated detections of removed objects  
  roi 4 / upside 4 / risk 2 / novelty 3 — Surviving wedge: detector ghost-rate benchmark; execute with strict artifact controls.
- **W2-C-0125** — Boxes snap to the stride grid: quantization artifacts in outputs  
  roi 4 / upside 4 / risk 2 / novelty 4 — Original cheap measurement with a potential free improvement; protect.
- **W2-C-0148** — Video architectures vs frame detector plus tracker: an equal-compute showdown  
  roi 4 / upside 4 / risk 3 / novelty 4 — Decisive equal-compute negative-result candidate for video detection.
- **W2-C-0154** — Self-training gains evaporate when the confidence threshold is honestly chosen  
  roi 4 / upside 4 / risk 3 / novelty 4 — Concrete leakage audit with quantified prediction; cheap.
- **W2-C-0201** — Decomposing the syn2real gap: content, appearance, and label convention  
  roi 4 / upside 4 / risk 3 / novelty 4 — Causal decomposition missing from a large literature; feasible with open simulators.
- **W2-C-0228** — Hallucinated-label noise rates in diffusion-generated detection training data  
  roi 4 / upside 4 / risk 2 / novelty 4 — Timely audit of an accelerating practice; quantified harm model.
- **W2-C-0241** — Synthetic degradations mislead restoration research: detection utility on real degradations  
  roi 4 / upside 4 / risk 2 / novelty 3 — Cheap ranking-disagreement audit that would redirect restoration-for-vision research.
- **W2-C-0243** — Objects drift under img2img augmentation: quantifying geometric label corruption  
  roi 4 / upside 4 / risk 3 / novelty 4 — Timely, measurable, and actionable; generative augmentation papers rarely check box validity.
- **W2-C-0245** — Temporal consistency beats per-frame quality: video SR for video detection  
  roi 4 / upside 4 / risk 3 / novelty 4 — Inference-only ranking-reversal study in an under-audited corner (video SR for machines).
- **W2-C-0251** — Photographer framing bias: the decentered test set  
  roi 4 / upside 4 / risk 3 / novelty 4 — Protected: simple counter-intuitive framing-bias audit with a clean construction.
- **W2-C-0266** — Same word, different concept: cross-dataset taxonomy misalignment as measurable noise  
  roi 4 / upside 4 / risk 2 / novelty 4 — Quantifies a nuisance everyone hand-waves; cheap and reusable.
- **W2-C-0267** — Benchmarks age: temporal decay of detection AP on contemporary imagery  
  roi 4 / upside 4 / risk 3 / novelty 4 — Fresh temporal-validity question with a falsifiable class-structure prediction.
- **W2-C-0272** — Benchmarks oversample interesting images: difficulty-distribution mismatch with deployment  
  roi 4 / upside 4 / risk 3 / novelty 4 — Deployment-relevant evaluation audit; empty-frame FP behavior is under-measured.
- **W2-C-0273** — Generative tail augmentation imports generator stereotypes into rare classes  
  roi 4 / upside 4 / risk 3 / novelty 4 — Timely audit of generative tail augmentation with a falsifiable split design.
- **W2-C-0290** — Determinism audit of popular detection repos  
  roi 4 / upside 4 / risk 2 / novelty 4 — Actionable infrastructure audit; natural host for 0288/0289 as sections.
- **W2-C-0294** — Checkpoint selection by test performance: prevalence and inflation size  
  roi 4 / upside 4 / risk 2 / novelty 4 — Cheap, certain, and produces a reusable correction constant.
- **W2-C-0296** — ImageNet init is not one thing: pretrained-weight provenance effects  
  roi 4 / upside 4 / risk 2 / novelty 4 — Timely hidden-variable audit; bundles naturally with the silent-variables family.
- **W2-C-0310** — Design-based test sets: survey sampling for deployment-valid detection estimates  
  roi 4 / upside 4 / risk 3 / novelty 4 — Methodologically serious D&B contribution; annotation-bounded.
- **W2-C-0312** — Optimal experiment design for ablation studies  
  roi 4 / upside 4 / risk 2 / novelty 4 — Cheap, useful, certain-outcome methodology transfer.
- **W2-C-0329** — Learned proposals contribute nothing at modern scale  
  roi 4 / upside 4 / risk 3 / novelty 4 — Protected: simple counter-intuitive; two runs to a quotable finding.
- **W2-C-0332** — Detectors barely use global context: the cropping test  
  roi 4 / upside 4 / risk 3 / novelty 4 — Protected: simple counter-intuitive with a clean bound; inference only.
- **W2-C-0333** — Silhouettes are almost enough: shape suffices for most detection classes  
  roi 4 / upside 4 / risk 3 / novelty 4 — Cheap falsification with an existing literature to collide with productively.
- **W2-C-0334** — NMS-free wins are tuning artifacts  
  roi 4 / upside 4 / risk 3 / novelty 4 — Protected: reviewer-disagreement-prone adversarial audit at inference cost.
- **W2-C-0335** — Label assignment research stops mattering at scale  
  roi 4 / upside 4 / risk 3 / novelty 4 — Tests whether a whole subfield's deltas survive modern scale; bounded compute.
- **W2-C-0339** — Only rank matters: confidence magnitudes carry no deployable information  
  roi 4 / upside 4 / risk 2 / novelty 4 — Cheap invariance audit that reframes what calibration buys in detection.
- **W2-C-0340** — Resolution is nothing but object pixel count  
  roi 4 / upside 4 / risk 3 / novelty 4 — Protected: simple counter-intuitive causal isolation at inference cost.

## Protected exceptions — ideas that would have died on average score

These score mediocre-to-poor on simple averages (risk 4, or novelty/feasibility dents) but are kept deliberately under the protection mandate:

- **W2-C-0055** (fresh i.i.d. COCO test set) — expensive and risky, but the single most informative missing artifact in detection evaluation. High-risk high-reward.
- **W2-C-0277** (end-to-end bias tracing) — instrumentation could eat the project; mechanistic payoff justifies it. High-risk high-reward.
- **W2-C-0303** (tuning-induced generalization tax) — confound-laden observational design reviewers will fight about; inference-only cost makes the bet cheap. Reviewer-disagreement-prone.
- **W2-C-0319** (weak-to-strong in dense prediction) — theory half may not land; timely transplant with controlled design. High-risk high-reward.
- **W2-C-0298** (benchmark hash-audit) — probable boring outcome, scandal-grade tail. Cheap-to-falsify long-shot.
- **W2-C-0341** (batch cross-talk exploit) — niche deployment surface; original attack, cheap demo. Cheap-to-falsify.
- **W2-C-0329** (vestigial RPN), **W2-C-0332** (cropping test), **W2-C-0333** (silhouettes), **W2-C-0340** (object pixel count) — simple counter-intuitive falsifications; each is 1–2 runs or inference-only from a possibly-wrong premise, which is exactly the class average-scoring kills.
- **W2-C-0334** (NMS-free wins are tuning artifacts) — adversarial re-tuning of published baselines; reviewer-disagreement-prone by construction.
- **W2-C-0287** (ablation sign-flip rates) — accuses the literature's component claims wholesale; disagreement-prone, bounded compute.
- **W2-C-0251** (photographer framing bias), **W2-C-0135** (co-occurrence overrides appearance), **W2-C-0013** (small objects detected from context) — counter-intuitive causal probes whose middling soundness scores mask high information value.
- **W2-C-0080** (intra-dataset tightness drift), **W2-C-0125** (stride-grid snapping) — small, odd, original measurements that averages would drown.

## Mutations worth carrying forward (not counted in keep-set)

58 ideas received mutate verdicts; the ones I would actually carry, with their surviving form (full details in `scores.jsonl` and `prior_work_attack.md`):

- **0046 → annotation-noise band + claims audit** (post COCO-ReM framing)
- **0032 → AP-rare significance audit** of published long-tail claims (Dave et al. collision)
- **0226-cluster (0227/0230/0248 fold in) → GT-controlled SR hallucination accounting**
- **0082 → SAM failure-prediction law** (atlas already exists)
- **0081 → within-family compute-matched pretraining-transfer test** (Battle-of-the-Backbones collision)
- **0003 → NMS-free-era suppression re-decomposition**
- **0328 → application section of 0309 (IRT)**
- **0116 → ghost-rate benchmark with inpainting-artifact controls**
- **0263+0268 → one tail-context-dependency paper, two instruments**
- **0289+0288 → sections of 0290 (silent-variables/determinism audit)**
- **0304 → merged into 0300 (reproduction-gap meta-analysis)**
- **0315 → deployment-cost extension of 0255**
- **0325+0238 → forensic evidence standards for CV (likelihood-ratio spine)**
- **0050/0049 → components of the 0311 metrology budget**

## Bundling note for the PI

Tier A contains natural multi-idea papers; treating each ID as one paper would overcount the batch. Obvious bundles: rigor/metrology (0302+0070+0064+0311+0284), long-tail forensics (0276+0256+0261+0264+0255), OVD evaluation conventions (0011+0124+0145+0001+0279), GT epistemology (0338+0344+0259+0080+0326), SR truthfulness (0226+0248+0231+0236).
