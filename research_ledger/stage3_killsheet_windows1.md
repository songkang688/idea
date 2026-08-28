# Stage 3 Prior-Work Kill-Sheet — Windows1 PI (vision / dense)

Prior: **already published unless proven otherwise.** Every citation below was retrieved and
verified during this pass. Claims I could not find a prior for are marked **NOT FOUND** and are
the only load-bearing novelty in this batch.

Verdict counts: **KILL 4 · MUTATE 8 · SURVIVE(weak) 1 · SURVIVE 0**

---

## VFM-A0022 — Worst-case semantically valid SAM click positions; IoU gap vs random-click eval

**Closest prior.** TETRIS: Towards Exploring the Robustness of Interactive Segmentation (AAAI
2024) — https://arxiv.org/abs/2402.06132

**Difference.** None material. TETRIS runs a fully differentiable white-box attack directly on
click coordinates, and it already imposes the validity constraint: positive clicks must fall in
unselected object area, negative clicks in selected non-object area, with an additional
distance-transform "interaction location loss" specifically to stop the optimizer from producing
clicks a real user would never make. It reports **IoU-D**, the gap between the IoU-maximizing and
IoU-minimizing click trajectories — the proposed metric. Coverage includes SAM, SAM-HQ and
MobileSAM (23 checkpoints, 5 datasets), and SAM-HQ ViT-B shows IoU-D 14.53 vs CFR-ICL's 2.39.

