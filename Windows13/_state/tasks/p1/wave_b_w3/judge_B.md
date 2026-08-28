# P1 Wave B — Judge B: Feasibility / Cheap-Kill / Resources (Wave 3: Generators G+H+J)

- **task_id:** `p1_wave_b_w3` | **role:** `judge_B_feasibility` | **wave:** `w3_GHJ` | **windows_id:** `Windows13` (locked, `windows_path: Windows13`, `window_locked: true`)
- **branch:** `cursor/p1-wave-b-w3-judge-b-feasibility-2e78` (cut from the canonical 494-record master branch tip so `ideas_master.jsonl`, `research_state.json`, `window.lock.json` are present and UNTOUCHED)
- **Scope:** independent feasibility pass over the three raw generator shards gen_g (100), gen_h (100), gen_j (104). Judge A's wave-3 output was **not on origin at judging time** (verified by `git fetch --prune` + full branch scan); nothing here is derived from any accepted list. gen_k/l/m/n/o/p were not read and are not merged in. Canonical master (494) was read ONLY for cross-wave collision notes.
- **Epistemic status:** NO novelty verified for any idea. Every prior-art / known-result remark, including the single kill, is this judge's unverified hypothesis. No citations asserted or invented.

## 1. Inputs

| Shard | Branch | Ideas | Schema |
|---|---|---|---|
| gen_g_domain_shift | `cursor/p1-gen-g-domain-shift-0165` | 100 (W13-P1-G-001..100) | legacy 13-field |
| gen_h_sr_restoration | `cursor/p1-gen-h-sr-restoration-1829` | 100 (W13-P1-H-001..100) | legacy 13-field |
| gen_j_diffusion_model_science | `cursor/p1-gen-j-diffusion-science-3470` | 104 (W13-P1-J-001..104) | full canonical gen_j schema |
| canonical master (read-only, collision notes) | `cursor/p1-wave-b-consolidator-w2-3111` | 494 accepted A–F ids | — |
| commissioning (GATE-1..8) | `cursor/p1-diversity-audit-consolidator-w2-942c` | — | — |

All 304 lines parsed; every id assigned exactly one verdict (validated mechanically).

## 2. Verdict counts

| Quantity | Value |
|---|---|
| Input total | 304 (G: 100, H: 100, J: 104) |
| **Keep** | **283** (G: 88, H: 91, J: 104) |
| Merge | 20 — 15 in-wave in-shard, 2 in-wave cross-shard (H→J), 3 cross-wave into accepted wave-1 ids |
| Kill (standalone) | 1 (G-002) |
| Kept at T1 (inference/analysis only) | 196 |
| Kept at T2 (small training / light collection / human pilots) | 87 |
| Kept at T3 (gated) | **0** |
| Score-5 keeps (decisive kill ≤ 1 GPU-day, public assets) | 132 |
| High-value anomalies protected | 29 |
| Duplicate groups (in-wave) | 17 |
| Co-run infrastructure clusters | 18 |

This is the most feasibility-friendly wave so far: **zero gated keeps** and zero required multi-GPU resources. gen_g is dominated by frozen-model evaluation studies (T1), gen_j by inference/probing on public checkpoints with the occasional CIFAR-scale training (bounded 1–6 GPU-days, single GPU), gen_h by matched small SR trainings (T2) that almost always carry a genuinely cheap first-step falsification.

## 3. Gate compliance (the headline finding)

The wave is **bimodal on gates, exactly as the w2 commissioning predicted**:

- **GATE-1 (numeric kill threshold in prediction):** gen_g **0/100** (zero digits anywhere in predictions); gen_h **0/100 usable** (H-066/H-072 contain digits, but they are a "4x" scale factor and an "8-bit" depth, not thresholds); gen_j **104/104** with pre-registered kill conditions.
- **GATE-2 (evidence_label):** gen_g 0/100, gen_h 0/100, gen_j 104/104 structured dicts.
- **GATE-3 (time/cost bound + public/single-GPU or nsr):** gen_g 100/100 state coarse bounds; **gen_h only 4/100** state any explicit time/cost bound — a textual schema failure, though this judge assessed the described actions and found them cheap; gen_j 104/104 with device class, and J-063 honestly sets `needs_special_resources=true` for its human study.
- **GATE-4 (≥1 named public dataset AND model):** **wave-wide failure** — gen_g 0/100, gen_h 0/100, gen_j 8/104. Experiments are phrased generically ("one public backbone", "a standard benchmark"). Benchmark-shopping risk; asset naming must be added at retrofit.
- **GATE-5 (retrofit duty):** every gen_g and gen_h verdict carries `gate5_retrofit_needed: true`. **This judge invented no numbers and no labels.** Recommendation: **schema-only repair-or-remand** — gen_j proves the schema is satisfiable at 104/104; gen_g/gen_h content is strong and should not be content-rejected over schema.
- **GATE-7:** PASS — zero citation strings in all 304 records and in these outputs.

## 4. The kill (1)

- **G-002** (published TTA gains are batch-statistics artifacts that vanish at batch size one): UNVERIFIED known-result-restatement assessment — small-batch collapse of batch-norm-dependent TTA is, to this judge's unverified knowledge, repeatedly documented; the residual meta-claim is low information per slot. Cheap to resurrect; the batch-size axis survives inside G-085's arrival-process rig.

## 5. Merges (20)

