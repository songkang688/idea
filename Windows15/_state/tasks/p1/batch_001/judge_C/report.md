# P1 Wave B — Judge C Report (adversarial duplicate / collision audit), batch_001, Windows15

- Task: `p1_wave_b_batch001_judge_C`
- Role: adversarial duplicate / intra-batch collision auditor (independent of judges A and B)
- Inputs audited (300 ideas total):
  - `origin/cursor/p1-wave-a-gen-a-f6f6` → gen_A shard, T01 SAM/PEFT, `W15-B001-A-001..100`
  - `origin/cursor/p1-wave-a-batch001-gen-b-9ddf` → gen_B shard, T02 medical, `W15-B001-B-001..100`
  - `origin/cursor/p1-wave-a-batch001-gen-c-65da` → gen_C shard, T03 smoke/transparent media, `W15-B001-C-001..100`
- Outputs: this report, `duplicates.json` (structured mapping), `verdict.jsonl` (300 per-idea verdicts), `done.json`
- Locked window respected: no lock or canonical state file touched; writes confined to `Windows15/_state/tasks/p1/batch_001/judge_C/`.
- No novelty verification performed (out of scope by contract). No citations, benchmarks, datasets, or results invented anywhere in this audit.

## Method and dedup standard

All 300 records were read at one-line level; ~55 collision candidates were then read at full-record level
(core_hypothesis, falsifiable_prediction, fastest_falsification) before any verdict was issued. The hard-duplicate
bar applied: **two ideas are duplicates when they assert the same core scientific claim, such that decisively
testing one substantially tests the other**. A re-instantiation in another territory counts as distinct only if the
domain changes the mechanism or the prediction — not merely the dataset. Entailment, nested claims, and competing
mechanisms over one observable are *not* duplicates; they are flagged as families or protected pairs.

Verdict vocabulary: `keep` (284) and `duplicate_of` (16, each with a canonical target and a salvage note for the
merge). `drop` was reserved for records with no distinct falsifiable claim at all; **no record qualified** — all
three generators cleared that bar.

## Verdict summary

| | gen_A | gen_B | gen_C | total |
|---|---|---|---|---|
| keep | 95 | 95 | 94 | **284** |
| duplicate_of | 5 | 5 | 6 | **16** |
| drop | 0 | 0 | 0 | **0** |

Hard duplicates: 12 intra-shard, 4 cross-territory. 39 near-duplicate families flagged (members kept, with
merge-order guidance). 10 competing pairs and 12 singular anomalies explicitly protected from over-dedup.

## 1. Cross-territory collisions (the attack the task ordered)

### T01 vs T02/T03 foundation-model defects — one confirmed 3-way collision

**The edge-snapping prior appears in all three shards as three ideas: `A-034`, `B-083`, `C-029`.** All three
assert that (pretrained/promptable) segmenters place boundaries at the strongest local image gradient rather than
the true boundary. Verdict: `B-083 → duplicate_of A-034`, `C-029 → duplicate_of A-034`. A-034 holds the strongest
formulation (a predictive two-parameter snap-field model of *where* hallucinated boundaries land). Salvage for the
merge: B-083's pretrained-vs-scratch signed-error control (provenance attribution) and C-029's gradient-alignment
excess score on media, where the true boundary is physically on no gradient at all — the sharpest testbed.

The rest of gen_B's foundation-model cluster survives: B-084 (nested-anatomy prompt ill-posedness) was checked
against A-001/A-006 — its variance-decomposition and hierarchy-ambiguity-score designs are genuinely distinct;
B-085/B-086/B-087/B-088 have no T01 counterpart. Gen_C's C-030/C-033/C-034/C-036/C-038 survive, two of them only
as protected halves of competing pairs (below).

### Evaluation metrology — one cross collision, one dense family

**`A-072 → duplicate_of B-020`** (medium confidence): both claim published method orderings on medical benchmarks
are statistically unresolved. A-072 argues from training-side seed/split variance, B-020 from evaluation-side
test-set power — one power-audit paper. The merge should keep A-072's replication-probability validation design.

