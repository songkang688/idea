# Stage 2 — Batch B Scoring Sheet (IDEA-B-0001 … IDEA-B-0340)

**PI:** Windows5
**Stage:** 2 (selection: 340 → survivors)
**Batch scored:** B only (`stage1_batch_B_ideas.md`, 340 ideas, no gaps)
**Reviewer:** independent Stage-2 reviewer
**Survivors:** 75 (see `stage2_batch_B_survivors.md`) · **Eliminated:** 265 (see `stage2_batch_B_killed.md`)

---

## How to read this sheet

Scores are 1–5. The eleven-slot block is in fixed order:

`N/S/Q/T/F/C/D/B/P/E/V`

| Slot | Dimension | 5 means |
|---|---|---|
| N | Novelty | genuinely new question or instrument |
| S | Significance | changes what a whole subfield does |
| Q | Scientific Question | a sharp falsifiable question, not a deliverable |
| T | Technical Soundness | design actually tests the hypothesis |
| F | Feasibility | executable by a small group with public resources |
| C | Compute | cheap (5 = evaluation-only / frozen models) |
| D | Dataset Availability | public data suffices |
| B | Baseline Availability | credible baselines exist off the shelf |
| P | Likelihood Already Published | **5 = unlikely already published** |
| E | Experimental Clarity | the minimal experiment is unambiguous |
| V | Venue Potential | top-tier venue plausible |

Reported separately (deliberately **not** folded into a mean):

- `R` = Risk (5 = high risk of an inconclusive or null-but-uninformative outcome)
- `U` = Potential Upside (5 = field-redirecting if confirmed)
- `ROI` = Research ROI (upside per unit of cost, risk-adjusted)

**Protect flags** (override the mean; see `stage2_batch_B_killed.md` §1 for policy):

- `HRHR` — high-risk / high-reward: kept *because* R is high and U is very high
- `CI` — simple counter-intuitive claim: one experiment can overturn a default
- `DM` — disagreement magnet: reviewers/community will split on the result
- `CF` — cheap-to-falsify: dies fast on frozen models or public checkpoints

**Kill codes** in the Reason column:

| Code | Meaning |
|---|---|
| K1-ENG | engineering-first: a module/method/tool proposal, question secondary (includes module-stacking in effect) |
| K2-THIN | audit or hygiene study whose likely conclusion is already believed, or whose consequence is small |
| K3-DUP | subsumed by a stronger sibling idea (ID given) |
| K4-DATA | blocked by data, metadata, or institutional access that public resources do not supply |
| K5-CMP | compute or scale cost disproportionate to the size of the claim |
| K6-PORT | domain transplant whose payoff is engineering, not a scientific question ("apply X to <domain>") |
| K7-HUM | human-subject study whose cost exceeds its generalizable yield at this stage |
| K8-DATE | finding dates immediately with model versions; methodology survives, numbers do not |
| K9-SIZE | effect likely below noise, non-exportable across datasets, or mechanism unlikely to separate cleanly |

---

## Cluster 1 — Dataset Failure / Annotation Efficiency / Long-Tail (0001–0040)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0001 | SAM pseudo-label noise is structured, so i.i.d. noise-robust losses fail on it | 4/4/5/4/4/3/4/4/4/4/4 | R3·U4·ROI5 | CF | **Y** | Measures the noise model of the field's default auto-labeler; either invalidates or licenses a whole method family |
| 0002 | Iso-budget frontier: many coarse masks vs few precise masks | 3/4/3/4/4/3/4/4/3/4/3 | R2·U3·ROI3 | — | N | K9-SIZE: frontier almost certainly dataset-specific; prescription won't export |
| 0003 | Scale/geometry long tail predicts SAM failure better than class long tail | 4/3/4/4/4/4/4/4/4/4/3 | R3·U3·ROI4 | — | N | K3-DUP (0009, 0037): geometric-stratum framing retained there with stronger claims |
| 0004 | Human click variance, not model variance, dominates thin-structure output variance | 3/3/4/4/3/4/3/3/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0089): prompt-distribution realism retained in the oracle-inflation study |
| 0005 | Prompt-instability as an active-learning acquisition function | 3/3/3/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K1-ENG: acquisition-function proposal; the question ("is instability epistemic?") is left implicit |
| 0006 | Multi-dataset convention mixing produces an averaged boundary *bias*, not variance | 4/4/5/4/3/4/3/4/4/4/4 | R3·U4·ROI4 | DM | **Y** | Attacks the field's default scaling recipe (pool everything) with a measurable bias term and a one-token fix |
| 0007 | PU objective for sparsely annotated auto-labeling | 3/3/3/4/4/3/4/4/2/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0320): the PU framing is stronger applied to everything-mode output |
| 0008 | Soft consensus beats hard majority vote for amorphous classes | 3/3/4/4/3/4/2/3/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0310): soft-label thread retained via the confidence-inversion mechanism |
| 0009 | Per-stratum pretraining frequency vs capability: separating data limits from architecture limits | 5/5/5/4/2/2/3/3/5/3/5 | R4·U5·ROI4 | HRHR | **Y** | The most consequential distinction in foundation-model planning; laborious but nothing else answers it |
| 0010 | Box→point supervision transfers better than point→box (prompt-type asymmetry) | 4/4/4/4/4/3/4/4/4/5/3 | R2·U3·ROI4 | CF | N | Almost-survived: cheap and default-setting, but the claim is narrow next to 0269/0193 |
| 0011 | Everything-mode recall collapses super-linearly past a grid-spacing threshold | 4/3/4/4/4/3/3/3/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: density confounds with size and contrast in real data; threshold likely won't be crisp |
| 0012 | Near-duplicates inflate few-shot / annotation-efficiency claims | 4/5/4/5/5/4/5/4/4/5/4 | R2·U4·ROI5 | CF·DM | **Y** | Cheap, decisive, and directly attacks numbers now driving clinical adoption decisions |
| 0013 | Report gains against the inter-rater noise floor | 3/4/4/4/3/4/3/4/3/4/3 | R3·U4·ROI3 | — | N | K3-DUP (0082): same goal, weaker instrument than the relabeling bootstrap |
| 0014 | Factorized error budget for report→prompt→mask pipelines | 4/4/4/4/3/3/2/3/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0156): report-supervision value retained via the exchange-rate study |
| 0015 | Models inherit the vertex-budget smoothness prior of their annotation tools | 4/3/4/3/3/3/3/3/4/3/3 | R4·U3·ROI2 | — | N | K9-SIZE: curvature spectra likely dominated by image resolution, not annotation economics |
| 0016 | Annotator boundary style is decodable from trained models (leakage) | 4/3/4/3/2/3/1/2/4/3/3 | R4·U3·ROI2 | — | N | K4-DATA: public smoke/fire datasets do not release annotator IDs |
| 0017 | Transparency benchmarks have no target-absent images, so FP behavior is unmeasured | 4/5/4/5/4/5/3/5/4/5/4 | R2·U4·ROI5 | CF | **Y** | Curate ~500 negatives and top-method rankings may invert; deployment harm is FP-dominated |
| 0018 | Rare-class errors are parent-class substitutions, not omissions | 3/3/3/4/4/4/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: re-scoring with a taxonomy; conclusion changes little about what to build |
| 0019 | Correcting SAM proposals anchors annotators, so datasets inherit model-lineage bias | 5/5/5/4/2/3/2/3/5/3/5 | R4·U5·ROI4 | HRHR·DM | **Y** | If true, the field's dominant annotation economy is quietly corrupting its own ground truth |
| 0020 | One gold exemplar + shape-model augmentation ≈ 30-shot for low-variance anatomy | 3/3/3/3/3/3/3/4/3/3/3 | R3·U3·ROI3 | — | N | K9-SIZE: deformation models built from the same data leak test shape statistics |
| 0021 | Tail classes want frozen probes, head classes want depth (two-branch readout) | 3/3/3/3/4/3/4/4/3/3/3 | R3·U3·ROI2 | — | N | K1-ENG: two-branch architecture whose win could come from ensembling, not the stated mechanism |
| 0022 | Effective sample size, not frame count, is the right size descriptor for video datasets | 4/3/4/4/4/3/4/3/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: everyone already discounts adjacent frames; formalizing it changes few decisions |
| 0023 | Eroded GT harms thin structures more than dilated GT at equal magnitude | 4/3/4/4/5/4/4/4/4/5/3 | R4·U3·ROI3 | — | N | K9-SIZE: at realistic 1–2 px magnitudes the asymmetry may not clear seed noise |
| 0024 | Retrieval + dense correspondence beats few-shot fine-tuning below a crossover n | 4/4/4/5/4/4/4/5/4/5/4 | R2·U4·ROI5 | DM·CF | **Y** | Installs the honest baseline the crowded few-shot medical-SAM literature never reports |
| 0025 | Alpha-matte supervision improves *binary* metrics for soft-boundary classes | 4/3/4/3/3/3/2/3/4/3/3 | R4·U3·ROI2 | — | N | K3-DUP (0310, 0318): soft/continuous supervision thread retained with sharper mechanisms |
| 0026 | Acquisition by expected improvement per annotation *minute* | 3/3/3/4/3/3/3/3/3/3/3 | R3·U3·ROI2 | — | N | K1-ENG: cost-aware acquisition method; time models transfer poorly across annotators |
| 0027 | Consensus training vs rater heads, evaluated on a held-out rater | 3/3/4/4/2/3/1/3/3/4/3 | R3·U3·ROI2 | — | N | K4-DATA: public datasets with ≥6 raters per image are too scarce to sweep rater count |
| 0028 | Prompting suppresses reliance on dataset shortcuts | 4/4/4/4/3/3/3/3/4/3/3 | R3·U4·ROI3 | — | N | K3-DUP (0303): near-duplicate pair; neither version survived (see killed §2 K3) |
| 0029 | Context-swap composites separate object rarity from context rarity | 3/3/4/4/4/4/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: clean decomposition, but both branches already have known remedies |
| 0030 | Keyframe-interval optimum from a measured propagation-drift model | 3/3/3/3/3/3/3/3/3/3/3 | R3·U2·ROI2 | — | N | K9-SIZE: drift is regime-dependent (wind); a single rate will not generalize |
| 0031 | Imbalance remedies change calibration, not recall | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI4 | CI | N | K2-THIN (near miss): good claim, but calibration metrics on tiny lesion-pixel populations are very noisy |
| 0032 | Fit inter-project schema transfer functions from doubly annotated images | 4/4/4/3/2/3/2/4/4/3/3 | R4·U3·ROI2 | — | N | K4-DATA: doubly annotated overlaps between projects are small and unrepresentative |
| 0033 | Tail OV failure is linguistic (name ambiguity), not visual rarity | 4/4/5/4/5/5/4/4/4/5/4 | R3·U4·ROI5 | CF | N | Almost-survived: cheapest clean causal probe in Cluster 1; lost a slot to 0124's stronger version |
| 0034 | Per-class leakage tax from the mutually-exclusive assumption in merged datasets | 3/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0320): the statistical fix is the same; 0320 states it where the practice is dominant |
| 0035 | Annotator fatigue as a correctable within-session quality gradient | 4/2/3/3/2/3/1/2/4/3/2 | R4·U2·ROI2 | — | N | K4-DATA: session timestamps are essentially never released |
| 0036 | Small-fire tail is a resolution artifact, fixable by GSD normalization | 3/3/3/3/3/3/3/3/3/3/3 | R3·U3·ROI3 | — | N | K6-PORT: aerial-pipeline engineering; upsampling cannot create missing information |
| 0037 | Closed-form IoU ceiling from annotation tolerance and object size | 4/5/5/5/5/5/4/4/4/5/4 | R2·U4·ROI5 | CF | **Y** | Derivable on paper, validated in one pass, and flags entire benchmark strata as already at ceiling |
| 0038 | Density maps beat instance masks per annotation dollar for clumped targets | 3/3/3/3/3/3/3/3/3/3/2 | R3·U2·ROI2 | — | N | K1-ENG: format comparison; conclusion sensitive to the counting model chosen |
| 0039 | Classification-derived pruning scores do not transfer to dense fine-tuning | 3/3/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: likely outcome is "dataset redundancy dominates", which is already assumed |
| 0040 | Unknown-pixel semantics is a bigger lever than tuned hyperparameters for OV recall | 4/4/4/4/3/3/4/3/4/4/3 | R3·U4·ROI3 | — | N | K2-THIN: recipe-sensitivity study; interacts with text-alignment method, needing replication to mean anything |

