# Stage 5 — Cluster C Experimental Engineering

**Role:** Experimental Engineer (Cloud Sub-Agent O) → Supervisor Windows7.
**Input:** 7 Stage-4 Cluster C survivors from `origin/cursor/stage4-cluster-c-reviewer2-c1be` (C-0028, C-0090, C-0128, C-0158, C-0229, C-0302, C-0310), Stage-3 audits from `origin/cursor/stage3-cluster-c-priorwork-f96e`, Stage-1 originals from `origin/cursor/stage1-cluster-c-ideas-8c7f`. A/B Stage-4 keeps read for overlap (none found; adjacency notes preserved from Stage 4).
**Charter:** Full experimental design per survivor, engineered against *real, verified codebases* (all repos/datasets below confirmed to exist via search this session). The **Killer Experiment** is the load-bearing field: the single pre-registered run-set whose outcome decides the idea's fate before the full program is funded. Designs assume work starts next week: every design opens with a bootstrap command list that runs on day one.

**Selection preference applied (per Supervisor):** ideas that change how people *train or evaluate* models outrank instrument/audit deliverables, however well-defended.

**Verdict summary: KEEP C-0028 (rank 2), KEEP C-0090 (rank 1). Optional-3rd slot evaluated and declined — C-0158's killer measurement is cheap but the paper-level claim is not; its Phase-1 probe is recommended as a rider. Full ranking in `stage5_cluster_C_top.md`, costs in `stage5_cluster_C_roi.csv`.**

---

## 1. C-0090 — Text-batch rehearsal works by gradient rebalancing, not by content

**Claim under test:** Interleaved text-only batches during multimodal fine-tuning prevent language forgetting via optimization balance (any matched-scale gradient on the language pathway), not via the content of the rehearsal text.
**Stage-4 mandatory condition (kept):** capability-stratified evaluation; results reported under two pre-registered gradient-matching conventions.

### 1.1 KILLER EXPERIMENT — "Content-free rehearsal grid"

Five rehearsal arms at fixed token budget on a LLaVA-1.5-7B full fine-tune, capability-stratified retention, pre-registered decision rule.

- **Base run:** LLaVA-1.5 recipe exactly as published (Vicuna-7B + CLIP ViT-L/336, 665K visual-instruction mix, 1 epoch, lr 2e-5) via `haotian-liu/LLaVA`. Alternative harness if the original recipe fights us: `TRI-ML/prismatic-vlms` (used by the closest adjacent prior, arXiv:2410.19925 — see §1.4).
- **Arms (rehearsal = 10% of total training tokens, interleaved 1 text batch per 9 multimodal batches):**
  - A0 `none` — no rehearsal (forgetting floor).
  - A1 `curated` — instruction/text mix of the kind the field curates (ShareGPT text-only slice + OpenOrca sample).
  - A2 `random-web` — C4 (`allenai/c4`) documents, no curation whatsoever.
  - A3 `shuffled-token` — the *same* C4 sample with tokens permuted within documents (destroys syntax and content, preserves unigram statistics and sequence length).
  - A4 `single-doc` — one fixed ~2K-token document repeated for the whole budget (destroys diversity and content; preserves "some real-text gradient").
- **Seeds:** 3 per arm (15 fine-tunes). Seed variance on A0/A1 gates all claims.
- **Stratified evaluation (pre-registered, all via `EleutherAI/lm-evaluation-harness` + `EvolvingLMMs-Lab/lmms-eval`):**
  - *Fluency:* WikiText perplexity, LAMBADA.
  - *Knowledge:* MMLU, NaturalQuestions closed-book.
  - *Reasoning:* GSM8K, ARC-Challenge.
  - *Instruction-following:* IFEval.
  - *Vision-language (sanity, must not regress):* VQAv2, GQA, TextVQA via lmms-eval.
  - Retention(c, arm) = score(c, arm) / score(c, Vicuna-7B base).
