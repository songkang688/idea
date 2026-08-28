# Experiments — AlphaSmoke

| ID | Arm |
|----|-----|
| B0 | HSV/Otsu baseline |
| P1 | Frozen COCO/SAM encoder + linear |
| P2 | Frozen matting encoder + linear |
| P2b | Same matting encoder trained on **binarized** mattes (R2 control) |
| M | Rank 4 models by Dice vs mMse (synthetic diagnostic) |

Primary endpoint: real-smoke mIoU. **ACTUAL:** none.
