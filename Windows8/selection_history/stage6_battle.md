# Stage 6 —— 研究组对抗（battle）（Windows8）

**这是一份 RETROSPECTIVE RECORD（事后补记），不是当时的实时记录。**

- **撰写时间：** 2026-08-29（UTC+8），由 Stage-6 记录环节完成。
- **该轮实际执行时间：** 2026-08-28（依据 `README.md`、`research_summary.md`、`supervisor_log.md`）。
- **本文件的性质：** 事后依据本目录树中已经存在的产物重建。该轮运行当时并没有产出任何 Stage-6 文件。下文每一条裁决都是*从已有产物中抄录或推导*出来的，每一行都注明来源。凡某个决定的理由从未被写下来的，这里就直接如实说明，而不是替它补上。
- **本文件不做的事：** 不重新打开 Final 3；不修改 `Idea_01/`、`Idea_02/`、`Idea_03/`；不修改 `stage2_top200.md` / `stage3_top50.md` / `stage4_top20.md` / `stage5_top5.md`。

**为什么"事后补记"这个标签是承重的（FACT）。** `supervisor_log.md` 恰好只有三节 —— "Git numbering decision"、"Stage 1 dispatch (t0)"、"Stage 1 recovery (t1)"。里面没有 Stage-6 的派发条目、没有投票计数、也没有任何与 Stage-6 rejector 相关联的子 agent id。本轮唯一被记录过的子 agent 就是三个 Stage-1 批次生成器，而它们三个在首次派发时全部失败（`request is required and could not be loaded from cloud agent state`）。因此没有任何证据表明存在独立的 Stage-6 评审流程，本文件也不主张存在。见 §5。

## 参与角色（按已有记录，并附各自的证据地位）

| 角色 | 记录在哪里 | 是否有独立性证据？ |
|------|----------------------|-------------------------|
| Supervisor / PI "Windows8" | `README.md`（"Supervisor: Windows8 (PI)"）、`supervisor_log.md`、`research_summary.md` | 不适用 —— 它是记录中唯一的决策者 |
| "Skeptical PI" | `evolution_summary.md` → "Stage 6 unresolved disagreements" 第 1 条 | **没有。** 只是被点名为一种立场，没有独立的 agent id 或日志 |
| "Segmentation expert" | `evolution_summary.md` → 同上第 1 条 | **没有。** 同上 |
| "Methodology reviewer" | `evolution_summary.md` → 同一节第 2 条 | **没有。** 同上 |
| "Reviewer #2" | `reviewer_summary.md` → "Reviewer #2 attacks that survived only if a killer experiment exists"；三个 Idea 目录下各自的 `reviewer_attacks.md` | **没有。** 这是 Supervisor 自己套用的一个对抗性检查清单人格 |
| 回音室审计员 | `reviewer_summary.md` → "Echo-chamber audit (Supervisor self-check)" —— 该标题本身就写明是*自*查 | **没有，按它自己的措辞就没有** |

**FACT.** 作为对照的 `Windows4` 在其 `stage6_battle.md` 开头写的是 "Role cycle covered by Stage 3 assassins + Stage 4 R2 (**three independent rejectors**). No false consensus."。Windows8 没有等价的记录，本文件也不作等价的主张。

## 1. Stage 6 的输入

**FACT.** 五个候选，来自 `stage5_top5.md`（`count=5`，ROI 排序按 `evolution_summary.md` → "Stage 5 Top 5 (ROI order)" 的记录）：

| Stage-5 排名 | ID | 代号 |
|---|----|----------|
| 1 | `IDEA-X-0004` | Spectral LoRA audit |
| 2 | `IDEA-X-0001` | Exclusion-region prompting |
| 3 | `IDEA-X-0003` | IoU-token reject option |
| 4 | `IDEA-X-0007` | Replay for promptability |
| 5 | `IDEA-X-0002` | Density decoder on frozen SAM |

输出：三个 package，早在本文件存在之前就已在 `README.md` 和 `research_summary.md` 中锁定。

## 2. 对抗矩阵，5 → 3

### 2.0 六条判据从何而来（没有发明任何新维度）

| 下文使用的判据 | 已有记录中的出处 |
|---------------------|-----------------|
| 科学问题是否可证伪 | `reviewer_summary.md` 的 Stage-2 维度列表（"scientific question"、"soundness"）；`evolution_summary.md` 中的 Stage-4 规则："Kill if no experiment can shut the attack"；每个 `proposal.md` 都给出了编号的可证伪 H1/H2/H3 加一条 kill 线 |
| killer 实验成本，"一个 GPU-day"量级 | `README.md` → "Killer experiment is one GPU-day and can kill the project honestly"；`evolution_summary.md` 中的 Stage-5 规则 → "ROI = information per GPU-hour"；`reviewer_summary.md` 的 Stage-2 维度 "feasibility"、"compute"、"ROI" |
| prior work 占位情况 | `reviewer_summary.md` → "Prior-work kills (Stage 3) — EVIDENCE" 表；`README.md` → "prior work already occupied the eval-only and adapter-SOTA slots"；`reviewer_summary.md` 的维度 "already-published risk" |
| 结果为 null 时是否仍可发表 | `reviewer_summary.md` 的维度 "risk"/"upside"；各 package 的负结果条款（`Idea_01/proposal.md`、`Idea_02/experiments.md` → "Negative"、`Idea_03/proposal.md`） |
| blast radius（如果我们对了，谁错了） | `reviewer_summary.md` 的维度 "significance"/"upside"；`research_summary.md` → "highest chance to change *where* people spend PEFT parameters"。**用词说明：** "blast radius" 这个说法出自 `Windows4/selection_history/stage6_battle.md`；这里把它借用为 Windows8 本来就已在打分的"重要性／上限收益"这条轴的标签，而不是新增一条判据 |
| 数据与 checkpoint 可得性 | `reviewer_summary.md` 的维度 "datasets"；`research_summary.md` → "Smoke dataset licenses and SAM checkpoints not in this VM"；`README.md` 的项目状态表 → Idea_01 "needs real SAM weights for science; toy loop runs"；`Idea_01/experiments.md` → "Datasets (plan, not downloaded here)" |

