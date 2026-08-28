# Stage 1 — Batch A: 340 Original Research Ideas

**PI:** Windows5
**Scope:** Vision foundation models, VLMs, PEFT, SAM/SAM2, segmentation (medical / smoke / fire / transparent / ambiguous), object detection, and adjacent scientifically-motivated directions.
**IDs:** IDEA-A-0001 … IDEA-A-0340
**Conventions:** Every idea has a falsifiable core hypothesis and a minimal experiment. Citations refer only to well-known real papers/systems (SAM, SAM2, CLIP, DINOv2, MedSAM, nnU-Net, LoRA, Mask2Former, CoOp, SegGPT, TENT, WiSE-FT, SynthSeg, Trans10K, etc.). Anything speculative is marked HYPOTHESIS. No experimental results are claimed anywhere — only proposed experiments.

---

## Cluster 1 — SAM / SAM2 Failure Modes & Mechanistic Analysis (IDEA-A-0001 … 0030)

### IDEA-A-0001
- **One-sentence idea:** Test whether SAM segments *visual boundaries* rather than *semantic objects* by dissociating the two on camouflage and texture-boundary stimuli.
- **Problem:** SAM's zero-shot masks are widely treated as "object" masks, but its training signal (SA-1B) rewards boundary-consistent regions, and nobody has cleanly dissociated edge-following from objecthood.
- **Core Hypothesis (falsifiable):** SAM's mask agreement with ground truth is predicted almost entirely by local boundary gradient strength, not by object semantics; on stimuli where a strong texture edge crosses an object (or a camouflaged object has no edge), SAM will follow the edge, not the object, in >80% of cases.
- **Why Important:** Thousands of pipelines use SAM masks as object proposals; if SAM is an edge-machine, downstream semantic conclusions are systematically biased.
- **Why Possibly Novel:** Failure reports on camouflage exist, but a controlled dissociation design (edge-present/object-absent vs object-present/edge-absent quadrants) has not been published as a mechanistic claim.
- **Minimal Experiment:** Build a 500-image 2×2 stimulus set (real camouflage images + composited texture-edge overlays on COCO objects); prompt SAM with center clicks; regress mask IoU against boundary gradient energy vs semantic-class factors.
- **Main Risk:** Composited stimuli may introduce blending artifacts SAM detects, confounding the edge/object dissociation.

### IDEA-A-0002
- **One-sentence idea:** Measure whether SAM's multi-mask ambiguity head reproduces the *distribution* of human annotator disagreement or just a fixed part/whole ladder.
- **Problem:** SAM outputs 3 masks to handle ambiguity, but it is unknown whether these correspond to how humans are actually ambiguous about the same prompt.
- **Core Hypothesis (falsifiable):** The Jensen–Shannon divergence between SAM's 3-mask distribution and the empirical human mask distribution is no better than a fixed heuristic ("part, object, group"), i.e., SAM models a granularity ladder, not scene-specific ambiguity.
- **Why Important:** If ambiguity output is a static ladder, uncertainty estimates built on SAM's multimask scores are not measuring real ambiguity.
- **Why Possibly Novel:** SAM's ambiguity head has been used but not validated against multi-annotator ground truth as a distribution-matching problem.
- **Minimal Experiment:** Collect 10 annotator masks per prompt on 300 ambiguous click-prompts (reuse multi-annotator subsets of existing datasets where possible); compare SAM multimask sets to human sets with optimal-assignment IoU and distributional divergence.
- **Main Risk:** 10 annotators may under-sample the true human distribution, making the null hard to reject.

### IDEA-A-0003
- **One-sentence idea:** Establish an empirical "failure law" relating object pixel size to SAM IoU and test whether the breakpoint is set by the ViT patch size (16 px).
- **Problem:** "SAM is bad at small objects" is folklore without a quantitative form; if the failure is patch-quantization-driven, it predicts a specific breakpoint and scaling.
- **Core Hypothesis (falsifiable):** SAM's mean IoU vs object diameter follows a saturating curve with a sharp knee at ~2–3 patch widths (32–48 px at 1024 input), and re-running with a hypothetical smaller-patch encoder (or higher-res tiling) shifts the knee proportionally — if the knee does not track patch size, the hypothesis is falsified.
- **Why Important:** Turns an anecdote into a design law: tells practitioners exactly when tiling/zooming is required rather than relying on trial and error.
- **Why Possibly Novel:** Size-stratified SAM evaluations exist informally, but no work has tested the patch-size causal claim by intervening on effective patch resolution.
- **Minimal Experiment:** Evaluate SAM on COCO/LVIS instances binned by diameter; repeat with 2× and 4× zoomed crops (changing object-size-in-patches while fixing semantics); check whether the IoU-vs-size curve collapses when the x-axis is measured in patches.
- **Main Risk:** Zooming changes context, which independently affects SAM; needs context-controlled crops.

### IDEA-A-0004
- **One-sentence idea:** Quantify error accumulation in SAM2 video segmentation as a function of occlusion duration and show whether the memory bank recovers or compounds drift.
- **Problem:** SAM2's streaming memory is assumed to handle occlusions, but there is no published curve of mask quality vs occlusion length or a characterization of post-occlusion recovery dynamics.
- **Core Hypothesis (falsifiable):** Post-occlusion IoU decays approximately exponentially with occlusion length beyond the memory horizon, and recovery after re-appearance is bimodal (full recovery or permanent identity loss), not gradual.
- **Why Important:** Occlusion behavior determines whether SAM2 can be trusted in surgery, driving, and wildlife monitoring; bimodal failure means average metrics hide catastrophic cases.
- **Why Possibly Novel:** SAM2 evaluations report aggregate J&F; occlusion-duration-conditioned failure curves and recovery-mode analysis are missing.
- **Minimal Experiment:** Take DAVIS/YouTube-VOS clips, procedurally insert synthetic occluders of controlled duration (5–120 frames) over tracked objects; measure IoU-vs-time and classify recovery modes.
- **Main Risk:** Synthetic occluders may be easier than real occlusions (no distractors); include a real-occlusion validation subset.

### IDEA-A-0005
- **One-sentence idea:** Characterize SAM2 identity switches between visually similar instances and test whether failures are appearance-driven or position-prior-driven.
- **Problem:** In multi-instance scenes (herds, crowds, surgical tools), SAM2 swaps targets, but the causal driver (appearance similarity vs motion/position prior in memory attention) is unknown.
- **Core Hypothesis (falsifiable):** Identity switches are predicted by inter-instance *appearance* similarity in SAM2's own memory embedding space with AUC > 0.8, while trajectory crossing without appearance similarity rarely causes switches.
- **Why Important:** Predicting when tracking will fail enables selective human verification; also tells us what to fix (appearance discrimination vs motion modeling).
- **Why Possibly Novel:** VOS identity-switch analyses exist for older trackers, not for memory-attention architectures like SAM2, and not using the model's own embedding space as the predictor.
- **Minimal Experiment:** On multi-instance VOS clips, log every switch event; for each, compute memory-embedding similarity and trajectory-crossing features; fit a logistic model and compare feature importance.
- **Main Risk:** Switch events may be too rare in standard benchmarks; may need a purpose-built similar-instance clip set.

### IDEA-A-0006
- **One-sentence idea:** Test the hypothesis that SAM's failure on amorphous matter (smoke, clouds, water, flames) is a smooth function of boundary gradient energy going to zero, not a categorical "class" failure.
- **Problem:** SAM fails on smoke/fire, but we don't know if this is a continuous physics-driven failure (no boundary → no mask) or a semantic gap (never saw the category).
- **Core Hypothesis (falsifiable):** Across amorphous and solid objects alike, SAM IoU is monotonically predicted by a single scalar — integrated boundary contrast — and amorphous categories lie on the *same* curve as solid objects (falsified if amorphous classes fall systematically below the curve).
- **Why Important:** If failure is purely contrast-driven, cheap contrast-enhancing preprocessing could fix smoke/fire segmentation; if categorical, retraining is needed.
- **Why Possibly Novel:** Unifies "SAM fails on X" reports under one measurable physical variable with a testable single-curve prediction.
- **Minimal Experiment:** Assemble 1k masks spanning smoke/fog/fire/water/glass/solid objects with computed boundary contrast; plot IoU vs contrast per category; test category offsets with ANCOVA.
- **Main Risk:** Ground-truth masks for amorphous matter are themselves ill-defined (see IDEA-A-0121), which injects label noise into the dependent variable.

### IDEA-A-0007
- **One-sentence idea:** Determine how much of SAM's mask granularity behavior is an imprint of the SA-1B annotation *protocol* rather than a property of images.
- **Problem:** SA-1B was built with a specific interactive annotation pipeline; SAM's notion of "a mask" may encode that pipeline's policy (e.g., preferred granularity, hole handling) rather than natural object statistics.
- **Core Hypothesis (falsifiable):** SAM's everything-mode mask-size and mask-count distributions match SA-1B's distributions far more closely than those of independently annotated datasets (ADE20K, LVIS) on the *same images*, indicating protocol imprinting.
- **Why Important:** Protocol imprinting means SAM is not a neutral "segment anything" tool but an SA-1B-policy replicator — critical for anyone using SAM masks as ground truth.
- **Why Possibly Novel:** Dataset bias is much-discussed for classes; annotation-*protocol* bias on mask granularity for a foundation model has not been quantified.
- **Minimal Experiment:** Run SAM everything-mode on images that have both LVIS and (proxy) SA-1B-style annotations; compare granularity histograms (masks per image, mask-size distribution, holes per mask) across the three sources.
- **Main Risk:** Distribution match could reflect image-domain overlap rather than protocol; control by using identical images across annotation sources.

### IDEA-A-0008
- **One-sentence idea:** Map SAM's IoU as a continuous function of click position within the object and identify whether the medial axis, not the centroid, is the optimal prompt locus.
- **Problem:** Papers simulate clicks at object centers, but real objects (crescents, rings, tubes) have centroids outside the mask, and there is no map of prompt-position sensitivity.
- **Core Hypothesis (falsifiable):** IoU as a function of click position is well-approximated by normalized distance-to-medial-axis, and centroid clicking underperforms medial-axis clicking by >10 IoU on non-convex objects.
- **Why Important:** Every interactive-segmentation evaluation and every auto-prompting pipeline depends on click placement; a validated placement law improves both.
- **Why Possibly Novel:** Click simulation strategies exist, but a dense spatial sensitivity *map* with a geometric predictive law has not been published for SAM.
- **Minimal Experiment:** For 200 objects spanning convexity levels, evaluate SAM at every grid position inside the GT mask; fit IoU(position) against distance-to-boundary and distance-to-medial-axis features.
- **Main Risk:** Result may be strongly resolution-dependent; must replicate across scales.

### IDEA-A-0009
- **One-sentence idea:** Determine whether SAM's negative clicks act as hard spatial constraints or merely re-rank among masks it already considered.
- **Problem:** Negative clicks are assumed to "carve out" regions, but SAM might only switch among a small internal hypothesis set, explaining why some errors are un-correctable by any number of negative clicks.
- **Core Hypothesis (falsifiable):** There exists a measurable set of errors (est. >20% of failure cases) where no sequence of ≤10 negative clicks changes the erroneous region's inclusion, and these cases are predicted by low diversity among SAM's latent multimask outputs.
- **Why Important:** Defines a hard ceiling for interactive correction with frozen SAM — practitioners need to know when clicking more is futile.
- **Why Possibly Novel:** Interactive segmentation work counts clicks-to-target; nobody has characterized the *unreachable set* of SAM corrections or tied it to hypothesis-set collapse.
- **Minimal Experiment:** On failure cases, run exhaustive greedy negative-click search (oracle placement); measure fraction of irrecoverable errors and correlate with multimask diversity (pairwise IoU of the 3 outputs).
- **Main Risk:** Greedy oracle search may miss recoverable sequences; mitigate with beam search on a subset.

### IDEA-A-0010
- **One-sentence idea:** Quantify SAM's topological errors on thin branching structures (vessels, wires, branches) using Betti-number mismatch rather than IoU.
- **Problem:** SAM can score decent IoU on tubular structures while destroying connectivity (broken vessels, merged wires), and pixel metrics cannot see it.
- **Core Hypothesis (falsifiable):** SAM's Betti-error (connected components + holes mismatch) on thin structures is >5× worse than a supervised U-Net at matched IoU, i.e., SAM is topologically miscalibrated relative to its pixel accuracy.
- **Why Important:** For medicine (vasculature) and infrastructure inspection, topology is the clinically/functionally relevant property, not IoU.
- **Why Possibly Novel:** Topology-aware losses exist for supervised nets; a topological audit of promptable foundation masks is missing.
- **Minimal Experiment:** Evaluate SAM (box + point prompts) vs nnU-Net on DRIVE/STARE retinal vessels and a wire/branch set; report Betti error, clDice, and IoU; compare topology-at-matched-IoU.
- **Main Risk:** SAM's 1024-px input may bottleneck thin structures trivially (resolution confound); include tiled high-res SAM as control.

### IDEA-A-0011
- **One-sentence idea:** Build the corruption-robustness profile of SAM across ImageNet-C-style corruptions and test whether prompt-based segmentation degrades differently from dense classification.
- **Problem:** Robustness benchmarks exist for classifiers, but promptable segmentation may fail differently (e.g., mask shrinkage vs class flips) and no per-corruption profile exists for SAM.
- **Core Hypothesis (falsifiable):** SAM degrades most under blur and noise (which destroy boundary gradients) but is nearly invariant to weather/color corruptions, and its degradation mode is systematic mask *shrinkage* toward high-contrast cores rather than random error.
- **Why Important:** Deployment (drones, dashcams, endoscopes) is corruption-rich; knowing the degradation *mode* enables targeted mitigation (e.g., deblurring only).
- **Why Possibly Novel:** Corruption benchmarks for promptable segmentation with degradation-mode analysis (shrinkage/expansion/fragmentation taxonomy) have not been published.
- **Minimal Experiment:** Apply 15 corruption types × 5 severities to a 1k-instance eval set; measure IoU plus a new shrinkage/fragmentation decomposition of the error.
- **Main Risk:** Synthetic corruptions may not represent real degradations (see IDEA-A-0338); add one real-corruption subset.

### IDEA-A-0012
- **One-sentence idea:** Probe whether SAM's image encoder features contain linearly decodable *semantic class* information or only geometric/boundary information.
- **Problem:** SAM was trained without semantic labels; whether its features incidentally encode semantics determines if SAM can anchor open-vocabulary pipelines or must be paired with CLIP-like models.
- **Core Hypothesis (falsifiable):** Linear probes on SAM encoder patch features achieve <50% of DINOv2's mIoU for semantic segmentation on ADE20K, while matching DINOv2 on class-agnostic boundary prediction — a double dissociation of geometry vs semantics.
- **Why Important:** Clarifies the division of labor in the now-standard "SAM + CLIP" pipelines and whether SAM-only semantic pipelines are theoretically limited.
- **Why Possibly Novel:** Individual probes exist scattered in papers; the explicit geometry-vs-semantics double dissociation between SAM and DINOv2 has not been tested cleanly.
- **Minimal Experiment:** Train linear probes for (a) semantic classes and (b) boundary/interior prediction on frozen SAM vs DINOv2 features on ADE20K; compare the 2×2 performance matrix.
- **Main Risk:** Linear probes may understate nonlinearly-encoded semantics; add a 2-layer MLP probe control.

### IDEA-A-0013
- **One-sentence idea:** Test whether SAM2's video-trained image encoder *lost* single-image segmentation quality relative to SAM1 — a modality trade-off audit.
- **Problem:** SAM2 is assumed to strictly supersede SAM1, but video training may have traded static-image boundary precision for temporal stability.
- **Core Hypothesis (falsifiable):** On a boundary-quality-weighted static benchmark (high-res, fine structures), SAM1 outperforms SAM2 by a measurable margin (>2 boundary-F points) despite SAM2's parity or superiority on region IoU.
- **Why Important:** Practitioners default to the newest model; if SAM2 regressed on fine static detail, single-image applications (matting, medical stills) should stay on SAM1 or use hybrids.
- **Why Possibly Novel:** No published head-to-head isolates *boundary-F on static fine structures* between SAM generations; release reports emphasize aggregate parity.
- **Minimal Experiment:** Evaluate SAM1 vs SAM2 (matched prompting) on DIS5K-style fine-structure images and high-res subsets; report boundary F-measure and IoU separately.
- **Main Risk:** Encoder architecture differences (ViT-H vs Hiera) confound "video training" as the cause; frame as model-level, not cause-level, claim unless ablations are possible.

### IDEA-A-0014
- **One-sentence idea:** Locate SAM's capacity bottleneck by asking whether a bigger/retrained *decoder* on frozen encoder features closes most of SAM's gap to supervised specialists.
- **Problem:** SAM pairs a huge encoder with a tiny (~4M param) decoder; it is unknown whether typical SAM failures are encoder blindness or decoder capacity limits.
- **Core Hypothesis (falsifiable):** Retraining only a 10×-larger decoder on frozen SAM encoder features recovers >60% of the gap between zero-shot SAM and a fully supervised specialist on fine-grained benchmarks; failure to recover implicates the encoder.
- **Why Important:** Directs the community's fine-tuning effort: if the decoder is the bottleneck, cheap decoder-only training beats expensive encoder PEFT.
- **Why Possibly Novel:** HQ-SAM touched decoder improvements; a systematic encoder-vs-decoder bottleneck attribution with capacity sweeps has not been done.
- **Minimal Experiment:** On 3 domains (medical, thin structures, camouflage), train decoder variants (1×, 4×, 10× capacity) on frozen features vs LoRA-tuned encoder with original decoder; compare gap closure.
- **Main Risk:** Bottleneck location likely varies by domain, complicating a single headline claim — treat per-domain attribution as the deliverable.

### IDEA-A-0015
- **One-sentence idea:** Measure whether SAM has a *granularity prior* miscalibrated to human part/whole judgments, i.e., it systematically prefers a granularity level humans don't.
- **Problem:** When prompts are ambiguous, SAM must pick a granularity; if its prior differs from the human modal choice, single-mask usage silently returns non-preferred granularity.
- **Core Hypothesis (falsifiable):** SAM's top-scored mask matches the human modal granularity choice in <60% of ambiguous prompts, with a systematic bias toward *larger* (whole-object) masks.
- **Why Important:** Auto-annotation pipelines take SAM's top mask; a systematic granularity bias propagates into every dataset built this way.
- **Why Possibly Novel:** Multimask output is known; the direction and magnitude of granularity *bias* vs human preference is unmeasured.
- **Minimal Experiment:** 500 ambiguous prompts, 15 humans choose preferred granularity from SAM's 3 masks + "none"; compare SAM's confidence ranking to human modal choice.
- **Main Risk:** Human granularity preference is context/task-dependent; fix an annotation task framing to stabilize it.

### IDEA-A-0016
- **One-sentence idea:** Audit whether SAM's predicted IoU/stability scores are *calibrated* confidence measures or merely rank-informative.
- **Problem:** Pipelines threshold SAM's predicted IoU to filter masks, implicitly assuming calibration, which has never been verified across domains.
- **Core Hypothesis (falsifiable):** SAM's predicted IoU is well-calibrated in-domain (ECE < 0.05 on COCO-like data) but overconfident by >0.15 expected calibration error on out-of-domain imagery (medical, aerial, art), and recalibration transfers poorly across domains.
- **Why Important:** Mask filtering thresholds tuned on natural images silently pass garbage masks in other domains — a hidden failure in many auto-labeling systems.
- **Why Possibly Novel:** Calibration is heavily studied for classifiers, essentially unstudied for promptable mask-quality prediction heads.
- **Minimal Experiment:** Collect (predicted IoU, actual IoU) pairs across 6 domains; plot reliability diagrams; test cross-domain transfer of isotonic recalibration.
- **Main Risk:** Actual IoU depends on GT quality, which varies by domain; use only high-quality GT subsets.

### IDEA-A-0017
- **One-sentence idea:** Chart where SAM breaks on non-photographic imagery (sketches, diagrams, maps, radar, ultrasound) and test whether failure tracks the image-statistics distance from SA-1B.
- **Problem:** "Segment anything" is used on charts, floorplans, and sensor imagery with unknown reliability, and there is no predictive account of which non-photographic domains work.
- **Core Hypothesis (falsifiable):** SAM's per-domain IoU is predicted (Spearman ρ > 0.8) by a simple domain-distance statistic (e.g., FID between domain images and SA-1B samples), implying failures are distributional, not structural.
- **Why Important:** A cheap pre-deployment "will SAM work here?" predictor would save enormous evaluation effort across applied fields.
- **Why Possibly Novel:** Domain-transfer anecdotes abound; a quantitative domain-distance → performance law for promptable segmentation is untested.
- **Minimal Experiment:** Evaluate SAM on 10 non-photographic domains with existing GT; compute FID/CMMD to a SA-1B sample; test rank correlation with mean IoU.
- **Main Risk:** FID may be a poor distance for line art; try multiple distances and report which (if any) predicts.

### IDEA-A-0018
- **One-sentence idea:** Propose clicks-to-convergence (number of interactive clicks to reach 90% IoU) as SAM's operational metric and identify the object taxonomy that *never converges*.
- **Problem:** Single-prompt IoU hides the practical cost of interactive use; some object types may be cheap to fix with clicks while others are unreachable (see IDEA-A-0009).
- **Core Hypothesis (falsifiable):** Object categories cluster into three convergence classes (fast: ≤3 clicks; slow: 4–10; non-convergent), and non-convergence is predicted by amorphous boundaries + thin topology, not by semantic rarity.
- **Why Important:** Annotation-cost planning and tool selection need convergence classes, not average IoU.
- **Why Possibly Novel:** Interactive segmentation uses NoC (number of clicks) metrics, but a taxonomy of *non-convergent* categories for foundation models and its predictors is new.
- **Minimal Experiment:** Simulated-oracle clicking on 50 categories × 40 instances; cluster convergence curves; fit predictors (boundary contrast, tubularity, size).
- **Main Risk:** Simulated clicks diverge from human behavior (see IDEA-A-0048); validate on a small human-in-the-loop subset.

### IDEA-A-0019
- **One-sentence idea:** Test whether SAM2 falsely re-identifies a *different* similar object after full occlusion exit-reentry ("phantom re-ID"), and how often this produces confidently wrong tracks.
- **Problem:** Re-detection after occlusion must choose among lookalikes; a confidently wrong re-ID is worse than a dropped track, and this failure's rate is unmeasured.
- **Core Hypothesis (falsifiable):** In scenes with ≥3 lookalike instances, SAM2 re-attaches to the wrong instance in >25% of full-occlusion reentries, and its internal object-score does not distinguish correct from phantom re-IDs (AUC < 0.6).
- **Why Important:** Confidence-blind identity errors are the worst failure class for surveillance, surgery, and wildlife tracking applications.
- **Why Possibly Novel:** Tracking literature studies re-ID, but SAM2's promptable-memory formulation and its score's (un)informativeness about identity errors is uncharacterized.
- **Minimal Experiment:** Curate/synthesize 200 exit-reentry events among lookalikes; measure wrong-reattachment rate and score AUC for correct vs phantom.
- **Main Risk:** Curating enough natural exit-reentry events is laborious; synthetic scene composition may be needed with realism checks.

