# Stage 4 — Reviewer #2 Attack, Set B (PEFT / Forgetting / Calibration / Medical-preprocess)

Role: Reviewer #2. Stance per rubric: **default REJECT. Survival iff a realistic experiment would silence the attack.**
Date: 2026-08-28. Inputs: `stage3_top50.md`, `stage3_kill_peft_vlm.md`, `stage3_kill_medical_smoke.md`, original
hypothesis text in `stage1_*.md` / `stage1_supervisor_seed.md`.

Epistemic status: REVIEW JUDGMENT. Citations below are **inherited from the Stage-3 kill files** (verified there,
tagged `[V]`/`[M]` in those documents); none were re-verified this pass and none are new. No experimental result
is claimed anywhere in this file.

Schema per target (as dispatched):
**Reject paragraph → Load-bearing assumption → Confounder → Missing baseline → Experiment-can-silence? → Verdict (REJECT / WEAK ACCEPT).**

A WEAK ACCEPT here is conditional: the listed silencing experiment and baselines are **mandatory obligations**; if
Stage 5 drops any of them, the verdict reverts to REJECT.

---

## Scoreboard

| # | Paper | IDs | Core claim under attack | Experiment can silence? | Verdict |
|---|-------|-----|-------------------------|-------------------------|---------|
| 1 | P065 | C1-065 + C1-061 | Prompt-type-resolved forgetting; multimask diversity collapse | YES (coverage-vs-forgetting factorial) | WEAK ACCEPT |
| 2 | P177 | S-177 + C1-062 | Forgetting localizes to decoder cross-attn; splice restores | YES (stitch-controlled swap grid) | WEAK ACCEPT |
| 3 | P107 | A1-107 | Attention-LoRA fixes boundaries, MLP-LoRA fixes regions | YES (matched-budget factorial, decoupled metrics) | WEAK ACCEPT |
| 4 | P031 | C1-031 (+C1-025/037/S-318) | FT desyncs IoU head; calibration tax | YES (recipe × domain × recalibration) | WEAK ACCEPT |
| 5 | P052 | S-052 (mutated) | Objectness prior harms stuff-like lesions at small n | YES for the harm; PARTIAL for the mechanism label | WEAK ACCEPT (re-scoped) |
| 6 | P110 | C1-110 | One gain–retention frontier scalar reliably ranks methods | **NO** (scalar validity is not empirical) | **REJECT** (standalone) |
| 7 | P108 | A1-108 + C1-067 | Interface drift *predicts* later zero-shot drop | In principle yes; null is worthless (ROI kill rule) | **REJECT** |
| 8 | P082 | C1-082 + S-183 | Published "forgetting" sits inside a threshold/plasticity noise floor | YES (noise-floor envelope on released checkpoints) | WEAK ACCEPT (run FIRST) |
| 9 | P044 | S-044 + A1-034 | Despeckle/window recovers ≥50% of PEFT gain on frozen SAM | YES (pre-registered falsifier w/ honest LoRA arm) | WEAK ACCEPT |

Net: 7 WEAK ACCEPT (all conditional) / 2 REJECT. Cross-paper structural attacks at the end of this file apply to
every WEAK ACCEPT and are non-optional.

---

## 1. P065 — C1-065 + C1-061: prompt-type behavioral forgetting + multimask diversity collapse

**Reject paragraph.**
The phenomenon — fine-tuning erodes SAM's zero-shot promptability — is motivation boilerplate, not a finding: Gu et
al. (arXiv:2404.09957) document collapse across 18 fine-tuning combinations, and CA-SAM (arXiv:2511.17201) cites the
erosion as the known problem its method fixes. Prompt-mode-resolved tables after fine-tuning already exist: SAM-Med2D
(arXiv:2308.16184) publishes Bbox/1pt/3pt/5pt for frozen SAM vs FT variants. What the authors add is an *ordering*
claim (points forget before boxes; negative clicks first per A1-109; diversity collapses), and they cannot currently
distinguish it from the trivial explanation: **models degrade on the prompt modes they were not fine-tuned with.**
That is train/test prompt-distribution mismatch — a data-coverage statement, not forgetting, and MedSAM (box-only
training, poor point behavior) already demonstrates it. The diversity-collapse half (C1-061) is an artifact-in-waiting:
standard SAM fine-tuning recipes either disable multimask output or backpropagate only the minimum-loss mask of the
three, so post-FT diversity collapse is a mechanical consequence of the loss-aggregation choice. As submitted this is
a table other papers half-contain, plus an artifact with a diversity metric the authors themselves flag as contested.

