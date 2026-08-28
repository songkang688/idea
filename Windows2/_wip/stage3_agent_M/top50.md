# Windows2 Stage-3 Agent M — Top 50 (200 → 50 after Reviewer #2)

Agent M (Stage 2/3/4 merger; **not the PI, no final-3, no full research packages**). Date: 2026-08-28.

**Working 200:** Agent I's `stage2_agent_I/provisional_200.md` (190 slots: 84 A / 59 B / 47 C), used as mandated — it supersedes G's partial and already applies the H/K kills, the F/J reconciliation, and the PI directive. All arm topology below follows I's fold unless a binding cap forces a change.

**Binding inputs applied:** H/J/K `verdicts.jsonl` (no KILL hosts the 50; framing-dead ideas only in mutated form); `PI_TO_I.md`; **`PI_BINDING.md` post-L overrides** (B-0114 4-arm-only, A-0061 demoted from bare SURVIVE, five mandatory revives, correlated-pair declarations); Agent L's audit; and the Stage-3 caps (annotation-taxonomy ≤ 2, C GT-epistemology ≤ 2, B PEFT-mechanics ≤ 2, C eval-audit ≤ 40% of the 50).

## Headline accounting

| Batch | Slots in 50 | Bare SURVIVE | SURVIVE-IF-EXPERIMENT | MUTATE | Unattacked / PI-revived hosts |
|---|---|---|---|---|---|
| A | 17 | 0 | 7 | 8 | 2 (A-0028 revive, A-0290 host) |
| B | 13 | 0 | 9 | 3 | 1 (B-0284) |
| C | 20 | 0 | 15 | 4 | 1 (C-0300 host) |
| **Total** | **50** | **0** | **31** | **15** | **4** |

There are now **zero bare SURVIVEs**: A-0061 was demoted by PI_BINDING (arXiv 2601.06067 topology-aware checkpoint selection; arXiv 2412.14619 metric guidance) to SURVIVE-IF-EXPERIMENT with mandatory positioning.

