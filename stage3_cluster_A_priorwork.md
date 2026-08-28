# Stage 3 — Cluster A Prior-Work Kill Report

**Sub-Agent G (adversarial Prior-Work Hunter) for Supervisor Windows7**
**Input:** 84 Cluster A survivors (from `stage2_cluster_A_survivors.md`, branch `cursor/stage2-cluster-a-scoring-0234`), full idea texts from `stage1_cluster_A_ideas.md` (branch `cursor/stage1-cluster-a-ideas-e2b2`). Cross-checked against Cluster B and C survivor lists for duplicates.
**Default assumption applied:** "this idea has probably already been done." All searches were real (web/arXiv/OpenReview/CVF). Where a search failed to surface a direct hit, this is stated explicitly and the idea was judged on adjacent literature, never on invented citations.

**Outcome: 84 → 17 survivors (12 KEEP + 5 MUTATE), 67 KILLED.**
**Cross-cluster duplicate kills:** A-0047 (overlaps B-0350), A-0162 (overlaps B-0274 and a Cluster C rare-class-CI survivor), A-0211 (overlaps B-0255 + RClicks).

Notation: each entry lists Closest Prior Works (real papers found in search), what that work actually did, our exact difference, remaining novelty, a novelty-confidence judgment, reviewer-likely attack papers, decision, and reason.

---

## Sub-cluster: SAM prompt sensitivity

### A-0002 — Positional-encoding aliasing as the cause of point-prompt instability
- **Decision:** KEEP
- **Closest Prior Works:**
  1. Stable Segment Anything Model — Fan et al., 2023, arXiv:2311.15776 — https://arxiv.org/abs/2311.15776
  2. TETRIS: Towards Exploring the Robustness of Interactive Segmentation — Moskalenko et al., 2024, arXiv:2402.06132 — https://arxiv.org/abs/2402.06132
- **Existing Work Actually Did:** Stable-SAM documents SAM's mask instability under low-quality/shifted prompts and attributes it to attention drift toward background, fixing it with deformable attention offsets. TETRIS finds worst-case (adversarial) click positions inside the object and shows large quality swings, providing robustness benchmarking of click position.
- **Our Exact Difference:** Neither work tests whether the *spatial structure* of instability is periodic and aligned with the prompt encoder's positional-embedding frequency grid, nor tests an anti-aliased positional re-encoding as a causal intervention. Prior work locates the failure in decoder attention; we test a competing, falsifiable encoder-side mechanism.
- **Remaining Novelty:** Fourier analysis of sub-pixel click-flip maps against the PE grid period + causal low-pass PE retraining. A mechanism identification, not another robustness benchmark.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** Stable-SAM (claims attention, not encoding, is the cause); TETRIS/RClicks-style robustness benchmarks ("instability already characterized").
- **Reason (survival):** The aliasing mechanism and the anti-aliasing intervention are absent from all found prior work; the experiment cleanly separates the two candidate mechanisms.

### A-0003 — Prompt-order sensitivity of multi-click prompting
- **Decision:** KEEP
- **Closest Prior Works:**
  1. TETRIS — Moskalenko et al., 2024, arXiv:2402.06132 (click-position robustness, fixed simulated order)
  2. SAM — Kirillov et al., 2023, ICCV, arXiv:2304.02643 (iterative mask-conditioned prompting protocol)
