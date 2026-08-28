# Stage 2 — Cluster A Survivors

**Reviewer:** Cloud Sub-Agent D (independent reviewer for Supervisor Windows7)
**Source:** `stage1_cluster_A_ideas.md` / `stage1_cluster_A_index.csv` from `origin/cursor/stage1-cluster-a-ideas-e2b2` (372 ideas, A-0001–A-0372).
**Full scores:** `stage2_cluster_A_scores.csv` (14 dimensions per idea + mean + decision + reason).

**Method notes:**
- Every idea was scored 1–10 on: Novelty, Significance, Scientific Question, Technical Soundness, Feasibility, Compute affordability, Dataset Availability, Baseline Availability, Not-Already-Published (inverted likelihood; **this is a judgment call, not a literature-search result**), Experimental Clarity, Venue Potential (CVPR/ICCV/ECCV/MICCAI), Risk, Potential Upside, Research ROI.
- Selection was **not** by mean score alone. The `mean_score` column excludes Risk. Several ideas with means above the keep line were killed (e.g., A-0189, A-0236, A-0116) for redundancy or fragility, and every PROTECT entry was retained *despite* its risk or mean because it satisfies an explicit protection criterion.
- Counts: **70 KEEP + 14 PROTECT = 84 survivors; 288 KILL.**

---

## KEEP (70)

### sam-prompt-sensitivity
- **A-0002** — Positional-encoding aliasing as the driver of click instability. Mechanistic, cheap Fourier analysis plus prompt-encoder-only retrain; falsifies cleanly either way.
- **A-0005** — Negative-click over-erosion law tied to mask-prior resolution. Concrete architectural bottleneck with a quantitative erosion law and a testable fix.

### sam2-video-memory
- **A-0016** — Forgetting curve of SAM2's memory bank: step-like (slot eviction) vs exponential (interference). Cheap controlled occlusions separate architectural from representational failure.
- **A-0017** — "Identity capture": stale memories causally blocking recovery, tested by memory surgery. Strong causal intervention with direct fix implications.
- **A-0030** — Did video pretraining damage SAM2's still-image ability vs SAM1? Cheap negative-transfer regression of wide community interest.

### sam3-concept-prompting
- **A-0031** — Relation-defined vs attribute-defined concept prompts: the grounding gap. Timely SAM3-era diagnosis with matched-difficulty design.
- **A-0032** — Exhaustivity failure: misses concentrate far from the visual prototype. Makes missed instances predictable a priori from the model's own embeddings.
- **A-0034** — Negative-concept prompting ("all animals except dogs") vs positive-query-plus-random-removal. The baseline sharply falsifies compositional negation.

### medsam-domain-shift
- **A-0047** — MedSAM segments plausible structures inside wrong boxes: no box-rejection capability. Clinically critical, cheaply demonstrable safety failure; MICCAI-strong.
- **A-0051** — MedSAM reproduces the majority training institution's annotation style on other institutions' data. Fresh data-provenance claim with audit value.
- **A-0053** — Shape-prior hallucination of healthy anatomy on pathological organs. Safety-critical, decomposable into anomalous-region vs typical-region error.

### boundary-quality
- **A-0061** — "Boundary Nyquist limit": contour error spectrum cut off by decoder resolution. Cheap, architecture-predictive law.
- **A-0062** — Do HQ-SAM-style gains survive soft multi-annotator boundaries, or are they metric gaming? Field-correcting evaluation claim.
- **A-0073** — Instance-instance boundaries are worse than instance-background at matched contrast. Isolates instance separation as a distinct boundary competence.

### mobile-distillation
- **A-0078** — Do students inherit the teacher's click-fragility maps? Natural experiment: MobileSAM (distilled) vs FastSAM (independent) vs EfficientSAM, no new training.
- **A-0080** — "Resolution honesty": effective resolution measured psychophysics-style with synthetic gap/protrusion charts. Exposes hollow high-res claims cheaply.
- **A-0084** — Efficient attention specifically breaks long-range mask coherence (fragmentation of extended objects). A hidden failure invisible in standard benchmarks.

### peft-mechanics
- **A-0092** — Required LoRA rank scales with intrinsic dimensionality of the domain shift. A clean quantitative law with direct configuration implications.
- **A-0093** — Adapter interference predicted by principal angles between update subspaces. Pre-merge compatibility test; timely for the adapter-merging ecosystem.
- **A-0104** — PEFT cannot inject inductive biases (scale-equivariance floor at any rank). Decision-relevant negative-result design with an equivariant-module control.

### peft-forgetting
- **A-0107** — Forgetting is mostly readout-level: original-decoder restore recovers zero-shot ability. Cheap 2×2 swap matrix; high practical value.
- **A-0113** — Vision-tower PEFT silently damages text-vision alignment even when vision probes look fine. Timely for VLM fine-tuning practice.
- **A-0120** — Population-level forgetting law fitted over 100+ public community fine-tunes. Ecosystem-as-natural-experiment; zero training cost.