### 2.1 矩阵

所有单元格都是关于尚未执行的工作的 **HYPOTHESIS** 级判断，除了那些陈述"某文件写了什么"的单元格（**FACT**），以及那些复述 `reviewer_summary.md` 中已记录的 prior-work 攻击的单元格（**VERIFIED PRIOR WORK (as recorded)** —— 只是抄录，本次并未拿去与文献重新核对）。

| 判据 | `X-0004` Spectral LoRA | `X-0001` Exclusion prompting | `X-0003` IoU reject | `X-0007` Replay promptability | `X-0002` Density head |
|---|---|---|---|---|---|
| **可证伪？** | **可以，而且是数值层面的。** 五个里唯一在自己 proposal 中带可预注册数值阈值的："≥80% of energy below cutoff \(k_c\)"、"pre-register \(k_c\)"（`Idea_02/proposal.md`） | **可以**，即 `Idea_01/proposal.md` 的 H3，但判定边界是定性的（"do not help COCO"） | **可以**，而且检验的正是效应的符号：ρ 必须变为**负**，而不只是变小（`Idea_03/proposal.md` H2） | **可以**，并且给了明确数值目标："<1 Dice drop on the medical target"（`raw/batch_X_hand.md`） | **可以**，即 `Idea_01/proposal.md` 的 H1，但表述为 "higher NSD" 且没给出差值下限 |
| **killer 成本**（已记录的估计） | "Killer < 1 GPU-day"（`Idea_02/proposal.md`）；Day-1 形态可以在 "any LoRA checkpoint or the toy trainer in `src/`" 上跑（`Idea_02/roadmap.md`） | 与 Idea_01 E0 共用："1×12–24GB GPU, <8h including embedding cache"（`Idea_01/experiments.md`） | **五个里最便宜："Zero training"** —— 在 100 张 COCO vs 100 张 Trans10K／烟雾图像上导出 SAM2 IoU token 与真实 GT IoU（`Idea_03/proposal.md`） | "COCO-proxy 200 images + LoRA"（`raw/batch_X_hand.md`）—— 需要一次真实的 PEFT 训练，所以严格来说比其他四个都贵 | 与 Idea_01 E0 共用，同样是 <8 小时的预算 |
| **prior work 占位** | 尚空。"LoRA-MedSAM / SAMed: efficiency + Dice, **no spectrum**"；"Med-SA: adapter design, not frequency diagnosis"（`Idea_02/proposal.md`）。邻近但不相同：谱偏置工作（Rahaman et al. 2019）在 `Idea_02/literature.md` 中被标为 "**adjacent**, not PEFT-delta" | 只有作为*因果干预*时才是空的。两个相邻的位置都已被占：纯评测已被杀（arXiv:2412.01240；arXiv:2510.21782；Trans10K+SAM evals），adapter-SOTA 已被杀（Med-SA arXiv:2304.12620 / MedIA 2025、SAMed、LoRA-MedSAM）—— `reviewer_summary.md` | 有争议。`reviewer_summary.md` 原样记录了这条攻击："Everyone already thresholds SAM IoU."。**只有**靠反校准证据才能存活 | 部分被占。"Med-SA claims PEFT avoids forgetting **without measuring** promptable zero-shot"（`raw/batch_X_hand.md`）—— 缺口是真的，但它是别人主张上的一个测量缺口 | 与 `X-0001` 同一个位置；`Idea_01/proposal.md` 的新颖性表把它对上 2412.04243 列为**竞争性机制**（objectness 在 \(D,p\) vs 纹理在 \(E\)） |
| **结果为 null 仍可发表？** | **可以，而且是明写的。** "If r64 already high-pass: kill HP method; **maybe still publish the audit as a short note**"（`Idea_02/experiments.md`） | 可以。"If H1 is false: … publish the negative as support for 2412.04243-style encoder limits"（`Idea_01/proposal.md`）；"If only H1: still a useful negative on encoder-adaptation narrative"（`Idea_01/roadmap.md`） | **作为主打不行。** "If only weakly calibrated, **kill and merge into Idea_01 analysis figure**"（`Idea_03/proposal.md`） | 两个方向都没有记录。整个目录树里 `X-0007` 都没有负结果条款 | 已被折进 Idea_01 的负结果条款；没有独立可发表的 null |
| **blast radius** | 广但间接：命中的是所有稠密 PEFT 的 rank 调参实践。`research_summary.md` 把 "highest chance to change *where* people spend PEFT parameters" 这句给的是 Idea_01 而不是它，然而 `evolution_summary.md` 在 ROI 上仍把 `X-0004` 排第一 —— 这是一处未被调和的张力，见 §5.2 | **五个里最广。** 若成立，"fine-tune / adapt the encoder" 这个默认做法就是走错了方向 —— `README.md`："the cheapest falsifier of the 'fine-tune the encoder' default" | 较窄：它改变的更多是部署与报告实践（弃答、risk-coverage），而不是模型设计 | 窄：只纠正一条关于 PEFT 与遗忘的、测量不足的主张 | 与 `X-0001` 的 blast radius 相同 —— 它们是同一个因果主张的两条臂，这也正是它们被合并的原因（§4.1） |
| **数据 / checkpoint 可得性** | **受阻最少。** 需要一个 LoRA checkpoint 或仓库内的 toy 训练器；器官数据集（Synapse/AMOS 子集）是公开研究数据集，不牵涉烟雾数据许可 | **受阻最重。** 需要真实 SAM 权重（"needs real SAM weights for science"，`README.md`）**并且**需要一个许可清晰的无定形数据集。已记录的退路："If licenses block, use a 200-frame hand-split from a CC-licensed smoke video — document provenance"（`Idea_01/experiments.md`） | 部分受阻：需要一个 SAM/SAM2 checkpoint，但它的 killer 只用 COCO + Trans10K 就能跑，因此**不依赖烟雾数据许可** | 卡在一套 PEFT 训练环境加一个 COCO 代理数据上 | 与 `X-0001` 卡在同样的地方 |
| **Stage-6 结果** | **→ Idea_02** | **→ Idea_01（主臂）** | **→ Idea_03** | **备选，未被杀掉**（§4.2） | **被吸收进 Idea_01（§4.1）** |

