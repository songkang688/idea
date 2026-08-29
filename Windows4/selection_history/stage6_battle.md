# Stage 6 — Research group battle (condensed, Windows4)

Role cycle covered by Stage 3 assassins + Stage 4 R2 (three independent rejectors). No false consensus.

## Unresolved disagreements kept explicit

- Set A wants P14 merged with P107v; Set C **scooped P107v** (HalluSegBench). Supervisor: **do not merge**. P14 stays vision-only counterfactual (inpaint/swap of *pixels inside the box*), not VLM hallucination.
- P063 vs P103 for third slot: glass physics has higher ceiling and heavier rendering cost; smoke transfer has public data and a one-week killer. **Third slot = AlphaSmoke.** P063 is backup.
- P065 vs P107 for PEFT slot: P107 is more “constructive mechanism” but smaller blast radius. **P065 is the PEFT paper**; P107 is an ablation chapter.

## Fatal flaws that ended threads

HalluSegBench scoop; RClicks/BREPS on prompts; Gu et al. on decoder-only; MedSAM-2 on prompt-slice; Matting Anything on SAM-alpha heads.

## Decisive experiments that remain (must run in this order)

1. P082 noise-floor envelope (1–2 GPU-days) — if “forgetting” is thresholding, **pivot Idea_02**
2. P14 on-manifold inpaint inside box vs prompt-only vs box-fill (CPU/GPU, frozen SAM)
3. P103 linear-probe / tiny-head: matting-pretrained encoder vs COCO-seg encoder on real smoke mIoU

Battle stop: no new fatal prior-work in Stage 4 beyond HalluSegBench, which we absorbed.
