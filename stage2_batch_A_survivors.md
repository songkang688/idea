# Stage 2 — Batch A: Survivors (73 / 340)

**Reviewer:** independent Stage 2 reviewer, Windows5 Autonomous Research Idea Evolution.
**Selection basis:** adversarial scoring (`stage2_batch_A_scores.md`) with protection rules for high-risk/high-reward (HR), simple-but-counter-intuitive (CI), reviewer-disagreement magnets (RM), and cheap-to-falsify (CF). Original Stage 1 fields reproduced verbatim; reviewer sections added.

---

## IDEA-A-0001 — SAM follows edges, not objects
**Cluster 1 · Protect: CI · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether SAM segments *visual boundaries* rather than *semantic objects* by dissociating the two on camouflage and texture-boundary stimuli.
- **Problem:** SAM's zero-shot masks are widely treated as "object" masks, but its training signal (SA-1B) rewards boundary-consistent regions, and nobody has cleanly dissociated edge-following from objecthood.
- **Core Hypothesis (falsifiable):** SAM's mask agreement with ground truth is predicted almost entirely by local boundary gradient strength, not by object semantics; on stimuli where a strong texture edge crosses an object (or a camouflaged object has no edge), SAM will follow the edge, not the object, in >80% of cases.
- **Why Important:** Thousands of pipelines use SAM masks as object proposals; if SAM is an edge-machine, downstream semantic conclusions are systematically biased.
- **Why Possibly Novel:** Failure reports on camouflage exist, but a controlled dissociation design (edge-present/object-absent vs object-present/edge-absent quadrants) has not been published as a mechanistic claim.
- **Minimal Experiment:** Build a 500-image 2×2 stimulus set (real camouflage images + composited texture-edge overlays on COCO objects); prompt SAM with center clicks; regress mask IoU against boundary gradient energy vs semantic-class factors.
- **Main Risk:** Composited stimuli may introduce blending artifacts SAM detects, confounding the edge/object dissociation.

**Survival Reason:** The cleanest mechanistic question in the cluster: a 2×2 dissociation design that converts scattered "SAM fails on X" anecdotes into a single testable mechanism claim, at inference-only cost.
**Major Risks:** Compositing artifacts (SAM may key on blending seams); the >80% threshold is aggressive; edge energy and objecthood are correlated in natural images, so the stimulus set carries the entire causal burden.
**Unresolved Questions:** Does the verdict differ between SAM's three mask heads? Does prompt type (box vs point) shift edge-allegiance? Where do HQ-SAM-style refinements sit on the edge-vs-object axis?
**Required Experiments:** (1) 2×2 stimulus battery with artifact controls (paste real camouflage patches, not just synthetic edges); (2) IoU regression on boundary-gradient energy vs semantic factors; (3) replication across SAM variants and prompt types; (4) a small human-baseline arm to confirm objects are recoverable by people.
**Reviewer Opinion:** Keep. This is the kind of result other Batch A survivors (0006, 0128, 0154) will cite as their mechanism; even a partial effect reshapes how SAM masks are consumed as "object" proposals.

---

## IDEA-A-0003 — IoU-vs-size failure law with a patch-size knee
**Cluster 1 · Protect: CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Establish an empirical "failure law" relating object pixel size to SAM IoU and test whether the breakpoint is set by the ViT patch size (16 px).
- **Problem:** "SAM is bad at small objects" is folklore without a quantitative form; if the failure is patch-quantization-driven, it predicts a specific breakpoint and scaling.
- **Core Hypothesis (falsifiable):** SAM's mean IoU vs object diameter follows a saturating curve with a sharp knee at ~2–3 patch widths (32–48 px at 1024 input), and re-running with a hypothetical smaller-patch encoder (or higher-res tiling) shifts the knee proportionally — if the knee does not track patch size, the hypothesis is falsified.
- **Why Important:** Turns an anecdote into a design law: tells practitioners exactly when tiling/zooming is required rather than relying on trial and error.
- **Why Possibly Novel:** Size-stratified SAM evaluations exist informally, but no work has tested the patch-size causal claim by intervening on effective patch resolution.
- **Minimal Experiment:** Evaluate SAM on COCO/LVIS instances binned by diameter; repeat with 2× and 4× zoomed crops (changing object-size-in-patches while fixing semantics); check whether the IoU-vs-size curve collapses when the x-axis is measured in patches.
- **Main Risk:** Zooming changes context, which independently affects SAM; needs context-controlled crops.

**Survival Reason:** Cheap-to-falsify with a sharp quantitative prediction (curve collapse in patch units); directly complements the training-side version (0161) at near-zero compute.
**Major Risks:** Context confound under zooming; size-stratified SAM audits exist informally, so novelty rests on the intervention (curve collapse), not the observation.
**Unresolved Questions:** Does the knee shift for SAM2/Hiera and efficient-SAM distillations? Is the law prompt-type-invariant? How does annotation noise at small sizes floor the curve?
**Required Experiments:** (1) Diameter-binned evaluation on COCO/LVIS; (2) 2×/4× context-controlled zoom arms; (3) curve-collapse test in patch units with formal breakpoint fitting; (4) cross-variant replication.
**Reviewer Opinion:** Keep. A week of inference for a design law that every deployment team using SAM on small structures would cite; pairs naturally with 0161 as the inference-time half of the tokenization-floor program.

---

## IDEA-A-0006 — Amorphous-matter failure is a boundary-contrast curve
**Cluster 1 · Protect: CI · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test the hypothesis that SAM's failure on amorphous matter (smoke, clouds, water, flames) is a smooth function of boundary gradient energy going to zero, not a categorical "class" failure.
- **Problem:** SAM fails on smoke/fire, but we don't know if this is a continuous physics-driven failure (no boundary → no mask) or a semantic gap (never saw the category).
- **Core Hypothesis (falsifiable):** Across amorphous and solid objects alike, SAM IoU is monotonically predicted by a single scalar — integrated boundary contrast — and amorphous categories lie on the *same* curve as solid objects (falsified if amorphous classes fall systematically below the curve).
- **Why Important:** If failure is purely contrast-driven, cheap contrast-enhancing preprocessing could fix smoke/fire segmentation; if categorical, retraining is needed.
- **Why Possibly Novel:** Unifies "SAM fails on X" reports under one measurable physical variable with a testable single-curve prediction.
- **Minimal Experiment:** Assemble 1k masks spanning smoke/fog/fire/water/glass/solid objects with computed boundary contrast; plot IoU vs contrast per category; test category offsets with ANCOVA.
- **Main Risk:** Ground-truth masks for amorphous matter are themselves ill-defined (see IDEA-A-0121), which injects label noise into the dependent variable.

