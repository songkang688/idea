# Adversarial Prior-Work Attack — Batch B (Agent E)

**Posture:** default assumption is *already published*. Every idea below had to earn survival
against live web literature search (no invented papers). 26 ideas attacked: the 15 mandated IDs
plus 11 that I ranked at or above them (0101, 0114, 0145, 0163, 0172, 0213, 0268, 0279, 0304, 0323, 0339).

**Citation policy:** URLs are given where the exact record was verified during this review.
A few closest-prior-works were located via live search but their exact arXiv IDs were not
re-verified before writing; those are cited by title/venue/year and flagged. No paper below is invented.

**Tally:**

| Verdict | Mandated 15 | Extras 11 | Total |
|---|---|---|---|
| SURVIVE | 0001, 0074, 0104, 0293, 0307, 0332 (6) | 0114, 0304, 0323, 0268 (4) | 10 |
| MUTATE | 0042, 0098, 0154, 0200, 0203, 0226, 0254 (7) | 0101, 0145, 0163, 0172, 0213, 0339 (6) | 13 |
| KILL | 0136, 0175 (2) | 0279 (1) | 3 |

---

## The 15 mandated IDs

### W2-B-0001 — DINOv2 register/high-norm artifacts predict per-pixel segmentation errors

- **Closest prior works:**
  - *Vision Transformers Need Registers* — Darcet, Oquab, Mairal, Bojanowski. ICLR 2024. https://arxiv.org/abs/2309.16588
  - *SINDER: Repairing the Singular Defects of DINOv2* — Wang, Zhang, Salzmann. ECCV 2024. https://arxiv.org/abs/2407.16826
  - *Denoising Vision Transformers* — Yang et al. ECCV 2024. https://arxiv.org/abs/2401.02957
- **What they did:** established that high-norm outlier tokens exist in DINOv2-class ViTs, that they hurt dense tasks, and that they can be removed (registers at pretraining, SINDER/DVT post-hoc repair).
- **Exact difference:** all three treat the artifact as a *defect to remove*. None quantifies the artifact-norm map as a *per-pixel error predictor* or free uncertainty channel (AUROC of norm vs segmentation error, comparison against softmax-entropy baselines).
- **Remaining novelty:** the reframing "artifact = free spatial uncertainty signal" plus its quantitative evaluation against standard uncertainty estimators.
- **Novelty confidence:** medium-high. The measurement is easy to run, so a scoop is plausible at any time; nothing found as of this search.
- **Reviewer #2 attack:** "Darcet et al. already characterized these tokens and follow-ups remove them; showing they correlate with errors is a two-figure appendix, not a paper."
- **Counter:** correlation-vs-error against calibrated baselines across models/tasks, plus the deployment story (uncertainty without extra forward passes), is a full empirical paper — and if the correlation is weak, that is a publishable negative about a plausible free lunch.
- **Verdict: SURVIVE** (reposition explicitly as uncertainty-quantification, cite all three works up front).

### W2-B-0042 — Synonym instability makes open-vocabulary segmentation rankings unreliable

- **Closest prior works:**
  - *Renovating Names in Open-Vocabulary Segmentation Benchmarks* — Huang et al. NeurIPS 2024 (located via search; URL not re-verified).
  - *Open-Vocabulary Segmentation with Semantic-Assisted Calibration* — Liu et al. CVPR 2024 (located via search; URL not re-verified).
  - Metric-reform work proposing "open mIoU"-style similarity-aware scoring for OVS evaluation (located via search; URL not re-verified).
- **What they did:** documented that class-name quality/choice materially changes OVS results, renovated benchmark names, and proposed name-robust metrics and calibration.
- **Exact difference:** prior work shows *names matter* and fixes names/metrics. 0042's specific quantity — variance of rankings across synonym sets *compared against* model-generation variance (is synonym noise bigger than the effect sizes papers claim?) — is not computed anywhere I found.
- **Remaining novelty:** the variance-decomposition framing (synonym variance vs method variance vs seed variance) as a claim about the field's inferential validity.
- **Novelty confidence:** medium. The ingredients are all published; the decomposition is the only fresh part.
- **Reviewer #2 attack:** "RENOVATE already showed benchmark names are broken and fixed them — your study is an ablation of their motivation section."
- **Verdict: MUTATE** — drop "synonyms cause instability" (known); the paper is the *variance ledger*: synonym-induced ranking variance vs published method deltas, with a conclusion about which published OVS conclusions survive name noise.

### W2-B-0074 — Modality-gap collapse during fine-tuning is a phase transition predicting zero-shot robustness loss

- **Closest prior works:**
  - *Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning* — Liang et al. NeurIPS 2022. https://arxiv.org/abs/2203.02053
  - Work arguing the modality gap relates to robustness ("bug or feature" robustness-perspective analysis, 2024–2025; located via search, URL not re-verified).
  - *Two Effects, One Trigger*-style analyses of gap origins (ICLR 2025 era; located via search, URL not re-verified).
