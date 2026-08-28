# Stage 2 — A+B Cluster Map (partial merge; Batch C pending)

**Pool:** 130 unique ideas (73 A + 75 B survivors, 18 merges — see `stage2_AB_duplicates.md`).
**Clusters:** 16 research themes. Merged ideas (`MERGE-XX`) are listed under their home cluster with constituent IDs.
**Notation:** protection flags follow each ID where relevant (HR/HRHR = high-risk/high-reward, CI = counter-intuitive, RM/DM = disagreement magnet, CF = cheap-to-falsify, M = merit/unprotected).

Counts: C1 9 · C2 12 · C3 5 · C4 12 · C5 5 · C6 9 · C7 13 · C8 5 · C9 6 · C10 11 · C11 9 · C12 6 · C13 10 · C14 6 · C15 6 · C16 6 = **130**.

---

## AB-C1 — Auto-labeling ecology & ground-truth contamination (9)

**Theme:** The field's data flywheel — SAM-assisted annotation, pseudo-labeling, self-consuming training loops — is quietly imprinting model biases onto the community's future ground truth. This is the most consequential cross-batch program: both batches independently generated its core ideas.

| ID | One-line |
|---|---|
| MERGE-01 (A-0029+B-0019) | Model-in-the-loop annotation corrupts its own GT: crossover anchoring study + inheritance test [HR+RM/HRHR·DM] |
| A-0007 | SAM's mask granularity is an imprint of the SA-1B annotation *protocol*, not image statistics [RM] |
| MERGE-09 (A-0267+B-0329) | Weak-to-strong dense distillation: students inherit bias-type errors, surpass variance-type errors [HRHR·DM] |
| B-0001 | SAM pseudo-label noise is structured/content-correlated; i.i.d. noise-robust learning theory fails on it [CF] |
| B-0191 | Error amplification in self-consuming segmentation pipelines: stability conditions of the data flywheel |
| B-0320 | Everything-mode output is positive-unlabeled data; PU-corrected training repairs the closed-world error |
| B-0009 | Geometric-stratum census of SA-1B: frequency-capability curve separating data-limited from architecture-limited failures [HRHR] |
| B-0006 | Pooling datasets with different conventions produces averaged boundary *bias*; one-token convention indicator fixes it [DM] |
| B-0053 | Part of the endoscopy "domain gap" is ontology shift, measurable by a 150-image bridge re-annotation [DM] |

**Program note:** MERGE-01 (mechanism at the annotator), A-0007 (mechanism at the protocol), B-0001 (noise model), MERGE-09 (inheritance/surpassing), B-0191 (multi-generation dynamics), B-0320 (statistical repair) form a full-stack contamination science. Highest strategic priority of the merged pool.

---

## AB-C2 — Benchmark validity & evaluation instruments (12)

**Theme:** The field's measurement instruments are themselves unmeasured: label-noise floors, sampling noise, instruction wording, human baselines, contamination, duplicate inflation, missing negatives.

| ID | One-line |
|---|---|
| MERGE-15 (A-0091+B-0082) | Label-noise-aware leaderboards: inter-annotator floors + relabeling bootstrap → rank-flip probabilities [RM/CF·DM] |
| MERGE-14 (A-0166+B-0037) | The annotation-tolerance ceiling: closed-form + empirical jitter floor; residuals predict the annotator [CI/CF] |
| A-0340 | Bootstrap the leaderboards: the fiction fraction of orderings within test-set sampling noise [CF] |
| A-0336 | Human floors and ceilings for segmentation benchmarks — the missing anchor [CI] |
| A-0337 | Annotation instructions as an experimental treatment: GT is instruction-contingent at SOTA-gap scale [RM] |
| B-0012 | Near-duplicate inflation of annotation-efficiency and few-shot claims; dedup-aware splits [CF·DM] |
| B-0017 | Transparency benchmarks have no target-absent images; ~500 curated negatives may invert rankings [CF] |
| B-0108 | Honest zero-shot: how much of "zero-shot" is hidden validation-set prompt/hyperparameter search [DM] |
| B-0110 | Certifiable FP/day estimation for rare-event monitoring via importance-sampled negatives |
| B-0294 | Bimodal difficulty-adjusted test losses as a corpus-free pretraining-contamination detector [HRHR] |
| A-0254 | A provably-novel procedurally-synthesized zero-shot benchmark (contamination-proof instrument) [RM] |
| A-0246 | Few-shot segmentation scores are base-class proximity in disguise; max-distance re-splits [CF] |

