# P1 Diversity Audit 1 — Auditor B (SAM+X / LoRA+X / loss+X pseudo-innovation detector)

- **task_id:** `p1_diversity_audit_1_B`
- **windows_path (LOCKED, read-only):** `Windows15` — lock and `ideas_master.jsonl` untouched; this task writes only under `tasks/p1/diversity_audit_1/auditor_B/`.
- **input:** `Windows15/_state/ideas_master.jsonl` (271 accepted ideas) from `origin/cursor/p1-wave-b-batch001-consolidator-7c96` @ `b8d60bce42ab0a9f0f7b35278454d65d59f01331`
- **machine-readable results:** `findings.json` (all idea_id lists validated against the master; regenerable via `build_findings.py`)

## 1. Verdict in one paragraph

The accepted corpus is unusually hypothesis-first. Naked permutation pseudo-innovation ("bolt X onto SAM/LoRA/the loss and claim novelty") is rare: **6/271 (2.2%)** are archetype-dominant as written — and all six already carry `mutation_required` from batch_001 consolidation, so the in-batch gate (judge_B) held. Adding five archetype-forward ideas whose headline claim is still the permutation payoff brings the must-fix band to **11/271 (4.1%)**. The full permutation *surface* — every idea whose experimental vehicle is a method/recipe/component swap, even when a genuine falsifiable hypothesis rides it — is **43/271 (15.9%)**. The larger diversity risk is not permutation but **template monoculture**: four claim skeletons are instantiated 8–23 times each, and 45% of the T01 shard orbits LoRA/PEFT mechanics.

## 2. Fraction estimates

| Band | Definition | Count | Fraction |
|---|---|---|---|
| Tier 1 | Archetype dominates; hypothesis thin, borrowed, or lives in another idea. Must be rewritten before Stage 2. | 6 | 2.2% |
| Tier 1 + 1.5 | Adds archetype-forward ideas where a real diagnostic exists but the permutation payoff is the headline claim. | 11 | 4.1% |
| Tier 2 surface | Any permutation vehicle, including redeemed instances (flag-and-keep standard). | 43 | 15.9% |
| Clean | No permutation archetype. | 228 | 84.1% |

## 3. Worst offenders (ranked)

**Tier 1 — archetype-dominant as written (all already `mutation_required`; do not promote un-rewritten):**

1. **W15-B001-A-100** — nearest-centroid LoRA router over frozen features. Standard embedding gating; the interesting premise (linear domain separability) is assumed true, and the deliverable is a deployment assembly.
2. **W15-B001-A-052** — k-center/core-set active learning transplanted verbatim onto SAM-LoRA; "coverage beats random" is the original core-set claim.
3. **W15-B001-A-084** — self-consistency test-time adaptation (TENT/MEMO family) + SAM; its only scientific content (inconsistency localizes errors) is explicitly borrowed from A-009.
4. **W15-B001-C-028** — motion-sparsity router dispatching to specialist models; Module A+B assembly with the physics signature left as an assertion.
5. **W15-B001-A-056** — SAM-proposes/human-verifies annotation workflow; the falsifiable core (low-rank updates cannot memorize incoherent errors) already lives in A-053.
6. **W15-B001-A-060** — query-by-committee active learning with the multimask heads as committee; the AL race is the deliverable.

**Tier 1.5 — archetype-forward; promote the diagnostic to the headline before Stage 2:**

7. **W15-B001-B-097** — agreement-ordered curriculum; "transferable boundary policy" mechanism under-specified, hard to isolate from generic curriculum effects.
8. **W15-B001-A-096** — label-free consistency adaptation; the load-bearing claim is a benchmark race ("beats 10–20-image supervised LoRA").
9. **W15-B001-B-098** — PCGrad-family gradient surgery for multi-organ training; keep the directional-conflict diagnostic, drop "outperforms any reweighting".
10. **W15-B001-C-087** — matting-vs-segmentation pretraining swap; inductive-bias attribution is confounded by corpus content unless the binarized-label control becomes primary.
11. **W15-B001-A-064** — "recalibrate the uncertainty pathway only"; a value-proposition permutation over which component to retrain.

**Auditor-B additions to the tier-2 surface** (genuine hypotheses on permutation vehicles; kept, tracked for balance): B-012 (early-stopping schedule), B-037 (operator swap), B-047 (multi-head architecture), C-003 (head swap), C-075 (output-head redesign), C-076 (Probabilistic-U-Net-family method).

