# Idea_02 — Camera-ID leakage inflation on smoke/fire benchmarks

**Hypothesis:** Random splits inflate detector mAP relative to **camera-disjoint** splits; **event-disjoint** (PYRONEAR-style) is not the same as camera-disjoint; empty frames from **seen cameras** score differently than unseen (memorization, not only geography shift).

## Killer

Train a small detector 3 seeds × {random, event-disjoint, camera-disjoint}. Probe camera-ID from frozen backbone. Empty-frame FP seen vs unseen cameras.
