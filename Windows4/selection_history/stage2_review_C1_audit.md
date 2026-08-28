# Stage 2 Review — Batch C1 + Meta-Audit

Role: Meta-Reviewer / Auditor + Reviewer. One pass, no web. 2026-08-28.
Inputs: `stage1_C1.md` (branch `cursor/stage1-c1-idea-catalog-209b`), S/A1/B1 catalogs, rubric, literature anchors.
Method: rubric decision rules (not mean score). Novelty / Significance on 1–5. All prior-work claims below are
**memory-based HYPOTHESES for Stage 3 to verify** — no web was used; no fabricated citations, only papers I
believe are real, and each must be confirmed or discarded in Stage 3.

Epistemic status of this file: REVIEW JUDGMENT (opinions + memory-based prior-work flags). No experimental results.

---

## C1 Keep (exactly 50 of 120)

Kept = survives kill rules and earns a slot under the 50-cap. "(absorbs X)" = X is killed as a standalone row but
lives on as an arm/section of the kept idea. Protect = shielded from mean-score death in later stages (15 total).

| ID | reason | Novelty | Significance | Protect? |
|---|---|---|---|---|
| C1-001 | SA-1B↔benchmark dedup audit: if overlap exists every zero-shot SAM number is tainted; eval-only, kills-or-dies in days | 4 | 5 | YES |
| C1-003 | Sim-click optimism bounds all NoC results; merge with A1-105/S-016 into one human-click study (×3 convergence = dedup, not triple credit) | 3 | 4 | no |
| C1-006 | J&F may mostly measure oracle frame-1 init; regression on released predictions, zero training | 3 | 4 | no |
| C1-007 | Benchmark lineage graph + cross-lineage transfer matrix; reusable artifact even if gains transfer | 4 | 3 | no |
| C1-012 | Pinned-checkpoint re-eval; version drift plausibly reorders methods given SAM/HQ/Efficient/SAM2 proliferation | 3 | 3 | no |
| C1-013 | Metric itself is known (Boundary IoU, Cheng et al.); kept ONLY as pre-registered PEFT rank-flip test and as tooling for other keeps — demoted from C1's Protect | 2 | 4 | no |
| C1-016 | If method gaps sit inside the annotator noise floor, leaderboard progress is illusory; run on COCO/ADE where (unlike medical) the floor is unpublished | 3 | 5 | YES |
| C1-017 | Per-class regression counts make "adaptation hurts" auditable; cheap; feeds C1-110 | 3 | 3 | no |
| C1-021 | ECE-vs-mIoU scatter on 10 public ckpts; the 1-day gate for the whole calibration thread | 2 | 3 | no |
| C1-025 | PEFT-vs-full-FT calibration at matched mIoU; canonical for the FT-calibration-tax thread (merge S-318/S-650) | 3 | 4 | no |
| C1-026 | IoU-head OOD reliability audit; canonical of a ×4-convergent thread (A1-006/S-298/S-361); pair with constructive twin A1-006 | 3 | 4 | YES |
| C1-031 | FT desyncs confidence head from mask head (absorbs C1-069); fresh, cheap to track, safety-relevant | 4 | 4 | YES |
| C1-032 | Focal-vs-CE calibration *reversal* on dense output — a divergence-from-classification hypothesis, not a port | 3 | 3 | no |
| C1-036 | Multimask variance as free aleatoric UQ; must difference vs FNPC 2023 (prompt-perturbation UQ is taken); pairs with C1-061 | 3 | 4 | YES |
| C1-037 | Robustness cost of PEFT; C1-048 matched-budget control folded in as mandatory arm (absorbs C1-043, C1-048) | 4 | 4 | YES |
| C1-038 | ANOVA clicks×checkpoints: if prompt variance > model variance, leaderboards are noise (merge A1-048/A1-094/S-001) | 3 | 4 | no |
| C1-039 | Resolution as the dominant unbenchmarked robustness axis (absorbs C1-091 inverted-U; merge A1-008/A1-013/B1-104) | 3 | 4 | no |
| C1-042 | Annotation-style shift (polygon vs pixel) as an eval axis; pairs A1-043/A1-119; must show it is not ordinary domain shift | 3 | 3 | no |
| C1-049 | LoRA rank scales with output resolution, not data size — a PEFT-science scaling claim, cheap grid | 3 | 3 | no |
| C1-053 | LR-swept full FT vs published seg-PEFT gains; the portfolio's baseline-honesty anchor (absorbs C1-005 honest-val arm) | 3 | 5 | YES |
| C1-054 | Encoder/decoder × domain/task-shift 2×2 (absorbs C1-051, C1-072; BitFit detail deferred to A1-112) | 3 | 3 | no |
| C1-055 | LN-only baseline missing from seg-PEFT literature; cheap, high kill-power; cls-side LN-tuning prior must be differenced | 3 | 4 | no |
| C1-057 | PEFT-vs-full-FT data-size crossover; the regime chart practitioners need (merge S-146, B1-086) | 3 | 4 | YES |
| C1-060 | Seed variance vs claimed method gaps; cheap audit that arms A1-106's instability law | 2 | 4 | no |
| C1-061 | FT collapses multimask proposal diversity = "ambiguity forgetting"; fresh, SAM-specific, cheap | 4 | 4 | YES |
| C1-062 | Layer-resolved forgetting via cross-attn re-splicing; one of the only mechanism ideas in C1 | 4 | 3 | no |
| C1-064 | Minimal replay dose curve for decoder retention; practical and cheap; CL-cls replay prior differenced by promptable-decoder setting | 3 | 4 | no |
| C1-065 | Umbrella behavioral-forgetting battery per prompt type (absorbs C1-063 click-depth, C1-071 negative-click, C1-074 cross-modal; merge A1-109) | 3 | 4 | YES |
| C1-066 | LoRA-forgets-too matched retention test; MUST difference vs the LLM-side "LoRA learns less, forgets less" result | 3 | 4 | no |
| C1-067 | CKA drift as predictive early-warning for zero-shot loss (merge A1-108, B1-114; absorbs C1-096); template-echo flagged below | 3 | 4 | no |
| C1-073 | Feature-space domain gap predicts retention loss — a predictive law, not an anecdote; template-echo flagged below | 3 | 4 | YES |
| C1-076 | Retention differences may be an LR artifact — strongest single confound attack in the batch; adversarial to C1-066/PEFT-retention claims | 4 | 4 | YES |
| C1-082 | Threshold-artifact check gates EVERY forgetting claim including ours; near-zero cost; run first in the Forget thread | 3 | 4 | YES |
| C1-084 | Entropy-min TTA vs prompt-following; adversarial pair with A1-087 (which predicts the opposite) — one of them dies | 3 | 3 | no |
| C1-085 | Probe-vs-FT gap stratified to boundaries/thin structures; decides when tuning is needed at all (pairs B1-037) | 3 | 4 | no |
| C1-087 | Backbone-scale non-monotonicity under small-n FT (merge S-286, S-052 curve, S-608) | 3 | 4 | no |
| C1-088 | SAM-as-label-engine quality audit vs experts; huge blast radius across pseudo-label pipelines | 3 | 4 | no |
| C1-094 | Text-side vs vision-side LoRA at matched params; the only open-vocab keep — deliberate anti-SAM-echo diversity slot | 3 | 3 | no |
| C1-095 | Cross-site method-rank correlation; attacks deployment validity of single-site validation | 3 | 4 | no |
| C1-097 | Unified PEFT-for-SAM replication vs tuned decoder-only baseline; flagship audit (absorbs C1-005, C1-009 protocol arms) | 3 | 5 | YES |
| C1-105 | Distilled SAMs lose multi-click refinement; eval-only NoC curves on deployed checkpoints (merge S-135) | 3 | 4 | no |
| C1-108 | Multi-task co-training calibration tax; adversarial pair with S-550 (predicts the opposite) | 3 | 3 | no |
| C1-109 | Certified click-stability via smoothing over prompt space — new formulation; certified-seg prior smooths pixels, not prompts; vacuous-radius risk accepted | 4 | 3 | no |
| C1-110 | Gain-retention benchmark suite; portfolio capstone (absorbs C1-083 frontier, C1-117 model cards; C1-068 interpolation demoted to a baseline arm here) | 3 | 5 | YES |
| C1-111 | Annotator-seconds effort model to replace NoC (absorbs C1-015); log availability is the real risk | 3 | 4 | no |
| C1-113 | Label-schema shift as a formal task; constructive twin B1-012 | 4 | 3 | no |
| C1-114 | Region-level selective segmentation (absorbs C1-034); simple-baselines-strong risk noted | 3 | 3 | no |
| C1-115 | Oracle-free auto-prompt eval protocol; enables honest promptable leaderboards (merge S-060, S-200) | 3 | 4 | no |
| C1-116 | Prompt portability as formal task spec (absorbs C1-092; merge B1-095 transfer matrix) | 3 | 3 | no |
| C1-118 | Class unlearning in dense decoders with probe-leakage metric; unlearning literature is hot, dense gap looks real | 4 | 3 | no |

