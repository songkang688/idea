# Idea_01 — SeeingInside

**SAM 究竟是在紧密边界框内观察图像证据，还是仅仅将边界框插值为掩码？**

| 字段 | 值 |
|---|---|
| Windows | Windows4 |
| Idea 槽位 | Idea_01（推荐 #1，Stage 6 锁定） |
| 项目 ID | P14 |
| 来源 Idea ID | S-014（紧密边界框内的图像证据消融），S-604（patch-shuffle 突变） |
| Stage-3 结论 | SURVIVE（`selection_history/stage3_kill_sam_eval.md`，Cluster 2） |
| Stage-4 结论 | WEAK ACCEPT 20 个项目排名第 1，基于 Reviewer #2 的重新设计要求（`selection_history/stage4_r2_setA.md`，P14） |
| Stage-6 锁定 | Idea_01，纯视觉（vision-only）；明确**不与 P107v / HalluSegBench 合并**（`selection_history/stage6_battle.md`） |
| 状态 | Stage 7 项目包 — 提案 + 可运行原型。**目前尚无科学实验结果。** |

## 一段话概述

当 SAM 接收到一个紧密边界框（tight bounding box）时，其输出掩码中有多少是由图像证据驱动的，又有多少仅仅是由边界框自身的几何形状驱动的？我们通过**流形内反事实（on-manifold counterfactuals）**来回答这个问题：保持 prompt 固定不变，通过修复去除目标（inpainting the object out）或替换为其他目标（swapping a different object in）来改变*边界框内的内容*——输入自然图像，输出自然图像。所有得分均对照三个**无图像证据零假设（no-image-evidence nulls）**进行校准：逐实例的凸性匹配框填充（convexity-matched box-fill）、*仅 prompt（prompt-only）*的 SAM 前向传播（将图像 embedding 替换为数据集均值），以及一个从不观察像素的小型*学习型 box→mask 回归器*。主要终点（primary endpoint）是低对比度医学图像领域，在该领域中紧密边界框提示是已部署的标准评测协议（MedSAM 类评估）：我们报告**在零图像证据下能够达到边界框 prompt Dice 的多大比例**。流形外探针（patch-shuffle S-604，embedding-mean S-014）被降级为次要收敛性检验，完全符合 Reviewer #2 的要求。

## 目录结构

```
Idea_01/
├── README.md                 ← 当前文件
├── proposal.md               ← 完整的 28 节研究提案
├── literature.md             ← 仅经验证的文献引用（Stage-3 列表 + Kirillov et al.）
├── experiments.md            ← 实验卡片 E0–E7，预注册阈值
├── reviewer_attacks.md       ← Reviewer #2 评审攻击及逐项应对方案
├── roadmap.md                ← 执行顺序、决策树、备用计划
├── diagrams/architecture.md  ← 流水线 + 决策逻辑的 Mermaid 架构图
├── configs/default.yaml      ← 原型的单一真实来源（SSOT）配置
├── requirements.txt
└── src/                      ← 可运行原型（杀手级实验 E0/E1 脚手架）
    ├── __init__.py
    ├── utils.py              ← 指标（Dice/IoU/boundary-F）、边界框操作、凸性、对比度
    ├── dataset.py            ← 合成可控数据集 + COCO/医学图像接口
    ├── model_sam.py          ← PromptableSegmenter 接口、官方 SAM 包装器、
    │                            BoxFillBaseline 存根、OracleThreshold 存根、学习型零假设模型
    ├── interventions.py      ← 目标移除修复、目标替换、patch 打乱、零假设干预
    ├── losses.py             ← 学习型 box→mask 零假设模型的 Dice+BCE 损失
    ├── train.py              ← 训练学习型无图像零假设模型
    ├── eval.py               ← 杀手级实验运行器（条件 × 填充 → 报告）
    └── inference.py          ← 单张图像演示
```

## 快速入门

```bash
pip install -r requirements.txt        # numpy+pyyaml 必须；torch/cv2 可选且优雅降级

# 在带有存根模型的合成数据上对完整杀手级实验流水线进行冒烟测试
# （在已知插值器和已知“具有视觉观察能力”的模型上验证决策逻辑）：
python -m src.eval --config configs/default.yaml

# 训练学习型 box→mask 无图像零假设模型（需要 torch）：
python -m src.train --config configs/default.yaml

# 当官方 SAM 权重可用时：
#   pip install git+https://github.com/facebookresearch/segment-anything.git
#   下载 sam_vit_h_4b8939.pth（或 vit_b），然后运行：
python -m src.eval --config configs/default.yaml \
    --override model.backend=sam model.sam_checkpoint=/path/to/sam_vit_b_01ec64.pth
```

## 认识论状态说明（Epistemic Status）

根据 Windows4 账本规范，本包中的每项主张均打上以下标签：
`KNOWN FACT | EVIDENCE | HYPOTHESIS | MODEL SPECULATION | EXPECTED RESULT | ACTUAL EXPERIMENTAL RESULT`。
**本包中暂无科学层面的 ACTUAL 结果。** 唯一的 ACTUAL 项目是带有存根模型的合成数据流水线冒烟测试输出，用于验证决策逻辑（见 `experiments.md` §E0）。所有关于 SAM 性能的陈述均为 EXPECTED 或 HYPOTHESIS。

## 具有约束力的既定义务（来自 Stage 4，不可协商）

1. 流形内的 inpaint/swap 反事实是**主要（primary）**干预手段。
2. Prompt-only 零假设和学习型 box→mask 零假设是**强制性（mandatory）**对比分支，且逐实例进行凸性匹配。
3. Embedding 均值替换（S-014）与 patch 打乱（S-604）仅作为**次要（secondary）**收敛性检验。
4. 低对比度医学图像（MedSAM 协议）是**主要终点（primary endpoint）**。
5. **不与 P107v / HalluSegBench 合并**：本项目干预的是可提示分割器在*边界框 prompt 内部的像素*；不提出任何关于 VLM/幻觉（hallucination）的主张。
