# P1 Wave B — Judge C: Value / Diversity / Anti-Collapse Audit (Windows14, Wave 2)

- **Task:** `p1_wave2_judge_C`
- **Role:** `judge_C_value_diversity` (high-value outliers, mode collapse, cluster overcrowding, SAM+X/LoRA+X/loss+X patterns, missing territories, QA)
- **Independence:** produced without reading wave2 Judge A or Judge B outputs.
- **Inputs (read-only, fetched from remote branches):**
  - `origin/cursor/windows14-p1-wave2-worker-a-cc54` → `worker_A.ideas.jsonl` (133 ideas, synthetic data + domain shift, 12 clusters)
  - `origin/cursor/windows14-p1-wave2-worker-b-8795` → `worker_B.ideas.jsonl` (126 ideas, SR/restoration + diffusion, 10 clusters)
  - `origin/cursor/windows14-p1-wave2-worker-c-9388` → `worker_C.ideas.jsonl` (130 ideas, negative results + contrarian, 13 clusters)
  - `origin/cursor/windows14-p1-wave2-worker-d-a7e5` → `worker_D.ideas.jsonl` (124 ideas, object detection, 15 clusters)
  - `origin/cursor/windows14-p1-wave2-worker-e-e584` → `worker_E.ideas.jsonl` (125 ideas, VLM dense prediction, 16 clusters)
  - Diversity-vs-existing reference (read-only, NOT modified): `origin/cursor/windows14-p1-wave1-consolidator-13bd` → `Windows14/_state/ideas_master.jsonl` (366 canonical wave1 ideas, ids `w14-0001..0366`)
- **Total wave2 ideas reviewed: 638.** All parsed as valid JSONL; each shard has a single consistent 15-field schema; 0 duplicate `id_seed`s within or across shards; all `evidence_status = HYPOTHESIS`.
- **No canonical files touched** (`window.lock.json`, `research_state.json`, `ideas_master.jsonl`, `research_ledger.md` untouched). Windows14 remains LOCKED. No worker or judge_A/judge_B files overwritten.

## Scope and non-claims

This audit flags ideas for *potential* value. **No novelty is verified here**: no literature search was performed, no papers are cited, and no flag should be read as a claim that an idea is new. All flags are advisory inputs to the wave2 consolidator; **no idea is dropped by this audit**.

## 0. Wave1 → Wave2 steering outcome (headline findings)

1. **The SAM+X / LoRA+X / loss+X collapse axes are gone.** Across all 638 ideas: 1 SAM mention, 0 LoRA mentions, ~3 "add a loss term" framings. Wave1's single-model anchoring flag was acted on effectively.
2. **Wave1's ten missing territories were substantially consumed.** Remote sensing/SAR (A, 12 ideas), LiDAR/driving (A, 11), microscopy/WSI (B, 14), industrial/agriculture/underwater (A, 11), video/streaming (B14+C8+D6+E4), fairness (C, 12), adversarial robustness (C, 12), annotation economics (C, partial), amodal/occlusion (D, partial), open-vocab semantics (D+E, extensive).
3. **Surface diversity is excellent.** Pairwise Jaccard over all 638 one-lines finds exactly one pair above 0.30 (w14w2c-113 / w14E-106 at 0.36 — a real cross-shard convergence, see JC2-CV-05). Duplication risk in wave2 is thematic, not lexical.
4. **The genre monoculture persists.** The dominant unresolved collapse axis is still the audit/diagnose/expose genre (see JC2-MC-01); wave2 steering fixed *territory* diversity but not *genre* diversity.

## 1. High-value outlier flags (45 ideas, 9 per shard)

Selection criteria: (a) field-level leverage if the hypothesis survives (evaluation validity, meta-science, safety); (b) contrarian against a stated default with a cheap decisive falsification; (c) mechanistic claims that unify or localize a phenomenon; (d) constructive ideas in an audit-heavy corpus. Machine-readable records in `judge_C.flags.jsonl` (type `high_value`).

### Worker A (synthetic data + domain shift) — 9

