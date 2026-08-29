# Idea_02 — MemorySurgeon

**基于因果 memory 手术的 SAM2 经检验分解工具（Causal memory surgery as a validated decomposition instrument for SAM2）。**
内部 ID `A-0017` · Windows7 · **本轮上限最高、单一风险也最高的选题。**

> 八种 memory 策略竞相修复 SAM2 的跟踪失败。但没有一种策略能够说明究竟有多少问题是归因于 memory 从而可以被修复的。本研究提供了这个分母。

## 一段话概述

当 SAM2 在长视频中丢失目标时，删除在失败发生后写入的 memory 条目，从真实标注（ground-truth）的恢复时机点重新回放（replay），并测量该失败在多大程度上是*源于 memory* 而非源于表征能力的。三项预注册的对照实验将该操作从单纯的修复启发式转化为一套因果分解工具：它必须击败完全重置（full reset），必须击败无效的 sham 手术，并且序列级的可逆比例必须在**控制通用序列难度（generic sequence difficulty）的偏相关分析后**，仍能预测独立预防性方法的收益。

**并且如果它能存活，就必须将方法封装交付。** `KNOWN FACT` Stage-6 元评审将方法臂定为**必须交付项（required deliverable）**：若定向删除（targeted deletion）以预注册的 ≥10 分优势击败完全重置，论文必须将该手术封装为免训练的 SAM2 wrapper，并与 SAMURAI 和 DAM4SAM 进行正面对决基准测试（E9，~40 GPU-h，以 P2 为触发条件）。这是 Windows7 中唯一能在单一预算内从测量毕业为方法的项目 —— 而唯一诚实的难点在于，测量过程是**依托 oracle 计时**的，而实用的 wrapper 无法依赖 oracle，因此 E9 需要一个失败触发器，其实际收益必然严格低于所测得的理论上限。

## 文件结构

| 文件 | 内容说明 |
|---|---|
| `proposal.md` | 完整的 28 节研究方案包。从这里开始阅读。 |
| `literature.md` | 拥挤的 2025–2026 年 SAM-memory 赛道，以及我们与之的精确差异 |
| `experiments.md` | E0–E9 实验、各实验臂、消融实验、决策规则 |
| `reviewer_attacks.md` | A1–A6 攻击点与专家分歧 D1–D2，附带回应每项问题的实验方案 |
| `roadmap.md` | 第 1 天 → 第 4 周实施路线图 |
| `diagrams/architecture.md` | Mermaid 流程图：手术实验臂、决策流、有效性设计 |
| `src/` | 可运行原型：memory bank、六个实验臂、回放门禁、偏相关有效性检验 |
| `configs/preregistration.yaml` | 在任何实验运行前冻结 —— 包括对照方法集合 |
| `references/` | 访问权限核对清单、文献验证日志 |

## 立即运行原型

```bash
pip install -r requirements.txt
python src/run_pilot.py
```

无需 GPU，无需下载 checkpoint。它针对一个其失败归因在构造时已知的模拟器运行小规模试验（pilot）决策规则，这是验证决策规则能否将真实效应与人为假象区分开来的唯一方法。

### 原型运行展示的内容

展示了两种情景，其中第二种尤为关键。

**情景 A — 源于 memory 的失败真实存在。**

```
H2-testable failures (pre-error memory survived FIFO): 23/50
recovery rate by arm: no_op=0.08 targeted=0.52 reset=0.48 sham=0.04 slot_control=0.54
targeted-no_op          +0.440  [+0.280, +0.580]   P1 PASS
targeted-sham           +0.480  [+0.340, +0.620]   P3 PASS
targeted-reset (all)    +0.040  [-0.160, +0.240]   <-- diluted, NOT the test
targeted-reset (H2 set) +0.130  [-0.130, +0.391]   <-- P2 is read here, PASS
VERDICT: decomposition survives all three arms at pilot scale.
```

**情景 B — 完全不存在源于 memory 的失败；跟踪器仅仅是在 memory bank 更空时表现更好。**

```
recovery rate by arm: no_op=0.58 targeted=0.94 reset=1.00 sham=0.64 slot_control=0.70
targeted-no_op          +0.360  [+0.200, +0.500]   P1 PASS   <-- the naive test is fooled
targeted-sham           +0.300  [+0.140, +0.460]   P3 PASS   <-- and so is this control
targeted-reset (H2 set) -0.130  [-0.304, +0.000]   P2 FAIL   <-- only P2 fires
slot_control-targeted   -0.240  [-0.380, -0.100]
VERDICT: targeted is no better than a restart. Publishable as a bounded diagnostic
post-mortem, not as a decomposition.
```

