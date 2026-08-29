# Windows13 — Stage-1 Exploration Report

- **windows_id / windows_path:** Windows13 (window_locked: true, defined_by P0, lock file `Windows13/_state/window.lock.json` — untouched by this task)
- **Repository:** https://github.com/songkang688/idea
- **Pipeline:** 1000+ -> 200 -> 50 -> 20 -> 5 -> 3
- **Report role:** p1_stage1_report_writer (report only — this task performed no generation, no judging, no ranking, and no Stage-1 git consolidation; the git agent runs next)
- **Written:** 2026-08-29 (UTC)

## 1. Outcome

Stage-1 exploration for Windows13 is **COMPLETE** at **1220 accepted ideas**, exceeding the 1000+ gate (`p1_stage1_count_gate = true`, independently recounted by completion auditor A's full recount and auditor C's independent parse). The meta-judge combined verdict is **PASS_WITH_REMEDIATION** (`p1_stage1_complete = true`); Stage-1 idea generation is frozen at the 1220-record master. All remediation items are selection-side and route to P2 ranking rules or to the three named selection-integrity lanes queued at the diversity_audit_w3 consolidation — none requires more Stage-1 generation (completion auditor C explicitly found `more_generators_required = false`).

**P2 ranking has NOT been started.** This report summarizes exploration only and performs no ranking.

## 2. Canonical artifacts and paths

| Artifact | Path | Where |
|---|---|---|
| Canonical 1220-record master | `Windows13/_state/ideas_master.jsonl` | canonical content produced at `origin/cursor/p1-wave-b-consolidator-w5-d795` @ `7338e5490f910a5079ce64bf2367a3c9a0619876`; present verbatim (1220 lines, re-verified) on this report branch's base `origin/cursor/p1-diversity-audit-consolidator-w3-2535` @ `9ab4003` |
| Canonical state | `Windows13/_state/research_state.json` | same branches (total_ideas 1220, count gate recorded) |
| Append-only ledger | `Windows13/_state/research_ledger.md` | same branches |
| Meta-judge verdict (full remediation text M1–M8) | `Windows13/_state/tasks/p1/stage1_completion/meta_judge.json` + `meta_judge.md` + `done_meta_judge.json` | `origin/cursor/p1-stage1-meta-judge-267c` |
| Remand pool (127 records, off-master) | `Windows13/_state/tasks/p1/wave_b_w3_gate5/remaining_remand.jsonl` | on this branch |
| Per-wave decisions | `Windows13/_state/tasks/p1/wave_b_w{1..5}/decision.json`, `Windows13/_state/tasks/p1/diversity_audit_w{1..3}/decision.json` | on this branch |
| This report | `Windows13/selection_history/stage1_exploration.md` | this branch |

Completion auditor branches (inputs to the meta-judge): `origin/cursor/p1-stage1-completion-auditor-a-0e29` (A count/dedup — PASS), `origin/cursor/p1-stage1-completion-auditor-b-97f0` (B quality/diversity — PASS_WITH_REMEDIATION), `origin/cursor/p1-stage1-completion-auditor-c-3c0d` (C mode-collapse — PASS_WITH_REMEDIATION).

## 3. Pipeline waves (generation -> judging -> consolidation)

Every wave was judged by three independent judges (A dedup, B feasibility, C adversary) and reconciled by majority vote at a consolidator; all counts below are quoted from `research_state.json` / the wave `decision.json` files, computed mechanically from judge outputs.

| Wave | Generators | Input | Accepted | Merged | Killed | Appended to master | Master after |
|---|---|---|---|---|---|---|---|
| wave_b_w1 | gen_a (SAM/foundation/PEFT), gen_b (hard-domain dense prediction), gen_c (contrarian eval) | 302 | 248 | 47 | 7 | 248 | 248 |
| wave_b_w2 | gen_d (object detection), gen_e (VLM dense prediction), gen_f (synthetic data) | 302 | 246 | 54 | 2 | 246 | 494 |
| wave_b_w3 (w3_GHJ) | gen_g (domain shift), gen_h (SR/restoration), gen_j (diffusion model science) | 304 | 271 | 31 | 2 | 144 (98 gen_j + 46 GATE-5-repaired g/h); 127 accepted-on-content g/h records remanded off-master | 638 |
| wave_b_w4 (w4_KLM) | gen_k (3D geometry/video), gen_l (LLM-agent vision), gen_m (training dynamics/objectives) | 305 | 296 | 9 | 0 | 296 | 934 |
| wave_b_w5 (w5_NPO) | gen_n (scaling/memorization/data laws), gen_p (constructive capability), gen_o (hard-domain diversifier) | 304 | 286 | 18 | 0 | 286 | **1220** |

Totals per canonical state: 1517 generated, **1220 accepted on master**, 159 merged, 11 killed, 127 accepted-on-content but remanded off-master pending GATE-5 threshold disposition.

Interleaved audit/repair lanes:

- **Diversity audits** ran at master sizes 248 (w1), 494 (w2), and 934 (w3, decision at `Windows13/_state/tasks/p1/diversity_audit_w3/decision.json`); w3 landed cleanly (irreconcilable=false, meta_judge_needed=false) and queued the selection-integrity lanes named in §5.
- **GATE-5 repair lane** (`wave_b_w3_gate5`): 46 of the 173 remanded gen_g/gen_h acceptances were repaired strictly by extracting kill thresholds from each record's own text (zero thresholds invented) and appended; 127 remain remanded.
- **Stage-1 completion audit**: three completion auditors (A count/dedup, B quality/diversity, C mode-collapse) audited the identical master commit `7338e54`, followed by the meta-judge.