| id | why flagged |
|---|---|
| w14w2a-008 | Generator-mediated benchmark contamination with zero pixel overlap — redefines what "no test images in training" certifies; meta-science with field-level reach. |
| w14w2a-019 | Single-axis sim-to-real gap measurements don't add up; interaction terms dominate — attacks the ablation-decomposition paradigm itself. |
| w14w2a-036 | Self-generation loop collapse rate predictable from per-cycle boundary-entropy loss — converges with w14w2b-079 from an independent shard (raises prior). |
| w14w2a-045 | Critical period for renderer-artifact lock-in — training-dynamics science with a clean early-vs-late randomization design. |
| w14w2a-096 | Normalization-statistic re-estimation as the mandatory null model for sim-to-real papers — embarrassing-baseline attack with corrective protocol. |
| w14w2a-098 | Domain-adversarial training's gains as gradient-noise regularization, matched-noise control — decisive debunk design aimed at a whole method family. |
| w14w2a-106 | Uncanny valley for training data: high-realism synthetic data can hurt more than low-realism — memorable, contrarian, testable by realism-graded corpora. |
| w14w2a-127 | "Shift algebra": combined-shift performance approximately multiplicative in single-shift survivals — a compositional law enabling deployment forecasting. |
| w14w2a-133 | Sim-to-real gap localized in the decoder, not the encoder — cheap decisive freeze/swap experiment that redirects adaptation effort. |

### Worker B (SR/restoration + diffusion) — 9

| id | why flagged |
|---|---|
| w14w2b-004 | Joint restoration+segmentation pipelines pass hints steganographically instead of restoring — sharp collusion hypothesis, perturbation test in hours. |
| w14w2b-015 | Seed-instability separates hallucinated from recovered structure: training-free hallucination detector (designed counterpoint w14w2b-019 on deterministic samplers). |
| w14w2b-030 | Photon noise is informative signal, not just corruption; denoising removes luminance evidence — physics-grounded contrarian gem. |
| w14w2b-053 | Diffusion segmentation samples are under-dispersed vs annotator distributions — attacks the field's headline "distribution over masks" claim (cross-ref canonical w14-0054). |
| w14w2b-057 | Most trained mask-diffusion models are secretly deterministic; the diffusion machinery is dead weight — embarrassing audit of a hot method family. |
| w14w2b-067 | Task utility as a third axis of the perception-distortion tradeoff, non-monotonic in both — theory framing with broad leverage over the whole shard. |
| w14w2b-099 | Virtual staining is "segmentation laundering": evaluation double-counts the staining prior — evaluative-validity claim with clinical stakes. |
| w14w2b-101 | Segmentation accuracy oscillates with codec GOP structure (better on I-frames) — vivid periodic artifact invisible to shuffled-frame evaluation. |
| w14w2b-117 | Scoring restored-image segmentation against clean-image GT credits hallucination; evidence-limited GT flips rankings — protocol fix with field-level reach. |

Runners-up worth consolidator attention: w14w2b-017 (mode substitution collapses rare-class recall; carried in JC2-CV-06), w14w2b-088 (stain normalization flips diagnostic class), w14w2b-096 (WSI patch context ceiling), w14w2b-121 (diffusion-segmentation gains vanish compute-matched).

### Worker C (negative results + contrarian) — 9

| id | why flagged |
|---|---|
| w14w2c-005 | Claimed emergent zero-shot segmentation abilities as thresholded-metric artifacts — imports the emergence-mirage debate to dense prediction; re-analysis only, no training. |
| w14w2c-007 | Scaling same-protocol annotation converges to protocol bias, not ground truth — epistemological claim about what GT even is. |
| w14w2c-035 | Certified robustness certifies interior pixels, never boundaries — structural gap in the certification literature's meaning for dense tasks. |
| w14w2c-045 | Skin-tone segmentation gaps mostly photometric; luminance-matched evaluation erases the majority — high-stakes contrarian with a controlled decisive test (pairs with w14w2c-046, w14w2c-056). |
| w14w2c-057 | Fixing existing label errors beats collecting new images per annotation-hour — direct practice-changing economics claim. |
| w14w2c-066 | Tail-class quality bottlenecked by head-class boundary quality, not tail sample count — counterintuitive causal structure with a clean intervention. |
| w14w2c-097 | A decade of CAM-based weakly-supervised progress compresses to near-noise under a unified tuning protocol — field-level replication audit. |
| w14w2c-105 | Benchmark deltas below the ground-truth reproducibility floor are unfalsifiable — complements canonical w14-0243 (statistical power) with a measurement-theory floor. |
| w14w2c-125 | Distillation transfers the teacher's failure map; error-correlated students destroy ensemble and audit value — safety-relevant compression science. |

