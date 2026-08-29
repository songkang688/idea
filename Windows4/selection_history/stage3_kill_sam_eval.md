# Stage 3 — 前序工作狙杀（Prior-Work Assassination）：SAM / 评估聚类（200→50 第 1 轮）

日期：2026-08-28。角色：**前序工作狙杀者（Prior-Work Assassin）**。默认假设：每个设想均已被发表。
认识状态（Epistemic status）：基于 2026-08-28 通过 arXiv/网络检索找到的真实、核实论文的**文献判断（LITERATURE JUDGMENT）**。
遵循的规则：绝无虚构引文；下文每个 arXiv ID 均在此轮中完成检索与阅读（摘要 + 相关章节）；若未找到前序工作，则明确标记为 **NOT FOUND** 而非生搬硬凑。

输入：`stage2_top200.md`、`literature_anchors.md`、Stage-1 设想文本（S/A1/C1 文件）。

记分板：在被攻击的 15 个聚类线索中，**9 个 KILL / 3 个 MUTATE / 3 个 SURVIVE**。

同时杀死多个聚类的两条横切事实（cross-cutting facts）：

- **莫斯科团队已经建立了“真实提示（realistic prompt）”评估体系。** 面向点击的 RClicks (NeurIPS 2024) 与面向边界框的 BREPS (arXiv:2601.15123, 2026) 共同涵盖了：大规模真实用户提示收集、提示分布模型、边缘化提示指标（prompt-marginalized metrics）、对提示的鲁棒性排名，以及最坏情况真实提示搜索 — 横跨自然与医学数据集。任何以“在真实 / 分布式 / 微扰提示下评估可提示模型”为核心载荷的 Windows4 设想，如今都属于重复实现。
- **SAM 论文自身预先排除了 multimask 的“新发现”。** Kirillov et al. 明确指出这三个输出被设计为整体 / 部分 / 子部分（whole / part / subpart）嵌套粒度，采用最小损失（min-loss）训练，并发表了 oracle 对比 argmax 的差距分析。

---

## 聚类 1 — 预言机提示协议（Oracle-prompt protocol） (S-003, A1-118, C1-115)

被攻击的主张：源自 GT 的提示夸大了 SAM 的主张（S-003：GT-box 评估暗中等同于检测器 benchmark）；报告在真实提示分布上的边缘化提示 IoU（A1-118）；保持排名的免预言机自动提示评估协议（C1-115）。

**最接近的前序工作**
- *RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation.* Antonov, Moskalenko, Shepelev, Krapukhin, Soshin, Konushin, Shakhuro. NeurIPS 2024 Datasets & Benchmarks. arXiv:2410.11722. https://arxiv.org/abs/2410.11722
- *BREPS: Bounding-Box Robustness Evaluation of Promptable Segmentation.* Moskalenko, Kuznetsov, Dudko, Iasakova, Boldyrev, Shepelev, Spiridonov, Kuznetsov, Shakhuro. 2026. arXiv:2601.15123. https://arxiv.org/abs/2601.15123
- *Segment anything model for medical image analysis: an experimental study.* Mazurowski et al. Medical Image Analysis 2023. https://doi.org/10.1016/j.media.2023.102918
- *Benchmarking Human and Automated Prompting in the Segment Anything Model.* 2024. arXiv:2410.22048. https://arxiv.org/abs/2410.22048
- *AoP-SAM: Automation of Prompts for Efficient Segmentation.* AAAI 2025. arXiv:2505.11980. https://arxiv.org/abs/2505.11980

**他们实际做了什么。** RClicks 收集了 47.5 万次真实点击，拟合了“可点击性（clickability）”分布模型，并将交互式方法重新 benchmark 为*真实点击上的期望值*，展示了基线模拟器高估了 5–29% 的性能且改变了方法的鲁棒性排名 — 这正是已发表的边缘化提示 IoU。BREPS 完成了边界框版本：对真实边界框的受控用户研究（桌面 vs 移动端）、边界框放置上的 IoU 热力图、用于寻找最坏情况真实边界框的自然度约束白盒搜索，以及一个 15 模型 × 10 数据集的 benchmark，发现相对于紧边界框协议存在 ~30% 的 IoU 下降；其明确指出 "tight bbox + small jitter" 协议高估了部署质量。Mazurowski et al. 在医学图像中形式化了 SAM 的 "oracle performance"，并证明提示模拟主导了结果。arXiv:2410.22048 对比了人类与六种自动提示策略（23.4 万套提示集），并量化了自动 vs 人类的差距。AoP-SAM 构建了自动提示生成及评估协议（greedy-IoU 匹配）。

**保留的确切差异。** S-003 的特定构想（将 GT 框替换为实际的弱检测器如 YOLO，并展示 Dice 崩塌超过了 encoder 大小的效应）是 BREPS/RoBox-SAM 退化曲线的一张插图级推论。A1-118 逐字逐句就是 RClicks/BREPS。C1-115 开放的细微切口：*自动提示*（显著性/检测器）评估是否在零预言机成本下*保持模型排名* — 自动提示方法存在，但针对该协议自身的秩相关审计不存在。

