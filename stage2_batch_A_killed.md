# Stage 2 — Batch A Killed Report

**Reviewer:** Independent Stage 2 Reviewer · **Scope:** IDEA-A-0001…0340 · **Killed:** 267 of 340 (78.5%)

This file summarizes what was eliminated and why. Full per-idea scores and one-line kill reasons are in `stage2_batch_A_scores.md`. Nothing here was killed for being risky — high-risk/high-reward, counter-intuitive, disagreement-magnet, and cheap-to-falsify ideas were actively protected. Ideas died for redundancy with a stronger sibling, for their core claim already existing in the literature, for compute/data/recruitment costs disproportionate to the verdict, or for having an engineering payload rather than a scientific question.

---

## Per-cluster elimination summary

**Cluster 1 — SAM/SAM2 Failure Modes (killed 23/30).** The cluster over-generated documentation-grade failure catalogs. Kills were dominated by (a) "measure a known weakness" entries with no mechanism claim (0004, 0010, 0018, 0026), (b) engineering-guidance maps useful for practitioners but not publishable science (0008, 0022, 0047), and (c) narrow convention documentation (0025). The seven survivors carry the mechanistic and counter-intuitive core (memory-vs-single-frame paradox 0001, density-blindness 0003, thin-structure law 0006, ambiguity-head science 0007/0013).

**Cluster 2 — Prompt Sensitivity (killed 16/20).** Prompt-perturbation phenomenology was heavily redundant: many entries were instances of "prompts change outputs, measure it." Companion experiments were folded into the strongest program (0032 into 0031); scale-ladder studies died on missing dense model ladders (0045). Survivors keep the falsifiable structure: order-sensitivity 0031, prompt-ensembling-as-uncertainty 0033, the text-prompt lottery 0041, spatial-linguistic dissociation 0049.

**Cluster 3 — PEFT & Fine-Tuning Instability (killed 21/25).** The forbidden-category filter hit hardest here: several entries reduced to PEFT-variant comparisons (adapter-vs-LoRA horse races) — method shootouts without a question. Compute-heavy decompositions (0052's 480-run bias-variance grid) and NLP-precedented transfers (0051's intrinsic-dimension rank prediction) also died. Survivors are the instability-mechanism core: seed-lottery 0055, loss-landscape asymmetry 0058, rank-collapse dynamics 0067, calibration-preservation mechanism 0072.

**Cluster 4 — Catastrophic Forgetting (killed 12/15).** Monitoring-note-scale observations (0081 boundary-before-region decay), fragile curvature estimation at foundation scale (0083), and recipe-grade mitigations (0071 EMA averaging, 0079 replay fractions) were cut. Survivors: forgetting-geometry 0076, the frozen-encoder counterfactual 0078, cross-architecture forgetting universality 0089.

**Cluster 5 — Medical Segmentation Limits (killed 24/30).** The "apply X to medical" filter killed several entries whose only novelty was the clinical domain. Recruitment-gated studies (0092 clinician prompts, 0104 time-normalized AL), partially published findings (0096 size-stratified sensitivity, 0108 leakage audits), and pipeline-entangled audits (0111 isotropic resampling) also died. Survivors carry genuine clinical-scientific questions: label-noise ceiling 0091, modality-collapse 0093, inter-rater floor as target 0097/0103, shortcut anatomy 0100, aggregate-metric deception 0118.

**Cluster 6 — Smoke & Fire (killed 14/20).** Application-flavored duplicates (alarm-pipeline variants, sensor-fusion engineering) died; the surviving six form a coherent program: density ground truth 0121/0122, temporal-signature necessity 0123, the false-alarm anatomy 0125/0126, and the benchmark-realism audit 0128.

**Cluster 7 — Transparent/Mirror/Ambiguous (killed 16/20).** Per-material catalog entries and RGB-D fusion engineering died. Survivors keep the physics-vs-shortcut dissociations: transparency-cue ablation 0141, mirror-detection mechanism 0142, polarization value quantification 0154, the glass-boundary information floor 0157.

**Cluster 8 — Small Objects & Boundary Quality (killed 15/20).** Metric-variant proposals and architecture-remedy comparisons without compute matching died; 0164's oracle-magnification decomposition lost to the stronger 0161+0313 pair; 0179's expert-analyst human floor was priced out by recruitment. Survivors: GSD-ladder science 0161, boundary-metric deception 0166, annotation-noise-vs-model-error at boundaries 0170/0174, tiling artifacts 0176.

