# src/ — runnable prototype (copied from `Windows2/_wip/stage7_proto_C0306/`)

This is a full copy of the Stage-7 Agent P synthetic prototype (not a stub), re-verified runnable
from this package layout: **27/27 tests pass; both configs run end-to-end; CPU-only; no datasets, no
model weights, no GPU.**

```bash
pip install -r src/requirements.txt        # numpy, PyYAML, pytest

# from the package root:
python src/run_synthetic.py                                        # default config
python src/run_synthetic.py --config configs/crowded_aggressive.yaml
python src/run_synthetic.py --quick --json out.json                # smoke run + JSON dump
python -m pytest src/tests/ -q                                     # 27 tests, ~5 s
```

**Every number printed is MEASURED ON SYNTHETIC DATA generated in-process** — see the disclaimer the
script prints, `../proposal.md` §18, and the original prototype README
(`Windows2/_wip/stage7_proto_C0306/README.md`).

## Differences from the original prototype (three path adjustments only; no logic changes)

1. `run_synthetic.py` — `sys.path` insert points at its own directory (code now lives *in* `src/`),
   and the default `--config` resolves to `<package root>/configs/default.yaml`.
2. `tests/conftest.py` — adds the `src/` directory (tests moved to `src/tests/`).
3. `tests/test_end_to_end.py` — config root resolves to the package root (`configs/` is top-level).

The original also ships `pyproject.toml` for an optional editable install and `ARCHITECTURE.md`
(code-accurate module diagram); consult those at the prototype path. Module map:

| File | Role (proposal.md §8 module) |
|---|---|
| `conformal_nms/boxes.py` | vectorized IoU (shared util) |
| `conformal_nms/nms.py` | standard greedy NMS — the intervention under study |
| `conformal_nms/synthetic.py` | scene generator — synthetic stand-in for module 1 (harvester) |
| `conformal_nms/blind_spot.py` | module 2 — H1 blind-spot analyzer (the gate) |
| `conformal_nms/conformal.py` | module 3 — split conformal, +∞ achievability certificate |
| `conformal_nms/suppression.py` | module 4 — CPS with provable coverage transfer |
| `conformal_nms/pipelines.py` | module 5 (minimal) — pipelines A–D + shared metrics |
| `conformal_nms/config.py` | YAML → dataclasses |
| `run_synthetic.py` | entry point — EXPECTED (hypothesis) vs MEASURED (synthetic) report |
| `tests/` | 27 CPU tests incl. exact theorem check |

Everything downstream of the generator consumes plain `(gt_boxes, cand_boxes, cand_scores)` triples
(`Scene` objects), so cached real-detector candidates are a drop-in replacement — the real killer
experiment is a loader swap (`../experiments.md` E1), not new machinery. Missing real-experiment
modules (harvester, dataset loaders, external baseline arms, frontier grid runner) are enumerated in
`../proposal.md` §11.
