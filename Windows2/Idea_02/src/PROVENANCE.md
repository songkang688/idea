# Provenance of this `src/` mirror

This directory is a **verbatim mirror** of the Stage-7 synthetic prototype
`Windows2/_wip/stage7_proto_A0028/` (built by Stage-7 Agent R; protocol source
`Windows2/_wip/stage5_agent_N/exp_07.md`), copied into the package draft by Stage-7 Agent V so the
package is self-contained and runnable when copied to `Windows2/Idea_02/`.

- **Canonical origin:** `Windows2/_wip/stage7_proto_A0028/` — if the two ever diverge, the proto
  directory wins until the PI copies this package to `Windows2/Idea_02/`, after which the Idea_02
  copy becomes canonical.
- **Copied verbatim:** `run_synthetic.py`, `requirements.txt`, `src/a0028/` (7 modules),
  `tests/` (5 files, 23 tests), `configs/` (`default.yaml`, `smoke.yaml`),
  `results_synthetic/report.md` (= proto `results/report.md`, the committed MEASURED-synthetic run).
- **Not copied:** `results/results.json` (596 KB per-cell JSON) — it stays at
  `Windows2/_wip/stage7_proto_A0028/results/results.json`; it is deterministically regenerable here
  via `python run_synthetic.py --config configs/default.yaml --out results_synthetic/`.
- **Verified at packaging time (2026-08-28):** smoke run (`configs/smoke.yaml`) and all 23 tests
  pass on this mirror, CPU-only.

Labeling reminder: everything this code produces is **MEASURED (synthetic surrogate)** — a
functional model of a memory tracker with a known arbitration parameter, **not SAM2**. The env-gated
real-SAM2 adapter (`src/a0028/sam2_wrapper.py`) is OFF by default and produces no numbers in this
package.
