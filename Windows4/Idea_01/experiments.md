# Experiments — SeeingInside

All cells **EXPECTED** until run.

| ID | Condition | Image | Prompt | Question |
|----|-----------|-------|--------|----------|
| E0 | SAM original | I | GT box | Ceiling under oracle box |
| E1 | Mean fill | I_fill | same | Interpolator |
| E2 | Inpaint | I_inpaint | same | On-manifold appearance |
| E3 | Swap crop | I_swap | same | Identity vs any object |
| E4 | Ellipse null | — | box | Geometry-only |
| E5 | GrabCut | I, box | — | Classical |
| E6 | Learned box→mask | box raster | — | Extra-parameter null |

**Killer = {E0,E1,E2,E4} on n=64.**

Controls: identical checkpoint, no TTA, one seed, freeze all weights.