---

## Cluster 2 — Domain Shift / Cross-Domain Transfer (0041–0080)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0041 | Frequency-band attribution of SAM's medical-domain drop | 4/4/4/4/4/5/4/4/4/4/3 | R3·U3·ROI4 | CF | N | K3-DUP (0072): amplitude-only adapter is the stronger, capacity-constrained version of the same measurement |
| 0042 | Grayscale mismatch is a stem-level phenomenon | 3/3/3/4/5/4/4/4/3/5/2 | R2·U2·ROI3 | — | N | K3-DUP (0270 thread): narrow single-modality case of the input-interface question |
| 0043 | Method rankings are not stable across intra-medical shift types | 4/4/4/4/3/2/3/4/4/4/4 | R3·U4·ROI3 | — | N | K5-CMP: 4 shift axes × 5 method families; public data will not fill the cells at matched difficulty |
| 0044 | Prompt-embedding-only test-time adaptation (weights untouched) | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | N | K3-DUP (0279): the prompt-side adaptation surface is retained with a stronger objective |
| 0045 | Night smoke failure: recoverable luminance shift vs destroyed texture | 4/4/4/4/2/3/2/3/4/4/3 | R4·U3·ROI2 | — | N | K4-DATA: fixed-camera day/night pairs *containing smoke in both* are essentially unavailable |
| 0046 | Stain normalization and adapters correct disjoint error sets | 4/3/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: mechanism comparison; likely answer ("partly disjoint") changes little |
| 0047 | Layer-wise drift predicts where adapters must sit | 3/4/4/4/3/2/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0247): duplicate formulation of placement-from-diagnosis |
| 0048 | Turbidity × transparency interaction in underwater segmentation | 4/3/4/4/2/3/1/3/5/4/3 | R4·U3·ROI2 | — | N | K4-DATA: requires purpose-built tank captures; no public factorial exists |
| 0049 | Sensor-noise modeling beats GAN translation for thermal sim-to-real | 4/3/4/4/3/3/2/3/4/4/3 | R3·U3·ROI3 | — | N | K4-DATA: calibrating the noise model needs the target camera or its undisclosed specs |
| 0050 | Adapters transfer to unseen domains better than visual prompts at matched in-domain IoU | 3/4/4/4/3/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0248, 0260): retention/transfer geometry retained with sharper causal controls |
| 0051 | Specialty-to-specialty interference matrix, predicted by domain-embedding distance | 4/4/4/4/2/2/3/4/4/4/4 | R4·U4·ROI2 | — | N | K5-CMP: order permutations across 6 specialties; factorial subsampling weakens the predictive claim |
| 0052 | Drone-viewpoint drop is context priors, not perspective geometry | 3/3/4/3/3/3/3/3/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: three-factor decomposition unlikely to be additive; remedy already known (background augmentation) |
| 0053 | Part of the endoscopy cross-dataset "domain gap" is ontology shift | 4/5/5/4/4/4/3/4/4/5/4 | R3·U5·ROI5 | DM | **Y** | A 150-image bridge re-annotation could show the DA literature has been fitting a label-definition gap |
| 0054 | Which domain-distance metric actually predicts fine-tuning gain | 4/5/4/5/3/2/4/4/4/5/4 | R3·U4·ROI4 | — | **Y** | Turns adaptation planning into a pre-annotation measurement; validated against realized gains, not proxies |
| 0055 | Fog invariance makes models blind to smoke (a "negative domain") | 5/4/5/4/4/4/3/4/5/4/4 | R3·U4·ROI4 | CI·DM | **Y** | Formalizes a class of shift where robustness and sensitivity are in direct conflict; safety-relevant |
| 0056 | Low-res drop = information loss + positional-embedding interpolation | 3/4/4/4/5/4/4/4/3/5/3 | R2·U3·ROI4 | CF | N | K3-DUP (0305, 0125): positional-geometry thread retained with the more surprising claims |
| 0057 | Token-statistics recalibration as the ViT-era replacement for BN adaptation | 4/5/4/4/4/4/4/4/4/4/4 | R3·U4·ROI5 | — | **Y** | If an affine token-statistic match recovers real shift loss, it is adopted everywhere within a year |
| 0058 | Bidirectional transfer asymmetry as a representation-richness metric | 4/4/4/3/2/1/3/3/4/3/3 | R4·U3·ROI1 | — | N | K5-CMP: requires matched-scale pretraining on two corpora; the match itself confounds the asymmetry |
| 0059 | Prompt-type × shift-type robustness matrix | 3/4/4/4/5/5/4/5/3/5/3 | R2·U3·ROI4 | CF | N | K3-DUP (0010, 0144): prompt-type-as-variable question already covered; matrix is a table, not a finding |
| 0060 | Specular highlights: invariance training vs physical simulation | 4/3/4/4/3/3/3/3/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: highlight editing introduces artifacts that confound the counterfactual it depends on |
| 0061 | Human-anatomy fine-tuning helps or hurts veterinary structures by shape divergence | 4/3/4/4/2/3/1/3/5/4/3 | R4·U3·ROI2 | — | N | K4-DATA: labeled veterinary CT would have to be commissioned |
| 0062 | Learned multispectral stem vs pseudo-RGB compositing for satellite smoke | 3/4/3/4/3/3/3/3/3/4/3 | R3·U3·ROI3 | — | N | K6-PORT: input-representation engineering; band advantage will be sensor-specific |
| 0063 | Exchange rate between images-per-site and number of sites | 3/4/4/4/3/2/3/4/3/4/3 | R3·U4·ROI3 | — | N | K5-CMP: (sites × images/site) grids at matched totals; heterogeneous site effects blur one rate |
| 0064 | Does classical UDA add anything on top of frozen foundation features? | 4/5/5/5/3/2/5/5/4/5/5 | R3·U5·ROI4 | DM | **Y** | A null-hypothesis audit that could retire a heavily cited methodology where it no longer applies |
| 0065 | Merging beats routing off-distribution; crossover set by hull position | 3/4/4/4/3/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0251 thread): adapter-combination geometry; router quality confounds the comparison |
| 0066 | Photobleaching as a physically generated live domain shift | 4/2/4/4/3/3/2/3/5/4/3 | R4·U2·ROI2 | — | N | K9-SIZE: bleaching is entangled with real biological change; drift attribution will not be clean |
| 0067 | Adapt to the background only: fix FPs with target-free frames | 4/4/4/4/4/3/4/4/4/4/3 | R3·U4·ROI4 | CI | N | K9-SIZE (near miss): sensitivity may drift silently; the FP/TP separation may not hold globally |
| 0068 | Layout-matched pairs show DA gains are layout, not appearance, adaptation | 4/4/4/4/3/3/2/4/4/4/4 | R3·U4·ROI3 | — | N | K4-DATA: depends on paired renderings whose realism caps external validity |
| 0069 | Shift-magnitude-parameterized calibration correction fitted on source alone | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: real shifts are multi-axis; the low-dimensional parameterization likely breaks where it matters |
| 0070 | Evaluate under measured clinician prompt distributions, not protocol prompts | 4/4/4/4/2/3/1/4/4/4/4 | R4·U4·ROI2 | — | N | K7-HUM: IRB + clinician logging for a result partially obtainable from 0089 |
| 0071 | Detector drift silently shifts the segmenter's input distribution | 4/4/4/4/3/3/3/3/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0217): the same coupling, measured with a cleaner transfer function |
| 0072 | Amplitude-only adapter as a measuring instrument for the "style fraction" of any shift | 5/4/5/5/4/4/4/4/5/4/4 | R3·U4·ROI5 | CI | **Y** | Turns folklore ("site shift is style") into a cheap standard diagnostic with a number attached |
| 0073 | Topology consistency as a label-free adaptation objective for tubular anatomy | 4/4/4/3/3/3/3/3/4/4/3 | R4·U3·ROI3 | — | N | K1-ENG: topology losses are unstable and can "fix" connectivity by hallucinating vessels |
| 0074 | Path dependence of domain-sequence adaptation order | 3/3/4/4/2/2/4/4/3/4/3 | R4·U2·ROI2 | — | N | K5-CMP: 24 orderings for an effect likely smaller than per-domain budget effects |
| 0075 | SAM may segment glass by its reflections, not its boundaries | 5/5/5/4/2/4/2/4/5/4/5 | R4·U5·ROI4 | HRHR·CI | **Y** | Cue attribution by physical intervention; identifies the true generalization bottleneck for transparency |
| 0076 | When does LoRA-delta averaging match centralized fine-tuning? | 4/4/4/4/3/2/3/4/4/4/4 | R3·U4·ROI3 | — | N | K5-CMP: simulated federation misses the dynamics that make real federated adaptation hard |
| 0077 | Distilled SAM variants inherit accuracy but not robustness | 4/4/4/4/4/3/4/5/4/4/3 | R2·U3·ROI4 | — | N | K2-THIN: the expected answer is already the community's prior; public variants differ in more than distillation |
| 0078 | Language as a domain coordinate: text-described domains for zero-data adaptation | 5/4/5/4/3/3/4/3/5/4/5 | R5·U5·ROI3 | HRHR | **Y** | Either opens a zero-data adaptation channel or measures the limit of language–vision domain alignment |
| 0079 | Physics-derived vs searched augmentation for ultrasound, by error mode | 3/3/4/4/3/3/3/3/3/4/3 | R3·U3·ROI3 | — | N | K6-PORT: augmentation engineering; device parameters needed for fidelity are undocumented publicly |
| 0080 | Negative-transfer crossover for mixing source data into fine-tuning | 3/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0315): the anchor-data question is retained in its counter-intuitive form |

---

