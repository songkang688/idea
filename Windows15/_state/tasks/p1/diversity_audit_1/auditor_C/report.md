# P1 Diversity Audit 1 — Auditor C: Contrarian-Hypothesis / Research-Blind-Spot Audit

- **task_id:** `p1_diversity_audit_1_C`
- **Window:** Windows15 (LOCKED — `window.lock.json` and `ideas_master.jsonl` read-only, untouched; this task writes only under `tasks/p1/diversity_audit_1/auditor_C/`)
- **Corpus audited:** `Windows15/_state/ideas_master.jsonl` (271 accepted ideas, batch 001) joined with the raw generator shards `tasks/p1/batch_001/gen_{A,B,C}/ideas.jsonl` (300 generated, 271 surviving) — the shards carry the full per-idea schema including `community_default_belief` / `why_that_may_be_wrong`, which the slim master rows do not.
- **Provenance:** fetched from `origin/cursor/p1-wave-b-batch001-consolidator-7c96` @ `b8d60bce42ab0a9f0f7b35278454d65d59f01331`; `ideas_master.jsonl` sha256 `150201919e85bd41172bb88d4e24c406361ae27fc34a0a93465f5013854c737d`.
- **Sibling audits consulted (not copied):** auditor_A (mode collapse) @ `fc9c24f`, auditor_B (permutation pseudo-innovation) @ `829c476`. Agreements and one disagreement are stated in §6.
- **Evidence policy compliance:** no literature was consulted or cited; every "the field believes / this is mainstream" statement below is this auditor's judgment and is labeled MODEL SPECULATION. All counts are computed directly from the corpus files; regex patterns and per-idea ID lists are in `findings.json` for reproduction.

## Verdict (one paragraph)

The corpus is **rhetorically contrarian everywhere and substantively counter-intuitive in only one direction.** The generation schema made `community_default_belief` and `why_that_may_be_wrong` mandatory (300/300 generated ideas filled both), so every idea is structurally framed as opposition to a default belief — zero ideas affirm, confirm, or delimit a community position. Within that forced frame, genuine directional surprises do exist (~44 ideas, 16.2%, predict an effect opposite to practitioner expectation, several excellent), but the contrarian energy flows almost entirely in the "field is too optimistic" direction: deflationary/debunk claims tag 39.1% of the corpus while "field is too **pessimistic**" claims are ~2% (roughly 4–6 ideas), null-result/equivalence claims are 2.6%, confirmatory boundary-of-validity science is 0, and meta-critique of the corpus's own critical instruments is 0 — even though ~40% of the corpus (per auditor_A's F1+F2+F3 count, independently consistent with my sweep) rests on those instruments being sound. Several of the best contrarian bets are unsupported singletons (foundation-model tax, anti-curriculum, automation-degrades-review, under-prompting narrative flip). The belief fields being debunked are diverse in topic but weak in provenance: only 5/271 carry any evidence label, ~10% contain absolutist intensifiers ("only path", "any population", "unconditionally") that inflate debunkability, and a 30-idea random sample classifies most as practice-defaults or folk attributions rather than documented positions — i.e., a real risk of **safe contrarianism against soft targets**. Recommended fixes for T07–T16: stance quotas (cap debunk at ~25%, floor anti-pessimism, null-result, quantitative-law, and constructive shares), a claim-direction enum replacing the mandatory belief/rebuttal pair for part of each batch, and territory charters that force the missing directions (§5). This is advisory only — the diversity-audit consolidator owns the canonical queue.

## 1. Method

1. Joined all 271 master rows to their raw shard records by `idea_id` (271/271 matched; master carries `title`/`core_hypothesis` only, shards carry the 13-field schema).
2. **Stance taxonomy sweep** (regex, non-exclusive, over `one_line` + `core_hypothesis`): deflationary (signal-is-artifact), anti-pessimism (capability-better-than-believed), directional surprise (effect opposite to expectation), null claim (no difference where one is assumed), quantitative law, constructive (new exploitable signal). Patterns in `findings.json`.
3. **Manual verification** of every idea in the small categories (anti-pessimism, null, meta-critique, confirmatory, scaling, tiny-specialist candidates) by reading the full records — the counts for those categories below are read-verified, not just regex hits.
4. **Belief-field forensics**: evidence-label frequency, hedge/folk-attribution markers, practice-description markers, absolutist intensifiers, plus manual classification of a fixed-seed random sample of 30 `community_default_belief` fields.
5. **Absence checks**: 18 targeted sweeps for hypothesis directions I expected a balanced contrarian corpus to contain; each claimed absence below was verified by reading all regex candidates (false positives discarded).

