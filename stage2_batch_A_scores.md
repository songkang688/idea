# Stage 2 — Batch A: Adversarial Scores (IDEA-A-0001 … 0340)

**Reviewer role:** independent Stage 2 reviewer for Windows5's Autonomous Research Idea Evolution.
**Input:** `stage1_batch_A_ideas.md` (340 ideas), `stage1_batch_A_index.md`.
**Output:** 73 survivors (21.5%), 267 killed. Survivors carry full dossiers in `stage2_batch_A_survivors.md`; elimination rationale in `stage2_batch_A_killed.md`.

**Scoring legend (1–5 unless noted):**
Nov=Novelty · Sig=Significance · SciQ=quality of the scientific question · Tech=technical soundness · Feas=feasibility · Cmp=compute friendliness (5=near-free) · Dat=dataset availability · Bas=baseline availability · Unp=likelihood NOT already published (5=very unlikely published) · Clr=experimental clarity · Ven=venue potential (CVPR/ICCV/ECCV/MICCAI) · Rsk=risk L/M/H (noted, not summed) · Up=potential upside · ROI=research ROI.
**Prot flags:** HR=high-risk/high-reward · CI=simple-but-counter-intuitive · RM=reviewer-disagreement magnet · CF=cheap-to-falsify. Protected ideas survive even where conservative mean-scoring would kill them.
**Selection was NOT by mean score.** Fatal flaws (likely-published, redundancy, infeasibility, forbidden category) kill high-mean ideas; protected categories rescue low-mean ones.

## Cluster 1 — SAM/SAM2 Failure Modes (0001–0030): kept 7/30

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0001 | SAM follows edges, not objects | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | M | 4 | 5 | CI | Y | Clean 2×2 mechanistic dissociation; cheap; underpins every SAM-as-object-proposal pipeline |
| 0002 | SAM ambiguity head vs human disagreement distribution | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | M | 3 | 3 | — | N | Needs 10-annotator collection; overlaps 0015/0260; null hard to reject |
| 0003 | IoU-vs-size failure law with patch-size knee | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 3 | 5 | 4 | L | 4 | 5 | CF | Y | Turns folklore into a quantitative design law; near-free; falsifiable knee prediction |
| 0004 | SAM2 occlusion-duration decay curves | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | L | 3 | 3 | — | N | Eval-paper flavor; VOS occlusion analyses close by; low surprise either way |
| 0005 | SAM2 identity switches: appearance vs position | 3 | 3 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Niche; switch events rare in benchmarks; purpose-built set needed |
| 0006 | Amorphous failure = boundary-contrast curve | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 5 | CI | Y | Single-variable law unifying smoke/fire/glass failures; decides preprocess-vs-retrain |
| 0007 | SAM masks imprint SA-1B annotation protocol | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | M | 5 | 5 | RM | Y | Ecosystem-level claim: "segment anything" = SA-1B policy replicator |
| 0008 | Click-position IoU map; medial-axis law | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 4 | 3 | 5 | 3 | L | 3 | 4 | — | N | Useful map but engineering guidance; almost survived |
| 0009 | Negative-click unreachable error set | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Interesting ceiling claim but narrow; folded into interactive-seg lit |
| 0010 | Betti-error audit on thin structures | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 2 | 4 | 3 | L | 3 | 3 | — | N | Topology audits of SAM already circulating in medical SAM papers |
| 0011 | Corruption-robustness profile of SAM | 2 | 3 | 3 | 4 | 4 | 4 | 5 | 4 | 2 | 4 | 3 | L | 2 | 2 | — | N | SAM robustness-to-corruption papers already exist; shrinkage taxonomy not enough |
| 0012 | SAM vs DINOv2 geometry/semantics probes | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 2 | 4 | 3 | L | 3 | 3 | — | N | Probing comparisons largely published; folded into 0202 matrix |
| 0013 | SAM2 worse than SAM1 on static fine boundaries | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | M | 4 | 5 | CI+CF | Y | Counter-intuitive newest-isn't-better; a week of inference; immediately actionable |
| 0014 | Encoder-vs-decoder bottleneck attribution | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Good question; HQ-SAM adjacent; capacity sweeps costly; almost survived |
| 0015 | SAM granularity prior vs human preference | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 3 | M | 3 | 3 | — | N | Human study; overlaps 0002/0188/0260 ambiguity family |
| 0016 | Predicted-IoU calibration audit cross-domain | 3 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 2 | 5 | 3 | L | 4 | 4 | — | N | OOD miscalibration partially documented in medical-SAM lit; almost survived |
| 0017 | Domain-distance predicts SAM performance | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | M | 3 | 2 | — | N | FID-style distance is a weak instrument for line art/sensor domains |
| 0018 | Clicks-to-convergence taxonomy | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | NoC metrics exist; non-convergence content covered by 0009 (also killed) |
| 0019 | Phantom re-ID after occlusion | 3 | 3 | 3 | 4 | 3 | 4 | 2 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Curation-heavy; niche failure class |
| 0020 | Resize-vs-tile crossover law | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Practical guide, low scientific depth; prompt-propagation protocol unsolved |
| 0021 | Is SAM functionally achromatic? | 4 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | L | 4 | 5 | CI+CF | Y | One-day falsification; equiluminant-edge condition is decisive; protected |
| 0022 | Box-vs-point disagreement as failure detector | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 3 | 5 | 3 | L | 4 | 4 | — | N | Useful but classic-ensemble-disagreement flavor; correlated errors cap it; almost |
| 0023 | Frozen-encoder head-to-head, matched decoders | 3 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 2 | 4 | 3 | L | 3 | 3 | — | N | Merged into 0202 task×backbone matrix |
| 0024 | What distillation to efficient SAM loses first | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Per-variant training-data confounds; descriptive profile only |
| 0025 | Modal vs amodal behavior by prompt type | 4 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 3 | L | 3 | 4 | — | N | Clean and cheap but narrow convention documentation; almost survived |
| 0026 | Memory-size non-monotonicity in SAM2 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Ablation-flavored; effect likely small vs clip variance |
| 0027 | Hole-filling bias on genus>0 objects | 4 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 3 | L | 3 | 4 | — | N | Cute genus audit; narrow robotics payoff; loses to stronger C1 survivors |
| 0028 | When prompt-jitter ensembling hurts | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Conditional-rule trick science; TTA-hurts genre known |
| 0029 | SAM-assisted annotation contaminates future GT | 5 | 5 | 5 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 5 | H | 5 | 5 | HR+RM | Y | Dataset-generation feedback loop; field-level stakes; protected high-risk |
| 0030 | Pre-hoc per-instance failure predictor | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Methodsy; the scientific content lives in 0016/0022 (both killed as near-misses) |