**FACT —— 适用于全部五个的横切约束。** `research_summary.md` → "Unresolved risks"："Smoke dataset licenses and SAM checkpoints not in this VM."。`README.md` 的项目状态把三个 package 都标为 *ready to start*，没有一个是已开始。因此**在 Stage 6 没有任何候选是基于实测证据被淘汰的**，因为根本不存在实测证据：`evolution_summary.md` 写明 "No actual experimental numbers were produced in this round."。

## 3. 三个胜出者：锁定理由、binding obligation、死亡条件

### 3.1 Idea_01 —— Objectness, Not Features（`IDEA-X-0001` + `IDEA-X-0002`，主打 package，#1 推荐）

**它赢在：blast radius × killer 成本，再加上一个尚空的 prior-work 位置。** 已记录的理由是 `README.md` → "Most recommended … **Idea_01.** It is the cheapest falsifier of the 'fine-tune the encoder' default, and prior work already occupied the eval-only and adapter-SOTA slots."。`research_summary.md` 又补上了那个决定性属性："Precise interaction hypothesis (win amorphous, lose COCO)."。它是五个中唯一一个：若主张为真，被推翻的是一种*当下的资源投入模式*，而不只是一种*报告习惯*。

**Binding obligation —— COCO 交互对照（H2）。不可省。**

- **FACT.** `research_summary.md` → "Unresolved risks"："Idea_01 can be **desk-rejected as a probe paper if the COCO interaction is omitted**."
- 操作上这就是 `Idea_01/proposal.md` 里已有的双边继续规则：只有当无定形上 NSD(B 或 C) > NSD(A) **且** COCO 上 NSD(B) < NSD(A) 时才继续。单边的无定形取胜*不算*通过。
- `Idea_01/reviewer_attacks.md` 指明了必需的产物："**Interaction plot:** amorphous gain × COCO loss (H2)"，同时还有三项该文件标为"能让质疑闭嘴"的义务：冻结 \(z\) 上参数量对齐的微型 U-Net、随机编码器对照、紧致度对齐的框（E1）。
- 还有一条出自 `Idea_01/reviewer_attacks.md` 的不可谈判项，原文照引因为它的措辞本身是绝对的：条件 B/C 与 zero-shot A 之间的训练数据不对称，必须被声明为"这是关于适配部位的问题"，"**say this in the intro or die**"。

**死亡 / 转向条件（全部有记录）。**

| 触发条件 | 动作 | 来源 |
|---|---|---|
| 无定形上 B ≪ A | **Kill。** 编码器才是瓶颈；明确禁止 "add adapters to 'fix' without new science" | `Idea_01/proposal.md` |
| 所有场景下 B ≈ A | **Pivot**，可能转成一篇校准论文 | `Idea_01/proposal.md` |
| IoU token 区分成功／失败的能力优于我们的头 | **Pivot 到 Idea_03** | `Idea_01/roadmap.md` |
| 补上 SAM2 + 紧致度对照后 H1 仍为假 | **Kill** | `Idea_01/roadmap.md` |
| H1 为假**且**随机特征编码器同样失败 | 解读为编码器能力上限，与 2412.04243 一致，发表负结果 | `Idea_01/experiments.md`、`Idea_01/proposal.md` |
| H1 为假**且**随机特征编码器*却奏效* | 这不是结果 —— 视为我们自己头部的数据泄漏／实现 bug | `Idea_01/experiments.md` |

