# Stage 3 — Prior-Art Attack Queue (Windows5, pool-200)

**Purpose:** ranked order for the Stage-3 prior-art killsheet over all 200 pool ideas — **hardest/most-at-risk novelty first**, per the auditor's finding that self-assessed novelty (Unp/NP columns) is the least reliable signal in the score sheets and that survivors, not just candidates, must be searched.
**Search protocol per idea:** search the merged framing *and* each constituent Stage-1 framing; record verdict {OPEN, CARVE (reposition), KILLED (pre-empted)} with citations; protected entries (HR/HRHR/CI/CF/REV) may be killed **only** on direct prior-art hits, not on taste.

**Tiers:** T1 (1–25) documented or strongly suspected overlap — attack immediately, before any experiment spend. T2 (26–73) crowded, fast-moving audit territory (SAM audits, PEFT deflation, CLIP-dense probing, TTA) — one existing paper could force re-scoping. T3 (74–131) standard verification. T4 (132–175) distinctive designs, moderate risk. T5 (176–200) most-distinctive bets (physics supervision, partnership-gated data, HRHR wildcards) — attack last; expected to survive.

## Tier 1 — kill attempts 1–25 (highest priority)

| Rank | Pool ID | Sources | Why attack first |
|---|---|---|---|
| 1 | **W5-012** (A-0340) | A-0340 | Verified pre-emption: Maier-Hein et al. (Nat. Commun. 2018) bootstrapped challenge rankings (first-rank stability 9–21%); the natural-image generalization and 'fiction fraction' framing are the only open carve. |
| 2 | **W5-023** (A-0245) | A-0245 | Verified pre-emption: nnU-Net Revisited (arXiv:2404.09556) already shows recipe>architecture for medical 3D; only the decade-spanning compute-matched natural-image arm is open. |
| 3 | **W5-129** (A-0013) | A-0013 | Verified pre-emption: arXiv:2408.04212 and 2408.00756 already report SAM2 ≤ SAM1 on 2D/medical; verify the static natural-image fine-boundary carve before any investment. |
| 4 | **W5-010** (MERGE-15) | A-0091 + B-0082 + C-0321  (= MERGE-15‡) | Rank-stability-under-relabeling sits next to the Maier-Hein/Wiesenfarth toolkit line; search challenge meta-analyses before funding the annotation budget. |
| 5 | **W5-024** (MERGE-29) | A-0226 + C-0340  (= MERGE-29) | Tuned-baseline replication territory partially occupied (nnU-Net Revisited; leakage/reproducibility surveys); confirm no existing compute-matched inflation estimate for the module-contribution genre. |
| 6 | **W5-124** (A-0097) | A-0097 | Dice-loss miscalibration is documented in isolated medical studies (idea concedes); confirm the imbalance-scaling law and CE→Dice schedule are unclaimed. |
| 7 | **W5-093** (MERGE-16) | A-0142 + B-0159  (= MERGE-16) | ClearGrasp-lineage robotics work already exploits depth invalidity as a transparency cue; verify the harvested-corpus and sign-of-contribution study are unclaimed. |
| 8 | **W5-015** (MERGE-28) | B-0012 + C-0328  (= MERGE-28) | Patient-level leakage / dedup auditing is an established medical-imaging literature; the few-shot-specific predictable-shrinkage law is the only likely-open part. |
| 9 | **W5-087** (B-0083) | B-0083 | Several medical-SAM evaluation papers already vary point/box protocols and note ranking effects; confirm the cross-protocol rank-correlation index is unclaimed. |
| 10 | **W5-074** (MERGE-22) | A-0031 + C-0067  (= MERGE-22) | Prompt/template sensitivity is well studied for CLIP classification and some OV-seg papers; check whether prompt-resampled leaderboard CIs already exist. |
| 11 | **W5-065** (C-0325) | C-0325 | Histogram matching is a decades-old DA baseline; search for a published 'intensity alignment closes most of the cross-site gap' audit on modern benchmarks. |
| 12 | **W5-193** (C-0101) | C-0101 | Entropy-minimization equivalence deflations are a known genre; search 2023–26 test-time prompt-tuning analyses before running. |
| 13 | **W5-030** (A-0055) | A-0055 | PEFT-vs-tuned-full-FT fairness studies exist; verify 'LLRD alone closes the gap' is unclaimed for dense prediction. |
| 14 | **W5-037** (MERGE-19) | B-0270 + C-0020  (= MERGE-19) | Stem/early-layer retraining is widespread repo folklore; search for any controlled multi-modality ceiling study. |
| 15 | **W5-048** (MERGE-20) | A-0078 + C-0034  (= MERGE-20) | 'Forgetting is superficial / recoverable by probing' has classification-era antecedents; verify the dense zero-shot version is open. |
| 16 | **W5-049** (MERGE-21) | A-0089 + C-0040  (= MERGE-21) | Relearning-speed and rewinding literatures (CL, unlearning) are adjacent; verify the time-constant/refresh-schedule framing is unclaimed. |
| 17 | **W5-052** (C-0050) | C-0050 | Weight averaging (soups, WiSE-FT, EMA) is heavily mined; check sequential-checkpoint averaging as a CL baseline specifically. |
| 18 | **W5-123** (B-0084) | B-0084 | The 2023–26 SAM-audit flood may already include IoU-head OOD calibration; an hour of search before an afternoon of compute. |
| 19 | **W5-101** (A-0128) | A-0128 | SAM-fails-on-smoke reports exist; the density-conditioned shrinkage law is the carve that must be verified as open. |
| 20 | **W5-057** (MERGE-06) | A-0303 + B-0057  (= MERGE-06) | ViT/LayerNorm test-time normalization papers 2022–25 are close neighbors; verify the recovery-fraction-as-diagnostic framing. |
| 21 | **W5-068** (A-0187) | A-0187 | VLM negation benchmarks emerged 2024–25; verify the dense anti-accuracy result and fusion-vs-encoding localization are unclaimed. |
| 22 | **W5-080** (C-0061) | C-0061 | SCLIP/ClearCLIP-style analyses already blame global components in CLIP patch tokens; the quantitative leakage decomposition may be published. |
| 23 | **W5-026** (MERGE-11) | A-0250 + B-0024  (= MERGE-11) | 'Simple baselines beat FSS meta-learning' is partially published; the cross-domain crossover map is the residual claim. |
| 24 | **W5-132** (A-0203) | A-0203 | SSL crop-statistics/object-centric bias studies exist; verify the causal decentered-cropping retraining intervention is unclaimed. |
| 25 | **W5-028** (C-0094) | C-0094 | Seed-variance meta-analyses exist in adjacent subfields; check for prompt-learning-specific ones before running. |

