# Idea_01 — SupportAudit

**少样本分割的错误 support 反事实审计（Wrong-support counterfactual audit of few-shot segmentation）。**
内部 ID `B-0121` · Windows7 · **本轮首选推荐（#1）。**

> 给少样本分割器喂入一张确切在 query 图像中不存在的类别的 support 图像，测量其报告的准确率还能保留多少。

## 为什么此项目排名第一

| 属性 | 取值 |
|---|---|
| 产生决策的算力成本 | **~2 A100-days** (killer 实验)；完整方案约 ~5 A100-days |
| 训练需求 | **无** —— 仅推理（inference only） |
| 数据 / checkpoint | 全部公开可用 |
| 可发表的结果分支 | **全部三种**（排行榜重排 / 为基准正名 / 控诉基准） |
| 主要统计量 | **方法内部比率（within-method ratio）**，因此不依赖于复现任何人的绝对数字 |

它是 Stage 2 所有聚类中唯一获得全票通过的第一名，并且经受住了一轮严苛的 Reviewer #2 评审而非放水过关 —— 由于干预直接施加于输入端，没有任何架构层面的攻击点。

## 文件结构

| 文件 | 内容说明 |
|---|---|
| `proposal.md` | 完整的 28 节研究方案包。从这里开始阅读。 |
| `literature.md` | 先验工作、各篇论文的实际做法，以及我们与之的精确区别 |
| `experiments.md` | 实验矩阵 E0–E7、消融实验、对照组、决策规则 |
| `reviewer_attacks.md` | 攻击点 A1–A7 以及分别回应每条攻击的对应实验 |
| `roadmap.md` | 第 1 天 → 第 4 周实施路线图 |
| `diagrams/architecture.md` | Mermaid 协议与数据流图 |
| `src/` | 可运行的测试工具（harness）+ 统计量实现，已对照 mock 对照组完成验证 |
| `configs/` | 预注册文件（在执行任何推理之前冻结） |
| `references/` | checkpoint 清单模板、文献验证日志 |

## 立即运行测试工具

```bash
cd src
pip install -r ../requirements.txt
python run_mve.py --episodes 200 --seed 0
```

无需下载 checkpoint，无需 GPU。脚本会构建一个合成基准，运行整个审计流水线，并应用预注册的决策规则。

### 测试运行展示的内容

`MockSegmenter` 是一个带有可调 `support_reliance` 的测试夹具（test fixture），为测试平台提供了一个阳性对照和一个阴性对照：

```
method                stratum                      n  retention (ratio of means)    med    SSS
mock_support_blind    S1_single_object            60         1.000 [1.000,1.000]  1.000  0.000
mock_support_blind    S3_distractor_present       60         1.000 [1.000,1.000]  1.000  0.000
mock_support_driven   S1_single_object            60         1.000 [1.000,1.000]  1.000  0.000
mock_support_driven   S3_distractor_present       60         0.762 [0.651,0.871]  1.000  0.238 *
  * primary and median estimators disagree by >0.2 (bimodal episodes)
```

从中可以读出三点结论，且三者全都是**测量工具本身**的特性，而非针对任何已发表方法的结论：

1. **对照组在 `S3` 上成功分离。** 盲目无视 support 的方法保持了全部精度（1.000）；由 support 驱动的方法损失了可测量的份额（0.762，置信区间排除 1.0）。该审计能够精确检测出其旨在检测的效应。
2. **在 `S1` 上没有任何分离。** 当 query 中仅存在单个目标时，只有唯一的东西可供分割，因此摧毁 support 不会改变输出结果。这是基准退化（假设 H3）在微缩尺度下的重现，也是 `S3` 被设定为预注册主要分层的根本原因。
3. **`*` 标记至关重要。** 比值的中位数估计器对 support 驱动的对照组给出的报告值为 1.000 —— 它会完全遗漏该效应。逐 episode 的保持率呈双峰分布，因此主要统计量必须是均值之比（ratio of means）。该修正是在运行原型时发现的，并在 `proposal.md` §10 中进行了完整论证。

**本仓库中的任何数字均不是关于已发表方法的实验结果。** 上述所有内容均来自 mock 夹具，其唯一目的是验证测量装置。

## 首日要运行的第一个实验（Day 1）

不是 MVE —— 而是 **checkpoint 归档门禁**（E0）。下载并对评测矩阵中的每个 checkpoint 计算 SHA-256，优先处理 BAM（OneDrive）和 HSNet（Google Drive），因为链接失效是该项目最大的实际风险。将哈希值记录在 `references/checkpoint_manifest.md` 中。随后在运行任何推理之前冻结预注册文件（`configs/preregistration.yaml`）。

## Killer 实验

在预注册的 `S3` 存在干扰物（distractor-present）分层上：(a) 是否有 ≥ 半数的专有（specialist）方法在错误类别 support 下保持率 `R > 0.5`，并且 (b) 其正确 support 下的准确率在统计上与无 support 的 objectness 下界无法区分 —— 分别在强下界（SAM AMG）和弱下界（传统显著性）下单独报告？若两项检验均未通过，则核心头条结论被证伪，我们转而发表正名认证（certification）结果。

## 状态

设计已完成，测试工具可正常运行，统计量已对照 mock 对照组完成验证。尚未针对任何真实 checkpoint 运行。