## Cluster 3 — Evaluation / Calibration / Uncertainty / Robustness (0081–0120)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0081 | Which mask metric predicts downstream clinical measurement error | 4/5/4/4/4/4/4/4/4/4/4 | R2·U4·ROI4 | — | N | Almost-survived: foundational and cheap, but conclusions must be stratified per clinical task, weakening the headline |
| 0082 | Relabeling bootstrap: rank stability under plausible test-set relabelings | 4/5/5/5/4/4/3/5/4/5/5 | R2·U5·ROI5 | CF·DM | **Y** | Gives the community an instrument to separate progress from noise; changes comparison norms, not just one paper |
| 0083 | Medical-SAM rankings are protocol-dependent | 4/5/5/5/5/5/5/5/4/5/4 | R2·U4·ROI5 | CF·DM | **Y** | Pure evaluation on public checkpoints; if rankings move, cross-paper comparison in this subfield is broken |
| 0084 | SAM's predicted-IoU head is miscalibrated out of domain | 4/5/4/5/5/5/4/5/4/5/4 | R2·U4·ROI5 | CF | **Y** | This head silently gates hundreds of auto-labeling and review pipelines and has never been audited |
| 0085 | Existence / extent / boundary uncertainty as separable quantities | 4/4/4/4/3/3/4/3/4/3/3 | R3·U3·ROI3 | — | N | K1-ENG: three estimators plus a routing story; components blur exactly on the small objects that matter |
| 0086 | Estimate web-pretraining contamination of medical benchmarks | 4/4/4/3/3/3/3/3/4/4/4 | R4·U4·ROI3 | — | N | K3-DUP (0294): web-visibility is a proxy; the corpus-free detector is the better instrument |
| 0087 | Corruption, adversarial, and shift robustness are not one property | 3/4/4/4/4/3/4/5/3/4/3 | R2·U3·ROI4 | — | N | K2-THIN: the expected weak-correlation answer is already assumed; ladder matching could manufacture it |
| 0088 | Target-absent FP rate as a first-class metric for rare-event segmentation | 4/5/4/5/4/4/3/4/4/5/4 | R2·U4·ROI4 | CF | N | K3-DUP (0017): same methodology, and 0017 carries a sharper falsifiable ranking claim |
| 0089 | The oracle-prompt inflation factor (GT-derived vs image-only prompts) | 4/5/5/4/3/4/3/4/4/5/4 | R3·U5·ROI4 | DM | **Y** | Every interactive-segmentation number is an upper bound by an unmeasured margin; this measures it |
| 0090 | Size-stratified re-ranking of public checkpoints | 3/4/4/5/5/5/4/5/3/5/3 | R2·U3·ROI4 | CF | N | Almost-survived: very cheap, but the more interesting version of the claim is 0288's scaling crossing |
| 0091 | Prompt ensembles vs weight ensembles vs MC-dropout per unit compute | 3/3/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: benchmark of known estimators; jitter-scale choices likely dominate the result |
| 0092 | Prompt selection breaks conformal exchangeability for mask bands | 4/4/5/4/3/3/4/3/5/4/4 | R4·U4·ROI3 | — | N | K3-DUP (0120, 0337): the "is this uncertainty statistically valid" question is retained twice over |
| 0093 | Oracle vs self-selection of multimask candidates | 4/4/4/5/5/5/4/4/4/5/3 | R2·U4·ROI4 | CF | N | K3-DUP (0269): the same decomposition, but 0269 turns it into an adaptation prescription |
| 0094 | Frame-IoU and temporal stability trade off; alarm metrics follow stability | 3/3/4/4/4/3/3/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: stability metrics exist; GT temporal consistency is itself unreliable |
| 0095 | Worst-case-prompt robustness and certified stable prompt regions | 4/4/4/3/3/2/4/3/5/3/4 | R4·U3·ROI2 | — | N | K9-SIZE: certified bounds on a nonlinear decoder are likely vacuous; empirical part duplicates 0128 |
| 0096 | Class-conditional calibration for extremely imbalanced dense prediction | 3/4/4/4/4/4/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: correct but expected; rare-pixel calibration estimates are high-variance |
| 0097 | A replication test set for a popular medical benchmark | 4/5/4/4/2/3/1/4/4/4/5 | R4·U5·ROI2 | — | N | K4-DATA: needs a data-holding partner and protocol matching that acquisition drift can spoof |
| 0098 | An independent verifier beats self-confidence at predicting failure | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | N | K1-ENG (near miss): a component proposal; the science ("what do verifiers see that the model can't?") stays implicit |
| 0099 | Distribution-valued ground truth for amorphous classes | 4/4/4/4/2/3/2/3/4/3/3 | R4·U3·ROI2 | — | N | K3-DUP (0310): the amorphous-supervision question is retained with a mechanism |
| 0100 | Codec/bitrate robustness curves for amorphous targets | 3/3/3/4/5/4/4/4/3/5/2 | R2·U2·ROI3 | — | N | K6-PORT: deployment engineering; the interesting version of this is 0285's non-monotonicity |
| 0101 | Pixel vs structure vs image abstention granularity | 3/3/4/4/3/3/4/3/3/3/3 | R3·U3·ROI2 | — | N | K7-HUM: workflow simulations need human validation to mean anything |
| 0102 | Relabel only high-disagreement pixels to stress-test rankings | 4/4/4/4/3/3/3/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0082): efficiency variant of the same audit; "correction" is ill-defined where disagreement is genuine |
| 0103 | Analytic propagation from box uncertainty to mask uncertainty | 4/3/4/3/4/3/4/3/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0217): same interface, and decoder mode-switching breaks the smoothness this needs |
| 0104 | Does SAM fail loudly or silently under semantically wrong prompts? | 5/5/5/4/5/5/4/4/5/5/4 | R2·U4·ROI5 | CF | **Y** | Defines and measures a safety property nobody reports; one evaluation pass produces the answer |
| 0105 | Power analysis for dense-prediction comparisons | 3/4/4/5/4/4/4/4/3/4/3 | R2·U4·ROI3 | — | N | K2-THIN: the science is straightforward; impact depends entirely on cultural uptake |
| 0106 | Signed boundary-offset signatures reveal metric-directed optimization | 4/3/4/3/4/4/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: attribution to metric-chasing is confounded by dataset differences |
| 0107 | Text-prompted outputs are more overconfident than point-prompted ones | 3/3/4/3/4/4/3/3/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: prompt modality confounds with target difficulty (users pick text for different targets) |
| 0108 | How much "zero-shot" performance is validation-set prompt search? | 4/5/5/4/4/4/4/4/4/4/4 | R3·U4·ROI5 | DM | **Y** | Zero-shot claims drive deployment planning; this is the cheapest way to find out what they are worth |
| 0109 | Train-test factorial of prompt-modality mixing | 3/3/4/4/2/2/3/3/4/4/3 | R3·U3·ROI2 | — | N | K5-CMP: requires training multimodal promptable models to answer an interface question |
| 0110 | Importance-sampled estimation of deployment-scale false-positive rates | 5/5/4/4/3/3/2/3/5/4/4 | R3·U4·ROI4 | — | **Y** | Makes rare-event FP claims certifiable; the gap between "demo" and "deployable" is exactly this estimator |
| 0111 | Do uncertainty visualizations change expert correction behavior? | 4/3/4/4/2/3/2/3/4/4/3 | R4·U3·ROI2 | — | N | K7-HUM: 12-expert within-subject study with counterbalancing, for a mostly-confirmatory result |
| 0112 | Intervention tests for claimed aleatoric/epistemic disentanglement | 4/4/5/5/4/3/4/4/4/5/4 | R3·U4·ROI4 | DM | N | Almost-survived: a real falsification standard; lost to 0120/0337 which test validity where the practice is most widespread |
| 0113 | Where does augmentation-consistency stop tracking true accuracy? | 3/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: divergence regimes likely dataset-idiosyncratic; the general map won't generalize |
| 0114 | PEFT seed variance vs the effect sizes PEFT papers report | 3/5/5/5/4/3/4/5/4/5/4 | R2·U5·ROI5 | DM | **Y** | If variance rivals claimed gaps, a fast-growing literature is statistically unsupported — and this is measurable now |
| 0115 | Uncertainty should align with rater disagreement, not just error | 4/3/4/4/2/3/1/3/4/4/3 | R3·U3·ROI2 | — | N | K4-DATA: multi-rater datasets rich enough for spatial correlation are scarce |
| 0116 | Clicks-to-quality rankings vs one-shot rankings | 3/4/4/4/4/4/4/4/3/4/3 | R2·U3·ROI4 | CF | N | K2-THIN: divergence is expected; simulated correction policies may not match human ones |
| 0117 | Are method differences mostly binarization-threshold artifacts? | 3/4/4/5/5/5/4/5/3/5/3 | R2·U3·ROI4 | CF | N | K2-THIN: cheap, but the likely finding ("some gaps shrink") is a footnote, not a redirection |
| 0118 | Which benchmarks predict aggregate performance (item analysis)? | 4/4/4/4/3/2/4/4/4/4/4 | R3·U4·ROI3 | — | N | K2-THIN: valuable hygiene, but predictivity estimates are biased by the model population sampled |
| 0119 | Does ImageNet-C-style robustness predict acquisition-artifact robustness? | 4/4/4/4/3/3/3/4/4/4/3 | R3·U3·ROI3 | — | N | K4-DATA: credibility hinges on artifact simulators validated against real artifacts |
| 0120 | Are SAM's multimask candidates a statistically valid uncertainty sample? | 5/5/5/4/5/5/4/4/5/5/4 | R2·U4·ROI5 | CF | **Y** | Either certifies a free uncertainty mechanism thousands of users already rely on, or documents its unsafe failure |

---

