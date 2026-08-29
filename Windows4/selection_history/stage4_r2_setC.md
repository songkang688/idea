# Stage 4 — Reviewer #2, Set C (8 targets)

Date: 2026-08-28. Role: **Reviewer #2**. Stance per rubric: **default REJECT**; a target survives
iff a *realistic* experiment (one lab, no new foundation-model pretrain, pre-registered kill
conditions) would silence the strongest attack I can mount.

Inputs: `stage3_top50.md`, `stage3_kill_medical_smoke.md`, `stage3_kill_peft_vlm.md`
(and `stage3_kill_sam_eval.md` for schema/cross-references).

Epistemic status: **REVIEW JUDGMENT.** Citation discipline follows the Stage-3 convention:
`[V]` = fetched and read (abstract or full text) during this pass, 2026-08-28;
`[S3]` = carried from a Stage-3 file that claimed web verification;
`[M]` = memory-cited classic — re-verify the ID before quoting in any draft.
No fabricated papers. Where my attack rests on a paper found *this pass* that Stage 3 missed,
it is flagged **NEW EVIDENCE** and logged in the register at the end.

Schema per target: Paper under review (as it would be submitted after the Stage-3 mutation) →
R2 attack (strongest rejection, numbered vectors) → The silencing experiment (design, controls,
pre-registered kill conditions, cost) → What no experiment can fix → Verdict → Confidence.

Verdict scale: **SILENCED** (attack answered by the specified experiment; survive),
**SILENCED-IF-MUTATED** (survives only in the modified form specified; modification binding),
**REJECT** (attack cannot be answered by any realistic experiment).

## Scoreboard

| Target | Verdict |
|---|---|
| P096 (S-096+S-102) | SILENCED (with measured-alpha arm mandatory) |
| P040 (A1-040) | SILENCED-IF-MUTATED (prediction paper, not curve paper) |
| P042 (S-042) | SILENCED (decimation design mandatory) |
| P107v (B1-107) | **REJECT as constituted** → narrow mutation permitted, flagship status revoked |
| P079f (B1-079) | SILENCED (four controls mandatory) |
| P051 (B1-051) | SILENCED-IF-MUTATED (amortization-parameterized frontier, efficient generators) |
| P228 (S-228) | SILENCED-IF-MUTATED (within-model causal design on BiomedParse-class target) |
| P061u (B1-061→B1-069) | SILENCED-IF-MUTATED (interaction-focused factorial; fold confirmed) |

Net: 3 silenced with binding controls, 4 silenced only under specified mutations, 1 rejected
as constituted (Stage-3 SURVIVE overturned on new evidence).

---

## 1. P096 — S-096 + S-102: "Smoke evaluation is broken" (metric reversal + rater ceiling)

**Paper under review.** Two-pillar evaluation paper per the Stage-3 merge: (1) re-score 8–10
published smoke segmenters under {IoU, Dice, Fβ} vs {alpha-MAE, SAD, gradient error} on
alpha-GT data and report rank reversal (Kendall τ); (2) measure multi-rater IoU/alpha ceilings
on standard RGB benchmarks (SSD/SMOKE5K/DS0x-real) and confront published SOTA deltas.

**R2 attack.**

1. **Strawman on the field's metrics (F8).** The SMOKE5K protocol *already* reports mMse
   alongside Fβ — FoSp (AAAI 2024, doi:10.1609/aaai.v38i7.28484 `[V]` **NEW EVIDENCE**) follows
   Yan et al. AAAI 2022 in using mMse + Fβ on SMOKE5K and mIoU only on SYN70K; the new
   AusSmoke/MultiNatSmoke benchmark (arXiv:2604.23542 `[V]` **NEW EVIDENCE**) reports IoU, F1,
   *and* MSE. "The field ranks by binary overlap alone" is false as stated; a reviewer pastes
   FoSp's metrics table and asks what reversal remains once mMse is in the leaderboard.
2. **The matting turn already happened.** SFMattingNet (Remote Sensing 17(13):2259, 2025,
   doi:10.3390/rs17132259 `[V]` **NEW EVIDENCE**) is trimap-free *smoke-and-fire matting* with
   SAD/MSE/Grad/Conn — the field is already migrating to alpha metrics without waiting for a
   validity study. "You are confirming a direction already taken."
3. **Alpha-GT circularity (the strongest vector).** Alpha ground truth exists only where smoke
   was synthetically composited (DS01–03) or subjectively annotated. A reversal demonstrated on
   synthetic composites shows that models trained/ranked on real binary masks disagree with
   synthetic alpha — which may indict the *synthetic data*, not the metric. On real smoke,
   "true alpha" is unobservable; the paper's gold standard is unfalsifiable exactly where the
   claim matters.
4. **Ceiling half is second.** Inter-annotator smoke disagreement is measured (hyperspectral,
   3 raters, arXiv:2602.10858 `[S3]`); CoSW (NeurIPS 2024 `[S3]`) treats smoke label noise as
   established. The ceiling pillar is a confrontation table, not a discovery.

**The silencing experiment.**

