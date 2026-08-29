# P1 Diversity Audit round 3 — Auditor B (quality / cheap-kill / constructive-vs-debunk / blind spots / queue)

- **Windows**: Windows13 (locked, `windows_path: Windows13`) — identity untouched, canonical files read-only.
- **Role**: `auditor_B_quality_blindspots`. Independent pass first; auditor A w3 read only afterwards for cross-check (§8).
- **Audited set**: `Windows13/_state/ideas_master.jsonl` @ `origin/cursor/p1-wave-b-consolidator-w4-e8e2` (commit `2411f930`), **934 records** re-verified (934 lines, 934 unique `id_seed`, 0 duplicate one-liners, merge bookkeeping consistent). Shards: A 94 / B 85 / C 69 / D 79 / E 79 / F 88 / G 30 / H 16 / J 98 / K 102 / L 96 / M 98.
- **Audited at**: 2026-08-29T01:45Z. Novelty of all 934 ideas remains **UNVERIFIED**. No citations added anywhere in this audit.

## 1. Headline: quality is bimodal and the boundary is the gate-ruling date

Every quality instrument splits the master into the same two populations: the 494 records generated **before** the w1/w2 gate rulings, and the 440 generated **after**.

| Instrument | w1+w2 legacy (494) | w3+w4 additions (440) |
|---|---|---|
| GATE-1 kill threshold inside prediction (union: digit or explicit kill-clause) | **24/494 (4.9%)** | **440/440 (100%)** |
| GATE-2 structured `evidence_label` dict | 94/494 (gen_a only) | 440/440 |
| GATE-3 time/cost bound in fastest experiment | w1 27.0%, w2 23.6% | **84.8%** (K/L/M 100%, J 60%, repaired G/H low by design) |
| GATE-4 names public dataset AND model in experiments | ~1% (gen_a partial) | gen_m 96/98; gen_k+gen_l 0–2% (all 198 correctly `gate4_deferred`) |

The gates work at generation/judge time and **nothing is retrofitting the stock**. Portfolio GATE-1 compliance is 464/934 (49.7%). The debt ledger is exact: 470 legacy no-threshold records + 7 gen_k `gate1_qualitative_threshold` numeric retrofits + 127 remanded G/H records. The w2 decision parked legacy normalization in `stage2_selection_notes` **without an owner** — my top recommendation (R1) is to commission that retrofit lane now, in parallel with w5 judging, because it is mechanical and it blocks all programmatic Stage-2 ranking.

Detail worth recording: of the 20 w3/w4 records without a digit in the prediction, all are tracked (15 gate5-repaired G/H verbal-exact bounds; 5 gen_k no-digit predictions, a strict subset of the 7 flagged ids). Zero untracked threshold gaps in the new waves.

## 2. Cheap-kill quality

- `fastest_falsification_experiment` carries a machine-readable time/cost bound on 498/934 (53.3%). gen_k/l/m are at 100%; gen_f is worst legacy (7/88 on this instrument).
- The 16 master gen_h records have **0/16** time bounds — correct behavior by the extract-only repair lane (it refused to invent costs), but it means the restoration records that did survive are the least cheap-kill-specified in the new waves.
- `needs_special_resources` exists on only 394/934 records; exactly two are `true` (J-063, M-030). The w4 decision's "sole nsr=true in the wave is M-030" is accurate for wave 4; J-063 is the w3 instance. Legacy cheapness remains self-asserted prose — my w1 32-id special-resource discount list is still the only instrument covering it.

## 3. evidence_label coverage: 400 missing, 100% backfillable

The dict is present on 534/934. The 400 dict-less records are exactly shards B/C/D/E/F — and **every one of them** carries the uppercase label vocabulary inline in its text fields, so the w2 "mechanically normalizable" claim is verified: parse-and-lift, no content authoring. Three dialects need an alias table before Stage-2 reads labels programmatically:

1. Canonical uppercase enum (A, G, H, L).
2. **`KNOWN PRIOR WORK`** — 196 records (all of gen_j and gen_m). Caution: blindly renaming to `VERIFIED PRIOR WORK` would **overclaim verification** the generators never did; map to an alias or keep with a lookup table.
3. gen_k lowercase snake_case (102 records: `expected_result_unverified`, `speculation_unverified`, …) — preserved verbatim at w4 by design.

