# PromptAmnesia — Experimental Design Specification (Windows4 / Idea_02)

**Epistemic status:** EXPERIMENT DESIGN. No experiment has been run. Every numeric value is a design
parameter or ESTIMATE. Machine-readable versions of these protocols live in `configs/`; executable
prototypes in `src/promptamnesia/`.

Execution order is **binding** (Stage 4 cross-paper ruling): E0 → E1 (gate) → freeze → E2 → E3 → E4 → E5.

---

## E0 — Pre-registration freeze

**Purpose.** Answer Stage-4 structural attack #1 (shared-grid poisoning) before it can occur.

**Procedure.**
1. Re-run the scoop-watch searches (`literature.md` §6); update related-work deltas if needed.
2. Re-verify all `[M]`-tagged citations that the pre-registration text quotes.
3. Freeze, in one tagged commit: `configs/shared_grid.yaml` (recipe), the matched-gain rule, the ordering
   contrast family (O1–O5), `configs/p082_gate.yaml` (target list + envelope definition), the
   ambiguity-probe mining protocol, and both click simulators.
4. After the tag, changes to any of these require a logged amendment section in the paper.

**Deliverable.** Tag `idea02-prereg-v1` on branch `cursor/windows4-research-idea-evolution-2962`.

---

## E1 — P082 gate: noise-floor envelope (RUNS FIRST; eval-only)

**Question (RQ1).** Do forgetting deltas of released fine-tuned checkpoints exceed the noise floor implied
by threshold, seed, prompt-sampling, and split variance?

**Subjects.** Frozen SAM ViT-B (and ViT-H reference); released MedSAM; released SAM-Med2D. Named
indictments use released checkpoints only (F8 rule).

