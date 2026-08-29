# Idea_01 — 相关文献（Literature）

**溯源标签。** `[S5-verified]` = 经 Stage-5 工程师于 2026-08-28 检索验证存在。`[S6-verified]` = 在 Stage-6 对抗性审查中发现或重新核实。`[inherited]` = 继承自 Stage-3/4 账本，未在 Stage 5/6 中独立重新核实。

> **本文件通篇执行的规则。** 未在 Windows7 的 Stage 1→6 会话中检索到的论文一律不予列入。仅阅读过摘要的文献均如实标注。我们绝不引用未曾见过的实验结果，也绝不杜撰会议/年份。下方标记为 `[inherited]` 的任何内容在进入投稿论文参考文献之前均应重新核实。

---

## 1. 偏差缓解文献 — 我们的动机来源，也是主要受攻击面

这些论文之所以存在，*是因为*该领域坚信 support 质量和类别偏差具有重要影响。但没有一篇文献测量过在彻底摧毁 support 后还能剩下多少准确率。

| 工作 | 实际所做工作 | 与本研究的关系 |
|---|---|---|
| **BAM** — Lang et al., CVPR 2022 (Oral). `github.com/chunbolang/BAM` `[S5-verified]` | 指出 FSS 中的基类偏差（base-class bias），并增加一个基类学习器分支进行抑制。 | 最强的"已知现象"攻击点（A6）。但 BAM 测量的是其*修复手段*在自研模型上的效果。我们测量的是跨评测面板在零假设模型下的残留效应。BAM 本身也*包含*在我们的评测面板中。 |
| **TBS** — AAAI 2024 `[inherited]` | 针对前景/背景偏差的缓解方案。 | 属于疗法（Treatment），而非诊断检验（Assay）。引用前需重新核实。 |
| **AENet** — ECCV 2024 `[inherited]` | 同一研究方向的缓解方案。 | 同上。引用前需重新核实。 |
| **Iterative modulation** — CVPR 2024 `[inherited]` | Support-query 交互精炼机制。 | 同一赛道。需重新核实。 |
| **Support dilution** — `arXiv:2501.13529` `[S6-verified, abstract]` | 扰动/稀释 support 质量作为构建新方法的手段。 | *操作手法*上最接近，但*研究目的*完全相反：他们劣化 support 是为了构建鲁棒性；我们摧毁 support 是为了测量其贡献份额。 |
| **SADe** — `arXiv:2607.24706` `[S6-verified, abstract]` | 同一赛道中具有 support 感知特性的方法。 | 存在相同的本质区别。 |

**为什么这一整列在论文中可以凝练为一句话。** 上述每一项工作都是一种*疗法（treatment）*。而我们是一套*诊断检验（diagnostic assay）*。该领域一直在开具处方，却从未测量过病灶本身究竟有多大。

---

## 2. 评测有效性文献 — 我们的意外盟友

| 工作 | 研究发现 | 为什么对我们至关重要 |
|---|---|---|
| **Open-V line**（在 `stage6_defense_brief.md` 中记录为 X2）`[S6-verified]` | 仓库间预处理空间的差异可导致 FSS 结果波动**高达 37 个百分点**。同时报告称，在标签不相交的词表上，*随着基础模型文本先验的减弱，support 的贡献相应增加*。 | 带来两项利好：(1) 它揭示了绝对 FSS 数值不可信，从而使我们的*比率*统计量具有更高的价值 —— 保持率无需精确复现任何人的绝对数字。(2) 反过来看，"先验强时 support 作用小"正是独立研究团队从相反方向观察到的我们所提出的假设。将其作为引证支撑；它让我们的立论成为非推测性的严谨前提，而非单纯的唱反调。 |

这也解释了为什么 `experiments.md` 中的 E5（原生评测器 vs 统一共享评测器）获得了算力支持：它以零边际算力成本将一项方法论攻击（A5）转化为了论文的第二头条结论，因为无论如何我们都必须重新运行每个 checkpoint。

---

## 3. 被审计的评测面板

全部在 Stage 5 期间（2026-08-28）验证了存在性。`KNOWN FACT` **存在性已验证并不等同于适用性已验证** —— 第 1 天的门禁（E0）将重新下载并对所有内容进行哈希校验。

