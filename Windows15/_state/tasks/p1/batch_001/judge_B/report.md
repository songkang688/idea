# P1 Wave B — batch_001 — Judge B report (architecture-permutation killer / feasibility judge)

- **task_id:** `p1_wave_b_batch001_judge_B`
- **windows_path (LOCKED):** `Windows15`
- **judge role:** independent permutation-kill + falsifiability + feasibility triage. No dedup decisions, no novelty verification, no ledger edits.

## Inputs

| shard | branch | head SHA | territory | ideas |
|---|---|---|---|---|
| gen_A | `origin/cursor/p1-wave-a-gen-a-f6f6` | `5b770eb05040d0168d2ee35fba69ca060a085964` | T01 SAM / foundation-model adaptation / PEFT | 100 (`W15-B001-A-001..100`) |
| gen_B | `origin/cursor/p1-wave-a-batch001-gen-b-9ddf` | `588902125444c35c9b4599e2a649d8ff96640bbf` | T02 Medical segmentation | 100 (`W15-B001-B-001..100`) |
| gen_C | `origin/cursor/p1-wave-a-batch001-gen-c-65da` | `046bd2ceb9e806802d4fc37e8806687eed0fda86` | T03 Smoke / fire / ambiguous segmentation | 100 (`W15-B001-C-001..100`) |

All 300 ideas were read in full (one_line, core_hypothesis, falsifiable_prediction, minimal_falsification_experiment, fastest_falsification, plus surrounding fields).

## Rubric

**Permutation archetypes flagged (`permutation_flag: true`):**
1. Module A+B assemblies whose deliverable is a system built from existing parts (routers, fusion pipelines, frozen-model ensembles-as-detectors).
2. Attention/loss/backbone/objective swaps and training-recipe permutations (curricula, augmentation swaps, loss schedules, gradient surgery, soups, pretraining-objective swaps).
3. SAM+X / LoRA+X applications of known methods (coreset active learning, rehearsal, test-time adaptation, post-hoc recalibration, input adapters, compression tricks, annotation workflows).

The flag records archetype pattern-match. A flagged idea is still **kept** when a genuine, falsifiable scientific hypothesis is the load-bearing content and the permutation is only the measurement vehicle; it is **mutated** when the archetype dominates and the hypothesis needs rewriting to survive; it would be **dropped** if no salvageable hypothesis existed.

**Falsifiability:** judged on whether the stated design has an explicit kill condition (an observable outcome under which the authors must abandon the claim).

**Feasibility of `minimal_falsification_experiment`:**
- `cheap` — evaluation/analysis-scale on public or synthetic assets, no or trivial training.
- `medium` — training runs, modest controlled captures (fog rig, tabletop, tripod), small non-expert annotation efforts.
- `expensive` — expert-annotation campaigns, clinician user studies, pretraining-scale compute, specialized instrumentation, hard-to-access clinical archives.
- `infeasible` — cannot realistically be run.

## Verdict summary

| shard | keep | mutate | drop | permutation-flagged | cheap | medium | expensive | infeasible |
|---|---|---|---|---|---|---|---|---|
| gen_A (T01) | 95 | 5 | 0 | 23 | 42 | 57 | 1 | 0 |
| gen_B (T02) | 100 | 0 | 0 | 7 | 21 | 69 | 10 | 0 |
| gen_C (T03) | 99 | 1 | 0 | 10 | 33 | 65 | 2 | 0 |
| **total** | **294** | **6** | **0** | **40** | **96** | **191** | **13** | **0** |

**Why zero drops:** all three generators visibly operated under a contract that pre-excluded bare permutations — every idea ships a stated hypothesis, a falsifiable prediction, and a fast kill condition. Applying the drop criterion honestly (permutation archetype **and** no salvageable hypothesis, or unfalsifiable), no idea qualified. The kill function of this pass is expressed in the 6 mutations (archetype-dominant ideas requiring hypothesis rewrites) and the 40 archetype flags handed to the consolidator, not in artificial drops.

**Falsifiability:** 300/300 judged falsifiable as stated. No unfalsifiable ideas found; the closest to interpretive risk are confound-heavy regressions (A-087, C-042), noted but killable as designed.

## Mutations (6) — rewrite directions

| idea_id | archetype | rewrite direction |
|---|---|---|
| W15-B001-A-052 | coreset/k-center AL applied to SAM-LoRA | Recast as: a labeled image's adaptation value is predicted by its coverage of the domain's feature-shift directions, measurable pre-training from frozen-feature discrepancy spectra (ties to A-021). Kill the "selection method beats random" framing. |
| W15-B001-A-056 | SAM-proposes/human-verifies annotation workflow | Isolate the falsifiable core: residual SAM mask errors are per-domain incoherent and hence un-memorizable by low-rank updates; make measured error-coherence the predictor of when cheap verification supervision matches dense labels (complements A-053). |
| W15-B001-A-060 | query-by-committee AL with SAM's multimask as committee | Drop the AL race. Test the informational claim: multimask disagreement specifically localizes convention/granularity uncertainty while low confidence mixes noise, difficulty and out-of-scope junk. Fold the measurement into the A-061/A-089 family. |
| W15-B001-A-084 | SAM + self-consistency test-time adaptation (established TTA family) | Promote the diagnostic claim: cross-prompt/augmentation inconsistency is spatially enriched at true error locations under shift (measure error-localization AUROC). Demote per-image adaptation to a secondary intervention arm. |
| W15-B001-A-100 | nearest-centroid routing over frozen features (assumed-true premise, engineering assembly) | Rewrite around the only non-obvious content: the routing failure boundary on near-duplicate domains (e.g. two CT sites) and whether centroid distance is a *calibrated* novel-domain detector. |
| W15-B001-C-028 | motion-sparsity router dispatching to existing specialist models (Module A+B) | Center the two-sided physical signature: volumetric media produce dense, temporally decorrelating change; refractive solids produce sparse, edge-locked, geometrically consistent change. Validate bimodality and cross-domain stability of the statistic first; the router is at most a downstream application. |

