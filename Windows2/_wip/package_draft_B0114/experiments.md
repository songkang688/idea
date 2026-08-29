# Experiments — B-0114: Prompts as Registers

Sections §14–§21. Protocol source of truth: N's `stage5_agent_N/exp_01.md` (killer) and `exp_02.md`
(gate), as battle-locked by Q (`top5.md`) and S (`final3.md`). Nothing here relaxes those locks.

---

## §14 Killer experiment specification (the 24-run grid)

**One dense benchmark, one backbone pair, four arms, three seeds. Everything else is the full matrix (§16).**

| Element | Specification |
|---|---|
| Task | **ADE20K** semantic segmentation (Zhou et al., CVPR 2017), 150 classes, standard train/val split |
| Backbones (frozen) | **DINOv2 ViT-B/14** (register-free) vs **DINOv2 ViT-B/14 + registers** (register-equipped sibling; Darcet et al. checkpoints from the DINOv2 repo) |
| Arms | (a) `learned` VPT-shallow, K=16; (b) `frozen_random`, K=16, same init distribution as VPT; (c) `attention_bias` — test-time-registers construction (arXiv:2506.08010), no appended token; (d) `no_token` |
| Heads | linear per-patch probe **and** light decoder (both reported; one head class per config, shared across arms) |
| Seeds | 3 (seed controls token init, head init, data order) |
| Runs | 4 arms × 2 backbones × 3 seeds = **24 runs** |
| Trainable params | prompts/bias + head only; matched across token arms; backbone bit-identical across arms per (variant, seed) |
| Readouts | per-arm mIoU; decomposition table (learned = a−max(b,c); register-bias = c−d; insertion = b−d); H2 seed-paired directional test; signature battery incl. **NOP-vs-broadcast diagnostics** (arXiv:2606.08105) |
| Budget | 24 runs × ~6–10 h on one A100-40GB (fits 24 GB at ViT-B, frozen backbone) ≈ **1–1.5 GPU-weeks** |
| Config draft | `configs/killer_ade20k.yaml` |

**Decision framing (binding):** every cell of the outcome space maps to a pre-registered interpretation
(§18). In particular: **if learned embeddings fully explain the gains — the dense-task replica of VPT
Fig. 11 — the mechanism claim STOPS** (§19); that outcome ships as the deflationary note, it does not
get argued around.

Two protocol details fixed at package time to prevent drift:

1. **Arm-(c) calibration.** The attention-bias arm uses the released test-time-registers procedure
   (register-neuron identification on the register-free backbone; bias/token-slot activation shifted at
   inference and held fixed during head training). No gradient flows into backbone weights. On the
   register-equipped backbone, arm (c) is still run (the construction is well-defined there) — its
   predicted effect under the register account is ≈0, which is itself a pre-registered check.
2. **Prompt-Fixed fidelity.** Arm (b) reproduces VPT's Prompt-Fixed setup exactly (same init scale,
   never updated) so that the classification control (§16) is a faithful Fig. 11 reproduction and the
   dense arm (b) is its exact dense analogue.

## §15 Binding ordering condition — the exp_02 gate & the B-0001 arm

**The 24-run grid is not funded until N's exp_02 returns.** (Q Round-3 lock, S seat conditions.)

- **exp_02** (~1 GPU-week, cheapest in the B batch): stratified audit of the register-norm map as a
  per-pixel error predictor — DINOv2 / DINOv2-reg / test-time-register-patched DINOv2 × ADE20K +
  Cityscapes × 5 predictor maps (norm map, softmax entropy, distance-to-boundary, edge density,
  prototype distance), evaluated **within foreground strata and boundary-distance bands**, not just
  overall. Config draft: `configs/exp02_gate.yaml`.
- **Gate rule (pre-registered):**
  - norm map **loses** to any free baseline within-foreground on register-free models → **DROP the
    B-0001 arm without ceremony**; B-0114 proceeds as a pure mechanism paper; the deflationary audit is
    published under B-0001's name (merged registers note branch per exp_02 §Dissociation).
  - norm map **wins** its strata → the B-0001 arm stays *in B-0001's own paper*; B-0114 still makes
    **no uncertainty claims** (PI binding: one bet in two costumes unless dissociated).
- **Dissociation enforcement carried into code** (prototype, kept at scale): the norm-vs-error hook is
  quarantined in `src/prototype/src/vpt_registers/b0001_hook.py`, runs only under `--with-b0001-hook`,
  prints under a "B-0001 TERRITORY" banner, and no B-0114 module imports it — properties enforced by
  AST-level tests. Claim-level dissociation: B-0114 answers *where VPT's dense gains come from*
  (mechanism attribution); B-0001 answers *whether artifact maps are usable signal* (consequence audit).
  Neither result implies the other.
