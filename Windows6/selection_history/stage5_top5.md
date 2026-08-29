# Stage 5 —— Top-5（事后重建 / RETROSPECTIVE RECONSTRUCTION）

- **Windows ID：** Windows6
- **分支：** `cursor/windows6-research-idea-evolution-b55d`
- **重建日期：** 2026-08-29（UTC）
- **重建自基线提交：** `69b4b2e`（"Research Idea Evolution - Windows 6 - Close remaining in-flight stage notes"）
- **任务：** W6-T1（Windows6 三个收尾任务中的第一个：T1 → T2 → T3）
- **文档类型：** **RETROSPECTIVE / 补记。** 这不是一份当时的实时 Stage-5 记录。

## 0. 本文件为什么存在，以及它不是什么

**FACT。** `evolution_summary.md` 写道：*"Stage 5 cloud engineering + DE assassin + auditor: **done**. Day-1 budgets ~2 / ~10 / ~8 GPU-h."* —— 即 Stage-5 工作**声称已经被执行了**。

**FACT。** 在提交 `69b4b2e` 时，`Windows6/selection_history/` 下**没有 `stage5_top5.md`**，也**没有 `stage6_battle.md`**。Stage-5 的主张从未落成文件。本文档是对该缺失阶梯事后的重建。

**本文件的范围（严格边界）：**

- 它**不重新选题**。下文的每一条裁决均抄录自已有产物。
- 它**不修改** `Idea_01/`、`Idea_02/`、`Idea_03/`，或任何已有的 `stage1_pool/` / `stage2*` / `stage3*` / `stage4*` 文件。
- 它**不修复**它在 §5 中记录的状态矛盾。那些矛盾刻意留给 **W6-T3**。
- 它**仅**从 `stage4_reviewer2_cheap5.jsonl` 重建 Top-5 梯队，因为那是该轮实际产出的唯一一个 5 项产物。

### 证据分级图例

| 标签 | 在本文件中的含义 |
|---|---|
| **FACT** | 直接存在于 Windows6 仓库产物中；可引用且可按行核对。 |
| **VERIFIED PRIOR WORK** | 某个 Stage-3/4 agent 检索过并用于杀掉或变异想法的外部论文。我们**没有**重跑他们的表格。 |
| **HYPOTHESIS** | 本轮希望检验的科学主张。未经测量。 |
| **SPECULATION** | *本*事后文档作出的、产物未直言的推断。 |
| **EXPECTED RESULT** | 预先注册的预测趋势。未经测量。 |
| **ACTUAL RESULT** | 实际运行得到的数字。**Windows6 中没有任何 ACTUAL RESULT。** |

**FACT。** Windows6 包含 **0 个 ACTUAL RESULTS**。`Windows6/README.md` 将三个 package 标为 **"no real SAM numbers" / "no smoke mAP" / "no VLM eval"**，`research_summary.md` 写道 *"All quantitative claims in packages are EXPECTED/HYPOTHESIS unless labeled otherwise. Prototypes are synthetic."*。`evolution_summary.md` 中的 `~2 / ~10 / ~8 GPU-h` 数字是**预算估计 → HYPOTHESIS**，不是实测运行时间。

---

## 1. 漏斗偏差声明（在看 Top-5 表格前先读此节）

`supervisor_log.md` 写明了原定政策：*"Continue waves until ≥1000 unique ideas, then **1000→200→50→20→5→3**."*。Windows6 没有执行那个阶梯。它被中断了（第一波超时），并通过一条狭窄的"廉价"通道收尾。

| 阶梯 | 标准政策 | Windows6 实际 | 状态 |
|---|---|---|---|
| 原始池 | 1000+ | **1080 原始 / 1062 有效**（S 系列 600 + A–F 480；按 `evolution_summary.md` 有 "D surplus"） | **达标** |
| → 200 | 200 个打分存活者 | **142** 推进（78 ABCF + 64 DE） | **不足（−58）** |
| → 50 | 50 档 | *从未产出* | **缺失** |
| → 20 | 20 档 | *从未产出* | **缺失** |
| → 5 | 20 → 5 | **10 条 DE 裁决 + 12 条 cheap-cluster 裁决 → 5**（见 §1.2） | **被替代，未按规程执行** |
| → 3 | 5 → 3 | **3 个存活**（Reviewer #2，`stage4_reviewer2_cheap5.jsonl`） | **仅在数量上达标** |