**Load-bearing assumption.** That prompt-type-specific degradation is a property of the *model* rather than of the
fine-tuning *prompt-sampling distribution*; and that "matched in-domain gain" across arms (full FT, decoder FT, LoRA)
is well-defined and achievable without introducing a new confounder (different early-stop points = different
effective training lengths).

**Confounder.** (a) FT prompt protocol: box-only vs point-only vs mixed training determines the observed ordering.
(b) Loss aggregation (min-loss-mask backprop vs all-mask) determines the diversity result. (c) Binarization
threshold shifts masquerading as forgetting (C1-082 — P082 gates this paper). (d) Seed and prompt-sampling variance
(C1-060) vs the size of the claimed ordering gaps.

**Missing baseline.** Frozen SAM with per-domain re-tuned threshold (fair floor); a *mixed-prompt* FT arm; LR-swept
full-FT and decoder-only arms (Gu et al.'s grid); VeRA/random-direction PEFT control (per Stage-3 cluster-2 ruling);
all-mask-loss FT arm for the diversity claim; ≥3-seed confidence intervals on every ordering statement.

**Experiment-can-silence?** **YES.** Crossed factorial: FT-prompt-mix {box-only, point-only, mixed} × eval battery
{box, 1-click, 5-click iterative incl. negative clicks, multimask-ambiguity} at matched target-domain gain
(pre-registered matching rule, e.g. first checkpoint within ±0.5 Dice of the weakest arm's best), threshold re-tuned
per arm on a held-out calibration split, ≥3 seeds. The forgetting claim survives **only if the prompt-type ordering
persists inside the mixed-prompt column** — that column isolates forgetting from coverage; the box-only column alone
proves nothing. For diversity: report the oracle-best-of-3 vs IoU-head-argmax gap on held-out ambiguous cases
(multi-annotated SA-1B-style instances); if FT kills *oracle-best-of-3*, capability was lost (real); if only the
argmax moves, it is a ranking/IoU-head problem and belongs to P031, not here. Cost: modest FT grid + eval — realistic.

**Verdict: WEAK ACCEPT.** Flagship of the thread, but the paper is the mixed-prompt column and the oracle-gap
decomposition; without them it is SAM-Med2D's table re-plotted.

---

## 2. P177 — S-177 + C1-062: forgetting locus (decoder vs encoder), layer-splice restoration

**Reject paragraph.**
"Forgetting concentrates in later/deeper layers" is known for deep networks (Ramasesh et al., arXiv:2007.07400), the
constructive twin ("which block should you tune") is published (surgical fine-tuning, arXiv:2210.11466), and Gu et
al. already ran encoder-vs-decoder tuning arms on SAM. The claimed novelty is the causal splice: put pre-FT prompt
cross-attention back into a fine-tuned SAM and watch zero-shot return. But the splice conflates **locus of
forgetting** with **interface compatibility** — and the authors' own portfolio contains the contradiction: sibling
proposal P108/A1-108 claims encoder adaptation shifts embedding statistics beyond the decoder's tolerance. If
interfaces drift, a failed splice does not mean forgetting is distributed and a successful splice does not mean it is
localized; chimera behavior is dominated by representational mismatch, which is exactly what the model-stitching
literature (Bansal et al., arXiv:2106.07682) warns about. Separately, "forgetting localizes where plasticity was
allowed" is close to tautological under standard recipes: the decoder receives most of the effective update, so the
freeze ablation (S-177) may simply re-describe the recipe.

**Load-bearing assumption.** Module interchangeability across checkpoints — that the encoder-decoder interface is
stationary enough for swapped modules to compose meaningfully — and that the forgetting locus is a property of the
architecture rather than of the per-module effective learning rate.

**Confounder.** (a) Per-module effective plasticity (LR × gradient norm × parameter count): locus tracks recipe unless
update-norm-matched arms are run. (b) Stitching incompatibility masquerading as "distributed forgetting."
(c) Swap-direction asymmetry (old-into-new vs new-into-old) never checked.

**Missing baseline.** Per-module WiSE-FT-style α-interpolation curves (the continuous superset of the binary splice —
if interpolation already shows decoder dominance, the splice is one point on a curve someone else can publish first);
splice **with a trained affine stitching layer** (cheap, per Bansal et al.) to separate mismatch from lost function;
both swap directions; Gu et al.'s enc-only/dec-only FT arms; update-norm-matched per-module fine-tuning.

**Experiment-can-silence?** **YES.** Full swap grid over {encoder, prompt encoder, decoder cross-attn, decoder rest},
both directions, each cell with and without a small trained stitch, plus per-module α-interpolation, on the matched-
gain checkpoints from P065's grid (reuse — no new training). Pre-registered readout: fraction of the zero-shot drop
recovered, with seed CIs. If cross-attn-splice+stitch restores most zero-shot while encoder-splice+stitch restores
approximately none, the locus claim stands at mechanism grade and I am silenced. Eval-only given checkpoints; cheap.

**Verdict: WEAK ACCEPT**, conditional on stitching controls and the interpolation baseline. The freeze ablation alone
(S-177) is one figure and remains REJECT as a standalone; it lives only as an arm inside this design.

---

## 3. P107 — A1-107: attention-LoRA fixes boundaries; MLP-LoRA fixes regions

**Reject paragraph.**
Placement studies are legion (He et al., arXiv:2110.04366; Conv-LoRA, arXiv:2401.17868; CoDyRA, arXiv:2412.01004);
the sole claimed delta is the placement→error-type map. But the two "error types" are not independent measurements:
**every region error contributes boundary error along its entire perimeter**, so boundary-F and interior-IoU are
mechanically coupled, and "attention fixes boundaries" may be nothing but the metric shadow of "this placement
happened to help more overall." Add the budget confound — rank-matched is neither parameter-matched nor
ΔW-norm-matched across attention projections vs MLP blocks — and the headline dichotomy is plausibly an artifact of
unmatched effective capacity read through correlated metrics. Conv-LoRA's local-inductive-bias narrative partially
contradicts the prediction; the authors present this as an honest kill-or-confirm, but the modal outcome is a mush of
non-decomposing effects on noisy medical boundary annotations — a null with no story.

**Load-bearing assumption.** That boundary vs interior error is a separable, attributable decomposition, and that
"matched rank" makes attention and MLP placements comparable.

**Confounder.** (a) Parameter count / ΔW spectral norm per placement. (b) Depth entanglement: attention and MLP
blocks exist at every depth, so placement effects may actually be depth effects. (c) Per-placement LR optimum.
(d) Boundary-annotation noise floor on medical data (inter-rater boundary jitter can exceed the claimed effect).

**Missing baseline.** Parameter-matched *and* ΔW-norm-matched grids; depth-stratified placement (early-vs-late
attention, early-vs-late MLP); Conv-LoRA as both baseline and rival theory; a **boundary-weighted-loss arm** — if loss
reweighting reproduces the "attention effect" under MLP placement, the mechanism is gradient signal, not placement;
combined attn+MLP at half budget each; ≥5 seeds with a pre-registered placement × error-type interaction test.

**Experiment-can-silence?** **YES.** The matched-budget, depth-stratified factorial with decoupled metrics — trimap-
band boundary quality *conditioned on matched interior detection*, not raw boundary-F — plus the loss-reweighting
counter-arm, on ≥2 datasets with disjoint annotation pipelines. If the interaction survives parameter matching, norm
matching, depth stratification, and the loss-reweighting control, the placement rule is real and I am silenced.
Small grids on public medical sets; realistic.

**Verdict: WEAK ACCEPT.** Only constructive/mechanism paper in this set; keep, but the decoupled-metric requirement
is non-negotiable — with raw boundary-F this is unpublishable regardless of outcome. A clean null is only reportable
inside the full placement × depth × budget study, so budget for that scope from the start.

---

## 4. P031 — C1-031 core (+C1-025, C1-037, S-318 merged): IoU-head desync / calibration tax

**Reject paragraph.**
"Fine-tuned models become miscalibrated" is a genre with fixes attached (Laplace-LoRA, arXiv:2308.13111; BLoB;
SWAG-LoRA), and robustness-for-gain trades are canon (Kumar et al., arXiv:2202.10054; WiSE-FT, arXiv:2109.01903);
porting either to segmentation is banned-pattern F2 without a divergence mechanism, as the authors' own Stage-3 file
concedes. The genuinely fresh object is SAM's separate IoU head — but the desync result is **over-determined by the
field's recipes**: MedSAM-style fine-tuning trains the mask path with Dice+CE and leaves the IoU-head loss off or
vestigial, so of course the confidence head drifts out of sync — the authors will have discovered that an untrained
head is untrained. Their own Stage-1 risk note ("easy fix reduces impact") is fatal as a headline: a one-line recipe
change (re-enable the IoU MSE term) or five minutes of post-hoc recalibration on a hundred validation masks plausibly
erases the phenomenon. What would remain — desync that survives a correct recipe, out of distribution — is currently
an assumption, not a result.

**Load-bearing assumption.** That desync persists when the IoU head is properly trained during FT *and* after cheap
post-hoc recalibration; and that dense-prediction calibration genuinely diverges from the classification/LLM genre
(claimed mechanism: Dice/focal loss geometry) rather than reproducing it.

**Confounder.** (a) Recipe: IoU-loss on/off and multimask on/off fully determine the naive result. (b) Measurement
domain: in-domain desync (recipe bug, fixable) vs held-out zero-shot desync (interesting) are different claims —
conflating them inflates the finding. (c) The matched-mIoU comparison across full-FT/PEFT inherits the same
gain-matching under-specification as P065. (d) Frozen SAM's IoU head may already be miscalibrated OOD (C1-026),
shrinking the "tax" attributable to FT.

**Missing baseline.** FT **with** the IoU-head loss enabled (the honest recipe — without this arm the paper is a bug
report); post-hoc recalibration arms (temperature scaling, isotonic, small head refit) at their true, trivial cost;
frozen-SAM OOD IoU-head calibration as the floor; and a decision-level consequence metric — multimask ranking
corruption (ties to P065's oracle-gap) and precision of predicted-IoU-filtered mask sets — because ECE deltas without
decision damage will not move reviewers.

**Experiment-can-silence?** **YES.** The 2×2×2 factorial {IoU-loss on, off} × {in-domain, held-out zero-shot} ×
{raw, recalibrated}, plus decision-consequence readouts, on the P065 checkpoint grid. The paper survives only in the
cell {IoU-loss on, zero-shot, recalibrated}: a residual desync that a correct recipe and cheap recalibration cannot
remove, with demonstrated ranking/filtering damage. Heads are tiny; the cost is evaluation. Realistic.

**Verdict: WEAK ACCEPT**, with the explicit warning that the modal outcome is a recipe footnote — acceptable only
because the factorial is cheap and the S-318 ordering claim ("calibration breaks before Dice") plus the C1-032
dense-loss divergence mechanism give the merged paper two additional ways to be interesting. If the easy fix kills
the desync, report the kill inside P082's deflation frame; do not stretch it into a paper.

---

## 5. P052 — S-052 (mutated): objectness prior as a small-n liability for stuff-like lesions

**Reject paragraph.**
"ImageNet transfer barely helps medical" is Transfusion (arXiv:1902.07208); "random init matches pretraining given
schedule" is He et al. (arXiv:1811.08883); "pretraining can hurt" is Zoph et al. (arXiv:2006.06882, opposite data
regime). The mutation promises a mechanism — SAM's *objectness prior* fights amoeboid, low-contrast, stuff-like
lesions at n≈50 — but "objectness prior" is not an ablatable quantity: any encoder-family comparison (SAM vs DINOv2
vs supervised vs random) varies pretraining data, objective, and effective architecture simultaneously, so attributing
the gap to "objectness" is narrative, not measurement. Worse, at n=50 both subset-draw variance and per-arm
hyperparameter fragility (random init demands its own schedule; a lazy recipe manufactures whichever crossover you
want) are individually large enough to create or erase the claimed effect. A single learning curve from a single
draw with shared hyperparameters — which is what the Stage-1 card describes — is not evidence of anything.

**Load-bearing assumption.** That the SAM-init deficit, if it exists, is attributable to a *prior over mask shapes*
rather than to pretraining-distribution mismatch generally; and that one n=50 draw is representative.

**Confounder.** (a) Hyperparameter-recipe × init interaction — dominant at small n. (b) Subset-draw variance.
(c) Lesion "stuff-ness" correlates with contrast, size, and annotation noise, so shape-stratified comparisons are
confounded by difficulty unless matched. (d) Tiny test sets on the relevant datasets → wide CIs on every gap.

**Missing baseline.** Frozen-encoder probes (if frozen SAM features + a light decoder beat fine-tuning at n=50, the
story is optimization, not the prior); DINOv2 and MAE arms at matched architecture (ViT-B everywhere); an n-grid
(50/100/200/500) with ≥10 resampled draws per point and per-arm HP sweeps; difficulty matching across shape strata
(match on frozen-SAM oracle-prompt Dice per stratum).

**Experiment-can-silence?** **YES for the harm; PARTIAL for the mechanism word.** Two pre-registered prongs:
(1) *Existence*: resampled learning curves, per-arm sweeps, matched-arch init families — settles whether SAM/FM init
underperforms random/self-sup init at small n at all. (2) *Mechanism*: the interaction test — the SAM-init deficit
grows with lesion stuff-ness while the DINOv2-init deficit does not, on difficulty-matched strata — plus a stimulus-
side causal arm: synthetic lesions with parametric "thing-ness" (compactness, boundary sharpness, contrast) composited
into real backgrounds, manipulating the prior's engagement without touching the model. If both prongs come out
positive I am substantially silenced; the residual attack ("that's pretraining-data distribution, not 'objectness'")
is about the label, not the measured interaction. Runs at n≈50 are minutes each; ~2k short runs ≈ a few GPU-days.

**Verdict: WEAK ACCEPT — re-scoped.** Mandatory: retitle the claim to the measurable interaction
("segmentation-pretrained init deficit grows with lesion stuff-ness at small n"); "objectness prior" may appear as
interpretation, never as the result. Both null outcomes (no harm; no interaction) are protected contrarian
lore-corrections, which is what keeps this above the REJECT line despite the fragile chain.

---

## 6. P110 — C1-110: gain–retention reporting protocol / frontier scalar

**Reject paragraph.**
Every component is published: the ID-gain-vs-zero-shot-retention frontier is the central figure of WiSE-FT
(arXiv:2109.01903); BWT/FWT have been the standardized gain-vs-retention scalars in continual learning since GEM
(arXiv:1706.08840, 2017); target-vs-control-task trade-off panels are task-arithmetic-era routine (arXiv:2212.04089);
and CA-SAM already publishes adaptation-plus-retention tables for SAM across nine datasets without needing this suite.
The Stage-1 hypothesis — "one frontier scalar reliably ranks adaptation methods" — is not an empirical claim at all:
whether a scalarization "reliably ranks" depends on the downstream user's trade-off preferences, which no experiment
can measure. The proposed rescue (a pre-registered rank flip between the scalar and single-metric rankings) cuts the
wrong way: a rank flip is evidence that the *panel* matters and that any single scalar — including the proposed one —
hides information. The suite is reporting hygiene, and reporting hygiene is a section, not a paper.

**Load-bearing assumption.** That there exists a preference-free, use-case-independent way to validate one scalar as
the "right" summary of a gain–retention surface. There is not.

**Confounder.** The scalar's ranking behavior depends entirely on the weighting/normalization chosen; any demonstrated
"reliable ranking" is circular (methods are ranked reliably *by the metric that defines the ranking*).

**Missing baseline.** Not applicable in the usual sense — the decisive comparisons (report BWT/FWT + WiSE-FT frontier
+ per-prompt-type retention as a panel) are exactly what reduces this to prior art.

**Experiment-can-silence?** **NO.** A rank-flip demo shows panels beat scalars (argument against the paper's own
scalar); no realistic experiment establishes scalarization validity, because it is a values question. This fails the
rubric's Stage-4 kill rule directly: the attack cannot be answered by an experiment.

**Verdict: REJECT** as a standalone paper — concurring with and hardening the Stage-3 demotion. Disposition: the
reporting panel (per-prompt-type retention, frontier plot, model-card row) becomes a mandatory *appendix protocol* of
P065 and P031. C1-110's Protect status should not shield a leaderboard with no finding.

---

## 7. P108 — A1-108 + C1-067: interface drift predicts later zero-shot regression

**Reject paragraph.**
Measuring representational drift across module boundaries is mature (CKA, arXiv:1905.00414; stitching,
arXiv:2106.07682; drift-as-forgetting-probe, Davari et al., arXiv:2203.13381), and CA-SAM has already methodized the
encoder–decoder interface with a shipped alignment layer — the conceptual room is shrinking, as Stage 3 conceded. The
mutated deliverable ("drift *predicts* regression with lead time and decision value") faces a baseline it has not
argued it can beat: **directly evaluating zero-shot behavior on a ~50-image probe set every k steps**, which measures
the actual quantity of interest at a cost comparable to computing the drift statistic itself. For the proxy to matter
it must show genuine lead time over direct measurement of its own validation target, beat trivial covariates (step
count and train loss "predict" any monotone degradation), and transfer across held-out *recipes*, not just seeds —
which requires a population-of-runs study. And the asymmetry that kills it: **the null outcome is worthless.** If
drift fails to beat step count or the direct probe, nothing in the literature is corrected — nobody claimed it would.
The paper only pays on the improbable branch; the rubric's ROI rule (upside × falsifiability / compute) prices this
below the line even though the study is technically runnable.

**Load-bearing assumption.** That internal drift moves *before* cheaply-measurable behavior does (representational
precursors with usable lead time), and that one drift statistic chosen a priori generalizes across recipes without
garden-of-forking-paths selection among the dozens of CKA/layer/token variants.

**Confounder.** Monotone-decay trivialities: in typical FT runs zero-shot decays monotonically, so *any* monotone
statistic — including wall-clock — "predicts" later drops. Incremental predictive value beyond step count and train
loss is the only admissible readout, and it is absent from the proposal.

**Missing baseline.** Direct sparse behavioral probing (the near-unbeatable one); step-count and train-loss
predictors; cross-recipe holdout validation; cost accounting per prediction.

**Experiment-can-silence?** In principle yes — a ~40-run population study (datasets × recipes × seeds) where the
pre-registered drift statistic beats step count, train loss, and the direct probe on lead time and early-stopping
decision value, validated on held-out recipes. I judge the silencing branch improbable and the null branch valueless;
per the ROI kill rule that combination is disqualifying even when an experiment technically exists.

**Verdict: REJECT.** Disposition: the drift statistic survives as one *covariate* logged inside P065/P177's training
grid (free to record, occasionally diagnostic). If, incidentally, it shows striking lead time there, Stage 5 may
resurrect the prediction paper with the population study pre-registered. It does not hold a Top-50 slot on its own.
Note the freed budget also resolves the portfolio's internal contradiction: P177's stitching controls double as the
test of A1-108's "interface tolerance" story, so nothing scientific is lost by this rejection.

---

## 8. P082 — C1-082 + S-183: threshold artifact + low-plasticity gatekeeper

**Reject paragraph.**
The learning–forgetting coupling is quantified (Biderman et al., arXiv:2405.09673: less learned, less forgotten;
Soutif et al. for ViTs), so the conceptual engine is borrowed, and threshold/operating-point pitfalls are Metrics
Reloaded canon — insiders already know both halves. The audit's bite therefore depends entirely on execution against
*other people's* claims, which raises the strawman trap (banned pattern F8): where checkpoints are unreleased, the
authors must re-implement, and every deflationary result will be answered with "your reimplementation is broken";
where checkpoints are released, the sample is biased toward reproducible papers and the indictment does not
generalize. There is also a fairness landmine inside the headline mechanism: "re-tuned threshold recovers lost
zero-shot" is leakage unless the threshold is granted symmetrically — frozen and fine-tuned models must both get
per-domain thresholds tuned on the same held-out calibration split, or the recovery is an artifact of asymmetric
oracle access. Finally, the self-defeating branch: if the audit finds forgetting *does* exceed the noise floor, this
"paper" is a confirmation note.

**Load-bearing assumption.** That the noise-floor envelope (seed × prompt-sampling × threshold × split variance) can
be computed under the *published* protocols faithfully enough that authors of audited papers cannot dismiss it, and
that enough flagship checkpoints (MedSAM, SAM-Med2D at minimum) are public to anchor the audit in re-evaluations
rather than re-implementations.

**Confounder.** (a) Asymmetric threshold tuning (the leakage above). (b) Protocol drift between the audited papers'
evaluation code and the audit's re-implementation. (c) Plasticity measurement itself: "task-2 gain is tiny" depends
on the same gain-matching conventions that P065/P031 struggle with.

**Missing baseline.** The frozen model run under *identical* variance sources (same seeds, same prompt draws, same
splits) as the fine-tuned ones — the envelope must be measured, not assumed; a Biderman-style gain-vs-retention
regression across the P065 checkpoint grid to show the coupling holds in this regime (confirmatory framing, as
Stage 3 already mandated); and an explicit list, fixed in advance, of which published deltas are being tested against
which envelope.

**Experiment-can-silence?** **YES — and cheaply, which is why it lives.** Eval-only: released checkpoints re-run under
the published protocols with symmetric threshold tuning; noise-floor envelope from frozen-SAM variance decomposition;
published forgetting deltas plotted against the envelope. Every outcome is informative: deltas inside the envelope
deflate a subfield; deltas outside it license the entire Forget thread (P065, P177, P031) with the noise floor
pre-computed. That two-sided payoff is exactly what the rubric protects.

**Verdict: WEAK ACCEPT — and it must run FIRST**, as Stage 3 ordered: it is the gatekeeper that decides whether
P065/P177 are measuring signal. Obligations: symmetric threshold protocol, released-checkpoints-only for any named
indictment, pre-registered target list, confirmatory (not discovery) framing of the Biderman coupling.

---

## 9. P044 — S-044 + A1-034 (mutated): physics-aware preprocessing vs PEFT falsifier

**Reject paragraph.**
The CT half of the original idea is dead — windowing is standard practice already quantified inside SAM2-CT pipelines
(SAMCT; the 2026 bone-CT study reporting ~30% from windowing alone), which Stage 3 acknowledged by killing A1-032 —
and RobustSAM (arXiv:2406.09627) explicitly argues learned degradation-invariant modules beat restoration
preprocessing, so the field has a published answer pointing the other way. What survives is one number: does
despeckling recover ≥50% of the LoRA gain on ultrasound? Three attacks. First, the strawman risk: Gu et al. showed
decoder-only fine-tuning is insufficient, so beating *decoder*-LoRA is beating a known-weak arm; the comparison must
be against encoder+decoder LoRA or reviewers will call it rigged (F8). Second, the ground-truth problem: ultrasound
GT boundaries were drawn by sonographers *on speckled images*; despeckling shifts apparent boundaries, so part of any
"gain" (or loss) is annotation-convention artifact, and the authors' own risk note ("despeckling may erase true
boundaries") concedes it. Third, significance: even a clean positive changes little practice — despeckling and LoRA
are both cheap, practitioners will do both, and "preprocess before you fine-tune" is a workshop tip, not a finding.

**Load-bearing assumption.** That the despeckle-vs-adaptation comparison is well-posed at all — i.e., that GT masks
define the same task on raw and despeckled inputs, and that NLM strength can be set without touching test data.

**Confounder.** (a) Annotation-convention shift under despeckling (the boundary-band problem). (b) NLM/window
hyperparameters tuned where? Test-set leakage manufactures the headline number. (c) Prompt-type interaction: box
prompts partially shield SAM from speckle; point prompts do not — a single-protocol result may not transfer.
(d) Dataset idiosyncrasy across the three ultrasound sets.

**Missing baseline.** Encoder+decoder LoRA (the honest PEFT arm); the **combination arm** (despeckle + LoRA) — if
effects are additive the "preprocess *vs* PEFT" framing collapses into "preprocessing is complementary," which changes
the story; boundary-band-excluded metrics (inner-core Dice + trimap analysis) to control the annotation artifact;
per-arm preprocessing-parameter tuning on training splits only; a test-time-augmentation control at matched inference
cost.

**Experiment-can-silence?** **YES — this is, by construction, the cheapest falsifier in the set.** The Stage-3 killer
experiment, hardened: 3 ultrasound sets (BUSI, TN3K, CAMUS) + 2 CT organ sets; {raw, despeckled, windowed} ×
{frozen, decoder-LoRA, enc+dec-LoRA, despeckle+enc+dec-LoRA}; identical box *and* point protocols; preprocessing
parameters tuned on train splits; boundary-band-excluded metrics alongside standard Dice; pre-registered claim:
preprocessing recovers ≥50% of the enc+dec-LoRA gain on ≥2 of 3 ultrasound sets. Both outcomes reportable (the
failure mode — despeckling erases diagnostic boundaries — is itself a finding against the preprocessing reflex).
Days of compute, not weeks.

**Verdict: WEAK ACCEPT** — scoped honestly as a compact falsifier paper. The significance attack stands as a ceiling:
this is a strong short paper or workshop headliner, not a main-track flagship; Stage 5 should budget it accordingly
and must not let it absorb resources from P065/P082.

---

## Cross-paper structural attacks (apply to all WEAK ACCEPTs; supervisor must answer)

1. **Shared-grid poisoning.** P065, P177, P031, P082 all reuse one fine-tuning checkpoint grid. Efficient — but a
   single recipe flaw (e.g., IoU-loss off, min-loss-mask backprop, unswept LR) contaminates four papers at once, and
   hostile reviewers of any one paper inherit every recipe attack. The grid recipe must be pre-registered once,
   reviewed against Gu et al.'s protocol, and frozen before any paper's analysis begins.
2. **"Matched gain" is a single point of failure.** P065's ordering, P031's matched-mIoU calibration comparison, and
   P082's plasticity measurement all lean on one under-specified matching convention. Define it once (metric,
   tolerance, early-stop rule), pre-register it, and use it verbatim in all three — otherwise each paper's reviewers
   will re-litigate it independently.
3. **Internal contradiction resolved by P108's rejection.** P177 assumes module interchangeability; A1-108 asserts
   interface drift breaks it. With P108 rejected, P177's stitching controls become the portfolio's only test of the
   interface story — they are therefore mandatory, not optional (already reflected in P177's obligations).
4. **Execution order.** P082 first (gatekeeper; may deflate the thread). Then the shared grid, then P065 → P031 →
   P177 (eval-reuse chain). P107 is independent (constructive slot). P052 and P044 are independent medical-side
   falsifiers. P110's panel ships inside P065/P031 appendices.
5. **Citation debt.** All attack citations above inherit Stage 3's verification status; `[M]`-tagged classics in
   those files (Ramasesh, Kumar, WiSE-FT, GEM, He, Zoph, Transfusion, CKA, stitching) must be re-verified before any
   draft quotes them.

## Verdict table (final, Set B)

| Paper | Verdict | One-line disposition |
|-------|---------|----------------------|
| P065 | WEAK ACCEPT | Lives in the mixed-prompt column + oracle-gap decomposition; else it is SAM-Med2D's table |
| P177 | WEAK ACCEPT | Lives only with stitching controls + α-interpolation; freeze ablation alone stays dead |
| P107 | WEAK ACCEPT | Lives only with matched budgets, depth stratification, decoupled metrics, loss-reweight arm |
| P031 | WEAK ACCEPT | Lives only in the {IoU-loss on, zero-shot, recalibrated} cell with decision damage |
| P052 | WEAK ACCEPT | Re-scoped to the stuff-ness × init interaction; "objectness prior" demoted to interpretation |
| P110 | **REJECT** | Scalar validity is not empirical; panel folds into P065/P031 appendices |
| P108 | **REJECT** | Direct probing dominates; worthless null; drift logged as a free covariate in the grid |
| P082 | WEAK ACCEPT | Gatekeeper — runs first, symmetric thresholds, released checkpoints only |
| P044 | WEAK ACCEPT | Compact falsifier vs enc+dec-LoRA with boundary-band controls; workshop-scale ceiling |
