# P1 Wave A — Generator A shard: SAM / foundation-model adaptation / PEFT / promptable-segmentation failure modes

- **windows_id**: Windows13 (locked; lock branch `cursor/windows13-p0-init-implementation-d93f`)
- **task_id**: `p1_gen_a_sam_foundation_peft` (role: generator, Wave A)
- **idea_count**: 102
- **status of novelty claims**: every `why_possibly_novel` is a HYPOTHESIS only. No verified novelty is claimed anywhere in this shard; Wave B dedup/verification is downstream.
- **evidence policy**: no invented papers, numbers, datasets, or results. Prior work is cited only where the generator is confident it exists (SAM, SAM 2, LoRA, adapters, VPT, BitFit, MAE, DINO, CKA, MobileSAM/FastSAM/EfficientSAM, HQ-SAM, ToMe, model soups, task arithmetic, texture-bias and registers papers, typographic attacks on CLIP). Everything else is labeled HYPOTHESIS or MODEL SPECULATION inline.

## Cluster index

| Cluster | Count | id_seed range |
|---|---|---|
| `prompt_geometry_failure_modes` | 10 | W13-P1-A-001 – W13-P1-A-010 |
| `what_peft_actually_learns` | 12 | W13-P1-A-011 – W13-P1-A-022 |
| `iou_head_calibration_uncertainty` | 8 | W13-P1-A-023 – W13-P1-A-030 |
| `encoder_representation_myths` | 10 | W13-P1-A-031 – W13-P1-A-040 |
| `decoder_token_mechanics` | 8 | W13-P1-A-041 – W13-P1-A-048 |
| `sam2_video_memory` | 9 | W13-P1-A-049 – W13-P1-A-057 |
| `data_priors_sa1b` | 8 | W13-P1-A-058 – W13-P1-A-065 |
| `evaluation_methodology` | 7 | W13-P1-A-066 – W13-P1-A-072 |
| `robustness_adversarial` | 7 | W13-P1-A-073 – W13-P1-A-079 |
| `distillation_efficiency` | 6 | W13-P1-A-080 – W13-P1-A-085 |
| `adapter_ecosystem_continual` | 6 | W13-P1-A-086 – W13-P1-A-091 |
| `interaction_loops_human_factors` | 5 | W13-P1-A-092 – W13-P1-A-096 |
| `adaptation_interfaces` | 6 | W13-P1-A-097 – W13-P1-A-102 |

---

## Cluster: `prompt_geometry_failure_modes` (10 ideas)

### W13-P1-A-001 — SAM's output granularity (part vs whole) is a near-deterministic function of click position relative to the object's medial axis, not a reflection of genuine ambiguity resolution.

- **Problem**: Point-prompt ambiguity in SAM is treated as an inherent property of the image, but the model may instead read geometric cues in the click location as a hidden granularity dial, making interactive behavior unpredictable to users who do not know this convention.
- **Core hypothesis**: The scale of the mask SAM returns for a single point is predictable from purely geometric prompt features (distance to nearest boundary, distance to medial axis) independent of image semantics.
- **Falsifiable prediction**: For a fixed object, moving a click along a path from the medial axis to the boundary produces a monotone (or piecewise-monotone) shrinkage of the selected mask scale in a large fraction of objects; a semantic-only account predicts no such systematic geometric trend.
- **Why important**: If granularity is geometrically encoded, interactive segmentation UIs and click-simulation training policies are miscalibrated, and part/whole ambiguity benchmarks conflate geometry with semantics.
- **Why possibly novel**: HYPOTHESIS: prompt ambiguity papers report that multiple valid masks exist, but a quantitative geometric law linking click coordinates to selected granularity has not, to my knowledge, been isolated as a controlled variable.
- **Community default belief (what is treated as true)**: Multimask output plus IoU ranking handles point ambiguity, and where a user clicks inside an object is roughly interchangeable.
- **Why that might be wrong**: SAM was trained with interactive click simulation where click placement correlates with intended mask scale, so the model plausibly internalized click geometry as a supervisory signal rather than treating clicks as scale-neutral.
- **Minimal falsification experiment**: Take 200 objects from any instance segmentation dataset with part annotations, sample 20 clicks per object along medial-axis-to-boundary rays, run frozen SAM, regress selected-mask area on geometric click features; falsified if geometric features explain little variance.
- **Fastest falsification experiment**: One afternoon: 20 objects, clicks sampled on a 5-point ray from centroid to boundary each, plot selected mask area vs normalized distance; a flat curve falsifies immediately.
- **Main risk**: The effect may be real but small compared to texture-driven variance, making it a curiosity rather than a usable law.
- **Evidence labels**: community_default_belief: KNOWN FACT (SAM's documented multimask design); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM (Kirillov et al. 2023) describes multimask ambiguity outputs; the geometric-law claim itself is MODEL SPECULATION

### W13-P1-A-002 — Box-prompt slack acts as an undocumented continuous scale prompt: SAM reads how loose a box is as a tolerance signal, so mask area inflates predictably with box dilation even when the object is unambiguous.

- **Problem**: Boxes are assumed to be binary localizers (object inside), but if slack is interpreted as a continuous signal, then detector-generated boxes with systematic slack bias silently shift downstream mask statistics.
- **Core hypothesis**: SAM's decoder uses box corner embeddings as a soft scale prior, so mask area is a smooth increasing function of box slack rather than a step function that saturates once the object is enclosed.
- **Falsifiable prediction**: Dilating ground-truth boxes by factors 1.0 to 1.5 produces a statistically significant positive slope of predicted-mask-area over box-area even for isolated objects on plain backgrounds, where the correct behavior is a flat curve.
- **Why important**: Detector-plus-SAM pipelines are ubiquitous; a slack-to-area transfer function would mean detector calibration errors propagate into segmentation bias in a lawful, correctable way.
- **Why possibly novel**: HYPOTHESIS: box robustness is usually reported as an average IoU drop under perturbation; treating slack as a signal with a measurable transfer function, and correcting for it, appears unexamined.
- **Community default belief (what is treated as true)**: A box prompt that contains the object suffices; small slack differences are noise the model is robust to.
- **Why that might be wrong**: During training, box prompts were synthesized from ground-truth masks with noise, so the model saw a correlation between slack magnitude and annotation looseness and had gradient pressure to exploit it.
- **Minimal falsification experiment**: On 500 isolated-object images, sweep box dilation, fit area-vs-slack slope per object, test whether the slope distribution is centered off zero; falsified if slopes are near zero once the object is enclosed.
- **Fastest falsification experiment**: Hours: 30 objects on clean backgrounds, 5 dilation levels, plot mean mask area vs dilation; a visible upward trend past enclosure confirms, flat falsifies.
- **Main risk**: Background clutter may dominate slack effects, making the transfer function image-dependent and useless for correction.
- **Evidence labels**: community_default_belief: EVIDENCE (common practice in detector+SAM pipelines); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM used noised box prompts in training per the paper; the transfer-function claim is MODEL SPECULATION

### W13-P1-A-003 — Although SAM encodes point sets symmetrically, PEFT-finetuned interactive variants develop click-order sensitivity, breaking the set-invariance contract users rely on.

- **Problem**: Interactive fine-tuning feeds clicks sequentially with previous-mask conditioning, which can implicitly convert an order-invariant interface into an order-sensitive one without anyone measuring it.
- **Core hypothesis**: Fine-tuning with iterative click simulation induces dependence on click order via the previous-mask input channel, so permuting the same click set changes final masks substantially more in adapted models than in frozen SAM.
- **Falsifiable prediction**: Permutation sensitivity (mean pairwise IoU across click-order permutations of the same click set) degrades significantly after iterative PEFT but stays near 1.0 for frozen SAM in single-shot multi-point mode.
- **Why important**: Order sensitivity makes evaluations irreproducible and user experience inconsistent; it also reveals that the previous-mask channel is a hidden state that adaptation methods must control.
- **Why possibly novel**: HYPOTHESIS: interactive segmentation work measures clicks-to-quality but I am not aware of order-permutation invariance being audited before vs after adaptation.
- **Community default belief (what is treated as true)**: Prompts are a set; giving the same clicks in any order yields the same segmentation.
- **Why that might be wrong**: Iterative training conditions each step on the previous mask, so the computation is a recurrence, and recurrences are generically order-sensitive unless explicitly symmetrized.
- **Minimal falsification experiment**: Take frozen SAM and one iteratively fine-tuned variant, sample 100 images with 4-click sets, evaluate all 24 permutations fed iteratively, compare permutation IoU variance between models.
- **Fastest falsification experiment**: Half a day: 20 images, 3-click sets, all 6 orders through an off-the-shelf iteratively-trained checkpoint vs frozen SAM; compare permutation spread.
- **Main risk**: Sensitivity might be dominated by the click simulator rather than the model, requiring careful separation of policy and model effects.
- **Evidence labels**: community_default_belief: KNOWN FACT (SAM prompt encoder is order-agnostic for simultaneous points); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: iterative click training exists in interactive segmentation (e.g., RITM line of work); the invariance-loss claim is MODEL SPECULATION

### W13-P1-A-004 — Negative clicks are strictly weaker than positive clicks in SAM: removing an over-segmented region takes systematically more clicks than adding an equivalent under-segmented region, revealing an asymmetric prompt algebra.

- **Problem**: Interfaces treat add and remove as symmetric operations, but if SAM's learned prompt algebra is asymmetric, correction budgets and simulated-click training curricula are misallocated.
- **Core hypothesis**: SAM's training distribution contained far fewer informative negative clicks, so the decoder's subtraction capacity is lower than its addition capacity for regions of matched area and boundary complexity.
- **Falsifiable prediction**: For matched error regions (same area, same boundary length), the median number of negative clicks needed to remove a false-positive region exceeds the median number of positive clicks needed to add a matched false-negative region.
- **Why important**: Asymmetry would change optimal correction strategies, click simulators, and the design of PEFT objectives for interactive use, and it exposes a measurable inductive bias of promptable decoders.
- **Why possibly novel**: HYPOTHESIS: click-count benchmarks aggregate over click types; a controlled matched-region add-vs-remove comparison isolating prompt algebra asymmetry appears missing.
- **Community default belief (what is treated as true)**: Positive and negative clicks are dual operations of roughly equal power.
- **Why that might be wrong**: Automatic mask generation and simulated interactive training mostly generate positive-first workflows, so negatives are rarer and later in the curriculum, plausibly yielding weaker learned operators.
- **Minimal falsification experiment**: Construct matched over- and under-segmentation errors by perturbing ground truth on 300 objects, run a fixed correction policy, compare click-count distributions for addition vs removal.
- **Fastest falsification experiment**: Hours: 30 objects, artificially dilate mask into background vs erode into object by the same area, count clicks to recover 95 percent IoU each way.
- **Main risk**: Constructing genuinely matched error regions is tricky; area and boundary matching may not equalize difficulty.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit in UI design, rarely stated); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM supports positive and negative points; the asymmetry claim is MODEL SPECULATION

### W13-P1-A-005 — Prompt-jitter robustness is a leading indicator of domain-shift robustness: PEFT-adapted SAMs lose click-jitter stability before their centroid-click accuracy drops, giving a label-free early-warning metric for over-adaptation.