### 1.1 上述数字的逐项核验

**FACT（原始池 = 1080）。** `stage1_pool/` 中的记录数：`A/B/C/D/E/F_001_080.jsonl` 各 80 条（480），`S_001_100.jsonl` 100 条，`S_101_250.jsonl` 150 条，`S_251_400.jsonl` 150 条，`S_401_600.jsonl` 200 条（600）。480 + 600 = **1080**。`1062 有效` 的数字由 `README.md` 与 `evolution_summary.md` 主张；本文档不重新推导 18 条的差额。

**FACT（142 不是一个干净的 "200 档"）。** 两个 Stage-2 产物与 `README.md` 对该档的描述自相矛盾：

- `stage2_ABCF_summary.md`：*"Reviewed 320 (A+B+C+F). **78 survivors.**"* —— `stage2_survivors_ABCF.jsonl` 有 **78** 条记录。
- `stage2_DE_summary.md`：*"Reviewed 160 (D+E). **64 survivors / 96 killed.**"* —— `stage2_survivors_DE.jsonl` 有 **64** 条记录。
- `README.md`：*"Stage 2: **78+64 scored**."*

因此 78 + 64 = **142** 在阶段总结中被称为*存活者（survivors）*，在 README 中被称为*打分者（scored）*。两种读法都以不同方式未达到 200 档：

1. 读为**存活者**：142 < 200。
2. 读为**打分者**：同样不对，因为实际评审了 480 条（320 + 160），142 是筛选出来的。

**FACT。** 无论哪种读法，**600 条 S 系列想法从未经过 Stage-2 打分。** Supervisor 种子目录虽然启动了（按 `supervisor_log.md`：*"Supervisor seed catalog started locally (S-series) so the funnel is not blocked by timeouts"*），但 Stage 2 只覆盖了 A–F。这是整轮中最大的一处偏差：**原始池的 55% 从未进入打分环节。**

本文档明确**拒绝**将本轮描述为"完成了 200 档"。它没有完成。

### 1.2 "→5" 是如何实际发生的（重建的选择规则）

根本没有可供收缩的 20 档。而是跑了两个独立的 Stage-3 分支，且只有其中一个分支喂给了 5：

**分支 A —— cheap-killer prior-work 簇**（`stage3_prior_work_kill_cheap.jsonl`，**12** 条裁决）：
- 保留 ×2：`sam-amg-intensity-clustering`（0.6）、`camera-id-leakage-smoke`（0.55）
- 变异 ×4：`F-012-samhq-vs-filter`（0.35）、`empty-slice-fpr-gate`（0.45）、`alignment-tax-vlm-localization`（0.5）、`clip-text-unused-organs`（0.5）
- 杀掉 ×6：`F-014-S-030-ln-affine-vs-lora`、`histogram-matching-da`、`lora-effective-rank`、`prompt-jitter-uncertainty`、`multiclick-nonmonotonic`、`dice-vs-ce-calibration`

**FACT。** cheap-5 恰好是 `保留 ×2 + 变异 ×3`，丢掉了 `F-012-samhq-vs-filter` 这一项变异：

> `sam-amg-intensity-clustering` + `camera-id-leakage-smoke` + `empty-slice-fpr-gate` + `alignment-tax-vlm-localization` + `clip-text-unused-organs` = **`stage4_reviewer2_cheap5.jsonl` 中的 5 个 ID**

**SPECULATION。** 没有产物写明*为什么* `F-012` 被排除在 5 之外。`stage2_ABCF_summary.md` 仅警告 *"Do not treat F-012 as 'filter matches HQ-SAM' (mutate to gain-stratification)"*。该排除未被记录；本文档不编造理由。