**剩余新颖性：** NONE (S-003, A1-118); SLIVER (C1-115 保持排名的审计)。
**新颖性置信度：** 5。
**Reviewer #2 可能引文：** RClicks (arXiv:2410.11722) 与 BREPS (arXiv:2601.15123)。
**裁决：** **KILL**。（若要挽救任何内容，将 C1-115 的秩相关问题并入现有 benchmark 的附录中，而非单独成文。）

---

## 聚类 2 — 紧框图像消融 / SAM 作为框插值器 (S-014, S-604)

被攻击的主张：在紧 GT 边界框下，SAM 的 decoder 几乎不查阅图像证据 — 在框内消融/打乱图像内容几乎不会改变 Dice；SAM 从而只是一个从框到 mask 的形状插值器。

**最接近的前序工作**
- *Stable Segment Anything Model.* Fan, Tao, Ke, Ye, Zhang, Wan, Wang, Tai, Tang. 2023. arXiv:2311.15776. https://arxiv.org/abs/2311.15776
- *BREPS* (同上), arXiv:2601.15123 — 框放置上的逐像素 IoU 热力图；1 像素的框偏移会导致 IoU 急剧改变。
- *Enhancing MedSAM with a Lightweight Box Predictor.* 2026. arXiv:2606.04705 — 记录了经过框微调的 MedSAM decoder "learned to expect" 边界框几何结构，且预测的框对不规则病灶施加了刚性矩形约束。
- *Robust Box Prompt based SAM (RoBox-SAM).* Huang et al. MICCAI MLMI 2024. arXiv:2407.21284 — 低质量框下的注意力漂移分析。

**他们实际做了什么。** Stable-SAM 是 "the first comprehensive analysis of SAM's segmentation stability across prompt qualities"，并将机制定位在不良提示下 *mask decoder 注意力集中在哪些图像特征上* — 即 decoder 对图像 vs 提示的依赖性已被从提示端进行过研究。BREPS 展示了输出是框坐标的陡峭函数。MedSAM 框预测器论文记录了框微调模型中的框状 mask 伪影和几何先验依赖性。在这些工作中，尚无人对*图像证据本身*进行干预。

**保留的确切差异。** 直接的因果干预尚未运行：冻结提示（紧 GT 框），销毁框内的图像证据（零化/均值图像嵌入、按 S-604 进行 patch 打乱、匹配噪声的内部），并将 Dice 作为框紧密度和对象对比度的函数与字面意义上的矩形填充零假设进行测量。所有已发表的工作都是在图像固定的情况下微扰提示；该实验是在提示固定的情况下微扰图像。这是一项不同的实验，也是一个不同的主张。

**剩余新颖性：** REAL（狭窄但真实的因果空白）。
**新颖性置信度：** 4。
**Reviewer #2 可能引文：** Stable-SAM (arXiv:2311.15776) — "decoder feature-activation under prompts already analyzed"；BREPS 的敏感性分析。
**裁决：** **SURVIVE**。
**杀手级实验（Killer experiment）：** 500 个 COCO + 500 个医学（低对比度）实例，紧 GT 框，四种内部条件 {intact 完整, patch-shuffled 打乱 (S-604), embedding-zeroed 嵌入归零 (S-014), luminance-matched noise 亮度匹配噪声} × 边界框填充 padding {0, 4, 8, 16 px}；报告 Dice 对比 box-fill 矩形填充零假设以及对比对象对比度的关系。预注册淘汰条件：若在所有情况下完整 vs 消融的 Dice 差距 > 15 个点，则 SAM 具备“视觉能力”，插值器主张在一周内被淘汰 — 仅当低对比度体系表现出插值器行为时，无论如何都要发表经过零假设校准的敏感性曲线。

---

## 聚类 3 — 嵌套尺度的 Multimask，而非语义 (S-018, C1-061, A1-003)

被攻击的主张：SAM 的 3 个 mask 编码的是嵌套尺度而非不同的语义对象（S-018）；微调会导致 multimask 多样性崩塌，即“歧义性遗忘（ambiguity forgetting）”（C1-061）；mask 多样性与纹理熵呈负相关（A1-003）。

**最接近的前序工作**
- *Segment Anything.* Kirillov et al. ICCV 2023. arXiv:2304.02643. https://arxiv.org/abs/2304.02643
- *Semantic-SAM: Segment and Recognize Anything at Any Granularity.* Li et al. 2023. arXiv:2307.04767. https://arxiv.org/abs/2307.04767
- *GraCo: Granularity-Controllable Interactive Segmentation.* Zhao et al. CVPR 2024 (Highlight). arXiv:2405.00587. https://arxiv.org/abs/2405.00587
- *How to build the best medical image segmentation algorithm using foundation models.* 2024. arXiv:2404.09957 — 记录了 SAM 微调方案导致的 zero-shot 遗忘（~35% 的下降）。
- *MedSAM / Segment Anything in Medical Images.* Ma et al. Nature Communications 2024. arXiv:2304.12306 — 结构设计上直接微调为单 mask 目标。

