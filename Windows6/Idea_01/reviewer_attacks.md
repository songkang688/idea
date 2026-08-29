# Idea_01 — Reviewer attacks & answers

Source of the A-series: [Reviewer2 attack top5 cheap](bc-ad2f6983-8ed1-53a5-b2ad-1c36114708f3),
recorded in `stage4_reviewer2_cheap5.jsonl`. The B- and C-series are our own
red team. **No attack is listed without the evidence that answers it**; an
attack with no shut-up experiment is an unmitigated risk and is labelled as one.

---

## A. The Stage-4 attacks (binding — these are why the idea survived)

### A1. "Windowing manufactures the result"

**The attack.** Windowing is a monotone intensity map. Choose the window that
compresses tissue contrast and any intensity clusterer will agree with anything.
Run one window and the finding is a preprocessing artifact.

**Why it is dangerous.** It is correct as stated. `proposal.md` §7 concedes it
outright.

**Evidence that shuts it.** E2: three clinical windows (abdomen 400/40, bone
2000/400, lung 1500/−600), **every cell reported**, H1 required on ≥2 of 3.
Holding on exactly one window is a pre-declared **pivot**, not a footnote.

### A2. "Agreement is not mechanism"

**The attack.** AMG correlating with k-means shows the two produce similar
partitions. It does not show AMG is *computing* intensity clustering. Two
methods can agree because CT anatomy is genuinely intensity-separable.

**Evidence that shuts it.** E3, the double dissociation: an intensity remap
that freezes edges versus a texture shuffle that freezes local mean intensity.
Both arms carry enforced validity checks, and the code refuses to emit a number
when a check fails. This is the residual obligation, verbatim: *"Must earn
mechanistic via intensity vs texture counterfactuals; else evaluation note."*

### A3. "k-means is one of many cheap baselines"

**The attack.** Beating chance is not the bar. If AMG merely agrees with
*something* cheap, the claim is empty.

**Evidence that shuts it.** Multi-Otsu and GMM as intensity-family controls,
and **SLIC as the discriminative spatial baseline**. The clusterers must beat
*superpixels*, not merely correlate with AMG. `cardinality_ratio` is reported so
nobody can claim the win is a mask-counting artifact.

### A4. "Metric shopping"

**The attack.** Pick the agreement metric that flatters the hypothesis.

**Evidence that shuts it.** Three metrics pre-registered — Hungarian IoU, ARI,
boundary-F — all reported on every card. The code has no "best metric" helper,
and `run_smoke.py` prints all three verdicts side by side including the ones
that disagree. Metric-selection discipline is anchored to Metrics Reloaded
(Nature Methods 2024, **VERIFIED PRIOR WORK**) — the same paper that killed the
sibling idea `F-022`, which is a standing reminder of the cost of getting this
wrong.

### A5. "'SAM is bad on CT' is already known"

**The attack.** arXiv 2408.11210 and arXiv 2408.04212 (**VERIFIED PRIOR WORK**)
already report CT weakness and window sensitivity.

**Evidence that shuts it.** Framing discipline. The paper ships **mechanism**,
not Dice tables, and must never claim CT weakness as a finding. `proposal.md`
§8 and §23 bind this; the closest-work table in §9 states for each paper why it
does not pre-empt us. If the paper ends up arguing "SAM is bad on CT", it has
already failed review.

### A6. "Hyperparameter brittleness"

**The attack.** One AMG setting is a lucky draw.

**Evidence that shuts it.** E2 sweeps `points_per_side` ∈ {16, 32} crossed with
k ∈ {8, 16, 32}. H3 requires the effect on ≥2 settings.

---

## B. The downgrade attack — the one that decides what this paper *is*

### B1. "This is an evaluation note, not a mechanistic finding"

**This is the highest-probability outcome, not a hypothetical.** It is written
into the Stage-4 record as the explicit failure mode: *"…else evaluation note."*
A reviewer will apply it the moment E3 is weak, and they will be right to.

**What triggers it.**
- E3 shows \(s_{\mathrm{int}} \approx s_{\mathrm{tex}}\) — no dissociation.
- Or E3 is not run at all.
- Or the dissociation appears on one window and one AMG setting only.

**What answering it requires.** A **clean** dissociation: the intensity arm
moving AMG substantially more than the texture arm, on ≥2 windows and ≥2 AMG
settings, with both validity gates passing. Nothing weaker converts a
correlation into a mechanism, and nothing weaker should be submitted as one.

