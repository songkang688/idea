# Idea_02 —— 烟雾／火焰基准上相机 ID 泄漏导致的指标虚高

**选题状态：** Final 3，**PROVISIONAL —— 尚未锁定。** Idea_02 是被
**GATE-A** 卡住的那一个：从来没有核实过任何公开烟雾／火焰数据集上是否
存在相机元数据，而本 package 自己的第一条停止规则就是
*"Kill if no camera metadata."*。见
[`../selection_history/stage6_battle.md`](../selection_history/stage6_battle.md) §5。

**证据状态：** **没有烟雾 mAP，没有训练过检测器。** `proposal.md` 写明
*"We have not trained a detector here."*。一切都是 HYPOTHESIS 或 EXPECTED
RESULT。脚本能跑，但跑在一个刻意植入了相机签名的合成语料上，而且在打印
任何数字之前都会说明这一点。

**假设。** 相对于**按相机划分（camera-disjoint）**，随机划分会让检测器
性能虚高；**按事件划分（event-disjoint，PYRONEAR 式）**与按相机划分*并不*
等价；而且来自**见过的**相机的空帧，其得分与来自未见过相机的空帧不同 ——
这是记忆，而不只是地理分布偏移。

## 为什么空帧就是整篇论文

"按相机划分分数更低"很容易被打发成普通的域偏移。空帧里**没有羽流**，
所以负样本上"见过 vs 未见过"的差距不可能是羽流外观造成的效应 ——
只能是背景造成的。正是这一点把一个域偏移观察变成一个记忆主张。

`proposal.md`：*"Fatal if we only report camera-disjoint drop without H4."*

## 现在就能跑（CPU，无需数据集，无需检测器，数秒）

```bash
python Idea_02/src/run_smoke.py --seed 0        # 划分结构门禁
python -m unittest discover -s Idea_02/tests    # 24 项自检
```

**只需要 numpy**。这道门禁检查的正是 H2 所依赖的那条性质：

| 协议 | 相机是否共享 | 事件是否共享 |
|---|---|---|
| random | > 0 | > 0 |
| **event_disjoint** | **> 0** | **0** |
| camera_disjoint | 0 | 0 |

中间那一行就是一行版的假设 —— 留出若干事件，塔（相机）却仍然留在训练集里。
如果代码根本产生不出这种结构，H2 就无从表达，任何真实实验都不值得开跑。

## Killer 实验

先跑卡片 **E-A**（GATE-A 的相机清点，不需要 GPU），然后跑卡片 **E1**：
PYRONEAR 子采样、YOLOv8n、1 个随机种子 × 3 种协议、相机 ID 探针、空帧
FPR。约 10 GPU-h（**HYPOTHESIS**）。见 [`experiments.md`](experiments.md)。

## Reviewer #2 附加的义务

原文照引 `stage4_reviewer2_cheap5.jsonl`：

> `Need event-disjoint vs camera-disjoint gap plus empty-frame memorization probe`

两个条件都要，不是任选其一。**另外请注意这里没有任何成文的降级条款** ——
与 Idea_01 不同，这个想法没有被给出 *"else …"*。唯一有记录的退路是
"相机少于 10 台时的转向"，而那会放弃 H2。`stage6_battle.md` §2.2 记下了
诚实的读法：**要么完整论文，要么杀掉。**

## 测试台抓到的两个协议缺陷

两个都会产出看起来可发表但实际上错误的结果，而且现在都被自检钉住了：

1. **相机 ID 探针原先是在随机划分上评测的。** 在把相机签名完全关掉之后，
   它仍然比随机猜测高出约 0.17 —— 它是靠识别火灾*事件*来说出相机是哪一台的，
   而不是靠识别塔。现在该探针一律在**按事件划分**下评测。
2. **空帧对比原先没有"见过的相机"那一侧。** 把空帧限制在测试划分里，
   在按相机划分下会把它们全部推到"未见过"那一侧，于是"见过"的 FPR 算出来
   是 `nan`。现在检测器只在非空帧上训练，因此每一张空帧都被留出，
   可以纯粹按"它的相机是否被见过"来划分。

## Package 地图

| 文件 | 内容 |
|---|---|
| [`proposal.md`](proposal.md) | 28 节：假设、测量工具、GATE-A、指标、kill 条件、决策树 |
| [`experiments.md`](experiments.md) | 卡片 E-A、E0–E5，含阈值与分叉 |
| [`reviewer_attacks.md`](reviewer_attacks.md) | Stage-4 的攻击 + 红队，含只被*部分*缓解的那两条 |
| [`roadmap.md`](roadmap.md) | 各阶段；哪些并行；哪些在 GATE-A 之前绝不开跑 |
| [`literature.md`](literature.md) | 只收已核实的条目；以及"不报我们没算过的虚高数字"这条规则 |
| [`diagrams/system.md`](diagrams/system.md) | 流水线图 |
| [`configs/`](configs/) | `default.yaml`（合成）与 `e1_killer.yaml`（真实协议） |
| [`src/camsplit/`](src/camsplit/) | 划分 + 重叠核算、指标、探针、检测器替身、流水线 |
| [`tests/test_smoke.py`](tests/test_smoke.py) | 24 项自检，只依赖 numpy |

## 代码有意拒绝去做的事

`data.load_real_corpus` 与 `detector.train_real_detector` 会抛出
`NotImplementedError` 并给出操作说明，而不是返回看起来合理的假输出。
`match_equal_n` 在无法匹配类别比例时会直接抛异常，而不是把一个不可比的
对比交付出去。`Split` 在训练／测试下标重叠时会抛异常。沉默正是那种把
EXPECTED 意外变成 ACTUAL 的失败模式。