### 3.2 Idea_02 —— Spectral Locality of Dense PEFT（`IDEA-X-0004`）

**它赢在：可证伪的精确度，以及负结果本身的价值。** 它是唯一在自己 proposal 中带有数值、可预注册阈值的候选（\(\|\delta\|_2^2\) 中 ≥80% 落在 \(k_c\) 以下，且 \(k_c\) 依 patch size 预先注册），也是唯一在失败情况下仍能产出可发表成果的（"maybe still publish the audit as a short note"，`Idea_02/experiments.md`）。`evolution_summary.md` 在 Stage-5 ROI 上把它排第 1。它同时也是受这台 VM 缺失资产阻碍最小的一个。

**它是在"会议契合度最弱"的情况下胜出的，而这一点被如实记录，没有被含糊掩过。** `research_summary.md` 的风险条目："Idea_02 may be 'not CV.'"。`research_ledger.md`："Confidence **medium-low (venue fit)**."。`Idea_02/reviewer_attacks.md` 的攻击："not a vision paper; LoRA math already low-rank; HP is just a conv."。尽管如此仍保留它的成文理由出自 `evolution_summary.md`："Decision: keep because it **predicts a *new adapter*** (high-frequency residual) if the spectrum claim holds" —— 也就是说，它是作为一个*建设性*主张被保留的，不是作为一份诊断。

**Binding obligation —— 参数量对齐的低通对照必须造成损害。** 这正是把"HP 只是又一个卷积"转化为频率主张的那条关键臂：

- `Idea_02/proposal.md` → "Control: low-pass residual with same param count should **hurt** NSD if the story is frequency."
- `Idea_02/reviewer_attacks.md` 把它列为义务 (2)，并用绝对措辞写明不跑它的后果："**If we cannot run (2), kill the method half and keep audit-only (weaker).**"
- 同一文件的另两项义务：(1) rank vs 频率的散点图，(3) 把 PEFT 之后的 COCO 可提示性作为第二条轴 —— 正是这一条把 `X-0007` 以备选身份留住（§4.2）。
- `reviewer_summary.md` 给出了面向评审的形态：针对 "LoRA is low-rank by definition so spectrum is obvious"，回答必须是 rank-64 LoRA vs rank-4 + 高频残差，并且 "the prediction is **NSD gap not Dice gap**"。

**死亡 / 转向条件（全部有记录）。**

| 触发条件 | 动作 | 来源 |
|---|---|---|
| H1 在**两个** backbone 上都为假 | **Kill** | `Idea_02/roadmap.md` |
| r64 本来就是高通的 | **杀掉 HP 方法那一半**，把审计留作 short note | `Idea_02/experiments.md` |
| 低通对照根本跑不了 | **杀掉方法那一半**，只保留审计 | `Idea_02/reviewer_attacks.md` |
| killer 为负结果，且遗忘成为剩下唯一的故事 | 激活 `X-0007`（§4.2） | `eliminated_ideas_summary.md` |

### 3.3 Idea_03 —— Selective SAM via IoU-token Recalibration（`IDEA-X-0003` + `IDEA-A-0064`）

**它赢在：killer 成本，以及它是唯一一个 killer 既不需要训练、也不需要烟雾数据许可的候选。** `Idea_03/proposal.md`："**Zero training**: dump SAM2 IoU tokens vs GT IoU on 100 COCO vs 100 Trans10K/smoke. Plot reliability."。按 "ROI = information per GPU-hour" 这条判据，它是五个中的极值点。

**Binding obligation —— 必须证明的是"反校准"，不是"弱校准"。** 这个区分就是整篇论文本身：

- **FACT.** `evolution_summary.md` → Stage-6 分歧："Decision: keep **if** we show SAM IoU is *anti-calibrated* on amorphous targets (**not merely weakly calibrated**)."
- `reviewer_summary.md`：针对 "Everyone already thresholds SAM IoU"，回答必须是 "reliability diagrams showing **anti-calibration** (higher IoU token → higher error) on amorphous sets"。
- `Idea_03/reviewer_attacks.md` 又补了两项义务："anti-calibration (**not just ECE>0**); coverage curves; reject **images** vs **pixels** (two protocols, **pre-registered**)"。
- 形式化地说这就是 `Idea_03/proposal.md` 的 H2：在无定形数据集上 Spearman ρ "drops and may go **negative**"。一个"为正但很小"的 ρ 不满足该义务。

**死亡条件 —— E0 若没有校准域差，它就死。这是三者中最硬的一条 kill 线。**

| 触发条件 | 动作 | 来源 |
|---|---|---|
| E0 未显示校准上的领域差异 | **Kill** | `research_summary.md`（"Idea_03 dies if E0 shows no calibration domain gap"）；`Idea_03/roadmap.md`（"Kill if no domain gap in E0"）；`research_ledger.md`（"Confidence medium; **dies on E0**"） |
| 无定形上 ρ 依然很高 | **Kill H2** —— 也就是核心假设 | `Idea_03/proposal.md` |
| 只是弱校准（有差距但无符号反转） | **作为主打杀掉**，并作为分析图并入 Idea_01 | `Idea_03/proposal.md` |