**Cluster 9 — VLMs for Dense Prediction (killed 15/20).** "Benchmark a VLM on segmentation" entries with no hypothesis died, as did guardrail engineering (0200 superclass fallback). Survivors carry dissociations and audits: spatial-language blindness 0181, counting-vs-locating 0183, referring-expression shortcut 0185, hallucinated-grounding asymmetry 0187, contamination audit 0199.

**Cluster 10 — Foundation-Model Representations (killed 19/25).** Costly pretraining-grid studies (0201 curation, 0213 resolution debt) and racing-literature entries (0218 emergence-artifact replication) died. Survivors anchor the representational science: task×backbone matrix 0202, dense-vs-global information geometry 0203, register-token pathology 0207, frequency-bias law 0211, texture-vs-shape allegiance 0223, patch-grid anisotropy 0225.

**Cluster 11 — Valuable Negative Results (killed 15/20).** The cluster's weaker entries were negative results whose truth would surprise no one (multi-scale TTA death 0229) or whose control everyone skips but the conclusion is benchmark-dependent (0230 self-training compute laundering). Survivors are the sharp falsifications: deep-supervision null 0226, TTA collapse anatomy 0238/0239, boundary-loss null 0242, curriculum null 0245.

**Cluster 12 — Few-Shot & Zero-Shot (killed 12/15).** The matcher-class literature already published 0247's core claim; 0257's support-allegiance dissociation lost to 0223 running the same logic on a stronger target; 0260's ambiguity floor was family-redundant with 0103/0336/0337. Survivors: episodic-protocol fiction 0246, support-set lottery 0250, the k-shot saturation law 0254.

**Cluster 13 — Weakly/Semi/Self-Supervised (killed 16/20).** Supervision-economics curves (0262/0263) were trimmed to the strongest, and matched-pretraining-arm costs killed 0275. The genuinely novel 0278 (mask-MAE prior from unpaired masks) died as method-flavored with convention-encoding risk. Survivors: CAM-ceiling verdict 0261, pseudo-label noise anatomy 0266, SAM-error inheritance 0267, uncertainty-routing failure 0280.

**Cluster 14 — Synthetic Data & Generative Training (killed 12/15).** Structured-noise anatomy (0281) and bias-amplification direction (0284) folded into the surviving program; dense model-collapse (0288) is being raced. Survivors: realism-factor attribution 0283, the rare-class inversion threshold 0285, procedural-vs-diffusion coverage circularity 0287.

**Cluster 15 — Domain Adaptation & Shift (killed 12/15).** The diagnostic near-misses (0297 style/content decomposition, 0304 Fourier spectroscopy) folded into the surviving 0296+0303 pair; 0301's cyclic-recurrence protocol died on data-assembly weight; 0300's foundation-vs-UDA confrontation was judged largely priced-in by 2026. Survivors: the fresh-pair ranking audit 0296, the norm-recovery tier diagnostic 0303, the night-vision information-floor decomposition 0305.

**Cluster 16 — Object Detection Failure Modes (killed 13/15).** Well-trodden comparisons (0318 anchor-based vs anchor-free) and already-probed questions (0320 detector-feature identity, 0317 COCO re-annotation post-COCO-ReM) died. Survivors: the compute-matched resolution showdown 0313 and the amorphous-primitive question 0319.

**Cluster 17 — Evaluation Methodology (killed 12/15).** The strongest cluster per capita; kills were mostly consolidation. 0331 (paired-test SOTA audit) and 0335 (worst-class re-scoring) delivered verdicts overlapping 0340 at higher cost; 0326's seed-noise reference tables cost 600 runs for a resource-track artifact. Survivors: human floors/ceilings 0336, instructions-as-treatment 0337, leaderboard fiction-fraction 0340.

---

## Forbidden-category enforcement

- **Module stacking:** zero survivors contain "add module A + module B" contributions; candidates in Clusters 3, 6, and 7 with attention/fusion-module payloads were killed regardless of scores.
- **"Apply X to medical" without a new question:** killed throughout Cluster 5 (and medical-flavored entries elsewhere); medical survivors all pose questions that are *about* the clinical setting (label-noise ceilings, inter-rater floors, shortcut anatomy), not ports.
- **Loss/backbone swaps:** killed on sight; the only loss-focused survivors are *falsifications* of loss claims (0242 boundary-loss null), which is the opposite of a swap paper.

