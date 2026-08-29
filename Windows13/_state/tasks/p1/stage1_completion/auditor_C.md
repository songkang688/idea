# P1 Stage-1 Completion — Auditor C (mode collapse / pseudo-innovation) — Windows13

- **task_id:** `p1_stage1_completion` · **role:** `auditor_C_mode_collapse`
- **windows_id / windows_path:** Windows13 / Windows13 · **window_locked:** true
- **audited master (READ ONLY):** `origin/cursor/p1-wave-b-consolidator-w5-d795` @ `7338e5490f910a5079ce64bf2367a3c9a0619876`, `Windows13/_state/ideas_master.jsonl`, 1220 records (re-verified: 1220 valid JSON lines, 1220 unique id_seeds)
- **Independent pass first:** every number below was computed by script on the canonical master **before** reading auditor A or the diversity_audit_w3 consolidator; those were consulted afterwards for cross-reference only. Machine evidence in `auditor_C.json`.
- `ideas_master.jsonl`, `research_state.json`, `window.lock.json` untouched. No other Windows scanned.

## VERDICT: PASS_WITH_REMEDIATION

The remaining collapse is **template-family-level and prior-art-exposure-level**, not subject-level or lexical. It is acceptable to **freeze Stage-1 generation** — more generators are **not** required and would not fix what remains — **provided** the four remediation items below (all selection-side, all already owned by lanes queued at the w3 diversity audit) execute before the Stage-2 200-cut. Meta-Judge combines A/B/C; this verdict does not end P1.

## 1. What I measured (all 1220 records, no sampling)

### 1a. Lexical near-duplication — LOW, no collapse
Exact all-pairs token-Jaccard over `one_line_idea`+`core_hypothesis`: **743,590 pairs, max 0.237** (J-051/J-076), 0 pairs ≥ 0.5, 42 pairs > 0.15. Zero exact duplicates of any hypothesis field. Domain/model/number-normalized 18-token skeletons of `falsifiable_prediction`: **0 collisions**. Within-shard structural 6-gram template reuse (prediction + experiment, normalized): 0 pairs above 0.30 in any of the 15 shards. Consistent with auditor A (max 0.242, different tokenizer).

### 1b. SAM+X / permutation volume — CONTAINED
- SAM/SAM2 mention share (idea+problem+hypothesis): **87/1220 = 7.1%**; one-liner-primary: 77 (6.3%), of which **76 are frozen wave-1 gen_a stock** and 1 is gen_k SAM2-memory inside its granted allowance.
- The "SAM + PEFT-variant" permutation subgroup: **38 records = 3.1%** of portfolio, spread over 13 gen_a-internal clusters (max 12).
- Trajectory: 34–35% (w1 audit, 248) → 9.6% (w3 audit, 934) → **7.1% (this audit, 1220)**. The ≤5%-per-shard guard held on every post-w1 shard; dilution came from diversified growth, exactly as designed.
- Smoke/fire fixation: all 32 one-liner instances are frozen gen_b w1 stock; the ban held for waves 2–5.
- Cross-shard domain-permutation test (same skeleton, domain swapped — the gen_o/gen_b risk): normalized-skeleton reuse ≈ 0 (max 0.16 within gen_o). gen_o's hard domains carry domain-native mechanisms (Beer-Lambert stain space, SAR incidence geometry, layout grammars), not re-skinned templates.

### 1c. Template families — PRESENT, MODERATE: this is the real remaining collapse
Loose semantic clustering (union-find, all-pairs Jaccard > 0.12): **287/1220 records (23.5%) sit in some multi-member family; 35 families of size ≥ 3; largest ≈ 15**. Qualitative reads confirm genuine epistemic-move families, individually distinct but one move permuted:

| family (my instrument) | size | members (examples) |
|---|---|---|
| variance/protocol-artifact audit of reported gains | ~13–15 | C-047, C-054, C-073, C-077, C-080, C-103, D-002, D-011, D-026, F-020, G-003, G-019, G-023, P-004 |
| text-encoder geometry predicts dense failure | ~7 | E-034, E-047, E-050, E-051, E-052, E-053, J-070 |
| gen_m pixels-per-batch / gradient-noise mechanics | ~8–10 | M-025, M-028, M-030, M-037, M-073, M-082, M-084, M-086 |
| sim-to-real cheap-statistics fix | ~8 | F-003, F-008, F-010, F-019, F-022, F-023, F-075, H-001 |
| provenance forensics ("X decodable from outputs") | ~4 | B-021, B-035, F-060 (+ N-070 adjacency) |

Independent re-census of the two headline judge-flagged cells: gen_m *ritual-is-mechanism* = **11/98** by my stricter regex (judge census 19 — both far over any ≤4–6 cap); *cheap/free-predictor-of-outcome* = **33** portfolio-wide by loose regex (judge census 14 with portfolio freeze — over the line on both instruments). Named sibling pairs verified by direct reading: J-051/J-076, E-029/E-054, B-060/B-065, F-019/F-023, N-061/N-070, C-003/C-004/C-057.

**Why acceptable at freeze:** each member is a distinct falsifiable hypothesis (not a restatement — 1a proves the texts and experiments differ substantively); families of 2–15 inside a 1220-pool feeding a 200-cut are prunable by intra-family competition at selection; judges already fired merges inside these families at w4/w5. More generation would grow these families (cheap-predictor doubled 7→14 across two audit rounds *despite* a per-shard cap), it cannot shrink them.

