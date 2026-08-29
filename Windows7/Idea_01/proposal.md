# Idea_01 — SupportAudit: Wrong-Support Counterfactual Audit of Few-Shot Segmentation

**Internal ID:** B-0121 (Cluster B, PROTECTED through Stage 2–4)
**Window:** Windows7 · **Package written:** 2026-08-29
**Status:** Ready to start. Zero training. ~5 A100-days full program.

> **Epistemic contract for this file.** Every quantitative statement is tagged. `KNOWN FACT` =
> checkable property of a public artifact. `EVIDENCE` = a finding reported by a cited paper.
> `HYPOTHESIS` / `EXPECTED` = our prediction, not measured. `ACTUAL RESULT` appears **nowhere in
> this file**, because we have not run anything yet. No benchmark number below was produced by us.

---

## 1. Executive Summary

**One sentence.** Feed few-shot segmentation methods a support image of the *wrong class* and
measure how much of their reported accuracy survives — per method, per benchmark, and per
query-complexity stratum — against a support-free objectness floor.

**Abstract.** Few-shot segmentation (FSS) reports accuracy under the assumption that a method's
mIoU reflects its ability to transfer information from a labelled support image to an unlabelled
query. That assumption has never been measured directly. We run the counterfactual the field
skipped: for each episode, we replace the correct-class support with supports drawn from classes
verified absent from the query, holding support-mask area approximately fixed, and we compute
**retention** = IoU_wrong / IoU_correct. Retention is a *within-method ratio*, so it is immune to
the absolute-number irreproducibility that plagues cross-paper FSS comparison. We stratify every
number by query complexity (single- vs multi-object, distractor-present vs absent), because a
method can score well on wrong supports either because it ignores the support (a model property)
or because the benchmark's queries contain exactly one salient object (a benchmark property) —
these are different indictments and the field currently cannot tell them apart. We anchor
everything to a **support-free objectness floor** (SAM automatic mask generation; plus a classical
salient-object detector as a second, weaker floor), so that "this method uses its support" becomes
a falsifiable claim rather than an assumption. Deliverables: a support-sensitivity score per
method, a sensitivity-adjusted leaderboard, and a released distractor-enriched evaluation split
with fixed episode and wrong-support lists.

**Why this is the #1 pick of Windows7.** Every outcome branch publishes, the whole program is
inference-only, and the decision costs about two A100-days.

---

## 2. Research Motivation

FSS methods are evaluated by mIoU on PASCAL-5i and COCO-20i. A high number is read as "the method
learned to segment a novel class from one example." But the query images in these benchmarks are
natural photographs, and natural photographs have salient foreground objects. A class-agnostic
saliency prior — "segment the big thing in the middle" — scores non-trivially on such benchmarks
*without reading the support at all*.

The field already behaves as if it half-knows this. `EVIDENCE` A mitigation literature exists
specifically to counteract base-class and foreground bias: BAM (CVPR 2022 Oral) is built around
base-class bias; TBS (AAAI 2024) and AENet (ECCV 2024) target the same family of failure
[inherited from Stage 3/4 ledger]. Support-dilution work (`arXiv:2501.13529`) and SADe
(`arXiv:2607.24706`) continue the line [verified-abstract at Stage 6]. These papers exist *because*
practitioners believe support quality matters. Nobody has measured how much accuracy survives the
support's total destruction.

`EVIDENCE` A second, independent validity problem surfaced during Stage 6: an unrelated group
reported that FSS numbers can shift by up to 37 points through preprocessing-space mismatch
between repositories (Open-V line, recorded as X2 in `stage6_defense_brief.md`). That finding makes
absolute FSS numbers untrustworthy across papers — and makes a *ratio* statistic like retention
strictly more valuable than it looked at Stage 5.

The motivating question is therefore not "is FSS good?" but: **how much of the FSS leaderboard is a
saliency prior wearing a support-conditioned costume, and does correcting for it reorder the
ranking?**

---

## 3. Problem Definition

Let a method be a function `f(S, Q) → M̂`, where the support `S = (I_s, M_s)` is an image and its
binary mask for class `c`, and `Q = I_q` is the query image. The benchmark scores
`IoU(M̂, M_q^c)` against the query's ground-truth mask for class `c`.

