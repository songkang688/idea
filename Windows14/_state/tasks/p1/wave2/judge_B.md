# P1 Wave 2 — Judge B: Architecture-Permutation / Feasibility Filter — Windows14

- **Task:** `p1_wave2_judge_B`
- **Role:** `judge_B_permutation_filter` (independent of Judge A; Judge A verdicts not consulted)
- **Status:** complete
- **Judged at (UTC):** 2026-08-28T20:30Z

## Inputs (read-only, fetched from remote shard branches)

| Shard | Branch | Ideas |
|---|---|---|
| `worker_A.ideas.jsonl` (synthetic data / domain shift) | `origin/cursor/windows14-p1-wave2-worker-a-cc54` | 133 |
| `worker_B.ideas.jsonl` (restoration / diffusion / degradation) | `origin/cursor/windows14-p1-wave2-worker-b-8795` | 126 |
| `worker_D.ideas.jsonl` (object detection science) | `origin/cursor/windows14-p1-wave2-worker-d-a7e5` | 124 |
| `worker_E.ideas.jsonl` (language-grounded dense prediction) | `origin/cursor/windows14-p1-wave2-worker-e-e584` | 125 |
| **Total** | | **508** |

worker_C was NOT read (still generating, per dispatch). No canonical ledgers touched (`ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json` untouched, per lock). No worker or judge_A files modified.

## Filter mandate and rubric (same protocol as wave1 judge_B)

Flag ideas that are, at the hypothesis level:

1. **Mere architecture permutations** — swap/rearrange modules or capacity with no mechanism claim.
2. **Module A+B pairings** — bolt module B onto system A where the pairing itself is the contribution.
3. **SAM + loss/backbone swaps** — a new loss or a different backbone as the deliverable (generalized here to any backbone/head swap, since wave2 territories are not SAM-centric).
4. **Mechanical medical/smoke transfers** — generalized to any mechanical port of a known method or known finding into the shard's territory with no territory-specific mechanism.
5. **Parameter-only scaling** — rank/size/hyperparameter sweeps without a mechanism.

Verdicts:

- **keep** — falsifiable mechanism/behavior claim; any architectural or method element is the *test instrument*, not the contribution.
- **mutate** — a real hypothesis is buried inside a permutation-shaped idea; the flags file specifies the salvage (what must become the primary claim).
- **kill** — the pairing/swap IS the whole idea, and any salvageable insight is already carried by another idea in the shards.

## Verdict counts

| Shard | keep | mutate | kill | total |
|---|---|---|---|---|
| worker_A (synthetic/shift) | 129 | 4 | 0 | 133 |
| worker_B (restoration/diffusion) | 126 | 0 | 0 | 126 |
| worker_D (detection) | 124 | 0 | 0 | 124 |
| worker_E (open-vocab/grounding) | 124 | 1 | 0 | 125 |
| **Total** | **503** | **5** | **0** | **508** |

The very low mutate/kill rate is a genuine finding, consistent with wave1 (382 reviewed, 22 mutate, 1 kill): all four generators wrote audit-, dissociation-, and law-shaped hypotheses rather than method proposals. Wave2 is even cleaner than wave1 — the territories (data science, failure-mode audits, evaluation science, language-interface fragility) structurally resist permutation-shaped ideas. Zero kills because in every flagged case the buried hypothesis is not fully carried by another idea in the shards; mutate with explicit re-centering preserves it.

## Mutates (5), by pattern

**Training-schedule permutations (schedule bake-off as deliverable, mechanism asserted but unmeasured):**