### IDEA-A-0020
- **One-sentence idea:** Quantify what SAM's fixed 1024×1024 input destroys, by comparing native-resize vs overlap-tiling on megapixel imagery as a function of object scale.
- **Problem:** Everyone resizes to 1024; for gigapixel/aerial/histology images this throws away small objects, but the size-dependent loss and the tiling trade-off (seams, context loss) lack a quantitative map.
- **Core Hypothesis (falsifiable):** There is a crossover object size (predicted ≈40 px at native resolution) below which tiling beats resizing despite context loss, and above which resizing wins; the crossover is stable across domains when measured in patches.
- **Why Important:** A validated resize-vs-tile decision rule affects every high-resolution SAM deployment (satellite, pathology, industrial inspection).
- **Why Possibly Novel:** Tiling is folk practice; the crossover law and its domain stability have not been established.
- **Minimal Experiment:** On aerial + histology + street megapixel sets, sweep object-size bins × {resize, tile with 4 overlap settings}; locate crossovers; test patch-normalized stability.
- **Main Risk:** Optimal tiling interacts with prompt placement across tiles; must fix a principled prompt-propagation protocol first.

### IDEA-A-0021
- **One-sentence idea:** Determine whether SAM's masks rely on chromatic information at all, via hue-rotation and grayscale interventions ("does SAM see color or only luminance structure?").
- **Problem:** For domains that are effectively monochrome (IR, many medical modalities), it matters whether SAM's competence depends on color statistics; this basic invariance is unmeasured.
- **Core Hypothesis (falsifiable):** SAM's IoU drops <2 points under full hue rotation and grayscale conversion on natural images, i.e., SAM is functionally achromatic — falsified if color-defined boundaries (equiluminant color edges) segment well, which would prove chromatic sensitivity.
- **Why Important:** Justifies (or refutes) transferring SAM to monochrome sensor domains without color-specific adaptation, and clarifies what boundary signal SAM uses.
- **Why Possibly Novel:** Channel-ablation studies exist for classifiers; the promptable-mask analog with equiluminant-edge stimuli is new.
- **Minimal Experiment:** Evaluate SAM under {original, grayscale, hue-rotated, equiluminant color-edge stimuli}; compare IoU deltas; the equiluminant set is the critical discriminating condition.
- **Main Risk:** Constructing properly equiluminant stimuli requires display-calibration assumptions; approximate with L*-matched synthetic images.

### IDEA-A-0022
- **One-sentence idea:** Use the disagreement between SAM's box-prompt and point-prompt outputs on the same object as a free, label-less error detector.
- **Problem:** Deployed SAM has no ground truth; a self-contained signal that flags likely-wrong masks would enable selective human review, and prompt-type disagreement is a candidate nobody has validated.
- **Core Hypothesis (falsifiable):** Box-vs-point mask disagreement (1 − IoU between the two outputs) predicts actual error with AUROC > 0.85, outperforming SAM's own predicted-IoU score as a failure detector.
- **Why Important:** A zero-cost failure detector changes auto-labeling economics: route only disagreeing cases to humans.
- **Why Possibly Novel:** Ensemble disagreement is classic, but *cross-prompt-type* self-disagreement as a calibrated failure signal for promptable models is unexplored.
- **Minimal Experiment:** On 5 datasets with GT, compute disagreement vs true IoU; compare AUROC against predicted-IoU and multimask-diversity baselines.
- **Main Risk:** Both prompt types may fail identically on hard cases (correlated errors), capping detector recall.

### IDEA-A-0023
- **One-sentence idea:** Run a controlled head-to-head of frozen SAM vs DINOv2 vs CLIP encoders as *dense feature extractors* under identical decoders to test the claim that SAM features are strong general-purpose dense features.
- **Problem:** SAM's encoder is often reused as a feature backbone on the assumption that segmentation pretraining ⇒ good dense features, but controlled comparisons under matched decoders/training are missing.
- **Core Hypothesis (falsifiable):** Under identical decoder + training budget, DINOv2 beats SAM's encoder on ≥4 of 5 dense tasks (semantic seg, depth, normals, correspondence, detection), i.e., SAM's encoder is specialized, not general.
- **Why Important:** Prevents the community from defaulting to SAM features where they are inferior; informs backbone choice with evidence, not brand.
- **Why Possibly Novel:** Partial comparisons exist in probing papers; the matched-decoder matched-budget dense-task matrix centered on this specific claim is not established.
- **Minimal Experiment:** Frozen encoders + identical DPT-style decoder, same schedule, 5 tasks, 3 seeds; report the full matrix with CIs.
- **Main Risk:** Decoder choice may favor one encoder's feature geometry; replicate with 2 decoder types.

### IDEA-A-0024
- **One-sentence idea:** Identify *what is lost first* when SAM is distilled to efficient variants (MobileSAM-class models): test the hypothesis that boundary precision and small objects degrade before region IoU.
- **Problem:** Efficient SAM variants report near-parity on aggregate metrics, but deployment reports suggest fine-detail loss; the structure of distillation loss is uncharacterized.
- **Core Hypothesis (falsifiable):** At matched aggregate IoU (within 1 point), distilled variants lose >5 points boundary-F and >8 points small-object IoU relative to teacher SAM — aggregate parity masks structured degradation.
- **Why Important:** Edge deployment decisions rely on aggregate parity claims; structured loss means unfitness for exactly the fine-grained use cases where SAM adds value.
- **Why Possibly Novel:** Distillation papers report means; the size- and boundary-stratified loss profile of segmentation distillation is unexamined.
- **Minimal Experiment:** Evaluate teacher vs 3 efficient variants on size-stratified + boundary-F metrics on identical prompts; report degradation profiles.
- **Main Risk:** Different efficient variants use different training data, confounding "distillation" as the cause; report per-model, claim the pattern only if consistent.

### IDEA-A-0025
- **One-sentence idea:** Test whether SAM performs *modal* (visible-region) or partially *amodal* (whole-object) segmentation when objects are partially occluded — and whether this is prompt-dependent.
- **Problem:** Downstream users assume SAM returns visible pixels only, but anecdotes show occasional occluder-crossing masks; the modal/amodal behavior boundary is unmapped.
- **Core Hypothesis (falsifiable):** SAM is strictly modal for point prompts (>95% of masks exclude occluded regions) but partially amodal for box prompts that span occluders, meaning output semantics silently change with prompt type.
- **Why Important:** Modal/amodal ambiguity corrupts measurement applications (sizing, counting coverage) that assume one or the other.
- **Why Possibly Novel:** Amodal segmentation is a known task; the *unintended* amodal behavior of promptable models as a function of prompt type is undocumented.
- **Minimal Experiment:** Use amodal datasets (with visible+occluded GT); prompt SAM both ways; measure occluded-region inclusion rate per prompt type.
- **Main Risk:** Occluded-region inclusion may be sporadic and dataset-dependent; needs multiple amodal benchmarks.

### IDEA-A-0026
- **One-sentence idea:** Characterize SAM2 accuracy as a function of memory-bank size and test for non-monotonicity ("more memory can hurt" via stale-feature interference).
- **Problem:** SAM2's memory length is a fixed engineering choice; whether longer memory monotonically helps, saturates, or *hurts* (stale appearance after object deformation) is unknown.
- **Core Hypothesis (falsifiable):** For deformable objects, accuracy vs memory-length is non-monotonic with an interior optimum, while for rigid objects it saturates monotonically — memory interference is deformation-dependent.
- **Why Important:** A deformation-adaptive memory policy could improve video segmentation for surgery/animals at zero training cost.
- **Why Possibly Novel:** Memory ablations exist as engineering choices; the deformation-conditioned interference hypothesis and its adaptive implication are new.
- **Minimal Experiment:** Sweep memory sizes on rigid vs deformable VOS subsets; plot accuracy curves per deformation level (quantified by optical-flow non-rigidity).
- **Main Risk:** Non-monotonicity may be small relative to seed/clip variance; needs many clips for power.

### IDEA-A-0027
- **One-sentence idea:** Audit SAM's handling of objects with holes (donuts, cups' handles, fences) and test the hypothesis of a closed-contour bias that systematically fills genus>0 regions.
- **Problem:** Masks with holes are topologically harder; if SAM's decoder has a filled-contour prior, hole-carrying classes get silently corrupted, which IoU barely registers for thin-rimmed objects.
- **Core Hypothesis (falsifiable):** SAM incorrectly fills >40% of ground-truth holes larger than 100 px² on a genus>0 object set, and negative clicks inside holes fix fewer than half of these (connecting to the unreachable-set idea IDEA-A-0009).
- **Why Important:** Robotics grasping and manipulation care about holes (handles!); a systematic fill-bias is an actionable, fixable defect.
- **Why Possibly Novel:** No published genus-stratified evaluation of promptable segmentation exists.
- **Minimal Experiment:** Build a 300-object genus≥1 evaluation set from existing datasets; measure hole preservation rate, with/without corrective clicks.
- **Main Risk:** GT hole annotation quality is inconsistent across source datasets; manual verification pass required.

### IDEA-A-0028
- **One-sentence idea:** Establish when prompt-jitter ensembling (averaging masks from perturbed prompts) helps vs actively hurts SAM, with a predictive rule.
- **Problem:** Prompt ensembling is casually used to "stabilize" SAM outputs, but averaging across an ambiguity boundary (part vs whole) should produce blurred nonsense; nobody has mapped help-vs-hurt regimes.
- **Core Hypothesis (falsifiable):** Ensembling improves IoU when jittered prompts agree (multimodal-free regime) but *reduces* IoU by >5 points when prompt jitter crosses ambiguity boundaries; a bimodality test on the mask set predicts which regime applies with >80% accuracy.
- **Why Important:** Turns a folk trick into a conditional rule, preventing silent quality loss in auto-labeling pipelines.
- **Why Possibly Novel:** TTA-hurts phenomena are known for classification; the ambiguity-crossing mechanism and its detectability for promptable masks are unstudied.
- **Minimal Experiment:** On 1k objects, run 9-point jitter ensembles; stratify outcomes by a mask-set bimodality statistic; validate the predictive rule out-of-sample.
- **Main Risk:** The bimodality statistic must be threshold-free to generalize; may need rank-based formulations.

### IDEA-A-0029
- **One-sentence idea:** Measure the annotation feedback loop: do datasets annotated *with SAM assistance* systematically over-represent SAM-easy boundaries, biasing all models trained on them?
- **Problem:** SAM is now embedded in annotation tools; if annotators accept SAM proposals preferentially where SAM is good, new datasets inherit SAM's competence profile — an ecosystem-level circularity nobody has quantified.
- **Core Hypothesis (falsifiable):** Datasets built with SAM-assisted pipelines show measurably higher agreement-with-SAM (by >10 IoU) than scratch-annotated datasets on matched content, and models trained on the former overestimate their real-world boundary quality by a corresponding margin.
- **Why Important:** This is dataset-generation contamination — it corrupts the community's future ground truth and inflates all downstream progress metrics.
- **Why Possibly Novel:** Model-assisted annotation bias has been raised conceptually; a quantitative two-condition annotation study for segmentation is missing.
- **Minimal Experiment:** Annotate the same 500 images two ways (SAM-assisted vs scratch, professional annotators); compare boundary statistics, agreement-with-SAM, and downstream model rankings trained on each.
- **Main Risk:** Annotator skill variance may swamp the assistance effect; use within-annotator crossover design.

### IDEA-A-0030
- **One-sentence idea:** Learn a lightweight per-instance failure predictor for SAM from its own internal signals (encoder features, multimask diversity, predicted IoU) and test whether failure is predictable *before* it happens.
- **Problem:** Selective prediction for promptable segmentation barely exists: we cannot currently say, pre-hoc, "SAM will fail on this prompt," which blocks safe automation.
- **Core Hypothesis (falsifiable):** A gradient-free probe on SAM's internal signals predicts per-instance IoU with Spearman ρ > 0.75 across held-out *domains*, substantially beating predicted-IoU alone (ρ ≈ 0.5, per IDEA-A-0016's expected miscalibration).
- **Why Important:** A domain-general failure predictor converts SAM from a demo tool into a component with a safety contract.
- **Why Possibly Novel:** Failure prediction exists for classification; a cross-domain-validated, internal-signal-based mask-quality predictor for SAM is new.
- **Minimal Experiment:** Train the probe on 4 domains, test on 3 held-out domains; report cross-domain ρ and risk-coverage curves vs baselines.
- **Main Risk:** Probe may latch onto domain identity rather than instance difficulty; enforce domain-held-out evaluation strictly.

---

## Cluster 2 — Prompt Sensitivity as a Scientific Object (IDEA-A-0031 … 0050)

### IDEA-A-0031
- **One-sentence idea:** Quantify the variance of open-vocabulary segmentation performance across semantically equivalent text prompts ("paraphrase variance") as a first-class model property.
- **Problem:** Open-vocab segmentation papers report one number per class name, but "dog"/"a dog"/"canine" can yield different masks; the magnitude and structure of paraphrase variance is unreported.
- **Core Hypothesis (falsifiable):** Paraphrase variance in mIoU exceeds the typical reported SOTA gap (1–2 points) for >30% of classes on ADE20K/Cityscapes open-vocab evaluations, meaning many published rankings are within prompt noise.
- **Why Important:** If rankings flip under paraphrases, the field's leaderboard conclusions are partially artifacts of prompt selection.
- **Why Possibly Novel:** Prompt sensitivity is studied for LLMs and classification; a systematic paraphrase-variance audit for *dense* prediction is missing.
- **Minimal Experiment:** For 3 open-vocab segmentation models, evaluate 10 human-written paraphrases per class on 2 benchmarks; report per-class variance and ranking stability under prompt resampling.
- **Main Risk:** Paraphrase set construction itself biases results; use multiple independent paraphrase authors.

### IDEA-A-0032
- **One-sentence idea:** Test whether multi-class open-vocabulary segmentation depends on the *order* and *composition* of the class-name list (context effects in the text encoder or softmax competition).
- **Problem:** Open-vocab models score each pixel against a class list; whether adding/removing/reordering unrelated classes changes masks for a fixed class is unknown but assumed to be "no."
- **Core Hypothesis (falsifiable):** Adding 20 distractor class names changes per-class IoU by >3 points for at least a quarter of classes (competition effect), while pure reordering changes nothing (order-invariance holds).
- **Why Important:** Real deployments use user-defined vocabularies; if vocabulary composition shifts masks, the same model gives different "ground truth" depending on an arbitrary list.
- **Why Possibly Novel:** Vocabulary-composition sensitivity of dense predictions has not been isolated as an experimental variable.
- **Minimal Experiment:** Fix images and target classes; sweep vocabulary size/composition/order; measure per-class IoU deltas on 2 models.
- **Main Risk:** Softmax-vs-sigmoid scoring differences across models may make results model-specific; test both scoring styles.

### IDEA-A-0033
- **One-sentence idea:** Map the relationship between lexical specificity of the prompt ("vehicle" → "car" → "sedan" → "2012 Toyota Camry") and segmentation quality, testing for a non-monotonic optimum.
- **Problem:** Users assume more specific prompts are better; but rare specific terms are poorly represented in text encoders, suggesting an interior optimum of specificity.
- **Core Hypothesis (falsifiable):** Segmentation IoU vs specificity level is inverse-U shaped, with the optimum at basic-level categories (in the Rosch sense), and the drop for over-specific prompts correlates with term frequency in pretraining corpora.
- **Why Important:** Gives users a principled prompting rule and connects cognitive "basic-level" theory to VLM behavior.
- **Why Possibly Novel:** Basic-level effects are known in psychology and classification; their existence in dense prediction and the frequency-mediated mechanism are untested.
- **Minimal Experiment:** Build 4-level specificity chains for 50 categories; evaluate 3 open-vocab segmenters; regress IoU against level and (proxy) term frequency.
- **Main Risk:** Specificity confounds with visual homogeneity of the category; control by fixing the evaluated instance set across levels.

### IDEA-A-0034
- **One-sentence idea:** Test whether explicitly naming background/distractor classes as "negative prompts" reliably improves open-vocabulary segmentation, or only helps when negatives are visually confusable with targets.
- **Problem:** Adding background class names is folk practice with contradictory anecdotes; the conditions under which it helps are uncharacterized.
- **Core Hypothesis (falsifiable):** Negative prompts improve target IoU only when the named negative is visually confusable with the target (embedding similarity above a threshold); adding non-confusable negatives has zero or negative effect.
- **Why Important:** Converts an unreliable trick into a conditional rule that can be automated (auto-select negatives by confusability).
- **Why Possibly Novel:** Negative prompting is used ad hoc; a confusability-conditioned law with automated negative selection is new for segmentation.
- **Minimal Experiment:** For 40 target classes, add negatives sampled at controlled embedding-similarity levels; measure IoU response curves vs similarity.
- **Main Risk:** Embedding similarity may poorly proxy visual confusability; validate with a confusion-matrix-based similarity measure.

### IDEA-A-0035
- **One-sentence idea:** Test whether learned soft prompts (CoOp-style) encode transferable semantics or dataset-specific statistics, by transplanting them across backbones and datasets.
- **Problem:** Prompt learning reports gains, but if learned vectors are dataset fingerprints rather than semantic refinements, they should fail to transfer in specific, predictable ways.
- **Core Hypothesis (falsifiable):** Learned prompts transfer across *datasets* with the same backbone (retaining >70% of their gain) but not across *backbones* on the same dataset (<20% retained), indicating they encode backbone-specific feature-space corrections, not semantics.
- **Why Important:** Clarifies what prompt learning actually learns, which determines whether prompt libraries can be shared and reused across models.
- **Why Possibly Novel:** CoOp transfer has been studied across datasets; the backbone-transplant dissociation (semantics vs feature-space correction) is not established.
- **Minimal Experiment:** Train CoOp prompts on 3 datasets × 3 CLIP variants; evaluate the full transplant matrix; compare gain retention across the two transfer axes.
- **Main Risk:** Prompt dimensionality differs across backbones; needs a principled mapping (e.g., train linear adapters) that could itself confound.

### IDEA-A-0036
- **One-sentence idea:** Use prompt-paraphrase output variance as a zero-label out-of-distribution and error detector for open-vocabulary dense prediction.
- **Problem:** Dense OOD detection typically needs logits or training; paraphrase-variance is a free test-time signal whose diagnostic value is unknown.
- **Core Hypothesis (falsifiable):** Per-pixel variance across 8 paraphrase prompts predicts per-pixel errors with AUROC > 0.8, and image-level variance flags OOD images better than max-softmax baselines.
- **Why Important:** A free, architecture-agnostic reliability signal for deployed open-vocab systems.
- **Why Possibly Novel:** Ensemble-disagreement is classic; *prompt-side* ensembling as a calibrated dense error detector has not been validated.
- **Minimal Experiment:** On in-domain + corrupted + novel-class splits, compute paraphrase-variance maps; report pixel-level error AUROC and image-level OOD AUROC vs baselines.
- **Main Risk:** Variance may saturate on genuinely ambiguous but correct regions (boundary pixels), inflating false positives; evaluate interior and boundary separately.

### IDEA-A-0037
- **One-sentence idea:** Compare the information content of one visual exemplar prompt vs one text prompt for segmentation, in bits, via controlled performance-matching.
- **Problem:** Text and exemplar prompting are treated as interchangeable interfaces, but their information content for a segmentation task has never been placed on a common scale.
- **Core Hypothesis (falsifiable):** One masked visual exemplar is worth k text attributes where k>5 for fine-grained categories but k<1 for common categories with canonical names — i.e., the text/exemplar exchange rate is category-frequency-dependent.
- **Why Important:** Guides interface design for annotation tools: when to ask users for words vs clicks vs examples.
- **Why Possibly Novel:** "Which prompt modality is better" comparisons exist per-benchmark; an exchange-rate formulation conditioned on category frequency is new.
- **Minimal Experiment:** On models supporting both (e.g., SEEM-class, in-context models like SegGPT), match performance by incrementally enriching text prompts until they equal one-exemplar performance; record required attribute counts by category frequency.
- **Main Risk:** Exchange rate depends on the specific model's training mixture; replicate on ≥2 model families before claiming generality.

### IDEA-A-0038
- **One-sentence idea:** Look for spatial aliasing artifacts in SAM's prompt encoding — do click prompts at certain pixel positions (relative to the patch grid) systematically yield worse masks?
- **Problem:** SAM encodes clicks with positional encodings tied to a discrete feature grid; sub-patch position could create a periodic accuracy pattern nobody has looked for.
- **Core Hypothesis (falsifiable):** Mask IoU shows a statistically significant periodic dependence (amplitude >1 IoU point) on click position modulo the 16-px patch grid, maximal when clicks fall on patch boundaries.
- **Why Important:** Even a small periodic artifact matters for automated dense prompting (grid prompting hits patch boundaries systematically) and reveals interpolation defects in prompt encoding.
- **Why Possibly Novel:** Aliasing is studied for downsampling in CNNs; prompt-encoding aliasing in promptable transformers is unexamined.
- **Minimal Experiment:** For 500 objects, place clicks at 16×16 sub-patch offsets around fixed semantic locations; average IoU by offset phase; test periodicity with a Fourier test.
- **Main Risk:** Effect size may be real but tiny (<0.3 IoU), making it statistically detectable yet practically irrelevant — report effect size with CIs, not just p-values.

### IDEA-A-0039
- **One-sentence idea:** Test whether prompt tuning ever exceeds the expressivity of a linear reweighting of frozen features — i.e., is prompt tuning secretly a linear probe?
- **Problem:** Prompt tuning is described as steering internal computation, but for frozen encoders its effective function class may be no richer than linear feature recombination, which would demystify (and commoditize) it.
- **Core Hypothesis (falsifiable):** For dense prediction with frozen ViTs, prompt tuning's accuracy is matched (±1 point) by a linear head over frozen multi-layer features on ≥80% of task/dataset combinations; cases where prompt tuning wins are concentrated where attention *pattern* changes are required (verified by attention-map divergence).
- **Why Important:** If equivalence holds broadly, practitioners can replace fragile prompt optimization with closed-form probes; where it fails identifies prompting's real value.
- **Why Possibly Novel:** Theory papers discuss prompt expressivity abstractly; a dense-prediction empirical equivalence test with an attention-divergence criterion is new.
- **Minimal Experiment:** On 6 segmentation datasets, compare visual prompt tuning vs multi-layer linear/MLP probes at matched parameter counts; measure attention-map divergence in the winner cases.
- **Main Risk:** "Matched parameter count" is ambiguous between methods; report full parameter-performance curves instead of single points.

### IDEA-A-0040
- **One-sentence idea:** Establish whether per-class prompt-specific temperature calibration fixes the systematic confidence imbalance across text prompts in open-vocabulary segmentation.
- **Problem:** Different class-name prompts produce logits on different scales (frequency and length effects), so a single softmax temperature miscalibrates some classes; this prompt-conditional miscalibration is unquantified.
- **Core Hypothesis (falsifiable):** Per-prompt temperature scaling reduces per-class ECE by >50% relative to global temperature on open-vocab segmentation, and learned temperatures correlate with prompt token frequency.
- **Why Important:** Calibrated per-class confidence is prerequisite for using open-vocab segmenters in risk-sensitive filtering pipelines.
- **Why Possibly Novel:** Temperature scaling is standard; its prompt-conditional variant and the frequency correlation for dense predictions are unexplored.
- **Minimal Experiment:** Fit global vs per-prompt temperatures on validation pixels; compare ECE per class; regress temperature against prompt frequency statistics.
- **Main Risk:** Per-prompt calibration may overfit rare classes' small pixel counts; use hierarchical shrinkage.

