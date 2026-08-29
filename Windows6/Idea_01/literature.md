# Idea_01 —— 文献（只收已核实的条目）

**本文件的取材规则。** 一个条目只有在它已经存在于
`selection_history/literature_anchors.md` 或本文件的原始版本中时才可以出现在
这里 —— 也就是说，只有当某个 Stage-3/4 agent 真的做过网页检索时才收。没有任何
一条是凭记忆添加的。凡论证需要某个引用、而它无法与那两个来源核对上的地方，
该位置写的是 `CITATION NEEDED — 待人工核验`，而不是一个猜出来的引用。

**我们不声称重跑过任何人的表格。** 每个条目都是 **VERIFIED
PRIOR WORK**，其含义是"有记录表明它被检索过、并被用来杀掉或变异某个
想法"，而不是"被复现过"。

---

## A. 核心 —— 本项目所占据的那处空缺

| 论文 | 年份 | 会议／ID | 与本课题的关系 |
|---|---|---|---|
| Segment Anything | 2023 | ICCV | 定义了 AMG，即本研究对象 |
| SAM2 CT review | 2024 | arXiv 2408.11210 | 黑箱式的 CT 评测。它在 `literature_anchors.md` 里被归入 *"Remaining-novelty targets"*，正因为它**不是**一项 AMG-vs-聚类的检验 |
| SAM/SAM2 low-contrast CT | 2024 | arXiv 2408.04212 | **最接近的邻近工作。** 它确立了对强度／窗宽窗位的依赖性；被 Reviewer #2 引用。它展示的是敏感性而非等价性，而且没有做任何纹理对照 |

**空缺（FACT，原样沿用自本文件的原始版本）：** *"no AMG vs
k-means Hungarian/ARI study with texture-vs-intensity counterfactuals."*
Stage-3 新颖性信心 **0.6** —— Windows6 中最高的。

## B. 约束我们能主张什么

| 论文 | 年份 | 会议／ID | 它施加的约束 |
|---|---|---|---|
| HQ-SAM | 2023 | NeurIPS, arXiv 2306.01567 | 掩码质量精修。长期约束：**我们不主张"滤波器 = HQ-SAM"。** 那种表述属于邻近的 `F-012`，而 `stage2_ABCF_summary.md` 明确禁止重述它 |
| SAMRefiner | 2025 | arXiv 2502.06756 | 同一族；精修不是机制 |
| MedSAM 相关的 CT 笔记 | 2024 | arXiv 2408.03322 | 基准背景，被 Reviewer #2 作为 MedSAM 式表述引用 |
| MedSAM TTA without parametric updates | 2025 | arXiv 2504.02008 | 适配相关背景。按 `proposal.md` §23 属于范围之外 —— 适配不是我们的研究对象 |
| Metrics Reloaded | 2024 | Nature Methods | 指标选择的纪律。**正是这篇论文杀掉了同胞想法 `F-022`**，因为后者报告的是一条近乎定义性的性质。它在这里作为长期警告，防止我们犯同样的错 |

## C. 投稿前需要人工核验的位置

以下没有一条能与 `literature_anchors.md` 或原始 `literature.md` 核对上，
因此没有一条被标注年份、会议或 ID。

| 用在何处 | 位置 |
|---|---|
| SLIC 超像素（空间对照，§13） | `CITATION NEEDED — 待人工核验` |
| Otsu / multi-Otsu 阈值化 | `CITATION NEEDED — 待人工核验` |
| Adjusted Rand Index（Hubert & Arabie 或等价文献） | `CITATION NEEDED — 待人工核验` |
| Hungarian / Kuhn–Munkres 分配算法 | `CITATION NEEDED — 待人工核验` |
| Boundary-F / 轮廓 F-measure 协议 | `CITATION NEEDED — 待人工核验` |
| TotalSegmentator 数据集 | `CITATION NEEDED — 待人工核验` |
| Medical Segmentation Decathlon (MSD) | `CITATION NEEDED — 待人工核验` |
| COCO（E4 对照） | `CITATION NEEDED — 待人工核验` |

这些全都是标准内容，几乎肯定很容易补上。它们被有意留空：一个凭记忆
重建、看起来合理的 bibtex 条目比一个看得见的空洞更糟，因为空洞会被
去核查，而条目不会。

## D. 有意不引用的工作，以及原因

| 工作 | 为什么被排除 |
|---|---|
| SAM-U (arXiv 2307.04973), UR-SAM (arXiv 2311.10529) | 提示抖动做不确定性。Stage 3 用它们**杀掉**了 `prompt-jitter-uncertainty`；与我们的机制主张无关 |
| RITM (arXiv 2102.06583), Stable Segment Anything (ICLR 2025) | 交互式点击行为。杀掉了 `multiclick-nonmonotonic` 那个想法；不是我们的研究对象 |
| LN-TTA (WACV 2026), IGTTA (IEEE TMI 2025) | 测试时适配；杀掉了 `F-014` |
| KiTS23 (arXiv 2309.02001), Randomized Histogram Matching (arXiv 2104.14032) | 强度对齐式的域适应；杀掉了 `histogram-matching-da`。与我们的强度主题邻近，但问题不同 —— 他们是去*修*强度偏移，我们是去*诊断*强度依赖性 |
| LoRA vs Full Fine-tuning (arXiv 2410.21228) | PEFT；杀掉了 `lora-effective-rank`。属于不同的簇 |
| Mehrtash et al. (IEEE TMI 2020) | Dice-vs-CE 校准；杀掉了 `dice-vs-ce-calibration` |

把这些列出来是有意义的：一个看到 SAM 不确定性文献没被引用的评审可能会
以为我们不知道这些工作。它们其实被检索过，并且是被有意排除的。

## E. 每条核心引用在论证中的用法

- **arXiv 2408.04212** 既是让我们的假设显得可信的那篇论文，*也是*最接近
  抢先它的那篇。`proposal.md` §9 明确写出了差别：它证明了窗宽窗位敏感性；
  它没有拿聚类器去检验等价性，也没有做任何强度／纹理的解离实验。
- **arXiv 2408.11210** 被引用是为了确立"SAM 系列模型在 CT 上的评测是黑箱式的"
  这一点 —— 而这恰恰就是一项机制性研究要填的空缺。
- **Segment Anything (ICCV 2023)** 只被引用来给出 AMG 的定义。我们不对
  SAM 的设计意图作任何主张。
- **Metrics Reloaded** 是在指标选择那一节里被防御性地引用的，
  因为同胞想法正是死在这一点上。
- **HQ-SAM / SAMRefiner** 被引用是为了圈开 `F-012` 那种表述。