### Worker D (object detection) — 9

| id | why flagged |
|---|---|
| w14D2-007 | In crowds, recall dies inside the suppression stage, not the network (pre-NMS oracle recall stays high) — reframes the crowd-detection bottleneck cheaply. |
| w14D2-015 | A distinct mode of "false positives" are correct detections missing from GT, estimable by cross-detector agreement — GT-completeness meta-science. |
| w14D2-025 | Negative vocabulary is the underused half of open-vocab detection — constructive, cheap, immediately deployable. |
| w14D2-047 | Below a size floor, small-object AP measures annotation noise — leaderboard-validity claim; converges with w14w2c-108 and w14D2-061. |
| w14D2-071 | DETR queries tile latent position-size space with coverage gaps; the miss map is extractable from the trained model without test data — elegant mechanistic prediction. |
| w14D2-077 | The NMS-free property of set-prediction detectors is distribution-bound; deployed DETR pipelines silently need emergency suppression — deployment-critical audit. |
| w14D2-085 | Foundation detectors fail non-photographic imagery at the proposal stage, not classification — inverts the assumed bottleneck; directly actionable. |
| w14D2-089 | Detection emerges later in model scale than recognition: region binding, not recognition, is the scaling bottleneck — big-picture scaling science. |
| w14D2-121 | Novel-object detection and OOD rejection are mathematically opposed uses of the same scalar signal; claimed dual wins are operating points on one curve — conceptual result that reorganizes an evaluation subfield. |

Runners-up: w14D2-109 (hand occlusion as privileged pattern), w14D2-112 (undercount recoverable from pre-NMS score mass), w14D2-124 (NMS discard pile as free active-learning signal).

### Worker E (VLM dense prediction) — 9

| id | why flagged |
|---|---|
| w14E-001 | BPE token-count bias puts multi-token class names on a different score scale — mechanistic, universal, testable in a day. |
| w14E-018 | Token-limit right-truncation silently deletes restrictive modifiers (English puts them last) — sharp linguistic-structural failure with immediate engineering fix. |
| w14E-028 | Lateral spatial language broken because flip augmentation erased chirality from vision pretraining — deep training-cause claim (test-time twin: w14E-020 flip-TTA averages 'left' with 'right'). |
| w14E-067 | Register-token artifacts create position-stable phantom detections — timely mechanistic claim tied to a known ViT phenomenon, cheap to verify. |
| w14E-084 | Coordinate-emitting VLMs snap to round numbers: numeric tokenization as a quantization prior on localization error — delightful, decisive histogram test. |
| w14E-095 | "Alignment tax on pixels": safety tuning degrades dense outputs for sensitive-adjacent queries with no refusal issued — novel safety × dense-prediction intersection. |
| w14E-105 | A text-only probe forecasts per-sample grounding failure: benchmarks are partly language-solvable — benchmark-validity result with a reusable diagnostic. |
| w14E-115 | Negative-space referents ("the gap between the buildings") are unrepresentable — clean conceptual boundary of current dense grounding. |
| w14E-124 | State-referential masks never update ("the traffic light that is red" stays after it turns green): grounding as one-shot event, not maintained belief — reframes referring video segmentation. |

## 2. Cross-shard convergence within wave2 (12 families — dual-signal: value AND dedup risk)

Independent shards converging raises a hypothesis's prior and creates consolidation-time duplication risk. The consolidator should merge each family into one canonical idea with per-domain instantiations. Machine-readable in `judge_C.flags.jsonl` (type `convergence_dedup`).

