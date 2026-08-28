# Windows2 Stage 1 - Agent C Cluster Map

Total: **345 ideas** across 12 exclusive angle clusters. Full details in `ideas.md` / `ideas.jsonl`.

| Cluster | Theme | ID range | Count | High-ROI |
|---|---|---|---|---|
| 1 | Object detection limitations | W2-C-0001 - W2-C-0040 | 40 | 10 |
| 2 | Evaluation weakness | W2-C-0041 - W2-C-0080 | 40 | 14 |
| 3 | Unproven community assumptions | W2-C-0081 - W2-C-0115 | 35 | 5 |
| 4 | Surprising empirical phenomena | W2-C-0116 - W2-C-0145 | 30 | 6 |
| 5 | Negative results that would change practice | W2-C-0146 - W2-C-0175 | 30 | 8 |
| 6 | Robustness, calibration, uncertainty quantification | W2-C-0176 - W2-C-0200 | 25 | 7 |
| 7 | Domain shift and synthetic-to-real | W2-C-0201 - W2-C-0225 | 25 | 4 |
| 8 | SR, restoration, generation, diffusion tied to dense prediction | W2-C-0226 - W2-C-0250 | 25 | 6 |
| 9 | Long-tail, metric fairness, dataset bias | W2-C-0251 - W2-C-0280 | 30 | 10 |
| 10 | Reproducibility and compute-fair comparison | W2-C-0281 - W2-C-0305 | 25 | 9 |
| 11 | New combinations with genuine scientific motivation | W2-C-0306 - W2-C-0325 | 20 | 6 |
| 12 | Simple hypotheses that challenge accepted beliefs | W2-C-0326 - W2-C-0345 | 20 | 7 |

## Cluster 1: Object detection limitations

Structural failure modes of detectors: open-vocabulary grounding gaps, tiny objects vs annotation noise floors, crowding and suppression bottlenecks, occlusion vs truncation, video flicker and temporal aggregation, query-budget ceilings.

IDs: `W2-C-0001` - `W2-C-0040` (40 ideas). High-ROI picks: `W2-C-0001`, `W2-C-0003`, `W2-C-0007`, `W2-C-0011`, `W2-C-0012`, `W2-C-0013`, `W2-C-0020`, `W2-C-0026`, `W2-C-0032`, `W2-C-0040`.

## Cluster 2: Evaluation weakness

The measurement instruments themselves: what AP, IoU, Dice, PQ, and calibration metrics actually measure, where they are gameable, statistically underpowered, convention-dependent, or decoupled from downstream utility.

IDs: `W2-C-0041` - `W2-C-0080` (40 ideas). High-ROI picks: `W2-C-0041`, `W2-C-0042`, `W2-C-0043`, `W2-C-0046`, `W2-C-0049`, `W2-C-0053`, `W2-C-0054`, `W2-C-0055`, `W2-C-0057`, `W2-C-0060`, `W2-C-0065`, `W2-C-0070`, `W2-C-0071`, `W2-C-0078`.

## Cluster 3: Unproven community assumptions

Folk beliefs the community repeats without compute-matched evidence: pretraining always transfers, SAM generalizes zero-shot, multi-scale/EMA/mosaic/deformable-attention necessity, mask supervision helps boxes, more data always helps.

IDs: `W2-C-0081` - `W2-C-0115` (35 ideas). High-ROI picks: `W2-C-0081`, `W2-C-0082`, `W2-C-0099`, `W2-C-0106`, `W2-C-0115`.

## Cluster 4: Surprising empirical phenomena

Measurable oddities worth turning into papers: ghost detections of removed objects, seed variance vs leaderboard deltas, stride-grid quantization, typographic hijacking, vocabulary interference, dataset fingerprints, batch-composition effects.

IDs: `W2-C-0116` - `W2-C-0145` (30 ideas). High-ROI picks: `W2-C-0116`, `W2-C-0119`, `W2-C-0122`, `W2-C-0129`, `W2-C-0136`, `W2-C-0145`.

## Cluster 5: Negative results that would change practice

