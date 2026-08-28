# Stage 2 — Cluster C Survivors

**Reviewer:** Cloud Sub-Agent F (independent reviewer), reporting to Supervisor Windows7
**Source:** `stage1_cluster_C_ideas.md` / `stage1_cluster_C_index.csv` (branch `cursor/stage1-cluster-c-ideas-8c7f`), 372 ideas
**Result:** 70 KEEP + 15 PROTECTED = 85 survivors; 287 killed.

## Method

Every idea was scored 1–5 on 14 dimensions (see `stage2_cluster_C_scores.csv`): novelty, significance, scientific question, technical soundness, feasibility, compute cost efficiency (5 = cheapest), dataset availability, baseline availability, likelihood already published (inverted into `not_already_published`, 5 = safest), experimental clarity, venue potential (CVPR/ICCV/ECCV/MICCAI), risk level (5 = riskiest; deliberately excluded from the composite), potential upside, and research ROI. The composite is the mean of the 13 positive dimensions.

**Selection was NOT by composite mean alone.** Decisions combined: (1) kill rules — likely-published, trope-adjacent (CLIP+SAM stacking / add-LLM-to-X / diffusion-augmentation-without-mechanism), infeasible-at-budget, vague novelty; (2) a protected set exempt from mean-ranking: high-risk high-reward bets, simple counter-intuitive claims, cheaply falsifiable claims, and disagreement-prone claims; (3) portfolio balance across the 13 sub-clusters; (4) redundancy resolution — where siblings tested the same underlying question, only the crisper instrument survived.

Protected ideas are marked **[PROTECTED: category]** and were retained even where composite, risk, or cost would have ranked them below the cut.

---

## VLM-DENSE (9 survivors)

### C-0002 — **[PROTECTED: counter-intuitive,cheaply-falsifiable]** (composite 4.46, risk 3/5)
- **Idea:** Claim that in fine-tuned open-vocabulary segmentation, replacing CLIP text embeddings with a frozen random orthogonal matrix of class vectors loses almost nothing, showing "language priors" contribute far less than advertised.
- **Why it survives:** random-orthogonal class vectors vs text embeddings is a one-week control experiment that could deflate the entire language-prior narrative for seen-class open-vocab segmentation

### C-0004 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Show that in "segmenting" multimodal LLMs, localization quality of hidden states monotonically degrades through LLM layers, so the best mask queries come from the earliest fusion layers, contradicting the "deep reasoning improves grounding" narrative.
- **Why it survives:** layer-wise localization probing inside pixel-grounding VLMs is unplowed, cheap on frozen models, and directly redesigns LISA-style architectures if the early-layer peak holds

### C-0005 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Test whether the gains attributed to language guidance in VLM-based dense predictors are mostly reproduced by simply running the vision encoder at the higher resolution these pipelines quietly adopt.
- **Why it survives:** resolution/TTA-matched vision-only baseline is the missing attribution control for language-guided dense claims; clean falsifiable confound test

### C-0007 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Show that elaborate prompt templates ("a photo of a {} in a scene") improve open-vocabulary segmentation only by shifting per-class logit priors, and a 1-parameter-per-class bias fitted on a handful of images matches them.
- **Why it survives:** reducing prompt engineering to a 1-parameter-per-class logit bias is cheap, crisp, and would kill a whole subgenre of prompt-template papers

### C-0009 — KEEP (composite 4.00, risk 3/5)
- **Idea:** Attribute the chronically blurry boundaries of VLM-based segmenters to spectral aliasing introduced by strided patch embedding, and show an anti-aliased (blur-pooled, overlapping) patch stem fixes boundaries without touching attention.
- **Why it survives:** spectral-aliasing account of blurry VLM boundaries has a concrete mechanism plus an anti-aliased patch-stem fix; strong CVPR-style analysis+method package

### C-0014 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Show that the family of training-free attention modifications (value-value attention, self-self attention, correlation reweighting) used to make CLIP segment is functionally equivalent to simple spatial smoothing of the patch-text similarity map.
- **Why it survives:** unifying the zoo of training-free CLIP-segmentation attention hacks as spatial smoothing is a cheap equivalence proof that would reorganize a noisy subfield

### C-0022 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Claim that at fixed compute, the mIoU variance across feature-upsampling strategies (bilinear, JBU, learned guided filters) exceeds the variance across frozen VLM backbones, inverting the field's attention allocation.
- **Why it survives:** variance-decomposition showing upsampler choice outweighs backbone choice at fixed compute inverts the field's attention allocation; cheap and immediately actionable

### C-0028 — **[PROTECTED: high-risk-high-reward]** (composite 3.62, risk 5/5)
- **Idea:** Attribute the emergence of patch-level alignment in contrastive VLMs to the statistics of hard negatives within batches (co-occurring concepts forcing spatial disambiguation), predicting that batch composition manipulation alone can create or destroy dense grounding.
- **Why it survives:** batch-composition as the causal origin of dense grounding in contrastive VLMs; expensive and may fail but success rewrites how dense alignment is trained