- **Gradient-matching conventions (both reported; conclusion must be convention-invariant):** (i) global-norm matching — text-batch loss scaled so mean global grad-norm of text steps matches A1; (ii) per-layer matching — per-transformer-block norm matching on the LLM tower. Telemetry: per-module grad norms logged every 50 steps (hooks; ~0 cost).
- **Pre-registered decision rule:** for each language capability c, define content-effect(c) = Ret(A1) − Ret(A2) and balance-effect(c) = Ret(A2) − Ret(A0).
  - **Mechanism confirmed** iff balance-effect ≥ 80% of [Ret(A1) − Ret(A0)] on ≥3 of 4 language capabilities *under both conventions* → headline: rehearsal-content curation budgets are misdirected; a gradient-balance term suffices.
  - **Stratified-recipe outcome** (the "mushy middle" made actionable) iff knowledge shows content-effect > 50% of total while fluency shows < 20%: publish the per-capability map + minimal-real-text fraction sweep (A2/A1 mixtures at {1, 5, 10}% real) → "you need X% real text, only for knowledge."
  - **Content camp confirmed** iff Ret(A2) ≈ Ret(A0) on all capabilities under both conventions — also publishable: the first controlled refutation of the Robins-1995 pseudo-rehearsal account in the multimodal regime.
  - A3 vs A2 separates lexical-statistics from syntax; A4 vs A2 separates diversity from content. These two contrasts are what keep any outcome from being a shrug.

### 1.2 Build plan (verified codebases)

| Component | Repo / dataset | Role |
|---|---|---|
| Training | `github.com/haotian-liu/LLaVA` | LLaVA-1.5 recipe, deepspeed configs shipped |
| Training (fallback) | `github.com/TRI-ML/prismatic-vlms` | Same-class VLM trainer used by closest prior |
| Text eval | `github.com/EleutherAI/lm-evaluation-harness` | MMLU/GSM8K/IFEval/WikiText/NQ/ARC/LAMBADA |
| VL eval | `github.com/EvolvingLMMs-Lab/lmms-eval` | VQAv2/GQA/TextVQA, one command per checkpoint |
| Rehearsal corpora | `allenai/c4` (HF), ShareGPT/OpenOrca (HF) | A1–A4 arm construction |
| Telemetry | torch hooks + wandb | per-module grad norms, both matching conventions |

Day-one bootstrap: clone LLaVA; download 665K mix + LLaVA-1.5 pretrained projector; verify the published recipe reproduces LLaVA-1.5 evals within noise (single run); implement the interleaved text-batch sampler (a ~100-line change in the LLaVA data module — same pattern as its existing multi-source sampler); land the grad-norm hooks; freeze the eval YAMLs (pre-registration artifact committed to the repo before any arm runs).

### 1.3 Compute & cost

Full LLaVA-1.5-7B fine-tune ≈ 8×A100-80GB × ~12 h ≈ 100 A100-h. 15 runs (killer) + 1 reproduction + 6 mixture-sweep runs (stratified-recipe branch, 2 seeds × 3 fractions) ≈ **2,300 A100-h**, evals ≈ 150 A100-h. No annotation, no API spend. Cheapest decisive design in the cluster; every branch of the decision rule is a publishable, practice-changing result.

### 1.4 Risks, controls, abort gates

