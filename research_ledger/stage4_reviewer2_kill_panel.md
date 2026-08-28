# Stage 4 — Reviewer #2 Kill Panel (Windows1 PI)

Role: hostile CVPR/ICCV/MICCAI reviewer. Each proposal rejected, then assessed for whether a real experiment rescues it.

Verified citations used (title + year + URL; all checked against live sources):

- Kumar, Ma, Liang. *Understanding Self-Training for Gradual Domain Adaptation*. 2020. https://arxiv.org/abs/2002.11361
- Wang et al. *Understanding Gradual Domain Adaptation: Improved Analysis, Optimal Path and Beyond*. 2022. https://arxiv.org/abs/2204.08200
- Li et al. *HalluSegBench: Counterfactual Visual Reasoning for Segmentation Hallucination Evaluation*. 2025. https://arxiv.org/abs/2506.21546
- Byrd, Lipton. *What is the Effect of Importance Weighting in Deep Learning?* 2019. https://arxiv.org/abs/1812.03372
- Goh et al. *Multimodal Neurons in Artificial Neural Networks*. 2021. https://distill.pub/2021/multimodal-neurons/
- Wortsman et al. *Robust fine-tuning of zero-shot models* (WiSE-FT). 2022. https://arxiv.org/abs/2109.01903
- Ramanathan et al. *PACO: Parts and Attributes of Common Objects*. 2023. https://arxiv.org/abs/2301.01795
- Pham et al. *Learning to Predict Visual Attributes in the Wild* (VAW). 2021. https://arxiv.org/abs/2106.09707
- Cheng et al. *Boundary IoU: Improving Object-Centric Image Segmentation Evaluation*. 2021. https://arxiv.org/abs/2103.16562
- Liu et al. *GRES: Generalized Referring Expression Segmentation*. 2023. https://arxiv.org/abs/2306.00968

The "ACL Findings 2025 one-generation NLP analog" cited by P1: UNSURE which paper — must be pinned or dropped.

---

## P1 SEG-0252 — Multi-generation model-in-the-loop labeling drift

- **Rejection:** Model-collapse tourism ported to masks. The metrics (boundary histograms, hole-filling, vertex stats) measure tool-UI artifacts, not "ontology drift" — annotators accept SAM's default mask to save clicks, and any assistive prior produces convergence to that prior. Multi-generation studies need real annotator cohorts, which the budget won't survive, and "students inherit their labels' statistics" is trivially true, hence unfalsifiable as posed.
- **Hidden assumption:** Annotator pools per generation are exchangeable; drift is model-caused, not fatigue/instruction/UI-default-caused.
- **Confounder:** Click budget and default-mask acceptance drive every proposed statistic independent of the teacher's ontology.
- **Missing baseline:** Human-only multi-generation arm (same UI, same time budget) — instruction drift happens without any model — plus a second-teacher arm to show teacher-specificity.
- **Trivial alternative:** Laziness: annotators accept defaults; conventions converge to whatever the tool proposes.
- **Shut-me-up experiment:** Two-generation crossover: gen-2 cohorts re-label under teacher A vs teacher B vs no teacher, matched UI/time. Show a classifier identifies the teacher from mask statistics (>90%), the signature exceeds human-only drift, and a student trained on gen-2-A labels reproduces A's signature on held-out images.
- **Decision:** KEEP-IF-EXPERIMENT.
- **Remaining fatal flaw:** Real annotator generations are expensive; simulated annotators would gut the claim.

## P2 SEG-0250 — Rare states vs rare classes at matched frequency

