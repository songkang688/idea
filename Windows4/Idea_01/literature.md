# SeeingInside — Literature (verified citations only)

**Citation policy (binding, per Windows4 supervisor ledger and Stage-7 instructions):**
every entry below appears in `Windows4/selection_history/stage3_kill_sam_eval.md`, where the
Stage-3 Prior-Work Assassin recorded it as retrieved and read (abstract + relevant sections)
on 2026-08-28, or is the SAM paper itself (Kirillov et al.). **No other papers are cited
anywhere in this package.** Where the proposal needs a tool whose paper is not on this list
(e.g., a diffusion inpainter), the tool is named generically and the citation is deferred to
run time — see §Deliberately-not-cited.

---

## A. Core — the causal gap this project occupies (Stage-3 Cluster 2)

1. **Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T.,
   Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., Girshick, R.**
   *Segment Anything.* ICCV 2023. arXiv:2304.02643. https://arxiv.org/abs/2304.02643
   — KNOWN FACT source for architecture: ViT image encoder, prompt encoder, light mask
   decoder; positional encodings re-injected into the image-embedding side of decoder
   cross-attention at every layer (paper + released `segment-anything` code). This
   architectural fact is why off-manifold ablations alone cannot identify image-evidence
   reliance (R2 attack iii) and why the prompt-only null is measurable at all.

2. **Fan, Q., Tao, X., Ke, L., Ye, M., Zhang, Y., Wan, P., Wang, Z., Tai, Y.-W., Tang, C.-K.**
   *Stable Segment Anything Model.* 2023. arXiv:2311.15776. https://arxiv.org/abs/2311.15776
   — "First comprehensive analysis of SAM's segmentation stability across prompt qualities";
   locates the mechanism in which image features the mask decoder attends to under bad
   prompts. **Prompt-side intervention with the image fixed** — the adjacent-but-different
   prior work Reviewer #2 is expected to cite. We invert the intervention.

3. **Moskalenko, A., Kuznetsov, N., Dudko, V., Iasakova, A., Boldyrev, T., Shepelev, D.,
   Spiridonov, T., Kuznetsov, B., Shakhuro, V.**
   *BREPS: Bounding-Box Robustness Evaluation of Promptable Segmentation.* 2026.
   arXiv:2601.15123. https://arxiv.org/abs/2601.15123
   — Real-user box distributions, per-pixel IoU heatmaps over box placement, worst-case
   realistic box search, 15 models × 10 datasets, ~30% IoU drops vs tight-box protocol.
   Establishes (i) output is a steep function of box coordinates, (ii) tight-box protocols
   overestimate deployment quality on natural images. Defines the "priced-in" boundary our
   significance argument must clear — hence the medical-primary endpoint.

4. **Huang, Y., et al.** *Robust Box Prompt based SAM (RoBox-SAM).* MICCAI MLMI 2024.
   arXiv:2407.21284. https://arxiv.org/abs/2407.21284
   — Systematic 0–30% box-shift sweeps over 99,299 images across 5 medical modalities;
   attention-drift analysis under low-quality boxes. Again: prompt perturbed, image fixed.

5. **(Authors as listed on arXiv.)** *Enhancing MedSAM with a Lightweight Box Predictor.*
   2026. arXiv:2606.04705. https://arxiv.org/abs/2606.04705
   — Documents that box-fine-tuned MedSAM decoders "learned to expect" box geometry and
   that predicted boxes impose rigid rectangular constraints on irregular lesions.
   Observational evidence of a box-geometry prior; motivates our EXPECTED result that
   MedSAM's null-reachable fraction exceeds base SAM's.

## B. The audited protocol — tight-box medical evaluation

6. **Ma, J., et al.** *Segment Anything in Medical Images (MedSAM).* Nature Communications
   2024. arXiv:2304.12306. https://arxiv.org/abs/2304.12306
   — The box-prompt medical protocol whose numbers our primary endpoint re-reads: what
   fraction of MedSAM-protocol box-prompt Dice is reachable with no image evidence.

7. **Mazurowski, M. A., et al.** *Segment anything model for medical image analysis: an
   experimental study.* Medical Image Analysis 2023.
   https://doi.org/10.1016/j.media.2023.102918
   — Formalized "oracle performance" for SAM in medical imaging; showed prompt simulation
   dominates results; object-size vs performance analysis. Guides medical cohort selection.

8. **Huang, Y., et al.** *Segment Anything Model for Medical Images?* Medical Image Analysis
   2024. arXiv:2304.14660. https://arxiv.org/abs/2304.14660
   — Size/contrast-stratified SAM failures across medical benchmarks; box-jitter sensitivity.
   Source for the low-contrast stratification variable.

