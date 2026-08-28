# Windows2 Stage-3 Agent M — Top 50 (200 → 50 after Reviewer #2)

Agent M (Stage 2/3/4 merger; **not the PI, no final-3, no full research packages**). Date: 2026-08-28.

**Working 200:** Agent I's `provisional_200.md` does not exist, so the 200 was built as specified: G's 121 B∪C slots (`stage2_agent_G/provisional_200_partial.md`) + F's 75 batch-A keeps (`stage2_agent_F/shortlist.md`) = **196 units** (A-0017/A-0051 already dead before this stage).

**Binding inputs applied:** H/J/K `verdicts.jsonl` (no KILL hosts the 50; framing-dead ideas only in mutated form), PI_TO_I.md protections, and the Stage-3 caps (annotation-taxonomy ≤ 2, C GT-epistemology ≤ 2, B PEFT-mechanics ≤ 2, C eval-audit ≤ 40% of the 50).

## Headline accounting

| Batch | Slots in 50 | Bare SURVIVE | SURVIVE-IF-EXPERIMENT | MUTATE | Unattacked carry |
|---|---|---|---|---|---|
| A | 17 | 1 (A-0061) | 7 | 8 | 1 (A-0322) |
| B | 14 | 0 | 10 | 3 | 1 (B-0284) |
| C | 19 | 0 | 15 | 4 | 0 |
| **Total** | **50** | **1** | **32** | **15** | **2** |

C eval-audit share: 13/50 = 26% (≤ 40% cap ✓). All 8 protected ideas present (B-0114, B-0001, B-0104, B-0194, C-0306, A-0206, A-0061, A-0175). Diversity minima met: 5 medical, 3 SAM/video + 1 SAM-fingerprint, 3 PEFT/VFM mechanism, 6 detection-eval slots that are not generic annotation-noise.