**他们实际做了什么。** SAM 论文*阐明了设计意图*："3 mask outputs is enough for most common cases (nested masks are often at most three deep: whole, part, and subpart)"，在三个头上采用最小损失训练，并分析了 oracle 选择差距。S-018 的“发现”就是文档中记录的设计意图。Semantic-SAM 和 GraCo 更进一步，将粒度变成了明确的可控轴。关于 C1-061：MedSAM 式的微调在构建上就丢弃了 multimask 头，且 arXiv:2404.09957 量化了微调后的能力遗忘 — 但尚无论文将*候选多样性崩塌（proposal-diversity collapse）*作为连续的遗忘指标进行测量。A1-003 的纹理熵负相关：作为已发表的测量处于 **NOT FOUND** 状态。

**保留的确切差异。** S-018：无 — 测量嵌套频率只是证实了训练目标。C1-061：多样性崩塌*曲线*（微调前/后成对 mask IoU / 粒度分布扩散，对比微调深度和数据规模）仍未经测量。A1-003 是一项协变量分析，成不了一篇论文。

**剩余新颖性：** NONE (S-018), SLIVER→REAL (C1-061), SLIVER (A1-003)。
**新颖性置信度：** 5 (S-018), 3 (C1-061)。
**Reviewer #2 可能引文：** SAM 论文 §Resolving Ambiguity；GraCo。
**裁决：** **MUTATE** — 直接杀死 S-018；将该聚类重塑为 C1-061 “歧义性遗忘”：针对微调后可提示 decoder 的多样性保留指标，以 A1-003 的纹理熵作为一个分析协变量，以 GraCo（其*增加*了粒度控制）作为建设性对比基准。

---

## 聚类 4 — 负点击悖论 / 不对称性 (S-005, A1-007)

被攻击的主张：负点击相对于正点击在价值上具有不对称性（S-005）；负点击可能非单调地扩大 mask / 恶化 IoU（A1-007）。

**最接近的前序工作**
- *Reviving Iterative Training with Mask Guidance for Interactive Segmentation (RITM).* Sofiiuk, Petrov, Konushin. 2021 (ICIP 2022). arXiv:2102.06583. https://arxiv.org/abs/2102.06583
- *FocSAM: Delving Deeply into Focused Objects in Segmenting Anything.* CVPR 2024. arXiv:2405.18706. https://arxiv.org/abs/2405.18706
- *DiffClick: Click-Differentiated Enhancement Network for Interactive Segmentation.* 2025 journal preprint (Univ. Leicester repository). https://figshare.le.ac.uk/articles/journal_contribution/DiffClick_Click-Differentiated_Enhancement_Network_for_Interactive_Segmentation/29650265
- *ClickAttention: Click Region Similarity Guided Interactive Segmentation.* 2024. arXiv:2408.06021. https://arxiv.org/abs/2408.06021
- *RClicks* (同上) — 方法相对于点击模式的鲁棒性，包括后续的纠正性点击。

**他们实际做了什么。** RITM 记录了 "adding a new click can even make the mask worse, contradicting user expectations"，并用 mask 状态条件化进行了修复。FocSAM 展示了 SAM 尤其会遭受灾难性的单点击崩塌（在后续点击中 IoU 从 88.6 骤降至 12.8），并发表了逐点击的 ΔIoU 分布 — 该“悖论”已被测量、绘制并得到缓解。DiffClick 量化了正负不平衡（没有负点击时失效率上升 ~20%），并构建了非对称处理两类点击的模块；ClickAttention 在架构上将它们解耦。现象与非对称处理均已存在。

**保留的确切差异。** 在*匹配预算下逐点击类型的干净边际价值规律*（S-005 的精确构想，逐点击的 FP 减少 vs TP 增益）并未以此形式发表 — 但这只是现有评估框架内的一个表格，且 DiffClick 的不平衡数据已经暗示了其方向。

**剩余新颖性：** SLIVER。
**新颖性置信度：** 4。
**Reviewer #2 可能引文：** RITM Fig. 4 与 FocSAM Fig. 1/4 ("already documented, already mitigated")。
**裁决：** **KILL**。（该悖论已被前序工作涵盖两次；残留的“非对称规律”表格自身构不成一篇论文。）

---

## 聚类 5 — 提示演化评分器失效 vs SAMPOT (S-007, S-347)

被攻击的主张：由无监督评分器引导的测试期提示演化是在追逐高对比度斑块，而非临床目标；提示演化会降低临床 Dice（受保护的反 SAMPOT 负结果）。

**最接近的前序工作**
- *Task-driven Prompt Evolution for Foundation Models (SAMPOT).* Sathish, Venkataramani, Shriram, Sudhakar. 2023. arXiv:2310.17128. https://arxiv.org/abs/2310.17128

**他们实际做了什么。** SAMPOT 通过在无监督分割质量回归器上进行梯度上升来演化提示位置（肺部 X 光），并在 ~75% 的病例中获得改善。至关重要的是，*SAMPOT 自己的论文就报告了 S-007 所预测的确切失效模式*：在其失效分析中，优化后的提示漂移出了肺野，因为评分器更偏好错误的但得分高的 mask，作者呼吁引入安全保护逻辑。针对提示演化中无监督评分器的系统性专题负面研究：**NOT FOUND**。