## 4. 没有成为 package 的两个候选

**FACT，直说，因为它决定了这一次 Stage 6 能承载多少分量：两个都没有被杀掉。** 五条 Stage-5 条目里，四条在 Final 3 之内，第五条被搁置。Stage 6 没有任何东西死亡。一个没有淘汰掉任何候选的 battle 阶段是一个弱的 battle 阶段；这里把它作为一个观察记录下来，不为它开脱。这同时也意味着"5 → 3"的收缩在算术上是**一次合并加一次搁置**，而不是三个胜者战胜两个败者。

### 4.1 `IDEA-X-0002` Density decoder on frozen SAM —— **被吸收（ABSORBED）**（既不是备选也不是杀掉）

**FACT.** `evolution_summary.md` → "Stage 5 Top 5 (ROI order)" 第 5 条在行内就写明了处置："IDEA-X-0002 Density decoder on frozen SAM embeddings **(merged into Idea_01 method)**."

package 本身也印证了这一点：密度头*就是* Idea_01 的方法，而不是它旁边的一个选项。`Idea_01/proposal.md` 的第 2 步就是 "**Density head** \(h_\theta(z)\)"；E0 的条件 B 就是 "Frozen linear/density head"；代码产物是 `Idea_01/src/train_density_head.py`；toy checkpoint 是 `Idea_01/outputs/idea01_e0/density_head.pt`。`IDEA-X-0001` 的排除区则以条件 C 的形式进入，即 "B + exclusion channel"。所以 `X-0001` 与 `X-0002` 是同一个交互检验的两条臂，这正是它们占一个 package 而不是两个的原因。

**不存在激活条件** —— 它作为 Idea_01 的一部分本来就已经处于激活状态。如果 Idea_01 死了，`X-0002` 随之而死；没有任何记录给出一条"`X-0002` 在 Idea_01 被杀后仍能存活"的路径。

### 4.2 `IDEA-X-0007` Replay for promptability —— **备选（BACKUP）**，且有成文的激活条件

**FACT.** `eliminated_ideas_summary.md` → "Parked high-ROI (not final 3)"："`X-0007 Replay promptability` | Why parked: **Strong**; overlaps Idea_02 forgetting subplot | **Revive if: Idea_02 killer is negative and forgetting is the remaining story**."

因此激活条件是明确的，而且挂在 **Idea_02** 身上，不是 Idea_01 或 Idea_03：如果 Idea_02 的谱 killer 返回负结果，而存活下来的故事是"可提示接口的遗忘"，那么 `X-0007` 就被提拔。

**它其实已经作为一条子轴被部分接入，只是还没被提拔。** `Idea_02/reviewer_attacks.md` 的义务 (3) 就是 "COCO promptability after PEFT (**link X-0007**) as a second axis"。所以 `X-0007` 今天已经在为 Idea_02 贡献一条实验轴，只有在上述复活条件下才成为主打。

**缺口，只记录不填补。** `X-0007` 在整个目录树里都没有负结果条款，因此如果它被提拔，它会是五个里唯一一个没有成文"万一是 null 怎么办"答案的。`eliminated_ideas_summary.md` 里的通用漏斗规则 —— "A killed idea is revived only if a new experiment would change the final-3 ranking" —— 管的是提拔本身，但对提拔之后会发生什么一字未提。

## 5. 保留的分歧（明确列出）

有三处分歧在当时就被记录了，这里按实质原样抄录。另有两处是本次事后补记环节发现的，并如实标注为此。**其中任何一处都没有被制造出虚假共识。**

### 5.1 当时就有记录的（来源：`evolution_summary.md` → "Stage 6 unresolved disagreements"）

1. **Idea_01 究竟是"只是提示／评测"，还是一次针对 objectness 的因果干预？** 双方立场被记录为 *Skeptical PI* vs *Segmentation expert*。**没有记录任何结论** —— `evolution_summary.md` 列出它就停下了。§3.1 的 binding obligation 存在的目的正是用实证来了结这场分歧：COCO 交互效应就是分开"probe 论文"与"因果部位"的那条界线。
2. **Idea_02 算是视觉贡献还是一份 PEFT 诊断？** 立场被记录为 *Methodology reviewer*。**已裁定为保留**，且理由有记录："keep because it predicts a *new adapter* (high-frequency residual) if the spectrum claim holds."。但分歧并未因此消解 —— `research_summary.md` 仍把 "Idea_02 may be 'not CV'" 列为在活的风险，`research_ledger.md` 仍把会议契合度的信心评为 "medium-low"。
3. **Idea_03 是否只是经典的选择性分类？** **有条件地裁定**："keep if we show SAM IoU is *anti-calibrated* … (not merely weakly calibrated)."。截至撰写本文，该条件尚未被满足，所以这场分歧在实践上仍然是开放的。

### 5.2 本次事后补记发现的 —— 执行顺序存在矛盾

**FACT.** 有两处已记录的顺序在"先跑什么"上互相冲突。

- `evolution_summary.md` 的 Stage-5 ROI 排序把 `IDEA-X-0004`（Idea_02）排在第 1，在 Idea_01 的各条臂之前。
- `README.md` → "Next experiment to run: **Idea_01 E0**"，以及 `research_summary.md` → "First experiment to run: `Idea_01` E0"。

