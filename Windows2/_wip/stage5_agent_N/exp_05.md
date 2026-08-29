# exp_05 — C-0306: conformal coverage destroyed by NMS + coverage-preserving suppression

**ID:** W2-C-0306.
**Pipeline status:** D bet #10 → G LOCK [M](P)(⏰) → K SURVIVE-IF-EXPERIMENT (blind-spot magnitude is the gate; WACV 2024 IoU-aware-calibration baseline mandatory; "third conformal-OD paper likely within months"). PI binding: gravity MUST include ≥1 C idea (this and/or C-0338).

## Research question

How much distribution-free (conformal) coverage does standard NMS silently destroy in object detection — and can a suppression rule designed to preserve candidate-set coverage restore nominal guarantees at bounded prediction-set size, beating both "calibrate after NMS" and "no NMS at all"?

## Falsifiable hypothesis

H1 (measurement): a non-trivial fraction of GT objects have **all** of their covering candidate boxes suppressed by standard NMS (the blind spot), and the fraction grows with scene crowdedness and NMS aggressiveness.
H2 (method): a coverage-aware suppression rule achieves nominal conformal coverage with prediction-set sizes smaller than the no-NMS + IoU-aware-calibration pipeline (WACV 2024, doi:10.1109/wacv57701.2024.00478) and coverage strictly better than SeqCRC-style post-NMS calibration (arXiv:2505.24038) on the suppressed-object stratum.
Falsified if: the blind spot is ≈1% everywhere (K's footnote scenario), or if the WACV 2024 no-NMS pipeline dominates the coverage/set-size frontier.

## Prediction

HYPOTHESIS: blind spot small on sparse COCO-style scenes, materially larger in crowded scenes (dense pedestrians, cluttered shelves) and at aggressive IoU thresholds — the regime where the method leg earns its slot. No magnitude claimed; the magnitude IS the gate.

## Method sketch (modules / dataflow)

1. **Candidate-cache harvester:** run detectors with post-processing disabled, cache full pre-NMS candidate sets (boxes, scores, class logits) — code-level access confirmed feasible per G's census for the sibling idea C-0158.
2. **Blind-spot analyzer:** for each GT object, compute whether any candidate covering it (IoU ≥ τ) survives NMS across (detector × NMS-IoU threshold × score threshold × crowdedness stratum).
3. **Conformal layer:** split-conformal calibration on candidate sets pre-suppression (following the COD formulation of SeqCRC as the reference construction, credited).
4. **Coverage-preserving suppression module (the method):** greedy suppression constrained to never remove the last calibrated-set representative of any spatial cluster; provable candidate-set coverage bound; tunable redundancy budget.
5. **Frontier evaluator:** coverage vs mean set size vs downstream duplicate-rate, against all baselines.

## Data

COCO val, LVIS (crowded/rare), plus one dense-crowd benchmark (e.g., CrowdHuman-class pedestrian data, chosen at execution) — the crowdedness axis is load-bearing. Cached predictions from 5–8 public detectors spanning anchor-based, anchor-free, and DETR-family (DETR-family = no-NMS natural control).

## Baselines

(1) SeqCRC-style conformal-after-NMS (arXiv:2505.24038); (2) IoU-aware calibration, no NMS (WACV 2024 — K-mandated); (3) soft-NMS and class-agnostic NMS variants; (4) DETR-family end-to-end (suppression-free by construction); (5) naive keep-all + conformal (set-size upper bound).

## Metrics

Blind-spot rate (fraction of GT objects losing all covering candidates), stratified by crowdedness/class/threshold; empirical coverage vs nominal (1−α) pre/post suppression; mean prediction-set size; risk/set-size frontier curves.

## Killer Experiment

**The blind-spot measurement alone: cached candidate sets → blind-spot rate table across detectors × thresholds × crowdedness.** Pure analysis on cached inference — days of work, and it decides everything downstream (K: "if it's 1%, the paper is a footnote; if large, everything downstream matters"). The method leg is built ONLY if the gate opens.

## GPU/VRAM/time estimate

Inference/caching: 5–8 detectors × 3 datasets ≈ **2–4 GPU-days (single 24GB GPU)**; storage ~200–500 GB for pre-NMS candidates (prunable by score floor). Blind-spot analysis + conformal layer: CPU, days. Method leg: no training, algorithm + evaluation ≈ 1–2 weeks of engineering. Total worst case < 1 GPU-week of compute.

## Stop / pivot / kill criteria

- **Kill the method leg** if blind-spot < ~1–2% in ALL strata including crowded scenes → publish the measurement as a short note (still the first quantification; still useful to the conformal-OD line).
- **Pivot to theory** if the WACV 2024 no-NMS pipeline dominates the frontier → the paper becomes "when is suppression compatible with coverage at all?" — a characterization result (conditions on candidate-cluster correlation under which any suppression preserves coverage), which retains the formal-novelty moat.
- **Urgency stop-loss:** two-quarter execution clock (K's urgency-cluster rule); freshness re-search at proposal AND experiment freeze — a third conformal-OD paper is expected within months.

## Reviewer-2 leftover

"Downstream users don't want candidate sets, they want detections" — the method must show the coverage-preserving output is consumable (bounded duplicate rate) or the practical story leaks. Crowded-scene NMS failure is old news qualitatively (duplicate suppression literature); the conformal-coverage framing must carry the novelty, which is why the formal coverage bound is not optional.

## Expected result (HYPOTHESIZED, not measured)

Gate opens in crowded strata; method beats conformal-after-NMS on suppressed-object coverage and beats no-NMS on set size in at least the crowded regime; DETR-family arm shows the problem is suppression-specific, not detection-specific.

## Negative-result interpretation

A universally tiny blind spot is a *pro-NMS* finding the conformal-OD literature currently assumes away — a citable calibration of how much the SeqCRC-style "condition on the post-NMS list" concession actually costs (answer: nothing). Cheap, honest, and it releases the portfolio's conformal slot for other C ideas.