**保留的确切差异。** 规模与系统性：SAMPOT 在单一任务上使用单一学习评分器以个案轶事的形式记录了该失效；尚无人发表过跨评分器家族（CRF 能量、NCut、predicted-IoU 头、学习回归器）× 数据集的系统性审计，测量代理目标在*何时*会与临床 Dice 产生反向相关。纯粹的“SAMPOT 失败”复现（S-347）只是 workshop 简报，而非论文。

**剩余新颖性：** SLIVER。
**新颖性置信度：** 3。
**Reviewer #2 可能引文：** SAMPOT §failure analysis ("the authors already told you this")。
**裁决：** **MUTATE** — 放弃纯反 SAMPOT 构架；能够存活的形式是评分器有效性研究："which unsupervised segmentation-quality proxies are safe optimization targets at test time, and in which contrast regimes do they invert" — 将 SAMPOT 作为设计空间中的一个点，并融入 predicted-IoU 校准失真（Windows4 聚类 26/S-361 谱系）。

---

## 聚类 6 — 人类 vs 模拟点击 (A1-105, C1-003)

被攻击的主张：真实人类点击与源自 GT 的模拟点击存在差异；模拟点击评估过于乐观并重排了方法；模拟点击泄漏了 GT 边界信息。

**最接近的前序工作**
- *RClicks.* Antonov et al. NeurIPS 2024 D&B. arXiv:2410.11722. https://arxiv.org/abs/2410.11722
- *Benchmarking Human and Automated Prompting in the Segment Anything Model (PointPrompt).* 2024. arXiv:2410.22048. https://arxiv.org/abs/2410.22048
- *BREPS* (针对框而非点击). arXiv:2601.15123.
- 背景：*Large-scale interactive object segmentation with human annotators.* Benenson, Popov, Ferrari. CVPR 2019 — OpenImages 规模下真实标注者的点击行为。

**他们实际做了什么。** RClicks 就是该设想以 Windows4 无法匹敌的规模执行的成果：47.5 万次众包真实点击、生成式可点击性模型、首轮真实点击评估、跨用户群体的鲁棒性指标（跨点击风格标注时间存在 3–79% 的差异），并证明基于误差区域中心的基线模拟高估了 5–29% 的真实世界性能且动摇了排名。PointPrompt 在 16 个数据集上补充了约 20 万套人类提示集，并量化了人类 vs 自动的差距。C1-003 的 "human NoC systematically worse than simulated NoC" 即为 RClicks Table 4。A1-105 的“收集 1k 次点击用户研究”被严格碾压（475倍）。

**保留的确切差异。** 医学专家的点击（放射科医生 vs 众包工人）未包含在 RClicks 中 — 但这残留的部分属于数据收集工作，而非科学假设。

**剩余新颖性：** NONE。
**新颖性置信度：** 5。
**Reviewer #2 可能引文：** RClicks。
**裁决：** **KILL**。

---

## 聚类 7 — Patch 网格混叠（Patch-grid aliasing） (A1-002)

被攻击的主张：SAM 边界 F 值（boundary-F）随子 patch（16 px）图像平移而振荡；此前无人测量过可提示分割中的 patch 网格混叠。

**最接近的前序工作**
- *Phase Marginalization for Patch-Grid Instability in Vision Transformers.* 2026. arXiv:2606.08132. https://arxiv.org/abs/2606.08132
- *Alias-Free ViT: Fractional Shift Invariance via Linear Attention.* NeurIPS 2025. arXiv:2510.22673. https://arxiv.org/abs/2510.22673
- *Sub-token ViT Embedding via Stochastic Resonance Transformers.* 2023. arXiv:2310.03967. https://arxiv.org/abs/2310.03967
- 先驱工作：Zhang, *Making Convolutional Networks Shift-Invariant Again*, ICML 2019。

**他们实际做了什么。** arXiv:2606.08132 将 patch 网格*相位（phase）*定义为稠密 ViT 预测的显式干扰变量，测量了语义边界附近（分割与深度）的子 patch 相位不稳定性，并给出了具备成本-精度可扩展性的免训练相位边缘化修复方案。Alias-Free ViT 形式化并修复了 ViT 中的分数平移混叠。SRT 利用子 token 平移从冻结的 ViT 中恢复超越奈奎斯特极限的细节。现象、测量方法学以及两种补救方案均已发表。

**保留的确切差异。** 专门在 SAM 上运行相同的测量（提示协同平移），并展示 boundary-F 中 16 px 的 FFT 周期性。这只是将 arXiv:2606.08132 的协议应用到又一个模型上。

**剩余新颖性：** NONE-to-SLIVER。
**新颖性置信度：** 4。
**Reviewer #2 可能引文：** arXiv:2606.08132。
**裁决：** **KILL**。

---

## 聚类 8 — 拓扑 / 孔洞先验（Topology / holes prior） (A1-004)

被攻击的主张：SAM 的 decoder 存在针对 genus>0 mask 的先验（甜甜圈空洞被填平）；SAM 文献中缺乏拓扑层面的失效表征。