Define, for a fixed episode `(S, Q)` and a set `W(Q)` of wrong-class supports whose classes are
verified absent from `Q`:

- **Correct-support accuracy:** `a_corr = IoU(f(S, Q), M_q^c)`
- **Wrong-support accuracy:** `a_wrong = median_{S' ∈ W(Q)} IoU(f(S', Q), M_q^c)`
- **Retention:** `R = a_wrong / a_corr`, computed only on episodes where `a_corr ≥ τ` (τ
  pre-registered; see §21 attack A4)
- **Insensitivity:** `V = median_{S'} IoU(f(S', Q), f(S, Q))` — agreement between the two
  *predictions*, independent of ground truth
- **Support-sensitivity score:** `SSS = 1 − R`
- **Support-free floor:** `a_floor = IoU(g(Q), M_q^c)` for a support-free objectness model `g`

The problem is to estimate `R`, `V`, and `a_corr − a_floor` for a panel of published methods,
stratified by query complexity, with confidence intervals, and to determine whether ranking methods
by `SSS` or by `a_corr` restricted to the distractor-present stratum reorders the published
leaderboard.

**Stratification (pre-registered, computable from benchmark instance annotations):**

| Stratum | Definition |
|---|---|
| `S1` single-object | query contains exactly one annotated instance of any class |
| `S2` multi-object same-class | ≥2 instances, all of class `c` |
| `S3` distractor-present | ≥1 annotated instance of a class ≠ `c` **(PRIMARY stratum)** |
| `S4` degenerate control | FSS-1000 episodes (single centred object by construction) |

`S3` is the primary stratum because it is the only one where "segment the salient thing" and
"segment the class the support names" can disagree.

---

## 4. Core Hypothesis

> **H1.** A substantial share of reported FSS accuracy on standard benchmarks is produced by a
> class-blind foreground/saliency prior rather than by use of the support.
>
> **H2.** The share differs systematically between architecture families: specialist meta-learners
> (PFENet / HSNet / BAM era) retain more accuracy under wrong supports than training-free
> foundation matchers (Matcher, PerSAM, SegGPT, FSSAM, SAM3-exemplar), because the latter match
> support features explicitly.
>
> **H3.** Retention is highest on single-salient-object queries, i.e. part of what looks like model
> insensitivity is benchmark degeneracy, and the two are separable by stratification.

---

## 5. Falsifiable Prediction (pre-registered)

**P1 (primary).** On the `S3` distractor-present stratum of COCO-20i / LVIS-92i, at least half of
the audited specialist methods retain `R > 0.5` under wrong-class supports.

**P2 (family separation).** Specialist-vs-foundation retention on `S3` differs by more than 15
percentage points, in the direction specialists > foundation.

**P3 (floor test).** For at least one audited method, correct-support accuracy on `S3` is
statistically indistinguishable (95% bootstrap CI overlap) from the support-free objectness floor.

**Falsification condition.** If all audited methods show `R < 0.2` on every stratum *including*
PASCAL single-object, H1 is refuted: FSS methods collapse appropriately when the support is wrong,
the field's validity is certified, and we publish the certification (see §20).

---

## 6. Key Insight

Three ideas do the work, and none of them is a new module.

1. **The counterfactual is on the input, not the model.** We do not probe, ablate, or retrain
   anything. We change one input — the support — in a controlled way and read the output. This is
   why the design survives a genuine Reviewer #2 round: there is no architecture to attack.

2. **Retention is a ratio, so it is reproducibility-proof.** `EVIDENCE` Cross-repo FSS numbers are
   unreliable (X2, §2). A ratio computed inside one method's own pinned harness does not depend on
   reproducing anyone's published absolute number. This is the single most under-appreciated
   property of the design and it is now the paper's defensive core.

3. **Stratification separates two indictments that look identical.** High retention on a benchmark
   whose queries have one object indicts *the benchmark*. High retention on distractor-present
   queries indicts *the model*. Every prior discussion of foreground bias conflates them; the
   `S3`-primary design does not.

---

## 7. Novelty — exact difference from closest prior work

