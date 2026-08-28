# P1 Wave B — batch_002 Consolidator Report (Windows15)

## Scope

Sole writer of canonical `ideas_master.jsonl` for this merge. Lock identity fields in
`window.lock.json` untouched. Base: `origin/cursor/p1-wave-b-batch001-consolidator-7c96`
(`b8d60bc`, ideas_master @ 271), fast-forward merged with
`origin/cursor/p1-diversity-audit-1-consolidator-ea44` (`0fad002` — a direct descendant of
the base, so the merge was conflict-free; the audit kept all 271 and did not touch
ideas_master). Batch_002 gen/judge artifacts were checked out per-path from their six
branches (each branch only touches its own shard directory — mechanically conflict-free).

## Inputs (KNOWN FACT)

| Shard | Branch | Count |
|---|---|---|
| gen_A (T04 Object detection) | `origin/cursor/p1-wave-a-batch002-gen-a-83d7` @ `decf0b3` | 100 ideas |
| gen_B (T05 VLM / dense prediction) | `origin/cursor/p1-wave-a-batch002-gen-b-0edc` @ `a70297e` | 100 ideas |
| gen_C (T06 failure mining) | `origin/cursor/p1-wave-a-batch002-gen-c-86e2` @ `b9a0d1e` | 100 ideas |
| judge_A (cluster + dedup) | `origin/cursor/p1-wave-b-batch002-judge-a-f0d4` @ `ba3ab58` | keep 278 / merge 16 / drop 6 |
| judge_B (permutation-kill) | `origin/cursor/p1-wave-b-batch002-judge-b-cc8c` @ `ed41ffe` | keep 286 / mutate 12 / drop 2 |
| judge_C (adversarial dedup) | `origin/cursor/p1-wave-b-batch002-judge-c-e0c7` @ `779c408` | keep 280 / duplicate_of 20 / drop 0 |

Judge counts re-verified against the raw verdict.jsonl files (300 verdicts each, ID sets
identical to the 300 generated ideas).

## Resolution rules

Rules R1–R7 carried over from batch_001 `decision.json`; one new rule was needed:

- **R2 dedup union** — removed if ≥1 dedup judge (A or C) names an explicit surviving
  target. Judge A drops that name a `duplicate_of` master anchor are dedup votes, not
  quality drops.
- **R3 chain-follow** — targets that were themselves removed are followed to the final
  surviving anchor. Two chains this batch: `B-022 → B-087 → B-017` and
  `B-030 → B-024 → C-045`. All multi-judge target sets converged after chaining (10/10);
  no cycles remained after R8.
- **R4 quality-drop majority (≥2/3)** — all 3 quality-drop votes were solo
  (judge_A: `C-038` prior-art risk; judge_B: `A-012`, `B-079` established-technique)
  and rest on prior-art judgments no agent citation-verified. Retained 2-1 with
  `stage2_priorart_check_required`.
- **R5 mutation passthrough** — 11 of judge_B's 12 mutates accepted with
  `mutation_required=true` + salvage note (`A-007, A-010, A-018, A-035, A-047, A-051,
  A-073, A-098, B-044, B-081, B-098`).
- **R6 precedence** — `B-083` had judge_B mutate + judge_A duplicate-of-master
  (`W15-B001-A-016`); dedup wins, salvage note preserved in decision.json.
- **R8 direction conflict (new)** — judges A and C agreed three pairs are single claims
  but named opposite survivors. Judge_C's survivor wins: it is the dedicated adversarial
  duplicate auditor, recorded confidence (high on all three), and audited against master;
  judge_A's notes on these pairs assert "same core claim" without arguing a survivor.
  Resolved: (`B-017`,`B-087`) → `B-017` survives; (`B-085`,`C-046`) → `C-046` survives;
  (`C-053`,`C-092`) → `C-053` survives.

## Outcome (KNOWN FACT)

- **Accepted: 272 / 300** (unanimous keep 255).
- **Removed as duplicate: 28** — 23 intra-batch, 5 into batch_001 master anchors
  (`B-072→W15-B001-B-076`, `B-083→W15-B001-A-016`, `C-001→W15-B001-A-003`,
  `C-064→W15-B001-C-033`, `C-070→W15-B001-A-005`). Overlap: 8 judge_A-only,
  7 judge_C-only, 10 both-convergent, 3 R8-resolved.
- **Quality dropped: 0** (3 solo votes overridden, flagged).
- **Canonical `ideas_master.jsonl`: 271 → 543 lines** (append-only; batch_001 lines
  byte-identical — the 5 master absorptions are recorded in decision.json instead of
  rewriting anchor lines).
- `research_state.json`: total_ideas 600, survivors 543, batches[2] added,
  diversity_audit_1 pointer preserved; `windows_*` identity/lock fields untouched.
- Ledger: batch_002 section appended.

## Advisory carryovers (not removals)

- judge_A: 38 master-near-duplicate watch entries, 9 prior-art-risk flags on kept ideas
  (carried as `judge_A_prior_art_risk_advisory` in accepted.jsonl), 4 internal
  contradiction pairs (each needs one resolving experiment matrix, per judge_A),
  12 cross-shard template twins kept.
- judge_C: 45 near-duplicate families, 12 protected competing pairs, 15 family flags —
  carried per-idea as `judge_c_flags`.
- Diversity audit contract v2 (stance quotas, skeleton freeze) binds generators from
  batch_003; checkpoint_2 (trigger at 500 accepted) is now due — recommend running it
  alongside batch_003 dedup.

## Evidence policy compliance

No citations invented, no benchmark numbers claimed, no experiments claimed run. All
accepted ideas remain HYPOTHESIS-level. All judge prior-art opinions carried as advisory
only. Consolidator added no novelty claims of its own.
