# Stage 2 — Batch C Scores (Independent Scientific Review)

Reviewer: independent Stage-2 reviewer for Windows5 research-idea evolution.
Source: `stage1_batch_C_ideas.md` (IDEA-C-0001 … IDEA-C-0340, verified 340 ideas, no gaps).
Mandate: keep ~70 for further study. **Final keep count: 74.**

## Scoring legend

Each idea scored 1–5 on 13 dimensions, reported as a compact string in fixed order:

`N/S/Q/T/F/Cp/Da/Ba/NP/EC/VP/PU/ROI`

| Code | Dimension |
|---|---|
| N | Novelty |
| S | Significance |
| Q | Scientific Question quality |
| T | Technical Soundness |
| F | Feasibility |
| Cp | Compute friendliness (5 = cheap) |
| Da | Dataset Availability |
| Ba | Baseline Availability |
| NP | Likelihood Already Published (5 = unlikely already published) |
| EC | Experimental Clarity |
| VP | Venue Potential |
| PU | Potential Upside |
| ROI | Research ROI |

`Avg` = mean of the 13 scores (2 decimals). **Selection was NOT by average alone**: protected categories override ranking.

Risk (recorded separately): L / M / H.
Prot (protect flag): `HR` = protected high-risk/high-reward; `CI` = protected simple counter-intuitive; `CF` = protected cheap-to-falsify; `-` = none (kept on merit or not kept).

Elimination policy applied: ideas that reduce to module combinations, "apply X to medical images," or loss/backbone swaps without a load-bearing scientific question were not kept; near-instances are flagged in the Reason column. Redundant ideas were consolidated (best-framed variant kept, others marked `dup/merge`).

---

## C1. PEFT failure & when full fine-tuning is necessary (0001–0030) — kept 5/30

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0001 | FT-update spectrum predicts PEFT failure | 4/4/5/4/4/3/4/4/4/4/4/4/4 | 4.00 | M | - | Y | Pre-hoc decision rule; strong falsifiable law |
| C-0002 | PEFT fails on low-level statistical shift | 4/4/4/4/4/3/4/4/3/4/3/3/4 | 3.69 | M | - | N | Overlaps 0020; stem hypothesis is the sharper version |
| C-0003 | Attention-vs-MLP placement taxonomy | 3/3/4/3/4/3/4/4/3/4/3/3/3 | 3.38 | M | - | N | Placement ablation; taxonomy may not transfer across scales |
| C-0004 | Linear probe interpolates PEFT outcome | 3/4/4/3/5/4/4/4/3/4/3/3/4 | 3.69 | M | - | N | Useful forecaster but α likely unstable with rank/data |
| C-0005 | Granularity shift breaks PEFT | 4/4/4/4/4/3/3/4/4/4/3/3/3 | 3.62 | M | - | N | Confounded with per-class sample size; hard to isolate |
| C-0006 | BitFit as task-typing diagnostic | 3/3/4/3/5/4/4/5/3/4/3/3/4 | 3.69 | M | - | N | Dichotomy likely a continuum; diagnostic value modest |
| C-0007 | PEFT underfits long-tail classes | 4/4/4/4/4/3/4/4/4/4/4/4/4 | 3.92 | M | - | N | Strong, but 0016 covers the clinical stratified-deficit angle |
| C-0008 | Norm-only gain fraction classifies shift | 3/4/4/4/4/4/4/4/3/4/3/3/4 | 3.69 | M | - | N | Real shifts mix components; classification boundary blurs |
| C-0009 | Early-gradient rank predicts LoRA rank | 3/3/4/3/4/4/4/4/3/4/3/3/4 | 3.54 | M | - | N | Head-warmup contamination; modest upside |
| C-0010 | PEFT calibration penalty vs FT | 4/4/4/4/4/4/4/4/4/4/4/3/4 | 3.92 | M | - | N | Near-miss; merge with 0108 theme (calibration of adapters) |
| C-0011 | PEFT failure: capacity vs optimization | 4/4/5/4/4/2/4/4/4/5/4/4/4 | 4.00 | M | - | Y | Clean mechanism adjudication nobody runs |
| C-0012 | Subspace overlap predicts LoRA-merge loss | 3/4/4/4/4/3/4/4/3/4/3/3/3 | 3.54 | M | - | N | Merging heuristics area crowded; layer heterogeneity risk |
| C-0013 | Dense needs early-layer LoRA, cls late | 3/4/4/3/4/3/4/4/3/4/3/3/3 | 3.46 | M | - | N | Decoder capacity masks encoder-layer effect |
| C-0014 | Gradient anti-alignment freeze/unfreeze test | 4/3/4/3/4/4/4/4/4/3/3/3/3 | 3.54 | H | - | N | Single-snapshot gradients too noisy for an instrument |
| C-0015 | Robustness–plasticity exchange rate | 4/4/4/3/3/3/4/4/3/3/3/3/3 | 3.38 | H | - | N | Exchange rate unlikely stable across shift types |
| C-0016 | PEFT small-lesion sensitivity gap | 4/5/4/4/4/3/4/4/4/4/4/4/4 | 4.00 | M | - | Y | Highest-stakes clinical regime; frequency mechanism + stem fix |
| C-0017 | Prompt vs weight PEFT double dissociation | 3/3/4/3/3/3/4/4/3/3/3/3/3 | 3.23 | H | - | N | Dissociating task families may not exist in practice |
| C-0018 | Frozen-BN confound in CNN PEFT | 3/4/4/4/5/4/4/4/3/4/3/3/4 | 3.77 | L | - | N | Close to known BN/TTA results; audit value only |
| C-0019 | PEFT cannot shift resolution prior | 3/4/4/4/4/3/4/4/3/4/3/3/3 | 3.54 | M | - | N | ERF estimation noisy; overlaps 0270 territory |
| C-0020 | Trainable stem + LoRA = full FT cross-modality | 4/4/4/4/4/3/4/4/3/4/4/4/4 | 3.85 | M | - | Y | Folklore→law; near-free recipe, ceiling-effect design |
| C-0021 | LoRA sits in sharper minima | 3/3/4/3/4/3/4/4/3/3/3/3/3 | 3.31 | H | - | N | Sharpness metrics reparameterization-fragile |
| C-0022 | Scaling law for PEFT/FT crossover N* | 4/4/4/4/3/2/4/4/4/4/4/3/3 | 3.62 | M | - | N | Expensive grid; N* ill-conditioned when curves shallow |
| C-0023 | PEFT can add but cannot unlearn | 5/4/5/4/4/3/3/4/4/4/4/5/4 | 4.08 | H | HR | Y | Protected: defines a principled must-full-FT class |
| C-0024 | Iterated LoRA-merge drift law | 3/3/4/3/4/3/4/4/4/3/3/3/3 | 3.38 | M | - | N | Divergence may be benign; weaker endpoint |
| C-0025 | PEFT worse on dense regression outputs | 3/3/4/3/4/3/4/4/4/3/3/3/3 | 3.38 | M | - | N | Difficulty matching across output types shaky |
| C-0026 | Adapters starve patch-token pathways | 4/3/4/3/3/3/4/3/4/3/3/3/3 | 3.31 | H | - | N | Path attribution in ViTs too fragile to carry the claim |
| C-0027 | Fisher layer selection beats low-rank | 4/4/4/4/4/3/4/4/3/4/4/4/4 | 3.85 | M | - | N | Good; trimmed — rank-vs-structure question served by 0011 |
| C-0028 | PEFT cannot install new invariances | 4/4/4/4/3/3/3/4/4/3/3/3/3 | 3.46 | M | - | N | Invariance can hide in heads; probing burden high |
| C-0029 | Benchmark built from failure predictors | 3/4/3/4/3/2/3/4/4/3/4/3/3 | 3.31 | M | - | N | Meta-benchmark; depends on other predictors maturing first |
| C-0030 | Adapted models lose future adaptability | 4/3/4/3/4/3/4/4/4/3/3/3/3 | 3.46 | M | - | N | Small effects vs chain variance; needs many chains |