- **Existing Work Actually Did:** Interactive-segmentation evaluation protocols (SAM's iterative training, standard NoC metrics) fix a single simulated click order; robustness work perturbs click *positions*, not click *orders*.
- **Our Exact Difference:** Holding the click *set* fixed and permuting *order*, measuring IoU spread, and ablating the inter-step low-res mask prior as the mediating mechanism. SEARCH NOTE: no paper found that measures order-invariance of promptable segmenters.
- **Remaining Novelty:** Order-invariance as a measurable property + mediation analysis via the mask prior; direct implication for benchmark validity of interactive protocols.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** Interactive segmentation protocol papers (RITM/SimpleClick evaluation conventions) claiming order is standardized so irrelevant; TETRIS (worst-case clicks subsume order effects).
- **Reason (survival):** Cheap, clean, unexamined invariance question with a specific mechanistic mediator to test.

### A-0005 — Negative-click over-erosion law for thin structures
- **Decision:** KILL
- **Closest Prior Works:**
  1. Quantifying the Limits of Segmentation Foundation Models: Modeling Challenges in Segmenting Tree-Like and Low-Contrast Objects — Wei et al., 2024, arXiv:2412.04243 — https://arxiv.org/html/2412.04243
  2. DIS-SAM / Promoting SAM towards Highly Accurate Dichotomous Image Segmentation — 2024 (arXiv HTML 2401.0248)
  3. HQ-SAM: Segment Anything in High Quality — Ke et al., NeurIPS 2023, arXiv:2306.01567
- **Existing Work Actually Did:** Quantified SFM failures on thin/tree-like structures with dedicated difficulty measures (DoGD, tree-likeness), showed the failures persist for HQ-SAM/SAM2 and resist decoder fine-tuning; DIS/ThinObject benchmarks quantify thin-structure quality; HQ-SAM addresses the low-res mask pathway.
- **Our Exact Difference:** Prior work is zero-shot / positive-prompt; the negative-click erosion-vs-local-width law tied to the 256×256 mask-prior resolution is not measured anywhere we found.
- **Remaining Novelty:** The erosion law itself — but thin-structure failure of the SAM mask pathway is already established as resolution-linked by the above works, so the delta is a second-order refinement.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** arXiv:2412.04243 (thin-structure failure already quantified and shown fine-tuning-resistant); HQ-SAM (resolution pathway already indicted and fixed).
- **Reason (elimination):** Core resolution-bottleneck claim already established; cluster already represented by A-0002/A-0003; remaining delta too incremental to survive the quota.

---

## Sub-cluster: SAM2 video memory

### A-0016 — Forgetting curve of SAM2's memory bank (decay law vs. slot eviction)
- **Decision:** KEEP
- **Closest Prior Works:**
  1. SAM2Long: Enhancing SAM 2 for Long Video Segmentation with a Training-Free Memory Tree — Ding et al., 2024, arXiv:2410.16268 — https://arxiv.org/abs/2410.16268
  2. SAMURAI: Adapting SAM for Zero-Shot Visual Tracking with Motion-Aware Memory — Yang et al., 2024, arXiv:2411.11922
- **Existing Work Actually Did:** SAM2Long documents error accumulation ("error propagation") in SAM2's greedy memory and fixes it with a memory tree; SAMURAI/DAM4SAM replace or filter memory entries heuristically. All are *method* papers with end-to-end metrics.
- **Our Exact Difference:** No work measures the functional form of re-ID decay vs. occlusion duration (exponential interference vs. step-like slot eviction) or aligns failures with logged memory-bank contents. This is a mechanism decomposition, not another memory fix.
- **Remaining Novelty:** Parametric occlusion-length sweeps + eviction-aligned failure analysis → distinguishes "better features" from "better scheduling".
- **Novelty Confidence:** medium-high
- **Reviewer-Likely Attack Papers:** SAM2Long, SAMURAI, DAM4SAM ("we already fixed memory") — rebuttal: they fix without characterizing; our decay law explains *when* their fixes matter.
- **Reason (survival):** Clean mechanistic decomposition absent from a method-dominated literature.

### A-0017 — "Identity capture": stale memories causally block recovery
- **Decision:** MUTATE
- **Closest Prior Works:**
  1. SAMURAI — Yang et al., 2024, arXiv:2411.11922
  2. DAM4SAM: A Distractor-Aware Memory for Visual Object Tracking with SAM2 — Videnovic et al., 2024/CVPR 2025, arXiv:2411.17576
- **Existing Work Actually Did:** Both identify distractor lock-in in SAM2's memory (appearance-similarity confusion) and *prevent* it via motion-aware selection (SAMURAI) or distractor-aware memory management (DAM4SAM), reporting end-to-end tracking gains.
- **Our Exact Difference:** They prevent; nobody performs *post-hoc causal surgery* — deleting specific post-error memory entries at ground-truth reappearance and measuring recovery rate — which quantifies how much of failure is memory-borne vs. representational.
- **Remaining Novelty:** Causal memory-editing intervention with a recovery-rate estimate; positions memory editing as a deployment-time repair primitive.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** SAMURAI, DAM4SAM ("phenomenon known, engineering solutions exist").
- **Mutated One-Liner:** *Causal memory surgery for SAM2: measure how much of organic tracking failure is reversible by targeted deletion of post-error memory entries, giving an upper bound that prevention methods (SAMURAI/DAM4SAM) can be scored against.*
- **New Hypothesis:** On ≥200 organic SAM2 failures, oracle-timed deletion of post-error entries restores tracking in >60% of cases, and the reversible fraction predicts (r>0.6) the gain achievable by distractor-aware memory methods per sequence — establishing memory-editing recovery as an upper-bound diagnostic.
- **Reason (survival via mutation):** Reframed from "discover the phenomenon" (done) to "quantify the causal, reversible share and turn it into an upper-bound diagnostic" (not done).

### A-0024 — Twin-object crossover identity test
- **Decision:** KILL
- **Closest Prior Works:**
  1. SAMURAI — Yang et al., 2024, arXiv:2411.11922
  2. DAM4SAM — Videnovic et al., 2024, arXiv:2411.17576
- **Existing Work Actually Did:** SAMURAI's stated motivation is precisely that SAM2 "neglects motion cues" and confuses appearance-similar objects in crowded scenes; both papers demonstrate and mitigate appearance-tie identity failures.
- **Our Exact Difference:** Only the synthetic twin/crossover parametrization (crossing angle/speed) remains.
- **Remaining Novelty:** A parametric psychophysics curve for a failure that is already demonstrated and mechanistically attributed (appearance-only memory, no motion integration).
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** SAMURAI (explicitly documents the appearance-based memory limitation and adds motion), MOT crossover stress-test literature.
- **Reason (elimination):** The headline conclusion ("SAM2 memory is appearance-based, no motion continuity") is already published as the premise of fix papers.

### A-0030 — Did SAM2's video training damage still-image ability vs. SAM1?
- **Decision:** KILL
- **Closest Prior Works:**
  1. Is SAM 2 Better than SAM in Medical Image Segmentation? — Sengupta, Chakrabarty, Soni, 2024, arXiv:2408.04212
  2. Quantifying the Limits of Segmentation Foundation Models — 2024, arXiv:2412.04243 (evaluates SAM, SAM2, HQ-SAM on identical still-image failure suites)
- **Existing Work Actually Did:** Sengupta et al. directly compare SAM vs SAM2 on 2D still (medical) images and find SAM2 frequently *worse*, especially in low-contrast regimes. arXiv:2412.04243 evaluates SAM/SAM2 side-by-side on tree-like/low-contrast still images and shows shared and regressed failure regimes.
- **Our Exact Difference:** Stratification by boundary frequency/object density on natural images plus a spectral-smoothing mechanism correlation.
- **Remaining Novelty:** Attribution to "temporal objectives" is confounded (architecture/data changed simultaneously) — acknowledged in the idea itself; the regression phenomenon is already documented.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Sengupta et al. 2024; arXiv:2412.04243.
- **Reason (elimination):** Headline finding published; the remaining stratified analysis cannot cleanly isolate its claimed cause.

---

## Sub-cluster: SAM3 concept prompting

### A-0031 — Relation-defined vs attribute-defined concept prompts
- **Decision:** KILL
- **Closest Prior Works:**
  1. SAM 3: Segment Anything with Concepts — Meta AI, 2025 (SA-Co benchmark; noun-phrase concept prompts, explicitly scoped to short noun phrases and hard negatives)
  2. Referring Expressions as a Lens into Spatial Language Grounding in Vision-Language Models — IJCNLP 2025 — https://aclanthology.org/2025.ijcnlp-long.183.pdf
  3. Mastering Negation: Boosting Grounding Models via Grouped Opposition-Based Learning — 2026, arXiv:2603.12606 (qualifier comprehension incl. spatial position)
- **Existing Work Actually Did:** SAM3 explicitly scopes concept prompting to simple noun phrases and reports failure on complex referring expressions; the IJCNLP study stratifies grounding failures by spatial-relation type across models; GOBL documents qualifier (incl. spatial) comprehension failures.
- **Our Exact Difference:** Matched-visual-difficulty attribute-vs-relation pairs on concept-promptable segmenters specifically.
- **Remaining Novelty:** Thin — the relation-vs-attribute failure asymmetry is already documented in adjacent grounding literature; only the matched-difficulty construction is new, and the idea itself flags that construction as the main risk.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** SAM3 paper (states the scope limitation directly); spatial-grounding-lens studies.
- **Reason (elimination):** Expected result already stated as a known limitation by the model's own paper.

### A-0032 — Exhaustivity failure: misses concentrate far from concept prototype
- **Decision:** KEEP
- **Closest Prior Works:**
  1. SAM 3 (SA-Co) — Meta AI, 2025 (measures instance-level recall for concept prompts, incl. hard negatives)
  2. LVIS: A Dataset for Large Vocabulary Instance Segmentation — Gupta et al., CVPR 2019 (exhaustive annotation protocol)
- **Existing Work Actually Did:** SA-Co measures *how much* is missed under concept prompts; LVIS provides exhaustivity infrastructure. Neither analyzes the *structure* of misses in the model's own embedding space.
- **Our Exact Difference:** Prototype-distance analysis of hits vs. misses (effect size, multivariate controls for size/occlusion) → a priori predictability of misses.
- **Remaining Novelty:** Predictable-miss model enabling targeted verification and honest recall bounds for auto-annotation corpora. SEARCH NOTE: no paper found doing instance-level miss-structure analysis for concept segmentation.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** SA-Co benchmark ("recall already measured"); long-tail recognition papers (prototype-distance effects known for classification).
- **Reason (survival):** The predictability claim (miss structure, not miss rate) is a precise, isolatable remainder.

### A-0034 — Negative-concept prompting ("all animals except dogs")
- **Decision:** KILL
- **Closest Prior Works:**
  1. SAM 3 — Meta AI, 2025 (SA-Co includes negative prompts / rejection of absent concepts; presence head)
  2. Know "No" Better: A Data-Driven Approach for Enhancing Negation Awareness in CLIP — Park et al., ICCV 2025, arXiv:2501.10913 (NegRefCOCOg)
  3. Vision-Language Models Do Not Understand Negation (NegBench) — Alhamoud et al., 2025, arXiv:2501.09425
  4. Mastering Negation (GOBL) — 2026, arXiv:2603.12606
- **Existing Work Actually Did:** Negation benchmarks for VLM/segmentation exist (NegRefCOCOg on referring segmentation; NegBench across tasks); SAM3 trains and evaluates hard negatives and a presence head; GOBL improves grounding under negation and measures absence handling.
- **Our Exact Difference:** Boolean set-algebra framing ("positive minus subtraction" baselines) only.
- **Remaining Novelty:** Marginal — the core empirical claim (concept heads lack compositional negation) is already established.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** NegRefCOCOg; NegBench; SAM3.
- **Reason (elimination):** Directly covered by an active negation-benchmark literature.

---

## Sub-cluster: MedSAM domain shift

### A-0047 — MedSAM cannot reject wrong boxes
- **Decision:** KILL (merged into A-0134 mutation; cross-cluster duplicate)
- **Closest Prior Works:**
  1. Segment Anything Model for Medical Images? — Huang et al., Medical Image Analysis 2024, arXiv:2304.14660 (large-scale prompt-perturbation evaluation incl. box jitter)
  2. SAM 3 — 2025 (presence head explicitly for "concept absent" rejection)
- **Existing Work Actually Did:** Large-scale MedSAM/SAM medical evaluations already perturb boxes and document confident segmentation of wrong regions; SAM3 introduces a trained presence/rejection signal at concept level.
- **Our Exact Difference:** Rejection-competency framing with radiologist plausibility rating.
- **Remaining Novelty:** Subsumed by the emptiness/rejection-calibration idea (A-0134 mutation), which covers wrong-box rejection as one condition. Also overlaps Cluster B survivor B-0350 (per cross-cluster check).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Huang et al. 2024; SAM3 presence head.
- **Reason (elimination):** Duplicate of A-0134's mutated scope + partially covered by box-perturbation studies + cross-cluster overlap (B-0350).

### A-0051 — MedSAM inherits institutional annotation styles
- **Decision:** KILL
- **Closest Prior Works:**
  1. Large-scale interactive object segmentation with human annotators — Benenson et al., CVPR 2019 (annotation-guideline/style effects on masks at scale)
  2. ValUES: A Framework for Systematic Validation of Uncertainty Estimation in Semantic Segmentation — Kahl et al., ICLR 2024 (inter-rater variation as measurable signal)
  3. Observer-variability / contouring-style literature in radiotherapy (multiple systematic reviews)
- **Existing Work Actually Did:** Established that annotation styles/guidelines measurably shape masks; medical inter-observer variability is heavily quantified; cross-cohort generalization failures of medical models are documented.
- **Our Exact Difference:** A style-classifier probe attributing MedSAM boundary placement to the majority training institution.
- **Remaining Novelty:** Real but fragile: requires datasets with known institutional provenance (rare), and the conclusion ("models average toward training-majority style") is the expected consequence of ERM — low surprise.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Benenson et al.; inter-observer variability literature ("style variance known; inheritance is unsurprising").
- **Reason (elimination):** Low-surprise expected result + data-availability blocker; loses quota competition.

### A-0053 — Pathology breaks shape priors: hallucinating healthy anatomy
- **Decision:** KILL
- **Closest Prior Works:**
  1. HALOS: Hallucination-free Organ Segmentation after Organ Resection Surgery — Rickmann et al., 2023, arXiv:2303.07717
  2. Automated Audit and Self-Correction Algorithm for Seg-Hallucination — Bioengineering 2025, doi:10.3390/bioengineering12010081
  3. Atlas-Based Under-Segmentation — MICCAI/PMC4219918 (systematic atlas-prior bias)
- **Existing Work Actually Did:** HALOS demonstrates exactly the hypothesized failure — models hallucinate resected organs in post-surgical scans — and builds a fix; "Seg-Hallucination" literature names, audits, and corrects prior-driven hallucination; atlas-bias is quantified.
- **Our Exact Difference:** Doing it on MedSAM specifically with anomalous-region error decomposition.
- **Remaining Novelty:** Model-swap increment on an established phenomenon.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** HALOS; seg-hallucination audit literature.
- **Reason (elimination):** Phenomenon demonstrated, named, and being fixed.

---

## Sub-cluster: Boundary quality

### A-0061 — Boundary Nyquist limit: spectral cutoff set by decoder resolution
- **Decision:** KEEP
- **Closest Prior Works:**
  1. FourierLoss: Shape-Aware Loss Function with Fourier Descriptors — 2023, arXiv:2309.12106
  2. Configurable synthetic segmentation errors via Fourier descriptors (MISS-tool) — 2022, arXiv:2212.14828
  3. Boundary IoU: Improving Object-Centric Image Segmentation Evaluation — Cheng et al., CVPR 2021, arXiv:2103.16562
- **Existing Work Actually Did:** Fourier descriptors are used as loss functions and error simulators; Boundary IoU measures boundary error scalar-wise. Nobody measures *where in contour-frequency space* model error concentrates, nor ties a cutoff to decoder feature-map resolution across models.
- **Our Exact Difference:** Error-energy-vs-curvature-frequency spectra across decoders of different resolutions; testing predictability of the cutoff from architecture ("boundary Nyquist constant").
- **Remaining Novelty:** An architectural constant converting "coarse boundaries" into a measurable, design-guiding quantity. SEARCH NOTE: no direct hit found.
- **Novelty Confidence:** medium-high
- **Reviewer-Likely Attack Papers:** FourierLoss (same math, different purpose); HQ-SAM (already fixed low-res pathway empirically).
- **Reason (survival):** Precise, cheap, model-comparative law; distinct from loss-design uses of the same tools.

### A-0062 — HQ-boundary gains vs. soft multi-annotator ground truth
- **Decision:** KEEP
- **Closest Prior Works:**
  1. HQ-SAM — Ke et al., NeurIPS 2023, arXiv:2306.01567
  2. Boundary IoU — Cheng et al., CVPR 2021 (checks metric consistency on only two annotators)
  3. Metrics Reloaded — Maier-Hein et al., Nature Methods 2024 (recommends NSD to absorb annotation imprecision)
- **Existing Work Actually Did:** HQ methods report gains against single hard GT; Boundary IoU's annotator-consistency check is minimal (n=2); Metrics Reloaded acknowledges boundary-annotation imprecision and offers tolerance-based metrics but never re-evaluates HQ-style methods against multi-annotator soft references.
- **Our Exact Difference:** Re-scoring SAM vs HQ-SAM (and successors) against 5-annotator soft boundaries; quantifying gain shrinkage = metric-gaming share.
- **Remaining Novelty:** Whether a visible fraction of "high-quality boundary" progress is an artifact of hard-label evaluation. SEARCH NOTE: no such re-evaluation found.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** Metrics Reloaded ("use NSD and the problem disappears"); HQ-SAM rebuttal ("visual quality obviously better").
- **Reason (survival):** Direct validity audit of a celebrated improvement line; experiments isolate the claim.

### A-0068 — Latent alpha-matte information in binary-trained logits
- **Decision:** MUTATE
- **Closest Prior Works:**
  1. Matting Anything (MAM) — Li et al., 2023, arXiv:2306.05399
  2. Matte Anything — Yao et al., 2023, arXiv:2306.04121
- **Existing Work Actually Did:** Both attach *trained* matting modules/pipelines to SAM and show SAM features/masks support matting after training — proving usable signal exists, but through learned readouts.
- **Our Exact Difference:** Training-free, definitional test: rank-correlate raw SAM logits with true alpha in translucent regions, controlling for trivial distance-to-boundary effects, plus boundary-placement variance analysis on translucency.
- **Remaining Novelty:** Whether alpha information is present in the *output logits themselves* (recoverable for free) vs. created by trained matting heads.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** MAM/Matte Anything ("matting from SAM already works").
- **Mutated One-Liner:** *A training-free audit of binary-trained mask logits against ground-truth alpha mattes: how much matting information do promptable models give away for free, and where does the forced hard boundary land on translucent matter?*
- **New Hypothesis:** After partialling out distance-to-boundary, SAM logit values retain significant rank correlation (ρ>0.3) with true alpha in translucent regions, and hard-boundary placement variance on translucent regions exceeds opaque regions by >5×, quantifying both the free signal and the representational cost of binary supervision.
- **Reason (survival via mutation):** Distinguishes latent-information measurement from trained-matting engineering, which prior work conflates.

### A-0073 — Instance-instance boundaries weaker than instance-background at matched contrast
- **Decision:** KILL
- **Closest Prior Works:**
  1. Semantic instance segmentation with discriminative deep supervision for medical images — (touching-boundary sub-network; explicitly states adjacent boundaries are "usually poorly learned")
  2. Structure-Preserving Instance Segmentation via Skeleton-Aware Distance Transform — 2023, arXiv:2310.05262
  3. Cell Instance Segmentation: The Devil Is in the Boundaries (Ceb) — 2025, arXiv:2510.09848
- **Existing Work Actually Did:** A whole methods literature exists because instance-instance (touching) boundaries are known to be systematically harder; papers state it, build specialized supervision/representations for it, and measure it in domain benchmarks.
- **Our Exact Difference:** Only the contrast-matched, boundary-type-conditional metric decomposition remains.
- **Remaining Novelty:** A tidier measurement of an accepted fact; the "gap survives fine-tuning" claim mirrors what arXiv:2412.04243 already showed for thin structures.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Ceb 2025 (title literally is the finding); SDT.
- **Reason (elimination):** Phenomenon is the founding premise of an existing methods subfield.

### A-0074 — Wiener deconvolution of decoder blur (training-free boundary recovery)
- **Decision:** KILL
- **Closest Prior Works:**
  1. SAMRefiner: Taming SAM for Universal Mask Refinement — Lin et al., ICLR 2025, arXiv:2502.06756
  2. ReGRAF: Training-free Prompt Refinement via Gradient Flow — OpenReview ZvPPLeVuhT
  3. CascadePSP / CRF-based post-processing (classical training-free refinement line)
- **Existing Work Actually Did:** Multiple training-free/label-free mask refinement routes exist (prompt mining, gradient flow, CRFs); they already harvest most of the post-hoc boundary headroom.
- **Our Exact Difference:** Treating the decoder as an estimable linear degradation operator (PSF) and inverting it.
- **Remaining Novelty:** The linear-PSF assumption is almost certainly false (input-dependent, nonlinear blur — the idea's own stated risk), and even if it worked, it competes in a crowded refinement market on the same metric.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** SAMRefiner (stronger training-free refinement, ICLR 2025); CascadePSP.
- **Reason (elimination):** Fragile core assumption + saturated task; method-shaped rather than science-shaped.

---

## Sub-cluster: Mobile distillation

### A-0078 — Do students inherit teacher click-fragility maps?
- **Decision:** KEEP
- **Closest Prior Works:**
  1. MobileSAM (decoupled distillation) — Zhang et al., 2023, arXiv:2306.14289
  2. EfficientSAM — Xiong et al., CVPR 2024
  3. Born-Again Neural Networks — Furlanello et al., ICML 2018, arXiv:1805.04770
- **Existing Work Actually Did:** Distillation papers report aggregate metric retention; born-again work shows students can beat teachers in classification. SEARCH NOTE: no work found measuring *failure-mode inheritance* (spatial fragility-map correlation teacher↔student vs. independently trained controls) for segmentation.
- **Our Exact Difference:** Correlation structure of click-fragility maps across teacher / distilled students / independent controls, with shared-data confound explicitly controlled.
- **Remaining Novelty:** Pathology inheritance as a measurable property of the distillation signal; enables selective pathology filtering.
- **Novelty Confidence:** medium-high
- **Reviewer-Likely Attack Papers:** Dataset-similarity explanations (shared training data explains correlation) — must be controlled, as the idea acknowledges.
- **Reason (survival):** Unmeasured, cheap with existing checkpoints (MobileSAM/EfficientSAM/SAM), clear falsifiable correlation structure.

### A-0080 — "Resolution honesty" spec for efficient SAM variants
- **Decision:** KILL
- **Closest Prior Works:**
  1. Quantifying the Limits of Segmentation Foundation Models — 2024, arXiv:2412.04243
  2. EfficientSAM — Xiong et al., CVPR 2024 (reports AP_S size-stratified results)
  3. DIS-5K / ThinObject-5K benchmarks (fine-structure quality quantification)
- **Existing Work Actually Did:** Thin/fine-structure failures of efficient and full SFMs are quantified with dedicated difficulty measures and size-stratified metrics; the gap between input resolution and effective detail is repeatedly demonstrated.
- **Our Exact Difference:** A psychophysics-style synthetic threshold ("minimum resolvable gap") spec.
- **Remaining Novelty:** A repackaging of documented failures into a new unit; the idea's own risk (synthetic thresholds may not transfer) undercuts the spec's value.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** arXiv:2412.04243 (already provides difficulty-parametrized quantification).
- **Reason (elimination):** Measurement-branding delta over established quantifications.

### A-0084 — Efficient attention damages long-range mask coherence
- **Decision:** KILL
- **Closest Prior Works:**
  1. Bridging the Divide: Reconsidering Softmax and Linear Attention — Han et al., NeurIPS 2024, arXiv:2412.06590
  2. Rectifying Magnitude Neglect in Linear Attention (MALA) — Fan et al., ICCV 2025
  3. Breaking the Low-Rank Dilemma of Linear Attention (RALA) — Fan et al., CVPR 2025
- **Existing Work Actually Did:** The linear-attention performance gap has been mechanistically dissected: non-injectivity (semantic confusion), *local* modeling deficits, magnitude neglect, low-rank outputs — with segmentation benchmarks. Crucially, the diagnosis is that linear attention fails at *local* modeling, not long-range reach.
- **Our Exact Difference:** Object-spatial-extent-stratified fragmentation analysis.
- **Remaining Novelty:** The premise (efficiency truncates long-range interactions → extended-object fragmentation) is contradicted by the found mechanistic literature; any residual effect would be re-attributed to the known causes.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Bridging the Divide (shows the binding deficit is local modeling, opposite of the hypothesis).
- **Reason (elimination):** Hypothesis mechanism already investigated and pointed the other way.

### A-0087 — Regimes where distilled students beat the teacher
- **Decision:** KILL
- **Closest Prior Works:**
  1. Born-Again Neural Networks — Furlanello et al., ICML 2018, arXiv:1805.04770
  2. MobileSAM/EfficientSAM evaluations (report per-dataset cases where students approach/exceed teacher on subsets)
- **Existing Work Actually Did:** Student>teacher effects are established in classification (born-again); efficiency papers' tables already contain subset-level reversals nobody deeply mined.
- **Our Exact Difference:** Regime characterization + image-statistics win predictor for segmentation.
- **Remaining Novelty:** The idea's own main risk (wins may be sparse noise) is likely: SAM-class students trail teachers by clear margins on nearly all reported strata, so stable win-regimes are improbable.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Born-Again Networks ("known effect"); EfficientSAM tables ("gap is uniform").
- **Reason (elimination):** Known effect + high null-result risk; loses quota competition.

---

## Sub-cluster: PEFT mechanics

### A-0092 — LoRA rank set by intrinsic dimension of the domain shift
- **Decision:** KILL
- **Closest Prior Works:**
  1. GeLoRA: Geometric Adaptive Ranks for Efficient LoRA Fine-tuning — 2024, arXiv:2412.09250
  2. AdaLoRA: Adaptive Budget Allocation for PEFT — Zhang et al., ICLR 2023, arXiv:2303.10512
  3. Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning — Aghajanyan et al., ACL 2021
- **Existing Work Actually Did:** GeLoRA derives rank from intrinsic dimensionality of hidden representations; AdaLoRA adaptively allocates rank; Aghajanyan established the intrinsic-dimension ↔ fine-tuning connection.
- **Our Exact Difference:** Controlled-dimensionality *domain shifts* in vision rather than task datasets.
- **Remaining Novelty:** Marginal instantiation; the rank↔intrinsic-dimension law is the founding claim of existing methods.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** GeLoRA; Aghajanyan et al.
- **Reason (elimination):** Directly anticipated by existing rank-selection theory/methods.

### A-0093 — Adapter interference predicted by principal angles
- **Decision:** KILL
- **Closest Prior Works:**
  1. Editing Models with Task Arithmetic — Ilharco et al., ICLR 2023, arXiv:2212.04089
  2. TIES-Merging: Resolving Interference When Merging Models — Yadav et al., NeurIPS 2023, arXiv:2306.01708
  3. Recent LoRA-merge compatibility analyses (subspace-overlap predictors of merging success; multiple 2024-25 papers surfaced in search)
- **Existing Work Actually Did:** Model/adapter merging interference is an established field; TIES identifies sign/subspace interference as the failure cause; newer work explicitly predicts mergeability from update-geometry statistics.
- **Our Exact Difference:** Vision-adapter instantiation of an already-proposed geometric compatibility test.
- **Remaining Novelty:** None that survives; the weight-vs-activation-geometry caveat is also already raised in merging literature.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** TIES-Merging; task-arithmetic line.
- **Reason (elimination):** Pre-merge geometric compatibility prediction already exists.

### A-0094 — Prompt-encoder-only fine-tuning suffices for many domain shifts
- **Decision:** KILL
- **Closest Prior Works:**
  1. How to build the best medical image segmentation algorithm using foundation models — Gu et al., 2024, arXiv:2404.09957 (systematic component-choice study)
  2. Medical SAM3 ablations — 2026 (partial fine-tuning of decoder+prompt encoder yields only ~64% Dice; holistic adaptation needed)
  3. SAM-DA: Decoder Adapter for Efficient Medical Domain Adaptation — 2025, arXiv:2501.06836
- **Existing Work Actually Did:** Component-wise fine-tuning attribution for SAM in domain shift is already systematically studied (decoder-only, decoder+encoder, PEFT variants); recent ablations show prompt-path-only adaptation is insufficient for meaningful shifts.
- **Our Exact Difference:** An 8-domain attribution table.
- **Remaining Novelty:** The core hypothesis is already contradicted for the domains it targets (medical).
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** arXiv:2404.09957; Medical SAM3 ablation.
- **Reason (elimination):** Question asked and answered in the negative by existing ablation studies.

### A-0100 — Transporting LoRA adapters across backbone scales
- **Decision:** KILL
- **Closest Prior Works:**
  1. LoRA-X: Bridging Foundation Models with Training-Free Cross-Model Adaptation — ICLR 2025, arXiv:2501.16559
  2. Cross-LoRA (training-free LoRA transfer across heterogeneous backbones) — 2025 (found in search)
- **Existing Work Actually Did:** Training-free transfer of LoRA updates across different (including differently-sized) backbones via subspace alignment — the exact mechanism proposed.
- **Our Exact Difference:** None material (ViT-B→ViT-L for segmentation is an instantiation).
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** LoRA-X; Cross-LoRA.
- **Reason (elimination):** Direct prior art.

### A-0104 — PEFT cannot inject inductive biases (scale equivariance)
- **Decision:** KILL
- **Closest Prior Works:**
  1. Equi-Tuning: Group Equivariant Fine-Tuning of Pretrained Models — Basu et al., AAAI 2023, arXiv:2210.06475
  2. Efficient Equivariant Transfer Learning from Pretrained Models (λ-equitune) — Basu et al., NeurIPS 2023
  3. Equivariant adapters for diffusion/vision models (GeoAda-type, surfaced in search)
- **Existing Work Actually Did:** Parameter-efficient *equivariant* adaptation modules already inject group equivariance into pretrained models — directly undermining the "reachability boundary" framing, since tiny equivariant modules are themselves PEFT.
- **Our Exact Difference:** Restricting the claim to *low-rank linear* update families only.
- **Remaining Novelty:** A negative result about one PEFT sub-family whose practical import is void (the field already routes around it with equivariant adapters).
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Equi-tuning line ("PEFT does inject biases").
- **Reason (elimination):** Framed boundary already crossed by existing methods.

---

## Sub-cluster: PEFT forgetting

### A-0107 — Forgetting under PEFT is a readout (decoder) phenomenon, recoverable by decoder reset
- **Decision:** KEEP
- **Closest Prior Works:**
  1. Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution — Kumar et al., ICLR 2022, arXiv:2202.10054 — https://arxiv.org/abs/2202.10054
  2. LoRA Learns Less and Forgets Less — Biderman et al., TMLR 2024, arXiv:2405.09673
  3. Continual Alignment for SAM (CA-SAM) — Wang et al., CVPR 2026 — https://openaccess.thecvf.com/content/CVPR2026F/papers/Wang_Continual_Alignment_for_SAM__Rethinking_Foundation_Models_for_Medical_CVPRF_2026_paper.pdf
  4. SAMed-2: Selective Memory Enhanced Medical SAM — 2025, arXiv:2507.03698
- **Existing Work Actually Did:** Kumar et al. established the feature-distortion vs. head account of fine-tuning damage for classification (LP-FT). LoRA-forgetting work measures how much is lost, not where. SAM continual-learning papers (CA-SAM, SAMed-2, PSF-SAM) document zero-shot erosion after SAM fine-tuning and *prevent* it with routing/memory machinery — none decompose where the erosion lives.
- **Our Exact Difference:** A four-way {original, tuned} × {encoder-adapters, decoder} swap matrix for promptable segmentation, quantifying the recoverable-by-decoder-reset fraction of forgetting. Classification's LP-FT result does not transfer trivially because SAM's decoder is a prompt-conditioned transformer, not a linear head.
- **Remaining Novelty:** The recovery matrix + the deployment implication (dual-decoder serving kills forgetting without continual-learning machinery). SEARCH NOTE: no component-swap forgetting decomposition found for promptable models.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** Kumar et al. ("known for classification"); CA-SAM ("we already preserve zero-shot"). Rebuttal: neither measures the readout share; CA-SAM's machinery may be unnecessary if the effect is decoder-local. Partial-overlap note: a Cluster C survivor locates VLM forgetting in embedding/unembedding drift — different model class, different component, complementary.
- **Reason (survival):** Cheap (existing checkpoints + swaps), decision-relevant, and the co-adaptation risk is itself a measurable outcome.

### A-0113 — Vision-tower PEFT silently damages text-vision alignment
- **Decision:** KILL
- **Closest Prior Works:**
  1. Robust Fine-Tuning of Zero-Shot Models (WiSE-FT) — Wortsman et al., CVPR 2022, arXiv:2109.01903
  2. Investigating the Catastrophic Forgetting in Multimodal Large Language Models — Zhai et al., 2023, arXiv:2309.10313
  3. Anchor-based robust fine-tuning line for CLIP (multiple 2023-24 papers)
- **Existing Work Actually Did:** Fine-tuning CLIP-style models is known to damage zero-shot/multimodal alignment even when target-task vision metrics improve; MLLM fine-tuning studies document multimodal capability forgetting with per-task probes; anchor/ensemble methods exist to preserve alignment.
- **Our Exact Difference:** Segmentation-specific adaptation + late-block update-norm localization.
- **Remaining Novelty:** Marginal — the headline phenomenon (vision-side tuning degrades multimodal alignment invisible to vision-only metrics) is the founding observation of the robust-fine-tuning literature.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** WiSE-FT; MLLM forgetting studies.
- **Reason (elimination):** Phenomenon established; only the task instantiation remains.

### A-0119 — Dormant capability revival: forgetting as suppression, not erasure
- **Decision:** KILL
- **Closest Prior Works:**
  1. Understanding Catastrophic Forgetting in Language Models via Implicit Inference — Kotha et al., ICLR 2024, arXiv:2309.10105
  2. LoRA Learns Less and Forgets Less — Biderman et al., TMLR 2024, arXiv:2405.09673
- **Existing Work Actually Did:** Kotha et al. showed "forgotten" LM capabilities are recoverable by prompting/conditioning (task inference shifted, capability intact) — the exact suppression-vs-erasure result, in language. LoRA-forgetting work shows low-rank updates preserve most capability.
- **Our Exact Difference:** Vision instantiation with prompt-space search over click/box patterns.
- **Remaining Novelty:** An instantiation whose mechanism-level conclusion is already published; per-case prompt search also risks overfitting noise (idea's own risk). Overlaps kept idea A-0107 (which tests the same suppression question with a cleaner intervention — decoder reset).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Kotha et al. ("suppression already shown"); A-0107-style component analyses.
- **Reason (elimination):** Redundant with kept A-0107, which answers the same question with a stronger, cheaper intervention.

### A-0120 — Population-level forgetting law from community checkpoints
- **Decision:** KILL
- **Closest Prior Works:**
  1. Model Zoos: A Dataset of Diverse Populations of Neural Network Models — Schürholt et al., NeurIPS 2022 Datasets & Benchmarks
  2. LoRA Learns Less and Forgets Less — Biderman et al., 2024 (forgetting vs. update-strength relationships)
- **Existing Work Actually Did:** Model-zoo/weight-space analysis established populations of checkpoints as an observational resource and predicts model properties from weights; forgetting-vs-update-norm relationships are measured in controlled settings.
- **Our Exact Difference:** Observational meta-analysis over uncontrolled community SAM fine-tunes.
- **Remaining Novelty:** The idea's own risk is fatal: community checkpoints have unknown data/recipe provenance, so the fitted "law" cannot separate domain distance from recipe variation — an uncontrollable confound, not a fixable nuisance.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Model Zoos line ("do it controlled or not at all"); any controlled forgetting study.
- **Reason (elimination):** Methodologically unsound as science; controlled versions already exist.

---

## Sub-cluster: Calibration & uncertainty

### A-0128 — Confidence inflation under iterative clicking
- **Decision:** MUTATE
- **Closest Prior Works:**
  1. On Calibrating Semantic Segmentation Models — Wang et al., NeurIPS 2023, arXiv:2212.12053
  2. Conformal Prediction Sets for Instance Segmentation — 2026, arXiv:2602.10045 (states SAM's predicted IoUs carry no calibration guarantee)
  3. SAM — Kirillov et al., 2023 (IoU-prediction head, trained on actual IoU)
- **Existing Work Actually Did:** Segmentation calibration is studied per-prediction (static); conformal work wraps SAM outputs with guarantees but treats the model as fixed; nobody audits how SAM's self-reported confidence *evolves along an interaction trajectory* relative to true IoU.
- **Our Exact Difference:** Trajectory-conditioned calibration: regress predicted and true IoU on click index; test whether inflation rate is a stable model constant; derive corrected stopping rules.
- **Remaining Novelty:** Interaction-indexed miscalibration as a distinct pathology breaking stopping criteria — absent from static calibration and conformal literatures.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** Static SAM-calibration audits ("miscalibration already known"); RClicks ("scripted clicks unrealistic").
- **Mutated One-Liner:** *Trajectory calibration of promptable models: does self-reported mask confidence inflate with interaction count independent of accuracy, and is the inflation a correctable model constant that repairs interactive stopping rules?*
- **New Hypothesis:** On ≥2k objects under RClicks-realistic simulated sessions, predicted-IoU inflation beyond true-IoU gain is positive after accuracy plateaus in >40% of objects; a single per-model linear correction of click-indexed confidence reduces wasted clicks (post-plateau interactions) by >30% at equal final quality.
- **Reason (survival via mutation):** Repositioned from "SAM is miscalibrated" (known) to "miscalibration is interaction-trajectory-structured and fixable at the stopping-rule level" (unmeasured); uses RClicks to defuse the simulation-realism attack.

### A-0132 — Do "aleatoric" estimators actually predict annotator ambiguity?
- **Decision:** KILL
- **Closest Prior Works:**
  1. ValUES: A Framework for Systematic Validation of Uncertainty Estimation in Semantic Segmentation — Kahl et al., ICLR 2024 — https://openreview.net/forum?id=yV6fD7LYkF
  2. A Probabilistic U-Net for Segmentation of Ambiguous Images — Kohl et al., NeurIPS 2018, arXiv:1806.05034
- **Existing Work Actually Did:** ValUES is nearly the exact study: it systematically tests whether uncertainty methods capture what they claim (aleatoric vs. epistemic separation), using multi-rater segmentation data and downstream tasks. The Prob-U-Net line evaluates against annotator distributions (GED) by construction.
- **Our Exact Difference:** Training an entropy-supervised estimator and testing cross-model transfer.
- **Remaining Novelty:** A follow-on experiment inside an existing validation framework, not a new question.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** ValUES (definitional validation already built and run).
- **Reason (elimination):** Core "category mistake" audit already published at ICLR 2024.

### A-0134 — Calibration of "emptiness": prompts that hit nothing
- **Decision:** MUTATE (absorbs A-0047)
- **Closest Prior Works:**
  1. SAM 3 — Meta AI, 2025 (presence head: trained concept-absence rejection, concept prompts only)
  2. Segment Anything Model for Medical Images? — Huang et al., Medical Image Analysis 2024, arXiv:2304.14660 (box-perturbation evaluations show confident wrong masks)
  3. Conformal Prediction Sets for Instance Segmentation — 2026, arXiv:2602.10045
- **Existing Work Actually Did:** SAM3 adds a presence/rejection signal for *text concepts*; medical evaluations document that geometric prompts on empty/wrong regions yield confident garbage; conformal methods bound mask error but assume an object is there.
- **Our Exact Difference:** A systematic emptiness benchmark across *geometric* prompt types (background clicks, texture boxes, wrong-organ boxes) measuring null-detection AUROC of existing signals (predicted IoU, stability score, logit statistics), plus a trained null-token head — quantifying the architectural absence-blindness of the entire SAM-1/2 deployment base.
- **Remaining Novelty:** Geometric-prompt rejection calibration; SAM3's presence head covers only concept prompts and is not available to point/box pipelines.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** SAM3 ("presence solved it" — only for text prompts); Huang et al. ("wrong-box failure known" — but not calibrated/benchmarked as rejection competence).
- **Mutated One-Liner:** *The absence option: benchmark and repair the inability of point/box-promptable segmenters to say "nothing is here," measured as null-detection AUROC across empty-prompt families and fixed with a trained null token.*
- **New Hypothesis:** Existing SAM signals achieve <0.75 AUROC for emptiness detection across empty-prompt families; a null-token fine-tune reaches >0.9 AUROC while preserving mask quality, raising auto-annotation precision at fixed recall by a measurable margin on SA-1B-style pipelines.
- **Reason (survival via mutation):** Merged with A-0047's wrong-box condition into one rejection-competence study; the geometric-prompt scope isolates it from SAM3's concept-level presence head. Cross-cluster note: B-0350 covers medical rejection; this entry is deliberately scoped to natural-image auto-annotation to avoid the duplicate.

---

## Sub-cluster: Small & thin objects

### A-0136 — Token-occupancy law: failure begins below 1 ViT token
- **Decision:** KEEP
- **Closest Prior Works:**
  1. Segmenter — Strudel et al., ICCV 2021, arXiv:2105.05633 (smaller patch → better segmentation, aggregate)
  2. SOHES — ICLR 2024, arXiv:2404.12386 (ablation: patch size 32→8 strongly improves mask quality; resolution matters less)
  3. FlexiViT: One Model for All Patch Sizes — Beyer et al., CVPR 2023, arXiv:2212.08013
  4. Quantifying the Limits of Segmentation Foundation Models — 2024, arXiv:2412.04243 (pixel-area-based difficulty)
- **Existing Work Actually Did:** Patch-size ablations show aggregate quality improves with smaller patches; small-object failure is quantified by pixel area. Nobody varies input resolution to *decouple token occupancy from pixel count* and test whether collapse is pinned to the <1-token threshold.
- **Our Exact Difference:** Same physical objects evaluated across resolutions spanning the 1-token boundary; quality plotted against token occupancy vs. pixel area as competing predictors.
- **Remaining Novelty:** A mechanistic unit (tokens, not pixels) for small-object failure, directly testable and architecture-predictive. SEARCH NOTE: no resolution-decoupled occupancy analysis found.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** SOHES/Segmenter ablations ("patch size effect known" — but confounded with compute and never object-aligned); FlexiViT ("patch-size flexibility exists" — a tool, not the analysis).
- **Reason (survival):** Cheap, sharply falsifiable (collapse either aligns with the token threshold or it doesn't), redirects small-object work toward tokenization.

### A-0137 — Small-object information survives the encoder, dies in the decoder
- **Decision:** KILL
- **Closest Prior Works:**
  1. Understanding Intermediate Layers Using Linear Classifier Probes — Alain & Bengio, 2016, arXiv:1610.01644 (probing methodology)
  2. HQ-SAM — Ke et al., NeurIPS 2023, arXiv:2306.01567 (already exploits early/high-res encoder features to fix decoder-lost detail)
  3. Quantifying the Limits of Segmentation Foundation Models — arXiv:2412.04243
- **Existing Work Actually Did:** HQ-SAM's entire mechanism is the premise of this idea: recoverable fine detail exists in encoder features that the standard decoder discards, and a small learned readout recovers it. Probing methodology is standard.
- **Our Exact Difference:** Reporting recoverable fractions by size bin instead of shipping the fix.
- **Remaining Novelty:** The qualitative conclusion is already implied by HQ-SAM's success; a Cluster C survivor also relocates long-tail failure from representation to readout with the same probe logic — cross-cluster methodological duplicate.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** HQ-SAM ("we built the readout; information presence is demonstrated").
- **Reason (elimination):** Premise already operationalized by a famous method; kept A-0136 covers the mechanistic remainder in this sub-cluster.

### A-0142 — Does context help or hurt small objects? Inpainting ablations
- **Decision:** KILL
- **Closest Prior Works:**
  1. Noise or Signal: The Role of Image Backgrounds in Object Recognition — Xiao et al., ICLR 2021, arXiv:2006.09994
  2. The Elephant in the Room — Rosenfeld et al., 2018, arXiv:1808.03305
- **Existing Work Actually Did:** Background/context ablation methodology and its conclusions (context can help or hurt; models over-rely on backgrounds) are established for recognition and detection; context-swap and removal protocols are standard.
- **Our Exact Difference:** Size-conditioned sign reversal for segmentation with attention-mass tracking.
- **Remaining Novelty:** A refinement (non-monotonicity in size) on an established methodology, with inpainting artifacts as a serious confound (idea's own risk).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Xiao et al. ("context ablation done"); inpainting-artifact critiques.
- **Reason (elimination):** Delta too small over established context-ablation science; loses quota competition.

### A-0146 — Packing-density phase transition for dense instances
- **Decision:** KILL
- **Closest Prior Works:**
  1. Cellpose — Stringer et al., Nature Methods 2021 (dense-instance segmentation regimes measured across densities)
  2. Cell Instance Segmentation: The Devil Is in the Boundaries — 2025, arXiv:2510.09848
  3. Quantifying the Limits of Segmentation Foundation Models — arXiv:2412.04243
- **Existing Work Actually Did:** Dense-instance domains (cytology, crowds) quantify separation failure vs. density routinely; resolution-linked failure of SFMs on fine structure is established.
- **Our Exact Difference:** Claiming a *discontinuous* transition with resolution-scaled critical point.
- **Remaining Novelty:** The phase-transition framing is likely a re-description of a steep sigmoid; distinguishing "sharp" from "discontinuous" at feasible sample sizes is statistically fraught, and the practical conclusion (density limits scale with resolution) is already the field's working assumption.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Cellpose-line density analyses; arXiv:2412.04243.
- **Reason (elimination):** Framing novelty without decision-changing content; kept A-0136 owns this sub-cluster's mechanism slot.

---

## Sub-cluster: Evaluation weakness

### A-0151 — Has mIoU steered the field? Longitudinal re-ranking under rebalanced metrics
- **Decision:** KILL
- **Closest Prior Works:**
  1. Boundary IoU — Cheng et al., CVPR 2021, arXiv:2103.16562 (shows model rankings change under boundary-sensitive metrics — the core result)
  2. Metrics Reloaded — Maier-Hein et al., Nature Methods 2024
  3. Do ImageNet Classifiers Generalize to ImageNet? — Recht et al., ICML 2019, arXiv:1902.10811 (longitudinal re-evaluation methodology)
- **Existing Work Actually Did:** Boundary IoU already demonstrated that mIoU hides boundary progress and re-ranked methods; Metrics Reloaded systematizes metric-induced blind spots; longitudinal re-evaluation frameworks exist.
- **Our Exact Difference:** A 5-year, 12-model trend analysis under composite metrics.
- **Remaining Novelty:** Scaling up an existing demonstration; composite-metric design subjectivity (idea's own risk) invites endless reviewer relitigation.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Boundary IoU; Metrics Reloaded.
- **Reason (elimination):** Core finding (metric-hidden capability axes) already published; kept A-0062 covers the sharper validity question in this space.

### A-0152 — Benchmark saturation vs. label-noise floor
- **Decision:** KILL
- **Closest Prior Works:**
  1. Pervasive Label Errors in Test Sets Destabilize ML Benchmarks — Northcutt et al., NeurIPS 2021 D&B, arXiv:2103.14749
  2. Are we done with ImageNet? — Beyer et al., 2020, arXiv:2006.07159
  3. Metrics Reloaded — Maier-Hein et al., 2024 (annotation imprecision handling)
- **Existing Work Actually Did:** Label errors shown to destabilize top-model rankings at scale; re-annotation studies quantified ceiling effects; for segmentation, multi-annotator variance is quantified in medical benchmarks.
- **Our Exact Difference:** Annotation-bootstrap significance testing for segmentation leaderboards specifically.
- **Remaining Novelty:** Real but thin, and it substantially overlaps kept idea A-0062 (multi-annotator re-scoring of boundary progress) plus a Cluster C survivor (rare-class confidence intervals span mIoU points).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Northcutt et al.; Beyer et al.
- **Reason (elimination):** Method established in classification; segmentation instantiation split across existing survivors (A-0062, C-cluster CI idea).

### A-0154 — Test-set contamination via annotation-style regurgitation
- **Decision:** KILL
- **Closest Prior Works:**
  1. Time Travel in LLMs: Tracing Data Contamination — Golchin & Surdeanu, ICLR 2024, arXiv:2308.08493 (behavioral contamination detection without training-data access)
  2. Membership Inference Attacks — Shokri et al., IEEE S&P 2017
  3. SAM — Kirillov et al., 2023 (SA-1B pipeline documentation enabling style analysis)
- **Existing Work Actually Did:** Behavioral (no-training-data-access) contamination detection is an active LLM subfield with mature protocols; membership inference gives the statistical foundations.
- **Our Exact Difference:** Segmentation-specific style-fingerprint statistics.
- **Remaining Novelty:** The style-fingerprint machinery is shared with kept idea A-0271 (pipeline-fingerprint inheritance), which tests a cleaner causal claim on controlled data; the contamination version suffers the style-convergence confound (idea's own risk) with no clean control.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** LLM contamination-detection line ("method ported, weaker identification").
- **Reason (elimination):** Confounded variant of kept A-0271; one fingerprint idea survives, the cleaner one.

### A-0162 — Statistical power audit of segmentation evaluation
- **Decision:** KILL (cross-cluster duplicate)
- **Closest Prior Works:**
  1. With Little Power Comes Great Responsibility — Card et al., EMNLP 2020, arXiv:2010.06595 (field-wide power audit, NLP)
  2. Accounting for Variance in Machine Learning Benchmarks — Bouthillier et al., MLSys 2021, arXiv:2103.03098
- **Existing Work Actually Did:** Card et al. ran exactly this audit for NLP (minimum detectable effects vs. published deltas); Bouthillier et al. quantified benchmark variance sources and detectability for vision/ML broadly.
- **Our Exact Difference:** Segmentation-benchmark instantiation.
- **Remaining Novelty:** The instantiation is real but is *already claimed twice within this project*: Cluster B survivor B-0274 (power analysis of long-tail benchmarks) and a Cluster C survivor (rare-class confidence intervals) cover the same methodology and headline message.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Card et al. ("template exists"); internal duplication with B-0274.
- **Reason (elimination):** Cross-cluster duplicate — B-0274 and the C-cluster CI idea own this space; keeping a third variant wastes a slot.

---

## Sub-cluster: Representation mismatch

### A-0167 — Pixelwise unique-information maps for SAM vs. CLIP features
- **Decision:** KILL
- **Closest Prior Works:**
  1. SAM-CLIP: Merging Vision Foundation Models — Wang et al., 2023, arXiv:2310.15308
  2. What Do Self-Supervised Vision Transformers Learn? — Park et al., ICLR 2023, arXiv:2305.00729 (systematic property comparison across pretrainings)
- **Existing Work Actually Did:** SAM-CLIP merges the two models and characterizes their complementary strengths (spatial vs. semantic) to build a fused model; comparative representation analyses across pretraining objectives quantify property differences.
- **Our Exact Difference:** Per-pixel unique-information decomposition instead of model-level fusion metrics.
- **Remaining Novelty:** Probe-capacity dependence (idea's own risk) makes "unique information" ill-defined in practice; the qualitative conclusion (semantic vs. geometric complementarity) is already established by the fusion line.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** SAM-CLIP ("complementarity established and exploited").
- **Reason (elimination):** Expected-result refinement of a known complementarity; measurement is probe-fragile.

### A-0169 — Object-centric attention vs. local smoothness: which makes DINO segmentation-friendly?
- **Decision:** KILL
- **Closest Prior Works:**
  1. What Do Self-Supervised Vision Transformers Learn? — Park et al., ICLR 2023, arXiv:2305.00729
  2. Emerging Properties in Self-Supervised Vision Transformers (DINO) — Caron et al., ICCV 2021, arXiv:2104.14294
  3. Vision Transformers Need Registers — Darcet et al., ICLR 2024, arXiv:2309.16588 (smoothness/artifact structure directly manipulated, dense gains measured)
- **Existing Work Actually Did:** Comparative analyses already dissociate self-supervised feature properties (attention structure, locality, smoothness) across objectives and link them to downstream dense performance; registers work causally manipulates feature smoothness and measures dense-task effects.
- **Our Exact Difference:** A distillation-based dissociation of two specific properties.
- **Remaining Novelty:** The idea's own risk (clean dissociation may be technically infeasible) is the crux: smoothness-preserving distillation that provably removes object-centric attention has no accepted construction, making the causal claim unfalsifiable in practice.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Park et al.; Darcet et al.
- **Reason (elimination):** Attribution question partially answered; proposed instrument unbuildable to referee standard.

### A-0175 — Camera-metadata shortcut channel in frozen VFM features
- **Decision:** KILL
- **Closest Prior Works:**
  1. Confounding variables can degrade generalization of radiology deep-learning models — Zech et al., PLOS Medicine 2018 (hospital/scanner signatures exploited as shortcuts)
  2. Shortcut Learning in Deep Neural Networks — Geirhos et al., Nature Machine Intelligence 2020, arXiv:2004.07780
  3. PRNU-based camera-source forensics literature (device fingerprints decodable from images)
- **Existing Work Actually Did:** Scanner/device signatures are decodable and demonstrably exploited as shortcuts by downstream heads (Zech et al. is the canonical demonstration); shortcut-learning theory generalizes the account; forensics proves device fingerprints survive in image statistics.
- **Our Exact Difference:** Measuring the strength of the channel in *frozen VFM features* specifically.
- **Remaining Novelty:** A strength measurement of an established channel; metadata-rich datasets are scarce (idea's own risk).
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Zech et al.; Geirhos et al.
- **Reason (elimination):** Phenomenon, mechanism, and harm all documented; only the feature-space venue changes.

### A-0178 — Artifact/high-norm tokens cause prompt-localized failures in promptable segmentation
- **Decision:** KEEP
- **Closest Prior Works:**
  1. Vision Transformers Need Registers — Darcet et al., ICLR 2024 (Oral), arXiv:2309.16588 — https://arxiv.org/abs/2309.16588
  2. Vision Transformers Don't Need Trained Registers — 2025, arXiv:2506.08010 (test-time register retrofitting)
- **Existing Work Actually Did:** Registers work identified high-norm artifact tokens, showed they discard local patch information, and improved *aggregate* dense metrics by adding registers; follow-ups retrofit registers without retraining. All evidence is representation-level or aggregate-benchmark-level.
- **Our Exact Difference:** Causal, prompt-conditioned tracing: compare failure rates for clicks landing on vs. off artifact patches (location-matched controls), then show register retrofitting removes the excess — a user-visible, task-level causal chain from a known anomaly.
- **Remaining Novelty:** The representation-anomaly → prompt-failure link; also yields a practical "prompt-hazard map" for interactive tools. SEARCH NOTE: no work found connecting artifact tokens to promptable-segmentation failures.
- **Novelty Confidence:** medium-high
- **Reviewer-Likely Attack Papers:** Darcet et al. ("registers already fix dense tasks" — aggregate, not prompt-causal); background-correlation confound critics (must match locations, as idea acknowledges).
- **Reason (survival):** Precise causal remainder with a built-in intervention (retrofit) and clean controls; connects interpretability to product failure.

---

## Sub-cluster: Detection failures

### A-0181 — DETR query territories predict crowded-region misses
- **Decision:** KILL
- **Closest Prior Works:**
  1. End-to-End Object Detection with Transformers (DETR) — Carion et al., ECCV 2020, arXiv:2005.12872 (visualizes per-query spatial/size specialization — "territories" — in the paper itself)
  2. DAB-DETR: Dynamic Anchor Boxes are Better Queries — Liu et al., ICLR 2022, arXiv:2201.12329 (queries as spatial anchors, formalizing territorial structure)
- **Existing Work Actually Did:** Query spatial specialization is shown in the original DETR paper and formalized by the anchor-query line; crowded-scene misses of query detectors are documented in dense-detection benchmarks (CrowdHuman analyses).
- **Our Exact Difference:** Regressing regional miss rates on count/slot-density ratios.
- **Remaining Novelty:** A quantitative dressing of a documented phenomenon; modern deformable/denoising variants blur territories (idea's own risk), dating the result on arrival.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** DETR (Fig. 7-style query plots); DAB-DETR.
- **Reason (elimination):** Territory structure is in the original paper; capacity account adds little.

### A-0183 — Background-prior contamination of open-vocabulary detection
- **Decision:** KILL
- **Closest Prior Works:**
  1. The Elephant in the Room — Rosenfeld et al., 2018, arXiv:1808.03305 (context/location priors dominate detection)
  2. Noise or Signal (backgrounds) — Xiao et al., ICLR 2021, arXiv:2006.09994
  3. Open-vocabulary detection base-class bias analyses (ViLD line, Gu et al., ICLR 2022, arXiv:2104.13921)
- **Existing Work Actually Did:** Location/context priors as detection failure causes are established; open-vocab work documents base-class bias in novel-class recall.
- **Our Exact Difference:** Spatial background-prior stratification specifically.
- **Remaining Novelty:** Appearance-location covariance (idea's own risk) requires synthetic placement controls that reintroduce composite artifacts — the same trap that killed A-0200's methodology; the qualitative conclusion is anticipated by context-prior literature.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Rosenfeld et al.; ViLD-line bias analyses.
- **Reason (elimination):** Anticipated result, confound-heavy design.

### A-0191 — Long-tail failure as a naming problem in open-vocab detection
- **Decision:** KILL
- **Closest Prior Works:**
  1. TIDE: A General Toolbox for Identifying Object Detection Errors — Bolya et al., ECCV 2020, arXiv:2008.08115 (classification-vs-localization error decomposition)
  2. Evaluating Large-Vocabulary Object Detectors: The Devil is in the Details — Dave et al., 2021, arXiv:2102.01066
- **Existing Work Actually Did:** Error decompositions separating "found but misclassified" from "missed" exist as standard tooling (TIDE) and have been applied to large-vocabulary settings (LVIS analysis line), including tail-class error profiling.
- **Our Exact Difference:** Paradigm comparison (open-vocab vs. closed-set) of the naming-vs-miss ratio.
- **Remaining Novelty:** Running existing tools on newer models — an evaluation report, not a new question.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** TIDE; Dave et al.
- **Reason (elimination):** Decomposition machinery and tail-error analyses already exist.

### A-0194 — Annotation-convention translator bounds cross-dataset AP loss
- **Decision:** KILL
- **Closest Prior Works:**
  1. Unbiased Look at Dataset Bias — Torralba & Efros, CVPR 2011 (cross-dataset gaps include annotation-convention components)
  2. TIDE — Bolya et al., ECCV 2020 (error attribution incl. box-quality conventions)
- **Existing Work Actually Did:** Dataset-bias work established that cross-dataset drops mix capability with convention mismatch; detection error toolkits attribute box-level discrepancies.
- **Our Exact Difference:** A learned box-transform translator as an upper-bound estimator.
- **Remaining Novelty:** The translator absorbs genuine localization correction (idea's own fatal risk), making the "convention share" unidentifiable — the estimate cannot support its headline claim.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Torralba & Efros; identifiability critics.
- **Reason (elimination):** Known phenomenon + unidentifiable estimator.

---

## Sub-cluster: Scaling & emergence

### A-0196 — Capability-resolved scaling exponents for segmentation
- **Decision:** KILL
- **Closest Prior Works:**
  1. Scaling Vision Transformers — Zhai et al., CVPR 2022, arXiv:2106.04560
  2. Quantifying the Limits of Segmentation Foundation Models — arXiv:2412.04243 (shows specific capabilities resist scale/fine-tuning)
- **Existing Work Actually Did:** Vision scaling laws exist at aggregate level; capability-resistance to scale is already demonstrated qualitatively for thin/low-contrast structures across SAM ladders.
- **Our Exact Difference:** Fitting per-capability exponents with uncertainty.
- **Remaining Novelty:** Public model ladders confound size with data/recipe (idea's own risk), so fitted "exponents" are not interpretable as scaling laws; the actionable conclusion (some failures won't scale away) is already published.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** arXiv:2412.04243; scaling-law methodology critics.
- **Reason (elimination):** Headline conclusion pre-empted; quantitative version unidentifiable on public ladders.

### A-0198 — Emergence vs. metric artifact in prompt composition
- **Decision:** KILL
- **Closest Prior Works:**
  1. Are Emergent Abilities of Large Language Models a Mirage? — Schaeffer et al., NeurIPS 2023, arXiv:2304.15004
- **Existing Work Actually Did:** Established precisely the continuous-vs-thresholded-metric account of emergence, with the recipe (swap metrics, watch discontinuities vanish) this idea proposes to run in vision.
- **Our Exact Difference:** Vision instantiation on prompt-composition suites.
- **Remaining Novelty:** Running a published analysis template in a new domain where sparse scale ladders (idea's own risk) cannot resolve curve shape anyway.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Schaeffer et al.
- **Reason (elimination):** Direct template port; expected answer already known.

### A-0200 — Inverse scaling in vision: priors override pixel evidence
- **Decision:** KILL
- **Closest Prior Works:**
  1. Inverse Scaling: When Bigger Isn't Better — McKenzie et al., TMLR 2023, arXiv:2306.09479
  2. The Elephant in the Room — Rosenfeld et al., 2018 (prior-violating scenes break detectors)
  3. ImageNet-D — CVPR 2024, arXiv:2403.18775 (diffusion-generated hard cases degrade many models)
- **Existing Work Actually Did:** The inverse-scaling program exists (language); prior-violation failures in vision are documented; synthetic hard-case generation pipelines exist.
- **Our Exact Difference:** Systematic scale-monotonicity testing for vision behaviors.
- **Remaining Novelty:** Composite/generation artifacts (idea's own risk) confound "prior override" with distribution shift; scale ladders again confound size with data. Two unidentifiabilities stacked.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** McKenzie et al. ("program exists"); ImageNet-D ("hard-case generation exists").
- **Reason (elimination):** Program template + failure phenomenon both published; clean attribution infeasible.

---

## Sub-cluster: Interactive loop

### A-0211 — Within-session human co-adaptation contaminates interactive benchmarks
- **Decision:** KILL (cross-cluster duplicate)
- **Closest Prior Works:**
  1. RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation — Antonov et al., NeurIPS 2024 D&B, arXiv:2410.11722 (475K real-user clicks incl. multi-round interactions; shows simulators mis-rank methods)
  2. TETRIS — Moskalenko et al., 2024, arXiv:2402.06132
- **Existing Work Actually Did:** RClicks collected large-scale *multi-round* real-user click data, built a clickability model, and demonstrated that static simulation misestimates real-world performance and robustness — covering most of the claimed gap.
- **Our Exact Difference:** Explicit longitudinal drift (strategy learning) analysis within sessions.
- **Remaining Novelty:** Thin residual over RClicks' real-click data; small-n user studies (idea's own risk) are underpowered for drift detection. Cluster B survivor B-0255 (simulated-vs-real user gap + calibrated user models) already owns this exact territory.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** RClicks; B-0255 duplication.
- **Reason (elimination):** Cross-cluster duplicate of B-0255, and RClicks pre-empts the headline.

### A-0221 — Annotation authority: novice deference to model confidence
- **Decision:** KILL
- **Closest Prior Works:**
  1. Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance — Bansal et al., CHI 2021
  2. Effect of Confidence and Explanation on Accuracy and Trust Calibration in AI-Assisted Decision Making — Zhang et al., FAT* 2020, arXiv:2001.02114
  3. To Trust or to Think — Buçinca et al., CSCW 2021
- **Existing Work Actually Did:** Over-reliance on confident wrong AI suggestions, under-reliance on unconfident correct ones, and net quality degradation regimes are core, replicated findings of the human-AI decision-making literature, including with confidence displays.
- **Our Exact Difference:** Segmentation-annotation instantiation.
- **Remaining Novelty:** Task port of a mature HCI result; ethical-design overhead (idea's own risk) for a predictable outcome.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Bansal et al.; Zhang et al.
- **Reason (elimination):** Established phenomenon in the adjacent field that owns the methodology.

---

## Sub-cluster: Ambiguity & multi-hypothesis

### A-0226 — Ambiguity taxonomy + does 3-mask output cover the ambiguity distribution?
- **Decision:** KILL
- **Closest Prior Works:**
  1. A Probabilistic U-Net for Segmentation of Ambiguous Images — Kohl et al., NeurIPS 2018, arXiv:1806.05034 (distribution-valued ambiguity handling + multi-annotator evaluation)
  2. Semantic-SAM: Segment and Recognize Anything at Any Granularity — Li et al., 2023, arXiv:2307.04767 (many-granularity outputs beyond 3)
  3. GraCo: Granularity-Controllable Interactive Segmentation — CVPR 2024
- **Existing Work Actually Did:** Ambiguity-as-distribution is a modeled and evaluated concept (Prob-U-Net line, GED metrics); granularity ambiguity specifically has dedicated architectures with more/controllable hypothesis budgets, implicitly conceding 3 slots truncate.
- **Our Exact Difference:** Empirical cardinality measurement of interpretation counts.
- **Remaining Novelty:** Annotator enumeration incompleteness (idea's own risk) caps the claim; the architecture-relevant conclusion (3 is not enough; budget should be input-adaptive) is already embodied in successor architectures. Kept A-0227 tests the sharper, cheaper question in this cluster.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Semantic-SAM ("we already output more granularities"); Prob-U-Net line.
- **Reason (elimination):** Conclusion pre-conceded by existing architectures; loses to A-0227 for the cluster slot.

### A-0227 — Is SAM's multimask diversity calibrated to input ambiguity, or a fixed template?
- **Decision:** KEEP
- **Closest Prior Works:**
  1. Flaws can be Applause: Unleashing Potential of Segmenting Ambiguous Objects in SAM (A-SAM) — NeurIPS 2024 — https://papers.nips.cc/paper_files/paper/2024/hash/50ee6db59fca8643dc625829d4a0eab9-Abstract.html
  2. A Probabilistic U-Net — Kohl et al., NeurIPS 2018, arXiv:1806.05034
  3. SAM — Kirillov et al., 2023 (subpart/part/whole design intent)
- **Existing Work Actually Did:** A-SAM *replaces* SAM's ambiguity handling with a CVAE to match ambiguous label distributions — implicitly assuming vanilla SAM's spread is inadequate but never measuring its calibration; Prob-U-Net line evaluates distribution match for its own models, not for SAM's fixed 3-slot output; the template hypothesis (spread is an input-independent part/whole signature) is untested.
- **Our Exact Difference:** A diversity-calibration audit of the deployed model class: correlate inter-hypothesis spread with human-interpretation entropy; test cross-image template similarity of the hypothesis structure.
- **Remaining Novelty:** Whether downstream uses of multimask spread as uncertainty (common in pipelines) are valid — a validity result independent of any fix. SEARCH NOTE: no calibration audit of SAM's multimask diversity found.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** A-SAM ("we already improved ambiguity handling" — a fix, not an audit); IoU-based diversity metric critics (idea acknowledges).
- **Reason (survival):** Cheap, decision-relevant audit with a crisp falsifiable template hypothesis; complements rather than duplicates the method line.

### A-0237 — Any-valid-interpretation scoring changes model rankings
- **Decision:** KILL
- **Closest Prior Works:**
  1. Prob-U-Net / LIDC-IDRI evaluation protocols — Kohl et al., 2018 (GED against annotator sets = multi-interpretation scoring)
  2. Metrics Reloaded — Maier-Hein et al., 2024
- **Existing Work Actually Did:** Scoring against sets/distributions of annotations (GED, hungarian-matched multi-rater metrics) is established in ambiguity-aware evaluation; medical benchmarks already use multi-rater references.
- **Our Exact Difference:** Benchmark-scale re-ranking of general models.
- **Remaining Novelty:** Enumeration cost/incompleteness (idea's own risk) + overlap with kept A-0062 (soft multi-annotator re-scoring) and kept A-0227 (interpretation-space coverage). Third variant of one theme.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** GED-protocol line; Metrics Reloaded.
- **Reason (elimination):** Methodology exists; theme already represented twice among survivors.

---

## Sub-cluster: Robustness & shift

### A-0242 — Interaction-recoverable vs. unrecoverable corruption robustness
- **Decision:** KILL
- **Closest Prior Works:**
  1. Robustness of SAM: Segment Anything Under Corruptions and Beyond — Qiao et al., 2023, arXiv:2306.07713
  2. RClicks — Antonov et al., NeurIPS 2024 (realism limits of simulated correction loops)
- **Existing Work Actually Did:** SAM corruption robustness is benchmarked across corruption types/severities; interactive evaluation methodology (NoC metrics) is standard; RClicks shows simulated clickers misestimate real interactive performance.
- **Our Exact Difference:** Clicks-to-recover as the robustness metric + representation-vs-readout mechanism probes.
- **Remaining Novelty:** Real but sits on two shaky legs: the recoverability split depends on simulated-clicker realism (undermined by RClicks) and the mechanism probe duplicates kept A-0107's readout-vs-representation machinery in a noisier setting.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Qiao et al. ("corruption robustness measured"); RClicks (simulation validity).
- **Reason (elimination):** Quota competition: mechanism slot already held by A-0107; measurement leg unreliable.

### A-0243 — Adversarial prompts and certified prompt-robustness radii
- **Decision:** KILL
- **Closest Prior Works:**
  1. TETRIS: Towards Exploring the Robustness of Interactive Segmentation — Moskalenko et al., 2024, arXiv:2402.06132 (adversarial in-object click search — the exact attack)
  2. Attack-SAM — Zhang et al., 2023, arXiv:2305.00866 (adversarial examples against SAM)
  3. Certified Adversarial Robustness via Randomized Smoothing — Cohen et al., ICML 2019, arXiv:1902.02918
- **Existing Work Actually Did:** TETRIS already computes worst-case click placements and documents large worst-vs-average gaps; SAM attack papers cover the adversarial channel; certification machinery exists generically.
- **Our Exact Difference:** Lipschitz certification over the prompt encoder.
- **Remaining Novelty:** Certified radii will be vacuous (idea's own risk) because mask flips occur at sub-pixel prompt shifts (established by kept A-0002's aliasing phenomenon); the empirical half is TETRIS.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** TETRIS; Attack-SAM.
- **Reason (elimination):** Empirical part done; theoretical part predictably vacuous.

---

## Sub-cluster: Open-vocab grounding

### A-0256 — Linguistic-construct-resolved referring failures and their scaling
- **Decision:** KILL
- **Closest Prior Works:**
  1. Referring Expressions as a Lens into Spatial Language Grounding in VLMs — IJCNLP 2025
  2. Vision-Language Models Do Not Understand Negation (NegBench) — Alhamoud et al., 2025, arXiv:2501.09425
  3. When and Why VLMs Behave like Bags-of-Words — Yuksekgonul et al., ICLR 2023, arXiv:2210.01936
- **Existing Work Actually Did:** Construct-stratified grounding failure analysis exists (spatial relations, negation, compositional order), with documented scale-resistance for several constructs.
- **Our Exact Difference:** Matched-visual-difficulty construction + scaling curves for referring *segmentation* specifically.
- **Remaining Novelty:** Same matched-difficulty fragility that killed A-0031; construct-specific failures and their scale behavior are already mapped in adjacent grounding tasks.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** NegBench; bags-of-words line.
- **Reason (elimination):** Failure taxonomy already published across constructs; segmentation port is incremental.

### A-0257 — Reporting-bias inheritance in grounded segmentation
- **Decision:** KILL
- **Closest Prior Works:**
  1. Seeing through the Human Reporting Bias — Misra et al., CVPR 2016, arXiv:1512.06974
  2. LVIS long-tail analyses — Gupta et al., 2019 onward (frequency-capability correlations)
- **Existing Work Actually Did:** Reporting bias (what people mention vs. what is visible) was named, measured, and modeled for visual concepts a decade ago; frequency-performance correlations are standard long-tail findings.
- **Our Exact Difference:** Partial-correlation attribution (text mention rate beyond visual frequency) for segmentation grounding.
- **Remaining Novelty:** Corpus statistics only approximate actual training text (idea's own risk), weakening the causal reading; the qualitative conclusion is anticipated by Misra et al.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Misra et al.; training-corpus-proxy critics.
- **Reason (elimination):** Core concept published; attribution identification weak.

### A-0262 — Attribute-object binding failures in dense grounding
- **Decision:** KILL
- **Closest Prior Works:**
  1. Winoground — Thrush et al., CVPR 2022, arXiv:2204.03162
  2. When and Why VLMs Behave like Bags-of-Words (ARO) — Yuksekgonul et al., ICLR 2023, arXiv:2210.01936
- **Existing Work Actually Did:** Compositional binding failure in VLMs is heavily benchmarked (attribute-object swaps, relational binding), with similarity-based retrieval accounts already advanced as the mechanism.
- **Our Exact Difference:** Dense-output (mask-localized) version with distractor-structure parametrics.
- **Remaining Novelty:** The mask output does add observability, but the mechanism conclusion (retrieval-based confusion growing with attribute sharing) is the published account; scene-construction bias (idea's own risk) invites the same critiques Winoground successors face.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** ARO/Winoground line ("binding failures established; your curves confirm our account").
- **Reason (elimination):** Confirmatory instantiation of a published mechanism; quota.

---

## Sub-cluster: Data-centric bias

### A-0271 — SA-1B pipeline fingerprints and their inheritance by trained models
- **Decision:** KEEP
- **Closest Prior Works:**
  1. Segment Anything — Kirillov et al., ICCV 2023, arXiv:2304.02643 (documents the filter stack that would *create* the fingerprint: predicted-IoU ≥ 0.88, stability thresholding, NMS, size filters)
  2. Large-scale interactive object segmentation with human annotators — Benenson et al., CVPR 2019 (annotation-process effects on mask statistics)
  3. AI models collapse when trained on recursively generated data — Shumailov et al., Nature 2024 (generation-recursion risk, language/generative setting)
- **Existing Work Actually Did:** The SAM paper documents (but does not analyze distributionally) an aggressive model-in-the-loop filter stack; annotation-process effects on masks are known; recursive-training degradation is established in generative modeling. Nobody has measured SA-1B's mask-statistic divergence from human datasets as a *generator signature*, nor tested whether models trained on it reproduce the signature on new images.
- **Our Exact Difference:** Fingerprint definition (curvature spectra, complexity ceilings, stability-filter survivals) + controlled matched-model training on assisted vs. manual data + signature-reproduction test.
- **Remaining Novelty:** First quantitative inheritance measurement for the auto-labeling era's flagship dataset; the mechanism (filter-induced selection bias) is documented but its downstream imprint is unmeasured. SEARCH NOTE: no SA-1B fingerprint/inheritance analysis found.
- **Novelty Confidence:** medium-high
- **Reviewer-Likely Attack Papers:** Model-collapse literature ("recursion risk known" — in generative modeling, without segmentation-specific fingerprints); content-confound critics (matched-content controls required, as idea acknowledges).
- **Reason (survival):** Precise, feasible (SA-1B is public), and foundational for the data-centric cluster; absorbs the honest parts of A-0154/A-0366/A-0367.

### A-0272 — Model-collapse dynamics for segmentation self-training
- **Decision:** KILL
- **Closest Prior Works:**
  1. AI models collapse when trained on recursively generated data — Shumailov et al., Nature 2024
  2. Self-Consuming Generative Models Go MAD — Alemohammad et al., ICLR 2024, arXiv:2307.01850
  3. Is Model Collapse Inevitable? — Gerstgrasser et al., 2024, arXiv:2404.01413 (data accumulation/human injection arrests collapse)
- **Existing Work Actually Did:** Collapse dynamics, degradation ordering (tails/diversity first), rate dependence on synthetic fraction, and the arresting effect of real-data injection are all established across generative and supervised recursion settings.
- **Our Exact Difference:** Dense-prediction property tracking (boundaries, rare morphologies).
- **Remaining Novelty:** The specific predictions (tails degrade first, human data arrests) are direct transfers of published findings; multi-generation segmentation training is expensive (idea's own risk) for a confirmatory answer.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Shumailov et al.; Gerstgrasser et al.
- **Reason (elimination):** All headline claims pre-published in adjacent settings; kept A-0271 covers the segmentation-specific data-loop risk with a sharper instrument.

### A-0275 — Marginal value of human labels by data stratum
- **Decision:** KILL
- **Closest Prior Works:**
  1. Active Learning Literature Survey — Settles, 2009 (value-targeted labeling is the field's core business)
  2. Segment Anything — Kirillov et al., 2023 (data engine: empirical human-vs-model label allocation at scale)
- **Existing Work Actually Did:** Active learning formalizes where human labels have marginal value (disagreement/uncertainty targeting included); SAM's own data engine is a worked example of stratifying human effort against model capability across stages.
- **Our Exact Difference:** Per-stratum label-source swap accounting with dollar normalization.
- **Remaining Novelty:** An accounting exercise inside active learning's framework; stratum interactions (idea's own risk) blur attribution.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Active-learning corpus; SAM data-engine ablations.
- **Reason (elimination):** Question owned by an established field; no precise scientific remainder.

---

## Sub-cluster: Continual & test-time adaptation

### A-0292 — Prompt memory as weight-free continual learning
- **Decision:** KILL
- **Closest Prior Works:**
  1. Personalize Segment Anything (PerSAM) — Zhang et al., ICLR 2024, arXiv:2305.03048 (training-free prompt-based adaptation of frozen SAM)
  2. Matcher — Liu et al., ICLR 2024, arXiv:2305.13310 (reference-based prompt generation over frozen models)
  3. SegGPT — Wang et al., ICCV 2023, arXiv:2304.03284 (visual in-context learning)
- **Existing Work Actually Did:** Frozen-model improvement via stored visual references / generated prompts is an established line (personalization, one-shot matching, in-context segmentation) — the substrate this idea claims is unexplored.
- **Our Exact Difference:** Framing accumulation as continual learning with monotonic-improvement curves.
- **Remaining Novelty:** Marginal: the mechanism exists; only the continual-learning bookkeeping is new, and gains cap at prompt expressiveness (idea's own risk).
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** PerSAM; Matcher; SegGPT.
- **Reason (elimination):** Substrate already built by three published systems.

### A-0296 — Prompt-consistency as a TTA objective
- **Decision:** KILL
- **Closest Prior Works:**
  1. Improving the Generalization of Segmentation Foundation Model under Distribution Shift via Weakly Supervised Adaptation (WeSAM) — Zhang et al., CVPR 2024, arXiv:2312.03502 (anchor-consistency self-training for SAM under shift)
  2. TENT: Fully Test-Time Adaptation by Entropy Minimization — Wang et al., ICLR 2021, arXiv:2006.10726
- **Existing Work Actually Did:** WeSAM already adapts SAM on unlabeled shifted targets using consistency between anchor and adapted networks across prompt-conditioned outputs — substantially the proposed signal; entropy baselines are standard.
- **Our Exact Difference:** Pure cross-prompt agreement (same object, different prompts) as the objective.
- **Remaining Novelty:** A variant objective within an existing SAM-TTA line; degenerate-solution risk (idea's own) is the known failure mode such methods already engineer around.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** WeSAM ("prompt-conditioned consistency adaptation exists").
- **Reason (elimination):** Method-shaped delta inside a published framework.

### A-0300 — Certified-deviation PEFT for regulated adaptation
- **Decision:** KILL
- **Closest Prior Works:**
  1. Efficient and Accurate Estimation of Lipschitz Constants for DNNs (LipSDP) — Fazlyab et al., NeurIPS 2019, arXiv:1906.04893
  2. Certified Adversarial Robustness via Randomized Smoothing — Cohen et al., ICML 2019, arXiv:1902.02918
- **Existing Work Actually Did:** Certification machinery (Lipschitz bounds, smoothing) exists and its central lesson is that non-vacuous bounds on high-dimensional dense outputs are extremely hard; norm-constrained update families are standard PEFT variants.
- **Our Exact Difference:** Composing the two into "certified adaptation" for segmentation.
- **Remaining Novelty:** The idea's own risk (vacuous bounds at useful adaptation strength) is the probable outcome given layer-wise Lipschitz products blow up through 12+ transformer blocks; no evidence base suggests otherwise.
- **Novelty Confidence:** medium (that it is NOT novel — as a feasible contribution)
- **Reviewer-Likely Attack Papers:** LipSDP-line tightness results.
- **Reason (elimination):** Theory-shaped idea with predictable negative outcome; regulator value hypothetical.

---

## Sub-cluster: Architecture internals

### A-0302 — Mask-token capacity law: description-length limits of the decoder
- **Decision:** KILL
- **Closest Prior Works:**
  1. HQ-SAM — Ke et al., NeurIPS 2023, arXiv:2306.01567 (adds an output token to expand decoding capacity — implicit concession the token budget binds)
  2. SegViT — NeurIPS 2022 (query/token budget vs. dense output quality trade-offs)
- **Existing Work Actually Did:** Token-budget effects on mask quality are demonstrated by token-engineering fixes; query-capacity trade-offs are documented in token-based decoder design.
- **Our Exact Difference:** Fitting an explicit complexity-threshold law with decoder-retraining ladders (1–16 tokens).
- **Remaining Novelty:** Real but expensive (retraining ladder) and metric-contestable (mask description length has no canonical definition — idea's own risk); the qualitative capacity story is already conceded by fixes.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** HQ-SAM ("token budget already shown to bind and fixed").
- **Reason (elimination):** Law-fitting exercise over a conceded phenomenon; loses quota competition to cheaper keeps.

### A-0313 — Individuation depth predicts touching-instance ability
- **Decision:** KILL
- **Closest Prior Works:**
  1. Understanding Intermediate Layers Using Linear Classifier Probes — Alain & Bengio, 2016, arXiv:1610.01644
  2. Do Vision Transformers See Like CNNs? — Raghu et al., NeurIPS 2021, arXiv:2108.08810 (layer-wise representation analysis across architectures)
  3. Touching-instance methods literature (see A-0073 kill: Ceb 2025 etc.)
- **Existing Work Actually Did:** Layer-wise probing of what becomes decodable at which depth is a mature methodology; touching-instance difficulty is an established methods subfield.
- **Our Exact Difference:** Correlating "individuation depth" with downstream instance metrics across encoders.
- **Remaining Novelty:** Depth-of-decodability correlates are a standard probing trope; linear probes understate nonlinear individuation (idea's own risk), making the predictor claim fragile.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Alain & Bengio methodology critiques; Raghu et al.
- **Reason (elimination):** Standard-methodology instantiation without a sharp falsifiable core.

### A-0314 — Activation steering for mask decoders
- **Decision:** MUTATE
- **Closest Prior Works:**
  1. Inference-Time Intervention — Li et al., NeurIPS 2023, arXiv:2306.03341 (steering vectors, LLMs)
  2. Activation Steering Decoding for LVLM hallucination — ACL 2025 — https://aclanthology.org/2025.acl-long.634/
  3. Steer2Edit: From Activation Steering to Component-Level Editing — 2026, arXiv:2602.09870
- **Existing Work Actually Did:** Activation steering is mature for LLM/LVLM *token generation* (behavior directions, hallucination suppression, component-level editing). SEARCH NOTE: no work found steering *dense continuous outputs* (mask geometry) in segmentation decoders.
- **Our Exact Difference:** Steering targets interpretable geometric mask properties (grow/shrink, include-attachments, boundary tightness) with dose-response and compositionality measurement — a different output modality and a scientific readout (does the decoder have linear property axes?), not behavior suppression.
- **Remaining Novelty:** Existence and geometry of property axes in prompt-conditioned mask decoders; doubles as a training-free control interface.
- **Novelty Confidence:** medium
- **Reviewer-Likely Attack Papers:** ITI/steering line ("technique known"); entanglement critics (idea's own risk).
- **Mutated One-Liner:** *Do mask decoders have linear property axes? Contrastive activation differences as steering vectors for interpretable mask properties, evaluated by cross-image generalization, dose-response linearity, and composition — a mechanistic map of SAM's decoder space, not another steering app.*
- **New Hypothesis:** For ≥3 of 4 tested properties (dilate/erode, attachment inclusion, boundary tightness, granularity), a single steering direction extracted from 100 contrastive pairs transfers to held-out images with monotone dose-response (Spearman ρ>0.7 between strength and property change) and <15% off-target property drift, establishing approximately linear, compositional property axes in the decoder.
- **Reason (survival via mutation):** Repositioned from "port steering to vision" (attackable as technique transfer) to "measure the decoder's internal property geometry" (unclaimed), with the control interface as a corollary.

---

## Sub-cluster: 3D, volumetric & geometry

### A-0316 — Multi-view mask consistency defect of 2D promptable models
- **Decision:** KILL
- **Closest Prior Works:**
  1. Segment Anything in 3D with NeRFs (SA3D) — Cen et al., NeurIPS 2023, arXiv:2304.12308
  2. Gaussian Grouping — Ye et al., ECCV 2024, arXiv:2312.00732
  3. GARField: Group Anything with Radiance Fields — Kim et al., CVPR 2024, arXiv:2401.09419
- **Existing Work Actually Did:** The entire SAM-to-3D lifting line exists *because* per-view SAM masks are inconsistent across views; these papers document the inconsistency (including granularity flips across views — GARField's core motivation) and engineer around it with 3D fusion.
- **Our Exact Difference:** A standalone quantification (lift-reproject IoU vs. viewpoint separation).
- **Remaining Novelty:** A measurement of a failure that motivates a published methods line; the practical conclusion (fuse in 3D, don't trust per-view masks) is already the field's consensus.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** SA3D; GARField ("inconsistency is our stated motivation").
- **Reason (elimination):** Phenomenon is the founding premise of an active subfield.

### A-0317 — Is implicit geometry causally used by segmentation? Cue-conflict test
- **Decision:** KILL
- **Closest Prior Works:**
  1. Probing the 3D Awareness of Visual Foundation Models — El Banani et al., CVPR 2024, arXiv:2404.08636
  2. ImageNet-trained CNNs are biased towards texture (cue-conflict methodology) — Geirhos et al., ICLR 2019, arXiv:1811.12231
- **Existing Work Actually Did:** 3D-awareness probing established which VFM features encode geometry; cue-conflict methodology for adjudicating cue use is standard and its general finding (appearance dominates) is robust across tasks.
- **Our Exact Difference:** Segmentation-decision-level cue-conflict with presence-vs-use dissociation.
- **Remaining Novelty:** Real but predictable (appearance will win — the idea itself predicts it); conflict-scene construction (idea's own risk) is the same artifact trap flagged repeatedly above. Trompe-l'oeil corpora are tiny.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** El Banani et al. ("presence mapped"); Geirhos et al. ("cue-conflict answer known").
- **Reason (elimination):** Expected outcome via established methodology on scarce data; quota.

### A-0320 — Latent amodal knowledge in modal-trained promptable models
- **Decision:** KILL
- **Closest Prior Works:**
  1. pix2gestalt: Amodal Segmentation by Synthesizing Wholes — Ozguroglu et al., CVPR 2024, arXiv:2401.14398
  2. Amodal Instance Segmentation with KINS — Qi et al., CVPR 2019
- **Existing Work Actually Did:** pix2gestalt demonstrated that large pretrained (diffusion) models harbor zero-shot amodal completion ability unlockable with light adaptation — the "latent amodal knowledge in foundation models" headline already exists; amodal benchmarks/protocols are mature.
- **Our Exact Difference:** Prompt-elicitation (rather than generative synthesis) on SAM-class models.
- **Remaining Novelty:** Whether elicited completions reflect scene-specific inference vs. shape priors (idea's own risk) is exactly the ambiguity pix2gestalt already navigated; the SAM-specific answer changes little.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** pix2gestalt ("latent amodal ability in foundation models shown").
- **Reason (elimination):** Headline claim published for a stronger model class.

### A-0330 — Reflection duplication and latent reflection-source binding
- **Decision:** KILL
- **Closest Prior Works:**
  1. Where Is My Mirror? — Yang et al., ICCV 2019 (mirror segmentation; reflection confusion documented)
  2. Don't Hit Me! Glass Detection in Real-World Scenes — Mei et al., CVPR 2020
- **Existing Work Actually Did:** Mirror/glass segmentation is a dedicated subfield with datasets and methods explicitly motivated by models confusing reflections with real content.
- **Our Exact Difference:** Duplication-rate quantification + latent reflection-vs-real probe on frozen features.
- **Remaining Novelty:** The probe angle is fresh but niche; probe generalization across reflection types (idea's own risk) and the existence of supervised mirror detectors (which already provide the deduplication signal) cap the impact.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Mirror/glass detection line ("dedicated detectors exist and work").
- **Reason (elimination):** Niche delta over an equipped subfield; quota.

---

## Sub-cluster: Compositionality & counting

### A-0334 — Scene-parse coherence: containment contradictions in mask sets
- **Decision:** KILL
- **Closest Prior Works:**
  1. Panoptic Segmentation — Kirillov et al., CVPR 2019, arXiv:1801.00868 (coherence-by-construction output format)
  2. Deep Hierarchical Semantic Segmentation — Li et al., CVPR 2022, arXiv:2203.14335 (hierarchy-consistency constraints and metrics)
  3. Semantic-SAM — Li et al., 2023, arXiv:2307.04767 (multi-granularity consistency training)
- **Existing Work Actually Did:** Output-coherence has been formalized twice: panoptic formats forbid contradictions by construction, and hierarchical segmentation lines define and optimize hierarchy-consistency metrics.
- **Our Exact Difference:** Auditing raw promptable-mask sets (which lack coherence constraints) and correlating a coherence score with downstream scene-graph accuracy.
- **Remaining Novelty:** That unconstrained mask sets contain contradictions is guaranteed by construction (no constraint is enforced) — a foreordained positive; the downstream-correlation claim is interesting but extraction-protocol-dependent (idea's own risk).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Panoptic/HSSN lines ("coherence formalized and enforced where it matters").
- **Reason (elimination):** Headline result is definitionally guaranteed; formalizations exist.

### A-0336 — Object permanence at the representation level in SAM2
- **Decision:** KILL
- **Closest Prior Works:**
  1. Learning Object Permanence from Video — Shamsian et al., ECCV 2020, arXiv:2003.10469
  2. SAM2Long — Ding et al., 2024, arXiv:2410.16268 (occlusion-driven memory error accumulation)
  3. IntPhys / Physion intuitive-physics probing lines
- **Existing Work Actually Did:** Object permanence probing in video models is established methodology; SAM2's occlusion behavior is characterized behaviorally by the memory-fix line.
- **Our Exact Difference:** Decodability-decay vs. behavioral re-acquisition timing (maintained-state vs. re-detection dissociation).
- **Remaining Novelty:** Real but duplicates kept A-0016's territory (forgetting-curve + memory-content alignment answers the same maintained-vs-re-detected question with a cheaper instrument); probes may read scene priors (idea's own risk).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** SAM2Long; permanence-probing line.
- **Reason (elimination):** Intra-cluster redundancy with kept A-0016; two SAM2-memory survivors (A-0016, A-0017) already fill this quota.

---

## Sub-cluster: Failure prediction & deployment

### A-0346 — Data-derived cross-model failure taxonomy
- **Decision:** KILL
- **Closest Prior Works:**
  1. TIDE — Bolya et al., ECCV 2020, arXiv:2008.08115 (detection failure taxonomy + toolbox)
  2. Metrics Reloaded — Maier-Hein et al., 2024 (error-type framework for validation)
  3. Boundary IoU — Cheng et al., 2021 (boundary-vs-region error decomposition)
- **Existing Work Actually Did:** Failure taxonomies and error decompositions exist as adopted tooling for detection and as frameworks for segmentation validation; they are expert-designed rather than cluster-derived.
- **Our Exact Difference:** Unsupervised clustering of error signatures across models.
- **Remaining Novelty:** Clustering granularity is subjective (idea's own risk), coverage/stability claims are unfalsifiable in practice, and adoption — the actual deliverable — depends on community process, not the paper.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** TIDE ("taxonomy exists and is adopted").
- **Reason (elimination):** Infrastructure ambition without a crisp falsifiable core; expert taxonomies incumbent.

### A-0348 — Wrongness visibility: optimizing for detectable errors
- **Decision:** KILL
- **Closest Prior Works:**
  1. Does the Whole Exceed its Parts? — Bansal et al., CHI 2021 (error detectability drives human-AI team outcomes)
  2. To Trust or to Think — Buçinca et al., CSCW 2021
- **Existing Work Actually Did:** The human-AI literature established that plausible-but-wrong outputs are the harm driver and measures detectability; complementary-team-performance framing already optimizes for it.
- **Our Exact Difference:** Segmentation-specific plausibility ratings + a plausibility-penalty training loss.
- **Remaining Novelty:** Rating subjectivity (idea's own risk) plus the same over-reliance findings killed A-0221; the training intervention is a method add-on to an HCI result.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Bansal et al.; Buçinca et al.
- **Reason (elimination):** Adjacent field owns the concept; segmentation port is incremental.

### A-0356 — Compact audit-probe suite for black-box capability fingerprinting
- **Decision:** KILL
- **Closest Prior Works:**
  1. tinyBenchmarks: evaluating LLMs with fewer examples — Polo et al., ICML 2024, arXiv:2402.14992
  2. Model fingerprinting / black-box auditing literature (multiple lines)
- **Existing Work Actually Did:** Predicting full-benchmark performance from small curated probe sets is published methodology (tinyBenchmarks: ~100 examples predict full suites); black-box behavioral auditing is an active area.
- **Our Exact Difference:** Designed synthetic probes for segmentation capabilities.
- **Remaining Novelty:** Direct methodology port; gaming/rotation problems (idea's own risk) are unsolved there too.
- **Novelty Confidence:** high (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** tinyBenchmarks.
- **Reason (elimination):** Template exists with the same math; vision port is engineering.

---

## Sub-cluster: Bonus cross-cutting

### A-0361 — Disagreement-maximizing benchmark synthesis (shared frontier)
- **Decision:** KILL
- **Closest Prior Works:**
  1. ImageNet-D — CVPR 2024, arXiv:2403.18775 (diffusion-synthesized hard cases that degrade many models simultaneously)
  2. 3DB: A Framework for Debugging Vision Models — Leclerc et al., 2021, arXiv:2106.03805 (systematic synthetic failure search)
- **Existing Work Actually Did:** Generative/synthetic search for inputs that break many models is published (ImageNet-D explicitly selects images that fool multiple surrogates); rendering-based debugging frameworks formalize the search.
- **Our Exact Difference:** Disagreement (not error) as the objective + segmentation outputs.
- **Remaining Novelty:** Generative-model bias constrains the search space (idea's own risk) — the discovered "shared frontier" is the frontier of the generator's manifold, a critique ImageNet-D already absorbs.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** ImageNet-D; 3DB.
- **Reason (elimination):** Search paradigm published; objective tweak insufficient.

### A-0366 — Model paleontology: inferring training data from behavior
- **Decision:** KILL
- **Closest Prior Works:**
  1. Membership Inference Attacks — Shokri et al., IEEE S&P 2017 (behavioral training-data inference foundations)
  2. Time Travel in LLMs — Golchin & Surdeanu, ICLR 2024 (behavioral contamination/provenance detection)
- **Existing Work Actually Did:** Inferring training-data properties from black-box behavior is an established security/auditing literature (membership, attribute, and property inference), including dataset-level property inference.
- **Our Exact Difference:** Segmentation-specific probe batteries for mixture recovery.
- **Remaining Novelty:** Subsumes into kept A-0271's fingerprint machinery (which validates the causal link on controlled mixtures first — the necessary prerequisite this idea skips); signal washout at scale (idea's own risk).
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Property-inference literature.
- **Reason (elimination):** Property inference exists; prerequisite science lives in kept A-0271.

### A-0367 — Distribution kinship: segmenters prefer generated images
- **Decision:** KILL
- **Closest Prior Works:**
  1. Self-Consuming Generative Models Go MAD — Alemohammad et al., ICLR 2024, arXiv:2307.01850
  2. AI models collapse... — Shumailov et al., Nature 2024
  3. ImageNet-D — CVPR 2024 (real-vs-generated evaluation asymmetries)
- **Existing Work Actually Did:** Synthetic-data feedback-loop dynamics, curation-bias amplification, and real-vs-generated performance asymmetries are actively published; the ecosystem-contamination mechanism is the model-collapse literature's core subject.
- **Our Exact Difference:** Segmentation-quality kinship measurement + curation-loop simulation.
- **Remaining Novelty:** Fair real/generated matching is unsolved (idea's own risk); the loop simulation re-derives collapse results; kept A-0271 covers the segmentation-specific data-loop risk with identifiable methodology.
- **Novelty Confidence:** medium (that it is NOT novel)
- **Reviewer-Likely Attack Papers:** Model-collapse line.
- **Reason (elimination):** Mechanism published; measurement unfair-matching-limited; theme held by A-0271.

---

## Final tally

| Decision | Count | IDs |
|---|---|---|
| KEEP | 12 | A-0002, A-0003, A-0016, A-0032, A-0061, A-0062, A-0078, A-0107, A-0136, A-0178, A-0227, A-0271 |
| MUTATE | 5 | A-0017, A-0068, A-0128, A-0134, A-0314 |
| KILL | 67 | all remaining |

**Survivors: 17 of 84 (20.2%).** Sub-cluster spread of survivors: prompt-sensitivity 2, SAM2-memory 2, SAM3-concepts 1, boundary 3, distillation 1, PEFT-forgetting 1, calibration 2, small-objects 1, evaluation 1, representation 1, ambiguity 1, data-centric 1.

**Search-integrity note:** Every citation above is a real paper surfaced by web/arXiv/OpenReview/CVF search or verified against search results during this stage. Entries where no direct prior work was found say so explicitly (SEARCH NOTE) and were judged on adjacent literature.