**最接近的前序工作**
- 感知拓扑的分割是一个成熟的子领域：Hu et al., *Topology-Preserving Deep Image Segmentation*, NeurIPS 2019; Shit et al., *clDice*, CVPR 2021; *Topology Optimization in Medical Image Segmentation with Fast Euler Characteristic*, arXiv:2507.23763; *Topology-Guaranteed Image Segmentation (connectivity, genus, width)*, arXiv:2601.11409。
- *COCO-ReM / Benchmarking Object Detectors with COCO: A New Path Forward.* Singh et al. ECCV 2024. arXiv:2403.18819 — 增加了约 2,000 个带有**真实孔洞**的验证集 mask，而 COCO-2017 中孔洞为**零**，即“无孔洞”行为很大程度上是一种标注格式惯例。
- SAM 工程实现：发布的自动 mask 生成器通过**填充孔洞**（低于面积阈值）来对 mask 进行后处理（facebookresearch/segment-anything, `min_mask_region_area`）。

**他们实际做了什么。** 拓扑社区拥有现成的指标（Betti 误差、Euler 示性数图、clDice）和训练修复方案；亏格（genus）约束是一个明确且已发表的维度。COCO-ReM 表明 benchmark 自身的 GT 缺乏孔洞，因此在 COCO 风格 mask 上训练/评估的*任何*模型都不会因为 genus>0 输出而获得奖励。SAM 自身的 pipeline 主动删除了小孔洞。SAM 特异性的亏格审计（“在环/杯状物体上的孔洞恢复率 vs U-Net”）：**NOT FOUND** — 但其两个可能的原因（标注惯例、后处理）已被记录，这使得朴素的审计在起点上就受到混淆。

**保留的确切差异。** 解耦 *decoder 先验* vs *标签惯例* vs *后处理*：原始 SAM（无孔洞填充，检查 logits）到底能否表示 genus>0？

**剩余新颖性：** SLIVER。
**新颖性置信度：** 3。
**Reviewer #2 可能引文：** clDice / Hu et al. ("topology metrics exist") + COCO-ReM ("your GT had no holes")。
**裁决：** **MUTATE** — 仅作为三方因果分解（先验 vs 惯例 vs 后处理）且基于 COCO-ReM 的真实带孔 mask 和原始 logits 进行评估时可行；作为“SAM 在甜甜圈上失效”的审计则直接死亡。

---

## 聚类 9 — 提示分布偏移（Prompt-distribution shift） (A1-091, A1-118)

被攻击的主张：点击惯例在不同数据集间存在差异；在另一数据集的提示分布下评估会引起与图像域偏移相当的 IoU 偏移 — “提示分布偏移”作为一个新的可测量维度。

**最接近的前序工作**
- *RClicks* (arXiv:2410.11722) — 可点击性分布、用户群分层、鲁棒性指标 ΔGR（跨点击风格有 3–79% 的差异）。
- *BREPS* (arXiv:2601.15123) — 边界框风格分布因平台而异（桌面 vs 移动端），模型在其下的排名会发生变动。
- *PointPrompt* (arXiv:2410.22048) — 跨 16 个数据集的人类提示分布，可预测性能的特征。

**他们实际做了什么。** RClicks/BREPS 确立了提示分布 (a) 因人群和平台而异，(b) 实质性影响指标，以及 (c) 会改变方法排名 — 这*正是*“提示分布偏移真实且可测量”的论题，且带有数据支撑。A1-118（边缘化 IoU）就是其核心头条指标。字面上的跨数据集分布置换矩阵（在数据集 A 上训练可点击性模型，在 B 上评估）只是对其发布数据的二次分析。

**保留的确切差异。** 命名了该维度并提出了置换矩阵实验；没有带来新数据或新能力。

**剩余新颖性：** NONE-to-SLIVER。
**新颖性置信度：** 4。
**Reviewer #2 可能引文：** RClicks + BREPS。
**裁决：** **KILL**。

---

## 聚类 10 — SA-1B 泄漏（SA-1B leakage） (C1-001)

被攻击的主张：SA-1B 与 zero-shot 评估 benchmark 之间的近似重复重合夸大了 SAM 的 zero-shot 数据；该重合此前从未被审计。

**最接近的前序工作**
- 针对 SA-23 / COCO / LVIS / DAVIS 的 SA-1B 专用去重审计：**NOT FOUND。**
- 同类别前序工作：*On the De-duplication of LAION-2B.* Webster et al. 2023. arXiv:2303.12733（网络规模图像去重 / 逐字复制分析）。
- *Soft Contamination Means Benchmarks Test Shallow Generalization.* 2026. arXiv:2602.12413（语义重复污染夸大了 benchmark 增益；虽偏向 LLM 但框架可迁移）。
- *Revising RVL-CDIP.* arXiv:2606.31446（在标准视觉 benchmark 中事后发现了 35% 的测试-训练近似重复重合）。
- 数据来源事实：Kirillov et al. 指出 SA-1B 图像是**从摄影服务商处获得授权许可的**，而非从 Flickr/网络爬取 — 这降低了（但未消除）与源自 Flickr 的 benchmark 产生重合的先验概率。

