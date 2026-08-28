# Stage-4 Reviewer-2 Attacks — Batch B Survivors (Agent H)

**Posture:** each idea is treated as an already-submitted paper. I write the harshest defensible
rejection, list the hidden assumptions the authors did not state, then ask the only question that
matters: **is there a realistic, affordable experiment that silences this reviewer?** If yes, that
experiment is specified (Killer Experiment). If no, the idea is KILLED regardless of how pretty it is.

**Scope:** all 20 of Agent E's "PhD-year bets" plus 9 fragile protected keeps = **29 ideas attacked**.
Mandatory freshness re-search (live web, 2024–2026 arXiv) was run on the five flagged IDs
(0332, 0001, 0307, 0114, 0304) and extended to 0074, 0268, 0133, 0194/0169, 0164, 0264,
0042, 0323, 0286, 0263, 0305, 0317. All URLs below were returned by live search during this
review or inherited from Agent E's verified list; none are invented. Where I cite a paper from
memory without re-verifying the URL this session, it is flagged **[not re-verified]**.

**Verdict scale:** SURVIVE (attack fails on today's record) / SURVIVE-IF-EXPERIMENT (attack
succeeds unless the named experiment is run and wins) / MUTATE (headline claim is dead; a
narrower claim survives) / KILL (no affordable experiment silences the reviewer).

## Tally

| Verdict | Count | IDs |
|---|---|---|
| SURVIVE | 0 | — |
| SURVIVE-IF-EXPERIMENT | 14 | 0001, 0092, 0101, 0104, 0114, 0145, 0169, 0194, 0213, 0226, 0227, 0263, 0268, 0317 |
| MUTATE | 9 | 0074, 0164, 0264, 0278, 0286, 0304, 0305, 0307, 0323 |
| KILL | 6 | 0025, 0033, 0042, 0133, 0252, 0332 |

**Freshness kills** (a 2024–2026 paper directly takes the headline): **0332, 0133, 0042**.
**Freshness-forced mutations:** 0074, 0164, 0264, 0286, 0304, 0305, 0307, 0323.
No idea earned an unconditional SURVIVE: that is the point of this stage. Every survivor
now carries a named experiment that is the difference between a paper and a rejection.

---

# PART 1 — The five mandated freshness targets

## W2-B-0332 — Visual chain-of-thought is post-hoc theater (artifact-swap intervention)

**REJECTION.** This paper was published while you were writing it. *On the Faithfulness of Visual
Thinking: Measurement and Enhancement* (arXiv 2510.23482) probes multimodal-CoT faithfulness
"through intervention on its visual and textual parts," corrupting the visual thoughts and measuring
answer change — and reports your headline result verbatim: "the model's predictions remain nearly
unchanged under visual intervention," i.e., the cited visual evidence is largely not load-bearing.
It then goes further than your proposal by building a training fix (SCCM). Around it, an entire
intervention ecosystem has formed: Evidence-RL (arXiv 2608.08021) turns region-level counterfactual
interventions into RL rewards and cites a *string* of 2024–2026 inference-time counterfactual
visual-intervention papers; V-SEAM (EMNLP 2025) does semantic-level causal visual editing; Fox
(arXiv 2606.27596) does causal attention interventions for visual grounding. Agent E flagged this
exact tripwire: "one arXiv hit on visual-evidence interventions for VLM CoT would flip 0332
SURVIVE→KILL overnight." The hit exists. The remaining sliver — mid-episode artifact *swap* in
agentic tool-use loops rather than corruption of generated visual thoughts — is a setting change,
not a question change, and the answer ("substantially theater") is already on the record.

**Hidden assumptions:** (1) that corrupting/swapping visual artifacts stays in-distribution for the
agent (2510.23482 already fought this); (2) that "the box the model drew" is the evidence the model
used, rather than a decorative output channel — which is exactly what the scooping paper found;
(3) that answer-change rate is interpretable without a difficulty-matched control episode.

**Fresh prior-work hits:**
- On the Faithfulness of Visual Thinking: Measurement and Enhancement — https://arxiv.org/abs/2510.23482
- Evidence-RL: Towards Evidence-intensive Visual Reasoning — https://arxiv.org/html/2608.08021v1
- V-SEAM: Visual Semantic Editing and Attention Modulating (EMNLP 2025) — https://aclanthology.org/2025.emnlp-main.880.pdf
- Fox: Dismantling Pathological Shortcuts, causal framework for faithful LVLM decoding — https://arxiv.org/html/2606.27596

**Killer experiment:** NONE. Any experiment you can run, 2510.23482 has either run or made
incremental. The agentic-loop variant is a delta a reviewer will price at a workshop paper.