| Closest prior | What it actually did | Our exact difference |
|---|---|---|
| BAM, CVPR 2022 Oral (`chunbolang/BAM`) | Identifies base-class bias; proposes a base-learner to suppress it. Measures the *fix*. | We never propose a fix. We measure the size of the residual support-independent share across a whole panel, with a floor and strata. |
| TBS (AAAI 2024), AENet (ECCV 2024) [inherited] | Mitigation methods for foreground/background bias. | Same: they are treatments; we are the diagnostic assay that says how much disease there is. |
| Support-dilution (`arXiv:2501.13529`), SADe (`arXiv:2607.24706`) [verified-abstract] | Degrade/perturb support quality to improve robustness or propose new modules. | They perturb support to *build* something. We destroy support entirely to *measure* something, with a support-free floor as the null model. |
| Open-V line (X2, Stage 6) | Reports that FSS numbers shift up to 37 pts under preprocessing mismatch; observes support contribution grows as text priors weaken. | Corroborates our premise from the opposite direction. We turn their confound into a per-method discrepancy table (§15, second headline). |

**Remaining novelty (confidence: high).** `KNOWN FACT` As of the Stage-4 and Stage-6 adversarial
sweeps, no published work reports a wrong-class-support counterfactual audit of an FSS method panel
with (a) a support-free objectness floor and (b) query-complexity stratification. The
mitigation literature is dense; the measurement is empty.

**What a reviewer will cite to attack us:** BAM and the 2024 mitigation wave, arguing "foreground
bias is known." Answer in §21/§22.

---

## 8. Proposed Method

This is an audit protocol, not a model. The "method" is the measurement apparatus.

### 8.1 Support injection

For each method `f` in the panel we write a thin wrapper that exposes a single hook: replace the
episode's support pair `(I_s, M_s)` with an arbitrary provided pair, leaving every other code path
— preprocessing, resizing, normalisation, inference, post-processing — untouched. `KNOWN FACT`
Each repository already constructs episodes internally; the wrapper intercepts at the episode
level, so per-repo preprocessing differences are preserved rather than papered over. This is
deliberate: preserving them is what makes the §15 discrepancy table possible.

### 8.2 Wrong-support sampling (pre-registered, fixed lists)

For query `Q` with class `c`:

1. Compute `A(Q)` = set of classes annotated present in `Q`.
2. Candidate wrong classes = `fold_classes \ ({c} ∪ A(Q))`.
3. Split candidates into **near** (same WordNet/COCO supercategory as `c`, e.g. cat→dog) and
   **far** (different supercategory, e.g. cat→airplane). Draw `K = 5` wrong supports: 2 near, 3
   far, fixed by seed and **shipped as a static list**, not regenerated from a seed at run time.
4. Support-mask area matching: accept a wrong support only if its mask area is within ±50% of the
   correct support's area (relative to image area). If fewer than `K` candidates qualify, relax to
   ±100% and record the relaxation per episode.

Fixed lists (not seeds) are required so that another group can reproduce the exact counterfactual.

### 8.3 Support-free objectness floors

- **Floor-A (strong):** SAM automatic mask generation; select the mask with the largest area among
  those whose centroid lies within the central 50% of the image. `KNOWN FACT` SAM AMG is a strong
  class-agnostic segmenter, so Floor-A is a *conservative* (hard-to-beat) null.
- **Floor-B (weak):** a classical salient-object detector.

Both floors are pre-registered and every floor-dependent claim is reported against **both**. This
is the Stage-6 mandatory condition (attack A2, §21).

### 8.4 Sensitivity-adjusted leaderboard

Rank methods by (i) `SSS` on `S3`, and (ii) `a_corr` restricted to `S3`. Report Kendall τ between
each and the published ordering. Release `S3` as a fixed **distractor-enriched split** with the
episode list, wrong-support list, and both floors' predictions.

---

## 9. Architecture Diagram

See `diagrams/architecture.md` (Mermaid source, renders on GitHub) and
`diagrams/protocol_flow.md` for the episode-level data flow. Inline summary:

```
episode (S,Q) ──┬─► f(S ,Q) ─► a_corr ─┐
                │                       ├─► R = a_wrong/a_corr ─► SSS ─► adjusted leaderboard
                ├─► f(S',Q) ─► a_wrong ─┘        (stratified by S1..S4)
                │   S' ∈ fixed wrong-support list (2 near + 3 far, area-matched)
                └─► g(Q)    ─► a_floor  ─► floor test (Floor-A strong / Floor-B weak)
```

---

## 10. Mathematical Formulation

No training objective exists. The estimands and their uncertainty:

**Per-episode retention.** For episode `e` with `a_corr(e) ≥ τ`:

```
R(e) = median_{S' ∈ W(e)} IoU(f(S', Q_e), M_e) / IoU(f(S_e, Q_e), M_e)
```

**Stratum-level retention (PRIMARY estimator — ratio of means).** For method `m`, benchmark `b`,
stratum `s`, with episode-level bootstrap (B = 10,000 resamples, numerator and denominator
resampled on the *same* episode indices):

```
R̂(m, b, s) = Σ_{e ∈ E(b,s)} a_wrong(e)  /  Σ_{e ∈ E(b,s)} a_corr(e)
```

> **Design correction, found while building the prototype (2026-08-29).** The Stage-5 design
> specified the stratum statistic as the *median of per-episode ratios*. Running the harness against
> the `MockSegmenter` controls showed why that is wrong: the per-episode retention distribution is
> strongly **bimodal**. Under a wrong support a method either lands on the correct object or it does
> not, so `R(e)` piles up near 0 and near 1 with almost no mass between. A median over that
> distribution is a coin flip on which pile is larger — it reports exactly 1.000 or exactly 0.000 and
> jumps discontinuously when one episode changes side. In the harness run, the fully support-driven
> control scored a median retention of 1.000 (indistinguishable from a support-blind method) while
> its ratio of means was 0.762 [0.651, 0.871]. Had we kept the median, the killer experiment would
> have been unable to detect the very behaviour it exists to detect. The ratio of means is stable,
> bootstraps cleanly, and carries the interpretation the paper actually wants: *what share of
> accuracy survives destroying the support*.
>
> The median of per-episode ratios is still computed and reported as a **secondary robust
> statistic**, and a large gap between the two is flagged, because a bimodal split is itself a
> finding: it says the method has a hard failure mode rather than graceful degradation.

**Support-sensitivity score.** `SSS(m, b, s) = 1 − R̂(m, b, s)`.

**Floor test.** Let `Δ(m,s) = a_corr(m,s) − a_floor(s)`. Method `m` fails the floor test in
stratum `s` iff the 95% bootstrap CI of `Δ(m,s)` contains 0.

**Leaderboard reordering.** With published ordering `π₀` and adjusted ordering `π₁`, report
Kendall `τ(π₀, π₁)` and the number of position changes. Pre-registered claim of "reordering" =
τ < 0.8 **and** ≥3 position changes among the top 8.

**Power.** `HYPOTHESIS` With 1,000 episodes per fold × 4 folds and a per-episode retention SD
assumed ≈0.3, the stratum-level median is resolved to roughly ±0.02 at 95%; the `S3` stratum on
PASCAL-5i is the thin one and may need COCO/LVIS to carry it. Per-stratum episode counts are
reported before any inferential claim (§21 attack A5).

---

## 11. Implementation

`src/` contains a runnable minimal prototype of the core innovation — the counterfactual harness,
the strata assignment, the floors, and the statistics — with a mock segmenter so the whole pipeline
executes on a laptop with no checkpoints. Real method wrappers are thin adapters against the
public repos listed in §11.2.

```
src/
  support_audit/
    __init__.py
    episodes.py      # episode construction, strata assignment (S1..S4)
    counterfactual.py# wrong-support sampling: near/far, area matching, FIXED LIST export
    floors.py        # Floor-A (SAM AMG) / Floor-B (saliency) interfaces + mock impls
    metrics.py       # IoU, retention, insensitivity, flip rate, SSS
    stats.py         # episode bootstrap CIs, floor test, Kendall tau leaderboard
    protocol.py      # end-to-end audit driver; method-agnostic
    adapters.py      # per-repo adapter Protocol + MockSegmenter reference impl
  run_mve.py         # the MVE driver (§17)
  make_wrong_support_lists.py  # emits the shipped static counterfactual lists
```