**分支 B —— DE 前 10 刺客**（`stage3_DE_top10.json.md`，**10** 条裁决）。**FACT：** 纯 DE 的想法没有一条作为独立条目进入 cheap-5。`E-009` 能进入 Top-5 仅仅是因为 `auditor_overlay.md` 将其与 `F-031` 合并为一个受保护的保留项。`D-008`、`D-060`、`E-025` 被搁置为扩展项（§4）。

**底线结论：** Windows6 的路径是 `1080 → 142 → (10 DE ‖ 12 cheap) → 5 → 3`。从未有过可供修剪的 50 档或 20 档。

---

## 2. Top-5（恰好 5 条，按 `stage4_reviewer2_cheap5.jsonl` 行顺序）

**FACT。** 本表格的成员构成不是一项 Stage-5 判断。它是对本轮唯一一份 5 项产物的原样抄录。

| # | Stage-4 ID | 原始 Stage-1/2/3 编号 | Reviewer #2 裁决 | `advance` | 进入 Final 3？ |
|---|---|---|---|---|---|
| 1 | `AMG-HU-clustering` | **F-067** | survive | `true` | **是 → `Idea_01`** |
| 2 | `camera-ID-smoke` | **F-043** | survive | `true` | **是 → `Idea_02`** |
| 3 | `empty-slice-FPR-Dice` | **F-022**（+ **F-074**，重复） | **kill** | *(字段缺席)* | 否 |
| 4 | `alignment-tax-localization` | **F-031 / E-009**（+ **F-039**，格式臂） | survive | `true` | **是 → `Idea_03`** |
| 5 | `atlas-vs-CLIP-text` | **F-036 / F-037** | **kill** | *(字段缺席)* | 否 |

**映射证据（皆为 FACT，均可定位）：**

- `auditor_overlay.md`：*"Protected keeps: **F-067** AMG clustering, **F-043** camera-ID, **F-031/E-009** alignment tax (stage-isolated)."*
- `auditor_overlay.md`：*"Reviewer #2 later **killed** **F-022** empty-FPR audit and **F-036/037** atlas-vs-text."*
- `stage2_ABCF_summary.md` supervisor 叠加意见：*"Keep/mutate: **F-067** AMG-vs-kmeans, **F-043** camera-ID, **F-022/F-074** empty-FPR audit, **F-031/F-039** alignment tax, **F-036/F-037** atlas vs text."* —— 这是唯一一行将全部五个映射起来的位置。
- `auditor_overlay.md` 还把 **F-074** 记录在"尽管 Stage 2 判保留但仍被杀"的集合中，标注为 *"dup of F-022"*。

---

### 2.1 `AMG-HU-clustering` —— F-067

- **原始编号：** `F-067`（`stage1_pool/F_001_080.jsonl`，种子 `amg`，变异类型 `cheaper`）；Stage-3 记录 ID `sam-amg-intensity-clustering`。
- **科学假设（HYPOTHESIS）：** 在做过窗宽窗位处理的 CT 上，SAM 的 Automatic Mask Generation 输出近似于 HU 空间中的强度聚类而非语义 objectness —— 因此 AMG 与 k-means/multi-Otsu/GMM 的一致度应高于与纹理超像素（SLIC）的一致度，并且在强度重映射下应发生变动，同时对保持强度的纹理置乱保持不变。
- **Stage-1 最小实验（FACT，原引）：** *"MI(AMG,kmeans-intensity) vs MI(AMG,kmeans-ViTfeat) on 100 images; near-equality proves intensity suffices"*。
- **Stage-3（FACT）：** `continue: keep`，`novelty_confidence: 0.6`，剩余新颖性 *"Mechanistic AMG vs HU k-means equivalence on CT not found"*。
- **Reviewer #2 裁决（FACT）：** `"continue":"survive"`，`"advance":true`。
- **残余义务（FACT，字面引自 `stage4_reviewer2_cheap5.jsonl`）：**
  > `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`
