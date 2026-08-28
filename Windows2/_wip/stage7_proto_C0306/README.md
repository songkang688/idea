# Stage-7 prototype — C-0306: conformal coverage vs NMS (synthetic)

Runnable minimal prototype of the **C-0306 killer experiment**
(`Windows2/_wip/stage5_agent_N/exp_05.md`; pipeline: D bet #10 → G LOCK →
K SURVIVE-IF-EXPERIMENT → N killer-experiment protocol). Built by Stage-7
Agent P. This is **not** the killer experiment itself and produces **no
real-data numbers** — it is the measurement + method machinery, demonstrated
end-to-end on synthetic scenes, so a researcher can (a) sanity-check the
mechanism, (b) audit the statistics, and (c) drop in cached real-detector
candidates later without rewriting anything.

```
NO NUMBER IN THIS DIRECTORY IS A COCO / LVIS / CrowdHuman RESULT.
Every quantity printed by run_synthetic.py is MEASURED ON SYNTHETIC DATA
generated in-process, and is labelled as such. The pre-registered claims
from exp_05 are printed as EXPECTED (hypothesis); what the synthetic run
actually produced is printed as MEASURED (synthetic). The magnitude on
real data is exactly the open question the killer experiment must answer.
```

## The claim being prototyped

Split-conformal calibration on detection candidate sets gives a marginal
guarantee: with probability ≥ 1−α, each GT object is covered (IoU ≥ τ) by
some candidate in the prediction set. Standard greedy NMS runs *after* the
scores are produced and can delete **every** covering candidate of a GT
object (the **blind spot**). Consequences prototyped here:

- **H1 (measurement gate):** the blind-spot rate is non-trivial and grows
  with scene crowdedness and NMS aggressiveness. K's attack: if it is ~1%
  everywhere, the paper is a footnote — the magnitude IS the gate.
- **Coverage destruction (falsifiable):** a guarantee calibrated pre-NMS no
  longer holds at nominal after NMS; and calibrating *after* NMS
  (SeqCRC-style, treating NMS as part of the model) cannot reach nominal at
  any threshold once blind-spot + miss rate exceeds α — the calibration
  itself certifies this by returning `q_hat = +inf`.
- **Constructive leg (H2 direction):** a coverage-preserving suppression
  (CPS) rule restores nominal coverage with sets much smaller than
  "keep everything", using a *provable* coverage-transfer argument
  (see "The CPS theorem" below).

## Quickstart

Requires Python ≥ 3.9, CPU only, no GPU, no datasets, no model weights.

```bash
cd Windows2/_wip/stage7_proto_C0306
pip install -r requirements.txt          # numpy, PyYAML, pytest

# main demo: three crowdedness strata, standard NMS (iou 0.5) at deploy
python run_synthetic.py --config configs/default.yaml

# stress demo: crowded scenes + aggressive NMS (iou 0.3) at deploy
python run_synthetic.py --config configs/crowded_aggressive.yaml

# options
python run_synthetic.py --config configs/default.yaml --quick          # 80 scenes/level smoke run
python run_synthetic.py --config configs/default.yaml --seed 1         # seed override
python run_synthetic.py --config configs/default.yaml --json out.json  # machine-readable dump

# tests (27 tests, ~5 s)
python -m pytest tests/ -q
```

Optional editable install (not needed to run anything above):
`pip install -e .`

## What the committed configs measure (SYNTHETIC — mechanism demo only)

Numbers below were produced by the exact commands above at the committed
seeds (α = 0.1 → nominal 90%, τ = 0.5). They are reproducible, synthetic,
and claim nothing about real detectors.

`configs/default.yaml` (deploy NMS IoU 0.5 — the standard operating point):

| crowd level | blind @ NMS 0.3 | blind @ NMS 0.5 | pre-NMS cov (A) | post-NMS cov (B) | CPS cov (D) | CPS set vs keep-all |
|---|---|---|---|---|---|---|
| sparse  |  1.95% | 0.00% | 90.7% | 90.4% | 91.7% | 48% |
| medium  |  7.05% | 0.00% | 88.4% | 87.3% | 90.8% | 53% |
| crowded | 13.21% | 0.07% | 89.0% | 87.3% | 93.1% | 58% |

`configs/crowded_aggressive.yaml` (deploy NMS IoU 0.3 — the regime exp_05
hypothesises the blind spot lives in):

| crowd level | blind @ NMS 0.3 | pre-NMS cov (A) | post-NMS cov (B) | calib-after-NMS (C) | CPS cov (D) |
|---|---|---|---|---|---|
| crowded      | 13.67% | 89.2% | **71.8%** | 85.9%, `q_hat=+inf` (cap 86.8%) | 93.8% |
| very_crowded | 16.03% | 90.1% | **69.4%** | 84.5%, `q_hat=+inf` (cap 83.4%) | 96.1% |

Readings (all synthetic):

- **Both of K's regimes appear.** At standard NMS (0.5) on sparse scenes the
  blind spot is ≈0 and coverage destruction is within noise — K's
  "footnote scenario". In crowded scenes under aggressive NMS the blind spot
  is 13–16% and pipeline B loses 18–21 pp of coverage (z > 20). The synthetic
  generator was tuned so both regimes are visible; **which regime real data
  occupies is the gate and is not answered here.**
