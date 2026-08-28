# References — B-0114: Prompts as Registers (annotated, with verification labels)

Labels: **[verified 2026-08-28]** = URL confirmed by live web search during package drafting (Agent W)
or carried from a pipeline-stage live fetch this cycle; **[in-record]** = surfaced by a pipeline
agent's live search this cycle (H Stage-4 / L Stage-6 audits) and carried in the repo record.
No invented citations: everything below entered the record through a logged search.

## Mandatory citation set (binding — every outward document cites all of these)

1. **Visual Prompt Tuning.** Menglin Jia, Luming Tang, Bor-Chun Chen, Claire Cardie, Serge Belongie,
   Bharath Hariharan, Ser-Nam Lim. ECCV 2022. arXiv:2203.12119 — https://arxiv.org/abs/2203.12119
   **[verified 2026-08-28]**
   *Role:* the method under study. **Fig. 11** (Prompt-Fixed vs Prompt-Learned vs Linear, classification
   only) is the ablation that struck the original B-0114 pilot (PI_BINDING.md; L audit Finding 1) and is
   this project's E0 bug-detector control: "the final performance of VPT is mainly contributed by the
   learned prompt embeddings instead of the enlarged sequence length."

2. **Vision Transformers Need Registers.** Timothée Darcet, Maxime Oquab, Julien Mairal,
   Piotr Bojanowski. ICLR 2024. arXiv:2309.16588 — https://arxiv.org/abs/2309.16588
   **[verified 2026-08-28]**
   *Role:* the register phenomenon — high-norm artifact tokens in low-information patches corrupt
   *spatial* feature maps; dedicated register tokens absorb the global computation. The reason Fig. 11
   may not generalize to dense prediction; source of the DINOv2-with-registers sibling checkpoints.

3. **DA-VPT: Semantic-Guided Visual Prompt Tuning for Vision Transformers.** Li Ren, Chen Chen, Liqiang
   Wang, Kien Hua. CVPR 2025. arXiv:2505.23694 — https://arxiv.org/abs/2505.23694 (CVF:
   https://openaccess.thecvf.com/content/CVPR2025/papers/Ren_DA-VPT_Semantic-Guided_Visual_Prompt_Tuning_for_Vision_Transformers_CVPR_2025_paper.pdf)
   **[verified 2026-08-28]**
   *Role:* the connection in print. Its §Artifact Consideration observes Darcet-style artifacts in VPT
   prompt attention maps, calls registers "analogous to learnable prompts," and defers "the nature and
   impact of these artifacts on model performance" to future investigation — the sentence this project
   answers. Cited up front per H's survival condition.

4. **Vision Transformers Don't Need Trained Registers.** Nick Jiang, Amil Dravid, Alexei A. Efros,
   Yossi Gandelsman. NeurIPS 2025 (Spotlight). arXiv:2506.08010 — https://arxiv.org/abs/2506.08010
   (code: https://github.com/nickjiang2378/test-time-registers) **[verified 2026-08-28]**
   *Role:* arm-(c) construction — register neurons identified and their activations shifted into an
   untrained token/slot, training-free; also the competitor mechanism (register function as attention
   geometry) H requires this project to disaggregate.

5. **Do All Vision Transformers Need Registers?** arXiv:2603.25803 — https://arxiv.org/html/2603.25803
   **[in-record]** (surfaced by H Stage-4 live search)
   *Role:* cross-architecture reassessment of register need; scopes which backbones our claims
   generalize to.

6. **A Unifying View of Attention Sinks.** arXiv:2606.08105 — https://arxiv.org/html/2606.08105v1
   **[in-record]** (surfaced by L Stage-6 audit live search)
   *Role:* splits register/sink function into **NOP vs broadcast** mechanisms with concrete diagnostics
   on DINOv2-reg. Mandatory readout axes per L Finding 1 — "a B-0114 execution that does not adopt the
   NOP/broadcast diagnostic axes will look coarse at review time."

7. **Vision Transformers with Self-Distilled Registers (PH-Reg).** Yinjie Chen, Zipeng Yan, Chong Zhou,
   Bo Dai, Andrew F. Luo. NeurIPS 2025 (Spotlight). arXiv:2505.21501 —
   https://arxiv.org/abs/2505.21501 (code: https://github.com/0raiser0/PH-Reg)
   **[verified 2026-08-28]**
   *Role:* post-hoc registers via self-distillation (E6 patched-pair option); documents that artifact
   behavior is not exhausted by high-norm tokens — the reason norm statistics are never our primary
   signature axis (confound §21.3).

8. **DINOv2: Learning Robust Visual Features without Supervision.** Maxime Oquab, Timothée Darcet, et al.
   arXiv:2304.07193 — https://arxiv.org/abs/2304.07193 (repo:
   https://github.com/facebookresearch/dinov2) **[verified 2026-08-28]**
   *Role:* the register-free backbone; the repo distributes both the vanilla and with-registers ViT-B/14
   checkpoints used as the killer grid's sibling pair.

9. **DINOv3.** Oriane Siméoni, et al. arXiv:2508.10104 — https://arxiv.org/abs/2508.10104
   **[verified 2026-08-28]**
   *Role:* register-equipped by default — primary evidence for the seat's obsolescence clock (roadmap
   §26 R3).

