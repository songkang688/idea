# Stage 6 — 研究团队决战答辩 (精炼版，Windows4)

角色轮转已由 Stage 3 刺客评审 + Stage 4 R2 (三位独立拒绝评审员) 覆盖。绝无虚假共识。

## 明确保留的未决分歧

- Set A 希望将 P14 与 P107v 合并；Set C 发现 **P107v 已被抢发** (HalluSegBench)。主管判定：**do not merge**。P14 保持仅限视觉的反事实分析 (*框内像素*的 inpaint/swap)，而非 VLM 幻觉。
- 针对第三个席位的 P063 vs P103：玻璃物理光学具有更高的上限但渲染成本更高；烟雾迁移拥有公开数据且具备一周内可完成的 killer 实验。**第三席位 = AlphaSmoke。** P063 作为备选。
- 针对 PEFT 席位的 P065 vs P107：P107 更偏向“建设性机制”，但波及面较小。**P065 作为 PEFT 核心论文**；P107 作为消融实验章节。

## 终结相关主线的致命缺陷

HalluSegBench 抢先发表；提示领域的 RClicks/BREPS；仅微调解码器领域的 Gu et al.；提示切片领域的 MedSAM-2；SAM-alpha 预测头领域的 Matting Anything。

## 遗留的决定性实验 (必须严格按此顺序运行)

1. P082 噪声下限包络 (1–2 GPU-days) —— 若“遗忘”实为阈值效应，**调整 Idea_02 的研发重心 (pivot Idea_02)**
2. P14 框内流形上图像修复 (on-manifold inpaint) vs 仅提示 vs 框填充 (CPU/GPU，冻结 SAM)
3. P103 线性探测 / 微型头部 (linear-probe / tiny-head)：真实烟雾 mIoU 上抠图预训练编码器 vs COCO-seg 编码器

决战答辩终止条件：Stage 4 中除已被我们消化的 HalluSegBench 之外，未出现新的致命先前工作。
