# Windows7 — 评审员总结（Reviewer Summary）

评审员实际改变了什么。未产生任何设计变更的反对意见未在此列出；仅在正文中予以反驳的反对意见已作相应标注，因为口头反驳并不是真正的修复。

---

## Idea_01 — SupportAudit (B-0121)

| 攻击点 | 设计变更 |
|---|---|
| "A wrong support is out-of-distribution; you are measuring OOD robustness, not support reliance." | 错误的 support 均取自**同一基准自身的 support 池**，仅类别不同。绝不使用合成数据，绝不进行人为损坏破坏。 |
| "Retention has no floor — 0.4 could be good or bad." | **设立两道下界底线（floors）**，均进行实测：一个无 support 的显著性基线和一个随机掩码基线。保持率（retention）均对照底线报告，绝不孤立呈现。 |
| "Wrong-support lists are a researcher degree of freedom." | 列表通过**冻结随机种子的确定性流程生成，在运行任何方法之前先行提交（commit）**并公开发布。 |
| "Only tests old methods." | **SAM3 臂**被提升进入核心实验矩阵，而非留作未来工作。 |
| "τ = 0.2 was chosen to make the result work." | τ 在预注册时冻结；同时报告敏感度扫描结果。 |
| "One benchmark's degeneracy is not the field's." | 分层分析作为主要分析维度，而非次要子群分析。`S1` vs `S3` 是核心头条结构。 |

**仅在正文中反驳（未改动设计）：** "this is an evaluation paper, not a method paper." 我们的回应是：研究对象特意设定为评测本身，且三种可能的结果分别对应不同且有用的论文。评审员仍可能不喜欢这种类型的论文。

---

## Idea_02 — MemorySurgeon (A-0017)

| 攻击点 | 设计变更 |
|---|---|
| **A1: "Reversibility correlates with sequence difficulty, not with anything about memory."** | 采用**偏相关分析（Partial correlation）**，在**任何对照方法运行前即冻结的对照集（comparator set）**上，控制 no-op 恢复率、失败次数及干扰物密度，并以其**最小值**进行评分。原型让利害关系变得具体：朴素的 `r` 为 0.86，但在某一个对照方法上骤降至 0.03。 |
| "Replay is not deterministic; your arm differences are harness noise." | **E0 门禁。** `no_op` 臂必须逐 bit 精确复现原始失败，否则项目终止。`check_replay_determinism` 采用抛出异常（raise）而非发出警告（warn）。 |
| "You cherry-picked recoverable failures." | 采用固定的采集协议，**零人工筛选**；模棱两可的重现分层（ambiguous-reappearance stratum）单独报告，绝不丢弃。 |
| "Deleting entries changes recency encodings; that is your effect." | 增加 `slot_control` 臂，将槽位占用（slot occupancy）与实际内容隔离开来。 |
| "Corpus size is unknown and may be tiny." | 产出量在 E1 阶段**先于**提出任何主张前报告，并附带明确的降级范围路径。 |
| "SAM2 is a moving target." | 资助设立 SAM3 臂（E7）。 |

**在实现过程中发现、而非由评审员提出的问题** —— 且这两点都比上面列表中的任何一条更为严重：

- **sham 臂的定义完全搞反了。** Stage 6 要求"删除错误发生后的条目，但重新插入数量匹配的错误发生前重复项"。该臂实际上依然移除了被污染的内容，从而执行了治疗性操作，即使在测量工具完全有效的情况下也会与 `targeted` 表现一致。`P3` 在构造上就是不可通过的。因此将其重新定义为无效对照（vacuous control）；字面原版保留为 `slot_control`。
- **合并长周期失败会使 H2 检验被稀释趋近于零。** 一旦 FIFO 队列将所有错误发生前的条目全部冲刷掉，`targeted` 和 `reset` 就变成了完全相同的操作，因此这些失败对二者差距的贡献严格为零。在原型中，原本子集上真实的 +0.130 差距在合并后被稀释至 +0.040 —— 这会导致在真实分解效应存在的世界中无法达到预注册的标准。P2 现在改为在 H2 可检验子集上进行判定，该子集的占比在 E1 阶段、提出任何 P2 主张之前先行报告。

---

## Idea_03 — RehearsalGrid (C-0090)

| 攻击点 | 设计变更 |
|---|---|
| **"Your control arm contradicts your premise."** LLaVA-1.5 的数据混合中已经包含了纯文本 ShareGPT，因此"复现已发表的 recipe"与"`A0` = no rehearsal"无法同时成立。**按原设想属于致命缺陷。** | 采用**剥离文本的基底并重新匹配各臂的 token 预算**；已发表配方的运行降级为参考对照点。主张收缩为"该配方的一个受控变体"，并在 §3 中明确声明。 |
| "Two of your four strata have unusable denominators." | **绝对增量（Absolute deltas）与保持率并列为主要指标**；**分母有效性门禁在各臂运行前执行**，未通过的分层直接替换而非用文字辩解。 |
| "'If the conventions diverge, that's the finding' is unfalsifiable-adjacent." | **明确将逐层匹配（Per-layer matching）设定为预注册的主要协议**，理由是记录在案的逐层梯度差异。全局范数匹配降级为敏感度分析。 |
| "Your 80% rule is a ratio of differences with a small denominator." | **在网格运行前明确声明最小可检测效应（MDE）**；低于该效应的份额不作解释；对每个份额计算 bootstrap 置信区间（CI）。 |
| "One model family, one scale." | **跨模型家族复现被提升进入核心设计**（在 prismatic-vlms 上进行 3 次运行）。虽然不能完全消除该攻击，但 §19 对此作出了诚实声明。 |
| "Robins 1995 predicted this." | 重新定调：若得出证伪分支反而是一篇更有力的论文。`KNOWN FACT` 在拿到数据前无法先验定论。 |

