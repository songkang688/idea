# Stage 6 —— 研究组对抗（battle）与 Final-3 锁定裁决（事后重建 / RETROSPECTIVE RECONSTRUCTION）

- **Windows ID：** Windows6
- **分支：** `cursor/windows6-research-idea-evolution-b55d`
- **重建日期：** 2026-08-29（UTC）
- **基线提交：** `0c25df6`（W6-T1 落地 `stage5_top5.md` 之后紧接的那次提交）
- **任务：** W6-T2（Windows6 三个收尾任务中的第二个：T1 → T2 → T3）
- **文档类型：** **RETROSPECTIVE / 补记。**

## 0. 本文件闭合了什么，以及它不是什么

**FACT。** `Windows6/README.md` 带着一条悬置的状态行：*"Provisional Final 3 packaged; **Stage 5/6 still confirming** against DE-top10 assassin + auditor."*。本文件的存在就是通过给出一份明确的 5 → 3 裁决以及一份明确的**锁定／暂定（locked / provisional）**结论（§5），来终结那个悬挂着的"still confirming"。

**FACT —— 这也是本文件中最重要的免责声明。** **Windows6 中从未发生过任何 Stage-6 辩论事件。** 没有任何产物记录过一场辩论、一次投票或一个评审小组。Windows6 实际拥有的是**四次独立的 rejector 环节**，各自有记录来源：

| Rejector 环节 | 产物文件 | 范围 |
|---|---|---|
| Stage-3 廉价 killer prior-work 刺客 | `stage3_prior_work_kill_cheap.jsonl`（12 条裁决） | A–F 廉价簇 |
| Stage-3 DE 前 10 刺客 | `stage3_DE_top10.json.md`（10 条裁决） | D+E 医学／VLM 分支 |
| Stage-4 Reviewer #2 | `stage4_reviewer2_cheap5.jsonl`（5 条裁决） | cheap-5 |
| 元审计员（Stage 2 vs Stage 3 调和） | `auditor_overlay.md` | 各梯队之间的冲突 |

本文件**依据这四次有记录的环节进行裁决**。它不凭空发明第五个评审人、评审小组、投票数或任何产物未点名的角色。当这四次环节发生冲突时，冲突保留在 §4 中，而不是被抹平成虚假共识。

**范围边界（硬边界）：**

- **不**修改 `Idea_01/`、`Idea_02/`、`Idea_03/` —— package 的加厚属于 **W6-T3**。
- **不**修改任何 `stage1_pool/` / `stage2*` / `stage3*` / `stage4*` 文件，也不修改 `stage5_top5.md`。
- **不**修改 `README.md`、`research_summary.md` 或 `supervisor_log.md` —— 状态调和属于 **W6-T3**。
- **不**重新评审 Reviewer #2 杀掉的两条。它们的理由仅作抄录，不予重新争论。

### 证据分级图例

与 `stage5_top5.md` 采用同一套标准：**FACT**（存在于 Windows6 产物中）· **VERIFIED PRIOR WORK**（由 Stage-3/4 agent 检索并用于杀掉／变异的外部论文；表格未重跑）· **HYPOTHESIS**（待检验主张）· **SPECULATION**（*本*文档作出的推断）· **EXPECTED RESULT**（预先注册的预测趋势）· **ACTUAL RESULT**（实际运行产出的数字）。

**FACT。** Windows6 拥有 **0 个 ACTUAL RESULTS**。`README.md` 将各 package 标为 *"no real SAM numbers" / "no smoke mAP" / "no VLM eval"*；`Idea_02/proposal.md` 写道 *"We have not trained a detector here."*。§6 中的每个成本数字都是 **HYPOTHESIS**。

**本文件执行的引用规则：** 外部论文**仅在**它们已出现在 `literature_anchors.md` 或某个 `Idea_0*/literature.md` 中时才可被引用。未添加任何新参考文献。

---

## 1. 5 → 3 裁决

**FACT。** 输入为 `stage5_top5.md` §2 中重建的 Top-5，该内容本身是对 `stage4_reviewer2_cheap5.jsonl` 的原样抄录。

| # | Stage-4 ID | 原始编号 | 沿用的裁决 | 依据 | 结果 |
|---|---|---|---|---|---|
| 1 | `AMG-HU-clustering` | F-067 | **survive**，`advance: true` | R2 + Stage-3 保留（0.6） + 审计员受保护保留 | → **`Idea_01`**，§2.1 |
| 2 | `camera-ID-smoke` | F-043 | **survive**，`advance: true` | R2 + Stage-3 保留（0.55） + 审计员受保护保留 | → **`Idea_02`**，§2.2 |
| 3 | `empty-slice-FPR-Dice` | F-022（+F-074 重复） | **KILL** | Reviewer #2 | 线程终结，§1.1 |
| 4 | `alignment-tax-localization` | F-031 / E-009（+F-039） | **survive (mutated)**，`advance: true` | R2 + Stage-3 变异（0.5） + DE 保留 E-009（0.55） + 审计员受保护保留 | → **`Idea_03`**，§2.3 |
| 5 | `atlas-vs-CLIP-text` | F-036 / F-037 | **KILL** | Reviewer #2 | 线程终结，§1.1 |

计数：**3 个存活 / 2 个被杀。**

### 1.1 终结线程的致命缺陷（抄录，不重新评审）

**`empty-slice-FPR-Dice`（F-022 / F-074）—— KILL。** Reviewer #2 理由，字面引自 `stage4_reviewer2_cheap5.jsonl`：

> `Near-definitional Dice property; Metrics Reloaded; no leaderboard preds`

