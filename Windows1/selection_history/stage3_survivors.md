# Stage 3 → 存活者（Windows1）—— 重建

状态：**事后重建。** Windows1 保留了两份 Stage-3 *击杀*清单，但从未写出一份 Stage-3 存活者清单。本文件通过对那两份清单的反推导出存活者集合。

来源（除此外无其他）：
- `research_ledger/stage3_priorwork_kill.md` —— SEG 切片（5 KILL / 4 SURVIVE / 11 MUTATE）
- `research_ledger/stage3_vfm_kills.md` —— VFM 切片（4 KILL / 8 MUTATE / 1 WEAK SURVIVE）
- 来自 `research_ledger/stage1_seg_keepers.md`、`research_ledger/stage1_vfma_asma_keepers.md`、`research_ledger/stage1_vfm_local_pool.md` 的一句话假设
- "是否推进？"一列与找回的 Stage-4 评审组记录核对（见 `stage4_candidates.md`）

认知标签遵循 `Windows1/README.md`。每行都是*决策记录*，绝非测量值。
`stage3_priorwork_kill.md` 携带自身警示，适用于下文每项基于引用的击杀：
"citations claimed web-verified; still treat 2025–2026 items as **EVIDENCE-FROM-AGENT** until re-checked in final packages."

在任何总账文件中均无支撑文本的行盖戳 **`NO RECORDED REASON — 需人工确认`**。
本文件中没有任何裁决理由是编造的。

---

## 1. 记分牌

| 切片 | KILL | MUTATE | SURVIVE | WEAK SURVIVE | 决策单元 | 存活者 |
|---|---|---|---|---|---|---|
| SEG (`stage3_priorwork_kill.md`) | 5 | 11 | 4 | 0 | **20** | **15** |
| VFM/ASM (`stage3_vfm_kills.md`) | 4 | 8 | 0 | 1 | **13** | **9** |
| 合计 | 9 | 19 | 4 | 1 | **33** | **24** |

**KNOWN FACT。** SEG 切片恰好包含 20 个决策单元，精确复现了 `Windows1/research_summary.md` 中的 "Stage 3 | ~20 attacked" 行。13 个 VFM/ASM 单元似乎**未**被计入那个"约 20"中。记录于 `FUNNEL_DEVIATION.md` §2。

**KNOWN FACT。** 24 个存活者进入了 Stage-4 边界，但 Stage-4 评审组仅攻击了 12 个。被淘汰的 12 个单元在 §4 中逐项列出；大部分没有记录理由。

---

## 2. SEG 切片 —— 存活者

裁决数值与 `stage3_priorwork_kill.md` 中完全一致。"领地排名"是该文件自身的已排序列表 "## Current top scientific territory" (1–10)；破折号表示该 ID 不在其中。

