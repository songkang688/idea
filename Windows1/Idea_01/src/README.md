# RetainSAM src

```
cd Windows1/Idea_01
pip install -r requirements.txt
PYTHONPATH=src python src/train_retain.py --config configs/killer_kvasir.yaml
```

This prints a WiSE-FT demo on dummy tensors. Plug in `segment_anything.sam_model_registry` and your dataloaders in `train_retain.py` before any real run.

Do not commit SAM `.pth` checkpoints.