一行中包含三项独立的致死因素：该效应接近于 Dice 的定义性性质而非实证发现；**VERIFIED PRIOR WORK** Metrics Reloaded（Nature Methods 2024，`literature_anchors.md`）已经覆盖了指标选择的领域；且由于无法获取排行榜预测结果，该审计无法运行。**FACT：** 记录中仅有 `reason` —— **没有 `residual`，也没有 `advance` 字段** —— 即 Reviewer #2 没有给该想法留下任何拯救路径。这就是在这里区分 kill 与 mutate 的标志。

**`atlas-vs-CLIP-text`（F-036 / F-037）—— KILL。** Reviewer #2 理由，原文：

> `CLIP-Driven Universal Model ICCV 2023 one-hot ablation; substitution unidentifiable`

**VERIFIED PRIOR WORK：** CLIP-Driven Universal Model，ICCV 2023 —— 所提出的 one-hot 替换消融在该论文中已经存在，且按其设定方式，atlas-vs-text 替换是不可辨识的。**FACT：** 同样仅有 `reason`，没有 `residual`，没有 `advance`。

**FACT —— 审计员没有拯救其中任何一个。** `auditor_overlay.md` 没有将任何一个保护进 Final 3，并直接写出了优先规则：*"Reviewer #2 later **killed** F-022 empty-FPR audit and F-036/037 atlas-vs-text… Those auditor 'keeps' do **not** enter Final 3."*。该规则所掩盖的分歧保留在 §4.1。

---

## 2. 三个存活者的详细审视

### 2.1 `Idea_01` —— 在 CT 上 SAM AMG ≈ HU 强度聚类（F-067）

**科学问题。** SAM 在 CT 上的 Automatic Mask Generation 是在执行语义 objectness，还是在做过窗宽窗位处理后近似于 HU 空间中的聚类？

**可证伪假设（HYPOTHESIS，来自 `Idea_01/proposal.md`）。**
- **H1：** 在固定临床窗之后，在预先注册的 CT 子集上，Hungarian 匹配的平均 IoU(AMG, k-means) > IoU(AMG, SLIC)。
- **H2（因果）：** 保持边缘的强度重映射对 AMG 的改变量，大于具有相同边缘图、保持强度的纹理置乱。
- **H3：** H1 差距跨越 AMG 超参数网格和 2–3 个窗宽窗位是稳定的；若非如此，该发现为**设置假象** → kill 或变异。

**残余义务（FACT，字面引自 `stage4_reviewer2_cheap5.jsonl`）：**

> `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`

**未履行残余义务时的降级路径 —— 这是源文本明确规定的一种情况。** *"else evaluation note"* 这句话就是降级：若没有因果臂，该贡献不再是关于 AMG 在计算什么的机制性主张，而是变成报告一致性相关关系的 evaluation note。**FACT：** `Idea_01/reviewer_attacks.md` 给出了更严格的本地规则 —— *"If we cannot run the causal arm, **do not submit**."*。因此两个产物在严重度上存在分歧（降级 vs 扣下不发）；记录在 §4.4，此处不予裁决。

**最接近的既有工作（VERIFIED PRIOR WORK；仅引自 `literature_anchors.md` / `Idea_01/literature.md`）。**
- Segment Anything, ICCV 2023 —— 提供被测试的 AMG 定义。
- SAM2 CT review, arXiv 2408.11210 —— 黑箱 CT 评测；在 `literature_anchors.md` 中被归入 *"Remaining-novelty targets"*，正因为它**不是** AMG-vs-k-means 检验。
- SAM/SAM2 low-contrast CT, arXiv 2408.04212 —— 强度／窗宽窗位依赖性；被 Reviewer #2 引用。
- HQ-SAM, NeurIPS 2023, arXiv 2306.01567 —— 用于杀掉邻近的 F-012 滤波主张；`Idea_01/literature.md` 记录了 *"we do **not** claim filter=HQ"*。
- MedSAM-related CT notes, arXiv 2408.03322 —— 基准背景。

**FACT（记录在案的空缺）：** `Idea_01/literature.md` 写道 *"**Gap:** no AMG vs k-means Hungarian/ARI study with texture-vs-intensity counterfactuals."*。Stage-3 新颖性信心 **0.6** —— 整轮中最高。

**最大评审攻击与封嘴证据。** *"窗宽窗位制造出结论"*（`Idea_01/reviewer_attacks.md` 攻击 1）：由于窗宽窗位是单调强度映射，只跑一个窗可以通过预处理本身人为制造出 AMG ≈ 聚类的一致性。封嘴证据：**扫描 3 个临床窗并全部报告**（腹部 400/40、骨 2000/400、肺 −600/1500 或有记录的等价设置），并要求 H1 在 ≥2 个窗上成立。`Idea_01/proposal.md` 直接承认了这一点：*"The paper is the **counterfactual**, not the correlation."*。次要攻击及其明确应答：一致性 ≠ 机制 → H2 臂；k-means 是众多廉价基线之一 → 同时跑 Otsu、GMM、SLIC；指标挑选 → 预先注册 Hungarian IoU + ARI + boundary-F；*"SAM 在 CT 上表现差已知"* → 论文是机制，不是 Dice 表格；超参数脆弱性 → AMG `points_per_side` 网格。