**In-wave (15):** G-015→G-017, G-026→G-025, G-035→G-095, G-036→G-027, G-052→G-057, G-073→G-012, G-074→G-055, G-088→G-087, G-091→G-072, H-006→H-001, H-016→H-007, H-027→H-013, H-033→H-053, H-062→H-028, H-088→H-029. Criterion: shared decisive experiment (one rig, multiple readouts), per the escalated family-merge-trigger rule. Reasons per pair in `judge_B.json → merge_ids`.

**In-wave cross-shard (2):** H-041→J-080 (one VAE roundtrip fidelity-floor battery; gen_j record is the gate-compliant primary, restoration pixel-vs-latent arm retained), H-039→J-062 (one agreement-vs-accuracy validity study; restoration arm retained).

**Cross-wave into accepted wave-1 ids (3, master untouched):** G-069→C-028 (corruption benchmarks don't predict real shift; method-ranking arm extends C-028), G-071→C-023 (decontaminate-before-robustness-claims is C-023's protocol on shift benchmarks), H-061→C-032 (fresh-secret-test-set adaptive-overfitting replication in the SR ecosystem — the record itself frames it as a replication).

## 6. Cheap-kill honor roll (run these first)

132 keeps are score-5. The batch this judge would schedule first, because each is decisive in ≤ 1 GPU-day and load-bearing for a cluster:

- **J-001** (SNR-indexed feature peak) — gates the entire diffusion-features cluster's extraction convention.
- **J-080 (+absorbed H-041)** — VAE roundtrip floor; upper-bounds a dozen latent-space claims in an afternoon.
- **J-047 / J-095** — trajectory commitment window; reprices every editing/guidance-window idea.
- **J-090** — terminal-SNR bias is closed-form checkable against public configs in hours.
- **G-007/G-008 (+G-014)** — is TTA mostly output correction / prior correction / input normalization? Three afternoon comparisons that reprice the whole TTA cluster.
- **G-057 (+G-052)** — pretraining-proximity stratification; if coverage explains robustness variance, a large slice of FM-robustness claims is repriced.
- **G-018** — zero-shot VLM vs classic UDA leaderboards, a few hours.
- **G-072 (+G-091)** — effective-robustness identifiability reanalysis on published tables, hours.
- **H-007 (+H-016)** — clean-input over-restoration audit; mandatory before any deployment-weighted claim.
- **H-013 (+H-027)** — misalignment hedging incentive: one blur-sweep plot decides it.
- **H-036** — late-stage conditioning swap in diffusion SR, minutes per image.
- **H-092** — 2x-twice vs 4x-once composition gap, immediate.
- **J-065 / J-068 / J-070** — count/canvas/negation binding batteries, hours each with detector autoscoring.

## 7. Co-run infrastructure (biggest cost amortizations)

18 clusters in `judge_B.json → co_run_clusters`. The three that matter most for scheduling: the **student_ladder_rig** (one distillation ladder serves 12 readouts across H+J — the wave's largest compute amortization), the **multi_seed_sampling_rig** (8 dispersion/uncertainty ideas across H+J share k-seed sampling), and the **human_preference_protocol_pool** (one rater pool amortizes all 6 human studies; without it gen_h's preference-study block is the wave's dominant labor cost).

## 8. Anomalies protected (29)

G-033, G-046, G-050, G-054, G-058, G-065, G-083, G-096; H-008, H-009, H-025, H-054, H-069, H-080, H-085, H-090, H-094, H-096; J-008, J-025, J-043, J-052, J-058, J-063, J-067, J-080, J-086, J-102, J-104. Standouts: G-058 (post-cutoff time-travel evaluation), H-080 (enhancement alters lip micro-motion — safety-relevant and cheap), H-085 (photo priors contaminate scientific imagery), J-043 (layout-tier memorization — an unmeasured second tier), J-086 (shared-VAE ecosystem correlates "independent" models' errors), J-104 (video memorizes at lower duplication thresholds).

## 9. Deliberate tensions kept (adjudicate by experiment, not dedup)

H-037 vs J-056 (dispersion misallocated vs well-localized); G-099 vs J-062 (agreement as harm estimator under shift); H-002 vs H-095 (measured degradations vs degradation diversity); H-099 vs J-079 (few-step fidelity equivalence vs 1-step discontinuity); G-061 vs J-016 (low-level robustness by model family); cross-wave G-017 vs accepted A-091 (self-training winner vs self-training collapse).

## 10. Caveats / handoff

1. **kill/merge ≠ bad idea**; Consolidator may resurrect anything; all merge targets are stated.
2. **Zero T3 keeps.** Closest calls are scale-gapped T2 pilots (G-030, G-063, G-064, H-047): recorded tiers price the pilot; the at-scale decisive versions are effectively T3.
3. **Judge A (w3) diff still owed:** expected friction points are the 3 cross-wave merges, 2 cross-shard merges, and the single kill.
4. **Family-cap pressure escalated, not force-resolved:** sample_dispersion_uncertainty sits at 8 members post-merge (two of them a kept tension); distillation family at 12 distinct instruments over one shared rig — recommend Stage-2 slot caps rather than judge-time merges (`judge_B.json → family_cap_pressure_notes`).
5. **Score-5 rubric** here is "≤ 1 GPU-day decisive on public assets" (132 keeps); do not compare against w2's stricter "afternoon" count without this note.
6. Per-id verdicts with tier, score, runnability, flags, and `gate5_retrofit_needed`: `judge_B.json → verdicts` (304 records). Kept ideas with annotations: `accepted_shard_B.jsonl` (283 lines).