---

## 复活项：Idea_02 的方法臂升级为必须交付项

元评审员（meta-auditor）的偏差审计发现锁定的 Top 5 **过度偏向测量**，因此发布了一项强制性条款而非建议。

**A-0017 的方法臂从可选的次要分析提升为必须交付项（required deliverable）。** 如果定向删除以预注册的 ≥10 分优势击败完整重置，则该论文*必须*将该手术做成免训练的 SAM2 wrapper 发布，并与 SAMURAI 和 DAM4SAM 进行正面对决基准测试。审计明确指出这是**真实的研究范围变更，而非重新贴标签：研究方案包必须为正面对决评测预算算力。** 目前该项已列为 E9（~40 GPU-h，以 P2 为触发条件），这也是 Idea_02 不再是一篇纯测量型论文的原因。

背后的逻辑是：A-0017 是 Top 5 中唯一能在同一算力预算内从测量毕业为方法的想法，将"上限诊断工具"转化为潜在的跟踪器改进方案。

**C-0028 被复活为*获得算力资助的第一候补（funded first alternate）*。** 其 0-GPU 离线演练门禁（H-arm constructibility：在 10K 生成批次上通过 KS < 0.05 相似度匹配加名词比率检验）立即启动运行，以便在 C-0090 未能通过功效门禁时，货架上已有一套完全消除风险的训练配方旗舰方案待命。我们特意**没有**将它与 C-0090 同时选中 —— 两项共享评测基础设施的 VLM 训练研究会在相反方向上重新造成单一文化（monoculture）。

---

## 预先承诺的备选递进阶梯（Fallback Ladder）

事先达成共识，以防失败发生时重新引发选题争议：

1. **C-0090 未通过其功效门禁** → 晋级 **C-0028**（此时其离线门禁已通过；仅凭决策三联组，9 次运行 ≈ 3,600 A100-h 即可定论）。
2. **B-0121 证明不可行**（基准退化极其彻底，以至于认证分支都失去意义） → 若其 $0 案头调研找到 ≥15 个可审计配对则晋级 **M5**；否则晋级已通过 MVE 的 **B-0212**。
3. **A-0017 在裕度测试运行前被抢发（scooped）** → 晋级已通过 MVE 的 **B-0212**；若 B-0212 的 MVE 失败，则 **A-0002**（同一聚类，~30 GPU-h 的 killer 测试集，Cluster A 中最干净的因果设计）作为廉价权宜替代。

---

## 悬而未决的分歧

**Idea_03 究竟该不该出现在本轮中？** 它是一个语言保留度研究，而整个研究组合的其他部分均建立在分割与跟踪之上；并且同样的 2,450 A100-h 足以资助 C-0028 的决策三联组。

评审组最终占上风的立场是：C-0090 是**经过深思熟虑的高昂选题，是对漏斗记录在案的廉价倾向的直接制衡** —— 它是 Top 5 中唯一无论得出何种结果分支都能改变人们*如何训练*的想法。它之所以击败 C-0028 夺得唯一的训练席位，是因为它便宜 2.2 倍、没有遗留的可行性门禁，且在其所在聚类内部被评为 ROI 第一名。

**这是一项研究组合维度的权衡判断，而非科学优劣之争，没有任何实验能够平息它。** 此处如实记录而非粉饰太平，因为它是后续最可能被事后质疑的一点。

---

## 元评审员的审计发现

| 审计发现 | 解决方案 |
|---|---|
| 锁定的 Top 5 过度偏向测量 | **已采取实际行动，而非仅仅记录**：A-0017 的方法臂成为必须交付项（见上文）。 |
| 整个漏斗中没有任何一篇 METHOD 体裁的论文达到提名级 | 审计中如实记录了该灭绝现象。过渡期的风险敞口由 A-0017 的强制方法臂覆盖；B-0112+M4 Leg-1 附属任务保持该赛道活跃；**建议在下一个 window 重新对 Stage-1 生成器下发指令**，以防出现连续三次灭绝。 |
| 新颖性主张依赖于二手引用 | 各想法的验证债务已记录在 `references/` 中；必须在投稿前结清。 |
| 反审计执行不对称（Cluster C 严苛，Cluster B 宽松），以及跨聚类存在 12 倍的成本门槛不一致（A-0107 在 450 GPU-h 被砍，而 C-0028 在 5,300 GPU-h 获得提名） | **未在源头上纠正。** 与 Final 3 相关的两条后果在 Stage-6 选拔中已被消除，但下一个 window 应当下发统一的 Stage-4/5 标准。 |
| B-0121 和 A-0017 对冻结 checkpoint 的依赖 | 在会话中已验证可用性；若 checkpoint 被撤回或许可证变更将迫使更换替代模型（发生概率低，影响小 —— 评测面板包含 7 个及 3+ 个候选方法）。 |
| 成本高度集中：单单一项研究的成本约为其余两项总和的 20 倍 | 予以接受，前提是 Idea_03 的功效门禁必须是一个**硬性**终止点而非阶段性检查点。 |