### calibration-uncertainty
- **A-0128** — Confidence rises with clicks even when accuracy has plateaued. Crisp safety pathology of interactive loops; cheap scripted sessions.
- **A-0132** — Do "aleatoric" estimators actually predict annotator entropy, or just model error? A definitional audit of segmentation uncertainty claims.
- **A-0134** — Calibrated "emptiness": can promptable models say a prompt hits nothing? A real unmodeled output mode with pipeline value.

### small-thin-objects
- **A-0136** — Token-occupancy law: quality collapses below 1-token occupancy regardless of pixel count. Separates tokenization limits from information limits.
- **A-0137** — Small-object information survives the encoder but dies in the decoder (probe recovery of failed masks). Would redirect small-object work to decoders.
- **A-0146** — Instance separation collapses at a critical packing density scaling with output resolution. Extrapolable feasibility law for dense-instance workloads.

### evaluation-weakness
- **A-0151** — Re-ranking historical models under error-type-balanced metrics: has mIoU steered the field? Cheap, provocative meta-science.
- **A-0152** — Are top-model gaps on saturated benchmarks below the label-noise ceiling? Bootstrap-over-annotations could invalidate leaderboard ordering.
- **A-0162** — Statistical-power audit: what fraction of published deltas is below the minimum detectable effect? Cheap and rigorous with field-level consequences.

### representation-mismatch
- **A-0167** — Pixel-level map of what SAM features uniquely resolve vs CLIP features. Quantifies the mismatch as analysis, not fusion engineering.
- **A-0175** — Camera metadata (focal length, ISO, pipeline) decodable from VFM features acts as shortcut features. Provocative, cheap probes, deployment-relevant.
- **A-0178** — Prompts landing on register/artifact tokens causally degrade masks. Timely link from a known representation anomaly to a user-visible failure.

### detection-failures
- **A-0181** — DETR query "territories": regional misses predicted by count-to-slot-density ratio. Reframes crowded-scene failure as resource allocation.
- **A-0183** — Spatial background-prior contamination caps novel-class recall in high-prior regions. Clean synthetic-placement control available.
- **A-0191** — Long-tail failure in open-vocab detectors is naming, not localization. Cheap decisive decomposition on LVIS tail; inverts closed-set wisdom.
- **A-0194** — Convention translator upper-bounds how much cross-dataset AP loss is annotation convention. Reframes "domain gap" claims.

### scaling-emergence
- **A-0196** — Capability-resolved scaling exponents (small objects vs mean IoU) from existing checkpoint ladders. Answers whether scale alone will close specific gaps.
- **A-0198** — Emergence-vs-metric-artifact test for prompt composition, continuous vs thresholded metrics. Vision-side contribution to the emergence debate.
- **A-0200** — Inverse scaling: larger VFMs increasingly override pixel evidence with semantic priors. Provocative and checkpoint-ladder cheap.

### interactive-loop
- **A-0211** — Humans co-adapt to model quirks within a session, contaminating static-simulator benchmarks. Modest-n study with large evaluative consequence.
- **A-0221** — Novices over-defer to confident wrong suggestions; assisted labels can be worse than unassisted. Ecosystem-critical claim about AI-assisted annotation.

### ambiguity-multihypothesis
- **A-0226** — Empirical taxonomy of segmentation ambiguity + does SAM's 3-slot output truncate it? Grounds the whole multi-hypothesis agenda.
- **A-0227** — Is hypothesis diversity input-adaptive or a fixed part/whole/background template? Sharp, cheap calibration-of-ambiguity test.
- **A-0237** — Any-valid-interpretation scoring: how much of "error" is granularity taste? Benchmark-correcting rescoring of existing models.

### robustness-shift
- **A-0242** — Split corruptions into interaction-recoverable vs unrecoverable (readout vs representation damage). Operationally decisive and cheap.
- **A-0243** — Adversarial prompts and certified prompt-robustness radii — robustness over prompt space, not pixel space. An unclaimed formal object.

### open-vocab-grounding
- **A-0256** — Linguistic-construct-stratified referring failures; comparatives/negation resist scaling. Identifies a scale-resistant linguistic core.
- **A-0257** — Reporting bias in text corpora predicts which attributes are ungroundable, beyond visual frequency. Causal language-side account with a cheap partial-correlation design.
- **A-0262** — Attribute-object binding failures in segmentation follow a similarity-retrieval account. Distractor-controlled scenes make the mechanism testable.

### data-centric-bias
- **A-0271** — SA-1B-scale annotation-pipeline fingerprints (curvature spectra, complexity ceilings) inherited by every downstream model. Timely data-ecology claim.
- **A-0272** — Model-collapse dynamics for segmentation self-training: boundary detail and rare morphology die first. Small-scale generations affordable and decision-relevant.
- **A-0275** — Where do human labels still beat model labels per dollar? Stratum-resolved marginal value steers annotation budgets in the foundation era.

