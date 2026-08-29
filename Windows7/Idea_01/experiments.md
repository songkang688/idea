# Idea_01 — Experiment Plan

All costs are inference-only on a single A100-40GB. **Total ≈5 A100-days, hard cap 8.**

---

## Pre-registration (must be committed before E1 runs)

Frozen in `configs/preregistration.yaml`:

- strata definitions `S1`–`S4` (computed from instance annotations, never from model output)
- episode filter `τ = 0.2`, with the sensitivity curve over `{0.1, 0.2, 0.3}` reported regardless
- `K = 5` wrong supports per episode: 2 near-supercategory + 3 far
- area matching tolerance ±50%, relaxed to ±100% with per-episode logging
- both floors (Floor-A SAM AMG strong, Floor-B saliency weak)
- primary statistic = **ratio of means**, secondary = median of per-episode ratios
- the killer decision rule verbatim
- the episode lists and the wrong-support lists themselves, as static files

Freezing the *lists* rather than the seeds is deliberate: a seed plus a code version is not
reproducible across library upgrades.

---

## Experiment matrix

| # | Experiment | Panel | Data | Cost | Decides |
|---|---|---|---|---|---|
| **E0** | Checkpoint archival + SHA-256 manifest | all | — | 0 GPU | feasibility gate |
| **E1** | **MVE** | PFENet, BAM, Matcher + (FSSAM or SAM3-exemplar) | PASCAL-5i f0, COCO-20i f0, 1k episodes each | ~1 A100-day | go / no-go |
| **E2** | Full panel × strata × 3 seeds | 8–10 methods | PASCAL, COCO, LVIS, all folds | ~3 A100-days | P1, P2 |
| **E3** | Floor battery | Floor-A, Floor-B | all queries | ~0.3 A100-day | P3 |
| **E4** | Near vs far wrong-support split | all | COCO | in E2 | attack A3 |
| **E5** | Native vs shared evaluator | all | PASCAL, COCO | ~0.5 A100-day | **second headline** |
| **E6** | `S4` degenerate control | all | FSS-1000 | ~0.2 A100-day | H3 |
| **E7** | Medical transfer probe | training-free only | MSD / AMOS one-shot organ episodes | ~0.5 A100-day | generalisation |

Floors are computed **once per query image** and cached across all methods (see
`src/support_audit/protocol.py`), which is where most of the saved compute comes from.

---

## E1 — the MVE gate

**Setup.** PFENet + BAM + Matcher + one foundation-era method (FSSAM, or SAM3-exemplar if access
lands in time). PASCAL-5i fold 0 and COCO-20i fold 0, 1,000 episodes each, one seed, correct vs
5 wrong supports, single stratification pass.

**Go** if either: any method retains `R > 0.35` on any stratum, **or** specialist-vs-foundation
retention differs by more than 15 points.

**No-go** if all retentions are `< 0.2` everywhere, including the PASCAL single-object stratum.
The idea dies here for about one A100-day, which is the point.

---

## E2/E3 — the killer experiment

> On the pre-registered `S3` distractor-present stratum:
> **(a)** ≥ half of specialist methods retain `R > 0.5` under wrong-class supports, **and**
> **(b)** their correct-support accuracy on `S3` is statistically indistinguishable (95% bootstrap
> CI overlap) from the support-free objectness floor, **reported separately for Floor-A and
> Floor-B**.
>
> Both legs failing ⇒ headline dead, certification result published instead.
> **Cost of the killer alone ≈2 A100-days.**

Leg (b) is never pooled across floors. Pooling would hide exactly the dependence that reviewer
attack A2 is about.

---

## Ablations

| Ablation | Why |
|---|---|
| near vs far wrong-class supports | A3: is retention an artifact of *which* wrong class? |
| area matching on / off | A3: does support size drive the effect? |
| `K = 1` vs `K = 5` | stability of the per-episode median |
| 1-shot vs 5-shot | does more support help, or more of the same prior? |
| **mixed supports** (4 correct + 1 wrong) | dose–response *inside* the support set — the sharpest version of the question |
| `τ ∈ {0.1, 0.2, 0.3}` | A4: the design's main analyst degree of freedom, published as a curve |
| Floor-A vs Floor-B | A2: every floor-dependent conclusion reported under both |

---

## Controls

1. **Support-free objectness floor** — the null model. The single most important number in the paper.
2. **Random correct-class support** (different instance, same class) — the benign-variation anchor.
   Separates "the support changed" from "the support is wrong."
3. **Blank / degenerate support**, where the method's input format permits it.
4. **Reproduced published numbers** — reproduced, never copied. Divergence is reported (E5).
5. **Harness controls** — `MockSegmenter` at `support_reliance ∈ {0, 1}` must separate before any
   real checkpoint is trusted. `KNOWN FACT` This control is what caught the median-vs-ratio-of-means
   estimator bug during prototyping (`proposal.md` §10).

---

## Robustness

- Repeat retention on FSS-1000: high retention *there* measures the benchmark, not the model.
- Verify conclusions are unchanged under each repo's official evaluator vs one shared evaluator
  (this is E5, and it is load-bearing rather than optional).
- Publish the shared episode lists so a third party can re-run the identical counterfactual.
- Report per-stratum episode counts **before** any inferential claim.

---

## Generalisation

Medical transfer probe (E7): one-shot organ episodes assembled from public abdominal CT
(MSD / AMOS slices), run through the training-free methods only (Matcher, PerSAM, SegGPT). CT
queries are far less saliency-degenerate than COCO photographs, so this is a *sharper* test of the
same hypothesis rather than a domain-transfer afterthought.

---

## Analysis and reporting

- Bootstrap over episodes (B = 10,000), numerator and denominator resampled on identical indices.
- Primary estimator = ratio of means. Secondary = median of per-episode ratios. A gap > 0.2 between
  them is flagged and reported, because bimodal per-episode retention means the method has a hard
  failure mode rather than graceful degradation.
- Leaderboard shift: Kendall τ plus count of position changes. Pre-registered "reordering" claim
  requires τ < 0.8 **and** ≥3 position changes among the top 8.

---

## Stop / continue

| Condition | Action |
|---|---|
| MVE go-condition fires | continue to E2 |
| `S4` high, `S3` low | **pivot to benchmark paper**; distractor-enriched split is the deliverable |
| all retentions `< 0.2` everywhere | **pivot to certification note** |
| E0 cannot assemble ≥4 verified checkpoints | **kill**; release the harness, publish nothing |
| 8 A100-days spent | ship with whatever methods ran |