两个文件说 Idea_01 优先，一处排序说 Idea_02 优先。§6 采用两文件的多数意见（先跑 Idea_01 E0），因为那是更明确的指令，同时把这处矛盾标出来而不是悄悄选一个。**请人工裁决。**

另外还存在第三种立场，但没有任何文件写过它，所以不予采纳：纯从"门禁效率"论证，Idea_03 的 E0 是唯一既不需训练也不需烟雾许可的 killer，因此它是删掉三个 package 之一的最便宜手段。如实标注 —— 这属于本审计员的 **SPECULATION**，不是 Windows8 记录在册的决策，并且被有意地不用于重排 §6。

### 5.3 本次事后补记发现的 —— 本轮的方法学缺陷

**FACT.** Windows8 的 Stage 6 **没有独立的 rejector。** 证据全部来自已有文件：

- `supervisor_log.md` 没有记录任何 Stage-6 派发、任何 rejector agent id、任何投票。
- 分歧清单中点名的三个角色都没有 agent id，这与 Stage-1 批次 agent 不同，后者是有的（`bc-c89434d9-…`、`bc-3afc797e-…`、`bc-4a5961ff-…`，加上重试的 `bc-7a636a75-…`、`bc-fb91c4d2-…`）。
- 三个最初的 Stage-1 云端子 agent 全部 ERROR，两个批次是由**本地** file-writer 补救的 —— 因此本轮从来没有在任何阶段成功运行过一个独立的对抗性 agent。
- `reviewer_summary.md` 的对抗性章节只是一个 "Reviewer #2" 人格，而它的偏见检查明确写着是 "Supervisor **self**-check"。
- 那份自查自己点出了暴露面："Bias risk: over-weighting SAM… Bias risk: over-weighting smoke."。两个风险在结果里都看得见 —— 三个 package 全是 SAM 家族，其中两个依赖无定形／烟雾类目标。

**这对"这次 Stage 6 能证明多少"意味着什么。** §5.1 里的三处分歧是真实记录，但它们是由同一个 Supervisor 表述出来的立场，不是独立 rejector 的产出。Windows4 那句 "three independent rejectors" 的 Stage-6 主张不能挪用到 Windows8 上。这一点被登记为 **Windows8 这一轮的方法学缺陷**，它是替代"编造一场多 agent 辩论"的那个诚实答案。

**相关内容，且已在别处记录 —— 不在此重复争论。** `stage5_top5.md` §4 与 §5（由 2026-08-29 的 Stage-5 审计环节补入）记录了：`stage2_top200.md` 是想法网格的一个机械前缀，只覆盖 52 个 core 中的 10 个；`stage3_top50.md` 的 50 个 ID 里有 30 个从未出现在 `stage2_top200.md` 中；以及为 Final 3 引用的三个血统标记（`LINEAR-PROBE` = `IDEA-A-0316`、`PEFT-SPECTRAL` = `IDEA-A-0211`、`SELECTIVE` ≈ `IDEA-A-1051`）都无法穿过 Stage 4 被追溯。这些缺陷位于 Stage 6 的上游，并已在那个文件里被送去人工裁决。

## 6. 决定性实验 —— 必须遵守的执行顺序

下面的顺序遵循 `README.md` 与 `research_summary.md`（与 ROI 排序的矛盾见 §5.2）。**所有成本都是已记录的估计值；这些估计本身即为 HYPOTHESIS，因为什么都还没跑过。** 阈值都从各 package 引用而来；凡某个 package 把阈值留成定性表述的，都被标为需要在开跑*之前*补齐的预注册缺口，而不是边跑边定。

### 第 1 步 —— Idea_01 E0（objectness killer）

- **设置（FACT，按已有记录）：** 在 200 张无定形 + 100 张 COCO 图像上缓存冻结的 SAM embedding；训练 `DensityHead`；条件 A = 带 GT 框提示的 SAM，B = 冻结密度头，C = B + 排除通道。见 `Idea_01/experiments.md`、`Idea_01/roadmap.md`（"Day 1 … **Stop criteria applied the same evening**"）。
- **成本估计（HYPOTHESIS）：** 1 张 12–24 GB GPU，含 embedding 缓存共 < 8 小时。
- **当前尚未满足的前置条件（FACT）：** 真实 SAM 权重，加上一个许可清晰的无定形数据集；已记录的退路是从一段 CC 许可的烟雾视频中手工切出 200 帧并记录来源出处。
- **判定规则（FACT，出自 `Idea_01/proposal.md`）：**

| 结果 | 动作 |
|---|---|
| 无定形上 NSD(B 或 C) > NSD(A) **且** COCO 上 NSD(B) < NSD(A) | **继续**进入第 1b 步 |
| 所有场景下 B ≈ A | **Pivot**（候选方向：校准论文） |
| 无定形上 B ≪ A | **Kill** Idea_01；不要用 adapter 去打补丁 |
| 无定形赢了但 COCO **没有**输 | **不得就此推进** —— 这正是 `research_summary.md` 点名的 desk-reject 形状；构成论文的是交互效应，而不是取胜本身 |

