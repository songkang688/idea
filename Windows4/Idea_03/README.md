# Windows4 / Idea_03 — AlphaSmoke

**抠图数据源向烟雾分割的迁移（P103）+ 烟雾评估指标有效性协议（P096），二合一 Stage-7 项目包。**

- 最终 3 强锁定：`../selection_history/stage4_top20.md`（Idea_03），在 `../selection_history/stage6_battle.md` 中裁定。
- 吸收的 Reviewer #2 评审结论：P103 有条件 WEAK ACCEPT（`stage4_r2_setA.md`），P096 SILENCED 并强制设立实测 alpha 分支（`stage4_r2_setC.md`）。
- **认识论状态说明：PLAN。** 尚未运行任何实验。本包不包含任何实测结果；所有数字均为预算、预注册阈值或相应标注的预测值。主张均带有 `KNOWN FACT | EVIDENCE | HYPOTHESIS | MODEL SPECULATION | EXPECTED RESULT` 标签；`ACTUAL EXPERIMENTAL RESULT` 标签出现次数为零。

## 内容摘要（TLDR）

烟雾真实的 Ground Truth 是一个 alpha/透射率场（alpha/transmittance field），但该领域通常在二值掩码上进行训练和排名。AlphaSmoke 使用一套统一的实验工具探索两个相互关联的核心问题：

1. **迁移能力（P103）：** 在真实烟雾数据上，基于 alpha 抠图（alpha-matting）的预训练是否优于基于 COCO 分割的预训练 —— 并通过**二值化抠图分支（binarized-matting arm）**（相同的图像，相同的预算，破坏软标签连续性）来隔离软标签机制？在**真实烟雾（real smoke）**上设立主要终点；第 1 周的冻结编码器线性探针（frozen-encoder linear probe）作为是否投入后续预训练算力的准入关卡。
2. **指标有效性（P096）：** 二值指标（IoU/Dice/**Fβ/mMse**）与 alpha 指标（MAE/SAD/Grad/Conn）对模型的排名是否存在显著差异（Kendall-τ 矩阵 + top-3 逆序反转）—— 以通过对照已知烟雾前背景进行合成反演所恢复的**实测 alpha 真实测试集（measured-alpha real test set）**为锚点，并由带有预注册降级规则的**多标注员上限（multi-rater ceiling）**研究界定其有效边界？

无需训练的**颜色/物理底线模型（physics floors）**（暗通道先验 dark channel、HSV 低饱和度规则）作为每一项可学习模型主张的基准门槛。严格的范围界限：本项目**绝非**基于检测器提示的火灾/SAM2 流水线（S-126 在 Stage 3 已被合并至其他方向）。

## 具有约束力的既定义务（B1–B10）

定义及来源详见 `proposal.md` §2：二值化抠图分支（B1）、真实烟雾主要终点（B2）、实测 alpha 分支（B3）、mMse/Fβ 评估列（B4）、带有降级规则的标注员上限（B5）、物理底线模型（B6）、预测头对齐控制（B7）、匹配预算（B8）、模型池中包含 SFMattingNet（B9）、严禁引入检测器的范围约束（B10）。

## 项目包内容清单

```
Idea_03/
├── README.md                  ← 当前文件
├── proposal.md                ← 完整的 Stage-7 提案，假设 H1–H4，实验分支，Mermaid 架构概览
├── experiments.md             ← 预注册：终点指标、终止条件 K-A1..K-B5、决策树 (Mermaid)、运行手册
├── metrics_protocol.md        ← 精确指标定义、τ 协议、alpha 恢复数学原理、上限测算方法
├── datasets.md                ← 数据集/checkpoint 清单，附带诚实的 UNVERIFIED 获取状态标记
├── reviewer_attacks.md        ← 每项 R2 评审攻击及对应的设计解答；残留风险披露
├── CITATIONS.md               ← 带有 [V]/[S3]/[M] 验证标签的文献引用总账
├── literature.md              ← 叙述性文献综述（总账见 CITATIONS.md）
├── roadmap.md                 ← 依准入关卡排序的执行路线图
├── diagrams/architecture.md   ← 架构级 Mermaid 图
├── references/                ← 面向审稿人的参考文献要点说明
├── requirements.txt
├── configs/
│   ├── default.yaml           ← 以下各任务配置的索引
│   ├── pretrain_arms.yaml     ← 预训练分支 M / MB / S / S+cal / 0 (B1, B7, B8)
│   ├── datasets.yaml          ← 路径 + 角色（在 R0 之前所有路径均为 TODO）
│   ├── eval_protocol.yaml     ← 评估指标列含 mMse/Fβ (B4), τ 规范, 终止阈值, 模型池规范 (B9, B10)
│   ├── linear_probe.yaml      ← 第 1 周杀手级实验配置
│   ├── rater_study.yaml       ← 3–5 名标注员 × 150 张图像 (B5)
│   └── alpha_capture.yaml     ← 实测 alpha 采集 + 质量控制 (B3)
├── src/hsv_baseline.py        ← 兼容性垫片 → alphasmoke.baselines.color_hsv
├── src/metrics_alpha.py       ← 兼容性垫片 → alphasmoke.metrics
├── src/probe.py               ← 兼容性垫片 → alphasmoke.probes
├── src/alphasmoke/
│   ├── metrics/
│   │   ├── alpha_metrics.py       ← MAE/SAD/MSE/mMse/Grad/Conn (Rhemann 测试套件)
│   │   ├── binary_metrics.py      ← IoU/Dice/Fβ/boundary-F
│   │   └── rank_agreement.py      ← 符号对齐的 Kendall τ 矩阵、逆序统计、Bootstrap 置信区间
│   ├── baselines/
│   │   ├── color_hsv.py           ← HSV 低饱和度烟雾先验规则 (B6)
│   │   └── dark_channel.py        ← 暗通道透射率底线模型 (B6)
│   ├── alpha_recovery/
│   │   └── background_inversion.py ← 实测 alpha 恢复 + 有效性/敏感性掩码 (B3)
│   ├── probes/
│   │   └── encoder_linear_probe.py ← 冻结编码器 1×1 卷积探针存根 (torch; checkpoint 为存根)
│   └── rater/
│       └── ceiling.py             ← 成对 IoU / alpha-MAE 上限测算 + 对照表格 (B5)
└── tests/
    └── test_selfchecks.py     ← 合成数组上的单元自测试（非实验结果）
```

## 运行自测试

```bash
cd Windows4/Idea_03
pip install -r requirements.txt   # numpy/scipy/pyyaml; torch 可选（仅探针需要）
python -m pytest tests/ -q        # 或: python tests/test_selfchecks.py
```

这些测试验证了合成数组上的指标实现正确性（恒等映射 → 满分，构造的逆序被正确检出，已知 alpha 的合成图像被成功恢复）。它们属于代码正确性检查，**绝非**实验结果。

## 最优先运行项

依据 `experiments.md` 运行手册：R0 许可核查 → R1 依据已发布的 FoSp/SMOKE5K 评测代码交叉核对指标 → **R2 第 1 周线性探针**（决定所有预训练算力投入的关卡，终止条件 K-A1）→ R3 在合成 alpha 上的纯评测 τ 矩阵。唯有当探针展现出显著分离度时，才会为计算密集的训练分支网格提供算力预算。
