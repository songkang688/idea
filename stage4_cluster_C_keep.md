# Stage 4 — Cluster C KEEP List (Reviewer #2 survivors)

**7 survivors of 18.** Each entry: the strongest attack Reviewer #2 could mount, and the realistic experiment that shuts the reviewer up (with mandatory conditions — a survivor that drops its condition reverts to KILL). Full attack transcripts in `stage4_cluster_C_attacks.md`.

Common property of all seven: an interventional lever the experimenter controls, and a decision that changes depending on the outcome. No pure audits survived.

---

## 1. C-0028 — In-batch concept co-occurrence, not loss design, creates dense alignment

- **Strongest attack:** "Retrieval stays equal" is unenforceable — noun-overlap curation *is* hard-negative mining (NegCLIP/JEST territory), so any segmentation gain is attributable to generic hardness, and a null at CLIP-small scale is excused by "below emergence scale."
- **Shutting-up experiment:** Three arms at CLIP-B/32 on ~20M pairs: random batches; noun-overlap-curated batches; **hardness-matched control** (batches matched to the curated arm's in-batch similarity/hardness distribution via caption-embedding similarity, without shared-noun co-occurrence). Curation-strength dose-response sweep, ≥3 seeds, retrieval + dense metrics reported jointly. Segmentation moving under co-occurrence but not under matched hardness isolates the mechanism; the dose-response curve makes the null informative.
- **Mandatory condition:** The hardness-matched arm. Without it, the paper is a JEST metric-swap and dies.
- **Payoff either way:** Mechanism confirmed → batch curation becomes a free dial for dense ability. Refuted → dense-alignment emergence needs a different explanation than the co-occurrence folklore.

## 2. C-0090 — Text-batch rehearsal works by gradient rebalancing, not by content

- **Strongest attack:** "Matched gradient scale" is underdefined (any matching convention can be disputed), pseudo-rehearsal with random inputs is 30 years old (Robins 1995), and the likely outcome is the mushy middle (fluency preserved, knowledge lost) that kills the clean headline.
- **Shutting-up experiment:** Five arms at fixed token budget on a LLaVA-1.5-class fine-tune: {none, curated mix, random web text, shuffled tokens, one repeated document}. **Pre-registered capability-stratified evaluation** (fluency / knowledge / reasoning / instruction-following) and results reported under two pre-registered gradient-matching conventions (global-norm and per-layer) to prove convention-invariance.
- **Mandatory condition:** The stratified evaluation. The mushy middle is only actionable if quantified per capability ("you need X% real text, only for knowledge retention").
- **Payoff either way:** Random text works → rehearsal-curation budgets across the field are wasted. Content matters → the first stratified map of *which* capability needs real content, still a cost-cutting recipe.

## 3. C-0128 — Generative editing enables causal measurement of context reliance in segmentation

- **Strongest attack:** The instrument may measure the editor, not the scene — edit artifacts are worst-case for dense models that read every pixel, "removal" edits substitute the generator's context prior rather than removing context, and the score could be editor-dependent.
- **Shutting-up experiment:** Three validity legs, then the measurement. (i) **Null-edit calibration:** invert-reconstruct with no semantic change → per-model artifact noise floor; all effects reported as excess over it. (ii) **Cross-editor invariance:** ≥2 unrelated editing systems; per-class score agreement. (iii) **Real-photo anchor:** video frames where objects naturally enter/leave otherwise-static scenes give artifact-free present/absent pairs; the synthetic score must match the real-pair score on overlapping classes. Then scale the robustness linkage to 100+ classes / 3 datasets with frequency and scale partialled out.
- **Mandatory condition:** Leg (iii). Physics, not promises, answers the artifact objection.
- **Payoff either way:** Delivers the field's first per-class, model-comparable context-reliance score; high-reliance classes are direct targets for context-decorrelation training, and the score's link (or non-link) to shift robustness is informative in both directions.

## 4. C-0229 — Multi-task pretraining's benefit is the data, not the tasks

- **Strongest attack:** The pooled-image control is unconstructible at the scale the claim targets (per-task labels don't exist on pooled images; pseudo-labeling smuggles in a teacher), and compute-matching is an unwinnable war.
- **Shutting-up experiment:** Run the decomposition where the control is *exact*: fully multi-labeled corpora (COCO: boxes/masks/captions/keypoints; Hypersim: depth/normals/semantics on identical images). Arms: {multi-task on pooled images, single-task on pooled images, single-task on own subset}; **two compute-matching conventions reported side by side**; transfer on held-out tasks. Two-point scale sweep (COCO-scale + one 10× arm) to show the decomposition direction is scale-stable.
- **Mandatory condition:** Fully-labeled corpora only — no pseudo-label arm anywhere in the design.
- **Payoff either way:** The deliverable is the decomposition number (fraction of the multi-task advantage that survives image-diversity equalization), which doesn't exist at any scale and directly prices labels-vs-images investment.

## 5. C-0158 (M6) — Uncertainty sampling selects LLM-annotator failures; decorrelated acquisition fixes it

- **Strongest attack:** "Why do active learning at all?" — LLM labels are cheap, so annotate-everything-then-filter makes acquisition order irrelevant; and the fix's annotator-error predictor is circular without ground truth.
- **Shutting-up experiment:** (i) Settings where budget genuinely binds: dense annotation by VLM agents (per-item mask generation at real compute cost) and frontier-model annotation at scale. (ii) Direct mechanism measurement on ground-truthed pools: item-level correlation between learner uncertainty and annotator error — a number, not an argument. (iii) Acquisition arms at matched *total cost*: random, uncertainty, error-penalized (predictor = annotator self-consistency/ensemble disagreement, no ground truth), **plus the honest baseline: annotate-everything + noise-robust training**. 3 text + 1 vision datasets.
- **Mandatory condition:** The annotate-everything baseline. If it wins, that is the published finding (AL+LLM pipelines should be dismantled) — every branch is actionable.
- **Payoff either way:** Mechanism + fix confirmed → default AL+LLM pipelines are silently suboptimal and there's a drop-in repair. Premise refuted → equally deployable advice.

## 6. C-0302 — Last-layer group-robustness fixes fail on spatially entangled bias

- **Strongest attack:** Refuting an unclaimed extension ("nobody said DFR works for segmentation") with a cartoon confound (class A always on background B); the constructive arm is a hyperparameter sweep.
- **Shutting-up experiment:** The **dissociation design**: identical images, identical planted correlation, two readouts (classification head, dense head). DFR fixes the classifier — does it fix the segmenter? Outcome genuinely open: a per-pixel 1×1 readout re-weights channel evidence locally and *could* recover worst-group IoU if local evidence is intact. Add a correlation-strength dial (graded bias, not 100% cartoons), one natural-bias dataset (context-entangled classes in Cityscapes/ADE), and a **retraining-depth curve** (retrain top-k blocks on balanced data) yielding a transferable "debiasing depth" quantity.
- **Mandatory condition:** The same-images classification-vs-dense dissociation. The dissociation — not the failure — is the finding; without it the strawman attack lands.
- **Payoff either way:** Recovery → a celebrated cheap fix extends to dense tasks. Failure → bias localized in spatial feature mixing, with a practical answer (how deep to retrain) that classification-era debiasing can't provide.

## 7. C-0310 — The camera ISP is a bigger domain axis than the weather

- **Strongest attack:** The headline is apples-to-oranges by construction — both "realistic ISP ranges" and "moderate weather" are author-chosen, so either axis can be made to win; and RAW data with dense labels barely exists.
- **Shutting-up experiment:** **Real-distribution anchoring** on both axes: ISP spread = identical RAW frames rendered through N *actual* pipelines (dcraw/RawTherapee profiles, phone SDKs, automotive ISP configs); weather spread = real paired conditions (ACDC clear↔fog/rain/snow, matched scenes). Labels are annotated once per RAW frame and are *exactly invariant* across all renders — the intervention re-renders pixels, never moves them. Training arm: ISP-randomized augmentation with Rawgment (CVPR 2023) as the published baseline.
- **Mandatory condition:** Real-device anchoring. An author-chosen ISP grid reverts this to unfalsifiable marketing and the idea dies.
- **Payoff either way:** ISP ≥ weather → the field's robustness effort is aimed at the wrong (visible) axis and a cheap controllable augmentation exists. ISP ≪ weather → the cross-device panic is quantified away; both outcomes redirect real engineering budgets.

---

## Portfolio shape after Stage 4

| Axis | Survivors |
|---|---|
| Training-mechanism causal tests | C-0028 (batch composition), C-0090 (rehearsal content), C-0229 (task-vs-data) |
| Measurement instruments with interventions + validation | C-0128 (counterfactual context), C-0310 (ISP re-rendering) |
| Robustness/debiasing with constructive levers | C-0302 (dissociation + debiasing depth) |
| Annotation-pipeline mechanism + fix | C-0158 (decorrelated acquisition) |

Salvage note: the fixed-checkpoint protocol harness from killed C-0276 should be built as shared infrastructure for C-0310 and C-0302 evaluations (protocol-controlled scoring), not as a standalone paper.