- **w14w2a-011** (`synthetic_scaling_laws`) — synthetic-fraction annealing beats every fixed ratio. The coverage-to-bias phase mechanism is never measured by the stated arms (decay vs fixed vs reverse). Salvage: measure the phase-role mechanism directly (phase-swap probes, per-phase gradient alignment, boundary-bias accumulation); schedule win becomes the confirmatory exploit.
- **w14w2a-101** (`adaptation_training_dynamics`) — interleaved sim-real cycling beats sequential. Rehearsal is a standard continual-learning method mechanically transferred; the experiment is a cycle-count bake-off. Salvage: make the bidirectional domain-forgetting characterization primary (what each phase overwrites, linking to kept w14w2a-094's boundary-first forgetting).

**Mechanical known-method transfers into the territory:**

- **w14w2a-104** (`synthetic_data_harms`) — gradient-conflict pruning of synthetic corpora. Gradient-based data valuation is established in classification/instruction tuning; the headline is the ported pipeline's win. Salvage: the harm law (which synthetic samples are harmful and why; where alignment predicts harm and visual-quality filters fail) is the deliverable.
- **w14w2a-123** (`domain_randomization_science`) — adversarially chosen randomization parameters, 10x fewer renders. Active DR exists in RL/robotics; the contribution as framed is the ported loop plus an efficiency number. Salvage: the failure-geography claim (failures concentrate in small, stable regions of randomization-parameter space) is the measurable primary claim.

**Backbone swap + module pairing:**

- **w14E-071** (`alignment_mechanics`) — SSL spatial backbone + thin text-alignment adapter beats CLIP tower. Hybrids already exist (record concedes this) and the stated experiment is a matched-budget backbone bake-off. Salvage: the asymmetric-retrofittability law — quantify the cost of retrofitting alignment onto SSL features versus retrofitting locality onto contrastive features (the missing reverse arm).

## Keep-with-note (11)

Kept, but the flags file records a mandatory framing/control (common thread: a known method, known finding, or permutation-shaped instrument is present, and a specific dissociation or delta keeps the idea hypothesis-first):

- **w14w2a-012** — capacity-split grid: label-noise-injection control mandatory (synthetic-vs-real confounds label perfection with everything else).
- **w14w2a-034** — harmonized copy-paste vs full-scene generation: the crossover criterion (generator mask-obedience level) must be reported, else it is a data-pipeline bake-off.
- **w14w2a-121** — curriculum DR: kept solely because of the pretrained-backbone dissociation arm that directly tests the early-underfitting mechanism.
- **w14D2-001** — density-adaptive NMS threshold: oracle-threshold-vs-density law must lead; differentiate from trained Adaptive-NMS heads.
- **w14D2-067** — level-targeted weather adaptation: the frequency-signature-to-level-drift prediction is the deliverable; recovery-vs-parameters curves alone would be a placement sweep.
- **w14D2-112** — detector-regressor count readout: the pre-NMS score-mass linearity-beyond-saturation law is the claim; the counting pipeline is the exploit.
- **w14E-001** — BPE token-count bias: pixel-decision-level effect after frequency/size controls is mandatory (text-side token-length artifacts are documented).
- **w14E-029** — negation attraction: the attraction-vs-ignorance delta over documented retrieval negation blindness is mandatory; overlaps wave1 negation entries (consolidator note below).
- **w14E-053** — typographic mask theft: dense-specific quantities (mask-diversion geometry, dose-response, theft despite genuine referent) are the contribution; the attack's existence is documented for classification.
- **w14E-067** — register-token phantom detections: the quantitative position-stable FP fingerprint plus correction is the contribution; artifact tokens are documented for ViTs.
- **w14E-084** — round-number coordinate snapping: the geometric footprint (histogram spikes, error-vs-roundness law, regression-head contrast) must lead; numeric-token priors are documented for LLM arithmetic.

## Notes for the consolidator

1. **Cross-shard near-duplicates were NOT deduped here** (out of judge_B scope). Notable families the consolidator must merge: vocabulary-interference (w14D2-026 / w14E-034 / w14E-089); multilingual query divergence (w14D2-032 / w14E-004); plurality/grammatical number (w14D2-029 / w14E-037…042); part-query-returns-whole (w14D2-028 / w14E-110); modifier/attribute non-compliance (w14D2-024, w14D2-030 / w14E-043, w14E-046); rare-class collapse to frequent neighbors (w14D2-027 / w14E-057 / w14E-063); caption-salience recall bias (w14D2-087 / w14E-055 / w14E-060 / w14E-103 / w14E-107); benchmark contamination by generated/enhanced imagery (w14w2a-112 / w14w2b-077 / w14w2b-084 / w14w2b-085); test-set leakage via generators (w14w2a-008 / w14w2b-086 / w14w2b-115); JPEG block-grid artifacts (w14w2b-013 / w14D2-070); keyframe/sparse-annotation evaluation bias (w14w2b-120 / w14D2-117); pre-NMS score mass as latent density/count signal (w14D2-001 / w14D2-112 — same measurement primitive, two exploits); temporal flicker metrics (w14w2b-101, w14w2b-105 / w14D2-096, w14D2-113).
2. **Cross-wave overlap:** w14E-029/w14E-036 (negation) overlap wave1's negation entries (w14_p1b_122 / w14p1c-092, both wave1 mutates); the consolidator should merge the wave2 attraction-effect framing as the stronger form.
3. **Mutate verdicts carry an explicit `mutation` field** in `judge_B.flags.jsonl` — apply the re-framing at merge time rather than dropping the idea.
4. **Judge A verdicts were not consulted** (independence requirement); conflicts between judge_A and judge_B flags must be resolved by the consolidator.
5. **worker_C is pending**: this judgment covers only shards A, B, D, E (508 ideas); worker_C requires a separate judging pass when it lands.
6. Novelty remains unverified for all ideas; no papers, citations, or numbers were invented or checked here.

## Files written (only)

- `Windows14/_state/tasks/p1/wave2/judge_B.md` (this file)
- `Windows14/_state/tasks/p1/wave2/judge_B.flags.jsonl` (508 verdict lines, one per idea)
- `Windows14/_state/tasks/p1/wave2/judge_B.done.json`

## Recommended next task type

`p1_wave2_consolidator` — merge worker shards A/B/D/E (plus worker_C once judged) with Judge A + Judge B flags into the canonical ledger, after a worker_C judging pass.
