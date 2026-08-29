# Stage 4 — Reviewer #2, Set A (50→20)

Date: 2026-08-28. Role: **Reviewer #2. Goal: REJECT.**
Survival rule (from `evaluation_rubric.md`): a project survives **only if a REALISTIC experiment would silence the core attack**. Attacks that are philosophical, require a new foundation-model pretrain, or cannot be experimentally controlled ⇒ **KILL**.

Epistemic status: **REVIEW JUDGMENT**. Citation policy: every named paper below either (a) appears in `stage3_kill_*.md` with an arXiv id claimed web-verified by the Stage-3 assassins, or (b) is a well-known public artifact cited from reviewer memory **without** an invented identifier and flagged for run-time verification. Architecture/dataset facts marked KNOWN FACT (code) are verifiable in the released `segment-anything` / `sam2` repositories or dataset cards. No fabricated papers, no fabricated numbers.

Targets (assigned): P14, P101, P079, P103, P063, P060, P001, P004, P007.
Set-A scoreboard: **4 REJECT / 5 WEAK ACCEPT** (all accepts conditional; cut order at the end).

---

## P14 — S-014 / S-604 — Ablate image tokens inside a tight box, prompt fixed

**Claim.** With tight GT boxes, destroying image evidence inside the box (embedding-zeroing, patch-shuffle, matched noise) barely changes Dice ⇒ SAM is a box-to-mask interpolator, not a model that "sees."

**Strongest reject paragraph.** The proposed intervention cannot identify the claim. (i) It is off-manifold: zeroed/mean image embeddings and patch-shuffled interiors are inputs no natural image produces; decoder behavior under them licenses no conclusion about what the decoder consults on natural inputs — the standard ablation fallacy of interpretability. (ii) It is not even localized: the ViT encoder is global, so pixel-level corruption inside the box changes embeddings *everywhere* via attention, and embedding-level zeroing inside the box creates activation statistics the decoder has never seen; "image evidence inside the box" is not a manipulable variable at either level. (iii) A degenerate positive is guaranteed by architecture: SAM's decoder re-injects positional encodings into the image-embedding side of cross-attention at every layer (KNOWN FACT, code/paper appendix), so with features destroyed the decoder still receives a full positional scaffold — emitting a clean box-shaped mask from positions alone is what the machinery *should* do and reveals no discovered "prior." (iv) The payoff is asymmetric: if Dice collapses, the result is the null everyone already believes ("SAM sees") — Stage 3's own kill-condition concedes this; if Dice persists, points (i)–(iii) plus dataset geometry explain it without any interpolator claim.

**Hidden assumption.** "Dice invariant under interior ablation ⇒ decoder ignores image evidence." The alternative with the identical signature: the *task* is degenerate — tight boxes on convex objects are near-sufficient statistics for the mask, so any mechanism (including a trivial one) scores high with or without image evidence.

**Confounder.** Object convexity/solidity jointly drives both the box-fill null and the intact score; contrast stratification alone does not control it. The padding sweep {0,4,8,16 px} conflates prompt informativeness with ablated area.

**Missing baselines.** (1) Prompt-only decoder — replace the *entire* image embedding with the dataset mean; that is the interpolator claim in one number. (2) A tiny trained box→mask regressor with no image input — if it matches ablated-SAM, "interpolation" is a property of label statistics, not of SAM. (3) Per-instance convexity-matched box-fill null, not a global one.

**Why significance fails (as designed).** BREPS (arXiv:2601.15123, Stage-3-verified) and the box-artifact literature already discredited tight-box protocols on natural images; "tight-box evaluation is degenerate" is priced in. The only regime where a positive indicts *published numbers* is low-contrast medical, where tight boxes are the deployed protocol (MedSAM-class evaluation) — and the current design treats medical as one of two symmetric arms instead of the point.