## C2. Catastrophic forgetting in sequential adaptation (0031–0060) — kept 5/30

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0031 | Small structures forgotten first | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Good; edged out by 0034/0040 which explain mechanism |
| C-0032 | Scanner forgetting = norm-statistics drift | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Norm-swap known in DA; recovery-fraction framing not enough |
| C-0033 | Boundary-hard exemplars for replay | 3/3/4/3/4/4/4/4/3/4/3/3/3 | 3.46 | M | - | N | Exemplar selection crowded; label-noise confound |
| C-0034 | Forgetting: feature loss vs readout loss | 4/5/5/4/4/4/4/4/3/5/4/4/5 | 4.23 | L | - | Y | Load-bearing decomposition for all CL remedies |
| C-0035 | Domain- vs class-incremental dissociation | 3/4/4/3/3/3/4/4/3/3/3/3/3 | 3.31 | M | - | N | "Matched severity" ill-defined; design fragile |
| C-0036 | Gradient conflict forecasts forgetting | 3/4/4/3/4/4/4/4/3/4/3/3/4 | 3.62 | M | - | N | Conflict evolves during training; forecast unstable |
| C-0037 | Two-phase forgetting dynamics | 3/3/4/3/4/3/4/4/4/3/3/3/3 | 3.38 | M | - | N | Optimizer-dependent; descriptive endpoint |
| C-0038 | EWC fails via Fisher estimation noise | 4/4/5/4/4/3/4/4/4/4/3/4/4 | 3.92 | M | - | N | Near-miss; estimator-vs-principle split is publishable |
| C-0039 | Generative replay harms rare classes | 4/5/4/4/3/3/4/4/4/4/4/4/4 | 3.92 | M | - | N | Near-miss; strong safety claim, generator-specificity risk |
| C-0040 | Forgetting = retrieval failure, not erasure | 5/4/5/4/4/4/4/4/4/4/4/5/5 | 4.31 | M | HR | Y | Protected: cheap reminders could replace CL machinery |
| C-0041 | Shift-magnitude curriculum ordering | 3/3/4/3/3/3/4/4/3/3/3/3/3 | 3.23 | M | - | N | Ordering effects likely inside seed noise |
| C-0042 | Calibration forgetting as early warning | 4/4/4/3/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | ECE estimation noise likely swamps lead signal |
| C-0043 | Real temporal drift vs artificial splits | 4/4/4/4/3/3/2/4/4/3/4/4/3 | 3.54 | H | - | N | Date-annotated public data scarce; dataset-batch merge flag |
| C-0044 | Modality forgetting concentrates early layers | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Near-miss; inversion claim good, CKA proxy risk |
| C-0045 | Router failure in adapter banks | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Router-design dependent; solid but narrower |
| C-0046 | SSL rehearsal on unlabeled old data | 3/4/4/4/4/4/4/4/3/4/3/3/4 | 3.69 | M | - | N | Diagnostic value contingent on 0034's outcome |
| C-0047 | Frequency-forgetting law | 3/4/4/4/4/3/4/4/3/4/3/3/3 | 3.54 | M | - | N | Frequency/size/difficulty confound heavy |
| C-0048 | BN vs GN forgetting trade-off | 3/3/4/3/4/3/4/4/4/3/3/3/3 | 3.38 | M | - | N | Initial-accuracy matching biases plasticity |
| C-0049 | Stability gap as patient-exposure integral | 4/4/4/4/4/3/4/4/3/4/3/3/4 | 3.69 | M | - | N | Good reframing; known phenomenon, eval-heavy |
| C-0050 | Checkpoint averaging beats CL methods | 4/5/4/4/5/4/4/4/3/5/4/4/5 | 4.23 | L | CI | Y | Protected counter-intuitive baseline; zero-overhead |
| C-0051 | Isolation CL forfeits backward transfer | 4/3/4/4/4/3/4/4/4/4/3/3/3 | 3.62 | M | - | N | Positive backward transfer may be too rare to price |
| C-0052 | CKA drift does not predict forgetting | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close call; proxy-validation useful, narrower audience |
| C-0053 | Interference lives in low-dim subspace | 4/4/4/4/4/3/4/4/3/4/3/3/4 | 3.69 | M | - | N | Gradient-projection CL exists; k-knee claim incremental |
| C-0054 | Coverage predicts data-free distillation | 3/4/4/4/4/3/4/4/3/4/3/3/3 | 3.54 | M | - | N | Coverage metrics may miss decision-relevant coverage |
| C-0055 | Per-layer λ beats method choice | 3/4/4/3/4/3/4/4/3/4/3/3/3 | 3.46 | M | - | N | Hyperparameter-allocation study; fairness disputes |
| C-0056 | Continuous TTA drift is a slow poison | 5/5/5/4/4/3/4/4/4/4/4/5/4 | 4.23 | M | CI | Y | Deployment-safety law; timely as TTA spreads |
| C-0057 | Forgetting partly label-protocol artifact | 5/4/5/4/3/4/3/4/5/4/4/4/4 | 4.08 | M | - | Y | Measurement repair of the field's headline number |
| C-0058 | Pathology features forgotten before anatomy | 4/4/4/3/3/3/3/4/4/3/3/3/3 | 3.38 | M | - | N | Needs joint labels; probe-headroom normalization tricky |
| C-0059 | Public proxies as privacy-safe replay | 3/4/4/3/4/4/4/4/3/4/3/3/3 | 3.54 | M | - | N | Practical trick; contamination risk; modest science |
| C-0060 | When backward transfer is positive | 4/3/4/3/4/3/4/4/4/3/3/3/3 | 3.46 | M | - | N | Constructed shifts may not represent real pairs |