- **残余义务的含义：** 若因果臂未跑，该贡献从机制性主张降级为 evaluation note。`Idea_01/reviewer_attacks.md` 将同一个门禁表述为 *"If we cannot run the causal arm, **do not submit**."*。
- **进入 Final 3：** **是** —— 打包为 `Idea_01`。`README.md` 将其标为 *"#1 start here"*。
- **Stage-5 工程化主张（HYPOTHESIS，仅限预算）：** `Idea_01/experiments.md` 记录了第一天计划：100 张 TotalSegmentator 切片、软组织窗、SAM ViT-B AMG vs k-means vs multi-Otsu，然后是纹理置乱，**≤2 GPU-h**，外加一个 **COCO 对照**以确保聚类等价性是 CT 特异的。未跑。**无 ACTUAL RESULT。**

### 2.2 `camera-ID-smoke` —— F-043

- **原始编号：** `F-043`（`stage1_pool/F_001_080.jsonl`，种子 `smoke`，变异类型 `cheaper`）；Stage-3 记录 ID `camera-id-leakage-smoke`。
- **科学假设（HYPOTHESIS）：** 烟雾／火焰基准分数因训练／测试间共享相机而虚高，且*按事件划分*并未消除此问题 —— 按相机划分的分数应低于随机划分，且冻结 backbone 特征上的线性相机 ID 探针应胜过随机水平。
- **Stage-1 最小实验（FACT，原引）：** *"Train linear camera classifier; correlate its accuracy with train/test gap across published splits"*。
- **Stage-3（FACT）：** `continue: keep`，`novelty_confidence: 0.55`，剩余新颖性 *"Peer-reviewed inflation quantification across smoke/fire benches"*。
- **Reviewer #2 裁决（FACT）：** `"continue":"survive"`，`"advance":true`。
- **残余义务（FACT，原文）：**
  > `Need event-disjoint vs camera-disjoint gap plus empty-frame memorization probe`
- **残余义务的含义：** 单纯按相机划分的分数下降并不构成论文；如果不将地理偏移与背景记忆分离开来，它就会坍缩为一篇已经被写过博客的诊断。
- **VERIFIED PRIOR WORK（用作攻击面，未复现）：** PYRONEAR-2025 按事件划分（arXiv 2402.05349）；Voxel51 Pyro-SDIS 审计在 `Idea_02/literature.md` 中被明确记录为 *"2026 blog — diagnosis, **no** retrained mAP"*，并附指令 *"Do not cite a peer-reviewed mAP inflation number we did not compute."*。
- **进入 Final 3：** **是** —— 打包为 `Idea_02`。
- **Stage-5 工程化主张（HYPOTHESIS，仅限预算）：** Pyronear-2025 子采样、YOLOv8n、1 种子 × 3 协议 + 探针 + 空帧 FPR，**约 10 GPU-h**；等 N、类别比例对齐的划分，在事件上聚类的 bootstrap。未跑。**无 ACTUAL RESULT** —— `Idea_02/proposal.md` 写道 *"We have not trained a detector here."*。

### 2.3 `empty-slice-FPR-Dice` —— F-022（+ F-074）

- **原始编号：** `F-022`（`stage1_pool/F_001_080.jsonl`，种子 `dice-fpr-hist`，变异类型 `reverse`），`F-074`（种子 `eval-flips`）记录为重复项；Stage-3 记录 ID `empty-slice-fpr-gate`。
- **最后表述的科学假设（HYPOTHESIS）：** CT 上的空切片假阳性属于校准失效而非表征失效，且空切片 FPR 在各已发表排行榜上与 Dice 是去相关的。
- **Stage-3（FACT）：** `continue: mutate`，`novelty_confidence: 0.45`，剩余新颖性 *"Cross-leaderboard FPR vs Dice decorrelation audit; kill two-stage gate as method"*。
- **Reviewer #2 裁决（FACT）：** `"continue":"kill"`。**记录中没有 `advance` 字段，也没有 `residual` 字段** —— 只有 `reason`。
- **Kill 理由（FACT，字面引自 `stage4_reviewer2_cheap5.jsonl`）：**
  > `Near-definitional Dice property; Metrics Reloaded; no leaderboard preds`