**Program note:** CONF-10 applies — this cluster's instruments condition how every other cluster's effect sizes should be read; schedule early.

---

## AB-C3 — Meta-science, replication & attribution (5)

**Theme:** Powered replication and attribution audits of the literature itself.

| ID | One-line |
|---|---|
| A-0245 | A 2015 U-Net with a 2026 recipe: what fraction of a decade's progress is recipe, not architecture [RM] |
| A-0226 | Attention-U-Net module gains re-run under tuned baselines and 5 seeds — the field's most common paper template [RM] |
| A-0242 | Publication-bias z-curve for reported segmentation deltas [RM] |
| MERGE-11 (A-0250+B-0024) | Deflationary baselines for few-shot segmentation: retrieval/correspondence + direct fine-tuning vs meta-learning [CF/DM·CF] |
| A-0261 | WSSS's residual gap decomposed by oracle substitution: is the CAM paradigm structurally exhausted? [RM] |

**Program note:** A-0226 ground-truths A-0242's caliper; B-0114 (in AB-C4) supplies the seed-noise nulls both need. Chain, don't duplicate.

---

## AB-C4 — PEFT & fine-tuning recipe science (12)

**Theme:** What parameter-efficient adaptation actually does, what explains its reported advantages, and what its hidden costs are.

| ID | One-line |
|---|---|
| A-0055 | LLRD alone may explain most of the reported PEFT advantage [CI+RM] |
| A-0067 | One dial: the encoder/decoder LR ratio explains most recipe variance [HR+RM] |
| A-0072 | Strong augmentation + frozen features vs LoRA at matched compute: adaptation as invariance injection [RM] |
| B-0114 | Seed variance of PEFT fine-tuning vs reported effect sizes; minimum-detectable-effect tables [DM] |
| B-0253 | Attention adapts "where", MLP adapts "what": a causal placement double-dissociation |
| B-0257 | The boundary tax of parameter efficiency: mIoU-equivalent, boundary-inferior [CI·DM] |
| B-0269 | Adapting the choice, not the masks: selection-head-only adaptation for convention-type gaps [CI·CF] |
| B-0270 | Is the input stem the whole story for semantics-preserving modality shift? [CI] |
| B-0272 | Capacity as regularization: small adapters may be noise-robust — the PEFT gap reverses under label noise [CI] |
| B-0306 | Less rank, more accuracy below ~20 samples: a rank-vs-n selection rule [CI·CF] |
| B-0315 | Five percent of elsewhere: out-of-domain anchor data as a superior regularizer [CI] |
| A-0238 | Depth auxiliary vs semantically-empty auxiliary: multi-task synergy or generic regularization? [CI] |

**Program note:** CONF-1/2/7/8 all live here — this cluster is deliberately stocked with productive contradictions. A-0055/A-0067/A-0072 + B-0114 should share one pre-registered grid.

---

## AB-C5 — Forgetting, retention & update geometry (5)

**Theme:** What fine-tuning destroys, where it lives, and how cheaply it comes back.

| ID | One-line |
|---|---|
| MERGE-07 (A-0076+B-0248) | The gain/retention frontier: forgetting as unforced error; retention-vs-effective-rank law [RM/DM] |
| A-0078 | Forgetting is mostly readout drift: linear re-probing recovers "lost" dense capabilities [CI] |
| A-0089 | Forgetting hysteresis: suppression, not erasure — refresh time-constants [HR] |
| MERGE-08 (A-0058+B-0260) | Low-rank adaptation amplifies shortcuts: worst-group + cross-site evidence, rank sweep as mechanism [HR+CI/CI·DM] |
| B-0251 | Predicting adapter-merging success from task-vector subspace geometry |

