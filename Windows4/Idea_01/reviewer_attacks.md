# SeeingInside — 审稿人攻击与回应（Reviewer Attacks & Answers）

记录来源：`Windows4/selection_history/stage4_r2_setA.md`（P14 评审意见，有条件 WEAK ACCEPT）。以下每项攻击均直接引用/浓缩自该评审意见，或是针对下一轮评审的预判。状态列说明：**ANSWERED-BY-DESIGN**（重新设计的评测协议消除了该攻击点），**MEASURED**（对攻击提出的替代假设进行了量化测算而非单纯否认），**OPEN**（我们接受并公开披露的残留风险）。

---

## A. 来自 Stage-4 拒稿段落的四大攻击

### A1. 流形外消融谬误（Off-manifold ablation fallacy）
*"Zeroed/mean image embeddings and patch-shuffled interiors are inputs no natural image produces; decoder behavior under them licenses no conclusion about natural inputs."*
（置零/均值图像 embedding 以及打乱 patch 的内部区域是任何自然图像都不会产生的输入；解码器在这些输入下的行为不能支持关于自然输入的任何结论。）

**状态：ANSWERED-BY-DESIGN。** 核心干预手段现已改为流形内操作：基于扩散模型的去除修复（inpaint-out）与目标替换（object-swap）均生成自然图像；边界框保持不变；每次计分的前向传播所看到的都是符合常理的照片/扫描图。Embedding 均值替换（S-014，由直接置零软化而来）和 patch 打乱（S-604）仅作为*次要收敛性检验*（E2）保留，绝不用于支撑核心主张。若次要探针与主要探针结论不一致，以主要探针为准，并将该分歧作为关于流形外探针本身特性的发现予以报告。

### A2. 非局部化干预（全局 ViT 注意力机制）
*"Pixel corruption inside the box changes embeddings everywhere via attention; 'image evidence inside the box' is not a manipulable variable."*
（边界框内的像素损坏会通过注意力机制改变所有位置的 embedding；“边界框内的图像证据”并不是一个可单独操纵的变量。）

**状态：ANSWERED-BY-DESIGN。** 对于自然反事实而言，这不再构成混淆：当场景中确实不存在该目标时，所传播的任何全局影响都是*来自改变后场景的合法证据流*，这恰恰是我们关注的因果变量。我们操纵的是“目标的证据”（场景级别的事实），而非“裁剪框内部的像素”（实现细节）。虚假修复对照组（sham-inpaint，在边界框外部进行等面积背景编辑）从数值上界定了接缝/全局副作用的边界。

### A3. 位置支架退化（Positional-scaffold degeneracy）
*"The decoder re-injects positional encodings at every layer; emitting a clean box-shaped mask from positions alone is what the machinery should do — no discovered 'prior'."*
（解码器在每一层都重新注入位置编码；仅凭位置信息就输出清晰的框状掩码正是该机制理应做到的——并未发现所谓的“先验”。）

**状态：MEASURED。** 仅 prompt 零假设（Prompt-only null：数据集均值图像 embedding、真实边界框、真实位置支架）将这一解释性反驳转化为了一个可报告的具体数字：仅靠位置支架本身所能达到的 Dice。如果仅凭 prompt 的 SAM 在某个分层中就已经达到了 intact Dice，我们就如实报告这一现象——这*就是*插值器的发现，并将其正确归因于位置通路（KNOWN FACT，架构来源：Kirillov et al., arXiv:2304.02643），而非神秘化的“先验”。

### A4. 不对称收益（"if Dice collapses you proved the null everyone believes"）
*"若 Dice 分数崩溃，你只是证明了大家都相信的零假设"*

**状态：ANSWERED-BY-DESIGN。** 医学优先的立意框架。在自然图像上，BREPS（arXiv:2601.15123）已经动摇了紧密边界框协议的可信度，因此 COCO 分层只是一个*对照组*，而非主张所在。在 MedSAM 协议体系中，紧密边界框是现行的部署标准（arXiv:2304.12306），因此无论哪种分支都会带来实质性推动：H1 → 表明已发表的医学 Dice 指标混淆了评测协议信息与真实分割能力；H0 → 为该协议提供了经过零假设校准的有力辩护。Stage-3 的 kill 条件依然有效（全部分层差距 > 15 个点 → 终止），因此下行风险是廉价可控的，而非事后粉饰。

## B. 来自评审意见的隐性假设与混淆因素

### B1. 任务退化替代假设（Task degeneracy alternative）
*"Tight boxes on convex objects are near-sufficient statistics; ANY mechanism scores high."*
（凸目标上的紧密边界框几乎是充分统计量；任何机制都能拿到高分。）

**状态：MEASURED。** 这并不是一个需要排除的替代假设——它正是 NRF 所要估计的目标量。学习型 box→mask 零假设（完全不接触像素）直接估计了“仅凭标签统计信息 + 边界框几何形状所能支持的性能”。论文的主张据此措辞：不是“SAM 忽略了图像”，而是“在分层 S 中，零图像证据即可达到评测协议 Dice 的 X%，且 SAM 的反事实敏感性与此类机制在统计上无法区分”。SAM 的特异性来自于与 CSG/persistence/swap-tracking 的联合判定。