## Cluster 4 — Representation Mismatch (0121–0155)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0121 | Standardized representation profiles for SAM / DINOv2 / CLIP features | 4/4/4/4/3/2/4/4/4/4/4 | R3·U4·ROI3 | — | N | K2-THIN: probing batteries are dominated by probe-capacity choices; predictive claim needs a large validation matrix |
| 0122 | Thin-structure quality depends periodically on orientation vs the patch lattice | 5/4/5/4/4/4/4/4/5/4/4 | R3·U4·ROI4 | CI·CF | **Y** | A lattice-induced bias would touch every ViT dense predictor, and synthetic controls make it cheap to test |
| 0123 | Learned windowing tokens preserve absolute CT intensity semantics | 3/3/3/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K6-PORT: input engineering for one modality; gains likely small where geometry dominates |
| 0124 | Text-space collinearity upper-bounds smoke/steam/fog discrimination | 5/4/5/4/4/4/4/4/5/4/4 | R3·U4·ROI5 | CF | **Y** | Localizes a safety-critical confusion to text-anchor geometry, with a clean anchor-substitution intervention |
| 0125 | Center bias: prompted quality declines toward image peripheries | 4/4/4/4/5/5/4/4/4/5/3 | R2·U3·ROI4 | CF | N | Almost-survived: cheap and real, but border/padding artifacts must be separated, and 0305 covers adjacent ground |
| 0126 | Transparency may be an output-format problem, not a feature problem | 5/5/5/4/3/3/2/4/5/4/5 | R3·U5·ROI4 | CI | **Y** | If two-layer probes decode glass from frozen features, an entire research direction is misallocated |
| 0127 | Encoders as band-pass filters vs ultrasound diagnostic bands | 4/3/4/3/3/3/3/3/4/3/3 | R3·U3·ROI2 | — | N | K6-PORT: diagnostic-band definitions vary per application, so the "fit" claim cannot be stated crisply |
| 0128 | The prompt→mask map is discontinuous; discontinuity density predicts interaction cost | 5/4/5/4/4/3/4/4/5/4/4 | R3·U4·ROI4 | CF | **Y** | Defines a geometric usability property of promptable models that training could optimize but nobody measures |
| 0129 | Small-structure failure: information absent or decoder-limited? | 5/5/5/4/4/3/4/4/4/4/4 | R3·U5·ROI5 | — | **Y** | Splits two expensive research directions (better decoders vs higher resolution) with evidence instead of assumption |
| 0130 | Does SAM represent background as a class or as absence? | 4/3/4/4/4/4/4/3/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0104, 0241): the hallucination-under-absence question is retained where it is operational |
| 0131 | Decoder depth requirement scales with target topological complexity | 3/3/4/3/4/3/3/4/3/4/3 | R3·U3·ROI3 | — | N | K1-ENG: depth-scaling study confounded with parameter count; a design rule, not a question |
| 0132 | Where in a VLM does pixel-localizable information collapse? | 5/5/5/4/4/3/4/4/4/4/5 | R3·U5·ROI5 | — | **Y** | Dense-capable VLMs are being built now on intuition; this replaces it with a decay map and tap points |
| 0133 | Native cue-conflict measurement of texture/shape bias for dense models | 4/3/4/3/4/4/4/3/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: synthetic cue-conflict stimuli sit off-manifold, distorting the very weights being estimated |
| 0134 | Is amodal extent decodable from modal-supervised features? | 4/3/4/4/3/3/2/3/4/4/3 | R3·U3·ROI2 | — | N | K4-DATA: amodal GT is scarce and partly conventional, adding label noise to the probe target |
| 0135 | Token merging damages boundaries and small objects, not means | 4/4/4/4/4/4/4/4/4/4/3 | R2·U3·ROI4 | — | N | K2-THIN: the direction of the answer is already believed; findings fragment across merging algorithms |
| 0136 | Is smoke perception achromatic — is color net-negative? | 5/4/5/4/5/5/4/4/4/5/4 | R3·U4·ROI5 | CI·CF | **Y** | Counter-intuitive, immediately actionable for a deployed safety application, and testable on frozen models first |
| 0137 | High-norm outlier tokens co-locate with prompted-segmentation errors | 4/3/4/3/4/4/4/4/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: outlier positions plausibly correlate with genuinely hard content; enrichment will be hard to attribute |
| 0138 | How much 3D structure is already in independent 2D slice features? | 4/4/4/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: slice-spacing heterogeneity blocks comparable measurement across datasets |
| 0139 | Parametric measurement of SAM's compactness/closedness shape prior | 4/3/4/4/4/4/4/3/4/4/3 | R3·U3·ROI3 | CF | N | K9-SIZE: rendered shape families have a synthetic-to-real gap that biases the prior estimate itself |
| 0140 | Is segmentation granularity a linear direction in text-embedding space? | 4/3/4/4/4/4/3/3/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: result likely specific to one text-encoder family |
| 0141 | Early-warning indicators of representation collapse during fine-tuning | 4/4/4/3/3/3/4/3/4/3/3 | R4·U3·ROI3 | — | N | K1-ENG: monitoring-tool proposal; indicator ordering probably differs across optimizers and PEFT types |
| 0142 | What does sliding-window inference lose on gigapixel images? | 4/4/4/4/3/2/3/3/4/4/3 | R3·U3·ROI2 | — | N | K5-CMP: true oracle context is hardware-bounded, capping the ceiling the study can measure |
| 0143 | Are flame features entangled with the illumination flames cast? | 4/4/4/3/3/3/3/3/4/4/3 | R4·U3·ROI3 | — | N | K4-DATA: intrinsic decomposition on fire scenes is not reliable enough to carry the intervention |
| 0144 | Do point / box / mask prompts read different feature subspaces? | 4/3/4/3/4/4/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: attention statistics are a weak proxy for information flow; needs causal patching to conclude anything |
| 0145 | Equivariance debt vs clinical orientation conventions | 3/3/4/3/4/4/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: some orientation dependence is anatomically legitimate, confounding the "bias" reading |
| 0146 | Feature transplant: does the decoder read identity or only geometry? | 5/4/5/3/3/3/4/3/5/3/4 | R4·U4·ROI3 | — | N | K9-SIZE: identity/geometry components probably will not separate cleanly enough to interpret the transplant |
| 0147 | Embedding-space density predicts zero-shot and fine-tuning gain | 3/4/4/3/4/3/4/4/3/4/3 | R4·U3·ROI3 | — | N | K3-DUP (0054): same predictor question, and high-dimensional density estimation is the fragile version |
| 0148 | Do learned upsamplers hallucinate boundary micro-geometry? | 5/4/5/4/3/3/3/3/5/4/4 | R4·U4·ROI3 | CI | N | Almost-survived: distinguishing hallucination from legitimate noise sensitivity needs careful repeat-acquisition design |
| 0149 | Relational language prompts fail dense grounding | 4/4/4/4/4/4/3/4/4/4/4 | R3·U3·ROI3 | — | N | K8-DATE: a snapshot of current VLM weakness; matched-difficulty pairs also need human validation |
| 0150 | Are mask-pretrained features sufficient for depth, normals, ownership? | 4/4/4/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: cross-task profile is dominated by probe design; the expected profile is roughly the prior |
| 0151 | Scanner fingerprint strength as a pre-screen for shortcut vulnerability | 4/4/4/4/4/3/3/4/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: decodability is necessary but not sufficient for shortcut adoption, which weakens prediction |
| 0152 | Local phase coherence carries thin-structure continuity | 4/3/4/3/3/3/3/3/4/3/3 | R4·U3·ROI2 | — | N | K9-SIZE: local phase-scrambling methodology is delicate; global scrambling destroys too much to interpret |
| 0153 | Prompt saturation is architectural (attention dilution), not informational | 4/4/4/4/4/4/4/4/4/4/3 | R3·U3·ROI3 | CF | N | K3-DUP (0282): the click-response pathology is retained in its more surprising non-monotonic form |
| 0154 | Fire is a dynamic texture mis-modeled by static object priors | 4/4/4/3/3/3/3/3/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: temporal baselines add architecture confounds beyond the static/dynamic distinction being tested |
| 0155 | Can epistemic uncertainty be linearly read from frozen features? | 4/4/4/4/4/4/4/4/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: linear probes likely capture dataset-difficulty proxies rather than transferable uncertainty |

---

## Cluster 5 — Multimodal Supervision (0156–0185)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0156 | Exchange rate between report-supervised and pixel-labeled images | 4/5/4/4/3/3/3/4/4/5/4 | R3·U4·ROI4 | — | **Y** | Prices an idle hospital-scale data asset with a clean iso-performance grid; directly changes budget decisions |
| 0157 | Which components of the thermal advantage are RGB-recoverable? | 4/4/5/4/2/3/2/3/4/4/4 | R4·U4·ROI2 | — | N | K4-DATA: paired RGB–thermal fire footage is too limited for a recoverability decomposition |
| 0158 | Fire crackle audio as temporal anchors for visual learning | 5/3/4/3/2/3/2/3/5/4/3 | R4·U3·ROI2 | — | N | K4-DATA: surveillance audio is wind- and codec-destroyed, and archives with both audio and masks are rare |
| 0159 | RGB-D invalid-depth pixels as free transparency supervision | 5/5/4/4/4/3/5/4/5/4/4 | R4·U5·ROI5 | HRHR | **Y** | Physics-generated labels at zero annotation cost could produce the largest transparency corpus in existence |
| 0160 | Word-region vs sentence-level alignment for dense outcomes | 4/4/4/4/2/1/3/3/4/4/4 | R4·U4·ROI2 | — | N | K5-CMP: matched pretraining runs; conclusions at reachable scale will be trend arguments |
| 0161 | Registered CT–MRI disagreement as a pseudo-label filter | 4/4/4/3/3/3/3/4/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: registration error itself generates disagreement, contaminating the signal being validated |
| 0162 | Polarization as privileged supervision transferable to RGB inference | 5/4/5/4/3/3/2/3/5/4/4 | R5·U5·ROI3 | HRHR | **Y** | Either yields a capture-once-deploy-everywhere recipe or proves the polarization cue has no RGB correlate |
| 0163 | Surgical narration as weak dense supervision | 4/4/4/3/2/2/1/3/4/4/3 | R4·U3·ROI2 | — | N | K4-DATA: narrated-procedure corpora with mask subsets are not publicly accessible |
| 0164 | Information content of radiologist gaze for lesion localization | 4/4/5/4/2/3/2/3/4/4/4 | R4·U4·ROI2 | — | N | K4-DATA: gaze-tracked reading datasets with masks are scarce; noise structure needs its own model |
| 0165 | NIR/visible transmission ratio as physical smoke-density supervision | 5/4/4/4/2/2/1/2/5/4/4 | R5·U4·ROI2 | — | N | K4-DATA: requires paired NIR-RGB rigs at controlled burns plus transmissometer validation |
| 0166 | Hallucination-weighted VLM captions as dense supervision | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | N | K3-DUP (0186, 0189, 0241): the structured-synthetic-noise question is retained three times over |
| 0167 | How much paired data does a text→prompt-space bridge need? | 4/4/4/4/4/3/4/4/4/5/3 | R3·U3·ROI4 | — | N | K1-ENG: bridge-building exercise; the prompt space may lack the semantic axes regardless of data |
| 0168 | Two-axis surface: report-contrastive volume × pixel-label volume | 3/4/4/4/2/2/3/4/3/4/3 | R3·U3·ROI2 | — | N | K3-DUP (0156): same production function, sparser grid, more compute |
| 0169 | Cardiac-pulse motion as automatic vessel labels in endoscopy | 5/4/4/3/2/3/1/3/5/4/3 | R5·U4·ROI2 | — | N | K4-DATA: camera and tissue motion swamp the cardiac band in most accessible footage |
| 0170 | Natural-language error critiques as a supervision channel | 5/4/4/3/2/3/2/3/5/3/4 | R4·U4·ROI2 | — | N | K7-HUM: critique collection at matched expert minutes is costly, and structuring the text erodes the naturalness claim |
| 0171 | Device acoustics as active-instrument labels | 4/3/4/3/2/3/1/3/4/4/3 | R4·U3·ROI2 | — | N | K4-DATA: OR audio is access-restricted and device-sound mapping varies per room |
| 0172 | Cross-view geometric consistency as an annotation substitute in the OR | 3/3/4/3/2/3/2/3/3/4/3 | R4·U3·ROI2 | — | N | K4-DATA: multi-view OR datasets are rare, and non-rigid anatomy violates the geometry assumed |
| 0173 | Text vs extra clicks for resolving ambiguity, per user-second | 4/4/4/4/3/3/3/4/4/4/3 | R3·U3·ROI3 | — | N | K7-HUM: user study whose result depends on the model's current text quality (dates fast) |
| 0174 | Does language supervision blur boundaries? A dose-response test | 5/4/5/4/4/3/4/4/5/4/4 | R3·U4·ROI4 | CI·DM | **Y** | Names the unmeasured cost side of the rush toward language-native dense models, with a falsifiable dose-response |
| 0175 | Meteorological conditioning: ambiguity resolution vs wind-aligned hallucination | 4/3/4/4/3/3/2/3/4/4/3 | R4·U3·ROI2 | — | N | K9-SIZE: public met data resolution is far coarser than camera scenes |
| 0176 | DICOM acquisition metadata as a free conditioning channel | 3/4/3/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K6-PORT: conditioning engineering; metadata completeness varies by institution and vendor |
| 0177 | Restain-and-register IHC as molecular ground truth for H&E | 5/5/4/4/2/3/1/3/5/4/5 | R5·U5·ROI2 | HRHR | N | Almost-survived: the highest-upside supervision idea in the cluster, but needs a wet lab and restaining alters tissue |
| 0178 | LiDAR dropout as volumetric weak labels for camera smoke perception | 5/4/4/4/2/3/2/3/5/4/4 | R4·U4·ROI2 | — | N | K4-DATA: synchronized logs through smoke are rare; dust/rain/exhaust contaminate the label channel |
| 0179 | Atlas priors injected through the prompt interface instead of the loss | 4/4/4/4/4/3/3/4/4/4/3 | R3·U3·ROI3 | — | N | K1-ENG: a prior-injection mechanism; prompt bandwidth may simply be too narrow to carry a spatial prior |
| 0180 | Is multimodal supervision order non-commutative? | 4/4/5/4/2/1/3/3/4/4/4 | R4·U4·ROI2 | — | N | K5-CMP: pretraining-order experiments at two scales; conclusions hinge on relative supervision volumes |
| 0181 | Spoken relative corrections as a sterile mask-editing channel | 4/3/3/3/3/3/3/3/4/4/3 | R4·U2·ROI2 | — | N | K7-HUM: ASR error in clinical noise likely dominates the interaction cost being measured |
| 0182 | Certified absence in reports as class-specific hard-negative supervision | 5/5/4/4/4/3/3/4/5/4/4 | R3·U4·ROI5 | — | **Y** | Report negations are free, expert-authored, and aimed precisely at the hallucinations that cause alarm fatigue |
| 0183 | Flow-discontinuity boundaries as a motion teacher for smoke edges | 4/3/4/3/3/3/3/3/4/4/3 | R4·U3·ROI2 | — | N | K9-SIZE: flow estimation degrades inside smoke — noisiest exactly where the supervision is needed |
| 0184 | Contrast-derived vessel labels encode a perfusion selection bias | 5/5/5/4/3/3/3/3/5/4/4 | R3·U4·ROI4 | CI·DM | **Y** | A paradigm case of physically generated labels whose bias opposes the clinical use, with the correction priced |
| 0185 | Do dense VLMs regress toward the textbook when image evidence is weak? | 5/5/5/4/3/3/3/3/5/4/5 | R4·U5·ROI4 | HRHR·DM | **Y** | "Prior-conforming segmentation of abnormal anatomy" is the worst conceivable medical-VLM failure and is untested |

