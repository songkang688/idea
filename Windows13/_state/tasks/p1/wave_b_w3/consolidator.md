# P1 Wave B — Consolidator, Wave 3 sub-wave w3_GHJ (generators G+H+J)

- **task_id:** `p1_wave_b_w3` | **role:** `consolidator` | **windows_id:** `Windows13` (locked, `windows_path: Windows13`, `window_locked: true`)
- **branch:** `cursor/p1-wave-b-consolidator-w3-bf20`
- **Canonical base:** `origin/cursor/p1-wave-b-consolidator-w2-3111` (494-line `ideas_master.jsonl`, preserved verbatim as the append base). The branch was fast-forwarded through `origin/cursor/p1-diversity-audit-consolidator-w2-942c` (a descendant that does not touch the master) so the w2 diversity-audit ledger rows 13–15 and exploration state are preserved — the same precedent the w2 consolidator followed.
- **Scope:** G+H+J only. gen_k/l/m/n/o/p/u were **not** judged, merged, or appended; they await their own waves.
- **Epistemic status:** novelty of every accepted idea remains UNVERIFIED. No citations, thresholds, labels, or numbers were invented anywhere in this consolidation.

## 1. Inputs

| Input | Branch | Verdict counts |
|---|---|---|
| Judge A (dedup) | `origin/cursor/p1-wave-b-w3-judge-a-dedup-e60e` | keep 260, kill_or_merge 44 |
| Judge B (feasibility) | `origin/cursor/p1-wave-b-w3-judge-b-feasibility-2e78` | keep 283, merge 20, kill 1 |
| Judge C (adversary) | `origin/cursor/p1-wave-b-w3-judge-c-adversary-e10f` | keep 254, merge 44, kill 6 |
| gen_g_domain_shift | `origin/cursor/p1-gen-g-domain-shift-0165` | 100 ideas, legacy 13-field schema |
| gen_h_sr_restoration | `origin/cursor/p1-gen-h-sr-restoration-1829` | 100 ideas, legacy 13-field schema |
| gen_j_diffusion_model_science | `origin/cursor/p1-gen-j-diffusion-science-3470` | 104 ideas, full gate schema |
| Commissioning gates | `origin/cursor/p1-diversity-audit-consolidator-w2-942c` | GATE-5 retrofit-or-remand, GATE-6 judge labels, family cap ≤6 |

All 304 ids were ruled on by all three judges (verified mechanically from the judge JSON files; zero uncovered ids, zero unknown ids).

## 2. Reconciliation policy (w1/w2 policy, extended for GATE-5)

1. ACCEPT if ≥2 of 3 judges vote keep; KILL if not accepted and ≥2 vote kill; MERGE otherwise.
2. Merge target = majority target among proposing judges; ties broken toward dedup-specialist Judge A; all targets validated to land in an accepted record, following chains.
3. Judge A's master-target `kill_or_merge` entries count as merge-into-master votes; its single standalone kill (G-068) counts as a kill vote.
4. 3-way keep/merge/kill splits resolve to MERGE (w1 fallback) — fired once (J-091).
5. **GATE-5 split applied after voting:** accepted gen_j records (104/104 schema-compliant) are appended to the master; accepted gen_g/gen_h records (0/100 and 0/100-usable kill thresholds) are **remanded**, not appended and not content-rejected.
6. Outvoted kill rationales travel as `judge_dissent` on the surviving record and route to the GATE-8 novelty lane.

## 3. Outcome

| Quantity | Value |
|---|---|
| Input | 304 (G 100, H 100, J 104) |
| **Accepted by majority** | **271** (G 84, H 89, J 98) — 232 unanimous, 39 by 2-1 |
| **Appended to `ideas_master.jsonl`** | **98** (gen_j only; master 494 → **592** lines, all parsed, 592 unique id_seeds) |
| **Remanded pending GATE-5 retrofit** | **173** (gen_g 84, gen_h 89) → `remand_gate5.jsonl` |
| Merged | 31 (22 into wave-3 accepted records, 9 into wave-1/2 master ids — no master record modified) |
| Killed | 2 (G-002 by B+C over A; G-068 by A+C over B) — both UNVERIFIED known-result assessments, resurrectable via GATE-8 |
| Checksum | 271 + 31 + 2 = 304; 98 + 173 = 271 |

## 4. Headline conflict: G-025 (C kill vs A+B merge-primary) — resolved, no meta-judge

Judge C killed G-025 as an unverified restatement of the published fair-selection ERM-matches-DG-algorithms result and wanted G-026 as surviving primary; Judges A and B both kept G-025 and merged G-026 into it. **Resolution: majority rule — G-025 kept as merge primary absorbing G-026 (keep 2-1, merge 2-1).** Written rule: a minority kill against a keep/merge-primary majority stands down, but its rationale is preserved verbatim as `judge_dissent` on the surviving record and routed to GATE-8; because G-026's content is absorbed via `merged_from`, C's preferred surviving primary is recoverable without loss if GATE-8 later upholds the kill. G-025 is a gen_g record, so it sits in the remand queue (not the master) until GATE-5 retrofit.

