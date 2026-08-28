# Stage 1 — Cluster A: Massive Original Research Idea Catalog

**Scope:** Vision Foundation Models; SAM / SAM2 / SAM3 / MedSAM / HQ-SAM / MobileSAM failure modes; Parameter-Efficient Fine-Tuning (PEFT) of vision/multimodal models; Image Segmentation; Object Detection; prompt sensitivity; catastrophic forgetting; boundary quality; small objects; uncertainty; calibration; representation mismatch; evaluation weakness.

**Provenance note:** All ideas below are *hypothesized* research directions generated at Stage 1 (volume phase). No experimental results are claimed. Novelty is *hypothesized*, not verified against a literature search; each idea must be checked against prior work before execution. No papers are cited or invented.

**Format per idea:** ID, one-sentence idea, problem, core hypothesis (falsifiable), why important, why possibly novel (hypothesized), minimal experiment, main risk, research cluster tag.

**Sub-cluster map:**
- `sam-prompt-sensitivity` (A-0001–A-0015)
- `sam2-video-memory` (A-0016–A-0030)
- `sam3-concept-prompting` (A-0031–A-0045)
- `medsam-domain-shift` (A-0046–A-0060)
- `boundary-quality` (A-0061–A-0075)
- `mobile-distillation` (A-0076–A-0090)
- `peft-mechanics` (A-0091–A-0105)
- `peft-forgetting` (A-0106–A-0120)
- `calibration-uncertainty` (A-0121–A-0135)
- `small-thin-objects` (A-0136–A-0150)
- `evaluation-weakness` (A-0151–A-0165)
- `representation-mismatch` (A-0166–A-0180)
- `detection-failures` (A-0181–A-0195)
- `scaling-emergence` (A-0196–A-0210)
- `interactive-loop` (A-0211–A-0225)
- `ambiguity-multihypothesis` (A-0226–A-0240)
- `robustness-shift` (A-0241–A-0255)
- `open-vocab-grounding` (A-0256–A-0270)
- `data-centric-bias` (A-0271–A-0285)
- `continual-tta` (A-0286–A-0300)
- `architecture-internals` (A-0301–A-0315)
- `3d-volumetric-geometry` (A-0316–A-0330)
- `compositional-counting` (A-0331–A-0345)
- `failure-prediction-deployment` (A-0346–A-0360)
- `bonus-cross-cutting` (A-0361–A-0372)

---

## Sub-cluster 1: SAM prompt sensitivity & prompt geometry (`sam-prompt-sensitivity`)

### A-0001
- **Idea:** Map the "prompt basin" geometry of SAM: for each object, the connected region of click locations that yield the correct mask, and test whether basin area predicts annotation cost.
- **Problem:** SAM's output changes discontinuously with click position, but the spatial structure of this instability is uncharacterized.
- **Hypothesis:** Prompt-basin area (fraction of in-object clicks producing IoU>0.9 masks) is a stable per-object property that predicts human interactive annotation time better than object size or IoU of the best mask.
- **Why Important:** Would give a principled, model-intrinsic difficulty measure for interactive labeling budgets.
- **Why Possibly Novel (hypothesized):** Prompt sensitivity is usually reported as aggregate variance, not as a per-object spatial basin with predictive claims.
- **Minimal Experiment:** Densely sample clicks on ~500 COCO/LVIS instances, compute basin maps, correlate basin area with logged human click counts from an annotation study.
- **Main Risk:** Basin area may be confounded with object size and boundary complexity, requiring careful controls.
- **Cluster:** `sam-prompt-sensitivity`

### A-0002
- **Idea:** Test whether SAM's point-prompt instability is driven by positional-encoding aliasing rather than semantic ambiguity, by comparing instability maps to the positional encoding's spatial frequency structure.
- **Problem:** We do not know if prompt sensitivity originates in the prompt encoder's positional embedding or in genuine object ambiguity.
- **Hypothesis:** A significant fraction of mask flips under sub-8-pixel click perturbation aligns with the period of SAM's positional encoding grid, and re-encoding prompts with anti-aliased (low-pass) positional features reduces flips without hurting accuracy.
- **Why Important:** Separates fixable encoding artifacts from irreducible ambiguity, guiding where robustness work should focus.
- **Why Possibly Novel (hypothesized):** Aliasing analyses exist for CNN downsampling but not, to my knowledge, for prompt-encoder positional embeddings in promptable segmentation.
- **Minimal Experiment:** Sweep clicks on a sub-pixel grid over 200 objects, Fourier-analyze the flip map, then retrain only the prompt encoder with smoothed positional features and re-measure.
- **Main Risk:** Flip maps may be dominated by decoder attention effects, making the positional-encoding signal hard to isolate.
- **Cluster:** `sam-prompt-sensitivity`

### A-0003
- **Idea:** Formalize and measure "prompt-order sensitivity" in multi-point prompting: whether the sequence in which identical clicks are given changes SAM's final mask, and why.
- **Problem:** Interactive pipelines assume click sets are order-invariant, but SAM's iterative mask-conditioning may break this.
- **Hypothesis:** For a fixed set of k≥3 clicks, permuting click order changes final IoU by >5 points on a non-trivial fraction of objects, and the effect is mediated by the low-resolution mask prior passed between iterations.
- **Why Important:** Order sensitivity silently corrupts benchmark comparisons of interactive methods that standardize click sets but not orders.
- **Why Possibly Novel (hypothesized):** Order-invariance of promptable segmenters appears untested; existing protocols fix a single simulated order.
- **Minimal Experiment:** For 1,000 objects, sample 10 permutations of 4 fixed clicks, measure IoU spread, then ablate the inter-step mask prior to test mediation.
- **Main Risk:** Effect may be small on natural images and only matter in adversarially chosen click sets.
- **Cluster:** `sam-prompt-sensitivity`

### A-0004
- **Idea:** Investigate whether box prompts and point prompts activate distinct internal "modes" in SAM's decoder, explaining why box+point combinations sometimes underperform boxes alone.
- **Problem:** Combining prompt types is assumed to add information, yet practitioners report degradation, with no mechanistic account.
- **Hypothesis:** Box and point prompts drive decoder cross-attention into two separable activation regimes (measurable by linear probes on decoder tokens), and combined prompts land in a low-density interpolation region where accuracy drops.
- **Why Important:** Determines whether prompt fusion needs regime-aware routing rather than naive concatenation.
- **Why Possibly Novel (hypothesized):** Mechanistic mode analysis of prompt-type interactions in SAM's decoder seems unexplored.
- **Minimal Experiment:** Collect decoder token activations under box-only, point-only, and mixed prompting on 5k objects; train probes to classify regime; correlate interpolation-region membership with per-object IoU drop.
- **Main Risk:** Activation regimes may not be linearly separable, weakening the probing methodology.
- **Cluster:** `sam-prompt-sensitivity`

### A-0005
- **Idea:** Quantify "negative-click pathology": the hypothesis that SAM over-erodes masks after background clicks near thin structures, and trace it to the resolution of the mask prior.
- **Problem:** Negative clicks intended to remove small leaks often delete large correct regions, frustrating interactive refinement.
- **Hypothesis:** The magnitude of over-erosion after a negative click scales with the local thinness of the structure relative to the 256×256 mask-prior resolution, and increasing prior resolution monotonically reduces it.
- **Why Important:** Identifies a concrete architectural bottleneck for interactive correction of thin structures (vessels, wires, limbs).
- **Why Possibly Novel (hypothesized):** Negative-click failure has anecdotal status but no quantitative erosion law tied to prior resolution.
- **Minimal Experiment:** Build a thin-structure benchmark (DRIVE vessels, wire datasets), apply scripted negative clicks, measure erosion vs. local width, retrain decoder head at 2× prior resolution.
- **Main Risk:** Retraining at higher prior resolution may confound capacity with resolution.
- **Cluster:** `sam-prompt-sensitivity`

### A-0006
- **Idea:** Test whether SAM's prompt sensitivity is predictable from the image encoder alone, enabling "sensitivity forecasting" before any prompt is given.
- **Problem:** Systems cannot currently warn users which objects will be prompt-fragile without expensive prompt sweeps.
- **Hypothesis:** A lightweight head on frozen encoder features predicts per-pixel prompt instability (variance of masks under click jitter) with rank correlation >0.6, implying instability is encoded pre-prompt.
- **Why Important:** Enables active prompting UIs and automatic escalation to humans on fragile regions.
- **Why Possibly Novel (hypothesized):** Instability prediction is studied for classifier confidence, not for prompt-conditioned mask variance from unprompted features.
- **Minimal Experiment:** Generate instability maps via click jitter on 2k images, train a linear/MLP probe on encoder features to regress them, evaluate on held-out datasets.
- **Main Risk:** Instability may depend irreducibly on the prompt itself, capping achievable correlation.
- **Cluster:** `sam-prompt-sensitivity`

### A-0007
- **Idea:** Characterize a "semantic granularity prior" in SAM: whether ambiguous clicks default to part, object, or group level in a way that is biased by texture statistics rather than semantics.
- **Problem:** SAM's multimask outputs resolve granularity ambiguity, but the ranking among them may reflect low-level texture cues, not object structure.
- **Hypothesis:** SAM's top-ranked mask granularity can be flipped from object to part by texture manipulations (contrast, high-frequency noise) that leave human granularity judgments unchanged.
- **Why Important:** Reveals whether the model's ambiguity resolution is semantically grounded or exploitable/spurious.
- **Why Possibly Novel (hypothesized):** Granularity-choice bias under controlled texture interventions appears unstudied for promptable models.
- **Minimal Experiment:** Construct texture-perturbed versions of 500 part-whole images (e.g., PartImageNet), measure top-mask granularity flips vs. human judgments from a small user study.
- **Main Risk:** Texture manipulations may also shift human perception, requiring careful psychophysics controls.
- **Cluster:** `sam-prompt-sensitivity`

### A-0008
- **Idea:** Study whether prompt jitter augmentation at fine-tuning time provably trades off peak accuracy for stability, and find the Pareto frontier.
- **Problem:** Practitioners fine-tune SAM with jittered prompts ad hoc; the stability-accuracy trade-off has no measured frontier.
- **Hypothesis:** There exists a jitter scale beyond which stability gains saturate while clean-prompt IoU keeps degrading, with the knee at roughly the object's median boundary distance.
- **Why Important:** Gives a principled recipe for robust prompt-conditioned fine-tuning instead of guessed jitter magnitudes.
- **Why Possibly Novel (hypothesized):** Jitter is used as augmentation but the frontier and its dependence on object statistics are unquantified.
- **Minimal Experiment:** Fine-tune SAM decoder with 6 jitter scales on the same data, plot stability (flip rate) vs. clean IoU, verify the knee against per-dataset boundary-distance statistics.
- **Main Risk:** The frontier may be dataset-specific, limiting a general law.
- **Cluster:** `sam-prompt-sensitivity`

### A-0009
- **Idea:** Test the hypothesis that SAM's text-free prompt space is star-shaped: any correct mask reachable by some click is reachable from the object centroid via iterative refinement.
- **Problem:** We lack a topological description of which masks are reachable from which prompts, so interactive strategies are heuristic.
- **Hypothesis:** For >90% of objects, greedy iterative clicking starting at the centroid reaches within 2 IoU points of the best mask found by exhaustive click search, i.e., reachability is centroid-star-shaped.
- **Why Important:** Would justify simple centroid-first strategies and bound the value of clever click placement.
- **Why Possibly Novel (hypothesized):** Reachability topology of promptable segmentation appears unformalized.
- **Minimal Experiment:** On 1k objects, run exhaustive first-click search vs. centroid-start greedy refinement (3 rounds), compare best-achievable IoU distributions.
- **Main Risk:** "Greedy refinement" definition may drive the result more than model properties.
- **Cluster:** `sam-prompt-sensitivity`

### A-0010
- **Idea:** Measure cross-model prompt transferability: whether the click that best segments an object in one SAM variant is also near-optimal in another, isolating whether prompt sensitivity is model-idiosyncratic or image-intrinsic.
- **Problem:** If optimal prompts are model-specific, human prompt skill and simulated-click benchmarks do not transfer across model versions.
- **Hypothesis:** Optimal-click transfer between SAM, HQ-SAM, and MobileSAM retains <60% of the achievable IoU gain over centroid clicks, indicating substantial model-idiosyncratic sensitivity.
- **Why Important:** Determines whether prompt-optimization research targets the image or the model, and whether click benchmarks are version-portable.
- **Why Possibly Novel (hypothesized):** Prompt-optimum transferability across promptable-model families seems unmeasured.
- **Minimal Experiment:** Grid-search best clicks per object per model on 500 objects; evaluate each model with every other model's best clicks; report transfer matrices.
- **Main Risk:** Distilled variants share the teacher's idiosyncrasies, inflating apparent transfer.
- **Cluster:** `sam-prompt-sensitivity`

### A-0011
- **Idea:** Investigate whether SAM prompt embeddings can be calibrated per-user: learning a tiny transformation of click embeddings that compensates for individual users' systematic click-placement biases.
- **Problem:** Different users click different canonical locations (center vs. distinctive part), and SAM's fixed prompt encoding treats them identically.
- **Hypothesis:** A per-user 2-layer MLP on prompt embeddings, trained from <50 correction interactions, reduces that user's clicks-to-target by ≥20% relative to the shared encoder.
- **Why Important:** Cheap personalization could substantially reduce annotation cost in production labeling.
- **Why Possibly Novel (hypothesized):** Personalization in interactive segmentation has targeted the image model, not the prompt-encoding channel.
- **Minimal Experiment:** Collect click logs from 10 annotators on the same 200 objects, fit per-user prompt MLPs, evaluate held-out clicks-to-90%-IoU.
- **Main Risk:** User bias may be too inconsistent within-user for 50 interactions to suffice.
- **Cluster:** `sam-prompt-sensitivity`

### A-0012
- **Idea:** Determine whether adversarially fragile prompts (clicks whose tiny perturbation flips the mask) coincide with human-perceived ambiguous regions or form a disjoint, model-specific set.
- **Problem:** It is unknown whether prompt fragility is an alignment failure (model disagrees with humans about ambiguity) or mirrors true ambiguity.
- **Hypothesis:** At least 40% of high-fragility click locations lie in regions humans rate as unambiguous, demonstrating model-specific fragility not explained by task ambiguity.
- **Why Important:** Quantifies the human-model ambiguity gap, which defines the ceiling for "ambiguity-aware" excuses of instability.
- **Why Possibly Novel (hypothesized):** Direct comparison of fragility maps against human ambiguity ratings appears missing.
- **Minimal Experiment:** Compute fragility maps for 300 images; collect human ambiguity annotations on a grid; measure overlap statistics with permutation tests.
- **Main Risk:** Human ambiguity ratings are noisy and granularity-dependent.
- **Cluster:** `sam-prompt-sensitivity`

### A-0013
- **Idea:** Test whether "prompt dropout" at inference (ensembling masks over random subsets of provided clicks) yields calibrated stability estimates that predict when interactive refinement will fail to converge.
- **Problem:** Interactive sessions sometimes oscillate without converging, and there is no early-warning signal.
- **Hypothesis:** Disagreement among prompt-subset ensembles at round t predicts non-convergence within the next 5 rounds with AUC>0.8, outperforming mask-confidence scores.
- **Why Important:** Enables systems to escalate to a different tool or human policy before wasting user effort.
- **Why Possibly Novel (hypothesized):** Dropout-style ensembling over the prompt set (not model weights) as a convergence predictor appears new.
- **Minimal Experiment:** Simulate 5k interactive sessions with scripted correction policies, log subset-ensemble disagreement per round, fit and evaluate the convergence predictor.
- **Main Risk:** Simulated correction policies may not reflect human oscillation patterns.
- **Cluster:** `sam-prompt-sensitivity`

### A-0014
- **Idea:** Characterize how image-space transformations (rotation, scale) commute with prompt-space transformations in SAM, defining an equivariance defect measure for promptable models.
- **Problem:** Rotating an image and its click should rotate the mask, but SAM's equivariance defect under this joint action is unmeasured.
- **Hypothesis:** SAM's prompt-conditional equivariance defect grows superlinearly with rotation angle and is dominated by the image encoder (not the prompt path), as isolated by swapping components across rotated/unrotated inputs.
- **Why Important:** Equivariance defects bound reliability in aerial, medical, and microscopy imaging where orientation is arbitrary.
- **Why Possibly Novel (hypothesized):** Equivariance is studied for classifiers/CNN backbones; joint prompt+image equivariance for promptable segmenters looks unformalized.
- **Minimal Experiment:** Evaluate mask consistency under 16 rotation angles with correspondingly rotated prompts on 1k objects; ablate by feeding rotated features with unrotated prompts and vice versa.
- **Main Risk:** Interpolation artifacts during rotation may inflate the measured defect.
- **Cluster:** `sam-prompt-sensitivity`

### A-0015
- **Idea:** Ask whether optimal prompting is learnable as a policy: train a small "prompter" network that places clicks for SAM, and test whether its learned policy generalizes across datasets better than heuristic policies.
- **Problem:** Simulated-click heuristics (center-of-error-region) may be far from optimal, and the structure of good prompting policies is unknown.
- **Hypothesis:** A learned prompt-placement policy trained on one dataset outperforms center-of-error heuristics by ≥1 click on average on unseen datasets, indicating dataset-general prompting structure exists.
- **Why Important:** Would replace hand-coded simulators in benchmarks and reduce clicks in automated pipelines.
- **Why Possibly Novel (hypothesized):** RL/imitation for click placement exists in fragments; a cross-dataset generalization claim about prompting policies is the untested core.
- **Minimal Experiment:** Train a policy with SAM frozen via REINFORCE/DAgger on COCO; evaluate clicks-to-90%-IoU on ADE20K, DAVIS frames, and medical slices vs. heuristics.
- **Main Risk:** Policy may overfit SAM's idiosyncrasies and fail under model updates.
- **Cluster:** `sam-prompt-sensitivity`

---

## Sub-cluster 2: SAM2 video memory & tracking failures (`sam2-video-memory`)

### A-0016
- **Idea:** Characterize the forgetting curve of SAM2's memory bank: how re-identification accuracy decays with occlusion duration, and whether the decay is exponential (interference) or step-like (slot eviction).
- **Problem:** SAM2 loses objects after long occlusions, but the functional form and mechanism of memory decay are uncharacterized.
- **Hypothesis:** Re-ID accuracy after occlusion follows a step function aligned with memory-slot eviction events rather than smooth decay, implying failures are architectural, not representational.
- **Why Important:** Distinguishes "needs better features" from "needs better memory scheduling," which require different fixes.
- **Minimal Experiment:** Construct controlled occlusion videos with parametric occlusion lengths (10–600 frames), measure re-ID success vs. length, and log memory-bank contents to align failures with evictions.
- **Why Possibly Novel (hypothesized):** SAM2 memory has been benchmarked end-to-end but not decomposed into decay-law analysis tied to slot dynamics.
- **Main Risk:** Synthetic occlusions may not capture appearance change during real occlusions.
- **Cluster:** `sam2-video-memory`

### A-0017
- **Idea:** Test whether SAM2's memory attention exhibits "identity capture": after a tracking error, the memory bank locks onto the distractor and actively suppresses recovery even when the true object reappears unambiguously.
- **Problem:** Tracking errors in SAM2 appear self-reinforcing, but whether memory causally prevents recovery is unproven.
- **Hypothesis:** Surgically deleting post-error memory entries at reappearance time restores correct tracking in >70% of failure cases, demonstrating that stale memories causally block recovery.
- **Why Important:** Motivates memory-editing interventions as a lightweight alternative to retraining for robust tracking.
- **Why Possibly Novel (hypothesized):** Causal memory-ablation studies (deleting specific entries mid-video) on SAM2 appear unexplored.
- **Minimal Experiment:** Collect 200 organic SAM2 failures on LVOS/long videos, replay each with targeted memory deletion at ground-truth reappearance frames, measure recovery rate.
- **Main Risk:** Requires ground-truth reappearance annotations; deletion timing may be a strong oracle.
- **Cluster:** `sam2-video-memory`

### A-0018
- **Idea:** Study whether SAM2's frame-rate sensitivity constitutes a hidden hyperparameter: the same physical video at different fps yields systematically different masklets, violating temporal-sampling invariance.
- **Problem:** Deployments run at varied fps, but SAM2's training fixed temporal statistics; invariance is assumed, not tested.
- **Hypothesis:** Downsampling videos from 30 to 6 fps changes J&F by >8 points in a direction predictable from object speed, and simple memory-stride adaptation recovers most of the loss.
- **Why Important:** fps mismatch is ubiquitous in robotics/edge deployments; quantifying it prevents silent degradation.
- **Why Possibly Novel (hypothesized):** Temporal-sampling invariance of memory-based video segmenters seems unbenchmarked.
- **Minimal Experiment:** Re-time DAVIS/MOSE videos at 5 frame rates, evaluate SAM2 J&F vs. fps stratified by object velocity, test stride-adaptive memory writing.
- **Main Risk:** Re-timing artifacts (frame duplication/blur) may confound pure sampling effects.
- **Cluster:** `sam2-video-memory`

### A-0019
- **Idea:** Quantify the interference cost of multi-object tracking in SAM2: whether tracking N objects with separate memory streams degrades each object's accuracy relative to solo tracking, despite nominally independent inference.
- **Problem:** SAM2 tracks objects independently, but shared encoder computation and prompt handling may still couple errors.
- **Hypothesis:** Per-object accuracy is statistically indistinguishable between solo and joint tracking, localizing all multi-object failures to prompt assignment rather than interference — or the null is falsified with measurable coupling.
- **Why Important:** Clarifies whether multi-object failures need architectural interaction modeling or better initialization only.
- **Why Possibly Novel (hypothesized):** The solo-vs-joint controlled comparison for SAM2 appears unreported.
- **Minimal Experiment:** On MOSE, run each annotated object solo and jointly with all others; paired per-object J&F comparison with significance testing.
- **Main Risk:** Result may be a boring null; value depends on framing either outcome as informative.
- **Cluster:** `sam2-video-memory`

### A-0020
- **Idea:** Investigate whether SAM2's memory representations drift toward "recency-weighted appearance averages" that fail under cyclic appearance change (e.g., rotating objects), and whether phase-aware memory sampling fixes it.
- **Problem:** Objects with periodic appearance (rotation, gait) revisit past appearances, but recency-biased memory may have evicted them.
- **Hypothesis:** Tracking error on periodic-appearance objects concentrates at phase points furthest from recently stored appearances, and uniform-phase memory sampling reduces those errors by ≥30%.
- **Why Important:** Periodic appearance is common (vehicles turning, animals walking); phase-aware memory is a cheap fix if the mechanism holds.
- **Why Possibly Novel (hypothesized):** Appearance-phase analysis of memory eviction appears novel for video foundation models.
- **Minimal Experiment:** Build/collect turntable-style and gait videos with phase labels, correlate per-frame error with phase distance to memory contents, then swap eviction policy.
- **Main Risk:** Phase labeling of in-the-wild videos is hard; may need synthetic rendering.
- **Cluster:** `sam2-video-memory`

### A-0021
- **Idea:** Test whether SAM2 can be prompted "in the past": propagating a late-video correction backwards through the memory mechanism, and characterizing the asymmetry between forward and backward propagation quality.
- **Problem:** Corrections arrive mid-session, but SAM2's memory is causally forward; the cost of this asymmetry is unquantified.
- **Hypothesis:** Backward propagation (reversed replay) recovers ≥90% of forward-propagation quality on reversible motion but <60% on articulated motion, quantifying a directional bias in learned memory.
- **Why Important:** Efficient bidirectional correction determines annotation-tool design for video datasets.
- **Why Possibly Novel (hypothesized):** Directional asymmetry of memory-based propagation is folklore but unmeasured.
- **Minimal Experiment:** On DAVIS, prompt at last frame and track on reversed video vs. prompt at first frame on forward video; stratify the gap by motion type.
- **Main Risk:** Reversed videos violate physics (e.g., gravity), confounding the asymmetry source.
- **Cluster:** `sam2-video-memory`

### A-0022
- **Idea:** Determine whether SAM2's occlusion head produces calibrated occlusion probabilities, and whether miscalibration is the direct cause of premature track termination.
- **Problem:** SAM2 predicts object presence per frame, but if this score is miscalibrated, downstream logic kills tracks wrongly.
- **Hypothesis:** SAM2's occlusion scores are overconfident near partial occlusion (ECE>0.15 in the 30–70% occluded regime), and isotonic recalibration alone reduces wrong terminations by ≥25% without touching mask quality.
- **Why Important:** A pure post-hoc fix to tracking persistence would be free accuracy for all SAM2 deployments.
- **Why Possibly Novel (hypothesized):** Calibration analysis of presence/occlusion heads (vs. mask IoU heads) appears missing.
- **Minimal Experiment:** Extract occlusion scores on MOSE with ground-truth visibility, compute reliability diagrams, apply isotonic regression, re-run tracking with recalibrated thresholds.
- **Main Risk:** Ground-truth partial-occlusion percentages are scarce; may need synthetic composites.
- **Cluster:** `sam2-video-memory`

### A-0023
- **Idea:** Study "memory poisoning" robustness: whether a few adversarially or naturally corrupted frames written into SAM2's memory disproportionately corrupt future predictions, and derive a write-gate criterion.
- **Problem:** Memory-augmented models may amplify single-frame errors into persistent failures; the amplification factor is unknown.
- **Hypothesis:** A single low-quality memory write during motion blur degrades subsequent-frame IoU superlinearly relative to skipping the write, and a quality-gated write policy (predicted-IoU threshold) recovers most losses.
- **Why Important:** Establishes memory hygiene as a first-class reliability concern for streaming vision models.
- **Why Possibly Novel (hypothesized):** Poisoning analyses target training data; inference-time memory-write poisoning in video segmentation looks new.
- **Minimal Experiment:** Inject controlled blur/compression into single frames, compare downstream error with forced vs. gated writes across corruption severities.
- **Main Risk:** Gating may starve memory during genuinely hard sequences, hurting long-term recall.
- **Cluster:** `sam2-video-memory`

### A-0024
- **Idea:** Ask whether SAM2's memory bank encodes identity or merely appearance, using twin-object videos (identical instances) to test if the model can maintain identity through crossovers without appearance cues.
- **Problem:** Identity maintenance under appearance ties is the hard core of tracking; SAM2's capability here is unquantified.
- **Hypothesis:** SAM2's crossover identity accuracy on identical twins is near chance (≤60%), showing its memory is appearance-based with no motion-continuity integration.
- **Why Important:** Defines the boundary between "video segmentation" and "tracking" capabilities of current video foundation models.
- **Why Possibly Novel (hypothesized):** Twin/crossover stress tests exist for MOT trackers but not for promptable video segmenters.
- **Minimal Experiment:** Render synthetic twin-object crossing videos with controlled kinematics; measure post-crossing identity retention vs. crossing angle and speed.
- **Main Risk:** Synthetic-to-real gap; results may not predict real-world identity errors.
- **Cluster:** `sam2-video-memory`

### A-0025
- **Idea:** Measure whether long-video error accumulation in SAM2 is dominated by rare catastrophic re-anchoring events rather than gradual drift, using changepoint analysis on per-frame IoU trajectories.
- **Problem:** "Drift" is invoked as the failure mode of long-video segmentation, but the temporal error structure is unanalyzed.
- **Hypothesis:** >70% of total IoU loss on 5-minute videos occurs within <5% of frames (catastrophic events), implying event prevention beats drift correction as a research target.
- **Why Important:** Redirects long-video robustness work toward event detection/rollback instead of continuous smoothing.
- **Why Possibly Novel (hypothesized):** Changepoint decomposition of video-segmentation error budgets appears unreported.
- **Minimal Experiment:** Run SAM2 on LVOS/long videos, compute per-frame IoU, apply changepoint detection, report error-mass concentration statistics and event triggers.
- **Main Risk:** Ground-truth density on long videos is sparse, complicating per-frame IoU estimation.
- **Cluster:** `sam2-video-memory`

### A-0026
- **Idea:** Test a "memory rehearsal" inference scheme: periodically re-encoding the first-frame prompt features into memory to prevent representation drift, framed as testing whether anchor rehearsal beats recency in memory-based video models.
- **Problem:** SAM2's memory is recency-dominated; whether persistent anchors would prevent drift is untested as a controlled question.
- **Hypothesis:** Pinning the initial conditioning frame permanently in memory improves long-video J&F by ≥5 points on videos with appearance drift while never hurting short videos by more than 1 point.
- **Why Important:** A zero-training modification with a clear mechanism test could immediately improve deployed systems.
- **Why Possibly Novel (hypothesized):** Anchor-pinning ablations on SAM2's memory bank appear unpublished; the design space of write/evict policies is largely unexplored.
- **Minimal Experiment:** Modify memory eviction to always retain frame-0 entries; A/B on LVOS vs. DAVIS; stratify by video length and drift magnitude.
- **Main Risk:** Stale anchors may harm objects with legitimate large appearance change.
- **Cluster:** `sam2-video-memory`

### A-0027
- **Idea:** Investigate whether SAM2 masklet quality can be predicted online from memory-attention entropy, giving a streaming self-diagnosis signal without ground truth.
- **Problem:** Streaming systems need to know when tracking is failing now, but SAM2 exposes no validated online quality signal beyond its IoU head.
- **Hypothesis:** Entropy of memory cross-attention distributions predicts per-frame IoU drops 5–10 frames before they occur, with earlier warning than the predicted-IoU head.
- **Why Important:** Early failure warning enables preemptive re-prompting in autonomous pipelines.
- **Why Possibly Novel (hypothesized):** Attention-entropy-based lead-time failure prediction in video segmentation appears untested.
- **Minimal Experiment:** Log attention entropy and predicted IoU across MOSE runs, fit lagged predictors of true IoU collapse, compare lead times.
- **Main Risk:** Entropy may correlate with scene clutter generally, yielding many false alarms.
- **Cluster:** `sam2-video-memory`

### A-0028
- **Idea:** Quantify how SAM2 handles topology changes (object splitting/merging, e.g., pouring liquids, dividing cells) and whether failures stem from the single-masklet assumption rather than perception.
- **Problem:** Real objects split and merge, but masklet-based tracking presumes persistent unitary objects.
- **Hypothesis:** At split events, SAM2 follows the fragment with higher feature similarity to memory and irreversibly drops the other, in >80% of cases, regardless of fragment size — a deterministic architectural bias.
- **Why Important:** Cell biology, fluids, and materials imaging all need split/merge handling; knowing the bias enables principled workarounds.
- **Why Possibly Novel (hypothesized):** Topology-change stress testing of promptable video segmentation seems absent.
- **Minimal Experiment:** Curate cell-division and object-splitting clips, annotate both fragments, measure which fragment SAM2 follows vs. feature-similarity and size predictors.
- **Main Risk:** Defining "correct" behavior at splits is task-dependent, complicating evaluation.
- **Cluster:** `sam2-video-memory`

### A-0029
- **Idea:** Test whether streaming compute budgets change SAM2's error profile qualitatively: under frame dropping (real-time constraint), do errors shift from boundary noise to identity loss, implying different mitigation than offline settings?
- **Problem:** Benchmarks run offline at full fps, but deployment drops frames under load; the error-type shift is uncharacterized.
- **Hypothesis:** Under 50% random frame drops, boundary-quality metrics degrade <10% while identity/re-ID errors more than double, showing memory (not perception) is the real-time bottleneck.
- **Why Important:** Guides engineering priorities for real-time SAM2 systems (invest in memory robustness, not sharper decoders).
- **Why Possibly Novel (hypothesized):** Error-type decomposition under compute-induced frame dropping appears unstudied.
- **Minimal Experiment:** Simulate frame-drop patterns (random, bursty) on DAVIS/MOSE, decompose J&F changes into boundary vs. identity components.
- **Main Risk:** Metric decomposition into "identity vs boundary" requires careful, defensible definitions.
- **Cluster:** `sam2-video-memory`

### A-0030
- **Idea:** Ask whether SAM2's video pretraining damaged its still-image ability relative to SAM1 in specific regimes (fine boundaries, dense scenes), constituting measurable negative transfer from temporal objectives.
- **Problem:** SAM2 is assumed to supersede SAM1 on images, but temporal training may trade away still-image capabilities in unmeasured corners.
- **Hypothesis:** SAM2 underperforms SAM1 on high-frequency-boundary objects and dense small-object scenes by a statistically significant margin, and the gap correlates with memory-module-induced feature smoothing.
- **Why Important:** Users choose one checkpoint for both uses; regime-specific regressions should be documented, not discovered in production.
- **Why Possibly Novel (hypothesized):** Systematic SAM1-vs-SAM2 still-image regression analysis stratified by object statistics appears missing.
- **Minimal Experiment:** Evaluate both models on identical still-image suites stratified by boundary frequency, object density, and size; test correlation of gaps with feature spectral content.
- **Main Risk:** Architecture and training-data differences confound the "temporal objective" attribution.
- **Cluster:** `sam2-video-memory`

---

## Sub-cluster 3: SAM3 concept-prompted segmentation failures (`sam3-concept-prompting`)

### A-0031
- **Idea:** Characterize the "concept granularity gap" in SAM3-style promptable concept segmentation: whether short noun-phrase prompts systematically fail on concepts defined by relations ("the cup on the left") versus attributes ("the red cup").
- **Problem:** Concept-promptable segmenters accept open-vocabulary phrases, but the failure boundary between attribute-based and relation-based concepts is unmapped.
- **Hypothesis:** Recall on relation-defined targets is at least 30 points lower than on attribute-defined targets with matched visual difficulty, indicating relational grounding is the binding failure, not vocabulary.
- **Why Important:** Defines what "concept segmentation" actually covers, preventing overclaiming and guiding data collection.
- **Why Possibly Novel (hypothesized):** Systematic attribute-vs-relation stratification for concept-promptable segmentation appears untested.
- **Minimal Experiment:** Build matched prompt pairs (attribute vs. relation for the same target) on 1k images; measure recall/precision gap with visual difficulty controlled by target size and contrast.
- **Main Risk:** Constructing genuinely matched-difficulty pairs is subtle and may leak confounds.
- **Cluster:** `sam3-concept-prompting`

### A-0032
- **Idea:** Test whether concept-promptable segmenters exhibit "exhaustivity failure": when asked for all instances of a concept, misses are not random but concentrated on instances far from the concept's visual prototype.
- **Problem:** Segment-everything-matching-a-concept requires exhaustive recall, but which instances get missed is unexplained.
- **Hypothesis:** Missed instances are systematically farther from the class mean in the model's own embedding space than found instances (effect size d>0.8), making misses predictable a priori.
- **Why Important:** Predictable misses enable targeted human verification and honest recall estimates in downstream corpora.
- **Why Possibly Novel (hypothesized):** Prototype-distance analysis of instance-level recall in concept segmentation appears new.
- **Minimal Experiment:** Run concept prompts on LVIS-style exhaustively annotated images, embed all GT instances, compare embedding distances of hits vs. misses.
- **Main Risk:** Embedding distance may proxy for size/occlusion, requiring multivariate controls.
- **Cluster:** `sam3-concept-prompting`

### A-0033
- **Idea:** Study prompt-phrasing sensitivity for concept segmentation: whether synonymous phrasings ("dog" vs. "canine" vs. "a dog") produce different instance sets, and quantify a phrasing-invariance score.
- **Problem:** Text prompts are treated as canonical, but linguistic surface form may drive output variation invisible to standard benchmarks.
- **Hypothesis:** Synonym substitution alone changes the returned instance set (symmetric difference) by >15% on average, and the variation is larger for rare concepts, falsifying phrasing invariance.
- **Why Important:** Downstream users cannot control phrasing precisely; invariance is a prerequisite for reliable concept search.
- **Why Possibly Novel (hypothesized):** Instance-set-level (not mAP-level) phrasing consistency for segmentation seems unmeasured.
- **Minimal Experiment:** Curate 100 concepts × 5 phrasings, run on a fixed image corpus, compute pairwise instance-set Jaccard and stratify by concept frequency.
- **Main Risk:** Some "synonyms" carry real semantic differences, requiring careful linguistic vetting.
- **Cluster:** `sam3-concept-prompting`

### A-0034
- **Idea:** Investigate negative-concept prompting: whether models can segment "all animals except dogs," and if failures reveal that concept prompts are implemented as similarity thresholds without set operations.
- **Problem:** Real queries involve exclusions and boolean structure, but concept heads may only support positive similarity matching.
- **Hypothesis:** Performance on exclusion queries is no better than applying the positive query and randomly removing instances, demonstrating absence of compositional negation in current concept heads.
- **Why Important:** Establishes whether set-algebraic querying requires architectural change or emerges from scale.
- **Why Possibly Novel (hypothesized):** Boolean-query stress tests for promptable segmentation appear absent.
- **Minimal Experiment:** Construct 200 exclusion queries with ground truth on densely annotated images; compare against positive-query-plus-oracle-subtraction and random-subtraction baselines.
- **Main Risk:** Prompt formatting choices could dominate results; needs multiple phrasing templates.
- **Cluster:** `sam3-concept-prompting`

### A-0035
- **Idea:** Test whether image exemplar prompts and text prompts for the same concept retrieve systematically different instance distributions, quantifying a cross-modal prompt gap within one model.
- **Problem:** Systems offer both text and exemplar prompting interchangeably, assuming they define the same concept extension.
- **Hypothesis:** Exemplar prompts bias retrieval toward the exemplar's pose/context (measurable as reduced intra-retrieved-set diversity vs. text prompts) even when both achieve similar precision.
- **Why Important:** Interchangeability assumptions corrupt dataset bootstrapping pipelines that mix prompt modalities.
- **Why Possibly Novel (hypothesized):** Within-model text-vs-exemplar extension comparison for segmentation appears unstudied.
- **Minimal Experiment:** For 50 concepts, prompt via text and via 5 random exemplars each; compare retrieved-set diversity (pose/scale/context statistics) and overlap.
- **Main Risk:** Diversity metrics on retrieved sets are themselves contestable.
- **Cluster:** `sam3-concept-prompting`

### A-0036
- **Idea:** Measure "hard-negative hallucination" in concept segmentation: the rate at which visually similar but categorically wrong objects are returned, as a function of the semantic distance of the nearest confusable category present.
- **Problem:** Precision failures may be dominated by structured confusions (wolf for dog) rather than random noise, but this structure is unquantified.
- **Hypothesis:** False-positive rate is predicted by the presence of a taxonomic sibling in the image (odds ratio >3), and no current confidence signal separates sibling confusions from correct detections.
- **Why Important:** Sibling confusions poison auto-labeled datasets in exactly the classes where labels matter most.
- **Why Possibly Novel (hypothesized):** Taxonomy-conditioned false-positive analysis for concept segmentation looks new.
- **Minimal Experiment:** Assemble images containing sibling pairs (from a taxonomy), run single-concept prompts, quantify FP odds ratios and confidence overlap distributions.
- **Main Risk:** Requires reliable taxonomies; visual similarity may not track taxonomy.
- **Cluster:** `sam3-concept-prompting`

### A-0037
- **Idea:** Ask whether concept segmenters internally decide instance count before segmenting (top-down) or segment then group (bottom-up), by probing intermediate representations for count information at different depths.
- **Problem:** The computational order of "how many" vs. "where" in exhaustive concept segmentation is unknown, yet determines failure structure in crowded scenes.
- **Hypothesis:** Count information is linearly decodable from mid-level representations before instance masks are resolved, and ablating it degrades exhaustivity specifically in crowded scenes.
- **Why Important:** Reveals the algorithmic strategy of learned exhaustive segmentation and where crowding failures originate.
- **Why Possibly Novel (hypothesized):** Order-of-computation probing for count-vs-localization in segmentation models appears unexplored.
- **Minimal Experiment:** Train linear probes for instance count at each transformer block on crowded images; causally patch count-carrying activations and observe exhaustivity changes.
- **Main Risk:** Linear decodability does not establish causal use; patching experiments are delicate.
- **Cluster:** `sam3-concept-prompting`

### A-0038
- **Idea:** Test the temporal stability of concept prompts in video: whether a concept prompt applied per-frame yields flickering instance sets, and whether the flicker is attributable to threshold effects near the decision boundary.
- **Problem:** Concept-driven video analytics needs temporally stable detections, but per-frame concept matching may oscillate.
- **Hypothesis:** >50% of instance flicker events involve match scores within a narrow band around the acceptance threshold, so score-hysteresis eliminates most flicker without new training.
- **Why Important:** Flicker breaks downstream counting/alerting; a threshold-dynamics fix would be free.
- **Why Possibly Novel (hypothesized):** Score-dynamics analysis of concept-prompted video flicker seems unreported.
- **Minimal Experiment:** Run concept prompts per-frame on videos with stable GT, log score trajectories of flickering instances, test hysteresis and temporal smoothing at the score level.
- **Main Risk:** Some flicker may come from encoder feature instability, not thresholds.
- **Cluster:** `sam3-concept-prompting`

### A-0039
- **Idea:** Characterize how concept segmentation degrades under domain shift differently for the recognition pathway vs. the mask pathway, using domain pairs where one pathway is stressed at a time.
- **Problem:** A concept segmenter can fail by not recognizing the concept or by mis-delineating it; aggregate metrics conflate the two.
- **Hypothesis:** Under style shift (photo→sketch), recognition recall collapses while conditional mask quality (given correct recognition) stays within 5 points, indicating the pathways fail independently.
- **Why Important:** Independent failure modes need independent fixes; conflated metrics misdirect research effort.
- **Why Possibly Novel (hypothesized):** Pathway-decomposed domain-shift analysis for unified concept segmenters appears new.
- **Minimal Experiment:** Evaluate on photo/sketch/clipart versions of matched scenes; report recognition recall and recognition-conditioned mask IoU separately.
- **Main Risk:** Truly matched cross-style scenes are scarce; may require rendered data.
- **Cluster:** `sam3-concept-prompting`

### A-0040
- **Idea:** Study prompt-set interference: whether asking a concept segmenter for multiple concepts simultaneously changes the results for each concept relative to querying them one at a time.
- **Problem:** Batched multi-concept querying is the efficient deployment mode, but concepts may compete for instances or attention.
- **Hypothesis:** Joint querying reduces per-concept recall for semantically close concepts sharing visual features, with interference proportional to embedding similarity of the queried concepts.
- **Why Important:** Determines safe batching policies for large-scale auto-annotation.
- **Why Possibly Novel (hypothesized):** Query-interference effects in multi-concept segmentation seem unmeasured.
- **Minimal Experiment:** Query 100 concept pairs jointly and separately on the same corpus; regress recall deltas on inter-concept embedding similarity.
- **Main Risk:** Implementation details of batching may differ across systems, limiting generality.
- **Cluster:** `sam3-concept-prompting`

### A-0041
- **Idea:** Test whether concept segmenters can abstain: measuring behavior when prompted with concepts absent from the image, and whether "absence competence" is independent of presence accuracy.
- **Problem:** Real pipelines query concepts that often aren't present, but benchmarks mostly evaluate present-concept accuracy.
- **Hypothesis:** False-positive rates on absent-concept prompts are uncorrelated (r<0.2) with present-concept accuracy across concepts, revealing absence handling as a separate, unoptimized capability.
- **Why Important:** Absence errors dominate practical harm (spurious detections at scale), yet are invisible in standard evaluation.
- **Why Possibly Novel (hypothesized):** Treating abstention on absent concepts as a distinct measurable capability for segmentation seems new.
- **Minimal Experiment:** For 200 concepts, query images with verified absence; compute per-concept FP rates; correlate with standard AP on present cases.
- **Main Risk:** Verifying true absence requires exhaustive annotation, which is expensive.
- **Cluster:** `sam3-concept-prompting`

### A-0042
- **Idea:** Investigate whether fine-grained concept boundaries ("mug" vs. "cup") in segmentation models match human category boundaries, using morphed/ambiguous objects as the probe set.
- **Problem:** Concept prompts imply crisp category boundaries; where the model draws them relative to human consensus is unknown.
- **Hypothesis:** Model category boundaries on a morph continuum are systematically shifted toward the more frequent training concept, misaligning with the human 50% point by a measurable offset.
- **Why Important:** Boundary misalignment quantifies frequency bias in open-vocabulary grounding, relevant for fairness and reliability.
- **Why Possibly Novel (hypothesized):** Psychophysics-style category-boundary measurement on segmentation prompt heads appears novel.
- **Minimal Experiment:** Generate 3D-rendered morph continua between confusable categories, query both concepts, compare model crossover point to crowdsourced human judgments.
- **Main Risk:** Rendered morphs may sit off-distribution for the model, distorting boundaries.
- **Cluster:** `sam3-concept-prompting`

### A-0043
- **Idea:** Quantify the "vocabulary tail cliff": whether concept-segmentation quality decays smoothly or cliff-drops with decreasing concept frequency in pretraining-scale text corpora, using corpus frequency as the sole predictor.
- **Problem:** Open-vocabulary claims hide where the vocabulary effectively ends.
- **Hypothesis:** There is a frequency threshold below which recall collapses discontinuously (cliff), rather than smooth log-linear decay, and the cliff location is stable across image domains.
- **Why Important:** Gives practitioners a concrete usable-vocabulary boundary and a scaling target.
- **Why Possibly Novel (hypothesized):** Cliff-vs-decay functional analysis tied to corpus frequency for segmentation appears untested.
- **Minimal Experiment:** Sample 500 concepts across 6 frequency decades, evaluate recall on a held-out annotated corpus, fit piecewise vs. smooth decay models and compare.
- **Main Risk:** Frequency estimates from public corpora may mismatch the actual pretraining data.
- **Cluster:** `sam3-concept-prompting`

### A-0044
- **Idea:** Test whether concept segmenters leak instance masks across prompt semantics: prompting "shadow" or "reflection" of an object to probe whether the model represents non-material visual entities as segmentable concepts.
- **Problem:** Shadows/reflections/highlights are visually salient but ontologically different; how concept models treat them reveals their implicit ontology.
- **Hypothesis:** Models segment reflections as object instances at high rates when prompted with the object noun (not the word "reflection"), inflating false positives in reflective scenes by a measurable factor.
- **Why Important:** Reflective/shadowed scenes are ubiquitous (retail, driving); ontology confusion creates systematic double counting.
- **Why Possibly Novel (hypothesized):** Ontological-category probing (material vs. optical phenomena) for segmentation models appears new.
- **Minimal Experiment:** Curate mirror/water/glass scenes with annotated reflections; measure object-prompt hits on reflections vs. shadow controls; test "reflection of X" prompts.
- **Main Risk:** Annotation of reflection extents is genuinely ambiguous.
- **Cluster:** `sam3-concept-prompting`

### A-0045
- **Idea:** Study whether interactive concept refinement (adding positive/negative exemplars) converges to the intended concept or oscillates, formalizing concept-refinement dynamics as a fixed-point problem.
- **Problem:** Users refine concept queries with exemplars, but whether refinement monotonically approaches the target extension is unknown.
- **Hypothesis:** Refinement is non-monotonic in ≥30% of sessions (adding a correct exemplar reduces F1), driven by exemplar-embedding averaging that shifts the decision boundary in unintended directions.
- **Why Important:** Non-monotonic refinement destroys user trust and wastes labeling effort in exactly the hard cases.
- **Why Possibly Novel (hypothesized):** Convergence analysis of exemplar-based concept refinement in segmentation seems unstudied.
- **Minimal Experiment:** Simulate refinement sessions with oracle exemplar selection on 100 concepts; track F1 trajectories; identify oscillation conditions as a function of concept variance.
- **Main Risk:** Results depend on the specific exemplar-aggregation mechanism, limiting cross-model generality.
- **Cluster:** `sam3-concept-prompting`

---

## Sub-cluster 4: MedSAM & medical domain shift (`medsam-domain-shift`)

### A-0046
- **Idea:** Decompose MedSAM's improvement over SAM into intensity-statistics adaptation vs. anatomical-shape learning, by evaluating on intensity-remapped natural images and shape-preserved synthetic medical images.
- **Problem:** It is unclear whether medical fine-tuning teaches modality physics (CT/MR intensity statistics) or anatomy priors, which have different generalization implications.
- **Hypothesis:** Most of MedSAM's gain transfers to intensity-remapped natural objects (statistics), with anatomy-specific gains confined to organs with strong shape regularity.
- **Why Important:** Determines whether new modalities need full retraining or only intensity adaptation layers.
- **Why Possibly Novel (hypothesized):** Causal decomposition of medical fine-tuning gains along the statistics/shape axis appears untested.
- **Minimal Experiment:** Construct (a) natural images remapped to CT-like histograms and (b) synthetic phantoms with organ shapes but natural textures; compare SAM-vs-MedSAM deltas on each.
- **Main Risk:** Synthetic constructs may not cleanly isolate the two factors.
- **Cluster:** `medsam-domain-shift`

### A-0047
- **Idea:** Test whether MedSAM's box-prompt dependence hides an inability to reject wrong boxes: measuring segmentation behavior when boxes are misplaced on healthy tissue or wrong organs.
- **Problem:** Medical pipelines feed automatic detections as boxes; MedSAM's behavior under wrong boxes determines error propagation.
- **Hypothesis:** MedSAM segments a plausible-looking structure inside a wrong box in >80% of cases with high confidence, i.e., it lacks box-rejection capability entirely, and this rate is unaffected by fine-tuning data volume.
- **Why Important:** Quantifies a silent failure amplifier in cascaded medical systems where detection errors become confident wrong masks.
- **Why Possibly Novel (hypothesized):** Wrong-prompt rejection as a measurable competency for medical promptable models appears unexamined.
- **Minimal Experiment:** Systematically displace ground-truth boxes onto adjacent anatomy in CT/MR sets, record mask confidence and plausibility ratings from radiologists on a sample.
- **Main Risk:** "Plausible-looking" needs expert evaluation, which is costly.
- **Cluster:** `medsam-domain-shift`

### A-0048
- **Idea:** Investigate slice-wise inconsistency in 2D MedSAM applied to 3D volumes as a diagnostic signal: whether inter-slice mask incoherence predicts volumetric segmentation error better than per-slice confidence.
- **Problem:** 2D promptable models applied slice-by-slice produce 3D-incoherent organs, but incoherence is treated as noise rather than signal.
- **Hypothesis:** An inter-slice coherence statistic (e.g., Dice between adjacent slice masks adjusted for anatomy) predicts volumetric Dice with r>0.7, enabling label-free quality control.
- **Why Important:** Label-free QC is the practical bottleneck for deploying interactive medical segmentation at scale.
- **Why Possibly Novel (hypothesized):** Using cross-slice incoherence as a calibrated quality predictor appears underexplored.
- **Minimal Experiment:** Segment 200 CT volumes slice-wise, compute coherence statistics, correlate with GT volumetric Dice, compare against confidence-based QC.
- **Main Risk:** Coherence may fail for genuinely irregular pathologies (infiltrative tumors).
- **Cluster:** `medsam-domain-shift`

### A-0049
- **Idea:** Test whether medical fine-tuning of SAM redistributes errors from over-segmentation to under-segmentation in a clinically asymmetric way, and whether the direction is controllable at fine-tuning time.
- **Problem:** Clinical harm is asymmetric (missing tumor tissue ≠ including healthy margin), but fine-tuning optimizes symmetric losses.
- **Hypothesis:** Standard MedSAM fine-tuning systematically shifts boundary bias inward (under-segmentation of lesions), and a boundary-asymmetric loss weighting can set the bias direction without losing overall Dice.
- **Why Important:** Bias direction, not just magnitude, determines clinical safety of automated margins.
- **Why Possibly Novel (hypothesized):** Directional boundary-bias analysis and control for promptable medical models appears novel.
- **Minimal Experiment:** Measure signed boundary error distributions of SAM vs. MedSAM on lesion datasets; retrain with asymmetric losses at 3 settings; verify controllability.
- **Main Risk:** Signed boundary error is sensitive to annotation-style bias in ground truth.
- **Cluster:** `medsam-domain-shift`

### A-0050
- **Idea:** Quantify "scanner fingerprint sensitivity": whether MedSAM performance varies more across scanner manufacturers than across patients, using multi-site datasets with crossed factors.
- **Problem:** Deployment spans scanners, but variance decomposition of promptable-model error into scanner vs. patient factors is missing.
- **Hypothesis:** Scanner identity explains more variance in MedSAM Dice than patient-level anatomy variation for at least some organs, and the scanner effect is concentrated in encoder early layers.
- **Why Important:** If scanners dominate, site-specific PEFT calibration becomes a certification requirement, not an option.
- **Why Possibly Novel (hypothesized):** Formal variance decomposition (mixed-effects) for foundation-model medical segmentation appears rare.
- **Minimal Experiment:** Fit mixed-effects models of Dice on multi-site CT/MR (scanner, site, patient factors); probe early-layer feature shifts across scanners.
- **Main Risk:** Public multi-site data may confound scanner with population.
- **Cluster:** `medsam-domain-shift`

### A-0051
- **Idea:** Study whether MedSAM inherits and amplifies annotation-style artifacts from its fine-tuning corpus: e.g., systematically reproducing the margin conventions of the dominant annotating institution.
- **Problem:** Medical GT encodes institutional annotation styles; a foundation model may homogenize toward the majority style, silently overriding local clinical conventions.
- **Hypothesis:** MedSAM's boundary placement on held-out data matches the majority training institution's style more than the test institution's own style, measurable via style-classifier probes on boundary geometry.
- **Why Important:** Style override is a governance problem: models impose foreign conventions on local practice.
- **Why Possibly Novel (hypothesized):** Institutional-style transfer as a measurable property of medical foundation models appears unstudied.
- **Minimal Experiment:** Train a boundary-style classifier distinguishing institutions on GT; apply to MedSAM outputs on cross-institution test sets; quantify style attribution.
- **Main Risk:** Requires datasets with known institutional provenance.
- **Cluster:** `medsam-domain-shift`

### A-0052
- **Idea:** Test few-shot modality onboarding: how many labeled cases from a truly novel modality (e.g., photoacoustic imaging) are needed for PEFT-adapted MedSAM to match a from-scratch U-Net, mapping the crossover curve.
- **Problem:** The "foundation models need less data" claim lacks crossover analysis on genuinely unseen medical modalities.
- **Hypothesis:** The PEFT-vs-scratch crossover occurs below 50 labeled volumes for structurally familiar anatomy but above 500 for novel contrast mechanisms, showing the prior is anatomical rather than physical.
- **Why Important:** Directly informs data-budget planning for new clinical imaging technologies.
- **Why Possibly Novel (hypothesized):** Crossover-curve methodology on truly out-of-corpus modalities appears missing.
- **Minimal Experiment:** On 2 rare modalities, sweep training-set size for LoRA-MedSAM vs. nnU-Net-style baseline; locate crossover points per anatomy.
- **Main Risk:** Access to rare-modality data with quality labels.
- **Cluster:** `medsam-domain-shift`

### A-0053
- **Idea:** Investigate whether pathology (tumors, anomalies) breaks MedSAM's shape priors constructively or destructively: does the model fall back to image evidence or hallucinate healthy anatomy?
- **Problem:** Foundation models trained mostly on typical anatomy may complete lesions into "expected" healthy shapes.
- **Hypothesis:** On organs with resections/anomalies, MedSAM's masks are biased toward the healthy-population shape atlas (measurable as reduced Dice specifically in the anomalous region), evidencing prior-driven hallucination.
- **Why Important:** Shape hallucination in pathological cases is precisely where medical segmentation matters most.
- **Why Possibly Novel (hypothesized):** Atlas-bias quantification of promptable models on anomalous anatomy appears new.
- **Minimal Experiment:** Evaluate on post-surgical/anomalous organ datasets; decompose error into anomalous-region vs. typical-region components; compare against a no-shape-prior baseline.
- **Main Risk:** Anomalous-region localization requires extra annotation effort.
- **Cluster:** `medsam-domain-shift`

### A-0054
- **Idea:** Ask whether prompt semantics differ across medical and natural domains: a box in natural images means "the object," but in medicine may mean "region of interest including context" — and whether models internalize this pragmatic difference.
- **Problem:** Prompt pragmatics are domain-dependent, but fine-tuning treats prompts as syntactically identical across domains.
- **Hypothesis:** MedSAM interprets loose boxes as "segment the central organ" while SAM interprets them as "segment the largest salient object," and this pragmatic divergence is measurable by varying box looseness on matched cases.
- **Why Important:** Explains cross-domain prompt-transfer failures and informs prompt-standardization for clinical UIs.
- **Why Possibly Novel (hypothesized):** Prompt-pragmatics as a learned, domain-specific convention appears unexamined.
- **Minimal Experiment:** Sweep box looseness (1.0×–3.0× GT) on natural and medical images for SAM/MedSAM; characterize the target-selection function of each model.
- **Main Risk:** Findings may reflect dataset box-style statistics rather than deep pragmatics.
- **Cluster:** `medsam-domain-shift`

### A-0055
- **Idea:** Quantify the interaction between windowing (CT display transforms) and MedSAM performance: whether the model has an implicit preferred windowing and how much performance is lost by feeding raw or wrongly windowed inputs.
- **Problem:** CT preprocessing choices (window/level) are inconsistent across deployments, and their effect on foundation-model segmentation is unquantified.
- **Hypothesis:** MedSAM has a narrow effective windowing basin (performance drops >10 Dice outside it), and a learned per-case windowing predictor recovers the loss, indicating windowing should be model-internal.
- **Why Important:** Preprocessing mismatch is among the most common silent failure sources in clinical ML integration.
- **Why Possibly Novel (hypothesized):** Systematic windowing-sensitivity mapping for medical foundation models appears unreported.
- **Minimal Experiment:** Evaluate MedSAM over a windowing grid on abdominal CT; fit sensitivity surfaces per organ; train a tiny windowing regressor and re-evaluate.
- **Main Risk:** Optimal windowing may differ per organ within one scan, complicating a single-input pipeline.
- **Cluster:** `medsam-domain-shift`

### A-0056
- **Idea:** Test cross-anatomy prompt interference in a single fine-tuned model: whether adding fine-tuning data for new organs degrades boundary conventions on previously mastered organs even when overall Dice holds.
- **Problem:** Sequential dataset accretion is the norm for medical model updates, but subtle regression in boundary conventions may hide under stable aggregate Dice.
- **Hypothesis:** After adding organ-B data, organ-A Dice is stable but organ-A boundary-distance distributions shift measurably toward organ-B's annotation conventions — convention-level forgetting invisible to Dice.
- **Why Important:** Regulatory-grade model updates need convention stability, not just metric stability.
- **Why Possibly Novel (hypothesized):** Convention-level (as opposed to accuracy-level) forgetting seems undefined in the literature.
- **Minimal Experiment:** Sequentially fine-tune on organ datasets with distinct margin conventions; track boundary-signed-error distributions per organ across stages.
- **Main Risk:** Convention differences across datasets may be too small to detect reliably.
- **Cluster:** `medsam-domain-shift`

### A-0057
- **Idea:** Study whether uncertainty maps from medical promptable models align with inter-radiologist disagreement regions, testing the claim that model uncertainty can substitute for multi-reader variability estimates.
- **Problem:** Multi-reader studies are expensive; model uncertainty is offered as a proxy without rigorous alignment evidence at the pixel level.
- **Hypothesis:** Pixelwise correlation between MedSAM ensemble uncertainty and inter-reader disagreement is moderate on smooth organs but near zero on pathology boundaries — exactly where it is needed.
- **Why Important:** Determines whether uncertainty maps can legitimately inform contour review prioritization.
- **Why Possibly Novel (hypothesized):** Pixel-level uncertainty-vs-reader-disagreement alignment for foundation models appears sparsely studied.
- **Minimal Experiment:** Use multi-reader datasets (e.g., prostate/lung), compute model uncertainty via prompt+dropout ensembles, correlate with reader variance maps stratified by tissue type.
- **Main Risk:** Few public multi-reader datasets; disagreement conflates style and true ambiguity.
- **Cluster:** `medsam-domain-shift`

### A-0058
- **Idea:** Investigate resolution-anisotropy failure: whether MedSAM errors on anisotropic volumes (thick slices) are dominated by the encoder's isotropy assumption and fixable by anisotropy-conditioned positional rescaling at inference.
- **Problem:** Medical volumes have wildly varying slice thickness; 2D models see anisotropy as unfamiliar aspect-ratio distortion in reformatted views.
- **Hypothesis:** Performance on sagittal/coronal reformats degrades proportionally to anisotropy ratio, and rescaling positional embeddings by the acquisition spacing recovers ≥50% of the loss without retraining.
- **Why Important:** Zero-training fixes for anisotropy would broaden usable views in clinical review tools.
- **Why Possibly Novel (hypothesized):** Spacing-conditioned positional correction at inference appears untried for promptable medical models.
- **Minimal Experiment:** Evaluate on reformatted views across anisotropy ratios; apply spacing-aware positional rescaling; measure recovery per organ.
- **Main Risk:** Positional rescaling may interact badly with pretrained attention patterns.
- **Cluster:** `medsam-domain-shift`

### A-0059
- **Idea:** Test whether MedSAM's failures on small lesions are detection failures or segmentation failures, by decoupling with oracle prompts: perfect boxes on lesions the model would otherwise miss.
- **Problem:** Small-lesion metrics conflate "can't find it" with "can't delineate it," blocking targeted improvement.
- **Hypothesis:** With oracle boxes, small-lesion Dice recovers to within 10 points of large-lesion Dice, localizing the deficit almost entirely to the prompting/detection stage rather than mask decoding.
- **Why Important:** Cleanly directs investment either to detection front-ends or decoder capacity for the highest-stakes medical targets.
- **Why Possibly Novel (hypothesized):** Oracle-prompt decoupling analysis specific to lesion size appears underused.
- **Minimal Experiment:** On lesion datasets stratified by diameter, compare automatic-prompt vs. oracle-box Dice; report the recoverable fraction per size bin.
- **Main Risk:** Oracle boxes may leak size information that inflates apparent decoder competence.
- **Cluster:** `medsam-domain-shift`

### A-0060
- **Idea:** Examine whether federating PEFT adapters across hospitals (adapter averaging vs. routing) preserves site-specific calibration while sharing anatomical knowledge, formalized as a modularity test of medical adaptation.
- **Problem:** Data can't leave hospitals; whether adapter-space aggregation shares the right knowledge (anatomy) without sharing the wrong knowledge (site biases) is untested.
- **Hypothesis:** Averaged adapters transfer anatomy gains across sites but degrade per-site calibration, whereas a two-component decomposition (shared + site-specific low-rank parts) preserves both, demonstrating separability of knowledge types in adapter space.
- **Why Important:** Provides a concrete privacy-compatible mechanism for multi-site medical model improvement.
- **Why Possibly Novel (hypothesized):** Knowledge-type separability in federated adapter aggregation for segmentation appears unexplored.
- **Minimal Experiment:** Train LoRA adapters at 4+ simulated "sites" (public datasets), compare averaging vs. shared+specific decomposition on cross-site Dice and per-site ECE.
- **Main Risk:** Public datasets may under-represent true inter-hospital variation.
- **Cluster:** `medsam-domain-shift`

---

## Sub-cluster 5: Boundary quality (`boundary-quality`)

### A-0061
- **Idea:** Test whether SAM-family boundary errors are spectrally band-limited: errors concentrate in boundary curvature frequencies above a cutoff set by the mask decoder's upsampling path, defining a "boundary Nyquist limit" for promptable models.
- **Problem:** Boundary error is reported as scalar metrics, hiding which spatial frequencies of the true contour the model can and cannot represent.
- **Hypothesis:** Contour error energy is negligible below a model-specific curvature frequency and near-total above it, with the cutoff predictable from decoder feature-map resolution.
- **Why Important:** A spectral limit converts vague "coarse boundaries" complaints into a measurable architectural constant guiding decoder design.
- **Why Possibly Novel (hypothesized):** Fourier analysis of contour error as a function of decoder resolution appears unformalized.
- **Minimal Experiment:** Compute contour Fourier descriptors of GT vs. predicted masks across models with different decoder resolutions; locate error cutoffs; test predictability from architecture.
- **Main Risk:** Natural object contours may lack sufficient high-frequency content to identify cutoffs precisely.
- **Cluster:** `boundary-quality`

### A-0062
- **Idea:** Investigate whether high-quality boundary heads (HQ-SAM style) improve real boundary accuracy or mostly improve boundary "confidence sharpness" that games boundary metrics against soft ground truth.
- **Problem:** Boundary-metric improvements may reflect harder thresholding rather than better localization, since GT boundaries are themselves uncertain by 1–3 pixels.
- **Hypothesis:** A significant fraction of HQ-style metric gains disappears when evaluated against multi-annotator soft boundaries instead of single-annotator hard boundaries.
- **Why Important:** Prevents the field from optimizing an artifact of hard-label evaluation rather than perceptual boundary quality.
- **Why Possibly Novel (hypothesized):** Re-evaluating boundary-quality methods against soft/multi-annotator references appears rare.
- **Minimal Experiment:** Collect 5-annotator boundaries on 300 objects; recompute boundary F-scores for SAM vs. HQ-SAM against soft references; compare gain shrinkage.
- **Main Risk:** Multi-annotator collection cost; annotator instructions may bias softness.
- **Cluster:** `boundary-quality`

### A-0063
- **Idea:** Characterize the "boundary attachment hierarchy" of segmentation foundation models: when true boundaries are weak, which image cues (color edges, texture edges, depth discontinuities) the predicted boundary snaps to, in what priority order.
- **Problem:** Predicted boundaries deviate systematically under weak evidence, but the model's cue-priority ordering is unknown.
- **Hypothesis:** SAM-family models have a stable cue hierarchy (luminance edge > texture boundary > semantic boundary) that mispredicts human boundary placement in camouflage and low-contrast regimes in a systematic, correctable direction.
- **Why Important:** Cue hierarchies explain and predict entire families of boundary failures rather than treating each as noise.
- **Why Possibly Novel (hypothesized):** Psychophysics-style cue-conflict experiments for segmentation boundary attachment appear novel.
- **Minimal Experiment:** Render cue-conflict stimuli (color edge displaced from texture edge from GT boundary); measure attachment rates per cue across displacement magnitudes.
- **Main Risk:** Synthetic cue-conflict stimuli may be off-distribution.
- **Cluster:** `boundary-quality`

### A-0064
- **Idea:** Test whether boundary quality and region quality are represented by separable subspaces in SAM's decoder, such that PEFT restricted to the boundary subspace improves contours without touching region behavior.
- **Problem:** Fine-tuning for boundaries typically shifts region behavior too, suggesting entangled representations—but separability has not been tested directly.
- **Hypothesis:** There exists a low-dimensional decoder weight subspace whose perturbation changes boundary F-score with near-zero effect on region IoU, demonstrable via subspace-constrained fine-tuning.
- **Why Important:** Separable control would enable surgical quality fixes without whole-model revalidation.
- **Why Possibly Novel (hypothesized):** Boundary/region subspace decomposition of decoder weights appears untried.
- **Minimal Experiment:** Fine-tune with projection onto candidate subspaces (from gradient PCA of boundary-only vs. region-only losses); measure the boundary/region change ratio.
- **Main Risk:** Subspaces may be input-dependent, defeating a global decomposition.
- **Cluster:** `boundary-quality`

### A-0065
- **Idea:** Quantify boundary error as a function of annotation-tool provenance in training data: whether polygon-annotated training masks cause vertex-like straight-line artifacts in model boundary predictions.
- **Problem:** Training masks carry tool artifacts (polygon straightness, brush smoothness); models may learn tool geometry as boundary prior.
- **Hypothesis:** Models trained on polygon-heavy data produce measurably straighter boundary segments (lower curvature entropy) than the true object statistics, and the artifact strength tracks the training-tool mixture.
- **Why Important:** Reveals that "boundary quality" ceilings may be data artifacts, redirecting effort from architectures to annotation processes.
- **Why Possibly Novel (hypothesized):** Tool-artifact inheritance in learned boundary statistics appears undocumented.
- **Minimal Experiment:** Compare curvature statistics of predictions from models trained on polygon vs. matting-quality masks on identical test sets; correlate with training-source composition.
- **Main Risk:** Confounded by dataset content differences beyond tool type.
- **Cluster:** `boundary-quality`

### A-0066
- **Idea:** Study occlusion-boundary vs. object-boundary confusion: whether segmentation models place boundaries at self-occlusion contours inside objects, and if this error is predictable from local depth-gradient magnitude.
- **Problem:** Models sometimes cut objects along internal contours (arm across body); the systematicity of this failure is unmeasured.
- **Hypothesis:** Internal-boundary insertion probability scales with the strength of internal depth discontinuity, showing models use depth-edge proxies rather than object-level continuity.
- **Why Important:** Predicts failures in articulated objects and informs whether monocular depth priors help or hurt segmentation.
- **Why Possibly Novel (hypothesized):** Depth-conditioned analysis of internal-boundary errors appears new.
- **Minimal Experiment:** Use datasets with depth (or estimated depth); detect internal-cut errors; regress error probability on internal depth-gradient statistics.
- **Main Risk:** Estimated depth introduces its own model biases into the analysis.
- **Cluster:** `boundary-quality`

### A-0067
- **Idea:** Test a "boundary consistency under prompt ensembles" measure: whether averaging masks from multiple prompts sharpens or blurs boundaries, resolving when ensembling helps boundary quality.
- **Problem:** Prompt ensembling is used for robustness, but its effect on boundary localization (systematic sharpening vs. blurring) is unquantified.
- **Hypothesis:** Prompt ensembling improves boundary F-score only when individual-mask boundary errors are unbiased (zero-mean); under biased errors (consistent over/under-shoot) it entrenches the bias, and the regime is predictable per object.
- **Why Important:** Turns ensembling from folklore into a conditionally applied tool with a decision rule.
- **Why Possibly Novel (hypothesized):** Bias-variance decomposition of boundary error under prompt ensembling appears unstudied.
- **Minimal Experiment:** For 1k objects, decompose boundary error into bias/variance across 10 prompts; verify ensemble gain aligns with the variance-dominant regime.
- **Main Risk:** Decomposition requires accurate GT boundaries at pixel level.
- **Cluster:** `boundary-quality`

### A-0068
- **Idea:** Investigate whether transparent and translucent object boundaries expose a fundamental limitation of binary mask supervision: models trained with hard masks cannot represent partial coverage, and where they place the hard boundary is arbitrary.
- **Problem:** Glass, smoke, hair require soft coverage, but SAM-family outputs are effectively binary; the placement policy of the forced hard boundary is uncharacterized.
- **Hypothesis:** On translucent regions, boundary placement variance across prompts is an order of magnitude higher than on opaque regions, and predicted logits in these regions carry recoverable alpha-matte information despite binary training.
- **Why Important:** Determines whether soft-mask capability is latent in existing models (cheap to extract) or absent (needs retraining).
- **Why Possibly Novel (hypothesized):** Probing binary-trained mask logits for latent matting information appears novel.
- **Minimal Experiment:** Evaluate SAM logits against alpha mattes on translucency datasets; measure rank correlation between logits and true alpha in soft regions.
- **Main Risk:** Logit-alpha correlation may reflect trivial distance-to-boundary effects.
- **Cluster:** `boundary-quality`

### A-0069
- **Idea:** Formalize "boundary drift under iterative refinement": whether repeated interactive corrections asymptotically converge to GT boundaries or to a model-specific attractor contour offset from GT.
- **Problem:** Interactive refinement assumes convergence to truth with enough clicks, but the fixed point of the refinement operator is unknown.
- **Hypothesis:** For each object there exists an attractor contour differing from GT by a systematic offset (dependent on local contrast), and no click sequence can reduce error below this floor.
- **Why Important:** Establishes the accuracy ceiling of interactive workflows, informing when pixel-perfect tasks need different tools.
- **Why Possibly Novel (hypothesized):** Fixed-point characterization of interactive segmentation dynamics appears absent.
- **Minimal Experiment:** Run exhaustive refinement (50+ oracle clicks) on 300 objects; measure asymptotic residual error and its correlation with local image statistics.
- **Main Risk:** Oracle-click policies may not explore the reachable set fully.
- **Cluster:** `boundary-quality`

### A-0070
- **Idea:** Test whether boundary quality transfers across scale: models fine-tuned to sharpen boundaries at one object scale may not transfer sharpening to other scales, revealing scale-specific boundary circuits.
- **Problem:** Boundary fine-tuning datasets have biased size distributions; whether learned sharpening generalizes across scales is unknown.
- **Hypothesis:** Boundary-F gains from fine-tuning on large objects transfer <30% to small objects (and vice versa), indicating scale-indexed rather than scale-invariant boundary processing.
- **Why Important:** Dictates whether boundary-quality data collection must stratify by scale.
- **Why Possibly Novel (hypothesized):** Scale-transfer analysis of boundary fine-tuning appears untested.
- **Minimal Experiment:** Fine-tune on size-restricted subsets (small-only, large-only); evaluate boundary metrics across the full size spectrum; compute transfer matrices.
- **Main Risk:** Size subsets differ in content, confounding scale with category.
- **Cluster:** `boundary-quality`

### A-0071
- **Idea:** Examine whether the standard mask upsampling path (transposed conv/interpolation) imposes an anisotropic boundary error: axis-aligned boundaries reconstructed better than diagonal ones.
- **Problem:** Upsampling grids are axis-aligned; whether this produces measurable orientation bias in boundary accuracy is unquantified.
- **Hypothesis:** Boundary error as a function of local contour orientation shows 4-fold periodicity (worst at 45°), with amplitude determined by the upsampling method, and orientation-aware upsampling removes it.
- **Why Important:** Orientation bias corrupts shape measurements downstream (e.g., morphology in biology).
- **Why Possibly Novel (hypothesized):** Orientation-resolved boundary-error analysis tied to upsampler design appears new.
- **Minimal Experiment:** Bin boundary errors by local GT contour orientation across datasets and models; compare amplitude across upsampler variants retrained identically.
- **Main Risk:** Natural-image orientation statistics may mask the effect; may need rotated evaluation.
- **Cluster:** `boundary-quality`

### A-0072
- **Idea:** Ask whether models can predict their own boundary error field: an auxiliary head trained to output per-boundary-pixel expected displacement, tested for calibration and downstream utility in weighted fusion.
- **Problem:** Confidence maps exist for regions, but calibrated boundary displacement error prediction is missing.
- **Hypothesis:** Expected boundary displacement is learnable to within 30% relative error and enables error-weighted mask fusion that beats uniform fusion on boundary F by a significant margin.
- **Why Important:** Boundary-error awareness is a prerequisite for metrology-grade uses of segmentation (measurement, dosimetry).
- **Why Possibly Novel (hypothesized):** Boundary displacement-field self-prediction with calibration analysis appears unexplored.
- **Minimal Experiment:** Train displacement head on existing datasets' residuals; evaluate calibration curves; test fusion utility on multi-prompt outputs.
- **Main Risk:** Residual fields may be too stochastic to learn beyond trivial contrast correlates.
- **Cluster:** `boundary-quality`

### A-0073
- **Idea:** Study "semantic boundary leakage": whether boundaries between two touching objects of the same class are systematically worse than object-background boundaries at matched contrast, isolating instance-separation as a distinct boundary competence.
- **Problem:** Boundary metrics average over boundary types; instance-instance boundaries may be the true weak point but are not reported separately.
- **Hypothesis:** At matched local contrast, instance-instance boundary F is ≥20 points below instance-background F, and the gap survives boundary-focused fine-tuning, indicating a representational (not resolution) limit.
- **Why Important:** Touching-instance separation drives errors in counting, crowd analysis, and biology.
- **Why Possibly Novel (hypothesized):** Contrast-controlled decomposition of boundary types appears unreported.
- **Minimal Experiment:** Classify each GT boundary pixel by type; compute type-conditional boundary metrics matched on local contrast; test persistence after HQ fine-tuning.
- **Main Risk:** Contrast matching across boundary types reduces usable data substantially.
- **Cluster:** `boundary-quality`

### A-0074
- **Idea:** Test whether logit-space boundary refinement (deconvolving the decoder's learned blur) can recover boundary detail without any retraining, treating the decoder as a known degradation operator.
- **Problem:** Decoders apply a learned effective blur to boundaries; if that blur is stable and estimable, classical deconvolution could invert it post hoc.
- **Hypothesis:** The decoder's boundary point-spread function is approximately input-independent, and Wiener-style deconvolution of mask logits improves boundary F on high-res GT without harming region IoU.
- **Why Important:** A training-free boundary upgrade applicable to all frozen deployments.
- **Why Possibly Novel (hypothesized):** Treating mask decoders as estimable linear degradation operators appears untried.
- **Minimal Experiment:** Estimate the effective PSF from step-edge synthetic inputs; apply deconvolution to logits on real data; measure boundary/region metric changes.
- **Main Risk:** The effective blur is likely input-dependent and nonlinear, breaking the deconvolution model.
- **Cluster:** `boundary-quality`

### A-0075
- **Idea:** Investigate human perceptual thresholds for boundary error in applied contexts: below what boundary F improvement do downstream human users (editors, clinicians) stop noticing differences, calibrating "sufficient" boundary quality per application.
- **Problem:** Boundary research chases metric gains without evidence that users perceive or benefit from them beyond some threshold.
- **Hypothesis:** Perceptual indifference thresholds vary by an order of magnitude across applications (photo editing vs. radiotherapy), and current SOTA already exceeds the threshold for several applications while falling far short for others.
- **Why Important:** Aligns research investment with real utility and defines application-specific stopping criteria.
- **Why Possibly Novel (hypothesized):** Psychophysical indifference-threshold measurement for segmentation boundary quality appears missing.
- **Minimal Experiment:** Two-alternative forced-choice studies with domain users comparing mask pairs at controlled boundary-F deltas across 3 application framings.
- **Main Risk:** User studies are expensive and threshold estimates may be task-framing sensitive.
- **Cluster:** `boundary-quality`

---

## Sub-cluster 6: Mobile / distillation failures (`mobile-distillation`)

### A-0076
- **Idea:** Characterize what is lost first in SAM distillation: rank-order the degradation of capabilities (boundary detail, ambiguity handling, rare-category grounding, prompt robustness) as student capacity shrinks.
- **Problem:** Distilled models report aggregate mIoU deltas, hiding which capabilities collapse first and guiding neither users nor distillers.
- **Hypothesis:** Capabilities degrade in a consistent order across distillation methods (ambiguity handling first, boundary detail last), implying capability-specific capacity thresholds rather than uniform degradation.
- **Why Important:** A capability-degradation ladder tells practitioners what a small model can be trusted for.
- **Why Possibly Novel (hypothesized):** Capability-ordered degradation analysis of segmentation distillation appears new.
- **Minimal Experiment:** Distill students at 5 capacity points; evaluate a battery isolating each capability; test order consistency across two distillation losses.
- **Main Risk:** Capability batteries may not cleanly isolate single capabilities.
- **Cluster:** `mobile-distillation`

### A-0077
- **Idea:** Test whether encoder-only distillation (MobileSAM style) creates a student-decoder mismatch: the frozen decoder receives slightly off-manifold features, causing errors that joint fine-tuning would fix at negligible cost.
- **Problem:** Reusing the teacher's decoder with a distilled encoder assumes feature-space compatibility that may fail off the distillation distribution.
- **Hypothesis:** Student encoder features lie measurably off the teacher feature manifold on out-of-distribution images (higher reconstruction error under a teacher-feature autoencoder), and decoder errors concentrate exactly where manifold deviation is largest.
- **Why Important:** Identifies a cheap fix (brief decoder adaptation) and a diagnostic (manifold distance) for distilled deployments.
- **Why Possibly Novel (hypothesized):** Manifold-deviation analysis of encoder-distilled promptable models appears unexamined.
- **Minimal Experiment:** Fit a density/AE model to teacher features; correlate student deviation with per-image IoU drop; test 1-epoch decoder adaptation.
- **Main Risk:** Manifold estimates in high dimensions are fragile.
- **Cluster:** `mobile-distillation`

### A-0078
- **Idea:** Study whether distillation transfers the teacher's prompt sensitivity or filters it: do students inherit the teacher's click-fragility maps, or develop their own?
- **Problem:** Distillation may copy pathologies along with capabilities, but pathology inheritance in promptable models is unmeasured.
- **Hypothesis:** Student fragility maps correlate with the teacher's (r>0.5) far more than architecture-matched independently trained models (r<0.2), demonstrating pathology inheritance through the distillation signal.
- **Why Important:** If pathologies are inherited, distillation offers a controlled setting to study — and selectively filter — failure modes.
- **Why Possibly Novel (hypothesized):** Failure-mode inheritance analysis in distillation appears understudied for segmentation.
- **Minimal Experiment:** Compute click-fragility maps for teacher, distilled students, and independently trained controls on shared images; compare correlation structure.
- **Main Risk:** Shared training data alone may explain fragility correlation.
- **Cluster:** `mobile-distillation`

### A-0079
- **Idea:** Investigate quantization's disparate impact on segmentation: whether INT8/INT4 quantization degrades boundary pixels disproportionately relative to interior pixels, and which layers cause it.
- **Problem:** Quantization is validated on aggregate metrics, but boundary-localized degradation would matter most for segmentation quality.
- **Hypothesis:** Quantization error concentrates on boundary logits (where activations are near decision thresholds), with the final decoder layers contributing most, so mixed-precision on <10% of layers recovers most boundary loss.
- **Why Important:** Boundary-aware quantization policies could make high-quality edge deployment feasible.
- **Why Possibly Novel (hypothesized):** Spatially resolved (boundary vs. interior) quantization-impact analysis appears new for promptable segmentation.
- **Minimal Experiment:** Quantize progressively; map per-pixel logit perturbation vs. distance-to-boundary; layer-wise sensitivity scan; test targeted mixed precision.
- **Main Risk:** Effects may be hardware/kernel-specific, reducing generality.
- **Cluster:** `mobile-distillation`

### A-0080
- **Idea:** Test the "resolution honesty" of efficient SAM variants: whether claimed support for high-res inputs actually improves effective output resolution, measured by the smallest resolvable structure rather than input pixel count.
- **Problem:** Efficient variants accept large inputs but may internally downsample, making input resolution a misleading spec.
- **Hypothesis:** Effective resolution (minimum resolvable gap/protrusion size, measured psychophysics-style with synthetic targets) saturates well below input resolution for most efficient variants, and the saturation point predicts real-data small-structure performance.
- **Why Important:** Gives users an honest, comparable "effective resolution" spec for model selection.
- **Why Possibly Novel (hypothesized):** Resolvable-structure-based resolution measurement for segmentation models appears unproposed.
- **Minimal Experiment:** Synthetic charts with parametric gaps/protrusions; find detection thresholds per model; validate against thin-structure benchmarks.
- **Main Risk:** Synthetic thresholds may not transfer to cluttered natural scenes.
- **Cluster:** `mobile-distillation`

### A-0081
- **Idea:** Ask whether distillation data composition matters more than method: a factorial study crossing distillation objectives with data mixtures to attribute student quality variance.
- **Problem:** Distillation papers vary method and data simultaneously; the community cannot tell which choice drives reported gains.
- **Hypothesis:** Data-mixture factors explain more student-performance variance than objective factors for promptable segmentation, especially in tail categories.
- **Why Important:** Redirects efficiency research toward data curation if the hypothesis holds, saving effort on objective engineering.
- **Why Possibly Novel (hypothesized):** Controlled factorial attribution in segmentation distillation appears missing.
- **Minimal Experiment:** 3 objectives × 4 data mixtures, same student architecture and budget; variance decomposition of downstream metrics.
- **Main Risk:** Compute cost of the factorial grid; interactions may dominate main effects.
- **Cluster:** `mobile-distillation`

### A-0082
- **Idea:** Study latency-accuracy scheduling within a single model: whether early-exit mask decoding (emitting masks from intermediate decoder states) provides usable anytime segmentation, and where quality jumps occur.
- **Problem:** Edge systems need anytime outputs, but promptable decoders are all-or-nothing; the quality profile of intermediate states is unknown.
- **Hypothesis:** Intermediate decoder states yield monotonically improving masks with a large quality jump at a specific stage (hypothesized: after the second token-to-image attention), making one natural early-exit point nearly free.
- **Why Important:** Anytime segmentation enables graceful degradation under variable compute budgets.
- **Why Possibly Novel (hypothesized):** Early-exit analysis inside promptable mask decoders appears unexplored.
- **Minimal Experiment:** Instrument decoder to emit masks per stage; measure quality-vs-stage curves across datasets; identify jump structure.
- **Main Risk:** Intermediate states may need a trained readout head, adding confound.
- **Cluster:** `mobile-distillation`

### A-0083
- **Idea:** Test whether small students benefit from "uncertainty-matched" distillation: matching the teacher's output distribution (including its ambiguity structure) rather than its argmax masks.
- **Problem:** Standard distillation transfers point predictions, discarding the teacher's ambiguity representation, which may be the harder-won knowledge.
- **Hypothesis:** Students distilled to match the teacher's multimask output distribution (all mask hypotheses + scores) preserve ambiguity handling at small capacity better than argmax distillation, at equal aggregate IoU.
- **Why Important:** Preserving ambiguity handling determines whether small models can drive interactive UIs safely.
- **Why Possibly Novel (hypothesized):** Multihypothesis-distribution distillation for promptable segmentation appears untested.
- **Minimal Experiment:** Distill with argmax vs. full-hypothesis matching; evaluate on ambiguity benchmarks (part/whole clicks) and standard suites.
- **Main Risk:** Hypothesis-matching losses may be unstable to optimize.
- **Cluster:** `mobile-distillation`

### A-0084
- **Idea:** Investigate whether efficient attention approximations (linear attention, pooling) in mobile variants specifically damage long-range mask coherence — the ability to include distant disconnected parts of one object.
- **Problem:** Efficient attention truncates long-range interactions; its effect on spatially extended object coherence is unquantified.
- **Hypothesis:** Mask fragmentation rate on spatially extended objects (e.g., fences, wires, occluded objects in two pieces) increases superlinearly as attention range shrinks, while compact-object metrics stay flat — a hidden failure invisible in standard benchmarks.
- **Why Important:** Defines which efficiency techniques are safe for which object types.
- **Why Possibly Novel (hypothesized):** Attention-range vs. object-extent interaction analysis appears new for segmentation.
- **Minimal Experiment:** Evaluate attention variants on an extent-stratified benchmark; measure fragmentation (connected-component errors) vs. object spatial extent.
- **Main Risk:** Extent-stratified data with disconnected GT objects is scarce; may need curation.
- **Cluster:** `mobile-distillation`

### A-0085
- **Idea:** Test cascaded deployment honesty: whether a small model + selective escalation to the large model (based on the small model's self-assessment) actually beats the large model alone on cost-quality curves, or whether self-assessment failures cluster exactly on escalation-worthy cases.
- **Problem:** Cascades assume the small model knows when it fails, but failure detection may be hardest exactly where the small model fails.
- **Hypothesis:** Small-model confidence is anticorrelated with escalation need on the most severe failures (confidently wrong), capping cascade performance well below oracle escalation, and an external lightweight escalation critic closes most of the gap.
- **Why Important:** Cascades are the dominant edge-deployment pattern; their true limits should be measured, not assumed.
- **Why Possibly Novel (hypothesized):** Adversarial analysis of self-assessed escalation in segmentation cascades appears missing.
- **Minimal Experiment:** Build MobileSAM→SAM cascade; compare confidence-based vs. oracle vs. learned-critic escalation on cost-quality Pareto curves.
- **Main Risk:** Results depend on threshold tuning; needs careful Pareto methodology.
- **Cluster:** `mobile-distillation`

### A-0086
- **Idea:** Examine whether token pruning/merging in ViT encoders discards exactly the tokens later needed by mask decoding: a temporal mismatch between pruning criteria (classification saliency) and segmentation needs (boundary tokens).
- **Problem:** Token-reduction methods are ported from classification, but segmentation needs dense boundary information that pruning criteria may deem unsalient.
- **Hypothesis:** Tokens pruned by attention-based saliency disproportionately cover object boundaries (measured by overlap statistics), and a decoder-gradient-informed pruning criterion retains boundary quality at equal token budgets.
- **Why Important:** Token reduction is the main ViT efficiency lever; making it segmentation-aware could be free quality.
- **Why Possibly Novel (hypothesized):** Boundary-coverage analysis of pruning criteria for promptable decoding appears new.
- **Minimal Experiment:** Log pruned-token locations vs. GT boundaries across pruning ratios; compare saliency-based vs. gradient-informed criteria at matched FLOPs.
- **Main Risk:** Gradient-informed criteria may be too expensive to compute online.
- **Cluster:** `mobile-distillation`

### A-0087
- **Idea:** Study whether distilled students can exceed their teacher locally: identifying image regimes where MobileSAM-class students beat SAM due to smoothing away teacher idiosyncrasies, formalizing "beneficial compression."
- **Problem:** Distillation is assumed strictly lossy, but compression may regularize away teacher noise in some regimes.
- **Hypothesis:** Students outperform teachers on a stable, characterizable subset (hypothesized: high-noise/low-light images where teacher overfits texture), and this subset is predictable from image statistics.
- **Why Important:** Regime-aware routing between student and teacher could beat both; also clarifies what teachers get wrong.
- **Why Possibly Novel (hypothesized):** Systematic characterization of student>teacher regimes in segmentation appears absent.
- **Minimal Experiment:** Paired evaluation on large corpora; isolate student-win clusters; train an image-statistics classifier to predict wins; verify on new data.
- **Main Risk:** Student wins may be sparse noise rather than stable regimes.
- **Cluster:** `mobile-distillation`

### A-0088
- **Idea:** Test the interaction of distillation with subsequent PEFT: whether distilled students are harder to fine-tune (less adaptable) than same-size scratch models, quantifying an "adaptability tax" of distillation.
- **Problem:** Users fine-tune distilled checkpoints, assuming adaptability equals that of normal models — untested.
- **Hypothesis:** At matched size and downstream data, distilled students adapt less (lower fine-tuned ceiling, slower convergence) than scratch-trained peers, because distillation collapses feature diversity needed for adaptation.
- **Why Important:** If true, "distill-then-adapt" pipelines should be reordered to "adapt-then-distill."
- **Why Possibly Novel (hypothesized):** The distillation-adaptability interaction appears unmeasured for vision models.
- **Minimal Experiment:** Distill and scratch-train matched architectures; LoRA-tune both on 5 downstream segmentation tasks; compare ceilings and sample efficiency; measure feature-space effective rank.
- **Main Risk:** Matched scratch baselines at reasonable quality require substantial compute.
- **Cluster:** `mobile-distillation`

### A-0089
- **Idea:** Investigate energy-per-mask as a first-class metric: profiling where energy is actually spent (encoder, decoder, memory traffic) across SAM variants, and whether architectural choices ranked by FLOPs re-rank under measured energy.
- **Problem:** Efficiency claims use FLOPs, but edge deployment cares about energy, and memory traffic often dominates.
- **Hypothesis:** Model rankings by measured energy-per-mask differ materially from FLOPs rankings (rank correlation <0.7), with memory-bound decoder stages penalizing some "efficient" designs.
- **Why Important:** Realigns the efficiency literature with the quantity deployments actually pay for.
- **Why Possibly Novel (hypothesized):** Measured-energy benchmarking of promptable segmentation families appears rare.
- **Minimal Experiment:** Profile 6 variants on 2 hardware targets with hardware energy counters across batch sizes and resolutions; publish energy-per-mask Pareto curves.
- **Main Risk:** Hardware specificity limits generality; needs at least two platforms.
- **Cluster:** `mobile-distillation`

### A-0090
- **Idea:** Test whether tiny prompt-conditioned models can skip the heavy image encoder entirely for repeated prompting: caching a scene representation once and answering many prompts with a micro-decoder, quantifying the amortization frontier.
- **Problem:** Interactive sessions re-pay encoder cost implicitly; the design space of "encode once, prompt many" with minimal decoders is unmapped.
- **Hypothesis:** For sessions with ≥5 prompts, a micro-decoder (<5M params) over cached features achieves ≥95% of full-decoder quality, and quality loss concentrates on prompts far (in feature space) from the session's earlier prompts.
- **Why Important:** Defines the true marginal cost of an additional prompt, central to interactive-tool economics.
- **Why Possibly Novel (hypothesized):** Amortization-frontier analysis for promptable segmentation sessions appears new.
- **Minimal Experiment:** Train micro-decoders at several sizes on cached SAM features; evaluate per-prompt quality vs. session statistics; map the amortization frontier.
- **Main Risk:** Micro-decoders may fail on ambiguity handling, which matters in interactive use.
- **Cluster:** `mobile-distillation`

---

## Sub-cluster 7: PEFT mechanics for vision/multimodal models (`peft-mechanics`)

### A-0091
- **Idea:** Test whether the optimal LoRA insertion depth for vision models is task-type-dependent in a predictable way: low-level tasks (boundary refinement) benefit from early-layer adapters, semantic tasks from late-layer adapters.
- **Problem:** LoRA placement in ViTs is chosen by convention (all attention layers), without a theory linking task type to placement.
- **Hypothesis:** A task's "feature-level demand" (measured by which frozen-layer probes best predict its labels) predicts the LoRA placement that maximizes fine-tuned performance, with rank correlation >0.7 across 12 tasks.
- **Why Important:** Converts PEFT placement from folklore to a measurable, predictive rule, saving sweep compute.
- **Why Possibly Novel (hypothesized):** Probe-predicted placement rules for vision PEFT appear unproposed.
- **Minimal Experiment:** For 12 segmentation/detection tasks, run frozen-layer probing, then sweep single-block LoRA placements; test whether probes predict the best placement.
- **Main Risk:** Placement effects may be too flat in large models to discriminate.
- **Cluster:** `peft-mechanics`

### A-0092
- **Idea:** Investigate whether LoRA ranks needed for vision adaptation are set by the intrinsic dimensionality of the domain shift rather than task complexity, using controlled shifts of measurable dimensionality.
- **Problem:** Rank selection is trial-and-error; no quantity computable from data predicts the required rank.
- **Hypothesis:** The minimal rank achieving 95% of full fine-tuning performance scales linearly with the estimated intrinsic dimension of the feature-space shift between source and target domains.
- **Why Important:** A rank-prediction rule would eliminate the most expensive PEFT hyperparameter search.
- **Why Possibly Novel (hypothesized):** Linking LoRA rank to measured shift dimensionality appears untested in vision.
- **Minimal Experiment:** Construct domain shifts of controlled dimensionality (parametric corruptions, style axes); sweep ranks; regress required rank on shift dimension estimates.
- **Main Risk:** Intrinsic-dimension estimators are noisy in high dimensions.
- **Cluster:** `peft-mechanics`

### A-0093
- **Idea:** Study "adapter interference algebra": when two independently trained LoRA adapters are composed (added), can interference be predicted from the principal angles between their weight-update subspaces?
- **Problem:** Adapter merging works sometimes and fails sometimes, with no predictive theory of when.
- **Hypothesis:** Post-composition performance drop correlates strongly with subspace overlap (small principal angles) in specific layers, enabling a pre-merge compatibility test that predicts failures before evaluation.
- **Why Important:** Reliable adapter composition would enable modular skill libraries for vision models.
- **Why Possibly Novel (hypothesized):** Geometric pre-merge compatibility prediction for vision adapters appears unvalidated.
- **Minimal Experiment:** Train 20 task adapters on one backbone; merge all pairs; regress pairwise performance drop on principal-angle statistics per layer.
- **Main Risk:** Interference may be governed by activation-space (not weight-space) geometry.
- **Cluster:** `peft-mechanics`

### A-0094
- **Idea:** Test whether prompt-encoder-only fine-tuning of SAM (freezing image encoder and mask decoder) suffices for a surprising range of domain adaptations, implying many "domain gaps" are prompt-interpretation gaps.
- **Problem:** Domain adaptation defaults to adapting the encoder, but if failures stem from prompt semantics, adapting the tiny prompt path may suffice.
- **Hypothesis:** For ≥30% of tested domain adaptations (medical, aerial, microscopy), prompt-encoder-only tuning recovers ≥80% of full-PEFT gains at <1% of trainable parameters.
- **Why Important:** Would dramatically cheapen adaptation and pinpoint where domain knowledge actually needs to live.
- **Why Possibly Novel (hypothesized):** Systematic component-attribution of adaptation gains in promptable models appears missing.
- **Minimal Experiment:** For 8 domains, fine-tune each component in isolation (prompt encoder, decoder, encoder-LoRA) and in combination; build an attribution table.
- **Main Risk:** Component interactions may make isolated attributions misleading.
- **Cluster:** `peft-mechanics`

### A-0095
- **Idea:** Investigate the loss-landscape connectivity of PEFT solutions: whether independently trained LoRA runs on the same task land in linearly connected minima (in adapter space), unlike full fine-tuning.
- **Problem:** PEFT's restricted parameterization may qualitatively change solution-space geometry, affecting ensembling and merging, but this is unmapped.
- **Hypothesis:** LoRA solutions for the same vision task are linearly mode-connected (no loss barrier) at far higher rates than full fine-tuning solutions, explaining why adapter averaging works.
- **Why Important:** Provides the geometric foundation for adapter arithmetic practices currently used blindly.
- **Why Possibly Novel (hypothesized):** Mode-connectivity analysis specifically in adapter subspaces for vision tasks appears new.
- **Minimal Experiment:** Train 10 seeds of LoRA and full FT on 3 segmentation tasks; measure loss barriers on linear paths; compare connectivity rates.
- **Main Risk:** Connectivity may trivially follow from low dimensionality, reducing novelty of the finding.
- **Cluster:** `peft-mechanics`

### A-0096
- **Idea:** Test whether PEFT under-trains "new physics" while over-fitting "new style": decomposing adaptation gains on domains that differ from pretraining in sensor physics vs. mere appearance statistics.
- **Problem:** PEFT's low capacity must allocate between qualitatively different kinds of domain novelty; its implicit allocation is unknown.
- **Hypothesis:** At fixed rank, PEFT closes style gaps (color/texture statistics) nearly fully but physics gaps (SAR speckle, ultrasound artifacts) only fractionally, and the gap ratio is rank-dependent in a characteristic way.
- **Why Important:** Tells practitioners which domain types genuinely need higher-capacity adaptation.
- **Why Possibly Novel (hypothesized):** Style-vs-physics decomposition of PEFT capacity allocation appears unstudied.
- **Minimal Experiment:** Build matched adaptation tasks (style-shifted natural images vs. SAR/ultrasound) with equal headroom; sweep ranks; compare gap-closure curves.
- **Main Risk:** "Equal headroom" matching across domain types is difficult to construct.
- **Cluster:** `peft-mechanics`

### A-0097
- **Idea:** Study gradient-flow bottlenecks in frozen-backbone PEFT: whether adaptation quality is limited by which layers gradients must traverse frozen, and whether inserting zero-init "gradient taps" (adapters used only for backward flow) helps.
- **Problem:** In PEFT, gradients to early adapters flow through frozen middle layers; whether this attenuates useful signal is unexamined.
- **Hypothesis:** Gradient norm attenuation through frozen blocks predicts per-layer adapter utility, and auxiliary gradient paths improve early-adapter effectiveness without adding inference cost.
- **Why Important:** Could unlock early-layer adaptation (needed for sensor-level shifts) within PEFT budgets.
- **Why Possibly Novel (hypothesized):** Backward-path engineering for vision PEFT appears unexplored.
- **Minimal Experiment:** Measure per-layer gradient statistics during LoRA training; correlate with per-layer adapter gains; test train-time-only auxiliary paths.
- **Main Risk:** Gradient attenuation may not be the binding constraint versus feature suitability.
- **Cluster:** `peft-mechanics`

### A-0098
- **Idea:** Ask whether PEFT changes what the model attends to or how it decodes: decomposing LoRA-induced behavioral change into attention-pattern change vs. value/readout change, per task.
- **Problem:** We lack a mechanistic taxonomy of what adaptation actually modifies inside vision transformers.
- **Hypothesis:** Domain adaptation predominantly alters value/readout pathways (attention maps stay stable), while task-type changes (segmentation→depth) require attention-pattern changes — a dichotomy testable by constrained PEFT variants.
- **Why Important:** Mechanism-aware PEFT could restrict updates to the pathway that matters, improving efficiency and safety.
- **Why Possibly Novel (hypothesized):** Attention-vs-value decomposition of vision PEFT effects appears novel.
- **Minimal Experiment:** Train LoRA constrained to QK (attention-only) vs. VO (value-only) on domain-shift and task-shift settings; compare gains and attention-map drift.
- **Main Risk:** QK/VO constraints entangle with optimization difficulty, confounding interpretation.
- **Cluster:** `peft-mechanics`

### A-0099
- **Idea:** Test the data-scaling behavior of PEFT vs. full fine-tuning at the low-data frontier: whether PEFT's advantage at small n comes from implicit regularization or from preserving pretrained feature geometry, distinguishable by feature-space analysis.
- **Problem:** "PEFT is better with little data" is accepted without a mechanism, blocking principled method choice.
- **Hypothesis:** PEFT's low-data advantage tracks preservation of pretrained feature neighborhoods (measured by k-NN overlap before/after tuning), not weight-space regularization strength, and disappears when full FT is constrained to preserve neighborhoods.
- **Why Important:** Identifies the operative mechanism, enabling better methods than either extreme.
- **Why Possibly Novel (hypothesized):** Mechanistic dissection of the PEFT low-data advantage in vision appears missing.
- **Minimal Experiment:** Sweep data sizes for LoRA, full FT, and neighborhood-regularized full FT on segmentation tasks; correlate advantage with feature-geometry preservation.
- **Main Risk:** Neighborhood-preserving full FT may be hard to implement cleanly.
- **Cluster:** `peft-mechanics`

### A-0100
- **Idea:** Investigate whether task vectors (weight deltas) from PEFT on vision tasks compose arithmetically across model scales: can an adapter trained on a small backbone be "up-mapped" to a larger backbone without retraining?
- **Problem:** Adapters must be retrained per backbone size, wasting compute; whether adaptation knowledge is scale-portable is unknown.
- **Hypothesis:** A linear map between small- and large-backbone feature spaces (fit once on unlabeled data) transports LoRA updates with ≥60% of retrained-adapter performance, indicating scale-invariant structure in adaptation directions.
- **Why Important:** Adapter portability would decouple adaptation cost from backbone growth.
- **Why Possibly Novel (hypothesized):** Cross-scale adapter transport for vision models appears untried.
- **Minimal Experiment:** Fit feature-space alignment between ViT-B and ViT-L; transport adapters for 5 tasks; compare against retrained adapters and zero-shot.
- **Main Risk:** Layer correspondence across scales is ill-defined.
- **Cluster:** `peft-mechanics`

### A-0101
- **Idea:** Study PEFT stability under prompt distribution shift: adapters tuned with box prompts may silently degrade point-prompt behavior, quantifying cross-prompt-type collateral damage of PEFT on promptable models.
- **Problem:** Fine-tuning datasets typically use one prompt type; effects on other prompt types are unmeasured collateral.
- **Hypothesis:** Box-only fine-tuning degrades point-prompt IoU by a measurable margin even on in-domain data, and mixed-prompt tuning at a small mixing ratio eliminates the damage without diluting target gains.
- **Why Important:** Protects the general-purpose promptability that makes these models useful, during specialization.
- **Why Possibly Novel (hypothesized):** Cross-prompt-type collateral analysis of PEFT appears unreported.
- **Minimal Experiment:** LoRA-tune with box-only, point-only, mixed prompts on 3 domains; evaluate all prompt types before/after; find minimal protective mixing ratio.
- **Main Risk:** Effect sizes may be small for shallow adaptation.
- **Cluster:** `peft-mechanics`

### A-0102
- **Idea:** Test whether normalization-layer-only tuning (bias/scale) exploits a different adaptation mechanism than LoRA — feature re-weighting vs. feature re-mixing — with different failure profiles under distribution shift.
- **Problem:** Multiple cheap PEFT families exist, but whether they are interchangeable or mechanistically complementary is unclear.
- **Hypothesis:** Norm-tuning and LoRA gains are partially non-overlapping (combined > either alone by more than additivity predicts on shifted data), because re-weighting corrects first-order statistics while re-mixing corrects feature correlations.
- **Why Important:** A mechanistic complementarity result would justify hybrid PEFT design rather than method monoculture.
- **Why Possibly Novel (hypothesized):** Mechanistic complementarity testing between PEFT families in vision appears absent.
- **Minimal Experiment:** Tune norm-only, LoRA-only, and both on matched budgets across shift types; analyze which feature statistics each corrects.
- **Main Risk:** Budget matching across method families is nontrivial.
- **Cluster:** `peft-mechanics`

### A-0103
- **Idea:** Investigate "adaptation shortcuts": whether PEFT preferentially learns dataset-specific shortcuts (annotation style, class priors) before genuine visual features, and whether the learning-order signature can flag shortcut-dominated adaptation early.
- **Problem:** Low-capacity adaptation may amplify shortcut learning, but the temporal order of what PEFT learns is unobserved.
- **Hypothesis:** Under LoRA, shortcut-aligned performance (on probe sets isolating annotation style/priors) rises earlier in training than genuine-feature performance, and the gap at 10% of training predicts final OOD degradation.
- **Why Important:** An early-warning signal for shortcut adaptation would save wasted fine-tunes and unsafe deployments.
- **Why Possibly Novel (hypothesized):** Learning-order analysis of shortcuts specifically under PEFT appears new.
- **Minimal Experiment:** Construct probe sets separating shortcut vs. genuine cues for 4 datasets; log both curves during tuning; validate the early predictor on held-out runs.
- **Main Risk:** Constructing clean shortcut probes is dataset-specific and laborious.
- **Cluster:** `peft-mechanics`

### A-0104
- **Idea:** Ask whether PEFT can adapt a model's inductive biases (not just its features): e.g., tuning a ViT-based SAM to acquire scale equivariance for aerial imagery through adapter design alone, testing the limits of bias injection via low-rank updates.
- **Problem:** It is unknown whether structural inductive biases are reachable within low-rank update families or require architectural change.
- **Hypothesis:** Scale-equivariance error on aerial imagery cannot be reduced below a floor by any rank-r LoRA (floor decreasing slowly with r), while a tiny equivariant module achieves it immediately — establishing a bias-reachability boundary for PEFT.
- **Why Important:** Defines what PEFT fundamentally cannot fix, preventing wasted adaptation effort.
- **Why Possibly Novel (hypothesized):** Reachability limits of inductive biases under low-rank adaptation appear unformalized.
- **Minimal Experiment:** Measure scale-consistency error across LoRA ranks vs. an equivariant baseline on aerial data with controlled scale factors.
- **Main Risk:** Negative results across ranks require careful optimization to be convincing.
- **Cluster:** `peft-mechanics`

### A-0105
- **Idea:** Test whether the best PEFT configuration is predictable from a cheap "fingerprint" of the target dataset (feature-shift statistics, label granularity, prompt type), learned across many adaptation runs as a meta-regression.
- **Problem:** Every adaptation project re-runs hyperparameter searches; cross-project regularities remain unexploited.
- **Hypothesis:** A meta-model trained on ~100 logged adaptation runs predicts near-optimal PEFT configuration (method, rank, placement, LR) for unseen datasets, retaining ≥90% of exhaustive-search performance at 5% of the cost.
- **Why Important:** Amortized PEFT configuration would change adaptation practice economically.
- **Why Possibly Novel (hypothesized):** Meta-learning PEFT configuration from dataset fingerprints for vision appears unbuilt.
- **Minimal Experiment:** Run a config grid across 25 diverse segmentation adaptations; fit the meta-regressor; validate on 5 held-out datasets.
- **Main Risk:** 25 datasets may under-sample the adaptation-problem space.
- **Cluster:** `peft-mechanics`

---

## Sub-cluster 8: PEFT & catastrophic forgetting (`peft-forgetting`)

### A-0106
- **Idea:** Quantify "zero-shot erosion" during SAM fine-tuning: the decay curve of general promptable ability as a function of fine-tuning steps on a narrow domain, and identify the erosion-onset predictor.
- **Problem:** Fine-tuned SAMs lose generality, but the erosion dynamics (onset, rate, which capabilities first) are uncharted.
- **Hypothesis:** Zero-shot erosion begins after a characteristic optimization phase transition (detectable by weight-update alignment shifting from decoder to encoder-adapter dominated), providing an early stopping signal that preserves generality at minimal target-task cost.
- **Why Important:** Practitioners need a principled stopping rule to keep one checkpoint serving both narrow and general use.
- **Why Possibly Novel (hypothesized):** Erosion-onset detection via optimization-phase signatures appears new.
- **Minimal Experiment:** Fine-tune SAM on 4 narrow domains; checkpoint densely; track zero-shot suites and update-alignment statistics; test the predictor.
- **Main Risk:** The phase transition may not exist or may be dataset-specific.
- **Cluster:** `peft-forgetting`

### A-0107
- **Idea:** Test whether forgetting under PEFT is primarily an output-head phenomenon in promptable models: general capability persists in features but becomes unreadable by the shifted decoder, recoverable by decoder-only reset.
- **Problem:** "Forgetting" conflates feature destruction with readout misalignment; the distinction dictates the cure.
- **Hypothesis:** After domain PEFT, restoring only the original decoder recovers ≥70% of lost zero-shot performance while retaining ≥80% of domain gains, showing forgetting is mostly readout-level at low ranks.
- **Why Important:** If forgetting is readout-level, dual-decoder deployment trivially solves it — no continual-learning machinery needed.
- **Why Possibly Novel (hypothesized):** Feature-vs-readout forgetting decomposition for promptable segmentation appears untested.
- **Minimal Experiment:** After PEFT on 5 domains, evaluate all four combinations of {original, tuned} × {encoder-adapters, decoder}; build the recovery matrix.
- **Main Risk:** Encoder-adapter and decoder changes may be co-adapted, making swaps incoherent.
- **Cluster:** `peft-forgetting`

### A-0108
- **Idea:** Study forgetting asymmetry across capability types: whether fine-tuning erodes ambiguity handling faster than average IoU, making "still looks fine" checkpoints subtly broken for interactive use.
- **Problem:** Forgetting is monitored via headline metrics; capability-selective erosion would evade detection.
- **Hypothesis:** Multimask ambiguity quality degrades 2–3× faster (per fine-tuning step) than single-mask IoU, because narrow-domain data is ambiguity-poor and the multimask head unlearns first.
- **Why Important:** Defines what must be monitored during fine-tuning to certify continued fitness for interactive products.
- **Why Possibly Novel (hypothesized):** Capability-resolved forgetting-rate measurement appears new for segmentation.
- **Minimal Experiment:** Fine-tune on single-mask medical data; track ambiguity benchmarks vs. IoU benchmarks per checkpoint; compare decay constants.
- **Main Risk:** Ambiguity benchmarks are less mature, adding measurement noise.
- **Cluster:** `peft-forgetting`

### A-0109
- **Idea:** Test "forgetting-free rank" existence: whether for each adaptation there is a maximal LoRA rank below which zero-shot performance is provably (empirically) preserved, and how this budget relates to target-task headroom.
- **Problem:** The rank-forgetting relationship is assumed monotone but its structure (threshold vs. gradual) is unmeasured.
- **Hypothesis:** Forgetting exhibits a rank threshold (sharp onset) rather than gradual growth, and the threshold correlates with the overlap between target-task gradients and the pretraining-dominant weight subspace.
- **Why Important:** A computable safe-rank budget would make no-forgetting adaptation a checkbox rather than a research problem.
- **Why Possibly Novel (hypothesized):** Threshold characterization of rank-vs-forgetting appears unexplored.
- **Minimal Experiment:** Sweep ranks (1–256) across 6 adaptations; locate forgetting onsets; test correlation with gradient-subspace overlap measured cheaply upfront.
- **Main Risk:** Thresholds may be optimizer/LR-dependent, complicating a clean law.
- **Cluster:** `peft-forgetting`

### A-0110
- **Idea:** Investigate whether interleaving a tiny fraction of "self-generated pretraining-proxy" data (SAM's own outputs on diverse unlabeled images) during PEFT prevents forgetting as well as true pretraining data, which is often unavailable.
- **Problem:** Rehearsal needs pretraining data that users don't have; whether self-distilled proxies suffice is a practical open question.
- **Hypothesis:** Rehearsing on the model's own frozen-checkpoint outputs (5% mixing) recovers ≥90% of the anti-forgetting benefit of true pretraining-data rehearsal across domains.
- **Why Important:** Makes forgetting mitigation accessible to everyone without SA-1B access.
- **Why Possibly Novel (hypothesized):** Self-output rehearsal specifically for promptable segmentation PEFT appears unassessed.
- **Minimal Experiment:** Compare no-rehearsal, true-data rehearsal, and self-output rehearsal at matched mixing ratios on 4 adaptations; measure zero-shot retention and target gains.
- **Main Risk:** Self-outputs encode model errors, possibly entrenching them (confirmation bias).
- **Cluster:** `peft-forgetting`

### A-0111
- **Idea:** Characterize sequential-adaptation orderings: whether adapting to domains in "increasing shift distance" order yields less total forgetting than the reverse, establishing curriculum effects in continual PEFT.
- **Problem:** Practitioners adapt models to a sequence of domains in arbitrary order; order effects on cumulative forgetting are unquantified.
- **Hypothesis:** Near-to-far ordering (natural→aerial→medical) preserves more aggregate performance than far-to-near, because early small updates establish reusable directions that later updates refine rather than overwrite.
- **Why Important:** Free performance from reordering — no new algorithms needed.
- **Why Possibly Novel (hypothesized):** Order-effect studies for sequential vision PEFT appear sparse.
- **Minimal Experiment:** Run all 6 orderings of 3 domains (plus 2 longer sequences) with fixed budgets; measure final all-domain performance matrices.
- **Main Risk:** Order effects may be dwarfed by budget and LR effects.
- **Cluster:** `peft-forgetting`

### A-0112
- **Idea:** Test whether forgetting during vision PEFT is spatially selective in weight space: concentrated in identifiable "plasticity hotspots" (specific heads/blocks) whose freezing eliminates most forgetting at minor target-task cost.
- **Problem:** Forgetting mitigation applies uniform penalties; if damage is localized, surgical protection would be cheaper and better.
- **Hypothesis:** >70% of zero-shot degradation is attributable to updates in <10% of adapted parameters (identifiable by influence-style attribution), and masking those parameters during tuning retains generality with <10% target-gain loss.
- **Why Important:** Turns anti-forgetting from a global constraint into targeted parameter hygiene.
- **Why Possibly Novel (hypothesized):** Hotspot attribution and masking for vision PEFT forgetting appears untried.
- **Minimal Experiment:** Attribute zero-shot loss to parameter groups via ablation/influence; retrain with hotspot masks; verify the retention/gain trade-off.
- **Main Risk:** Attribution instability; hotspots may shift when masked (whack-a-mole).
- **Cluster:** `peft-forgetting`

### A-0113
- **Idea:** Study cross-modal forgetting in multimodal PEFT: fine-tuning the vision tower of a vision-language model for segmentation may silently damage text-vision alignment, measurable only through multimodal (not vision-only) probes.
- **Problem:** Vision-side adaptation is validated on vision metrics, leaving alignment damage undetected until multimodal deployment fails.
- **Hypothesis:** Vision-tower PEFT that improves segmentation degrades retrieval/grounding alignment measurably even when linear-probe vision quality is unchanged, and alignment damage correlates with update magnitude in late vision blocks feeding the shared space.
- **Why Important:** Multimodal models are adapted vision-first routinely; invisible alignment damage is a deployment hazard.
- **Why Possibly Novel (hypothesized):** Alignment-forgetting under vision-only PEFT appears unmeasured.
- **Minimal Experiment:** LoRA-tune the vision tower of an open VLM for segmentation; track retrieval, grounding, and VQA probes across checkpoints; localize damaging layers.
- **Main Risk:** Alignment metrics vary across probe tasks, complicating a unified conclusion.
- **Cluster:** `peft-forgetting`

### A-0114
- **Idea:** Ask whether forgetting is dominated by loss-function mismatch rather than data distribution: fine-tuning SAM with a different loss (e.g., Dice instead of its pretraining mix) may itself erode calibration/generality even on distribution-matched data.
- **Problem:** Data shift and objective shift are conflated in every fine-tuning study; their separate contributions to forgetting are unknown.
- **Hypothesis:** Objective shift alone (same-distribution data, different loss) accounts for a substantial share of calibration erosion and multimask degradation, isolable by fine-tuning on pretraining-like data with altered losses.
- **Why Important:** If the objective drives forgetting, loss-matching (not data rehearsal) is the cheap fix.
- **Why Possibly Novel (hypothesized):** Objective-shift-only forgetting isolation appears undone for segmentation.
- **Minimal Experiment:** Fine-tune on SA-1B-like data under 4 losses; measure generality/calibration erosion with data held fixed; compare against domain-shift-induced erosion.
- **Main Risk:** "Pretraining-like" data approximation may be imperfect.
- **Cluster:** `peft-forgetting`

### A-0115
- **Idea:** Test task-vector negation as forgetting repair: whether subtracting a scaled adaptation vector post hoc restores generality on demand, enabling a single checkpoint to be "dialed" between specialist and generalist modes at inference.
- **Problem:** Users must currently keep multiple checkpoints; continuous interpolation between specialist and generalist behavior is unvalidated for promptable segmentation.
- **Hypothesis:** Performance on target and zero-shot suites varies smoothly and monotonically along the adaptation-vector scaling axis, with a Pareto-optimal dial setting outperforming both endpoints on mixed workloads.
- **Why Important:** Dialable specialization simplifies deployment and quantifies the specialist-generalist trade-off cleanly.
- **Why Possibly Novel (hypothesized):** Adaptation-dial characterization for SAM-family models appears unreported.
- **Minimal Experiment:** Sweep interpolation coefficients on 5 adapted checkpoints; plot target-vs-zero-shot trade-off curves; test mixed-workload optima.
- **Main Risk:** Non-monotonic interpolation behavior would break the dial concept.
- **Cluster:** `peft-forgetting`

### A-0116
- **Idea:** Investigate forgetting through the lens of prompt-space coverage: fine-tuning with a narrow prompt distribution (tight boxes only) may cause "prompt-space forgetting" — degraded behavior on prompt regions unused during tuning — independent of image-domain effects.
- **Problem:** Forgetting is framed as image-distribution shift; prompt-distribution shift is an unstudied second axis.
- **Hypothesis:** Models fine-tuned with narrow prompt distributions degrade on held-out prompt regions (loose boxes, multi-point) even on the tuning images themselves, demonstrating prompt-space forgetting as a distinct phenomenon.
- **Why Important:** Reveals a hidden dimension of fine-tuning hygiene specific to promptable architectures.
- **Why Possibly Novel (hypothesized):** Prompt-space forgetting as a concept appears unintroduced.
- **Minimal Experiment:** Fine-tune with restricted prompt families; evaluate the full prompt battery on tuning-domain images; map degradation across prompt space.
- **Main Risk:** Prompt-space effects may be small relative to image-domain effects.
- **Cluster:** `peft-forgetting`

### A-0117
- **Idea:** Study whether elastic-consolidation penalties transfer to adapter space: is penalizing adapter-parameter movement (relative to their own trajectory) effective, or does forgetting in PEFT require function-space (output-level) constraints?
- **Problem:** Classic anti-forgetting regularizers were designed for full fine-tuning; their validity within low-rank subspaces is untested.
- **Hypothesis:** Weight-space penalties on adapters are near-ineffective (adapter weights are non-identifiable), while function-space distillation on held-out images prevents forgetting at equal compute — a qualitative difference from full fine-tuning behavior.
- **Why Important:** Prevents cargo-culting continual-learning methods into PEFT where their assumptions fail.
- **Why Possibly Novel (hypothesized):** Systematic weight-vs-function-space regularization comparison inside PEFT appears missing.
- **Minimal Experiment:** Compare EWC-style adapter penalties vs. output distillation on sequential segmentation adaptations at matched budgets.
- **Main Risk:** Result may depend on adapter parameterization details.
- **Cluster:** `peft-forgetting`

### A-0118
- **Idea:** Test whether "forgetting" reported in fine-tuned VFMs is partially benchmark contamination artifact: zero-shot suites overlapping pretraining data make erosion look worse (or better) than true generalization change.
- **Problem:** Zero-shot retention is measured on public benchmarks likely seen during pretraining, biasing forgetting estimates in unknown directions.
- **Hypothesis:** Forgetting magnitude measured on likely-contaminated benchmarks differs systematically from that on verified-novel data (post-training-date imagery), and the sign of the bias is predictable from memorization strength.
- **Why Important:** Correct forgetting measurement underlies the entire continual-learning-for-VFM literature.
- **Why Possibly Novel (hypothesized):** Contamination-controlled forgetting measurement appears absent.
- **Minimal Experiment:** Assemble post-cutoff test imagery; compare fine-tuning-induced deltas on contaminated vs. novel suites for the same capabilities.
- **Main Risk:** Verifying non-contamination is hard without training-data access.
- **Cluster:** `peft-forgetting`

### A-0119
- **Idea:** Investigate "dormant capability revival": whether capabilities apparently lost to fine-tuning can be revived by prompt engineering alone (specific prompt patterns re-eliciting pretrained behavior), indicating suppression rather than erasure.
- **Problem:** The erasure-vs-suppression nature of forgetting in vision models determines whether recovery needs retraining.
- **Hypothesis:** For a substantial fraction of forgotten cases, there exist prompt configurations (multi-point patterns, box framings) that recover pre-fine-tuning outputs, proving the capability is suppressed, not erased — analogous to jailbreaking but for capability recovery.
- **Why Important:** Suppression implies cheap recovery mechanisms and reframes forgetting as a routing problem.
- **Why Possibly Novel (hypothesized):** Prompt-based capability revival in vision fine-tuning appears untested.
- **Minimal Experiment:** Collect post-fine-tuning failures that pre-fine-tuning succeeded on; search prompt space per case; measure revival rate and pattern regularities.
- **Main Risk:** Prompt search may overfit per-case noise rather than reveal systematic revival.
- **Cluster:** `peft-forgetting`

### A-0120
- **Idea:** Test population-level forgetting laws: aggregating hundreds of community fine-tunes of SAM (public checkpoints) to fit an empirical law relating adaptation dataset properties to zero-shot erosion, treating the ecosystem as a natural experiment.
- **Problem:** Individual studies cannot map the forgetting landscape; the public checkpoint ecosystem is an unused observational dataset.
- **Hypothesis:** Across community checkpoints, zero-shot erosion follows a predictable function of adaptation-domain distance and update norm, robust enough to forecast erosion of new fine-tunes within ±15%.
- **Why Important:** An empirical forgetting law would let practitioners predict costs before training and standardize reporting.
- **Why Possibly Novel (hypothesized):** Observational meta-analysis of forgetting across public vision checkpoints appears undone.
- **Minimal Experiment:** Harvest 100+ public SAM fine-tunes; run a fixed zero-shot battery; fit and cross-validate the erosion law against checkpoint metadata.
- **Main Risk:** Public checkpoints have inconsistent provenance/documentation, adding noise.
- **Cluster:** `peft-forgetting`

---

## Sub-cluster 9: Calibration & uncertainty (`calibration-uncertainty`)

### A-0121
- **Idea:** Test whether SAM's predicted-IoU head is calibrated conditionally: globally decent calibration may hide severe miscalibration conditioned on object category, size, or prompt type — the regimes where decisions are made.
- **Problem:** The IoU head is used as a quality gate, but conditional calibration (where gating actually operates) is unverified.
- **Hypothesis:** Conditional expected calibration error stratified by object size is >3× the marginal ECE, with systematic overconfidence on small objects, making size-blind gating unsafe.
- **Why Important:** Every auto-filtering pipeline built on the IoU head inherits these conditional biases.
- **Why Possibly Novel (hypothesized):** Conditional (stratified) calibration audits of the IoU head appear missing.
- **Minimal Experiment:** Compute reliability diagrams stratified by size/category/prompt-type on 5 datasets; quantify conditional-vs-marginal ECE ratios.
- **Main Risk:** Stratified bins may lack samples; needs large evaluation corpora.
- **Cluster:** `calibration-uncertainty`

### A-0122
- **Idea:** Investigate pixelwise mask-logit calibration as spatial fields: whether miscalibration has consistent spatial structure (overconfident interiors, underconfident boundaries) that a spatially-aware recalibration map fixes better than global temperature.
- **Problem:** Temperature scaling treats all pixels identically, but segmentation confidence errors are plausibly spatially structured.
- **Hypothesis:** A single distance-to-boundary-conditioned recalibration function (fit once per model) reduces pixelwise ECE by ≥50% relative to global temperature across datasets, revealing spatially universal miscalibration structure.
- **Why Important:** Calibrated pixel confidences enable principled downstream fusion, active correction, and risk maps.
- **Why Possibly Novel (hypothesized):** Distance-conditioned universal recalibration for promptable masks appears new.
- **Minimal Experiment:** Fit boundary-distance-binned recalibration on one dataset; test transfer of the same function across 6 datasets vs. per-dataset temperature.
- **Main Risk:** The structure may be dataset-dependent, breaking universality.
- **Cluster:** `calibration-uncertainty`

### A-0123
- **Idea:** Study whether prompt-ensemble variance is a fundamentally different uncertainty type than weight-ensemble variance in promptable models, capturing prompt-interpretation ambiguity vs. model uncertainty — and whether they are additive predictors of error.
- **Problem:** Uncertainty sources in promptable models are conflated; the unique information in prompt-space uncertainty is unquantified.
- **Hypothesis:** Prompt-ensemble and dropout-ensemble variances are weakly correlated (r<0.4) and each independently predicts distinct error types (ambiguity errors vs. domain-shift errors), so their combination dominates either alone for failure prediction.
- **Why Important:** Correct uncertainty taxonomy determines which cheap estimator suffices per application.
- **Why Possibly Novel (hypothesized):** A decomposition treating the prompt as an uncertainty source appears unformalized.
- **Minimal Experiment:** Compute both variances on 10k cases with error-type labels; fit predictive models per error type; test additivity.
- **Main Risk:** Error-type labeling is subjective and labor-intensive.
- **Cluster:** `calibration-uncertainty`

### A-0124
- **Idea:** Test conformal prediction for masks: constructing distribution-free confidence regions (inner/outer mask bounds) with guaranteed coverage, and measuring how loose the bounds must be for SAM-class models in vs. out of domain.
- **Problem:** Set-valued guarantees exist for classification, but calibrated inner/outer mask bounds with finite-sample guarantees are rarely deployed for promptable segmentation.
- **Hypothesis:** Conformalized morphological bounds (erode/dilate calibrated on residual quantiles) achieve target coverage with informative (non-trivial) width in-domain, but the required width explodes disproportionately under domain shift — quantifying guarantee costs honestly.
- **Why Important:** Downstream consumers (surgery planning, mapping) need coverage guarantees, not point masks.
- **Why Possibly Novel (hypothesized):** Systematic width-vs-shift analysis for conformal segmentation on VFMs appears sparse.
- **Minimal Experiment:** Calibrate morphological conformal bounds on one domain; evaluate coverage/width in-domain and across 4 shifted domains.
- **Main Risk:** Morphological score functions may be poorly matched to error structure, inflating widths.
- **Cluster:** `calibration-uncertainty`

### A-0125
- **Idea:** Ask whether the multimask scores of SAM constitute a calibrated distribution over interpretations: does the score vector's implied probability of "which mask a human would choose" match empirical human choice frequencies?
- **Problem:** Multimask scores rank hypotheses, but whether they are choice-calibrated against human interpretation distributions is unknown.
- **Hypothesis:** SAM's softmaxed mask scores misestimate human choice frequencies with systematic bias toward larger masks, and a monotone recalibration fixes downstream ambiguity-resolution accuracy without retraining.
- **Why Important:** Interpretation-calibrated scores would let systems defer correctly on genuinely ambiguous prompts.
- **Why Possibly Novel (hypothesized):** Human-choice calibration of multimask outputs appears unmeasured.
- **Minimal Experiment:** Collect human mask-choice frequencies on 500 ambiguous prompts; compare to score-implied distributions; fit and validate recalibration.
- **Main Risk:** Human choices depend on task framing, adding variance.
- **Cluster:** `calibration-uncertainty`

### A-0126
- **Idea:** Investigate calibration transfer under PEFT: whether fine-tuning that improves accuracy systematically destroys calibration, and whether calibration can be preserved by a small "calibration rehearsal" loss at negligible accuracy cost.
- **Problem:** Adaptation studies report accuracy; the calibration cost of adaptation is largely unmeasured for segmentation.
- **Hypothesis:** Standard PEFT increases confidence faster than accuracy (growing overconfidence), and a proper-scoring-rule term on 1% held-out data eliminates the calibration damage without measurable accuracy loss.
- **Why Important:** Deployed thresholds silently break when calibration shifts under adaptation.
- **Why Possibly Novel (hypothesized):** Calibration-preserving PEFT for segmentation appears unstudied.
- **Minimal Experiment:** Track ECE and accuracy across PEFT checkpoints on 5 adaptations, with and without the calibration term.
- **Main Risk:** Effect sizes may vary with loss choice, requiring several baselines.
- **Cluster:** `calibration-uncertainty`

### A-0127
- **Idea:** Test whether uncertainty communicated as "second-best hypothesis" (showing the alternative mask) beats scalar confidence for human decision quality in verification workflows — an uncertainty-representation question, not an estimation one.
- **Problem:** Uncertainty research optimizes estimators, but how uncertainty should be represented to human verifiers is untested for segmentation.
- **Hypothesis:** Verifiers shown the top-2 masks catch more true errors per unit time than verifiers shown heatmaps or scalar scores, because alternatives direct attention to decision-relevant regions.
- **Why Important:** Human-AI verification throughput is the practical bottleneck of auto-annotation economics.
- **Why Possibly Novel (hypothesized):** Uncertainty-representation trials for segmentation verification appear rare.
- **Minimal Experiment:** Within-subject user study (n≈20) verifying masks under 3 uncertainty displays; measure error-catch rate and time.
- **Main Risk:** User-study effects may be small relative to individual variance.
- **Cluster:** `calibration-uncertainty`

### A-0128
- **Idea:** Study "confidence collapse under iterative prompting": whether SAM's confidence monotonically increases with more clicks even when accuracy stagnates, creating dangerous certainty at interaction dead-ends.
- **Problem:** Interactive loops read confidence to decide when to stop; if confidence inflates with interaction count independent of accuracy, stopping rules are broken.
- **Hypothesis:** Predicted IoU increases with click count roughly linearly even on objects where true IoU has plateaued, and the inflation rate is a stable model constant correctable post hoc.
- **Why Important:** Fixes stopping criteria in every interactive annotation deployment.
- **Why Possibly Novel (hypothesized):** Interaction-count-conditioned confidence auditing appears new.
- **Minimal Experiment:** Run scripted 10-click sessions on 2k objects; regress predicted and true IoU on click index; quantify divergence.
- **Main Risk:** Scripted clicks may not reproduce human interaction statistics.
- **Cluster:** `calibration-uncertainty`

### A-0129
- **Idea:** Investigate whether epistemic uncertainty in VFMs can be read from feature-space density (distance to pretraining feature manifold) without any ensembling, validated against actual error on novel domains.
- **Problem:** Ensembles are expensive; a single-pass epistemic signal from the frozen encoder would be widely useful if valid.
- **Hypothesis:** A density model over encoder features (fit on generic unlabeled data) predicts domain-shift-induced errors with AUROC within 0.05 of deep ensembles at <5% of the cost, but fails specifically on adversarial and near-manifold shifts.
- **Why Important:** Cheap epistemic signals determine deployability of VFMs in safety-relevant pipelines.
- **Why Possibly Novel (hypothesized):** Rigorous manifold-density-vs-ensemble comparison for promptable segmentation appears missing.
- **Minimal Experiment:** Fit normalizing-flow/k-NN density on SAM features; evaluate failure prediction across 8 shifted datasets against ensembles.
- **Main Risk:** Density estimation quality in 1024-d feature spaces.
- **Cluster:** `calibration-uncertainty`

### A-0130
- **Idea:** Test the "calibration inheritance" of downstream heads: whether heads trained on frozen VFM features inherit the encoder's confidence pathologies, implying calibration debt propagates through the ecosystem.
- **Problem:** Many products build small heads on frozen VFM features, assuming calibration is head-local — an untested assumption.
- **Hypothesis:** Heads trained on features from a miscalibrated encoder reproduce the encoder's error-confidence correlation structure even with calibrated training labels, and feature whitening reduces the inheritance.
- **Why Important:** Identifies whether ecosystem-wide calibration problems must be fixed at the foundation or can be fixed per-application.
- **Why Possibly Novel (hypothesized):** Calibration-propagation-through-features analysis appears unexamined.
- **Minimal Experiment:** Train matched heads on features from encoders with induced calibration differences; compare downstream reliability diagrams.
- **Main Risk:** Constructing encoders differing only in calibration is nontrivial.
- **Cluster:** `calibration-uncertainty`

### A-0131
- **Idea:** Study selective-prediction curves as the primary model-comparison tool: whether VFM rankings change when compared at matched coverage (fraction of cases attempted) rather than full coverage, revealing "risk-adjusted" model quality.
- **Problem:** Model A may beat B on average but lose badly at the high-confidence operating points where deployments actually run.
- **Hypothesis:** Model rankings on segmentation suites change for a substantial fraction of model pairs when evaluated at 80% coverage with each model's own confidence, making full-coverage leaderboards misleading for deployment choice.
- **Why Important:** Aligns evaluation with how models are actually operated (with rejection).
- **Why Possibly Novel (hypothesized):** Coverage-conditioned leaderboard analysis for segmentation VFMs appears rare.
- **Minimal Experiment:** Recompute pairwise rankings of 8 models at multiple coverage levels across suites; count rank inversions vs. full coverage.
- **Main Risk:** Depends on each model exposing a usable confidence — heterogeneity complicates fairness.
- **Cluster:** `calibration-uncertainty`

### A-0132
- **Idea:** Ask whether aleatoric-uncertainty ground truth can be constructed from annotation multiplicity, then test if any current segmentation uncertainty estimator actually predicts it rather than predicting model error.
- **Problem:** "Aleatoric" estimators are validated against model error, not against measured irreducible ambiguity — a category mistake.
- **Hypothesis:** Existing estimators correlate more with model error than with multi-annotator entropy (the true aleatoric target), failing the definitional test; a estimator trained explicitly on annotator entropy transfers better across models.
- **Why Important:** Correctly separating error prediction from ambiguity estimation is foundational for downstream decision theory.
- **Why Possibly Novel (hypothesized):** Definitional validation of aleatoric estimators against annotator distributions appears missing for segmentation.
- **Minimal Experiment:** Use multi-annotator datasets; correlate estimator outputs with annotator entropy vs. model error; train an entropy-supervised estimator and test cross-model transfer.
- **Main Risk:** Annotator entropy confounds ambiguity with annotator skill variance.
- **Cluster:** `calibration-uncertainty`

### A-0133
- **Idea:** Test temporal calibration in video segmentation: whether confidence of SAM2 remains calibrated as tracking progresses, or degrades with time since last prompt, requiring time-conditioned recalibration.
- **Problem:** Video confidence is treated as stationary, but error accumulates with tracking duration while confidence may not.
- **Hypothesis:** Calibration error grows monotonically with frames-since-prompt, and conditioning recalibration on this single variable restores near-uniform calibration across a session.
- **Why Important:** Time-honest confidence enables rational re-prompting schedules in long videos.
- **Why Possibly Novel (hypothesized):** Time-conditioned calibration analysis of tracking confidence appears new.
- **Minimal Experiment:** Bin SAM2 confidence-accuracy pairs by frames-since-prompt across video suites; fit time-conditioned recalibration; validate on held-out videos.
- **Main Risk:** Confounding between time and content difficulty in real videos.
- **Cluster:** `calibration-uncertainty`

### A-0134
- **Idea:** Investigate calibration of "emptiness": how well promptable models express that a prompt hits nothing (background clicks, boxes over texture), and whether an explicit null-mask hypothesis improves pipeline precision.
- **Problem:** Promptable models always return a mask; the absence option is architecturally missing, forcing downstream heuristics.
- **Hypothesis:** Current models' best available null signal (low predicted IoU) is far from calibrated for emptiness detection, and adding a trained null-hypothesis output improves auto-annotation precision substantially at fixed recall.
- **Why Important:** Spurious masks from empty prompts are a top contamination source in automated dataset construction.
- **Why Possibly Novel (hypothesized):** Explicit emptiness calibration for promptable segmentation appears understudied.
- **Minimal Experiment:** Construct empty-prompt benchmarks; evaluate null-detection AUROC of existing signals; fine-tune with a null output token and compare.
- **Main Risk:** Defining "hits nothing" has edge cases (stuff classes, amorphous regions).
- **Cluster:** `calibration-uncertainty`

### A-0135
- **Idea:** Study cross-dataset transferability of recalibration maps: whether a recalibration function fitted on one dataset transfers to others within the same modality, testing if miscalibration is a model property or a data property.
- **Problem:** Recalibration is refit per dataset by default; if miscalibration is model-intrinsic, one map should transfer broadly.
- **Hypothesis:** Recalibration transfer retains ≥80% of ECE reduction within-modality but <30% across modalities, locating miscalibration jointly in model and modality statistics with quantified proportions.
- **Why Important:** Transferable calibration would remove a per-deployment labeled-data requirement.
- **Why Possibly Novel (hypothesized):** A transfer taxonomy for segmentation recalibration appears unbuilt.
- **Minimal Experiment:** Fit recalibration on each of 10 datasets; evaluate the full 10×10 transfer matrix; decompose variance into model/modality/data factors.
- **Main Risk:** Requires consistent GT quality across datasets for fair ECE.
- **Cluster:** `calibration-uncertainty`

---

## Sub-cluster 10: Small & thin objects (`small-thin-objects`)

### A-0136
- **Idea:** Establish the "token-occupancy law" for small-object segmentation: performance as a function of how many ViT tokens the object occupies, testing whether failures begin exactly below 1-token occupancy.
- **Problem:** Small-object failure is described by pixel area, but the mechanistically relevant unit for ViTs is token occupancy — the two diverge across resolutions.
- **Hypothesis:** Segmentation quality collapses when objects occupy <1 token regardless of pixel count (varying input resolution to decouple the two), identifying tokenization, not information, as the binding constraint.
- **Why Important:** Redirects small-object research from generic "attention to small things" to the specific tokenization bottleneck.
- **Why Possibly Novel (hypothesized):** Resolution-decoupled token-occupancy analysis appears untested.
- **Minimal Experiment:** Evaluate the same physical objects at multiple input resolutions spanning the 1-token threshold; plot quality vs. token occupancy vs. pixel area.
- **Main Risk:** Resolution changes alter global context too, confounding the isolation.
- **Cluster:** `small-thin-objects`

### A-0137
- **Idea:** Test whether small-object information survives the encoder but dies in the decoder: probing whether frozen SAM features contain linearly decodable masks for objects the decoder fails on.
- **Problem:** The failure locus for small objects (encoder representation vs. decoder readout) determines the fix, but is unlocalized.
- **Hypothesis:** For a substantial fraction of decoder-failed small objects, a linear probe on encoder features recovers IoU>0.5 masks, proving recoverable information is discarded downstream.
- **Why Important:** If information survives, small-object performance is a readout problem solvable without retraining encoders.
- **Why Possibly Novel (hypothesized):** Probe-based failure localization for small-object segmentation appears fresh.
- **Minimal Experiment:** Collect decoder failures on small objects; train per-dataset linear probes on frozen features; report recoverable fractions by size bin.
- **Main Risk:** Probe capacity choices blur the "information present" criterion.
- **Cluster:** `small-thin-objects`

### A-0138
- **Idea:** Investigate crop-and-zoom as principled inference for small objects: deriving the optimal zoom policy (when and how much to crop) from a model's measured size-response curve rather than heuristics.
- **Problem:** Zooming helps small objects but is applied with fixed heuristics; the policy implied by the model's own scale response is uncomputed.
- **Hypothesis:** A zoom policy that maps each object to the model's empirically optimal scale band (measured once on calibration data) beats fixed-zoom and no-zoom baselines by a significant margin at equal compute, and the optimal band is stable across datasets.
- **Why Important:** Converts a lore-based trick into a calibrated, transferable inference procedure.
- **Why Possibly Novel (hypothesized):** Size-response-derived zoom policies appear unformalized.
- **Minimal Experiment:** Measure IoU vs. rendered-scale curves; implement the derived policy; A/B against heuristics on small-object suites at matched FLOPs.
- **Main Risk:** Context loss from cropping may offset scale gains for context-dependent objects.
- **Cluster:** `small-thin-objects`

### A-0139
- **Idea:** Study thin-structure connectivity as a distinct competency: whether models that segment thin structures with high pixel accuracy still break topological connectivity, and whether connectivity failures cluster at specific curvature/junction motifs.
- **Problem:** Pixel metrics hide topological breaks that destroy downstream utility (vessel graphs, wire routing).
- **Hypothesis:** Connectivity breaks concentrate at high-curvature points and X-junctions (not randomly along structures), implicating specific local ambiguities rather than global capacity — testable via motif-conditioned break rates.
- **Why Important:** Motif-specific failures suggest targeted data augmentation rather than architecture overhaul.
- **Why Possibly Novel (hypothesized):** Motif-conditioned topological failure analysis appears rare.
- **Minimal Experiment:** Extract break locations on vessel/wire datasets; classify local motifs; compare break-rate distributions against motif base rates.
- **Main Risk:** Motif taxonomy subjectivity; annotation of junction types.
- **Cluster:** `small-thin-objects`

### A-0140
- **Idea:** Test whether small-object detection failures in open-vocabulary detectors are recognition failures or localization failures, by decoupling with oracle boxes and oracle labels respectively.
- **Problem:** Small-object AP conflates finding, classifying, and boxing; the dominant failure stage is unidentified per model family.
- **Hypothesis:** For current open-vocab detectors, small-object AP loss decomposes predominantly into proposal-stage misses (localization), with classification-given-box nearly size-invariant — opposite to the pattern in closed-set detectors.
- **Why Important:** Directs small-object work to the correct pipeline stage per model family.
- **Why Possibly Novel (hypothesized):** Stage-decomposed small-object analysis across open-vocab families appears missing.
- **Minimal Experiment:** Run oracle-box and oracle-class ablations on size-stratified LVIS; report per-stage recovery by model family.
- **Main Risk:** Oracle ablations interact; ordering effects need careful design.
- **Cluster:** `small-thin-objects`

### A-0141
- **Idea:** Investigate the effect of training-data size distributions on small-object competence: does oversampling small instances at fixed data volume transfer to unseen categories, or does small-object skill remain category-bound?
- **Problem:** Whether "smallness" is a transferable skill or a per-category memorization is unknown, determining data strategy.
- **Hypothesis:** Small-instance oversampling on category set A improves small-object performance on disjoint category set B by ≥50% of the within-A gain, evidencing a category-general smallness skill.
- **Why Important:** Category-general transfer would let one curated small-object corpus lift the entire long tail.
- **Why Possibly Novel (hypothesized):** Cross-category transfer measurement of size-specific skill appears untested.
- **Minimal Experiment:** Fine-tune with size-resampled data on split A; evaluate size-stratified metrics on disjoint split B vs. controls.
- **Main Risk:** Category splits may leak visually similar classes.
- **Cluster:** `small-thin-objects`

### A-0142
- **Idea:** Ask whether context helps or hurts small objects in VFMs: measuring the causal effect of surrounding context on small-object segmentation via inpainting-based context ablations.
- **Problem:** Small objects are assumed to need context, but context may also swamp their weak signal in attention; the net causal effect is unmeasured.
- **Hypothesis:** Context benefit is non-monotonic in object size: below a size threshold, ablating context (neutral inpainting) *improves* segmentation because attention mass stops leaking to context, reversing the standard assumption.
- **Why Important:** Would justify context-suppressing inference modes for small-object regimes.
- **Why Possibly Novel (hypothesized):** Causal context ablation across the size spectrum appears novel.
- **Minimal Experiment:** Inpaint context around objects at varying sizes; measure IoU deltas vs. size; track attention-mass reallocation.
- **Main Risk:** Inpainting artifacts may introduce their own confounds.
- **Cluster:** `small-thin-objects`

### A-0143
- **Idea:** Study sub-pixel boundary encoding for tiny objects: whether logit fields around 3–10 pixel objects carry sub-pixel localization information exceeding the mask grid, extractable for metrology applications.
- **Problem:** Tiny-object masks are quantization-dominated; whether the continuous logits encode finer localization than binarized outputs is unknown.
- **Hypothesis:** Subpixel centroid/extent estimators computed from logits beat binarized-mask estimators by ≥2× localization accuracy on tiny objects, approaching the information-theoretic bound from image blur.
- **Why Important:** Enables measurement-grade use (particle analysis, astronomy, defect metrology) without super-resolution retraining.
- **Why Possibly Novel (hypothesized):** Logit-based sub-pixel metrology from VFMs appears unexplored.
- **Minimal Experiment:** Synthetic tiny objects with exact ground truth positions; compare centroid/extent errors from logits vs. binary masks vs. classical fitting.
- **Main Risk:** Logit shapes may be decoder artifacts uncorrelated with true sub-pixel position.
- **Cluster:** `small-thin-objects`

### A-0144
- **Idea:** Test whether the small-object gap is partially an NMS/post-processing artifact in detectors: small objects suffer disproportionately from IoU-based duplicate removal because their IoU is hypersensitive to pixel-level box noise.
- **Problem:** IoU thresholds behave differently across scales (one-pixel shifts change small-box IoU drastically), but post-processing is scale-blind.
- **Hypothesis:** Scale-normalized duplicate-removal criteria (e.g., center-distance in units of object size) recover a measurable fraction of small-object AP without touching the model, quantifying how much "detection failure" is post-processing failure.
- **Why Important:** Free small-object AP by fixing plumbing, plus honest attribution of the gap.
- **Why Possibly Novel (hypothesized):** Scale-conditioned post-processing attribution of small-object loss appears under-quantified.
- **Minimal Experiment:** Replace NMS criteria with scale-normalized variants across detectors; report size-stratified AP deltas and error-type migration.
- **Main Risk:** May be less relevant to NMS-free architectures, dating the finding.
- **Cluster:** `small-thin-objects`

### A-0145
- **Idea:** Investigate attention starvation of small objects: whether the total attention mass a small object receives in a cluttered scene predicts its segmentation failure better than its size, formalizing "salience competition" as the failure driver.
- **Problem:** Small objects fail more in cluttered scenes than alone, suggesting a competition effect distinct from size itself.
- **Hypothesis:** Received-attention mass mediates the size-failure relationship (size loses predictive power once attention mass is conditioned on), and attention re-injection at the prompt location eliminates the clutter penalty.
- **Why Important:** Mediation analysis identifies the manipulable variable (attention allocation) for targeted fixes.
- **Why Possibly Novel (hypothesized):** Formal mediation analysis of attention mass in segmentation failure appears new.
- **Minimal Experiment:** Measure per-object received attention across clutter conditions; run mediation analysis; test inference-time attention biasing toward prompts.
- **Main Risk:** Attention mass is layer/head-ambiguous; needs a defensible aggregate.
- **Cluster:** `small-thin-objects`

### A-0146
- **Idea:** Study densely packed small instances (grains, cells, crowds) as a phase-transition problem: whether instance-separation ability collapses discontinuously at a critical packing density, and whether the critical density scales with model resolution.
- **Problem:** Packed-instance failure is treated as gradual; a critical-density characterization would change how limits are reported and predicted.
- **Hypothesis:** Instance-recall vs. packing-density curves show a sharp transition whose critical point scales linearly with effective output resolution, enabling extrapolation of feasibility for a target density from model specs.
- **Why Important:** Predictable feasibility boundaries prevent doomed deployments in cytology, agriculture, and crowd analysis.
- **Why Possibly Novel (hypothesized):** Phase-transition framing of packing density in segmentation appears untested.
- **Minimal Experiment:** Synthetic packing-density sweeps plus real datasets binned by density; locate transitions across models with differing resolutions.
- **Main Risk:** Real-data density confounds with object appearance changes.
- **Cluster:** `small-thin-objects`

### A-0147
- **Idea:** Test whether small-object performance can be bought at inference time via test-time augmentation targeted by a size-aware disagreement detector, spending compute only where the size regime predicts fragility.
- **Problem:** Uniform TTA is wasteful; small objects are a predictable fragility regime deserving targeted compute.
- **Hypothesis:** Size-and-disagreement-gated TTA achieves ≥90% of full-TTA small-object gains at ≤25% of its compute, establishing adaptive-compute allocation as strictly dominant for size-skewed workloads.
- **Why Important:** Practical recipe aligning compute expenditure with failure probability.
- **Why Possibly Novel (hypothesized):** Fragility-gated TTA for segmentation appears unstudied as a controlled question.
- **Minimal Experiment:** Implement gated vs. uniform TTA on size-skewed datasets; report Pareto curves of small-object AP vs. compute.
- **Main Risk:** Gains bounded by TTA's inherent ceiling on the base model.
- **Cluster:** `small-thin-objects`

### A-0148
- **Idea:** Investigate annotation reliability as the hidden ceiling for small objects: measuring inter-annotator IoU as a function of object size to determine where model "failures" are actually within label noise.
- **Problem:** Small-object metrics may bottom out at human labeling noise, making reported model gaps partially fictitious.
- **Hypothesis:** Inter-annotator IoU declines steeply below ~20px objects, and correcting model-human gaps for label noise removes a large share of the claimed small-object deficit on standard benchmarks.
- **Why Important:** Reframes the small-object problem: some of it needs better labels and noise-aware metrics, not better models.
- **Why Possibly Novel (hypothesized):** Noise-corrected small-object gap accounting appears rare.
- **Minimal Experiment:** Multi-annotate size-stratified samples from COCO/LVIS; compute noise-adjusted model gaps per size bin.
- **Main Risk:** Annotator recruitment/protocol strongly affects noise estimates.
- **Cluster:** `small-thin-objects`

### A-0149
- **Idea:** Ask whether video temporal integration can rescue small static objects: aggregating SAM2 features across frames of a shaking/moving camera to super-resolve small-object segmentation beyond single-frame ability.
- **Problem:** Single frames under-resolve small objects, but multi-frame evidence with sub-pixel offsets contains recoverable detail that memory architectures may or may not exploit.
- **Hypothesis:** SAM2's memory attention does not currently exploit sub-pixel multi-frame evidence (video ≈ best single frame for small statics), but explicit feature registration and averaging yields measurable super-resolution gains — locating an unexploited information source.
- **Why Important:** Camera jitter is free information for edge devices; exploiting it lifts the small-object floor without new sensors.
- **Why Possibly Novel (hypothesized):** Multi-frame sub-pixel analysis for promptable video segmentation appears unexamined.
- **Minimal Experiment:** Controlled jittered-camera videos of resolution charts and small objects; compare SAM2, single-frame SAM, and registration-averaged variants.
- **Main Risk:** Registration errors may cancel the sub-pixel gains in practice.
- **Cluster:** `small-thin-objects`

### A-0150
- **Idea:** Test size-conditional prompt strategies: whether the optimal prompt type flips with object size (points beating boxes below a size threshold because tiny boxes are noisier than clicks), yielding a size-aware prompting rule.
- **Problem:** Prompt-type recommendations ignore object size, though prompt information content scales differently with size for boxes vs. points.
- **Hypothesis:** Below a threshold size, point prompts outperform boxes (box coordinate noise exceeds object extent), and above it boxes win; the crossover is predictable from annotation-noise models.
- **Why Important:** A simple, deployable prompting rule that improves the weakest regime for free.
- **Why Possibly Novel (hypothesized):** Size-conditioned prompt-type analysis appears undone.
- **Minimal Experiment:** Evaluate point vs. box prompting with realistic coordinate noise across size bins on 3 datasets; locate crossovers; validate the noise-model prediction.
- **Main Risk:** Crossover may depend on annotator-noise assumptions that vary by tool.
- **Cluster:** `small-thin-objects`

---

## Sub-cluster 11: Evaluation weakness (`evaluation-weakness`)

### A-0151
- **Idea:** Quantify metric-induced research bias: whether mIoU's insensitivity to boundary and small-object errors has measurably steered model development, by re-ranking historical models under error-type-balanced metrics.
- **Problem:** The field optimizes what mIoU sees; capabilities invisible to mIoU may have stagnated or regressed unnoticed across model generations.
- **Hypothesis:** Under a boundary- and size-balanced composite metric, the apparent monotone progress of segmentation models over recent generations flattens or partially inverts for specific capability axes.
- **Why Important:** Reveals whether "progress" is metric-shaped, informing benchmark reform priorities.
- **Why Possibly Novel (hypothesized):** Longitudinal re-ranking under rebalanced metrics appears undone systematically.
- **Minimal Experiment:** Evaluate 12 historical models spanning 5 years under mIoU and 4 rebalanced composites; analyze trend changes per capability.
- **Main Risk:** Composite-metric design choices could themselves bias conclusions; needs sensitivity analysis.
- **Cluster:** `evaluation-weakness`

### A-0152
- **Idea:** Test benchmark saturation vs. label-noise floor: for saturated segmentation benchmarks, determine whether top models have reached the label-noise ceiling, making residual gaps meaningless.
- **Problem:** Leaderboard gaps of <1 point drive publication, but may lie entirely within annotation noise, making rankings lottery-like.
- **Hypothesis:** On several standard benchmarks, inter-annotator agreement bounds imply top-5 model differences are statistically indistinguishable, and bootstrap-over-annotations breaks current orderings.
- **Why Important:** Prevents wasted effort chasing noise and motivates noise-aware reporting standards.
- **Why Possibly Novel (hypothesized):** Annotation-bootstrap significance testing of leaderboard orderings appears rare.
- **Minimal Experiment:** Multi-annotate benchmark samples; propagate label uncertainty through metric computation; report significance of top-model gaps.
- **Main Risk:** Partial re-annotation may not capture full benchmark noise structure.
- **Cluster:** `evaluation-weakness`

### A-0153
- **Idea:** Study "prompt protocol sensitivity" of promptable-model benchmarks: how much reported rankings depend on the simulated prompting protocol (click policy, box jitter), and define protocol-robust evaluation.
- **Problem:** Papers use idiosyncratic prompt simulators, so cross-paper numbers are incomparable in unknown ways.
- **Hypothesis:** Model rankings flip for a substantial fraction of model pairs across common prompt protocols, and reporting a protocol-marginalized score (average over a protocol distribution) yields stable rankings.
- **Why Important:** Establishes whether promptable-segmentation comparisons are currently reproducible at all.
- **Why Possibly Novel (hypothesized):** Protocol-marginalized evaluation for promptable models appears unproposed.
- **Minimal Experiment:** Evaluate 8 models under 6 documented protocols; count ranking inversions; test stability of the marginalized score under protocol resampling.
- **Main Risk:** Defining the protocol distribution introduces its own arbitrariness.
- **Cluster:** `evaluation-weakness`

### A-0154
- **Idea:** Investigate test-set contamination of VFMs via output regurgitation: detecting whether SAM-family models reproduce annotation-style idiosyncrasies of specific public test sets, indicating those sets leaked into training.
- **Problem:** Web-scale pretraining plausibly ingests benchmark images/labels, but segmentation-specific contamination detection tools are missing.
- **Hypothesis:** Models emit statistically detectable signatures (matching test-set-specific annotation conventions on ambiguous boundaries) on contaminated benchmarks but not on verified-clean ones, providing a contamination test without training-data access.
- **Why Important:** Contamination invalidates zero-shot claims — the central selling point of VFMs.
- **Why Possibly Novel (hypothesized):** Style-signature contamination detection for segmentation appears new.
- **Minimal Experiment:** Define per-benchmark annotation-style fingerprints; test whether model outputs match fingerprints beyond what image evidence supports, using post-cutoff data as control.
- **Main Risk:** Style convergence may occur without contamination (confound).
- **Cluster:** `evaluation-weakness`

### A-0155
- **Idea:** Build the case for "failure-mass" reporting: whether the tail of per-image errors (worst 5%) diverges across models that share identical mean metrics, and whether tail behavior predicts deployment incidents better than means.
- **Problem:** Mean metrics compress away the tail, but deployments die by the tail; the mean-tail decoupling across modern models is unquantified.
- **Hypothesis:** Models matched within 0.5 mIoU differ by >2× in 95th-percentile per-image error, and tail metrics correlate better with human-reported failure severity in an applied setting.
- **Why Important:** Motivates tail-aware leaderboards that would immediately change model selection for practitioners.
- **Why Possibly Novel (hypothesized):** Tail-divergence quantification across metric-matched segmentation models appears missing.
- **Minimal Experiment:** Evaluate metric-matched model pairs; compare per-image error distributions; run a small practitioner study rating failure severity against both metric families.
- **Main Risk:** Tail estimates are high-variance; need large evaluation sets.
- **Cluster:** `evaluation-weakness`

### A-0156
- **Idea:** Test whether "zero-shot" evaluations of promptable models are actually measuring prompt-engineering skill of the evaluator: variance across reasonable evaluator choices vs. variance across models.
- **Problem:** If evaluator degrees of freedom (prompt choice, threshold, resolution) rival model differences, zero-shot comparisons measure the wrong thing.
- **Hypothesis:** Evaluator-choice variance amounts to a large fraction (>50%) of between-model variance on common zero-shot suites, quantified by crossed evaluator×model designs.
- **Why Important:** Establishes error bars that honest zero-shot claims must carry.
- **Why Possibly Novel (hypothesized):** Crossed variance decomposition of evaluator vs. model appears unapplied to segmentation.
- **Minimal Experiment:** Have 6 independent evaluators (scripted configurations) evaluate 6 models; fit variance components; publish the ratio.
- **Main Risk:** Choosing "reasonable" evaluator configurations is itself contestable.
- **Cluster:** `evaluation-weakness`

### A-0157
- **Idea:** Investigate benchmark ecology: whether the set of widely used segmentation benchmarks spans a small subspace of real-world image statistics, quantifying coverage holes against a large unlabeled corpus.
- **Problem:** Benchmarks accumulate by convenience; the coverage of real usage distributions is asserted, never measured.
- **Hypothesis:** Standard benchmark suites cover <40% of the density of a broad web/robotics/medical usage corpus in feature space, with identifiable holes (night, motion blur, dense text, reflective surfaces) where model rankings differ from benchmark rankings.
- **Why Important:** Coverage holes are where silent deployment failures live; mapping them prioritizes new benchmark construction.
- **Why Possibly Novel (hypothesized):** Quantified coverage analysis of segmentation benchmark ecology appears novel.
- **Minimal Experiment:** Embed benchmarks and usage corpora in a common feature space; estimate coverage; spot-evaluate models in the largest holes with targeted annotation.
- **Main Risk:** Feature-space choice shapes coverage conclusions.
- **Cluster:** `evaluation-weakness`

### A-0158
- **Idea:** Study granularity ambiguity as an evaluation confound: what fraction of measured "errors" on standard benchmarks are legitimate alternative granularities (part vs. whole) punished as mistakes?
- **Problem:** Fixed-granularity GT penalizes defensible interpretations, distorting model comparison in unknown magnitude.
- **Hypothesis:** Granularity-defensible predictions account for a nontrivial share (>15%) of measured error on instance benchmarks, and models differ systematically in granularity style, making current rankings partially granularity-taste rankings.
- **Why Important:** Separates real errors from taste mismatches, enabling granularity-aware evaluation.
- **Why Possibly Novel (hypothesized):** Quantified granularity-confound accounting appears missing.
- **Minimal Experiment:** Human-review sampled "errors" from 5 models with a granularity-defensibility rubric; estimate confound share per model and benchmark.
- **Main Risk:** Defensibility judgments are subjective; needs multiple reviewers and agreement analysis.
- **Cluster:** `evaluation-weakness`

### A-0159
- **Idea:** Test evaluation-through-use: whether downstream-task deltas (robot grasp success, image-editing user acceptance) correlate with segmentation-metric deltas across models, calibrating how much benchmark improvement buys real utility.
- **Problem:** The exchange rate between benchmark points and downstream utility is unknown, so effort allocation is uncalibrated.
- **Hypothesis:** The benchmark-utility correlation is strong at low quality but saturates sharply beyond a task-specific threshold, and the threshold varies by an order of magnitude across applications.
- **Why Important:** Tells the field where marginal benchmark gains stopped mattering — per application.
- **Why Possibly Novel (hypothesized):** Multi-application exchange-rate curves for segmentation quality appear unmeasured.
- **Minimal Experiment:** Plug 6 models spanning quality levels into 3 downstream harnesses (grasping sim, editing study, counting pipeline); fit utility-vs-metric curves.
- **Main Risk:** Downstream harness idiosyncrasies may dominate the mapping.
- **Cluster:** `evaluation-weakness`

### A-0160
- **Idea:** Investigate temporal evaluation drift: whether models evaluated on benchmarks collected years ago overestimate performance on current-day imagery (new products, styles, cameras), quantifying "benchmark aging" rates for segmentation.
- **Problem:** The world drifts while benchmarks freeze; the aging rate of segmentation benchmarks is unmeasured.
- **Hypothesis:** Performance on temporally stratified imagery (matched content, different capture years) declines measurably with recency for models trained on older corpora, at a quantifiable rate per year that differs by category.
- **Why Important:** Aging rates determine benchmark refresh schedules and honest deployment expectations.
- **Why Possibly Novel (hypothesized):** Benchmark-aging quantification for segmentation appears novel.
- **Minimal Experiment:** Collect year-stamped imagery of stable categories; evaluate fixed models across years; fit temporal decay curves.
- **Main Risk:** Isolating time from content/camera confounds requires careful matching.
- **Cluster:** `evaluation-weakness`

### A-0161
- **Idea:** Test pairwise-comparison evaluation for segmentation: whether human A/B mask preferences produce different model rankings than IoU-based metrics, and build a preference-trained mask-quality model as an evaluation instrument.
- **Problem:** IoU may diverge from perceived quality (penalizing benign deviations, ignoring salient errors), but preference-based segmentation evaluation is undeveloped.
- **Hypothesis:** Human pairwise preferences re-rank models relative to IoU in a reproducible way, and a learned preference model achieves higher agreement with held-out humans than any handcrafted metric.
- **Why Important:** Preference-calibrated evaluation aligns benchmarks with what users actually value.
- **Why Possibly Novel (hypothesized):** Preference-model-based segmentation evaluation appears nascent/absent.
- **Minimal Experiment:** Collect 10k pairwise mask preferences; compare metric-vs-human rank agreements; train and validate the preference model across datasets.
- **Main Risk:** Preferences are context-dependent (task framing changes what "better" means).
- **Cluster:** `evaluation-weakness`

### A-0162
- **Idea:** Study statistical power of common evaluation practice: given typical test-set sizes and variances, what effect sizes can segmentation papers actually detect, and what fraction of published deltas fall below the detectable threshold?
- **Problem:** Papers claim gains without power analysis; the field's false-discovery characteristics are unknown.
- **Hypothesis:** A large fraction of recently published improvement claims fall below the minimum detectable effect at standard test sizes, implying the literature contains substantial noise mining.
- **Why Important:** A power audit would recalibrate reviewing norms and required evidence.
- **Why Possibly Novel (hypothesized):** Field-wide power audits for segmentation evaluation appear undone.
- **Minimal Experiment:** Estimate per-benchmark metric variance via bootstrap; compute minimum detectable effects; survey published deltas from recent proceedings against them.
- **Main Risk:** Survey selection choices could bias the audit; must pre-register criteria.
- **Cluster:** `evaluation-weakness`

### A-0163
- **Idea:** Investigate "annotation style transfer" as an evaluation equalizer: re-annotating a common test set under multiple explicit style guides to measure how much cross-dataset performance differences are style artifacts.
- **Problem:** Cross-dataset gaps are attributed to domain difficulty, but may partly reflect annotation-style mismatch with training conventions.
- **Hypothesis:** Under style-harmonized re-annotation, cross-dataset generalization gaps shrink by a sizable measurable fraction, re-attributing "domain gap" to convention gap for some dataset pairs.
- **Why Important:** Correct attribution changes the research response (style adaptation vs. representation learning).
- **Why Possibly Novel (hypothesized):** Controlled style-guide re-annotation for gap attribution appears rare.
- **Minimal Experiment:** Re-annotate 300 images under 3 style guides; evaluate fixed models against each; decompose gaps into style vs. residual domain components.
- **Main Risk:** Re-annotation cost; style guides may not capture implicit conventions.
- **Cluster:** `evaluation-weakness`

### A-0164
- **Idea:** Test adaptive benchmarks that resist optimization: an evaluation protocol that continually reweights toward each submitted model's weakest regimes, and whether it changes development incentives in simulation.
- **Problem:** Static benchmarks reward overfitting to fixed distributions; evaluation that adapts to probe weaknesses is unexplored for segmentation.
- **Hypothesis:** Under simulated iterated development (models optimized against the benchmark), adaptive weakest-regime evaluation produces models with better worst-case and OOD behavior than static evaluation at equal development budget.
- **Why Important:** Benchmark design is a mechanism-design problem; adaptive protocols could realign incentives field-wide.
- **Why Possibly Novel (hypothesized):** Mechanism-design simulation of segmentation benchmark protocols appears new.
- **Minimal Experiment:** Simulate development loops (hyperparameter/data selection against static vs. adaptive metrics); compare resulting models on held-out stress suites.
- **Main Risk:** Simulation may poorly proxy real research dynamics.
- **Cluster:** `evaluation-weakness`

### A-0165
- **Idea:** Quantify the reproducibility half-life of segmentation results: re-running headline evaluations from released code across environment/dependency drift to measure how fast reported numbers become irreproducible and why.
- **Problem:** Anecdotes of numbers not reproducing abound; the decay structure (causes, magnitudes) is unmeasured.
- **Hypothesis:** A significant fraction of headline numbers shift beyond claimed-improvement magnitudes when re-run with current dependencies, with image I/O and resize implementations as the dominant, fixable causes.
- **Why Important:** Identifies the concrete engineering causes of silent irreproducibility and their fix priority.
- **Why Possibly Novel (hypothesized):** Causal attribution of reproduction drift in segmentation evaluation appears unstudied.
- **Minimal Experiment:** Re-run 15 released evaluation pipelines under controlled dependency variations; attribute deltas via ablation of I/O, resize, and numeric factors.
- **Main Risk:** Selection of re-runnable repos biases toward better-engineered work.
- **Cluster:** `evaluation-weakness`

---

## Sub-cluster 12: Representation mismatch (`representation-mismatch`)

### A-0166
- **Idea:** Test the contrastive-vs-dense mismatch hypothesis: whether CLIP-style image-level pretraining produces feature geometries fundamentally misaligned with dense prediction (measured by intra-object feature coherence), explaining why segmentation heads on CLIP features underperform.
- **Problem:** The specific geometric property that makes some pretrained features "bad for segmentation" is not isolated.
- **Hypothesis:** Intra-object feature coherence (variance within GT masks) predicts frozen-feature segmentation quality across 10 pretrained encoders better than linear-probe classification accuracy does, isolating the operative property.
- **Why Important:** A validated predictor of dense-task suitability would guide pretraining objectives and encoder selection without expensive trials.
- **Why Possibly Novel (hypothesized):** Cross-encoder property-isolation for dense suitability appears incomplete in the literature.
- **Minimal Experiment:** Compute candidate geometric properties for 10 encoders; train identical heads; regress head performance on properties; validate the winner on held-out encoders.
- **Main Risk:** Properties are correlated across encoders, hampering causal isolation.
- **Cluster:** `representation-mismatch`

### A-0167
- **Idea:** Investigate whether SAM's encoder features and CLIP's features are complementary at the pixel level: fusing them not for performance engineering, but to map *which* pixels each representation uniquely resolves.
- **Problem:** "Semantic vs. spatial" complementarity is asserted at the model level, but pixel-level unique-information maps are missing.
- **Hypothesis:** CLIP features uniquely resolve pixels requiring category identity (confusable textures across classes) while SAM features uniquely resolve geometric boundary pixels, with <20% overlap in uniquely resolved sets — quantifying the mismatch precisely.
- **Why Important:** Unique-information maps tell architecture designers what fusion must preserve, beyond blind concatenation.
- **Why Possibly Novel (hypothesized):** Pixelwise unique-information decomposition between VFM feature spaces appears new.
- **Minimal Experiment:** Train per-pixel predictors from each feature set and their union; compute pixelwise information gains; cluster and characterize uniquely resolved pixels.
- **Main Risk:** Probe capacity may distort information attribution.
- **Cluster:** `representation-mismatch`

### A-0168
- **Idea:** Study resolution mismatch between pretraining and deployment: whether ViT features at unseen resolutions degrade due to positional extrapolation rather than content statistics, isolable by evaluating identical content at native vs. interpolated positions.
- **Problem:** Deployment resolutions differ from pretraining, and the failure attribution (positional extrapolation vs. content scale) is unresolved.
- **Hypothesis:** Most resolution-shift degradation in dense tasks traces to positional-embedding interpolation error (removable by resolution-specific positional refit on unlabeled data) rather than content-scale mismatch.
- **Why Important:** A cheap unlabeled-data fix would unlock arbitrary-resolution deployment of frozen VFMs.
- **Why Possibly Novel (hypothesized):** Positional-vs-content attribution at resolution shift appears untested for dense tasks.
- **Minimal Experiment:** Evaluate dense probes at multiple resolutions with (a) interpolated positions, (b) refit positions, (c) content rescaled; decompose degradation.
- **Main Risk:** Positional refit may inadvertently adapt content statistics too.
- **Cluster:** `representation-mismatch`

### A-0169
- **Idea:** Test whether the "segmentation-friendly" property of DINO-style features is attributable to their emergent object-centric attention or to local smoothness, by constructing feature sets that dissociate the two properties.
- **Problem:** Multiple properties co-occur in self-supervised features; which one drives dense-task suitability is unknown.
- **Hypothesis:** Local smoothness without object-centric attention (achievable via smoothness-regularized distillation) accounts for most frozen-feature segmentation ability, demoting the celebrated attention structure to an epiphenomenon.
- **Why Important:** Correct attribution redirects self-supervised pretraining design toward the operative property.
- **Why Possibly Novel (hypothesized):** Dissociation experiments between feature properties appear undone.
- **Minimal Experiment:** Distill feature sets preserving one property at a time; evaluate frozen segmentation probes; compare property-ablated performance.
- **Main Risk:** Clean dissociation via distillation may be technically difficult.
- **Cluster:** `representation-mismatch`

### A-0170
- **Idea:** Investigate token-grid anisotropy inheritance: whether downstream dense heads inherit the ViT patch grid as a measurable bias (mask edges snapping to patch boundaries), and how deep the artifact persists after upsampling layers.
- **Problem:** Patch tokenization imposes a lattice; whether and how much this lattice contaminates final masks is unquantified.
- **Hypothesis:** Predicted boundary positions show statistically significant excess density at patch-boundary phases, decaying with decoder depth but never vanishing, and phase-randomized ensembling (shifted crops) removes it.
- **Why Important:** Lattice artifacts bias shape statistics in scientific applications and are correctable once measured.
- **Why Possibly Novel (hypothesized):** Phase-density analysis of mask boundaries relative to token grids appears new.
- **Minimal Experiment:** Histogram boundary positions modulo patch size across datasets/models; test excess at grid phases; validate the shifted-ensemble fix.
- **Main Risk:** Natural boundary statistics may alias with grid phases spuriously.
- **Cluster:** `representation-mismatch`

### A-0171
- **Idea:** Ask whether feature spaces of different VFMs are related by simple transformations: fitting linear/orthogonal maps between encoder feature spaces and measuring what fraction of dense-task-relevant structure survives translation.
- **Problem:** Every downstream head is encoder-specific; if feature spaces are largely isomorphic, heads could be ported across encoders.
- **Hypothesis:** Linear maps fit on unlabeled data transfer dense heads across same-family encoders with <10% relative loss, but fail across pretraining-objective families, quantifying which objectives create genuinely different geometries.
- **Why Important:** Head portability would decouple application development from encoder churn.
- **Why Possibly Novel (hypothesized):** Dense-task-focused feature-space translation studies appear sparse.
- **Minimal Experiment:** Fit maps between 6 encoder pairs; port segmentation heads; measure retention vs. retrained heads; group by objective family.
- **Main Risk:** Linear maps may be insufficient, requiring careful nonlinear controls.
- **Cluster:** `representation-mismatch`

### A-0172
- **Idea:** Study layer-role reorganization under fine-tuning: whether adapting a VFM for segmentation redistributes where (which depth) boundary and semantic information lives, breaking downstream tools that tap fixed layers.
- **Problem:** Ecosystem tools extract features from fixed layers, assuming stable layer roles across fine-tuning — untested.
- **Hypothesis:** Fine-tuning shifts information depth-profiles substantially (boundary information migrating earlier), and a lightweight "layer-role calibration" probe restores tool compatibility without retraining tools.
- **Why Important:** Silent layer-role drift breaks feature-tapping pipelines in unobservable ways.
- **Why Possibly Novel (hypothesized):** Depth-profile drift analysis under fine-tuning appears unexamined.
- **Minimal Experiment:** Probe information content per layer before/after various fine-tunings; quantify profile shifts; test probe-guided layer reselection.
- **Main Risk:** Probing methodology may itself be sensitive to feature scaling changes.
- **Cluster:** `representation-mismatch`

### A-0173
- **Idea:** Test whether multimodal joint spaces sacrifice spatial fidelity for alignment: measuring the spatial information (localization accuracy decodable from features) of vision encoders before and after text-alignment training at matched architectures.
- **Problem:** Text alignment may be spatially lossy, but the spatial cost of alignment training is unquantified in controlled settings.
- **Hypothesis:** Alignment training measurably reduces decodable localization precision relative to a vision-only twin (same data/architecture), with the loss concentrated in late layers and recoverable by early-layer skip connections.
- **Why Important:** Quantifies a fundamental trade-off shaping all multimodal architecture design for dense tasks.
- **Why Possibly Novel (hypothesized):** Controlled twin-model spatial-cost measurement of alignment appears missing.
- **Minimal Experiment:** Train matched encoders with and without alignment loss on identical data; compare spatial-decoding probes per layer.
- **Main Risk:** Matched-training compute cost; small-scale results may not extrapolate.
- **Cluster:** `representation-mismatch`

### A-0174
- **Idea:** Investigate "feature staleness" in cascaded vision systems: when a detector proposes regions and a promptable segmenter refines them, do the two models' representational disagreements (different notions of objectness) cause characteristic cascade failures?
- **Problem:** Cascades compose models trained with different objectives; failure at the interface (objectness mismatch) is unattributed.
- **Hypothesis:** Cascade errors concentrate on instances where the two models' objectness scores maximally disagree, and a 2-model agreement gate predicts cascade failure better than either model's confidence.
- **Why Important:** Interface-aware diagnostics for composed systems, which is how VFMs are actually deployed.
- **Why Possibly Novel (hypothesized):** Representational-disagreement analysis at cascade interfaces appears new.
- **Minimal Experiment:** Build detector→SAM cascades; log both models' internal scores; test disagreement as a failure predictor across datasets.
- **Main Risk:** Score comparability across heterogeneous models needs careful normalization.
- **Cluster:** `representation-mismatch`

### A-0175
- **Idea:** Study whether frozen VFM features encode camera metadata (focal length, ISO, processing pipeline) strongly enough to act as shortcut features for downstream heads, causing camera-coupled generalization failure.
- **Problem:** Downstream heads may latch onto camera signatures in features rather than content, but the strength of camera encoding in VFM features is unmeasured.
- **Hypothesis:** Camera parameters are decodable from VFM features with high accuracy, and downstream segmentation heads trained on camera-skewed data measurably exploit them (performance drops under camera-swap counterfactuals).
- **Why Important:** Identifies a pervasive hidden shortcut channel in every frozen-feature pipeline.
- **Why Possibly Novel (hypothesized):** Camera-signature shortcut analysis in VFM features appears unexplored.
- **Minimal Experiment:** Probe camera-parameter decodability; train heads on camera-confounded splits; evaluate under camera-balanced test sets.
- **Main Risk:** Public datasets rarely document camera metadata richly.
- **Cluster:** `representation-mismatch`

### A-0176
- **Idea:** Test the "objectness universality" assumption: whether SAM's class-agnostic objectness transfers to domains with non-photographic object statistics (documents, circuit boards, star fields), or silently switches to texture-contiguity heuristics.
- **Problem:** Class-agnostic segmentation is marketed as universal; the operating definition of "object" outside natural photos is uncharacterized.
- **Hypothesis:** On non-photographic domains, SAM's masks align with local-contrast contiguity rather than domain-expert object definitions (measured by expert-annotated ground truth), and the misalignment is predictable from feature-statistics distance to natural photos.
- **Why Important:** Defines the validity boundary of "segment anything" claims for scientific/industrial users.
- **Why Possibly Novel (hypothesized):** Operationalized objectness audits across non-photographic domains appear sparse.
- **Minimal Experiment:** Collect expert object definitions in 4 non-photo domains; evaluate SAM alignment; correlate misalignment with domain feature distance.
- **Main Risk:** Expert definitions vary within domains, complicating ground truth.
- **Cluster:** `representation-mismatch`

### A-0177
- **Idea:** Investigate representational collapse in feature upsampling: whether the common bilinear-upsample-then-convolve pattern discards a measurable fraction of the encoder's boundary information, using information-theoretic estimates before/after each decoder stage.
- **Problem:** Decoder stages are designed by convention; where information is actually lost along the decode path is unmeasured.
- **Hypothesis:** The first upsampling stage destroys more boundary-relevant information than all subsequent stages combined, and replacing only that stage with a learned resampler recovers most of the recoverable loss.
- **Why Important:** Stage-resolved information accounting turns decoder design from trial-and-error into targeted repair.
- **Why Possibly Novel (hypothesized):** Stage-wise information audits of segmentation decoders appear rare.
- **Minimal Experiment:** Estimate decodable boundary information after each decoder stage (probe-based); ablate/replace the lossiest stage; verify recovery.
- **Main Risk:** Information estimates via probes are lower bounds, complicating stage comparisons.
- **Cluster:** `representation-mismatch`

### A-0178
- **Idea:** Ask whether registers/artifact tokens in ViTs (high-norm background tokens) corrupt promptable segmentation specifically when prompts land near artifact-token locations, linking a known representation anomaly to a task-level failure.
- **Problem:** High-norm token anomalies are documented representationally, but their causal footprint on prompt-conditioned tasks is unmapped.
- **Hypothesis:** Click prompts falling on artifact-token patches yield systematically degraded masks (excess failure rate) and register-token retrofitting eliminates the excess, establishing a causal chain from representation anomaly to user-visible failure.
- **Why Important:** Connects representation science to concrete product failures, motivating retrofits.
- **Why Possibly Novel (hypothesized):** Task-level causal tracing of artifact tokens in promptable models appears new.
- **Minimal Experiment:** Locate high-norm tokens; compare prompt failure rates on vs. off those patches; repeat with register-retrofitted encoders.
- **Main Risk:** Artifact-token locations correlate with background regions, needing careful matching.
- **Cluster:** `representation-mismatch`

### A-0179
- **Idea:** Study cross-modal prompt mismatch in unified models: whether visual prompts (boxes) and language prompts activate inconsistent segment hypotheses for the same target, quantifying intra-model cross-modal disagreement as a reliability signal.
- **Problem:** Unified models accept multiple prompt modalities assumed consistent; their internal cross-modal disagreement rate is unknown and potentially informative.
- **Hypothesis:** Cross-modal disagreement (box-prompted vs. text-prompted masks for the same instance) exceeds 10% of cases, concentrates on boundary ambiguity and granularity, and flags errors with higher precision than single-modality confidence.
- **Why Important:** Free reliability signal from redundant prompting — no extra models required.
- **Why Possibly Novel (hypothesized):** Intra-model cross-modal consistency auditing for segmentation appears unexploited.
- **Minimal Experiment:** Prompt matched instances via box and text in one unified model; measure disagreement statistics; evaluate disagreement as an error detector.
- **Main Risk:** Text prompts introduce granularity variance beyond target identity.
- **Cluster:** `representation-mismatch`

### A-0180
- **Idea:** Test whether pretraining data geometry explains cross-encoder transfer asymmetries: encoders pretrained on object-centric photos transfer worse to scene-centric dense tasks than vice versa, controlling architecture and compute.
- **Problem:** Transfer asymmetries between encoders are observed but unattributed to data composition vs. objective vs. architecture.
- **Hypothesis:** With architecture/objective/compute matched, pretraining-data composition (object-centric vs. scene-centric ratio) predicts direction and magnitude of dense-transfer asymmetry, establishing data geometry as a first-order factor.
- **Why Important:** Would elevate data composition to a controlled design variable for foundation-model builders.
- **Why Possibly Novel (hypothesized):** Controlled data-composition transfer studies at VFM scale appear rare.
- **Minimal Experiment:** Pretrain matched mid-scale encoders on composition-controlled mixtures; evaluate dense transfer both directions; fit composition-transfer curves.
- **Main Risk:** Mid-scale results may not extrapolate to production scales.
- **Cluster:** `representation-mismatch`

---

## Sub-cluster 13: Object detection failures (`detection-failures`)

### A-0181
- **Idea:** Test whether DETR-style query slots develop persistent spatial "territories" that cause systematic misses when object counts in a region exceed local slot allocation, framing missed detections as a resource-allocation failure.
- **Problem:** Query-based detectors miss objects in crowded subregions, but whether misses follow a slot-territory structure is unestablished.
- **Hypothesis:** Each query's matched-object spatial distribution is stable across images (territories), and per-region miss rates are predicted by the ratio of local object count to local slot density, not by global count.
- **Why Important:** A validated slot-allocation account converts crowding failures from mystery to a measurable capacity constraint with clear fixes.
- **Why Possibly Novel (hypothesized):** Territory-based miss prediction for query detectors appears untested quantitatively.
- **Minimal Experiment:** Map query-territory densities on trained detectors; regress regional miss rates on count/slot-density ratios across crowded datasets.
- **Main Risk:** Territories may be too diffuse in modern deformable variants.
- **Cluster:** `detection-failures`

### A-0182
- **Idea:** Investigate duplicate-suppression errors as identity decisions: when two overlapping detections are merged, how often does the survivor take the wrong class/box ("identity theft"), and is the error direction predictable from confidence miscalibration?
- **Problem:** NMS/duplicate handling is evaluated by AP only; the semantic correctness of which hypothesis survives is unexamined.
- **Hypothesis:** In overlap-merge events between different-class hypotheses, the surviving class is wrong in a substantial, calibration-predictable fraction of cases, so calibration repair improves detection accuracy without touching localization.
- **Why Important:** Reveals an error class invisible to AP decompositions and cheaply fixable.
- **Why Possibly Novel (hypothesized):** Identity-level audits of duplicate suppression appear missing.
- **Minimal Experiment:** Log merge events on dense datasets; adjudicate survivor correctness against GT; test calibration-repaired merging.
- **Main Risk:** Requires GT-matched adjudication protocol for ambiguous overlaps.
- **Cluster:** `detection-failures`

### A-0183
- **Idea:** Study open-vocabulary detectors' "background prior" inheritance: whether regions labeled background in base training become systematically undetectable for novel classes occupying those regions (e.g., ceiling-mounted objects), a spatial prior contaminating open-vocabulary claims.
- **Problem:** Open-vocab detectors are trained with base-class backgrounds; novel objects in habitual-background locations may be structurally suppressed.
- **Hypothesis:** Novel-class recall is significantly lower in high-background-prior regions (quantified from base-training statistics) than in low-prior regions, controlling for object appearance — a location-based ceiling on open-vocabulary generalization.
- **Why Important:** Identifies a systematic, correctable blind spot in the dominant open-vocab training recipe.
- **Why Possibly Novel (hypothesized):** Spatial background-prior contamination analysis appears new.
- **Minimal Experiment:** Estimate spatial background priors from base annotations; evaluate novel-class recall stratified by prior; test prior-reweighted fine-tuning.
- **Main Risk:** Object appearance may covary with location, needing synthetic placements for control.
- **Cluster:** `detection-failures`

### A-0184
- **Idea:** Test the "confidence semantics drift" across detector operating points: whether a fixed confidence value means different precision at different object sizes/classes/times of day, making single-threshold deployment principally unsound — and quantify the cost.
- **Problem:** Deployments use one threshold, but confidence-precision mappings likely vary across conditions in unmeasured magnitude.
- **Hypothesis:** Condition-conditional precision at a fixed confidence varies by >30 points across common strata, and per-stratum thresholding recovers a large fraction of oracle-threshold performance.
- **Why Important:** Quantifies the hidden cost of the universal single-threshold practice and validates a simple fix.
- **Why Possibly Novel (hypothesized):** Systematic stratified confidence-semantics audits appear rare.
- **Minimal Experiment:** Compute conditional precision-confidence curves across strata on 4 datasets; measure fixed-vs-stratified thresholding gaps.
- **Main Risk:** Strata definitions influence conclusions; must pre-register.
- **Cluster:** `detection-failures`

### A-0185
- **Idea:** Investigate whether detection errors under occlusion follow an amodal-modal confusion: models localize the visible fragment but classify as if seeing the whole, or vice versa, producing characteristic box-class inconsistencies.
- **Problem:** Occlusion failures are lumped together; the amodal/modal inconsistency structure is undescribed.
- **Hypothesis:** Under partial occlusion, box extent regresses toward visible-fragment bounds while class confidence remains near full-object levels, and this inconsistency signature predicts occlusion-caused errors with high precision.
- **Why Important:** The signature enables occlusion-specific error detection and targeted training data synthesis.
- **Why Possibly Novel (hypothesized):** Box-class inconsistency analysis under occlusion appears unquantified.
- **Minimal Experiment:** Evaluate on occlusion-controlled composites; measure box-extent vs. class-confidence responses to occlusion fraction; validate the signature detector on real data.
- **Main Risk:** Synthetic occlusion may not reproduce natural occlusion statistics.
- **Cluster:** `detection-failures`

### A-0186
- **Idea:** Ask whether query-based detectors can count: probing whether the query-matching mechanism imposes an architectural ceiling on per-class instance counts (queries exhausted), distinct from perceptual limits.
- **Problem:** Detectors' failures on high-count scenes (100+ instances) may be architectural (query budget) rather than perceptual, but the two are conflated.
- **Hypothesis:** Detection recall vs. instance count shows a sharp knee at a fraction of the query budget (interference before exhaustion), and the knee scales sublinearly with query count — an architectural law measurable across models.
- **Why Important:** Determines whether high-count applications need more queries, different architectures, or tiling.
- **Why Possibly Novel (hypothesized):** Recall-vs-count law measurement across query budgets appears undone.
- **Minimal Experiment:** Evaluate detectors with varied query budgets on count-controlled synthetic and real crowded scenes; locate knees; fit scaling.
- **Main Risk:** Training-data count distributions confound architectural limits.
- **Cluster:** `detection-failures`

### A-0187
- **Idea:** Study cross-class calibration coupling in detectors: whether improving one class's data (recalibrating its confidence) shifts other classes' precision through shared logit normalization, creating maintenance whack-a-mole in production.
- **Problem:** Class-wise model updates are assumed local, but shared representations/normalizations may globalize their effects.
- **Hypothesis:** Targeted single-class fine-tuning measurably shifts confidence distributions of untouched classes (beyond retraining noise), with coupling strength predicted by class co-occurrence and feature similarity.
- **Why Important:** Quantifies update side effects that plague production detector maintenance.
- **Why Possibly Novel (hypothesized):** Class-coupling measurement of targeted updates appears unstudied.
- **Minimal Experiment:** Fine-tune on single-class data increments; measure per-class confidence/precision shifts vs. seed-noise baselines; model coupling factors.
- **Main Risk:** Distinguishing coupling from training stochasticity needs many seeds.
- **Cluster:** `detection-failures`

### A-0188
- **Idea:** Test whether "detect-then-segment" and "segment-then-group" pipelines have complementary failure sets, and whether their disagreement is a near-oracle error detector for both.
- **Problem:** Two architectural philosophies coexist, but their failure-set overlap — and hence the value of cross-checking — is unmeasured.
- **Hypothesis:** Failure sets overlap on <40% of errors, and pipeline disagreement detects errors of either pipeline with precision far above self-confidence, making dual-pipeline verification economically rational for high-stakes annotation.
- **Why Important:** Grounds system-level redundancy design in measured failure decorrelation.
- **Why Possibly Novel (hypothesized):** Failure-set decorrelation quantification between paradigm families appears missing.
- **Minimal Experiment:** Run representative pipelines of each family on shared benchmarks; compute failure overlap and disagreement-based detection curves.
- **Main Risk:** Implementation quality differences may masquerade as paradigm differences.
- **Cluster:** `detection-failures`

### A-0189
- **Idea:** Investigate prompt-box "gravity" in promptable detection: whether loose user boxes bias detected extents toward the box (anchoring), quantifying how prompt geometry contaminates output geometry.
- **Problem:** Boxes serve as both query and implicit prior; the anchoring strength of prompt geometry on output geometry is unquantified.
- **Hypothesis:** Output box extent interpolates between true extent and prompt extent with a stable anchoring coefficient that grows with visual ambiguity, and deconvolving the anchoring improves extent accuracy on loose prompts.
- **Why Important:** Anchoring corrupts downstream measurements (sizes, distances) in human-in-the-loop detection.
- **Why Possibly Novel (hypothesized):** Quantitative anchoring analysis of prompt geometry appears new.
- **Minimal Experiment:** Sweep prompt-box looseness/offsets on annotated objects; fit anchoring coefficients vs. ambiguity; test post-hoc deanchoring.
- **Main Risk:** Anchoring may be nonlinear and context-dependent, resisting a simple coefficient.
- **Cluster:** `detection-failures`

### A-0190
- **Idea:** Study temporal flicker of detectors on static scenes: quantifying detection instability under imperceptible frame noise as a "detection jitter constant," and testing whether jitter predicts real-video tracking failure downstream.
- **Problem:** Frame-to-frame detection flicker on essentially identical inputs is folklore; its magnitude, structure, and downstream costs are unmeasured.
- **Hypothesis:** Sub-JND input perturbations produce class-flips or box jitter on a substantial fraction of borderline detections, and the per-model jitter constant predicts downstream tracker identity-switch rates better than AP does.
- **Why Important:** Adds a stability axis to detector evaluation that directly matters for video systems.
- **Why Possibly Novel (hypothesized):** A standardized detection-jitter measure appears unproposed.
- **Minimal Experiment:** Replay static scenes with sensor-noise-level perturbations across detectors; compute jitter statistics; correlate with tracking metrics on video suites.
- **Main Risk:** Jitter depends on threshold placement; needs threshold-marginalized definitions.
- **Cluster:** `detection-failures`

### A-0191
- **Idea:** Ask whether long-tail detection failure is primarily a naming problem in open-vocab systems: rare classes are detected but assigned frequent-class names, testable by decoupling localization recall from naming accuracy on tail classes.
- **Problem:** Tail-class AP conflates "not seen" with "seen but misnamed," which have opposite remedies (data vs. calibration/prompting).
- **Hypothesis:** For open-vocab detectors, a majority of tail-class AP loss is naming failure (correct class-agnostic box exists), with naming errors biased toward frequent siblings — the reverse of closed-set detectors' miss-dominated profile.
- **Why Important:** Redirects the long-tail effort from data collection toward naming calibration where appropriate.
- **Why Possibly Novel (hypothesized):** Naming-vs-miss decomposition across paradigms appears fresh at foundation scale.
- **Minimal Experiment:** Evaluate class-agnostic recall vs. named AP on LVIS tail; classify errors; compare paradigms.
- **Main Risk:** Class-agnostic matching criteria affect the decomposition.
- **Cluster:** `detection-failures`

### A-0192
- **Idea:** Test detector behavior under "class absence certainty": images guaranteed to contain zero instances (verified empty scenes), measuring the false-positive floor and its scaling with scene complexity — the detection analogue of specificity testing.
- **Problem:** Benchmarks contain mostly positive scenes; the FP floor on verified-empty inputs, which dominates alert-fatigue economics, is unmeasured.
- **Hypothesis:** FP rates on verified-empty scenes scale superlinearly with texture complexity and are dominated by a small set of recurring "phantom motifs" per model, which are identifiable and suppressible.
- **Why Important:** Alert-heavy deployments (security, medical screening) are ruled by exactly this floor.
- **Why Possibly Novel (hypothesized):** Verified-absence stress suites for detection appear uncommon.
- **Minimal Experiment:** Curate verified-empty scene sets across complexity levels; catalog FP motifs per detector; test motif-targeted suppression fine-tuning.
- **Main Risk:** Verifying absence at scale is expensive.
- **Cluster:** `detection-failures`

### A-0193
- **Idea:** Investigate whether detectors' localization and classification streams disagree systematically as functions of viewpoint: boxes degrading at oblique views while classification stays stable, generating viewpoint-conditioned inconsistency maps.
- **Problem:** Viewpoint robustness is measured monolithically; stream-specific viewpoint sensitivity is unmapped.
- **Hypothesis:** Localization error grows with viewpoint obliqueness at several times the rate of classification error, and the divergence is architecture-family-dependent (query-based vs. dense heads).
- **Why Important:** Stream-resolved sensitivity informs which architectural stream needs viewpoint-diverse data.
- **Why Possibly Novel (hypothesized):** Stream-decomposed viewpoint analysis appears unreported.
- **Minimal Experiment:** Use 3D-controlled renderings and multi-view real datasets; fit per-stream error-vs-viewpoint curves per architecture family.
- **Main Risk:** Rendering realism limits transfer of conclusions.
- **Cluster:** `detection-failures`

### A-0194
- **Idea:** Study "annotation-policy overfitting" in detection: whether models internalize dataset-specific box conventions (amodal vs. modal, include-handle-or-not), and quantify how much cross-dataset AP loss is convention mismatch rather than capability gap.
- **Problem:** Cross-dataset drops are read as generalization failure, but box-convention differences may explain a hidden share.
- **Hypothesis:** A learned per-dataset "convention translator" (small box-transform model) recovers a substantial fraction of cross-dataset AP loss without touching the detector, upper-bounding the convention share.
- **Why Important:** Correctly attributes generalization gaps and offers a cheap deployment adapter.
- **Why Possibly Novel (hypothesized):** Convention-translation bounding of cross-dataset gaps appears novel for detection.
- **Minimal Experiment:** Train box-transform translators between dataset pairs on overlap classes; measure AP recovery; report convention-share estimates.
- **Main Risk:** Translators may absorb some genuine localization correction, inflating estimates.
- **Cluster:** `detection-failures`

### A-0195
- **Idea:** Test whether end-to-end detectors trained without NMS develop implicit internal suppression circuits, identifiable and editable, whose failure explains residual duplicate errors.
- **Problem:** NMS-free models must suppress duplicates internally, but the mechanism, its location, and its failure conditions are unidentified.
- **Hypothesis:** Duplicate suppression localizes to identifiable self-attention interactions among queries (ablating them restores duplicates), and residual duplicate errors occur exactly when those interactions saturate — enabling targeted capacity increase at that circuit.
- **Why Important:** Mechanistic understanding of learned suppression enables reliability engineering of end-to-end detectors.
- **Why Possibly Novel (hypothesized):** Circuit-level analysis of learned duplicate suppression appears nascent.
- **Minimal Experiment:** Ablate query self-attention patterns systematically; measure duplicate-rate causality; correlate residual duplicates with circuit saturation statistics.
- **Main Risk:** Circuits may be distributed, resisting localization.
- **Cluster:** `detection-failures`

---

## Sub-cluster 14: Scaling laws & emergence in VFMs (`scaling-emergence`)

### A-0196
- **Idea:** Measure capability-resolved scaling laws for promptable segmentation: whether boundary quality, ambiguity handling, and small-object competence scale with model/data size at different exponents, implying divergent capability futures.
- **Problem:** Scaling analyses report aggregate metrics; capability-specific exponents that would forecast which failures scale away are missing.
- **Hypothesis:** Small-object competence scales with a materially smaller exponent than average IoU, predicting that scale alone will not close the small-object gap within feasible budgets.
- **Why Important:** Capability-resolved forecasts tell the field which problems require ideas rather than scale.
- **Why Possibly Novel (hypothesized):** Capability-decomposed scaling exponents for segmentation appear unpublished.
- **Minimal Experiment:** Evaluate a model-size ladder (existing checkpoints) on capability-isolating suites; fit per-capability scaling curves; compare exponents with uncertainty.
- **Main Risk:** Public ladders confound size with data/recipe changes.
- **Cluster:** `scaling-emergence`

### A-0197
- **Idea:** Test whether interactive efficiency (clicks-to-target) improves with scale faster than zero-click accuracy, indicating scale preferentially buys "correctability" rather than correctness.
- **Problem:** Scale's effect on the interactive regime — arguably the deployment-relevant one — is unquantified relative to automatic accuracy.
- **Hypothesis:** Clicks-to-90%-IoU decreases with model scale at a rate exceeding the zero-click IoU improvement rate, because larger models better integrate corrective evidence.
- **Why Important:** If correctability scales faster, product strategy should center interaction, not autonomy, as models grow.
- **Why Possibly Novel (hypothesized):** Interactive-regime scaling measurement appears absent.
- **Minimal Experiment:** Run standardized interactive protocols across a checkpoint ladder; fit scaling of clicks-to-target vs. zero-click metrics.
- **Main Risk:** Interactive protocol choices may interact with scale, needing multiple protocols.
- **Cluster:** `scaling-emergence`

### A-0198
- **Idea:** Investigate emergent prompt-composition ability: whether the capacity to correctly integrate 3+ heterogeneous prompts (points+box+text) appears discontinuously at some scale, or grows smoothly — testing "emergence" claims in a controllable vision setting.
- **Problem:** Emergence debates lack vision-domain tests with dense metrics where discontinuity claims can be evaluated cleanly.
- **Hypothesis:** Multi-prompt integration measured with continuous metrics (IoU under prompt conflict) improves smoothly with scale, and apparent discontinuities arise only under thresholded metrics — supporting the metric-artifact account of emergence for this capability.
- **Why Important:** Vision offers dense, cheap metrics to adjudicate the emergence controversy rigorously.
- **Why Possibly Novel (hypothesized):** Emergence-vs-metric-artifact tests in promptable vision appear undone.
- **Minimal Experiment:** Evaluate prompt-composition suites across scale ladders with both continuous and thresholded metrics; compare curve shapes.
- **Main Risk:** Available scale ladders may be too sparse to resolve curve shape.
- **Cluster:** `scaling-emergence`

### A-0199
- **Idea:** Study data-scaling saturation structure for segmentation pretraining: whether adding more same-distribution masks saturates capabilities in a fixed order, defining a "capability saturation schedule" that guides data-collection stopping.
- **Problem:** Data collection continues past usefulness for some capabilities while others starve, but the saturation order is unknown.
- **Hypothesis:** Capabilities saturate in a stable order (region accuracy first, granularity control last) across data scales, and the order is predicted by per-capability label information density.
- **Why Important:** Saturation schedules turn data budgeting into an allocation problem across capability-targeted data types.
- **Why Possibly Novel (hypothesized):** Capability-saturation ordering for segmentation data appears unmeasured.
- **Minimal Experiment:** Train mid-scale models on nested data subsets; locate per-capability saturation points; test order stability across two data sources.
- **Main Risk:** Mid-scale saturation orders may reshuffle at production scale.
- **Cluster:** `scaling-emergence`

### A-0200
- **Idea:** Test inverse scaling candidates in vision: identify segmentation/detection behaviors that degrade with scale (e.g., over-reliance on semantic priors overriding pixel evidence in unusual scenes), and characterize their mechanism.
- **Problem:** Inverse scaling is documented in language; systematic search for scale-worsened vision behaviors is missing.
- **Hypothesis:** Larger VFMs increasingly override pixel evidence with semantic priors on prior-violating scenes (objects in impossible contexts, atypical colors), measurably worsening at fixed evaluation as scale grows.
- **Why Important:** Scale-worsened behaviors define where bigger is dangerous — critical for safety-relevant deployments.
- **Why Possibly Novel (hypothesized):** An inverse-scaling search program for vision models appears unexecuted.
- **Minimal Experiment:** Build prior-violation suites (counterfactual composites); evaluate across scale ladders; verify monotone degradation and probe the prior-vs-evidence mechanism.
- **Main Risk:** Composite artifacts may drive effects rather than priors.
- **Cluster:** `scaling-emergence`

### A-0201
- **Idea:** Ask whether scaling changes error correlation across models: as models grow, do their residual errors converge (shared blind spots) or decorrelate, determining the future value of ensembling and of independent model development.
- **Problem:** If scale homogenizes errors, ensemble and multi-vendor redundancy strategies lose value precisely as reliance grows.
- **Hypothesis:** Residual-error correlation between independently trained models increases with scale on in-distribution data but not OOD, implying shared-blind-spot risk concentrates in-domain.
- **Why Important:** Governs redundancy architecture for safety-critical vision systems.
- **Why Possibly Novel (hypothesized):** Error-correlation scaling measurement appears new for vision.
- **Minimal Experiment:** Evaluate pairs of independent models at multiple scales; compute error correlations in/out of distribution; fit scale trends.
- **Main Risk:** Truly independent training runs at scale are scarce.
- **Cluster:** `scaling-emergence`

### A-0202
- **Idea:** Study the scaling of "prompt literalism": whether larger promptable models follow prompts more literally (segmenting exactly the clicked part) versus inferring intent (the whole object), quantifying an interpretive-stance drift with scale.
- **Problem:** How scale shifts the literal-vs-intent balance shapes UX design, but the drift direction is unknown.
- **Hypothesis:** Interpretive stance drifts measurably with scale in a consistent direction (hypothesized: toward intent inference), changing optimal prompting strategies across model generations.
- **Why Important:** UX and tooling must anticipate stance drift as backends upgrade.
- **Why Possibly Novel (hypothesized):** Interpretive-stance measurement across scale appears unformalized.
- **Minimal Experiment:** Present part-ambiguous prompts across a model ladder; classify outputs as literal/intent; fit stance-vs-scale curves.
- **Main Risk:** Stance classification requires careful operationalization.
- **Cluster:** `scaling-emergence`

### A-0203
- **Idea:** Test compute-optimal allocation between encoder and decoder for promptable segmentation: whether the scaling-optimal parameter split shifts toward decoders as tasks demand finer masks, contradicting the encoder-heavy convention.
- **Problem:** Parameter allocation across components follows convention, not measured compute-optimality for the segmentation objective.
- **Hypothesis:** For boundary-critical workloads, compute-optimal allocation places several times more relative capacity in the decode path than current designs, with the optimum shifting predictably with output-resolution demands.
- **Why Important:** Misallocation wastes the entire field's training compute; measured optima would redirect architecture design.
- **Why Possibly Novel (hypothesized):** Component-wise compute-optimal analysis for segmentation appears missing.
- **Minimal Experiment:** Train an allocation grid (encoder/decoder splits) at fixed total compute across two scales; fit allocation-performance surfaces per workload type.
- **Main Risk:** Grid training cost; conclusions may depend on architecture family.
- **Cluster:** `scaling-emergence`

### A-0204
- **Idea:** Investigate whether scaling pretraining diversity (domains) vs. depth (more of the same) trades off differently for zero-shot robustness vs. adaptability, defining a diversity-depth frontier for VFM data strategy.
- **Problem:** Data strategy debates lack controlled measurements of the diversity-depth trade-off's downstream consequences.
- **Hypothesis:** Diversity-heavy pretraining maximizes zero-shot robustness while depth-heavy maximizes post-PEFT ceilings, with the frontier's shape stable across model sizes — enabling strategy selection by intended use.
- **Why Important:** Data collection is the dominant cost; the frontier converts strategy debates into engineering choices.
- **Why Possibly Novel (hypothesized):** Controlled diversity-depth frontier measurement for segmentation appears absent.
- **Minimal Experiment:** Pretrain matched mid-scale models on diversity/depth-controlled mixtures; evaluate zero-shot and post-PEFT endpoints; map the frontier.
- **Main Risk:** Mid-scale frontier may shift at production scale.
- **Cluster:** `scaling-emergence`

### A-0205
- **Idea:** Test whether scale substitutes for prompts: measuring the exchange rate between model scale and prompt information (how many fewer clicks a 10× model needs), and whether the exchange rate is constant or regime-dependent.
- **Problem:** Scale and interaction are alternative information sources; their substitution structure is unquantified.
- **Hypothesis:** The scale-prompt exchange rate is strongly regime-dependent: scale substitutes for prompts on common objects but not on ambiguous/rare targets, where interaction remains irreplaceable at any feasible scale.
- **Why Important:** Determines the long-run division of labor between model growth and interface design.
- **Why Possibly Novel (hypothesized):** Formal substitution analysis between scale and interaction appears new.
- **Minimal Experiment:** Measure clicks-to-target across a model ladder stratified by object commonness/ambiguity; fit exchange-rate surfaces.
- **Main Risk:** Ladder confounds (data/recipe) contaminate exchange estimates.
- **Cluster:** `scaling-emergence`

### A-0206
- **Idea:** Study memorization-generalization structure in segmentation pretraining: whether per-sample memorization (verbatim mask reproduction) concentrates on atypical annotation styles, and whether removing memorized samples changes downstream behavior.
- **Problem:** Memorization is studied for classification/generation; its structure and functional role in segmentation pretraining is uncharted.
- **Hypothesis:** Memorized training masks concentrate in style-atypical annotations, and their removal degrades style-robustness (memorization serves as implicit style coverage), revealing a functional role for memorization.
- **Why Important:** Informs privacy-motivated deduplication policies about hidden capability costs.
- **Why Possibly Novel (hypothesized):** Functional-memorization analysis for dense labels appears unexplored.
- **Minimal Experiment:** Detect memorized samples via influence/extraction tests at mid scale; retrain without them; compare style-robustness suites.
- **Main Risk:** Memorization detection for masks lacks established tooling.
- **Cluster:** `scaling-emergence`

### A-0207
- **Idea:** Ask whether emergent "segmentation without prompts" (unprompted object discovery quality) predicts promptable quality across scale, testing if a cheap unprompted probe forecasts expensive promptable evaluation.
- **Problem:** Full promptable evaluation is protocol-heavy; a cheap scaling proxy would accelerate model development loops.
- **Hypothesis:** Unprompted discovery quality (clustering-based) correlates with prompted performance across checkpoints within a training run (r>0.9), enabling proxy-based early stopping and data decisions.
- **Why Important:** Cheap faithful proxies compress developmen iteration cycles substantially.
- **Why Possibly Novel (hypothesized):** Proxy-validity analysis across training trajectories appears unreported.
- **Minimal Experiment:** Log both proxy and full protocol across training checkpoints of two runs; measure trajectory-wise correlation and decision agreement.
- **Main Risk:** Proxy validity may break exactly at decision-relevant margins.
- **Cluster:** `scaling-emergence`

### A-0208
- **Idea:** Test scale effects on annotation-noise robustness: whether larger models trained on noisy masks learn to *exceed* their label quality (denoising) or to reproduce noise more faithfully, resolving a bidirectional-prediction standoff.
- **Problem:** Both "big models average out noise" and "big models memorize noise" are argued; segmentation offers a measurable setting.
- **Hypothesis:** Beyond a scale threshold, models' outputs are systematically closer to clean GT than their own noisy training labels on held-out replicas (denoising regime), with the threshold dependent on noise structure (random vs. systematic).
- **Why Important:** Determines viable label-quality budgets for VFM training economics.
- **Why Possibly Novel (hypothesized):** Label-transcendence threshold measurement for segmentation appears new.
- **Minimal Experiment:** Train scale ladder on controlled-noise masks with clean held-out GT; measure output-vs-label proximity to truth across scales and noise types.
- **Main Risk:** Controlled noise may not represent real annotation error structure.
- **Cluster:** `scaling-emergence`

### A-0209
- **Idea:** Investigate whether scaling reduces or amplifies dataset bias expression: measuring bias metrics (e.g., context-dependence of detection) across a model ladder trained on the same biased corpus.
- **Problem:** Whether scale mitigates or entrenches training-data bias is contested and largely unmeasured in vision.
- **Hypothesis:** Contextual bias (e.g., failing to detect objects out of typical context) grows with scale at fixed data (stronger prior learning), while feature-level biases shrink — a two-regime pattern reconciling conflicting intuitions.
- **Why Important:** Bias-scaling direction determines whether fairness work compounds or erodes with model growth.
- **Why Possibly Novel (hypothesized):** Bias-decomposed scaling measurement appears absent for detection/segmentation.
- **Minimal Experiment:** Evaluate context-swap and feature-bias suites across a fixed-data model ladder; fit per-bias-type scale trends.
- **Main Risk:** Fixed-data ladders are rare; may require training them.
- **Cluster:** `scaling-emergence`

### A-0210
- **Idea:** Test the "capability tax" of multi-task foundation training: whether adding tasks (detection, depth, captioning) to a segmentation foundation model at fixed compute imposes measurable per-capability costs, and map the task-interference matrix at scale.
- **Problem:** Multi-task VFMs are assumed synergistic; the sign and structure of task interference at foundation scale is unmeasured.
- **Hypothesis:** Task pairs partition into stable synergy/interference classes (predictable from gradient-conflict statistics measured early in training), letting builders forecast the cost of each added capability before full training.
- **Why Important:** Task-portfolio decisions are foundational and currently made blind.
- **Why Possibly Novel (hypothesized):** Early-forecastable interference matrices at VFM scale appear unbuilt.
- **Minimal Experiment:** Train task-subset combinations at mid scale; measure interference matrix; validate early gradient-conflict forecasting on held-out combinations.
- **Main Risk:** Interference structure may be recipe-sensitive (loss weights, sampling).
- **Cluster:** `scaling-emergence`

---

## Sub-cluster 15: Interactive segmentation & human-in-the-loop dynamics (`interactive-loop`)

### A-0211
- **Idea:** Model the human-model interaction as a two-agent system: whether humans adapt their clicking strategies to a model's quirks within a session, and how this co-adaptation contaminates interactive benchmarks that assume static user behavior.
- **Problem:** Interactive metrics assume users are fixed policies; real users learn the model, changing the measured system's dynamics mid-evaluation.
- **Hypothesis:** Users measurably shift click strategies within 20 interactions (toward model-favorable placements), improving joint performance beyond what static-policy simulation predicts, by a quantifiable co-adaptation gain.
- **Why Important:** Benchmarks that ignore co-adaptation mis-rank models for real deployment where users learn.
- **Why Possibly Novel (hypothesized):** Within-session co-adaptation measurement for segmentation appears unstudied.
- **Minimal Experiment:** Longitudinal user study (n≈20) with click logging across 100 objects; detect strategy drift; compare joint-performance trajectories to static simulations.
- **Main Risk:** Individual variability may swamp co-adaptation signals at small n.
- **Cluster:** `interactive-loop`

### A-0212
- **Idea:** Test whether "model asks, human answers" beats "human clicks freely": an active-querying interface where the model requests specific disambiguations, evaluated against free clicking at matched interaction budgets.
- **Problem:** Interaction bandwidth is spent inefficiently when humans guess what the model needs; the value of model-directed queries is unquantified for segmentation.
- **Hypothesis:** Model-directed binary queries ("is this region part of the object?") at points of maximal expected information gain reduce total interaction time by ≥30% versus free clicking at equal final quality.
- **Why Important:** Reframes interactive segmentation as optimal experiment design, potentially halving annotation costs.
- **Why Possibly Novel (hypothesized):** Information-optimal query generation for mask disambiguation appears underexplored.
- **Minimal Experiment:** Implement expected-information-gain query selection over SAM hypotheses; user study comparing paradigms at matched budgets.
- **Main Risk:** Query comprehension overhead may consume the theoretical gains.
- **Cluster:** `interactive-loop`

### A-0213
- **Idea:** Characterize interaction failure spirals: sessions where each correction worsens the mask, identifying the dynamical signature (correction-response gain >1) and the conditions triggering instability.
- **Problem:** Some interactive sessions diverge — corrections amplify errors — but the phenomenon lacks a dynamical characterization and predictor.
- **Hypothesis:** Spiral sessions exhibit a measurable loop gain (mask-change magnitude per correction) exceeding 1 from the first correction, predictable from initial mask-hypothesis entropy, enabling early spiral warnings.
- **Why Important:** Spirals destroy user trust disproportionately; predicting them enables interface interventions.
- **Why Possibly Novel (hypothesized):** Control-theoretic analysis of interactive segmentation dynamics appears new.
- **Minimal Experiment:** Mine spiral sessions from large simulated and human logs; fit loop-gain models; validate entropy-based early prediction.
- **Main Risk:** Spiral definition sensitivity; human logs are scarce.
- **Cluster:** `interactive-loop`

### A-0214
- **Idea:** Test scribbles vs. clicks information-theoretically: measuring bits-of-constraint per second of user effort across prompt modalities, and whether the best modality flips with object complexity.
- **Problem:** Prompt-modality choices are stylistic; an effort-normalized information framework for comparing them is missing.
- **Hypothesis:** Scribbles dominate clicks in constraint-bits per second for high-genus/thin objects but lose for compact objects, with the crossover predictable from object skeleton complexity.
- **Why Important:** Grounds interface design in measurement rather than fashion.
- **Why Possibly Novel (hypothesized):** Effort-normalized information analysis of prompt modalities appears unformalized.
- **Minimal Experiment:** Instrument effort (time, path length) and outcome across modalities on complexity-stratified objects with real users; fit crossover curves.
- **Main Risk:** Effort measurement noise across users and devices.
- **Cluster:** `interactive-loop`

### A-0215
- **Idea:** Study "correction locality violation": user corrections intended as local edits causing distant mask changes, quantifying the violation rate and its trust cost, and testing locality-constrained decoding.
- **Problem:** Users expect local edits to act locally; promptable decoders re-infer globally, sometimes changing distant regions — an unquantified UX hazard.
- **Hypothesis:** Distant changes (>2× object scale from correction) occur in a nontrivial fraction of corrections, correlate with user-reported frustration, and locality-constrained decoding eliminates them at <2% quality cost.
- **Why Important:** Locality is a core interaction contract; honoring it cheaply would improve every interactive tool.
- **Why Possibly Novel (hypothesized):** Locality-contract analysis for promptable decoders appears new.
- **Minimal Experiment:** Measure distant-change rates across correction types; user study linking violations to trust ratings; implement masked-region re-decoding and re-measure.
- **Main Risk:** Some distant changes are genuinely desirable (topology fixes), complicating the contract.
- **Cluster:** `interactive-loop`

### A-0216
- **Idea:** Investigate optimal correction ordering for multi-error masks: whether fixing the largest error first (greedy) is suboptimal because corrections interact, and derive an interaction-aware ordering policy.
- **Problem:** Users and simulators fix errors greedily; if corrections interact through the model's re-inference, ordering matters unexplored.
- **Hypothesis:** Interaction-aware ordering (fixing errors whose correction maximally reduces other errors) saves ≥20% of corrections versus greedy on multi-error masks, and the interaction structure is predictable from hypothesis overlap.
- **Why Important:** Free efficiency for every annotation workflow via smarter ordering suggestions.
- **Why Possibly Novel (hypothesized):** Correction-interaction analysis in interactive segmentation appears unexamined.
- **Minimal Experiment:** Simulate all correction orderings on multi-error cases; measure ordering spread; fit interaction predictors; validate the derived policy.
- **Main Risk:** Combinatorial simulation cost limits object sample sizes.
- **Cluster:** `interactive-loop`

### A-0217
- **Idea:** Test undo-informed learning: whether user undo events (implicit negative feedback on model updates) form a supervision signal that, aggregated across sessions, identifies systematic model failures better than explicit error reports.
- **Problem:** Undo streams are discarded, yet they precisely mark moments the model violated user intent.
- **Hypothesis:** Failure clusters mined from undo events have higher precision for reproducible model bugs than clusters from explicit feedback, because undos are behaviorally honest and abundant.
- **Why Important:** Turns free interaction exhaust into a model-improvement pipeline.
- **Why Possibly Novel (hypothesized):** Undo-stream mining for vision model diagnostics appears unused.
- **Minimal Experiment:** Instrument an annotation tool; collect undo streams; cluster undo-preceding states; verify cluster reproducibility as model failures.
- **Main Risk:** Undos conflate user error with model error, needing disentanglement.
- **Cluster:** `interactive-loop`

### A-0218
- **Idea:** Study expertise transfer through interaction data: whether models fine-tuned on expert-user interaction traces acquire the experts' disambiguation preferences, transferring tacit knowledge that explicit labels miss.
- **Problem:** Expert annotators embed tacit conventions in their interaction sequences (what they fix first, what they accept), which mask-only training discards.
- **Hypothesis:** Training on interaction traces (state-action sequences) transfers acceptance thresholds and granularity preferences measurably better than training on final masks alone, evaluated by agreement with held-out expert decisions.
- **Why Important:** Tacit-knowledge capture could raise auto-annotation to expert level without formalizing conventions.
- **Why Possibly Novel (hypothesized):** Trace-based tacit-convention learning for segmentation appears new.
- **Minimal Experiment:** Collect expert traces; train trace-conditioned vs. mask-only models; compare on expert-agreement metrics.
- **Main Risk:** Trace data collection at scale; expert time is expensive.
- **Cluster:** `interactive-loop`

### A-0219
- **Idea:** Test latency's causal effect on interactive segmentation quality: not just satisfaction, but whether response delays change user strategies (fewer, coarser corrections) and degrade final masks — with a measured latency-quality curve.
- **Problem:** Latency budgets are set by feel; the causal quality cost of each 100ms is unmeasured for segmentation interaction.
- **Hypothesis:** Final mask quality degrades measurably beyond a latency threshold (hypothesized 300–500ms) via a strategy-shift mechanism (users batch corrections), not merely reduced correction counts.
- **Why Important:** Justifies (or debunks) engineering investment in low-latency inference with quality-denominated numbers.
- **Why Possibly Novel (hypothesized):** Causal latency-quality curves with mechanism analysis appear missing for vision interaction.
- **Minimal Experiment:** Within-subject study injecting controlled latencies; log strategies and final quality; fit the curve and test mediation via strategy variables.
- **Main Risk:** Lab settings may not reproduce production impatience.
- **Cluster:** `interactive-loop`

### A-0220
- **Idea:** Investigate cross-object priming within sessions: whether segmenting several objects of a category primes the model-user system (via cached prompts or user expectations) to segment subsequent same-category objects faster, and whether tools should exploit it by batching similar objects.
- **Problem:** Session-level structure (object ordering) is ignored by tools; priming effects could make ordering a free optimization.
- **Hypothesis:** Same-category batching reduces per-object interaction time by ≥15% relative to shuffled order, with the gain split measurably between user priming and exploitable model-side context reuse.
- **Why Important:** Zero-cost workflow reordering with measurable annotation savings.
- **Why Possibly Novel (hypothesized):** Session-order effects in interactive segmentation appear unstudied.
- **Minimal Experiment:** User study with batched vs. shuffled object orders; decompose gains via model-side context ablations.
- **Main Risk:** Fatigue and learning effects confound ordering effects.
- **Cluster:** `interactive-loop`

### A-0221
- **Idea:** Test the "annotation authority" problem: when model suggestions disagree with novice annotators, who is right how often — and does showing model confidence change novice deference optimally or pathologically?
- **Problem:** Model-assisted labeling flips authority dynamics; whether confidence displays induce correct deference is unknown for segmentation.
- **Hypothesis:** Novices over-defer to confident wrong suggestions (accepting a large fraction of high-confidence errors) and under-defer to unconfident correct ones, with net label quality *below* unassisted labeling in identifiable regimes.
- **Why Important:** Assisted labeling can silently degrade dataset quality — the opposite of its purpose — in measurable conditions.
- **Why Possibly Novel (hypothesized):** Deference-calibration studies for segmentation assistance appear rare.
- **Minimal Experiment:** Controlled study crossing suggestion correctness × displayed confidence × annotator expertise; measure acceptance and final quality.
- **Main Risk:** Ethical design needed around deliberately wrong suggestions.
- **Cluster:** `interactive-loop`

### A-0222
- **Idea:** Study memory across sessions: whether a personalized interaction memory (this user's past corrections on similar content) reduces repeated corrections, and what memory representation (exemplar vs. adapter) transfers corrections best.
- **Problem:** Tools forget every session; repeat corrections on similar content waste effort, and the right personalization substrate is unknown.
- **Hypothesis:** Retrieval-based exemplar memory (correction replay on visually similar regions) reduces repeated corrections more than adapter fine-tuning at equal storage, because corrections are instance-specific rather than distributional.
- **Why Important:** Determines the architecture of personalization in annotation products.
- **Why Possibly Novel (hypothesized):** Substrate comparison for interaction-memory personalization appears untested.
- **Minimal Experiment:** Longitudinal simulated + human sessions on themed corpora; compare exemplar-retrieval vs. adapter personalization on repeat-correction rates.
- **Main Risk:** Retrieval quality on visual similarity may bottleneck the exemplar approach.
- **Cluster:** `interactive-loop`

### A-0223
- **Idea:** Test group interaction: multiple annotators refining the same mask concurrently or sequentially — does sequential refinement converge to better masks than the best individual, or do annotators undo each other along style disagreements?
- **Problem:** Collaborative annotation dynamics for dense labels are unmeasured; wiki-style refinement may or may not converge for masks.
- **Hypothesis:** Sequential multi-annotator refinement converges on content errors but oscillates indefinitely on style dimensions (boundary tightness), so style-locking (fixing conventions upfront) is necessary and sufficient for convergence.
- **Why Important:** Collaborative refinement could raise gold-standard quality if its failure modes are engineered away.
- **Why Possibly Novel (hypothesized):** Convergence analysis of collaborative mask refinement appears new.
- **Minimal Experiment:** Chain annotators on shared masks with/without style guides; measure convergence vs. oscillation spectra of successive edits.
- **Main Risk:** Recruiting enough annotators for chains; ordering effects.
- **Cluster:** `interactive-loop`

### A-0224
- **Idea:** Investigate eyetracking as a zero-effort prompt channel: whether gaze fixations during natural viewing suffice as implicit clicks for promptable models, and where gaze-as-prompt fails relative to deliberate clicks.
- **Problem:** Gaze is nearly free to collect in AR/VR contexts, but its adequacy as a prompt substitute (precision, intentionality) is unquantified.
- **Hypothesis:** Fixation clusters achieve within 15% of click-prompt quality for salient objects but fail systematically on low-salience targets where user intent diverges from bottom-up attention — mapping the gaze-prompt validity boundary.
- **Why Important:** Hands-free segmentation would unlock accessibility and AR annotation use cases.
- **Why Possibly Novel (hypothesized):** Gaze-prompt validity mapping for SAM-class models appears sparse.
- **Minimal Experiment:** Collect gaze during object-identification tasks; feed fixations as prompts; compare against clicks stratified by target salience.
- **Main Risk:** Eyetracker precision and calibration drift contaminate prompt quality.
- **Cluster:** `interactive-loop`

### A-0225
- **Idea:** Test interruption robustness of interactive sessions: when users abandon sessions midway, are partial interaction traces usable as weak supervision, and how much value do incomplete sessions carry relative to completed ones?
- **Problem:** Abandoned sessions are discarded wholesale, though they contain valid partial constraints — an unmeasured data loss.
- **Hypothesis:** Partial traces (with abandonment modeled as censoring, not rejection) recover ≥60% of completed-session supervision value per interaction, substantially changing the economics of annotation at scale.
- **Why Important:** Real pipelines have high abandonment; recovering that value is free data.
- **Why Possibly Novel (hypothesized):** Censoring-aware learning from abandoned annotation sessions appears unstudied.
- **Minimal Experiment:** Truncate sessions artificially at varying points; train with censoring-aware losses; map supervision value vs. completion fraction.
- **Main Risk:** Real abandonment is informative (harder cases), violating random-censoring assumptions.
- **Cluster:** `interactive-loop`

---

## Sub-cluster 16: Ambiguity & multi-hypothesis segmentation (`ambiguity-multihypothesis`)

### A-0226
- **Idea:** Construct a taxonomy of segmentation ambiguity (granularity, boundary, membership, count) and test whether SAM's three-mask output covers the empirical ambiguity distribution or systematically truncates it.
- **Problem:** The fixed hypothesis count (3) is an architectural guess; the true ambiguity cardinality distribution in natural prompts is unmeasured.
- **Hypothesis:** A significant fraction of ambiguous prompts (>25%) have ≥4 human-defensible interpretations, and SAM's three slots collapse distinct interpretation types rather than sampling them representatively.
- **Why Important:** Defines the hypothesis-budget requirement for faithful ambiguity handling, grounding architecture choices in measurement.
- **Why Possibly Novel (hypothesized):** Empirical ambiguity-cardinality measurement appears missing.
- **Minimal Experiment:** Multi-annotate interpretations for 1k ambiguous prompts; classify ambiguity types; compare against SAM's hypothesis coverage.
- **Main Risk:** Interpretation enumeration by annotators may be incomplete.
- **Cluster:** `ambiguity-multihypothesis`

### A-0227
- **Idea:** Test whether the diversity of SAM's multimask outputs is calibrated to input ambiguity: does hypothesis spread grow with true ambiguity, or is it a fixed architectural signature independent of the input?
- **Problem:** Useful multi-hypothesis output should modulate diversity with ambiguity; whether SAM's does is unknown.
- **Hypothesis:** SAM's inter-hypothesis diversity correlates only weakly (r<0.3) with human-measured ambiguity, behaving as a fixed part-whole-background template rather than input-adaptive uncertainty.
- **Why Important:** If diversity is template-like, downstream uses of hypothesis spread as uncertainty are invalid.
- **Why Possibly Novel (hypothesized):** Diversity-calibration analysis of multimask outputs appears new.
- **Minimal Experiment:** Correlate hypothesis-set diversity with annotator-interpretation entropy across prompts; test template-similarity of hypothesis structure across unrelated images.
- **Main Risk:** Diversity metrics on masks (IoU-based) may miss semantic diversity.
- **Cluster:** `ambiguity-multihypothesis`

### A-0228
- **Idea:** Study whether ambiguity resolution should be lazy: systems that carry multiple mask hypotheses through downstream stages (tracking, counting) and resolve only at decision time, versus eager single-mask commitment — quantifying the value of deferred disambiguation.
- **Problem:** Pipelines commit to one mask early, discarding alternatives whose value downstream is unmeasured.
- **Hypothesis:** Lazy resolution improves end-task metrics (tracking consistency, count intervals) by a measurable margin over eager commitment at bounded compute overhead, with gains concentrated on granularity-ambiguous instances.
- **Why Important:** Would restructure vision pipelines around hypothesis propagation, a significant architectural shift justified only by measurement.
- **Why Possibly Novel (hypothesized):** End-task evaluation of deferred mask disambiguation appears rare.
- **Minimal Experiment:** Build hypothesis-propagating variants of tracking and counting pipelines; compare end metrics and compute against eager baselines.
- **Main Risk:** Hypothesis combinatorics may explode in long pipelines.
- **Cluster:** `ambiguity-multihypothesis`

### A-0229
- **Idea:** Test whether part-whole ambiguity follows compositional structure: when a click is part-whole ambiguous, are the offered hypotheses consistent with a single part hierarchy, or incoherent mixtures (part of one decomposition, whole of another)?
- **Problem:** Hypothesis sets should reflect coherent scene parses; incoherent hypothesis mixtures reveal a non-compositional ambiguity mechanism.
- **Hypothesis:** A measurable fraction of SAM hypothesis triples are hierarchy-incoherent (hypotheses that cannot coexist in any single part decomposition), and incoherence predicts downstream selection errors.
- **Why Important:** Coherence is a testable signature distinguishing structured scene understanding from independent mask proposals.
- **Why Possibly Novel (hypothesized):** Hierarchy-coherence auditing of hypothesis sets appears new.
- **Minimal Experiment:** Annotate part hierarchies for 500 objects; test hypothesis-set embeddability into single hierarchies; correlate incoherence with error rates.
- **Main Risk:** Ground-truth part hierarchies are themselves contestable.
- **Cluster:** `ambiguity-multihypothesis`

### A-0230
- **Idea:** Investigate sequential hypothesis elicitation: prompting the model repeatedly with "give another interpretation" (via hypothesis-conditioned re-prompting) to enumerate its full interpretation space, measuring exhaustiveness and redundancy of the elicitable set.
- **Problem:** The model's latent interpretation space may exceed its k-slot output; elicitation protocols to enumerate it are undeveloped.
- **Hypothesis:** Conditioned re-prompting (masking prior hypotheses' regions from prompts) elicits substantially more distinct valid interpretations than the default output, showing the interpretation space is larger than the interface exposes.
- **Why Important:** Full interpretation enumeration enables true coverage of ambiguity for high-stakes review.
- **Why Possibly Novel (hypothesized):** Interpretation-space enumeration protocols for promptable models appear unbuilt.
- **Minimal Experiment:** Implement iterative elicitation; measure yield curves (new valid interpretations per iteration) against annotator-enumerated references.
- **Main Risk:** Elicitation tricks may generate invalid interpretations requiring filtering.
- **Cluster:** `ambiguity-multihypothesis`

### A-0231
- **Idea:** Study ambiguity as a transferable annotation: whether ambiguity maps (where interpretations disagree) transfer across models, enabling one model's ambiguity atlas to warn another model's users.
- **Problem:** If ambiguity is image-intrinsic, its expensive measurement could be amortized across the model ecosystem; if model-specific, each model needs its own.
- **Hypothesis:** Inter-model ambiguity-map correlation is high (r>0.7) for granularity ambiguity but low for boundary ambiguity, splitting ambiguity into transferable and model-specific components with distinct handling.
- **Why Important:** Amortizable ambiguity atlases would cheapen safe deployment across model families.
- **Why Possibly Novel (hypothesized):** Cross-model ambiguity-transfer decomposition appears unexamined.
- **Minimal Experiment:** Compute ambiguity maps for 5 models on shared corpora; correlate by ambiguity type; validate atlas-based warnings on a held-out model.
- **Main Risk:** Ambiguity-map estimation noise may cap measurable correlations.
- **Cluster:** `ambiguity-multihypothesis`

### A-0232
- **Idea:** Test the "commitment cost" of single-mask APIs: quantifying how much downstream applications lose when the API returns argmax masks versus full hypothesis sets, across application types — an ecosystem-level interface-design question.
- **Problem:** Most deployed APIs expose one mask; the aggregate downstream cost of this interface decision has never been priced.
- **Hypothesis:** Hypothesis-set APIs improve downstream task metrics by application-dependent margins (large for counting/editing, small for classification), yielding a principled table of where single-mask interfaces are acceptable.
- **Why Important:** Interface standards shape the entire application ecosystem; pricing the commitment cost informs standardization.
- **Why Possibly Novel (hypothesized):** Interface-cost quantification across application portfolios appears new.
- **Minimal Experiment:** Run 5 downstream applications with argmax vs. hypothesis-set inputs; tabulate deltas; identify the interface-sensitive application classes.
- **Main Risk:** Application implementations may under-exploit hypothesis sets, underestimating the cost.
- **Cluster:** `ambiguity-multihypothesis`

### A-0233
- **Idea:** Investigate whether disagreement between granularity levels can be resolved by task context injection: conditioning mask selection on a downstream task descriptor ("for grasping" vs. "for counting") and measuring intent-alignment gains.
- **Problem:** Correct granularity is task-relative, but models resolve it context-free; the value of task conditioning is unquantified.
- **Hypothesis:** Task-descriptor conditioning (learned selection head over hypotheses) aligns granularity choices with task-appropriate ground truth substantially better than context-free selection, generalizing across unseen task descriptions.
- **Why Important:** Task-relative disambiguation is the missing layer between promptable models and applications.
- **Why Possibly Novel (hypothesized):** Task-conditioned hypothesis selection with generalization claims appears fresh.
- **Minimal Experiment:** Build task-labeled granularity GT for 4 tasks; train/evaluate selection heads; test on held-out task descriptions.
- **Main Risk:** Task descriptors may be too coarse to determine granularity reliably.
- **Cluster:** `ambiguity-multihypothesis`

### A-0234
- **Idea:** Study inter-annotator disagreement as a segmentation target: training models to output the *distribution* of human masks (not a consensus), and testing whether distribution-matched models make better downstream decisions under all aggregation rules.
- **Problem:** Consensus training discards disagreement structure; whether distribution modeling strictly dominates for downstream use is unproven.
- **Hypothesis:** Models trained to match annotator distributions (via multi-sample losses) can reproduce any consensus rule post hoc within noise, while consensus-trained models cannot recover the distribution — an asymmetry making distribution training strictly preferable at equal data.
- **Why Important:** Would settle the consensus-vs-distribution training debate for dense labels with a dominance argument.
- **Why Possibly Novel (hypothesized):** The strict-dominance framing for segmentation label distributions appears untested.
- **Minimal Experiment:** Train both paradigms on multi-annotator data; evaluate recoverability of held-out aggregation rules and downstream decision quality.
- **Main Risk:** Multi-annotator data volume may be insufficient for distribution learning.
- **Cluster:** `ambiguity-multihypothesis`

### A-0235
- **Idea:** Test whether ambiguity handling degrades under domain shift faster than accuracy: models losing their multi-hypothesis competence (collapsing to single modes) on new domains even where their argmax remains decent.
- **Problem:** Robustness studies track accuracy; the robustness of *uncertainty structure* (hypothesis diversity fidelity) is unmeasured.
- **Hypothesis:** Hypothesis-set quality (coverage of valid interpretations) degrades at several times the rate of argmax IoU under domain shift, silently breaking ambiguity-dependent workflows before accuracy alarms fire.
- **Why Important:** Ambiguity collapse is invisible to standard monitoring yet fatal for interactive and review workflows.
- **Why Possibly Novel (hypothesized):** Shift-robustness of hypothesis structure appears unstudied.
- **Minimal Experiment:** Evaluate hypothesis coverage and argmax IoU across a domain-shift ladder; compare degradation slopes.
- **Main Risk:** Valid-interpretation ground truth needed per domain — annotation-heavy.
- **Cluster:** `ambiguity-multihypothesis`

### A-0236
- **Idea:** Investigate the geometry of hypothesis space: whether SAM's mask hypotheses for a prompt lie on a low-dimensional manifold (e.g., a granularity axis) whose parameterization enables continuous granularity control as a user-facing dial.
- **Problem:** Discrete hypothesis slots may sample an underlying continuous granularity structure that, if parameterized, would offer better control than slot selection.
- **Hypothesis:** Interpolations in the decoder's hypothesis-token space produce valid intermediate-granularity masks (monotone nested regions) for most objects, evidencing a continuous internal granularity parameterization.
- **Why Important:** A granularity dial would replace hypothesis roulette with direct control — a UX and reliability upgrade.
- **Why Possibly Novel (hypothesized):** Latent granularity-axis discovery in mask decoders appears unexplored.
- **Minimal Experiment:** Interpolate hypothesis tokens; test mask validity/nestedness across interpolation; user-test a dial prototype on part-whole tasks.
- **Main Risk:** Interpolations may leave the valid-output manifold, producing artifacts.
- **Cluster:** `ambiguity-multihypothesis`

### A-0237
- **Idea:** Test ambiguity-aware evaluation: scoring predictions as correct if they match *any* human-defensible interpretation, and measuring how model rankings change relative to fixed-GT scoring.
- **Problem:** Fixed-GT scoring punishes valid alternative interpretations, distorting comparisons in unknown directions per model.
- **Hypothesis:** Under any-valid-interpretation scoring, model rankings change materially, with models penalized under fixed GT for systematic granularity styles recovering most, revealing style-vs-error confusion in current benchmarks.
- **Why Important:** Alignment of evaluation with the actual space of correct answers is foundational validity work.
- **Why Possibly Novel (hypothesized):** Any-interpretation scoring at benchmark scale appears unimplemented.
- **Minimal Experiment:** Enumerate valid interpretations on 1k prompts; rescore 8 models; analyze rank shifts and per-model recovery patterns.
- **Main Risk:** Interpretation enumeration is expensive and possibly incomplete.
- **Cluster:** `ambiguity-multihypothesis`

### A-0238
- **Idea:** Study count ambiguity in cluster objects (grapes, crowds, foliage): whether models represent "one cluster vs. many items" ambiguity at all, and how hypothesis sets behave on aggregation-ambiguous prompts.
- **Problem:** Aggregation ambiguity (collective vs. individual) is common but absent from ambiguity discussions centered on part-whole.
- **Hypothesis:** On aggregation-ambiguous prompts, current hypothesis sets almost never span the collective-individual distinction (offering only spatial variants), missing an entire ambiguity dimension humans routinely intend.
- **Why Important:** Aggregation choice changes downstream counts by orders of magnitude, silently.
- **Why Possibly Novel (hypothesized):** Aggregation-ambiguity auditing for promptable models appears new.
- **Minimal Experiment:** Curate aggregation-ambiguous prompt sets; classify hypothesis-set spans; compare against human intent distributions.
- **Main Risk:** Constructing clean aggregation-ambiguous cases needs care.
- **Cluster:** `ambiguity-multihypothesis`

### A-0239
- **Idea:** Investigate whether ambiguity signatures identify mislabeled training data: instances where a strong model's hypothesis set persistently disagrees with GT flagging annotation errors with high precision, turning ambiguity outputs into a data-cleaning instrument.
- **Problem:** Label-error detection uses loss ranking, which conflates hard-but-correct with wrong labels; hypothesis-set structure may disambiguate the two.
- **Hypothesis:** Cases where GT matches *no* model hypothesis while hypotheses agree with each other are enriched for true label errors (precision >80%), outperforming loss-based ranking at matched review budgets.
- **Why Important:** Better label-error detection compounds across every downstream training effort.
- **Why Possibly Novel (hypothesized):** Hypothesis-set-based label auditing appears untried for segmentation.
- **Minimal Experiment:** Apply the criterion to standard datasets; human-verify flagged samples; compare precision-recall of review queues against loss ranking.
- **Main Risk:** Model biases may systematically flag correct-but-unusual labels.
- **Cluster:** `ambiguity-multihypothesis`

### A-0240
- **Idea:** Test whether ambiguity can be reduced pre-model by capture guidance: instructing capture (viewpoint, framing) to minimize downstream segmentation ambiguity, quantifying how much ambiguity is capture-removable versus intrinsic.
- **Problem:** Ambiguity is treated as fixed input property; its decomposition into capture-dependent and intrinsic components is unmeasured.
- **Hypothesis:** A substantial fraction of granularity/boundary ambiguity (>40%) is removable by capture changes (closer framing, angle changes), and a viewfinder-time ambiguity predictor can guide capture effectively.
- **Why Important:** Moving ambiguity reduction to capture time is cheaper than resolving it computationally later.
- **Why Possibly Novel (hypothesized):** Capture-time ambiguity mitigation for segmentation appears unstudied.
- **Minimal Experiment:** Photograph objects under varied capture protocols; measure ambiguity metrics per protocol; train and field-test a capture-guidance predictor.
- **Main Risk:** Capture guidance is inapplicable to archival or third-party imagery.
- **Cluster:** `ambiguity-multihypothesis`

---

## Sub-cluster 17: Robustness, corruptions & distribution shift (`robustness-shift`)

### A-0241
- **Idea:** Build corruption-response fingerprints for promptable segmentation: per-model curves of performance vs. corruption type/severity, and test whether fingerprints predict which model survives a given deployment environment better than average robustness scores.
- **Problem:** Robustness is summarized as a single mean-over-corruptions number, discarding the structure that determines environment-specific survival.
- **Hypothesis:** Environment-matched fingerprint selection picks the best model for a held-out environment substantially more often than mean-robustness ranking, proving the mean is decision-insufficient.
- **Why Important:** Converts robustness benchmarking from a leaderboard into a deployment decision tool.
- **Why Possibly Novel (hypothesized):** Fingerprint-based environment matching for segmentation appears unbuilt.
- **Minimal Experiment:** Profile 8 models across a corruption battery; characterize 5 real environments' corruption statistics; test fingerprint-matched vs. mean-based selection.
- **Main Risk:** Real environments mix corruptions in ways batteries may not span.
- **Cluster:** `robustness-shift`

### A-0242
- **Idea:** Test whether prompt-based interaction masks robustness failures: interactive correction ability may fully compensate corruption-induced errors for some corruption types (recoverable) but not others (unrecoverable), splitting robustness into two operationally distinct kinds.
- **Problem:** Robustness is measured zero-shot, but deployed promptable models are corrected interactively; which corruptions remain harmful under interaction is unknown.
- **Hypothesis:** Blur/noise-induced errors are largely interaction-recoverable (clicks restore quality) while semantic corruptions (fog, low light) resist correction — because the former damage readout and the latter damage representation.
- **Why Important:** Interaction-aware robustness reprioritizes which corruptions matter for promptable deployments.
- **Why Possibly Novel (hypothesized):** Interaction-recoverability decomposition of corruption robustness appears new.
- **Minimal Experiment:** Measure clicks-to-target across corruption types/severities; classify corruptions by recoverability; verify the representation-vs-readout mechanism via probes.
- **Main Risk:** Recoverability may depend on simulated-clicker realism.
- **Cluster:** `robustness-shift`

### A-0243
- **Idea:** Investigate adversarial prompts (not images): worst-case click/box placements within valid prompting regions that minimize performance, defining certified prompt-robustness radii for promptable models.
- **Problem:** Adversarial robustness focuses on image perturbations; the prompt channel is an unexamined attack/failure surface.
- **Hypothesis:** Worst-case in-object clicks degrade IoU by >30 points on a large fraction of objects (vs. <5 for average-case), and certified radii (prompt regions with guaranteed quality) are computable via Lipschitz-style analysis of the prompt encoder.
- **Why Important:** Prompt-channel guarantees matter wherever prompts come from untrusted or noisy sources (auto-detectors, users).
- **Why Possibly Novel (hypothesized):** Certified robustness over the prompt space appears unformalized.
- **Minimal Experiment:** Optimize adversarial prompts per object; measure worst-vs-average gaps; derive and validate empirical certification bounds.
- **Main Risk:** Certification may yield vacuously small radii.
- **Cluster:** `robustness-shift`

### A-0244
- **Idea:** Study compression robustness as a deployment reality: JPEG/H.264/AV1 artifacts' effect on segmentation, testing whether codec-aware fine-tuning transfers across codecs or requires per-codec treatment.
- **Problem:** Almost all deployed images are lossy-compressed, yet robustness suites underweight codec artifacts, and codec-generalization of fixes is untested.
- **Hypothesis:** Codec artifacts cause boundary-localized errors with codec-specific signatures, and fine-tuning on one codec transfers partially within DCT-family codecs but not to learned codecs — defining codec-robustness equivalence classes.
- **Why Important:** Pipelines change codecs routinely; knowing transfer classes prevents silent regressions.
- **Why Possibly Novel (hypothesized):** Codec-transfer equivalence analysis for segmentation appears missing.
- **Minimal Experiment:** Evaluate across codecs/bitrates; fine-tune per codec; build the transfer matrix; analyze artifact signatures.
- **Main Risk:** Codec implementations vary; needs careful pipeline control.
- **Cluster:** `robustness-shift`

### A-0245
- **Idea:** Test the "shift direction asymmetry" hypothesis: models degrade differently under shifts toward higher vs. lower image quality than training (e.g., a model trained on web images tested on professional captures), revealing an unexamined asymmetry in domain-gap thinking.
- **Problem:** Domain gap is treated as symmetric distance, but degradation may be direction-dependent in systematic ways.
- **Hypothesis:** Upshift (to cleaner/higher-quality inputs than training) causes measurable degradation with a distinct signature (over-segmentation of newly visible detail), demonstrating that "better input" can be out-of-distribution.
- **Why Important:** Counterintuitive upshift failures blindside deployments that upgrade cameras.
- **Why Possibly Novel (hypothesized):** Directional shift asymmetry for segmentation appears undocumented.
- **Minimal Experiment:** Construct quality-ladder datasets of identical scenes; evaluate models trained at middle rungs in both directions; characterize asymmetric error signatures.
- **Main Risk:** Building matched multi-quality captures is logistically heavy.
- **Cluster:** `robustness-shift`

### A-0246
- **Idea:** Investigate spatially non-uniform robustness: whether corruption sensitivity varies across the image field (center vs. periphery) due to training composition bias, producing position-dependent reliability maps for VFMs.
- **Problem:** Robustness is measured image-globally; positional structure in sensitivity would matter for framing decisions and safety zones.
- **Hypothesis:** Peripheral image regions show measurably higher corruption sensitivity than central regions (center-bias inheritance), and the positional profile transfers across corruption types within a model.
- **Why Important:** Position-dependent reliability informs camera framing, cropping policies, and attention-based compute allocation.
- **Why Possibly Novel (hypothesized):** Positional robustness mapping for segmentation appears new.
- **Minimal Experiment:** Corrupt localized patches at controlled positions; map sensitivity fields per model; test cross-corruption transfer of the field.
- **Main Risk:** Object-position statistics of test data confound positional attribution.
- **Cluster:** `robustness-shift`

### A-0247
- **Idea:** Study robustness interactions: whether corruption combinations (blur+noise+low-light, as co-occur at night) degrade superadditively relative to single-corruption predictions, invalidating the single-corruption benchmark paradigm.
- **Problem:** Real degradations co-occur, but benchmarks test corruptions singly, assuming additive composition — untested for segmentation.
- **Hypothesis:** Naturalistic corruption combinations degrade performance significantly beyond additive predictions from marginals, with the interaction structure stable enough to model with pairwise terms.
- **Why Important:** If interactions dominate, the field's robustness numbers systematically overestimate deployed reliability.
- **Why Possibly Novel (hypothesized):** Interaction-structure measurement of corruption compositions appears sparse.
- **Minimal Experiment:** Evaluate a factorial corruption grid; fit additive and pairwise models to degradation; quantify interaction excess on naturalistic combinations.
- **Main Risk:** Factorial grids grow combinatorially; needs fractional designs.
- **Cluster:** `robustness-shift`

### A-0248
- **Idea:** Test whether robustness can be retrofitted through the prompt path alone: fine-tuning only the prompt encoder to compensate for known corruptions (encoding "this image is foggy" implicitly), leaving the heavy encoder untouched.
- **Problem:** Robustness fine-tuning targets the encoder at high cost; the prompt path is a tiny, unexplored intervention point for conditioning on degradation.
- **Hypothesis:** Corruption-conditioned prompt-encoder tuning recovers a meaningful fraction (>40%) of corruption-induced loss at <1% of encoder-tuning parameters, because much of the loss is decoder misreading of shifted features rather than lost information.
- **Why Important:** Ultra-cheap robustness retrofits would change deployment economics for edge fleets.
- **Why Possibly Novel (hypothesized):** Prompt-path robustness retrofitting appears untried.
- **Minimal Experiment:** Tune prompt encoders per corruption family; compare recovery against LoRA-encoder baselines at matched and unmatched budgets.
- **Main Risk:** Information genuinely destroyed by corruption caps prompt-path recovery.
- **Cluster:** `robustness-shift`

### A-0249
- **Idea:** Investigate "robustness forgetting" during standard fine-tuning: whether domain fine-tunes silently discard the pretrained model's corruption robustness even within the target domain, and whether robustness must be explicitly rehearsed.
- **Problem:** Fine-tuning evaluations use clean target data, potentially missing that adapted models became brittle to corruptions the base model handled.
- **Hypothesis:** Domain fine-tuning reduces corruption robustness within the target domain itself (clean-target overfitting), and mixing minimal corrupted target data (5%) fully preserves it — a free fix once measured.
- **Why Important:** Deployed fine-tunes face corrupted inputs; silent robustness loss is a production trap.
- **Why Possibly Novel (hypothesized):** Within-domain robustness forgetting under fine-tuning appears unmeasured for segmentation.
- **Minimal Experiment:** Fine-tune on clean domains; evaluate corrupted-domain suites before/after; test corruption-mixing mitigation curves.
- **Main Risk:** Effect may vary strongly with fine-tuning depth, needing a breadth of configurations.
- **Cluster:** `robustness-shift`

### A-0250
- **Idea:** Test weather/lighting counterfactuals via controlled re-rendering: using relighting models to generate the same scene under many conditions, isolating illumination robustness from all content confounds present in natural weather datasets.
- **Problem:** Natural adverse-condition datasets confound weather with location/content; controlled counterfactual illumination evaluation is missing at scale.
- **Hypothesis:** Under content-controlled relighting, segmentation degradation attributes mostly to a low-dimensional set of illumination factors (shadow hardness, dynamic range compression), enabling targeted augmentation that closes most of the naturally measured gap.
- **Why Important:** Correct attribution of "night degradation" determines whether data, sensors, or preprocessing is the fix.
- **Why Possibly Novel (hypothesized):** Counterfactual-relighting robustness attribution appears fresh for segmentation.
- **Minimal Experiment:** Relight a scene corpus along controlled factors; regress degradation on factors; validate targeted augmentation on real night data.
- **Main Risk:** Relighting-model artifacts may contaminate the counterfactuals.
- **Cluster:** `robustness-shift`

### A-0251
- **Idea:** Study robustness of the prompt-image binding: whether corruptions disrupt the model's association between prompt location and image content (clicks "landing" on wrong features under distortion) as a distinct failure channel from feature degradation.
- **Problem:** Corruption failures are attributed to feature quality; binding failures (prompt mislocalization in feature space) are an unseparated channel.
- **Hypothesis:** Geometric distortions (rolling shutter, lens warp) cause binding errors identifiable by prompt-conditioned attention landing offset from the click, and binding errors respond to prompt-coordinate correction while feature errors do not — separating the channels.
- **Why Important:** Distinct channels need distinct fixes (geometric calibration vs. robust features).
- **Why Possibly Novel (hypothesized):** Prompt-binding robustness as a separate channel appears unstudied.
- **Minimal Experiment:** Apply parametric geometric distortions; measure attention-landing offsets vs. mask errors; test coordinate-correction recovery.
- **Main Risk:** Attention landing is an imperfect proxy for binding.
- **Cluster:** `robustness-shift`

### A-0252
- **Idea:** Test extreme-ratio safety: model behavior on inputs wildly outside spec (16:1 panoramas, 1000×20 strips, gigapixel crops), characterizing failure modes at input-geometry extremes that pipelines actually produce.
- **Problem:** Preprocessing bugs and unusual sensors produce extreme geometries; model behavior there is unknown and possibly silently wrong.
- **Hypothesis:** Beyond aspect-ratio thresholds, models fail non-obviously (plausible masks with systematic offsets) rather than obviously, making extreme-geometry inputs a silent-corruption class needing input validation with measured thresholds.
- **Why Important:** Silent plausible-but-wrong failures are the worst deployment class; spec boundaries should be measured, not guessed.
- **Why Possibly Novel (hypothesized):** Input-geometry failure-mode mapping appears undone.
- **Minimal Experiment:** Evaluate across aspect/scale grids with GT; classify failure obviousness; derive validated input-spec boundaries per model.
- **Main Risk:** Findings are model-version-specific; needs an automated re-testing harness.
- **Cluster:** `robustness-shift`

### A-0253
- **Idea:** Investigate whether self-supervised test-time objectives (entropy, consistency) used for adaptation can be gamed by the environment: distribution shifts under which TTA objectives improve while true accuracy collapses, mapping the safety envelope of test-time adaptation for segmentation.
- **Problem:** TTA optimizes proxies; shifts that decouple proxy from accuracy would make TTA actively harmful, but the decoupling conditions are unmapped.
- **Hypothesis:** Structured shifts (e.g., texture-uniform scenes) cause entropy-minimizing TTA to confidently collapse masks (proxy improves, accuracy collapses), and a proxy-accuracy divergence detector based on prediction topology flags these cases.
- **Why Important:** TTA is entering deployments; its failure envelope must be characterized before trust.
- **Why Possibly Novel (hypothesized):** Adversarial-environment analysis of segmentation TTA appears sparse.
- **Minimal Experiment:** Run TTA methods across a shift taxonomy; identify divergence cases; build and validate the divergence detector.
- **Main Risk:** Detector may not generalize across TTA methods.
- **Cluster:** `robustness-shift`

### A-0254
- **Idea:** Study multi-frame consistency as a robustness resource: for near-static cameras, whether enforcing temporal self-consistency at inference recovers single-frame corruption losses without any adaptation, quantifying the "free redundancy" available in video streams.
- **Problem:** Frame redundancy is discarded by per-frame inference; its recoverable value under corruption is unquantified for promptable models.
- **Hypothesis:** Consistency-filtered predictions (temporal median of aligned masks) recover ≥50% of corruption-induced loss for stochastic corruptions (noise, compression flicker) but ≤10% for static corruptions (fog), cleanly splitting corruption types by temporal recoverability.
- **Why Important:** Free robustness from redundancy changes cost-benefit calculations for edge video systems.
- **Why Possibly Novel (hypothesized):** Temporal-recoverability decomposition of corruption loss appears new.
- **Minimal Experiment:** Corrupt video streams; compare per-frame vs. consistency-filtered outputs by corruption type; map recoverability.
- **Main Risk:** Camera/scene motion breaks alignment assumptions.
- **Cluster:** `robustness-shift`

### A-0255
- **Idea:** Test robustness certification transfer: whether randomized-smoothing-style certificates derived for classification transfer meaningfully to mask outputs (certifying pixel sets stable under bounded perturbations), and how large certified regions are for real VFMs.
- **Problem:** Certification theory is classification-centric; certified guarantees for structured mask outputs are underdeveloped and their practical size unknown.
- **Hypothesis:** Pixelwise smoothing certificates yield non-vacuous certified stable regions covering the majority of interior pixels but near-zero boundary bands, formalizing that only mask interiors are certifiable with current techniques.
- **Why Important:** Establishes what safety-critical users can and cannot get certified today, directing certification research.
- **Why Possibly Novel (hypothesized):** Practical certification-size measurement for promptable masks appears missing.
- **Minimal Experiment:** Implement smoothed inference for SAM-class models; compute certified-pixel maps across datasets; report certified-fraction statistics vs. perturbation budgets.
- **Main Risk:** Smoothing degrades base performance, complicating fair reporting.
- **Cluster:** `robustness-shift`

---

## Sub-cluster 18: Open-vocabulary & language grounding for segmentation (`open-vocab-grounding`)

### A-0256
- **Idea:** Test whether referring-expression failures decompose along linguistic structure: quantifier failures ("all", "two of"), comparative failures ("the larger"), and negation failures having distinct error signatures and different scaling behavior.
- **Problem:** Referring segmentation errors are aggregated; the linguistic-construct-specific failure structure that would guide data/architecture fixes is unmapped.
- **Hypothesis:** Comparatives and negations fail at rates far exceeding matched-complexity attributive expressions, and their failures do not improve across model scale ladders while attributive failures do — locating a scale-resistant linguistic core.
- **Why Important:** Identifies which language capabilities need mechanisms rather than scale.
- **Why Possibly Novel (hypothesized):** Construct-resolved scaling analysis for referring segmentation appears missing.
- **Minimal Experiment:** Build construct-stratified referring benchmarks with matched visual difficulty; evaluate across scales; compare construct-specific trends.
- **Main Risk:** Matching visual difficulty across constructs is delicate.
- **Cluster:** `open-vocab-grounding`

### A-0257
- **Idea:** Investigate the "reporting bias inheritance" in grounded segmentation: whether visually groundable attributes that people rarely mention (default colors, typical sizes) are disproportionately ungroundable, tracing model gaps to language-data reporting statistics.
- **Problem:** Text supervision reflects what people say, not what is visible; the transfer of this reporting bias into grounding capability is unquantified.
- **Hypothesis:** Grounding accuracy for attribute-object pairs correlates with the pair's text-corpus mention rate beyond visual frequency, demonstrating language-side reporting bias as an independent cause of grounding failure.
- **Why Important:** Attributes the failure to the right data stream (text vs. image), directing collection efforts.
- **Why Possibly Novel (hypothesized):** Reporting-bias attribution for segmentation grounding appears fresh.
- **Minimal Experiment:** Estimate mention rates and visual frequencies for attribute-object pairs; evaluate grounding per pair; run the partial-correlation analysis.
- **Main Risk:** Corpus mention statistics approximate the actual training text imperfectly.
- **Cluster:** `open-vocab-grounding`

### A-0258
- **Idea:** Study spatial-language grounding resolution: how precisely models resolve spatial prepositions ("on", "under", "leaning against") into segmentation decisions, and whether errors reflect coarse bounding-region approximations of genuinely relational concepts.
- **Problem:** Spatial prepositions have configurational semantics; models may implement them as coarse spatial priors, failing predictable configurations.
- **Hypothesis:** Model behavior on preposition-guided segmentation matches a simple relative-bounding-box template (not configurational semantics), mispredicting exactly the configurations where template and true relation diverge (e.g., "under" with overhangs).
- **Why Important:** Configuration-level failures matter for robotics instruction following; template detection reveals the mechanism.
- **Why Possibly Novel (hypothesized):** Template-vs-configuration diagnosis of spatial grounding appears new for segmentation.
- **Minimal Experiment:** Construct configuration-controlled scenes dissociating templates from true relations; measure model agreement with each account.
- **Main Risk:** Scene construction (real or rendered) at controlled configurations is labor-intensive.
- **Cluster:** `open-vocab-grounding`

### A-0259
- **Idea:** Test cross-lingual grounding parity: whether open-vocabulary segmentation quality for concept translations tracks the training text's language distribution, and whether visual grounding transfers across languages through shared embeddings or must be relearned per language.
- **Problem:** Non-English users face unquantified capability gaps, and the transfer mechanism (shared visual anchors vs. per-language learning) is undetermined.
- **Hypothesis:** Grounding quality gaps across languages exceed what embedding-similarity to English predicts, indicating per-language grounding learning rather than free transfer through shared space.
- **Why Important:** Parity measurement and mechanism identification guide multilingual training investment.
- **Why Possibly Novel (hypothesized):** Mechanistic cross-lingual analysis for segmentation grounding appears sparse.
- **Minimal Experiment:** Evaluate concept segmentation across 10 languages with matched concepts; regress gaps on language-data share and embedding alignment.
- **Main Risk:** Translation quality of evaluation concepts confounds capability measurement.
- **Cluster:** `open-vocab-grounding`

### A-0260
- **Idea:** Investigate description-length scaling: whether longer, more specific referring expressions monotonically improve grounding or exhibit an inverted-U (over-specification confusing models), and locate the optimal specificity point.
- **Problem:** Users don't know how much detail to give; the specificity-performance relationship is uncharacterized.
- **Hypothesis:** Grounding accuracy peaks at intermediate description lengths and declines with over-specification, because models mis-integrate redundant attributes into conjunctive constraints that spuriously fail.
- **Why Important:** Yields concrete prompting guidance and reveals the constraint-integration mechanism.
- **Why Possibly Novel (hypothesized):** Specificity-response curves for referring segmentation appear unmeasured.
- **Minimal Experiment:** Generate specificity ladders for fixed targets (1–10 attributes); measure accuracy curves; analyze failure modes at the over-specified end.
- **Main Risk:** Generated descriptions may introduce naturalness confounds along the ladder.
- **Cluster:** `open-vocab-grounding`

### A-0261
- **Idea:** Study grounding under referential ambiguity: when an expression matches multiple instances, do models exhibit consistent selection biases (leftmost, largest, most central), and do users' expectations match those biases?
- **Problem:** Ambiguous references are resolved silently by unknown model biases that may systematically mismatch user expectations.
- **Hypothesis:** Models show strong consistent selection biases (hypothesized: largest/most-central) that align with human expectations for only some ambiguity types, with mismatches concentrated in spatial-scanning conventions (humans expect reading-order).
- **Why Important:** Bias-expectation mismatches cause silent wrong selections in every language-driven interface.
- **Why Possibly Novel (hypothesized):** Bias-vs-expectation alignment measurement appears new.
- **Minimal Experiment:** Curate multi-match scenes; measure model selection distributions; collect human expectation distributions; compare alignment by ambiguity type.
- **Main Risk:** Human expectations vary culturally, complicating the reference standard.
- **Cluster:** `open-vocab-grounding`

### A-0262
- **Idea:** Test compositional binding errors in grounded segmentation: for "red cup next to blue plate," measuring attribute-object binding failure rates (segmenting the blue cup) as a function of scene distractor structure — the segmentation version of the binding problem.
- **Problem:** Binding failures are documented for VLM classification; their structure in dense grounding (where output reveals the bound entity precisely) is richer and unmeasured.
- **Hypothesis:** Binding failures grow with distractor attribute-sharing in a pattern matching a similarity-based retrieval account (not random confusion), and the mask output localizes the failure to retrieval rather than segmentation.
- **Why Important:** Dense outputs make binding failures precisely observable, offering the cleanest testbed for a core cognitive-architecture question.
- **Why Possibly Novel (hypothesized):** Dense-output binding analysis appears underexploited.
- **Minimal Experiment:** Construct distractor-controlled scenes; measure binding-failure rates vs. distractor structure; fit retrieval-account predictions.
- **Main Risk:** Scene construction bias may favor one theoretical account.
- **Cluster:** `open-vocab-grounding`

### A-0263
- **Idea:** Investigate whether grounded models can segment by function ("something to cut with") versus by name, and whether function-grounding failures reflect missing affordance representations or missing lexical mappings.
- **Problem:** Functional queries are natural for users and robots, but the failure locus (visual affordance representation vs. language mapping) is undetermined.
- **Hypothesis:** Models fail function queries at high rates even for objects they segment correctly by name, and intermediate-layer probes show affordance information present but unaccessed by language — locating the failure in the mapping, not the representation.
- **Why Important:** Locating the failure determines whether robotics needs new pretraining or just mapping layers.
- **Why Possibly Novel (hypothesized):** Failure-locus analysis for functional grounding appears new.
- **Minimal Experiment:** Build name-vs-function query pairs; measure gaps; probe intermediate features for affordance decodability; test a small mapping layer trained on limited affordance data.
- **Main Risk:** Affordance ground truth is context-dependent and partly subjective.
- **Cluster:** `open-vocab-grounding`

### A-0264
- **Idea:** Study temporal referring in video ("the car that just turned left"): whether video segmentation models can ground event-anchored references, and if failures stem from missing event memory rather than language parsing.
- **Problem:** Event-anchored reference requires binding language to temporal episodes — a capability whose bottleneck (memory vs. parsing) is unidentified.
- **Hypothesis:** Models parse event language correctly (verified via text-side probes) but cannot bind it to visual episodes beyond a few seconds back, localizing the failure in temporal binding rather than language understanding.
- **Why Important:** Event grounding is essential for surveillance/robotics queries; the bottleneck determines the architecture fix.
- **Why Possibly Novel (hypothesized):** Bottleneck localization for temporal referring segmentation appears fresh.
- **Minimal Experiment:** Build event-anchored referring benchmarks with controlled anchor-to-query delays; decompose failures via language-probe vs. temporal-window ablations.
- **Main Risk:** Constructing unambiguous event references at scale is expensive.
- **Cluster:** `open-vocab-grounding`

### A-0265
- **Idea:** Test whether text-prompt engineering transfers across grounded-segmentation models: prompt templates optimized on one model helping or hurting others, quantifying the portability of prompt-engineering investment in the vision-language space.
- **Problem:** Organizations invest in prompt libraries whose cross-model portability is unknown, creating hidden lock-in.
- **Hypothesis:** Optimized template gains transfer <40% across model families (near-zero across objective families), and transferability is predictable from text-encoder similarity — making prompt investment effectively model-specific.
- **Why Important:** Portability economics shape build-vs-buy and upgrade decisions across the industry.
- **Why Possibly Novel (hypothesized):** Prompt-portability quantification for grounded segmentation appears absent.
- **Minimal Experiment:** Optimize templates per model on fixed tasks; cross-evaluate the template×model matrix; regress transfer on encoder similarity.
- **Main Risk:** Template optimization method choices may drive portability conclusions.
- **Cluster:** `open-vocab-grounding`

### A-0266
- **Idea:** Investigate vocabulary-free segmentation evaluation: measuring open-vocabulary models against exhaustive *unnamed* region annotations (is every coherent region segmentable by *some* query?) to separate vocabulary coverage from segmentation coverage.
- **Problem:** Open-vocab evaluation is gated by the evaluator's label vocabulary, conflating "model can't segment it" with "nobody named it."
- **Hypothesis:** A significant fraction of coherent regions (human-delineated, unnamed) are unreachable by any natural-language query for current models, quantifying a "nameability gap" distinct from mask-quality limits.
- **Why Important:** The nameability gap bounds language-driven interfaces fundamentally and is invisible to current benchmarks.
- **Why Possibly Novel (hypothesized):** Nameability-gap measurement appears unattempted.
- **Minimal Experiment:** Exhaustively region-annotate images without names; crowdsource query attempts per region; measure the unreachable fraction and its correlates.
- **Main Risk:** "Any query" is human-crowdsourced, hence lower-bounded imperfectly.
- **Cluster:** `open-vocab-grounding`

### A-0267
- **Idea:** Study negation acquisition through contrastive fine-tuning: whether targeted "X but not Y" training generalizes negation compositionally to unseen concept pairs, or memorizes pair-specific exclusions — testing the learnability of a logical operator in grounding.
- **Problem:** Whether logical operators over visual concepts are learnable as generalizable operations (vs. pair memorization) is a foundational open question with practical stakes.
- **Hypothesis:** Negation fine-tuning on N concept pairs generalizes to held-out pairs with accuracy scaling in N (operator learning), rather than remaining at baseline (memorization), with a measurable sample-efficiency constant.
- **Why Important:** Operator learnability determines whether compositional querying needs architectural logic or just data.
- **Why Possibly Novel (hypothesized):** Held-out-pair generalization tests for visual negation appear rare.
- **Minimal Experiment:** Fine-tune with negation data at varying pair counts; evaluate held-out pair negation; fit generalization-vs-N curves.
- **Main Risk:** Negation data construction may leak surface heuristics.
- **Cluster:** `open-vocab-grounding`

### A-0268
- **Idea:** Test attribute grounding density: whether models ground attributes only at object level (the whole cup is "red") or at true attribute extent (only the red stripe), measuring attribute-extent fidelity as a distinct capability from object segmentation.
- **Problem:** Attribute queries return object masks by habit; whether models can localize attribute extents within objects is untested.
- **Hypothesis:** Current grounded segmenters return object-level masks for sub-object attribute queries in the vast majority of cases, and attribute-extent fidelity requires (and responds to) part-level contrastive supervision — a measurable missing capability.
- **Why Important:** Attribute-extent localization matters for inspection, retail, and editing applications.
- **Why Possibly Novel (hypothesized):** Attribute-extent fidelity measurement appears new.
- **Minimal Experiment:** Annotate attribute extents distinct from object masks; evaluate models on extent-vs-object responses; test part-supervised fine-tuning.
- **Main Risk:** Attribute-extent ground truth involves genuinely fuzzy boundaries.
- **Cluster:** `open-vocab-grounding`

### A-0269
- **Idea:** Investigate query-image feedback loops in retrieval-then-segment systems: whether errors correlate across the retrieval and segmentation stages (shared embeddings), defeating the error-independence assumption behind pipeline reliability estimates.
- **Problem:** System reliability calculations assume stage independence; shared foundation embeddings likely correlate stage errors in unmeasured magnitude.
- **Hypothesis:** Retrieval and segmentation errors on the same query-image pairs are strongly positively correlated when stages share encoders, inflating true system error rates well above independence-based estimates, and encoder diversification restores near-independence.
- **Why Important:** Correct system-reliability math for the compound VFM systems everyone is building.
- **Why Possibly Novel (hypothesized):** Stage-error correlation measurement in VFM pipelines appears new.
- **Minimal Experiment:** Build retrieve-then-segment systems with shared vs. diverse encoders; measure stage-error correlations and system-level reliability against predictions.
- **Main Risk:** Correlation depends on task mix; needs several workloads.
- **Cluster:** `open-vocab-grounding`

### A-0270
- **Idea:** Study "grounded hallucination" bidirectionality: whether models that hallucinate segmentation for absent concepts also fail to segment present-but-atypical instances, testing if both errors share a single prototype-matching mechanism with one threshold.
- **Problem:** False positives (hallucination) and false negatives (atypicality misses) are treated as separate problems; a shared mechanism would unify their fixes.
- **Hypothesis:** Per-concept hallucination rates and atypicality-miss rates are strongly correlated across concepts and both move together under prototype-threshold interventions, evidencing one underlying similarity threshold rather than two mechanisms.
- **Why Important:** A single-mechanism account halves the engineering surface for reliability work.
- **Why Possibly Novel (hypothesized):** Unified-mechanism testing for grounding errors appears fresh.
- **Minimal Experiment:** Measure both error rates per concept across corpora; test threshold interventions; evaluate joint-movement predictions.
- **Main Risk:** Correlation may arise from concept difficulty confounds rather than shared mechanism.
- **Cluster:** `open-vocab-grounding`

---

## Sub-cluster 19: Data-centric biases & pseudo-label loops (`data-centric-bias`)

### A-0271
- **Idea:** Characterize the annotation-pipeline fingerprint of SA-1B-scale datasets: measurable statistical signatures left by the model-in-the-loop collection process (mask complexity ceilings, boundary smoothness), and their inheritance by every model trained on the data.
- **Problem:** Model-assisted dataset construction bakes the assisting model's biases into the data; the fingerprint's structure and downstream inheritance are unquantified.
- **Hypothesis:** SA-1B-style masks show detectable generator signatures (curvature spectra, size-complexity relationships) diverging from fully human datasets, and models trained on them reproduce these signatures on new images at measurable strength.
- **Why Important:** Dataset fingerprints propagate one generation's limits into the next — the central risk of the auto-labeling era.
- **Why Possibly Novel (hypothesized):** Generator-fingerprint inheritance measurement appears undone for segmentation data.
- **Minimal Experiment:** Compare mask-statistic distributions between assisted and manual datasets; train matched models on each; test signature reproduction on shared test images.
- **Main Risk:** Content differences between datasets confound pipeline signatures.
- **Cluster:** `data-centric-bias`

### A-0272
- **Idea:** Test model-collapse dynamics for segmentation self-training: iterating "train on own outputs" generations and measuring which mask properties degrade first, at what rate, and whether small human-data injections arrest collapse.
- **Problem:** Segmentation-specific collapse dynamics (what degrades: boundaries, rare classes, diversity?) under recursive pseudo-labeling are unmeasured.
- **Hypothesis:** Collapse manifests first as boundary-detail loss and rare-morphology disappearance (before mean IoU moves), with degradation rate proportional to the pseudo-label fraction and arrested by ≥5% human data per generation.
- **Why Important:** The field is entering recursive-data regimes; collapse early-warning indicators are needed before quality is silently lost.
- **Why Possibly Novel (hypothesized):** Property-resolved collapse tracking for dense prediction appears new.
- **Minimal Experiment:** Run 5 self-training generations with controlled human-data fractions; track boundary/diversity/rare-class metrics per generation.
- **Main Risk:** Compute cost of multi-generation training at meaningful scale.
- **Cluster:** `data-centric-bias`

### A-0273
- **Idea:** Study "easy-mask bias" in auto-curated datasets: confidence-filtered pseudo-labels over-representing easy objects, and whether models trained on such data develop measurable difficulty avoidance (worse-than-expected performance exactly on hard cases).
- **Problem:** Confidence filtering is standard hygiene, but its selection effect on the difficulty distribution — and the resulting learned bias — is unmeasured.
- **Hypothesis:** Confidence-filtered training produces models whose difficulty-performance curve is steeper than matched models trained on unfiltered noisy data, i.e., filtering trades noise robustness for hard-case competence in a quantifiable exchange.
- **Why Important:** The standard practice may be optimizing the wrong trade; measuring the exchange rate informs curation policy.
- **Why Possibly Novel (hypothesized):** Difficulty-distribution selection effects of confidence filtering appear unstudied for segmentation.
- **Minimal Experiment:** Train on filtered vs. noise-matched unfiltered pseudo-labels; compare difficulty-stratified performance curves.
- **Main Risk:** Difficulty quantification itself requires a model, risking circularity.
- **Cluster:** `data-centric-bias`

### A-0274
- **Idea:** Investigate geographic/economic coverage bias in segmentation data through the object lens: household objects, vehicles, and street furniture from under-represented regions failing at rates predictable from data-source geography.
- **Problem:** Geographic bias is documented for classification; its object-level segmentation structure (which objects, which failure types) is unmapped.
- **Hypothesis:** Region-specific object variants (cookware, vehicles, infrastructure) show boundary and recognition failures scaling with source-data geographic skew, and failures concentrate in category-atypical shapes rather than textures.
- **Why Important:** Segmentation ships in global products; object-level bias maps enable targeted data repair.
- **Why Possibly Novel (hypothesized):** Object-level geographic failure mapping for segmentation appears sparse.
- **Minimal Experiment:** Assemble geographically stratified object imagery; evaluate models; regress failures on estimated data-source geography; classify failure types.
- **Main Risk:** Geographic data-source estimates for foundation datasets are rough.
- **Cluster:** `data-centric-bias`

### A-0275
- **Idea:** Test the marginal value of human annotation in the foundation era: on which data strata do human labels still beat model-generated labels for training (as measured by downstream gains per label dollar), and where has the crossover already happened?
- **Problem:** Annotation budgets are allocated by habit; the human-vs-model label value frontier by stratum is unmeasured.
- **Hypothesis:** Human labels retain positive marginal value only on identifiable strata (ambiguous boundaries, rare morphologies, small objects), with the value crossover predictable by model self-disagreement — enabling disagreement-directed human labeling.
- **Why Important:** Reallocating annotation budgets by measured value could multiply effective dataset quality per dollar.
- **Why Possibly Novel (hypothesized):** Stratum-resolved label-value measurement appears absent.
- **Minimal Experiment:** Train with stratum-swapped label sources (human vs. model per stratum); measure downstream deltas per stratum; validate disagreement-based targeting.
- **Main Risk:** Stratum interactions may complicate clean attribution.
- **Cluster:** `data-centric-bias`

### A-0276
- **Idea:** Study duplication effects in web-scale segmentation corpora: near-duplicate scenes with slightly different auto-labels acting as label noise amplifiers, and whether dedup-with-label-reconciliation beats plain dedup.
- **Problem:** Near-duplicates are common in web corpora; conflicting labels on duplicates create a specific noise structure whose training effect is unstudied for dense labels.
- **Hypothesis:** Conflicting near-duplicate labels degrade boundary consistency measurably more than equivalent random noise (models oscillate between conventions), and reconciling labels across duplicate clusters before training recovers the loss.
- **Why Important:** A concrete, fixable corpus pathology at the scale where fixing matters.
- **Why Possibly Novel (hypothesized):** Duplicate-conflict noise analysis for segmentation appears new.
- **Minimal Experiment:** Inject controlled duplicate-conflict structures; compare against matched random noise; test reconciliation preprocessing.
- **Main Risk:** Synthetic conflict structure may differ from natural duplication patterns.
- **Cluster:** `data-centric-bias`

### A-0277
- **Idea:** Investigate class co-occurrence scaffolding: whether models can only segment certain classes in their habitual context (ship needs water), quantifying context dependence per class and testing context-free data augmentation as the cure.
- **Problem:** Context dependence is anecdotal; per-class quantification and its data-side cause (co-occurrence statistics) need joint measurement.
- **Hypothesis:** Per-class context dependence (performance drop under context swap) is predicted by training co-occurrence entropy (low-entropy classes are context-bound), and targeted decontextualized augmentation reduces dependence without hurting in-context performance.
- **Why Important:** Context-bound classes fail exactly in the unusual scenes where detection matters (accidents, anomalies).
- **Why Possibly Novel (hypothesized):** Co-occurrence-entropy prediction of context dependence appears untested for segmentation.
- **Minimal Experiment:** Measure context-swap degradation per class; regress on co-occurrence entropy; run the augmentation intervention on the most context-bound classes.
- **Main Risk:** Context-swap composites introduce compositing artifacts.
- **Cluster:** `data-centric-bias`

### A-0278
- **Idea:** Test temporal data drift within training corpora: whether models weight recent-era imagery styles over older ones (or vice versa) beyond their corpus proportions, revealing implicit temporal weighting in training dynamics.
- **Problem:** Corpora span decades of imagery styles; whether training equalizes, recency-weights, or archaism-weights styles is unknown.
- **Hypothesis:** Per-era performance deviates from corpus-proportion predictions in a consistent direction (hypothesized: high-frequency modern styles dominate learning), quantifiable by era-stratified evaluation against era-stratified corpus statistics.
- **Why Important:** Archival applications (heritage digitization, medical archives) depend on knowing era-related performance structure.
- **Why Possibly Novel (hypothesized):** Era-weighting analysis of vision training appears new.
- **Minimal Experiment:** Stratify evaluation by capture era; compare performance profile against corpus era composition; test on models with known corpus vintages.
- **Main Risk:** Era correlates with content and resolution, needing careful controls.
- **Cluster:** `data-centric-bias`

### A-0279
- **Idea:** Study the "benchmark gravity" effect on data collection: whether new segmentation datasets increasingly resemble existing benchmarks statistically (convergent curation), shrinking the effective diversity of the evaluation ecosystem over time.
- **Problem:** Dataset builders calibrate against existing benchmarks, potentially homogenizing the data ecosystem — an unmeasured systemic drift.
- **Hypothesis:** Distributional distance between new datasets and the benchmark centroid has decreased over publication years (controlling for domain), evidencing convergent curation that inflates cross-dataset generalization estimates.
- **Why Important:** Ecosystem homogenization silently converts "cross-dataset generalization" into within-cluster interpolation.
- **Why Possibly Novel (hypothesized):** Longitudinal curation-convergence analysis appears undone.
- **Minimal Experiment:** Embed datasets by year of release in a common statistic space; test centroid-distance trends; correlate with reported generalization gaps.
- **Main Risk:** Genuine world homogenization (more phone photos) confounds curation effects.
- **Cluster:** `data-centric-bias`

### A-0280
- **Idea:** Test synthetic-data fingerprint leakage: whether models trained partly on rendered/generated imagery acquire detectable behavioral signatures on real data (e.g., expecting rendering-typical lighting), and whether signature strength predicts real-world degradation.
- **Problem:** Synthetic data enters most pipelines now; its behavioral residue on real-data performance lacks measurement instruments.
- **Hypothesis:** Synthetic-trained models show characteristic error patterns on real images (shadow-boundary handling, specular treatment) whose strength scales with synthetic fraction and predicts real-domain deficits, enabling a fingerprint-based synthetic-exposure audit of third-party models.
- **Why Important:** Auditing tools for training-data composition of black-box models serve procurement and safety.
- **Why Possibly Novel (hypothesized):** Behavioral synthetic-exposure audits appear undeveloped.
- **Minimal Experiment:** Train with controlled synthetic fractions; identify discriminative behavioral signatures; validate the audit on held-out models.
- **Main Risk:** Signatures may be renderer-specific, limiting audit generality.
- **Cluster:** `data-centric-bias`

### A-0281
- **Idea:** Investigate active-learning failure at foundation scale: whether classical uncertainty-based acquisition selects redundant or pathological samples when the labeler is a model-assisted pipeline, and design acquisition functions aware of the assistant's bias.
- **Problem:** Active learning theory assumes independent labelers; with model-assisted labeling, acquisition and labeling biases interact in unstudied ways.
- **Hypothesis:** Uncertainty-based acquisition preferentially selects samples where the labeling assistant also fails, importing correlated label errors precisely on the acquired set and negating expected gains — measurable as an acquisition-labeler correlation penalty.
- **Why Important:** Active learning and assisted labeling are combined everywhere; their interaction may quietly nullify both.
- **Why Possibly Novel (hypothesized):** Acquisition-assistant interaction analysis appears new.
- **Minimal Experiment:** Simulate AL loops with assistant-labeled acquisitions vs. oracle labels; measure the correlation penalty; test decorrelated acquisition designs.
- **Main Risk:** Simulation fidelity to real assisted-labeling error structure.
- **Cluster:** `data-centric-bias`

### A-0282
- **Idea:** Study mask-quality stratification of training value: whether a small fraction of very-high-quality masks contributes disproportionately to boundary competence, supporting a "quality-pyramid" data strategy over uniform quality.
- **Problem:** Data budgets buy either many rough masks or few precise ones; the marginal-value structure across the quality spectrum is unmeasured for dense prediction.
- **Hypothesis:** Boundary competence scales primarily with the volume of top-quality masks (matting-grade), largely independent of rough-mask volume beyond a threshold — implying pyramid budgets dominate uniform budgets at fixed cost.
- **Why Important:** Directly optimizes the largest cost line in segmentation model development.
- **Why Possibly Novel (hypothesized):** Quality-stratified marginal-value curves appear unmeasured.
- **Minimal Experiment:** Train on controlled quality mixtures at fixed budgets; fit per-capability value curves across mixtures; identify optimal pyramids.
- **Main Risk:** Quality-cost models vary across annotation vendors, affecting the budget mapping.
- **Cluster:** `data-centric-bias`

### A-0283
- **Idea:** Test cross-generation feedback risk in deployed annotation tools: whether datasets annotated with SAM-assisted tools produce models whose errors correlate with SAM's, creating an ecosystem-wide error monoculture measurable today.
- **Problem:** One assistant model now touches a large share of new datasets; the resulting inter-dataset error correlation is unmeasured systemic risk.
- **Hypothesis:** Models trained on independent datasets that share SAM-assisted provenance exhibit significantly correlated errors on stress cases (relative to models from manually annotated data), demonstrating monoculture propagation through the tool layer.
- **Why Important:** Error monoculture undermines redundancy assumptions across the entire vision ecosystem.
- **Why Possibly Novel (hypothesized):** Tool-layer monoculture measurement appears unattempted.
- **Minimal Experiment:** Gather datasets with documented annotation tooling; train matched models; compare cross-dataset error correlations by tool provenance.
- **Main Risk:** Provenance documentation is sparse; confounds abound.
- **Cluster:** `data-centric-bias`

### A-0284
- **Idea:** Investigate optimal noise structure for mask training: whether structured label noise (systematic margins) damages learning more or less than unstructured noise at equal magnitude, informing which annotation errors are worth fixing.
- **Problem:** Annotation QA treats all errors alike; learning theory suggests structured and random noise have different costs, unquantified for dense labels.
- **Hypothesis:** Systematic noise (consistent over-tight margins) is learned as convention (recoverable by output calibration) while random noise of equal magnitude irreversibly blurs boundary learning — so QA should prioritize consistency over correctness.
- **Why Important:** Reorders annotation QA priorities with direct cost implications.
- **Why Possibly Novel (hypothesized):** Structured-vs-random noise asymmetry for mask learning appears untested.
- **Minimal Experiment:** Train on controlled noise types at matched magnitudes; measure recoverable vs. irrecoverable degradation; validate the calibration recovery for systematic noise.
- **Main Risk:** Real annotation noise mixes both types, complicating translation to practice.
- **Cluster:** `data-centric-bias`

### A-0285
- **Idea:** Study data ordering effects at scale: whether curriculum (easy-to-hard) vs. anti-curriculum vs. random data ordering during VFM pretraining changes final capability profiles (not just speed), testing order-dependence of what is ultimately learned.
- **Problem:** Ordering is assumed to affect convergence speed only; permanent capability effects at foundation scale are unverified.
- **Hypothesis:** Ordering leaves permanent capability signatures at fixed final loss (curriculum favoring boundary precision, anti-curriculum favoring hard-case recall), demonstrating path dependence in foundation training.
- **Why Important:** If path dependence is real, data ordering becomes a free capability-shaping lever.
- **Why Possibly Novel (hypothesized):** Permanent-effect ordering studies at meaningful scale appear rare for vision.
- **Minimal Experiment:** Pretrain matched mid-scale models under 3 orderings to equal final loss; compare capability batteries; replicate across seeds.
- **Main Risk:** "Equal final loss" stopping may itself bias comparisons.
- **Cluster:** `data-centric-bias`

---

## Sub-cluster 20: Continual & test-time adaptation of VFMs (`continual-tta`)

### A-0286
- **Idea:** Test single-image adaptation limits: how much a promptable model can legitimately adapt from one test image (its own structures as self-supervision) without hallucinating, mapping the overfitting boundary of single-sample TTA for segmentation.
- **Problem:** Single-image TTA promises free gains, but the point where adaptation becomes self-confirmation is uncharacterized for dense prediction.
- **Hypothesis:** Gains from single-image TTA reverse sign after a predictable number of steps proportional to image self-similarity (texture repetitiveness), providing a computable early-stopping rule that keeps TTA safe.
- **Why Important:** A safety rule for the most tempting (and dangerous) adaptation regime.
- **Why Possibly Novel (hypothesized):** Overfitting-boundary laws for single-image segmentation TTA appear missing.
- **Minimal Experiment:** Run TTA step ladders across images with measured self-similarity; locate gain-reversal points; validate the stopping rule out-of-sample.
- **Main Risk:** Reversal points may vary with the TTA objective choice.
- **Cluster:** `continual-tta`

### A-0287
- **Idea:** Study adaptation reversibility: after TTA on a corrupted stream, does the model return to baseline when conditions normalize, or accumulate permanent drift — and design "elastic" adaptation with guaranteed return properties.
- **Problem:** Streaming TTA changes weights continuously; whether models recover when the world recovers is unmeasured, risking permanent degradation from transient conditions.
- **Hypothesis:** Standard streaming TTA accumulates non-returning drift (hysteresis) after condition cycles, and anchoring adaptation as a bounded offset from frozen weights eliminates hysteresis at negligible adaptation cost.
- **Why Important:** Hysteresis-free adaptation is a prerequisite for unattended long-running systems.
- **Why Possibly Novel (hypothesized):** Hysteresis measurement for segmentation TTA appears new.
- **Minimal Experiment:** Cycle corruption conditions on video streams; measure post-cycle deviation from baseline behavior; compare anchored vs. free adaptation.
- **Main Risk:** Some drift may be beneficial (environment learning), complicating the metric.
- **Cluster:** `continual-tta`

### A-0288
- **Idea:** Investigate what continual adaptation should key on: detecting *when* to adapt via distribution-shift detectors vs. adapting continuously, testing whether triggered adaptation dominates continuous adaptation in accuracy-stability trade-offs.
- **Problem:** Continuous adaptation wastes compute and risks drift during stable periods; the triggering policy design space is unexplored for segmentation streams.
- **Hypothesis:** Shift-triggered adaptation (activate only when feature-drift detectors fire) matches continuous adaptation's shift responsiveness while eliminating most stable-period drift, dominating on combined metrics across realistic condition schedules.
- **Why Important:** Establishes the control architecture for practical deployed adaptation.
- **Why Possibly Novel (hypothesized):** Triggered-vs-continuous policy comparison for dense-prediction streams appears sparse.
- **Minimal Experiment:** Simulate realistic condition schedules on video corpora; compare policies on accuracy, drift, and compute; ablate detector choices.
- **Main Risk:** Detector latency may miss fast shifts, hiding triggered-policy weaknesses.
- **Cluster:** `continual-tta`

### A-0289
- **Idea:** Test cross-user adaptation contamination in shared deployments: one user's corrective adaptation degrading another user's workflows on a shared adapted model, quantifying the interference and testing per-user adapter isolation.
- **Problem:** Shared production models adapt on pooled feedback; inter-user interference in adaptation is an unmeasured multi-tenant hazard.
- **Hypothesis:** Pooled adaptation on conflicting user conventions (different granularity preferences) measurably degrades each user relative to per-user adapters, with interference proportional to convention divergence — quantifying the personalization-sharing trade-off.
- **Why Important:** Multi-tenant adaptation architecture is being decided now, largely without measurement.
- **Why Possibly Novel (hypothesized):** Multi-tenant adaptation interference for vision appears unstudied.
- **Minimal Experiment:** Simulate user populations with divergent conventions; compare pooled vs. isolated adaptation on per-user metrics; fit interference-vs-divergence curves.
- **Main Risk:** Simulated conventions may understate real user diversity.
- **Cluster:** `continual-tta`

### A-0290
- **Idea:** Study feature-bank test-time adaptation: adapting via a growing episodic memory of test-domain features (retrieval-augmented inference) instead of weight updates, testing whether memory-based adaptation avoids forgetting and drift by construction.
- **Problem:** Weight-update adaptation inherently risks drift; memory-based alternatives trade storage for stability, but the trade's terms are unmeasured for segmentation.
- **Hypothesis:** Retrieval-augmented adaptation matches weight-update TTA's in-domain gains while exhibiting zero measurable drift and instant reversibility, at a storage cost growing sublinearly with stream length after deduplication.
- **Why Important:** A drift-free adaptation mechanism would remove the main deployment objection to TTA.
- **Why Possibly Novel (hypothesized):** Memory-vs-weight adaptation comparison for promptable segmentation appears fresh.
- **Minimal Experiment:** Implement feature-bank inference over SAM features; compare against TTA baselines on gains, drift, reversibility, and storage across streams.
- **Main Risk:** Retrieval latency may violate real-time budgets.
- **Cluster:** `continual-tta`

### A-0291
- **Idea:** Investigate adaptation credit assignment in compound systems: when a detector-plus-segmenter pipeline degrades under shift, determining which component to adapt (and in what order) via component-wise shift attribution, rather than adapting everything.
- **Problem:** Pipeline adaptation lacks a component-attribution methodology; blanket adaptation wastes budget and multiplies drift risk.
- **Hypothesis:** Component-wise shift attribution (feature-drift localization per stage) predicts which single-component adaptation recovers the majority of pipeline loss, beating uniform adaptation at equal budget on most shift types.
- **Why Important:** Efficient pipeline maintenance under drift is the operational reality of production vision.
- **Why Possibly Novel (hypothesized):** Attribution-directed pipeline adaptation appears unformalized.
- **Minimal Experiment:** Impose shifts affecting known stages; test attribution accuracy; compare attribution-directed vs. uniform adaptation recovery.
- **Main Risk:** Inter-stage interactions may defeat single-component attribution.
- **Cluster:** `continual-tta`

### A-0292
- **Idea:** Test "prompt memory" as continual learning: accumulating a library of (visual context → effective prompt) pairs instead of updating weights, treating continual improvement as prompt-policy learning over a frozen model.
- **Problem:** Weight-space continual learning is risky; prompt-space accumulation over frozen models is an unexplored continual-learning substrate for vision.
- **Hypothesis:** Retrieval-based prompt policies (reuse prompts that worked in similar contexts) improve monotonically with experience without any forgetting risk, approaching a measurable fraction of weight-based continual learning's gains on recurring-context workloads.
- **Why Important:** Zero-forgetting-by-construction continual improvement suits regulated deployments where weights must stay fixed.
- **Why Possibly Novel (hypothesized):** Prompt-space continual learning for segmentation appears unproposed.
- **Minimal Experiment:** Build the prompt-memory system on recurring-context streams (fixed camera datasets); track improvement curves against weight-based baselines.
- **Main Risk:** Gains cap at what prompt variation can express — possibly little for hard shifts.
- **Cluster:** `continual-tta`

### A-0293
- **Idea:** Study adaptation under label-delay: real feedback arrives hours or days late (human review), making standard online adaptation stale — quantify staleness costs and test delay-compensated adaptation schemes.
- **Problem:** Online-adaptation research assumes instant labels; realistic feedback delays change the problem in unmeasured ways.
- **Hypothesis:** Adaptation value decays with feedback delay at a rate set by environment nonstationarity, and delay-aware weighting (discounting stale feedback against detected drift) recovers most of the no-delay value up to a computable delay horizon.
- **Why Important:** Aligns adaptation research with the feedback logistics of actual deployments.
- **Why Possibly Novel (hypothesized):** Delay-aware adaptation analysis for vision streams appears new.
- **Minimal Experiment:** Replay streams with parametric feedback delays; measure value-decay curves; test delay-compensation schemes across nonstationarity levels.
- **Main Risk:** Nonstationarity estimation itself may be delayed, nesting the problem.
- **Cluster:** `continual-tta`

### A-0294
- **Idea:** Investigate negative transfer in fleet adaptation: aggregating adaptations across a device fleet (federated TTA) when devices face heterogeneous conditions, characterizing when sharing helps vs. poisons and deriving a sharing-decision statistic.
- **Problem:** Fleet learning pools adaptations by default; condition heterogeneity may make pooling actively harmful in unmeasured regimes.
- **Hypothesis:** Pooled adaptation helps when inter-device condition similarity exceeds a threshold (measurable from feature statistics) and harms below it, and a similarity-gated sharing rule dominates both always-share and never-share policies.
- **Why Important:** Fleet-level adaptation policy is a live engineering decision lacking evidence.
- **Why Possibly Novel (hypothesized):** Similarity-gated federated TTA for segmentation appears untested.
- **Minimal Experiment:** Simulate fleets with controlled condition heterogeneity; map pooling benefit vs. similarity; validate the gating rule.
- **Main Risk:** Simulated heterogeneity may miss real-fleet correlation structures.
- **Cluster:** `continual-tta`

### A-0295
- **Idea:** Test whether adaptation should target the input instead of the model: learned per-deployment input transforms (color/tone/geometry correction toward the training distribution) as a weight-free adaptation alternative, and where input-space adaptation fundamentally cannot reach.
- **Problem:** Input normalization vs. model adaptation is an old dichotomy never mapped rigorously for VFMs: which shifts are input-correctable?
- **Hypothesis:** A learned invertible input transform recovers most performance for photometric shifts but none for semantic/content shifts, and the recoverable fraction is predictable from whether the shift commutes with the model's early layers.
- **Why Important:** Input-space fixes are auditable, reversible, and certifiable — knowing their reach determines when they suffice.
- **Why Possibly Novel (hypothesized):** Commutation-based reachability theory for input-space adaptation appears new.
- **Minimal Experiment:** Train input transforms across shift taxonomy; measure recovery fractions; test the commutation predictor.
- **Main Risk:** The commutation formalism may be too coarse for real shifts.
- **Cluster:** `continual-tta`

### A-0296
- **Idea:** Study self-supervised prompt-consistency adaptation: adapting on unlabeled targets by penalizing SAM's prompt-inconsistency (different prompts on one object should agree), and testing whether this vision-specific self-supervision beats generic entropy objectives.
- **Problem:** Segmentation TTA borrows objectives from classification (entropy); the promptable structure offers a richer self-supervision signal whose value is unmeasured.
- **Hypothesis:** Prompt-consistency objectives yield larger and safer adaptation gains than entropy minimization (less collapse risk, better boundary recovery) because they enforce a model-internal agreement invariant instead of confidence inflation.
- **Why Important:** A stronger, structurally grounded TTA objective for the entire promptable-model class.
- **Why Possibly Novel (hypothesized):** Prompt-consistency as TTA objective appears underexplored.
- **Minimal Experiment:** Implement consistency-based TTA; compare against entropy/pseudo-label baselines across shift suites on gains and collapse rates.
- **Main Risk:** Consistency can be satisfied by degenerate solutions (empty masks) without careful constraints.
- **Cluster:** `continual-tta`

### A-0297
- **Idea:** Investigate long-horizon continual adaptation audit trails: methods to reconstruct *why* a continually adapted model behaves as it does (which past adaptations caused current behavior), enabling root-cause analysis after months of drift.
- **Problem:** Continually adapted models become unexplainable accumulations; post-hoc attribution of behavior to adaptation history is an unsolved maintenance need.
- **Hypothesis:** Logging low-rank adaptation increments with timestamps permits accurate behavioral attribution (replaying subsets identifies which increments caused a given behavior change) at storage costs feasible for year-long deployments.
- **Why Important:** Auditability determines whether continual adaptation is deployable in regulated domains at all.
- **Why Possibly Novel (hypothesized):** Adaptation-history attribution tooling appears unbuilt for vision.
- **Minimal Experiment:** Run months-long simulated adaptation with logging; test attribution accuracy on injected behavior changes; measure storage/replay costs.
- **Main Risk:** Increment interactions may defeat subset-replay attribution.
- **Cluster:** `continual-tta`

### A-0298
- **Idea:** Test adaptation-vs-reset scheduling: when accumulated adaptation underperforms a fresh restart from the base model plus quick re-adaptation, deriving the optimal reset schedule as a function of drift statistics.
- **Problem:** Continual systems never ask whether resetting beats continuing; the reset-vs-continue economics are unquantified.
- **Hypothesis:** Under realistic drift with occasional regime changes, periodic reset-plus-readapt outperforms pure continual adaptation, with the optimal reset period computable from measured regime-change frequency — a renewal-theory result for model maintenance.
- **Why Important:** Reset scheduling is a free, simple maintenance policy that may dominate sophisticated continual methods.
- **Why Possibly Novel (hypothesized):** Renewal-theoretic reset analysis for vision adaptation appears new.
- **Minimal Experiment:** Simulate drift with regime changes; compare reset schedules against continual baselines; validate the renewal-derived optimum.
- **Main Risk:** Real drift statistics may be too irregular for renewal assumptions.
- **Cluster:** `continual-tta`

### A-0299
- **Idea:** Study minimal-supervision drift correction: ranking cheap supervision types (single click per hour, one verified mask per day, binary "still working?" signals) by drift-correction value per unit human effort in streaming segmentation.
- **Problem:** Deployments can afford trickles of supervision; the value hierarchy of supervision types for drift correction is unmeasured.
- **Hypothesis:** Sparse verified masks dominate abundant weak signals per effort-unit for representation drift, while abundant binary alarms dominate for threshold drift — a two-regime hierarchy enabling effort-optimal monitoring design.
- **Why Important:** Optimizing the human-effort budget is the binding constraint of monitored deployments.
- **Why Possibly Novel (hypothesized):** Supervision-type value ranking for drift correction appears absent.
- **Minimal Experiment:** Simulate drift scenarios with supervision budgets across types; measure correction value per effort; map the regime boundary.
- **Main Risk:** Effort costs vary by interface quality, complicating unit normalization.
- **Cluster:** `continual-tta`

### A-0300
- **Idea:** Test whether adaptation can be certified stable: constructing PEFT update families with provable output-deviation bounds on a reference distribution (adaptation that cannot change behavior on certified inputs beyond ε), enabling regulated in-field updates.
- **Problem:** Regulators block field adaptation for lack of behavioral guarantees; bounded-deviation adaptation families are undeveloped for vision.
- **Hypothesis:** Norm-constrained low-rank updates with layer-wise Lipschitz budgets yield certified output-deviation bounds that are non-vacuous (tight enough to permit useful adaptation) on realistic reference sets — establishing feasible certified adaptation.
- **Why Important:** Would unlock adaptation in medical/automotive domains where it is currently prohibited.
- **Why Possibly Novel (hypothesized):** Certified-deviation PEFT for segmentation appears unconstructed.
- **Minimal Experiment:** Derive bounds for constrained LoRA families; measure bound tightness vs. adaptation utility on medical shift tasks; characterize the certified-utility frontier.
- **Main Risk:** Bounds may be vacuous at useful adaptation strengths.
- **Cluster:** `continual-tta`

---

## Sub-cluster 21: Architecture internals (`architecture-internals`)

### A-0301
- **Idea:** Map the division of labor between SAM's decoder self-attention and cross-attention: which mask properties (extent, boundary, coherence) each attention type determines, via targeted attention-pattern interventions.
- **Problem:** The decoder is treated as a black box; property-level attribution to its attention mechanisms would enable targeted repair of specific failure types.
- **Hypothesis:** Mask extent decisions localize to token-to-image cross-attention while spatial coherence localizes to image self-attention, demonstrated by property-specific degradation under mechanism-specific perturbations.
- **Why Important:** Mechanism-property maps convert "the mask is wrong" into "this circuit failed," enabling surgical fixes.
- **Why Possibly Novel (hypothesized):** Property-resolved mechanistic attribution in mask decoders appears nascent.
- **Minimal Experiment:** Perturb each attention pathway independently (noise, ablation, patching); measure property-specific error responses across 1k objects.
- **Main Risk:** Pathways may be redundant, blurring attributions.
- **Cluster:** `architecture-internals`

### A-0302
- **Idea:** Test whether the output-token bottleneck (a handful of mask tokens summarizing the whole query) causes information-theoretic mask complexity limits: masks whose description length exceeds token capacity failing predictably.
- **Problem:** Complex masks (many components, high-genus shapes) may exceed what fixed mask tokens can encode, but the capacity limit is unmeasured.
- **Hypothesis:** Mask reconstruction error grows sharply beyond a complexity threshold (measured in mask description length), and the threshold scales with mask-token count in controlled retraining — establishing a capacity law.
- **Why Important:** A capacity law predicts which applications (cell colonies, foliage) need architectural changes, not tuning.
- **Why Possibly Novel (hypothesized):** Token-capacity laws for mask decoding appear underexplored.
- **Minimal Experiment:** Evaluate error vs. mask complexity metrics; retrain decoder variants with 1–16 mask tokens; test threshold scaling.
- **Main Risk:** Mask complexity metrics are multiple and contestable.
- **Cluster:** `architecture-internals`

### A-0303
- **Idea:** Investigate positional-embedding extrapolation pathologies: how promptable models behave when objects appear at positions/scales rare in pretraining (image corners, extreme sizes), attributing failures to embedding-space extrapolation vs. content unfamiliarity.
- **Problem:** Performance dips at spatial extremes are folklore; the embedding-vs-content attribution is untested.
- **Hypothesis:** Corner/edge performance dips persist when familiar content is composited into rare positions (embedding-driven), and vanish under position-randomized fine-tuning of embeddings alone — isolating a cheap fix.
- **Why Important:** Spatial fairness of segmentation matters for automated cropping, surveillance, and document analysis.
- **Why Possibly Novel (hypothesized):** Position-extrapolation attribution for promptable models appears new.
- **Minimal Experiment:** Composite objects across position grids; measure positional performance fields; retrain positional embeddings only; re-measure.
- **Main Risk:** Compositing artifacts may contaminate positional measurements.
- **Cluster:** `architecture-internals`

### A-0304
- **Idea:** Study attention-sink formation in vision transformers used for segmentation: whether sink tokens (absorbing attention mass) create spatial dead zones where prompts underperform, and whether sink-aware inference redistributes attention productively.
- **Problem:** Attention sinks are characterized in language models; their spatial consequences in dense vision tasks are unmapped.
- **Hypothesis:** Attention-sink locations create measurable prompt-response dead zones (lower mask quality for prompts landing there), and inference-time sink neutralization recovers the deficit without retraining.
- **Why Important:** Connects a known transformer phenomenon to spatially localized task failures with a cheap intervention.
- **Why Possibly Novel (hypothesized):** Spatial dead-zone analysis of attention sinks appears new for segmentation.
- **Minimal Experiment:** Locate sinks per image; test prompt quality on/off sink locations with matched content; apply sink-masking at inference.
- **Main Risk:** Sink locations may covary with genuinely uninformative regions.
- **Cluster:** `architecture-internals`

### A-0305
- **Idea:** Test layer-skip robustness as a modularity probe: which encoder layers can be skipped at inference with minimal segmentation damage, and whether skippable layers correspond to identifiable redundant computation that distillation should target first.
- **Problem:** Layer-level redundancy structure of VFM encoders under dense tasks is unmapped, leaving compression to guesswork.
- **Hypothesis:** Skippability is bimodal (layers are either near-free or catastrophic to skip), stable across datasets, and predicts distillation-compression difficulty layer-by-layer.
- **Why Important:** A skippability atlas would give compression research a principled starting map.
- **Why Possibly Novel (hypothesized):** Dense-task skippability atlases appear unbuilt.
- **Minimal Experiment:** Skip layers (with identity or interpolation bridges) singly and in combinations; measure segmentation damage; correlate with distillation outcomes.
- **Main Risk:** Skipping alters activation statistics for downstream layers, confounding attribution.
- **Cluster:** `architecture-internals`

### A-0306
- **Idea:** Investigate whether mask decoders implement approximate energy minimization: testing if decoder iterations behave like optimization steps on an implicit energy (monotone refinement, convergence), which would license optimization-theoretic analysis of failures.
- **Problem:** Decoder iterations are designed heuristically; if they implement implicit optimization, failure modes become analyzable via energy-landscape tools.
- **Hypothesis:** Decoder iterate sequences exhibit optimization signatures (monotone decrease of a learnable energy, step-size sensitivity, local-minimum trapping on ambiguous inputs), and trapping predicts multimodal ambiguity cases.
- **Why Important:** An optimization account unifies scattered failure observations under landscape geometry.
- **Why Possibly Novel (hypothesized):** Energy-interpretation testing of mask decoders appears fresh.
- **Minimal Experiment:** Fit implicit energies to iterate sequences; test monotonicity/convergence predictions; correlate trapping diagnostics with ambiguity benchmarks.
- **Main Risk:** Decoders may be too shallow (2 iterations) for meaningful dynamics.
- **Cluster:** `architecture-internals`

### A-0307
- **Idea:** Study frequency-domain division of labor across encoder depth: whether early layers carry boundary-frequency information that late layers discard, explaining why single-layer feature taps force a boundary-semantics trade-off.
- **Problem:** Feature-tap choices (which layer feeds the decoder) trade boundary detail against semantics; the spectral basis of this trade-off is unquantified.
- **Hypothesis:** Decodable boundary information peaks at early-middle depth and decays monotonically after, while semantic information rises — with the crossing point predicting the optimal single-tap layer per task, and multi-tap fusion beating any single tap by a margin predicted by the spectral gap.
- **Why Important:** Converts feature-tap selection from convention to spectral measurement.
- **Why Possibly Novel (hypothesized):** Spectral depth-profiles for tap selection appear informal so far.
- **Minimal Experiment:** Probe boundary/semantic decodability per layer across models; validate tap-selection and fusion predictions on segmentation tasks.
- **Main Risk:** Probe architecture choices affect decodability estimates.
- **Cluster:** `architecture-internals`

### A-0308
- **Idea:** Test stochasticity fingerprints of nondeterministic inference: whether GPU nondeterminism (atomics, reduction order) produces mask variation exceeding tolerance in boundary regions, quantifying the reproducibility floor of deployed segmentation.
- **Problem:** Bit-level nondeterminism is assumed inconsequential; its mask-level footprint (especially at boundaries) is unmeasured.
- **Hypothesis:** Repeated identical-input inference varies boundary pixels measurably on borderline structures (near-threshold logits), setting a hardware-dependent reproducibility floor relevant for forensic and medical applications.
- **Why Important:** Applications requiring exact reproducibility must know (and possibly certify) this floor.
- **Why Possibly Novel (hypothesized):** Reproducibility-floor measurement for segmentation appears undone.
- **Minimal Experiment:** Run repeated inference across hardware/settings; quantify mask-variation statistics; map variation to logit-margin distributions.
- **Main Risk:** Modern deterministic-mode settings may make the effect negligible (still worth documenting).
- **Cluster:** `architecture-internals`

### A-0309
- **Idea:** Investigate the role of the IoU-prediction head as a training regularizer: whether its auxiliary gradient shapes mask features beneficially (or harmfully), separable by training matched models with the head detached vs. attached.
- **Problem:** Auxiliary heads change training dynamics invisibly; the IoU head's contribution to mask quality (beyond its scoring function) is unknown.
- **Hypothesis:** The IoU head's gradients act as a mask-quality-aware curriculum (upweighting borderline cases), and detaching it degrades boundary quality measurably even when scores are never used — revealing a hidden training dependency.
- **Why Important:** Understanding hidden dependencies matters when architectures are modified or heads are removed for efficiency.
- **Why Possibly Novel (hypothesized):** Auxiliary-head training-effect isolation for SAM-class models appears untested.
- **Minimal Experiment:** Train matched models with attached/detached/stop-gradient IoU heads; compare mask quality and training dynamics.
- **Main Risk:** Retraining cost; effects may be small at scale.
- **Cluster:** `architecture-internals`

### A-0310
- **Idea:** Study cross-image feature interference in batched inference: whether batch-level normalization or memory-optimization paths cause image A's content to measurably influence image B's masks, auditing inference isolation of production stacks.
- **Problem:** Inference isolation is assumed; optimized batched paths (shared normalization statistics, fused kernels) may violate it subtly.
- **Hypothesis:** Some production inference configurations exhibit measurable cross-image influence (output changes when batchmates change), concentrated in normalization-sensitive layers — a silent correctness bug class needing standardized audits.
- **Why Important:** Isolation violations corrupt reproducibility and create data-leak channels across users.
- **Why Possibly Novel (hypothesized):** Batch-isolation audits for vision inference appear unperformed.
- **Minimal Experiment:** Vary batchmates systematically for fixed target images across inference stacks; measure output deviations; localize responsible operations.
- **Main Risk:** Well-implemented stacks may show a null (still valuable as an audit protocol).
- **Cluster:** `architecture-internals`

### A-0311
- **Idea:** Test width-vs-depth allocation in mask decoders: whether decoder capability scales better with more attention heads and width (parallel hypothesis capacity) or more iterations and depth (sequential refinement capacity), per failure type.
- **Problem:** Decoder scaling directions are chosen by analogy to encoders; failure-type-resolved returns to width vs. depth are unmeasured.
- **Hypothesis:** Width buys multi-hypothesis and multi-object capabilities while depth buys boundary refinement, with distinct saturation points — so the optimal decoder shape depends measurably on workload failure profiles.
- **Why Important:** Decoder design currently copies defaults; workload-matched shaping is free performance.
- **Why Possibly Novel (hypothesized):** Failure-resolved width-depth analysis for mask decoders appears missing.
- **Minimal Experiment:** Train a decoder shape grid on fixed encoders; evaluate per-capability batteries; map shape-capability response surfaces.
- **Main Risk:** Grid conclusions may depend on the frozen encoder choice.
- **Cluster:** `architecture-internals`

### A-0312
- **Idea:** Investigate residual-stream pollution during multi-prompt inference: whether processing many prompts against cached features accumulates state (via any stateful component) that biases later prompts in the sequence, auditing prompt-order independence of inference engines.
- **Problem:** Prompt independence over cached features is architecturally expected but implementation-level state (caches, buffers) may violate it silently.
- **Hypothesis:** Certain inference implementations show measurable prompt-order effects on identical prompt sets, traceable to implementation state rather than model design — establishing an audit protocol and a correctness bug class.
- **Why Important:** Order-dependent inference breaks reproducibility of batch annotation runs in undetected ways.
- **Why Possibly Novel (hypothesized):** Prompt-order independence auditing appears unperformed.
- **Minimal Experiment:** Permute large prompt sets on fixed images across implementations; test output invariance; bisect any violations to components.
- **Main Risk:** Likely null for reference implementations; value concentrated in optimized stacks.
- **Cluster:** `architecture-internals`

### A-0313
- **Idea:** Study the emergence of instance individuation in encoder features: at which depth two touching same-class objects become linearly separable in feature space, and whether that depth predicts instance-separation ability across architectures.
- **Problem:** Where individuation happens inside encoders is unknown, though it determines whether instance failures are encoder- or decoder-attributable.
- **Hypothesis:** Individuation depth (first layer where instance identity is linearly decodable for touching objects) varies across architectures and strongly predicts their touching-instance segmentation accuracy — a mechanistic performance predictor.
- **Why Important:** A measurable internal correlate of a key capability guides architecture search cheaply.
- **Why Possibly Novel (hypothesized):** Individuation-depth measurement appears new.
- **Minimal Experiment:** Probe instance separability per layer on touching-object corpora across 6 encoders; correlate depth statistics with downstream instance metrics.
- **Main Risk:** Linear separability may understate nonlinear individuation.
- **Cluster:** `architecture-internals`

### A-0314
- **Idea:** Test activation-steering for segmentation control: whether adding learned steering vectors to decoder activations controls interpretable mask properties (grow/shrink, include-attachments, tighten-boundary) reliably across images — a training-free control interface.
- **Problem:** Users lack continuous control knobs over mask properties; activation steering offers a possible zero-training control channel of unknown reliability for vision decoders.
- **Hypothesis:** Property-aligned steering directions exist (found from contrastive activation pairs), generalize across images with predictable strength-response curves, and compose approximately linearly for independent properties.
- **Why Important:** Reliable steering would provide product-grade mask control without model changes and reveal the decoder's internal property axes.
- **Why Possibly Novel (hypothesized):** Activation steering for mask decoders appears unexplored.
- **Minimal Experiment:** Extract steering vectors from contrastive pairs (tight/loose masks); test generalization, dose-response, and compositionality on held-out images.
- **Main Risk:** Directions may be entangled, producing side effects on unrelated properties.
- **Cluster:** `architecture-internals`

### A-0315
- **Idea:** Investigate architectural memory of pretraining resolution: whether models pretrained at fixed resolution encode a persistent "native scale" detectable in feature statistics, biasing all downstream size perception even after multi-resolution fine-tuning.
- **Problem:** Resolution flexibility is claimed after fine-tuning, but a residual native-scale bias would systematically distort size-dependent behavior in unmeasured ways.
- **Hypothesis:** Feature-statistic signatures of pretraining resolution survive multi-resolution fine-tuning and predict residual size-estimation biases (objects near native token scale privileged) — a persistent architectural memory with quantifiable behavioral footprint.
- **Why Important:** Hidden scale biases matter for measurement applications and cross-resolution deployment fairness.
- **Why Possibly Novel (hypothesized):** Persistent native-scale memory analysis appears new.
- **Minimal Experiment:** Fine-tune fixed-resolution models multi-resolution; test for surviving resolution signatures and size-conditioned performance asymmetries against natively multi-resolution controls.
- **Main Risk:** Distinguishing architectural memory from data effects requires careful controls.
- **Cluster:** `architecture-internals`

---

## Sub-cluster 22: 3D, volumetric & geometric coupling (`3d-volumetric-geometry`)

### A-0316
- **Idea:** Test multi-view mask consistency as a 3D-understanding probe: whether SAM's masks of the same object from different viewpoints correspond to a single coherent 3D region, quantifying the "3D consistency defect" of 2D promptable models.
- **Problem:** 2D masks are lifted to 3D in reconstruction pipelines assuming cross-view consistency that is unmeasured.
- **Hypothesis:** Cross-view mask lift-and-reproject consistency degrades sharply with viewpoint separation beyond 30°, with failure concentrated at self-occlusion boundaries, quantifying exactly where per-view masking breaks 3D pipelines.
- **Why Important:** 3D reconstruction and robotics pipelines consume 2D masks; their consistency budget should be measured, not assumed.
- **Why Possibly Novel (hypothesized):** Systematic 3D-consistency-defect measurement for promptable models appears sparse.
- **Minimal Experiment:** Use multi-view datasets with meshes; prompt corresponding views; measure lift-reproject IoU vs. viewpoint separation; localize failures.
- **Main Risk:** Prompt correspondence across views must be automated carefully.
- **Cluster:** `3d-volumetric-geometry`

### A-0317
- **Idea:** Investigate whether monocular geometric cues in VFM features (implicit depth/normals) causally support segmentation decisions or are epiphenomenal, via cue-conflict scenes where geometry and appearance disagree.
- **Problem:** VFM features decode depth surprisingly well, but whether segmentation *uses* this geometry is undetermined.
- **Hypothesis:** On geometry-appearance conflict scenes (painted shadows, trompe-l'oeil), segmentation follows appearance over geometry in most cases, showing geometric information is present but unused — an integration gap rather than a representation gap.
- **Why Important:** Integration gaps suggest cheap fixes (loss terms) rather than expensive new pretraining.
- **Why Possibly Novel (hypothesized):** Causal-use testing of implicit geometry in segmentation appears new.
- **Minimal Experiment:** Curate/construct conflict scenes; measure which cue masks follow; probe feature-level geometry presence in the same cases.
- **Main Risk:** Conflict scenes are rare and construction may introduce artifacts.
- **Cluster:** `3d-volumetric-geometry`

### A-0318
- **Idea:** Study native-3D vs. slice-wise 2D adaptation for volumetric medical segmentation at matched budgets: whether 2D foundation priors plus inter-slice fusion beat 3D-from-scratch across data scales, mapping the crossover.
- **Problem:** The field oscillates between 2D-foundation and 3D-native approaches without a controlled crossover map by data availability.
- **Hypothesis:** 2D-foundation-plus-fusion dominates below a data threshold (per anatomy) and 3D-native above it, with the threshold predictable from through-plane information content of the anatomy.
- **Why Important:** A crossover map ends a recurring architecture debate with a decision rule.
- **Why Possibly Novel (hypothesized):** Controlled 2D-vs-3D crossover analysis appears fragmented in the literature.
- **Minimal Experiment:** Train both paradigms across data-size ladders on several anatomies; locate crossovers; regress on anatomy statistics.
- **Main Risk:** Fusion-method choice affects the 2D side's ceiling.
- **Cluster:** `3d-volumetric-geometry`

### A-0319
- **Idea:** Test 3D prompt semantics: what a "click" should mean in volumetric promptable segmentation (surface point vs. interior point vs. ray), and whether prompt-semantic mismatch explains failures of naive 2D-prompt ports to 3D.
- **Problem:** 3D promptable models port 2D prompt types without examining their changed semantics in volumes — an unstudied design dimension.
- **Hypothesis:** Interior-point prompts and surface-point prompts produce systematically different segmentations in current 3D models (unintended sensitivity), and semantically explicit prompt encoding (declaring point type) improves 3D interactive efficiency measurably.
- **Why Important:** Prompt semantics is the interface foundation for the coming generation of 3D interactive tools.
- **Why Possibly Novel (hypothesized):** 3D prompt-semantics analysis appears unexamined.
- **Minimal Experiment:** Evaluate 3D promptable models under controlled prompt placements (surface/interior/ray); measure sensitivity; test type-annotated prompt encoding.
- **Main Risk:** Few mature 3D promptable baselines exist to test.
- **Cluster:** `3d-volumetric-geometry`

### A-0320
- **Idea:** Investigate amodal completion competence: whether promptable models can be elicited (via prompts on occluded regions) to output amodal masks, and if amodal knowledge exists latently in models trained only on modal masks.
- **Problem:** Whether modal-trained models harbor recoverable amodal structure determines if amodal segmentation needs new data or new readouts.
- **Hypothesis:** Prompting on occluder regions with object-context clicks elicits partial amodal completions significantly above chance, and a light amodal readout head trained on small data unlocks systematic amodal ability — evidencing latent amodal knowledge.
- **Why Important:** Amodal reasoning is prerequisite for manipulation and driving; latent capability would drastically cut its data cost.
- **Why Possibly Novel (hypothesized):** Latent-amodal-elicitation studies for SAM-class models appear rare.
- **Minimal Experiment:** Construct occlusion-controlled scenes with amodal GT; test prompt-elicitation protocols; train small amodal heads on frozen features.
- **Main Risk:** Elicited completions may reflect shape priors rather than scene-specific inference.
- **Cluster:** `3d-volumetric-geometry`

### A-0321
- **Idea:** Study scale-metric blindness: promptable models cannot access metric scale (a toy car vs. real car at equal image size), testing whether metric-scale conditioning (camera intrinsics injection) changes segmentation decisions where physical size matters.
- **Problem:** Image-space models conflate physically different objects at equal angular size; whether intrinsics conditioning helps dense tasks is untested.
- **Hypothesis:** Intrinsics-conditioned fine-tuning measurably improves segmentation in scale-ambiguous cases (miniatures, close-ups) by resolving category priors correctly, demonstrating that metric information has task value beyond monocular cues.
- **Why Important:** Robotics and AR always possess intrinsics; leaving them unused may waste free accuracy.
- **Why Possibly Novel (hypothesized):** Intrinsics-conditioning value measurement for segmentation appears new.
- **Minimal Experiment:** Fine-tune with/without intrinsics tokens on datasets with camera metadata; evaluate on scale-ambiguity-stratified cases.
- **Main Risk:** Scale-ambiguous evaluation cases are rare and need curation.
- **Cluster:** `3d-volumetric-geometry`

### A-0322
- **Idea:** Test video-lifted pseudo-3D supervision: whether enforcing that SAM2 masklets sweep consistent 3D volumes (via structure-from-motion) during fine-tuning improves both video consistency and single-frame 3D-consistency defects.
- **Problem:** Temporal and geometric consistency are trained separately; using SfM-derived 3D coherence as free supervision for mask quality is unexplored as a controlled question.
- **Hypothesis:** SfM-consistency fine-tuning reduces cross-view mask defects and improves occlusion-boundary accuracy on still images, showing 3D-coherence supervision transfers to single-view geometric competence.
- **Why Important:** Free geometric supervision from unlabeled video could address a family of geometry-linked failures at once.
- **Why Possibly Novel (hypothesized):** SfM-coherence as mask supervision for promptable models appears fresh.
- **Minimal Experiment:** Fine-tune with SfM-consistency losses on unlabeled video; evaluate cross-view consistency, occlusion boundaries, and standard suites.
- **Main Risk:** SfM errors may inject geometric noise worse than the signal.
- **Cluster:** `3d-volumetric-geometry`

### A-0323
- **Idea:** Investigate viewpoint bias inheritance: quantifying how internet photography's canonical-viewpoint bias shapes segmentation competence across the viewing sphere, using controlled orbits of common objects.
- **Problem:** Performance is reported viewpoint-marginalized; the viewing-sphere structure of competence (and its data-side cause) is unmapped.
- **Hypothesis:** Per-object segmentation quality over the viewing sphere correlates with estimated photographic viewpoint frequency, with characteristic collapse at rare viewpoints (top-down, underside) that targeted synthetic orbits repair.
- **Why Important:** Robots and drones see rare viewpoints constantly; the bias map defines their risk exposure.
- **Why Possibly Novel (hypothesized):** Viewing-sphere competence mapping appears rare for segmentation.
- **Minimal Experiment:** Render/photograph object orbits; map quality over the sphere; correlate with viewpoint-frequency estimates; test synthetic-orbit fine-tuning.
- **Main Risk:** Viewpoint-frequency estimation for training corpora is approximate.
- **Cluster:** `3d-volumetric-geometry`

### A-0324
- **Idea:** Study part-segmentation consistency under articulation: whether part masks (e.g., limb boundaries) remain consistent as objects articulate, testing if models segment parts by geometry (joint structure) or by appearance snapshots.
- **Problem:** Part boundaries should track anatomical structure under articulation; snapshot-based parts would fragment inconsistently — the mechanism is undetermined.
- **Hypothesis:** Part-boundary placement varies systematically with pose (appearance-snapshot behavior) rather than staying anatomically anchored, and the inconsistency magnitude predicts downstream pose-estimation errors when masks are used as inputs.
- **Why Important:** Consistent parts matter for biomechanics, animation, and robotics affordance mapping.
- **Why Possibly Novel (hypothesized):** Articulation-consistency measurement for part segmentation appears new.
- **Minimal Experiment:** Evaluate part masks across pose sequences with anatomical GT; measure boundary drift vs. pose; correlate with downstream tasks.
- **Main Risk:** Anatomical part GT under articulation is expensive to annotate.
- **Cluster:** `3d-volumetric-geometry`

### A-0325
- **Idea:** Test transparency-geometry entanglement: segmenting through transparent surfaces (objects behind glass) to determine whether models represent the layered scene structure or collapse layers into single-surface decisions.
- **Problem:** Layered scenes (windows, water, containers) are ubiquitous, but whether models represent layer structure is unknown, and single-layer collapse would explain a family of errors.
- **Hypothesis:** Prompted on objects behind glass, models blend occluder and target into hybrid masks at high rates, and the blend ratio tracks relative contrast — evidencing layer collapse rather than layered representation, with prompt-based layer selection impossible in current architectures.
- **Why Important:** Layer-aware segmentation is required for driving (windshields), retail (displays), and robotics (containers).
- **Why Possibly Novel (hypothesized):** Layer-collapse characterization for promptable models appears fresh.
- **Minimal Experiment:** Curate behind-glass scenes with dual-layer GT; classify output modes (target/occluder/hybrid); test contrast dependence of blending.
- **Main Risk:** Dual-layer GT annotation is inherently ambiguous at reflections.
- **Cluster:** `3d-volumetric-geometry`

### A-0326
- **Idea:** Investigate volumetric prompt propagation: for 3D volumes, whether a single-slice prompt should propagate via the model's own features vs. geometric priors, and characterize where feature-propagation fails predictably (anatomy changes topology across slices).
- **Problem:** Slice-prompt propagation methods lack a failure map tied to anatomical topology, causing unpredictable 3D interactive behavior.
- **Hypothesis:** Feature-based propagation fails predictably at topology-change slices (branch points, organ boundaries), and a topology-change detector (from feature-flow divergence) triggers re-prompting requests exactly where human input is needed.
- **Why Important:** Predictable interactive 3D workflows determine clinical adoption of promptable volumetric tools.
- **Why Possibly Novel (hypothesized):** Topology-aware propagation-failure prediction appears new.
- **Minimal Experiment:** Propagate prompts through annotated volumes; align failures with topology-change annotations; validate the detector's re-prompt triggering.
- **Main Risk:** Topology-change ground truth requires anatomical expertise.
- **Cluster:** `3d-volumetric-geometry`

### A-0327
- **Idea:** Study shadow-object binding: whether models segment objects with or without their shadows in a principled or contingent manner, and whether shadow treatment consistency can be controlled by a single learned direction.
- **Problem:** Shadow inclusion is inconsistent across images and prompts, corrupting area measurements downstream; the internal representation of the object-shadow relationship is uncharacterized.
- **Hypothesis:** Shadow inclusion is contingent on low-level contrast rather than represented as a semantic attachment relation, but a single activation direction can control inclusion consistently — revealing latent structure without semantic understanding.
- **Why Important:** Consistent shadow policy matters for agriculture, mapping, and measurement applications.
- **Why Possibly Novel (hypothesized):** Shadow-binding control analysis appears unexplored.
- **Minimal Experiment:** Measure shadow-inclusion rates vs. contrast conditions; search for control directions via contrastive activation pairs; test consistency of controlled inclusion.
- **Main Risk:** Shadow GT (attached vs. cast) requires careful annotation protocol.
- **Cluster:** `3d-volumetric-geometry`

### A-0328
- **Idea:** Test cross-sensor volumetric transfer: whether adapters trained for CT transfer zero-shot to structurally similar but physically different volumetric modalities (industrial CT, micro-CT, OCT), locating the boundary between structure-transferable and physics-bound adaptation knowledge.
- **Problem:** Volumetric adaptation is siloed per modality; the transferable fraction across physically distinct volumetric sensors is unmeasured.
- **Hypothesis:** Anatomy/structure-related adapter components transfer across volumetric modalities (recoverable by adapter decomposition) while intensity-physics components do not, and the decomposition can be computed post hoc to enable partial transfer.
- **Why Important:** Partial-transfer tooling would connect medical, industrial, and scientific volumetric communities' adaptation investments.
- **Why Possibly Novel (hypothesized):** Adapter decomposition for cross-physics transfer appears untried.
- **Minimal Experiment:** Train CT adapters; decompose (subspace analysis); test component-wise transfer to micro-CT/OCT tasks.
- **Main Risk:** The structure/physics decomposition may not align with any weight-space structure.
- **Cluster:** `3d-volumetric-geometry`

### A-0329
- **Idea:** Investigate whether egocentric video's geometric regularities (ground plane, hand proximity) are exploited or ignored by video segmentation models, testing egocentric-prior injection as a deployment-time improvement for wearables.
- **Problem:** Egocentric footage has strong geometric priors that general video models may waste; the exploitable headroom is unquantified.
- **Hypothesis:** Current models leave measurable performance on the table in egocentric settings (errors violating ground-plane and hand-interaction priors), and lightweight prior injection (geometric consistency reranking) recovers a meaningful fraction without retraining.
- **Why Important:** Wearable AR is a major deployment surface with structurally distinct video statistics.
- **Why Possibly Novel (hypothesized):** Egocentric-prior headroom quantification appears new for promptable video models.
- **Minimal Experiment:** Categorize errors on egocentric benchmarks by prior violation; implement prior-based reranking; measure recovery.
- **Main Risk:** Priors fail in edge cases (mirrors, climbing), needing safe gating.
- **Cluster:** `3d-volumetric-geometry`

### A-0330
- **Idea:** Study reflective-surface duplication: quantifying how often models segment reflections as independent objects across mirror/water/glass scenes, and whether reflection identity (link to source object) is decodable from features despite wrong mask outputs.
- **Problem:** Reflection handling failures are known anecdotally; their rate, structure, and the latent presence of reflection-source binding are unmeasured.
- **Hypothesis:** Reflection duplication is frequent and confidence-indistinguishable from real objects at the output level, yet reflection-vs-real is linearly decodable from intermediate features — an unread internal signal that a small head can surface for deduplication.
- **Why Important:** Reflection duplicates corrupt counting and tracking in water/urban-glass environments routinely.
- **Why Possibly Novel (hypothesized):** Latent reflection-signal decoding appears untested.
- **Minimal Experiment:** Curate reflection scenes with GT; measure duplication and confidence overlap; train reflection probes on frozen features; test deduplication.
- **Main Risk:** Probe results may not generalize across reflection types (specular vs. diffuse).
- **Cluster:** `3d-volumetric-geometry`

---

## Sub-cluster 23: Compositionality, counting & parts (`compositional-counting`)

### A-0331
- **Idea:** Test whether segment-then-count beats count-then-segment architecturally: comparing error structures of counting via exhaustive instance segmentation vs. direct density estimation on the same backbone, per density regime.
- **Problem:** Counting via segmentation inherits instance-separation failures while density methods lack verifiability; their regime-wise dominance structure on shared representations is unmeasured.
- **Hypothesis:** Segmentation-based counting dominates below a density threshold and density estimation above it, with the crossover determined by the backbone's instance-separability depth (linking to individuation capacity), enabling a hybrid switcher with the best of both.
- **Why Important:** Counting drives agriculture, biology, and retail decisions; regime-aware method selection is directly deployable.
- **Why Possibly Novel (hypothesized):** Shared-backbone regime comparison of counting paradigms appears sparse.
- **Minimal Experiment:** Train both heads on one frozen backbone; evaluate across density-stratified corpora; locate crossovers; validate the switcher.
- **Main Risk:** Head capacity differences may confound the paradigm comparison.
- **Cluster:** `compositional-counting`

### A-0332
- **Idea:** Study whole-part consistency enforcement: whether requiring part masks to tile their parent object (no gaps/overlaps) at inference improves both part and whole accuracy, testing consistency as a free accuracy source.
- **Problem:** Parts and wholes are predicted independently, allowing geometric contradictions whose resolution could improve both — an untested consistency dividend.
- **Hypothesis:** Projecting predictions onto the consistency constraint (parts partition whole) improves part accuracy and boundary quality measurably on articulated categories, with gains proportional to the model's baseline inconsistency rate.
- **Why Important:** Consistency constraints are compute-cheap and model-agnostic if they work.
- **Why Possibly Novel (hypothesized):** Inference-time part-whole projection analysis appears fresh.
- **Minimal Experiment:** Measure baseline part-whole contradictions; apply constrained decoding/projection; evaluate accuracy changes across categories.
- **Main Risk:** GT part decompositions vary, making the constraint definition dataset-relative.
- **Cluster:** `compositional-counting`

### A-0333
- **Idea:** Investigate relational segmentation ("segment what the person is holding"): whether failures decompose into relation detection vs. relatum segmentation, and whether relations are represented anywhere in frozen VFM features.
- **Problem:** Relation-conditioned segmentation is required by assistants/robots, but its failure anatomy and representational prerequisites are unmapped.
- **Hypothesis:** Relation information (holding, wearing, supporting) is weakly decodable from frozen features at object-pair level, and most task failures trace to relation detection (not segmentation), implying relation-focused supervision is the binding investment.
- **Why Important:** Correctly locating the bottleneck saves misdirected data collection.
- **Why Possibly Novel (hypothesized):** Failure decomposition for relational segmentation appears missing.
- **Minimal Experiment:** Build relation-conditioned benchmarks; decompose errors via oracle-relation and oracle-mask ablations; probe features for relation decodability.
- **Main Risk:** Oracle ablations require relation annotations at scale.
- **Cluster:** `compositional-counting`

### A-0334
- **Idea:** Test hierarchical granularity coherence across the whole scene: whether a model's implicit scene parse (all masks at all granularities) forms a consistent hierarchy or contains cyclic/contradictory containment relations, defining a scene-level coherence score.
- **Problem:** Mask sets are evaluated individually; the structural coherence of the implied scene parse — which downstream reasoning consumes — is unmeasured.
- **Hypothesis:** Current models produce containment contradictions (A contains B, B overlaps A's complement) in a substantial fraction of complex scenes, and the coherence score predicts downstream scene-graph task accuracy better than mean mask IoU.
- **Why Important:** Scene-level coherence is what structured downstream reasoning actually depends on.
- **Why Possibly Novel (hypothesized):** Parse-coherence scoring for segmentation outputs appears new.
- **Minimal Experiment:** Extract exhaustive multi-granularity masks; compute containment-consistency statistics; correlate coherence with scene-graph task performance.
- **Main Risk:** Exhaustive extraction protocols may shape coherence results.
- **Cluster:** `compositional-counting`

### A-0335
- **Idea:** Study subitizing vs. counting signatures in VFMs: whether models show the human small-number advantage (exact for 1–4, approximate beyond), locating where numerical representations transition and whether the transition mirrors attention capacity.
- **Problem:** The numerical cognition profile of vision models is uncharacterized, though it predicts count reliability structure for applications.
- **Hypothesis:** Instance-count accuracy shows a sharp exact-to-approximate transition at a model-specific small number that scales with decoder query capacity, paralleling (but not matching) the human subitizing boundary.
- **Why Important:** Knowing the exact-count regime tells applications when counts are trustworthy without verification.
- **Why Possibly Novel (hypothesized):** Subitizing-profile measurement for segmentation models appears new.
- **Minimal Experiment:** Count-controlled scenes from 1–50 instances; measure exactness curves per model; correlate transitions with architectural capacity parameters.
- **Main Risk:** Count accuracy confounds with density/occlusion at higher numbers.
- **Cluster:** `compositional-counting`

### A-0336
- **Idea:** Investigate object permanence in video segmentation at the representation level: whether occluded-object state is maintained in features during occlusion (decodable position/extent) or reconstructed at reappearance, distinguishing memory from re-detection accounts of SAM2 behavior.
- **Problem:** Tracking-through-occlusion could work via maintained state or re-recognition; which mechanism operates determines failure predictions and fixes.
- **Hypothesis:** Occluded-object position remains decodable from memory features during short occlusions (maintained state) but decays to chance before behavioral re-acquisition fails — showing behavior outlives representation via re-detection, a hybrid account with testable transition timing.
- **Why Important:** Mechanism clarity guides whether to invest in memory persistence or re-identification robustness.
- **Why Possibly Novel (hypothesized):** Representation-level permanence probing in video VFMs appears fresh.
- **Minimal Experiment:** Probe occluded-object decodability across occlusion durations; align decay curves with behavioral re-acquisition success.
- **Main Risk:** Probes may read out scene priors rather than object state.
- **Cluster:** `compositional-counting`

### A-0337
- **Idea:** Test material-vs-object segmentation entanglement: prompting on multi-material objects (knife with wooden handle) to characterize whether models default to material or object boundaries, and whether the default is controllable by prompt phrasing or position.
- **Problem:** Material and object boundaries systematically diverge; which one models return, when, and under whose control is unmapped.
- **Hypothesis:** Click position within a material region biases output toward material boundaries while box prompts bias toward object boundaries — an implicit, undocumented prompt-type semantics that users unknowingly invoke.
- **Why Important:** Material-level segmentation matters for recycling, manufacturing, and grasp planning; implicit semantics cause silent task mismatch.
- **Why Possibly Novel (hypothesized):** Material-object default mapping across prompt types appears unstudied.
- **Minimal Experiment:** Curate multi-material object sets with dual GT; measure output type vs. prompt type/position; document the semantics.
- **Main Risk:** Material GT boundaries need careful annotation standards.
- **Cluster:** `compositional-counting`

### A-0338
- **Idea:** Study collective-entity segmentation: how models handle entities that exist only as collectives (queue of people, flock, pile), testing whether collective concepts have any representational support or degenerate to instance unions.
- **Problem:** Collectives are first-class semantic entities with emergent boundaries (a pile's outline ≠ union of item outlines), unexamined in segmentation.
- **Hypothesis:** Prompted with collective nouns, models return either single instances or naive unions, never emergent collective boundaries (e.g., including interstitial space of a pile), demonstrating a missing representational category measurable against human collective-extent judgments.
- **Why Important:** Collectives appear in surveillance, agriculture, and logistics queries routinely.
- **Why Possibly Novel (hypothesized):** Collective-entity auditing appears new for segmentation.
- **Minimal Experiment:** Collect human collective-extent annotations; compare model outputs under collective prompts; classify output modes.
- **Main Risk:** Human collective extents have high variance requiring distribution-level comparison.
- **Cluster:** `compositional-counting`

### A-0339
- **Idea:** Investigate cross-instance property transfer in prompting: whether "segment all things like this one" (exemplar generalization within an image) uses abstract property matching or template matching, dissociable by property-vs-appearance-matched distractor design.
- **Problem:** In-image exemplar generalization is a core interactive capability whose underlying matching computation (abstract vs. template) is undetermined.
- **Hypothesis:** Generalization follows appearance-template matching (fails on property-same/appearance-different instances) rather than property abstraction, with the failure structure predictable from feature-space distances — defining current limits of exemplar prompting.
- **Why Important:** Interactive dataset-bootstrapping workflows depend on knowing what exemplar prompts actually generalize over.
- **Why Possibly Novel (hypothesized):** Matching-computation dissociation for exemplar prompting appears new.
- **Minimal Experiment:** Construct scenes with property/appearance-crossed instance sets; measure generalization patterns; fit both matching accounts.
- **Main Risk:** Constructing crossed sets in natural images is hard; may need staged photography.
- **Cluster:** `compositional-counting`

### A-0340
- **Idea:** Test constituent tracking through transformations: whether models maintain part identity through object state changes (folded/unfolded, assembled/disassembled), probing identity representations beyond spatial continuity.
- **Problem:** State changes break spatial continuity that trackers rely on; whether any current representation supports transformation-invariant part identity is unknown.
- **Hypothesis:** Part re-identification across state changes is near chance for current video models even with clean visibility, and contrastive fine-tuning on transformation pairs yields large gains — evidencing a data gap rather than architectural impossibility.
- **Why Important:** Assembly, cooking, and manufacturing applications require transformation-robust identity.
- **Why Possibly Novel (hypothesized):** Transformation-identity benchmarks for segmentation appear unbuilt.
- **Minimal Experiment:** Curate transformation videos with part-identity GT; evaluate re-identification; run the contrastive fine-tuning intervention.
- **Main Risk:** Part-identity annotation through transformations is laborious.
- **Cluster:** `compositional-counting`

### A-0341
- **Idea:** Study numerical prompt semantics: what "segment 3 apples" should return when 5 exist, and whether models have any consistent cardinality-constrained selection semantics (top-confidence, spatial clustering, or noncompliance).
- **Problem:** Cardinality-constrained queries are natural but their execution semantics in current models is uncharacterized and possibly incoherent.
- **Hypothesis:** Models ignore cardinality constraints entirely (returning all or one), and imposing selection semantics requires only a constrained decoding layer over existing hypothesis scores — cardinality competence is a readout, not a representation, problem.
- **Why Important:** Constraint compliance is basic to instruction-following interfaces.
- **Why Possibly Novel (hypothesized):** Cardinality-semantics auditing appears new for segmentation.
- **Minimal Experiment:** Evaluate cardinality-constrained prompts on count-controlled scenes; classify compliance behavior; test constrained-decoding retrofits.
- **Main Risk:** Prompt phrasing may dominate results; needs phrasing marginalization.
- **Cluster:** `compositional-counting`

### A-0342
- **Idea:** Investigate boundary sharing consistency: when two adjacent objects are segmented separately, whether their shared boundary coincides (pixel-level agreement) or leaves gaps/overlaps, quantifying pairwise consistency as a distinct model property.
- **Problem:** Independent per-prompt inference may violate the physical constraint that adjacent objects share exact boundaries — a consistency property never benchmarked.
- **Hypothesis:** Independently prompted adjacent masks disagree along shared boundaries by measurable margins (systematically biased toward double inclusion of boundary pixels), and joint decoding removes the inconsistency with side benefits to both masks' accuracy.
- **Why Important:** Boundary agreement is required for tiling-based applications (mapping, histology) where gaps/overlaps corrupt downstream geometry.
- **Why Possibly Novel (hypothesized):** Shared-boundary consistency measurement appears new.
- **Minimal Experiment:** Prompt adjacent-object pairs independently; measure boundary agreement statistics; compare against joint-decoding variants.
- **Main Risk:** GT shared boundaries also have annotation noise, complicating attribution.
- **Cluster:** `compositional-counting`

### A-0343
- **Idea:** Test scene-context arithmetic: whether removing an object (inpainting) changes segmentation of unrelated remaining objects, measuring the locality of scene representations and identifying nonlocal entanglement in VFM inference.
- **Problem:** Object representations should be approximately local, but global attention permits entanglement whose magnitude and structure are unmeasured.
- **Hypothesis:** Removing one object measurably changes masks of distant unrelated objects in a nontrivial fraction of scenes, with entanglement structured by co-occurrence statistics (contextually related objects entangled most) — quantifying representational nonlocality.
- **Why Important:** Nonlocality bounds compositional editing reliability and reveals context-prior strength.
- **Why Possibly Novel (hypothesized):** Object-removal locality measurement appears fresh.
- **Minimal Experiment:** Inpaint objects from scenes; measure mask changes on remaining objects vs. distance/relatedness; map entanglement structure.
- **Main Risk:** Inpainting quality contaminates the intervention.
- **Cluster:** `compositional-counting`

### A-0344
- **Idea:** Study typed-part transfer: whether part vocabulary learned on one category (vehicle wheels) transfers to novel categories with analogous parts (office-chair wheels), testing compositional part abstraction in segmentation models.
- **Problem:** Part concepts are semi-abstract (functional roles, repeated shapes); whether models represent them abstractly enough for cross-category transfer is unknown.
- **Hypothesis:** Part segmentation transfers across categories at rates far above chance for functionally defined parts (wheels, handles, legs) but not stylistic parts, evidencing partial compositional abstraction with a functional/stylistic boundary.
- **Why Important:** Part abstraction would multiply the value of every part-annotated dataset across categories.
- **Why Possibly Novel (hypothesized):** Cross-category part-transfer taxonomy appears unmeasured.
- **Minimal Experiment:** Train part heads on source categories; evaluate on analogous parts of held-out categories; classify transfer by part type.
- **Main Risk:** Analogous-part correspondence definitions are contestable.
- **Cluster:** `compositional-counting`

### A-0345
- **Idea:** Investigate the interaction of counting and ambiguity: propagating granularity ambiguity into count intervals (a "rock pile" count depends on granularity choice) and testing interval-valued counting against point estimates for decision quality.
- **Problem:** Counts are reported as points though granularity ambiguity makes them interval-valued; the decision cost of false precision is unmeasured.
- **Hypothesis:** Granularity-aware count intervals (derived from hypothesis sets) cover true task-relative counts with high reliability where point estimates mislead, improving downstream decisions (inventory, dosing) in measurable ways.
- **Why Important:** Honest counting under ambiguity is a safety and economics issue in deployed counting systems.
- **Why Possibly Novel (hypothesized):** Ambiguity-propagated counting appears unformalized.
- **Minimal Experiment:** Build granularity-ambiguous counting benchmarks with task-relative GT; compare interval vs. point pipelines on decision-quality metrics.
- **Main Risk:** Interval consumers (downstream logic) must be built to evaluate fairly.
- **Cluster:** `compositional-counting`

---

## Sub-cluster 24: Failure prediction, trust & deployment (`failure-prediction-deployment`)

### A-0346
- **Idea:** Build the failure taxonomy first: an empirically derived, model-agnostic taxonomy of segmentation failure modes (from large-scale clustering of error cases across models), tested for coverage, stability, and transferability as a reporting standard.
- **Problem:** Failure discussion lacks shared vocabulary; each paper invents categories, blocking cumulative failure science.
- **Hypothesis:** Unsupervised clustering of error signatures across many models converges to a stable taxonomy (~15–25 modes) that covers >90% of errors, transfers to unseen models, and predicts which mitigation family fixes each mode.
- **Why Important:** A validated taxonomy is infrastructure for the entire reliability field — the enabling deliverable for everything else.
- **Why Possibly Novel (hypothesized):** Data-derived cross-model failure taxonomies appear unattempted for segmentation.
- **Minimal Experiment:** Collect 50k error cases across 10 models; cluster error signatures; validate coverage/stability on held-out models; test mitigation predictiveness on a subset.
- **Main Risk:** Clustering granularity choices shape the taxonomy subjectively.
- **Cluster:** `failure-prediction-deployment`

### A-0347
- **Idea:** Test failure forecasting from inputs alone: predicting per-image failure probability before running the model (from cheap image statistics + a tiny forecaster), enabling pre-inference routing decisions at near-zero cost.
- **Problem:** Failure prediction currently requires running the model; pre-inference forecasting would enable routing, pricing, and batching decisions earlier and cheaper.
- **Hypothesis:** A forecaster on cheap statistics (resolution, clutter proxies, blur, domain classifier) predicts model failure with AUROC>0.75 — capturing most of post-hoc confidence's routing value at a fraction of the cost.
- **Why Important:** Pre-inference triage restructures serving economics for high-volume pipelines.
- **Why Possibly Novel (hypothesized):** Pre-inference failure forecasting for segmentation appears unbuilt.
- **Minimal Experiment:** Train forecasters per model on labeled outcomes; compare routing value against post-hoc confidence at matched infrastructure cost.
- **Main Risk:** Forecast ceilings may be low if failures are content-specific.
- **Cluster:** `failure-prediction-deployment`

### A-0348
- **Idea:** Study the "wrongness visibility" spectrum: classifying model errors by how detectable they are to non-expert users (obvious vs. plausible-but-wrong), and testing whether plausible-wrongness is predictable and reducible by training interventions.
- **Problem:** Deployment harm scales with undetectable errors, not all errors; the visibility structure of segmentation errors is unmeasured.
- **Hypothesis:** A stable fraction of errors is rated "plausible" by users (undetectable without GT), this fraction varies substantially across models at equal accuracy, and plausibility-weighted training (penalizing confident coherent errors) reduces it measurably.
- **Why Important:** Optimizing for detectable-when-wrong is a distinct, deployment-critical objective the field ignores.
- **Why Possibly Novel (hypothesized):** Error-visibility measurement and optimization appear new.
- **Minimal Experiment:** User-rate error detectability across models; verify inter-model variance at matched accuracy; run the plausibility-penalty training intervention.
- **Main Risk:** Detectability ratings depend on user expertise and task framing.
- **Cluster:** `failure-prediction-deployment`

### A-0349
- **Idea:** Investigate confidence communication contracts: designing and testing model output "contracts" (e.g., "boundary within ±k px at 95%") that downstream engineers can build against, and measuring contract violation rates of current models.
- **Problem:** Model outputs lack engineering-grade specifications; downstream systems guess tolerances, causing integration failures.
- **Hypothesis:** Contract-style outputs (calibrated bounds per mask property) can be constructed post hoc with violation rates <5% in-domain, and contract-checking flags domain shift earlier than accuracy monitoring.
- **Why Important:** Contracts are how every other engineering discipline consumes components; vision needs them for real systems integration.
- **Why Possibly Novel (hypothesized):** Engineering-contract formulation for segmentation outputs appears new.
- **Minimal Experiment:** Define property contracts; calibrate on held-out data; measure violation rates in/out of domain; test violation-based shift detection.
- **Main Risk:** Contracts tight enough to be useful may be violated too often to be credible.
- **Cluster:** `failure-prediction-deployment`

### A-0350
- **Idea:** Test disagreement-based regression testing for model updates: whether output diffs on an unlabeled canary corpus predict which capabilities changed between model versions, enabling label-free release qualification.
- **Problem:** Model updates ship on aggregate benchmarks; capability-level regressions hide in aggregate stability, and labeling release-qualification suites is slow.
- **Hypothesis:** Structured diff analysis (where and how outputs changed on canaries) localizes capability changes with high agreement to labeled ground truth findings, enabling qualification decisions without new labels.
- **Why Important:** Release engineering for vision models needs cheap, sensitive regression instruments.
- **Why Possibly Novel (hypothesized):** Label-free capability-diff qualification appears undeveloped.
- **Minimal Experiment:** Compare model version pairs on canaries and labeled suites; measure agreement of diff-based vs. labeled findings; optimize canary composition.
- **Main Risk:** Diffs conflate improvements with regressions without labels; needs directional heuristics.
- **Cluster:** `failure-prediction-deployment`

### A-0351
- **Idea:** Study human-model complementarity zones: mapping where model+human verification adds accuracy over either alone (as a function of case difficulty and model confidence), optimizing reviewer routing by measured complementarity rather than confidence alone.
- **Problem:** Review routing assumes humans fix what models miss; the actual complementarity structure (humans also fail on model-hard cases) is unmeasured.
- **Hypothesis:** Complementarity is non-monotone in difficulty: humans add most value in a mid-difficulty band, while model-hard cases are also human-hard — so confidence-based routing over-allocates review to unfixable cases, and complementarity-based routing improves corrected-output quality at equal review budget.
- **Why Important:** Review budgets are the main cost of quality-critical pipelines; routing by measured complementarity is directly monetizable.
- **Why Possibly Novel (hypothesized):** Complementarity-zone mapping for segmentation QA appears absent.
- **Minimal Experiment:** Collect human corrections across difficulty/confidence strata; map complementarity; compare routing policies at fixed budgets.
- **Main Risk:** Human performance varies by workforce, limiting map portability.
- **Cluster:** `failure-prediction-deployment`

### A-0352
- **Idea:** Investigate failure contagion in downstream chains: how a single upstream mask error propagates through multi-stage pipelines (measure→decide→act), identifying amplification vs. attenuation stages and designing propagation-aware error budgets.
- **Problem:** Error budgets are set per-component; propagation dynamics through real pipelines (amplification factors per stage) are unmeasured.
- **Hypothesis:** Error propagation is strongly stage-dependent (geometric measurement stages amplify boundary errors superlinearly; classification stages attenuate them), enabling propagation-aware budgets that reallocate accuracy requirements across the pipeline at equal end-task quality and lower total cost.
- **Why Important:** System-level error budgeting is how reliable engineering is done; vision pipelines currently lack it.
- **Why Possibly Novel (hypothesized):** Propagation-factor measurement through vision pipelines appears rare.
- **Minimal Experiment:** Instrument 3 real pipeline archetypes; inject controlled upstream errors; measure end-task degradation curves per error type; derive budgets.
- **Main Risk:** Pipeline archetypes may not generalize across industries.
- **Cluster:** `failure-prediction-deployment`

### A-0353
- **Idea:** Test the monitoring-signal hierarchy for silent degradation: ranking practical label-free signals (confidence drift, output-statistic drift, disagreement with a shadow model, input-distribution drift) by detection latency and false-alarm cost across realistic degradation scenarios.
- **Problem:** Production monitoring picks signals by intuition; their comparative detection operating characteristics for segmentation degradation are unmeasured.
- **Hypothesis:** Shadow-model disagreement dominates on detection latency for model-side degradations while input-drift signals dominate for world-side changes — a two-axis hierarchy enabling principled monitoring design at known alarm budgets.
- **Why Important:** Silent degradation is the top operational fear for deployed vision; evidence-based monitoring design addresses it directly.
- **Why Possibly Novel (hypothesized):** Comparative monitoring-signal benchmarking for segmentation appears absent.
- **Minimal Experiment:** Simulate degradation scenario suites (model rot, drift, sensor faults); measure per-signal detection ROC and latency; publish the hierarchy.
- **Main Risk:** Scenario realism drives conclusions; needs practitioner-validated scenarios.
- **Cluster:** `failure-prediction-deployment`

### A-0354
- **Idea:** Study explanation utility for segmentation failures: whether attaching causal explanations to failures ("missed due to backlight") changes user trust and behavior more appropriately than confidence scores, measured by calibrated reliance metrics.
- **Problem:** Explanations are assumed to help users calibrate reliance; for segmentation failures this is untested and explanations might induce over-trust.
- **Hypothesis:** Cause-attributed failure explanations improve appropriate reliance (accepting good masks, rejecting bad ones) over confidence-only displays, but only when explanations are verified-accurate — inaccurate explanations damage reliance below baseline, quantifying the accuracy bar explanations must meet.
- **Why Important:** Defines evidence-based requirements for explanation features shipping in vision products.
- **Why Possibly Novel (hypothesized):** Reliance-calibration testing of segmentation explanations appears new.
- **Minimal Experiment:** User study crossing explanation presence×accuracy on verification tasks; measure reliance appropriateness and downstream decision quality.
- **Main Risk:** Constructing verified-accurate explanations requires solving attribution first for the study set.
- **Cluster:** `failure-prediction-deployment`

### A-0355
- **Idea:** Investigate versioned-behavior pinning: techniques to guarantee that specific certified behaviors (golden-case outputs) survive model updates exactly, and measure the capability cost of pinning growing golden sets.
- **Problem:** Updates improve averages but break specific certified behaviors customers depend on; behavior-pinning technology and its cost curve are undeveloped.
- **Hypothesis:** Constrained update methods (output-matching losses on golden sets) preserve pinned behaviors exactly with capability costs growing measurably but sublinearly in golden-set size up to a practical ceiling — defining the feasible scale of behavioral guarantees.
- **Why Important:** Enterprise and regulated adoption depends on behavioral stability guarantees that currently don't exist.
- **Why Possibly Novel (hypothesized):** Pinning-cost curves for vision model updates appear unmeasured.
- **Minimal Experiment:** Fine-tune with golden-set constraints at growing set sizes; measure pin fidelity and general-capability costs; locate the practical ceiling.
- **Main Risk:** Exact pinning may be impossible under architecture changes, requiring tolerance definitions.
- **Cluster:** `failure-prediction-deployment`

### A-0356
- **Idea:** Test the audit-probe suite concept: a small standardized set of diagnostic inputs (synthetic + curated) whose output pattern fingerprints a black-box segmentation model's capability profile, enabling third-party auditing without weights or large-scale evaluation.
- **Problem:** Third parties (regulators, customers) cannot audit black-box vision APIs efficiently; compact diagnostic instruments don't exist.
- **Hypothesis:** A few hundred designed probes predict a model's full capability-battery profile with high fidelity (rank correlation >0.85 per capability), because capabilities constrain responses to designed probes strongly — making compact auditing information-theoretically feasible.
- **Why Important:** Auditing infrastructure is prerequisite for accountability in the vision-API economy.
- **Why Possibly Novel (hypothesized):** Compact capability-fingerprinting suites for segmentation appear unconstructed.
- **Minimal Experiment:** Design probe candidates; fit probe-to-battery predictors across many models; validate on held-out models including API-only ones.
- **Main Risk:** Probes may be gamed once public; needs private/rotating variants.
- **Cluster:** `failure-prediction-deployment`

### A-0357
- **Idea:** Study cost-of-error asymmetry elicitation: methods to extract application-specific error cost functions from domain experts (which errors matter how much), and whether cost-aligned model selection differs materially from accuracy-based selection in practice.
- **Problem:** Model selection uses symmetric metrics while real costs are asymmetric; the practical decision gap this creates is unmeasured.
- **Hypothesis:** Elicited cost functions across 5 application domains re-rank candidate models materially relative to mIoU ranking in most domains, with cost-aligned selection yielding measurable end-metric improvements in deployment simulations.
- **Why Important:** Bridges the last mile between benchmarks and application value with a reusable elicitation method.
- **Why Possibly Novel (hypothesized):** Systematic cost-elicitation for segmentation selection appears rare.
- **Minimal Experiment:** Run structured elicitation with domain experts; construct cost-weighted metrics; compare selections and simulate deployment outcomes.
- **Main Risk:** Elicited costs may be unstable across experts within a domain.
- **Cluster:** `failure-prediction-deployment`

### A-0358
- **Idea:** Investigate abstention interface design: how a segmentation system should *say* "I can't do this region" (partial masks with holes vs. explicit unknown-region maps vs. refusal), measured by downstream human-system team performance rather than model metrics.
- **Problem:** Abstention research optimizes when to abstain; how to represent partial abstention in dense outputs for human consumption is undesigned and untested.
- **Hypothesis:** Explicit unknown-region maps (tri-state masks) outperform silent low-confidence holes and whole-image refusal on team task performance, because they preserve usable partial work while directing human attention — establishing tri-state output as the right interface primitive.
- **Why Important:** Interface primitives standardize across the industry; getting abstention representation right has ecosystem leverage.
- **Why Possibly Novel (hypothesized):** Abstention-representation studies for dense outputs appear new.
- **Minimal Experiment:** Implement three abstention interfaces; team-performance study on completion tasks with induced model uncertainty; compare throughput/quality.
- **Main Risk:** Results may depend on task time pressure and user training.
- **Cluster:** `failure-prediction-deployment`

### A-0359
- **Idea:** Test long-tail incident mining from deployment logs: whether clustering production near-failures (user corrections, low-confidence spikes) surfaces novel failure modes absent from all public benchmarks, quantifying the benchmark-deployment failure gap.
- **Problem:** The overlap between benchmark-measurable failures and production failures is unknown; deployment exhaust may contain a systematically different failure distribution.
- **Hypothesis:** A substantial fraction (>30%) of production failure clusters have no benchmark counterpart (novel modes: UI overlays, sensor artifacts, adversarial user content), quantifying how much reliability work benchmarks structurally cannot see.
- **Why Important:** Measures the blind spot of the entire benchmark-driven reliability paradigm and motivates deployment-integrated evaluation.
- **Why Possibly Novel (hypothesized):** Benchmark-deployment gap quantification appears undone for segmentation.
- **Minimal Experiment:** Partner with a deployed annotation tool; mine and cluster incidents; match clusters against benchmark taxonomies; report the unmatched fraction.
- **Main Risk:** Requires production data access and careful privacy handling.
- **Cluster:** `failure-prediction-deployment`

### A-0360
- **Idea:** Study reliability economics end-to-end: constructing the full cost curve of segmentation reliability (model cost + review cost + error cost) across operating points, and testing whether current deployments sit far from cost-optimal points in reconstructable case studies.
- **Problem:** Reliability decisions (model size, review rate, thresholds) are made piecemeal; the joint cost optimization they implicitly attempt is never solved explicitly.
- **Hypothesis:** Reconstructed cost curves for real case studies show deployments operating far from optimal (typically over-reviewing easy strata and under-reviewing hard ones), with the optimality gap quantifiable and recoverable by joint optimization.
- **Why Important:** Translates the entire reliability research agenda into the economic terms deployment decisions actually use.
- **Why Possibly Novel (hypothesized):** Joint reliability-economics optimization for segmentation appears unformalized.
- **Minimal Experiment:** Reconstruct cost structures for 3 case studies; fit cost curves across operating points; compute and validate optimality gaps against recorded outcomes.
- **Main Risk:** Cost data access and generalizability across organizations.
- **Cluster:** `failure-prediction-deployment`

---

## Sub-cluster 25 (bonus): Cross-cutting ideas (`bonus-cross-cutting`)

### A-0361
- **Idea:** Test the "one benchmark to break them all" inverse-design method: automatically searching image space (via generative models with realism constraints) for inputs that maximize disagreement across all top segmentation models, characterizing the shared frontier of the field's capability.
- **Problem:** Model-specific stress tests miss the shared frontier — inputs hard for every model — which defines the field's collective blind spot.
- **Hypothesis:** Realism-constrained disagreement maximization discovers coherent input families (not noise) where all models fail together, and these families predict future architecture-independent failures better than any single-model analysis.
- **Why Important:** The shared frontier is the field's true to-do list, discoverable automatically.
- **Why Possibly Novel (hypothesized):** Multi-model disagreement-maximizing input synthesis for segmentation appears new.
- **Minimal Experiment:** Optimize latent codes of a generative model for cross-model disagreement under realism constraints; cluster discovered families; validate their difficulty on held-out models.
- **Main Risk:** Generative-model bias constrains the searchable input space.
- **Cluster:** `bonus-cross-cutting`

### A-0362
- **Idea:** Study capability arbitrage between prompting and fine-tuning: for a fixed target task, mapping when prompt engineering alone matches PEFT (and when it cannot), as a function of task distance from pretraining — a decision boundary for the cheapest adequate adaptation.
- **Problem:** Teams choose between prompting and tuning by habit; the decision boundary in task space is unmeasured.
- **Hypothesis:** Prompt-only adaptation matches PEFT within noise for tasks below a measurable representational-distance threshold and falls off a cliff beyond it, giving a cheap pre-test (feature-distance measurement) that predicts the right adaptation tier.
- **Why Important:** A validated decision rule saves the ecosystem enormous duplicated experimentation.
- **Why Possibly Novel (hypothesized):** Prompting-vs-PEFT boundary mapping for vision appears absent.
- **Minimal Experiment:** For 20 tasks spanning distances, exhaust prompt-side optimization and compare to PEFT; regress the gap on distance measures; validate the pre-test.
- **Main Risk:** "Exhausting" prompt optimization is ill-defined; needs a standardized budget.
- **Cluster:** `bonus-cross-cutting`

### A-0363
- **Idea:** Investigate the segmentation "Turing test": whether experts can distinguish model masks from human annotations at various quality tiers, using detectability as a model-free quality milestone and identifying the residual tells.
- **Problem:** Progress lacks an absolute (non-benchmark) milestone; indistinguishability-from-human provides one, along with a catalog of remaining tells.
- **Hypothesis:** Current top models fail expert indistinguishability specifically on ambiguity-resolution style and boundary micro-conventions (not accuracy), and the identified tells define a concrete residual research agenda.
- **Why Important:** Reframes "how good are we" in absolute terms and extracts an actionable tell list.
- **Why Possibly Novel (hypothesized):** Forensic indistinguishability studies for masks appear unconducted.
- **Minimal Experiment:** Expert forced-choice studies on mask provenance across quality tiers; analyze discriminating features via post-hoc interviews and feature analysis.
- **Main Risk:** Tells may reflect annotation-tool style rather than intelligence gaps.
- **Cluster:** `bonus-cross-cutting`

### A-0364
- **Idea:** Test cross-task failure coupling within one VFM: whether an image that causes segmentation failure also elevates failure probability for detection/depth/captioning heads on the same backbone, measuring shared-representation risk concentration.
- **Problem:** Multi-head products assume head failures are independent; shared backbones likely couple them, invalidating redundancy assumptions inside a single system.
- **Hypothesis:** Per-image failure indicators across heads are substantially correlated (far above content-difficulty baselines), concentrated in backbone-attributable cases — quantifying the systemic-risk cost of representation sharing.
- **Why Important:** Within-system redundancy design (fallback heads) depends on knowing this coupling.
- **Why Possibly Novel (hypothesized):** Intra-model cross-task failure coupling appears unmeasured.
- **Minimal Experiment:** Evaluate multiple heads on shared backbones across corpora; measure failure correlations; decompose into backbone vs. head causes via representation-swap controls.
- **Main Risk:** Content difficulty inflates correlations; needs careful baselining.
- **Cluster:** `bonus-cross-cutting`

### A-0365
- **Idea:** Study annotation instruments as measurement devices: applying metrology principles (calibration standards, traceability, uncertainty budgets) to segmentation ground truth, and testing whether metrology-grade GT changes model rankings.
- **Problem:** GT is treated as truth rather than measurement; without uncertainty budgets and standards, benchmark conclusions lack metrological validity.
- **Hypothesis:** Metrology-grade annotation (calibrated annotators, reference standards, stated uncertainty) yields GT whose uncertainty budgets overturn a measurable fraction of published model comparisons, establishing the necessity of measurement science for benchmarks.
- **Why Important:** Imports a mature discipline's rigor into the field's weakest foundation.
- **Why Possibly Novel (hypothesized):** Metrological treatment of segmentation GT appears unattempted.
- **Minimal Experiment:** Develop calibration protocols and reference objects; re-annotate benchmark samples metrologically; propagate uncertainty into model comparisons.
- **Main Risk:** Metrology-grade annotation cost limits scale.
- **Cluster:** `bonus-cross-cutting`

### A-0366
- **Idea:** Test "model paleontology": inferring properties of a black-box model's training data (mask sources, domain mixture, annotation tools) purely from behavioral probes, validated on models with known provenance.
- **Problem:** Training-data transparency is absent for commercial models; behavioral inference methods for data provenance are undeveloped for vision.
- **Hypothesis:** Behavioral probes (style reproduction, convention preferences, fingerprint statistics) recover training-mixture properties of known-provenance models with useful accuracy, enabling third-party provenance auditing of black boxes.
- **Why Important:** Provenance auditing supports licensing enforcement, bias assessment, and procurement decisions.
- **Why Possibly Novel (hypothesized):** Behavioral data-provenance inference for segmentation models appears new.
- **Minimal Experiment:** Train models on known mixtures; develop probe batteries; measure mixture-recovery accuracy; test on public models with documented data.
- **Main Risk:** Provenance signals may be washed out at scale or by data overlap.
- **Cluster:** `bonus-cross-cutting`

### A-0367
- **Idea:** Investigate the interaction of image generation and segmentation models sharing training corpora: whether segmentation models are systematically better at segmenting generated images (distribution kinship), creating feedback risks as generated content floods the web.
- **Problem:** Generated imagery is entering both the web and training corpora; whether segmenters treat generated content as "easier in-distribution" data — biasing dataset curation loops — is unmeasured.
- **Hypothesis:** Segmentation quality on generated images exceeds matched real images (kinship effect), causing confidence-filtered auto-curation to over-select generated content and compounding synthetic drift across generations.
- **Why Important:** Identifies a concrete mechanism of ecosystem-level synthetic contamination with measurable early indicators.
- **Why Possibly Novel (hypothesized):** Kinship-driven curation-bias analysis appears new.
- **Minimal Experiment:** Compare segmentation quality/confidence on matched real-vs-generated pairs; simulate curation loops; measure synthetic-fraction drift.
- **Main Risk:** Matching real and generated content fairly is nontrivial.
- **Cluster:** `bonus-cross-cutting`

### A-0368
- **Idea:** Study attention-free segmentation foundations: whether state-space or convolutional architectures at matched scale reproduce SAM-class promptable behavior, isolating which observed failure modes are attention-specific vs. task-intrinsic.
- **Problem:** All promptable-segmentation phenomenology comes from attention architectures; without architectural controls, failures cannot be attributed to attention vs. the task itself.
- **Hypothesis:** Matched-scale attention-free models reproduce most aggregate performance but differ characteristically on long-range coherence and prompt-sensitivity failure modes, cleanly splitting the failure taxonomy into architectural and intrinsic parts.
- **Why Important:** Attribution to architecture vs. task guides where the next architectural generation should differ.
- **Why Possibly Novel (hypothesized):** Controlled cross-architecture failure phenomenology appears missing.
- **Minimal Experiment:** Train matched promptable models (attention vs. SSM/conv) on identical data; run the full failure battery; classify failure modes by architecture dependence.
- **Main Risk:** Matched training at meaningful scale is expensive.
- **Cluster:** `bonus-cross-cutting`

### A-0369
- **Idea:** Test knowledge-decay forecasting for deployed VFMs: modeling how a frozen model's real-world performance will decay over future years (from world-drift statistics), producing "shelf-life certificates" per application domain.
- **Problem:** Frozen models decay as the world drifts, but deployments lack quantitative shelf-life estimates for planning retraining budgets.
- **Hypothesis:** Domain-specific decay rates estimated from historical world-drift (product churn, style change velocity) forecast future performance decay within useful error bars, validated retrospectively on old models evaluated across the intervening years.
- **Why Important:** Shelf-life certificates convert vague "models rot" anxiety into budgetable maintenance schedules.
- **Why Possibly Novel (hypothesized):** Quantitative shelf-life forecasting for vision models appears unbuilt.
- **Minimal Experiment:** Retrospectively evaluate decade-old models on year-stratified data; fit decay models per domain; validate forecasts on held-out years.
- **Main Risk:** Historical decay may not extrapolate through structural breaks (new content types).
- **Cluster:** `bonus-cross-cutting`

### A-0370
- **Idea:** Investigate minimal architectures for the prompt-to-mask function: distilling the entire promptable-segmentation behavior into interpretable-by-construction models (decision-tree/program hybrids over features) to measure how much of SAM's behavior is simple, and where irreducible complexity lives.
- **Problem:** The intrinsic complexity of the promptable-segmentation function is unknown — how much of SAM is doing something simple that we could write down?
- **Hypothesis:** A large fraction of SAM's input-output behavior (hypothesized >70% of cases) is reproducible by compact interpretable programs over frozen features, with residual cases concentrating in ambiguity resolution — locating the genuinely complex core of the capability.
- **Why Important:** Separating the simple bulk from the complex core reshapes both efficiency and interpretability agendas.
- **Why Possibly Novel (hypothesized):** Behavioral complexity decomposition of promptable segmentation appears unattempted.
- **Minimal Experiment:** Fit interpretable surrogates to SAM behavior at scale; measure coverage-fidelity curves; characterize the non-surrogatable residual.
- **Main Risk:** Surrogate coverage may be inflated by easy-case abundance; needs difficulty-stratified reporting.
- **Cluster:** `bonus-cross-cutting`

### A-0371
- **Idea:** Study open-weight vs. API-model behavioral divergence over time: longitudinally fingerprinting commercial segmentation APIs to detect silent model changes, measuring the rate and character of unannounced behavioral drift users are exposed to.
- **Problem:** API users cannot see model swaps; the frequency and impact of silent changes on segmentation behavior is undocumented, undermining reproducibility of anything built on APIs.
- **Hypothesis:** Longitudinal probing detects unannounced behavioral changes at measurable rates, with changes concentrated in confidence calibration and boundary conventions — quantifying the reproducibility risk of API dependence for scientific and industrial users.
- **Why Important:** Evidence about silent drift informs the build-on-API vs. self-host decision and motivates change-disclosure norms.
- **Why Possibly Novel (hypothesized):** Longitudinal API-drift measurement for vision appears unconducted.
- **Minimal Experiment:** Probe segmentation APIs on fixed suites at regular intervals for months; detect changepoints; characterize what changed.
- **Main Risk:** Requires sustained monitoring infrastructure and careful terms-of-service compliance.
- **Cluster:** `bonus-cross-cutting`

### A-0372
- **Idea:** Test unified failure-cost dashboards as research infrastructure: whether presenting per-model failure taxonomies, tail metrics, and cost-weighted scores in a standardized public artifact changes which models practitioners select, measured by observed selection behavior versus leaderboard defaults.
- **Problem:** Rich evaluation exists in papers but selection behavior follows single-number leaderboards; whether better information presentation changes real decisions is an untested infrastructure hypothesis.
- **Hypothesis:** Practitioners given multi-dimensional failure dashboards select models that outperform leaderboard-default choices on their own downstream tasks in a majority of cases, demonstrating that evaluation-information presentation (not just content) materially affects field outcomes.
- **Why Important:** If presentation changes outcomes, evaluation infrastructure is an intervention point as powerful as new metrics.
- **Why Possibly Novel (hypothesized):** Selection-behavior experiments on evaluation presentation appear unconducted in vision.
- **Minimal Experiment:** Build dashboards for 10 models; run a selection study with practitioners having real downstream tasks; compare outcome quality of dashboard-informed vs. leaderboard-default selections.
- **Main Risk:** Study participants may not represent decision-makers in industry settings.
- **Cluster:** `bonus-cross-cutting`

---

## Catalog summary

- **Total ideas:** 372 (A-0001 through A-0372).
- **Stage:** Stage 1 volume generation — no filtering applied; novelty is hypothesized throughout and must be verified against literature before execution.
- **Coverage:** 25 sub-clusters spanning SAM-family failure modes (prompt sensitivity, video memory, concept prompting, medical shift, boundary quality, distillation), PEFT mechanics and catastrophic forgetting, calibration/uncertainty, small/thin objects, evaluation weaknesses, representation mismatch, detection failures, scaling/emergence, interactive dynamics, ambiguity, robustness, open-vocabulary grounding, data-centric biases, continual/test-time adaptation, architecture internals, 3D/geometry, compositionality/counting, failure prediction/deployment, and cross-cutting infrastructure questions.
- **Quality filter applied during generation:** every idea specifies a problem, a falsifiable core hypothesis, a minimal experiment, and a main risk; no "module A + module B" stacking ideas were included.