| ID | 一句话假设 | Stage-3 裁决 | 领地排名 | 理由来源 | 是否推进到 Stage 4？ |
|---|---|---|---|---|---|
| **SEG-0252** | 人机协同标注会在世代间放大标注约定惯例（标签生态学）。 | SURVIVE | 1 | `stage3_priorwork_kill.md`；假设来自 `stage1_seg_keepers.md` Top-30 | **是** —— 评审组 P1 |
| **SEG-0250** | 在频率匹配时，罕见的*物体状态*相比罕见的*类别*导致更大的精度损失。 | SURVIVE | 2 | `stage3_priorwork_kill.md` 领地 #2 "matched-frequency state-tail vs class-tail" | **是** —— 评审组 P2 |
| **SEG-0275** | 知识截断点之后的概念名称可在无污染情况下测试开放词表接地（时间留出）。 | SURVIVE | 3 | `stage3_priorwork_kill.md`；`stage1_seg_keepers.md` Top-30 | **是** —— 评审组 P3 |
| **SEG-0285** | 图像内的印刷文本能在物理上重定向掩码，而不仅是字幕。 | SURVIVE **(weak)** | 9 | `stage3_priorwork_kill.md` 标注为 `0285(weak)` 且领地 #9 "physical typographic injection moving masks" | **是** —— 评审组 P9 |
| **SEG-0276** | 逐类别先验形状场通过可迁移系数 α 与局部证据插值，并与 SAM 提示敏感性产生交互。 | MUTATE | 4 | `stage3_priorwork_kill.md` 领地 #4 | **是** —— 评审组 P4 |
| **SEG-0355** | "未定义"与"不确定"被混淆：现有头部上的单调打分无法区分它们。 | MUTATE | 5 | `stage3_priorwork_kill.md` 领地 #5 | **是** —— 评审组 P5 |
| **SEG-0002** | 人类边界抖动构成了噪声底线；减去它可对报道的 SOTA 重新排序。 | MUTATE | 6 | `stage3_priorwork_kill.md` 领地 #6；`stage1_seg_keepers.md` Top-30 | **是** —— 评审组 P6 |
| **SEG-0240** | 采样 vs 重新加权的差距是一项上下文统计机制，而非优化假象。 | MUTATE | 7 | `stage3_priorwork_kill.md` 领地 #7 | **是** —— 评审组 P7 |
| **SEG-0085** | 去噪／SR 管线对微小低对比度病灶的抑制是增强强度的函数。 | MUTATE | 8 | `stage3_priorwork_kill.md` 领地 #8；`stage1_seg_keepers.md` Top-30 | **是** —— 评审组 P8 → **Idea_02** |
| **SEG-0193** | 测试集复制注入可产出因果 ΔmIoU 虚高曲线。 | MUTATE | 10 | `stage3_priorwork_kill.md` 领地 #10 | **是** —— 评审组 P10（随后成为整轮唯一的 Stage-4 KILL） |
| **SEG-0103 / SEG-0125** *(合并单元)* | 0103：无监督域适应的走／停统计量。0125：在第 1 轮即可读出的自训练误差放大定律。 | MUTATE | — | 在 `stage3_priorwork_kill.md` 中记录为单一单元 `0103/0125`；假设来自 `stage1_seg_keepers.md` Top-30 | **是** —— 评审组 P11（"UDA amplification exponent vs GDA theory; churn stopping rule"）承载了前后两半 |
| **SEG-0019** | 边界幻觉是缺乏证据的：遮蔽局部证据依然能产出高置信度轮廓。 | MUTATE | — | 裁决已记录；**其后续消失无理由** | **否** —— `NO RECORDED REASON — 需人工确认` |
| **SEG-0054** | 可见度之前的烟雾可从时间闪烁光谱中检测。 | MUTATE | — | 裁决已记录；**其后续消失无理由** | **否** —— `NO RECORDED REASON — 需人工确认` |
| **SEG-0031** | `NO RECORDED HYPOTHESIS` —— 0031 在 `stage1_seg_keepers.md` Top-30 中缺席，仅作为 `0031(P)` 出现在 Stage-2 提升列表中。 | MUTATE | — | 裁决已记录；假设文本与后续处置均缺席 | **否** —— `NO RECORDED REASON — 需人工确认` |
| **SEG-0122** | `NO RECORDED HYPOTHESIS` —— 0122 仅出现在 Stage-2 被低估提升列表中。 | MUTATE | — | 裁决已记录；假设文本与后续处置均缺席 | **否** —— `NO RECORDED REASON — 需人工确认` |

### SEG 切片 —— Stage 3 被击杀项（为完整性列出）

全部五项均有记录在案的 prior-work 理由，且全部在 `Windows1/selection_history/eliminated_ideas_summary.md` 中得到独立证实。依据源文件自身的警示，将这些引用视为 EVIDENCE-FROM-AGENT。

| ID | 一句话假设 | 记录的击杀理由 | 在 eliminated_ideas_summary 中证实？ |
|---|---|---|---|
| SEG-0074 | 用浸润概率场替代硬轮廓。 | 既有工作：MRI–病理概率图 + 患者级校准已经存在 | 是 —— "SEG-0074 original" |
| SEG-0206 | 水印／Logo 可学习性作为数据集病理。 | ImageNet-W；水印学习往往本身就是*设计目标* | 是 |
| SEG-0185 | 冻结稠密探针以约 1% 算力预测微调排名。 | LogME / OTCE-seg | 是 |
| SEG-0046 | 将烟雾作为光密度回归，而非二值掩码。 | SMOKE+ / 去雾 / AAAI 2022 透射率引导烟雾 | 是 —— "SEG-0046 framing" |
| SEG-0113 | 从无标签数据流预测部署 mIoU。 | Bar CVPRW 2022 / AutoEval / SPE | 是 |

**部分复活说明（EVIDENCE）。** 这五项中有两项后来由 `research_ledger/meta_audit.md` 以*变异*形态复活："revive 0046 as transmittance-vs-binary hypothesis (not 'framing paper')" 以及 "revive 0074 only as cross-stain calibration of disagreement fields"。`meta_audit.md` 亦记录了 supervisor **拒绝**更宽泛的主张："REJECTS: treating 0074 original as wrongly killed — original form IS published (RAPSODI/calibration). Only mutation survives."。SEG-0074-M 随后演变为 **Idea_03 DisagreeShift**。因此 Stage-3 击杀项通过明确收敛的变异产出了一项入围方案，总账对该复活的限制异常清晰。

---

## 3. VFM / ASM 切片 —— 存活者

裁决完全按 `stage3_vfm_kills.md` 记录。一句话假设来自 `stage1_vfma_asma_keepers.md`（A 命名空间）与 `stage1_vfm_local_pool.md`（VFM 命名空间）。