- *Against 1:* include mMse-on-binary-GT as its own column in the τ matrix. The claim becomes
  sharper, not weaker: show whether mMse against *binary* GT rank-correlates with alpha-MAE
  against *alpha* GT. If it does (τ > 0.8), the field's existing metric already proxies alpha
  error and pillar 1 dies — pre-registered kill condition. If it does not, FoSp's table is the
  paper's motivation, not its refutation.
- *Against 3 (mandatory arm):* build a **measured-alpha real test set** — no annotation, no
  synthesis. Fixed-camera smoke sequences with clean pre-smoke background frames (FIgLib-style
  towers `[S3: Dewangan et al. 2022]`, plus lab captures with locked exposure) permit
  physics-based alpha recovery by compositing inversion against the known background. Controls:
  exposure-locked sequences only; exclude saturated/backlit frames; report sensitivity of
  recovered alpha to the single-scattering assumption via lab smoke against calibrated
  backgrounds. Rank the same checkpoints on (a) synthetic alpha, (b) measured real alpha,
  (c) binary GT. The reversal claim survives only if (a) and (b) agree against (c).
- *Against 2:* score SFMattingNet inside the same pool; frame the paper as the validity audit
  the matting turn skipped — no published evidence yet shows binary leaderboards *mis-rank*;
  this experiment supplies or refutes it.
- *Against 4:* run the ceiling as pillar-2 exactly as Stage 3 specified (3–5 raters × 150
  images from SSD/SMOKE5K test sets, pairwise IoU and alpha-MAE ceilings, overlay published
  deltas), with the pre-registered demotion: if ceilings exceed 0.85 IoU, drop the pillar to
  an appendix.

Cost: eval-only on ~10 checkpoints + ~300 rater-annotated images + one fixed-camera capture
campaign. No training. Feasible within the rubric's ROI rules.

**What no experiment can fix.** Nothing structural. The paper's ceiling is venue-level: it is
an evaluation-science paper for a small field, and its headline is hostage to the τ matrix.

**Verdict: SILENCED** — with the measured-alpha real arm and the mMse column **binding**.
Without the measured-alpha arm, attack 3 stands and the verdict flips to REJECT.
**Confidence:** medium-high.

---

## 2. P040 — A1-040: Boundary-diffuseness under-segmentation law

**Paper under review.** Synthetic lesions with parameterized edge-gradient width inserted into
real CT/MR backgrounds; plot *signed* boundary error vs width for SAM/SAM2/MedSAM; validate the
fitted law's out-of-sample prediction on LiTS infiltrative-vs-circumscribed subgroups.

**R2 attack.**

1. **"Quantified lore" (the core objection).** He et al. (arXiv:2304.09324 `[S3]`) already fit
   a GLM showing contrast and size are the dominant predictors of SAM Dice; Mazurowski et al.
   (MedIA 2023 `[S3]`) documents poor performance on fuzzy boundaries. A monotone
   error-vs-blur curve is a re-parameterization of the known contrast dependence. Where is the
   *law* — i.e., what does it predict that the GLM does not?
2. **Diffuseness–contrast collinearity.** Widening a gradient profile at fixed peak intensity
   lowers local contrast. Unless the sweep manipulates edge width at *matched* Michelson
   contrast (and matched size), the "diffuseness law" is the contrast curve wearing a new axis.
3. **Insertion-artifact validity.** Parametric Gaussian-profile lesions are off-manifold;
   biophysically-conditioned tumor synthesis with continuous infiltration fields now exists
   (arXiv:2510.09365 `[V]` **NEW EVIDENCE**) and sets the realism bar. A reviewer asks why the
   model's response to toy composites should transfer to real infiltration.
4. **Circular validation.** Measuring "diffuseness" of real LiTS lesions uses image gradients
   around the GT boundary — the same boundary the error is scored against; and
   infiltrative-vs-circumscribed subgrouping is itself an annotation judgment.

**The silencing experiment.**

- *Against 1+2 (the discriminating design):* a **two-factor sweep** — edge-gradient width ×
  Michelson contrast, manipulated orthogonally at matched lesion size. Two mechanisms make
  different predictions: a *snap-to-edge* prior predicts signed under-segmentation growing with
  gradient width even at high contrast (mask contracts to the steepest gradient ring); a
  *contrast-threshold* account predicts error tracking contrast at any width. The experiment
  discriminates them. That is a law with content, not a curve: it predicts *where* the boundary
  lands (the isophote of steepest gradient), checkable per-case. Pre-registered kill: if signed
  error is flat in width at matched contrast, the diffuseness law is dead and the result folds
  into the known contrast story.
- *Against 3:* two synthesis arms — (a) parametric profiles, (b) biophysical-concentration
  lesions from the arXiv:2510.09365 class of generator with the concentration field's decay
  length as the diffuseness parameter; plus a sham-insertion control (circumscribed profile
  through the identical compositing pipeline) to price the insertion artifact itself. The law
  must agree across (a) and (b).
