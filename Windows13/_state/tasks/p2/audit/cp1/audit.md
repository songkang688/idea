# P2 Audit — Checkpoint 1 (W13-P2-B001…B005)

**Verdict: PASS_WITH_REMEDIATION** — all hard compliance gates pass; remediation items are consolidator-side normalizations, not judge errors. No record was re-judged; no Keep/Kill changed.

## Coverage — PASS
- 305/305 verdict lines (5 × 61), ids exactly match the frozen membership in `state_reader/batches.json`; zero missing, zero extra, zero duplicates, zero `master_line` mismatches.
- Every record is `provisional` with `final_200_decision = not_made_here`; all `done_judge.json` counts match recomputed counts.

## Integrity — PASS
- `ideas_master.jsonl` / `window.lock.json` untouched: each judge branch adds only its own 3 output files. Canonical master @ `4a94eaf` verified (1220 lines, md5 `175193e5…`).
- `novelty_status = unverified` on all 305. Zero fabricated-citation / benchmark-number pattern hits across verdicts, review queues, and done files.

## Policy — PASS
- **M1**: 138 GATE-8 flags, all in `p1_gate8_novelty_triage`. Only 2 kills (A-077, B-056); both non-prior-art rationale, both routed to the review queue + triage lane. In-scope M1-named records C-016 and D-059 correctly parked Borderline in the lane. Zero silent prior-art kills.
- **M4**: 261 family notes; all 19 majority-keep→Borderline downgrades carry documented family/GATE-8 grounds (best-of-family enforced).
- **M5**: threshold field tracked on all 305; neither kill is threshold-absence-based — down-rank-not-kill respected.
- **M6**: debt tracked on all 305 (binding for A-012/A-053 per B001).
- **M7**: zero thin-territory kills; `adapter_ecosystem_continual` (n=5) fully preserved (2 Keep / 3 Borderline).

## Bias (reported, not re-judged)
- No mean-score sorting; splits resolved case-by-case with documented overrides.
- No high-risk/high-upside mistreatment: all 13 kill_lean carriers routed to Wave C (11 Borderline, 2 Kill-with-routing); A-032 protected from a compute kill.
- No minority-cluster suppression: zero kills at cluster size ≤5; weak size↔keep-rate tilt (r ≈ 0.29) — watch item.
- **Mild paper-shaped / popular-topic tilt at the Keep/Borderline margin**: negative-results (29% Keep), protocol-assumptions (33%), human-baselines (43%) vs 66.2% overall — none killed, all routed, but Wave C must give them a real second look (E4).

## Drift
| Batch | Keep% | Borderline% | Kill% | ReviewQ | GATE-8 density | GATE-8 high |
|---|---|---|---|---|---|---|
| B001 | 68.9 | 31.1 | 0.0 | 33 | 36.1% | 0 |
| B002 | 70.5 | 27.9 | 1.6 | 29 | 34.4% | 2 |
| B003 | 68.9 | 29.5 | 1.6 | 36 | 23.0% | 1 |
| B004 | 63.9 | 36.1 | 0.0 | 34 | 57.4% | 6 |
| B005 | 59.0 | 41.0 | 0.0 | 31 | 75.4% | 10 |

Keep% falls as GATE-8 density surges into C/D-prefix territory — plausibly content-driven, but cross-batch pooling requires normalization (E3). Kill rate ~0.66%: the real 200-cut pressure is fully deferred (E6).

## Escalations for consolidator
1. **E1 (low)** — normalize B002's `moderate` → `medium` severity vocab.
2. **E2 (med)** — reconcile per-record M5/M6 flags (99.3%/100%) with the global census (431/287 of 1220) before ranking on them.
3. **E3 (med)** — GATE-8-aware, per-batch-normalized comparison; do not naively pool Keep lists.
4. **E4 (med)** — counter the paper-shaped/popular-topic tilt when reviewing the 101 Borderlines.
5. **E5 (high)** — C-016 and D-059 must clear `p1_gate8_novelty_triage` before any 200-cut entry (M1 BINDING).
6. **E6 (med)** — plan the real cut mechanism: pooled Keeps (202) from 5/20 batches already exceed the 200 target.

Next: `p2_consolidator_cp1`. Machine-readable detail in `audit.json`.