- **What may run before the gate returns** (week-one co-schedule, §25): infrastructure only — the
  token-injection wrapper, the arm-(c) module, and the **classification bug-detector control** (§16),
  which is a prerequisite, not a result.

## §16 Full experiment matrix beyond the killer

Committed only after the killer grid lands in a live cell of §18; pre-specified now so scope cannot
silently grow.

| Block | Contents | Purpose | Budget |
|---|---|---|---|
| **E0 — classification control (prerequisite)** | VTAB-style triplet (e.g., CIFAR-100 / DTD / EuroSAT), arms (a),(b),(d), both backbones, 1 seed then 3 | **must reproduce Prompt-Fixed ≈ Linear (VPT Fig. 11)**; failure = implementation bug, all results embargoed until fixed | ~2 GPU-days |
| **E1 — killer grid** | §14 | RQ1 + RQ3 on ADE20K | 1–1.5 GPU-weeks |
| **E2 — sink-only control arm** | arm (e) added to E1's register-free cells (config `with_sink` lineage) | separates in-softmax geometry (token present, values zeroed) from arm (c)'s biased-softmax geometry; bounds the denominator confound jointly with E3 | ~1 GPU-day |
| **E3 — token-count sweep** | K ∈ {1, 4, 16, 64} for arms (a),(b) on register-free ADE20K | register absorption saturates at small K (Darcet: ~4 registers suffice); generic capacity/temperature effects scale with K — divergent signatures | ~3 GPU-days |
| **E4 — VPT-deep variant** | arms (a),(b) deep-insertion on E1's grid | insertion mechanics differ shallow vs deep (H hidden assumption 4) | ~4 GPU-days |
| **E5 — task generalization** | Cityscapes segmentation + NYUv2 depth (RMSE), killer arms | dense ≠ ADE20K-only; depth = non-classification dense readout | ~1 GPU-week |
| **E6 — backbone generalization** | one supervised ViT-B pair: vanilla vs PH-Reg-patched (arXiv:2505.21501) or test-time-register-patched (arXiv:2506.08010) | the H2 contrast is not a DINOv2 quirk; patched-sibling design removes the "different pretraining run" objection (§21.4) | ~4 GPU-days |
| **E7 — signature deep-dive** | NOP/broadcast class shares per layer/arm/K; register-competition on equipped backbone; norm distributions | RQ2; mandatory per L Finding 1 | analysis-only |

Full-study total: **4–6 GPU-weeks** (N exp_01 estimate), entered only from a live cell.

## §17 Metrics & statistical analysis plan

- **Task metrics:** mIoU (ADE20K, Cityscapes), RMSE (NYUv2). Reported per arm as 3-seed mean ± sd.
- **Decomposition:** computed seed-wise then aggregated; telescoping identity asserted programmatically
  (prototype invariant carried to scale). Components reported with seed sd; fractions of total VPT gain
  reported with the denominator's sd propagated.
- **H2 test (pre-registered):** seeds are paired across backbones (same token/head init streams).
  Statistic: mean seed-paired gap Δ = gain(free) − gain(equipped). **Declared positive only if
  Δ > 2× pooled seed sd** (Stage-6 lock). With n=3 seeds this is a directional check, not a
  significance ceremony — the package says so in print, and the full matrix (E5/E6) is what upgrades it
  to a claim about "dense tasks" and "backbones" in general.
- **Arm-fraction thresholds:** arm (b) or (c) "reproduces X% of VPT's gain" is computed against
  (a−d) per seed per backbone. The pre-registered kill threshold is **<5% each** (§19); the pivot
  threshold is **arm (c) ≥ 50%**.
- **Signature metrics:** attention-sink mass (patch-query mass onto prompt slots, per layer);
  high-norm outlier fraction; prompt-to-patch norm ratio; NOP-vs-broadcast class shares
  (arXiv:2606.08105 diagnostics); register-displacement on the equipped backbone. Signatures are
  **descriptive conditions on H1**, not standalone claims: H1 requires *both* a non-zero arm-(c)
  fraction *and* register signatures on learned prompts.
- **Multiple readouts discipline:** the paper's headline is decided by the decomposition + H2 only.
  Signature analyses are labeled exploratory wherever they leave the pre-registered battery.

## §18 Pre-registered interpretation table (binding)

Read on register-free ADE20K unless stated. "b", "c" = fraction of total VPT gain (a−d) reproduced.
Every cell was written **before** any real-data run; the sandbox did not edit it.

