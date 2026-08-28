# Stage 2 — Batch B Elimination Record (265 of 340 killed)

**PI:** Windows5
**Stage:** 2 (selection: 340 → 75 survivors)
**Companion files:** `stage2_batch_B_scores.md` (per-idea scores and reasons), `stage2_batch_B_survivors.md` (75 survivors)

265 ideas were eliminated: 250 under nine kill codes, 15 as almost-survived (§3). Per-idea reasons are in the scores sheet; this file records the policy, the eliminated clusters, and the near misses.

---

## 1. Selection policy (how protection overrode the mean)

Ranking by mean score alone would have flooded the survivor list with safe, well-scoped audit studies and killed every expensive bet. Instead:

- **HRHR (high-risk / high-reward):** kept when Risk ≥ 4 *and* Upside ≥ 4–5, if failure is informative and no cheaper instrument answers the same question. Ten survivors carry this flag (0009, 0019, 0075, 0078, 0159, 0162, 0185, 0294, 0318, 0329). HRHR did **not** save 0177 (needs a wet lab), 0204 (null unfalsifiable), or 0328 (theory likely vacuous at realistic priors) — protection requires that a failed bet still teach something.
- **CI (simple counter-intuitive):** one experiment can overturn a default (0136, 0200, 0272, 0285, 0288, 0306, 0310, 0315, 0338 …). Protected because these are cheap and, if confirmed, immediately redirect practice.
- **DM (disagreement magnet):** results reviewers/communities will split over (0012, 0064, 0089, 0108, 0114, 0186, 0226, 0233, 0248, 0329 …). Protected because contested results move fields.
- **CF (cheap-to-falsify):** dies fast on frozen models/public checkpoints (0017, 0037, 0082, 0083, 0084, 0104, 0120, 0269, 0282, 0305, 0337 …). Protected because kill-fast experiments are the highest-ROI use of early program time.

Per the task brief, two patterns were killed on sight: **module-stacking / engineering-first proposals** (K1-ENG, 35 kills — the question was secondary to a deliverable) and **"apply to medical/domain X" without a scientific question** (K6-PORT, 12 kills).

---

## 2. Eliminated clusters (organized by kill code)

### K3-DUP — subsumed by a stronger sibling (50 kills)
The largest bucket. Batch B is thread-rich: many ideas restate one question at different sharpness. Policy: keep the sharpest formulation, kill the rest, and record the anchor. Representative consolidations:

| Thread | Killed | Survives in |
|---|---|---|
| Soft/continuous supervision semantics | 0008, 0025, 0099, 0296 | 0310 (confidence inversion), 0318 (density fields) |
| PU / closed-world auto-labeling statistics | 0007, 0034 | 0320 |
| Prompt-distribution realism | 0004, 0044, 0292, 0317 | 0089, 0193, 0279 |
| Positional/resolution geometry artifacts | 0056, 0125\*, 0299 | 0305 (plus 0122) |
| Placement-from-diagnosis (PEFT) | 0047, 0247, 0264 | 0253 |
| Retention/transfer geometry of adapters | 0050, 0065, 0254 | 0248, 0251, 0260 |
| Generation-vs-selection decomposition | 0093, 0283 | 0269 |
| Uncertainty validity (conformal/coverage) | 0092, 0102, 0013 | 0082, 0120, 0337 |
| Contamination auditing | 0086 | 0294 |
| Color-as-shortcut | 0287 | 0136 |
| Restoration/SR preprocessing skepticism | 0243, 0295, 0333 | 0331, 0338 |
| Interface coupling (detector→segmenter) | 0071, 0103 | 0217 |
| Distance-predicts-gain | 0147, 0293 | 0054 |
| Structured-synthetic-noise reliance | 0206, 0166\* | 0189 (0166 near-dup of three survivors) |
| Click-response pathology | 0153, 0281 | 0282, 0128 |
| Decoder/pretraining value localization | 0289 | 0129 |
| Shortcut-blocking prompts | 0028, 0303 | none — the pair died together: injected-correlation designs create synthetic shortcuts whose realism caps the paradigm claim |

\*0125 and 0166 are also listed among almost-survived / near misses in the scores sheet.