**他们实际做了什么。** 工具链（SSCD/pHash）、污染分析套路以及令人尴尬的事后重合发现先例均已存在；尚无人将其针对 SA-1B ↔ 分割 benchmark 对进行检验。

**保留的确切差异。** 审计本身。这确实未经运行、成本极低且仅限评估。诚实的风险在于：SA-1B 的授权许可来源使得零结果（null result）成为最大概率的结局，而此处的零结果只是一条社交媒体动态，成不了论文。

**剩余新颖性：** REAL（作为未经运行的审计），具备条件价值。
**新颖性置信度：** 3。
**Reviewer #2 可能引文：** Webster et al. (arXiv:2303.12733) — "dedup methodology is standard"。
**裁决：** **SURVIVE**（作为守门审计，而非旗舰项目）。
**杀手级实验（Killer experiment）：** 在 SA-1B（发布划分）与包含 23 个数据集的 SA-23 套件及 COCO/LVIS/DAVIS 验证集之间进行 SSCD + pHash 近似重复检索；预注册：若在任何套件上重合率 ≥0.5%，报告重合子集 vs 干净子集的分数差；若低于该阈值，在更广泛的评估规范论文中发表一段文字并停止。

---

## 聚类 11 — 标注者噪声底线（Annotator noise floor） (C1-016)

被攻击的主张：主要分割 benchmark 上的 SOTA 方法差距处于标注者间噪声底线之内，且该底线“在主要分割集上未发表”。

**最接近的前序工作**
- *Label Convergence: Defining an Upper Performance Bound in Object Recognition through Contradictory Annotations.* Tschirschwitz & Rodehorst. 2024. arXiv:2409.09412. https://arxiv.org/abs/2409.09412
- *Benchmarking Object Detectors with COCO: A New Path Forward (COCO-ReM).* Singh et al. ECCV 2024. arXiv:2403.18819. https://arxiv.org/abs/2403.18819
- *LVIS.* Gupta, Dollár, Girshick. CVPR 2019（内置在 benchmark 中的双标注一致性测量）。
- *Segment Anything* §Dataset（人工审计：将 SA-1B mask 质量与已发表的 COCO/LVIS/OpenImages 约 0.85–0.91 的标注者间 IoU 进行对比）。

**他们实际做了什么。** Label Convergence 论文就是 C1-016 的已执行版本：它估计了由标注一致性所隐含的性能上限（LVIS 收敛区间 62.6–67.5 mAP），并观察到 Co-DETR 达到 66.8 — 即“SOTA 处于噪声底线之内”，采用与 C1-016 所提相同的重复标注方法学发表。COCO-ReM 表明 COCO 的 mask 噪声大到足以重排 50 个检测器。LVIS 在 2019 年就发表了标注者一致性统计数据；SAM 论文自身的审计*引用了*这些数据。“主要分割集的噪声底线未发表”的前提在事实上是错误的。

**保留的确切差异。** 可提示/交互式指标（NoC）而非 mAP — 这只是一个脚注，因为 RClicks 已经处理了交互式指标的人类方差方面。

**剩余新颖性：** NONE。
**新颖性置信度：** 5。
**Reviewer #2 可能引文：** arXiv:2409.09412。
**裁决：** **KILL**。

---

## 聚类 12 — ~16 px 尺度底线（Scale floor ~16 px） (A1-073)

被攻击的主张：在低于约 16 px 的物体上，SAM mask 是与边界框填充基线无法区分的噪声；在任何人微调之前确立该底线并对补救措施（切片平铺、上采样）进行排名。

**最接近的前序工作**
- *Computer-Vision Benchmark Segment-Anything Model (SAM) in Medical Images.* He et al. 2023. arXiv:2304.09324 — 跨 12 个数据集的广义线性模型（GLM）：相对目标大小是 SAM Dice 单一最显著的预测因子。
- *Segment anything model for medical image analysis.* Mazurowski et al. MedIA 2023 — 目标大小 vs 性能分析。
- *Segment Anything Model for Medical Images?* Huang et al. MedIA 2024. arXiv:2304.14660 — 按大小/对比度分层的失效。
- *Slicing Aided Hyper Inference (SAHI).* Akyon et al. ICIP 2022. arXiv:2202.06934 — 平铺切片作为标准小目标补救方案，带有按大小分层的报告惯例（COCO AP-small）。

**他们实际做了什么。** SAM 质量对尺度的依赖性是 SAM 评估文献中被复现次数最多的发现之一；补救措施排名（切片保留分辨率；上采样不增加信息）是成熟的 SAHI 结论外加 COCO 小/中/大分层惯例。真正缺乏的是*零假设校准（null calibration）*：尚无人报告尺寸阈值，在低于该阈值时 SAM 的 Dice 在统计学上与直接填满提示框无法区分。

**保留的确切差异。** 作为硬性底线数值的框填充等效阈值。属于一张插图的体量。