## 4. Cross-check against the in-batch gate

Judge_B flagged 40/300 with `permutation_flag` at batch time; 37 survived dedup into the master (A-063, A-093, C-078 were absorbed as duplicates). This audit independently converged on the same 6 mutation-required ideas, confirms the 31 remaining flag-and-keep calls, upgrades 5 of them to tier 1.5, and adds 6 ideas judge_B did not flag. Total surface: 37 + 6 = 43. No accepted idea warrants outright removal on permutation grounds — the archetypes that would have justified drops were already screened out at generation (all 300 shipped falsifiable predictions) or gated with `mutation_required` at consolidation.

## 5. Template monoculture (the real diversity risk)

Each instance below has genuine content; the risk is portfolio-level redundancy at the Stage-2 cut (1000+ → 200), where these families should compete internally rather than each send every member forward:

| Skeleton | Count | Examples |
|---|---|---|
| "Metric/benchmark artifact X hides Y; re-evaluation flips rankings" | 23 (8.5% of corpus) | A-068..075, B-013..023, C-039..048 |
| "{Frozen-model byproduct} is a free {sensor/label/detector}" | 14 | A-009, A-061, A-062, C-011, C-030, C-031, C-034, C-057, C-060, C-062, C-063 |
| "Models learn the annotator/protocol artifact, not the anatomy/medium" | 14 | A-036, B-002..011, B-073, C-001, C-004, C-015, C-016 |
| "Gap lives in {component}; tuning only {component} matches LoRA" | 8 | A-008, A-015, A-016, A-032, A-064, A-081, A-082, A-083 |

## 6. Underweighted territories

Territory-level balance is fine (T01 93 / T02 89 / T03 89). The imbalance is method-orbit concentration: **42/93 T01 ideas orbit LoRA/PEFT mechanics** (peft_mechanism, counterintuitive_peft, capability_erosion, data_efficiency, peft_lifecycle). Underweighted axes to feed batch_002+ generation:

1. **Language/text-prompted & VLM-grounded segmentation** — ~2 ideas (B-086, C-032). Planned T05 covers this; require grounding-mechanism claims, not CLIP+SAM assemblies.
2. **Video/temporal/streaming segmentation outside smoke** — SAM-2-style memory behavior entirely untouched.
3. **Security/adversarial/spoofing** — 1 idea (C-099); natural sub-quota for T06 failure mining.
4. **Efficiency, distillation, scaling laws** — ~2 ideas (A-091, A-079); scaling-law measurement fits the corpus's metrology strength.
5. **Continual/lifelong deployment** — 3 ideas (peft_lifecycle), thin for a deployment-relevant axis.
6. **Fairness/equity/population bias** — 2 ideas (B-079, B-091); the medical territory especially warrants demographic-stratification hypotheses.
7. **Theory (identifiability, sample complexity, formal limits)** — 3 ideas, all T03 physics; zero formal-analysis ideas in T01/T02.
8. **Interactive/human-factors outside T02** — T02's human_ai_interaction question style ports directly to T01/T03.
9. **Instance/panoptic/amodal formulation science outside media** — formulation-level ontology questions proved fertile in T03; apply to solid-object territories.

## 7. Recommendations for the consolidator

- Enforce the existing gate: the 6 tier-1 ideas must be reformulated per judge_B's salvage notes before Stage-2 promotion; re-center the 5 tier-1.5 ideas on their diagnostics at the same checkpoint.
- Add a **negative-control requirement** to the generation contract: every idea states the control/dissociation separating its mechanism claim from "the new combination just works better".
- Cap per-batch instances of a single claim skeleton (suggest ≤5) at generation time.
- For any "method A vs method B on benchmark C" experiment, require the predicted mechanism signature distinguishing a win from generic capacity/tuning effects (per A-068's own finding).

## Caveats

- No literature verification was performed; archetype family names (core-set, TENT/MEMO, PCGrad, Probabilistic U-Net) are pattern-matching references, not verified prior-art judgments.
- Tiers grade the ideas **as written** in `core_hypothesis`; several tier-1/1.5 ideas contain salvageable science, which is why the recommendation is mutation, not removal.
- This is one of the diversity-audit passes; the fraction estimates are one auditor's rubric and should be reconciled by `p1_diversity_audit_consolidator`.