- **Rejection:** "Matched pixel/instance frequency" is a mirage: a shattered plate and a canonical axolotl differ in boundary complexity, part topology, occlusion, context co-occurrence, and annotation quality. One covariate of a dozen is controlled and the design is called causal. Whichever direction the result goes, it is an artifact of which states/classes were picked from noisy PACO/VAW attribute labels.
- **Hidden assumption:** Frequency is the dominant error driver, so matching it isolates the state effect.
- **Confounder:** Rare states change mask geometry (fragmentation, deformation) — error rises because delineation is harder for anyone, including humans.
- **Missing baseline:** Boundary-complexity-matched control; oracle-box arm (GT box given) to split recognition failure from delineation failure.
- **Trivial alternative:** Rare states = more occlusion/deformation = geometrically harder masks. No prior story needed.
- **Shut-me-up experiment:** Counterfactual pairs (diffusion-edited or rendered: same instance, canonical vs rare state, boundary complexity measured and matched) with a training-frequency knob. Show the gap survives complexity matching and is dose-dependent in state frequency, not class frequency.
- **Decision:** KEEP-IF-EXPERIMENT.
- **Remaining fatal flaw:** Full nuisance matching on real data may be impossible; the synthetic escape hatch invites sim2real dismissal.

## P3 SEG-0275 — Post-cutoff concept-name open-vocab benchmark

- **Rejection:** LiveBench-for-segmentation, and the bottleneck is supply, not the idea: genuinely new names with segmentable, visually distinctive referents are rare; most are compositional or synonyms the model resolves lexically, contaminating the backoff analysis sold as the contribution. Cutoffs are unverifiable for continually-updated or retrieval-augmented models. Auto-refresh guarantees irreproducible numbers.
- **Hidden assumption:** Model knowledge boundary = published training cutoff; no retrieval.
- **Confounder:** New names co-occur with new visual domains (product/social-media imagery) — failures may be domain shift, not lexical novelty.
- **Missing baseline:** Nonce-word control: existing concepts renamed with made-up words. If backoff behavior is identical, the post-cutoff collection machinery adds nothing over OOV-ness.
- **Trivial alternative:** Tokenizer fragmentation on any OOV string explains the behavior taxonomy.
- **Shut-me-up experiment:** Behavioral discontinuity at each model's cutoff using time-stamped names with pre/post domain distributions matched, AND the nonce control failing to reproduce the backoff taxonomy.
- **Decision:** KEEP-IF-EXPERIMENT.
- **Remaining fatal flaw:** Maintenance burden + per-model cutoff verification; a benchmark without a surprising finding is midlist.

## P4 SEG-0276-M — Per-category prior shape field; transferable coefficient

- **Rejection:** "Transferable coefficient" presumes a one-dimensional tradeoff between "prompt-semantic strength" and "local evidence," neither of which has an agreed operationalization — both will be defined via the authors' own knobs, making the law circular. Masks are discrete multimodal outputs; "interpolation" between evidence and prior needs a metric space never specified. The geometry-vs-presence contrast with HalluSegBench may collapse: geometry-level hallucination could be presence-level hallucination at higher resolution.
- **Hidden assumption:** Prior and evidence combine monotonically in some latent space where interpolation is meaningful.
- **Confounder:** Degrading evidence (blur/occlusion) also perturbs encoder features governing prompt attention — the two knobs are not independent.
- **Missing baseline:** Bayesian mean-shape template + likelihood model; if it reproduces the curves, the "field" is class-mean shape regression.
- **Trivial alternative:** Under weak evidence the model emits the category's average training mask. Memorized mean shape, no field.
- **Shut-me-up experiment:** Fit the coefficient on model A / categories X; predict quantitatively (with CIs) mask geometry on model B / held-out categories / held-out degradation types, beating the mean-shape baseline.
- **Decision:** KEEP-IF-EXPERIMENT — HRHR; killer experiment is inference-only (cheap).
- **Remaining fatal flaw:** Operationalizing "prompt-semantic strength" may never survive review.

## P5 SEG-0355-M — Undefined vs uncertain conflation (GRES no-target + abstention)