Other recorded reconciliations (full detail in `decision.json`):

- **J-091 (3-way split: A merge→J-093 / B keep / C kill)** → merge into J-093 per the w1 fallback; C's published-schedule-correction rationale and B's keep travel with the record.
- **J-090, J-099** (C kill vs A+B keep) → kept 2-1 with C's kill reasons as dissent; **G-068** (A+C kill vs B keep) → killed 2-1 with B's dissent; **G-002** (B+C kill vs A keep) → killed 2-1.
- **Merge-target ties:** G-031 → G-093 (A's target over C's C-084); G-052 → A's target G-071, whose own 2-1 merge lands the chain in master C-023.
- Judge A's 11 master-collision ports (G-055, G-057, G-058, G-069, G-072, G-074, G-078, G-091, H-050, H-056, H-061): 6 confirmed by ≥2 judges and absorbed into master ids (C-023, C-028, C-029, C-032, C-077 ×2, B-085 ×2 — 9 total merges into master incl. chain and cross-checks); the remaining 5 (G-057, G-058, G-072, H-050 + G-054) were **kept** by B+C majorities and carry A's collision flags as dissent for GATE-8.

## 5. GATE-5 policy: schema-only REMAND (option a) — no zero-threshold records entered the master

All three judges independently measured gen_g 0/100 and gen_h 0/100-usable pre-registered kill thresholds (H-066/H-072 numerals are scale/bit-depth descriptors) and 0/200 `evidence_label` dicts, and all three recommended schema-only repair-or-remand rather than content rejection. Judge A: "they must NOT be merged threshold-less into the master." The commissioning prefers not flooding the master with zero-threshold records. Accordingly:

- **Appended:** only the 98 accepted gen_j records — every appended wave-3 record carries a numeric kill threshold inside `falsifiable_prediction` and an `evidence_label` dict (verified 104/104 on the raw shard by this consolidator's own re-scan; no separate-field normalization was needed, only master-schema metadata was added).
- **Remanded:** all 173 accepted gen_g/gen_h records, written with full fields, judge votes, dissents, and `merged_from` to `Windows13/_state/tasks/p1/wave_b_w3/remand_gate5.jsonl`, each flagged `gate5_deferred: true` with `gate5_missing[]` and `remand.lane = p1_wave_b_w3_gate5_repair`. The repair lane must retrofit thresholds/labels (and GATE-4 asset names; gen_h GATE-3 time bounds) from each record's own experiment text **without inventing results**, after which a consolidator appends them. They are accepted-on-content and must not be re-generated or re-judged from scratch.
- **Invented by this consolidator: nothing.** Zero thresholds, labels, assets, or numbers.

## 6. GATE-6 and family caps

- GATE-6 recorded, not enforced (Stage-2 instrument): genre quotas must use judge labels — gen_j self-declares 35.6% constructive vs ~19% by Judge C's strict phrasing audit; gen_g is debunk-dominant and likely violates the ≤40% pure-debunk quota. Judge C's labels are preserved per-record.
- Family caps: judge-time merges already fired inside the over-cap families; the three cells still over cap (dispersion_as_uncertainty 7, generator_memorization_primary 8, cheap_predictor_of_outcome g7/h1/j4) contain members that ≥2 judges kept as mechanistically distinct, so forced consolidator merges would override keep majorities — deferred to Stage-2 slot caps exactly as Judges B and C recommend, with C's protected ids recorded.

## 7. Canonical state updates

- `ideas_master.jsonl`: 494 → **592** lines (98 gen_j records appended; every line JSON-parsed; 592 unique id_seeds; no duplicate id_seeds; wave-1/2 records untouched).
- `research_state.json`: `total_ideas` 494 → 592; `idea_counts` extended with `p1_wave_b_w3` (incl. remand accounting); `exploration.wave_b_w3_consolidation` and `last_consolidator` updated. Stage 1, `windows_id` Windows13, `window_locked: true`, windows_path all unchanged.
- `research_ledger.md`: rows 16–18 appended.
- `window.lock.json`: **untouched.**

## 8. Handoff

1. **GATE-5 repair lane** (`p1_wave_b_w3_gate5_repair`): retrofit + append the 173 remanded gen_g/gen_h records — highest-priority follow-up; the master jumps to 765 when it lands.
2. **Remaining wave-B shards:** gen_k (105, on origin) and gen_l/gen_m/gen_n/gen_p (+ gen_o/gen_u when pushed) need their own judge waves (`p1_wave_b`).
3. **More generators** (`p1_wave_a_more_generators`): 592 accepted is still far below the 1000+ Stage-1 target; the diversity-audit queue (gen_p/o/n/u, then gen_q/r) stands.
4. **Diversity audit:** due — 271 acceptances this wave (98 on master + 173 remanded); the audit should run on the post-repair master (765) or now if counting remanded acceptances; last audit ran at 494.
5. **GATE-8 novelty lane:** owed for the 46 master-flagged keeps, the B/C watchlists, both kills, and every outvoted kill rationale (G-025, J-090, J-099, J-091).
