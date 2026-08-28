# Idea_02 experiments

## Killer

1. Inventory camera IDs on one public set (PYRONEAR or FIgLib if IDs exist).
2. Build three splits; train YOLO-nano or Smoke-CNN, 3 seeds.
3. Metrics: image-level AP and FAR@recall — IoU is secondary (operational).
4. Empty-frame protocol: score negatives from seen vs unseen cameras.
5. Linear probe: camera classification from pooled backbone features (train cameras vs test time).

## Stop

- **Kill** if no camera metadata.
- **Pivot** to event-disjoint only if cameras < 10 (underpowered).
- **Continue** if H1 and H4 hold on ≥2 datasets.

## Compute

1 GPU, 1–3 days for small detector × 9 runs.
