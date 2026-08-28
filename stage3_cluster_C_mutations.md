# Stage 3 — Cluster C Mutations

8 survivors whose original claims were too close to prior work (or too weak/broad) but that contained a precise, untested remainder. Each is rewritten as the sharpest version that survives the adversarial prior-work audit.

---

## M1 — from C-0002 (absorbing the useful control of killed C-0005)

**Original claim:** Text embeddings are just an arbitrary linear classifier for open-vocab segmentation.

**Why mutated:** The random/fixed-classifier control is a known classification result (Hoffer et al., "Fix your classifier," ICLR 2018), and the companion resolution claim (C-0005) is covered by S² (Shi et al., 2024) and MM1. The unrun piece is the *combination* in open-vocab dense prediction.

**Mutated claim:** On seen classes — which dominate reported OV-seg numbers — replacing the CLIP text tower with random-orthogonal class vectors at matched resolution/TTA recovers most of the reported mIoU; the text tower's semantic geometry earns its keep only on genuinely unseen classes.

**Minimal experiment:** Fine-tune one mask decoder on COCO-Stuff under (a) CLIP text embeddings, (b) random orthogonal vectors, (c) shuffled text embeddings, resolution/TTA matched; report seen vs held-out-class mIoU decomposition.

**Kill condition:** If (b) collapses on seen classes, the field's implicit assumption is confirmed and the paper is a null.

**Reviewer attack papers:** Hoffer et al. 2018; SAN/OVSeg-style papers with strong unseen-class gains.

## M2 — from C-0014

**Original claim:** Self-attention "surgery" methods for CLIP segmentation equal Gaussian smoothing.

**Why mutated:** NACLIP (Hajimiri et al., 2024) already builds a Gaussian neighborhood prior *into* attention, so the bare claim is half-published as a method. The unpublished piece is the adversarial equivalence audit.

**Mutated claim:** Under a matched hyperparameter-tuning budget, a post-hoc tuned Gaussian/bilateral filter over vanilla CLIP similarity maps statistically matches the mIoU of the published attention-surgery family (SCLIP, GEM, CLIP Surgery, NACLIP) on VOC/Context/ADE.

**Minimal experiment:** Reimplement three surgery methods; tune the filter baseline with an identical validation budget (same number of trials); paired bootstrap over images.

**Kill condition:** If surgery methods beat the tuned filter by a clear margin, publish the negative audit result honestly or drop.

**Reviewer attack papers:** NACLIP ("Gaussian prior is ours"); GEM ("gains exceed smoothing").

## M3 — from C-0047

**Original claim:** Patch serialization order shapes VLM spatial reasoning.

**Why mutated:** "Order matters" is folklore-adjacent (ViT permutation studies, Naseer et al. 2021) and VLM spatial failures are documented (Kamath et al., EMNLP 2023). The crisp untested prediction is *directional asymmetry*.

**Mutated claim:** Because raster-scan serialization makes left/right adjacency local in token order but above/below adjacency distant, frozen VLMs are measurably more accurate on horizontal than vertical spatial relations — and the asymmetry flips or shrinks under column-major/boustrophedon serialization at small retrain scale.

**Minimal experiment:** (1) Audit horizontal-vs-vertical relation accuracy on What's Up / VSR-style benchmarks across frozen open VLMs, controlling for relation-frequency priors in training text. (2) Optional: small VLM retrain with column-major serialization; test asymmetry flip.

**Kill condition:** No horizontal/vertical asymmetry beyond text-prior confounds in step (1) → dead cheaply.

**Reviewer attack papers:** Kamath et al. 2023; Naseer et al. 2021.

## M4 — from C-0068

**Original claim:** Fresh optimizer state, not full-rank updates, causes early fine-tuning damage.

**Why mutated:** LoRA-forgetting is an instructed harsh zone; "LoRA Learns Less and Forgets Less" (Biderman et al., TMLR 2024) owns the rank narrative and Ash & Adams (NeurIPS 2020) own warm-starting. The exact confound-isolating control is absent.

**Mutated claim:** A measurable fraction of the "full fine-tuning forgets more than LoRA" gap is an optimizer-transient artifact: transplanting converged Adam second moments (warm-started optimizer state) into full fine-tuning at matched effective learning-rate schedule closes part of the forgetting gap without changing update rank.

**Minimal experiment:** Llama-class model, one instruction-tuning dataset; arms: full-FT fresh Adam, full-FT transplanted moments, full-FT with per-parameter LR mimicking transplanted preconditioner, LoRA. Measure source-task forgetting curves over the first N steps.