- **Problem**: Detecting when PEFT starts to overfit currently requires held-out labeled masks; a label-free proxy computable from unlabeled target images would make adaptation safer and cheaper.
- **Core hypothesis**: Over-adaptation first manifests as a shrinking basin of prompt attraction (masks change under small click jitter) while best-prompt accuracy is still intact, because the model narrows its prompt-conditioned decision boundaries before moving them.
- **Falsifiable prediction**: During LoRA fine-tuning, a jitter-consistency score (mean IoU between masks from clicks jittered by a few pixels) on unlabeled data peaks and starts declining at least some epochs before held-out mIoU declines, across multiple domains.
- **Why important**: A label-free early-stopping signal for segmentation PEFT would be immediately practical and would support the deeper claim that robustness of the prompt map and robustness of the feature map are coupled.
- **Why possibly novel**: HYPOTHESIS: prompt-perturbation robustness has been used as an evaluation, but as an unsupervised early-stopping criterion for PEFT it appears unexplored.
- **Community default belief (what is treated as true)**: Early stopping for fine-tuning requires labeled validation data; prompt robustness is an output property, not a training signal.
- **Why that might be wrong**: The geometry of prompt space gives many free correlated probes per image, so instability there can be statistically detectable before mean accuracy moves.
- **Minimal falsification experiment**: Run LoRA adaptation on two public domain-shifted segmentation datasets, log jitter-consistency on unlabeled validation images and true mIoU per epoch, test whether jitter-consistency peaks earlier; falsified if the two curves peak together or in reverse order.
- **Fastest falsification experiment**: One training run with per-epoch checkpoints already suffices: overlay the two curves and check the ordering of their peaks.
- **Main risk**: Jitter consistency may saturate (masks fully stable) in easy domains, giving no early signal exactly where none is needed and none where needed.
- **Evidence labels**: community_default_belief: EVIDENCE (standard practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION for the coupling; LoRA (Hu et al. 2021) and SAM are VERIFIED PRIOR WORK

### W13-P1-A-006 — Most objects contain interior adversarial click points where frozen SAM returns near-zero-IoU masks, and these failure points cluster along internal texture boundaries rather than being random.

- **Problem**: Robustness reports average over click positions, hiding whether failures are diffuse noise or a structured, predictable subset of prompt space that users will inevitably hit.
- **Core hypothesis**: The click-to-mask map has a structured failure set: interior points near strong internal gradients (logos, seams, shadows) reliably produce part-like or degenerate masks, and this set is stable across model seeds and image augmentations.
- **Falsifiable prediction**: Failure-point maps (per-pixel IoU of the mask produced by clicking that pixel) computed twice under mild augmentation correlate strongly, and failure density near internal edges exceeds density in flat regions by a large factor.
- **Why important**: Structured failure sets can be predicted from the image alone, enabling click-guidance UIs and better click simulators, and they characterize what promptable segmentation actually conditions on.
- **Why possibly novel**: HYPOTHESIS: dense per-pixel prompt sweep maps exist informally in demos, but their stability, structure, and predictability from low-level image features have not been quantified as an object of study.
- **Community default belief (what is treated as true)**: Clicking well inside an object gives a good mask; failures come from ambiguous or tiny objects, not from specific interior positions.
- **Why that might be wrong**: The decoder attends locally around the prompt embedding location, so strong internal gradients can capture the attention and terminate region growing, making interior failure points systematic.
- **Minimal falsification experiment**: For 100 objects, compute dense click-IoU maps on a grid, correlate failure density with distance-to-internal-edge, and test map stability under augmentation; falsified if failures are spatially unstructured or unstable.
- **Fastest falsification experiment**: Hours: 10 objects with visible internal texture seams, 200-point grids, visualize click-IoU maps; visible filament structure along seams confirms.
- **Main risk**: Dense sweeps are compute-heavy; subsampling may miss thin failure filaments and understate structure.
- **Evidence labels**: community_default_belief: EVIDENCE (informal community experience); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION beyond the documented SAM architecture

### W13-P1-A-007 — Masks produced by SAM's automatic everything mode are frequently not reproducible by any single click, meaning automatic and interactive SAM are effectively two different segmenters sharing weights.

- **Problem**: Papers freely mix everything-mode masks and click-mode masks as if they were the same model output, but the grid-prompt plus NMS pipeline may generate masks outside the single-prompt reachable set, confounding comparisons and downstream pseudo-labeling.
- **Core hypothesis**: A non-trivial fraction of everything-mode masks cannot be recovered above a high-IoU threshold by any single point prompt in the image, because they arise from NMS interactions between multiple prompt seeds.
- **Falsifiable prediction**: Searching over dense single-click prompts recovers, at IoU above 0.9, only a strict subset of everything-mode masks, with the unreachable fraction concentrated on masks born from merged or suppressed candidates.
- **Why important**: If reachable sets differ, pseudo-labels from everything mode train students on masks that interactive use can never produce, and benchmark claims about SAM conflate two pipelines.
- **Why possibly novel**: HYPOTHESIS: the reachability relation between SAM's two operating modes appears never to have been measured.
- **Community default belief (what is treated as true)**: Everything mode is just many point prompts plus post-processing, so its masks are the same objects interactive SAM produces.
- **Why that might be wrong**: Post-processing (deduplication, thresholds, stability filtering) is a set-level operation that creates and destroys masks in ways no single prompt can express.
- **Minimal falsification experiment**: For 200 images, compute everything-mode masks, then for each mask search a dense click grid restricted to the mask interior for the best single-click reproduction; report the unreachable fraction; falsified if it is negligible.
- **Fastest falsification experiment**: Hours: 20 images, everything mode vs 100-click interior search per mask; count masks with best single-click IoU below 0.8.
- **Main risk**: Dense search is expensive and the unreachable fraction may be small on natural images while still mattering in specialized domains.
- **Evidence labels**: community_default_belief: KNOWN FACT (everything mode is documented as grid prompting plus filtering); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM automatic mask generation pipeline; the reachability gap is MODEL SPECULATION

### W13-P1-A-008 — When box and point prompts conflict, SAM resolves the conflict by a fixed learned hierarchy rather than evidence weighting, and PEFT silently reorders that hierarchy, changing pipeline behavior without any accuracy metric noticing.

- **Problem**: Multi-prompt pipelines assume prompt fusion is stable, but conflict-resolution order is an unmeasured behavioral contract that adaptation can rewrite, breaking downstream systems that relied on it.
- **Core hypothesis**: Frozen SAM has a consistent dominance ordering (e.g., box constrains, point selects within) under conflicting prompts, and LoRA adaptation on a domain where one prompt type dominated training data measurably shifts this ordering.
- **Falsifiable prediction**: A conflict battery (boxes around object A with points on object B at varying distances) yields a stable dominance curve for frozen SAM, and adapted checkpoints show statistically distinct curves whose direction depends on the prompt type used in adaptation.
- **Why important**: Behavioral contracts of foundation models under ill-posed inputs are what production systems actually depend on; showing PEFT changes them argues for contract-level regression testing of adapters.
- **Why possibly novel**: HYPOTHESIS: prompt-conflict behavior and its drift under adaptation appear unstudied; robustness work focuses on noisy prompts, not contradictory ones.
- **Community default belief (what is treated as true)**: More prompts give more information and the model fuses them sensibly; conflicts are user error not worth characterizing.
- **Why that might be wrong**: Training rarely contains genuinely contradictory prompts, so conflict behavior is an extrapolation artifact with no reason to be stable under weight updates.
- **Minimal falsification experiment**: Build a 500-case conflict battery from any instance dataset, define a dominance score, evaluate frozen vs box-adapted vs point-adapted LoRA checkpoints; falsified if dominance curves coincide.
- **Fastest falsification experiment**: Hours: 30 conflict cases through frozen SAM and any public domain-adapted SAM checkpoint, compare which prompt wins per case.
- **Main risk**: Conflict cases may produce degenerate low-confidence masks where dominance is undefined, requiring careful scoring.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION beyond documented SAM prompt encoding

### W13-P1-A-009 — The click-to-mask map of SAM has measurable sub-pixel aliasing: masks can flip discontinuously between adjacent click pixels due to positional-encoding interpolation, defining an effective Lipschitz constant of promptable segmentation.

- **Problem**: No one characterizes the continuity of the prompt-to-output map, yet UI zoom levels, coordinate rounding, and annotation tooling all assume clicks a pixel apart are equivalent.
- **Core hypothesis**: Fourier positional encoding of point prompts creates high-frequency components in the prompt embedding, so the mask output is locally non-smooth in click coordinates, with discontinuity density predictable from the encoding bandwidth.
- **Falsifiable prediction**: Measured over many objects, the distribution of mask-IoU change per one-pixel click displacement is heavy-tailed with a spike of near-total flips, and reducing positional-encoding frequency (where checkpoints allow) or averaging prompt embeddings over a sub-pixel neighborhood removes the spike.
- **Why important**: A Lipschitz characterization of prompt maps gives a principled robustness metric for promptable models and a nearly free inference-time fix (prompt-embedding smoothing) if the hypothesis holds.
- **Why possibly novel**: HYPOTHESIS: smoothness of outputs with respect to prompt coordinates, as opposed to image perturbations, seems not to have been formalized or measured for SAM-class models.
- **Community default belief (what is treated as true)**: The prompt encoder is smooth enough that neighboring clicks give the same mask; click robustness is only an issue at object boundaries.
- **Why that might be wrong**: High-frequency Fourier features are intentionally non-smooth to give positional discriminability, and nothing in training explicitly regularizes the map toward continuity away from boundaries.
- **Minimal falsification experiment**: For 100 objects, compute IoU between masks from all adjacent click pairs on a dense grid, quantify the flip-spike, then test prompt-embedding averaging as an intervention; falsified if flips are rare or unaffected by smoothing.
- **Fastest falsification experiment**: Hours: dense 1-pixel-step click sweeps across 10 object interiors, histogram of adjacent-click IoU; a spike near zero confirms aliasing-like flips exist.
- **Main risk**: Flips may be caused by genuine ambiguity boundaries rather than encoding aliasing, requiring the intervention arm to disambiguate.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM uses Fourier-style positional encodings for point prompts per the paper; the aliasing consequence is MODEL SPECULATION

### W13-P1-A-010 — Because SAM rescales every image to a fixed input resolution, the same physical click has resolution-dependent semantics: click informativeness and effective precision degrade lawfully with source image size, an unmodeled shift for high-resolution domains.

- **Problem**: Applications feed SAM images from 0.3 to 100 megapixels, but the prompt interface silently changes meaning across this range because a click subtends different fractions of the model's internal pixel grid.
- **Core hypothesis**: There exists a lawful relationship between source resolution and both minimum-selectable-object-size and click-precision requirements, fully explained by the fixed internal resolution, and tiling strategies change the prompt semantics rather than merely adding compute.
- **Falsifiable prediction**: Segmenting the same physical scene captured at multiple resolutions shows that the smallest reliably clickable object scales linearly with downsampling factor, and that failure onset is predicted by object size in internal pixels, not in source pixels or physical units.
- **Why important**: It converts scattered anecdotes about SAM failing on small structures in large images into a quantitative interface law that guides tiling, zooming, and adapter design for gigapixel domains.
- **Why possibly novel**: HYPOTHESIS: resolution effects are folded into domain gap in current discussions; isolating the prompt-semantics component with same-scene multi-resolution controls appears new.
- **Community default belief (what is treated as true)**: SAM is resolution-agnostic in practice; poor small-object performance is a generic limitation, not an interface artifact with a precise law.
- **Why that might be wrong**: A fixed internal grid mathematically bounds what a point can address; the community just has not separated this bound from feature-quality explanations.
- **Minimal falsification experiment**: Build a same-scene pyramid set (render or downsample high-res sources), measure click success vs object size in internal pixels across pyramid levels; falsified if failure onset does not collapse onto a single internal-pixel curve.
- **Fastest falsification experiment**: Hours: one high-res image set, 4 pyramid levels, click every annotated object, plot success vs internal-pixel size per level and check curve collapse.
- **Main risk**: Downsampling changes texture statistics too, so careful controls (blur-matched comparisons) are needed to isolate the geometric effect.
- **Evidence labels**: community_default_belief: EVIDENCE (community anecdotes about small objects); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM uses a fixed input resolution (1024 in the released implementation)

## Cluster: `what_peft_actually_learns` (12 ideas)

### W13-P1-A-011 — LoRA adaptation of SAM to shifted domains mostly learns low-order intensity and color recalibration, not new shape priors: matched-histogram preprocessing recovers most of the LoRA gain without any weight updates.

- **Problem**: Hundreds of papers report LoRA-on-SAM gains without asking what function the adapter implements; if it is mostly photometric normalization, far cheaper input-space fixes suffice and reported gains mislead about what adaptation contributes.
- **Core hypothesis**: For modality-style shifts (grayscale, stain variation, sensor gamma), the function computed by encoder LoRA is well-approximated by a per-channel monotone intensity transform of the input, so its benefit largely disappears once inputs are histogram-matched to the pretraining distribution.
- **Falsifiable prediction**: Across several shifted domains, histogram matching plus frozen SAM closes a large fraction of the frozen-to-LoRA gap, and the residual gap correlates with a shape-change measure of the domain rather than a photometric one.
- **Why important**: It would re-baseline an entire subfield: PEFT comparisons must include strong input-normalization baselines, and adapter capacity could be reserved for genuinely structural shift.
- **Why possibly novel**: HYPOTHESIS: input-normalization baselines are occasionally used but a functional-equivalence analysis between learned LoRA updates and photometric transforms has not been done to my knowledge.
- **Community default belief (what is treated as true)**: LoRA adapts internal representations to the new domain; the gain reflects learned domain-specific features.
- **Why that might be wrong**: The first-order discrepancy between web photos and many target domains is photometric, gradients fix first-order errors first, and low-rank updates are well-suited to global recalibration, so LoRA plausibly spends its capacity there.
- **Minimal falsification experiment**: On three shifted datasets, compare frozen SAM, frozen SAM plus histogram matching, and LoRA SAM; additionally fit the best monotone intensity transform to mimic LoRA outputs; falsified if normalization closes little of the gap.
- **Fastest falsification experiment**: One day: single domain, frozen vs histogram-matched-frozen vs published LoRA numbers on the same split; if normalization closes most of the gap, the hypothesis survives its first test.
- **Main risk**: Some domains conflate photometric and structural shift, and histogram matching itself can destroy diagnostic contrast, muddying attribution.
- **Evidence labels**: community_default_belief: EVIDENCE (dominant framing in PEFT-for-SAM literature); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: LoRA-based SAM adaptation exists (e.g., SAMed for medical images); functional-equivalence claim is MODEL SPECULATION

### W13-P1-A-012 — Rank-1 LoRA is sufficient for modality-level adaptation of SAM, and everything above rank 1 fits annotation style rather than domain content, measurable by cross-annotator generalization.

- **Problem**: Rank is chosen by grid search on in-distribution validation, which cannot distinguish learning-the-domain from learning-the-annotator; the field lacks a decomposition of what each rank increment buys.
- **Core hypothesis**: The domain-content component of adaptation lives in a one-dimensional weight-update subspace, while higher-rank components encode annotation-protocol idiosyncrasies, so higher rank helps same-annotator test sets but hurts or does not help different-annotator test sets of the same domain.
- **Falsifiable prediction**: On a dataset with multiple annotation sources for the same imagery, rank-1 and rank-16 LoRA tie on cross-annotator evaluation while rank-16 wins on same-annotator evaluation, and the rank-16 update projected onto its top singular direction recovers rank-1 behavior.
- **Why important**: It gives a principled rank-selection rule, explains why aggressive PEFT generalizes worse across hospitals or labs, and separates two kinds of learning the field currently conflates.
- **Why possibly novel**: HYPOTHESIS: LoRA rank ablations are ubiquitous, but decomposing rank benefits into content-vs-annotation-style using multi-annotator ground truth appears novel for segmentation.
- **Community default belief (what is treated as true)**: Higher LoRA rank means more capacity to learn the domain, with diminishing returns; rank tuning is a pure capacity question.
- **Why that might be wrong**: The single largest systematic difference in a new dataset is often the labeling protocol, not the imagery, and low-rank updates preferentially capture the largest systematic differences in order.
- **Minimal falsification experiment**: Use any dataset with two independent annotation passes (or re-annotate 100 images), train LoRA at ranks 1, 4, 16, evaluate same-source vs cross-source; falsified if higher rank helps both equally.
- **Fastest falsification experiment**: One day if multi-annotator data exists: train ranks 1 and 16, compare the two evaluation matrices.
- **Main risk**: Multi-annotator segmentation data is scarce and annotator disagreement may be too small in some domains to expose the effect.
- **Evidence labels**: community_default_belief: EVIDENCE (standard rank-ablation practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION for the decomposition; LoRA is VERIFIED PRIOR WORK

### W13-P1-A-013 — Where LoRA is placed in SAM changes what is learned, not just how much: attention-projection LoRA learns spatial grouping changes while MLP LoRA learns appearance re-mapping, yielding qualitatively different error profiles at equal parameter count.

- **Problem**: Placement choices (QV vs QKVO vs MLP) are treated as an efficiency knob tuned by validation mIoU, obscuring that different placements may fix different error types and thus should be chosen per failure mode.
- **Core hypothesis**: Attention-path adapters mainly change which pixels group together (affecting under- and over-merging errors) while MLP-path adapters mainly change appearance interpretation (affecting missed-object and texture-confusion errors), and this dissociation is visible in error-type-decomposed metrics.
- **Falsifiable prediction**: At matched parameter budgets on the same domain, QV-only and MLP-only LoRA reach similar mIoU but their error decompositions (merge errors vs recognition errors, boundary vs region) differ significantly and consistently across seeds and domains.
- **Why important**: It would turn PEFT placement from a hyperparameter into a diagnostic-driven design choice and reveal a functional decomposition of transformer blocks in dense prediction.
- **Why possibly novel**: HYPOTHESIS: placement ablations report scalar metrics; error-type dissociation by adapter placement in segmentation models appears unexamined.
- **Community default belief (what is treated as true)**: LoRA placement mainly trades off parameter count vs accuracy; QV placement is a good default everywhere.
- **Why that might be wrong**: Attention and MLP sublayers implement different function classes (data-dependent mixing vs pointwise transforms), so restricting updates to one path constrains which behaviors can change, an effect scalar metrics cannot see.
- **Minimal falsification experiment**: Train QV-only and MLP-only LoRA at matched parameters on two domains, decompose errors with boundary-vs-region and split-vs-merge metrics, test for consistent placement-by-error-type interaction; falsified if profiles are statistically indistinguishable.
- **Fastest falsification experiment**: One day: single domain, two placements, visualize and quantify error maps on 100 validation images.
- **Main risk**: Error decomposition metrics are noisy and the dissociation, even if real, may be too weak to guide practice.
- **Evidence labels**: community_default_belief: EVIDENCE (common default in LoRA papers); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION for the dissociation

### W13-P1-A-014 — Decoder-only PEFT can match encoder PEFT for many domain shifts because the gap manifests as prompt-token-to-feature misalignment rather than feature deficiency, contradicting the default that the encoder must adapt.

- **Problem**: The community defaults to adapting the big encoder (expensive, risks forgetting) on the assumption that domain shift corrupts features; if the lightweight decoder is the true bottleneck, most adaptation compute is wasted.
- **Core hypothesis**: Frozen SAM encoder features remain linearly sufficient to separate object from background in many shifted domains, and failures arise because the decoder's cross-attention queries no longer align with feature statistics; hence adapting only the two-layer decoder (a tiny parameter set) recovers most of the achievable gain.
- **Falsifiable prediction**: Across several shifted domains, decoder-only tuning reaches within a few points of encoder LoRA, and a linear probe on frozen encoder features predicts per-domain how much of the gap decoder tuning can close.
- **Why important**: Orders-of-magnitude cheaper adaptation, near-zero risk to the shared encoder in multi-task systems, and a clean empirical answer to where domain shift lives in promptable architectures.
- **Why possibly novel**: HYPOTHESIS: decoder-only fine-tuning appears in some pipelines as a baseline, but the linear-sufficiency analysis linking probe accuracy to the encoder-vs-decoder adaptation gap seems missing.
- **Community default belief (what is treated as true)**: Domain adaptation of SAM means adapting the image encoder; the decoder is a small head that transfers.
- **Why that might be wrong**: MAE-style pretraining plus SA-1B scale plausibly yields features far more shift-tolerant than assumed, while the decoder was trained on a narrow distribution of feature statistics and prompt geometries, making it the brittle component.
- **Minimal falsification experiment**: On four shifted datasets: linear-probe frozen features for foreground separability, then compare decoder-only tuning vs encoder LoRA vs both; falsified if decoder-only consistently loses by a wide margin even where probes are strong.
- **Fastest falsification experiment**: One day on one domain: linear probe plus decoder-only tuning vs published encoder-LoRA numbers on the same split.
- **Main risk**: Some domains (e.g., strong noise, novel physics of image formation) genuinely corrupt features, so the claim must be scoped by the probe, which reviewers may see as circular unless pre-registered.
- **Evidence labels**: community_default_belief: EVIDENCE (dominant practice in SAM adaptation literature); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM decoder is small (two-way transformer) per the paper; sufficiency claim is MODEL SPECULATION

### W13-P1-A-015 — Task-specific PEFT silently destroys SAM's ambiguity machinery: after adaptation, the three multimask outputs collapse toward one mask, removing a capability no downstream metric tracks.

- **Problem**: Adapted SAMs are evaluated on single-mask accuracy, so nobody notices if the hypothesis-space behavior (distinct part/whole proposals) quietly dies, even though pipelines and users still consume the multimask API.
- **Core hypothesis**: Fine-tuning on datasets with unique ground-truth masks provides gradient pressure that collapses the output-token diversity, so inter-mask IoU among the three outputs rises toward 1.0 as adaptation proceeds, at a rate set by dataset ambiguity level.
- **Falsifiable prediction**: Inter-output diversity on held-out natural images drops monotonically during PEFT on single-truth datasets, and models adapted on datasets with genuinely ambiguous labels retain diversity; the collapse precedes any measurable single-mask accuracy change on natural images.
- **Why important**: Ambiguity handling is a headline capability of promptable segmentation; documenting its fragility defines a regression test every adapter release should run and motivates diversity-preserving PEFT objectives.
- **Why possibly novel**: HYPOTHESIS: forgetting under fine-tuning is well known, but forgetting of output multiplicity (rather than accuracy on old data) appears unmeasured for segmentation foundation models.
- **Community default belief (what is treated as true)**: PEFT preserves pretrained capabilities by design; small low-rank updates cannot break a core behavior like multimask output.
- **Why that might be wrong**: The multimask mechanism depends on a delicate symmetry among output tokens that a rank-1 update to shared projections can break globally, since all tokens flow through the same adapted weights.
- **Minimal falsification experiment**: Track mean pairwise inter-mask IoU on a fixed natural-image probe set across PEFT checkpoints for three domains; falsified if diversity is stable or recovers, or if collapse merely mirrors accuracy loss.
- **Fastest falsification experiment**: Hours: load any public adapted-SAM checkpoint, compare inter-mask IoU distribution against frozen SAM on 100 COCO images.
- **Main risk**: Diversity might collapse only on in-domain images (arguably desired) and persist on natural images, making the finding a nuance rather than an alarm.
- **Evidence labels**: community_default_belief: EVIDENCE (widely repeated PEFT motivation); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM's three-mask ambiguity output is documented; the collapse dynamics are MODEL SPECULATION

### W13-P1-A-016 — Adapter-tuned SAM exhibits within-image interference: adaptation for target structures measurably degrades masks for untouched object categories present in the same images, a ripple effect invisible to target-only evaluation.

- **Problem**: PEFT evaluations measure the target task only, but real images contain many objects; if adapting for one structure corrupts segmentation of co-occurring others, multi-purpose deployments inherit hidden regressions.
- **Core hypothesis**: Because encoder adapters alter the shared feature field of the whole image, improving target-structure segmentation redistributes feature geometry and degrades non-target masks in the same scenes more than on unrelated scenes, i.e., interference is spatially and contextually coupled.
- **Falsifiable prediction**: For an adapted model, non-target-object IoU drop is larger on images containing the target structure than on statistically matched images without it, and the drop correlates with spatial proximity to target structures.
- **Why important**: It reframes PEFT safety: adapters are not additive capabilities but global reallocation of a shared representation, which matters for any platform serving one adapted SAM to many use cases.
- **Why possibly novel**: HYPOTHESIS: forgetting is usually measured across datasets; within-image, spatially-resolved interference appears unmeasured.
- **Community default belief (what is treated as true)**: PEFT changes are task-local; unrelated objects in the same image are unaffected because the adapter is small.
- **Why that might be wrong**: A ViT's attention globally mixes tokens, so a low-rank change that amplifies target-structure features necessarily perturbs the contextualization of every other token in the image.
- **Minimal falsification experiment**: Adapt SAM to one structure type in scenes that also contain COCO-annotated objects, evaluate non-target IoU on with-target vs without-target images and as a function of distance to target; falsified if drops are uniform or negligible.
- **Fastest falsification experiment**: One day: one adapted checkpoint, 200 images with both target and non-target annotations, paired comparison of non-target IoU vs frozen SAM.
- **Main risk**: Confounding between images containing the target and general scene statistics; matching must be done carefully.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-017 — The sample-efficiency crossover between head-only tuning and LoRA is predictable before training from a frozen-feature similarity score, giving a decision rule for which PEFT to use at a given dataset size.

- **Problem**: Practitioners choose PEFT methods by folklore or expensive sweeps; the field lacks a cheap pre-training diagnostic that predicts which method wins at the available data budget.
- **Core hypothesis**: For each domain there is a crossover sample size below which touching the encoder hurts (LoRA underperforms decoder or head-only tuning), and this crossover is a monotone function of a feature-space domain-similarity measure (such as CKA between frozen SAM features on source-like and target images) computable without labels.
- **Falsifiable prediction**: Across at least six domains and five dataset sizes, measured crossover points rank-correlate strongly with the pre-computed similarity score; falsified if crossovers exist but are unpredictable, or if LoRA dominates at all sizes everywhere.
- **Why important**: A validated adaptation-difficulty meter would save large amounts of compute community-wide and would ground PEFT choice in measurable representation geometry rather than habit.
- **Why possibly novel**: HYPOTHESIS: transferability metrics exist for classification (e.g., feature-based transferability estimation), but a crossover-prediction law for segmentation PEFT method selection appears untested.
- **Community default belief (what is treated as true)**: LoRA is the safe default at any data size; more data just helps it more.
- **Why that might be wrong**: With very few labeled masks, encoder updates chase annotation noise and destroy transferable features, a regime documented in other transfer settings but not mapped for promptable segmentation.
- **Minimal falsification experiment**: Grid of six domains times five sizes times two methods with three seeds, fit crossovers, correlate with the label-free similarity score; the grid is small models (SAM-B) to keep compute bounded.
- **Fastest falsification experiment**: Two domains times three sizes with SAM-B: if head-only never beats LoRA even at 10 images, the crossover premise is already in trouble.
- **Main risk**: Crossovers may be diffuse (methods tie over wide ranges), making the crossover point ill-defined and the law untestable as stated.
- **Evidence labels**: community_default_belief: EVIDENCE (common practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: CKA (Kornblith et al. 2019) exists as a similarity measure; the crossover law is MODEL SPECULATION

### W13-P1-A-018 — Bias-only tuning (BitFit-style) of SAM matches LoRA on texture- and intensity-shifted domains, implying that most claimed domain adaptation for segmentation is feature re-centering, not feature re-learning.

- **Problem**: If a few thousand bias parameters replicate LoRA's gains on common shifts, the field's mental model of what adaptation does is wrong, and comparisons omitting this baseline systematically overstate method sophistication.
- **Core hypothesis**: Distribution shift in many target domains moves feature means more than feature directions, so additive per-channel corrections (biases, LayerNorm parameters) capture most recoverable gain, with LoRA's advantage confined to shifts that rotate feature geometry.
- **Falsifiable prediction**: On a suite of shifted domains stratified by a mean-shift-vs-rotation diagnostic of frozen features, bias-only tuning ties LoRA on mean-shift-dominant domains and loses substantially only on rotation-dominant ones.
- **Why important**: It provides both a strong cheap baseline that all PEFT-for-SAM papers should include and a falsifiable geometric theory of what domain gap is for dense prediction.
- **Why possibly novel**: HYPOTHESIS: BitFit is known for NLP and classification; its systematic evaluation on promptable segmentation, stratified by a shift-geometry diagnostic, appears missing.
- **Community default belief (what is treated as true)**: Low-rank weight updates are needed to adapt representations; bias tuning is too weak for dense prediction under real shift.
- **Why that might be wrong**: Dense prediction relies heavily on feature statistics that normalization layers expose as directly steerable, so additive corrections have disproportionate leverage compared to classification intuitions.
- **Minimal falsification experiment**: Six domains, compute the mean-shift-vs-rotation diagnostic from frozen features, train bias-only vs LoRA at matched schedules, test the predicted interaction; falsified if bias-only loses everywhere regardless of shift geometry.
- **Fastest falsification experiment**: One day: one texture-shifted domain, bias-only vs LoRA at matched steps; a tie flips the default assumption immediately for that class of shift.
- **Main risk**: LayerNorm interactions may let bias tuning implement more than re-centering, blurring the interpretation even if the empirical tie holds.
- **Evidence labels**: community_default_belief: EVIDENCE (prevailing PEFT practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: BitFit (Ben Zaken et al. 2022) exists; extension claims are MODEL SPECULATION

### W13-P1-A-019 — PEFT overfits to the prompt type used during adaptation: LoRA trained with box prompts degrades point-prompt performance on the same domain (and vice versa), violating the assumed prompt-agnosticism of adaptation.

- **Problem**: Adaptation pipelines pick one prompt simulation (usually boxes for convenience) and implicitly promise a model adapted for all prompt modes; if adaptation is prompt-specific, deployed behavior diverges from reported behavior whenever users prompt differently.
- **Core hypothesis**: Gradients through the prompt-conditioned decoder shape encoder adapters toward features that serve the training prompt's information profile (boxes give scale, points do not), so cross-prompt transfer of adapters is systematically lossy and asymmetric (box-trained hurts points more than point-trained hurts boxes).
- **Falsifiable prediction**: A two-by-two train-prompt vs test-prompt matrix on the same domain shows significant off-diagonal drops, with the box-trained-point-tested cell worst; the asymmetry replicates across domains.
- **Why important**: It exposes an unstated degree of freedom that confounds every PEFT-for-SAM comparison and dictates that adapters be trained (or at least evaluated) under mixed-prompt curricula.
- **Why possibly novel**: HYPOTHESIS: papers report the prompt type they evaluate with, but a controlled train-prompt-by-test-prompt transfer matrix for PEFT appears unpublished.
- **Community default belief (what is treated as true)**: An adapter fixes the features for the domain; prompt handling is the frozen decoder's job and remains prompt-agnostic.
- **Why that might be wrong**: Feature adaptation is driven by decoder gradients that are strongly conditioned on prompt information content, so the learned features inherit prompt-specific shortcuts (e.g., relying on box-provided scale).
- **Minimal falsification experiment**: Same domain, same budget, train LoRA under box-only, point-only, and mixed prompts; evaluate all three under both prompt types; falsified if off-diagonal drops are negligible.
- **Fastest falsification experiment**: One day: train box-only LoRA on one domain, evaluate with points; compare against published point-prompt numbers for the same setup.
- **Main risk**: Effect sizes may be small on easy domains, requiring harder domains or fine-grained metrics to resolve.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit in current practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-020 — Under sequential PEFT, promptability forgets faster than features: SAM adapted to domain B after domain A retains transferable features (linear probes stay strong) while interactive behavior on domain A collapses, locating forgetting in the prompt pathway.

- **Problem**: Continual-learning studies of segmentation track mask accuracy only, so the field does not know which subsystem forgets: the representation, or the machinery that maps prompts onto it.
- **Core hypothesis**: Feature geometry is anchored by massive pretraining and moves slowly under sequential low-rank updates, whereas the prompt-conditioned readout is low-dimensional and brittle, so forgetting measured via prompts vastly overstates forgetting measured via probes.
- **Falsifiable prediction**: After A-then-B adaptation, domain-A linear-probe foreground separability drops only slightly while domain-A click-based IoU drops severely, and re-tuning only the decoder on a handful of domain-A examples restores most click performance.
- **Why important**: It changes continual-learning strategy for foundation segmenters: protect or modularize the small prompt pathway instead of replaying data through the giant encoder, potentially making forgetting cheap to fix.
- **Why possibly novel**: HYPOTHESIS: dissociating representational vs interface forgetting appears novel for promptable segmentation; analogous probe-based analyses exist in classification continual learning.
- **Community default belief (what is treated as true)**: Catastrophic forgetting means the representation is overwritten; recovery requires replay or regularization on the full model.
- **Why that might be wrong**: In prompt-conditioned architectures the interface is a distinct, small subsystem that can fail independently, an option classification-centric forgetting theory never had to consider.
- **Minimal falsification experiment**: Two-domain sequential LoRA with per-stage checkpoints; measure per-domain linear probes vs click IoU throughout; then decoder-only repair with 10 images; falsified if probes collapse in lockstep with click IoU.
- **Fastest falsification experiment**: One day with SAM-B: A-then-B LoRA, probe vs click metrics on A, plus the 10-image decoder repair test.
- **Main risk**: Linear probes may be too coarse a proxy for the features the decoder actually needs, understating representational forgetting.
- **Evidence labels**: community_default_belief: EVIDENCE (standard continual-learning framing); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION for the dissociation

### W13-P1-A-021 — Weight-space merging of independently trained domain LoRAs works unusually well for SAM (compared to classification adapters) because prompt conditioning absorbs cross-domain conflicts, making the merged model a testbed for when adapter arithmetic succeeds.

- **Problem**: Adapter merging is hit-or-miss with no accepted predictor of success; promptable segmentation offers a mechanism (per-instance prompt conditioning) that could explain and predict mergeability, but nobody has tested the mechanism.
- **Core hypothesis**: Conflicts between domain adapters mostly concern which structure to segment, a decision the prompt already resolves at inference; therefore merged LoRAs retain most per-domain performance in promptable mode while the same merge fails in prompt-free (semantic head) mode, isolating prompting as the conflict absorber.
- **Falsifiable prediction**: Across pairs of domain LoRAs, average merged-model retention in promptable evaluation exceeds retention in prompt-free evaluation by a large margin, and retention correlates with prompt informativeness (boxes retain more than single points).
- **Why important**: A mechanistic account of merging success would guide multi-domain deployment (one merged adapter vs adapter routing) and adds a controlled setting to the model-merging literature where the conflict-resolution variable is manipulable.
- **Why possibly novel**: HYPOTHESIS: model soups and task arithmetic are established for classification; using prompt conditioning as a controllable conflict-absorption mechanism appears unexplored.
- **Community default belief (what is treated as true)**: Adapter merging degrades with domain dissimilarity in a task-generic way; there is no architectural reason segmentation should merge better.
- **Why that might be wrong**: Prompt conditioning moves the task-selection burden from weights to inputs, exactly the burden that causes destructive interference in merged classifiers.
- **Minimal falsification experiment**: Train LoRAs on three dissimilar domains, merge pairwise by averaging, evaluate promptable vs prompt-free retention; falsified if promptable retention is not systematically higher.
- **Fastest falsification experiment**: One day: two existing public domain LoRAs (or quickly trained ones), merge, measure promptable retention vs each parent.
- **Main risk**: Prompt-free evaluation requires attaching a semantic head, introducing a confound that must be carefully matched.
- **Evidence labels**: community_default_belief: EVIDENCE (merging literature); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: model soups (Wortsman et al. 2022) and task arithmetic (Ilharco et al. 2022) exist; the prompt-absorption mechanism is MODEL SPECULATION

### W13-P1-A-022 — Visual prompt-token tuning (VPT-style) preserves SAM's everything-mode and zero-shot behavior far better than LoRA at equal target-domain accuracy, because appended tokens cannot rewrite spatial feature geometry.

- **Problem**: PEFT methods are ranked by target accuracy alone; the collateral damage each method class inflicts on retained capabilities is unmeasured, though it determines which method is safe for shared deployments.
- **Core hypothesis**: There is a method-class law: input-space and token-space adaptation (learned prompts, prefix tokens) trade a small target-accuracy ceiling for large capability retention, while weight-space adaptation (LoRA, adapters) does the reverse, and the trade-off is governed by whether the method can alter token-mixing pathways.
- **Falsifiable prediction**: At matched target mIoU, VPT-adapted SAM shows significantly smaller degradation than LoRA on a fixed retained-capability battery (everything-mode mask count and quality on natural images, multimask diversity, click-jitter stability), consistently across domains.
- **Why important**: It gives platform operators a principled safety ordering of PEFT classes and connects adaptation mechanics (what can be rewritten) to capability retention (what is lost).
- **Why possibly novel**: HYPOTHESIS: VPT and LoRA are both known, but a retention-vs-target trade-off law tied to the mechanism class, evaluated on promptable segmentation capabilities, appears new.
- **Community default belief (what is treated as true)**: PEFT methods are roughly interchangeable at matched accuracy; choose by convenience and parameter count.
- **Why that might be wrong**: Mechanistically, appended tokens act through attention as soft context and cannot restructure pairwise mixing among image tokens, so the reachable function class (and hence the damage surface) is genuinely smaller.
- **Minimal falsification experiment**: Adapt SAM to two domains with VPT and LoRA at several budgets, plot target accuracy vs retention-battery score, test whether method classes occupy distinct Pareto regions; falsified if curves overlap.
- **Fastest falsification experiment**: One day: one domain, VPT vs LoRA to matched target IoU, run the retention battery on 100 natural images.
- **Main risk**: VPT may fail to reach usable target accuracy on hard shifts, collapsing the comparison region.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: VPT (Jia et al. 2022) exists; the retention law is MODEL SPECULATION

## Cluster: `iou_head_calibration_uncertainty` (8 ideas)

### W13-P1-A-023 — SAM's predicted-IoU head is a mask-style critic, not an accuracy estimator: under domain shift its score tracks smoothness and compactness of the mask more than true IoU, which breaks every pipeline that uses the score for filtering.

- **Problem**: Everything-mode filtering, pseudo-label selection, and auto-annotation all rank masks by the predicted IoU score, assuming it estimates correctness; if it estimates conformity to SA-1B mask style instead, these pipelines systematically select fluent-but-wrong masks out of distribution.
- **Core hypothesis**: The IoU head learned features of masks that correlated with quality in-distribution (compactness, boundary smoothness, closed topology) and regresses onto those features; under shift the correlation with true IoU collapses while correlation with style features persists.
- **Falsifiable prediction**: On shifted domains, partial correlation of predicted score with true IoU (controlling for compactness and boundary smoothness) approaches zero, while partial correlation with style features (controlling for true IoU) remains high; in-distribution both are positive.
- **Why important**: A quantitative indictment of score-based filtering would force redesign of auto-labeling pipelines and reframe predicted-quality heads as in-distribution style priors, a general lesson for foundation models with self-assessment heads.
- **Why possibly novel**: HYPOTHESIS: poor calibration of SAM scores under shift is anecdotally noted, but the decomposition into style-vs-accuracy components via partial correlation appears undone.
- **Community default belief (what is treated as true)**: The predicted IoU score is a reliable, if slightly optimistic, proxy for mask quality; thresholding on it removes bad masks.
- **Why that might be wrong**: The head only ever saw in-distribution masks with in-distribution error structure, and regressing quality from mask shape features is the shortcut solution gradient descent will find.
- **Minimal falsification experiment**: Collect masks with predicted scores on one natural and two shifted datasets, compute true IoU and style features, run partial-correlation analysis; falsified if score remains an accuracy estimator after controlling for style.
- **Fastest falsification experiment**: Hours: one shifted dataset, scatter predicted score vs true IoU colored by compactness; a compactness-stratified score with flat IoU dependence is visible by eye.
- **Main risk**: Style and accuracy are correlated in ground truth too, so the decomposition requires careful statistical treatment and enough dispersion in both variables.
- **Evidence labels**: community_default_belief: EVIDENCE (widespread pipeline practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM predicts an IoU score per mask; the style-critic decomposition is MODEL SPECULATION

### W13-P1-A-024 — During PEFT, calibration of the IoU head collapses before mask quality does, so score-vs-truth divergence on a small probe set is an early-warning signal for harmful over-adaptation.

- **Problem**: There is no cheap online signal telling practitioners when continued fine-tuning starts damaging a promptable model; loss curves keep improving while generalization silently degrades.
- **Core hypothesis**: The IoU head sits downstream of adapted features but is rarely included in PEFT parameter sets, so feature drift first appears as miscalibration of the frozen head, measurable epochs before held-out mask accuracy declines.
- **Falsifiable prediction**: Across domains and PEFT methods, expected calibration error of the score on held-out data begins rising at least a few epochs before held-out mIoU begins falling, with consistent lead time across seeds.
- **Why important**: An intrinsic early-warning metric (no extra labels beyond a small probe set) would make PEFT safer and supports a general principle: frozen self-assessment heads are drift detectors for adapted backbones.
- **Why possibly novel**: HYPOTHESIS: using a frozen auxiliary head's miscalibration as a canary for backbone adaptation damage appears unexplored in segmentation.
- **Community default belief (what is treated as true)**: Overfitting is monitored via validation loss or accuracy; calibration is an afterthought evaluated once at the end.
- **Why that might be wrong**: Calibration depends on the joint distribution of features and errors, which shifts as soon as features move, while accuracy has slack from margin; so miscalibration is mathematically positioned to move first.
- **Minimal falsification experiment**: Instrument LoRA training on three domains with per-epoch ECE and mIoU on held-out data; test for consistent temporal precedence of calibration collapse; falsified if orderings are random or reversed.
- **Fastest falsification experiment**: Rerun one existing PEFT training with checkpoints, plot ECE and mIoU per epoch, check peak ordering; hours if checkpoints exist.
- **Main risk**: If practitioners fine-tune the IoU head jointly (some do), the canary is silenced; the finding then only applies to head-frozen recipes.
- **Evidence labels**: community_default_belief: EVIDENCE (standard practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-025 — SAM's own score distribution is a free domain-shift detector: the shape of predicted-IoU histograms over grid prompts detects out-of-distribution imagery as well as dedicated feature-space OOD methods, at zero additional model cost.

- **Problem**: Deployments need to know when incoming imagery has drifted beyond the model's competence, but bolt-on OOD detectors add compute and their scores are unrelated to segmentation competence specifically.
- **Core hypothesis**: Competence-relevant shift compresses and shifts the grid-prompt score distribution in characteristic ways (mass moving off the high-score mode), so simple statistics of that distribution predict per-image segmentation quality drop better than generic feature-distance OOD scores.
- **Falsifiable prediction**: Across a spectrum of shifts, image-level correlation between score-distribution statistics and true achievable IoU exceeds that of a standard feature-based OOD baseline using the same backbone.
- **Why important**: A built-in, task-aligned competence meter changes how promptable models are deployed (triage, human fallback) and demonstrates that self-assessment heads carry usable epistemic signal even when miscalibrated pointwise.
- **Why possibly novel**: HYPOTHESIS: using the distribution of a segmentation model's own quality scores over systematic prompts as an OOD/competence signal appears unexamined.
- **Community default belief (what is treated as true)**: OOD detection requires dedicated machinery; task heads are unreliable under the very shift you want to detect.
- **Why that might be wrong**: Even a biased critic changes its output distribution under input shift; distribution shape (not pointwise value) may carry robust signal the pointwise-calibration critique misses.
- **Minimal falsification experiment**: On mixed-domain image pools, compute grid-prompt score histograms, fit a competence predictor from summary statistics, compare against a Mahalanobis-style feature baseline for predicting per-image quality; falsified if the baseline dominates.
- **Fastest falsification experiment**: Hours: 200 images spanning three domains, grid prompts, correlate mean top-score against oracle achievable IoU per image.
- **Main risk**: Idea 023 (style-critic behavior) implies scores can stay high on wrong masks, which would cap this detector exactly where it is most needed; the two hypotheses constrain each other and should be tested jointly.
- **Evidence labels**: community_default_belief: EVIDENCE (OOD literature norms); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-026 — SAM's ambiguity bottleneck is ranking, not generation: the correct mask is frequently among the three outputs but not top-ranked, so fixing selection (a tiny head) would harvest most of the oracle-vs-deployed gap.

- **Problem**: The gap between oracle (best-of-3) and deployed (top-ranked) performance is routinely reported but never decomposed; if it is a pure ranking failure, the field is fine-tuning giant encoders to fix a three-way classification problem.
- **Core hypothesis**: Under domain shift, mask-generation capability degrades slower than ranking capability, so the fraction of cases where the oracle mask exists but is misranked grows with shift, and retraining only the selection mechanism on few labels recovers most of the oracle gap.
- **Falsifiable prediction**: On shifted domains, the misranked-but-present fraction is a large share of the oracle gap, and a lightweight recalibrated ranker (trained on under 100 masks) closes most of that share, while in-distribution the fraction is small.
- **Why important**: It redirects adaptation effort toward the cheapest effective intervention and provides a clean decomposition (generate vs select) applicable to any multi-hypothesis foundation model.
- **Why possibly novel**: HYPOTHESIS: oracle-vs-top1 gaps are reported, but the decomposition into generation failure vs selection failure across shift levels, plus the minimal-repair experiment, appears missing.
- **Community default belief (what is treated as true)**: The oracle gap reflects intrinsic ambiguity, and closing it requires better mask generation via full adaptation.
- **Why that might be wrong**: Generation is backed by the whole pretrained encoder-decoder while selection is one small regressor trained on in-distribution statistics, so selection is the fragile link under shift.
- **Minimal falsification experiment**: On three domains, log all three masks with scores, compute present-but-misranked rates, train a tiny ranker per domain on 100 labeled prompts, measure recovered gap; falsified if the oracle gap is mostly generation failure.
- **Fastest falsification experiment**: Hours: one shifted dataset, 300 prompts, compute how often best-of-3 beats top-1 by a margin; a large fraction immediately supports the ranking-bottleneck view.
- **Main risk**: With only three hypotheses the ceiling is low in truly hard domains; the decomposition may show generation failure dominates exactly where help is needed.
- **Evidence labels**: community_default_belief: EVIDENCE (common interpretation of oracle numbers); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM outputs three masks with scores; the decomposition is MODEL SPECULATION

### W13-P1-A-027 — Disagreement between SAM's stability score and its predicted IoU score is a label-error detector: pixels-cheap, model-free-of-extra-training, and usable to audit ground truth in segmentation datasets.

- **Problem**: Segmentation benchmarks contain annotation errors that silently distort model rankings, and current label-error detection needs ensembles or training dynamics; a frozen foundation model may already expose a usable error signal.
- **Core hypothesis**: When SAM is prompted with ground-truth-derived prompts, cases where stability score is high but agreement with ground truth is low are enriched for annotation errors rather than model errors, because the two scores capture independent evidence about boundary support.
- **Falsifiable prediction**: Ranking dataset samples by the stability-high-agreement-low criterion and manually auditing the top slice reveals an annotation-error rate several times the base rate, on at least two public datasets.
- **Why important**: A free data-auditing tool from a frozen model has immediate practical value, and it supports a broader claim: foundation-model self-consistency signals can arbitrate between model error and label error.
- **Why possibly novel**: HYPOTHESIS: confident-learning approaches exist for classification labels; using promptable-segmenter internal score disagreement for mask-quality auditing appears new.
- **Community default belief (what is treated as true)**: Ground truth is treated as correct; disagreement between model and label is model error by definition when computing metrics.
- **Why that might be wrong**: A model trained on a billion masks encodes a strong prior over plausible object boundaries; where its self-consistency is high, systematic disagreement with a single annotator plausibly indicates annotator fault.
- **Minimal falsification experiment**: On two datasets, compute the criterion for all instances, audit 100 top-ranked and 100 random instances blind, compare error rates; falsified if enrichment is absent.
- **Fastest falsification experiment**: Hours: one dataset, rank by criterion, eyeball the top 30 cases; obvious annotation errors in the majority would be a strong first signal.
- **Main risk**: The criterion may mostly flag genuinely ambiguous objects, requiring an ambiguity-controlled audit protocol.
- **Evidence labels**: community_default_belief: KNOWN FACT (benchmarking convention); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM computes stability scores in its automatic pipeline; the auditing application is MODEL SPECULATION

### W13-P1-A-028 — SAM's three multimask outputs are not diverse hypotheses but a hard-coded scale quantization (part, object, group), which predicts a specific failure family on structures without hierarchical scale organization.

- **Problem**: The multimask mechanism is marketed as ambiguity handling, but if it only expresses one axis of ambiguity (containment hierarchy), then non-hierarchical ambiguity (interleaved objects, alternative groupings at the same scale) is structurally unrepresentable and silently mishandled.
- **Core hypothesis**: The three output tokens specialize to nested scale levels during training, so for prompts whose plausible masks are non-nested alternatives at similar scale, SAM returns three near-nested masks and misses at least one valid alternative entirely.
- **Falsifiable prediction**: On a constructed benchmark of same-scale ambiguity (interleaved stripes, overlapping translucent objects, tangled cables), the three outputs are mutually nested in most cases while human-annotated alternatives are non-nested, and containment order of outputs is stable across images.
- **Why important**: It precisely characterizes what kind of ambiguity promptable segmentation can express, informing both benchmark design and architectural fixes (tokens conditioned on alternative axes).
- **Why possibly novel**: HYPOTHESIS: the whole-part-subpart training supervision is documented for SAM, but the consequence that same-scale ambiguity is unrepresentable, and a benchmark isolating it, appear unexplored.
- **Community default belief (what is treated as true)**: Three masks with IoU ranking adequately capture prompt ambiguity for practical purposes.
- **Why that might be wrong**: The training signal explicitly organized outputs by containment hierarchy, so the learned hypothesis space is a chain, and chains cannot represent antichains of alternatives.
- **Minimal falsification experiment**: Build 200 same-scale-ambiguity cases with multiple valid annotations, prompt SAM, measure nestedness of outputs vs coverage of valid alternatives; falsified if outputs frequently cover non-nested alternatives.
- **Fastest falsification experiment**: Hours: 20 tangled-object photos, click intersections, check whether any output pair is non-nested.
- **Main risk**: Constructing convincing same-scale ambiguity cases without artificial-looking stimuli takes care; natural examples may be rare enough to question importance.
- **Evidence labels**: community_default_belief: EVIDENCE (paper framing and common usage); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM trains multimask outputs on whole/part/subpart supervision per the paper; the antichain limitation is MODEL SPECULATION

### W13-P1-A-029 — Recalibrating only SAM's IoU head on a shifted domain (freezing all mask-producing weights) recovers a large fraction of practical pipeline performance, because deployed loss is dominated by wrong mask selection and wrong filtering thresholds.

- **Problem**: Teams jump to LoRA or full fine-tuning when auto-annotation quality drops on a new domain, paying compute and forgetting costs, without checking whether the mask generator is fine and only the scorer is broken.
- **Core hypothesis**: In score-mediated pipelines (filtering, NMS, selection), a shift-induced miscalibrated scorer causes most of the end-to-end quality drop, so head-only recalibration on a small labeled set approaches LoRA-level pipeline metrics at a fraction of the cost and zero backbone risk.
- **Falsifiable prediction**: On auto-annotation pipelines over shifted domains, head-recalibrated SAM closes a majority of the frozen-to-LoRA gap in pipeline-level metrics (mask AP of filtered outputs), while closing little of the gap in single-prompt oracle IoU.
- **Why important**: It offers a deployment-relevant cheap fix and cleanly separates two failure sources that current evaluations blend, sharpening how the community attributes domain-shift damage.
- **Why possibly novel**: HYPOTHESIS: score recalibration is standard in classification; treating the IoU head as the primary shift casualty in segmentation pipelines and quantifying the recoverable fraction appears new.
- **Community default belief (what is treated as true)**: Domain shift degrades masks; adaptation must touch the mask-producing pathway to help.
- **Why that might be wrong**: Oracle-vs-deployed gaps (idea 026) suggest mask generation survives shift better than assessment does, and pipelines amplify assessment errors through thresholds.
- **Minimal falsification experiment**: Three shifted domains, three arms (frozen, head-recalibrated on 200 masks, LoRA), evaluate pipeline metrics and oracle metrics separately; falsified if head recalibration recovers little pipeline performance.
- **Fastest falsification experiment**: One day: single domain, recalibrate head with isotonic regression on 100 labeled masks, rerun the pipeline, compare AP.
- **Main risk**: The result depends on pipeline design; conclusions may not transfer across filtering strategies, requiring a small pipeline-design grid.
- **Evidence labels**: community_default_belief: EVIDENCE (common adaptation practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-030 — Variance across SAM's internal token-to-image attention maps localizes boundary errors: an unused, training-free per-pixel uncertainty map already exists inside the decoder.

- **Problem**: Users get a binary mask and one scalar score; pixel-level confidence would enable targeted review and active correction, but adding uncertainty heads requires retraining nobody wants to do.
- **Core hypothesis**: Disagreement among cross-attention patterns of the output token across decoder layers and heads concentrates precisely where the produced boundary is wrong, because attention disagreement reflects unresolved evidence integration.
- **Falsifiable prediction**: A per-pixel disagreement map computed from existing decoder attention (no retraining) achieves meaningful precision-recall for locating boundary segments with high error, beating a distance-to-boundary baseline and mask-logit entropy on the same cases.
- **Why important**: Free, architecture-native uncertainty would upgrade every SAM deployment (review triage, active learning, correction guidance) and demonstrates that promptable decoders contain latent epistemic signals.
- **Why possibly novel**: HYPOTHESIS: attention-based interpretability is common, but validating decoder-attention disagreement as a quantitative boundary-error localizer for SAM appears untested.
- **Community default belief (what is treated as true)**: Getting pixel-level uncertainty from SAM requires ensembles, test-time augmentation, or a retrained uncertainty head; internal attention is for visualization only.
- **Why that might be wrong**: The decoder integrates evidence through few attention operations, so unresolved conflicts have nowhere to hide except as inter-head and inter-layer disagreement, which is directly readable.
- **Minimal falsification experiment**: Extract attention maps for 500 prompts across two datasets, compute disagreement maps, evaluate error-localization AUROC against logit-entropy and distance baselines; falsified if disagreement adds nothing over baselines.
- **Fastest falsification experiment**: Hours: 30 prompts with known error maps, overlay disagreement maps, compute AUROC; visible alignment or misalignment is quickly diagnostic.
- **Main risk**: Attention maps are low-resolution (64x64 internal grid), possibly too coarse to localize thin boundary errors that matter most.
- **Evidence labels**: community_default_belief: EVIDENCE (uncertainty-estimation norms); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM decoder uses cross-attention between tokens and image embedding; the uncertainty claim is MODEL SPECULATION

## Cluster: `encoder_representation_myths` (10 ideas)

### W13-P1-A-031 — SAM encoder features are excellent boundary features but poor semantic features, and the two qualities anti-correlate across layers, refuting the assumption that a segmentation foundation model is a general visual foundation model.

- **Problem**: SAM features are increasingly reused as generic visual representations (matching, correspondence, retrieval) on the assumption that segmentation pretraining yields broadly good features; if the representation traded semantics for boundary acuity, this reuse is misguided in predictable ways.
- **Core hypothesis**: Class-agnostic mask supervision optimized the encoder for where-things-end rather than what-things-are, so linear probes show SAM below weaker self-supervised baselines on semantic tasks while dominating on boundary and grouping tasks, with the gap widening in later layers.
- **Falsifiable prediction**: A layer-by-layer probe battery (classification, semantic correspondence vs boundary detection, grouping) shows SAM's semantic probe curve falling below a DINO-class baseline in late layers while its boundary probes rise, producing a characteristic scissors pattern absent in classification-pretrained ViTs.
- **Why important**: It would correct a growing misuse of SAM features and articulate a concrete representational trade-off (semantics vs boundary acuity) with implications for what one pretraining task can provide.
- **Why possibly novel**: HYPOTHESIS: individual comparisons of SAM features exist in various papers, but a layer-resolved scissors-pattern analysis framing an explicit trade-off appears unarticulated.
- **Community default belief (what is treated as true)**: SAM is a vision foundation model; its features are strong general-purpose representations because of massive pretraining data.
- **Why that might be wrong**: The training objective never rewarded identity information beyond what grouping requires, and information not rewarded at scale tends to be compressed away in late layers.
- **Minimal falsification experiment**: Run frozen-feature probes per layer for SAM, MAE, and DINO-class models on matched data across semantic and boundary tasks; falsified if SAM tracks the baselines on semantic probes or shows no late-layer divergence.
- **Fastest falsification experiment**: One day: linear probes on one classification and one boundary-detection dataset for SAM vs one baseline, final layer only; a large split already indicates the trade-off.
- **Main risk**: Probe design choices can flip conclusions; the battery must be broad and hyperparameter-fair to be credible.
- **Evidence labels**: community_default_belief: EVIDENCE (common reuse practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM encoder initialized from MAE pretraining per the paper; DINO exists; the scissors pattern is MODEL SPECULATION

### W13-P1-A-032 — SAM inherits a persistent MAE fingerprint: its failure modes align with reconstruction-pretraining biases (low-level statistics, local completion) more than with its segmentation training, measurable by comparing against a counterfactual contrastive-initialized SAM.

- **Problem**: Everyone treats SAM's behavior as the product of SA-1B-scale mask supervision, ignoring that the encoder began as an MAE and that initialization biases can survive fine-tuning; attribution of SAM's failure modes to the wrong cause misleads attempts to fix them.
- **Core hypothesis**: A substantial share of SAM's characteristic errors (texture leakage, completion of occluded regions, insensitivity to global semantics) is inherited from generative-reconstruction pretraining and would differ qualitatively had the encoder been initialized contrastively, even with identical segmentation training.
- **Falsifiable prediction**: Training two smaller SAM-style models identically except for encoder initialization (MAE vs contrastive) yields significantly different error-type distributions on a diagnostic battery, with the MAE-initialized model showing more texture-completion errors, despite similar mean IoU.
- **Why important**: It tests whether foundation-model behavior is set by the largest training stage or path-dependent on initialization, a question with broad implications for how the field attributes and repairs model behavior.
- **Why possibly novel**: HYPOTHESIS: initialization-dependence of fine-tuned model behavior is studied for small models; a controlled study at promptable-segmentation scale with error-type phenotyping appears missing.
- **Community default belief (what is treated as true)**: SA-1B-scale supervision dominates; initialization is a convergence-speed detail that washes out.
- **Why that might be wrong**: Fine-tuning is known to move weights little in relative terms, and behavior in underdetermined regions of input space is set by priors, exactly where failure modes live.
- **Minimal falsification experiment**: Train two ViT-S promptable segmenters on an open mask corpus from MAE vs contrastive initializations, phenotype errors on a diagnostic set; falsified if error distributions converge.
- **Fastest falsification experiment**: Days (training-bound), but a cheap precursor exists: compare MAE and SAM error phenotypes directly; strong phenotype overlap between MAE-probing errors and SAM errors is suggestive first evidence obtainable in hours.
- **Main risk**: Compute: even at ViT-S scale this needs a real training budget, and small-scale conclusions may not transfer to ViT-H.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit attribution); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM's encoder was MAE-pretrained per the paper; MAE (He et al. 2022) is VERIFIED PRIOR WORK

### W13-P1-A-033 — The layer-wise need for adaptation in SAM is U-shaped: earliest and final encoder layers require updates while the middle two-thirds are domain-universal, contradicting both adapt-everything and adapt-last-layers defaults.

- **Problem**: PEFT parameter budgets are spread uniformly or concentrated late by convention, without a map of where domain-specific computation actually lives in a segmentation ViT.
- **Core hypothesis**: Early layers encode sensor and texture statistics (shift-sensitive), late layers interface with the decoder's expectations (shift-sensitive), and middle layers compute generic grouping (shift-tolerant), so per-layer adaptation gain follows a U-shape across depths and across domains.
- **Falsifiable prediction**: Single-layer LoRA insertions evaluated per depth on several domains trace a U-shaped gain curve, and a budgeted allocation matching the U-shape beats uniform and last-k allocations at equal parameters.
- **Why important**: A validated adaptation map cuts PEFT cost, and the U-shape (if real) is evidence for a three-phase functional organization of dense-prediction transformers.
- **Why possibly novel**: HYPOTHESIS: layer-wise probing exists for classification ViTs; a per-layer adaptation-gain map for promptable segmentation with an allocation test appears new.
- **Community default belief (what is treated as true)**: Later layers are more task-specific, so adapting them (or everything) is the sensible default.
- **Why that might be wrong**: That heuristic comes from classification, where semantics concentrate late; dense grouping may instead be generic in the middle with domain-coupling at both interfaces.
- **Minimal falsification experiment**: For SAM-B on three domains, train 12 single-layer LoRA variants plus allocation arms; falsified if gain is flat or monotone in depth.
- **Fastest falsification experiment**: One day: three single-layer LoRAs (early, middle, late) on one domain; a middle-layer minimum is immediate support.
- **Main risk**: Single-layer gains may not compose additively, weakening the allocation corollary even if the U-shape holds.
- **Evidence labels**: community_default_belief: EVIDENCE (transfer-learning folklore); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-034 — SAM's windowed-attention design leaves a grid fingerprint: under domain shift, segmentation errors cluster along the window boundaries of the ViT, an architecture-induced spatial artifact nobody audits for.

- **Problem**: Error analyses treat mistake locations as image-driven; if a fixed architectural grid systematically seeds errors, then error maps are partially artifacts of engineering choices, and tiling or padding decisions interact with it invisibly.
- **Core hypothesis**: Because most encoder layers use windowed attention with only sparse global layers, cross-window integration is weaker, and under shift (where features are noisier) mask boundary errors and mask fragmentation align with the internal window lattice at rates far above chance.
- **Falsifiable prediction**: Averaging error maps over many shifted-domain images in encoder-grid coordinates reveals periodic structure at the window frequency, absent in-distribution or in a full-attention variant at matched accuracy.
- **Why important**: It exposes a class of architecture-induced, spatially-structured failure invisible to scalar metrics, with direct implications for how images should be tiled and padded and for the design of efficient attention in dense models.
- **Why possibly novel**: HYPOTHESIS: window artifacts are known in image restoration models; a quantitative audit for promptable segmentation under shift appears absent.
- **Community default belief (what is treated as true)**: Windowed attention with a few global layers is functionally equivalent to full attention for segmentation quality.
- **Why that might be wrong**: Equivalence was validated in-distribution where redundancy masks integration weaknesses; shift removes the redundancy and exposes the lattice.
- **Minimal falsification experiment**: Accumulate per-pixel error frequencies in grid coordinates over 1000 shifted images, test for periodicity via Fourier analysis of the aggregate map; falsified if no window-frequency peak exists.
- **Fastest falsification experiment**: Hours: 200 shifted images with random offsets, aggregate error map, look for lattice peaks in its spectrum.
- **Main risk**: Object-position biases in datasets could masquerade as periodicity; randomized image offsets are needed as controls.
- **Evidence labels**: community_default_belief: EVIDENCE (design choice validated in the SAM paper in-distribution); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM's ViT uses windowed attention with periodic global blocks per the paper

### W13-P1-A-035 — Despite being trained to find boundaries, SAM remains texture-biased in the cue-conflict sense: when shape and texture disagree, its groupings follow texture, showing that segmentation training does not confer shape bias.

- **Problem**: The community tacitly assumes a model that segments everything must understand shape; if SAM's grouping is texture-driven, its failures on camouflage, stains, and shadows are principled and predictable rather than random edge cases.
- **Core hypothesis**: Class-agnostic mask training rewards locally-consistent-region detection, which texture statistics support more cheaply than global shape, so SAM's decisions in cue-conflict stimuli (shape of A, texture of B) side with texture at rates comparable to ImageNet-trained ViTs.
- **Falsifiable prediction**: On segmentation-adapted cue-conflict stimuli (objects with transplanted textures, texture boundaries crossing shape boundaries), SAM's masks follow texture boundaries against shape boundaries in the majority of conflicts, and PEFT on shape-critical domains reduces this only marginally.
- **Why important**: Shape-vs-texture bias shaped the robustness literature for classification; establishing the segmentation analogue defines which robustness interventions transfer and explains a family of SAM failures with one mechanism.
- **Why possibly novel**: HYPOTHESIS: cue-conflict methodology exists for classifiers (Geirhos et al.); a rigorous segmentation-native adaptation measuring grouping decisions under conflict appears missing.
- **Community default belief (what is treated as true)**: Training on a billion masks teaches shape; SAM's boundary acuity implies shape understanding.
- **Why that might be wrong**: Boundary acuity requires only local contrast sensitivity; nothing in the objective requires global shape representation, and shortcut theory predicts the cheaper cue wins.
- **Minimal falsification experiment**: Build 300 cue-conflict segmentation stimuli with unambiguous shape-defined ground truth, prompt SAM, score texture-following rate against human annotators as reference; falsified if SAM is shape-dominant.
- **Fastest falsification experiment**: Hours: 30 texture-transplant stimuli, click centers, tally whether masks stop at texture or shape boundaries.
- **Main risk**: Synthetic stimuli may be out-of-distribution enough that behavior reflects distribution shift, not cue preference; naturalistic conflict cases (camouflage datasets) should corroborate.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: cue-conflict texture-bias methodology (Geirhos et al. 2019) exists for classification

### W13-P1-A-036 — Token-norm inflation under domain shift maps where adaptation is needed: per-layer feature-norm statistics on unlabeled target images predict the optimal LoRA placement, enabling data-driven adapter allocation without any labels.

- **Problem**: Adapter placement is chosen blind; a label-free diagnostic that localizes shift within the network would let practitioners spend parameters exactly where the model is struggling.
- **Core hypothesis**: Layers whose token-norm and activation-statistics deviate most from natural-image reference statistics under target-domain inputs are the layers where LoRA insertion yields the largest gain, because statistical deviation marks broken computations.
- **Falsifiable prediction**: Across domains, rank correlation between per-layer statistical-deviation scores (computed on unlabeled target images) and measured per-layer single-LoRA gains is strong; allocation guided by deviation beats uniform allocation at matched budgets.
- **Why important**: It would turn PEFT configuration from folklore into measurement, and validate a general principle that internal-statistics drift localizes damage in foundation models.
- **Why possibly novel**: HYPOTHESIS: activation-statistics monitoring exists for OOD detection; using it prescriptively to allocate adaptation capacity in segmentation models appears untested.
- **Community default belief (what is treated as true)**: Where to place adapters is a hyperparameter to sweep, not something the network's own statistics can tell you.
- **Why that might be wrong**: Statistical drift is the visible symptom of computation operating off-manifold, and repairing off-manifold computation is what adaptation does, so symptom location and repair location plausibly coincide.
- **Minimal falsification experiment**: For three domains, compute per-layer deviation profiles, then train single-layer LoRAs per depth to get ground-truth gain profiles, correlate; falsified if correlation is weak or inconsistent.
- **Fastest falsification experiment**: One day: one domain, deviation profile vs three single-layer LoRA gains (early, middle, late); rank agreement is a quick signal.
- **Main risk**: Deviation might mark layers reacting to shift rather than layers whose repair helps, breaking the prescriptive link even if the descriptive one holds.
- **Evidence labels**: community_default_belief: EVIDENCE (current practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-037 — Aspect-ratio distortion from SAM's square-padded resizing is a first-order hidden failure source for thin elongated structures, rivaling texture shift in damage but fixable by inference-time letterboxing choices alone.

- **Problem**: Domain-gap discussions focus on appearance, ignoring that preprocessing geometry (fixed square input, positional-embedding interpolation) deforms structure statistics; blame is misassigned and cheap fixes are missed.
- **Core hypothesis**: Performance loss on thin-structure domains decomposes into an appearance component and a preprocessing-geometry component, with the geometry component dominating when structures are near the internal resolution limit; changing only padding, tiling, and positional-embedding handling recovers it.
- **Falsifiable prediction**: A factorial evaluation crossing appearance (native vs style-matched) with preprocessing (default vs geometry-preserving) on thin-structure datasets attributes a larger share of the frozen-model deficit to preprocessing than to appearance, opposite to the community's implicit attribution.
- **Why important**: If a leading cause of failure is a controllable engineering choice, many reported domain gaps are inflated, and PEFT gains partly re-learn what better preprocessing gives for free.
- **Why possibly novel**: HYPOTHESIS: individual tricks (tiling, high-res variants) are known; a controlled attribution decomposing preprocessing geometry vs appearance shift appears missing.
- **Community default belief (what is treated as true)**: SAM fails on thin structures because such masks are rare in web-image training data (an appearance and prior problem).
- **Why that might be wrong**: A structure two internal-pixels wide is unresolvable regardless of priors; the resolution and distortion bottleneck logically precedes the prior-based explanation but is rarely isolated.
- **Minimal falsification experiment**: Two thin-structure datasets, 2x2 factorial (appearance matching x geometry-preserving preprocessing), frozen SAM; falsified if appearance dominates the decomposition everywhere.
- **Fastest falsification experiment**: Hours: one dataset, default vs tiled geometry-preserving inference with frozen SAM; the gap between them bounds the preprocessing component.
- **Main risk**: Geometry-preserving inference (tiles, overlaps) changes compute and context; fairness of comparison requires care.
- **Evidence labels**: community_default_belief: EVIDENCE (common explanation in adaptation papers); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM resizes inputs to a fixed square resolution in the released implementation

### W13-P1-A-038 — SAM is unusually sensitive to JPEG and resampling artifacts because SA-1B consisted of high-quality licensed photography, making compression level an unmodeled domain axis that hits SAM harder than supervised baselines.

- **Problem**: Real-world pipelines feed SAM heavily compressed or re-encoded images (screenshots, telemedicine, drone links), but robustness studies emphasize weather and noise corruptions, leaving codec-induced shift unquantified.
- **Core hypothesis**: The pretraining corpus's uniformly high image quality created a quality-blind spot: boundary-acuity features exploit high-frequency detail that compression destroys, so SAM's boundary quality degrades faster with compression strength than that of models trained on messy web data.
- **Falsifiable prediction**: Boundary-F scores as a function of JPEG quality decline with a steeper slope for frozen SAM than for segmentation baselines trained on standard (compression-diverse) datasets, and the loss concentrates in boundary precision rather than region recall.
- **Why important**: Compression is the single most common transformation applied to images in the wild; a documented codec fragility would change deployment guidance and motivate quality-diverse pretraining or augmentations.
- **Why possibly novel**: HYPOTHESIS: corruption benchmarks include JPEG as one entry, but a focused analysis of quality-distribution mismatch traced to the pretraining corpus, with boundary-decomposed metrics, appears missing.
- **Community default belief (what is treated as true)**: SAM's scale makes it robust to mundane perturbations like compression; robustness concerns center on weather, blur, and noise.
- **Why that might be wrong**: Scale conveys robustness only to variation present in the data; SA-1B's curation plausibly removed exactly this variation, and boundary precision depends on the frequencies compression removes first.
- **Minimal falsification experiment**: Evaluate frozen SAM and two baselines across a JPEG-quality ladder on shared benchmarks with boundary-decomposed metrics; falsified if SAM's slope is not steeper.
- **Fastest falsification experiment**: Hours: 100 images at 4 quality levels, frozen SAM boundary-F curve vs one baseline.
- **Main risk**: Attribution to corpus quality (rather than architecture) needs an extra control, e.g., an augmentation-retrained variant, which adds cost.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit robustness assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B was built from licensed high-resolution photography per the SAM paper

### W13-P1-A-039 — SAM's encoder exhibits high-norm outlier tokens (register-like sinks), and their spatial positions correlate with mask leakage errors, linking a known ViT pathology to concrete segmentation failures for the first time.

- **Problem**: Outlier tokens are documented in classification ViTs as a global-information artifact, but whether they exist in SAM and whether they matter for dense outputs is unknown; if they seed localized errors, a known cure (register tokens) becomes an adaptation-free fix.
- **Core hypothesis**: SAM's encoder develops a small set of high-norm tokens at semantically vacant positions; because the decoder reads the spatial feature map directly, these positions carry corrupted local information and are enriched among pixels where masks leak or fragment.
- **Falsifiable prediction**: High-norm token locations are stable per image, and conditional error rates at those locations exceed matched-control locations significantly; adding trained register tokens (with brief adapter-level tuning) reduces exactly those errors without moving other metrics.
- **Why important**: It would connect representation pathology research to dense-prediction quality with a causal repair, and provide a concrete mechanism for a subset of hitherto-unexplained SAM errors.
- **Why possibly novel**: HYPOTHESIS: outlier tokens and registers are established for classification ViTs (Darcet et al.); their dense-prediction consequences in SAM appear unexamined.
- **Community default belief (what is treated as true)**: Outlier tokens are a curiosity of classification ViTs with no established consequence for dense prediction quality.
- **Why that might be wrong**: Dense decoders consume every spatial position, so a pathology harmless under global pooling becomes load-bearing; nobody has looked because the pathology was discovered in a different subfield.
- **Minimal falsification experiment**: Detect high-norm tokens across 1000 images, test error enrichment at their positions with matched controls; then a register-tuning intervention arm; falsified if no enrichment or no targeted repair.
- **Fastest falsification experiment**: Hours: token-norm maps for 50 images, overlay with SAM error maps, visual plus statistical check of co-location.
- **Main risk**: SAM's segmentation training may have suppressed outlier formation, yielding a clean null (itself informative but less publishable).
- **Evidence labels**: community_default_belief: VERIFIED PRIOR WORK (outlier tokens documented in ViTs, e.g., registers paper by Darcet et al. 2023); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK for the pathology in classification ViTs; SAM-specific claims are MODEL SPECULATION

### W13-P1-A-040 — An adaptability meter for SAM: pre-adaptation representation-similarity between frozen SAM features and a tiny target-domain-supervised probe network predicts final PEFT gain, letting teams forecast adaptation ROI before spending compute.

- **Problem**: Teams cannot predict whether PEFT will lift a new domain by two points or twenty; a cheap pre-hoc predictor would rationalize compute allocation across the many domains competing for adaptation effort.
- **Core hypothesis**: The achievable PEFT gain is governed by how much target-relevant structure frozen features already contain but misalign, which is measurable as the gap between (a) similarity of frozen SAM features to features of a small net trained on 50 target images and (b) frozen SAM's zero-shot performance; large similarity with poor zero-shot predicts large PEFT gain.
- **Falsifiable prediction**: Across at least ten domains, a two-variable predictor (feature similarity, zero-shot score) explains most of the variance in realized LoRA gain, and the similarity term carries significant weight beyond zero-shot score alone.
- **Why important**: Forecasting fine-tuning outcomes from frozen-model measurements is a general capability the field lacks; segmentation offers dense supervision that makes tiny probe networks meaningful, making it the right testbed.
- **Why possibly novel**: HYPOTHESIS: transferability estimation exists for classification (LEEP-style measures); a validated pre-hoc gain predictor for segmentation PEFT with the misalignment framing appears new.
- **Community default belief (what is treated as true)**: You find out what fine-tuning buys by fine-tuning; zero-shot performance is the only available forecast.
- **Why that might be wrong**: Zero-shot score conflates two different states (features absent vs features misaligned) that have opposite implications for adaptation, and similarity measurements can separate them.
- **Minimal falsification experiment**: Ten domains: train tiny probes on 50 images each, compute similarity and zero-shot scores, run standardized LoRA, regress gains; falsified if the regression is weak or the similarity term is useless.
- **Fastest falsification experiment**: Three domains chosen to span the hypothesis space (high-sim/low-zero-shot, low-sim/low-zero-shot, high/high): check gain ordering matches prediction; two days including LoRA runs at SAM-B scale.
- **Main risk**: Ten domains may be too few for a stable regression; conclusions are hostage to domain-suite selection.
- **Evidence labels**: community_default_belief: EVIDENCE (current practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: transferability estimation exists for classification (e.g., LEEP, Nguyen et al. 2020); segmentation instantiation is MODEL SPECULATION

## Cluster: `decoder_token_mechanics` (8 ideas)

### W13-P1-A-041 — The two-layer mask decoder, not the encoder, is the binding constraint for dense thin structures: deepening only the decoder (keeping the encoder frozen) recovers vessel- and crack-like segmentation that encoder PEFT cannot, at a fraction of the parameters.

- **Problem**: Thin-structure failure is attributed to encoder resolution and priors, driving expensive encoder-side interventions, but nobody has tested whether the decoder's two rounds of cross-attention simply cannot propagate connectivity information along elongated structures.
- **Core hypothesis**: Segmenting elongated connected structures requires iterative evidence propagation proportional to structure length; two decoder layers implement a fixed small number of propagation steps, so failures scale with structure tortuosity and are relieved by decoder depth, not encoder adaptation.
- **Falsifiable prediction**: Error rate on thin structures increases with geodesic length-to-width ratio under frozen SAM; adding decoder layers (trained on modest data, encoder frozen) flattens this curve, while encoder LoRA at matched parameters does not.
- **Why important**: It relocates a famous failure mode from the expensive component to the cheap one, changes adaptation strategy for a large application family, and provides an interpretable computational account (propagation depth) of a failure.
- **Why possibly novel**: HYPOTHESIS: decoder modifications for quality exist (e.g., HQ-SAM adds tokens and features), but the propagation-depth account of thin-structure failure with a tortuosity-stratified test appears new.
- **Community default belief (what is treated as true)**: Thin-structure failure stems from the encoder's internal resolution and pretraining priors; the decoder is a sufficient lightweight head.
- **Why that might be wrong**: Cross-attention with a handful of tokens over a coarse grid gives few sequential integration steps, while linear structures demand many; the encoder may already represent the structure that the decoder cannot trace.
- **Minimal falsification experiment**: Stratify a vessel-like dataset by tortuosity, evaluate frozen SAM, decoder-deepened SAM, and encoder-LoRA SAM at matched trainable parameters; falsified if decoder depth does not preferentially fix high-tortuosity errors.
- **Fastest falsification experiment**: One day: freeze everything, train a 4-layer decoder clone vs the standard 2-layer on the same small vessel dataset, compare tortuosity-stratified curves.
- **Main risk**: Deepened decoders must be trained, so gains could come from extra data exposure rather than depth; parameter- and data-matched controls are essential.
- **Evidence labels**: community_default_belief: EVIDENCE (dominant explanation in adaptation literature); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: HQ-SAM (Ke et al. 2023) improves mask quality via decoder-side changes; the propagation-depth mechanism is MODEL SPECULATION

### W13-P1-A-042 — SAM's mask tokens are overloaded scale-generalists: forcing token specialization by object scale (a handful of scale-conditioned output tokens) tests whether token capacity, not feature quality, limits small-object segmentation.

- **Problem**: Small-object failure is blamed on features or resolution, but a single learned output token must serve objects across four orders of magnitude of area, and the token-capacity explanation has never been isolated.
- **Core hypothesis**: A single output token's query vector cannot be simultaneously optimal for all scales, so the effective operating point is biased toward the training-mass scale; adding scale-dedicated tokens (trained briefly, all else frozen) disproportionately improves off-modal scales.
- **Falsifiable prediction**: Scale-stratified accuracy of frozen SAM shows depressed performance at scale extremes; a token-specialized variant trained on the same data redistributes accuracy toward extremes, while an equally-parameterized non-specialized control does not.
- **Why important**: It probes whether the query-token bottleneck is a real capacity limit in promptable architectures, informing decoder design beyond SAM (any DETR-style promptable head).
- **Why possibly novel**: HYPOTHESIS: multi-token decoders exist for quality (HQ-SAM) and ambiguity (SAM itself), but scale-conditioned token specialization as a causal test of token overload appears untried.
- **Community default belief (what is treated as true)**: Output tokens are flexible queries; failures at scale extremes come from features and internal resolution, not from token capacity.
- **Why that might be wrong**: In DETR-style systems queries famously specialize by location and size on their own, suggesting one shared query serving all scales is an unnatural operating regime that training mass will bias.
- **Minimal falsification experiment**: Train 3 scale-conditioned tokens vs 3 unconditioned extra tokens (control) on identical data with frozen backbone; compare scale-stratified gains; falsified if both arms move identically.
- **Fastest falsification experiment**: Hours for the descriptive half: scale-stratified accuracy curve of frozen SAM on one instance dataset to confirm the off-modal depression exists and is large.
- **Main risk**: Scale conditioning requires knowing scale at inference; a scale-router adds complexity that may absorb the gains.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: DETR query specialization is documented (Carion et al. 2020); token-overload claim for SAM is MODEL SPECULATION

### W13-P1-A-043 — SAM has a constant systematic boundary offset (not proportional jitter) traceable to its 4x upsampling path, which means a universal sub-pixel correction could improve every SAM output at zero model cost.

- **Problem**: Boundary error is treated as stochastic and content-driven; if a fixed directional or radial bias exists from the transposed-convolution upsampler, all downstream measurements (areas, volumes, morphometrics) are biased, and a post-hoc correction is free accuracy.
- **Core hypothesis**: The learned upsampling path induces a content-independent boundary displacement field (systematic erosion or dilation of a fixed sub-pixel magnitude, possibly orientation-dependent), detectable by aggregating signed boundary errors over many objects and correctable by a fixed morphological adjustment.
- **Falsifiable prediction**: Signed distance between predicted and true boundaries, aggregated over thousands of straight-boundary segments, has a nonzero mean of consistent sign across datasets, roughly independent of object size and texture; applying the inverse offset improves boundary-F everywhere.
- **Why important**: A universal correction improving all deployments is rare low-hanging fruit, and the measurement methodology (signed aggregate boundary bias) would become a standard audit for any dense predictor.
- **Why possibly novel**: HYPOTHESIS: boundary quality is heavily studied, but decomposition into constant systematic bias vs proportional jitter, and attribution to the upsampling path, appears missing for SAM.
- **Community default belief (what is treated as true)**: Boundary errors are content-dependent noise; there is no free constant to subtract.
- **Why that might be wrong**: Learned transposed convolutions are known to produce systematic phase biases in other dense tasks, and SAM's logits are thresholded at a fixed value that need not coincide with the true boundary level set.
- **Minimal falsification experiment**: Aggregate signed boundary error over three datasets stratified by orientation and scale; falsified if mean bias is near zero or sign-inconsistent across datasets.
- **Fastest falsification experiment**: Hours: synthetic images with exactly known boundaries (rendered shapes), measure signed offset distribution of frozen SAM masks.
- **Main risk**: Annotation conventions (annotators biased inward or outward) could produce the same signature; multi-dataset consistency and synthetic-image controls are the discriminator.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM's decoder upsamples mask logits through a learned path and thresholds at a fixed value

### W13-P1-A-044 — Promptable segmentation cannot express relationally-defined regions (the gap between two objects, the part of A occluded by B), a representational blind spot of prompt-as-locator interfaces that no amount of PEFT fixes.

- **Problem**: The prompt interface assumes every desired region is an appearance-coherent thing a point or box can indicate, but many practically-needed regions are defined by relations between things; the boundary of this expressible set has never been mapped.
- **Core hypothesis**: SAM's decoder implements approximate appearance-similarity expansion around the prompt, so regions whose definition requires relations rather than appearance coherence (gaps, shadows-of, occluded-parts-of) sit outside the reachable output set regardless of prompt engineering, and PEFT shifts but does not remove the boundary.
- **Falsifiable prediction**: On a taxonomy of region types (appearance-coherent, boundary-coherent, relational), exhaustive prompt search achieves high best-IoU for the first two classes and drastically lower for relational regions, and LoRA on relational examples improves in-category performance only marginally compared to its effect on appearance categories.
- **Why important**: Mapping the expressiveness frontier of promptable interfaces tells the field what promptability can and cannot deliver, motivating relation-aware prompt types rather than more adaptation of the same interface.
- **Why possibly novel**: HYPOTHESIS: individual failure anecdotes exist; a systematic expressiveness taxonomy with reachability measurement (best achievable IoU over exhaustive prompts) appears new.
- **Community default belief (what is treated as true)**: With the right prompts (or light fine-tuning), SAM can segment anything a user can indicate.
- **Why that might be wrong**: The decoder's computation is anchored to appearance affinity with the prompted location; relational regions have no anchoring appearance, so the failure is architectural, not a data gap.
- **Minimal falsification experiment**: Annotate 100 relational and 100 matched appearance-coherent regions, run exhaustive prompt search (points, boxes, multi-point combos) for best-IoU, then a LoRA arm on relational training data; falsified if relational best-IoU is comparable or trains up easily.
- **Fastest falsification experiment**: Hours: 20 gap-between-objects cases, dense prompt search, record best achievable IoU; uniformly low values are immediate signal.
- **Main risk**: Exhaustive prompt search is approximate; claiming unreachability requires careful search-budget arguments.
- **Evidence labels**: community_default_belief: EVIDENCE (marketing framing and common expectation); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-045 — The hypernetwork MLP mapping mask tokens to dynamic convolution weights in SAM is effectively linear: distilling it to a linear map costs almost nothing, revealing that the decoder's expressive component is placed where expressivity is not used.

- **Problem**: Architectural components are assumed to earn their nonlinearity; if SAM's dynamic-filter generator operates in a linear regime, the field misunderstands where the decoder's actual work happens, which matters for compression and for redesign.
- **Core hypothesis**: Across prompts and images, the token-to-filter MLP's input-output map is well-approximated by its best linear fit (high R-squared), and swapping in the linear fit changes masks negligibly; the decoder's nonlinear work is concentrated in attention, not filter generation.
- **Falsifiable prediction**: A linear surrogate for the hypernetwork, fit on activations from a modest image set, preserves mask outputs above 0.95 IoU on held-out images, while the same procedure applied to attention layers fails badly.
- **Why important**: It identifies dead expressivity in a widely-copied architecture, enables cheaper decoder variants, and demonstrates a general audit (linear-regime detection) applicable to any hypernetwork component.
- **Why possibly novel**: HYPOTHESIS: linear-regime analyses exist for classifiers; auditing SAM's dynamic-filter path specifically appears undone.
- **Community default belief (what is treated as true)**: Each decoder component, including the filter-generating MLP, contributes necessary nonlinear computation.
- **Why that might be wrong**: Hypernetwork-style paths often collapse to low effective rank and near-linear behavior when trained with strong upstream representations, but nobody checks after publication.
- **Minimal falsification experiment**: Fit linear surrogate on 1000 prompts, evaluate output fidelity on 1000 held-out prompts across two datasets; falsified if fidelity is low in-distribution.
- **Fastest falsification experiment**: Hours: fit and swap on 100 images, histogram output IoU between original and surrogate.
- **Main risk**: Linearity may hold in-distribution but break exactly on hard or shifted cases, inverting the practical conclusion; shifted-domain fidelity must be measured too.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM generates mask filters from tokens via an MLP per the paper; linearity claim is MODEL SPECULATION

### W13-P1-A-046 — Prompt tokens dilute output tokens in decoder self-attention: SAM's accuracy degradation with many clicks is an attention-budget artifact with a predictable functional form, fixable by attention masking rather than retraining.

- **Problem**: Users adding more clicks expect monotone improvement, but heavily-prompted SAM sometimes worsens; if the cause is attention dilution (output token's attention mass spread over many prompt tokens), the fix is architectural bookkeeping, not more training.
- **Core hypothesis**: As prompt-token count grows, the output token's self-attention allocation to informative tokens shrinks roughly inversely, degrading integration; renormalizing or masking self-attention at inference restores monotonicity without weight changes.
- **Falsifiable prediction**: Accuracy vs click-count curves plateau then dip for standard SAM, with dip onset predicted by measured attention-mass dilution; an inference-time attention renormalization removes the dip on the same prompts.
- **Why important**: Monotone-improvement-with-more-input is a basic usability contract for interactive systems; diagnosing and repairing its violation via mechanism (not retraining) shows the value of mechanistic analysis for product-level fixes.
- **Why possibly novel**: HYPOTHESIS: many-click degradation is anecdotally known; the attention-dilution mechanism with a training-free intervention appears untested.
- **Community default belief (what is treated as true)**: More clicks give the model strictly more information, so performance should not degrade; observed dips are user error.
- **Why that might be wrong**: Softmax attention is a fixed budget; adding tokens mechanically dilutes it, and SAM's training saw mostly few-click episodes, leaving the many-click regime uncalibrated.
- **Minimal falsification experiment**: Measure accuracy and output-token attention mass vs click count (1 to 24) on 300 objects; then apply attention renormalization and re-measure; falsified if no dip exists, or the dip persists under renormalization.
- **Fastest falsification experiment**: Hours: 30 objects, scripted informative clicks up to 20, plot the curve; a reproducible dip plus dilution measurements is the first checkpoint.
- **Main risk**: Degradation may instead come from conflicting click semantics (later clicks in ambiguous positions), requiring careful simulated-click protocols that keep information content fixed while varying count.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit usability assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM's decoder self-attends over concatenated prompt and output tokens per the paper

### W13-P1-A-047 — Encoder-side PEFT breaks an implicit encoder-decoder contract in SAM: feature drift makes the frozen decoder's cross-attention read features it was never calibrated for, and a contract-violation metric predicts when joint (vs encoder-only) tuning is required.

- **Problem**: Recipes freeze the decoder during encoder adaptation to save parameters and preserve promptability, assuming decoder tolerance to feature change; there is no measure of when this assumption fails and silently caps adaptation gains.
- **Core hypothesis**: The frozen decoder tolerates feature drift up to a threshold measurable as divergence of decoder cross-attention statistics (entropy, focus location) from their pretraining regime; beyond it, encoder-only tuning saturates and joint tuning pulls ahead, with the threshold consistent across domains.
- **Falsifiable prediction**: Across adaptation runs, the gap between encoder-only and joint tuning correlates strongly with the contract-violation metric measured on the encoder-only model, enabling a decision rule that predicts (before running joint tuning) which regime a domain is in.
- **Why important**: It converts a folklore recipe choice into a measurable criterion and characterizes modular tolerance in composite foundation models, relevant wherever frozen heads consume adapted backbones.
- **Why possibly novel**: HYPOTHESIS: freeze-vs-joint comparisons exist per-paper; an interface-drift metric that predicts the comparison outcome appears new.
- **Community default belief (what is treated as true)**: The decoder is robust to encoder adaptation; freezing it is safe and standard.
- **Why that might be wrong**: The decoder's two layers were trained against one specific feature distribution; nothing regularizes adapted features to stay readable, and two layers have little capacity to absorb distributional surprise.
- **Minimal falsification experiment**: Six domains, encoder-only and joint arms, compute attention-statistic divergence on encoder-only checkpoints, correlate with the joint-minus-encoder-only gap; falsified if no predictive relationship.
- **Fastest falsification experiment**: One day: one hard domain, encoder-only vs joint runs, plus the divergence measurement; a big gap co-occurring with big divergence is the first confirmation.
- **Main risk**: Attention statistics may drift benignly; the metric needs a null model of harmless drift to avoid false alarms.
- **Evidence labels**: community_default_belief: EVIDENCE (standard recipe); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-048 — SAM's decoder cannot represent holes below a scale threshold: mask topology is systematically simplified (genus reduced) as hole size shrinks, defining a topological failure family with a measurable critical scale.

- **Problem**: Applications needing topologically-correct masks (rings, perforated parts, loops of vasculature) rely on SAM without knowing that its architecture may impose a resolution-dependent topology filter that silently closes holes.
- **Core hypothesis**: The coarse internal grid plus smooth upsampling acts as a low-pass filter on the mask indicator function, so holes below a critical fraction of object scale are filled with probability approaching one, and the critical scale is predictable from the internal feature resolution and stable across content.
- **Falsifiable prediction**: On synthetic annuli and perforated shapes swept across hole-size ratios, hole-preservation probability transitions sharply at a critical ratio that matches internal-resolution arithmetic, and the transition point is invariant to texture but shifts with input resolution scaling exactly as predicted.
- **Why important**: A quantitative topology-fidelity law tells practitioners when SAM outputs can be trusted for topology-sensitive downstream tasks and gives architecture designers a concrete target (topology-preserving decoding).
- **Why possibly novel**: HYPOTHESIS: topology-aware segmentation losses exist; a measured topological transfer function for a foundation segmenter appears absent.
- **Community default belief (what is treated as true)**: SAM masks are pixelwise decisions; topology errors are just boundary noise, not a systematic filter with a critical scale.
- **Why that might be wrong**: The mask is decoded from a 64x64-scale representation through smooth learned upsampling; representation theory says sub-grid topology cannot be encoded, but nobody has measured where the cliff sits or checked its lawfulness.
- **Minimal falsification experiment**: Synthetic sweep over hole ratios, textures, and input resolutions; fit transition points; falsified if hole survival is content-dependent or does not scale with internal resolution as predicted.
- **Fastest falsification experiment**: Hours: annulus sweep at one resolution, plot hole-survival vs ratio, check for a sharp transition.
- **Main risk**: Synthetic stimuli may understate real-image performance where context cues help; a small real perforated-object set should corroborate.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM decodes masks from a coarse internal feature grid per the paper

## Cluster: `sam2_video_memory` (9 ideas)

### W13-P1-A-049 — SAM2's memory bank induces confirmation bias: early mask errors are written to memory and then re-read as evidence, making per-object error growth superlinear after occlusions in a way promptless re-initialization would avoid.

- **Problem**: Streaming-memory tracking is celebrated for temporal consistency, but consistency is a double-edged sword: it can lock in errors; the field lacks a measurement separating error persistence caused by memory from error caused by frames being hard.
- **Core hypothesis**: Because memory attention conditions current predictions on past predicted masks, an error written at time t raises the probability of the same error at t+1 beyond what frame difficulty explains, creating a self-reinforcing loop whose strength grows with the number of memory slots the error occupies.
- **Falsifiable prediction**: In paired runs on identical frames where one arm has its memory surgically corrected (ground-truth mask injected at time t) and the other does not, downstream error divergence exceeds what a memoryless per-frame model shows; error autocorrelation in SAM2 exceeds frame-difficulty-matched controls and jumps after each occlusion event.
- **Why important**: It quantifies the stability-plasticity trade-off of memory architectures with a causal method (memory surgery), guiding when trackers should distrust their own memory, and defines a general evaluation for self-conditioned video models.
- **Why possibly novel**: HYPOTHESIS: tracking drift is old knowledge, but causal attribution of drift to the memory-conditioning loop via memory-intervention experiments in SAM2 appears new.
- **Community default belief (what is treated as true)**: Memory improves tracking robustness; occasional drift is a price worth paying and is caused by hard frames, not by the memory mechanism itself.
- **Why that might be wrong**: Conditioning on your own outputs is a classic positive-feedback design; in language models it produces exposure-bias cascades, and SAM2's memory is architecturally analogous, yet the analogy is untested.
- **Minimal falsification experiment**: On videos with dense ground truth, run SAM2 with and without one-time memory correction at controlled error points, measure divergence curves; falsified if corrected and uncorrected runs reconverge quickly (memory does not perpetuate errors).
- **Fastest falsification experiment**: One day: 20 videos, inject a synthetic error into memory at frame k (paint a wrong mask), measure how many frames the injected error persists vs a no-injection control.
- **Main risk**: Memory surgery requires implementation access to SAM2 internals; engineering effort could dominate.
- **Evidence labels**: community_default_belief: EVIDENCE (SAM2 paper framing); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 (Ravi et al. 2024) uses a streaming memory bank conditioned on past predictions; the confirmation-bias dynamics are MODEL SPECULATION

### W13-P1-A-050 — SAM2's object memory encodes appearance rather than identity: repeated similar objects (twins, uniform players, identical parts) cause identity swaps at rates predictable from appearance similarity alone, exposing the absence of spatiotemporal identity binding.

- **Problem**: Users assume a video object segmenter tracks the indicated object; if memory matching is appearance-based, semantically identical distractors will capture the track, and no benchmark isolates this because standard video datasets rarely control distractor similarity.
- **Core hypothesis**: Swap probability at crossing or proximity events is a monotone function of feature-space similarity between target and distractor, approximately independent of motion-continuity cues that would trivially disambiguate for a tracker with a motion model, revealing that memory attention lacks positional-continuity binding.
- **Falsifiable prediction**: On a controlled benchmark of same-appearance distractor events (filmed or composited), swap rate rises steeply with appearance similarity and is barely reduced when motion continuity is made maximally informative (slow, smooth, non-overlapping paths).
- **Why important**: It defines the identity-binding failure of memory-based video segmentation with a quantitative law, directly motivating (and providing the evaluation for) motion-aware memory designs.
- **Why possibly novel**: HYPOTHESIS: identity swaps are known in multi-object tracking; a similarity-parameterized causal characterization for promptable video segmentation appears missing.
- **Community default belief (what is treated as true)**: SAM2 tracks the prompted object; failures happen in cluttered or fast scenes, not as lawful appearance-similarity capture in easy scenes.
- **Why that might be wrong**: Memory attention retrieves by feature similarity; unless training data punished appearance-based retrieval with identical distractors (rare in web video), positional binding had no gradient pressure to emerge.
- **Minimal falsification experiment**: Build 200 controlled distractor events by compositing (control similarity via appearance interpolation), run SAM2, regress swap rate on similarity and motion informativeness; falsified if motion cues dominate.
- **Fastest falsification experiment**: Hours: a dozen composited crossing events at three similarity levels, count swaps; a similarity-ordered swap rate is the first signal.
- **Main risk**: Composited videos may introduce artifacts SAM2 detects; filmed twin-object sets are cleaner but harder to parameterize.
- **Evidence labels**: community_default_belief: EVIDENCE (benchmark-driven impressions); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 memory attention design; the appearance-only binding claim is MODEL SPECULATION

### W13-P1-A-051 — Video training regressed SAM2's single-image behavior in specific structure families relative to SAM1 (a capability trade nobody has mapped), so image-mode users may be silently better served by the older model.

- **Problem**: SAM2 is presented as a strict upgrade covering images and video; if temporal training reallocated capacity away from certain static-image competencies (fine boundaries, tiny objects, dense scenes), the community's default upgrade path is wrong for some users and nobody knows which.
- **Core hypothesis**: Multi-objective training (video plus image) with shared capacity creates measurable regressions on static-image subfamilies where video supervision is misaligned with fine spatial detail, e.g., because video masks are temporally smoothed and lower-detail than SA-1B annotations.
- **Falsifiable prediction**: A stratified image-mode audit (boundary detail, object size, scene density, structure type) shows statistically robust SAM1-over-SAM2 wins concentrated in identifiable strata, not random noise, with effect direction stable across datasets.
- **Why important**: Model-succession decisions across the industry assume monotone improvement; a mapped regression profile would correct deployment guidance and illuminate what multi-task video training costs static perception.
- **Why possibly novel**: HYPOTHESIS: aggregate image-mode comparisons exist in the SAM2 report; a stratified regression map designed to find where the newer model loses appears absent.
- **Community default belief (what is treated as true)**: SAM2 is at least as good as SAM1 on images, so image users should upgrade unconditionally.
- **Why that might be wrong**: Shared-capacity multi-task training essentially always trades somewhere; the interesting question is where, and aggregate metrics are designed (unintentionally) not to show it.
- **Minimal falsification experiment**: Run both models on several image benchmarks with stratified metrics and matched prompting, apply multiple-comparison-corrected tests per stratum; falsified if no coherent regression strata survive correction.
- **Fastest falsification experiment**: One day: both models, one dense-scene and one fine-boundary dataset, stratified comparison with matched prompts.
- **Main risk**: Regressions may be small enough to be practically irrelevant even if statistically real; effect sizes must be reported honestly.
- **Evidence labels**: community_default_belief: EVIDENCE (release framing and aggregate numbers); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 supports image mode and reports strong aggregate image results; the strata-level regression claim is MODEL SPECULATION

### W13-P1-A-052 — SAM2 has a hard forgetting horizon set by its memory capacity: reacquisition probability after occlusion collapses at a critical occlusion duration (a cliff, not a slope), and the cliff location is a fixed architectural constant rather than content-dependent.

- **Problem**: Practitioners need to know how long an object can disappear before the tracker is effectively re-initialized, but robustness is reported as averages over uncontrolled occlusion statistics, hiding whether degradation is graceful or cliff-like.
- **Core hypothesis**: Because the memory bank holds a bounded number of recent frames plus prompted frames, occlusions longer than the effective temporal span evict all target evidence except the distant prompt, producing a sharp phase transition in reacquisition probability whose location depends on memory configuration, frame rate, and eviction policy, but only weakly on scene content.
- **Falsifiable prediction**: Reacquisition probability vs occlusion duration (controlled synthetic occlusions on real videos) shows a sigmoid with a sharp transition; the transition point shifts predictably when memory size or frame sampling is reconfigured, and varies little across content categories.
- **Why important**: A quantified memory horizon is an operational spec every deployment needs (how long can a surgical tool leave frame, a pedestrian be occluded), and phase-transition behavior would sharpen theory about bounded-memory streaming architectures.
- **Why possibly novel**: HYPOTHESIS: occlusion robustness is benchmarked in aggregate; a controlled duration-sweep establishing cliff-vs-slope and its architectural determinants appears new.
- **Community default belief (what is treated as true)**: Longer occlusions are gradually harder; performance degrades smoothly with occlusion length.
- **Why that might be wrong**: Bounded-slot memories do not degrade gracefully: evidence either survives eviction or does not, which mathematically predicts a threshold effect the aggregate benchmarks average away.
- **Minimal falsification experiment**: Insert synthetic full occlusions of parameterized duration into 100 videos, sweep memory configurations, fit transition curves; falsified if degradation is linear or strongly content-dependent.
- **Fastest falsification experiment**: Hours: 20 videos, five occlusion durations, plot reacquisition vs duration; a visible cliff answers the shape question immediately.
- **Main risk**: Synthetic occlusion may not trigger the same occlusion-head behavior as natural occlusion; a natural-occlusion validation subset is needed.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit smooth-degradation assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 maintains a bounded memory of recent and prompted frames per the paper

### W13-P1-A-053 — For video domain shift, adapting only SAM2's memory-attention layers beats adapting the image encoder at equal parameter budget: domain gap in video lives in temporal association, not appearance encoding.

- **Problem**: Video PEFT recipes copy image PEFT (adapt the encoder), assuming appearance shift dominates; if association rules (how memory matches across time) are what break in new domains like medical endoscopy or thermal drones, the standard recipe misallocates all its capacity.
- **Core hypothesis**: Cross-domain failures in video segmentation are dominated by memory retrieval errors (wrong temporal association under new motion and appearance-change statistics) rather than frame-level encoding errors, so memory-attention LoRA recovers more tracking accuracy per parameter than encoder LoRA.
- **Falsifiable prediction**: On several shifted video domains, memory-attention-only LoRA outperforms encoder-only LoRA at matched parameters on tracking metrics while losing slightly on single-frame metrics, and the advantage grows with the domain's temporal-statistics distance from natural video.
- **Why important**: It would establish that temporal association is a separately-adaptable competence with its own domain gap, reshaping how video foundation models are adapted and evaluated.
- **Why possibly novel**: HYPOTHESIS: PEFT for SAM2 exists in early forms; the encoder-vs-memory allocation question with temporal-statistics analysis appears open.
- **Community default belief (what is treated as true)**: Adapting the image encoder is how you adapt any vision model, including video models; temporal machinery generalizes.
- **Why that might be wrong**: Temporal statistics (deformation rates, illumination dynamics, camera motion) differ across domains at least as much as appearance, and memory attention was trained only on natural-video temporal statistics.
- **Minimal falsification experiment**: Three shifted video domains, three arms (encoder LoRA, memory LoRA, both) at matched budgets, tracking and per-frame metrics; falsified if encoder adaptation dominates everywhere.
- **Fastest falsification experiment**: One day: one shifted domain, two arms at small budget, compare tracking-metric recovery per parameter.
- **Main risk**: Public shifted-video segmentation datasets with dense annotation are scarce; may require assembling evaluation data.
- **Evidence labels**: community_default_belief: EVIDENCE (image-PEFT convention); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 architecture separates image encoding from memory attention; the allocation claim is MODEL SPECULATION

### W13-P1-A-054 — SAM2's occlusion prediction is a motion-prior guess, not an evidence-based judgment: it infers disappearance from motion patterns rather than from what pixels show, failing lawfully on static occlusions and motionless disappearances.

- **Problem**: The occlusion head gates whether the model reports the object as present; if it keys on motion statistics instead of visual evidence, whole application classes (static cameras, slow scenes, objects hidden by moving occluders while stationary) inherit a systematic blind spot nobody has characterized.
- **Core hypothesis**: Occlusion-head accuracy is high when occlusion co-occurs with characteristic motion signatures (as in web video training data) and collapses when occlusion is decoupled from motion (static object occluded by another static object after a camera pan, object occluded without either moving), revealing the head learned motion-occlusion correlation rather than visibility reasoning.
- **Falsifiable prediction**: On a controlled battery decoupling motion from visibility (four cells: moving/static object x moving/static occluder), occlusion-head error concentrates in the decoupled cells, with error rates several times the coupled cells.
- **Why important**: It identifies which occlusion judgments downstream systems can trust and demonstrates a shortcut-learning failure inside a headline capability of a flagship model.
- **Why possibly novel**: HYPOTHESIS: the occlusion head's decision basis appears never to have been probed with motion-visibility decoupling.
- **Community default belief (what is treated as true)**: The occlusion head reads visual evidence of the object being covered; its errors come from ambiguity, not from a motion shortcut.
- **Why that might be wrong**: In web video, occlusion almost always co-occurs with motion, so a motion shortcut fits training data perfectly and is cheaper to learn than visibility reasoning; shortcut theory predicts the model took it.
- **Minimal falsification experiment**: Film or composit 100 clips covering the four decoupling cells, run SAM2, compare occlusion-head confusion matrices per cell; falsified if performance is uniform.
- **Fastest falsification experiment**: Hours: ten static-occlusion clips (pan camera behind pillar while both objects static), check occlusion-head outputs against obvious ground truth.
- **Main risk**: Constructing convincing decoupled cases at scale requires filming effort or careful compositing.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 includes an occlusion-prediction output per the paper; the shortcut claim is MODEL SPECULATION

### W13-P1-A-055 — SAM2 has a preferred temporal sampling rate: tracking accuracy is non-monotone in frame rate, peaking near training-video statistics, so both slowing down and speeding up input degrades it, contrary to the assumption that more frames never hurt.

- **Problem**: Deployments choose frame rates by compute budget assuming a monotone accuracy-compute trade-off; if memory attention is tuned to a band of inter-frame change magnitudes, aggressive frame rates actively hurt, and nobody has measured the response curve.
- **Core hypothesis**: Memory retrieval and update were optimized for the inter-frame displacement distribution of training videos, so both under-sampling (too much change per step) and over-sampling (near-duplicate frames flooding memory slots and diluting temporal diversity) reduce accuracy, producing an inverted-U response to frame rate.
- **Falsifiable prediction**: On fixed videos re-sampled at multiple rates (with memory size held constant), tracking accuracy follows an inverted-U with an interior optimum, and the optimum shifts when memory eviction policy is modified, implicating slot competition rather than image content.
- **Why important**: A tuned-band temporal sensitivity would change deployment guidance (higher FPS can be worse for free) and reveal that streaming memory models have a temporal operating range analogous to a resonance, a design consideration for all future streaming architectures.
- **Why possibly novel**: HYPOTHESIS: frame-rate ablations exist for trackers, but the inverted-U prediction tied to memory-slot competition, with eviction-policy manipulation as the causal test, appears new.
- **Community default belief (what is treated as true)**: More temporal samples give the tracker more information; high frame rate is always at least neutral for accuracy.
- **Why that might be wrong**: Bounded memory means frames compete for slots; near-duplicates crowd out temporally diverse evidence, a mechanism absent from unbounded-memory intuitions the community carries over.
- **Minimal falsification experiment**: Resample 50 videos at five rates, run SAM2 with fixed memory config, plot accuracy vs rate; then vary eviction policy to test optimum shift; falsified if accuracy is monotone in rate.
- **Fastest falsification experiment**: Hours: five videos at three rates (quarter, native, four-x via interpolation), check for non-monotonicity.
- **Main risk**: Ground-truth interpolation across resampled rates introduces evaluation noise; annotation-preserving resampling protocols are needed.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit monotonicity assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 streaming memory with bounded recent-frame slots; the inverted-U claim is MODEL SPECULATION

### W13-P1-A-056 — Propagation in SAM2 is temporally asymmetric beyond content effects: propagating a middle-frame prompt backward is systematically worse than forward, revealing an architectural arrow of time that batch (offline) video adaptation should exploit or repair.

- **Problem**: Offline users (annotators, editors) prompt at whichever frame is easiest and propagate both directions, assuming symmetry; a directional handicap would bias annotation quality within every produced dataset in an unexamined way.
- **Core hypothesis**: Training predominantly on forward-streaming episodes taught memory attention forward-conditional statistics (how objects evolve forward in time), so backward propagation runs the model off its learned conditional distribution even on time-symmetric content, producing an accuracy gap that persists on reversibility-controlled clips.
- **Falsifiable prediction**: On clips filtered for approximate time-reversal symmetry of content (no gravity-driven or causal-direction cues), forward propagation from a middle prompt outperforms backward propagation with a consistent margin, and the margin persists when clips are physically reversed (controlling content direction).
- **Why important**: Datasets annotated with SAM2 assistance inherit direction-dependent quality gradients (later frames better than earlier), a bias that will propagate into every model trained on them; also a clean case study of temporal inductive bias in streaming architectures.
- **Why possibly novel**: HYPOTHESIS: forward-backward asymmetry with content-direction controls (reversed-clip protocol) appears unmeasured for SAM2.
- **Community default belief (what is treated as true)**: Propagation quality depends on content difficulty, not direction; backward equals forward for symmetric content.
- **Why that might be wrong**: The model's conditional distribution was fit on one temporal direction; even on symmetric content, learned drift priors (e.g., growth vs shrinkage of masks) need not be symmetric.
- **Minimal falsification experiment**: Select or film 100 near-time-symmetric clips, propagate from middle prompts both directions on original and reversed versions, compare accuracy in a 2x2 design; falsified if the architectural asymmetry vanishes under reversal control.
- **Fastest falsification experiment**: Hours: 20 clips, middle prompt, both directions, paired comparison; the reversed-clip control can follow if a gap appears.
- **Main risk**: Truly time-symmetric content is rare; the filter may leave few clips or subtle asymmetries.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit symmetry assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 processes video as a stream; the asymmetry claim is MODEL SPECULATION

### W13-P1-A-057 — Adapting SAM2 on domain video corrupts its image-mode promptability faster than adapting SAM1 on matched images does, because gradients through memory attention couple the static pathway to temporal objectives, making video PEFT uniquely forgetting-prone.

- **Problem**: Teams adopt SAM2 as their single model for images and video, then adapt it on video data; if temporal adaptation damages the image pathway disproportionately, the consolidation strategy carries a hidden tax nobody has priced.
- **Core hypothesis**: In SAM2, image-mode behavior shares parameters with temporally-conditioned computation, so video-domain gradients perturb static-mode functions in ways image-domain gradients (in SAM1 adaptation) do not, yielding faster degradation of image-mode metrics per unit of target-domain gain.
- **Falsifiable prediction**: Matching target-domain improvement between (a) SAM2 video-adapted and (b) SAM1 image-adapted on frames of the same domain, arm (a) shows larger drops on a fixed image-mode retention battery (natural-image click IoU, multimask diversity), consistently across domains and budgets.
- **Why important**: It quantifies the cost of unified image-video models under adaptation, informing whether organizations should maintain separate adapted models per modality, and probes how multi-task architectures distribute adaptation damage.
- **Why possibly novel**: HYPOTHESIS: forgetting under video fine-tuning, normalized per unit target gain and compared across architecture generations, appears unstudied.
- **Community default belief (what is treated as true)**: PEFT is gentle enough that adapting the unified model on video leaves image mode essentially intact.
- **Why that might be wrong**: Temporal objectives reward temporal smoothing of features; smoothed features are exactly what fine image-mode boundary detail does not want, creating directed interference rather than random drift.
- **Minimal falsification experiment**: Two domains with paired video and frame datasets; adapt SAM2 on video, SAM1 on frames, to matched target gains; run image-mode retention battery; falsified if retention losses are comparable.
- **Fastest falsification experiment**: One day: video-adapt SAM2 on one domain briefly, run the image-mode retention battery before and after, compare to a SAM1 control.
- **Main risk**: Matching target gains across different architectures and tasks is methodologically delicate; multiple matching criteria should be reported.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: SAM 2 shares its encoder across image and video modes per the paper; the differential-forgetting claim is MODEL SPECULATION

## Cluster: `data_priors_sa1b` (8 ideas)

### W13-P1-A-058 — Model-in-the-loop data generation gave SAM a mask-style monoculture: SA-1B's semi-automatic pipeline filtered out messy, low-compactness masks, so SAM inherits a compactness prior that is a data-flywheel artifact, not a property of the visual world.

- **Problem**: SAM's systematic preference for smooth closed regions is treated as a neutral architectural bias, but if it was manufactured by the data engine's own filtering (stability thresholds, model-assisted annotation), then every model trained on SAM outputs compounds the artifact, and the community cannot see it because the benchmark masks share the same lineage.
- **Core hypothesis**: The distribution of mask complexity (boundary fractal dimension, concavity counts) in SA-1B is significantly narrower than in fully-manual datasets of comparable content, and SAM's error rate grows with a target mask's distance from the SA-1B complexity mode faster than content difficulty explains.
- **Falsifiable prediction**: Comparing complexity distributions of SA-1B against manual datasets shows compression around a compact-mask mode; SAM performance stratified by target complexity shows a decline aligned with SA-1B density rather than with human difficulty ratings of the same instances.
- **Why important**: It would document a concrete case of dataset-flywheel bias in a flagship foundation model, with a measurable signature and a clear warning for all model-assisted annotation pipelines now proliferating.
- **Why possibly novel**: HYPOTHESIS: model-in-the-loop bias is discussed abstractly; a quantitative complexity-distribution audit of SA-1B linked to SAM's error profile appears undone.
- **Community default belief (what is treated as true)**: SA-1B's scale and diversity make it a faithful sample of segmentable structure in natural images.
- **Why that might be wrong**: Its pipeline retained masks the model-in-the-loop was confident about and stable on, which mathematically skews the retained distribution toward what early models found easy: compact, smooth regions.
- **Minimal falsification experiment**: Compute complexity statistics for large samples of SA-1B and manual datasets; stratify SAM errors by complexity controlling for human-rated difficulty on a 500-instance subset; falsified if distributions match or errors track difficulty, not complexity-density.
- **Fastest falsification experiment**: Hours: complexity histograms of 100k SA-1B masks vs a manual dataset; visible mode compression is the first checkpoint.
- **Main risk**: Content differences between datasets confound complexity comparisons; matched-content subsets are needed.
- **Evidence labels**: community_default_belief: EVIDENCE (common framing); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B was collected with a model-assisted, staged data engine per the SAM paper; the monoculture claim is MODEL SPECULATION

### W13-P1-A-059 — SAM carries a photographic-composition prior: mask quality for identical content varies with its position in the frame (center and rule-of-thirds hotspots), an artifact of professional photography in SA-1B that surveillance and industrial imagery violates wholesale.

- **Problem**: Spatial performance heterogeneity within the frame is invisible to standard metrics, yet fixed-camera applications (inspection, retail, security) place objects anywhere, so a composition prior would translate directly into location-dependent reliability that nobody specifies.
- **Core hypothesis**: Because professional photos concentrate subjects at compositional hotspots, SAM's per-location accuracy map (same object pasted at controlled positions) is non-uniform with peaks at center and thirds intersections, and the non-uniformity shrinks in models trained on uncurated data.
- **Falsifiable prediction**: Paste-controlled experiments show accuracy varying by position with a pattern matching photographic composition statistics, and the pattern persists across object categories and scales, while a supervised baseline trained on uniform-position data shows a flatter map.
- **Why important**: Position-dependent reliability is a deployment hazard with a simple audit and mitigation (position augmentation in PEFT), and the finding would add spatial composition to the catalogue of dataset biases foundation models absorb.
- **Why possibly novel**: HYPOTHESIS: center bias is known for saliency models; a quantitative positional accuracy map for promptable segmentation traced to photographic composition appears new.
- **Community default belief (what is treated as true)**: SAM segments an object equally well wherever it appears in the frame; translation invariance is approximately assumed.
- **Why that might be wrong**: ViTs have absolute positional embeddings and the training data had strongly non-uniform object-position statistics; nothing enforces translation invariance, and the two factors compound.
- **Minimal falsification experiment**: Composite 50 objects at a 5x5 position grid over diverse backgrounds, prompt identically, build the positional accuracy map; falsified if flat within noise.
- **Fastest falsification experiment**: Hours: one object, 25 positions, three backgrounds; a visible center-vs-corner gap is the first signal.
- **Main risk**: Compositing artifacts may interact with position; real translated-crop protocols should corroborate.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit invariance assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: ViTs use positional embeddings; SA-1B is professional licensed photography per the SAM paper

### W13-P1-A-060 — Class-agnostic training left latent semantics in SAM: its masks snap to semantic category boundaries even when low-level evidence contradicts them, so SAM is a covert semantic segmenter whose hidden classes bias supposedly geometry-only outputs.

- **Problem**: SAM is used as a neutral geometric tool (e.g., in scientific imaging) on the premise that it has no category preferences; if hidden semantic attractors shape its boundaries, unbiasedness claims in downstream measurement pipelines are wrong in unquantified ways.
- **Core hypothesis**: Mask boundaries preferentially align with human category boundaries (person vs background, object vs shadow) even under adversarially-matched low-level contrast, because annotators segmented nameable things, injecting semantics into supposedly class-agnostic supervision.
- **Falsifiable prediction**: On stimuli where a low-level boundary (contrast edge) and a semantic boundary (category edge with matched local contrast) compete, SAM sides with the semantic boundary far above chance, and the effect strength correlates with category nameability ratings.
- **Why important**: It changes what SAM outputs mean for measurement applications and quantifies how much semantics leaks through class-agnostic annotation, a question relevant to every dataset built by asking humans to segment things.
- **Why possibly novel**: HYPOTHESIS: SAM's semantic awareness is informally noted; a controlled contrast-matched competition protocol quantifying covert semantics appears missing.
- **Community default belief (what is treated as true)**: SAM is class-agnostic; its groupings follow visual evidence, not object categories.
- **Why that might be wrong**: The training masks were drawn around nameable objects by humans; category structure is statistically embedded in the supervision even if labels were discarded.
- **Minimal falsification experiment**: Construct 200 competition stimuli with photometrically matched competing boundaries, run SAM, measure semantic-side rate; falsified if near chance.
- **Fastest falsification experiment**: Hours: 20 shadow-vs-object cases where the shadow edge has stronger contrast than the object edge; count which boundary SAM follows.
- **Main risk**: Perfect photometric matching is hard; matching must be verified with low-level baseline models siding at chance.
- **Evidence labels**: community_default_belief: EVIDENCE (paper framing of class-agnostic design); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B masks were created without category labels per the SAM paper; the covert-semantics claim is MODEL SPECULATION

### W13-P1-A-061 — SAM has a viewpoint prior from licensed photography: performance drops lawfully with deviation from eye-level, subject-facing viewpoints, making overhead, egocentric, and oblique-angle imagery systematically underserved for reasons unrelated to content.

- **Problem**: Drone, robot, bodycam, and ceiling-camera imagery are huge application areas; if their deficit is a viewpoint prior rather than content difficulty, then viewpoint-targeted augmentation or adaptation would be far cheaper than the domain-specific retraining currently prescribed.
- **Core hypothesis**: For matched scenes and objects, accuracy is a decreasing function of viewpoint distance from the photographic canon (elevation and tilt statistics of professional photos), and viewpoint explains a large share of the deficit currently attributed to domain gap in aerial and egocentric benchmarks.
- **Falsifiable prediction**: On multi-view captures of the same scenes (or synthetic renders sweeping camera elevation), frozen SAM accuracy declines monotonically with elevation deviation from eye level at matched object visibility, and reweighting evaluation of an aerial benchmark by viewpoint distance accounts for most of its measured domain gap.
- **Why important**: Correct causal attribution of the aerial and egocentric gap changes the fix (cheap viewpoint augmentation vs expensive domain pipelines) and adds viewpoint to the list of auditable foundation-model priors.
- **Why possibly novel**: HYPOTHESIS: domain gaps for aerial imagery are documented; decomposing them into viewpoint prior vs appearance content with same-scene multi-view controls appears new.
- **Community default belief (what is treated as true)**: Aerial and egocentric imagery are hard for SAM because their content (small objects, unusual textures) differs from web photos.
- **Why that might be wrong**: Content and viewpoint were never separated: SA-1B viewpoint statistics are extremely narrow, and priors over rare conditioning variables degrade even when local appearance is familiar.
- **Minimal falsification experiment**: Render or capture same-scene viewpoint sweeps, measure accuracy vs elevation at controlled visibility; falsified if the curve is flat and gaps only appear with content change.
- **Fastest falsification experiment**: Hours: one synthetic scene, seven camera elevations, identical objects; plot the accuracy-vs-elevation curve.
- **Main risk**: Visibility and occlusion patterns covary with viewpoint; controls must equalize the visible-region difficulty.
- **Evidence labels**: community_default_belief: EVIDENCE (common attribution in aerial-adaptation papers); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B consists of licensed photography per the SAM paper; viewpoint-statistics claim about the corpus is HYPOTHESIS pending measurement

### W13-P1-A-062 — SAM's part-vs-whole ambiguity resolution is anchored to SA-1B's mask-size distribution: when object-to-image size ratios leave the training regime, granularity choices become systematically biased (macro shots yield parts, distant shots yield groups) independent of prompt intent.

- **Problem**: Users at unusual magnifications (microscopy, macro photography, satellite) report SAM returning the wrong granularity; without knowing this is a lawful size-prior effect, they blame prompts or domain and reach for heavy adaptation.
- **Core hypothesis**: The learned prior over selected-mask scale is anchored to the absolute mask-area distribution of SA-1B, so for images whose true-object area ratio is off-distribution, the top-ranked granularity shifts toward the prior mode, producing predictable part-selection at high magnification and group-selection at low magnification.
- **Falsifiable prediction**: Zoom sweeps of the same physical object show top-ranked mask granularity switching at area-ratio thresholds aligned with SA-1B mask-size distribution quantiles, and the switch points move consistently when re-ranking by a size-prior-corrected score.
- **Why important**: A quantitative size-prior law enables a zero-training fix (prior-corrected re-ranking) and explains a widespread cross-domain annoyance mechanistically.
- **Why possibly novel**: HYPOTHESIS: granularity instability is anecdotal; tying switch points to training-distribution quantiles and correcting by re-ranking appears new.
- **Community default belief (what is treated as true)**: Granularity selection reflects image ambiguity and prompt placement; magnification per se is not a systematic factor.
- **Why that might be wrong**: Ranking heads regress toward training-frequency priors when the likelihood is flat; off-distribution magnifications flatten the likelihood exactly where the prior then dominates.
- **Minimal falsification experiment**: Zoom-sweep protocol on 50 objects, log top-ranked mask area ratios, compare switch points to SA-1B quantiles, test the corrected re-ranker; falsified if switches are content-driven and uncorrectable by prior adjustment.
- **Fastest falsification experiment**: Hours: 10 objects, five zoom levels each, tally granularity of top-ranked masks vs zoom.
- **Main risk**: SA-1B statistics are known, but establishing prompt-intent ground truth for granularity requires careful task design.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B mask statistics are published with the dataset; the anchoring claim is MODEL SPECULATION

### W13-P1-A-063 — Guideline archaeology: SAM's handling of pathological cases (wires, fences, reflections, transparent objects) encodes recoverable traces of SA-1B annotation-guideline decisions, showing that foundation models memorize policy, not just imagery.

- **Problem**: When SAM behaves oddly on hard structure classes, users cannot tell whether behavior reflects visual evidence or a frozen annotation-policy choice (e.g., whether annotators included holes in fences); the distinction determines whether adaptation or post-processing is the right fix.
- **Core hypothesis**: For structure classes where annotation guidelines forced a convention, SAM's outputs are more consistent (lower cross-image entropy of topological choices) than for classes where guidelines were silent, revealing policy memorization distinguishable from evidence-driven behavior.
- **Falsifiable prediction**: Behavioral consistency scores across structure classes are bimodal: convention-governed classes (fence holes, wire inclusion) show high consistency even across contradictory visual evidence, while guideline-silent classes show evidence-dependent variability; the partition predicts which behaviors PEFT can easily flip (policies flip fast, evidence integration does not).
- **Why important**: Separating policy memory from perceptual competence in foundation models is a general interpretability question, and the flip-rate prediction has direct adaptation-cost implications.
- **Why possibly novel**: HYPOTHESIS: dataset-bias analyses exist, but reading annotation policy back out of a model's behavioral consistency, with a differential-adaptability prediction, appears new.
- **Community default belief (what is treated as true)**: SAM's outputs reflect learned visual structure; annotation-protocol details wash out at a billion-mask scale.
- **Why that might be wrong**: Policies apply systematically across millions of masks (unlike noise, which averages out), so scale amplifies rather than washes out conventions.
- **Minimal falsification experiment**: Define 10 structure classes, collect 100 cases each, measure behavioral consistency and evidence-sensitivity, then fine-tune small adapters to flip each behavior and compare flip costs; falsified if consistency is uniform or flip costs do not track the partition.
- **Fastest falsification experiment**: Hours: fences and wires, 30 cases each, check whether hole-handling is rigidly consistent regardless of hole visibility.
- **Main risk**: Without access to the actual guidelines, the policy-vs-evidence partition must be inferred, weakening claims; partial guideline information from the SAM paper mitigates this only partly.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B annotation involved staged human and automated protocols per the SAM paper; specific guideline contents are not public, so policy inference is MODEL SPECULATION

### W13-P1-A-064 — The synthetic-data paradox for promptable models: PEFT on synthetic renders improves boundary accuracy in the real target domain while destroying ambiguity handling, because synthetic ground truth is unique by construction and unlearns the multimask prior.

- **Problem**: Synthetic data is the default remedy for label scarcity, evaluated on accuracy alone; if it silently removes a model's ability to represent ambiguity (which real scenes have and renders lack), models inherit an overconfident single-answer disposition invisible to standard metrics.
- **Core hypothesis**: Synthetic supervision with unique masks provides consistent gradient pressure against output diversity, so ambiguity capabilities degrade faster under synthetic PEFT than under real-data PEFT at matched accuracy gains, and reintroducing ambiguity into synthetic labels (multiple valid renders per prompt) prevents the damage.
- **Falsifiable prediction**: At matched target-domain accuracy improvements, synthetic-trained adapters show significantly larger drops in multimask diversity and oracle-vs-top1 gap on natural probe images than real-trained adapters, and the ambiguity-augmented synthetic arm patches the difference.
- **Why important**: It identifies a hidden cost of the field's favorite data substitute, with a concrete label-generation fix, and generalizes to any multi-hypothesis model trained on simulation.
- **Why possibly novel**: HYPOTHESIS: synthetic-to-real gaps are studied for accuracy; the ambiguity-erosion channel with an augmentation countermeasure appears new.
- **Community default belief (what is treated as true)**: Synthetic data is a cheap, safe substitute whose main issue is the appearance gap (sim-to-real), addressable by domain randomization.
- **Why that might be wrong**: Appearance is only one axis; label-distribution properties (uniqueness, boundary crispness) also differ and train the output head directly, an unmodeled channel of sim-to-real damage.
- **Minimal falsification experiment**: Three-arm PEFT (real, synthetic, ambiguity-augmented synthetic) matched on accuracy gain, ambiguity battery on held-out natural images; falsified if arms retain diversity equally.
- **Fastest falsification experiment**: One day: quick synthetic PEFT run, before-and-after multimask diversity on 100 natural images vs a real-data control arm.
- **Main risk**: Building ambiguity-augmented synthetic labels requires renderer control and a defensible sampling scheme over valid segmentations.
- **Evidence labels**: community_default_belief: EVIDENCE (synthetic-data practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-065 — SA-1B's grid-prompt generation left a periodic spatial fingerprint in SAM: averaged over many images, mask-probability and mask-seed statistics show energy at the generation grid frequency, an unnoticed artifact coupling dataset construction to model prior.

- **Problem**: If the model's spatial prior carries the data engine's prompt-grid periodicity, then object detection and counting pipelines built on everything-mode inherit spatially periodic sensitivity, and dataset-construction parameters leak into every downstream model in a way nobody audits.
- **Core hypothesis**: Masks in SA-1B's automatic stage were seeded from regular point grids, biasing the retained-mask spatial statistics; SAM internalized this as a weak periodic prior detectable by averaging click-response maps or everything-mode seed statistics over thousands of images in grid-aligned coordinates.
- **Falsifiable prediction**: The spatial spectrum of aggregate mask-initiation statistics shows peaks at the generation-grid frequency significantly above surrogate controls (phase-randomized aggregates), and the peaks weaken in models fine-tuned on manually-annotated data.
- **Why important**: Even a weak result establishes that dataset-generation hyperparameters imprint on foundation-model priors, motivating fingerprint audits of data engines now used everywhere (auto-labeling, model-in-the-loop pipelines).
- **Why possibly novel**: HYPOTHESIS: periodic artifacts are studied for generative upsamplers; a data-engine fingerprint analysis for a segmentation foundation model appears new.
- **Community default belief (what is treated as true)**: Dataset-construction machinery leaves no systematic trace in the trained model beyond content statistics.
- **Why that might be wrong**: The grid was applied identically to millions of images; identical systematic procedures are exactly what models can and do internalize, as positional biases in other models show.
- **Minimal falsification experiment**: Aggregate mask statistics over 10k images in normalized coordinates, spectral analysis against surrogate nulls; falsified if no grid-frequency structure exists.
- **Fastest falsification experiment**: One day: aggregate everything-mode seed positions over 2k images, Fourier transform of the density map, look for lattice peaks.
- **Main risk**: The effect, if present, is likely tiny and demands rigorous null models to avoid false positives; a null result has modest value.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B's fully-automatic stage used regular grid prompting per the SAM paper

## Cluster: `evaluation_methodology` (7 ideas)

### W13-P1-A-066 — Benchmark mIoU anti-correlates with interactive usability across PEFT methods: adapters that win static benchmarks require more correction clicks in deployment because they trade prompt responsiveness for prompt-independent priors.

- **Problem**: PEFT methods for SAM are ranked by single-shot mIoU with simulated prompts, but real usage is interactive; if the ranking inverts under clicks-to-quality metrics, the community is systematically selecting the wrong methods for deployment.
- **Core hypothesis**: Adaptation that maximizes single-shot accuracy does so partly by strengthening domain priors that override prompt details; such prior-heavy models respond weakly to corrective clicks, so single-shot accuracy and interactive efficiency are anti-correlated across adapted checkpoints within a domain.
- **Falsifiable prediction**: Across 10+ adapted checkpoints per domain (varying method and budget), the correlation between single-shot mIoU and clicks-to-90-percent-IoU is positive (worse) rather than negative, and prompt-ablation sensitivity mediates the relationship statistically.
- **Why important**: It would overturn the field's selection criterion for adaptation methods and introduce prompt responsiveness as a first-class evaluation axis for promptable models.
- **Why possibly novel**: HYPOTHESIS: interactive metrics exist in interactive-segmentation literature, but the claim that PEFT optimization inverts rankings between static and interactive axes, with a mediation analysis, appears new.
- **Community default belief (what is treated as true)**: Higher benchmark mIoU means a better adapted model, full stop; interactive quality follows from static quality.
- **Why that might be wrong**: Single-shot metrics reward models for ignoring prompt noise, which is behaviorally identical to ignoring prompts; the metric cannot distinguish confident competence from prompt deafness.
- **Minimal falsification experiment**: Train a grid of adapters on two domains, evaluate single-shot and simulated-interactive metrics plus prompt-ablation sensitivity, compute correlations and mediation; falsified if rankings agree across axes.
- **Fastest falsification experiment**: One day: two checkpoints with equal mIoU but different training (LoRA vs decoder-tune), compare clicks-to-quality curves; divergence at equal mIoU is the proof of concept.
- **Main risk**: Simulated clickers may not represent human correction behavior; a small human study would strengthen but also complicate the result.
- **Evidence labels**: community_default_belief: EVIDENCE (universal benchmarking practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-067 — Boundary metrics conflate constant offset with jitter: decomposing boundary error into bias and variance components changes which PEFT method wins, because methods differ in which component they fix.

- **Problem**: Boundary-F and HD95 summarize boundary error as a scalar, but a fixed 2-pixel dilation (correctable post hoc) and 2-pixel random jitter (a real quality problem) score identically, so method comparisons reward the wrong improvements.
- **Core hypothesis**: PEFT methods partition into offset-fixers (whose gains vanish after optimal per-method morphological correction) and jitter-fixers (whose gains survive), and published rankings mix the two, so re-ranking after bias correction reorders a substantial fraction of comparisons.
- **Falsifiable prediction**: Recomputing published-style comparisons with bias-corrected boundary metrics (subtract fitted constant offset before scoring) flips the winner in a meaningful fraction of method pairs, and the flip pattern is consistent across datasets.
- **Why important**: A metric decomposition that reorders leaderboards forces cleaner claims about what adaptation methods actually improve and gives practitioners a free post-processing win where offset dominates.
- **Why possibly novel**: HYPOTHESIS: bias-variance decompositions are standard elsewhere; applying them to segmentation boundary metrics to audit PEFT comparisons appears new.
- **Community default belief (what is treated as true)**: Boundary metrics measure boundary quality; a better score means better boundaries in every sense that matters.
- **Why that might be wrong**: Metrics integrate over error structure; two structurally different errors with equal integrals have very different practical costs and remediation, a distinction the community's tooling never surfaces.
- **Minimal falsification experiment**: Take five adapted checkpoints across methods on two datasets, fit per-model constant offsets, recompute metrics, count ranking flips; falsified if rankings are invariant.
- **Fastest falsification experiment**: Hours: one checkpoint pair, offset-corrected re-scoring; one flip suffices to demonstrate the phenomenon exists.
- **Main risk**: Optimal offset fitting must avoid overfitting to test data; proper train-test protocol for the correction is needed.
- **Evidence labels**: community_default_belief: EVIDENCE (metric conventions); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-068 — Oracle (best-of-3) evaluation inflates robustness claims by an amount that grows with domain shift, so the literature's picture of SAM's cross-domain competence is systematically rosier than any deployable configuration.

- **Problem**: Papers often report oracle-selected masks to isolate generation quality, but readers and downstream users interpret the numbers as achievable performance; if the oracle-deployed gap widens with shift (per the ranking-fragility hypothesis), the inflation is largest exactly where claims matter most.
- **Core hypothesis**: The oracle-vs-top1 gap is not a constant tax but an increasing function of domain shift, because ranking degrades faster than generation; consequently cross-domain comparisons under oracle protocols misestimate relative difficulty of domains and overstate zero-shot transfer.
- **Falsifiable prediction**: Across a shift ladder (in-distribution to far domains), the oracle-top1 gap grows monotonically, and domain-difficulty rankings under oracle vs deployed protocols disagree for a meaningful fraction of domain pairs.
- **Why important**: It quantifies a protocol-induced bias distorting the field's map of where SAM works, with immediate implications for how papers must report results.
- **Why possibly novel**: HYPOTHESIS: both protocols are used casually; the systematic shift-dependence of their divergence appears unmeasured.
- **Community default belief (what is treated as true)**: Oracle evaluation is a harmless idealization; it shifts all numbers up uniformly without distorting comparisons.
- **Why that might be wrong**: Uniform-shift assumptions require the selection mechanism to degrade in lockstep with generation, but the two are different subsystems with different training exposure (idea 026), so lockstep is the special case, not the default.
- **Minimal falsification experiment**: Evaluate frozen SAM under both protocols across six domains ordered by shift metrics, plot gap vs shift, test monotonicity; falsified if the gap is flat.
- **Fastest falsification experiment**: Hours: three domains spanning shift levels, both protocols, check gap ordering.
- **Main risk**: Defining a defensible one-dimensional shift ladder is contestable; multiple shift metrics should agree.
- **Evidence labels**: community_default_belief: EVIDENCE (reporting practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-069 — Centroid-click evaluation is a lucky-prompt protocol: model rankings among adapted SAMs invert under prompt distributions sampled from real user behavior, because centroid clicks are systematically easier than human clicks.

- **Problem**: Nearly all point-prompt evaluations click the object centroid or a maximally-interior point; humans click salient parts, high-contrast spots, or wherever the cursor lands first, so reported comparisons may not predict deployed rankings at all.
- **Core hypothesis**: Model robustness to prompt-placement variation differs across adaptation methods (some narrow the prompt basin, idea 005), so the ranking of methods under centroid protocol and under human-sampled prompt distributions diverges measurably, with prompt-basin width as the mediating variable.
- **Falsifiable prediction**: Collecting a modest set of real human click distributions (or using logged clicks from annotation tools) and re-evaluating a grid of adapted checkpoints flips method rankings in a meaningful fraction of comparisons relative to centroid protocol, and flip magnitude correlates with basin-width differences.
- **Why important**: Evaluation realism determines which research directions look promising; documenting ranking instability under realistic prompts would redirect method development toward robustness of the prompt map rather than peak performance at an idealized prompt.
- **Why possibly novel**: HYPOTHESIS: click-simulation policies are known to matter for training; their distorting effect on evaluation rankings of adapted models appears unquantified.
- **Community default belief (what is treated as true)**: Centroid or max-interior clicks are a fair, neutral standard for comparing point-prompt segmentation.
- **Why that might be wrong**: Centroid clicks maximize distance from boundary ambiguity, sampling only the easiest point of each object's prompt space; a protocol that samples one extreme cannot certify orderings over the whole space.
- **Minimal falsification experiment**: Gather human click data on 300 objects (small user study or public annotation logs), evaluate six checkpoints under both prompt distributions, compare rankings; falsified if rankings are stable.
- **Fastest falsification experiment**: Hours: 30 objects with 5 self-collected human clicks each, evaluate two checkpoints under both protocols; a ranking flip at small scale motivates the full study.
- **Main risk**: Human click collection introduces its own biases (task instructions matter); multiple instruction conditions strengthen validity.
- **Evidence labels**: community_default_belief: EVIDENCE (protocol conventions); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-070 — Zero-shot claims for SAM on web-sourced benchmarks are partially memorization: near-duplicate overlap between SA-1B and popular evaluation sets inflates zero-shot numbers by a measurable margin revealed through deduplicated re-evaluation.

- **Problem**: SA-1B's 11 million images were sampled from the same visual web ecosystem many benchmarks draw from; without a published overlap audit, zero-shot generalization and memorized-familiarity are indistinguishable in reported numbers.
- **Core hypothesis**: Near-duplicate and same-scene overlap between SA-1B and common evaluation sets is nonzero, and SAM's performance on overlapping items exceeds matched non-overlapping items by a margin too large to attribute to content difficulty, quantifying a memorization component in zero-shot claims.
- **Falsifiable prediction**: An embedding-based near-duplicate audit finds a measurable overlap fraction, and the per-item performance gap between overlap and matched-control items is significantly positive; removing overlap items shifts headline zero-shot numbers detectably on at least one benchmark.
- **Why important**: Contamination auditing became standard for LLM benchmarks; establishing the practice (and the magnitude) for segmentation foundation models protects the validity of the field's central generalization claims.
- **Why possibly novel**: HYPOTHESIS: contamination is heavily studied for language models; a rigorous SA-1B-vs-benchmarks audit appears absent, possibly because mask-level supervision made people assume it does not matter.
- **Community default belief (what is treated as true)**: SAM's evaluations are genuinely zero-shot; image-level contamination is a language-model problem, not a concern for segmentation with held-out datasets.
- **Why that might be wrong**: Web-scale corpora sample the same photogenic scenes and stock imagery benchmarks were built from; overlap is the default expectation at scale, not the exception, until audited.
- **Minimal falsification experiment**: Run near-duplicate detection between SA-1B and three benchmarks, form matched pairs, compare performance; falsified if overlap is negligible or the performance gap is zero.
- **Fastest falsification experiment**: One day: embed one benchmark and a few million SA-1B images (subsample) with an off-the-shelf encoder, count high-similarity pairs; a nonzero hit rate justifies the full audit.
- **Main risk**: SA-1B is large to process, and matched-control construction (difficulty matching) is the methodological crux; a null result is still publishable as an audit but less impactful.
- **Evidence labels**: community_default_belief: EVIDENCE (reporting practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SA-1B contains 11M images and 1.1B masks per the SAM paper; overlap magnitude is HYPOTHESIS pending measurement

### W13-P1-A-071 — SAM's failures are bimodal (near-perfect or catastrophic), so mean metrics track the mixture weight rather than segmentation quality, and PEFT methods should be compared by failure-rate curves instead of averages.

- **Problem**: Two adapted models with equal mean IoU can be operationally opposite (one uniformly mediocre, one mostly perfect with rare disasters); safety-critical users need the distinction, but the literature reports means almost exclusively.
- **Core hypothesis**: Per-instance IoU distributions for frozen and adapted SAM are strongly bimodal across domains, adaptation methods differ primarily in how they move mass between modes (not in shifting the good mode), and mean-based rankings therefore disagree with risk-based rankings (e.g., probability of IoU below 0.5) in a predictable fraction of comparisons.
- **Falsifiable prediction**: Bimodality coefficients of per-instance IoU distributions are high across settings, method rankings under mean-IoU vs failure-rate metrics disagree substantially, and the good-mode location is nearly invariant across methods while mixture weights vary.
- **Why important**: It changes what adaptation research optimizes (mode transport, not average lift) and equips deployment decisions with the risk-relevant statistic means cannot supply.
- **Why possibly novel**: HYPOTHESIS: per-instance variability is occasionally shown; the mixture-model account of adaptation effects and the ranking-disagreement quantification appear new.
- **Community default belief (what is treated as true)**: Mean IoU differences reflect quality differences; distributional details are second-order refinements.
- **Why that might be wrong**: Promptable segmentation succeeds or fails at the object level (found it or grabbed the wrong thing); such all-or-nothing mechanics generate mixtures, and means over mixtures are known to mislead.
- **Minimal falsification experiment**: Collect per-instance IoU for a method grid on three domains, fit two-component mixtures, test mode invariance and ranking disagreement; falsified if distributions are unimodal or rankings agree.
- **Fastest falsification experiment**: Hours: histogram per-instance IoU for frozen SAM on one shifted dataset; visible bimodality is the entry ticket for the full study.
- **Main risk**: Bimodality may itself be an artifact of dataset heterogeneity (easy and hard subpopulations), requiring stratified analysis to locate its source.
- **Evidence labels**: community_default_belief: EVIDENCE (reporting practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-072 — Cross-paper PEFT-for-SAM comparisons are confounded by prompt-simulation policy more than by method: a controlled re-implementation shows the prompt protocol explains more ranking variance than the adaptation technique being advertised.

- **Problem**: Every adaptation paper picks its own prompt simulation (box jitter levels, click counts, click placement rules), making the literature an uncontrolled meta-experiment where methods and protocols vary together; the field may be accumulating conclusions about protocols while believing they are about methods.
- **Core hypothesis**: Re-running representative PEFT methods under a crossed design (methods x prompt protocols) shows protocol main effects and method-protocol interactions comparable to or exceeding method main effects for common metric differences reported between consecutive papers.
- **Falsifiable prediction**: Variance decomposition over the crossed grid attributes a share of ranking variance to protocol at least as large as to method, and at least one widely-cited ordering between two methods reverses under a different (equally defensible) protocol.
- **Why important**: A demonstrated protocol confound would justify a community-standard prompt-simulation specification, improving the signal value of all future comparisons.
- **Why possibly novel**: HYPOTHESIS: protocol sensitivity is suspected informally; a quantitative variance decomposition across methods and protocols for SAM adaptation appears undone.
- **Community default belief (what is treated as true)**: Published comparisons transfer: if method A beat method B in its paper, A is the better technique for that domain.
- **Why that might be wrong**: Prompt simulation determines task difficulty and the information the model receives; small protocol choices plausibly dwarf few-point method margins, but nobody has measured the ratio.
- **Minimal falsification experiment**: Implement four methods and four protocols on two domains with fixed seeds, run the full cross, decompose variance; falsified if method effects dominate cleanly.
- **Fastest falsification experiment**: One day: two methods, two protocols, one domain; an observed interaction larger than the method margin already makes the point.
- **Main risk**: Faithful re-implementation of published methods is laborious and disputable; using released checkpoints where available mitigates.
- **Evidence labels**: community_default_belief: EVIDENCE (citation practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

## Cluster: `robustness_adversarial` (7 ideas)

### W13-P1-A-073 — Corruption robustness of SAM is prompt-type dependent in a structured way (boxes resist blur, points resist occlusion, and vice versa fails), so prompt choice is a free robustness lever no pipeline currently exploits.

- **Problem**: Robustness studies evaluate one prompt type or average over them, missing the interaction; if different prompts fail under different corruptions, deployed systems could switch prompt strategies by condition monitoring at zero model cost.
- **Core hypothesis**: Prompt types inject different information (boxes give scale and extent priors robust to high-frequency loss; points rely on local features robust to geometric occlusion but fragile to blur), producing a structured corruption-by-prompt interaction matrix that is stable across datasets.
- **Falsifiable prediction**: A full corruption-battery-by-prompt-type evaluation yields a significant, reproducible interaction (not just main effects), and a condition-aware prompt-selection policy derived from the matrix beats any fixed prompt type on mixed-corruption streams.
- **Why important**: A validated interaction matrix converts robustness knowledge into an actionable inference-time policy and clarifies mechanistically what each prompt type contributes to the decoder's evidence integration.
- **Why possibly novel**: HYPOTHESIS: corruption benchmarks for SAM exist; the prompt-type interaction structure and the derived switching policy appear unexplored.
- **Community default belief (what is treated as true)**: Robustness is a property of the model; prompts affect accuracy but corruption sensitivity is prompt-independent.
- **Why that might be wrong**: Prompts determine which image evidence the decoder weights; corruptions destroy specific evidence types; the intersection is mechanically prompt-dependent, yet evaluations average over precisely this structure.
- **Minimal falsification experiment**: Fifteen corruptions x three prompt types x two datasets with matched instances, test interaction significance and policy gains; falsified if effects are additive.
- **Fastest falsification experiment**: Hours: blur and occlusion x points and boxes on 100 instances; a crossed pattern in the 2x2 is the proof of concept.
- **Main risk**: Interaction may exist but be too weak for a policy to beat the best fixed prompt type.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit in evaluation design); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-074 — Universal adversarial prompt perturbations exist: a single learned pixel-offset field applied to any user click (imperceptible at UI level) collapses SAM's masks across images, exposing prompt space as an unsecured attack surface cheaper than image attacks.

- **Problem**: Adversarial work on SAM attacks the image; but in deployed annotation platforms and agent pipelines the prompt channel (coordinates passed through software layers) is equally attackable and completely unstudied as a threat model, despite being lower-bandwidth and easier to manipulate covertly.
- **Core hypothesis**: Because the click-to-mask map is locally non-smooth (idea 009) with structured failure sets (idea 006), there exist image-agnostic offset fields (a few pixels, spatially varying) that transport clicks into failure regions at high rates, learnable from a modest image corpus and transferable across SAM variants.
- **Falsifiable prediction**: An offset field with max norm under 5 pixels, optimized on 1000 images, reduces mean IoU on held-out images by a large factor, transfers across SAM-B/L/H and distilled variants above chance, and defeats naive defenses (click averaging) unless they are prompt-smoothing aware.
- **Why important**: It defines a new attack surface for promptable models with realistic deployment relevance (annotation-supply-chain integrity, agent pipelines) and motivates certified smoothness of prompt maps as a defense objective.
- **Why possibly novel**: HYPOTHESIS: image-space attacks on SAM exist in the literature; universal prompt-coordinate-space attacks appear unstudied.
- **Community default belief (what is treated as true)**: Adversarial risk for segmentation lives in the image; a few pixels of click displacement is harmless noise the model tolerates.
- **Why that might be wrong**: Tolerance to random jitter says nothing about worst-case jitter; the existence of structured failure sets makes worst-case displacement qualitatively different from random displacement.
- **Minimal falsification experiment**: Optimize the offset field on a training corpus, evaluate on held-out images and across model variants against jitter baselines; falsified if learned fields do no better than random jitter of the same magnitude.
- **Fastest falsification experiment**: One day: optimize per-image worst-case 3-pixel offsets first (upper bound); if even per-image worst-case barely hurts, the universal version is dead on arrival.
- **Main risk**: If the click-to-mask map is smoother than hypothesized, only large (perceptible) offsets work, deflating the threat model.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION; existence of image-space SAM attacks is plausible prior work but specific papers are not cited to avoid unverified attribution

### W13-P1-A-075 — PEFT concentrates adversarial vulnerability: LoRA-adapted SAM is easier to attack than either frozen SAM or fully fine-tuned SAM, because low-rank updates create a small, findable subspace whose manipulation controls the whole adapted behavior.

- **Problem**: Security evaluations certify base models, and practitioners assume small parameter deltas mean small behavioral attack-surface changes; if adaptation concentrates sensitivity into a low-dimensional subspace, every adapted deployment is quietly weaker than its certified base.
- **Core hypothesis**: Adversarial examples against LoRA-adapted models succeed at lower perturbation budgets than against frozen or fully-tuned models at matched clean accuracy, and attack gradients align measurably with the LoRA subspace, establishing concentration (not just shift) of vulnerability.
- **Falsifiable prediction**: Attack success at fixed epsilon is ordered LoRA-adapted above fully-tuned above frozen at matched clean accuracy on the target domain, and projecting attack perturbation gradients onto the LoRA update subspace shows disproportionate alignment relative to random subspaces of equal dimension.
- **Why important**: It connects the geometry of adaptation to security, implying rank and placement choices are security parameters, and would motivate adversarial-aware PEFT regularizers.
- **Why possibly novel**: HYPOTHESIS: robustness of fine-tuned vs frozen models is studied for classification; subspace-concentration analysis of vulnerability for segmentation PEFT appears new.
- **Community default belief (what is treated as true)**: PEFT's small parameter change implies approximately the base model's robustness profile.
- **Why that might be wrong**: Low-rank adaptation creates a few high-leverage directions trained on little data without adversarial pressure; attackers optimize exactly for high-leverage directions.
- **Minimal falsification experiment**: Three matched checkpoints (frozen, LoRA, full FT) on one domain, standardized attacks at several budgets plus gradient-subspace alignment analysis; falsified if orderings reverse or alignment is absent.
- **Fastest falsification experiment**: One day: PGD at two budgets against frozen vs one public LoRA-adapted checkpoint on the adapted domain; a large success-rate gap is the first evidence.
- **Main risk**: Matching clean accuracy across the three regimes is nontrivial and drives the comparison's fairness.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-076 — SAM's low-contrast failures are threshold failures, not perception failures: under fog or dim light the logit landscape preserves the object (rank order intact) but the fixed binarization threshold misplaces the boundary, so an input-conditional threshold fixes fog for free.

- **Problem**: Degraded-visibility performance drives expensive enhancement preprocessing and domain adaptation, all premised on features failing; if the failure is in the final thresholding step, the community is repairing the wrong stage of the pipeline.
- **Core hypothesis**: Global contrast reduction compresses mask logits toward the threshold without destroying their spatial ordering, so oracle-threshold masks (choosing the best cutoff per image) recover most of the clean-condition accuracy, and a lightweight contrast-conditioned threshold predictor captures most of the oracle gain.
- **Falsifiable prediction**: On synthetic and real low-contrast sets, the gap between fixed-threshold and oracle-threshold performance accounts for the majority of the degradation, whereas under structural corruptions (occlusion, noise) the oracle threshold recovers little, confirming specificity.
- **Why important**: A one-parameter inference-time fix for a whole corruption family would be immediately deployable, and the logit-preservation finding would sharpen understanding of where robustness actually breaks in dense predictors.
- **Why possibly novel**: HYPOTHESIS: adaptive thresholding is an old image-processing idea; demonstrating that a foundation segmenter's weather fragility is largely a thresholding artifact appears new.
- **Community default belief (what is treated as true)**: Weather robustness requires robust features via augmentation, enhancement front-ends, or adaptation; the output stage is not the problem.
- **Why that might be wrong**: The binarization constant was calibrated on clean-image logit statistics; global input compression predictably shifts logit scale, a trivial mechanism hiding inside an impressive-looking failure.
- **Minimal falsification experiment**: Contrast-degradation ladder on two datasets, compare fixed vs oracle vs predicted thresholds, plus structural-corruption controls; falsified if oracle thresholding recovers little under low contrast.
- **Fastest falsification experiment**: Hours: 50 images, four synthetic contrast levels, fixed vs per-image best threshold; the recovered fraction answers the core question immediately.
- **Main risk**: Real fog involves scattering structure beyond global contrast; synthetic-to-real gap in the corruption model could limit the fix.
- **Evidence labels**: community_default_belief: EVIDENCE (robustness literature practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM thresholds mask logits at a fixed value in the released implementation

### W13-P1-A-077 — Geometry-only prompting makes SAM structurally immune to typographic and semantic-patch attacks that fool text-conditioned segmenters, a security advantage of coordinate interfaces that quantifies the robustness cost of language conditioning.

- **Problem**: The field is racing to add text conditioning to segmentation (open-vocabulary models), implicitly assuming language grounding is a free capability upgrade; its adversarial cost relative to coordinate prompting has never been isolated with matched-architecture comparisons.
- **Core hypothesis**: Attacks that exploit the language-vision binding (printed words, semantically suggestive patches) transfer to text-conditioned segmenters but not to coordinate-prompted SAM on the same images, and the robustness gap persists after both models are adapted to the same domain, establishing an interface-inherent (not training-data) effect.
- **Falsifiable prediction**: On a battery of typographic and semantic-patch manipulations, text-conditioned segmentation degrades severely while point- and box-prompted SAM on identical targets degrades marginally, and hybrid models (text plus geometry) degrade in proportion to their measured reliance on the text pathway.
- **Why important**: It provides a quantified security argument in the interface-design debate for promptable vision, relevant to safety-critical procurement decisions between text-driven and geometry-driven tools.
- **Why possibly novel**: HYPOTHESIS: typographic attacks on CLIP are established (Goh et al. documented typographic attacks on CLIP-like models); a controlled interface-level comparison for segmentation appears new.
- **Community default belief (what is treated as true)**: Text conditioning adds capability without a distinct robustness cost; attacks are a model-quality issue, not an interface issue.
- **Why that might be wrong**: The attack surface is the conditioning channel itself: coordinates cannot be spoofed by scene content, text bindings can; this is an architectural distinction, not a training deficiency.
- **Minimal falsification experiment**: Build 200 typographic and patch-attack scenes with clear target ground truth, evaluate a text-conditioned segmenter and SAM with matched prompting effort; falsified if SAM degrades comparably.
- **Fastest falsification experiment**: Hours: 20 scenes with printed misleading labels on objects, compare a public text-prompted segmenter vs SAM box prompts.
- **Main risk**: Matched-effort prompting across interfaces is hard to define fairly; multiple prompting budgets should be reported.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: typographic attacks on CLIP were documented (OpenAI multimodal neurons work); segmentation-interface comparison is MODEL SPECULATION

### W13-P1-A-078 — SAM's transferability to a new domain is predicted by that domain's mid-frequency spectral content: band-pass ablation shows SAM relies on a specific spatial-frequency band, and domains missing it (ultrasound speckle, low-detail thermal) fail regardless of semantic simplicity.

- **Problem**: Domain difficulty for SAM is discussed in semantic terms (unfamiliar objects) while a simpler physical account (missing spatial-frequency support the model depends on) has not been tested, though it would yield a five-minute transferability screening.
- **Core hypothesis**: SAM's grouping decisions depend disproportionately on a mid-frequency band (measurable by band-stop performance ablation on natural images), and zero-shot performance across domains correlates strongly with target-domain energy in that band, better than with semantic-distance measures.
- **Falsifiable prediction**: Band-stop filtering of specific frequencies degrades SAM on natural images far more than equal-energy removal elsewhere; across 10 domains, band-energy overlap predicts zero-shot rank order with high correlation, beating an embedding-distance baseline.
- **Why important**: A physical, computable predictor of transfer beats vague domain-gap talk, guides preprocessing (frequency reshaping as cheap adaptation), and characterizes what evidence SAM's grouping actually uses.
- **Why possibly novel**: HYPOTHESIS: frequency analyses exist for classifiers; a frequency-reliance profile for promptable segmentation used as a transfer predictor appears new.
- **Community default belief (what is treated as true)**: Domain difficulty is about semantic and textural unfamiliarity; spectral composition is a low-level detail models of this scale abstract away.
- **Why that might be wrong**: Boundary evidence is physically carried by specific frequency bands; a model optimized for boundary acuity plausibly specialized to the bands where its training data carried boundary information.
- **Minimal falsification experiment**: Frequency-ablation battery on natural images to map reliance; correlate domain band-energy with zero-shot scores across a domain suite; falsified if reliance is flat or correlation is weak.
- **Fastest falsification experiment**: Hours: three band-stop conditions on 100 natural images; a sharp reliance peak is the entry result.
- **Main risk**: Frequency reliance may be resolution-confounded (idea 010); analyses must normalize object scale.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-079 — SAM flips inconsistently between modal (visible-region) and amodal (completed-object) segmentation depending on prompt position relative to an occluder, an unacknowledged mode ambiguity that makes its outputs unreliable as either kind of ground truth.

- **Problem**: Pipelines assume SAM outputs visible-region masks; occasionally it completes objects behind occluders, and when it does is undocumented, contaminating datasets built with SAM assistance with an unlabeled mixture of modal and amodal masks.
- **Core hypothesis**: The modal-amodal choice is governed lawfully by prompt geometry (distance from the occlusion boundary, prompted side) and occluder characteristics (thin occluders trigger completion, thick ones do not), reflecting mixed conventions in SA-1B annotation rather than randomness.
- **Falsifiable prediction**: On a controlled occlusion battery, the completion rate varies systematically with occluder width and prompt-to-occluder distance, is stable across images with matched geometry, and matches the mixture one would predict from plausible annotation conventions (wires and poles completed, walls not).
- **Why important**: Whoever documents the mode-selection law can both audit existing SAM-derived datasets for mixture contamination and give practitioners a control knob (prompt placement) for selecting the intended mode.
- **Why possibly novel**: HYPOTHESIS: amodal segmentation is its own subfield, but SAM's implicit mode-mixing law and its dataset-contamination consequence appear undescribed.
- **Community default belief (what is treated as true)**: SAM segments visible regions; amodal completion is out of scope and does not occur.
- **Why that might be wrong**: SA-1B annotators inevitably handled thin-occluder cases inconsistently (annotating the whole road sign behind a wire), so the model learned a context-dependent mixture, not a single convention.
- **Minimal falsification experiment**: Build 300 occlusion scenes parameterized by occluder width and prompt placement, measure completion rates, fit the geometric law; falsified if completion is rare or unpredictable.
- **Fastest falsification experiment**: Hours: 20 scenes with a thin pole crossing objects, click both sides at varying distances, tally completion behavior.
- **Main risk**: Ground truth for intended mode is a convention choice; the study must report both modal and amodal scoring throughout.
- **Evidence labels**: community_default_belief: EVIDENCE (common assumption in pipeline design); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

## Cluster: `distillation_efficiency` (6 ideas)

### W13-P1-A-080 — Distillation kills ambiguity first: efficient SAM students match teacher mIoU while losing most of the teacher's hypothesis-space structure (multimask diversity, granularity control), because distillation targets the argmax mask, not the distribution over valid masks.

- **Problem**: Efficient SAM variants are certified by accuracy parity, and the community concludes they are drop-in replacements; if the compressed models have silently lost the ability to represent alternative segmentations, interactive and ambiguity-dependent applications inherit an untracked regression.
- **Core hypothesis**: Standard distillation objectives (matching final masks or single embeddings) provide no gradient signal for hypothesis diversity, so student models exhibit collapsed multimask outputs and weakened prompt-granularity response even when their top-mask accuracy matches the teacher.
- **Falsifiable prediction**: Across public efficient variants (MobileSAM-class, FastSAM-class, EfficientSAM-class), an ambiguity battery (inter-mask diversity, granularity switching under prompt sweeps, oracle-vs-top1 gap) shows large losses relative to teachers despite near-parity mIoU, with loss magnitude ordered by how output-centric each distillation objective was.
- **Why important**: It exposes a blind spot in how model compression is certified, defines the missing evaluation, and motivates diversity-preserving distillation objectives for any multi-hypothesis model.
- **Why possibly novel**: HYPOTHESIS: efficient SAM papers report accuracy and speed; a systematic ambiguity audit across the efficiency family appears missing.
- **Community default belief (what is treated as true)**: Efficient SAM variants are functionally equivalent, cheaper SAMs; accuracy parity certifies equivalence.
- **Why that might be wrong**: Equivalence was only ever measured on the axis distillation optimized; unmeasured capabilities have no reason to survive compression, and ambiguity is exactly the unmeasured axis.
- **Minimal falsification experiment**: Run the ambiguity battery on three efficient variants and their teachers over 500 images; falsified if students preserve ambiguity structure at accuracy parity.
- **Fastest falsification experiment**: Hours: one efficient variant vs teacher, inter-mask diversity and a 10-object granularity sweep; a visible collapse settles the existence question.
- **Main risk**: Some efficient variants changed architecture (single-mask heads) making the comparison partly definitional; the audit must separate architectural removal from distillation-induced collapse.
- **Evidence labels**: community_default_belief: EVIDENCE (release framing of efficient variants); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: MobileSAM, FastSAM, and EfficientSAM exist as efficient SAM-family models; the ambiguity-loss claim is MODEL SPECULATION

### W13-P1-A-081 — Distilled students fail on a strict superset of teacher failures: compression does not trade failure regions but nests them, so teacher-side failure prediction transfers to students for free, enabling cheap cascade designs.

- **Problem**: Cascade systems (cheap student first, expensive teacher fallback) need to know whether student failures are predictable from teacher behavior; if failure sets are nested rather than disjoint, fallback logic and audit tooling simplify dramatically, but nobody has tested the set relationship.
- **Core hypothesis**: Because students are optimized to imitate teachers (not to solve the task independently), student competence is approximately teacher competence intersected with capacity constraints, predicting per-instance failure containment: cases the teacher fails, the student fails too, plus additional capacity-driven failures.
- **Falsifiable prediction**: Per-instance evaluation of teacher-student pairs shows the student succeeding where the teacher fails at rates far below what independent errors at matched marginal accuracy would predict (containment violation rate close to noise), consistently across distilled variants but not across independently-trained model pairs.
- **Why important**: Containment (or its refutation) determines correct cascade and ensemble design for the SAM family, and it tests a basic proposition about what imitation learning can and cannot add.
- **Why possibly novel**: HYPOTHESIS: teacher-student agreement is studied via aggregate fidelity; the set-relationship (containment) framing with cascade implications appears new for segmentation.
- **Community default belief (what is treated as true)**: Students trade accuracy for speed diffusely; where they fail relative to the teacher is idiosyncratic.
- **Why that might be wrong**: Imitation objectives upper-bound student knowledge by teacher outputs on the training distribution; novel student successes would require information the training signal never carried, making containment the structural default.
- **Minimal falsification experiment**: Per-instance success matrices for three teacher-student pairs plus an independently-trained control pair on 2000 instances; falsified if students beat teachers on a substantial instance fraction.
- **Fastest falsification experiment**: Hours: one pair, 300 instances, count student-succeeds-teacher-fails cases against the independence baseline.
- **Main risk**: Instance-level success requires choosing IoU thresholds; results should be shown threshold-robust.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-082 — Feature-space distillation preserves prompt responsiveness while output-space distillation destroys it: two certified-equivalent compression routes produce behaviorally different interactive models, and the difference is invisible to standard benchmarks.

- **Problem**: Distillation recipes for SAM differ in what they match (encoder embeddings vs final masks), and recipe choice is treated as an implementation detail; if it determines interactive behavior, the community needs to know before efficient variants become the default annotation backends.
- **Core hypothesis**: Matching encoder features transfers the representation the decoder's prompt machinery was calibrated for, preserving click-response dynamics; matching final masks lets the student solve the imitation task with prompt-insensitive shortcuts, so interactive responsiveness (marginal effect of each additional click) degrades specifically under output-space distillation.
- **Falsifiable prediction**: Students distilled with feature matching show click-response curves close to the teacher, while output-matched students at equal single-shot accuracy show flattened curves (later clicks change masks less), with the difference persisting across student capacities.
- **Why important**: It provides a causal design rule for compressing interactive models (match the interface-feeding representation, not the behavior), applicable beyond segmentation to any prompt-conditioned system.
- **Why possibly novel**: HYPOTHESIS: both distillation styles exist in the efficient-SAM family; attributing interactive-behavior differences to the matching target with controlled experiments appears new.
- **Community default belief (what is treated as true)**: What matters in distillation is student capacity and data; the choice of matching target is secondary once accuracy is matched.
- **Why that might be wrong**: Accuracy is a single functional of behavior; different matching targets can produce equal accuracy with different function classes, and only the feature-matched class is constrained to preserve the prompt interface's operating conditions.
- **Minimal falsification experiment**: Distill matched-capacity students under both objectives from the same teacher and data, compare click-response curves and clicks-to-quality; falsified if behavior is equivalent.
- **Fastest falsification experiment**: One day: two small students (one per objective) on a modest corpus, click-response comparison on 100 objects.
- **Main risk**: Fair capacity and schedule matching between distillation styles is delicate; multiple budgets needed.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: MobileSAM used encoder-level distillation per its paper; controlled comparison is MODEL SPECULATION

### W13-P1-A-083 — Quantization is prompt-type biased: INT8 SAM loses point-prompt accuracy well before box-prompt accuracy, because sparse point information rides small activations that quantization noise drowns, making current quantization certifications misleading for interactive use.

- **Problem**: Quantized SAMs are validated on aggregate accuracy, typically with box prompts (from detection pipelines); if the prompt types degrade at different quantization levels, edge deployments optimized for interactive clicking are certified with the wrong test.
- **Core hypothesis**: Point prompts inject low-magnitude, spatially-sparse signals into the decoder whose downstream computation operates near quantization noise floors, whereas box prompts inject redundant, higher-magnitude constraints; therefore accuracy-vs-bitwidth curves diverge by prompt type, with points collapsing one to two bits earlier.
- **Falsifiable prediction**: Sweeping quantization levels shows a consistent prompt-type gap in degradation onset, localized (by per-layer sensitivity analysis) to decoder cross-attention paths carrying prompt-token information rather than to the encoder.
- **Why important**: Prompt-conditional fragility under quantization redefines how promptable models must be certified for edge deployment and identifies which layers need mixed-precision protection, a directly actionable engineering result.
- **Why possibly novel**: HYPOTHESIS: quantization studies of SAM exist for aggregate accuracy; prompt-type-stratified quantization analysis appears absent.
- **Community default belief (what is treated as true)**: Quantization degrades models uniformly across usage modes; one accuracy number per bitwidth characterizes the trade-off.
- **Why that might be wrong**: Uniform degradation assumes signal magnitudes are homogeneous across pathways, which is false by construction in an architecture mixing dense image evidence with sparse prompt tokens.
- **Minimal falsification experiment**: Quantize SAM at four bitwidths, evaluate point vs box protocols on matched instances, run per-layer sensitivity attribution; falsified if degradation is prompt-independent.
- **Fastest falsification experiment**: Hours: one INT8 conversion, points vs boxes on 200 instances; a visible asymmetric drop is the entry evidence.
- **Main risk**: Results may vary across quantization schemes (PTQ vs QAT); a scheme grid inflates cost but is needed for generality.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit in certification practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-084 — Token merging and pruning for SAM encoders selectively destroys thin and small structures long before average metrics move, because merging criteria based on feature similarity preferentially eliminate the minority tokens carrying rare-structure evidence.

- **Problem**: Token-reduction methods are adopted for speed with average-accuracy validation, but dense prediction needs every spatial location; if reduction is structurally biased against exactly the hard structures (vessels, wires, cracks), efficiency work is quietly re-introducing failure modes adaptation work just fixed.
- **Core hypothesis**: Feature-similarity-based token merging removes tokens belonging to spatially-small, texturally-distinct structures first (they have few similar neighbors and low total attention mass), so structure-stratified accuracy degrades ordered by structure thinness while global mIoU is flat, and a structure-aware merge criterion eliminates the bias at equal speedup.
- **Falsifiable prediction**: Applying standard token merging at increasing reduction ratios shows thin-structure metrics collapsing at ratios where overall mIoU changes marginally; instrumenting merge decisions confirms disproportionate merging of thin-structure tokens; a protected-token variant restores their accuracy at matched throughput.
- **Why important**: It documents a systematic efficiency-fairness trade-off across structure types and provides the fix, keeping efficient SAMs usable in the industrial and scientific domains most sensitive to thin structures.
- **Why possibly novel**: HYPOTHESIS: token merging (e.g., ToMe) is established for classification ViTs; structure-stratified consequences for promptable dense prediction and a protective criterion appear new.
- **Community default belief (what is treated as true)**: Token reduction with flat average-metric curves is safe to deploy; degradation, when it comes, is gradual and uniform.
- **Why that might be wrong**: Merging criteria are majority-statistics driven by design; rare-structure evidence is definitionally minority statistics, so the bias is baked into the mechanism and invisible to average metrics.
- **Minimal falsification experiment**: Token-merging sweep on SAM across reduction ratios, structure-stratified evaluation on natural plus thin-structure datasets, merge-decision audit, and one protected-merge arm; falsified if degradation is structure-uniform.
- **Fastest falsification experiment**: Hours: one merging config at two ratios on a vessel-like dataset plus COCO; compare metric-drop ratios between the two.
- **Main risk**: The protected criterion could reintroduce compute overhead that eats the speedup; throughput must be honestly matched.
- **Evidence labels**: community_default_belief: EVIDENCE (efficiency-work validation practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: token merging methods such as ToMe (Bolya et al.) exist for ViTs; SAM-specific structural bias is MODEL SPECULATION

### W13-P1-A-085 — Per-prompt early exit for SAM: mask quality saturates at an encoder depth that varies by prompt difficulty, and a prompt-conditioned depth router can cut average compute substantially at negligible accuracy cost, because most prompts are easy.

- **Problem**: SAM's encoder cost is fixed regardless of whether the prompt asks for an easy dominant object or a hard boundary case, wasting compute on the easy majority; dynamic-depth methods exist for classification but promptable segmentation adds an unexplored twist: difficulty is prompt-dependent, not just image-dependent.
- **Core hypothesis**: For a large fraction of prompts, masks decoded from intermediate encoder layers (with a lightweight per-layer alignment) match final-layer masks; the saturation depth is predictable before full computation from cheap prompt-image agreement features, enabling a router with controllable risk.
- **Falsifiable prediction**: Decoding from intermediate layers shows per-prompt saturation depths with high variance across prompts; a router trained on cheap features achieves large average-depth reduction at under one point accuracy loss, and the router's errors concentrate on predictable prompt categories (boundary-adjacent clicks).
- **Why important**: Prompt-conditional compute is the natural efficiency frontier for interactive models (users generate many trivially easy prompts), and the saturation-depth analysis doubles as an interpretability map of where segmentation-relevant computation completes.
- **Why possibly novel**: HYPOTHESIS: early-exit is established for classification; prompt-conditioned early exit with saturation-depth analysis for promptable segmentation appears new.
- **Community default belief (what is treated as true)**: The full encoder is needed for quality masks; dynamic depth is a classification trick that dense prediction's spatial detail requirements rule out.
- **Why that might be wrong**: Most prompts target dominant, high-contrast objects whose grouping is plausibly resolved early; the assumption that dense tasks need full depth everywhere has never been tested per-prompt.
- **Minimal falsification experiment**: Train per-layer alignment heads, measure saturation-depth distributions on two datasets, train and evaluate the router; falsified if saturation depths are uniformly deep or unpredictable.
- **Fastest falsification experiment**: One day: alignment heads at three depths, saturation histogram on 500 prompts; high variance plus early mass justifies the router.
- **Main risk**: Intermediate-layer decoding may need enough alignment capacity that the saved compute is partly spent on the alignment heads.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: early-exit networks exist for classification; promptable-segmentation instantiation is MODEL SPECULATION

## Cluster: `adapter_ecosystem_continual` (6 ideas)

### W13-P1-A-086 — The IoU head is a free adapter router: selecting which domain LoRA to apply per image by comparing SAM's own predicted-score distributions under each adapter beats both single adapters and weight merging, with zero additional trained parameters.

- **Problem**: Multi-domain deployments must choose among adapter selection (needs a trained router), merging (loses per-domain performance), or manual routing (operational burden); an intrinsic routing signal would eliminate the extra machinery, but nobody has checked whether the model already provides one.
- **Core hypothesis**: Running a probe prompt set through each candidate adapter and reading the predicted-score distribution yields a competence signal sufficient for near-oracle adapter selection, because the score head (though miscalibrated absolutely, idea 023) remains relatively informative across adapters on the same image.
- **Falsifiable prediction**: Score-based routing achieves a large fraction of oracle-routing accuracy across a five-domain adapter zoo, beating the best single adapter and uniform merging, and degrades gracefully as domains become similar (where routing errors are harmless).
- **Why important**: Zero-cost routing makes adapter zoos operationally simple, and relative-competence readout from self-assessment heads would be a reusable pattern for foundation-model ecosystems generally.
- **Why possibly novel**: HYPOTHESIS: adapter routing via trained gates exists; routing via the frozen model's own quality head appears untested for segmentation.
- **Community default belief (what is treated as true)**: Routing among adapters requires training a router or gating network; internal heads are too unreliable under shift to drive selection.
- **Why that might be wrong**: Absolute calibration and relative discrimination are different properties; a head can be biased yet still rank its own competence across adapters usefully, and only absolute calibration has been criticized.
- **Minimal falsification experiment**: Five domain adapters, mixed-domain test stream, compare score-routing vs oracle vs best-single vs merged; falsified if score-routing tracks the merged or single baselines.
- **Fastest falsification experiment**: Hours: two adapters, two domains, route by mean top-score over a 3x3 probe grid; compare to oracle routing on 100 images.
- **Main risk**: Idea 023's style-critic effect could make scores uninformative exactly on hard out-of-domain images, capping routing quality; the two studies should share infrastructure.
- **Evidence labels**: community_default_belief: EVIDENCE (router-design practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-087 — Catastrophic remembering: narrow-domain PEFT resurrects pretraining biases that SAM's final training had suppressed (texture leakage, compact-mask preference), so adaptation can move a model backward along its own training history, not just away from it.

- **Problem**: Forgetting is framed as losing recent capabilities; the possibility that fine-tuning reactivates older, suppressed behaviors (because narrow data removes the pressure that suppressed them) is unexamined for segmentation models, yet it predicts a specific, testable error signature.
- **Core hypothesis**: Behaviors suppressed late in SAM's training (errors characteristic of MAE-stage or early-data-engine-stage models) reappear under narrow-domain PEFT in proportion to how far the adaptation data distribution is from the data that drove the suppression, producing error profiles that match earlier-stage models more than a generic degradation model would predict.
- **Falsifiable prediction**: Error-profile similarity between adapted SAM and reference earlier-stage models (MAE probes, weaker segmenters) increases with adaptation, on non-target images, beyond what matched-accuracy random degradation controls show.
- **Why important**: If adaptation moves models backward along their developmental trajectory, adapter safety evaluation should include regression tests against known ancestral failure modes, a fundamentally different test battery than current practice.
- **Why possibly novel**: HYPOTHESIS: the reactivation-of-suppressed-behavior framing exists in psychology; a quantitative version for foundation-model adaptation appears untested.
- **Community default belief (what is treated as true)**: Fine-tuning damage is forward-looking noise: the model gets worse in unpredictable ways, not in historically-structured ways.
- **Why that might be wrong**: Suppression in neural networks is often implemented as context-dependent overrides rather than erasure; remove the maintaining pressure and the override decays first, un-masking the old behavior — a mechanism with support in continual-learning analyses of smaller models.
- **Minimal falsification experiment**: Define an ancestral-error battery from MAE-feature probes and early open segmenters, track adapted-SAM similarity to it across PEFT intensity with degradation-matched controls; falsified if adapted errors are no more ancestral than random degradation.
- **Fastest falsification experiment**: One day: heavy LoRA on one narrow domain, compare error-type histogram on natural images against frozen SAM and an MAE-probe baseline.
- **Main risk**: Constructing credible ancestral references is the weak point; MAE probes are an approximation of SAM's actual early stages.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-088 — Interference between simultaneously-composed LoRAs is predicted by principal angles between their update subspaces: a five-minute weight-space measurement forecasts whether two adapters can be stacked, replacing trial-and-error composition.

- **Problem**: Users increasingly stack adapters (domain plus task plus style), discovering incompatibilities empirically after deployment; a predictive compatibility metric computable from weights alone would make composition an engineering discipline instead of alchemy.
- **Core hypothesis**: Destructive interference between composed LoRAs is driven by subspace overlap in specific layers (aligned directions with conflicting scalings), so a weighted principal-angle profile predicts composed-model performance drop, and orthogonality-encouraged retraining of one adapter eliminates the interference it predicts.
- **Falsifiable prediction**: Across an adapter-pair grid, the subspace-overlap metric correlates strongly with measured composition damage; pairs retrained with orthogonality constraints show both reduced predicted overlap and reduced actual damage, closing the causal loop.
- **Why important**: Composability is the core promise of the adapter ecosystem; a validated predictor plus a constructive fix would be immediately adopted and would ground composition in measurable weight geometry.
- **Why possibly novel**: HYPOTHESIS: LoRA merging and interference are actively studied in NLP; a validated per-layer principal-angle predictor with a causal retraining arm for segmentation adapters appears new.
- **Community default belief (what is treated as true)**: Adapter compatibility must be discovered empirically per combination; weight inspection cannot tell you whether behaviors will conflict.
- **Why that might be wrong**: Low-rank updates live in small subspaces where geometric collision is well-defined and rare by chance; when collisions do occur they are plausibly both necessary and sufficient for conflict, making prediction feasible precisely because of the low-rank structure.
- **Minimal falsification experiment**: Train eight single-purpose adapters on SAM, evaluate all pairs composed, correlate damage with subspace metrics, run the orthogonal-retraining arm on the worst pairs; falsified if geometry does not predict damage.
- **Fastest falsification experiment**: Hours: three adapter pairs spanning low to high subspace overlap, measure composition damage, check ordering.
- **Main risk**: Interference may be dominated by activation-space (data-dependent) effects invisible to weight-space geometry, which the study design should detect via residual analysis.
- **Evidence labels**: community_default_belief: EVIDENCE (current practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: LoRA composition and merging are studied in the NLP literature; the segmentation-specific predictive law is MODEL SPECULATION

### W13-P1-A-089 — Adaptation order matters and easy-first wins: sequentially adapting SAM through domains ordered from near to far (relative to pretraining) yields better final multi-domain performance than far-first or random order, establishing a curriculum effect for adapters.

- **Problem**: Organizations adapt models through domain sequences dictated by business timing, assuming order is irrelevant to the final result; if order changes the endpoint, sequencing becomes a controllable optimization variable nobody is using.
- **Core hypothesis**: Early adaptation steps set the effective inductive bias for later ones: near-domain-first preserves prompt-map smoothness and feature geometry that far-domain adaptation then builds on, while far-first breaks structures that near-domain data cannot rebuild, producing path dependence measurable at equal total data and compute.
- **Falsifiable prediction**: Over multiple domain triples, near-to-far ordering ends with higher average multi-domain performance and higher retained natural-image capability than far-to-near, with the gap exceeding seed variance; path dependence correlates with how much the far domain damages prompt-map smoothness when applied first.
- **Why important**: A confirmed curriculum effect converts adaptation scheduling into a free performance lever and informs theories of how sequential fine-tuning composes in weight space.
- **Why possibly novel**: HYPOTHESIS: curricula are studied for pretraining and task learning; domain-ordering effects for sequential PEFT of a segmentation foundation model appear unexamined.
- **Community default belief (what is treated as true)**: With the same data and budget, the endpoint of sequential adaptation is roughly order-independent; forgetting depends on what you trained, not when.
- **Why that might be wrong**: Optimization is path-dependent in nonconvex landscapes, and adaptation steps are large enough to move between basins; order-independence is a linear-regime assumption applied outside its regime.
- **Minimal falsification experiment**: Three domains with defensible near/far ordering (by frozen-feature similarity), run all six orders with three seeds, compare endpoint metrics; falsified if orders are statistically indistinguishable.
- **Fastest falsification experiment**: One day: two domains, both orders, three seeds each at small scale; a consistent endpoint gap is the existence proof.
- **Main risk**: Six orders times seeds is compute-heavy; SAM-B scale and small domains keep it feasible but limit generality.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-090 — Domain shifts share low-rank structure: one shared LoRA trained jointly on N diverse domains matches N separate LoRAs at one-Nth the parameters, implying that adaptation learns a common shift-correction operator rather than N unrelated fixes.

- **Problem**: The adapter-per-domain paradigm assumes domain corrections are essentially unrelated; if a shared low-rank correction captures most of every domain's gain, the field is storing and serving N copies of nearly the same function while missing the scientific point that domain gap has universal structure.
- **Core hypothesis**: A large component of what each domain LoRA learns is a domain-generic correction (e.g., re-weighting frequency bands, relaxing photometric priors, adjusting decoder thresholds) so joint training finds it with minimal per-domain residual, and the shared update's singular vectors are interpretable as generic shift operators.
- **Falsifiable prediction**: Shared LoRA at rank r approaches the average performance of per-domain LoRAs at rank r each, the gap shrinking as domain count grows; SVD of per-domain updates independently trained shows high pairwise subspace overlap in specific layers, corroborating shared structure.
- **Why important**: Both an infrastructure result (one adapter to serve all) and a scientific one: it would mean domain gap for a segmentation foundation model is a low-dimensional, characterizable object, not an unstructured catch-all.
- **Why possibly novel**: HYPOTHESIS: multi-task adapters exist; the claim that cross-domain segmentation shift itself is low-rank-shared, with the SVD-overlap corroboration, appears untested.
- **Community default belief (what is treated as true)**: Each domain needs its own adapter; domain corrections do not meaningfully share structure across dissimilar domains.
- **Why that might be wrong**: All these domains deviate from the same pretraining distribution, so their corrections all point back toward relaxing the same priors — a common component the per-domain paradigm never looks for.
- **Minimal falsification experiment**: Six domains: per-domain vs shared LoRA at matched total and per-domain parameters, plus subspace-overlap analysis of independent updates; falsified if shared lags badly and overlaps are near chance.
- **Fastest falsification experiment**: Hours: SVD-overlap analysis of three existing per-domain LoRAs; high overlap justifies the joint-training experiment.
- **Main risk**: Negative transfer between conflicting domains could mask shared structure; per-domain residual mini-adapters should be an arm to separate the effects.
- **Evidence labels**: community_default_belief: EVIDENCE (adapter-per-domain practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-091 — Self-training SAM on its own confident masks converges to degenerate over-smooth segmentation because the confidence signal is style-biased (idea 023): the obvious test-time adaptation baseline is predicted to fail in a specific, diagnosable way.

- **Problem**: Test-time adaptation via confident pseudo-labels is the default recipe ported from classification; for SAM, if confidence tracks mask style rather than correctness, self-training amplifies the style prior each round, and the failure will be misread as a data problem rather than a mechanism problem.
- **Core hypothesis**: Iterative self-training with score-thresholded pseudo-masks drifts the model toward producing compact, smooth masks regardless of image evidence, with measurable shrinkage of boundary complexity distribution across rounds, while true accuracy first plateaus then declines — a signature distinguishable from ordinary overfitting.
- **Falsifiable prediction**: Across self-training rounds, predicted-score-selected masks show monotonically decreasing boundary complexity, the model's outputs on held-out images follow, and accuracy on complex-boundary objects declines before accuracy on compact objects, exactly the ordering the style-bias mechanism predicts and ordinary overfitting does not.
- **Why important**: It preempts a wave of flawed test-time adaptation work by identifying the failure mechanism in advance, and the diagnostic signature (complexity shrinkage ordering) lets others check their own pipelines cheaply.
- **Why possibly novel**: HYPOTHESIS: self-training failure modes are known generically (confirmation bias); the style-collapse mechanism specific to mask-quality-scored segmentation appears unarticulated.
- **Community default belief (what is treated as true)**: Confidence-filtered self-training is a reasonable, usually-helpful adaptation baseline; failures come from too-low thresholds or too-few iterations.
- **Why that might be wrong**: The recipe assumes confidence correlates with correctness under shift, which idea 023 argues is precisely what breaks; recycling a biased critic as a teacher institutionalizes its bias.
- **Minimal falsification experiment**: Run score-thresholded self-training on two shifted domains for five rounds, track complexity distributions and stratified accuracy; falsified if outputs do not drift toward compactness or the decline ordering is absent.
- **Fastest falsification experiment**: One day: two self-training rounds on one domain, compare boundary-complexity histograms of selected pseudo-labels round over round; visible shrinkage is the mechanism's fingerprint.
- **Main risk**: Well-chosen regularizers might mask the effect; the study should include both vanilla and regularized arms to map when the failure is expressed.
- **Evidence labels**: community_default_belief: EVIDENCE (TTA practice in classification and segmentation); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

## Cluster: `interaction_loops_human_factors` (5 ideas)

### W13-P1-A-092 — Click-policy shift is a hidden domain gap: SAM was trained on simulator clicks (error-region centers), humans click salient interiors and high-contrast landmarks, and this policy mismatch accounts for a measurable slice of real-world underperformance relative to benchmarks.

- **Problem**: The gap between benchmark and deployed interactive performance is attributed to image domain shift, but the prompts themselves are also out-of-distribution: no one has quantified how much performance is lost purely because human click distributions differ from training simulators.
- **Core hypothesis**: SAM's interactive competence is calibrated to simulator click statistics, so evaluating with human-logged clicks on in-domain images (no image shift at all) already produces a significant performance drop, and retraining the click simulator to match human statistics closes most of that drop.
- **Falsifiable prediction**: On identical images, human-click evaluation underperforms simulator-click evaluation by a margin exceeding annotator noise, the margin correlates with per-image divergence between human and simulator click distributions, and a human-statistics-matched fine-tune recovers most of it without any image-domain data.
- **Why important**: It cleanly separates two conflated sources of deployment gap and shows that prompt-distribution alignment is a data-free adaptation axis — likely cheaper than any image-domain adaptation.
- **Why possibly novel**: HYPOTHESIS: click simulation strategies are studied for training efficiency; framing human-vs-simulator click divergence as a quantifiable domain gap with its own adaptation appears new.
- **Community default belief (what is treated as true)**: Clicks are clicks; performance gaps in deployment come from image distribution shift, not from who or what generated the click.
- **Why that might be wrong**: The model's conditional distribution was fit to a specific prompt-generating process; conditioning variables are part of the data distribution, and changing their statistics is textbook covariate shift that happens to be invisible in image-space audits.
- **Minimal falsification experiment**: Collect human clicks on 500 benchmark objects, evaluate frozen SAM under both click sources, then fine-tune with human-matched simulation and re-evaluate; falsified if the two click sources perform equally.
- **Fastest falsification experiment**: Hours: 50 objects, five self-collected human clicks each vs standard simulator clicks, paired accuracy comparison on frozen SAM.
- **Main risk**: Human click collection is a small user study with IRB-style overhead; public annotation-tool logs could substitute if accessible.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM's interactive training used simulated prompts per the paper; human-divergence magnitude is HYPOTHESIS pending measurement

### W13-P1-A-093 — Interactive correction has oscillation modes: correcting one region creates errors elsewhere with probability that grows with adaptation strength, so heavily adapted SAMs exhibit whack-a-mole dynamics that make some targets uncorrectable in finite clicks.

- **Problem**: Interactive evaluation assumes monotone convergence to the target mask; if the correction operator has oscillatory or divergent modes (fixing A breaks B, fixing B re-breaks A), click-count metrics hide a qualitative failure class that determines whether annotation tasks can complete at all.
- **Core hypothesis**: The correction map (current mask plus corrective click to next mask) is a learned operator whose contraction property is not guaranteed; PEFT that strengthens domain priors reduces contraction (the model keeps snapping back to its prior), increasing the rate of non-converging correction sequences measurable as limit cycles in mask space.
- **Falsifiable prediction**: Simulated correction runs show a nonzero and adaptation-strength-increasing rate of cyclic or non-converging sequences (mask trajectory revisits previous states within a tolerance), concentrated on objects conflicting with the adapted prior; frozen SAM shows the lowest cycle rate.
- **Why important**: Convergence of interactive correction is the property annotation economics actually depends on; characterizing and monitoring the correction operator's dynamics introduces a control-theoretic lens on interactive segmentation.
- **Why possibly novel**: HYPOTHESIS: clicks-to-quality is standard; treating interactive refinement as a dynamical system and measuring its convergence and cycles appears new.
- **Community default belief (what is treated as true)**: More corrective clicks monotonically approach the target; interactive refinement always terminates for a competent user.
- **Why that might be wrong**: Each correction is a full re-inference through a model with strong priors, not an incremental edit; there is no architectural guarantee of contraction, and strengthened priors actively oppose corrections toward prior-inconsistent targets.
- **Minimal falsification experiment**: Run scripted 20-click correction policies on 500 objects across frozen and adapted checkpoints, detect cycles and non-convergence, correlate rates with adaptation strength; falsified if trajectories converge monotonically everywhere.
- **Fastest falsification experiment**: Hours: 30 prior-conflicting objects (unusual shapes in an adapted domain), 15-click scripted corrections, check for state revisits.
- **Main risk**: Cycle detection depends on the correction policy; several policies must be tested to show the phenomenon is model-driven, not policy-driven.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit monotone-convergence assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-094 — The model's best click is not where humans click: a gradient-derived where-to-click advisor (computed from SAM's own sensitivity) increases per-click information and cuts annotation time, revealing that human click intuitions are miscalibrated to the model's actual decision geometry.

- **Problem**: Interactive tools let users click by intuition, and all guidance research focuses on improving the model; the complementary question — telling the user where their click would help the model most — is unaddressed, though it needs no model changes at all.
- **Core hypothesis**: Per-pixel expected mask improvement (estimable from prompt-sensitivity maps or output variance under hypothetical clicks) identifies click locations substantially better than human choice, and displaying a top-k suggestion overlay improves clicks-to-quality even after accounting for user compliance costs.
- **Falsifiable prediction**: In simulation, advisor-chosen clicks dominate human-logged clicks in marginal IoU gain per click; in a small user study, the overlay condition reduces time-to-target-quality with no accuracy loss, and the advantage is largest exactly on objects where idea 006's failure structure makes intuitive clicks bad.
- **Why important**: It inverts the adaptation direction (adapt the human interface to the model rather than the model to data), a cheap and immediately deployable path to better annotation throughput that also maps where model and human spatial intuitions diverge.
- **Why possibly novel**: HYPOTHESIS: active-learning-style query selection exists at the image level; per-click spatial guidance derived from the model's own sensitivity for interactive segmentation appears unexplored.
- **Community default belief (what is treated as true)**: Humans know where to click; interactive segmentation research should improve the model's response to clicks, not redirect the human.
- **Why that might be wrong**: Human clicks optimize human-perceptual saliency, but the model's decision geometry (attention structure, failure filaments) is alien to human intuition; nothing aligns the two, and ideas 006 and 009 predict specific divergences.
- **Minimal falsification experiment**: Implement the sensitivity-map advisor, run simulated comparisons on 1000 objects, then a 10-person user study with and without overlay; falsified if advisor clicks are no better than human or centroid baselines.
- **Fastest falsification experiment**: One day: simulated advisor-vs-centroid-vs-random comparison on 200 objects; a clear per-click information gain justifies the user study.
- **Main risk**: Sensitivity estimation per candidate click is expensive; approximations (coarse grids, one forward pass surrogates) must be validated for fidelity.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit in tool design); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-095 — Fine-tuning on accumulated user corrections personalizes toward the user's annotation style rather than toward accuracy: correction-trained models drift measurably toward individual annotator idiosyncrasies, conflating personalization with improvement.

- **Problem**: Products increasingly fine-tune on the corrections users make (treating them as free ground truth), assuming corrections encode true errors; corrections also encode the corrector's stylistic preferences (boundary tightness, hole handling), and no evaluation separates the two learning signals.
- **Core hypothesis**: Training on one annotator's corrections improves agreement with that annotator faster than agreement with a multi-annotator consensus, and a decomposition against consensus ground truth shows a substantial fraction of the learned update is style, predicting degraded performance when the model serves other users.
- **Falsifiable prediction**: Correction-trained models show rising same-annotator agreement with flat or declining consensus agreement, and cross-user evaluation shows other annotators need more corrections with the personalized model than with the base model on matched tasks.
- **Why important**: It warns that correction-loop learning silently fragments shared models into per-user dialects — an important finding for the growing human-in-the-loop adaptation industry — and defines the consensus-based evaluation such systems need.
- **Why possibly novel**: HYPOTHESIS: annotator bias is known in dataset construction; its dynamics inside online correction-based fine-tuning of a foundation segmenter appear unstudied.
- **Community default belief (what is treated as true)**: User corrections are ground truth; training on them straightforwardly improves the model for everyone.
- **Why that might be wrong**: A correction fixes the delta between model output and one person's intended mask, and intentions differ systematically across people; the training signal cannot distinguish shared truth from private style without multiple sources, which correction loops never have.
- **Minimal falsification experiment**: Multi-annotator dataset with consensus labels: fine-tune on single-annotator corrections, track same-annotator vs consensus agreement, then cross-user click-count evaluation; falsified if consensus agreement rises in step with same-annotator agreement.
- **Fastest falsification experiment**: One day if two-annotator data exists: fine-tune on annotator A corrections, evaluate against annotator B labels; a widening A-vs-B gap is the signature.
- **Main risk**: Requires multi-annotator infrastructure; annotator style differences may be small in some domains, bounding the effect.
- **Evidence labels**: community_default_belief: EVIDENCE (industry practice framing); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-096 — Prompt reuse across near-duplicate images fails silently at a predictable rate: prompts transferred between adjacent video frames or repeated product shots produce degraded masks without degraded confidence, defining an unstudied reliability metric (prompt transferability) for promptable models.

- **Problem**: Batch workflows commonly reuse a prompt across visually similar images (frames, catalog shots, tiled scans) assuming near-duplicate inputs preserve prompt validity; the failure rate of this ubiquitous practice has never been characterized, and confidence does not flag it.
- **Core hypothesis**: Prompt validity decays with small image transformations much faster than image similarity metrics suggest (because failure sets from idea 006 move with texture, not with content), so transferred prompts hit failure regions at rates predictable from local image-gradient changes but not from global similarity, while predicted scores stay high.
- **Falsifiable prediction**: On near-duplicate pairs (consecutive frames, re-shots), reusing source-image prompts yields a measurable rate of severe mask degradation uncorrelated with predicted score, and a cheap local-gradient-change statistic around the prompt location predicts failures with useful AUROC.
- **Why important**: It quantifies a silent failure in widespread workflows, provides a deployable guard (the local-change statistic), and introduces prompt transferability as a robustness dimension distinct from image robustness.
- **Why possibly novel**: HYPOTHESIS: robustness to image perturbation at fixed prompts is studied; robustness of a fixed prompt across naturally-varying near-duplicates appears unexamined.
- **Community default belief (what is treated as true)**: If two images look almost identical, a prompt that works on one works on the other; batch prompt reuse is safe.
- **Why that might be wrong**: Prompt validity depends on the local decision geometry at the click location, which is far more sensitive to small perturbations than global appearance is; similarity metrics measure the wrong thing for this purpose.
- **Minimal falsification experiment**: Build near-duplicate pairs from video and catalog datasets, transfer prompts, measure degradation rates and score blindness, fit the local-change predictor; falsified if transfer failures are rare or well-flagged by scores.
- **Fastest falsification experiment**: Hours: 50 consecutive-frame pairs, transfer clicks, count severe degradations and check score behavior on failures.
- **Main risk**: Ground truth on both images of each pair is needed; annotation cost bounds the study size.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit workflow assumption); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

## Cluster: `adaptation_interfaces` (6 ideas)

### W13-P1-A-097 — Resolution adaptation is a positional-encoding problem, not a feature problem: tuning only SAM's positional embeddings (all other weights frozen) recovers most of the gain that high-resolution fine-tuning provides, isolating where resolution knowledge lives.

- **Problem**: Adapting SAM to higher-resolution inputs is done by expensive full or encoder fine-tuning, on the assumption that features must re-learn scale; if interpolated positional embeddings are the actual bottleneck, resolution transfer costs a thousand parameters, and the community misunderstands what breaks under resolution change.
- **Core hypothesis**: Feature computations (attention patterns, local mixing) are largely scale-covariant, and the dominant failure at unseen resolutions comes from positional-embedding interpolation distorting spatial geometry; therefore PE-only tuning at the target resolution closes most of the gap to full high-res fine-tuning.
- **Falsifiable prediction**: At doubled input resolution, PE-only tuning recovers a large majority of the full-fine-tuning improvement across datasets, and attention-pattern analysis confirms pre-tuning distortions concentrate at positions where interpolation error is largest.
- **Why important**: It reduces an expensive adaptation to a trivial one and answers a representational question — whether scale handling in ViT segmenters is encoded in weights or in the positional scaffold — with consequences for all high-resolution dense prediction.
- **Why possibly novel**: HYPOTHESIS: PE interpolation tricks are folklore; a controlled decomposition attributing resolution-transfer gains to PE-only adaptation for promptable segmentation appears missing.
- **Community default belief (what is treated as true)**: Resolution transfer requires adapting features; positional-embedding interpolation is a lossless technicality.
- **Why that might be wrong**: Attention is position-blind except through the PEs, so resolution change enters the computation almost entirely through the positional scaffold — the one component everyone treats as a detail.
- **Minimal falsification experiment**: Three arms at high resolution (frozen with interpolated PE, PE-only tuned, full fine-tune) on two datasets; falsified if PE-only tuning recovers little of the full-fine-tune gain.
- **Fastest falsification experiment**: One day: PE-only tuning at 2x resolution on one dataset vs frozen-interpolated baseline; the recovered fraction is immediately informative.
- **Main risk**: Memory costs of high-resolution attention may force windowing changes that confound the attribution.
- **Evidence labels**: community_default_belief: EVIDENCE (common practice); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: ViTs require positional-embedding interpolation at new resolutions; attribution claim is MODEL SPECULATION

### W13-P1-A-098 — Test-time re-estimation of LayerNorm statistics (no training, no labels) closes a measurable fraction of SAM's domain gap, revealing how much of foundation-model domain shift is first-moment drift that normalization can absorb.

- **Problem**: The cheapest conceivable adaptation — updating normalization statistics on unlabeled target data — is a standard baseline for BatchNorm models but undefined-by-default for LayerNorm ViTs like SAM, so nobody knows what fraction of SAM's domain gap is trivially normalizable.
- **Core hypothesis**: Although LayerNorm normalizes per token (making the BatchNorm trick inapplicable directly), inserting lightweight input-statistics re-centering or recalibrating the learned affine parameters via unlabeled moment matching absorbs the first-moment component of domain shift, which constitutes a nontrivial fraction of the total gap on photometric-shift domains.
- **Falsifiable prediction**: Across a domain suite, unsupervised moment-matching recalibration recovers a consistent fraction of the frozen-to-LoRA gap on photometric-shift domains and near zero on structural-shift domains, providing simultaneously a cheap fix and a shift-taxonomy diagnostic.
- **Why important**: It establishes the correct zero-cost baseline all SAM adaptation papers should report, and the recovery fraction itself becomes a useful measure of how much of any domain's gap is superficial.
- **Why possibly novel**: HYPOTHESIS: test-time normalization adaptation is established for BatchNorm CNNs; a validated LayerNorm-appropriate analogue for promptable ViT segmenters appears unestablished.
- **Community default belief (what is treated as true)**: ViTs with LayerNorm have no normalization-statistics lever; test-time statistic adaptation is a BatchNorm-era trick that does not transfer.
- **Why that might be wrong**: The learned affine parameters after LayerNorm play the distribution-matching role BatchNorm statistics played, and they are recalibratable from unlabeled data; the community stopped looking after the architecture changed.
- **Minimal falsification experiment**: Implement two recalibration variants, evaluate on six domains stratified by shift type against frozen and LoRA references; falsified if recovery is negligible everywhere.
- **Fastest falsification experiment**: Hours: one photometric-shift domain, affine recalibration by feature-moment matching on 100 unlabeled images, measure recovery.
- **Main risk**: LayerNorm's per-token normalization may genuinely leave no first-moment slack to exploit, yielding a clean null (which still fixes the baseline question).
- **Evidence labels**: community_default_belief: EVIDENCE (TTA literature norms); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: test-time BatchNorm adaptation is established for CNNs; the LayerNorm analogue for SAM is MODEL SPECULATION

### W13-P1-A-099 — PEFT under a fixed prompt protocol turns SAM into a prompt-ignoring semantic segmenter: adapted models' outputs become nearly invariant to prompt content, meaning many published adapted-SAM results are really measuring a learned semantic prior wearing a promptable interface.

- **Problem**: Adaptation pipelines train and evaluate with rigid prompt protocols (always a centroid click or a ground-truth box), so nothing in the objective requires continued prompt sensitivity; the field may be publishing promptable-model results that a prompt-free model would replicate, without anyone measuring prompt dependence post-adaptation.
- **Core hypothesis**: Prompt-ablation sensitivity (output change when the prompt is moved, degraded, or randomized) collapses during protocol-rigid PEFT at a rate driven by target-dataset homogeneity, and adapted models approach the behavior of an equivalent prompt-free segmentation head trained on the same data.
- **Falsifiable prediction**: Post-PEFT models show drastically reduced output variance under prompt randomization compared to frozen SAM, their accuracy with random prompts approaches their accuracy with correct prompts on the target domain, and a prompt-free distilled head matches them, none of which holds for frozen SAM.
- **Why important**: It changes the interpretation of a large experimental literature (what was actually evaluated), and defines prompt-dependence retention as a mandatory reported metric for adapted promptable models.
- **Why possibly novel**: HYPOTHESIS: prompt-sensitivity collapse under rigid-protocol adaptation is a natural consequence nobody appears to have quantified or named.
- **Community default belief (what is treated as true)**: An adapted SAM is still a promptable model; the prompt keeps doing its job after fine-tuning.
- **Why that might be wrong**: Optimization removes whatever the loss does not require, and rigid protocols make prompt information redundant with the dataset prior; the interface remains, the function behind it quietly changes category.
- **Minimal falsification experiment**: Take five published-style adaptation recipes, measure prompt-randomization sensitivity before and after training, plus the prompt-free-equivalent comparison; falsified if sensitivity survives adaptation broadly.
- **Fastest falsification experiment**: Hours: one public adapted checkpoint, compare masks under correct vs random prompts on its target data; near-identical outputs are the smoking gun.
- **Main risk**: Some target tasks genuinely have one object per image, where prompt invariance is arguably correct behavior; the study must include multi-object target domains where invariance is unambiguously pathological.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-100 — For non-RGB modalities, a tiny learned input stem beats the standard channel-inflation trick: freezing all of SAM and learning only a 1x1 modality-to-pseudo-RGB projection outperforms replicating RGB weights across channels, showing the modality gap lives at the input interface.

- **Problem**: Depth, thermal, SAR, and multispectral imagery are wrestled into SAM by copying RGB patch-embedding weights across channels or naive grayscale conversion, a convention adopted without comparison against the minimal alternative of learning the input projection itself.
- **Core hypothesis**: SAM's features are modality-agnostic once inputs are mapped into the photometric statistics it expects, so a learned input stem of a few thousand parameters (with everything else frozen) captures most of what encoder PEFT achieves on non-RGB modalities, while channel inflation misaligns input statistics and forces downstream layers to compensate.
- **Falsifiable prediction**: Across three non-RGB modalities, stem-only training beats channel inflation consistently and reaches a large fraction of encoder-LoRA performance, and the learned stems converge to interpretable mappings (e.g., depth gradients to pseudo-shading) across seeds.
- **Why important**: A validated minimal recipe would immediately serve several application communities, and the interpretable-stem finding would show that cross-modality transfer of segmentation features is an input-coding problem rather than a representation problem.
- **Why possibly novel**: HYPOTHESIS: learned input adapters exist in scattered forms; a controlled stem-vs-inflation-vs-LoRA comparison with stem interpretability analysis for SAM appears missing.
- **Community default belief (what is treated as true)**: Channel inflation or grayscale replication is the standard, adequate way to feed non-RGB data to RGB-pretrained models; real gains require adapting the encoder.
- **Why that might be wrong**: Inflation preserves weights but not input statistics, feeding the frozen encoder data far off its expected manifold; a learned stem fixes the manifold mismatch directly at the cheapest possible location.
- **Minimal falsification experiment**: Three modalities, three arms (inflation, stem-only, encoder LoRA) at matched data; compare accuracy and analyze stem weights across seeds; falsified if stems lag inflation or LoRA dominates by wide margins everywhere.
- **Fastest falsification experiment**: One day: depth modality, stem-only vs inflation with frozen SAM on one dataset; the gap direction is immediately informative.
- **Main risk**: Modalities with fundamentally different noise physics (speckle in SAR) may defeat any pointwise input mapping, bounding the claim's scope.
- **Evidence labels**: community_default_belief: EVIDENCE (widespread convention); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: MODEL SPECULATION

### W13-P1-A-101 — Loss choice shapes mask topology more than architecture choice: the focal-plus-dice convention in SAM adaptation imposes a measurable bias toward simply-connected masks, an ignored confound that may explain topology-related conclusions across the PEFT literature.

- **Problem**: Adaptation papers vary architectures and PEFT methods while uniformly copying the loss recipe, so systematic topology effects of the loss (hole-filling, fragment suppression) are invisible in comparisons and get misattributed to methods or domains.
- **Core hypothesis**: Dice-family losses, by rewarding bulk overlap, penalize topologically complex predictions asymmetrically, so models adapted with focal-dice produce fewer holes and fragments than boundary- or cross-entropy-trained counterparts at matched IoU, and reported method differences in topology-sensitive domains shrink substantially once loss is controlled.
- **Falsifiable prediction**: A loss-by-method factorial on topology-rich domains shows loss main effects on topology metrics (Betti-number error, hole recall) exceeding method main effects, while IoU differences remain method-dominated, demonstrating that topology conclusions in the literature track the loss convention.
- **Why important**: Identifying a field-wide confound redirects credit assignment in dozens of comparisons and gives topology-sensitive application areas (medical, industrial inspection) a cheap corrective: change the loss, not the architecture.
- **Why possibly novel**: HYPOTHESIS: loss effects on segmentation topology are known in principle; quantifying loss-vs-method effect ratios as a confound audit of the SAM-adaptation literature appears new.
- **Community default belief (what is treated as true)**: The loss recipe is settled infrastructure; differences between adapted models reflect their adaptation methods.
- **Why that might be wrong**: Losses define what error structure is cheap; topology is exactly the mask property over which common losses differ most, yet it is the property comparisons never stratify by.
- **Minimal falsification experiment**: Two domains rich in holes and fragments, three losses crossed with three PEFT methods, topology-decomposed evaluation; falsified if method effects dominate topology metrics.
- **Fastest falsification experiment**: One day: one method, two losses, one hole-rich dataset; a topology-metric gap at matched IoU demonstrates the confound exists.
- **Main risk**: Interaction effects (loss-method) could complicate the clean main-effect story; the factorial design handles but complicates messaging.
- **Evidence labels**: community_default_belief: EVIDENCE (recipe uniformity in the literature); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: KNOWN FACT: SAM's training used a focal-plus-dice loss combination per the paper; the confound magnitude is MODEL SPECULATION

### W13-P1-A-102 — Pseudo-label bias amplification law: students trained on SAM everything-mode outputs inherit its anti-small, anti-thin biases amplified by a measurable factor, so each generation of SAM-labeled training data drifts further from reality in a predictable direction.

- **Problem**: SAM-generated pseudo-labels now feed countless training pipelines; if the generator's known biases are amplified (not just copied) by students — because students turn soft, occasional omissions into confident systematic ones — the ecosystem is compounding a directional error nobody is tracking across generations.
- **Core hypothesis**: Bias amplification through pseudo-label training holds for segmentation: the student's size-dependent recall curve is a sharpened version of the teacher's (omission probabilities pushed toward 0 or 1), and a second generation (student labels training a new student) sharpens further, following a contraction map whose fixed point excludes small structures entirely.
- **Falsifiable prediction**: Measuring size-stratified recall across teacher, student, and second-generation student shows monotone steepening of the size-recall curve at its low end, with amplification factors consistent across architectures, and simple label-noise corrections (loss reweighting by teacher uncertainty) break the contraction.
- **Why important**: It quantifies a compounding ecosystem-level risk of foundation-model-generated data, gives the field an early-warning metric (curve steepening), and connects to bias-amplification results known from classification.
- **Why possibly novel**: HYPOTHESIS: bias amplification is documented for attribute classification; a generational contraction analysis for segmentation pseudo-labels with an intervention appears new.
- **Community default belief (what is treated as true)**: Students average out teacher noise; pseudo-label training approximately preserves the teacher's quality profile rather than amplifying its biases.
- **Why that might be wrong**: Averaging holds for symmetric noise, but omission of small structures is asymmetric systematic bias; students fit the systematic component and, facing consistent absence, learn confident absence — the amplification mechanism.
- **Minimal falsification experiment**: Generate SAM pseudo-labels on a corpus with real ground truth available, train a student, generate second-generation labels, train again; compare size-stratified recall curves across generations; falsified if curves do not steepen.
- **Fastest falsification experiment**: One day: one generation only — compare teacher vs student size-recall curves on ground-truthed data; visible steepening at generation one is the core signal.
- **Main risk**: Two generations of training is compute-heavy; small architectures and subsampled corpora keep it tractable at the cost of scale realism.
- **Evidence labels**: community_default_belief: HYPOTHESIS (implicit); core_hypothesis: HYPOTHESIS; falsifiable_prediction: HYPOTHESIS; prior_work_basis: VERIFIED PRIOR WORK: bias amplification is documented in classification settings; the segmentation generational law is MODEL SPECULATION