**Can an experiment shut me up? YES.** Redesign: (a) make **on-manifold natural counterfactuals** the primary intervention — diffusion-inpaint the object out (or swap in a different object) with the box held fixed; image evidence changes, input statistics stay natural, prompt constant; (b) demote embedding-zeroing / S-604 patch-shuffle to secondary convergence checks; (c) add the prompt-only and learned box→mask nulls, matched per instance on convexity; (d) make low-contrast medical the primary endpoint: report what fraction of MedSAM-protocol box-prompt Dice is reachable by the no-image-evidence null. If ablated/inpainted Dice ≈ intact Dice ≈ learned no-image null in the medical regime, while masks fail to track swapped-in content, the interpolator claim stands on manifold and I am silenced. **Pool note:** intervention (a) is the same instrument as P107v (B1-107 inpaint-object-out); merge or explicitly coordinate — do not spend two of 20 slots on one instrument.

**Verdict: WEAK ACCEPT** (survive to 20), conditional on the redesign and the P107v merge. The original S-014 embedding-zeroing instrument alone: REJECT.

---

## P101 — A1-101 — Prompt-embedding norm as training-free granularity knob

**Claim.** Multiplying sparse prompt-token embeddings by a scalar α monotonically steers frozen SAM between part and whole; a latent, training-free granularity control.

**Strongest reject paragraph.** The pre-registered headline experiment cannot distinguish the interesting hypothesis (granularity is *encoded* in prompt-token norm) from the boring one (norm is attention temperature). Scaling a prompt token scales its attention logits: α→0 approaches the unprompted condition, where SAM defaults to large salient wholes; α→∞ saturates attention on the point. A monotone α→mask-area curve over this range is therefore close to guaranteed by construction, and the planned success criterion (Spearman monotonicity of α vs mask area) will be met whether or not any granularity code exists. Worse, *area is not granularity*: area can grow by bleeding into background or neighboring instances — degradation, not whole-level segmentation. And with multimask output on, α modulates which of the three heads the predicted-IoU selector picks, so the apparent continuous knob may be SAM's documented discrete whole/part/subpart design observed through a selector.

**Hidden assumption.** Mask area is a proxy for position in the *same object's* part–whole hierarchy. Only nested GT can test that; area cannot.

**Confounder.** (1) IoU-head mask selection (the output head must be fixed). (2) LayerNorm inside the decoder re-normalizes the scaled token layer by layer, so the effective intervention is non-linear in α and layer-dependent — "norm" is not a clean coordinate.

**Missing baselines.** (1) Logit-threshold sweep on one fixed head — also training-free, also monotone in area, zero novelty; the comparison must be part/whole agreement at *matched mask area*. (2) Selecting among SAM's own three multimask outputs (Stage 3 already required this). (3) Direction control: rotate the prompt embedding to a random direction at identical norm — if "granularity" tracks norm regardless of direction, it is temperature, not a code. (4) GraCo (arXiv:2405.00587), if any capability claim survives.

**Why significance fails.** GraCo and Semantic-SAM own the capability. If the knob merely interpolates within/between SAM's three designed levels, the finding is a re-parameterization of known structure. The mechanism nugget matters only if it beats the trivial baselines at matched area on nested part GT (PartImageNet / PACO-class part annotations — KNOWN real datasets, verify at run time) *and* generalizes beyond one checkpoint (SAM2, HQ-SAM); otherwise it is a single-model curiosity at workshop scale.

**Can an experiment shut me up? YES**, in 1–2 GPU-days: fix the mask head; sweep α; compare against threshold-sweep and three-head-selection at matched mask area on nested part/whole GT; run the fixed-norm random-direction control; require demonstrably valid *intermediate* granularities (masks matching a genuine intermediate level that no discrete head or threshold reaches); replicate on SAM2. If α beats both trivial baselines on part/whole agreement at matched area, direction matters, and intermediates are real, the temperature explanation dies and I am silenced.

**Verdict: WEAK ACCEPT** — lowest tier; first to cut if the 20-slot quota binds. Without the matched-area baseline table: REJECT.

---

## P079 — S-079 — SAM2 memory: position vs appearance collapse

**Claim.** SAM2 memory embeddings encode position/order rather than appearance; shown by linear probes plus a causal permutation of temporal-position encodings.