**Retention domains.** COCO val2017 instance subset; LVIS-rare subset; TN3K; BUSI (checkpoint-dependent:
a checkpoint's own training domain is excluded from its retention set).

**Variance decomposition (the envelope).** For the **frozen** model, per (domain, prompt type):
- ≥5 prompt-sampling seeds (box jitter draws, point placement draws);
- ≥3 calibration/eval split draws;
- full binarization-threshold sweep on each calibration draw (tuned threshold then applied to eval draw);
- envelope = empirical 95% band of the |Δmetric| distribution across these replicates under the null
  "same weights, no forgetting". Implementation: `src/promptamnesia/threshold_gate.py::build_envelope`.

**Symmetric threshold protocol.** Frozen and fine-tuned checkpoints get thresholds tuned on the **same**
calibration split, then frozen for eval. No asymmetric oracle access (the C1-082 leakage trap).

**Pre-registered targets.** Listed in `configs/p082_gate.yaml` (checkpoint × domain × prompt-type cells).
The published-protocol re-evaluations reproduce each checkpoint's own documented prompting protocol first,
then re-measure under the symmetric protocol; both numbers are reported.

**Decision rule.** PROCEED iff ≥1 checkpoint shows a reproduced retention delta outside the envelope on
≥2 retention domains for ≥1 prompt type; else PIVOT (deflation branch). Implementation:
`threshold_gate.py::gate_decision`.

**Budget.** ESTIMATE 1–2 GPU-days. Partial one-domain readout available in <1 day (rubric kill-cheapness).

---

## E2 — Shared fine-tuning checkpoint grid

**Purpose.** Produce every checkpoint used by E3–E5 and by sibling paper P031, under one frozen recipe.

**Design matrix** (full spec `configs/shared_grid.yaml`):

| Axis | Levels |
|---|---|
| Domain | BUSI (ultrasound); MSD Task09 Spleen 2D (CT) |
| FT prompt mix | box-only; point-only; mixed (1/3 box-jitter, 1/3 single positive point, 1/3 iterative ≤5 clicks incl. negative) |
| Recipe | full-FT @ 3 LRs; decoder-only FT; LoRA enc+dec (attention q,v); VeRA-style random-direction control (rank-matched) |
| Loss aggregation (mixed column only) | min-loss-mask; all-mask (multimask enabled in both) |
| IoU-head loss | ON (default; the honest recipe). One OFF cell shared with P031 |
| Seeds | 3 (5 for headline cells if E1's envelope is wide) |

**Logging per checkpoint (free covariates, P108 residue).** step, train/val loss, target-domain val Dice
at tuned threshold, per-module-group update norm, encoder–decoder interface CKA drift. Never analyzed as a
headline claim; available for exploratory appendix only.

**Checkpoint cadence.** Dense enough that the matched-gain rule (below) can select within ±0.5 Dice:
every epoch on small sets, every N steps otherwise (set in config).

**Matched-gain rule (verbatim, used by E3/E4/E5 and P031).**
> For each (domain, mix, seed), let G\* be the best target-domain validation Dice achieved by the weakest
> recipe arm in that stratum. Every arm contributes the first checkpoint (in training order) whose
> target-domain validation Dice is within ±0.5 Dice points of G\*. Arms that never reach G\*−0.5 are
> excluded from matched comparisons in that stratum and reported. Validation Dice is computed at the arm's
> own calibration-split-tuned threshold.
Sensitivity: headline contrasts re-run at ±0.25 and ±1.0 tolerance.
Implementation: `src/promptamnesia/matched_gain.py`.

**Budget.** ESTIMATE 25–45 GPU-days (≈204 short ViT-B fine-tunes when the grid is fully expanded — see
`train_lora_stub --print-plan`). Trim order if over budget: (1) point-only column LR sweeps shrunk;
(2) ViT-H replication dropped; (3) seeds 3→2 on non-headline cells (headline cells keep ≥3 — Stage-4
obligation).

---

## E3 — P065 behavioral battery (prompt-type eval matrix)

**Question (RQ2/RQ5, H2/H3).** Is degradation prompt-type-structured *inside the mixed column*, and how
much of the naive ordering is coverage?

**Eval battery** (implementation `src/promptamnesia/eval_prompt_matrix.py`, protocols
`configs/p065_eval_battery.yaml`):

| Column | Protocol | Primary readout |
|---|---|---|
| box | GT-box + pre-registered jitter | Dice/mIoU at tuned threshold |
| 1-click | single positive point, interior-sampling rule | Dice/mIoU |
| iterative-5 | click k+1 at center of largest error component; negative clicks on FP regions | Dice@k curve; NoC@90 where defined |
| multimask-ambiguity | E4 (below) | oracle-vs-argmax gap |

**Retention suites.** COCO val2017 instances; LVIS-rare; the non-fine-tuned medical domain (cross-domain
probe). Frozen SAM evaluated under the identical protocol is the floor for every Δ.

**Threshold policy.** Per-arm, per-domain threshold tuned on the shared calibration split (same split for
frozen and fine-tuned), then frozen — the E1 code path, reused.

**Click-simulator sensitivity.** Every headline contrast duplicated under the alternative click-placement
rule (uniform-interior instead of error-centroid). Contrasts that flip are demoted to
simulator-dependent observations (Stage-3 RClicks/BREPS hygiene).

**Statistical plan.** Pre-registered contrast family (Holm-corrected):
- O1: Δ(1-click) vs Δ(box)
- O2: Δ(negative-click subprotocol) vs Δ(positive-only subprotocol)
- O3: Δ(Dice@click-5) vs Δ(Dice@click-1)
- O4: Δ(oracle best-of-3) vs Δ(argmax) [E4]
- O5: point-FT→box-eval vs box-FT→point-eval (coverage asymmetry, off-diagonal)

A contrast **counts** only if: Holm-significant under hierarchical bootstrap (images × seeds), point
estimate outside the E1 envelope, and it holds in the **mixed** column. Box-only-column orderings are
reported as the coverage map (RQ5), never as forgetting.

**Budget.** ESTIMATE 3–6 GPU-days (forward passes only; ~120 checkpoints × 4 columns × 3–4 suites).

---

## E4 — Diversity arm: oracle best-of-3 decomposition (C1-061)

**Question (RQ3/H4).** Capability loss or ranking loss?

**Probe set construction (pre-registered).** Mine COCO/LVIS annotations for nested/overlapping instance
pairs (part-vs-whole, object-vs-group). A probe = (image, point prompt at the ambiguous locus, set of ≥2
valid GT masks). Mining script and final probe index committed before E2 analysis begins. Target size:
enough probes for stable bootstrap CIs (design target ≥500; final N reported, never asserted in advance).

**Measurement per probe per checkpoint.** Multimask mode → 3 candidates + IoU-head scores.
- oracle = max over candidates of max-over-valid-GTs IoU;
- argmax = IoU (vs best-matching GT) of the head-selected candidate;
- gap = oracle − argmax.
Implementation: `src/promptamnesia/diversity.py`.

**Decomposition verdicts (pre-registered).**
| Observation | Verdict |
|---|---|
| oracle drops (all-mask-loss cells included) | capability loss — diversity-forgetting claim stands |
| oracle intact, argmax drops | ranking loss → transferred to P031, withdrawn here |
| oracle drops only in min-loss-mask cells | loss-aggregation recipe artifact — reported as such |

**Budget.** Included in E3's evaluation pass.

---

## E5 — P177 mechanism arm: splice × stitch × interpolation

**Question (RQ4/H5).** Where does the lost behavior live? Stitching controls **mandatory** (binding).

**Inputs.** Matched-gain checkpoint pairs (pre-FT SAM, fine-tuned arm) from E2 — no new fine-tuning.

**Module partition** (parameter-name map in `configs/p177_splice.yaml` / `src/promptamnesia/splice.py`):
image encoder · prompt encoder · decoder cross-attention blocks (token↔image) · decoder-rest (+ output
and IoU heads).

**Grid.** For each module group: swap in **both directions** × {no stitch, trained affine stitch} —
stitch = per-channel scale+shift (optionally 1×1 linear) at the swapped interface, trained on the
calibration split, everything else frozen, capped capacity. Plus **stitch-only cells** (no swap) to
calibrate stitch power. Plus per-module-group **α-interpolation** α ∈ {0, .25, .5, .75, 1} (WiSE-FT-style)
as the continuous baseline the binary splice must beat for informativeness.

**Confounder control.** Per-module update-norm accounting from E2 logs + one update-norm-matched
fine-tuning arm (added to E2 if E1 PROCEEDs) — otherwise "locus" re-describes the recipe.

**Readout (pre-registered).** Restoration fraction per cell and per prompt type:
R = (metric(chimera) − metric(FT)) / (metric(frozen) − metric(FT)), with hierarchical-bootstrap CIs.
Computed per battery column — the mechanism may be prompt-type-specific (bridge to E3).

**Verdict rule.** H5 stands only if cross-attn+stitch restores a large fraction while encoder+stitch
restores ≈none, in both directions, beyond the α-curve, CIs non-overlapping. Otherwise: locus claim
withdrawn; swap grid and α-curves reported descriptively.

**Budget.** ESTIMATE 2–4 GPU-days (stitch training is minutes per cell; the cost is battery re-evaluation
of chimeras — restrict chimera evaluation to the headline retention suite if needed).

---

## Cross-cutting rules

1. **No fake metrics.** Result tables in the package are structural skeletons (NaN) until a run artifact
   (config hash + seed + commit) exists. `eval_prompt_matrix.py --dry-run` emits the skeleton.
2. **Symmetric thresholds everywhere** — single code path (`threshold_gate.py`) for gate and battery.
3. **One matched-gain rule** — single code path (`matched_gain.py`) for E3/E4/E5 and P031.
4. **Every ordering claim carries:** seeds, CIs, envelope comparison, mixed-column status, simulator
   sensitivity status.
5. **Failure reporting:** arms excluded by the matched-gain rule, probes discarded by mining filters, and
   contrasts flipped by the alternative simulator are enumerated in the appendix, not dropped.
