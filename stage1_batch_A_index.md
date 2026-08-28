# Stage 1 — Batch A: Index

**PI:** Windows5
**File indexed:** `stage1_batch_A_ideas.md`
**Total idea count:** 340 (IDEA-A-0001 … IDEA-A-0340, verified contiguous, 8 required fields present for every idea)

---

## 1. Clusters (17 groups)

| # | Cluster name | ID range | Count |
|---|--------------|----------|-------|
| 1 | SAM / SAM2 Failure Modes & Mechanistic Analysis | IDEA-A-0001 … 0030 | 30 |
| 2 | Prompt Sensitivity as a Scientific Object | IDEA-A-0031 … 0050 | 20 |
| 3 | PEFT & Fine-Tuning Instability | IDEA-A-0051 … 0075 | 25 |
| 4 | Catastrophic Forgetting & Continual Adaptation | IDEA-A-0076 … 0090 | 15 |
| 5 | Medical Segmentation: Limits, Assumptions, Clinical Validity | IDEA-A-0091 … 0120 | 30 |
| 6 | Smoke & Fire Segmentation: Physics, Ground Truth, Deployment | IDEA-A-0121 … 0140 | 20 |
| 7 | Transparent, Mirror & Ambiguous Object Segmentation | IDEA-A-0141 … 0160 | 20 |
| 8 | Small Objects & Boundary Quality | IDEA-A-0161 … 0180 | 20 |
| 9 | VLMs for Dense Prediction: Grounding, Hallucination, Language Limits | IDEA-A-0181 … 0200 | 20 |
| 10 | Foundation-Model Representations & Unproven Community Assumptions | IDEA-A-0201 … 0225 | 25 |
| 11 | Valuable Negative Results & Falsification Studies | IDEA-A-0226 … 0245 | 20 |
| 12 | Few-Shot & Zero-Shot Segmentation | IDEA-A-0246 … 0260 | 15 |
| 13 | Weakly-, Semi- & Self-Supervised Segmentation | IDEA-A-0261 … 0280 | 20 |
| 14 | Synthetic Data & Generative Training for Dense Tasks | IDEA-A-0281 … 0295 | 15 |
| 15 | Domain Adaptation & Distribution Shift | IDEA-A-0296 … 0310 | 15 |
| 16 | Object Detection Failure Modes | IDEA-A-0311 … 0325 | 15 |
| 17 | Evaluation Methodology & Benchmark Science | IDEA-A-0326 … 0340 | 15 |

**Coverage of the requested angles** (each angle appears in multiple clusters):
existing-method failure modes (1, 8, 9, 12, 13, 15, 16), foundation-model failure (1, 9, 10), SAM/SAM2 failure (1, and 0128, 0145, 0154, 0114, 0267), medical limitation (5, plus 0160, 0292), smoke/fire/transparent/ambiguous (6, 7, plus 0319, 0287, 0290), prompt sensitivity (2, plus 0092, 0038), fine-tuning instability (3), catastrophic forgetting (4, plus 0068, 0086), small object/boundary (8, plus 0096, 0161–0180), unproven community assumptions (10, plus 0093, 0100, 0111, 0134, 0168, 0221), valuable negative results (11, plus 0107, 0128, 0134, 0300, 0325), simple counter-intuitive hypotheses (0013, 0021, 0049, 0055, 0074, 0078, 0131, 0142, 0157, 0187, 0203, 0245, 0300, 0336, 0340).

---

## 2. Twenty Most Surprising Ideas (counter-intuitive if the hypothesis holds)

| Rank | ID | Why surprising |
|------|----|----------------|
| 1 | IDEA-A-0245 | Most of a decade of segmentation "architecture progress" may be training recipe: a 2015 U-Net with a 2026 recipe could close >60% of the gap. |
| 2 | IDEA-A-0300 | Frozen DINOv2 features with a source-trained head may beat the entire accumulated UDA literature with zero target data. |
| 3 | IDEA-A-0142 | Adding depth input may *hurt* transparent-object segmentation — and the depth sensor's failure pattern may itself be the best transparency cue. |
| 4 | IDEA-A-0203 | "Emergent object segmentation" in self-supervised ViTs may be an echo of random-crop augmentation statistics, not discovered objecthood. |
| 5 | IDEA-A-0013 | SAM2 may be *worse* than SAM1 at fine static-image boundaries — the newest model isn't strictly better. |
| 6 | IDEA-A-0187 | Referring segmentation under negation may be systematically *worse than chance* — models confidently select the negated object. |
| 7 | IDEA-A-0078 | Catastrophic forgetting may be mostly output-readout drift: the "lost" capabilities may still sit linearly decodable in the features. |
| 8 | IDEA-A-0055 | Much of the vision-PEFT literature's advantage may be reproducible by plain layer-wise learning-rate decay on full fine-tuning. |
| 9 | IDEA-A-0123 | State-of-the-art fire segmenters may be color detectors with extra steps — blue gas flames missed, sunsets flagged. |
| 10 | IDEA-A-0176 | Part of "small objects are hard" may be that benchmark JPEG compression already deleted the small-object signal before any model saw it. |
| 11 | IDEA-A-0118 | Medical models may hallucinate surgically removed organs — segmenting "where organs usually are," a silent patient-safety failure. |
| 12 | IDEA-A-0157 | On near-invisible clean glass, humans may beat the best models by >30 points — proving competence, not information, is the bottleneck. |
| 13 | IDEA-A-0049 | Lay language ("collapsed lung") may prompt general medical VLM grounding better than correct expert terminology ("pneumothorax"). |
| 14 | IDEA-A-0021 | SAM may be functionally achromatic — color-defined boundaries invisible to a model everyone treats as a general perceptual front-end. |
| 15 | IDEA-A-0100 | Standard flip test-time augmentation may systematically *harm* lateralized anatomy in medical pipelines — a harmful default in challenge winners. |
| 16 | IDEA-A-0041 | Chain-of-thought reasoning may not causally change where VLMs ground at all — the text may be post-hoc rationalization of a fixed visual pathway. |
| 17 | IDEA-A-0131 | Calibrated thermal-only models may match published RGB+IR fusion results — the fusion literature's marginal value may be confined to a tiny regime. |
| 18 | IDEA-A-0170 | Implicit-neural mask decoders' celebrated "sub-pixel boundaries" may be hallucinated smoothness that matches annotator style, not recovered information. |
| 19 | IDEA-A-0029 | SAM-assisted annotation may be contaminating the field's future ground truth — new datasets inheriting SAM's competence profile in a feedback loop. |
| 20 | IDEA-A-0074 | LoRA dropout — copied into thousands of configs — may be a pure placebo for dense-prediction fine-tuning. |