## C3. VLMs for dense prediction (0061–0090) — kept 5/30

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0061 | Global leakage in CLIP patch tokens | 5/4/5/4/4/4/4/4/4/4/4/4/4 | 4.15 | M | - | Y | Mechanistic account of dense-CLIP failure + layer instrument |
| C-0062 | Alignment training destroys localization over checkpoints | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Near-miss; public checkpoint grids sparse near the knee |
| C-0063 | Relational language grounding at chance | 4/4/4/4/4/4/3/4/3/4/3/3/4 | 3.69 | M | - | N | Bag-of-words known for retrieval; dense extension moderate |
| C-0064 | Things-vs-stuff gap from caption statistics | 4/4/4/3/3/3/4/4/3/3/3/3/3 | 3.38 | M | - | N | Confound matching (frequency, boundary) fragile |
| C-0065 | Layer-selection law for dense readout | 3/4/4/3/4/3/4/4/3/4/3/3/4 | 3.54 | M | - | N | Useful engineering; interactions blur layer optima |
| C-0066 | Mask artifact tokens for dense repair | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Merged into 0263's framing; neither kept (register literature fast-moving) |
| C-0067 | Prompt sensitivity = leaderboard noise | 4/5/4/4/5/4/4/4/4/5/4/4/5 | 4.31 | L | - | Y | Inference-only statistical repair of open-vocab rankings |
| C-0068 | Dense-gain vs global-loss frontier | 3/4/4/3/3/2/4/4/3/3/3/3/3 | 3.23 | M | - | N | Strict data/compute matching across methods laborious |
| C-0069 | Caption statistics, not architecture, cause grounding | 5/4/5/4/3/2/4/3/4/4/4/4/3 | 3.77 | H | - | N | Strong causal design but synthetic-scale extrapolation risk |
| C-0070 | Renamed-ontology contamination test | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close call; partly served by 0067+0081 audits |
| C-0071 | VLM dense outputs not shift-equivariant | 3/4/4/4/4/4/4/4/3/4/3/3/4 | 3.69 | M | - | N | Superseded by 0261 grid-phase analysis (kept) |
| C-0072 | Text-only referring-segmentation baseline | 4/5/4/4/5/4/4/4/3/4/4/4/5 | 4.15 | M | HR | Y | Protected: audits the subfield's central grounding claim |
| C-0073 | Phrase-to-region binding is the missing level | 4/4/4/4/4/4/3/4/4/4/3/3/4 | 3.77 | M | - | N | Close call; probe-matrix design leak-prone |
| C-0074 | Scale-conditional pseudo-mask bias law | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | SAM-batch merge flag (prompt-derived mask bias theme) |
| C-0075 | Fusion resolution, not depth, binds localization | 3/4/4/3/3/2/4/4/3/3/3/3/3 | 3.23 | M | - | N | Compute-fair continuum training expensive |
| C-0076 | Negation blindness breaks medical grounding | 4/5/4/4/4/4/3/4/3/4/4/4/4 | 3.92 | M | - | Y | Clinically pressing; report-statistics linkage testable |
| C-0077 | Texture-over-shape bias in patch-text similarity | 3/4/4/4/4/4/4/4/3/4/3/3/4 | 3.69 | M | - | N | Cue-conflict transplant; natural-image linkage uncertain |
| C-0078 | Decoders succeed by undoing alignment | 5/4/5/4/4/4/4/4/4/4/4/5/4 | 4.23 | H | HR | Y | Protected: pipeline-self-contradiction finding if true |
| C-0079 | Contrastive temperature controls localization | 4/4/4/4/3/2/4/4/4/4/3/4/3 | 3.62 | M | - | N | Small-scale training may not reproduce dynamics |
| C-0080 | Caption co-occurrence predicts boundary confusion | 4/4/5/4/3/3/4/4/4/4/4/4/3 | 3.85 | M | - | N | Strong; interventional pretraining arm costly — trimmed |
| C-0081 | Open-vocab success carried by frequent classes | 4/4/4/4/4/4/4/4/3/4/4/4/4 | 3.92 | M | - | N | Close call; overlaps 0067/0070 audit family |
| C-0082 | Ordinal/counting expression benchmark | 4/4/4/4/4/4/3/4/4/4/4/4/4 | 3.92 | M | - | N | Benchmark construction heavy; strong but deferred |
| C-0083 | Radial error field from PE interpolation | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Duplicate of 0262 (C10 runner-up, better framing) |
| C-0084 | SSL-vs-VLM error complementarity oracle | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Oracle bound only; investment-guidance value modest |
| C-0085 | Alignment destroys instance discrimination | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Close; nonlinear-probe caveat weakens ceiling claim |
| C-0086 | Caption region-binding density law | 4/4/5/4/3/2/3/3/4/4/4/4/3 | 3.62 | H | - | N | Annotator circularity + controlled pretraining cost |
| C-0087 | Qualifier blindness in medical VLMs | 4/4/4/3/3/4/2/4/4/3/3/3/3 | 3.38 | M | - | N | Per-instance size labels scarce |
| C-0088 | Tokenizer fragmentation breaks medical terms | 4/4/4/4/4/4/3/4/4/4/3/3/4 | 3.77 | M | - | N | Close call; rarity/fragmentation disentangling hard |
| C-0089 | Latent localization: probe-vs-readout headroom | 4/4/5/4/4/4/4/4/3/4/3/4/4 | 3.92 | M | - | N | Near-miss; information-vs-readout audit well framed |
| C-0090 | Prompts act as priors, not evidence | 4/4/5/4/4/4/4/4/4/4/3/4/4 | 4.00 | M | - | N | Close call; strong decomposition, trimmed on budget |

## C4. Prompt learning pathologies (0091–0118) — kept 5/28

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0091 | Learned prompts are dataset fingerprints | 5/4/4/4/4/4/3/4/4/4/4/4/4 | 4.00 | M | HR | Y | Protected: prompt reuse becomes a safety issue |
| C-0092 | Prompts converge to class-prior fitting | 4/4/4/4/5/4/4/4/3/4/3/4/4 | 3.92 | L | - | N | Close call; deflation largely covered by 0095+0316 |
| C-0093 | Nearest-word prompt interpretation is invalid | 4/3/4/4/5/5/4/4/3/4/3/3/4 | 3.85 | L | - | N | Near-miss; hygiene result, modest venue ceiling |
| C-0094 | Seed-variance meta-analysis of prompt learning | 4/5/4/5/4/3/4/4/4/5/4/4/5 | 4.23 | L | - | Y | Field-level reliability estimate; decisive |
| C-0095 | Base-new trade-off = regularization artifact | 4/5/5/4/4/3/4/4/4/5/4/4/5 | 4.23 | M | - | Y | One-knob frontier test deflates a method branch |
| C-0096 | Prompt-length capacity knee | 3/3/4/3/4/4/4/4/3/3/3/3/3 | 3.38 | M | - | N | Knee-location theory soft ("attribute complexity") |
| C-0097 | Prompts regress to caption manifold | 4/3/4/3/3/3/4/4/4/3/3/3/3 | 3.38 | H | - | N | Embedding density estimation delicate |
| C-0098 | Visual prompts = normalization perturbation | 4/4/5/4/4/4/4/4/4/4/3/4/4 | 4.00 | M | - | N | Close call; strong mechanism split, trimmed on budget |
| C-0099 | Prompts capture acquisition-context shortcuts | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Shortcut literature adjacent; counterfactual edits hard |
| C-0100 | Prompt-set interference law | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Softmax-competition confound; deployment niche |
| C-0101 | TPT ≡ entropy min + temperature | 4/4/5/4/4/4/4/4/4/4/3/4/4 | 4.00 | M | - | Y | Mechanism-vs-artifact with harmful-residual analysis |
| C-0102 | Prompt ensembling = variance reduction | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Close; matched-variance null is nice but small scope |
| C-0103 | Learned prompts are adversarial-like | 4/3/4/3/4/4/4/4/4/4/3/3/4 | 3.69 | M | - | N | Norm-matching disputes; fragility angle secondary |
| C-0104 | Data lineage predicts prompt transfer | 3/3/4/3/3/3/3/4/4/3/3/3/3 | 3.23 | M | - | N | Lineage opaque for most models |
| C-0105 | Conditional prompts barely condition | 4/3/4/4/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Audit of a narrower method family |
| C-0106 | Global prompts cannot encode spatial priors | 3/4/4/3/4/4/4/4/3/4/3/3/3 | 3.54 | M | - | N | Borderline module design; SAM-batch adjacency flag |
| C-0107 | Task arithmetic in prompt space | 3/3/4/3/4/4/4/4/4/3/3/3/3 | 3.46 | M | - | N | Nonlinearity likely breaks additivity everywhere |
| C-0108 | Calibration: prompt tuning vs LoRA | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Merged theme with 0010; neither kept individually |
| C-0109 | Hard prompts match soft at equal compute | 4/4/4/4/3/3/4/4/4/4/3/4/4 | 3.77 | M | - | N | Close; regulated-setting value, search-tooling burden |
| C-0110 | Few-shot validation leakage audit | 4/4/4/4/4/3/4/4/3/4/3/4/4 | 3.77 | M | - | N | Dataset-batch merge flag (protocol-leakage theme) |
| C-0111 | Prompts memorize class-name tokens | 4/4/4/4/5/4/4/4/3/4/3/3/4 | 3.85 | L | - | N | Close; synonym stress test simple, scope narrow |
| C-0112 | Initialization dominates prompt method identity | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; variance attribution nice, overlaps 0094 program |
| C-0113 | Prompt collapse destroys fine-grained classes | 5/4/4/4/4/4/4/4/4/4/3/4/4 | 4.00 | M | CI | Y | Protected: monitorable training pathology + early warning |
| C-0114 | Prompt elaboration doesn't move visual grounding | 4/4/4/3/4/4/3/4/4/4/3/3/4 | 3.69 | M | - | N | Attribution-noise risk; bounds a hope, narrower claim |
| C-0115 | Negation blindness minimal-fix cost curve | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Merged into 0076 (kept); fix-cost arm noted there |
| C-0116 | Prompt tuning amplifies label noise | 3/4/4/4/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Plausible mechanism; incremental comparison study |
| C-0117 | Prompt-pool forgetting lives in the router | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close; oracle-routing decomposition neat, niche |
| C-0118 | Concept tokens encode site, not pathology | 4/4/4/4/3/4/2/4/4/4/3/3/3 | 3.54 | M | - | N | Multi-site concept-labeled data scarce |

