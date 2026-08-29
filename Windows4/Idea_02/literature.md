# PromptAmnesia — 文献综述（Windows4 / Idea_02）

**认识论状态说明：** LITERATURE REVIEW。以下所有文献引用均**继承自 Windows4 Stage-3/4 验证流程**（`selection_history/stage3_kill_peft_vlm.md`, `stage4_r2_setB.md`, `literature_anchors.md`）。标签字面保留：

- `[V]` — 由 Stage-3/4 智能体于 2026-08-28 检索并阅读（摘要或全文）；
- `[M]` — 凭记忆引用的经典文献：确信其存在，**在任何手稿引用之前必须对照 arXiv 进行重新验证**（在 `roadmap.md` 中作为发布阻塞项追踪）。

在 Stage 7 未新增任何文献引用，以下亦不存在任何伪造引用。本文件任何位置均不宣称我们自身的实验结果。

---

## 1. 核心现象：微调侵蚀 SAM 的 Zero-Shot 行为

| 论文 | 标签 | 确立了什么结论 | 为何未能解决我们的问题 |
|---|---|---|---|
| Gu et al., *How to build the best medical image segmentation algorithm using foundation models*, MELBA 2025, arXiv:2404.09957 | [V] | 18 种微调组合 × 17 个数据集；原生全量微调在 ViT-B/H 上导致崩溃/灾难性遗忘；在编码器+解码器上应用 PEFT 表现更优；记录了流行方法的无效性；包含仅解码器微调分支 | 仅衡量**领域内（in-domain）Dice**；无逐 prompt 类型的 zero-shot 保留能力评估，无匹配增益对照，无覆盖率与遗忘的解耦分离，无噪声底线 |
| CA-SAM, *Continual Alignment for SAM*, arXiv:2511.17201 | [V] | 将泛化能力的侵蚀作为已知动机；提出在未见过的医学数据集上保留 zero-shot 的方法（9 个数据集的持续学习基准）；将问题定位在编码器–解码器接口（对齐层） | 仅报告了*其自身方法*的 OOD Dice — 非受控审计；无 prompt 类型分辨率；接口叙事是方法论包装，而非因果层面的探查 |
| EvoSAM, arXiv:2503.06236 | [V] | 基于 LoRA 专家的持续学习 SAM；将持续学习基线应用于 SAM/MedSAM | 属于修复赛道论文；预设了我们所要审计的测量现象 |
| MedSAM, Ma et al., Nature Communications 2024, arXiv:2304.12306 | [M] | 仅边界框微调；不支持点 prompt 或表现极差 | 这属于**覆盖率效应** — 我们的零假设模型（提案 §8），而非遗忘 |
| SAM-Med2D, Cheng et al., arXiv:2308.16184 | [V] | 使用框+点+掩码进行微调；发布了冻结 SAM 与微调变体在 Bbox/1pt/3pt/5pt 上的对比表 | 该表格未做匹配增益控制，采用朴素阈值，无负点击，无多样性分析，无随机种子/置信区间，无混合 vs 仅边界框析因设计 |
| Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024, arXiv:2304.14660 | [M] | 绘制了**冻结** SAM 的 prompt 类型敏感性图谱 | 冻结模型的敏感性 ≠ 微调诱发的性能变化 |
| Kumar et al., *Fine-Tuning can Distort Pretrained Features*, ICLR 2022, arXiv:2202.10054 | [M] | 微调会牺牲 OOD 稳健性以换取 ID 增益（分类任务） | 概念层面；无交互式/密集预测实例 |
| WiSE-FT, Wortsman et al., CVPR 2022, arXiv:2109.01903 | [M] | 权重插值描绘了增益-保留前沿曲线 | 在此用作 P177 中的 α 插值**基线**，并作为报告面板中的前沿图格式 |

## 2. SAM 上的构造性 PEFT 赛道（已饱和；仅作为背景）

| 论文 | 标签 | 相关性 |
|---|---|---|
| SAMed, Zhang & Liu, arXiv:2304.13785 | [M] | 医学图像上的 LoRA-on-SAM；训练配方参考 |
| Medical SAM Adapter, Wu et al. | [M] (anchors) | Adapter-PEFT 赛道拥挤 — Stage-1 淘汰区名单 |
| Conv-LoRA, Zhong et al., ICLR 2024, arXiv:2401.17868 | [V] | 宣称“保留了 SAM 的分割知识”；结构位置/归纳偏置工程（属于 P107 的领域，非本文领域） |
| LoRA, Hu et al., ICLR 2022 | [M] (anchors; 待重新核验 arXiv ID) | 所适配的方法本身 |
| VeRA, Kopiczko et al., ICLR 2024, arXiv:2310.11454 | [V] | 冻结随机低秩方向 + 训练缩放参数 ≈ LoRA。**强制对照分支**（Stage-3 cluster-2 裁定）：训练的 PEFT 效应必须战胜随机方向 |
| Dutt et al., *PEFT for Medical Image Analysis: The Missed Opportunity*, MIDL 2024, arXiv:2305.08252 | [V] | 17 种 PEFT 方法，700+ 次运行，在不同数据量下扫描全量微调基线；彻底否定了 C1-057（交叉效应）— 我们**不**重新主张交叉效应 |

