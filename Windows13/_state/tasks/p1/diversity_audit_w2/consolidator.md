# P1 Diversity Audit — Wave 2 Consolidation (Windows13)

- **Task**: `p1_diversity_audit_w2` / role `consolidator`
- **Branch**: `cursor/p1-diversity-audit-consolidator-w2-942c` (based on the canonical master tip `origin/cursor/p1-wave-b-consolidator-w2-3111` @ `929445d`)
- **Canonical accepted master**: 494 records in `Windows13/_state/ideas_master.jsonl` — line count and per-record JSON parse re-verified by this consolidator (494 lines, 494 unique `id_seed`). **Not modified by this task.**
- **Verdict**: A, B, and C are reconcilable. `irreconcilable = false`, `meta_judge_needed = false`.

## Inputs

| Auditor | Branch | Commit | Audited |
|---|---|---|---|
| A (mode collapse) | `origin/cursor/p1-diversity-audit-w2-auditor-a-7ef7` | `b974923` | 494 @ `929445d` |
| B (quality/blind spots) | `origin/cursor/p1-diversity-audit-w2-auditor-b-0688` | `2c1e08e` | 494 @ `929445d` |
| C (adversary) | `origin/cursor/p1-diversity-audit-w2-auditor-c-32c6` | `43a0856` | 494 @ `929445d` |

Prior context: w1 audit decision on `origin/cursor/p1-diversity-audit-consolidator-w1-25a0` (canonical count was 248 then; its gen_i..gen_p queue has been partially executed since).

## Off-master awareness (mandated scan, run before writing the plan)

`git fetch origin --prune` + `git ls-tree -r` over **all 164 origin branches** for `Windows13/_state/tasks/p1/generators/`:

- **In master (burned)**: gen_a, gen_b, gen_c (wave1); gen_d, gen_e, gen_f (wave2).
- **Generated off-master, judges pending (409 raw ideas — DO NOT recommission, NOT merged by this task)**: gen_g domain-shift (100, `p1-gen-g-domain-shift-0165`), gen_h SR/restoration (100, `p1-gen-h-sr-restoration-1829`), gen_j diffusion science (104, `p1-gen-j-diffusion-science-3470`), gen_k 3D/geometry/video (105, `p1-gen-k-3d-geometry-video-dc89`).
- **In flight / unpushed, treated as burned per dispatcher lock**: gen_l (LLM/agent vision), gen_m (training dynamics) — confirmed absent from every origin branch, letters burned anyway.
- **Retired permanently**: gen_i (see below).
- **Verified free on origin**: gen_n..gen_v (no branch names, no shard dirs).

## Consensus (all EVIDENCE, 3/3 unless noted)

1. Lexical duplication stays LOW (max Jaccard 0.246–0.282 depending on instrument; 0 near-dup pairs). Collapse is **family/genre-level**.
2. **SAM guard HELD**: subject share fell 35.1% → ~16–17.6%; wave2 added zero SAM records. Already below the 25% running target.
3. **Genre collapse is now the dominant axis**: 494/494 contrarian schema; C's split = debunk 51.4% + mixed 23.9% vs constructive 7.7%.
4. **Annotation/convention/label-noise pathology** is the largest surviving cross-shard family (39.3% mention-share; largest fingerprint cell 13 vs cap 6) → escalated to HARD BAN as primary subject.
5. **w1 quality gates were dead letters** in wave2 (kill thresholds 4/246; structured evidence_label 0/246; fingerprint tags 0/246) — but gen_j's 104/104 full compliance proves the gates are satisfiable. Off-master compliance is bimodal: gen_j FULL, gen_k divergent-schema, gen_h 2/100, gen_g 0/100 (pre-audit, excusable at generation time).
6. The w1 blind spots SR/restoration, diffusion, 3D/video, domain-shift are **already filled off-master** (409 raw ideas). **Judging, not generation, is the bottleneck.**
7. 1000+ is reachable with existing letters alone (A: ~903 → ~1230; C: ~910 → ~1235; HYPOTHESIS arithmetic on 81.8% observed acceptance). New letters are diversity plays.
8. **Zero fake citations** anywhere (14 real gen_a citations enumerated by C; 0 in the 409 off-master ideas; audits and this consolidation add none).

## Reconciliation (no meta-judge needed)

