# Idea_01 —— 路线图

所有预算都是 **HYPOTHESIS**（估计值，抄录自
`selection_history/evolution_summary.md` 与 `experiments.md`）。没有一个是
实测运行时间。Windows6 的 **ACTUAL RESULTS 为零**。

排序原则：**最便宜的 kill 排最前。** 下面每个阶段的安排都遵循这一点：
最可能终结整个项目的那个实验，同时也是成本最低的那个。在机制被挣到手
之前，不跑任何昂贵的东西。

## Phase 0 —— 测试台验证（CPU，本 package 内已完成）

| | |
|---|---|
| **工作** | 卡片 E0。`python Idea_01/src/run_smoke.py`、`python -m unittest discover -s Idea_01/tests` |
| **成本** | CPU 数秒。不需要 GPU、权重、数据 |
| **退出条件** | E0 门禁 PASS 且 22 项自检全绿 |
| **状态** | **已完成。** 测试台通过；它抓到了两个缺陷（AMG 替身对分位数不变，以及 Hungarian IoU 用 \|A\| 做归一化），这两个缺陷各自都会静默地废掉一条假设。见 `experiments.md` E0 |

**Phase 0 换不到什么。** 换不到任何科学结论。它只意味着测量工具没有
明显损坏。

## Phase 1 —— 起机（第一次 GPU 会话）

| | |
|---|---|
| **工作** | 把 `segmenters.sam_amg` 接到真实的 `SamAutomaticMaskGenerator`；把 `data.load_real_ct_slices` 接到 nibabel/pydicom。目前两者都抛 `NotImplementedError` 并给出操作说明，而不是返回假输出 |
| **另外** | **预先注册那 100 张切片的清单并冻结它。** 要在看到任何结果之前完成 |
| **成本** | 约 1 GPU-h（**HYPOTHESIS**） |
| **退出条件** | 真实 AMG 在 5 张切片上端到端跑通，且指标表能填满 |

## Phase 2 —— E1 killer（H1）

| | |
|---|---|
| **工作** | 卡片 E1：100 张切片、腹部窗、AMG 对比 k-means / multi-Otsu / GMM / SLIC，三个指标全报 |
| **成本** | 约 2 GPU-h（**HYPOTHESIS**） |
| **继续条件** | 最好的强度基线在三个指标上都胜过 SLIC，且 bootstrap 置信区间不含 0 |
| **Kill 条件** | SLIC ≥ 每一个强度基线 |
| **标记条件** | 各指标结论不一致 —— 把这个标记带进 E2；在那里 H1 必须在三个指标上都成立，否则该主张就是依赖指标的 |

**这是整个项目的决策点。** 在它出结论之前不要开始 Phase 3。

## Phase 3 —— E2 ‖ E3（H3 与 H2，并行）

这两张卡片**不共享任何状态，可以在不同 GPU 上并发运行**。
E3 是科学上决定性的那张；E2 是保护它免受 Reviewer #2 攻击 A1 的那张。

| 卡片 | 工作 | 成本（**HYPOTHESIS**） | 分叉 |
|---|---|---|---|
| **E2** | 3 种窗 × 2 种 AMG 设置 × 3 个 k 值，完整网格全部报告 | 约 8–20 GPU-h | ≥2/3 的窗成立 → 继续 · 恰好 1 个 → **pivot** 成一篇窗宽窗位假象的论文 · 0 个 → **kill** |
| **E3** | 强度重映射臂（γ ∈ {0.4,0.5,0.7,1.4}）与纹理置乱臂（tile ∈ {4,8,16}），两者都带强制的有效性门禁 | 约 2–4 GPU-h | 出现解离 → 机制性论文 · \(s_{\mathrm{int}} \approx s_{\mathrm{tex}}\) → **降级** · \(s_{\mathrm{int}} > s_{\mathrm{tex}}\) → **kill**，报告负结果 · 方向随 tile 尺寸翻转 → **判该臂无效**，重新设计 |

**在 E3 完成之前，先解决那处长期悬置的严重性冲突。** Stage-4 的记录说
H2 失败意味着 *"else evaluation note"*（降级）；而本 package 的
`reviewer_attacks.md` B1 说的是*不要投稿*（扣下不发）。
`stage6_battle.md` §4.4 把它登记为未解决。它决定了在最可能出现的那条分支上
会发生什么，因此不能事后再定。

## Phase 4 —— E4 特异性（H4）

| | |
|---|---|
| **工作** | 卡片 E4：在一个 COCO 子集上跑完全相同的协议 |
| **成本** | 约 2 GPU-h（**HYPOTHESIS**） |
| **门禁** | **只在 E3 成功之后才跑。** 去控制一个还没挣到机制的效应的特异性，是没有意义的 |
| **Kill 条件** | COCO 上复现出了 CT 上的那个差距 —— 那么这篇 CT 论文就不存在了；最多只是一条关于 AMG 在单通道图像上的一般性注记 |

## Phase 5 —— 可选的加固

E5（SAM2 泛化性，约 4–8 GPU-h）与 E6（失败案例：金属、对比剂、
低剂量，约 1 GPU-h）。两者都是 **HYPOTHESIS**。都不在关键路径上；
只有在 Phase 2–4 已经产出一篇论文时才跑。

## Phase 6 —— 论文与发布

一篇短的分析型论文。发布内容：代码、配置、预先注册的切片清单、
逐切片的指标 CSV。只发布派生指标 —— 不再分发患者影像。

**候选标题。** *Is SAM AMG Just Intensity Clustering on CT?* ·
*Windowing, Superpixels, and the Objectness of Foundation Models* ·
*A Causal Test of SAM's CT Objectness*

## 预算汇总

| 路径 | 合计（**HYPOTHESIS**） |
|---|---|
| 在 E1 处 kill | 约 3 GPU-h |
| 在 E3 处 kill／降级 | 约 15 GPU-h |
| 走到 E4 完成一篇完整论文 | 约 15–35 GPU-h |
| 完整矩阵的上界 | 40–80 GPU-h（`experiments.md`） |

决策树存在的意义就是让那个上界永远不会被花掉。Day-1 是约 2 GPU-h，
即 `evolution_summary.md` 中记录的那个数字 —— 同样是估计，不是
测量。

## 长期规则

1. 最便宜的 kill 排最前；机制没挣到之前不跑任何昂贵的东西。
2. 先预先注册再测量 —— 切片清单、指标、阈值。
3. 有效性门禁未通过时，一个数字都不产出。
4. 每张卡片都报告全部三个指标，包括那些结论相互矛盾的。
5. 预算无论被引用到哪里，都保持标注为 **HYPOTHESIS**。

## 依赖图

```
Phase 0 (E0, CPU, 已完成)
   |
Phase 1 (起机 + 预先注册切片清单)
   |
Phase 2 (E1 killer, H1) ---- kill ----> 停止
   |
   +---------------+
   |               |
Phase 3a (E2, H3)  Phase 3b (E3, H2)  <-- 并行；E3 是决定性的那个
   |               |
   +-------+-------+
           |
   Phase 4 (E4, H4) ---- COCO 也复现出来 ----> 杀掉 CT 特异性
           |
   Phase 5 (E5/E6, 可选)
           |
   Phase 6 (论文)
```
