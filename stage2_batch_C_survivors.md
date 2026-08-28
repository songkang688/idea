# Stage 2 — Batch C Survivors (74 ideas kept for further study)

Reviewer: independent Stage-2 reviewer for Windows5 research-idea evolution.
Source: `stage1_batch_C_ideas.md` (340 ideas); scores and keep decisions in `stage2_batch_C_scores.md`.
Each survivor retains its original Stage-1 fields verbatim, followed by the Stage-2 review fields (Survival Reason, Major Risks, Unresolved Questions, Required Experiments, Reviewer Opinion).

Survivors per cluster: C1 5, C2 5, C3 5, C4 5, C5 6, C6 7, C7 6, C8 7, C9 6, C10 6, C11 6, C12 10 — total 74.

---

## C1. PEFT failure & when full fine-tuning is necessary — 5 kept

### IDEA-C-0001
- **One-sentence idea:** Predict PEFT failure from the spectral structure of the weight update that full fine-tuning would make.
- **Problem:** LoRA-style methods sometimes match full fine-tuning (FT) and sometimes fail badly, with no accepted pre-hoc predictor of which regime a task falls into.
- **Core Hypothesis (falsifiable):** PEFT underperforms full FT precisely when the singular-value spectrum of (W_FT − W_pre) is heavy-tailed (effective rank above the adapter rank); tasks with rapidly decaying spectra show no gap.
- **Why Important:** Would turn "try LoRA and hope" into a measurable decision rule, saving compute and preventing silent under-adaptation in clinical deployments.
- **Why Possibly Novel:** Intrinsic-dimension arguments exist for *why LoRA works*; a systematic, task-level *failure predictor* validated across dense and classification tasks is missing.
- **Minimal Experiment:** Fully fine-tune a ViT-B on ~10 diverse tasks (natural + medical, dense + classification), compute per-layer update spectra, correlate spectral decay rate with the LoRA-vs-FT gap at matched budgets.
- **Main Risk:** The update spectrum may itself depend on optimizer/regularization choices, making the predictor unstable across training recipes.

- **Survival Reason:** Turns the PEFT-vs-full-FT choice into a measurable pre-hoc decision rule; a clear falsifiable spectral criterion with broad practical reach across every adaptation deployment.
- **Major Risks:** Update spectra depend on optimizer/regularization recipe, so the predictor may be unstable across training regimes; requires ~10 full fine-tunes to establish ground truth.
- **Unresolved Questions:** Which layers' spectra matter most; whether the criterion holds for dense and 3D tasks; whether adapter placement interacts with spectral shape.
- **Required Experiments:** Build a 10-task FT update-spectrum bank (natural + medical, dense + classification); LoRA rank sweeps at matched budgets; rank-correlation of spectral decay vs realized gap; recipe-robustness replication across 2 optimizers and 2 schedules.
- **Reviewer Opinion:** The strongest "predictive law" idea in C1. Even a negative result (spectra recipe-unstable) is informative for the intrinsic-rank narrative that underpins LoRA's popularity.

### IDEA-C-0011
- **One-sentence idea:** Adjudicate whether PEFT failures are capacity failures or optimization failures by giving PEFT unbounded compute.
- **Problem:** When LoRA lags full FT, papers conclude "insufficient capacity", but LoRA also changes optimization geometry.
- **Core Hypothesis (falsifiable):** For a substantial fraction of "PEFT-hard" tasks, LoRA at fixed rank closes the gap given 5–10× training length with tuned schedules — implying optimization, not capacity, is the binding constraint.
- **Why Important:** The remedy differs completely (better schedules vs higher rank/full FT); current practice may waste capacity to fix an optimization problem.
- **Why Possibly Novel:** Compute-unbounded PEFT training is rarely run because it defeats PEFT's selling point — but as *science* it isolates the mechanism.
- **Minimal Experiment:** Pick 6 tasks with reported LoRA gaps; train LoRA 10× longer with LR re-sweeps; classify each task as capacity- or optimization-limited.
- **Main Risk:** Very long adapter training may overfit small target sets, conflating a third failure mode.

- **Survival Reason:** Clean mechanism adjudication (capacity vs optimization) that changes the remedy for PEFT failures; rare because compute-unbounded PEFT training defeats PEFT's selling point, so nobody runs it.
- **Major Risks:** Very long adapter training overfits small target sets, introducing a third failure mode; conclusions may depend on which "PEFT-hard" tasks are selected.
- **Unresolved Questions:** How to select failure tasks without bias; whether the optimization deficit is fixable by schedule families rather than sheer length.
- **Required Experiments:** 6 tasks with documented LoRA gaps; 10× schedules with learning-rate re-sweeps; overfitting controls with validation-tracked early stopping; per-task classification as capacity- vs optimization-limited.
- **Reviewer Opinion:** Moderate compute, high interpretive payoff; the resulting dichotomy would be cited by essentially every subsequent PEFT paper.

### IDEA-C-0016
- **One-sentence idea:** Test whether PEFT specifically fails at small-lesion sensitivity because the required update lives in high-frequency spatial features.
- **Problem:** Aggregate Dice hides that adaptation methods may differ most on the smallest, most clinically important structures.
- **Core Hypothesis (falsifiable):** The LoRA-vs-FT sensitivity gap grows as lesion size shrinks (log-linear in lesion diameter), and injecting adapters into the patch-embedding/early conv stem removes the size dependence.
- **Why Important:** Small-lesion detection is the highest-stakes regime in oncology screening.
- **Why Possibly Novel:** Size-stratified analysis of PEFT is essentially absent; the frequency-localization mechanism gives it a testable cause.
- **Minimal Experiment:** Lesion segmentation dataset stratified by diameter; LoRA (standard vs +stem) vs full FT; plot per-stratum sensitivity.
- **Main Risk:** Small lesions have noisy ground truth; annotation error may dominate the measured gap.

- **Survival Reason:** Size-stratified PEFT sensitivity targets the highest-stakes clinical regime (small lesions) with a concrete frequency-localization mechanism and an actionable stem-adapter fix.
- **Major Risks:** Small-lesion ground truth is noisy and may dominate the measured gap; per-stratum power requires large lesion counts.
- **Unresolved Questions:** Whether the log-linear size dependence holds across modalities; whether the stem fix suffices or decoder resolution is the true binding factor.
- **Required Experiments:** Lesion datasets stratified by diameter (LiTS/LIDC-class); LoRA vs LoRA+trainable-stem vs full FT; per-stratum sensitivity curves with confidence intervals; annotation-noise audit on the smallest stratum.
- **Reviewer Opinion:** High clinical resonance; pairs naturally with 0020 and could merge with it at the next evolution stage.

### IDEA-C-0020
- **One-sentence idea:** Show that adapting the input stem plus PEFT elsewhere equals full FT for out-of-modality transfer (the "input stem hypothesis").
- **Problem:** RGB-pretrained backbones transferred to ultrasound/OCT/X-ray may fail primarily at the first nonlinearity, not in deep semantics.
- **Core Hypothesis (falsifiable):** For cross-modality transfer, full FT of only the patch-embedding/stem (≤1% of parameters) plus standard LoRA reaches ≥95% of full-FT performance; omitting the stem caps performance regardless of adapter rank.
- **Why Important:** Gives a near-free recipe for the hardest transfer setting in medical imaging.
- **Why Possibly Novel:** Stem-retraining is folklore in scattered repos; a controlled multi-modality validation with the rank-independence claim is missing.
- **Minimal Experiment:** RGB backbone → {ultrasound, OCT, dermoscopy, CXR} tasks; factorial {stem trainable?} × {LoRA rank}; test the predicted ceiling effect.
- **Main Risk:** Some modalities may also need late-layer semantic change (e.g., speckle-defined textures), diluting the claim.

- **Survival Reason:** The "input stem hypothesis" is a precise, cheap, falsifiable ceiling claim for cross-modality transfer with immediate recipe value for the hardest medical transfer setting.
- **Major Risks:** Some modalities (speckle-defined textures) need late semantic change too, diluting the ceiling claim; backbone availability differences confound comparisons.
- **Unresolved Questions:** Where the stem/deep boundary sits per modality; interaction between stem training and adapter rank needs the full factorial to resolve.
- **Required Experiments:** RGB→{ultrasound, OCT, dermoscopy, CXR} factorial {stem trainable?}×{LoRA rank}; test of the predicted rank-independent ceiling; ERF/frequency analyses as mechanism support.
- **Reviewer Opinion:** Folklore-to-law conversion; likely to become the default recipe if confirmed, and cheap enough to falsify quickly if not.

### IDEA-C-0023
- **One-sentence idea:** Test the hypothesis that PEFT cannot *unlearn* — tasks requiring suppression of misleading pretrained features need full FT.
- **Problem:** Some transfers require actively removing a pretrained cue (e.g., texture bias harmful for modality X); additive low-rank updates may be poor at suppression.
- **Core Hypothesis (falsifiable):** On tasks constructed so that a known pretrained cue is anti-correlated with the target label, the LoRA-vs-FT gap is large and grows with the cue's pretrained salience, while on cue-neutral controls the gap vanishes.
- **Why Important:** Identifies a principled class of "must-full-FT" problems, including shortcut-ridden medical datasets.
- **Why Possibly Novel:** PEFT is analyzed as *adding* capability; the asymmetry between adding and suppressing has not been isolated experimentally.
- **Minimal Experiment:** Cue-conflict datasets (texture vs shape; scanner artifact vs pathology) with controllable correlation; measure gap vs cue salience.
- **Main Risk:** Constructed cue conflicts may exaggerate effects relative to natural datasets; needs one natural validation case.

- **Survival Reason:** PROTECTED (high-risk/high-reward). The add-vs-suppress asymmetry would define a principled "must-full-FT" task class; counter-intuitive, theory-adjacent, and directly relevant to shortcut-ridden medical datasets.
- **Major Risks:** Constructed cue-conflict datasets may exaggerate the effect; a natural validation case may be hard to find; pretrained-cue salience is hard to quantify cleanly.
- **Unresolved Questions:** Whether suppression failure persists at high ranks and with DoRA-style variants; whether targeted subtractive updates can repair it without full FT.
- **Required Experiments:** Texture/shape and scanner-artifact cue-conflict datasets with controllable cue-label correlation; gap-vs-salience curves for LoRA vs FT; one natural shortcut-dataset validation arm.
- **Reviewer Opinion:** If confirmed, this changes PEFT doctrine; if refuted, it kills a plausible folk belief. Either outcome justifies the protection.

---

## C2. Catastrophic forgetting in sequential medical/domain adaptation — 5 kept

### IDEA-C-0034
- **One-sentence idea:** Decompose forgetting into feature loss vs readout loss by probing frozen features of forgotten models.
- **Problem:** "The model forgot task A" conflates destroyed representations with a re-pointed decoder/head.
- **Core Hypothesis (falsifiable):** After standard sequential adaptation, a linear/light probe on the adapted backbone recovers most old-task performance (readout forgetting), except under modality change where features are genuinely destroyed — two regimes separable by probe-recovery fraction.
- **Why Important:** The remedy differs completely: cheap head re-tuning vs expensive representation protection.
- **Why Possibly Novel:** Probe-based forgetting decomposition exists for classification; regime mapping across realistic medical shift types does not.
- **Minimal Experiment:** Sequential adaptation across site/protocol/modality shifts; at each step probe old-task performance from frozen features; map recovery fraction by shift type.
- **Main Risk:** Probe capacity choice changes conclusions; needs a probe-capacity sweep.

- **Survival Reason:** The feature-loss vs readout-loss decomposition is the load-bearing measurement for every continual-learning remedy; the regime map by shift type is directly actionable (cheap head re-tuning vs expensive representation protection).
- **Major Risks:** Probe capacity choice changes conclusions; regime boundaries between shift types may be blurry rather than clean.
- **Unresolved Questions:** Whether regimes transfer across architectures; where prompt/adapter-based CL methods sit within the decomposition.
- **Required Experiments:** Sequential adaptation across site/protocol/modality shifts; probe-capacity sweeps (linear → 2-layer); recovery-fraction regime map; replication on two backbones.
- **Reviewer Opinion:** Foundational for C2; several other survivors (0040, 0057) form a natural package with this as the anchor.

### IDEA-C-0040
- **One-sentence idea:** Distinguish erasure from retrieval failure: how much "forgotten" performance returns with a tiny rewinding set.
- **Problem:** Forgetting metrics cannot tell whether knowledge is destroyed or merely inaccessible under the shifted parameterization.
- **Core Hypothesis (falsifiable):** For most site-shift sequences, re-exposure to ≤20 old-domain images restores ≥80% of lost performance in a few steps (retrieval failure), while modality-shift sequences show slow, data-hungry recovery (erasure) — a measurable dichotomy with different protection implications.
- **Why Important:** If forgetting is mostly retrieval failure, cheap "reminder" protocols beat expensive continual-learning machinery.
- **Why Possibly Novel:** Rapid-recovery ("rewinding") curves as a forgetting taxonomy are established in neuroscience but not in medical CL.
- **Minimal Experiment:** After each adaptation step, fine-tune on k∈{5,20,100} old images; plot recovery vs k across shift types.
- **Main Risk:** Recovery speed confounds with learning-rate settings; requires LR-matched controls.

- **Survival Reason:** PROTECTED (high-risk/high-reward). The retrieval-vs-erasure dichotomy could replace heavyweight CL machinery with cheap "reminder" protocols; the neuroscience-grounded rewinding methodology is fresh in this field.
- **Major Risks:** Recovery speed confounds with learning-rate settings; the ≤20-image claim may be dataset-specific; rapid recovery may overfit the reminder set rather than restore knowledge.
- **Unresolved Questions:** What predicts which regime a shift falls into (connects to 0034); whether recovered performance persists through subsequent adaptations.
- **Required Experiments:** Rewinding curves at k∈{5,20,100} old images across site-shift and modality-shift sequences; LR-matched controls; held-out old-domain evaluation to exclude reminder-set overfitting.
- **Reviewer Opinion:** The cheapest high-upside experiment in C2; a positive result is a practice-changer for hospital deployments and the framing is memorable.

### IDEA-C-0050
- **One-sentence idea:** Benchmark sequential-checkpoint weight averaging as a nearly-free anti-forgetting baseline that may beat dedicated CL methods.
- **Problem:** CL literature compares against weak naive baselines; simple weight averaging across domain checkpoints is rarely in the comparison set.
- **Core Hypothesis (falsifiable):** Uniform or Fisher-weighted averaging of per-domain fine-tuned checkpoints attains lower average forgetting than EWC and matches modest replay on cross-site medical segmentation — at zero training-time overhead.
- **Why Important:** If a trivial baseline wins, the field's method complexity is unjustified, and deployment guidance changes immediately.
- **Why Possibly Novel:** Model soups are known for robustness; positioning and rigorously testing them as a *continual-learning baseline* in medical dense prediction is largely unexplored.
- **Minimal Experiment:** 4-domain sequence; compare naive sequential, EWC, 1% replay, and checkpoint averaging on average accuracy/forgetting.
- **Main Risk:** Averaging fails when domains induce non-linearly-connected minima (e.g., modality shifts); scope must be honestly reported.

- **Survival Reason:** PROTECTED (simple counter-intuitive). Checkpoint weight averaging as a continual-learning baseline: if a trivial zero-overhead method beats EWC and matches replay, the field's method complexity is unjustified.
- **Major Risks:** Averaging fails when domains induce non-linearly-connected minima (modality shifts); risks being dismissed as "just model soups" without the CL positioning.
- **Unresolved Questions:** Where averaging breaks (shift-magnitude threshold); uniform vs Fisher-weighted averaging; interaction with sequence length.
- **Required Experiments:** 4-domain sequences comparing naive sequential, EWC, 1% replay, and checkpoint averaging; loss-barrier/connectivity analysis as the mechanism arm; honest scope reporting for failure cases.
- **Reviewer Opinion:** Exactly the deflationary baseline reviewers wish existed; low cost, immediate citation value regardless of outcome.

### IDEA-C-0056
- **One-sentence idea:** Quantify cumulative "TTA drift": continuously running test-time adaptation in deployment causes progressive forgetting.
- **Problem:** TTA methods (entropy minimization, statistics updates) are evaluated per-batch; deployed continuously, their updates compound without any consolidation mechanism.
- **Core Hypothesis (falsifiable):** Under a realistic stream (site mixture with rare-case bursts), continuous TTA degrades monotonically on a frozen reference set, with drift rate proportional to stream non-stationarity; periodic parameter resets trade recent-gain for drift elimination at a measurable exchange rate.
- **Why Important:** TTA is being deployed as a safety feature while possibly being a slow poison; the field needs the drift law.
- **Why Possibly Novel:** Lifelong/continual TTA is nascent; a quantitative drift model tied to stream statistics for medical imaging does not exist.
- **Minimal Experiment:** Simulate 100k-image streams with controlled non-stationarity; run TENT-style TTA continuously; track reference-set performance and fit drift-rate model.
- **Main Risk:** Drift may be method-specific; needs 3 TTA families to claim generality.