## Tier 2 — crowded fast-moving territory (26–73)

| Rank | Pool ID | Sources | Search target (one-liner) |
|---|---|---|---|
| 26 | W5-001 (MERGE-01) | A-0029 + B-0019  (= MERGE-01) | Within-annotator crossover (scratch / SAM-assisted / correct-the-proposal) measuring anchoring and agreement-with-SAM inflation, plus student… |
| 27 | W5-002 (A-0007) | A-0007 | Determine how much of SAM's mask granularity behavior is an imprint of the SA-1B annotation *protocol* rather than a property of images. |
| 28 | W5-003 (MERGE-09) | A-0267 + B-0329 + C-0310  (= MERGE-09‡) | Students trained on weak-teacher/SAM labels (hard or soft) inherit spatially correlated bias-type errors and surpass variance-type errors;… |
| 29 | W5-005 (B-0191) | B-0191 | Measure the generational dynamics of pipelines where models pseudo-label data used to train successor models (the standard auto-labeling loop),… |
| 30 | W5-004 (B-0001) | B-0001 | Characterize SAM-generated pseudo-label noise as spatially structured (boundary-biased, systematically dilated/eroded per texture class) and test… |
| 31 | W5-006 (B-0320) | B-0320 | Treat SAM everything-mode outputs as what they statistically are—high-precision positives over an unknown-recall support—and develop… |
| 32 | W5-008 (B-0006) | B-0006 | Show that fine-tuning one model on multiple datasets with different annotation conventions (e.g., "organ+capsule" vs "organ only") produces a… |
| 33 | W5-009 (B-0053) | B-0053 | Estimate what fraction of cross-dataset performance drop between endoscopy benchmarks is due to differing label definitions ("polyp" boundaries,… |
| 34 | W5-056 (MERGE-05) | A-0296 + B-0064  (= MERGE-05) | Published UDA methods on fresh adaptation pairs (frozen + bounded-retuning) against source-only and frozen-foundation baselines at matched compute;… |
| 35 | W5-031 (A-0067) | A-0067 | Test whether a single scalar — the encoder/decoder learning-rate ratio — explains most variance among PEFT/fine-tuning recipes for promptable… |
| 36 | W5-032 (A-0072) | A-0072 | Run the controlled comparison the field skipped: strong augmentation + frozen features + linear/light decoder vs weak augmentation + LoRA, at matched… |
| 37 | W5-033 (B-0114) | B-0114 | Measure the cross-seed variance of LoRA/adapter fine-tuning results for segmentation and compare it against the effect sizes typically reported when… |
| 38 | W5-035 (B-0257) | B-0257 | Test whether PEFT methods that match full fine-tuning on region-level metrics systematically underperform on boundary-localized metrics—a hidden… |
| 39 | W5-038 (B-0272) | B-0272 | Test whether low-capacity PEFT confers implicit robustness to label noise in fine-tuning data—the constrained update cannot fit structured annotation… |
| 40 | W5-039 (B-0306) | B-0306 | Test the counterintuitive observation that very low LoRA ranks (1–2) sometimes outperform standard ranks (8–16) on tiny fine-tuning datasets,… |
| 41 | W5-042 (C-0001) | C-0001 | Predict PEFT failure from the spectral structure of the weight update that full fine-tuning would make. |
| 42 | W5-043 (C-0011) | C-0011 | Adjudicate whether PEFT failures are capacity failures or optimization failures by giving PEFT unbounded compute. |
| 43 | W5-044 (C-0016) | C-0016 | Test whether PEFT specifically fails at small-lesion sensitivity because the required update lives in high-frequency spatial features. |
| 44 | W5-045 (C-0023) | C-0023 | Test the hypothesis that PEFT cannot *unlearn* — tasks requiring suppression of misleading pretrained features need full FT. |
| 45 | W5-072 (A-0181) | A-0181 | Audit patch-level image-text alignment in CLIP-style models to establish *why* global contrastive training produces spatially misaligned dense… |
| 46 | W5-069 (A-0183) | A-0183 | Isolate spatial-relation reasoning ("left of", "behind", "between") as the failure locus in referring expression segmentation via minimal-pair… |
| 47 | W5-077 (B-0132) | B-0132 | Trace the layer-by-layer decay of pixel-localizable information in LLaVA-style VLMs to identify precisely where dense-prediction capacity is… |
| 48 | W5-078 (B-0174) | B-0174 | Test whether adding language supervision to segmentation training systematically degrades boundary precision (language groups pixels semantically,… |
| 49 | W5-081 (C-0072) | C-0072 | Build a text-only baseline audit for referring segmentation: how often is the mask predictable without looking at the image? |
| 50 | W5-082 (C-0076) | C-0076 | Show that report-supervised medical VLMs align to reporting style — including pervasive negations — and that negation breaks their dense grounding. |
| 51 | W5-083 (C-0078) | C-0078 | Test whether decoders trained on frozen CLIP features learn to *invert* the alignment direction — actively removing text-aligned components to… |
| 52 | W5-088 (B-0104) | B-0104 | Characterize what promptable segmenters output when prompts are semantically wrong (clicked on the wrong organ, box around the wrong object), and… |
| 53 | W5-089 (B-0128) | B-0128 | Measure the continuity structure of the click-position-to-output-mask mapping—identifying discontinuity manifolds where millimeter click changes flip… |
| 54 | W5-090 (B-0282) | B-0282 | Quantify how often adding a correction click degrades SAM-family mask quality (non-monotonic refinement), characterize the conditions triggering it,… |
| 55 | W5-086 (MERGE-17) | B-0089 + B-0193  (= MERGE-17) | Collect human prompt logs once: measure the oracle-prompt inflation factor of GT-derived evaluation prompts, and the training-side gain from… |
| 56 | W5-097 (A-0154) | A-0154 | Determine whether camouflaged object detection failures are perceptual (features don't separate figure from ground) or attentional (features suffice… |
| 57 | W5-128 (A-0001) | A-0001 | Test whether SAM segments *visual boundaries* rather than *semantic objects* by dissociating the two on camouflage and texture-boundary stimuli. |
| 58 | W5-133 (A-0266) | A-0266 | Test whether unsupervised segmentation via SSL-feature clustering discovers *objects* or merely *contiguous texture regions*, using scenes where… |
| 59 | W5-134 (A-0211) | A-0211 | Re-measure texture-vs-shape bias in modern VFMs (DINOv2, CLIP, SAM-class) with dense-prediction-relevant stimuli, testing whether the CNN-era texture… |
| 60 | W5-196 (C-0121) | C-0121 | Test whether consistency regularization works via implicit boundary smoothing rather than the cluster assumption it cites. |
| 61 | W5-198 (C-0132) | C-0132 | Quantify the positional shortcut in pixel-level contrastive SSL on spatially registered medical images. |
| 62 | W5-199 (C-0137) | C-0137 | Show that "barely-supervised" (one labeled volume) segmentation success is carried by implicit registration, and collapses on unregistered anatomy. |
| 63 | W5-021 (A-0246) | A-0246 | Audit base-class leakage in few-shot segmentation benchmarks: how much of reported FSS performance comes from novel classes resembling base classes… |
| 64 | W5-017 (B-0108) | B-0108 | Measure how much of reported "zero-shot" segmentation performance is attributable to prompt-template and hyperparameter search on validation data… |
| 65 | W5-184 (C-0290) | C-0290 | Test whether Dice loss is actually necessary for imbalanced segmentation, or whether tuned weighted cross-entropy matches it. |
| 66 | W5-185 (C-0311) | C-0311 | Test whether early stopping on validation Dice silently sacrifices boundary quality that continues improving after Dice plateaus. |
| 67 | W5-160 (C-0326) | C-0326 | Run the slice-order checkerboard test on "3D" models: feed volumes with permuted slice order and see whether claimed volumetric reasoning notices. |
| 68 | W5-161 (C-0332) | C-0332 | Apply the mask-the-lesion test systematically to medical detection papers: does the detector still fire on surrounding context when the finding… |
| 69 | W5-195 (C-0316) | C-0316 | Replace learned prompts with random-but-frozen vectors of matched norm: if accuracy holds, prompt "learning" is mostly capacity, not semantics. |
| 70 | W5-084 (C-0329) | C-0329 | Replace the VLM text encoder's output with class-mean image embeddings: if open-vocab segmentation is unchanged, "language" contributes nothing… |
| 71 | W5-025 (A-0242) | A-0242 | Estimate publication bias in segmentation literature by comparing the distribution of reported improvements against the expected null distribution… |
| 72 | W5-011 (MERGE-14) | A-0166 + B-0037 + C-0245  (= MERGE-14‡) | Closed-form max-IoU from boundary tolerance and object size, empirically anchored by multi-rater jitter; annotator-identity prediction from residuals… |
| 73 | W5-091 (A-0328) | A-0328 | Validate (or invalidate) simulated-click protocols for interactive segmentation by measuring ranking agreement with real-user evaluations across the… |

## Tier 3 — standard verification (74–131)

| Rank | Pool ID | Sources | Search target (one-liner) |
|---|---|---|---|
| 74 | W5-027 (A-0261) | A-0261 | Decompose the remaining gap in image-label-only weakly supervised semantic segmentation (WSSS) into localization, extent, and boundary components to… |
| 75 | W5-029 (C-0315) | C-0315 | Run the scramble test on published "global context" modules: shuffle distant image regions and see if the module's benefit survives. |
| 76 | W5-034 (B-0253) | B-0253 | Causally test the hypothesis that adapting attention weights primarily corrects spatial-relational errors (grouping, extent) while adapting MLP… |
| 77 | W5-036 (B-0269) | B-0269 | Test whether adapting only the multimask selection head—which candidate mask to prefer—captures most of the benefit of full adaptation for domains… |
| 78 | W5-040 (B-0315) | B-0315 | Test the phenomenon that mixing a small fraction (~5%) of unrelated out-of-domain data into fine-tuning outperforms optimally tuned conventional… |
| 79 | W5-041 (A-0238) | A-0238 | Test whether auxiliary depth estimation genuinely improves segmentation or whether the reported multi-task benefit is explained by the extra… |
| 80 | W5-046 (A-0052) | A-0052 | Quantify the bias-variance decomposition of PEFT vs full fine-tuning across random seeds: is PEFT's advantage on small data mostly variance reduction? |
| 81 | W5-055 (B-0286) | B-0286 | Systematically test whether fine-tuning that improves average performance regresses identifiable subgroups (rare acquisition settings, atypical… |
| 82 | W5-058 (B-0054) | B-0054 | Benchmark candidate domain-distance measures (FID in various feature spaces, MMD, spectral divergences, token-distribution shifts) as predictors of… |
| 83 | W5-059 (B-0072) | B-0072 | Constrain all trainable adaptation to a global Fourier amplitude filter and measure how much of various domain gaps this single interpretable… |
| 84 | W5-061 (B-0279) | B-0279 | Adapt segmentation models to new domains without any labels by distilling the consensus of prompt-perturbation ensembles (the base model's own… |
| 85 | W5-062 (A-0239) | A-0239 | Audit entropy-minimization test-time adaptation (TENT-class) on segmentation for silent class collapse, and characterize the conditions (class… |
| 86 | W5-063 (B-0304) | B-0304 | Test the phenomenon that removing or bottlenecking encoder-decoder skip connections sometimes improves cross-domain segmentation—evaluating whether… |
| 87 | W5-067 (A-0041) | A-0041 | Test whether chain-of-thought style reasoning text actually changes *where* VLMs ground (attention/mask placement) or only changes the verbal… |
| 88 | W5-070 (MERGE-02) | A-0185 + B-0241  (= MERGE-02) | One benchmark crossing {present / absent-plausible / absent-implausible} targets with a prompt-assertiveness ladder; mask-emission rates, confidence,… |
| 89 | W5-071 (A-0199) | A-0199 | Measure interference from scene text (signs, labels, watermarks) on VLM grounding: does written text in images hijack text-prompted segmentation… |
| 90 | W5-073 (B-0124) | B-0124 | Test whether the near-collinearity of related concept embeddings in CLIP text space ("smoke", "steam", "fog", "haze") predicts—and… |
| 91 | W5-075 (A-0033) | A-0033 | Map the relationship between lexical specificity of the prompt ("vehicle" → "car" → "sedan" → "2012 Toyota Camry") and segmentation quality, testing… |
| 92 | W5-076 (A-0049) | A-0049 | Test whether expert medical terminology or lay descriptions prompt medical VLM segmentation better — the "vocabulary register mismatch" question. |
| 93 | W5-085 (B-0033) | B-0033 | Decompose open-vocabulary segmentation failures on tail classes into linguistic causes (polysemous or obscure class names) versus visual causes (rare… |
| 94 | W5-110 (MERGE-04) | A-0161 + B-0129 + C-0264  (= MERGE-04‡) | Probe frozen features to locate the decodability crossover for small/thin structures, attribute the loss layer-by-layer to patch embedding, and test… |
| 95 | W5-111 (A-0003) | A-0003 | Establish an empirical "failure law" relating object pixel size to SAM IoU and test whether the breakpoint is set by the ViT patch size (16 px). |
| 96 | W5-112 (A-0313) | A-0313 | Test whether raw input resolution beats all architectural small-object remedies at matched compute — the compute-matched showdown the small-object… |
| 97 | W5-113 (B-0288) | B-0288 | Test whether larger foundation-segmenter variants perform relatively worse on very small structures than smaller variants—an inverse-scaling pocket… |
| 98 | W5-114 (A-0176) | A-0176 | Audit dataset-level JPEG compression as a hidden confounder for small-object and boundary research: are benchmark small objects already destroyed by… |
| 99 | W5-115 (A-0174) | A-0174 | Measure the effect of ViT attention artifacts (high-norm "register" tokens appearing in feature maps) on small-object localization, testing whether… |
| 100 | W5-116 (B-0122) | B-0122 | Measure how segmentation quality of thin structures varies with their orientation relative to the ViT patch grid, and determine whether the effect… |
| 101 | W5-121 (A-0103) | A-0103 | Test whether model uncertainty maps (entropy, MC-dropout, ensembles) actually correlate with *clinician disagreement* regions, which is the… |
| 102 | W5-122 (MERGE-18) | B-0120 + B-0337 + C-0253  (= MERGE-18‡) | One coverage-testing methodology (held-out-rater reference distributions, in- and out-of-domain) applied to the three 'free' uncertainty sources… |
| 103 | W5-125 (B-0310) | B-0310 | Investigate the paradoxical observation that models trained on soft labels (matting-style, multi-rater averages) sometimes output more extreme… |
| 104 | W5-126 (A-0280) | A-0280 | Test whether model uncertainty actually targets the pixels humans most need to label — auditing the core assumption of uncertainty-routed annotation… |
| 105 | W5-138 (C-0289) | C-0289 | Test non-monotonicity of pretraining scale for medical transfer: curated small pretraining can beat web-scale for specific modalities. |
| 106 | W5-139 (C-0301) | C-0301 | Measure the true frozen-backbone ceiling for dense prediction with properly engineered multi-layer readouts. |
| 107 | W5-140 (B-0300) | B-0300 | Investigate the phenomenon that continued self-supervised pretraining (MAE-style) on target-domain data before supervised fine-tuning sometimes… |
| 108 | W5-141 (B-0217) | B-0217 | Characterize how upstream box-localization errors transform into downstream mask errors in detect-then-segment pipelines, and test whether training… |
| 109 | W5-142 (B-0223) | B-0223 | Isolate how label-assignment rules in detector training (IoU thresholds, center sampling) systematically under-train on extreme-aspect-ratio objects… |
| 110 | W5-143 (B-0233) | B-0233 | Rigorously measure the marginal value of learned object detection over classical background-model change detection for static-camera fire/smoke… |
| 111 | W5-144 (B-0331) | B-0331 | Using SR models with controllable generative strength (guidance/hallucination knobs), map the frontier between detail hallucination and downstream… |
| 112 | W5-145 (B-0338) | B-0338 | Test whether denoising preprocessing harms detection of near-resolution-limit targets (distant smoke plumes, micro-calcifications) because… |
| 113 | W5-146 (B-0285) | B-0285 | Test the counterintuitive observation that mild lossy compression sometimes improves smoke segmentation, evaluating the hypothesis that compression's… |
| 114 | W5-147 (C-0273) | C-0273 | Audit window-position bias in sliding-window inference: prediction quality varies systematically between window centers and edges, hidden by overlap… |
| 115 | W5-149 (MERGE-27) | A-0093 + C-0300  (= MERGE-27) | Matched-budget component swaps (3D context handling, augmentation policy, resolution/preprocessing-normalization stack) causally decompose the… |
| 116 | W5-151 (B-0156) | B-0156 | Measure how many report-supervised images (spatial constraints parsed from routine radiology text) equal one expert pixel-labeled image for training… |
| 117 | W5-152 (B-0182) | B-0182 | Exploit explicit negative findings in radiology reports ("no pneumothorax", "no focal lesion") as verified-absence supervision, testing whether… |
| 118 | W5-153 (B-0184) | B-0184 | Use registered pre/post-contrast CT differencing to generate automatic vessel labels at scale, and characterize the systematic bias this induces… |
| 119 | W5-159 (MERGE-24) | B-0081 + C-0177  (= MERGE-24) | Which segmentation metric predicts errors in the quantities clinicians consume (volumes, diameters, growth rates, boundary-derived indices) — and do… |
| 120 | W5-162 (A-0096) | A-0096 | Establish the sensitivity-vs-lesion-size law for medical VFMs versus specialized detectors, testing whether foundation models have a systematically… |
| 121 | W5-164 (B-0186) | B-0186 | Measure the mode coverage of diffusion-generated medical images against the true long tail of pathology presentations, testing whether synthesis… |
| 122 | W5-165 (MERGE-12) | A-0285 + B-0190  (= MERGE-12) | Sweep within-class and global synthetic fractions across two generator families; endpoints: rare-class real-instance recall inversion, silent… |
| 123 | W5-166 (B-0189) | B-0189 | Test whether segmentation models trained on lesions synthetically inpainted into healthy images learn to detect the generative fingerprint (boundary… |
| 124 | W5-167 (B-0200) | B-0200 | Test whether the pixel-perfect labels of rendered data teach segmentation models boundary-tolerance expectations that mismatch real-world annotation… |
| 125 | W5-168 (A-0283) | A-0283 | Run factor-controlled sim-to-real for segmentation — independently making geometry, texture, lighting, and sensor-model real versus synthetic — to… |
| 126 | W5-169 (A-0287) | A-0287 | Compare procedural (physics/graphics) generation against diffusion-model generation for training data on *out-of-web-distribution* phenomena (smoke,… |
| 127 | W5-190 (C-0124) | C-0124 | Show that self-training converges toward a single annotator style, collapsing the inter-rater variance present in the initial labels. |
| 128 | W5-192 (C-0095) | C-0095 | Test whether the celebrated base-new class trade-off in prompt learning is a regularization artifact rather than a generalization property. |
| 129 | W5-194 (C-0113) | C-0113 | Document "prompt collapse": class prompts converging toward each other during long training, silently destroying fine-grained discrimination. |
| 130 | W5-197 (C-0127) | C-0127 | Show that the "low-data regime" simulated by subsampling big datasets misrepresents true small-cohort learning, breaking method rankings. |
| 131 | W5-200 (C-0143) | C-0143 | Test whether label-efficient methods change the slope or only the intercept of the labeled-data learning curve. |

## Tier 4 — distinctive designs, moderate risk (132–175)

| Rank | Pool ID | Sources | Search target (one-liner) |
|---|---|---|---|
| 132 | W5-014 (A-0337) | A-0337 | Treat annotation instructions as an experimental variable: annotate the same images under different (all-reasonable) instruction documents and… |
| 133 | W5-013 (A-0336) | A-0336 | Measure human segmentation performance (time-budgeted and unlimited) on standard benchmarks to establish the human floors and ceilings that… |
| 134 | W5-016 (B-0017) | B-0017 | Show that transparent-object segmentation benchmarks contain almost no target-absent images, leaving false-positive behavior unmeasured, and build a… |
| 135 | W5-018 (B-0110) | B-0110 | Develop and validate an importance-sampling estimator for extremely low false-positive rates (FP/day) of fire/smoke systems, replacing infeasible… |
| 136 | W5-098 (A-0121) | A-0121 | Demonstrate that binary smoke masks are ill-posed ground truth by measuring annotator threshold inconsistency, and propose density-graded ground… |
| 137 | W5-103 (A-0123) | A-0123 | Test whether fire segmentation models are mostly color detectors, via hue-manipulation stress tests and colored-distractor benchmarks (sunsets, neon,… |
| 138 | W5-102 (A-0126) | A-0126 | Replace IoU with detection-latency (time from first visible smoke to first correct alarm-grade mask) as the primary metric for wildfire smoke… |
| 139 | W5-107 (A-0319) | A-0319 | Test whether bounding boxes are the wrong output primitive for amorphous phenomena (smoke, fire, spills, dust) by comparing box-based against… |
| 140 | W5-108 (B-0219) | B-0219 | Test whether non-maximum suppression and its query-based equivalents systematically destroy correct detections of amorphous, fragmenting targets… |
| 141 | W5-106 (B-0055) | B-0055 | Test whether robustness-oriented adaptation toward foggy conditions increases false positives on smoke (and vice versa), revealing an adversarial… |
| 142 | W5-096 (A-0157) | A-0157 | Measure the human-vision floor for near-invisible glass (clean, anti-reflective, well-lit) and test whether current models are above or below human… |
| 143 | W5-094 (B-0075) | B-0075 | Determine whether foundation segmenters localize transparent objects via boundary/refraction cues (domain-stable) or via reflected environmental… |
| 144 | W5-092 (MERGE-10) | A-0141 + B-0126  (= MERGE-10) | Probes on frozen VFM features over glass regions decode {glass presence, background class, both layers}; the three-way verdict routes transparency… |
| 145 | W5-100 (MERGE-03) | A-0006 + B-0226  (= MERGE-03) | A single standardized integrated-boundary-contrast measure may predict IoU and detection recall across amorphous matter, camouflage, transparency,… |
| 146 | W5-130 (MERGE-13) | A-0021 + B-0136  (= MERGE-13) | A common color-intervention battery {original, grayscale, hue-rotated, equiluminant, chroma-only} applied to SAM-class models and smoke segmenters:… |
| 147 | W5-135 (A-0223) | A-0223 | Determine whether in-context segmentation (SegGPT/Painter-style visual prompting) performs abstraction or sophisticated nearest-neighbor copying, via… |
| 148 | W5-136 (A-0225) | A-0225 | Test the "platonic convergence" claim at the *patch* level: are different VFMs' dense feature spaces converging to affinely equivalent… |
| 149 | W5-137 (A-0207) | A-0207 | Quantify how much of inter-VFM downstream variance is explained by training *data* overlap versus objective and architecture, using models with… |
| 150 | W5-131 (A-0202) | A-0202 | Build the definitive task×backbone matrix for frozen dense features (DINOv2, CLIP, SAM, MAE-class) under matched probing protocols, testing whether… |
| 151 | W5-047 (MERGE-07) | A-0076 + B-0248  (= MERGE-07) | One LR × components × steps × rank sweep with matched-target checkpoint selection traces the gain/retention Pareto frontier, places published recipes… |
| 152 | W5-050 (MERGE-08) | A-0058 + B-0260  (= MERGE-08) | Low-rank updates can only reweight existing (often spurious) directions: worst-group degradation on constructed spurious correlations plus sharper… |
| 153 | W5-051 (B-0251) | B-0251 | Test whether the success of merging multiple dataset-specific LoRAs into one (versus training jointly) is predictable from the geometry of their… |
| 154 | W5-053 (C-0056) | C-0056 | Quantify cumulative "TTA drift": continuously running test-time adaptation in deployment causes progressive forgetting. |
| 155 | W5-054 (C-0057) | C-0057 | Disentangle true representational forgetting from annotation-protocol mismatch when measuring cross-site "forgetting". |
| 156 | W5-066 (A-0301) | A-0301 | Study continual adaptation under *cyclically returning* domains (day/night, seasons, weather) and test whether current continual-DA methods oscillate… |
| 157 | W5-157 (C-0164) | C-0164 | Determine the effective resolution ceiling of medical FMs: which subtle findings live below what the representation can carry? |
| 158 | W5-171 (C-0179) | C-0179 | Measure the equivariance conflict: box regression rewards translation-sensitive features while mask prediction demands equivariance, and shared… |
| 159 | W5-172 (C-0187) | C-0187 | Test the amodal-modal conflict: detectors learn amodal object extent while segmentation learns visible (modal) extent, corrupting shared features… |
| 160 | W5-173 (C-0190) | C-0190 | Show that competing instance-segmentation paradigms differ almost entirely on boundary pixels — and agree elsewhere. |
| 161 | W5-174 (C-0192) | C-0192 | Show mask-classification architectures secretly perform detection: their queries have box-like receptive behavior, inheriting detection's failure… |
| 162 | W5-175 (C-0196) | C-0196 | Show that deriving lesion detection from segmentation post-processing destroys calibrated lesion-level confidence, and quantify the decision cost. |
| 163 | W5-176 (C-0204) | C-0204 | Test whether sliding-window 3D segmentation loses whole-object evidence that detection-style global context retains — on large lesions exceeding… |
| 164 | W5-177 (C-0205) | C-0205 | Decompose segmentation boundary error into image-aleatoric, annotation-protocol, and model-bias components with a reusable methodology. |
| 165 | W5-178 (C-0206) | C-0206 | Measure the physics floor: partial-volume effects and slice thickness define a computable lower bound on boundary error in medical imaging. |
| 166 | W5-179 (C-0208) | C-0208 | Derive and verify the systematic inward/outward boundary bias induced by cross-entropy training under class imbalance. |
| 167 | W5-180 (C-0210) | C-0210 | Redo method comparison statistics accounting for spatial autocorrelation of boundary errors — standard tests overstate significance. |
| 168 | W5-183 (C-0218) | C-0218 | Perform bias-variance decomposition of boundary displacement fields: model boundary errors are directional and consistent, not random. |
| 169 | W5-186 (C-0233) | C-0233 | Validate inter-rater disagreement maps as a free error oracle: where raters disagree predicts where models fail. |
| 170 | W5-187 (C-0234) | C-0234 | Quantify consensus harm: training on majority-vote/STAPLE labels destroys clinically relevant ambiguity information relative to training on raw rater… |
| 171 | W5-188 (C-0235) | C-0235 | Decompose rater disagreement into systematic style offsets versus genuine ambiguity using mixed-effects modeling — recovering hidden agreement. |
| 172 | W5-022 (C-0339) | C-0339 | Evaluate methods against 1-pixel morphological perturbations of ground truth: if rankings flip, benchmarks measure annotation-style matching, not… |
| 173 | W5-117 (MERGE-25) | B-0305 + C-0261  (= MERGE-25) | Dense quality oscillates with input size at the patch-grid period and with sub-patch translation phase of object boundaries — an unmeasured variance… |
| 174 | W5-118 (MERGE-26) | A-0170 + C-0276  (= MERGE-26) | Do INR decoders and learned feature upsamplers recover image information or impose metric-pleasing priors? Synthetic scenes with exact sub-pixel… |
| 175 | W5-119 (C-0269) | C-0269 | Test whether anti-aliased patchification (strided-conv tokenizers violate Nyquist) changes ViT texture bias and dense robustness. |

## Tier 5 — most-distinctive bets, attack last (176–200)

| Rank | Pool ID | Sources | Search target (one-liner) |
|---|---|---|---|
| 176 | W5-105 (B-0318) | B-0318 | Attach a differentiable single-scattering radiative-transfer head to a segmentation backbone so smoke predictions are expressed as volumetric density… |
| 177 | W5-099 (A-0122) | A-0122 | Use atmospheric transmission physics (Beer–Lambert attenuation) to derive alpha-matte smoke ground truth from smoke/no-smoke image pairs, creating… |
| 178 | W5-104 (A-0125) | A-0125 | Test whether the turbulence statistics of smoke motion (spectral signatures of buoyant plumes) provide a self-supervision signal that separates smoke… |
| 179 | W5-095 (B-0162) | B-0162 | Train transparency segmenters with polarization imagery as privileged supervision (available only at training time) and measure how much of the… |
| 180 | W5-163 (B-0177) | B-0177 | Generate automatic cell/structure labels for H&E histology by restaining the same physical slides with IHC markers and registering the pair, then… |
| 181 | W5-170 (A-0278) | A-0278 | Learn label-space priors by masked autoencoding on *unpaired* segmentation masks (no images), and test whether such shape/layout priors improve… |
| 182 | W5-060 (B-0078) | B-0078 | Test whether natural-language descriptions of a target domain ("underwater, greenish turbidity, particulate backscatter") can condition a segmenter's… |
| 183 | W5-019 (B-0294) | B-0294 | Test whether per-image loss distributions on evaluation sets exhibit mixture structure (a memorized low-loss mode and a genuine-generalization mode)… |
| 184 | W5-020 (A-0254) | A-0254 | Construct a true-zero-shot benchmark from procedurally synthesized never-seen categories to measure how much of "zero-shot segmentation" survives… |
| 185 | W5-007 (B-0009) | B-0009 | Audit web-scale segmentation pretraining data (SA-1B) for the frequency of hard strata—transparent, wiry, camouflaged, low-contrast, tiny—and test… |
| 186 | W5-120 (C-0287) | C-0287 | Quantify numerics as a benchmark variance source: low-precision attention implementations change dense outputs near boundaries at rates comparable to… |
| 187 | W5-189 (C-0249) | C-0249 | Stress-test losses under multimodal ground truth: standard objectives assume unimodal truth and fail predictably when raters split between discrete… |
| 188 | W5-158 (C-0173) | C-0173 | Measure salience suppression: FMs detect the most prominent lesion and systematically under-report additional ones. |
| 189 | W5-156 (C-0162) | C-0162 | Test whether report-supervised FMs learn the distribution of *reported* findings, systematically missing unreported incidentals. |
| 190 | W5-191 (C-0091) | C-0091 | Show that learned soft prompts are dataset fingerprints: the training dataset is identifiable from the prompt vector alone. |
| 191 | W5-079 (B-0185) | B-0185 | Construct controlled conflicts between linguistic anatomical priors ("the liver is homogeneous") and image evidence (nodular cirrhotic liver) to… |
| 192 | W5-148 (A-0118) | A-0118 | Test how segmentation models fail on post-surgical and anatomically variant patients, quantifying the "atlas prior" dependence of modern learned… |
| 193 | W5-109 (A-0124) | A-0124 | Build the smoke/fog/steam/cloud/dust confusion benchmark and test whether any visual model can separate these physically distinct but visually… |
| 194 | W5-127 (B-0098) | B-0098 | Train small independent verifier networks that predict a frozen segmenter's per-case failure (IoU below threshold) from the image and predicted mask,… |
| 195 | W5-150 (MERGE-23) | A-0100 + C-0149  (= MERGE-23) | Flip-TTA imposes an anatomically invalid invariance inside standard pipelines, and medical FMs may be unable to represent left vs right at all — a… |
| 196 | W5-155 (C-0151) | C-0151 | Test whether FMs lost metric scale: physical-size estimation fails because pretraining pipelines discard pixel spacing. |
| 197 | W5-154 (C-0150) | C-0150 | Measure the pairwise-reasoning gap: FMs cannot compare two scans (change detection) even when they analyze each well individually. |
| 198 | W5-064 (A-0305) | A-0305 | Determine whether night-time segmentation is a domain-adaptation problem or an information-deficit problem, by measuring the human ceiling on the… |
| 199 | W5-181 (C-0212) | C-0212 | Detect annotation-tool fingerprints in ground-truth boundaries and quantify their effect on benchmark comparisons. |
| 200 | W5-182 (C-0214) | C-0214 | Extract sub-pixel boundary estimates from logit gradients: models know boundary positions more precisely than their argmax masks express. |

*End of attack queue: 200 entries, ranks 1–200.*