| Cell | Outcome | Interpretation | Consequence |
|---|---|---|---|
| K1 | b < 5% AND c < 5% AND H2 gap < 2× sd | **dense-task replica of VPT Fig. 11** — all gain is learned content; register connection is cosmetic everywhere | **STOP mechanism claim** (§19). Ship deflationary note (title §1.4): completes Fig. 11 on dense tasks, closes DA-VPT's open question negatively, retires B-0001's motivation link. Merged-note branch with exp_02 activates; seat degrades per S; B-0194 is named replacement |
| K2 | b < 5% AND c < 5% BUT H2 gap ≥ 2× sd | content-only arms, yet VPT behaves differently by register regime — geometry arms mis-specified or mechanism is content-mediated (learned prompts carry register function *only when trained*) | Run E2/E3 diagnostics before any claim; if signatures show learned-prompt sink mass ≫ frozen, write the H2-led paper (title §1.5) with the mechanism question explicitly open |
| M1 | 5% ≤ c < 50%, signatures positive (learned prompts classify as NOP/broadcast registers, frozen do not) | **register function confirmed as a minority component** — the predicted branch | Mechanism paper (titles §1.1/§1.2): decomposition + signatures + H2; E5/E6 fund generalization |
| M2 | 5% ≤ c < 50%, signatures negative | gain without register signatures — attention-geometry helps for a non-register reason (smoothing/temperature) | Report as attention-geometry component, **not** register function; E2/E3 arbitrate; title §1.2 (question form) |
| P1 | c ≥ 50% | attention-bias injection is most of VPT's dense value | **PIVOT** to retrofit paper (title §1.3): training-free VPT substitute; the portfolio's second constructive shot; VPT-comparison table becomes the headline |
| X1 | b ≥ c and b ≥ 20% | raw insertion (denominator/capacity) rivals bias — H's confound is live | E2+E3 mandatory before interpretation; if sink_only ≈ b, the effect is in-softmax geometry, not register absorption; scope claims accordingly |
| X2 | any arm ordering unstable across seeds (sign flips) | under-powered or task-idiosyncratic | extend seeds on the unstable cells only (pre-approved +2 seeds); if still unstable → mush handling (§19) |
| H2-only note | H2 gap ≥ 2× sd in ANY cell | reported in every branch | the boundary-condition finding stands independently; on the equipped backbone arm (c) ≈ 0 is the consistency check |

**Mush definition (S battle, FF attack):** an outcome lying outside every row above (e.g., c between
thresholds with contradictory signatures AND unstable H2). Pre-registered handling: no headline claim;
degrade to the mechanism half of the merged exp_02 note; PI decides on B-0194 activation. Mush is a
named branch, not a failure to plan.

## §19 Stop / pivot / kill criteria (binding, verbatim-in-substance from N/Q/S locks)

- **STOP (Fig. 11 replica — the task-mandated stop):** if the killer grid lands in K1 — learned
  embeddings fully explain the gains (arms b and c each <5% of VPT's dense gain across seeds AND H2
  gap < 2× seed sd) — **the mechanism claim stops.** No re-runs hunting a positive cell, no threshold
  softening. Output: deflationary note (title §1.4) or the mechanism half of the merged exp_02 note.
- **PIVOT (retrofit):** arm (c) ≥ 50% of VPT gain → the paper becomes the training-free-substitute
  recipe (title §1.3, cell P1).
- **HALT (bug detector):** the classification control E0 fails to reproduce Prompt-Fixed ≈ Linear →
  implementation bug assumed; **all** results embargoed until the control reproduces print.
- **DROP (B-0001 arm):** exp_02 gate rule, §15.
- **KILL (scoop):** a register-mechanism paper with dense-task token arms prints before execution →
  seat kill (Stage-6 lock; freshness protocol §13).
- **KILL (calendar):** execution has not started this quarter → obsolescence clock fires; PI decides
  (the register-free backbone population decays; §26).
- **STOP (classification arms):** early-stop the classification extension if E0 passed and the dense
  result is already decided — classification adds nothing beyond the control role.
- **Named replacement:** if the seat dies by K1 or scoop, **B-0194 activates without a new battle**
  (S `why_not_the_other_two.md`).

## §20 Prototype status & sandbox results (SANDBOX-ONLY — labeled per the provenance banner)

`src/prototype/` is a verbatim copy of Agent T's CPU synthetic prototype (`_wip/stage7_proto_B0114/`):
a tiny ViT pretrained in-process with global-only objectives on generated scenes, 39 passing tests,
deterministic, no downloads. **It validates the instrument** — arms, telescoping decomposition,
H2 readout, signature battery, B-0001 quarantine — **and nothing else.**

> **NO NUMBER BELOW IS AN ADE20K / CITYSCAPES / NYUV2 / IMAGENET / DINOv2 RESULT.** All values were
> MEASURED ON SYNTHETIC SCENES generated in-process by a toy backbone constructed so that the
> hypothesized mechanism has something to act on. They appear here for instrument-validation
> transparency only.

Sandbox headline (from `src/prototype/README.md`, `configs/default.yaml` + `with_sink.yaml`, 3 seeds):