- **R1 — p vs o first**: A+C elevate gen_p to priority 1; B dispatches gen_o first and calls gen_p "still justified, urgency reduced". Adopted p(1), o(2) by 2/3; B's refinement kept — gen_p targets the debunk-heaviest clusters for debunk-to-repair conversion.
- **R2 — gen_m**: all three auditors treated gen_m as dispatchable; the dispatcher lock says it is **in flight** (shard absent from origin, letter burned regardless). Removed from the queue; B's 9 anti-overlap ids recorded for gen_m's *judges*; C's continual/open-world extension redirected to new reserve **gen_v** (cannot re-brief an in-flight generator).
- **R3 — letter map q/r/s/t/u**: B's letter assignments conflicted with A's; C (writing after reading A) kept A's map. Adopted A+C's map (2/3). **Every B territory survives under another letter**: security+fairness → gen_u; efficiency → gen_t; model lifecycle → gen_v; psychophysics → folded into gen_q.
- **R4 — gen_q TTA collision (C's catch)**: A proposed a TTA-primary gen_q counting master-only coverage; off-master gen_g holds 14 dedicated TTA ideas (G-001..G-014). gen_q commissioned **narrowed** to inference-time compute scaling / test-time search / TTT-for-dense (+ psychophysics, active-learning folklore), TTA-method critique HARD-banned as primary subject, dispatch only after gen_g is judged.
- **R5 — gen_r timing**: A+C say the w1 revisit trigger fired (coverage 0.0%, off-master shards leave it untouched); B says keep deferred until wave3 is judged. Commissioned (2/3) with B's caveat as the dispatch condition: dispatch only after wave-3 judging confirms coverage stays ~0.
- **R6 — constructive-count spread** (A 4.9% loose-w2 / B 25.2% clear-w2 / C 7.7% portfolio): instrument variance, not a factual conflict — same pattern as w1. C's 7.7% is the headline; protected-id set = union of B-w1 46 + B-w2 62 + C-w2 38 ids.
- **R7 — gen_t priority**: B ranked efficiency/deployment 1st; A+C keep it reserve. Reserve kept (2/3) but promoted to FIRST reserve with an explicit trigger (wave-3 acceptance < ~70% or queue exhausted); B's dissent recorded.

## gen_i: RETIRED permanently

Per C's attack A5 (and the parent's standing rule): w1 queued `gen_i_restoration_lowlevel`, but the territory was commissioned as **gen_h**. gen_i is a dangling letter with a stale mandate in a canonical file — retired, never to be reassigned. The letter registry is append-only.

## Commissioning queue (ordered)

| # | Task | Letter | Status | Key guards |
|---|---|---|---|---|
| 1 | `p1_gen_p_constructive_capability` | p | w1 letter, elevated 8→1 | ≥80% constructive, 0% pure audit; aimed at debunk-heaviest clusters; ≤10% SAM |
| 2 | `p1_gen_o_hard_domain_diversifier` | o | w1 letter, elevated 7→2 | underwater/microscopy/document-OCR emphasis; smoke/fire/transparent ban; ≤25% medical |
| 3 | `p1_gen_n_scaling_memorization_data_laws` | n | w1 letter, guards strengthened | anti-overlap vs 9 accepted gen_f ids; + emergence audit; no synthetic-pipeline framings |
| 4 | `p1_gen_u_adversarial_security_fairness` | u | NEW (C; folds B ranks 3+4) | attack/bias mechanism + numeric kill per idea; ≤20% eval-critique |
| 5 | `p1_gen_q_inference_time_compute` | q | NEW, narrowed (R4) | **after gen_g judged**; TTA-method critique banned as primary (gen_g owns G-001..G-014) |
| 6 | `p1_gen_r_cross_field_transfer` | r | NEW (w1-deferred, trigger met) | **after wave-3 coverage check**; both fields + transferred structure named |

Reserves (not commissioned): gen_t efficiency/deployment (first reserve, promotion trigger defined), gen_s embodied/interactive, gen_v model-lifecycle/continual (NEW). Next fresh letter: gen_w.

All queued shards must use the **full gen_j gate schema** (numeric kill threshold inside `falsifiable_prediction`, `evidence_label` dict, `family_fingerprint`, `genre`, `needs_special_resources`, `seg_metric_dependent`).

## Guards and gates delta (w1 → w2)

Kept all w1 global guards (SAM caps, calibration primary-cluster ban, smoke/fire/transparent ban, F1–F5 bans, structure quota, metric independence, genre quota, off-master awareness). Added/escalated:

- HARD BAN annotation/convention/label-noise pathology as primary subject (escalated from stop-feeding).
- Caps: cheap-predictor-of-outcome ≤3/shard; equalization/matched-budget-null ≤3/shard; small/dense/crowded-counting primary ≤5/shard.
- Realism-not-the-active-ingredient framing banned outside gen_f.
- Wave1-template-port rule: template re-instantiation requires a subject-native mechanism claim.
- Judges treat family membership as a merge trigger; fingerprint cap ≤6 enforced at judge time and Stage 2.

Quality gates for wave 3: the four w1 gates (numeric kill, evidence_label schema = gen_j canonical, time/cost bound on fastest test, no fake citations) **plus** named public dataset+model per experiment (B), a judge-time **retrofit duty** for the noncompliant gen_g/gen_h shards (attach thresholds + labels or remand; normalize gen_k's separate kill_threshold field at consolidation), genre self-label audits (C caught gen_j/gen_k inflation), and a ~10%-per-shard prior-art triage lane before Stage 2 (novelty is unverified for 494/494; the 73 permutation-flagged wave2 ids go first).

## Recommended next tasks (parallel tracks)

1. **`p1_wave_b_w3`** — judge wave over generated shards gen_g + gen_h + gen_j + gen_k (409 ideas; 3 judges + consolidator; G+H+J or G+H+K first is acceptable if 4 shards is too large). This consolidator did **not** merge any shard; that is the Wave B consolidator's job after a full judge wave.
2. **`p1_wave_a_more_generators`** — dispatch gen_p, gen_o, gen_n, gen_u now; gen_q and gen_r behind their dispatch conditions.

## Scope compliance

`window.lock.json` untouched; `ideas_master.jsonl` untouched (494); no generator shard copied into master; `research_state.json` updated in exploration fields only (Stage 1, Windows13, locked preserved); `research_ledger.md` append-only; no force-push; no fake citations.
