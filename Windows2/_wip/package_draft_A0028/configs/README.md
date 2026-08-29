# configs/

- `default.yaml`, `smoke.yaml` — **synthetic surrogate** configs, consumed by `../src/run_synthetic.py`
  (copies of the mirror's own `../src/configs/`, kept here so package-level specs live in one place).
  Everything they produce is MEASURED (synthetic surrogate) — not SAM2.
- `killer_sam2l.yaml` — the **pre-registered real-model killer-battery spec** (SAM2.1-L, 1 GPU-day,
  `experiments.md` Section 20). Not consumed by any runner in this package; the real-model runner is
  built days 1–3 of week one against this spec. Grid, gates, and scoring thresholds in this file are
  frozen by pre-registration; changing them after day 4 requires a logged PI override.