情景 B 正是对照实验臂存在的全部意义。如果设计仅仅测试"定向删除是否优于什么都不做"，就会报告出 +0.360 的虚假效应并将其称为因果分解 —— 并且请注意**此时 P3 也会通过**。唯有 P2 能捕获这一特定假象。这两个对照臂是互补的，单独任何一个都无法满足需求。

**预测有效性（Predictive validity），在混淆因素按设计显式注入的数据上：**

```
comparator     naive r   partial r
SAMURAI          0.952       0.682
DAM4SAM          0.918       0.397
SAM2Long         0.859       0.028
min partial r = 0.028 (threshold 0.4) -> FAIL
```

这就是评审员攻击 A1 的具体体现。接近 0.9 的原始相关系数看起来像是压倒性的有效性验证；但在偏相关分析剔除 no-op 恢复率、失败次数和干扰物密度后，某一个对照方法的相关性骤降至 0.03。预注册的统计量是**在任何对照方法运行前预先冻结的对照集上的最小值**，因此单个强对照方法无法单独支撑头条结论。

**上述所有数字均来自模拟数据。** 其目的在于验证决策规则，而非评估 SAM2 本身。

## 通过构建原型发现的两处设计修正

1. **sham 臂的定义完全搞反了。** Stage 6 要求"删除错误发生后的条目，但重新插入数量匹配的错误发生前重复项"。字面实现该方案依然会移除被污染的内容 —— 从而执行了治疗性操作 —— 这导致"targeted 必须击败 sham"在构造上就是无法通过的。真正的 sham 手术应该只做切口而不移除任何治疗性内容。无效版本现定为 `sham`；Stage-6 的字面版本保留为 `slot_control`，用于回答不同的问题。参见 `proposal.md` §3。
2. **当失败持续时间超过 memory 容量上限时，`targeted` 与 `reset` 实质上是完全相同的操作。** 此时 FIFO 已经冲刷掉了所有错误发生前的条目，因此在这些失败上 H2 是无法检验的 —— 将它们合并计算并不会测量到一个较小的效应，而是会根据语料库的失败持续时间分布将**真实效应稀释趋近于零**。在原型中，50 次失败中仅有 23 次属于 H2 可检验样本，合并计算导致原本子集上真实的 +0.130 差距被稀释为 +0.040，从而在分解效应真实存在的世界中导致 P2 判定失败。**因此，P2 仅在 H2 可检验子集上进行判定**，真实数据采集必须在 E1 阶段、提出任何 P2 主张之前先行报告该子集占比。参见 `proposal.md` §3 与 §19。
3. **小规模试验（pilot）针对 P2 的检验效能特别不足。** 在 n = 23 时，情景 A 的 H2 子集差距为 +0.130，置信区间为 [-0.130, +0.391]。50 次失败的 pilot 门禁足以判定 P1 和 P3，但*不足以*判定 P2 —— 因此在 pilot 阶段 P2 未通过是扩大 H2 子集样本量的信号，而非终止项目的理由。唯有 P3 失败才会在 pilot 阶段直接终止项目。

## 首日要运行的第一个实验（Day 1）

**E0，回放确定性门禁（replay-determinism gate）。** `no-op` 臂必须逐 bit 精确复现原始失败；SAM2 的 video-predictor 缓存机制使这成为真实存在的风险而非走过场。若回放不具备确定性，所有实验臂之间的差异都部分混入了测试工具噪声，后续任何分析都将失去合理解释性。同在第 1 天需要完成：确认 DiDi 数据集的访问权限（`go.vicos.si/didi` —— 无镜像备份）。

## Killer 实验

收集 ≥200 次自然发生的失败。`targeted` 必须击败 `no_op` 达到 ≥30 分优势，击败 `reset` 达到 ≥10 分优势，击败 `sham` 达到 ≥10 分优势；且满足 `min_{c ∈ frozen} partial r > 0.4`。任何一项未达标均会证伪工具主张。耗时约 ~60 GPU-h。
通过 reset 裕度检验还将**触发强制性方法臂**（E9）。

## 算力预算

核心实验约 ~80–120 GPU-h · 加上 Stage-6 强制实验臂约 ~140–180 · 加上 E9 约 ~180–220。全程零训练需求，单卡 A100-40GB。E9 仅在项目已取得成功的实验分支上运行。

## 最大风险

**被同行抢发的时间钟（scoop clock）。** `EVIDENCE` SAM-memory 子领域在两年内发表了至少 6 种 memory 策略，并在 2025 年 12 月发表了一项带有 SAM3 zoo 的系统性 memory 设计研究。这是 Windows7 中新颖性衰减最快的课题，若只能启动一个项目应优先安排其启动。

## 状态

设计已完成，原型可正常运行，决策规则已对照已知假象情景完成验证。尚未针对真实 SAM2 运行。
