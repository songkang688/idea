# Windows14 Research Ledger

Append-only ledger of pipeline events for research window Windows14.

| timestamp (UTC) | stage | event | evidence |
|---|---|---|---|
| 2026-08-28T17:44:30Z | P0 | Windows14 workspace initialized and locked (windows_number=14, defined_by=P0, definition_status=canonical) | Canonical decision `_state/tasks/p0/windows_init/decision.json` (origin/cursor/p0-windows-init-consolidator-9906 @ 57133e0); pre-mkdir re-fetch 2026-08-28T17:43:55Z and pre-lock re-fetch both confirmed Windows14 absent on every origin branch head and PR head; no bump needed |
| 2026-08-28T19:08:14Z | P1 wave 1 | Wave 1 consolidated: raw 382 -> accepted 366, dropped 16 | `Windows14/_state/tasks/p1/wave1/accepted.jsonl` + `consolidator.md` + `consolidator.done.json`; workers A/B/C shards judged by judges A (clusters), B (pattern flags), C (advisory flags) |
| 2026-08-28T20:42:57Z | P1 wave 2 | Wave 2 consolidated: raw 638 -> accepted 623, dropped 15; canonical total 989 | `Windows14/_state/tasks/p1/wave2/accepted.jsonl` + `consolidator.md` + `consolidator.done.json`; workers A/B/C/D/E shards judged by judges A (clusters), B (pattern flags, two passes: A/B/D/E + worker_C), C (advisory flags) |

Pipeline target: `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`. Total ideas: 989. Status: Stage 1 in progress.

## P1 Wave 1 consolidation (2026-08-28T19:08:14Z) - counts only

- Raw ideas: 382 (worker_A 132, worker_B 126, worker_C 124; all id_seeds unique, judges A and B each covered all 382).
- Accepted: 366 -> appended to `ideas_master.jsonl` (was empty; 366 lines after append, no duplicates).
- Dropped: 16 (15 judge_A near-duplicate drops, 1 judge_B kill `w14p1c-050`; no overlap between the two sets).
- Conflicts recorded in `consolidator.md`: 37 (21 kept with mutate flag under keep+flag rule, 14 A-drop-vs-B-keep, 1 A-drop-vs-B-mutate, 1 A-keep-vs-B-kill).
- Advisory flags carried onto accepted ideas: 35 high_value, 54 convergence_family (deeper merge deferred to Stage 2), 19 novelty_claim_unverified, 21 mutate_recommended.
- Progress: 366 / 1000 accepted-idea target.
- Next queue: `Windows14/_state/tasks/p1/generator_task_queue.json` - wave 2, 3 slots (synthetic data + domain shift; SR/restoration + diffusion; negative results + contrarian); wave 3 planned for LLM/agent, cross-field, capped uncertainty/calibration top-up.

## P1 Wave 2 consolidation (2026-08-28T20:42:57Z) - counts only

- Raw ideas: 638 (worker_A 133, worker_B 126, worker_C 130, worker_D 124, worker_E 125; all id_seeds unique across shards; judge_A cluster membership covered all 638 exactly once; judge_B covered all 638 across its two passes, A/B/D/E on judge_B.flags.jsonl and worker_C on judge_B_worker_C.flags.jsonl).
- Accepted: 623 -> appended to `ideas_master.jsonl` as `w14-0367`..`w14-0989` (pure append; all 366 wave-1 rows byte-identical; dedup guard found no id collisions).
- Dropped: 15 (all judge_A near-duplicate drops; 0 judge_B kills).
- Conflicts recorded in `consolidator.md`: 22 (7 kept with mutate flag under keep+flag rule, 15 A-drop-vs-B-keep).
- Advisory flags carried onto accepted ideas: 44 high_value (45 issued, 1 on dropped w14w2a-036), 55 convergence_family (63 memberships issued, 8 on dropped ideas; deeper merge deferred to Stage 2), 21 canonical_overlap (wave1-overlap cross-references, merge deferred to Stage 2), 48 novelty_claim_unverified (JC2-QA-02 downgrade), 20 keep_with_note (judge_B), 7 mutate_recommended (judge_B), 5 cross_wave_near_dup (judge_A advisory vs wave1 ids).
- Progress: 989 / 1000 accepted-idea target.
- Next queue: `Windows14/_state/tasks/p1/generator_task_queue.json` - wave 3, 3 slots (LLM/agent; cross-field transfer; judge_C missing territories with constructive-genre quota). Uncertainty/calibration top-up NOT issued: over-represented per judge_C JC2-MC-04 (~87 wave-2 mentions plus wave-1's 34-idea family), so the conditional cap rule redirects the third slot to missing territories.
