# Idea_01 —— 在 CT 上把 SAM AMG 视为强度聚类

**选题状态：** Final 3，**PROVISIONAL —— 尚未锁定。** Stage 1–6 均已
记录；锁定结论及其未关闭的门禁见
[`../selection_history/stage6_battle.md`](../selection_history/stage6_battle.md) §5。
Idea_01 是 Final 3 中唯一**没有任何未核实的数据或
checkpoint 前置条件**的一个，这也是 `Windows6/README.md` 把它标为
*"#1 start here"* 的原因。

**证据状态：** **没有任何真实 SAM 数字，没有真实 CT。** 本 package 中的
一切都是 HYPOTHESIS 或 EXPECTED RESULT。脚本能跑，但跑在一个合成
phantom 上，且用"阈值 + 连通域"作为 AMG 的替身，并且在打印任何数字之前
都会先输出一条占位横幅说明这一点。

**假设（可证伪）。** 在做过窗宽窗位处理的 CT 上，SAM Automatic Mask Generation
（AMG）产出的掩码集合与强度聚类（k-means / multi-Otsu / GMM）的一致程度
高于与基于纹理的超像素（SLIC）的一致程度；并且 AMG 会跟随**强度重映射**
而变化，同时对**保持强度不变的纹理置乱保持不变**。

如果纹理置乱那条臂对 AMG 的扰动与强度重映射一样大，那么这个
机制性主张就**死了** —— 见下方的降级路径。

## 一句话

SAM 在 CT 上的"objectness"，在做过窗宽窗位之后基本就是 HU 聚类 —— 除非
反事实实验给出相反结论。

## 现在就能跑（CPU，无需权重，无需数据，数秒）

```bash
python Idea_01/src/run_smoke.py --seed 0        # E0 测试台门禁
python -m unittest discover -s Idea_01/tests    # 22 项自检
```

**只需要 numpy**。scipy 和 PyYAML 只是可选的加速件；没有它们一切照样
能跑、能通过。如果测试台没能通过自己的 E0 门禁，`run_smoke.py` 会以非零
状态退出。

## Killer 实验（Day 1）

[`experiments.md`](experiments.md) 中的卡片 **E1**：**100** 张预先注册的
TotalSegmentator/MSD 切片，腹部窗，SAM ViT-B AMG 对比 k-means /
multi-Otsu / GMM / SLIC。三个预先注册的指标 —— Hungarian IoU、ARI、
boundary-F —— 全部报告。约 2 GPU-h（**HYPOTHESIS**）。

> 样本量在记录中曾不一致（有些地方写 50，有些地方写 100）。
> `stage6_battle.md` §4.7 记录了这一点，§6 裁定为 **100**。

之后是卡片 **E3**，即反事实各臂。E3 才是决定这究竟算不算一篇
机制性论文的那张卡。

## 决定这篇论文性质的那条义务

Reviewer #2 是**有条件地**让这个想法通过的。以下原文照引
`stage4_reviewer2_cheap5.jsonl`：

> `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`

卡片 E3 就是这条义务的全部内容。如果它失败，贡献就
降级为一篇 evaluation note —— 另外请注意 `stage6_battle.md` §4.4 记录的
那处未解决冲突：本 package 的 `reviewer_attacks.md` 把同一个条件读作
*"不要投稿"*，而不是*"降级"*。**动笔之前先把以哪一方为准定下来。**

## Package 地图

| 文件 | 内容 |
|---|---|
| [`proposal.md`](proposal.md) | 28 节：假设、方法、干预、基线、指标、kill 条件、决策树 |
| [`experiments.md`](experiments.md) | 卡片 E0–E6，含输入、阈值、分叉与预算 |
| [`reviewer_attacks.md`](reviewer_attacks.md) | Stage-4 的攻击 + 我们自己的红队，每条都附能回应它的证据 |
| [`roadmap.md`](roadmap.md) | 各阶段，什么并行跑，什么放最后跑 |
| [`literature.md`](literature.md) | 只收已核实的条目；无法核实的位置留作 `CITATION NEEDED` |
| [`references/math.md`](references/math.md) | 指标定义，包括 IoU 归一化为什么改过 |
| [`diagrams/system.md`](diagrams/system.md) | 流水线图 |
| [`configs/`](configs/) | `default.yaml`（合成 smoke 测试）与 `e1_killer.yaml`（真实协议） |
| [`src/amgclust/`](src/amgclust/) | 指标、分割器、干预、流水线、配置／随机种子控制 |
| [`tests/test_smoke.py`](tests/test_smoke.py) | 22 项自检，只依赖 numpy |

## 代码有意拒绝去做的事

`segmenters.sam_amg` 与 `data.load_real_ct_slices` 会抛出 `NotImplementedError`
并给出操作说明，而不是返回看起来合理的假输出。一个悄悄用 mock 顶替真实
组件的 package，正是 EXPECTED 意外变成 ACTUAL 的方式。