## Permutation-flagged but kept (34)

- **gen_A (18):** A-008 (PEFT-method comparison; redeemed by gap-typing hypothesis), A-015 (placement recipe; first-layer-statistics localization), A-016 (LN-only comparison; multiplicative channel-statistics mechanism), A-019 (LoRA+regularizer; rank-vs-regularization attribution), A-028 (rehearsal; displacement-vs-erasure), A-032 (head recalibration; readout-mismatch dissociation), A-057 (curriculum; gradient-starvation mechanism, inverted prediction), A-063 (technique comparison; matched-FLOPs framing), A-064 (recalibration-only adaptation; pipeline-value decomposition), A-078 (soups; variance-vs-capacity attribution), A-079 (binarization; directional-content claim), A-081 (input adapter; gap-through-the-lens decomposition), A-082 (channel gating; destructive-interference hypothesis), A-083 (PE-only tuning; scale-vs-content dissociation), A-092 (LoRA+speckle augmentation; anatomy-free transfer prediction), A-093 (tone-curve adapter; 1-D gap claim), A-096 (consistency adaptation; label-free-beats-few-shot claim), A-098 (stitching+LoRA; linear-portability hypothesis).
- **gen_B (7):** B-007 (supervision-recipe comparison; calibration-for-free prediction), B-063 (click-policy training; predictability claim measured first), B-093 (task-swap comparison; intermediate-error hypothesis), B-095 (loss schedule; probability-saturation mechanism), B-096 (augmentation replacement; label-noise reattribution), B-097 (curriculum; boundary-policy transfer), B-098 (gradient surgery; directional-conflict diagnostic).
- **gen_C (9):** C-008 (added branch; oracle residual test), C-031 (frozen-model-ensemble detector; inconsistency-signature claim), C-054 (pre-filter module; computable crossover law), C-057 (fusion differencing; LWIR-opacity physics), C-061 (audio-visual X+Y; localization sharpness as the measured quantity), C-062 (flash/no-flash; calibrated densitometry), C-077 (decomposition training; synthetic-transfers-better hypothesis), C-078 (factored architecture; spectra measurement precedes build), C-087 (pretraining swap; inductive-bias attribution via binarized-label control).

## Feasibility notes

- **Expensive (13):** A-091 (pretraining-scale subset runs); B-002, B-051, B-091 (expert re-annotation / rare-cohort or archive curation); B-061, B-062, B-063, B-065, B-066, B-067, B-081 (clinician / reader / editing studies); C-059 (aerosol chamber + filter-wheel instrumentation); C-097 (multi-fuel burns under safety supervision). All have stated cheap fast-kills that should run before committing the full experiment.
- **Availability-risk mediums (flagged in notes):** B-008 (annotation timestamps), B-011 (pre-QC archives), B-029 (kernel-paired volumes), B-043 (pediatric labels), B-077 (adjudicated label corrections), C-039 (soft-labeled smoke data).
- **Shared-infrastructure batching:** gen C's fog-rig captures (C-005/011/015/019/047/081/095 plus others) should be one capture campaign if advanced — consistent with gen C's own done.json note.
- **No infeasible ideas found.**

## Cross-shard observations for the consolidator (not adjudicated here)

- **Near-duplicate families across shards:** jitter/perturbation-instability (A-009, A-066, C-030, C-034); interactive non-convergence (A-005, C-036); model-disagreement-reproduces-rater-disagreement (A-061, B-059, C-083); annotation-style/tool signatures (A-036, C-013); disagreement-driven label auditing (A-067, B-077); metric-confound audits (A-069, B-013); statistical-power audits (A-072, B-014, B-020); resolution/thin-structure limits (A-035, C-010/C-040 — related but distinct claims).
- **Gen A's own T02-collision flags** (A-045, A-056, A-058, A-061, A-092..096) stand; dedup task should adjudicate.
- **Valuable internal contradiction to preserve, not dedup away:** A-017 (conventions require encoder changes) vs A-045/A-046 (conventions are decoder-side readout policies). Binding these into one adjudicating experiment is higher value than either alone.
- **Premise dependency:** A-090's causal story depends on the SA-1B privacy-blurring detail that gen A tagged as unverified; the behavioral test stands regardless, but interpretation needs the provenance check.

## Caveats

- No literature/novelty verification was performed; archetype comparisons in notes ("query-by-committee", "PCGrad-style", "flash/no-flash photography") are references to well-known method families used for pattern-matching, not verified-novelty judgments about the ideas.
- Falsifiability and feasibility were judged on the designs as written; feasibility grades assume a typical academic lab with GPU access and, for T02, clinical collaborators.
- Decisions here are independent recommendations for the batch_001 consolidator; they do not modify the lock, canonical ledgers, or any gen-shard file.
