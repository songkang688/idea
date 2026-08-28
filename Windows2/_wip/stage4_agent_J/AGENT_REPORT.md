# Windows2 Stage-4 Agent J — Report (Reviewer-2 attack on batch-A survivors)

Role: Reviewer #2 + freshness assassin for F's 20 PhD-year bets plus three PI-flagged shortlist members (0175, 0334, 0026). NOT the PI; no final-3 selection. Skipped already-KILLED 0017 and 0051. No F/G/H/I files modified.

Note: `Windows2/_wip/PI_TO_I.md` was listed as required reading but does not exist anywhere in the repo (verified after pulling latest origin); I proceeded on F's AGENT_REPORT/prior_work_attack/shortlist and Agent A's ideas.jsonl.

## What I did

1. Rebuilt each of the 23 targets from `stage1_agent_A/ideas.jsonl` and F's verdicts/mutations.
2. Ran ~15 batches of fresh live web/arXiv searches (2024–2026 focus) — every citation in my outputs was surfaced live this session or explicitly inherited from F's verified list. No invented papers or URLs.
3. Wrote the harshest defensible rejection per idea, enumerated hidden assumptions, and specified a killer experiment (or the mutation that makes one possible) → `reviewer2_attacks.md`.
4. Machine-readable verdicts → `verdicts.jsonl` (23 lines).

## Verdict totals (23 attacked)

**0 KILL / 13 MUTATE / 9 SURVIVE-IF-EXPERIMENT / 1 SURVIVE** — plus 3 of the SURVIVE-IF ideas are pilot-gated (0121, 0075, 0175: run a cheap pilot, kill on a pre-registered floor).

Zero hard kills is not softness: these 20 already survived F's 352→75→20 funnel and one adversarial pass. But **two ideas suffered framing kills** — their headline claims as written are dead to 2025–26 prior work and only mutations survive:

- **W2-A-0199** (context-completion hallucination): HalluSegBench (arXiv:2506.21546) is *the* counterfactual segmentation-hallucination benchmark; HII-DPO (arXiv:2602.10425) names scene-conditioned hallucination and demonstrates the co-occurrence-prior mechanism with counterfactual edits. F ranked 0199 #16 and never web-attacked it — the largest freshness casualty in the batch. Surviving sliver: the dose-response law (mined training co-occurrence → hallucination rate) on classical segmenters with known training data.
- **W2-A-0215** (protocol dominates architecture): Bauchwitz WACV 2025 (task configuration → trained-model performance), Nature MI 2023 (labelling instructions), and arXiv:2608.24486 (label effect ≈ 5x model effect) pre-empt the headline; also never web-attacked by F. Surviving sliver: a zero-annotation-budget version using COCO vs Sama-COCO dual labels of the same images.

## Freshness kills / material downgrades (papers F did not have)

| ID | Fresh hit | Effect |
|----|-----------|--------|
| 0199 | HalluSegBench arXiv:2506.21546; HII-DPO arXiv:2602.10425 | framing killed; Tier-A → mutation-only |
| 0215 | Bauchwitz WACV 2025; arXiv:2608.24486; Nat. MI 2023 | framing killed; commissioned corpus dead on cost-benefit |
| 0237 | 'Annotation Matters' doi:10.63317/3fss6oc5mono (NLP re-annotation recovers most of cross-corpus gap) | conceptual novelty spent; merge with 0249 |
| 0249 | arXiv:2608.24486 (label vs model effect) | phenomenon demonstrated; merge with 0237 |
| 0074 | COMPASS arXiv:2509.22240; CONSIGN arXiv:2505.14113 | conformal line answers the practical question; audit survives only with deployed-pipeline survey |
| 0331 | CC-DiceCE ISBI 2026 arXiv:2511.17146 (instance-loss gradient contrasts) | instrumentation niche closing; pursue first or drop |
| 0300 | Hidden Clones arXiv:2603.17111 (VLM ensembles, effective voters) | correlated errors now in vision; era→lineage redesign |
| 0334 | BareBones arXiv:2604.10528 (silhouette-only benchmark, 26 VLMs) | shape→category leg doubly occupied; privacy audit only |
| 0121 | VehicleSec 2026 'Seeing is Deceiving'; US patents 12481025/12099123 | phenomenon known on LiDAR side; camera audit survives, pilot-gated |
| 0071 | Cellpose-SAM doi:10.1101/2025.04.28.651001; CardioSAM arXiv:2604.03313 | conceptual correction: pairwise inter-rater Dice is NOT an upper bound; ceiling formalism must change |