**Death 条件（FACT，来自 `Idea_01/experiments.md` "Stop"）。**
- **KILL**：若在**全部窗**下 SLIC 与 AMG 的一致度 ≥ k-means。
- **KILL**：若纹理置乱对 AMG 的扰动幅度与强度重映射大致相当（H2 失败 —— 机制性主张按残余条款自身规定死亡）。
- **KILL**（Stage-5 门禁）：若 AMG 相比 k-means 更接近真值 **且** 纹理置乱大幅扰动 AMG。
- **PIVOT**：若仅单一窗显示聚类等价性（H3 失败 → 设置假象）。
- **KILL CT 特异性主张**：若 COCO 对照显示出相同的聚类等价性 —— 该效应便非 CT 特异。
- **CONTINUE**：仅当 H1 与 H2 在 ≥2 个窗和 ≥2 组 AMG 设置上成立。

### 2.2 `Idea_02` —— 烟雾／火焰上相机 ID vs 按事件划分的泄漏（F-043）

**科学问题。** 已发表的烟雾／火焰检测性能中有多少是相机熟悉度而非羽流检测 —— 以及*按事件划分*（当前最佳实践）到底是否充分？

**可证伪假设（HYPOTHESIS，来自 `Idea_02/proposal.md`）。**
- **H1：** camera-disjoint mAP < random-split mAP，差距大于种子标准差。
- **H2：** event-disjoint mAP ≠ camera-disjoint mAP（同相机不同事件的残余泄漏）。
- **H3：** 冻结 backbone 特征上的线性探针在留出时间划分上预测相机 ID 胜过随机水平。
- **H4：** 来自**训练集**相机的空（无烟）帧比来自未见过相机的空帧产生更高的假阳性率或置信度。

**残余义务（FACT，原文）：**

> `Need event-disjoint vs camera-disjoint gap plus empty-frame memorization probe`

**未履行残余义务时的降级路径。** 源文本对该项**没有**给出显式降级条款 —— 与 Idea_01 不同，没有 *"else …"*。产物给出的是一个两步后备阶梯，本文件如实抄录而非发明：
1. **记录在案的转向（FACT，`Idea_02/experiments.md`）：** *"**Pivot** to event-disjoint only if cameras < 10 (underpowered)."*。该转向放弃了 H2 —— 即区分本工作与 PYRONEAR 既有实践的核心主张。
2. **SPECULATION（本文档推断，如实标注）：** 若产出了 H2 差距但未产出 H4，论文无法区分地理偏移与背景记忆，将坍缩回 Voxel51 博客诊断。`Idea_02/proposal.md` 将等价门禁表述为 *"Fatal if we only report camera-disjoint drop without H4"* —— "fatal"，而非 "downgrade"。没有任何产物描述过存活的缩水形态。诚实的读法是 **Idea_02 没有记录在案的软着陆**：它要么完整成文，要么 kill。

**最接近的既有工作（VERIFIED PRIOR WORK；仅引自 `literature_anchors.md` / `Idea_02/literature.md`）。**
- PYRONEAR-2025，arXiv 2402.05349 —— 按事件划分 + pHash。既是最接近的工作也是靶子：贡献在于 event-disjoint ≠ camera-disjoint。
- Voxel51 Pyro-SDIS 审计，2026 博客 —— 记录为 *"diagnosis, **no** retrained mAP"*。**FACT：** `Idea_02/literature.md` 携带长期指令 *"Do not cite a peer-reviewed mAP inflation number we did not compute."*。本文件严格遵从：任何地方均未陈述虚高数字。
- SmokeFrames / Nemo —— 早期语料，标注 *"check camera IDs before use"*。

**最大评审攻击与封嘴证据。** *"相机身份不过是地理位置；你们重新测了一遍分布偏移，那不是新闻"*（`Idea_02/reviewer_attacks.md`：*"Confounder: camera = geography"*）。封嘴证据：**空帧记忆探针**（H4）。空帧中没有羽流，因此负样本上见过 vs 未见过的相机差距无法用羽流外观分布偏移解释；它是背景记忆。已在 `Idea_02/experiments.md` 中规定的配套对照：未在烟雾上训练过的 ImageNet 预训练 backbone 作为探针对照，在**事件**上聚类的 bootstrap，等 N、类别比例对齐划分，以及区分重复帧泄漏与相机签名的 pHash 去重重跑。次要攻击与明确应答：相对于博客的新颖性 → 重新训练并量化；相机数量 N 极小 → 多折叠 + 置信区间；充满噪声的 mAP → 3 个种子并报告 FAR。

**Death 条件（FACT，来自 `Idea_02/proposal.md` 与 `experiments.md`）。**
- **KILL**：若任何可用公开数据集上均无相机元数据（这是一项**前提条件**，见 §5 GATE-A）。
- **KILL**：若在按事件划分下按相机划分的降幅消失（H2 死亡 → PYRONEAR 已解决）。
- **KILL**：若相机 ID 探针处于随机水平（H3 死亡）。
- **KILL**：若仅有单一一组极小的相机可用。
- **PIVOT**：若相机数 < 10 则转向仅按事件划分。
- **STOP**（Stage-5 门禁）：若在种子噪声内 random ≈ camera-disjoint **且** 探针 ≈ 随机水平 **且** 无见过／未见过空帧 FPR 差距 —— 停止前用另外 2 个种子确认。
- **CONTINUE**：若 H1 与 H4 在 ≥2 个数据集上成立。

### 2.3 `Idea_03` —— 对齐后 VLM 中的定位税（F-031 / E-009, + F-039）

**科学问题。** 对齐（SFT → RLHF）是否会损害 VLM 的定位能力？如果是，*在哪个阶段*以及*在哪一部分* —— 解码策略还是视觉表征？

