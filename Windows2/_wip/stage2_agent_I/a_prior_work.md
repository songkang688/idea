# Batch A Prior-Work Attacks (Agent I)

Agent I (merger + novelty assassin for batch A; **not PI, no final-3**). Date: 2026-08-28.

Agent F's `prior_work_attack.md` was **not present** when this merge started (F's directory contained only `shortlist.md`, `scores.jsonl`, `kills.md`, `parts/`). Per mission, I ran my own web prior-work attacks on **all 17 F Tier A ideas** plus every A keep that touches a G LOCK or a predicted collision cluster. Every citation below is a real, web-verified paper (title-level identity confirmed); where I could not verify a specific paper I say so rather than invent one.

**F's attack file and Stage-4 Agent J's `verdicts.jsonl` were pushed while this fold was in flight; Part 5 reconciles my verdicts with theirs and supersedes Parts 1–4 where they conflict.**

Verdict key: **LOCK** = survives with full claim · **KEEP (FLEX)** = survives, competes on merit · **MUTATE** = survives only with the demoted/refocused claim stated · **MERGE→host** = content survives as a named arm, no slot · **KILL** = literature occupies the territory.

---

## Part 1 — F Tier A (17 ideas)

### W2-A-0074 — Volume measurements inherit uncalibrated uncertainty from segmentation
- **Searched:** conformal/evidential uncertainty for segmentation-derived volumetry; tumor-volume confidence intervals.
- **Found:** Conformal prediction for volume assessment is now an active line: prostate-volume CP on multi-center MRI (*Insights into Imaging* 2024, DOI 10.1186/s13244-024-01863-w); **COMPASS** (arXiv:2509.22240) builds CP intervals directly for downstream segmentation metrics such as organ size, with validity proofs; **CONSeg** (AJNR 2025) voxelwise CP for glioma; split-conformal patient-level PSMA tumor-volume intervals (JNM 2026 supplement). The *construction* of volume CIs is no longer open.
- **Verdict: MUTATE → KEEP (FLEX).** The surviving claim is the **diagnostic** one none of these papers test: naive volume CIs derived from voxelwise/independence assumptions are **anti-conservative because boundary errors are spatially correlated**, and the synthetic-lesion anchor can measure by how much. Position explicitly against COMPASS/CONSeg as the audit of their assumptions, not a rival CI method. Novelty demoted from "first volume CI" to "first validity audit of volume CIs under correlated boundary error".

### W2-A-0121 — Puddles are mirrors: phantom-object segmentation in driving scenes
- **Searched:** water-hazard/puddle detection; mirror/reflection segmentation; reflection-induced false positives in driving.
- **Found:** Robotics water-hazard/puddle detection exists (reflection-based wet-surface detection); mirror segmentation is established (MirrorNet line, ICCV 2019 onward). No paper measures **phantom-object rates in standard segmentation models on wet roads with geometric verification via road-plane mirror symmetry**.
- **Verdict: LOCK.** The mirror-symmetry verification instrument and the metric-invisible safety error class are unclaimed. Must cite mirror-segmentation and water-hazard lines as adjacent, not competing.

### W2-A-0148 — Human-AI teaming for camouflage search; binary masks are the worst output format
- **Searched:** human-AI team complementarity; AI-assisted visual search; uncertainty visualization for detection aids.
- **Found:** Human-AI complementarity literature is mature (e.g., Bansal et al., CHI 2021, "Does the whole exceed its parts?"); automation-bias classics (Parasuraman & Riley 1997). No study anchors on **camouflage search with mask-format as the manipulated variable**.
- **Verdict: KEEP (FLEX).** The causal claim "binary masks anchor and net-hurt teaming vs uncertainty-bearing formats" in a search task is open; the general complementarity result is not. Cite the HCI line as the frame, claim only the format effect.