- **预注册缺口（已标记）：** "≈" 和 "≪" 在任何文件里都没有数值余量，也没有指定随机种子数量或显著性检验。**HYPOTHESIS：** 没有预注册的余量和重复次数，第 1 步自己的停止规则是不可判定的。开跑前必须补上。
- **第 1b 步，同一道门，任何主张离开房间之前必须完成（FACT，出自 `Idea_01/reviewer_attacks.md` 与 `experiments.md` E1–E3）：** 紧致度对齐的框、随机编码器对照、SAM2 冻结编码器、参数量对齐的微型 U-Net。`Idea_01/roadmap.md` 把这些安排在 Day 2–3。注意随机编码器对照已被记录的读法：若 H1 失败*且*随机特征也失败 → 编码器能力上限（一个真实的负结果）；若 H1 失败*且*随机特征**却奏效** → 视为我们自己的泄漏／bug，不是发现。

### 第 2 步 —— Idea_02 FFT 审计（谱 killer）

- **设置（FACT）：** 在一个小规模器官数据集（Synapse/AMOS 子集）上做 LoRA；在 64 张图像上缓存 \(\delta\)；径向功率谱；统计 \(k_c\) 以下的能量占比。Day-1 退路明确允许 "any LoRA checkpoint or the toy trainer in `src/`"（`Idea_02/roadmap.md`）。
- **成本估计（HYPOTHESIS）：** killer < 1 GPU-day；完整 Synapse/AMOS 需 3–5 天。
- **判定规则（FACT，出自 `Idea_02/proposal.md`、`experiments.md`、`roadmap.md`）：**

| 结果 | 动作 |
|---|---|
| \(\|\delta\|_2^2\) 中 ≥ 80% 落在预注册的 \(k_c\) 以下**且** r64 没有把能量搬到 \(k_c\) 之上 | **继续**进入 r4 vs r64 vs r4+HP 那条臂 |
| 参数量对齐条件下 r4+HP 在 **NSD** 上胜过 r64（Dice 可以持平） | **继续** —— 建设性主张成立 |
| 参数量对齐的**低通**残差*没有*损害 NSD | **杀掉方法那一半**，只保留审计 —— 频率这套叙事得不到支持 |
| 低通对照根本跑不了 | **杀掉方法那一半**，只保留审计 |
| r64 本来就是高通的（H1 为假） | **杀掉 HP 方法**；审计本身仍可作为 short note 站得住 |
| H1 在**两个** backbone 上都为假 | **Kill Idea_02**，并按 §4.2 评估是否提拔 `X-0007` |

- **预注册缺口（已标记）：** \(k_c\) 必须依 patch size 定下来*并写进文件*，且要在第一次 FFT 之前完成。80% 这个数已经预注册了；\(k_c\) 本身在任何文件里还不是一个具体数字。

### 第 3 步 —— Idea_03 E0（校准 killer）

- **设置（FACT）：** 零训练；在 100 张 COCO vs 100 张 Trans10K／烟雾图像上导出 SAM/SAM2 的 IoU token 与真实 GT IoU；绘制可靠性图；随后在 val 上做 isotonic、在 test 上算 risk-coverage（Day 2–3）。
- **成本估计（HYPOTHESIS）：** 只做推理，无训练；三者中预算最小。没有记录任何具体数字，因此这里也不断言。
- **判定规则（FACT，出自 `Idea_03/proposal.md`、`roadmap.md`、`research_summary.md`、`evolution_summary.md`）：**

| 结果 | 动作 |
|---|---|
| COCO 上 ρ 为正且 ECE 低于预注册的界，**且**无定形上 ρ 掉到 ≈0 或**为负** | **继续**进入 isotonic + risk-coverage |
| 存在领域差距但**无符号反转**（只是弱校准） | **作为主打杀掉**；作为分析图并入 Idea_01 |
| 无定形上 ρ 依然很高 | **Kill** H2，Idea_03 随之而死 |
| 完全没有校准上的领域差异 | **Kill Idea_03** —— 本轮最硬的那条 kill 线 |

- **预注册缺口（已标记）：** `Idea_03/proposal.md` 要求 "ECE below a **pre-registered bound**"，但任何地方都没有写下这个界；同样，H3 的覆盖率目标在 proposal 里写作 "cover 80%"、在预期里写作 "coverage 80%"，但 `reviewer_attacks.md` 要求预注册的"图像级 vs 像素级"协议划分至今没有指定。两者都必须在 E0 之前定下来，否则 E0 杀不了任何东西。

### 跨步骤的相互作用（有记录，不是发明的）

- 第 1 步 → 第 3 步：如果 Idea_01 的 E0 显示 IoU token 区分成功与失败的能力优于密度头，`Idea_01/roadmap.md` 规定**转向 Idea_03**。所以第 1 步的失败可以*强化*第 3 步，而不是白跑一趟。
- 第 3 步 → 第 1 步：只有弱校准这一结果会把 Idea_03 的内容作为分析图送进 Idea_01（`Idea_03/proposal.md`）。
- 第 2 步 → `X-0007`：谱 killer 为负结果、而遗忘成为存活故事时，备选被提拔（`eliminated_ideas_summary.md`）。
- **值得点明的后果（HYPOTHESIS）：** 这三个 package 不是相互独立的赌注。Idea_01 与 Idea_03 各自都能吸收对方的失败，而 Idea_02 会把接力棒交给一个备选。因此相关性失败是相当可能的：一个共因失败 —— 拿不到 SAM checkpoint，或拿不到许可清晰的无定形数据 —— 会同时干掉第 1 步和第 3 步，因为两者都需要真实 SAM 权重。`research_summary.md` 已经把这个暴露面列出来了。