**剩余新颖性：** SLIVER。
**新颖性置信度：** 4。
**Reviewer #2 可能引文：** He et al. arXiv:2304.09324 + SAHI。
**裁决：** 作为独立论文予以 **KILL**；框填充零假设图应作为强制报告分支包含在候选池中存活的其他小目标或医学评估之中。

---

## 聚类 13 — 嵌入尺度粒度旋钮（Embedding-scale granularity knob） (A1-101)

被攻击的主张：将稀疏提示 token 嵌入乘以标量能够单调地引导冻结 SAM 输出在局部与整体之间切换 — 一种潜在的、免训练的粒度控制。

**最接近的前序工作**
- *GraCo: Granularity-Controllable Interactive Segmentation.* Zhao et al. CVPR 2024 Highlight. arXiv:2405.00587 — 连续粒度滑块，通过在自动生成的 mask-粒度对上进行 LoRA 微调实现。
- *Semantic-SAM.* Li et al. 2023. arXiv:2307.04767 — 训练得到的多粒度分割。
- *Segment Anything.* Kirillov et al. — 通过 multimask 头实现的 3 级离散粒度（平凡基线）。
- 在冻结 SAM 提示嵌入中免训练的潜在旋钮发现：**NOT FOUND。**

**他们实际做了什么。** GraCo 通过训练交付了该*能力*（用户可控粒度）；Semantic-SAM 原生训练支持该能力；SAM 自身暴露了三个离散级别。尚无人报告提示嵌入范数的标量能调节冻结模型中的粒度 — 若属实且具有单调性，这是关于 decoder 如何编码尺度的真实机制发现，而不仅仅是一个更廉价的 GraCo。

**保留的确切差异。** 零训练 vs LoRA 训练，外加可解释性主张（粒度线性编码在提示 token 幅度中）。能力上 GraCo 胜出；机制上该问题完全开放。

**剩余新颖性：** REAL (机制), SLIVER (能力)。
**新颖性置信度：** 3。
**Reviewer #2 可能引文：** GraCo ("granularity control exists; what does training-free add?")。
**裁决：** **SURVIVE** — 但表述为机制发现，而非 GraCo 的竞争者。
**杀手级实验（Killer experiment）：** 在包含嵌套 GT 的 1k 张 SA-1B 图像（外加 PartImageNet）上，对点提示嵌入扫描标量 α ∈ [0.25, 4]；预注册单调性（α vs mask 面积以及 vs 局部/整体一致性的 Spearman 相关系数）以及两个淘汰条件：(a) 非单调/杂乱响应，或 (b) 无法击败在 SAM 自身三个 multimask 输出之间进行选择的平凡基线。2 个 GPU 天；一周内决定生死。

---

## 聚类 14 — 通道提升灰度图（Channel-lift grayscale） (A1-033)

被攻击的主张：微小的已学 1→3 通道提升（1×1 conv）在灰度医学模态上优于通道复制，且以 ~0.1% 的参数逼近 LoRA；伪 RGB 接口是一个被忽视的自适应表面。

**最接近的前序工作**
- *SAM-aware Test-time Adaptation for Universal Medical Image Segmentation (SAM-TTA).* 2025. arXiv:2506.05221 — 一种学习得到的自适应贝塞尔曲线变换（12 个参数），将灰度转换为面向 SAM 的 3 个多样化通道，明确以通道复制为动机并展示了优越性。
- *COVID-19 Classification ... with Three-Channel Grayscale CT Images.* MDPI Big Data Cogn. Comput. 7(1):36, 2023 — 基于 HE/CLAHE 的 3 通道组合在预训练模型上优于复制。
- *RepViT-CXR.* 2025. arXiv:2509.08234 — 胸部 X 射线 ViT 的通道复制策略，讨论了复制非最优性。
- 临床实践先验：多窗位 CT 合成为 RGB 通道是标准的放射学预处理技巧。

**他们实际做了什么。** SAM-TTA 在相同模型类别上提出了完全相同的论题：伪 RGB 接口是一个自适应表面；映射 1→3 通道的少数已学参数在医学图像上对 SAM 优于复制。MDPI 论文在 2023 年提出了非学习版本的论点。A1-033 的确切工具（1×1 conv）和确切对比（在匹配参数预算下 vs LoRA）属于 SAM-TTA 框架下的消融级差异。

**保留的确切差异。** 参数化形式（线性 conv vs 贝塞尔强度曲线）以及 LoRA 对比表格。

**剩余新颖性：** SLIVER。
**新颖性置信度：** 4。
**Reviewer #2 可能引文：** SAM-TTA (arXiv:2506.05221)。
**裁决：** **KILL**。

---

## 聚类 15 — 检测器框抖动预算（Detector-box jitter budget） (A1-071)

被攻击的主张：SAM mask IoU 保持平坦，直到边界框抖动超过目标尺寸的约 20% 时发生崩塌 — 从而定义了检测器→SAM pipeline 中最弱可用检测器的边界。