### C-0029 — KEEP (composite 4.08, risk 3/5)
- **Idea:** Validate (or refute) the implicit assumption that cheap frozen-feature segmentation probes rank backbones the same way full fine-tuning does, which underlies nearly all "foundation model dense benchmark" papers.
- **Why it survives:** validating whether frozen-probe rankings predict full fine-tuning rankings underwrites the entire foundation-model-benchmark genre; expensive but foundational


## VLM-ARCH (7 survivors)

### C-0033 — KEEP (composite 4.23, risk 2/5)
- **Idea:** Show that the MLP-vs-QFormer-vs-cross-attention projector debate in VLM assembly is confounded by output token count, and at matched visual token budget all projectors perform equivalently.
- **Why it survives:** token-count-matched projector comparison is the missing control in the MLP-vs-QFormer debate; cheap decisive design study

### C-0036 — KEEP (composite 4.00, risk 2/5)
- **Idea:** Test whether the gains from unfreezing vision encoders during VLM training are reproduced by tuning only LayerNorm/bias parameters, implying the encoder learns no genuinely new features during multimodal alignment.
- **Why it survives:** LayerNorm/bias-only tuning reproducing full encoder unfreezing would show multimodal alignment learns no new visual features; cheap with immediate training-recipe consequences

### C-0039 — KEEP (composite 3.92, risk 3/5)
- **Idea:** Show that compositional failures of LLaVA-class models (attribute binding, word order) are inherited from the vision encoder's contrastively-trained feature geometry, not from the LLM, by swapping encoders with different composition sensitivity.
- **Why it survives:** encoder-swap causal test of whether compositional failures are inherited from contrastive feature geometry cleanly splits blame between towers

### C-0047 — **[PROTECTED: counter-intuitive,cheaply-falsifiable]** (composite 4.31, risk 4/5)
- **Idea:** Test whether the raster-scan serialization of visual patches — an arbitrary choice — measurably biases VLM spatial reasoning (e.g., better horizontal than vertical relations) and whether Hilbert-curve or column-major orders shift the bias predictably.
- **Why it survives:** raster-scan serialization as a hidden spatial-reasoning bias is a delightfully simple unasked question; either result is informative

### C-0051 — KEEP (composite 4.00, risk 3/5)
- **Idea:** Document a perception-interference effect where, holding the vision tower and tuning data constant, larger LLM decoders perform worse on purely perceptual tasks because stronger language priors override visual evidence more aggressively.
- **Why it survives:** perception-interference law (bigger LLM decoder = worse pure perception) is counter-intuitive and disagreement-prone with a clean scale-series test

### C-0058 — KEEP (composite 4.38, risk 2/5)
- **Idea:** Attribute a specific, predictable class of OCR errors in VLMs (digit substitutions, decimal misplacements) to subword tokenization of numerals in the language decoder rather than to visual encoding limits.
- **Why it survives:** attributing digit-substitution OCR errors to numeral subword tokenization is a crisp cheap causal split (retokenize and compare) with direct fix implications

### C-0060 — KEEP (composite 4.00, risk 3/5)
- **Idea:** Test the "platonic representation" hypothesis concretely by transplanting a projector trained for encoder-A/LLM-B into encoder-C/LLM-B after only a cheap linear stitch, predicting near-full performance if semantic geometries are truly convergent.
- **Why it survives:** projector-transplant test of the platonic-representation hypothesis converts a philosophical debate into a cheap stitching experiment


## FT-INSTAB (7 survivors)

### C-0064 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Show that most catastrophic forgetting during instruction/multimodal fine-tuning is caused by drift of embedding and unembedding matrices rather than changes in transformer blocks, so freezing those two matrices retains generality at no adaptation cost.
- **Why it survives:** locating catastrophic forgetting in embedding/unembedding drift with a freeze fix is cheap, mechanistic, and immediately actionable for multimodal fine-tuning

### C-0068 — KEEP (composite 4.38, risk 2/5)
- **Idea:** Show that the rapid feature destruction in the first steps of full fine-tuning is driven by cold-started Adam statistics (huge effective steps), and warm-starting optimizer state removes most of the LoRA-vs-full-FT forgetting gap.
- **Why it survives:** cold-Adam-statistics account of early-fine-tuning feature destruction plus optimizer warm-start fix is a cheap mechanism experiment attacking the LoRA-vs-full-FT folklore

### C-0069 — KEEP (composite 4.23, risk 2/5)
- **Idea:** Localize fine-tuning loss spikes to gradient amplification through LayerNorm/RMSNorm scale parameters in low-loss regions, and show that a reduced lr on norm parameters alone eliminates spikes without slowing adaptation.
- **Why it survives:** LayerNorm-scale gradient amplification as the spike mechanism with a targeted norm-lr fix; falsifiable and of broad practical value

