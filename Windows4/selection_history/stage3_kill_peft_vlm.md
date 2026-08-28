# Stage 3 — Prior-Work Assassination: PEFT / Forgetting / VLM / Annotation-Efficiency clusters

Role: Prior-Work Assassin. Default assumption: **already published**. Date: 2026-08-28.
Scope: 18 clusters assigned from `stage2_top200.md` (clusters 8, 18–24, 32–39, 43–45 of the cluster-lead list, plus A1-107/A1-108).
Method: **web-verified real papers only.** Every load-bearing citation below was fetched and read this pass unless
marked `[M]` = memory-cited classic (high confidence it exists, but re-verify the arXiv ID before quoting in a paper).
Unmarked / `[V]` = verified this session (abstract or full text fetched).

Epistemic status: REVIEW JUDGMENT on novelty. No claim below is an experimental result of ours.

Verdict scale per rubric:
- **Overlap**: NONE (no credible prior), SLIVER (partial overlap; a defensible delta remains), REAL (the core claim or its decisive version is published).
- **Verdict**: KILL (no publishable delta), MUTATE (survives only in a modified form; modification specified), SURVIVE (delta is real; differencing obligations listed).
- **R2 attack paper**: the single paper a hostile reviewer will paste into the rejection.

Banned-pattern check (from `stage2_review_C1_audit.md`): each verdict states which false-novelty pattern (F1–F9) the idea
risked; F2 = cls→seg port without divergence mechanism, F3 = prompt-perturbation amnesia, F5 = weight-arithmetic port,
F7 = convergent-duplicate double counting, F8 = strawman assumption.

---

## Scoreboard

