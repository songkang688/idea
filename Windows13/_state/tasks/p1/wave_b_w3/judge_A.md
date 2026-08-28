# P1 Wave B — Judge A: Hypothesis-Level Dedup (Wave 3, sub-wave G+H+J)

- **task_id:** `p1_wave_b_w3` | **role:** `judge_A_dedup` | **windows_id:** `Windows13` (locked)
- **branch:** `cursor/p1-wave-b-w3-judge-a-dedup-e60e`
- **Scope:** cross-shard hypothesis-level dedup for the THIRD generator wave, sub-wave G+H+J only (the Wave-B consolidator split the 4 pushed shards; gen_k is judged separately). Near-duplicate clustering, permutation/template flagging, family-membership merge triggers (w2 diversity ruling), cross-wave collision flagging against the canonical 494-idea master (READ ONLY, not appended), collision enumeration against unjudged shards gen_k/l/m/n/p (FLAG ONLY, none merged), GATE-5 compliance audit, and an accepted-candidate list for THIS sub-wave. Canonical state (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched.
- **Epistemic status:** NO novelty is verified for any kept idea. Every prior-art / known-result remark below is the judge's unverified HYPOTHESIS. No experimental numbers or citations were invented.

## 1. Inputs

| Shard | Branch | Ideas | Gate schema |
|---|---|---|---|
| gen_g_domain_shift | `cursor/p1-gen-g-domain-shift-0165` | 100 (W13-P1-G-001..100) | pre-gate (no thresholds / labels) |
| gen_h_sr_restoration | `cursor/p1-gen-h-sr-restoration-1829` | 100 (W13-P1-H-001..100) | pre-gate (no thresholds / labels) |
| gen_j_diffusion_model_science | `cursor/p1-gen-j-diffusion-science-3470` | 104 (W13-P1-J-001..104) | FULL gen_j canonical schema |
| **Total wave-3 sub-wave input** | | **304** | |
| (reference, read-only) canonical master | `cursor/p1-wave-b-consolidator-w2-3111` | 494 accepted (A94/B85/C69/D79/E79/F88) | |
| (flag-only) gen_k / gen_l / gen_m / gen_n / gen_p | on origin | 105/100/100/100/104 | enumerated, NOT merged |
| (in flight) gen_o, gen_u | not on origin at judge time | — | verified absent via ls-remote |

All 304 lines parsed; IDs contiguous per shard; no cross-shard ID collisions; no ideas invented or renumbered.

## 2. Method

Each idea was compared on `core_hypothesis` content (mechanism + falsifiable claim), first within and across G/H/J, then against the 494 accepted master ideas, then against the five unjudged origin shards. Two ideas were treated as duplicates when they assert the same mechanism with the same falsification design, differing only in substrate. Per the w2 diversity commissioning, **family membership was a MERGE TRIGGER**, not only pairwise similarity: judge-assigned family fingerprints were capped at <= 6 kept primaries per cell, and the caps fired real merges (memorization, posterior-dispersion, degradation-realism) and real kills (annotation-convention hard ban). Lexical token-Jaccard scans found **no pair >= 0.24 anywhere** (within-wave, vs master, vs collision shards) — duplication in this wave is entirely family/hypothesis-level, exactly as the w2 audit predicted, so every verdict rests on manual hypothesis comparison, and surface-similarity tools would have caught none of the 31 duplicate groups below.

## 3. Verdict Counts

| Quantity | Value |
|---|---|
| Input total | 304 (G: 100, H: 100, J: 104) |
| **Keep (accepted candidates this sub-wave)** | **260** (G: 81, H: 84, J: 95) |
| Kill or merge | 44 (G: 19, H: 16, J: 9) |
| Within-wave duplicate groups | 31 (32 merged members; 2 groups are cross-shard) |
| Master-collision kill groups (target in accepted 494) | 8 (11 kills) |
| Standalone known-result kill | 1 (G-068, resurrectable) |
| Kept ideas carrying master collision/prior-art flags | 46 |
| Kept ideas carrying off-master (gen_k/l/m/n/p/u) collision flags | 27 |
| Flagged template/permutation ids (kept + killed) | 138 across 20 families |
| Family-cap merge triggers fired | 9 |
| High-value anomalies (protected) | 21 |
| Deliberate tensions kept | 7 |
| Judge clusters (all 304 ids assigned exactly once) | 32 |

gen_j is the strongest shard ever judged in this window (95/104 kept, all records fully gate-compliant, fingerprints genuinely distinct); its 9 kills are all family-cap consolidations, not quality failures. gen_g is the most master-collided shard: 7 of its 8 master kills re-derive accepted shard-C evaluation critiques on the shift substrate. gen_h's kills are dominated by within-shard restatements (12 of 16).

## 4. Duplicate Groups That Matter Most

Full list with reasons: `judge_A.json -> duplicate_groups`.

- **Cross-shard (the reason this judge exists):** dg07 distillation-averages-posterior-modes (keep J-059, merge H-040 — restoration and dense prediction stating one law); dg08 VAE-roundtrip-ceiling (keep J-080, merge **H-041 and J-084** — three substrates, one decode(encode(x)) bound).
- **gen_g consolidations:** selection-oracle circularity (G-019 ⊃ G-003); TTA-is-output-repriors (G-007 ⊃ G-008); stream-realism rankings (G-073 ⊃ G-012); augmentation-ensembling gains (G-009 ⊃ G-013); FM-nullifies-alignment (G-015 ⊃ G-017); backbone-not-algorithm (G-025 ⊃ G-026); invariance-robustness tradeoff (G-093 ⊃ G-031); environment-partition quality (G-027 ⊃ G-036); contamination (G-071 ⊃ G-052); decision-aware harm predictors (G-090 ⊃ G-087); language-supplies-domain (G-035 ⊃ G-095).
- **gen_h consolidations:** degradation-factor attribution (H-001 ⊃ H-006); neural-processing degradations (H-054 ⊃ H-008); conditioning-beats-marginalization (H-097 ⊃ H-018); misalignment metric bias (H-013 ⊃ H-027); matched-recipe compression (H-091 ⊃ H-032); evidence-gated abstention (H-086 ⊃ H-035); hallucination-scales-with-prior (H-033 ⊃ H-053); observation-consistency fidelity (H-028 ⊃ H-062); restoration-vs-reimagination (H-044 ⊃ H-084); human-machine divergence (H-029 ⊃ H-088).
- **gen_j family-cap consolidations:** sharp-attractor signature (J-040 ⊃ J-042); layout-tier memorization (J-043 ⊃ J-045); surgical unlearning (J-041 ⊃ J-046); memorization dose-response (J-038 ⊃ J-104, video arm); seed-layout control (J-052 ⊃ J-053); iterated-regeneration contraction (J-031 ⊃ J-054); dispersion-matches-ill-posedness (J-056 ⊃ J-060, aperture-anisotropy arm preserved); spectrum-matched schedules (J-093 ⊃ J-091).

## 5. Family-Merge Triggers and Caps (w2 ruling applied)

Nine merges/kills were forced by family caps rather than pure pairwise duplication:

- **memorization family** (14 raw members incl. gen_h): capped to exactly 6 gen_j primaries (J-038, J-039, J-040, J-041, J-043, J-044) via dg13/dg14/dg15/dg20; J-074 is cross-assigned to the distillation family; H-043/H-098 remain as restoration-substrate members with gen_n collision flags.
- **posterior_dispersion_as_uncertainty** (9 members): capped at 6 primaries via dg18; the family contains two deliberate tensions (Section 7).
- **degradation_realism_decomposition** (7 members, the gen_h analog of gen_f's content-over-realism factorials): capped at 6 via dg01.
- **annotation-convention pathology** (HARD BAN as primary subject, master family already over cap): G-055 and G-074 killed outright into accepted B-085 (mg01).
- **equalization_matched_budget_null** (w2 cap <= 3/shard): gen_h reduced to 3 primaries via dg05.

**Dominant new template of this wave** (the w3 analog of SAM+X / content-over-realism): **cheap_predictor_of_outcome** — "quantity X, computable before/without labels, predicts outcome Y" — 17 ids across all three shards (G-021, G-043, G-080, G-084, G-089, G-090, G-092, G-099, H-012, H-017, J-026, J-029, J-032, J-049, J-062, J-078 + merged G-087). All members carry distinct predictor→predictand fingerprints (max cell 2 after dg30), so they were kept, but the family is flagged as the first candidate for Stage-2 slot caps. Other large flagged families: distillation_lossmap (12), vae_bottleneck_attribution (9), iterated_regeneration_drift (9), snr_reparameterization_universality (gen_j's signature move, 5), consistency_self_audit with new transforms T = scale-composition / equivariance / instruction-inverse / semigroup (each T genuinely new vs the w2 list).

## 6. Cross-Wave Collisions Against the 494 Master (flag only — master untouched)

11 wave-3 ideas were killed as near-verbatim ports of accepted ideas: G-057→C-024, G-058→C-085, G-072+G-091→C-081, G-055+G-074→B-085, G-078+H-058→C-077, H-061→C-032, H-056→C-029, H-050→C-020 (the paraphrase-port kill repeats the w2 E-021 precedent exactly). One standalone kill on known-result grounds (UNVERIFIED judge assessment, no citation invented): G-068 (weight-averaging robustness recovery) — resurrect if the novelty judge disagrees; note its live tension with kept G-028.

46 keeps carry explicit master flags. Highest-risk keeps for the novelty gate, in order: **G-069** (vs C-028), **G-014** (vs F-023), **J-086** (vs D-060), **J-008** (vs A-039 + registers literature), **H-024** (vs C-037), **H-083** (vs D-030), **G-054** (vs D-064/D-061), **G-097** (vs C-089/D-058), **G-086** (vs D-091/C-045), **G-071** (vs C-023/C-024/C-032/F-086), **G-051** (vs C-029 + known-practice risk), **G-053** (vs C-015). Full map: `judge_A.json -> master_collision_flags_on_keeps`.

## 7. Off-Master Collision Flags (gen_k/l/m/n/p enumerated, NOT merged)

27 keeps carry flags against unjudged origin shards — these are reconciliation duties for the shards' own future judges, not verdicts: the strongest is **J-038 ↔ N-053/N-054/N-055** (memorization dose-response laws, generative vs discriminative — gen_n's judges must dedup against whatever the consolidator accepts from this list). Also: J-074↔N-070 (distillation inherits memorization/membership), H-043/H-098↔N-081/N-055, G-047/G-056↔N-043 (effective sample size), G-030/G-060/G-063↔gen_n scaling territory, G-086↔L-092 (iso-cost accounting), G-006↔gen_l/gen_q boundary (per R4, gen_g owns TTA critique G-001..G-014), H-076/H-077↔K-077 (codec/aliasing exploitation), J-009↔P-055/P-061 (cross-backbone head portability), J-012/J-015↔P-049, J-005/J-011/J-097/J-102/J-103↔gen_k depth/video territory, J-092/J-078/H-091↔gen_m boundary, **H-090↔gen_u** (fairness territory: if H-090 is accepted, gen_u's brief must treat it as occupied ground). gen_o and gen_u have no shards on origin (verified by ls-remote at judge time).

## 8. GATE-5 / GATE-6 (recorded, NOT repaired — no pretending)

- Mechanical audit confirms the commissioning numbers: **gen_g 0/100** records with a numeric kill threshold in `falsifiable_prediction`, **gen_h 2/100 borderline** (H-066/H-072 contain incidental numerals — a 4x scale factor and a bit depth — but NO pre-registered kill threshold, so effectively 0/100), **gen_j 104/104 compliant** (threshold + evidence_label dict + family_fingerprint + genre on every record). evidence_label dicts: gen_g 0/100, gen_h 0/100, gen_j 104/104.
- **This judge did NOT retrofit.** Inventing 165 numeric thresholds during a dedup pass is fabrication risk, not repair. Every kept gen_g/gen_h record carries `judge_A_meta.gate5.retrofit_needed=true`. Recommended path: judge B attaches thresholds during feasibility (it reads every fastest-experiment anyway), judge C spot-audits, consolidator writes the mandatory gate-compliance line — or the gen_g+gen_h keeps are remanded as a block. They must NOT be merged threshold-less into the master.
- GATE-6: gen_j self-declares 37/104 (35.6%) constructive_capability — exactly the figure the w2 audit found inflated vs ~7% by phrasing. Recorded for judge C / consolidator; genre labels were not used for any verdict here.

## 9. High-Value Anomalies (protected, 21)

G-033 (compositional shift as unmeasured axis), G-050 (deployment feedback loops break i.i.d.), G-065 (shortcut mechanism survives scale), G-085 (bursty arrival breaks TTA at zero shift), H-025 (preference flips with viewing time/GT knowledge), H-042 (imperceptible perturbations flip restored semantics), H-043 (restoration injects memorized training images), H-049 (SSL invariances make worse perceptual-loss backbones), H-051 (failures peak where prior strongest & evidence weakest), H-071 (single-ground-truth convention is the root of both blur and fabrication), H-076 (video SR's multi-frame gain is aliasing exploitation), H-080 (enhancement alters lip/expression micro-motion), J-008 (generative register tokens buffer appearance state), J-010 (symmetric-part margin), J-018 (motion affordances in static-image features), J-039 (caption-keyed recall enables inference-time mitigation), J-052 (seed as composition genome), J-065 (shared subitizing breakpoint in probes and generation), J-082 (deterministic decoder texture vocabulary), J-090 (closed-form terminal-SNR bias), J-102 (collapse periodicity measures temporal memory).

## 10. Deliberate Tensions Kept (adjudicate by experiment, not dedup)

1. **H-030 vs H-037** — cross-seed variance is a usable hallucination map vs diversity is misallocated exactly where it matters.
2. **J-056/J-057 vs J-058** — sampler dispersion expresses true ambiguity vs posteriors systematically under-disperse.
3. **H-099 vs J-079** — iteration adds nothing at matched compute for fidelity vs the 1-to-2-step transition is a real discontinuity (also touches J-019).
4. **J-019 vs J-073/J-075** — one-step students keep perception features vs lose input sensitivity and accessible diversity.
5. **G-037 vs G-041** — classical tests on frozen embeddings suffice vs embedding statistics mask semantic shift.
6. **J-023 vs J-070** — negation failure lives in score-space geometry vs in the text encoder.
7. **H-095 vs H-002** — degradation diversity keeps paying vs a compact measured set beats randomized diversity.

## 11. Accepted-Candidate List

260 kept ids with judge clusters, duplicate groups, family flags, master and off-master collision flags, GATE-5 status, anomaly/tension notes and full copied source fields: `accepted_shard_A.jsonl`. Machine-readable dispositions: `judge_A.json`.

## 12. Caveats / handoff to judges B, C and the Consolidator

1. **Novelty unverified everywhere.** The 46 master-flagged keeps and the 12 highest-risk ids in Section 6 are first in line for the novelty gate; the 17-member cheap-predictor family is first in line for Stage-2 slot caps.
2. **GATE-5 retrofit-or-remand is unfinished by design** (Section 8) — a gate-compliance line in the wave-3 consolidator done-file is mandatory per the w2 decision; 165 of 260 keeps need thresholds and labels before master merge.
3. **kill_or_merge is not a quality verdict.** Likeliest resurrection candidates: J-104 (video memorization as its own privacy track), J-060 (aperture-anisotropy — the most quantitative member of its group), G-068 (if the novelty judge rejects the known-result assessment), H-084 (forensic certificates as a deliverable distinct from H-044's boundary).
4. **Off-master flags (Section 7) are duties for the gen_k/l/m/n/p/u judge waves**, not verdicts on those shards.
5. **Not judged here:** feasibility/compute triage, impact ranking, genre-quota enforcement (GATE-6 recorded only), Stage-2 selection, and any change to canonical state. The 494-master remains exactly as the wave-2 Consolidator wrote it; this sub-wave covers G+H+J only, and dispositions may shift when judges B and C report and the Wave-B consolidator merges.
