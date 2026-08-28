# Windows2 Stage-4 Agent J — Reviewer-2 Attack on Batch-A Survivors

Attacker: Cloud Sub-Agent J (Reviewer #2 + freshness assassin). Scope: F's 20 PhD-year bets plus three shortlist members flagged by the PI (0175, 0334, 0026). Already-KILLED ideas skipped per instructions: W2-A-0017, W2-A-0051. I did not modify any F/G/H/I files.

Method: each idea is treated as a submitted paper and rejected as hard as possible on the standard axes (novelty, significance, hidden assumptions, confounders, missing baselines, dataset bias, weak metrics, unfair comparison, extra data/compute, cherry-picking, generalization, causal weakness, trivial alternatives, reproducibility, practical relevance, paper story). Then I ask: can a realistic experiment shut the reviewer up? Fresh arXiv/web searches (2024–2026, ~15 query batches run live during this review) supplement F's prior-work attack; **no paper below is cited from memory alone** — every citation was surfaced by a live search in this session or is explicitly inherited from F's verified list (marked "[F-verified]"). Where a fresh hit changes F's verdict, it is flagged **FRESHNESS HIT**.

Verdict semantics:
- **SURVIVE** — attack fails; idea stands as written.
- **SURVIVE-IF-EXPERIMENT** — the attack is answerable, but only by the named killer experiment; the idea should not be greenlit without committing to it (and to publishing the null if it comes out that way).
- **MUTATE** — as written the paper gets rejected; a specific mutation survives (given).
- **KILL** — no realistic experiment shuts the reviewer up.

Summary:

| ID | F's verdict | J's verdict | One-line reason |
|----|-------------|-------------|-----------------|
| 0206 | SURVIVE | SURVIVE-IF-EXPERIMENT | dataset-dialect confounder can fake the fingerprint; controlled-provenance test mandatory |
| 0163 | SURVIVE | SURVIVE-IF-EXPERIMENT | band atlas must show rank flips beyond reproduction noise |
| 0150 | SURVIVE | SURVIVE-IF-EXPERIMENT | signed-bias psychophysics with interface control is the whole paper |
| 0151 | SURVIVE | SURVIVE-IF-EXPERIMENT | decomposition not identifiable without synthetic-GT validation |
| 0075 | SURVIVE | SURVIVE-IF-EXPERIMENT | base-rate + case-selection confounds; outcome-anchored design still unclaimed |
| 0145 | SURVIVE | MUTATE | occlusion confound breaks GPS-collar design; temporal-adjacency verification survives |
| 0121 | SURVIVE | SURVIVE-IF-EXPERIMENT | LiDAR-side mirror phantoms now formalized (VehicleSec 2026); camera-side audit survives, null-risk real |
| 0249 | (Tier A keep) | MUTATE | label-vs-model effect now demonstrated; not identifiable separately from 0237 — merge |
| 0237 | SURVIVE | MUTATE | annotation-shift-vs-domain-shift re-annotation recipe now published in NLP — merge with 0249 |
| 0349 | SURVIVE | MUTATE | premise flaw: models are trained on human conventions; reframe as convention-learnability |
| 0074 | MUTATE | MUTATE (narrower) | **FRESHNESS HIT** COMPASS does metric-space conformal for segmentation-derived scalars |
| 0331 | MUTATE | MUTATE (narrower) | **FRESHNESS HIT** ISBI 2026 paper already contrasts instance-loss gradients |
| 0300 | MUTATE | MUTATE (narrower) | **FRESHNESS HIT** Hidden Clones brings correlated-error ensembles into vision-language |
| 0071 | (Tier B keep) | MUTATE | ceiling formalism is wrong: pairwise inter-rater Dice is not an upper bound |
| 0100 | (Tier B keep) | SURVIVE-IF-EXPERIMENT | methodology fully standard; the finding is the paper; applications venue |
| 0199 | (Tier A keep) | MUTATE (severe) | **FRESHNESS HIT** HalluSegBench + HII-DPO own the segmentation-hallucination framing |
| 0215 | (Tier B keep) | MUTATE | **FRESHNESS HIT** WACV 2025 + label-effect studies pre-empt the headline; zero-cost mutation exists |
| 0061 | (Tier B keep) | SURVIVE | cheapest unclaimed decisive result in the set |
| 0352 | MUTATE | MUTATE (harder) | supervision-budget circularity; physical-GT-anchored domains only |
| 0326 | MUTATE | SURVIVE-IF-EXPERIMENT | dual-branch architectures already act on the intuition; the measured crossover law is the only claim left |
| 0175 | (Tier A keep) | SURVIVE-IF-EXPERIMENT | PSF/edge-definition convention undermines "camera-true" GT at exactly sub-pixel scale |
| 0334 | MUTATE | MUTATE (narrower) | **FRESHNESS HIT** BareBones ships a silhouette-only recognition benchmark |
| 0026 | SURVIVE | MUTATE | online drift monitors dominate the pre-flight predictor; the surviving paper is the variance decomposition |

Totals: **0 KILL, 13 MUTATE, 9 SURVIVE-IF-EXPERIMENT, 1 SURVIVE** (23 attacked, 3 of them beyond the mandatory 20). Two ideas (0199, 0215) suffered **framing kills**: their headline claims as stated are dead to 2025–26 prior work and only survive as mutations.

---

## W2-A-0206 — SAM fingerprint forensics + inheritance

**Harshest rejection.** "Your fingerprint classifier does not detect SAM; it detects *datasets*. Your own sister idea (W2-A-0312) says annotation style is strong enough to classify a mask's source benchmark from geometry alone. Any dataset that used SAM assistance also differs from hand-drawn corpora in image sources, class mixes, annotator pools, resolutions, and polygon simplification settings. A classifier trained on 'known SAM/human pairs' scraped from different corpora learns the corpus, not the model. Your prevalence survey is then uninterpretable, and your 'inheritance' measurement inherits the same confound: models trained on 'high-fingerprint' datasets differ from controls in a hundred ways besides SAM provenance. Also: model attribution from outputs is a decade-old genre (GAN fingerprints), and dataset provenance/lineage tooling is an active engineering field — what remains is an application."

**Hidden assumptions.**
1. SAM style is separable from dataset dialect (the killer confound — nobody has shown this).
2. Post-editing by humans leaves enough residual signature (F noted this; verify with edit-depth-stratified data).
3. "Inheritance" is attributable: downstream models trained on fingerprinted data reproduce SAM's failure modes *because of the labels*, not because both saw similar web imagery.
4. Fresh check: no direct competitor surfaced in this session either (searches over SAM-mask provenance detection and machine-annotation auditing returned image-forgery localization, e.g. Loupe arXiv:2506.16819, and governance-side lineage tooling — nothing on mask-geometry provenance forensics). The window is still open, consistent with F.

**Killer experiment.** Controlled-provenance corpus: take ONE dataset's images; have the SAME annotator pool produce (a) hand-drawn masks, (b) SAM-assisted-then-edited masks at logged edit depths, (c) raw SAM masks. Train the fingerprint classifier on (a) vs (c), test on (b) and on *held-out datasets* with documented provenance. Only cross-dataset generalization of the fingerprint — with dataset identity controlled — licenses the prevalence survey. For inheritance: train matched models on (a) vs (b) labels of the same images (identical images, identical classes — only label provenance differs) and compare failure-mode profiles (wire breakage, hole filling) on a neutral probe set. This is exactly one annotation-controlled dataset plus standard training runs; realistic.

**Verdict: SURVIVE-IF-EXPERIMENT.** The idea is still the flagship, but greenlighting without the dialect control is how this paper dies at rebuttal.

---

## W2-A-0163 — Stuff-stuff transition-band atlas + band-aware evaluation

**Harshest rejection.** "Three objections. (1) Trivial alternative: Boundary IoU [F-verified, arXiv:2103.16562] already has a tolerance parameter; setting d per class-pair gives you 'band-aware evaluation' without any ontological manifesto — your contribution reduces to a lookup table of d values. (2) Unsurprising core: 'annotators disagree inside fuzzy transitions' is what everyone already believes; near-chance agreement inside bands confirms folklore. (3) Your headline — band-aware scoring changes stuff rankings — is a rank-flip claim, and rank flips on saturated benchmarks are routinely within reproduction noise (your own batch's 0313/0322 make this exact point). Fresh 2025 work already bins evaluation by distance-to-boundary bands for uncertainty calibration (BA-ECE, arXiv:2506.16589) and trains with boundary-band consistency losses (arXiv:2511.01434), so 'the field has no band concept' overstates the gap."

**Hidden assumptions.**
1. Band width is a property of the class pair, not of the image resolution, annotation tool, or zoom level (collides with 0150 — if boundary placement is scale-relative, the "band atlas" is scale-indexed, which the idea does not model).
2. The band-vs-edge classifier (needed because curbs are sharp) can be built without circularity — it must not use the very annotator-agreement data that defines the bands, or the evaluation reform becomes self-fulfilling.
3. Rank flips exceed retraining/reproduction noise.

**Killer experiment.** Multi-annotate (5+ raters) ~100 stuff-stuff transitions per class pair on Cityscapes/ADE subsets at fixed interface and resolution; publish class-pair band widths with CIs; re-score the public model zoo band-aware WITH bootstrap CIs on rankings; report the fraction of rank changes outside noise. Also run the trivial-alternative baseline (Boundary IoU with per-pair d) and show what the band model adds beyond it. All of this is cheap and decisive; the ontological claim stands or dies on the atlas.

**Verdict: SURVIVE-IF-EXPERIMENT** (the per-pair-d baseline is mandatory; without it, the paper is a rhetorical wrapper around a tolerance parameter).

---

## W2-A-0150 — Boundary GT is scale-relative

**Harshest rejection.** "Lower viewing resolution means less information; broader placement distributions at low zoom are a mathematical necessity, not a discovery. Your only novel claim is the SIGNED, systematic shift — and your design cannot isolate it: zoom level co-varies with brush radius in screen pixels, cursor gain, anti-aliased rendering of the image (the resampling kernel moves apparent edges by up to half a pixel by itself), and monitor PSF. WACV 2025 already showed task configuration (tools, workflow) shifts annotation quality and downstream models (Bauchwitz et al., WACV 2025); an interface artifact dressed up as psychophysics will not clear that bar. And your consequence leg — mixed-resolution training learns a boundary optimal at no scale — requires the shift to be large relative to inter-annotator noise, which you have not established; if the signed shift is 0.3 px against 2 px noise, the training consequence is unmeasurable."

**Hidden assumptions.**
1. The signed shift survives strict interface control (same brush in *image* pixels, same resampling kernel, randomized order).
2. Shift direction is consistent across annotators and boundary types (if half shift inward and half outward, there is no "bias field", only variance inflation — still a finding, but a different and weaker paper).
3. Dataset metadata (annotation zoom) is recoverable for the training-consequence leg — it mostly is not, so that leg needs purpose-built corpora.

**Killer experiment.** Within-annotator, within-object, randomized zoom-order psychophysics with the interface controls above; report the signed shift field vs noise floor per boundary-fuzziness class; pre-register the resampling-kernel control (annotate the SAME rendered pixels at different nominal zooms via interpolation-free integer scaling). Only if shift/noise > ~0.5 does the training-consequence leg get funded.

**Verdict: SURVIVE-IF-EXPERIMENT.** Foundational if the signed shift is real; an interface-artifact paper if not. The psychophysics leg is cheap; gate everything else on it.

---

## W2-A-0151 — Three-way boundary error budget (model / annotation / metric)

**Harshest rejection.** "Your decomposition is not identifiable. The 'annotation share' you estimate from multi-annotation spread conflates measurement error with genuine referent ambiguity — your own team's 0163 says the boundary is a BAND, in which case 'annotation imprecision' is not noise around a true curve but the absence of a true curve, and your error budget divides by a fiction. The model-side decomposition exists (Bernhard et al., WACV 2024 [F-verified]); noise-injection benchmarks exist (COCO-N, arXiv:2406.10891); Boundary IoU already calibrated tolerance from two-expert consistency. What's left is an estimator whose validity you assert but never test, extrapolated from 200 objects to benchmark-wide claims."

**Hidden assumptions.**
1. Annotation noise spectra measured at high zoom transfer to production annotations made at unknown zoom (collides with 0150).
2. Rasterization/metric share is separable from annotation share (both live in the same sub-3px band).
3. 200 objects, sampled feasibly, bound benchmark-wide budgets — needs stratified design + CIs, not means.

**Killer experiment.** Validate the estimator where truth is known: synthetic renders with exact vector GT, inject calibrated annotation noise (from the 0150-style psychophysics) and rasterization variants, confirm the decomposition recovers the injected shares. Then apply to 200 real objects per benchmark with stratified sampling. Publishing the estimator-validation table is what separates this from hand-waving.

**Verdict: SURVIVE-IF-EXPERIMENT** (the synthetic-validation leg is non-negotiable; also must define whether "annotation share" means noise-around-curve or band-width, and be consistent with 0163/0150 if all three ship from one lab).

---

## W2-A-0075 — Consensus fusion erases correct minority-expert detections

**Harshest rejection.** "Three statistical objections. (1) Base rate: regions flagged by exactly one of N experts are overwhelmingly false positives; 'true findings at a rate far above chance' is a trivial bar since chance is near zero — a 5% minority-region precision is 'far above chance' and clinically useless; you need to pre-register the precision threshold that would change fusion practice. (2) Outcome-verification selection: cases with pathology/follow-up are not a random sample — they skew toward clinically suspicious cases, which inflates minority-region precision exactly where you want to find it (confirmation built into the cohort). (3) Fusion research has moved past global STAPLE: 2025–26 methods already do per-sample, locally reliability-weighted fusion (RaLMPH, arXiv:2606.15554; CASC-AI, arXiv:2502.07302), so 'consensus erases the minority' attacks a 2004 strawman. Also everything hinges on rare data access — a promissory note, not a paper."

**Hidden assumptions.**
1. Minority-flagged regions can be linked to outcomes at region level (lesion-level pathology correlation is rarely recorded; often only patient-level outcomes exist — patient-level linkage dilutes the claim).
2. "Specialist minority" is identifiable ex ante (else post-hoc rater cherry-picking).
3. The finding transfers to modern locally-adaptive fusion, not just STAPLE.

**Killer experiment.** LIDC-IDRI-anchored pilot: 4 raters per nodule, partial diagnostic follow-up exists; measure precision of minority-only regions vs matched random regions of equal size/intensity statistics (the correct chance baseline), stratified by subtlety score; pre-register the effect size that matters (e.g., minority-region malignancy precision ≥ 3x matched-control precision, concentrated in low-prevalence subtypes). Then test whether RaLMPH-style modern fusion still erases those regions. If region-level outcome linkage proves impossible, the idea dies honestly at the pilot.

**Verdict: SURVIVE-IF-EXPERIMENT** (pilot-gated; the outcome-anchored instrument remains unclaimed — fresh searches again found only better-fusion methods, not the audit).

---

## W2-A-0145 — Findability bias: COD datasets contain only failed camouflage

**Harshest rejection.** "Your GPS-collar design cannot distinguish successful camouflage from physical occlusion. A collar says the animal is within the camera's frustum; it does not say photons from the animal reached the sensor. Recall failures on 'present-but-unfound' frames will be dominated by vegetation occlusion, motion blur, and frame-edge truncation — none of which is camouflage. Ecology has modeled imperfect detection for decades (occupancy models; the 'Framing pictures' framework, doi:10.1002/ece3.4878, lists 40 detection-bias factors; 2025 work quantifies AI/citizen-science classification bias, doi:10.1111/2041-210x.70132) — your contribution over that literature is exactly the camouflage-vs-occlusion separation you cannot make. Worse: COD benchmarks (COD10K/NC4K/CAMO) are internet photos of found animals, not camera-trap frames; a findability correction estimated on camera traps does not transfer to those benchmarks' statistics, so the promised 'asterisk on every COD number' does not follow. GPS-to-frustum geometry is also noisy (collar error tens of meters), and the ecology collaboration is a promissory note."

**Hidden assumptions.**
1. "In frustum" can be upgraded to "visible in principle" — the crux the original design lacks.
2. Findability bias measured in camera-trap conditions generalizes to COD benchmark imagery.
3. Enough verified-present-unfound frames exist to power the estimate.

**Killer experiment (mutation).** Replace collar verification with **temporal-adjacency verification**: in burst/video camera-trap archives, select frames at time t where the animal is *visibly identifiable in adjacent frames t±k* (so it is in view and unoccluded at essentially the same position) but hard/impossible to find at t; measure human and model recall on the t frames. Adjacent-frame visibility separates camouflage from occlusion by construction, uses existing public burst archives (no collar partnership), and directly yields the recall-vs-benchmark gap. Frame the deliverable as a *bound* on findability bias for camera-trap-like distributions, and drop the claim that it corrects COD benchmark numbers.

**Verdict: MUTATE** (temporal-adjacency design replaces the collar design; scope claim shrinks from "every COD number" to "an existence proof + bound for findability bias"). Data access stops being the wall; the ecology-vs-CV novelty defense must be explicit.

---

## W2-A-0121 — Mirror-geometry-verified phantom objects in puddles

**Harshest rejection.** "The phenomenon is neither hidden nor unmeasured. **FRESHNESS**: VehicleSec 2026 formalizes mirror-induced perception failures for AV stacks end-to-end — phantom Object Addition and Object Removal, physics-informed artifact models, CARLA injection (Yahia et al., 'Seeing is Deceiving', USENIX VehicleSec 2026) — and granted US patents (12481025, 12099123) already describe classifying puddle mirror images and inverting low observation points about the road plane; road-spray ghost objects are documented (arXiv:2310.00944). Industry has seen, named, and engineered around this failure. Your remaining claim is camera-segmentation-specific prevalence — and there you face a null-result trap: modern segmentation models trained on rainy-scene data may almost never segment reflected objects as real, in which case your paper's finding is 'the problem does not exist at the camera-semantics level.' Your mirror-symmetry verifier also assumes a planar road and a known homography; puddle surfaces ripple, and reflections are distorted — your verifier will have both false positives and blind spots you cannot quantify without hand labels, at which point why not just hand-label?"

**Hidden assumptions.**
1. Camera-side phantom rates are non-negligible in modern models (the entire paper bets on this; nobody has published the rate — which is also why it's still open).
2. Planar-mirror geometry approximates real puddles well enough to verify at scale.
3. Wet-scene subsets of public benchmarks are large enough to measure per-class phantom rates with CIs.

**Killer experiment.** One-week pilot before anything else: run 5 public models on curated wet subsets (ACDC-rain, BDD100K-rainy, nuImages rain), flag vehicle/pedestrian segments intersecting road-labeled regions, apply the mirror test with an uncertainty band, hand-verify 200 flags. If phantom rates are ≥ a pre-registered floor (e.g., >1 per 100 wet scenes for any class), fund the full audit + metric-blindness analysis; if not, kill and report the pilot in a workshop note. Positioning must lead with "the LiDAR side is known (VehicleSec 2026, patents); the camera-segmentation benchmark side is unmeasured."

**Verdict: SURVIVE-IF-EXPERIMENT** (pilot-gated; the "hidden error class" rhetoric must be retired — the class is known, the *measurement* is missing).

---

## W2-A-0249 — Reference-quality asymmetry inflates measured domain gaps

**Harshest rejection.** "**FRESHNESS**: the core phenomenon is now demonstrated. 'Model Effect or Label Effect?' (arXiv:2608.24486) holds model weights fixed and shows re-annotation shifts pooled DSC by 0.14–0.19 — several times the 0.03 model effect — for pulmonary embolism segmentation; the chest-radiography audit literature (arXiv:2509.15107) treats label quality and domain shift jointly. 'Target labels can be worse and it changes measured numbers' is no longer a suspicion needing a paper. What remains is your decomposition instrument — and it is confounded at its core: you cannot distinguish a target label that is *worse* from one that follows a *different convention* (that distinction is literally your sibling idea 0237). Your no-reannotation diagnostic makes this fatal: model-consensus statistics flag target labels as 'wrong' wherever they deviate from source-convention predictions — the diagnostic detects convention difference and calls it quality. You would 'correct' the gap by converting target labels to source conventions and book the change as a quality repair."

**Hidden assumptions.**
1. "Quality" is definable independently of convention — only possible as *within-protocol* error: violations of the target dataset's own written protocol, adjudicated by raters trained on the target protocol.
2. "Source-grade re-annotation" does not silently re-conventionize the labels (it does, unless protocol is explicitly held to target).
3. Quality asymmetry is common enough across benchmark pairs to matter (unknown a priori; survey risk).

**Killer experiment.** Only meaningful jointly with 0237 — see below.

**Verdict: MUTATE — merge with 0237** into a single three-way gap decomposition (appearance / convention / within-protocol quality). Standalone, 0249 is un-identifiable and half-scooped.

---

## W2-A-0237 — Annotation-convention shift masquerades as domain shift

**Harshest rejection.** "**FRESHNESS**: the exact recipe — re-annotate the external corpus under the source protocol, show the 'domain gap' was largely annotation shift — is now published in NLP with dramatic numbers (Hebrew offensive-language study, doi:10.63317/3fss6oc5mono: cross-corpus accuracy jumps up to +39.8 points under re-annotation, 'most of the cross-dataset failure … is an artifact of divergent annotation criteria'). Label-space and box-convention alignment is an active engineering line for detection (arXiv:2506.04737). Your conceptual novelty is spent; what's left is a segmentation-specific execution. And there your >25% quantifier hides the same identifiability problem as 0249: 'written protocols under-specify actual annotator behavior' (your own risk note), so annotators 'trained on source-dataset examples' will import source *quality* along with source *convention* — your convention fraction absorbs the quality fraction. Finally, the UDA-reinterpretation payoff assumes adaptation methods learn conventions; you never test that directly — a UDA method trained source→target could be evaluated against BOTH label sets, which you don't propose."

**Hidden assumptions.**
1. Convention is learnable-by-annotators to a reproducible standard (protocol-training fidelity is measurable — needs an inter-annotator check on the re-annotation itself).
2. Affected-class selection isn't cherry-picking (pre-register which classes are convention-exposed before re-annotating).
3. The convention fraction generalizes beyond the one canonical pair measured.

**Killer experiment (for the merged 0237+0249 paper).** For 2 benchmark pairs: (a) re-annotate 300 target images under source protocol by source-trained annotators (convention arm); (b) independently adjudicate within-protocol errors in original target labels by target-trained annotators (quality arm); (c) evaluate source models and UDA-adapted models against all three references (original target, convention-converted, quality-repaired). Decompose the measured gap into appearance / convention / quality with CIs, and test directly whether UDA gains concentrate in the convention share (the "adaptation methods get credit for learning label conventions" smoking gun). This is one coherent, fundable paper; two separate papers are each rejectable.

**Verdict: MUTATE — merge with 0249;** cite the NLP result as the template, own the segmentation-specific three-way decomposition and the UDA-credit test.

---

## W2-A-0349 — Human boundary conventions encode function, not photometry

**Harshest rejection.** "Your premise contradicts supervised learning. Models 'place boundaries where image evidence says' — except they are trained on *human-annotated* datasets that already embody the functional conventions you describe; a well-fit model reproduces the rider/bicycle split because Cityscapes' protocol mandates it, not because photometry says so. So the systematic divergence you propose to measure should be near zero for in-distribution junction types, and where it isn't, the parsimonious explanation is ordinary underfitting at low-evidence junctions, not a philosophical disagreement about what boundaries mean. Second: what you call 'human convention' is mostly *written protocol* — the rider/bike split is an instruction, not psychology; without a free-labeling annotator pool (no protocol) you are measuring dataset sociology, which is 0237's paper, not a psychophysics result. Third: Hoffman–Richards [F-verified] predicts part boundaries at curvature minima, which correlate with functional joints — your taxonomy must dissociate them or 'function' is unfalsifiable. The affordance-segmentation field (survey arXiv:2505.05074; ICCV 2025 language-guided affordance work) already operationalizes function-driven regions without your dichotomy."

**Hidden assumptions.**
1. Models systematically deviate from training-label conventions toward photometric edges (needs to be true for the headline; likely only true where local evidence is weak — which reframes the whole idea).
2. "Human convention" is protocol-independent (needs a free-labeling arm to establish).
3. Junction taxonomy is annotator-independent (F noted; multiple pools needed).

**Killer experiment (mutation).** Reframe as **convention-learnability**: for a taxonomy of junction types (with the curvature-minima/function dissociation control), measure (a) the signed offset between model boundaries and *their own training labels* per junction type, (b) how the offset scales with local photometric evidence strength, and (c) whether free-labeling humans (no protocol) agree with dataset protocol at those junctions. The paper becomes: WHICH functional conventions do models fail to learn, WHERE does photometry override the learned convention, and which "boundary errors" are convention disagreements. This keeps the deep question and drops the false model-vs-human dichotomy.

**Verdict: MUTATE** (the as-written framing gets destroyed in review by the "models are trained on human labels" observation; the learnability reframing survives and is still among the deepest ideas in the batch).

---

## W2-A-0074 — Volume CIs are anti-conservative under boundary-correlated errors

**Harshest rejection.** "**FRESHNESS**: the field has routed around your problem. COMPASS (arXiv:2509.22240) produces conformal intervals *directly for segmentation-derived metrics* (areas, organ size) with covariate-shift handling; CONSIGN (arXiv:2505.14113) builds spatial-correlation-aware conformal sets; CONSeg (arXiv:2502.21158) and conformal confidence sets (arXiv:2410.03406) give calibrated volumetric/spatial guarantees. Nobody defends pixel-independent propagation — you are auditing a method the literature already treats as wrong (SSN 2020 [F-verified] is premised on it). Name one deployed pipeline that actually computes volume CIs by independent-pixel propagation, or your 2–5x anti-conservatism factor is a number about a strawman. Also, your direction-of-error story needs care: naive *variance propagation* under-covers, but naive *pixelwise conformal* over-covers (CONSIGN's motivation) — 'pixel uncertainty gives wrong volume CIs' is two different failures depending on the pipeline, and conflating them will get caught."

**Hidden assumptions.**
1. Deployed/clinical pipelines exist that propagate pixelwise uncertainty to volume CIs naively (must be documented — FDA-cleared volumetry tools, radiomics packages — before any experiment).
2. Multi-rater "true volume" spread is small relative to the miscalibration measured (F noted; synthetic anchor required).
3. The correlation-length law is stable across modalities (else it's a per-dataset table, not a law).

**Killer experiment.** (1) Systematic survey of released uncertainty-to-volume code paths (MONAI-based pipelines, published radiomics/volumetry tools) documenting who actually propagates what — this is the strawman-proofing step and is itself a contribution; (2) coverage audit on synthetic lesions with exact GT + multi-rater sets, separately for variance-propagation and pixelwise-conformal pipelines, reporting the anti-conservatism/over-conservatism factor and its regression on measured boundary-error correlation length; (3) COMPASS/CONSeg as reference upper bounds, per F's mutation.

**Verdict: MUTATE (narrower than F's).** The audit survives only with the deployed-pipeline survey attached; otherwise it evaporates into "we knew pixel independence is wrong."

---

## W2-A-0331 — Dice's per-instance gradient starvation

**Harshest rejection.** "**FRESHNESS**: the gap is closing in-frame. Blob loss [F-verified, arXiv:2205.08209] owns the phenomenon statement; 'On the dice loss gradient' [F-verified, arXiv:2304.04319] did the analytical gradient work; and now CC-DiceCE (ISBI 2026, arXiv:2511.17146) benchmarks instance-wise losses in nnU-Net *and explicitly contrasts the gradient fields of competing instance losses* (their Fig. 2 discusses per-component gradient magnitudes under Voronoi decomposition). Your 'instrument the gradients' novelty is becoming these papers' figure panels. Deeper: your causal claim is confounded — gradient share correlates with instance size by construction, and size correlates with recall through resolution, contrast, and receptive-field effects that have nothing to do with the loss; 'starvation predicts misses' must beat the trivial size-only predictor or it is a re-description of 'small lesions are missed.' And your data-side fix is folklore: nnU-Net-style patch sampling already oversamples foreground, and per-component-normalized sampling is a standard trick; showing it 'recovers most missed instances' will read as confirming known practice."

**Hidden assumptions.**
1. Starvation ratio carries predictive information about per-lesion recall BEYOND lesion size and contrast (the entire scientific content; must be tested with size/contrast-controlled regression).
2. Gradient bookkeeping at instance level is numerically meaningful under mixed-precision/accumulation (engineering risk F noted).
3. The starvation law transfers across architectures (else it's a nnU-Net telemetry note).

**Killer experiment.** Instrument per-instance gradient shares during training on 2 multi-lesion 2D datasets; fit recall ~ starvation + size + contrast + location; the paper exists only if starvation has significant partial effect beyond covariates AND intervening on gradient allocation (per-component normalization at fixed data) moves recall as the law predicts, while blob-loss/CC-DiceCE-style fixes are tested for whether they equalize gradient shares or merely re-weight outcomes (F's mutation, kept). Pre-register the partial-effect threshold.

**Verdict: MUTATE (narrower than F's).** Six more months of instance-loss papers with gradient figures could flip this to KILL; if pursued, pursue first.

---

## W2-A-0300 — Ensemble-gain collapse by cohort era

**Harshest rejection.** "**FRESHNESS**: the correlated-errors result has now crossed into vision. Hidden Clones (arXiv:2603.17111) shows family-correlated errors in 17 vision-language models collapse effective ensemble size to 2.5–3.6 voters, with a question tier where voting hits 0%; Kim et al. ICML 2025 [F-verified] did 350+ LLMs; 'Great Models Think Alike' [F-verified] ties correlation to capability. 'The dense counterpart' is a domain-port of an established finding, and your era-longitudinal angle is methodologically the weakest part: era is confounded with scale, accuracy, data volume, AND architecture family simultaneously; 'scale-matched cohorts' across 2019–2025 barely exist for dense prediction (how many 2019-era models match a 2024 ViT-L in accuracy?); and public-checkpoint survivorship bias means your old cohorts are the unusually-good survivors. Any observed gain decline has five explanations before monoculture."

**Hidden assumptions.**
1. Enough public dense-prediction checkpoints per era exist to form accuracy-matched cohorts (inventory this FIRST; it is probably the binding constraint).
2. Lineage overlap is measurable (training-data disclosure is spotty; 'SA-1B-descended' is often unknowable).
3. Ensemble gain normalized by member accuracy is the right functional form (results will be sensitive to this choice — pre-register it).

**Killer experiment.** Pixel-level shared-error maps + effective-voter analysis (Hidden-Clones-style eigen-analysis, credited) across an accuracy-matched dense-model zoo, with lineage (data-overlap) as the regressor instead of era. Dropping "era" for "lineage" kills the worst confound: compare same-accuracy models with disjoint vs shared training corpora (medical vs web-descended, per the idea's own note). The longitudinal story becomes a supplementary descriptive figure, not the claim.

**Verdict: MUTATE (narrower than F's).** Lineage-regressed, not era-regressed; the pixel-level shared-error map is the differentiator vision-language work doesn't have.

---

## W2-A-0071 — Which leaderboards crossed their noise floor

**Harshest rejection.** "Your central inference — Dice above inter-rater agreement implies style fitting — is statistically wrong. Pairwise inter-rater Dice is NOT an upper bound on legitimate performance: a model matching the *consensus* of raters will beat any single pair's agreement (Cellpose-SAM makes exactly this argument, explicitly noting inter-human agreement is not a performance bound and that consensus segmentation halves error, doi:10.1101/2025.04.28.651001). CardioSAM (arXiv:2604.03313) already markets 'surpasses inter-expert agreement' as a FEATURE. So your audit, as stated, would flag legitimately-good models as epistemically empty. Meanwhile the leaderboard-fragility space is crowded: 'False Promises' (arXiv:2505.04720) quantified false outperformance claims in 53% of segmentation papers; RankInsight (arXiv:2512.19091) ships significance maps and metric-choice reversals; MICCAI 2024 'Confidence Intervals Uncovered' and Maier-Hein 2018 (both cited via those tools' documentation) covered rank instability. The harmonization of published inter-rater figures across protocols — your data plan — is exactly the apples-to-oranges exercise you'd reject in others."

**Hidden assumptions.**
1. A correct ceiling exists and is computable: it does, but it is the *consensus-referenced* ceiling (expected agreement of an infinite-rater consensus with held-out raters), not pairwise Dice — and computing it needs ≥3 raters per case, which most benchmarks lack.
2. Residual model errors can be projected onto "rater-style dimensions" (needs an explicit style basis — tightness, occlusion handling, hole conventions — measured from multi-rater data).
3. Published inter-rater figures are comparable enough to rank benchmarks (they are not; the audit must commission or reuse raw multi-rater masks, not published summary numbers).

**Killer experiment.** For 2–3 benchmarks with raw multi-rater data (or budgeted re-rating): compute the consensus-referenced ceiling properly (rater-vs-consensus curves extrapolated in N), locate SOTA relative to THAT, and decompose SOTA residuals into style-aligned vs anatomy-aligned components. The headline table becomes "distance to the correct ceiling," including cases (CardioSAM-style claims) where marketing used the wrong bar in the flattering direction.

**Verdict: MUTATE** (fix the ceiling formalism; the audit is then genuinely useful and fresh examples like CardioSAM give it a news hook — but as written it would be rejected by any statistically-literate reviewer, ironically for the same sin it audits).

---

## W2-A-0100 — Provenance-level leakage audit of smoke/fire benchmarks

**Harshest rejection.** "Zero methodological novelty: video-frame leakage is a named antipattern with published fixes — cluster-based splits via CLIP/DINO embeddings (IEEE Access 2024, doi:10.1109/access.2024.3383047; arXiv:2511.13944), and Ramos et al. ICCVW 2025 [F-verified] did the multi-dataset leakage-impact audit for visual benchmarks. You are running a standard pipeline on four small datasets; this is a data-cleaning tech report. Your >10-point-drop prediction is also unfalsifiable-as-stated: aggressive dedup over-merges distinct events (your own risk note), and the drop size depends monotonically on the merge threshold — you can dial the headline number. If rankings do NOT change after cleanup, there is no paper at all."

**Hidden assumptions.**
1. Same-event contamination is prevalent in the specific public smoke/fire benchmarks chosen (nobody has verified; that IS the paper).
2. Merge-threshold choices can be made principled (temporal-metadata + hand-verification of flagged clusters, threshold-sweep sensitivity reporting).
3. Public models/checkpoints exist to re-evaluate (else retraining budget enters).

**Killer experiment.** The audit itself, with two integrity locks: (a) threshold-sweep curves (performance drop as a function of dedup aggressiveness) instead of a single number, with manual verification of a random cluster sample at each threshold; (b) pre-registered ranking-stability test with bootstrap CIs so "rankings change" is a statistical claim. Two GPU-days plus curation; decisive either way for the safety-procurement story even if the CV-novelty story is thin.

**Verdict: SURVIVE-IF-EXPERIMENT** — with the honest caveat that this is an applications/dataset-track paper (or a strong workshop paper), not a main-track novelty claim. Its value to the PI is speed and certainty, not prestige.

---

## W2-A-0199 — Context-completion hallucination with dose-response

**Harshest rejection.** "**FRESHNESS — the framing is taken.** HalluSegBench (arXiv:2506.21546) is 'the first benchmark specifically designed to evaluate hallucinations in visual grounding through the lens of counterfactual visual reasoning': 1,340 factual/counterfactual pairs over 281 classes, metrics for hallucination severity, and the finding that vision-driven hallucinations dominate — for segmentation. HII-DPO (arXiv:2602.10425) names *scene-conditioned hallucination*, builds counterfactual object-removal images, and shows models assert removed objects because of scene-object co-occurrence priors. Causal-LLaVA (arXiv:2505.19474) and Image Tokens Matter (arXiv:2505.21547) trace hallucination to co-occurrence statistics mechanistically. Your paper's memorable sentence — 'dense prediction has a measurable prior-override failure mode analogous to LLM hallucination' — is now the related-work section. Your methodological choice (curating real dry-canal photos) is *weaker* than the published counterfactual-editing designs: curation cannot control confounds (drained pools differ from full pools in more than water), while editing can. What survives is one quantitative instrument: the dose-response law against association strength mined from training co-occurrence — untested in any of the above — and the extension from VLM-referring models to classical dense segmenters and stuff classes."

**Hidden assumptions.**
1. Training co-occurrence is minable (for classical segmenters with known training sets, yes; that's an advantage over closed VLMs — use it).
2. Real-scene curation adds value beyond edited counterfactuals (only as an ecological-validity check, not as the main design).
3. Hallucination rates for classical dense segmenters are non-trivial (plausible but unmeasured — pilot first).

**Killer experiment (mutation).** On classical segmenters with FULLY KNOWN training data (Cityscapes/ADE-trained zoo): mine context-class association strengths from the training corpora; build both edited counterfactuals (HalluSegBench-style, credited) and a small real-scene curated set; fit hallucination rate vs association strength per model family; test the evidence-ablation leg. The paper's claim becomes the *quantitative law and its training-statistics predictor*, explicitly positioned as the dense/classical complement to HalluSegBench.

**Verdict: MUTATE (severe — framing killed by freshness).** F ranked this #16 with SURVIVE-grade confidence and never web-attacked it; it is the largest freshness casualty in the batch. As a PhD-year bet it drops out of the top tier; as a well-scoped instrument paper it still exists.

---

## W2-A-0215 — Protocol choice dominates architecture improvement

**Harshest rejection.** "**FRESHNESS**: every component of your headline now has a published demonstration. Bauchwitz et al. (WACV 2025) manipulated annotation task configuration and measured effects through to *trained-model performance*; 'Labelling instructions matter' (Nature Machine Intelligence 2023, doi:10.1038/s42256-023-00625-5) established instruction effects on annotation quality at scale; and 'Model Effect or Label Effect?' (arXiv:2608.24486) quantified label effects (ΔDSC 0.14–0.19) as several times the model effect (0.03) with weights held fixed. Your specific comparison — boundary-first vs region-first professional protocols, trained-model deltas vs the median published architecture gain — is a refinement of a now-established conclusion, and you propose to spend a five-figure annotation budget to obtain it. Your yardstick ('median published architecture improvement') is also mushy: median over what set, which decade, which benchmark? That number can be curated to make the comparison land wherever you like."

**Hidden assumptions.**
1. Boundary-first vs region-first produces bigger deltas than the tool/config manipulations already published (unknown; if smaller, the paper is a null vs prior work).
2. "Neutral test set" exists (any test set embodies some protocol; the evaluation reference is not protocol-free — deep problem the proposal never addresses: models trained under protocol A will score higher on test labels drawn under protocol A; you need dual-protocol TEST labels too, doubling the corpus).
3. The vendor delivers protocol fidelity (needs manipulation checks).

**Killer experiment (mutation).** Zero-annotation-budget version: exploit existing dual-annotation corpora — COCO vs Sama-COCO [F-verified, arXiv:2311.02709] re-annotations of the SAME images under different campaigns/protocols. Train matched architectures on each label set; evaluate on BOTH test references plus out-of-family data; compare protocol-induced deltas against a pre-registered, systematically-collected distribution of published architecture gains (reuse 0322's mining). This converts a five-figure commissioning project into a GPU-week study, and the dual-test-reference design fixes the neutrality hole.

**Verdict: MUTATE** (the commissioned-corpus version is dead on cost-benefit given 2023–25 prior work; the Sama-COCO version survives and is cheap).

---

## W2-A-0061 — Topology is lost at checkpoint-selection time

**Harshest rejection.** "Betti-number estimates on a validation set are noisy; 'topology-selected checkpoints dominate' may be selection on noise, and your dominance claim will not replicate across seeds. The clDice/topology-loss literature (still churning: TopoSculpt arXiv:2509.03938; SDF-TopoNet arXiv:2503.14523; AC2RUNet arXiv:2606.12319) implicitly assumes training is the binding constraint — if your claim were true, someone would have noticed for free. Modern schedules (EMA weights, cosine-with-restarts) may erase the Dice-topology checkpoint divergence. And the practical payoff is a one-line fix (add topology to the selection criterion), which reviewers will call engineering."

**Hidden assumptions.**
1. Dice-vs-topology checkpoint divergence exists near convergence for standard pipelines (the claim; cheap to check).
2. Val-set topology metrics have enough SNR to select on (needs val-size/seed sensitivity analysis).
3. Result transfers across ≥3 architectures (own risk note; keep).

**Attack outcome.** No fresh prior work found on the checkpoint-selection reframing (searches returned only new topology losses and refinement modules — i.e., the field keeps paying training-time costs for what may be a selection-time loss, which is precisely the idea's point). Every attack above is answerable inside one cheap experiment: multi-seed, multi-architecture full-checkpoint logging with train/val/test topology trajectories and a selection-noise control. Either outcome teaches: dominance → free gains + field-level embarrassment; no dominance → topology is genuinely lost in training, validating the loss literature.

**Verdict: SURVIVE.** The cheapest unclaimed decisive result among all 23. The noise-control and seed-replication requirements go in the design, not against the idea.

---

## W2-A-0352 — Segmentation-free scalar measurement

**Harshest rejection.** "Three problems, one fatal-shaped. (1) The head-to-head genre exists in-domain and your hypothesis LOST: the fetal-head-circumference study (PMC8877769) ran exactly the fair segmentation-vs-regression comparison and segmentation won; direct cardiac volume estimation is 20+ years old (arXiv:1510.06375); choroidal-thickness regression is 'competitive', not superior (doi:10.3390/jcm11113203); counting is settled [F-verified]. Your prior is against you. (2) Supervision-budget circularity: for lesion volume and most medical scalars, the ground-truth scalar IS derived from expert masks — 'matched supervision cost' comparisons are incoherent when the regression target's provenance is segmentation; your regression arm trains on distilled mask labor while pretending to be mask-free. (3) The referee vanishes exactly where you predict wins: where boundary ambiguity is high, scalar GT (from masks) is equally uncertain, so 'regression beats segment-then-measure' is unmeasurable there by construction."

**Hidden assumptions.**
1. Mask-independent scalar ground truth exists for the chosen domains (this is THE design constraint, not a detail).
2. "Matched supervision cost" can be operationalized without circularity (only with physically-measured targets).
3. The boundary-ambiguity interaction is testable with a trustworthy referee at high ambiguity.

**Killer experiment (mutation).** Anchor every task in **physically-measured, mask-free ground truth**: phantom/ex-vivo lesion volumes by displacement or manufactured geometry; vegetation biomass by harvest weight; cell counts by flow cytometry or serial dilution. Then the interaction test is legitimate: vary boundary ambiguity (blur, phase, stain) while the physical referent stays exact, and measure where regression crosses segmentation. Without physical GT, drop the idea; with it, F's pre-registered-interaction mutation stands and the FHC counter-result becomes the baseline to beat rather than a refutation.

**Verdict: MUTATE (harder condition than F's).** F's mutation (exclude counting, pre-register interaction) is necessary but not sufficient; physical-GT anchoring is the actual survival condition.

---

## W2-A-0326 — Signed context-value curves (region vs boundary)

**Harshest rejection.** "The field already acts on your 'unexamined assumption': HRNet keeps a high-resolution pathway, bilateral/two-branch real-time nets (e.g. BEVANet, arXiv:2508.07300) explicitly separate detail and context branches, and Swin-style windowed attention IS bounded context — so 'a decade of architecture design assumes context monotonically helps' is a strawman built by ignoring half the architectures. RF non-monotonicity is documented in niches [F-verified: olfactory-bulb, TEM, amygdala RF studies], and 2025 remote-sensing work mechanistically derives boundary over-smoothing from large-receptive-field aggregation (CRISP, arXiv:2608.23746, frequency-domain analysis of context-induced high-frequency decay) — your phenomenon has a published mechanism sketch. Masked-attention inference is off-manifold (your own note), and the retrained-variant control at ViT scale across 3 datasets is not 'a week of compute.' What's left is the quantitative crossover law — real, but a measurement of a believed thing."

**Hidden assumptions.**
1. Attention-radius masking measures usable context rather than distribution shift (retraining arm is mandatory, and IS the compute cost — budget honestly: weeks, not a week).
2. The crossover scale is stable across datasets/architectures (else no "law", just a table).
3. Property split (region vs boundary) is clean at evaluation (boundary metrics inherit the C07 noise-floor problems — coordinate with 0151/0164 designs).

**Killer experiment.** F's mutation stands, with two additions: include architectures that already embody locality (Swin, HRNet, bilateral nets) as natural experiments — if the claim is right, their boundary-vs-region profiles should sit ON the predicted curve, providing cheap cross-validation without retraining everything; and pre-register the crossover-scale invariance test.

**Verdict: SURVIVE-IF-EXPERIMENT** (paper = the measured crossover law + its architectural cross-validation; the "decade of dogma" framing must go).

---

## W2-A-0175 — Physical calibration-shape ground truth (zero-annotation boundary benchmark)

**Harshest rejection.** "Your 'camera-true boundary with exact sub-pixel geometry' does not survive the optics. After lens PSF and defocus, the image of a printed edge is a blur profile several pixels wide; the 'true boundary' in image coordinates is then a *convention* — 50% intensity crossing? PSF-centroid? geometric projection of the physical edge through a calibrated lens model? These differ by exactly the sub-pixel amounts you claim to measure, so your metrology-grade GT quietly depends on an edge-definition choice — the same conventionality problem (cf. your own 0163/0150) you claim to escape, reintroduced at the sub-pixel scale. Registration via fiducials adds its own sub-pixel error budget you must propagate. Second: printed high-contrast shapes are trivially easy stimuli; a model zoo will saturate, and biases measured there (chromatic offsets, contrast-dependent placement) reflect the lab stimulus, not natural scenes — ecological validity is not an add-on, it is the objection. Third: so-what — if the systematic biases are smaller than annotation noise, they are by construction invisible in every application evaluated against annotations; name a downstream decision they change. Calibration-target literature (3D-printed targets with sub-pixel feature accuracy, arXiv:2608.05066; SynthCal, arXiv:2307.01013) shows the hardware is standard — your novelty is entirely in the segmentation-evaluation application."

**Hidden assumptions.**
1. An edge-definition convention can be fixed, justified, and propagated through the error budget (the paper must OWN this, deriving GT as the geometric projection under the calibrated optical model, with the convention-sensitivity reported as an uncertainty band).
2. Model biases measured on lab stimuli transfer to natural imagery (textured/embedded variants are necessary but not sufficient; a bridge experiment is needed — e.g., show the same contrast-dependent bias sign on real objects with independently-surveyed geometry).
3. At least one measured bias is consequential (e.g., flips a published boundary-method comparison, or biases a real measurement application from C03).

**Killer experiment.** Pilot: print/manufacture the target set (standard hardware per the calibration literature), image across 3 cameras, compute the full GT error budget (registration + optics + convention sensitivity); measure the model zoo; the benchmark is viable only if (model systematic biases) >> (GT error budget) — publish that inequality as Table 1. Then one consequence demonstration (a published sub-3px claim that reverses under physical GT).

**Verdict: SURVIVE-IF-EXPERIMENT.** No prior segmentation-metrology benchmark surfaced in fresh searches; the instrument is genuinely unclaimed — but the optics-convention problem must be solved on paper before any printing happens, or the whole benchmark measures its own PSF model.

---

## W2-A-0334 — Class-agnostic masks leak semantics

**Harshest rejection.** "**FRESHNESS**: the measurement instrument now exists. BareBones (arXiv:2604.10528) is a silhouette-only recognition benchmark — pixel-level silhouettes across six datasets, evaluated on 26 VLMs — that already operationalizes 'can category be recovered from mask shape alone.' Notably it found the OPPOSITE headline: VLMs collapse without texture ('Texture Bias Cliff'), so 'shape IS semantics' is at minimum model-dependent, and your high-accuracy claim requires attacker-trained shape classifiers, which lands you back in thirty-year-old silhouette recognition [F-verified: Mokhtarian & Murase]. The privacy leg has a strawman problem: WHO releases mask-only data as anonymization? You must document actual release practices ('semantic-free' claims in dataset cards, medical de-identification pipelines releasing organ masks) — if no documented practice exists, you are attacking a hypothetical, and privacy venues will say so. VLM-privacy work meanwhile is racing ahead on real attack surfaces (arXiv:2408.01228; arXiv:2608.01020)."

**Hidden assumptions.**
1. Real mask-only release practices exist and make implicit anonymity claims (must be documented FIRST — a survey of dataset cards/DUAs claiming masks are "de-identified" or "semantic-free" is the paper's foundation).
2. Scene/activity/demographic recovery from mask *ensembles* is where the new information is (single-mask category recovery is classical + now benchmarked).
3. Leakage persists across mask quality levels (own note; keep).

**Killer experiment (mutation).** (1) Documented-practice survey (the strawman-proofing); (2) attack exactly those release formats: from mask-only scenes, train recovery of scene type, activity, and sensitive attributes (medical condition from organ-mask morphology, floor plans from indoor mask layouts), reporting recovery rates vs quality; (3) position single-object shape→category as the known baseline (cite BareBones + classical silhouette work), claiming only the ensemble/privacy-audit layer.

**Verdict: MUTATE (narrower than F's).** The scientific "shape-semantics coupling" leg is now doubly occupied (classical + BareBones); only the documented-practice privacy audit survives, and it is conditional on such practices actually existing.

---

## W2-A-0026 — Masklet drift predictable from frame-0 ambiguity

**Harshest rejection.** "Practical relevance is inverted: the deployment problem your triage solves is already solved better by *online* monitors — object-pointer EMA distance flags drift as it starts (Prompt Self-Correction, Electronics 2025 [F-verified]), with one-frame latency and access to strictly more information than your frame-0 predictor; nobody needs a pre-flight forecast when the in-flight alarm is free. The science claim then carries everything, and it is fragile: drift on the benchmarks that matter (LVOS/MOSE long video) is dominated by discrete events — occlusions, reappearances, distractor switches — that frame-0 ambiguity cannot see (your own risk note), and 2025-26 memory work keeps showing failures are memory-selection artifacts (SAM2Long [F-verified]; Rethinking Memory Design, arXiv:2512.22624, argues tracking is 'bottlenecked by memory design'). An r>0.6 on short clean DAVIS clips will be read as 'ambiguous objects track worse,' which nobody doubts."

**Hidden assumptions.**
1. Drift *rate* (slope) is the right target as opposed to failure *events* (slope regression quietly excludes the catastrophic mode that matters).
2. Frame-0 features are causally upstream (ambiguity amplification) rather than correlated with object-class difficulty that also drives occlusion frequency (confounded; needs event/slope separation).
3. The prediction transfers across SAM2 variants (F's condition; keep).

**Killer experiment (mutation).** Variance decomposition rather than prediction headline: on DAVIS + MOSE + LVOS, decompose per-object tracking degradation into (a) smooth drift slope and (b) discrete failure events; regress each on frame-0 ambiguity features vs motion/occlusion covariates, on vanilla AND memory-fixed SAM2. Deliverable: what fraction of VOS failure is pre-determined at frame 0 vs event-driven vs memory-artifact — a causal map of where failure comes from, with the triage application demoted to a corollary.

**Verdict: MUTATE** (from "static predicts temporal" to "decompose the causes of temporal failure"; keeps the cheap-falsify protection, drops the claim that online monitors already dominate).

---

## Cross-cutting notes for the PI

1. **The re-annotation arbiter cluster shares one epistemic risk.** 0237, 0249, 0151, 0150, 0163, and 0071 all use "more/better annotations" as the referee, and all six quietly require a taxonomy that separates noise / convention / quality / genuine ambiguity. That taxonomy does not exist and is arguably the real foundational paper hiding inside this batch. If several of these are greenlit, build the taxonomy + shared annotation infrastructure ONCE.
2. **Rank-flip claims need the 0313/0322 statistics layer.** 0163, 0100, 0071 (and 0183 outside my scope) all promise "rankings change"; none can defend that without bootstrap/reproduction-noise CIs. Ship the statistics keeps first or jointly.
3. **The freshness-fragile set.** 0199 (already hit), 0331, 0300, 0074, 0215 sit in niches with multiple 2025–26 publications per quarter. Any of these, if pursued, should be re-searched at proposal time AND at experiment-freeze time.
4. **Curation-based causal designs lost to editing-based ones.** HalluSegBench/HII-DPO won 0199's ground with controlled counterfactual editing while 0199 proposed curation. Batch-A ideas that rely on "curate rare real scenes" as the causal control (0199, parts of 0121) should consider whether an editing/synthesis arm strengthens or replaces curation.