Cap status: C eval-audit 14/50 = 28% (≤ 40% ✓); annotation-taxonomy 2/2; GT-epistemology 2/2; PEFT 2/2. All 8 protected ideas present (B-0114 in 4-arm form only, B-0001, B-0104, B-0194, C-0306, A-0206, A-0061, A-0175). All 5 PI_BINDING revives placed: A-0199-mut (slot 17), A-0028 (slot 14), C-0334 (named arm of C-0283+0285), C-0082-mut (named arm of A-0026), A-0090 (named arm inside C-0122's A-0100 arm).

Merged slots (one slot, multiple I-slots): A-0237+0249, C-0276+0256, C-0283+0285, C-0136+0287+0302. PI-declared correlated pairs that count as ONE bet unless experiments dissociate: B-0114 × B-0001; A-0061 × A-0206; the taxonomy cluster; the GT-epistemology pair.

---

## Batch A — 17 slots

### 1. W2-A-0061 — Topology is lost at checkpoint-selection time, not training time
- **Cluster:** training/selection dynamics. **R2 verdict: SURVIVE-IF-EXPERIMENT** (J's bare SURVIVE demoted by PI_BINDING after L's Finding 2).
- **Killer experiment:** Multi-seed, multi-architecture full-checkpoint logging on vessel/airway segmentation with train/val/test topology trajectories measured by **Betti matching, not raw Betti numbers, no dimension aggregation** (arXiv 2412.14619's guidance), plus a selection-noise control. **Exact residual to state up front:** HyperTopo-Adapters (arXiv 2601.06067) already ships a "min-PD within top-K Dice" selection rule on one Kaggle leaf-lesion dataset — it proves appetite and kills the "nobody has looked at selection" framing; what remains open is the systematic multi-seed, multi-benchmark quantification of how much topology Dice-based selection discards, with selection-noise controls and the field-level cost accounting (training-time topology losses paid for a selection-time problem).
- **Why it survived the cut:** Still the cheapest decisive result in batch A — every checkpoint is already logged in a normal run — but it is now a this-cycle window, not a comfortable one. Protected. PI correlated-pair warning: with A-0206 this is one "diagnosis-without-fix" bet, not two.

### 2. W2-A-0206 (←A-0264 arm) — SAM-fingerprint forensics with a controlled-provenance corpus
- **Cluster:** provenance/contamination forensics. **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Build the controlled-provenance corpus — same images, same annotators, three arms (hand-drawn; SAM-assisted with edit-depth logged; raw SAM) — and require the fingerprint classifier to generalize across datasets with dataset identity controlled, separating SAM style from dataset dialect (the A-0312 confound). Inheritance measured by training matched models on provenance-only-differing labels. Hosts A-0264's pseudo-label error-anatomy arm per I's fold.
- **Why it survived:** Data-genetics flagship; L's live spot-check found a dense generated-**image** attribution literature but **no mask-space provenance work** — window open, urgency real, and the image-attribution toolbox is the method shelf. Must not be greenlit without the dialect control. A-0205 (verification-bias human study) cut but revivable as this program's human-study arm.

### 3. W2-A-0175 — Physical calibration-shape ground truth: the zero-annotation boundary benchmark
- **Cluster:** annotation & boundary metrology. **R2 verdict (J): SURVIVE-IF-EXPERIMENT (pilot-gated).**
- **Killer experiment:** Pilot with a full GT error budget — registration + optics + edge-definition-convention sensitivity (50%-crossing vs geometric projection differ at exactly the sub-pixel scale claimed) — published as Table 1; viable only if model systematic biases ≫ GT error budget. One consequence demonstration required: a published sub-3px claim reversing under physical GT.
- **Why it survived:** No prior segmentation-metrology benchmark exists; instrument unclaimed; protected, with a real silencing experiment. Feeds A-0276 (scaling exponents) as a second-wave consumer.

### 4. W2-A-0163 (←A-0151 arm) — Stuff-stuff boundaries are bands, not curves: the transition-band atlas
- **Cluster:** annotation & boundary metrology (taxonomy slot 1 of 2). **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Multi-rater band atlas on Cityscapes/ADE with a fixed annotation interface; band-aware re-scoring of public models with bootstrap CIs on rank changes; mandatory per-pair-tolerance Boundary IoU baseline. Hosts A-0151's three-way boundary-error-budget arm per I's fold (J's identifiability point: 0151's "annotation share" is only definable with 0163's band taxonomy — one multi-rater pool, one paper family). Rank-flip claims must consume the statistics layer (C-0300/rigor program) as a prerequisite.
- **Why it survived:** J's #3 paper-shaped in batch A; unambiguous deliverable; L's constructive-quota list names it a LOCK-ready constructive candidate (band-aware GT + scoring is an artifact, not just a complaint).

### 5. W2-A-0237 (←A-0249, C-0208 arms) — Convention/quality/model three-way decomposition of "domain gap", with the UDA-credit smoking gun
- **Cluster:** annotation & boundary metrology (taxonomy slot 2 of 2). **R2 verdict (J): MUTATE, merge mandatory.**
- **Killer experiment:** Convention arm (source-protocol re-annotation of target images, NLP "Annotation Matters" template cited) + quality arm (within-protocol error adjudicated by target-protocol-trained raters) + evaluation of source and UDA-adapted models against all three references — testing whether UDA gains concentrate in the convention share. Hosts C-0208's label-conventions-are-a-domain arm per I's fold.
- **Why it survived:** Half-scooped phenomenon (label effect ≈ 5× model effect) but the segmentation-specific decomposition plus the UDA-credit test is unclaimed; shares the taxonomy infrastructure with 0163 (one bet with it under the PI's correlated-cluster declaration).

### 6. W2-A-0121 — Mirror-geometry-verified phantom objects in puddles (camera-side audit)
- **Cluster:** domain safety probes. **R2 verdict (J): SURVIVE-IF-EXPERIMENT (pilot-gated).**
- **Killer experiment:** One-week pilot: 5 models on ACDC-rain/BDD-rainy/nuImages-rain, mirror-symmetry test about the road plane with an uncertainty band, 200 hand-verified flags, pre-registered phantom-rate floor; fund the full audit only if the floor is exceeded. LiDAR-side phenomenon is published (VehicleSec 2026, patents); the camera-side measurement is what is missing.
- **Why it survived:** Best forensic idea in C05 with a built-in physical verifier; A-LOCK in I's 200; pilot is cheap and strictly information-positive.

### 7. W2-A-0075 — Consensus fusion erases correct minority-expert detections
- **Cluster:** medical measurement science. **R2 verdict (J): SURVIVE-IF-EXPERIMENT (pilot-gated).**
- **Killer experiment:** LIDC-IDRI-anchored pilot: minority-only region precision vs matched random-region control, stratified by subtlety, pre-registered clinically meaningful effect size; then test whether modern locally-reliability-weighted fusion (RaLMPH, CASC-AI) still erases those regions, so global-STAPLE is not a strawman. Region-level outcome linkage is the feasibility crux.
- **Why it survived:** Most ethically loaded finding in the cluster; HRHR-protected; L names it the medical-executable candidate to promote post-pilot if the compute-partner question stays open.

### 8. W2-A-0326 — Signed context-value crossover curves for region vs boundary
- **Cluster:** detector psychophysics & context. **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Masked-radius context sweeps plus retrained variants, PLUS locality-embodying architectures (Swin, HRNet, bilateral nets) as natural experiments that must land on the predicted curve; pre-registered crossover-scale invariance test; monotonicity-dogma framing dropped.
- **Why it survived:** Compute-bounded, property-resolved, free architectural cross-validation; boundary metrics coordinate with 0175/0163.

### 9. W2-A-0074 — Are segmentation-derived volume CIs valid? Coverage audit + deployed-pipeline survey
- **Cluster:** medical measurement science. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Mandatory deployed-pipeline survey (who actually propagates what — itself a contribution), then a coverage audit on synthetic-GT lesions run separately for variance-propagation and pixelwise-conformal pipelines, with a correlation-length regression; COMPASS/CONSIGN/CONSeg as reference bounds.
- **Why it survived:** Clinically consequential and checkable; the conformal line answered the method question but nobody audited deployed practice or the per-pipeline coverage direction.

### 10. W2-A-0331 — Dice's per-instance gradient starvation, instrumented
- **Cluster:** medical measurement science. **R2 verdict (J): MUTATE — pursue first or drop (freshness-fragile).**
- **Killer experiment:** Instrumented training on two multi-lesion 2D datasets; regress per-lesion recall on starvation + size + contrast + location with a pre-registered partial-effect threshold (beat the size-only predictor); intervene on gradient allocation at fixed data; test whether blob loss / CC-DiceCE equalize gradient shares or only outcomes.
- **Why it survived:** Instrument-level science on the loss the whole medical field uses; CC-DiceCE (ISBI 2026) is closing the niche — flagged first-in within the next-20.

### 11. W2-A-0349 — Convention-learnability: signed model-vs-own-training-label offsets per junction type
- **Cluster:** annotation & boundary metrology. **R2 verdict (J): MUTATE** (demoted to FLEX by I; survives here on depth).
- **Killer experiment:** Signed offset between model outputs and their own training labels per junction type, scaling with local photometric evidence strength; free-labeling human arm separates written-protocol sociology from psychology; curvature/function dissociation control (Hoffman-Richards confound) mandatory.
- **Why it survived:** Deepest surviving reframing of what boundary error means; fresh searches found nothing occupying it.

### 12. W2-A-0145 — Findability bias in camouflage datasets, bounded by temporal adjacency
- **Cluster:** domain safety/ecology probes. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Temporal-adjacency verification in burst/video camera-trap archives: animal visibly identifiable at t±k but hard at t; measure human + model recall on the t frames; claim an existence proof and a bound, not a benchmark correction. Removes the ecology-collaboration wall and the occlusion confound.
- **Why it survived:** Original selection-bias claim at reduced, executable scope; portfolio diversity beyond benchmarks-and-backbones.

### 13. W2-A-0026 (←C-0082-mut arm) — Causal map of VOS failure: variance decomposition + failure-prediction law
- **Cluster:** interactive/video segmentation behavior. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Variance decomposition of per-object degradation into smooth slope vs discrete events, regressed on frame-0 ambiguity vs motion/occlusion covariates, on vanilla AND memory-fixed SAM2 (DAVIS+MOSE+LVOS). Hosts the **PI-revived C-0082-mut arm**: regress SAM/SAM2 failure (IoU < τ) on computable image properties across ≥5 domain-shifted datasets, validate the fitted law on 2 held-out domains (fresh scoop-check on the SAM-failure-atlas family first, per L).
- **Why it survived:** The SAM2 behavioral-science unit per I's fold; triage becomes a corollary of the causal map.

### 14. W2-A-0028 — SAM2 teleport test: appearance vs location tracking
- **Cluster:** interactive/video segmentation behavior. **R2 verdict: none — PI_BINDING revive; requires a Reviewer-2 pass at Stage 5 before engineering.**
- **Killer experiment:** One GPU-day: prompt SAM2 on frame 0, teleport the object (cut-paste and curated cuts), measure whether the mask follows appearance or location under temporal sparsity; pre-register the either-outcome interpretation (appearance-tracking vs location-prior are both findings).
- **Why it survived:** PI_BINDING mandatory revive — F's "among the best of C02" (ROI 5, feasibility 5) that fell through the top-20 crack and was never attacked; the cheapest orphaned high-scorer and the SAM2/video-memory cluster's second, uncorrelated instrument alongside 0026.

### 15. W2-A-0215 — Protocol effect at zero annotation cost: COCO vs Sama-COCO
- **Cluster:** provenance/contamination forensics. **R2 verdict (J): MUTATE — framing dead as written (binding); only this mutation may proceed.**
- **Killer experiment:** Train matched models on COCO vs Sama-COCO label sets of the same images; evaluate on both test references + out-of-family data; compare deltas against a pre-registered mined distribution of published architecture gains (reuses the C-0300/A-0322 mining). GPU-week, zero annotation cost.
- **Why it survived:** Commissioned-corpus version dead on cost-benefit (Bauchwitz WACV 2025; Nature MI 2023; arXiv:2608.24486); the dual-label natural experiment is unclaimed and cheap. L's revive list endorses exactly this surviving form.

### 16. W2-A-0290 (←A-0300-mut arm) — Shared blind spots across the model zoo + lineage-resolved effective voters
- **Cluster:** monoculture & generality. **R2 verdict:** host unattacked (F Tier B); arm A-0300 **MUTATE (J)**.
- **Killer experiment:** Pixel-level shared-vs-unique error split across an accuracy-matched dense-model zoo (data-ecosystem holes vs architecture limits), with lineage-overlap covariates; hosts A-0300's mutated arm — effective-voter eigen-analysis on disjoint vs shared training corpora (the pixel-level shared-error map is the differentiator no VLM/LLM clone-detection paper has; era story demoted to a descriptive figure).
- **Why it survived:** I's fold makes 0290 the host and 0300 the arm; together they operationalize the monoculture thesis for dense prediction with one zoo.

### 17. W2-A-0199-mut — Context-completion hallucination as a training-data-grounded dose-response law
- **Cluster:** detector psychophysics & context. **R2 verdict (J): MUTATE — framing dead as written; PI_BINDING revives the mutation with L's larger claim.**
- **Killer experiment:** Mine object co-occurrence statistics from ADE20K/COCO-Stuff train sets; build **editing-based counterfactuals** (inpaint the target out — J's "editing beats curation" fix); measure hallucinated-pixel rate vs co-occurrence decile for ≥3 classical segmenters with fully known training data (~2 GPU-days), plus a real-scene validation subset. Must cite HalluSegBench/HII-DPO as the motivating VLM-side phenomenon and position as the mechanism/dose-response paper the VLM papers cannot run (they don't know their training data).
- **Why it survived:** L verified both scooping papers are VLM-side; the causal, training-data-grounded half is the scientifically stronger half, not a sliver. PI_BINDING mandates the slot.

---

## Batch B — 13 slots

### 18. W2-B-0114 — VPT gains decomposed: learned vs absorptive vs attention-bias, dense tasks only (4-arm form ONLY)
- **Cluster:** VFM register/PEFT mechanism (PEFT slot 1 of 2). **R2 verdict (H): SURVIVE-IF-EXPERIMENT — PI_BINDING: keep only this redesign or drop.**
- **Killer experiment:** 4-arm × 2-backbone design: full VPT vs frozen-random tokens vs attention-bias-only injection vs no-token, on register-free AND register-equipped siblings, ≥3 **dense** tasks (+ classification as reference), pre-registered prediction that register-equipped backbones gain less from VPT; DA-VPT cited up front; adopt the NOP-vs-broadcast register diagnostics (arXiv 2606.08105) as readout axes.
- **Why it survived:** The "afternoon frozen-token pilot" framing is struck everywhere — VPT's own Fig. 11 already showed Prompt-Fixed ≈ Linear (L Finding 1), so the naive form is dead by E's own pre-registered rule. What survives is H's dense-task mechanism paper: VPT's ablation was classification-only and register effects matter for dense prediction. PI correlated-pair warning: with B-0001 this is ONE register bet.

### 19. W2-B-0104 — The PEFT invariance-inheritance ceiling, dissociated from "LoRA learns less"
- **Cluster:** VFM register/PEFT mechanism (PEFT slot 2 of 2). **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** Invariance-dissociation grid: task pairs matched on frozen-probe difficulty but differing in invariance-breaking demand; LoRA across ranks including the mandatory high-rank arm vs full FT. Lives iff the PEFT gap tracks invariance-breaking demand at matched difficulty AND persists at high rank; else folds into a rank-dependence note.
- **Why it survived:** Only PEFT-family member whose killer experiment separates mechanism from tautology; B-0092/B-0101 cut under the ≤2 cap per H's own family warning.

### 20. W2-B-0001 — Register-norm artifact map: uncertainty channel or saliency prior?
- **Cluster:** VFM register/PEFT mechanism. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** Stratified AUROC audit (~1 GPU-week): norm map vs entropy, distance-to-boundary, edge density, prototype distance on ADE20K+Cityscapes, within foreground/background and boundary-distance strata, on register-free, register-equipped, and test-time-register-patched backbones; must beat cheap baselines within foreground on register-free models.
- **Why it survived:** L's independent live search reproduced H's finding that no paper sells the norm map as per-pixel uncertainty — window open. Executes on B-0114's backbone grid as the paired arm of the single register bet (PI pairing).

### 21. W2-B-0194 — Segmentation sycophancy under randomized prompt dose
- **Cluster:** interactive/video segmentation behavior. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** Randomized-dose protocol: difficulty-stratified images, prompt count assigned randomly 1–10, multiple click policies including RClicks' human-derived distribution; sycophancy exists iff the confidence–accuracy gap grows with randomized dose within strata (~1 week compute). Randomization kills the selection-bias objection.
- **Why it survived:** Safety-adjacent, cheap, decisive; the SAM-UQ literature provides the citation slot without owning the dose-response law. One program with B-0169.

### 22. W2-B-0169 — Negative-click dose-response across the policy envelope
- **Cluster:** interactive/video segmentation behavior. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Factorial positive × negative click sweep under ≥4 placement policies including RClicks' clickability model, ≥4 model families; survives iff degradation-beyond-k holds across the whole policy envelope, onset predictor validated out-of-policy.
- **Why it survived:** Felt daily, never measured; shares the randomized-dose + policy-envelope protocol with 0194 (the RClicks-hostage hedge).

### 23. W2-B-0268 — Generated-image contamination of web benchmarks, with calibration arms
- **Cluster:** provenance/contamination forensics. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Urgent.
- **Killer experiment:** Three calibration arms before any headline: placebo (pipeline on guaranteed-clean pre-2021 benchmarks), injection (seed known generated images at controlled rates, verify recovery), provenance (manual + watermark verification subsample with CIs); then the ranking-distortion audit.
- **Why it survived:** The generated-image version is undone; clean-baseline window closing; two-quarter clock.

### 24. W2-B-0213 (←0200, B-0042-residual) — Robust-inversion audit of VFM comparisons across resolution/probe conventions
- **Cluster:** protocol-confound audits. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Audit under ≥3 pre-registered matching definitions (pixel-, feature-map-, FLOP-matched) × probe capacities; deliverable is the set of published VFM conclusions that invert under ALL matchings; pre-committed publication either way. Hosts the name-choice protocol axis (B-0042 residual, per PI/H).
- **Why it survived:** Kerssies documented setting-sensitivity, not the all-matchings inversion set; two-quarter clock; disagreement-prone by design.

### 25. W2-B-0227 — Annotation-convention overfitting: precise single-rater labels transfer worse
- **Cluster:** supervision imprint on representations. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Natural-variation version only: multi-rater segmentation datasets, single-rater precise vs rater-sampled noisy targets at matched budget and matched held-out-rater source Dice; evaluate cross-domain transfer. Synthetic iid flips banned.
- **Why it survived:** Contrarian, decisive either way, cheap; the training-consequence claim none of the A-side convention audits makes.

### 26. W2-B-0263 — Label-integrity accounting of procedural vs generated corruption training
- **Cluster:** synthetic/generated data effects. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Same scenes, three arms (procedural / diffusion-edited / diffusion-edited + label-integrity filtering), severity matched by equal reference-model degradation; train identical segmenters, evaluate ACDC + real adverse sets; measure per-arm label-corruption rates. The accounting is the contribution regardless of which arm wins.
- **Why it survived:** Swims against WeatherDG/Cityscape-Adverse with a mechanism those papers don't measure.

### 27. W2-B-0304 — Categorical warping follows the supervision taxonomy
- **Cluster:** supervision imprint on representations. **R2 verdict (H): MUTATE.**
- **Killer experiment:** {CLIP-lineage, SSL, supervised-ImageNet ViT} × {3D-render, latent, image-space morphs}; pre-registered prediction that discontinuity locations align with human naming boundaries only for language-aligned models, taxonomy boundaries for supervised, neither for SSL; supervised-classifier control mandatory (categorical warping per se is a 2021 result).
- **Why it survived:** Clean, unoccupied psychophysics-grade paradigm; the taxonomy prediction is the insurance. Sole survivor of the language-imprint family in the 50 (0305/0307/0323 cut; 0317 cut as collaborator-gated).

### 28. W2-B-0164 — Savings/relearning dose curves for dense VFM forgetting
- **Cluster:** supervision imprint on representations. **R2 verdict (H): MUTATE.**
- **Killer experiment:** VFM single-task adaptation: savings-vs-dose curves against scratch-head controls AND representational probes (CKA, linear retention); deliverable is the dissociation where retention probes say "gone" but savings say "cheap to restore," localized by layer; positioned as the vision instantiation of ICML 2026's reversibility framework.
- **Why it survived:** Dense/vision quantification with never-trained controls is open and near-free.

### 29. W2-B-0286 (←B-0293 residual) — Site-invariance as a cross-family pretraining differentiator
- **Cluster:** medical measurement science. **R2 verdict (H): MUTATE.**
- **Killer experiment:** Cross-family (natural vs ≥4 medical FMs) × cross-modality (CXR/CT/pathology) site-decodability plus cross-site transfer on scanner-matched subsets; the paper is the decodability-to-transfer correlation and the family contrast, importing the pathology Robustness Index as baseline. Hosts the medical-pretraining-attribution residual (B-0293, G's conditional exercised — no compute partner).
- **Why it survived:** The natural-vs-medical family contrast with a transfer-prediction claim is unclaimed; the portfolio's cheapest medical-FM-science slot, which L's Finding 7 says must not go empty.

### 30. W2-B-0284 — The lesion-size/stride law and a feasibility calculator
- **Cluster:** medical measurement science. **R2 verdict: not attacked (G FLEX, E-protected, cheap); carried with unattacked-risk flag.**
- **Killer experiment:** Detectability/Dice as a function of lesion size in units of backbone stride across VFM backbones and adaptation regimes at fixed data; deliverable is a validated feasibility calculator tested prospectively on a held-out modality; a negative (non-stride-limited) result recalibrates sub-patch claims for medical.
- **Why it survived:** Cheap constructive mechanism with clinical planning value; complements 0286 without correlation. Needs a Stage-5 mini-attack.

---

## Batch C — 20 slots

### 31. W2-C-0306 — Conformal coverage destroyed by NMS + coverage-preserving suppression
- **Cluster:** NMS & confidence mechanism. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.** Mission-protected; urgent.
- **Killer experiment:** Gate: measure the fraction of GT objects whose only covering candidates NMS suppresses, across detectors/thresholds/crowdedness. If material, build coverage-preserving suppression vs SeqCRC-post-NMS AND the no-NMS IoU-aware-calibration baseline on the risk/set-size frontier.
- **Why it survived:** Formal-novelty moat; K's #1 paper-shaped C idea; third conformal-OD paper expected within months. One of L's named constructive candidates — PI_BINDING requires gravity to include it and/or C-0338.

### 32. W2-C-0338 (←C-0007, A-0164, A-0323, A-0071 arms) — The size-resolved human ceiling
- **Cluster:** GT-epistemology (slot 1 of 2). **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Per-size-bin human-human agreement AP vs model-GT AP with a pre-registered crossing point ("below s pixels, AP-small progress is unfalsifiable"); precondition: size census of the LVIS double annotations. Arms per I's fold + K's verdicts: C-0007/A-0164 tiny-object noise floor + jitter-propagation method; A-0323 general-classes human-mIoU; A-0071's consensus-referenced-ceiling correction (pairwise inter-rater Dice is NOT an upper bound — Cellpose-SAM argument).
- **Why it survived:** Label Convergence supplies the aggregate ceiling and the artifact; the size-stratified crossing point is the family's strongest post-0046 wedge. Wedges decay in months — first wave.

### 33. W2-C-0057 — The missing-annotation tax law (differential, anti-quality)
- **Cluster:** GT-epistemology (slot 2 of 2). **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Controlled deletion at rates r with uniform AND salience-matched deletion processes (fitted from COCO-ReM/MJ-COCO recovered-label statistics) across ≥15 detectors; distortion-vs-quality slopes and the leaderboard crossover. Inference-only.
- **Why it survived:** The differential effect (missing labels punish better detectors more) is unclaimed; takes the last capped GT-epistemology slot over 0326/0344/0259/0311 on cost and decisiveness.

### 34. W2-C-0158-mut — The winner's curse in detection confidences: selection-bias theory of post-NMS miscalibration
- **Cluster:** NMS & confidence mechanism. **R2 verdict (K): MUTATE.**
- **Killer experiment:** Derive expected overconfidence under an explicit selection model from candidate-cluster statistics; verify the predicted miscalibration curve across NMS variants; show the theory-implied correction matches/beats IoU-aware calibration where applicable.
- **Why it survived:** The empirics are owned (WACV 2024, IJCV 2024); the predictive theory is not. Narrowed form only, per PI directive.

### 35. W2-C-0308 — Machine psychophysics: adaptive staircases for detector thresholds
- **Cluster:** detector psychophysics & context. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** High-dimensional joint thresholds (occlusion × size × contrast × clutter) via QUEST+/AEPsych-grade staircases; predictive-validity gate: thresholds must out-predict per-stratum benchmark AP vs cheap baselines and dissociate equal-AP models.
- **Why it survived:** Top-decile originality at inference-scale cost; no detector application found; the validity gate makes the instrument falsifiable.

### 36. W2-C-0135 — Psychometric arbitration curves: when context overrides appearance
- **Cluster:** detector psychophysics & context. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Parametric appearance degradation in-context vs out-of-context; per-class P(detected) vs appearance evidence × context strength surfaces; context axis validated against training co-occurrence; matched-degradation controls.
- **Why it survived:** The arbitration curve is absent from a dense context-bias literature; detection-side complement to A-0199-mut's segmentation dose-response (shared co-occurrence mining, different tasks — coordinate, don't duplicate).

### 37. W2-C-0193 — Operating-point drift: fixed-threshold precision collapses under mild shift while AP barely moves
- **Cluster:** deployment & update reliability. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Shift ladder × 10 detectors: delta-AP vs delta-precision@fixed-τ decoupling curves, plus a label-free threshold-recalibration baseline showing the failure is cheaply correctable.
- **Why it survived:** Deployment monitoring is maturing but nobody isolated the operating-point failure mode; cheap, decisive, actionable.

### 38. W2-C-0321 — Negative-flip contracts for detector updates
- **Cluster:** deployment & update reliability. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Instance-level negative-flip rates across public detector version ladders at matched/improved AP; flip taxonomy including localization regressions invisible to AP; behavioral contract suite artifact + one positive-congruent mitigation baseline.
- **Why it survived:** Negative-flip literature owns classification/NLP/LLMs; detection version absent; artifact-class contribution.

### 39. W2-C-0136 + 0287 + 0302-mut (←A-0313, A-0198, C-0046-claims-residual arms) — The detection rigor program
- **Cluster:** claims rigor & benchmark statistics. **R2 verdicts (K):** 0136 SURVIVE-IF, 0287 SURVIVE-IF, 0302 MUTATE. One slot per K's shared-grid/absorb logic.
- **Killer experiment:** One shared seed grid: ≥7 seeds × 3 architectures × 2 schedules on COCO for variance-components decomposition (instance/image/seed/framework nested bootstrap); 5 seeds × 10 published ablation tables in original codebases for P(sign flip | claimed delta); claims audit restricted to scale-matched published deltas with a pre-registered inclusion rule and prospective interval validation. No flagship-scale extrapolation (died with B-0033; L's governance note on the B-0033 arm recorded — the ViT-S pretraining-variance arm stays **dormant-but-named**, executable only with partner compute). Arms: A-0313 segmentation power-audit; A-0198 seed-churn variance (relocated from cut C-0311); C-0043's MICCAI-facing size-stratified MDE arm; C-0046's claims-audit residual.
- **Why it survived:** Census confirmed open; ~12-month first-mover shelf life; one program instead of three correlated slots.

### 40. W2-C-0283 + 0285 (←C-0334 arm) — The pre-registered tuning-fairness audit
- **Cluster:** claims rigor & benchmark statistics. **R2 verdict (K): SURVIVE-IF-EXPERIMENT (both), merge recommended.**
- **Killer experiment:** Pre-registered 12–20 method-baseline pairs under two budget conventions (published budget; baseline given the method's disclosed trial count over a pre-declared space); headline is the claimed-minus-fair-budget delta distribution over time with CIs. **PI-revived C-0334 named arm:** NMS-free vs NMS comparisons where only the classical baseline's post-processing (NMS/score thresholds, top-k) is re-tuned on val at modest budget — post-processing explicitly written into the protocol as a tunable (closing the governance hole L flagged).
- **Why it survived:** Any reviewer treats 0283/0285 as one paper; the genre is proven and detection unserved; the 0334 arm gives it a concrete headline case for 1–2 GPU-days.

### 41. W2-C-0309-mut — What is an item in a detection benchmark? IRT with convention stability
- **Cluster:** claims rigor & benchmark statistics. **R2 verdict (K): MUTATE.**
- **Killer experiment:** 2PL/3PL fits over instance-outcome matrices across ≥30 detectors under ≥3 matching conventions (the convention-stability question is the new content); pre-registered misfit↔COCO-ReM lift; 1k short test validated on held-out model families; mandatory positioning against arXiv:2409.04041.
- **Why it survived:** Usable artifact + methods finding nobody owns; one of L's named constructive candidates.

### 42. W2-C-0011 — Template/synonym variance vs leaderboard margins in OVD
- **Cluster:** protocol-confound audits. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.** Two-quarter clock.
- **Killer experiment:** 10–15 OVD checkpoints × ~30 template/synonym sets on OV-COCO/OV-LVIS; induced AP-novel spread vs the distribution of published pairwise deltas; rank-inversion counts under template resampling.
- **Why it survived:** Method papers are starting to report template robustness — the leaderboard-level number is still unclaimed; window closing.

### 43. W2-C-0279 — Exposure residual structure: what rarity does beyond pretraining exposure
- **Cluster:** long-tail & exposure. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.** Fast lane.
- **Killer experiment:** Regress LVIS-rare per-class AP on estimated pretraining exposure; the paper lives in the residual structure (localization-vs-recognition decomposition) plus the invented-names zero-exposure causal arm; mandatory Udandarao positioning.
- **Why it survived:** Sharp wedge with a causal lever the exposure-law line lacks; execute early.

### 44. W2-C-0122-mut (←C-0264-dup, C-0298, A-0100 + A-0090 arms) — Duplication and leakage where they hurt
- **Cluster:** provenance/contamination forensics. **R2 verdict (K): MUTATE** (host); A-0100 arm **SURVIVE-IF (J)**.
- **Killer experiment:** LVIS-tail duplicate-concentration analysis; test-side dedup re-scoring for AP-inflation bounds (no retraining); cross-benchmark duplicate scan; generic census demoted to appendix (D-LeDe owns the pHash audit). **A-0100 arm (J's design intact):** smoke/fire video-provenance clustering with threshold-sweep curves, manual cluster verification per threshold, pre-registered bootstrap ranking-stability test — **plus the PI-revived A-0090 arm:** re-score public smoke-detection outputs with a time-to-detect metric, converting the debunk into audit + constructive metric proposal. Hosts C-0298's hash-variant audit.
- **Why it survived:** I's fold places A-0100 here under the contamination cap (≤5); the unit is certain-yield, fast, and now carries a constructive layer per L's Finding 3.

### 45. W2-C-0260 — Benchmark monoculture: the cross-dataset rank-generality census
- **Cluster:** monoculture & generality. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** 15 detectors × 8–10 datasets fine-tuned under one fixed protocol; rank correlation stratified by size/density/domain distance; published-claim inversion census; pre-committed null publication; per-class prediction release as the reusable artifact and reimplementation shield.
- **Why it survived:** COCO-O/BoB/COUNTS answer adjacent cells, not the fine-tuned rank-generality question; the most reusable audit artifact in batch C.

### 46. W2-C-0276 + 0256 (merged) — Long-tail forensics: tail-progress illusion + size-frequency confound, with prediction release
- **Cluster:** long-tail & exposure. **R2 verdict (K): SURVIVE-IF-EXPERIMENT (both), merge mandatory.**
- **Killer experiment:** Retrain 6–8 long-tail methods in one codebase (third-party checkpoints mostly unavailable); RELEASE per-class predictions; per-class delta concentration with bootstrap bands, the 0255 head-class utility arm, and the frequency-vs-size partial-effect decomposition inside the same grid.
- **Why it survived:** Dave et al.'s +2.9 AP-rare from ranking policy alone demands this audit; one merged paper where two slots were reviewer bait.

### 47. W2-C-0159 — Detection active learning replicated at realistic batch sizes and box costs
- **Cluster:** adaptation economics. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Lueth-for-detection: 6–8 published AL methods × 2 codebases × box-cost accounting × tuned-random × ≥5 seeds, pre-registered, deployment-scale batch sizes.
- **Why it survived:** Expensive-labeling stakes; the field's contradictory-conclusions problem is unresolved for detection; recent adjacent results sharpen rather than scoop.

### 48. W2-C-0226 — GT-controlled super-resolution truthfulness: recovered vs hallucinated AP
- **Cluster:** synthetic/generated data effects. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** HR-GT protocol: downsample, super-resolve, score against HR ground truth; decompose delta-AP into recovered vs hallucinated; classical-vs-generative contrast; Hallucination Score correlation arm; one real-LR validation arm. Hosts the 0248/0231 asymmetry and object-destruction arms.
- **Why it survived:** The detection-metric hallucination decomposition is confirmed unclaimed.

### 49. W2-C-0150-mut (←C-0221, A-0245 arms) — The exchange rate of adaptation: labeled-target-boxes equivalent of every UDA method
- **Cluster:** adaptation economics. **R2 verdict (K): MUTATE.**
- **Killer experiment:** N\* curves for 6–8 UDA methods: labeled target images (box-level cost axis) for plain fine-tuning to match each method, under old AND foundation-era backbones. Hosts the foundation-gap-closure arm (0221) and A-0245's cross-pair rank-stability arm per I's fold.
- **Why it survived:** Converts a self-retiring subfield's obituary into a permanent decision instrument; complements A-0237+0249 (economics vs label semantics).

### 50. W2-C-0300 (←C-0304-C, A-0322 arms) — The reproduction-noise floor: reproduction-gap meta-analysis + literature-mined spread table
- **Cluster:** claims rigor & benchmark statistics. **R2 verdict: host not attacked (G FLEX); carried as the portfolio's statistics prerequisite.**
- **Killer experiment:** Meta-analysis of reproduction gaps plus the A-0322 arm: mine score spread for identical model-benchmark pairs across published papers with citation-provenance tracking (copied numbers masquerading as reproductions); deliverable is a per-benchmark reproduction-noise table and the fraction of published deltas below the floor. Zero GPUs.
- **Why it survived:** J names the statistics keeps as *prerequisites* for every rank-flip claim in this portfolio (0163, 0122's arms, 0215-mut); I's fold hosts A-0322 here; cheapest high-value slot in the 50. Needs a Stage-5 mini-attack (host unattacked).
