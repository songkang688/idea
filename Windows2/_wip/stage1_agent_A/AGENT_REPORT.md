# Windows2 Stage 1 — Agent A Report

Agent: Cloud Sub-Agent A (claude-fable-5-thinking-xhigh), exclusive angle clusters 1–10 (SAM/segmentation failure science; PEFT/VFM-tuning and detection/eval angles left to other agents).

## Counts

- **Total ideas: 352** (target ≥340). IDs `W2-A-0001`..`W2-A-0352`, sequential, machine-validated (JSON parse, required fields, unique/sequential IDs, parent references, near-duplicate one-liner screen at token-Jaccard 0.65 — zero flags).
- 14 clusters, 25 ideas each (C14 has 27). See `clusters.md`.
- 61 ideas carry `mutate_from` links (deliberate mutations of earlier ideas rather than hidden duplicates).

## Duplicates killed internally

Killed or merged during generation (details in `clusters.md`, merge/mutate notes):

- ~10 early drafts violating the hard rules (module-A+B, "apply to medical", loss/backbone/attention tweaks, "SAM + dataset X") were discarded before writing.
- 5 near-duplicate pairs resolved by scope-splitting with explicit `mutate_from` links (clinician vs crowdworker clicks; ignore-region audit vs census; OV confidence dilution vs OV evaluation protocol; glass frame-reliance vs interior-blindness corollary; smoke annotation-variance vs alpha-threshold psychophysics).
- 3 ideas killed outright as weak or out-of-scope (polarization-for-camouflage, gamified annotation, audio-glass).

## 20 most surprising ideas (my ranking)

1. **W2-A-0145** Findability bias: COD datasets contain only camouflage that FAILED; telemetry-verified camera-trap evaluation can bound the unmeasurable selection bias.
2. **W2-A-0334** "Class-agnostic" masks leak semantics: shape alone recovers categories and scenes — privacy and framing consequences.
3. **W2-A-0339** 3D may be intrinsically EASIER than 2D per supervision bit — the field's difficulty intuition could be an accounting artifact.
4. **W2-A-0206** SAM fingerprint forensics: assisted datasets carry detectable boundary-style signatures that future models inbreed on.
5. **W2-A-0107/0114** Depth-sensor dropout and LiDAR-camera disagreement as free, fleet-scale glass annotation — a sensor weakness converted into a data engine.
6. **W2-A-0028** SAM2 teleport test: under temporal sparsity, memory attention may degrade into a location prior (follows the place, not the object).
7. **W2-A-0341** Prompt sensitivity may INCREASE with scale on ambiguous objects — scale changes the character of instability, not its amount.
8. **W2-A-0097** Heat shimmer as a segmentable phenomenon: objects visible only through their refraction field, potentially preceding visible smoke.
9. **W2-A-0239** Deliberately recompressing deployment inputs toward training statistics may IMPROVE accuracy — inverted compression shift.
10. **W2-A-0175** Metrology-grade boundary ground truth from photographed printed shapes — sub-annotation-noise boundary science becomes possible.
11. **W2-A-0148** Binary masks may be the WORST output format for human-AI camouflage search (anchoring-induced misses) despite being the field's standard.
12. **W2-A-0331** Dice's per-instance gradient starvation measured directly — a mechanistic, instrument-level explanation for chronic small-lesion misses.
13. **W2-A-0272** Layered design files (PSDs) as a giant untapped corpus of professional-grade masks with different economics than annotation.
14. **W2-A-0198** Seed-churn atlases: retraining randomness reproduces human-disagreement maps for free and audits published gains.
15. **W2-A-0075** Consensus label fusion structurally erases the minority expert who is right about rare pathology — outcome-anchored test.
16. **W2-A-0326** More context can HURT boundary precision — a monotonicity assumption embedded in a decade of architecture design, testable in a week.
17. **W2-A-0022** The prompt-Jacobian of SAM as a label-free boundary-ownership detector — differentiation with respect to the prompt as a new readout channel.
18. **W2-A-0352** Many "segmentation" applications may not need masks at all: direct scalar regression as the honest baseline for measurement tasks.
19. **W2-A-0343** Relational grounding gap: compositional queries ("the handle of the second cup from the left") likely collapse to bag-of-words — a missing capability layer, not a performance gap.
20. **W2-A-0110** The same window flips optical class between day (transmissive) and night (mirror) — a physics-forced diurnal domain shift inside a single scene.

## 10 cheapest killer experiments