---

## 3. Twenty Cheapest-to-Falsify Ideas (inference-only or small-annotation studies; no large training runs)

| Rank | ID | Why cheap |
|------|----|-----------|
| 1 | IDEA-A-0021 | Hue-rotate/grayscale existing images, run frozen SAM, compare IoU — a day of inference. |
| 2 | IDEA-A-0022 | Box-vs-point disagreement as failure detector: run SAM twice per object on existing GT datasets, compute AUROC. |
| 3 | IDEA-A-0016 | Calibration audit of SAM's predicted-IoU head: collect (predicted, actual) pairs on existing datasets, plot reliability diagrams. |
| 4 | IDEA-A-0031 | Paraphrase-variance audit: re-run existing open-vocab checkpoints with 10 prompt variants per class. |
| 5 | IDEA-A-0032 | Vocabulary composition/order sensitivity: same checkpoints, permuted and padded class lists. |
| 6 | IDEA-A-0043 | Prompt length-vs-content dissociation: factorial prompt battery, inference only. |
| 7 | IDEA-A-0044 | 80-template pruning: greedy template selection over cached text embeddings — nearly free. |
| 8 | IDEA-A-0046 | One-character typo attack surface: enumerate edits for 100 class names, measure IoU drops. |
| 9 | IDEA-A-0050 | Prompt-embedding interpolation phase transitions: 200 prompt pairs × 20 steps of inference. |
| 10 | IDEA-A-0008 | Click-position sensitivity map: grid of prompts over 200 objects with frozen SAM. |
| 11 | IDEA-A-0025 | Modal-vs-amodal behavior: prompt SAM on existing amodal benchmarks, measure occluded-region inclusion. |
| 12 | IDEA-A-0027 | Hole-filling bias: assemble genus≥1 objects from existing datasets, run SAM, count filled holes. |
| 13 | IDEA-A-0038 | Prompt-encoding aliasing: sub-patch click offsets, Fourier test on IoU periodicity — inference only. |
| 14 | IDEA-A-0047 | Everything-mode blind spots: run grid prompting on LVIS, stratify recall by size/nesting. |
| 15 | IDEA-A-0128 | SAM-on-smoke prompt-strategy audit: existing smoke datasets, existing checkpoints, one small U-Net baseline. |
| 16 | IDEA-A-0145 | SAM transparency bimodality: dense prompt sweeps on Trans10K-class data, classify outputs. |
| 17 | IDEA-A-0182 | VLM counting psychophysics: controlled count ladders, API-level inference on existing VLMs. |
| 18 | IDEA-A-0185 | Hallucinated-mask absence benchmark: present/absent prompt triads over densely annotated existing datasets. |
| 19 | IDEA-A-0196 | Ordinal referring selection ("second largest"): controlled scenes, inference across existing models. |
| 20 | IDEA-A-0340 | Bootstrap leaderboard confidence: pure re-analysis of released per-image predictions — no model runs at all. |

---

## 4. Notes

- No experimental results are claimed anywhere in the batch; every idea specifies a falsifiable hypothesis and a minimal experiment that could refute it.
- Citations are restricted to well-known real systems/papers (SAM, SAM2, CLIP, DINOv2, MedSAM, nnU-Net, LoRA, BitFit, CoOp, Mask2Former, SegFormer, DETR, SegGPT/Painter, TENT, WiSE-FT, SynthSeg, Trans10K, ClearGrasp, COD10K, LVIS, COCO, BraTS, DRIVE/STARE, FSC-147, GTA→Cityscapes, LAION, SA-1B); speculative quantities are marked HYPOTHESIS in place.
- Cross-references between ideas (e.g., IDEA-A-0016 ↔ 0070, 0121 ↔ 0122 ↔ 0132 ↔ 0319, 0029 ↔ 0219 ↔ 0267) indicate coherent research programs that can share infrastructure in later stages.
