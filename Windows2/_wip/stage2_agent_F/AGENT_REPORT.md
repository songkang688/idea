# Windows2 Stage-2 Agent F — Report (Batch A review)

Role: Independent Reviewer + Novelty Assassin. Scope: all 352 batch-A ideas (W2-A-0001..0352). I did not touch batches B or C, and I do not pick a final 3.

## What I did

1. Scored all 352 ideas on the 14 mandated dimensions → `scores.jsonl` (one JSON object per idea; fields: 14 dimension scores 1–5, `flags`, `verdict`, `note`).
2. Selected a shortlist of **75 keeps** (17 Tier A / 31 Tier B / 21 Tier C / 6 protected exceptions) → `shortlist.md`. 53 additional KEEP-grade ideas were demoted to BORDERLINE purely by budget and are flagged `tier-2-revivable`.
3. Killed **51** ideas → `kills.md` (reason families: already published, in-batch duplicate, ill-posed, tech-report scope, infeasible).
4. Ran an adversarial prior-work web attack on **28 ideas** (the 15 mandated + 13 I rank at/above them) → `prior_work_attack.md`. Outcome: 2 KILL, 15 MUTATE, 11 SURVIVE. One shortlist member (W2-A-0017) was demoted after a direct WACV 2026 hit.

Final tallies: **KEEP 75 / BORDERLINE 226 / KILL 51.**

## The 20 ideas I would bet a PhD year on

Ordered roughly by conviction; all survived or were strengthened by the prior-work attack (mutations noted).

1. **W2-A-0206** — SAM-fingerprint forensics + inheritance measurement. No prior work found; the data-genetics flagship. Pairs with 0264/0252.
2. **W2-A-0163** — Stuff-stuff transition-band atlas + band-aware evaluation. Sharp ontological claim, cheap, metric-changing; Boundary IoU is the only neighbor and it's a single scalar.
3. **W2-A-0150** — Scale-relativity of boundary ground truth. Attacks an unexamined axiom; underpins all C07 metrology; only industry folklore is adjacent.
4. **W2-A-0151** — Three-way boundary error budget (model/annotation/metric). The enforcement instrument for half the audit cluster; WACV'24 decomposition is model-side only.
5. **W2-A-0075** — Outcome-anchored audit of consensus erasing correct minority experts. STAPLE bias is known; clinical-truth erasure is unmeasured. Highest ethical stakes in the batch.
6. **W2-A-0145** — Findability bias: COD datasets contain only failed camouflage. Selection-bias bound on an entire benchmark family; no competitor found.
7. **W2-A-0121** — Mirror-geometry-verified phantom objects in puddles. Hidden, safety-relevant error class invisible to current metrics; cheap geometric verifier.
8. **W2-A-0249** — Reference-quality asymmetry inflating measured domain gaps. Recalibrates the UDA literature with a no-reannotation diagnostic.
9. **W2-A-0237** — Convention shift masquerading as domain shift (protocol-controlled re-annotation). Gap accounting, not another UDA method; links 0245/0226.
10. **W2-A-0349** — Functional vs photometric boundary conventions (with the curvature-minima control). Bridges established psychophysics to benchmark metrology.
11. **W2-A-0074** (mutated) — Coverage audit of volume CIs from pixelwise uncertainty; anti-conservatism factor + correlation-length law, conformal as upper bound.
12. **W2-A-0331** (mutated) — Gradient-flow instrumentation of Dice's per-instance starvation; tests whether blob-loss-style fixes equalize gradients or just outcomes.
13. **W2-A-0300** (mutated) — Ensemble-gain collapse by cohort era for dense models + pixel-level shared-error maps; the dense counterpart of the LLM correlated-errors results.
14. **W2-A-0071** — Which leaderboards have crossed their own noise floor. Field-level service; pairs with 0321/0322/0313 statistics keeps.
15. **W2-A-0100** — Provenance-level leakage audit of smoke/fire benchmarks. Cheap, decisive, likely devastating; the contamination cluster's easiest win.
16. **W2-A-0199** — Context-completion hallucination with association-strength dose-response. The segmentation version of a memorable cognitive result.
17. **W2-A-0215** — Protocol choice dominates median architecture improvement. The most subversive annotation-economics test; huge reinterpretation upside.
18. **W2-A-0061** — Topology lost at checkpoint-selection time, not training time. Cheap, counter-intuitive, immediately actionable for medical pipelines.
19. **W2-A-0352** (mutated) — Segmentation-free scalar measurement with the boundary-ambiguity interaction pre-registered (counting excluded — already answered).
20. **W2-A-0326** (mutated) — Property-decomposed signed context-value curves (region vs boundary). Must engage receptive-field folklore, but the decomposition law is unclaimed.

## 10 revived ideas (killed or demoted by others'/my first pass — kept alive with conditions)

These were BORDERLINE/tier-2 demotions or near-kills that I explicitly do NOT want silently lost:

1. **W2-A-0111** (tier-2) — Information-theoretically-invisible glass regions polluting benchmarks. Revive if the C05 cluster gets any slot: it's the human-ceiling instrument for glass.
2. **W2-A-0090** (tier-2) — Time-to-detect reformulation for smoke. The framing is right even though wildfire-detection literature is close; revive as the evaluation layer for any C04 keep.
3. **W2-A-0021** (tier-2) — Cheapest decisive AUROC comparison of SAM-uncertainty signals. Revive as the shared measurement backbone for 0001/0198 mutations (one GPU-day).
4. **W2-A-0065** (tier-2) — Real-click-vs-simulator gap in clinical interactive segmentation. RClicks-style work covers natural images; revive if a MICCAI-track slot exists.
5. **W2-A-0189** (tier-2) — Bidirectional pasting to separate context-prior from appearance deficit. Clean causal design; revive if COD/rare-class attribution matters to the PI.
6. **W2-A-0220** (tier-2) — Quality-quantity phase boundary for rough masks. Annotation-economics regime map with direct budget advice; revive for any applied track.
7. **W2-A-0226** (tier-2) — Gap-composition fractions per UDA benchmark. Revive as the explanatory layer inside the 0245 mutation (they should ship together).
8. **W2-A-0310** (tier-2) — Fresh-test-set replication (Recht-style) for dense prediction. Big but slow; revive if the PI wants one high-visibility field-service paper.
9. **W2-A-0315** (tier-2) — Ecosystem-scale patient-leakage forensics via anatomical fingerprinting. Revive if medical-data access is confirmed; the WSI leakage audit (arXiv:2607.12278) shows the appetite.
10. **W2-A-0017-sliver → 0203** — 0017 died to WACV 2026, but its expressivity question survives inside 0203 (masks no prompt can produce). Revive 0203 from tier-2 if the SAM cluster keeps a slot; it inherits 0017's motivation with a formal, un-scooped core.

## Bias audit (self-assessment)

- **Meta/audit vs method skew.** My keep list is heavily weighted toward measurement, forensics, and metrology (flags: metric-audit 40, forensic 18, statistics, contamination). Agent A's batch itself skews this way, but I amplified it: audits are cheap-to-falsify and survive either outcome, which my protection mandate rewards. Constructive/method ideas I kept as counterweight: 0107 (depth-dropout supervision), 0042 (amodal video), 0097 (shimmer channel), 0272 (design-file corpus), 0292 (procedural pretraining), 0345 (emergent capability). If the PI wants CVPR *method* papers rather than analysis papers, my ranking under-serves that and Tier C constructive entries should be promoted.
- **Familiarity bias.** I am most confident attacking SAM/medical/UDA clusters where literature is densest; my SURVIVE verdicts in psychophysics-adjacent areas (0150, 0349) and ecology-adjacent areas (0145) carry wider error bars because those literatures use different vocabulary. Confidence labels in `prior_work_attack.md` encode this.
- **Recency risk.** Several MUTATE verdicts (0301, 0300, 0205, 0148) sit in fast-moving 2025–26 niches; six months of arXiv could flip them to KILL. The 0017 demotion (killed by a WACV 2026 paper) is the cautionary example — I'd re-run the attack on any idea before it becomes a thesis chapter.
- **Duplicate handling.** Agent A's mutation chains created overlap families (0001/0021/0198 uncertainty-equivalence; 0017/0203 expressivity; 0074-family volumetrics). I killed/merged within families but a different reviewer might merge differently; scores.jsonl notes record the cross-references.

## What would change my ranking

1. **Venue target.** If the PI optimizes MICCAI, promote 0074/0075/0061/0331/0315; if CVPR/ICCV method tracks, promote the constructive Tier C (0107, 0042, 0097, 0272, 0292) over the audit block.
2. **Data access facts.** 0075 and 0145 are top-10 only if outcome-linked multi-rater data / telemetry-verified camera-trap archives are actually obtainable; without them they drop to mutation-only status. Same for 0107 (fleet depth logs).
3. **A single new arXiv hit** on SAM-mask provenance detection would demote 0206 from #1 to a mutation (inheritance measurement only). This is the highest-variance bet in my top 5.
4. **Compute budget.** My scoring assumed academic-lab compute. If large-scale retraining is off the table, 0292/0300/0345 weaken and the zero-GPU statistics keeps (0322, 0321, 0313) strengthen.
5. **Other agents' disagreement.** Ideas where I expect reviewer disagreement (flagged `disagreement-prone`, 27 kept) were deliberately protected; if D/E converge on kills for those, treat the disagreement itself as signal to escalate to the PI rather than majority-vote them away.

## Files written (all under `Windows2/_wip/stage2_agent_F/`)

- `scores.jsonl` — 352 lines, 14 dimensions + flags + verdict + note per idea.
- `shortlist.md` — 75 keeps in 4 tiers + protection audit + post-attack demotion record.
- `kills.md` — 51 kills grouped by cluster with reasons.
- `prior_work_attack.md` — 28 attacked ideas with citations, differences, remaining novelty, confidence, Reviewer-#2 lines, verdicts, mutations.
- `AGENT_REPORT.md` — this file.
- `parts/` — intermediate per-cluster scoring files (kept for audit trail).
