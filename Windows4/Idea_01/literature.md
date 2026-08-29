# SeeingInside — 文献引用（仅经验证的引用）

**引用政策（具约束力，依据 Windows4 主管账本及 Stage-7 说明）：**
以下每一项条目均出现在 `Windows4/selection_history/stage3_kill_sam_eval.md` 中（Stage-3 先前工作审查员于 2026-08-28 检索并完整阅读了摘要与相关章节），或者是 SAM 论文本身（Kirillov et al.）。**本包中任何位置均未引用其他论文。** 当提案需要某种在列表中无对应论文的工具时（例如扩散 inpainter），仅对该工具进行泛化命名，并将其引用推迟至实际运行阶段 —— 详见 §刻意未引用的文献。

---

## A. 核心文献 — 本项目所填补的因果空白（Stage-3 Cluster 2）

1. **Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., Girshick, R.**
   *Segment Anything.* ICCV 2023. arXiv:2304.02643. https://arxiv.org/abs/2304.02643
   — 架构层面的 KNOWN FACT 来源：ViT 图像编码器、prompt 编码器、轻量掩码解码器；在解码器交叉注意力的每一层，位置编码都会被重新注入到图像 embedding 一侧（论文 + 开源的 `segment-anything` 代码）。这一架构事实解释了为何单独的流形外消融无法确定对图像证据的依赖程度（R2 attack iii），以及为何仅 prompt 的零假设在技术上是完全可测量的。

2. **Fan, Q., Tao, X., Ke, L., Ye, M., Zhang, Y., Wan, P., Wang, Z., Tai, Y.-W., Tang, C.-K.**
   *Stable Segment Anything Model.* 2023. arXiv:2311.15776. https://arxiv.org/abs/2311.15776
   — “首个在不同 prompt 质量下对 SAM 分割稳定性进行的全面分析”；定位了在劣质 prompt 下掩码解码器所关注的图像特征机制。**图像固定下的 Prompt 端干预** —— 这是预计 Reviewer #2 会引用的相邻但方向不同的先前工作。我们将该干预方向进行了反转。

3. **Moskalenko, A., Kuznetsov, N., Dudko, V., Iasakova, A., Boldyrev, T., Shepelev, D., Spiridonov, T., Kuznetsov, B., Shakhuro, V.**
   *BREPS: Bounding-Box Robustness Evaluation of Promptable Segmentation.* 2026. arXiv:2601.15123. https://arxiv.org/abs/2601.15123
   — 真实用户边界框分布、针对边界框位置的逐像素 IoU 热力图、最坏情况现实边界框搜索、15 个模型 × 10 个数据集、相比紧密边界框协议出现约 30% 的 IoU 下降。确立了：(i) 输出是边界框坐标的陡峭函数，(ii) 紧密边界框协议高估了自然图像上的实际部署质量。界定了我们显著性论证必须跨越的“已被预期（priced-in）”边界 —— 这正是我们将主要终点设在医学图像上的原因。

4. **Huang, Y., et al.** *Robust Box Prompt based SAM (RoBox-SAM).* MICCAI MLMI 2024. arXiv:2407.21284. https://arxiv.org/abs/2407.21284
   — 跨 5 种医学模态、对 99,299 张图像进行的 0–30% 系统性边界框偏移扫描；低质量边界框下的注意力漂移分析。同样属于：扰动 prompt，保持图像不变。

5. **(Authors as listed on arXiv.)** *Enhancing MedSAM with a Lightweight Box Predictor.* 2026. arXiv:2606.04705. https://arxiv.org/abs/2606.04705
   — 记录了使用边界框微调的 MedSAM 解码器“学会了预期”边界框几何形状，且预测框会对不规则病灶施加刚性矩形约束。这是关于边界框几何先验的观察性证据；支持了我们的 EXPECTED 结果，即 MedSAM 可由零假设达到的比例将高于 base SAM。

## B. 被审计的评测协议 — 紧密边界框医学评估

6. **Ma, J., et al.** *Segment Anything in Medical Images (MedSAM).* Nature Communications 2024. arXiv:2304.12306. https://arxiv.org/abs/2304.12306
   — 我们的主要终点所重新审视的基于边界框 prompt 的医学评测协议：即在零图像证据下，能够达到 MedSAM 协议边界框 prompt Dice 的多大比例。

7. **Mazurowski, M. A., et al.** *Segment anything model for medical image analysis: an experimental study.* Medical Image Analysis 2023. https://doi.org/10.1016/j.media.2023.102918
   — 形式化了 SAM 在医学影像中的 "oracle performance"；证明了 prompt 模拟主导了评测结果；分析了目标尺寸与性能之间的关系。为医学图像队列的选择提供了指引。

8. **Huang, Y., et al.** *Segment Anything Model for Medical Images?* Medical Image Analysis 2024. arXiv:2304.14660. https://arxiv.org/abs/2304.14660
   — 跨医学基准按尺寸/对比度分层的 SAM 失效分析；边界框抖动敏感性。低对比度分层变量的来源。

