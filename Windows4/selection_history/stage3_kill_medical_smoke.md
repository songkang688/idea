# Stage 3 — 前序工作狙杀（Prior-Work Assassination）：Medical / SAM2-memory / Smoke-Fire / Glass / RT 聚类

日期：2026-08-28。角色：前序工作狙杀者（Prior-Work Assassin）。默认立场：**已经发表（already published）**。
认识状态（Epistemic status）：**基于真实、公开可查论文的评审判断（REVIEW JUDGMENT）**（以下所有引文均在此轮审查中经过网络核实；无一虚构）。凡是未能定位到确切主张之处，均明确标注为 **NOT FOUND** — 这是此处唯一接受的新颖性凭证。

输入：`stage2_top200.md` 聚类线索、`literature_anchors.md`、`stage1_supervisor_seed.md` / `stage1_A1.md` 中的原始假设文本。

每个目标的模式（Schema）：最接近的工作 → 它们做了什么 → 确切差异 → 剩余新颖性（NONE / SLIVER / REAL）→ 置信度 → R2 引文（唯一的拒稿武器）→ 裁决（KILL / MUTATE / SURVIVE，若存活则给出杀手级实验 killer experiment）。

记分板：在被攻击的 28 个 ID 中，**15 个 KILL / 8 个 MUTATE（→7 个合并后的变体）/ 5 个 SURVIVE**。

---

## 1. Decoder 局部的医疗差距 / 预处理 > PEFT — S-041, S-044, A1-034, A1-032

**假设（Hypotheses）。** S-041：冻结 encoder 并仅微调 SAM 的 decoder 可以弥合大部分 MedSAM 差距。S-044/A1-034：超声图像的经典去斑（despeckling）对冻结 SAM 的性能提升超过（decoder）LoRA。A1-032：针对每个器官的 1-D CT window/level 搜索无需训练即可恢复 SAM 因对比度失效导致的大部分性能损失。

**最接近的工作（Closest works）。**
- Gu et al., *How to build the best medical image segmentation algorithm using foundation models: a comprehensive empirical study with Segment Anything Model*, arXiv:2404.09957。系统性地消融了 **mask-decoder-only vs encoder+decoder** 微调（涵盖原生全微调与 PEFT，18 种组合，17 个放射学数据集）。结果：decoder-only 是 *insufficient*（不足的）；在 encoder 和 decoder **两者**上都进行 PEFT 胜出。
- Ma et al., *Segment Anything in Medical Images* (MedSAM), Nature Communications 2024 / arXiv:2304.12306 — 完整的 encoder+decoder 微调，prompt encoder 保持冻结。
- Wu et al., *Medical SAM Adapter*, arXiv:2304.12620 — 医疗领域针对 SAM 的 adapter PEFT（anchor：极为拥挤）。
- Chen et al., *RobustSAM: Segment Anything Robustly on Degraded Images*, CVPR 2024 / arXiv:2406.09627 — 明确讨论了将图像恢复预处理作为直觉替代方案，并论证了学习得到的退化不变模块优于预处理。
- Lee et al., *Practical Window Setting Optimization for Medical Image Deep Learning*, arXiv:1812.00572 — 学习/优化的 CT 窗宽窗位（windowing）可提升模型性能（SAM 时代之前）。
- SAMCT, arXiv:2403.13258 — 专家针对每个对象选定的 CT 密度窗作为标准预处理。
  zero-shot SAM2 应用于 CT 的论文常规性地应用并消融了 windowing（一篇 2026 年的 SAM2 骨骼 CT 研究 arXiv:2603.23116 报告仅靠 windowing 相比原始 HU 输入就能将分割效果提升 ~30%；JMIR 的 SAM2 腹部器官研究 PMC12231515 将 W/L 400/50 固定为标准协议）。

**确切差异（Exact difference）。** S-041 的*特定实验已经被 Gu et al. 运行过了* — 且已发表的结论与假设完全相反（冻结 encoder 会损失大量 Dice；encoder 的自适应至关重要，因为 SAM 的 encoder 是针对自然图像调优的）。对于 A1-032，将 CT 窗宽窗位作为低成本自适应手段已是常规实践，并在 SAM2-CT pipeline 内部得到了量化；不需要有人专门写一篇题为 "window search as PEFT baseline" 的论文，因为每个 pipeline 都在默默这样做。真正缺失的内容是：在提示匹配的前提下，在超声上进行 **head-to-head despeckle-vs-LoRA**（NOT FOUND），即对“预处理恢复 ≥50% 的 PEFT 增益”进行量化验证。

**剩余新颖性（Remaining novelty）。** S-041: **NONE**（问题已被提出并被不利地解答）。A1-032: **NONE**（标准实践，已被部分量化）。S-044/A1-034: **SLIVER**（head-to-head 的具体数值）。

**置信度（Confidence）。** High (S-041, A1-032), Medium-High (S-044/A1-034)。

**R2 引文（R2 citation）。** Gu et al., arXiv:2404.09957 ("fine-tuning only the mask decoder is generally insufficient"；在 17 个数据集上 encoder+decoder PEFT 均表现更优)。

**裁决（Verdict）。** S-041 **KILL**。A1-032 **KILL**（折叠为下文基线表中的一行）。S-044/A1-034 **MUTATE** → 一篇紧凑的证伪论文："physics-aware preprocessing vs PEFT on promptable models"。杀手级实验（Killer experiment）：3 个超声数据集（如 BUSI, TN3K, CAMUS）+ 2 个 CT 器官数据集；冻结的 SAM/SAM2 配合 {raw, NLM/despeckled, windowed} × {no FT, decoder LoRA, enc+dec LoRA}，采用完全相同的 box-prompt 协议；仅当预处理在 ≥2 个数据集上恢复 ≥50% 的 LoRA 增益时，该主张方可成立。成本极低、结论明确，且其失败模式（预处理抹除了真实边界）本身亦可成文报告。

---

## 2. 各向异性 vs “医疗” 3D / SAM2-as-video — S-042, A1-039