Diversity plays queued at w3 but not part of the 1220 master and **not Stage-1 obligations** under the verdict: gen_r / gen_w / gen_v (queued, not dispatched by this report) and gen_q (in flight, off-master). Their disposition belongs to P2 / named-lane supervision.

## 4. Meta-judge verdict

**PASS_WITH_REMEDIATION** (`origin/cursor/p1-stage1-meta-judge-267c`, decided 2026-08-29T02:28:00Z). Combination: auditor A PASS + auditor B PASS_WITH_REMEDIATION + auditor C PASS_WITH_REMEDIATION, with no inter-auditor factual conflicts. Headline auditor findings (quoted from the verdict, not re-measured here):

- **A (count/dedup):** 1220 valid unique JSONL records; 0 duplicate/colliding id_seeds; 0 near-duplicate pairs at Jaccard >= 0.60 over all 743,590 pairs; 0 records outside `Windows13/`; per-shard counts reconcile with state.
- **B (quality/diversity):** the GATE-5-compliant w3–w5 core (726 records) alone exceeds the 200-idea Stage-2 target 3.6x; 156 clusters, max share 1.15%; zero unlabeled records, zero fake citations (36 distinct citation strings all verified real), zero invented numbers, zero claimed experiments; tracked debts are per-record-flagged and lane-owned.
- **C (mode-collapse):** residual collapse is template-family-level and prior-art-exposure-level, not subject- or lexical-level; **more generators explicitly NOT required** (added volume would grow the template families that constitute the residual collapse).

Auditor B's dispatch-ordering concern (R7) was **waived** by the meta-judge (M8) with recorded rationale; no re-audit required.

## 5. Remediation items (pointers only — full binding text in `meta_judge.json` on `origin/cursor/p1-stage1-meta-judge-267c`)

These are preconditions on the Stage-2 200-cut, not on Stage-1 completion. This report tracks them; it does not execute them.

1. **GATE-8 novelty triage (M1, binding, before the 200-cut).** Owner lane `p1_gate8_novelty_triage` (queued at diversity w3, unstarted). Head of queue: W13-P1-O-002 and W13-P1-O-031 (judge-verified real prior art, retained 2-1 with dissents), then the five outvoted judge_C prior-art kills (C-016, D-059, K-020, K-069, L-012), the 141 judge_dissent carriers, and the w2/w4/w5 watchlists.
2. **Remand-pool disposition — 127 records (M2, binding, before the cut).** Owner lane `p1_wave_b_w3_gate5_repair_2` (queued, unstarted). The 127 accepted-on-content gen_g/gen_h records at `Windows13/_state/tasks/p1/wave_b_w3_gate5/remaining_remand.jsonl` (54 G + 73 H) must get an explicit repair-append or kill-with-decision; never a silent drop. They are correctly excluded from the 1220 and not needed for the count gate.
3. **Fingerprint controlled-vocabulary back-map (M3, binding, before mechanical slot caps).** Owner lane `p1_stage2_retrofit_lane` (queued, unstarted). All 680 free-text `family_fingerprint` strings must be back-mapped onto the controlled ~30-enum vocabulary mandated by the w3 decision; until then the cut applies the w3 genre-blind pooled caps (eval-subject pool <= 25% of the 200) and the cheap-predictor freeze rule.
4. **Family caps / forced best-of-family adjudication (M4, binding, at the 200-cut).** Owner: P2 rankers. Named sibling sets (e.g., J-051/J-076, E-029/E-054, B-060/B-065, F-019/F-023, N-061/N-070, C-003/C-004/C-057, the gen_e text-encoder-geometry block, the gen_m mechanics block, the variance/protocol-artifact, sim-to-real, and provenance-forensics families) must yield best-of-family only, never multiple undifferentiated siblings.

Additional tracked items (see M5–M8 in `meta_judge.json`): 431 soft-threshold records down-ranked on falsifiability and numeric-retrofitted before entering the 200 (M5, binding); 287 `gate4_deferred` records owe dataset+model pinning (M6); thin territories (fairness ~1, inference-time compute ~3, embodied 17, continual 10) protected from volume-based elimination (M7); ordering concern waived (M8, resolved).

## 6. Integrity attestations

- **No fake citations.** This report introduces no new citations; every citation string named here (Sea-thru / O-002; Tellez et al. / O-031) is quoted from the auditors' verified findings. Auditors A/B/C independently reported zero fabricated citations across all 1220 records.
- **No invented experimental results.** No experiments were run at any point in Stage-1; zero claimed experimental results exist in the master (auditor-verified). All predictions in the master are labeled per the evidence policy (HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT etc.).
- **Novelty remains UNVERIFIED** for all 1220 records. No prior-art search has been completed; GATE-8 (item 1 above) owns that lane and must complete before the 200-cut.
- **Canonical state untouched:** `ideas_master.jsonl`, `research_state.json`, and `window.lock.json` were not modified by this report task. Outputs of this task: this file and `Windows13/_state/tasks/p1/stage1_completion/done_report_writer.json`.
- **No git Stage-1 consolidation claim:** this task is the report writer only; the Stage-1 git consolidation commit is owed by the git agent (`p1_stage1_git_agent`), which has not run as of this report.

## 7. Next step

`p1_stage1_git_agent` — consolidate the Stage-1 completion artifacts (meta-judge verdict + this report) onto the canonical line. The selection-integrity lanes (items 1–3 in §5) run on their own queued track before the Stage-2 200-cut and do not block the git agent.