## 2. Q1 — Does the corpus lack counter-intuitive hypotheses?

**Answer: not wholesale — it lacks specific *directions* of counter-intuitiveness.**

Stance distribution (non-exclusive tags; n=271; ID lists in `findings.json`):

| Stance | Count | Share | Read-verified? |
|---|---|---|---|
| Deflationary (trusted signal is artifact/shortcut/confound) | 106 | 39.1% | sampled |
| Directional surprise (effect opposite to expectation) | 44 | 16.2% | all read |
| Quantitative law (functional form / threshold / scaling claim) | 22 | 8.1% | all read |
| Constructive (new exploitable signal/capability) | 17 | 6.3% | sampled |
| Null / equivalence (no difference where one is assumed) | 7 | 2.6% | all read |
| **Anti-pessimism (capability better than the field believes)** | **6 regex → ~4 genuine** | **~1.5%** | all read |
| Untagged (diagnostic/measurement, no strong stance) | 109 | 40.2% | sampled |

### 2.1 What exists and is good — protect at the Stage-2 cut

The directional-surprise band contains genuinely counter-intuitive, decision-relevant bets. Fifteen strongest (this auditor's judgment; full list in `findings.json`):

| idea_id | Counter-intuitive core |
|---|---|
| A-057 | Anti-curriculum wins: training on SAM's *worst* zero-shot images first accelerates adaptation |
| A-077 | Foundation-model tax: small from-scratch specialist beats LoRA-SAM at matched *total* cost |
| B-065 | Near-perfect automation degrades human review so much that intermediate-accuracy models yield better final contours |
| B-093 | Direct image-to-measurement regression beats segment-then-measure — segmentation may not be the right intermediate |
| C-091 | Clutter *helps* glass segmentation, inverting the universal clutter-hurts assumption |
| A-028 | PEFT forgetting is displacement, not erasure — 50 rehearsal images restore most zero-shot loss |
| C-093 | Aggressive boundary-label jitter barely hurts smoke models — annotation-precision budgets spent on a fiction |
| B-038 | Super-resolution preprocessing is *worse* for safety than honest low-resolution uncertainty |
| A-031 | LoRA-is-gentler has a crossover: under high-rank shift LoRA both underfits AND forgets more |
| B-060 | Consistent bias beats inconsistent accuracy for treatment-response assessment |
| A-070 | "SAM fails on X" papers under-prompt; oracle-prompt re-evaluation overturns failure narratives |
| A-078 | Souping same-task LoRAs beats doubling rank — PEFT is variance-limited, not capacity-limited |
| C-082 | Amodal completion helps glass but *harms* smoke — object permanence is not universally good |
| B-025 | Medical models are texture-first, shape-last, inverting the anatomy-prior story |
| A-004 | One negative click in clutter often hurts more than a positive click helps |

### 2.2 What is missing — the one-sidedness

- **Zero affirmative hypotheses.** No idea's core hypothesis confirms, strengthens, or maps the domain of validity of a community belief (regex + read check: 0/271). A calibrated portfolio should contain "belief X is right, and here is precisely where it stops holding" bets — they are as falsifiable as debunks and currently absent.
- **Anti-pessimism ≈ 1.5%.** Read-verified genuine members: A-070 (under-prompting), A-007 (category-blind tokens secretly carry decodable semantics — latent capability), C-019 / C-079 (physics recovers more than assumed from single images/video). Against ~106 deflationary ideas, the corpus bets ~25:1 that the field is fooled by optimism rather than by pessimism. Nothing enforces that asymmetry except the schema (§3).
- **Null results ≈ 2.6%.** Seven ideas (e.g., C-027 smoke/haze indistinguishability, C-093 jitter-insensitivity). No "methods A and B are statistically indistinguishable once tuned" hypotheses aimed at the corpus's own crowded clusters.
- **Zero meta-critique.** 40% of the corpus (evaluation-critique + shortcut-reliance + annotation-provenance families) relies on counterfactual manipulations, probes, and disagreement analyses as instruments. Not one idea hypothesizes that those instruments themselves produce artifacts (both regex candidates A-007, A-090 are false positives — they critique SAM, not the critique toolchain). A genuinely contrarian corpus would aim at least one gun at itself.
- **Singleton fragility.** The boldest contrarian bets are 1-idea families with no competing formulation and no fallback if the single formulation is flawed: A-077, A-057, B-065, B-093, A-070, C-090 (untrained humans beat SOTA at incipient smoke detection), A-007. Compare: "models use shortcuts" gets ~36 formulations. The portfolio over-diversifies its safest claim family and under-diversifies its boldest ones.

## 3. Q2 — Did the `community_default_belief` schema force a uniform debunk stance?

**Answer: yes — structurally, measurably, and in one direction only.**

1. **Mandatory opposition.** All 300 generated ideas (100% per shard) fill both `community_default_belief` and `why_that_may_be_wrong`. The schema literally requires every idea to state a belief and argue why it is wrong; there is no schema slot for "and this belief is right / partially right / holds only under conditions". Zero corpus ideas affirm a default belief — perfect compliance with the forced frame.
2. **Topic-diverse, stance-uniform.** The belief fields are lexically diverse (my 6-theme sweep captures only 11.1% of them — no single strawman is recycled en masse; consistent with auditor_A's finding that collapse is at the meta-template level, not topic level). What is uniform is the *relation* to the belief: oppose. The schema constrained the direction, not the subject.
3. **Weak belief provenance.** Only 5/271 belief fields carry any evidence label (4 VERIFIED PRIOR WORK, 1 KNOWN FACT); 266 are unlabeled assertions about what "the community" believes. 13/271 explicitly hedge the belief as folklore/implicit/unstated; 27/271 (10.0%) contain absolutist intensifiers ("the only path", "any population", "unconditionally", "harmless", "nobody would...") that make the belief easier to refute than any position a careful practitioner actually holds.
4. **Random-sample classification** (seed 15, n=30, per-idea judgments in `findings.json`; MODEL SPECULATION — this is one auditor's reading): ~40% plausible argued positions a named sub-community would defend (e.g., A-019 rank-capacity folklore, B-018 Surface-Dice stance, A-057 curriculum-helps, C-052 flicker-signature); ~40% *practice defaults* — descriptions of what pipelines do, recast as beliefs (e.g., B-016, A-074, C-098, A-009); ~20% constructed/overstated attributions whose absolutist form no one would defend (e.g., C-095 "the only path", B-057 "any population", A-031 "unconditionally", C-096 "harmless and helpful"). Debunking a practice-default is often legitimate science; debunking an intensifier-inflated attribution is rhetorical free profit — the schema does not distinguish these, and nothing in the pipeline scores belief provenance.
5. **The forced frame explains the direction asymmetry.** "State a belief, then say why it may be wrong" naturally produces "field is fooled" (deflationary) hypotheses; producing an anti-pessimism idea inside this schema requires the awkward inversion of debunking a *negative* belief (exactly what the rare A-070 does — its stated belief is "SAM fails on X"). The observed 25:1 deflation-to-rehabilitation ratio, uniform across all three generators (auditor_A independently measured 24–28% deflationary title rates per shard), is what this schema predicts. It is a pipeline property, not a generator quirk.

**Consequence, not catastrophe:** the falsifiable cores remain testable regardless of stance framing, and judges screened compliance well (auditor_B's tier-1 is only 2.2%). The damage is portfolio-level: an entire missing hemisphere of hypothesis space (§4) plus a systematic risk that "novelty vs. the default belief" was measured against manufactured defaults.

## 4. Q3 — Missing scientific questions

Each item below was verified absent or near-absent by targeted sweep + reading of all candidates (patterns and candidate dispositions in `findings.json`). "Missing" means: no accepted idea has this as its headline falsifiable claim.

1. **Capability rehabilitation at scale.** Which reported foundation-model failures (medical, camouflage, transparency, smoke) are evaluation artifacts — under-prompting, wrong operating thresholds, mask-selection protocol? One idea exists (A-070, T01-only). The symmetric question for T02/T03 evaluation stacks is unasked.
2. **Latent-capability probing.** What does the frozen model *know* that its output interface cannot express (linear decodability of classes, depth, materials, boundaries from internal states)? A-007 is the lone instance.
3. **Model-scale behavior.** Zero ideas use backbone scale (ViT-B/L/H, distilled variants) as the experimental variable: no emergence claims, no inverse-scaling claims, no "which corpus finding flips with scale" checks. Every claimed artifact/shortcut in the corpus is implicitly assumed scale-invariant.
4. **Test-time compute.** Zero ideas on inference-time scaling: does sampling/ensembling/iterative refinement at test time buy segmentation quality the way it buys LLM quality? (Adjacent but distinct from A-005's limit-cycle critique.)
5. **Confirmatory / boundary-of-validity science.** Zero ideas map where a community belief *holds* (e.g., "rank-matching folklore A-019 is correct within [regime], quantifiably"). The corpus can say "belief X is wrong" 106 ways but cannot calibrate any belief's domain of validity.
6. **Meta-critique of the critique toolchain.** Zero ideas test whether counterfactual-manipulation probes, shortcut-reliance measurements, or disagreement decompositions are themselves confounded — the load-bearing instruments of ~40% of the corpus are unexamined.
7. **Joint-implication ("grand synthesis") tests.** 109 critique ideas, no hypothesis about their *combined* effect: e.g., "protocol + shortcut + label artifacts jointly account for >X% of published SOTA deltas on benchmark Y" — the single most decision-relevant contrarian claim the family could make.
8. **Positive human–AI complementarity.** Zero ideas hypothesize conditions where human+model exceeds both alone; the human-factors slice (B-065, B-081) is exclusively "automation harms humans".
9. **Cross-task transfer/interference.** Segmentation ↔ detection/depth/counting transfer has ~2 passing mentions, no headline claim (relevant given T04/T05 are queued: batch_002 will inherit this hole unless charged with it).
10. **Memorization / regurgitation / privacy.** No headline claim on whether SAM regurgitates SA-1B masks, whether adapters leak patient anatomy, or contamination forensics (6 regex hits all use "memorize" as mechanism vocabulary, e.g., A-053's rank-noise filter).
11. **Data lineage feedback loops.** SA-1B is itself model-in-the-loop annotated, and B-069 covers iterated self-training collapse — but "model-generated labels polluting the *next* generation of training corpora" as an ecosystem-level measurable is unclaimed.
12. **Decision-theoretic value of accuracy.** Which metric improvements are economically/clinically worthless because they sit below decision thresholds? Five loose matches (A-049, A-077, B-062, B-070...), none carrying it as the core claim outside A-077's cost framing.

## 5. Recommended territory mix for T07–T16 (advisory — consolidator writes the canonical queue)

Assumes batch_002 (T04 object detection, T05 VLM/dense prediction, T06 failure mining) proceeds as already queued. Design goals: fill verified holes (§4), rebalance stance directions (§2–3), don't re-till saturated ground (HC-23/36/02/30 per auditor_A; LoRA-mechanics orbit per auditor_B).

| Territory | Charter | Primary stance quota | Fills |
|---|---|---|---|
| **T07 Capability rehabilitation & oracle evaluation** | Re-test reported FM failures under oracle prompting/protocols across T01–T03 domains; latent-capability probing of frozen models | ≥50% anti-pessimism | §4.1, §4.2 |
| **T08 Scaling behavior & test-time compute** | Backbone-scale as variable (emergence/inverse-scaling of corpus-claimed artifacts), data-scaling laws, inference-time compute scaling | ≥50% quantitative-law | §4.3, §4.4 |
| **T09 Video, temporal & streaming segmentation** | SAM-2-family memory mechanics, longitudinal medical change, temporal claims outside T03 | balanced; ≤25% deflationary | biggest coverage hole (concurs with A §6.10, B §6.2) |
| **T10 Constructive signal harvesting** | Turn corpus diagnostics into mechanisms: uncertainty/disagreement/consistency as supervision, free sensors made into working systems (grow HC-37/38 from near-singletons) | ≥60% constructive | §2.2 constructive deficit |
| **T11 Interactive segmentation & human factors** | Correction dynamics, annotation ergonomics, automation bias AND complementarity conditions | ≥30% anti-pessimism/complementarity | §4.8; HC-34 starvation |
| **T12 Boundary-conditions & adversarial collaboration** | Map domains of validity of the top ~15 beliefs the corpus attacks; replicate the corpus's own biggest claims; meta-critique of probe instruments | 100% confirmatory/null/meta | §4.5–§4.7 |
| **T13 3D, geometry & non-photographic domains** | Volumetric beyond medical, remote sensing, industrial inspection, documents, microscopy | balanced | territory ceiling (concurs with A §6.12) |
| **T14 Open-world formulation science** | Instance/panoptic/amodal/part-whole ontology outside media; what "an object" is to a segmenter | balanced | §2.2; B §6.9 |
| **T15 Theory & formal limits** | Identifiability, information-theoretic impossibility, sample complexity; formalize C-027/C-010-style results for T01/T02 | ≥40% quantitative-law/null | B §6.7; thin formal slice |
| **T16 Security, lineage & memorization** | Adversarial/spoofing (currently 1 idea), regurgitation/privacy, model-generated-label feedback, contamination forensics | balanced | §4.10, §4.11 |

**Cross-cutting generation-contract changes (any territory):**

- Stance quotas per 100-idea shard: **≤25 deflationary**, **≥20 constructive**, **≥10 anti-pessimism**, **≥10 quantitative-law**, **≥5 null/equivalence**, and **≥3 ideas whose falsification would *vindicate* a community default** (affirmative bets).
- Replace the mandatory `community_default_belief`/`why_that_may_be_wrong` pair with a **`claim_direction` enum** (`debunk | rehabilitate | affirm_with_boundary | new_capability | quantitative_law | null_result`) plus an *optional* belief field; when the belief field is used, require a **provenance tag** (`documented_position | practice_default | folk_attribution`) and forbid absolutist intensifiers unless quoted.
- Require a **`who_would_disagree`** field: name the sub-community that would bet against the hypothesis. If no one would bet against it, it is not contrarian — it is consensus wearing a contrarian costume.
- Singleton-protection: instruct Stage-2 judges that portfolio value of the singleton contrarian bets (A-077, A-057, B-065, B-093, A-070, C-090, A-007) is not measured by cluster size; consider commissioning 2–3 competing formulations of each rather than letting them face the cut alone.

## 6. Relation to auditors A and B (independent cross-check)

- **Concur with A:** deflationary meta-family dominance (my 39.1% deflationary tag vs. A's 40.2% F1+F2+F3 mass — independently derived, consistent); schema-induced house style; uniformity across shards; temporal/video and territory-ceiling blind spots.
- **Concur with B:** permutation pseudo-innovation is not the main risk; underweighted axes (theory, security, continual) confirmed by my sweeps.
- **Nuance vs. A (mild disagreement):** A's title-level count (~1% constructive) understates constructive content — full-text tagging finds 6.3%, and the directional-surprise band (16.2%) means the corpus is *not* short of counter-intuitive instance-level claims. The scarcity is directional (anti-pessimism, null, affirmative, meta-critique), not generic "lack of counter-intuitive hypotheses". Rebalancing should target claim *direction*, not just add "constructive" volume.
- **Addition neither A nor B measured:** belief-field provenance forensics (§3.3–3.4) — the debunk stance is aimed at defaults that are largely undocumented or intensifier-inflated, which is a novelty-inflation risk at Stage 2 in addition to a diversity problem.

## Caveats

- All stance/absence counts are regex-plus-reading heuristics by one auditor; small categories were read exhaustively, large ones sampled. Patterns and ID lists in `findings.json` allow full re-derivation.
- The sample classification in §3.4 and the "safe contrarianism" assessment are MODEL SPECULATION (no literature checked, per window evidence policy); the consolidator should treat them as one vote.
- No idea is accused of being non-novel; nothing here verified prior art. Recommendations concern portfolio balance only.
- The T07–T16 table is a recommendation. This task did **not** write or modify any task queue, canonical state file, or the window lock.
