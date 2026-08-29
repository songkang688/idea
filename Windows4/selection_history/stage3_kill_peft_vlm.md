# Stage 3 — 前序工作狙杀（Prior-Work Assassination）：PEFT / Forgetting / VLM / Annotation-Efficiency 聚类

角色：前序工作狙杀者（Prior-Work Assassin）。默认假设：**已经发表（already published）**。日期：2026-08-28。
范围：从 `stage2_top200.md` 分配的 18 个聚类（聚类线索列表中的聚类 8, 18–24, 32–39, 43–45，外加 A1-107/A1-108）。
方法：**仅基于网络核实的真实论文。** 下文所有承重引文除非标有 `[M]`（= 凭借记忆引用的经典工作，极高置信度确认其存在，但在论文中引用前需重新核对 arXiv ID），均在此轮中完成获取与阅读。无标记 / `[V]` = 本轮已核实（已获取摘要或全文）。

认识状态（Epistemic status）：关于新颖性的评审判断（REVIEW JUDGMENT）。下文无任何主张属于我们自身的实验结果。

依据评审标准的裁决标尺：
- **重合度（Overlap）**：NONE（无可靠前序工作），SLIVER（部分重合；仍保留可辩护的增量 delta），REAL（核心主张或其决定性版本已发表）。
- **裁决（Verdict）**：KILL（无具备可发表性的 delta），MUTATE（仅能以修改后的形式存活；已明确修改方案），SURVIVE（delta 真实存在；列出了求差对比 obligations 义务）。
- **R2 攻击论文（R2 attack paper）**：怀有敌意的审稿人在拒稿意见中会直接粘贴的那篇单一论文。

虚假新颖性违禁模式检查（Banned-pattern check，引自 `stage2_review_C1_audit.md`）：每项裁决均指明该设想冒了哪种虚假新颖性模式（F1–F9）的风险；F2 = 无分歧机制的分类到分割移植（cls→seg port without divergence mechanism），F3 = 提示微扰失忆（prompt-perturbation amnesia），F5 = 权重算术移植（weight-arithmetic port），F7 = 收敛重复的双重计数（convergent-duplicate double counting），F8 = 稻草人假设（strawman assumption）。

---

## 记分板（Scoreboard）