- **Survival Reason:** PROTECTED (counter-intuitive, deployment-critical). Continuous test-time adaptation as a "slow poison" is a quantitative drift law the field urgently needs as TTA moves into deployed systems.
- **Major Risks:** Drift may be method-specific rather than general; simulated streams may miss the structure of real clinical non-stationarity.
- **Unresolved Questions:** Optimal reset schedules and their gain/drift exchange rate; whether drift is detectable online without a frozen reference set.
- **Required Experiments:** 100k-image streams with controlled non-stationarity; ≥3 TTA families (entropy-minimization, statistics-update, pseudo-label); drift-rate model fitting; reset-policy trade-off curves.
- **Reviewer Opinion:** Timely and high-impact; the framing will land with both benchmark and clinical audiences. Absorb eliminated 0293 (TTA calibration/boundary costs) as a secondary endpoint.

### IDEA-C-0057
- **One-sentence idea:** Disentangle true representational forgetting from annotation-protocol mismatch when measuring cross-site "forgetting".
- **Problem:** Old-site performance drops after adaptation may partly reflect that the new site's *label style* was learned — a labeling artifact, not knowledge loss.
- **Core Hypothesis (falsifiable):** Re-annotating a small old-site subset under the new site's protocol reduces measured "forgetting" by a substantial fraction (>30%) in protocol-divergent dataset pairs, and by ~0% in protocol-matched pairs.
- **Why Important:** If a chunk of reported forgetting is protocol artifact, the CL literature overestimates the phenomenon it studies.
- **Why Possibly Novel:** Label-protocol confounds in forgetting measurement have not been isolated experimentally.
- **Minimal Experiment:** Two dataset pairs (protocol-matched, protocol-divergent); re-annotate 50 old images per pair under the new protocol; recompute forgetting.
- **Main Risk:** Re-annotation is costly and needs clinician time; keep subsets minimal and targeted.

- **Survival Reason:** Separates annotation-protocol artifact from true representational forgetting — measurement repair that could shrink the field's headline phenomenon by a third.
- **Major Risks:** Re-annotation requires clinician time; protocol-divergent dataset pairs with documented conventions are hard to source.
- **Unresolved Questions:** What share of published forgetting numbers is protocol artifact; whether the same artifact inflates domain-adaptation gaps generally.
- **Required Experiments:** Two dataset pairs (protocol-matched vs protocol-divergent); 50-image re-annotations under the new site's protocol; recomputed forgetting with artifact share quantified.
- **Reviewer Opinion:** Small, surgical, potentially embarrassing to the CL literature in the best way; the design is cheap enough to protect against its data-access risk.

---

## C3. VLMs for dense prediction: alignment vs localization mismatch — 5 kept

### IDEA-C-0061
- **One-sentence idea:** Quantify "global leakage": how much of each CLIP patch token's content is image-level semantics rather than local content.
- **Problem:** Contrastive image-text training optimizes a global objective; patch tokens may become carriers of global information, corrupting their use for dense prediction.
- **Core Hypothesis (falsifiable):** Mutual information between a patch token and the image-level label exceeds that between the token and its own receptive-field content in late CLIP layers, and the leakage ratio predicts zero-shot segmentation failure per layer.
- **Why Important:** Explains, mechanistically, why naive dense readouts from CLIP fail — and where (which layer) to read instead.
- **Why Possibly Novel:** Global-vs-local content of patch tokens has been gestured at (attention visualizations) but not measured information-theoretically or linked predictively to dense-task performance.
- **Minimal Experiment:** Probe patch tokens for (a) global label and (b) local patch identity across layers; correlate the leakage ratio with per-layer zero-shot segmentation quality.
- **Main Risk:** MI estimation on high-dim features is hard; use classifier-based bounds and report sensitivity.

- **Survival Reason:** Information-theoretic measurement of "global leakage" supplies the mechanism behind naive CLIP dense-readout failure plus a practical per-layer readout-selection instrument.
- **Major Risks:** Mutual-information estimation on high-dimensional features is fragile; leakage may correlate with but not cause dense failure.
- **Unresolved Questions:** Whether register tokens or dense-alignment fine-tuning reduce leakage; whether leakage explains the decoder behavior hypothesized in 0078.
- **Required Experiments:** Classifier-based MI bounds for patch-token vs global-label and vs local-content across layers and ≥3 VLMs; leakage-ratio correlation with per-layer zero-shot segmentation; probe-family sensitivity analysis.
- **Reviewer Opinion:** The most mechanistic idea in C3; would anchor a family of VLM-dense papers and directly feeds 0078.

### IDEA-C-0067
- **One-sentence idea:** Treat class-name prompt sensitivity as measurement noise and re-estimate open-vocab segmentation leaderboards with prompt-averaged confidence intervals.
- **Problem:** Zero-shot dense results swing wildly with synonym choice ("sofa" vs "couch"), yet leaderboards report single-prompt point estimates.
- **Core Hypothesis (falsifiable):** Across published open-vocab segmenters, the within-method variance across reasonable prompt paraphrases exceeds the between-method differences for a substantial fraction of benchmark class pairs — meaning many reported rankings are prompt artifacts.
- **Why Important:** If rankings are noise, the field's progress narrative in open-vocab dense prediction needs statistical repair.
- **Why Possibly Novel:** Prompt sensitivity is known for classification; a formal noise-model treatment of *dense benchmark rankings* is absent.
- **Minimal Experiment:** 5 public methods × 20 prompt paraphrase sets × 2 benchmarks; variance decomposition of scores; report which claimed gaps survive.
- **Main Risk:** Choosing "reasonable paraphrases" is subjective; use multiple paraphrase sources including model-generated and human ones.

- **Survival Reason:** Treats class-name prompt sensitivity as measurement noise and re-estimates open-vocab leaderboards with confidence intervals — cheap, decisive, field-hygiene work.
- **Major Risks:** The "reasonable paraphrase" set is contestable; conclusions may be benchmark-specific.
- **Unresolved Questions:** How much of reported open-vocab progress survives prompt-marginalized evaluation; whether benchmarks should mandate prompt-averaged reporting.
- **Required Experiments:** 5 public methods × 20 paraphrase sets (human + model-generated) × 2 benchmarks; hierarchical variance decomposition; surviving-gap table.
- **Reviewer Opinion:** Inference-only with high venue potential as an evaluation paper; complements 0094 and 0340 in the measurement-repair program.

### IDEA-C-0072
- **One-sentence idea:** Build a text-only baseline audit for referring segmentation: how often is the mask predictable without looking at the image?
- **Problem:** Referring-expression datasets contain language priors ("the sky", "the left man") that let models score without genuine cross-modal grounding.
- **Core Hypothesis (falsifiable):** A model given only the text (plus dataset-level mask statistics) achieves a nontrivial fraction of reported referring-segmentation performance, and per-sample text-predictability correlates with where published models succeed — indicating prior exploitation rather than grounding.
- **Why Important:** Cleans the evidence base for a subfield whose central claim is cross-modal grounding.
- **Why Possibly Novel:** Language-prior audits exist for VQA; the dense/referring-mask analogue with per-sample analysis is not established.
- **Minimal Experiment:** Train text→mask-prior model on referring benchmarks; stratify published-model performance by text-predictability; report the grounded remainder.
- **Main Risk:** Defining the text-only baseline's allowed knowledge (image size? typical layouts?) needs care to avoid straw-manning either direction.

- **Survival Reason:** PROTECTED (high-risk/high-reward). The text-only referring-segmentation baseline audits the central grounding claim of an entire subfield; the VQA language-prior audit transplanted to dense prediction, overdue and cheap.
- **Major Risks:** Defining the baseline's allowed knowledge (image size, typical layouts) risks straw-manning in either direction; per-sample predictability analysis requires care.
- **Unresolved Questions:** The honest "grounded remainder" of current SOTA; whether findings transfer to medical referring tasks where priors are even stronger.
- **Required Experiments:** Text→mask-prior model trained on RefCOCO-family benchmarks; stratification of ≥3 published models' performance by text-predictability; grounded-remainder estimation with several baseline-knowledge tiers.
- **Reviewer Opinion:** Potentially deflationary for a hot area; the tiered-baseline design defuses the straw-man objection. Protect and run early.

### IDEA-C-0076
- **One-sentence idea:** Show that report-supervised medical VLMs align to reporting style — including pervasive negations — and that negation breaks their dense grounding.
- **Problem:** Radiology reports frequently assert absence ("no consolidation"); contrastive alignment on such text may create pathological associations between absence-words and normal anatomy.
- **Core Hypothesis (falsifiable):** In report-pretrained medical VLMs, similarity maps for "no X" prompts activate the same regions as "X" prompts (negation blindness), and the degree of blindness predicts failure of the model's pseudo-mask quality on pathology classes with high negation frequency in reports.
- **Why Important:** Negation is not an edge case in clinical text; if it corrupts grounding, medical VLM supervision needs restructuring.
- **Why Possibly Novel:** Negation blindness is known for general CLIP retrieval; its dense/grounding consequence in *medical* report-trained models, tied to report negation statistics, is unexamined.
- **Minimal Experiment:** Compare similarity maps for affirmed vs negated findings on labeled CXR data; correlate per-class blindness with negation frequency in public report corpora.
- **Main Risk:** Public report-image data is limited; MIMIC-CXR class coverage constrains generality.