Good news: `ACTUAL EXPERIMENTAL RESULT` is used **zero** times in 934 records — nothing fabricates having run an experiment.

## 4. Constructive vs debunk: improving, instrument-dependent, not yet rebalanced

Four instruments, one direction:

| Instrument | Scope | Constructive |
|---|---|---|
| Self-labels | J/K/L/M (394) | 141/394 = **35.8%** |
| judge_C labels (GATE-6-compliant) | K/L/M labeled (273) | 83/273 = **30.4%** |
| My strict phrasing regex | all 934 | 71/934 = **7.6%** (debunk 21.6%) |
| My hand-label, seeded stratified n=40 | all waves | **35% ± 15**; by wave: w1 3/10, w2 1/10, w3 5/10, w4 5/10 |

GATE-6 self-label inflation is reconfirmed in every w4 shard (K +1.8pt, L +8.3pt, M +5.5pt vs judge labels) — genre quotas must keep using judge labels. The honest portfolio headline is a **range (8–35%)**, not a point; what is unambiguous is that w3/w4 run 2–3x more constructive than w1/w2 on every instrument that can see the split, and debunk is still the plurality genre. Hold the rebalance verdict until in-flight gen_p (104 raw, ≥80% constructive mandate) is judged. My 71 strict-constructive ids join the three prior protected lists (w1 46, w2 62, C-w2 38) against genre-blind culling.

## 5. Remaining blind spots at 934

**Unowned / orphaned (the real gaps):**
- **Cross-field transfer: 0 primary, third consecutive audit.** I hand-inspected all 7 loose regex mentions; none is genuine vision↔audio/time-series/graph transfer science.
- **Attack science ~0.4% / fairness ~0.1% primary — orphaned by the gen_u policy block.** The strongest fairness seed, H-090 (face-enhancement demographic disparity), is in the **remand queue**, not the master.
- **Model lifecycle/continual: 4 primary records (0.4%)** — F-102, G-011, G-080, G-085. gen_m turned out to be within-run training dynamics, as the w2 decision predicted.
- Psychophysics 0.5% and active-learning folklore 0.6% — gen_q fold-ins, riding on gen_q dispatch.

**Thin but owned in-flight (do not duplicate):** scaling laws 2 primary, memorization/privacy 4 primary → gen_n; underwater **0**, industrial inspection 0 primary, microscopy 1, document/OCR 2, remote sensing 1 primary, agriculture 4 → gen_o; genre → gen_p.

**Filled since w2, confirmed:** diffusion science (98), 3D/video (102), LLM-agent (96), training dynamics (98). **Exception — restoration**: only 16 gen_h records reached the master; 73 accepted-on-content gen_h records sit remanded. The one w1 blind spot whose fill was undone by GATE-5. Closing Stage 1 with 16 restoration records silently re-opens it (→ R2).

## 6. Queue validation

**w2 queue execution**: gen_p/gen_o/gen_n dispatched exactly as ordered (104+100+100 raw on origin, verified read-only) and are in w5_NPO judging (judges A+B pushed, C pending — consolidation blocked on C). gen_u never dispatched (policy-blocked). gen_i stays retired. Letters a–p burned; q, r, s, t, v, w, x, y, z free on origin.

**Dispatch conditions — formally discharged by this audit:**
- **gen_r**: the w2 dispatch condition was this auditor's own w2 caveat (recheck cross-field coverage after wave-3 judging). Measured: 0 primary on the 934 master including judged G/H/J/K/L/M. **Condition MET — dispatch immediately.**
- **gen_q**: condition "after gen_g judged" MET. Accepted TTA boundary in master = G-003/006/007/011/012. **New caveat from this audit**: the hard anti-overlap list must also name the 7 *remanded* TTA-block ids (G-001/004/005/008/009/010/014) which can re-enter via a repair pass; G-002/G-013 were merged or killed.
- **gen_v**: w2 promotion trigger ("audit w3 if lifecycle coverage still ~0 after gen_m judged") is **MET** at 0.4% primary. Recommend promoting to the active queue alongside r/q.
- **gen_t**: trigger **NOT met** (w3 acceptance 89.1%, w4 97.0%, both ≫ 70%; "all six letters dispatched" is structurally unmeetable while gen_u is blocked — recommend rewriting the trigger to the 5 dispatchable letters). If commissioned, mandate must **exclude distillation**: I count 22 distillation-primary-ish records, including a 10-record gen_j block (J-019/049/059/072–078) plus K-010/K-015/M-069.