## Supporting set

10. **SINDER: Repairing the Singular Defects of DINOv2.** Haoqi Wang, Tong Zhang, Mathieu Salzmann.
    ECCV 2024. arXiv:2407.16826 — https://arxiv.org/abs/2407.16826 **[in-record]**
    *Role:* artifact direction is weight-determined — relevant to why frozen-random tokens may fail to
    attract sink mass even when learned ones do.

11. **Efficient Streaming Language Models with Attention Sinks (StreamingLLM).** Guangxuan Xiao,
    Yuandong Tian, Beidi Chen, Song Han, Mike Lewis. ICLR 2024. arXiv:2309.17453 —
    https://arxiv.org/abs/2309.17453 **[verified 2026-08-28]**
    *Role:* provenance of the attention-sink concept the register literature builds on.

12. **An Image is Worth 16x16 Words (ViT).** Alexey Dosovitskiy, et al. ICLR 2021. arXiv:2010.11929 —
    https://arxiv.org/abs/2010.11929 **[verified 2026-08-28]**
    *Role:* substrate architecture.

13. **LoRA: Low-Rank Adaptation of Large Language Models.** Edward J. Hu, et al. ICLR 2022.
    arXiv:2106.09685 — https://arxiv.org/abs/2106.09685 **[verified 2026-08-28]**
    *Role:* weight-side PEFT contrast — the register question is specific to token-based PEFT.

14. **AdaptFormer: Adapting Vision Transformers for Scalable Visual Recognition.** Shoufa Chen, et al.
    NeurIPS 2022. arXiv:2205.13535 — https://arxiv.org/abs/2205.13535 **[in-record]**
    *Role:* adapter-side PEFT contrast.

## Datasets & benchmarks

15. **ADE20K / Scene Parsing through ADE20K.** Bolei Zhou, et al. CVPR 2017. arXiv:1608.05442 —
    https://arxiv.org/abs/1608.05442 (site: https://groups.csail.mit.edu/vision/datasets/ADE20K/)
    **[verified 2026-08-28]** — killer benchmark (E1).

16. **The Cityscapes Dataset for Semantic Urban Scene Understanding.** Marius Cordts, et al. CVPR 2016.
    arXiv:1604.01685 — https://arxiv.org/abs/1604.01685 **[verified 2026-08-28]** — E5, exp_02.

17. **Indoor Segmentation and Support Inference from RGBD Images (NYU Depth v2).** Nathan Silberman,
    Derek Hoiem, Pushmeet Kohli, Rob Fergus. ECCV 2012 —
    https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html **[verified 2026-08-28]** — E5 depth task.

18. **The Visual Task Adaptation Benchmark (VTAB).** Xiaohua Zhai, et al. arXiv:1910.04867 —
    https://arxiv.org/abs/1910.04867 **[verified 2026-08-28]** — E0 classification-control suite style.

## Freshness obligations (see literature.md §13)

Re-search at proposal freeze and experiment freeze; kill trigger = a printed register-mechanism paper
with dense-task token arms; exp_02's own stop = any paper selling the norm map as per-pixel
uncertainty. Additions to this file must carry a verification label and fetch date.
