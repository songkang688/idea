# P1 Diversity Audit 1 — Consolidator Report

- **task_id:** `p1_diversity_audit_1_consolidator`
- **window:** Windows15 (locked; `window.lock.json` untouched)
- **date:** 2026-08-28
- **corpus audited:** `Windows15/_state/ideas_master.jsonl`, 271 accepted ideas @ `b8d60bc` (batch_001 consolidation)

## 1. Inputs merged

| Auditor | Focus | Branch @ head |
|---|---|---|
| auditor_A | mode collapse / cluster crowding | `origin/cursor/p1-diversity-auditor-a-d203` @ `fc9c24f` |
| auditor_B | permutation pseudo-innovation (SAM+X / LoRA+X / loss+X) | `origin/cursor/p1-diversity-audit-1-auditor-b-10e4` @ `829c476` |
| auditor_C | contrarian/stance balance, schema forcing, blind spots | `origin/cursor/p1-diversity-audit-1-auditor-c-79d3` @ `e106a3b` |

All three fork from the same corpus head and write disjoint paths; the git octopus merge was textually conflict-free. Every conflict below is semantic and resolved by an explicit rule (DR1–DR9 in `decision.json`).

## 2. Conflicts found and how they were resolved

1. **Territory naming (the one real collision).** Auditor_C proposed its own advisory T07–T16 registry (capability rehabilitation, scaling, video, constructive harvesting, …). The locked P1 registry (state_reader queue v1, re-confirmed by the parent) already defines T07–T16 differently (benchmark/dataset weaknesses, uncertainty/calibration, synthetic data, domain shift, negative results, contrarian hypotheses, SR/restoration, diffusion/generation, LLM/agent, cross-field transfer). **Rule DR1: a locked registry is never renumbered.** Auditor_C's IDs are rejected; its ten charters are kept as content and remapped into the canonical territories (mapping table in `decision.json#territory_remap`). Its video/temporal, theory, and security charters — which have no canonical territory — land in the two batch_006 second-pass shards, which queue v1 already reserved for audit-guided re-balancing.
2. **Constructive-deficit magnitude.** Auditor_A measured ~1% constructive by title; auditor_C measured 6.3% constructive and 16.2% directional-surprise by full text. **Rule DR2: full-text supersedes title-only** (titles under-count; auditor_C flagged exactly this nuance). Both agree on the direction, so the finding stands: the shortage is *directional* — anti-pessimism ~1.5%, null/equivalence 2.6%, affirmative 0%, meta-critique 0%.
3. **Deflationary mass.** Two independent methods agree: 40.2% (meta-family grouping, A) vs 39.1% (stance regex, C). **Rule DR3: adopt the concordance interval ~39–40%**, labeled EVIDENCE (heuristic), never KNOWN FACT.
4. **Removal question.** No auditor demanded any deletion (A: "rebalancing pressure, not pruning"; B: "mutation, not removal"; C: publishes a *protect* list). **Rule DR4: deletion requires unanimity; observed 0/3 → zero deletions.** `ideas_master.jsonl` is untouched.
5. **Flags.** Auditor_B upgraded 5 judge-kept ideas to tier 1.5 and added 6 to the permutation surface; auditor_C published 15 protected singletons. **Rule DR5: flags are unioned** into `decision.json#stage2_flag_register`; the batch_001 `mutation_required` six and `stage2_priorart_check_required` four carry over unchanged.
6. **Quota numbers.** Only auditor_C proposed a full numeric quota set; auditor_A independently proposed the identical 25% deflationary cap. **Rule DR6: adopt C's numbers, binding from batch_003**, advisory for the already-dispatched batch_002 generators, binding on batch_002 *judges* for the skeleton freeze.
7. **Schema fix.** A said "soften/alternate the `community_default_belief` field"; C said "replace it with a `claim_direction` enum + optional belief with provenance tag + `who_would_disagree`". **Rule DR7: C's proposal supersedes because it subsumes A's** and B raised no objection. The ledger's three standing questions remain values, not a mandatory oppositional template.

## 3. Canonical verdict (full text in `decision.json`)

- **No cluster-level mode collapse** (40 clusters, effective count 32.1, Gini 0.275).
- **Moderate meta-template crowding**: ~39–40% of the corpus shares one deflationary skeleton ("trusted signal X is actually artifact Y"), uniform across all three generators → pipeline/schema property, root-caused to the mandatory `community_default_belief`/`why_that_may_be_wrong` fields (300/300 filled, 0 affirmations).
- **Low permutation pseudo-innovation**: tier-1 is 6/271 (2.2%), all already gated `mutation_required`; the generation-time falsifiability gate held.
- **High stance asymmetry**: deflation:rehabilitation ≈ 25:1; affirmative and meta-critique classes empty. This is the audit's main corrective target.
- **Corpus action: keep all 271.** Correction happens at generation time, not by pruning.

## 4. What the next queue does about it

`next_task_queue.json` (queue_version 3) covers batches 003–006:

- **batch_003 (ready):** T07 benchmark/dataset weaknesses (steered hard away from the frozen 23-instance metric-reranking skeleton, toward MQ-01/MQ-07/validity maps), T08 uncertainty/calibration (constructive ≥30, grow HC-37/HC-38), T09 synthetic data (lineage/contamination MQ-10/11, scaling laws).
- **batch_004:** T10 domain shift (3D/remote-sensing/document domains, fairness), T11 negative results (the null-result engine, ≥40 null/equivalence, MQ-08/MQ-12), T12 contrarian hypotheses (contrarian-to-the-corpus: boundary-of-validity MQ-05, meta-critique MQ-06, adversarial replication, scale flips MQ-03).
- **batch_005:** T13 SR/restoration, T14 diffusion/generation, T15 LLM/agent — each with anti-assembly guardrails (the ledger forbids pseudo-innovation to chase sanctioned directions).
- **batch_006:** T16 cross-field transfer + two audit-mandated second-pass shards closing the consensus blind spots (video/temporal + interactive/human-factors; security/memorization + theory + efficiency).
- **Anti-debunk-only quota (parent requirement):** every shard must deliver ≥18/100 ideas that AFFIRM a default with its boundary of validity (≥3), propose null/equivalence (≥5), or rehabilitate a reported failure (≥10); deflationary framings capped at 25/100. T07/T12 and the batch_006 coverage shards carry raised minima.
- **Target math:** 271 now; ~510–535 projected after batch_002; batches 003–005 project the master across 1000 during batch_005 dedup; batch_006 provides margin and coverage regardless. `stage_completion` gate at ≥1000 unchanged.

## 5. Files written / not written

Written: `diversity_audit_1/decision.json`, `diversity_audit_1/next_task_queue.json`, this report, `consolidator/done.json`, ledger audit section, `research_state.json` `diversity_audit_1` pointer (all `windows_*` identity fields preserved).

Not written: `ideas_master.jsonl` (zero deletions, DR4), `window.lock.json` (locked).

## 6. Evidence policy

All audit statistics remain single-auditor regex/manual heuristics (EVIDENCE / MODEL SPECULATION per the auditors' own labels). No novelty verification was performed by anyone; no citations were consulted or invented; no sub-agent conclusion has been promoted to fact.