**假设（Hypotheses）。** S-042：3D 上的失效在于各向异性（anisotropy），而非其“医疗属性”；各向同性重采样（isotropic resampling）对 SAM 的提升超过医疗微调。A1-039：将 z 轴视为时间；在最大截面切片上进行提示并双向传播优于从顶层切片传播（“prompt-slice policy unstudied”）。

**最接近的工作（Closest works）。**
- Ma et al., *Segment Anything in Medical Images and Videos: Benchmark and Deployment*, arXiv:2408.03322 — 中间切片 box prompt、双向 SAM2 传播作为**默认协议**，之所以如此选择是因为 "because it usually has the largest object size"。
- Dong et al. (Mazurowski lab), *Segment anything model 2: an application to 2D and 3D medical images*, arXiv:2408.00756 — 在 18–21 个数据集上遍历了 prompt-slice 选择（最大切片 vs 中心切片，"F-modes"）、传播方向（单向 vs 双向，"D-modes"）以及预测通道。
- BioSAM-2 / Biomedical SAM-2, arXiv:2408.03286 — 中间切片提示并先向后后向前传播，并将其作为既定选择引用。
- JMIR AI 2025 SAM2 腹部 CT 研究 (PMC12231515) — 明确消融了每个器官的 prompt 切片位置（尾侧 caudal / 中间 mid / 头侧 cranial）。
- MedSAM-2, arXiv:2408.00874 — 认为切片顺序/朝向在医疗体数据中没有意义，处理 6 个朝向，并引入自排序记忆库（anchor）。
- CSAM, *A 2.5D Cross-Slice Attention Module for Anisotropic Volumetric Medical Image Segmentation* (PMC11349312) — 将各向异性作为一等公民问题；nnU-Net (Isensee et al., Nature Methods 2021) 将感知间距的重采样确立为行业准则。

**确切差异（Exact difference）。** A1-039 的 "unstudied prompt-slice policy" 已经被研究得透彻穷尽 — 最大切片 vs 中间切片 vs 位置提示、双向传播，正是 arXiv:2408.00756 的消融网格以及 arXiv:2408.03322 中的默认做法。对于 S-042，*因果分解（decomposition）*才是核心重点：尚未发现有任何论文在固定数据的前提下，将 zero-shot SAM2 传播 Dice 作为重采样切片间距的受控函数进行测量，并进而将该提升与医疗微调进行对比（NOT FOUND）。每个人都把重采样当作基本规范；但没有人发表过因果归因实验指出“各向异性解释了‘医疗差距’的 X%”。

**剩余新颖性（Remaining novelty）。** A1-039: **NONE**。S-042: **SLIVER→REAL**（混淆项剥离，一条干净的曲线）。