### C-0074 — KEEP (composite 3.85, risk 3/5)
- **Idea:** Test whether a weight-space EMA of an unstable fine-tuning run silently tracks a high-quality solution even through loss spikes, implying spikes are excursions around a sound mean trajectory rather than trajectory derailments.
- **Why it survives:** EMA-tracks-a-sound-trajectory-through-spikes reframes spikes as excursions not derailments; nearly free to test on any unstable run

### C-0076 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Establish that unfreezing the vision encoder during VLM training has a phase boundary: unfreezing before the projector converges causes irreversible representation collapse, while after it, unfreezing is uniformly safe — turning two-stage folklore into a measurable criterion.
- **Why it survives:** converting two-stage unfreezing folklore into a measurable phase boundary (projector convergence) gives the community a criterion instead of a superstition

### C-0077 — **[PROTECTED: counter-intuitive,disagreement-prone]** (composite 3.62, risk 4/5)
- **Idea:** Test the counterintuitive hypothesis that models pretrained on aggressively filtered, high-quality data are more brittle under fine-tuning (narrower stable-lr range, more forgetting) because their representations are sharper and less redundant.
- **Why it survives:** curated high-quality pretraining data producing more brittle fine-tuning inverts the data-quality gospel; risky but high information value either way

### C-0090 — KEEP (composite 4.23, risk 3/5)
- **Idea:** Test why interleaving text-only batches during multimodal fine-tuning prevents language-capability forgetting: the standard rehearsal-content explanation vs. the hypothesis that any gradient of matched scale on the language pathway (even from random text) rebalances update norms and prevents drift.
- **Why it survives:** random-text-vs-real-text rehearsal cleanly separates content-rehearsal from gradient-scale-rebalancing explanations of multimodal forgetting; counter-intuitive if random text suffices


## REP-LEARN (9 survivors)

### C-0091 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Demonstrate that linear-probe accuracy — the field's default representation-quality metric — fails to predict how useful features are to realistic nonlinear heads under distribution shift, and propose a "tunability probe" that does.
- **Why it survives:** showing linear probes mispredict nonlinear-head utility under shift, plus a tunability probe replacement, attacks the field's default representation metric with a constructive fix

### C-0093 — **[PROTECTED: disagreement-prone]** (composite 3.85, risk 4/5)
- **Idea:** Test the assumed harm of dimensional collapse in contrastive learning by constructing models with controlled effective ranks and showing transfer performance is flat over a wide collapse range.
- **Why it survives:** flat transfer across a wide controlled range of dimensional collapse would contradict a whole diagnostics literature; controlled-rank construction is the hard risky part

### C-0095 — KEEP (composite 3.92, risk 3/5)
- **Idea:** Show that whether a model is pretrained with CLS-token or mean-pooled objectives — usually treated as an implementation detail — determines the gradient distribution over patches and thereby the dense-task quality of patch tokens, independent of the objective family.
- **Why it survives:** CLS-vs-mean-pool pretraining as the hidden determinant of patch-token dense quality is a concrete overlooked mechanism testable with matched pretraining pairs

### C-0096 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Explain the puzzle that masked-image-modeling features probe poorly but fine-tune excellently by showing their advantages live in high-frequency, nonlinearly-coded components that linear probes cannot read but fine-tuning can exploit.
- **Why it survives:** explains the MIM probe-badly/finetune-well puzzle via high-frequency nonlinearly-coded components; resolves a genuine standing anomaly with clear probes

### C-0099 — **[PROTECTED: disagreement-prone,cheaply-falsifiable]** (composite 4.54, risk 3/5)
- **Idea:** Show that after simple feature whitening at transfer time, the performance differences among major SSL methods (contrastive, distillation, redundancy-reduction) largely vanish, implying much of the method literature differs in second-moment structure, not information content.
- **Why it survives:** whitening-at-transfer erasing SSL method differences would collapse much of the objective-design literature into second-moment bookkeeping; cheap and explosive

### C-0103 — KEEP (composite 3.92, risk 3/5)
- **Idea:** Test whether the celebrated superiority of modern SSL (DINOv2-style) over supervised pretraining survives when supervised training is given equal data scale via weak labels, modern augmentation, and matched schedules — or whether "SSL is better" is a data-scale confound.
- **Why it survives:** SSL-vs-supervised at matched data scale via weak labels is the missing confound test under the DINOv2-era consensus; expensive but decision-relevant for the whole field

### C-0109 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Show that rare/tail classes are well represented in frozen-feature geometry (recoverable with few-shot exemplar matching) even when linear probes trained on the full imbalanced distribution fail them, relocating the long-tail problem from representation to readout.
- **Why it survives:** relocating the long-tail problem from representation to readout (tail classes recoverable few-shot from frozen geometry) redirects a large literature; cheap frozen-feature study