---

## Cluster 6 — Synthetic Data Pitfalls (0186–0215)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0186 | Does generative augmentation cover the tail it is prescribed for? | 5/5/5/4/3/3/3/4/5/4/5 | R3·U5·ROI5 | DM | **Y** | If synthesis reproduces the skew it is supposed to fix, the field's main scarcity remedy is a placebo |
| 0187 | Optical fidelity vs context realism in transparency rendering | 4/3/4/4/3/2/3/3/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: fidelity and context interact through renderer specifics, blocking clean factor separation |
| 0188 | Scattering accuracy vs shape realism in simulated smoke | 4/3/4/4/3/2/2/3/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: same confound, plus noisy real-smoke evaluation labels |
| 0189 | Do models trained on inpainted lesions learn the paste, not the lesion? | 5/5/5/4/4/4/4/4/4/5/4 | R2·U4·ROI5 | CI·CF | **Y** | A circularity flaw in a fast-spreading augmentation practice, detectable with a cheap fingerprint classifier |
| 0190 | Synthetic-fraction threshold beyond which robustness silently degrades | 4/5/4/4/3/2/4/4/4/4/4 | R3·U4·ROI4 | — | **Y** | The monitoring instrument the field needs before synthetic-heavy training becomes irreversible practice |
| 0191 | Which errors amplify across generations of self-consuming auto-labeling? | 5/5/5/4/3/2/4/4/5/4/5 | R3·U5·ROI4 | — | **Y** | Defines the stability conditions of the data flywheel everyone is now building on |
| 0192 | Does copy-paste augmentation erode legitimate context reasoning? | 4/3/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: verdict is task-dependent by construction, so the paper ends in "report per stratum" |
| 0193 | Programmatic training prompts vs human prompt distributions | 4/5/4/4/3/3/3/4/4/4/4 | R3·U4·ROI4 | — | **Y** | A training-recipe variable nobody reports, with a nearly free fix, aimed at the deployment gap inside the interface |
| 0194 | Error-mode signatures of GAN / diffusion / simulation data | 4/3/4/4/3/2/3/3/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: signatures likely reflect implementation choices rather than paradigm essence |
| 0195 | Does privacy-motivated synthetic replacement preserve subgroup equity? | 4/5/4/4/3/3/2/4/4/4/4 | R3·U4·ROI3 | — | N | K4-DATA: subgroup labels are incomplete in most datasets, capping audit resolution |
| 0196 | Physics violations in text-to-image fire data and their downstream cost | 4/4/4/4/4/3/4/3/4/4/3 | R3·U3·ROI3 | — | N | K1-ENG: rule-based auditor tool; rules cover only auditable violations, missing statistical wrongness |
| 0197 | Which synthetic-data statistics predict transfer (is FID the wrong target)? | 4/5/4/4/2/2/3/4/4/4/4 | R3·U4·ROI3 | — | N | K5-CMP: 30+ synthetic variants trained end to end; predictor validity may be task-family-specific |
| 0198 | The controllability–realism frontier for medical synthesis | 3/4/4/4/3/2/3/3/3/4/3 | R4·U3·ROI2 | — | N | K9-SIZE: frontier position will reflect implementation quality more than paradigm |
| 0199 | Auditing generator compositional blind spots before training on output | 4/4/4/4/3/3/3/3/4/4/3 | R4·U3·ROI3 | — | N | K1-ENG: audit tooling whose verifier shares blind spots with the generator it audits |
| 0200 | Pixel-perfect synthetic labels may teach the wrong boundary tolerance | 5/4/5/4/4/3/4/4/5/4/4 | R3·U4·ROI4 | CI | **Y** | Inverts a data-quality intuition and prescribes deliberately degrading labels — cheap to run, hard to ignore |
| 0201 | Do generated hard negatives patch or warp decision boundaries? | 4/4/4/4/3/3/2/3/4/4/3 | R4·U3·ROI3 | — | N | K4-DATA: verification needs real confuser sets (real steam near infrastructure) that barely exist |
| 0202 | k-space vs image-space synthesis of MRI artifacts | 4/4/4/4/3/3/2/3/4/4/3 | R3·U3·ROI3 | — | N | K4-DATA: real artifact-labeled evaluation scans require scanner cooperation |
| 0203 | Marginal transfer value per domain-randomization axis | 3/3/4/4/3/2/3/3/3/4/3 | R3·U3·ROI3 | — | N | K6-PORT: rendering-budget engineering; axis interactions defeat clean marginal attribution |
| 0204 | Does restricted-data ancestry leak through synthetic intermediaries? | 5/5/4/4/3/2/3/3/5/4/5 | R5·U4·ROI2 | HRHR | N | K9-SIZE: a null result is unfalsifiable (true insulation vs weak attack), and policy relevance cannot rescue that |
| 0205 | Counterfactual pairs vs independent samples: the effective-sample multiplier | 4/4/4/4/3/3/3/3/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: edit artifacts are a ready shortcut; artifact controls may absorb the measured multiplier |
| 0206 | Do synthetic-trained models depend on generator frequency fingerprints? | 4/4/4/4/4/3/4/3/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0189): artifact-reliance question retained where the practice is most consequential |
| 0207 | Joint real × synthetic scaling law with a substitution rate | 4/5/4/4/2/1/3/4/4/4/4 | R4·U4·ROI2 | — | N | K5-CMP: log-spaced two-resource grid; fitted parameters date with generator quality |
| 0208 | Sharp occlusion-generalization phase transitions under controlled rendering | 4/3/4/4/3/2/3/3/4/4/3 | R4·U3·ROI2 | — | N | K9-SIZE: rendered occlusion statistics miss real occluder correlations, which is where the claim would matter |
| 0209 | Compositing-pipeline overfitting in matting-based smoke synthesis | 4/3/4/4/4/3/3/3/4/4/3 | R4·U2·ROI3 | — | N | K9-SIZE: pipeline differences may be too subtle to matter under augmentation-heavy training |
| 0210 | Site-twin synthetic data vs generic synthetic data for fixed cameras | 4/4/4/4/2/2/2/3/4/4/3 | R4·U3·ROI2 | — | N | K6-PORT: deployment engineering with twin-maintenance costs that dominate the measured advantage |
| 0211 | How far can latent augmentation push before masks become invalid? | 4/3/4/4/4/3/4/3/4/4/3 | R3·U3·ROI3 | — | N | K1-ENG: a validity-checker deliverable whose checker shares failure modes with the generator |
| 0212 | Simulator fitting vs randomization, selected by fit residual | 4/4/4/4/3/2/3/3/4/4/3 | R3·U3·ROI3 | — | N | K1-ENG: decision-rule engineering; statistic-matching objectives are gameable by degenerate parameters |
| 0213 | Can model selection outsource to synthetic validation data? | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI4 | — | N | K2-THIN: likely answer ("coarse decisions transfer, fine ones don't") is the prior; selection/gap correlations bias it |
| 0214 | Memorization–utility frontier for medical diffusion augmentation | 4/5/4/4/2/2/2/3/4/4/4 | R4·U4·ROI2 | — | N | K5-CMP: regularization × duration grids plus extraction attacks; conclusions remain attack-relative |
| 0215 | Does multi-generator mixing decorrelate artifacts or accumulate them? | 4/4/4/4/2/2/2/3/4/4/3 | R4·U3·ROI2 | — | N | K5-CMP: needs 5 architecturally diverse capable generators per domain, which do not exist for most domains |

---