- **Rejection:** "No monotone threshold on existing scores separates them" is a universal negative over a nonparametric class and cannot be proven empirically; only the scores actually tried can be shown to fail, which reads as "didn't try hard enough" (temperature scaling? ensembles? evidential heads?). The distinction itself is model-class-relative: "more data would help" is not a property of the input alone. Ground truth for "undefined" is a fuzzy human judgment.
- **Hidden assumption:** A ground-truth undefined/uncertain partition exists and annotators agree on it (report κ or it didn't happen).
- **Confounder:** Undefined queries are linguistically weirder — a language-only classifier may separate them, locating the "conflation" in query construction, not the model.
- **Missing baseline:** Ensemble disagreement, MC-dropout, evidential heads, LLM verbalized confidence — the claim dies if any off-the-shelf epistemic proxy separates the classes.
- **Trivial alternative:** The no-target head was trained only on "object absent," so of course it conflates everything else — a training-data statement, not a finding.
- **Shut-me-up experiment:** Constructive ground truth: pairs where more data provably disambiguates (subsample→full ablation) vs provably cannot (ambiguous by construction); ROC≈0.5 for the full enumerated score battery, plus a trained probe that DOES separate them — signal exists, scores miss it.
- **Decision:** KEEP-IF-EXPERIMENT (borderline KILL at current claim strength).
- **Remaining fatal flaw:** Must weaken to an enumerated-scores claim, which weakens the headline.

## P6 SEG-0002-M — Boundary-jitter noise floor; SOTA re-ranking

- **Rejection:** The headline logic is statistically incoherent: GT jitter is shared across all models evaluated on the same labels, so it does not subtract from between-model BIoU deltas — paired comparisons cancel common-mode noise, and a 0.5% delta can be significant under a paired test even when the floor is 2%. "Annotation noise swamps small gains" is decade-old folk knowledge; the novelty reduces to a re-annotation study plus an invalid subtraction.
- **Hidden assumption:** GT jitter acts as independent additive noise w.r.t. model ranking. It is common-mode instead.
- **Confounder:** Multi-annotator variance mixes annotator skill, instruction ambiguity, and genuine boundary ambiguity (mixed pixels).
- **Missing baseline:** Paired bootstrap on existing leaderboards — free, no re-annotation. If deltas already fail paired tests the machinery is redundant; if they pass, the claim is false. Also training-seed variance.
- **Trivial alternative:** Small deltas are seed noise — cheaper explanation than annotation noise.
- **Shut-me-up experiment:** ≥5-annotator re-labeling of val subsets; show model rankings flip (not merely shrink) across annotator references, with seed variance controlled and paired tests reported.
- **Decision:** KEEP-IF-EXPERIMENT — cheap and useful, but incremental.
- **Remaining fatal flaw:** The paired-evaluation objection may kill the "gains vanish" headline outright.

## P7 SEG-0240-M — Variance-matched sampling vs reweighting

- **Rejection:** Full-batch training is a different optimization regime (no implicit SGD regularization, different schedules, BatchNorm pathologies) — the "control" changes more than it fixes. Matching scalar gradient-noise variance leaves the noise covariance structure unmatched, which is plausibly the thing that matters. "Remaining gap = context-stat shift" is argument-by-elimination, and the elimination is not exhaustive: normalization layers alone see different activation statistics under oversampling.
- **Hidden assumption:** Scalar noise variance is a sufficient statistic for the optimization-side difference.
- **Confounder:** BN/GN statistics under resampling — an architectural channel that is neither "SGD noise" nor "context stats."
- **Missing baseline:** GN/LN-only architecture arm; long-vs-short training arm (importance-weighting effects vanish with training time in overparameterized nets — Byrd & Lipton 2019).
- **Trivial alternative:** The gap is a training-duration artifact.
- **Shut-me-up experiment:** Factorial: {resample, reweight} × {BN, GN} × {explicit noise-covariance injection} × {short, long}, on paste-synthesized data where context stats are independently manipulable; show the gap tracks the context manipulation only.
- **Decision:** KEEP-IF-EXPERIMENT — an ML-theory paper in a CVPR costume.
- **Remaining fatal flaw:** Elimination never closes; factorial compute is heavy.

## P8 SEG-0085-M — Lesion suppression surface; universal threshold

- **Rejection:** "Universal across pipelines/modalities" is precisely the claim MICCAI reviewers distrust: suppression depends on training-set lesion-size distribution, loss choice, resolution, and — critically — postprocessing: connected-component filtering deletes small lesions after the network, so much of the "suppression probability" is a pipeline config, not a model property. A surface fit over N pipelines is a survey; universality dies on the first pipeline trained with small-lesion oversampling. Synthetic insertion confounds insertion realism with detectability.
- **Hidden assumption:** Suppression is a function of (size, contrast, enhancement) only — not location, background tissue, or training-set statistics.
- **Confounder:** Postprocessing CC-filtering and resampling interpolation.
- **Missing baseline:** Human reader curve at matched size×contrast (is the model below the imaging-physics floor?); postprocessing-ablated arm.
- **Trivial alternative:** Resolution/PSF limit plus the known small-object bias of Dice loss.
- **Shut-me-up experiment:** Phantom/insertion study across ≥4 independent pipelines, 2 modalities, postprocessing ablated, showing suppression surfaces collapse onto one curve after normalizing by voxel size and training-set size distribution; functional form pre-registered.
- **Decision:** KEEP-IF-EXPERIMENT — clinically important; soften "universal" to "conditional law."
- **Remaining fatal flaw:** One adversarially trained pipeline falsifies universality; the surviving claim is weaker.

## P9 SEG-0285 — In-image text redirects masks; layer mechanism

- **Rejection:** Typographic attacks are five years old (Goh et al. 2021); extending them from captions to masks is the expected next domino — reviewers already assume masks follow captions, so the headline replicates the community's null hypothesis. "Which layers" from activation patching is correlational and layer indices don't transfer across architectures. Physical sticker trials will be underpowered.
- **Hidden assumption:** Redirection flows through the text-reading pathway rather than through the sticker's raw saliency.
- **Confounder:** Any high-contrast patch attracts mask decoders — saliency-matched controls required.
- **Missing baseline:** Scrambled/unreadable text sticker at matched size/contrast; quantified caption-redirect-without-mask-redirect dissociation.
- **Trivial alternative:** Salient patch perturbs the mask decoder; nothing about reading.
- **Shut-me-up experiment:** Dissociation: cases where captions redirect but masks don't (or vice versa) with flat scrambled-text controls; then a localized text-pathway patching intervention that flips the mask, replicated on ≥2 architectures.
- **Decision:** KEEP-IF-EXPERIMENT — cheap, likely to work, limited ceiling.
- **Remaining fatal flaw:** Novelty ceiling; adjacency to adversarial-patch literature invites "incremental."

## P10 SEG-0193-M — Test-replica spiking; ΔmIoU inflation curve

- **Rejection:** Contamination-inflation curves are dataset- and capacity-specific; a curve fitted on one setup licenses no generalization, so the deliverable is a calibration table nobody else can use. "Replica" is undefined — exact dup, near-dup, augmented, same-scene — and the curve differs by orders of magnitude across these; the regime that matters (semantic near-duplicates from generative pipelines) is exactly where "known rates" are unknowable.
- **Hidden assumption:** Inflation is a smooth monotone function of replica rate, independent of the rest of training.
- **Confounder:** Adding replicas changes dataset size and class balance simultaneously.
- **Missing baseline:** Retrodiction on real contaminated corpora via dedup detectors; the near-dup vs exact-dup axis.
- **Trivial alternative:** Memorization of duplicates is textbook; inflation ≈ duplicate fraction × per-image gain is nearly dimensional analysis.
- **Shut-me-up experiment:** Curve fitted on setup A predicts inflation (within CI) on unseen dataset/model B including a perceptual-distance-graded near-dup regime, packaged as an estimator that audits a real suspect training set.
- **Decision:** KILL as standalone (salvage as a section of a contamination-audit tool).
- **Remaining fatal flaw:** No transportable law is plausible.

## P11 SEG-0103-M — UDA amplification exponent vs GDA theory; churn stopping rule

- **Rejection:** The GDA bound is a worst-case upper bound already known to be loose — Kumar et al. 2020 give exponential-in-T; Wang et al. 2022 improved it to additive — so "empirical exponent beats theory" is a foregone conclusion; comparing an empirical fit to a non-tight bound is a category error. The stopping rule is the useful half, but it's an anecdote until it beats trivial baselines across many shifts.
- **Hidden assumption:** A single power-law exponent exists; self-training failure is often phase-transition-like (fine, fine, collapse), not power-law.
- **Confounder:** Exponent estimates entangle shift magnitude with pseudo-label threshold and augmentation choices.
- **Missing baseline:** Target-entropy / proxy-risk model selection heuristics; random stopping.
- **Trivial alternative:** Churn and degradation both correlate with shift size; churn adds nothing over measuring shift.
- **Shut-me-up experiment:** Pre-registered stopping rule evaluated on ≥8 shift benchmarks it wasn't tuned on, beating entropy/proxy-risk with effect sizes; separately map the phase structure where power-law fits fail.
- **Decision:** KEEP-IF-EXPERIMENT (stopping rule only; drop the theory-comparison framing).
- **Remaining fatal flaw:** Theory half is unsalvageable; rule alone is workshop-tier unless it wins broadly.

## P12 VFM-0263/0274 — Constrained SAM-FT: max Dice s.t. promptability drop < ε

- **Rejection:** The entire novelty is a constraint formulation the community implements informally with LoRA, frozen encoders, replay, and weight interpolation (WiSE-FT spans a near-free Pareto front by interpolating checkpoints). Unless the constrained optimizer strictly dominates those on the Dice-vs-promptability front, this is a reinvention with a Lagrangian. SA-1B has no held-out prompt protocol, so "promptability" will be an invented metric, and the constraint binds w.r.t. the authors' own yardstick.
- **Hidden assumption:** SA-1B promptability proxies foundation behavior generally (zero-shot transfer on unseen domains, interactivity).
- **Confounder:** ε on SA-1B (natural images) can be trivially satisfied while promptability collapses on other domains — constraint on the wrong distribution.
- **Missing baseline:** Checkpoint weight interpolation, LoRA-rank sweep, SA-1B replay fraction sweep — all at matched operating points.
- **Trivial alternative:** Linear interpolation already spans the whole Pareto front.
- **Shut-me-up experiment:** Pareto plot on 3 target domains (incl. medical): constrained method vs interpolation vs LoRA vs replay, promptability measured on SA-1B AND held-out third domains; show strict dominance anywhere on the front.
- **Decision:** KEEP-IF-EXPERIMENT — engineering-safe, novelty-fragile.
- **Remaining fatal flaw:** High probability the interpolation baseline matches, leaving no paper.

---

## Top-7 for Stage 5 engineering

| Rank | Idea | Rationale |
|---|---|---|
| 1 | P4 shape-prior field | HRHR protected: killer experiment is inference-only and decisively falsifiable (cross-model, held-out-category prediction vs mean-shape baseline). |
| 2 | P9 typographic mask attack | Cheapest to execute; dissociation + patching converts a known effect into a mechanism claim. |
| 3 | P2 rare states vs rare classes | Counterfactual state-edit pairs feasible with current editing models; strong conceptual payoff if the gap survives complexity matching. |
| 4 | P5 undefined vs uncertain | Repaired constructive framing (probe separates, scores don't) is a real finding; medium cost. |
| 5 | P6 noise-floor re-rank | Near-free triage: paired bootstrap on existing leaderboards first — either outcome informative; de-risks the re-annotation spend. |
| 6 | P12 constrained SAM-FT | Safe engineering with built-in kill switch: run the weight-interpolation baseline first; proceed only if headroom exists. |
| 7 | P8 lesion suppression | MICCAI-valuable after softening "universal"; gate on a cheap 2-pipeline postprocessing-ablated pilot. |

Dropped: P1 (HRHR but the killer experiment needs real multi-generation annotator cohorts — expensive, so the cheap-killer protection rule doesn't apply), P3 (run only the cheap nonce-word pilot; full auto-refreshing bench is a maintenance sink), P7 (factorial compute heavy; elimination logic never closes), P11 (theory half dead; stopping rule workshop-tier), P10 (killed).