**Remaining novelty.** Effectively zero at the claim level. The only unclaimed surface is
*transfer* of worst-case clicks black-box across SAM variants, and Practical Region-level Attack
(https://arxiv.org/abs/2404.08255) already covers prompt-agnostic transferable attacks in the
image-perturbation threat model.

**Confidence.** High (0.9).

**R2 attack cite.** TETRIS, arXiv:2402.06132 — "this is IoU-D with the validity constraint
renamed."

**Verdict: KILL.**

---

## VFM-A0051 — Linear probe on frozen encoder recovers GT mask ⇒ failure is decoder-side

**Closest prior.** Where Does Texture Evidence Live in SAM? Features, Proposal Masks, and Texture
Segmentation (2026) — https://arxiv.org/abs/2606.14755. Supporting: There is no SAMantics!
(https://arxiv.org/abs/2411.15288, 2024); SANSA (https://arxiv.org/abs/2505.21795, 2025);
FrozenSeg (https://arxiv.org/abs/2409.03525, 2024).

**Difference.** The inferential move is already published in exactly this shape. The texture paper
probes frozen SAM features, shows the signal "is not absent from the frozen representation," then
separately tests the proposal/decoder route and concludes the failure "is better described as
readout and commitment mismatch than simple texture blindness." SANSA runs a pixel-level linear
probe on frozen SAM2 features versus DINOv2 to argue semantics are latent but unread, then
recovers them with AdaptFormer. FrozenSeg names the mask-proposal decoder as "the performance
bottleneck" and freezes both foundation models to fix it. "No SAMantics" runs the linear-probe
diagnostic on SAM features directly.

**Remaining novelty.** Encoder-vs-decoder attribution as a general statement is dead. What is not
published is **prompt-conditioned** credit assignment: probing conditioned on the specific
click/box that failed, on interactive-segmentation failure cases, with a swap intervention
(frozen-encoder + retrained decoder vs retrained encoder + frozen decoder) to convert correlation
into attribution.

**Confidence.** High (0.85) that the generic claim is occupied.

**R2 attack cite.** arXiv:2606.14755 §8.2 (frozen features contain recoverable evidence;
consolidation bottleneck).

**Verdict: MUTATE** — reframe to per-prompt credit assignment with an intervention, or drop.

---

## VFM-A0028 — Click vs box mask disagreement predicts GT error without labels

**Closest prior.** SAM-U: Multi-box prompts triggered uncertainty estimation (MICCAI UNSURE 2023)
— https://arxiv.org/abs/2307.04973. Supporting: FNPC-SAM
(https://pmc.ncbi.nlm.nih.gov/articles/PMC11182739/, 2024); MedSAM-U
(https://arxiv.org/abs/2409.00924, 2024); EvanySeg / Towards Ground-truth-free Evaluation of Any
Segmentation in Medical Images (https://arxiv.org/abs/2409.14874, 2024).

**Difference.** Prompt-variance-as-uncertainty is fully published — SAM-U treats multiple box
prompts as test-time augmentation, runs Monte Carlo over them, and produces pixel-level
uncertainty; FNPC-SAM uses that uncertainty to correct FN/FP; EvanySeg predicts Dice with no GT at
all and is the direct baseline any reviewer will demand. **But every one of these varies prompts
*within* a single prompt type** (multi-box, or multi-point). **NOT FOUND:** any paper using
disagreement *across prompt modalities* (click vs box on the same object) as the label-free error
signal.

**Remaining novelty.** Narrow but real. Cross-modality disagreement is a different and plausibly
better-conditioned signal, because Stable-SAM (https://arxiv.org/abs/2311.15776) shows point and
box prompts fail through *different* decoder-attention pathologies (background-biased vs
part-confined activation), so their disagreement should carry information that within-type jitter
does not. Needs to beat EvanySeg and SAM's own IoU head on ranking/calibration, not just correlate.

**Confidence.** Medium (0.6) — survives only as a delta over SAM-U with a hard baseline table.

**R2 attack cite.** SAM-U, arXiv:2307.04973 — "multi-prompt variance already gives you this."

**Verdict: MUTATE** — cross-modality only, framed as calibration/ranking vs EvanySeg + IoU head.

---

## VFM-A0166 — Near-duplicate overlap (SA-1B-style corpora vs COCO/ADE eval) inflates zero-shot

**Closest prior.** Does CLIP's generalization performance mainly stem from high train-test
similarity? (ICLR 2024) — https://arxiv.org/abs/2310.09562. Methodology: Do We Train on Test Data?
Purging CIFAR of Near-Duplicates (J. Imaging 2020) — https://www.mdpi.com/2313-433X/6/6/41. Also
Deduplicating Training Data Makes Language Models Better (ACL 2022) —
https://doi.org/10.18653/v1/2022.acl-long.577.

**Difference.** This hypothesis has already been tested at the strongest possible level of rigor
in the adjacent domain — and **largely rejected.** Mayilvahanan et al. retrained CLIP on pruned
LAION splits matched to ImageNet's train-test similarity and found overall performance "remains
high"; their sketch-pruned model still hit 44.78% on ImageNet-Sketch where the similarity-matched
expectation was ~14%. So the prior is not just "someone did this," it is "someone did this and the
effect was small." Barz & Denzler already own the near-duplicate detection + test-set-replacement
methodology (3.3% / 10% contamination on CIFAR-10/100). **NOT FOUND:** any quantification of
SA-1B ↔ COCO/ADE20K/LVIS image-level overlap. HQ-SAM only asserts its own HQSeg-44K has no overlap
with its eval sets.

**Remaining novelty.** The segmentation instantiation is genuinely unmeasured, but the idea is
structurally weaker than it looks: you cannot retrain SAM on a deduplicated SA-1B, so you can only
report *stratified* eval deltas (dup vs non-dup subsets), which is a much weaker instrument than
what ICLR 2024 already brought. Expect a null.

**Confidence.** High (0.85) that prior exists; medium (0.6) that the result is a null.

**R2 attack cite.** arXiv:2310.09562 — "high train-test similarity is insufficient to explain
foundation-model zero-shot performance; we already retrained to show it."

**Verdict: MUTATE** — demote to a measurement/audit artifact (overlap statistics + deduped
leaderboard deltas) with a pre-registered null. Do not sell it as an inflation claim.

---

## VFM-A0168 — Center-of-error simulated clicking overstates interactive seg vs human clicks

**Closest prior.** RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation
(2024) — https://arxiv.org/abs/2410.11722. Also TETRIS (https://arxiv.org/abs/2402.06132, AAAI
2024); Benenson et al., Large-Scale Interactive Object Segmentation With Human Annotators (CVPR
2019) —
https://openaccess.thecvf.com/content_CVPR_2019/papers/Benenson_Large-Scale_Interactive_Object_Segmentation_With_Human_Annotators_CVPR_2019_paper.pdf;
Rethinking Annotator Simulation (https://arxiv.org/abs/2404.01816, 2024).

**Difference.** None. This is the single most thoroughly occupied cell in the batch. RClicks
collected **475K real user clicks**, fit a clickability model to sample human-like clicks, and
concluded verbatim that "in real-world usage interactive segmentation models may perform worse
than it has been reported in the baseline benchmark, and most of the methods are not robust."
TETRIS ran a 600-user study and states the center-of-largest-error assumption "may not hold."
Benenson compared 2.5M real-annotator instances against simulation in 2019 and analyzed annotator
click behavior.

**Remaining novelty.** Zero.

**Confidence.** Very high (0.95).

**R2 attack cite.** RClicks, arXiv:2410.11722.

**Verdict: KILL.**

---

## VFM-A0121 — Frozen vs unfrozen encoder crossover as a function of labeled set size (dense)

**Closest prior.** Kumar et al., Fine-Tuning can Distort Pretrained Features and Underperform
Out-of-Distribution (ICLR 2022) — https://arxiv.org/abs/2202.10054. Dense/vision instantiations: A
Novel Benchmark for Few-Shot Semantic Segmentation in the Era of Foundation Models
(https://arxiv.org/abs/2401.11311, 2024); Lessons and Insights from a Unifying Study of PEFT in
Visual Recognition (https://arxiv.org/abs/2409.16434, 2024); How to build the best medical image
segmentation algorithm using foundation models (https://arxiv.org/abs/2404.09957, 2024); Rein
(https://arxiv.org/abs/2312.04265, CVPR 2024); Surgical Fine-Tuning
(https://arxiv.org/abs/2210.11466, ICLR 2023).

**Difference.** The crossover phenomenon is owned by Kumar et al. (ID/OOD, with LP-FT as the fix).
The dense/few-shot sweep is substantially covered: the FSS benchmark compares linear, multilayer,
SVF, LoRA and full FT across shot counts and finds the fine-tuning family "yield comparable
results between them"; Rein finds ~1% trainable parameters *beats* full FT for domain-generalized
segmentation (78.4 mIoU Cityscapes). **NOT FOUND:** a labeled-set-size crossover curve for dense
tasks paired with an *a priori predictive rule* for which side of the crossover you are on.

**Remaining novelty.** Only in the predictive direction. A descriptive curve is a reproduction. A
cheap selector — LogME-style (https://proceedings.mlr.press/v139/you21b.html, ICML 2021) extended
to dense readouts, or Auto-RGN from Surgical FT — that calls frozen-vs-tuned before you pay for
either run, is not published for segmentation and is the only defensible framing.

**Confidence.** Medium-high (0.75).

**R2 attack cite.** arXiv:2401.11311 — "already swept linear vs LoRA vs SVF vs full FT across shot
counts on dense tasks."

**Verdict: MUTATE** — ship a dense transferability *selector* with a decision-accuracy metric, not
a curve.

---

## VFM-A0263 / VFM-0274 — Constrained SAM-FT: max target Dice s.t. SA-1B promptability drop < ε

**Closest prior.** HQ-SAM: Segment Anything in High Quality (NeurIPS 2023) —
https://arxiv.org/abs/2306.01567. Also WiSE-FT: Robust Fine-Tuning of Zero-Shot Models
(https://arxiv.org/abs/2109.01903, CVPR 2022); PEFT unifying study
(https://arxiv.org/abs/2409.16434, 2024).

**Difference.** HQ-SAM is this idea's answer already shipped as a method: it freezes all SAM
weights precisely "to preserve the zero-shot transfer capability… while preventing model
overfitting or catastrophic forgetting," and its Table 9 *quantifies the exact trade-off this
proposal wants to constrain* — LoRA on SAM's encoder drops zero-shot COCO AP<sub>B</sub> from 33.3
to 28.6 and encoder adapters to 29.6, while HQ-SAM reaches 34.4. WiSE-FT provides the continuous
dial (θ = (1−α)θ₀ + αθ₁) along the retention/target axis, and the PEFT unifying study has already
applied WiSE to PEFT and found it "overturns" PEFT's apparent robustness advantage.

**Remaining novelty.** The Lagrangian/Pareto *framing* (explicit ε-budget on SA-1B promptability
retention) is not how any of these are written, but that is packaging, not a finding — a reviewer
will read it as WiSE-FT's α-sweep with a constraint bolted on. The one genuinely missing artifact
is a standardized **promptability-retention benchmark** (held-out SA-1B promptable eval + reporting
protocol) that everyone fine-tuning SAM could be required to report.

**Confidence.** High (0.85).

**R2 attack cite.** HQ-SAM, arXiv:2306.01567 Table 9 (encoder LoRA/adapter zero-shot degradation
already measured); WiSE-FT for the dial.

**Verdict: MUTATE** — build the retention benchmark/instrument, not the constrained optimizer.

---

## VFM-A0077 — Learned LoRA update effective rank << nominal; truncate

**Closest prior.** Post-Optimization Adaptive Rank Allocation for LoRA (PARA, 2026) —
https://arxiv.org/abs/2604.27796. Also AdaLoRA (https://arxiv.org/abs/2303.10512, ICLR 2023);
LoRA-Squeeze (https://arxiv.org/abs/2602.10993, 2026); PHLoRA
(https://arxiv.org/abs/2509.10971, 2025); SpectralLoRA (https://arxiv.org/abs/2604.10649, 2026).

**Difference.** None — both halves of the idea are published, separately and together. PARA is
literally "data-free post-hoc SVD truncation of trained LoRA with a global singular-value
threshold," reporting **75–90% parameter reduction while preserving performance across vision and
language benchmarks**, and explicitly recommending the proposed recipe (train at high rank, rely on
post-hoc compression to discard extra ranks). LoRA-Squeeze does the same via randomized SVD, both
post-hoc and in-training. AdaLoRA owns the training-time version with importance-based singular
value pruning on a cubic budget schedule. SpectralLoRA supplies the "updates are spectrally
redundant" measurement (33% of DCT coefficients carry 90% of energy).

**Remaining novelty.** Zero. Even a vision-only/dense-only replication is pre-empted: PARA
evaluates on vision benchmarks.

**Confidence.** Very high (0.95).

**R2 attack cite.** PARA, arXiv:2604.27796.

**Verdict: KILL.**

---

## VFM-A0148 — High-norm outlier tokens in ViT VFMs hurt dense probes; renormalize

**Closest prior.** Vision Transformers Need Registers (ICLR 2024) —
https://arxiv.org/abs/2309.16588. The fix-without-retraining: Vision Transformers Don't Need
Trained Registers (2025) — https://arxiv.org/abs/2506.08010.

**Difference.** None. Darcet et al. identify high-norm tokens in low-informative background
regions, show they carry global information at the cost of spatial detail, demonstrate the harm to
**dense prediction specifically**, and fix it with register tokens — setting SOTA for
self-supervised dense prediction. The proposed "renormalize instead of retrain" mutation is itself
already published: test-time registers identify the sparse "register neurons" responsible and shift
their high-norm activations into an added untrained token, "achieving results comparable to models
explicitly trained with register tokens," extended to off-the-shelf VLMs.

**Remaining novelty.** Zero. Both the diagnosis slot and the training-free-remedy slot are taken.

**Confidence.** Very high (0.95).

**R2 attack cite.** arXiv:2309.16588 (diagnosis + dense harm); arXiv:2506.08010 (training-free fix).

**Verdict: KILL.**

---

## VFM-A0153 — Linear map CLIP patches → DINOv2 geometry recovers correspondence

**Closest prior.** Talk2DINO: Talking to DINO (2024) — https://arxiv.org/abs/2411.19331. Also
Probing the 3D Awareness of Visual Foundation Models (https://arxiv.org/abs/2404.08636, CVPR 2024);
A Tale of Two Features (https://arxiv.org/abs/2305.15347, NeurIPS 2023).

**Difference.** Talk2DINO maps CLIP embeddings into DINOv2's patch space with a learned map and
frozen backbones — but it maps **text** embeddings, for open-vocabulary segmentation, and the map is
nonlinear (two affine transforms separated by tanh). El Banani et al. establish the gap this idea
exploits (DINOv2 encodes depth/normals, CLIP "exhibits very poor performance") — importantly, their
**correspondence** evaluation is *zero-shot nearest-neighbour on frozen features, with no learned
probe*, unlike their depth/normal experiments which do use trained dense probes. A Tale of Two
Features fuses (concatenate + L2-normalize, α=0.5) rather than mapping one space into the other.

**NOT FOUND:** a **linear** map from CLIP **patch** tokens into DINOv2 patch space, evaluated on
semantic/geometric correspondence.

**Remaining novelty.** The strongest crack in this batch. It is a clean linear-identifiability
question with a real bifurcation: if a linear map recovers DINOv2-level correspondence from CLIP
patches, El Banani's conclusion weakens from "CLIP lacks geometry" to "CLIP's geometry is linearly
present but unread by NN matching"; if it fails, that is a genuine negative result about
representational content. Cheap to run on SPair-71k / PF-Pascal with the probe3d and sd-dino
codebases.

**Confidence.** Medium-high (0.7) that the specific experiment is unoccupied. Main risk: reviewers
compress it to "Talk2DINO without text."

**R2 attack cite.** Talk2DINO, arXiv:2411.19331 (learned CLIP→DINOv2 mapping exists);
arXiv:2404.08636 (the CLIP-vs-DINOv2 geometry gap is already characterized).

**Verdict: MUTATE (strongest survivor)** — must be framed as linear identifiability with the
nonlinear map and the fusion baseline both in the table, and must state the negative result as a
publishable outcome up front.

---

## ASM-A0073 — Prompt adaptation more brittle than LoRA under covariate shift (vision/seg)

**Closest prior.** Choice of PEFT Technique in Continual Learning: Prompt Tuning is Not All You
Need (2024) — https://arxiv.org/abs/2406.03216. Also Lessons and Insights from a Unifying Study of
PEFT in Visual Recognition (https://arxiv.org/abs/2409.16434, 2024); Probing OOD Robustness of LMs
with PETL (https://arxiv.org/abs/2301.11660, 2023); Rein (https://arxiv.org/abs/2312.04265, CVPR
2024).

**Difference.** The ranking is already established, and on vision backbones. The continual-learning
paper trains ViT-B/16 on Split CIFAR-100 and DomainNet and finds prompt tuning "lags behind that of
LoRA by a significant margin" at comparable parameter budgets, explicitly attacking the unablated
choice of prompt tuning. The PEFT visual-recognition study covers PEFT-vs-full-FT robustness under
ImageNet-V2/S/R/A shift and shows WiSE overturns the PEFT advantage. The PETL paper finds "LoRA is
the most stable during learning and prefix-tuning fluctuates severely." Rein compares fine-tuning
strategies across five VFMs for domain-generalized segmentation.

**Remaining novelty.** The dense/segmentation instantiation under controlled covariate shift is not
directly done, but the expected result is already predicted by three papers, so a confirmation has
low value. Any real contribution has to be **mechanistic** — why prompt capacity fails under shift
(e.g. prompts cannot re-route early-layer input-level statistics, which is exactly the regime
Surgical Fine-Tuning, https://arxiv.org/abs/2210.11466, shows requires early-block tuning).

**Confidence.** High (0.8) that the claim is prior.

**R2 attack cite.** arXiv:2406.03216 — "prompt tuning underperforms LoRA; we showed this on ViTs."

**Verdict: MUTATE** — mechanism-first (shift-type × adaptation-locus interaction), or drop.

---

## ASM-A0021 — Overtrained-smaller models beat compute-optimal on dense downstream

**Closest prior.** Gadre et al., Language models scale reliably with over-training and on downstream
tasks (2024) — https://arxiv.org/abs/2403.08540. Vision side: Getting ViT in Shape: Scaling Laws for
Compute-Optimal Model Design (SoViT, NeurIPS 2023) — https://arxiv.org/abs/2305.13035.

**Difference.** Gadre et al. own over-training scaling laws and the perplexity→downstream-error
power law, but in language. SoViT owns the vision compute-optimal story (SoViT-400m/14 matching
ViT-g/14 at <½ inference cost; optimal parameter count grows only ~2.5× per 10× compute) — **and it
flags dense prediction as its own open limitation**, reporting 43.5 / 43.7 / 44.8 PQ for ViT-L/16 /
SoViT-400m/14 / ViT-g/14 on COCO panoptic and concluding "dense segmentation tasks can be a
limitation of the proposed optimal model shape, and a different model shape might be derived in
this domain. We leave this investigation for future work."

**Remaining novelty.** Real and explicitly invited by SoViT — the dense-task shape/over-training
frontier is unclaimed. **NOT FOUND:** any paper deriving compute-optimal or over-trained scaling for
dense downstream transfer. But the honest blocker is cost: this requires pretraining a grid of
backbones, which is not a Windows1-scale experiment unless run on an existing public checkpoint
family (e.g. a released over-trained/compute-optimal ViT suite) rather than fresh pretraining.

**Confidence.** High (0.8) that the dense question is open; low (0.3) that it is executable here.

**R2 attack cite.** SoViT, arXiv:2305.13035 §panoptic — "we already reported dense as a limitation";
Gadre, arXiv:2403.08540 for the over-training machinery.

**Verdict: MUTATE** — reframe as secondary analysis over an existing public checkpoint grid, gated
on that grid existing. Otherwise infeasible.

---

## ASM-A0109 — Seed variance of dense FT exceeds published method gaps

**Closest prior.** nnU-Net Revisited: A Call for Rigorous Validation in 3D Medical Image
Segmentation (MICCAI 2024) — https://arxiv.org/abs/2404.09556. Also Bouthillier et al., Accounting
for Variance in Machine Learning Benchmarks (MLSys 2021) — https://arxiv.org/abs/2103.03098;
Picard, torch.manual_seed(3407) is all you need (2021) — https://arxiv.org/abs/2109.08203.

**Difference.** The *conclusion* is heavily pre-figured but the *specific measurement is not made
on this population.* nnU-Net Revisited shows claimed segmentation gains evaporate under rigorous
validation — but attributes this to inadequate baselines, insufficient datasets and unequal compute,
not seed variance, and its scope is 3D medical CNN/Transformer/Mamba architectures, not VFM
adaptation. Bouthillier decomposes variance sources (finding data sampling dominates, with model
init under 50% of bootstrap variance) on small general benchmarks. Picard scans seeds on CV
classification. **NOT FOUND:** a seed-variance study of dense fine-tuning of vision foundation
models (SAM/DINOv2 adapters, LoRA-seg, PEFT-seg) benchmarked against the published inter-method
gaps in that literature.

**Remaining novelty.** Low-glamour, high-service, and genuinely unoccupied. Strengthened by two
facts already in the record: the FSS foundation-model benchmark found linear/SVF/LoRA/full-FT
"yield comparable results between them," and Rein reports ~1% trainable parameters beating full FT
— i.e. the reported gaps in this literature are small enough that seed variance is a live
explanation. Bouthillier's finding that data sampling dominates initialization also means the
protocol must randomize splits, not just seeds, or the headline will be wrong.

**Confidence.** Medium-high (0.7) that a scoped version is publishable — as a
benchmark/reproducibility artifact, not a headline result.

**R2 attack cite.** arXiv:2404.09556 — "we already showed segmentation method claims don't survive
rigorous validation"; arXiv:2103.03098 for the variance-decomposition methodology you must adopt.

**Verdict: SURVIVE (weak)** — scope to VFM dense adaptation, randomize splits + seeds per
Bouthillier, and position against nnU-Net Revisited rather than ignoring it.

---

## Summary table

| ID | Verdict | Closest prior | Conf. |
|---|---|---|---|
| VFM-A0022 | **KILL** | TETRIS, arXiv:2402.06132 | 0.90 |
| VFM-A0051 | MUTATE | arXiv:2606.14755 / SANSA / FrozenSeg | 0.85 |
| VFM-A0028 | MUTATE | SAM-U, arXiv:2307.04973 | 0.60 |
| VFM-A0166 | MUTATE | arXiv:2310.09562 (ICLR 2024) | 0.85 |
| VFM-A0168 | **KILL** | RClicks, arXiv:2410.11722 | 0.95 |
| VFM-A0121 | MUTATE | arXiv:2401.11311 / LP-FT | 0.75 |
| VFM-A0263/0274 | MUTATE | HQ-SAM Table 9 / WiSE-FT | 0.85 |
| VFM-A0077 | **KILL** | PARA, arXiv:2604.27796 | 0.95 |
| VFM-A0148 | **KILL** | Registers + test-time registers | 0.95 |
| VFM-A0153 | MUTATE (best) | Talk2DINO, arXiv:2411.19331 | 0.70 |
| ASM-A0073 | MUTATE | arXiv:2406.03216 | 0.80 |
| ASM-A0021 | MUTATE | SoViT, arXiv:2305.13035 | 0.80 |
| ASM-A0109 | SURVIVE (weak) | nnU-Net Revisited, arXiv:2404.09556 | 0.70 |

## Verified NOT FOUND gaps (the only real novelty in this batch)

1. Cross-**prompt-modality** (click vs box) disagreement as a label-free segmentation error
   predictor. All prior varies prompts within one type.
2. SA-1B ↔ COCO/ADE20K/LVIS image-level near-duplicate overlap statistics.
3. A **linear** map from CLIP **patch** tokens into DINOv2 patch space, evaluated on correspondence.
4. Labeled-set-size frozen/unfrozen crossover for dense tasks paired with an *a priori* predictive
   selector.
5. Compute-optimal / over-training scaling laws targeting **dense** downstream transfer (explicitly
   left open by SoViT).
6. Seed + split variance of **VFM dense fine-tuning** measured against that literature's published
   method gaps.