## 3. 我们确认/扩展而非重新发现的遗忘科学

| 论文 | 标签 | 在 PromptAmnesia 中的定位 |
|---|---|---|
| Biderman et al., *LoRA Learns Less and Forgets Less*, TMLR 2024, arXiv:2405.09673 | [V] | 学习–遗忘耦合（LLM 领域）。我们的耦合回归在交互式分割机制中属于**验证性工作**（Stage-3 立意顺序）；同时预测了小可塑性微调表现出极小的真实遗忘 —— 这是 P082 通缩分支的驱动核心 |
| Soutif et al., *Empirical Analysis of Forgetting in Pre-trained Models with Incremental Low-Rank Updates*, CoLLAs / PMLR v274, 2025 | [V] | ViT 模型上 LoRA 秩与可塑性/遗忘的关系 |
| CoDyRA, arXiv:2412.01004 | [V] | 秩/位置与可塑性–稳定性权衡（视觉领域） |
| Ramasesh et al., *Anatomy of Catastrophic Forgetting*, arXiv:2007.07400 | [M] | 遗忘集中在更深层（分类任务）。P177 必须指出差异：prompt 交叉注意力在分类任务中没有对应物（Stage-3 F2 发散机制） |
| Davari et al., *Probing Representation Forgetting*, CVPR 2022, arXiv:2203.13381 | [M] | 表征级与输出级遗忘探针 |
| Lee et al., *Surgical Fine-Tuning*, ICLR 2023, arXiv:2210.11466 | [M] | 微调哪个模块取决于分布偏移 —— 机制定位问题的构造性孪生问题 |
| GEM, Lopez-Paz & Ranzato, NeurIPS 2017, arXiv:1706.08840 | [M] | BWT/FWT 标量指标 — 引用以阐明为何我们交付的是**面板（panel）**而非新的标量（接受 P110 REJECT） |
| Task arithmetic, Ilharco et al., ICLR 2023, arXiv:2212.04089 | [M] | 目标 vs 对照权衡面板属于常规做法 — 基于同样的原因 |

## 4. 测量规范（准入关卡的基石）

| 论文 | 标签 | 作用与定位 |
|---|---|---|
| Maier-Hein et al., *Metrics Reloaded*, Nature Methods 2024 | [M] | 阈值/工作点陷阱是公认准则；C1-082 将其应用于遗忘主张 — 业内已知的机制，尚未应用的空白 |
| RClicks / BREPS 系列（Stage-3 sam_eval 淘汰项） | 继承 | 淘汰了朴素点击模拟论文；迫使我们采用预注册模拟器 + 双模拟器敏感性重复验证 |
| Kornblith et al., CKA, ICML 2019, arXiv:1905.00414 | [M] | 表征漂移协变量记录（P108 残留） |
| Bansal et al., *Revisiting Model Stitching*, NeurIPS 2021, arXiv:2106.07682 | [M] | 拼接兼容性警告，促成了 P177 必须引入训练拼接对照 |
| Merchant et al., *What Happens To BERT Embeddings During Fine-tuning?*, arXiv:2004.14448 | [M] | 微调漂移剖析（NLP 领域），为协变量日志提供背景 |

## 5. 本项目包明确**不**提出的相邻主张

- **校准 / IoU 预测头失步** — 属于 P031 的论文领域（Laplace-LoRA arXiv:2308.13111 [V], BLoB, SWAG-LoRA arXiv:2405.03425 [V] 范式）。PromptAmnesia 仅在 oracle 分解判定为排序损失时*移交*多样性主张。
- **参数位置 → 错误类型** — 属于 P107 领域（He et al. arXiv:2110.04366 [M]; Conv-LoRA）。
- **数据规模交叉**（已否决：Dutt et al.）、**PEFT 复现诚实性**（已否决：Gu et al.）、**随机 LoRA 独立成文**（已否决：VeRA）、**保留能力单一标量**（已拒绝：P110）、**表征漂移预测**（已拒绝：P108）— 继承的所有评审结论均予接受；其残留内容仅作为对照/协变量/面板呈现。

## 6. 撞车监测（执行期间的常驻检索）

REVIEW JUDGMENT：风险最高的撞车方向，在预注册冻结前以及投稿前需重新检索：

1. 任何在 2026 年开展**在匹配增益下**按 prompt 类型分解保留能力或覆盖率/遗忘析因设计的论文（检索词："prompt-specific forgetting SAM", "promptability retention fine-tuning"）。
2. 任何将阈值/方差包络线应用于 SAM 遗忘主张的审计研究（P082 撞车点）。
3. 任何在可提示解码器上开展因果模块移植/拼接的研究（P177 撞车点）。
4. 发布带有逐 prompt 保留能力表格的新持续学习 SAM 模型（CA-SAM/EvoSAM 后续工作）— 这将缩小 §1 的差异增量，必须在相关工作部分明确对比。

若仅在 (1) 发生撞车，将动摇旗舰立意 → 回退方案为准入关卡/通缩分支加上机制分支（两者由于分别属于审计级和因果级，更难被抢发）。