**Strongest reject paragraph.** As designed, the probe rediscovers the architecture's documented inputs. SAM2's memory entries carry *explicit learned temporal-position encodings* (KNOWN FACT, code — Stage 3 already noted the small fixed set of temporal encodings in `facebookresearch/sam2`); "position is linearly decodable from memory" is therefore true by construction, and a headline to that effect is code-reading with a probe. On the appearance side the probe is confounded by the data: in videos and volumes, position and appearance are strongly correlated — adjacent slices look alike, anatomy varies smoothly with index — so slice-index decodability may be appearance leaking through and vice versa; linear probes on correlated nuisances identify nothing without decorrelation. Finally, the causal arm (permute temporal encodings, measure Dice damage) shows only that the model *uses* position — unsurprising for a tracker built on recency — not that appearance is absent, and not that positional dominance *causes* the known 3D failures.

**Hidden assumption.** That "position vs appearance" is a dichotomy recoverable by observational probes on natural sequences. It is not, absent decorrelated inputs.

**Confounder.** (1) The additive, *known* positional code — must be subtracted/regressed out before any content claim. (2) Position–appearance correlation intrinsic to natural volumes and videos. (3) Probe capacity and the memory-features-vs-object-pointer distinction (different tensors, different claims).

**Missing baselines.** (1) Identical probes on pre-memory image-encoder features — ViT positional embeddings make position decodable there too; the claim is only about memory if the position:appearance ratio *changes* at the memory bank. (2) Probe transfer across videos/volumes (generalization, not in-sequence curve-fitting). (3) Constructed decorrelation sequences — cut-together videos where appearance changes abruptly on a fixed positional schedule, and reordered-slice volumes doing the reverse.

**Why significance fails (as designed).** The fix-market already concluded that recency/order assumptions fail and shipped five replacements (MedSAM-2 arXiv:2408.00874, SAM2Long arXiv:2410.16268, SAMURAI arXiv:2411.11922, DAM4SAM arXiv:2411.17576, SLM-SAM2 arXiv:2505.01854 — all Stage-3-verified). A probe that post-hoc explains what the fixes already exploit is commentary unless the probe statistic *predicts failure* out-of-sample better than trivial covariates (slice spacing, object size, motion magnitude). Scoop risk is live (the SAM2-analysis line, arXiv:2503.00042).

**Can an experiment shut me up? YES.** Mandatory redesign: (a) regress out the known temporal encodings, probe the residual; (b) report the position:appearance information ratio at encoder vs memory — the *delta* is the claim; (c) run the constructed decorrelation sequences; (d) pre-register the predictive test: position-dominance computed on the prompted first half of a sequence must predict propagation collapse in the second half, benchmarked against the trivial covariates; (e) keep the causal permutation as the closing check. All frozen-model, cheap. If the ratio shifts toward position specifically at the memory stage after removing the explicit code, and the statistic predicts failure out-of-sample beyond covariates, I am silenced.

**Verdict: WEAK ACCEPT**, conditional on (a) and (b) being mandatory. The headline as originally designed: REJECT.

---

## P103 — S-103 — Portrait-matting pretrain → smoke transfer

**Claim.** Matting-pretrained models transfer to smoke better than COCO-segmentation-pretrained models; mechanism = shared soft-boundary structure.

**Strongest reject paragraph.** The evaluation is circular where it is measurable and unmeasurable where it is honest. The only smoke benchmarks with alpha ground truth (DS01–03 class, per Yuan et al. arXiv:1809.00774) are *synthetic alpha composites* — produced by exactly the compositing operation matting models are trained to invert. A matting-pretrained model winning alpha-MAE there demonstrates alignment with the benchmark's generative process, not transfer to smoke. On real smoke (SMOKE5K-real class), labels are binary and noisy (Stage 3's own inter-rater evidence: arXiv:2602.10858), so the soft-boundary mechanism — the entire scientific content — is untestable exactly where the claim needs to hold. Meanwhile the pretraining arms are confounded twice: (1) scale/diversity — matting corpora are ~10³–10⁴ images against 10⁵–10⁷ for segmentation pretraining, so either outcome is attributable to budget mismatch; (2) output-space alignment — the matting-pretrained network arrives with an alpha-regression head trained on alpha targets, while the COCO arm must learn one during fine-tuning; "matting wins" may reduce to "regression-head warm-start wins," which has nothing to do with smoke or soft boundaries.

