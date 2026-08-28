# exp_10 — A-0100 + A-0090: smoke/fire provenance leakage audit + time-to-detect as the constructive layer

**ID:** W2-A-0100 (host) + W2-A-0090 (merged evaluation layer, per L revive #5 and F's own request: "revive as the evaluation layer for any C04 keep").
**Pipeline status:** A-0100: F keep (cheap-falsify) → J SURVIVE-IF-EXPERIMENT (applications/dataset-track honesty caveat). A-0090: F tier-2 → L revive as merged arm. PI mandate: medical/safety diversity slot.

## Research question

(1) How much of reported smoke/fire detection performance is same-event train/test leakage (provenance audit)? (2) Once leakage-corrected, does the field's frame-wise formulation itself mismeasure the deployment task — i.e., does a time-to-detect (TTD) metric on ignition-anchored video reorder methods and reveal that simple temporal accumulation beats frame-wise segmentation in the sub-visible regime?

## Falsifiable hypothesis

H1 (audit): event-level dedup/re-splitting of public smoke/fire benchmarks reduces reported scores materially and reorders methods beyond bootstrap noise, with larger drops for higher-capacity models.
H2 (TTD): at matched false-alarm rates on ignition-timestamped fixed-camera video, long-horizon temporal accumulation detects smoke earlier than frame-wise segmentation SOTA.
Falsified if: (H1) leakage prevalence is low and rankings are bootstrap-stable across the dedup-threshold sweep; (H2) frame-wise models match or beat accumulation on detection latency at equal FAR.

## Prediction

HYPOTHESIS: scraped-video benchmarks contain non-trivial same-event contamination (the mechanism — frames of one event in both splits — is structurally likely for scraped corpora, but prevalence is unmeasured; J: "nobody has verified; that IS the paper"). H2 direction is plausible (background modeling integrates sub-visible signal) but genuinely uncertain — this is the merged paper's discovery arm.

## Method sketch (modules / dataflow)

**Audit leg (A-0100):** (1) provenance clusterer: perceptual hash + temporal-correlation + embedding clustering (CLIP/DINO cluster-split fixes are KNOWN antipatterns fixes — IEEE Access 2024 doi:10.1109/access.2024.3383047, arXiv:2511.13944 — cited as method, not novelty); (2) **threshold-sweep integrity lock** (J-mandated): performance drop as a *function* of dedup aggressiveness with manual verification of random cluster samples at each threshold — no single dialable headline number; (3) re-evaluation of public checkpoints on clean event-level splits; (4) pre-registered bootstrap ranking-stability test.
**TTD leg (A-0090):** (5) ignition-anchored evaluation set: fixed-camera videos with ignition timestamps (controlled burns, tower cameras — public sources; curation gate below); (6) TTD metric layer: detection-latency vs FAR curves (TTD-ROC), scored on model *outputs* — no retraining; (7) accumulation baseline: classical long-horizon background modeling; (8) frame-wise SOTA arm: public smoke segmentation/detection models scored under the same TTD layer.

## Data

4 public smoke/fire benchmarks (audit leg); ignition-timestamped fixed-camera video from public controlled-burn/tower-camera sources (TTD leg). Curation gate: if <~30 usable ignition-anchored sequences can be assembled, the TTD leg reports on what exists and states the power limit plainly.

## Baselines

Audit: original-split scores (the published numbers being audited). TTD: accumulation vs 3+ public frame-wise models; a hybrid (frame-wise scores accumulated over time) as the obvious defense a reviewer will propose — include it, since if the hybrid wins, the constructive recommendation changes from "different models" to "different aggregation".

## Metrics

Audit: leakage prevalence per dataset (verified-cluster fraction), score drop vs threshold curves, ranking-flip rate with bootstrap CIs. TTD: median detection latency at fixed FAR, TTD-ROC AUC, per-sequence earliness distributions.

## Killer Experiment

**The audit leg on 4 datasets with the threshold-sweep + bootstrap locks (2 GPU-days + curation), immediately followed by the TTD re-scoring of existing model outputs (days, no training).** The two legs share re-evaluation infrastructure; together they convert a debunk into debunk + constructive metric proposal — the audit-to-artifact conversion L's Finding 3 demanded.

## GPU/VRAM/time estimate

**~2 GPU-days re-evaluation (single 16–24GB GPU) + ~2–3 weeks part-time curation/verification.** TTD leg adds inference over video: ~2–4 GPU-days. No training anywhere. Total ≤1.5 GPU-weeks, curation-dominated.

## Stop / pivot / kill criteria

- **Audit null:** low prevalence + stable rankings → publish the short negative note (benchmarks are cleaner than feared — procurement-relevant) and let the TTD leg stand alone as the metric proposal (it does not depend on H1).
- **TTD kill:** if accumulation does not beat frame-wise at any FAR, H2 dies; the TTD metric layer still ships as the evaluation artifact (the metric's value does not require the accumulation result).
- **Curation stop:** if ignition-anchored data cannot reach minimal power, freeze the TTD leg as a protocol paper appendix and ship the audit alone.

## Reviewer-2 leftover

J's honesty caveat stands: this is an applications/dataset-track paper — its value is speed, certainty, and safety relevance, not main-track novelty; do not let venue inflation creep back. The dedup over-merge risk (distinct-but-similar events) is bounded by the sweep + manual verification but never eliminated; the TTD leg's fixed-camera assumption (A's own risk note) restricts the deployment claim — say so.

## Expected result (HYPOTHESIZED, not measured)

Material leakage in at least some of the 4 datasets with capacity-correlated drops; TTD reordering with accumulation winning in the sub-visible regime and losing after plume establishment.

## Negative-result interpretation

Both nulls together would be a genuinely reassuring result for the safety-procurement audience (benchmarks honest, formulation adequate) — publishable in a domain venue and cheap. The merged design guarantees at least one shipping artifact (event-level splits + TTD evaluation code) regardless of outcomes, which is why the merge dominates either idea alone.