9. **He, S., et al.** *Computer-Vision Benchmark Segment-Anything Model (SAM) in Medical
   Images.* 2023. arXiv:2304.09324. https://arxiv.org/abs/2304.09324
   — GLM across 12 datasets: relative target size is the single most significant predictor
   of SAM Dice. Motivates size as a mandatory covariate in our regression.

10. **Cheng, D., et al.** *SAM on Medical Images: A Comprehensive Study on Three Prompt
    Modes.* 2023. arXiv:2305.00035. https://arxiv.org/abs/2305.00035
    — Jitter-scale sweeps; accuracy decreases with jitter scale. Prompt-side again.

11. **(Authors as listed on arXiv.)** *FNPC (False-Negative/Positive Correction with box
    position/size sensitivity analysis on ultrasound).* 2023. arXiv:2308.10382.
    https://arxiv.org/abs/2308.10382
    — Ultrasound box-sensitivity evidence + multi-box augmentation remedy; prompt-side.

## C. Context — prompt realism and GT quality (secondary framing)

12. **Antonov, A., Moskalenko, A., Shepelev, D., Krapukhin, A., Soshin, K., Konushin, A.,
    Shakhuro, V.** *RClicks: Realistic Click Simulation for Benchmarking Interactive
    Segmentation.* NeurIPS 2024 Datasets & Benchmarks. arXiv:2410.11722.
    https://arxiv.org/abs/2410.11722
    — The click-side realistic-prompt program; with BREPS, owns "realistic prompt
    evaluation". Cited to delimit what SeeingInside is *not* (we do not propose a prompt
    protocol; we audit evidence reliance under the existing one).

13. **(Authors as listed on arXiv.)** *Benchmarking Human and Automated Prompting in the
    Segment Anything Model (PointPrompt).* 2024. arXiv:2410.22048.
    https://arxiv.org/abs/2410.22048
    — Human-vs-automated prompt gap at 234K prompt-set scale; context for prompt-side
    literature saturation.

14. **Singh, M., et al.** *Benchmarking Object Detectors with COCO: A New Path Forward
    (COCO-ReM).* ECCV 2024. arXiv:2403.18819. https://arxiv.org/abs/2403.18819
    — COCO mask-quality diagnosis; reason boundary-F is secondary on COCO in our design.

---

## Deliberately NOT cited (and why)

- **Diffusion inpainting / generative editing papers.** The primary counterfactual
  instrument requires an off-the-shelf inpainter, but no inpainting paper appears in the
  Stage-3 verified list, and Windows4 policy forbids citing from memory. The tool will be
  selected and its citation added at run time, verified against the actual artifact used.
- **HalluSegBench / P107v lineage.** Referenced in this package only as *process facts*
  (Stage-4 Set-C scoop finding; Stage-6 no-merge ruling recorded in
  `selection_history/stage6_battle.md`), never as scientific support. SeeingInside makes no
  VLM-hallucination claim and does not build on that benchmark (proposal §23).
- **Everything else in `stage3_kill_sam_eval.md`** (RITM, FocSAM, GraCo, Semantic-SAM,
  SAMPOT, SAHI, Label Convergence, SAM-TTA, …) — verified but irrelevant to P14's claim;
  omitted to keep the related-work surface honest and minimal. One exception is allowed at
  writing time: the Stage-4 P101 review's multimask-selection confound is handled with the
  SAM paper itself (multimask design is documented there), requiring no extra citation.

## How each core citation is used in the proposal

| Citation | Role in SeeingInside |
|---|---|
| Kirillov et al. 2304.02643 | Architecture KNOWN FACTs; positional re-injection; multimask design; frozen weights |
| Stable-SAM 2311.15776 | Closest prior (prompt-side); expected R2 citation; differentiation §9 |
| BREPS 2601.15123 | "Priced-in" boundary on natural images; motivates medical-primary endpoint |
| RoBox-SAM 2407.21284 | Medical prompt-side sweeps; differentiation |
| MedSAM box-predictor 2606.04705 | Box-geometry prior evidence; MedSAM-arm EXPECTED direction |
| MedSAM 2304.12306 | The audited protocol (primary endpoint definition) |
| Mazurowski MedIA 2023 | Oracle-prompt formalization; cohort guide |
| Huang 2304.14660 | Contrast stratification variable |
| He 2304.09324 | Size covariate |
| Cheng 2305.00035, FNPC 2308.10382 | Prompt-side saturation; ultrasound arm context |
| RClicks 2410.11722, PointPrompt 2410.22048 | Scope delimitation vs prompt-realism program |
| COCO-ReM 2403.18819 | COCO GT-quality caveat |