**Hidden assumption.** That synthetic-composite alpha is a valid proxy for physical smoke transmittance, and that portrait/object matting boundary statistics (hair, fur — high-frequency thin geometry) resemble volumetric-media boundaries (low-frequency density ramps). Neither is established.

**Confounder.** Pretrain scale/diversity; head alignment; synthetic-GT provenance shared with the pretraining task.

**Missing baselines.** (1) **Matting-pretrain-with-binarized-labels arm** — same images, same budget, soft labels destroyed: the one arm that isolates the soft-label mechanism from data provenance. (2) Segmentation-pretrain + brief alpha-head calibration on generic synthetic composites (head-alignment control). (3) Matched-budget subsample of the segmentation corpus. (4) Dark-channel transmission floor (already planned — keep).

**Why significance fails (as designed).** "Pretrain provenance A beats B on niche domain C," without mechanism isolation, is a data point, not a law; smoke segmentation is a small field and the practitioner-actionable content ("start from a matting checkpoint") is consumed in one line.

**Can an experiment shut me up? YES.** Four-arm pretrain design {COCO-seg, matting, matting-binarized, scratch} at matched fine-tune budgets and matched pretrain image counts where feasible; **primary endpoint on real smoke** (binary IoU + boundary-F) with sample-efficiency curves; synthetic alpha metrics demoted to secondary with the circularity caveat printed in the paper. The claim lives only if the ordering matting > matting-binarized > COCO holds on real smoke at low data budgets and the gap grows as smoke data shrinks. If matting ≈ matting-binarized, the soft-boundary mechanism is dead even if the transfer helps — report that and stop.

**Verdict: WEAK ACCEPT**, conditional on the binarized arm and the real-smoke primary endpoint. As designed (alpha-MAE on synthetic composites as headline): REJECT.

---

## P063 — A1-063 + A1-067 — Refraction feature physics (glass)

**Claim.** (063) Feature-flow vs pixel-flow mismatch from two ordinary frames localizes refractive regions, training-free. (067) ViT feature displacement through glass regresses on optically predicted refraction warp (Mitsuba renders).

**Strongest reject paragraph.** For A1-063 the detector's signal is confounded with its own measurement error. Glass regions are precisely where the pixel-flow estimator's assumptions (brightness constancy, local rigidity) fail, so "foundation-feature flow disagrees with RAFT flow" fires wherever RAFT is wrong — specular highlights, motion blur, disocclusions, textureless regions — and glass co-occurs with all of them. The paper would then be measuring flow-estimator failure and rebranding it foundation-feature physics; the one baseline that tests this — RAFT forward–backward inconsistency alone, no foundation features anywhere — is absent from the Stage-3 design. For A1-067 the mechanistic regression is squeezed from both sides: refraction warps through common glassware are frequently sub-patch (<16 px), invisible to patch-quantized ViT features, so R²≈0 there is a resolution artifact, not absent physics; supra-patch warps are trackable by raw pixel correspondence, so R²>0 there is optics 101 for *any* feature, including color patches. Neither outcome says anything about representations unless the ViT is compared against a pixel-level null. Practically: Trans10K/GDD are single-image benchmarks, so the two-frame method needs re-shot or newly captured data — the headline comparison against supervised glass methods will happen on a small home-made set no reviewer will weight.

**Hidden assumption.** That frozen-ViT feature-correspondence flow is a meaningful physical observable at sub-patch scales, and that the mismatch is specific to *refraction* rather than generic non-Lambertian weirdness.