- *Against 4:* on real data, compute the diffuseness proxy in a fixed annulus *straddling* the
  GT boundary (GT used only to locate the annulus, not to score sharpness), and pre-register the
  synthetic-fitted law's prediction of signed error on real subgroups *before* scoring. Report
  prediction R², not just correlation.

Cost: inference-only on frozen models + one generator fine-tune already published; ≈ GPU-days,
not weeks.

**What no experiment can fix.** If the two-factor sweep shows width effects are fully absorbed
by contrast, no framing rescues a standalone paper — that outcome is one figure inside the
medical-eval thread. The submission must be built so that this demotion path is explicit.

**Verdict: SILENCED-IF-MUTATED** — from "fit a curve" to "discriminate snap-to-edge vs
contrast-threshold mechanisms and predict real-lesion signed error out-of-sample." The
mechanism-discrimination framing and the two-factor design are binding; without them attack 1
stands. **Confidence:** medium.

---

## 3. P042 — S-042: Anisotropy confound vs "medical 3D"

**Paper under review.** Hold data fixed; measure zero-shot SAM2 propagation Dice as a controlled
function of slice spacing; report the fraction of the "medical gap" (vs MedSAM-2/fine-tuned
SAM2) closed by resampling alone; Dice-vs-anisotropy-ratio curve across datasets.

**R2 attack.**

1. **Hygiene-as-paper.** nnU-Net (Isensee et al., Nature Methods 2021 `[S3]`) made
   spacing-aware resampling doctrine; every serious pipeline resamples. "Resampling helps" is
   not news at any venue.
2. **The intervention is confounded three ways.** Resampling z changes (a) the number of
   slices, hence the number of propagation steps, hence accumulated drift (Dong et al.
   arXiv:2408.00756 `[S3]` showed error grows with slice distance); (b) interpolation blur on
   the invented slices; (c) apparent inter-slice motion magnitude. "Anisotropy" as a causal
   variable is a bundle; the headline "X% of the gap is anisotropy" inherits all three.
3. **"Fraction of the gap" is ill-posed.** The number depends on the fine-tuned comparator,
   its checkpoint, the prompt protocol, and the dataset mix; a hostile reviewer constructs a
   comparator that moves the fraction from 20% to 70%.
4. **Scoop probe.** Checked this pass: the zero-shot SAM2-CT ablation study
   (arXiv:2603.23116 `[V]`) sweeps prompts, memory selection, propagation schemes, and
   multi-axis fusion on TotalSegmentator — **no spacing/resampling arm** (verified by full-text
   inspection). SAM2-ProMem (MICCAI 2025 `[V]` **NEW EVIDENCE**) manipulates memory, not
   spacing. The gap Stage 3 claimed is still open as of today.

**The silencing experiment.**

- *Against 2 (the design that decides the paper):* **decimate, don't interpolate.** Start from
  near-isotropic CT (sub-mm to 1.5 mm z-spacing subsets of TotalSegmentator/AMOS); create
  {1.5, 3, 6} mm variants by *dropping slices* — no invented data, acquisition and in-plane
  appearance held fixed, anisotropy manipulated causally. Report drift both per-step and per-mm:
  if Dice falls per-mm at *fewer* propagation steps, error accumulation is exonerated and
  anisotropy (inter-slice appearance jump) is isolated. Then, and only then, add the
  interpolated-upsampling arm on natively-thick volumes to measure how much of the loss
  interpolation recovers — now interpretable because the causal direction was established on
  decimated data.
- *Against 1:* the claim is not "resampling helps" but an *attribution with a named adversary*:
  MedSAM-2's motivation (arXiv:2408.00874 `[S3]`) attributes the 3D failure to medicalness
  (slice order meaninglessness); if a large fraction of the zero-shot gap closes by spacing
  manipulation alone, the fine-tune literature's premise is partially an acquisition artifact.
  State this as the falsifiable stake in the introduction.
- *Against 3:* pre-register comparators (public MedSAM-2 checkpoint + one reproduced fine-tuned
  SAM2), one fixed prompt protocol (middle-slice box, bidirectional, per arXiv:2408.03322
  `[S3]`), and report the closed-fraction as a *range across datasets with CIs*, never a single
  number. Publish the per-dataset anisotropy-ratio curve as the primary object; the fraction is
  secondary.

Kill condition (carried from Stage 3, still correct): dies if spacing manipulation moves Dice
<30% as much as fine-tuning everywhere. Cost: inference-only; days.

**What no experiment can fix.** Nothing structural; the result is informative in both
directions. Residual risk is a benchmark-appendix scoop, mitigated but not eliminated by the
two probes run this pass.

**Verdict: SILENCED** — decimation design and pre-registered comparators binding.
**Confidence:** medium-high.

---

## 4. P107v — B1-107: Phantom dense masks after inpainting-out (VLM hallucination)

**Paper under review.** Stage-3 SURVIVE, slotted as flagship P5 (with S-228): inpaint the object
out; text-prompted segmenters still fire; co-occurrence-driven phantom masks at the pixel level;
trace-controls (sham surgery) for inpainting artifacts.

**R2 attack.**