Each needs roughly a GPU-day or less plus public data/checkpoints; all can falsify their hypothesis decisively.

1. **W2-A-0034** Apply model-free temporal smoothing to frozen VOS predictions; if J&F rises, the metric partially rewards smoothness style. (Hours.)
2. **W2-A-0021** AUROC of SAM head-disagreement vs predicted-IoU for failure detection on 5 shifted datasets. (One GPU-day.)
3. **W2-A-0326** Attention-radius masking sweep on trained models: sign of context's marginal value per output property. (One GPU-day.)
4. **W2-A-0152** Re-score public checkpoints with size-stratified metrics; check whether 5 years of gains exist in the smallest decile. (Inference only.)
5. **W2-A-0160** Fit one morphological offset per class on validation; measure boundary-metric recovery on test. (Hours.)
6. **W2-A-0018** JPEG-quality sweep + boundary-position phase histograms modulo 8 px: grid-snapping forensics. (Hours.)
7. **W2-A-0191** Correlate top-2 logit margin maps with annotator-disagreement maps vs deep-ensemble maps on multi-rater data. (One GPU-day.)
8. **W2-A-0322** Literature-only: compile cross-paper score spreads for identical model-benchmark pairs; publish the reproduction noise table. (No GPU.)
9. **W2-A-0099** Mask fire pixels at test time; retained accuracy measures auto-exposure/global-cue shortcut. (Hours.)
10. **W2-A-0045** Budget-matched simulation: one perfect frame-0 mask vs the same human-seconds as sparse clicks across the video, with SAM2. (One GPU-day.)

## Risks of bias in my batch

1. **Audit-heavy skew.** A large share of ideas are measurement/audit studies (benchmarks, annotation noise, metric validity) rather than new capabilities. This reflects my judgment that the field's references are its weakest layer, but a portfolio built only from my batch would under-invest in constructive methods. Stage 2 should balance against other agents' batches.
2. **"X is partly annotation noise" template overuse.** The pattern appears in many clusters (boundaries, tails, domain gaps, medical ceilings). Each instance is independently falsifiable, but if the template's core premise is weaker than I believe, a correlated block of ideas devalues together — a common-mode risk.
3. **SAM-centrism.** Clusters C01/C02 and several others assume promptable-segmentation remains the dominant paradigm. If the field pivots (e.g., to MLLM-native dense outputs), some failure-mode science becomes archaeology. Partially hedged by C12/C14.
4. **Human-study bottlenecks.** Many ideas need psychophysics or annotator studies (0065, 0126, 0148, 0155, 0188, 0201, 0215, 0223, 0336, 0351). I may underestimate their logistical cost; a batch selected for cheapness should draw from the GPU-only subset.
5. **Physics optimism.** The physics-channel family (polarization, thermal, parallax, caustics, shimmer, shadow-alpha) assumes controlled capture is available; several are prospective (new sensors) rather than retrospective (existing imagery), limiting immediate benchmark impact.
6. **Novelty is self-assessed.** Per instructions I did no literature search; every idea is tagged "UNVERIFIED — needs lit search" where relevant, and only high-confidence prior work is tagged KNOWN (e.g., Eulerian magnification, registers/attention-sinks, FDA, LVIS federated design, label-error and adaptive-overfitting literatures, DINO emergence, probabilistic U-Net line, clDice). Some fraction of the 352 — I would guess 15–30% — will collapse into existing work on a serious search. That attrition is expected at Stage 1 and is what Stage 2 filtering is for.
7. **Anglophone/web-data lens.** Dataset-bias ideas (geography, aesthetics) are framed from the public English-web benchmark ecosystem; other data ecosystems (industrial, non-Western medical) may have different failure structures my batch does not capture.

## File inventory

- `Windows2/_wip/stage1_agent_A/ideas.md` — rendered catalog (352 ideas).
- `Windows2/_wip/stage1_agent_A/ideas.jsonl` — canonical machine-readable catalog (one JSON object per line).
- `Windows2/_wip/stage1_agent_A/clusters.md` — cluster map, merge/mutate notes, cross-cluster threads.
- `Windows2/_wip/stage1_agent_A/AGENT_REPORT.md` — this report.
- `Windows2/_wip/stage1_agent_A/parts/c01.jsonl`..`c14.jsonl` — source-of-truth cluster files.
- `Windows2/_wip/stage1_agent_A/build_catalog.py` — assembler/validator (run: `python3 build_catalog.py`).