Ideas where fresh searches found **nothing new** (window still open, F's assessment holds modulo my design attacks): 0206, 0163, 0150, 0151, 0075, 0145, 0061, 0352, 0326, 0175, 0026, 0100, 0349.

## The 8 most paper-shaped (cheapest path to a defensible paper, post-attack)

Ranked by (survives review) x (cost to decisive result). This is a shape ranking, not a significance ranking — the PI weighs upside separately.

1. **W2-A-0061** — topology at checkpoint-selection time. Only clean SURVIVE. Multi-seed checkpoint logging; either outcome publishes; no fresh competitor (the field keeps building topology losses, which is the point).
2. **W2-A-0100** — smoke/fire leakage audit. Method standard, finding unclaimed, two GPU-days + curation; honest venue is dataset/applications track.
3. **W2-A-0163** — stuff-stuff band atlas. Modest annotation budget; deliverable (per-pair band widths + band-aware re-scoring with CIs) is unambiguous; must beat the per-pair-tolerance Boundary IoU baseline.
4. **W2-A-0326** — context-value crossover law. Compute-bounded; locality-embodying architectures (Swin/HRNet/bilateral) provide free cross-validation of the predicted curve.
5. **W2-A-0151** — boundary error budget, IF the synthetic-GT estimator validation leads. Turns an identifiability complaint into a methods contribution.
6. **W2-A-0206** — SAM fingerprint + inheritance, IF the controlled-provenance corpus is built first. Highest upside of the eight; the dialect confound is the one honest wall.
7. **W2-A-0071** — noise-floor audit, AFTER switching to consensus-referenced ceilings. CardioSAM-style "surpasses inter-expert agreement" marketing gives it a live target.
8. **W2-A-0215 (mutated)** — COCO vs Sama-COCO protocol-effect study. GPU-week, zero annotation cost, pre-registered architecture-gain yardstick from 0322's mining.

Honorable mention: 0121 and 0175 are one cheap pilot away from either top-tier or dead — that optionality is valuable; run both pilots before committing anything else in C05/C07.

## Correlated failures (portfolio risks the PI should price)

1. **The re-annotation-arbiter cluster (0237, 0249, 0151, 0150, 0163, 0071).** All six use "more/better annotations" as referee and all six need a noise/convention/quality/genuine-ambiguity taxonomy that does not exist. They fail together if that taxonomy is unbuildable, and they duplicate infrastructure if built separately. Recommendation: 0237+0249 merge is mandatory (identifiability); 0151/0163/0150 should share one annotation protocol and multi-rater pool; the hidden foundational paper is the taxonomy itself.
2. **Rank-flip claims without a statistics layer (0163, 0100, 0071).** Each promises "rankings change"; none survives review without bootstrap/reproduction-noise CIs. F's statistics keeps (0313/0322) are prerequisites, not siblings.
3. **Freshness-fragile set (0199, 0215, 0331, 0300, 0074).** Multiple 2025–26 publications per quarter in each niche. Two already lost their framing this round (0199, 0215). Any of these pursued must be re-searched at proposal AND experiment-freeze; 0331 in particular should be first-in or dropped.
4. **Curation-based causal designs lose to editing-based ones.** HalluSegBench/HII-DPO took 0199's ground with controlled counterfactual editing while batch A proposed curating rare real scenes. Any batch-A design using curation as the causal control should add or switch to an editing/synthesis arm.
5. **Pilot-gated bets share a null-risk profile (0121, 0075, 0175).** All three are one pre-registered pilot from resolution; running the pilots is cheap and strictly information-positive, but they should not be counted as three independent "Tier A" slots until the pilots return.
6. **Data-access-conditional pair (0075, 0145).** F flagged both; my attack tightened them differently — 0145's collar design is replaced by temporal-adjacency verification (removes the ecology-partner wall), while 0075 still depends on region-level outcome linkage (LIDC pilot decides).

## Bias audit (self)

- I attacked hardest where fresh literature was densest (hallucination, conformal, instance losses, ensembles); my SURVIVE-IF verdicts in metrology/psychophysics territory (0150, 0175, 0349-mutation) rest on absence-of-evidence across fewer searches — the same asymmetric error bars F disclosed.
- I favored "the experiment is the paper" verdicts (9 SURVIVE-IF) over binary SURVIVE/KILL; a PI who wants fewer, harder commitments should read SURVIVE-IF as "conditionally alive, commit to publishing the null."
- Zero KILLs on a mandate to kill: my honest reading is that F's top-20 filter already removed the killable; where I found scooping (0199, 0215) a defensible mutation existed. If the PI wants a forced kill list, the weakest three post-attack are 0199, 0215, 0334 (all reduced to slivers of their original ambition).

## Files written (all under `Windows2/_wip/stage4_agent_J/`)

- `reviewer2_attacks.md` — 23 full attacks: harshest rejection, hidden assumptions, killer experiment, verdict; cross-cutting notes.
- `verdicts.jsonl` — 23 lines: id, F-verdict, J-verdict, freshness flags + citations, one-line rejection, one-line killer experiment, notes.
- `AGENT_REPORT.md` — this file.