### B2. 凸性混淆（Convexity confound）
**状态：ANSWERED-BY-DESIGN。** 逐实例凸性匹配零假设（匹配实心度的填充，而非全局矩形）；将实心度作为预注册回归分析中的协变量；进行分层报告。

### B3. Padding 扫描混淆了 prompt 信息量与消融区域面积
**状态：ANSWERED-BY-DESIGN。** 进行解耦设计：padding 仅改变 prompt（消融区域固定为 GT 目标）；另设独立分支在固定 padding 下扫描消融区域的膨胀程度（E4）。

## C. 预判的下一轮攻击（我方红队推演）

### C1. “修复工具残留了目标信息” / 接缝伪影（seam artifacts）
修复算法可能会留下低级痕迹（频率特征、接缝），SAM 可能会读取这些痕迹。
**状态：MEASURED + OPEN。** 缓解措施：带有拒绝并重新采样的质量筛选；10% 人工审查；虚假修复（sham-inpaint）分支界定伪影效应的边界；经典修复算法收敛分支（属于不同的伪影体系 —— 跨工具的一致性可反驳伪影驱动的结论）。公开披露残留风险：没有任何筛选是完美的；这是医学模态（CT/超声修复的真实感）上的主要 OPEN 事项，也是为何替换分支（swap arm，其插入内容为真实图像素材）在医学模态中具有更高权重的原因。

### C2. “这就是 SAM 版的 HalluSegBench”（撞车相邻工作）
**状态：ANSWERED-BY-DESIGN。** Stage-6 主管裁定：不与 P107v 合并；HalluSegBench 基准测试评估的是*语言驱动分割中的幻觉*；SeeingInside 评估的是*基于边界框 prompt 的掩码解码器相对于无图像零假设的图像证据依赖性*。没有文本 prompt，没有 VLM，没有幻觉分类法，读出指标也完全不同（NRF/CSG/persistence vs 幻觉率）。提案 §23 阐明了这一边界；论文的相关工作章节将明确指出该差异，而非寄希望于审稿人忽略这种相邻性。

### C3. “基于 GT 生成的框是 oracle prompt；你们的审计继承了已被质疑的协议”
**状态：ANSWERED-BY-DESIGN。** 我们审计的是*实际部署状态下的*协议（MedSAM 类的评估）；结论关乎其数值的真实含义。Oracle prompt 只会让我们的证明更加严苛而非更容易：边界框越紧密，prompt 携带的信息越多，而这正是 NRF 所量化的内容。现实边界框分支（BREPS 风格的宽松边界框）是计划中的敏感性分析（E4），预计会*降低* NRF —— EXPECTED，单调性已预注册。

### C4. “在反事实图像上计算相对于原始 GT 的 Dice 是没有意义的”
若单独使用确实如此 —— 去除目标后已不存在真实目标。**状态：ANSWERED-BY-DESIGN。** Persistence（持久度）P = Dice(m_out, m_intact) 是主要反事实读出指标（掩码对掩码，无需 GT）；同时报告相对于 GT 的 CSG，以便与被审计的协议保持指标连续性；目标替换追踪（swap-tracking）则使用*已知的*插入掩码 s_new 作为参考标准。

### C5. “多掩码输出头选择机制掩盖了真实效应”
**状态：ANSWERED-BY-DESIGN。** 以单掩码输出头为主要实验；将多掩码 + IoU 预测头选择作为敏感性分析分支。（该混淆因素家族记录在 Stage-4 P101 评审中；多掩码设计是 SAM 论文的 KNOWN FACT。）

### C6. “仅测试了冻结的 SAM — 微调模型可能有所不同”
**状态：MEASURED。** 设立 MedSAM 检查点分支（E5）。EXPECTED 方向：使用边界框微调的解码器表现出*更高*的 NRF（边界框几何先验依据：arXiv:2606.04705）。无论何种结果都具有信息量；不作预设假设。

### C7. “n=1000 个实例样本量偏小”
**状态：OPEN（接受该风险）。** 统计功效：采用配对逐实例设计，并在中位数差距上使用 Bootstrap 置信区间；每个领域 500 个样本在 4×4×4 分层完全交叉下每单元约有 8 个实例，因此所有主张均在边际分层级别（如每个对比度四分位数等）提出，绝不在单个交叉单元级别提出。如果主要终点上的置信区间跨越了 τ 阈值，我们将在发表前扩充医学图像队列 —— 计算成本仅涉及前向传播。

---

## 既定执行纪律

- 严禁基于单一指标给出判定结论；提案 §15 中的四向合取条件是得出 "interpolator" 结论的唯一合规依据。
- 任何被证伪的实验都会直接淘汰其在决策树上对应的分支（见 `roadmap.md`）；严禁事后调整阈值 —— τ1–τ3 已在 `configs/default.yaml` 中冻结。
- 最终论文中的所有数字必须在代码库中附带 EXPECTED/ACTUAL 溯源标签。