| # | 聚类（Cluster） | ID 列表 | 重合度（Overlap） | 裁决（Verdict） |
|---|---|---|---|---|
| 1 | PEFT tax on SAM promptability | S-141, C1-097, C1-065 | REAL (现象) / SLIVER (审计) | S-141 KILL · C1-097 MUTATE · C1-065 SURVIVE |
| 2 | Random LoRA ≈ trained | S-148 | REAL | KILL (降级为对照分支) |
| 3 | Protocol forgetting boxes→points | S-176 | SLIVER | MUTATE |
| 4 | Forgetting in decoder not encoder | S-177, C1-062 | SLIVER | SURVIVE (带求差对比) |
| 5 | Plasticity too small → forgetting is noise | S-183, C1-082 | SLIVER | SURVIVE (作为守门审计) |
| 6 | FT calibration tax | C1-025, C1-031, C1-037, S-318 | SLIVER | MUTATE (合并；C1-031 为核心) |
| 7 | Pretrain-harm small-n | S-052 | SLIVER | MUTATE |
| 8 | PEFT vs tuned full-FT honesty | C1-053 | REAL | KILL (并入 #1) |
| 9 | PEFT data-size crossover | C1-057 | REAL | KILL (仅作为报告分支) |
| 10 | Gain–retention frontier | C1-110 | REAL (组件) | MUTATE |
| 11 | LoRA placement vs error type | A1-107 | NONE→SLIVER | SURVIVE |
| 12 | Encoder–decoder contract drift | A1-108, C1-067 | SLIVER (正在缩窄) | MUTATE |
| 13 | VLM prior harms rare/atypical + negation | S-228, S-240, B1-107 | REAL (否定, 频率) / SLIVER (稠密) | S-240 KILL · S-228 MUTATE · B1-107 SURVIVE |
| 14 | AL / semi-sup dead under VFM init | B1-011, B1-025 | REAL | KILL 两者 |
| 15 | Copy-paste ≥ diffusion synth | B1-051 | SLIVER | SURVIVE |
| 16 | Histogram matching explains UDA | B1-061 | REAL (精神实质上) | MUTATE |
| 17 | FSS support variance / background cheat | B1-074, B1-079 | SLIVER | B1-074 MUTATE · B1-079 SURVIVE |
| 18 | CLIP dense linear realignment | B1-097 | REAL | KILL |

净结果：7 个 KILL，6 个 MUTATE，5 个 SURVIVE（按子 ID 计算：10 个 kill 级别，8 个 mutate，7 个 survive）。

---

## 1. PEFT 对 SAM 可提示性的代价（PEFT tax on SAM promptability） — S-141（"LoRA on SAM encoder destroys promptability"），C1-097（SAM 的统一 PEFT 复现审计），C1-065（提示类型特异性遗忘）

**最接近的真实论文**
- Gu et al., *How to build the best medical image segmentation algorithm using foundation models: a comprehensive empirical study with Segment Anything Model*, MELBA 2025, arXiv:2404.09957 `[V]`。18 种微调组合（3 个 backbone × encoder/decoder × 原生/LoRA/Adapter）× 17 个数据集。明确记录了**原生全量微调会导致模型崩塌/灾难性遗忘（model collapse / catastrophic forgetting）**（在 ViT-B/H 上），以及在 encoder+decoder 中使用 PEFT 表现更优；明确 "demonstrate[s] the ineffectiveness of some methods popular in the literature"；包含了 decoder-only FT（其 "FT-SAM" 风格分支）以及基于 prompt 的设置。
- *Continual Alignment for SAM (CA-SAM)*, arXiv:2511.17201 `[V]`。在动机中指出微调后的 SAM "tend to erode SAM's generalization, yielding poor OOD performance"，并构建了一种逐任务自适应的方法，**同时保留在未见医疗数据集上的 zero-shot 行为**（9 个数据集的持续学习 benchmark）。
- EvoSAM, arXiv:2503.06236 `[V]`：基于 LoRA 专家的持续 SAM，对比应用于 SAM/MedSAM 的持续学习基线进行了 benchmark 评测 — "SAM 存在遗忘并对其修复" 的赛道已被占据。
- Zhang & Liu, SAMed, arXiv:2304.13785 `[M]`；Wu et al., Medical SAM Adapter（在我们的 anchors 中）— SAM 上构建型 PEFT 赛道已高度饱和。
- Kumar et al., *Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution*, ICLR 2022, arXiv:2202.10054 `[M]`；Wortsman et al., WiSE-FT, CVPR 2022, arXiv:2109.01903 `[M]` — 通用的 "adaptation costs zero-shot robustness" 结论。

**他们做了什么 vs. 我们主张了什么。** S-141 的核心论点（"PEFT/FT erodes SAM's zero-shot ability"）现在已是*动机章节的陈词滥调（boilerplate）* — CA-SAM 带着引用给出了这一定论，Gu et al. 测量了崩塌，Conv-LoRA (arXiv:2401.17868 `[V]`) 将 "preserves SAM's segmentation knowledge" 作为卖点进行宣传。C1-097 的复现论题（"half of PEFT-for-SAM methods fail to beat a tuned decoder-only baseline"）已被 Gu et al. 实质性执行：同等预算统一协议、decoder-only 分支，并证明文献中流行的方法无效。

**保留的确切差异。** 尚无人**在匹配域内增益的前提下，按提示类型、在留出的自然类别上从行为层面测量该代价**：zero-shot box vs point vs negative-click vs multimask 多样性保留（C1-061 的多样性崩塌），同时控制学习率混淆项（C1-076）和阈值伪影（C1-082）。Gu et al. 测量的是域内 Dice；CA-SAM 测量的是*其自身方法*的 OOD Dice，而非对该领域各 checkpoint 的受控审计。

**重合度（Overlap）：** 现象本身以及统一复现框架为 REAL；按提示类型细分的行为审计为 SLIVER。置信度：High（三个独立核实的来源）。违禁模式风险：F7（3次收敛确实是预警，判断准确）。

**R2 攻击论文：** Gu et al. arXiv:2404.09957 (+ CA-SAM arXiv:2511.17201)。

**裁决（Verdict）：** S-141 作为独立的 "document the harm" 论文予以 **KILL**。C1-097 **MUTATE**：放弃复现框架（已被 Gu et al. 完成），仅保留在*已发布* checkpoint 上的预注册排名反转测试。C1-065 **SURVIVE** 作为该聚类的核心：可提示性代价测试套件（逐 prompt 类型的 zero-shot 保留 + 歧义性遗忘），明确与 Gu et al. 的 §prompt 实验以及 CA-SAM 的 OOD 表格进行求差对比。

---

## 2. 随机 LoRA ≈ 训练所得 — S-148（"random LoRA directions with same rank almost match trained LoRA on seg"）

**最接近的真实论文**
- Kopiczko, Blankevoort & Asano, *VeRA: Vector-based Random Matrix Adaptation*, ICLR 2024, arXiv:2310.11454 `[V]`。**冻结的、随机初始化的、跨层共享的低秩矩阵**，仅配合微小的可训练缩放向量，即可在 GLUE、E2E、图像分类以及 7B/13B 指令微调上**匹敌 LoRA**。
- Aghajanyan et al., *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning*, arXiv:2012.13255 `[M]`；Li et al., *Measuring the Intrinsic Dimension of Objective Landscapes*, ICLR 2018, arXiv:1804.08838 `[M]` — 在**随机子空间**内训练已足矣；"方向并不重要，容量才是关键" 这一观点已有十年的证据支持。

**他们做了什么 vs. 我们主张了什么。** VeRA 确切就是 "random directions + minimal calibration ≈ trained LoRA"，并在包括视觉在内的各模态上得到了展示。S-148 当初受保护所依赖的“震撼点”（"if random matches trained, the PEFT literature loses its floor"）此前已经发生过了，且该领域已将其吸纳为一种*方法*（VeRA 已进入 HuggingFace PEFT）。

**保留的确切差异。** 仅在于“在 SAM / 稠密 mask 上”的具体实例化，以及更极端的字面理解（*零*训练缩放 — 这几乎必定是错误的且无趣：未经训练的随机 ΔW 只是注入噪声）。分割专用的版本与 VeRA 相比无法预测出任何差异 — 属于违禁模式 F2（无分歧机制的移植）。

**重合度（Overlap）：** REAL。置信度：High。**R2 攻击论文：** VeRA arXiv:2310.11454。

**裁决（Verdict）：** 作为论文予以 **KILL**。挽救方案：随机方向 PEFT（VeRA 风格）成为聚类 1 审计中的**强制对照分支** — 任何 SAM 专用的 PEFT 增益都必须超越它。这是基线，而非假设。

---

## 3. 协议遗忘：框到点（Protocol forgetting boxes→points） — S-176（"train on boxes, point Dice crashes below frozen SAM"）

**最接近的真实论文**
- Ma et al., *Segment Anything in Medical Images* (MedSAM), Nature Communications 2024, arXiv:2304.12306 `[M]`。仅在 box 上训练；论文和代码库记录了点提示不支持/效果差 — 社区早已知晓针对 box 特化的微调无法迁移至点。
- Cheng et al., SAM-Med2D, arXiv:2308.16184 `[V]`。**之所以采用 box+points+masks 微调正是因为**提示模式覆盖率至关重要，并报告了 SAM vs FT-SAM vs SAM-Med2D 完整的 Bbox/1pt/3pt/5pt 表格（SAM 1pt 为 18.94 Dice，而 FT 变体为 60–70）— 微调后按提示模式细分的评估已经存在。
- Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024, arXiv:2304.14660 `[M]`（我们自己的 anchor）：冻结 SAM 的 prompt-type 敏感性已绘制完成。

**他们做了什么 vs. 我们主张了什么。** 组成要素（微调后的提示模式表格；无法支持点的 box-only 模型）均已发表。*尚未*发表的是：**被表述为遗忘的模型内部提示迁移矩阵** — 在协议 A 上微调，测量在协议 B 上**相对于冻结模型**的退化（"drops below frozen SAM" 是可证伪的新内容），包括负点击和迭代精细化深度（C1-063），且排除了阈值重新调整（C1-082）的因素。

**重合度（Overlap）：** SLIVER。置信度：Medium-High（在 2025-26 年的 workshop 中可能存在直接的 "prompt-protocol forgetting" 论文；本次审查中未发现）。**R2 攻击论文：** SAM-Med2D + MedSAM（"we already know box-only can't point — so what?"）。

**裁决（Verdict）：** **MUTATE**：合并入 C1-065 测试套件（聚类 1 的存活者）。该独立主张只是其他论文已经部分包含的表格；存活的内容是*低于冻结基线*的回归分析及其提示类型排序。

---

## 4. 遗忘发生在 Decoder 而非 Encoder — S-177（冻结消融），C1-062（交叉注意力重新拼接可恢复 zero-shot）

**最接近的真实论文**
- Ramasesh et al., *Anatomy of Catastrophic Forgetting: Hidden Representations and Task Semantics*, arXiv:2007.07400 `[M]`：遗忘集中在更深层（分类）。
- Davari et al., *Probing Representation Forgetting in Supervised and Unsupervised Continual Learning*, CVPR 2022, arXiv:2203.13381 `[M]`：表征层 vs 输出层遗忘探针。
- Lee et al., *Surgical Fine-Tuning Improves Adaptation to Distribution Shifts*, ICLR 2023, arXiv:2210.11466 `[M]`：应微调哪个 block 取决于分布偏移类型 — 属于位置问题的建设性孪生篇。
- Gu et al. arXiv:2404.09957 `[V]`：SAM 的 encoder vs decoder 微调分支已经存在（作为性能分析而非遗忘位置分析）。
- CA-SAM arXiv:2511.17201 `[V]`：将自适应问题定位在 **encoder–decoder 接口处**（其 Alignment Layer）— 证明接口化框架正在演变为方法。

**保留的确切差异。** 尚无论文在可提示的 mask decoder 上进行**因果层置换 / 重新拼接恢复（causal layer-swap / re-splice restoration）**：将微调前（pre-FT）的 prompt 交叉注意力拼接回微调后的 SAM 中，并测量能恢复多少 zero-shot 能力。分类中“深层会遗忘”的结论无法预测遗忘存在于 encoder（近似冻结）/ prompt-decoder 架构的何处 — 这里存在真正的分歧机制（prompt 交叉注意力没有分类的类比物），从而清除了违禁模式 F2。

**重合度（Overlap）：** SLIVER。置信度：Medium（在针对 SAM 的持续学习浪潮中存在特定于 SAM 的位置分析论文是合理的；但未检索到）。**R2 攻击论文：** Ramasesh arXiv:2007.07400 ("known for deep nets") + surgical fine-tuning。

**裁决（Verdict）：** **SURVIVE**，前提条件为：(a) 引用并与 Ramasesh/Davari/Lee 进行求差对比；(b) 将 Gu et al. 的 enc/dec 分支作为基线运行；(c) 核心交付成果必须是*恢复*结果（机制），而非冻结消融（S-177 单独只是一张图，成不了论文 — 将其折叠并入）。

---

## 5. 可塑性过小导致遗忘实为噪声 — S-183，C1-082（阈值伪影）

**最接近的真实论文**
- Biderman et al., *LoRA Learns Less and Forgets Less*, TMLR 2024, arXiv:2405.09673 `[V]`。在 LLM 上量化了学习与遗忘的**耦合（coupling）**：更少的可塑性 ⇒ 更少的遗忘，受秩控制；遗忘与学到的知识量挂钩。这正是 S-183 背后的确切概念引擎。
- Soutif et al., *An Empirical Analysis of Forgetting in Pre-trained Models with Incremental Low-Rank Updates*, CoLLAs / PMLR v274, 2025 `[V]`：**面向 Vision Transformer** 的 LoRA-rank vs 可塑性与遗忘。
- CoDyRA, arXiv:2412.01004 `[V]`：rank/placement vs 可塑性-稳定性权衡，同样面向视觉。
- Maier-Hein et al., *Metrics Reloaded*, Nature Methods 2024 `[M]`：分割指标中的工作点/阈值陷阱已成定论 — C1-082 的机制虽为业内熟知（存在违禁模式 F1 风险），但**尚未被应用于遗忘主张**。

**保留的确切差异。** 尚无人对目前规模可观的 SAM 持续学习文献（CA-SAM, EvoSAM, SynESAM…）进行审计，以排查**所报告的“遗忘”是否超出了（微小的 task-2 增益 × 阈值/二值化伪影 × 随机种子方差）所蕴含的噪声底线**。LLM 的耦合结论使这一点*更可能*属实，而不会降低其新颖性：它预测了小可塑性的分割微调应该表现出很小的真实遗忘 — 因此文献中发表的巨大 delta 是存疑的。

**重合度（Overlap）：** SLIVER（耦合机制在 LLM 上为 REAL；稠密/可提示模型上的缩水审计为 NONE-found）。置信度：Medium-High。**R2 攻击论文：** Biderman arXiv:2405.09673 ("we know forgetting scales with learning")。

**裁决（Verdict）：** **SURVIVE** — 且按照 C1 审计的要求，作为整个 Forget 线程的守门人**最先运行**。C1-082 是其内部的强制对照，而非独立论文。要求义务：对照 Biderman/Soutif，将其表述为*在全新体系中确认该耦合机制并用其对已发表主张进行挤水分（deflate）*，而非宣称自身发现了这一耦合。

---

## 6. 微调的校准代价（FT calibration tax） — C1-025（PEFT 保持校准），C1-031（FT 导致 IoU 头失步），C1-037（PEFT 损失鲁棒性），S-318（校准退化快于 Dice）

**最接近的真实论文**
- Yang et al., *Bayesian Low-rank Adaptation for Large Language Models* (Laplace-LoRA), ICLR 2024, arXiv:2308.13111 `[V]`：记录了 (Lo)RA 微调后的模型会变得**过度自信/校准失真（overconfident/miscalibrated）**并给出了修复方案；目前已形成完整的贝叶斯 PEFT 文献（BLoB NeurIPS 2024 `[V]`, SWAG-LoRA arXiv:2405.03425 `[V]`）— "PEFT calibration" 并非无人踏足的处女地。
- Kumar et al. arXiv:2202.10054 `[M]` + WiSE-FT arXiv:2109.01903 `[M]`：微调牺牲 OOD 鲁棒性换取 ID 增益（分类）；概念层面对应 C1-037 的论题。
- Gu et al. arXiv:2404.09957 `[V]`：PEFT 在 SAM 微调中能防止崩溃 — 属于 C1-037 方向的部分反证/重合。
- Minderer et al., *Revisiting the Calibration of Modern Neural Networks*, NeurIPS 2021, arXiv:2106.07998 `[M]`：跨模型家族的校准 vs 准确率，包括 zero-shot 模型。

**保留的确切差异。** (a) 上述所有校准结论均为**分类/LLM**；稠密预测中 full-FT vs PEFT 在匹配 mIoU 下的像素/mask 校准仍未经测量（适用 C1-032 的分歧规则：像 Dice/focal 这类稠密损失极有可能颠覆分类的结论 — 属于机制，而非简单的移植）。(b) **C1-031 是唯一真正新鲜的对象**：SAM 拥有一个*独立的置信度头*（IoU token）；尚无论文追踪微调是否会导致该头与 mask 头失步（desynchronize）。C1-026（IoU 头的 OOD 失准，在其他地方受保护）是其 zero-shot 兄弟篇。

**重合度（Overlap）：** 总体为 SLIVER；作为 "fine-tuned models are miscalibrated" 大类为 REAL。置信度：Medium-High。**R2 攻击论文：** Laplace-LoRA arXiv:2308.13111 + WiSE-FT。

**裁决（Verdict）：** **MUTATE** — 将这 4 个 ID 合并为一篇论文：*分割自适应中匹配准确率的校准+鲁棒性前沿，以 IoU 头失步（C1-031）为机制核心，并以 S-318 的 "ECE breaks before Dice" 作为排序主张*。C1-025 和 C1-037 单独存在属于 F2 移植；它们仅作为分支存在。

---

## 7. 小样本下预训练有害（Pretrain-harm small-n） — S-052（"SAM/ImageNet init < random init on tiny lesions at n=50"）

**最接近的真实论文**
- Raghu et al., *Transfusion: Understanding Transfer Learning for Medical Imaging*, NeurIPS 2019, arXiv:1902.07208 `[M]`：ImageNet 迁移在医疗任务上带来的收益出奇地小；从头训练的小模型即可匹敌。
- He et al., *Rethinking ImageNet Pre-training*, ICCV 2019, arXiv:1811.08883 `[M]`：只要训练周期充分，随机初始化在 COCO 上可匹敌预训练，**包括在检测/分割中数据量降低至 10% 的情况**。
- Zoph et al., *Rethinking Pre-training and Self-training*, NeurIPS 2020, arXiv:2006.06882 `[M]`：预训练可能会产生**实质性损害** — 但发生在强数据增强 / 大数据体系下，与 S-052 的体系*截然相反*。
- Gu et al. arXiv:2404.09957 `[V]` 及 C1-087 的孪生线程：小样本微调下的规模-数据相互作用正在被绘制。

**他们做了什么 vs. 我们主张了什么。** "Pretraining may not help medical" 已发表（Transfusion）；"pretraining can hurt" 已发表（Zoph，大数据）。S-052 的特定体系 — **在 n≈50 的微小稀疏病灶上，且特指来自 SAM/基础模型的初始化产生损害** — 尚未见发表，且标准认知预测的恰恰相反（迁移在小样本下帮助最大），这使得它成为真正的反直觉逆向赌注，而非被提前抢跑。

**确切差异 / 机制义务。** 必须交付机制，而非仅仅交付一条曲线：S-054 的物体性先验冲突（SAM 的物体 prior 与变形虫状低对比度病灶发生冲突）是求差对比的杠杆；否则审稿人会将其归入 Transfusion-redux。

**重合度（Overlap）：** SLIVER。置信度：Medium。**R2 攻击论文：** Transfusion arXiv:1902.07208 + Zoph arXiv:2006.06882。

**裁决（Verdict）：** **MUTATE**：从 "FM features hurt at small n"（拥挤的框架）转变为 "分割预训练 encoder 的物体性先验在小样本下对 stuff 类/非典型病灶构成可测量的负债" — 学习曲线交叉 + 先验消融。接受高零假设风险（它当初受保护正是因为这一点）。

---

## 8. PEFT 对比调优的全量微调诚实度 — C1-053（"LR-swept full FT matches published seg-PEFT gains"）

**最接近的真实论文**
- Gu et al. arXiv:2404.09957 `[V]`：在 18 种策略/17 个数据集上跨同等预算的统一协议；明确 "demonstrate the ineffectiveness of some methods popular in the literature"；包括 decoder-only 和原生 FT 分支。这*正是* SAM PEFT 的基线诚实度审计，已执行完毕。
- Dutt et al., *Parameter-Efficient Fine-Tuning for Medical Image Analysis: The Missed Opportunity*, MIDL 2024, arXiv:2305.08252 `[V]`：17 种 PEFT 算法，700+ 受控运行，全量 FT 基线遍历了不同数据量。
- Biderman et al. arXiv:2405.09673 `[V]`：在适当调优下，**全量 FT 在域内击败 LoRA**（LLM）— 概念层面的诚实度结论。

**保留的确切差异。** 针对调优后的基线重新运行*已发表论文的*确切主张（复现特定数值）— 但这只是 Gu et al. 的 "ineffectiveness" 发现外加一个更长的附录；审稿渠道会认为这是增量复现。

**重合度（Overlap）：** REAL。置信度：High。**R2 攻击论文：** Gu et al. arXiv:2404.09957。

**裁决（Verdict）：** 作为独立论文予以 **KILL**。诚实基线的纪律要求并入聚类 1 的存活审计中（那里的每个分支都带有经过学习率遍历的 full-FT/decoder-FT 对照）。C1-053 的保护状态转移至 C1-065。

---

## 9. PEFT 数据规模交叉点 — C1-057（"crossover at low-hundreds of images; above it full FT wins"）

**最接近的真实论文**
- Dutt et al. arXiv:2305.08252 `[V]`：**交叉曲线图已经存在** — "at 100% of downstream data full fine-tuning is optimal… as availability decreases the benefits of PEFT increase; the crossover is at 50%… LoRA overtakes the baseline as early as 80% (ViT-L)"。医学图像，ViT-B/L，多个数据集。
- Jia et al., *Visual Prompt Tuning*, ECCV 2022, arXiv:2203.12119 `[M]`：VPT vs full-FT 数据规模体系依赖性（分类）。
- Gu et al. arXiv:2404.09957 `[V]`：SAM 特定的数据体系，包括 few-shot 设置。
- Biderman et al. arXiv:2405.09673 `[V]`：LLM 的体系依赖性。

**保留的确切差异。** 仅在于“针对分割、以绝对图像数量计、按 backbone 大小细分” — 这是一个网格单元，而非一个科学问题。属于违禁模式 F2/F7（在我们各批次中收敛出现了 3 次，因为它已经融入该领域的思维定式）。

**重合度（Overlap）：** REAL。置信度：High。**R2 攻击论文：** Dutt et al. arXiv:2305.08252。

**裁决（Verdict）：** 作为论文予以 **KILL**；保留作为聚类 1 审计内报告的一条曲线。（其 Stage-2 保护状态在此依正当理由予以撤销。）

---

## 10. 增益-保留前沿 Benchmark — C1-110

**最接近的真实论文**
- WiSE-FT, CVPR 2022, arXiv:2109.01903 `[M]`：ID 增益 vs zero-shot 保留的**前沿是该论文的核心插图**（插值连续地描绘了该前沿）。
- Ilharco et al., *Editing Models with Task Arithmetic*, ICLR 2023, arXiv:2212.04089 `[M]`：权重空间编辑的目标任务 vs 对照任务权衡评估。
- Lopez-Paz & Ranzato, GEM, NeurIPS 2017, arXiv:1706.08840 `[M]`：BWT/FWT — 持续学习中十年来标准化的增益 vs 保留标量。
- CA-SAM arXiv:2511.17201 `[V]`：已经报告了 SAM 在 9 个医疗数据集上的自适应 + zero-shot 保留 — 社区无需我们的 benchmark 即可产出这些表格。

**保留的确切差异。** 一个*标准化的、专用于可提示分割的*套件（逐提示类型保留、前沿标量、模型卡）。仅属于形式化层面的新颖性；每个组件均已存在。

**重合度（Overlap）：** 组件上为 REAL。置信度：High。**R2 攻击论文：** WiSE-FT + GEM ("you renamed BWT")。

**裁决（Verdict）：** **MUTATE**：仅作为附加在聚类 1/5/6 实证论文上的**报告协议 + 排行榜**存活（C1-117 模型卡分支），并至少展示一个预注册的排名反转（依据违禁模式 F4/F6 规则）。不能作为独立的 benchmark 论文获得资助。

---

## 11. LoRA 放置位置 vs 误差类型 — A1-107（"attention-LoRA fixes boundaries; MLP-LoRA fixes regions"）

**最接近的真实论文**
- He et al., *Towards a Unified View of Parameter-Efficient Transfer Learning*, ICLR 2022, arXiv:2110.04366 `[M]`：放置位置很重要（NLP；仅限任务级指标）。
- Zhong et al., *Convolution Meets LoRA*, ICLR 2024, arXiv:2401.17868 `[V]`：针对 SAM PEFT 的放置/归纳偏置工程（LoRA 中的卷积注入局部先验）；展示了放置/架构选择会改变分割质量 — 但从未分解**每种放置位置修复了哪种误差类型**。
- CoDyRA arXiv:2412.01004 `[V]`：放置位置 × 秩 vs 学习/遗忘 — 同样处于任务级别，而非误差类型级别。
- C1-052（作为重复项被杀）和 S-144/S-91（作为绘图项被杀）是我们自己劣质的孪生设想 — 在此正确合并。

**保留的确切差异。** 映射*adapter 放置位置 → boundary-F vs interior-IoU 误差分解*尚未被检索到。它提出了一个可证伪的、具有机制意味的预测（注意力影响长程成组/边界；MLP 影响局部纹理分类），而 Conv-LoRA 的局部先验叙事与此部分*矛盾* — 这是一个诚实的确认或证伪（kill-or-confirm）设计。

**重合度（Overlap）：** 误差类型映射为 NONE found；一般的放置位置研究为 SLIVER。置信度：Medium（放置位置论文众多；可能潜藏有误差分解的论文）。**R2 攻击论文：** He et al. arXiv:2110.04366 + Conv-LoRA。

**裁决（Verdict）：** **SURVIVE**。义务：参数匹配的放置位置；预注册边界/内部误差分解；将 Conv-LoRA 作为基线和被检验的理论；明确将既定风险（效应未清晰分解）作为零假设。

---

## 12. Encoder–Decoder 契约漂移 — A1-108（接口漂移统计量），C1-067（CKA 漂移作为早期预警）

**最接近的真实论文**
- CA-SAM arXiv:2511.17201 `[V]`：构建了一个 **Alignment Layer 来对齐 SAM 中的 encoder–decoder 特征分布** — “接口契约”已不再仅仅是一个叙事构架；它已经是一个交付的方法。
- Kornblith et al., CKA, ICML 2019, arXiv:1905.00414 `[M]`；Bansal et al., *Revisiting Model Stitching*, NeurIPS 2021, arXiv:2106.07682 `[M]`：跨模块边界的表征兼容性测量已高度成熟。
- Davari et al. arXiv:2203.13381 `[M]`：CKA 风格漂移作为持续学习中的遗忘探针。
- Merchant et al., *What Happens To BERT Embeddings During Fine-tuning?*, arXiv:2004.14448 `[M]`：微调漂移剖析，NLP。

**保留的确切差异。** 现有工作测量漂移或修复接口；尚无工作在可提示模型中将漂移验证为**具备预测性的早期预警信号**（在 zero-shot/prompt-behavior 退化前的提前期 k，可操作的早停规则）。该预测性主张也是 C1-073 的模板 — C1 审计将其标记为模板回响（F7），因此整个组合中仅允许存在一篇预测性漂移论文。

**重合度（Overlap）：** SLIVER，且正在加速缩窄（CA-SAM）。置信度：Medium。**R2 攻击论文：** CA-SAM + Davari。

**裁决（Verdict）：** **MUTATE**：将 A1-108 + C1-067（+C1-073 的回归设计）合并为一篇*预测（prediction）*论文：先验选定漂移统计量，交付提前期（lead-time）和决策价值（早停 vs 基于损失）。若仅停留在 "drift exists/correlates"，则直接被拒。

---

## 13. VLM 先验对罕见/非典型病灶及否定的损害 — S-228, S-240, B1-107

**最接近的真实论文**
- Alhamoud et al., *Vision-Language Models Do Not Understand Negation* (NegBench), CVPR 2025, arXiv:2501.09425 `[V]`：18 个任务变体，79k 样本，**包括医疗领域（CONCH, BioMedCLIP）**；VLM 在否定上处于随机猜测水平；合成数据修复。
- *CXR-Align* benchmark, PhysioNet 2025 `[V]`：胸部 X 光报告对齐中的否定处理 — "no pneumothorax" 简直就是该领域的标准范例。
- NAST, arXiv:2602.12498 `[V]`：针对**医疗 VLM 否定**的逐层微调 — 修复文献已经开启。
- Yuksekgonul et al., 词袋模型/NegCLIP, ICLR 2023, arXiv:2210.01936 `[M]`。
- Udandarao et al., *No "Zero-Shot" Without Exponential Data*, NeurIPS 2024, arXiv:2404.04125 `[M]`：zero-shot 性能取决于预训练**概念频率（concept frequency）** — 即 "text prior fails on rare/atypical" 引擎（C1-002 在我们自己的审计中已因此被杀）。
- Li et al., POPE, EMNLP 2023, arXiv:2305.10355 `[M]`；Rohrbach et al., CHAIR, EMNLP 2018, arXiv:1809.02156 `[M]`：由**共现先验**驱动的对象幻觉，通过基于共现的负采样进行测量 — B1-107 在 VQA/captioning 上的论题。

**确切差异。**
- S-240（否定破坏了 VLM 驱动的分割）：识别/检索/对齐版本已全面发表，包括医疗。剩余的细微切口 — 否定下的像素级指代表达分割 — 只是一个评估切片，成不了论文。**KILL**（若需要，作为评估切片并入 S-228 的后续工作中）。
- S-228（文本先验抑制了非典型表现）：频率→zero-shot 已发表（Udandarao）；但在*因果消融文本先验的前提下，非典型表现上的稠密召回损害*（在按频率分层的表现上，纯视觉 vs VLM 提示分割）尚未发表。**MUTATE** 转向该因果、受控频率的设计；必须引用 NegBench-med/CXR-Align/Udandarao。高临床价值使其保持存活。
- B1-107（将目标 inpaint 擦除，VLM 分割器依然触发 — 幽灵 mask）：POPE/CHAIR 确立了文本输出的共现幻觉；**未发现稠密预测的反事实 inpainting 审计**。混淆项（inpainting 痕迹）真实存在且已被我们自己的 AB 评审员标记；要求设置痕迹对照（将现有对象重新 inpaint 作为假手术 sham surgery）。**SURVIVE**。

**重合度（Overlap）：** 否定和频率为 REAL，稠密反事实为 SLIVER。置信度：对 kills 项为 High，对 B1-107 的存活为 Medium（稠密幻觉 benchmark 涌现迅速）。**R2 攻击论文：** NegBench；Udandarao；POPE。

---

## 14. VFM 初始化下主动学习/半监督已死 — B1-011（DINOv2 下熵 AL ≈ random），B1-025（VFM 初始化下 ST ≈ Mean Teacher）

**最接近的真实论文**
- Gupte et al., *Revisiting Active Learning in the Era of Vision Foundation Models*, TMLR 2024, arXiv:2401.14555 `[V]`：**在 DINOv2/OpenCLIP 下**系统性重构 AL 评估，推翻了低预算经验法则（冷启动选择、不确定性 vs 典型性），提出了修正策略。B1-011 的问题已被提出并被解答（分类）。
- Mittal et al., *Realistic Evaluation of Deep Active Learning for Image Classification and Semantic Segmentation*, IJCV 2025 `[V]`：**包含分割**；展示了随机(+SSL)击败 AL 的体系并绘制了 AL 何时奏效 — 稠密预测版本的审计已然存在。
- Yang et al., *UniMatch V2*, TPAMI 2025, arXiv:2410.10777 `[V]`：**基于 DINOv2** 重建半监督分割；头条结论："a simple update on the encoder brings more improvement than careful method designs" 以及 "labeled-only DINOv2-S beats semi-supervised ResNet-101" — 即 VFM 初始化压缩了 B1-025 想要测试的方法设计 delta。SemiVL (ECCV 2024) `[V via citation]` 涵盖了 VLM 引导的变体。
- 冷启动：*Foundation Model Makes Clustering a Better Initialization for Cold-Start AL*, arXiv:2402.02561 `[V]`。

**保留的确切差异。** B1-025 字面上的测试对（纯 ST vs Mean Teacher，冻结 VFM，差距 <0.5）是 UniMatch V2 已发表的重测中两行的消融；B1-011 分割专用的 AL 循环是 Mittal et al. 网格中的一个单元格。这两个差异都无法跨越“IJCV/TPAMI 作者是否会认为这是新闻？”的门槛（违禁模式 F1）。

**重合度（Overlap）：** REAL。置信度：High。**R2 攻击论文：** UniMatch V2 arXiv:2410.10777；Gupte et al. arXiv:2401.14555。

**裁决（Verdict）：** 两者均 **KILL**。将标注效率的精力重定向至 B1-028（域外无标注污染）和 B1-001 式预算单位问题，上述论文均未触及这些方面。

---

## 15. 在算力匹配下 Copy-paste ≥ Diffusion 合成 — B1-051

**最接近的真实论文**
- Ghiasi et al., *Simple Copy-Paste is a Strong Data Augmentation Method for Instance Segmentation*, CVPR 2021, arXiv:2012.07177 `[M]`：copy-paste 是极强的基线。
- Zhao et al., *X-Paste*, ICML 2023, arXiv:2212.03863 `[V]`：StableDiffusion 生成 + CLIP 过滤的实例在 LVIS 上**击败了纯 Copy-Paste**（整体 +1.2 box/mask AP，在罕见类上提升更多）— 正面对手，声称相反方向的结论。
- He et al., *Is Synthetic Data from Generative Models Ready for Image Recognition?*, ICLR 2023, arXiv:2210.07574 `[M]`。

**保留的确切差异。** X-Paste 的对比**并非算力匹配（not compute-matched）**：扩散生成、CLIP 过滤以及 mask 后处理的 GPU-hours 均被排除在核算之外。尚未有人在实例分割中发表过包含生成过程在内的诚实等 GPU-hours 前沿。B1-051 拥有一个具名的对手，且其头条数据可以被反转 — 确切符合评审标准所奖励的“若我们正确，谁被证明是错的”的形态。

**重合度（Overlap）：** SLIVER。置信度：Medium-High（在合成数据扩展文献中可能存在算力核算论文；但未检索到）。**R2 攻击论文：** X-Paste arXiv:2212.03863（审稿人会引用其增益；应对手段即为算力账本）。

**裁决（Verdict）：** **SURVIVE**。义务：将生成+过滤算力计入合成组；规模匹配的真实数据组（Ghiasi）作为第三种条件；报告扩散模型胜出的交叉规模（诚实可能的结果）。

---

## 16. 直方图匹配解释了 UDA — B1-061（"style matching recovers ≥60% of self-training UDA gain"）

**最接近的真实论文**
- Yang & Soatto, *FDA: Fourier Domain Adaptation for Semantic Segmentation*, CVPR 2020, arXiv:2004.05498 `[V]`：一种**免训练的低频幅度置换**在 GTA→Cityscapes 上实现了当时的 SOTA UDA — "cheap spectral/style alignment captures most of the gap" 这一结论已有六年历史；现在已作为默认数据增强与 HistogramMatching 一同集成在 Albumentations 中。
- Hoyer et al., DAFormer, CVPR 2022, arXiv:2111.14887 `[M]`：带有消融的现代自训练 pipeline；因果分解的目标。
- Feather-light FDA for MRI, arXiv:2208.00474 `[V]`：廉价风格迁移已足够这一观点在医学领域得到复现。

**保留的确切差异。** B1-061 是*针对 2024 年代 pipeline 的归因审计*（DAFormer/MIC 类增益中有多少比例来自于风格？），而非一种方法。但 FDA 已经让“廉价风格 ≈ UDA 的大部分”成为社区先验，且 B1-069（全因子可加性，在别处保留）更尖锐地测试了相同的分解。

**重合度（Overlap）：** 精神实质上为 REAL；对现代 pipeline 归因而言为 SLIVER。置信度：High。**R2 攻击论文：** FDA arXiv:2004.05498。

**裁决（Verdict）：** **MUTATE**：并入 B1-069 的 ±style × ±self-training 析因设计。作为独立主张，它会被视为附带百分比数字的 FDA 重复版。

---

## 17. FSS Support 方差 / 背景作弊 — B1-074（support choice > method choice），B1-079（背景相似度捷径）

**最接近的真实论文**
- Tang et al., *Overcoming Support Dilution for Robust Few-shot Semantic Segmentation*, arXiv:2501.13529 `[V]`：记录了 support 图像**贡献差异巨大**（shot 数量增加可能带来损害；按贡献排序剪枝可修复该问题）— 基于 B1-074 的现象构建的方法，但缺乏审计视角。
- *A Novel Benchmark for Few-Shot Semantic Segmentation in the Era of Foundation Models*, arXiv:2401.11311 `[V]`：用现代 VFM 重新 benchmark FSS；基础特征基线重排了该领域 — 方法方差已知在缩小。
- Lang et al., *Learning What Not to Segment* (BAM), CVPR 2022, arXiv:2203.07615 `[V]`：**基类偏置（base-class bias）** — FSS 模型系统性地在已见类别区域触发；经典已发表的 FSS 捷径结论。
- Few-shot 分类中的 episode 方差（置信区间文献，如 Dhillon et al. ICLR 2020 `[M]`）。

**确切差异。**
- B1-074：*方差分解*（support 抽取方差 vs 方法方差，相同 episode，已发布 checkpoint）尚未见发表；2501.13529 优化了选择，但从未报告足以质疑 FSS 排行榜的方差分解。SLIVER → **MUTATE**：作为纯评估 ANOVA 运行（对照 C1-038 的 clicks×checkpoints 设计），引用 2501.13529 作为支持证据，2401.11311 作为 checkpoint 池。
- B1-079：BAM 展示了*类别先验*捷径；B1-079 指控存在正交的 **episode 构建捷径**（support/query 背景相似度）。未检索到背景置换审计。**SURVIVE**，义务：控制合成伪影（使用同背景合成图作为假手术置换），并明确与 BAM 的偏置进行求差对比。

**重合度（Overlap）：** 两者均为 SLIVER。置信度：Medium。**R2 攻击论文：** 2501.13529 (B1-074); BAM (B1-079)。

---

## 18. CLIP 稠密线性重对齐 — B1-097（"linear map from ~100 labels recovers ≥70% of dense-CLIP gap"）

**最接近的真实论文**
- Zhou et al., MaskCLIP(+), ECCV 2022, arXiv:2112.01071 `[M]`：注意力手术暴露出稠密 CLIP 特征；奠基性的修复。
- Wang et al., SCLIP, arXiv:2312.01597 `[V]`：**免训练**注意力校正，平均 zero-shot mIoU 从 14.1 提升至 38.2。
- Wysoczańska et al., CLIP-DINOiser, ECCV 2024, arXiv:2312.12359 `[V]`：**两个轻量卷积层，零标注**，从 CLIP 自身学习，在 COCO/Context/Cityscapes/ADE 上达到 SOTA — 在成本和监督轴上均严格超越（strictly dominates）"线性头 + 100 标签"。
- 外加 GEM, NACLIP, ClearCLIP, ProxyCLIP（免训练家族，2023-24）`[M]`；以及监督对齐方向的 LSeg arXiv:2201.03546 `[M]` 和 PACL arXiv:2212.04994 `[M]`。

**他们做了什么 vs. 我们主张了什么。** 实际问题（"低成本重对齐 CLIP 稠密特征"）已被反复解决，包括使用比 B1-097 所提*更少*的监督。残余的科学主张（"失准可以通过线性方式纠正"）已被免训练家族部分解答：其中很大一部分属于**注意力池化伪影（attention-pooling artifact）**，甚至不是特征空间的线性偏移。

**重合度（Overlap）：** REAL。置信度：High。**R2 攻击论文：** CLIP-DINOiser arXiv:2312.12359 + SCLIP。

**裁决（Verdict）：** **KILL**。可挽救的残留内容 → B1-098（注意力手术*无法*修复的部分：手术后残差的误差分类），其不在此攻击集中，应吸收 B1-097 的 Protect 名额。

---

## 跨聚类致 Stage-3 导师备忘

1. **2024–26 年的 SAM-continual 浪潮（Gu 2404.09957, CA-SAM 2511.17201, EvoSAM 2503.06236）直接落在了我们最密集的线索上。** 聚类 1, 8, 9, 10 中凡是写着“无人测量过 SAM 的自适应 vs 保留”的内容，字面上均已不再成立。存活的切入点是*行为层面/按提示类型细分*以及*对审计者进行审计（audit-the-auditors）*的角度（聚类 3, 4, 5）。
2. **本集合建议合并出的论文**（遵循 ≥30% 建设性配额）：
   - P1 = C1-065 测试套件 + S-176 矩阵 + 随机 LoRA/VeRA 对照 + LR-sweep 对照（聚类 1+2+3+8+9）。
   - P2 = 作为 P1 守门人的 S-183 噪声底线审计（聚类 5）。
   - P3 = C1-031 IoU 头失步 + 校准/鲁棒性前沿（聚类 6），通过 C1-110 的面板进行报告（聚类 10）。
   - P4 = A1-107 放置位置→误差类型（聚类 11）— 建设性/机制名额。
   - P5 = B1-107 稠密反事实幻觉 + S-228 按频率分层的先验损害（聚类 13）。
   - P6 = B1-051 算力诚实的合成数据审计（聚类 15）。
   - P7 = B1-079 背景置换审计（聚类 17）。
3. **请求修正 Protect 名单：** 撤销 C1-053, C1-057 的 Protect（因撞车被合理杀死）；转移至 C1-065 和 C1-031。S-148 的 Protect 作废（VeRA）；其预算归入 A1-107。
4. **未经核实的记忆引文**在全文中均标注为 `[M]`；在其中任何聚类进入论文草稿之前，请重新核验 `[M]` 的 arXiv ID。上述引文绝无虚构；`[M]` 标注项皆为按标题+会议引用的经典论文。