### W2-A-0150 — Boundary GT is scale-relative: correct boundaries drift with viewing resolution
- **Searched:** annotation scale/zoom effects; resolution-dependent ground truth; boundary evaluation at multiple scales.
- **Found:** Boundary-quality metrics exist (Boundary IoU, CVPR 2021); annotation-variability studies exist; I found **no paper establishing a systematic, directional scale-dependence of the annotated boundary itself** with interface-controlled re-annotation.
- **Verdict: LOCK.** Interface controls (zoom fixed vs free) are mandatory, as F noted.

### W2-A-0163 — Stuff-stuff boundaries are measure-zero fictions (transition bands)
- **Searched:** transition zones in segmentation GT; matting trimaps; band-based evaluation.
- **Found:** Trimap/unknown-band machinery exists in matting; boundary-tolerance bands exist inside metrics (BF-score, Boundary IoU tolerance). Nobody has (a) measured multi-annotator **band width distributions per class pair** for stuff-stuff transitions or (b) proposed band-aware GT as the label model.
- **Verdict: LOCK.** The ontological claim + cheap multi-annotator test survive; metric-tolerance prior work must be cited as implicit acknowledgment, not resolution.

### W2-A-0175 — Photographed printed calibration shapes as zero-annotation boundary GT
- **Searched:** physical calibration targets for segmentation evaluation; sub-pixel edge metrology benchmarks.
- **Found:** Calibration targets (checkerboard/ChArUco) and sub-pixel edge localization (Devernay-style) are classical **camera-calibration** tools; no segmentation benchmark uses printed geometry to obtain camera-true sub-pixel boundary GT below annotation noise.
- **Verdict: LOCK.** Flagship metrology instrument; the ecological-validity objection is pre-answered by textured/embedded variants. Pairs with A-0276 (scaling exponents need a noise-free boundary reference).

### W2-A-0199 — Rare-context hallucination: models paint plausible-but-absent stuff
- **Searched:** context bias/shortcut literature; background reliance; hallucination in dense prediction.
- **Found:** Context reliance is established at the classification/detection level (elephant-in-the-room transplant effects, Rosenfeld et al. 2018; background reliance, Xiao et al. 2020 "Noise or Signal"). Segmentation-specific, **dose-response by context-association strength on real scenes** (dry canals, drained pools) is not published.
- **Verdict: MUTATE → KEEP (FLEX).** Demote "context overrides evidence" (known) to background; the quantified association-strength dose-response curve + curated real-scene corpus is the paper.

### W2-A-0205 — Verification bias: annotators accept wrong-but-plausible machine masks
- **Searched:** automation bias in annotation; AI-assisted labeling acceptance; label-noise correlation structure.
- **Found:** Automation bias is established in human factors; model-assisted annotation pipelines are everywhere (SAM/SAM2 data engines describe accept/refine loops). I found **no measurement of acceptance rates for wrong-but-plausible masks, nor any test that accepted errors are correlated with model style and inherited by students trained on verified labels**.
- **Verdict: LOCK.** Core of the inbreeding thesis with A-0206. The correlated-contamination claim breaks the independence assumption of the label-noise literature — that framing survives attack.

### W2-A-0206 — Detect the SAM fingerprint in datasets annotated with SAM assistance
- **Searched:** machine-generated mask detection; annotation provenance forensics; model attribution for segmentation.
- **Found:** Provenance work is **metadata engineering** (C2PA-style manifests, audit-trail annotation tools) — it assumes cooperation. Model-attribution forensics exists for generated **images** (GAN fingerprints line, ICCV 2019 onward) but not for **mask geometry/boundary style**. Nothing detects SAM assistance post hoc from the masks themselves.
- **Verdict: LOCK.** Flagship of the data-genetics agenda. Hosts A-0264 (error anatomy) as its constructive arm. Cite GAN-fingerprint literature as the methodological template.