### 11.1 What is real vs mock

`KNOWN FACT` The code in `src/` runs end-to-end today against `MockSegmenter`, which lets us
validate the statistics, the strata logic, and the list format before any checkpoint is downloaded.
The per-repo adapters (`PFENetAdapter`, `MatcherAdapter`, …) are specified as a `Protocol` with one
method; each is expected to be tens of lines against the corresponding repo's episode API.

### 11.2 Reusable public codebases

All were existence-verified during Stage 5 (2026-08-28). `KNOWN FACT` existence-verified ≠
fitness-verified; day-1 tasks in §24 re-check and archive every checkpoint.

| Method | Repo | Note |
|---|---|---|
| PFENet | `github.com/dvlab-research/PFENet` | 8 pretrained models, both benchmarks |
| HSNet | `github.com/juhongm999/hsnet` | Google Drive checkpoints — link-rot risk |
| BAM | `github.com/chunbolang/BAM` | OneDrive checkpoints — link-rot risk |
| Matcher | `github.com/aim-uofa/Matcher` | ICLR 2024, training-free DINOv2+SAM |
| PerSAM | `github.com/ZrrSkywalker/Personalize-SAM` | training-free + 2-param variant |
| FSSAM | `github.com/Sam1224/FSSAM` | ICML 2025, SAM2-based |
| SegGPT | HuggingFace `SegGptForImageSegmentation` | in `transformers` |
| SAM / SAM2 | `facebookresearch` official checkpoints | Floor-A |
| SAM3-exemplar | official release (HF-gated) | **added at Stage 6** — see §21 A1 |

---

## 12. Dataset Plan

| Dataset | Role | Split |
|---|---|---|
| PASCAL-5i (VOC2012 + SBD) | standard FSS, thin `S3` | 4 folds × 1,000 episodes × 3 sampling seeds |
| COCO-20i (COCO 2014) | primary `S3` carrier | 4 folds × 1,000 episodes × 3 seeds |
| LVIS-92i | high multi-object density | as used by Matcher |
| FSS-1000 | `S4` degenerate control | 1,000 episodes |
| MSD / AMOS CT slices | generalisation probe (§15) | one-shot organ episodes, training-free methods only |

**Preprocessing.** Deliberately *per-repo native*, not unified — see §8.1. The shared-evaluator
comparison is run as a second pass and the difference is a reported result, not a nuisance.

**Augmentation.** None. This is an audit of released checkpoints under their own protocols.

---

## 13. Baselines

1. **Support-free objectness floor** (Floor-A strong, Floor-B weak) — the null model. This is the
   most important baseline in the paper.
2. **Random correct-class support** (a different instance of class `c`) — the benign-variation
   anchor, isolating "support changed" from "support is wrong".
3. **Blank/degenerate support** — for methods that accept it; bounds the input-format effect.
4. **Reproduced published correct-support numbers** — reproduced, never copied. Divergence from the
   paper's reported number is itself reported (§15).

---

## 14. Metrics

Retention `R`; insensitivity `V`; flip rate (`V > 0.9`); `SSS`; floor gap `Δ`; Kendall τ between
leaderboards; per-stratum episode counts; bootstrap CIs everywhere; per-method reproduction
discrepancy (ours vs published, and shared-evaluator vs native evaluator).

---

## 15. Experimental Matrix

| # | Experiment | Panel | Data | Cost | Decides |
|---|---|---|---|---|---|
| E0 | Checkpoint archival + hash | all | — | 0 GPU | feasibility |
| E1 | **MVE** | PFENet, BAM, Matcher, + FSSAM *or* SAM3-exemplar | PASCAL-5i f0, COCO-20i f0 | ~1 A100-day | go/no-go |
| E2 | Full panel × strata | 8–10 methods | PASCAL, COCO, LVIS | ~3 A100-days | P1–P3 |
| E3 | Floor battery | Floor-A, Floor-B | all | ~0.3 A100-day | P3 |
| E4 | Near/far wrong-support split | all | COCO | included in E2 | A3 defence |
| E5 | Shared vs native evaluator | all | PASCAL, COCO | ~0.5 A100-day | **second headline** |
| E6 | `S4` degenerate control | all | FSS-1000 | ~0.2 A100-day | H3 |
| E7 | Medical transfer probe | training-free only | MSD/AMOS | ~0.5 A100-day | generalisation |