- **VERIFIED PRIOR WORK：** Metrics Reloaded, Nature Methods 2024（`literature_anchors.md`）。
- **进入 Final 3：** **否。** `auditor_overlay.md` 明确指出审计员自己的保留不覆盖此项：*"Those auditor 'keeps' do **not** enter Final 3."*。

### 2.4 `alignment-tax-localization` —— F-031 / E-009（+ F-039）

- **原始编号：** 这是唯一一个**合并**条目。
  - `F-031`（`stage1_pool/F_001_080.jsonl`，种子 `vlm-clip`，变异类型 `split`）：*"Alignment tax on localization confounds RLHF objective with RLHF data distribution"*。
  - `E-009`（`stage1_pool/E_001_080.jsonl`，标签 `rlhf-tax`）：*"Quantify localization drop from base to RLHF checkpoint pairs"*。
  - `F-039`（种子 `vlm-clip`，变异类型 `reverse`）提供了格式假象臂：*"The tax is an output-format artifact: aligned models hedge on raw coordinates"*。在 `stage2_ABCF_summary.md` 中与 F-031 归为一组（*"F-031/F-039 alignment tax"*），但**未**被 `auditor_overlay.md` 点名。
  - `auditor_overlay.md` 是合并的权威依据：*"F-031/E-009 alignment tax (stage-isolated)"*。
  - Stage-3 廉价簇记录 ID：`alignment-tax-vlm-localization`。
- **科学假设（HYPOTHESIS）：** 在控制输出格式后，chat/RLHF checkpoint 在定位上弱于匹配的 base/SFT checkpoint；若下降仅出现在生成的坐标中而非冻结视觉 token 探针中，则对齐税属于格式效应而非感知效应。
- **两项 Stage-3 裁决，皆有记录（FACT）：**
  - 廉价簇：`continue: mutate`，`novelty_confidence: 0.5`，剩余新颖性 *"Stage-isolated base vs SFT vs RLHF localization curve only"*。
  - DE 前 10 刺客：`E-009` **keep**，置信度 **0.55**，备注 *"matched checkpoint localization tax still open"*。
- **Reviewer #2 裁决（FACT）：** `"continue":"survive"`，`"advance":true`。`reviewer_summary.md` 注明其为 *"survive (mutated)"*。
- **残余义务（FACT，原文）：**
  > `Format-controlled eval + representation probe + small text-only DPO control`
- **残余义务的含义：** 三项独立的义务 —— 语法受限／似然评测以消除格式混淆因素、冻结视觉 token 探针以定位该税、以及在提出任何关于 RLHF 优化目标的因果主张前完成纯文本 DPO 臂。
- **VERIFIED PRIOR WORK（攻击面）：** MDGD 视觉遗忘（EMNLP Findings 2025）与 TWIST & SCOUT（ICCV 2025）—— `Idea_03/literature.md` 记录了*阶段隔离的定位曲线* **未被找到**为独立论文（EVIDENCE GAP，置信度约 0.5）。
- **进入 Final 3：** **是** —— 打包为 `Idea_03`。`README.md` 称其为 *"Highest impact, highest concurrent-work risk"*。
- **Stage-5 工程化主张（HYPOTHESIS，仅限预算）：** 一对 base/chat、2k RefCOCO、三种评测模式（自由生成 / 语法受限 / 针对 ≤16 个共享干扰项的似然排序），**≤8 GPU-h**，关于相同视觉编码器 + 坐标 tokenization 的硬门禁；产出预先注册为 O1 格式假象 / O2 策略税 / O3 表征税。未跑。**无 ACTUAL RESULT。**

### 2.5 `atlas-vs-CLIP-text` —— F-036 / F-037