| # | family | members | note |
|---|---|---|---|
| CV-01 | Self-consuming generation loops collapse boundary-complexity first (early-warning metric) | w14w2a-036, w14w2b-079 (+w14E-103 salience-drift variant) | Near-identical A/B claims; merge, keep E's language-side variant distinct. |
| CV-02 | Latent-autoencoder downsampling imposes a thin-structure floor | w14w2a-031, w14w2b-052 | Same architectural-floor hypothesis from two angles. |
| CV-03 | JPEG/codec grid artifacts become learned boundary/detection priors | w14w2b-013, w14D2-070, w14w2c-020, w14w2b-092 | Also overlaps canonical w14-0096 (JPEG × patch grid); consolidate as one artifact-physics program. |
| CV-04 | Copy-paste/compositing augmentation teaches edge-artifact shortcuts | w14w2c-068, w14D2-100, w14w2b-082 (+w14w2a-034 opposite-sign) | w14w2a-034 argues copy-paste *wins* — a designed disagreement worth preserving explicitly. |
| CV-05 | Caption/word frequency, not visual difficulty, governs per-class open-vocab quality | w14w2c-113, w14D2-022, w14E-010, w14E-055, w14E-106 | Three shards, the corpus's only lexical near-duplicate pair; strongest single merge target in wave2. |
| CV-06 | Regression-to-the-frequent: rare inputs silently replaced by frequent lookalikes | w14w2b-017, w14w2c-121, w14D2-027, w14E-057, w14E-063, w14E-087 | FOUR-shard convergence (restoration, contrarian, detection, VLM). Merged well, this is a candidate unifying cross-domain law — flagged both high-value-as-family and top dedup priority. |
| CV-07 | Vocabulary/query-set interference in open-vocab scoring | w14D2-026, w14D2-081, w14E-034, w14E-089, w14E-090 (+w14E-088) | Same renormalization mechanism; merge to one idea with detection and segmentation instantiations. |
| CV-08 | Temporal-consistency optimization installs persistence bias (late on state changes) | w14w2b-103, w14w2b-120, w14w2c-087, w14D2-118 (+w14D2-113 counterpoint, w14E-122/124 language variant) | Coherent program: keep the benchmark-design member (b-120) and the mechanism member (b-103) distinct. |
| CV-09 | Benchmark contamination via web crawls / generated-content drift | w14w2a-112, w14w2b-077/084/085/086/115, w14w2c-103/110, w14D2-060, w14E-101 | 10+ members and wave1 canonical already covers contamination (w14-0229, w14-0238). Overcrowded — cap hard at consolidation; keep the mechanistically distinct members (a-112 ecosystem drift, b-115 restoration-side memorization, c-110 post-crawl protocol). |
| CV-10 | Small-object metrics bounded by annotation noise | w14w2c-108, w14D2-047, w14D2-061 (+w14E-108 GT-error residual floor) | Same measurement-floor logic in segmentation and detection; merge with task-specific predictions. |
| CV-11 | Resampling/aliasing/upsampling mechanics create systematic spatial biases | w14w2b-034, w14D2-037, w14D2-044, w14D2-048, w14E-070, w14E-082 | Overlaps canonical w14-0099 (half-pixel bilinear offset). Consolidate as one "resampling mechanics" program, not six ideas. |
| CV-12 | Leaderboard metrics diverge from fixed-threshold deployment behavior | w14D2-020, w14D2-090, w14E-074, w14w2c-092, w14w2c-106, w14w2b-114 | Genre-wide pattern; keep the 2–3 sharpest instantiations, fold the rest. |

## 3. Overlap with wave1 canonical `ideas_master.jsonl` (8 flags)

Wave2 must be deduplicated against the 366 canonical ideas, not just internally. Machine-readable type `canonical_overlap`.