**Total: ≈5 A100-days, zero training.** Hard cap 8 A100-days (§25).

---

## 16. Ablation Plan

- Wrong-support similarity: near-class vs far-class.
- Support-mask area matching on / off.
- `K = 1` vs `K = 5` wrong draws.
- 1-shot vs 5-shot; **mixed supports** (4 correct + 1 wrong) → dose–response in the support set.
- Episode filter threshold `τ ∈ {0.1, 0.2, 0.3}` — reported as a sensitivity curve, because τ is
  the design's main analyst degree of freedom (§21 A4).
- Floor choice: every floor-dependent conclusion reported under Floor-A and Floor-B.

---

## 17. Killer Experiment

> **The stratified wrong-support counterfactual with support-free floor.**
>
> On the pre-registered `S3` distractor-present stratum:
> **(a)** ≥ half of specialist methods retain `R > 0.5` under wrong-class supports, **and**
> **(b)** their correct-support accuracy on `S3` is statistically indistinguishable (95% bootstrap
> CI overlap) from the support-free objectness floor — **reported separately for Floor-A and
> Floor-B**.
>
> If (a) and (b) both fail — methods collapse under wrong supports *and* beat both floors — the
> headline claim is dead and the certification result (§20) is published instead.
>
> **Cost of the killer alone: ~2 A100-days.**

**MVE gate before the killer (~1 A100-day):** PFENet + BAM + Matcher + one foundation-era method on
PASCAL-5i fold 0 and COCO-20i fold 0.
*Go* if any method retains `R > 0.35` on any stratum, or specialist-vs-foundation retention differs
by >15 points.
*No-go* if all retentions `< 0.2` everywhere including PASCAL single-object.

---

## 18. Expected Results

**All numbers below are `EXPECTED` / `HYPOTHESIZED`. None has been measured.**

| Quantity | Expected |
|---|---|
| Specialist retention, PASCAL-5i `S1` | 0.40 – 0.60 |
| Specialist retention, COCO `S3` | 0.20 – 0.40 |
| Foundation-matcher retention, COCO `S3` | 0.10 – 0.30 |
| FSS-1000 (`S4`) retention, all methods | high (benchmark degeneracy, not model property) |
| Leaderboard positions changed (top 8) | ≥ 3 |
| Floor test failures | ≥ 1 method on `S3` under Floor-B; fewer under Floor-A |

`HYPOTHESIS` The direction we most expect to be wrong about is P2: SAM3-exemplar and other
foundation-era methods may retain *more* than we predict if their objectness prior dominates their
exemplar conditioning. That would be a more interesting result than our prediction, not a failure.

---

## 19. Failure Cases

- **Checkpoint link rot** (BAM OneDrive, HSNet Google Drive) — the #1 practical risk. Mitigation:
  day-1 archival (§24, E0).
- **Thin `S3` on PASCAL-5i** — mitigated by COCO/LVIS carrying the primary stratum; per-stratum
  counts published before inference.
- **Unstable retention when `a_corr` is small** — mitigated by the pre-registered `τ` filter plus
  the τ sensitivity curve.
- **Wrong-support non-exchangeability** — "classes absent from Q" correlates with query content
  through co-occurrence structure. Mitigated by fixed per-fold wrong-class pools and the near/far
  split promoted from ablation into the main design.

---

## 20. Negative Results — what a failure means

**If everything collapses (`R < 0.2` everywhere).** The field's validity is *certified* by the
first counterfactual audit ever run on it. We publish the certification plus the stratified
protocol and the distractor-enriched split. `HYPOTHESIS` Stage 6 flagged an honest disagreement
here: the attack pass argued this branch may be workshop-grade rather than top-venue. We price it
that way rather than pretending otherwise — but it costs 5 A100-days to find out, and the split and
harness survive either way.

