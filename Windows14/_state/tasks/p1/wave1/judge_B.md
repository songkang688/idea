# P1 Wave B — Judge B: Architecture-Permutation / SAM+X Filter — Windows14

- **Task:** `p1_wave1_judge_B`
- **Role:** `judge_B_permutation_filter` (independent of Judge A)
- **Status:** complete
- **Judged at (UTC):** 2026-08-28T18:55Z

## Inputs (read-only, fetched from remote shard branches)

| Shard | Branch | Ideas |
|---|---|---|
| `worker_A.ideas.jsonl` | `origin/cursor/windows14-p1-wave-a-worker-a-e978` | 132 |
| `worker_B.ideas.jsonl` | `origin/cursor/windows14-p1-wave-a-worker-b-c6ba` | 126 |
| `worker_C.ideas.jsonl` | `origin/cursor/windows14-p1-wave-a-worker-c-4be5` | 124 |
| **Total** | | **382** |

No canonical ledgers touched (`ideas_master.jsonl`, `research_state.json`, `window.lock.json` untouched, per lock).

## Filter mandate and rubric

Flag ideas that are, at the hypothesis level:

1. **Mere architecture permutations** — swap/rearrange modules with no mechanism claim.
2. **Module A+B pairings** — SAM+retrieval, SAM+SSM sidecar, detector+matting, sensor fusion, gated multi-head designs, where the pairing itself is the contribution.
3. **SAM + loss/backbone swaps** — new loss / different backbone as the deliverable.
4. **Mechanical medical/smoke transfers** — known natural-image findings or known methods ported to the domain with no domain-specific mechanism.
5. **Parameter-only scaling** — rank/size sweeps without a mechanism.

Verdicts:

- **keep** — falsifiable mechanism/behavior claim; any architectural element is the *test instrument*, not the contribution.
- **mutate** — a real hypothesis is buried inside a permutation-shaped idea; the flags file specifies the salvage (what must become the primary claim).
- **kill** — the pairing/swap IS the whole idea, and any salvageable insight is already carried by another idea in the shards.

## Verdict counts

| Shard | keep | mutate | kill | total |
|---|---|---|---|---|
| worker_A (SAM/PEFT) | 120 | 12 | 0 | 132 |
| worker_B (medical) | 124 | 2 | 0 | 126 |
| worker_C (smoke/fire/transparent) | 115 | 8 | 1 | 124 |
| **Total** | **359** | **22** | **1** | **382** |

The low kill rate is a genuine finding, not leniency: all three generators wrote mechanism-first, falsifiable hypotheses rather than method proposals, so almost nothing is a *pure* permutation. Where permutation patterns appear, they nearly always wrap a salvageable claim — hence mutate, with explicit re-centering instructions, dominates kill.

## Kill (1)

- **w14p1c-050** (`output_format_permutation`) — learned router + binary/matte dual heads. Pure architecture permutation; "routing each instance to its right head helps" is near-tautological, and the real insight (binary masks are a category error for amorphous matter) is already carried by w14p1c-041/042/045/024.

## Mutates (22), by pattern

**Placement permutations (tune-only-module-X entries of the same sweep family):**
- **w14A-016** (hypernetwork MLP), **w14A-042** (neck-bias BitFit), **w14A-047** (leave-one-in atlas). Salvage: fold into the placement-concentration hypotheses (w14A-030 fracture layers, w14A-117 global-block bottleneck, both kept) and measure the claimed mechanism directly instead of reporting a single-site win. Kept family members with real dissociations: w14A-030, w14A-077, w14A-117, w14A-127.

**Known-method ports to SAM (mechanical transfers within territory):**
- **w14A-040** (O-LoRA-style orthogonality), **w14A-049** (SVD adapter merging vs averaging), **w14A-053** (WiSE-FT-style alpha interpolation), **w14A-076** (prefix tuning), **w14A-112** (ControlNet-style zero-init grafting). Salvage: in each case a measurable SAM/segmentation-specific quantity exists (adaptation-manifold dimensionality, adapter subspace geometry, capability-ordered forgetting spectrum, decoder task capacity, small-data dominance law) — make it the deliverable.

**Module A+B pairings:**
- **w14A-060** (SAM+retrieval), **w14A-074** (SAM+FFT branch), **w14A-079** (SAM+scanline SSM, the SAM+Mamba pattern), **w14_p1b_094** (dense decoder + organ-token sequence model), **w14p1c-030** (RGB-to-polarization predictor — also has a data-processing-inequality problem as stated), **w14p1c-048** (detector+matting), **w14p1c-055** (background subtraction+SAM), **w14p1c-097** (thermopile fusion). Salvage: probe/measure the claimed capability absence or complementarity first; the module is the intervention, not the contribution.

**Backbone swap:**
- **w14A-120** (SAM decoder transplanted onto another frozen encoder). Salvage: bridge-rank vs representational-distance law as the deliverable, differentiated from MobileSAM-style distillation.

**Gating/aux-task/loss permutations:**
- **w14p1c-037** (day/night two-head gate → test regime disjointness instead), **w14p1c-066** (aux disagreement head → require representation-level mechanism check), **w14p1c-095** (advection-consistency loss → physics-validity map first).

**Mechanical cross-domain transfers of known findings:**
- **w14_p1b_122** and **w14p1c-092** (CLIP negation blindness ported to medical / smoke prompting). Salvage: domain-specific locus claims (medical report-pretrained text encoders; fusion-level bag-of-concepts collapse vs text-encoder separability).

## Keep-with-note (10)

Kept, but the flags file records a mandatory framing/control: w14A-043, w14A-072, w14A-102, w14A-118, w14A-124, w14_p1b_067, w14p1c-056, w14p1c-059, w14p1c-090, w14p1c-102. Common thread: an architectural or known-method element is present but a specific dissociation/control keeps the idea hypothesis-first; the note states the control that must be run.

## Notes for the consolidator

1. Verdicts here are per-hypothesis under the permutation filter only; Judge B did **not** dedupe near-identical hypotheses across shards (e.g., prompt-jitter instability appears as w14A-010 / w14_p1b_005 / w14p1c-001/061; negation blindness as w14_p1b_122 / w14p1c-092; patch-grid minimum-size limits as w14A-021 / w14_p1b_061 / w14p1c-105). Cross-shard merging is consolidator/Judge-A territory.
2. Mutate verdicts carry an explicit `mutation` field in `judge_B.flags.jsonl` — apply it at merge time rather than dropping the idea.
3. The placement-permutation family in worker_A should be consolidated to the kept anchors (w14A-030/077/117/127) with the mutated members folded in as validation protocols.

## Files written (only)

- `Windows14/_state/tasks/p1/wave1/judge_B.md` (this file)
- `Windows14/_state/tasks/p1/wave1/judge_B.flags.jsonl` (382 verdict lines, one per idea)
- `Windows14/_state/tasks/p1/wave1/judge_B.done.json`

## Recommended next task type

`p1_wave1_consolidator` — merge worker shards with Judge A + Judge B flags into `ideas_master.jsonl`.