| 方法 | 代码仓库 / 来源 | 模型家族 | 风险等级 |
|---|---|---|---|
| PFENet | `github.com/dvlab-research/PFENet` `[S5-verified]` | specialist | low — 提供 8 个预训练模型 |
| HSNet | `github.com/juhongm999/hsnet` `[S5-verified]` | specialist | **Google Drive checkpoints — 链接失效风险** |
| BAM | `github.com/chunbolang/BAM` `[S5-verified]` | specialist | **OneDrive checkpoints — 链接失效风险** |
| Matcher | `github.com/aim-uofa/Matcher`, ICLR 2024 `[S5-verified]` | foundation, training-free | low |
| PerSAM | `github.com/ZrrSkywalker/Personalize-SAM` `[S5-verified]` | foundation, training-free | low |
| FSSAM | `github.com/Sam1224/FSSAM`, ICML 2025 `[S5-verified]` | foundation, SAM2-based | low |
| SegGPT | HF `SegGptForImageSegmentation` `[S5-verified]` | foundation | low |
| SAM / SAM2 | `facebookresearch` 官方 `[S5-verified]` | — (Floor-A) | low |
| **SAM3-exemplar** | 官方发布, HF-gated `[S6-verified]` | foundation | **在 Stage 6 追加** —— 必须在第 1 天申请访问权限 |

---

## 4. SAM3 与学术时效钟

`EVIDENCE` SAM3 于 2025 年 11 月发布（`arXiv:2511.16719`）；SAM 3.1 于 2026 年 3 月发布 `[S6-verified]`。SAM3 实现了基于样例提示的概念分割 —— 而图像样例**本质上就是** support。

这促成了 Stage 6 对本项目最重要的一处修正（攻击点 A1）：以 2020–2022 年专有模型为中心的审计面临着沦为"博物馆批判"的风险。修复成本低廉且已融入设计 —— 增加一个 SAM3-exemplar 臂，使**基础模型时代的保持率成为并列头条结论**，专有模型降级为历史对照组。在 2026 年，真正有价值的问题不是 PFENet 是否使用了它的 support，而是 SAM3 是否使用了。

---

## 5. 数据集

| 数据集 | 承担角色 | 备注 |
|---|---|---|
| PASCAL-5i (VOC2012 + SBD) | 标准 FSS 基准 | 此处的 `S3` 分层样本较少 |
| COCO-20i (COCO 2014) | **主要的 `S3` 承载数据集** | 实例级标注天然提供了分层信息 |
| LVIS-92i | 高密度多目标场景 | Matcher 所采用的数据集 `[S5-verified]` |
| FSS-1000 | `S4` 退化对照组 | 在构建时*结构上就限定为*单一居中目标 —— 正是其关键特征 |
| MSD / AMOS CT 切片 | 泛化性探针 | 仅用于免训练方法 |

许可证情况：VOC/SBD/COCO/LVIS/FSS-1000 均采用标准科研许可证。无需标注预算、无需付费凭证数据、无需 API 调用开销。

---

## 6. 评审员可能引用的文献及对应回应位置

| 可能的引用文献 | 攻击角度 | 回应方案与位置 |
|---|---|---|
| BAM (CVPR 2022 Oral) | "基类偏差和前景偏差早已是已知现象。" | `proposal.md` §7 + §22/A6：作为*疗法目标*是已知的，但从未作为相对于零假设模型的份额进行测量，也从未进行过分层。 |
| TBS / AENet 2024 年浪潮 | "社区已经修复了该问题。" | 同上。它们的存在构成了我们的动机章节；一个修复方法并不会报告其在整个评测面板上所修复问题的具体体量。 |
| SAM3 / `arXiv:2511.16719` | "你们审计的是过时的模型。" | §22/A1：增设 SAM3-exemplar 臂，设立基础模型时代并列头条结论。 |
| 指标/评测改革相关文献 | "又一篇单纯的评测论文。" | 交付物是一套实体产物 —— 带有冻结 episode 和反事实列表的富含干扰物的数据集划分 —— 而非空洞观点。 |

---

## 7. 待结清的验证债务

在此如实记录而非刻意隐藏：

1. TBS (AAAI 2024)、AENet (ECCV 2024) 以及 CVPR 2024 迭代调制条目被标记为 `[inherited]` —— **在将其编入参考文献之前，必须重新核实发表会议、年份与实际内容。**
2. `arXiv:2501.13529` 与 `arXiv:2607.24706` 仅在**摘要层面**进行了阅读。
3. Open-V / X2 的 "37 points" 属于该研究组报告的 `EVIDENCE`，非由我们亲测，引用时应注明出处并重新通读原始文献。