**Confounder.** Flow-estimator error spatially co-located with glass; attention context (a patch's feature moves because its *context* moved, not because its content refracted); camera-motion parallax at depth discontinuities mimicking refractive warp.

**Missing baselines.** (1) RAFT forward–backward inconsistency / flow-uncertainty alone (RAFT: Teed & Deng, ECCV 2020 — KNOWN). (2) Pixel/color-patch correspondence as the null regressor in the Mitsuba arm — the ViT claim must beat "pixels track warp." (3) Saliency and monodepth-discontinuity baselines (planned — keep). (4) The mirror/specular-metal negative control (planned — keep; it is the only thing separating this from a generic weirdness detector).

**Why significance fails (as designed).** Training-free two-frame glass detection is a capability without a customer — robotics stacks use learned models plus active sensing, and the supervised ceiling (GDNet/EBLNet line) sits far above any plausible training-free AUROC. The project's worth therefore rests entirely on the mechanism finding, which the 063-first ordering leaves unidentified.

**Can an experiment shut me up? YES — if the program is reordered.** Run A1-067 first, fully controlled: Mitsuba scenes with an IOR sweep including IOR = 1.0 twins (identical geometry/lighting, no refraction) as the within-scene control; matched camera baselines; regress per-patch feature displacement on predicted optical warp **with pixel-correspondence R² as the printed null**; the representation-science claim is the *residual structure* — where ViT features under/over-shoot the optical prediction (attention-context signature) — not raw R²; use multi-resolution feature extraction (stride/dilation) to address sub-patch blindness. Only if a feature-specific, IOR-monotone signal exists beyond the pixel null does A1-063 proceed — with the FB-inconsistency and mirror controls mandatory — as an application section, not a standalone paper.

**Verdict: WEAK ACCEPT** for the reordered program (A1-067 mechanism-first; A1-063 demoted to application). A1-063 as standalone flagship: REJECT.

---

## P060 — A1-060 — Depth-edge auto-prompts for glass

**Claim.** Monodepth depth-discontinuity boxes → SAM recovers most of manual-prompt IoU on glassware; chains two frozen models where each alone fails.

**Strongest reject paragraph.** The hypothesis has no physical content, because monocular depth is a *function of the RGB image*. Whatever edge the depth model draws at a glass boundary was computed from RGB evidence; "depth edges succeed where RGB edges fail" cannot mean depth contributes information beyond RGB — it can only mean "a large trained network extracts glass-relevant contours better than Canny," which is true of essentially any large model and is scientifically empty. The fair control is not RGB-Canny but a learned RGB boundary detector of comparable capacity; against that, the depth model's only remaining advantage is whatever glass supervision leaked into its training corpus — at which point the chain is a weakly-supervised glass detector assembled by accident, not "two frozen models where each alone fails." The design also hides its degrees of freedom in the unsolved middle step: edge maps do not give instances, and the edge→box grouping (contour closure, thresholds, NMS) will be tuned on Trans10K — training in disguise under a training-free banner.

**Hidden assumption.** That depth *edges* are reliable on glass while depth *values* are not. Untested, and for clean transparent glass modern monodepth (Depth Anything class — KNOWN) often reports the background's depth straight through, yielding *no* boundary at the glass surface; the edge that does appear sits at the frame — which is an RGB edge.

**Confounder.** Glass supervision inside the depth model's training data; grouping-heuristic tuning; glass-type mix (framed vs frameless) dominating aggregate numbers.

**Missing baselines.** Learned RGB boundary detector at matched capacity; SAM automatic-mask-generator + transparency scoring; a 100-label weakly-supervised detector (if that beats the chain, the zero-training constraint is theater); supervised ceiling (GDNet / EBLNet — planned).

**Why significance fails.** Even the best outcome — recovering "most of manual-prompt IoU" — recovers most of a number Han et al. (arXiv:2305.00278) showed is poor. The deliverable is a systems note in a niche with an existing supervised solution and no deployment story for the zero-training constraint. Stage 3 itself graded it junior-scope; at 50→20, junior-scope is fatal.

**Can an experiment shut me up? NO.** The learned-RGB-boundary control is realistic to run — but any *positive* outcome remains attributable to "bigger trained model finds contours better than a filter," because monodepth is RGB-derived; no experiment in this design can make depth edges carry information beyond RGB, and the significance ceiling (systems note) is not experiment-addressable. → KILL.

**Verdict: REJECT.**

---

## P001 — C1-001 — SA-1B ↔ benchmark near-duplicate leakage audit

**Claim.** SSCD/pHash near-dup retrieval between SA-1B and SA-23 / COCO / LVIS / DAVIS vals; if overlap exists, zero-shot SAM numbers are inflated.

**Strongest reject paragraph.** This is a lottery ticket priced as a project. The modal outcome is null — SA-1B's licensed-photo-provider provenance (Stage-3-noted, from the SAM paper) makes benchmark overlap structurally unlikely, and Stage 3 already conceded "a null here is a tweet, not a paper." The positive branch is weaker than advertised: near-duplication is not contamination-caused inflation. Overlapped images are not exchangeable with clean ones — photographic style, scene type, and difficulty differ — so "overlapped subset scores higher than clean subset" is confounded by difficulty from the start. Establishing *inflation* requires matched-difficulty controls and, more fundamentally, a *relative* claim: SAM's margin over baselines must shrink on clean subsets — but the baselines carry their own contamination with COCO/LVIS training data, collapsing the comparison lattice. Technically the audit is not even clean: SA-1B was released downscaled with face/license-plate blurring (KNOWN FACT, dataset card — verify at run time), which perturbs both pHash and SSCD retrieval against benchmark originals; the measured overlap is a lower bound with unknown miss rate, and at 11M × val-set scale, false-positive near-dups (landmarks, sunsets, stock scenes) demand manual adjudication the "kills-or-dies-in-days" budget ignores.

**Hidden assumption.** That overlap, if found, causally explains score differences rather than shared-difficulty confounding; that dedup tooling calibrated on web scrapes (Webster et al., arXiv:2303.12733 genre) transfers to blurred, downscaled licensed imagery.

**Confounder.** Difficulty non-exchangeability of duplicate images; baseline contamination symmetric with SAM contamination.

**Missing baselines.** Matched-difficulty clean control subsets; a positive-control calibration run — inject known duplicates at known transformation levels (downscale + blur) to estimate retrieval recall under SA-1B-style processing before believing any overlap rate.

**Why significance fails.** SAM's zero-shot claims do not rest on margins small enough for plausible overlap rates (<1%) to overturn; even a confirmed overlap yields "numbers move ε on subset X" — a correction footnote. The only world where this is a paper is a large, verified, difficulty-controlled overlap that *reverses a margin* — a conjunction of unlikelihoods.

**Can an experiment shut me up? NO** — my attack is on the payoff distribution, not on the method. The audit is competently designed and cheap; no experimental refinement changes the fact that its modal and median outcomes are unpublishable. Exactly as Stage 3 said: gating audit, not flagship. Run it as pre-registered hygiene (with the existing ≥0.5% stop rule) inside whichever eval paper survives; do not spend a Top-20 slot on it. → KILL as a project.

**Verdict: REJECT** (as a Top-20 project; retain as an internal hygiene gate).

---

## P004 — A1-004 — Topology/holes: prior vs convention vs postprocess decomposition

**Claim.** Three-way causal decomposition of SAM's missing genus>0 masks — decoder prior vs annotation convention vs postprocessing — via raw logits evaluated on COCO-ReM's genuinely-holed GT.

**Strongest reject paragraph.** Two of the three arms are already answered in public artifacts, and the third is unidentifiable without a forbidden intervention. Postprocessing: SAM's released pipeline fills holes below an area threshold (KNOWN FACT, code — `min_mask_region_area`); documenting that is code-reading, not research. Convention: COCO-ReM (arXiv:2403.18819) already established that COCO-2017 GT contained zero true holes, so no COCO-trained or COCO-evaluated model is rewarded for genus>0 output — published. The remaining arm, "decoder prior," has no independent mechanistic content: SAM's mask head is a per-pixel dot-product readout that can represent arbitrary spatial patterns, so there is no *architectural* obstruction to holes; any hole-aversion is training-label statistics. And the provenance of those statistics is the killer: SA-1B's final-stage masks were generated by the model pipeline itself (the data engine's fully automatic stage, per the SAM paper) with hole-filling in the loop — so "decoder prior" and "label convention" are the same variable at one remove. Separating them requires retraining SAM on hole-preserving labels — a new foundation pretrain, which the survival rules forbid. The remaining observational move (negative click inside the donut hole: can SAM emit genus>0 at all?) is a one-figure capability check that is a footnote whichever way it lands.