**If retention is high only where benchmarks are degenerate (`S4` high, `S3` low).** The
indictment moves from models to benchmarks. The distractor-enriched split becomes the main
deliverable and the paper becomes a benchmark paper.

**If retention is high on `S3` too.** H1 confirmed; the sensitivity-adjusted leaderboard is the
headline.

---

## 21. Reviewer #2 Attack

Recorded from `stage4_cluster_B_attacks.md` and `stage6_attack_brief.md`, with the Stage-6
mandatory conditions folded in.

| # | Attack | Severity |
|---|---|---|
| **A1** | *"Post-SAM3, auditing PFENet/HSNet/BAM indicts a museum."* SAM3 (Nov 2025) does exemplar-prompted concept segmentation; image exemplars **are** supports. A specialist-centric audit is archaeology. | High — reframing |
| **A2** | *"Leg (b) is hostage to the floor."* SAM AMG is a very strong floor; a weak classical SOD floor could flip the verdict on identical data. "Fully accounted for by the prior" then depends on which prior you granted. | High |
| **A3** | *"Wrong-class supports are not exchangeable."* Available wrong classes correlate with query content; ±50% area matching is loose. Stratum differences could be sampling artifacts. | Medium |
| **A4** | *"Retention is unstable and `τ` is an analyst degree of freedom."* | Medium |
| **A5** | *"Per-repo protocol differences make the panel incomparable."* | Medium |
| **A6** | *"Foreground bias is known (BAM, TBS, AENet). What is new?"* | Medium — framing |
| **A7** | *"The certification branch is a workshop note, not a paper."* | Open — honestly unresolved |

---

## 22. Response Strategy — the experiment that shuts each attack down

| # | Response | Where it lives |
|---|---|---|
| **A1** | **Add a SAM3-exemplar arm and make foundation-era retention the co-headline.** Cost: one HF-gated checkpoint, inside the existing budget. The specialists become the historical control, not the headline. | E1, E2 |
| **A2** | **Pre-register both floors and report leg (b) against each.** A conclusion that holds under the strong Floor-A is unattackable; one that holds only under Floor-B is reported as such. The attack is answered by refusing to pick. | E3, §8.3 |
| **A3** | **Ship fixed wrong-support lists** (not seeds) with a near/far split promoted into the main design, plus per-episode logging of area-matching relaxations. Near-vs-far retention difference is itself a reported result. | E4, §8.2 |
| **A4** | **Pre-register `τ`, publish the τ-sensitivity curve** across {0.1, 0.2, 0.3}. If the conclusion moves with τ, we say so. | §16 |
| **A5** | **Run both native and shared evaluators and publish the discrepancy table.** This converts the attack into the paper's *second headline* (§15 E5), corroborating the X2 preprocessing finding on our own panel. | E5 |
| **A6** | Position on the measurement/treatment distinction (§7): the mitigation literature is the *motivation*, and the deliverable is the assay + adjusted leaderboard + released split. | §7 |
| **A7** | No experiment fixes this; it is a venue judgement. We price the certification branch as the weakest outcome, and note the split + harness are artifacts regardless. Recorded as an accepted risk, not defended away. | §20 |

---

## 23. Compute Plan

`KNOWN FACT` Inference only. Zero training. Zero annotation.

- ~8–10 methods × 2–3 benchmarks × 4 folds × 1,000 episodes × 6 support conditions (1 correct +
  5 wrong) ≈ 500k forward passes.
- At 0.3–1 s per pass → **≈5 A100-days** including strata, both floors, and 3 episode-sampling
  seeds.
- Peak VRAM: fits a single 40 GB A100; SegGPT and SAM2/SAM3-based methods are the heaviest.
- Engineering: ~8 small support-injection wrappers.
- Hard cap: 8 A100-days.

---

## 24. Implementation Roadmap

**Day 1 — E0, the gate that protects everything.** Download and SHA-256 every checkpoint
(BAM/OneDrive and HSNet/Google Drive first — highest rot risk); mirror to internal storage; record
hashes in `references/checkpoint_manifest.md`. Request SAM3 HF access. *If a checkpoint is
unobtainable, the panel shrinks and we say so — we do not silently substitute.*

