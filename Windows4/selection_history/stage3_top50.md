# Stage 3 → ~50 surviving hypotheses (Windows4)

Date: 2026-08-28. After adversarial prior-work search (3 independent assassins).
Epistemic status: **REVIEW JUDGMENT**. Citations in `stage3_kill_*.md` are claimed web-verified by those agents; Stage 4 must still treat closest-work as attack surface.

## Scoreboard

| File | KILL | MUTATE | SURVIVE |
|------|------|--------|---------|
| `stage3_kill_sam_eval.md` | 9 clusters | 3 | 3 |
| `stage3_kill_medical_smoke.md` | 15 IDs | 8 | 5 |
| `stage3_kill_peft_vlm.md` | 7 clusters | 6 | 5 |

Load-bearing kills: RClicks/BREPS ate oracle-prompt / human-click / prompt-distribution / box-jitter; Gu et al. 2404.09957 ate decoder-only MedSAM and much PEFT-replication; MedSAM-2 / Dong et al. ate SAM2-as-video prompt-slice; ProFSAM ate detector+SAM2 fire; Label Convergence / COCO-ReM ate noise-floor-as-paper.

## Stage-4 attack list (merged unique papers, ~24; expand with arms to ~50 rows)

### SURVIVE (flagship)

1. **P14** S-014/S-604 — Ablate *image* tokens inside a tight box; prompt fixed. (SAM seeing vs box-to-mask interpolator)
2. **P101** A1-101 — Prompt-embedding norm as training-free granularity knob (difference vs GraCo)
3. **P079** S-079 — Probe SAM2 memory: position vs appearance collapse
4. **P103** S-103 — Portrait-matting pretrain → smoke (transfer, not SAM wrapper)
5. **P063** A1-063 + A1-067 — Feature-flow / feature-warp vs optical refraction (glass)
6. **P060** A1-060 — Depth-edge auto-prompts for glass (RGB-edge control required)
7. **P065** C1-065 + C1-061 — Prompt-type behavioral forgetting + multimask diversity collapse
8. **P177** S-177 + C1-062 — Forgetting locus: decoder vs encoder, layer splice
9. **P107** A1-107 — Attention-LoRA vs MLP-LoRA error-type split
10. **P107v** B1-107 — Inpaint-object-out; phantom dense masks (VLM hallucination)
11. **P079f** B1-079 — FSS background-swap cheat
12. **P051** B1-051 — Copy-paste vs diffusion at matched GPU-hours

### MUTATE (still in pool)

13. **P096** S-096 + S-102 — Smoke metric reversal (Dice vs alpha/ceiling), not another segmenter
14. **P044** S-044/A1-034 — Despeckle/window vs LoRA on ultrasound/CT (preprocess falsifier)
15. **P042** S-042 — Anisotropy confound vs “medical 3D” (not a new SAM2)
16. **P040** A1-040 — Boundary-diffuseness under-segmentation law
17. **P007** S-007 — Scorer-validity of test-time prompt evolution (not anti-SAMPOT slogan)
18. **P004** A1-004 — Holes: prior vs COCO-convention vs postprocess
19. **P031** C1-031 + C1-025/037 — FT desyncs IoU-head vs mask quality; calibration/robustness frontier
20. **P052** S-052 — Mutate to objectness-prior harm at small-n (not generic FM-hurt)
21. **P110** C1-110 — Reporting protocol attached to P065, not a standalone suite paper
22. **P108** A1-108/C1-067 — Drift statistic *predicts* later zero-shot drop
23. **P228** S-228 — Frequency-controlled VLM prior vs atypical appearance (dense)
24. **P061u** B1-061 — Fold into factorial style×self-training (not FDA remix)
25. **P082** C1-082 + S-183 — Threshold artifact + low-plasticity gatekeeper (run first, may kill Forget thread)
26. **P001** C1-001 — SA-1B near-dup audit (gating; modal outcome = null)

### Dropped from Top-50 (hygiene only)

Oracle boxes, simulated clicks, MedSAM decoder-only, SAM2 prompt-slice, smoke-as-instance ontology, time-to-alarm, dose-volume, partial-volume-as-alpha, random-LoRA-as-paper, AL-dead-under-DINOv2, CLIP linear map, channel-lift, patch-grid aliasing.

## Next

Stage 4 Reviewer #2: reject each of P14–P061u unless a realistic experiment would silence the attack.
