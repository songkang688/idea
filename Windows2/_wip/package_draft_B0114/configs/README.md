# configs/ — real-experiment config drafts (NOT runnable against the prototype)

These YAMLs are **specification drafts** for the real runs (`experiments.md` §14–§16). They follow the
prototype's config schema style but reference real datasets/checkpoints and fields the prototype does
not implement (`backbone_ckpt`, `dataset`, `attention_bias`, `diagnostics`). The prototype's own
runnable sandbox configs live in `../src/prototype/configs/` and are untouched.

| File | Experiment | Gate status |
|---|---|---|
| `exp02_gate.yaml` | exp_02 stratified norm-map audit | **runs first (binding)** |
| `classification_control.yaml` | E0 Fig. 11 reproduction control | prerequisite; HALT on failure |
| `killer_ade20k.yaml` | E1 24-run killer grid | committed only after exp_02 returns |
| `token_sweep.yaml` | E3 K-sweep confound bound | after E1 lands in a live cell |

Checkpoint hashes and dataset paths are placeholders (`TODO@execution`) until group-compute paths are
assigned; pinning them is promotion-checklist item 3 (`roadmap.md` §28).