## Cluster 7 — Detection Limitations (0216–0245)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0216 | Compute-optimal operating surface for sub-10-pixel plume detection | 3/4/3/4/4/3/3/4/3/4/3 | R3·U3·ROI3 | — | N | K6-PORT: deployment optimization; optimal points likely camera- and scene-specific |
| 0217 | The box→mask error transfer function, and matching the segmenter's training noise to it | 4/5/4/5/4/3/4/5/4/5/4 | R2·U4·ROI5 | — | **Y** | The dominant production architecture's unmodeled interface, with a zero-inference-cost fix |
| 0218 | Is the open-vocabulary "stuff gap" alignment or region generation? | 4/4/5/4/4/3/3/4/4/4/4 | R3·U4·ROI4 | — | N | K3-DUP (0219): same diagnosis (object-centric machinery, not features), cheaper instrument in 0219 |
| 0219 | Is duplicate suppression the binding constraint for amorphous targets? | 5/4/5/4/4/4/3/4/5/4/4 | R3·U4·ROI4 | CI | **Y** | Attributes a chronic failure to a specific replaceable pipeline stage, not to feature quality where effort now goes |
| 0220 | Annotation-jitter ceiling propagated through detection matching | 4/4/4/4/4/4/4/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0037): the ceiling derivation is retained for masks, which is the cleaner formulation |
| 0221 | Temporal information-value curve for low-contrast smoke | 3/3/4/4/4/3/3/4/3/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: frame rates and compression differ so widely that one curve will not unify |
| 0222 | Where does mask-derived objectness fail vs classical proposals? | 4/4/4/4/4/4/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: capacity matching between proposal mechanisms is contestable enough to weaken any conclusion |
| 0223 | Label assigners systematically starve elongated objects of gradient | 5/5/5/5/4/3/4/5/4/5/4 | R2·U4·ROI5 | CI | **Y** | A training-logic fix, universal across detectors, for a safety-critical object family — and cheap to instrument |
| 0224 | The crowding threshold where detection must become density estimation | 3/4/4/4/4/3/3/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: real crowding correlates with staining and focus, confounding the pure-density attribution |
| 0225 | Which confidence component decalibrates first under shift? | 4/4/4/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: some detector families entangle the scores irrecoverably, fragmenting coverage |
| 0226 | One contrast–recall law unifying camouflage, transparency, and low-contrast lesions | 5/5/5/4/4/4/4/4/5/4/5 | R4·U5·ROI4 | DM | **Y** | If the curves collapse, three separate literatures should be merged; if not, the differences become precise |
| 0227 | Marginal FP-reduction value per hard-negative category | 4/4/4/4/4/3/3/4/4/4/3 | R3·U4·ROI4 | — | N | Almost-survived: highly actionable, but category value interacts with positive-set composition, needing a joint design |
| 0228 | Energy–latency–recall frontier for always-on edge fire detection | 3/4/3/4/3/2/3/4/3/4/3 | R3·U3·ROI2 | — | N | K6-PORT: hardware-specific energy results will not generalize across edge platforms |
| 0229 | Economic crossover between training a detector and prompting a foundation model | 4/4/4/3/3/3/3/3/5/4/3 | R4·U3·ROI3 | — | N | K8-DATE: cost parameters drift with every model release; only the framework survives |
| 0230 | Center-line matching instead of box IoU for elongated objects | 4/4/4/4/4/4/4/4/4/4/3 | R3·U3·ROI4 | — | N | K2-THIN: derived center-line GT adds a processing-noise layer to a metric-redesign argument |
| 0231 | Excess recall penalty for edge-truncated targets | 4/4/4/4/4/4/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: data-vs-architecture attribution will not separate cleanly; remedy (truncation augmentation) already obvious |
| 0232 | Instance-decomposition conventions as a hidden training-noise source | 4/3/4/4/3/3/3/3/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: hierarchical matching relaxes evaluation, so the gain is partly definitional |
| 0233 | What does a learned detector add over background-model change detection? | 5/5/5/4/4/3/3/4/5/5/4 | R3·U5·ROI5 | DM·CI | **Y** | A deflationary question with large compute stakes that the monitoring literature has never asked cleanly |
| 0234 | Query-utilization scaling law for dense-instance scenes | 3/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: attention-collapse behavior near saturation is likely DETR-variant-specific |
| 0235 | Does open-vocabulary detection know near-vocabulary unknowns? | 4/4/4/4/4/4/3/4/4/4/4 | R3·U3·ROI3 | — | N | K8-DATE: a snapshot of current OV models; semantic and visual proximity axes are hard to control jointly |
| 0236 | How weak can fire-detection labels be (timestamps → boxes)? | 4/4/4/4/2/3/2/3/4/4/3 | R4·U3·ROI2 | — | N | K4-DATA: validating exchange rates needs archives that are both fully labeled and timestamped |
| 0237 | Scale interpolation works, extrapolation does not | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: scale extrapolation entangles with resolution and blur; the fix (equivariance) is already the known answer |
| 0238 | Objectness-distilled detector initialization | 3/3/3/3/4/3/4/4/3/4/3 | R3·U2·ROI2 | — | N | K1-ENG: initialization engineering, and the gain may be replicable by just using the foundation model |
| 0239 | Event-level (deduplicated) evaluation for camera networks | 4/4/4/4/3/3/2/4/4/4/3 | R3·U3·ROI3 | — | N | K4-DATA: multi-camera event GT with cross-camera association is scarce |
| 0240 | Spatial precision ceiling of VLM-proposed boxes as prompts | 4/4/4/4/4/4/4/4/4/4/4 | R3·U3·ROI4 | — | N | K8-DATE: defines today's automation boundary; numbers obsolete within a release cycle |
| 0241 | Leading questions: hallucinated detections under prevalence expectations | 5/5/5/4/5/4/4/4/5/5/5 | R2·U5·ROI5 | CI·CF | **Y** | Text-driven monitoring is productizing now; this measures its worst failure mode before norms solidify |
| 0242 | Zoom policies as budgeted sequential decisions | 3/4/3/4/3/2/3/4/3/4/3 | R3·U3·ROI2 | — | N | K1-ENG: policy-learning method; policies overfit dataset-specific spatial priors |
| 0243 | Deblur-then-detect vs blur-robust features for tiny plumes | 4/4/4/4/3/3/2/3/4/4/3 | R4·U3·ROI3 | — | N | K3-DUP (0338): the restoration-destroys-signal claim is retained in its sharper forensic form |
| 0244 | FP processes are episode-clustered, so FP/frame mispredicts FP/day | 5/5/4/4/2/3/1/3/5/4/4 | R4·U4·ROI2 | — | N | K4-DATA: needs long-duration labeled monitoring logs that are scarce and site-idiosyncratic |
| 0245 | Prompt the segmenter with the detector's score distribution, not its top-1 | 4/4/4/4/5/4/4/4/4/5/3 | R2·U3·ROI4 | — | N | K1-ENG: an interface tweak; decoders trained on single-intent prompts may simply reject the aggregate |

---

## Cluster 8 — Parameter Efficiency vs Quality (0246–0280)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0246 | The intrinsic rank of a domain shift, predictable before training | 4/4/4/4/3/2/4/4/4/4/4 | R3·U4·ROI3 | — | N | Almost-survived: turns the most-tuned PEFT knob into a measurement, but knees are optimizer-dependent and 0306's inversion of the same knob is sharper |
| 0247 | Adapter placement predicted from shift diagnosis | 3/4/4/4/3/2/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0253): placement-from-diagnosis retained with a causal double-dissociation design |
| 0248 | Does low rank causally protect zero-shot generality? The retention frontier | 4/5/5/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | DM | **Y** | Tests whether "LoRA forgets less" is causal geometry or just undertraining, at matched target IoU — the folklore every adapter deployment leans on |
| 0249 | Does the classification PEFT ranking break on dense tasks? | 3/4/4/4/3/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: per-method tuning quality will dominate family essence; the reorder claim can't be separated from tuning culture |
| 0250 | Prompt tokens express only spatially low-rank corrections | 4/3/4/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: deep prompt variants blur the global-only characterization the claim rests on |
| 0251 | Merge-or-retrain predicted from task-vector geometry | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | **Y** | Turns routine adapter consolidation from a gamble into a weight-space calculation, validated against joint training |
| 0252 | Where does 4-bit quantization damage go? | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K2-THIN: boundary-concentrated damage is the expected answer; findings fragment across quantization families |
| 0253 | Attention adapts "where", MLP adapts "what" (causal placement test) | 5/4/5/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | **Y** | A double dissociation that would give PEFT placement a mechanism; anchors the placement thread (0047, 0247, 0264 killed into it) |
| 0254 | Adapter arithmetic: does organ A + organ B = both organs? | 4/4/4/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0251): composition/interference geometry retained via merge prediction; boundary-zone errors are its evaluation appendix |
| 0255 | The PEFT-vs-full-FT crossover map | 3/4/4/4/3/2/4/4/3/4/3 | R3·U3·ROI2 | — | N | K5-CMP: data ladders × shifts × two regimes, and crossovers drift with model scale — cartography that dates |
| 0256 | Sensitivity-guided rank allocation across layers | 3/3/3/4/3/3/4/4/3/4/3 | R3·U3·ROI2 | — | N | K1-ENG: budget-allocation method; Fisher sensitivity may mispredict where low-rank helps |
| 0257 | The boundary tax of parameter efficiency | 4/5/5/4/4/3/4/4/4/4/4 | R3·U4·ROI5 | CI·DM | **Y** | If PEFT-equals-full-FT is a region-metric artifact, the equivalence claims driving clinical PEFT adoption systematically overpromise |
| 0258 | Prompt-encoder-only personalization to user click style | 4/4/4/4/2/3/2/4/4/4/3 | R4·U3·ROI2 | — | N | K4-DATA: per-user prompt logs are not public and must be collected under IRB-adjacent constraints |
| 0259 | Does update geometry matter beyond parameter count? | 4/4/4/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: optimizer interactions with each geometry masquerade as geometric effects; the isolation the claim needs may not exist |
| 0260 | Adapters overfit sites harder (update locality vs transfer) | 4/4/5/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | CI·DM | **Y** | Inverts the "conservatism aids generality" folklore with a matched-performance design; the multi-site reversal makes it mechanistic |
| 0261 | Gradient-free PEFT feasibility envelope | 4/3/3/4/3/3/4/4/4/4/3 | R4·U3·ROI2 | — | N | K1-ENG: black-box optimization engineering; zeroth-order variance may cap gains below usefulness |
| 0262 | Forgetting dynamics of sequential adapter rollouts | 3/4/4/4/3/2/3/4/3/4/3 | R3·U3·ROI2 | — | N | K5-CMP: 12-site longitudinal grids per strategy, and simulated rollouts miss the temporal drift that makes the question real |
| 0263 | Does PEFT recover calibration or only accuracy? | 4/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: plausible-and-expected; small-target calibration estimates are noisy exactly where the claim matters |
| 0264 | Depth-capacity law of injected prompts | 4/3/4/3/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0253): placement-from-mechanism thread anchored there; residual-stream shortcuts muddy the depth theory |
| 0265 | Optimal granularity for scanner-specific micro-adapters | 3/4/3/4/3/3/3/4/3/4/3 | R3·U3·ROI2 | — | N | K6-PORT: operational design rule; metadata reliability and fleet specifics dominate the answer |
| 0266 | Warm-starting adapters from accumulated task vectors | 3/3/3/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K1-ENG: initialization engineering with negative-transfer risk exactly in the low-data regime it targets |
| 0267 | Component-wise adaptation value (is the decoder the right place to spend?) | 4/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: "upsampler owns boundaries, backbone owns semantics" is already the prior; component boundaries differ across architectures |
| 0268 | Difficulty-routed heterogeneous adapter capacity | 3/3/3/3/3/3/4/4/3/3/3 | R4·U3·ROI2 | — | N | K1-ENG: routing architecture whose overhead and instability can eat the allocation gains |
| 0269 | Selection-head-only adaptation for granularity-convention gaps | 5/5/5/4/4/4/4/4/4/5/4 | R3·U5·ROI5 | CI·CF | **Y** | The oracle-candidate audit is nearly free and could reclassify part of the medical-SAM adaptation literature as selection problems solved with generation-sized tools |
| 0270 | Is the input stem the whole story for modality shift? | 4/4/5/4/4/3/4/4/4/5/4 | R3·U4·ROI4 | CI | **Y** | "The transformer is an input-agnostic computer" is a clean falsifiable claim splitting modality gap into interface vs semantics; anchors 0042's thread |
| 0271 | Allocated vs used: effective-rank dynamics of LoRA | 4/3/4/4/4/3/4/4/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: spectral utilization is optimizer-shaped (Adam preconditioning), so the diagnostic may measure the optimizer, not the task |
| 0272 | Capacity as regularization: are small adapters implicitly noise-robust? | 4/4/5/4/4/3/4/4/4/5/4 | R3·U4·ROI4 | CI | **Y** | A sign-reversal claim — PEFT accuracy-optimal, not a compromise, under noisy labels — tested by controlled injection; inverts the efficiency-quality frame where labels are noisiest |
| 0273 | Hypernetwork-generated adapters from unlabeled samples | 4/4/3/3/2/2/4/3/4/3/3 | R5·U4·ROI2 | — | N | K1-ENG: amortization machinery; the domain-to-update mapping may be too multimodal for regression |
| 0274 | Spectral-token adapters for global shifts | 3/3/3/4/3/3/4/4/4/4/3 | R3·U3·ROI2 | — | N | K1-ENG: adapter-parameterization proposal; attention's existing global mixing muddies attribution |
| 0275 | Train-time vs inference-time capacity at matched compute | 3/3/4/3/4/3/4/4/3/3/3 | R3·U3·ROI3 | — | N | K2-THIN: the substitution-fraction answer is expected, and compute bookkeeping across regimes is contestable enough to absorb the result |
| 0276 | Matryoshka adapters: one run, every deployment size | 3/3/2/4/4/3/4/4/3/4/3 | R3·U3·ROI2 | — | N | K1-ENG: deployment convenience engineering; the question is a deliverable |
| 0277 | Adapter-subspace Monte Carlo uncertainty | 3/3/3/3/4/3/4/4/3/4/3 | R3·U3·ROI2 | — | N | K1-ENG: cheap-uncertainty method; per-task perturbation calibration erodes the cheapness claim |
| 0278 | Does the adapter create a new adversarial attack surface? | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: the white-box threat model makes the headline conditional; certification relevance depends on attacker assumptions few deployments match |
| 0279 | Label-free PEFT: distilling prompt-ensemble consensus into adapters | 4/5/4/4/4/3/4/4/4/4/4 | R3·U4·ROI5 | — | **Y** | The consistency anchor is unique to promptable models; if collapse-resistant, it gets applied at essentially every deployment — anchors 0044/0317 |
| 0280 | Cross-scale adapter transplantation | 3/3/3/3/3/3/4/4/4/4/3 | R4·U3·ROI2 | — | N | K1-ENG: alignment engineering; cross-scale correspondence may be too nonlinear for the linear maps proposed |