**置信度（Confidence）。** High (A1-039), Medium (S-042 — 很难绝对证明确切分解的完全缺失；某些 benchmark 的附录中可能包含我未曾发现的间距消融）。

**R2 引文（R2 citation）。** Dong et al., arXiv:2408.00756 (prompt-slice/direction 消融)；Ma et al., arXiv:2408.03322 (中间切片双向作为默认)。

**裁决（Verdict）。** A1-039 **KILL**。S-042 **MUTATE** → 纯粹的混淆项分析论文。杀手级实验（Killer experiment）：固定原生间距 ≥3 mm 的 TotalSegmentator/AMOS 体数据；在 {native, 3 mm, 1.5 mm, 1 mm-iso} 重采样下评估冻结 SAM2 的传播，对比原生间距下的 MedSAM-2/微调 SAM2；报告仅靠重采样所弥合的“医疗差距”比例，以及跨数据集的 Dice-vs-anisotropy-ratio 曲线。若重采样带来的 Dice 变化低于微调变化的 30%，则该假设淘汰。

---

## 3. 嵌套的器官内肿瘤物体性（Nested tumor-in-organ objectness） — S-054, A1-040

**假设（Hypotheses）。** S-054：给定肿瘤点提示时，SAM 的物体性先验（objectness prior）更倾向于选中整个器官（LiTS 肝内肿瘤失效规律）。A1-040：SAM 的贴边先验（snap-to-edge prior）对浸润性肿瘤分割不足，误差随着边界弥散度（diffuseness）增大而增加。

**最接近的工作（Closest works）。**
- Mazurowski et al., *Segment Anything Model for Medical Image Analysis: an Experimental Study*, Medical Image Analysis 2023 / arXiv:2304.10517 — 专门分析了 **嵌套物体提示歧义性（nested-object prompt ambiguity）**（"a point in a necrotic tumor component could mean the component, the tumor, the hemisphere, the brain, or the head"），展示了其上的 multimask 输出，并报告了较差的肿瘤分割性能。
- Kirillov et al., *Segment Anything*, ICCV 2023 — multimask 输出的存在正是为了应对嵌套物体的歧义性（整体/部分/子部分 whole/part/subpart）。
- Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024 — 在病灶上的 prompt 类型敏感性与不稳定性（anchor）。
- Self-Prompt-SAM, arXiv:2502.00630 — 记录了点提示崩塌至器官/胸腔尺度区域的现象。
- He et al., arXiv:2304.09324 — zero-shot SAM 在微小/低对比度（即弥散）结构上表现最差。
- Xu et al., *Flaws can be Applause* (A-SAM), NeurIPS 2024 — 将 SAM 在嵌套/多标注者结构（LIDC, BraTS）上的歧义性作为建模目标。

**确切差异（Exact difference）。** 该现象（肿瘤内点提示 → 器官 mask；嵌套解剖结构的歧义性）已有图文和数据发表。NOT FOUND 的部分是：**参数化定律（parametric law）** — 将有符号边界误差表达为受控边缘弥散度参数的单调函数（A1-040 的合成梯度宽度扫描），即对失效进行*预测（prediction）*而非仅仅是*描述（description）*。

**剩余新颖性（Remaining novelty）。** S-054: **NONE**。A1-040: **SLIVER**（定量定律 + 临床关联）。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** Mazurowski et al., MedIA 2023 / arXiv:2304.10517（嵌套提示歧义性章节）。

**裁决（Verdict）。** S-054 **KILL**。A1-040 **MUTATE** → "boundary-diffuseness failure law"。杀手级实验（Killer experiment）：将具有参数化梯度剖面宽度的合成病灶插入真实 CT/MR 背景中；绘制 SAM/SAM2/MedSAM 的有符号边界误差与宽度的关系曲线；在 LiTS 浸润性 vs 局限性亚组上验证拟合定律的预测效果。若该关系非单调或仅局限于特定数据集，则淘汰。

---

## 4. 患者级划分的数据泄漏（Patient-level split leakage） — S-068

**假设（Hypothesis）。** SAM 医疗微调论文中的图像级划分（image-level splits）夸大了所报告的增益；按患者重新划分将使该领域的增益大幅缩水。

**最接近的工作（Closest works）。**
- Yagis et al., *Effect of data leakage in brain MRI classification using 2D CNNs*, Scientific Reports 2021 (PMC8604922) — 切片级划分对比受试者级划分会使准确率虚高 25–55%；在切片级划分下，随机标签甚至仍能达到 ~96% 的“准确率”。
- *How You Split Matters*, arXiv:2309.00350 — 纵向 3D MRI 中的数据泄漏。
- Rouzrokh et al., *Mitigating Bias in Radiology Machine Learning: 1. Data Handling*, RadioGraphics / Radiology: AI 2022 (PMC9533091) — 将患者级划分作为标准准则，并给出了肝脏 MRI 多序列的示例。
- medRxiv 2020.04.23.20076406 — 对 Coudray et al. 的重新分析，揭示了切片级划分导致的指标虚高。

**确切差异（Exact difference）。** 其机制、量级和补救措施在各种模态和任务中均已有发表文献；这在当下已是教科书级别的方法论。唯一未发表的部分是一份*普查（census）*：到底哪些特定的 SAM/MedSAM 微调论文使用了图像级划分，以及在患者级重新划分后其 delta 缩小了多少（作为 SAM 专有审计未被找到 NOT FOUND）。但这属于元研究/科学新闻调查，并非科学假设 — 且其影响力依赖于公开点名曝光（shaming），而非科学本身。

**剩余新颖性（Remaining novelty）。** **NONE**（现象本身）；SLIVER（SAM 领域审计，科学上限较低）。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** Yagis et al., Sci Rep 2021 (PMC8604922)。

**裁决（Verdict）。** 作为独立假设予以 **KILL**。在所有存活的 Windows4 实验中，保留患者级划分作为强制性的基本规范（hygiene）；若需要审计，可作为另一篇论文中的一个表格，而不是独立成文。

---

## 5. SAM2 记忆机制：打乱 / 记忆关闭 / 邻近性 / 位置崩塌 — S-073, S-079, S-081, A1-017

**假设（Hypotheses）。** S-073：打乱切片顺序会破坏原生 SAM2，但不会破坏基于 bag-of-memory 的变体。S-081：在 2D 静态图像上禁用记忆库应当能恢复 SAM 的表现 — 否则属于训练伪影。S-079：记忆嵌入（memory embeddings）编码的是位置/顺序而非外观（线性探针 linear probe）。A1-017：遮挡恢复能力在超出记忆库时间跨度后发生急剧崩塌。

**最接近的工作（Closest works）。**
- MedSAM-2, arXiv:2408.00874 — *正是建立在与 S-073 完全相同的前提之上构建其自排序记忆库*："in medical imaging, the order of slices may not be meaningful"；用基于置信度/相似度排序的记忆取代基于邻近性（recency）的记忆。
- Dong et al., arXiv:2408.00756 — 已经在医疗体数据上运行了 **清除记忆 vs 保留记忆（memory-cleared vs memory-retained）** 的迭代精细化（即 S-081 的消融实验，已执行），并报告 SAM2 在单帧 2D 上 ≈ SAM。
- Ding et al., *SAM2Long*, ICCV 2025 / arXiv:2410.16268 — 诊断了贪婪记忆选择和误差累积问题；提出了免训练的记忆树；对遮挡/重现具备鲁棒性（属于 A1-017 的范畴）。
- Yang et al., *SAMURAI*, arXiv:2411.11922 — 感知运动的记忆选择，取代朴素的 FIFO 邻近性机制。
- Videnovic et al., *DAM4SAM* (distractor-aware memory), arXiv:2411.17576 — 自省式记忆更新。
- SLM-SAM 2, arXiv:2505.01854 — 针对医疗体数据中过度传播的长短期记忆库。
- *An Analysis of Segment Anything 2*, arXiv:2503.00042 — 开始探索记忆交叉注意力及对象指针的可解释性（记忆特征/指针编码了什么）。
- 架构事实（sam2 代码库，facebookresearch/sam2）：最近帧记忆仅有 6 个学习得到的时间位置编码 + 提示帧 1 个 — A1-017 想要揭露的“显式常数”已经在代码中公开可见，这也正是 SAM2Long/SAMURAI 所利用的切入点。

**确切差异（Exact difference）。** 邻近性/贪婪记忆的病态已经被诊断并被反复修复（这是一个拥挤的修复市场：SAM2Long, SAMURAI, DAM4SAM, SLM-SAM2, MedSAM-2）。医疗领域关闭记忆和顺序/方向的消融实验已经存在。NOT FOUND 的部分是：针对记忆内容的**表征层探针（representation-level probe）** — 在记忆库嵌入上训练线性探针以量化位置 vs 外观信息，并将探针读数与传播失效联系起来。目前还没有人发表过*记忆内部实际编码了什么*；大家发表的都是对其的*替代方案*。

**剩余新颖性（Remaining novelty）。** S-073: **NONE**（前提已被 MedSAM-2 消耗；打乱诊断只是一张插图，而非一篇论文）。S-081: **NONE**（已完成）。A1-017: **NONE→SLIVER**（截断对比记忆库大小的曲线是对已知失效的量化，且已有现有修复）。S-079: **REAL**（机制性内容分析尚缺）。

**置信度（Confidence）。** High (S-073, S-081, A1-017), Medium (S-079 — 可解释性工作正在加速；arXiv:2503.00042 邻近该领域，可能在数月内发生撞车 scoop）。

**R2 引文（R2 citation）。** MedSAM-2 arXiv:2408.00874 (顺序无意义论断 + 排序记忆)；SAM2Long arXiv:2410.16268 (误差累积、遮挡)。

**裁决（Verdict）。** S-073 **KILL**，S-081 **KILL**，A1-017 **KILL**。S-079 **SURVIVE**。S-079 的杀手级实验（Killer experiment）：冻结 SAM2；运行医疗体数据和自然视频；提取记忆库条目；针对 (a) 帧/切片索引，(b) 对象/器官身份，(c) 外观聚类 训练线性探针；报告探针准确率比值并将位置主导性与传播失败案例相关联；随后进行因果检验 — 在推理时置换时间位置编码并测量相比置换记忆特征带来的 Dice 损伤。若外观信息占主导或位置主导性无法预测失败，则淘汰。

---

## 6. 单提示漂移（One-prompt drift） — S-074

**假设（Hypothesis）。** 切片 0 上的单个提示会随切片距离增加而退化；漂移曲线（Dice vs Δslice）可证伪每卷单个提示的主张。

**最接近的工作（Closest works）。**
- Dong et al., arXiv:2408.00756 — 确切测量了该现象：全卷单个提示的平均值为 0.36，而逐切片提示为 0.50；性能随着与标注切片距离的增加而下降；将其归因于传播误差累积（提示切片的 IoU 保持稳定）。
- Ma et al., arXiv:2408.03322 — 在提示的中间切片上的过分割会在 PET 体数据中传播；用更好的中间切片 mask 初始化可将 3D DSC 提升高达 17.5%。
- SAM2Long, arXiv:2410.16268 — 量化了自然视频中传播片段上的性能下降。

**确切差异（Exact difference）。** 无实质差异。漂移曲线已存在于多个 benchmark 中；对“单个提示过度夸大”的批评已然是 SLM-SAM 2 和 MedSAM-2 等后续工作的动机阐述。

**剩余新颖性（Remaining novelty）。** **NONE**。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** Dong et al., arXiv:2408.00756。

**裁决（Verdict）。** **KILL**。

---

## 7. 烟雾作为 Alpha 通道 / 指标反转 / 本体论 — S-096, S-097, A1-046

**假设（Hypotheses）。** S-097：烟雾是密度场而非实例 — 基于实例的 SAM 无法表示重叠的烟羽。A1-046：为 SAM 添加一个微小的 alpha 回归头。S-096：在 alpha-MAE 与二值 Dice 评估下，模型排名会发生反转。

**最接近的工作（Closest works）。**
- Yuan et al., *A Wave-Shaped Deep Neural Network for Smoke Density Estimation*, IEEE TIP 2020 — 单图像烟雾**密度回归（density regression）**；明确将密度定性为分割/检测的正确目标。
- Yuan et al., *Deep Smoke Segmentation*, Neurocomputing 2019 / arXiv:1809.00774 — 通过 alpha 混合合成烟雾；**ground truth 即为 alpha 通道**（DS01–03 数据集）；评估包含了针对 alpha 的逐像素 MSE。
- Yan et al., *Transmission-Guided Bayesian Generative Model for Smoke Segmentation*, AAAI 2022 — 透射率（transmission ≈ alpha）作为物理引导；对标注不确定性建模；SMOKE5K 数据集。
- Li et al., *Matting Anything (MAM)*, CVPR Workshops 2024 / arXiv:2306.05399 — **在冻结的 SAM 上构建轻量级 Mask-to-Matte 头（2.7 M 参数）**，根据 box/point/text 提示预测 alpha matte。Yao et al., *Matte Anything*, arXiv:2306.04121 — 同属该领域。
- Anchor：Pattern Recognition 上的 density-aware progressive smoke segmentation with SAM background priors。
- Rhemann et al., *A Perceptually Motivated Online Benchmark for Image Matting*, CVPR 2009 — 标准 alpha 误差指标套件（SAD/MSE/gradient/connectivity）。

**确切差异（Exact difference）。** 本体论主张（S-097）在烟雾文献中已有 5 年以上历史 — 密度/透射率回归本身就是已发表的重构范式。架构主张（A1-046）实质上就是将 MAM 替换为“烟雾”一词。唯一 NOT FOUND 的内容是：**指标有效性研究（metric-validity study）** — 选取 N 个已发表的烟雾分割模型，在 alpha-GT 数据上用二值 IoU/Dice 对比 alpha-MAE 进行评分，并展示排名反转（Kendall τ），即证明该领域的排行榜存在指标伪影。

**剩余新颖性（Remaining novelty）。** S-097: **NONE**。A1-046: **NONE**（MAM 的领域移植）。S-096: **SLIVER→REAL**（尚未有人做过该反转研究；所有要素均已齐备）。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** Yuan et al., IEEE TIP 2020 (烟雾密度估计)；Li et al., arXiv:2306.05399 (MAM)。

**裁决（Verdict）。** S-097 **KILL**。A1-046 **KILL**。S-096 **MUTATE** → 指标反转论文（根据 seed-2 变体与 S-612/S-632 合并）。杀手级实验（Killer experiment）：8–10 个已发表的烟雾模型 + MAM + 阈值化 SAM，在 DS01–03 + SMOKE5K（+alpha 子集）上运行；计算 {IoU, Dice} 与 {alpha-MAE, SAD, gradient} 之间的等级相关性；交付成果为 τ 矩阵以及前 3 名中的反转案例。若排名极其稳定（各处 τ > 0.8），则改为作为负结果简报（negative result note）发表。

---

## 8. 烟雾标注者间一致性上限（Inter-rater ceiling） — S-102, A1-054

**假设（Hypothesis）。** 烟雾边界上的标注者间 IoU（~<0.75）低于许多已发表的改进 delta，从而限制了有意义的进展；此前无人对此进行测量。

**最接近的工作（Closest works）。**
- 高光谱烟雾分割数据集论文，arXiv:2602.10858 — 每张图像三个标注者；报告了一致性统计数据（仅 52.07% 的标记为烟雾的像素达成全票一致；33.79% 为单标注者标记），明确讨论了透明区域的不一致性。“此前无人测量”的前提已被打破。
- Zhu et al., *CoSW: Conditional Sample Weighting for Smoke Segmentation with Label Noise*, NeurIPS 2024 — 将烟雾数据集中不可避免的标签噪声作为核心问题。
- Yan et al., AAAI 2022（见上文） — 对标注层面的不确定性进行了显式建模。
- Concentration-weighted forest-smoke segmentation, Electronics 2021 (doi:10.3390/electronics10212675) — 将半透明性引起的标注歧义作为动机问题。
- 通用的多标注者上限是成熟方法论：LIDC-IDRI 4 阅片者 mask、QUBIQ challenge（被 Medical Matting, arXiv:2106.09887 与 alpha mattes 结合使用）。

**确切差异（Exact difference）。** 烟雾上的原始分歧数据现已存在（高光谱，3 名标注者），且烟雾标签噪声是一个活跃的 NeurIPS 级别课题。NOT FOUND 的内容是：**正面交锋（confrontation）** — 将标准 RGB benchmark（SSD/SMOKE5K/DS0x-real）上的成对标注者间 IoU 上限，与这些相同 benchmark 上已发表的 SOTA delta 制表对比，得出结论：“在 M 个报告的改进中，有 K 个低于标注一致性上限”。

**剩余新颖性（Remaining novelty）。** **SLIVER**（对比表格；测量本身已不再具备新颖性）。

**置信度（Confidence）。** Medium-High。

**R2 引文（R2 citation）。** arXiv:2602.10858 (标注者间烟雾统计数据)；CoSW, NeurIPS 2024。

**裁决（Verdict）。** **MUTATE** → 并入 S-096 指标论文作为其第二支柱（上限 + 指标反转 = 一篇 "smoke evaluation is broken" 论文）。杀手级实验（Killer experiment）：从 SSD 和 SMOKE5K 测试集中抽取 150 张图像，由 3–5 名标注者标注；成对计算 IoU 和 alpha-MAE 上限；叠加已发表方法的 delta。若上限超过 0.85 IoU，则（作为焦点结论）淘汰 — 此时说明烟雾标签质量良好，仅指标批评部分存活。

---

## 9. 抠图到烟雾的迁移（Matting→smoke transfer） — S-103

**假设（Hypothesis）。** 在 alpha 抠图数据（人像/自然）上预训练比 COCO 式分割预训练能更好地迁移到烟雾 — 这是候选池中唯一具备物理机制的邻近领域迁移赌注（软边界 soft boundaries 是共享的结构）。

**最接近的工作（Closest works）。**
- Li et al., MAM, arXiv:2306.05399 — 在五个抠图数据集上训练，展示了跨任务抠图泛化能力；从未在烟雾上评估。
- Yuan et al., arXiv:1809.00774 / TIP 2020 — 目标端存在烟雾 alpha 数据。
- He, Sun & Tang, *Single Image Haze Removal Using Dark Channel Prior*, CVPR 2009 / TPAMI 2011 — 雾气透射率估计 ≈ 类烟雾介质的物理 alpha（免训练的邻近先验）。
- Sun et al., *Semantic Image Matting* 以及通用的 matting-transfer 文献均存在，但未找到 matting→smoke 迁移的研究。**NOT FOUND**：在烟雾 alpha/分割上对 matting-pretrained 与 segmentation-pretrained 模型进行的任何受控对比。

**确切差异（Exact difference）。** 所有要素均已发表，迁移主张本身未经测试。风险在于科学层面而非新颖性：迁移可能直接失败（人像到体积介质的领域鸿沟），且 MAM 使工程实现变得极其简单，因此速度至关重要。

**剩余新颖性（Remaining novelty）。** **REAL**（切口狭窄但干净，带有物理机制）。

**置信度（Confidence）。** Medium（MAM 应用周边的进展非常快）。

**R2 引文（R2 citation）。** 审稿人会挥舞 MAM arXiv:2306.05399 — 应对方式是指出 MAM 从未涉足烟雾，且该主张关注的是*预训练数据来源（pretraining data provenance）*而非架构。

**裁决（Verdict）。** **SURVIVE**。杀手级实验（Killer experiment）：相同的架构（MAM 头），三种预训练方案 — (a) COCO/SA-1B 分割，(b) 人像/自然抠图（P3M-10k, AIM-500, Composition-1k），(c) 从头训练 — 在有限的烟雾 alpha 数据（DS01–03 划分）上以对齐的预算微调，在 SMOKE5K-real 和留出的合成集上测试；报告 alpha-MAE 和样本效率曲线；以暗通道透射率作为免训练的底线基准。该主张仅在以下情况下存活：在所有数据预算下，matting-pretrain 均超越 segmentation-pretrain（超出随机种子噪声），且随着烟雾数据减少差距进一步扩大。

---

## 10. 匹配检测器的火灾 SAM（Detector-matched fire SAM） — S-126

**假设（Hypothesis）。** “基于 SAM2 的火灾分割”论文本质上是由检测器提示的 SAM2；当检测器 AP 匹配时增益消失 — 针对 ProFSAM 风格 pipeline 的狙杀实验。

**最接近的工作（Closest works）。**
- Ugwu & Zhang, *Promptable Fire Segmentation…* (ProFSAM), arXiv:2510.21782 (ICIGP 2026) — YOLOv11n 预测 box → SAM2/MobileSAM/TinySAM；box 提示优于 point/auto；确系 S-126 意图攻击的 pipeline，已被证实真实存在且结构与预设完全一致。
- Huang et al., MedIA 2024 及广泛的 prompt-sensitivity 文献 — mask 质量与 prompt/box 质量挂钩；box > point 的鲁棒性在各领域均有据可查。
- Dong et al./Ma et al. benchmarks — 用更好的 mask/box 初始化 SAM2 可提升下游所有指标（相同的归因逻辑）。

**确切差异（Exact difference）。** 分割质量主要取决于提示质量早已确立；专门针对火灾 pipeline 且匹配检测器 AP 的因果分解处于 NOT FOUND 状态 — 但这属于*反驳型实验（rebuttal experiment）*，而非独立贡献。其结论已被提示敏感性文献预先注定，其唯一可发表的形式是作为评估协议论文的一部分。

**剩余新颖性（Remaining novelty）。** **SLIVER**（归因实验；结论可预测）。

**置信度（Confidence）。** Medium-High。

**R2 引文（R2 citation）。** arXiv:2510.21782（被攻击目标本身承认提示占主导：box 策略决定了性能）。

**裁决（Verdict）。** **MUTATE** → 吸收进 prompt-distribution 评估聚类（A1-118/A1-091，cluster 31）：一项要求检测器提示的分割论文报告*条件化于 prompt AP 的增益*的协议，在火灾 + 医疗 + 玻璃上进行展示。作为独立论文：在非评论类 track 的任何会议上都将直接被拒（dead on arrival）。

---

## 11. 报警时间 vs mIoU（Time-to-alarm vs mIoU） — S-109, S-134

**假设（Hypotheses）。** 早期预警需要检测稀薄烟雾而非关注 IoU；报警时间（time-to-alarm）才是关键指标且与 mIoU 不相关；“任务重定义（task redefinition）”。

**最接近的工作（Closest works）。**
- Dewangan et al., *FIgLib & SmokeyNet*, Remote Sensing 2022 (doi:10.3390/rs14041007) — 野火烟雾 benchmark，其核心头条指标**就是以分钟计的检测时间（time-to-detection in minutes）**（列出了跨架构的 TTD 表格；基线为 3.12 min），并指出低 TTD 模型（ResNet50, 1.01 min）由于假阳性过高而无法使用 — 即准确率与 TTD 之间的权衡已被展示。
- *Multimodal Wildland Fire Smoke Detection*, arXiv:2212.14143 — 优化并报告了 TTD delta。
- 火灾检测标准实践（UL 268 / EN 54 风格的 time-to-alarm）远早于这一切。

**确切差异（Exact difference）。** 该指标早已存在，是野火旗舰 benchmark 中的主要指标，且正被积极优化。NOT FOUND：专门针对*分割*模型进行的 TTD-vs-mIoU 形式化相关性研究。但这残余的价值只是一张散点图，且 FIgLib 自身的表格已经暗示了这一点。

**剩余新颖性（Remaining novelty）。** “任务重定义”主张为 **NONE**；相关性曲线为 SLIVER。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** Dewangan et al., Remote Sensing 14(4):1007, 2022。

**裁决（Verdict）。** 两者均 **KILL**。若需要相关性图表，可作为 S-096/S-102 烟雾评估论文中的一张插图，利用带分割头的 FIgLib 序列完成。

---

## 12. 玻璃折射扭曲 / 双帧视差（Glass refraction warp / two-frame parallax） — A1-058, A1-063, A1-067

**假设（Hypotheses）。** A1-058：背景扭曲幅度可预测 SAM 对透明物体的逐实例 IoU。A1-063：SAM 特征光流与像素光流之间的双帧视差不匹配可在免训练条件下定位折射区域。A1-067：折射可测量地扭曲了 ViT 特征一致性，与光学预测吻合 — 机制性桥梁。

**最接近的工作（Closest works）。**
- Han et al., *SAM Meets Glass: Mirror and Transparent Objects Cannot Be Easily Detected*, arXiv:2305.00278 — SAM 在玻璃/镜面上失效；远低于 GDNet/TransLab/EBLNet。
- Xu et al., *TransCut*, ICCV 2015 — 光场畸变/线性度作为透明度信号（折射作为线索的先例，但需要光场采集）。
- Xue et al., *Refraction Wiggles for Measuring Fluid Depth and Velocity from Video*, ECCV 2014 — 跨帧折射引起的 motion-of-motion 特征；物理违背作为信号的先例，针对流体、基于经典强度特征。
- Xie et al., Trans10K/TransLab, ECCV 2020；Mei et al., GDNet, CVPR 2020 — 监督基线与数据集。
- Glass-SAM, ICASSP 2026 (doi:10.1109/icassp55912.2026.11461633) — 通过分形/形状上下文信号增强 SAM 用于透明物体 — 面向玻璃的 SAM 修复市场已经开启。

**确切差异（Exact difference）。** 折射作为信号已存在于光场（TransCut）和视频放大（wiggles）形式中。NOT FOUND 的内容是：(a) 单目扭曲幅度作为基础模型的*逐实例失效预测器*（A1-058）；(b) 基于两张普通帧的*基础模型特征 vs 像素光流*不匹配检测器（A1-063）；(c) ViT 特征位移对光学预测折射扭曲的任何定量回归（A1-067）。其新颖性在于将物理规律违背迁移到了基础模型表征空间中。

**剩余新颖性（Remaining novelty）。** A1-058: **SLIVER**（预测器，在 063/067 存在后虽有用但偏增量）。A1-063: **REAL**。A1-067: **REAL**。

**置信度（Confidence）。** Medium（透明物体方向小众；光场和偏振线索可能隐藏变体 — 偏振线索玻璃分割确实存在，如 Mei et al. CVPR 2022，但那是传感器线索而非表征物理学主张）。

**R2 引文（R2 citation）。** TransCut ICCV 2015 + Xue et al. ECCV 2014（审稿人："refraction cues are old"）；应对：那些工作需要光场/已知背景视频；我们的方法从两张普通帧的冻结 ViT 特征中读出物理违背。

**裁决（Verdict）。** A1-058 **MUTATE** → 作为 A1-063 的验证章节（扭曲幅度作为检测器背后的连续回归量）。A1-063 **SURVIVE**。杀手级实验（Killer experiment）：在玻璃场景上进行小基线双帧拍摄（手持）（Trans10K/GDD 重拍子集 + 新拍摄）；计算 RAFT 像素流 vs SAM/DINOv2 特征对应流；计算不匹配图对玻璃 mask 的 AUROC；对比免训练基线（显著性、单目深度不连续性、暗通道）和监督上限（GDNet）。若不匹配 AUROC ≤ 显著性基线，或其在镜子/镜面金属（无折射）上同样触发，则淘汰。A1-067 **SURVIVE** 作为机制性姊妹篇：已知折射率 IOR/几何形状的 Mitsuba 渲染 → 预测扭曲场；将逐 patch ViT 特征位移对预测光学扭曲进行回归（报告 R²）；随后在真实拍摄上测试蕴含的解析修正。若特征扭曲由注意力上下文而非几何主导（R² ≈ 0），则淘汰 — 这本身也是可报告的负结果。

---

## 13. 玻璃的深度边缘自动提示（Depth-edge auto-prompt for glass） — A1-060

**假设（Hypothesis）。** 单目深度不连续性生成的 box 可以在玻璃器皿上恢复手动提示 SAM 的大部分 IoU — 级联了两个单独使用时均会失效的冻结模型。

**最接近的工作（Closest works）。**
- Han et al., arXiv:2305.00278 — SAM 单独在玻璃上失效（前提的一半，已发表）。
- Sajjan et al., *ClearGrasp*, ICRA 2020 / arXiv:1910.02550 — 深度传感器/单目深度在透明物体上失效（前提的另一半，已发表）；预测 mask+法线+边界以修复深度 — 这是*相反*的级联方向。
- Glass-SAM, ICASSP 2026 — 针对玻璃的 SAM+先验，但基于分形/形状上下文，而非深度提示。
- 通过辅助模型对 SAM 进行通用自动提示是一个庞大的类别（检测器 box、显著性、文本）。

**确切差异（Exact difference）。** 该特定级联（单目深度边缘 → box prompt → SAM，在 Trans10K/GDD 上对比手动提示进行评估）处于 NOT FOUND 状态。但新颖性是组合式的而非概念性的：两种失效模式均已有据可查，自动提示已成范式，且现代单目深度（Depth Anything 类）在玻璃上的表现并不一致 — 该级联的前提（在深度*数值*不可靠的地方，深度*边缘*依然可靠）是唯一真正未经测试的主张。

**剩余新颖性（Remaining novelty）。** **SLIVER→REAL**（一项干净的系统科学结果；C1 审计将其复活是有原因的）。

**置信度（Confidence）。** Medium。

**R2 引文（R2 citation）。** ClearGrasp ICRA 2020（审稿人："depth fails on glass, your prompt source is broken"）；应对：该失效具有结构性 — 边界得以保留 — 且我们确切量化了保留程度。

**裁决（Verdict）。** **SURVIVE**（初级初阶规模 junior-scope）。杀手级实验（Killer experiment）：MiDaS + Depth-Anything 边缘 → box → SAM 在 Trans10K 和 GDD 上运行；报告恢复的手动提示 IoU 百分比，按玻璃类型分层；消融边缘来源（深度 vs RGB Canny vs 学习边界）；包含深度产生幻觉的失效分类。若 RGB 边缘表现与深度边缘同样好（此时深度模型无额外贡献），则淘汰 — 该对照实验是强制性的。

---

## 14. 部分容积效应作为 Alpha 通道（Partial-volume as alpha） — S-395

**假设（Hypothesis）。** CT 部分容积效应（partial volume）就是 alpha 抠图；将两者统一，引入抠图工具箱（在 Stage 2 中作为跨领域统一被保护）。

**最接近的工作（Closest works）。**
- Wang et al., *Medical Matting: Medical Image Segmentation with Uncertainty from the Matting Perspective*, MICCAI 2021 + Computers in Biology and Medicine 2023 / arXiv:2106.09887 — alpha matte 作为模糊病灶的软 mask；创建了医疗 alpha-matte 数据集（LIDC-IDRI, QUBIQ brain-growth, ISIC）；论证了 alpha 作为标注方法优于二值化。
- Wang et al., *3D Matting: a benchmark study on soft segmentation for pulmonary nodules in CT*, Computers in Biology and Medicine 2022 — 将 2D 抠图算法移植到 3D CT，**用放射密度校准 alpha matte**，构建了第一个 3D 医疗抠图数据集和端到端 3D 抠图网络。
- MICCAI 2024, *Multi-scale Region-aware Implicit Neural Network for Medical Images Matting* — 医疗抠图方向非常活跃。
- Van Leemput et al., *A unifying framework for partial volume segmentation of brain MR images*, IEEE TMI 22(1):105–119, 2003 — 通过 EM 将部分容积显式建模为混合分数；分数组织隶属度已是 20 多年前的方法论。

**确切差异（Exact difference）。** 这种“统一”已被发表了两次：分数隶属度 PV 建模（2003）以及带有放射密度校准的医疗 alpha 抠图（2021–2024）。唯一未被占领的细碎角落是：针对下采样高分辨率真实真值进行验证的显式*物理同一性*论证（成像 PSF 下 PV 分数 = 混合 alpha）— 这充其量只是一个推论，不足以支撑一篇论文。

**剩余新颖性（Remaining novelty）。** **NONE**（至多是推论尺度的 SLIVER）。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** Wang et al., arXiv:2106.09887 + CBM 2022 3D Matting (基于放射密度校准的 alpha)。

**裁决（Verdict）。** **KILL**。撤回 Stage-2 保护；成熟工具箱的引入工作此前已经发生。

---

## 15. 剂量不敏感的放疗勾画误差（Dose-insensitive RT contour errors） — S-513

**假设（Hypothesis）。** 表征不改变剂量的分割误差；强调临床相关性优于单纯追求 Dice（在 Stage 2 中作为杠杆率最高的评估设想受到保护）。

**最接近的工作（Closest works）。**
- *Clinically Oriented Contour Evaluation Using Dosimetric Indices Generated From Automated Knowledge-Based Planning*, IJROBP 2019 (S0360-3016(18)34045-8) — 针对每个勾画变体基于 KBP 生成放疗计划；几何-剂量学相关性微弱（在 126 个相关性中有 61% 的 R² < 0.2）；不存在可接受性的几何阈值；几何指标是剂量学影响的拙劣分类器。
- Sherer et al., *Metrics to evaluate the performance of auto-segmentation for radiation treatment planning: a critical review*, Radiotherapy & Oncology 2021 (PMC9444281) — 领域全范围结论：DSC/HD 与临床有意义的终点无关。
- *The predictive value of segmentation metrics on dosimetry in organs at risk of the brain*, Radiother Oncol 2021 (PMID 34293536) — Dice 与平均剂量效应之间的 Pearson 相关系数 ≈ −0.11；轮廓变异相对于靶区的方向才是关键决定因素（即*哪些*误差对剂量不敏感：已被表征）。
- ICCR 2024 (Groningen/NKI/Twente) — 自动分割对剂量学影响的 DIP/DIE 分解。
- Medical Physics 2025 wDSC 论文 (doi:10.1002/mp.17840) — 构建了用于编码剂量邻近性的距离加权 Dice；“修复”一代的工作已经展开。

**确切差异（Exact difference）。** 核心主张 — 许多几何误差不会改变剂量、Dice 无法分辨这些误差、误差相对于靶区的位置/方向决定了其实际影响 — 是大量放疗文献的既定共识，且已有综述和第二代纠正性指标。引入 SAM 并没有拯救它：更换分割器并不能改变评估科学的本质。

**剩余新颖性（Remaining novelty）。** **NONE**。

**置信度（Confidence）。** High。

**R2 引文（R2 citation）。** IJROBP 2019 KBP 勾画评估研究；Sherer et al. 2021 综述。

**裁决（Verdict）。** **KILL**。撤回 Stage-2 保护。如果 Windows4 想要一个感知剂量的切入点，开放的前沿在上游（例如将可提示分割的*不确定性*传播到 NTCP 中），但这属于 Stage 1 循环利用的新假设，而非本假设。

---

## NOT FOUND 登记簿（经检索未定位到的确切主张 — 唯一的鲜活新颖性）

1. 冻结 SAM 在超声上的 Head-to-head 去斑/NLM vs LoRA 对比（S-044/A1-034 sliver）。
2. SAM2 3D“医疗差距”中受控各向同性重采样 vs 微调的因果分解（S-042）。
3. SAM 有符号边界误差作为边缘弥散度的参数化函数（A1-040）。
4. SAM2 记忆嵌入的线性探针内容分析（位置 vs 外观）（S-079）。
5. 烟雾上 Dice vs alpha-MAE 的模型排名反转研究（S-096）。
6. RGB benchmark 烟雾标注者间一致性上限与已发表 SOTA delta 的正面交锋（S-102/A1-054）。
7. 烟雾 alpha 上的 Matting 预训练 vs 分割预训练迁移测试（S-103）。
8. 火灾 SAM pipeline 匹配检测器 AP 的因果归因（S-126）。
9. 分割模型跨架构的 TTD vs mIoU 相关性（S-109/S-134 残留）。
10. 单目逐实例扭曲幅度 → SAM 玻璃 IoU 预测器（A1-058）。
11. 基于两张普通帧的基础特征流 vs 像素流折射违背检测器（A1-063）。
12. ViT 特征扭曲对光学预测折射扭曲的回归（A1-067）。
13. 在 Trans10K/GDD 上评估的单目深度边缘 → box → SAM 级联（A1-060）。

## 裁决总表（Verdict table）

| ID(s) | Verdict | Novelty | Conf. |
|---|---|---|---|
| S-041 | KILL | NONE | High |
| A1-032 | KILL | NONE | High |
| S-044 + A1-034 | MUTATE (preprocess-vs-PEFT 证伪) | SLIVER | Med-High |
| A1-039 | KILL | NONE | High |
| S-042 | MUTATE (各向异性混淆分解) | SLIVER→REAL | Med |
| S-054 | KILL | NONE | High |
| A1-040 | MUTATE (弥散度失效规律) | SLIVER | High |
| S-068 | KILL (保留作为规范) | NONE | High |
| S-073 | KILL | NONE | High |
| S-081 | KILL | NONE | High |
| A1-017 | KILL | NONE→SLIVER | Med-High |
| S-079 | SURVIVE (记忆内容探针) | REAL | Med |
| S-074 | KILL | NONE | High |
| S-097 | KILL | NONE | High |
| A1-046 | KILL | NONE | High |
| S-096 | MUTATE (指标反转研究) | SLIVER→REAL | High |
| S-102 + A1-054 | MUTATE (并入 S-096 论文) | SLIVER | Med-High |
| S-103 | SURVIVE (matting→smoke 迁移测试) | REAL | Med |
| S-126 | MUTATE (并入 prompt-distribution 评估，cluster 31) | SLIVER | Med-High |
| S-109, S-134 | KILL | NONE | High |
| A1-058 | MUTATE (A1-063 的验证分支) | SLIVER | Med |
| A1-063 | SURVIVE (特征流折射违背) | REAL | Med |
| A1-067 | SURVIVE (特征扭曲 vs 光学扭曲) | REAL | Med |
| A1-060 | SURVIVE (深度边缘提示，带 RGB 边缘对照) | SLIVER→REAL | Med |
| S-395 | KILL (撤回保护) | NONE | High |
| S-513 | KILL (撤回保护) | NONE | High |

致导师备忘：两个在 Stage 2 中受到*保护（protected）*的想法（S-395, S-513）在此淘汰 — 当初保护是基于跨领域优雅性，而在这两起案例中，目标领域实际上早已完成了桥梁构建（Medical/3D Matting；放疗几何-剂量学文献）。存活的集合结构清晰连贯：一个表征科学探针（S-079）、一个迁移赌注（S-103），以及一个三部分的玻璃物理学研究计划（A1-063 + A1-067，配以 A1-058 作为验证，A1-060 作为应用型初级课题）。