**Kill condition:** Transplanted moments close ≈0% of the gap → rank story stands; report null.

**Reviewer attack papers:** Biderman et al. 2024; Ash & Adams 2020.

## M5 — from C-0099

**Original claim:** Whitening erases most claimed differences between SSL methods.

**Why mutated:** Duality theory (Garrido et al., ICLR 2023) and matched-recipe benchmarks already argue method families are close; whitening exists as a method component (W-MSE). The unrun cheap audit: post-hoc whitening on *published checkpoints*.

**Mutated claim:** Applying identical post-hoc feature whitening to N published SSL checkpoints (contrastive, distillation, MIM families) shrinks the reported inter-method linear-probe spread by a large, quantifiable fraction — attributing much of the SSL leaderboard to second-moment bookkeeping rather than representational content.

**Minimal experiment:** ≥12 public checkpoints; frozen features on IN-1k + 5 transfer sets; probe accuracy before/after whitening; variance decomposition of method-family effect.

**Kill condition:** Spread survives whitening mostly intact → null published cheaply or dropped.

**Reviewer attack papers:** Garrido et al. 2023; solo-learn benchmark papers.

## M6 — from C-0158

**Original claim:** Uncertainty sampling poisons active learning when the LLM is the annotator.

**Why mutated:** AL-with-LLM-annotators exists (FreeAL, EMNLP 2023) and noisy-oracle AL is classic. The unowned piece is the *correlated-noise mechanism* and its fix.

**Mutated claim:** Uncertainty-based acquisition is anti-correlated with LLM-annotation quality — the same items that maximize learner uncertainty maximize annotator error — so uncertainty AL underperforms random sampling at fixed budget precisely when annotator and learner difficulty are correlated; an acquisition function penalized by predicted annotator error restores the AL advantage.

**Minimal experiment:** 3 text + 1 vision classification datasets; GPT-class annotator; measure item-level correlation between learner uncertainty and annotator error; compare random vs uncertainty vs error-penalized acquisition at matched budgets.

**Kill condition:** Correlation near zero or uncertainty AL still wins → mechanism dead, report correlation study as short paper or drop.

**Reviewer attack papers:** FreeAL; classic noisy-oracle AL (assumes acquisition-independent noise — that assumption is the target).

## M7 — from C-0355

**Original claim:** Head-class data improves tail-class generalization.

**Why mutated:** Head→tail feature transfer is established (OLTR, CVPR 2019; Kang et al., ICLR 2020). The unpublished piece is the labeling-economics curve.

**Mutated claim:** There exists a measurable annotation-budget crossover: below it, the next label is worth more on a head class than a tail class *for tail-class performance itself* — and the crossover point is predicted by a pre-computable feature-sharing score (e.g., class-prototype similarity on a foundation backbone) before any labels are bought.

**Minimal experiment:** Long-tail benchmarks (ImageNet-LT, iNat-LT subsets); marginal-value curves via controlled label-budget sweeps; test crossover prediction from the sharing score on held-out class pairs.

**Kill condition:** No crossover exists (tail labels always dominate) or the score fails to predict → drop.

**Reviewer attack papers:** OLTR; Kang et al. 2020; active-learning budget literature.

## M8 — from C-0365

**Original claim:** Which pre-deep-learning ideas revive on foundation features?

**Why mutated:** As a survey it is unfocused and partially covered by ad hoc revivals (dense-CRF decline; superpixel-assisted SAM variants; kNN-on-DINOv2). The missing piece is a *predictive principle*.

**Mutated claim:** Classical components encode explicit priors (boundary snapping, spatial smoothness, geometric verification); a classical component helps a foundation model exactly where the model's measured failure profile leaves that prior unmet. Failure-mode profiling therefore *predicts, before integration*, which classical component will help which model — turning revival from trial-and-error into a testable matching principle.

**Minimal experiment:** Profile 3 foundation models (DINOv2, SAM, CLIP-seg) on boundary error, smoothness violations, geometric consistency; predict help/no-help for 4 classical components (CRF, superpixels, MRF smoothing, RANSAC verification) per model; run the 12-cell grid and score the predictions.

**Kill condition:** Prediction accuracy at chance → principle dead; grid results alone are not a paper.

**Reviewer attack papers:** CRF-decline analyses; SAM+superpixel hybrid papers.