---

## Cluster 9 — Surprising Empirical Phenomena (0281–0315)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0281 | The off-center click advantage | 4/3/4/4/5/5/4/4/4/5/3 | R3·U3·ROI4 | CF | N | K3-DUP (0128): dense click-grid response surfaces retained there; placement optimization is the engineering tail of that map |
| 0282 | Non-monotonic refinement: when more clicks make masks worse | 5/4/5/4/4/4/4/4/5/5/4 | R2·U4·ROI5 | CI·CF | **Y** | Breaks the monotone-improvement contract click-efficiency metrics assume; candidate-trajectory logging pins the mode-switch mechanism on frozen models |
| 0283 | Cross-organ transfer as objectness/convention recalibration | 4/4/4/4/3/3/4/4/4/4/3 | R4·U4·ROI3 | — | N | K3-DUP (0269): the convention-vs-content decomposition survives there with a cheaper instrument; transfer magnitudes may be too small for swap attribution |
| 0284 | Augmentation inversion at low data | 4/4/4/4/4/3/4/4/3/4/3 | R3·U4·ROI3 | — | N | K9-SIZE: inversion points likely dataset-idiosyncratic; the general boundary the prescription needs may not exist |
| 0285 | Compression that helps: JPEG as a matched filter for smoke | 5/4/5/4/5/5/4/4/4/5/4 | R3·U4·ROI5 | CI·CF | **Y** | Beneficial degradation inverts the input-quality dogma with a spectral mechanism and a frozen-model kill test; also a caution for robustness benchmarking |
| 0286 | Subgroup regression under fine-tuning | 4/5/4/4/4/3/3/4/3/4/4 | R3·U4·ROI3 | DM | N | Almost-survived: the right clinical question, but the core mechanism (fine-tuning trades pretrained robustness; interpolation recovers) is substantially documented for classification, and subgroup metadata caps audit resolution |
| 0287 | Color as a saboteur: grayscale beats RGB cross-site | 4/4/4/4/4/3/4/4/4/4/3 | R3·U4·ROI4 | CI | N | K3-DUP (0136): the color-net-negative question is retained where it is safety-critical; the endoscopy variant adds site-transfer control but the same mechanism |
| 0288 | Bigger models, smaller structures: an inverse-scaling pocket | 5/5/5/4/4/3/4/4/4/4/4 | R3·U5·ROI4 | CI·DM | **Y** | A verified crossing overturns scale-is-all procurement exactly where small things matter most; size-stratified ladders on public checkpoints are cheap |
| 0289 | The random-decoder anomaly | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0129): the information-vs-decoder split is measured there; probing-predicts-decoder-value is its corollary |
| 0290 | Why do prompted models benefit unevenly from TTA? | 3/3/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K1-ENG: selective-TTA policy engineering; the value predictor likely captures dataset difficulty proxies |
| 0291 | Anti-curriculum: hard-first fine-tuning | 4/3/4/3/4/3/4/4/3/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: difficulty-scoring choices dominate ordering effects; the curriculum literature's contradictions will reproduce |
| 0292 | Training-time prompt jitter buys calibration for free | 4/3/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0193): training-time prompt-distribution effects retained there; the calibration decoupling risks being metric-specific |
| 0293 | The freezing paradox: early layers matter more for "closer" domains | 4/4/4/4/4/3/4/4/4/4/3 | R3·U4·ROI3 | CI | N | K3-DUP (0054): adaptation-depth demand is the layer-resolved version of the distance-predictor question 0054 answers against realized gains |
| 0294 | Bimodal loss residuals detect pretraining contamination | 5/5/4/4/4/4/4/3/5/4/4 | R4·U5·ROI4 | HRHR | **Y** | A corpus-free contamination detector would be applied to every benchmark and model; if difficulty regression separates the modes, the field gains an instrument it cannot currently buy |
| 0295 | SR preprocessing: real detail, smoothing, or hallucination? | 4/4/4/4/4/3/4/4/4/4/3 | R3·U4·ROI3 | — | N | K3-DUP (0331): the guidance-parameterized frontier with the seed-ensemble detector subsumes this decomposition |
| 0296 | Spatially structured label smoothing breaks the sharpness tradeoff | 3/3/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0310): the soft-supervision-to-confidence mapping is retained with the sharper paradox; the frontier-breaker is a method rider |
| 0297 | Weak partners, strong rare-class recall | 4/3/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: gains likely vanish against tail-aware strong recipes; per-stratum anticorrelation is fragile to model choice |
| 0298 | Restart scars: do LR restarts permanently damage boundaries? | 4/3/4/3/3/3/4/4/4/4/3 | R4·U3·ROI2 | — | N | K9-SIZE: at well-tuned restart amplitudes the effect is likely marginal; Hessian attribution is heavy machinery for a schedule footnote |
| 0299 | The border penalty of resolution extrapolation | 4/4/4/4/4/4/4/4/4/5/3 | R3·U3·ROI4 | CF | N | K3-DUP (0305): resolution-geometry artifacts retained via the aliasing periodicity study; border effects mix with attention edge artifacts |
| 0300 | Objectness erosion: when continued SSL hurts promptable models | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | N | Almost-survived: a real recipe conflict at the intersection of two major practices, but conclusions hinge on masking ratio and duration, and grouping probes are unsettled instruments |
| 0301 | Do early-training error maps predict final errors? | 3/4/4/4/4/3/4/4/3/4/3 | R3·U3·ROI3 | — | N | K2-THIN: the example-level analogue is documented for classification; predictability likely breaks at boundary regions where triage matters |
| 0302 | Are class labels dead weight for prompted training? | 4/4/4/4/3/2/4/4/4/4/4 | R3·U4·ROI3 | — | N | K5-CMP: matched-volume prompted-training runs from scratch; the semantics-shape-features confound needs scale to exclude |
| 0303 | Prompts as shortcut blockers | 4/4/4/4/3/3/4/4/4/4/3 | R3·U4·ROI3 | — | N | K3-DUP (0028): near-duplicate pair, and both die on the same flaw — injected correlations create synthetic shortcuts whose realism caps the paradigm claim |
| 0304 | Style leaks through skips | 5/5/5/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | CI·DM | **Y** | Indicts the most standard dense-architecture component with probe, ablation, and swap interventions; a robustness-preserving skip redesign touches every U-Net descendant |
| 0305 | Periodic performance in input size: aliasing with the patch grid | 5/4/5/4/4/4/4/4/5/5/4 | R3·U4·ROI4 | CI·CF | **Y** | A free correction to a systematic artifact contaminating every resolution decision and cross-paper ViT comparison; 2–4 px sweeps on frozen models settle it |
| 0306 | Less rank, more accuracy: the low-rank advantage on tiny datasets | 4/4/4/4/5/4/4/4/4/5/3 | R2·U4·ROI5 | CI·CF | **Y** | Rank defaults are data-size-agnostic while the modal medical fine-tune is tiny-n; a validated rank-vs-n rule upgrades the most common regime nearly for free |
| 0307 | Hidden language priors under purely visual prompts | 4/4/4/4/3/3/4/3/4/4/4 | R4·U4·ROI3 | — | N | K4-DATA: matched visual-only control models at comparable scale don't exist publicly; without them the leakage attribution is unidentifiable |
| 0308 | Pure-noise negatives as an FP suppressor | 4/3/4/4/4/4/4/4/4/4/3 | R3·U3·ROI4 | CI | N | Almost-survived: cheap with a genuinely clarifying mechanism (absence-mode calibration), but loss-normalization artifacts are a live rival and 0017/0182 already carry the negatives thread |
| 0309 | The inertia tax: temporal smoothing vs growing fires | 4/4/4/4/3/3/2/4/4/4/3 | R3·U4·ROI3 | — | N | K4-DATA: growth-rate-annotated event onsets are scarce; without them the latency law is unmeasurable |
| 0310 | Confidence inversion: soft labels in, hard predictions out | 5/4/5/4/4/4/3/4/5/4/4 | R3·U4·ROI4 | CI | **Y** | If soft supervision backfires into sharper confidence, every multi-rater and matting pipeline mis-signals uncertainty; the loss-structure account is directly testable — anchors 0008/0025/0099/0296 |
| 0311 | Seeds as annotation auditors | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI4 | CF | N | Almost-survived: nearly free and clever, but disagreement plausibly concentrates on genuine ambiguity where "error" is undefined, and 0082 owns the label-noise instrument slot |
| 0312 | Sleeper domains: zero-shot mispredicts fine-tuning outcomes | 4/4/4/4/3/2/4/4/4/4/4 | R3·U4·ROI3 | — | N | K5-CMP: uniform fine-tuning across 20+ domains, and the uniform recipe itself confounds the adaptability ranking |
| 0313 | Random features, real boundaries: where pretraining doesn't matter | 4/4/4/4/4/3/4/4/3/4/3 | R3·U4·ROI3 | CI | N | Almost-survived: strategic cartography of where pretraining pays, but decoder-capacity matching can manufacture either answer; 0129's decomposition is the cleaner cut |
| 0314 | Prompts don't transfer across model versions | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K8-DATE: the depreciation schedule obsoletes with each release; only the framework survives |
| 0315 | Five percent of elsewhere: OOD data as a superior regularizer | 4/4/4/4/4/3/4/4/4/4/3 | R3·U4·ROI4 | CI | **Y** | A data-space regularizer dominating tuned weight decay is cheap to falsify and immediately actionable in the modal fine-tuning scenario; anchors 0080 |

