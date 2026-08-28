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

## Stage 5 engineering

Equal-N, class-ratio-matched splits. Cluster bootstrap over **events**. Probe control: ImageNet-pretrained backbone never trained on smoke.

Day-1: Pyronear-2025 subsample, YOLOv8n, 1 seed × 3 protocols + probe + empty-frame FPR. ~10 GPU-h.

**STOP** if random≈camera-disjoint within seed noise **and** probe≈chance **and** no seen/unseen empty FPR gap (confirm with 2 more seeds).

Dedup (pHash) rerun separates duplicate leakage from camera signature.
