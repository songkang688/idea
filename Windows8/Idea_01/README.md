# Idea_01 README

**Objectness, Not Features** — frozen SAM embeddings + density/exclusion vs prompted SAM.

## Quick start

```bash
pip install -r ../../requirements.txt
python src/train_density_head.py --config configs/killer_e0.yaml
python src/eval_killer.py --config configs/killer_e0.yaml
```

Without SAM weights, the script runs a **FakeEncoder** so the training loop is executable. Replace with `sam_encoder.py` when checkpoints are available.

## Hypothesis tags

All numbers produced by this code on FakeEncoder are **toy mechanics checks**, not scientific results.
