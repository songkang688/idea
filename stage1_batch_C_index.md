# Stage 1 — Batch C Index

PI: Windows5 · Autonomous Research Idea Evolution, Stage 1.
Source file: `stage1_batch_C_ideas.md`

## Count

- **Total ideas: 340** (IDEA-C-0001 … IDEA-C-0340), sequential, no gaps or duplicates.
- Every idea includes: Idea ID, One-sentence idea, Problem, Core Hypothesis (falsifiable), Why Important, Why Possibly Novel, Minimal Experiment, Main Risk.
- Batch is distinct from SAM-centric and dataset-centric batches; no "A+B module", "use transformer", "new attention", or hypothesis-free "apply SAM to X" ideas were included.

## Clusters

| Cluster | Theme | ID Range | Count |
|---|---|---|---|
| C1 | PEFT failure & when full fine-tuning is necessary | IDEA-C-0001 – 0030 | 30 |
| C2 | Catastrophic forgetting in sequential medical/domain adaptation | IDEA-C-0031 – 0060 | 30 |
| C3 | VLMs for dense prediction: alignment vs localization mismatch | IDEA-C-0061 – 0090 | 30 |
| C4 | Prompt learning pathologies | IDEA-C-0091 – 0118 | 28 |
| C5 | Weak/semi/self-supervised segmentation: scientific gaps | IDEA-C-0119 – 0148 | 30 |
| C6 | Medical vision foundation models: what they still cannot do | IDEA-C-0149 – 0178 | 30 |
| C7 | Object detection vs segmentation representation conflict | IDEA-C-0179 – 0204 | 26 |
| C8 | Boundary quality as a scientific problem | IDEA-C-0205 – 0232 | 28 |
| C9 | Ambiguous labels / inter-rater disagreement as signal | IDEA-C-0233 – 0260 | 28 |
| C10 | Foundation-model tokenization / resolution / memory artifacts | IDEA-C-0261 – 0288 | 28 |
| C11 | Community beliefs that may be false (testable) | IDEA-C-0289 – 0314 | 26 |
| C12 | Cheap experiments that could overturn implicit assumptions | IDEA-C-0315 – 0340 | 26 |
| | **Total** | | **340** |

Cross-cluster themes that recur (useful for Stage 2 evolution): mechanism-vs-artifact adjudication (0011, 0098, 0101, 0121, 0148, 0296); measurement/statistics repair of benchmarks (0067, 0094, 0110, 0210, 0229, 0245, 0287, 0321, 0330, 0333, 0339, 0340); signed/structured error analysis replacing scalar metrics (0177, 0190, 0216, 0217, 0218, 0227, 0228); annotation process as an object of study (0139, 0212, 0242, 0247, 0251, 0252, 0254); data-statistics → model-behavior causal chains (0069, 0080, 0086, 0158, 0285).

## 20 Most Surprising Ideas

Selected for counterintuitive hypotheses — if true, each would change a default belief or practice.