**Day 2–3.** Support-injection wrappers for PFENet, BAM, Matcher. Generate and freeze the wrong-
support lists (`make_wrong_support_lists.py`). Assign strata from instance annotations. Commit the
pre-registration artifact (frozen strata definitions, `τ`, `K`, floors, decision rule) **before**
running anything.

**Day 3–5 — E1 MVE.** ~1 A100-day. Go/no-go.

**Week 2 — E2/E3/E4.** Full panel, all strata, both floors, near/far split.

**Week 3 — E5/E6/E7.** Evaluator discrepancy table, FSS-1000 control, medical probe. Release the
distractor-enriched split.

**Week 4.** Sensitivity-adjusted leaderboard; paper draft; artifact packaging.

---

## 25. Stop / Continue Criteria

**Continue** if the MVE go-condition fires (any method `R > 0.35` on any stratum, or ≥15-point
family separation).

**Pivot to benchmark paper** if `S4` retention is high but `S3` retention is low — the deliverable
becomes the distractor-enriched split.

**Pivot to certification note** if all retentions `< 0.2` everywhere *including* PASCAL `S1` and
the COCO `S3` stratum.

**Kill** if E0 cannot assemble ≥4 methods with verified checkpoints (the panel is too thin for a
leaderboard claim) — release the harness and stop.

**Hard cap:** 8 A100-days. The audit ships with whatever methods ran.

---

## 26. Possible Extensions

- **Medical FSS audit.** The `S3` logic transfers directly to one-shot organ segmentation; CT
  queries are *less* saliency-degenerate than COCO, so retention there is a sharper test.
- **Support-sensitivity as a training signal.** If `SSS` is measurable and low, it becomes a
  regulariser target — but this is future work; adding it here would turn an audit into a method
  paper and re-expose every attack we just closed.
- **Temporal extension.** Same counterfactual for few-shot *video* object segmentation, where the
  first frame is the support.
- **Cross-pollination with Idea_02.** Both projects instrument a frozen foundation model with a
  controlled input intervention and a pre-registered null; the statistics module is shareable.

---

## 27. Paper Story

> Few-shot segmentation reports how well a model segments a novel class from one example. We
> checked whether the example matters. Feeding methods a support image of a class that is
> provably absent from the query, we find [`EXPECTED`: a large share of] reported accuracy
> survives — and on the benchmark strata where a saliency prior cannot help, the picture changes
> and the leaderboard reorders. We release a support-sensitivity score, a distractor-enriched
> evaluation split, and the fixed counterfactual lists that make the measurement reproducible.

The narrative works in all three branches because the object of study is the *evaluation*, not a
model: a high number, a low number, and a benchmark-degeneracy number are three different papers,
all of which the field needs.

---

## 28. Candidate Titles

1. *Does the Support Matter? A Wrong-Support Counterfactual Audit of Few-Shot Segmentation*
2. *Support-Independent Accuracy: How Much of Few-Shot Segmentation Is a Saliency Prior?*
3. *Segmenting the Wrong Class: Certifying (or Indicting) Few-Shot Segmentation Benchmarks*
4. *Retention: A Reproducibility-Proof Statistic for Few-Shot Segmentation*
5. *The Distractor-Present Stratum: Re-Ranking Few-Shot Segmentation Under Counterfactual Supports*

---

## Provenance

Derived from Windows7 Stage 1–6 artifacts on `songkang688/idea`:
`cursor/stage1-cluster-b-ideas-6596` → `cursor/stage2-cluster-b-scoring-9022` →
`cursor/stage3-cluster-b-priorwork-5dcc` → `cursor/stage4-cluster-b-reviewer2-b25a` →
`cursor/stage5-cluster-b-engineering-a00b` → `cursor/stage6-attack-pass-top5-cca8` /
`cursor/stage6-defense-top5-2995` / `cursor/stage6-meta-review-final3-4fc5`.
Stage-6 mandatory conditions (SAM3 arm, dual floors, fixed lists, day-1 archival) are folded into
§8, §15, §17, §22, §24 rather than appended.