## C5. Weak/semi/self-supervised segmentation (0119–0148) — kept 6/30

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0119 | Pseudo-label errors diffuse from boundaries | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close; dynamics model nice, loss-dependence risk |
| C-0120 | Labeled-subset selection dominates SSL method | 4/5/4/4/4/3/4/4/3/4/4/4/4 | 3.92 | M | - | N | Near-miss; selection-vs-method variance attribution strong |
| C-0121 | Consistency training = boundary smoothing | 5/4/5/4/4/4/4/4/4/4/4/4/4 | 4.15 | M | - | Y | Missing control experiment for a whole method family |
| C-0122 | Scribble geometry law | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close; annotation-protocol value, moderate upside |
| C-0123 | CAM-hard class taxonomy | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; class-typing subjectivity risk |
| C-0124 | Self-training collapses rater ambiguity | 5/4/5/4/4/4/3/4/4/4/4/4/4 | 4.08 | M | HR | Y | Protected: bridges SSL practice and multi-rater agenda |
| C-0125 | SSL gains: representation vs optimization | 4/4/5/4/3/2/4/4/3/4/4/4/3 | 3.69 | M | - | N | Long-schedule compute heavy; attribution hard to close |
| C-0126 | OOD contamination breaks semi-supervised | 4/4/4/4/4/3/4/4/3/4/3/4/4 | 3.77 | M | - | N | Close call; operating-envelope value, threshold arbitrariness |
| C-0127 | Subsampled "low-data" ≠ real small cohorts | 5/5/4/4/4/3/3/4/4/4/4/4/4 | 4.00 | M | - | Y | Validity audit for all low-data claims; dataset-flag |
| C-0128 | Report labels carry correlated noise | 4/4/4/4/3/3/3/4/4/3/4/4/3 | 3.62 | M | - | N | Expert re-read cost; strong but heavy |
| C-0129 | Anatomical plausibility of mixing augmentation | 3/3/4/3/4/4/4/4/3/4/3/3/3 | 3.46 | M | - | N | In-domain/OOD split useful; modest stakes |
| C-0130 | Early-warning for entropy collapse | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close; alarm generalization across datasets uncertain |
| C-0131 | EMA-rate scaling rule | 3/3/4/3/4/3/4/4/3/4/3/3/3 | 3.38 | M | - | N | Hyperparameter study without deeper question |
| C-0132 | Positional shortcut in registered medical SSL | 5/4/5/4/4/3/4/4/4/4/4/4/4 | 4.08 | M | - | Y | Silent shortcut in the standard recipe; dose-response design |
| C-0133 | Baseline inflation in semi-supervised claims | 4/5/4/4/4/2/4/4/3/4/4/4/4 | 3.85 | M | - | N | Compute-heavy replication; served by 0340 (kept) |
| C-0134 | Fixed thresholds mechanically lock out minorities | 4/4/4/4/4/4/4/4/3/5/3/3/4 | 3.85 | L | - | N | Adaptive-threshold literature close; oracle framing nice |
| C-0135 | Information ceiling of image-level supervision | 4/4/5/3/3/3/4/4/4/3/4/4/3 | 3.69 | H | - | N | Ceiling estimation itself model-limited |
| C-0136 | View correlation caps co-training gains | 4/3/4/4/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Error-correlation/outcome entanglement |
| C-0137 | Barely-supervised success = implicit registration | 5/4/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | - | Y | Sharp deflation; alignment-stratified design clean |
| C-0138 | Scanner fingerprints in SSL features causal | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; supervised-model analogues published |
| C-0139 | Click simulators diverge from real clinicians | 4/4/4/4/3/4/2/4/4/4/4/4/3 | 3.69 | M | - | N | SAM-batch merge flag (interactive-seg evaluation theme) |
| C-0140 | Superpixel bias inheritance | 4/3/4/4/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Signature-transfer test nice; niche pipeline |
| C-0141 | Distance heuristic vs uncertainty machinery | 4/4/4/4/5/4/4/4/3/5/3/4/4 | 4.00 | L | - | N | Close call; strong deflationary control, trimmed |
| C-0142 | Propagation beats consistency on temporal data | 3/4/4/4/4/4/4/4/3/4/3/3/4 | 3.69 | M | - | N | Method comparison flavor; structure-exploitation obvious |
| C-0143 | Label-efficiency: slope vs intercept | 5/5/5/4/4/3/4/4/4/4/4/4/4 | 4.15 | M | - | Y | Converts "N× savings" marketing into a scaling claim |
| C-0144 | Dense-vs-global SSL gradient conflict | 3/3/4/3/4/3/4/4/4/3/3/3/3 | 3.38 | M | - | N | Gradient cosine coarse; recipe-tuning flavor |
| C-0145 | Active learning under real annotation costs | 4/4/4/4/3/4/3/4/4/4/3/4/4 | 3.77 | M | - | N | Close; timed-study requirement, strong if run |
| C-0146 | Partial-label missingness dose-response law | 4/4/4/4/4/3/4/4/3/4/3/4/4 | 3.77 | M | - | N | Close; PU corrections partially published |
| C-0147 | SSL features lack anatomical invariants | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; probe battery valuable, elicitation risk |
| C-0148 | Why EMA teachers beat students | 4/4/5/4/4/3/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; 2×2 adjudication clean, mechanism may mix |

## C6. Medical vision foundation models: limits (0149–0178) — kept 7/30

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0149 | Laterality flip-consistency safety probe | 4/5/4/4/5/5/4/4/4/4/4/4/5 | 4.31 | L | - | Y | Never-event capability audit; cheap and decisive |
| C-0150 | FMs cannot compare two scans | 4/5/4/4/4/4/3/4/4/4/4/4/4 | 4.00 | M | - | Y | Interval change = the modal clinical act; ladder design |
| C-0151 | FMs lost metric scale (pixel spacing) | 4/5/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | - | Y | Crisp information-destruction claim + injection test |
| C-0152 | Prevalence-performance power law | 4/4/4/3/3/3/3/4/4/3/4/4/3 | 3.54 | H | - | N | Prevalence estimation in opaque corpora rough |
| C-0153 | Slice-shuffle partitions benchmarks 2D/3D | 4/4/4/4/5/5/4/4/3/4/3/4/4 | 4.00 | L | - | N | Merged into 0326 (kept); run as one paper |
| C-0154 | Cross-modality patient identity fails | 4/4/4/4/3/4/3/4/4/4/3/3/3 | 3.62 | M | - | N | Paired data scarce; matching-gap claim narrower |
| C-0155 | Counting deficit beyond ~4 | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; VLM counting failures known in general domain |
| C-0156 | Demographic shortcut causal chain | 4/5/4/4/4/4/4/4/2/4/4/4/4 | 3.92 | M | - | N | Near-miss; race-decoding published, causal arm incremental |
| C-0157 | Overconfidence on unseen pathology | 4/4/4/4/3/4/3/4/3/4/3/4/3 | 3.62 | M | - | N | "Never-seen" unverifiable for opaque corpora |
| C-0158 | Device-pathology confusion imprint | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; label-correlation control is the hard part |
| C-0159 | Acquisition-era decay (FM shelf-life) | 4/4/4/3/3/4/2/4/4/3/3/3/3 | 3.38 | M | - | N | Era-annotated data scarce; institution confound |
| C-0160 | FMs cannot abstain where it matters | 4/5/4/4/4/4/4/4/3/4/3/4/4 | 3.92 | M | - | N | Close; selective-prediction literature adjacent |
| C-0161 | Topology-violation audit FM vs specialist | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Close; useful metric, modest novelty |
| C-0162 | FMs learn reported findings, miss incidentals | 5/5/5/4/3/4/3/4/4/4/4/5/4 | 4.15 | H | HR | Y | Protected: supervision-policy blindness; needs re-reads |
| C-0163 | Compositional multi-disease failure | 4/4/4/3/3/4/3/4/4/3/3/4/3 | 3.54 | M | - | N | Severity confounds heavy; interaction estimation hard |
| C-0164 | Effective-resolution ceiling of FM features | 4/4/5/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | - | Y | Physics-style capability bound; pairs with 0264/0206 |
| C-0165 | Few-shot claims under strict patient/site splits | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Near-miss; dataset-batch merge flag (leakage theme) |
| C-0166 | Physics-artifact stress vs augmented baselines | 4/4/4/4/3/3/3/4/3/4/3/3/3 | 3.46 | M | - | N | Artifact simulation validation burden |
| C-0167 | Embedding space is modality-first | 4/4/4/4/4/4/4/4/3/4/3/3/4 | 3.77 | M | - | N | Close; variance decomposition simple, expected result |
| C-0168 | Slice-wise inconsistency corrupts volumetry | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; consistency-vs-accuracy split useful, folded into 0177 story |
| C-0169 | Occlusion-verified hallucination attribution | 4/5/4/4/4/4/3/4/3/4/4/4/4 | 3.92 | M | - | N | Close; hallucination literature moving fast |
| C-0170 | FM pretraining contaminates benchmarks | 4/4/4/4/3/4/3/4/3/4/3/4/3 | 3.62 | M | - | N | Merged with 0328 (kept); dataset-batch flag |
| C-0171 | Adult FMs on pediatric imaging interfere | 4/4/4/4/3/3/2/4/4/4/3/4/3 | 3.54 | M | - | N | Public pediatric data limited |
| C-0172 | Contrast-phase sensitivity map | 4/4/4/4/4/4/3/4/4/4/3/3/4 | 3.77 | M | - | N | Close; phase metadata unreliable |
| C-0173 | Salience suppression of second lesions | 5/5/5/4/3/4/3/4/4/4/4/5/4 | 4.15 | H | HR | Y | Protected: representational multi-lesion failure |
| C-0174 | Multimodal fine-tunes reduce to additive bias | 4/4/5/4/4/4/3/4/4/4/3/4/4 | 3.92 | M | - | N | Close; functional-ANOVA audit strong, trimmed |
| C-0175 | Static-image bias on surgical video | 4/4/4/4/3/3/3/4/4/3/3/3/3 | 3.46 | M | - | N | Appearance-controlled task construction delicate |
| C-0176 | Site fine-tunes diverge, break interoperability | 4/4/4/4/4/3/4/4/4/4/3/3/4 | 3.77 | M | - | N | Simulated-site realism; anchor-reg fix is method-y |
| C-0177 | Dice parity hides clinical-measure failure | 5/5/5/4/4/4/4/4/4/5/4/5/5 | 4.46 | L | - | Y | Attacks the exact evidence used in adoption decisions |
| C-0178 | FM-as-teacher vs FM-as-engine frontier | 3/4/4/4/3/3/4/4/3/4/3/3/3 | 3.46 | M | - | N | Engineering-flavored frontier mapping |