1. **Scooped. NEW EVIDENCE overturning Stage 3's NOT FOUND.** *HalluSegBench* /
   Counterfactual Segmentation Reasoning (Li et al., arXiv:2506.21546 `[V]`; dataset public on
   HuggingFace, PLAN-Lab) is "the first large-scale benchmark to diagnose referring and
   reasoning expression segmentation hallucinations using controlled visual counterfactuals":
   3,673 factual–counterfactual pairs across 816 categories, ΔIoU_textual vs ΔIoU_visual to
   disentangle language- vs vision-driven failures, a Confusion Mask Score for structured
   phantom masks, evaluation of LISA/PixelLM/Seg-Zero/SESAME-class models, *and* a
   counterfactual-fine-tuned fix (RobustSeg, −30% hallucination). Their headline finding is
   B1-107's thesis: vision-driven hallucinations dominate, models "often persisting in false
   segmentation." The same paper cites *Visual Jenga* (Bhattad, Preechakul & Efros, NeurIPS
   2025 `[V via 2506.21546 refs]`) — counterfactual *inpainting* is an established instrument.
   Stage 3's "no dense-prediction counterfactual-inpainting audit found" is stale. No
   experiment silences a scoop; the "first dense counterfactual audit" framing is dead, and
   with it the flagship slot.
2. **The residue is at artifact risk.** HalluSegBench's edits are *replacements* (target
   swapped for a similar object), not removals — but any removal-based follow-up faces the
   inpainting-trace confound with a published, artifact-lighter alternative sitting next to it.
3. **Fix already shipped.** RobustSeg means the phenomenon has a mitigation baseline; an
   audit-only paper now competes with a method+benchmark package.

**The residual (what HalluSegBench verifiably does not do).**

- *Removal, not replacement:* their counterfactual scene still contains a plausible distractor
  object; ΔIoU_visual conflates "confuses a similar object" with "hallucinates from context
  alone." Object-out counterfactuals isolate the pure co-occurrence prior — scene context with
  *nothing* at the location.
- *No sham-surgery artifact control* is claimed in their pipeline; the trace-control arm
  (re-inpaint regions *not* containing the target; identical artifact statistics, no removal)
  remains unclaimed.
- *Model classes:* they cover reasoning-seg VLMs; open-vocabulary detector+SAM pipelines
  (Grounding-DINO+SAM class) and text-prompted *medical* segmentation (BiomedParse,
  arXiv:2405.12971 `[V]` — which ships a K-S-test abstention mechanism, i.e., a model that
  *claims* to know when the object is absent) are untested.
- *Dose–response attribution:* phantom-mask rate as a function of pretraining co-occurrence
  strength (POPE-style stratification `[S3: arXiv:2305.10355]`) at the pixel level — mechanism,
  not existence.

**Verdict: REJECT as constituted.** The Stage-3 SURVIVE and the P5 flagship slot are revoked on
verified new evidence. A narrow mutation may re-enter the pool as a junior-scope companion to
P228: "context-only phantom masks: what replacement counterfactuals miss" — removal-based,
sham-surgery-controlled, co-occurrence dose–response, evaluated on detector+SAM pipelines and
BiomedParse's abstention (does the K-S test actually fire on inpainted-out anatomy?). It must
adopt HalluSegBench's metrics (ΔIoU_visual, CMS) and report on their benchmark for
comparability. It is a delta paper now; budget accordingly. **Confidence:** high (scoop
verified full-text this pass).

---

## 5. P079f — B1-079: FSS background-swap cheat

**Paper under review.** Audit claiming FSS episodes reward support/query *background similarity*
— an episode-construction shortcut orthogonal to BAM's base-class bias; background-swap
intervention quantifies the shortcut's contribution to benchmark scores.

**R2 attack.**

1. **The phenomenon is named and methodized. NEW EVIDENCE.** Zhu et al., *Addressing Background
   Context Bias in Few-Shot Segmentation through Iterative Modulation*, CVPR 2024
   (doi:10.1109/cvpr52733.2024.00324 `[V]`): "different background contexts of support and
   query images can cause their foreground features to be misaligned. This phenomenon, known as
   background context bias…" — plus a fix. TBS, AAAI 2024 (doi:10.1609/aaai.v38i5.28242 `[V]`)
   builds a module around exactly the two failure cases (dissimilar backgrounds; target-similar
   support background). A reviewer pastes these and writes: "the 'shortcut' you reveal is the
   motivation section of two 2024 method papers."
2. **Compositing-artifact confound.** Swapped episodes are off-manifold (matting halos,
   lighting mismatch); measured degradation over-estimates the shortcut. The sham-swap control
   (recomposite same background) does not equate foreground-background lighting coherence in
   the *swapped* arm.
3. **BAM overlap.** Base-class bias (Lang et al., CVPR 2022 `[S3]`) fires on seen-class regions;
   without class control, background-similarity effects are partially BAM's bias re-measured.
4. **Stale-checkpoint attack.** The FM re-benchmark (arXiv:2401.11311 `[S3]`) reordered FSS; if
   DINOv2-matching methods don't use the shortcut, the audit indicts a deprecated model class.

**The silencing experiment.**