**Program note:** MERGE-07 is the shared infrastructure spine; A-0078/A-0089 are its mechanistic core. B-0315 (C4) may be the explicit version of what low rank does implicitly — Stage 3 should test that link.

---

## AB-C6 — Domain shift: diagnostics & test-time adaptation (9)

**Theme:** Classify shifts cheaply, adapt with the minimal sufficient tier, and audit the machinery the field built before foundation models.

| ID | One-line |
|---|---|
| MERGE-05 (A-0296+B-0064) | The UDA reality audit: fresh-pair ranking transfer × marginal value over foundation baselines [RM/DM] |
| MERGE-06 (A-0303+B-0057) | Token/norm-statistics recalibration: optimization-free TTA method + minutes-cheap shift-tier diagnostic [CF] |
| B-0054 | Which domain-distance metric actually predicts realized fine-tuning gain? |
| B-0072 | Amplitude-only Fourier adapters measure the "style fraction" of any shift [CI] |
| B-0078 | Language as a domain coordinate: text-described domains for zero-shot adaptation [HRHR] |
| B-0279 | Label-free PEFT: distilling prompt-ensemble consensus into adapters (collapse-resistant TTA) |
| A-0239 | Entropy TTA silently collapses rare classes; predictive trigger conditions [CF] |
| B-0304 | Style leaks through skip connections, bypassing deep-pathway invariance [CI·DM] |
| A-0305 | Night vision: adaptation gap or information deficit? Human-ceiling decomposition [CI] |

**Program note:** B-0072's style fraction is the routing variable for MERGE-06, B-0279, and B-0304 — run it first as the cluster's instrument.

---

## AB-C7 — Language–vision grounding & dense-VLM failure modes (13)

**Theme:** Does language actually steer dense prediction — and what happens when it lies, negates, specifies, or names the absent?

| ID | One-line |
|---|---|
| A-0041 | Does chain-of-thought causally change grounding, or is reasoning post-hoc? [HR+CI] |
| A-0187 | Negation: models select the negated object above chance — anti-accuracy, a fusion failure [CI+CF] |
| A-0183 | Spatial-relation minimal pairs near chance: is the core value proposition real? [CF] |
| MERGE-02 (A-0185+B-0241) | The absent-target hallucination benchmark: plausibility × prompt-assertiveness; refusal protocols [CF+RM/CI·CF] |
| A-0199 | Scene text hijacks grounding in proportion to OCR capability [CF] |
| A-0181 | CLIP dense misalignment is co-occurrence-structured, not random noise [M] |
| B-0124 | Text-space collinearity upper-bounds open-vocab confusion for amorphous classes [CF] |
| A-0031 | Paraphrase variance exceeds reported SOTA gaps in open-vocab segmentation [CF+RM] |
| A-0033 | Prompt-specificity inverse-U: the basic-level optimum, frequency-mediated [CI+CF] |
| A-0049 | Lay vs expert terminology for medical grounding: the register mismatch [CI+CF] |
| B-0132 | Where do VLMs lose spatial detail? Layer-wise localization-decay maps with validated tap points |
| B-0174 | Does text supervision smooth away boundary precision? The semantic-blur dose-response [CI·DM] |
| B-0185 | Knowledge conflict: dense VLMs regress to textbook priors exactly on abnormal cases [HRHR·DM] |

**Program note:** A-0183/A-0187/MERGE-02 share scenes, models, and attribution tooling; A-0181 is the mechanistic backbone that predicts where hallucinated masks land. B-0185 + A-0118 (C15) share the refusal-metric design.

---

## AB-C8 — Interactive segmentation & the prompt interface (5)

**Theme:** The interaction channel is an unmodeled interface with its own domain gaps, discontinuities, and failure etiquette.