- **原始编号：** `F-036`（*"Replacing the CLIP text tower with one-hot class embeddings loses nothing for organ segmentation"*）与 `F-037`（*"A registered atlas probability channel subsumes text conditioning for organs"*），皆属于 `stage1_pool/F_001_080.jsonl`，种子 `vlm-clip`；Stage-3 记录 ID `clip-text-unused-organs`。
- **最后表述的科学假设（HYPOTHESIS）：** 在以文本为条件的器官分割中，CLIP 文本塔充当空间先验，因此 atlas 质心应当能在无损情况下替代它。
- **Stage-3（FACT）：** `continue: mutate`，`novelty_confidence: 0.5`，剩余新颖性 *"Atlas-centroid substitution proving text is spatial prior"*。
- **Reviewer #2 裁决（FACT）：** `"continue":"kill"`。**无 `advance` 字段，无 `residual` 字段** —— 只有 `reason`。
- **Kill 理由（FACT，原文）：**
  > `CLIP-Driven Universal Model ICCV 2023 one-hot ablation; substitution unidentifiable`
- **VERIFIED PRIOR WORK：** CLIP-Driven Universal Model, ICCV 2023 —— 其已有的 one-hot 消融使得所提出的替换方案不可辨识。
- **进入 Final 3：** **否。** 同 §2.3 的审计员覆盖规则。

---

## 3. Top-5 → Final 3 结果

**FACT。** 5 个中有 3 个以 `advance: true` 存活；2 个被杀。这是 Windows6 的实现数量与标准漏斗吻合的唯一地方，且它的吻合纯粹是廉价通道的巧合，并非执行了 20 选 5 的规程。

Final 3 是暂定的。`reviewer_summary.md`：*"Provisional **Final 3** pending DE-top10 assassin + auditor overlay."*。这两项后来都有记录（`stage3_DE_top10.json.md`、`auditor_overlay.md`），但没有任何产物宣布 Final 3 已确认 —— 见 §5。

---

## 4. 储备项／扩展项（明确**不属于** Top-5 成员）

**FACT。** `stage3_DE_top10.json.md` 结尾写道：*"Held as **extensions**, not Final 3: **D-008, D-060, E-025**."*。那是原始的 Stage-3 判断；本文件仅作抄录。三者皆未出现在 `stage4_reviewer2_cheap5.jsonl` 中，因此**它们都不是 Top-5 成员**，且从未被 Reviewer #2 的 cheap-5 环节审视过。

| ID | Stage-1 想法（原文） | Stage-3 DE 裁决 | Stage-3 备注（原文） | Stage-2 DE 打分信号 |
|---|---|---|---|---|
| `D-008` | *"Slice-flicker as uncertainty estimator"* | **keep**，置信度 0.60 | *"slice-flicker as **eval** not FP-reduction train"* | keep，`protect_flag: true`，roi 5 |
| `D-060` | *"Volume-weighted per-organ FROC"* | **keep**，置信度 0.55 | *"FPs per litre organ volume FROC"* | keep，roi 5 |
| `E-025` | *"Randomize Set-of-Mark numbering; measure answer variance"* | **mutate**，置信度 0.50 | *"SoM on-image permutation; ship a fix"* | keep，`protect_flag: true`，roi 5 |

**关于 D-008 的说明（FACT）。** Stage-3 的保留是有重述前提的：它作为**评测**信号存活，而不是作为降假阳性的训练方法。任何后续复活都必须携带该约束。

**SPECULATION。** 这三者在 Stage-2 ROI 上的得分与 cheap-5 的若干成员相当或更高，却被搁置了。没有任何产物记录了"为什么把廉价簇送去 Reviewer #2 而把 DE 的保留项扣下"的决策规则。这是缺失 20 档的后果：由于没有共同的 20 项池，两个 Stage-3 分支从未相互横向排名。

**FACT。** 其余 DE 前 10 条目处理如下且**不属于**扩展项：`E-035` kill（0.15）、`E-041` kill（0.05）、`E-057` kill（0.20）、`D-067` kill（0.25）、`D-062` mutate（0.40）、`E-001` mutate（0.35）。`D-062` 与 `E-001` 是没有记录归宿的变异项。

---

## 5. 状态不一致登记表 —— **供 W6-T3 使用，本任务不予修复**

**本任务不修改下列任何文件。** 记录在此以便 W6-T3 可以一次性调和它们。

### INCONSISTENCY-01 —— README 声称 Stage 5/6 仍在确认中