- **What they did:** characterized the gap's existence, geometric origins, and static correlations with robustness/performance.
- **Exact difference:** all of it is *statics* (gap at convergence, gap at initialization). Nobody tracks gap trajectory *during downstream fine-tuning*, identifies an abrupt collapse, or uses collapse onset as an early-warning signal for zero-shot robustness loss.
- **Remaining novelty:** the dynamics + phase-transition claim + predictive use (stop before collapse).
- **Novelty confidence:** high on the dynamics angle; the gap literature is crowded but oriented differently.
- **Reviewer #2 attack:** "The gap is a well-studied epiphenomenon; correlation of its collapse with forgetting zero-shot behavior is expected, not surprising — WiSE-FT already tells us fine-tuning erodes zero-shot ability."
- **Counter:** WiSE-FT (Wortsman et al., CVPR 2022, https://arxiv.org/abs/2109.01903) shows the erosion, not a cheap online predictor of *when* it begins; an actionable early-stopping signal is the deliverable.
- **Verdict: SURVIVE** (must include a "gap-statics are known" related-work section and a non-gap baseline predictor).

### W2-B-0098 — LoRA dynamics are reproduced by full fine-tuning with rescaled learning rates

- **Closest prior works:**
  - *LoRA vs Full Fine-tuning: An Illusion of Equivalence* — Shuttleworth, Andreas et al. 2024. https://arxiv.org/abs/2410.21228
  - *LoRA Learns Less and Forgets Less* — Biderman et al. TMLR 2024. https://arxiv.org/abs/2405.09673
- **What they did:** Shuttleworth et al. show LoRA and full FT reach *structurally different* solutions ("intruder dimensions") even at matched task accuracy; Biderman et al. characterize LoRA's lower learning/lower forgetting profile.
- **Exact difference:** 0098 hypothesizes function-space equivalence under LR rescaling — Shuttleworth et al. is direct counter-evidence at the weight-spectrum level, and partially at the behavior level (different forgetting profiles).
- **Remaining novelty:** only the *boundary question*: under which (rank, LR, task) regimes does the equivalence approximately hold before intruder dimensions appear?
- **Novelty confidence:** low for the claim as stated; medium for the boundary version.
- **Reviewer #2 attack:** "Your hypothesis was tested and falsified in 2024; citation: Illusion of Equivalence."
- **Verdict: MUTATE** — invert into "when does the LoRA≈rescaled-full-FT approximation break?": measure equivalence as a function of rank/LR/dose, merge with 0095's displacement-budget control, and treat intruder-dimension emergence as the order parameter.

### W2-B-0104 — PEFT preserves pretrained invariances that dense tasks must break

- **Closest prior works:**
  - *LoRA Learns Less and Forgets Less* — Biderman et al. TMLR 2024. https://arxiv.org/abs/2405.09673
  - *LoRA vs Full Fine-tuning: An Illusion of Equivalence* — Shuttleworth et al. 2024. https://arxiv.org/abs/2410.21228
  - Dense-PEFT adapter papers observing dense-task weight updates are not low-rank (located via search, URL not re-verified).
- **What they did:** established LoRA's conservatism (learns/forgets less) and structural differences from full FT; adapter work implies dense tasks demand different update structure.
- **Exact difference:** none of these measures *invariance/equivariance* inheritance specifically, nor ties PEFT's dense-task failures to un-broken pretrained invariances (e.g., augmentation invariances that destroy precise localization).
- **Remaining novelty:** the mechanism (invariance inheritance) and the predictor (invariance-deficit of the frozen model predicts PEFT dense-gap).
- **Novelty confidence:** medium-high; adjacent literatures are hot but this specific mechanism is unclaimed.
- **Reviewer #2 attack:** "This is 'LoRA learns less' with extra steps — conservatism trivially implies preserved invariances."
- **Counter:** the claim is falsifiable and directional: it predicts *which* dense tasks PEFT fails (those needing invariance-breaking), not just *that* PEFT is conservative. A dissociation experiment (tasks matched in difficulty, differing in invariance-breaking demand) separates it from generic conservatism.
- **Verdict: SURVIVE** (positioning against both cited works is mandatory).

### W2-B-0136 — Catastrophic forgetting is feature rotation, not erasure

- **Closest prior works:**
  - *Probing Representation Forgetting in Supervised and Unsupervised Continual Learning* — Davari et al. CVPR 2022. https://arxiv.org/abs/2203.13381
  - *Anatomy of Catastrophic Forgetting: Hidden Representations and Task Semantics* — Ramasesh et al. ICLR 2021. https://arxiv.org/abs/2007.07400
  - Recent "accessibility collapse" characterizations of forgetting as readout-recoverable (located via search, URL not re-verified).
- **What they did:** showed with optimal linear probes that representations degrade far less than task accuracy suggests — forgetting is substantially a readout/alignment phenomenon concentrated in upper layers. This *is* the rotation-not-erasure claim.
- **Exact difference:** essentially none at the level 0136 states it.
- **Remaining novelty:** none for the headline claim.
- **Novelty confidence:** high confidence it is published.
- **Reviewer #2 attack:** "Davari et al., CVPR 2022. Next."
- **Verdict: KILL.** Salvageable mutation (recorded, not kept as a separate idea): whether *emergent dense abilities* of VFMs (segmentation-quality features that were never explicit training targets) are erased or merely rotated under adaptation — that question is folded into the 0163 audit-bias program.

### W2-B-0154 — Decoder/head capacity governs how much the backbone forgets

- **Closest prior works:**
  - *Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution* (LP-FT) — Kumar et al. ICLR 2022. https://arxiv.org/abs/2202.10054
  - *How to prepare your task head for finetuning* — Ren et al. ICLR 2023 (located via search; URL not re-verified).
- **What they did:** LP-FT shows head initialization state changes how much fine-tuning distorts the backbone; Ren et al. analyze how task-head properties modulate backbone feature change during fine-tuning.
- **Exact difference:** prior work manipulates head *initialization/training schedule*; 0154's dial is head *capacity* (decoder size/expressivity) with a monotone hypothesis for dense decoders. Ren et al. imply the relationship may be non-monotone.
- **Remaining novelty:** a systematic capacity→backbone-forgetting curve for dense decoders (linear → DPT-scale) does not exist; the monotone version as stated is likely false.
- **Novelty confidence:** medium.
- **Reviewer #2 attack:** "LP-FT already established the head-backbone interaction; sweeping decoder size is an ablation of known mechanics."
- **Verdict: MUTATE** — hypothesis becomes *non-monotonicity*: there is an interior forgetting-maximizing head capacity, with mechanism (gradient magnitude vs gradient absorption). The curve, not the direction, is the contribution.

### W2-B-0175 — Interactive-segmentation rankings are simulation-policy artifacts

- **Closest prior works:**
  - *RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation* — Antonov et al. NeurIPS 2024. https://arxiv.org/abs/2410.11722
  - *TETRIS* click/interaction benchmark work referenced therein.
- **What they did:** collected 475K real user clicks, built a clickability model, and showed baseline click-simulation strategies overestimate performance (5–29% annotation-time underestimation) and that method robustness rankings change under realistic clicks — including across clicking-pattern groups.
- **Exact difference:** none material. RClicks is 0175, executed with more resources than a PhD-year replication would have.
- **Remaining novelty:** none.
- **Novelty confidence:** high confidence published.
- **Reviewer #2 attack:** "This is RClicks. It won a NeurIPS D&B slot doing exactly this."
- **Verdict: KILL.**

### W2-B-0200 — Linear probing underestimates dense information and misranks VFMs

- **Closest prior works:**
  - *Attention, Please! Revisiting Attentive Probing Through the Lens of Efficiency* — Psomas et al. ICLR 2026. https://arxiv.org/abs/2506.10178
  - *How to Benchmark Vision Foundation Models for Semantic Segmentation?* — Kerssies et al. CVPR 2024 Workshops. https://arxiv.org/abs/2404.12172
  - Dense attentive-probing evaluation work (located via search; URL not re-verified).
- **What they did:** Psomas et al. show linear probing understates models with local-representation pretraining and that attentive probes change conclusions; Kerssies et al. explicitly recommend *against* linear probing for VFM segmentation benchmarking because it is unrepresentative and alters rankings.
- **Exact difference:** the qualitative claim (LP misranks; better probes change rankings) is published. What is not: a quantitative decomposition of *how much* dense information LP leaves on the table per model family, and which published *scientific conclusions* (not just leaderboard orders) flip.
- **Remaining novelty:** the conclusion-flipping audit; the probe-capacity sweep as measurement theory.
- **Novelty confidence:** low-medium for the claim as stated.
- **Reviewer #2 attack:** "Kerssies et al. told the community to stop using linear probes in 2024, and attentive probing is now standard; you are relitigating settled protocol."
- **Verdict: MUTATE** — merge with 0213 into a single *protocol-confound audit*: probe capacity × input resolution as joint confounds, with the deliverable being a list of specific published VFM-comparison claims that invert under corrected protocol.

### W2-B-0203 — Bilinear upsampling is the binding constraint in frozen-VFM segmentation

- **Closest prior works:**
  - *FeatUp: A Model-Agnostic Framework for Features at Any Resolution* — Fu, Hamilton et al. ICLR 2024. https://arxiv.org/abs/2403.10516
  - LiFT and LoftUp-style learned feature-upsampler follow-ups (2024–2025; located via search, URLs not re-verified).
- **What they did:** built learned feature upsamplers and showed large dense-task gains over bilinear upsampling for frozen features — establishing that upsampling is *a* major constraint.
- **Exact difference:** FeatUp demonstrates gains but does not decompose the frozen-vs-finetuned gap into "resolution/upsampling" vs "feature content" terms, nor establish where the ceiling is once upsampling is saturated.
- **Remaining novelty:** the *accounting*: what fraction of the frozen-VFM dense gap is upsampling-attributable per model/task, and what residual remains after FeatUp-class methods.
- **Novelty confidence:** low for "upsampling matters" (published); medium for the decomposition.
- **Reviewer #2 attack:** "FeatUp's ablations already imply your answer; this is a re-run of their Table 3 with more models."
- **Verdict: MUTATE** — from "upsampling is the constraint" (known) to "the post-upsampler residual decomposition": quantify the remaining gap, attribute it (semantic content vs localization vs calibration), and identify when frozen+upsampler matches fine-tuning.

### W2-B-0226 — Frozen features degrade gracefully under shift, tuned features sharply: a measurable "shift budget"

- **Closest prior works:**
  - *Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution* — Kumar et al. ICLR 2022. https://arxiv.org/abs/2202.10054
  - *Robust fine-tuning of zero-shot models* (WiSE-FT) — Wortsman et al. CVPR 2022. https://arxiv.org/abs/2109.01903
  - *The Evolution of Out-of-Distribution Robustness Throughout Fine-Tuning* — Andreassen et al. 2021. https://arxiv.org/abs/2106.15831
- **What they did:** established the direction: fine-tuning trades OOD robustness for ID accuracy; frozen/interpolated models are more robust; robustness erodes along fine-tuning trajectories.
- **Exact difference:** the literature gives the sign of the effect, mostly for classification. It does not provide *per-model, per-task budget curves* — accuracy as a function of continuous shift magnitude, frozen vs tuned, for dense prediction — usable as a deployment decision rule ("tune if expected shift < s*").
- **Remaining novelty:** the quantitative crossover-point estimation on dense tasks with controlled continuous shift dials.
- **Novelty confidence:** medium; the framing is fresh, the direction is textbook.
- **Reviewer #2 attack:** "LP-FT + WiSE-FT already taught practitioners this tradeoff; a budget curve is an engineering nomogram, not science."
- **Verdict: MUTATE** — keep, but the claim must be the *functional form and its stability* (do crossover points transfer across shift families?), which is a falsifiable scientific question, not a nomogram.

### W2-B-0254 — Synthetic training data buys accuracy but sells calibration

- **Closest prior works:**
  - *AUGCAL: Improving Sim2Real Adaptation by Uncertainty Calibration on Augmented Synthetic Images* — Prabhu et al. ICLR 2024. https://arxiv.org/abs/2312.06106
  - Sim2real miscalibration analyses cited therein (Sim2Real UDA calibration literature, 2022–2024).
- **What they did:** documented that sim-trained/adapted models are miscalibrated and overconfident on real data, and patched it — for *simulator* (graphics) data in UDA pipelines.
- **Exact difference:** the claim is established for simulator data. For *diffusion-generated* training data (the 2024–2026 regime), the accuracy-calibration tradeoff, its mechanism (mode coverage vs likelihood-tail truncation), and stratification by generation likelihood are not characterized.
- **Remaining novelty:** generator-era version with mechanism; likelihood-stratified calibration analysis.
- **Novelty confidence:** medium.
- **Reviewer #2 attack:** "AUGCAL already named and fixed this; swapping GTA5 for Stable Diffusion is a dataset swap."
- **Counter:** diffusion data's failure modes (mode collapse, prompt-conditioned coverage) are structurally different from renderer domain gap; whether the calibration tax persists, worsens, or inverts is genuinely open.
- **Verdict: MUTATE** — scope to generated (not simulated) data, make mechanism (coverage vs fidelity) the hypothesis, keep AUGCAL as the baseline patch to beat.

### W2-B-0293 — Matched-budget ablation: where does medical pretraining actually pay over natural VFMs?

- **Closest prior works:**
  - *Does DINOv3 Set a New Medical Vision Standard?* — 2025. https://arxiv.org/abs/2509.06467
  - *Towards General Purpose Vision Foundation Models for Medical Image Analysis: DINOv2 on Radiology Benchmarks* — Baharoon et al. 2023. https://arxiv.org/abs/2312.02366
  - *Feature Quality and Adaptability of Medical Foundation Models* — 2025. https://arxiv.org/abs/2511.09742
  - UNI / CONCH pathology-FM evaluations (Chen et al.; Lu et al., Nature Medicine 2024).
- **What they did:** benchmarked natural VFMs vs medical FMs across modalities and tasks; found natural VFMs often competitive, medical FMs ahead in linear probing on some radiographic tasks, both poor on subtle localization.
- **Exact difference:** every comparison is between *unmatched* models (different data scale, compute, architecture, recipe). No study isolates the medical-pretraining term at matched budget, so "medical pretraining pays here" remains confounded with "this lab trained longer."
- **Remaining novelty:** the controlled attribution — matched-compute, matched-architecture pretraining pairs (medical vs natural vs mixed corpus), localizing *which capability axis* (global label, salient anatomy, subtle lesion, site invariance) the medical term buys.
- **Novelty confidence:** medium-high for the causal version; the observational version is saturated.
- **Reviewer #2 attack:** "We have a dozen benchmarks already saying natural VFMs are strong baselines — see the DINOv3 medical report — your grid adds decimal places."
- **Counter:** those benchmarks *cannot* answer the attribution question because their model pairs are unmatched; that is precisely the gap. But the pretraining runs make this the most expensive survivor — flagged as needing a compute partner.
- **Verdict: SURVIVE** (as the causal matched-budget design only; any observational variant is dead on arrival).

### W2-B-0307 — Language alignment degrades metric depth/3D structure (causal, matched-data)

- **Closest prior works:**
  - *Probing the 3D Awareness of Visual Foundation Models* — El Banani et al. CVPR 2024. https://arxiv.org/abs/2404.08636
- **What they did:** probed frozen VFMs for depth/surface-normal/correspondence quality; found language-aligned models (CLIP-lineage) weaker on 3D properties than SSL models — *observationally*, across unmatched pretrained checkpoints.
- **Exact difference:** existing evidence is correlational over incomparable models. 0307 runs matched-data, matched-architecture pretraining with/without language alignment (and alignment-strength dials) to isolate the causal term, plus mechanism (which depth cues are lost).
- **Remaining novelty:** the causal isolation and dose-response; nobody has done the controlled contrast.
- **Novelty confidence:** medium-high (main risk is a concurrent controlled study; none found).
- **Reviewer #2 attack:** "El Banani et al. already showed CLIP is bad at 3D; your controlled rerun confirms what everyone believes — low information gain."
- **Counter:** "everyone believes it" is exactly why a clean causal test matters; if alignment does *not* cause the deficit at matched data (it's a data-distribution artifact), that overturns a community default — high information either way.
- **Verdict: SURVIVE.**

### W2-B-0332 — Visual chain-of-thought is post-hoc theater (artifact-swap causal test)

- **Closest prior works:**
  - *Measuring Faithfulness in Chain-of-Thought Reasoning* — Lanham et al. 2023. https://arxiv.org/abs/2307.13702
  - VLM-specific CoT-faithfulness evaluations and verification pipelines, e.g. CoRGI-style grounded-verification work and 2025–2026 VLM CoT-faithfulness benchmarks (located via search; URLs not re-verified).
- **What they did:** Lanham et al. established CoT-faithfulness tests (truncation, corruption) for LLMs; recent VLM work benchmarks whether stated visual reasoning steps are consistent with answers, and builds verifiers that check step-image consistency.
- **Exact difference:** existing VLM faithfulness tests mostly perturb *text* reasoning or measure consistency. 0332's intervention manipulates the *visual evidence* cited by the chain (swap/remove the specific referenced region) and asks whether the answer changes — a causal test of whether cited visual evidence is load-bearing.
- **Remaining novelty:** the visual-evidence intervention protocol and a decomposition of theater-vs-use across model families and task types.
- **Novelty confidence:** medium — this space is the fastest-moving of all attacked ideas; scoop risk is the highest among survivors.
- **Reviewer #2 attack:** "CoT unfaithfulness is established in LLMs and already being cataloged for VLMs; another benchmark of it is incremental."
- **Counter:** the deliverable is not a benchmark but an intervention result: the fraction of visual-CoT steps that are causally load-bearing, which no text-side perturbation can measure.
- **Verdict: SURVIVE** (with an explicit freshness check immediately before execution, given field velocity).

---

## Extras — ideas I ranked at or above the mandated set

### W2-B-0101 — Dense tasks have higher intrinsic update rank; LoRA accuracy tracks captured spectral mass

- **Closest prior works:** LoRA (Hu et al. 2021, https://arxiv.org/abs/2106.09685); *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning* (Aghajanyan et al. 2020, https://arxiv.org/abs/2012.13255); dense-PEFT adapter work reporting dense-task weight deltas are not low-rank (located via search; URL not re-verified).
- **What they did:** established low intrinsic dimension for classification-style fine-tuning; adapter papers observe dense tasks resist low-rank updates.
- **Exact difference:** the observation "dense needs more rank" is partially published; the *task-indexed required-rank law* (accuracy gap regressed on captured spectral mass of full-FT deltas, validated cross-task) is not.
- **Remaining novelty:** the quantitative law and its predictive use (choose rank from a cheap spectral probe).
- **Novelty confidence:** medium.
- **Reviewer #2 attack:** "Adapter papers already told practitioners to raise rank for dense tasks; your law reformats their ablation tables."
- **Verdict: MUTATE** — the law (functional form + cross-task transfer of the spectral-mass→accuracy mapping) is the paper; the binary claim is dead.

### W2-B-0114 — VPT prompt tokens function as trainable register tokens

- **Closest prior works:** *Visual Prompt Tuning* (Jia et al. ECCV 2022, https://arxiv.org/abs/2203.12119); *Vision Transformers Need Registers* (Darcet et al. ICLR 2024, https://arxiv.org/abs/2309.16588).
- **What they did:** VPT established prompt-token adaptation; Darcet et al. established that extra non-semantic tokens absorb global aggregation and remove artifacts.
- **Exact difference:** the two literatures have not been connected. No work tests whether VPT gains are partially reproduced by *frozen random* tokens (pure register effect, no learning), or whether learned VPT tokens develop register signatures (high norm, artifact absorption), especially on register-free backbones.
- **Remaining novelty:** the identification claim and its decomposition (absorptive vs learned contribution).
- **Novelty confidence:** high — this is the cleanest unclaimed connection found in the whole batch; also the cheapest to falsify.
- **Reviewer #2 attack:** "Registers are about pretraining artifacts, VPT is about adaptation; the analogy is cosmetic."
- **Counter:** the frozen-random-token control converts the analogy into a measurable effect size; if it reproduces a nontrivial fraction of VPT's gain, the finding rewrites how VPT baselines must be run.
- **Verdict: SURVIVE.**

### W2-B-0145 — Calibration forgets before accuracy during adaptation

- **Closest prior works:** *Continual Calibration: Coverage Can Collapse Before Accuracy in Lifelong LLM Fine-Tuning* (2026, https://arxiv.org/abs/2604.23987); *Calibration of Continual Learning Models* (2024, https://arxiv.org/abs/2404.07817); *TOOD: Task-Aware OOD Score Calibration for Continual Learners* (2026, https://arxiv.org/abs/2607.29592).
- **What they did:** demonstrated, for LLM lifelong fine-tuning and CL classification, that calibration/coverage degrades faster than accuracy — the exact temporal-ordering headline of 0145.
- **Exact difference:** the ordering is unpublished only for *dense vision* (per-pixel/per-region calibration) under *single-task VFM adaptation* (not task-sequence CL).
- **Remaining novelty:** dense spatial version: where in the image calibration decays first, and whether region-level calibration decay predicts subsequent accuracy forgetting.
- **Novelty confidence:** low-medium; the conceptual point is taken.
- **Reviewer #2 attack:** "Coverage-collapses-before-accuracy is already shown; porting to segmentation is a domain swap."
- **Verdict: MUTATE** — survives only as the spatial/dense version with the region-level early-warning claim; demoted from my top tier.

### W2-B-0163 — ID retention probes underestimate forgetting; OOD probes reveal hidden damage

- **Closest prior works:** LP-FT (Kumar et al. ICLR 2022, https://arxiv.org/abs/2202.10054); *The Hidden Costs on Distributional Shifts when Fine-tuning Joint Text-Image Encoders* (ECCV 2022 AROW workshop, https://eccv22-arow.github.io/short_paper/0028.pdf); *Model Reprogramming Outperforms Fine-tuning on OOD Data in Text-Image Encoders* (2024, https://arxiv.org/abs/2403.10800).
- **What they did:** established that fine-tuning damages OOD generalization and OOD detection while ID metrics look healthy — for the *downstream* task.
- **Exact difference:** 0163 is about *old-task retention audits*: paired ID/OOD probes of previously-held capabilities, and the claim that the audit gap widens with adaptation dose. Related mechanism, different measurement object — but the surprise value is reduced by the prior work.
- **Remaining novelty:** forgetting-audit bias quantification with dose-response, pretrained-normalized to separate shift difficulty from damage.
- **Novelty confidence:** medium-low.
- **Reviewer #2 attack:** "LP-FT-era work already implies ID metrics mask feature distortion; your 'audit bias' is that observation renamed."
- **Verdict: MUTATE** — survives narrowly as the audit-methodology paper (how wrong are current forgetting numbers, as a function of dose/method), explicitly not as a robustness rediscovery.

### W2-B-0172 — Dictionary definitions in prompts collapse dense performance while classification survives

- **Closest prior works:** *ITACLIP* (Aydin et al., CVPR 2025 Workshops, https://arxiv.org/abs/2411.12044); *LMSeg* (2024, https://arxiv.org/abs/2412.00364); CLIP-ES prompt-sharpness analysis (Lin et al., https://arxiv.org/abs/2212.09506).
- **What they did:** ITACLIP *adds* LLM-generated definitions/synonyms and improves training-free OVSS (choosing synonyms vs definitions per dataset by performance — implying definitions sometimes lose); CLIP-ES shows prompt wording strongly modulates dense (CAM) quality with a sharpness heuristic.
- **Exact difference:** prior work treats auxiliary text as an engineering knob and reports net gains; 0172 claims a *systematic dissociation* (dense hurt, classification unhurt) with a mechanism (name-token anchoring dilution). The dissociation as stated is now contested by ITACLIP's positive results.
- **Remaining novelty:** the controlled response-curve study — auxiliary-text length/type vs dense-vs-classification performance, with attention-to-name-token diagnostics — explaining *both* ITACLIP's gains and any collapse regimes.
- **Novelty confidence:** medium-low for the original claim; medium for the reconciliation study.
- **Reviewer #2 attack:** "ITACLIP improves segmentation using definitions; your central prediction is already empirically contradicted."
- **Verdict: MUTATE** — from "definitions hurt dense" to "when and why auxiliary text helps vs hurts dense but not classification"; demoted from my top tier.

### W2-B-0213 — Input-resolution confound overturns published VFM dense rankings

- **Closest prior works:** *How to Benchmark Vision Foundation Models for Semantic Segmentation?* (Kerssies et al., CVPR 2024 Workshops, https://arxiv.org/abs/2404.12172); Res-Bench resolution-robustness benchmarking for MLLMs (2025, https://arxiv.org/abs/2510.16926).
- **What they did:** Kerssies et al. show VFM segmentation rankings shift across benchmark settings (probe type, datasets, domain shift) and issue protocol recommendations; Res-Bench shows MLLM accuracy is resolution-unstable.
- **Exact difference:** Kerssies et al. sweep several settings but do not isolate *train/eval resolution* as the confound, nor normalize per-model native resolution, nor quantify how many published cross-paper conclusions invert under resolution matching.
- **Remaining novelty:** the resolution-specific audit with per-model native-resolution normalization and a conclusion-inversion count.
- **Novelty confidence:** medium.
- **Reviewer #2 attack:** "Benchmark-sensitivity for VFM segmentation is documented; you are adding one more axis to Kerssies et al.'s Figure 1."
- **Counter:** resolution is not one-more-axis — it is the axis conflated with model identity (models ship with different native resolutions), which makes it a *confound*, not a setting; that distinction is the paper.
- **Verdict: MUTATE** (kept, protected DP; must be framed as an extension-and-correction of Kerssies et al.).

### W2-B-0268 — Synthetic-image contamination of web-collected benchmarks distorts adaptation rankings

- **Closest prior works:** *Will Large-scale Generative Models Corrupt Future Datasets?* (Hataya et al., ICCV 2023, https://arxiv.org/abs/2211.08095); SelfClean-style dataset-cleaning work (located via search; URL not re-verified).
- **What they did:** Hataya et al. showed that injecting generated images into training sets degrades downstream models — a simulation of future contamination; cleaning work detects near-duplicates/label errors.
- **Exact difference:** 0268 measures *actual* contamination rates in benchmarks by collection date and — the fresh part — the induced *method-ranking distortion* on contaminated vs clean subsets (an eval-integrity, not train-integrity, claim).
- **Remaining novelty:** contamination-vs-date measurement in real benchmark suites plus ranking-distortion quantification.
- **Novelty confidence:** medium-high, with urgency (the window to measure "clean" pre-2022 baselines is closing).
- **Reviewer #2 attack:** "Detector unreliability makes your contamination estimates unfalsifiable; Hataya already covered the harm."
- **Counter:** detector-ensemble + manual verification subsample bounds estimator error; Hataya et al. simulated *training* harm, not measured *evaluation* distortion.
- **Verdict: SURVIVE.**

### W2-B-0279 — Modality-resolved sufficiency map for natural VFMs in medicine

- **Closest prior works:** *Does DINOv3 Set a New Medical Vision Standard?* (2025, https://arxiv.org/abs/2509.06467); *DINOv2 on Radiology Benchmarks* (2023, https://arxiv.org/abs/2312.02366); *Feature Quality and Adaptability of Medical Foundation Models* (2025, https://arxiv.org/abs/2511.09742); frozen-feature CT/CXR benchmarks (2026, https://arxiv.org/abs/2608.05960, https://arxiv.org/abs/2606.11606).
- **What they did:** collectively, benchmarked natural VFMs across medical modalities and tasks, identified where they suffice (many 2D tasks) and fail (WSI, EM, PET, subtle lesions) — i.e., produced the sufficiency map.
- **Exact difference:** none sufficient to sustain a separate idea; the observational map exists across these papers.
- **Remaining novelty:** only the causal matched-budget attribution — which is idea 0293.
- **Novelty confidence:** high confidence published.
- **Reviewer #2 attack:** "The DINOv3 medical report is your paper, with more modalities than you proposed."
- **Verdict: KILL** (fold residual value into 0293).

### W2-B-0304 — Language quantizes continuous shape space (morph-trajectory discontinuities)

- **Closest prior works:** categorical-perception studies of deep networks (color/phoneme domains) and VLM concept-geometry probing; El Banani et al. 3D-awareness probing (https://arxiv.org/abs/2404.08636) as the nearest geometry-probing anchor. No work found tracing feature trajectories along controlled *shape morphs* and testing for discontinuities aligned with naming boundaries.
- **What they did:** adjacent literatures establish categorical effects in color perception in deep nets and geometric deficits of language-aligned features — neither tests trajectory smoothness along object-morph continua.
- **Exact difference:** the morph-trajectory discontinuity measurement, the SSL-vs-CLIP contrast, and alignment with human naming boundaries are all unclaimed.
- **Remaining novelty:** high — cleanest genuinely-new measurement design among the extras.
- **Novelty confidence:** medium-high (adjacent fields are active; the specific paradigm appears unoccupied).
- **Reviewer #2 attack:** "Morph artifacts, not language, will produce your discontinuities; renderer choice is doing the work."
- **Counter:** multiple independent morphing pipelines (3D render, latent-space, image-space) with SSL models as the artifact control — discontinuities appearing only in language-aligned models across all pipelines cannot be a morph artifact.
- **Verdict: SURVIVE.**

### W2-B-0323 — Mention bias: unmentioned-but-visible content is under-represented in language-aligned features

- **Closest prior works:** *Seeing through the Human Reporting Bias* (Misra et al., CVPR 2016, https://arxiv.org/abs/1512.06974); recent analyses of reporting/pragmatics bias in caption corpora and its persistence at scale (2024–2025; located via search, URL not re-verified).
- **What they did:** established that captions systematically under-mention visible content (reporting bias) and that caption-trained models inherit label noise from it — at the *image-label* level.
- **Exact difference:** no work measures the *feature-level* imprint: frozen-representation decodability gaps for chronically-unmentioned categories, SSL-normalized (to control visual difficulty), correlated with corpus mention probability, verified by caption-intervention retraining.
- **Remaining novelty:** the decodability version + the mention-probability dose-response + small-scale causal retraining.
- **Novelty confidence:** medium-high.
- **Reviewer #2 attack:** "Reporting bias is a 2016 finding; of course supervision weighting shapes features — unfalsifiable folk wisdom dressed as a study."
- **Counter:** the SSL-normalized decodability gap is precisely the falsifiable version of the folk wisdom, and the caption-intervention retraining makes it causal, not correlational.
- **Verdict: SURVIVE.**

### W2-B-0339 — Agentic loops vs bigger encoders at matched compute: task-structured crossover

- **Closest prior works:** *Visual Reasoning Agent (VRA)* (2025, https://arxiv.org/abs/2509.16343); *On Test-Time Scaling for Vision-Language Models* (2026, https://arxiv.org/abs/2606.28864); CVPR 2026 workshop analysis of vision test-time-scaling limits (path redundancy; https://openaccess.thecvf.com/content/CVPR2026W/Viscale/papers/Yang_Understanding_the_Limits_of_Vision_Test-Time_Scaling_Path_Redundancy_Instance_CVPRW_2026_paper.pdf).
- **What they did:** demonstrated agentic/test-time-compute gains for vision tasks, showed small models + test-time compute can match large models, and analyzed when vision test-time scaling saturates.
- **Exact difference:** the generic "iteration vs scale" tradeoff is now actively being published. What is not: a *predictive theory of the crossover* — evidence-locality metrics that say in advance which tasks favor iteration vs scale at matched FLOPs.
- **Remaining novelty:** the locality-predictor and the task-structured crossover map; matched-FLOP accounting rigor.
- **Novelty confidence:** medium-low and decaying fast; this is the hottest contested space among the extras.
- **Reviewer #2 attack:** "Test-time-scaling papers already report when extra compute helps; your 'predictor' is post-hoc curve labeling."
- **Verdict: MUTATE** — the falsifiable object is the pre-registered locality predictor (compute the metric first, predict the crossover, then measure); without that pre-registration structure the idea is dead in a year.

---

## Cross-cutting observations from the attack

1. **Statics are published, dynamics are open.** Three survivors (0074, 0145-mutated, 0163-mutated) live because the literature measures endpoints while the ideas measure *trajectories*. This is a repeatable novelty heuristic for this field right now.
2. **Observational is published, causal is open.** 0293, 0307, 0323 survive specifically as matched/controlled versions of correlational findings that already exist.
3. **Benchmark-integrity ideas age fastest.** 0175 and 0279 were fully scooped; 0042, 0200, 0213 partially. Anything whose contribution is "the eval is broken" must check for a NeurIPS D&B paper doing exactly that.
4. **The 2024 LoRA-theory wave killed more than expected.** Shuttleworth et al. and Biderman et al. between them forced mutations on 0098 and 0101 and constrain 0104's framing.
