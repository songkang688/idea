# Stage 4 → 候选者（Windows1）—— R2 评审组记录已找回

状态：**事后重建。完整的 Reviewer #2 评审组记录已找回。**

`research_ledger/stage4_reviewer2.md` 是一份约 1.1 KB 的摘要，并声称完整评审组记录位于
"on branch cursor/reviewer2-stage4-kill-panel-5733 (cloud worktree, **not this repo**)"。
**该括号内的陈述是错误的。** 该分支就在本仓库中，且评审组记录 —— 21,207 字节，
包含全部 12 个提案及其完整攻击结构 —— 已从中找回。

---

## 1. 找回记录

**评审组记录已找回。** 出处信息：

| 字段 | 取值 |
|---|---|
| 分支 | `origin/cursor/reviewer2-stage4-kill-panel-5733` |
| 该分支上的路径 | `research_ledger/stage4_reviewer2_kill_panel.md` |
| Blob | `edeaccb6a431c460e93a0e207b378839a82cf7ab`（21,207 字节） |
| Commit | `c77a907e5d210d768d909b897e5dbdbd46da36a5`，"Add Stage 4 Reviewer #2 kill panel for 12 segmentation/VFM proposals", Fri Aug 28 2026 |
| 标题行 | `# Stage 4 — Reviewer #2 Kill Panel (Windows1 PI)` |

归属于 Windows1 在三处独立考量上均非常确凿：标题写着 "Windows1 PI"；分支后缀 `5733` 与 `research_ledger/stage4_reviewer2.md` 中的 `Source: bc-90c313c0-0076-59a0-a25e-0727cdb45733` 行吻合；且该评审组的 Top-7 清单以相同的顺序和相同的七个 ID 完全复现了摘要中的 R2 Top-7。

**该分支仅包含两个文件** —— `README.md` 与该评审组记录 —— 因此它是一个纯评审组分支，从未被合并。这正是该记录在 `main` 上缺席的原因。本回填**不**合并该分支或将该记录复制进 `research_ledger/`；而是在此对其建立索引并进行总结，使 `research_ledger/` 保持原样。

### 检索的分支，以及各自实际包含的内容

有四个分支被指名可能包含 Stage-4 评审组素材。**只有其中一个包含。**

| 分支 | 裁决 | 实际内容 |
|---|---|---|
| `cursor/reviewer2-stage4-kill-panel-5733` | **Windows1 评审组 —— 已找回** | `research_ledger/stage4_reviewer2_kill_panel.md`，标题为 "(Windows1 PI)"，P1–P12 与 Windows1 的 SEG-/VFM- ID 吻合 |
| `cursor/stage4-cluster-a-reviewer2-f1fa` | **非 Windows1** | `stage3_cluster_A_*` 与 `stage4_cluster_A_*`（攻击、decisions.csv、keep、killed） |
| `cursor/stage4-cluster-b-reviewer2-b25a` | **非 Windows1** | `stage4_cluster_B_*` |
| `cursor/stage4-cluster-c-reviewer2-c1be` | **非 Windows1** | `stage4_cluster_C_*` |

**三个簇分支属于不同窗口的 Stage 4，绝不能并入 Windows1。** 逐文件核查的证据：

- `stage4_cluster_A_keep.md` 与 `stage4_cluster_A_killed.md` 均带有表头 "**Reviewer #2 (Cloud Sub-Agent J) → Supervisor Windows7.**"。簇 B 点名了 "Cloud Sub-Agent K"。
- 其 ID 命名空间为 `A-0003`、`A-0016`、`B-0058`、`B-0062`、`C-0028`、`C-0090` … —— 带有连字符的簇字母方案，与 Windows1 的 `SEG-0001…0365`、`VFM-0001…0350`、`ASM-0001…0350` 或 `A0001…A0180` 命名空间**完全不相交**。
- 其主题与 Windows1 的漏斗不相关（SAM2 内存 FIFO 驱逐、MoE 路由作为病理检测器、多普勒音频监督、剂量图作为轮廓监督、维度坍缩、文本批次排练）。
- 其计数亦不符合 Windows1 的 Stage 4：簇 A 是 17 个中 7 个存活，B 是 20 个中 7 个，C 是 18 个中 7 个。Windows1 的 Stage 4 是 12 个提案且 1 个击杀。

这三个分支在其目录树中携带 `Windows1/` 与 `research_ledger/`，且具有与 `main` **逐字节一致的 blob 哈希** —— 它们仅仅是从已经合并了 Windows1 的提交切出的。这种继承性使得它们看起来相关，也是 `research_ledger/` 绝不能被重定位的原因（见 `LEDGER_INDEX.md` §4）。

---

## 2. 评审组结构

找回的评审组中的每个提案均按照固定的七部分模式进行评估，这使得下方的重构具有统一性而非印象化：

1. **拒稿理由（Rejection）** —— 苛刻评审人最强烈的单一反对意见
2. **隐含假设（Hidden assumption）**
3. **混淆因素（Confounder）**
4. **缺失基线（Missing baseline）**
5. **平凡替代方案（Trivial alternative）** —— 必须排除的低成本解释
6. **封嘴实验（Shut-me-up experiment）** —— 能使反对意见闭嘴的具体研究
7. **决策（Decision）** + **剩余致命缺陷（Remaining fatal flaw）**

评审组开篇即给出角色定位："苛刻的 CVPR/ICCV/MICCAI 评审人。每个提案先予以拒稿，随后评估是否有真实实验能拯救它。"