| ID | 一句话假设 | Stage-3 裁决 | 记录的变异方向 | 是否推进到 Stage 4？ |
|---|---|---|---|---|
| **VFM-0263 / VFM-0274** | 0263：在 SA-1B 可提示性下降 < ε 的约束下最大化目标 Dice。0274：将保留 SA-1B AMG 质量与 COCO 微调作为双重目标。 | MUTATE *(写作 `A0263` —— 命名空间错误，见下文)* | "HQ-SAM Table 9 already measured drop; WiSE-FT is the α dial; need retention BENCHMARK + method that beats WiSE-FT" | **是** —— 评审组 P12 → **Idea_01** |
| A0051 | 可提示分割器中的编码器／解码器探针差距。 | MUTATE | "prompt-conditioned credit assignment" | **否** —— `NO RECORDED REASON — 需人工确认` |
| A0028 | 跨提示分歧预测误差。 | MUTATE | "cross-modality (not within-type) disagreement" | **否** —— `NO RECORDED REASON — 需人工确认` |
| A0166 | SA-1B / 评测近重复泄漏。 | MUTATE | "SA-1B stats as audit not hypothesis" | **否** —— `NO RECORDED REASON — 需人工确认` |
| A0121 | 冻结 vs 微调的数据规模交叉点 n\*。 | MUTATE | "crossover + a priori selector" | **无评审组席位，但确实继续推进了。** 见 §5 —— 它以 "Frozen/tuned crossover law" 重现于 `meta_audit.md` Top-8 #2，并在 Stage-5 工程师 Top-5 #2 中重现为 "Frozen/tuned n\*"。记录的最终死因：`eliminated_ideas_summary.md` "Frozen/tuned n\* \| Selector circularity; worst cost-to-kill"。 |
| A0153 | 线性映射对齐 CLIP patch 特征与 DINOv2 空间对应性。 | MUTATE —— 标注为 "**BEST VFM crack**" | "linear CLIP-patch→DINOv2 correspondence" | **否。** 存在记录的原因：被 prior work 击杀 —— `eliminated_ideas_summary.md` "VFM-A0153 \| CLIP-DINOiser / ProxyCLIP / Platonic Representation Hypothesis"，`evolution_summary.md` 将 "linear CLIP→DINOv2 as lead (Platonic / CLIP-DINOiser)" 列在击杀项中。注意反转：Stage 3 评分最高的 VFM 项在未到达 Reviewer #2 的情况下死亡。 |
| A0073 | 分布偏移下的 Prompt-tuning vs LoRA。 | MUTATE | "vision instantiation" | **否** —— `NO RECORDED REASON — 需人工确认` |
| A0021 | 针对稠密预测的过度训练小模型 vs Chinchilla 最优模型。 | MUTATE | "ride public grids only" | **否** —— `NO RECORDED REASON — 需人工确认` |
| A0109 | 随机种子与划分方差超过已发表的方法差值。 | **WEAK SURVIVE** | （无记录） | **否** —— `NO RECORDED REASON — 需人工确认`。注意主题与 SEG-0002-M（评审组 P6）重叠，后者的评审组文本将"训练种子方差"列为必需基线；A0109 是否被吸收进该项**未有记录**。 |

### VFM 切片 —— Stage 3 被击杀项

| ID | 一句话假设 | 记录的击杀理由 | 在 eliminated_ideas_summary 中证实？ |
|---|---|---|---|
| A0022 | 针对交互式分割的最坏情况*有效*点击序列。 | TETRIS | 是 —— "VFM-A0022 \| TETRIS AAAI 2024" |
| A0168 | Oracle 点击模拟相对于人类点击存在泄漏。 | RClicks | 是 —— "VFM-A0168 \| RClicks 2024" |
| A0077 | 通过 SVD 截断的有效 LoRA 秩。 | PARA | 是 —— "VFM-A0077 \| PARA / AdaLoRA" |
| A0148 | ViT 中的离群／高范数 token 重归一化。 | Registers | 是 —— "VFM-A0148 \| DINOv2 registers" |

**记录在案的合并复活（EVIDENCE）。** A0022 与 A0168 单独在此被杀，随后被重组：`meta_audit.md` 指示 "merge worst-case clicks with oracle-click leak" 并将结果列为 Top-8 #7 "Worst-case/oracle-click interactive eval merge"。它进入了 Stage-5 工程师 Top-5（#5, "Interactive eval merge"），随后在 Stage 6 死亡 —— `eliminated_ideas_summary.md`："Interactive eval merge \| Occupied by TETRIS + RClicks"，即最终被击杀了其两个母项的相同两篇论文所击杀。