- **Survival Reason:** Negation blindness in report-trained medical VLM dense grounding, tied quantitatively to report negation statistics — clinically pressing, measurable, and specific to the medical supervision pipeline.
- **Major Risks:** Public report-image data limits coverage (MIMIC-CXR classes); similarity-map metrics may miss subtler grounding failures.
- **Unresolved Questions:** Whether a small hard-negative fine-tune repairs dense grounding and at what data cost (absorb eliminated 0115's fix-cost curve); whether blindness scales with model size.
- **Required Experiments:** Affirmed-vs-negated similarity maps on labeled CXR data; per-class blindness vs corpus negation frequency; hard-negative fine-tuning arm at 1k/10k/100k pairs with side-effect battery.
- **Reviewer Opinion:** Keep as the medical-dense anchor of the negation theme; merge 0115's minimal-fix framing into it at the next stage.

### IDEA-C-0078
- **One-sentence idea:** Test whether decoders trained on frozen CLIP features learn to *invert* the alignment direction — actively removing text-aligned components to recover spatial detail.
- **Problem:** Frozen-VLM segmentation pipelines work better than raw similarity readouts; what the trained decoder actually does to the features is unknown.
- **Core Hypothesis (falsifiable):** The decoder's learned input transformation systematically down-projects the directions most aligned with text embeddings (measurable via projection analysis), and constraining the decoder to preserve those directions reproduces the raw-readout failures — proving decoders succeed by undoing alignment.
- **Why Important:** If decoders fight the alignment, the pipeline is self-contradictory, motivating feature surgery before decoding rather than heavier decoders.
- **Why Possibly Novel:** Mechanistic analysis of what dense decoders do to frozen VLM features has not been reported.
- **Minimal Experiment:** Train linear/light decoders on frozen CLIP; compute alignment of suppressed vs amplified subspaces with text-embedding span; run the constrained-decoder control.
- **Main Risk:** Subspace analyses can be basis-dependent; use multiple decompositions (PCA, CCA against text space).

- **Survival Reason:** PROTECTED (high-risk/high-reward). "Decoders succeed by undoing alignment" would expose the standard frozen-CLIP segmentation pipeline as self-contradictory — a mechanistic result with large design consequences.
- **Major Risks:** Subspace analyses are basis-dependent; the effect may be small, decoder-specific, or an artifact of the decomposition choice.
- **Unresolved Questions:** Whether feature surgery before decoding beats heavier decoders; whether the effect strength tracks alignment strength across checkpoints (connects to 0061).
- **Required Experiments:** Linear/light decoders on frozen CLIP; projection analysis of suppressed vs amplified subspaces against the text-embedding span; constrained-decoder control reproducing raw-readout failures; ≥2 decompositions (PCA, CCA).
- **Reviewer Opinion:** Real risk of a mushy outcome, but the constrained-decoder control makes it falsifiable; the narrative payoff justifies protection.

---

## C4. Prompt learning pathologies — 5 kept

### IDEA-C-0091
- **One-sentence idea:** Show that learned soft prompts are dataset fingerprints: the training dataset is identifiable from the prompt vector alone.
- **Problem:** CoOp-style prompts are interpreted as "task semantics", but they may primarily encode dataset-specific statistics (style, class priors, acquisition quirks).
- **Core Hypothesis (falsifiable):** A classifier over learned prompt vectors identifies the source dataset with high accuracy even across matched-task datasets (same classes, different collection), and the fingerprint strength anti-correlates with the prompt's cross-dataset transfer.
- **Why Important:** If prompts are fingerprints, prompt reuse across sites is unsafe and reported "generalizable prompts" claims need re-reading.
- **Why Possibly Novel:** Prompts have been probed for word-similarity, not for dataset-identity information content.
- **Minimal Experiment:** Train prompts on 6 dataset pairs with shared label spaces; train dataset-ID classifier on prompt vectors; correlate ID-accuracy with transfer drop.
- **Main Risk:** Few matched-task dataset pairs exist; may need constructed splits with documented differences.

- **Survival Reason:** PROTECTED (high-risk/high-reward). Prompts as dataset fingerprints reframes prompt reuse as a safety/leakage issue and prompt vectors as auditable artifacts — a genuinely new lens on a ubiquitous method.
- **Major Risks:** Matched-task dataset pairs are scarce; the fingerprint may be trivially class-prior-driven, requiring a prior-ablated control.
- **Unresolved Questions:** What information carries the fingerprint (style vs priors vs acquisition statistics); whether fingerprint strength quantitatively predicts transfer failure.
- **Required Experiments:** Prompts trained on 6 matched-task dataset pairs; dataset-ID classifier on prompt vectors; ID-accuracy vs transfer-drop correlation; prior-ablation control (compare against bias-only adjusted zero-shot).
- **Reviewer Opinion:** Also carries a privacy/membership-inference angle that could support a second paper; protect despite the data-pairing burden.

### IDEA-C-0094
- **One-sentence idea:** Run a seed-variance meta-analysis of prompt-learning literature: how many reported gains exceed seed noise?
- **Problem:** Prompt tuning has few parameters but high optimization variance; papers report single-seed or best-seed numbers on few-shot splits.
- **Core Hypothesis (falsifiable):** Re-running representative prompt-learning methods with ≥10 seeds and multiple few-shot draws shows that a substantial fraction of published between-method gaps fall inside the joint seed+split noise band.
- **Why Important:** If method rankings are noise, the subfield's guidance to practitioners is unreliable.
- **Why Possibly Novel:** Rigorous variance accounting (seed × split × hyperparameter) for the prompt-learning benchmark canon has not been published.
- **Minimal Experiment:** 5 canonical methods × 11 datasets × 10 seeds × 5 few-shot draws with authors' code; hierarchical variance decomposition.
- **Main Risk:** Compute-heavy though individually cheap runs; prioritize the most-cited comparisons.

- **Survival Reason:** Seed/split variance meta-analysis of the prompt-learning canon; measurement repair with immediate field-wide consequences for how few-shot claims are read.
- **Major Risks:** Compute accumulates across 5×11×10×5 runs; author-code reproduction friction may bias which methods get included.
- **Unresolved Questions:** Which canonical claims survive; whether variance itself is predictable from shots and dataset size (enabling cheap power analysis).
- **Required Experiments:** 5 canonical methods × 11 datasets × 10 seeds × 5 few-shot draws with authors' code; hierarchical variance decomposition (seed/split/hyperparameter); surviving-gap and variance-reference tables.
- **Reviewer Opinion:** The prompt-learning field is overdue for this; pairs with 0067 (prompt noise) and eliminated 0110 (protocol leakage) as one evaluation-integrity program.

### IDEA-C-0095
- **One-sentence idea:** Test whether the celebrated base-new class trade-off in prompt learning is a regularization artifact rather than a generalization property.
- **Problem:** Base-class gains vs new-class drops are theorized as overfitting-to-seen-classes; but simple regularization knobs (early stopping, weight decay to zero-shot) may trace the same trade-off curve.
- **Core Hypothesis (falsifiable):** The base-new frontier of specialized methods is matched by vanilla CoOp with a single regularization strength swept — implying published "solutions" move along, not above, an easily accessible curve.
- **Why Important:** Deflates or validates a large branch of prompt-learning method development with one controlled sweep.
- **Why Possibly Novel:** Frontier-equivalence testing (methods vs one-knob baseline) has not been performed for base-new claims.
- **Minimal Experiment:** Sweep regularization-to-zero-shot strength for vanilla prompts; overlay published methods' (base, new) points against the swept frontier.
- **Main Risk:** Some methods may genuinely exceed the frontier; the experiment is decisive either way but must tune the baseline honestly.

- **Survival Reason:** The one-knob frontier-equivalence test could deflate an entire branch of base-new prompt methods; decisive in either direction and cheap relative to its consequence.
- **Major Risks:** "Honest tuning" of the baseline is disputable; some methods may genuinely exceed the frontier, yielding a partial rather than clean result.
- **Unresolved Questions:** Which regularizer family traces the frontier best; whether the result holds beyond CLIP-scale encoders and into dense tasks.
- **Required Experiments:** Regularization-to-zero-shot strength sweep for vanilla CoOp; overlay published (base, new) operating points from ≥8 methods; pre-registered tuning protocol; frontier-exceedance statistics.
- **Reviewer Opinion:** Sharply framed and likely controversial — exactly what Stage 2 should be protecting. Publish with the swept frontier as a reusable reference curve.

### IDEA-C-0101
- **One-sentence idea:** Test whether test-time prompt tuning is functionally equivalent to entropy minimization plus temperature calibration.
- **Problem:** TPT-style methods report zero-shot gains, but their objective (confidence maximization over augmentations) may reduce to well-known calibration adjustments.
- **Core Hypothesis (falsifiable):** A closed-form per-sample temperature/prior adjustment fitted to the same augmentation ensemble reproduces the bulk of TPT's gains at a fraction of compute; TPT's residual advantage concentrates on samples where it changes the argmax, which are disproportionately errors.
- **Why Important:** If true, an expensive test-time optimization is replaceable by an analytic step — and its residual behavior is harmful.
- **Why Possibly Novel:** The equivalence-and-residual decomposition of TPT has not been reported.
- **Minimal Experiment:** Reimplement TPT; compare with augmentation-ensemble + temperature/prior fitting; analyze argmax-changing samples separately.
- **Main Risk:** Multiple TPT variants exist; test the 2–3 most-cited to support generality.

- **Survival Reason:** Reduces test-time prompt tuning to closed-form calibration if the hypothesis holds; the argmax-changing residual analysis doubles as a harm probe for an expensive deployed technique.
- **Major Risks:** TPT variants differ enough that equivalence may hold for some and not others; augmentation-ensemble equivalence may be partial.
- **Unresolved Questions:** Compute-matched comparison against simple ensembling; whether residual harm concentrates on OOD samples specifically.
- **Required Experiments:** Reimplement 2–3 most-cited TPT variants; fit per-sample temperature/prior adjustments on identical augmentation ensembles; gain decomposition; separate analysis of argmax-changing cases.
- **Reviewer Opinion:** Mechanism-vs-artifact adjudication at its best, with modest compute; a clean example of the batch's deflationary strength.

### IDEA-C-0113
- **One-sentence idea:** Document "prompt collapse": class prompts converging toward each other during long training, silently destroying fine-grained discrimination.
- **Problem:** Prompt training monitors accuracy, not the geometry of the prompt set; converging prompts would degrade exactly the confusable classes while aggregate metrics look stable.
- **Core Hypothesis (falsifiable):** Pairwise similarity among class-prompt embeddings increases with training beyond a task-dependent point, and its rise predicts (precedes) the decline of confusable-pair accuracy — establishing collapse as a monitorable pathology with an early-warning signal.
- **Why Important:** Adds a cheap training-time diagnostic preventing silent fine-grained degradation.
- **Why Possibly Novel:** Prompt-set geometry dynamics during training have not been tracked or linked to per-pair outcomes.
- **Minimal Experiment:** Long prompt training on fine-grained datasets; log prompt-similarity trajectories and per-pair accuracy; test the lead-lag relation and a similarity-penalty fix.
- **Main Risk:** Collapse may be benign reparameterization in some encoders; the per-pair accuracy linkage is the decisive test.

- **Survival Reason:** PROTECTED (counter-intuitive). Prompt collapse as a monitorable training pathology with a lead-lag early-warning signal; nobody currently tracks prompt-set geometry during training.
- **Major Risks:** Collapse may be benign reparameterization in some encoders; the long-training regime studied may be unrepresentative of common practice.
- **Unresolved Questions:** Whether a similarity penalty prevents collapse without hurting aggregate accuracy; whether collapse also occurs in dense-task prompt tuning.
- **Required Experiments:** Long prompt training on fine-grained datasets; prompt-similarity trajectories with per-confusable-pair accuracy; lead-lag statistical test; similarity-penalty intervention arm.
- **Reviewer Opinion:** A small, crisp paper; the lead-lag analysis is the make-or-break evidence and is cheap to obtain.

---

## C5. Weak/semi/self-supervised segmentation: scientific gaps — 6 kept

### IDEA-C-0121
- **One-sentence idea:** Test whether consistency regularization works via implicit boundary smoothing rather than the cluster assumption it cites.
- **Problem:** The mechanism of consistency training in segmentation is asserted (decision boundaries in low-density regions) but never separated from a mundane alternative: averaging over perturbations smooths predicted boundaries.
- **Core Hypothesis (falsifiable):** Replacing consistency training with explicit boundary-smoothing regularization (no unlabeled data) reproduces a large fraction of its gains on standard benchmarks; the residual unlabeled-data benefit concentrates on images whose appearance is far from labeled examples — separating smoothing from information gain.
- **Why Important:** Correct mechanism changes what unlabeled data is worth collecting and how methods should be built.
- **Why Possibly Novel:** The smoothing-equivalence control experiment has not been run for dense consistency methods.
- **Minimal Experiment:** Match consistency methods against label-only smoothing controls; stratify residual gains by appearance distance to labeled set.
- **Main Risk:** Designing a fair smoothing control requires care (strength matching via boundary-jitter statistics).

- **Survival Reason:** The smoothing-equivalence control for consistency regularization is a first-order mechanism question for all of semi-supervised segmentation — the control experiment is conspicuously absent from the literature.
- **Major Risks:** Fair smoothing-strength matching is delicate; residual-gain stratification needs a defensible appearance-distance metric.
- **Unresolved Questions:** Whether the residual unlabeled-data benefit concentrates on images far from the labeled set; whether conclusions hold for the strongest modern methods.
- **Required Experiments:** Consistency methods vs label-only boundary-smoothing controls on 3 benchmarks; strength matching via boundary-jitter statistics; residual-gain stratification by appearance distance to labeled data.
- **Reviewer Opinion:** Could reset how the field explains its own gains; the cluster-assumption story has never faced this mundane alternative.

### IDEA-C-0124
- **One-sentence idea:** Show that self-training converges toward a single annotator style, collapsing the inter-rater variance present in the initial labels.
- **Problem:** Pseudo-labels are generated by a model trained on multi-rater-influenced data; iterating may systematically homogenize label style, losing calibrated ambiguity.
- **Core Hypothesis (falsifiable):** Across self-training rounds, the distributional spread of predictions on ambiguous regions (where raters disagree) shrinks monotonically toward one mode, and the final model's rater-likelihood is high for one rater and low for others — measurable style collapse absent in the supervised baseline.
- **Why Important:** Semi-supervised pipelines may silently discard exactly the ambiguity information medicine needs to keep.
- **Why Possibly Novel:** Interaction between self-training dynamics and multi-rater label structure is unstudied.
- **Minimal Experiment:** Multi-rater dataset; run self-training; track per-round prediction spread on disagreement regions and per-rater likelihoods.
- **Main Risk:** Requires multi-rater ground truth; several public sets (prostate, lung nodule) qualify.

- **Survival Reason:** PROTECTED (high-risk/high-reward). Self-training as an ambiguity destroyer connects semi-supervised practice to the multi-rater agenda (C9); medically, the discarded distributional signal is exactly what risk-aware deployment needs.
- **Major Risks:** Requires multi-rater data (LIDC, prostate collections); style-collapse metrics must be disentangled from mere prediction sharpening.
- **Unresolved Questions:** Which loop component drives collapse (argmax pseudo-labels vs confidence filtering); whether distributional pseudo-labels prevent it at acceptable cost.
- **Required Experiments:** Self-training on LIDC-IDRI/QUBIQ-class multi-rater sets; per-round prediction spread on disagreement regions; per-rater likelihood trajectories; distributional-pseudo-label intervention arm.
- **Reviewer Opinion:** Bridges two literatures cleanly; strong MICCAI-to-NeurIPS range. Protect for its data dependence, not its science.

### IDEA-C-0127
- **One-sentence idea:** Show that the "low-data regime" simulated by subsampling big datasets misrepresents true small-cohort learning, breaking method rankings.
- **Problem:** Papers simulate scarcity as 5% of a large dataset — preserving class coverage and appearance diversity that genuine small cohorts lack.
- **Core Hypothesis (falsifiable):** Method rankings established on subsampled-scarcity benchmarks reorder significantly on true small cohorts (single-site, consecutive patients), because subsampling preserves diversity that specific methods exploit — measurable as a ranking-correlation breakdown.
- **Why Important:** The field's low-data conclusions guide exactly the users (small clinics, rare diseases) that the evaluation misrepresents.
- **Why Possibly Novel:** Direct subsampled-vs-genuine scarcity comparisons with ranking analysis are missing.
- **Minimal Experiment:** Match label counts between subsampled large datasets and genuinely small cohorts; run 5 methods; compare rankings and interaction structure.
- **Main Risk:** Genuine small cohorts differ in many ways; use several to average over idiosyncrasies.

- **Survival Reason:** The subsampled-scarcity vs genuine-small-cohort audit touches every low-data claim in medical segmentation; if rankings reorder, the field has been optimizing for the wrong users.
- **Major Risks:** Genuine small cohorts differ in many uncontrolled ways; ranking instability may be hard to attribute to a specific diversity dimension.
- **Unresolved Questions:** Which diversity dimension (class coverage, appearance modes, patient count) drives the mismatch; whether subsampling protocols can be repaired to simulate scarcity honestly.
- **Required Experiments:** Label-count-matched comparisons between subsampled large datasets and several genuine single-site cohorts; 5 methods; ranking-correlation and interaction analysis; diversity-dimension ablations.
- **Reviewer Opinion:** Dataset-adjacent (flagged for merge with the dataset-failure batch) but the method-ranking consequence is distinct enough to keep here.

### IDEA-C-0132
- **One-sentence idea:** Quantify the positional shortcut in pixel-level contrastive SSL on spatially registered medical images.
- **Problem:** Medical volumes are roughly aligned; pixel contrastive objectives can minimize loss by encoding position rather than appearance semantics.
- **Core Hypothesis (falsifiable):** Features from pixel-contrastive SSL on registered data predict spatial coordinates far better than appearance-matched controls, and their downstream transfer drops disproportionately on unregistered/abnormal cases — with registration-breaking augmentation closing both gaps.
- **Why Important:** A silent shortcut in the standard recipe for medical dense SSL would explain fragile transfer to pathological anatomy.
- **Why Possibly Novel:** The registration-induced positional shortcut has not been isolated or dosed.
- **Minimal Experiment:** Train pixel-contrastive SSL with/without registration-breaking transforms; probe features for coordinates; compare transfer on aligned vs distorted anatomy.
- **Main Risk:** Position and anatomy are inherently correlated; the dose-response design (graded registration breaking) addresses this.

- **Survival Reason:** The positional shortcut in pixel-contrastive SSL on registered medical images is a plausible silent failure of the standard recipe, and the graded registration-breaking design gives it a proper dose-response test.
- **Major Risks:** Position and anatomy are inherently correlated, so complete disentanglement is impossible; registration-breaking augmentation may help for unrelated reasons.
- **Unresolved Questions:** How much published medical-SSL transfer is position-driven; whether the shortcut explains fragility on pathological/distorted anatomy.
- **Required Experiments:** Pixel-contrastive SSL with graded registration-breaking transforms; coordinate-prediction probes; transfer evaluation on aligned vs distorted/pathological cases; dose-response curve linking the three.
- **Reviewer Opinion:** The dose-response design elevates this above a one-off gotcha; results generalize to any spatially registered SSL corpus.

### IDEA-C-0137
- **One-sentence idea:** Show that "barely-supervised" (one labeled volume) segmentation success is carried by implicit registration, and collapses on unregistered anatomy.
- **Problem:** Single-volume supervision methods report strong results on well-aligned datasets (cardiac, abdominal atlases); the role of implicit spatial alignment is unacknowledged.
- **Core Hypothesis (falsifiable):** Performance of barely-supervised methods degrades toward failure as test-time anatomical alignment with the labeled volume decreases (measured by registration residual), while many-label baselines degrade far less — alignment, not method ingenuity, is the active ingredient.
- **Why Important:** Corrects the perceived readiness of extreme-low-label methods for pathological, poorly aligned real-world anatomy.
- **Why Possibly Novel:** Alignment-stratified evaluation of barely-supervised claims has not been reported.
- **Minimal Experiment:** Stratify test cases by registration residual to the labeled volume; compare degradation slopes across supervision levels.
- **Main Risk:** Registration residual is imperfectly measurable on pathological cases — use multiple registration methods.

- **Survival Reason:** Alignment-stratified evaluation of barely-supervised segmentation directly tests whether implicit registration, not method ingenuity, is the active ingredient — a sharp, checkable deflation.
- **Major Risks:** Registration residual is imperfectly measurable on pathological cases; degradation slopes may confound with case difficulty.
- **Unresolved Questions:** Whether popular one-shot methods fail outright on unregistered anatomy; what alignment threshold defines each method's operating envelope.
- **Required Experiments:** Stratify test cases by registration residual to the labeled volume (2 independent registration methods); compare degradation slopes across supervision levels; dedicated pathological-anatomy arm.
- **Reviewer Opinion:** Directly actionable for anyone considering extreme-low-label methods; honest scoping of a fashionable capability.

### IDEA-C-0143
- **One-sentence idea:** Test whether label-efficient methods change the slope or only the intercept of the labeled-data learning curve.
- **Problem:** Methods claim to "reduce annotation needs by N×", implying slope changes, but most evaluations report isolated points, not curves.
- **Core Hypothesis (falsifiable):** Fitting power-law learning curves across label fractions shows that semi/weak/self-supervised methods shift the intercept (constant multiplier) but leave the exponent statistically unchanged — implying their advantage shrinks at scale and "N× savings" claims are point-estimate artifacts.
- **Why Important:** The slope-vs-intercept distinction determines whether label-efficiency methods matter for well-funded projects or only tiny ones.
- **Why Possibly Novel:** Learning-curve-exponent analysis is standard in scaling literature but unapplied to label-efficiency claims in segmentation.
- **Minimal Experiment:** 4 methods × 6 label fractions × 3 datasets; fit curves; test exponent equality statistically.
- **Main Risk:** Curve fitting needs many points at low fractions where variance is high; use repeated draws.

- **Survival Reason:** The slope-vs-intercept learning-curve analysis converts "N× annotation savings" marketing into a testable scaling claim — one of the batch's best methodological ideas with consequences for funding-level decisions.
- **Major Risks:** Exponent estimation needs many low-fraction points where variance is high; the power-law form may not fit all regimes.
- **Unresolved Questions:** Whether any method family genuinely changes the exponent (and by what mechanism); whether the result extends to detection and classification.
- **Required Experiments:** 4 methods × 6 label fractions × 3 datasets with repeated draws; power-law fits with statistical exponent-equality tests; functional-form sensitivity analysis.
- **Reviewer Opinion:** Quietly devastating if intercept-only turns out to be the norm; belongs in the batch's top tier.

---

## C6. Medical vision foundation models: what they still cannot do — 7 kept

### IDEA-C-0149
- **One-sentence idea:** Run a clinical-safety probe for laterality: can medical foundation models reliably represent left vs right?
- **Problem:** Wrong-side errors are "never events" clinically; whether FM representations distinguish laterality (beyond image-flip statistics) is unverified.
- **Core Hypothesis (falsifiable):** Probes for anatomical laterality on FM features perform well on canonical orientations but collapse under flipped or marker-removed images — the models encode orientation conventions, not laterality — measurable as a flip-consistency failure rate.
- **Why Important:** Laterality is a minimal bar for clinical text generation, retrieval, and reporting built on FM features.
- **Why Possibly Novel:** Laterality has not been treated as a standalone capability audit for medical FMs.
- **Minimal Experiment:** Laterality probes on {canonical, flipped, marker-ablated} images across 4 FMs; report consistency matrices.
- **Main Risk:** Datasets embed laterality markers; careful ablation of burned-in annotations is required.

- **Survival Reason:** Laterality as a minimal clinical-safety capability audit: wrong-side errors are never-events, the probes are cheap, and no FM audit currently isolates this.
- **Major Risks:** Burned-in laterality markers confound; probe success on features may not imply downstream-task safety.
- **Unresolved Questions:** Whether FMs encode orientation convention rather than true laterality; whether text supervision worsens the failure.
- **Required Experiments:** Laterality probes on {canonical, flipped, marker-ablated} images across 4 FMs; flip-consistency matrices; validation of the marker-ablation pipeline itself.
- **Reviewer Opinion:** Small paper, big clinical footnote; likely to become a standard audit item if published first.

### IDEA-C-0150
- **One-sentence idea:** Measure the pairwise-reasoning gap: FMs cannot compare two scans (change detection) even when they analyze each well individually.
- **Problem:** Longitudinal comparison is a core radiology act; FM architectures and pretraining see single images, and their comparison ability is untested.
- **Core Hypothesis (falsifiable):** On controlled change-detection tasks (synthetic and registered-pair real data), FM-based pipelines perform near chance for changes below a large magnitude, while trivially trained siamese baselines succeed — a structural, not scale, deficiency.
- **Why Important:** Defines a capability boundary directly blocking the most common clinical use case (interval change).
- **Why Possibly Novel:** Change-detection audits of medical FMs with controlled magnitude ladders do not exist.
- **Minimal Experiment:** Construct change ladders (lesion growth steps) on registered pairs; evaluate FM zero/few-shot vs small siamese supervised baseline.
- **Main Risk:** Registration errors mimic change; use synthetic insertions with verified realism as the controlled arm.

- **Survival Reason:** Change detection (pairwise reasoning) is the modal clinical act and a plausibly structural blind spot of single-image FMs; the change-magnitude-ladder design is clean and decisive.
- **Major Risks:** Registration errors mimic true change; synthetic insertions must pass realism checks to carry the controlled arm.
- **Unresolved Questions:** Whether the deficit is representational or interface-level (could paired-input prompting fix it); how it scales with model size.
- **Required Experiments:** Change ladders (lesion growth steps) on registered pairs, synthetic and natural; FM zero/few-shot vs small trained siamese baselines; error decomposition by change magnitude.
- **Reviewer Opinion:** Defines a capability boundary that FM vendors implicitly claim to have crossed; strong impact either way.

### IDEA-C-0151
- **One-sentence idea:** Test whether FMs lost metric scale: physical-size estimation fails because pretraining pipelines discard pixel spacing.
- **Problem:** Clinical decisions hinge on millimeters, but FM preprocessing resizes images, destroying the mapping between pixels and physical units.
- **Core Hypothesis (falsifiable):** FM features cannot support size estimation beyond relative-within-image judgments (probes fail to predict physical size across images with varying spacing), and injecting spacing as a side input at probe time restores accuracy — the information is destroyed, not unused.
- **Why Important:** Measurement is half of radiology; a metric-blind foundation cannot support it.
- **Why Possibly Novel:** Metric-scale capability audits for medical FMs are absent.
- **Minimal Experiment:** Physical-size probes across mixed-spacing datasets with/without spacing injection; compare against spacing-aware baselines.
- **Main Risk:** Some anatomy provides internal scale references; control by cross-anatomy evaluation.

- **Survival Reason:** Metric-scale destruction (pixel spacing discarded by preprocessing) is a crisp information-availability audit with a definitive spacing-injection test; measurement is half of radiology.
- **Major Risks:** Internal anatomical scale references partially rescue size estimation, so cross-anatomy controls are essential.
- **Unresolved Questions:** Which pipelines preserve spacing information; whether spacing is genuinely destroyed or merely unused (the injection test adjudicates).
- **Required Experiments:** Physical-size probes across mixed-spacing datasets with and without spacing injection at probe time; cross-anatomy evaluation; audit of common FM preprocessing stacks.
- **Reviewer Opinion:** Almost embarrassingly simple, which is exactly why it will be cited; the injection test is the elegant part.

### IDEA-C-0162
- **One-sentence idea:** Test whether report-supervised FMs learn the distribution of *reported* findings, systematically missing unreported incidentals.
- **Problem:** Reports document what radiologists chose to mention; findings outside the clinical question (incidentals) are under-reported, biasing FM supervision.
- **Core Hypothesis (falsifiable):** On images with expert re-reads that recover unreported findings, report-trained FMs detect reported-type findings well but miss unreported-type ones at rates predicted by reporting-frequency statistics — the model inherits the reporting policy, not the visual truth.
- **Why Important:** Incidental findings are a major clinical value proposition for AI; an FM structurally blind to them fails the pitch.
- **Why Possibly Novel:** The reported-vs-present distinction has not been operationalized as an FM evaluation axis.
- **Minimal Experiment:** Re-read a stratified image sample to establish present-but-unreported findings; measure FM sensitivity by reportedness stratum.
- **Main Risk:** Re-read cost; mitigate with targeted sampling where reporting gaps are known to concentrate.

- **Survival Reason:** PROTECTED (high-risk/high-reward). "Models learn the reporting policy, not the visual truth" is a supervision-bias account of FM blind spots that only a re-read study can verify — expensive, but no cheaper design answers it.
- **Major Risks:** Expert re-reads are costly; reportedness strata confound with finding difficulty and prevalence.
- **Unresolved Questions:** What fraction of incidental findings are structurally invisible to report-trained FMs; whether incidental-focused supervision can patch the gap.
- **Required Experiments:** Stratified re-read study establishing present-but-unreported findings; FM sensitivity by reportedness stratum across ≥2 report-trained models; prevalence- and difficulty-adjusted analysis.
- **Reviewer Opinion:** The single most consequential medical-FM hypothesis in the batch; protect the budget it needs.

### IDEA-C-0164
- **One-sentence idea:** Determine the effective resolution ceiling of medical FMs: which subtle findings live below what the representation can carry?
- **Problem:** Micro-findings (microcalcifications, early interstitial change) may fall below FM effective spatial bandwidth after tokenization and pooling — the field lacks a frequency-resolved capability map.
- **Core Hypothesis (falsifiable):** FM feature sensitivity to controlled high-frequency perturbations cuts off at a measurable spatial frequency per model, and clinical findings whose discriminative energy lies above the cutoff show near-chance FM performance regardless of fine-tuning — a physics-style capability bound.
- **Why Important:** Tells users which clinical problems FMs cannot address at any data budget, before they try.
- **Why Possibly Novel:** Frequency-response characterization of medical FM representations is not in the literature.
- **Minimal Experiment:** Bandpass perturbation sensitivity analysis per FM; align finding types by discriminative-frequency content; test the predicted performance cliff.
- **Main Risk:** Fine-tuning may partially reopen bandwidth; test the bound both frozen and fine-tuned.

- **Survival Reason:** A frequency-response capability bound for medical FMs — a physics-style spec sheet telling users which findings are unreachable at any fine-tuning budget.
- **Major Risks:** Fine-tuning may partially reopen effective bandwidth; mapping clinical findings to discriminative frequency content is nontrivial.
- **Unresolved Questions:** Whether cutoffs are tokenizer-determined (connects to 0264) or emergent from training; whether cutoffs retrodict published per-finding results.
- **Required Experiments:** Bandpass perturbation sensitivity analysis per FM; alignment of finding types by discriminative-frequency content; frozen vs fine-tuned bound comparison.
- **Reviewer Opinion:** Elegant bridge between signal processing and FM evaluation; forms a natural trilogy with 0264 and 0206.

### IDEA-C-0173
- **One-sentence idea:** Measure salience suppression: FMs detect the most prominent lesion and systematically under-report additional ones.
- **Problem:** Multi-lesion sensitivity is clinically vital (staging, metastasis counts); representation-level "winner-take-most" behavior would cap it independent of thresholds.
- **Core Hypothesis (falsifiable):** Per-lesion detection probability conditioned on lesion properties drops significantly when a more salient lesion is present in the same image (versus matched single-lesion controls), the suppression strengthens with salience gap, and it persists across detection thresholds — a representational, not calibration, effect.
- **Why Important:** Missing the second lesion changes staging and treatment; aggregate sensitivity metrics hide this failure specifically.
- **Why Possibly Novel:** Conditional (context-dependent) per-lesion sensitivity analysis for FMs has not been performed.
- **Minimal Experiment:** Multi-lesion datasets plus synthetic-insertion controls; estimate conditional detection curves vs salience gap.
- **Main Risk:** Natural multi-lesion images differ in many ways; synthetic insertion provides the controlled arm and must pass realism checks.

- **Survival Reason:** PROTECTED (high-risk/high-reward). Salience suppression — the presence of a prominent lesion lowering detection of others — is a representational multi-lesion failure invisible to aggregate sensitivity, with severe staging consequences if real.
- **Major Risks:** Natural multi-lesion images differ in many ways (severity confounds); synthetic-insertion realism; the effect could reduce to threshold artifacts despite the design.
- **Unresolved Questions:** Mechanism (attention competition, winner-take-most pooling); whether the effect worsens or improves with model scale.
- **Required Experiments:** Conditional per-lesion detection curves vs salience gap on natural multi-lesion data plus realism-checked synthetic insertions; threshold-sweep persistence check; attention-analysis arm for mechanism.
- **Reviewer Opinion:** The most clinically alarming hypothesis in C6; worth the construction effort and the protection.

### IDEA-C-0177
- **One-sentence idea:** Audit the clinical-metric gap: generalist FMs match specialists on Dice while losing on the measures clinicians consume (volumetry, diameters, boundary-derived indices).
- **Problem:** Benchmark parity on overlap metrics is taken as clinical parity; derived clinical measurements weight errors differently.
- **Core Hypothesis (falsifiable):** At matched Dice, FM segmentations produce significantly larger errors in derived clinical quantities (volumes, RECIST-style diameters, wall thickness) than specialist models, because FM errors are spatially structured (boundary-biased, inconsistency-prone) in ways Dice averages away.
- **Why Important:** Adoption decisions cite Dice parity; if clinical measures diverge, those decisions are misinformed at the last mile.
- **Why Possibly Novel:** Matched-Dice comparisons on derived clinical endpoints have not been systematically reported.
- **Minimal Experiment:** Dice-matched FM/specialist output pairs; compute clinical-measure error distributions; identify the responsible error structure.
- **Main Risk:** Dice matching requires careful pairing protocols; use multiple matching schemes.

- **Survival Reason:** Matched-Dice divergence on derived clinical measures attacks the exact evidence used in FM adoption decisions; the spatially-structured-error account is concrete and testable.
- **Major Risks:** Dice-matching protocols can be gamed or disputed; clinical-measure ground truth carries its own noise.
- **Unresolved Questions:** Which error structures (boundary bias, slice inconsistency) drive the endpoint divergence; whether post-hoc correction can close it.
- **Required Experiments:** Dice-matched FM/specialist output pairs across ≥3 tasks; volumetry/RECIST-diameter/wall-thickness error distributions; error-structure attribution using 0218-style bias fields; multiple matching protocols.
- **Reviewer Opinion:** Immediately quotable by regulators and skeptics alike; absorb eliminated 0232 (endpoint sensitivity maps) and 0168 (slice inconsistency) as supporting arms.

---

## C7. Object detection vs segmentation representation conflict — 6 kept

### IDEA-C-0179
- **One-sentence idea:** Measure the equivariance conflict: box regression rewards translation-sensitive features while mask prediction demands equivariance, and shared backbones must compromise.
- **Problem:** Multi-task det+seg models share features between objectives with opposing symmetry requirements; the compromise has never been measured as such.
- **Core Hypothesis (falsifiable):** Backbone feature equivariance (response shift under input shift) in jointly trained models sits between the values of detection-only and segmentation-only twins, and its position on that axis predicts which task the joint model sacrifices — equivariance is the contested resource.
- **Why Important:** Gives multi-task architecture design a measurable target instead of blind head balancing.
- **Why Possibly Novel:** Equivariance as the quantified locus of det/seg conflict has not been proposed or tested.
- **Minimal Experiment:** Train {det-only, seg-only, joint} triplets; measure layer-wise equivariance; correlate with per-task performance deltas.
- **Main Risk:** Equivariance metrics are implementation-sensitive; use two independent measures.

- **Survival Reason:** Equivariance as the contested resource in det+seg multi-task learning replaces loss-weight folklore with a measurable, designable quantity.
- **Major Risks:** Equivariance metrics are implementation-sensitive; the intermediate-value claim may hold only for specific architectures.
- **Unresolved Questions:** Whether equivariance is causal or a correlate of the trade-off; whether equivariance-targeted regularization can move the joint frontier.
- **Required Experiments:** {det-only, seg-only, joint} triplets on 2 architectures; layer-wise equivariance profiles with 2 independent metrics; correlation with per-task performance deltas; small regularization pilot.
- **Reviewer Opinion:** Gives the cluster's abstract "conflict" a number; the right anchor paper for the det/seg program.

### IDEA-C-0187
- **One-sentence idea:** Test the amodal-modal conflict: detectors learn amodal object extent while segmentation learns visible (modal) extent, corrupting shared features under occlusion.
- **Problem:** Boxes routinely cover occluded object parts, masks never do; joint training feeds features contradictory supervision precisely on occluded regions.
- **Core Hypothesis (falsifiable):** In occlusion-stratified evaluation, joint det+seg models show a characteristic error signature absent in single-task twins — mask over-extension into occluded regions and box under-coverage — with magnitude proportional to occlusion rate in training data.
- **Why Important:** Occlusion is pervasive; a supervision-contradiction account would explain a known but unattributed error pattern.
- **Why Possibly Novel:** The amodal-modal supervision contradiction has not been isolated experimentally.
- **Minimal Experiment:** Occlusion-controlled synthetic scenes + occlusion-annotated real data; compare error signatures across single vs joint training.
- **Main Risk:** Real occlusion annotation is scarce; the synthetic arm carries the controlled burden.

- **Survival Reason:** The amodal-modal supervision contradiction is a precise, occlusion-conditioned account of a known-but-unattributed error pattern, with a strong synthetic control arm.
- **Major Risks:** Real occlusion annotation is scarce; the predicted signature may be small relative to generic occlusion difficulty.
- **Unresolved Questions:** Whether the signature scales with training-data occlusion rate as predicted; whether amodal-mask supervision removes it.
- **Required Experiments:** Occlusion-controlled synthetic scenes plus occlusion-annotated real data; error-signature comparison across single-task vs joint models; training-data occlusion-rate manipulation.
- **Reviewer Opinion:** A sharp falsifiable prediction of the exact kind C7 needs; the contradiction framing is memorable and generative.

### IDEA-C-0190
- **One-sentence idea:** Show that competing instance-segmentation paradigms differ almost entirely on boundary pixels — and agree elsewhere.
- **Problem:** Paradigm debates (top-down vs bottom-up vs query-based) cite aggregate AP, obscuring where the paradigms actually behave differently.
- **Core Hypothesis (falsifiable):** Per-pixel agreement analysis shows inter-paradigm disagreement concentrates within a thin boundary band (with interior agreement near ceiling), implying paradigm choice is a boundary-handling choice — and boundary-band metrics reorder the paradigm ranking relative to AP.
- **Why Important:** Refocuses paradigm research on the pixels where paradigms differ, and questions AP as the deciding metric.
- **Why Possibly Novel:** Cross-paradigm spatial agreement decomposition has not been published.
- **Minimal Experiment:** Matched-AP model triplets; per-pixel agreement/disagreement maps; boundary-band metric re-ranking.
- **Main Risk:** Matched-AP triplets constrain model availability; train controlled versions where needed.

- **Survival Reason:** Per-pixel agreement decomposition showing paradigms differ almost only at boundaries would reframe paradigm debates as boundary-handling choices — cheap, clarifying, and probably true.
- **Major Risks:** Matched-AP triplets constrain model availability; the conclusion may vary by dataset density and object statistics.
- **Unresolved Questions:** Whether boundary-band metrics reorder paradigms consistently; where interior disagreements concentrate when they do exist.
- **Required Experiments:** Matched-AP model triplets on 2 benchmarks; per-pixel agreement/disagreement maps; boundary-band metric re-ranking; controlled retraining where public checkpoints are unavailable.
- **Reviewer Opinion:** Nobody has bothered to check this; the payoff-to-effort ratio is excellent.

### IDEA-C-0192
- **One-sentence idea:** Show mask-classification architectures secretly perform detection: their queries have box-like receptive behavior, inheriting detection's failure modes.
- **Problem:** Mask-classification (query-decoder) segmentation is presented as a departure from detection, but its queries may functionally re-implement boxes — importing crowding and duplicate pathologies unacknowledged.
- **Core Hypothesis (falsifiable):** Query attention footprints in mask-classification models are compact and box-approximable (high IoU between attention support and fitted boxes), and the models exhibit detection-typical failures (crowding misses, duplicate-merge errors) at rates predicted by the box-approximability score.
- **Why Important:** Correct lineage understanding predicts failure modes and prevents re-discovering detection fixes under new names.
- **Why Possibly Novel:** The functional-equivalence audit between queries and boxes has not been carried out.
- **Minimal Experiment:** Attention-footprint analysis on trained mask-classification models; failure-mode battery comparison against detectors and FCN-style models.
- **Main Risk:** Footprint compactness varies across layers/heads; aggregate carefully with per-query analysis.

- **Survival Reason:** PROTECTED (counter-intuitive). Mask-classification queries functioning as boxes explains inherited detection failures and prevents the field rediscovering detection fixes under new names — a lineage audit with predictive content.
- **Major Risks:** Attention-footprint compactness varies by layer and head; "box-approximable" needs a principled threshold to avoid circularity.
- **Unresolved Questions:** Whether box-approximability predicts crowding failures across model families; whether query redesigns (registers, deformable attention) break the equivalence.
- **Required Experiments:** Attention-footprint analysis on Mask2Former-class models; box-IoU of footprint supports; failure-mode battery vs detectors and FCN-style models; per-query stratified analysis.
- **Reviewer Opinion:** Durable conceptual contribution; even partial confirmation reshapes how the community reads mask-classification results.

### IDEA-C-0196
- **One-sentence idea:** Show that deriving lesion detection from segmentation post-processing destroys calibrated lesion-level confidence, and quantify the decision cost.
- **Problem:** Medical pipelines often segment then extract lesions by connected components, assigning ad-hoc confidences (max/mean pixel score) whose decision-theoretic quality is unexamined.
- **Core Hypothesis (falsifiable):** Lesion-level confidences derived from pixel scores are systematically miscalibrated (size-dependent bias: large lesions overconfident) and rank lesions worse than detection-native confidence at matched localization quality, measurably degrading downstream triage decisions at fixed review budgets.
- **Why Important:** Lesion-level operating points drive clinical review workflows; broken confidence silently corrupts them.
- **Why Possibly Novel:** The pixel-to-lesion confidence conversion problem is unformalized and unmeasured.
- **Minimal Experiment:** Compare lesion-confidence schemes (pixel-derived variants vs detection-native) on lesion benchmarks; calibration and triage-simulation analysis.
- **Main Risk:** Triage simulation assumptions matter; use several review-budget models.

- **Survival Reason:** The pixel-to-lesion confidence conversion problem is unformalized yet sits directly under clinical triage workflows; the size-dependent miscalibration hypothesis is specific and checkable.
- **Major Risks:** Triage simulations depend on assumed review budgets; detection-native baselines must be tuned fairly to avoid a hollow win.
- **Unresolved Questions:** Which conversion rule (size-normalized, evidence-pooled) is least miscalibrated; whether the size-dependent overconfidence generalizes across architectures.
- **Required Experiments:** Lesion benchmarks with confidence-scheme battery (max/mean pixel, size-normalized, detection-native); lesion-level calibration analysis; review-budget triage simulations across ≥3 models.
- **Reviewer Opinion:** Fills a real gap between segmentation outputs and clinical decision layers; practical enough to influence deployed pipelines quickly.

### IDEA-C-0204
- **One-sentence idea:** Test whether sliding-window 3D segmentation loses whole-object evidence that detection-style global context retains — on large lesions exceeding window size.
- **Problem:** 3D medical segmentation processes fixed windows for memory reasons; objects larger than the window are never seen whole, unlike in detection-style whole-volume approaches.
- **Core Hypothesis (falsifiable):** Segmentation error on lesions larger than the inference window grows discontinuously at the window-size threshold (controlling for lesion size effects below it), and providing coarse whole-volume context (low-res global pass) removes the discontinuity — proving a window-induced, not size-induced, failure.
- **Why Important:** Large lesions are high-stakes cases; a systematic window artifact on them would be an important hidden failure of standard pipelines.
- **Why Possibly Novel:** The window-threshold discontinuity has not been isolated from general size effects.
- **Minimal Experiment:** Size-stratified evaluation across window sizes on lesion datasets; regression-discontinuity analysis at window thresholds; global-context intervention.
- **Main Risk:** Large lesions are rare; pool across datasets and use synthetic enlargement as a supplementary arm.

---

- **Survival Reason:** The window-size discontinuity on large lesions is a hidden systematic failure of universal sliding-window practice, testable with a clean regression-discontinuity design and a cheap global-context intervention.
- **Major Risks:** Large lesions are rare, limiting statistical power; synthetic lesion enlargement must remain realistic; the discontinuity may smear across architectures.
- **Unresolved Questions:** Whether coarse whole-volume context fully removes the effect; whether other whole-object statistics (intensity landmarks) contribute (connects to eliminated 0313).
- **Required Experiments:** Size-stratified evaluation across inference window sizes; regression-discontinuity analysis at window thresholds; low-resolution global-context intervention; multi-dataset pooling plus a synthetic-enlargement arm.
- **Reviewer Opinion:** Practical and surgical; the RD framing gives it statistical credibility unusual for pipeline audits.

---

## C8. Boundary quality as a scientific problem — 7 kept

### IDEA-C-0205
- **One-sentence idea:** Decompose segmentation boundary error into image-aleatoric, annotation-protocol, and model-bias components with a reusable methodology.
- **Problem:** Boundary error is reported as one number, conflating irreducible image ambiguity, labeling convention, and actual model deficiency — making cross-paper progress claims uninterpretable.
- **Core Hypothesis (falsifiable):** The three components are separable using (a) multi-rater data for protocol variance, (b) local image-gradient statistics for aleatoric floor, and (c) residual for model bias — and across modern models, the model-bias component is a minority share of total boundary error on standard benchmarks.
- **Why Important:** If most boundary error is not model-caused, boundary-method research is optimizing an already-saturated component.
- **Why Possibly Novel:** Boundary-error budget accounting as a formal decomposition has not been established.
- **Minimal Experiment:** Multi-rater datasets; estimate the three components for 5 models; report error budgets and their stability.
- **Main Risk:** Component identifiability requires assumptions; validate with synthetic data where components are known.

- **Survival Reason:** The boundary error budget (image-aleatoric / annotation-protocol / model-bias) is the foundational accounting that the rest of C8 consumes; if model bias is a minority share, boundary-method research needs redirection.
- **Major Risks:** Component identifiability rests on modeling assumptions; multi-rater data limits which benchmarks can be budgeted.
- **Unresolved Questions:** Whether the model-bias share is really minority across modern models; how budgets shift across modalities and structure types.
- **Required Experiments:** Multi-rater datasets; synthetic validation where components are known by construction; error budgets for 5 models; cross-dataset stability analysis of the decomposition.
- **Reviewer Opinion:** If executed well this becomes the reference decomposition for boundary evaluation; top-five idea in the batch.

### IDEA-C-0206
- **One-sentence idea:** Measure the physics floor: partial-volume effects and slice thickness define a computable lower bound on boundary error in medical imaging.
- **Problem:** Boundary metrics are compared to zero as the implicit ideal, though imaging physics makes sub-PSF boundary localization information-theoretically limited.
- **Core Hypothesis (falsifiable):** A floor computed from point-spread function and voxel anisotropy predicts the plateau of boundary accuracy across models and datasets; models at the floor cannot be distinguished by boundary metrics, and reported "improvements" below the floor are noise.
- **Why Important:** Establishes when boundary progress is real versus metrological illusion — a calibration the field lacks.
- **Why Possibly Novel:** Physics-derived boundary-metric floors are not part of segmentation evaluation practice.
- **Minimal Experiment:** Derive floors for public CT/MR datasets from acquisition metadata; compare model boundary errors and inter-model gaps against floors.
- **Main Risk:** PSF metadata is incomplete for some datasets; estimate empirically from edge profiles where missing.

- **Survival Reason:** Physics-derived boundary-metric floors (PSF, voxel anisotropy) calibrate when boundary "progress" is metrological illusion — a missing yardstick for an entire evaluation culture.
- **Major Risks:** PSF metadata is incomplete for many datasets; floor derivation must handle anisotropy and reconstruction kernels carefully.
- **Unresolved Questions:** How many published inter-model gaps sit below the floor; whether image-wise empirical floor estimation from edge profiles is reliable.
- **Required Experiments:** Floor derivation for public CT/MR datasets from acquisition metadata; model-vs-floor and gap-vs-floor comparisons; empirical edge-profile estimation where metadata is missing.
- **Reviewer Opinion:** Physics grounding the field lacks; natural merge partner for the noise-floor work in 0321/0330 and the physical-truth ambition of eliminated 0224.

### IDEA-C-0208
- **One-sentence idea:** Derive and verify the systematic inward/outward boundary bias induced by cross-entropy training under class imbalance.
- **Problem:** Boundary placement bias is observed anecdotally (models "shrink" rare structures) but lacks an analytic account tied to the loss.
- **Core Hypothesis (falsifiable):** The stationary decision boundary under pixel-wise CE sits at a posterior threshold displaced from the true boundary by a computable function of local class prior and label noise — predicting per-structure signed bias that matches measured displacement fields across datasets.
- **Why Important:** A predictable, correctable bias affecting every CE-trained segmenter — including volumetry used clinically.
- **Why Possibly Novel:** The quantitative displacement prediction and its empirical verification are missing from the literature.
- **Minimal Experiment:** Derive the displacement formula; measure signed boundary displacement across structures with varying priors; compare prediction to measurement.
- **Main Risk:** Real training deviates from the stationary analysis (augmentation, schedules); test robustness across recipes.

- **Survival Reason:** A closed-form displacement-bias prediction from cross-entropy under class imbalance is rare theory-with-verification, and it predicts a correctable systematic error in clinical volumetry.
- **Major Risks:** Real training deviates from the stationary analysis (augmentation, schedules, compound losses); the formula may hold only approximately.
- **Unresolved Questions:** Whether the formula predicts measured bias fields (connects to 0218); how Dice/Tversky variants shift the displacement (absorbing eliminated 0230's stationary analysis).
- **Required Experiments:** Derivation of the displacement formula; signed boundary-displacement measurement across structures with varying priors; recipe-robustness checks; bias-correction demonstration.
- **Reviewer Opinion:** The theory anchor of C8; even partial confirmation gives the field its first principled loss-to-boundary account.

### IDEA-C-0210
- **One-sentence idea:** Redo method comparison statistics accounting for spatial autocorrelation of boundary errors — standard tests overstate significance.
- **Problem:** Boundary-error comparisons treat per-pixel or per-case errors as independent; boundary errors are strongly spatially autocorrelated, shrinking effective sample sizes.
- **Core Hypothesis (falsifiable):** Applying autocorrelation-corrected inference (effective-N adjustment, block bootstrap along boundaries) to published-style comparisons removes statistical significance from a substantial fraction of boundary-metric "wins" while leaving region-metric conclusions largely intact.
- **Why Important:** The field's boundary-improvement claims rest on inference that may be systematically anti-conservative.
- **Why Possibly Novel:** Spatial-statistics rigor has not been imported into segmentation benchmarking.
- **Minimal Experiment:** Measure boundary-error autocorrelation lengths; re-run 10 representative comparisons with corrected inference; report surviving claims.
- **Main Risk:** Correction methods have their own assumptions; use two independent correction approaches.

- **Survival Reason:** Spatial-autocorrelation-corrected inference could remove statistical significance from a substantial fraction of boundary-metric "wins" — statistics repair with real teeth, imported from a mature discipline.
- **Major Risks:** Correction methods carry their own assumptions; effective-N estimation along boundaries is subtle.
- **Unresolved Questions:** What fraction of published boundary claims survive; whether benchmarks should ship autocorrelation-aware test code as standard.
- **Required Experiments:** Boundary-error autocorrelation length measurement; re-analysis of 10 representative comparisons with block bootstrap and effective-N adjustment; two independent correction approaches for robustness.
- **Reviewer Opinion:** Underrated and cheap; belongs with 0321/0339 in a measurement-integrity trilogy that could anchor the whole program.

### IDEA-C-0212
- **One-sentence idea:** Detect annotation-tool fingerprints in ground-truth boundaries and quantify their effect on benchmark comparisons.
- **Problem:** Polygon tools, brushes, and level-set-assisted tools each impose characteristic boundary statistics (vertex spacing, curvature spectra, smoothness) that become part of "ground truth" invisibly.
- **Core Hypothesis (falsifiable):** The annotation tool is identifiable from boundary statistics alone at high accuracy, models trained on one tool's labels score systematically higher against same-tool test labels (tool-matching bonus), and part of cross-dataset "generalization gaps" is tool mismatch rather than image-domain shift.
- **Why Important:** A hidden variable contaminating every cross-dataset boundary comparison should be measured and corrected for.
- **Why Possibly Novel:** Tool forensics on segmentation ground truth appears entirely unexplored.
- **Minimal Experiment:** Train tool classifiers on datasets with documented tooling; measure the tool-matching bonus via cross-tool re-annotation of a subset.
- **Main Risk:** Tool metadata is rarely documented; requires targeted small re-annotation studies.

- **Survival Reason:** PROTECTED (counter-intuitive). Annotation-tool forensics — ground truth carrying identifiable tool fingerprints that confer tool-matching score bonuses — is a wholly unexplored confound in every cross-dataset boundary comparison.
- **Major Risks:** Tool metadata is rarely documented; the tool-matching bonus claim needs targeted cross-tool re-annotation; effect size may be small relative to domain shift.
- **Unresolved Questions:** Which boundary statistics carry the fingerprint; whether evaluation can deconvolve tool style post hoc.
- **Required Experiments:** Tool classifiers trained on datasets with documented tooling; small cross-tool re-annotation study; quantification of the tool-matching bonus; decomposition of cross-dataset gaps into tool vs domain components.
- **Reviewer Opinion:** Original in the strongest sense; even a null (no detectable fingerprint) is a useful sanity result. Dataset-batch merge flag noted.

### IDEA-C-0214
- **One-sentence idea:** Extract sub-pixel boundary estimates from logit gradients: models know boundary positions more precisely than their argmax masks express.
- **Problem:** Standard mask extraction discretizes at pixel resolution, discarding the continuous structure of the network's output field around boundaries.
- **Core Hypothesis (falsifiable):** Sub-pixel boundary localization derived from the logit field's zero-crossing interpolation beats argmax-mask boundaries against high-resolution reference truth by a consistent margin — demonstrating recoverable precision that standard evaluation and deployment throw away.
- **Why Important:** Free precision for volumetry and margins, plus a reframing: boundary quality is partly a readout problem, not a learning problem.
- **Why Possibly Novel:** Sub-pixel readout of segmentation networks against super-resolution ground truth has not been systematically evaluated.
- **Minimal Experiment:** Datasets with high-res reference (downsample-for-input protocol); compare argmax vs interpolated zero-crossing boundaries.
- **Main Risk:** Downsample-based reference protocols may favor interpolation methods artificially; complement with genuinely higher-resolution rescans where available.

- **Survival Reason:** PROTECTED (cheap counter-intuitive). Sub-pixel boundary readout from logit zero-crossings — free precision that standard argmax evaluation discards, reframing boundary quality as partly a readout problem.
- **Major Risks:** Downsample-for-input reference protocols can artificially favor interpolation methods; genuinely higher-resolution references are limited.
- **Unresolved Questions:** How much precision is recoverable per architecture; whether soft-label training (eliminated 0226) increases the recoverable margin.
- **Required Experiments:** Zero-crossing interpolation vs argmax boundaries against high-resolution references; paired-resolution rescans where available; per-structure and per-architecture gain analysis.
- **Reviewer Opinion:** A quick win with practical volumetry payoff; likely to be adopted in pipelines if positive, and cheap to refute if not.

### IDEA-C-0218
- **One-sentence idea:** Perform bias-variance decomposition of boundary displacement fields: model boundary errors are directional and consistent, not random.
- **Problem:** Boundary error metrics are unsigned magnitudes, hiding whether models systematically displace boundaries (bias) or scatter around truth (variance) — different problems with different fixes.
- **Core Hypothesis (falsifiable):** Across seeds, per-location mean displacement (bias field) accounts for the majority of squared boundary error in trained segmenters, bias fields are reproducible across architectures (image-driven), and simple post-hoc bias-field correction improves boundaries more than typical loss innovations.
- **Why Important:** If boundary error is mostly reproducible bias, it is correctable — a cheap large win the unsigned-metric convention has hidden.
- **Why Possibly Novel:** Signed, seed-resolved displacement decomposition has not been applied to segmentation boundaries.
- **Minimal Experiment:** Multi-seed trainings; estimate bias/variance fields on held-out data; test bias-correction transfer across seeds and models.
- **Main Risk:** Bias fields may be dataset-specific (annotation-driven); the architecture-reproducibility test distinguishes image- from label-driven bias.

- **Survival Reason:** Signed bias/variance decomposition of boundary displacement: if reproducible bias dominates, a cheap post-hoc correction beats years of loss innovation — a high-leverage reframing with reusable machinery.
- **Major Risks:** Bias fields may be annotation-driven rather than image-driven (the architecture-reproducibility test is essential); multi-seed training costs.
- **Unresolved Questions:** Bias-field transfer across models and datasets; interaction with 0208's theoretical predictions and 0310's distillation-inheritance claim.
- **Required Experiments:** Multi-seed trainings; per-location bias/variance field estimation on held-out data; cross-architecture reproducibility; bias-correction transfer tests.
- **Reviewer Opinion:** The central methodological node of C8 — 0208, 0310, and 0177 all consume its outputs; sequence it early.

---

## C9. Ambiguous labels / inter-rater disagreement as signal — 6 kept

### IDEA-C-0233
- **One-sentence idea:** Validate inter-rater disagreement maps as a free error oracle: where raters disagree predicts where models fail.
- **Problem:** Model error prediction (quality control) is built from model internals; the annotation process itself may already contain the best error predictor, unused.
- **Core Hypothesis (falsifiable):** Spatial rater-disagreement maps predict held-out model error maps with accuracy exceeding model-confidence-based error predictors, across architectures — implying model errors are dominated by intrinsic case ambiguity rather than model idiosyncrasy.
- **Why Important:** Would give deployment QC a model-independent error forecaster and reframe error analysis around case difficulty.
- **Why Possibly Novel:** Disagreement as a quantitative error-forecasting instrument (benchmarked against confidence methods) has not been established.
- **Minimal Experiment:** Multi-rater datasets; compare disagreement maps vs confidence/ensemble error predictors for several models; report predictive AUCs.
- **Main Risk:** Circularity if models were trained on the same raters' styles; use rater-disjoint training/evaluation splits.

- **Survival Reason:** Rater-disagreement maps as a model-free error oracle, benchmarked head-to-head against confidence-based error predictors — reframes quality control around case ambiguity rather than model internals.
- **Major Risks:** Circularity if evaluated models trained on the same raters' styles; multi-rater coverage limits generality.
- **Unresolved Questions:** Whether the oracle transfers across architectures and domains; how much a combined oracle+confidence predictor improves over either.
- **Required Experiments:** Multi-rater datasets with rater-disjoint training/evaluation splits; predictive-AUC comparison of disagreement maps vs confidence/ensemble predictors across ≥4 models.
- **Reviewer Opinion:** Simple and useful; the rater-disjoint control is what makes it credible science rather than a correlation note.

### IDEA-C-0234
- **One-sentence idea:** Quantify consensus harm: training on majority-vote/STAPLE labels destroys clinically relevant ambiguity information relative to training on raw rater sets.
- **Problem:** Consensus fusion is the default preprocessing for multi-rater data, presumed harmless noise reduction; it may erase exactly the distributional signal risk-aware applications need.
- **Core Hypothesis (falsifiable):** Models trained on raw multi-rater labels (as distributions) match consensus-trained models on consensus metrics while being substantially better calibrated to the rater distribution on ambiguous regions — the consensus step is where ambiguity information dies, measurably.
- **Why Important:** A default preprocessing choice with hidden costs affects nearly all multi-annotated medical datasets.
- **Why Possibly Novel:** The information cost of consensus fusion, isolated as a training-data intervention, is rarely measured directly.
- **Minimal Experiment:** Train on {consensus, raw multi-rater} from identical images; evaluate consensus accuracy and rater-distribution likelihood on held-out multi-rater data.
- **Main Risk:** Raw multi-rater training methods vary; use 2–3 established schemes to detach the claim from method specifics.

- **Survival Reason:** PROTECTED (counter-intuitive). Consensus fusion as the point where ambiguity information dies indicts the default preprocessing of nearly all multi-rater medical data, with a direct twin-training test.
- **Major Risks:** Distribution-training methods vary (claim must detach from method specifics); consensus-metric parity must be convincingly demonstrated.
- **Unresolved Questions:** Which fusion schemes (majority vote, STAPLE) destroy most information; consequences for downstream risk models.
- **Required Experiments:** {consensus-trained, raw-multi-rater-trained} twins with 2–3 established distributional methods; consensus accuracy plus held-out rater-distribution likelihood; ambiguity-region calibration analysis.
- **Reviewer Opinion:** The flagship of C9 and the cleanest bridge from label practice to clinical uncertainty needs; top-tier keep.

### IDEA-C-0235
- **One-sentence idea:** Decompose rater disagreement into systematic style offsets versus genuine ambiguity using mixed-effects modeling — recovering hidden agreement.
- **Problem:** All disagreement is treated as ambiguity; but raters may agree on the structure while differing by consistent personal offsets (tight vs generous delineation), a separable component.
- **Core Hypothesis (falsifiable):** A mixed-effects model (rater-specific boundary offset fields + shared ambiguity term) explains a majority of inter-rater variance on typical datasets, and style-corrected labels show substantially higher effective agreement — most "ambiguity" is removable style.
- **Why Important:** Changes the interpretation of multi-rater data everywhere: variance budgets, achievable-performance ceilings, and label fusion should all use style-corrected quantities.
- **Why Possibly Novel:** Formal style/ambiguity decomposition of segmentation disagreement is not standard practice.
- **Minimal Experiment:** Fit the decomposition on multi-rater datasets; report variance shares; validate style terms by cross-structure prediction of each rater's offsets.
- **Main Risk:** Style may be context-dependent (structure-specific); model hierarchical style terms.

- **Survival Reason:** The style-offset vs genuine-ambiguity mixed-effects decomposition could reveal that most "ambiguity" is removable style — changing variance budgets, performance ceilings, and fusion practice everywhere.
- **Major Risks:** Style may be context/structure-dependent, requiring hierarchical terms; identifiability with few raters per dataset.
- **Unresolved Questions:** Style-corrected achievable-performance ceilings; whether style correction improves fusion and tolerance-band evaluation (feeds 0245).
- **Required Experiments:** Mixed-effects model fitting on multi-rater datasets; variance-share reporting; validation of style terms by cross-structure prediction of each rater's offsets.
- **Reviewer Opinion:** Statistically mature modeling that medical label analysis has needed for a decade; the cross-structure validation is the convincing part.

### IDEA-C-0245
- **One-sentence idea:** Introduce tolerance-aware metrics: ignore errors inside the rater-variance band, and test how method rankings change.
- **Problem:** Metrics penalize deviations from a single reference even where experts themselves span a band; methods may be ranked by their fit to arbitrary within-band positions.
- **Core Hypothesis (falsifiable):** Recomputing benchmark comparisons with rater-variance tolerance bands (errors within the band count as zero) collapses a substantial fraction of published method gaps and reorders rankings — the surviving differences identify methods with genuine beyond-ambiguity improvements.
- **Why Important:** Distinguishes real progress from within-ambiguity noise fitting across the whole evaluation literature.
- **Why Possibly Novel:** Tolerance-band evaluation grounded in measured rater variance is not standard, and its effect on rankings is undocumented.
- **Minimal Experiment:** Construct tolerance bands from multi-rater data; re-evaluate 10 method comparisons with and without bands; quantify ranking stability.
- **Main Risk:** Bands require multi-rater data per benchmark; transfer physics-predicted bands (cf. 0240) where absent, with validation.

- **Survival Reason:** Tolerance-band evaluation grounded in measured rater variance directly tests whether published method gaps are within-ambiguity noise — measurement repair with immediate leaderboard consequences.
- **Major Risks:** Bands require multi-rater data per benchmark; transferring physics-predicted bands (eliminated 0240's idea) adds assumptions needing validation.
- **Unresolved Questions:** What fraction of published gaps collapse inside the band; how to standardize band construction for leaderboard adoption.
- **Required Experiments:** Band construction from multi-rater data; re-evaluation of 10 published-style comparisons with and without bands; ranking-stability quantification; physics-band transfer pilot.
- **Reviewer Opinion:** Combines naturally with 0321 and 0339 into a single evaluation-integrity story; keep all three and coordinate protocols.

### IDEA-C-0249
- **One-sentence idea:** Stress-test losses under multimodal ground truth: standard objectives assume unimodal truth and fail predictably when raters split between discrete hypotheses.
- **Problem:** When ambiguity is discrete (vessel branches left or right; lesion is one structure or two), the rater distribution is multimodal — and pixel-wise losses trained on it converge to averages that match no rater.
- **Core Hypothesis (falsifiable):** On constructed and natural multimodal-truth cases, models trained with standard losses produce anatomically invalid averaged solutions at high rates, while distribution-aware training preserves modes — with the invalid-average rate predictable from the modes' spatial separation.
- **Why Important:** Averaged solutions are silently absurd (blended branches, phantom bridges) and clinically dangerous; the failure condition should be characterized, not anecdotal.
- **Why Possibly Novel:** Multimodality as a formal failure condition of segmentation losses has not been characterized with predictive structure.
- **Minimal Experiment:** Construct mode-separation ladders (synthetic + curated real); measure invalid-average rates across losses and distribution-aware alternatives.
- **Main Risk:** Detecting "anatomically invalid" needs task-specific validity rules; start with objective topological criteria.

- **Survival Reason:** PROTECTED (high-risk/high-reward). Standard losses producing anatomically invalid "averaged" solutions under multimodal rater truth is a dangerous, characterizable pathology — silent absurdities like blended vessel branches deserve a predictive account.
- **Major Risks:** "Anatomically invalid" needs objective, task-specific rules; natural multimodal-truth cases are scarce; the mode-separation ladder is mostly synthetic.
- **Unresolved Questions:** Invalid-average rates in deployed models; which distribution-aware methods preserve modes at acceptable accuracy cost.
- **Required Experiments:** Mode-separation ladders (synthetic plus curated real cases); invalid-average rate measurement across standard losses; objective topological validity criteria; distribution-aware training baselines.
- **Reviewer Opinion:** A safety result waiting to be documented; protect despite the construction burden because no aggregate metric will ever surface it.

### IDEA-C-0253
- **One-sentence idea:** Quantify how well test-time augmentation disagreement aligns with human disagreement — a free surrogate for ambiguity maps.
- **Problem:** Multi-rater maps are expensive; prediction variability under input transforms is free, but its correspondence to human ambiguity is asserted rather than measured.
- **Core Hypothesis (falsifiable):** Spatial correlation between TTA-disagreement maps and real rater-disagreement maps is substantial but structured: high where ambiguity is appearance-driven, near zero where it is definitional — yielding a validated map of when the free surrogate is trustworthy.
- **Why Important:** A validated surrogate would extend every disagreement-based technique (0233, 0244, 0245) to single-rater datasets at zero annotation cost.
- **Why Possibly Novel:** The TTA-vs-human disagreement correspondence has not been quantitatively mapped and conditioned.
- **Minimal Experiment:** Compute both maps on multi-rater benchmarks; correlation analysis stratified by ambiguity type (cf. 0247's decomposition).
- **Main Risk:** Correspondence may be model-dependent; evaluate across 3 architectures.

- **Survival Reason:** PROTECTED (cheap-to-falsify). TTA-disagreement vs human-disagreement correspondence validates — or bounds — the field's favorite free ambiguity surrogate, at inference-only cost.
- **Major Risks:** Correspondence may be strongly model-dependent; the appearance-vs-definitional stratification borrows a decomposition (0247) that was not kept.
- **Unresolved Questions:** Exactly where the surrogate is trustworthy; whether ensemble disagreement dominates TTA disagreement as a surrogate.
- **Required Experiments:** TTA-disagreement and rater-disagreement maps on multi-rater benchmarks; spatial correlation stratified by ambiguity type; replication across ≥3 architectures; usage guidance for surrogate consumers.
- **Reviewer Opinion:** Everyone who cites TTA variance as "uncertainty" needs this number; the cheapest useful experiment in C9.

---

## C10. Foundation-model tokenization / resolution / memory artifacts — 6 kept

### IDEA-C-0261
- **One-sentence idea:** Measure grid-phase sensitivity: segmentation quality oscillates with the alignment between object boundaries and the ViT patch grid.
- **Problem:** Patchification imposes a fixed 14/16-pixel lattice; whether performance depends periodically on where boundaries fall within a patch is unmeasured — and it would constitute an unacknowledged noise source in every ViT benchmark result.
- **Core Hypothesis (falsifiable):** Sub-patch translations of the input produce periodic IoU oscillations with period equal to patch size, amplitude largest for thin structures, and negligible in CNN baselines — quantifying an aliasing artifact intrinsic to patch tokenization.
- **Why Important:** A periodic artifact means results depend on arbitrary image framing; it also motivates anti-aliased or shifted-ensemble inference with predictable gains.
- **Why Possibly Novel:** Grid-phase performance analysis for ViT dense prediction has not been reported.
- **Minimal Experiment:** Evaluate ViT and CNN segmenters under 0–16px translation sweeps; Fourier-analyze the score-vs-shift curves; stratify by structure width.
- **Main Risk:** Translation requires padding/cropping care to avoid confounding content changes.

- **Survival Reason:** Grid-phase performance oscillation is a crisp, cheap, previously unmeasured aliasing artifact claim: if IoU oscillates with sub-patch translation, every ViT benchmark number carries framing noise.
- **Major Risks:** Translation implementation confounds (padding/cropping content changes); heavy augmentation in modern training may already suppress phase sensitivity.
- **Unresolved Questions:** The amplitude-vs-structure-width law; whether shifted-ensemble inference delivers the predicted free gains.
- **Required Experiments:** 0–16px integer shift sweeps on ViT and CNN segmenters with crop-consistent evaluation; Fourier analysis of score-vs-shift curves; thin-structure stratification; shifted-ensemble validation.
- **Reviewer Opinion:** Textbook cheap-to-falsify design; positive or null, it settles a real question about tokenized dense prediction.

### IDEA-C-0264
- **One-sentence idea:** Audit thin-structure information survival through patch embedding: what is destroyed at tokenization versus recoverable downstream.
- **Problem:** Structures thinner than the patch stride (vessels, wires, fissures) may lose identity at the very first layer, bounding all downstream processing — but the loss has not been isolated from later-stage limitations.
- **Core Hypothesis (falsifiable):** Probes on post-embedding tokens show thin-structure detectability dropping sharply below a width threshold tied to stride and embedding filters, this threshold propagates unchanged to final-layer features (nothing downstream recovers it), and sub-stride convolutional stems shift the threshold predictably — the bottleneck is the tokenizer.
- **Why Important:** Identifies which anatomy classes are structurally unreachable for given tokenizer settings, before training anything.
- **Why Possibly Novel:** Layer-of-loss attribution for thin structures (tokenizer vs downstream) has not been established.
- **Minimal Experiment:** Width-ladder synthetic structures + vessel data; probe detectability at embedding and final layers across stem designs.
- **Main Risk:** Learned embeddings differ across pretrained models; test several checkpoints to separate architecture from weights.

- **Survival Reason:** Tokenizer-stage information destruction for thin structures, with layer-of-loss attribution: identifies which anatomy classes are structurally unreachable for a given tokenizer before any training happens.
- **Major Risks:** Learned embeddings differ across pretrained checkpoints; probes measure accessibility, not strict information absence.
- **Unresolved Questions:** The exact width-threshold law versus stride and embedding filters; whether sub-stride convolutional stems shift the threshold as predicted.
- **Required Experiments:** Width-ladder synthetic structures plus vessel datasets; detectability probes at the embedding layer and final layer; stem-design comparisons across several checkpoints.
- **Reviewer Opinion:** Fundamental and immediately useful; forms a natural pair with 0164's frequency bound at the FM level.

### IDEA-C-0269
- **One-sentence idea:** Test whether anti-aliased patchification (strided-conv tokenizers violate Nyquist) changes ViT texture bias and dense robustness.
- **Problem:** Patch embedding is a stride-16 convolution — a textbook aliasing operation — yet aliasing's contribution to ViT behavior (texture sensitivity, shift instability) has not been isolated at the tokenizer.
- **Core Hypothesis (falsifiable):** Adding proper low-pass filtering before patch sampling (fixed, non-learned) reduces measured shift inconsistency and high-frequency texture reliance of ViT features at equal accuracy, with the largest dense-task gains on high-frequency-content domains (pathology, bone) — aliasing at tokenization is a causal contributor to known ViT pathologies.
- **Why Important:** A one-layer, principled fix testable against multiple documented artifacts (0261, 0071) at once.
- **Why Possibly Novel:** Anti-aliasing is studied for CNN downsampling; the ViT-tokenizer version with dense endpoints is essentially untested.
- **Minimal Experiment:** Train twin ViTs {standard, anti-aliased tokenizer} at modest scale; run shift-consistency, cue-conflict, and dense-task batteries.
- **Main Risk:** Retraining requirement limits scale; complement with fine-tuning-only conversions of existing checkpoints.

- **Survival Reason:** Anti-aliased patchification tests a principled causal account (Nyquist violation at the tokenizer) of several documented ViT pathologies simultaneously — one fixed low-pass layer against shift instability and texture bias.
- **Major Risks:** Requires twin retraining (modest scale); effects may shrink at convergence under strong augmentation; fine-tune-only conversion may not suffice.
- **Unresolved Questions:** Whether anti-aliasing removes 0261-style grid-phase sensitivity; interaction with patch size and high-frequency medical domains.
- **Required Experiments:** Twin ViTs {standard, anti-aliased tokenizer} at modest scale; shift-consistency, cue-conflict, and dense-task batteries; fine-tuning-only conversion arm on existing checkpoints.
- **Reviewer Opinion:** The most intervention-flavored keep in C10, but the aliasing hypothesis is genuine science with wide reach; kept because it adjudicates a mechanism, not because it adds a module.

### IDEA-C-0273
- **One-sentence idea:** Audit window-position bias in sliding-window inference: prediction quality varies systematically between window centers and edges, hidden by overlap blending.
- **Problem:** 3D/high-res pipelines predict in overlapping windows and blend; the blend obscures whether voxels near window edges receive systematically worse predictions — and whether blending weights are anywhere near optimal.
- **Core Hypothesis (falsifiable):** Per-voxel error conditioned on within-window position shows a reproducible center-to-edge quality gradient (context truncation effect), Gaussian blending under-corrects it, and empirically fitted position-dependent weights improve final accuracy at zero model change — a free, measurable pipeline win.
- **Why Important:** Sliding-window inference is universal in medical segmentation; its internal quality structure has never been audited.
- **Why Possibly Novel:** Window-relative error profiling and empirical blend optimization are absent from standard practice.
- **Minimal Experiment:** Log per-voxel error in window coordinates across datasets/models; fit optimal blend weights; validate gains.
- **Main Risk:** Gradients may be architecture-specific; profile CNN and transformer backbones separately.

- **Survival Reason:** Window-position error profiling of sliding-window inference exposes a potential free accuracy win in a universally used pipeline; near-zero risk and immediate utility.
- **Major Risks:** Center-to-edge gradients may be architecture-specific; residual gains after Gaussian blending may be small.
- **Unresolved Questions:** The optimal blend-weight fitting protocol; whether the position gradient interacts with 0204's window-size failure on large objects.
- **Required Experiments:** Per-voxel error logging in window-relative coordinates across datasets and models; empirically fitted position-dependent blend weights; validation gains; CNN vs transformer profiles.
- **Reviewer Opinion:** The definition of low-hanging fruit; every nnU-Net-style pipeline will cite it if the fitted weights help.

### IDEA-C-0276
- **One-sentence idea:** Test whether learned feature-upsampling methods add image information or merely impose learned priors — hallucinating plausible but ungrounded boundary detail.
- **Problem:** Feature up-samplers (FeatUp-style) sharpen coarse backbone features impressively; whether the added detail reflects the specific image or dataset-prior interpolation is unresolved and consequential for medical use.
- **Core Hypothesis (falsifiable):** On stimuli where local image evidence contradicts dataset priors (constructed boundary displacements), learned up-samplers place detail according to priors rather than evidence at a measurable rate, while evidence-guided baselines (bilateral/guided filtering) follow the image — the sharpness is partly hallucination, quantifiable per method.
- **Why Important:** Prior-driven boundary detail in medical pipelines is a silent fabrication risk exactly where it looks most convincing.
- **Why Possibly Novel:** Evidence-vs-prior adjudication tests for feature upsampling have not been designed or run.
- **Minimal Experiment:** Construct evidence-prior conflict stimuli; compare upsampler outputs against both hypotheses; quantify hallucination rates per method.
- **Main Risk:** Constructed conflicts must remain realistic; use physically plausible boundary manipulations.

- **Survival Reason:** Evidence-vs-prior adjudication of learned feature upsampling targets a silent fabrication risk: sharp boundary detail that reflects dataset priors rather than the image, precisely where outputs look most convincing.
- **Major Risks:** Constructed evidence-prior conflict stimuli must remain physically plausible; hallucination-rate metrics need careful definition.
- **Unresolved Questions:** Per-method hallucination rates (learned upsamplers vs guided filtering); whether hallucinated detail propagates into downstream clinical decisions.
- **Required Experiments:** Conflict stimuli with physically plausible boundary displacements; upsampler battery comparison; hallucination-rate quantification; downstream propagation check on one clinical quantity.
- **Reviewer Opinion:** Timely — feature upsampling is spreading into medical pipelines faster than its epistemics are being examined; strong keep.

### IDEA-C-0287
- **One-sentence idea:** Quantify numerics as a benchmark variance source: low-precision attention implementations change dense outputs near boundaries at rates comparable to reported method gains.
- **Problem:** FlashAttention variants, bf16/fp16 choices, and kernel fusion alter floating-point summation orders; dense predictions near decision boundaries can flip, yet numerics is never reported or controlled in benchmarks.
- **Core Hypothesis (falsifiable):** Across numerics configurations (kernels, precisions, batch nondeterminism), per-pixel prediction flips concentrate near boundaries and accumulate to metric differences overlapping the magnitude of typical published improvements on fine-grained boundary metrics — numerics is an unacknowledged term in the field's error budget.
- **Why Important:** If numerics-induced variance rivals claimed gains, reporting standards must change (fixed-numerics evaluation or variance disclosure).
- **Why Possibly Novel:** Numerics-variance accounting for dense-prediction benchmarks has not been published.
- **Minimal Experiment:** Evaluate fixed checkpoints under a numerics-configuration grid; flip-map analysis; compare variance to published deltas.
- **Main Risk:** Findings depend on hardware generation; report across two GPU families.

- **Survival Reason:** PROTECTED (high-risk/high-reward). Numerics (attention kernels, precision, batch nondeterminism) as an unacknowledged variance term rivaling published method gains would force reporting-standards changes across dense-prediction benchmarking.
- **Major Risks:** Hardware-generation dependence; flip rates may prove negligible for well-margined models (an informative but less dramatic null).
- **Unresolved Questions:** Which layers/operations dominate boundary flips; whether benchmarks should fix numerics configurations or disclose variance.
- **Required Experiments:** Fixed checkpoints evaluated under a numerics grid (attention kernels, fp16/bf16/fp32, deterministic vs nondeterministic reduction); boundary flip-map analysis; variance vs published-delta comparison; two GPU families.
- **Reviewer Opinion:** Cheap, strange, and important; the protect flag exists for exactly this kind of unglamorous but foundational audit.

---

## C11. Community beliefs that may be false — 6 kept

### IDEA-C-0289
- **One-sentence idea:** Test non-monotonicity of pretraining scale for medical transfer: curated small pretraining can beat web-scale for specific modalities.
- **Problem:** "More pretraining data always helps downstream medical tasks" guides model selection, but distribution mismatch may make web-scale pretraining actively dilutive for some modalities.
- **Core Hypothesis (falsifiable):** For at least some modality/task pairs (e.g., ultrasound, OCT), models pretrained on smaller curated in-domain-adjacent corpora outperform web-scale-pretrained models of matched architecture after identical fine-tuning — and the crossover is predicted by a measurable domain-distance statistic.
- **Why Important:** Model-selection defaults ("take the biggest") drive real medical projects; documented exceptions with a predictor would change practice.
- **Why Possibly Novel:** Scale-vs-curation crossovers with a validated pre-hoc predictor have not been mapped for medical transfer.
- **Minimal Experiment:** {web-scale, curated-medium, in-domain-small} pretrained backbones × 8 medical tasks with matched fine-tuning; crossover analysis against domain-distance measures.
- **Main Risk:** Matched-architecture checkpoints across pretraining regimes are scarce; some controlled pretraining required.

- **Survival Reason:** Curation-beats-scale crossovers with a pre-hoc domain-distance predictor attack the "take the biggest checkpoint" default at its evidence base, for the modalities where mismatch is most plausible.
- **Major Risks:** Matched-architecture checkpoints across pretraining regimes are scarce, forcing some controlled pretraining; crossovers may be modality-idiosyncratic.
- **Unresolved Questions:** Which domain-distance statistic predicts the crossover; whether the effect persists at the largest FM scales.
- **Required Experiments:** {web-scale, curated-medium, in-domain-small} pretrained backbones × 8 medical tasks with matched fine-tuning; crossover analysis against candidate distance measures; held-out modality validation.
- **Reviewer Opinion:** The most consequential C11 belief-test for medical practitioners; the predictor requirement keeps it from being a mere leaderboard exercise.

### IDEA-C-0290
- **One-sentence idea:** Test whether Dice loss is actually necessary for imbalanced segmentation, or whether tuned weighted cross-entropy matches it.
- **Problem:** "Use Dice loss for imbalance" is near-universal advice, potentially established against under-tuned CE baselines and perpetuated by citation.
- **Core Hypothesis (falsifiable):** With properly tuned class weights and learning-rate schedules, weighted CE matches Dice-family losses on region metrics across imbalance levels, while showing different (sometimes better) boundary and calibration behavior — the belief reflects tuning asymmetry, not loss superiority.
- **Why Important:** Loss folklore shapes thousands of experiments; a corrected account also recovers CE's superior probabilistic properties where usable.
- **Why Possibly Novel:** A tuning-equalized, multi-metric adjudication of the CE-vs-Dice belief is missing despite the topic's ubiquity.
- **Minimal Experiment:** Imbalance-graded datasets × {tuned WCE, Dice, compound} with equal tuning budgets; multi-metric comparison with variance accounting.
- **Main Risk:** "Properly tuned" invites dispute; pre-register tuning protocols and budgets.

- **Survival Reason:** The Dice-vs-properly-tuned-weighted-CE adjudication targets the field's most-repeated loss advice with a tuning-equalized, pre-registered design; CE's superior probabilistic properties raise the stakes.
- **Major Risks:** "Properly tuned" invites dispute; conclusions may vary by imbalance regime and metric family.
- **Unresolved Questions:** Calibration and boundary behavior differences at matched region metrics (connects to 0208); task-conditional guidance.
- **Required Experiments:** Imbalance-graded datasets × {tuned weighted CE, Dice-family, compound} with equal, pre-registered tuning budgets; multi-metric evaluation with variance accounting.
- **Reviewer Opinion:** Folklore surgery with a huge audience; execution hygiene (pre-registration) is everything here.

### IDEA-C-0300
- **One-sentence idea:** Attribute nnU-Net's dominance: is it the self-configuring architecture or simply the preprocessing/normalization stack?
- **Problem:** nnU-Net's success is culturally attributed to holistic self-configuration; component-level attribution would tell the field which parts to copy — but has not been done systematically.
- **Core Hypothesis (falsifiable):** Transplanting only nnU-Net's preprocessing/intensity-normalization/resampling stack onto generic baselines recovers the majority of its advantage across tasks, while its architecture choices contribute a minor share — the field under-invests in preprocessing because attribution is missing.
- **Why Important:** Correct credit assignment redirects replication effort to the components that matter.
- **Why Possibly Novel:** Full factorial component attribution of the nnU-Net stack has not been published.
- **Minimal Experiment:** Factorial transplant of {preprocessing, augmentation, architecture, postprocessing} components onto plain baselines across 5 tasks.
- **Main Risk:** Components interact; factorial (not one-at-a-time) design is essential and costlier.

- **Survival Reason:** Factorial component attribution of nnU-Net's dominance is the highest-leverage credit-assignment experiment in medical segmentation; the preprocessing-carries-it hypothesis is specific and actionable.
- **Major Risks:** Components interact, making one-at-a-time transplants misleading (factorial design is costlier); version drift in the reference system.
- **Unresolved Questions:** The preprocessing vs architecture share; whether the attribution transfers to transformer-based pipelines.
- **Required Experiments:** Factorial transplant of {preprocessing, augmentation, architecture, postprocessing} onto plain baselines across 5 tasks; interaction analysis; component-share reporting.
- **Reviewer Opinion:** Someone will eventually do this; better to do it carefully and first. Redirects replication effort across the whole field.

### IDEA-C-0301
- **One-sentence idea:** Measure the true frozen-backbone ceiling for dense prediction with properly engineered multi-layer readouts.
- **Problem:** "Frozen backbones can't do dense prediction well" justifies universal fine-tuning; the claim is largely tested with naive single-layer readouts.
- **Core Hypothesis (falsifiable):** With multi-layer feature aggregation and modest decoders, frozen modern backbones close most of the gap to full fine-tuning on standard segmentation benchmarks — the believed necessity of fine-tuning reflects readout under-engineering, with the residual gap concentrated in domain-shifted settings.
- **Why Important:** Frozen deployment enables shared backbones, cheap certification, and multi-task serving; its real ceiling should be known.
- **Why Possibly Novel:** A systematic frozen-ceiling measurement with strong readouts across backbones is missing.
- **Minimal Experiment:** Readout-capacity sweeps on frozen backbones vs fine-tuning across 6 dense tasks; gap decomposition by domain distance.
- **Main Risk:** "Modest decoder" boundaries need pre-registration to avoid moving goalposts.

- **Survival Reason:** The frozen-backbone ceiling with properly engineered multi-layer readouts tests the universal fine-tuning assumption; frozen deployment has large certification and serving implications.
- **Major Risks:** "Modest decoder" goalposts must be pre-registered; results may hinge on backbone family and pretraining type.
- **Unresolved Questions:** Where the residual gap concentrates (domain shift?); connections to 0034's readout-forgetting result and eliminated 0335's linear-sufficiency control.
- **Required Experiments:** Readout-capacity sweeps on frozen backbones vs full fine-tuning across 6 dense tasks; pre-registered decoder budget ladder; gap decomposition by domain distance.
- **Reviewer Opinion:** Bridges C1's PEFT program and C11's belief-testing; high practical value for multi-task serving decisions.

### IDEA-C-0310
- **One-sentence idea:** Measure what distillation actually transfers in segmentation: soft labels carry the teacher's spatially correlated error structure along with its "dark knowledge".
- **Problem:** Distillation is treated as transferring beneficial class-similarity information; in dense tasks the teacher's systematic boundary biases (cf. 0218) are part of the signal, and their inheritance is unexamined.
- **Core Hypothesis (falsifiable):** Student boundary-bias fields correlate strongly with teacher bias fields (far above independently trained controls), inherited bias persists even when students surpass teachers on aggregate metrics, and bias-corrected teacher outputs (0218's correction) produce measurably better students — distillation transfers error structure, correctably.
- **Why Important:** Distillation is the deployment path for foundation models (cf. 0178); inherited systematic bias would propagate silently into clinical tools.
- **Why Possibly Novel:** Error-structure inheritance analysis in dense distillation is missing.
- **Minimal Experiment:** Teacher/student bias-field correlation analysis across distillation setups; bias-corrected-teacher intervention.
- **Main Risk:** Bias-field estimation needs multi-seed teachers; compute-heavy but tractable.

- **Survival Reason:** Distillation inheriting spatially correlated teacher error structure reframes the FM→specialist deployment path as a bias conduit; the bias-corrected-teacher intervention makes it constructive rather than merely critical.
- **Major Risks:** Bias-field estimation needs multi-seed teachers (compute); inheritance may weaken as students grow strong.
- **Unresolved Questions:** Whether bias-corrected distillation reliably improves students; which distillation losses transmit the most error structure.
- **Required Experiments:** Teacher/student bias-field correlation across distillation setups; independently trained controls; bias-corrected-teacher intervention using 0218's machinery.
- **Reviewer Opinion:** A strong synthesis idea that depends on 0218's tools — schedule it after that machinery exists.

### IDEA-C-0311
- **One-sentence idea:** Test whether early stopping on validation Dice silently sacrifices boundary quality that continues improving after Dice plateaus.
- **Problem:** Standard practice stops training when val-Dice plateaus; if metric families converge at different speeds (cf. 0207), the convention systematically truncates boundary learning.
- **Core Hypothesis (falsifiable):** Boundary metrics continue improving significantly after val-Dice plateau in a substantial fraction of training runs, so Dice-based stopping leaves consistent boundary performance unbanked — and multi-metric stopping criteria capture it at negligible cost.
- **Why Important:** A universal training convention may be systematically shaving boundary quality off every published model.
- **Why Possibly Novel:** Metric-resolved post-plateau training dynamics have not been documented.
- **Minimal Experiment:** Extended trainings past Dice plateau across datasets/architectures; metric-family trajectory analysis; stopping-rule comparison.
- **Main Risk:** Post-plateau boundary gains may overfit annotation style; validate on multi-rater or physical-reference subsets.

- **Survival Reason:** PROTECTED (cheap-to-falsify). Early stopping on validation Dice truncating still-improving boundary learning is a universal-convention audit costing almost nothing, with an immediate multi-metric stopping-rule remedy.
- **Major Risks:** Post-plateau boundary "gains" may be annotation-style overfitting — the multi-rater/physical-reference validation arm is essential.
- **Unresolved Questions:** How frequent and how large the unbanked boundary improvement is; principled multi-metric stopping design; connection to metric-resolved scaling exponents (eliminated 0207).
- **Required Experiments:** Extended trainings past Dice plateau across datasets and architectures; metric-family trajectory analysis; stopping-rule comparison; multi-rater validation of late boundary gains.
- **Reviewer Opinion:** An easy early win for the program; even a modest effect changes default training practice.

---

## C12. Cheap experiments to overturn implicit assumptions — 10 kept

### IDEA-C-0315
- **One-sentence idea:** Run the scramble test on published "global context" modules: shuffle distant image regions and see if the module's benefit survives.
- **Problem:** Many papers attribute gains to long-range context aggregation; if performance is unchanged when distant content is scrambled, the module's stated mechanism is not what it does.
- **Core Hypothesis (falsifiable):** For a substantial fraction of published context modules, the accuracy gain over local baselines persists under distant-region scrambling — the gains come from added capacity/regularization, not from the long-range information the papers credit.
- **Why Important:** Mechanism misattribution compounds across the literature; a cheap universal test cleans it.
- **Why Possibly Novel:** Scramble-based mechanism verification has not been applied systematically to context-module claims.
- **Minimal Experiment:** Take 5 public context-module models; evaluate with block-scrambled inputs (preserving local windows); compare gain retention against local-only baselines.
- **Main Risk:** Scrambling introduces edge artifacts; use soft-blended scrambles and artifact controls.

- **Survival Reason:** PROTECTED (cheap-to-falsify). The scramble test is a universal, inference-only mechanism-verification instrument for "global context" claims — a reusable audit, not a one-off.
- **Major Risks:** Scrambling introduces edge artifacts (needs soft blending and artifact controls); modules using mid-range context muddy interpretation.
- **Unresolved Questions:** The distribution of gain-retention across published modules; whether retention predicts OOD behavior.
- **Required Experiments:** 5 public context-module models; block-scramble batteries preserving local windows; artifact controls; gain-retention comparison against local-only baselines.
- **Reviewer Opinion:** Should become a standard reviewer request; trivially cheap and endlessly reusable.

### IDEA-C-0316
- **One-sentence idea:** Replace learned prompts with random-but-frozen vectors of matched norm: if accuracy holds, prompt "learning" is mostly capacity, not semantics.
- **Problem:** Prompt-tuning papers imply prompts encode task semantics; the null hypothesis — any extra trainable-then-frozen directions plus the head recalibration suffice — is never run.
- **Core Hypothesis (falsifiable):** Freezing prompts at random initialization while training only the same lightweight components the method trains recovers a large fraction of reported gains on standard benchmarks — bounding the semantic content of learned prompts from above.
- **Why Important:** A one-afternoon control that recalibrates interpretation of an entire method family.
- **Why Possibly Novel:** The random-frozen-prompt control is conspicuously absent from the literature.
- **Minimal Experiment:** Rerun 3 canonical prompt methods with random-frozen prompts across their benchmarks; gain-retention table.
- **Main Risk:** Method variants differ in what else is trained; match trainable components exactly per method.

- **Survival Reason:** PROTECTED (cheap-to-falsify). Random-frozen prompts of matched norm upper-bound the semantic content of prompt learning — the conspicuously missing null control for an entire method family.
- **Major Risks:** Trainable-component matching must be exact per method; results may vary across benchmarks.
- **Unresolved Questions:** How much of CoOp-family gains survive the control; whether dense-task prompts behave differently.
- **Required Experiments:** 3 canonical prompt methods rerun with random-frozen prompts and identical trainable components; gain-retention tables across their own benchmarks.
- **Reviewer Opinion:** One afternoon of compute against years of interpretation; pairs with 0094/0095 as a prompt-learning audit suite.

### IDEA-C-0321
- **One-sentence idea:** Re-annotate 50 test images with 3 raters and check whether benchmark leaderboard gaps exceed the annotation noise floor.
- **Problem:** Leaderboard differences are interpreted as method quality without knowing the test labels' own uncertainty — a floor obtainable for the cost of a small annotation study.
- **Core Hypothesis (falsifiable):** For popular benchmarks, the score fluctuation induced by substituting equally valid alternative annotations exceeds a large fraction of the top-10 leaderboard spread — many ranked differences are label-noise artifacts, quantifiably.
- **Why Important:** A few-hundred-dollar experiment that recalibrates how much attention leaderboard deltas deserve.
- **Why Possibly Novel:** Annotation-noise floors for specific popular leaderboards are not published.
- **Minimal Experiment:** Triple-annotate 50-image test subsets on 2 benchmarks; recompute top-model scores against each annotation; compare spread to leaderboard gaps.
- **Main Risk:** Subset sampling variance; choose stratified subsets and report confidence intervals.

- **Survival Reason:** PROTECTED (cheap-to-falsify). Small 3-rater re-annotation to bound leaderboard label-noise floors is the most decisive-per-dollar experiment in the batch and anchors 0210/0245/0339's claims.
- **Major Risks:** 50-image subsets may under-sample benchmark diversity; rater recruitment and protocol drift.
- **Unresolved Questions:** Floor size versus top-10 leaderboard spreads per benchmark; how leaderboards should report label-noise confidence intervals.
- **Required Experiments:** Triple re-annotation of stratified 50-image test subsets on 2 popular benchmarks; re-scoring of top public models against each annotation; spread-vs-gap analysis with confidence intervals.
- **Reviewer Opinion:** Flagged as dataset-batch adjacent (merge candidate), kept here because the whole measurement-integrity program cites its number.

### IDEA-C-0325
- **One-sentence idea:** Test histogram matching as a domain-adaptation baseline: if intensity alignment closes most of the cross-site gap, complex DA methods are solving an already-solved problem.
- **Problem:** Domain-adaptation papers for medical imaging rarely include the cheapest classical baseline — per-image intensity histogram alignment — leaving their headroom claims unanchored.
- **Core Hypothesis (falsifiable):** Histogram matching (plus nothing) recovers a majority of the cross-site performance drop on standard medical DA benchmarks, and published DA methods' gains shrink to marginal once applied on top of it — the benchmarks primarily measure intensity shift.
- **Why Important:** An hour-long baseline that potentially reframes an entire benchmark literature's difficulty claims.
- **Why Possibly Novel:** The baseline is old; its systematic accounting against the modern DA literature is missing.
- **Minimal Experiment:** Histogram-matching preprocessing on 4 DA benchmarks; compare against published DA gains with and without it.
- **Main Risk:** Matching can harm pathological-intensity cases; report per-case distributions, not just means.

- **Survival Reason:** PROTECTED (cheap-to-falsify). Histogram matching as the missing classical domain-adaptation baseline: an hour of preprocessing that could reframe the difficulty claims of a benchmark literature.
- **Major Risks:** Matching can harm pathological-intensity cases (per-case reporting essential); results will vary by benchmark.
- **Unresolved Questions:** What share of published DA gains survives on top of matching; which benchmarks measure more than intensity shift.
- **Required Experiments:** Histogram-matching preprocessing on 4 DA benchmarks; published-method deltas recomputed with and without it; per-case error distributions rather than means.
- **Reviewer Opinion:** Emblematic of C12's purpose; must be in the survivor set on falsifiability-per-cost grounds alone.

### IDEA-C-0326
- **One-sentence idea:** Run the slice-order checkerboard test on "3D" models: feed volumes with permuted slice order and see whether claimed volumetric reasoning notices.
- **Problem:** 3D architectures claim volumetric context use; if predictions are unchanged under slice permutation, the models are functionally 2.5D and the papers' mechanism claims fail.
- **Core Hypothesis (falsifiable):** A measurable fraction of published 3D models show near-identical performance under local slice permutations — their receptive fields or learned features do not exploit inter-slice order, contradicting the stated rationale for their 3D design.
- **Why Important:** Zero-training mechanism verification for a whole architecture class.
- **Why Possibly Novel:** Order-destruction testing of 3D segmentation models has not been reported systematically.
- **Minimal Experiment:** Local and global slice-permutation batteries on 6 public 3D models; degradation profiles vs claimed 3D mechanisms.
- **Main Risk:** Some tasks genuinely need no order information; pair with tasks where order provably matters (cf. 0153).

- **Survival Reason:** PROTECTED (cheap-to-falsify). Slice-order permutation testing of "3D reasoning" claims is zero-training mechanism verification for an architecture class; absorbs 0153's benchmark-partitioning framing into one paper.
- **Major Risks:** Order-insensitivity may be task-appropriate (needs paired tasks where order provably matters); trivial stitching heuristics confound interpretation.
- **Unresolved Questions:** Which public 3D models actually exploit inter-slice order; whether order use correlates with through-plane boundary quality.
- **Required Experiments:** Local and global slice-permutation batteries on 6 public 3D models; degradation profiles versus claimed mechanisms; order-critical control tasks; graded local shuffles.
- **Reviewer Opinion:** Inference-only, immediately interpretable, and mildly explosive if many "3D" models don't notice.

### IDEA-C-0328
- **One-sentence idea:** Run embedding-based near-duplicate detection between train and test splits of popular benchmarks — a cheap contamination audit with potentially large consequences.
- **Problem:** Benchmark splits constructed years ago (sometimes from overlapping sources) may contain near-duplicates or same-patient leakage that inflates all published results on them.
- **Core Hypothesis (falsifiable):** Automated near-duplicate and same-patient detection finds nontrivial contamination in at least some widely used benchmarks, and re-scoring published-style models on decontaminated test sets measurably shrinks and reorders reported performance.
- **Why Important:** Everything downstream of a contaminated benchmark is miscalibrated; the audit costs a day per benchmark.
- **Why Possibly Novel:** Systematic contamination audits are common in NLP now but rare for medical-imaging benchmarks.
- **Minimal Experiment:** Embedding-NN plus metadata analysis on 5 benchmarks; contamination reports; decontaminated re-scoring of public models.
- **Main Risk:** Near-duplicate thresholds need care to avoid false positives; verify flagged pairs manually.

- **Survival Reason:** Train/test near-duplicate and same-patient contamination archaeology for medical benchmarks — high-consequence hygiene with mature tooling from NLP; absorbs 0170's FM-pretraining contamination angle.
- **Major Risks:** Near-duplicate thresholds produce false positives (manual verification required); some benchmarks may be clean, yielding a quiet result.
- **Unresolved Questions:** Contamination prevalence across the medical benchmark canon; the effect size of decontaminated re-scoring on published rankings.
- **Required Experiments:** Embedding nearest-neighbor plus metadata audits on 5 benchmarks; manual verification of flagged pairs; decontaminated re-scoring of public models.
- **Reviewer Opinion:** Dataset-batch merge flag; kept here because every other evaluation-repair survivor depends on knowing the benchmarks are clean.

### IDEA-C-0329
- **One-sentence idea:** Replace the VLM text encoder's output with class-mean image embeddings: if open-vocab segmentation is unchanged, "language" contributes nothing beyond class indexing.
- **Problem:** Open-vocabulary methods credit language understanding; the null — text embeddings function merely as arbitrary class anchors learnable from images alone — is never tested.
- **Core Hypothesis (falsifiable):** Substituting text embeddings with image-derived class prototypes (mean embeddings of a handful of examples) preserves most open-vocab segmentation performance on seen-vocabulary classes, with genuine language value confined to zero-example classes — bounding the linguistic contribution precisely.
- **Why Important:** Clarifies what "language-driven" methods actually use language for — with one embedding-swap experiment.
- **Why Possibly Novel:** The prototype-substitution control is absent from the open-vocab dense literature.
- **Minimal Experiment:** Embedding-swap evaluation on 4 open-vocab segmenters; seen vs zero-example class analysis.
- **Main Risk:** Prototype quality depends on example count; sweep from 1 to 100 examples.

- **Survival Reason:** PROTECTED (cheap counter-intuitive). Replacing the text encoder with class-mean image prototypes bounds the linguistic contribution of "language-driven" segmentation with a single embedding swap.
- **Major Risks:** Prototype quality depends on example count (sweep required); seen-class emphasis may understate language's genuine zero-example role.
- **Unresolved Questions:** Where language genuinely matters (zero-example classes, composition); whether the result transfers to medical VLM segmenters.
- **Required Experiments:** Embedding-swap evaluation on 4 open-vocab segmenters; example-count sweeps (1–100); seen vs zero-example class analysis.
- **Reviewer Opinion:** Deflationary with a precise scope; complements 0072 and 0067 in the language-claims audit family.

### IDEA-C-0332
- **One-sentence idea:** Apply the mask-the-lesion test systematically to medical detection papers: does the detector still fire on surrounding context when the finding itself is erased?
- **Problem:** Reported detection performance may ride on contextual shortcuts (position, co-occurring devices, patient habitus); the direct occlusion control is quick and rarely reported.
- **Core Hypothesis (falsifiable):** For a measurable fraction of published-style medical detectors, inpainting the lesion region leaves detection confidence above the decision threshold on many cases — a context-shortcut prevalence estimate per model and dataset that reframes their claimed sensitivity.
- **Why Important:** Context-firing detectors fail exactly on atypical presentations; the prevalence number belongs next to every reported AUC.
- **Why Possibly Novel:** Systematic occlusion-audit results across medical detection models are not published.
- **Minimal Experiment:** Lesion inpainting on positive cases across 5 public detectors; confidence-retention distributions; per-dataset shortcut prevalence.
- **Main Risk:** Inpainting artifacts can themselves trigger detectors; validate with artifact-only controls.

- **Survival Reason:** PROTECTED (cheap-to-falsify). The mask-the-lesion occlusion audit yields a per-model context-shortcut prevalence number that belongs next to every reported medical-detection AUC.
- **Major Risks:** Inpainting artifacts can themselves trigger detectors (artifact-only controls essential); prevalence may vary wildly across datasets.
- **Unresolved Questions:** Which context factors carry the shortcut (position, devices, patient habitus); whether shortcut prevalence predicts failures on atypical presentations.
- **Required Experiments:** Lesion inpainting on positive cases across 5 public detectors; confidence-retention distributions; artifact-only controls; context-attribution analysis.
- **Reviewer Opinion:** The clinical-safety twin of 0315; cheap, immediately interpretable, and hard to argue against as due diligence.

### IDEA-C-0339
- **One-sentence idea:** Evaluate methods against 1-pixel morphological perturbations of ground truth: if rankings flip, benchmarks measure annotation-style matching, not accuracy.
- **Problem:** If dilating or eroding all test masks by one pixel reorders method rankings, methods differ mainly in their systematic offset relative to an arbitrary annotation convention — a possibility never checked.
- **Core Hypothesis (falsifiable):** On boundary-sensitive metrics, single-pixel ground-truth morphology changes flip a substantial fraction of pairwise method rankings on popular benchmarks — published boundary superiority claims are largely claims about matching the annotation convention's tightness, and offset-calibrated evaluation removes the flips.
- **Why Important:** An hour-long test that separates delineation skill from convention matching across any leaderboard.
- **Why Possibly Novel:** Ground-truth-perturbation ranking-stability tests are not part of benchmarking practice.
- **Minimal Experiment:** Re-score 10 public models against {erode-1, original, dilate-1} test masks; pairwise ranking-flip statistics; offset-calibration correction.
- **Main Risk:** Some anatomy makes 1-pixel morphology ill-defined (thin structures); handle with topology-aware perturbation.

- **Survival Reason:** PROTECTED (cheap-to-falsify). Re-scoring against ±1-pixel morphological perturbations of ground truth tests whether boundary leaderboards measure delineation skill or annotation-convention matching — an afternoon-scale experiment with field-level consequences.
- **Major Risks:** Ill-defined for thin structures (needs topology-aware perturbation); flips may concentrate in a few metrics, narrowing the claim.
- **Unresolved Questions:** Flip rates across benchmarks and metrics; whether per-model signed-offset calibration (using 0218's bias fields) stabilizes rankings.
- **Required Experiments:** Re-scoring 10 public models against {erode-1, original, dilate-1} test masks; pairwise ranking-flip statistics; offset-calibrated re-evaluation; topology-aware handling of thin structures.
- **Reviewer Opinion:** Dataset-batch merge flag; with 0321 and 0210 it completes the evaluation-integrity core of this survivor set.

### IDEA-C-0340
- **One-sentence idea:** Perform compute-matched re-comparison: give baselines the proposed method's full compute (including hyperparameter search) and measure surviving gains for a sample of papers.
- **Problem:** Proposed methods receive development-time tuning that baselines never get; the implicit assumption — reported gaps reflect methods, not budget asymmetry — is the field's most consequential untested claim.
- **Core Hypothesis (falsifiable):** When baselines receive equal total compute (training plus documented search budget), a substantial fraction of sampled published gaps shrink below significance — with shrinkage predicted by the original paper's search-budget asymmetry, quantifying the field's systematic method-inflation factor.
- **Why Important:** Produces the correction coefficient everyone suspects exists; changes how reviewers and readers should discount reported gains.
- **Why Possibly Novel:** Budget-matched meta-replication with an inflation-factor estimate has not been executed for dense prediction.
- **Minimal Experiment:** Sample 8 recent comparisons with public code; re-tune baselines under matched budgets; surviving-gain analysis with pre-registered protocol.
- **Main Risk:** Budget accounting from papers is incomplete; use conservative (favor-the-paper) budget estimates.

---

*End of Batch C: 340 ideas (IDEA-C-0001 … IDEA-C-0340).*

- **Survival Reason:** Compute-matched re-comparison estimating the field's systematic method-inflation factor is the meta-scientific capstone of the batch: the correction coefficient everyone suspects exists, measured.
- **Major Risks:** Budget accounting from papers is incomplete (use conservative, favor-the-paper estimates); re-tuning baselines is expensive; reception will be contentious.
- **Unresolved Questions:** The magnitude of the inflation factor; whether shrinkage is predicted by the original papers' search-budget asymmetry as hypothesized.
- **Required Experiments:** Sample of 8 recent public-code comparisons under a pre-registered sampling rule; matched-budget baseline re-tuning including documented search; surviving-gain analysis and inflation-factor estimate.
- **Reviewer Opinion:** Heavier than the other C12 keeps, but it converts a community grumble into a number; pre-registration is non-negotiable for credibility.

---