- **文件：** `Windows6/README.md`
- **文字（FACT）：** *"Status: Provisional Final 3 packaged; Stage 5/6 still confirming against DE-top10 assassin + auditor."*
- **冲突对象：** `evolution_summary.md`，后者称 Stage 5 已完成。
- **同样相关：** `Idea_01/README.md` 写着 *"Status: Stage 4 survived Reviewer #2; **Stage 5 in flight**."* —— 同一状态的第四种表述。

### INCONSISTENCY-02 —— supervisor_log 依然写着 Stage 1

- **文件：** `Windows6/selection_history/supervisor_log.md`
- **文字（FACT）：** *"Current stage: **Stage 1 — Massive Idea Exploration** (retry wave)"*，最后更新 2026-08-28。
- **冲突对象：** 其自身的派发日志，该日志已经记录了 *"Stage3 assassin done"* 与 Reviewer #2 环节 —— 即在任何跨文件对比之前，阶段字段就与本文件的正文内部自相矛盾。

### INCONSISTENCY-03 —— evolution_summary 声称 Stage 5 完成，却无 Stage-5 产物

- **文件：** `Windows6/selection_history/evolution_summary.md`
- **文字（FACT）：** *"Stage 5 cloud engineering + DE assassin + auditor: **done**. Day-1 budgets ~2 / ~10 / ~8 GPU-h."*
- **冲突对象：** 提交 `69b4b2e` 时缺失 `stage5_top5.md`（本文档填补的空缺）以及 INCONSISTENCY-01。
- **附加标记：** `~2 / ~10 / ~8 GPU-h` 数字读起来像实测值。它们是 **HYPOTHESIS**（预算估计）。W6-T3 应予以标注。

### INCONSISTENCY-04 —— Stage-3 廉价簇裁决计数不匹配 *(W6-T1 新发现)*

- **文件：** `Windows6/selection_history/evolution_summary.md`
- **文字（FACT）：** *"Stage 3 cheap-killer prior-work: done. **Keep 2, mutate 3, kill 6.**"* —— 合计为 **11**。
- **实际（FACT）：** `stage3_prior_work_kill_cheap.jsonl` 包含 **12** 条记录：保留 2、**变异 4**、杀掉 6。
- **关于原因的 SPECULATION：** "mutate 3" 似乎只计算了晋级到 cheap-5 的变异项，静默漏掉了 `F-012-samhq-vs-filter`。若是这样，总结把"给出的变异裁决数"与"被晋级的变异数"混为一谈了。
- **留给 W6-T3。** 仅记录；此处不做更正。

### 非不一致项，为完整性在此记录

`README.md` 的 *"Stage 2: 78+64 scored"* 属于表述不严谨而非矛盾（见 §1.1），但它是最容易被误读为"200 档已完成"的一句话。它没有完成。**480 条被评审 → 142 条存活；600 条 S 系列从未被打分。**

---

## 6. 溯源

**为构建本文件所读取的产物：** `Windows6/README.md`、`Windows6/research_summary.md`；`selection_history/` 下的 `stage2_ABCF_summary.md`、`stage2_DE_summary.md`、`stage2_survivors_ABCF.jsonl`、`stage2_survivors_DE.jsonl`、`stage3_DE_top10.json.md`、`stage3_prior_work_kill_cheap.jsonl`、`stage4_reviewer2_cheap5.jsonl`、`auditor_overlay.md`、`reviewer_attacks.md`、`reviewer_summary.md`、`eliminated_ideas_summary.md`、`evolution_summary.md`、`literature_anchors.md`、`supervisor_log.md`，加上对 `stage1_pool/*.jsonl` 的定向 ID 检索；以及 `Idea_01/`、`Idea_02/`、`Idea_03/` 下的 `README.md`、`proposal.md`、`experiments.md`、`reviewer_attacks.md`、`roadmap.md`、`literature.md`。

**W6-T1 撰写的文件：** 仅本文件。未修改任何既有文件。

**本任务未产出的内容：** `stage6_battle.md`（依然缺失）、对 INCONSISTENCY-01…04 的任何修复、对 Final 3 的任何改动。
