# Stage 2 — Meta-Review / Audit (Windows5)

**Role:** Independent meta-reviewer/auditor, separate from the two Stage-2 reviewers.
**Inputs audited:**
- `cursor/stage1-batch-a-idea-generation-88c4` — `stage1_batch_A_ideas.md` (340 ideas), `stage1_batch_A_index.md`
- `cursor/stage1-batch-b-ideas-89e3` — `stage1_batch_B_ideas.md` (340 ideas), `stage1_batch_B_index.md`
- `cursor/stage2-batch-a-review-a57f` — survivors (73/340), killed (267), scores
- `cursor/stage2-batch-b-review-f04c` — survivors (75/340), killed (265), scores

**Pool state:** 148 survivors of 680 (21.8%). Kill rates nearly identical across batches (A 78.5%, B 77.9%).

---

## 1. Executive verdicts on the six audit questions

| # | Question | Verdict |
|---|----------|---------|
| 1 | Echo chamber (too many evaluation-methodology ideas, too few method ideas)? | **Partially confirmed — structural, not collusive.** The imbalance is not at the eval-cluster level (A's Cluster 17 survived at 20%, near the batch average); it is at the *framing* level: "audit X" survives, "build X" dies. Combined pool: ~62% mechanism/failure-mode studies, ~28% audits of benchmarks/protocols/literature, **~10% constructive contributions** (new supervision signals, methods, data resources). Both reviewers applied identical protection taxonomies (HRHR/CI/DM/CF) and identical on-sight kill rules from the same supervisor brief, so they converged on the same survivor profile independently — a top-down echo, not reviewer collusion. |
| 2 | Wrongly dropped high-risk/high-reward ideas? | **Yes, a specific class.** HRHR protection worked for compute-risky ideas (B-0009, A-0203, A-0122 were correctly saved) but systematically failed for **data/partnership-risky** ideas: B-0177 (HRHR-flagged, killed for wet-lab), A-0139 (Nov 5 formalism, killed for footage), A-0146 (Nov 5 formulation-breaker, killed for annotation cost), B-0148, A-0124, A-0301. The reviewers effectively imposed a "public-checkpoints-and-public-data-only" prior that deletes the highest-upside supervision/data ideas regardless of upside. |
| 3 | False novelty in top survivors? | **Yes — 3 verified cases, several suspected** (§3). Verified against literature: A-0340 (bootstrap leaderboard stability — Maier-Hein et al., Nat. Commun. 2018 did exactly this for biomedical challenges), A-0245 (recipe-vs-architecture — nnU-Net Revisited, 2024, already established the medical-3D half), A-0013 (SAM2-worse-than-SAM1 on static/2D — multiple 2024 papers report it for medical 2D). None are fatal; all need honest repositioning as generalizations, not firsts. |
| 4 | Missing directions vs SAM / medical / smoke-fire / PEFT / VLM? | **Video-temporal SAM2 science is the largest hole** (near-zero survivors); also: efficiency/distillation science (killed as "engineering"), clinical-outcome-anchored metric validity, subgroup safety of fine-tuning, SSL-continued-pretraining recipe conflicts, and 3D/volumetric-native foundation questions beyond A-0093. Details in §4. |
| 5 | Revive list | **12 revives** with full Stage-1 text in §5. |
| 6 | Supervisor bias (meta-evaluation vs build-a-model)? | **Confirmed and quantifiable.** The Stage-2 brief mandated on-sight kills of "engineering-first" and "apply-to-domain" ideas: Batch B logged K1-ENG 35 + K6-PORT 12 = 47 on-sight kills (18% of all kills), with the reviewer admitting several "are likely to *work* (0245, 0266, 0316); they died because their success would be a deliverable, not an answer." Batch A killed its single most novel idea (A-0278, Nov 5) explicitly for "builds a thing rather than tests a claim." Meanwhile meta-evaluation survived at high rates in every cluster. The pipeline currently optimizes for "criticize the field's measurements" over "advance the field's capabilities." |

---

## 2. Echo-chamber analysis (Q1, Q6 evidence)

### 2.1 Composition of the 148 survivors (auditor's classification)

| Type | Batch A (73) | Batch B (75) | Combined | Share |
|---|---|---|---|---|
| Mechanism / failure-mode / dissociation science | ~44 | ~47 | ~91 | ~62% |
| Evaluation, benchmark, protocol & literature meta-science | ~26 | ~16 | ~42 | ~28% |
| Constructive (new supervision, method, data resource, physics GT) | ~3 (0122, 0125, 0254) | ~12 (0057, 0078, 0110, 0159, 0162, 0182, 0184, 0193, 0217, 0279, 0318, 0320) | ~15 | ~10% |

Reading: Batch B's reviewer preserved a meaningfully healthier build fraction (16%) than Batch A's (4%). Batch A's survivor list is almost purely critique — the entire Cluster 3 (PEFT) survivor set, for example, is deflationary (LLRD explains PEFT, augmentation matches LoRA, one dial explains recipes); not one PEFT survivor in A proposes anything.

### 2.2 Why this is a structural echo, not reviewer collusion

- Both reviewers used the same four protection classes and the same two forbidden categories, traceable to the shared supervisor brief ("Per the task brief, two patterns were killed on sight" — B killed report §1; identical enforcement section in A killed report).
- Both batches' Stage-1 generation was already audit-tilted: A dedicated clusters 11 ("Valuable Negative Results") and 17 ("Evaluation Methodology") = 35/340 ideas; B dedicated cluster 3 (Evaluation/Calibration, 40 ideas) and cluster 9 (Surprising Phenomena, 35 ideas). Stage 2 then amplified the tilt.
- Cross-batch redundancy went unchecked because each reviewer saw only their batch. At least 11 near-duplicate survivor pairs/programs now sit in the pool (see §6.2) — e.g., A-0091 vs B-0082 (label-noise floors vs rank stability), A-0103 vs B-0337/B-0120 (uncertainty-vs-rater validity), A-0031 vs B-0083/B-0108 (protocol sensitivity of rankings), A-0003/0161 vs B-0122/0129/0288/0305 (tokenization/small-structure), A-0029/0007/0267 vs B-0019/0191/0320/0329 (contamination flywheel). Redundancy inside the audit genre consumed slots that method ideas were killed to free.

### 2.3 What the reviewers got right (for balance)

The protection policy genuinely saved counter-intuitive and HRHR compute bets that mean-scoring would have killed (B killed report §1 documents this explicitly; A protected 0203's SSL retraining). The kill of module-stacking and loss-swap papers was correct and clean — zero such survivors. The problem is not that audits survived; it is that *construction* was treated as a forbidden category rather than judged on the falsifiability of its enabling hypothesis.

---

## 3. False-novelty findings in top survivors (Q3)

Verified against the literature (checked 2026-08):

1. **A-0340 — "Bootstrap the leaderboards: the fiction fraction."** Claims bootstrap CIs "have not been done" for segmentation leaderboard structure. **Substantially pre-empted for medical:** Maier-Hein et al., *"Why rankings of biomedical image analysis competitions should be interpreted with care"* (Nature Communications 9:5217, 2018) bootstrapped (1,000 resamples) all 2015 segmentation challenges and reported first-rank stability of only 9–21%; the Wiesenfarth et al. toolkit made this standard for MICCAI challenges (e.g., CrossMoDA 2021 reports Kendall-tau ranking stability). The natural-image-leaderboard generalization and the "fiction fraction" headline remain contributions, but the idea must cite and position against this line or it will be desk-noted by any MICCAI-adjacent reviewer. Same caveat applies partially to A-0091 and B-0082 (annotation-observer sensitivity of rankings is also in Maier-Hein 2018).
2. **A-0245 — "A 2015 U-Net with a 2026 recipe."** *nnU-Net Revisited: A Call for Rigorous Validation in 3D Medical Image Segmentation* (arXiv:2404.09556, 2024) already demonstrated for medical 3D that properly configured CNN U-Nets beat Transformer/Mamba architectures and that claimed architectural gains collapse under rigorous baselines. A-0245's natural-image, decade-spanning, compute-matched decomposition is still open — but the medical arm is done, and A-0226 (attention-U-Net replication) overlaps the same paper's finding even more directly. Both survive, but their novelty budgets are thinner than scored (A-0245 Unp 4 is optimistic; 2–3 is honest).
3. **A-0013 — "SAM2 worse than SAM1 on static fine boundaries."** Multiple 2024 papers already ran the head-to-head on 2D images: *Is SAM 2 Better than SAM in Medical Image Segmentation?* (arXiv:2408.04212 — SAM2 worse on CT/ultrasound), *SAM 2: an application to 2D and 3D medical images* (arXiv:2408.00756 — parity on single-frame 2D). The survivor's carve ("boundary-F on static fine structures, natural high-res") is real but narrow; the headline "newest isn't better" is published. Should be demoted from CI+CF protection to a quick confirmation arm inside the cluster-1 program.

Suspected (not independently verified, flagged for Stage-3 prior-work sweep):

4. **A-0097** (Dice loss destroys calibration) — the phenomenon is documented in isolated medical-imaging studies (the idea itself concedes this); only the imbalance-scaling law and schedule fix are new.
5. **A-0142** (depth input hurts on glass) — robotics work (ClearGrasp lineage) already exploits depth-invalidity as a transparency cue; the controlled sign-of-contribution study is the only new part, as the reviewer noted.
6. **B-0012** (near-duplicate inflation) — patient-level leakage/dedup auditing is an established medical-imaging literature; the few-shot-specific quantification is the residual novelty.
7. **B-0083** (prompt-protocol sensitivity) — several medical-SAM evaluation papers already vary point/box protocols and note ranking effects; the systematic cross-protocol rank-correlation index is the incremental part.

**Recommendation:** Stage 3 must run the prior-work killsheet on *survivors*, not only on new ideas — the Stage-2 reviewers' "Unp" scores were self-assessed without search and are the least reliable column in both score sheets.

---

## 4. Missing research directions (Q4)

Relative to the five mandated axes:

- **SAM / SAM2:** The pool contains essentially **no video/temporal science** — A killed every SAM2-video idea (0004 occlusion decay, 0005 identity switches, 0026 memory non-monotonicity, 0086 video-FT-degrades-image) and B kept only 0233 (static-camera change detection). The only surviving temporal idea is A-0125 (turbulence spectra). SAM2's memory mechanism — the single biggest architectural novelty in the promptable-segmentation line — is unexamined by 148 surviving ideas. Also missing: **distillation/efficiency science** (A-0024, A-0224 quantization, A-0339 FLOPs-vs-latency all killed as "engineering" — but efficiency-accuracy scaling laws are legitimate science with huge practitioner reach).
- **Medical segmentation:** well covered on audits (0091/0097/0100/0103/0118/0093), but missing: **metric→clinical-outcome validity** (B-0081 killed; nothing in the pool connects mask metrics to the measurements clinicians consume — the root validity question under every medical audit already in the pool), **subgroup/fairness safety of adaptation** (B-0286 killed; no surviving idea asks who regresses when the average improves), longitudinal/change segmentation, and registration-segmentation coupling.
- **Smoke / fire:** the strongest program in the pool (A-0121/0122/0123/0125/0126/0128/0319 + B-0136/0318/0055/0241). Genuine residual gaps: **confusable-aerosol separability** (A-0124 killed — the false-alarm question underneath B-0055 and B-0124), IR/thermal fusion value (A-0131 killed on data), and satellite/geostationary-scale early detection (never generated — Stage-3 generation gap).
- **PEFT:** deep coverage of deflation (A-0055/0067/0072, B-0114/0248/0253/0257/0260/0306) but the **formal mechanism** is missing: A-0052's seed-level bias-variance decomposition was killed purely on compute (480 runs) even though it is the theory that would unify B-0272 (noise robustness), B-0306 (rank-data law), and A-0055. Also missing: PEFT×quantization interaction, and rank-vs-model-scale laws.
- **VLM dense prediction:** audits are rich (A-0181/0183/0185/0187/0199, B-0132/0174/0185); missing: the **cheap text-side causal probe** (B-0033, killed as duplicate of B-0124 although 0124 covers only amorphous classes, not the general long tail), visual-token-budget scaling for grounding (A-0191, killed on compute — legitimate but should be logged as a scaling-collaboration idea, not deleted), and any constructive dense-VLM training idea (everything constructive in this space was K1-ENG'd).
- **Cross-cutting:** no surviving idea in either batch touches **3D/point-cloud/mesh promptable segmentation** — a generation gap, not a review gap; flag for Stage-3 idea generation rather than revival.

---

## 5. Revive list (12 — full Stage-1 text, verbatim)

Selection principles: (a) correct the anti-construction bias with build ideas whose enabling hypotheses are falsifiable; (b) restore the data/partnership-gated HRHR class with explicit go/no-go gates; (c) fill the §4 gaps; (d) add no more benchmark meta-audits (the one eval revive, B-0081, anchors metrics to clinical outcomes — a validity question, not another leaderboard critique).

### R1 — IDEA-A-0278 — Mask-MAE prior from unpaired mask archives  *(anti-build-bias casualty; Batch A's most novel killed idea, Nov 5)*

- **One-sentence idea:** Learn label-space priors by masked autoencoding on *unpaired* segmentation masks (no images), and test whether such shape/layout priors improve label-efficient segmentation when injected as a regularizer.
- **Problem:** Massive mask archives exist without usable images (privacy-stripped medical, licensing-orphaned datasets); whether label-space structure alone — shapes, adjacencies, layouts — carries transferable value has not been tested.
- **Core Hypothesis (falsifiable):** A mask-MAE prior trained on unpaired masks, used to regularize low-label training (penalizing unlikely label configurations), improves 10-label-regime performance by >3 mIoU on structurally regular domains (anatomy, streets) and ~0 on unstructured ones — label-space structure is real, transferable, and domain-regularity-dependent.
- **Why Important:** Unlocks a dormant data resource (orphaned masks) and quantifies how much of segmentation is knowable from labels alone.
- **Why Possibly Novel:** Shape priors are classical; foundation-style pretraining on *unpaired mask corpora* as a portable prior is unexplored.
- **Minimal Experiment:** Train mask-MAE on pooled mask archives; inject as an energy/regularizer in low-label training across structured/unstructured domains; measure the interaction.
- **Main Risk:** Priors may encode dataset-specific annotation conventions rather than world structure (cf. IDEA-A-0007); test cross-dataset prior transfer explicitly.

**Auditor note:** The kill reason ("builds a thing rather than tests a claim") is wrong on its face — the structured-vs-unstructured interaction *is* the falsifiable claim, and the convention-encoding risk is a feature: it makes this the constructive twin of survivor A-0007. Highest-priority revive.

### R2 — IDEA-B-0177 — Restain-and-register IHC as molecular ground truth for H&E  *(HRHR protection failure; the reviewer's own "highest-upside supervision idea in Cluster 5")*

- **One-sentence idea:** Generate automatic cell/structure labels for H&E histology by restaining the same physical slides with IHC markers and registering the pair, then characterize and correct the registration-induced label noise for training.
- **Problem:** Histology annotation demands pathologist time and suffers known inter-rater problems, while chemistry can produce molecularly defined labels—if the registration noise between stains can be handled.
- **Core Hypothesis:** Restain-registered IHC labels train H&E segmenters that match or exceed pathologist-annotation-trained models on molecularly verifiable targets, provided training explicitly models the spatially structured registration noise (which naive training does not tolerate).
- **Why Important:** Offers molecular ground truth at chemistry cost instead of expert cost, potentially rebasing histology segmentation datasets.
- **Why Possibly Novel:** Restain supervision exists in isolated efforts; the registration-noise-aware training treatment and head-to-head against expert labels are undeveloped.
- **Minimal Experiment:** Produce restained-registered pairs for one marker; quantify registration noise structure; train noise-aware vs naive vs expert-labeled models; compare on independent molecular validation.
- **Main Risk:** Restaining alters tissue subtly, and some targets lack clean IHC markers.

**Auditor note:** Revive **conditionally**: hold as a partnership-gated HRHR slot with a hard go/no-go (existing public restain-registered pairs, e.g. from registration-challenge releases, must support the noise-characterization pilot before any wet-lab spend). Killing HRHR ideas *because* they carry the risk the flag exists to protect is a protection-policy contradiction.

### R3 — IDEA-B-0081 — Which segmentation metric predicts downstream clinical measurement error?  *(the missing root-validity question of the medical program)*

- **One-sentence idea:** Determine empirically which mask metric (IoU, boundary F1, HD95, surface Dice) best predicts errors in the downstream clinical quantities actually consumed (volumes, diameters, growth rates), and expose where the standard metrics mispredict utility.
- **Problem:** Papers optimize and rank by IoU/Dice, but clinicians consume derived measurements; the metric-to-utility mapping is assumed, not measured.
- **Core Hypothesis:** For thin and small structures, boundary-localized metrics predict measurement error far better than region metrics, and metric-induced method rankings materially disagree with utility-induced rankings on at least some structure classes.
- **Why Important:** If leaderboard metrics mispredict utility, the field's selection pressure is miscalibrated at the root.
- **Why Possibly Novel:** Direct regression from mask metrics to downstream clinical measurement error across structure classes has not been systematically published.
- **Minimal Experiment:** On datasets with GT masks, compute derived clinical measurements from predictions of many public models; regress measurement errors on mask metrics; compare rank orders.
- **Main Risk:** Utility definitions vary by clinical task; conclusions must be stratified, not global.

**Auditor note:** Killed as "must be stratified, weakening the headline" — but stratified metric-validity results are exactly what A-0091/B-0082/B-0083 need to matter clinically. Cheap (public checkpoints + arithmetic on predictions). The one eval-genre revive, because it anchors evaluation to outcomes instead of adding another leaderboard critique.

### R4 — IDEA-A-0052 — Bias-variance decomposition of PEFT vs full fine-tuning  *(compute-bias casualty; SciQ 5; the missing theory under four survivors)*

- **One-sentence idea:** Quantify the bias-variance decomposition of PEFT vs full fine-tuning across random seeds: is PEFT's advantage on small data mostly variance reduction?
- **Problem:** PEFT beats full FT on small datasets, attributed vaguely to "regularization"; a formal seed-level bias-variance decomposition would identify the mechanism.
- **Core Hypothesis (falsifiable):** Across 20 seeds, PEFT shows ≥3× lower seed variance but *higher* bias (worse best-seed performance) than full FT; the mean gap is explained primarily by the variance term at n<500 images and flips sign as n grows.
- **Why Important:** If PEFT is variance reduction, alternatives like full-FT ensembles or better early stopping may dominate — the field's small-data default would change.
- **Why Possibly Novel:** Seed-level bias-variance analysis of the PEFT-vs-FT question for segmentation is missing; papers report single-seed means.
- **Minimal Experiment:** 3 datasets × 4 training sizes × {LoRA, full FT} × 20 seeds on one backbone; decompose test error; locate the crossover.
- **Main Risk:** 480 runs is compute-heavy; mitigate with small backbone + short schedules, verifying conclusions on one large configuration.

**Auditor note:** Revive at reduced scope (2 datasets × 3 sizes × 10 seeds ≈ 120 runs) and **share the grid with B-0114** (PEFT seed variance, survivor), which already budgets 10 seeds × 4 methods × 4 sizes — the marginal cost of the decomposition on top of B-0114's runs is near zero. Killing it while keeping B-0114 was a cross-batch coordination failure.

### R5 — IDEA-B-0300 — Objectness erosion: when continued SSL pretraining hurts promptable segmentation  *(recipe-conflict science; fills the pretraining-dynamics gap)*

- **One-sentence idea:** Investigate the phenomenon that continued self-supervised pretraining (MAE-style) on target-domain data before supervised fine-tuning sometimes degrades promptable segmentation, testing whether reconstruction objectives erode the objectness/grouping structure that prompt decoding depends on.
- **Problem:** The domain-adaptive-pretraining recipe (SSL on target, then fine-tune) is standard advice inherited from NLP and classification, but promptable segmentation relies on representational properties (grouping, boundary salience) that reconstruction objectives do not preserve and may actively trade away—an unexamined recipe conflict.
- **Core Hypothesis:** MAE-style continued pretraining measurably degrades frozen-feature grouping quality (probeable before any fine-tuning) while improving pixel-reconstruction-aligned properties, the degradation propagates to prompted-segmentation performance in low-label fine-tuning regimes (insufficient supervision to rebuild grouping), and grouping-preserving SSL variants (contrastive or distillation-anchored) avoid the trap—defining which SSL is safe for promptable models.
- **Why Important:** Corrects a default recipe at the intersection of two major practices before it becomes further entrenched in dense-model adaptation.
- **Why Possibly Novel:** The SSL-objective-versus-objectness conflict for promptable models has not been isolated.
- **Minimal Experiment:** Continue-pretrain with objective ladders; probe grouping properties; fine-tune across label budgets; map where each SSL objective helps or harms.
- **Main Risk:** Effects may depend on pretraining duration and masking ratio in ways that complicate clean recommendations.

**Auditor note:** Killed on "instrument softness" (no settled grouping probe) — but survivors B-0129/B-0132 are building exactly that probe infrastructure; the reviewer's own almost-survived note says "if a robust grouping probe emerges from 0129/0132's work, rerun this." That condition is already funded. Revive now and sequence after 0129/0132.

### R6 — IDEA-B-0286 — Subgroup regression under fine-tuning: who loses when the average improves?  *(medical-safety gap; nothing in the pool covers it)*

- **One-sentence idea:** Systematically test whether fine-tuning that improves average performance regresses identifiable subgroups (rare acquisition settings, atypical anatomy, minority demographics) below the zero-shot baseline—making the pre-fine-tuning model strictly better for some patients.
- **Problem:** Fine-tuning decisions are made on aggregate metrics, subgroup regressions would be clinically and ethically material, and the zero-shot-versus-fine-tuned comparison at subgroup granularity is simply not part of current adaptation practice.
- **Core Hypothesis:** Fine-tuning on realistically skewed target data produces measurable subgroup regressions relative to zero-shot in a substantial fraction of adaptation runs (the adapted model trades tail robustness inherited from web-scale pretraining for target-majority fit), regressions concentrate in subgroups underrepresented in fine-tuning data relative to pretraining, and lightweight interpolation between base and adapted weights recovers most subgroup loss at minor average cost.
- **Why Important:** Establishes whether the field's default adaptation practice violates "do no harm" at subgroup level—and provides the monitoring protocol to catch it.
- **Why Possibly Novel:** Zero-shot-versus-fine-tuned subgroup regression auditing has not been formalized for dense medical tasks.
- **Minimal Experiment:** Run standard adaptations across datasets with subgroup metadata; compute subgroup-level base-versus-adapted deltas; test weight-interpolation mitigation.
- **Main Risk:** Subgroup metadata availability limits which regressions are observable.

**Auditor note:** Killed because the mechanism "is documented for classification" — but the dense/medical instantiation with the do-no-harm framing is precisely the kind of consequential port the pool keeps elsewhere (e.g., A-0242 ports z-curves from psychology). Shares infrastructure with survivors B-0248/B-0260 (retention/transfer geometry); marginal cost is small.

### R7 — IDEA-A-0124 — The smoke/fog/steam/cloud/dust confusion benchmark  *(false-alarm science; the reviewer called its framing "superb"; killed on curation)*

- **One-sentence idea:** Build the smoke/fog/steam/cloud/dust confusion benchmark and test whether any visual model can separate these physically distinct but visually similar aerosols from single frames.
- **Problem:** Wildfire systems must distinguish smoke from look-alike aerosols, but no benchmark isolates this five-way confusion, and it is unknown whether single-frame separation is even information-theoretically feasible.
- **Core Hypothesis (falsifiable):** Single-frame human expert accuracy on the five-way task is barely above chance for distant plumes (<45% vs 20% chance), while short temporal clips restore human accuracy to >80% — the discrimination is fundamentally temporal, and single-frame models are structurally capped.
- **Why Important:** If discrimination is temporal, the industry's single-frame smoke detectors have a hard false-alarm floor — an architecture-independent conclusion that changes system design.
- **Why Possibly Novel:** False-alarm categories are known operationally; the human-referenced single-frame-vs-clip information analysis is new science for the domain.
- **Minimal Experiment:** Curate a five-way aerosol dataset with clips; run human studies (frame vs clip); benchmark models under both input regimes.
- **Main Risk:** Ground-truth aerosol identity needs metadata (fire reports, weather records); curation is the main effort.

**Auditor note:** This is the information-theoretic ceiling under three survivors (B-0055 fog-negative-domain, B-0124 text-anchor confusion, A-0126 latency metric) and the only killed idea that restores a *temporal* question to the smoke program. Curation amortizes across B-0017/B-0241/B-0110's already-funded negative-set work.

### R8 — IDEA-A-0328 — Simulated-click protocol validity for interactive segmentation  *(protocol-validity gap; amortizable with funded B-side user studies)*

- **One-sentence idea:** Validate (or invalidate) simulated-click protocols for interactive segmentation by measuring ranking agreement with real-user evaluations across the current model generation.
- **Problem:** Interactive segmentation progress is measured almost entirely through click simulators (cf. IDEA-A-0048); if simulator rankings diverge from human-user rankings for modern models, the subfield's leaderboard is measuring the wrong thing — the protocol validity check is overdue.
- **Core Hypothesis (falsifiable):** Simulator-based and real-user rankings agree on coarse model tiers but disagree on adjacent pairs in >30% of cases, with disagreement concentrated where models differ in error *placement* (which simulators respond to differently than humans) — simulators are valid for screening, invalid for fine ranking.
- **Why Important:** Defines the evidentiary weight simulator results can carry — directly affecting how interactive-segmentation papers should be evaluated and written.
- **Why Possibly Novel:** Small user studies exist per-paper; the protocol-validity study across a model generation with tier/fine-ranking decomposition is missing.
- **Minimal Experiment:** 25 users × 6 models × standardized tasks with logged interactions; compare ranking structures against 3 simulator protocols.
- **Main Risk:** User-study variance; within-subject design and pre-registered analysis are mandatory.

**Auditor note:** Killed on user-study cost — but Batch B *funded* the same data collection twice (B-0089 oracle-inflation and B-0193 prompt-log collection, which the B reviewer explicitly ordered to "run as one user-study effort"). A-0328's logs are the same logs. Reviving it makes the already-budgeted human study serve three papers instead of two. Cross-batch coordination failure, cost-free fix.

### R9 — IDEA-B-0033 — Tail open-vocabulary failure is linguistic, not visual  *(VLM causal probe; near-miss #1 in Batch B's own list)*

- **One-sentence idea:** Decompose open-vocabulary segmentation failures on tail classes into linguistic causes (polysemous or obscure class names) versus visual causes (rare appearance), by intervening on the text side only.
- **Problem:** Open-vocab models fail on rare classes, and everyone assumes the cause is visual rarity, but tail class names are also rarer and more ambiguous in the text encoder's training distribution.
- **Core Hypothesis:** For a meaningful fraction of tail classes, replacing the class name with a disambiguated description (or a name that is frequent in text corpora) recovers a large share of the gap, holding the image pathway fixed.
- **Why Important:** If language is the bottleneck, the fix is prompt engineering or text-encoder training—far cheaper than collecting rare visual data.
- **Why Possibly Novel:** Text-side interventions as a causal probe for long-tail dense prediction are rarely isolated from visual factors.
- **Minimal Experiment:** On a long-tail benchmark, evaluate per-class performance under {original name, synonym set, LLM-generated disambiguated description}; correlate recovery with corpus-frequency and polysemy measures of names.
- **Main Risk:** Description prompts can leak spatial hints, inflating recovery for non-linguistic reasons; needs controls.

**Auditor note:** Killed as duplicate of B-0124, but 0124 covers only amorphous-class text-anchor collinearity; 0033 is the general long-tail version, and it mechanistically connects to A-0033 (specificity inverse-U) and A-0049 (register mismatch) — three surviving ideas would share its frequency-regression machinery. The B reviewer's own note: "resurrect if 0124's anchor-substitution design hits trouble" — resurrect now, run them together.

### R10 — IDEA-A-0096 — The small-lesion sensitivity law: foundation models vs specialists  *(clinical small-object gap; A-0161 does not carry this)*

- **One-sentence idea:** Establish the sensitivity-vs-lesion-size law for medical VFMs versus specialized detectors, testing whether foundation models have a systematically worse small-lesion exponent.
- **Problem:** Missing small lesions is the clinically catastrophic failure; whether VFM adaptation sacrifices small-lesion sensitivity relative to purpose-built models is unquantified as a scaling relationship.
- **Core Hypothesis (falsifiable):** Detection sensitivity vs lesion diameter follows a sigmoid whose midpoint is ≥30% larger (worse) for adapted VFMs than for specialized 3D models at matched overall Dice — aggregate parity hides small-lesion inferiority.
- **Why Important:** If the law holds, aggregate-metric-based claims that "VFMs match specialists" are clinically misleading precisely where it matters most.
- **Why Possibly Novel:** Size-stratified evaluation exists; the cross-family sigmoid-midpoint comparison at matched aggregate performance is new.
- **Minimal Experiment:** On lesion datasets with size distributions (lung nodules, liver lesions, MS lesions), fit per-model sensitivity-size curves; compare midpoints at matched Dice.
- **Main Risk:** Size confounds with contrast and location; use stratified matching or covariate adjustment.

**Auditor note:** The kill rationale ("survivor 0161 carries the general size-law science") conflates two different laws: 0161 is about *tokenization* floors in natural images; 0096 is about *sensitivity* (detection, not delineation) at matched aggregate Dice in 3D clinical data — the number regulators and radiology procurement actually need. Also the natural evaluation arm of survivor A-0093 (nnU-Net decomposition) and B-0288 (inverse scaling); shares all stratification machinery.

### R11 — IDEA-A-0301 — Continual adaptation under cyclically returning domains  *(deployment-realistic protocol; "genuinely new evaluation science" per the reviewer)*

- **One-sentence idea:** Study continual adaptation under *cyclically returning* domains (day/night, seasons, weather) and test whether current continual-DA methods oscillate — repeatedly re-learning and forgetting each phase — instead of consolidating a cycle-covering solution.
- **Problem:** Real deployment shift is largely cyclic, not a linear sequence of novel domains, but continual-DA is evaluated on linear sequences; whether methods exploit recurrence (consolidate) or thrash (re-adapt every cycle, accumulating damage) is unknown.
- **Core Hypothesis (falsifiable):** Standard continual-DA methods show non-decreasing re-adaptation cost across repeated cycles (no consolidation), while an explicit phase-memory design converges to near-zero re-adaptation by cycle 3 — current methods waste the structure of recurrence, falsified if standard methods naturally consolidate.
- **Why Important:** Cyclic shift is the actual deployment condition for outdoor perception; consolidation-vs-thrashing determines long-run cost and stability of adaptive systems.
- **Why Possibly Novel:** Continual DA uses linear domain sequences; the cyclic-recurrence protocol and consolidation metrics are new evaluation science.
- **Minimal Experiment:** Build cyclic benchmarks from time-stamped driving data; run continual-DA methods over 5+ cycles; measure per-cycle adaptation cost trajectories.
- **Main Risk:** Real cyclic data confounds cycle phase with content drift; complement with controlled synthetic cycles.

**Auditor note:** Killed on data-assembly weight, but day/night/weather cycles are recoverable from existing time-stamped driving corpora (BDD100k-class) plus the synthetic-cycle control the idea itself proposes. Connects the A-cluster-4 forgetting-hysteresis program (A-0089's refresh loops are the *training-side* of this exact phenomenon) to deployment; also the only continual-deployment protocol idea left anywhere in the pool.

### R12 — IDEA-B-0098 — Independent verifier vs self-confidence for failure prediction  *(K1-ENG near-miss; revive with the science made explicit)*

- **One-sentence idea:** Train small independent verifier networks that predict a frozen segmenter's per-case failure (IoU below threshold) from the image and predicted mask, and benchmark them against the model's own confidence outputs.
- **Problem:** Silent failure is the key deployment risk; self-reported confidence is entangled with the very representations that caused the failure.
- **Core Hypothesis:** An independent verifier trained on diverse failure examples detects out-of-domain failures with substantially higher AUROC than self-confidence, because it can key on inconsistency cues (mask-image disagreement) the primary model is blind to.
- **Why Important:** A reliable external failure detector is the missing component for autonomous labeling and clinical triage pipelines.
- **Why Possibly Novel:** Verifier-vs-self-confidence comparisons are established in LLM research but not systematized for dense prediction.
- **Minimal Experiment:** Build failure datasets across 6 domains; train verifiers with held-out-domain evaluation; compare AUROC/AUPR vs self-confidence and ensembles.
- **Main Risk:** Verifiers may overfit the primary model's specific failure styles and miss novel ones.

**Auditor note:** The B reviewer's kill note conceded the science "stays implicit" — so make it explicit as the revival condition: the deliverable is the *attribution* (what do verifiers see that self-confidence structurally cannot — mask-image consistency cues vs representation-entangled confidence), with held-out-model and held-out-domain generalization as the falsifiable claims. This is the generation-side complement of survivors B-0084 (IoU-head calibration) and B-0104 (silent failure), and the pool's only surviving path to an external safety monitor.

**Revive ID summary:** A-0278, A-0052, A-0096, A-0124, A-0301, A-0328 · B-0033, B-0081, B-0098, B-0177 (gated), B-0286, B-0300.
Pool after revives: 148 + 12 = **160**.

---

## 6. Recommended balance for the ~200-idea pool

### 6.1 Target composition

Assuming the pool grows to ~200 via revives plus Stage-3 generation/merging, the auditor recommends rebalancing from the current 62/28/10 (mechanism/eval/build) to approximately:

| Category | Target share | ~Count | Current state | Action |
|---|---|---|---|---|
| Mechanism & failure-mode science (dissociations, laws, causal probes) | 40% | ~80 | over-supplied (~91) | trim via §6.2 merges; keep the sharpest formulation per thread |
| Evaluation / benchmark / protocol meta-science | 20% | ~40 | at cap (~42) and internally redundant | **hard cap**; merge duplicates; admit new entries only if outcome-anchored (B-0081-style), not another leaderboard critique |
| Constructive: new supervision signals, physics-grounded GT, training/adaptation methods with falsifiable enabling hypotheses | 20% | ~40 | badly under-supplied (~15 + 6 revives) | Stage-3 generation should target this class explicitly; re-admit "builds a thing" ideas whenever the enabling hypothesis is falsifiable |
| HRHR bets, including data/partnership-gated ones with go/no-go gates | 10% | ~20 | 20 flagged but skewed to compute-risk | reserve ≥5 slots for data/partnership-gated bets (R2-class); each carries an explicit cheap kill-test to run first |
| Domain full-stack programs (smoke/fire, medical clinical validity, transparency) | 10% | ~20 | good (smoke exemplary) | protect as coherent units; add the temporal/video and clinical-outcome layers via R7/R3/R10 |

### 6.2 Cross-batch merges (free slots; do before adding anything)

At least 11 survivor threads are duplicated across batches and should be merged into single programs at Stage 3: (1) A-0091 + B-0082 + B-0037 label-noise floors/rank stability; (2) A-0103 + B-0337 + B-0120 uncertainty validity vs raters; (3) A-0031 + B-0083 + B-0108 protocol/prompt sensitivity of rankings; (4) A-0340 + B-0082 resampling of leaderboards (reposition against Maier-Hein 2018); (5) A-0007 + A-0029 + A-0267 + B-0019 + B-0191 + B-0320 + B-0329 contamination/data-flywheel; (6) A-0003 + A-0161 + B-0122 + B-0129 + B-0288 + B-0305 tokenization & small structures; (7) A-0176 + B-0285 + B-0338 + B-0331 preprocessing/compression skepticism; (8) A-0142 + B-0075 + B-0126 + B-0159 + B-0162 transparency; (9) A-0055 + A-0072 + B-0114 + B-0248 (+ revived A-0052) PEFT demystification; (10) A-0006 + B-0226 boundary-contrast laws; (11) A-0128 + B-0136 + B-0318 + A-0121/0122/0126 smoke program. Merging these frees roughly 15–20 slots for the under-supplied constructive class without losing any question.

### 6.3 Process fixes for Stage 3

1. **Amend the supervisor brief:** replace "kill engineering-first on sight" with "kill engineering-first *unless the enabling hypothesis is independently falsifiable and the deliverable would be consumed by ≥2 other pool ideas*." A-0278, B-0159, B-0318 pass this test; module-stacking still fails it.
2. **Run the prior-work killsheet on survivors** (not just candidates) — the self-assessed Unp column produced three verified false-novelty survivors (§3).
3. **Cross-batch dedup pass before any new scoring** (§6.2).
4. **Shared-infrastructure accounting:** several kills (A-0328, A-0052, B-0033) were costed as standalone when funded survivors already pay for their data/runs. Cost ideas at *marginal*, not standalone, cost.
5. **Generation directive for the gaps no revive covers:** SAM2 memory/temporal science, efficiency-accuracy scaling laws, 3D/point-cloud promptable segmentation, satellite-scale smoke detection.

---

## 7. Bias findings — summary ranking

1. **Most serious: anti-construction bias.** The supervisor brief's on-sight kill rules plus both reviewers' "question, not deliverable" aesthetic reduced the build fraction to ~10% of the pool (~4% in Batch A). A research program that can only criticize measurements and document failures has no Stage-5 implementable projects that *advance* capability; the field-facing risk is a portfolio of well-executed papers that other groups cite while building the things this program declined to build. Exhibit A: Batch A's most novel idea (A-0278, Nov 5) was killed for being constructive.
2. **Public-data-only prior kills the best HRHR bets** (B-0177, A-0139, A-0146, B-0148, A-0124): the HRHR protection flag was applied to compute risk but not data risk, inverting its purpose exactly where upside is highest.
3. **Self-assessed novelty without search** produced ≥3 verified false-novelty survivors (A-0340, A-0245, A-0013) while "likely published" was used to kill others (A-0300, A-0247) — an asymmetric, unverified standard.
4. **No cross-batch coordination:** duplicated audit programs consumed slots; complementary ideas (A-0328 vs B-0089/0193; A-0052 vs B-0114) were killed for costs the other batch had already funded.
5. **Temporal/video blind spot:** every SAM2-video idea died in both batches independently — the one place the two reviewers' independent judgments converged on an identical *coverage* hole rather than a framing preference.

---

*End of Stage-2 meta-audit. Revives: A-0278, A-0052, A-0096, A-0124, A-0301, A-0328, B-0033, B-0081, B-0098, B-0177 (gated), B-0286, B-0300.*