**沿用的认知警示。** 这些属于 REVIEWER JUDGMENT，与 `research_ledger/stage2_seg_review.md` 一致（"Scores are REVIEWER JUDGMENT not facts"）。下方的攻击并非关于任何方法的已证实事实，且没有"封嘴实验"被实际运行过 —— 最多属于 HYPOTHESIS / EXPECTED。**不存在 ACTUAL EXPERIMENTAL RESULT。**

### 评审组声称的引用

评审组列出了十篇声称"已与在线来源核对"的引用：Kumar/Ma/Liang 2020 (arXiv 2002.11361); Wang et al. 2022 (2204.08200); Li et al. HalluSegBench 2025 (2506.21546); Byrd & Lipton 2019 (1812.03372); Goh et al. Multimodal Neurons 2021 (distill.pub); Wortsman et al. WiSE-FT 2022 (2109.01903); Ramanathan et al. PACO 2023 (2301.01795); Pham et al. VAW 2021 (2106.09707); Cheng et al. Boundary IoU 2021 (2103.16562); Liu et al. GRES 2023 (2306.00968)。

将这些视为 **EVIDENCE-FROM-AGENT**，而非经本次回填核实 —— `stage3_priorwork_kill.md` 为本轮确立了该标准，此处不予放宽。

**评审组将其自身的一处引用标记为未解决**，原文："The 'ACL Findings 2025 one-generation NLP analog' cited by P1: **UNSURE which paper — must be pinned or dropped.**"。作为未决事项沿用；此处不作解决，在确证前不予引用。

---

## 3. 12 个候选者

`stage4_reviewer2.md` 将结果总结为 "KILL: P10 0193 replica-spiking (no transportable law). KEEP-IF-EXPERIMENT: all others. **No unconditional KEEP.**"。找回的评审组完全证实了这一点：11 个 KEEP-IF-EXPERIMENT，1 个 KILL，0 个无条件 KEEP。

| # | ID | 一句话假设 | Reviewer #2 裁决 | 理由来源 | 是否推进到 Stage 5？ |
|---|---|---|---|---|---|
| **P1** | SEG-0252 | 多代人机协同标注会使掩码约定发生漂移。 | KEEP-IF-EXPERIMENT | 评审组 P1 | **有争议。** 在 Stage 4 被廉价 killer 规则淘汰，随后保持在候选竞争中 —— 见 §5 |
| **P2** | SEG-0250 | 在频率匹配下，罕见物体*状态*比罕见*类别*造成更大损失。 | KEEP-IF-EXPERIMENT | 评审组 P2；R2 Top-7 第 3 名 | 是，随后在 Stage 6 被裁减 |
| **P3** | SEG-0275 | 知识截断后的概念名称能衡量真正的开放词表接地。 | KEEP-IF-EXPERIMENT | 评审组 P3 | 收缩为"仅限低成本随机词试点" |
| **P4** | SEG-0276-M | 逐类别先验形状场具有可迁移的证据／先验插值系数 α。 | KEEP-IF-EXPERIMENT —— "HRHR; killer experiment is inference-only (cheap)" | 评审组 P4；**R2 Top-7 第 1 名** | 是，但仅在 supervisor 修正后 —— 见 §5 |
| **P5** | SEG-0355-M | 所有现有打分都混淆了"未定义"与"不确定"。 | KEEP-IF-EXPERIMENT **(在当前主张强度下处于临界 KILL)** | 评审组 P5；R2 Top-7 第 4 名 | 不在 Stage-5 工程师 Top-5 中 |
| **P6** | SEG-0002-M | 边界抖动噪声底线会对报道的 SOTA 重新排序。 | KEEP-IF-EXPERIMENT —— "cheap and useful, but incremental" | 评审组 P6；R2 Top-7 第 5 名 | 不在 Stage-5 工程师 Top-5 中 |
| **P7** | SEG-0240-M | 采样 vs 重新加权的差距属于上下文统计，非优化问题。 | KEEP-IF-EXPERIMENT —— "an ML-theory paper in a CVPR costume" | 评审组 P7 | **否** —— "Dropped by cheap-killer rule: … 0240 factorial" |
| **P8** | SEG-0085-M | 病灶抑制是尺寸、对比度与增强强度的函数。 | KEEP-IF-EXPERIMENT —— "clinically important; **soften 'universal' to 'conditional law'**" | 评审组 P8；R2 Top-7 第 7 名 | **是 → Idea_02** |
| **P9** | SEG-0285 | 图像内文本通过读文本通路重定向掩码。 | KEEP-IF-EXPERIMENT —— "cheap, likely to work, limited ceiling" | 评审组 P9；**R2 Top-7 第 2 名** | **有争议** —— 审计员将其裁减；见 §5 |
| **P10** | SEG-0193-M | 测试集复制注入产出因果 ΔmIoU 曲线。 | **KILL** —— "replica injection is not a transportable law; metric artifact" | 评审组 P10；**唯一的 Stage-4 KILL** | **否** |
| **P11** | SEG-0103/0125-M | UDA 放大指数 vs GDA 理论；自训练轮换停止规则。 | KEEP-IF-EXPERIMENT —— "high risk of negative, but cheap to test" | 评审组 P11；R2 Top-7 第 6 名 | 不在 Stage-5 工程师 Top-5 中 |
| **P12** | VFM-0263/0274 | 在保持 SA-1B 可提示性的约束下微调 SAM 能够胜过 WiSE-FT 插值。 | KEEP-IF-EXPERIMENT —— "method paper; must strictly dominate WiSE-FT interpolation" | 评审组 P12 | **是 → Idea_01** |