## Cluster 2 — Prompt Sensitivity (0031–0050): kept 4/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0031 | Paraphrase variance vs SOTA gaps | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | L | 4 | 5 | CF+RM | Y | If rankings sit inside prompt noise, leaderboard conclusions wobble; days of inference |
| 0032 | Vocabulary composition/order sensitivity | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 3 | L | 3 | 4 | — | N | Strong companion experiment but subsumable under 0031's program; almost |
| 0033 | Specificity inverse-U (basic-level optimum) | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | M | 4 | 5 | CI+CF | Y | Rosch basic-level theory meets dense prediction; frequency mechanism testable |
| 0034 | Negative prompts help only when confusable | 3 | 3 | 3 | 3 | 4 | 5 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Trick-to-rule engineering; methodsy |
| 0035 | CoOp prompts: dataset vs backbone transfer | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | CoOp transfer studied; cross-backbone mapping introduces its own confound |
| 0036 | Paraphrase variance as OOD/error detector | 3 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Method paper; boundary-pixel false positives likely dominate |
| 0037 | Exemplar-vs-text exchange rate in bits | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | M | 3 | 3 | — | N | Neat framing but model-mixture-dependent; few dual-interface models |
| 0038 | Prompt-encoding aliasing on patch grid | 4 | 2 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 2 | L | 2 | 2 | — | N | Idea's own risk section concedes practical irrelevance; index overrated it (cheap #13) |
| 0039 | Is prompt tuning secretly a linear probe? | 4 | 4 | 5 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Strong demystification; matched-budget sweeps heavy; almost survived |
| 0040 | Per-prompt temperature calibration | 3 | 3 | 3 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 2 | L | 2 | 2 | — | N | Incremental calibration variant; no venue pull |
| 0041 | Does CoT causally change grounding? | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 5 | H | 5 | 5 | HR+CI | Y | Causal intervention on reasoning with mask endpoint; kills or crowns "reasoning segmentation" |
| 0042 | Multilingual dense-prediction audit | 3 | 4 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | M | 3 | 3 | — | N | Equity value real but translation logistics dominate; audit-flavored |
| 0043 | Prompt length vs content dissociation | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Hygiene experiment; folded under 0031's umbrella |
| 0044 | Prune the 80-template CLIP ensemble | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 2 | 5 | 2 | L | 2 | 2 | — | N | Template pruning largely settled for classification; index overrated (cheap #7) |
| 0045 | Does scale shrink prompt sensitivity? | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | M | 4 | 3 | — | N | Good question; clean dense model ladders barely exist; almost survived |
| 0046 | One-character typo attack surface | 3 | 3 | 3 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Deployment note; tokenizer-fragmentation link is the only fresh part |
| 0047 | Everything-mode recall blind spots | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 3 | L | 3 | 4 | — | N | Useful dissection; engineering-adjacent; NMS sensitivity muddies claims; almost |
| 0048 | Human vs simulated clicks, ranking inversion | 4 | 4 | 4 | 3 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | H | 4 | 3 | — | N | Superseded by 0328 (protocol-validity framing), itself a near-miss; human-study variance |
| 0049 | Lay vs expert terms for medical grounding | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 5 | 4 | M | 4 | 5 | CI+CF | Y | Free performance lever + diagnosis of what the text tower knows; protected |
| 0050 | Prompt-interpolation phase transitions | 3 | 2 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 2 | M | 2 | 2 | — | N | Off-manifold interpolants make the result uninterpretable; index overrated (cheap #9) |

## Cluster 3 — PEFT & Fine-Tuning Instability (0051–0075): kept 4/25

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0051 | LoRA rank predicted by ΔW intrinsic dimension | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | NLP analogues exist; pilot-rank instability risk; almost survived |
| 0052 | Bias-variance decomposition of PEFT vs full FT | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Excellent framing; 480-run grid; almost survived on compute |
| 0053 | Attention-LoRA=spatial, MLP-LoRA=semantic | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Nice dissociation; real tasks mix shift types; overlaps 0062 |
| 0054 | Component rewinding attribution for SAM FT | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Redundant with 0014 + 0077 family |
| 0055 | LLRD explains most PEFT advantage | 4 | 5 | 4 | 4 | 4 | 3 | 5 | 5 | 3 | 5 | 4 | M | 5 | 5 | CI+RM | Y | If true, dozens of PEFT comparisons need reinterpretation; protected magnet |
| 0056 | Attention-entropy collapse as divergence alarm | 3 | 3 | 3 | 3 | 3 | 2 | 4 | 4 | 4 | 3 | 3 | M | 3 | 2 | — | N | 100-run instrumentation for a monitoring heuristic; multi-causal spikes |
| 0057 | BitFit as shift-type diagnostic | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Redundant with 0065/0303 diagnostic family; 0303 survives |
| 0058 | LoRA amplifies spurious correlations | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 5 | HR+CI | Y | Low-rank ⇒ reweight existing (possibly spurious) directions; worst-group safety stakes |
| 0059 | LoRA-merge interference from subspace overlap | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | M | 3 | 3 | — | N | Model-merging literature moving too fast; likely covered by 2026 |
| 0060 | PEFT preserves calibration better than full FT | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Good; accuracy-matching finicky; loses tiebreak to 0058/0072; almost |
| 0061 | PEFT/full-FT crossover vs label complexity | 3 | 4 | 3 | 4 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | M | 3 | 2 | — | N | Expensive grid to fit a lookup curve; schedule-dependence acknowledged |
| 0062 | Early adapters=input shift, late=label shift | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Redundant with 0053; factorial with it would be one paper |
| 0063 | Prompt-tuning seed variance = flat degenerate valleys | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | M | 3 | 2 | — | N | Sharpness metrics notoriously slippery; niche method pathology |
| 0064 | Effective-rank collapse during LoRA training | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Diagnostic curiosity; adaptive-rank trigger is method work |
| 0065 | Norm-tuning fixes scanner shift | 3 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 2 | 5 | 3 | L | 4 | 4 | — | N | Norm-tuning known; 0303 (survivor) generalizes the diagnostic; almost survived |
| 0066 | fp16 instability locus in SAM | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 2 | M | 3 | 2 | — | N | Valuable engineering note, not a conference paper |
| 0067 | One dial: encoder/decoder LR ratio explains recipes | 5 | 4 | 5 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | H | 5 | 4 | HR+RM | Y | Radical simplification claim; R²>0.7 or bust; protected reviewer magnet |
| 0068 | Fine-tuning collapses SAM's ambiguity head | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | L | 3 | 4 | — | N | Fresh forgetting axis but a trivial loss term may fix it, deflating the paper; almost |
| 0069 | Warmup = decoder/encoder gradient mismatch | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Plausible optimization science; "encoder damage" operationalization circular |
| 0070 | Mask-loss vs IoU-head gradient conflict | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 2 | — | N | Conflict may be rare; two-phase fix is recipe tweak |
| 0071 | Weight-EMA as free forgetting mitigation | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 3 | 5 | 3 | L | 4 | 4 | — | N | Cheap and useful; thin as a flagship; EMA-averaging lit adjacent; almost |
| 0072 | Strong-aug frozen features vs LoRA at matched compute | 4 | 4 | 5 | 4 | 4 | 3 | 5 | 5 | 3 | 5 | 4 | M | 4 | 5 | RM | Y | The controlled comparison the field skipped; adaptation-vs-invariance verdict |
| 0073 | Surgical fine-tuning for dense tasks | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Validation of a classification-era heuristic; oracle cost high |
| 0074 | LoRA dropout is placebo | 3 | 2 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 2 | L | 2 | 2 | — | N | Well-powered null on a minor knob = workshop note; index overrated (surprising #20) |
| 0075 | Task arithmetic for dense: addition works, negation fails | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Timely; task-vector lit racing; shared-decoder constraint; almost survived |

## Cluster 4 — Catastrophic Forgetting (0076–0090): kept 3/15

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0076 | Gain/retention frontier; forgetting is unforced error | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | M | 5 | 4 | RM | Y | "Most forgetting is recipe hygiene" would reset practice; frontier estimation is the instrument |
| 0077 | Layer-wise forgetting localization by rewinding | 3 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Folded into the 0076/0078 program; classification analogues exist |
| 0078 | Forgetting is mostly readout drift | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | M | 5 | 5 | CI | Y | If capabilities remain linearly decodable, continual learning changes objective entirely |
| 0079 | Minimal replay fraction for retention | 3 | 4 | 3 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Useful curve; SA-1B access friction; saturation result likely unsurprising; almost |
| 0080 | Modality-order effects in sequential adaptation | 3 | 3 | 3 | 4 | 3 | 2 | 4 | 4 | 3 | 4 | 3 | M | 3 | 2 | — | N | 6-ordering grid, recipe-dependent conclusions |
| 0081 | Boundary skill forgotten before region skill | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | L | 3 | 4 | — | N | Neat decay-dynamics observation; monitoring-note scale; almost survived |
| 0082 | WiSE-FT interpolation for dense prediction | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 2 | 4 | 3 | M | 3 | 3 | — | N | Dense WiSE-FT replications already appearing; fresh-decoder boundary is the only new bit |
| 0083 | Forgetting: direction matters more than distance | 4 | 4 | 5 | 3 | 3 | 3 | 4 | 4 | 4 | 3 | 4 | H | 4 | 3 | — | N | Curvature estimation at foundation scale fragile; two estimators may disagree; almost |
| 0084 | Adapter libraries vs weight updates trade sheet | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Benchmark bake-off; router choice dominates outcome |
| 0085 | Tower-swap forgetting attribution in VLMs | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 3 | L | 4 | 4 | — | N | Clean diagnostic with one-line recipe payoff; co-adaptation artifacts; almost |
| 0086 | SAM2 video FT degrades image path | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Cross-modality regression testing; effect may vanish under LoRA |
| 0087 | Does Fisher localize dense-task knowledge? | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Diagonal-Fisher critique known in CL; negative may only indict approximation |
| 0088 | Teacher-veto failure of retention distillation | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Conditional law; distillation-weight sweep muddies attribution |
| 0089 | Forgetting hysteresis: suppression not erasure | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | H | 5 | 4 | HR | Y | Suppression-vs-erasure with time constants; cheap-refresh implication; protected |
| 0090 | Concept-vs-prior forgetting decomposition benchmark | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | M | 3 | 3 | — | N | Benchmark construction; axes may be empirically correlated (own risk admits) |

## Cluster 5 — Medical Segmentation Limits (0091–0120): kept 6/30

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0091 | Leaderboard gains below label-noise floor | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 5 | M | 5 | 5 | RM | Y | Cross-benchmark annotator-ceiling audit tied to leaderboard spreads; field-recalibrating |
| 0092 | Clinician prompts vs benchmark-tight boxes | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 4 | 3 | — | N | Clinician recruitment gates it; strong MICCAI candidate otherwise; almost |
| 0093 | Why nnU-Net still wins: causal decomposition | 4 | 5 | 5 | 4 | 3 | 2 | 5 | 5 | 3 | 4 | 4 | H | 5 | 4 | HR+RM | Y | The strategic fork of medical VFMs; component-swap attribution; protected magnet |
| 0094 | Scanner shift is high-frequency texture shift | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | M | 4 | 4 | — | N | Clean band-swap causal design; Fourier-DA adjacency lowers novelty; almost |
| 0095 | 2D-vs-3D gap tracks slice-identifiability | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Human slice-study burden; law is nice but effortful |
| 0096 | Small-lesion sensitivity law: VFM vs specialist | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Clinically pointed; size-stratified evals partially exist; almost survived |
| 0097 | Dice loss destroys calibration; imbalance-scaled | 4 | 5 | 4 | 4 | 4 | 3 | 5 | 5 | 3 | 5 | 4 | L | 4 | 5 | RM | Y | Settles a folklore dispute about the default loss with a usage rule; absorbs 0244 |
| 0098 | Asymmetry shortcut fails on bilateral disease | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | M | 4 | 4 | — | N | Sharp shortcut hypothesis; severity confound matching hard; almost survived |
| 0099 | Dice-vs-topology ranking inversions (vessels) | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | L | 3 | 3 | — | N | clDice literature already makes inversions expected |
| 0100 | Flip-TTA harms lateralized anatomy | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | L | 4 | 5 | CI+CF | Y | Harmful default inside challenge winners; days to falsify; protected |
| 0101 | SynthSeg-style randomization for pathology | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 4 | H | 4 | 3 | — | N | Worthy but big program; "extend SynthSeg" flavor within Stage-2 scope |
| 0102 | Federated LoRA factor-averaging breaks | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | M | 3 | 3 | — | N | Factor-vs-composed aggregation already noted in FedPEFT literature |
| 0103 | Uncertainty maps ≠ clinician disagreement | 4 | 5 | 5 | 4 | 4 | 5 | 3 | 4 | 4 | 5 | 4 | M | 5 | 5 | CI | Y | Boundary-band-excluded test may empty the clinical value proposition of uncertainty maps |
| 0104 | 3D active learning vs random, time-normalized | 3 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | AL-vs-random critiques exist; timing-model sensitivity; almost |
| 0105 | Infiltration maps instead of step-edge GT | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 4 | 3 | — | N | Needs radiation-oncology grounding; distributional claims only for now |
| 0106 | What transfers across tumor types | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Transfer-matrix study; covariate story underpowered |
| 0107 | Anatomical-relation language ignored by VLMs | 4 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | L | 3 | 4 | — | N | Cheap negative; encoder-vs-fusion attribution murky; almost survived |
| 0108 | Patient-level leakage audit + dedup splits | 3 | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | L | 4 | 4 | — | N | High-value hygiene; classification-leakage precedents make it maintenance science; almost |
| 0109 | Does medical pretraining still beat DINOv2? | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Budget-stratified audit; overlapping ablations appear in recent VFM-medical papers |
| 0110 | Missing-sequence robustness trade-off | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 2 | 4 | 3 | L | 3 | 3 | — | N | Missing-modality literature dense; router-vs-dropout is incremental |
| 0111 | Isotropic resampling: legacy habit? | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | — | N | Good default re-audit; nnU-Net pipeline entanglement makes isolation hard; almost |
| 0112 | Benchmark version drift audit | 3 | 3 | 3 | 4 | 3 | 4 | 2 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Version archaeology; old releases hard to obtain |
| 0113 | Ultrasound: VFM value vanishes under speckle-aug | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Modality-statistics logic generalized by 0310 (near-miss); US-specific claim narrower |
| 0114 | SAM2 surgical failure is event-driven | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Event annotation subjective; deployment-guard payoff real but niche |
| 0115 | Pathology context-radius requirement | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | — | N | Anti-hype measurement; saturation is capacity-dependent; almost survived |
| 0116 | Metric ranking flips + downstream anchor | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Metric criticism perennial; downstream-surrogate anchor is the fresh part; almost |
| 0117 | Report-supervision localization ceiling | 4 | 4 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | M | 4 | 3 | — | N | Radiologist panel gates it; ceiling logic excellent; almost |
| 0118 | Models hallucinate surgically removed organs | 5 | 5 | 5 | 4 | 3 | 4 | 2 | 4 | 4 | 4 | 5 | M | 5 | 5 | CI | Y | Patient-safety silent failure; atlas-prior mechanism; protected counter-intuitive |
| 0119 | Synthetic-lesion insertion artifacts learned | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Folded into 0282/0285 artifact-shortcut family (0285 survives) |
| 0120 | Clinician+model complementarity conditions | 4 | 4 | 4 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 4 | H | 4 | 3 | — | N | IRB/human-factors heavy; HCI venue better fit |

## Cluster 6 — Smoke & Fire (0121–0140): kept 6/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0121 | Binary smoke masks are ill-posed GT | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | M | 5 | 5 | RM | Y | Task-redefinition with a measurable threshold-decomposition test; anchors the smoke program |
| 0122 | Beer–Lambert transmittance ground truth | 5 | 5 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | H | 5 | 4 | HR | Y | First physically defined supervision for smoke; protected high-risk construction |
| 0123 | Fire segmenters are color detectors | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 5 | 4 | L | 4 | 5 | CI+CF | Y | Predicts missed blue flames + sunset false alarms; safety-critical; cheap |
| 0124 | Smoke/fog/steam/cloud/dust: temporal separability | 4 | 4 | 5 | 4 | 2 | 4 | 2 | 3 | 4 | 4 | 4 | H | 5 | 3 | — | N | Information-theoretic framing superb; curation + human studies gate it; almost |
| 0125 | Turbulence spectra as label-free smoke signal | 5 | 4 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | H | 5 | 4 | HR | Y | Physics-grounded appearance-free pretext; protected high-risk/high-reward |
| 0126 | Detection latency as the wildfire metric | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 4 | RM | Y | Mission-aligned metric; ranking-disagreement claim is testable and consequential |
| 0127 | Which synthetic-smoke fidelity axis matters | 3 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Folded into 0283/0287 synthetic-fidelity program |
| 0128 | No prompt strategy rescues SAM on smoke | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | L | 4 | 5 | CF | Y | Definitive cheap negative + shrinkage law; blocks unfit auto-labeling; protected |
| 0129 | Fire benchmarks reward scene context | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Context-bias genre known; fire instance; inpainting artifacts risk |
| 0130 | Day/night regime conflict in fire models | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Regime analysis plausible but unsurprising; specialist-vs-mixed ablation flavor |
| 0131 | Calibrated IR-only matches RGB+IR fusion | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | M | 4 | 4 | — | N | Modality-ablation ethic excellent; public RGB-IR fire data too thin; almost survived |
| 0132 | Density regression beats binary training | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Merged into the 0121/0122 program as its natural experiment |
| 0133 | Hard-negative taxonomy benchmark | 4 | 5 | 3 | 4 | 3 | 4 | 2 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Operationally vital; curation + licensing dominate; benchmark-paper venue risk; almost |
| 0134 | Video architecture vs frame+filter at matched compute | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Good null design; conclusion likely frame-rate-dependent |
| 0135 | Codec compression deletes faint smoke | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | L | 3 | 3 | — | N | Practical data-pipeline finding; augmentation fix mundane |
| 0136 | Weak labels from dispatch/satellite metadata | 3 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 4 | 3 | 3 | H | 4 | 2 | — | N | Heavy engineering; metadata noise unquantified |
| 0137 | Plume-physics consistency as label-free QA | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | H | 4 | 3 | — | N | Wind-field variability may sink the advection fit |
| 0138 | Do better masks improve fire-spread forecasts? | 4 | 5 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 3 | M | 5 | 3 | — | N | Rare utility-chain science; simulator error floors + venue mismatch; almost survived |
| 0139 | Plume instance identity: merge-horizon formalism | 5 | 3 | 5 | 3 | 2 | 4 | 2 | 3 | 5 | 3 | 3 | H | 4 | 3 | — | N | Genuinely new formalism; multi-source footage nearly nonexistent; almost |
| 0140 | Cross-geography gap is negative-class shift | 3 | 4 | 4 | 4 | 3 | 4 | 2 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Actionable decomposition; regional data + camera confounds |

## Cluster 7 — Transparent/Mirror/Ambiguous (0141–0160): kept 4/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0141 | Features on glass encode the background | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | M | 5 | 5 | HR+CI | Y | If representation is "transparent to transparency", no decoder can fix it; field-redirecting |
| 0142 | Depth input hurts; depth-invalidity is the cue | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | M | 5 | 5 | CI | Y | Sign-inversion of "more modalities help"; sensor failure as signal; protected |
| 0143 | Supervise boundaries/highlights, not glass interiors | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Loss-reweighting flavor (forbidden-adjacent) despite nice physics rationale |
| 0144 | Is reflection/transmission decomposition necessary? | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Necessity question decent; reflection-strength GT gating |
| 0145 | SAM on glass: prompt-conditioned bimodality | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 5 | 3 | L | 4 | 4 | — | N | Cheap; subsumed by 0141's stronger representational claim; almost survived |
| 0146 | Double-assignment through transparent occluders | 5 | 4 | 5 | 4 | 2 | 4 | 2 | 3 | 5 | 4 | 4 | H | 4 | 3 | — | N | Formulation-breaking idea; behind-glass annotation cost gates it; almost |
| 0147 | Distributional eval for ambiguous regions | 3 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Multi-annotator eval family; 0103/0337 carry the flag |
| 0148 | Shadow-inclusion convention audit | 3 | 3 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 3 | L | 3 | 3 | — | N | Hygiene note; graded-penumbra metrics fiddly |
| 0149 | Mirrors: scene-reasoning or texture matching? | 4 | 4 | 4 | 4 | 3 | 4 | 2 | 4 | 4 | 4 | 4 | M | 4 | 4 | — | N | Clean mechanism test; atypical-mirror set requires controlled capture; almost |
| 0150 | Polarization: sensing vs learning, distillability test | 4 | 4 | 5 | 4 | 3 | 4 | 2 | 3 | 4 | 4 | 4 | M | 4 | 3 | — | N | Sharp epistemic instrument; paired datasets too small for conclusive effect; almost |
| 0151 | Wires/meshes are matting, not segmentation | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 3 | M | 4 | 3 | — | N | Task redefinition; downstream-task choice could rig either verdict |
| 0152 | Refraction distortion as standalone cue | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Synthetic-first ceiling study; in-the-wild estimation unsolved |
| 0153 | Transparency benchmarks measure container shapes | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | L | 4 | 3 | — | N | Bias-audit genre; sourcing unusual transparent objects is the bottleneck |
| 0154 | COD failure: attentional vs perceptual | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | L | 5 | 5 | CF | Y | One oracle-prompt experiment could redirect the COD subfield; near-free |
| 0155 | Soft labels improve downstream decisions | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | M | 4 | 3 | — | N | Downstream battery is simulation-dependent; calibration-benefit lit adjacent |
| 0156 | Collision-weighted transparency metric | 3 | 4 | 3 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 3 | L | 3 | 3 | — | N | Metric-proposal redundancy with stronger 0126/0116 exemplars |
| 0157 | Human floor on near-invisible glass | 4 | 4 | 5 | 4 | 3 | 5 | 2 | 4 | 4 | 4 | 4 | M | 5 | 4 | CI | Y | Competence-vs-information verdict decides modeling-vs-sensing investment; protected |
| 0158 | Water surfaces: which paradigm fits? | 3 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | M | 4 | 3 | — | N | Regime comparison; turbidity GT weak |
| 0159 | Does mask IoU predict grasp success on glass? | 4 | 4 | 5 | 4 | 2 | 3 | 3 | 3 | 4 | 4 | 4 | H | 4 | 3 | — | N | Utility-chain validation needs robot trials; 0138 (also near-miss) is same genre |
| 0160 | Transparency failure signature in medical imaging | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | M | 4 | 3 | — | N | Borderline "port toolkit to medical"; phenomenological analogy risk |

## Cluster 8 — Small Objects & Boundary Quality (0161–0180): kept 5/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0161 | Patch-quantization floor: decoder-invariance test | 4 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 3 | 5 | 4 | M | 5 | 4 | RM | Y | Settles whether small-object decoder research is futile; interventionist design |
| 0162 | CNN vs ViT boundary error styles | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 4 | 3 | L | 3 | 3 | — | N | Descriptive signature study; recipe confounds |
| 0163 | Where boundary information dies (layer probes) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | — | N | Good audit; probe-capacity dependence muddies "decodability"; almost survived |
| 0164 | Oracle-magnification decomposition of small-object failure | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Overlaps 0161 + 0313; the weaker of the three |
| 0165 | Boundary losses: decisions or confidence paint? | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | M | 4 | 4 | — | N | Sharp decomposition; formalization risk; almost survived (absorbs 0227) |
| 0166 | Annotation jitter floor; residuals predict annotator | 5 | 5 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 5 | CI | Y | Annotator-identity test is a killer instrument for boundary-metric saturation |
| 0167 | Learned seam repair vs overlap tiling | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Engineering/module flavor (forbidden-adjacent) |
| 0168 | Are FPNs vestigial for modern ViTs? | 3 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 2 | 4 | 3 | L | 3 | 3 | — | N | ViTDet already showed plain-backbone sufficiency for detection; segmentation delta small |
| 0169 | PE interpolation damages local geometry | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 | M | 3 | 3 | — | N | Native high-res training arm expensive; effect likely small |
| 0170 | INR decoders hallucinate sub-pixel boundaries | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | M | 5 | 5 | CI | Y | Synthetic-truth dissociation exposes metric gaming; measurement-app stakes; protected |
| 0171 | Copy-paste teaches paste detection | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Copy-paste artifact family; 0285 (survivor) carries the sharpest version |
| 0172 | Crowding failure is assignment, not features | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Strong oracle decomposition; hint-injection without retraining tricky; almost survived |
| 0173 | Connectivity metrics reorder thin-structure rankings | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | L | 4 | 3 | — | N | clDice-era results make inversions expected; checkpoint availability |
| 0174 | Register-token artifacts blind small objects | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | L | 4 | 5 | CF | Y | Ties a hot ViT mechanism to concrete dense harm; pure inference study; protected |
| 0175 | Query starvation for small instances | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Redundant with 0172's assignment-failure program |
| 0176 | Benchmark JPEG already deleted small objects | 5 | 5 | 5 | 4 | 3 | 4 | 2 | 4 | 4 | 4 | 4 | M | 5 | 4 | CI | Y | Benchmark-construction confounder; reframes "small objects are hard"; protected |
| 0177 | Learned foveation vs uniform resolution | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Methodsy architecture comparison; proposal-recall bound dominates |
| 0178 | Perceptually weighted boundary metric | 4 | 4 | 4 | 4 | 2 | 4 | 3 | 4 | 4 | 4 | 4 | M | 4 | 3 | — | N | 5k-preference collection; framing effects; metric-proposal genre |
| 0179 | Human floor for sub-8px aerial detection | 4 | 4 | 4 | 4 | 2 | 4 | 3 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Expert imagery analysts hard to recruit; human-ceiling family capped (0336 survives) |
| 0180 | Topology-first click ordering rule | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Annotation-efficiency tip; heterogeneity likely swamps the universal rule |

## Cluster 9 — VLMs for Dense Prediction (0181–0200): kept 5/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0181 | CLIP dense misalignment is co-occurrence-structured | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | M | 5 | 5 | — | Y | Structural characterization every OV-seg method implicitly assumes; predicts which classes fail |
| 0182 | VLM counting: subitizing breakpoint | 4 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 2 | 5 | 3 | L | 3 | 3 | — | N | VLM counting failures heavily documented by 2026; framing repackages; index overrated (cheap #17) |
| 0183 | Spatial-relation minimal pairs near chance | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 3 | 5 | 4 | L | 5 | 5 | CF | Y | Tests the core value proposition of language-guided segmentation; adversarial filtering |
| 0184 | Term frequency explains OV per-class IoU | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 4 | M | 4 | 4 | — | N | Frequency effects partially shown for OV classification/LVIS tails; almost survived |
| 0185 | Absence benchmark: masks for absent objects | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 5 | 4 | L | 5 | 5 | CF+RM | Y | Refusal as first-class metric; hallucination-as-scene-prior mechanism; cheap |
| 0186 | LLM text tower fixes compositional grounding? | 3 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | M | 4 | 3 | — | N | Text-tower swaps proliferating (LLM2CLIP-era); dissociation angle insufficient |
| 0187 | Negation: worse than chance, fusion failure | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 5 | 4 | L | 5 | 5 | CI+CF | Y | Anti-accuracy is worse than random — a deployment hazard with locatable cause; protected |
| 0188 | Language granularity control nameability law | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Decent; part-annotation coverage limits; loses tiebreak in cluster |
| 0189 | Mask-vs-caption supervision exchange rate | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 4 | 4 | 4 | 3 | M | 4 | 2 | — | N | Training-grid economics; expensive iso-contour fitting |
| 0190 | Attribute-object binding at pixel level | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Binding lit dense (Winoground-era); spatial-competition twist fresh; almost survived |
| 0191 | Visual-token budget scaling for grounding | 4 | 4 | 4 | 4 | 3 | 2 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Token-budget training sweeps costly; resolution/pooling confound; almost |
| 0192 | Reasoning-seg models: salience ablation | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Merged into 0041's causal program (survivor) |
| 0193 | Impossible combinations: composition fails to noun | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Generated-scene artifacts; compositionality genre crowded |
| 0194 | OV benchmark contamination accounting | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | M | 4 | 3 | — | N | Folded into contamination program; 0254 (survivor) delivers the clean instrument |
| 0195 | Verbal confidence ≠ mask quality | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | M | 4 | 4 | — | N | Good interface-safety finding; elicitation-protocol sensitivity; almost |
| 0196 | Ordinal selection: endpoints by salience only | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 5 | 3 | L | 4 | 4 | — | N | Cheap and clean; reviewers may find failure unsurprising; almost survived |
| 0197 | Segment-then-name vs name-then-segment | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Bake-off with routing; instantiation-fairness disputes |
| 0198 | Language as domain-shift regularizer | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Pairing text/label supervision on identical images is hard in practice |
| 0199 | Scene text hijacks grounding | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | L | 4 | 5 | CF | Y | Typographic attacks extended to masks with OCR-capability scaling law; cheap |
| 0200 | Superclass fallback + self-detection | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | L | 4 | 4 | — | N | Practical guardrail; expert GT verification cost; almost survived |

## Cluster 10 — Foundation-Model Representations & Assumptions (0201–0225): kept 6/25

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0201 | Curated subsets beat full corpus for dense | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | M | 4 | 2 | — | N | Pretraining grids costly; mid-scale extrapolation caveat is its own defeater; almost |
| 0202 | Task×backbone frozen-feature matrix | 3 | 5 | 4 | 4 | 4 | 3 | 5 | 5 | 2 | 5 | 4 | L | 4 | 5 | — | Y | Community-resource matrix absorbing 0012/0023; scale confounds stated honestly |
| 0203 | SSL "object emergence" = crop-statistics artifact | 5 | 5 | 5 | 4 | 3 | 2 | 4 | 4 | 4 | 4 | 4 | H | 5 | 4 | HR+CI | Y | Causal intervention on a celebrated narrative; SSL retraining cost is the risk; protected |
| 0204 | Dense vs classification scaling exponents | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Clean model ladders scarce; exponent CIs wide at 4–5 sizes; shares infra with 0202 |
| 0205 | Label-free predictor of the best dense layer | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Useful diagnostic; folklore-to-predictor is engineering-adjacent |
| 0206 | Frequency retention mediates boundary quality | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Decodability-vs-usage gap; the causal intervention arm is expensive |
| 0207 | Data vs method variance decomposition | 4 | 5 | 5 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | H | 5 | 4 | RM | Y | If data dominates, the method-comparison literature needs re-reading; kernel design disputes = magnet |
| 0208 | MIM-vs-contrastive gap under scale | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Multi-scale matched pretraining pairs expensive; extrapolation caveats blunt the verdict |
| 0209 | Compositional bias; recomposition fix | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Nice decomposition; recomposition entangles with object density; almost |
| 0210 | PE extrapolation is structured warping | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | PE-scheme-dependent; analytic correction is engineering payoff |
| 0211 | Texture-vs-shape verdict inverts for dense readouts | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | CI | Y | Within-model dissociation would invalidate classification-probe bias claims for segmentation |
| 0212 | Patch-level linear attribute directions | 4 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Patch attribute GT scarce; class-entanglement likely; tool-flavored |
| 0213 | Resolution debt unrepayable by adaptation | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Matched-compute accounting across schedules is treacherous; pretraining pairs costly; almost |
| 0214 | Dedup effects on dense endpoints | 3 | 3 | 3 | 4 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | M | 3 | 2 | — | N | Pretraining-grid economics for a secondary pipeline question |
| 0215 | Patch metric anisotropy + local whitening | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | NLP-anisotropy port; the correction is an incremental method |
| 0216 | Adversarial map of VFM universality boundary | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Task-curation invites cherry-picking disputes; specialist-budget fairness hard |
| 0217 | Do model soups work for segmentation? | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 2 | 4 | 3 | L | 3 | 3 | — | N | Dense-soup variants likely explored by 2026; recipe payoff |
| 0218 | Dense "emergence" = thresholded-metric artifact | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | LLM-critique replication flavor; dense model ladders sparse; almost |
| 0219 | Provenance bias of model-assisted benchmarks | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | H | 5 | 4 | — | N | Folded into 0029's contamination program; scratch-annotation cost shared there |
| 0220 | Encoder/decoder allocation law | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | M | 4 | 2 | — | N | Giant budget sweep; "task distance" operationalization fragile |
| 0221 | Video pretraining → better static boundaries? | 4 | 4 | 4 | 4 | 2 | 2 | 3 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Matching data quantity across video/image regimes is definitionally hard |
| 0222 | Token importance anti-correlated across tasks | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | L | 4 | 4 | — | N | Strong practical stakes; profiles may only partially decorrelate; almost survived |
| 0223 | In-context segmentation: abstraction or copying? | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | CI | Y | Mechanism dissociation for visual ICL; predicts generalization limits either way; protected |
| 0224 | Dense degrades first under quantization | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Deployment-useful; PTQ-method dependence; mixed-precision fix is recipe work; almost |
| 0225 | Platonic convergence is semantics-only at patch level | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | RM | Y | Tests a hot theory exactly where it should break; affine-alignment design clean; magnet |

## Cluster 11 — Valuable Negative Results & Falsification (0226–0245): kept 5/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0226 | Attention-U-Net gains are baseline artifacts | 4 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 5 | 4 | M | 5 | 4 | RM | Y | Powered replication of the field's most common paper template; author-pushback magnet |
| 0227 | Boundary-loss equivalence audit | 3 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 3 | 4 | 3 | M | 3 | 3 | — | N | Folded into 0165's sharper decomposition (itself a near-miss); TOST grid heavy |
| 0228 | Generative aug vs tuned classical aug | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Strong null candidate; generator quality is a moving target; 0284/0285 family carries synthetic |
| 0229 | Multi-scale TTA is dead on modern ViTs | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 4 | 3 | L | 4 | 4 | — | N | Cheap and useful; 0100 owns the harmful-TTA slot with a sharper instance; almost |
| 0230 | Self-training rounds = compute laundering | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | The equal-compute control the lit skips; conclusion likely benchmark-dependent; almost |
| 0231 | Adapter zoo ≈ LoRA at matched budgets | 3 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Reimplementation labor + fairness disputes; PEFT slots taken by 0055/0072 |
| 0232 | Frequency modules = augmentation substitutes | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Niche module family; interaction design fine but stakes small |
| 0233 | Deep supervision vestigial under modern recipes | 3 | 3 | 4 | 4 | 4 | 3 | 5 | 5 | 3 | 4 | 3 | L | 3 | 3 | — | N | Useful hygiene; workshop-scale finding either way |
| 0234 | Pixel-contrastive gains = budget effect | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | One controlled comparison; conceptually folded into 0334's compute-matching genre |
| 0235 | Distillation temperature is a dead knob | 3 | 2 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 2 | L | 2 | 2 | — | N | Dead-knob nulls are workshop notes unless the knob is load-bearing |
| 0236 | Curriculum effects don't survive seeds | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Powered null valuable but curriculum already low-credibility for dense |
| 0237 | Targeted vs generic data collection | 4 | 5 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | M | 4 | 3 | — | N | Applied stakes high; collection logistics dominate and resist standardization |
| 0238 | Depth auxiliary vs semantically-empty auxiliary | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | CI | Y | The empty-auxiliary control is a sharp new instrument for all multi-task synergy claims |
| 0239 | Entropy TTA silently collapses rare classes | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | L | 5 | 5 | CF | Y | Average metrics hide the harm; predictive triggers; safety-relevant and cheap |
| 0240 | Architectural ensemble diversity ≈ seed diversity | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | OOD-conditional wrinkle nice; classification-era analogues strong |
| 0241 | Sub-pixel jitter is placebo | 2 | 2 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 2 | L | 2 | 2 | — | N | Recipe-hygiene note; smallest stakes in the cluster |
| 0242 | Publication-bias z-curve for segmentation deltas | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | M | 5 | 5 | RM | Y | A measured selection-bias coefficient for the field; psychology methods ported honestly |
| 0243 | Detection warm-starts obsolete vs SSL | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Checkpoint-quality confounds; the habit is already fading |
| 0244 | Dice+CE default audit | 3 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 3 | 4 | 3 | L | 4 | 4 | — | N | Absorbed by 0097's calibration-first design (survivor); designs share compute |
| 0245 | 2015 U-Net + 2026 recipe closes the decade gap | 5 | 5 | 5 | 4 | 4 | 3 | 5 | 5 | 4 | 5 | 5 | M | 5 | 5 | RM | Y | The decade-attribution audit; "ResNet strikes back" for segmentation; batch flagship |

## Cluster 12 — Few-Shot & Zero-Shot Segmentation (0246–0260): kept 3/15

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0246 | FSS scores = base-class proximity | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 4 | 4 | L | 5 | 5 | CF | Y | Split-geometry confound quantified + max-distance re-splits; cheap and decisive |
| 0247 | Frozen-VFM matching beats FSS architectures | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 2 | 4 | 4 | L | 4 | 4 | — | N | Matcher-class training-free results already published the core claim; almost survived |
| 0248 | Positive-vs-negative support information value | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 3 | M | 3 | 3 | — | N | Needs negative-accepting architectures; composition rule is interface tweak |
| 0249 | Zero-shot gap is mostly boundary-side | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | L | 4 | 4 | — | N | OV+SAM refinement pipelines already imply the answer |
| 0250 | Meta-training loses to direct 5-shot fine-tuning cross-domain | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | L | 5 | 5 | CF | Y | Existence test for a subfield; fixed-recipe honesty; cheap to run |
| 0251 | Prototype failure tracks class multimodality | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Nice quantitative law; embedding-dependence; loses cluster tiebreak |
| 0252 | Support selection matters more than model choice | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Good factor-importance design; LLM analogue makes the outcome guessable |
| 0253 | GFSS frontiers are method-invariant | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 3 | — | N | Frontier methodology sound; GFSS audience narrow |
| 0254 | Provably-novel synthetic zero-shot benchmark | 5 | 5 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | H | 5 | 4 | RM | Y | The contamination-proof instrument (absorbs 0194/0333); difficulty calibration is the hard part |
| 0255 | Support-noise robustness matrix | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Deployment note; synthetic-corruption realism caveat |
| 0256 | FSS fails on dense repetition | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Industrial relevance real; benchmark construction dominates the work |
| 0257 | Supports: semantic or appearance allegiance? | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Clean dissociation, but 0223 runs the same logic on the stronger target; almost |
| 0258 | System-nominated supports | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Active-learning-adjacent method work |
| 0259 | Marginal value of text atop 5 shots | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Good decomposition; conclusions likely model-family-specific |
| 0260 | Human ambiguity floor of 1-shot task | 4 | 4 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | — | N | Ambiguity-floor family already served by 0103/0336/0337; human-study cost; almost |

## Cluster 13 — Weakly-, Semi- & Self-Supervised (0261–0280): kept 4/20

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0261 | WSSS gap is structural extent error | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 3 | 4 | 4 | M | 5 | 5 | RM | Y | Paradigm-exhaustion verdict via oracle substitution; ends or redirects a subfield |
| 0262 | Point-supervision value curve saturates at 3–5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Decision-relevant curve; annotation-economics family trimmed to strongest; almost |
| 0263 | Time-normalized supervision-form ranking | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Human timing studies + tool-UX dependence; almost |
| 0264 | Confirmation-bias dynamics are forecastable | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Good longitudinal design; intervention payoff indirect; almost |
| 0265 | Consistency augmentations teach false invariances | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Class-taxonomy subtlety; menu pruning is recipe work |
| 0266 | Object discovery or texture grouping? | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 4 | 4 | CI | Y | Dissociation-scene audit of "unsupervised objects"; perception-science instrument; protected |
| 0267 | Students inherit SAM's error signature | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 5 | 5 | — | Y | Concrete inheritance measurement for the dominant pseudo-labeler; completes 0029's program |
| 0268 | CAM pipelines vs VLM grounding showdown | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 3 | M | 4 | 3 | — | N | Head-to-head likely published in parts by 2026; vocabulary wrinkle small |
| 0269 | Classical priors subsumed by feature affinity? | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 3 | 3 | — | N | Pipeline-hygiene audit; exception map niche |
| 0270 | SAM×CLIP pseudo-label error decorrelation | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Useful co-training anatomy; payoff mostly feeds method work |
| 0271 | Minority-class drift law in self-training | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Law-fitting nice; the correction is a method; augmentation interaction risk |
| 0272 | Domain-SSL crossover scale law | 4 | 4 | 4 | 4 | 3 | 2 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Valuable pricing curve; SSL ladders expensive; recipe-dependence |
| 0273 | Alt-text noise taxonomy: type beats rate | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Type-differential damage plausible; injection-realism caveat |
| 0274 | Exemplar value is predictable a priori | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Reproducibility service; sweep cost; proxy-fidelity risk |
| 0275 | Flow SSL teaches over-grouping of articulated parts | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Sign-prediction design good; matched pretraining arms costly; almost |
| 0276 | Label-free stopping for pseudo-labeling | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Honest-information framing; churn signals likely architecture-dependent |
| 0277 | Verify-vs-annotate budget split law | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Applied economics; simulation realism gates the claim |
| 0278 | Mask-MAE prior from unpaired mask archives | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Genuinely novel resource; method-flavored; convention-encoding risk (cf. 0007); almost |
| 0279 | Taxonomy merging as partial-label learning | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Union test-set labor; partial-label literature adjacent |
| 0280 | Uncertainty routes labels to the wrong pixels | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | L | 5 | 5 | CI+CF | Y | Attacks a productized assumption with a cheap simulation; confident-error angle; protected |

## Cluster 14 — Synthetic Data & Generative Training (0281–0295): kept 3/15

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0281 | Noise floor of generation-derived masks | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Structured-noise anatomy folded into the 0283/0285 program; almost |
| 0282 | Synthetic-fraction inverted-U phase transition | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Curve mapping subsumed: 0285 tests the sharpest slice with a usable safety rule |
| 0283 | Which realism factor buys sim-to-real transfer | 4 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 5 | 4 | — | Y | Budget-reallocating factor attribution; the 2⁴ factorial is honest causal design |
| 0284 | Generative augmentation amplifies dataset bias | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | M | 4 | 4 | — | N | Direction-of-effect question good; bias metrics need construction; almost |
| 0285 | Synthetic rare-class fix inverts above ~70% fraction | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | M | 5 | 5 | CI | Y | The fix fails exactly where aimed; within-class threshold is a deployable safety rule |
| 0286 | Copy-paste realism: region vs boundary resolution | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Metric-decomposed resolution nice; the controversy is niche |
| 0287 | Procedural beats diffusion on web-sparse phenomena | 4 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | M | 5 | 4 | — | Y | Exposes the circularity limit of generative augmentation; anchors smoke-program data |
| 0288 | Dense model-collapse dynamics | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 2 | 4 | 4 | M | 4 | 4 | — | N | Model-collapse literature racing; the dense version likely claimed by 2026; almost |
| 0289 | Can synthetic test sets rank models? | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Screening-vs-fine-ranking result useful; hostage to suite quality |
| 0290 | Physics-fidelity attribution for smoke/fire data | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Folded into 0283's factor logic at the physics level + the 0122 program |
| 0291 | Real-geometry-conditioned generation | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Practical middle path; condition-quality sensitivity; method-flavored |
| 0292 | Privacy-synthetic data deletes fine structures | 4 | 5 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | M | 4 | 3 | — | N | Policy stakes real; privacy-strength quantification fragile across generators |
| 0293 | Breadth vs depth in domain randomization | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Allocation question decent; budget units fuzzy |
| 0294 | Differentiable-rendering as a labeling instrument | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Regime map useful; silent fit failures; engineering-heavy |
| 0295 | Sequential vs mixed synthetic-real training | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | L | 4 | 3 | — | N | Gap-conditioned rule plausible; recipe-tuning fairness dominates |

## Cluster 15 — Domain Adaptation & Distribution Shift (0296–0310): kept 3/15

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0296 | UDA rankings scramble on fresh pairs | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | M | 5 | 5 | RM | Y | Ranking-transfer verdict on a decade of UDA; frozen-hyperparameter honesty; magnet |
| 0297 | Style/content gap decomposition per benchmark | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Diagnostic value folded into the 0296+0304 program; almost |
| 0298 | TTA collapse detector + rollback | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Methodsy sibling of 0239 (survivor); detect-and-rollback is engineering |
| 0299 | SFDA privacy claim leaks through weights | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Attack-strength bounds the claim; security venue better fit |
| 0300 | Frozen DINOv2 beats the UDA literature | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 1 | 4 | 3 | L | 4 | 3 | — | N | Rein/DGSS-era results already ran this confrontation; index overrated it (surprising #2) |
| 0301 | Continual DA thrashes under cyclic domains | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Recurrence protocol is genuinely new eval science; data assembly heavy; almost |
| 0302 | Do domain-gap measures predict anything? | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | 30-pair assembly is the real cost; the task-aware predictor is a method |
| 0303 | Norm-recovery fraction as shift-tier diagnostic | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | L | 4 | 5 | CF | Y | Minutes-cheap tier diagnostic; generalizes 0065 beyond medical; immediately adoptable |
| 0304 | Fourier-swap success as gap spectroscopy | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Clever trick-to-instrument move; window-size sensitivity; near-miss to 0296/0303 |
| 0305 | Night vision: adaptation gap or information deficit | 4 | 5 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 4 | CI | Y | Human-ceiling decomposition splits fixable from unfixable; sensor-vs-model verdict |
| 0306 | Physics-anchored rain/fog robustness curves | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Regulator-grade framing; real-weather validation data scarce |
| 0307 | UDA corrupts under label-space mismatch | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Deployment warning useful; open-set-DA adjacency lowers novelty |
| 0308 | Multi-source: diversity or just quantity? | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Matched-total control good; conclusion may be spread-metric-dependent |
| 0309 | Geographic bias decomposition for driving | 4 | 5 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Equity stakes; diverse labeled data scarcity gates the decomposition |
| 0310 | Modality statistics predict adapter sufficiency | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Predictive criterion nice (generalizes 0113); adapter-capacity confounds; almost survived |

## Cluster 16 — Object Detection Failure Modes (0311–0325): kept 2/15

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0311 | Query niche gaps predict misses | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Good mechanism; DETR query analyses accumulating; the fix is method work |
| 0312 | NMS distorts calibration density-dependently | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Density-conditioned recalibration useful; detection-calibration niche; almost |
| 0313 | Resolution beats small-object architecture remedies | 4 | 5 | 4 | 4 | 4 | 3 | 5 | 5 | 3 | 4 | 4 | M | 5 | 5 | RM | Y | Compute-matched confrontation re-baselines a subfield; pairs with 0161; magnet |
| 0314 | OV hallucination grows asymmetrically under shift | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Extends 0185 (survivor) to detection; folded into that program |
| 0315 | Long-tail failure is also localization | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | TIDE-style decomposition; plausible but incremental analysis genre |
| 0316 | Learned suppression fails to extrapolate to crowds | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Predictable-vs-unpredictable failure framing good; composited-crowd caveat; almost |
| 0317 | COCO re-annotation compresses modern rankings | 3 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 2 | 4 | 4 | M | 4 | 3 | — | N | COCO-ReM-style re-annotation efforts already published the core result; almost |
| 0318 | Anchor-based vs anchor-free: dead distinction | 3 | 3 | 3 | 4 | 4 | 3 | 5 | 5 | 3 | 4 | 3 | L | 3 | 3 | — | N | Distinction already faded; equivalence audit is tidy-up work |
| 0319 | Boxes are the wrong primitive for amorphous targets | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 4 | — | Y | Output-primitive science judged on downstream decisions; completes the smoke program |
| 0320 | Detector features lack instance identity | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Information-audit logic strong; tracking lit already probes embeddings; almost |
| 0321 | Detectors implicitly learn amodal extent | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 3 | — | N | Cute discovery claim; regression-smoothing confound |
| 0322 | Train-test resolution transfer law + cheap fix | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Practical law; FixRes lineage makes it maintenance science |
| 0323 | Convention mismatch inflates cross-dataset drops | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Convention-translation instrument nice; capacity policing subtle |
| 0324 | Detection→density crossover is stride-predictable | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Predictable crossover useful; counting audience small at CV venues |
| 0325 | Deblurring pays a hallucination tax | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | M | 4 | 4 | — | N | Safety-negative genre; restoration-vs-robustness literature adjacent |

## Cluster 17 — Evaluation Methodology & Benchmark Science (0326–0340): kept 3/15

| ID | One-line | Nov | Sig | SciQ | Tech | Feas | Cmp | Dat | Bas | Unp | Clr | Ven | Rsk | Up | ROI | Prot | Srv | Reason |
|----|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|------|-----|--------|
| 0326 | Benchmark seed-noise reference tables | 3 | 5 | 3 | 4 | 3 | 2 | 5 | 5 | 3 | 5 | 4 | L | 5 | 4 | — | N | High-leverage infrastructure; 600-run compute; venues treat it as resource; almost |
| 0327 | Benchmark-death criterion + lifecycle report | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 4 | — | N | Strong framing; re-annotation cost shared with 0091 (survivor), which carries the core |
| 0328 | Simulated-click protocol validity | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | The protocol-validity study interactive seg needs (absorbs 0048); user-study variance; almost |
| 0329 | Validated metric-selection decision tree | 3 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 3 | M | 4 | 3 | — | N | Prescription instrument; archetype construction subjective |
| 0330 | Baseline drift across the literature | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 3 | M | 4 | 3 | — | N | Comparability-failure documentation; overlaps the 0326/0331/0334 program |
| 0331 | What fraction of SOTA claims survives paired tests | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | L | 5 | 5 | — | N | Cheap and damning; 0340 delivers the same verdict with even less compute; almost |
| 0332 | Leaderboard adaptive-overfitting dose-response | 4 | 4 | 4 | 4 | 3 | 4 | 2 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Fresh-split construction heavy; classification precedents strong |
| 0333 | Contamination-adjusted zero-shot scores | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | M | 5 | 4 | — | N | Strong deliverable; 0254 (survivor) provides the cleaner instrument for the same claim |
| 0334 | Compute-inflation coefficient of the literature | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | M | 5 | 4 | — | N | 30-method reproduction is a consortium's work, not one paper's |
| 0335 | Worst-class metrics reorder leaderboards | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | L | 4 | 4 | — | N | Useful re-scoring; fairness-metrics port; less novel than 0340's fiction-fraction |
| 0336 | Human floors/ceilings for segmentation benchmarks | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | M | 5 | 5 | CI | Y | The missing anchor of dense evaluation; "superhuman" becomes measurable; protected |
| 0337 | Annotation instructions as an experimental treatment | 5 | 5 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | M | 5 | 4 | RM | Y | GT is instruction-contingent at SOTA-gap scale — new methodology; crossover design; magnet |
| 0338 | Do corruption benchmarks predict real degradation? | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | M | 4 | 3 | — | N | Proxy-validity question good; paired real-degradation data scarce |
| 0339 | FLOPs-latency divergence re-ranks efficient models | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | L | 4 | 4 | — | N | Deployment-useful audit; systems-venue flavor |
| 0340 | Bootstrap the leaderboards: fiction fraction | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 5 | 4 | L | 5 | 5 | CF | Y | Zero-model-run re-analysis; the fiction-fraction is a headline number; cheapest idea in batch |

---

## Final tally

**73 survivors / 340 (21.5%).** Per cluster: C1 7/30 · C2 4/20 · C3 4/25 · C4 3/15 · C5 6/30 · C6 6/20 · C7 4/20 · C8 5/20 · C9 5/20 · C10 6/25 · C11 5/20 · C12 3/15 · C13 4/20 · C14 3/15 · C15 3/15 · C16 2/15 · C17 3/15.

**Survivor IDs:**
0001, 0003, 0006, 0007, 0013, 0021, 0029 · 0031, 0033, 0041, 0049 · 0055, 0058, 0067, 0072 · 0076, 0078, 0089 · 0091, 0093, 0097, 0100, 0103, 0118 · 0121, 0122, 0123, 0125, 0126, 0128 · 0141, 0142, 0154, 0157 · 0161, 0166, 0170, 0174, 0176 · 0181, 0183, 0185, 0187, 0199 · 0202, 0203, 0207, 0211, 0223, 0225 · 0226, 0238, 0239, 0242, 0245 · 0246, 0250, 0254 · 0261, 0266, 0267, 0280 · 0283, 0285, 0287 · 0296, 0303, 0305 · 0313, 0319 · 0336, 0337, 0340.

**Protected sets among survivors:** HR (high-risk/high-reward, 10): 0029, 0041, 0058, 0067, 0089, 0093, 0122, 0125, 0141, 0203. CI (simple-but-counter-intuitive, 25): incl. 0001, 0013, 0021, 0033, 0049, 0055, 0078, 0100, 0103, 0118, 0123, 0142, 0157, 0166, 0170, 0176, 0187, 0211, 0223, 0238, 0266, 0280, 0285, 0305, 0336. RM (reviewer-disagreement magnets): 0007, 0029, 0031, 0055, 0067, 0072, 0076, 0091, 0093, 0097, 0121, 0126, 0161, 0185, 0207, 0225, 0226, 0242, 0245, 0254, 0261, 0296, 0313, 0337. CF (cheap-to-falsify): 0003, 0013, 0021, 0031, 0033, 0049, 0100, 0123, 0128, 0154, 0174, 0183, 0185, 0187, 0199, 0239, 0246, 0250, 0280, 0303, 0340. Unprotected merit survivors: 0181, 0202, 0267, 0283, 0287, 0319.