**Hidden assumption.** That prior/convention/postprocess are separable by evaluation-only experiments. They are not: the interesting split (architecture vs training statistics) needs interventions on training.

**Confounder.** SA-1B label provenance (model-annotated, hole-filled) collapses two arms of the decomposition into one.

**Missing baselines.** Topology-capable baselines under the identical raw-logit protocol (U-Net, clDice-line methods) — though supplying them only sharpens a comparison whose conclusion (SAM under-represents holes; the causes are documented) is already assembled from published parts.

**Why significance fails.** Topology-aware segmentation owns the metrics and the fixes (Hu et al. NeurIPS 2019; clDice CVPR 2021 — Stage-3-verified); COCO-ReM owns the GT diagnosis; SAM's code owns the postprocessing confession. A paper gluing these into a "decomposition" contributes attribution bookkeeping on a behavior nobody disputes, delivers no fix and no capability, and its practitioner-actionable content — "disable hole-filling and don't trust COCO-style GT" — is two sentences.

**Can an experiment shut me up? NO** within allowed budgets. The only experiment that would isolate a genuine decoder prior from label convention is retraining on hole-preserving labels (new pretrain → forbidden by rule). Everything runnable — raw-logit eval on COCO-ReM, negative-click probes — leaves the attack intact because both outcomes are footnotes. → KILL.