**最接近的前序工作**
- *Robust Box Prompt based SAM (RoBox-SAM).* Huang et al. MICCAI MLMI 2024. arXiv:2407.21284 — 系统性的 0–30% 随机框偏移遍历（99,299 张图像，5 种模态）、退化曲线及修复方案。
- *Segment Anything Model for Medical Images?* Huang et al. MedIA 2024. arXiv:2304.14660 — 确立了边界框抖动敏感性。
- *SAM on Medical Images: A Comprehensive Study on Three Prompt Modes.* Cheng et al. 2023. arXiv:2305.00035 — 抖动尺度遍历；"prediction accuracy decreases with jitter scale"。
- *BREPS.* arXiv:2601.15123 — 最坏情况真实边界框搜索；~30% IoU 下降；逐像素框放置 IoU 热力图；15 个模型。
- *FNPC.* 2023. arXiv:2308.10382 — 超声上的边界框位置/大小敏感性 + 多框增强补救方案。

**他们实际做了什么。** 抖动-IoU 曲线已至少被独立发表了四次，包括确切的“SAM 能够承受多大边界框误差”的框架（RoBox-SAM：10% 以内稳定，向 30% 逼近时崩塌；BREPS：在真实边界内发生灾难性最坏情况）。“预算”数字及其类别依赖性可以直接从这些曲线中读取。将该预算与*特定检测器*的误差分布（S-126 火灾 pipeline 变体）进行匹配属于系统工程。

**保留的确切差异。** 无实质差异。

**剩余新颖性：** NONE。
**新颖性置信度：** 5。
**Reviewer #2 可能引文：** RoBox-SAM + BREPS。
**裁决：** **KILL**。

---

## 总结总表（Summary table）

| # | 聚类（牵头 ID） | 杀手级前序工作 | 剩余新颖性 | 置信度 | 裁决 |
|---|---|---|---|---|---|
| 1 | Oracle-prompt protocol (S-003, A1-118, C1-115) | RClicks; BREPS; Mazurowski MedIA'23 | NONE/SLIVER | 5 | KILL |
| 2 | Tight-box image ablation (S-014, S-604) | Stable-SAM (仅相邻) | REAL | 4 | **SURVIVE** |
| 3 | Nested multimask (S-018, C1-061, A1-003) | SAM 论文设计; GraCo | NONE / SLIVER→REAL | 5/3 | MUTATE → "歧义性遗忘" |
| 4 | Negative-click paradox (S-005, A1-007) | RITM; FocSAM; DiffClick | SLIVER | 4 | KILL |
| 5 | Prompt-evolution scorer failure (S-007, S-347) | SAMPOT 自身的失效分析 | SLIVER | 3 | MUTATE → 评分器有效性审计 |
| 6 | Human vs simulated clicks (A1-105, C1-003) | RClicks; PointPrompt | NONE | 5 | KILL |
| 7 | Patch-grid aliasing (A1-002) | arXiv:2606.08132; Alias-Free ViT | NONE/SLIVER | 4 | KILL |
| 8 | Topology/holes prior (A1-004) | 拓扑分割领域; COCO-ReM holes | SLIVER | 3 | MUTATE → 先验 vs 惯例 vs 后处理三方分解 |
| 9 | Prompt-distribution shift (A1-091, A1-118) | RClicks; BREPS | NONE/SLIVER | 4 | KILL |
| 10 | SA-1B leakage (C1-001) | NOT FOUND (同类: LAION 去重) | REAL, 条件性 | 3 | **SURVIVE** (守门审计) |
| 11 | Annotator noise floor (C1-016) | Label Convergence arXiv:2409.09412; COCO-ReM; LVIS | NONE | 5 | KILL |
| 12 | Scale floor ~16 px (A1-073) | He et al. 2304.09324; SAHI | SLIVER | 4 | KILL (保留框填充零假设作为报告分支) |
| 13 | Embedding-scale granularity (A1-101) | GraCo (仅能力) | REAL (机制) | 3 | **SURVIVE** |
| 14 | Channel-lift grayscale (A1-033) | SAM-TTA arXiv:2506.05221 | SLIVER | 4 | KILL |
| 15 | Box-jitter budget (A1-071) | RoBox-SAM; BREPS; 2305.00035 | NONE | 5 | KILL |

## 对 Stage-3 候选池的影响

- Windows4 的整个“真实提示评估”阵营（此处聚类 1, 6, 9, 15；波及更宽候选池中的 C1-038, S-016, S-019, A1-048, A1-094）均已被 RClicks/BREPS 团队占领。建议进行全池筛查：任何最小实验为“微扰或重新分布提示并重测 IoU”的假设，在进入 Stage 4 之前都应依据这两篇论文重新审计。
- 建议推进的存活项：**S-014/S-604**（紧框内部图像证据消融 — 本批次中唯一真正未经运行的因果探针）、**A1-101**（免训练粒度旋钮，作为机制）、**C1-001**（SA-1B 去重，作为带有预注册停止规则的低成本守门审计）。重新进入候选池的变体：**C1-061**（歧义性遗忘）、**S-007 作为评分器有效性审计**、**A1-004 作为三方分解**。
- Stage 2 的收敛性预警得到了印证：四个最高置信度 kill 中有三个（聚类 6, 9, 11）是在 ≥3 个种子批次中均出现的设想。跨批次收敛预测了*优先性*，而事实上该领域早已将它们发表。