---

## Cluster 10 — Genuinely Motivated Combinations (0316–0330)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0316 | Conformal stopping for coverage-guaranteed click budgets | 4/4/4/3/4/3/4/4/4/4/3 | R4·U4·ROI3 | — | N | K1-ENG: guarantee engineering; adaptive stopping breaks exchangeability and the correction may spend the click savings — the validity thread lives in 0120/0337 |
| 0317 | Prompt-consistency objectives for weight-space TTA | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | — | N | K3-DUP (0279): same consistency anchor; 0279 tests it in distillation form with collapse-rate metrics |
| 0318 | Differentiable scattering: a physics head for volumetric smoke | 5/4/4/4/3/3/3/3/5/4/4 | R4·U5·ROI3 | HRHR | **Y** | Physics-in-the-loop turns ordinary 2D masks into supervision for a 3D physical quantity; either grounds smoke quantification or shows single-view inversion is under-constrained — worth one hard attempt |
| 0319 | Refraction's motion signature as a transparency cue | 4/3/4/4/3/3/3/4/4/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: flow estimation collapses on textureless backgrounds exactly where the transparency cue is needed most |
| 0320 | Positive-unlabeled statistics for everything-mode auto-labeling | 4/5/4/5/4/3/4/4/4/4/4 | R3·U4·ROI5 | — | **Y** | Repairs the false closed-world assumption in the field's dominant auto-labeling pattern with the theory built for exactly this data; anchors 0007/0034 |
| 0321 | Shape-statistics-constrained adapters | 3/4/3/4/3/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K1-ENG: constraint machinery; the prior suppresses pathological shape variation — the cases that matter most |
| 0322 | Retrieval-of-prompts: transferring interaction knowledge | 3/3/3/3/3/3/3/4/4/4/3 | R4·U3·ROI2 | — | N | K1-ENG: interaction-infrastructure proposal; prompt success may be too image-conditioned for similarity retrieval |
| 0323 | Counterfactual shortcut audits via generative editing | 4/4/4/4/4/3/4/4/4/4/4 | R3·U4·ROI3 | — | N | K9-SIZE: edit artifacts perturb models, so the instrument's validity rests on the very fidelity controls under question |
| 0324 | Boundary Shapley values for multi-rater consensus | 4/3/3/4/3/3/2/4/4/4/3 | R4·U3·ROI2 | — | N | K1-ENG: fusion-rule proposal with combinatorial cost; multi-rater data rich enough to validate it is scarce |
| 0325 | Information-optimal clicking from the multimask posterior | 4/3/3/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K1-ENG: policy method; the 3-candidate posterior is likely too coarse to represent the ambiguities that matter |
| 0326 | Topology-first evaluation for vascular segmentation | 3/4/4/4/4/4/4/4/3/4/3 | R3·U4·ROI3 | — | N | K2-THIN: topology metrics exist (clDice, Betti errors) and ranking sensitivity is expected; the novel clinical-validation arm is a K7-HUM study |
| 0327 | Bandit-routed annotation budgets | 3/4/3/4/3/3/4/4/3/4/3 | R3·U3·ROI2 | — | N | K1-ENG: pipeline optimization; campaign non-stationarity erodes the regret guarantees that are the point |
| 0328 | The identifiability of masks from k clicks | 5/4/4/3/2/4/4/3/5/3/4 | R5·U4·ROI2 | — | N | K9-SIZE: tractable only under priors too simplified to predict real behavior; the bound risks vacuity exactly where interaction is hard |
| 0329 | Weak-to-strong generalization in dense prediction | 5/5/5/4/4/3/4/4/4/4/5 | R3·U5·ROI4 | HRHR·DM | **Y** | Determines the ceiling of the field's dominant dataset-construction strategy; the bias/variance error decomposition converts an ideology fight into a measurement |
| 0330 | Refinement as curve evolution: stability conditions for iterative decoders | 4/3/4/3/3/3/4/4/5/4/3 | R4·U3·ROI3 | — | N | K9-SIZE: learned updates may be too far from any local evolution law for the stability theory to bind |

---

## Cluster 11 — SR / Restoration / Generation / Diffusion / LLM Agents (0331–0340)

| ID | One-line | N/S/Q/T/F/C/D/B/P/E/V | R·U·ROI | Flag | Y/N | Reason |
|---|---|---|---|---|---|---|
| 0331 | The hallucination-utility frontier of SR for dense prediction | 4/5/4/4/4/3/4/4/4/4/4 | R3·U4·ROI4 | DM | **Y** | Frontier plus a deployable no-GT audit (seed-ensemble variance) before generative preprocessing embeds silently in measurement-critical pipelines; subsumes 0295 |
| 0332 | Diffusion features vs discriminative features for amorphous stuff | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K9-SIZE: timestep/layer extraction freedoms must be searched per family, letting either side of the dissociation win by tuning |
| 0333 | Does restoration reintroduce a domain gap? | 4/4/4/4/4/3/4/4/4/4/3 | R3·U3·ROI3 | — | N | K3-DUP (0331, 0338): the restoration-preprocessing family is represented by its two sharpest claims; the third-distribution mechanism folds into 0331 as a covariate |
| 0334 | Is cycle-consistency a valid generation metric? | 4/4/4/4/3/3/4/4/4/4/4 | R3·U4·ROI3 | — | N | K7-HUM: the load-bearing instrument is a human-fidelity protocol that is itself noisy and costly; the collusion claim cannot stand without it |
| 0335 | Denoising as uncertainty grounding | 4/4/4/4/3/2/4/4/4/4/3 | R3·U4·ROI3 | — | N | K5-CMP: modality-realistic denoising pretraining per feature family; the inheritance may not survive fine-tuning |
| 0336 | LLM agents as guideline compilers for annotation QA | 4/4/3/3/4/3/4/3/4/4/3 | R4·U3·ROI3 | — | N | K8-DATE: a capability snapshot of current VLM agents; precision caps move every release, only the protocol survives |
| 0337 | Are diffusion mask priors valid posteriors? | 5/5/5/4/3/3/3/4/5/4/4 | R3·U4·ROI4 | CF·DM | **Y** | Generative uncertainty is consumed as calibrated in medical prototypes; coverage tests against held-out rater distributions settle its statistical status — anchors 0092/0099 |
| 0338 | Noise as signal: does restoration destroy forensic cues at the resolution limit? | 5/4/5/4/4/3/3/4/5/4/4 | R4·U4·ROI4 | CI | **Y** | If restoration deletes the earliest detectable signal, uniform preprocessing harms exactly the systems built for early detection; matched-training controls make it decisive — anchors 0243 |
| 0339 | Interactive segmentation as Bayesian inversion | 4/4/4/3/3/2/4/4/4/3/4 | R4·U4·ROI2 | — | N | K1-ENG: system rebuild; posterior maintenance may miss interactive latency budgets without approximations that forfeit its advantages |
| 0340 | Agentic pipelines vs monolithic fine-tunes | 4/4/4/3/2/2/3/3/4/3/4 | R4·U4·ROI2 | — | N | K5-CMP: both paradigms × heterogeneity battery × multiple agent frameworks; framework quality dominates paradigm effects |

---

## Tally

| Cluster | Range | Survivors |
|---|---|---|
| 1 Dataset failure / annotation / long-tail | 0001–0040 | 8 (0001, 0006, 0009, 0012, 0017, 0019, 0024, 0037) |
| 2 Domain shift / transfer | 0041–0080 | 8 (0053, 0054, 0055, 0057, 0064, 0072, 0075, 0078) |
| 3 Evaluation / calibration / uncertainty | 0081–0120 | 9 (0082, 0083, 0084, 0089, 0104, 0108, 0110, 0114, 0120) |
| 4 Representation mismatch | 0121–0155 | 7 (0122, 0124, 0126, 0128, 0129, 0132, 0136) |
| 5 Multimodal supervision | 0156–0185 | 7 (0156, 0159, 0162, 0174, 0182, 0184, 0185) |
| 6 Synthetic data pitfalls | 0186–0215 | 6 (0186, 0189, 0190, 0191, 0193, 0200) |
| 7 Detection limitations | 0216–0245 | 6 (0217, 0219, 0223, 0226, 0233, 0241) |
| 8 Parameter efficiency vs quality | 0246–0280 | 9 (0248, 0251, 0253, 0257, 0260, 0269, 0270, 0272, 0279) |
| 9 Surprising phenomena | 0281–0315 | 9 (0282, 0285, 0288, 0294, 0304, 0305, 0306, 0310, 0315) |
| 10 Motivated combinations | 0316–0330 | 3 (0318, 0320, 0329) |
| 11 SR / restoration / generation / agents | 0331–0340 | 3 (0331, 0337, 0338) |
| **Total** | 0001–0340 | **75 survive · 265 eliminated** |