Protect count: 15 (001, 016, 026, 031, 036, 037, 053, 057, 061, 065, 073, 076, 082, 097, 110).
Changes vs C1's own protect list: demoted C1-003 (merged), C1-013 (metric is known — only the flip is the finding),
C1-068 (WiSE-FT port → baseline arm of C1-110); promoted C1-031, C1-065, C1-076, C1-082.

### Killed — notable causes (70 killed; grouped, not exhaustive)

- **Folded into a keep (alive as arms):** 005→097/053, 009→097, 015→111, 034→114, 043→037, 048→037, 051→054,
  063/071/074→065, 069→031, 072→054, 083→110, 091→039, 092→116, 096→067, 117→110.
- **Dup of a better twin in another batch (defer):** 040 (A1-015/A1-083 generalize), 050/052 (A1-107 maps
  placement→error type), 058 (A1-092 is the informative direction), 090 (B1-026/031 constructive), 014 (S-198
  already marked Known), 086 (S-287/S-353).
- **Memory-based prior-work kill (Stage 3 must confirm):** 002 (concept-frequency vs zero-shot exists for
  cls/retrieval — Udandarao et al.-type), 011/093 (template/loss duels well-trodden), 018 (PQ=RQ×SQ by definition),
  019 (TIDE-style error decomposition), 023 (NSD is standard), 028 (boundary-concentrated uncertainty is
  Bayesian-seg folklore), 029 (Ovadia et al. 2019 for cls, admitted mirror), 030 (FNPC 2023 — in our own anchors),
  080 (task arithmetic known, outcome admitted expected), 098 (max-prob baseline hard to beat — known),
  099 (replay dominance known in CL-cls), 100 (attention-is-not-explanation genre), 102 (MetricsReloaded covers
  empty-mask handling), 106 (DAFormer-era baselines), 107 (correspondence comparisons exist), 112 (GED /
  Probabilistic U-Net multi-rater eval), 119 (SAMPOT — in our own anchors).
