# Idea_03 —— 对齐后 VLM 中阶段隔离的定位税

**选题状态：** Final 3，**PROVISIONAL —— 尚未锁定。** Idea_03 被
**GATE-B** 卡住：还没有任何一对 base/chat checkpoint 被核实为共享视觉
编码器与坐标 tokenization，而本 package 自己的 `experiments.md` 一直把
这称为 *"Hard gate"*。见
[`../selection_history/stage6_battle.md`](../selection_history/stage6_battle.md) §5。

**证据状态：** **没有 VLM 评测，没有加载过任何 checkpoint。** 一切都是
HYPOTHESIS 或 EXPECTED RESULT。脚本能跑，但跑在模拟的"base"与
"chat"模型上，其失效模式是由配置选定的，而且在打印任何数字之前
都会说明这一点。

**假设。** chat 对齐后的 VLM 出现的定位能力退化，**并非**主要是
输出格式造成的假象，而且通过把格式受控的评测与冻结特征探针结合起来，
可以定位出到底是哪个阶段造成了它。

## 三分的答案

| | 探针完好 | 探针下降 |
|---|---|---|
| **似然差距 ≈ 0** | **O1** —— 格式假象。写负结果 | （不自洽 —— 去检查测量工具） |
| **似然差距 > 0** | **O2** —— 解码策略税 | **O3** —— 表征税 |

三种结果都可发表。这对科学是优点，对排优先级则是缺点：这个项目没有
便宜的 kill，所以唯一真正的门禁是 GATE-B，唯一真正的压力是时间。

## 现在就能跑（CPU，无需 VLM，无需 checkpoint，数秒）

```bash
python Idea_03/src/run_smoke.py --seed 0        # O1/O2/O3 往返门禁
python -m unittest discover -s Idea_03/tests    # 27 项自检
```

**只需要 numpy**。这道门禁会分别植入四种可能答案 ——
`none`、`format`、`policy`、`representation` —— 然后检查
`classify_outcome` 能否仅凭测量值把它还原出来。一个连植入的答案都还原
不出来的决策函数，绝不能拿去对准一个真实答案。

## 代码不允许你违反的那条规则

当缺少 likelihood-rank 模式时，`classify_outcome` 会**抛异常**。单靠
自由生成得到的差距无法与格式混淆因素分离，而跳过第 3 种模式是在这里
发表错误结果最容易的途径。那条 kill 规则 ——
*"Kill if H1 fails under constrained decoding"* —— 是在代码里强制的，
不只是写在文档里。

同样，`mean_iou` 会同时报告"把解析失败计入"和"不计入"两种 IoU。
这两个数字之间的差值**就是被量化出来的格式税**。一个 chat 模型回答
*"Sure! The cat is at [12, 30, 44, 80]"*，它其实定位对了；给它打零分
测的是文风。

## Killer 实验

先跑卡片 **E-B**（GATE-B，不需要 GPU），然后跑卡片 **E1**：一对已核实的
checkpoint、约 2k 条指代表达、三种评测模式（自由生成 / 语法受限 /
针对 ≤16 个**共享**干扰项的似然排序）外加冻结特征探针。≤8 GPU-h
（**HYPOTHESIS**），只做评测。见 [`experiments.md`](experiments.md)。

**STOP 规则，原文照引：** *"STOP if likelihood gap ~0 on pair 1 and pair 2. Do
not run DPO unless observational gap survives format control."*

## Reviewer #2 附加的义务

原文照引 `stage4_reviewer2_cheap5.jsonl`：

> `Needs format-controlled eval + representation probe + small text-only DPO control`

三个条件。前两个是卡片 E1；第三个是卡片 E4，而没有它，
`proposal.md` §23 禁止对对齐目标做任何因果性主张。

## Windows6 中被并行工作抢先的风险最高 —— 排期前必读

三处独立记录一致指向这一点：Stage-3 的保留信心为 **0.55**（Final 3 中
最低，备注写着 *"matched checkpoint localization tax still open"*）、
`literature.md` 中的一处 **EVIDENCE GAP，信心约 0.5**，以及 `Windows6/README.md`
自己写的 *"highest concurrent-work risk"*。

它的新颖性是**由一处空缺定义的**，而实验又便宜、只做评测、不需要新数据、
用的是公开 checkpoint —— 所有让它对我们有吸引力的性质，同样让它对
所有其他人都有吸引力。

**对排期的后果：** 尽管 Idea_01 在可行性上被排为 *"#1 start here"*，
GATE-B 与 E1 也**不应**排在 Idea_01 之后。它们只花几个小时，而它们的
价值会随时间衰减。详见 `proposal.md` §26.1。

## Package 地图

| 文件 | 内容 |
|---|---|
| [`proposal.md`](proposal.md) | 28 节：假设、那个 2×2、GATE-B、指标、kill 条件、并行工作分析、决策树 |
| [`experiments.md`](experiments.md) | 卡片 E-B、E0–E4，含阈值与分叉 |
| [`reviewer_attacks.md`](reviewer_attacks.md) | Stage-4 的攻击 + 红队，含只被*部分*缓解的那两条 |
| [`roadmap.md`](roadmap.md) | 各阶段；以及为什么在这里速度比算力更重要 |
| [`literature.md`](literature.md) | 只收已核实的条目；MDGD 被作为一条攻击引用 |
| [`diagrams/system.md`](diagrams/system.md) | 流水线图 |
| [`configs/`](configs/) | `default.yaml`（合成）与 `e1_killer.yaml`（真实协议） |
| [`src/aligntax/`](src/aligntax/) | 框、三种解码模式、探针、指标、O1/O2/O3 决策函数 |
| [`tests/test_smoke.py`](tests/test_smoke.py) | 27 项自检，只依赖 numpy |

## 代码有意拒绝去做的事

`data.verify_checkpoint_pair` 会抛出 `NotImplementedError`，并逐条写明
GATE-B 的三项检查，因此代码不可能在未核实的 checkpoint 对上意外继续往下跑。
缺少似然模式时 `classify_outcome` 会抛异常。`Config` 会拒绝未知键和
非法的 `tax_mode` 取值。沉默正是那种把 EXPECTED 变成 ACTUAL 的失败模式。