### C-0113 — **[PROTECTED: cheaply-falsifiable,counter-intuitive]** (composite 4.46, risk 3/5)
- **Idea:** Test how much head training actually contributes on top of modern frozen backbones by comparing trained MLP heads against frozen random-feature heads (random MLP + linear readout), predicting near-parity that exposes "head engineering" as low-value on strong features.
- **Why it survives:** frozen random-MLP heads matching trained heads on strong features is a days-cheap test that would deflate head-engineering papers

### C-0118 — KEEP (composite 4.08, risk 3/5)
- **Idea:** Overturn the universal discard-the-projector convention by showing projector features are superior for fine-grained and instance-level transfer, because the projector holds the invariances while the backbone retains nuisance detail — the standard story backwards for a class of tasks.
- **Why it survives:** projector-features-better-for-fine-grained inverts the universal discard-the-projector convention with a clear task-split prediction; cheap frozen-feature test


## GEN4SEG (7 survivors)

### C-0123 — KEEP (composite 4.00, risk 3/5)
- **Idea:** Run the missing controlled comparison — generative (diffusion) vs. discriminative (contrastive) pretraining at strictly matched data, compute, and architecture — to isolate what generative pretraining actually adds for dense prediction.
- **Why it survives:** strictly matched generative-vs-discriminative pretraining for dense prediction is the missing controlled comparison the whole diffusion-features debate rests on; expensive but definitive

### C-0125 — **[PROTECTED: counter-intuitive]** (composite 4.00, risk 4/5)
- **Idea:** Test whether image restoration (denoising) removes informative signal — sensor noise correlates with materials, depth, and lighting — such that segmentation on restored images is worse than on raw noisy images for models trained appropriately.
- **Why it survives:** restoration-removes-informative-signal (raw noisy beats denoised for appropriately trained segmenters) inverts the restore-then-analyze dogma; cheap enough to falsify quickly

### C-0126 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Show that reported gains from adding diffusion-generated training images to segmentation datasets are mostly reproduced by reweighting/oversampling the real data to the same class-frequency profile the synthetic data induces.
- **Why it survives:** reproducing diffusion-augmentation gains by reweighting real data to the induced class-frequency profile is the mechanism-test that the synthetic-data genre owes the community

### C-0128 — KEEP (composite 4.00, risk 2/5)
- **Idea:** Use inversion-based object insertion/removal to build counterfactual scene pairs and measure, causally, how much modern segmenters rely on context vs. local evidence per class — replacing correlational context studies.
- **Why it survives:** inversion-based counterfactual scene pairs turn correlational context studies into causal per-class context-reliance measurements; strong benchmark-free instrument

### C-0129 — KEEP (composite 4.00, risk 2/5)
- **Idea:** Characterize systematically when text-to-image attention maps used to auto-generate image-mask training pairs produce corrupted supervision ("attention leakage" onto associated regions like shadows and reflections), yielding quantitative laws of where free synthetic mask data can be trusted.
- **Why it survives:** quantitative failure laws for attention-derived synthetic masks (leakage onto shadows/reflections) tells the field exactly where free mask supervision can be trusted

### C-0145 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Test whether reported gains from super-resolving inputs for small-object detection vanish when the detector is simply trained and run at the matched effective resolution, exposing SR as an expensive resampling operator in this role.
- **Why it survives:** SR-for-small-objects vs matched-effective-resolution training is a clean deflation with direct deployment consequences for aerial/medical pipelines

### C-0148 — KEEP (composite 3.85, risk 3/5)
- **Idea:** Develop and validate a falsifiable decision rule: generative augmentation improves a segmentation task if and only if a measurable mode-coverage gap exists between the real training set and the target distribution that the generator demonstrably covers.
- **Why it survives:** a falsifiable if-and-only-if decision rule (mode-coverage gap) for when generative augmentation helps replaces anecdote with mechanism; exactly the anti-trope study the area needs


## LLM-ANNOT (6 survivors)

### C-0154 — KEEP (composite 4.00, risk 2/5)
- **Idea:** Demonstrate that optimizing annotation-guideline prompts for LLM annotators shifts the resulting label distributions in ways that materially change trained-model behavior — making "ground truth" an artifact of prompt engineering choices that are never reported.
- **Why it survives:** guideline-prompt choices materially shifting trained-model behavior makes ground truth an unreported experimenter degree of freedom; cheap and unsettling

### C-0157 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Test the claim that requiring chain-of-thought rationales improves LLM annotation accuracy, hypothesizing instead that rationales leave accuracy unchanged but make erroneous labels much easier to detect post-hoc (by humans or auditor models).
- **Why it survives:** rationales-do-not-improve-but-make-errors-auditable is a crisp dissociation with direct annotation-pipeline consequences; cheap

### C-0158 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Show that classic active learning breaks under LLM annotation because uncertainty-based acquisition preferentially selects exactly the items where LLM labels are least reliable, creating a feedback loop that concentrates label noise where the student is most sensitive.
- **Why it survives:** uncertainty-based acquisition selecting exactly the items where LLM labels fail breaks classic active learning under machine annotation; feedback-loop mechanism is precise and testable