## C7. Detection vs segmentation representation conflict (0179–0204) — kept 6/26

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0179 | Equivariance is the contested resource | 4/4/5/4/4/3/4/4/4/4/4/4/4 | 4.00 | M | - | Y | Gives the det/seg conflict a measurable quantity |
| C-0180 | Detection pretraining: recall up, boundary down | 4/4/4/4/3/3/4/4/4/4/3/4/3 | 3.69 | M | - | N | Matched-scale pretraining checkpoints scarce |
| C-0181 | Query competition collapses touching instances | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Near-miss; adjacency-conditioned analysis strong |
| C-0182 | Duplicate-suppression vs boundary trade-off | 3/3/4/4/4/3/4/4/4/4/3/3/3 | 3.54 | M | - | N | Loss-interaction non-monotonicity risk |
| C-0183 | Center-based failure on elongated structures | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; anchor-free literature nearby |
| C-0184 | Conflict-depth measurement prescribes split | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; conflict depth drifts during training |
| C-0185 | ROI-grid boundary ceiling, regime split | 4/4/4/5/5/4/4/4/4/4/3/4/4 | 4.08 | L | - | N | Close call; learned sub-grid interpolation weakens bound |
| C-0186 | Offset-to-center vs offset-to-boundary probes | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close; probing instrument, supports 0179 |
| C-0187 | Amodal-modal supervision contradiction | 5/4/5/4/4/4/4/4/4/4/4/4/4 | 4.15 | M | - | Y | Precise occlusion-conditioned error signature |
| C-0188 | Masks help boxes, boxes don't help masks | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; budget-matching cost model contentious |
| C-0189 | Anchor-set fingerprints persist after transfer | 4/3/4/3/4/3/4/4/4/3/3/3/3 | 3.46 | M | - | N | Subtle periodicity; power-hungry |
| C-0190 | Paradigms differ only at boundary pixels | 5/4/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | L | - | Y | Cheap spatial decomposition reframing paradigm debates |
| C-0191 | Things/stuff split is a frequency split | 4/3/4/3/4/3/4/4/4/3/3/3/3 | 3.46 | M | - | N | Partial support likely; countability objection |
| C-0192 | Mask-classification queries secretly boxes | 5/4/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | CI | Y | Protected counter-intuitive lineage audit |
| C-0193 | Mask-AP archaeology: boundary progress flat | 4/4/4/4/4/4/4/4/4/4/4/4/4 | 4.00 | M | - | N | Close call; checkpoint comparability risk |
| C-0194 | Coarse language hurts masks more than boxes | 4/4/4/3/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Metric commensurability problem |
| C-0195 | Crowding phase diagram for counting | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; synthetic-to-real boundary transfer risk |
| C-0196 | Pixel-to-lesion confidence is broken | 4/5/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | - | Y | Unformalized clinical decision-layer problem |
| C-0197 | Box-supervision ceiling flags prior exploitation | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; ceiling depends on prior model class |
| C-0198 | Pareto price of det+seg head sharing | 4/4/4/4/3/2/4/4/4/4/3/3/3 | 3.54 | M | - | N | Dense loss-weight sweeps expensive |
| C-0199 | Identity vs boundary: two error processes | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Close; decomposition useful, video niche here |
| C-0200 | Center+offset interpolates the paradigms | 3/3/4/3/4/3/4/4/4/3/3/3/3 | 3.38 | M | - | N | Interpolation claim low-stakes either way |
| C-0201 | Seg teaches det better than det teaches seg | 4/4/4/4/4/3/4/4/4/4/3/3/4 | 3.77 | M | - | N | Teacher-quality matching across tasks contentious |
| C-0202 | FPN allocation from dataset statistics | 3/3/4/3/4/3/4/4/3/4/3/3/3 | 3.38 | M | - | N | Scoped to explicit pyramids; engineering rule |
| C-0203 | Matching instability predicts duplicates | 4/3/4/4/4/3/4/4/4/4/3/3/3 | 3.62 | M | - | N | Rare-event statistics need huge eval scale |
| C-0204 | Window-size discontinuity on large lesions | 4/5/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | - | Y | Hidden failure of universal practice; clean RD design |