**可证伪假设（HYPOTHESIS，来自 `Idea_03/proposal.md`）。**
- **H1：** 在 ≥1 个公开 checkpoint 对上，受限框指标从 base → chat 下降。
- **H2：** 冻结视觉 token 上的线性探针**不**下降（代价在解码／格式）**或确实**下降（代价在表征） —— 分支本身就是结论。
- **H3（可选，因果）：** 纯文本偏好上的 LoRA DPO 依然损害 H1 → 责任在优化目标，而非图像数据配比。

**残余义务（FACT，原文）：**

> `Format-controlled eval + representation probe + small text-only DPO control`

**FACT：** 这是整轮中唯一带有**三个**合取条件的残余，分别对应不同的假设（H1 / H2 / H3）。它是三个存活者中最沉重的残余。

**未履行残余义务时的降级路径。** 此处产物异常清晰，因为 `Idea_03/experiments.md` 预先注册了三种产出：
- **O1** —— 似然打分下差距消失 → 代价属于**格式假象**；记录在案的指令为 *"write negative"*。这就是降级：一份关于格式的负结果，而非对齐税论文。
- **O2** —— 差距在似然下存活但探针保持完好 → **策略税**。
- **O3** —— 探针同样下降 → **表征税**。
- 若格式受控评测根本没跑，`Idea_03/proposal.md` 明确指出：*"**Kill** if H1 fails under constrained decoding (formatting confound)"* —— 且 DPO 臂明确被拦截在其后：*"Do not run DPO unless observational gap survives format control."*。因此降级阶梯为 O3 → O2 → O1(负结果) → kill，且 DPO 合取条件是**有前提的**，而非无条件的。

**最接近的既有工作（VERIFIED PRIOR WORK；仅引自 `literature_anchors.md` / `Idea_03/literature.md`）。**
- MDGD，EMNLP Findings 2025 —— 指令微调下的视觉遗忘。`Idea_03/proposal.md`：*"Visual forgetting under instruction tuning is **published**… Reviewer #2 killed the generic headline."*。
- TWIST & SCOUT，ICCV 2025 —— 接地／无遗忘微调；记录为最接近工作，*"we must cite them as attacks."*。
- RL-finetuned VLM robustness，2026，arXiv 2602.12506。
- LLaVA / LLaVA-RLHF 系列，2023–24 —— *"checkpoint pairs if licenses allow"*。
- **FACT（存活的空缺）：** `Idea_03/literature.md` 记录了 *"Stage 3: stage-isolated localization curve was NOT FOUND as a standalone paper (EVIDENCE GAP, conf ~0.5)."*。

#### 2.3.1 并行工作风险 —— 按要求单独处理

**FACT。** `README.md` 将 Idea_03 评为 *"Highest impact, highest concurrent-work risk."*。**FACT。** `stage3_DE_top10.json.md` 将 `E-009` 保留在置信度 **0.55**，并附备注 *"matched checkpoint localization tax still open"*。**FACT。** 廉价簇刺客独立将该想法打分为 **0.5**，剩余新颖性收缩为 *"Stage-isolated base vs SFT vs RLHF localization curve only"*。

综合阅读这三条：**通用大标题已不存在，剩下的是狭窄的残余切片。** 0.55 不是舒适的余量 —— 它是刺客在说该问题*依然*开放，即**截至检索日期**依然开放，而非在构造上必然开放。两项结构性加剧因素：

1. **SPECULATION（本文档）。** 残余新颖性由*缺席*定义（"NOT FOUND as a standalone paper"）。由缺席定义的新颖性随时间单调衰减，是在当下与投稿之间最容易被抢先的失效模式。对比 Idea_01（0.6 建立在*正向*结构性空缺上：无人跑过反事实臂）与 Idea_02（0.55 建立在*方法学*空缺上：博客未曾重新训练）。尽管 Idea_03 的置信度数字居中，其空缺是三者中最脆弱的。
2. **FACT。** 抢先者所需的唯一数字生成成本很低。`Idea_03/proposal.md` 将整体投入定为 *"Eval-only: 1 GPU, 1–2 days"*，`experiments.md` 定为 *"≤8 GPU-h"*。对我们成本低，对其他人同样成本低。

**package 中已有的缓解措施（FACT）。** 硬门禁 —— *"identical vision encoder + coordinate tokenization"* —— 是把此研究从"chat 模型得分更低"转化为阶段隔离主张的关键，也是防范被抢先的最强防线，因为未做 checkpoint 对齐的并行论文无法回答同一个问题。Reviewer #2 记录在案的指令强化了这一点：*"cite MDGD; we only claim stage+format isolation"*、*"do not claim causal RLHF without H3"*、*"box parsing ≠ localization: constrained decoding + probe"* 以及 *"Small N families: honest scope."*。

**风险裁决。** Idea_03 保留在 Final 3 中，但它是三者中**最可能被并行工作抢先的一个**，也是可行性前提条件核实最不充分的一个（§5 GATE-B）。其在执行顺序（§6）中的优先级相应放置：按依赖关系排在最后，但其便宜的前提检查排在最前，正因为未通过的门禁应在花 GPU 之前暴露，而非之后。

**Death 条件（FACT）。**
- **KILL**：若 H1 在受限解码下失效（下降属于格式混淆因素）。
- **STOP**：若对 1 **和** 对 2 的似然差距皆 ~0。
- **硬门禁**：没有具备相同视觉编码器与相同坐标 tokenization 的 checkpoint 对 → 阶段隔离主张完全不可行。
- **不跑** DPO 臂，除非观测差距经受住了格式控制。
- 在 O1 下**降级为负结果**。

---