| component (mIoU delta, sandbox) | register_free | register_equipped |
|---|---|---|
| total VPT gain | +0.040 ± 0.023 | +0.014 ± 0.019 |
| insertion (geometry) | −0.064 ± 0.030 | +0.000 ± 0.002 |
| content transfer | +0.111 ± 0.019 | +0.012 ± 0.017 |
| co-adaptation | −0.007 ± 0.011 | +0.002 ± 0.003 |
| sink geometry (`sink_only`) | +0.004 ± 0.041 | +0.018 ± 0.018 |
| H2 gap (free − equipped) | **+0.025 ± 0.042** (direction positive, inside 3-seed noise) | — |

**The honest read (HYPOTHESIS-level risk, NOT a dense-task finding):** in the sandbox, **the
learned-embedding axis dominated** — content transfer carried essentially the whole register-free VPT
gain, frozen-random insertion was *negative*, and the value-zeroed sink arm gained ≈0 despite soaking
more attention mass than learned tokens. That is **content-dominant, Fig.-11-like behavior in a toy
that was constructed to favor the register mechanism.** We log this as a risk input (§26 R1): it
raises the credence we assign to the K1 kill cell on real data. It is **not** evidence about dense
tasks — the toy (dim 48, depth 3, 32×32 scenes) does not and cannot exhibit the scale-emergent
high-norm artifact phenomenon (Darcet et al. observe it in large, long-trained ViTs), which is the very
phenomenon H1 rides on. The pre-registered interpretation table (§18) was written before the sandbox
ran and is unchanged by it.

Also measured in the sandbox and carried as instrument lessons (not findings): (i) the H2 *direction*
appeared (equipped baseline higher, every component smaller) — the qualitative pattern exp_01 predicts,
demonstrated in a sandbox built to contain it; (ii) prompts *displaced* attention mass from built-in
registers on the equipped backbone — a register-competition signature the real runs should look for;
(iii) injected tokens made patch features MORE sensitive to the global nuisance, not less — the
invariance metric cleanly dissociates "absorb globals away" from "route globals in", and which branch
real backbones take is an open empirical question.

Prototype → real-run migration path (from T's README, adopted): swap TinyViT for frozen DINOv2 /
DINOv2-reg and synthetic scenes for ADE20K; keep `train_arm`, `metrics.py`, `signatures.py`; replace
the toy value-zeroing sink with the exact 2506.08010 construction for arm (c); add K-sweep, VPT-deep,
NOP/broadcast diagnostics, classification controls. See `src/README.md`.

## §21 Confounds & threats to validity

1. **Softmax-denominator confound (H's central attack; Reviewer-2 leftover, answered in print).**
   Inserting any token changes every attention normalization — "X% reproduced by frozen tokens"
   conflates register absorption with attention smoothing. Bounds, not elimination: (i) arm (c)
   changes geometry *without* sequence-length change; (ii) arm (e) `sink_only` holds the denominator
   shift of (b) while muting content; (iii) the K-sweep (E3) separates saturating register absorption
   from K-scaling temperature effects. The paper states plainly that the confound is **bounded, not
   eliminated** — the residual is priced in the limitations section, not hidden.
2. **Head-tuning artifact.** If VPT's benchmark gains are partly head-tuning artifacts, the
   decomposition inherits that fragility (H hidden assumption 2). Mitigation: two head classes (linear
   + light decoder) reported for every arm; conclusions must hold under both.
3. **Norm-signature validity.** PH-Reg shows artifact tokens can be *low*-norm — norm statistics alone
   never define register function; the NOP/broadcast diagnostics are the primary signature axis
   (mandatory per L).
4. **Backbone-pair matching.** DINOv2 vs DINOv2-reg are separate pretraining runs (same data/recipe,
   registers added) — not a strict intervention. Mitigation: E6's patched-sibling pair (same weights,
   registers added post hoc via 2506.08010/PH-Reg) provides the within-run contrast; H2 must agree in
   direction across both pair types.
5. **VPT-shallow vs VPT-deep.** Insertion mechanics differ; killer grid is shallow-only, E4 covers deep
   before any "VPT in general" wording is used.
6. **Single-K killer.** K=16 chosen to match common VPT practice; all fraction claims are scoped to the
   sweep once E3 lands.
7. **Generalization scope.** ADE20K-only until E5; DINOv2-family-only until E6; claims are worded to
   the evidence in hand at each publication branch.
8. **Obsolescence.** Register-equipped backbones are becoming default (DINOv3 ships with registers).
   The H2 arm is the insurance: it converts "a paper about the past" into a boundary-condition law that
   explains *why* the register-free result is historical (§26 R3).
9. **Sandbox anchoring.** Risk that the team (or reviewers) treat §20's content-dominant toy outcome as
   evidence for K1. Countermeasure: the provenance banner, HYPOTHESIS labeling, and the fact that the
   interpretation table §18 predates the sandbox and is locked.