Merged slots (one slot, multiple IDs): A-0237+0249 (J-mandated), C-0276+0256, C-0283+0285, C-0136+0287+0302 (K's shared-grid/absorb logic). Arms without slots living inside the 50: C-0007→0338, A-0071's residual→0338 positioning, C-0298→0122, C-0043→0338/rigor program, B-0200→0213, C-0080→(dead with 0046's host; tightness-drift note in rigor program).

---

## Batch A — 17 slots

### 1. W2-A-0061 — Topology is lost at checkpoint-selection time, not training time
- **Cluster:** training/selection dynamics. **R2 verdict (J): SURVIVE** — the only bare SURVIVE in the entire portfolio.
- **Killer experiment:** Multi-seed, multi-architecture full-checkpoint logging on vessel/airway segmentation with train/val/test topology (Betti/clDice) trajectories alongside Dice, plus a selection-noise control to show Dice-selected checkpoints sit systematically off the Dice–topology Pareto frontier relative to topology-aware selection. Either outcome teaches: if topology diverges late, the field is paying training-time costs (TopoSculpt, SDF-TopoNet, AC2RUNet keep shipping topology losses) for a selection-time problem; if not, the losses are vindicated.
- **Why it survived the cut:** Cheapest unclaimed decisive result of J's 23; every checkpoint is already logged in a normal run; fresh search found only new topology losses — which is the idea's own point. Protected by PI directive.

### 2. W2-A-0206 — SAM-fingerprint forensics with a controlled-provenance corpus
- **Cluster:** provenance/contamination forensics. **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Build a controlled-provenance corpus — same images, same annotators, three arms (hand-drawn, SAM-assisted with edit-depth logged, raw SAM) — and require the fingerprint classifier to generalize across datasets with dataset identity controlled, so SAM style is separated from dataset dialect (the confound that otherwise makes this a rediscovery of A-0312). Inheritance is then measured by training matched models on provenance-only-differing labels.
- **Why it survived:** Data-genetics flagship; two fresh searches again found no direct competitor; timely for every dataset built since 2023. Protected. Must not be greenlit without the dialect control. A-0205 (verification bias) and A-0312 (dialect classifier) are cut but revivable as arms of this program.

### 3. W2-A-0175 — Physical calibration-shape ground truth: the zero-annotation boundary benchmark
- **Cluster:** annotation & boundary metrology. **R2 verdict (J): SURVIVE-IF-EXPERIMENT (pilot-gated).**
- **Killer experiment:** Pilot with a full GT error budget — registration + optics + edge-definition-convention sensitivity (50%-crossing vs geometric projection differ at exactly the sub-pixel scale claimed) — published as Table 1; the benchmark is viable only if model systematic biases ≫ GT error budget. One consequence demonstration required: a published sub-3px claim reversing under physical GT.
- **Why it survived:** No prior segmentation-metrology benchmark exists (calibration-target literature serves camera geometry); instrument unclaimed; protected, and it still has a silencing experiment. The optics-convention problem must be solved on paper before printing.

### 4. W2-A-0163 — Stuff-stuff boundaries are bands, not curves: the transition-band atlas
- **Cluster:** annotation & boundary metrology (annotation-taxonomy slot 1 of 2). **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Multi-rater band atlas on Cityscapes/ADE with a fixed annotation interface; band-aware re-scoring of public models with bootstrap CIs on rank changes; mandatory per-pair-tolerance Boundary IoU baseline (the trivial alternative that must be beaten). Band width is scale- and interface-indexed, so the design must fix both.
- **Why it survived:** J's #3 paper-shaped in batch A: modest annotation budget, unambiguous deliverable (per-pair band widths + rank-change CIs). Takes one of the two capped taxonomy slots over 0150/0151/0071 on decisiveness per dollar.

### 5. W2-A-0237 + W2-A-0249 (merged) — Convention/quality/model three-way decomposition of "domain gap", with the UDA-credit smoking gun
- **Cluster:** annotation & boundary metrology (annotation-taxonomy slot 2 of 2). **R2 verdict (J): MUTATE, merge mandatory** (mutually unidentifiable standalone).
- **Killer experiment:** Merged design: a convention arm (source-protocol re-annotation of target images, following the NLP "Annotation Matters" template) + a quality arm (within-protocol error adjudicated by target-protocol-trained raters) + evaluation of source and UDA-adapted models against all three references — testing directly whether UDA gains concentrate in the convention share.
- **Why it survived:** The phenomenon is half-scooped (label-effect ≈ 5× model-effect, arXiv:2608.24486) but the segmentation-specific three-way decomposition plus the UDA-credit test is unclaimed and devastating if the >25% figure holds for one canonical pair.

### 6. W2-A-0121 — Mirror-geometry-verified phantom objects in puddles (camera-side audit)
- **Cluster:** domain safety probes. **R2 verdict (J): SURVIVE-IF-EXPERIMENT (pilot-gated).**
- **Killer experiment:** One-week pilot: 5 models on ACDC-rain/BDD-rainy/nuImages-rain, mirror-symmetry test about the road plane with an uncertainty band, 200 hand-verified flags, pre-registered phantom-rate floor; fund the full audit only if the floor is exceeded. Retire the "hidden error class" rhetoric — the LiDAR side is known (VehicleSec 2026, patents); the camera-side measurement is what is missing.
- **Why it survived:** Best forensic idea in C05 with a built-in physical verifier; the pilot is cheap and strictly information-positive; null-result trap is contained by the pre-registered floor.

### 7. W2-A-0075 — Consensus fusion erases correct minority-expert detections
- **Cluster:** medical measurement science. **R2 verdict (J): SURVIVE-IF-EXPERIMENT (pilot-gated).**
- **Killer experiment:** LIDC-IDRI-anchored pilot: minority-only region precision vs matched random-region control, stratified by subtlety, with a pre-registered clinically meaningful effect size; then test whether modern locally-reliability-weighted fusion (RaLMPH, CASC-AI) still erases those regions, so global-STAPLE is not a strawman. Region-level outcome linkage is the feasibility crux.
- **Why it survived:** Most ethically loaded finding available in the cluster; HRHR-protected since F; the pilot design resolves the data-access question cheaply before commitment.

### 8. W2-A-0100 — Provenance-level leakage audit of smoke/fire benchmarks
- **Cluster:** provenance/contamination forensics. **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** The audit itself with integrity locks: video-provenance clustering with threshold-sweep curves, manual cluster verification at each threshold, and a pre-registered bootstrap ranking-stability test — so the drop size cannot be dialed via the merge threshold and "rankings change" survives review.
- **Why it survived:** J's #2 paper-shaped: method standard, finding unclaimed, two GPU-days + curation. Honest venue is a dataset/applications track; value is speed and certainty.

### 9. W2-A-0326 — Signed context-value crossover curves for region vs boundary
- **Cluster:** detector psychophysics & context. **R2 verdict (J): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Masked-radius context sweeps plus retrained variants (answering the off-manifold objection), PLUS locality-embodying architectures (Swin, HRNet, bilateral nets) as natural experiments that must land on the predicted curve; pre-registered crossover-scale invariance test. Drop the "decade of monotonicity dogma" framing (Swin/HRNet already embody locality; CRISP derives boundary over-smoothing mechanistically).
- **Why it survived:** Compute-bounded, property-resolved, and the architectural cross-validation is free; boundary metrics must coordinate with the C07 noise-floor work (0175/0163).

### 10. W2-A-0074 — Are segmentation-derived volume CIs valid? Coverage audit + deployed-pipeline survey
- **Cluster:** medical measurement science. **R2 verdict (J): MUTATE** (concurs with F's mutation, narrower).
- **Killer experiment:** Mandatory strawman-proofing survey of deployed pipelines (who actually propagates what — itself a contribution), then a coverage audit on synthetic-GT lesions run separately for variance-propagation and pixelwise-conformal pipelines, with a correlation-length regression; COMPASS/CONSeg as reference bounds rather than competitors.
- **Why it survived:** Clinically consequential and checkable; the conformal literature (COMPASS, CONSIGN) answered the method question but nobody has audited what deployed pipelines actually do, and the anti-conservative-coverage direction remains unmeasured per pipeline type.

### 11. W2-A-0331 — Dice's per-instance gradient starvation, instrumented
- **Cluster:** medical measurement science. **R2 verdict (J): MUTATE — pursue first or drop (freshness-fragile).**
- **Killer experiment:** Instrumented training on two multi-lesion 2D datasets; regress per-lesion recall on starvation + size + contrast + location with a pre-registered partial-effect threshold (must beat the size-only predictor); intervene on gradient allocation at fixed data; test whether blob loss / CC-DiceCE equalize gradient shares or only outcomes.
- **Why it survived:** Instrument-level science on the loss the entire medical field uses; CC-DiceCE (ISBI 2026) is closing the niche, so this is first-in-or-drop — flagged for immediate execution in the next-20.

### 12. W2-A-0349 — Convention-learnability: signed model-vs-own-training-label offsets per junction type
- **Cluster:** annotation & boundary metrology. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Measure the signed offset between model outputs and their own training labels per junction type, scaling with local photometric evidence strength; a free-labeling human arm separates written-protocol sociology from psychology; a curvature/function dissociation control answers the Hoffman-Richards confound. (As originally written it dies to the observation that models are trained on labels already embodying the functional conventions.)
- **Why it survived:** Still among the deepest ideas in batch A after mutation; reframes what boundary error means; fresh searches found nothing occupying it.

### 13. W2-A-0145 — Findability bias in camouflage datasets, bounded by temporal adjacency
- **Cluster:** domain safety/ecology probes. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Temporal-adjacency verification in burst/video camera-trap archives: the animal is visibly identifiable at t±k but hard at t; measure human + model recall on the t frames; claim an existence proof and a bound, not a benchmark correction. This removes the ecology-collaboration wall of the GPS-collar design and dodges the occlusion confound.
- **Why it survived:** The selection-bias claim ("datasets contain only failed camouflage") remains original and testable at reduced scope; diversifies the portfolio beyond benchmarks-and-backbones.

### 14. W2-A-0026 — Where does VOS failure come from? Variance decomposition of masklet drift
- **Cluster:** interactive/video segmentation behavior. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Variance decomposition of per-object degradation into smooth slope vs discrete events (occlusions/switches), regressed on frame-0 ambiguity vs motion/occlusion covariates, on vanilla AND memory-fixed SAM2, across DAVIS+MOSE+LVOS. Triage ("static predicts temporal") becomes a corollary of the causal map rather than the headline.
- **Why it survived:** Satisfies the video diversity requirement with an attacked, named design; the memory-design literature keeps attributing failure to memory artifacts without this decomposition. (A-0028 teleport probe cut as the weaker sibling.)

### 15. W2-A-0215 — Protocol effect at zero annotation cost: COCO vs Sama-COCO
- **Cluster:** provenance/contamination forensics. **R2 verdict (J): MUTATE — framing dead as written (binding); only this mutation may proceed.**
- **Killer experiment:** Train matched models on COCO vs Sama-COCO label sets of the same images; evaluate on both test references + out-of-family data; compare deltas against a pre-registered mined distribution of published architecture gains (reusing A-0322's mining). GPU-week, zero annotation cost.
- **Why it survived:** The commissioned-corpus version is dead on cost-benefit against Bauchwitz WACV 2025 / Nature MI 2023 / arXiv:2608.24486, but the dual-label natural experiment is unclaimed, cheap, and quantifies protocol-as-treatment for segmentation specifically.

### 16. W2-A-0300 — Effective voters in dense prediction: lineage, not era, with pixel-level shared-error maps
- **Cluster:** monoculture & generality. **R2 verdict (J): MUTATE.**
- **Killer experiment:** Replace era with lineage: an accuracy-matched dense-model zoo split by disjoint vs shared training corpora; effective-voter eigen-analysis plus pixel-level shared-error maps; the longitudinal ensemble-collapse story is demoted to a descriptive figure.
- **Why it survived:** Hidden Clones (arXiv:2603.17111) took the VLM version, but the pixel-level shared-error map is the differentiator no VLM/LLM paper has, and it operationalizes the monoculture thesis for dense prediction.

### 17. W2-A-0322 — The reproduction-noise floor mined from the literature itself
- **Cluster:** annotation & boundary metrology (statistics layer). **R2 verdict: not attacked (F Tier B); carried as infrastructure.**
- **Killer experiment:** Meta-analysis of score spread for identical model-benchmark pairs across published papers, with citation-provenance tracking to prevent spread underestimates (copied numbers masquerading as reproductions); deliverable is a per-benchmark reproduction-noise table plus the fraction of published deltas smaller than the floor.
- **Why it survived:** Zero-GPU, immediately usable by every reviewer, and J explicitly names F's statistics keeps as *prerequisites* for the rank-flip claims elsewhere in this portfolio (0163, 0100, 0215-mutated). Cheapest high-value slot in batch A; C-0300-FLEX (reproduction-gap meta-analysis) cut as its duplicate.

---

## Batch B — 14 slots

### 18. W2-B-0114 — VPT prompt tokens are trainable registers: the 4-arm decomposition
- **Cluster:** VFM token/register & PEFT mechanism (PEFT slot 1 of 2). **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** 4-arm × 2-backbone design: full VPT vs frozen-random tokens vs attention-bias-only injection vs no-token, on register-free AND register-equipped siblings, ≥3 dense + 3 classification tasks, with the pre-registered prediction that register-equipped backbones gain less from VPT. DA-VPT cited up front; the attention-bias arm converts analogy into mechanism.
- **Why it survived:** H's best risk-adjusted bet in batch B — every cell of the outcome table publishes; census confirmed artifacts (DINOv2 ±reg pairs + official VPT code) make it an afternoon-scale start.

### 19. W2-B-0104 — The PEFT invariance-inheritance ceiling, dissociated from "LoRA learns less"
- **Cluster:** VFM token/register & PEFT mechanism (PEFT slot 2 of 2). **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** Invariance-dissociation grid: task pairs matched on frozen-probe difficulty but differing in invariance-breaking demand; LoRA across ranks including a mandatory high-rank arm vs full FT. The paper lives iff the PEFT gap tracks invariance-breaking demand at matched difficulty AND persists at high rank; if high rank closes the gap, fold into the rank-dependence story.
- **Why it survived:** The only member of the PEFT family whose killer experiment separates mechanism from tautology. B-0092/B-0101 cut under the ≤2 PEFT cap per H's own "at most two from this family" warning.

### 20. W2-B-0001 — Register-norm artifact map: uncertainty channel or saliency prior?
- **Cluster:** VFM token/register & PEFT mechanism. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** Stratified AUROC audit (~1 GPU-week): norm map vs entropy, distance-to-boundary, edge density, prototype distance on ADE20K+Cityscapes, within foreground/background and boundary-distance strata, on register-free, register-equipped, and test-time-register-patched backbones; must beat cheap baselines within foreground on register-free models.
- **Why it survived:** The honest reframing survives its own negative outcome (a deflationary note is still a finding), and no one has run this specific measurement despite the hottest artifact literature of 2024–26.

### 21. W2-B-0194 — Segmentation sycophancy under randomized prompt dose
- **Cluster:** interactive/video segmentation behavior. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Mission-protected.
- **Killer experiment:** Randomized-dose protocol: difficulty-stratified images, prompt count assigned randomly 1–10, multiple click policies including RClicks' human-derived distribution; sycophancy exists iff the confidence–accuracy gap grows with randomized dose within strata (~1 week of compute). The randomization kills the selection-bias objection (users escalate on hard cases) that sinks the observational version.
- **Why it survived:** Safety-adjacent, catchy, cheap; the SAM-UQ literature (UncertainSAM, RUAC) provides the citation slot without owning the dose-response law. Run as one program with B-0169.

### 22. W2-B-0169 — Negative-click dose-response across the policy envelope
- **Cluster:** interactive/video segmentation behavior. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Factorial positive × negative click sweep under ≥4 placement policies including RClicks' clickability model, across ≥4 model families; the claim survives iff degradation-beyond-k holds across the whole policy envelope, with the onset predictor validated out-of-policy. Both this and 0194 live inside RClicks' hostage situation — the shared protocol is the hedge.
- **Why it survived:** Felt daily, never measured, cheap, decisive either way; pairs with 0194 as one interactive-behavior program (two slots, one protocol).

### 23. W2-B-0268 — Generated-image contamination of web benchmarks, with calibration arms
- **Cluster:** provenance/contamination forensics. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.** Urgent (clean-baseline window closing).
- **Killer experiment:** Three calibration arms before any headline: placebo (run the pipeline on guaranteed-clean pre-2021 benchmarks), injection (seed known generated images at controlled rates, verify recovery), provenance (manual + watermark verification subsample with CIs). Only then the ranking-distortion audit — the calibration arms are the difference between science and a scare.
- **Why it survived:** The generated-image (as opposed to duplicate-leakage) version is undone; urgency is real; H paper-shaped #5. Two-quarter execution clock.

### 24. W2-B-0213 (+0200) — Robust-inversion audit of VFM comparisons across resolution/probe conventions
- **Cluster:** protocol-confound audits. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Audit under ≥3 pre-registered matching definitions (pixel-, feature-map-, FLOP-matched) × probe capacities; the deliverable is the set of published VFM conclusions that invert under ALL defensible matchings; if that set is empty, publish "rankings are resolution-robust" — pre-committed either way. Hosts B-0042's residual (name choice as a protocol axis).
- **Why it survived:** Kerssies documented setting-sensitivity but not the all-matchings inversion set; expect fights — that is the disagreement-prone value. Fastest-aging cluster: two-quarter clock.

### 25. W2-B-0227 — Annotation-convention overfitting: precise single-rater labels transfer worse
- **Cluster:** supervision imprint on representations. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Natural-variation version only: multi-rater segmentation datasets, single-rater precise vs rater-sampled noisy targets at matched budget and matched held-out-rater source Dice; evaluate cross-domain transfer. (Synthetic iid flips are banned — they don't model annotation structure; the matching protocol is the whole fight.)
- **Why it survived:** Contrarian, decisive either way, cheap; connects the B-side to the A-side annotation-convention agenda (0237+0249, 0215) with a training-consequence claim none of them makes.

### 26. W2-B-0263 — Label-integrity accounting of procedural vs generated corruption training
- **Cluster:** synthetic/generated data effects. **R2 verdict (H): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Same scenes, three arms (procedural / diffusion-edited / diffusion-edited + label-integrity filtering), severity matched by equal reference-model degradation; train identical segmenters, evaluate on ACDC + real adverse sets; measure per-arm label-corruption rates. The label-integrity accounting is the contribution regardless of which arm wins — the horse-race slogan is dropped.
- **Why it survived:** Swims against WeatherDG/Cityscape-Adverse currents with a mechanism (label corruption) those papers don't measure; every outcome is informative.

### 27. W2-B-0304 — Categorical warping follows the supervision taxonomy
- **Cluster:** supervision imprint on representations. **R2 verdict (H): MUTATE.**
- **Killer experiment:** Full grid: {CLIP-lineage, SSL, supervised-ImageNet ViT} × {3D-render, latent, image-space morphs}; pre-registered prediction that discontinuity locations align with human naming boundaries only for language-aligned models, taxonomy boundaries for supervised, neither for SSL; boundary depth/pose-decodability readout. The supervised-classifier control is mandatory (categorical warping per se is a 2021 result).
- **Why it survived:** H paper-shaped #7: smaller than the original pitch but a clean, unoccupied psychophysics-grade paradigm; the taxonomy prediction is the insurance against "any categorical supervision quantizes."

### 28. W2-B-0317 — Does MIL identifiability predict which concepts never emerge densely?
- **Cluster:** supervision imprint on representations. **R2 verdict (H): SURVIVE-IF-EXPERIMENT** (empirical program only; theory deferred).
- **Killer experiment:** On LAION-trained OpenCLIP: co-occurrence identifiability scores per concept; per-concept dense emergence; regression with SSL-decodability and frequency as covariates — the theory survives only if identifiability adds predictive power over frequency + difficulty. Theorem-level claims wait for the theory collaborator.
- **Why it survived:** Highest-ceiling idea in the language-imprint family; the covariate-controlled regression is affordable now and either validates or retires the framework before anyone commits a PhD year. Not in the next-20 (collaborator-gated).

### 29. W2-B-0164 — Savings/relearning dose curves for dense VFM forgetting
- **Cluster:** supervision imprint on representations. **R2 verdict (H): MUTATE.**
- **Killer experiment:** VFM single-task adaptation: savings-vs-dose curves against scratch-head controls AND representational probes (CKA, linear retention); the deliverable is the dissociation where retention probes say "gone" but savings say "cheap to restore," localized by layer — the vision instantiation of ICML 2026's reversibility framework, positioned as such.
- **Why it survived:** The conceptual flag is planted elsewhere (Unlearning Isn't Deletion), but the dense/vision quantification with never-trained controls is open and near-free; measures what every retention probe misses.

### 30. W2-B-0286 — Site-invariance as a cross-family pretraining differentiator
- **Cluster:** medical measurement science. **R2 verdict (H): MUTATE.**
- **Killer experiment:** Cross-family (natural vs ≥4 medical FMs) × cross-modality (CXR/CT/pathology) site-decodability plus cross-site transfer on scanner-matched subsets; the paper is the decodability-to-transfer correlation and the family contrast, importing the pathology Robustness Index (arXiv:2501.18055) as baseline rather than competing with it.
- **Why it survived:** The pathology audit exists; the natural-vs-medical family contrast with a transfer-prediction claim is the unclaimed part, and it is the portfolio's cheapest medical-FM science slot.

### 31. W2-B-0284 — The lesion-size/stride law and a feasibility calculator
- **Cluster:** medical measurement science. **R2 verdict: not attacked (G FLEX, E-protected, cheap); carried.**
- **Killer experiment:** Measure detectability/Dice as a function of lesion size in units of backbone stride across VFM backbones and adaptation regimes, holding data fixed; deliverable is a validated feasibility calculator ("given lesion-size distribution and backbone stride, expected ceiling is X") tested prospectively on a held-out modality. If the law is not stride-limited, the negative result recalibrates the sub-patch literature's medical claims.
- **Why it survived:** Cheap constructive mechanism with immediate clinical planning value; complements B-0286 without correlation (architecture-physics vs data-provenance); carried on E's protection with the unattacked-risk flag recorded.

---

## Batch C — 19 slots

### 32. W2-C-0306 — Conformal coverage destroyed by NMS + coverage-preserving suppression
- **Cluster:** NMS & confidence mechanism. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.** Mission-protected; urgent.
- **Killer experiment:** Gate first: measure the fraction of GT objects whose only covering candidates NMS suppresses, across detectors, thresholds, and crowdedness strata. If material, build coverage-preserving suppression and compare against SeqCRC-post-NMS AND the no-NMS IoU-aware-calibration baseline (now mandatory) on the risk/set-size frontier.
- **Why it survived:** Genuine formal novelty with a moat; K's #1 paper-shaped C idea; the third conformal-OD paper is expected within months — first wave of execution.

### 33. W2-C-0338 — The size-resolved human ceiling: below s pixels, AP-small progress is unfalsifiable
- **Cluster:** GT-epistemology (slot 1 of 2). **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Per-size-bin human-human agreement AP vs model-GT AP with a pre-registered crossing point; precondition is a size census of the LVIS double annotations. Label Convergence supplies the aggregate ceiling and the artifact; this takes the size-stratified slot it left open. Hosts C-0007 (tiny-object noise floor) as its benchmark-facing arm and absorbs A-0071's consensus-referenced-ceiling correction (pairwise inter-rater Dice is NOT an upper bound).
- **Why it survived:** Cheap, sharp, and the family's strongest post-0046 wedge; wedges decay in months — first wave.

### 34. W2-C-0057 — The missing-annotation tax law (differential, anti-quality)
- **Cluster:** GT-epistemology (slot 2 of 2). **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Controlled deletion at rates r with uniform AND salience-matched deletion processes (fitted from COCO-ReM/MJ-COCO recovered-label statistics) across ≥15 detectors; deliver distortion-vs-quality slopes and the leaderboard crossover point. Inference-only.
- **Why it survived:** The differential effect (missing labels punish better detectors more) remains unclaimed; ReM/MJ-COCO de-risk the premise and make the deletion model non-toy. Uses the last capped GT-epistemology slot over 0326/0344/0259/0311 on cost and decisiveness.

### 35. W2-C-0158 — The winner's curse in detection confidences: a selection-bias theory of post-NMS miscalibration
- **Cluster:** NMS & confidence mechanism. **R2 verdict (K): MUTATE.**
- **Killer experiment:** Derive expected overconfidence under an explicit selection model from candidate-cluster statistics; verify the predicted miscalibration curve across NMS variants; show the theory-implied correction matches or beats IoU-aware calibration where applicable. (The empirics — "NMS biases confidences" — are owned by WACV 2024/IJCV 2024; the predictive theory is not.)
- **Why it survived:** Only narrowed theory form admitted, per PI directive; pairs with 0306 as the NMS-mechanism duo without duplicating it (calibration vs coverage).

### 36. W2-C-0308 — Machine psychophysics: adaptive staircases for detector thresholds
- **Cluster:** detector psychophysics & context. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** High-dimensional joint thresholds (occlusion × size × contrast × clutter) where grid sweeps are infeasible, using mature staircase methodology (QUEST+/AEPsych); predictive-validity gate: thresholds must out-predict per-stratum benchmark AP against cheap baselines and dissociate equal-AP models, or the instrument is a curiosity.
- **Why it survived:** Top-decile originality, inference-scale cost, no detector application found in fresh search; the validity gate makes it falsifiable as an instrument.

### 37. W2-C-0135 — Psychometric arbitration curves: when context overrides appearance
- **Cluster:** detector psychophysics & context. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Parametric appearance degradation in-context vs out-of-context; per-class P(detected) vs appearance evidence × context strength surfaces; the context axis validated against training co-occurrence statistics; matched-degradation controls. The context-bias literature is dense (Mask Pooling, UFR, OOC detection) but the arbitration curve specifically is absent.
- **Why it survived:** Protected causal probe, cheap, and it carries the context-prior territory after A-0199's framing death (HalluSegBench/HII-DPO) — the portfolio keeps the mechanism without the scooped framing.

### 38. W2-C-0193 — Operating-point drift: fixed-threshold precision collapses under mild shift while AP barely moves
- **Cluster:** deployment & update reliability. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Shift ladder × 10 detectors: delta-AP vs delta-precision@fixed-τ decoupling curves, plus a label-free threshold-recalibration baseline showing the failure is cheaply correctable — which converts the audit into an actionable deployment result rather than a complaint.
- **Why it survived:** Deployment monitoring is maturing (D3M, sequential risk monitoring) but nobody isolated the operating-point failure mode; cheap and decisive; detection-eval diversity that is not annotation-noise.

### 39. W2-C-0321 — Negative-flip contracts for detector updates
- **Cluster:** deployment & update reliability. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Instance-level negative-flip rates across public detector version ladders at matched/improved AP; a flip taxonomy including localization regressions invisible to AP; deliverables are a behavioral contract suite artifact plus one positive-congruent mitigation baseline.
- **Why it survived:** The negative-flip literature owns classification/NLP/LLMs; the detection version is absent; artifact-class contribution with industrial pull.

### 40. W2-C-0136 + 0287 + 0302-mutated (merged) — The detection rigor program: seed-variance census, ablation sign-flip rates, resolution diagnostics
- **Cluster:** claims rigor & benchmark statistics. **R2 verdicts (K):** 0136 SURVIVE-IF, 0287 SURVIVE-IF, 0302 MUTATE. One slot per K's shared-grid and absorb logic (0311's flagship role is vacated by the GT-epistemology cap).
- **Killer experiment:** One shared seed grid: ≥7 seeds × 3 architectures × 2 schedules on COCO for the variance-components decomposition (instance/image/seed/framework nested bootstrap — the components LLM-eval statistics cannot see); 5 seeds × 10 published ablation tables in original codebases for P(sign flip | claimed delta); claims audit restricted to scale-matched published deltas with a pre-registered inclusion rule and prospective interval validation on fresh seeds. No flagship-scale extrapolation (that claim died with B-0033). Hosts C-0043's MICCAI-facing size-stratified MDE arm.
- **Why it survived:** The detection census is confirmed still open; the "port LLM-eval statistics" pattern has a ~12-month shelf life, so this ships as one first-mover program instead of three correlated slots.

### 41. W2-C-0283 + 0285 (merged) — The pre-registered tuning-fairness audit (stale baselines + shadow tuning)
- **Cluster:** claims rigor & benchmark statistics. **R2 verdict (K): SURVIVE-IF-EXPERIMENT (both), merge recommended.**
- **Killer experiment:** Pre-registered: 12–20 method-baseline pairs under two budget conventions — (a) the paper's own published budget, (b) baseline given exactly the method's disclosed trial count over a pre-declared search space; headline is the claimed-minus-fair-budget delta distribution over time (decay model) with CIs. detrex's +0.4–1.1 AP retuned-baseline gains are the prior to beat.
- **Why it survived:** Any reviewer treats 0283/0285 as one paper, so the portfolio does too; the genre (Musgrave/Dacrema) is proven and detection is unserved. Second rigor-family allowance under K's cap (0327-mutated cut, compute-conditional).

### 42. W2-C-0309-mutated — What is an item in a detection benchmark? IRT with convention stability
- **Cluster:** claims rigor & benchmark statistics. **R2 verdict (K): MUTATE.**
- **Killer experiment:** 2PL/3PL fits over instance-outcome matrices across ≥30 detectors under ≥3 matching conventions (the convention-stability question is the new content); pre-registered misfit↔COCO-ReM error-recovery lift; a 1k short test validated on held-out model families. Positioning against the 91-model vision IRT study (arXiv:2409.04041) is mandatory and survivable.
- **Why it survived:** K paper-shaped #7; produces a usable artifact (the short test) plus a methods finding (is the IRT fit an artifact of the matching rule?) that no one owns.

### 43. W2-C-0011 — Template/synonym variance vs leaderboard margins in OVD
- **Cluster:** protocol-confound audits. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.** Two-quarter clock.
- **Killer experiment:** 10–15 OVD checkpoints × ~30 template/synonym sets on OV-COCO/OV-LVIS; compare induced AP-novel spread against the distribution of published pairwise deltas; count rank inversions under template resampling. A two-GPU-week inference grid that ships the one number the field lacks.
- **Why it survived:** Method papers are starting to report template robustness (TG-OverLoCK) — the window is closing but the leaderboard-level number is still unclaimed; detection-eval diversity beyond annotation noise.

### 44. W2-C-0279 — Exposure residual structure: what rarity does beyond pretraining exposure
- **Cluster:** long-tail & exposure. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.** Fast lane.
- **Killer experiment:** Regress LVIS-rare per-class AP on estimated pretraining exposure (Udandarao's method); the paper lives in the residual structure — a localization-vs-recognition decomposition of exposure residuals — plus the invented-names zero-exposure causal arm. Mandatory Udandarao positioning: the correlational spine is owned; the decomposition and causal arm are not.
- **Why it survived:** Sharp wedge in a moving field; the invented-names arm gives it a causal lever the exposure-law line lacks; flagged for early execution.

### 45. W2-C-0122-mutated — Duplication where it hurts: tail concentration, dedup AP bounds, cross-benchmark leakage
- **Cluster:** provenance/contamination forensics. **R2 verdict (K): MUTATE.**
- **Killer experiment:** LVIS-tail duplicate-concentration analysis (the 0264 arm), test-side dedup re-scoring for AP-inflation bounds (no retraining), and a cross-benchmark duplicate scan; the generic census is demoted to an appendix (D-LeDe published the pHash audit with the KITTI scandal number). Hosts C-0298's hash-variant audit as a side arm.
- **Why it survived:** The where-it-hurts version is unclaimed and certain-yield; anchors the C-side of the contamination cluster while C-0345 is deferred (bundle/stagger per K).

### 46. W2-C-0260 — Benchmark monoculture: the cross-dataset rank-generality census
- **Cluster:** monoculture & generality. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** 15 detectors × 8–10 datasets fine-tuned under one fixed protocol; rank correlation stratified by object size/density/domain distance; a published-claim inversion census; pre-committed null publication if rankings are stable. The per-class prediction release is the reusable artifact and the shield against reimplementation-fidelity attacks.
- **Why it survived:** COCO-O/BoB/COUNTS answer adjacent cells but not the fine-tuned rank-generality question; D bet #7; the most reusable audit artifact in batch C.

### 47. W2-C-0276 + 0256 (merged) — Long-tail forensics: tail-progress illusion + size-frequency confound, with prediction release
- **Cluster:** long-tail & exposure. **R2 verdict (K): SURVIVE-IF-EXPERIMENT (both), merge mandatory (salami-slicing defense).**
- **Killer experiment:** Retrain 6–8 long-tail methods in one codebase (third-party checkpoints are mostly unavailable — G census); RELEASE per-class predictions as the artifact; per-class delta concentration with bootstrap bands, the 0255 head-class utility arm, and the frequency-vs-size partial-effect decomposition inside the same grid.
- **Why it survived:** Dave et al.'s +2.9 AP-rare from ranking policy alone is re-verified and demands this audit; one merged paper is fundable where two slots were reviewer bait.

### 48. W2-C-0159 — Detection active learning replicated at realistic batch sizes and box costs
- **Cluster:** adaptation economics. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** Lueth-for-detection: 6–8 published AL methods × 2 codebases × box-cost accounting × tuned-random baseline × ≥5 seeds, pre-registered, batch sizes at deployment scale. Recent adjacent results (SOTA AL loses to random under box-cost; rankings flip across val sets) sharpen rather than scoop the design.
- **Why it survived:** Expensive-labeling stakes, survived attack with high confidence, and the field's contradictory-conclusions problem (ALBench motivation) is still unresolved for detection.

### 49. W2-C-0226 — GT-controlled super-resolution truthfulness: recovered vs hallucinated AP
- **Cluster:** synthetic/generated data effects. **R2 verdict (K): SURVIVE-IF-EXPERIMENT.**
- **Killer experiment:** HR-GT protocol: downsample, super-resolve, score against HR ground truth; decompose delta-AP into recovered information vs hallucination; classical-vs-generative SR contrast; Hallucination Score correlation arm (comparator, not competitor); one real-LR validation arm to answer the synthetic-degradation objection.
- **Why it survived:** The detection-metric hallucination decomposition is confirmed unclaimed; hosts the 0248/0231 asymmetry and object-destruction arms from G's merge.

### 50. W2-C-0150-mutated — The exchange rate of adaptation: labeled-target-boxes equivalent of every UDA method
- **Cluster:** adaptation economics. **R2 verdict (K): MUTATE.**
- **Killer experiment:** N\* curves for 6–8 UDA methods: how many labeled target images (with a box-level cost axis) plain fine-tuning needs to match each method, under old AND foundation-era backbones. The field is self-retiring Mean-Teacher DAOD (arXiv:2503.23220; Foundational FSOD zero-shot already beats FSOD SOTA) — the exchange-rate instrument is what remains valuable.
- **Why it survived:** Converts a dying subfield's obituary into a permanent decision instrument; hosts the 0221 foundation-gap-closure arm; complements A-0237+0249's convention-share question without overlap (economics vs label semantics).