## 3. 三个存活者的跨领域证据状态

**FACT。** 所有三项残余义务**均未履行**。没有任何实验被跑过：`Idea_01` 拥有合成 CPU 原型（`src/amg_intensity_equiv.py`），`Idea_02` 拥有划分模拟器加合成特征上的相机 ID 探针（`src/camera_split_audit.py`），`Idea_03` 拥有合成受限评测测试台（`src/format_controlled_box.py`）。**三者跨领域的 ACTUAL RESULT 计数：零。**

**FACT（package 深度，测量于基线提交 `0c25df6`）。** Windows6 的 `proposal.md` 大小在 Idea_01 / 02 / 03 中分别为 **2781 / 1330 / 987 字节**。分支 `cursor/windows4-research-idea-evolution-2962` 上的同名文件为 **29870 / 35997 / 24385 字节** —— 差距约为 **11× / 27× / 25×**。Windows6 的 `Idea_01/proposal.md` 甚至直接从带编号的 "§7–28" 标题跳到指向列表，即第 7 到 28 节声明了但不存在。**这是打包层面的不足，而非科学层面的不足** —— 底层的假设、门禁与停止规则全部具体存在。加厚属于 **W6-T3**；其对锁定裁决的影响在 §5 GATE-D 中说明。

---

## 4. 明确保留的未解决分歧

仅记录有记载的冲突。不重构任何产物未证明的辩论。

### 4.1 审计员保留 vs Reviewer #2 击杀 —— F-022, F-036/037

**FACT。** `auditor_overlay.md` 开篇即列出优先规则 *"Stage-3 named papers win collisions"* 并列出受保护的保留项，随后记录了 **Reviewer #2 后来杀掉了 F-022 空切片 FPR 审计与 F-036/037 atlas-vs-text**，得出结论 *"Those auditor 'keeps' do **not** enter Final 3."*。

**分歧是真实的，且仅通过先后顺序而非辩论得到解决。** 审计员在 Stage-2/3 调和中有理由保留这些线程；Reviewer #2 随后杀掉了它们。叠加意见通过时间／权威（"R2 在后，R2 胜出"）化解了冲突，而不是反驳审计员的依据（后者从未被重新陈述）。**SPECULATION：** 若 Reviewer #2 发生在审计员*之前*，叠加意见自己的优先规则并不显然会产生相同结果。**保持开放。此处不予重新争论** —— §0 禁止重新评审击杀项，本文件遵守该规定。

### 4.2 Stage-3 扩展项 vs Final 3 —— D-008、D-060、E-025 从未与存活者横向排名

**FACT。** `stage3_DE_top10.json.md` 结尾写道：*"Held as **extensions**, not Final 3: D-008, D-060, E-025."*。**FACT。** 没有任何一个出现在 `stage4_reviewer2_cheap5.jsonl` 中 —— **Reviewer #2 从未审视过它们。**

**FACT。** 按字面记录的 Stage-3 置信度数字，`D-008` 位于 **0.60**，与 Idea_01 的 0.6 持平，并高于 Idea_02 的 0.55 和 Idea_03 的 0.5/0.55。`D-060` 位于 **0.55**，与 Idea_02 持平。

**SPECULATION —— 以及防止过度解读上一行的一条重要警示。** 那些置信度来自**两次不同的刺客运行**（DE 前 10 环节与廉价簇环节），没有任何证据表明两个尺度之间经过了对齐校准。因此这种对比是*具提示性的，而非严格有效的*。这恰恰就是问题所在：**产物中不包含一套能证明 Final 3 胜过扩展项的公共尺度**，因为 —— 依据 `stage5_top5.md` §1 —— 两个 Stage-3 分支从未在 20 档相遇。这是形成 §5 裁决的最大单一输入。

### 4.3 同一想法得出了两个不同的 Stage-3 裁决标签

**FACT。** 定位税线程被评判了两次：廉价簇刺客在 0.5 给出 `mutate`（`alignment-tax-vlm-localization`）；DE 刺客在 0.55 给出 `keep`（`E-009`）。同一个底层问题，两个标签，两个置信度，没有产物对其进行调和。`auditor_overlay.md` 合并了 ID（*"F-031/E-009"*）但未处理裁决分歧。方向上兼容 —— 两者都让它存活 —— 但该轮从未为其最高影响力的想法产出单一权威的 Stage-3 裁决。

### 4.4 Idea_01 的残余要求有多硬 —— 降级还是扣下不发？

**FACT。** `stage4_reviewer2_cheap5.jsonl` 指出失效模式为 *"else evaluation note"* —— 一次降级。**FACT。** `Idea_01/reviewer_attacks.md` 写道 *"If we cannot run the causal arm, **do not submit**."* —— 扣下不发。同一情形面对两套不同指令，没有产物说明以何者为准。后果重大：它决定了 H2 失败时得到的是更短的论文还是没有论文。

### 4.5 Stage-2 保留项被 Stage-3 推翻

**FACT。** `auditor_overlay.md` 记录了 *"Killed despite Stage-2 keep: F-001/002/003 jitter-UQ, F-014 LN≈LoRA, F-051 AdaLoRA-rank, F-074 dup of F-022."*。Stage 2 将这些评为保留项；Stage 3 针对它们指名了既有工作。通过既定规则 *"Stage-3 named papers win collisions"* 予以解决 —— 此处记录为一项依政策解决而非依辩论解决的分歧。

### 4.6 F-012 在没有记录理由的情况下被移出 cheap-5