### K2-THIN — likely conclusion already believed, or consequence small (46 kills)
Audit and hygiene studies whose most probable outcome changes few decisions: 0018, 0022, 0029, 0039, 0040, 0046, 0052, 0060, 0069, 0077, 0087, 0091, 0094, 0096, 0105, 0106, 0107, 0113, 0116, 0117, 0118, 0121, 0135, 0138, 0144, 0145, 0150, 0192, 0194, 0213, 0222, 0224, 0225, 0231, 0232, 0234, 0237, 0249, 0252, 0263, 0267, 0275, 0301, 0326, and the near misses 0031, 0090-adjacent items. These are competent studies; Stage 2 exists to spend slots on questions whose answers surprise someone.

### K9-SIZE — effect below noise, non-exportable, or mechanism won't separate (42 kills)
Ideas whose predicted effect is plausibly real but likely too small, too confounded, or too local to carry a paper's claim: 0002, 0011, 0015, 0020, 0023, 0030, 0036\*, 0066, 0133, 0137, 0139, 0140, 0146, 0151, 0152, 0154, 0155, 0161, 0175, 0183, 0187, 0188, 0198, 0204, 0205, 0208, 0209, 0221, 0250, 0259, 0271, 0278, 0284, 0291, 0297, 0298, 0319, 0323, 0328, 0330, 0332, and kin. Common failure shapes: the confound is the same size as the effect (0133's off-manifold stimuli, 0161's registration error); the number won't export across datasets (0002, 0030, 0284); the components won't dissociate (0146, 0187, 0188).

### K1-ENG — engineering-first: module/method/tool, question secondary (35 kills)
The module-stacking bucket the brief demanded: 0005, 0021, 0026, 0038, 0073, 0085, 0131, 0141, 0167, 0179, 0196, 0199, 0211, 0212, 0238, 0242, 0245, 0256, 0261, 0266, 0268, 0273, 0274, 0276, 0277, 0280, 0290, 0316, 0321, 0322, 0324, 0325, 0327, 0339, and the near miss 0098. Several are likely to *work* (0245, 0266, 0316); they died because their success would be a deliverable, not an answer.

### K4-DATA — blocked by data, metadata, or institutional access (32 kills)
Public resources cannot supply the required instrument: annotator IDs/timestamps (0016, 0035), paired or rigged captures (0045, 0048, 0049, 0061, 0157, 0158, 0165, 0169, 0171, 0172, 0178), rich multi-rater sets (0027, 0115), clinician logging (0070 — also K7), amodal/layered GT (0134), replication partners (0097), long-duration labeled logs (0236, 0239, 0244, 0309), real confuser/artifact sets (0201, 0202), subgroup labels (0195), user logs (0258), matched control models (0307). Many are good ideas for a lab with the right partnerships; this program does not have them at Stage 2.

### K5-CMP — compute/scale disproportionate to the claim (20 kills)
Factorial pretraining or many-run designs whose grids outrun the claim's value: 0043, 0051, 0058, 0063, 0074, 0076, 0109, 0142, 0160, 0168, 0180, 0197, 0207, 0214, 0215, 0255, 0262, 0302, 0312, 0335, 0340.

### K6-PORT — domain transplant without a scientific question (12 kills)
"Apply X to domain Y" where the payoff is engineering: 0036, 0062, 0079, 0100, 0123, 0127, 0176, 0203, 0210, 0216, 0228, 0265.

### K7-HUM — human-subject cost exceeds generalizable yield at this stage (8 kills)
0101, 0111, 0170, 0173, 0181, 0334, plus 0070 (with K4) and 0326's clinical arm. Note the program *kept* the two human studies whose yield is foundational and amortized (0019 anchoring, 0089/0193 shared prompt-log collection).

### K8-DATE — finding dates with model versions (6 kills)
0149, 0229, 0235, 0240, 0314, 0336. Methodology survives, numbers do not; snapshot papers of current-model weakness were deprioritized.

---

## 3. The 15 almost-survived

Ranked roughly by how close the call was. Each would be a defensible swap for the weakest survivor in its cluster; Stage 3 may resurrect any of them.