- *Against 1 (framing, then evidence):* Zhu/TBS treat background mismatch as a *robustness
  nuisance* their method fixes; neither quantifies the shortcut's contribution to *benchmark
  scores* or shows leaderboard gaps move under background-controlled episodes. The audit's
  deliverable is the evaluation-validity number those papers implicitly presuppose: variance
  decomposition of PASCAL-5i/COCO-20i episode scores into background-similarity strata, plus
  the re-ranking of released checkpoints under similarity-controlled episode resampling. The
  method papers become *supporting evidence* (the field already builds fixes for this bias)
  rather than scoops — but only if both are cited and differenced explicitly.
- *Against 2 (two-sided triangulation, binding):* (a) interventional arm with sham-swap
  (identical decompose-recomposite pipeline, same background) *and* a harmonization pass, with
  the artifact tax measured as sham-vs-original delta and subtracted; (b) **non-interventional
  arm with no compositing at all**: stratify natural episodes by measured background similarity
  (frozen-encoder features on GT-background pixels) and show the score gradient across strata.
  The shortcut claim stands only if both arms agree in sign and approximate magnitude.
- *Against 3:* class-controlled design — swap backgrounds within episodes whose backgrounds
  contain no base-class objects (filter via GT); report the BAM-attributable share separately.
- *Against 4:* checkpoint pool spans legacy (PFENet/HSNet-era), 2024 methods (including TBS and
  Zhu et al. — do the *fixes* close the swap gap?), and FM-based baselines from
  arXiv:2401.11311. Pre-registered fork: shortcut persists under FM matching → strong paper;
  disappears → "background shortcut is a ResNet-era artifact," smaller but honest.

Cost: eval-only + compositing pipeline; no training. Kill condition: if the non-interventional
gradient is flat (score independent of background similarity), the shortcut claim dies
regardless of what swaps show — pre-register it.

**What no experiment can fix.** If the effect exists but is fully absorbed by the 2024 fixes,
the paper demotes to a benchmark-hygiene note. Acceptable risk.

**Verdict: SILENCED** — four controls binding (sham-swap + natural-gradient arm + class control
+ FM checkpoints), and explicit differencing against Zhu et al./TBS. **Confidence:** medium-high.

---

## 6. P051 — B1-051: Copy-paste vs diffusion at matched GPU-hours

**Paper under review.** Honest equal-compute frontier for synthetic data in instance
segmentation: charge generation+filtering to the synthesis arm; X-Paste's headline
(arXiv:2212.03863 `[S3]`) as the named adversary; scale-matched real-data arm as third condition.

**R2 attack.**

1. **Amortization ill-posedness (the strongest vector).** Generated instance pools are produced
   once and reused across runs, models, and papers; charging full generation cost to a single
   training run is an accounting *choice*, and under any realistic reuse factor the generation
   term amortizes toward zero. A single "at matched compute, copy-paste wins" verdict is an
   artifact of where the ledger line is drawn.
2. **Strawman generator (F8). NEW EVIDENCE sharpens this.** X-Paste is SD1.5-era. MosaicFusion
   (training-free, ~4.3× fewer generation GPU-hours than X-Paste; IJCV-published, ID re-verify
   `[M]`), the multi-round generative augmentation paper at NeurIPS 2025 (generation reduced to
   ~6% of prior SOTA volume via feedback, proceedings paper `[V]` **NEW EVIDENCE**), and
   FLORA (arXiv:2508.21712 `[V]` **NEW EVIDENCE**, consumer-GPU LoRA generation, 10% of the
   data volume) mean generation cost is collapsing. Compute-matching against X-Paste alone is
   beating a 2023 pipeline with a 2026 ruler; the conclusion has a shelf life of one generator
   generation.
3. **Rare-class confound.** Diffusion's documented advantage is rare/novel classes (X-Paste:
   +6.8 box AP on long-tail) where real instances for copy-paste *do not exist at any compute
   budget*. Pooled-AP compute-matching hides that the two arms buy different things.
4. **Wrong constraint.** In most labs annotation and data access bind, not GPU-hours; who
   deploys on a matched-FLOPs frontier?

**The silencing experiment (this is the mutation).**

- *Against 1:* abandon the verdict framing. The deliverable is the **frontier as a function of
  the amortization factor k** (number of training runs the generated pool is reused across):
  AP(budget, arm, k) with k ∈ {1, 3, 10, ∞}. The paper's finding is the crossover surface —
  "copy-paste dominates below K reuses at budget B; diffusion above" — robust to the accounting
  attack because the accounting *is* the x-axis. Pre-registered kill: if K ≤ 2 at all budgets,
  the honest headline is "diffusion wins under minimal reuse" and the anti-X-Paste framing is
  dropped (publish the frontier anyway).
- *Against 2:* three synthesis pipelines, not one — X-Paste-style (retrieval+filter),
  MosaicFusion-style (training-free), FLORA-style (LoRA-tuned efficient generator) — each with
  its own measured generation ledger. The claim is then about the *frontier's shape*, not one
  pipeline's loss.