1. **IDEA-C-0023** — PEFT can add capabilities but cannot *unlearn* misleading pretrained cues; suppression tasks structurally require full fine-tuning.
2. **IDEA-C-0040** — Most "catastrophic forgetting" under site shift is retrieval failure, not erasure: ~20 old images recover most of it in a few steps.
3. **IDEA-C-0050** — Trivial checkpoint weight averaging may beat dedicated continual-learning methods in medical segmentation at zero overhead.
4. **IDEA-C-0056** — Continuously running test-time adaptation is a slow poison: cumulative "TTA drift" degrades deployed models monotonically.
5. **IDEA-C-0061** — CLIP patch tokens may carry more information about the *image-level* label than about their own receptive field ("global leakage").
6. **IDEA-C-0072** — A text-only model (never seeing the image) may recover a nontrivial share of reported referring-segmentation performance.
7. **IDEA-C-0078** — Decoders trained on frozen CLIP features may succeed by actively *undoing* the text alignment the pipeline is built on.
8. **IDEA-C-0091** — Learned soft prompts are dataset fingerprints: the training dataset is identifiable from the prompt vector alone.
9. **IDEA-C-0113** — "Prompt collapse": class prompts converge toward each other during long training, silently destroying fine-grained discrimination.
10. **IDEA-C-0124** — Self-training collapses multi-rater ambiguity into one annotator's style, discarding exactly the distributional signal medicine needs.
11. **IDEA-C-0132** — Pixel-contrastive SSL on registered medical images can minimize its loss by encoding *position*, not anatomy — a silent shortcut.
12. **IDEA-C-0162** — Report-trained medical FMs learn the distribution of *reported* findings, systematically missing unreported incidentals.
13. **IDEA-C-0173** — Foundation models exhibit "salience suppression": the presence of a prominent lesion measurably lowers detection of others in the same image.
14. **IDEA-C-0192** — Mask-classification segmentation architectures functionally re-implement detection: queries behave like boxes and inherit detection's failures.
15. **IDEA-C-0212** — The annotation *tool* (polygon vs brush vs level-set) is identifiable from ground-truth boundary statistics and confers a tool-matching score bonus.
16. **IDEA-C-0214** — Networks know boundaries better than their masks show: sub-pixel boundary readout from logits beats argmax against high-res truth.
17. **IDEA-C-0234** — Consensus fusion (majority vote/STAPLE), the default preprocessing for multi-rater data, is where ambiguity information dies — measurably.
18. **IDEA-C-0252** — Adjudicated consensus is statistically a *new rater*: panel labels differ from every individual and from statistical fusion in consistent directions.
19. **IDEA-C-0287** — Floating-point/kernel numerics (FlashAttention, bf16) flip boundary pixels at rates comparable to published method gains — an unacknowledged variance term.
20. **IDEA-C-0329** — Replacing the text encoder with class-mean image prototypes may leave "language-driven" segmentation unchanged — language as mere class indexing.

## 20 Cheapest-to-Falsify Ideas

Selected for minimal experiments runnable in hours-to-days with public models/data, mostly inference-only or single short trainings.

1. **IDEA-C-0316** — Random-frozen prompts vs learned prompts (inference + light training on existing benchmarks).
2. **IDEA-C-0317** — Train on 8× downsampled masks; measure benchmark boundary-sensitivity ceiling (one short training per benchmark).
3. **IDEA-C-0318** — Image-free prior-only baseline (atlas/position statistics); compute benchmark prior floors (no deep training).
4. **IDEA-C-0325** — Histogram matching as a domain-adaptation baseline (preprocessing + evaluation only).
5. **IDEA-C-0326** — Slice-order permutation test on published 3D models (inference only).
6. **IDEA-C-0332** — Mask-the-lesion occlusion audit of medical detectors (inference + inpainting only).
7. **IDEA-C-0334** — Evaluate public models at 2× training resolution; ranking-stability audit (inference only).
8. **IDEA-C-0339** — Re-score models against ±1-pixel morphologically perturbed ground truth (evaluation only).
9. **IDEA-C-0330** — Perturbation-derived noise floors for boundary metrics (inference only).
10. **IDEA-C-0338** — Zero skip connections at inference in trained U-Nets; per-class reliance profiles (inference only).
11. **IDEA-C-0322** — Segmentation logit lens: early-layer readouts vs final predictions (linear probes on frozen models).
12. **IDEA-C-0323** — Per-class channel-ablation sparsity probes on trained segmenters (no training).
13. **IDEA-C-0335** — Linear probe vs full decoder sufficiency test on frozen encoders (linear probes only).
14. **IDEA-C-0328** — Embedding-based train/test near-duplicate contamination audit (inference + nearest neighbors).
15. **IDEA-C-0321** — 50-image, 3-rater test-set re-annotation to bound leaderboard noise (small annotation study, no training).
16. **IDEA-C-0315** — Scramble test for "global context" module claims (inference on public checkpoints).
17. **IDEA-C-0093** — Nearest-word prompt interpretability audit: projection collapse + seed instability (light prompt trainings).
18. **IDEA-C-0067** — Prompt-paraphrase variance decomposition of open-vocab segmentation leaderboards (inference only).
19. **IDEA-C-0253** — TTA-disagreement vs human-disagreement correspondence on existing multi-rater benchmarks (inference only).
20. **IDEA-C-0149** — Laterality flip-consistency probe for medical foundation models (probing frozen features).

## Notes

- No experimental results are claimed anywhere in this batch; all hypotheses are stated as falsifiable predictions with named minimal experiments and main risks.
- No specific papers are cited with invented findings; references to method families (LoRA, CoOp, DETR, nnU-Net, MAE, Prob U-Net, FlashAttention, etc.) are to widely known public method classes only.