The wider metrology overlap (gen_A 068–075, gen_B 013–024, gen_C 039–048) is a *family*, not a duplicate pile:
each member names a different confound (LR tuning, wall-clock budgets, benchmark redundancy, test-label noise,
Hausdorff test-retest variance, preprocessing, empty-case conventions, resolution, matting-vs-IoU, instance
conventions). Flagged as families F11 and F12 with merge-order guidance; collapsing them into one "evaluation is
broken" idea would destroy ten distinct falsifiable claims. Intra-shard containments were cut instead:
`A-020 → A-068`, `C-040 → C-010`, `C-042 → C-020` (the latter two literally contained inside the canonical
records' own prediction text — under-flagged by gen_C).

### Uncertainty — no hard cross-duplicate, two protected disagreements

The three uncertainty clusters (gen_A 061–067, gen_B 076–082, gen_C 034/076/083) mostly measure *different
instruments*: multimask spread, prompt-jitter variance, trained ensembles, K-hypothesis heads, per-rater
supervision. Two real tensions were found and protected rather than merged:

- **A-066 vs C-034**: gen_A calibrates prompt-jitter variance as *epistemic model uncertainty* (decoupling from
  ambiguity OOD); gen_C uses the same probe as a *stimulus-ambiguity* meter. Competing calibrations of one
  instrument — a decisive joint experiment, not a duplicate.
- **B-059 vs B-077**: ensemble disagreement maps irreducible rater ambiguity vs correctable label error —
  competing interpretations inside one shard, kept as a pair.

One intra-shard cut: `B-082 → B-076` (both discover that spatial uncertainty is ~deterministic
boundary-distance geometry; recalibration-fix and MC-dropout-null are two arms of one claim). The
model-diversity-predicts-rater-disagreement family (A-061, B-059, B-077, C-083) is flagged F01 with A-061 kept
as the zero-training canonical member.

### Other cross-territory hard cuts

- **`C-013 → B-003`**: annotation-style fingerprints (tool signature is one style factor within the
  annotator/institution style claim; keep C-013's controlled dual-tool re-annotation as the cleanest causal
  design). A-036 stays separate — it is a provenance claim about SAM/SA-1B machine annotation, pairing with A-085.

## 2. Intra-shard near-duplicates (generator hints adjudicated + unflagged catches)

Generator-hinted pairs: gen_A's 009/063 collapsed (`A-063 → A-009`: same jitter-beats-IoU-head claim restated at
matched FLOPs); gen_A's 040/086 *upgraded to protected competing pair* (mechanical ceiling vs learned prior);
gen_C's C-010/C-040 collapsed and C-001/C-043 collapsed as hinted; C-030/C-034 and C-017/C-080 kept distinct as
the generator claimed. All other hinted links verified as linked-but-distinct.

Catches the generators did **not** flag:

| cut | why |
|---|---|
| `A-093 → A-081` | thermal tone-curve is the flagship case of input-transform adaptation; A-081's own fastest-falsification already names "one thermal domain, LUT vs LoRA-8" |
| `A-043 → A-070` | camouflage is one instance of the general under-prompting audit A-070 runs across 8 claimed-failure domains |
| `B-075 → B-047` | per-site heads and harmonized-label federation are two interventions on one claim: site label protocols, not optimization, dominate multi-site loss |
| `B-052 → B-046` | offline harmonization and test-time normalization both instantiate "statistical alignment erases the pathology signal" |
| `B-100 → B-012` | temporal (per-structure stopping) and spatial (targeted regularization) views of one phenomenon: late memorization of boundary-band label noise |
| `B-082 → B-076` | see uncertainty section |
| `C-042 → C-020`, `C-078 → C-050` | claims contained in / extending the canonical record's own prediction text |

Every cut carries a salvage note in `duplicates.json` so the consolidator's merge loses no falsification arm.

## 3. High-value anomalies protected from over-dedup

Ten **competing pairs** (both members protected; merging either pair into one vague claim would destroy a decisive
experiment): A-040/A-086, A-017/A-046 (a matched *contradiction* about where label conventions live), A-019/A-053,
A-057/B-097, B-059/B-077, A-066/C-034, A-005/C-036, C-052/C-063, C-067/C-085, A-027/C-093.

Twelve **singular anomalies** protected because they superficially resemble a family they do not belong to:
C-090 (human motion pop-out — psychophysics, not a temporal-model variant), B-079 (abstention rejects the sick),
B-065 (intermediate-accuracy automation wins after human correction), A-076 (random-encoder control), C-025
(polarization triviality), A-098 (LoRA re-basing), C-004 (exposure-defined fire GT), B-094 (absence detection with
a learnability claim), A-084 (self-consistency as training signal, not uncertainty meter), C-099 (generated-smoke
spoofing), A-090 (SA-1B privacy-blur shortcut — idea protected, premise still needs the fact-check gen_A flagged),
B-093 (regression beats segment-then-measure).

## 4. Notes for the consolidator

1. Family **F06 (supervision-definition gap)** has the highest residual over-merge risk in the batch: five kept
   ideas (A-067, A-089, B-001, B-047, C-001) share one theme and must not be collapsed across; the two legitimate
   collapses inside it (B-075, C-043) are already cut.
2. A-039 is a territory encroachment (T01 idea about transparency conventions); keep, but co-cluster with gen_C's
   transparency-ontology ideas (C-002/C-081). Gen_A's self-flagged T02-adjacent ideas (A-092/A-094/A-096) were
   checked against the full gen_B shard: no counterparts exist; keep in T01.
3. Under quota pressure, merge within twins/families in the order stated per family in `duplicates.json`
   (e.g. A-050+A-062, A-032+A-064, B-019+B-060, A-023+A-025, C-003/C-074/C-075 within-territory only).
4. My verdicts are independent; where judges A/B disagree on the four medium-confidence cross cuts
   (A-072, B-083, C-029, C-013), the disagreement itself is signal — those four are the borderline of the
   dedup standard.

## Compliance

- Independent audit; no shard file modified; no canonical state touched.
- No novelty verification performed; nothing herein asserts literature novelty.
- No invented citations, papers, datasets, benchmarks, or experimental results.