Negative results that would redirect practice if firmly established: explanations failing sanity checks, UDA losing to 50 labels, calibration dying at NMS, active learning losing to random, distillation discarding tails, TTA collapse.

IDs: `W2-C-0146` - `W2-C-0175` (30 ideas). High-ROI picks: `W2-C-0146`, `W2-C-0148`, `W2-C-0149`, `W2-C-0150`, `W2-C-0154`, `W2-C-0158`, `W2-C-0159`, `W2-C-0166`.

## Cluster 6: Robustness, calibration, uncertainty quantification

Robustness, calibration, and uncertainty as first-class measurable objects: spatial calibration, open-set overclaiming, threshold drift, conformal boxes, flicker-as-uncertainty, failure alarms, drift early warning.

IDs: `W2-C-0176` - `W2-C-0200` (25 ideas). High-ROI picks: `W2-C-0177`, `W2-C-0178`, `W2-C-0180`, `W2-C-0188`, `W2-C-0190`, `W2-C-0193`, `W2-C-0197`.

## Cluster 7: Domain shift and synthetic-to-real

Domain shift and synthetic-to-real as decomposable, measurable quantities: gap factorization, fidelity ROI curves, asset diversity vs volume, label-convention shift, ISP vs photons, foundation-backbone gap closure.

IDs: `W2-C-0201` - `W2-C-0225` (25 ideas). High-ROI picks: `W2-C-0201`, `W2-C-0206`, `W2-C-0208`, `W2-C-0221`.

## Cluster 8: SR, restoration, generation, diffusion tied to dense prediction

Super-resolution / restoration / generation only as dense-prediction science: does SR recover information or hallucinate it, object erasure by denoisers, generated-data label noise and fingerprints, task-aware codecs, enhancement optima divergence.

IDs: `W2-C-0226` - `W2-C-0250` (25 ideas). High-ROI picks: `W2-C-0226`, `W2-C-0227`, `W2-C-0228`, `W2-C-0231`, `W2-C-0234`, `W2-C-0236`.

## Cluster 9: Long-tail, metric fairness, dataset bias

Long-tail, metric fairness, and dataset bias as scientific objects: framing and geographic bias, tail-progress illusions, head-class sacrifice accounting, CLIP-curation blind-spot propagation, annotation salience bias.

IDs: `W2-C-0251` - `W2-C-0280` (30 ideas). High-ROI picks: `W2-C-0251`, `W2-C-0252`, `W2-C-0254`, `W2-C-0255`, `W2-C-0258`, `W2-C-0259`, `W2-C-0260`, `W2-C-0269`, `W2-C-0276`, `W2-C-0279`.

## Cluster 10: Reproducibility and compute-fair comparison

Reproducibility and compute-fair comparison as research: stale baselines, shadow tuning, framework variance, ablation sign-flips, composition tests, power tables, benchmark mutation audits.

IDs: `W2-C-0281` - `W2-C-0305` (25 ideas). High-ROI picks: `W2-C-0281`, `W2-C-0282`, `W2-C-0283`, `W2-C-0285`, `W2-C-0287`, `W2-C-0292`, `W2-C-0299`, `W2-C-0302`, `W2-C-0303`.

## Cluster 11: New combinations with genuine scientific motivation

Cross-disciplinary imports with stated motivation: conformal-aware NMS, psychophysics staircases, item response theory, survey sampling, metrology error budgets, extreme value theory, bandit annotation, contract testing.

IDs: `W2-C-0306` - `W2-C-0325` (20 ideas). High-ROI picks: `W2-C-0306`, `W2-C-0308`, `W2-C-0309`, `W2-C-0311`, `W2-C-0319`, `W2-C-0321`.

## Cluster 12: Simple hypotheses that challenge accepted beliefs

Simple, cheap, belief-challenging hypotheses: residual errors are annotation errors, recipes not architectures drove progress, 1k images rank models, classification not localization is the bottleneck, instructions beat annotators.

IDs: `W2-C-0326` - `W2-C-0345` (20 ideas). High-ROI picks: `W2-C-0326`, `W2-C-0327`, `W2-C-0328`, `W2-C-0331`, `W2-C-0338`, `W2-C-0344`, `W2-C-0345`.