| # | wave2 members | wave1 canonical | recommendation |
|---|---|---|---|
| DX-01 | w14E-073, w14E-119 | w14-0010/0070/0081/0137/0169 (prompt-perturbation-as-uncertainty family) | Paraphrase disagreement is the language-space instance of the canonical family; merge as instantiation, not new idea. |
| DX-02 | w14E-080, w14E-064, w14E-083 | w14-0021, w14-0193 (patch/tokenization floor) | Same architectural-floor law; w14E-064 (fusion-stage scale) is the only genuinely new mechanism — keep that, fold the rest. |
| DX-03 | w14w2b-053, w14w2b-054, w14w2b-063 | w14-0054, w14-0135 (ambiguity/hypothesis-diversity collapse) | Same phenomenon, new (diffusion) mechanism; cross-reference rather than duplicate. |
| DX-04 | w14w2c-075 | w14-0192 (TTA raises mean while increasing catastrophic tail) | Near-identical claim generalized beyond medical; merge. |
| DX-05 | w14w2b-110 | w14-0363 (auto-exposure makes fires self-hiding) | Same camera-policy mechanism class, different domain; cross-reference. |
| DX-06 | w14E-029/030/033/036, w14w2c-120 | w14-0254 (negation blindness) | Wave2 expands one canonical idea into a five-idea program (absence, complement sets, negated attributes, scaling claim); consolidator should restructure as one canonical program with sub-hypotheses. |
| DX-07 | w14w2c-126 | w14-0073, w14-0167 (token pruning discards rare targets) | Near-clone of w14-0167; note w14-0073 claims the opposite sign — preserve the designed disagreement. |
| DX-08 | w14E-102, w14E-100, w14D2-035, w14D2-058, w14w2c-049 | w14-0063/0135/0139/0141 (annotation-convention family) | Convention-artifact claims re-emerging per territory; admit only members with new mechanisms (w14E-102's per-word convention keying is the sharpest). |

## 4. Mode-collapse risks (5 flags)

1. **JC2-MC-01 — Audit-genre monoculture persists (top unresolved collapse axis).** As in wave1, the overwhelming majority of ideas are diagnose/measure/expose/debunk studies. Constructive contributions (new methods, objectives, task formulations, datasets-as-artifacts) are a small minority — roughly 30 of 638 by one-line reading (e.g., A: a-011 synthetic annealing, a-121/123 DR curricula; D: D2-001, D2-025, D2-112, D2-113, D2-116, D2-124; E: E-032, E-069, E-073, E-098). Wave2 steering fixed territory, not genre. If a wave3 happens, impose an explicit constructive-genre quota; at consolidation, protect the constructive minority from being outcompeted by louder audit claims.
2. **JC2-MC-02 — Forecasting template.** "X is measurable/predictable from Y before/without training" appears in ~162 ideas (A: 37, D: 47 are heaviest). Many are individually good; as a corpus they are one rhetorical machine. Give any future generator the template as a negative constraint.
3. **JC2-MC-03 — Debunk template inside Worker C.** "Gains vanish once the baseline is tuned / compute is matched" recurs across ~20+ C ideas (c-011..c-022, c-069, c-072, c-074, c-076, c-097, c-100) plus w14w2b-121 and w14D2-119. Within-mandate for a contrarian shard, but it is one paper shape repeated across method families; the consolidator should rank by evidential leverage of the target (e.g., c-097 WSSS-decade audit ≫ generic module debunks) and cap the family.
4. **JC2-MC-04 — Theme overcrowding: contamination and calibration.** Contamination/leakage: ~57 wave2 ideas plus an existing canonical family (see CV-09, DX flags). Calibration/confidence: ~87 wave2 mentions plus wave1's 34-idea uncertainty family. Both need explicit caps at consolidation to avoid portfolio skew.
5. **JC2-MC-05 — Anchoring migrated, not removed.** Wave1's SAM anchoring is gone, but Worker B is ~100% diffusion-anchored and Worker E predominantly CLIP-style-contrastive-anchored (by territory design). GAN/autoregressive/flow generators, non-contrastive text-vision models, and DINO-style self-supervised lineages are nearly absent corpus-wide. Portfolio risk: results age with two model families instead of one.

Positive anti-collapse findings, for the record: SAM+X (1 mention), LoRA+X (0), loss+X (~3) — eliminated; 0 duplicate ids; single lexical near-duplicate pair in 203k pairs; per-shard cluster structure genuinely distinct (66 distinct cluster labels).

## 5. Missing territories / research blind spots (10 flags — input for a later generator queue)

1. **JC2-MT-01** — 3D beyond LiDAR-driving: indoor point clouds, meshes, NeRF/Gaussian-splatting segmentation. Zero coverage across both waves.
2. **JC2-MT-02** — Interactive / human-in-the-loop segmentation science: correction economics, interaction protocols, mixed-initiative labeling (wave1 had prompting mechanics; wave2 nearly dropped it — only w14w2c-065/094/101 touch it).
3. **JC2-MT-03** — Constructive-genre quota: architectures, training objectives, task reformulations, benchmark/dataset artifacts with falsifiable design hypotheses (the persistent genre gap of JC2-MC-01, phrased as a territory).
4. **JC2-MT-04** — Embodied / closed-loop perception: dense predictions consumed by planners/trackers, action-conditioned evaluation, utility calibration (only w14D2-021, w14D2-040 touch it).
5. **JC2-MT-05** — Multimodal sensor-fusion dense prediction: RGB-D, thermal, event, multispectral fusion science (only incidental members: w14w2b-113, w14E-117).
6. **JC2-MT-06** — Document / diagram / UI / text-dense imagery dense prediction (only w14E-053/054 touch typography; no layout segmentation science).
7. **JC2-MT-07** — Instance/panoptic task-formulation science and multi-task interference (segmentation × detection × depth cross-talk; only w14D2-002, w14w2c-109 adjacent).
8. **JC2-MT-08** — Continual/lifelong deployment adaptation: drift trajectories exist in A (a-058/077/078/130) but no continual-learning science (rehearsal, plasticity, forgetting under deployment schedules) beyond wave1's TTA cluster.
9. **JC2-MT-09** — Theory and formal analysis of dense prediction: sample complexity, invariance theory, generalization bounds under spatial correlation (only w14w2a-125/127, w14w2c-009).
10. **JC2-MT-10** — Human perception & annotation science as a measurement instrument: psychophysics of boundary perception, rater modeling beyond convention artifacts (w14w2c-112, w14E-100 incidental).

## 6. QA issues for the consolidator (3 flags)

1. **JC2-QA-01 — Inconsistent `id_seed` schemes, with a provenance hazard.** Three conventions across five shards: `w14w2a-###`/`w14w2b-###`/`w14w2c-###` vs `w14D2-###` vs `w14E-###`. `w14E-###` visually parallels wave1's shard scheme (`w14A-###`), inviting provenance confusion even though no actual collision exists (wave1 canonical ids are `w14-####`). Normalize at merge; preserve original ids in a provenance field, as wave1 did.
2. **JC2-QA-02 — Unverified absence-as-fact phrasing.** 27 ideas state "has never been / nobody has / no one has" as fact, mostly in the `problem` field (heaviest: Worker D with 12, Worker E with 8; full id list in the flags file — e.g., w14D2-109, w14E-105, w14w2a-098). Six more one-lines assert absence-of-practice as fact ("nobody uses/collects/ships/benchmarks": w14D2-077, w14D2-123, w14D2-124, w14E-020, w14E-032, w14E-119), and 17 `why_possibly_novel` fields make absolute absence claims without hedging (list in flags file). None of these were literature-verified; the consolidator must downgrade all of them to "not verified against prior work" and must not propagate them into `ideas_master.jsonl` as fact. (Most shards' `why_possibly_novel` fields are otherwise well-hedged — "appears missing/unstudied" — and Worker B/C often prefix "HYPOTHESIS, unverified", which is the right pattern.)
3. **JC2-QA-03 — Uniform `evidence_status: HYPOTHESIS` (638/638).** Correct and honest; the consolidator must not infer any evidence gradient from this field — ranking must come from judge flags.

## Counts

- Ideas reviewed: 638 (A:133, B:126, C:130, D:124, E:125)
- High-value flags: **45** (9 per shard)
- Collapse-related flags: **25** (12 wave2 cross-shard convergence + 8 wave1-canonical overlap + 5 mode-collapse risks)
- Missing-territory flags: 10
- QA flags: 3
- Total flag records in `judge_C.flags.jsonl`: **83**

## Recommended next task

`p1_wave2_consolidator` — merge the five wave2 shards into the canonical state, reconciling Judge A/B/C flags; deduplicate the 12 wave2 convergence families AND the 8 canonical-overlap families against `ideas_master.jsonl`; normalize id schemes with provenance; downgrade all unverified-absence phrasing; cap contamination and calibration themes; protect the constructive-genre minority; and carry the 10 missing territories into any wave3 generator queue.
