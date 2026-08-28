# P1 Wave B — Judge B: Feasibility / Experimental Falsifiability / Cheap-Kill Design (Wave 1: Generators A+B+C)

- **task_id:** `p1_wave_b_w1` | **role:** `judge_B_feasibility` | **windows_id:** `Windows13` (locked)
- **branch:** `cursor/p1-wave-b-judge-b-feasibility-a49e`
- **Scope:** independent second judging pass over the same 302 ideas Judge A saw. I re-read all three generator shards myself and formed my own keep/merge/kill lists; Judge A's shard was consulted only afterwards as one input, and every agreement or disagreement below is informational for the Consolidator — nothing here is a reconciliation. Canonical state (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched.
- **Epistemic status:** NO novelty verified for any idea. Every `prior_art_risk` flag is this judge's unverified hypothesis. No citations asserted or invented.

## 1. Inputs

| Shard | Branch | Ideas |
|---|---|---|
| gen_a_sam_foundation_peft | `cursor/p1-gen-a-sam-foundation-peft-c8d4` | 102 (W13-P1-A-001..102) |
| gen_b_hard_domain_dense_prediction | `cursor/p1-gen-b-hard-domain-a13a` | 96 (W13-P1-B-001..096) |
| gen_c_contrarian_eval | `cursor/windows13-p0-init-implementation-d93f` | 104 (W13-P1-C-001..104) |
| judge_A (reference only) | `cursor/p1-wave-b-judge-a-dedup-f906` | 245-keep dedup pass |

All 302 lines parsed; every id assigned exactly one verdict.

## 2. Method — what this judge scored

Each idea was tiered on the cost of its **decisive** falsification (not its aspirational full study):

- **T1 — inference/analysis only** (frozen public models, cached predictions, synthetic stimuli, hours-to-a-day): the cheap-kill gold standard.
- **T2 — small training or light collection** (LoRA/probe/small-model runs, Blender rendering, small DIY annotation pilots): runnable on one GPU plus modest labor.
- **T3 — gated or expensive** (polarimetric/event-camera hardware, clinical experts, recruitment-scale human studies, pretraining-scale compute): kept only when the hypothesis justifies waiting for the gate.

Additional axes: is the falsification **actually runnable as stated** (public assets exist?), is the idea an **architecture-permutation** (recipe ported onto a new model with no belief at risk), and is it **too vague** (no crisp failure criterion). Duplicate/cluster structure was assessed independently of Judge A.

## 3. Verdict Counts

| Quantity | Value |
|---|---|
| Input total | 302 (A: 102, B: 96, C: 104) |
| **Keep** | **245** (A: 93, B: 84, C: 68) |
| Merge (with explicit targets) | 44 (A: 6, B: 11, C: 27) |
| Kill | 13 (A: 3, B: 1, C: 9) |
| Kept at T1 (inference/analysis only) | 97 |
| Kept at T2 | 142 |
| Kept at T3 (gated; do not schedule until gate confirmed) | 6 (B-060, B-071, B-072, B-083, B-085, B-094) |
| High-value anomalies protected | 20 |
| Duplicate groups | 28 |
| Co-run infrastructure clusters (not merges) | 9 |
| Recorded disagreements vs Judge A | 12 |

The same headline number as Judge A (245) is a coincidence of composition, not agreement: my A/B/C split is 93/84/68 vs A's 92/85/68, and the member lists differ (see §7).

## 4. Kills (13) — feasibility grounds

- **A-032** (MAE fingerprint): decisive test requires counterfactual pretraining of two promptable segmenters; the cheap precursor (phenotype overlap) cannot separate inheritance from convergence. No cheap kill exists.
- **A-085** (per-prompt early exit): "easy prompts saturate early" is near-certain; confirming it yields a router recipe, not a falsified belief. Permutation.
- **A-089** (easy-first adapter curriculum): noise-dominated effect; honest settlement needs seeds × orders × domains, expensive for a generic payoff. Permutation.
- **B-056** (spatially varying thresholds): mathematically guaranteed nonzero gap whose size is dictated by invented cost maps — a measurement, not a hypothesis at risk.
- **C-035, C-036, C-041, C-055, C-062** — known-critique restatements (multi-label re-evaluation, boundary metrics, FPR@TPR reporting, attention faithfulness, cross-threat non-transfer): all cheap to run, all largely already answered in the literature (unverified judge assessment); low information per unit work.
- **C-056, C-058** (equalized SSL-vs-supervised; curation complexity): both hit a pretraining-scale compute wall; the small-scale version cannot settle an explicitly scale-dependent claim, and the curation question is already actively measured by public competitions.
- **C-059** (visual emergence = metric artifact): direct port of a famous result; permutation.
- **C-104** (adaptive human-in-the-loop eval): near-tautological, evaluator-skill-confounded, no crisp failure criterion.

## 5. Cheap-kill honor roll (run these first)

97 kept ideas are T1. The ones I'd schedule in the first batch because they are decisive, cheap, and load-bearing for other ideas:

- **A-023** (IoU head is a style critic) — its outcome reprices A-025, A-086, A-091.
- **A-043** (constant boundary offset on synthetic exact boundaries) — cleanest kill in the wave; an afternoon.
- **A-015 / A-099** (public adapted checkpoints: multimask collapse; prompt-ignoring adapted SAMs) — inference on existing checkpoints, immediate.
- **A-076 + B-033** (threshold-vs-perception complementary pair) — oracle-threshold protocols, hours each.
- **B-049** (extent-level calibration gap), **B-020/B-022/B-074** (multi-rater analysis-only trio), **B-041/B-042/B-044/B-045** (smoke/fire shortcut counterfactuals).
- **C-057** (scale doesn't fix shifted calibration beyond accuracy) — public scale ladders, cached logits.
- **C-047, C-042, C-075, C-081, C-090** — laptop-scale analyses of protocol variance, reweighting, benchmark redundancy, ceiling artifacts, image-swap consistency.
- **B-088's hash audit** (merged into C-027) — cheapest, highest-yield first action of the entire leakage family; run before any retraining.

## 6. Duplicate groups and co-run clusters (independent of Judge A)

28 duplicate groups with primaries and reasons are in `judge_B.json → duplicate_groups`. Cross-shard collisions I found independently: A-071≡B-036 (bimodality), C-024⊃A-070 (seen-shot), C-027⊃{B-088, C-033, C-099} (leakage), C-066⊃{C-068, C-101} with B-095 as dense twin, C-018⊃{C-005, C-014, C-017} with B-050 as dense twin, C-013⊃B-051 (aleatoric identifiability), C-073⊃{C-007, C-078, B-038} (statistical audit), C-077⊃{C-031, C-049, C-050, C-051, C-053, C-098} (evaluation-stack nuisance).

Nine **co-run clusters** are flagged where distinct kept ideas share buildable infrastructure (click-sweep harness, synthetic smoke renderer, multi-rater ingestion stack, SAM2 memory probes, human-click corpus, cue-conflict stimuli, re-annotation pool, spatial-fingerprint tooling). These are scheduling hints, not merges.

## 7. Disagreements vs Judge A (my notes; Consolidator resolves, parent should not)

1. **A-032**: A kept; I kill — falsification is training-bound, precursor confounded.
2. **A-074** (universal adversarial prompt offsets): A killed as permutation; I keep-flagged — the staged per-image-bound-first kill design is exactly the discipline we want, and it's a one-day test. Low novelty priority.
3. **A-086** (IoU-score adapter routing): A killed; I keep-flagged — one-afternoon kill, in designed tension with A-023.
4. **A-059/A-061 merge direction reversed**: I keep A-059 (position-grid compositing is hours; viewpoint sweeps need rendering). Same one-study outcome either way.
5. **B-015/B-089 direction reversed**: I keep B-015 — displacement statistics are a falsifiable instrument; B-089's blind taxonomy clustering has no failure criterion.
6. **B-051 merge target**: C-013 (identifiability), not B-019 (map alignment) — B-051's sharp content is the capacity-manipulation test.
7. **B-056**: A kept; I kill (near-tautological).
8. **C-056, C-058**: A kept; I kill (pretraining-scale compute wall).
9. **C-079**: A killed/merged; I keep — the controlled dev-loop is the causal design in the adaptive-overfitting family and is cheap; triangulates with C-032.
10. **C-093**: A killed/merged; I keep — template re-rendering is a controlled counterfactual, a distinct design from blind baselines.
11. **C-078**: same direction as A (removed as standalone) but with an explicit target: fold power curves into C-073.
12. Overall shard-C consolidation largely agrees with A (template families collapse to umbrellas C-077/C-042/C-089/C-095/C-073/C-018); shard-B disagreements are mostly about which member of a pair is the cheaper/sharper primary.

## 8. Anomalies protected (20)

A-034 (window-lattice error fingerprint — also T1-cheap), A-044, A-063, A-065, A-079, A-087, B-016, B-029, B-030, B-054, B-067 (variance-decay deviation measures ambiguity structure — clever and cheap), B-069, B-071 (hardware-gated), B-083 (fast version runnable on public paired thermal footage), B-090, B-093, C-069, C-072 (kept with a data-access warning: unrunnable unless narrowed to datasets with documented annotation origins), C-074, C-075.

## 9. Caveats / handoff

1. **kill/merge ≠ bad idea.** These are feasibility dispositions; the Consolidator may resurrect anything, and merge targets say where the content folds.
2. **T3 keeps are conditional**: B-060 (polarimetric camera), B-071 (event camera), B-072/B-085 (clinical experts), B-083 (instrumented releases; fast version is T2), B-094 (protocol pilot required). Do not schedule until the gate is confirmed.
3. **prior_art_risk flags are unverified** and concentrated in shard C; a dedicated prior-art search pass must precede Stage-2 selection.
4. Per-id verdicts with tier, score (5=cheapest kill), runnability, and flags: `judge_B.json → verdicts`. Kept ideas with judge annotations: `accepted_shard_B.jsonl` (245 lines).