**Verdict: REJECT.**

---

## P007 — S-007 — Scorer validity of test-time prompt evolution

**Claim (Stage-3 mutated form).** Audit across unsupervised scorer families (CRF energy, NCut, predicted-IoU head, learned regressors) × datasets: when do test-time prompt-evolution proxies anti-correlate with clinical Dice.

**Strongest reject paragraph.** This is a survey of Goodhart's law in a niche with one inhabitant. The qualitative conclusion — unsupervised quality proxies can be maximized away from the clinical target — is conceded *in the target paper itself*: SAMPOT's own failure analysis (arXiv:2310.17128, Stage-3-verified) reports the optimized prompt drifting out of the lung field because the scorer prefers wrong high-scoring masks. What the audit adds is an enumeration over an unbounded design space: scorer families × datasets × evolution operators have no natural boundary, so any reported "regime map" is a sample the authors chose — a different scorer or dataset can always be added or removed — and "when does it invert" has no out-of-sample content unless a *predictive law* is pre-registered (a measurable scene statistic forecasting inversion before the optimizer runs). Stage 1 flagged exactly this failure mode: "scorer choice cherry-pick." Absent the law, the deliverable is a table of anecdotes with confidence intervals.

**Hidden assumption.** That "scorer validity" is a stable property of the scorer, rather than of the scorer × image-statistics × optimizer-budget interaction. If the latter, the audit's cells do not transfer and the map is dataset-bound.

**Confounder.** Optimizer strength: a weak optimizer fails to exploit any scorer (everything looks safe); a strong one breaks all of them (everything looks unsafe). Apparent scorer differences may be optimization-budget artifacts unless budgets are equalized and pre-registered.

**Missing baselines.** Random-walk prompt perturbation at matched step budget (present in the original S-007 sketch — must stay); a small *supervised* IoU-regressor scorer as the ceiling, bounding what any proxy could achieve.

**Why significance fails.** Test-time prompt evolution is not deployed practice; its published corpus is essentially SAMPOT. A rigorous negative audit of a method nobody uses protects nobody — "who is wrong if we're right" returns approximately one author team, who already agreed with the finding in their own failure analysis. Executed perfectly, the venue ceiling is a negative-results workshop track.