**FACT。** 廉价簇环节给出了 4 个变异；只有 3 个进入 Reviewer #2。`F-012-samhq-vs-filter`（变异，0.35）被移出。**FACT。** 唯一相关的指令是 `stage2_ABCF_summary.md` 的 *"Do not treat F-012 as 'filter matches HQ-SAM' (mutate to gain-stratification)"* —— 一条划定范围的说明，而非淘汰。沿用自 `stage5_top5.md` §1.2；依然未被解释。

### 4.7 Idea_01 第一天样本量：50 张切片还是 100 张？

**FACT。** `README.md` 写着 *"then **50** real CT slices with SAM AMG vs k-means/SLIC"*；`Idea_01/experiments.md` killer 步骤 3 写着 *"On **50** MSD/TotalSegmentator slices"*；同一文件中的 Stage-5 工程化区块写着 *"Day-1: **100** TotalSegmentator slices"*。虽是小问题，但这是支撑后续一切的核心实验内部未调和的数字。§6 在操作上通过取较大数字并予以说明来解决。

### 4.8 已在别处记录的记账冲突

`stage5_top5.md` §5 记录了 INCONSISTENCY-01 至 -04（README 暂定 / supervisor_log 卡在 Stage 1 / evolution_summary 声称 Stage 5 完成 / 廉价簇裁决计数 11 vs 12）。那些属于状态与算术缺陷而非科学分歧，依然留给 **W6-T3** 修复。此处不予重复。

---

## 5. 锁定裁决 —— **Final 3 保持 PROVISIONAL（暂定）**

### 裁决

> **Windows6 Final 3 在提交 `0c25df6` 处不能被锁定。它们保持 PROVISIONAL。**

想法集合在很大程度上是正确的，该裁决不应被读为对科学内容的怀疑。它是在陈述：**三者中有两个依然可能被尚未执行的查证所杀掉**，而且**选题从未在横向对比集合中运行过**。此时宣布锁定将记录下一个证据尚不支持的决定。

### 为什么未锁定 —— 三项独立理由

**理由 1（决定性）—— 三个存活者中有两个具有未核实的可行性前提条件，且每一项在其自身 package 中都是 *kill* 条件，而非普通风险。**

- **`Idea_02`：** `experiments.md` 步骤 1 为 *"Inventory camera IDs on one public set (PYRONEAR or FIgLib **if IDs exist**)"*，第一条停止规则为 *"**Kill** if no camera metadata."*。**FACT：** Windows6 中没有任何产物记录过相机 ID 曾被确认存在，也没有记录过有多少台相机。整个想法建立在未核验的假设上。`literature.md` 甚至带有警示 *"check camera IDs before use."*。
- **`Idea_03`：** `experiments.md` 施加了 *"**Hard gate:** identical vision encoder + coordinate tokenization"*，`literature.md` 仅将 checkpoint 对列为 *"if licenses allow."*。**FACT：** 没有任何产物点名了经核实满足该门禁的具体模型对。`experiments.md` 仅给出 *"e.g. Qwen-VL vs Chat"* —— 一个例子，而非核验。

两项检查都很便宜，无需 GPU，仅需数小时。锁定一个其中两个成员离死亡仅一步查证之遥的 Final 3 是站不住脚的。

**理由 2 —— Final 3 从未在横向对比集合中排过名。** 依据 §4.2 与 `stage5_top5.md` §1：没有 50 档与 20 档；两个 Stage-3 分支从未在公共尺度上相遇；`D-008`（0.60）与 `D-060`（0.55）被搁置为扩展项而从未与存活者面对面比较；Reviewer #2 从未见过它们。锁定是在断言 *"这三个击败了全场。"* Windows6 能支撑的只是 *"这三个在跑通的单一通道中存活了下来。"* 这是不同的主张，且只有第二条为真。

**理由 3 —— 本轮的状态记录依然自相矛盾。** 四个产物陈述了四个不同阶段（README：Stage 5/6 确认中；`supervisor_log.md`：Stage 1；`evolution_summary.md`：Stage 5 完成；`Idea_01/README.md`：Stage 5 进行中）。在混乱的状态字段上宣布锁定是不可审计的 —— 读者无法判断锁定了什么、何时锁定的。这属于 **W6-T3** 的修复范围，也是锁定决定必须在 T3 之后而非之前的原因。

### 被明确**拒绝**作为不锁定理由的论据

有两条诱人的论据是错误的，记录应予以澄清：

- **"三项残余义务未履行。"** 不是阻碍。残余要求是*待做*的研究；它们拦截的是**发表**，而非**选题**。若未履行的残余阻碍锁定，那么在论文撰写之前没有任何 Final 3 可以被锁定。`stage5_top5.md` 与上文 §2 均将其视为前瞻性义务。
- **"零 ACTUAL RESULTS / 仅有合成原型。"** 同样不是阻碍，原因相同。`README.md` 与 `research_summary.md` 已经如实标注；Final 3 是对科学问题的下注，而非对发现的报告。

真正的阻碍是理由 1–3：未核实的*前提条件*、缺失的*横向对比集*，以及不自洽的*状态记录*。

### 解锁门禁 —— 必须满足什么，由谁执行