### C-0159 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Demonstrate that established noisy-label learning methods, built for (conditionally) independent human noise, systematically fail on LLM-annotated data whose errors are confident, correlated, and prior-structured — and characterize the new noise model needed.
- **Why it survives:** confident correlated prior-structured LLM label noise violating the assumptions of the entire noisy-label literature is a foundational negative result with a constructive new noise model

### C-0170 — KEEP (composite 4.00, risk 2/5)
- **Idea:** Measure the "self-generated easiness" effect: referring expressions, questions, and captions produced by VLMs for benchmark construction are systematically easier for VLMs to solve than human-authored equivalents on the same images, inflating reported progress.
- **Why it survives:** self-generated-easiness (machine-authored benchmarks are easier for machines) quantifies a circularity that inflates reported progress; cheap paired-design test

### C-0179 — KEEP (composite 4.08, risk 3/5)
- **Idea:** Test for lineage bias in machine-annotated benchmarks: evaluation sets labeled by a model family systematically advantage later models of that family (shared priors, formats, blind spots) over equally capable models from other lineages.
- **Why it survives:** lineage bias (benchmarks labeled by a model family advantaging that family's descendants) is a fresh structural threat to evaluation validity as machine annotation becomes standard


## EMP-PHEN (7 survivors)

### C-0188 — KEEP (composite 4.46, risk 2/5)
- **Idea:** Quantify the underappreciated instability whereby segmentation outputs for a fixed image change depending on what other images share its inference batch (through batch normalization or cross-batch statistics), violating the implicit determinism assumption of evaluation and deployment.
- **Why it survives:** batch-composition-dependent segmentation outputs violate the determinism assumption of evaluation and deployment; trivially cheap to demonstrate and practically alarming

### C-0190 — KEEP (composite 4.23, risk 2/5)
- **Idea:** Document a monotonic rise in error correlation across independently developed vision models over the last decade — an emerging monoculture where new models make the same mistakes — and quantify its consequences for ensembling and benchmark headroom.
- **Why it survives:** rising cross-model error correlation (model monoculture) quantifies a systemic risk to ensembling and benchmark headroom nobody tracks; historical-checkpoint study is feasible

### C-0193 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Establish that per-pixel segmentation decisions stabilize at characteristic depths (easy interior pixels early, boundary/rare-class pixels late), and exploit this "pixel prediction depth" phenomenon for adaptive-compute segmentation with per-pixel early exits.
- **Why it survives:** per-pixel prediction-depth phenomenon plus early-exit exploitation gives both a scientific observation and a practical adaptive-compute segmentation method

### C-0200 — **[PROTECTED: high-risk-high-reward,counter-intuitive]** (composite 3.85, risk 5/5)
- **Idea:** Test whether a fixed random initialization that performs well on one dataset also performs well on unrelated datasets and tasks — i.e., "lucky inits" are init-intrinsic rather than init-task matches — with implications for init reuse as a free performance lever.
- **Why it survives:** init-intrinsic lucky initializations would create a free reusable performance lever and contradict init-as-noise orthodoxy; likely null but cheap enough to gamble

### C-0204 — **[PROTECTED: high-risk-high-reward,disagreement-prone]** (composite 3.62, risk 5/5)
- **Idea:** Test the contrarian hypothesis that certain training loss spikes are followed by measurable *improvements* in generalization relative to spike-free counterfactual trajectories — spikes as basin-escaping exploration rather than pure pathology.
- **Why it survives:** spikes-as-beneficial-exploration contradicts the universal spikes-are-pathology assumption; needs careful counterfactual trajectories but a positive result changes training practice

### C-0207 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Show that learned positional embeddings absorb dataset-specific spatial priors (sky-up, subjects-centered, ground-below) that measurably help ID performance but systematically harm transfer to rotated, aerial, or unconventional-framing domains — PEs as a hidden bias store.
- **Why it survives:** learned positional embeddings as a hidden store of dataset spatial priors, with predictable transfer harm to aerial/rotated domains, is a fresh testable locus of bias

### C-0210 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Show that fine-tuning batch size systematically trades in-distribution accuracy against OOD robustness even when runs are matched on ID validation loss — small batches buy robustness with noise — making batch size a hidden robustness hyperparameter reported by nobody.
- **Why it survives:** batch size silently trading ID accuracy against OOD robustness at matched validation loss would expose an unreported hyperparameter confound across the literature


## ASSUMP (4 survivors)

### C-0214 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Decompose the celebrated benefit of pretraining on larger-vocabulary datasets (21k classes vs. 1k) to test whether gains derive from label-space richness or simply from more images, by ablating vocabulary at fixed image count.
- **Why it survives:** vocabulary-richness vs image-count decomposition of 21k-pretraining gains is a clean unrun ablation behind a default community belief

### C-0219 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Characterize the regime where few-shot fine-tuning of foundation models *underperforms* their own zero-shot behavior — testing the default assumption that any labeled target data should be used for adaptation.
- **Why it survives:** mapping the regime where few-shot fine-tuning underperforms zero-shot challenges the always-adapt default with direct practitioner consequences

### C-0229 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Decompose multi-task pretraining benefits by comparing multi-task models against single-task models trained on the *pooled images* (with only one task's labels), testing the assumption that task diversity itself — rather than image diversity — improves representations.
- **Why it survives:** multi-task-vs-pooled-images decomposition isolates whether task diversity itself improves representations; a clean unrun control behind multi-task folklore

### C-0240 — KEEP (composite 4.08, risk 3/5)
- **Idea:** Challenge the accepted claim that freezing pretrained backbones (or linear probing) preserves OOD robustness better than fine-tuning, by testing whether the effect is an artifact of measuring robustness on shifts aligned with the pretraining distribution — with the conclusion reversing on shifts aligned with the target task.
- **Why it survives:** freezing-preserves-robustness as an artifact of pretraining-aligned shift choices, with predicted reversal on task-aligned shifts, directly attacks a celebrated finding; disagreement-prone with a clean 2x2 design


## NEG-HYP (6 survivors)

### C-0247 — KEEP (composite 4.08, risk 3/5)
- **Idea:** Predict a null for the widespread practice of masked-autoencoder self-pretraining on small domain-specific corpora (tens of thousands of medical/aerial images) before fine-tuning, against simply fine-tuning a general checkpoint or training from scratch with strong augmentation.
- **Why it survives:** null for small-corpus domain-specific MAE pretraining vs general-checkpoint fine-tuning attacks a default recipe across medical/aerial imaging; strong MICCAI relevance either way

### C-0248 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Test the null that distilling an ensemble into a single student transfers its accuracy but not its OOD robustness or calibration — the properties for which ensembles are actually valued — making "distill the ensemble" a false economy for reliability purposes.
- **Why it survives:** ensemble distillation transferring accuracy but not the robustness/calibration that ensembles are valued for exposes a false economy in reliability engineering

### C-0251 — KEEP (composite 3.85, risk 3/5)
- **Idea:** Predict that multi-view (>2) contrastive formulations provide no representation-quality benefit over standard two-view training at matched compute, with multi-crop's celebrated gains attributable entirely to its resolution asymmetry, not view count.
- **Why it survives:** multi-crop gains attributed to resolution asymmetry rather than view count is a precise mechanism null against a canonized SSL component

### C-0262 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Test the null that mixup's celebrated calibration improvement is entirely reproducible by temperature scaling a mixup-free model — i.e., mixup changes confidence scale, not the confidence-accuracy relationship's informativeness.
- **Why it survives:** mixup-calibration-equals-temperature-scaling is a days-cheap equivalence test that would delete a standard claim from the augmentation literature

### C-0265 — **[PROTECTED: disagreement-prone,cheaply-falsifiable]** (composite 4.38, risk 3/5)
- **Idea:** Test the null that chain-of-thought prompting improves multimodal *perception* accuracy (recognition, counting, OCR, localization), as opposed to multi-step reasoning tasks — predicting zero or negative effects because verbalization cannot add visual information and may overwrite it with priors.
- **Why it survives:** CoT-null-or-negative-for-perception cuts against the reasoning-helps-everything current; cheap benchmark sweep with high argument value either way

### C-0270 — KEEP (composite 4.23, risk 2/5)
- **Idea:** Test the null that the universal practice of filtering pseudo-labels by confidence threshold selects no better than randomly keeping the same volume of pseudo-labels, because confidence correlates with easiness in ways that make retained labels redundant rather than informative.
- **Why it survives:** confidence-thresholded pseudo-label selection performing no better than volume-matched random retention attacks the core operator of semi/self-supervised pipelines with a trivial control


## EVAL-FAIL (6 survivors)

### C-0274 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Quantify how much open-vocabulary segmentation/detection evaluation, which requires predicting the benchmark's exact class-name token, penalizes semantically correct predictions (synonyms, hypernyms), and show that semantic-similarity-aware scoring changes method rankings.
- **Why it survives:** quantifying the exact-class-name penalty and showing semantic-similarity-aware scoring reorders open-vocabulary methods fixes a known-broken but unmeasured evaluation convention

### C-0276 — KEEP (composite 4.23, risk 2/5)
- **Idea:** Document how nominally identical benchmarks (ADE20K, Cityscapes, COCO variants) exist in silently divergent versions across codebases — different label mappings, ignored-class conventions, split files, and annotation revisions — and quantify the cross-paper comparability error this creates.
- **Why it survives:** documenting silently divergent versions of nominally identical benchmarks across codebases quantifies a comparability error the whole field silently absorbs

### C-0279 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Quantify the fraction of claimed state-of-the-art margins in segmentation/detection attributable to inference-time protocol choices (multi-scale testing, flipping, sliding-window overlap, threshold tuning) rather than to the proposed methods, via a protocol-normalized re-evaluation of recent leaderboard entries.
- **Why it survives:** protocol-normalized re-evaluation quantifying how much of recent SOTA margins is inference-time protocol rather than method is high-leverage hygiene for the whole leaderboard economy

### C-0285 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Audit the open secret that "zero-shot" cross-dataset segmentation/detection evaluations use hyperparameters (score thresholds, mask-fusion settings, prompt templates) tuned on the target benchmark, quantifying how much reported zero-shot performance depends on this hidden supervision.
- **Why it survives:** auditing hidden target-benchmark hyperparameter tuning inside zero-shot cross-dataset claims measures how much of reported zero-shot is quiet supervision

### C-0293 — KEEP (composite 4.54, risk 1/5)
- **Idea:** Show that per-class IoU estimates for rare classes in standard benchmarks rest on so few test regions that their confidence intervals span several points of mIoU, and a substantial fraction of claimed improvements is attributable to statistically insignificant rare-class fluctuations.
- **Why it survives:** rare-class IoU confidence intervals spanning multiple mIoU points would reclassify a fraction of claimed SOTA margins as noise; a weekend of bootstrap statistics with field-wide consequences

### C-0300 — KEEP (composite 4.15, risk 3/5)
- **Idea:** Estimate the aggregate false-discovery rate of one year of segmentation/detection SOTA claims by systematically re-running a random sample of published improvements with proper seed statistics, matched tuning, and held-out evaluation — turning meta-scientific criticism into a measured quantity.
- **Why it survives:** a measured false-discovery rate for a year of segmentation/detection SOTA claims converts meta-scientific complaint into a number the field must answer; expensive but flagship-grade


## ROBUST (6 survivors)

### C-0302 — KEEP (composite 3.69, risk 3/5)
- **Idea:** Test whether the celebrated finding that spurious correlations live in the last layer (fixable by last-layer retraining) breaks down for dense prediction, where spurious cues (context textures, co-occurring backgrounds) are spatially entangled with features throughout the network.
- **Why it survives:** last-layer-retraining (spurious-cues-live-in-the-last-layer) breaking down for dense prediction attacks a celebrated finding exactly where its assumptions (spatial entanglement) fail

### C-0310 — KEEP (composite 3.85, risk 3/5)
- **Idea:** Quantify the sensitivity of recognition/segmentation models to camera image-signal-processor (ISP) parameters — demosaicing, tone mapping, sharpening, denoising — by re-rendering RAW captures under controlled ISP variation, testing whether ISP shift causes degradation comparable to or exceeding celebrated environmental shifts.
- **Why it survives:** ISP-parameter sensitivity via RAW re-rendering opens a robustness axis (the camera pipeline) the field treats as invisible; fresh with hardware-aware deployment stakes

### C-0312 — KEEP (composite 4.38, risk 2/5)
- **Idea:** Show that distribution shift induces systematic *directional* prediction bias (toward frequent, contextually expected classes) rather than symmetric accuracy loss, meaning rare and safety-critical classes vanish from predictions first — a failure structure aggregate robustness metrics cannot see.
- **Why it survives:** directional prediction bias under shift (rare/safety classes vanish first) exposes a failure structure aggregate robustness metrics cannot see; cheap re-analysis of existing shifted benchmarks

### C-0320 — KEEP (composite 4.15, risk 2/5)
- **Idea:** Measure robustness under *combinations* of individually mild corruptions (slight blur + slight noise + slight color shift), testing the hypothesis that degradation composes super-linearly — real-world conditions are compositions, and single-axis benchmarks systematically understate deployed risk.
- **Why it survives:** super-linear composition of individually mild corruptions directly indicts single-axis robustness benchmarks with a cheap factorial design

### C-0325 — KEEP (composite 4.38, risk 2/5)
- **Idea:** Demonstrate that segmentation models under shift can maintain respectable mIoU while entire object instances vanish from predictions — pixel- and instance-level robustness decouple — and introduce instance-survival metrics that expose safety-relevant failures aggregate metrics miss.
- **Why it survives:** pixel-vs-instance robustness decoupling (whole instances vanish at stable mIoU) plus instance-survival metrics is a safety-relevant blind spot with a cheap measurement fix

### C-0330 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Show that selective-prediction (abstention) mechanisms tuned in-distribution invert under shift — the model abstains on hard-but-solvable ID-like items while confidently answering the shifted items it gets wrong — and establish shift-robust abstention evaluation as a required reporting standard.
- **Why it survives:** abstention mechanisms inverting under shift (confident on wrong shifted items, abstaining on solvable ID items) breaks the safety story selective prediction is sold on


## GENERAL (8 survivors)

### C-0332 — KEEP (composite 4.31, risk 2/5)
- **Idea:** Test whether the celebrated linear ID-OOD accuracy relationship — which underpins how the field interprets robustness interventions — holds for segmentation and detection, where spatial error structure and per-class coupling could break the law.
- **Why it survives:** testing whether the ID-OOD linear accuracy law survives structured dense-prediction errors determines whether the field's main robustness interpretive tool applies to segmentation at all

### C-0334 — KEEP (composite 4.08, risk 4/5)
- **Idea:** Test the parsimony hypothesis that texture bias, shortcut learning, and adversarial vulnerability — treated as three literatures — are manifestations of one measurable quantity (the model's effective spectral/simplicity bias), such that a single intervention moves all three predictably.
- **Why it survives:** unifying texture bias, shortcut learning, and adversarial vulnerability under one measurable spectral-simplicity quantity is a high-upside consolidation bet with a concrete single-intervention prediction

### C-0338 — KEEP (composite 4.00, risk 3/5)
- **Idea:** Establish that models compose visual concepts (attribute-object, object-context) exactly as far as the compositional statistics of training data allow — a measurable "visual n-gram" law — reframing compositional failure from an architecture problem to a data-statistics bound.
- **Why it survives:** a visual n-gram law bounding compositional generalization by training-data co-occurrence statistics would reframe compositionality from architecture problem to data-statistics bound

### C-0343 — **[PROTECTED: disagreement-prone]** (composite 4.08, risk 4/5)
- **Idea:** Test whether the widely studied neural-collapse geometry (simplex ETF structure of last-layer features) has any causal relevance to generalization by training models with collapse explicitly prevented and showing unchanged downstream behavior.
- **Why it survives:** preventing neural collapse and observing unchanged generalization would demote a hot theoretical literature to epiphenomenon status; constructing collapse-free-but-matched training is the hard risky part

### C-0348 — KEEP (composite 4.15, risk 4/5)
- **Idea:** Measure the "underspecification volume" of modern training pipelines — how differently identically-scoring models can behave OOD — across model scale, testing the uncomfortable hypothesis that scale *increases* the behavioral spread of equivalent models rather than pinning it down.
- **Why it survives:** testing whether scale increases the behavioral spread of identically-scoring models (underspecification volume) is an uncomfortable high-stakes question about what scaling actually pins down

### C-0349 — KEEP (composite 4.00, risk 3/5)
- **Idea:** Quantify how much of measured cross-dataset performance drops in segmentation/detection stems from annotation-convention differences (boundary placement, class definitions, granularity, void handling) rather than image-distribution shift — by re-annotating image subsets under both conventions.
- **Why it survives:** re-annotating subsets under both conventions to split cross-dataset drops into annotation-convention vs true distribution shift would recalibrate the entire domain-generalization literature

### C-0355 — **[PROTECTED: counter-intuitive]** (composite 4.08, risk 4/5)
- **Idea:** Test the counterintuitive allocation hypothesis that adding more *head-class* data improves tail-class performance — because tail classes are recognized through compositional reuse of features refined on head classes — inverting the standard rebalancing prescription.
- **Why it survives:** more head-class data improving tail performance via compositional feature reuse inverts the rebalancing orthodoxy; a clean allocation experiment with reversal-grade upside

### C-0360 — KEEP (composite 4.08, risk 2/5)
- **Idea:** Establish that fine-grained downstream capability is bounded by a computable pretraining resolution/patch-size ceiling — features for details smaller than the effective sampling scale cannot exist and are not recoverable by fine-tuning — replacing "more data/capacity will fix it" expectations with a hard law.
- **Why it survives:** a computable pretraining resolution/patch-size ceiling on fine-grained downstream capability would replace more-scale-will-fix-it expectations with a hard law; directly relevant to medical/aerial fine detail


## WILDCARD (3 survivors)

### C-0361 — **[PROTECTED: high-risk-high-reward]** (composite 3.46, risk 5/5)
- **Idea:** Build and validate an autonomous agent pipeline that re-executes published vision experiments from paper+code artifacts, producing the first literature-scale replication census and a taxonomy of why vision results fail to reproduce.
- **Why it survives:** an autonomous literature-scale replication census is the single highest-upside meta-science bet in the catalog; likely to partially fail, transformative if it lands

### C-0365 — KEEP (composite 4.08, risk 3/5)
- **Idea:** Systematically re-test the classical segmentation toolbox (CRFs, superpixels, contour grouping, MRF priors) on top of modern foundation features, testing the hypothesis that several "obsolete" structured methods become competitive again once their unary terms are strong — a directed archaeology of discarded ideas.
- **Why it survives:** directed archaeology re-testing CRFs/superpixels/structured priors on foundation features is a cheap systematic sweep that could resurrect discarded tools now that unary terms are strong

### C-0372 — **[PROTECTED: disagreement-prone,high-risk-high-reward]** (composite 3.31, risk 5/5)
- **Idea:** Pilot adversarial collaboration — proponents and skeptics of a contested vision claim jointly preregister decisive experiments — on two live controversies (e.g., "language supervision improves dense features" and "attention is necessary at scale"), evaluating the protocol itself as a dispute-resolution instrument for the field.
- **Why it survives:** adversarial collaboration on live vision controversies is a protocol experiment the field has never run; hard to organize but success creates a reusable dispute-resolution instrument