**Can an experiment shut me up? NO** as scoped. The rescue exists in principle — pre-register a scene-statistic predictor of scorer inversion and validate it out-of-sample, tying into predicted-IoU miscalibration — but that is a different, harder paper (failure *prediction*), it belongs inside the P031 calibration/IoU-head cluster, and it inherits the niche's significance ceiling either way. The audit as proposed cannot answer "unbounded design space + known conclusion + no customer" with any experiment. → KILL; fold the predicted-IoU-miscalibration fragment into P031.

**Verdict: REJECT.**

---

## Set-A verdict table

| Project | IDs | Core attack | Experiment silences it? | Verdict |
|---|---|---|---|---|
| P14 | S-014/S-604 | Off-manifold intervention + positional leakage + degenerate-task alternative | YES — on-manifold counterfactuals (inpaint/swap), prompt-only & learned box→mask nulls, medical primary endpoint | **WEAK ACCEPT** (merge with P107v) |
| P101 | A1-101 | Attention-temperature artifact; area ≠ granularity; head-selection confound | YES — matched-area vs threshold-sweep & 3-head baselines, direction control, nested GT | **WEAK ACCEPT** (lowest tier) |
| P079 | S-079 | Probe rediscovers explicit positional code; position–appearance correlation | YES — subtract known encodings, encoder-vs-memory ratio delta, decorrelated sequences, out-of-sample failure prediction | **WEAK ACCEPT** (conditional) |
| P103 | S-103 | Synthetic-alpha circularity; pretrain-scale & head-alignment confounds | YES — binarized-matting arm, real-smoke primary endpoint, matched budgets | **WEAK ACCEPT** (conditional) |
| P063 | A1-063/A1-067 | Flow-error confound (063); sub-patch/pixel-null squeeze (067) | YES — 067-first with IOR=1.0 twins + pixel-correspondence null; 063 demoted to application with FB-inconsistency & mirror controls | **WEAK ACCEPT** (restructured) |
| P060 | A1-060 | Monodepth is RGB-derived ⇒ no information beyond RGB possible; junior-scope ceiling | NO — any positive is "big model beats Canny"; significance not experiment-addressable | **REJECT** |
| P001 | C1-001 | Modal outcome null; positive branch difficulty-confounded; ε-sized stakes | NO — attack is on the payoff distribution, not the method | **REJECT** (keep as hygiene gate) |
| P004 | A1-004 | Two arms already published; prior-vs-convention split needs retraining SAM (forbidden) | NO — identification requires new foundation pretrain | **REJECT** |
| P007 | S-007 | Goodhart survey, unbounded design space, one-paper niche, conclusion pre-conceded | NO — rescue is a different paper inside P031; significance ceiling immovable | **REJECT** |

## Consequences for the pool (supervisor notes)

1. **Slot arithmetic.** Set A: 5 survive / 4 die. If the global 20-slot quota binds after Set B/C reviews, cut my accepts in this order: P101 first, P103 second — both are lowest-tier conditional accepts.
2. **Merge P14 into/with P107v.** The redesigned P14 and B1-107 share the inpaint-object-out instrument. One paper, one slot. Failing to merge wastes a slot and invites a self-scoop.
3. **Glass program shrinks from 3 slots to 1.** A1-067-led mechanism paper with A1-063 as its application section; A1-060 dead. The pool should not carry "glass" as a theme — it carries one representation-physics question.
4. **P007's residue** (predicted-IoU miscalibration as an unsafe optimization target) belongs inside P031 (C1-031 calibration cluster), not as a standalone.
5. **P001 stays in the process, out of the Top 20:** pre-registered hygiene gate with the Stage-3 stop rule (≥0.5% overlap → escalate; else one paragraph in an eval-hygiene appendix).
6. **Pattern warning for Set B/C reviewers:** three of my four kills failed the same test — the *positive* branch of the experiment was not publishable (P060: attributable to model scale; P001: ε-stakes; P004: attribution bookkeeping). Check every remaining project's best-case outcome, not just its falsifiability.