| # | Cluster | IDs | Overlap | Verdict |
|---|---|---|---|---|
| 1 | PEFT tax on SAM promptability | S-141, C1-097, C1-065 | REAL (phenomenon) / SLIVER (audit) | S-141 KILL · C1-097 MUTATE · C1-065 SURVIVE |
| 2 | Random LoRA ≈ trained | S-148 | REAL | KILL (demote to control arm) |
| 3 | Protocol forgetting boxes→points | S-176 | SLIVER | MUTATE |
| 4 | Forgetting in decoder not encoder | S-177, C1-062 | SLIVER | SURVIVE (with differencing) |
| 5 | Plasticity too small → forgetting is noise | S-183, C1-082 | SLIVER | SURVIVE (as gatekeeper audit) |
| 6 | FT calibration tax | C1-025, C1-031, C1-037, S-318 | SLIVER | MUTATE (merge; C1-031 is the core) |
| 7 | Pretrain-harm small-n | S-052 | SLIVER | MUTATE |
| 8 | PEFT vs tuned full-FT honesty | C1-053 | REAL | KILL (fold into #1) |
| 9 | PEFT data-size crossover | C1-057 | REAL | KILL (report as arm only) |
| 10 | Gain–retention frontier | C1-110 | REAL (components) | MUTATE |
| 11 | LoRA placement vs error type | A1-107 | NONE→SLIVER | SURVIVE |
| 12 | Encoder–decoder contract drift | A1-108, C1-067 | SLIVER (shrinking) | MUTATE |
| 13 | VLM prior harms rare/atypical + negation | S-228, S-240, B1-107 | REAL (negation, frequency) / SLIVER (dense) | S-240 KILL · S-228 MUTATE · B1-107 SURVIVE |
| 14 | AL / semi-sup dead under VFM init | B1-011, B1-025 | REAL | KILL both |
| 15 | Copy-paste ≥ diffusion synth | B1-051 | SLIVER | SURVIVE |
| 16 | Histogram matching explains UDA | B1-061 | REAL (in spirit) | MUTATE |
| 17 | FSS support variance / background cheat | B1-074, B1-079 | SLIVER | B1-074 MUTATE · B1-079 SURVIVE |
| 18 | CLIP dense linear realignment | B1-097 | REAL | KILL |

Net: 7 KILL, 6 MUTATE, 5 SURVIVE (counting sub-IDs: 10 kill-level, 8 mutate, 7 survive).

---

## 1. PEFT tax on SAM promptability — S-141 ("LoRA on SAM encoder destroys promptability"), C1-097 (unified PEFT-for-SAM replication audit), C1-065 (prompt-type-specific forgetting)

**Closest real papers**
- Gu et al., *How to build the best medical image segmentation algorithm using foundation models: a comprehensive empirical study with Segment Anything Model*, MELBA 2025, arXiv:2404.09957 `[V]`. 18 fine-tuning combinations (3 backbones × encoder/decoder × vanilla/LoRA/Adapter) × 17 datasets. Explicitly documents that **vanilla full fine-tuning causes model collapse / catastrophic forgetting** on ViT-B/H and that PEFT in encoder+decoder is superior; explicitly "demonstrate[s] the ineffectiveness of some methods popular in the literature"; includes decoder-only FT (their "FT-SAM"-style arm) and prompt-based settings.
- *Continual Alignment for SAM (CA-SAM)*, arXiv:2511.17201 `[V]`. States as motivation that fine-tuned SAMs "tend to erode SAM's generalization, yielding poor OOD performance," and builds a method that adapts per task **while preserving zero-shot behavior on unseen medical datasets** (9-dataset continual benchmark).
- EvoSAM, arXiv:2503.06236 `[V]`: LoRA-expert continual SAM, benchmarked against CL baselines applied to SAM/MedSAM — the "SAM forgets, fix it" lane is already occupied.
- Zhang & Liu, SAMed, arXiv:2304.13785 `[M]`; Wu et al., Medical SAM Adapter (in our anchors) — the constructive PEFT-on-SAM lane is saturated.
- Kumar et al., *Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution*, ICLR 2022, arXiv:2202.10054 `[M]`; Wortsman et al., WiSE-FT, CVPR 2022, arXiv:2109.01903 `[M]` — the generic "adaptation costs zero-shot robustness" result.

**What they did vs. what we claimed.** S-141's headline ("PEFT/FT erodes SAM's zero-shot ability") is now
*motivation-section boilerplate* — CA-SAM asserts it with citations, Gu et al. measured collapse, Conv-LoRA
(arXiv:2401.17868 `[V]`) advertises "preserves SAM's segmentation knowledge" as a selling point. C1-097's replication
thesis ("half of PEFT-for-SAM methods fail to beat a tuned decoder-only baseline") is substantially executed by
Gu et al.: same-budget unified protocol, decoder-only arm, popular methods shown ineffective.

**Exact difference that remains.** Nobody measures the tax **behaviorally, per prompt type, on held-out natural
categories, at matched in-domain gain**: zero-shot box vs point vs negative-click vs multimask-diversity retention
(C1-061's diversity collapse), with the LR confound (C1-076) and threshold artifact (C1-082) controlled. Gu et al.
measure in-domain Dice; CA-SAM measures OOD Dice of *their* method, not a controlled audit of the field's checkpoints.

**Overlap:** REAL for the phenomenon and for the unified-replication framing; SLIVER for the prompt-resolved behavioral audit. Confidence: high (three independent verified sources). Banned-pattern risk: F7 (×3 convergence was a warning, correctly).

**R2 attack paper:** Gu et al. arXiv:2404.09957 (+ CA-SAM arXiv:2511.17201).

**Verdict:** S-141 **KILL** as a standalone "document the harm" paper. C1-097 **MUTATE**: drop the replication framing
(done by Gu et al.), keep only pre-registered rank-flip tests on *released* checkpoints. C1-065 **SURVIVE** as the
cluster's core: the promptability-tax battery (per-prompt-type zero-shot retention + ambiguity forgetting), explicitly
differenced against Gu et al. §prompt experiments and CA-SAM's OOD tables.

---

## 2. Random LoRA ≈ trained — S-148 ("random LoRA directions with same rank almost match trained LoRA on seg")

**Closest real papers**
- Kopiczko, Blankevoort & Asano, *VeRA: Vector-based Random Matrix Adaptation*, ICLR 2024, arXiv:2310.11454 `[V]`.
  **Frozen, randomly initialized, layer-shared low-rank matrices** with only tiny trained scaling vectors **match LoRA**
  on GLUE, E2E, image classification, and 7B/13B instruction tuning.
- Aghajanyan et al., *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning*, arXiv:2012.13255 `[M]`; Li et al., *Measuring the Intrinsic Dimension of Objective Landscapes*, ICLR 2018, arXiv:1804.08838 `[M]` — training inside **random subspaces** suffices; the "directions don't matter much, capacity does" point is a decade of evidence.

**What they did vs. what we claimed.** VeRA is precisely "random directions + minimal calibration ≈ trained LoRA,"
demonstrated across modalities including vision. The "shock" S-148 was protected for ("if random matches trained, the
PEFT literature loses its floor") already happened, and the field absorbed it as a *method* (VeRA is in HuggingFace PEFT).

**Exact difference that remains.** Only the instantiation "on SAM / dense masks" and the stronger literal reading
(*zero* trained scaling — which is almost certainly false and uninteresting: an untrained random ΔW is noise injection).
A seg-specific version predicts nothing different from VeRA — banned pattern F2 (port without divergence mechanism).

**Overlap:** REAL. Confidence: high. **R2 attack paper:** VeRA arXiv:2310.11454.

**Verdict:** **KILL** as a paper. Salvage: random-direction PEFT (VeRA-style) becomes a **mandatory control arm** in the
cluster-1 audit — any PEFT-for-SAM gain must beat it. That is a baseline, not a hypothesis.

---

## 3. Protocol forgetting boxes→points — S-176 ("train on boxes, point Dice crashes below frozen SAM")

**Closest real papers**
- Ma et al., *Segment Anything in Medical Images* (MedSAM), Nature Communications 2024, arXiv:2304.12306 `[M]`.
  Trained box-only; the paper and repo document that point prompting is unsupported/poor — the community already
  knows box-specialized FT does not transfer to points.
- Cheng et al., SAM-Med2D, arXiv:2308.16184 `[V]`. Fine-tunes **with boxes+points+masks precisely because** prompt-mode
  coverage matters, and reports the full Bbox/1pt/3pt/5pt table for SAM vs FT-SAM vs SAM-Med2D (SAM 1pt = 18.94 Dice vs
  FT variants 60–70) — prompt-mode-resolved evaluation after FT exists.
- Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024, arXiv:2304.14660 `[M]` (our own anchor):
  prompt-type sensitivity of frozen SAM is mapped.

**What they did vs. what we claimed.** The ingredients (prompt-mode tables after FT; box-only models that can't point)
are published. What is *not* published: the **within-model prompt-transfer matrix framed as forgetting** — FT on
protocol A, measure degradation on protocol B **relative to the frozen model** ("drops below frozen SAM" is the
falsifiable, new part), including negative clicks and iterative refinement depth (C1-063), with threshold re-tuning
(C1-082) ruled out.

**Overlap:** SLIVER. Confidence: medium-high (a direct "prompt-protocol forgetting" paper may exist in 2025-26 workshops;
none surfaced in this pass). **R2 attack paper:** SAM-Med2D + MedSAM ("we already know box-only can't point — so what?").

**Verdict:** **MUTATE**: merge into the C1-065 battery (cluster 1's survivor). The standalone claim is a table other
papers half-contain; the survivor is the *below-frozen-baseline* regression and its prompt-type ordering.

---

## 4. Forgetting in decoder not encoder — S-177 (freeze ablation), C1-062 (cross-attn re-splicing restores zero-shot)

**Closest real papers**
- Ramasesh et al., *Anatomy of Catastrophic Forgetting: Hidden Representations and Task Semantics*, arXiv:2007.07400 `[M]`:
  forgetting concentrates in deeper layers (classification).
- Davari et al., *Probing Representation Forgetting in Supervised and Unsupervised Continual Learning*, CVPR 2022,
  arXiv:2203.13381 `[M]`: representation- vs output-level forgetting probes.
- Lee et al., *Surgical Fine-Tuning Improves Adaptation to Distribution Shifts*, ICLR 2023, arXiv:2210.11466 `[M]`:
  which block to tune depends on shift type — the constructive twin of the locus question.
- Gu et al. arXiv:2404.09957 `[V]`: encoder-vs-decoder tuning arms for SAM exist (as performance, not forgetting-locus, analysis).
- CA-SAM arXiv:2511.17201 `[V]`: locates the adaptation problem at the **encoder–decoder interface** (their Alignment Layer) — evidence the interface framing is being methodized.

**Exact difference that remains.** No paper does the **causal layer-swap / re-splice restoration** on a promptable mask
decoder: splice pre-FT prompt cross-attention back into a fine-tuned SAM and measure how much zero-shot returns. The
classification "deep layers forget" result does not predict where forgetting lives in an encoder(frozen-ish)/
prompt-decoder architecture — there is a genuine divergence mechanism (prompt cross-attn has no cls analogue), which
clears banned pattern F2.

**Overlap:** SLIVER. Confidence: medium (SAM-specific locus papers are plausible in the CL-for-SAM wave; none found).
**R2 attack paper:** Ramasesh arXiv:2007.07400 ("known for deep nets") + surgical fine-tuning.

**Verdict:** **SURVIVE**, conditional on: (a) citing and differencing Ramasesh/Davari/Lee; (b) running Gu et al.'s
enc/dec arms as baselines; (c) the deliverable being the *restoration* result (mechanism), not the freeze ablation
(S-177 alone is one figure, not a paper — fold it in).

---

## 5. Plasticity too small, forgetting is noise — S-183, C1-082 (threshold artifact)

**Closest real papers**
- Biderman et al., *LoRA Learns Less and Forgets Less*, TMLR 2024, arXiv:2405.09673 `[V]`. The learning–forgetting
  **coupling** is quantified for LLMs: less plasticity ⇒ less forgetting, controlled by rank; forgetting tracks how much
  was learned. This is the exact conceptual engine behind S-183.
- Soutif et al., *An Empirical Analysis of Forgetting in Pre-trained Models with Incremental Low-Rank Updates*,
  CoLLAs / PMLR v274, 2025 `[V]`: LoRA-rank vs plasticity and forgetting **for vision transformers**.
- CoDyRA, arXiv:2412.01004 `[V]`: rank/placement vs plasticity–stability trade-off, again vision.
- Maier-Hein et al., *Metrics Reloaded*, Nature Methods 2024 `[M]`: operating-point/threshold pitfalls in segmentation
  metrics are canon — C1-082's mechanism is insider-known (banned-pattern F1 risk) but **unapplied to forgetting claims**.

**Exact difference that remains.** Nobody has audited the now-sizeable SAM-continual-learning literature (CA-SAM,
EvoSAM, SynESAM…) for **whether reported "forgetting" exceeds the noise floor implied by (tiny task-2 gain ×
threshold/binarization artifacts × seed variance)**. The LLM coupling result makes this *more* likely to be true, not
less novel: it predicts small-plasticity seg fine-tunes should show small true forgetting — so published big deltas are
suspect.

**Overlap:** SLIVER (coupling REAL for LLMs; the deflation audit for dense/promptable models NONE-found). Confidence:
medium-high. **R2 attack paper:** Biderman arXiv:2405.09673 ("we know forgetting scales with learning").

**Verdict:** **SURVIVE** — and per the C1 audit, run **first** as the gatekeeper of the whole Forget thread. C1-082 is a
mandatory control inside it, not a separate paper. Obligation: frame against Biderman/Soutif as *confirming the coupling
in a new regime and using it to deflate published claims*, not as discovering it.

---

## 6. FT calibration tax — C1-025 (PEFT preserves calibration), C1-031 (FT desyncs IoU head), C1-037 (PEFT loses robustness), S-318 (calibration breaks faster than Dice)

**Closest real papers**
- Yang et al., *Bayesian Low-rank Adaptation for Large Language Models* (Laplace-LoRA), ICLR 2024, arXiv:2308.13111 `[V]`:
  documents that (Lo)RA-fine-tuned models become **overconfident/miscalibrated**, and fixes it; a whole Bayesian-PEFT
  literature (BLoB NeurIPS 2024 `[V]`, SWAG-LoRA arXiv:2405.03425 `[V]`) now exists — "PEFT calibration" is not virgin ground.
- Kumar et al. arXiv:2202.10054 `[M]` + WiSE-FT arXiv:2109.01903 `[M]`: fine-tuning trades OOD robustness for ID gain
  (classification); C1-037's thesis at the concept level.
- Gu et al. arXiv:2404.09957 `[V]`: PEFT protects against collapse in SAM tuning — partial counter-evidence/overlap for C1-037's direction.
- Minderer et al., *Revisiting the Calibration of Modern Neural Networks*, NeurIPS 2021, arXiv:2106.07998 `[M]`: calibration vs accuracy across model families, incl. zero-shot models.

**Exact difference that remains.** (a) All calibration results above are **classification/LLM**; matched-mIoU
pixel/mask calibration for full-FT vs PEFT on dense prediction is unmeasured (C1-032's divergence rule applies: dense
losses like Dice/focal plausibly invert cls conclusions — a mechanism, not a port). (b) **C1-031 is the only genuinely
fresh object**: SAM has a *separate confidence head* (IoU token); no paper tracks whether FT desynchronizes it from the
mask head. C1-026 (OOD miscalibration of the IoU head, protected elsewhere) is its zero-shot sibling.

**Overlap:** SLIVER overall; REAL for "fine-tuned models are miscalibrated" as a genre. Confidence: medium-high.
**R2 attack paper:** Laplace-LoRA arXiv:2308.13111 + WiSE-FT.

**Verdict:** **MUTATE** — collapse the four IDs into one paper: *matched-accuracy calibration+robustness frontier of
seg adaptation, with IoU-head desync (C1-031) as the mechanistic core and S-318's "ECE breaks before Dice" as the
ordering claim*. C1-025 and C1-037 alone are F2 ports; they live only as arms.

---

## 7. Pretrain-harm small-n — S-052 ("SAM/ImageNet init < random init on tiny lesions at n=50")

**Closest real papers**
- Raghu et al., *Transfusion: Understanding Transfer Learning for Medical Imaging*, NeurIPS 2019, arXiv:1902.07208 `[M]`:
  ImageNet transfer gives surprisingly little benefit on medical tasks; small scratch models match.
- He et al., *Rethinking ImageNet Pre-training*, ICCV 2019, arXiv:1811.08883 `[M]`: random init matches pretraining on
  COCO given schedule, **including down to 10% data** for detection/seg.
- Zoph et al., *Rethinking Pre-training and Self-training*, NeurIPS 2020, arXiv:2006.06882 `[M]`: pre-training can
  actively **hurt** — but in the strong-augmentation / larger-data regime, the *opposite* regime to S-052's.
- Gu et al. arXiv:2404.09957 `[V]` and C1-087's twin thread: scale–data interactions under small-n FT are being mapped.

**What they did vs. what we claimed.** "Pretraining may not help medical" is published (Transfusion); "pretraining can
hurt" is published (Zoph, large-data). S-052's specific regime — **harm at n≈50 with tiny, sparse lesions, from
SAM/foundation init specifically** — is not published, and standard lore predicts the opposite (transfer helps most at
small n), which makes it a true contrarian bet rather than a scoop.

**Exact difference / mechanism obligation.** Must ship a mechanism, not a curve: S-054's objectness-prior conflict
(SAM's thing-prior fighting amoeboid low-contrast lesions) is the differencing lever; otherwise reviewers file it under
Transfusion-redux.

**Overlap:** SLIVER. Confidence: medium. **R2 attack paper:** Transfusion arXiv:1902.07208 + Zoph arXiv:2006.06882.

**Verdict:** **MUTATE**: from "FM features hurt at small n" (crowded framing) to "the objectness prior of
segmentation-pretrained encoders is a measurable liability for stuff-like/atypical lesions at small n" — learning-curve
crossover + prior-ablation. High null-risk accepted (it was protected for exactly this).

---

## 8. PEFT vs tuned full-FT honesty — C1-053 ("LR-swept full FT matches published seg-PEFT gains")

**Closest real papers**
- Gu et al. arXiv:2404.09957 `[V]`: unified same-budget protocol across 18 strategies/17 datasets; explicitly
  "demonstrate the ineffectiveness of some methods popular in the literature"; includes decoder-only and vanilla-FT arms.
  This *is* the baseline-honesty audit for SAM PEFT, executed.
- Dutt et al., *Parameter-Efficient Fine-Tuning for Medical Image Analysis: The Missed Opportunity*, MIDL 2024,
  arXiv:2305.08252 `[V]`: 17 PEFT algorithms, 700+ controlled runs, full-FT baselines swept across data volumes.
- Biderman et al. arXiv:2405.09673 `[V]`: with proper tuning, **full FT beats LoRA in-domain** (LLM) — the honesty result at the concept level.

**Exact difference that remains.** Re-running *published papers'* exact claims against a swept baseline (replication
of specific numbers) — but that is Gu et al.'s "ineffectiveness" finding plus a longer appendix; venues will read it as
incremental replication.

**Overlap:** REAL. Confidence: high. **R2 attack paper:** Gu et al. arXiv:2404.09957.

**Verdict:** **KILL** as standalone. The honest-baseline discipline folds into cluster 1's surviving audit
(every arm there carries an LR-swept full-FT/decoder-FT control). C1-053's Protect status transfers to C1-065.

---

## 9. PEFT data-size crossover — C1-057 ("crossover at low-hundreds of images; above it full FT wins")

**Closest real papers**
- Dutt et al. arXiv:2305.08252 `[V]`: **the crossover chart exists** — "at 100% of downstream data full fine-tuning is
  optimal… as availability decreases the benefits of PEFT increase; the crossover is at 50%… LoRA overtakes the baseline
  as early as 80% (ViT-L)". Medical imaging, ViT-B/L, multiple datasets.
- Jia et al., *Visual Prompt Tuning*, ECCV 2022, arXiv:2203.12119 `[M]`: VPT-vs-full-FT data-scale regime dependence (classification).
- Gu et al. arXiv:2404.09957 `[V]`: SAM-specific data regimes incl. few-shot setups.
- Biderman et al. arXiv:2405.09673 `[V]`: regime dependence for LLMs.

**Exact difference that remains.** Only "for segmentation, in absolute image counts, per backbone size" — a grid cell,
not a question. Banned pattern F2/F7 (it converged ×3 across our batches because it's in the field's bloodstream).

**Overlap:** REAL. Confidence: high. **R2 attack paper:** Dutt et al. arXiv:2305.08252.

**Verdict:** **KILL** as a paper; keep as one reported curve inside cluster-1's audit. (Its Stage-2 Protect status is
hereby revoked with cause.)

---

## 10. Gain–retention frontier benchmark — C1-110

**Closest real papers**
- WiSE-FT, CVPR 2022, arXiv:2109.01903 `[M]`: the ID-gain-vs-zero-shot-retention **frontier is the paper's central
  figure** (interpolation traces it continuously).
- Ilharco et al., *Editing Models with Task Arithmetic*, ICLR 2023, arXiv:2212.04089 `[M]`: target-vs-control-task
  trade-off evaluation for weight-space edits.
- Lopez-Paz & Ranzato, GEM, NeurIPS 2017, arXiv:1706.08840 `[M]`: BWT/FWT — standardized gain-vs-retention scalars in CL for a decade.
- CA-SAM arXiv:2511.17201 `[V]`: already reports adaptation + zero-shot retention across 9 medical datasets for SAM —
  the community is producing these tables without our benchmark.

**Exact difference that remains.** A *standardized, promptable-segmentation-specific* suite (per-prompt-type retention,
frontier scalar, model cards). Formulation-only novelty; every component exists.

**Overlap:** REAL on components. Confidence: high. **R2 attack paper:** WiSE-FT + GEM ("you renamed BWT").

**Verdict:** **MUTATE**: survives only as the **reporting protocol + leaderboard** attached to the cluster-1/5/6
empirical papers (the C1-117 model-card arm), with at least one pre-registered rank flip demonstrated (per banned-pattern
F4/F6 rule). Not fundable as a standalone benchmark paper.

---

## 11. LoRA placement vs error type — A1-107 ("attention-LoRA fixes boundaries; MLP-LoRA fixes regions")

**Closest real papers**
- He et al., *Towards a Unified View of Parameter-Efficient Transfer Learning*, ICLR 2022, arXiv:2110.04366 `[M]`:
  placement matters (NLP; task-level metrics only).
- Zhong et al., *Convolution Meets LoRA*, ICLR 2024, arXiv:2401.17868 `[V]`: placement/inductive-bias engineering for
  SAM PEFT (conv-in-LoRA injects local priors); shows placement/architecture choices move seg quality — but never
  decomposes **which error type** each placement fixes.
- CoDyRA arXiv:2412.01004 `[V]`: placement × rank vs learning/forgetting — again task-level, not error-type-level.
- C1-052 (killed as dup) and S-144/S-91 (killed as cartography) are our own inferior twins — correctly folded here.

**Exact difference.** Mapping *adapter placement → boundary-F vs interior-IoU error decomposition* is unfound. It makes
a falsifiable, mechanism-flavored prediction (attention moves long-range grouping/boundaries; MLP moves local texture
classification) that Conv-LoRA's local-prior narrative partially *contradicts* — an honest kill-or-confirm setup.

**Overlap:** NONE found for the error-type mapping; SLIVER for placement studies generally. Confidence: medium
(placement papers are numerous; an error-decomposed one may lurk). **R2 attack paper:** He et al. arXiv:2110.04366 + Conv-LoRA.

**Verdict:** **SURVIVE.** Obligations: matched-param placements; boundary/interior decomposition pre-registered;
Conv-LoRA as baseline and as the theory being tested; stated risk (effects don't decompose cleanly) is the null.

---

## 12. Encoder–decoder contract drift — A1-108 (interface drift statistic), C1-067 (CKA drift as early warning)

**Closest real papers**
- CA-SAM arXiv:2511.17201 `[V]`: builds an **Alignment Layer that aligns encoder–decoder feature distributions** in SAM —
  the "interface contract" is no longer just a framing; it is a shipped method.
- Kornblith et al., CKA, ICML 2019, arXiv:1905.00414 `[M]`; Bansal et al., *Revisiting Model Stitching*, NeurIPS 2021,
  arXiv:2106.07682 `[M]`: representation-compatibility measurement across module boundaries is mature.
- Davari et al. arXiv:2203.13381 `[M]`: CKA-style drift as a forgetting probe in CL.
- Merchant et al., *What Happens To BERT Embeddings During Fine-tuning?*, arXiv:2004.14448 `[M]`: FT-drift anatomy, NLP.

**Exact difference.** Existing work measures drift or fixes the interface; none validates drift as a **predictive
early-warning signal** (lead time k before zero-shot/prompt-behavior regression, actionable stopping rule) in a
promptable model. That predictive claim is also C1-073's template — the C1 audit flagged this as a template-echo (F7),
so only one predictive-drift paper may exist in the portfolio.

**Overlap:** SLIVER, actively shrinking (CA-SAM). Confidence: medium. **R2 attack paper:** CA-SAM + Davari.

**Verdict:** **MUTATE**: merge A1-108 + C1-067 (+C1-073's regression design) into one *prediction* paper: drift statistic
chosen a priori, lead-time and decision-value (early-stop vs loss-based) as the deliverables. "Drift exists/correlates"
is dead on arrival.

---

## 13. VLM prior harms rare/atypical + negation — S-228, S-240, B1-107

**Closest real papers**
- Alhamoud et al., *Vision-Language Models Do Not Understand Negation* (NegBench), CVPR 2025, arXiv:2501.09425 `[V]`:
  18 task variants, 79k examples, **including medical (CONCH, BioMedCLIP)**; VLMs at chance on negation; synthetic-data fix.
- *CXR-Align* benchmark, PhysioNet 2025 `[V]`: negation handling in chest X-ray report alignment — "no pneumothorax" is
  literally the worked example of the field.
- NAST, arXiv:2602.12498 `[V]`: layer-specific fine-tuning for **medical VLM negation** — the fix literature has started.
- Yuksekgonul et al., bags-of-words/NegCLIP, ICLR 2023, arXiv:2210.01936 `[M]`.
- Udandarao et al., *No "Zero-Shot" Without Exponential Data*, NeurIPS 2024, arXiv:2404.04125 `[M]`: zero-shot
  performance tracks pretraining **concept frequency** — the "text prior fails on rare/atypical" engine (C1-002 was
  already killed on this basis in our own audit).
- Li et al., POPE, EMNLP 2023, arXiv:2305.10355 `[M]`; Rohrbach et al., CHAIR, EMNLP 2018, arXiv:1809.02156 `[M]`:
  object hallucination driven by **co-occurrence priors**, measured via co-occurrence-based negative sampling — B1-107's
  thesis for VQA/captioning.

**Exact differences.**
- S-240 (negation breaks VLM-driven segmentation): the recognition/retrieval/alignment version is comprehensively
  published, medical included. Remaining sliver — pixel-level referring segmentation under negation — is one evaluation
  slice, not a paper. **KILL** (fold as an eval slice into S-228's successor if wanted).
- S-228 (text prior suppresses atypical presentations): frequency→zero-shot is published (Udandarao); *dense recall harm
  on atypical presentations, with the text prior causally ablated* (vision-only vs VLM-prompted segmentation on
  frequency-stratified findings) is not. **MUTATE** into that causal, frequency-controlled design; must cite
  NegBench-med/CXR-Align/Udandarao. High clinical stakes keep it alive.
- B1-107 (inpaint the object out, VLM segmenter still fires — phantom masks): POPE/CHAIR established co-occurrence
  hallucination for text outputs; **no dense-prediction counterfactual-inpainting audit found**. The confound (inpainting
  traces) is real and was flagged by our own AB reviewer; require trace-controls (re-inpaint present objects as sham
  surgery). **SURVIVE**.

**Overlap:** REAL (negation, frequency), SLIVER (dense counterfactual). Confidence: high on the kills, medium on
B1-107's survival (dense-hallucination benchmarks are appearing fast). **R2 attack papers:** NegBench; Udandarao; POPE.

---

## 14. AL / semi-sup dead under VFM init — B1-011 (entropy AL ≈ random under DINOv2), B1-025 (ST ≈ Mean Teacher under VFM init)

**Closest real papers**
- Gupte et al., *Revisiting Active Learning in the Era of Vision Foundation Models*, TMLR 2024, arXiv:2401.14555 `[V]`:
  systematically re-evaluates AL **with DINOv2/OpenCLIP**, overturns low-budget lore (cold-start selection,
  uncertainty-vs-typicality), proposes the corrected strategy. B1-011's question, asked and answered (classification).
- Mittal et al., *Realistic Evaluation of Deep Active Learning for Image Classification and Semantic Segmentation*,
  IJCV 2025 `[V]`: **segmentation included**; shows regimes where random(+SSL) beats AL and maps when AL pays — the
  dense-prediction version of the audit exists.
- Yang et al., *UniMatch V2*, TPAMI 2025, arXiv:2410.10777 `[V]`: rebuilds semi-supervised segmentation **on DINOv2**;
  headline findings: "a simple update on the encoder brings more improvement than careful method designs" and
  "labeled-only DINOv2-S beats semi-supervised ResNet-101" — i.e., VFM init compresses the method-design deltas that
  B1-025 wanted to test. SemiVL (ECCV 2024) `[V via citation]` covers the VLM-guided variant.
- Cold-start: *Foundation Model Makes Clustering a Better Initialization for Cold-Start AL*, arXiv:2402.02561 `[V]`.

**Exact difference that remains.** B1-025's literal pair (plain ST vs Mean Teacher, frozen-VFM, gap <0.5) is a two-row
ablation inside UniMatch V2's already-published re-benchmark; B1-011's seg-specific AL loop is a cell in Mittal et al.'s
grid. Neither difference clears the "would the IJCV/TPAMI authors consider this news?" bar (banned pattern F1).

**Overlap:** REAL. Confidence: high. **R2 attack papers:** UniMatch V2 arXiv:2410.10777; Gupte et al. arXiv:2401.14555.

**Verdict:** **KILL both.** Redirect annotation-efficiency weight to B1-028 (off-domain unlabeled contamination) and
B1-001-style budget-unit questions, which the above papers do not touch.

---

## 15. Copy-paste ≥ diffusion synthesis at matched compute — B1-051

**Closest real papers**
- Ghiasi et al., *Simple Copy-Paste is a Strong Data Augmentation Method for Instance Segmentation*, CVPR 2021,
  arXiv:2012.07177 `[M]`: copy-paste is a strong baseline.
- Zhao et al., *X-Paste*, ICML 2023, arXiv:2212.03863 `[V]`: StableDiffusion-generated + CLIP-filtered instances
  **beat plain Copy-Paste** on LVIS (+1.2 box/mask AP overall, more on rare) — the direct adversary, claiming the
  opposite direction.
- He et al., *Is Synthetic Data from Generative Models Ready for Image Recognition?*, ICLR 2023, arXiv:2210.07574 `[M]`.

**Exact difference.** X-Paste's comparison is **not compute-matched**: diffusion generation, CLIP filtering, and mask
post-processing GPU-hours are excluded from the accounting. Nobody has published the honest
equal-GPU-hours (generation included) frontier for instance segmentation. B1-051 has a named adversary whose headline
number it can flip — exactly the "who is wrong if we are right" shape the rubric rewards.

**Overlap:** SLIVER. Confidence: medium-high (a compute-accounting paper may exist in the synthetic-data-scaling
literature; none surfaced). **R2 attack paper:** X-Paste arXiv:2212.03863 (reviewers will cite its gains; the answer is
the compute ledger).

**Verdict:** **SURVIVE.** Obligations: charge generation+filtering to the synth arm; scale-matched real-data arm
(Ghiasi) as the third condition; report the crossover scale where diffusion wins (the honest possible outcome).

---

## 16. Histogram matching explains UDA — B1-061 ("style matching recovers ≥60% of self-training UDA gain")

**Closest real papers**
- Yang & Soatto, *FDA: Fourier Domain Adaptation for Semantic Segmentation*, CVPR 2020, arXiv:2004.05498 `[V]`:
  a **training-free low-frequency amplitude swap** achieved then-SOTA UDA on GTA→Cityscapes — the "cheap spectral/style
  alignment captures most of the gap" result, six years old; now shipped as a default augmentation in Albumentations
  alongside HistogramMatching.
- Hoyer et al., DAFormer, CVPR 2022, arXiv:2111.14887 `[M]`: modern self-training pipeline with ablations; the target of the decomposition.
- Feather-light FDA for MRI, arXiv:2208.00474 `[V]`: the cheap-style-transfer-suffices point replicated in medical.

**Exact difference.** B1-061 is an *attribution audit against 2024-era pipelines* (what fraction of DAFormer/MIC-class
gains is style?), not a method. But FDA already made "cheap style ≈ most of UDA" the community's prior, and B1-069
(additivity factorial, kept elsewhere) tests the same decomposition more sharply.

**Overlap:** REAL in spirit; SLIVER for modern-pipeline attribution. Confidence: high. **R2 attack paper:** FDA arXiv:2004.05498.

**Verdict:** **MUTATE**: fold into B1-069's ±style × ±self-training factorial. As a standalone claim it reads as FDA
redux with a percentage attached.

---

## 17. FSS support variance / background cheat — B1-074 (support choice > method choice), B1-079 (background-similarity shortcut)

**Closest real papers**
- Tang et al., *Overcoming Support Dilution for Robust Few-shot Semantic Segmentation*, arXiv:2501.13529 `[V]`:
  documents that support-image **contribution varies drastically** (more shots can hurt; contribution-ranked pruning
  fixes it) — a method built on B1-074's phenomenon, without the audit framing.
- *A Novel Benchmark for Few-Shot Semantic Segmentation in the Era of Foundation Models*, arXiv:2401.11311 `[V]`:
  re-benchmarks FSS with modern VFMs; foundation-feature baselines reorder the field — method-variance is already known to shrink.
- Lang et al., *Learning What Not to Segment* (BAM), CVPR 2022, arXiv:2203.07615 `[V]`: **base-class bias** — FSS models
  systematically fire on seen-class regions; the canonical published FSS-shortcut result.
- Episode-variance in few-shot classification (confidence-interval literature, e.g. Dhillon et al. ICLR 2020 `[M]`).

**Exact differences.**
- B1-074: the *variance decomposition* (support-draw variance vs method variance, same episodes, released checkpoints)
  is not published; 2501.13529 optimizes selection but never reports the decomposition that would indict FSS
  leaderboards. SLIVER → **MUTATE**: run as an eval-only ANOVA (mirror of C1-038's clicks×checkpoints design), citing
  2501.13529 as evidence-in-favor and 2401.11311 as the checkpoint pool.
- B1-079: BAM shows a *class-prior* shortcut; B1-079 alleges an orthogonal **episode-construction** shortcut
  (support/query background similarity). No background-swap audit found. **SURVIVE**, with obligations: control
  compositing artifacts (sham-swap with same-background composites), and difference explicitly vs BAM's bias.

**Overlap:** SLIVER both. Confidence: medium. **R2 attack papers:** 2501.13529 (B1-074); BAM (B1-079).

---

## 18. CLIP dense linear realignment — B1-097 ("linear map from ~100 labels recovers ≥70% of dense-CLIP gap")

**Closest real papers**
- Zhou et al., MaskCLIP(+), ECCV 2022, arXiv:2112.01071 `[M]`: attention surgery exposes dense CLIP features; the founding fix.
- Wang et al., SCLIP, arXiv:2312.01597 `[V]`: **training-free** attention correction, 14.1→38.2 average zero-shot mIoU.
- Wysoczańska et al., CLIP-DINOiser, ECCV 2024, arXiv:2312.12359 `[V]`: **two light conv layers, zero annotations**,
  learned from CLIP itself, SOTA on COCO/Context/Cityscapes/ADE — strictly dominates "linear head + 100 labels" on both
  cost and supervision axes.
- Plus GEM, NACLIP, ClearCLIP, ProxyCLIP (training-free family, 2023-24) `[M]`; LSeg arXiv:2201.03546 `[M]` and
  PACL arXiv:2212.04994 `[M]` on the supervised-alignment side.

**What they did vs. what we claimed.** The practical problem ("cheaply realign CLIP's dense features") is solved
repeatedly, including with *less* supervision than B1-097 proposes. The residual scientific claim ("the misalignment is
linearly correctable") is half-answered by the training-free family: much of it is an **attention-pooling artifact**, not
even a feature-space linear offset.

**Overlap:** REAL. Confidence: high. **R2 attack paper:** CLIP-DINOiser arXiv:2312.12359 + SCLIP.

**Verdict:** **KILL.** Salvageable residue → B1-098 (what attention surgery *cannot* fix: error taxonomy of the
post-surgery residual), which is not in this attack set and should absorb B1-097's Protect slot.

---

## Cross-cluster notes for the Stage-3 supervisor

1. **The 2024–26 SAM-continual wave (Gu 2404.09957, CA-SAM 2511.17201, EvoSAM 2503.06236) landed inside our densest
   thread.** Everything in clusters 1, 8, 9, 10 that reads "nobody measured adaptation-vs-retention for SAM" is now
   false as stated. The survivors are the *behavioral/prompt-resolved* and *audit-the-auditors* angles (clusters 3, 4, 5).
2. **Recommended consolidated papers out of this set** (respecting the ≥30% constructive quota):
   P1 = C1-065 battery + S-176 matrix + random-LoRA/VeRA control + LR-sweep control (clusters 1+2+3+8+9).
   P2 = S-183 noise-floor audit gating P1 (cluster 5).
   P3 = C1-031 IoU-head desync + calibration/robustness frontier (cluster 6), reporting via C1-110's panel (cluster 10).
   P4 = A1-107 placement→error-type (cluster 11) — constructive/mechanism slot.
   P5 = B1-107 dense counterfactual hallucination + S-228 frequency-stratified prior harm (cluster 13).
   P6 = B1-051 compute-honest synthesis audit (cluster 15). P7 = B1-079 background-swap audit (cluster 17).
3. **Protect-list corrections requested:** revoke Protect from C1-053, C1-057 (killed with cause, scooped);
   transfer to C1-065 and C1-031. S-148's Protect is void (VeRA); its budget goes to A1-107.
4. **Unverified-memory citations** are tagged `[M]` throughout; before any of these clusters becomes a paper draft,
   re-verify `[M]` arXiv IDs. No citation above is fabricated; `[M]` items are canonical papers cited by title+venue.
