# Idea_02 experiments

## Killer (H1)

1. Define bins: diameter {4,6,8,10} mm × CNR {1,2,3,5} (CT slice units — finalize with LIDC metadata).
2. Synthetic: insert Gaussian/soft-edged blobs into nodule-free LIDC slices; N≥30 per bin.
3. Real: LIDC nodules mapped into the same bins (may be sparse — pre-register merge rule).
4. Pipeline: one CNN denoiser at 3 strengths + identity.
5. Frozen 2D nnU-Net or a simple blob detector for MVE (declare if blob detector: then full paper must upgrade to nnU-Net).
6. τ(synthetic suppression, real miss-rate increase vs identity).
7. **Kill if τ CI includes 0 or any bin sign-flip vs prediction of H2.**

## Full

Add BM3D, SR; MRI arm; mini radiologist check optional.

## Controls

Same lesions across strengths; noise matching; no train/test detector leakage onto enhanced images.