**Standing conflict that must be resolved before writing (FACT).** The record
gives two incompatible instructions for this contingency:

| Source | Instruction |
|---|---|
| `stage4_reviewer2_cheap5.jsonl` | *"else evaluation note"* — **downgrade** |
| This file, original version | *"If we cannot run the causal arm, do not submit."* — **withhold** |

`stage6_battle.md` §4.4 logged this as unresolved. It decides whether a failed
H2 yields a shorter paper or no paper. **Settle it before writing.** This file
does not settle it unilaterally, because the Stage-4 record outranks a package
note and the package note is the stricter reading — the disagreement is real
and belongs to the supervisor.

### B2. "You have proven a definitional property"

**The attack.** Of course a segmenter on a single-channel calibrated modality
agrees with intensity clustering — CT *is* intensity. The finding is true by
construction.

**Why it is dangerous.** This is precisely the attack that **killed the sibling
idea `F-022`**: *"Near-definitional Dice property; Metrics Reloaded; no
leaderboard preds."* The same reviewer reflex applies here.

**Evidence that shuts it.** The **SLIC baseline** and the **COCO control**
(E4). If the result were definitional, a spatial superpixel method on the same
single-channel input would agree equally well — it does not, or H1 fails. And
if AMG behaved this way on natural images too, the claim would not be about CT
at all, which is why E4 can kill the CT-specificity claim outright.

---

## C. Our own red team (anticipated next-round attacks)

### C1. "Your texture shuffle is just adding noise"

Permuting a residual raises high-frequency energy, and any region-growing
method fragments under noise for reasons unrelated to objectness. **Answer:**
sweep `shuffle_tile` ∈ {4, 8, 16}; if the H2 direction flips with tile size the
arm is measuring tile size and the result is void (pre-declared in E3). Report
the tile sweep whatever it shows. **This attack is only partly mitigated** —
matched high-frequency energy between the two arms would be a stronger design
and is not currently specified.

### C2. "AMG returns nested masks; your matching is ill-posed"

AMG produces overlapping, nested masks; clusterers produce partitions. Matching
one to the other is not obviously well defined. **Answer:** Hungarian one-to-one
normalised by `min(|A|,|B|)` for match quality, `coverage_iou` for the
directional many-to-one question, and `cardinality_ratio` reported explicitly so
the mismatch is visible rather than absorbed. `proposal.md` §15 states why
normalising by `|A|` was wrong.

### C3. "Slice selection favours the hypothesis"

**Answer:** the slice list is pre-registered before E1 (cross-cutting rule 1).
If it is not, every later card is confirmation.

### C4. "Frozen SAM only — fine-tuned models may differ"

**Answer:** honest scope. The title names SAM ViT-B unless E5 shows SAM2 agrees.
MedSAM-family adaptation (arXiv 2408.03322, arXiv 2504.02008, **VERIFIED PRIOR
WORK**) is context, not subject; §23 puts it out of scope.

### C5. "100 slices is small"

**Answer:** per-slice paired comparison with bootstrap CI over slices, and the
H1 verdict requires the same direction on three metrics across two windows and
two AMG settings — a conjunction that is much harder to hit by chance than a
single significance test on a larger n. If CIs are still wide after E2, raise n
before raising claims.

### C6. "You are re-deriving HQ-SAM's point"

**Answer:** no. HQ-SAM (NeurIPS 2023, arXiv 2306.01567) and SAMRefiner
(arXiv 2502.06756) are **VERIFIED PRIOR WORK** on mask-quality refinement, and
`literature.md` carries the standing constraint *"we do not claim filter=HQ"*.
That framing belonged to the adjacent `F-012`, which `stage2_ABCF_summary.md`
explicitly forbids restating.

### C7. "Boundary-F will agree trivially"

Both families place edges at high-gradient locations, so boundary-F may be the
least discriminative of the three metrics. **Answer:** predicted in advance
(`proposal.md` §19) and reported anyway. A pre-registered metric that turns out
uninformative is reported as uninformative, not dropped.

---

## Standing discipline

1. Never claim "SAM is bad on CT". That is known and is not this paper.
2. Never report a subset of the three metrics.
3. Never report a number from an arm whose validity gate failed.
4. Never relabel EXPECTED as ACTUAL. Windows6 has zero ACTUAL RESULTS.
5. If E3 does not deliver a clean dissociation, resolve B1's standing conflict
   **before** deciding what to write.
