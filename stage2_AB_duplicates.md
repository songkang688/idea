# Stage 2 — A+B Duplicate Merges & Conflict Flags (partial merge; Batch C pending)

**Role:** Supervisor's clustering/dedup agent, Windows5 Autonomous Research Idea Evolution.
**Inputs:** `stage2_batch_A_survivors.md` (73), `stage2_batch_B_survivors.md` (75) — 148 survivors total.
**Output of this pass:** 18 merges (16 cross-batch A+B, 2 within-B) → **130 unique ideas** in `stage2_AB_merged_pool.md`.
**Rule applied:** merge only when two ideas test substantially the same claim or share so much design that one experimental program answers both. Thematic siblings that answer *different* questions were kept separate and logged in §2. Merge IDs `MERGE-01…18` are stable; Batch C merges will append `MERGE-19+`.

Every merged entry keeps **both original IDs** and inherits the **union of protection flags**.

---

## §1 — Merges (near-duplicates → single mutated idea)

### MERGE-01 = IDEA-A-0029 + IDEA-B-0019 — Model-in-the-loop annotation corrupts its own ground truth
- **A-0029:** SAM-assisted annotation over-represents SAM-easy boundaries, biasing future datasets (HR+RM).
- **B-0019:** Annotators correcting SAM proposals under-correct systematic errors; model-lineage bias inherits across generations (HRHR·DM).
- **Merged mutated idea:** One within-annotator crossover study — the same annotators label matched images {from scratch, SAM-assisted, correct-the-proposal} with washout and counterbalancing; measure agreement-with-SAM inflation and anchoring on systematic errors; train students on each corpus and test error-signature inheritance and downstream ranking shifts.
- **Why merged:** Same core claim (model-in-the-loop annotation quietly imprints the model's competence profile onto "ground truth"), same instrument (within-subject crossover annotation study), same deliverable (contamination coefficient + inheritance test). The two batches independently converged — strongest convergence signal in the pool.
- **Protection carried:** HR+RM / HRHR·DM (maximum protection in the pool).

### MERGE-02 = IDEA-A-0185 + IDEA-B-0241 — The absent-target hallucination benchmark
- **A-0185:** Absence benchmark: confident masks for named-but-absent objects; plausibility-graded triads (CF+RM).
- **B-0241:** Prevalence-conditioned prompting: hallucination grows with prompt assertiveness; absence-option protocols cut it (CI·CF).
- **Merged mutated idea:** A single benchmark crossing {present / absent-plausible / absent-implausible} targets with a prompt-assertiveness ladder ("is there…?" → "find the…" → "segment the…"); measure mask-emission rates, confidence, and the spatial targeting of hallucinated masks against scene-prior/co-occurrence maps; evaluate refusal/absence-option protocols at fixed true-positive sensitivity.
- **Why merged:** Identical dependent variable (mask emission on certified-absent images) and shared load-bearing labor (verified-absence negative curation); plausibility gradient and assertiveness ladder are two axes of one design.
- **Protection carried:** CF+RM / CI·CF.

### MERGE-03 = IDEA-A-0006 + IDEA-B-0226 — One boundary-contrast law across hard-target literatures
- **A-0006:** Amorphous-matter failure is a smooth function of boundary contrast, not a category failure (CI).
- **B-0226:** Camouflage, transparency, and low-contrast lesion detection may lie on one contrast-recall curve (DM).
- **Merged mutated idea:** Test whether a single standardized integrated-boundary-contrast measure predicts both segmentation IoU and detection recall across amorphous matter, camouflage, transparency, and low-contrast lesions — same-curve (ANCOVA category-offset) test, plus a causal arm: contrast-enhance inputs and test predicted recovery. Curve collapse would merge three failure literatures; category offsets would make their differences precise.
- **Why merged:** Same hypothesis (failure is a continuous function of one physical variable, not category membership), same x-axis construct; A's causal arm and B's cross-literature scope strengthen each other.
- **Protection carried:** CI / DM.
- **Dependency:** the smoke y-axis inherits IDEA-A-0121's ill-posed-GT critique — see CONF-3.

### MERGE-04 = IDEA-A-0161 + IDEA-B-0129 — The small-structure bottleneck: information-absent vs decoder-limited
- **A-0161:** Patch-quantization floor: decoder-capacity invariance × patch-size interventions (RM).
- **B-0129:** Oracle probes on frozen features split small-lesion failure into decoder-limited vs information-absent regimes.
- **Merged mutated idea:** Two-stage design: (1) overparameterized pixel probes on frozen features across size strata locate the decodability crossover cheaply; (2) decoder-capacity {1×,3×,10×} × patch-size {8,16,32} training grid tests whether the floor is tokenization-irreversible. Deliverable: the crossover size and the verdict on where small-structure investment should go (decoders vs resolution/tokenization).
- **Why merged:** Same question ("is the information even there?"), complementary instruments; the probe stage is the natural go/no-go gate for the expensive intervention grid.
- **Protection carried:** RM.

### MERGE-05 = IDEA-A-0296 + IDEA-B-0064 — The UDA reality audit
- **A-0296:** UDA rankings scramble on fresh adaptation pairs; gains shrink >50% (RM).
- **B-0064:** Does classical UDA add anything over frozen foundation features with pseudo-label filtering? (DM).
- **Merged mutated idea:** One matched-compute grid: ~6–8 published UDA methods × {frozen hyperparameters, bounded re-tuning} × 4 fresh pairs (aerial/medical/underwater/thermal) × 3 backbone regimes (scratch / supervised / foundation-frozen), with source-only and foundation-baseline arms on every pair. Reports (a) ranking transfer from GTA→Cityscapes, (b) marginal UDA value over foundation baselines, per shift type.
- **Why merged:** The experimental grids are ~80% identical (same methods, budgets, pairs, baselines); both are deflationary audits of the same literature and are strictly stronger run together.
- **Protection carried:** RM / DM. Expensive but decision-grade.

### MERGE-06 = IDEA-A-0303 + IDEA-B-0057 — Statistics recalibration: TTA method + shift-tier diagnostic
- **A-0303:** Norm-recovery fraction as a cheap diagnostic mapping shifts to the minimal sufficient adaptation tier (CF).
- **B-0057:** Token-statistics recalibration as the LayerNorm-era replacement for BN-based TTA.
- **Merged mutated idea:** Per-layer token-population statistic matching for ViTs, evaluated twice: as an optimization-free TTA method (IoU recovery vs TENT and oracle fine-tuning, collapse behavior on long streams) and as an instrument (recovery fraction, measurable in minutes with unlabeled data, routing shifts to norm-stats / PEFT / full-UDA tiers). BN and LN-analog arms; ≥10 pairs spanning sensor/photometric/semantic/mixed shifts.
- **Why merged:** A-0303 explicitly asks for the LN-era analog; B-0057 *is* that analog. One measurement operation, two readouts (method + diagnostic).
- **Protection carried:** CF; the highest immediate-adoption-probability entry in the pool.

### MERGE-07 = IDEA-A-0076 + IDEA-B-0248 — The gain/retention frontier: is forgetting unforced error?
- **A-0076:** Map the target-gain vs zero-shot-retention Pareto frontier; test whether common recipes sit far inside it (RM).
- **B-0248:** At strictly matched target performance, does the low-rank constraint causally preserve zero-shot capability? (DM).
- **Merged mutated idea:** One sweep (LR × trained-components × steps × rank) on shared tasks with dense checkpointing; select checkpoints at matched target IoU (B's confound control); trace the empirical frontier, place published recipes on it, and fit retention-vs-effective-update-rank curves. Verdicts: how much forgetting is recipe hygiene, and whether "LoRA forgets less" survives the undertraining confound.
- **Why merged:** Same frontier, same infrastructure; B's matched-target selection discipline is exactly the control A's frontier estimate needs.
- **Protection carried:** RM / DM.

### MERGE-08 = IDEA-A-0058 + IDEA-B-0260 — Low-rank adaptation amplifies shortcuts
- **A-0058:** LoRA amplifies spurious correlations; worst-group degradation at matched ID accuracy (HR+CI).
- **B-0260:** Adapters overfit site fingerprints harder than full FT at matched in-site IoU (CI·DM).
- **Merged mutated idea:** Test the shared mechanism — low-rank updates can only reweight existing (often spurious) directions — on both constructed spurious-correlation datasets (worst-group IoU) and natural multi-hospital site shifts (out-of-site transfer, fingerprint-alignment diagnostic), with a rank sweep as the mechanism prediction and a multi-site reversal arm.
- **Why merged:** Identical claim and mechanism, synthetic and natural instantiations; matched-ID-performance design discipline is shared. Cross-batch convergence on a safety-critical inversion of PEFT folklore.
- **Protection carried:** HR+CI / CI·DM.
- **Tension with B-0272:** see CONF-1.

### MERGE-09 = IDEA-A-0267 + IDEA-B-0329 — Weak-to-strong dense distillation: inherit vs surpass
- **A-0267:** Students trained on SAM pseudo-labels reproduce SAM's error signature (merit).
- **B-0329:** Weak-to-strong generalization in dense prediction: students surpass on variance-type errors, imitate bias-type errors (HRHR·DM).
- **Merged mutated idea:** Train strong students on weak-teacher/SAM labels across teacher-quality ladders with held-out truth; decompose student-vs-teacher deltas into inherited bias-type errors (signature-match fidelity, using the Batch-A failure taxonomy) vs surpassed variance-type errors; test bias-breaking label perturbations and scratch-data mixing dilution curves; audit one in-the-wild SAM-labeled dataset for the predicted signature.
- **Why merged:** One experiment (students on weak labels + error decomposition against teacher) answers both; A supplies the signature instrument, B the bias/variance theory and surpassing test.
- **Protection carried:** HRHR·DM. Capstone of the contamination program (with MERGE-01, A-0007, B-0001, B-0191, B-0320).

### MERGE-10 = IDEA-A-0141 + IDEA-B-0126 — What frozen features know about layered scenes
- **A-0141:** Features on glass encode the background, not the glass — transparency as representational failure (HR+CI).
- **B-0126:** Two-layer probes decoding glass + transmitted background would make transparency an output-format problem (CI).
- **Merged mutated idea:** One probing program on frozen VFM features over glass regions (interior vs edge stratified, probe-capacity swept): decode {glass presence, background class, both layers}. Outcomes route the field: neither decodable → representation-level fix (pretraining); background only → A's "transparent to transparency" verdict; both decodable → B's output-format fix (layered heads + supervision).
- **Why merged:** Same substrate (linear/two-layer probes on frozen features over Trans10K-class data); B's positive case presupposes A's measurement. Three-way verdict is stronger than either alone.
- **Protection carried:** HR+CI / CI. Flagship of the transparency cluster.

### MERGE-11 = IDEA-A-0250 + IDEA-B-0024 — Deflationary baselines for few-shot segmentation
- **A-0250:** Meta-learning vs direct 5-shot PEFT fine-tuning, cross-domain, with a training-free matching arm (CF).
- **B-0024:** Retrieval + dense-correspondence transfer beats few-shot fine-tuning below a crossover n (DM·CF).
- **Merged mutated idea:** One shot-ladder grid (n ∈ {1,3,5,10,30}) × {episodically meta-trained FSS, direct PEFT fine-tune with a pre-registered fixed recipe, retrieval + DINO-correspondence transfer} × cross-domain targets (medical anatomies + aerial); locate crossovers, regress them on registration residuals, and deliver the honest-baseline table the FSS/medical-SAM literatures never report.
- **Why merged:** A-0250's third arm *is* B-0024's method; identical shot budgets, targets, and honesty constraints. One study retires two gaps.
- **Protection carried:** CF / DM·CF.

### MERGE-12 = IDEA-A-0285 + IDEA-B-0190 — Synthetic-fraction dose-response thresholds
- **A-0285:** Rare-class synthetic augmentation inverts (real-instance recall drops) above ~70% within-class synthetic fraction (CI).
- **B-0190:** A synthetic-fraction threshold where in-domain gains coexist with silent OOD-robustness decay.
- **Merged mutated idea:** One fraction-ladder design sweeping both *within-class* and *global* synthetic fractions across two generator families; endpoints: real-instance rare-class recall (inversion threshold), cross-site/corruption robustness (poisoning threshold), and a generator-classifier probe as the label-free threshold detector. Deliverable: dose rules for the field's main scarcity remedy.
- **Why merged:** Same experimental machinery (synthetic-fraction ladders, real-vs-synthetic stratified evaluation, probe detectors); two failure modes of one dose-response curve.
- **Protection carried:** CI.

### MERGE-13 = IDEA-A-0021 + IDEA-B-0136 — Functional achromaticity of dense models
- **A-0021:** Is SAM functionally achromatic? Hue-rotation/grayscale/equiluminant interventions (CI+CF).
- **B-0136:** Luminance-only smoke: color channels mainly import false-positive risk (CI·CF).
- **Merged mutated idea:** A common color-intervention battery — {original, grayscale, hue-rotated, equiluminant edges, chroma-only} — applied to SAM-class models (frozen) and smoke segmenters (frozen, then retrained on {RGB, L-only, chroma-only}); establishes which dense capabilities are colorblind, with the equiluminant condition as the discriminating test and FP-stratified smoke reporting as the deployment payoff.
- **Why merged:** Same instrument (channel/hue interventions), same question (is the boundary signal achromatic?), general + applied instantiations.
- **Protection carried:** CI+CF / CI·CF. Note apparent tension with A-0123 (fire = color detectors) — see CONF-9.

### MERGE-14 = IDEA-A-0166 + IDEA-B-0037 — The annotation-tolerance ceiling
- **A-0166:** Annotation jitter floor; model residuals predict annotator identity (style-fitting proof) (CI).
- **B-0037:** Closed-form maximum-IoU ceiling from boundary tolerance and object size/shape (CF).
- **Merged mutated idea:** Derive the analytic IoU ceiling as a function of boundary tolerance and object size (B); estimate real tolerance from multi-rater re-annotation on 3 benchmarks (A); flag at-ceiling strata; and run the annotator-identity-prediction test on model residuals to prove sub-jitter "progress" is style-fitting.
- **Why merged:** The analytic ceiling needs the empirical tolerance; the empirical jitter measurement needs the analytic form to convert to per-stratum ceilings. Two halves of one paper.
- **Protection carried:** CI / CF.

### MERGE-15 = IDEA-A-0091 + IDEA-B-0082 — Label-noise-aware leaderboards
- **A-0091:** Inter-annotator ceiling of medical benchmarks vs leaderboard spread — progress within label noise (RM).
- **B-0082:** Relabeling bootstrap: resample plausible relabelings from a fitted inter-rater noise model; report rank-flip probabilities (CF·DM).
- **Merged mutated idea:** Expert re-annotation (3 raters × 50–100 cases × ~5 benchmarks) fits the noise model *and* measures the floor; the relabeling bootstrap then converts it into rank-flip probabilities for public leaderboards; deliverables: which reported gains are within label noise, per-benchmark death verdicts, and a reusable rank-stability instrument.
- **Why merged:** B's instrument consumes exactly the multi-rater data A collects; same annotation budget, one program. (A-0340's *image-sampling* bootstrap is a different noise source and stays separate — the two are designed complements.)
- **Protection carried:** RM / CF·DM. Flagship-tier for medical evaluation.

### MERGE-16 = IDEA-A-0142 + IDEA-B-0159 — Depth failure as transparency signal
- **A-0142:** Naive RGB-D fusion hurts transparency; depth-*invalidity* as an explicit feature outperforms both (CI).
- **B-0159:** Invalid-depth pixels harvested as free physics-generated transparency labels — potentially the largest transparency corpus in existence (HRHR).
- **Merged mutated idea:** Exploit the same physical fact (depth sensors fail on glass) on both sides of the pipeline: (a) inference — {RGB, naive RGB-D, RGB+validity-mask} triad across 3 sensor types; (b) supervision — harvest invalid-depth masks from public RGB-D corpora with confounder filtering (range limits, absorption, occlusion shadows), characterize label noise, and train RGB models on harvested vs manual labels at matched scale.
- **Why merged:** One discovery claim ("depth invalidity is the strongest transparency cue"), two exploitation arms; noise characterization from (b) informs feature design in (a).
- **Protection carried:** CI / HRHR (protected wildcard).

### MERGE-17 = IDEA-B-0089 + IDEA-B-0193 — The human-prompt distribution gap (within-B merge)
- **B-0089:** Oracle-prompt inflation factor in interactive-segmentation reporting (DM).
- **B-0193:** Programmatic vs human-realistic prompt distributions in SAM-style training — a nearly free fix.
- **Merged mutated idea:** Collect human prompt logs once (4 tasks); measure (a) the oracle-prompt inflation factor of GT-derived prompts and fit predictors from target-visibility statistics, and (b) the training-side gain from fine-tuning with a fitted human-prompt model vs programmatic sampling, evaluated under real human prompting. Evaluation-side and training-side halves of one gap, on one dataset.
- **Why merged:** B's reviewer already prescribed shared data collection; the merged framing (the interaction channel has a domain gap; measure it at eval, close it at training) is strictly stronger.
- **Protection carried:** DM.

### MERGE-18 = IDEA-B-0120 + IDEA-B-0337 — Are free mask ensembles valid posteriors? (within-B merge)
- **B-0120:** Coverage-test SAM's multimask candidate spread as an uncertainty interval; hypothesis: it collapses OOD (CF).
- **B-0337:** Coverage-test mask-diffusion sample spread against held-out rater distributions (CF·DM).
- **Merged mutated idea:** One coverage-testing methodology (held-out-rater reference distributions, in- and out-of-domain) applied to the two "free" uncertainty sources practitioners already consume: SAM multimask spread and mask-diffusion samples; compare against ensembles/conformal baselines per unit compute; test post-hoc recalibration of each.
- **Why merged:** Identical instrument (distributional coverage tests against rater populations), identical question ("is free/generative uncertainty statistically real?"); B's reviewer flagged them as a pair.
- **Protection carried:** CF / CF·DM.

---

## §2 — Related but NOT merged (watchlist for Batch C / Stage 3)

These pairs share a theme or infrastructure but answer different questions. Do not collapse them; do co-schedule them.

| Family | Members | Why kept separate |
|---|---|---|
| Annotation-convention imprinting | A-0007 · B-0006 · B-0053 | Single-protocol imprint (A-0007) vs multi-protocol averaging bias + token fix (B-0006) vs ontology-vs-appearance decomposition (B-0053). Three distinct claims, one shared vocabulary. |
| Prompt/protocol evaluation instability | A-0031 · B-0083 · B-0108 | Text-paraphrase variance vs click-protocol sensitivity vs hidden validation-search inflation. Different mechanisms of the same disease; publish as a suite. |
| Uncertainty vs expert disagreement | A-0103 · MERGE-18 | Heuristic UQ maps vs generative/candidate ensembles; same reference data (multi-rater), different objects. |
| Medical hallucination of absent anatomy | A-0118 · B-0185 | Atlas-prior hallucination in automatic models vs text-prior override in VLMs. Twin refusal framings; joint metric design only. |
| Generator coverage limits | B-0186 · A-0287 | Tail coverage of within-domain augmentation vs procedural-vs-diffusion on web-sparse phenomena. Shared coverage metrics, different comparisons. |
| Human floor/ceiling instrument | A-0336 · A-0157 · A-0305 | General benchmark anchor vs glass hardest-regime verdict vs night information-floor verdict. Batch A already consolidated this family; the two domain applications carry independent decisions. |
| Color reliance | MERGE-13 · A-0123 | Independence-of-color (achromaticity) vs over-reliance-on-color (fire shortcut). Opposite directions; see CONF-9. |
| Size failure laws | A-0003 · MERGE-04 | Inference-side IoU-vs-size law with patch knee vs causal tokenization-floor intervention. Same program, different evidence layers. |
| Amorphous detection primitives | A-0319 · B-0219 | Output primitive (box vs blob) vs suppression-stage (NMS) attribution. Two pipeline stages. |
| Contamination instruments | A-0254 · B-0294 | Construct a contamination-proof benchmark vs detect contamination behaviorally. Complementary instruments. |
| Negative-set infrastructure | B-0017 · B-0110 · MERGE-02 | Shared curation of verified-absent/hard-negative sets; distinct claims (ranking inversion / FP certification / hallucination benchmark). Amortize curation across all three. |
| Meta-science calibration chain | A-0226 · A-0242 · B-0114 | Replication re-runs ground-truth the z-curve; seed-variance tables calibrate both. Chain, not duplicate. |
| Loss → calibration structure | A-0097 · B-0310 | Dice-vs-CE imbalance-scaled miscalibration vs soft-label mean-regression overconfidence. Different mechanisms. |
| SA-1B audits | A-0007 · B-0009 | Protocol-granularity imprint vs frequency-capability census. Same corpus, different measurements. |

---

## §3 — Conflict flags (where reviewers would disagree)

**CONF-1 — Low-rank: shield or amplifier?** MERGE-08 (A-0058+B-0260) predicts low-rank updates *amplify* shortcuts under spurious correlations/site shift; B-0272 predicts low-rank *protects* under structured label noise. Same mechanism (constrained update geometry), opposite signs, different noise/shift geometry. Reviewers will split on which regime dominates practice. Resolution path: run both on a shared grid with B-0001's fitted SAM-noise model as the injection source; the sign map (noise-type × shift-type → help/harm) is the real deliverable.

**CONF-2 — The boundary-expressivity paradox.** B-0257 (boundary tax: low rank cannot express high-frequency boundary detail) vs B-0272 (low rank cannot fit boundary-offset noise — and that's protective). Both cannot be unconditionally true; the reconciliation (signal vs noise in the same frequency band) must be tested explicitly.

**CONF-3 — Smoke ground truth validity.** A-0121 (binary smoke masks are threshold noise) undermines the dependent variable of MERGE-03's contrast law, A-0128's shrinkage law, and every smoke IoU number in the pool. Sequencing constraint: A-0121/A-0122 density machinery first; reviewers of the smoke program will disagree until it exists.

**CONF-4 — Who deleted the small objects?** MERGE-04/A-0003 attribute small-structure failure to patch tokenization; A-0176 claims benchmark JPEG already destroyed the evidence before models saw it. Rival attributions of the same phenomenon; A-0176's paired lossless capture must run as the confounder control before floor claims are headlined.

**CONF-5 — Preprocessing: helps or harms?** B-0338 (denoising deletes the forensic cue tiny targets depend on) vs B-0285 (compression deletes clutter and *helps* smoke). Both invert preprocessing dogma in opposite directions; the reconciliation variable is target-class spectral separation vs contrast-to-noise regime. Reviewers will pattern-match a contradiction unless framed as one target-relative theory of preprocessing.

**CONF-6 — Scale up or scale hurts?** A-0313 (raw input resolution dominates architectural remedies at matched compute) vs B-0288 (bigger *models* lose to smaller ones on tiny structures). Input-scaling vs capacity-scaling axes; not logically contradictory but a guaranteed reviewer collision — coordinate the size-stratified evaluation suites.

**CONF-7 — Rival single-factor reductions of PEFT.** A-0055 (LLRD explains most of the PEFT advantage) vs A-0067 (the encoder/decoder LR ratio explains most recipe variance). Overlapping variables in different parameterizations; run on shared grids or reviewers will accuse the program of explaining the same variance twice.

**CONF-8 — Is PEFT intrinsically valuable?** A-0072 (strong augmentation + frozen features matches LoRA at matched compute) vs B-0306/B-0272 (rank-tuned adapters have intrinsic small-n and noise-robustness value). Deflation vs defense of the same method family; the low-data stratification is where they collide directly.

**CONF-9 — Color: irrelevant or a crutch?** MERGE-13 concludes(-ish) dense models are functionally achromatic; A-0123 claims fire segmenters are color detectors. Different models and tasks, but the headlines read as contradictory. Frame jointly: color is unused where luminance structure suffices (SAM), over-used where it is the cheapest shortcut (fire).

**CONF-10 — The evaluation cluster vs everyone's effect sizes.** MERGE-15, MERGE-14, A-0340, A-0337, A-0336 collectively argue that 0.5–2-point benchmark gaps are frequently within noise (label, sampling, instruction, or human-floor). But several audits in this very pool (A-0245, MERGE-05, A-0226, A-0313) use gaps of that scale as endpoints. Sequencing: evaluation instruments first, or every audit must carry noise-aware CIs. This is a program-level dependency reviewers will exploit.

**CONF-11 — Physics labels: free lunch or biased lunch?** B-0159 (MERGE-16) treats sensor-physics labels as a windfall; B-0184 shows enhancement-physics labels encode blindness to exactly the clinical cases that matter. Same paradigm, opposite morals; publish as a pair, as Batch B's reviewer proposed.

**CONF-12 — Attribution overlap in medical progress.** A-0093 (nnU-Net's residual advantage = 3D context + augmentation policy) and A-0245 (a decade of progress = recipes) partially claim the same variance on the same benchmarks. Coordinate decompositions so the two papers cannot be read as double-counting.

**CONF-13 — Frozen-hyperparameter fairness.** Within MERGE-05, the frozen-hyperparameter protocol will be attacked by UDA authors as unfair (both batch reviewers flagged this independently). The bounded-retuning arm is the negotiated compromise; pre-register it.

**CONF-14 — Prompted-evaluation protocol overlap.** MERGE-17 (oracle inflation) and B-0083 (protocol sensitivity) measure adjacent instabilities of the same reporting practice; without a shared protocol taxonomy their numbers will appear to disagree. Pre-agree the taxonomy before either runs.

---

*End of duplicates & conflicts log. 148 → 130 unique. Batch C merge pass will extend this file.*