### IDEA-A-0041
- **One-sentence idea:** Test whether chain-of-thought style reasoning text actually changes *where* VLMs ground (attention/mask placement) or only changes the verbal rationale while grounding stays fixed.
- **Problem:** Reasoning-segmentation systems assume intermediate reasoning improves localization, but reasoning could be post-hoc rationalization with grounding determined by the visual pathway alone.
- **Core Hypothesis (falsifiable):** For referring segmentation with reasoning-capable VLMs, forcing incorrect-but-plausible reasoning chains changes final masks in <15% of cases — grounding is causally insensitive to the reasoning text.
- **Why Important:** If grounding ignores reasoning, "reasoning segmentation" marketing is misleading and the real bottleneck is elsewhere.
- **Why Possibly Novel:** CoT faithfulness is studied for QA; a causal intervention on reasoning chains with *mask output* as the dependent variable is new.
- **Minimal Experiment:** On referring-segmentation cases requiring inference, inject correct vs subtly wrong reasoning prefixes; measure mask-change rate and accuracy under each condition.
- **Main Risk:** Injected reasoning may be off-distribution for the model, causing degenerate behavior unrelated to faithfulness; include fluency-matched controls.

### IDEA-A-0042
- **One-sentence idea:** Stratify multilingual prompt performance for CLIP-based segmentation by language typology and script to locate where "multilingual" claims break for dense tasks.
- **Problem:** Multilingual CLIP variants claim broad coverage, but dense-prediction performance per language is unreported; users worldwide prompt in their own languages with unknown reliability.
- **Core Hypothesis (falsifiable):** Dense-task degradation vs English correlates primarily with pretraining text volume per language, not typological distance; morphologically rich languages show additional degradation only for compound category names.
- **Why Important:** Equity of access: quantifies who is underserved by current open-vocab tools and why.
- **Why Possibly Novel:** Multilingual audits exist for retrieval/classification; segmentation-level multilingual audits with typology analysis are missing.
- **Minimal Experiment:** Translate a 60-class vocabulary into 15 languages (verified by native speakers); evaluate 2 multilingual open-vocab segmenters; regress degradation on corpus-volume and typology features.
- **Main Risk:** Translation quality itself varies; use back-translation checks and multiple translators.

### IDEA-A-0043
- **One-sentence idea:** Isolate the effect of prompt *length* (token count) from prompt *content* on dense prediction quality, testing the hypothesis of a content-independent length effect.
- **Problem:** Template studies confound length with content; if padding a prompt with semantically empty tokens changes masks, prompt engineering conclusions are partly artifacts of length.
- **Core Hypothesis (falsifiable):** Adding neutral filler tokens ("a photo of a … in a scene, shown clearly") changes per-class IoU systematically (|Δ|>1 point for >30% of classes) even when fillers carry no class-relevant semantics, revealing a pure length/attention-dilution effect.
- **Why Important:** Separates real prompt semantics from tokenization mechanics — foundational hygiene for all prompt-based dense prediction research.
- **Why Possibly Novel:** Length effects are reported for LLM prompting; controlled length-vs-content dissociation for segmentation prompts is not.
- **Minimal Experiment:** Factorial design: 5 content variants × 4 length paddings across 40 classes and 2 models; two-way ANOVA on IoU.
- **Main Risk:** No filler is perfectly "neutral"; use several unrelated filler families and check consistency.

### IDEA-A-0044
- **One-sentence idea:** Deconstruct the classic 80-template CLIP prompt ensemble: identify how few templates capture the full ensemble benefit for dense tasks and what property makes a template matter.
- **Problem:** The 80-template ensemble (from the CLIP paper) is cargo-culted into segmentation pipelines at 80× embedding cost without knowing which templates do the work.
- **Core Hypothesis (falsifiable):** Greedy selection finds ≤5 templates within 0.3 mIoU of the full-80 ensemble on segmentation benchmarks, and marginal template value is predicted by embedding-space diversity, not by template plausibility.
- **Why Important:** 16× cost reduction for open-vocab systems plus a principled theory of template value.
- **Why Possibly Novel:** Template pruning was explored for classification; dense-task template attribution and the diversity-predicts-value law are new.
- **Minimal Experiment:** Greedy forward selection of templates on 2 open-vocab segmenters; regress marginal gains on embedding diversity metrics; validate the top-5 set across datasets.
- **Main Risk:** Optimal subsets may be dataset-specific; the cross-dataset validation is the load-bearing part of the design.

### IDEA-A-0045
- **One-sentence idea:** Determine whether prompt sensitivity shrinks, persists, or *grows* with model scale in vision-language dense prediction.
- **Problem:** A common assumption holds that scaling smooths prompt sensitivity; for dense outputs this is untested, and sharper decision boundaries in bigger models could amplify sensitivity instead.
- **Core Hypothesis (falsifiable):** Paraphrase variance (per IDEA-A-0031) decreases sublinearly or not at all with model scale across a model family — falsifying the "scale fixes prompting" assumption if variance is flat or increasing.
- **Why Important:** If scale doesn't fix prompt sensitivity, robust-prompting research remains necessary regardless of scaling roadmaps.
- **Why Possibly Novel:** Scale-vs-sensitivity curves exist for LLM QA tasks; none exist for dense visual prediction.
- **Minimal Experiment:** Evaluate 3–4 sizes within one open-vocab family with the identical paraphrase battery; plot variance vs scale with bootstrap CIs.
- **Main Risk:** Few public families offer clean scale ladders for dense tasks; may require careful matching of training recipes across sizes.

### IDEA-A-0046
- **One-sentence idea:** Find the minimal textual perturbation (character/word level) that flips a segmentation output, and characterize the attack surface of text-prompted dense models.
- **Problem:** Adversarial robustness of the *text* input to dense predictors is essentially uncharted; typos and near-synonyms are natural perturbations users produce constantly.
- **Core Hypothesis (falsifiable):** For current open-vocab segmenters, a single-character typo suffices to drop target IoU by >20 points for >10% of class names, and vulnerability concentrates in low-frequency tokenizer-fragmented names.
- **Why Important:** Real users typo; a system whose masks collapse under one character is unfit for interactive deployment, and the tokenizer-fragmentation link suggests a fix.
- **Why Possibly Novel:** Text adversarial attacks target classifiers/LLMs; dense-output sensitivity to natural typos and its tokenizer-level mechanism are unstudied.
- **Minimal Experiment:** Enumerate 1-edit typos for 100 class names; measure worst-case and expected IoU drops; correlate with token fragmentation statistics.
- **Main Risk:** Distinguishing "legitimate semantic change" typos (cat→car) from benign ones requires careful filtering.

### IDEA-A-0047
- **One-sentence idea:** Audit SAM's "everything mode" grid prompting for systematic blind spots: which object statistics (size, position, contrast, crowding) does dense grid prompting miss?
- **Problem:** Everything-mode is used as if it enumerates all objects, but grid prompting + NMS has structural biases (e.g., small objects between grid points, nested objects suppressed) that are unquantified.
- **Core Hypothesis (falsifiable):** Everything-mode recall is <60% for objects smaller than the grid spacing and for nested objects (objects inside objects), while single targeted prompts recover >90% of the missed instances — the blind spot is the prompting scheme, not the model.
- **Why Important:** Auto-labeling and open-world discovery pipelines built on everything-mode inherit these blind spots as dataset biases.
- **Why Possibly Novel:** Everything-mode is treated as a solved utility; its recall structure as a function of object statistics hasn't been dissected.
- **Minimal Experiment:** On LVIS (dense annotations), measure everything-mode recall stratified by size/nesting/crowding at several grid densities; verify recoverability with oracle prompts.
- **Main Risk:** NMS parameters strongly affect results; report sensitivity across NMS settings to keep claims robust.

### IDEA-A-0048
- **One-sentence idea:** Compare real human clicking behavior against the simulated click policies used in interactive-segmentation evaluations, and measure how much benchmark rankings depend on the simulator.
- **Problem:** Interactive segmentation progress is measured with simulated clicks (center-of-error-region policies); if humans click differently, reported rankings may not predict real usability.
- **Core Hypothesis (falsifiable):** Human clicks differ systematically from simulators (earlier boundary clicks, corner preference), and at least one widely used method ordering *inverts* under real-human evaluation.
- **Why Important:** The entire interactive-segmentation subfield rests on click simulators; a ranking inversion would demand protocol reform.
- **Why Possibly Novel:** Small usability studies exist; a ranking-stability study between simulated and human protocols across modern models (including SAM) is missing.
- **Minimal Experiment:** 20 users × 200 targets × 3 models with logged clicks; compare NoC/IoU rankings vs simulator rankings; analyze click-placement distributions.
- **Main Risk:** Human study variance is high; power analysis first, within-subject design mandatory.

### IDEA-A-0049
- **One-sentence idea:** Test whether expert medical terminology or lay descriptions prompt medical VLM segmentation better — the "vocabulary register mismatch" question.
- **Problem:** Medical VLMs are prompted with expert terms ("pneumothorax") though their web-scale pretraining likely contains far more lay language ("collapsed lung"); the optimal register is unknown.
- **Core Hypothesis (falsifiable):** For general-domain VLMs applied to medical grounding, lay-term prompts outperform expert terms by >5 IoU on average, and the gap reverses for models pretrained on biomedical literature (PubMed-scale corpora).
- **Why Important:** A free performance lever for medical VLM deployment, plus a diagnostic of what medical knowledge the text tower actually holds.
- **Why Possibly Novel:** Register/terminology effects on *grounding* (not QA) in medical VLMs are unmeasured.
- **Minimal Experiment:** Build expert/lay prompt pairs for 30 findings; evaluate grounding IoU for 2 general and 2 biomedical VLMs; test the interaction effect.
- **Main Risk:** Expert/lay pairs may differ in specificity, not just register; control for description length and specificity.

### IDEA-A-0050
- **One-sentence idea:** Test local linearity of the prompt-to-mask mapping: does interpolating between two text-prompt embeddings produce smoothly interpolating masks, or are there discontinuous mask transitions?
- **Problem:** Prompt-embedding arithmetic is used casually (averaging templates, steering vectors) on the assumption of smoothness; the actual geometry of the prompt→mask map is unknown.
- **Core Hypothesis (falsifiable):** The prompt→mask map exhibits sharp phase transitions (mask changes >50% IoU within <5% of the interpolation path) for >30% of prompt pairs, concentrated where the interpolant crosses class decision boundaries in text space — smoothness fails in predictable places.
- **Why Important:** Determines the validity of all embedding-averaging tricks (template ensembles, prompt steering) used across open-vocab segmentation.
- **Why Possibly Novel:** Latent interpolation studies exist for generative models; the prompt-conditioned *discriminative dense output* geometry is unexplored.
- **Minimal Experiment:** Interpolate 200 prompt pairs (related and unrelated classes) in text-embedding space; segment at 20 interpolation steps; quantify transition sharpness and locate transition points.
- **Main Risk:** Interpolated embeddings are off-manifold for the text encoder; complement with token-space (discrete) interpolation paths.

---

## Cluster 3 — PEFT & Fine-Tuning Instability (IDEA-A-0051 … 0075)

### IDEA-A-0051
- **One-sentence idea:** Test whether the optimal LoRA rank for dense-prediction fine-tuning tracks a measurable "intrinsic dimension" of the task shift, giving a predictive rank-selection rule.
- **Problem:** LoRA rank is chosen by grid search per task; if optimal rank is predictable from a cheap task statistic, an expensive hyperparameter disappears.
- **Core Hypothesis (falsifiable):** The smallest rank achieving 95% of best performance correlates (ρ > 0.8) with the effective rank of the full-fine-tuning weight update (ΔW) measured on a small pilot run, across ≥10 segmentation adaptation tasks.
- **Why Important:** Rank selection is the most-tuned PEFT knob; a predictive rule saves compute for every adapter user and reveals what "task size" means.
- **Why Possibly Novel:** Intrinsic-dimension arguments motivated LoRA, but a validated *predictive* rank rule for dense tasks (not NLP classification) hasn't been established.
- **Minimal Experiment:** For 10 adaptation tasks (medical/aerial/etc. on SAM or SegFormer backbones), run short full-FT pilots to estimate ΔW effective rank; run LoRA rank sweeps; test the correlation.
- **Main Risk:** Effective rank of a short pilot may not match converged ΔW rank; check pilot-length sensitivity.

### IDEA-A-0052
- **One-sentence idea:** Quantify the bias-variance decomposition of PEFT vs full fine-tuning across random seeds: is PEFT's advantage on small data mostly variance reduction?
- **Problem:** PEFT beats full FT on small datasets, attributed vaguely to "regularization"; a formal seed-level bias-variance decomposition would identify the mechanism.
- **Core Hypothesis (falsifiable):** Across 20 seeds, PEFT shows ≥3× lower seed variance but *higher* bias (worse best-seed performance) than full FT; the mean gap is explained primarily by the variance term at n<500 images and flips sign as n grows.
- **Why Important:** If PEFT is variance reduction, alternatives like full-FT ensembles or better early stopping may dominate — the field's small-data default would change.
- **Why Possibly Novel:** Seed-level bias-variance analysis of the PEFT-vs-FT question for segmentation is missing; papers report single-seed means.
- **Minimal Experiment:** 3 datasets × 4 training sizes × {LoRA, full FT} × 20 seeds on one backbone; decompose test error; locate the crossover.
- **Main Risk:** 480 runs is compute-heavy; mitigate with small backbone + short schedules, verifying conclusions on one large configuration.

### IDEA-A-0053
- **One-sentence idea:** Determine whether LoRA on attention vs MLP layers adapts *spatial* vs *semantic* behavior respectively, using targeted probes rather than only end metrics.
- **Problem:** Placement choices (Q/K/V vs MLP) are folklore-driven; if placements have dissociable functional effects, placement can be chosen by diagnosing the needed adaptation type.
- **Core Hypothesis (falsifiable):** Attention-only LoRA changes attention maps (spatial reorganization) with minimal feature-space rotation, while MLP-only LoRA does the reverse; tasks with geometric shift (new sensor) benefit from attention placement and semantic shift (new classes) from MLP placement, with a double dissociation.
- **Why Important:** Replaces trial-and-error placement with a diagnostic rule and links PEFT design to a mechanistic account.
- **Why Possibly Novel:** Placement ablations report end metrics only; the mechanistic dissociation with matched-budget probes is new.
- **Minimal Experiment:** 2 geometric-shift + 2 semantic-shift tasks × 3 placements at matched parameter budgets; measure attention-map divergence, CKA feature rotation, and task metrics.
- **Main Risk:** Real tasks mix both shift types; include synthetic pure-shift controls.

### IDEA-A-0054
- **One-sentence idea:** When fine-tuning SAM end-to-end, measure which component (encoder, prompt encoder, decoder) changes most and which changes are *necessary*, via component-wise freezing and rewinding.
- **Problem:** SAM fine-tuning recipes freeze components based on intuition; nobody has published a component-attribution analysis of where adaptation actually lives.
- **Core Hypothesis (falsifiable):** For medical adaptation, >80% of the performance gain survives rewinding the encoder to pretrained weights (keeping the adapted decoder), indicating decoder-dominant adaptation; for sensor-shift domains (thermal), the reverse holds.
- **Why Important:** Component attribution determines the cheapest safe recipe (train 4M decoder params vs 600M encoder params) per domain type.
- **Why Possibly Novel:** Rewinding/attribution analysis (in the spirit of lottery-ticket rewinding) applied to promptable segmentation components is new.
- **Minimal Experiment:** Fine-tune SAM fully on 4 domains; rewind each component combination; report performance-retention matrix.
- **Main Risk:** Components co-adapt, so rewinding may understate a component's standalone role; complement with freeze-from-start runs.

### IDEA-A-0055
- **One-sentence idea:** Test the hypothesis that layer-wise learning-rate decay (LLRD) alone accounts for most of the reported benefit of sophisticated PEFT schemes in dense-prediction fine-tuning.
- **Problem:** Many adapter papers compare against naive full FT with uniform LR; LLRD is a strong, cheap baseline that is often missing, potentially inflating PEFT novelty claims.
- **Core Hypothesis (falsifiable):** Full FT with tuned LLRD comes within 0.5 mIoU of the best PEFT method on ≥70% of standard adaptation benchmarks, at equal compute.
- **Why Important:** If confirmed, dozens of PEFT comparisons need reinterpretation and practitioner defaults simplify dramatically.
- **Why Possibly Novel:** LLRD is known in NLP fine-tuning; its role as the hidden confounder in vision PEFT literature hasn't been isolated.
- **Minimal Experiment:** Reproduce 6 published PEFT-vs-FT comparisons for segmentation, adding LLRD-tuned full FT; report the revised gaps.
- **Main Risk:** "Tuned LLRD" requires its own search budget; account compute honestly on both sides.

### IDEA-A-0056
- **One-sentence idea:** Identify attention-entropy collapse as an early-warning signal for loss spikes and divergence during fine-tuning of pretrained ViT segmenters.
- **Problem:** Fine-tuning large ViTs on small dense datasets intermittently diverges; practitioners restart blindly because no leading indicator is established for dense fine-tuning.
- **Core Hypothesis (falsifiable):** A drop in mean attention entropy of ≥X% (calibrated on stable runs) precedes loss spikes by ≥50 steps in >80% of divergence events, enabling preemptive LR reduction that eliminates the spike without hurting final accuracy.
- **Why Important:** Converts fine-tuning stability from folklore ("lower the LR and pray") into monitored control, saving compute and enabling automation.
- **Why Possibly Novel:** Entropy collapse is documented in large-scale *pretraining*; its use as a predictive control signal in downstream dense fine-tuning is untested.
- **Minimal Experiment:** Instrument 100 fine-tuning runs with varied LRs/datasets; log attention entropy; measure lead-time and precision/recall of the early-warning rule; test the intervention.
- **Main Risk:** Divergence may have multiple causes with different signatures; taxonomy of spike types may be required first.

### IDEA-A-0057
- **One-sentence idea:** Use bias-only tuning (BitFit) as a scientific probe: which adaptation tasks are solvable by output-distribution shifts alone, and what does that imply about "domain gap"?
- **Problem:** If a domain shift is fixable by tuning only bias terms (<0.1% of parameters), the gap is a distributional offset, not a representational deficit — a diagnostic nobody applies systematically in vision.
- **Core Hypothesis (falsifiable):** BitFit recovers >80% of full-FT gains on intensity/style shifts (scanner change, weather) but <20% on structural shifts (new anatomy, new object classes), cleanly classifying shift types.
- **Why Important:** Provides a cheap, principled "gap diagnostic" that tells practitioners how much adaptation machinery a given shift actually needs.
- **Why Possibly Novel:** BitFit exists as a method; its use as a *measurement instrument* for shift taxonomy in dense prediction is new.
- **Minimal Experiment:** 8 adaptation pairs spanning style vs structural shifts; report BitFit-recovery fraction per pair; validate the two-cluster structure.
- **Main Risk:** The style/structural dichotomy may be a continuum; report recovery fraction as the primary axis rather than forcing clusters.

### IDEA-A-0058
- **One-sentence idea:** Test whether LoRA's low-rank constraint makes fine-tuned models *more* susceptible to spurious correlations than full fine-tuning under distribution shift.
- **Problem:** Low-rank updates can only reweight existing feature directions; if the strongest existing directions are spurious (backgrounds, textures), LoRA may amplify shortcut reliance — an unexamined safety issue.
- **Core Hypothesis (falsifiable):** On datasets with known spurious correlations (backgrounds correlated with class), LoRA-adapted segmenters show larger worst-group degradation than full FT at matched in-distribution accuracy.
- **Why Important:** PEFT is the default in industry; a systematic shortcut amplification would be a serious hidden cost, especially for medical deployment.
- **Why Possibly Novel:** PEFT robustness studies focus on average OOD accuracy; the spurious-direction amplification mechanism with worst-group analysis is new for dense tasks.
- **Minimal Experiment:** Construct segmentation datasets with controlled background-class correlation; adapt with LoRA vs full FT; measure worst-group IoU on decorrelated test splits.
- **Main Risk:** Constructing spurious correlations without confounds is delicate; needs several independent correlation types (texture, color, context).

### IDEA-A-0059
- **One-sentence idea:** Characterize interference when merging LoRA adapters trained on different medical imaging modalities into one model, and test whether interference is predictable from adapter subspace overlap.
- **Problem:** Institutions want one model with mergeable per-modality adapters, but LoRA merging behavior for dense tasks is anecdotal, and there is no predictive theory of when merging fails.
- **Core Hypothesis (falsifiable):** Post-merge performance drop per task correlates strongly (ρ > 0.7) with the principal-angle overlap between adapter subspaces, enabling pre-merge compatibility screening without evaluation data.
- **Why Important:** Adapter marketplaces and federated model assembly need a compatibility test; subspace overlap would be a free one.
- **Why Possibly Novel:** Model merging is studied at whole-weight level (task arithmetic); a validated subspace-overlap interference law for dense-task LoRAs is new.
- **Minimal Experiment:** Train 6 modality adapters on a shared backbone; merge all pairs; regress performance drop on subspace principal angles.
- **Main Risk:** Interference may depend on data similarity in ways subspace geometry misses; include data-similarity covariates.

### IDEA-A-0060
- **One-sentence idea:** Test whether PEFT preserves the pretrained model's calibration and uncertainty quality better than full fine-tuning — a "calibration conservation" hypothesis.
- **Problem:** Fine-tuning is known to damage calibration; whether PEFT's restricted updates protect the pretrained model's uncertainty behavior is unknown but highly consequential for risk-sensitive uses.
- **Core Hypothesis (falsifiable):** At matched task accuracy, LoRA-tuned segmenters show ≤50% of the ECE increase of fully fine-tuned ones and retain better OOD-detection AUROC, because the frozen backbone preserves the pretrained density model.
- **Why Important:** If PEFT buys calibration for free, it should be preferred for medical/safety deployments even where accuracy ties.
- **Why Possibly Novel:** PEFT papers measure accuracy; the calibration/uncertainty conservation question for dense prediction has not been posed cleanly.
- **Minimal Experiment:** 4 adaptation tasks × {LoRA, full FT} matched to equal accuracy; compare pixel-level ECE, OOD AUROC, and corruption robustness.
- **Main Risk:** Matching accuracy exactly is hard; use accuracy-calibration Pareto curves instead of point comparisons.

### IDEA-A-0061
- **One-sentence idea:** Map the dataset-size crossover where full fine-tuning overtakes PEFT for medical segmentation, and test whether the crossover is predictable from label complexity.
- **Problem:** "Use PEFT for small data" lacks a quantitative boundary; practitioners with 50–5000 images have no evidence-based rule.
- **Core Hypothesis (falsifiable):** The PEFT/full-FT crossover occurs at a dataset size proportional to output complexity (number of structures × boundary length), such that a single normalized curve predicts the crossover within 2× across ≥5 medical tasks.
- **Why Important:** A validated crossover law is an immediately usable decision rule for every clinical adaptation project.
- **Why Possibly Novel:** Scattered comparisons exist at fixed sizes; the normalized crossover law with a complexity covariate is untested.
- **Minimal Experiment:** 5 medical datasets × 6 training sizes × {LoRA, full FT}, 3 seeds; fit crossover points; regress on complexity measures.
- **Main Risk:** Crossovers may be schedule-dependent; fix compute-matched tuned schedules per cell, which is expensive but necessary.