- **Calibrate-after-NMS is not a fix once the blind spot exceeds α:** the
  split-conformal quantile lands on +inf, i.e. nominal coverage is
  unachievable at any threshold; coverage on the blind stratum is 0 by
  construction (printed in the `blind-cov` column).
- **CPS** holds ≥ nominal (conservative, as the theorem predicts — it
  guarantees a lower bound) at roughly half the keep-all set size and with
  duplicates/GT reduced ~2.4x (e.g. 3.97 → 1.63 in crowded).

## The four pipelines

| | calibration pool | deploy-time pool | status |
|---|---|---|---|
| **A** keep-all + conformal | full pre-NMS cache | full cache | valid; set-size upper bound (exp_05 baseline 5) |
| **B** calibrate pre-NMS → deploy NMS | full cache | NMS survivors | **the silently broken pipeline** under study |
| **C** conformal after NMS | NMS survivors | NMS survivors | SeqCRC-style (arXiv:2505.24038 framing); valid only when blind+miss ≤ α |
| **D** coverage-preserving suppression | full cache @ τ_cal | CPS-suppressed conformal set | provable coverage transfer at τ |

## The CPS theorem (the formal-novelty seed)

The Jaccard/Marczewski–Steinhaus distance `d(A,B) = 1 − IoU(A,B)` is a metric
(triangle inequality: Kosub 2019, arXiv:1612.02696). Hence for a kept box
`a`, a suppressed box `b`, and a GT `g`:

```
IoU(a, g) ≥ IoU(a, b) + IoU(b, g) − 1.
```

CPS recipe: calibrate the conformal layer at the stricter covering threshold
`τ_cal = τ + (1 − κ)`, then greedily suppress **within the prediction set**,
allowing a box to be removed only by a kept representative with
`IoU ≥ κ`. Then every GT covered at `τ_cal` pre-suppression stays covered at
`τ` post-suppression — deterministically per scene — so the marginal 1−α
guarantee transfers to the suppressed output. This is checked *exactly* (not
statistically) in `tests/test_suppression.py::test_theorem_coverage_transfer_exact`.
The knobs κ (merge threshold) and the redundancy budget trace the
coverage/set-size frontier the full paper would map.

## Layout

```
stage7_proto_C0306/
├── README.md                  # this file
├── ARCHITECTURE.md            # mermaid diagram + module map + invariants
├── requirements.txt
├── pyproject.toml             # optional editable install
├── run_synthetic.py           # entry point (EXPECTED vs MEASURED report)
├── configs/
│   ├── default.yaml           # sparse/medium/crowded, deploy NMS iou 0.5
│   └── crowded_aggressive.yaml# crowded/very_crowded, deploy NMS iou 0.3
├── src/conformal_nms/
│   ├── boxes.py               # vectorized IoU
│   ├── nms.py                 # standard greedy NMS
│   ├── synthetic.py           # scene generator (tiny-COCO mock)
│   ├── conformal.py           # split conformal on candidate sets
│   ├── blind_spot.py          # H1 analyzer
│   ├── suppression.py         # CPS (the constructive method sketch)
│   ├── pipelines.py           # pipelines A–D + metrics
│   └── config.py              # YAML loading
└── tests/                     # 27 CPU tests, no downloads
```

## From prototype to the real killer experiment

Everything downstream of the generator consumes plain
`(gt_boxes, cand_boxes, cand_scores)` triples (`Scene` objects). To run the
real gate per exp_05:

1. Replace `generate_dataset(...)` with a loader over cached pre-NMS
   candidate sets from 5–8 public detectors with post-processing disabled
   (COCO val, LVIS, one dense-crowd benchmark), stratified by crowdedness.
2. Re-run `blind_spot_table` — that table alone is the go/no-go gate
   (K: "if it's 1%, the paper is a footnote; if large, everything downstream
   matters").
3. If the gate opens, add the mandatory baselines this prototype does not
   implement: soft-NMS / class-agnostic NMS arms, the WACV 2024 IoU-aware
   calibration **no-NMS** pipeline (doi:10.1109/wacv57701.2024.00478,
   K-mandated), a DETR-family suppression-free control, and the full SeqCRC
   construction (this prototype implements only its calibrate-after-NMS
   skeleton), then map the coverage/set-size frontier with CPS's κ and
   redundancy knobs.

## Honesty & limitations

- **Synthetic ≠ evidence.** The generator was deliberately tuned so both the
  footnote regime and the destruction regime are visible; it can demonstrate
  the mechanism and validate the code, never the magnitude on real data.
- **Exchangeability caveat.** Conformal validity here treats pooled GT
  objects across i.i.d. scenes as the exchangeable unit; within-scene
  correlation means finite-sample validity is exact at the scene level and
  approximate at the object level (same concession as the conformal-OD
  literature; the real study should report both units).
- **CPS is one-sided.** The theorem gives coverage ≥ nominal (measured: it
  runs conservative, e.g. 93–96% at nominal 90% in crowded synthetic); the
  set-size cost of that conservatism vs pipeline C and vs the WACV 2024
  no-NMS baseline is precisely the frontier the method leg must win on.
- **Class-agnostic.** Single-class prototype; class-aware NMS and per-class
  calibration are real-experiment concerns.
