# A-0028 — Annotated References

All URLs live-verified 2026-08-28 (packaging session). BibTeX in `references.bib`. The **mandatory
citation set** (battle-locked at Stage 6) is marked ★. Scoop re-search addenda get appended here,
dated, at experiment freeze and submission freeze (`roadmap.md` Section 26, C2).

## Subject models

- **SAM2** — Ravi et al., "SAM 2: Segment Anything in Images and Videos," 2024.
  [arXiv:2408.00714](https://arxiv.org/abs/2408.00714) · [code](https://github.com/facebookresearch/sam2).
  Primary subject. Streaming memory bank + memory attention; the arbitration under measurement lives
  in this mechanism. SAM2.1-L is the killer-battery subject.
- **SAM3** — Carion et al., "SAM 3: Segment Anything with Concepts," 2025.
  [arXiv:2511.16719](https://arxiv.org/abs/2511.16719) · [code](https://github.com/facebookresearch/sam3).
  Second-generation subject; memory-based video tracker retained, so the identical probe applies →
  first controlled generational comparison of memory behavior (E5).

## The distractor-fix line (the papers that presuppose the arbitration) ★

- ★ **DAM4SAM (CVPR 2025)** — Videnović, Lukežič, Kristan, "A Distractor-Aware Memory for Visual
  Object Tracking with SAM2." [arXiv:2411.17576](https://arxiv.org/abs/2411.17576) ·
  [CVPR open access](https://openaccess.thecvf.com/content/CVPR2025/papers/Videnovic_A_Distractor-Aware_Memory_for_Visual_Object_Tracking_with_SAM2_CVPR_2025_paper.pdf) ·
  [project](https://jovanavidenovic.github.io/dam-4-sam/) · [code + DiDi](https://github.com/jovanavidenovic/DAM4SAM).
  Documents distractor drift; partitions memory (RAM/DRM); ships DiDi. Fix philosophy #1: curate
  appearance-memory content. Subject model in E6.
- ★ **DAM4SAM extended** — Videnović et al., "Distractor-Aware Memory-Based Visual Object Tracking,"
  2025. [arXiv:2509.13864](https://arxiv.org/abs/2509.13864). Journal-style extension (13 benchmarks;
  EfficientTAM/EdgeTAM integrations). **This is the arXiv ID carried in the battle-locked claim** —
  same line as 2411.17576; both cited.
- ★ **SAMURAI** — Yang, Huang, Chai, Jiang, Hwang, "SAMURAI: Adapting Segment Anything Model for
  Zero-Shot Visual Tracking with Motion-Aware Memory," 2024.
  [arXiv:2411.11922](https://arxiv.org/abs/2411.11922) · [code](https://github.com/yangchris11/samurai).
  In-print claim that SAM2 "tends to prioritize appearance similarity over spatial and temporal
  consistency" — anecdotal evidence base (Fig. 1), Kalman motion prior + gated memory selection.
  Fix philosophy #2: explicit location/motion prior. Joined the mandatory set at Stage-6 Round 5
  (fourth kill attempt → citation obligation). Subject model in E6.
- ★ **SAM2/SAM3 memory-design study** — Alansari, Naseer, Al Marzouqi, Javed, Werghi, "Rethinking
  Memory Design in SAM-Based Visual Object Tracking," 2025.
  [arXiv:2512.22624](https://arxiv.org/abs/2512.22624) · [code (SAM3 Tracking Zoo)](https://github.com/HamadYA/SAM3_Tracking_Zoo).
  Re-implements SAM2-era memory designs on SAM3; ten-benchmark evaluation; hybrid short-term
  appearance + long-term distractor-resolving memory. Fix philosophy #3: partition by function.
  Closest adjacent work AND fastest-moving absorb risk; its zoo is reusable harness for E6.

## Memory-tracking lineage and design space

- **XMem** — Cheng & Schwing, ECCV 2022. [arXiv:2207.01578](https://arxiv.org/abs/2207.01578).
  Atkinson–Shiffrin multi-store VOS memory; pre-SAM lineage.
- **Cutie** — Cheng et al., CVPR 2024. [arXiv:2310.12982](https://arxiv.org/abs/2310.12982).
  Object-level memory reading, distractor-motivated.
- **KeepTrack** — Mayer et al., ICCV 2021. [arXiv:2103.16556](https://arxiv.org/abs/2103.16556).
  Distractor-aware association pre-SAM: the appearance-vs-location tension is a decade-old axis.
- **SAM2Long** — Ding et al., ICCV 2025. [arXiv:2410.16268](https://arxiv.org/abs/2410.16268).
  Training-free memory tree for long video.
- **HiM2SAM** — Chen, Sun, Li, Qin, Benini. [arXiv:2507.07603](https://arxiv.org/abs/2507.07603).
  Hierarchical motion estimation + memory optimization for long-term tracking.
- **SAMITE** — Xu, Zhu, Liu, Lin, Long, Li, Zhao. [arXiv:2507.21732](https://arxiv.org/abs/2507.21732).
  Prototypical memory bank with a **position-wise anchor** + positional pseudo-prompts —
  live-verified this session as a *fourth* fix-paper presupposing the arbitration
  (see `literature.md` Section 12 addendum).
- **EfficientTAM** — [arXiv:2411.18933](https://arxiv.org/abs/2411.18933);
  **EdgeTAM** — [arXiv:2501.07256](https://arxiv.org/abs/2501.07256). Efficiency variants shown (in
  2509.13864) to benefit from memory redesign — the instrument's future customer base.

## Methodology

- **Psychometric fitting** — Wichmann & Hill, *Perception & Psychophysics* 63:1293–1313, 2001.
  [DOI:10.3758/BF03194544](https://doi.org/10.3758/BF03194544).
- **Wilson interval** — Wilson, *JASA* 22:209–212, 1927.
  [DOI:10.1080/01621459.1927.10502953](https://doi.org/10.1080/01621459.1927.10502953).
- **Poisson image editing** — Pérez, Gangnet, Blake, SIGGRAPH 2003.
  [DOI:10.1145/1201775.882269](https://dl.acm.org/doi/10.1145/1201775.882269).
- **Object permanence probing** — Shamsian et al., ECCV 2020.
  [arXiv:2003.10469](https://arxiv.org/abs/2003.10469).

## Datasets

- **COCO** — Lin et al. [arXiv:1405.0312](https://arxiv.org/abs/1405.0312) — donor objects.
- **LVIS** — Gupta et al. [arXiv:1908.03195](https://arxiv.org/abs/1908.03195) — rare-category donors.
- **DAVIS 2017** — Pont-Tuset et al. [arXiv:1704.00675](https://arxiv.org/abs/1704.00675) — backgrounds.
- **MOSE** — Ding et al. [arXiv:2302.01872](https://arxiv.org/abs/2302.01872) — crowded backgrounds.
- **LVOS** — Hong et al. [arXiv:2211.10181](https://arxiv.org/abs/2211.10181) — long-video context.
- **DiDi** — distractor-distilled set, [DAM4SAM repo](https://github.com/jovanavidenovic/DAM4SAM) —
  external anchor (E7).

## Scoop-search log

- **2026-08-28 (packaging session, Agent V):** all URLs above re-verified live; no controlled
  teleport/swap dissociation probe found; SAMURAI/DAM4SAM/2512.22624 remain fix-papers presupposing
  the arbitration. New finding this pass: SAMITE (2507.21732) is a **fourth** presupposing fix-paper
  (position-wise memory anchor + positional pseudo-prompts; no dissociation measurement) — added to
  the citation set, wedge strengthened, absorb-risk trend confirmed. Consistent with the Stage-5 (N),
  Stage-6 (Q Fight 2), and Stage-6 (S Round 5 Part B) searches. Next mandatory re-search: experiment
  freeze (week one, day 5).