### IDEA-A-0062
- **One-sentence idea:** Test the asymmetry hypothesis that early-layer adapters handle input-distribution shift while late-layer adapters handle label-space shift, using placement-restricted PEFT.
- **Problem:** Adapter placement across depth is chosen uniformly by default; if depth placement maps onto shift type, placement can be diagnostic and efficient.
- **Core Hypothesis (falsifiable):** Early-only adapters (first third of blocks) recover >80% of full-adapter gains on sensor/style shifts but <30% on new-class shifts; late-only adapters show the mirrored pattern.
- **Why Important:** Halves adapter parameter budgets with a principled rule, and yields a cheap probe for diagnosing what kind of shift a new dataset presents.
- **Why Possibly Novel:** Depth-restricted PEFT exists as ablation; the shift-type × depth interaction as a confirmed dissociation for segmentation is not established.
- **Minimal Experiment:** 3 style-shift + 3 label-shift tasks × {early, late, uniform} placements at matched budget; test the interaction.
- **Main Risk:** Overlaps conceptually with IDEA-A-0053 (attention vs MLP); coordinate designs to share runs and separate depth from module-type effects factorially.

### IDEA-A-0063
- **One-sentence idea:** Explain why textual/visual prompt tuning is more seed-sensitive than LoRA by testing the loss-landscape hypothesis (prompt tokens sit in flatter, more degenerate valleys).
- **Problem:** Practitioners observe prompt tuning's notorious seed variance without a mechanistic account, making fixes ad hoc (longer warmup, more restarts).
- **Core Hypothesis (falsifiable):** Prompt-tuning optima exhibit higher solution diversity (pairwise distance between converged prompts across seeds) and flatter minima than LoRA optima, and initializing prompts from embedding-space PCA of task data cuts seed variance by >50%.
- **Why Important:** A mechanistic explanation converts an unreliable method into a reliable one via principled initialization.
- **Why Possibly Novel:** Seed sensitivity is reported anecdotally; the landscape analysis plus a validated initialization fix for dense-task prompt tuning is new.
- **Minimal Experiment:** 20-seed runs of prompt tuning vs LoRA on 3 segmentation tasks; measure solution dispersion, sharpness, and the PCA-init intervention's effect.
- **Main Risk:** Landscape metrics (sharpness) are notoriously slippery; use multiple sharpness definitions and emphasize the intervention result.

### IDEA-A-0064
- **One-sentence idea:** Track the *effective rank trajectory* of LoRA updates during training and test whether premature rank collapse predicts underfitting on complex dense tasks.
- **Problem:** LoRA's nominal rank bounds capacity, but the update's effective rank during optimization may collapse far below it, silently under-using capacity on hard tasks.
- **Core Hypothesis (falsifiable):** Effective rank collapses to <30% of nominal rank within early training on most tasks, and tasks where final performance trails full FT are exactly those where effective rank saturates at the nominal bound — a capacity-starvation signature usable as an online rank-increase trigger.
- **Why Important:** Enables adaptive-rank LoRA with a principled trigger, and explains when PEFT underperforms.
- **Why Possibly Novel:** Static rank ablations are common; effective-rank *dynamics* as a capacity diagnostic for dense fine-tuning is unexplored.
- **Minimal Experiment:** Instrument LoRA training on 8 tasks; log singular-value spectra; correlate saturation events with final performance gaps; prototype the adaptive trigger.
- **Main Risk:** Effective-rank thresholds are arbitrary; pre-register the definition and report full spectra.

### IDEA-A-0065
- **One-sentence idea:** Test whether tuning only normalization parameters (norm-tuning) suffices for scanner/site adaptation in medical segmentation — the "distribution-shift-is-just-statistics" hypothesis.
- **Problem:** Cross-site medical degradation is treated with heavy machinery (UDA, full FT), yet if it is chiefly first/second-order feature-statistics mismatch, norm-parameter tuning should fix it at negligible cost.
- **Core Hypothesis (falsifiable):** Norm-only tuning with ≤50 labeled target images recovers >70% of the cross-site performance drop on ≥4 of 6 site-pairs, but fails (<20% recovery) when the shift includes protocol changes that alter anatomy visibility.
- **Why Important:** Establishes the cheapest defensible adaptation baseline for clinical deployment and cleanly separates statistical from structural site shift.
- **Why Possibly Novel:** Norm-tuning exists; a systematic medical multi-site audit with a structural-vs-statistical decomposition is missing.
- **Minimal Experiment:** 6 public multi-site pairs (prostate MRI, fundus, etc.); norm-tuning vs LoRA vs full FT at several label budgets; stratify by shift type.
- **Main Risk:** Public multi-site data confounds site with population; use datasets with documented acquisition differences.

### IDEA-A-0066
- **One-sentence idea:** Characterize half-precision (fp16/bf16) fine-tuning instabilities specific to SAM's architecture and identify which numerical component (attention logits, IoU head, mask logits) is the fragile point.
- **Problem:** Practitioners report SAM fine-tuning NaNs in mixed precision, but the failure locus is folklore; a component-level numerical audit would fix recipes community-wide.
- **Core Hypothesis (falsifiable):** Instability originates predominantly in one identifiable site (HYPOTHESIS: overflow in attention logits under relative-position bias at high resolution), and selectively keeping that site in fp32 eliminates >90% of divergent runs at negligible speed cost.
- **Why Important:** SAM fine-tuning is ubiquitous; a validated one-line numerical fix has outsized practical value.
- **Why Possibly Novel:** Mixed-precision failure analyses exist for LLMs; an architecture-specific audit for promptable segmentation models is unpublished.
- **Minimal Experiment:** Instrument activations/grad norms across 50 fine-tuning runs at varied LR; localize first-overflow site; test selective-fp32 interventions.
- **Main Risk:** Instability may be multi-causal across settings; report a fault-tree rather than a single culprit if so.

### IDEA-A-0067
- **One-sentence idea:** Test whether a single scalar — the encoder/decoder learning-rate ratio — explains most variance among PEFT/fine-tuning recipes for promptable segmentation ("the stability–plasticity dial").
- **Problem:** The recipe zoo (freeze this, adapt that) may collapse onto one underlying control variable; if so, the field is over-parameterizing a one-dimensional choice.
- **Core Hypothesis (falsifiable):** Across recipes, final target-task and retained-generality metrics are predicted (R² > 0.7) by the effective encoder:decoder LR ratio alone, with recipe identity adding <5% explained variance.
- **Why Important:** Radical simplification of fine-tuning practice; reframes recipe papers as points on a single trade-off curve.
- **Why Possibly Novel:** Nobody has regressed the recipe zoo onto a common control variable for segmentation fine-tuning.
- **Minimal Experiment:** 30 recipe configurations on 3 tasks; compute effective LR ratios; fit the one-variable model and measure residual recipe effects.
- **Main Risk:** "Effective LR ratio" for adapters requires a principled definition (update-norm ratio); pre-register it.

### IDEA-A-0068
- **One-sentence idea:** Measure whether task-specific fine-tuning destroys SAM's multimask ambiguity behavior (mode collapse of the ambiguity head) even when single-mask accuracy improves.
- **Problem:** Fine-tuning optimizes one mask per prompt, likely collapsing the 3-hypothesis diversity that makes SAM useful interactively — an unmeasured capability loss.
- **Core Hypothesis (falsifiable):** After standard single-mask fine-tuning, inter-mask diversity (pairwise 1−IoU among the 3 outputs) drops by >60% on ambiguous prompts, and interactive-correction performance (clicks-to-target on ambiguous cases) degrades even as benchmark IoU rises.
- **Why Important:** Reveals a hidden trade-off in every SAM fine-tune: benchmark gains may be paid for with interactive-usability losses.
- **Why Possibly Novel:** Forgetting is usually measured on task accuracy; forgetting of *ambiguity representation* is a new axis.
- **Minimal Experiment:** Fine-tune SAM on 3 tasks; before/after, measure multimask diversity and simulated interactive convergence on an ambiguity-rich prompt set.
- **Main Risk:** Diversity loss may be recoverable with a trivial loss term, making the finding short-lived — include that mitigation as part of the study.

### IDEA-A-0069
- **One-sentence idea:** Establish why dense-prediction fine-tuning needs different warmup schedules than classification, testing the hypothesis that decoder-encoder gradient-scale mismatch at initialization is the cause.
- **Problem:** Warmup lengths are copied across task types despite structural differences (fresh decoders inject large gradients into pretrained encoders); the mechanism lacks direct evidence.
- **Core Hypothesis (falsifiable):** The minimal safe warmup length is predicted by the initial decoder-to-encoder gradient-norm ratio (ρ > 0.8 across configurations), and pre-scaling decoder initialization to equalize gradient norms eliminates the need for warmup entirely.
- **Why Important:** Removes a tuned hyperparameter and prevents silent encoder damage in the first 100 steps of every dense fine-tune.
- **Why Possibly Novel:** Warmup theory exists for from-scratch training; the pretrained-encoder/fresh-decoder interaction for dense tasks is unstudied.
- **Minimal Experiment:** Sweep warmup lengths × decoder init scales on 4 dense fine-tuning setups; measure early encoder-weight drift and final accuracy; test the gradient-ratio predictor.
- **Main Risk:** "Encoder damage" needs careful operationalization (e.g., retained linear-probe performance) to avoid circularity.

### IDEA-A-0070
- **One-sentence idea:** Quantify gradient conflict between SAM's mask loss and IoU-prediction loss during fine-tuning and test whether decoupling them improves both mask quality and quality-prediction calibration.
- **Problem:** SAM co-trains mask and IoU-prediction heads; under fine-tuning on new domains, these objectives may conflict (gradient cosine < 0), degrading the IoU head's calibration (connecting to IDEA-A-0016).
- **Core Hypothesis (falsifiable):** Gradient conflict episodes correlate with degradation of predicted-IoU calibration, and a two-phase schedule (mask first, IoU head after, encoder frozen in phase 2) yields both better masks and >30% lower ECE than joint training.
- **Why Important:** The IoU head is the trust signal downstream pipelines use; keeping it calibrated through fine-tuning is a deployment requirement.
- **Why Possibly Novel:** Multi-task gradient conflict is studied generically; its specific consequence for mask-quality *calibration* in promptable models is new.
- **Minimal Experiment:** Instrument gradient cosines during SAM fine-tuning on 3 domains; compare joint vs two-phase schedules on IoU and ECE.
- **Main Risk:** Conflict may be rare in practice; the descriptive phase decides whether the interventional phase is warranted.

### IDEA-A-0071
- **One-sentence idea:** Test whether a weight-EMA (exponential moving average) of the fine-tuning trajectory recovers most of the forgetting-mitigation benefit of explicit regularization methods, for free.
- **Problem:** Forgetting mitigation uses replay/regularizers with implementation cost; EMA implicitly averages toward earlier (less forgotten) weights and might capture most of the benefit at zero cost — untested for dense adaptation.
- **Core Hypothesis (falsifiable):** EMA weights retain ≥70% more zero-shot generality than final weights at equal target-task accuracy, matching or beating L2-SP-style regularization on the retention–adaptation Pareto front for segmentation fine-tunes.
- **Why Important:** If a free trick dominates purpose-built methods, forgetting-mitigation baselines across the literature need revision.
- **Why Possibly Novel:** EMA is used for accuracy/stability; framing and evaluating it as a forgetting mitigation on the retention Pareto front is new.
- **Minimal Experiment:** Fine-tune SAM/SegFormer on 4 tasks; compare final vs EMA weights vs L2-SP vs replay on (target accuracy, retained-generality) Pareto plots.
- **Main Risk:** EMA horizon becomes the new hyperparameter; sweep it and report sensitivity.

### IDEA-A-0072
- **One-sentence idea:** Run the controlled comparison the field skipped: strong augmentation + frozen features + linear/light decoder vs weak augmentation + LoRA, at matched compute, for dense adaptation.
- **Problem:** Augmentation strength and adaptation method are always co-varied in papers; we don't know how much of PEFT's benefit is reproducible by augmentation with a frozen backbone.
- **Core Hypothesis (falsifiable):** On ≥50% of small-data segmentation tasks, strong-aug + frozen features matches LoRA + default-aug within 1 mIoU at equal compute, implying much of "adaptation" is invariance injection, not representation change.
- **Why Important:** Reorders the practitioner's toolbox: augmentation is simpler, safer (no forgetting), and composable.
- **Why Possibly Novel:** The augmentation-vs-adaptation *equivalence question* has not been posed as a controlled matched-compute study for dense tasks.
- **Minimal Experiment:** 6 tasks × {frozen+strong-aug, frozen+weak-aug, LoRA+weak-aug, LoRA+strong-aug} at matched budgets; 3 seeds; report the full factorial.
- **Main Risk:** "Strong augmentation" must be tuned per-task to be a fair champion, inflating its budget; account tuning cost explicitly.

### IDEA-A-0073
- **One-sentence idea:** Validate "surgical fine-tuning" (choosing which blocks to tune based on a shift-diagnostic) for dense prediction, testing whether gradient-based block selection beats uniform PEFT.
- **Problem:** Block-selection heuristics (relative gradient norm per block) were proposed for classification; whether they select correctly for dense tasks with structured shifts is unknown.
- **Core Hypothesis (falsifiable):** Blocks ranked by early-training gradient-norm ratio predict the best-performing tuned subset (top-3 overlap >2/3), and surgical tuning of the top-3 blocks beats uniform LoRA at equal parameter budget on shift-specific tasks.
- **Why Important:** Automated block selection removes a manual design step and could become the default PEFT policy.
- **Why Possibly Novel:** Surgical fine-tuning was studied for classification robustness; dense-prediction validation with promptable models is missing.
- **Minimal Experiment:** 6 shift tasks; compute block diagnostics from 100-step pilots; compare diagnostic-selected vs uniform vs exhaustive-best subsets.
- **Main Risk:** Exhaustive-best requires many runs to establish ground truth; restrict to 12-block backbones to keep the oracle tractable.

### IDEA-A-0074
- **One-sentence idea:** Perform a null-hypothesis test on LoRA dropout for dense-prediction fine-tuning: does it do anything beyond noise across a well-powered grid?
- **Problem:** LoRA dropout is inherited from NLP defaults and copied into vision configs; its effect for dense tasks may be indistinguishable from zero, i.e., pure cargo cult.
- **Core Hypothesis (falsifiable):** Across a 3-dataset × 5-dropout-level × 10-seed grid, LoRA dropout's effect on mIoU is within the seed-noise band (effect size < 0.2σ) at every level — the null holds.
- **Why Important:** Deleting dead hyperparameters reduces search spaces community-wide; also demonstrates a template for auditing inherited defaults.
- **Why Possibly Novel:** Nobody publishes well-powered null results on hyperparameters; that absence is exactly the gap.
- **Minimal Experiment:** The stated grid with pre-registered equivalence testing (TOST) rather than significance hunting.
- **Main Risk:** A null on 3 datasets doesn't preclude niche settings where it matters; scope claims carefully to tested regimes.

### IDEA-A-0075
- **One-sentence idea:** Test whether task arithmetic (adding/subtracting weight-difference vectors) works for dense prediction: can a segmentation capability be cleanly added or removed from a fine-tuned model?
- **Problem:** Task vectors show clean composition for classification; dense capabilities may be less linear (spatial decoders, structured outputs), and nobody has mapped where arithmetic breaks.
- **Core Hypothesis (falsifiable):** Adding task vectors composes segmentation capabilities with <20% interference when tasks use disjoint classes, but *subtracting* a task vector fails to remove a dense capability cleanly (>50% capability remains or collateral damage exceeds 10 mIoU on retained tasks) — addition works, negation doesn't.
- **Why Important:** Model editing without retraining is valuable for licensing/unlearning; knowing negation fails for dense tasks prevents false security in "capability removal" claims.
- **Why Possibly Novel:** Task arithmetic papers focus on classification/generation; a dense-prediction composition/negation audit is missing.
- **Minimal Experiment:** Fine-tune one backbone on 4 segmentation tasks; evaluate all pairwise additions and single negations on all tasks; report interference matrices.
- **Main Risk:** Requires a shared backbone/decoder architecture across tasks, constraining task choice.

---

## Cluster 4 — Catastrophic Forgetting & Continual Adaptation (IDEA-A-0076 … 0090)

### IDEA-A-0076
- **One-sentence idea:** Map the full Pareto frontier between target-task gain and zero-shot generality loss when fine-tuning SAM, and test whether published fine-tunes sit far from that frontier.
- **Problem:** SAM fine-tunes report target gains without measuring generality loss; the community lacks even a descriptive account of the trade-off's shape, let alone whether existing recipes are efficient.
- **Core Hypothesis (falsifiable):** The gain/retention frontier is strongly concave (large retention is nearly free up to a knee), and ≥70% of common recipes (full FT, decoder-only, LoRA at default LR) sit >10 retention points inside the frontier — i.e., forgetting in practice is mostly unforced error.
- **Why Important:** If most forgetting is unforced, the fix is recipe hygiene, not new algorithms — a message with immediate practical consequences.
- **Why Possibly Novel:** Forgetting is documented, but frontier estimation with recipe-efficiency auditing for promptable segmentation is new.
- **Minimal Experiment:** Sweep LR × trained-components × steps on 2 target tasks; measure target IoU and zero-shot IoU on a 6-domain retention suite; trace the empirical frontier and place standard recipes on it.
- **Main Risk:** The frontier depends on the retention suite's composition; use a broad, pre-registered suite.

### IDEA-A-0077
- **One-sentence idea:** Localize forgetting layer-wise in dense models: after fine-tuning, which layers' changes are responsible for zero-shot generality loss, tested by selective weight rewinding.
- **Problem:** Forgetting is measured as a scalar; where in the network generality is lost determines which mitigation (freezing, partial rewind) can work.
- **Core Hypothesis (falsifiable):** Rewinding the last third of encoder blocks to pretrained values restores >70% of lost generality while sacrificing <20% of target gains — forgetting is concentrated in late semantic layers, not early features.
- **Why Important:** Motivates surgical retention recipes (rewind or freeze late blocks) that could dominate global regularizers.
- **Why Possibly Novel:** Layer-wise forgetting analyses exist for classification continual learning; a rewinding-based causal localization for dense foundation models is missing.
- **Minimal Experiment:** Fine-tune on 3 tasks; rewind each block-third combination; measure the target/retention matrix.
- **Main Risk:** Layer roles differ across architectures (ViT vs Hiera); replicate on two encoder families.

### IDEA-A-0078
- **One-sentence idea:** Test whether "forgetting" in fine-tuned dense models is mostly output-head/decoder drift rather than feature destruction, via linear re-probing of frozen intermediate features.
- **Problem:** If fine-tuned encoders still contain the old capabilities linearly (only the readout drifted), then forgetting is shallow and cheaply reversible — a fundamentally different problem than feature erasure.
- **Core Hypothesis (falsifiable):** Linear probes retrained on the *fine-tuned* encoder's features recover >85% of original zero-shot dense performance on forgotten domains, versus <40% recovery from the drifted full model — most forgetting is readout drift.
- **Why Important:** Changes the objective of continual learning for foundation models from "preserve weights" to "preserve or re-derive readouts," which is far cheaper.
- **Why Possibly Novel:** Probing-based forgetting decomposition exists in isolated classification studies; the dense-prediction version with promptable decoders is new.
- **Minimal Experiment:** After fine-tunes on 3 tasks, retrain lightweight decoders/probes on frozen adapted encoders for 4 forgotten domains; compare recovery rates.
- **Main Risk:** "Recovery via retraining a probe" requires labeled data from forgotten domains; quantify how little suffices.

### IDEA-A-0079
- **One-sentence idea:** Determine the minimal replay fraction of pretraining-like data (e.g., SA-1B samples) that preserves SAM's generality during fine-tuning, and whether replay composition matters more than quantity.
- **Problem:** Replay is the classic fix, but for foundation-scale pretraining sets nobody knows the retention-vs-replay-fraction curve or whether curated replay (diverse masks) beats random replay.
- **Core Hypothesis (falsifiable):** Retention vs replay fraction saturates extremely early (≥90% retention at ≤1% replay), and diversity-curated replay halves the required fraction relative to random sampling.
- **Why Important:** Makes retention nearly free in every SAM fine-tuning recipe, with a concrete recommended replay budget.
- **Why Possibly Novel:** Replay scaling laws at the foundation-model scale for promptable segmentation haven't been published.
- **Minimal Experiment:** Fine-tune with replay fractions {0, 0.1%, 0.5%, 1%, 5%} × {random, diversity-curated}; measure the retention suite; locate saturation.
- **Main Risk:** SA-1B licensing/availability constraints; can substitute a large diverse mask corpus as proxy with caveats.

### IDEA-A-0080
- **One-sentence idea:** Test for order effects in sequential adaptation of a medical VFM across modalities (CT→MR→US vs US→MR→CT): does curriculum order change final multi-modality competence?
- **Problem:** Institutions adapt models sequentially as data arrives; if order matters strongly, deployment pipelines need sequencing policies, and "continual" results reported for one order are misleading.
- **Core Hypothesis (falsifiable):** Ending on the most distributionally distinct modality (ultrasound) causes the largest forgetting of earlier ones, and starting from it yields the best final average — a >5-point average-Dice spread across orderings, violating order-invariance.
- **Why Important:** Directly actionable sequencing guidance for real clinical ML operations, and a clean testbed for interference theory in dense tasks.
- **Why Possibly Novel:** Task-order effects are known in small-scale continual learning; modality-order effects for medical foundation adaptation are unmeasured.
- **Minimal Experiment:** All 6 orderings of 3 modalities with a fixed recipe; measure the final per-modality and average Dice; test order effects with permutation statistics.
- **Main Risk:** Order effects may be recipe-dependent; replicate under 2 recipes (LoRA vs full FT).

### IDEA-A-0081
- **One-sentence idea:** Test whether fine-grained boundary competence is forgotten *before* region-level competence during fine-tuning — a "last learned, first forgotten" hypothesis for dense skills.
- **Problem:** Forgetting is tracked with coarse metrics; if boundary skill decays first, models can look retained on IoU while already degraded for precision applications.
- **Core Hypothesis (falsifiable):** During fine-tuning on a new domain, zero-shot boundary-F on retained domains decays ≥3× faster (in steps) than region IoU, and the decay order is consistent across tasks and seeds.
- **Why Important:** Defines which retention metric must be monitored; IoU-based retention claims may be systematically overstated.
- **Why Possibly Novel:** Skill-decomposition of forgetting dynamics (boundary vs region) has not been examined for segmentation models.
- **Minimal Experiment:** Log boundary-F and IoU on a retention suite every N steps during 6 fine-tuning runs; compare decay time-constants.
- **Main Risk:** Boundary-F is noisier than IoU; needs enough evaluation instances for stable curves.