1. **IDEA-B-0033 — Tail OV failure is linguistic, not visual.** The cheapest clean causal probe in Cluster 1 (name-substitution intervention). Lost its slot to 0124, which makes the same text-space argument with a sharper geometric bound. Resurrect if 0124's anchor-substitution design hits trouble.
2. **IDEA-B-0286 — Subgroup regression under fine-tuning.** Exactly the right clinical question ("who drops below zero-shot when the average improves?"), but the core mechanism — fine-tuning trades pretrained robustness, weight interpolation recovers it — is substantially documented for classification, and subgroup metadata caps audit resolution. Would survive in a batch with weaker Cluster 9 competition.
3. **IDEA-B-0081 — Which mask metric predicts downstream clinical measurement error.** Foundational and cheap, but conclusions must be stratified per clinical task, weakening the headline. A strong candidate to fold into 0082/0083's evaluation program rather than run alone.
4. **IDEA-B-0112 — Intervention tests for aleatoric/epistemic disentanglement claims.** A real falsification standard; lost to 0120/0337, which test uncertainty validity where the practice is most widespread. Its intervention methodology should be inherited by both survivors.
5. **IDEA-B-0311 — Seeds as annotation auditors.** Nearly free and clever; died because cross-seed disagreement plausibly concentrates on genuine ambiguity (where "error" is undefined) and 0082 owns the label-noise instrument slot. Worth a weekend pilot inside 0082's infrastructure.
6. **IDEA-B-0125 — Center bias of prompted quality.** Cheap and real, but border/padding artifacts must first be separated from positional-embedding effects; 0305 covers adjacent ground with a sharper mechanism. Fold its position-stratified metrics into 0305's protocol.
7. **IDEA-B-0308 — Pure-noise negatives as an FP suppressor.** The absence-mode-calibration mechanism is genuinely clarifying, but loss-normalization artifacts are a live rival explanation, and 0017/0182 already carry the negatives thread. A one-ablation add-on to 0182.
8. **IDEA-B-0246 — The intrinsic rank of a domain shift.** Principled (turn the most-tuned PEFT knob into a pre-training measurement), but knee points are optimizer-dependent and 0306's inversion of the same knob is more surprising per unit compute. Its spectral predictor should be tested inside 0306's grid.
9. **IDEA-B-0090 — Size-stratified re-ranking of public checkpoints.** Very cheap, but the interesting version of the claim is 0288's scaling crossing; 0090 alone is a table, 0288 is a law. Run 0090's evaluation pass as 0288's first milestone.
10. **IDEA-B-0010 — Prompt-type supervision asymmetry (box→point vs point→box).** Cheap and default-setting, but narrow next to 0269/0193, which own the interaction-channel slots. Resurrect as a controlled sub-experiment of 0193.
11. **IDEA-B-0300 — Objectness erosion from continued SSL.** A real recipe conflict at the intersection of two major practices; died on instrument softness (grouping probes unsettled, masking-ratio dependence). If a robust grouping probe emerges from 0129/0132's work, rerun this.
12. **IDEA-B-0313 — Random features, real boundaries.** Strategic cartography of where pretraining pays, but decoder-capacity matching can manufacture either answer; 0129's oracle-probe decomposition is the cleaner cut at the same question.
13. **IDEA-B-0148 — Do learned upsamplers hallucinate boundary micro-geometry?** Important safety-adjacent question (relates to 0331), but distinguishing hallucination from legitimate noise sensitivity needs repeat-acquisition data that is hard to source. Revisit if such data surfaces.
14. **IDEA-B-0227 — Marginal FP-reduction value per hard-negative category.** Highly actionable for dataset builders, but category value interacts with positive-set composition, needing a joint design that outgrew its slot. 0017/0110/0241's negative-curation work will generate its data as a byproduct.
15. **IDEA-B-0177 — Restain-and-register IHC as molecular ground truth for H&E.** The highest-upside supervision idea in Cluster 5 (HRHR-flagged), killed only by the wet-lab requirement and the tissue-alteration confound. If a pathology partnership materializes, this jumps straight back into the program.

---

## 4. Bookkeeping

- Killed: 265 (250 coded + 15 almost-survived). Survivors: 75. Total: 340, no gaps.
- Kill-code counts: K3-DUP 50 · K2-THIN 46 · K9-SIZE 42 · K1-ENG 35 · K4-DATA 32 · K5-CMP 20 · K6-PORT 12 · K7-HUM 8 · K8-DATE 6 (a few rows carry two codes; per-idea reasons in the scores sheet are authoritative).
- Every K3-DUP kill names its surviving anchor; no thread was killed end-to-end without a recorded reason (the one deliberate exception: 0028/0303, whose shared design flaw is recorded on both rows).