**Survival Reason:** A single-variable law that would unify a scattered failure literature and decide preprocess-vs-retrain for every amorphous domain; strong CI protection — "category failure" collapsing to physics would surprise most readers.
**Major Risks:** Dependent-variable noise from ill-posed amorphous GT (0121's point); "integrated boundary contrast" needs a robust operationalization or the curve is definitionally circular.
**Unresolved Questions:** Which contrast measure (multi-scale gradient energy? transmission proxy?) is the right x-axis? Do glass and smoke sit on the same curve or does specularity break it?
**Required Experiments:** (1) 1k-mask battery spanning six matter types with pre-registered contrast measures; (2) ANCOVA for category offsets; (3) a causal arm: contrast-enhance amorphous inputs and test predicted IoU recovery; (4) coordinate GT with the 0121/0122 density machinery.
**Reviewer Opinion:** Keep. This is the mechanistic backbone of the smoke program (0121/0122/0128); the causal contrast-enhancement arm converts a correlation paper into a strong finding either way.

---

## IDEA-A-0007 — SAM masks imprint the SA-1B annotation protocol
**Cluster 1 · Protect: RM · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Determine how much of SAM's mask granularity behavior is an imprint of the SA-1B annotation *protocol* rather than a property of images.
- **Problem:** SA-1B was built with a specific interactive annotation pipeline; SAM's notion of "a mask" may encode that pipeline's policy (e.g., preferred granularity, hole handling) rather than natural object statistics.
- **Core Hypothesis (falsifiable):** SAM's everything-mode mask-size and mask-count distributions match SA-1B's distributions far more closely than those of independently annotated datasets (ADE20K, LVIS) on the *same images*, indicating protocol imprinting.
- **Why Important:** Protocol imprinting means SAM is not a neutral "segment anything" tool but an SA-1B-policy replicator — critical for anyone using SAM masks as ground truth.
- **Why Possibly Novel:** Dataset bias is much-discussed for classes; annotation-*protocol* bias on mask granularity for a foundation model has not been quantified.
- **Minimal Experiment:** Run SAM everything-mode on images that have both LVIS and (proxy) SA-1B-style annotations; compare granularity histograms (masks per image, mask-size distribution, holes per mask) across the three sources.
- **Main Risk:** Distribution match could reflect image-domain overlap rather than protocol; control by using identical images across annotation sources.
- 
**Survival Reason:** Ecosystem-level claim with a clean same-images design: "segment anything" reframed as "replicate SA-1B's annotation policy." A reviewer-disagreement magnet — some will call it obvious, others field-critical — which is exactly the protected profile.
**Major Risks:** Constructing a faithful "SA-1B-style" annotation proxy without Meta's actual pipeline; distributional similarity is weaker evidence than per-instance agreement.
**Unresolved Questions:** Which protocol dimensions (granularity, hole policy, part/whole preference) imprint most strongly? Does fine-tuning erase or preserve the imprint (link to 0068)? Do SAM-derived datasets inherit it (link to 0029/0267)?
**Required Experiments:** (1) Everything-mode granularity histograms vs LVIS/ADE20K on identical images; (2) per-instance agreement analysis, not just marginals; (3) human study where annotators label under SA-1B-style vs free instructions (shares design with 0337); (4) inheritance check in one SAM-distilled student.
**Reviewer Opinion:** Keep, high priority. Together with 0029 and 0267 this forms the contamination trilogy — the most consequential research program in Batch A.

---
## IDEA-A-0013 — SAM2 worse than SAM1 on static fine boundaries
**Cluster 1 · Protect: CI+CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether SAM2's video-trained image encoder *lost* single-image segmentation quality relative to SAM1 — a modality trade-off audit.
- **Problem:** SAM2 is assumed to strictly supersede SAM1, but video training may have traded static-image boundary precision for temporal stability.
- **Core Hypothesis (falsifiable):** On a boundary-quality-weighted static benchmark (high-res, fine structures), SAM1 outperforms SAM2 by a measurable margin (>2 boundary-F points) despite SAM2's parity or superiority on region IoU.
- **Why Important:** Practitioners default to the newest model; if SAM2 regressed on fine static detail, single-image applications (matting, medical stills) should stay on SAM1 or use hybrids.
- **Why Possibly Novel:** No published head-to-head isolates *boundary-F on static fine structures* between SAM generations; release reports emphasize aggregate parity.
- **Minimal Experiment:** Evaluate SAM1 vs SAM2 (matched prompting) on DIS5K-style fine-structure images and high-res subsets; report boundary F-measure and IoU separately.
- **Main Risk:** Encoder architecture differences (ViT-H vs Hiera) confound "video training" as the cause; frame as model-level, not cause-level, claim unless ablations are possible.

**Survival Reason:** Newest-isn't-better is a counter-intuitive, immediately actionable claim; a week of inference falsifies it. Protected CI+CF.
**Major Risks:** Cause attribution impossible without ablations (architecture and data both changed); community may have partially noticed this in scattered comparisons.
**Unresolved Questions:** Does the regression concentrate in specific structure types (thin filaments, matting-like edges)? Does a SAM1-encoder/SAM2-decoder hybrid recover both properties?
**Required Experiments:** (1) Matched-prompt evaluation on DIS5K-class fine-structure sets; (2) separate boundary-F and region-IoU reporting; (3) resolution-ladder analysis; (4) explicit framing as model-level regression audit with a hybrid arm if feasible.
**Reviewer Opinion:** Keep. Cheap, decisive, deployment-relevant. Even a null (no regression) is a useful citable equivalence for practitioners choosing checkpoints.

---

## IDEA-A-0021 — Is SAM functionally achromatic?
**Cluster 1 · Protect: CI+CF · Nov 4 / Sig 3 / SciQ 4 / Feas 5 / Unp 4 / ROI 5**

- **One-sentence idea:** Determine whether SAM's masks rely on chromatic information at all, via hue-rotation and grayscale interventions ("does SAM see color or only luminance structure?").
- **Problem:** For domains that are effectively monochrome (IR, many medical modalities), it matters whether SAM's competence depends on color statistics; this basic invariance is unmeasured.
- **Core Hypothesis (falsifiable):** SAM's IoU drops <2 points under full hue rotation and grayscale conversion on natural images, i.e., SAM is functionally achromatic — falsified if color-defined boundaries (equiluminant color edges) segment well, which would prove chromatic sensitivity.
- **Why Important:** Justifies (or refutes) transferring SAM to monochrome sensor domains without color-specific adaptation, and clarifies what boundary signal SAM uses.
- **Why Possibly Novel:** Channel-ablation studies exist for classifiers; the promptable-mask analog with equiluminant-edge stimuli is new.
- **Minimal Experiment:** Evaluate SAM under {original, grayscale, hue-rotated, equiluminant color-edge stimuli}; compare IoU deltas; the equiluminant set is the critical discriminating condition.
- **Main Risk:** Constructing properly equiluminant stimuli requires display-calibration assumptions; approximate with L*-matched synthetic images.

**Survival Reason:** A one-day falsification with a decisive discriminating condition (equiluminant edges); the cheapest genuinely mechanistic idea in the cluster. Index cheap-#1 ranking is, for once, deserved.
**Major Risks:** Equiluminance construction subtleties; a "mostly achromatic" middle result is less quotable than either extreme.
**Unresolved Questions:** Does achromaticity hold across SAM variants and medical-SAM fine-tunes? Does it interact with the edge-following mechanism of 0001?
**Required Experiments:** (1) Four-condition intervention battery; (2) L*-matched synthetic equiluminant edge set; (3) transfer check on real monochrome domains (IR, X-ray) to close the loop on the motivating claim.
**Reviewer Opinion:** Keep. Small but perfectly formed; the equiluminant condition makes it publishable science rather than an ablation note.

---

## IDEA-A-0029 — SAM-assisted annotation contaminates future ground truth
**Cluster 1 · Protect: HR+RM · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 5 · Risk H**

- **One-sentence idea:** Measure the annotation feedback loop: do datasets annotated *with SAM assistance* systematically over-represent SAM-easy boundaries, biasing all models trained on them?
- **Problem:** SAM is now embedded in annotation tools; if annotators accept SAM proposals preferentially where SAM is good, new datasets inherit SAM's competence profile — an ecosystem-level circularity nobody has quantified.
- **Core Hypothesis (falsifiable):** Datasets built with SAM-assisted pipelines show measurably higher agreement-with-SAM (by >10 IoU) than scratch-annotated datasets on matched content, and models trained on the former overestimate their real-world boundary quality by a corresponding margin.
- **Why Important:** This is dataset-generation contamination — it corrupts the community's future ground truth and inflates all downstream progress metrics.
- **Why Possibly Novel:** Model-assisted annotation bias has been raised conceptually; a quantitative two-condition annotation study for segmentation is missing.
- **Minimal Experiment:** Annotate the same 500 images two ways (SAM-assisted vs scratch, professional annotators); compare boundary statistics, agreement-with-SAM, and downstream model rankings trained on each.
- **Main Risk:** Annotator skill variance may swamp the assistance effect; use within-annotator crossover design.

**Survival Reason:** Protected high-risk/high-reward: field-level stakes (the community's future ground truth), a controlled two-condition design, and a finding that compounds in importance every year model-assisted annotation grows.
**Major Risks:** Annotation cost (professional annotators, crossover design); effect may be tool-UX-dependent; publication resistance from dataset builders.
**Unresolved Questions:** Does contamination concentrate in boundary style or also in instance granularity (link 0007)? What acceptance-threshold policies mitigate it? How fast does it compound across dataset generations (link 0267/0288)?
**Required Experiments:** (1) 500-image within-annotator crossover (SAM-assisted vs scratch); (2) agreement-with-SAM and boundary-statistics comparison; (3) downstream ranking experiment training on both GT versions; (4) absorb 0219's benchmark-provenance margin-shift analysis as a second study arm.
**Reviewer Opinion:** Keep, flagship-tier. If Batch A produces one paper the field is forced to cite defensively, it is this one. Coordinate with 0007 (mechanism) and 0267 (inheritance fidelity).

---

## IDEA-A-0031 — Paraphrase variance vs reported SOTA gaps
**Cluster 2 · Protect: CF+RM · Nov 4 / Sig 5 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Quantify the variance of open-vocabulary segmentation performance across semantically equivalent text prompts ("paraphrase variance") as a first-class model property.
- **Problem:** Open-vocab segmentation papers report one number per class name, but "dog"/"a dog"/"canine" can yield different masks; the magnitude and structure of paraphrase variance is unreported.
- **Core Hypothesis (falsifiable):** Paraphrase variance in mIoU exceeds the typical reported SOTA gap (1–2 points) for >30% of classes on ADE20K/Cityscapes open-vocab evaluations, meaning many published rankings are within prompt noise.
- **Why Important:** If rankings flip under paraphrases, the field's leaderboard conclusions are partially artifacts of prompt selection.
- **Why Possibly Novel:** Prompt sensitivity is studied for LLMs and classification; a systematic paraphrase-variance audit for *dense* prediction is missing.
- **Minimal Experiment:** For 3 open-vocab segmentation models, evaluate 10 human-written paraphrases per class on 2 benchmarks; report per-class variance and ranking stability under prompt resampling.
- **Main Risk:** Paraphrase set construction itself biases results; use multiple independent paraphrase authors.

**Survival Reason:** Days of inference against the credibility of every OV-segmentation leaderboard; the ranking-stability-under-resampling analysis is the killer deliverable. Absorbs 0032 (order/composition sensitivity) and 0043 (length/content) as secondary arms.
**Major Risks:** Paraphrase-set authorship bias; the field may dismiss it as "known for LLMs" unless the dense-specific ranking-flip evidence is airtight.
**Unresolved Questions:** Is variance class-structured (rare classes noisier)? Does prompt-ensembling restore ranking stability or merely shift it? How does variance interact with vocabulary-order effects (0032's content)?
**Required Experiments:** (1) 10-paraphrase × multi-author battery on 2 benchmarks × ≥3 models; (2) bootstrap ranking-stability analysis under prompt resampling; (3) vocabulary composition/order sub-study; (4) reporting-protocol proposal (prompt-marginalized scores).
**Reviewer Opinion:** Keep. The evaluation-hygiene twin of 0340; cheap, quotable, and likely to change how OV papers must report numbers.

---

## IDEA-A-0033 — Prompt-specificity inverse-U (basic-level optimum)
**Cluster 2 · Protect: CI+CF · Nov 4 / Sig 4 / SciQ 5 / Feas 5 / Unp 4 / ROI 5**

- **One-sentence idea:** Map the relationship between lexical specificity of the prompt ("vehicle" → "car" → "sedan" → "2012 Toyota Camry") and segmentation quality, testing for a non-monotonic optimum.
- **Problem:** Users assume more specific prompts are better; but rare specific terms are poorly represented in text encoders, suggesting an interior optimum of specificity.
- **Core Hypothesis (falsifiable):** Segmentation IoU vs specificity level is inverse-U shaped, with the optimum at basic-level categories (in the Rosch sense), and the drop for over-specific prompts correlates with term frequency in pretraining corpora.
- **Why Important:** Gives users a principled prompting rule and connects cognitive "basic-level" theory to VLM behavior.
- **Why Possibly Novel:** Basic-level effects are known in psychology and classification; their existence in dense prediction and the frequency-mediated mechanism are untested.
- **Minimal Experiment:** Build 4-level specificity chains for 50 categories; evaluate 3 open-vocab segmenters; regress IoU against level and (proxy) term frequency.
- **Main Risk:** Specificity confounds with visual homogeneity of the category; control by fixing the evaluated instance set across levels.

**Survival Reason:** Counter-intuitive (more specific ≠ better), theory-connected (Rosch basic-level), mechanism-bearing (frequency mediation), and inference-only. The best science-per-GPU-hour in cluster 2.
**Major Risks:** Specificity/homogeneity confound; frequency proxies for closed pretraining corpora are approximate.
**Unresolved Questions:** Does the optimum shift for biomedical registers (link 0049)? Is the mechanism text-tower frequency or image-text alignment sparsity? Do LLM-text-tower models flatten the curve?
**Required Experiments:** (1) 4-level chains × 50 categories with fixed instance sets; (2) frequency regression using open-corpus proxies (LAION); (3) mediation analysis (frequency vs specificity level); (4) cross-model replication including one open-data model.
**Reviewer Opinion:** Keep. Publishable at a top venue on the strength of the inverse-U + mechanism combination; also directly feeds prompting practice.

---

## IDEA-A-0041 — Does chain-of-thought causally change grounding?
**Cluster 2 · Protect: HR+CI · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5 · Risk H**

- **One-sentence idea:** Test whether chain-of-thought style reasoning text actually changes *where* VLMs ground (attention/mask placement) or only changes the verbal rationale while grounding stays fixed.
- **Problem:** Reasoning-segmentation systems assume intermediate reasoning improves localization, but reasoning could be post-hoc rationalization with grounding determined by the visual pathway alone.
- **Core Hypothesis (falsifiable):** For referring segmentation with reasoning-capable VLMs, forcing incorrect-but-plausible reasoning chains changes final masks in <15% of cases — grounding is causally insensitive to the reasoning text.
- **Why Important:** If grounding ignores reasoning, "reasoning segmentation" marketing is misleading and the real bottleneck is elsewhere.
- **Why Possibly Novel:** CoT faithfulness is studied for QA; a causal intervention on reasoning chains with *mask output* as the dependent variable is new.
- **Minimal Experiment:** On referring-segmentation cases requiring inference, inject correct vs subtly wrong reasoning prefixes; measure mask-change rate and accuracy under each condition.
- **Main Risk:** Injected reasoning may be off-distribution for the model, causing degenerate behavior unrelated to faithfulness; include fluency-matched controls.

**Survival Reason:** Protected HR+CI: a causal intervention with a mask endpoint that either crowns or kills "reasoning segmentation" — a growing subfield betting on the assumption this idea tests. Absorbs 0192 (salience ablation) as a control arm.
**Major Risks:** Off-distribution injected reasoning; model-family heterogeneity (verdict may differ between architectures that fuse text early vs late).
**Unresolved Questions:** Does faithfulness scale with model size? Are there case types (spatial inference chains) where reasoning is causally used? Does fine-tuning for reasoning-segmentation increase causal sensitivity?
**Required Experiments:** (1) Correct vs subtly-wrong reasoning-prefix injection with fluency-matched controls; (2) mask-change-rate and accuracy analysis; (3) 0192-style salience ablation (does the "reasoning" case set even require reasoning?); (4) ≥3 model families.
**Reviewer Opinion:** Keep, high priority. The CoT-faithfulness question with a dense endpoint is exactly the kind of import that top vision venues reward, and both outcomes are consequential.

---
## IDEA-A-0049 — Lay vs expert terminology for medical grounding
**Cluster 2 · Protect: CI+CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether expert medical terminology or lay descriptions prompt medical VLM segmentation better — the "vocabulary register mismatch" question.
- **Problem:** Medical VLMs are prompted with expert terms ("pneumothorax") though their web-scale pretraining likely contains far more lay language ("collapsed lung"); the optimal register is unknown.
- **Core Hypothesis (falsifiable):** For general-domain VLMs applied to medical grounding, lay-term prompts outperform expert terms by >5 IoU on average, and the gap reverses for models pretrained on biomedical literature (PubMed-scale corpora).
- **Why Important:** A free performance lever for medical VLM deployment, plus a diagnostic of what medical knowledge the text tower actually holds.
- **Why Possibly Novel:** Register/terminology effects on *grounding* (not QA) in medical VLMs are unmeasured.
- **Minimal Experiment:** Build expert/lay prompt pairs for 30 findings; evaluate grounding IoU for 2 general and 2 biomedical VLMs; test the interaction effect.
- **Main Risk:** Expert/lay pairs may differ in specificity, not just register; control for description length and specificity.

**Survival Reason:** Free performance lever plus a text-tower diagnostic, with a predicted interaction (general vs biomedical pretraining) that makes the design self-controlling. Cheap and counter-intuitive.
**Major Risks:** Register/specificity confound; medical grounding models are a moving target (the interaction may shrink as biomedical VLMs standardize).
**Unresolved Questions:** Does the register effect track corpus term frequency continuously (tie to 0033's mechanism)? Does it hold for non-English clinical language? Does it transfer from grounding to report generation?
**Required Experiments:** (1) 30-finding expert/lay pairs, length- and specificity-matched; (2) 2 general + 2 biomedical VLMs, interaction test; (3) frequency-mediation regression shared with 0033; (4) small clinician validation that lay phrasings are clinically faithful.
**Reviewer Opinion:** Keep. MICCAI-ready, days of compute, and mechanistically connected to 0033 — run them as one prompting-science program.

---

## IDEA-A-0055 — LLRD explains most of the PEFT advantage
**Cluster 3 · Protect: CI+RM · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Test the hypothesis that layer-wise learning-rate decay (LLRD) alone accounts for most of the reported benefit of sophisticated PEFT schemes in dense-prediction fine-tuning.
- **Problem:** Many adapter papers compare against naive full FT with uniform LR; LLRD is a strong, cheap baseline that is often missing, potentially inflating PEFT novelty claims.
- **Core Hypothesis (falsifiable):** Full FT with tuned LLRD comes within 0.5 mIoU of the best PEFT method on ≥70% of standard adaptation benchmarks, at equal compute.
- **Why Important:** If confirmed, dozens of PEFT comparisons need reinterpretation and practitioner defaults simplify dramatically.
- **Why Possibly Novel:** LLRD is known in NLP fine-tuning; its role as the hidden confounder in vision PEFT literature hasn't been isolated.
- **Minimal Experiment:** Reproduce 6 published PEFT-vs-FT comparisons for segmentation, adding LLRD-tuned full FT; report the revised gaps.
- **Main Risk:** "Tuned LLRD" requires its own search budget; account compute honestly on both sides.

**Survival Reason:** Protected CI+RM: one cheap baseline potentially deflating a whole literature. The disagreement it will provoke (tuning-fairness disputes) is a feature, not a bug.
**Major Risks:** Tuning-budget accounting disputes; partial precedents in NLP make the vision-dense novelty contingent on execution quality.
**Unresolved Questions:** Does the LLRD-equivalence hold in low-data regimes where PEFT's regularization should matter most? Does it interact with the LR-ratio dial of 0067?
**Required Experiments:** (1) Reproduce 6 published PEFT-vs-FT comparisons with LLRD arms at matched, pre-registered budgets; (2) low-data stratification; (3) joint analysis with 0067's encoder/decoder-LR-ratio model; (4) release full sweep grids.
**Reviewer Opinion:** Keep. Coordinate 0055/0067/0072 as one "PEFT demystification" program sharing runs; the trio is stronger than any of them alone.

---

## IDEA-A-0058 — LoRA amplifies spurious correlations
**Cluster 3 · Protect: HR+CI · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether LoRA's low-rank constraint makes fine-tuned models *more* susceptible to spurious correlations than full fine-tuning under distribution shift.
- **Problem:** Low-rank updates can only reweight existing feature directions; if the strongest existing directions are spurious (backgrounds, textures), LoRA may amplify shortcut reliance — an unexamined safety issue.
- **Core Hypothesis (falsifiable):** On datasets with known spurious correlations (backgrounds correlated with class), LoRA-adapted segmenters show larger worst-group degradation than full FT at matched in-distribution accuracy.
- **Why Important:** PEFT is the default in industry; a systematic shortcut amplification would be a serious hidden cost, especially for medical deployment.
- **Why Possibly Novel:** PEFT robustness studies focus on average OOD accuracy; the spurious-direction amplification mechanism with worst-group analysis is new for dense tasks.
- **Minimal Experiment:** Construct segmentation datasets with controlled background-class correlation; adapt with LoRA vs full FT; measure worst-group IoU on decorrelated test splits.
- **Main Risk:** Constructing spurious correlations without confounds is delicate; needs several independent correlation types (texture, color, context).

**Survival Reason:** Protected HR+CI with a crisp mechanism (low-rank updates can only reweight existing — possibly spurious — directions) and worst-group safety stakes for the industry-default adaptation method.
**Major Risks:** Spurious-correlation construction artifacts; effect size may depend on rank, making the headline claim rank-conditional.
**Unresolved Questions:** Does amplification scale inversely with rank (mechanism prediction)? Do DoRA/orthogonality-regularized variants mitigate it? Does it appear in real (not constructed) medical scanner-site correlations?
**Required Experiments:** (1) Controlled correlation datasets across ≥3 correlation types; (2) LoRA-vs-full-FT worst-group analysis at matched ID accuracy; (3) rank sweep as the mechanism test; (4) one natural-correlation medical replication.
**Reviewer Opinion:** Keep. The rank-sweep mechanism prediction elevates this from robustness benchmarking to theory-testing; strong CVPR/MICCAI dual-track candidate.

---

## IDEA-A-0067 — One dial: the encoder/decoder LR ratio
**Cluster 3 · Protect: HR+RM · Nov 5 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Test whether a single scalar — the encoder/decoder learning-rate ratio — explains most variance among PEFT/fine-tuning recipes for promptable segmentation ("the stability–plasticity dial").
- **Problem:** The recipe zoo (freeze this, adapt that) may collapse onto one underlying control variable; if so, the field is over-parameterizing a one-dimensional choice.
- **Core Hypothesis (falsifiable):** Across recipes, final target-task and retained-generality metrics are predicted (R² > 0.7) by the effective encoder:decoder LR ratio alone, with recipe identity adding <5% explained variance.
- **Why Important:** Radical simplification of fine-tuning practice; reframes recipe papers as points on a single trade-off curve.
- **Why Possibly Novel:** Nobody has regressed the recipe zoo onto a common control variable for segmentation fine-tuning.
- **Minimal Experiment:** 30 recipe configurations on 3 tasks; compute effective LR ratios; fit the one-variable model and measure residual recipe effects.
- **Main Risk:** "Effective LR ratio" for adapters requires a principled definition (update-norm ratio); pre-register it.

**Survival Reason:** Protected HR+RM: a radical-simplification claim (R²>0.7 or bust) that reviewers will fight about. High risk of a messy middle result, but the upside — collapsing the recipe zoo to one dial — justifies protection.
**Major Risks:** The effective-ratio definition is contestable and result-determining; a 0.5 R² outcome is unpublishable-ish.
**Unresolved Questions:** Is update-norm ratio the right operationalization for adapters and prompt-tuning? Does the dial predict forgetting (link 0076) as well as target gain?
**Required Experiments:** (1) Pre-registered effective-ratio definition; (2) 30-recipe × 3-task grid; (3) one-variable regression with residual-variance decomposition; (4) out-of-sample recipe prediction test.
**Reviewer Opinion:** Keep under protection. Run after (or jointly with) 0055/0076 so the grid triple-serves; the out-of-sample prediction test is what makes or breaks credibility.

---

## IDEA-A-0072 — Strong augmentation + frozen features vs LoRA, matched compute
**Cluster 3 · Protect: RM · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Run the controlled comparison the field skipped: strong augmentation + frozen features + linear/light decoder vs weak augmentation + LoRA, at matched compute, for dense adaptation.
- **Problem:** Augmentation strength and adaptation method are always co-varied in papers; we don't know how much of PEFT's benefit is reproducible by augmentation with a frozen backbone.
- **Core Hypothesis (falsifiable):** On ≥50% of small-data segmentation tasks, strong-aug + frozen features matches LoRA + default-aug within 1 mIoU at equal compute, implying much of "adaptation" is invariance injection, not representation change.
- **Why Important:** Reorders the practitioner's toolbox: augmentation is simpler, safer (no forgetting), and composable.
- **Why Possibly Novel:** The augmentation-vs-adaptation *equivalence question* has not been posed as a controlled matched-compute study for dense tasks.
- **Minimal Experiment:** 6 tasks × {frozen+strong-aug, frozen+weak-aug, LoRA+weak-aug, LoRA+strong-aug} at matched budgets; 3 seeds; report the full factorial.
- **Main Risk:** "Strong augmentation" must be tuned per-task to be a fair champion, inflating its budget; account tuning cost explicitly.

**Survival Reason:** The controlled factorial the field skipped; verdict reframes "adaptation" as invariance-injection vs representation change. RM-protected — augmentation-vs-PEFT partisans will collide in review.
**Major Risks:** Augmentation-tuning budget fairness; conclusion may be backbone-dependent (DINOv2 vs SAM encoders).
**Unresolved Questions:** Does the equivalence hold under distribution shift (where 0058 predicts LoRA is fragile)? Where exactly does the frozen-feature ceiling bind (link 0202)?
**Required Experiments:** (1) Full 2×2 factorial × 6 tasks × 3 seeds at matched budgets with explicit tuning accounting; (2) shift-stratified evaluation; (3) two backbones; (4) joint reporting with 0055's LLRD arms.
**Reviewer Opinion:** Keep. Completes the PEFT-demystification trio; the factorial design is its shield against the fairness disputes it will attract.

---

## IDEA-A-0076 — The gain/retention frontier: forgetting is unforced error
**Cluster 4 · Protect: RM · Nov 4 / Sig 5 / SciQ 4 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Map the full Pareto frontier between target-task gain and zero-shot generality loss when fine-tuning SAM, and test whether published fine-tunes sit far from that frontier.
- **Problem:** SAM fine-tunes report target gains without measuring generality loss; the community lacks even a descriptive account of the trade-off's shape, let alone whether existing recipes are efficient.
- **Core Hypothesis (falsifiable):** The gain/retention frontier is strongly concave (large retention is nearly free up to a knee), and ≥70% of common recipes (full FT, decoder-only, LoRA at default LR) sit >10 retention points inside the frontier — i.e., forgetting in practice is mostly unforced error.
- **Why Important:** If most forgetting is unforced, the fix is recipe hygiene, not new algorithms — a message with immediate practical consequences.
- **Why Possibly Novel:** Forgetting is documented, but frontier estimation with recipe-efficiency auditing for promptable segmentation is new.
- **Minimal Experiment:** Sweep LR × trained-components × steps on 2 target tasks; measure target IoU and zero-shot IoU on a 6-domain retention suite; trace the empirical frontier and place standard recipes on it.
- **Main Risk:** The frontier depends on the retention suite's composition; use a broad, pre-registered suite.

**Survival Reason:** "Most forgetting is recipe hygiene" would reset continual-learning-for-VFM practice; frontier estimation is the right instrument and doubles as infrastructure for 0067/0078/0089.
**Major Risks:** Retention-suite composition disputes; sweep compute is nontrivial; frontier may be recipe-family-dependent.
**Unresolved Questions:** Is the knee position task-distance-dependent? Do the frontier's efficient points coincide with specific LR-ratio values (0067's dial)?
**Required Experiments:** (1) Pre-registered 6-domain retention suite; (2) LR × components × steps sweep on 2 targets; (3) frontier tracing with published-recipe placement; (4) shared-run analysis with 0067.
**Reviewer Opinion:** Keep. The descriptive frontier alone is citable; the "unforced error" quantification is the headline. Run as the infrastructure spine of cluster 4's program.

---

## IDEA-A-0078 — Forgetting is mostly readout drift
**Cluster 4 · Protect: CI · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether "forgetting" in fine-tuned dense models is mostly output-head/decoder drift rather than feature destruction, via linear re-probing of frozen intermediate features.
- **Problem:** If fine-tuned encoders still contain the old capabilities linearly (only the readout drifted), then forgetting is shallow and cheaply reversible — a fundamentally different problem than feature erasure.
- **Core Hypothesis (falsifiable):** Linear probes retrained on the *fine-tuned* encoder's features recover >85% of original zero-shot dense performance on forgotten domains, versus <40% recovery from the drifted full model — most forgetting is readout drift.
- **Why Important:** Changes the objective of continual learning for foundation models from "preserve weights" to "preserve or re-derive readouts," which is far cheaper.
- **Why Possibly Novel:** Probing-based forgetting decomposition exists in isolated classification studies; the dense-prediction version with promptable decoders is new.
- **Minimal Experiment:** After fine-tunes on 3 tasks, retrain lightweight decoders/probes on frozen adapted encoders for 4 forgotten domains; compare recovery rates.
- **Main Risk:** "Recovery via retraining a probe" requires labeled data from forgotten domains; quantify how little suffices.

**Survival Reason:** Protected CI: if lost capabilities remain linearly decodable, continual learning's objective changes entirely. Simple design, big reframe — the strongest single idea in cluster 4.
**Major Risks:** Classification-era precedents partially anticipate it; probe-data requirements could blunt the "cheaply reversible" message.
**Unresolved Questions:** How few labels suffice for readout recovery? Does recovery degrade with fine-tune distance/duration (link 0089's hysteresis)? Does it hold for promptable decoders, not just dense probes?
**Required Experiments:** (1) 3-fine-tune × 4-forgotten-domain probe-recovery grid; (2) label-budget curves for recovery; (3) promptable-decoder re-alignment arm; (4) time-course analysis shared with 0089.
**Reviewer Opinion:** Keep, high priority. Combined with 0089 (suppression-vs-erasure) this pair could own the "forgetting is shallow" narrative for dense models.

---

## IDEA-A-0089 — Forgetting hysteresis: suppression, not erasure
**Cluster 4 · Protect: HR · Nov 5 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Test for hysteresis in forgetting: after fine-tuning away a capability, does brief re-exposure to the original objective restore it far faster than it was learned ("rapid reversibility"), and does the restoration survive continued target training?
- **Problem:** Whether forgotten dense capabilities are erased or merely suppressed determines the economics of capability maintenance; hysteresis dynamics are unmeasured for foundation-scale segmentation.
- **Core Hypothesis (falsifiable):** Restoring zero-shot generality takes <5% of the original steps (suppression, not erasure), but restored capability decays again within a similar budget of continued target training — a repeatable hysteresis loop with characteristic time-constants.
- **Why Important:** Suggests cheap periodic "refresh" schedules as a practical alternative to continual-learning machinery, with predictable maintenance costs.
- **Why Possibly Novel:** Rapid-recovery phenomena are hinted at in LLM literature; a quantitative hysteresis characterization for dense vision models is new.
- **Minimal Experiment:** Fine-tune SAM on a target task, then alternate short generality-refresh and target phases; log both metrics; fit time-constants across cycles.
- **Main Risk:** Refresh data may leak target-relevant signal; use strictly disjoint domains for refresh.

**Survival Reason:** Protected HR: the time-constant characterization is genuinely new for dense models and implies a cheap maintenance policy (periodic refresh) that practitioners could adopt immediately.
**Major Risks:** Refresh-data leakage; cycles may not be stationary (time-constants drifting), muddying the "law" claim; SA-1B access needed for authentic refresh objectives.
**Unresolved Questions:** Do time-constants depend on the recipe's frontier position (0076)? Is suppression localized to readouts (0078) or distributed? Does the loop stabilize or degrade over many cycles?
**Required Experiments:** (1) Alternating refresh/target phases with logged dual metrics; (2) time-constant fitting across ≥5 cycles; (3) disjoint-domain refresh controls; (4) joint probe-analysis with 0078 to locate where suppression lives.
**Reviewer Opinion:** Keep under HR protection. Riskiest of the cluster-4 trio but the one with a genuinely new phenomenon to name; the three ideas share infrastructure and should be one program.

---
## IDEA-A-0091 — Leaderboard gains below the label-noise floor
**Cluster 5 · Protect: RM · Nov 4 / Sig 5 / SciQ 4 / Feas 3 / Unp 3 / ROI 5**

- **One-sentence idea:** Quantify the inter-annotator-variability ceiling of major medical segmentation benchmarks and identify which reported SOTA gains are below the label-noise floor.
- **Problem:** Leaderboard gains of 0.5–1 Dice are celebrated on benchmarks whose annotator disagreement may be several Dice points, meaning models are being fit to one annotator's style, not anatomy.
- **Core Hypothesis (falsifiable):** For ≥half of widely used benchmarks, the top-10 leaderboard spread is smaller than the measured inter-annotator Dice spread on a re-annotated subset — recent "progress" is within label noise.
- **Why Important:** Redirects the field from chasing sub-noise gains toward multi-annotator ground truth and distributional evaluation.
- **Why Possibly Novel:** Inter-annotator variability is known per-dataset anecdotally; a cross-benchmark audit tied explicitly to leaderboard spreads is missing.
- **Minimal Experiment:** Re-annotate 50–100 cases from 5 benchmarks with 3 experts each; compare annotator spread to public leaderboard spreads.
- **Main Risk:** Expert annotation is expensive; partner with clinical collaborators or use existing multi-annotator releases where available.

**Survival Reason:** The cross-benchmark audit tying annotator ceilings directly to leaderboard spreads is field-recalibrating for medical segmentation; also carries 0327's benchmark-death criterion as a natural extension.
**Major Risks:** Expert-annotation cost; benchmark owners' pushback; results hinge on annotator-pool quality.
**Unresolved Questions:** Which benchmarks are already "dead" by the criterion (0327)? Does the noise floor vary by structure type enough to salvage some sub-noise claims? What reporting standard should replace single-GT Dice?
**Required Experiments:** (1) 3-expert re-annotation of 50–100 cases × 5 benchmarks; (2) spread-vs-leaderboard comparison with CIs; (3) benchmark-lifecycle verdicts (absorbing 0327); (4) a concrete multi-annotator reporting proposal.
**Reviewer Opinion:** Keep, flagship-tier for MICCAI. The single most useful service audit in cluster 5; shares annotation budget with 0103 and 0166.

---

## IDEA-A-0093 — Why nnU-Net still wins: causal decomposition
**Cluster 5 · Protect: HR+RM · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 3 / ROI 4 · Risk H**

- **One-sentence idea:** Run a compute- and tuning-matched showdown between nnU-Net and foundation-model fine-tunes to isolate *why* well-tuned U-Nets remain competitive in medical segmentation.
- **Problem:** Foundation models dominate natural images but reportedly struggle to beat nnU-Net; existing comparisons confound tuning effort, resolution handling, and preprocessing, so the *cause* of U-Net resilience is unknown.
- **Core Hypothesis (falsifiable):** After matching preprocessing/resolution/tuning budget, the remaining nnU-Net advantage concentrates in (a) full-resolution 3D context and (b) target-specific augmentation — and vanishes on 2D high-contrast tasks, localizing exactly what foundation models lack.
- **Why Important:** Tells the field whether to invest in 3D-native foundation models, resolution handling, or augmentation transfer — a strategic fork.
- **Why Possibly Novel:** Comparisons exist but none decompose the gap causally with matched budgets and component swaps.
- **Minimal Experiment:** On 6 tasks spanning 2D/3D and contrast levels, run both families with matched budgets, then component-swap (give the ViT nnU-Net's augmentation and resolution policy) to attribute the gap.
- **Main Risk:** "Matched tuning" is contentious; pre-register budgets and publish all configs.

**Survival Reason:** Protected HR+RM: the strategic fork of medical VFM investment, attacked with component-swap attribution rather than another bake-off. Expensive and contentious — which is why nobody has done it properly.
**Major Risks:** Compute-heavy (full 3D training grids); "matched tuning" disputes; the gap may shrink on its own as 3D-native VFMs mature, dating the result.
**Unresolved Questions:** Which component (3D context, augmentation policy, resolution handling) dominates per task type? Does the verdict differ for lesions vs organs? Where does 0245's recipe-attribution logic intersect (recipe vs architecture)?
**Required Experiments:** (1) Matched-budget dual-family runs on 6 tasks spanning 2D/3D and contrast; (2) component swaps (augmentation policy, resolution policy, 3D context) as the causal core; (3) pre-registered budgets and public configs; (4) coordination with 0245's recipe-equalization methodology.
**Reviewer Opinion:** Keep under protection. The component-swap design is the only version of this comparison worth running; fund it with the batch's largest compute allocation.

---

## IDEA-A-0097 — Dice loss destroys calibration, imbalance-scaled
**Cluster 5 · Protect: RM · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Test at scale whether Dice loss — the medical default — systematically destroys probability calibration relative to cross-entropy, and whether the harm scales with class imbalance.
- **Problem:** Dice loss is near-universal in medical segmentation, yet its miscalibration side effect (known in isolated studies) has never been quantified across tasks or connected to imbalance level, leaving practitioners without a usage rule.
- **Core Hypothesis (falsifiable):** Dice-trained models show ECE ≥3× cross-entropy-trained models at matched Dice score, with miscalibration growing monotonically with foreground sparsity; a two-phase (CE→Dice) schedule retains Dice's accuracy without the calibration penalty.
- **Why Important:** Calibrated probabilities are prerequisites for uncertainty-guided review and safe thresholding in clinical use; the default loss may be silently forfeiting them.
- **Why Possibly Novel:** The imbalance-conditioned quantification and the validated schedule fix, across many tasks, would settle a long-standing folklore dispute.
- **Minimal Experiment:** 8 tasks spanning imbalance levels × {Dice, CE, CE→Dice, Dice+CE} × 3 seeds; report accuracy-calibration Pareto per imbalance level.
- **Main Risk:** ECE estimation on sparse foregrounds is fragile; use debiased calibration estimators and regional calibration metrics.

**Survival Reason:** Settles a folklore dispute about the single most-used loss in medical imaging, with an imbalance-conditioned usage rule as the deliverable. Absorbs 0244's Dice+CE default audit into the same grid.
**Major Risks:** ECE estimation fragility on sparse foregrounds; isolated precedents mean the contribution is the systematic scaling law, not the phenomenon.
**Unresolved Questions:** Does the CE→Dice schedule preserve calibration under distribution shift? How does the imbalance-scaling interact with 0103's finding that uncertainty maps are boundary-band-dominated?
**Required Experiments:** (1) 8-task × 4-loss × 3-seed grid stratified by imbalance (absorbing 0244's arms); (2) debiased and regional calibration estimators; (3) accuracy-calibration Pareto per imbalance level; (4) downstream uncertainty-review simulation as clinical linkage.
**Reviewer Opinion:** Keep. Bread-and-butter science the field will actually use; coordinate compute with 0244's absorbed design as originally cross-referenced.

---

## IDEA-A-0100 — Flip-TTA harms lateralized anatomy
**Cluster 5 · Protect: CI+CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 4 / ROI 5**

- **One-sentence idea:** Audit test-time augmentation in medical segmentation for anatomically *invalid* invariances (e.g., left-right flips on lateralized anatomy) and quantify the harm TTA silently causes.
- **Problem:** Flip/rotate TTA is copied from natural images into medical pipelines, but anatomy is chiral and oriented; averaging over invalid transforms may blur lateralized structures — an unexamined standard practice.
- **Core Hypothesis (falsifiable):** Flip-TTA reduces accuracy on lateralized structures (>2 Dice on left/right-distinct organs) while helping symmetric ones, such that anatomy-aware TTA policies beat blanket TTA on ≥70% of tasks.
- **Why Important:** TTA is in nearly every medical pipeline including challenge winners; a validated anatomy-aware policy is an immediate free improvement.
- **Why Possibly Novel:** TTA is treated as harmless; its anatomical validity has not been systematically audited.
- **Minimal Experiment:** On 8 tasks with lateralized and symmetric structures, compare no-TTA vs blanket-TTA vs anatomy-aware TTA; stratify by structure laterality.
- **Main Risk:** Effects may be small per-structure; aggregate across many structures for power.

**Survival Reason:** A harmful default sitting inside challenge winners, falsifiable in days with existing checkpoints. Protected CI+CF; also carries the killed 0229's multi-scale-TTA question as a secondary arm.
**Major Risks:** Small per-structure effects requiring aggregation; challenge pipelines vary in TTA implementation details.
**Unresolved Questions:** How much of published challenge-winner performance changes under anatomy-aware TTA? Does the harm extend to orientation-sensitive pathologies (situs inversus as the extreme test)?
**Required Experiments:** (1) No-TTA / blanket / anatomy-aware comparison on 8 tasks stratified by laterality; (2) power-aggregated effect analysis; (3) re-scoring of 2–3 public challenge winners; (4) optional multi-scale-TTA arm (0229's content).
**Reviewer Opinion:** Keep. Small, sharp, immediately adopted if confirmed — the ideal cheap-to-falsify profile.

---

## IDEA-A-0103 — Uncertainty maps ≠ clinician disagreement
**Cluster 5 · Protect: CI · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether model uncertainty maps (entropy, MC-dropout, ensembles) actually correlate with *clinician disagreement* regions, which is the operational meaning of "useful uncertainty" in medical segmentation.
- **Problem:** Uncertainty methods are validated against model error, but their clinical use case is flagging regions where experts would disagree or want review — an alignment nobody measures.
- **Core Hypothesis (falsifiable):** Pixel-wise correlation between model uncertainty and multi-annotator disagreement is weak (ρ < 0.4) for standard methods, and is dominated by trivial boundary-band effects — after excluding boundary bands, correlation approaches zero.
- **Why Important:** If uncertainty maps only recapitulate "boundaries are uncertain," their clinical value proposition (flagging genuinely ambiguous regions) is empty and needs new methods.
- **Why Possibly Novel:** The boundary-band-excluded analysis against expert disagreement, across methods, is a new and stringent validity test.
- **Minimal Experiment:** On multi-annotator datasets, compute uncertainty-disagreement correlation with and without boundary-band exclusion for 4 uncertainty methods.
- **Main Risk:** Few datasets have dense multi-annotator masks; prioritize those that do (e.g., prostate, lung nodule collections).

**Survival Reason:** The boundary-band-excluded test is a stringent new instrument that may empty the clinical value proposition of an entire uncertainty-quantification literature. Protected CI; feeds 0280's annotation-routing question directly.
**Major Risks:** Multi-annotator data scarcity; negative result requires careful power analysis to be convincing.
**Unresolved Questions:** Do any methods (evidential, ensemble-diversity) survive the boundary exclusion? Is clinician disagreement itself stable enough to be the target (link 0337)? What does "useful uncertainty" cost to obtain if not free from softmax?
**Required Experiments:** (1) 4-method uncertainty-vs-disagreement correlation with and without boundary bands on multi-annotator sets; (2) power analysis for the null; (3) downstream review-routing simulation shared with 0280; (4) annotator-stability control.
**Reviewer Opinion:** Keep, high priority. The kind of validity audit that changes what "uncertainty-aware" is allowed to mean in MICCAI papers.

---

## IDEA-A-0118 — Models hallucinate surgically removed organs
**Cluster 5 · Protect: CI · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 5**

- **One-sentence idea:** Test how segmentation models fail on post-surgical and anatomically variant patients, quantifying the "atlas prior" dependence of modern learned models.
- **Problem:** Learned models may implicitly encode normal-anatomy atlases; post-surgical absence (resected organs), transplants, and congenital variants then trigger hallucinated structures — a patient-safety failure mode without a benchmark.
- **Core Hypothesis (falsifiable):** On post-resection cases, models hallucinate the absent organ (predict >20% of its typical volume) in ≥40% of cases, and hallucination rate correlates with the organ's positional consistency in training data — models segment "where organs usually are."
- **Why Important:** Hallucinating absent anatomy is among the most dangerous silent failures for clinical use; establishing and benchmarking it forces mitigation.
- **Why Possibly Novel:** Atlas-prior dependence is discussed for registration-based methods; its quantification in deep segmentation models with a positional-consistency predictor is new.
- **Minimal Experiment:** Assemble post-surgical cases (nephrectomy, pneumonectomy) from public data; measure hallucinated-volume statistics across 5 models; test the consistency correlation.
- **Main Risk:** Post-surgical public data is scarce; synthetic organ-removal (inpainting) can extend the set with realism checks.

**Survival Reason:** Patient-safety silent failure with a mechanism (positional-consistency prior) and a benchmark deliverable; the medical twin of 0185's absence benchmark. Protected CI.
**Major Risks:** Post-surgical data scarcity; inpainting-based extension needs stringent realism checks or it tests the inpainter.
**Unresolved Questions:** Does hallucination rate drop for models trained with absence-aware sampling? Do promptable models (MedSAM-class) hallucinate less than fully automatic ones? Is the positional-consistency correlation causal?
**Required Experiments:** (1) Public post-resection case assembly (nephrectomy/pneumonectomy); (2) hallucinated-volume statistics across ≥5 models; (3) positional-consistency regression; (4) inpainting-extended set with radiologist realism vetting; (5) joint refusal-metric design with 0185.
**Reviewer Opinion:** Keep. The single most quotable safety finding available in this batch; regulators and clinical-AI teams will cite it.

---

## IDEA-A-0121 — Binary smoke masks are ill-posed ground truth
**Cluster 6 · Protect: RM · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Demonstrate that binary smoke masks are ill-posed ground truth by measuring annotator threshold inconsistency, and propose density-graded ground truth as the corrected task definition.
- **Problem:** Smoke has no boundary — annotators binarize a continuous density field at arbitrary personal thresholds, so smoke-segmentation benchmarks may largely measure threshold mimicry, capping and distorting all reported progress.
- **Core Hypothesis (falsifiable):** Inter-annotator disagreement on smoke masks concentrates in low-density regions and corresponds to annotators applying different implicit density thresholds (recoverable as a per-annotator scalar), such that a single density map explains >80% of inter-annotator mask variance.
- **Why Important:** If a scalar threshold explains the disagreement, the field should regress density and let applications choose thresholds — redefining the task rather than chasing noise.
- **Why Possibly Novel:** Smoke datasets exist with binary masks; the threshold-decomposition analysis of annotator behavior and the resulting task redefinition are new.
- **Minimal Experiment:** 5 annotators mask 200 smoke images; fit per-annotator threshold models over an estimated density proxy (e.g., dark-channel/transmission); measure explained variance.
- **Main Risk:** Density proxies may be poor on complex backgrounds; validate proxies on synthetic smoke with known density first.

**Survival Reason:** Task-redefinition with a measurable decomposition test (per-annotator scalar thresholds); anchors the entire smoke program (0122, 0128, 0126, 0319). RM-protected — "your task is ill-posed" always draws fire.
**Major Risks:** Density-proxy quality on complex backgrounds; 80% explained-variance threshold may be optimistic.
**Unresolved Questions:** Do thresholds vary within-annotator over time? Does the threshold model hold for fog/steam (link to killed 0124's separability program)? What loss should density-regression training use (absorbed 0132)?
**Required Experiments:** (1) 5-annotator × 200-image study; (2) per-annotator threshold-model fitting over validated density proxies; (3) synthetic-smoke proxy validation; (4) density-regression vs binary-training comparison (0132's absorbed experiment).
**Reviewer Opinion:** Keep, program anchor. The smoke cluster's scientific credibility rests on this measurement being done carefully; fund the annotation study properly.

---

## IDEA-A-0122 — Beer–Lambert transmittance as smoke ground truth
**Cluster 6 · Protect: HR · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Use atmospheric transmission physics (Beer–Lambert attenuation) to derive alpha-matte smoke ground truth from smoke/no-smoke image pairs, creating physically defined labels without human thresholding.
- **Problem:** Human smoke labels are threshold-arbitrary (IDEA-A-0121); paired imagery (fixed cameras before/during smoke) permits computing per-pixel transmittance as physically meaningful ground truth, which nobody has operationalized into a benchmark.
- **Core Hypothesis (falsifiable):** Transmittance maps computed from pairs are reproducible across illumination-matched pairs (correlation >0.9), and models trained to regress transmittance transfer better to unseen scenes (>10% relative error reduction) than binary-mask-trained models thresholded post hoc.
- **Why Important:** Provides the first physically grounded supervision signal for the wildfire-detection domain, where early low-density smoke is exactly what matters.
- **Why Possibly Novel:** Transmission estimation exists in dehazing; using it to *define ground truth* for smoke segmentation benchmarks is a new construction.
- **Minimal Experiment:** Collect/assemble fixed-camera pairs (wildfire camera archives); compute transmittance labels; train regression vs binary models; evaluate cross-scene.
- **Main Risk:** Illumination changes between pair frames corrupt transmittance; restrict to short-interval pairs and model illumination explicitly.

**Survival Reason:** Protected HR: the first physically defined supervision for smoke — a benchmark-construction idea whose success would obsolete threshold-mimicry training (0121's diagnosis) and enable 0126's latency metric on principled labels.
**Major Risks:** Illumination drift between paired frames; wildfire archive access/licensing; transmittance validity at very low densities where it matters most.
**Unresolved Questions:** What interval/illumination tolerance keeps transmittance valid? Can single-image density proxies be calibrated against the paired GT? How does the physical GT interact with 0290's rendering-fidelity question for synthetic pretraining?
**Required Experiments:** (1) Fixed-camera pair assembly with illumination matching; (2) reproducibility analysis across matched pairs; (3) transmittance-regression vs binary training with cross-scene evaluation; (4) release as a benchmark with 0121's threshold analysis attached.
**Reviewer Opinion:** Keep under HR protection. Construction-heavy but the payoff — physics-grounded labels for a safety domain — is the kind of contribution that outlives model generations.

---

## IDEA-A-0123 — Fire segmenters are color detectors
**Cluster 6 · Protect: CI+CF · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether fire segmentation models are mostly color detectors, via hue-manipulation stress tests and colored-distractor benchmarks (sunsets, neon, brake lights).
- **Problem:** Fire has a distinctive color signature, inviting a spectral shortcut; if models are ~color thresholds with extra steps, they will fail on atypical flames (methanol, gas burners) and false-alarm on red/orange distractors — unquantified in current benchmarks.
- **Core Hypothesis (falsifiable):** State-of-the-art fire segmenters lose >50% IoU on hue-shifted flames while confidently segmenting >30% of matched colored distractors — performance is explained predominantly by chromatic features, not structure or motion.
- **Why Important:** Fire detection is safety-critical; a color shortcut means predictable catastrophic failures (blue gas flames missed, sunsets flagged).
- **Why Possibly Novel:** Color dependence is suspected folklore; the controlled hue-intervention quantification with distractor benchmarks is not published.
- **Minimal Experiment:** Build hue-shifted flame sets (real atypical flames + controlled shifts) and a distractor set; evaluate 5 public fire models; decompose feature reliance.
- **Main Risk:** Hue-shifting real flames synthetically may create artifacts; anchor with genuinely atypical-flame photos (gas, chemical fires).

**Survival Reason:** Safety-critical shortcut audit with specific, checkable predictions (blue flames missed, sunsets flagged); cheap; the fire-side complement of 0021's achromaticity test.
**Major Risks:** Synthetic hue-shift artifacts; public fire-model availability and quality varies.
**Unresolved Questions:** Does adding temporal features (flicker) break the color shortcut? How much do existing benchmarks' color statistics predict their models' distractor false-alarm rates? Does the shortcut survive IR fusion?
**Required Experiments:** (1) Real atypical-flame anchor set (gas/chemical fires) + controlled hue shifts; (2) matched colored-distractor battery; (3) 5-model feature-reliance decomposition; (4) flicker/temporal ablation arm.
**Reviewer Opinion:** Keep. Straightforward, safety-quotable, and the negative space (models that pass) would map which training choices avoid the shortcut.

---

## IDEA-A-0125 — Turbulence spectra as a label-free smoke signal
**Cluster 6 · Protect: HR · Nov 5 / Sig 4 / SciQ 5 / Feas 3 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Test whether the turbulence statistics of smoke motion (spectral signatures of buoyant plumes) provide a self-supervision signal that separates smoke from all rigid-world motion without labels.
- **Problem:** Smoke's defining property is its dynamics (buoyancy-driven turbulence), yet self-supervised smoke detection from motion statistics — rather than appearance — remains untested as a primary signal.
- **Core Hypothesis (falsifiable):** A classifier over local spatiotemporal spectra (no appearance features) achieves >0.9 AUC separating smoke regions from moving rigid objects, vegetation, and camera shake, and pretraining on this signal improves downstream smoke segmentation with 10× fewer labels.
- **Why Important:** A physics-grounded, appearance-free signal would be robust to exactly the shifts (color, lighting, geography) that break appearance models.
- **Why Possibly Novel:** Optical-flow features have been used ad hoc; the turbulence-spectrum formulation as a self-supervised pretext for segmentation is new.
- **Minimal Experiment:** Compute spatiotemporal spectral features on labeled wildfire clips; test the motion-only classifier; pretrain a video encoder on the pretext and fine-tune with limited labels.
- **Main Risk:** Distant smoke moves few pixels between frames; characterize the minimum apparent-motion regime where the signal exists.
**Survival Reason:** Protected HR: physics-grounded, appearance-free pretext that would be robust to exactly the shifts that break appearance models; genuinely novel formulation.
**Major Risks:** Minimum apparent-motion regime may exclude the distant early smoke that matters most (tension with 0126's latency goal); compression artifacts corrupt spectra (killed 0135's finding is a caveat here).
**Unresolved Questions:** At what distance/resolution does the turbulence signature survive codecs? Does the pretext transfer to fog/steam discrimination? Can it combine with 0122's transmittance labels?
**Required Experiments:** (1) Motion-only spectral classifier on labeled clips with distance stratification; (2) codec-robustness analysis; (3) pretext pretraining + low-label fine-tuning comparison; (4) hard-negative battery (vegetation, shake, rigid motion).
**Reviewer Opinion:** Keep under HR protection. The distance-regime characterization should be run first as a go/no-go gate; if the signal survives at operationally relevant distances, this is a major contribution.

---

## IDEA-A-0126 — Detection latency as the wildfire metric
**Cluster 6 · Protect: RM · Nov 4 / Sig 5 / SciQ 4 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Replace IoU with detection-latency (time from first visible smoke to first correct alarm-grade mask) as the primary metric for wildfire smoke systems, and test whether IoU-optimal models are latency-suboptimal.
- **Problem:** Wildfire response cares about minutes-to-detection of faint early smoke, but the field optimizes IoU on developed plumes; the two objectives may rank models differently, misdirecting research.
- **Core Hypothesis (falsifiable):** On time-stamped ignition sequences, model rankings by median detection latency disagree with IoU rankings (rank correlation <0.5), and latency winners share high recall on low-density smoke rather than high boundary accuracy.
- **Why Important:** Realigning the metric with the mission could redirect the entire subfield's optimization target toward what saves forests.
- **Why Possibly Novel:** Latency metrics exist in event detection; their application and the ranking-disagreement demonstration for smoke *segmentation* are new.
- **Minimal Experiment:** Assemble ignition-to-detection sequences from wildfire camera archives; evaluate 6 models by latency and IoU; compare rankings.
- **Main Risk:** True ignition timestamps are approximate; use first-human-visible frame as the anchor with multiple annotators.

**Survival Reason:** Mission-aligned metric with a testable ranking-disagreement claim; the evaluation-science layer of the smoke program. RM-protected — metric-replacement proposals always split reviewers.
**Major Risks:** Ignition-timestamp uncertainty; archive access; false-alarm-rate control must be matched or latency comparisons are meaningless.
**Unresolved Questions:** What is the right latency/false-alarm operating framework (FROC-style)? Do latency winners generalize across geography? How does 0122's density GT sharpen the "alarm-grade mask" definition?
**Required Experiments:** (1) Ignition-sequence assembly with multi-annotator first-visible anchors; (2) 6-model latency-vs-IoU ranking comparison at matched false-alarm rates; (3) low-density-recall attribution analysis; (4) metric-protocol release.
**Reviewer Opinion:** Keep. Completing 0121→0122→0126 gives the smoke program diagnosis, supervision, and metric — a full-stack task redefinition worth defending as a unit.

---

## IDEA-A-0128 — No prompt strategy rescues SAM on smoke
**Cluster 6 · Protect: CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Systematically quantify SAM/SAM2's failure on smoke across prompt strategies, testing whether *any* prompting scheme (multi-point, box, dense grid, video propagation) recovers usable smoke masks.
- **Problem:** SAM is being wired into wildfire pipelines as a zero-shot labeler, but its edge-driven mask prior (cf. IDEA-A-0006) is maximally mismatched to boundary-free smoke — the practical recoverability question is unanswered.
- **Core Hypothesis (falsifiable):** No prompt strategy raises SAM's smoke IoU above 0.5× a small supervised baseline's; failures are shrinkage-to-dense-core (predictable from the density field), meaning SAM masks systematically under-cover exactly the low-density smoke that matters for early detection.
- **Why Important:** A definitive negative result would stop the community from building wildfire auto-labeling on an unfit foundation, and the shrinkage law quantifies the bias any SAM-derived smoke dataset inherits.
- **Why Possibly Novel:** "SAM fails on smoke" is anecdote; the exhaustive prompt-strategy audit with the density-conditioned shrinkage characterization is not published.
- **Minimal Experiment:** On 3 smoke datasets, sweep prompt strategies × SAM variants; measure IoU and density-stratified coverage; compare to a small supervised U-Net.
- **Main Risk:** Density stratification requires density estimates (link to IDEA-A-0122); use paired-frame or synthetic subsets where density is known.

**Survival Reason:** Protected CF: a definitive cheap negative with a quantified shrinkage law that blocks a specific bad practice (SAM auto-labeling of smoke) before it propagates into datasets.
**Major Risks:** Someone ships a smoke-tuned SAM variant that partially rescues it, dating the negative; density stratification depends on 0122's machinery.
**Unresolved Questions:** Does the shrinkage law transfer to fog/dust? How much SAM-derived smoke data already exists in the wild, and does it show the predicted bias (link 0267)?
**Required Experiments:** (1) Prompt-strategy × SAM-variant sweep on 3 smoke datasets; (2) density-stratified coverage analysis; (3) small supervised U-Net comparison baseline; (4) audit of one existing SAM-assisted smoke dataset for inherited shrinkage.
**Reviewer Opinion:** Keep. The rare negative result with an actionable law attached; a week of inference, permanent citation value in the wildfire-CV niche.

---
## IDEA-A-0141 — Features on glass encode the background
**Cluster 7 · Protect: HR+CI · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether deep features computed *on* transparent objects encode the background seen through them rather than the object, making transparency a representational (not just detection) failure.
- **Problem:** Transparent objects violate the assumption that pixel appearance belongs to the surface at that pixel; whether backbone features on glass regions represent "glass" or "the background behind glass" is unmeasured and determines what any downstream head can do.
- **Core Hypothesis (falsifiable):** Linear probes on patch features within glass regions decode the *background* class with >70% accuracy but "glass present" with <55% (near chance for hard cases) across major VFMs — the representation itself is transparent to transparency.
- **Why Important:** If features don't encode transparency, no decoder can recover it, and the fix must be at the representation-learning level — a field-redirecting conclusion.
- **Why Possibly Novel:** Transparency papers propose detectors; the representational-content probing question (what do features on glass encode?) has not been asked.
- **Minimal Experiment:** On Trans10K-style data with known backgrounds, train probes on frozen VFM features for background-class and glass-presence decoding; compare across VFMs and layers.
- **Main Risk:** Glass regions contain boundary/specular pixels that leak glass evidence; analyze interior vs edge patches separately.

**Survival Reason:** Protected HR+CI: "the representation is transparent to transparency" is a field-redirecting claim testable with linear probes on frozen features. Subsumes 0145's cheaper behavioral version.
**Major Risks:** Boundary/specular leakage into "interior" patches; probe-capacity dependence of decodability claims.
**Unresolved Questions:** Which layer (if any) carries glass evidence? Do depth-invalidity cues (0142) enter the representation? Does representation-level failure predict which decoder fixes fail (retrospective explanation of the transparency literature)?
**Required Experiments:** (1) Interior-vs-edge stratified probing on Trans10K-class data across ≥4 VFMs and all layers; (2) probe-capacity sweep; (3) behavioral corroboration (0145's prompt-bimodality arm); (4) retrospective correlation with published transparency-method gains.
**Reviewer Opinion:** Keep, flagship-tier for cluster 7. Both outcomes are decisive: encoded-but-unused redirects decoder work, not-encoded redirects pretraining.

---

## IDEA-A-0142 — Depth input hurts; depth-invalidity is the cue
**Cluster 7 · Protect: CI · Nov 5 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether adding depth input *hurts* transparent-object segmentation — since depth sensors return the background or noise on glass — inverting the usual "more modalities help" assumption.
- **Problem:** RGB-D models are assumed superior, but on transparent surfaces depth is systematically wrong (returns background depth or dropout), potentially teaching models an anti-glass shortcut; the sign of depth's contribution on transparency is unestablished.
- **Core Hypothesis (falsifiable):** RGB-D models underperform RGB-only models on transparent-object IoU by >5 points when depth is naively fused, but *depth-invalidity* (the dropout/mismatch pattern itself) used as an explicit feature outperforms both — the sensor's failure is the best transparency cue.
- **Why Important:** Reframes a sensor failure as signal, with direct consequences for robotic grasping and navigation stacks that currently trust depth.
- **Why Possibly Novel:** Depth unreliability on glass is known in robotics; the systematic sign-of-contribution study and invalidity-as-feature formalization for segmentation are new.
- **Minimal Experiment:** On RGB-D transparency datasets (ClearGrasp-style), train {RGB, naive RGB-D, RGB + depth-validity-mask} models; compare on transparent and opaque classes.
- **Main Risk:** Depth invalidity patterns are sensor-specific (stereo vs ToF vs structured light); replicate across sensor types.

**Survival Reason:** Sign-inversion of "more modalities help" plus the elegant reframe of sensor failure as signal. Protected CI with immediate robotics consequences.
**Major Risks:** Sensor-specificity of invalidity patterns; robotics literature partially exploits depth dropout already, so the segmentation-specific sign study must be clearly scoped.
**Unresolved Questions:** Which fusion depths (early/late) produce the harm? Is invalidity informative for mirrors too? Does the invalidity feature survive sensor upgrades (better ToF)?
**Required Experiments:** (1) {RGB, naive RGB-D, RGB+validity-mask} triad on ClearGrasp-class data; (2) transparent-vs-opaque class stratification; (3) three sensor types; (4) fusion-depth ablation.
**Reviewer Opinion:** Keep. Clean, counter-intuitive, deployable; with 0141 it gives cluster 7 both the representational and the sensor-level story.

---

## IDEA-A-0154 — Camouflage failure: attentional or perceptual?
**Cluster 7 · Protect: CF · Nov 4 / Sig 5 / SciQ 5 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Determine whether camouflaged object detection failures are perceptual (features don't separate figure from ground) or attentional (features suffice but saliency/prompting never looks there), using oracle-prompt interventions.
- **Problem:** COD is treated as one problem, but the two failure sources demand opposite fixes (representation learning vs search/prompting); no work cleanly separates them.
- **Core Hypothesis (falsifiable):** Given an oracle point prompt, promptable models recover >70% of the COD performance gap versus specialized COD models — most camouflage failure is attentional (not finding the object), not perceptual (not being able to delineate it).
- **Why Important:** If failure is attentional, COD research should pivot from feature engineering to search strategies and prompt generation — a field-level redirection.
- **Why Possibly Novel:** COD papers benchmark end-to-end; the oracle-prompt decomposition into find-vs-delineate components is not established.
- **Minimal Experiment:** On COD10K-class benchmarks, evaluate SAM-class models with {no prompt/auto, oracle point, oracle box}; decompose the gap to specialist models by prompt level.
- **Main Risk:** Prompted and unprompted models differ architecturally; include prompted versions of specialist models where possible.

**Survival Reason:** One oracle-prompt experiment could redirect an entire subfield's investment from features to search. Near-free, protected CF.
**Major Risks:** Architecture mismatch between prompted and unprompted families; partial precedents (SAM-on-COD evaluations) mean the decomposition framing is the novelty.
**Unresolved Questions:** Does the attentional/perceptual split vary by camouflage type (texture-matching vs disruptive coloration)? What does the residual perceptual gap correlate with (0001's edge-following)?
**Required Experiments:** (1) {auto, oracle-point, oracle-box} ladder on COD10K-class data; (2) gap decomposition vs specialist models; (3) camouflage-type stratification; (4) prompted-specialist control arm.
**Reviewer Opinion:** Keep. Textbook decomposition study: cheap, decisive, and the redirect (search vs features) is actionable by everyone in the COD niche.

---

## IDEA-A-0157 — The human floor on near-invisible glass
**Cluster 7 · Protect: CI · Nov 4 / Sig 4 / SciQ 5 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Measure the human-vision floor for near-invisible glass (clean, anti-reflective, well-lit) and test whether current models are above or below human performance on the hardest transparency regime.
- **Problem:** Some glass is nearly invisible even to humans (people walk into doors); without a human floor, we cannot say whether model failures reflect missing information or missing competence.
- **Core Hypothesis (falsifiable):** On a hardest-regime glass set, human detection (brief-presentation) exceeds the best models by >30 points — humans exploit weak cues (frames, context, subtle reflections) that models don't, proving competence (not information) is the bottleneck.
- **Why Important:** Locates the transparency frontier precisely: if humans succeed where models fail, the information exists and modeling should continue; if both fail, sensing (polarization) is the answer (link to IDEA-A-0150).
- **Why Possibly Novel:** Human baselines are almost never collected for transparency benchmarks; the hardest-regime comparison is absent.
- **Minimal Experiment:** Curate hard-glass images; run controlled human detection/localization experiments; compare with model outputs under matched viewing conditions.
- **Main Risk:** Matching human and model "viewing conditions" (time, resolution) fairly requires careful psychophysics design.

**Survival Reason:** The competence-vs-information verdict decides whether transparency research should invest in modeling or sensing — a rare experiment that prices a whole research direction. Protected CI.
**Major Risks:** Psychophysics design fairness; hard-glass curation is laborious; humans may use scene priors models could also learn, muddying "information exists."
**Unresolved Questions:** Which weak cues (frames, reflections, context) carry the human advantage — and are they present in features (0141's probes)? Where does polarization sensing beat both (killed 0150's question, inherited here as context)?
**Required Experiments:** (1) Hardest-regime glass curation with capture metadata; (2) brief-presentation human detection/localization study; (3) matched-condition model evaluation; (4) cue-ablation analysis (mask frames/reflections) to locate the human advantage.
**Reviewer Opinion:** Keep. The human-ceiling instrument applied where it is most decisive; feeds directly into 0141's representational story.

---

## IDEA-A-0161 — The patch-quantization floor: decoder-invariance test
**Cluster 8 · Protect: RM · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 3 / ROI 4**

- **One-sentence idea:** Formally test the "patch quantization floor" — that ViT-based segmenters have an accuracy floor for objects below k× patch size that no decoder can remove — via decoder-capacity and patch-size interventions.
- **Problem:** Small-object weakness of ViT segmenters is universally observed but causally unattributed; if patch tokenization discards sub-patch information irreversibly, decoder research on small objects is futile.
- **Core Hypothesis (falsifiable):** For objects <2 patch widths, segmentation accuracy is capped regardless of decoder capacity (10× decoder sweep changes nothing), but halving patch size lifts the cap proportionally — the bottleneck is tokenization, falsified if any decoder recovers sub-patch accuracy.
- **Why Important:** Settles where the community should spend effort on small objects: tokenization/resolution (encoder side) vs decoding — with direct consequences for model design economics.
- **Why Possibly Novel:** Patch-size effects are folklore; the decoder-capacity-invariance test that isolates irreversibility has not been run.
- **Minimal Experiment:** Train patch-8/16/32 encoders × decoder capacities {1×, 3×, 10×} on size-stratified benchmarks; test the predicted invariance/scaling pattern.
- **Main Risk:** Pretrained checkpoints differ across patch sizes; control with from-scratch or re-tokenized fine-tunes.

**Survival Reason:** Settles whether small-object decoder research is futile — an interventionist design (capacity invariance × patch scaling) rather than another observation. RM-protected; pairs with 0003 (inference-side law) and 0313 (compute-matched resolution).
**Major Risks:** Checkpoint-comparability across patch sizes; training grid cost; a partial result (soft floor) is harder to headline.
**Unresolved Questions:** Do token-merging/high-res adaptation tricks circumvent the floor? Does the floor interact with 0176's compression confound (small objects deleted before tokenization)? Where do hybrid conv-stem ViTs sit?
**Required Experiments:** (1) Patch-8/16/32 × decoder-capacity {1×,3×,10×} grid on size-stratified benchmarks; (2) from-scratch or re-tokenized controls; (3) curve-collapse analysis in patch units (shared with 0003); (4) one conv-stem hybrid arm.
**Reviewer Opinion:** Keep. The causal core of the small-object program; coordinate with 0003 and 0313 to share evaluation stratification.

---

## IDEA-A-0166 — The annotation jitter floor; residuals predict the annotator
**Cluster 8 · Protect: CI · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 5**

- **One-sentence idea:** Measure the human annotation boundary-jitter floor (±how many pixels is GT itself uncertain) per dataset, and test whether models have already saturated it — meaning boundary metrics now measure annotator-style overfitting.
- **Problem:** Boundary metrics keep "improving," but if annotation jitter is ±2–3 px, sub-jitter improvements can only reflect fitting the annotator's systematic style, not reality — the saturation point has never been established per benchmark.
- **Core Hypothesis (falsifiable):** On mature benchmarks, top models' boundary error is already below the measured inter-annotator jitter, and their residual "errors" correlate with *annotator identity* (predictable from which annotator labeled the image) — proving style-fitting.
- **Why Important:** Declares boundary-metric saturation where it exists, redirecting evaluation to multi-annotator or physically defined boundaries.
- **Why Possibly Novel:** Label noise is discussed generally; the annotator-identity-prediction test for boundary residuals is a novel, sharp instrument.
- **Minimal Experiment:** Re-annotate boundary bands on 3 benchmarks (3 annotators); measure jitter; test whether model residuals predict annotator identity above chance.
- **Main Risk:** Annotator metadata is often unavailable; choose datasets where it exists or create controlled re-annotations.

**Survival Reason:** The annotator-identity-prediction test is the sharpest instrument in the batch for proving style-fitting; converts "label noise exists" into "your boundary metric measures the annotator." Protected CI.
**Major Risks:** Annotator-metadata availability; jitter measurement itself needs careful protocol or it inherits the problem it measures.
**Unresolved Questions:** Which benchmarks are boundary-saturated (feeds 0091/0327's death criterion)? Does INR-decoder smoothness exploit exactly this (0170's dissociation)? Can physically defined boundaries (0122-style) replace jittery GT?
**Required Experiments:** (1) 3-annotator boundary-band re-annotation on 3 benchmarks; (2) jitter quantification with protocol release; (3) annotator-identity prediction from model residuals; (4) saturation verdicts per benchmark.
**Reviewer Opinion:** Keep, high priority. Shares annotation infrastructure with 0091/0337; the identity-prediction result would be one of the most quoted numbers from this batch.

---

## IDEA-A-0170 — INR decoders hallucinate sub-pixel boundaries
**Cluster 8 · Protect: CI · Nov 5 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether implicit-neural-representation decoders (continuous coordinate-based mask heads) capture true sub-pixel boundary information or merely hallucinate smooth boundaries that please metrics.
- **Problem:** INR decoders output arbitrarily high-resolution masks and score well on boundary metrics, but their sub-pixel detail could be smoothness prior rather than recovered information — indistinguishable under standard evaluation.
- **Core Hypothesis (falsifiable):** On synthetic imagery with known sub-pixel ground truth, INR decoders' boundary placements correlate with true sub-pixel positions no better than bilinear upsampling + smoothing (the information isn't there), while scoring higher on human-annotated benchmarks (the smoothness matches annotator style) — a dissociation exposing metric gaming.
- **Why Important:** Distinguishes real super-resolution of masks from aesthetic smoothing — critical for measurement applications (cell morphometry, material analysis) that consume "sub-pixel" outputs.
- **Why Possibly Novel:** INR mask decoders are evaluated on human GT only; the synthetic sub-pixel-truth dissociation test is new.
- **Minimal Experiment:** Render anti-aliased synthetic scenes with exact continuous boundaries; evaluate INR vs upsampling decoders on true sub-pixel error and on human-annotated benchmarks; test the dissociation.
- **Main Risk:** Synthetic scenes may lack the texture complexity where INRs could shine; include graded-complexity scenes.

**Survival Reason:** The synthetic-truth dissociation cleanly separates recovered information from aesthetic smoothing — with real stakes for measurement applications consuming "sub-pixel" outputs. Protected CI; the constructive twin of 0166's saturation claim.
**Major Risks:** Synthetic-scene complexity ceiling; INR-decoder field is small enough that the audience is limited.
**Unresolved Questions:** Does the verdict extend to diffusion-based mask refiners? Is there any regime (strong texture gradients) where sub-pixel information is genuinely decodable?
**Required Experiments:** (1) Anti-aliased synthetic scenes with exact continuous boundaries at graded complexity; (2) INR vs bilinear+smoothing comparison on true sub-pixel error; (3) human-benchmark scoring of the same models; (4) formal dissociation test.
**Reviewer Opinion:** Keep. Small but rigorous; the metric-gaming exposure generalizes beyond INRs to any refinement method scored on human GT.

---

## IDEA-A-0174 — Register-token artifacts blind small objects
**Cluster 8 · Protect: CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 4 / ROI 5**

- **One-sentence idea:** Measure the effect of ViT attention artifacts (high-norm "register" tokens appearing in feature maps) on small-object localization, testing whether artifact positions systematically mask small instances.
- **Problem:** DINOv2-class models exhibit high-norm artifact tokens in low-information regions (motivating register tokens); whether these artifacts collide with and suppress small objects in dense prediction is an open, checkable question.
- **Core Hypothesis (falsifiable):** Small-object recall drops significantly (>10%) for instances whose spatial location coincides with artifact tokens compared to matched non-artifact locations, and register-token models show no such positional recall deficit — artifacts cause localized dense-prediction blindness.
- **Why Important:** Ties a mechanistic ViT phenomenon to a concrete downstream harm, justifying (or not) register adoption for dense tasks on evidence.
- **Why Possibly Novel:** Registers were motivated by feature-map aesthetics and probing; the small-object-collision harm analysis is new.
- **Minimal Experiment:** Localize artifact tokens per image; compare recall for artifact-coincident vs matched control instances; replicate with register-equipped models.
- **Main Risk:** Artifact locations correlate with low-information regions where small objects are rare; matching on local image statistics is essential.

**Survival Reason:** Ties a hot ViT mechanism (register tokens) to a concrete dense harm with a pure inference study; the register/no-register model pair is a natural experiment. Protected CF.
**Major Risks:** Location-statistics confound (artifacts prefer low-information regions); effect may be small once matched.
**Unresolved Questions:** Do artifacts also perturb boundary placement of large objects? Does artifact-aware inference (masking artifact tokens) recover recall without retraining?
**Required Experiments:** (1) Artifact localization per image across DINOv2-class models; (2) matched-statistics recall comparison for artifact-coincident instances; (3) register-model replication; (4) artifact-masking intervention arm.
**Reviewer Opinion:** Keep. Timely, cheap, mechanism-connected; even a null cleanly bounds a live worry about the field's favorite dense backbone.

---

## IDEA-A-0176 — Benchmark JPEG already deleted the small objects
**Cluster 8 · Protect: CI · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Audit dataset-level JPEG compression as a hidden confounder for small-object and boundary research: are benchmark small objects already destroyed by compression before models ever see them?
- **Problem:** Popular benchmarks were collected as compressed JPEGs; compression disproportionately destroys small-object texture and boundary detail, so measured "model limits" may partly be data limits — never audited.
- **Core Hypothesis (falsifiable):** On losslessly captured evaluation sets, model small-object performance is >15% higher than on JPEG-matched versions of the same scenes, and cross-benchmark differences in reported small-object difficulty correlate with dataset compression statistics — part of "small objects are hard" is "small objects were deleted."
- **Why Important:** Corrects the field's understanding of the small-object frontier and argues for lossless evaluation sets for boundary/small-object research.
- **Why Possibly Novel:** Compression robustness is studied as input perturbation; compression as *benchmark-construction confounder* for small-object conclusions is unexamined.
- **Minimal Experiment:** Capture a paired lossless/compressed evaluation set; quantify the performance delta; measure compression statistics across existing benchmarks and correlate with reported difficulty.
- **Main Risk:** New capture introduces domain shift vs benchmarks; the within-paired-set comparison carries the causal weight.

**Survival Reason:** Benchmark-construction confounder that reframes "small objects are hard" — a data-provenance insight nobody has audited. Protected CI; the capture effort is the moat.
**Major Risks:** Capture logistics and domain shift; correlational cross-benchmark arm is weaker than the paired arm.
**Unresolved Questions:** How much of the patch-floor (0161) and the failure-law knee (0003) is compression-conditional? Do modern benchmarks collected at higher quality show smaller "small-object gaps"?
**Required Experiments:** (1) Paired lossless/JPEG capture set (the causal core); (2) within-pair performance deltas by object size; (3) cross-benchmark compression-statistics survey; (4) re-interpretation analysis for 0003/0161 curves.
**Reviewer Opinion:** Keep. The kind of confounder audit that permanently changes how benchmark numbers are read; coordinate stratification with the rest of the cluster-8 program.

---

## IDEA-A-0181 — CLIP dense misalignment is co-occurrence-structured
**Cluster 9 · Protect: — (merit) · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Audit patch-level image-text alignment in CLIP-style models to establish *why* global contrastive training produces spatially misaligned dense features, and quantify the misalignment's structure.
- **Problem:** CLIP features are repurposed for segmentation despite training only for global alignment; the known "noisy dense features" problem lacks a structural characterization (is misalignment random, object-boundary-concentrated, or background-leaking?), which any fix implicitly assumes.
- **Core Hypothesis (falsifiable):** CLIP patch-text similarity systematically leaks object scores into co-occurring background regions (measurable as background-context activation exceeding object activation for >20% of classes), and the leak strength per class correlates with caption co-occurrence statistics — misalignment is co-occurrence-structured, not random noise.
- **Why Important:** Every open-vocab segmentation method inherits this structure; knowing it is co-occurrence-driven predicts exactly which classes fail and motivates targeted (not generic) fixes.
- **Why Possibly Novel:** Dense CLIP noise is widely worked around; its statistical structure and caption-statistics origin have not been directly measured.
- **Minimal Experiment:** Compute patch-text alignment maps for 80 classes on segmentation GT; quantify object-vs-context activation ratios; regress on caption co-occurrence from public corpora (e.g., LAION statistics).
- **Main Risk:** Public caption statistics only proxy CLIP's private training data; use models with released training corpora where possible.

**Survival Reason:** Structural characterization that every OV-segmentation fix implicitly assumes; the co-occurrence regression gives it a mechanism and per-class failure predictions. Survives on merit without protection flags.
**Major Risks:** Caption-statistics proxying for closed corpora; parts of the phenomenon are folklore in the OV-seg community, so the quantitative structure must carry the paper.
**Unresolved Questions:** Does the leak structure transfer to SigLIP/LLM-tower models? Can co-occurrence statistics *predict* which classes benefit from which published fix (retrospective validation)? Link to 0185: is hallucination the same co-occurrence readout?
**Required Experiments:** (1) 80-class patch-alignment maps on segmentation GT; (2) object-vs-context activation ratios; (3) co-occurrence regression on open-corpus models (LAION-trained); (4) retrospective fix-prediction analysis.
**Reviewer Opinion:** Keep. The mechanistic backbone of cluster 9; 0185 and 0187 both become more interpretable if this structure is established first.

---

## IDEA-A-0183 — Spatial-relation minimal pairs near chance
**Cluster 9 · Protect: CF · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Isolate spatial-relation reasoning ("left of", "behind", "between") as the failure locus in referring expression segmentation via minimal-pair expressions that differ only in the relation.
- **Problem:** Referring segmentation errors conflate category recognition, attribute binding, and spatial reasoning; without isolation, methods "improve" without knowing which capability moved — and spatial relations are suspected to be near-chance.
- **Core Hypothesis (falsifiable):** On minimal pairs where only the spatial relation disambiguates the target, current referring-segmentation models perform <15 points above chance, with egocentric relations ("left of") worse than intrinsic ones ("on top of") — spatial language is largely unused by the grounding pathway.
- **Why Important:** Spatial relations are the core value proposition of language-guided segmentation over class-guided; if they don't work, the field's premise needs repair.
- **Why Possibly Novel:** Spatial-reasoning weaknesses are shown for VQA; the minimal-pair segmentation isolation with relation taxonomy is not established.
- **Minimal Experiment:** Build 1k minimal-pair referring cases from images with duplicate-category instances; evaluate 5 models; stratify by relation type.
- **Main Risk:** Duplicate-instance scenes may be atypical for the models; adversarial-filtering critiques apply — validate with human performance on the same pairs.

**Survival Reason:** Tests the core value proposition of language-guided segmentation with minimal pairs — the cleanest isolation design available. Protected CF; near-chance results would be a field-level alarm.
**Major Risks:** VQA spatial-failure precedents reduce surprise; adversarial-filtering critique must be pre-empted with human baselines.
**Unresolved Questions:** Does CoT prompting move spatial-relation accuracy (link 0041)? Are failures text-encoding or fusion-side (0187's attribution machinery applies)? Does fine-tuning on relation-rich data fix it or overfit the taxonomy?
**Required Experiments:** (1) 1k minimal-pair battery over duplicate-instance scenes; (2) relation-type taxonomy stratification (egocentric/intrinsic); (3) human-performance validation; (4) encoding-vs-fusion attribution shared with 0187.
**Reviewer Opinion:** Keep. With 0185 and 0187 this forms a "language actually used?" triptych that should share scenes, models, and attribution tooling.

---

## IDEA-A-0185 — The absence benchmark: masks for absent objects
**Cluster 9 · Protect: CF+RM · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Build an "absence benchmark" measuring how often VLM-based segmenters produce confident masks for *named but absent* objects, and characterize what drives segmentation hallucination.
- **Problem:** Text-prompted segmenters are rarely tested with prompts for absent objects; deployment (e.g., "segment the tumor", "find the pedestrian") requires calibrated refusal, and hallucinated masks are the silent worst case.
- **Core Hypothesis (falsifiable):** Current OV/referring segmenters produce above-threshold masks for absent-but-scene-plausible objects in >40% of cases (vs <10% for implausible ones), with hallucination targeting the most co-occurrence-typical scene regions — hallucination is a scene-prior readout, predictable from context.
- **Why Important:** Establishes the refusal capability as a first-class metric for language-driven segmentation, which safety-relevant deployments need before adoption.
- **Why Possibly Novel:** Object hallucination is studied for captioning/VQA; the *mask-producing* hallucination benchmark with plausibility gradients is missing.
- **Minimal Experiment:** Construct present/absent-plausible/absent-implausible prompt triads over 1k images; measure mask-emission rates and confidence; analyze spatial targets of hallucinated masks.
- **Main Risk:** "Absent" requires exhaustive annotation; use densely annotated datasets (ADE20K/LVIS) to certify absence.

**Survival Reason:** Makes refusal a first-class metric with a plausibility-graded design and a mechanism claim (scene-prior readout). Protected CF+RM; absorbs 0314's detection-side extension as a follow-on arm.
**Major Risks:** Absence certification labor; captioning-hallucination precedents mean the mask-level and plausibility-gradient parts must carry the novelty.
**Unresolved Questions:** Do hallucinated masks land where 0181's co-occurrence leak predicts? How does hallucination scale under domain shift (0314's question)? What refusal mechanisms (thresholds, verbalized confidence) actually work?
**Required Experiments:** (1) Present/absent-plausible/absent-implausible triads over densely annotated images; (2) mask-emission and confidence analysis; (3) spatial-target analysis against co-occurrence maps (0181 linkage); (4) shift-conditioned extension (0314's content) as arm two.
**Reviewer Opinion:** Keep. Deployment-critical, benchmark-shaped, and mechanistically connected to the cluster's backbone; medical twin 0118 shares the refusal framing.

---

## IDEA-A-0187 — Negation: worse than chance, a fusion failure
**Cluster 9 · Protect: CI+CF · Nov 4 / Sig 5 / SciQ 5 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Measure whether referring segmentation models process negation ("the cup that is not red") above chance, and whether failures are text-encoding or vision-grounding failures.
- **Problem:** Negation is frequent in natural instructions but suspected to be ignored by VLMs; for segmentation, negation failure produces exactly-wrong outputs (the negated object), which is worse than random — the failure severity and locus are unmeasured.
- **Core Hypothesis (falsifiable):** On negated referring expressions with two-candidate scenes, models select the *negated* (wrong) object above 50% (systematic anti-accuracy, worse than chance), and text-embedding probes show negation is representable but unused by the grounding head — a fusion failure, not an encoding failure.
- **Why Important:** Systematically inverted behavior under negation is a deployment hazard for instruction-following robots; locating the failure enables targeted repair.
- **Why Possibly Novel:** Negation blindness is documented for CLIP retrieval; the segmentation-specific anti-accuracy phenomenon and encoding-vs-fusion attribution are new.
- **Minimal Experiment:** Two-object scenes with negated referring prompts; measure choice rates; probe text embeddings for negation decodability; compare against fusion-layer attribution.
- **Main Risk:** Prompt phrasing variety matters; use many syntactic negation forms to avoid overfitting conclusions to one construction.

**Survival Reason:** Anti-accuracy (worse than random) is a qualitatively different and scarier claim than "models ignore negation"; the encoding-vs-fusion attribution gives it a locatable cause. Protected CI+CF.
**Major Risks:** CLIP-retrieval negation precedents; phrasing-form overfitting; newer instruction-tuned models may already partially handle negation, compressing the effect.
**Unresolved Questions:** Does anti-accuracy persist in LLM-fused segmenters? Is the fix at fusion (as the probe predicts) — and does a small fusion fine-tune repair it without collateral damage?
**Required Experiments:** (1) Two-candidate scenes × many syntactic negation forms; (2) choice-rate analysis vs chance; (3) text-embedding negation-decodability probes; (4) fusion-layer attribution; (5) minimal-repair fine-tune arm as the causal confirmation.
**Reviewer Opinion:** Keep. The single most deployment-alarming finding available in cluster 9 if confirmed; shares all infrastructure with 0183/0185.

---

## IDEA-A-0199 — Scene text hijacks grounding
**Cluster 9 · Protect: CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 4 / ROI 5**

- **One-sentence idea:** Measure interference from scene text (signs, labels, watermarks) on VLM grounding: does written text in images hijack text-prompted segmentation toward regions containing matching words?
- **Problem:** VLMs read scene text; a prompt for "stop" may ground to a stop sign's *text* rather than the requested object concept, and adversarial or incidental text may hijack masks — an interference channel unquantified for dense prediction.
- **Core Hypothesis (falsifiable):** Planting prompt-matching scene text shifts grounding to the text region in >30% of cases for OCR-capable VLMs (and near 0% for CLIP-class models without strong OCR), with hijack probability scaling with text size — grounding inherits typographic-attack vulnerability in proportion to OCR capability.
- **Why Important:** Typographic hijacking of *masks* enables real attacks (adversarial signage) and everyday failures (product labels); the OCR-capability link identifies which models are exposed.
- **Why Possibly Novel:** Typographic attacks are known for CLIP classification; the dense-grounding hijack with capability-scaling analysis is new.
- **Minimal Experiment:** Composite prompt-matching text into scenes at controlled sizes/positions; measure grounding-shift rates across models with graded OCR ability.
- **Main Risk:** Compositing artifacts; replicate top findings with physically photographed text-in-scene setups.

**Survival Reason:** Extends typographic attacks to masks with a capability-scaling law (hijack ∝ OCR ability) — a predictive, not merely demonstrative, security result. Protected CF.
**Major Risks:** Compositing artifacts; classification-attack precedents; capability-scaling requires a good OCR-ability measure across models.
**Unresolved Questions:** Does incidental (non-adversarial) scene text measurably degrade everyday grounding benchmarks? Are there cheap inference-time defenses (text-region masking)?
**Required Experiments:** (1) Controlled text compositing across sizes/positions; (2) grounding-shift measurement across OCR-graded models; (3) physical photographed replication of headline cases; (4) incidental-text audit on standard benchmarks; (5) defense probe.
**Reviewer Opinion:** Keep. Security framing plus scaling law makes this more than a stunt; cheap and self-contained.

---
## IDEA-A-0202 — The task×backbone matrix for frozen dense features
**Cluster 10 · Protect: — (merit) · Nov 3 / Sig 5 / SciQ 4 / Feas 4 / Unp 2 / ROI 5**

- **One-sentence idea:** Build the definitive task×backbone matrix for frozen dense features (DINOv2, CLIP, SAM, MAE-class) under matched probing protocols, testing whether any single "best dense backbone" exists or dominance is task-structured.
- **Problem:** Backbone choice for dense tasks is driven by fashion and scattered single-task probes with inconsistent protocols; the community lacks a controlled dominance map and a theory of *which* pretraining objective wins *where*.
- **Core Hypothesis (falsifiable):** No backbone dominates: objective type predicts the winner per task family (contrastive→semantics, MIM→texture/depth, segmentation-supervised→boundaries), with the pattern stable across probe capacities — falsified if one backbone Pareto-dominates.
- **Why Important:** The matrix would be an immediately used community resource and would ground "which objective learns what" claims in controlled evidence.
- **Why Possibly Novel:** Partial probing comparisons abound; the matched-protocol matrix with objective-family analysis and capacity controls is missing.
- **Minimal Experiment:** 5 backbones × 6 dense tasks × 3 probe capacities × 3 seeds, one shared harness; release everything.
- **Main Risk:** Backbones differ in scale/data, confounding the objective attribution; include scale-matched pairs where possible and state limits.

**Survival Reason:** Community-resource value: the matched-protocol matrix that absorbs killed 0012/0023 and grounds a dozen other survivors' backbone choices. Survives on merit despite modest novelty.
**Major Risks:** Scale/data confounds limit objective-level attribution; partial matrices in the literature erode surprise; harness design choices will be litigated.
**Unresolved Questions:** Which cells are protocol-fragile (flip under probe capacity)? Do objective-family predictions hold on scale-matched pairs? How fast does the matrix date as new VFMs ship?
**Required Experiments:** (1) 5-backbone × 6-task × 3-capacity × 3-seed grid under one released harness; (2) scale-matched pair analysis; (3) objective-family regression; (4) versioned public release with add-a-model protocol.
**Reviewer Opinion:** Keep. Not glamorous, but half of Batch A implicitly assumes this matrix exists; building it well is high-leverage service science.

---

## IDEA-A-0203 — SSL "object emergence" is a crop-statistics artifact
**Cluster 10 · Protect: HR+CI · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Test whether "emergent segmentation" in self-supervised ViT attention maps is a genuine objecthood representation or an artifact of the cropping-based augmentation statistics used in pretraining.
- **Problem:** Attention-based object emergence (DINO-style) is celebrated as evidence SSL learns objects; but random-crop augmentation makes centered, large objects statistically special, so the "emergence" may be an augmentation echo — the causal driver is untested.
- **Core Hypothesis (falsifiable):** Retraining with object-decentered cropping statistics substantially degrades attention-object alignment (>40% relative) without harming downstream classification — object emergence is largely an augmentation artifact, falsified if emergence survives decentered training.
- **Why Important:** The claim "SSL discovers objects" shapes theory and method design; knowing it is (or isn't) an augmentation artifact recalibrates what SSL actually learns.
- **Why Possibly Novel:** Emergence has been replicated widely but its causal origin in augmentation statistics has not been intervened upon.
- **Minimal Experiment:** Pretrain matched SSL models with standard vs decentered vs object-aware cropping; measure attention-mask alignment and downstream transfer.
- **Main Risk:** Retraining SSL models is compute-heavy; mid-scale models suffice for the causal question.

**Survival Reason:** Protected HR+CI: a causal intervention on one of SSL's most celebrated narratives. Expensive (SSL retraining) but the question is exactly the kind Stage 2 should protect rather than let compute-cost kill.
**Major Risks:** Mid-scale results may not persuade believers in large-scale emergence; decentered cropping changes more than object statistics (context diversity).
**Unresolved Questions:** Does the artifact account also explain 0266's texture-vs-object question (shared program)? Do video-SSL models (motion signal) show crop-independent emergence? What crop statistics maximize/minimize emergence?
**Required Experiments:** (1) Matched SSL pretraining under {standard, decentered, object-aware} cropping at mid-scale; (2) attention-object alignment and downstream transfer; (3) dose-response over crop-centering statistics; (4) shared dissociation-scene evaluation with 0266.
**Reviewer Opinion:** Keep under HR protection. The single most theory-relevant idea in cluster 10; run 0266 first as the cheap correlational prelude, then this as the causal strike.

---

## IDEA-A-0207 — Data vs method: the variance decomposition
**Cluster 10 · Protect: RM · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Quantify how much of inter-VFM downstream variance is explained by training *data* overlap versus objective and architecture, using models with disclosed corpora.
- **Problem:** The community attributes model differences to objectives and architectures, but training-data composition is a massive uncontrolled variable; without decomposition, method-level conclusions drawn from model comparisons are unreliable.
- **Core Hypothesis (falsifiable):** For models with known corpora, a data-overlap kernel predicts pairwise downstream-behavior similarity (error correlation across a dense-task suite) better than objective or architecture indicators — data explains more variance than method, falsified if method indicators dominate.
- **Why Important:** If data dominates, the field's method-comparison literature needs data-controlled re-examination, and open-data models become scientifically privileged.
- **Why Possibly Novel:** "Data vs method" is debated qualitatively; a quantitative variance decomposition over public VFMs has not been performed.
- **Minimal Experiment:** Assemble 10+ open-data models; compute pairwise behavior similarity on dense suites; regress on data-overlap, objective, and architecture kernels.
- **Main Risk:** Open-data model pool is limited and unbalanced; report the decomposition's stability under leave-one-out.

**Survival Reason:** RM-protected: "data explains more than method" would force re-reading of the comparison literature, and the kernel-regression methodology will be fought over — the productive kind of controversy.
**Major Risks:** Small, unbalanced open-data model pool; kernel design choices determine the answer; correlational, not interventional.
**Unresolved Questions:** Is the pool (≥10 open-data VFMs) sufficient in 2026? Can targeted mini-pretrains (same data, different objective) add interventional anchors? How does this interact with 0202's matrix (same evaluation suite)?
**Required Experiments:** (1) Open-data model assembly; (2) pairwise error-correlation computation on 0202's dense suite; (3) three-kernel regression with leave-one-out stability; (4) 2–3 interventional mini-pretrain anchors if budget allows.
**Reviewer Opinion:** Keep under protection. Fragile but important; sharing the evaluation suite with 0202 halves its cost and doubles its credibility.

---

## IDEA-A-0211 — Texture-vs-shape verdict inverts for dense readouts
**Cluster 10 · Protect: CI · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 3 / ROI 4**

- **One-sentence idea:** Re-measure texture-vs-shape bias in modern VFMs (DINOv2, CLIP, SAM-class) with dense-prediction-relevant stimuli, testing whether the CNN-era texture bias actually disappeared or merely moved.
- **Problem:** "Transformers are shape-biased" is now folklore based on classification-oriented cue-conflict tests; whether dense predictions (masks) follow shape or texture under conflict — the version that matters for segmentation — has not been measured.
- **Core Hypothesis (falsifiable):** Under texture-shape cue-conflict for segmentation (shape of A textured as B), modern VFM-based segmenters follow *texture boundaries* in >40% of cases despite classifying by shape — the bias verdict inverts between classification and dense readouts of the same backbone.
- **Why Important:** If dense readouts are texture-driven while classification is shape-driven, bias conclusions from classification probes are invalid for segmentation applications — a significant reinterpretation.
- **Why Possibly Novel:** Cue-conflict methodology exists; its dense-output version with the within-model dissociation is new.
- **Minimal Experiment:** Build cue-conflict segmentation stimuli; measure mask allegiance (shape vs texture boundary) across backbones/readouts; compare with classification allegiance of the same models.
- **Main Risk:** Synthesizing convincing cue-conflict at mask level is harder than at image level; use style-transfer plus careful GT definitions.

**Survival Reason:** Within-model dissociation (same backbone, opposite bias verdicts by readout) would invalidate a folklore claim exactly where it is applied. Protected CI; stimulus construction is the main cost.
**Major Risks:** Mask-level cue-conflict synthesis quality; GT definition disputes on conflicted stimuli.
**Unresolved Questions:** Does the inversion (if found) track decoder architecture or encoder features (probe-level analysis)? How does it relate to 0001's edge-allegiance and 0266's texture-grouping findings — one underlying texture-following account?
**Required Experiments:** (1) Style-transfer cue-conflict stimulus battery with pre-registered GT rules; (2) mask-allegiance measurement across backbones × readouts; (3) matched classification-allegiance comparison; (4) probe-level localization of where allegiance is set.
**Reviewer Opinion:** Keep. Connects three survivors (0001, 0266) under a possible common mechanism; the within-model inversion is the quotable result.

---

## IDEA-A-0223 — In-context segmentation: abstraction or copying?
**Cluster 10 · Protect: CI · Nov 5 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4**

- **One-sentence idea:** Determine whether in-context segmentation (SegGPT/Painter-style visual prompting) performs abstraction or sophisticated nearest-neighbor copying, via support-query relationship manipulations.
- **Problem:** In-context dense models appear to "understand" tasks from one example, but the mechanism — abstract task inference vs feature-matched label transfer — is undetermined, and the two predict different generalization limits.
- **Core Hypothesis (falsifiable):** Performance collapses (>50% relative) when support and query share task semantics but differ in low-level statistics (style-shifted supports), while remaining high for semantically-different but visually-similar supports — behavior tracks visual similarity, not task abstraction; falsified if the opposite pattern holds.
- **Why Important:** If in-context segmentation is nearest-neighbor copying, its failure conditions are predictable (and its "task generalization" marketing overstated); if abstraction, it deserves aggressive scaling.
- **Why Possibly Novel:** In-context mechanism analysis exists for LLMs; the visual-dense version with the similarity-vs-semantics dissociation design is new.
- **Minimal Experiment:** Build support-query grids crossing semantic-match × visual-match; evaluate in-context segmenters; identify which axis controls performance.
- **Main Risk:** Style manipulation may degrade supports' usability for any mechanism; calibrate degradation with oracle fine-tuned models.

**Survival Reason:** Mechanism dissociation with a 2×2 design (semantic-match × visual-match) that predicts generalization limits either way; the strongest of the several allegiance-dissociation ideas in the batch (kills 0257 by covering the sharper target).
**Major Risks:** Style manipulation degradation confound; in-context dense model pool is small.
**Unresolved Questions:** Does scale shift the copying→abstraction balance? Do retrieval-augmented pipelines (support selection, killed 0252's topic) exploit or mask the mechanism? Does the verdict predict cross-domain in-context failure?
**Required Experiments:** (1) Semantic×visual support-query grid; (2) oracle fine-tuned calibration of style-degradation; (3) ≥3 in-context models; (4) cross-domain validation of the predicted failure conditions.
**Reviewer Opinion:** Keep. LLM-style mechanism science ported to dense vision with a design that genuinely discriminates; results will steer whether in-context segmentation deserves scaling investment.

---

## IDEA-A-0225 — Platonic convergence is semantics-only at patch level
**Cluster 10 · Protect: RM · Nov 5 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4**

- **One-sentence idea:** Test the "platonic convergence" claim at the *patch* level: are different VFMs' dense feature spaces converging to affinely equivalent representations, or does convergence hold only for global semantics?
- **Problem:** Evidence suggests foundation models converge toward shared representations at the global level; if dense/spatial features do not converge equivalently, model interchangeability assumptions (feature swapping, cross-model distillation, universal decoders) fail in unmapped ways.
- **Core Hypothesis (falsifiable):** Cross-model affine alignment of patch features achieves high fidelity for semantic content (class decodability preserved >90%) but low fidelity for geometric content (boundary/position decodability <50% preserved) — convergence is semantics-only, falsified if geometric content aligns equally well.
- **Why Important:** Defines the real limits of model-agnostic dense tooling (universal decoders, cross-model probes) and refines a prominent theoretical narrative with dense-level evidence.
- **Why Possibly Novel:** Representational convergence is measured with global similarity metrics; the semantic-vs-geometric decomposition of dense alignment is new.
- **Minimal Experiment:** Fit affine maps between patch spaces of 6 VFM pairs; measure preservation of semantic vs geometric decodability through the maps.
- **Main Risk:** Affine may be the wrong alignment class; include lightweight nonlinear aligners as robustness checks.

**Survival Reason:** Tests a fashionable theory (platonic representation hypothesis) exactly at the level where it should break; the semantic/geometric decomposition is a new instrument. RM-protected — theory partisans will dispute alignment classes.
**Major Risks:** Alignment-class sensitivity; the theory's own literature is moving fast, so timing matters.
**Unresolved Questions:** Does convergence increase with model scale (the theory's core prediction) for geometric content too? Do universal-decoder failures in practice match the predicted geometric non-transfer?
**Required Experiments:** (1) Affine + lightweight nonlinear alignment across 6 VFM pairs; (2) semantic-vs-geometric decodability preservation; (3) scale-ladder analysis within one family; (4) practical validation via cross-model decoder swapping.
**Reviewer Opinion:** Keep. High theory-relevance per GPU-hour; shares feature extraction with 0202's harness.

---

## IDEA-A-0226 — Attention-U-Net gains are baseline artifacts
**Cluster 11 · Protect: RM · Nov 4 / Sig 5 / SciQ 4 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Reproduce a representative sample of "attention module added to U-Net" medical segmentation papers under tuned baselines to test whether the reported gains survive — a targeted replication study of the field's most common paper template.
- **Problem:** Hundreds of medical segmentation papers add attention modules to U-Nets and report 1–2 Dice gains, typically against under-tuned baselines with single seeds; the aggregate reliability of this literature is unknown but heavily cited.
- **Core Hypothesis (falsifiable):** Under matched tuning budgets and ≥5 seeds, more than half of the sampled modules' gains fall within seed noise of the tuned plain baseline — the module literature's effect sizes are substantially baseline-artifact.
- **Why Important:** This paper template shapes clinical-AI development choices; a rigorous replication estimate recalibrates trust and redirects effort toward what actually moves performance (data, recipes).
- **Why Possibly Novel:** Replication studies exist in ML broadly; a systematic one for this dominant medical-segmentation genre with tuned-baseline methodology has not been done.
- **Minimal Experiment:** Sample 15 published modules with available code; re-run with standardized tuned baselines, 5 seeds, matched schedules; report effect-size distribution with CIs.
- **Main Risk:** Author pushback over tuning choices; pre-register the protocol and invite original authors to review configs.

**Survival Reason:** Powered replication of the field's most common paper template — the highest-volume target for a falsification study in all of Batch A. RM-protected by construction.
**Major Risks:** Author disputes over tuning; module sampling bias accusations; substantial compute across 15 modules × 5 seeds.
**Unresolved Questions:** What fraction of gains survive, and do survivors share a mechanism? Does the effect-size distribution show the publishability discontinuity 0242 predicts (natural data-sharing)? How should reviewers weight module papers afterward?
**Required Experiments:** (1) Pre-registered sampling of 15 coded modules; (2) tuned-baseline re-runs, 5 seeds, matched schedules; (3) effect-size distribution with CIs; (4) author-review of configs before publication; (5) feed deltas into 0242's z-curve.
**Reviewer Opinion:** Keep. Run jointly with 0242 (this is its ground-truthed subsample) and 0245 (recipe attribution); together they are the negative-results backbone of the batch.

---

## IDEA-A-0238 — Depth auxiliary vs semantically-empty auxiliary
**Cluster 11 · Protect: CI · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4**

- **One-sentence idea:** Test whether auxiliary depth estimation genuinely improves segmentation or whether the reported multi-task benefit is explained by the extra supervision acting as a regularizer replaceable by label-free alternatives.
- **Problem:** Depth-auxiliary gains for segmentation are cited as evidence of geometric synergy; but any auxiliary target correlated with image structure might regularize equally well, and the synergy-vs-regularization question determines whether depth labels are worth acquiring.
- **Core Hypothesis (falsifiable):** Replacing depth supervision with structurally similar but semantically empty auxiliaries (predicting blurred luminance, or *shuffled-pair* depth) recovers >70% of the multi-task gain — the benefit is generic regularization, falsified if true depth outperforms matched pseudo-auxiliaries.
- **Why Important:** Labs pay for depth sensors/labels on synergy claims; the control experiment separating information content from regularization has been skipped.
- **Why Possibly Novel:** Multi-task ablations compare task sets; the semantically-empty matched-auxiliary control is a sharper instrument not yet applied.
- **Minimal Experiment:** {seg-only, +depth, +empty-auxiliary variants} × 3 datasets × 5 seeds; compare gain fractions.
- **Main Risk:** Designing truly "structurally matched, semantically empty" auxiliaries is subtle; use several variants to triangulate.

**Survival Reason:** The semantically-empty-auxiliary control is a genuinely new instrument applicable to every multi-task synergy claim; depth is just the first target. Protected CI.
**Major Risks:** "Structurally matched, semantically empty" is hard to certify; a middle result (partial recovery) needs careful interpretation.
**Unresolved Questions:** Which auxiliary families (normals, edges, SSL targets) survive the control? Does the verdict flip in low-data regimes? Can the instrument be standardized as a reporting requirement for multi-task papers?
**Required Experiments:** (1) {seg-only, +depth, +≥3 empty-auxiliary variants} × 3 datasets × 5 seeds; (2) gain-fraction decomposition; (3) low-data stratification; (4) methods-note formalizing the control for reuse.
**Reviewer Opinion:** Keep. The instrument outlives the depth question; this is methodology-building disguised as an ablation.

---

## IDEA-A-0239 — Entropy TTA silently collapses rare classes
**Cluster 11 · Protect: CF · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Audit entropy-minimization test-time adaptation (TENT-class) on segmentation for silent class collapse, and characterize the conditions (class imbalance, shift type) that trigger it.
- **Problem:** TTA methods validated on classification are applied to segmentation, where entropy minimization can collapse rare classes into dominant ones while *improving* average metrics — a dangerous failure whose triggering conditions are unmapped.
- **Core Hypothesis (falsifiable):** On class-imbalanced segmentation under shift, entropy-based TTA improves mIoU while reducing rare-class IoU by >30% relative in a predictable fraction of cases, with collapse probability rising with batch-level class skew — average metrics actively hide the harm, falsified if rare-class performance tracks average gains.
- **Why Important:** TTA is entering safety-relevant deployments; documenting the collapse regime with predictive triggers is prerequisite to safe use.
- **Why Possibly Novel:** TTA instability is noted anecdotally; the class-collapse characterization with trigger conditions for dense tasks is not established.
- **Minimal Experiment:** Run 4 TTA methods across shift benchmarks; track per-class trajectories during adaptation; model collapse probability from batch statistics.
- **Main Risk:** Collapse depends on implementation details (BN vs LN adaptation); cover both normalization regimes.

**Survival Reason:** Safety-relevant hidden harm (averages improve while rare classes die) with predictive triggers; inference-scale cost. Protected CF; the science that killed 0298's engineering sibling.
**Major Risks:** Anecdotal awareness in the TTA community; implementation-detail dependence (BN vs LN) doubles the grid.
**Unresolved Questions:** Are trigger conditions (batch skew) stable enough for deployment guardrails (0298's inherited goal)? Does collapse interact with 0335's worst-class metric agenda? Which TTA families are structurally immune?
**Required Experiments:** (1) 4-method × shift-benchmark grid with per-class trajectory logging; (2) collapse-probability modeling from batch statistics; (3) BN and LN regimes; (4) trigger-validation on held-out shifts.
**Reviewer Opinion:** Keep. The characterization is the durable contribution; guardrail engineering (0298) can follow once triggers are established.

---

## IDEA-A-0242 — Publication bias: the z-curve for segmentation deltas
**Cluster 11 · Protect: RM · Nov 5 / Sig 5 / SciQ 4 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Estimate publication bias in segmentation literature by comparing the distribution of reported improvements against the expected null distribution from seed noise (z-curve/caliper analysis of reported deltas).
- **Problem:** If many reported gains cluster just above significance/noise thresholds, the literature's aggregate evidential value is inflated by selection; segmentation-specific quantification of this bias does not exist.
- **Core Hypothesis (falsifiable):** Reported improvement distributions show a discontinuity at the informal ~0.5–1.0 point "publishability threshold" (excess mass just above, deficit just below) inconsistent with any smooth true-effect distribution — quantifiable selection bias, falsified if the distribution is smooth.
- **Why Important:** A measured selection-bias coefficient for the field would contextualize every small reported gain and strengthen the case for preregistration and seed-reporting norms.
- **Why Possibly Novel:** Z-curve methods exist in psychology's replication literature; application to segmentation benchmark deltas is new.
- **Minimal Experiment:** Extract reported deltas from 500+ segmentation papers (automated parsing + manual verification); fit discontinuity models against seed-noise nulls estimated from public multi-seed studies.
- **Main Risk:** Reported deltas are heterogeneous (different benchmarks/metrics); normalize within benchmark-metric strata.

**Survival Reason:** A field-level selection-bias coefficient — one number that contextualizes every small reported gain. RM-protected; honest port of psychology's replication methodology.
**Major Risks:** Delta heterogeneity across benchmarks/metrics; seed-noise null estimation depends on scarce multi-seed studies (killed 0326's tables would have helped — use its logic on a smaller scale).
**Unresolved Questions:** Does the discontinuity vary by venue/subfield? Do 0226's replication results calibrate the caliper (ground truth for a subsample)? What reporting reforms does the measured coefficient justify?
**Required Experiments:** (1) Automated + verified delta extraction from 500+ papers; (2) within-stratum normalization; (3) discontinuity model vs smooth-effect nulls; (4) calibration against 0226's re-run subsample; (5) reform proposal.
**Reviewer Opinion:** Keep. Meta-science with teeth; pairing with 0226 turns a distributional argument into a ground-truthed one.

---

## IDEA-A-0245 — A 2015 U-Net with a 2026 recipe
**Cluster 11 · Protect: RM · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Re-train decade-old architectures (original U-Net, DeepLab-era models) with fully modern recipes to measure what fraction of a decade's reported segmentation progress is recipe rather than architecture.
- **Problem:** Progress narratives credit architectures, but recipes (augmentation, schedules, normalization, pretraining) improved simultaneously; the attribution has never been settled for segmentation, distorting where the field believes value comes from.
- **Core Hypothesis (falsifiable):** Modern-recipe U-Net (2015 architecture) closes >60% of the reported gap to modern architectures on standard benchmarks — most of a decade's progress is recipe, falsified if the architecture gap survives recipe equalization.
- **Why Important:** Correct attribution redirects research investment (recipes and data vs architecture novelty) and recalibrates how reviewers weigh architectural contributions.
- **Why Possibly Novel:** Similar studies exist for classification (ResNet strikes back); the segmentation version across the U-Net-to-transformer decade has not been done.
- **Minimal Experiment:** Train {U-Net-2015, DeepLabv3, SegFormer, Mask2Former} under identical modern recipes at matched compute on 4 benchmarks; decompose the historical gap.
- **Main Risk:** "Modern recipe" choices favor some architectures; tune recipes per-architecture within a fixed budget for fairness.

**Survival Reason:** The batch flagship falsification study: index surprising-#1, deservedly. "ResNet strikes back" for segmentation, with the decade-attribution number every reviewer will quote whichever way it lands.
**Major Risks:** Recipe-fairness disputes (per-architecture tuning budgets); classification precedent means execution rigor is the differentiator; compute-heavy.
**Unresolved Questions:** Does the recipe fraction differ by benchmark type (medical vs natural)? Where do pretraining effects sit in the decomposition (recipe or architecture-enabler)? How does the verdict interact with 0093's nnU-Net question and 0226's module audit?
**Required Experiments:** (1) 4-architecture × 4-benchmark grid under equalized, per-architecture-tuned recipes at matched compute; (2) gap decomposition vs historical reported numbers; (3) pretraining-effect isolation arm; (4) coordinated analysis with 0093/0226.
**Reviewer Opinion:** Keep, top priority. If Batch A funds three expensive studies, this is one of them (with 0093 and 0203); the attribution number becomes field infrastructure.

---
## IDEA-A-0246 — FSS scores are base-class proximity in disguise
**Cluster 12 · Protect: CF · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Audit base-class leakage in few-shot segmentation benchmarks: how much of reported FSS performance comes from novel classes resembling base classes seen during episodic training?
- **Problem:** FSS protocols split classes into base/novel, but visual similarity between splits (novel "sheep" after base "cow") means "few-shot" performance partly measures base-class generalization — the leakage magnitude has never been quantified.
- **Core Hypothesis (falsifiable):** Per-novel-class FSS performance correlates strongly (ρ > 0.7) with feature-space proximity to the nearest base class, and re-splitting benchmarks to maximize base-novel distance drops reported SOTA by >15 IoU — much of "few-shot learning" is near-class transfer.
- **Why Important:** If FSS scores are dominated by split geometry, method comparisons are confounded and truly-novel-class deployment expectations are inflated.
- **Why Possibly Novel:** Class-split criticism exists for few-shot classification; the quantified leakage analysis with distance-controlled re-splits for segmentation is missing.
- **Minimal Experiment:** Compute base-novel proximity for standard splits (PASCAL-5i/COCO-20i); correlate with per-class results of 5 published methods; construct and evaluate max-distance splits.
- **Main Risk:** Feature-space proximity depends on the embedding used; replicate with multiple embeddings.

**Survival Reason:** Cheap, decisive audit of the FSS protocol itself; the max-distance re-split is a constructive deliverable, not just criticism. Protected CF.
**Major Risks:** Embedding-dependence of proximity; classification-side precedents reduce surprise; FSS community pushback on re-splits.
**Unresolved Questions:** Do method rankings change on max-distance splits (the practical question)? How does leakage interact with 0250's meta-learning-vs-fine-tuning verdict? Should re-splits become the standard protocol?
**Required Experiments:** (1) Proximity computation under ≥3 embeddings; (2) per-class correlation across 5 published methods; (3) max-distance re-split construction and re-evaluation; (4) ranking-stability analysis.
**Reviewer Opinion:** Keep. With 0250 it forms a two-pronged audit of whether FSS-as-practiced measures what it claims; both are inference-scale.

---

## IDEA-A-0250 — Meta-learning vs direct fine-tuning, cross-domain
**Cluster 12 · Protect: CF · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether episodic meta-training helps at all for cross-domain few-shot segmentation (natural→medical/aerial), versus simply fine-tuning a foundation model on the 5 available target images.
- **Problem:** Meta-learning claims to teach "how to learn from few examples," but for cross-domain deployment the mundane alternative — directly fine-tuning on the shots — is rarely compared fairly; practitioners don't know which to use.
- **Core Hypothesis (falsifiable):** Direct 5-shot fine-tuning (with modern PEFT and augmentation) beats episodically meta-trained FSS models on cross-domain targets by >5 IoU — meta-training's benefit does not survive domain shift, falsified if meta-trained models win cross-domain.
- **Why Important:** The comparison determines whether cross-domain FSS research should exist as a distinct enterprise or collapse into few-sample fine-tuning practice.
- **Why Possibly Novel:** Within-domain comparisons exist; the cross-domain audit with modern fine-tuning baselines is missing.
- **Minimal Experiment:** 4 cross-domain targets × {meta-trained FSS, PEFT fine-tune, training-free matching} at identical shot budgets; 5 support-set resamples each.
- **Main Risk:** Fine-tuning needs hyperparameters chosen without target validation data; use a fixed cross-domain-validated recipe to keep it honest.

**Survival Reason:** Existence test for a subfield with a fixed-recipe honesty constraint; cheap and directly decision-relevant for practitioners. Protected CF.
**Major Risks:** Hyperparameter honesty is hard to police; meta-learning defenders will dispute the FSS model selection.
**Unresolved Questions:** Does the verdict flip with shot count (1 vs 5 vs 20)? Where does training-free matching (killed 0247's content, folded here as the third arm) sit? Does 0246's leakage explain any within-domain meta-learning advantage?
**Required Experiments:** (1) 4 cross-domain targets × 3 method families × 5 support resamples; (2) pre-registered fixed fine-tuning recipe; (3) shot-count ladder; (4) joint interpretation with 0246.
**Reviewer Opinion:** Keep. The training-free arm inherits 0247's question at zero extra cost, making this the consolidated FSS-reality-check study.

---

## IDEA-A-0254 — A provably-novel synthetic zero-shot benchmark
**Cluster 12 · Protect: RM · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4 · Risk H**

- **One-sentence idea:** Construct a true-zero-shot benchmark from procedurally synthesized never-seen categories to measure how much of "zero-shot segmentation" survives when pretraining exposure is provably zero.
- **Problem:** Zero-shot claims are untestable on natural categories (everything is in web data somewhere, cf. IDEA-A-0194); provably novel synthetic categories with controllable structure would give the first clean zero-shot measurement.
- **Core Hypothesis (falsifiable):** On procedurally generated novel object categories (parametric shape-texture grammars, verified absent from training corpora), OV segmentation performance drops >40% relative to matched-difficulty natural categories — a large share of "zero-shot" is memory, falsified if synthetic-novel performance matches natural.
- **Why Important:** Provides the field's first uncontaminated zero-shot number and a reusable instrument for honest evaluation of future models.
- **Why Possibly Novel:** Synthetic OOD objects exist for detection robustness; the calibrated-difficulty, contamination-proof zero-shot benchmark for segmentation is new.
- **Minimal Experiment:** Build the generator with difficulty calibration (human segmentability matching to natural classes); evaluate 5 OV models on matched natural/synthetic pairs.
- **Main Risk:** Synthetic rendering artifacts confound difficulty matching; use human performance as the difficulty anchor.

**Survival Reason:** The contamination-proof instrument the zero-shot literature lacks; absorbs 0194's accounting question and 0333's adjusted-scores agenda into one clean construction. RM-protected.
**Major Risks:** Difficulty calibration between synthetic and natural is the whole game; rendering-artifact shortcuts; "synthetic isn't representative" critiques.
**Unresolved Questions:** Can human-segmentability anchoring really equate difficulty? How much does the drop vary across model families (memory-heavy vs alignment-heavy)? Can the generator parameterize compositional novelty gradients?
**Required Experiments:** (1) Shape-texture grammar generator with corpus-absence verification; (2) human-anchored difficulty calibration; (3) 5-model natural/synthetic matched evaluation; (4) novelty-gradient analysis; (5) public release as a living instrument.
**Reviewer Opinion:** Keep under protection. Construction-heavy but this is the reusable instrument version of three killed audit ideas — the right consolidation.

---

## IDEA-A-0261 — WSSS's residual gap is structural extent error
**Cluster 13 · Protect: RM · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Decompose the remaining gap in image-label-only weakly supervised semantic segmentation (WSSS) into localization, extent, and boundary components to test whether the CAM paradigm has hit a structural ceiling.
- **Problem:** WSSS progress has slowed near a performance plateau; without knowing whether the residual gap is in finding objects, estimating their extent, or delineating boundaries, the field cannot tell if the CAM-seed paradigm is exhausted or under-optimized.
- **Core Hypothesis (falsifiable):** ≥70% of the residual gap to full supervision is extent error (systematic under/over-coverage of discriminative regions), which is *structural* to classification-derived localization — oracle boundary refinement barely helps, and no CAM-family method can close it, falsified if boundary refinement recovers most of the gap.
- **Why Important:** Declares (with evidence) whether WSSS research should abandon the CAM paradigm for foundation-model-based alternatives, ending a possibly futile optimization race.
- **Why Possibly Novel:** WSSS papers optimize the pipeline; the component-wise ceiling analysis of the paradigm itself is not published.
- **Minimal Experiment:** For 5 WSSS methods, replace each pipeline stage with oracles (perfect seeds, perfect extent, perfect boundaries); attribute the residual gap per component.
- **Main Risk:** Oracle definitions influence attribution; use multiple oracle constructions and report ranges.

**Survival Reason:** Oracle-substitution ceiling analysis that could end a subfield's optimization race with evidence; the paradigm-exhaustion verdict is RM-protected territory.
**Major Risks:** Oracle-construction sensitivity; WSSS community investment in the paradigm guarantees resistance; VLM-grounding alternatives (killed 0268) are moving fast, dating the comparison.
**Unresolved Questions:** Does the extent-error share vary by class type? Do foundation-based weak-supervision pipelines escape the same ceiling or hit it elsewhere? What is the honest headroom left for CAM research?
**Required Experiments:** (1) 5-method × 3-oracle substitution grid; (2) multi-construction oracle robustness; (3) component attribution with ranges; (4) one foundation-grounding pipeline analyzed under the same oracles for contrast.
**Reviewer Opinion:** Keep. Decomposition-as-verdict is the right way to referee a plateaued subfield; the oracle methodology generalizes.

---

## IDEA-A-0266 — Object discovery or texture grouping?
**Cluster 13 · Protect: CI · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4**

- **One-sentence idea:** Test whether unsupervised segmentation via SSL-feature clustering discovers *objects* or merely *contiguous texture regions*, using scenes where objecthood and texture segmentation disagree.
- **Problem:** Unsupervised segmentation methods report improving object metrics, but their clustering substrate may be texture coherence that only correlates with objects in curated benchmarks — on texture-object dissociated scenes the methods' true nature would show.
- **Core Hypothesis (falsifiable):** On dissociation scenes (multi-texture single objects, uniform-texture multi-object groups), SSL-clustering methods track texture boundaries in >70% of conflicts — "unsupervised object discovery" is largely texture grouping, falsified if methods follow objecthood cues (closure, continuity) over texture.
- **Why Important:** Clarifies what unsupervised segmentation actually achieves, tempering claims and directing work toward genuine objecthood signals (motion, 3D).
- **Why Possibly Novel:** The dissociation-scene methodology (borrowed from perception science) has not been applied to audit unsupervised segmentation claims.
- **Minimal Experiment:** Curate/construct dissociation scenes; evaluate 5 unsupervised methods on texture-vs-object allegiance; compare against human grouping.
- **Main Risk:** Constructed scenes may be off-distribution for the methods; include natural dissociation cases (striped animals, uniform crowds).

**Survival Reason:** Perception-science dissociation methodology applied to a celebrated claim; the cheap correlational prelude to 0203's causal intervention. Protected CI.
**Major Risks:** Constructed-scene distribution shift; allegiance scoring needs careful GT rules on conflict scenes.
**Unresolved Questions:** Do motion-pretrained models shift toward objecthood cues (link 0275's killed content and 0221)? Does allegiance predict downstream unsupervised-segmentation utility? Shared mechanism with 0211's texture-following masks?
**Required Experiments:** (1) Dissociation-scene battery mixing natural (striped animals, uniform crowds) and constructed cases; (2) 5-method allegiance evaluation with human-grouping baseline; (3) pre-registered conflict GT rules; (4) joint reporting with 0203.
**Reviewer Opinion:** Keep. Run before 0203; if clustering is already texture-allegiant here, the expensive causal study gains a sharp prior.

---

## IDEA-A-0267 — Students inherit SAM's error signature
**Cluster 13 · Protect: — (merit) · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Quantify what student models inherit from SAM when trained on SAM pseudo-labels: do students replicate SAM's boundary style, granularity bias, and amorphous-object failures, and at what fidelity?
- **Problem:** SAM-as-pseudo-labeler is now standard for scaling datasets, but distillation propagates teacher biases (cf. IDEA-A-0007, 0015) into students that will be evaluated as if independent — the inheritance profile is unmeasured.
- **Core Hypothesis (falsifiable):** Students trained on SAM pseudo-labels reproduce SAM's specific error signature (granularity choices, hole-filling, amorphous shrinkage) at >70% signature-match on cases where independent human GT disagrees with SAM — student "performance" partly measures SAM-agreement, falsified if students average away teacher idiosyncrasies.
- **Why Important:** The entire SAM-labeled data ecosystem inherits these biases invisibly; measuring inheritance fidelity is prerequisite for trusting SAM-scaled datasets.
- **Why Possibly Novel:** Distillation bias is known abstractly; the concrete signature-inheritance measurement for the field's dominant pseudo-labeler is new.
- **Minimal Experiment:** Train students on SAM labels for 3 domains; evaluate on human-GT subsets where SAM errs; measure signature-match rates vs error-averaging.
- **Main Risk:** Signature matching needs careful definition; use the failure taxonomy from Cluster 1 as the instrument.

**Survival Reason:** Completes the contamination trilogy (0007 mechanism → 0029 annotation loop → 0267 inheritance fidelity); survives on merit as the measurement that makes the other two actionable.
**Major Risks:** Signature-match definition; students may partially average errors, giving a fuzzy fidelity number.
**Unresolved Questions:** Does inheritance fidelity depend on student capacity and training length? Does mixing scratch-annotated data dilute the signature sublinearly or linearly (mitigation curve)? Does 0128's smoke-shrinkage signature appear in wild SAM-labeled datasets?
**Required Experiments:** (1) 3-domain student training on SAM labels; (2) signature-match measurement on SAM-error subsets using the Cluster-1 failure taxonomy; (3) capacity and data-mixing sweeps; (4) in-the-wild dataset audit arm.
**Reviewer Opinion:** Keep. The trilogy should be pitched and executed as one program; this is its quantitative capstone.

---

## IDEA-A-0280 — Uncertainty routes labels to the wrong pixels
**Cluster 13 · Protect: CI+CF · Nov 4 / Sig 5 / SciQ 5 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether model uncertainty actually targets the pixels humans most need to label — auditing the core assumption of uncertainty-routed annotation (the model asks for labels where it is uncertain) for dense tasks.
- **Problem:** Uncertainty-guided labeling assumes uncertain pixels are the valuable ones, but uncertainty concentrates on trivial boundary bands (cf. IDEA-A-0103) while systematic errors are often *confident*; the assumption's validity for dense annotation routing is unverified.
- **Core Hypothesis (falsifiable):** Labeling budget spent on high-uncertainty regions yields less downstream improvement per pixel than budget spent on confident-but-wrong regions identified by cross-model disagreement — uncertainty routes labels to already-known ambiguity, missing the valuable systematic errors, falsified if uncertainty-routed labeling wins.
- **Why Important:** Uncertainty routing is being productized in annotation platforms; if it targets the wrong pixels, substantial industry annotation spend is misallocated.
- **Why Possibly Novel:** Active learning compares acquisition functions on aggregate; the uncertainty-vs-confident-error routing dissociation for dense labels is unexamined.
- **Minimal Experiment:** On datasets with full GT, simulate annotation routing by {uncertainty, disagreement, random} at matched pixel budgets; compare retraining gains.
- **Main Risk:** Simulated routing ignores human annotation ergonomics (region coherence); include region-level (not pixel-level) budget accounting.

**Survival Reason:** Attacks a productized assumption with a cheap, fully simulatable design; the confident-error-vs-uncertainty dissociation is the fresh instrument. Protected CI+CF; the applied twin of 0103.
**Major Risks:** Simulation-vs-ergonomics gap; active-learning literature adjacency requires careful positioning.
**Unresolved Questions:** Does the verdict hold at region-level (ergonomic) budgets? Which disagreement signals best locate confident errors? Do annotation platforms' actual routing policies match the audited assumption?
**Required Experiments:** (1) {uncertainty, cross-model disagreement, random} routing simulation at matched budgets on full-GT datasets; (2) region-level budget accounting; (3) retraining-gain comparison across ≥3 datasets; (4) joint analysis with 0103's boundary-band finding.
**Reviewer Opinion:** Keep. Industry-relevant, near-free, and the natural applied payoff of 0103's validity audit.

---

## IDEA-A-0283 — Which realism factor buys sim-to-real transfer
**Cluster 14 · Protect: — (merit) · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 3 / ROI 4**

- **One-sentence idea:** Run factor-controlled sim-to-real for segmentation — independently making geometry, texture, lighting, and sensor-model real versus synthetic — to identify which realism factor actually buys transfer for dense tasks.
- **Problem:** "Realism" in synthetic data is treated as one axis, but rendering budgets must be allocated across factors; dense prediction may need geometric realism far more than photometric realism (or vice versa) — the factor attribution has not been done for segmentation.
- **Core Hypothesis (falsifiable):** Sensor-model realism (noise, optics, compression) and geometric layout realism dominate transfer for segmentation (together >70% of the sim-to-real gap closure), while texture photorealism — where most rendering effort goes — contributes <15% — falsified if photorealism dominates.
- **Why Important:** Reallocates synthetic-data engineering budgets field-wide, and explains why some cheap-looking synthetic datasets transfer well while expensive photoreal ones don't.
- **Why Possibly Novel:** Factor studies exist for object detection in driving; the dense-segmentation factor decomposition including sensor modeling is missing.
- **Minimal Experiment:** Render a 2⁴ factorial (each factor real-matched vs naive) on one controllable scene domain; train and evaluate on real data; fit factor effects.
- **Main Risk:** Factors interact with the target domain; replicate the factorial in a second domain before generalizing.

**Survival Reason:** Honest 2⁴ factorial causal design answering the budget question every synthetic-data team faces; absorbs killed 0281/0290's fidelity questions into one framework.
**Major Risks:** Rendering-pipeline engineering; domain-specificity of factor effects; detection-side precedents.
**Unresolved Questions:** Does the sensor-model factor's predicted dominance hold across camera classes? How do factor effects shift for amorphous phenomena (0287's domain)? Can the factorial be extended with 0290's physics-fidelity sub-factors for smoke?
**Required Experiments:** (1) 2⁴ factorial rendering in one controllable domain; (2) matched training + real evaluation; (3) factor-effect fitting with interactions; (4) second-domain replication; (5) smoke-domain extension arm coordinated with 0287/0122.
**Reviewer Opinion:** Keep. The factorial discipline is what separates this from the pile of "synthetic realism" papers; results directly price rendering effort.

---

## IDEA-A-0285 — The synthetic rare-class fix inverts above ~70%
**Cluster 14 · Protect: CI · Nov 5 / Sig 5 / SciQ 5 / Feas 4 / Unp 4 / ROI 5**

- **One-sentence idea:** Test whether generating synthetic examples of *rare classes* fixes long-tail segmentation or teaches shortcut detection of generation artifacts on exactly those classes.
- **Problem:** The obvious long-tail fix — synthesize the rare classes — has a specific failure mode: if rare-class training data is predominantly synthetic, models may learn "rare class = synthetic-looking," failing on real rare instances precisely where the fix was aimed; this coupling is untested.
- **Core Hypothesis (falsifiable):** When synthetic fraction within a class exceeds ~70%, real-instance recall for that class *decreases* relative to no-augmentation baselines (artifact-shortcut regime), while below it augmentation helps — a within-class mixing threshold that current practice routinely violates for the rarest classes.
- **Why Important:** Defines a safety rule for the most common synthetic-data use case, preventing the fix from silently inverting on the classes that need it most.
- **Why Possibly Novel:** Long-tail augmentation papers report per-class gains without the within-class-fraction analysis or real-vs-synthetic recall decomposition.
- **Minimal Experiment:** Sweep within-class synthetic fractions for rare classes on long-tail benchmarks; measure real-instance recall separately; locate the inversion threshold.
- **Main Risk:** Threshold likely depends on generator quality (ties to IDEA-A-0282); report thresholds per generator tier.

**Survival Reason:** The fix inverts exactly where it is aimed — a sharp, safety-rule-producing slice of the synthetic-fraction question that absorbs 0282's curve and 0119/0171's artifact-shortcut instances. Protected CI.
**Major Risks:** Generator-quality dependence of the threshold; real-instance rare-class evaluation is statistically noisy.
**Unresolved Questions:** Is the threshold predictable from forensic-detectability of the generator (a transferable rule)? Does artifact-shortcut formation show early-training signatures (monitoring hook)? Does harmonization/post-processing move the threshold?
**Required Experiments:** (1) Within-class synthetic-fraction sweeps on long-tail benchmarks; (2) real-vs-synthetic recall decomposition; (3) two generator tiers; (4) forensic-probe correlation for threshold prediction; (5) power-aware rare-class evaluation design.
**Reviewer Opinion:** Keep. The most deployment-consequential synthetic-data idea in the batch; the within-class-fraction lens is the insight the per-class-gain literature missed.

---

## IDEA-A-0287 — Procedural beats diffusion on web-sparse phenomena
**Cluster 14 · Protect: — (merit) · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Compare procedural (physics/graphics) generation against diffusion-model generation for training data on *out-of-web-distribution* phenomena (smoke, transparency, medical), testing whether generative models can synthesize what they never saw well enough to teach it.
- **Problem:** Diffusion generators are trained on web data, so their coverage of exactly the phenomena that need synthetic data (rare, hard-to-photograph) is suspect; procedural generation has no such circularity — but the comparison for segmentation training value has not been run.
- **Core Hypothesis (falsifiable):** For web-underrepresented phenomena, procedural data beats diffusion-generated data as training material (>5 IoU downstream) despite lower photorealism, with diffusion data exhibiting mode-collapse toward web-typical instances (measurable as lower coverage of the phenomenon's physical parameter space) — falsified if diffusion data wins on these domains.
- **Why Important:** Chooses the right synthesis technology per domain and exposes the circularity limit of generative augmentation — you can't generate your way out of what the generator never learned.
- **Why Possibly Novel:** The two synthesis paradigms are compared on photorealism, not on training value for web-sparse phenomena.
- **Minimal Experiment:** Produce matched-size procedural and diffusion datasets for smoke + transparent objects; train identical models; evaluate on real benchmarks; measure parameter-space coverage of both sources.
- **Main Risk:** Procedural quality depends on engineering effort; fix effort budgets and document them.

**Survival Reason:** Exposes the circularity limit of generative augmentation with a measurable mechanism (parameter-space coverage); supplies the data strategy for the smoke and transparency programs (0122, 0141).
**Major Risks:** Effort-budget fairness between paradigms; diffusion models improve fast, requiring the coverage mechanism (not just the endpoint) to carry lasting value.
**Unresolved Questions:** Does fine-tuning diffusion models on small real sets of the phenomenon close the coverage gap? Is coverage the right mechanism metric, or does artifact structure (0285) dominate? Which phenomena sit on which side of the boundary?
**Required Experiments:** (1) Matched-size procedural vs diffusion sets for smoke + transparency at fixed effort budgets; (2) identical-model training with real-benchmark evaluation; (3) physical-parameter-space coverage measurement; (4) diffusion-fine-tuned third arm.
**Reviewer Opinion:** Keep. The mechanism (coverage circularity) is the durable contribution; even as generators improve, the boundary question stays relevant.

---
## IDEA-A-0296 — UDA rankings scramble on fresh pairs
**Cluster 15 · Protect: RM · Nov 4 / Sig 5 / SciQ 5 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether a decade of unsupervised domain adaptation (UDA) methods generalizes beyond the benchmark pairs they were developed on (GTA→Cityscapes), by evaluating them on fresh adaptation pairs they have never been tuned against.
- **Problem:** UDA method development has iterated on the same few pairs for years; the methods' hyperparameters and design choices may be benchmark-pair-specific, making the literature's reported ordering meaningless for new deployments — the overfitting-to-the-pair magnitude is unmeasured.
- **Core Hypothesis (falsifiable):** On 4 novel adaptation pairs, the published UDA method ranking scrambles (rank correlation < 0.4 with GTA→Cityscapes ordering) and the average gain over source-only baselines shrinks by >50% — the field has been fitting the benchmark, falsified if rankings and gains transfer.
- **Why Important:** Determines whether UDA research produced transferable principles or benchmark-specific artifacts — a verdict the field needs before further iteration.
- **Why Possibly Novel:** UDA criticism exists in commentary; the fresh-pair generalization audit with ranking-transfer statistics has not been executed.
- **Minimal Experiment:** Re-run 8 published UDA methods (released code, frozen hyperparameters) on 4 new pairs (aerial, medical, underwater, thermal); compare orderings and gain retention.
- **Main Risk:** Frozen hyperparameters may unfairly penalize methods; add a bounded re-tuning arm to separate brittleness from overfitting.

**Survival Reason:** The ranking-transfer verdict on ten years of UDA — the strongest single audit in the domain-adaptation cluster, and a guaranteed reviewer-disagreement magnet (UDA authors will contest the frozen-hyperparameter protocol; that fight is the point). Protected RM.
**Major Risks:** Frozen-hyperparameter protocol will be attacked as unfair; released code for older methods may not run on new pairs without nontrivial adaptation; fresh-pair annotation quality varies.
**Unresolved Questions:** How much bounded re-tuning restores the ordering (brittleness vs overfitting split)? Do method *families* (self-training vs adversarial vs alignment) transfer even if individual methods don't? Does the scramble correlate with how long a method was tuned on GTA→Cityscapes (publication-date effect)?
**Required Experiments:** (1) 8 published UDA methods, frozen hyperparameters, on 4 novel pairs spanning aerial/medical/underwater/thermal; (2) rank-correlation and gain-retention statistics vs GTA→Cityscapes; (3) bounded re-tuning arm (fixed budget per method); (4) family-level aggregation analysis; (5) source-only and foundation-frozen baselines on every pair.
**Reviewer Opinion:** Keep with priority. This is the cluster's anchor; 0297 (style/content decomposition) and 0304 (Fourier spectroscopy) were killed as near-misses because their diagnostic payloads fold into this audit plus 0303.

---

## IDEA-A-0303 — Norm-recovery fraction as the shift-tier diagnostic
**Cluster 15 · Protect: CF · Nov 4 / Sig 4 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Test the dichotomy that normalization-statistics adaptation suffices for *sensor* shift but not *semantic* shift, establishing a cheap diagnostic that tells practitioners which adaptation tier a given shift requires.
- **Problem:** Adaptation machinery spans a cost ladder (norm-stats → norm-params → PEFT → full UDA), but there is no validated diagnostic mapping a given shift to the minimal sufficient tier — practitioners either over-spend or under-adapt (generalizing IDEA-A-0065 beyond medical).
- **Core Hypothesis (falsifiable):** Recomputing normalization statistics on target data recovers >70% of the drop for sensor/photometric shifts and <15% for semantic/layout shifts across 10 diverse pairs, making norm-recovery-fraction (measurable with unlabeled data in minutes) a reliable shift-tier diagnostic — falsified if recovery fractions don't separate shift types.
- **Why Important:** A minutes-cheap diagnostic that selects the right adaptation tier would be adopted immediately across applied vision.
- **Why Possibly Novel:** Norm-based adaptation is known; its formalization as a *diagnostic instrument* with a validated tier-mapping is new.
- **Minimal Experiment:** 10 shift pairs spanning types × the adaptation-tier ladder; measure recovery fractions per tier; validate the diagnostic's tier predictions.
- **Main Risk:** Modern norm-free/LN architectures complicate the recipe; define the LN analog (recompute affine calibration) and test both.

**Survival Reason:** Minutes-cheap, label-free, immediately adoptable, and falsifiable in a week of compute — the definition of cheap-to-falsify. Generalizes the killed 0065 (medical norm-tuning) and 0057 (BitFit diagnostic) into one instrument. Protected CF.
**Major Risks:** LayerNorm/norm-free architectures may not admit a clean analog, shrinking applicability to modern backbones; the sensor/semantic dichotomy may blur on mixed shifts (which are the common real case).
**Unresolved Questions:** What is the LN-era analog and does it preserve the diagnostic's separation? How does the diagnostic behave on *mixed* shifts — is recovery fraction additive across components? Can the tier prediction be validated prospectively (predict, then run the ladder, then check)?
**Required Experiments:** (1) 10 shift pairs deliberately spanning sensor/photometric/semantic/mixed; (2) full adaptation-tier ladder per pair; (3) recovery-fraction measurement with unlabeled target data only; (4) BN and LN-analog arms; (5) prospective validation on 3 held-out pairs.
**Reviewer Opinion:** Keep. The highest adoption-probability idea in the cluster; pairs naturally with 0296 (the audit says the field overfit; this says what to do instead, cheaply).

---

## IDEA-A-0305 — Night vision: adaptation gap or information deficit
**Cluster 15 · Protect: CI · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Determine whether night-time segmentation is a domain-adaptation problem or an information-deficit problem, by measuring the human ceiling on the same night imagery models fail on.
- **Problem:** Night segmentation is framed as domain shift (fixable by adaptation), but low-light imagery may simply lack the information — in which case adaptation research chases an impossible target and sensor-side solutions (exposure, NIR) are the answer; the framing has never been tested against a human ceiling.
- **Core Hypothesis (falsifiable):** On standard night benchmarks, human segmentation (with unlimited time, contrast tools allowed) exceeds the best adapted models by >15 mIoU on structure-rich classes but matches models on severely underexposed regions — the gap decomposes into a recoverable adaptation component and a hard information floor, mapped per region, falsified if humans match models everywhere (pure information deficit) or exceed everywhere (pure adaptation gap).
- **Why Important:** Splits the night-vision problem into its fixable and unfixable parts, directing adaptation research and sensor investment respectively.
- **Why Possibly Novel:** Night benchmarks exist; the human-ceiling decomposition of the night gap has not been measured.
- **Minimal Experiment:** Human annotation study on night benchmark subsets with per-region luminance logging; compare human/model performance stratified by local information content.
- **Main Risk:** Human tools (contrast stretching) must be standardized; report the tool protocol as part of the ceiling's definition.

**Survival Reason:** Counter-intuitive framing flip: the field assumes night is an adaptation problem; this measures whether the target is even achievable. Either outcome redirects effort (adaptation research vs sensor investment). Protected CI.
**Major Risks:** Human-study cost and protocol sensitivity (the ceiling is only as good as the tool/instruction standardization); night benchmark GT itself was annotated by humans, creating circularity that must be handled (fresh annotation from raw captures).
**Unresolved Questions:** Does the decomposition depend on camera ISP settings (raw vs processed input)? Where do NIR/thermal sensors sit relative to the measured information floor? Does the recoverable component predict which adaptation methods help where?
**Required Experiments:** (1) Human annotation study on stratified night-benchmark subsets with standardized contrast tools; (2) per-region luminance/information logging; (3) model-vs-human comparison stratified by local information content; (4) raw-sensor arm to separate ISP losses; (5) protocol publication with skill-level replication.
**Reviewer Opinion:** Keep. The human-ceiling instrument (shared with 0336) applied where it changes an entire subfield's premise; feasibility is the main watch item — scope the study to 2 benchmarks.

---

## IDEA-A-0313 — Resolution beats small-object architecture remedies
**Cluster 16 · Protect: RM · Nov 4 / Sig 5 / SciQ 4 / Feas 4 / Unp 3 / ROI 5**

- **One-sentence idea:** Test whether raw input resolution beats all architectural small-object remedies at matched compute — the compute-matched showdown the small-object detection literature has skipped.
- **Problem:** Dozens of architectural fixes target small-object detection, each compared at fixed resolution; if simply spending the same extra compute on resolution dominates them, the literature's recommendations are misordered for practitioners.
- **Core Hypothesis (falsifiable):** At matched inference FLOPs, resolution scaling exceeds ≥80% of published architectural small-object remedies on their own benchmarks, with architecture wins confined to memory-bound regimes where resolution cannot be raised — resolution is the dominant currency, falsified if architectures win at matched compute.
- **Why Important:** Gives practitioners the correct first move for small-object problems and re-baselines the subfield's comparisons.
- **Why Possibly Novel:** Resolution ablations exist locally; the systematic compute-matched confrontation against the remedy literature has not been assembled.
- **Minimal Experiment:** Reproduce 6 small-object methods; compare each against its baseline-at-higher-resolution at matched FLOPs across 3 benchmarks.
- **Main Risk:** FLOPs vs latency vs memory give different "matched compute" verdicts; report all three accountings (ties to IDEA-A-0339).

**Survival Reason:** A compute-matched confrontation that could re-baseline an entire subfield with six reproductions — enormous verdict-per-GPU-hour, and a guaranteed disagreement magnet among small-object-method authors. Protected RM.
**Major Risks:** "Matched compute" is contestable (FLOPs vs latency vs memory give different verdicts — all three must be reported); reproduction fidelity of the 6 methods will be scrutinized.
**Unresolved Questions:** Where exactly is the memory-bound boundary beyond which architecture wins? Do the same conclusions hold for segmentation of small structures (medical lesions, aerial)? Is there an interaction — do the best remedies help *more* at high resolution?
**Required Experiments:** (1) Reproduce 6 published small-object remedies on their own benchmarks; (2) baseline-at-higher-resolution arms matched on FLOPs, latency, and memory separately; (3) 3 benchmarks spanning aerial/driving/generic; (4) remedy×resolution interaction grid; (5) memory-bound regime mapping.
**Reviewer Opinion:** Keep. Absorbed 0164 (oracle-magnification decomposition), which was the weaker sibling; pairs with 0161's GSD-ladder science. The three-accounting honesty requirement is what elevates this above a blog-post-grade ablation.

---

## IDEA-A-0319 — Boxes are the wrong primitive for amorphous targets
**Cluster 16 · Protect: — (merit) · Nov 4 / Sig 4 / SciQ 5 / Feas 4 / Unp 4 / ROI 4**

- **One-sentence idea:** Test whether bounding boxes are the wrong output primitive for amorphous phenomena (smoke, fire, spills, dust) by comparing box-based against blob/level-set-based detection formulations on downstream decision quality.
- **Problem:** Detection pipelines force amorphous phenomena into boxes whose corners are meaningless (a smoke box is mostly non-smoke); the primitive mismatch plausibly harms both learning and downstream use, but no controlled formulation comparison exists.
- **Core Hypothesis (falsifiable):** For amorphous targets, blob-primitive detectors (center + soft extent) beat box detectors on downstream decision metrics (alarm localization error, extent-tracking stability) by >20% relative at matched compute, while boxes remain superior for rigid objects — the optimal primitive is phenomenology-dependent, falsified if boxes suffice everywhere.
- **Why Important:** Output-primitive choice is beneath the field's attention yet shapes everything downstream; a validated phenomenology-to-primitive mapping upgrades safety systems (fire, hazmat) immediately.
- **Why Possibly Novel:** Alternative primitives exist scatteredly; the controlled formulation comparison judged on downstream decisions is new.
- **Minimal Experiment:** Implement matched box and blob detectors for smoke/fire datasets; evaluate on downstream-decision suites (localization-for-response, temporal stability); replicate on rigid-object controls.
- **Main Risk:** Blob GT must be derived from masks consistently; reuse the density-GT machinery from IDEA-A-0121/0122.

**Survival Reason:** Output-primitive science — a representational question the field treats as settled by convention, judged on downstream decisions rather than proxy AP. Completes the amorphous-phenomena program (0121, 0122, 0141, 0287). Unprotected merit survivor.
**Major Risks:** Blob ground truth derivation is a design choice that shapes the verdict; downstream-decision metrics need external grounding (fire-response experts) to avoid being self-serving.
**Unresolved Questions:** What is the right blob parameterization (center+extent, level sets, density fields)? Do gains persist when the downstream consumer is a learned policy rather than a rule? Where do elongated-but-rigid objects (wires, cracks) fall on the primitive map?
**Required Experiments:** (1) Matched box and blob detectors on smoke/fire datasets at matched compute; (2) downstream-decision suite (alarm localization error, extent-tracking stability); (3) rigid-object control replication; (4) blob-parameterization ablation; (5) GT-derivation sensitivity analysis reusing 0121/0122 density machinery.
**Reviewer Opinion:** Keep. The batch's amorphous-phenomena thread (density GT → detection primitive → data strategy) is one of its most coherent research programs; this is its capstone.

---

## IDEA-A-0336 — Human floors and ceilings for segmentation benchmarks
**Cluster 17 · Protect: CI · Nov 4 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 5**

- **One-sentence idea:** Measure human segmentation performance (time-budgeted and unlimited) on standard benchmarks to establish the human floors and ceilings that segmentation evaluation has always lacked.
- **Problem:** Unlike classification (where human baselines anchored progress narratives), segmentation benchmarks have no published human performance — so "superhuman" claims, headroom estimates, and difficulty comparisons across benchmarks all float without an anchor.
- **Core Hypothesis (falsifiable):** Human mIoU on standard benchmarks is substantially below 100 (HYPOTHESIS: 75–90 depending on benchmark, driven by class-definition ambiguity rather than perceptual failure), and current top models already exceed time-budgeted human performance on ≥2 benchmarks while trailing unlimited-time humans everywhere — the human anchor reorders our sense of which benchmarks are "hard."
- **Why Important:** Human anchors recalibrate headroom claims, identify benchmarks where residual "error" is definitional, and give "superhuman" a measurable meaning for dense prediction.
- **Why Possibly Novel:** Astonishingly, systematic human baselines for major segmentation benchmarks have never been published.
- **Minimal Experiment:** Trained annotators segment stratified samples of 4 benchmarks under {90 s/image, unlimited} budgets against official GT; report human floors/ceilings with disagreement decomposition.
- **Main Risk:** "Human performance" depends on training and instructions; standardize and publish the protocol, report across skill levels.

**Survival Reason:** The missing anchor of dense-prediction evaluation — the fact that no systematic human baseline exists for major segmentation benchmarks is itself the surprising finding. Counter-intuitively simple: no model training at all. Protected CI.
**Major Risks:** The "human performance" construct is protocol-dependent (skill, tools, time) — the number is only as citable as the protocol is defensible; circularity with human-made GT (disagreement with GT conflates human error and GT error).
**Unresolved Questions:** How to decompose human-GT disagreement into perceptual error vs definitional ambiguity (link to 0337's instruction experiment)? Do human ceilings differ across benchmark eras (older GT = noisier anchor)? What time budget best represents "practical human performance"?
**Required Experiments:** (1) Trained annotators on stratified samples of 4 benchmarks under {90s, unlimited} budgets; (2) disagreement decomposition against official GT with adjudication; (3) skill-level replication (novice/trained/expert); (4) per-class human-difficulty profiles vs model-difficulty profiles; (5) published protocol as a community instrument.
**Reviewer Opinion:** Keep with priority. Cheap in GPU terms, expensive in study design; the anchor gets cited by every headroom discussion for years. Killed 0179 (aerial human floor) and 0260 (1-shot ambiguity floor) as family redundancy — this is the general instrument.

---

## IDEA-A-0337 — Annotation instructions as an experimental treatment
**Cluster 17 · Protect: RM · Nov 5 / Sig 5 / SciQ 5 / Feas 3 / Unp 4 / ROI 4**

- **One-sentence idea:** Treat annotation instructions as an experimental variable: annotate the same images under different (all-reasonable) instruction documents and measure how much benchmark ground truth — and resulting model rankings — depend on instruction wording.
- **Problem:** Instructions define what ground truth *is* (occlusion handling, boundary conventions, class edge cases), yet they are unpublished, unversioned, and never varied experimentally; the GT variance induced by instruction choice is a hidden hyperparameter of every benchmark.
- **Core Hypothesis (falsifiable):** Two reasonable instruction variants produce GT differing by >5 IoU-equivalent on ambiguity-prone classes, sufficient to invert model rankings whose gaps are below that scale — benchmark conclusions are instruction-contingent at the scale of typical SOTA gaps.
- **Why Important:** Establishes instruction publication and sensitivity reporting as necessary benchmark practice, and bounds the interpretive weight small gaps can carry.
- **Why Possibly Novel:** Annotation quality is studied as error; instruction wording as a *treatment* in a controlled GT experiment is new methodology.
- **Minimal Experiment:** Draft 3 defensible instruction variants; annotate 500 images under each (separate annotator pools); quantify GT divergence and re-rank 8 models per variant.
- **Main Risk:** Annotator pools differ beyond instructions; use crossover assignment to isolate the instruction effect.

**Survival Reason:** The most methodologically novel idea in the evaluation cluster (Nov 5): instructions-as-treatment is genuinely new experimental methodology, and "GT is instruction-contingent at SOTA-gap scale" would be a finding every benchmark paper must cite. Guaranteed disagreement magnet (benchmark maintainers will resist). Protected RM.
**Major Risks:** Annotator-pool confound requires careful crossover design; annotation cost for 3×500 images is substantial; "all-reasonable" instruction variants must be defended as genuinely reasonable, not straw men.
**Unresolved Questions:** Which classes/conventions carry the instruction sensitivity (occlusion? boundaries? class edges)? Does instruction-induced GT variance behave like noise (uniform model impact) or like bias (reorders models)? Can instruction sensitivity be predicted from image content, enabling targeted re-annotation?
**Required Experiments:** (1) 3 defensible instruction variants drafted with practitioner input; (2) 500 images × 3 variants with crossover annotator assignment; (3) GT-divergence quantification per class and convention; (4) re-ranking of 8 models per variant with inversion analysis; (5) link to 0340's annotation-perturbation resampling.
**Reviewer Opinion:** Keep. Together with 0091, 0103, 0336, and 0340, this forms the batch's strongest thread: the measurement instruments of the field are themselves unmeasured. Absorbed 0147 (distributional ambiguity eval).

---

## IDEA-A-0340 — Bootstrap the leaderboards: the fiction fraction
**Cluster 17 · Protect: CF · Nov 4 / Sig 5 / SciQ 4 / Feas 5 / Unp 3 / ROI 5**

- **One-sentence idea:** Apply bootstrap resampling over test sets to published segmentation rankings and measure what fraction of leaderboard orderings are statistically indistinguishable under test-set sampling variation alone.
- **Problem:** Leaderboards present point-estimate orderings with no test-set-sampling uncertainty; two models differing by 0.4 mIoU on a 2k-image test set may be statistically tied, but the field has never computed ranking confidence at scale — the leaderboard's implied precision is unexamined.
- **Core Hypothesis (falsifiable):** Under image-level bootstrap, >50% of adjacent-pair orderings on major segmentation leaderboards are within sampling noise (overlapping 95% intervals), and the fraction grows near the top where gaps compress — most fine-grained leaderboard structure is statistically fictional, falsified if orderings are robust under resampling.
- **Why Important:** A leaderboard confidence layer (cheap to compute, easy to display) would immediately upgrade the field's primary comparison instrument; the measured fiction-fraction makes the case.
- **Why Possibly Novel:** Bootstrap CIs are standard statistics; their systematic application to segmentation leaderboard structure — with the fiction-fraction as the headline measurement — has not been done.
- **Minimal Experiment:** Obtain per-image results (released predictions or re-runs) for 20 models on 3 benchmarks; bootstrap ranking distributions; report pairwise distinguishability matrices.
- **Main Risk:** Bootstrap over images ignores annotation-noise correlation; complement with annotation-perturbation resampling (link to IDEA-A-0337).

**Survival Reason:** The cheapest idea in the batch that produces a headline number: near-zero model runs (released predictions suffice), a week of analysis, and a "fiction fraction" that reframes how leaderboards are read. The purest cheap-to-falsify entry. Protected CF.
**Major Risks:** Per-image predictions may not be released for all models (re-runs needed for some); image-level bootstrap understates uncertainty by ignoring annotation-noise correlation — the 0337 complement is needed for the full story.
**Unresolved Questions:** Does the fiction fraction differ across metrics (mIoU vs boundary-F vs worst-class)? How does it scale with test-set size (prescription for benchmark builders)? Should adjacent-rank claims require a minimum-detectable-difference disclosure?
**Required Experiments:** (1) Per-image results for 20 models on 3 benchmarks (released predictions where available); (2) image-level bootstrap ranking distributions with pairwise distinguishability matrices; (3) fiction-fraction vs leaderboard position analysis; (4) test-set-size scaling curves; (5) annotation-perturbation complement linked to 0337.
**Reviewer Opinion:** Keep. Absorbed 0331 (paired-test SOTA-claim audit) and 0335 (worst-class re-scoring), both of which deliver overlapping verdicts at higher cost. If forced to pick one evaluation-statistics idea, this is it.

---

## Closing note

73 survivors of 340 (21.5%). Protection accounting: 10 high-risk/high-reward, 25 counter-intuitive, 24 disagreement magnets, 21 cheap-to-falsify (flags overlap; primary flag shown per idea), 6 unprotected merit survivors. No module-stacking, no "apply-X-to-medical-without-a-question", and no loss/backbone-swap ideas were retained. Full elimination rationale in `stage2_batch_A_killed.md`; complete score table in `stage2_batch_A_scores.md`.

*End of Stage 2 Batch A survivors (73 ideas).*