### IDEA-A-0082
- **One-sentence idea:** Evaluate weight-space interpolation (WiSE-FT style) between pretrained and fine-tuned segmentation models: does the classification-era result that interpolation beats both endpoints transfer to dense prediction?
- **Problem:** WiSE-FT's robustness interpolation is now folklore, but dense decoders and spatial heads may break the linear-connectivity conditions it relies on.
- **Core Hypothesis (falsifiable):** For segmentation fine-tunes of CLIP/DINOv2-initialized models, some interpolation coefficient beats the fine-tuned endpoint on OOD *without* losing >1 point in-domain on the majority of tasks — but fails specifically when the decoder is trained from scratch (no shared basin).
- **Why Important:** A free robustness knob for dense models if it works; a documented failure boundary (fresh decoders) if it doesn't — both actionable.
- **Why Possibly Novel:** WiSE-FT was shown for zero-shot classifiers; a careful dense-prediction replication with the fresh-decoder boundary condition is missing.
- **Minimal Experiment:** 5 segmentation fine-tunes with shared vs fresh decoders; sweep interpolation α; plot ID/OOD curves per condition.
- **Main Risk:** Requires the pretrained model to have a usable zero-shot dense mode for fair OOD endpoints; choose setups accordingly.

### IDEA-A-0083
- **One-sentence idea:** Test the assumed monotonic link between weight-space distance traveled during fine-tuning and the amount of forgetting — is distance actually the right predictor?
- **Problem:** Regularizers (L2-SP, EWC) penalize weight distance on the assumption that distance ⇒ forgetting; direction may matter far more than magnitude, making distance-based regularization misaimed.
- **Core Hypothesis (falsifiable):** At matched weight-space distance, forgetting varies by >3× depending on update direction (measured via overlap with pretraining-loss curvature directions), and distance alone explains <30% of forgetting variance across runs.
- **Why Important:** If direction dominates, the standard regularizer family is optimizing the wrong quantity, explaining its mediocre dense-task performance.
- **Why Possibly Novel:** The distance-vs-direction decomposition for forgetting in dense foundation models has not been measured.
- **Minimal Experiment:** Generate many fine-tuning runs with varied hyperparameters; regress retention loss on (distance, curvature-weighted direction overlap); compare explanatory power.
- **Main Risk:** Estimating pretraining-loss curvature for foundation models is approximate (K-FAC/low-rank); validate with two estimators.

### IDEA-A-0084
- **One-sentence idea:** Compare continual adaptation via growing *prompt/adapter libraries* (no weight sharing between tasks) against weight-updating methods, measuring the true cost of forgetting-free-by-construction designs.
- **Problem:** Library approaches sidestep forgetting entirely but pay costs (routing errors, no forward transfer) that are rarely quantified against interference-suffering alternatives on dense tasks.
- **Core Hypothesis (falsifiable):** Adapter libraries dominate weight-updating continual learning on retention (by construction) but lose ≥5 points on *new-task* performance due to zero forward transfer, and the routing error rate at inference exceeds 10% under domain ambiguity — quantifying the price of isolation.
- **Why Important:** Practitioners need the honest trade sheet: isolation vs transfer is the central design decision for continual dense systems.
- **Why Possibly Novel:** Both families exist; the controlled head-to-head with routing-error and forward-transfer accounting for segmentation is missing.
- **Minimal Experiment:** 6-task medical sequence; compare library (per-task LoRA + learned router) vs replay vs EWC on retention, forward transfer, and routing metrics.
- **Main Risk:** Router design strongly affects library results; use several routers and report the range.

### IDEA-A-0085
- **One-sentence idea:** When fine-tuning dual-tower VLMs for dense tasks, measure whether forgetting concentrates in the text tower or vision tower, via tower-swap diagnostics.
- **Problem:** Open-vocab segmentation fine-tunes update both towers; knowing which tower's drift destroys zero-shot transfer would let us freeze the fragile one.
- **Core Hypothesis (falsifiable):** Swapping the fine-tuned text tower back to pretrained restores most zero-shot open-vocab performance (>70%) while swapping the vision tower does not — text-side drift is the main cause of open-vocabulary forgetting.
- **Why Important:** A one-line recipe change (freeze the text tower) could preserve open-vocab ability in every dense VLM fine-tune.
- **Why Possibly Novel:** Tower-wise forgetting attribution via post-hoc swapping has not been reported for dense VLMs.
- **Minimal Experiment:** Fine-tune 2 open-vocab segmenters on closed-vocab tasks; evaluate all four tower-swap combinations on zero-shot suites.
- **Main Risk:** Towers co-adapt during fine-tuning, so swaps may produce incompatibility artifacts; include brief re-alignment controls.

### IDEA-A-0086
- **One-sentence idea:** Measure modality-level forgetting in SAM2: does fine-tuning on video tasks degrade static-image segmentation, and is the memory module the mediator?
- **Problem:** SAM2 serves both image and video use; task-specific video fine-tunes may silently degrade the (more widely used) image path, and nobody measures cross-modality regression.
- **Core Hypothesis (falsifiable):** Video-task fine-tuning degrades static-image zero-shot IoU by a measurable margin (>3 points) even when the image path shares all weights except memory, and the degradation localizes to encoder blocks most attended by memory tokens.
- **Why Important:** Establishes cross-modality regression testing as a required practice for multi-mode foundation models.
- **Why Possibly Novel:** Image↔video interference within one promptable model is a new forgetting axis.
- **Minimal Experiment:** Fine-tune SAM2 on 2 video tasks; track static-image suites; localize drift by per-block weight-change × attention analysis.
- **Main Risk:** Effect may be small with LoRA-based tunes; include full-FT condition to bound the worst case.

### IDEA-A-0087
- **One-sentence idea:** Test whether Fisher-information-based importance (EWC-style) actually localizes the weights that matter for dense-task knowledge, using targeted perturbation as ground truth.
- **Problem:** EWC assumes Fisher diagonal identifies important weights; for dense prediction with spatial decoders this assumption is untested, potentially explaining EWC's weak segmentation results.
- **Core Hypothesis (falsifiable):** Perturbing top-Fisher weights degrades dense-task performance no more than perturbing random weights of equal norm in ≥half of layers — the Fisher diagonal fails to identify dense-task-critical parameters.
- **Why Important:** If Fisher localization fails, a whole family of regularization methods is built on sand for dense tasks, and better importance measures are needed.
- **Why Possibly Novel:** EWC has been *applied* to segmentation; a direct perturbation-based validation of its core assumption has not.
- **Minimal Experiment:** Compute Fisher diagonals for a trained segmenter; perturbation experiments (top-k Fisher vs random vs gradient-based alternatives); compare degradation curves.
- **Main Risk:** Diagonal vs full-Fisher distinction — a negative result may only indict the diagonal approximation; include K-FAC comparison.

### IDEA-A-0088
- **One-sentence idea:** Characterize when self-distillation from the frozen pretrained model (as a retention regularizer) *hurts* target-task adaptation, testing the "teacher veto" hypothesis on contradicting domains.
- **Problem:** Distill-from-old-self is a popular retention trick, but when the target domain contradicts pretrained behavior (e.g., SAM must learn that smoke has no crisp boundary), the frozen teacher may veto necessary learning.
- **Core Hypothesis (falsifiable):** Retention distillation's target-task cost correlates with teacher-target disagreement (measured as pretrained-model error on target data): on high-disagreement domains, distillation costs >5 points of target performance while on low-disagreement domains it is free.
- **Why Important:** Gives a pre-hoc rule for when to use retention distillation vs replay, based on a cheap disagreement measurement.
- **Why Possibly Novel:** Retention distillation is used blindly; its failure condition (teacher-target contradiction) has not been formalized or measured for dense tasks.
- **Minimal Experiment:** 6 target domains ordered by pretrained-SAM error; fine-tune ± distillation; regress target-cost on disagreement.
- **Main Risk:** Distillation weight confounds the effect; sweep it and compare Pareto fronts rather than points.

### IDEA-A-0089
- **One-sentence idea:** Test for hysteresis in forgetting: after fine-tuning away a capability, does brief re-exposure to the original objective restore it far faster than it was learned ("rapid reversibility"), and does the restoration survive continued target training?
- **Problem:** Whether forgotten dense capabilities are erased or merely suppressed determines the economics of capability maintenance; hysteresis dynamics are unmeasured for foundation-scale segmentation.
- **Core Hypothesis (falsifiable):** Restoring zero-shot generality takes <5% of the original steps (suppression, not erasure), but restored capability decays again within a similar budget of continued target training — a repeatable hysteresis loop with characteristic time-constants.
- **Why Important:** Suggests cheap periodic "refresh" schedules as a practical alternative to continual-learning machinery, with predictable maintenance costs.
- **Why Possibly Novel:** Rapid-recovery phenomena are hinted at in LLM literature; a quantitative hysteresis characterization for dense vision models is new.
- **Minimal Experiment:** Fine-tune SAM on a target task, then alternate short generality-refresh and target phases; log both metrics; fit time-constants across cycles.
- **Main Risk:** Refresh data may leak target-relevant signal; use strictly disjoint domains for refresh.

### IDEA-A-0090
- **One-sentence idea:** Build a forgetting benchmark that separates *concept* forgetting (which categories/domains are lost) from *prior* forgetting (boundary style, granularity, calibration), since current retention scores conflate them.
- **Problem:** A single retained-mIoU number cannot distinguish a model that forgot rare categories from one that forgot boundary precision or calibration — different failures needing different fixes.
- **Core Hypothesis (falsifiable):** Standard fine-tunes produce *dissociable* forgetting profiles: recipes exist that preserve concepts but corrupt priors and vice versa, demonstrated by a double dissociation across ≥2 recipes on the proposed metric battery.
- **Why Important:** Metric infrastructure shapes research; a decomposition benchmark would redirect continual-learning-for-dense-vision toward the actual failure modes.
- **Why Possibly Novel:** Retention benchmarks exist as aggregate suites; a validated decomposition into concept vs prior axes with dissociation evidence is new.
- **Minimal Experiment:** Assemble metric battery (per-domain IoU, boundary-F, granularity-choice agreement, ECE); evaluate 6 recipes; test for the dissociation structure via factor analysis.
- **Main Risk:** Axes may be empirically correlated, undermining the decomposition — the factor analysis is the honest test.

---

## Cluster 5 — Medical Segmentation: Limits, Assumptions, Clinical Validity (IDEA-A-0091 … 0120)

### IDEA-A-0091
- **One-sentence idea:** Quantify the inter-annotator-variability ceiling of major medical segmentation benchmarks and identify which reported SOTA gains are below the label-noise floor.
- **Problem:** Leaderboard gains of 0.5–1 Dice are celebrated on benchmarks whose annotator disagreement may be several Dice points, meaning models are being fit to one annotator's style, not anatomy.
- **Core Hypothesis (falsifiable):** For ≥half of widely used benchmarks, the top-10 leaderboard spread is smaller than the measured inter-annotator Dice spread on a re-annotated subset — recent "progress" is within label noise.
- **Why Important:** Redirects the field from chasing sub-noise gains toward multi-annotator ground truth and distributional evaluation.
- **Why Possibly Novel:** Inter-annotator variability is known per-dataset anecdotally; a cross-benchmark audit tied explicitly to leaderboard spreads is missing.
- **Minimal Experiment:** Re-annotate 50–100 cases from 5 benchmarks with 3 experts each; compare annotator spread to public leaderboard spreads.
- **Main Risk:** Expert annotation is expensive; partner with clinical collaborators or use existing multi-annotator releases where available.

### IDEA-A-0092
- **One-sentence idea:** Test whether the box prompts used to train/evaluate MedSAM-style models match how clinicians would actually prompt, and measure the performance gap under realistic prompting.
- **Problem:** MedSAM's box-prompt protocol assumes tight boxes; real clinicians draw loose, fast boxes or prefer clicks, and the deployment gap from idealized prompts is unmeasured.
- **Core Hypothesis (falsifiable):** Clinician-drawn prompts (collected in a timed setting) are systematically looser (>20% area slack) and yield >8 Dice lower performance than benchmark-tight boxes, and the degradation is worse for small lesions.
- **Why Important:** Reported medical promptable-segmentation numbers may substantially overstate clinical utility; realistic-prompt evaluation should become standard.
- **Why Possibly Novel:** Prompt realism for *medical* promptable models with actual clinician behavior data has not been studied.
- **Minimal Experiment:** Collect prompts from 10 clinicians on 200 cases under time pressure; evaluate MedSAM-class models under collected vs idealized prompts.
- **Main Risk:** Clinician recruitment; a smaller trainee cohort with expert validation could substitute initially.