- **Low ceiling / hygiene-not-paper / vague:** 004, 008, 010, 020, 022, 024, 027, 033, 035, 041, 044, 045, 046,
  047, 056, 059, 070, 075, 077, 078, 079, 081, 089, 101, 103, 104, 120.

---

## Audit

### Echo chamber risks

- **Eval-vs-methods imbalance is real and structural (S-720 confirmed).** ~96/120 of C1 are audit / negative /
  assumption-check ideas; the S-catalog's biggest clusters are EVAL_LEAK, ASSUMPTION, NEG_RESULT; the rubric's
  "who is wrong if we are right?" dimension rewards accusation-shaped ideas. Even after my cull, ~38/50 keeps are
  audits. An all-audit portfolio has *correlated* failure: if effect sizes are small, everything nulls at once,
  and CVPR-class venues rarely take pure audits without either a flipped leaderboard or a constructive protocol.
  Mitigation: every kept audit should name its constructive twin (e.g., C1-026↔A1-006, C1-003↔A1-105 protocol,
  C1-115's auto-prompt protocol), and Stage 3 should carry ≥30% method/mechanism ideas — which currently live
  almost entirely in A1 (see revive list).
- **Cross-batch convergence is being mistaken for independent validation.** The same hypotheses recur:
  prompt-jitter UQ ×4 (C1-030/C1-036/A1-098/S-011 — with FNPC 2023 as known prior), human-vs-sim clicks ×3
  (C1-003/A1-105/S-016), resolution/scale ×5 (C1-039/C1-091/A1-008/A1-013/B1-104), IoU-head calibration ×4
  (C1-026/A1-006/S-298/S-361), PEFT crossover-n ×3 (C1-057/S-146/B1-086), seed variance ×3 (C1-060/A1-106/S-203),
  "feature-distance predicts outcome" template ×5 (C1-073/C1-067/A1-082/B1-039/B1-065). All generators shared the
  same seed catalog and anchors, so convergence is correlated, not independent evidence of importance. Rule:
  dedup before Stage 3, and treat convergence as *elevated* prior-work risk — if four of our agents derived it
  from the same memes, the field likely already did too.
- **SAM-centrism / single-model risk.** >80% of the pool presupposes SAM/SAM2 as the object of study. Findings may
  not survive the next checkpoint family, and audits go stale fastest. Mitigation: kept audits must run on ≥2
  model families where feasible (e.g., SAM + an open-vocab or DINOv2-probe pipeline); C1-094 kept partly as a
  deliberate non-SAM slot; B1's annotation-efficiency cluster is the least SAM-echoed asset in the pool — weight
  it up in cross-batch selection.
- **Claim-template echo ("X was never measured").** Our house style is the unmeasured-claim; several were in fact
  measured (FNPC, SAMPOT, MetricsReloaded, Boundary IoU, GED, task arithmetic, Ovadia et al., LLM LoRA-forgetting).
  The echo chamber is not just topical (SAM) but rhetorical: Stage 3 must attack "never audited" claims hardest,
  starting from our own anchors file, which already refutes two C1 ideas (C1-030, C1-119).
- **Rubric Goodharting / kill-culture overshoot.** "Default: already done" + "default: reject" plus protect-tags
  concentrated on contrarian negatives risks a portfolio that can only subtract. Calibration alone has ~20 ideas
  across batches for a niche readership — I kept 6 and capped the thread with a single 1-day gate (C1-021).
  Forgetting/retention now spans ~14 keeps+revives; C1-082 (threshold artifact) and C1-076 (LR confound) are
  protected precisely because they can kill *our own* thread before reviewers do.

### Revive from S / A1 (10) — killed-looking or unprotected, revived to counter the eval bias

None of these appear on the S/A1 protect lists; each risks mean-score or "known/crowded"-tag death. Mostly
constructive/mechanism ideas, which is what the portfolio lacks.

1. **A1-033** — learned 1×1-conv channel lifting for grayscale modalities: tiny constructive method attacking the ignored pseudo-RGB interface; clean LoRA comparison at 0.1% params.
2. **A1-035** — atlas-registered anatomical boxes as human-free SAM prompts: classical registration + promptable FM, no detector training; pairs with the auto-prompt eval C1-115.
3. **A1-043** — fine-tuned SAM overfits annotator boundary conventions, not anatomy: reframes cross-hospital "domain shift" as label-convention shift; high clinical significance.
4. **A1-060** — depth-edge auto-prompts for transparent objects: constructive chaining of two frozen models where each alone fails.
5. **A1-072** — SAM everything-mode as long-tail proposal engine vs RPN recall on LVIS-rare: constructive detection use; Stage 3 must check SAM-proposal-for-OVD prior.
6. **A1-091** — prompt-distribution shift as a distinct measurable axis: the formulation that makes C1-003/C1-038 a research program rather than one audit.
7. **A1-101** — prompt-embedding norm scaling steers part/whole granularity: latent control-knob discovery in a frozen model; mechanism-flavored, cheap.
8. **S-042** — the 3D medical gap is anisotropy, not "medical": confound-first causal claim; one resampling experiment could deflate a whole subfield's framing.
9. **S-045** — intensity windowing is a hidden hyperparameter as large as prompt type: tagged "known to clinicians" (would die by insider-rule), but *quantifying* it is load-bearing for every MedSAM comparison — keep as a mandatory reporting arm, not a standalone paper.
10. **S-064** — meta-analysis: MedSAM-FT gains track #FT-images, not method: cheapest highest-blast-radius audit in the S-catalog; only needs published tables.

### False-novelty patterns to ban in Stage 3

1. **Folklore-as-novelty.** "Nobody measured X" where X is insider knowledge (slice-level leakage, windowing, Dice-is-a-size-metric). Test: would an nnU-Net/MetricsReloaded author consider this news? If no — kill or demote to a reporting arm.
2. **Cls→seg ports without a divergence mechanism.** "Known for classification, untested for segmentation" is not novelty (C1-029-style). Admissible only when the hypothesis *predicts a different outcome* on dense output and says why (C1-032 is the model).
3. **Prompt-perturbation amnesia.** Any prompt-jitter/uncertainty/prompt-search idea must explicitly difference itself from FNPC 2023 and SAMPOT — both are in our own anchors and still slipped into C1 twice (C1-030, C1-119).
4. **Hygiene-audit-as-paper.** Norm-stats swaps, fixed-TTA re-runs, checkpoint pinning are paragraphs, not papers, unless a pre-registered rank flip is demonstrated; otherwise fold into a protocol suite (C1-097/C1-110).
5. **Weight-arithmetic ports.** WiSE-FT interpolation, task-vector negation, LoRA merging are established; a dense/promptable application needs a decoder-specific hypothesis (e.g., C1-061's diversity collapse), not "first time on SAM".
6. **Metric-substitution novelty.** Boundary-F/clDice/NSD/PQ/GED already exist; the metric is never the contribution — only a discovered, pre-registered ranking inversion is.
7. **Convergent-duplicate double counting.** The same hypothesis surfacing in S, A1, B1, C1 must enter Stage 3 exactly once, with its duplicates listed — and with prior-work suspicion *raised*, not lowered, by the convergence.
8. **Strawman assumptions.** "The field assumes X" requires citing at least one real paper whose claims depend on X; unattributed assumptions are unfalsifiable rhetoric.
9. **Renamed-axis novelty.** Declaring a new shift type (annotation-style, prompt-distribution, schema shift) requires showing it is not subsumed by ordinary domain-shift measures — orthogonality is part of the burden of proof.

### Handoff to Stage 3

- Attack order: protected keeps first (they anchor the portfolio), then the ×N-convergent threads (highest hidden-prior risk).
- Verify every memory-based prior flagged above; where partial overlap is found, **mutate, do not auto-kill** (rubric rule).
- Enforce the ≥30% constructive/mechanism quota using the revive list plus A1's protect set.