| 门禁 | 要求 | 负责人 | 关闭它的标准 |
|---|---|---|---|
| **GATE-A** | 在 ≥1 个公开烟雾／火焰数据集上确认相机元数据存在 | Idea_02 执行者，训练前 | 一份带相机**数量**的成文相机清单。≥10 台相机 → 门禁通过。<10 → 转向仅按事件划分的机制触发，放弃 H2，且 Idea_02 必须在锁定前**重新论证或被替换**。0 台 → Idea_02 按自身停止规则 **kill**。无需 GPU。 |
| **GATE-B** | 点名一对经核实在可用许可下具有相同视觉编码器**且**相同坐标 tokenization 的 base/chat checkpoint 对 | Idea_03 执行者，花 GPU 前 | 从模型卡／配置中确认了这两项性质的点名模型对。失败 → 阶段隔离主张不可行，Idea_03 必须降级为格式假象研究或被替换。无需 GPU。 |
| **GATE-C** | 补齐缺失的对比步骤：在**单一**公共标准上将 3 个存活者与 `D-008`、`D-060`、`E-025` 共同排名 | Supervisor（正规 Stage-6 环节） | 一份产物、一个尺度、全部六个打分，并明确说明是否有扩展项排名超过存活者。关闭 §4.2。无需 GPU。 |
| **GATE-D** | 调和状态记录并将 package 补充到 Final 3 可供审阅的深度 | **W6-T3** | INCONSISTENCY-01…04 调和为单一状态行；package 不再比 Windows4 参考版本薄 11–27 倍；`Idea_01/proposal.md` 缺失的 "§7–28" 补齐或删除。 |

**锁定条件（全部四项）。** 当 GATE-A、GATE-B、GATE-C 与 GATE-D 全部关闭时，Final 3 方可宣布为 **LOCKED**，该声明应写入调和后的状态行，而非写进本文件。

**刻意不作为门禁的内容：** 运行 §6 中的实验。那些实验决定论文是否存在，而非选题是否严密。

### 关于可能结局的有条件说明

**SPECULATION。** GATE-A 与 GATE-B 各自只需数小时案头工作，GATE-C 是一次打分环节，GATE-D 已排期为 W6-T3。最可能的结局是全部四项关闭且 Final 3 维持原样锁定 —— Idea_01 基础扎实，Idea_02/Idea_03 通过前提条件的概率高于失败的概率。本说明是一份预测，而非裁决；**上述裁决为 PROVISIONAL，在门禁关闭并记录之前，任何下游文档都不应引用 Windows6 为已锁定 Final 3。**

---

## 6. 剩余的决定性实验（必须按此顺序运行）

所有成本数字均为 **HYPOTHESIS**（从 `Idea_0*/experiments.md` 与 `evolution_summary.md` 抄录的预算估计）。没有任何一项被运行过。步骤 0a 与 0b 是 §5 的门禁，排在最前因为它们免费且能 kill 掉三个成员中的两个。

**步骤 0a —— GATE-A：相机 ID 清点（无需 GPU，数小时）。**
清点 PYRONEAR-2025 或 FIgLib 上的相机 ID。
→ **≥10 台相机：** 继续至步骤 4。 · **1–9 台相机：** 转向仅按事件划分，放弃 H2，重新论证 Idea_02 的 Final-3 席位。 · **任何地方均无相机元数据：** 按其自身停止规则 **KILL Idea_02** 并通过 GATE-C 提拔替代项。

**步骤 0b —— GATE-B：checkpoint 对核实（无需 GPU，数小时）。**
确认一对具有相同视觉编码器、相同坐标 tokenization 且许可可用的 base/chat 对。
→ **通过：** 继续至步骤 6。 · **失败：** **降级 Idea_03** 为格式假象研究（O1 分支作为独立负结果）或替换它。在此明确前不花 ≤8 GPU-h。

**步骤 1 —— Idea_01 合成健全性检查（CPU，数分钟）。约 0 GPU-h。**
在合成分段常数 "CT" 上运行 `Idea_01/src/amg_intensity_equiv.py`。
→ **阈值（FACT，来自 `experiments.md`）：** 若 AMG 模拟（阈值连通域）即使在合成块上也**没有**胜过 SLIC，*"**实现**有误 —— 在接触真实 SAM 前修复。"*
→ **修复并重试**，而非 kill。该步骤不能验证科学结论；它只能让测试台作废。

**步骤 2 —— 真实 CT 上的 Idea_01 相关性臂（约 2 GPU-h，HYPOTHESIS）。**
SAM ViT-B AMG vs k-means (k ∈ {8,16,32}) vs SLIC vs multi-Otsu vs GMM，在 **100 张 TotalSegmentator/MSD 切片**上 —— 取两个记录数字中较大的一个（见 §4.7；README 和 killer 清单写 50，Stage-5 区块写 100；使用较大值并标注分歧而非静默取平均）。三个临床窗。预先注册的指标：Hungarian 平均 IoU、ARI、boundary-F —— 全部报告，不进行指标挑选。
→ 若在 ≥2 个窗上 IoU(AMG,k-means) > IoU(AMG,SLIC)，则 **继续**。 · 若 3 个窗中仅 1 个展现该效应，则 **PIVOT**（H3 失败 → 设置假象）。 · 若在**全部**窗上 SLIC ≥ k-means，则 **KILL**。

**步骤 3 —— Idea_01 反事实臂 + COCO 对照（本轮决定性实验；增量约 2 GPU-h，HYPOTHESIS）。**
臂 (i) 组织内部单调 HU 重映射，Sobel 边缘冻结；臂 (ii) 置换高频残差，保持每超像素 HU 均值。随后在 COCO 上运行相同协议。
→ 若强度重映射对 AMG 的扰动显著大于纹理置乱，在 ≥2 个窗和 ≥2 组 AMG 设置上成立，则 **作为机制性论文继续**。 · 若两条臂对 AMG 的扰动幅度相当，则 **降级为 evaluation note** —— 这是残余要求自身的 *"else evaluation note"*；注意 §4.4 记录了 `Idea_01/reviewer_attacks.md` 将同一情形读为*不投稿*，该冲突必须在动笔前解决。 · 若 COCO 对照复现了聚类等价性，则 **KILL CT 特异性主张**。 · 若 AMG 相比 k-means 更接近真值 **且** 纹理置乱大幅扰动 AMG，则 **KILL**（Stage-5 门禁）。