### continual-tta
- **A-0292** — Continual improvement as prompt-policy learning over frozen weights: forgetting-free by construction. Clean safety property; recurring-context workloads.
- **A-0296** — Prompt-consistency as a vision-native TTA objective, with collapse-safety comparison against entropy minimization.

### architecture-internals
- **A-0302** — Mask-token capacity law: masks whose description length exceeds token capacity fail predictably; threshold scales with token count.
- **A-0313** — "Individuation depth" (layer where touching instances separate) predicts instance-separation ability across architectures.
- **A-0314** — Activation steering for interpretable mask control (grow/shrink, tighten, include-attachments). Training-free control; imports a hot LLM tool with clear vision semantics.

### 3d-volumetric-geometry
- **A-0316** — 3D-consistency defect of 2D promptable masks vs viewpoint separation. Underpins every SAM-to-3D lifting pipeline; cheap with existing multi-view data.
- **A-0320** — Latent amodal knowledge in modal-trained models, elicited by prompts and a light readout head. Strong scientific and practical stakes.
- **A-0330** — Reflections segmented as real objects while reflection-vs-real is linearly decodable inside features. An unread internal signal with a cheap probe test.

### compositional-counting
- **A-0334** — Scene-level containment-coherence score: do multi-granularity masks form a consistent hierarchy? Exposes contradictions no per-mask metric sees.
- **A-0336** — Object permanence: is occluded-object state maintained in memory features or reconstructed at reappearance? Probe-decay timing gives a crisp hybrid account.

### failure-prediction-deployment
- **A-0346** — Empirically derived, model-agnostic failure taxonomy with coverage/stability/transfer tests. Foundational reporting infrastructure.
- **A-0348** — "Plausible-but-wrong" error fraction as a distinct safety axis that varies across models at matched accuracy.
- **A-0356** — Compact audit-probe suite that fingerprints black-box segmentation capability profiles. Timely for API-era accountability.

### bonus-cross-cutting
- **A-0361** — Realism-constrained input search maximizing cross-model disagreement: maps the field's shared capability frontier.
- **A-0367** — Segmentation models are better on generated images (distribution kinship), so confidence-filtered curation over-selects synthetic content. Timely feedback-loop result.

---

## PROTECTED (14) — retained regardless of mean score

Labeled by protection criterion. These are survivors *in addition to* the 70 keeps.

### High-risk / high-reward
- **A-0100** (peft-mechanics) — Transport LoRA adapters across backbone scales via a feature-space map. Layer correspondence may not exist; if it does, PEFT economics change.
- **A-0154** (evaluation-weakness) — Test-set contamination detected from annotation-style regurgitation, no training-data access needed. Style-convergence confound may sink it; forensic payoff is huge.
- **A-0300** (continual-tta) — Certified adaptation: PEFT families with provable output-deviation bounds for regulated in-field updates. Bounds may be vacuous; success creates a new deployment class.
- **A-0366** (bonus) — "Model paleontology": inferring training-data properties of black boxes from behavioral probes. Signals may wash out at scale; auditing payoff is large.

### Simple but counter-intuitive
- **A-0003** (sam-prompt-sensitivity) — Permuting identical clicks changes the final mask. Order-invariance is silently assumed by every interactive benchmark; days of compute to test.
- **A-0074** (boundary-quality) — Treat the decoder as a fixed blur kernel and Wiener-deconvolve mask logits, training-free. Probably fails (nonlinear); cheap to find out; strange if it works.
- **A-0087** (mobile-distillation) — Distilled students beat their teacher in stable, characterizable regimes ("beneficial compression").
- **A-0094** (peft-mechanics) — Prompt-encoder-only tuning recovers most of full-PEFT gains for many domains: "domain gaps" as prompt-interpretation gaps.
- **A-0119** (peft-forgetting) — "Forgotten" capabilities revived by prompt patterns alone: suppression, not erasure.
- **A-0142** (small-thin-objects) — Removing context *improves* small-object segmentation below a size threshold, reversing the context-helps assumption.

### Huge reviewer-disagreement potential
- **A-0169** (representation-mismatch) — DINO's celebrated object-centric attention as an epiphenomenon of local smoothness. A debunk that will split any review panel.
- **A-0317** (3d-volumetric-geometry) — Trompe-l'oeil / painted-shadow cue conflicts: geometric information present in features but unused by segmentation decisions.

### Falsifiable with a cheap experiment
- **A-0024** (sam2-video-memory) — Identical-twin-object crossovers: SAM2 identity at chance would prove memory is appearance-only. One synthetic rendering pipeline, one number.
- **A-0068** (boundary-quality) — SAM logits in translucent regions carry recoverable alpha-matte information despite binary training. One rank-correlation on matting datasets.

---

*Not-already-published scores are reviewer judgment only; each surviving idea still requires a real literature check before execution (as the Stage 1 provenance note also demands). No citations were consulted or invented in this review.*