### IDEA-A-0093
- **One-sentence idea:** Run a compute- and tuning-matched showdown between nnU-Net and foundation-model fine-tunes to isolate *why* well-tuned U-Nets remain competitive in medical segmentation.
- **Problem:** Foundation models dominate natural images but reportedly struggle to beat nnU-Net; existing comparisons confound tuning effort, resolution handling, and preprocessing, so the *cause* of U-Net resilience is unknown.
- **Core Hypothesis (falsifiable):** After matching preprocessing/resolution/tuning budget, the remaining nnU-Net advantage concentrates in (a) full-resolution 3D context and (b) target-specific augmentation — and vanishes on 2D high-contrast tasks, localizing exactly what foundation models lack.
- **Why Important:** Tells the field whether to invest in 3D-native foundation models, resolution handling, or augmentation transfer — a strategic fork.
- **Why Possibly Novel:** Comparisons exist but none decompose the gap causally with matched budgets and component swaps.
- **Minimal Experiment:** On 6 tasks spanning 2D/3D and contrast levels, run both families with matched budgets, then component-swap (give the ViT nnU-Net's augmentation and resolution policy) to attribute the gap.
- **Main Risk:** "Matched tuning" is contentious; pre-register budgets and publish all configs.

### IDEA-A-0094
- **One-sentence idea:** Decompose cross-scanner degradation in medical segmentation into frequency bands to test whether scanner shift is fundamentally a texture (high-frequency) phenomenon.
- **Problem:** Cross-site drops are treated monolithically; if the damaging shift lives in specific frequency bands, cheap band-level normalization could replace heavy adaptation machinery.
- **Core Hypothesis (falsifiable):** Swapping only high-frequency amplitude spectra between sites reproduces >70% of the cross-site performance drop, while low-frequency swaps reproduce <20% — scanner shift is predominantly high-frequency texture shift.
- **Why Important:** Validates or kills a whole class of cheap Fourier-based fixes for the most common deployment failure in medical AI.
- **Why Possibly Novel:** Fourier domain adaptation exists as a method; the *causal decomposition* of medical scanner shift by band has not been established.
- **Minimal Experiment:** On 3 multi-site datasets, create band-swapped hybrid images; measure model degradation per band configuration; attribute the drop.
- **Main Risk:** Band swapping creates unnatural images; verify with a perceptual realism check and monotonic band-width sweeps.

### IDEA-A-0095
- **One-sentence idea:** Quantify how much 2D-slice-based foundation models lose on structures *defined by* 3D continuity (vessels, ducts, small nodules), versus structures identifiable per-slice.
- **Problem:** Most medical VFM adaptations process volumes slice-wise; the assumption that 2D suffices is untested per structure type, hiding systematic failures on continuity-defined anatomy.
- **Core Hypothesis (falsifiable):** The 2D-vs-3D performance gap correlates strongly with a structure's "slice-identifiability" score (human ability to segment from single slices), approaching zero for high-identifiability organs and exceeding 10 Dice for continuity-defined structures.
- **Why Important:** Provides a per-structure rule for when 3D-native modeling is mandatory, focusing expensive 3D development where it matters.
- **Why Possibly Novel:** 2D-vs-3D comparisons exist per-task; the slice-identifiability law unifying them is new.
- **Minimal Experiment:** Measure human single-slice segmentability for 10 structures; compare matched 2D and 3D models; test the correlation.
- **Main Risk:** Human slice-identifiability measurement is itself a study; use a small clinician panel with clear protocol.

### IDEA-A-0096
- **One-sentence idea:** Establish the sensitivity-vs-lesion-size law for medical VFMs versus specialized detectors, testing whether foundation models have a systematically worse small-lesion exponent.
- **Problem:** Missing small lesions is the clinically catastrophic failure; whether VFM adaptation sacrifices small-lesion sensitivity relative to purpose-built models is unquantified as a scaling relationship.
- **Core Hypothesis (falsifiable):** Detection sensitivity vs lesion diameter follows a sigmoid whose midpoint is ≥30% larger (worse) for adapted VFMs than for specialized 3D models at matched overall Dice — aggregate parity hides small-lesion inferiority.
- **Why Important:** If the law holds, aggregate-metric-based claims that "VFMs match specialists" are clinically misleading precisely where it matters most.
- **Why Possibly Novel:** Size-stratified evaluation exists; the cross-family sigmoid-midpoint comparison at matched aggregate performance is new.
- **Minimal Experiment:** On lesion datasets with size distributions (lung nodules, liver lesions, MS lesions), fit per-model sensitivity-size curves; compare midpoints at matched Dice.
- **Main Risk:** Size confounds with contrast and location; use stratified matching or covariate adjustment.

### IDEA-A-0097
- **One-sentence idea:** Test at scale whether Dice loss — the medical default — systematically destroys probability calibration relative to cross-entropy, and whether the harm scales with class imbalance.
- **Problem:** Dice loss is near-universal in medical segmentation, yet its miscalibration side effect (known in isolated studies) has never been quantified across tasks or connected to imbalance level, leaving practitioners without a usage rule.
- **Core Hypothesis (falsifiable):** Dice-trained models show ECE ≥3× cross-entropy-trained models at matched Dice score, with miscalibration growing monotonically with foreground sparsity; a two-phase (CE→Dice) schedule retains Dice's accuracy without the calibration penalty.
- **Why Important:** Calibrated probabilities are prerequisites for uncertainty-guided review and safe thresholding in clinical use; the default loss may be silently forfeiting them.
- **Why Possibly Novel:** The imbalance-conditioned quantification and the validated schedule fix, across many tasks, would settle a long-standing folklore dispute.
- **Minimal Experiment:** 8 tasks spanning imbalance levels × {Dice, CE, CE→Dice, Dice+CE} × 3 seeds; report accuracy-calibration Pareto per imbalance level.
- **Main Risk:** ECE estimation on sparse foregrounds is fragile; use debiased calibration estimators and regional calibration metrics.

### IDEA-A-0098
- **One-sentence idea:** Test whether pathology segmentation models exploit contralateral asymmetry as a shortcut, by evaluating on symmetric (bilateral) pathologies and synthetically symmetrized scans.
- **Problem:** For brain/organ pathologies, models may learn "find the asymmetric region" rather than pathology appearance — a shortcut that fails exactly on bilateral disease, which is unmeasured.
- **Core Hypothesis (falsifiable):** Models trained on predominantly unilateral pathology datasets drop >15 Dice on bilateral/symmetric cases relative to matched unilateral cases, and saliency analysis shows contralateral reference usage; symmetrized-input training removes both effects at modest cost.
- **Why Important:** Bilateral presentations are common and clinically critical; a shortcut of this kind is a patient-safety issue invisible to standard benchmarks.
- **Why Possibly Novel:** Asymmetry priors are used *deliberately* in classical methods; their status as an unintended shortcut in deep models is untested.
- **Minimal Experiment:** Stratify test sets by laterality; compare performance; run occlusion-based attribution on the contralateral side; test the symmetrization intervention.
- **Main Risk:** Bilateral cases may be harder for confounding reasons (severity); match on lesion size and contrast.

### IDEA-A-0099
- **One-sentence idea:** Measure the divergence between pixel-overlap metrics and topological correctness for vascular/airway segmentation, and test whether model rankings invert under topology-first evaluation.
- **Problem:** Clinical downstream uses of vessel segmentation (navigation, flow modeling) need connectivity, but benchmarks rank by Dice; if rankings invert under clDice/Betti metrics, the field is optimizing the wrong objective.
- **Core Hypothesis (falsifiable):** Across public vessel/airway benchmarks, ≥30% of pairwise model orderings invert between Dice and topology metrics, and the models winning on topology share identifiable design choices (higher-resolution decoders, topology-aware losses).
- **Why Important:** A documented ranking inversion would justify changing the default metric for an entire clinical subfield.
- **Why Possibly Novel:** Topology metrics exist; the systematic ranking-inversion audit across benchmarks and model families does not.
- **Minimal Experiment:** Re-evaluate 10 published models on 3 vessel benchmarks with Dice, clDice, and Betti error; quantify inversion rate and correlates.
- **Main Risk:** Reproducing 10 models faithfully is laborious; use released checkpoints only.

### IDEA-A-0100
- **One-sentence idea:** Audit test-time augmentation in medical segmentation for anatomically *invalid* invariances (e.g., left-right flips on lateralized anatomy) and quantify the harm TTA silently causes.
- **Problem:** Flip/rotate TTA is copied from natural images into medical pipelines, but anatomy is chiral and oriented; averaging over invalid transforms may blur lateralized structures — an unexamined standard practice.
- **Core Hypothesis (falsifiable):** Flip-TTA reduces accuracy on lateralized structures (>2 Dice on left/right-distinct organs) while helping symmetric ones, such that anatomy-aware TTA policies beat blanket TTA on ≥70% of tasks.
- **Why Important:** TTA is in nearly every medical pipeline including challenge winners; a validated anatomy-aware policy is an immediate free improvement.
- **Why Possibly Novel:** TTA is treated as harmless; its anatomical validity has not been systematically audited.
- **Minimal Experiment:** On 8 tasks with lateralized and symmetric structures, compare no-TTA vs blanket-TTA vs anatomy-aware TTA; stratify by structure laterality.
- **Main Risk:** Effects may be small per-structure; aggregate across many structures for power.

### IDEA-A-0101
- **One-sentence idea:** Extend the SynthSeg-style domain-randomization hypothesis to pathology: can models trained on *purely synthetic* randomized lesions generalize to real pathology better than real-data models generalize cross-site?
- **Problem:** SynthSeg showed randomized synthetic data yields contrast-agnostic anatomy segmentation; whether the same principle covers *pathology* (whose appearance is more variable and clinically critical) is an open, testable question.
- **Core Hypothesis (falsifiable):** Models trained on procedurally randomized synthetic lesions achieve cross-site generalization within 5 Dice of real-data models' in-site performance, and *beat* real-data models on out-of-distribution sites — randomization trades peak accuracy for portability.
- **Why Important:** If true, data-sharing barriers in medical AI shrink dramatically: synthesis recipes replace patient-data transfer.
- **Why Possibly Novel:** SynthSeg covers healthy anatomy; a rigorous pathology extension with cross-site out-performance criteria is unestablished.
- **Minimal Experiment:** Build a randomized lesion generator for one pathology (e.g., white-matter lesions); train synthetic-only vs real-data models; evaluate across ≥3 real sites.
- **Main Risk:** Pathology appearance may have irreducible real-data-only structure; a negative result still bounds the approach usefully.

### IDEA-A-0102
- **One-sentence idea:** Test whether federated averaging of LoRA adapters breaks down under non-IID medical site data, and whether the failure is in the low-rank factorization itself (factor misalignment across sites).
- **Problem:** Federated PEFT is proposed for privacy-preserving medical adaptation, but averaging low-rank factors A·B across sites is mathematically dubious when sites' updates span different subspaces — the failure mode is uncharacterized.
- **Core Hypothesis (falsifiable):** Naive LoRA-factor averaging underperforms averaging the *composed* updates (ΔW) by >5 Dice under high site heterogeneity, with the gap predicted by cross-site subspace principal angles — the factorization, not federation, is the problem.
- **Why Important:** Federated medical adaptation is heading to deployment; knowing the correct aggregation operator prevents a silent systemic error.
- **Why Possibly Novel:** Federated LoRA papers exist; the factor-vs-composed aggregation dissociation with a subspace-angle predictor for dense medical tasks is new.
- **Minimal Experiment:** Simulate 6-site federation with controlled heterogeneity; compare aggregation operators; regress the gap on principal angles.
- **Main Risk:** Simulated site splits may understate real heterogeneity; validate on one genuinely multi-site dataset.

### IDEA-A-0103
- **One-sentence idea:** Test whether model uncertainty maps (entropy, MC-dropout, ensembles) actually correlate with *clinician disagreement* regions, which is the operational meaning of "useful uncertainty" in medical segmentation.
- **Problem:** Uncertainty methods are validated against model error, but their clinical use case is flagging regions where experts would disagree or want review — an alignment nobody measures.
- **Core Hypothesis (falsifiable):** Pixel-wise correlation between model uncertainty and multi-annotator disagreement is weak (ρ < 0.4) for standard methods, and is dominated by trivial boundary-band effects — after excluding boundary bands, correlation approaches zero.
- **Why Important:** If uncertainty maps only recapitulate "boundaries are uncertain," their clinical value proposition (flagging genuinely ambiguous regions) is empty and needs new methods.
- **Why Possibly Novel:** The boundary-band-excluded analysis against expert disagreement, across methods, is a new and stringent validity test.
- **Minimal Experiment:** On multi-annotator datasets, compute uncertainty-disagreement correlation with and without boundary-band exclusion for 4 uncertainty methods.
- **Main Risk:** Few datasets have dense multi-annotator masks; prioritize those that do (e.g., prostate, lung nodule collections).

### IDEA-A-0104
- **One-sentence idea:** Audit active learning for 3D medical segmentation: do published slice/region selection strategies beat random selection under rigorous, budget-matched protocols?
- **Problem:** Active learning papers report gains, but 3D medical AL has known evaluation pitfalls (warm-start leakage, unrealistic budget accounting, annotation-time ignored); the true value over random is contested.
- **Core Hypothesis (falsifiable):** Under annotation-*time*-normalized budgets (not slice counts) and cold-start protocols, ≥half of published AL strategies fail to beat random selection on 3D tasks; gains concentrate only in extreme low-budget regimes.
- **Why Important:** Hospitals invest in AL tooling based on these papers; an honest audit either validates the investment or redirects it.
- **Why Possibly Novel:** AL criticism exists for classification; the time-normalized 3D segmentation audit with cold-start rigor is missing.
- **Minimal Experiment:** Reimplement 5 AL strategies on 3 3D tasks; measure annotation time with a timing model from real annotator logs; compare against random at matched time budgets.
- **Main Risk:** Annotation-time models vary by tool; publish sensitivity to the timing model.

### IDEA-A-0105
- **One-sentence idea:** Replace step-edge ground truth with graded "infiltration maps" for diffusely infiltrating tumors and test whether models trained on soft targets produce more clinically faithful margins.
- **Problem:** Infiltrative tumors (gliomas) have no true boundary, yet ground truth forces a binary contour; models therefore learn artificially crisp margins, which misinform resection/radiation planning.
- **Core Hypothesis (falsifiable):** Models trained on soft infiltration targets (derived from multi-annotator fusion + multi-modal signal) predict held-out annotator *distributions* better (lower distributional divergence) than binarized training, without losing binary-threshold Dice.
- **Why Important:** Aligns the machine-learning target with the biological reality of infiltration — a representational fix, not an architecture fix.
- **Why Possibly Novel:** Soft labels exist generically; formulating infiltration as the ground-truth object with clinical-margin evaluation is a new framing for this class of pathology.
- **Minimal Experiment:** On multi-annotator glioma data, build soft targets; train matched models on soft vs hard targets; evaluate distributional match and margin-sensitivity curves.
- **Main Risk:** Clinical evaluation of "faithful margins" needs radiation-oncology input; scope initial claims to distributional metrics.

### IDEA-A-0106
- **One-sentence idea:** Characterize what transfers when fine-tuning across tumor types (e.g., liver→kidney lesions): appearance features, "lesion-ness" priors, or only generic contrast sensitivity.
- **Problem:** Cross-pathology transfer is assumed beneficial but its content is opaque; knowing *what* transfers would tell us whether pan-lesion foundation training is worthwhile.
- **Core Hypothesis (falsifiable):** Transfer gains from tumor A to tumor B are predicted by shared low-level contrast statistics (ρ > 0.7), not by organ or histology similarity — cross-pathology transfer is mostly generic blob-contrast learning.
- **Why Important:** If transfer is generic, small shared "lesion-prior" pretraining suffices and organ-specific data hoarding is unnecessary; if specific, pan-cancer datasets gain value.
- **Why Possibly Novel:** Transfer matrices across pathologies with a *predictive covariate analysis* (what explains the matrix) have not been published.
- **Minimal Experiment:** 6 lesion datasets; full transfer matrix (train A, fine-tune small B); regress gains on appearance-similarity vs anatomy-similarity covariates.
- **Main Risk:** Dataset size imbalance confounds the matrix; subsample to matched sizes.

### IDEA-A-0107
- **One-sentence idea:** Test whether adding anatomical-relationship language ("the pancreas lies posterior to the stomach") to prompts improves VLM-based medical grounding at all, or whether current VLMs cannot use spatial-anatomical text.
- **Problem:** Medical prompt engineering assumes richer anatomical descriptions help, but VLMs' capacity to convert anatomical-relations text into spatial predictions is unverified — the effort may be wasted.
- **Core Hypothesis (falsifiable):** Anatomical-relation prompts change VLM segmentation outputs in the direction of the stated relation in <20% of cases (measured by centroid displacement consistency), i.e., current medical VLMs ignore relational anatomy language.
- **Why Important:** A negative result would redirect medical-VLM work from prompt enrichment to structural grounding mechanisms; a positive result gives a free accuracy lever.
- **Why Possibly Novel:** Relational-language grounding tests exist for natural images; the anatomical version — where relations are objectively verifiable — has not been run.
- **Minimal Experiment:** Construct paired prompts (with/without true and *false* anatomical relations) for 20 structures; measure output displacement consistency with stated relations.
- **Main Risk:** Failure may be due to the text encoder or the grounding head; include text-embedding probing to attribute.

### IDEA-A-0108
- **One-sentence idea:** Audit patient-level data leakage across popular medical segmentation benchmarks (same patient in train/test, cross-dataset duplicates) and re-estimate SOTA gaps after deduplication.
- **Problem:** Benchmarks assembled from overlapping public sources risk patient-level leakage, inflating scores in unknown amounts — a hygiene audit the field has skipped for segmentation.
- **Core Hypothesis (falsifiable):** ≥3 widely used benchmarks contain patient-level or near-duplicate leakage affecting >5% of test cases, and deduplicated re-evaluation shrinks published SOTA-vs-baseline gaps by ≥30% on affected benchmarks.
- **Why Important:** Leakage-inflated benchmarks distort method selection for clinical deployment; the audit deliverable (clean splits) benefits everyone.
- **Why Possibly Novel:** Leakage audits exist for natural-image and radiograph classification; a systematic segmentation-benchmark audit with re-evaluation is missing.
- **Minimal Experiment:** Run perceptual-hash + registration-based duplicate detection across 8 benchmarks; publish cleaned splits; re-evaluate released checkpoints.
- **Main Risk:** Near-duplicate detection on volumetric data needs care (same scanner ≠ same patient); manual verification of flagged pairs.

### IDEA-A-0109
- **One-sentence idea:** Test whether domain-specific medical pretraining still adds value over general foundation features (DINOv2-class) for segmentation in 2026, and precisely where.
- **Problem:** Medical pretraining (RadImageNet-style) was justified against ImageNet-era features; whether that justification survives modern general VFMs is unresolved, and labs keep paying the medical-pretraining cost.
- **Core Hypothesis (falsifiable):** With modern general VFMs, medical-specific pretraining adds >2 Dice only for modalities far from natural-image statistics (ultrasound, OCT) and for tiny fine-tuning budgets (<100 cases); elsewhere it adds nothing.
- **Why Important:** Deallocates or reallocates significant community compute and data-collection effort based on evidence.
- **Why Possibly Novel:** The comparison is often made against outdated baselines; a current-generation, budget-stratified audit is missing.
- **Minimal Experiment:** {General VFM, medical-pretrained, from-scratch} × 6 modalities × 3 fine-tune budgets; map where the medical-pretraining delta exceeds noise.
- **Main Risk:** Available medical-pretrained checkpoints vary in quality; use the strongest public ones and state the scope.

### IDEA-A-0110
- **One-sentence idea:** Characterize the failure structure of multi-sequence MRI segmentation models when sequences are missing at test time, and test whether "sequence dropout" training solves it or merely averages the damage.
- **Problem:** Clinical MRI often lacks sequences the model was trained with; models fail unpredictably, and the standard fix (dropout over sequences during training) may trade peak performance for uniform mediocrity — unquantified.
- **Core Hypothesis (falsifiable):** Sequence-dropout training reduces worst-case missing-sequence degradation by >50% but costs >3 Dice on complete inputs, whereas a router-style dedicated-path design achieves both — the trade-off is architectural, not fundamental.
- **Why Important:** Missing sequences are the rule, not the exception, in real hospitals; deployment readiness depends on characterizing this.
- **Why Possibly Novel:** Missing-modality methods exist; the peak-vs-robustness trade-off quantification with the "is it fundamental?" framing is not established for segmentation.
- **Minimal Experiment:** Train {vanilla, sequence-dropout, routed} models on BraTS-style data; evaluate all 2^n sequence subsets; compare complete-input and worst-case scores.
- **Main Risk:** Router models add capacity; match parameter counts to keep the comparison fair.

### IDEA-A-0111
- **One-sentence idea:** Test whether resampling anisotropic medical volumes to isotropic grids — the universal preprocessing default — actually helps modern segmentation models, or whether native-resolution processing with anisotropy-aware position encoding is superior.
- **Problem:** Isotropic resampling interpolates invented voxels and blurs the thin-slice axis; the practice predates learned position encodings, and its cost-benefit has not been re-examined for transformer-era models.
- **Core Hypothesis (falsifiable):** For volumes with anisotropy ratio >3, native-grid processing with scaled position encodings beats isotropic resampling by >2 Dice on thin structures, while for near-isotropic data the difference is nil — resampling is a legacy habit whose harm scales with anisotropy.
- **Why Important:** Changes a preprocessing default embedded in virtually every medical pipeline including nnU-Net.
- **Why Possibly Novel:** Anisotropy handling is studied within CNN receptive-field design; a transformer-era re-audit of the resampling default is missing.
- **Minimal Experiment:** 4 datasets spanning anisotropy ratios; {resample, native+scaled-PE} × 2 architectures; stratify by structure thickness.
- **Main Risk:** nnU-Net's pipeline entangles resampling with patch-size heuristics; careful isolation required.

### IDEA-A-0112
- **One-sentence idea:** Detect and quantify silent annotation-protocol drift across versions of long-lived medical benchmarks (organ boundary conventions changing between releases) and its effect on longitudinal method comparisons.
- **Problem:** Benchmarks evolve (re-annotations, added cases, convention updates); papers compare against numbers from different versions as if constant — the magnitude of version drift is unknown.
- **Core Hypothesis (falsifiable):** For ≥2 major benchmarks, inter-version ground-truth changes alone shift a frozen model's Dice by more than typical claimed improvements (>1 Dice), invalidating naive cross-version comparisons in the literature.
- **Why Important:** Establishes version-pinning and drift-reporting as required practice, and flags which historical comparisons are unsound.
- **Why Possibly Novel:** Dataset versioning issues are discussed in ML-ops; a quantified medical-benchmark drift audit with literature impact analysis is new.
- **Minimal Experiment:** Evaluate frozen public checkpoints on multiple versions of 3 benchmarks; catalog GT changes; survey papers for cross-version comparisons.
- **Main Risk:** Old versions may be hard to obtain; archive collaboration needed.

### IDEA-A-0113
- **One-sentence idea:** Test whether natural-image VFMs transfer to ultrasound *at all* in a stratified way, given that speckle violates the additive-noise and edge-statistics assumptions of natural-image pretraining.
- **Problem:** Ultrasound's multiplicative speckle and view-dependent anatomy are maximally far from web-image statistics; blanket claims about VFM medical transfer may hide near-total failure on US-specific structure.
- **Core Hypothesis (falsifiable):** VFM transfer gains over from-scratch training on ultrasound segmentation vanish (<1 Dice) once the from-scratch model receives speckle-appropriate augmentation, whereas the same comparison on CT/X-ray retains >5 Dice VFM advantage — VFM value is modality-statistics-dependent.
- **Why Important:** Ultrasound is the most accessible global imaging modality; knowing whether foundation features help determines resource allocation for US AI.
- **Why Possibly Novel:** VFM-transfer studies average over modalities; the speckle-controlled, augmentation-matched ultrasound isolation is new.
- **Minimal Experiment:** 3 US tasks + 2 CT tasks; {VFM fine-tune, scratch + speckle augmentation}; compare modality-wise VFM deltas.
- **Main Risk:** "Speckle-appropriate augmentation" must be strong to be a fair champion; involve US physics expertise.

### IDEA-A-0114
- **One-sentence idea:** Evaluate SAM2 as a surgical-video tissue tracker and test whether its memory model — built for object permanence of rigid things — systematically fails on deforming, self-similar tissue.
- **Problem:** Surgical AR/robotics wants off-the-shelf tissue tracking; SAM2's memory assumes appearance persistence, which deforming, bleeding, cauterized tissue violates in specific ways nobody has profiled.
- **Core Hypothesis (falsifiable):** SAM2's tissue-tracking failure events concentrate at (a) deformation-rate spikes and (b) appearance-change events (cautery, bleeding, irrigation) with >70% of failures within 1 s of such events — failure is event-driven, not gradual, making event-triggered re-prompting a viable fix.
- **Why Important:** Event-driven failure means cheap deployment guards (re-prompt on detected events) rather than full retraining.
- **Why Possibly Novel:** Surgical SAM2 evaluations report averages; the event-aligned failure analysis with the re-prompting implication is new.
- **Minimal Experiment:** Annotate event timestamps in surgical clips (public cholecystectomy datasets); align SAM2 failure onsets with events; prototype event-triggered re-prompting.
- **Main Risk:** Event annotation is subjective; use multiple annotators with adjudication.

### IDEA-A-0115
- **One-sentence idea:** Quantify the context radius that histopathology structures actually require, testing whether gigapixel "context starvation" of patch-based models is a real accuracy bottleneck or a myth.
- **Problem:** Patch-based processing is blamed for missing long-range context in pathology, motivating expensive whole-slide architectures — but the required context radius per structure/diagnostic task has never been measured directly.
- **Core Hypothesis (falsifiable):** For ≥80% of common segmentation targets (glands, tumor regions), oracle experiments show accuracy saturates at context radii ≤2× current patch sizes, and only rare tasks (invasion-front delineation) benefit from >4× context — whole-slide context is over-sold for segmentation.
- **Why Important:** Prevents (or justifies) a costly architectural arms race in computational pathology with a direct measurement.
- **Why Possibly Novel:** Context ablations exist per-model; a model-agnostic oracle *context-radius requirement* measurement per structure is new.
- **Minimal Experiment:** Train/evaluate with concentric context-cropped inputs at multiple radii for 6 pathology targets; fit saturation curves per target.
- **Main Risk:** Saturation depends on model capacity; replicate with 2 capacities to separate model-limited from information-limited saturation.

### IDEA-A-0116
- **One-sentence idea:** Measure how often model *rankings* on medical segmentation flip between Dice, HD95, surface-Dice, and lesion-wise detection metrics, and derive which metric predicts downstream clinical-task utility.
- **Problem:** Papers optimize and report Dice, but clinical utility may track boundary or lesion-detection metrics; if rankings disagree substantially, single-metric leaderboards are misleading in unquantified ways.
- **Core Hypothesis (falsifiable):** Metric-pair ranking disagreement exceeds 25% across published models on standard tasks, and a downstream surrogate task (e.g., volumetry error, RT-margin coverage) is predicted best by surface-based metrics, not Dice.
- **Why Important:** Grounds metric choice in downstream utility, replacing convention with evidence — the metric question determines what the field optimizes.
- **Why Possibly Novel:** Metric criticism is perennial; the systematic ranking-flip quantification plus a downstream-utility anchor is the missing empirical piece.
- **Minimal Experiment:** Re-evaluate 15 released models across 4 metrics on 4 tasks; compute ranking stability; define one downstream surrogate per task and test predictiveness.
- **Main Risk:** Downstream surrogates require clinical grounding; choose ones with existing literature (volumetry, margins).

### IDEA-A-0117
- **One-sentence idea:** Measure the noise floor of report-derived weak supervision: how accurately can radiology-report text localize findings, bounding the best possible text-supervised medical grounding.
- **Problem:** Text-supervised medical segmentation is a growing field, but reports describe findings with intrinsic spatial vagueness ("right lower lobe"); the information-theoretic ceiling of report-based localization is unmeasured, so progress claims lack a reference.
- **Core Hypothesis (falsifiable):** Expert humans given only report text localize findings with a median oracle-overlap corresponding to a coarse-region ceiling (HYPOTHESIS: lobe/quadrant level, not lesion level), and current text-supervised models already operate within 20% of that human ceiling — the bottleneck is the supervision, not the models.
- **Why Important:** If models are at the supervision ceiling, further architecture work is futile and effort must shift to richer supervision (measurements, keyframes).
- **Why Possibly Novel:** The human-referee ceiling measurement for report-based localization has not been established.
- **Minimal Experiment:** Radiologists localize 200 findings from text alone (no image-specific hints beyond the report); compare model and human localization distributions.
- **Main Risk:** Reports vary hugely in specificity; stratify by report detail level.

### IDEA-A-0118
- **One-sentence idea:** Test how segmentation models fail on post-surgical and anatomically variant patients, quantifying the "atlas prior" dependence of modern learned models.
- **Problem:** Learned models may implicitly encode normal-anatomy atlases; post-surgical absence (resected organs), transplants, and congenital variants then trigger hallucinated structures — a patient-safety failure mode without a benchmark.
- **Core Hypothesis (falsifiable):** On post-resection cases, models hallucinate the absent organ (predict >20% of its typical volume) in ≥40% of cases, and hallucination rate correlates with the organ's positional consistency in training data — models segment "where organs usually are."
- **Why Important:** Hallucinating absent anatomy is among the most dangerous silent failures for clinical use; establishing and benchmarking it forces mitigation.
- **Why Possibly Novel:** Atlas-prior dependence is discussed for registration-based methods; its quantification in deep segmentation models with a positional-consistency predictor is new.
- **Minimal Experiment:** Assemble post-surgical cases (nephrectomy, pneumonectomy) from public data; measure hallucinated-volume statistics across 5 models; test the consistency correlation.
- **Main Risk:** Post-surgical public data is scarce; synthetic organ-removal (inpainting) can extend the set with realism checks.

### IDEA-A-0119
- **One-sentence idea:** Test whether models trained with synthetic-lesion insertion learn lesion appearance or the *insertion artifacts*, using artifact-free rendering and forensic-detector analysis.
- **Problem:** Synthetic lesion augmentation is popular for rare pathologies, but if blending leaves forensic traces, models may key on artifacts — inflating validation scores and collapsing on real lesions.
- **Core Hypothesis (falsifiable):** A forensic classifier can detect standard lesion insertions with >90% AUC, and segmentation models trained on detectable insertions drop >2× more on real-lesion test sets than models trained on forensically undetectable insertions — artifact learning is real and measurable.
- **Why Important:** Establishes a quality-control criterion (forensic undetectability) for all synthetic medical data pipelines.
- **Why Possibly Novel:** Insertion realism is assessed visually; the forensic-detectability criterion linked causally to downstream degradation is new.
- **Minimal Experiment:** Create insertion sets at graded realism; train forensic detectors and segmentation models; correlate detectability with real-data generalization.
- **Main Risk:** Achieving "forensically undetectable" insertions may be hard; even so, the correlation across the realism gradient answers the question.

### IDEA-A-0120
- **One-sentence idea:** Identify the conditions under which clinician+model segmentation outperforms both alone, testing whether complementarity requires *calibrated disagreement signals* rather than raw accuracy.
- **Problem:** Human-AI teaming studies in classification show automation bias and complementarity failures; for segmentation — where the interaction is spatial editing — the conditions for genuine complementarity are unstudied.
- **Core Hypothesis (falsifiable):** Team performance exceeds the best individual only when the model exposes calibrated per-region confidence (letting clinicians triage where to edit); without it, clinicians over-accept model masks and team performance falls below the clinician-alone level on hard cases.
- **Why Important:** Determines the interface requirements for safe clinical deployment of segmentation assistance — accuracy alone provably won't suffice if the hypothesis holds.
- **Why Possibly Novel:** Automation-bias literature exists for detection/classification; the spatial-editing segmentation version with confidence-interface manipulation is new.
- **Minimal Experiment:** Within-subject clinician study: edit model masks under {no confidence, calibrated confidence, miscalibrated confidence} interfaces on matched case sets; compare team error profiles.
- **Main Risk:** Human-study logistics and IRB; start with trainees and simulated clinical stakes.

---

## Cluster 6 — Smoke & Fire Segmentation: Physics, Ground Truth, Deployment (IDEA-A-0121 … 0140)

### IDEA-A-0121
- **One-sentence idea:** Demonstrate that binary smoke masks are ill-posed ground truth by measuring annotator threshold inconsistency, and propose density-graded ground truth as the corrected task definition.
- **Problem:** Smoke has no boundary — annotators binarize a continuous density field at arbitrary personal thresholds, so smoke-segmentation benchmarks may largely measure threshold mimicry, capping and distorting all reported progress.
- **Core Hypothesis (falsifiable):** Inter-annotator disagreement on smoke masks concentrates in low-density regions and corresponds to annotators applying different implicit density thresholds (recoverable as a per-annotator scalar), such that a single density map explains >80% of inter-annotator mask variance.
- **Why Important:** If a scalar threshold explains the disagreement, the field should regress density and let applications choose thresholds — redefining the task rather than chasing noise.
- **Why Possibly Novel:** Smoke datasets exist with binary masks; the threshold-decomposition analysis of annotator behavior and the resulting task redefinition are new.
- **Minimal Experiment:** 5 annotators mask 200 smoke images; fit per-annotator threshold models over an estimated density proxy (e.g., dark-channel/transmission); measure explained variance.
- **Main Risk:** Density proxies may be poor on complex backgrounds; validate proxies on synthetic smoke with known density first.

### IDEA-A-0122
- **One-sentence idea:** Use atmospheric transmission physics (Beer–Lambert attenuation) to derive alpha-matte smoke ground truth from smoke/no-smoke image pairs, creating physically defined labels without human thresholding.
- **Problem:** Human smoke labels are threshold-arbitrary (IDEA-A-0121); paired imagery (fixed cameras before/during smoke) permits computing per-pixel transmittance as physically meaningful ground truth, which nobody has operationalized into a benchmark.
- **Core Hypothesis (falsifiable):** Transmittance maps computed from pairs are reproducible across illumination-matched pairs (correlation >0.9), and models trained to regress transmittance transfer better to unseen scenes (>10% relative error reduction) than binary-mask-trained models thresholded post hoc.
- **Why Important:** Provides the first physically grounded supervision signal for the wildfire-detection domain, where early low-density smoke is exactly what matters.
- **Why Possibly Novel:** Transmission estimation exists in dehazing; using it to *define ground truth* for smoke segmentation benchmarks is a new construction.
- **Minimal Experiment:** Collect/assemble fixed-camera pairs (wildfire camera archives); compute transmittance labels; train regression vs binary models; evaluate cross-scene.
- **Main Risk:** Illumination changes between pair frames corrupt transmittance; restrict to short-interval pairs and model illumination explicitly.

### IDEA-A-0123
- **One-sentence idea:** Test whether fire segmentation models are mostly color detectors, via hue-manipulation stress tests and colored-distractor benchmarks (sunsets, neon, brake lights).
- **Problem:** Fire has a distinctive color signature, inviting a spectral shortcut; if models are ~color thresholds with extra steps, they will fail on atypical flames (methanol, gas burners) and false-alarm on red/orange distractors — unquantified in current benchmarks.
- **Core Hypothesis (falsifiable):** State-of-the-art fire segmenters lose >50% IoU on hue-shifted flames while confidently segmenting >30% of matched colored distractors — performance is explained predominantly by chromatic features, not structure or motion.
- **Why Important:** Fire detection is safety-critical; a color shortcut means predictable catastrophic failures (blue gas flames missed, sunsets flagged).
- **Why Possibly Novel:** Color dependence is suspected folklore; the controlled hue-intervention quantification with distractor benchmarks is not published.
- **Minimal Experiment:** Build hue-shifted flame sets (real atypical flames + controlled shifts) and a distractor set; evaluate 5 public fire models; decompose feature reliance.
- **Main Risk:** Hue-shifting real flames synthetically may create artifacts; anchor with genuinely atypical-flame photos (gas, chemical fires).

### IDEA-A-0124
- **One-sentence idea:** Build the smoke/fog/steam/cloud/dust confusion benchmark and test whether any visual model can separate these physically distinct but visually similar aerosols from single frames.
- **Problem:** Wildfire systems must distinguish smoke from look-alike aerosols, but no benchmark isolates this five-way confusion, and it is unknown whether single-frame separation is even information-theoretically feasible.
- **Core Hypothesis (falsifiable):** Single-frame human expert accuracy on the five-way task is barely above chance for distant plumes (<45% vs 20% chance), while short temporal clips restore human accuracy to >80% — the discrimination is fundamentally temporal, and single-frame models are structurally capped.
- **Why Important:** If discrimination is temporal, the industry's single-frame smoke detectors have a hard false-alarm floor — an architecture-independent conclusion that changes system design.
- **Why Possibly Novel:** False-alarm categories are known operationally; the human-referenced single-frame-vs-clip information analysis is new science for the domain.
- **Minimal Experiment:** Curate a five-way aerosol dataset with clips; run human studies (frame vs clip); benchmark models under both input regimes.
- **Main Risk:** Ground-truth aerosol identity needs metadata (fire reports, weather records); curation is the main effort.

### IDEA-A-0125
- **One-sentence idea:** Test whether the turbulence statistics of smoke motion (spectral signatures of buoyant plumes) provide a self-supervision signal that separates smoke from all rigid-world motion without labels.
- **Problem:** Smoke's defining property is its dynamics (buoyancy-driven turbulence), yet self-supervised smoke detection from motion statistics — rather than appearance — remains untested as a primary signal.
- **Core Hypothesis (falsifiable):** A classifier over local spatiotemporal spectra (no appearance features) achieves >0.9 AUC separating smoke regions from moving rigid objects, vegetation, and camera shake, and pretraining on this signal improves downstream smoke segmentation with 10× fewer labels.
- **Why Important:** A physics-grounded, appearance-free signal would be robust to exactly the shifts (color, lighting, geography) that break appearance models.
- **Why Possibly Novel:** Optical-flow features have been used ad hoc; the turbulence-spectrum formulation as a self-supervised pretext for segmentation is new.
- **Minimal Experiment:** Compute spatiotemporal spectral features on labeled wildfire clips; test the motion-only classifier; pretrain a video encoder on the pretext and fine-tune with limited labels.
- **Main Risk:** Distant smoke moves few pixels between frames; characterize the minimum apparent-motion regime where the signal exists.

### IDEA-A-0126
- **One-sentence idea:** Replace IoU with detection-latency (time from first visible smoke to first correct alarm-grade mask) as the primary metric for wildfire smoke systems, and test whether IoU-optimal models are latency-suboptimal.
- **Problem:** Wildfire response cares about minutes-to-detection of faint early smoke, but the field optimizes IoU on developed plumes; the two objectives may rank models differently, misdirecting research.
- **Core Hypothesis (falsifiable):** On time-stamped ignition sequences, model rankings by median detection latency disagree with IoU rankings (rank correlation <0.5), and latency winners share high recall on low-density smoke rather than high boundary accuracy.
- **Why Important:** Realigning the metric with the mission could redirect the entire subfield's optimization target toward what saves forests.
- **Why Possibly Novel:** Latency metrics exist in event detection; their application and the ranking-disagreement demonstration for smoke *segmentation* are new.
- **Minimal Experiment:** Assemble ignition-to-detection sequences from wildfire camera archives; evaluate 6 models by latency and IoU; compare rankings.
- **Main Risk:** True ignition timestamps are approximate; use first-human-visible frame as the anchor with multiple annotators.

### IDEA-A-0127
- **One-sentence idea:** Determine which fidelity dimension of synthetic smoke (color spectrum, transparency compositing, or turbulent motion) matters most for sim-to-real transfer, via factor-controlled rendering.
- **Problem:** Synthetic smoke data is cheap, but renderers vary in physical fidelity along separable axes, and nobody knows which axis buys generalization — so effort is spent uniformly or arbitrarily.
- **Core Hypothesis (falsifiable):** Transfer performance is dominated by transparency-compositing fidelity (correct alpha over real backgrounds), with photometric spectrum fidelity contributing <20% of the gap and motion fidelity mattering only for video models — a factor ranking stable across test domains.
- **Why Important:** Tells every synthetic-smoke pipeline where to invest rendering effort, and by extension informs synthetic data design for all transparent phenomena.
- **Why Possibly Novel:** Sim-to-real factor analysis exists for rigid objects (texture/lighting); the transparency-specific factor decomposition is new.
- **Minimal Experiment:** Render smoke datasets varying each fidelity axis independently (2×2×2 factorial); train identical models; evaluate on real smoke benchmarks; fit factor effects.
- **Main Risk:** Factors interact (motion fidelity is invisible without transparency fidelity); the factorial design must include interactions.

### IDEA-A-0128
- **One-sentence idea:** Systematically quantify SAM/SAM2's failure on smoke across prompt strategies, testing whether *any* prompting scheme (multi-point, box, dense grid, video propagation) recovers usable smoke masks.
- **Problem:** SAM is being wired into wildfire pipelines as a zero-shot labeler, but its edge-driven mask prior (cf. IDEA-A-0006) is maximally mismatched to boundary-free smoke — the practical recoverability question is unanswered.
- **Core Hypothesis (falsifiable):** No prompt strategy raises SAM's smoke IoU above 0.5× a small supervised baseline's; failures are shrinkage-to-dense-core (predictable from the density field), meaning SAM masks systematically under-cover exactly the low-density smoke that matters for early detection.
- **Why Important:** A definitive negative result would stop the community from building wildfire auto-labeling on an unfit foundation, and the shrinkage law quantifies the bias any SAM-derived smoke dataset inherits.
- **Why Possibly Novel:** "SAM fails on smoke" is anecdote; the exhaustive prompt-strategy audit with the density-conditioned shrinkage characterization is not published.
- **Minimal Experiment:** On 3 smoke datasets, sweep prompt strategies × SAM variants; measure IoU and density-stratified coverage; compare to a small supervised U-Net.
- **Main Risk:** Density stratification requires density estimates (link to IDEA-A-0122); use paired-frame or synthetic subsets where density is known.

### IDEA-A-0129
- **One-sentence idea:** Measure how much of fire/smoke benchmark performance comes from *scene context* rather than fire/smoke appearance, by testing on context-swapped and context-only images.
- **Problem:** Fire datasets pair flames with fire-typical scenes (forests, burnt structures); models may detect the scene, not the fire, inflating benchmarks and guaranteeing false alarms on fire-typical scenes without fire.
- **Core Hypothesis (falsifiable):** Models score >0.3 IoU-equivalent activation on fire-scene images with fire removed (context-only), and lose >40% performance on fires composited into atypical scenes — context contributes a large, quantifiable fraction of reported accuracy.
- **Why Important:** Context reliance is a hidden false-alarm engine for deployed systems; quantifying it forces context-controlled benchmark design.
- **Why Possibly Novel:** Context bias is studied for object recognition; the fire-domain quantification with context-only false-alarm measurement is new.
- **Minimal Experiment:** Build context-only (fire inpainted out) and context-swapped (fire composited into neutral scenes) test sets; evaluate 5 models; decompose performance.
- **Main Risk:** Inpainting/compositing artifacts; use high-quality generative inpainting with forensic checks (cf. IDEA-A-0119).

### IDEA-A-0130
- **One-sentence idea:** Characterize the day/night regime shift in fire segmentation — saturation-dominated night imagery vs texture-visible day imagery — and test whether one model can span both or the regimes require exposure-conditioned processing.
- **Problem:** Night fire appears as saturated blobs (no texture), day fire as textured flames; models trained on mixed data may compromise both regimes, and the regime structure is unexamined.
- **Core Hypothesis (falsifiable):** A single mixed-trained model underperforms per-regime specialists by >8 IoU in each regime, and the gap traces to conflicting feature reliance (texture vs intensity-geometry) demonstrable by feature-attribution divergence — regime conditioning (not more data) closes it.
- **Why Important:** Fires burn at night; deployment systems need to know whether time-of-day conditioning is architecturally necessary.
- **Why Possibly Novel:** Day/night domain gaps are studied for driving; the saturation-regime analysis specific to emissive phenomena (fire as light source) is new.
- **Minimal Experiment:** Split fire benchmarks by exposure regime; train mixed vs specialist vs exposure-conditioned models; compare with attribution analysis.
- **Main Risk:** Night fire data is scarcer; balance evaluation sets to avoid regime-size confounds.

### IDEA-A-0131
- **One-sentence idea:** Challenge RGB+IR fusion papers for fire detection by testing whether calibrated IR alone matches fusion performance, isolating RGB's marginal value.
- **Problem:** Multimodal fusion papers claim RGB+thermal synergy for fire, but rarely include a well-tuned IR-only baseline; fire is a thermal phenomenon, so RGB's contribution may be negligible or even negative (false-alarm source).
- **Core Hypothesis (falsifiable):** A tuned IR-only model comes within 2 IoU of published fusion models on their own benchmarks, and RGB's marginal value concentrates entirely in sub-resolution distant fires where thermal pixels saturate or blur — fusion helps in a narrow, specifiable regime.
- **Why Important:** Sensor selection drives system cost; if IR-only suffices, deployments simplify, and fusion research should target the actual marginal-value regime.
- **Why Possibly Novel:** Modality-ablation rigor is rare in this application literature; the regime-localization of fusion value is new.
- **Minimal Experiment:** Reproduce 4 fusion benchmarks; add tuned single-modality baselines; stratify the fusion delta by target size/distance.
- **Main Risk:** Public RGB-IR fire datasets are few; may need to include industrial/thermal datasets as proxies.

### IDEA-A-0132
- **One-sentence idea:** Reformulate smoke understanding as continuous density-field regression and test whether regression-trained models beat segmentation-trained models even on the original binary-mask benchmarks.
- **Problem:** If binary masks are thresholded density (IDEA-A-0121), then regression is the natural learning target and binarization should happen at inference — but whether regression training helps or hurts on existing binary benchmarks is an open empirical question.
- **Core Hypothesis (falsifiable):** Models trained to regress proxy density (from dark-channel/paired-frame supervision) and thresholded at test time match or beat directly-binary-trained models on binary IoU while additionally providing calibrated density — regression dominates on the Pareto front.
- **Why Important:** A task reformulation that wins on the old metric while adding physical meaning would be adopted immediately.
- **Why Possibly Novel:** Density regression exists in dehazing; the head-to-head against binary training *on binary benchmarks* is the untested load-bearing claim.
- **Minimal Experiment:** Train matched models under both targets on 2 smoke datasets; evaluate binary IoU (threshold-swept) and density error where available.
- **Main Risk:** Proxy density supervision is noisy; compare several proxies and report supervision-noise sensitivity.

### IDEA-A-0133
- **One-sentence idea:** Build a hard-negative benchmark of the operational false-alarm taxonomy for wildfire cameras (clouds, fog banks, dust, glare, agricultural burns, geysers, chimney steam) with per-category error reporting.
- **Problem:** Deployed wildfire detectors are judged by false-alarm rate, but academic benchmarks contain few hard negatives, so papers report inflated precision that collapses operationally — the negative taxonomy has never been benchmarked.
- **Core Hypothesis (falsifiable):** Current published smoke models exhibit >10× higher false-positive rates on the hard-negative suite than on standard benchmark negatives, with cloud-shadow-on-ridges and fog banks dominating errors — and per-category profiles differ enough across models to enable complementary ensembling.
- **Why Important:** Provides the missing operational evaluation standard for a safety-critical application, directly comparable across research groups.
- **Why Possibly Novel:** Operational teams know the taxonomy internally; no public per-category hard-negative benchmark exists for the research community.
- **Minimal Experiment:** Curate 2k hard negatives across 8 categories from public wildfire camera archives; evaluate 6 public models; publish per-category false-alarm profiles.
- **Main Risk:** Licensing of camera archive imagery; use archives with permissive terms and document provenance.

### IDEA-A-0134
- **One-sentence idea:** Null-test the assumption that temporal modeling helps smoke segmentation: does a video architecture beat single-frame inference plus simple temporal post-filtering at matched compute?
- **Problem:** Video models are assumed necessary for smoke (motion matters!), but heavy temporal architectures may add nothing over cheap temporal aggregation of frame-wise outputs — an unexamined efficiency question with deployment consequences.
- **Core Hypothesis (falsifiable):** At matched compute, frame-model + median/hysteresis temporal filtering achieves ≥95% of the video model's F1 on smoke benchmarks, except specifically for early-detection latency (IDEA-A-0126) where video models win — temporal modeling's value is confined to the faint-smoke regime.
- **Why Important:** Wildfire systems run on edge hardware; if cheap post-filtering suffices except for early detection, system design changes materially.
- **Why Possibly Novel:** The compute-matched video-vs-filtering comparison with regime localization has not been run for smoke.
- **Minimal Experiment:** Compare {frame model, frame+filtering, video model} at matched FLOPs on smoke video benchmarks; stratify by smoke density/age.
- **Main Risk:** The conclusion may be dataset-dependent (camera frame rates vary); replicate across frame-rate regimes.

### IDEA-A-0135
- **One-sentence idea:** Quantify the effect of video-codec compression artifacts on smoke segmentation — wildfire cameras stream heavily compressed video whose block artifacts and temporal smoothing plausibly destroy faint-smoke signal.
- **Problem:** Research models train on high-quality footage but deploy on compressed streams; compression may selectively erase exactly the low-contrast texture that distinguishes early smoke, and the degradation law is unmeasured.
- **Core Hypothesis (falsifiable):** Smoke-detection recall on faint smoke drops superlinearly with compression (quantization parameter), with the knee at bitrates typical of deployed cameras, while dense-smoke performance is compression-insensitive — and augmenting training with codec-degraded data recovers >70% of the loss.
- **Why Important:** Identifies whether a major real-world performance gap is a data-pipeline issue fixable by augmentation rather than modeling.
- **Why Possibly Novel:** Compression robustness is studied for recognition; the faint-signal-selective degradation analysis for safety monitoring is new.
- **Minimal Experiment:** Re-encode smoke benchmarks across bitrate ladders; measure density-stratified recall; test codec-augmentation recovery.
- **Main Risk:** Synthetic re-encoding may differ from camera-native encoding pipelines; validate on native streams from one deployment.

### IDEA-A-0136
- **One-sentence idea:** Mine weak labels for fire/smoke segmentation from non-visual metadata (alarm timestamps, satellite hotspot detections, dispatch records) and test how far metadata-only supervision can go.
- **Problem:** Pixel labels for fire are scarce, but abundant weak signals exist (a camera's field-of-view had a confirmed fire at time t); the achievable segmentation quality from such spatially unlocalized supervision is unknown.
- **Core Hypothesis (falsifiable):** Combining temporal weak labels with motion/appearance priors (MIL over spatiotemporal proposals) yields segmentation within 15 IoU of fully supervised training, with the residual gap concentrated in smoke-extent (not detection) accuracy.
- **Why Important:** Unlocks orders of magnitude more training signal for a label-starved safety domain, and tests the general limits of temporally-localized, spatially-free supervision.
- **Why Possibly Novel:** MIL weak supervision is classic; the cross-referenced metadata construction (satellite hotspots + camera geometry) as a supervision source is new engineering-science.
- **Minimal Experiment:** Assemble camera archives cross-referenced with fire records; train MIL models; compare against a fully supervised subset.
- **Main Risk:** Metadata timestamps and geolocations are noisy; quantify label noise explicitly before modeling.

### IDEA-A-0137
- **One-sentence idea:** Use physical plume-dynamics consistency (masks over time obeying advection-diffusion behavior) as an unsupervised quality score for smoke segmentation, testing whether physics-consistency predicts accuracy without ground truth.
- **Problem:** Deployed smoke systems cannot measure their own accuracy; a physics-consistency check (does the mask sequence evolve like a plume?) could provide reference-free quality monitoring — validity untested.
- **Core Hypothesis (falsifiable):** A physics-consistency score (fit residual of mask evolution to a simple advection-diffusion model) correlates with true IoU at ρ > 0.7 across models and scenes, and flags failure cases (context false alarms, cloud confusion) whose "masks" evolve unphysically.
- **Why Important:** Reference-free quality monitoring is the missing piece for autonomous wildfire systems that must self-report reliability.
- **Why Possibly Novel:** Physics consistency is used in fluid ML; as a *label-free evaluation instrument* for segmentation it is unexplored.
- **Minimal Experiment:** Compute consistency scores for multiple models on labeled smoke videos; measure score-IoU correlation; test false-alarm discrimination.
- **Main Risk:** Wind-field variability may make simple advection models too loose; may need coarse wind estimates from consecutive frames.

### IDEA-A-0138
- **One-sentence idea:** Test whether better smoke segmentation masks actually improve downstream fire-spread forecasting — the assumed but unverified utility chain of the entire subfield.
- **Problem:** Smoke/fire segmentation research justifies itself by downstream utility (spread prediction, resource dispatch), but the sensitivity of downstream forecasts to mask quality has never been measured — maybe coarse blobs suffice.
- **Core Hypothesis (falsifiable):** Fire-spread forecast error is insensitive to mask boundary quality (saturating at coarse IoU ≈ 0.5) but highly sensitive to detection latency and plume-base localization — the field is optimizing dimensions the application doesn't need.
- **Why Important:** Aligning the research objective with true downstream sensitivity could redirect effort from boundary refinement to latency and localization (cf. IDEA-A-0126).
- **Why Possibly Novel:** Downstream-utility sensitivity analysis is rare anywhere in segmentation; for wildfire it has never been done.
- **Minimal Experiment:** Feed degraded masks (controlled IoU/latency/localization perturbations) into an established spread model (e.g., Rothermel-based simulators); measure forecast-error sensitivity per perturbation axis.
- **Main Risk:** Spread models have their own error floors that may mask sensitivity; use multiple simulators and synthetic scenario ground truth.

### IDEA-A-0139
- **One-sentence idea:** Investigate whether smoke plumes should be treated as *instances* with persistent identity (per-plume tracking) rather than "stuff," and whether instance identity is even well-defined when plumes merge and split.
- **Problem:** Multi-fire scenarios need per-source attribution ("which plume comes from which ignition"), but smoke is annotated as amorphous stuff; whether plume instance identity is definable and learnable is an open conceptual and empirical question.
- **Core Hypothesis (falsifiable):** Human annotators agree on plume-instance identity (>80% temporal consistency) up to merge events but not after them, defining a principled identity horizon; models can match human identity assignment up to that horizon using source-localization features.
- **Why Important:** Per-source attribution changes wildfire response (multiple ignitions = suspected arson, different dispatch); it requires resolving the identity formalism first.
- **Why Possibly Novel:** Video instance segmentation assumes solid objects; the fluid-instance identity problem with a merge-horizon formalism is unexplored.
- **Minimal Experiment:** Multi-annotator plume-identity labeling on multi-source fire videos; measure agreement structure; train and evaluate identity assignment up to the horizon.
- **Main Risk:** Multi-source footage is rare; augment with controlled burn footage and synthetic multi-plume scenes.

### IDEA-A-0140
- **One-sentence idea:** Quantify cross-geography generalization of wildfire smoke models (vegetation type, atmospheric conditions, terrain) and identify which environmental factor drives the transfer gap.
- **Problem:** Smoke models trained on one region (e.g., California camera networks) are deployed elsewhere (Mediterranean, Australia) with unknown degradation, and the causal factor (fuel type changes smoke color/density vs terrain changes background) is unidentified.
- **Core Hypothesis (falsifiable):** Cross-region degradation is driven predominantly by *background* ecosystem appearance (false-alarm shift), not smoke appearance itself — smoke-region recall transfers within 5%, while false-positive rates rise >5×, localizing the problem to negative-class shift.
- **Why Important:** If the gap is negative-class-driven, the fix is cheap regional hard negatives, not smoke data collection — an actionable decomposition for global deployment.
- **Why Possibly Novel:** Cross-region evaluation with recall/false-positive decomposition attributing the gap has not been published for this domain.
- **Minimal Experiment:** Train on one region's cameras, test on 3 others; decompose error into smoke-recall vs background-false-positive components; test regional-negative fine-tuning.
- **Main Risk:** Regional datasets differ in camera hardware too; include camera-model covariates in the analysis.

---

## Cluster 7 — Transparent, Mirror & Ambiguous Object Segmentation (IDEA-A-0141 … 0160)

### IDEA-A-0141
- **One-sentence idea:** Test whether deep features computed *on* transparent objects encode the background seen through them rather than the object, making transparency a representational (not just detection) failure.
- **Problem:** Transparent objects violate the assumption that pixel appearance belongs to the surface at that pixel; whether backbone features on glass regions represent "glass" or "the background behind glass" is unmeasured and determines what any downstream head can do.
- **Core Hypothesis (falsifiable):** Linear probes on patch features within glass regions decode the *background* class with >70% accuracy but "glass present" with <55% (near chance for hard cases) across major VFMs — the representation itself is transparent to transparency.
- **Why Important:** If features don't encode transparency, no decoder can recover it, and the fix must be at the representation-learning level — a field-redirecting conclusion.
- **Why Possibly Novel:** Transparency papers propose detectors; the representational-content probing question (what do features on glass encode?) has not been asked.
- **Minimal Experiment:** On Trans10K-style data with known backgrounds, train probes on frozen VFM features for background-class and glass-presence decoding; compare across VFMs and layers.
- **Main Risk:** Glass regions contain boundary/specular pixels that leak glass evidence; analyze interior vs edge patches separately.

### IDEA-A-0142
- **One-sentence idea:** Test whether adding depth input *hurts* transparent-object segmentation — since depth sensors return the background or noise on glass — inverting the usual "more modalities help" assumption.
- **Problem:** RGB-D models are assumed superior, but on transparent surfaces depth is systematically wrong (returns background depth or dropout), potentially teaching models an anti-glass shortcut; the sign of depth's contribution on transparency is unestablished.
- **Core Hypothesis (falsifiable):** RGB-D models underperform RGB-only models on transparent-object IoU by >5 points when depth is naively fused, but *depth-invalidity* (the dropout/mismatch pattern itself) used as an explicit feature outperforms both — the sensor's failure is the best transparency cue.
- **Why Important:** Reframes a sensor failure as signal, with direct consequences for robotic grasping and navigation stacks that currently trust depth.
- **Why Possibly Novel:** Depth unreliability on glass is known in robotics; the systematic sign-of-contribution study and invalidity-as-feature formalization for segmentation are new.
- **Minimal Experiment:** On RGB-D transparency datasets (ClearGrasp-style), train {RGB, naive RGB-D, RGB + depth-validity-mask} models; compare on transparent and opaque classes.
- **Main Risk:** Depth invalidity patterns are sensor-specific (stereo vs ToF vs structured light); replicate across sensor types.

### IDEA-A-0143
- **One-sentence idea:** Test the hypothesis that for transparent objects, supervision should be concentrated on boundaries and specular highlights because interior pixels carry background (hence misleading) gradients.
- **Problem:** Standard training weights all mask pixels equally, but a glass interior's appearance is the background — supervising "glass" on background-looking pixels may actively teach wrong associations, an unexamined training pathology specific to transparency.
- **Core Hypothesis (falsifiable):** Reweighting the loss toward boundary/highlight pixels (down-weighting interiors) improves transparent-object IoU by >5 points at fixed architecture, while the same reweighting *hurts* opaque classes — confirming the interior-gradient pathology is transparency-specific.
- **Why Important:** A principled, near-free training fix derived from the physics of the failure, not architecture stacking.
- **Why Possibly Novel:** Boundary-weighted losses exist generically; the transparency-specific causal rationale (interior gradients are wrong, not just less informative) and the opaque-class control are new.
- **Minimal Experiment:** Train matched models with interior-weight sweeps on Trans10K + an opaque control dataset; verify the predicted interaction.
- **Main Risk:** Interior pixels may still carry refraction cues the hypothesis undervalues; the weight sweep (not binary ablation) will reveal this.

### IDEA-A-0144
- **One-sentence idea:** Test whether jointly predicting the reflection and transmission layers (layer decomposition) is necessary for robust glass segmentation, or whether segmentation-only training implicitly learns the decomposition.
- **Problem:** Glass appearance mixes reflected and transmitted light; it is unknown whether segmentation models must explicitly disentangle these layers or whether the mixture is separable enough for direct discrimination.
- **Core Hypothesis (falsifiable):** Features from segmentation-only glass models cannot linearly decode reflection-layer strength (R² < 0.2), and adding a decomposition auxiliary task improves segmentation specifically on high-reflection cases (>8 IoU on the top-reflection quartile, no gain elsewhere).
- **Why Important:** Localizes when physical disentanglement is required — informing all mixed-appearance domains (wet surfaces, windows, water).
- **Why Possibly Novel:** Reflection removal and glass segmentation exist as separate literatures; the necessity question connecting them (does one need the other?) is untested.
- **Minimal Experiment:** Quantify per-image reflection strength on glass datasets; evaluate segmentation stratified by it; add decomposition auxiliaries and measure the stratified delta.
- **Main Risk:** Reflection-strength ground truth requires estimation; use polarization-captured subsets or synthetic renders for calibration.

### IDEA-A-0145
- **One-sentence idea:** Audit SAM's transparency behavior on Trans10K-class data: does it segment the glass, the background through it, or an inconsistent mixture depending on prompt placement?
- **Problem:** SAM's behavior on transparent objects is anecdotally erratic; characterizing *what SAM thinks the object is* under different prompts on glass would define the failure precisely and test whether prompt engineering can rescue it.
- **Core Hypothesis (falsifiable):** Click prompts on low-reflection glass interiors return background-object masks in >60% of cases, while clicks on highlights/edges return glass masks — SAM's output on transparency is bimodally controlled by local prompt evidence, and no single prompt policy exceeds 0.6 IoU on hard transparent categories.
- **Why Important:** SAM-based auto-labeling silently mislabels transparent regions in every dataset it touches; the prompt-conditioned failure map tells users exactly when not to trust it.
- **Why Possibly Novel:** Transparency failure is mentioned in passing in SAM analyses; the prompt-placement-conditioned bimodality characterization is new.
- **Minimal Experiment:** Dense prompt-position sweeps on 500 transparent objects; classify output masks (glass/background/mixture); map outcome vs local prompt-site features.
- **Main Risk:** GT for "the background object behind glass" needs annotation; label a subset for the three-way outcome classification.

### IDEA-A-0146
- **One-sentence idea:** Study amodal completion for transparent occluders: when object A is seen through glass B, can models segment A completely and B simultaneously — a double-assignment problem standard formulations cannot express?
- **Problem:** Standard segmentation assigns each pixel one label, but pixels showing an object through glass legitimately belong to both; the representational inadequacy is unaddressed, and datasets force arbitrary single assignments.
- **Core Hypothesis (falsifiable):** Models trained with overlapping (multi-label) masks for see-through configurations outperform single-label training by >10 IoU on *both* the occluder and occludee, and single-label training provably caps combined performance (the labels compete).
- **Why Important:** Layered scene understanding through transparency matters for robotics (grasp the glass, not the object behind it) and AR; the formulation fix precedes any architecture work.
- **Why Possibly Novel:** Amodal segmentation handles opaque occlusion; the transparent-occluder double-assignment formulation and its dataset implications are unexplored.
- **Minimal Experiment:** Annotate/synthesize a see-through multi-label dataset; train single-label vs multi-label heads on identical backbones; compare per-layer IoU.
- **Main Risk:** Annotation of behind-glass extents is hard for real images; bootstrap with synthetic renders plus a small real validation set.

### IDEA-A-0147
- **One-sentence idea:** Evaluate segmentation models on *distribution match* to multiple human annotations for intrinsically ambiguous regions (glass edges, shadow boundaries, reflections) instead of single-GT accuracy.
- **Problem:** For ambiguous visual categories there is no single correct mask; evaluating against one annotation punishes models arbitrarily and rewards annotator mimicry, but ambiguity-aware evaluation is absent from transparency/shadow benchmarks.
- **Core Hypothesis (falsifiable):** Model rankings change substantially (rank correlation <0.6) between single-GT IoU and multi-annotator distributional metrics (e.g., generalized energy distance), and models with stochastic/multi-hypothesis heads win under the latter despite losing under the former.
- **Why Important:** The evaluation defines the field's objective; if rankings invert, current benchmarks are steering methods away from honest ambiguity representation.
- **Why Possibly Novel:** Multi-annotator evaluation exists in medical imaging; porting it with ranking-inversion evidence to transparency/shadow domains is new.
- **Minimal Experiment:** Collect 5 annotations each for 300 ambiguous-region images; re-evaluate 6 public models under both regimes; measure ranking stability.
- **Main Risk:** Annotation cost; concentrate on the ambiguous-region subset rather than full images.

### IDEA-A-0148
- **One-sentence idea:** Characterize whether SAM and open-vocab segmenters treat shadows as objects, and formalize the shadow-inclusion convention problem that silently corrupts downstream measurements.
- **Problem:** Shadows attached to objects are inconsistently included/excluded by models and datasets alike; the convention ambiguity injects unmeasured variance into any pipeline computing object size, position, or count.
- **Core Hypothesis (falsifiable):** SAM includes attached shadows in >30% of low-sun-angle object masks (dataset-dependent), open-vocab models do so at systematically different rates per class, and the inconsistency accounts for a measurable fraction (>15%) of apparent inter-model disagreement on outdoor benchmarks.
- **Why Important:** A hidden convention problem that biases all downstream geometry; quantifying it forces explicit shadow policies in datasets and models.
- **Why Possibly Novel:** Shadow detection is its own field; the convention-inconsistency audit across foundation models is new.
- **Minimal Experiment:** Annotate shadow extents for 500 outdoor objects; measure per-model shadow-inclusion rates and their contribution to inter-model mask disagreement.
- **Main Risk:** Shadow attachment is continuous (penumbra); define graded inclusion metrics up front.

### IDEA-A-0149
- **One-sentence idea:** Test whether mirror segmentation in current models is scene-reasoning or texture matching, by evaluating on mirrors whose reflected content is atypical (mirrors reflecting other mirrors, uniform walls, or paintings).
- **Problem:** Mirror detection models may key on "typical reflected content looks like a rotated scene copy" rather than reasoning about reflection geometry; the shortcut predicts specific failures on atypical reflections that no benchmark isolates.
- **Core Hypothesis (falsifiable):** Model performance on mirrors drops >25 IoU when reflected content is atypical (uniform/abstract), while human performance drops <5 — models match reflected-content statistics rather than detecting the mirror surface, unlike humans who use frame/geometry cues.
- **Why Important:** Mirrors cause catastrophic errors in robotics/AR (navigating into mirrors); knowing the mechanism dictates whether to fix data or add geometric reasoning.
- **Why Possibly Novel:** Mirror segmentation datasets exist (MSD-class); the content-atypicality stress test with human referencing is new.
- **Minimal Experiment:** Curate/construct atypical-reflection mirror sets; evaluate 4 mirror-segmentation models + humans; compare degradation profiles and attribution maps.
- **Main Risk:** Atypical mirrors are rare in the wild; controlled photography sessions may be needed to build the set.

### IDEA-A-0150
- **One-sentence idea:** Quantify how much cheap single-shot polarization sensing improves transparency segmentation relative to learning-based RGB methods, establishing whether transparency is a sensing problem or a learning problem.
- **Problem:** Polarization strongly cues specular/transmissive surfaces, but polarization cameras add cost; the field lacks a controlled comparison of "better sensor, simple model" vs "RGB, sophisticated model" for transparency.
- **Core Hypothesis (falsifiable):** A simple model with 4-angle polarization input outperforms the best RGB-only transparency models by >10 IoU on hard glass categories, and the polarization advantage cannot be distilled into RGB models (student-teacher transfer recovers <30% of it) — the information is absent from RGB, not merely unexploited.
- **Why Important:** The distillation test distinguishes "sensor necessary" from "sensor convenient" — a decision-grade result for robotics platform design.
- **Why Possibly Novel:** Polarization segmentation exists; the distillability test that determines information-absence vs exploitation-failure is the new scientific move.
- **Minimal Experiment:** Capture paired RGB+polarization transparency data (or use existing sets); train per-modality models; run cross-modal distillation; compare deltas.
- **Main Risk:** Paired-capture datasets are small; effect sizes must be large to be conclusive at that scale.

### IDEA-A-0151
- **One-sentence idea:** Reformulate wire/mesh/fence segmentation as alpha matting rather than binary segmentation, testing whether sub-pixel structures are fundamentally misdefined as binary masks.
- **Problem:** Fences, wires, and meshes occupy fractional pixels; binary GT forces arbitrary rounding that both corrupts training and caps measurable accuracy — yet thin-structure benchmarks remain binary.
- **Core Hypothesis (falsifiable):** On thin-structure imagery, annotator-independent alpha ground truth (from multi-exposure or synthetic compositing) reveals that binary-trained models systematically overestimate coverage by >30%, and matting-formulated training improves downstream tasks (inpainting removal, robotic wire avoidance) where binary training plateaus.
- **Why Important:** Task redefinition for a whole class of structures ubiquitous in agriculture, infrastructure inspection, and drone navigation.
- **Why Possibly Novel:** Matting and thin-structure segmentation are separate literatures; the claim that binary is *wrong* (not just harder) for sub-pixel structures, with downstream validation, is new.
- **Minimal Experiment:** Build alpha GT via synthetic compositing + real multi-exposure captures; compare binary vs matting training on downstream utility metrics.
- **Main Risk:** Downstream utility tasks must be chosen carefully to avoid favoring either formulation by construction.

### IDEA-A-0152
- **One-sentence idea:** Test whether the refraction-induced distortion field (background warping seen through glass) is a learnable and sufficient cue for localizing transparent objects without any appearance features.
- **Problem:** Refraction warps the background in a physically constrained way, but no work isolates distortion as a standalone transparency cue, so its information content is unknown.
- **Core Hypothesis (falsifiable):** A model given only estimated local distortion fields (from background-prior mismatch or stereo disparity anomalies) localizes refractive objects with >0.5 IoU — comparable to appearance-based methods on textured backgrounds but degrading to chance on textureless backgrounds, mapping exactly where the cue exists.
- **Why Important:** Identifies a complementary, physics-grounded cue with a known validity domain, enabling principled cue fusion instead of monolithic learning.
- **Why Possibly Novel:** Refraction is used in lab-based reconstruction; as an isolated in-the-wild segmentation cue with a validity map, it is unstudied.
- **Minimal Experiment:** Synthesize refractive objects over textured/textureless backgrounds with GT distortion; train distortion-only models; evaluate against appearance-only baselines by background-texture stratum.
- **Main Risk:** In-the-wild distortion estimation is itself hard; the synthetic-first design bounds the cue's ceiling before tackling estimation.

### IDEA-A-0153
- **One-sentence idea:** Audit transparency benchmarks for object-class bias (mostly cups/bottles/windows) and measure how much reported "transparency understanding" is actually container-shape recognition.
- **Problem:** If benchmarks are dominated by a few container shapes, models may recognize "cup-shaped things" rather than transparency per se — inflating perceived progress on the general phenomenon.
- **Core Hypothesis (falsifiable):** Models trained on standard transparency datasets drop >20 IoU on transparent objects with unusual shapes (sculptures, machine parts, sheets) while *opaque* cups/bottles score deceptively high transparency-class confidence — shape, not transparency, drives current models.
- **Why Important:** Reveals whether the field has been solving a narrower problem than claimed, and yields a corrected benchmark composition.
- **Why Possibly Novel:** Class bias audits exist for recognition datasets; the shape-vs-phenomenon dissociation for transparency (including the opaque-container false-positive test) is new.
- **Minimal Experiment:** Assemble unusual-shape transparent and opaque-container test sets; evaluate public models; decompose performance by shape typicality vs actual transparency.
- **Main Risk:** Unusual transparent objects are hard to source; combine web curation with controlled captures.

### IDEA-A-0154
- **One-sentence idea:** Determine whether camouflaged object detection failures are perceptual (features don't separate figure from ground) or attentional (features suffice but saliency/prompting never looks there), using oracle-prompt interventions.
- **Problem:** COD is treated as one problem, but the two failure sources demand opposite fixes (representation learning vs search/prompting); no work cleanly separates them.
- **Core Hypothesis (falsifiable):** Given an oracle point prompt, promptable models recover >70% of the COD performance gap versus specialized COD models — most camouflage failure is attentional (not finding the object), not perceptual (not being able to delineate it).
- **Why Important:** If failure is attentional, COD research should pivot from feature engineering to search strategies and prompt generation — a field-level redirection.
- **Why Possibly Novel:** COD papers benchmark end-to-end; the oracle-prompt decomposition into find-vs-delineate components is not established.
- **Minimal Experiment:** On COD10K-class benchmarks, evaluate SAM-class models with {no prompt/auto, oracle point, oracle box}; decompose the gap to specialist models by prompt level.
- **Main Risk:** Prompted and unprompted models differ architecturally; include prompted versions of specialist models where possible.

### IDEA-A-0155
- **One-sentence idea:** Test whether training on soft (annotator-distribution) boundary labels for ambiguous regions produces better *downstream* decisions than hard labels, beyond just better calibration.
- **Problem:** Soft labels are known to improve calibration, but whether they improve the decisions downstream systems make with masks (grasp planning, measurement, editing) is untested — calibration could be cosmetic.
- **Core Hypothesis (falsifiable):** On tasks with ambiguity-heavy boundaries, soft-label-trained models improve downstream decision metrics (e.g., robotic grasp success near boundaries, measurement error bars covering truth) by >15% relative, even when hard-label IoU is identical — the benefit is invisible to IoU.
- **Why Important:** Justifies (or debunks) the extra cost of multi-annotator collection with an application-grade endpoint rather than a proxy metric.
- **Why Possibly Novel:** Soft-label benefits are shown on proxy metrics; the downstream-decision evaluation design for segmentation ambiguity is new.
- **Minimal Experiment:** Train hard vs soft label models on multi-annotator data; run a simulated grasp/measurement downstream battery where boundary uncertainty matters; compare decision quality.
- **Main Risk:** Simulated downstream tasks may not capture real stakes; keep the battery diverse and pre-registered.

### IDEA-A-0156
- **One-sentence idea:** Define safety-weighted evaluation for transparent obstacles in driving/robot navigation, where missing a glass door is weighted by collision consequence, and test whether current model rankings survive.
- **Problem:** Uniform IoU treats a missed glass wall like a missed poster; safety-relevant evaluation for transparency is absent, and rankings under consequence-weighted metrics may differ sharply.
- **Core Hypothesis (falsifiable):** Under a collision-risk-weighted metric (miss cost scaled by object traversability consequence), model rankings on transparency benchmarks change for ≥40% of model pairs, and the models that win are those with high recall/low precision profiles currently penalized by IoU.
- **Why Important:** Deployment decisions for navigation systems should use consequence-aligned metrics; showing ranking inversion makes the case concretely.
- **Why Possibly Novel:** Safety-weighted metrics exist conceptually in AV literature; instantiation and ranking-impact analysis for transparent obstacles is new.
- **Minimal Experiment:** Define the weighted metric with traversability annotations on indoor/outdoor glass benchmarks; re-rank public models; analyze which operating points win.
- **Main Risk:** Consequence weights are debatable; publish sensitivity analysis across weight choices.

### IDEA-A-0157
- **One-sentence idea:** Measure the human-vision floor for near-invisible glass (clean, anti-reflective, well-lit) and test whether current models are above or below human performance on the hardest transparency regime.
- **Problem:** Some glass is nearly invisible even to humans (people walk into doors); without a human floor, we cannot say whether model failures reflect missing information or missing competence.
- **Core Hypothesis (falsifiable):** On a hardest-regime glass set, human detection (brief-presentation) exceeds the best models by >30 points — humans exploit weak cues (frames, context, subtle reflections) that models don't, proving competence (not information) is the bottleneck.
- **Why Important:** Locates the transparency frontier precisely: if humans succeed where models fail, the information exists and modeling should continue; if both fail, sensing (polarization) is the answer (link to IDEA-A-0150).
- **Why Possibly Novel:** Human baselines are almost never collected for transparency benchmarks; the hardest-regime comparison is absent.
- **Minimal Experiment:** Curate hard-glass images; run controlled human detection/localization experiments; compare with model outputs under matched viewing conditions.
- **Main Risk:** Matching human and model "viewing conditions" (time, resolution) fairly requires careful psychophysics design.

### IDEA-A-0158
- **One-sentence idea:** Characterize water-surface segmentation as a distinct problem regime — dynamic, specular, transparent, and boundary-free at once — and test which existing paradigm (matting, segmentation, layer decomposition) fits it best.
- **Problem:** Water surfaces (floods, puddles, rivers) combine every hard property at once, and flood-mapping applications inherit models built for none of them; the right output representation is unresolved.
- **Core Hypothesis (falsifiable):** On flood/puddle imagery, layer-decomposition-based approaches (surface reflection + transmitted bed) outperform binary segmentation by >10 IoU specifically on shallow/clear water where binary training is self-contradictory, while performing equally on turbid water — representation choice matters exactly where transparency is high.
- **Why Important:** Flood extent mapping drives disaster response; getting the representation right for shallow-water edges affects real decisions.
- **Why Possibly Novel:** Water segmentation exists in remote sensing; the representation-comparison framing driven by transparency level is new.
- **Minimal Experiment:** Assemble water imagery stratified by turbidity/clarity; train the three paradigms on matched data; compare stratified performance.
- **Main Risk:** Clarity stratification needs ground truth (turbidity estimates); use scene metadata and expert rating.

### IDEA-A-0159
- **One-sentence idea:** Test whether transparent-object segmentation accuracy actually predicts robotic grasp success — validating (or breaking) the assumed utility chain of transparency research.
- **Problem:** Transparency segmentation papers motivate via robotic manipulation, but grasping may depend on cues (rim localization, depth completion) only weakly coupled to mask IoU; the correlation is unmeasured.
- **Core Hypothesis (falsifiable):** Across models spanning 30 IoU points, grasp success on transparent objects correlates weakly with mask IoU (ρ < 0.4) but strongly with rim/contact-edge localization error — the field's metric is misaligned with its stated application.
- **Why Important:** If rim accuracy is what matters, benchmarks and losses should target it — a concrete, testable realignment of an application-justified field.
- **Why Possibly Novel:** Downstream validity checks are rare; none exist linking transparency segmentation metrics to physical manipulation outcomes.
- **Minimal Experiment:** Run grasp trials (real or high-fidelity sim) using masks from models of varying quality; regress success on IoU vs rim-error metrics.
- **Main Risk:** Sim-based grasping may not reflect real contact physics on glass; include a small real-robot validation.

### IDEA-A-0160
- **One-sentence idea:** Port the transparency toolkit to medical imaging by testing whether membranes, cysts, and fluid interfaces behave like "transparent objects" for VFMs — same failure signatures, same fixes.
- **Problem:** Medical structures with transmissive appearance (serous membranes, vitreous, cyst walls) may fail for the same representational reasons as glass (IDEA-A-0141), but the two literatures never touch; if the failure signature matches, transparency-domain fixes transfer for free.
- **Core Hypothesis (falsifiable):** On medical structures rated high-transmissivity by clinicians, VFM segmentation errors show the transparency signature (interior assigned to background structures, boundary-driven success) with effect sizes matching natural-image glass — and boundary-weighted training (IDEA-A-0143) yields parallel gains in both domains.
- **Why Important:** Establishes a cross-domain failure taxonomy, letting medical imaging import solutions from a better-resourced problem domain.
- **Why Possibly Novel:** Nobody has tested whether "transparency" is a domain-general failure mode with a conserved signature across natural and medical imagery.
- **Minimal Experiment:** Clinician-rate transmissivity for 10 structure types; measure the error-signature statistics in both domains; test the shared intervention.
- **Main Risk:** Medical "transparency" differs physically (acoustic/radiographic vs optical); the signature comparison must be phenomenological, not mechanistic.

<!-- APPEND -->