**gen_u disposition (divergence with auditor A, flagged for the consolidator):** A proposes new letter gen_w inheriting the blocked mandate verbatim. My position: the policy block attaches to the **mandate content**, not the letter glyph; a verbatim re-issue risks a second blocked dispatch. Recommend either a **re-scoped measurement-science mandate** (disparity measurement, certification-gap audits à la C-088, benchmark-confound audits à la C-034, restoration-fairness à la remanded H-090; explicit no-attack-recipes guard) under a fresh letter, or recording attack science as an accepted permanent blind spot. Occupied ground if re-scoped: C-034, C-083, C-086, C-088, C-097, A-075, A-077, D-059, and remand H-090.

**Remand lane**: 127 = 54 G + 73 H, verified against `remaining_remand.jsonl` and `research_state.json`. **No owner.** Extract-only repair is exhausted; the leftovers need thresholds that don't exist in their text, and inventing numbers is forbidden. Recommend a threshold-**authoring** lane with explicit provenance labels (`gate5_threshold_authored_by`, EXPECTED RESULT framing, never presented as generator content) or a labeled Stage-1 exit as a sub-pool — a ruling is owed before Stage-1 close because 934+127 changes the 200-cut composition.

**Capacity** (HYPOTHESIS arithmetic on verified counts): 934 + 304 in-flight × 0.77 blended acceptance ≈ **1168** — 1000+ clears on w5_NPO alone. q/r/v and the remand pool are diversity/quality plays, not capacity plays.

## 7. Citation integrity

14 records carry citation-like strings — the identical all-gen_a set known since w1/w2, all famous real works. The 440 w3/w4 appends contributed **zero** citation strings. **Zero fake citations found; this audit adds none.** GATE-8 novelty triage remains unstarted and has grown to 105 dissent-carrying records + the w2 73-id list + w4's 20-id watchlist — schedule before the 200-cut (R8).

## 8. Cross-check vs auditor A w3 (read after my independent pass)

**Independent agreements** (computed before reading A): 420/440 digit-bearing w3/w4 predictions (exact match, benignly different decompositions of the 20); 440/440 evidence_label dicts; same 14-record citation set; cross-field zero; gen_r priority-1; gen_q anti-overlap sharpening; ~1168 capacity; gen_t distillation shrink.

**Correction to A**: A's report says the gen_u-successor occupied-ground check is against "accepted H-090" — H-090 is **not** in the master; it is in the 127-record remand queue (verified in both files). Any successor commissioning must scan `remaining_remand.jsonl` too.

**Divergences for the consolidator** (none irreconcilable): gen_u successor mandate text (verbatim-inherit vs re-scope, §6); gen_v priority (A ranks 4th, my trigger analysis says the written w2 condition is met now); constructive headline (A's 10.8% point vs my 8–35% instrument range — same direction, different instruments; adopt a range).

## 9. Recommendations (ranked)

1. **R1** Commission the legacy retrofit lane now: 470 GATE-1 thresholds n/a→owed decision, 400 evidence_label lifts, 7 gen_k numeric retrofits, label-dialect alias table. Mechanical, parallelizable, blocks Stage-2.
2. **R2** Rule on the 127 remands (threshold-authoring with provenance vs labeled exit). 73 are the restoration territory; H-090 is the fairness seed.
3. **R3** Dispatch gen_r (condition discharged here) and gen_q (add remanded TTA ids to its ban list).
4. **R4** Promote gen_v (trigger met, 0.4% lifecycle coverage).
5. **R5** Rule on gen_u successor: re-scoped measurement-science mandate preferred; never re-issue the blocked mandate verbatim.
6. **R6** Rewrite gen_t trigger (5 dispatchable letters) and shrink its mandate to exclude distillation.
7. **R7** Hold the genre verdict until gen_p lands; measure with judge labels (GATE-6); 4 protected constructive id-lists now in force.
8. **R8** Start GATE-8 novelty triage before the 200-cut.

## 10. Scope compliance

Canonical files untouched (`ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json` carried verbatim from the canonical tip). Files written: only the three `diversity_audit_w3/auditor_B.*` outputs. Own branch `cursor/p1-diversity-audit-w3-auditor-b-f4db`; no force-push; Windows13 identity unchanged; off-master reads were read-only (gen_n/o/p line counts, remand queue, auditor A post-pass).
