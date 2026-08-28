# P1 Diversity Audit — Auditor B (Hypothesis Quality / Blind Spots / Constructive Balance)

- **task_id:** p1_diversity_audit_w1
- **role:** auditor_B_quality_blindspots (independent of Auditor A; A's shard read only AFTER forming own notes)
- **windows:** Windows13 (windows_path Windows13, window_locked true)
- **audited set:** `Windows13/_state/ideas_master.jsonl` (248 records) on `origin/cursor/p1-wave-b-consolidator-w1-7a58` (commit 936670f)
- **audited_at_utc:** 2026-08-28T19:26:01Z
- **method:** deterministic regex/count analysis over all fields of all 248 records, plus manual read of all 248 one-liners and spot-reads of full records (A-001, A-008, B-002, C-010, and others). Hand-labeled constructive-capability classification. No records modified. `ideas_master.jsonl`, `research_state.json`, `window.lock.json` untouched.

---

## 1. Hypothesis-quality audit

### 1.1 Field completeness — STRONG

All 12 substantive text fields (`one_line_idea`, `problem`, `core_hypothesis`, `falsifiable_prediction`, `why_important`, `why_possibly_novel`, `minimal_falsification_experiment`, `main_risk`, `community_default_belief`, `why_it_might_be_wrong`, `fastest_falsification_experiment`) are present and non-trivial (>20 chars) on **248/248** records. Zero empty or stub fields. Zero exact/near-duplicate one-liner prefixes.

The contrarian triple the wave was commissioned for — community_default_belief + why_it_might_be_wrong + fastest_falsification_experiment — is **complete on all 248 records**. [EVIDENCE: field scan]

### 1.2 Evidence-labeling schema is INCONSISTENT across shards — top structural defect

- **94/248** records (all of gen_a) carry the structured `evidence_label` dict with per-claim labels including `prior_work_basis`.
- **154/248** records (all of gen_b and gen_c) instead use inline `[HYPOTHESIS]` / `[EXPECTED RESULT]`-style tags inside field text and have **no** `evidence_label` object.

Both conventions do label speculation, so this is not a fabrication risk, but a downstream ranking stage that reads `evidence_label` programmatically will silently treat 62% of the portfolio as unlabeled. **Consolidator should normalize before Stage 2.** [EVIDENCE]

### 1.3 Falsifiability — directionally good, numerically weak

- **0/248** falsifiable_predictions contain hedge words (may/might/could) — predictions are stated crisply. [EVIDENCE]
- Spot-reads confirm predictions are genuinely directional (e.g., A-008 "stable dominance curve … statistically distinct curves", C-010 "reduce measured overconfidence … more than for weaker ones").
- **BUT only 4/248 (1.6%)** predictions state a numeric kill threshold. The portfolio leans on unquantified qualifiers ("a large fraction", "substantially", "systematically"), which makes falsification adjudication subjective at kill time: a 5% effect can be argued either way. This is the **single biggest quality gap**. [EVIDENCE: regex for %/decimals/point-thresholds in `falsifiable_prediction`]
- **157/248** records have no explicit "falsified if / kills the idea" clause in either experiment field (the kill condition is implicit in the prediction). gen_a is the disciplined shard here; gen_b/gen_c largely omit it.

### 1.4 Cheap-kill presence — present everywhere, cost-bounded unevenly

Every record has a `fastest_falsification_experiment` and spot-reads show they are concrete (specific N, specific manipulation, specific readout). Explicit time/cost bound ("one afternoon", "hours", "one day", "single GPU"):

| shard | fastest test carries explicit time/cost bound |
|---|---|
| gen_a | 92/94 (98%) |
| gen_b | 52/85 (61%) |
| gen_c | 33/69 (48%) |

**32/248** fastest tests require non-standard resources — human raters/experts (multi-annotator or clinician studies: B-002, B-017–B-022, B-084, B-085, C-065–C-067…) or special hardware (polarization: B-060/B-012; event camera: B-071; HDR: B-042; thermal/particulate sensors: B-083). These are legitimate experiments but are **not** "cheap kills" for an autonomous or single-GPU pipeline; Stage-2 ranking should discount claimed cheapness for these. [EVIDENCE: resource regex + manual check]

### 1.5 Citations — CLEAN, no fake citations found

Exactly 13 citation strings appear across all 248 records, each used once, all in gen_a's `prior_work_basis` labels: Kirillov 2023 (SAM), Ravi 2024 (SAM2), Hu 2021 (LoRA), Ben Zaken 2022 (BitFit), Jia 2022 (VPT), He 2022 (MAE), Kornblith 2019 (CKA), Wortsman 2022 (model soups), Ilharco 2022 (task arithmetic), Geirhos 2019 (texture bias), Darcet 2023 (registers), Ke 2023 (HQ-SAM), Carion 2020 (DETR). All are real, well-known papers used accurately, and each is explicitly wrapped in a VERIFIED-PRIOR-WORK vs MODEL-SPECULATION split. gen_b/gen_c cite nothing (they hedge with "to my knowledge" style claims instead) — no fabrication risk, but their novelty claims are entirely unverified self-assessments. [EVIDENCE: citation-pattern scan of all records]

---

## 2. Blind spots vs the P1 priority list

Counts = records whose one_line/core_hypothesis/cluster is primarily about the topic (strict), with anywhere-in-record mentions in parentheses. [EVIDENCE: keyword scan, medical regex corrected for the `ct\b`-matches-"object" artifact; "document" hits verified to be the word "documented", i.e., real doc/OCR coverage is ~0]

| P1 priority topic | primary | (mentions) | verdict |
|---|---|---|---|
| SAM/SAM2 | 82 | (90) | SATURATED — 33% of portfolio |
| medical | 33 | (60) | covered, but narrow lens (ambiguity/ground-truth only) |
| uncertainty/calibration | 57 | (73) | SATURATED — 3 shards converged independently |
| smoke/fire/transparent | 48 | (64) | well covered (gen_b) |
| VFM general (CLIP/DINO/ViT/pretraining) | 36 | (76) | covered, mostly as eval-critique object |
| PEFT | 37 | (49) | covered, but ~exclusively PEFT-of-SAM |
| domain shift/adaptation | 22 | (55) | covered via SAM/PEFT lens |
| video/temporal | 25 | (38) | moderate (SAM2 + smoke dynamics) |
| annotation/human factors | 43 | (69) | heavily covered |
| synthetic data | 12 | (50) | thin & critique-only (B-082/B-087/C-064); no constructive generation hypotheses |
| detection | 17 | (35) | **UNDERWEIGHT** — almost all incidental; only B-023, C-011 are detection-primary |
| VLM dense prediction | 9 | (11) | **BLIND SPOT** — the 9 are gen_c eval critiques; zero open-vocab/grounding capability hypotheses |
| cross-field (physics/other sciences) | 16 | (35) | physics-of-media only; no remote sensing (6 incidental), microscopy (1), 3D/depth/LiDAR (2), driving (1) |
| SR/restoration | 2 | (3) | **BLIND SPOT** — essentially absent |
| diffusion/generative | 1 | (4) | **BLIND SPOT** — no diffusion-for-perception, diffusion-as-data-engine, generative priors |
| LLM/agent | 1 | (1) | **BLIND SPOT** — C-060 (CoT critique) is the only record |

**Net:** 5 of the 14 P1 priority territories (SR/restoration, diffusion, LLM/agent, VLM dense, detection) hold **~30 of 248 records (12%)** combined, while SAM+uncertainty+eval-critique hold well over half. The portfolio is deep, not broad.

Secondary blind spots (not on the priority list but conspicuous): 3D/point-cloud/depth (2), remote sensing/aerial (0 primary), document/OCR (0), autonomous driving (1), microscopy/pathology-as-domain (1), open-vocabulary segmentation (2), training-objective/optimization science (~3).

---

## 3. Debunk vs constructive balance

Hand-labeled over all 248 one-liners (constructive-capability = if the hypothesis is TRUE, it directly yields a usable method, training target, architecture change, or free diagnostic signal — not merely invalidating a belief):

- **Debunk/critique** (belief X is wrong / metric Y is broken / model Z secretly fails): **~150/248 (~60%)**
- **Neutral characterization laws** (quantitative law of behavior, exploitable but not framed as a fix): **~52 (~21%)**
- **Constructive-capability**: **46/248 (18.5%)**
  - gen_a: 24/94 (A-005, A-012, A-017, A-022, A-024, A-025, A-026, A-027, A-029, A-030, A-036, A-041, A-042, A-043, A-045, A-053, A-076, A-078, A-086, A-088, A-090, A-094, A-097, A-100)
  - gen_b: 22/85 (B-005, B-020, B-024, B-026, B-037, B-050, B-057, B-060, B-061, B-062, B-063, B-065, B-069, B-071, B-072, B-073, B-074, B-080, B-083, B-084, B-090, B-094)
  - gen_c: **0/69** capability hypotheses (a few audit-protocol proposals, e.g. C-037/C-073, are constructive methodology but not capability)

**Verdict: yes, the portfolio is debunk-skewed, ~3:1 critique-to-construction**, and the skew is structural: an entire shard (gen_c, 28% of records) is contrarian-by-design with zero capability content, and both other shards default to failure-mode framing. Note this is a *milder* verdict than a crude regex gives (Auditor A's surface regex found 0 method proposals; manual reading finds 46 real ones — the constructive ideas exist but are phrased as testable hypotheses rather than "we propose X", which is fine and arguably better). The real deficit: constructive ideas cluster in the SAM ecosystem and smoke/medical targets; there are **no constructive hypotheses at all** in restoration, diffusion, detection, VLM-dense, or LLM/agent territory, and gen_c's 40+ diagnosed eval pathologies come with almost no "here is the better protocol, and here is how to test that it is better" counterparts.

Within the constructive set, the strongest sub-genre is "free diagnostic signals" (A-025 IoU-histogram OOD detector, A-027 label-error detector, A-086 adapter router, B-026 prompt-jitter ambiguity meter) — cheap, testable, publishable. The rarest is "new training target/architecture" (~20 records, 8%).

---

## 4. Recommended next territories (queue for generators — NOT a lock)

Ordered by (blind-spot severity × constructive potential × cheap-kill testability). Each is a generator brief, with quota guidance.

1. **restoration_x_dense_prediction** — SR/restoration science: when does restoration pre-processing help vs hallucinate for downstream segmentation/detection; perception-distortion tradeoffs as falsifiable laws; restoration hallucination risk in medical/scientific imagery. (Fills the emptiest priority territory; natural bridge to existing smoke/low-contrast work.)
2. **diffusion_for_perception** — diffusion/generative models as feature extractors, data engines, and uncertainty priors for dense prediction; physics-constrained synthetic data for participating media (constructive successor to B-082/B-087 critiques and the synthetic-data gap).
3. **vlm_dense_capability** — open-vocabulary / referring / grounded segmentation as capability hypotheses (not eval critique): mass-noun vs count-noun grounding (extend B-030), text-prompted dense prediction on hard domains, medical referring segmentation. Constructive quota ≥ 60%.
4. **detection_science** — detection-primary hypotheses: query mechanics of DETR-family (mirror gen_a's decoder work), small-object/lesion detection vs overlap metrics (extend B-023), detection calibration done right (extend C-011).
5. **constructive_eval_repair** — take gen_c's strongest diagnosed pathologies and generate the fix-hypotheses: paired/variance-budgeted evaluation designs, harness-invariant metrics, contamination-robust protocols — each with a falsifiable "the repaired protocol changes conclusion X" prediction.
6. **objective_function_science** — losses and training targets for dense prediction beyond focal+dice (generalize B-057 log-transmittance, B-080 level-set supervision, B-024 mixture regression, A-101); Auditor-A-confirmed zero permutation volume here, so it is clear ground.
7. **cross_field_deployment** — remote sensing/UAV fire & smoke monitoring (deployment-side successor to gen_b), microscopy/pathology dense prediction, 3D/depth/LiDAR interaction with transparency (extend B-014).
8. **llm_agent_vision_loops** — agentic/tool-use pipelines around segmentation (LLM-orchestrated prompting, self-correcting annotation agents), VLM-as-judge reliability as capability question (extend C-071).
9. **medical_beyond_ambiguity** — longitudinal/temporal medical (B-072 is the lone seed), cross-site convention transfer as a constructive method (B-085), medical VLM/report-grounded segmentation (0 records today).

**Generator-brief quality gates for the next wave** (fixes Section 1 defects):
- Every `falsifiable_prediction` MUST carry a numeric kill threshold (effect size, %, or metric delta).
- Every record MUST carry the structured `evidence_label` dict (gen_a's schema, incl. `prior_work_basis`).
- `fastest_falsification_experiment` MUST state a time/cost bound and require only public data + single GPU (or explicitly flag `needs_special_resources`).
- Per-generator constructive-capability quota ≥ 50%.
- Stop-feeding list (agrees with Auditor A): SAM internals, PEFT-of-SAM, uncertainty/calibration, annotation pathology, generic eval critique.

---

## 5. Cross-check vs Auditor A (read after independent analysis)

Independent agreement: SAM (A: 87 mentions / B: 82 primary) and calibration/uncertainty (A: 31 direct / B: 57 loose-primary) saturated; eval-critique super-cluster dominant; 3D, remote sensing, training-dynamics, active-learning blind spots; zero loss+X permutation volume. One substantive divergence: A's genre-level regex reported "0 records propose a method as primary contribution"; manual labeling finds 46 constructive-capability records (18.5%) — the debunk-skew conclusion stands, but consolidator should use the 46-record list above as the protected constructive core when balancing Stage 2, not treat the portfolio as 100% critique.

*No fake citations introduced by this audit; all counts reproducible from `ideas_master.jsonl` with the regexes described.*