### W2-A-0237 — Annotation-convention shift masquerades as domain shift
- **Searched:** cross-dataset label convention studies; dataset bias; re-annotation experiments in UDA.
- **Found:** Dataset bias is classical (Torralba & Efros 2011); label-convention drift is documented within-dataset (COCO-ReM's error inventory; "Label Convergence" line already flagged by G). The specific decomposition — **what fraction of a measured cross-country domain gap is label-sociology, testable with ~300 re-annotations under both conventions** — is unclaimed.
- **Verdict: KEEP (FLEX), host.** Hosts A-0249 (target-label quality asymmetry) and absorbs G's **C-0208** ("label conventions are a domain", incl. its 0014/0134 arms) — same thesis, A's version has the sharper falsifiable figure (>25% of gap) and the UDA-credit-assignment consequence.

### W2-A-0249 — Domain gap is partly an annotation-quality gap
- **Searched:** target-domain label quality; benchmark noise asymmetry in UDA.
- **Found:** No direct measurement of reference-quality asymmetry inflating measured shift.
- **Verdict: MERGE→A-0237.** Same experimental infrastructure (dual-convention/quality re-annotation); lives as the quality-asymmetry arm with its no-reannotation diagnostic.

### W2-A-0300 — Ensemble gains are collapsing generation by generation
- **Searched:** ensemble diversity decline; model convergence/homogenization; deep-ensemble diversity.
- **Found:** Ensemble diversity theory is mature (deep-ensembles loss-landscape line, Fort et al. 2019); "algorithmic monoculture" and model-similarity papers exist for classifiers. The longitudinal, era-cohorted **dense-prediction** measurement is unclaimed but is one number away from being an arm, not a paper.
- **Verdict: MUTATE + MERGE→A-0290.** Survives as the temporal-trend arm of A-0290 (shared blind spots across the zoo): same model-zoo inference infrastructure, same monoculture thesis; scale-matched cohorts control the era-vs-scale confound.

### W2-A-0326 — "More context always helps" is false for boundaries
- **Searched:** effective receptive field; context ablation for segmentation; crop-size effects.
- **Found:** Effective receptive-field analysis (Luo et al., NeurIPS 2016) and qualitative "context can hurt locally" observations exist; crop-size/context sweeps appear in training-recipe papers as tuning, never as **signed, property-resolved context-value curves** (boundary precision vs region accuracy separately).
- **Verdict: MUTATE → KEEP (FLEX).** Reposition as measurement science: the field's qualitative suspicion becomes a quantified, per-property curve with the retrained-variant arm answering the off-manifold objection. Monotonicity-assumption framing stays.

### W2-A-0331 — Dice's gradient pathology on multi-instance images
- **Searched:** instance imbalance in Dice; per-lesion loss weighting; Dice gradient analysis.
- **Found (kill):** **blob loss** (Kofler et al., arXiv:2205.08209) states and fixes exactly this: "a large foreground instance can dominate minor instances and still produce a satisfactory DSC", with per-instance loss terms and MS-lesion/liver/microscopy gains. Successors (**ICI loss**, arXiv:2304.06229; CC-DiceCE line) extend it. The mechanism is identified, named, and has a fix family; a diagnosis-only paper would be reviewed as a blob-loss ablation.
- **Verdict: KILL.** Gradient-flow instrumentation adds decimal places to a published mechanism. (F ranked this top-5; the literature disagrees.)

### W2-A-0334 — Class-agnostic masks leak semantics; privacy consequences
- **Searched:** silhouette/shape-only recognition; classification from binary masks; mask privacy.
- **Found:** Shape-only recognition is established as a *capability* (silhouette CNN classification; ASA-Net, Neurocomputing 2022; FSSD few-shot shape descriptors, arXiv:2312.01315). Nobody has quantified **leakage at dataset scale as a privacy/"semantic-free"-claim problem** (scene/activity recovery from "anonymized" masks).
- **Verdict: LOCK, with the mechanism claim demoted.** "Shape predicts category" is known; "how much semantics leaks through published mask corpora, and what that does to privacy claims" is the paper. Absorbs G's **C-0333** ("silhouettes are almost enough: shape suffices for most detection classes") as its capability-measurement arm — same territory, A-0334 carries the larger claim set.

### W2-A-0349 — Human boundary conventions encode function, not photometry
- **Searched:** affordance segmentation; boundary semantics; annotation instructions vs image evidence.
- **Found:** Affordance segmentation datasets exist (IIT-AFF line); annotation-instruction effects are documented qualitatively. The **signed per-junction-type offset between model (photometric) and human (functional) boundary placement** is unmeasured.
- **Verdict: LOCK.** Deepest annotation-theory idea in the batch; affordance literature disciplines the taxonomy rather than preempting the measurement.

### W2-A-0352 — Segmentation-free measurement: regression beats segment-then-measure
- **Searched:** direct regression of clinical measurements; segmentation-free volumetry/EF estimation.
- **Found (kill):** Segmentation-free direct regression is an established, repeatedly-published paradigm in medical imaging: 3D-CNN LVEF regression from cine-MRI reaching cardiologist-comparable reliability (*Biomedicines* 2024, "Segmentation-Free Estimation of LVEF Using 3D CNN"; *Sensors* 2023 LV/RV EF 3D-CNN), video-transformer EF regressors (ViViEchoformer, 2024), plus EchoNet-style video EF regression. The "mask is an unnecessary middleman" question has answers in the highest-value domain.
- **Verdict: KILL.** The matched-budget three-task comparison is incremental over an existing paradigm. The residual auditability-aware **decision rule** (when a consumer should demand a mask) survives as a framing note inside A-0337's metric→downstream validity study, no slot.

---

## Part 2 — Collision-relevant A keeps and merges

### W2-A-0341 — Prompt sensitivity increases with scale on ambiguous objects
- **Found:** Prompt-robustness work exists (RClicks, NeurIPS 2024, real-click distributions — already used to kill B-0175); G's portfolio holds B-0169 (negative-click dose-response), B-0194 (sycophancy), and **B-0182 (scale increases prompt sensitivity on rare classes — text prompts)**. No paper tests the sign-splitting scale×ambiguity interaction for **visual** prompts with a controlled mini-SAM series.
- **Verdict: KEEP (FLEX).** Modality split vs B-0182 (visual clicks vs text templates), mechanism split vs B-0169/0194 (granularity-hypothesis flipping vs dose-response/sycophancy). Mandatory cross-citation; see `collisions_AFG.md` §1.

### W2-A-0301 — Did SA-1B swallow the test sets? Contamination forensics
- **Found:** NLP contamination auditing is a template; dense-prediction lacks the audit. G holds C-0345 (foundation-model test-set exposure) — same question, thinner instrument.
- **Verdict: KEEP (FLEX), host.** Absorbs **C-0345** as the exposure-tracking arm; closed-corpus honesty bounds stated. Counts against the 5-slot contamination cap.

### W2-A-0245 — UDA methods overfit their development pair (rank correlation)
- **Found:** The reality-check genre exists in classification (Musgrave et al., ECCV 2020, metric learning); G LOCK **C-0150** is the UDA reckoning host.
- **Verdict: MERGE→C-0150.** Cross-pair rank-stability becomes an arm of C-0150's instrument set; a standalone would split one referee-facing story into two.

### W2-A-0164 — Tiny-object SOTA below the annotation noise floor
- **Found:** G LOCK **C-0007** is the same instrument ("tiny-object annotation-noise floor", census-confirmed unclaimed). Near-duplicate across batches.
- **Verdict: MERGE→C-0007.** A's jitter-propagation derivation of minimum-evaluable-object-size becomes the method arm.

### W2-A-0071 — Leaderboards above the inter-rater ceiling
- **Found:** Single-dataset inter-rater studies are standard (LIDC, QUBIQ multi-rater data); the **multi-leaderboard audit + style-vs-anatomy decomposition** is not.
- **Verdict: MUTATE → KEEP (FLEX).** Claim only the ecosystem-level audit; single-dataset ceilings are known.

### W2-A-0075 — Consensus fusion erases correct minority experts
- **Found:** STAPLE (Warfield et al., IEEE TMI 2004) and theoretical critiques of consensus fusion exist; **outcome-anchored** verification (minority detections validated against clinical outcomes on rare pathologies) is unclaimed.
- **Verdict: KEEP (FLEX), HRHR protection honored.** Data access remains the honest wall.

### W2-A-0313 — Statistical power audit of segmentation SOTA claims
- **Found:** Genre template exists (Musgrave; classification reality checks). G LOCK **C-0302** is the rigor-infrastructure flagship (MDE/power tables, claims re-analysis).
- **Verdict: MERGE→C-0302.** Segmentation-specific bootstrap re-analysis becomes a named arm; keeping both would be two power audits in one portfolio.

### W2-A-0322 — Reproduction noise floor mined from the literature
- **Found:** G FLEX **C-0300** (reproduction-gap meta-analysis, hosts 0304-C) covers the same mined-from-papers spread.
- **Verdict: MERGE→C-0300.** A's citation-provenance tracking improves the host's method; zero-GPU virtue preserved inside the host.

### W2-A-0228 — Night failure is mostly ISP failure
- **Found:** G FLEX **C-0212** ("night is an ISP artifact") is the same attribution claim from batch C.
- **Verdict: MERGE→C-0212.** A's RAW-domain evaluation design and vendor-varying recovered-fraction headline become the execution arm of the host.

### W2-A-0305 — Effective headroom estimation per benchmark
- **Found:** G LOCK **C-0326** (powered adjudication of residual COCO errors — share that is GT problems) measures the same quantity on COCO with better feasibility (ReM error inventory).
- **Verdict: MERGE→C-0326.** A's multi-benchmark headroom table generalizes the host's protocol; the sociological prediction rides along.

### W2-A-0100 — Deduplicate smoke/fire benchmarks by video provenance
- **Found:** Provenance-leakage audit genre exists in other domains; G LOCK **C-0122** is the train-test duplication census.
- **Verdict: MERGE→C-0122.** Smoke/fire same-event-video leakage becomes a domain arm of the census.

### W2-A-0323 — Measure human mIoU baselines
- **Found:** G LOCK **C-0338** (human small-object ceiling, LVIS double annotations public) already owns the human-ceiling instrument.
- **Verdict: MERGE→C-0338.** A's crossing-profile framing (humans below SOTA on convention-diligence, above on ambiguity) becomes the general-classes arm.

### W2-A-0198 — Seed-churn maps as a free ambiguity atlas
- **Found:** Churn is published for classification; G LOCK **C-0311** is the metrology-grade uncertainty budget host (already carries bootstrap, noise-derived thresholds, framework variance).
- **Verdict: MERGE→C-0311.** Dense churn + the gains-concentrate-on-churn-pixels audit becomes the model-variance arm of the uncertainty budget.

### W2-A-0264 — SAM pseudo-label error anatomy
- **Verdict: MERGE→A-0206** (constructive companion arm; itemized anatomy + inheritance measurement inside the fingerprint paper).

### W2-A-0026 — Masklet drift predictable from first-frame ambiguity
- **Found:** SAM2 failure modes are described qualitatively in the SAM 2 paper's own analysis; no static-predicts-temporal law.
- **Verdict: MUTATE → KEEP (FLEX) as unit host.** Forms the SAM-failure-prediction unit; hosts the **C-0082-mut** failure-scaling law G predicted would re-enter via A (collision #6), plus optional arms from cut 0029 (erosion bias) / 0043 (absorbing states). Occlusion-event dominance stays the honest failure mode.

### W2-A-0337 — Mask metrics don't predict task success
- **Found:** Metric-validity concern is voiced everywhere, measured nowhere with instrumented consumers; G FLEX **C-0078** (AP vs downstream utility, $) is the detection twin.
- **Verdict: KEEP (FLEX), host.** Absorbs **C-0078** as the detection arm; also carries A-0352's residual decision-rule framing. One metric→downstream validity program, not two.

### W2-A-0312 — Masks reveal their dataset (annotation-style dialects)
- **Found:** No mask-dialect classifier published; adjacent to A-0206 (model fingerprint) but the target differs (dataset sociology vs model provenance).
- **Verdict: KEEP (FLEX).** Outside the contamination cap (not SAM/SA-1B-specific); mandatory cross-citation with A-0206.

### W2-A-0195 — Sub-10-example classes are retrieval, not generalization
- **Found:** Memorization/nearest-neighbor tests exist for classification; the tail-of-segmentation audit is unclaimed.
- **Verdict: KEEP (FLEX).** Embedding-choice replication is the methodological demand.

### W2-A-0152 / W2-A-0151 / W2-A-0321 / W2-A-0268 / W2-A-0351 / W2-A-0061
- **0152** size-stratified leaderboard flips: inference-only, no direct prior found — **KEEP (FLEX)**.
- **0151** three-way boundary error decomposition: distinct from C-0311 (COCO AP budget) by metric family and community; shares metrology infrastructure — **KEEP (FLEX)**, cross-referenced.
- **0321** LVIS rare-class CIs: nearly-free statistics, unclaimed — **KEEP (FLEX)**.
- **0268** SSL-for-segmentation under DINOv2-grade features: re-baselining genre exists (which strengthens the method); pre-registration discipline required — **KEEP (FLEX)**.
- **0351** two-annotator myth (multi-modal disagreement): foundational annotation theory, no dense-panel remeasurement found — **KEEP (FLEX)**, HRHR honored.
- **0061** Dice-topology Pareto (checkpoint-selection claim): clDice line exists and is cited as the frame; the checkpoint-selection-time claim is new — **KEEP (FLEX)**.

---

## Part 3 — Kills of F keeps outside Tier A (literature)

### W2-A-0272 — Layered design files (PSD/SVG) as the largest untapped mask corpus
- **Found (kill):** The corpus is no longer untapped: **CreativePSD** (PSDesigner, arXiv:2603.25738 — "first design dataset based on the PSD format", 10k+ layer-annotated files), **LICA** (arXiv:2603.16098 — 1.55M layered compositions with per-layer geometry), OmniPSD's ~200k-PSD collection, plus Graphic-Design-Bench built on LICA. The harvesting/licensing recipe and layer-semantics grouping are published.
- **Verdict: KILL.** The residual claim ("design layers pretrain **natural-image** segmentation") was A's own weakest leg — design-layer boundaries are synthetic-composited, not photographic occlusion boundaries — and does not survive as a standalone once the corpus-novelty is gone.

### W2-A-0017 — SA-1B imprinted a compact-region prior; wiry objects structurally outside output space
- **Found (kill):** Zhang, Konz, Kramer & Mazurowski, **"Quantifying the Limits of Segmentation Foundation Models"** (WACV 2026, arXiv:2412.04243): tree-like/thin-structure failure quantified across SAM/SAM 2/HQ-SAM with interpretable metrics, attributed to **textural confusion, with targeted fine-tuning failing to resolve it — "indicating a fundamental limitation"** (architectural, not data-genetic). It also directly discusses SA-1B's low object concavity. The paper both occupies the territory and evidences against 0017's causal story: F's own condition ("needs the fine-tune causal leg to beat correlation reviews") is answered in the negative by published fine-tuning results.
- **Verdict: KILL.**

### W2-A-0107 — Depth-sensor dropout as free glass supervision at fleet scale
- **Found (kill):** LiDAR glass detection from invalid/no-return + intensity + multi-echo cues is established: Foster et al. glass mapping & reflectance-field maps; **TOPGN** (arXiv:2408.05608) real-time transparent-obstacle detection from intensity; **GRAR** (arXiv:2606.10541) explicitly exploits the "measurement void" of glass and fuses it with a vision foundation model to produce glass masks with completion of no-return regions. Self-supervised auto-labeling from LiDAR without humans is likewise mature (LISO, ECCV 2024; OYSTER, 2023).
- **Verdict: KILL.** The fleet-scale filtering recipe is engineering on top of published cues.

---

## Part 4 — Attack notes on tier-2 rescues admitted to the 200

Rescues were re-screened against the same threat map before admission; three were merged instead of slotted:

- **A-0003** (patch-grid aliasing causes SAM thin-structure failure): collides with G FLEX **B-0018** (thin-structure Nyquist law) and with the WACV 2026 limits paper above. The causal **phase-sweep** design is the only unclaimed piece → **MERGE→B-0018** as its causal arm. Not a slot.
- **A-0153** (bilinear-decoder sharpness floor): collides with G FLEX **B-0203** (post-upsampler residual decomposition, FeatUp-aware) → **MERGE→B-0203** as the analytic-floor arm. Not a slot.
- **A-0220** (noisy-many vs precise-few exchange rate): collides with G FLEX **C-0115** (quality-vs-quantity exchange rate) → **MERGE→C-0115** as the mask-precision-threshold arm. Not a slot.
- **A-0065** (clinician-click sim2real gap): RClicks (NeurIPS 2024) owns realistic clicks for natural images — admitted **only** with the clinician-corpus + method-reordering claim; RClicks cited as the instrument being ported, MICCAI-facing.
- **A-0239** (compression asymmetry, inverted shift): no paper tests the benchmark-compressed/deployment-raw direction; admitted with codec-matrix scope.
- **A-0025** (topology bias from training statistics): cleanest single data-genetics mechanism; fine-tune causal leg is what the WACV 2026 paper lacks for topology (it tested texture confusion, not hole-filling) — admitted.
- **A-0315** (patient-level leakage): individual incidents are known; the ecosystem-scale anatomical-fingerprint audit is not — admitted; sits outside the contamination cap (medical hygiene, not SAM lineage) but must cross-cite C-0122.
- **A-0034** (VOS oracle smoother), **A-0309** (PQ matching cliff), **A-0255** (Hungarian-matching circularity), **A-0203** (unpromptable objects), **A-0283** (radial extrapolation failure): no occupying prior found at title level; each admitted with the standard "re-search before proposal" flag.
- Remaining rescues (0010, 0020, 0046, 0062, 0068, 0099, 0101, 0160, 0170, 0178, 0200, 0209, 0233, 0286, 0343, 0348) carry F's original screening plus my collision check against the G portfolio; none touches a G LOCK. A-0343 must cite the ARO/bag-of-words line (ICLR 2023) as its classification-side template; A-0348 must position against test-time-compute work in generative models as an import, not an invention.

**Pre-reconciliation totals: 5 literature kills (0331, 0352, 0272, 0017, 0107) · mutations kept (0074, 0199, 0326, 0071, 0026-unit) · 17 A ideas merged into hosts · everything else survived attack. See Part 5 for the final post-reconciliation totals.**

---

## Part 5 — Reconciliation with F's `prior_work_attack.md` and J's Stage-4 verdicts (supersedes conflicts above)

F's attack (28 ideas, live-searched: 2 KILL, 15 MUTATE, 11 SURVIVE) and J's Reviewer-2 verdicts on 23 batch-A survivors arrived mid-merge. Where we independently attacked the same idea, agreement was high (0017 KILL/KILL; 0074, 0199, 0300, 0326, 0331-premise, 0334-mechanism all judged occupied by both). Divergences, resolved as follows:

| ID | Mine | F / J | Resolution |
|---|---|---|---|
| **A-0331** | KILL (blob loss/ICI) | F: MUTATE (gradient instrumentation unclaimed) · J: MUTATE, "freshness-fragile, pursue first" (CC-DiceCE ISBI 2026 already prints gradient-field contrasts) | **Restored as FLEX [mut]**: per-instance gradient-share instrumentation + data-side-vs-loss-side remedies; must beat the size-only predictor; execute-first flag |
| **A-0352** | KILL (segmentation-free EF regression established) | F: MUTATE (non-count scalars open) · J: MUTATE (regression *lost* in-domain on fetal-head circumference PMC8877769; physical-GT anchoring is the survival condition) | **Restored as FLEX [mut]**: physical referents (phantom volumes, harvest biomass, cytometry counts) with boundary ambiguity varied; rides A-0175 infrastructure |
| **A-0107** | KILL (GRAR/TOPGN/Foster) | F: MUTATE (supervision-purity fraction + fleet-scaling law unclaimed; F found SILICA/Bootstrap-Perception, I found GRAR — all use the cue, none train pure-RGB from mined masks) | **Restored as FLEX [mut]**: purity taxonomy + pseudo-label scaling study |
| **A-0334** | LOCK (leakage-at-scale) | F: MUTATE (silhouette recognition classical) · J: MUTATE — **BareBones (arXiv:2604.10528)** now provides the mask-only recognition benchmark, with an opposite headline for VLMs; only the documented-practice privacy audit survives | **Demoted to FLEX [mut]**; C-0333 arm retained but flagged as partially scooped by BareBones |
| **A-0349** | LOCK | J: MUTATE — training-labels objection (models are trained on human conventions, so in-distribution divergence should be ~0); Hoffman–Richards minima confound | **Demoted to FLEX [mut]**: convention-learnability version (model vs own training labels, per junction type, evidence-strength scaling, curvature/function dissociation control) |
| **A-0199** | MUTATE (dose-response) | J: MUTATE with freshness hit — HalluSegBench (arXiv:2506.21546), HII-DPO already own segmentation-hallucination framing | Kept FLEX; repositioned as the dense/classical-segmenter complement with fully-known training data |
| **A-0121** | LOCK | J: SURVIVE-IF-EXPERIMENT; freshness: VehicleSec 2026 mirror-induced **LiDAR** phantoms + patents | Kept LOCK; camera-side audit unclaimed; pilot-gated (pre-registered phantom-rate floor); "hidden error class" rhetoric retired |
| **A-0071** | MUTATE (ecosystem audit) | J: MUTATE — pairwise inter-rater Dice is **not** an upper bound (Cellpose-SAM argument); consensus-referenced ceiling required | Mutation adopted: rater-vs-consensus extrapolated ceiling, SOTA located against that, style-vs-anatomy residual decomposition |
| **A-0148** | KEEP | F: MUTATE — soft-vs-hard highlighting literature owns the core format effect | Mutation adopted: COD-specific with calibration quality experimentally manipulated; harm condition links A-0188 |
| **A-0145 / A-0215 / A-0026 / A-0181 / A-0237(+0249) / A-0301 / A-0074 / A-0326 / A-0076 / A-0300 / A-0198 / A-0245** | keep/merge | F/J mutations of scope | All adopted as row-level notes in `provisional_200.md`; none changes slot structure (my merges 0249→0237, 0300→0290, 0198→C-0311, 0245→C-0150, 0100→C-0122 are each independently endorsed by F or J) |

**Final totals after reconciliation: 2 literature kills (0272, 0017) · 3 kills reverted to mutations (0331, 0352, 0107) · 2 LOCK demotions (0334, 0349) · A portfolio 85 slots, grand total 200.**