### 1d. Fingerprint crowding — instrument DEFEATED, debt not disaster
`family_fingerprint` exists on 680/1220 records (w3–w5 only) and is free text: **680/680 distinct values** — zero mechanical cap enforcement is possible on the raw field (reproduces the w3 audit's 393/394 finding at 1220). The controlled ~30-enum vocabulary mandated by the w3 decision "from w5 consolidation onward" was **not adopted at w5**, which reported over-cap cells in yet another private vocabulary (annotation_protocol_capability 14, memorization_dose_response 12, dense_transfer_exponents 11, illumination_geometry_confounds 7). The over-cap census (10–24 cells depending on vocabulary) cannot be joined across waves. Three independent instruments agree on *where* the crowding is, so this is an instrumentation debt (owned by the retrofit lane), not hidden collapse.

### 1e. Genre balance — debunk monoculture broken; skew localized in frozen legacy
Labeled 680 (w3–w5): constructive 44.6%, characterization 44.0%, debunk 12.1%. Unlabeled 540 (w1/w2) by my regex heuristic: ~55% debunk-leaning. Blended portfolio ≈ **31% debunk / 28% constructive / 38% characterization** vs 51.4% debunk / 7.7% strict-constructive at the 494-audit. Eval-critique surface: 32.3% mention-level, **10.9% by primary cluster** — and 43 of those 133 are gen_p's constructive eval-*repair* records. The skew is concentrated in frozen w1/w2 stock, fenced by the protected constructive id-lists and the w3 genre-blind eval-subject pool cap (≤25% of the 200-cut).

### 1f. Pseudo-innovation / prior-art exposure — the largest single risk, bounded and owned
`novelty_status` = unverified on **1220/1220**. At least two accepted records are demonstrably **real prior art retained by 2-1 majority**: **O-002** = Sea-thru (Akkaynak & Treibitz, CVPR 2019, doi:10.1109/CVPR.2019.00178 — **independently re-verified by live web check during this audit**, including the monocular-depth substitution O-002 claims as its delta, which public implementations already do) and **O-031** = Tellez et al. 2018 / Medical Image Analysis 2019 (doi:10.1016/j.media.2019.101544, judge-C web-verified at w5). Five more outvoted judge-C prior-art kills sit accepted with dissents: C-016, D-059, K-020, K-069, L-012. Unprocessed watchlists: w2's 73-id permutation list, w4's 20-id + w5's 27-id high-risk lists, 141 `judge_dissent` carriers. This is *enumerated, per-record-flagged* exposure with a queued owner (`p1_gate8_novelty_triage`) — acceptable at freeze **only** because R1 below binds it before the 200-cut. The count gate survives worst-case triage (1220 − all flagged ≫ 1000).

### 1g. Fake citations — ZERO
Exhaustive extraction over every string field of all 1220 records: ~20 distinct citation-like strings, **all correctly attributed to real works** (SAM, LoRA, CKA, BitFit, model soups, task arithmetic, VPT, MAE, Geirhos cue-conflict, ViT registers, HQ-SAM, DETR, SAM 2, Sea-thru with real DOI, Tellez with real DOI, SMLM challenge, GWHD 2021, Pascal VOC 2012), every one wrapped in an honest evidence label; gen_n's 23 on-master citation-bearing records carry "KNOWN PRIOR WORK (model recall, unverified here)" verbatim. 0 invented benchmark numbers in novelty/belief/importance fields. This auditor adds no citations.

### 1h. Subject/cluster spread — WIDE
156 clusters, largest 14 (1.1%); shard sizes 69–102 across 15 families; top subject mention shares: detection 17.3%, annotation 9.3%, calibration 7.9% (down from 20.6%), SAM 7.1%, depth 6.6%. Remaining blind spots (cross-field transfer 0, security/fairness ~0.5%, lifecycle 0.4%) have queued generators (r/w/v) as **coverage plays for the 200-cut, not freeze blockers**.

## 2. Why PASS_WITH_REMEDIATION and not FAIL (more generators)

FAIL-requiring-more-generators would be the wrong cure. The evidence says generation volume is not the problem: subject crowding is diluted, lexical duplication is near-zero, shard territories are disjoint, and the count gate cleared with margin. What remains — template-family growth, unverified novelty, fingerprint instrumentation, remand disposition — is **selection-side debt**, and one of its drivers (cheap-predictor family doubling despite caps) demonstrably *worsens* with more generation. Every remediation item already has a named, queued owner from the w3 decision; this verdict binds Stage-1 freeze to their execution rather than inventing new machinery.

## 3. Binding remediation (before the Stage-2 200-cut)

1. **R1 — GATE-8 first:** `p1_gate8_novelty_triage` priority items 1–4 complete before the cut; explicit dispositions for O-002, O-031 and the five outvoted prior-art kills (C-016, D-059, K-020, K-069, L-012). Never rank these blind.
2. **R2 — fingerprint back-mapping before mechanical caps:** back-map all 680 free-text fingerprints onto the controlled vocabulary before slot-cap enforcement; until then apply the w3 genre-blind pooled caps (eval pool ≤25%) and the cheap-predictor displacement rule from the judge flag lists.
3. **R3 — remand disposition:** the 127-record gen_g/gen_h pool (73 gen_h = the restoration blind spot) gets repair-append or kill-with-decision before cut composition is fixed (`p1_wave_b_w3_gate5_repair_2`).
4. **R4 — forced family adjudication at the cut:** best-of-family selection over the named sibling sets in §1c (extends the w3 list of 5 pairs); never multiple undifferentiated siblings into the 200.

## 4. Unresolved items

- Novelty unverified 1220/1220 (bounded by R1, unresolved until GATE-8 runs).
- O-002/O-031 disposition pending (my independent web check confirms judge-C's O-002 evidence).
- Fingerprint vocabulary-join problem compounds each wave until R2 lands.
- 127-record remand pool ownerless-in-execution until repair_2 dispatches.
- True debunk share of the unlabeled 540 is instrument-dependent (~55% of that stock by my heuristic); exact figure needs the retrofit lane's label backfill.
- Cheap-predictor census divergence (33 loose vs 14 judge-fingerprint) — Stage-2 must pick one instrument and apply it consistently.

## 5. Cross-reference (read after independent pass)

- **Auditor A (count/dedup, PASS):** fully consistent — identical zero-duplicate findings, near-identical max Jaccard (0.242 vs my 0.237), identical shard counts.
- **Diversity audit w3 consolidator:** its guard trends (SAM guard held, crowding moved to template families, fingerprint instrument defeated, capacity no longer the bottleneck) are independently reproduced at 1220 by my own instruments.

*No fake citations; every number computed by script from the audited commit; canonical state untouched; recommended next task: `p1_stage1_meta_judge`.*