| ID | One-line |
|---|---|
| MERGE-17 (B-0089+B-0193) | The human-prompt distribution gap: oracle-prompt evaluation inflation + training-side prompt mismatch [DM] |
| B-0083 | Medical-SAM rankings under 5 click protocols: cross-protocol rank correlation [CF·DM] |
| B-0104 | Wrong-prompt behavior: does SAM fail loudly or silently under semantic prompt errors? [CF] |
| B-0128 | Lipschitz geometry of the click-to-mask map; discontinuity density predicts interaction cost [CF] |
| B-0282 | Non-monotonic refinement: when more correction clicks make masks worse [CI·CF] |

**Program note:** CONF-14 — MERGE-17 and B-0083 need a shared protocol taxonomy before either runs.

---

## AB-C9 — Transparency, camouflage & layered scenes (6)

**Theme:** Targets that violate the one-surface-per-pixel assumption: what the representation encodes, which cues carry it, and where humans still win.

| ID | One-line |
|---|---|
| MERGE-10 (A-0141+B-0126) | What frozen features know about layered scenes: glass, background, or both — representation vs output format [HR+CI/CI] |
| MERGE-16 (A-0142+B-0159) | Depth failure as transparency signal: invalidity as inference feature and as free physics-generated supervision [CI/HRHR] |
| B-0075 | Does SAM segment glass by its reflections? Reflection-swap cue attribution [HRHR·CI] |
| B-0162 | Polarization-taught transparency: what fraction of the privileged advantage survives RGB-only inference? [HRHR] |
| A-0157 | The human floor on near-invisible glass: competence vs information bottleneck [CI] |
| A-0154 | Camouflage failure: attentional or perceptual? Oracle-prompt decomposition [CF] |

**Program note:** Ordering: MERGE-10 (is it in the features?) → B-0075 (which cue?) → B-0162/MERGE-16 (which supervision?), with A-0157 pricing the information limit.

---

## AB-C10 — Amorphous matter full stack: smoke, fire, wildfire (11)

**Theme:** Task redefinition for boundary-free matter: diagnosis (GT is ill-posed), supervision (physics labels), metric (latency), primitives (blobs not boxes), and the SAM mismatch.

| ID | One-line |
|---|---|
| A-0121 | Binary smoke masks are ill-posed GT: per-annotator density thresholds explain the disagreement [RM] |
| A-0122 | Beer–Lambert transmittance from paired frames as physically defined smoke GT [HR] |
| MERGE-03 (A-0006+B-0226) | One boundary-contrast law across amorphous / camouflage / transparency / lesion failure [CI/DM] |
| A-0128 | No prompt strategy rescues SAM on smoke; the density-conditioned shrinkage law [CF] |
| A-0126 | Detection latency, not IoU, as the wildfire metric: ranking disagreement claim [RM] |
| A-0123 | Fire segmenters are color detectors: hue-shift stress tests + colored-distractor battery [CI+CF] |
| A-0125 | Turbulence spectra as a label-free smoke signal: appearance-free self-supervision [HR] |
| B-0318 | Differentiable single-scattering renderer: 2D smoke masks supervise a 3D density field [HRHR] |
| B-0055 | Fog as a negative domain: does adapting to fog worsen smoke detection? [CI·DM] |
| A-0319 | Boxes are the wrong primitive for amorphous targets: blob/level-set formulations on decision metrics [M] |
| B-0219 | Is NMS the binding constraint for fragmenting-plume detection? Suppression-stage attribution [CI] |

**Program note:** CONF-3 — A-0121/A-0122 gate the y-axis of everything else here. The full stack (diagnosis → supervision → metric → primitive → data strategy) is the most coherent applied program in the pool.

---

## AB-C11 — Small structures & token-lattice artifacts (9)

**Theme:** Why small things fail: tokenization floors, lattice aliasing, register-token collisions, compression confounders, and what actually fixes them.