*步骤 1–3 排在最前，因为 Idea_01 最便宜、没有未核实的数据前提条件，且是本轮的 `#1 start here`。其反事实臂是 Windows6 中唯一无需获取任何新资产即可将残余义务转化为完整主张的实验。*

**步骤 4 —— Idea_02 试点：1 种子 × 3 划分协议（约 10 GPU-h，HYPOTHESIS）。需要 GATE-A 通过。**
Pyronear-2025 子采样，YOLOv8n，划分 {random, event-disjoint, camera-disjoint}，等 N 且类别比例对齐。报告图像级 AP 与 FAR@recall。外加相机 ID 线性探针与见过 vs 未见过的空帧 FPR，采用 ImageNet 预训练对照 backbone 并按事件聚类 bootstrap。
→ 若 camera-disjoint < random 超过种子标准差 **且** 存在见过／未见过空帧差距，则 **继续至 3 种子 + 第二数据集**。 · 若在种子噪声内 random ≈ camera-disjoint **且** 探针 ≈ 随机水平 **且** 无空帧 FPR 差距，则 **停止** —— 宣布前用另外 2 个种子确认。 · 若在按事件划分下按相机划分的降幅消失，则 **KILL**（H2 死亡）。

**步骤 5 —— Idea_02 pHash 去重重跑（增量，HYPOTHESIS）。仅在步骤 4 继续时执行。**
将重复帧泄漏与相机签名分离开来。
→ 若去重后差距存活，则 **继续**。 · 若差距完全由重复帧解释，则 **降级**为近重复帧审计 —— 此时它成了用数字复述 Voxel51 博客，`Idea_02/proposal.md` 认为这对立论是致命的。

**步骤 6 —— Idea_03 三模式评测（≤8 GPU-h，HYPOTHESIS）。需要 GATE-B 通过。**
一对已核实对，2k RefCOCO，模式：自由生成 / 语法受限 / GT 对比 ≤16 个共享干扰框的似然排序。随后是冻结视觉 token 线性探针。
→ **O3 —— 表征税**（似然差距存在，探针下降）：最强结果，继续。 · **O2 —— 策略税**（似然差距存在，探针完好）：继续。 · **O1 —— 格式假象**（似然下差距消失）：**撰写负结果**；不进入 DPO。 · 若对 1 **和** 对 2 似然差距皆 ~0，则 **停止**。

**步骤 7 —— Idea_03 纯文本 DPO 对照（1–2 × 24GB，数天，HYPOTHESIS）。门禁：仅在 O2 或 O3 时执行。**
`Idea_03/experiments.md` 明确指出 —— *"Do not run DPO unless observational gap survives format control."*
→ 若纯文本偏好微调依然使定位退化，则 **推进至因果主张**（优化目标而非数据配比）。 · 否则 **限定在观测性主张**；按 `reviewer_attacks.md`：*"do not claim causal RLHF without H3."*。

### 对抗终止条件

**FACT。** 在 Stage 4 之后没有针对三个存活者提出新的致命既有工作。两次击杀（§1.1）吸收了本轮发现的两次致命冲突 —— 针对 F-022 的 Metrics Reloaded，针对 F-036/037 的 CLIP-Driven Universal Model。留下的威胁不是某篇已知论文，而是 Idea_03 的**由缺席定义的新颖性**（§2.3.1），任何进一步的文献阅读都无法消除该威胁，唯有执行速度能提供保护。

---

## 7. 溯源

**为构建本文件所读取的产物：** `Windows6/README.md`、`Windows6/research_summary.md`；`selection_history/` 下的 `stage5_top5.md`、`stage3_DE_top10.json.md`、`stage3_prior_work_kill_cheap.jsonl`、`stage4_reviewer2_cheap5.jsonl`、`auditor_overlay.md`、`reviewer_attacks.md`、`reviewer_summary.md`、`literature_anchors.md`、`evolution_summary.md`、`supervisor_log.md`、`stage2_ABCF_summary.md`、`stage2_DE_summary.md`；`Idea_01/` 下的 `README.md`、`proposal.md`、`experiments.md`、`reviewer_attacks.md`、`roadmap.md`、`literature.md`、`references/math.md`；`Idea_02/` 与 `Idea_03/` 下除 `references/math.md` 外的同套文件。

**格式参考（仅限结构，未复用内容）：** 分支 `cursor/windows4-research-idea-evolution-2962` 上的 `Windows4/selection_history/stage6_battle.md` —— 提供 *"Unresolved disagreements kept explicit"*、*"Fatal flaws that ended threads"*、*"Decisive experiments that remain (must run in this order)"* 与 *"Battle stop"* 等章节组织模式。§3 引用的 Windows4 package 大小读取自该分支的文件树清单。

**W6-T2 撰写的文件：** 仅本文件。未修改任何既有文件。

**留给 W6-T3 的工作：** 来自 `stage5_top5.md` §5 的 INCONSISTENCY-01…04；`README.md` / `research_summary.md` / `supervisor_log.md` 中的状态行；package 加厚（GATE-D）。**W6-T3 绝不能将 Final 3 记录为已锁定** —— 依据 §5，在 GATE-A…D 关闭之前它保持 PROVISIONAL。