- **Scoop check (searched this session):** arXiv:2410.19925 (*Improving MLLMs Using Continual Learning*, CoLLAs 2026) studies LLaVA linguistic forgetting with rehearsal among 5 mitigations — but its rehearsal arm uses *real* data only; no content-free controls (random/shuffled/single-doc), no gradient-matching analysis. It is scaffold, not scoop: cite, reuse their task splits, subsume. Residual risk: a content-free control appearing in the next cycle — mitigated by the design being 15 fine-tunes from done.
- **Convention dispute (Reviewer #2 attack 1):** both conventions reported; if conclusions diverge across conventions, that divergence *is* the finding (mechanism is convention-dependent → gradient-balance story refuted in its strong form).
- **Abort gate:** if seed-σ on A0/A1 retention exceeds half the A1−A0 gap after the first 6 runs, escalate to 5 seeds or drop to LLaVA-1.5-13B where forgetting is larger; if still underpowered → report power analysis and kill (cheap failure: <1K A100-h spent).

### 1.5 Practice change

Either the field stops paying for rehearsal-data curation (mechanism confirmed), or it gets the first per-capability rehearsal dosing recipe (partial), or curation is validated with a controlled effect size (refuted). All three change how people *train* multimodal models.

**VERDICT: KEEP — rank 1.**

---

## 2. C-0028 — In-batch concept co-occurrence, not loss design, creates dense alignment

**Claim under test:** Batch composition (caption-noun co-occurrence forcing spatial disambiguation among in-batch hard negatives) is a causal lever on emergent patch-level alignment in contrastive VLMs — separable from generic hard-negative effects.
**Stage-4 mandatory condition (kept):** the hardness-matched control arm. Without it this is a JEST metric-swap and dies.

### 2.1 KILLER EXPERIMENT — "Hardness-matched decision triple + dose curve"

- **Corpus:** CC12M + CC3M downloaded via `rom1504/img2dataset` into webdataset shards; deduplicated, capped at 20M image-text pairs, frozen (checksummed shard list committed — the C-0276 salvage habit).
- **Batch-construction arms** (implemented as a webdataset `compose()` batching iterator in `mlfoundations/open_clip` — the maintainer-documented pattern for custom batch composition; no trainer surgery needed):
  - **R** — random batches (baseline).
  - **N(s)** — noun-overlap curation at strength s: batches assembled so a fraction s of pairs share ≥1 head noun (spaCy noun-chunk extraction, precomputed per caption; index over nouns → constrained sampler). Strengths s ∈ {0.25, 0.5, 0.75}.
  - **H(s)** — hardness-matched control: batches assembled to match N(s)'s *in-batch caption-similarity distribution* (precomputed caption embeddings, all-MiniLM or CLIP text tower + FAISS range search) under the explicit constraint of **no shared head nouns** within the matched pairs. Matching target: quantile-matched histogram of pairwise in-batch similarities (KS-distance < 0.05 vs N(s), verified offline before any GPU is spent).
- **Model/recipe:** CLIP ViT-B/32 from `open_clip`, batch 4096, ~320M samples seen (≈16 passes over 20M), identical lr/temperature init/schedule across arms; learnable temperature logged (Reviewer-#2 attack 2 telemetry).
- **Decision triple:** R, N(0.5), H(0.5) × **3 seeds** = 9 runs. Dose curve: N(0.25), N(0.75), H(0.25), H(0.75) × 1 seed = 4 runs. Total 13 pretraining runs.
- **Joint metrics (both reported for every run, per the mandatory condition):**
  - *Dense:* zero-shot segmentation via **two independent training-free protocols** — SCLIP (`wangf3014/SCLIP`) and NACLIP (`sinahmr/NACLIP`), both MMSegmentation-based, on VOC20, Context59, COCO-Object, ADE20K. Two protocols so the finding cannot be an artifact of one attention-surgery choice. Plus a raw patch-text alignment score (no surgery): patch-level retrieval mIoU à la CLIP dense probing.
  - *Global:* COCO/Flickr30k retrieval R@1/R@5 and ImageNet zero-shot via `LAION-AI/CLIP_benchmark`.
- **Pre-registered decision rule:**
  - **Mechanism isolated** iff ΔmIoU(N−R) > 2σ_seed AND ΔmIoU(N−H) ≥ 0.5 · ΔmIoU(N−R) under *both* dense protocols, AND the N-dose curve is monotone (Spearman ρ > 0 across s). Retrieval deltas reported alongside; if retrieval moves, the claim narrows to "dense gains at matched retrieval" using H as the anchor — the comparison N vs H at matched hardness is what survives.
  - **JEST-reframe outcome** iff N tracks H within seed noise on dense metrics → co-occurrence is generic hardness; publish as a controlled refutation with the dose curve (the first dense-task accounting of batch hardness — still novel; JEST never measured dense grounding, confirmed at Stage 3).
  - **Uninformative null defused:** if neither N nor H moves dense metrics at any dose, the monotone-dose design converts "below emergence scale" into a measured flat curve + a scale-extrapolation section; kill the headline honestly.

### 2.2 Build plan (verified codebases)

| Component | Repo / dataset | Role |
|---|---|---|
| Pretraining | `github.com/mlfoundations/open_clip` | CLIP-B/32 trainer; webdataset pipeline |
| Batch curation | `webdataset` `compose()` custom iterator | maintainer-documented custom batching (issues #359/#450) |
| Data download | `github.com/rom1504/img2dataset` | CC12M/CC3M → webdataset shards |
| Caption NLP | spaCy `en_core_web_trf` | head-noun extraction (offline, CPU) |
| Hardness index | sentence-transformers + FAISS | caption-similarity matching for H arms |
| Dense eval 1 | `github.com/wangf3014/SCLIP` | training-free zero-shot seg (MMSeg) |
| Dense eval 2 | `github.com/sinahmr/NACLIP` | independent protocol, same datasets |
| Global eval | `github.com/LAION-AI/CLIP_benchmark` | retrieval + zero-shot classification |

Day-one bootstrap: img2dataset pull of CC3M (small) → implement noun index + curated-batch iterator → **offline dry-run**: generate 10K batches per arm, verify (a) KS-distance of similarity histograms N vs H < 0.05, (b) shared-noun rate in H ≈ R baseline rate, (c) throughput within 10% of random batching. This offline gate costs zero GPU and de-risks the entire design before the first pretraining run.

### 2.3 Compute & cost

CLIP-B/32, batch 4096, 320M samples: ≈ 45–55 h on 8×A100 ≈ 400 A100-h/run. 13 runs ≈ **5,200 A100-h** + eval (~100 A100-h; training-free seg is inference-only). Curation preprocessing is CPU-only. This is the most expensive kept design — affordable as the cluster's flagship on an 8-GPU node or modest cloud budget, and the decision triple alone (9 runs, 3,600 A100-h) settles the claim.

### 2.4 Risks, controls, abort gates

- **Matched hardness ≠ matched everything:** temperature and grad-SNR telemetry logged per arm; if learnable temperature diverges > 0.2 between N and H, add a fixed-temperature replicate of the decision triple (3 runs, budgeted as contingency).
- **Emergence floor:** CLIP-B/32 at 20M pairs has weak-but-nonzero dense ability under SCLIP/NACLIP protocols (published numbers on vanilla CLIP confirm measurable signal); the raw patch-alignment score is the sensitive low-floor instrument if mIoU floors out.
- **Throughput:** curated batching must not silently reduce effective data diversity (each sample's appearance count logged; arms matched on samples-seen histograms).
- **Abort gate:** offline dry-run failing the KS/noun criteria (means H is unconstructible at s=0.5 on this corpus) → reduce s to the largest constructible level; if < 0.25, kill before GPU spend.

### 2.5 Practice change

If the mechanism is isolated, batch curation becomes a documented, nearly-free *pretraining dial* for dense ability — a training-recipe change any CLIP shop can adopt without new objectives. If refuted, the dense-emergence folklore loses its most-cited informal explanation, with a dose curve in hand. Either way this changes how people train and how dense-emergence claims are evaluated.

**VERDICT: KEEP — rank 2.** (Rank 1 on impact, rank 2 on ROI; see top file.)

---

## 3. C-0158 (M6) — Uncertainty sampling selects LLM-annotator failures; decorrelated acquisition fixes it

**Claim under test:** Learner-uncertainty acquisition preferentially selects items where LLM-annotator error spikes (correlated difficulty), concentrating label noise where the student is most sensitive; reliability-penalized acquisition repairs the loop.
**Stage-4 mandatory condition (kept):** the annotate-everything + noise-robust-training baseline at matched total cost.

### 3.1 KILLER EXPERIMENT — "The correlation number" (Phase 1, cheap, decisive)

Before any acquisition arm runs: measure the item-level correlation between learner uncertainty and annotator error directly, on fully ground-truthed pools.

- **Pools (all public, labels exist):** AG News, TREC-50, Banking77 (text); one vision pool — COCO-subset (5K images) with per-instance masks as ground truth.
- **Annotators:** GPT-4o-mini and Qwen2.5-72B-Instruct for text (2 annotators → generality); for vision, a VLM-agent dense annotator (Grounded-DINO + SAM pipeline, per-item real compute cost) producing instance masks.
- **Learners:** DeBERTa-v3-base (text) via `small-text` (`webis-de/small-text`, the standard transformer-AL library); Mask R-CNN R50 (vision, detectron2).
- **Measurement:** train the learner on a random 10% seed set; score every remaining pool item's learner uncertainty (margin/entropy); annotate *the full pool* with each LLM annotator; compute per-item annotator-error indicator vs ground truth; report Spearman ρ(uncertainty, error) with bootstrap CIs, per dataset × annotator; plus self-consistency (5 samples) as the no-ground-truth error predictor and *its* correlation with true error.
- **Pre-registered decision rule:**
  - ρ ≤ 0.1 everywhere → premise dead; publish the cheap null (a real contribution: the folklore is measurable and absent) and stop. Total spend to this point: ~$1–2K API + <100 GPU-h.
  - ρ ≥ 0.3 on ≥2 settings AND self-consistency predicts error (AUROC ≥ 0.7) → fund Phase 2.
- **Phase 2 (the paper):** acquisition arms at matched *total cost* (annotation $ + compute $, cost model pre-registered): random; uncertainty; error-penalized (uncertainty × predicted-reliability from self-consistency — no ground truth used); **annotate-everything + noise-robust training** (cleanlab confident-learning filter and co-teaching, whichever is stronger per dataset). Binding-budget settings front and center: the VLM dense-annotation pool (per-item cost is real GPU time) and one frontier-annotator-at-scale text setting. If annotate-everything wins at matched cost, *that* is the published finding (AL+LLM pipelines should be dismantled) — every branch actionable.

### 3.2 Build plan (verified codebases)

| Component | Repo / tool | Role |
|---|---|---|
| AL loops (text) | `github.com/webis-de/small-text` | pool-based AL, transformer learners, standard strategies |
| AL for NLG / LLM-annotator plumbing | `github.com/Aktsvigun/atgen` | LLM-as-annotator integration patterns (OpenAI batch API = 50% cheaper) |
| Noise-robust baseline | `github.com/cleanlab/cleanlab` + co-teaching reimpl. | annotate-everything arm |
| Vision annotator | Grounded-DINO + `facebookresearch/segment-anything` | per-item dense annotation at real compute cost |
| Vision learner | detectron2 Mask R-CNN | student for the dense pool |
| Adjacent-prior check | FreeAL (EMNLP 2023), MoLLIA (AAAI 2026), ActiveLLM (TACL) | none measures the uncertainty–error correlation or runs matched-cost annotate-everything; cite and position |

### 3.3 Compute & cost

Phase 1: ~$1.5K API + ~120 GPU-h (learner training + VLM annotation of 5K images). Phase 2: ~$4–6K API + ~400 GPU-h (AL loops are small-model retraining). Cheapest killer in the cluster.

### 3.4 Risks & abort gates

- Effect-size heterogeneity across annotator/task pairs is expected; the design reports the correlation *grid*, and Phase 2 only proceeds where Phase 1 found signal (honest scoping, not cherry-picking — the grid is published either way).
- Circularity attack answered by construction: reliability predictor = annotator self-consistency only.
- Abort gate = the Phase-1 decision rule itself.

### 3.5 Practice change & verdict

Changes how people run annotation *pipelines* (training-data acquisition), with deployable advice in every branch.

**VERDICT: DROP from the top-2 (declined the optional-3rd slot).** The killer measurement is exceptional and cheap — but the *paper* is not: the binding-budget settings and matched-cost arms push Phase 2 into real spend, and the deliverable is pipeline advice, a step below the top two's training-recipe changes in the "change how people train/evaluate" preference ordering. **Recommendation to Supervisor:** run Phase 1 as a ~$2K rider during the C-0090/C-0028 program; promote to full nomination next cycle iff ρ ≥ 0.3 lands.

---

## 4. C-0310 — The camera ISP is a bigger domain axis than the weather

**Claim under test:** Cross-device ISP shift (real pipelines on identical RAW frames) degrades dense-task accuracy on par with or beyond real clear→adverse weather shift; ISP-randomized training is the cheap fix.
**Stage-4 mandatory condition (kept):** real-device anchoring on both axes.

### 4.1 KILLER EXPERIMENT — "Two empirical distributions, one comparison"

- **ISP axis (treatment = re-render, labels exactly invariant):** identical RAW frames rendered through N ≥ 8 *real* pipelines: LibRaw/`rawpy` (2 parameterizations), RawTherapee-cli with 3 real camera-profile PP3s, darktable-cli with 2 XMP styles, `openISP`-class pure-Python ISP tuned to phone-like and automotive-like configurations (the `debayer` batch tool automates the RawTherapee/darktable legs). Pipeline set justified as spanning real device families, not an author grid.
- **RAW data with labels (all verified real):** PASCALRAW (4,259 RAW, det: person/car/bicycle), NOD/RAW-NOD (7.2K RAW night, det), RAOD/ROD (`huawei-noah/noah-research/RAOD`, ~20K 24-bit day+night driving, det), MultiRAW (5 sensors, det). RAWDet-7 (arXiv:2602.03760) consolidates these with standardized labels — adopt its splits. Detection first; a 500-frame dense-segmentation annotation batch (annotated once per RAW frame, valid across all renders) is a gated extension.
- **Weather axis (real, paired):** ACDC — 4,006 adverse images with *corresponding same-scene clear references* (1,503 clear references now annotated), fog/rain/snow/night.
- **Models:** 8 pretrained detectors/segmenters (COCO-pretrained DINO/Faster R-CNN family; Cityscapes-pretrained SegFormer/Mask2Former/DeepLabv3+ from MMSegmentation zoo for the ACDC leg and the seg extension).
- **Measurement:** (i) cross-ISP drop matrix — every model evaluated on every render; per-model spread = max−min and pairwise-median mAP/mIoU deltas over identical frames/labels; (ii) clear→adverse per-condition drops on ACDC matched scenes for the same segmenters. Both axes are now empirical distributions over real hardware/weather — the incommensurability attack dies by construction.
- **Pre-registered decision rule:** compare median cross-ISP drop vs median clear→adverse drop with paired bootstrap CIs. ISP ≥ weather → headline stands; ISP within [0.5×, 1×] weather → "second axis of comparable magnitude" (still deployment-relevant); ISP < 0.25× weather → the cross-device panic is quantified away — publish the negative with the drop matrix as the first cross-ISP benchmark table.
- **Training arm (the practice-change payload):** ISP-randomized augmentation (sample a real pipeline per training image at RAW load time) on RAOD; baseline = Rawgment-style noise-accounted augmentation **reimplemented** (CVPR 2023 paper has no public code — verified this session; reimplementation is ~2 weeks of the augmentation math, treated as a deliverable artifact) + standard sRGB augmentation. Evaluate held-out-pipeline generalization.

### 4.2 Compute & cost

Rendering: CPU-bound (~10⁵ frame-renders, embarrassingly parallel). Evaluation matrix: ~150 GPU-h. Training arm: ~600 GPU-h (detector training × arms × 2 seeds). Dense-label extension: ~$8–12K annotation (gated). Protocol-controlled scoring harness shared with C-0302 (the C-0276 salvage).

### 4.3 Risks & drop rationale

The intervention is genuinely clean (labels invariant under treatment) and the data risk is smaller than Stage 4 feared (RAWDet-7 exists). But: (a) the headline remains a *magnitude-comparison audit* — the training arm is the only practice-change component and it contends with Rawgment's published territory plus a reimplementation dependency; (b) dense-task claims (the cluster's charter) need new annotation money; (c) detection-first weakens the "bigger than weather *for segmentation*" headline. **DROP — rank 4. Revival trigger:** a public RAW driving set with dense labels (ecosystem is moving — RAWDet-7 appeared this year), or supervisor approval of the annotation budget; the design above is then fully runnable as written.

---

## 5. C-0302 — Last-layer group-robustness fixes fail on spatially entangled bias

**Claim under test:** DFR-style last-layer sufficiency, celebrated for classification, does not transfer to dense prediction where bias is spatially entangled — tested by dissociation on identical images, with a constructive retraining-depth deliverable.
**Stage-4 mandatory condition (kept):** the same-images classification-vs-dense dissociation.

### 5.1 KILLER EXPERIMENT — "Waterbirds-Seg dissociation"

- **Dataset construction (cheap, fully controlled):** rebuild Waterbirds *with masks* — the original was CUB birds cut-pasted onto Places backgrounds via `kohpangwei/group_DRO` scripts; CUB ships segmentation masks, so the dense version (per-pixel bird class + background) falls out of the same compositor. Correlation dial: planted bird-class↔background correlation at {0.5, 0.7, 0.9, 0.95, 1.0} (graded, not the 100% cartoon).
- **Two readouts on identical images, same ResNet-50 backbone:** (i) classification head (global pool + linear); (ii) dense head (per-pixel 1×1 conv readout, and a DeepLabv3+ decoder as the realistic variant) — trained per task mode on the biased data.
- **Intervention:** DFR exactly per `PolinaKirichenko/deep_feature_reweighting` / `izmailovpavel/spurious_feature_learning`: retrain only the readout on a small group-balanced set. Worst-group accuracy (cls) vs worst-group IoU (dense), recovery fraction = (post-DFR − biased) / (balanced-oracle − biased).
- **Pre-registered decision rule:** dense recovery ≥ 80% of classification recovery at matched correlation → DFR *extends* (celebrated cheap fix works for dense — positive surprise, publish); ≤ 30% → bias lives in spatial feature mixing → run the **retraining-depth curve** (retrain top-k blocks on balanced data, k = 1…4) yielding the transferable "debiasing depth" quantity; intermediate → the correlation-strength dose-response is the result. The *dissociation on identical images* is the finding in every branch.
- **Natural-bias arm:** context-entangled Cityscapes classes (rider↔bicycle, sidewalk↔road context) with group splits defined by co-occurrence statistics — one arm, pre-registered, to answer the cartoon objection.

### 5.2 Cost & drop rationale

~400–700 GPU-h total (small datasets, readout retraining is minutes; depth-curve is the main spend). Clean, cheap, genuinely open outcome. **DROP — rank 5:** the deliverable is a diagnosis plus a depth knob for the subcommunity that uses last-layer debiasing on dense tasks — a real but narrow practice change, outranked by the top two's field-wide training-recipe implications. Strong revival candidate for a workshop-to-main-track pipeline if a nominee dies at Stage 6; shares the protocol-controlled eval harness with C-0310.

---

## 6. C-0128 — Generative editing enables causal measurement of context reliance in segmentation

**Claim under test:** Inversion/inpainting-based counterfactual scene edits yield a valid, editor-independent, per-class context-reliance score for dense models, which links to shift robustness.
**Stage-4 mandatory condition (kept):** the real-photo anchor (leg iii).

### 6.1 KILLER EXPERIMENT — the three validity legs (instrument qualification before any science)

- **Leg i — null-edit calibration:** invert-and-reconstruct (no semantic change) every evaluation image per editor; per-model response to null edits = artifact noise floor; all context effects reported as excess.
- **Leg ii — cross-editor invariance:** ≥3 *architecturally unrelated* editing systems, all verified public: LaMa via `geekyutao/Inpaint-Anything` (non-diffusion inpainter), PowerPaint (`open-mmlab/PowerPaint`, SD-based, removal mode), OmniPaint (`yeates/OmniPaint`, FLUX-based removal+insertion incl. shadows/reflections). Per-class score agreement across editors: Spearman ρ ≥ 0.8 required.
- **Leg iii — physical anchor (the one no artifact objection survives):** CDnet 2014 (`changedetection.net`) — static-camera videos with per-frame pixel-accurate foreground ground truth; the *intermittent object motion* category provides genuine present/absent pairs of the same scene at zero generative artifact. Compute the real-pair context score on overlapping classes (person, car, ...); synthetic score must match: ρ ≥ 0.7 on shared classes.
- **Decision rule:** any leg fails → the instrument is dead; publish the negative as a methods caution (cheap). All legs pass → fund the measurement: 100+ classes × 3 datasets (COCO, ADE20K, Cityscapes), segmenters from the MMSegmentation zoo + SAM-family, frequency/scale partialled out, robustness linkage to cross-dataset transfer drops.

### 6.2 Cost & drop rationale

Edit generation ~300–500 GPU-h (inference only, 3 editors × ~30K edits + nulls); measurement phase ~200 GPU-h. **DROP — rank 6:** even with the best validation design in the cluster, the deliverable is an *instrument + score* — the practice change (context-decorrelation training targets) is downstream work the paper motivates but does not perform. Under this stage's explicit preference against instrument/audit deliverables, it cannot displace the top two. High-quality fallback; legs i–iii are also independently reusable infrastructure for any future counterfactual-eval project (adjacent to B-0121's counterfactual audit, per the Stage-4 cross-cluster note).

---

## 7. C-0229 — Multi-task pretraining's benefit is the data, not the tasks

**Claim under test:** Most of the multi-task pretraining advantage on held-out transfer survives when image diversity is equalized (single task on pooled images) — the decomposition number the field lacks.
**Stage-4 mandatory condition (kept):** fully-labeled corpora only; no pseudo-label arm.

### 7.1 KILLER EXPERIMENT — "Exact-control decomposition on COCO"

- **Corpora where the control is exact (verified):** COCO 2017 train (118K images with boxes, masks, captions, keypoints — all label types on the same pooled images) and Hypersim (`apple/ml-hypersim`, 77,400 images with depth, normals, semantic/instance labels on identical frames; download scripts shipped).
- **Arms (ViT-S backbone):** MT-pooled (all tasks, all images) / ST-pooled per task (one task's labels, all images) / ST-own per task (one task, ¼-subset "own" images). Trainers: `median-research-group/LibMTL` (JMLR library: 8 architectures, 16 weighting strategies — kills the "your MT baseline is weak" objection) with `EPFL-VILAB/MultiMAE` as the pretraining-flavored replicate.
- **Two compute conventions side by side:** matched gradient-steps×tokens and matched wall-clock FLOPs — the war becomes a robustness table.
- **Transfer:** held-out tasks/datasets — ADE20K (linear + fine-tune), NYUv2 depth, VOC detection.
- **Decomposition:** D_task = [MT-pooled − ST-pooled], D_data = [ST-pooled − ST-own]; the deliverable is the ratio, with a 10×-pooled-images single-task arm (CC-scale images, one task) as the two-point scale sweep.
- **Decision rule:** D_task < 25% of total under both conventions → "it's the data"; > 75% → "it's the tasks"; the middle *is* the priced decomposition — informative but headline-soft.

### 7.2 Cost & drop rationale

The arm grid is large: (1 MT + 4 ST-pooled + 4 ST-own) × 2 corpora × 2 seeds + scale arm ≈ 20+ pretraining runs ≈ **6–9K A100-h** — the most expensive design in the cluster, and the celebrated claims being deflated live 100× above the affordable scale, so the scale-transfer escape hatch survives any budget we command. **DROP — rank 7 (worst ROI):** right control, real lever, but cost-per-decision is the cluster's worst and the likely outcome (the known middle) prices an investment question without changing a training recipe.

---

## Shared infrastructure note (C-0276 salvage, per Stage 4)

The fixed-checkpoint, protocol-pinned evaluation harness (checksummed data manifests, frozen eval configs committed before runs, single scoring path for all arms) is implemented once during the C-0090 bootstrap and reused by every design above; it is deliberately *not* a paper (Stage-4 kill of C-0276 upheld).

## Cross-cluster check

No collision with A-cluster keeps (SAM/promptable program) or B-cluster keeps (medical program). C-0090 is adjacent to A-0107 (PEFT forgetting) — different mechanism (optimization balance vs readout locus), different model class; flagged for the Stage-6 portfolio view, no consolidation needed.