**VERDICT: KILL (freshness).** Mutated claim: none retained. If the PI wants a survivor in this
space, it must be a *new question* (e.g., does RL-training on counterfactual evidence rewards
transfer faithfulness across tasks — but that is Evidence-RL's own future-work section, i.e.,
already someone else's roadmap).

---

## W2-B-0001 — Register/high-norm artifacts as a free per-pixel error predictor

**REJECTION.** Three attacks, in increasing order of severity. (1) *Novelty of the primitive:*
"feature norm as confidence" is an established OOD/uncertainty primitive (FeatureNorm, CVPR 2023
[not re-verified]); your contribution reduces to spatializing a known scalar trick. (2) *The marker
is unreliable:* PH-Reg (arXiv 2505.21501) reports that artifact tokens "are not necessarily
high-norm, and can be low-norm as well" — your predictor variable does not even reliably flag the
artifacts it is named after. (3) *The confounder is fatal if unhandled:* Darcet et al. established
that high-norm tokens appear "primarily in low-informative background areas." Background interiors
are where segmentation is trivially correct and object boundaries — where errors live — are where
artifacts are rare. Your norm map is plausibly a *background detector*, and its error-prediction
AUROC may be matched or beaten by embarrassing baselines: distance-to-predicted-boundary, local
edge density, or the probe's own softmax entropy, all equally free. Meanwhile the deployment story
("free uncertainty from artifacts") is evaporating: test-time registers (NeurIPS 2025,
arXiv 2506.08010) remove the artifacts *for free, post hoc*, and DINOv3-era backbones ship with
registers — the population of models on which your signal exists is shrinking quarterly.

**Hidden assumptions:** (1) norm magnitude is monotone in error probability *within* foreground,
not just between background/foreground strata; (2) artifact positions are input-dependent enough
to track image-specific errors (SINDER, arXiv 2407.16826, shows the defect *direction* is largely
weight-determined); (3) the signal survives on register-equipped/repaired backbones, else the paper
is an obituary for a bug class that is already fixed; (4) sparse artifact coverage (a few tokens per
image) can move aggregate AUROC at all.

**Fresh prior-work hits:**
- Vision Transformers Don't Need Trained Registers (test-time registers) — https://arxiv.org/abs/2506.08010
- PH-Reg: Vision Transformers with Self-Distilled Registers — https://arxiv.org/abs/2505.21501
- Do All Vision Transformers Need Registers? A Cross-Architectural Reassessment — https://arxiv.org/html/2603.25803
- SINDER: Repairing the Singular Defects of DINOv2 — https://arxiv.org/abs/2407.16826
- Inference-Time Attention Engineering (artifact attenuation) — https://arxiv.org/html/2410.04801
- (No paper found selling the norm map as a per-pixel uncertainty channel — the specific claim is still open.)

**Killer experiment (cheap, ~1 GPU-week):** frozen DINOv2 (no registers), DINOv2-with-registers,
and test-time-register-patched model; linear probe on ADE20K + Cityscapes; per-pixel error
prediction AUROC/AUPRC of (a) token-norm map, (b) probe softmax entropy, (c) distance-to-boundary,
(d) local edge density, (e) feature-distance to train prototypes — **stratified by
foreground/background and by distance-to-boundary**. The paper exists only if (a) beats (b)–(e)
within foreground strata on register-free models AND the authors state plainly what happens on
register-equipped models. A weak/negative result is publishable only as a short deflationary note.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Mutated framing (mandatory): "is the artifact map an
uncertainty channel or just a saliency prior? A stratified audit" — uncertainty-baselines paper,
not a free-lunch paper.

---

## W2-B-0307 — Language alignment causally degrades metric depth at matched data

**REJECTION.** The central novelty claim — "nobody has done the controlled matched-data,
matched-architecture contrast" — expired in October 2025. *Data or Language Supervision: What Makes
CLIP Better than DINO?* (arXiv 2510.11835, EMNLP 2025 Findings) pre-trains CLIP and DINO "under
controlled settings — using the same architecture, dataset, and training configuration," then
attributes semantic-vs-low-level differences to the objective. Your proposal is that paper's
experimental design pointed at a different probe battery. Worse for your surprise budget: their
matched-data result already leans your way (DINO better on vision-centric evaluations), and the
broader literature has been saying "language hurts low-level geometry" since CVPR 2024 (*On the
Robustness of Language Guidance for Low-Level Vision Tasks*, arXiv 2404.08540) on top of the
correlational Probing-3D-Awareness result (arXiv 2404.08636) you already concede. So the community
default you propose to test is now supported observationally, behaviorally, AND by a matched-data
contrast at the VQA level. A reviewer prices the residual — dense geometric probes on matched pairs
— as a table, not a paper, and the pretraining compute you request as an expensive way to produce it.

**Hidden assumptions:** (1) matched-caption-availability data is representative pretraining data
(captioned subsets are object-centric web photos — the depth-cue distribution is not neutral);
(2) one alignment recipe (CLIP-style contrastive) stands in for "language" — SigLIP/CapPa/latent
alignment may not share the deficit; (3) linear decodability of metric depth from frozen features is
the right operationalization of "geometric structure"; (4) the effect size at feasible scale
(ViT-S/B, ~10–100M images) predicts the flagship-scale effect.

**Fresh prior-work hits:**
- Data or Language Supervision: What Makes CLIP Better than DINO? — https://arxiv.org/abs/2510.11835
- On the Robustness of Language Guidance for Low-Level Vision Tasks (CVPR 2024) — https://arxiv.org/abs/2404.08540
- Probing the 3D Awareness of Visual Foundation Models (CVPR 2024) — https://arxiv.org/abs/2404.08636
- Hybrid-grained aggregation noting CLIP/DINO geometric complementarity — https://arxiv.org/html/2510.09320v1

**Killer experiment (cheap first stage, no pretraining):** obtain/replicate the 2510.11835 matched
checkpoints (same architecture/data/config CLIP-vs-DINO) and run the El Banani 3D-probe battery
plus metric-depth linear probes on them. If the matched pair reproduces the depth deficit, THEN the
dose-response stage (alignment-weight dial λ ∈ {0, 0.1, …, 1} on one matched corpus) becomes the
paper: not "does language hurt depth" (assumed by everyone, now half-shown) but "the deficit's
functional form in alignment strength, and which depth cues (occlusion, perspective, texture
gradient) carry it."

**VERDICT: MUTATE.** Mutated claim: "the *dose-response and cue-decomposition* of the
language-alignment geometry tax at matched data — extending 2510.11835 from VQA-level to dense
geometry." The binary causal claim is no longer worth a PhD year; the mechanism-resolved version is.

---

## W2-B-0114 — VPT prompt tokens are trainable registers

**REJECTION.** The "two literatures have never been connected" pitch is stale: DA-VPT
(arXiv 2505.23694) already observes register-style artifacts in VPT prompt attention maps, cites
Darcet et al., and calls registers "analogous to learnable prompts" — the connection is in print,
you would merely be the first to *quantify* it. The mechanism story is also partially published:
the test-time-registers paper (arXiv 2506.08010) shows register function is reproducible by a pure
*attention bias*, supporting Sun et al.'s claim that registers primarily act as attention biases —
so "VPT tokens absorb global aggregation" has a known, more specific competitor mechanism you must
disaggregate. Your frozen-random-token control is confounded as designed: inserting any token
changes every softmax denominator in every attention layer (a temperature effect), so "X% of VPT's
gain reproduced by frozen tokens" conflates register absorption with attention smoothing. And the
most likely outcome — partial reproduction, say 20–40% — is mush: VPT partly works by learning
(nobody doubted it) and partly by token insertion (mildly interesting), with the headline
"reattribution" claim supported by neither extreme. Finally, register-equipped backbones (DINOv2-reg,
DINOv3) are becoming default; a mechanism story about register-free ViTs is a paper about the past.

**Hidden assumptions:** (1) frozen-random tokens isolate "register function" rather than generic
attention-capacity/temperature effects; (2) VPT benchmark gains (VTAB-style) are the right target —
if VPT's gains are largely head-tuning artifacts, the decomposition inherits that fragility;
(3) high-norm signature = register function (PH-Reg shows artifact tokens can be low-norm);
(4) results transfer across VPT-shallow vs VPT-deep, which have different insertion mechanics.

**Fresh prior-work hits:**
- DA-VPT: Semantic-Guided Visual Prompt Tuning (artifact discussion §Artifact Consideration) — https://www.arxiv.org/pdf/2505.23694
- Vision Transformers Don't Need Trained Registers (registers ≈ attention biases) — https://arxiv.org/abs/2506.08010
- Do All Vision Transformers Need Registers? — https://arxiv.org/html/2603.25803
- Visual Prompt Tuning (Jia et al., ECCV 2022) — https://arxiv.org/abs/2203.12119
- Vision Transformers Need Registers (Darcet et al., ICLR 2024) — https://arxiv.org/abs/2309.16588

**Killer experiment (the afternoon experiment, now with 4 arms + 2 backbones):** on a register-free
backbone AND its register-equipped sibling, compare (a) full VPT, (b) frozen-random tokens,
(c) attention-bias-only injection (test-time-register style, no token), (d) no-token baseline,
across ≥3 dense + 3 classification tasks; report gain decomposition and learned-token norm/attention
signatures. Arm (c) is what converts "cosmetic analogy" into a mechanism identification; the
register-equipped backbone arm tests the paper's own prediction (VPT should gain less there) —
a pre-registered directional prediction that, if confirmed, silences the reviewer.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Still the best risk-adjusted bet in the batch — but only in the
4-arm form with DA-VPT cited up front. The 2-arm version E scored is no longer publishable alone.

---

## W2-B-0304 — Language quantizes continuous shape space (morph discontinuities)

**REJECTION.** The phenomenon you present as new — categorical warping of representations along
morph continua in category-trained networks — is a 2021 result: Bonnasse-Gahot & Nadal,
*Categorical Perception: A Groundwork for Deep Learning* (arXiv 2012.05549), demonstrated
within-category compression and between-category expansion along morphed continua in deep networks,
with the effect strengthening with depth, and it is standard cognitive-science background besides.
So "features jump at category boundaries" is expected from *any* categorical supervision — an
ImageNet-supervised ViT should quantize too, and your central causal attribution ("language did
it") collapses into "categories did it" unless you run the supervised-classifier control that your
proposal conspicuously lacks. The tooling is also no longer yours: a 2026 framework for generating
semantic morph continua and comparing human and machine boundaries already exists
(arXiv 2603.24730, rabbit–duck morphs, human-vs-model boundary placement), and categorical-perception
analyses in LLM hidden states (arXiv 2603.28258) mean the "CP in foundation models" flag is planted.
What remains genuinely yours: the SSL-vs-CLIP-vs-supervised three-way contrast on *shape* morphs, and
the alignment of jump locations with *human naming boundaries* rather than taxonomy labels. That is
a real paper, but it is one-third the paper you pitched, and morph-pipeline artifacts (your own
stated risk) can manufacture discontinuities in every arm.

**Hidden assumptions:** (1) SSL models are a clean null (DINOv2's distillation and clustering
objectives can induce their own discreteness — the "SSL glides" premise is unverified); (2) morph
midpoints are on-manifold for all model families equally, else discontinuity size confounds with
familiarity; (3) human naming boundaries are stable/portable across the render styles used;
(4) curvature statistics on trajectories distinguish "quantization" from generic non-smooth feature
response to non-semantic image change.

**Fresh prior-work hits:**
- Categorical Perception: A Groundwork for Deep Learning — https://arxiv.org/abs/2012.05549
- A Framework for Generating Semantically Ambiguous Images to Probe Human and Machine Perception — https://www.arxiv.org/pdf/2603.24730
- Categorical Perception in LLM Hidden States — https://arxiv.org/abs/2603.28258
- Is CLIP the main roadblock for fine-grained open-world perception? (coarse-category bias in CLIP space) — https://arxiv.org/pdf/2404.03539

**Killer experiment:** the full contrast grid — {CLIP-lineage, SSL (DINOv2, MAE), *supervised
ImageNet ViT*} × {3D-render morphs, latent morphs, image-space morphs} — with the pre-registered
prediction that jump *locations* align with human naming boundaries only in language-aligned models
while supervised models jump at taxonomy boundaries and SSL models jump least. Add a
depth/pose-decodability readout at the boundary to link quantization to the dense-regression story.
Without the supervised control this is unreviewable; with it, either outcome is informative.

**VERDICT: MUTATE.** Mutated claim: "categorical warping follows the *supervision taxonomy*:
naming boundaries predict discontinuity locations in language-aligned models, class boundaries in
supervised models, neither in SSL — a dissociation of *which* categories quantize shape space."
The slogan "language quantizes shape" overclaims and dies; the dissociation survives.

---

# PART 2 — The rest of Agent E's twenty PhD-year bets

## W2-B-0074 — Modality-gap collapse as a phase transition predicting zero-shot loss

**REJECTION.** The load-bearing novelty claim — "the trajectory of the gap during fine-tuning is
unobserved" — is false as of mid-2025, twice over. MG-CLIP (arXiv 2507.09118) "analyze[s] the
variations in the modality gap during the fine-tuning of vision-language pre-trained models,"
concludes the gap "effectively reflects the extent to which pre-trained knowledge is preserved,"
and builds a method on gap preservation. GNSP (arXiv 2507.19839) states outright that "sharp
variations of this gap serve as an effective indicator of unstable inter-modal relationships and
correlate with the degradation of zero-shot ability," and likewise intervenes to stabilize it.
Gap-dynamics-as-forgetting-indicator is now the *premise* of two methods papers, not a discovery.
What you have left is the fine structure: is the collapse a genuine phase transition (sharp onset in
a narrow step window) rather than drift, and does onset *lead* zero-shot degradation with enough
margin to act — versus loss curves, weight-displacement norms, and MG-CLIP's own monitoring? That
is a real measurement question, but it is a leading-indicator bake-off, not the geometric discovery
E's top tier advertised.

**Hidden assumptions:** (1) a scalar gap statistic (centroid distance) captures the relevant
geometry — Two Effects One Trigger (arXiv 2404.07983) shows few embedding dimensions drive the gap,
so the scalar may move for irrelevant reasons; (2) collapse *precedes* rather than co-occurs with
zero-shot loss (lead time is the entire practical value and is unmeasured); (3) single-task
fine-tuning behaves like the CL settings where the indicator is established.

**Fresh prior-work hits:**
- MG-CLIP: Mind the Gap — preserving/compensating the modality gap in CLIP CL — https://arxiv.org/abs/2507.09118
- GNSP: Gradient Null Space Projection (gap variation as degradation indicator) — https://arxiv.org/abs/2507.19839
- Two Effects, One Trigger (gap statics, dimensions, object bias) — https://arxiv.org/abs/2404.07983
- ZAF, Stabilizing Zero-Shot Prediction (NeurIPS 2024) — https://papers.neurips.cc/paper_files/paper/2024/file/e7feb9dbd9a94b6c552fc403fcebf2ef-Paper-Conference.pdf

**Killer experiment (cheap):** fine-tune CLIP on 4 tasks × 4 LRs × 3 seeds, log per-step gap
statistics + zero-shot metrics; test (a) changepoint sharpness against a smooth-drift null,
(b) *lead time* of gap-collapse onset over zero-shot-degradation onset, (c) predictive AUC vs loss-,
gradient-, and weight-norm baselines. Survives only if lead time is positive, robust, and the gap
beats the boring predictors.

**VERDICT: MUTATE.** Mutated claim: "gap collapse is a *leading* indicator with actionable lead
time, benchmarked against cheap baselines, in single-task fine-tuning" — positioned explicitly as
the quantitative validation MG-CLIP/GNSP assumed. Demoted from top tier.

---

## W2-B-0323 — Mention bias: unmentioned-but-visible content is decodability-poor

**REJECTION.** Both halves of this paper exist. The measurement half: *Interpreting the structure of
multi-object representations in vision encoders* (arXiv 2406.09067) already ran the
mentioned-vs-unmentioned probe — their "caption gap" shows caption-trained models (CLIP, BLIP)
decode caption-mentioned objects well and "the model's ability to decode [an unmentioned] object
plummeted," with SSL-family comparisons in the model roster. The causal half: *Two Effects, One
Trigger* (arXiv 2404.07983) manipulated caption presence directly in controlled retraining and
showed models become biased toward whatever the captions consistently mention — your
"caption-intervention retraining at small scale" is their Figure 6(b). BiAug (arXiv 2310.01330,
ICCVW 2025) already builds mitigation for reporting-bias omissions. What is left is the connective
tissue: a *continuous* mention-probability dose-response estimated from real corpora, per-pixel
(dense) rather than object-level decodability, and SSL normalization for visual difficulty. Useful,
quantitative — and exactly the kind of "their union, with a WordNet frequency axis" contribution
that Reviewer 2 feeds on.

**Hidden assumptions:** (1) corpus mention probability is estimable at category level without
circularity (detector-based visibility estimates use models trained on the same biased data);
(2) SSL decodability is a clean visual-difficulty control (SSL has its own salience biases);
(3) the dense version differs materially from the object-level version already published.

**Fresh prior-work hits:**
- Interpreting the structure of multi-object representations in vision encoders — https://www.alphaxiv.org/abs/2406.09067 (arXiv 2406.09067)
- Two Effects, One Trigger — https://arxiv.org/abs/2404.07983
- BiAug: reporting bias in visual-language datasets — https://arxiv.org/abs/2310.01330 / https://openaccess.thecvf.com/content/ICCV2025W/MRR%202025/papers/Wu_Towards_Reporting_Bias_in_Visual-Language_Datasets_Bi-modal_Data_Augmentation_by_ICCVW_2025_paper.pdf
- Seeing through the Human Reporting Bias (Misra et al., CVPR 2016) — https://arxiv.org/abs/1512.06974

**Killer experiment:** per-pixel decodability across ~200 categories spanning the full corpus
mention-probability range, SSL-normalized, fit the dose-response curve; then ONE targeted
caption-intervention retraining at small scale where mention probability of held-out categories is
raised/lowered synthetically, testing whether the *curve* (not just the gap) shifts as predicted.
The curve + curve-shift is the only deliverable 2406.09067 and 2404.07983 don't own.

**VERDICT: MUTATE.** Mutated claim: "the mention-probability *dose-response law* for dense
decodability, and its causal shift under caption intervention." Demoted from top-5; must cite both
scooping papers in the abstract.

---

## W2-B-0104 — PEFT preserves pretrained invariances dense tasks must break

**REJECTION.** Strip the instrumentation and this is "LoRA learns less" (Biderman et al., TMLR 2024)
restated in invariance vocabulary: constrained updates stay near the pretrained function, so of
course pretrained invariances persist — the claim risks being *analytically true* and empirically
empty. The causal arrow is unargued: retained invariance may be a passive correlate of small
functional displacement (measure: any distance), not the *mechanism* of dense underperformance; you
need tasks where invariance-breaking demand is dissociated from difficulty, and constructing that
dissociation is the entire burden. Meanwhile the intruder-dimensions result (arXiv 2410.21228) says
LoRA solutions are structurally *different*, not merely conservative — if LoRA can add rank-one
intruders, it is not obvious it cannot break a shift invariance when the loss demands it; your
premise needs that demonstration, not assumption. Finally, the actionable payoff ("predict when
LoRA fails from frozen-model invariance") competes with a one-line alternative: just raise the rank
(adaptive-rank PEFT is standard practice) — if higher rank fixes it, your "no rank increase will
help" headline is falsified by the first ablation any reviewer requests.

**Hidden assumptions:** (1) invariance is measurable on encoder features without head contamination;
(2) pretrained invariances are actually strong in modern SSL backbones (DINOv2 is surprisingly
equivariance-rich — the premise that there is much invariance to inherit needs its own measurement);
(3) the dissociation tasks exist and can be matched on difficulty; (4) "invariance-breaking demand"
of a task can be quantified independently of the models being compared (else circular).

**Fresh prior-work hits (E's, still the frontier):**
- LoRA Learns Less and Forgets Less — https://arxiv.org/abs/2405.09673
- LoRA vs Full Fine-tuning: An Illusion of Equivalence — https://arxiv.org/abs/2410.21228

**Killer experiment:** the invariance-dissociation grid: task pairs matched on frozen-probe
difficulty but differing in invariance-breaking demand (e.g., color-invariant classification vs
color-sensitive dense regression; shift-invariant tagging vs sub-patch localization); LoRA (across
ranks, incl. high rank) vs full FT; measure retained invariance + task gap. The paper lives only if
(a) the PEFT gap tracks invariance-breaking demand at matched difficulty AND (b) the gap persists
at high rank. If (b) fails, mutate honestly into a rank-dependence study and merge with 0101.

**VERDICT: SURVIVE-IF-EXPERIMENT.** The mechanism framing is attackable but the dissociation
design, if it works, is the only thing in the 009x/010x family that separates mechanism from
tautology. Correlated risk with 0098/0101 noted in the report.

---

## W2-B-0268 — Synthetic-image contamination of web benchmarks distorts rankings

**REJECTION.** The estimator is the paper, and the estimator is broken. Generated-image detectors
have unknown, distribution-dependent error rates; Hataya et al. (ICCV 2023, arXiv 2211.08095)
already warned that "easy detection of generated images may not be applicable to up-to-date
generative models." Your contamination-rate-by-collection-date curve is therefore uninterpretable
without ground truth you don't have, and your ranking-distortion result has a lethal circularity:
detector-flagged subsets are not random — they oversample stylized, smooth, object-centric images —
so ranking changes on "contaminated" subsets may reflect *image-property* stratification, not
contamination per se. A placebo test on guaranteed-clean pre-2021 data flagged by the same detector
would likely also shift rankings, and you did not propose it. Meanwhile the adjacent
integrity-audit space is crowding fast: real-duplicate leakage audits (ICCVW 2025), VLM benchmark
contamination detection (ICLR 2026) — reviewers will ask what your audit adds beyond "one more
integrity scare with a shakier detector."

**Hidden assumptions:** (1) detector ensembles + manual subsample bound the error usefully at the
low contamination rates in question (base-rate problem: at 2% contamination, even 95%-specific
detectors produce mostly false positives); (2) "collection date" is recoverable for web benchmarks;
(3) contaminated-vs-clean ranking deltas exceed subset-resampling noise.

**Fresh prior-work hits:**
- Data Leakage in Visual Datasets (ICCVW 2025) — https://openaccess.thecvf.com/content/ICCV2025W/Findings/papers/Ramos_Data_Leakage_in_Visual_Datasets_ICCVW_2025_paper.pdf
- Will Large-scale Generative Models Corrupt Future Datasets? — https://arxiv.org/abs/2211.08095
- Contamination Detection for VLMs using Multi-Modal Semantic Perturbations (ICLR 2026) — https://proceedings.iclr.cc/paper_files/paper/2026/file/9aa7c1c0e510f2a1986108fce49c3e60-Paper-Conference.pdf
- (No paper found measuring generated-image contamination *rates in benchmarks* + induced ranking distortion — the specific claim remains open.)

**Killer experiment (the estimator-validation the reviewer demands):** (a) placebo arm: run the
detector pipeline on pre-2021-crawled benchmarks (guaranteed clean); any "ranking distortion" found
there calibrates the circularity artifact. (b) Injection arm: seed known generated images at
controlled rates into clean benchmarks; verify the pipeline recovers rates and distortion.
(c) Provenance arm: manual + C2PA/watermark verification on a stratified subsample with reported
CIs. Only then run the headline audit. This is all cheap; it is also the difference between
eval-integrity science and a blog post.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Urgency real, window closing; but the paper is dead on arrival
without the placebo/injection calibration arms.

---

## W2-B-0213 (mutated, merged with 0200) — Resolution × probe confound audit of VFM rankings

**REJECTION.** Kerssies et al. (arXiv 2404.12172) showed VFM segmentation rankings shift across
benchmark settings and issued protocol recommendations; you are adding an axis to their Figure 1
and calling it a confound. The deeper problem is that your correction is itself a choice: "matched
effective resolution" has no unique definition (match input pixels? feature-map size? receptive
field? compute?), and models *co-designed* with their native resolution are penalized by any
matching — at which point benchmark authors will reply that resolution handling IS a capability,
not a confound, and your "corrected" rankings are just different rankings under a different
convention. Your own risk note concedes multiple defensible matchings. A result that inverts under
the auditor's own free parameter is not an audit; it is a preference.

**Hidden assumptions:** (1) a defensible partition of "resolution handling" from "representation
quality" exists at all; (2) published conclusions are pinned enough to be "inverted" (many hedge);
(3) probe-capacity and resolution effects are separable in the joint sweep rather than interacting
three-ways with task.

**Fresh prior-work hits (E's, confirmed frontier):**
- How to Benchmark VFMs for Semantic Segmentation? — https://arxiv.org/abs/2404.12172
- Attention, Please! Revisiting Attentive Probing — https://arxiv.org/abs/2506.10178
- Res-Bench (MLLM resolution instability) — https://arxiv.org/abs/2510.16926

**Killer experiment:** run the audit under ≥3 pre-registered matching definitions (pixel-matched,
feature-map-matched, FLOP-matched) × probe capacities; the deliverable is the set of published
conclusions that invert under **all** matchings (robust inversions) vs those that are
convention-dependent. Robust inversions silence the "your convention" objection; if the robust set
is empty, publish that as "published rankings are resolution-robust" — also useful, less glamorous.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Survives only as the all-matchings-inversion audit; any
single-convention version gets the rejection above verbatim.

---

## W2-B-0226 (mutated) — Shift budgets: frozen degrades gracefully, tuned sharply

**REJECTION.** The direction is textbook (LP-FT, WiSE-FT, Andreassen et al.), and E already conceded
the mutation to "functional form and its stability." What remains is built on an unsolved
measurement problem: "shift magnitude" is not a scalar. Corruption severity, geographic distance,
and temporal drift are incommensurable axes; any budget curve is parameterized by an arbitrary
ladder ordering, and your own risk note admits it. Crossover points s* will not transfer across
shift families — that is the expected outcome — leaving you with a negative result about a construct
(scalar shift budget) you invented. And the practical payoff ("budgets on model cards") assumes
deployers can estimate their expected shift on your ladder, which nobody can. WiSE-FT interpolation
also dominates the deployment decision this curve is supposed to inform: why choose frozen-vs-tuned
when the interpolation gives you both?

**Hidden assumptions:** (1) an ordering of shifts exists that is even approximately
model-independent; (2) frozen-vs-tuned is the relevant dichotomy in the WiSE-FT era; (3) curve
*shape* differences (cliff vs linear) are estimable with feasible eval budgets at high severities
where datasets get tiny and noisy.

**Killer experiment:** fit budget curves on corruption-severity ladders for 6 models; test
(a) cross-family transfer of crossover points to geographic/temporal shifts, (b) whether adding
WiSE-FT interpolation curves collapses the frozen/tuned dichotomy. Pre-register the functional
forms. If crossovers transfer within stated tolerance, the budget construct is real; if not, report
the instability as the finding and stop there.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Weakest of the surviving bets; the honest expected outcome is
the negative branch, which is a modest paper.

---

## W2-B-0101 (mutated) — Task-indexed required-rank law for PEFT

**REJECTION.** Your regressor is noise: the "spectral mass of full-FT deltas" depends on seed, LR,
and schedule — full fine-tuning solutions are not unique, so the task's "intrinsic update rank" is
an artifact of one trajectory unless you show cross-seed stability first, which no one has. Your
premise also inherits the corpse of 0098: intruder-dimension work (arXiv 2410.21228) shows LoRA does
not find truncated-full-FT solutions, so there is no a-priori reason LoRA accuracy should track
captured spectral mass of a solution it does not approximate — the law may fail not because dense
tasks are high-rank but because the whole truncation picture is wrong. And the practitioner story is
obsolete on arrival: adaptive-rank PEFT (AdaLoRA/DoRA-era) already allocates rank empirically;
a "law" that requires a full fine-tuning run to compute its predictor is a rank-selection rule that
costs more than the thing it selects.

**Hidden assumptions:** (1) delta spectra are stable across seeds/LR (unverified, likely false in
the tail); (2) a cheap proxy for spectral mass exists that does not require full FT (else no
practical value); (3) layerwise heterogeneity aggregates into a single task index; (4) accuracy-vs-
captured-mass is monotone even though LoRA solutions are structurally different objects.

**Killer experiment:** (a) cross-seed stability of full-FT delta spectra (3 seeds × 3 tasks — if
unstable, stop); (b) LoRA rank sweeps regressed on captured mass vs two cheap baselines (gradient
covariance spectrum at init; NTK-style probe) — the law must beat the cheap predictors to matter;
(c) held-out-task prediction. Bounded, ~2–3 GPU-weeks.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Lives or dies on step (a), which nobody has run and which is
nearly free. Correlated with 0104/0098 family risk.

---

## W2-B-0145 (mutated) — Spatial calibration decays before accuracy in dense adaptation

**REJECTION.** The temporal-ordering headline is published for CL and LLMs (E's own attack found
arXiv 2404.07817 and 2604.23987); your dense-vision version must therefore stand on the *spatial*
claim alone, and that claim has a one-parameter defeater: temperature. If per-region temperature
re-tuning restores calibration (your own minimal experiment includes this arm), then "calibration
forgets first" collapses to "confidence scale drifts first" — a finding of approximately zero
deployment consequence, since everyone re-tunes temperature. The onset comparison is also
metrically rigged: ECE and accuracy are incommensurable, so "earlier onset" depends entirely on
your onset definitions and noise floors; ECE estimators are biased at region level with few pixels
per bin. A reviewer will make you show the ordering survives (a) temperature correction,
(b) proper scoring rules, (c) matched onset-detection procedures — and the literature suggests it
may not.

**Hidden assumptions:** (1) calibration decay is not reducible to a global/regional temperature
drift; (2) region-level ECE is estimable at the doses where the ordering is claimed; (3) the
ordering has practical lead time (as with 0074, lead time is the value and is unmeasured).

**Fresh prior-work hits (E's):**
- Calibration of Continual Learning Models — https://arxiv.org/abs/2404.07817
- Continual Calibration: Coverage Can Collapse Before Accuracy — https://arxiv.org/abs/2604.23987

**Killer experiment:** adaptation-dose trajectories on 3 dense tasks; old-task regional accuracy,
ECE, Brier, and *temperature-corrected* ECE; onset detection with one pre-registered procedure
applied to all metrics. The paper exists iff the ordering survives temperature correction and the
region-level early-warning signal predicts later accuracy loss with usable lead time.

**VERDICT: SURVIVE-IF-EXPERIMENT** (narrowly; the temperature arm is the whole ballgame).

---

## W2-B-0194 — Segmentation sycophancy: confidence rises with prompts, accuracy doesn't

**REJECTION.** Your "law" is plausibly pure selection bias: in real and simulated interaction,
prompt count is not randomized — users add prompts *because* the case is hard, so conditional
accuracy at high interaction depth is mechanically depressed while confidence (trained to predict
IoU improvements from added prompts) rises on average. Without randomized prompt dose at fixed
difficulty, the "divergence curve" is a difficulty-stratification artifact wearing a safety costume.
The space is also no longer empty: SAM confidence-error misalignment is documented ("mask-level
confidence confusion" and confident-errors under shift in RUAC, arXiv 2605.10603), UncertainSAM
(ICML 2025) traces uncertainty to insufficient prompts, and BALD-SAM (arXiv 2603.10828) actively
exploits prompt-conditioned uncertainty — so "SAM confidence misbehaves under prompting" is
established terrain; only the dose-response *shape* is yours.

**Hidden assumptions:** (1) a standardized confidence exists across architectures (mask-probability
aggregates and IoU-head outputs are not the same object and disagree); (2) simulated clickers
represent human escalation behavior (RClicks, arXiv 2410.11722, says simulation policies distort
exactly such curves); (3) "accuracy doesn't rise" holds conditional on difficulty, not just
marginally.

**Fresh prior-work hits:**
- UncertainSAM (ICML 2025) — https://proceedings.mlr.press/v267/kaiser25a.html
- RUAC: Segment Anything with Robust Uncertainty-Accuracy Correlation — https://arxiv.org/html/2605.10603v3
- BALD-SAM: Disagreement-based Active Prompting — https://arxiv.org/abs/2603.10828
- RClicks (NeurIPS 2024) — https://arxiv.org/abs/2410.11722

**Killer experiment (cheap, decisive):** randomized-dose protocol — fix image/object strata by
frozen-model difficulty, assign prompt count randomly (1–10), multiple click policies + the RClicks
human-click distribution; plot confidence and accuracy vs dose *within strata*. Sycophancy exists
iff the confidence-accuracy gap grows with randomized dose. One week of compute, ends the argument.

**VERDICT: SURVIVE-IF-EXPERIMENT.** Catchy and safety-adjacent, but only the randomized version is
a paper; the observational version is a confound.

---

## W2-B-0169 — Negative clicks hurt beyond 2–3: an anti-monotone dose-response

**REJECTION.** RClicks (NeurIPS 2024) demonstrated that interactive-segmentation conclusions are
hostage to click-simulation policy — and your entire effect lives inside that hostage situation:
"beyond 2–3 negatives it degrades" will hold under some placement policies and invert under others,
because simulated negative clicks concentrate in exactly the ambiguous regions where masks are
fragile. Practitioner folklore already says "too many points confuse SAM," so the qualitative
finding will read as confirming a known nuisance, and the similarity-based onset predictor is
decorative until it survives cross-policy transfer. The paper is one figure unless the human-click
arm and the policy-robustness analysis carry it.

**Hidden assumptions:** (1) a policy-robust dose-response exists to be measured; (2) negative-click
semantics are comparable across models (SAM-family vs RITM-family treat background points
differently); (3) the onset is a property of the image-object pair, not of the clicker.

**Fresh prior-work hits:**
- RClicks — https://arxiv.org/abs/2410.11722
- BALD-SAM (prompt-informativeness is policy-dependent) — https://arxiv.org/abs/2603.10828

**Killer experiment:** factorial positive×negative sweep under ≥4 policies **including RClicks'
human-derived clickability model**, ≥4 model families; report the dose-response envelope across
policies. The claim survives iff degradation-beyond-k holds across the entire policy envelope
including human-like clicks; the similarity-based onset predictor is validated out-of-policy.

**VERDICT: SURVIVE-IF-EXPERIMENT.**

---

## W2-B-0164 — Relearning speed (savings) reveals memory retention probes miss

**REJECTION.** The savings paradigm has been ported — you were late. *Unlearning Isn't Deletion*
(arXiv 2505.16831, ICML 2026) uses constrained-budget relearning as its primary probe of whether
forgotten knowledge persists, defines relearning protocols with budget matched to the forget set,
compares recovery across data sources, and builds a representational framework (CKA/Fisher/PCA
drift) around forgetting regimes — "forgotten abilities are cheaper to restore" is its running
theme. NeurIPS 2024's *Reawakening knowledge* (arXiv 2403.09613) shows anticipatory recovery
dynamics in cyclic fine-tuning. The insight "behavioral loss overstates representational loss" is
additionally the Davari-CVPR-2022 result E already used to kill 0136. Your residual is a domain
port (VFM dense abilities) plus a curve (savings vs dose) plus a control (never-pretrained heads)
— real work, but the conceptual flag you wanted to plant is planted, in a hotter subfield, with
better instrumentation.

**Hidden assumptions:** (1) "never-trained control" is constructible (scratch heads on matched
architectures confound head capacity with backbone memory); (2) few-shot relearning measures
*retained structure* rather than easier optimization geometry near a fine-tuned solution;
(3) savings percentage is comparable across abilities with different sample complexity.

**Fresh prior-work hits:**
- Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs — https://arxiv.org/abs/2505.16831
- Reawakening knowledge: Anticipatory recovery from catastrophic interference — https://arxiv.org/abs/2403.09613

**Killer experiment:** VFM single-task adaptation; savings curves (few-shot relearning budget vs
recovery) across fine-tuning doses, against BOTH scratch-head controls and representational probes
(CKA, linear-probe retention); the deliverable is the *dissociation*: doses where retention probes
say "gone" but savings say "cheap to restore," localized to layers. Near-free on existing
checkpoints, as E said.

**VERDICT: MUTATE.** Mutated claim: "a savings-vs-dose *quantification* for dense VFM abilities,
dissociating storage from retrieval where retention probes are blind — the vision instantiation of
the reversibility framework of 2505.16831." Conceptual-novelty framing must be dropped.

---

## W2-B-0227 — Cleaner labels transfer worse (label-quality paradox)

**REJECTION.** The clause doing all the work is "at matched source performance," and it cannot be
honestly satisfied: cleaner labels produce higher source accuracy, so matching requires
undertraining or regularizing the clean-label model — introducing exactly the confound the claim is
about. Without matching, "noisy transfers better" is the regularization literature restated: label
smoothing/noise-as-regularizer improving generalization is a 2019-era result (Müller et al., *When
Does Label Smoothing Help?* [not re-verified]), and "precise boundary conventions overfit to
source" is annotation-domain-shift folklore. The synthetic-noise arm is disconnected from the
motivating story (natural annotation variation is structured, not iid flips — your own risk note),
so the headline generalizes from a noise model nobody deploys.

**Hidden assumptions:** (1) a non-circular matching protocol exists; (2) synthetic noise ladders
span the relevant structure of natural annotation variation; (3) the effect is about *labels* and
not about the augmentation/regularization that co-varies with label precision in practice.

**Killer experiment:** use datasets with genuine multi-annotator variation (e.g., multi-rater
medical segmentation; LVIS/COCO dual annotations) rather than synthetic flips: train on
single-rater "precise" vs rater-sampled "noisy" targets at *matched training budget and matched
source Dice on a held-out rater*, then evaluate cross-domain transfer. Only natural-variation
results count; synthetic ladders are supporting material.

**VERDICT: SURVIVE-IF-EXPERIMENT** (the natural-annotation version only; the synthetic-noise paper
is a rejection).

---

## W2-B-0263 — Procedural corruptions beat realistic generated ones for robustness training

**REJECTION.** The bet now swims against published current: WeatherDG (arXiv 2410.12075) and
Cityscape-Adverse (arXiv 2411.00425) both report that diffusion-generated adverse-condition
training data substantially improves real-world robustness (ACDC-style), and
*Are Synthetic Corruptions A Reliable Proxy For Real-World Corruptions?* (arXiv 2505.04835) finds
strong synthetic-real correlation on the evaluation side. Your mechanism ("generation subtly
rewrites scene structure, breaking pixel-label correspondence") is plausible but the comparison is
unidentifiable as proposed: "matched severity coverage" between a procedural fog filter and a
diffusion fog edit has no agreed definition, and generation quality is a moving target — any result
you publish is versioned to SDXL-of-2026 and dies with the next release. The realistic outcome is
"it depends on the corruption family," which is an ablation table, not a dissociation.

**Hidden assumptions:** (1) severity can be equated across pipelines (you propose calibration but
against which reference model?); (2) label integrity is the operative mechanism rather than
diversity/coverage differences; (3) findings survive generator version churn.

**Fresh prior-work hits:**
- WeatherDG — https://arxiv.org/abs/2410.12075
- Cityscape-Adverse — https://arxiv.org/abs/2411.00425
- Are Synthetic Corruptions A Reliable Proxy For Real-World Corruptions? — https://arxiv.org/abs/2505.04835

**Killer experiment:** same source scenes, three arms — procedural corruption, diffusion-edited
corruption (labels reused), diffusion-edited corruption with label-integrity filtering — severity
matched by equal mIoU degradation of a fixed reference model; train identical segmenters; evaluate
on ACDC + real adverse sets; *measure* label-corruption rates per arm (that measurement is the
mechanism test and is novel regardless of which arm wins). Either outcome is informative because
the label-integrity accounting, not the horse race, is the contribution.

**VERDICT: SURVIVE-IF-EXPERIMENT** (reframed: the label-integrity accounting is the paper; the
"procedural beats generated" slogan is bait for a fight you may lose).

---

## W2-B-0286 — Site-of-origin decodability: natural VFMs vs medical FMs

**REJECTION.** The audit exists. *Current Pathology Foundation Models are unrobust to Medical
Center Differences* (arXiv 2501.18055) measures exactly your quantity — center-of-origin
decodability from FM embeddings — finds "the medical center of origin is predicted more accurately
than the tissue source and cancer type," introduces a Robustness Index ranking FMs by
biological-over-confounder dominance, and links same-center confounding to downstream error
structure. PANDA-PLUS-Bench extends it (slide-ID prediction surviving color normalization and
grayscale); *Towards robust foundation models for digital pathology* quantifies the spurious-
correlation dose-response. Your differentiators — natural-vs-medical FM families, radiology
modalities, and the decodability→cross-site-transfer correlation — are a roster change plus one
regression on top of an occupied protocol. And your provocative direction (natural VFMs *more*
site-invariant) is now merely one plausible cell of a table someone else built.

**Hidden assumptions:** (1) site decodability inversely predicts transfer (2501.18055 suggests
same-center confounding drives errors, but the cross-model correlation is unestablished);
(2) site is separable from population case-mix with scanner-matched subsets (rarely available in
radiology); (3) pathology conclusions do not already answer the radiology question in reviewers'
minds.

**Fresh prior-work hits:**
- Current Pathology FMs are unrobust to Medical Center Differences — https://arxiv.org/abs/2501.18055
- PANDA-PLUS-Bench — https://www.mdpi.com/3042-6707/1/2/14
- Towards robust foundation models for digital pathology — https://pmc.ncbi.nlm.nih.gov/articles/PMC13260997/
- Knowledge-guided adaptation of pathology FMs (site-signature mitigation) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12749728/

**Killer experiment:** cross-family (DINOv2/DINOv3/CLIP vs 4+ medical FMs) × cross-modality (CXR,
CT, pathology) site-decodability + cross-site transfer on scanner-matched subsets, with the
Robustness Index as the imported baseline metric; the paper is the *correlation* (does site
decodability predict transfer rank across families?) and the natural-vs-medical contrast, not the
audit itself.

**VERDICT: MUTATE.** Mutated claim: "site-invariance as a cross-family pretraining differentiator
that *predicts* cross-site transfer — extending the pathology Robustness Index audit to the
natural-vs-medical contrast across modalities."

---

## W2-B-0042 (mutated) — The synonym-variance ledger for OVS

**REJECTION.** This micro-literature completed its life cycle without you: RENOVATE
(NeurIPS 2024, arXiv 2403.09593) showed benchmark names are imprecise and fixed them; Open-metric
work (arXiv 2311.03352) rebuilt scoring to stop punishing synonyms; and SynCLIP (CVPR 2026) now
runs explicit "synonym-robustness evaluation under synonym substitution" across models AND trains
the sensitivity away with synonym-coherent pretraining. Phenomenon documented, metric reformed,
fix shipped. The ledger's one residual number — is synonym-induced ranking variance larger than
published between-model deltas? — is a meta-analytic figure computable from existing sensitivity
tables, and its punchline lands on a field that has already conceded the point and moved to
mitigation. E demoted this to bet #20; I am closing it.

**Hidden assumptions:** (1) extension-matched synonym sets are constructible at scale (sofa/couch
regional-extension problem — the authors' own risk note); (2) "model-generation variance" is a
stable comparator (release deltas vary wildly by pair); (3) anyone will change practice based on a
ledger when SynCLIP-style training and open metrics already exist as responses.

**Fresh prior-work hits:**
- SynCLIP (CVPR 2026) — https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_SynCLIP_Synonym-Coherent_Language-Image_Pretraining_for_Robust_Open-Vocabulary_Dense_Perception_CVPR_2026_paper.pdf
- RENOVATE (NeurIPS 2024) — https://arxiv.org/abs/2403.09593
- Rethinking Evaluation Metrics of Open-Vocabulary Segmentation — https://arxiv.org/abs/2311.03352

**Killer experiment:** NONE as a standalone. The only useful remnant — name choice as one axis of
protocol variance — belongs inside 0213's multi-axis protocol audit.

**VERDICT: KILL (freshness).** Mutated claim: none standalone; fold the name axis into 0213.

---

# PART 3 — Fragile protected keeps

## W2-B-0025 — Emergent attention segmentation is epiphenomenal (DP-protected)

**REJECTION.** This proposal re-imports the "attention is not explanation" debate (Jain & Wallace
2019 and its rebuttals [not re-verified]) into vision with the same unresolved construct problem
that made that debate end in stalemate: attention maps are not a readout *about* the computation,
they ARE the computation's mixing weights, so "intervene while preserving distributional
statistics" is close to incoherent — any intervention that destroys object alignment changes the
function, and any that doesn't hasn't destroyed it. Every outcome has a prepared deflation: outputs
unchanged → "your intervention was too weak / off-manifold compensation"; outputs changed → "you
broke the network, of course outputs changed." The claim "epiphenomenal" is not operationalized,
and no matched-statistics control can operationalize it, because there is no agreed null model for
what a "non-segmenting but otherwise equivalent" attention pattern is. DP protection says either
outcome splits the community; I claim the community splits over the *method*, not the finding, and
methodological splits do not move fields — they spawn rebuttal chains.

**Hidden assumptions:** (1) a meaningful null family of attention patterns exists; (2) head-level
interventions compose linearly enough to attribute; (3) "the model uses its attention maps" is a
hypothesis distinct from "the model computes with attention" — it isn't, as stated.

**Killer experiment:** NONE that silences the construct objection. (The nearest defensible cousin —
ablate/reroute specific heads and measure dense-task deltas — is standard interpretability practice
and does not test "epiphenomenality.")

**VERDICT: KILL.**

---

## W2-B-0033 — Pretraining seed variance vs published VFM gaps (DP-protected)

**REJECTION.** The inferential structure is broken by design: you can afford multi-seed pretraining
only at ViT-S/ImageNet-100 scale, but the claims you want to indict live at ViT-L/LVD-142M scale —
and variance does not extrapolate across 3 orders of magnitude of data and compute (your own risk
note). At feasible scale the paper proves "seed variance exists in small-scale SSL," which the
variance-accounting literature already established generically (Bouthillier et al., *Accounting for
Variance in ML Benchmarks*, MLSys 2021 [not re-verified]; Picard's seed study [not re-verified]).
The field-reform conclusion ("published 1–2 point gaps may be noise") is precisely the part your
budget cannot license: flagship labs will correctly reply that their scale suppresses seed noise
via data size and averaging, and you will have no counter-evidence. A methods-reform paper whose
central extrapolation is unfundable is not insurance; it is a liability that consumes a year of
compute to produce a shrug.

**Hidden assumptions:** (1) small-scale variance bounds flagship-scale variance (no theory or data
supports this in either direction); (2) frozen-probe mIoU variance is the right target rather than
downstream fine-tuned variance; (3) anyone changes behavior absent flagship-scale evidence.

**Killer experiment:** NONE affordable. The decisive experiment is 5-seed pretraining of a
flagship-scale model — a compute-partner fantasy that, per E's own criteria for 0293, converts to a
kill when the partner does not exist.

**VERDICT: KILL.**

---

## W2-B-0092 — Inverse stability scaling with model size (CI-protected)

**REJECTION.** Your "law" is most plausibly a measurement of how wrong standard LR heuristics are at
scale, not an intrinsic property: instability at fixed LR grids across model sizes is exactly what
µP/µTransfer-style parameterization theory predicts and *fixes* [not re-verified] — under corrected
parameterization the exponent may vanish, making the paper an advertisement for a known fix. The CI
protection ("probably wrong but cheap to check") underprices the interpretive trap: if you find
inverse scaling under default heuristics, reviewers say "wrong parameterization"; if you correct
parameterization and the effect vanishes, you have re-derived µP; only the narrow middle — inverse
scaling *surviving per-scale LR optimization* — is a finding, and priors say it won't.

**Hidden assumptions:** (1) "instability" (seed variance, spike rate) is comparable across scales at
their respective optima; (2) 3–4 points identify a power law (they don't; they bound a trend);
(3) fixed 5k-image tasks are the deployment-relevant regime for ViT-H.

**Killer experiment (the only version worth running):** ViT-S/B/L ladder, per-scale LR *optimized*
(grid to the variance-minimizing LR at matched final accuracy), 10 seeds; report variance and spike
rate at optimum vs scale, under both standard and µP parameterizations. If instability grows at
optimum under both, publish; anything less is a hyperparameter artifact.

**VERDICT: SURVIVE-IF-EXPERIMENT** (with the per-scale-optimum control mandatory; expected outcome
is a null, priced accordingly).

---

## W2-B-0133 — LoRA memorizes more per-parameter (CI-protected privacy inversion)

**REJECTION.** The 2025–2026 record answers you, in the wrong direction and at scale.
A high-precision MIA study (arXiv 2601.12104) provides "the first quantification of the privacy gap
between full fine-tuning and LoRA": full FT 0.993 AUC / 82.6% TPR@1%FPR vs LoRA 0.553 AUC / 1.5% —
a 55× detection-rate reduction. Federated-learning experiments (arXiv 2502.05087) find LoRA cuts
verbatim memorization up to 10× across 1B–70B models, medicine/law/finance domains. Rank studies
(arXiv 2507.21009) show memorization *rises* with rank — i.e., with trainable parameters — the
opposite of your per-parameter inversion. LoRA-Leak (arXiv 2507.18302) shows LoRA models remain
attackable, but nowhere near parity with full FT. Your escape hatch — "per-trainable-parameter"
normalization — is rhetorical: privacy risk is a property of the deployed artifact, not a ratio;
dividing a smaller absolute leakage by a much smaller denominator to declare an "inversion" is the
kind of metric engineering reviewers exist to catch. The vision/few-shot domain swap has no stated
mechanism for sign reversal. E's own protection was conditional on a pre-execution literature
re-check; the re-check just failed.

**Hidden assumptions:** (1) per-parameter normalization is decision-relevant to anyone (it is not);
(2) few-shot vision inverts a sign that is consistent across models, domains, and attack families
in text; (3) "concentration in the adapter subspace" implies higher extractability rather than
easier *defense* (adapter can be audited/noised in isolation).

**Fresh prior-work hits:**
- Powerful Training-Free Membership Inference (full-FT vs LoRA gap quantified) — https://arxiv.org/html/2601.12104v1
- Mitigating Unintended Memorization with LoRA in FL — https://arxiv.org/abs/2502.05087
- Memorization in Fine-Tuned LLMs (rank → memorization) — https://arxiv.org/pdf/2507.21009
- LoRA-Leak — https://arxiv.org/pdf/2507.18302
- Window-based MIAs against fine-tuned LLMs — https://arxiv.org/pdf/2601.02751

**Killer experiment:** NONE that rescues the inversion headline. (An honest "MIA on PEFT for dense
vision models" benchmark is a fine engineering paper for someone else; it is not this claim.)

**VERDICT: KILL (freshness).**

---

## W2-B-0252 — Interpolation-frontier kinks as mechanism transitions (HRHR-protected)

**REJECTION.** Three independent literatures predict your null or defeat your inference. First,
Neyshabur et al., *What is Being Transferred in Transfer Learning?* (2020 [not re-verified]), found
models fine-tuned from shared pretrained initializations are connected by essentially flat,
barrier-free paths — the smoothness you must overturn. Second, the published WiSE-FT interpolation
curves are famously smooth and concave; nobody has reported kinks in five years of people staring
at exactly these plots, which is weak evidence of absence but strong evidence about effect size.
Third, even if you detect statistically reproducible kinks, the inference "kink ⇒ discrete
mechanism transition" is unlicensed: thresholded metrics (mIoU, accuracy) manufacture kinks from
smooth underlying score changes; changepoint detection on noisy 1-D curves with multiple
tasks × coefficients is a garden of forking paths; and per-layer interpolation (your sharpening
trick) breaks the function-space interpretation entirely. HRHR protection bought a lottery ticket;
the lottery has a published history of not paying out, and the prize (mechanistic conclusion) is
unclaimable even on a win.

**Hidden assumptions:** (1) smooth metrics would show the kinks too (must use soft losses, not
accuracy); (2) kink locations are seed-stable; (3) any mapping from frontier geometry to "mechanism"
exists beyond correlation with an ability battery, itself thresholded.

**Killer experiment:** NONE that secures the mechanistic claim. (Seed-stable kinks in soft losses
would be a curiosity note, not the promised payoff.)

**VERDICT: KILL.**

---

## W2-B-0264 — Synthetic medical data launders privacy (HRHR-protected)

**REJECTION.** The pipeline you propose to expose has been exposed at both ends. Generator end: Dar
et al. (arXiv 2402.01054; Nature BME 2025) show unconditional latent diffusion models memorize
patient data at startling rates (~40.9% of patient data memorized; ~78.5% of synthetic samples are
near-copies in their settings) — synthetic medical images carrying real-patient signal is
established, not hypothetical. Downstream end: the transitive attack — MIA against a model trained
*only on synthetic data*, targeting the generator's training members — was mounted for clinical
notes in Scientific Reports 2024 (*De-identification is not enough*), which "proposed a way to
mount a membership inference attack where the target model is trained with synthetic data" and
found synthetic data inherits real-data privacy concerns. Medical-diffusion MIA methodology is its
own subfield now (e.g., DEB, MDPI 2026). Your residual is the imaging/dense instantiation plus a
leakage-vs-generation-volume curve — a quantification exercise on a demonstrated phenomenon, in a
regulatory conversation that has already moved to mitigation (privacy-filtered generation, TMI
2025). "Field-defining if positive" was the HRHR bet; the field defined itself while the bet was on
the table.

**Hidden assumptions:** (1) segmentation-model MIA is sensitive enough to detect second-hand
membership signal (dense MIAs are weaker than classification MIAs); (2) the effect survives
standard dedup/privacy filtering that generator vendors now apply; (3) IRB-compatible datasets with
known generator-membership ground truth are accessible.

**Fresh prior-work hits:**
- Unconditional LDMs Memorize Patient Imaging Data — https://arxiv.org/abs/2402.01054
- De-identification is not enough (transitive MIA via synthetic training data) — https://www.nature.com/articles/s41598-024-81170-y
- Privacy-Preserving Latent Diffusion (TMI 2025, mitigation) — https://doi.org/10.1109/tmi.2025.3618511
- DEB: MIA risks in medical diffusion models — https://www.mdpi.com/2076-3417/16/7/3140

**Killer experiment:** controlled generator training on known patient splits; downstream
*segmentation* models adapted on synthetic-only data; strong MIAs targeting generator-set
membership; leakage as a function of generation volume and of privacy-filter strength — with
filter-defeat (or filter-vindication) as the headline. Feasible; the filter interaction is the only
angle mitigation papers haven't quantified.

**VERDICT: MUTATE.** Mutated claim: "does privacy filtering actually close the transitive
membership channel in dense medical adaptation, and at what utility cost — a red-team audit of the
mitigation stack," not a discovery of the channel.

---

## W2-B-0278 — Spectral coverage criterion predicts sign of synthetic-data effect (HRHR)

**REJECTION.** The claim as written is unfalsifiable armor-plating: "helps *when and only when* it
populates undersampled eigendirections" — an iff over all generators, tasks, and training recipes,
measured in an unspecified feature space. The criterion is circular (coverage is computed in some
encoder's geometry; the choice of encoder is a free parameter that can be tuned post hoc until the
criterion "predicts"), and it competes against brutally cheap baselines nobody mentions: real-data
set size, FID/precision-recall of the generator, simple class-frequency accounting. The conflicting
literature it promises to reconcile is conflicting for boring reasons (generator quality, prompt
distribution, filtering) that a single geometric scalar will not absorb. HRHR protection is for
ideas with paradigm payoff; this has paradigm *packaging* around what will, in practice, decay into
"coverage correlates with gains sometimes, ρ≈0.4."

**Hidden assumptions:** (1) an encoder-invariant notion of "undersampled directions" exists;
(2) linear eigendirections capture the relevant coverage (why not local density or topology?);
(3) sign of effect is stable across training recipes for fixed data (it is not — augmentation and
LR change signs).

**Killer experiment:** pre-registered sign-prediction contest: ≥20 (task, generator, mixing-ratio)
configurations; criterion computed *before* training in 3 different reference encoders; compared
against FID, generator recall, and data-size baselines; success = beating all baselines with
encoder-robust predictions. Bounded (each configuration is a small adaptation run), and the
pre-registration is what makes a positive result credible.

**VERDICT: MUTATE.** Mutated claim: drop the iff; "a pre-registered comparison of coverage-geometry
predictors vs cheap baselines for the sign of synthetic-data effects." Keep only if the PI wants
one theory-flavored bet in the synthetic cluster; 0263's mutated form is cheaper and sturdier.

---

## W2-B-0305 — Whorfian imprint of English spatial categories (HRHR-protected)

**REJECTION.** The behavioral core is published: COMFORT (arXiv 2410.17385) evaluated nine VLMs
across 109 languages on spatial frame-of-reference tasks and found exactly the English-dominance
imprint you hypothesize — models "fail to adhere to language-specific or culture-specific
conventions in cross-lingual tests, as English tends to dominate other languages." Encoder-side,
language-dependent geometric shifts in multilingual VLE embedding spaces are documented
(arXiv 2509.23098), and multilingual dense-CLIP grounding gaps are quantified across 13 languages
(arXiv 2605.09060). Your remaining novelty — feature-level *transmission* (English-lexicalized
contrasts more linearly separable in the visual encoder; multilingual variants shifting toward
their mixture's ontology) — sits behind the confound you yourself flag: caption-language composition
co-varies with image distribution, region, and data source, and "caption-translated controls"
require retraining runs that turn a probe study into a pretraining program. The paradigm-level
payoff HRHR paid for has been partially banked by COMFORT at the behavior level; what's left is a
representational footnote guarded by a confound.

**Hidden assumptions:** (1) translation-based multilingual probes preserve the spatial semantics
being tested (translation is itself Anglocentric for FoR distinctions); (2) public "multilingual
CLIP variants" differ mainly in caption language rather than in everything else; (3) linear
separability of spatial contrasts in frozen features is the right transmission measure.

**Fresh prior-work hits:**
- COMFORT: spatial frame-of-reference under ambiguity, 109 languages — https://arxiv.org/abs/2410.17385
- Blind to Position, Biased in Language (language-dependent VLE geometry) — https://www.alphaxiv.org/abs/2509.23098 (arXiv 2509.23098)
- Language-Conditioned Visual Grounding with CLIP Multilingual — https://arxiv.org/html/2605.09060v1

**Killer experiment:** small-scale matched-pretraining pairs on the *same images* with
machine-translated caption sets (EN vs EN+X mixtures), probing separability of spatial contrasts
that language X splits and English merges; the caption-translation control is the only design that
cuts the data-composition confound, and it must be run at small scale first to justify anything
larger.

**VERDICT: MUTATE.** Mutated claim: "caption-language composition causally shifts visual spatial-
relation geometry at matched images" — a controlled small-scale transmission study, explicitly
downstream of COMFORT's behavioral result. HRHR status no longer justified; reprice as a mid-cost
mechanism study.

---

## W2-B-0317 — MIL identifiability predicts which concepts can never emerge densely (HRHR)

**REJECTION.** Two structural objections. First, the modeling premise — caption supervision IS
multiple-instance learning — is a contestable analogy, not a theorem: CLIP's InfoNCE over
continuous embeddings with soft cross-image negatives is not bag-label MIL, and instance-level
identifiability results (the toolkit you'd import — e.g., NeurIPS 2024's PAC framework for
instance-level MIL learnability) carry assumptions (instance independence, bag-label determinism)
that captions violate flagrantly. A reviewer lets you have the analogy for intuition and then
rejects every theorem-shaped claim built on it. Second, the empirical program is confounded at its
core: concepts that "never appear isolated" in corpora are also visually context-bound, rare, and
hard — corpus co-occurrence correlates with visual difficulty, so identifiability scores will
predict dense failure through boring covariates unless you control for SSL-model dense quality per
concept, which drags the whole 0323 apparatus in as a dependency. The "regardless of scale" clause
is untestable without scale ladders you don't have.

**Hidden assumptions:** (1) the MIL reduction preserves what matters about contrastive caption
training; (2) corpus statistics of open web data approximate the actual (filtered, deduplicated)
training distribution; (3) identifiability-violating concepts exist in enough abundance to power
the test; (4) SSL normalization removes visual-difficulty confounds.

**Fresh prior-work hits:**
- Are Multiple Instance Learning Algorithms Learnable for Instances? (NeurIPS 2024) — https://proceedings.neurips.cc/paper_files/paper/2024/file/1468ecc3d7e9dc2fbf336eed9bb292e0-Paper-Conference.pdf
- FocusMIL (causal max-pooling MIL analysis) — https://arxiv.org/abs/2408.09449
- (No work found applying MIL identifiability to caption-supervised dense emergence — the specific program remains unclaimed.)

**Killer experiment:** on models with released training data (LAION-trained OpenCLIP): compute
co-occurrence-based identifiability scores per concept; measure per-concept dense emergence;
regress emergence on identifiability *with SSL-decodability and frequency as covariates*. The
theory survives only if identifiability adds predictive power over frequency + difficulty. This is
affordable and decisive for the empirical half; the theory half still needs the collaborator E
flagged.

**VERDICT: SURVIVE-IF-EXPERIMENT** (empirical program only, with covariate controls; theorem-level
claims dropped until the MIL reduction is formally defended).

---

# Cross-cutting notes from this attack round

1. **E's "dynamics/causal upgrade" monoculture failed correlated, as E predicted.** Of the five
   survivors E built on "statics are published, dynamics/causal are open" (0074, 0145, 0163→,
   0307, 0323), this round found the dynamics/causal versions partially published for 0074
   (MG-CLIP/GNSP), 0307 (matched-pretraining contrast), and 0323 (caption-intervention retraining).
   The heuristic's shelf life in this field is ~12 months.
2. **Cheap-to-falsify cuts both ways.** CF protection favored ideas anyone can run in a week —
   which is exactly why three of them (0332, 0133, 0042) were run, in effect, by someone else
   before this program started executing.
3. **Every surviving idea now carries a named control that was absent from its Stage-1 form**
   (randomized dose for 0194, placebo/injection arms for 0268, supervised-classifier arm for 0304,
   attention-bias arm for 0114, temperature arm for 0145, per-scale-LR-optimum for 0092,
   all-matchings audit for 0213). Stage-5 should treat these controls as non-negotiable parts of
   any execution plan, not reviewer-appeasement garnish.
