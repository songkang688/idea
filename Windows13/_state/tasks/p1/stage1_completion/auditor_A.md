# P1 Stage-1 Completion — Auditor A (count / dedup) — Windows13

- **task_id:** `p1_stage1_completion` · **role:** `auditor_A_count_dedup`
- **windows_id / windows_path:** Windows13 / Windows13 · **window_locked:** true
- **audited master:** `origin/cursor/p1-wave-b-consolidator-w5-d795` @ `7338e5490f910a5079ce64bf2367a3c9a0619876`, file `Windows13/_state/ideas_master.jsonl`
- **audited_at:** 2026-08-29T02:00:48Z
- **This audit is read-only**: `ideas_master.jsonl`, `research_state.json`, and `window.lock.json` were not modified. Machine evidence in `auditor_A.json` (all numbers script-derived, none hand-typed).

## VERDICT: PASS

Stage-1 **quantity** and **internal uniqueness** are met on the canonical master. I do not end P1; Meta-Judge combines A/B/C.

## Check 1 — JSONL validity & count: PASS

- 1220 lines read; **1220/1220 parse as JSON objects** (0 invalid, 0 empty, trailing newline present, 0 exact duplicate whole lines).
- **Count gate independently re-verified: 1220 >= 1000.**
- Matches canonical claims exactly: `research_state.json` `total_ideas` = 1220, `idea_counts.stage1_accepted_total` = 1220, `p1_stage1_count_gate` = true.

## Check 2 — id_seed uniqueness & systematic collisions: PASS

- 0 records missing `id_seed`; **1220 unique id_seeds out of 1220** (0 duplicates).
- Systematic collision sweeps all clean: 0 case/whitespace-normalized collisions, 0 zero-padding collisions (e.g. `-007` vs `-7`), 0 nonstandard formats — all 1220 match `W13-P1-<LETTER>-NNN`, all prefixed `W13-`.
- Per-generator counts reproduce `research_state` shard bookkeeping exactly:
  A=94, B=85, C=69 (w1=248) · D=79, E=79, F=88 (w2=246) · G=30, H=16, J=98 (w3 appended=144) · K=102, L=96, M=98 (w4=296) · N=91, P=96, O=99 (w5=286). Sum = 1220.
- In-range numbering gaps (e.g. gen_h holds only 16 of 1..98) are absences from judged merges/kills and the 127-record gen_g/gen_h GATE-5 remand — **not** collisions.

## Check 3 — hypothesis-level duplicates / near-duplicates: PASS

- **Full pairwise scan** (not sample-only): 743,590 pairs; token-Jaccard over `core_hypothesis` + `one_line_idea` (732,188 pairs evaluated past a conservative length prune that can only discard pairs below 0.60).
- **0 pairs at Jaccard >= 0.80** (near-duplicate threshold); **0 pairs even at >= 0.60**; global max = **0.242**.
- Max pair manually reviewed: `W13-P1-E-029` (synonym-consistency audit of open-vocab masks) vs `W13-P1-E-054` (cross-lingual translated-query mask consistency) — same instrument family, clearly distinct hypotheses. Not duplicates.
- Exact-match scan on normalized text: 0 duplicate `core_hypothesis`, 0 duplicate `one_line_idea`, 0 duplicate `falsifiable_prediction`.
- Deterministic systematic sample (every 122nd record, 10 probes, nearest neighbor over all 1220): all nearest-neighbor Jaccard <= 0.188; no near-duplicate surfaced.

## Check 4 — records live under Windows13/: PASS

- `git ls-tree` of audited HEAD: the only `ideas_master*` file in the tree is `Windows13/_state/ideas_master.jsonl`.
- `git grep` over HEAD excluding `Windows13/`: **zero** `W13-P1-` id_seeds outside Windows13/.
- Content outside Windows13/ is only the repo `README.md` and `_p0_dispatch/` P0 bootstrap records (no idea records).
- `wave` field distribution inside master: w1=248, w2=246, w3=144, w4=296, w5=286 (sum 1220) — consistent with the append history.

## Unresolved items (flags, not count/dedup failures)

1. 127 accepted gen_g/gen_h records remain remanded off-master in `Windows13/_state/tasks/p1/wave_b_w3_gate5/remaining_remand.jsonl` (no extractable numeric threshold). Correctly excluded from the 1220 and not needed for the 1000+ gate, but Stage-2 must not silently drop them.
2. This audit certifies **internal** uniqueness only; novelty vs external prior art is out of Auditor A scope (O-002/O-031 judge_C prior-art dissents remain queued for GATE-8).
3. gate4_deferred asset-pinning flags (287 records across w4/w5) and threshold retrofits are quality debts outside the count/uniqueness gate, owned by the Stage-2 retrofit lane.

*No fake citations or invented numbers: every figure above was computed by script from the repository at the audited commit.*