## C8. Boundary quality as a scientific problem (0205–0232) — kept 7/28

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0205 | Boundary error budget: aleatoric/protocol/model | 5/5/5/4/4/4/4/4/4/4/4/4/5 | 4.31 | M | - | Y | Foundational accounting the cluster stands on |
| C-0206 | Physics floor for boundary metrics | 5/5/5/4/4/4/4/4/4/4/4/4/4 | 4.23 | M | - | Y | Missing yardstick: when is boundary progress illusion |
| C-0207 | Boundaries learn slower: metric-resolved scaling | 4/4/4/4/3/2/4/4/4/4/4/4/3 | 3.69 | M | - | N | Close call; compute-heavy sweeps, strong if run |
| C-0208 | CE displacement bias derived and verified | 4/4/5/5/4/4/4/4/4/4/4/4/4 | 4.15 | M | - | Y | Rare theory-with-verification; correctable volumetry bias |
| C-0209 | Calibrated boundary-distance from logit margins | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; useful calibration tool, narrower question |
| C-0210 | Autocorrelation-corrected boundary statistics | 5/5/4/5/4/4/4/4/4/4/4/4/5 | 4.31 | L | - | Y | Field-wide inference repair; anti-conservative tests |
| C-0211 | Humans complete boundaries, models don't | 4/3/4/4/3/4/3/4/4/4/3/3/3 | 3.54 | M | - | N | Human study; convention-vs-perception ambiguity |
| C-0212 | Annotation-tool fingerprints in ground truth | 5/4/4/4/4/4/3/4/5/4/4/4/4 | 4.08 | M | CI | Y | Protected: unexplored confound in every benchmark; dataset-flag |
| C-0213 | Boundary skill is not transferable | 4/4/4/4/4/3/4/4/4/4/3/3/4 | 3.77 | M | - | N | Close; correlation-structure study, restriction-of-range risk |
| C-0214 | Sub-pixel boundary readout from logits | 5/4/4/4/5/5/4/4/4/5/4/4/5 | 4.38 | L | CI | Y | Protected: free precision; readout-problem reframing |
| C-0215 | Universal scale-relative loss-band law | 3/3/4/3/4/3/4/4/4/4/3/3/3 | 3.46 | M | - | N | Shallow optima would void the law |
| C-0216 | Distance losses reshape tails, not means | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; distribution-level analysis, fold into 0210 protocol |
| C-0217 | Through-plane error dominates, unmeasured | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; direction decomposition valuable, GT reliability issue |
| C-0218 | Boundary errors are reproducible bias fields | 5/5/5/4/4/3/4/4/4/4/4/5/4 | 4.23 | M | - | Y | If bias dominates, cheap correction beats loss research |
| C-0219 | Decoder type identifiable from outputs | 4/3/4/4/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Forensics interesting; nuisance-factor stakes modest |
| C-0220 | Clinician-preference boundary metric | 4/5/4/4/3/4/2/4/4/4/4/4/3 | 3.77 | M | - | N | Close; clinician-study cost, single-task scope |
| C-0221 | Topology enforcement costs local geometry | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; frontier tracing useful, method-sweep flavor |
| C-0222 | Architecture boundary-bandwidth transfer function | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; spec-sheet idea, annotation-smoothing contamination |
| C-0223 | Oracle refinement headroom accounting | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; bounds a genre, oracle-family dependence |
| C-0224 | Physical-truth boundary calibration set | 5/5/4/4/2/3/2/4/4/4/4/5/3 | 3.77 | H | - | N | Acquisition cost; propose as joint effort with 0206 |
| C-0225 | Curve-space vs pixel-space uncertainty | 4/4/4/4/3/4/4/4/4/3/3/4/3 | 3.69 | M | - | N | Technically heavy; calibration endpoint good |
| C-0226 | Hard-mask binarization instills bias | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; soft-label protocol dependence; ties to 0214 |
| C-0227 | Hausdorff events need their own taxonomy | 4/4/4/4/4/4/4/4/4/4/3/3/4 | 3.85 | M | - | N | Cause annotation judgment-laden |
| C-0228 | Factor analysis of segmentation metrics | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; psychometric framing nice, descriptive |
| C-0229 | Evaluation resolution flips rankings | 4/4/4/4/5/4/4/4/4/4/3/4/4 | 4.00 | L | - | N | Close; overlaps 0334/0339 protocol-stability audits |
| C-0230 | Losses are boundary priors in disguise | 4/4/5/4/4/4/4/4/4/4/3/4/4 | 4.00 | M | - | N | Close; stationary analysis overlaps 0208 (kept) |
| C-0231 | Refinement gains concentrate on unreliable labels | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; needs multi-rater strata + physical arm |
| C-0232 | Boundary-error → clinical-endpoint sensitivity map | 4/5/4/4/4/4/4/4/4/4/4/4/4 | 4.08 | M | - | N | Near-miss; merge with 0177's clinical-metric program |

## C9. Ambiguous labels / inter-rater disagreement (0233–0260) — kept 6/28

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0233 | Disagreement maps as free error oracle | 4/5/4/4/4/4/3/4/4/4/4/4/4 | 4.00 | M | - | Y | Model-free QC forecaster; rater-disjoint control |
| C-0234 | Consensus fusion is where ambiguity dies | 5/5/5/4/4/4/3/4/4/4/4/5/5 | 4.31 | M | CI | Y | Protected: indicts default preprocessing measurably |
| C-0235 | Disagreement = style offsets + true ambiguity | 5/5/5/4/4/4/3/4/4/4/4/4/4 | 4.15 | M | - | Y | Mixed-effects decomposition; changes variance budgets |
| C-0236 | Raters are transformations, not noise | 4/4/5/4/3/4/2/4/4/4/4/4/3 | 3.77 | M | - | N | Near-miss; ≥5-rater datasets scarce |
| C-0237 | Ambiguity predictable from image alone | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; extends ambiguity methods to single-rater data |
| C-0238 | Rank models by rater-distribution likelihood | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; GED-style scoring exists, reordering claim untested |
| C-0239 | Rater-budget dose-response law | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; annotation economics, subsampling design simple |
| C-0240 | Physics predicts rater disagreement | 4/4/5/4/4/4/3/4/4/4/4/4/4 | 4.00 | M | - | N | Close call; strong tie to 0206, trimmed on budget |
| C-0241 | Disagreement training exports calibration | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; shift changes true ambiguity, confounded |
| C-0242 | Annotator confidence is uninformative | 4/3/4/4/3/4/2/4/4/4/3/3/3 | 3.46 | M | - | N | Requires new collection protocol |
| C-0243 | Prob-seg models collapse local ambiguity | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; locality-resolved diversity metrics useful |
| C-0244 | Agreement-ordered curricula | 3/3/4/3/4/4/3/4/4/4/3/3/3 | 3.46 | M | - | N | Curriculum effects notoriously small |
| C-0245 | Tolerance-band metrics from rater variance | 5/5/4/4/4/4/3/4/4/4/4/4/4 | 4.08 | M | - | Y | Separates progress from within-ambiguity noise fitting |
| C-0246 | Synthetic raters ≠ real disagreement | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; dataset-batch merge flag (simulation validity) |
| C-0247 | Disagreement is partly ontology mismatch | 4/4/4/4/3/4/2/4/4/4/3/4/3 | 3.62 | M | - | N | Two-phase re-annotation cost; valuable if run |
| C-0248 | Spatial expertise signatures for crowd fusion | 4/4/4/3/3/4/2/4/4/3/3/3/3 | 3.38 | M | - | N | Expertise-labeled multi-rater data scarce |
| C-0249 | Standard losses fail multimodal truth | 5/4/5/4/4/4/3/4/4/4/4/4/4 | 4.08 | H | HR | Y | Protected: invalid-average pathology, safety stakes |
| C-0250 | Down-weighting ambiguity hurts OOD | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; sign-flip claim neat, effect-size uncertain |
| C-0251 | Session fatigue is recoverable label noise | 4/3/4/3/3/4/2/4/5/3/3/3/3 | 3.38 | M | - | N | Timestamped annotation data rare |
| C-0252 | Adjudicated consensus is a new rater | 5/4/4/4/3/4/2/4/5/4/3/4/3 | 3.77 | H | - | N | Close call; pre-adjudication labels rarely retained |
| C-0253 | TTA disagreement vs human disagreement | 4/4/4/4/5/5/3/4/4/4/3/4/5 | 4.08 | L | CF | Y | Protected cheap: validates the field's free surrogate |
| C-0254 | Multi-rater budget on boundary bands only | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; simulation-first design is doable |
| C-0255 | Whose style did the model learn | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; allegiance framing nice, control burden |
| C-0256 | Rater simulators pass discrimination tests? | 4/4/4/4/3/4/3/4/4/4/3/4/3 | 3.69 | M | - | N | Per-rater data requirements steep |
| C-0257 | Grade disagreement carries prognosis | 4/5/4/4/3/4/2/4/4/4/4/4/3 | 3.77 | M | - | N | Close call; outcome-linked multi-rater data limiting |
| C-0258 | Disagreement vs confident-learning error detection | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; division-of-labor result useful |
| C-0259 | "Within rater variability" safety argument fails | 4/5/4/4/4/4/3/4/4/4/4/4/4 | 4.00 | M | - | N | Close; position-paper flavor, keep as companion to 0245 |
| C-0260 | Rater style is low-dim and transferable | 4/4/4/4/3/4/2/4/4/4/3/4/3 | 3.62 | M | - | N | Multi-structure multi-rater data scarce |

