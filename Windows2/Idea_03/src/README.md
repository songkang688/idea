# src/ — prototype code (wrapped) and the path to the real runs

## What is here

`prototype/` is a **verbatim copy** of `Windows2/_wip/stage7_proto_B0114/` (Stage-7 Agent T's CPU
synthetic prototype), included so the package is self-contained and so the real implementation can
start from tested code. Nothing in it was modified by the packaging agent. See
`prototype/README.md` for its own quickstart, measured-sandbox tables, and honesty notes, and
`prototype/ARCHITECTURE.md` for the sandbox-level diagram and tested invariants.

> **Provenance:** every number the prototype prints is MEASURED ON SYNTHETIC SCENES generated
> in-process. No ADE20K / Cityscapes / NYUv2 / ImageNet / DINOv2 number exists anywhere under `src/`.
> The sandbox's content-dominant outcome is a HYPOTHESIS-level risk input (`experiments.md` §20),
> not a dense-task finding.

Quick sanity run (CPU-only, ~60 s + ~2 s tests):

```bash
cd prototype
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
python run_synthetic.py --config configs/default.yaml
python -m pytest tests/ -q   # 39 tests
```

## What carries over to the real experiment, verbatim or near-verbatim

| Prototype module | Real-run fate |
|---|---|
| `src/vpt_registers/train.py::train_arm` | kept — arm interface consumes `(features, labels)`; backbone-agnostic |
| `src/vpt_registers/metrics.py` | kept — decomposition + telescoping assertion + H2 readout are scale-free |
| `src/vpt_registers/signatures.py` | kept, extended — add NOP-vs-broadcast classification (arXiv:2606.08105) and register-competition readout |
| `src/vpt_registers/b0001_hook.py` | kept quarantined — flag gate, banner, and import-isolation AST tests re-enforced at scale |
| `src/vpt_registers/config.py` + YAML pattern | kept — real configs in `../configs/` follow the same schema style |
| `tests/` | kept as CI — plus new tests pinning the 2506.08010 arm against its reference implementation |

## What must be replaced or added for the real runs

1. **Backbone:** `TinyViT` → frozen DINOv2 ViT-B/14 and DINOv2-with-registers ViT-B/14 (checkpoints
   pinned by hash from the DINOv2 release).
2. **Data:** synthetic scene generator → ADE20K (killer), then Cityscapes / NYUv2 / classification
   triplet (full matrix).
3. **Arm (c):** the toy `sink_only` value-zeroing is NOT the real attention-bias arm. The real arm (c)
   uses the exact **test-time-registers** construction (arXiv:2506.08010, pinned repo commit). The toy
   sink arm survives as arm (e), the denominator control.
4. **Additions the prototype deliberately does not implement:** token-count sweep K ∈ {1,4,16,64},
   VPT-deep, NOP/broadcast diagnostics, classification Fig. 11 control, 24-run protocol on the ViT-B
   pair. All specified in `../experiments.md` §14–§16 and `../configs/`.

## Invariants that must survive the port (tested in the prototype)

- backbone bit-identical across arms per (variant, seed); prompt params owned by the arm;
- one head class per config for every arm; head reads patch tokens only;
- decomposition telescopes seed-wise (programmatic assertion);
- EXPECTED (pre-registered) vs MEASURED blocks separated in all run output;
- B-0001 hook: flag-gated, banner-printed, import-isolated.