| ID | One-line |
|---|---|
| MERGE-04 (A-0161+B-0129) | The small-structure bottleneck: information-absent vs decoder-limited, probes + patch interventions [RM] |
| A-0003 | The IoU-vs-size failure law with a patch-size knee; curve collapse in patch units [CF] |
| A-0313 | Resolution beats architectural small-object remedies at matched compute [RM] |
| B-0288 | Inverse scaling pocket: smaller model variants beat larger ones on tiny structures [CI·DM] |
| A-0176 | Benchmark JPEG already deleted the small objects: compression as construction confounder [CI] |
| A-0174 | Register-token artifacts collide with and blind small objects [CF] |
| B-0122 | Angular aliasing: thin-structure quality oscillates with orientation vs the patch lattice [CI·CF] |
| B-0305 | Periodic performance in input size: resolution × patch-grid aliasing contaminates comparisons [CI·CF] |
| A-0170 | INR decoders hallucinate sub-pixel boundaries: synthetic-truth dissociation of metric gaming [CI] |

**Program note:** CONF-4 and CONF-6 live here. Share one size-stratified evaluation suite across all nine.

---

## AB-C12 — Uncertainty, calibration & confidence validity (6)

**Theme:** Is any of the field's uncertainty real — heuristic maps, free ensembles, quality heads, soft labels?

| ID | One-line |
|---|---|
| A-0103 | Uncertainty maps ≠ clinician disagreement once boundary bands are excluded [CI] |
| MERGE-18 (B-0120+B-0337) | Are free mask ensembles valid posteriors? Coverage tests for multimask spread and diffusion samples [CF/CF·DM] |
| B-0084 | Out-of-domain calibration of SAM's predicted-IoU head — load-bearing and never audited [CF] |
| A-0097 | Dice loss destroys calibration, imbalance-scaled; the CE→Dice schedule fix [RM] |
| B-0310 | Confidence inversion: soft-label training with mean-regression losses yields *harder* predictions [CI] |
| A-0280 | Uncertainty routes labels to the wrong pixels: confident errors beat uncertain boundaries for annotation value [CI+CF] |

**Program note:** A-0103 and MERGE-18 share multi-rater reference data with MERGE-15 (C2); coordinate collection once.

---

## AB-C13 — Representation science of visual foundation models (10)

**Theme:** What VFM features actually encode and why: edges vs objects, texture vs shape, convergence, emergence, in-context mechanisms, data vs method.

| ID | One-line |
|---|---|
| A-0001 | SAM follows edges, not objects: 2×2 camouflage/texture-edge dissociation [CI] |
| A-0013 | SAM2 lost static fine-boundary quality relative to SAM1: modality trade-off audit [CI+CF] |
| MERGE-13 (A-0021+B-0136) | Functional achromaticity: color-channel reliance from SAM to smoke [CI+CF/CI·CF] |
| A-0202 | The task×backbone matrix for frozen dense features under one matched protocol [M] |
| A-0203 | SSL "object emergence" as a crop-statistics artifact: causal retraining intervention [HR+CI] |
| A-0266 | Object discovery or texture grouping? Dissociation scenes for unsupervised segmentation [CI] |
| A-0211 | Texture-vs-shape verdict inverts between classification and dense readouts of the same backbone [CI] |
| A-0223 | In-context segmentation: abstraction or sophisticated copying? Semantic×visual support grids [CI] |
| A-0225 | Platonic convergence is semantics-only at patch level: geometric content does not align [RM] |
| A-0207 | Data vs method: data-overlap kernels explain inter-VFM variance better than objectives [RM] |

**Program note:** A-0266 (cheap correlational) gates A-0203 (expensive causal); A-0001/A-0211/A-0266 may share one texture-allegiance account. A-0202's harness serves A-0207 and A-0225.

---

## AB-C14 — Composed pipelines & preprocessing skepticism (6)

**Theme:** The interfaces between pipeline stages — detection→segmentation, SR→prediction, restoration→detection — are unmodeled and sometimes harmful.