## C10. Tokenization / resolution / memory artifacts (0261–0288) — kept 6/28

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0261 | Grid-phase performance oscillation | 5/4/4/4/5/5/4/4/4/5/4/4/5 | 4.38 | L | - | Y | Cheap, sharp, unmeasured aliasing artifact claim |
| C-0262 | PE-interpolation spatial distortion field | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close call; subsumes 0083; strong runner-up |
| C-0263 | Predict artifact-token locations pre-forward | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; register-token literature moving fast |
| C-0264 | Tokenizer destroys thin structures at layer one | 5/5/5/4/4/4/4/4/4/4/4/4/4 | 4.23 | M | - | Y | Layer-of-loss attribution; defines unreachable anatomy |
| C-0265 | Window-boundary seams in dense outputs | 4/3/4/4/4/4/4/4/4/4/3/3/4 | 3.77 | M | - | N | Close; effects likely small at convergence |
| C-0266 | Error-accumulation law of memory video seg | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | SAM2-batch merge flag (memory drift theme) |
| C-0267 | Token pruning drops boundary tokens | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; audit framework useful, method-specific outcomes |
| C-0268 | Packed-training cross-image leakage | 4/3/4/4/3/3/4/4/4/4/3/3/3 | 3.54 | M | - | N | Implementation-specific; two-codebase burden |
| C-0269 | Anti-aliased patchification fixes ViT pathologies | 4/4/5/4/4/3/4/4/4/4/4/4/4 | 4.00 | M | - | Y | Principled causal fix tested against multiple artifacts |
| C-0270 | High-res fine-tuning redistributes ERF | 4/4/4/4/4/3/4/4/4/4/3/3/4 | 3.77 | M | - | N | ERF measurement noise; predictive claim soft |
| C-0271 | CLS vs mean pooling decides dense usability | 4/4/4/4/3/2/4/4/4/4/3/4/3 | 3.62 | M | - | N | Controlled pretraining required; modest scale OK but trimmed |
| C-0272 | Quantization damages boundaries first | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close call; deployment-relevant, recipe-flavored |
| C-0273 | Window-position error profile; free blend win | 4/5/4/4/5/4/4/4/4/5/3/4/5 | 4.23 | L | - | Y | Universal pipeline audit with immediate payoff |
| C-0274 | Anisotropy-matched 3D tokenization | 3/4/4/4/4/3/4/4/4/4/3/3/4 | 3.69 | M | - | N | Closest to architecture swap; hypothesis thin |
| C-0275 | Memory-token capacity saturation | 4/4/4/4/3/3/3/4/4/4/3/4/3 | 3.62 | M | - | N | Synthetic-complexity mapping risk |
| C-0276 | Feature upsamplers hallucinate prior detail | 5/5/5/4/4/4/4/4/4/4/4/4/4 | 4.23 | M | - | Y | Fabrication-risk adjudication; timely for medical use |
| C-0277 | Attention sinks: parasitic or load-bearing | 4/3/4/4/4/3/4/4/4/4/3/3/4 | 3.69 | M | - | N | Train/inference regime disagreement risk |
| C-0278 | Patch-size scaling laws from data statistics | 4/4/4/4/3/2/4/4/4/4/4/4/3 | 3.69 | M | - | N | Close; compute-heavy sweeps |
| C-0279 | Multi-scale models secretly switch strategies | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; untrained-resolution dip is the one hard prediction |
| C-0280 | Dense extrapolation benchmark for encodings | 4/4/4/4/3/3/4/4/4/4/3/3/3 | 3.62 | M | - | N | Benchmark engineering; folklore-check value |
| C-0281 | Stage-wise aliasing compounds in hierarchies | 4/4/4/4/4/3/4/4/4/4/3/3/4 | 3.77 | M | - | N | Close; folded conceptually into 0269 |
| C-0282 | Long sequences starve small objects | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; token-count/resolution controls delicate |
| C-0283 | WSI tile artifacts propagate to biomarkers | 4/4/4/4/4/4/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; pathology-specific, GT tiling confound |
| C-0284 | VQ codebook caps boundary precision | 4/4/4/4/4/4/4/4/4/4/4/4/4 | 4.00 | M | - | N | Close call; timely for unified models, oracle approximation |
| C-0285 | Orientation priors in position embeddings | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; intervention isolates positional share |
| C-0286 | Mask ratio is a hidden boundary knob | 4/4/4/4/3/2/4/4/4/4/3/4/3 | 3.62 | M | - | N | Controlled pretraining twins required |
| C-0287 | Numerics flip boundary pixels at method-gain rates | 5/5/4/4/5/4/4/4/4/4/4/4/5 | 4.31 | M | HR | Y | Protected: unacknowledged variance term in benchmarks |
| C-0288 | Aspect-ratio squashing teaches deformation | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; twin trainings needed, effect plausible |

## C11. Community beliefs that may be false (0289–0314) — kept 6/26

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0289 | Curated small pretraining can beat web-scale | 4/5/4/4/3/2/4/4/4/4/4/4/4 | 3.85 | M | - | Y | Attacks "take the biggest" with a crossover predictor |
| C-0290 | Dice loss vs properly tuned weighted CE | 4/5/4/4/4/3/4/4/3/5/4/4/4 | 4.00 | M | - | Y | The field's most-repeated loss advice, finally adjudicated |
| C-0291 | ImageNet-pretraining obsolescence re-test | 3/4/4/4/4/3/4/4/2/4/3/3/4 | 3.54 | M | - | N | Well-trodden territory; likely-published risk high |
| C-0292 | ViT data hunger under equalized recipes | 3/4/4/4/4/3/4/4/3/4/3/3/4 | 3.62 | M | - | N | Close; matching disputes, moderate novelty |
| C-0293 | TTA degrades calibration and boundaries | 4/4/4/4/5/4/4/4/4/4/3/4/4 | 4.00 | L | - | N | Near-miss; merge with 0056 (TTA drift) program |
| C-0294 | Dense contrastive SSL doesn't need big batches | 4/4/4/4/3/2/4/4/4/4/3/4/3 | 3.62 | M | - | N | Pretraining sweeps costly; democratization angle noted |
| C-0295 | When 3D actually beats 2.5D: a moderator | 4/5/4/4/4/3/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close call; compute-matching conventions contested |
| C-0296 | Deep supervision = implicit warmup | 4/4/5/4/4/3/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; factorial design right, stakes moderate |
| C-0297 | Seed ensembles vs diverse ensembles | 4/4/4/4/4/3/4/4/4/4/3/3/4 | 3.77 | M | - | N | Pool-composition sensitivity |
| C-0298 | Domain randomization trades worst sites for mean | 4/5/4/4/4/3/3/4/4/4/3/4/4 | 3.85 | M | - | N | Close; needs genuinely many sites |
| C-0299 | Robust losses make thresholds redundant | 4/4/4/4/4/3/4/4/3/4/3/3/4 | 3.69 | M | - | N | Robust losses have own hyperparameters; wash risk |
| C-0300 | nnU-Net dominance: preprocessing or architecture | 4/5/5/4/4/3/4/5/4/4/4/5/5 | 4.31 | M | - | Y | Highest-leverage credit assignment in medical seg |
| C-0301 | Frozen-backbone ceiling with real readouts | 4/5/4/4/4/3/4/4/3/4/4/4/4 | 3.92 | M | - | Y | Tests the universal fine-tuning assumption |
| C-0302 | Safe label-violation augmentation budget | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; rater-variance calibration neat |
| C-0303 | Task-format alignment matters less than believed | 4/4/4/4/3/2/4/4/4/4/3/4/3 | 3.62 | M | - | N | Controlled pretraining cost |
| C-0304 | Do boundary losses improve boundary metrics | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; fold into 0210+0216 verification protocol |
| C-0305 | Resample vs reweight = BatchNorm interaction | 4/4/5/4/4/4/4/4/4/4/3/4/4 | 4.00 | M | - | N | Close; tidy mechanism, moderate reach |
| C-0306 | Resolution has per-structure optima | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; joint RF/resolution sweep needed |
| C-0307 | MTL gains vanish under matched budgets | 4/4/4/4/3/2/4/4/4/4/3/4/3 | 3.62 | M | - | N | Matching conventions contested; 0340 covers meta-claim |
| C-0308 | SSL robustness splits by corruption family | 4/4/4/4/4/3/4/4/3/4/3/4/4 | 3.77 | M | - | N | Matched twins scarce |
| C-0309 | Synthetic data = expensive distribution smoothing | 4/4/4/4/4/3/4/4/3/4/3/4/4 | 3.77 | M | - | N | Close; diversity-matching metric disputes |
| C-0310 | Distillation transfers teacher error structure | 5/5/5/4/4/3/4/4/4/4/4/4/4 | 4.15 | M | - | Y | FM→specialist path as a bias conduit; ties 0218 |
| C-0311 | Dice early stopping truncates boundary learning | 4/4/4/4/5/4/4/4/4/5/3/4/5 | 4.15 | L | CF | Y | Protected cheap: universal-convention audit |
| C-0312 | Attention explanations fail dense faithfulness | 4/4/4/4/4/4/4/4/3/4/3/4/4 | 3.85 | M | - | N | Close; faithfulness-metric pathologies |
| C-0313 | Patch training loses global-context evidence | 4/4/4/4/3/3/4/4/4/4/3/4/4 | 3.77 | M | - | N | Close; 0204 covers the sharpest slice of this |
| C-0314 | Benchmark rank barely predicts medical transfer | 4/5/4/4/4/3/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close call; probe-based selector is the useful half |

