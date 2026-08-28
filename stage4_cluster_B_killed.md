# Stage 4 — Cluster B Kill List (12 killed)

Reviewer #2 kills among the Stage-3 Cluster B survivors. Full attack text in `stage4_cluster_B_attacks.md`.
Kill standard: no realistic experiment can answer the strongest attack.

| # | ID | Idea (one line) | Kill reason (strongest unanswerable attack) |
|---|----|-----------------|---------------------------------------------|
| 1 | B-0058 (P) | MoE routing as free pathology detector | Scale/confound dilemma: small-scale null says nothing about FM-scale emergence; small-scale positive is confounded by acquisition-specialization (idea's own risk). Must also beat the engineered MoE-AD wave (AnomalyMoE, MoECLIP, ReMoE, REN — searched). No affordable experiment answers both. |
| 2 | B-0062 | Physically calibrated per-pixel smoke transmittance GT | Benchmark-validity circularity: the field-transfer claim can only be verified with field-scale dense GT — the thing whose absence motivates the dataset. Glycol-vs-combustion optics and multiple-scattering/path-radiance regime gaps unresolved; heavy capture rig for a lab-bound result. Closest call — revivable if rescoped as a lab-physics benchmark without the field claim. |
| 3 | M2 (B-0069) | Soft-boundary metric validation arm | Dies with host B-0062; Stage 3 already judged it too thin standalone. |
| 4 | B-0193 | Speckle-native SSL for ultrasound | Signal destroyed in obtainable data (clinical B-mode is speckle-filtered/log-compressed; public RF corpora too small for matched-compute SSL claims). Pretext predicts a deterministic, locally computable statistic — solvable by a filter bank, so even a positive is uninterpretable. |
| 5 | B-0285 | Rare anatomical variants long-tail benchmark | Curation is the unsolved cost and the result can't ship (privacy/licensing of case-report imagery); n≈10 per variant is anecdote-level power; headline is what every reviewer already believes; flagger is established atlas-consistency machinery. |
| 6 | B-0344 | Dose maps as inverse contour supervision | Structural identifiability failure: dose gradients sit at PTV margins (systematic 5–10 mm protocol-specific offset from anatomy — teaches the margin, not the organ), beam apertures, and constraint surfaces that bind only near targets; distal anatomy gets zero signal. The minimal experiment cannot distinguish success from its own failure mode. |
| 7 | B-0350 | Suggestion-induced hallucination benchmark for medical segmentation | Direct prior-work hit found this session: MedVeriSeg-Bench (arXiv 2604.10242) — absent-target queries for text-prompted medical segmentation, 24 modalities/151 entities, plus training-free rejection mitigation; HEAL-MedVQA (IJCAI 2025) covers the VQA side. Remaining deltas are follow-ups, not a program. Negation substance survives as B-0331. |
| 8 | B-0353 (P) | Doppler audio as vessel supervision | Dominated: color-Doppler-*image* weak supervision for vessel segmentation is published (ISBI 2023; DopUS-Net), and gate audio is a strict information subset of the dense color-Doppler map from the same exam. No paired audio+B-mode dataset exists (searched); prospective collection inherits operator selection bias. |
| 9 | B-0361 | Ambiguity handling as transferable skill | Decisive experiment cannot exist: requires multi-rater GT across ambiguity domains whose planned collection (B-0070 line) was killed. Unremovable confound: boundary-width statistics alone predict cross-domain "uncertainty transfer." Stage-3 novelty confidence already medium-low. |
| 10 | M1 (B-0007) | Mirror-Cost flipping audit | Conceded low ceiling (Stage 3's own words); outcome is folklore confirmation; effect size predicted to vanish at modern model scale by the idea's own risk statement. Workshop note, not a slot. |
| 11 | M3 (B-0078) | Tone-mapping destroys fire evidence | Decisive experiment unrealistic: paired RAW/HDR capture of real fires + matched confusers at benchmark diversity is a regulated, expensive campaign yielding demo-scale n. Attribution confound (temporal flicker vs radiometry) survives even a positive result. |
| 12 | M6 (B-0366) | Calibrated annotation-collapse simulation | Calibration theater: 1–2 published scalars (OSAIRIS catch rates) don't constrain the behavior model that determines every conclusion; the deliverable (stabilizing blind-case ratio) is unvalidatable — no generation-2+ data exists or can be created in scope. |

**(P)** = was PROTECTED. Protected kills this round: B-0058, B-0353 — protection not honored where the
strongest attack has no experimental answer, consistent with Stage-3 precedent.

## Kill pattern summary

- **No realistic decisive experiment:** B-0058 (scale/confound dilemma), B-0353 (no data, dominated baseline),
  B-0361 (required GT doesn't exist), M3 (capture campaign), M6 (unvalidatable simulation).
- **Structural bias the experiment can't see:** B-0344 (margin-shaped supervision).
- **Validity circularity:** B-0062 + M2 (field claim needs the GT being proposed).
- **Signal unavailable in obtainable data / trivial pretext:** B-0193.
- **Underpowered + unshippable + predictable:** B-0285.
- **Direct fresh prior-work hit:** B-0350 (MedVeriSeg-Bench, HEAL-MedVQA).
- **Conceded ceiling:** M1.