- *Against 3:* report frequent/common/rare LVIS strata separately; pre-register the expected
  concession (diffusion wins rare at most k) and let the frontier show where.
- *Against 4:* add a fourth arm — real-data scaling (Ghiasi copy-paste on more real images
  `[S3: arXiv:2012.07177]`) — so the paper answers the deployment question ("given B GPU-hours
  and no new annotation, what do I do?") rather than a metaphysical one.

Cost: this is the expensive survivor — ~40–80 training runs at Mask R-CNN-R50/LVIS-subset
scale plus three generation pipelines. Feasible for one lab with a cluster; borderline against
the rubric's "weeks not years." The k-parameterization does not add runs (it re-weights the
ledger post hoc); the three-pipeline requirement does. Trim by running the third pipeline at
two budgets only.

**What no experiment can fix.** Shelf life. The frontier moves with every generator release;
the paper must sell the *methodology* (the ledger + k-frontier as a reporting standard) as the
durable contribution, with the 2026 numbers as an instance.

**Verdict: SILENCED-IF-MUTATED** — from verdict paper to amortization-parameterized frontier
with ≥3 generation pipelines and frequency strata. Without the k-axis, attack 1 is fatal.
**Confidence:** medium.

---

## 7. P228 — S-228: VLM text prior suppresses atypical presentations (dense, causal)

**Paper under review.** Stage-3 mutation: frequency-controlled, *causally ablated* audit —
does the language prior of text-prompted dense segmenters suppress recall on atypical disease
presentations, with the text prior's contribution isolated?

**R2 attack.**

1. **Frequency→zero-shot is published.** Udandarao et al. (arXiv:2404.04125 `[S3]`) — concept
   frequency governs zero-shot performance; NegBench covers medical VLM text failures
   (arXiv:2501.09425 `[S3]`). "Dense version is an evaluation slice of a known law."
2. **Cross-model confounding.** "Vision-only vs VLM-prompted" across *different* models
   (e.g., nnU-Net vs BiomedParse) confounds architecture, training data, and supervision;
   nothing about the *text prior* is isolated.
3. **Atypicality is unoperationalized.** Pretraining-corpus frequency of a *presentation*
   (not a class) is hard to count; radiologist "atypicality" ratings are subjective; the two
   may disagree.
4. **Power.** Atypical presentations are rare by definition; per-stratum n will be small and
   the headline effect fragile.
5. **The target's own claim points the other way.** BiomedParse (arXiv:2405.12971 `[V]`
   **NEW EVIDENCE**, Nature-Methods-class) advertises *superior* performance on irregular,
   atypical-shaped objects vs box-prompted methods, and its published fairness audit covers
   only sex/age. A reviewer says: the flagship text-prompted medical segmenter claims
   atypicality is its *strength*.

**The silencing experiment.**

- *Against 2 (the design core — within-model causal levers, no cross-model comparison):*
  BiomedParse accepts free text. Hold the image fixed and manipulate *only the prompt*:
  {canonical finding name, typical-presentation descriptor, atypical-presentation descriptor
  matched for length/terminology, shuffled-word prompt, empty/generic prompt}. The text
  prior's causal contribution to the mask is the within-image delta across prompts. Add the
  point/box-prompted SAM-class floor on identical cases as the no-language reference. Every
  comparison is within-model or within-image; attack 2 dies by construction.
- *Against 5 (named-adversary confrontation):* BiomedParse's irregular-shape superiority is
  about *shape*; the hypothesis is about *presentation frequency*. Stratify its own held-out
  data by (a) shape irregularity (their convex-ratio metric) and (b) presentation-frequency
  proxy, and show the two axes dissociate — the model can be good at irregular shapes of
  *common* presentations and still suppress rare ones. If the axes don't dissociate, the
  hypothesis dies; pre-register it.
- *Against 3 (two independent operationalizations, agreement required):* (i) corpus frequency
  of finding-descriptor n-grams in the model's own training corpus (BiomedParseData/PMC-derived,
  accessible); (ii) blinded radiologist typicality ratings on the evaluation cases. Effects
  must replicate under both, else report as inconclusive.
- *Against 4:* aggregate across ≥10 finding types with mixed-effects models (finding as random
  effect); pre-register the minimum detectable suppression (e.g., ≥5 Dice points on atypical
  stratum) and the per-stratum n floor.
- *Against 1:* the differencing sentence writes itself only after the causal arm exists —
  Udandarao predicts the *correlation*; this measures the *prompt-causal share* of the harm on
  dense output, which no frequency-law paper contains. Cite NegBench/CXR-Align/Udandarao in the
  introduction as the recognition-level base camp.

Cost: inference-only on public checkpoints + rating study; the corpus-counting arm is
engineering. Feasible.