## C12. Cheap experiments overturning implicit assumptions (0315–0340) — kept 10/26

| ID | One-line | Scores | Avg | Risk | Prot | Keep | Reason |
|---|---|---|---|---|---|---|---|
| C-0315 | Scramble test for global-context claims | 5/4/5/4/5/5/4/4/4/5/4/4/5 | 4.46 | L | CF | Y | Protected cheap: universal mechanism-verification tool |
| C-0316 | Random-frozen prompts vs learned prompts | 5/4/4/4/5/5/4/4/4/5/4/4/5 | 4.38 | L | CF | Y | Protected cheap: bounds semantic content of prompt learning |
| C-0317 | 8× downsampled masks: benchmark sensitivity | 4/4/4/4/5/4/4/4/4/5/3/4/5 | 4.15 | L | - | N | Close; merge with 0339/0321 sensitivity-certificate line |
| C-0318 | Image-free prior floors for benchmarks | 4/4/4/4/5/5/4/4/4/5/3/4/5 | 4.23 | L | - | N | Dataset-batch merge flag (prior-floor theme) |
| C-0319 | Single-volume SSL pretraining control | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; modality-dependence caveat |
| C-0320 | Component-swap attribution audit | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; entangled components risk; 0340 covers meta-claim |
| C-0321 | 3-rater re-annotation noise floor for leaderboards | 4/5/4/4/4/5/3/4/4/5/4/4/5 | 4.23 | L | CF | Y | Protected cheap: decisive per dollar; dataset-flag |
| C-0322 | Segmentation logit lens per class | 4/3/4/4/5/5/4/4/4/4/3/3/4 | 3.92 | L | - | N | Close; interpretability transplant, modest stakes |
| C-0323 | Per-class channel sparsity probes | 4/3/4/4/5/5/4/4/4/4/3/3/4 | 3.92 | L | - | N | Close; pruning-adjacent literature |
| C-0324 | Random-frozen-encoder benchmark control | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | L | - | N | Close; decoder-capacity dependence weakens verdicts |
| C-0325 | Histogram matching as the missing DA baseline | 4/5/4/4/5/5/4/4/3/5/3/4/5 | 4.23 | L | CF | Y | Protected cheap: possibly reframes DA benchmark difficulty |
| C-0326 | Slice-order permutation test of 3D claims | 5/4/4/4/5/5/4/4/4/5/3/4/5 | 4.31 | L | CF | Y | Protected cheap: zero-training mechanism check; absorbs 0153 |
| C-0327 | Most fine-tuning gain arrives in epoch one | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; schedule confounds; regime-refocus idea noted |
| C-0328 | Train/test near-duplicate contamination audit | 4/5/4/4/4/4/4/4/3/4/4/4/5 | 4.08 | M | - | Y | High-consequence hygiene; dataset-flag; absorbs 0170 |
| C-0329 | Image prototypes replace the text encoder | 5/4/5/4/5/5/4/4/4/5/4/4/5 | 4.46 | L | CF | Y | Protected cheap: bounds "language-driven" claims precisely |
| C-0330 | Perturbation noise floors for boundary metrics | 4/4/4/4/5/5/4/4/4/5/3/4/5 | 4.23 | L | - | N | Near-miss; merge with 0321/0339 as one metrology paper |
| C-0331 | Semantic-permutation training control | 4/4/4/4/4/3/4/4/4/4/3/4/4 | 3.85 | M | - | N | Close; pretrained-weight leakage caveat |
| C-0332 | Mask-the-lesion occlusion audit of detectors | 5/5/4/4/5/5/4/4/3/4/4/4/5 | 4.31 | L | CF | Y | Protected cheap: per-model context-shortcut prevalence |
| C-0333 | 5-seed re-runs of headline dense claims | 4/4/4/4/4/3/4/4/3/4/3/4/4 | 3.77 | M | - | N | Overlaps 0094 (kept) and 0340 (kept) |
| C-0334 | Evaluate at 2× resolution: rankings reshuffle | 4/4/4/4/5/5/4/4/4/4/3/4/4 | 4.08 | L | - | N | Close; overlaps 0229; one-sweep value noted |
| C-0335 | Linear probe matches the fancy decoder | 4/4/4/4/5/5/4/4/4/4/3/4/4 | 4.08 | L | - | N | Close; served by 0301's readout-ceiling program |
| C-0336 | Same loss differs across frameworks | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; reproducibility microscope, narrow claim |
| C-0337 | Augmentation-normalization ordering effects | 4/4/4/4/4/4/4/4/4/4/3/4/4 | 3.92 | M | - | N | Close; pipeline-factor audit, folds into 0336 theme |
| C-0338 | Zero skip connections at inference | 4/4/4/4/5/5/4/4/4/4/3/4/4 | 4.08 | L | - | N | Close; off-distribution ablation caveat |
| C-0339 | ±1px ground-truth morphology re-scoring | 5/5/4/4/5/5/4/4/4/5/4/4/5 | 4.46 | L | CF | Y | Protected cheap: convention-matching vs skill; dataset-flag |
| C-0340 | Compute-matched baselines: field inflation factor | 4/5/4/4/3/2/4/4/4/4/4/5/4 | 3.92 | M | - | Y | Meta-scientific capstone; correction coefficient |

---

## Keep summary

- **Kept: 74 / 340** (target 67–75).
- Per cluster: C1 5, C2 5, C3 5, C4 5, C5 6, C6 7, C7 6, C8 7, C9 6, C10 6, C11 6, C12 10.
- Protected high-risk/high-reward (HR, 10): 0023, 0040, 0072, 0078, 0091, 0124, 0162, 0173, 0249, 0287.
- Protected counter-intuitive (CI, 7): 0050, 0056, 0113, 0192, 0212, 0214, 0234.
- Protected cheap-to-falsify (CF, 10): 0253, 0311, 0315, 0316, 0321, 0325, 0326, 0329, 0332, 0339.
- Kept on merit alone (47, including 0132): all other Keep=Y rows.
- Cross-batch merge flags: SAM-failure adjacent — 0074, 0106, 0139, 0266 (all eliminated here). Dataset-failure adjacent — 0043, 0110, 0165, 0170, 0246, 0318, 0330 (eliminated) and 0127, 0212, 0321, 0328, 0339 (kept, flagged).