| ID | One-line |
|---|---|
| B-0217 | The box-to-mask error transfer function; train under the detector's measured error distribution |
| B-0223 | Assigner-induced gradient starvation of elongated objects; ratio-conditional assignment [CI] |
| B-0233 | What does a detector add over change detection for static-camera monitoring? [DM·CI] |
| B-0331 | The hallucination-utility frontier of super-resolution for downstream dense prediction [DM] |
| B-0338 | Noise as signal: restoration deletes the forensic cues tiny-target detection relies on [CI] |
| B-0285 | Compression that helps: JPEG as a matched filter for smoke [CI·CF] |

**Program note:** CONF-5 (B-0338 vs B-0285) is this cluster's productive contradiction; aim for one target-relative theory of preprocessing.

---

## AB-C15 — Medical supervision economics & deployment safety (6)

**Theme:** Pricing supervision channels and cataloguing silent clinical failure modes.

| ID | One-line |
|---|---|
| A-0118 | Models hallucinate surgically removed organs: the atlas-prior safety failure [CI] |
| A-0093 | Why nnU-Net still wins: causal component-swap decomposition at matched budgets [HR+RM] |
| A-0100 | Flip-TTA harms lateralized anatomy: an invalid invariance inside challenge winners [CI+CF] |
| B-0156 | The exchange rate between radiology reports and pixel labels, per finding type |
| B-0182 | Absence statements as supervision: certified negations against hallucinated segmentations |
| B-0184 | Contrast-enhancement vessel GT is physiologically selective: blind to occluded segments [CI·DM] |

**Program note:** B-0156/B-0182/B-0184 form the supervision-pricing thread; A-0118 pairs with B-0185 (C7) on refusal metrics; CONF-11 (B-0184 vs MERGE-16's enthusiasm) and CONF-12 (A-0093 vs A-0245) apply.

---

## AB-C16 — Synthetic training data: coverage, artifacts & dose (6)

**Theme:** When synthesis helps, when it placebos, and when it poisons — coverage, fingerprints, dose thresholds, and realism-factor pricing.

| ID | One-line |
|---|---|
| B-0186 | Does generative augmentation actually cover the tail it promises to fix? Per-stratum coverage [DM] |
| MERGE-12 (A-0285+B-0190) | Synthetic-fraction dose-response: rare-class inversion + robustness-poisoning thresholds [CI] |
| B-0189 | The inpainting fingerprint: do models learn the lesion or the paste? [CI·CF] |
| B-0200 | Too-clean ground truth: annotator-noise-matched synthetic labels may beat perfect ones [CI] |
| A-0283 | Which realism factor buys sim-to-real transfer: 2⁴ factorial (geometry/texture/lighting/sensor) [M] |
| A-0287 | Procedural beats diffusion on web-sparse phenomena: the coverage-circularity limit [M] |

**Program note:** B-0186's per-stratum reporting discipline should be imposed on every synthetic-data claim in the pool; A-0287 supplies the data strategy for C10's smoke program and C9's transparency program.

---

## Cross-cluster dependency map (Stage 3 sequencing hints)

1. **Instruments before audits:** AB-C2's noise-floor/bootstrap instruments (MERGE-15, MERGE-14, A-0340, A-0337) condition effect-size claims in C3, C4, C6, C11 (CONF-10).
2. **GT redefinition before smoke claims:** A-0121/A-0122 gate MERGE-03, A-0128, A-0126, A-0319 (CONF-3).
3. **Cheap gates before expensive strikes:** A-0266→A-0203; MERGE-04 probe stage→intervention grid; B-0318's parity test→physical validation; B-0072 style fraction→MERGE-06/B-0279 routing.
4. **Shared infrastructure:** multi-rater data (MERGE-15, MERGE-14, A-0103, MERGE-18, A-0336); negative-set curation (B-0017, B-0110, MERGE-02); human prompt logs (MERGE-17, B-0083); size-stratified suites (all of C11); A-0202 harness (A-0207, A-0225).
5. **The PEFT grid:** A-0055/A-0067/A-0072/B-0114/MERGE-07/MERGE-08/B-0272 should be planned as one pre-registered compute program (CONF-1/2/7/8).

*End of cluster map. Batch C survivors will be assigned to these 16 themes or open new ones.*