## 7. Battle 收尾

**FACT.** Stage-5 那五个候选中，没有任何一个是在 Stage 6 基于证据被淘汰的，因为当时没有任何实验跑过。`evolution_summary.md`："6 Battle | 3 | **3** | No false consensus; remaining disagreements listed below"，以及 "No actual experimental numbers were produced in this round."。Final 3 是基于已记录的*先验*判断锁定的 —— 成本、可证伪性、prior-work 占位、blast radius —— 不是基于测量。本文件把这一点作为事实状态记录下来，而不是把它包装成一场已经裁决过的比赛。

## 8. 漏斗完整性索引

| 层级 | 目标 | 存档文件 | 已记录数量 |
|---|---|---|---|
| 1 原始生成 | ≥ 1000 | `raw/pool.jsonl`（+ `raw/batch_A|B|C.md`、`raw/batch_A|B|C_prior.md`、`raw/batch_X_hand.md`） | 2766 |
| 2 评审 | 约 200 | `stage2_top200.md` | 200 |
| 3 Prior-work 攻击 | 约 50 | `stage3_top50.md` | 50 |
| 4 Reviewer #2 | 约 20 | `stage4_top20.md` | 19 |
| 5 工程化 / ROI | 约 5 | `stage5_top5.md` | 5 |
| 6 Battle | 3 | **`stage6_battle.md`（本文件）** + `Idea_01/`、`Idea_02/`、`Idea_03/` | 3 |

现在每一层都有文件了。**但这不等于每一层都可审计** —— `stage5_top5.md` §4 记录的 Stage-2 与 Stage-2→3 缺陷仍然未解决，`stage5_top5.md` §5 里那三个血统标记也一样。

## 9. 本文件的证据分级声明

- **FACT** —— 本目录树中某个文件写了什么，以及那些已被核实为"不存在"的事项（`supervisor_log.md` 中没有 Stage-6 派发；Stage-6 各角色没有 agent id；在本文件之前不存在任何 Stage-6 文件）。
- **VERIFIED PRIOR WORK (as recorded)** —— 各条 prior-work 攻击及其标识（Med-SA arXiv:2304.12620 / MedIA 2025；SAMed arXiv:2304.13785；LoRA-MedSAM；MedSAM arXiv:2304.12306；SAM arXiv:2304.02643；SAM 2 arXiv:2408.00714；HQ-SAM arXiv:2306.01567；arXiv:2412.01240；arXiv:2412.04243；arXiv:2510.21782；Trans10K；nnU-Net Nature Methods 2021；LoRA ICLR 2022；Rahaman et al. 2019；Geifman & El-Yaniv；Guo et al.；CC-Dice AAAI 2025）都是从 `reviewer_summary.md`、`eliminated_ideas_summary.md` 以及三个 `literature.md` 文件抄录的。**本次没有拿它们中的任何一条去与文献重新核对，也没有新增任何论文、引用、会议或作者。**
- **HYPOTHESIS** —— §2.1 中的每一条判据判断、§6 中的每一个成本估计，以及关于某个未执行实验将如何表现的每一条主张。
- **SPECULATION** —— 在行内标注，全文只用了一次（§5.2，关于先跑 Idea_03 的门禁效率论证），并且明确没有据此行动。
- **EXPECTED RESULT** —— 仅出现在某个 package 本身已经给出预测的地方，例如 `Idea_01/proposal.md` "Amorphous NSD: C ≥ B > A; COCO: A > B"；`Idea_02/proposal.md` "Dice: r64 ≈ r4+HP > r4. NSD: r4+HP > r64 ≥ r4"；`Idea_02/experiments.md` "Predicted: random 3×3 ≈ LoRA extra rank (no NSD gain)"；`Idea_03/proposal.md` "H1 true, H2 true, coverage 80%"。
- **ACTUAL RESULT —— 无。** 本文件中没有任何内容被套上这个标签；这一条就是它唯一的出现位置。整个目录树里唯一的数值产物都是 toy 或合成的，并且都自带标注：`Idea_01/outputs/idea01_e0/toy_report.txt`（"TOY RUN (FakeEncoder). NOT a scientific result."）及其配套的 `density_head.pt`、`Idea_02/outputs/idea02_fft/toy_report.txt`（"TOY LoRA on random tensors. NOT a scientific result."）、`Idea_03/outputs/idea03_e0/toy_report.txt`（"SYNTHETIC illustration of H1/H2. NOT measured on SAM."）。按 `README.md` 的规定，"Do not report FakeEncoder numbers as results" —— 这些文件里的任何数值都没有在本文件中被复述来支持或反驳任何假设，也没有任何这样的数值影响过上文的任何裁决。
- **没有编造流程。** 凡 `evolution_summary.md`、`reviewer_summary.md` 或各 package 的 `reviewer_attacks.md` 中没有记录过的评审 agent、投票、评分、排名会议或辩论，本文件一律不作断言。凡记录沉默之处，§5.3 就直说记录是沉默的。