**What no experiment can fix.** If the prompt-causal share is ~0 (harm lives in the visual
encoder's frequency bias, not the language prior), the paper becomes "frequency bias in dense
medical segmentation" — still publishable, but it re-enters Udandarao's shadow. Accept the
risk; both outcomes are reportable.

**Verdict: SILENCED-IF-MUTATED** — within-model prompt-manipulation design binding;
cross-model "vision-only vs VLM" comparisons excluded from the headline; dual atypicality
operationalization binding. Pairs naturally with the demoted P107v residue (same target
models, same abstention machinery). **Confidence:** medium.

---

## 8. P061u — B1-061 (folded into B1-069): style × self-training factorial

**Paper under review.** Per Stage-3 mutation: not "histogram matching explains UDA" but a
±style-alignment × ±self-training factorial on modern pipelines, measuring additivity and
interaction, with the B1-061 attribution question as one read-out.

**R2 attack.**

1. **FDA redux.** FDA (arXiv:2004.05498 `[S3]`) made "cheap spectral alignment captures much of
   the gap" the community prior in 2020; it ships in Albumentations. A percentage attached to a
   known direction is not a contribution.
2. **The cells already exist, scattered.** Method papers publish ablations containing factorial
   cells: Kim & Byun (arXiv:2003.00867 `[V]` **NEW EVIDENCE**) *is* a style-transfer +
   self-training pipeline whose ablation reports style-only vs style+ST margins in 2020;
   DAFormer's ablation tables (arXiv:2111.14887 `[S3]`) contain further cells. "Your 2×2 is an
   anthology of other papers' Table 5."
3. **The arms are not separable in modern pipelines.** DAFormer-class self-training embeds
   cross-domain pixel mixing (DACS); "±style" inside a pipeline that already mixes domains at
   the input is ill-defined — remove the mixing and it is no longer the published method.
4. **Compute.** 2×2 × pairs × seeds × a DAFormer-scale pipeline is dozens of GPU-days for a
   result whose direction FDA already gave.

**The silencing experiment.**

- *Against 2 (why scattered cells don't answer it):* published ablations are per-method,
  single-seed, backbone-confounded (DAFormer itself showed the SegFormer backbone absorbs much
  of "UDA progress"), and *never estimate the interaction term* — which is the scientific
  object here. The claim under test is not "style helps" (FDA) but whether style and
  self-training consume the **same** portion of the domain gap (sub-additive → practitioners
  can skip the expensive component) or orthogonal portions (additive → both required). No
  published table decides this with seeds and a fixed backbone.
- *Against 3 (arm definition, binding):* factorialize at the *augmentation interface*, not over
  published methods: base = source-only SegFormer-B3/B5, fixed; +style = input-level
  translation (FDA and histogram-matching as two style instantiations); +ST = confidence-
  thresholded pseudo-label self-training *without* cross-domain mixing; the full published
  methods (DAFormer/MIC) enter as reference points above the factorial, not as cells. State
  explicitly that the factorial tests *component classes*, not trademarked pipelines — this
  concedes attack 3's premise and neutralizes it.
- *Against 1:* the pre-registered deliverable is the interaction sign and its stability across
  {GTA→Cityscapes, Synthia→Cityscapes, one cross-scanner medical pair (e.g., fundus or
  cardiac)}. FDA predicts nothing about the interaction; if the interaction is strongly
  sub-additive on all three pairs, B1-061's "style explains most of it" is *derived* rather
  than asserted, and the practice implication (when to skip ST) is the headline. Kill
  condition: if the interaction is additive everywhere, the attribution story dies and the
  honest paper is "style and self-training are complementary" — a useful negative, one tier
  down.
- *Against 4:* 4 cells × 3 pairs × 3 seeds = 36 runs at ~1–2 GPU-days each, plus 2 style
  instantiations on the +style cells only (+12 runs). ~50–80 GPU-days total. Heavy but within
  one-lab feasibility; trim seeds to 2 on the medical pair if needed.

**What no experiment can fix.** This can never be a flagship — the ceiling is a solid,
well-controlled attribution study at a second-tier venue or a strong workshop-to-main pipeline.
The Stage-3 fold into B1-069 is confirmed; B1-061 must not resurface as a standalone
"histogram matching explains UDA" claim under any outcome.

**Verdict: SILENCED-IF-MUTATED** — interaction-focused factorial with fixed backbone,
augmentation-interface arm definitions, medical third pair, seeds. **Confidence:** medium-high.

---

## NEW EVIDENCE register (found and read this pass; not in Stage-3 files)

1. **HalluSegBench / CSR** — Li et al., arXiv:2506.21546 `[V]` (+ public dataset, PLAN-Lab).
   Counterfactual-edit dense hallucination benchmark + RobustSeg fix. **Overturns Stage 3's
   NOT FOUND #B1-107; P107v flagship revoked.** Also cites Visual Jenga (Bhattad et al.,
   NeurIPS 2025) — counterfactual inpainting as an established instrument.
2. FoSp — AAAI 2024, doi:10.1609/aaai.v38i7.28484 `[V]`. SMOKE5K protocol = mMse + Fβ
   (weakens P096's "binary-only leaderboards" premise; answered by the mMse column).
3. AusSmoke/MultiNatSmoke — arXiv:2604.23542 `[V]`. New binary smoke benchmark, IoU/F1/MSE;
   SOTA deltas of 1–3 IoU points (grist for the S-102 ceiling confrontation).
4. SFMattingNet — Remote Sensing 17(13):2259, 2025, doi:10.3390/rs17132259 `[V]`. Smoke/fire
   trimap-free matting with SAD/MSE/Grad/Conn (the matting turn has begun; must be in the
   P096 checkpoint pool).
5. Zhu et al., background context bias in FSS — CVPR 2024, doi:10.1109/cvpr52733.2024.00324
   `[V]`; TBS — AAAI 2024, doi:10.1609/aaai.v38i5.28242 `[V]`. Named phenomenon + fixes;
   P079f must difference against both.
6. Biophysically-conditioned 3D tumor synthesis — arXiv:2510.09365 `[V]`. Continuous
   infiltration fields; both the realism attack on P040 and its second synthesis arm.
7. Generation-efficiency wave for P051: multi-round generative augmentation (NeurIPS 2025
   proceedings `[V]`), FLORA (arXiv:2508.21712 `[V]`), MosaicFusion (claims verified via
   secondary source; arXiv ID `[M]` — re-verify before citing in a draft).
8. BiomedParse — arXiv:2405.12971 `[V]` (Nature-Methods-class). Text-prompted dense medical
   segmentation with K-S abstention; fairness audit = sex/age only. Concrete target for P228
   and the P107v residue.
9. Zero-shot SAM2-CT ablation study — arXiv:2603.23116 `[V]` full-text checked: prompt /
   memory / multi-axis ablations, **no spacing arm** (P042's gap holds as of 2026-08-28).
   SAM2-ProMem, MICCAI 2025 `[V]`: memory manipulation, not spacing.
10. Kim & Byun, texture-invariant UDA — arXiv:2003.00867 `[V]`. Style+ST composition with
    ablations in 2020 (attack surface for P061u; answered by the interaction framing).

## Summary table

| Target | Strongest attack | Silencing experiment (core) | Verdict | Conf. |
|---|---|---|---|---|
| P096 S-096+S-102 | alpha-GT circularity; mMse already in protocol | measured-alpha real arm (background-frame inversion) + mMse column in τ matrix + rater ceiling | SILENCED | Med-High |
| P040 A1-040 | quantified lore; contrast collinearity | two-factor width×contrast sweep discriminating snap-to-edge vs contrast-threshold; out-of-sample real prediction | SILENCED-IF-MUTATED | Med |
| P042 S-042 | confounded intervention; hygiene-as-paper | slice-decimation (not interpolation) causal design; per-step vs per-mm drift; pre-registered comparators | SILENCED | Med-High |
| P107v B1-107 | **HalluSegBench arXiv:2506.21546 — scooped** | none silences a scoop; narrow removal+sham-surgery+dose-response residue only | **REJECT as constituted** | High |
| P079f B1-079 | CVPR/AAAI 2024 named the bias; compositing artifacts | sham-swap + natural-similarity-gradient triangulation; BAM class control; FM checkpoints | SILENCED | Med-High |
| P051 B1-051 | amortization ill-posedness; strawman generator | k-parameterized amortization frontier; ≥3 generation pipelines; frequency strata | SILENCED-IF-MUTATED | Med |
| P228 S-228 | cross-model confounding; BiomedParse claims the opposite | within-model prompt-content manipulation on BiomedParse; shape-vs-frequency dissociation; dual atypicality measures | SILENCED-IF-MUTATED | Med |
| P061u B1-061 | FDA redux; cells exist scattered; arms inseparable | interaction-estimating 2×2 at augmentation interface, fixed backbone, 3 pairs, seeds | SILENCED-IF-MUTATED | Med-High |

## Notes for the supervisor

1. **P107v's rejection is the pass's load-bearing result.** Stage 3's P5 package (B1-107 +
   S-228) must be rebuilt around S-228's causal design as the lead, with the B1-107 residue
   (removal counterfactuals, sham surgery, abstention audit on BiomedParse) as a supporting
   section, benchmarked on HalluSegBench for comparability. The stage3_top50 flagship list
   needs the corresponding edit at Stage 5.
2. **Recurring pattern across set C:** every survivor was saved by the same three moves —
   (a) replace a verdict/percentage headline with a *parameterized frontier or interaction
   term*; (b) add a *non-interventional triangulation arm* wherever the intervention has an
   artifact confound (swap→natural gradient; insertion→biophysical arm; synthetic alpha→
   measured alpha); (c) name the adversary whose published claim moves if the result lands
   (MedSAM-2's premise, X-Paste's ledger, BiomedParse's atypicality boast). Stage 5 should
   apply the same three tests to sets A and B survivors.
3. **Compute ranking of survivors (cheapest first):** P042, P096, P079f, P228, P040 (all
   inference/eval + light annotation) ≪ P061u (~50–80 GPU-days) ≈ P051 (~40–80 runs).
   The two training-heavy survivors should not both be funded; P051's shelf-life risk makes
   P061u the safer of the two if forced to choose.
4. Per the Stage-3 `[M]` discipline: the MosaicFusion arXiv ID must be re-verified before any
   draft cites it; all other load-bearing citations in this file were fetched this pass.