9. **He, S., et al.** *Computer-Vision Benchmark Segment-Anything Model (SAM) in Medical Images.* 2023. arXiv:2304.09324. https://arxiv.org/abs/2304.09324
   — 跨 12 个数据集的广义线性模型（GLM）：相对目标尺寸是 SAM Dice 最显著的单一预测指标。促使我们将尺寸作为回归模型中的强制协变量。

10. **Cheng, D., et al.** *SAM on Medical Images: A Comprehensive Study on Three Prompt Modes.* 2023. arXiv:2305.00035. https://arxiv.org/abs/2305.00035
    — 抖动尺度扫描；准确率随抖动尺度增加而下降。同样属于 Prompt 端研究。

11. **(Authors as listed on arXiv.)** *FNPC (False-Negative/Positive Correction with box position/size sensitivity analysis on ultrasound).* 2023. arXiv:2308.10382. https://arxiv.org/abs/2308.10382
    — 超声图像上的边界框敏感性证据 + 多框增强补救措施；Prompt 端研究。

## C. 背景文献 — Prompt 真实感与 GT 质量（次要框架）

12. **Antonov, A., Moskalenko, A., Shepelev, D., Krapukhin, A., Soshin, K., Konushin, A., Shakhuro, V.** *RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation.* NeurIPS 2024 Datasets & Benchmarks. arXiv:2410.11722. https://arxiv.org/abs/2410.11722
    — 点击端的现实 prompt 研究；与 BREPS 一同构成了“现实 prompt 评估”领域。引用此文献旨在界定 SeeingInside *不是*什么（我们不提出新的 prompt 协议；我们在现有协议下审计其对图像证据的依赖性）。

13. **(Authors as listed on arXiv.)** *Benchmarking Human and Automated Prompting in the Segment Anything Model (PointPrompt).* 2024. arXiv:2410.22048. https://arxiv.org/abs/2410.22048
    — 在 23.4 万 prompt 规模下测算的人工与自动化 prompt 差距；为 prompt 端文献的饱和现状提供了背景。

14. **Singh, M., et al.** *Benchmarking Object Detectors with COCO: A New Path Forward (COCO-ReM).* ECCV 2024. arXiv:2403.18819. https://arxiv.org/abs/2403.18819
    — COCO 掩码质量诊断；在我们的实验设计中 boundary-F 在 COCO 上作为次要指标的原因。

---

## 刻意未引用的文献（及原因）

- **扩散修复（Diffusion inpainting）/ 生成式编辑论文。** 主要的反事实工具需要现成的 inpainter，但在 Stage-3 验证列表中并未包含任何 inpainting 论文，且 Windows4 政策严禁凭记忆添加引用。该工具将在运行时选定并补全引用，与实际使用的产物进行严格核对。
- **HalluSegBench / P107v 系列。** 在本包中仅作为*流程事实*提及（Stage-4 Set-C 撞车发现；Stage-6 不合并裁决记录于 `selection_history/stage6_battle.md`），绝不作为科学支撑。SeeingInside 不提出任何关于 VLM 幻觉的主张，也不基于该基准构建（提案 §23）。
- **`stage3_kill_sam_eval.md` 中的其他所有文献**（RITM, FocSAM, GraCo, Semantic-SAM, SAMPOT, SAHI, Label Convergence, SAM-TTA 等）— 虽经验证，但与 P14 的主张无关；予以略去以保持相关工作部分的严谨与精炼。论文撰写时允许一个例外：Stage-4 P101 评审提出的多掩码选择混淆问题可通过 SAM 论文本身处理（多掩码设计已在其中记录），无需额外引用。

## 提案中对各项核心引用的具体使用方式

| 引用文献 | 在 SeeingInside 中的定位与作用 |
|---|---|
| Kirillov et al. 2304.02643 | 架构 KNOWN FACT；位置编码重新注入；多掩码设计；冻结权重 |
| Stable-SAM 2311.15776 | 最相近的先前工作（Prompt 端）；预期的 R2 引用；差异化论述 §9 |
| BREPS 2601.15123 | 自然图像上的“已被预期”边界；促使设立医学图像主要终点 |
| RoBox-SAM 2407.21284 | 医学 Prompt 端扫描；差异化论述 |
| MedSAM box-predictor 2606.04705 | 边界框几何先验依据；MedSAM 分支的 EXPECTED 方向 |
| MedSAM 2304.12306 | 被审计的评测协议（主要终点定义） |
| Mazurowski MedIA 2023 | Oracle-prompt 形式化；队列选择指南 |
| Huang 2304.14660 | 对比度分层变量 |
| He 2304.09324 | 尺寸协变量 |
| Cheng 2305.00035, FNPC 2308.10382 | Prompt 端饱和度背景；超声分支背景 |
| RClicks 2410.11722, PointPrompt 2410.22048 | 相比于 prompt-realism 计划的范围界定 |
| COCO-ReM 2403.18819 | COCO GT 质量注意事项 |