---

## 15 "almost survived" — and why they were killed

1. **IDEA-A-0331 — What fraction of SOTA claims survives paired significance tests.** Cheap and damning, Upside 5 / ROI 5. Killed because 0340 (bootstrap fiction-fraction) delivers the same field-level verdict with even less compute and a sharper headline number; keeping both would be double-publishing one finding.
2. **IDEA-A-0304 — Fourier-swap success as gap spectroscopy.** Elegant trick-to-instrument reframing. Killed because its diagnostic payload is subsumed by the surviving 0296 (fresh-pair audit) + 0303 (norm-recovery diagnostic) pair, and the hidden window-size parameter undermines the "one-shot spectroscope" claim.
3. **IDEA-A-0297 — Style/content gap decomposition per benchmark.** The right explanatory companion to 0296. Killed as a dependent satellite: its decomposition only matters if 0296's scramble result lands, and imperfect style-neutralization tools make its core measurement contestable on its own.
4. **IDEA-A-0052 — Bias-variance decomposition of PEFT vs full fine-tuning.** Excellent statistical framing (SciQ 5). Killed on compute: the honest version needs a ~480-run grid across tasks, budgets, and seeds; a subsampled version wouldn't support the decomposition claims.
5. **IDEA-A-0039 — Is prompt tuning secretly a linear probe?** Strong demystification target. Killed because matched-budget equivalence testing across model scales is heavy, and a positive result (they're equivalent) is publishable mainly as a note unless the equivalence breaks somewhere interesting.
6. **IDEA-A-0278 — Mask-MAE prior from unpaired mask archives.** The most novel killed idea (Nov 5): a genuinely new resource. Killed as method-flavored (builds a thing rather than tests a claim) with a convention-encoding risk — mask archives embed annotation conventions (cf. survivor 0007), so the "prior" may be a convention prior.
7. **IDEA-A-0247 — Frozen-VFM matching beats few-shot segmentation architectures.** Killed because training-free matcher-class results in the literature have already published the core claim (Unp 2); what remains is a tidier confirmation, not a discovery.
8. **IDEA-A-0326 — Benchmark seed-noise reference tables.** High-leverage community infrastructure. Killed on the 600-run compute bill and venue reality: reference tables are resource-track artifacts, and survivor 0340 makes the statistical point with far less compute.
9. **IDEA-A-0317 — COCO re-annotation compresses modern rankings.** Killed because COCO-ReM-style re-annotation efforts have already published the core result (Unp 2); the marginal contribution is a larger sample of a known effect.
10. **IDEA-A-0096 — Small-lesion sensitivity law: foundation vs specialist.** Clinically pointed. Killed because size-stratified sensitivity evaluations partially exist in the medical imaging literature and survivor 0161 (GSD ladder) carries the general size-law science; the medical instance adds a venue, not a question.
11. **IDEA-A-0230 — Self-training rounds as compute laundering.** The equal-compute control the semi-supervised literature systematically skips. Killed because the verdict is likely benchmark-dependent (helps where unlabeled data is plentiful and shifted, launders where it isn't), which turns the headline into "it depends" — and survivor 0245's curriculum null holds the cluster's strongest null slot.
12. **IDEA-A-0301 — Continual DA thrashes under cyclic domains.** The cyclic-recurrence protocol is genuinely new evaluation science. Killed on data-assembly weight: time-stamped multi-cycle driving data with stable content is scarce, and the synthetic fallback weakens the deployment claim that motivates the idea.
13. **IDEA-A-0065 — Norm-tuning fixes scanner shift.** Killed as the special case: survivor 0303 generalizes exactly this diagnostic beyond medical with a validated tier-mapping; keeping both would spend two slots on one instrument.
14. **IDEA-A-0328 — Simulated-click protocol validity for interactive segmentation.** Absorbs the good part of 0048. Killed on user-study variance: the human-clicker arm needed for validation is expensive, high-variance, and the likely result (simulators are optimistic but rank-preserving) is a calibration note.
15. **IDEA-A-0075 — Task arithmetic for dense prediction: addition works, negation fails.** Timely and falsifiable. Killed because the task-vector literature is moving fast enough that the dense-prediction port risks being scooped before completion (Unp 3 trending down), and the shared-decoder constraint muddies the clean weight-space story that makes task arithmetic attractive.

---

*End of Stage 2 Batch A killed report. 267 killed · 73 survive → Stage 3.*
