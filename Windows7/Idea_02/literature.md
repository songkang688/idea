# Idea_02 — 相关文献（Literature）

**溯源标签。** `[S5-verified]` = 经 Stage-5 工程师于 2026-08-28 检索验证存在。`[S6-verified]` = 在 Stage-6 对抗性/答辩审查中发现或重新核实。`[S6-abstract]` = 仅阅读摘要。`[inherited]` = 继承自 Stage 3/4，未重新核实。

> 这是 Windows7 中最拥挤的赛道。诚实的现状总结：**没有致命的抢发，存在两个快速流逝的时间钟，且已有团队在展开立意阵地抢占。**

---

## 1. Memory 策略浪潮 — 我们的对照方法，而非直接竞争对手

`EVIDENCE` 据 `arXiv:2512.22624` 与 `arXiv:2606.24449` `[S6-verified]` 记载，至少有 6 篇已发表方法指出 FIFO 或基于置信度的 memory 写入会导致 SAM2 中的误差累积：

| 方法 | 代码仓库 | 在本研究中的角色 |
|---|---|---|
| SAMURAI | `github.com/yangchris11/samurai` `[S5-verified]` | 对照方法（运动感知 memory 选择，免训练） |
| DAM4SAM | `github.com/jovanavidenovic/DAM4SAM` `[S5-verified]` | 对照方法 + **DiDi 数据集来源** |
| SAM2Long | `github.com/Mark12Ding/SAM2Long` `[S5-verified]` | 对照方法（免训练 memory 树） |
| SAMITE | 经由 `arXiv:2512.22624` `[S6-verified]` | 候选对照方法 |
| HiM2SAM | 经由 `arXiv:2512.22624` `[S6-verified]` | 候选对照方法 |
| SENTRY | `arXiv:2606.24449` `[S6-verified]` | 候选对照方法 |
| AS-SAM2 | TCSVT 2026，承诺开源代码 `[S6-verified]` | 候选对照方法，取决于其是否开源 |

**为什么这份清单是一笔资产。** Stage 5 围绕两个对照方法设计了有效性测试。有了五到六个对照方法，"可逆比例预测预防收益"不再是关于两个 wrapper 的偶然现象，而是升华为关于该机制大类的普遍结论 —— *前提*是对照集合在运行任何对照方法前已完成冻结，且报告的统计量是最小值而非最大值。两项条件均已写入 `configs/preregistration.yaml`。

---

## 2. 立意阵地的抢占

| 工作 | 实际所做工作 | 与本研究的精确差异 |
|---|---|---|
| **`arXiv:2512.22624`** — *Rethinking Memory Design in SAM-Based Visual Object Tracking*, Dec 2025 `[S6-verified]` | 系统分析 SAM2 时代的 memory 机制；在 SAM3 内部进行复现；在十个基准上展开评测；提出统一的长短期混合 memory 架构；**开源公共 SAM3 跟踪 zoo**。 | 属于一项*设计研究（design study）*。未开展 oracle 手术，未做可逆性分解，未做外部有效性检验。但它占据了"系统性 memory 核心研究"的生态位，因此我们的立论文风必须坚持**分解优先（decomposition-first）**，而非泛泛宣称"我们研究 SAM2 memory"。 |
| **CL-MC** — `arXiv:2602.19380` `[S6-verified]` | 针对 SAM2 漂移的检测器触发式 memory 覆写 —— 属于重置（reset）家族的应用型*修复手段*。 | 使 P2 检验（`targeted > reset`）具备承重意义而非装饰性：既然已存在可引用的重置型修复手段，该差距就必须被严谨测量。 |

`EVIDENCE` Stage 6 的全部四位专家一致认同 `arXiv:2512.22624` 尚未开展 oracle 手术或可逆性分解。他们在该论文的存在究竟有多大影响上存在分歧 —— 在 `reviewer_attacks.md` 中如实记录为未解决的分歧，不做强行结论。

---

## 3. 该领域在论文中公开发出的疑问

两处文献引用对引言动机章节的支撑力度超越了我们能构建的任何论辩：

1. `EVIDENCE` `arXiv:2512.22624` 明确指出该子领域**"受制于 memory 设计的瓶颈（bottlenecked by memory design）"** `[S6-verified]`。
2. `EVIDENCE` **SAM2RL**（`arXiv:2507.08548`）`[S6-verified]` 针对单个视频过拟合强化学习 memory 策略，报告其**相比 SAM2 实现了 +4.91% 的跟踪质量提升** —— 在其评测环境下击败了 SAMURAI 和 DAM4SAM —— 并随后观察到即使是过拟合策略*"依然无法达到最优性能，这暗示了 memory bank 容量的理论极限。"*

一个发表了八种策略却随后在论文中公开承认不知道极限在哪里的领域，是一个缺少分母的领域。

**SAM2RL 也是我们最佳的隐藏上行机会。** 其理论上限是通过*优化*推导出的；而我们的理论上限是通过 *oracle 计时*推导出的。若两种独立推导出的理论上限相互吻合，将比 Stage 4 所用的立意辩解更有力地化解对 oracle 依赖性的质疑（A6），且边际成本仅为一个开源代码仓库加一份共享序列列表。

---

## 4. SAM3 与代际演进问题

`EVIDENCE` SAM3 于 2025 年 11 月发布（`arXiv:2511.16719`）；SAM 3.1 于 2026 年 3 月发布 `[S6-verified]`。SAM3 跟踪器**继承了 SAM2 的 memory bank 架构**，且报告称其 memory 策略更为保守。

这既是最大的威胁（A3：在 2026 年投稿时，仅针对 SAM2.1 的论文显得像过时的考古），也是最大的机遇。在 SAM2.1 **和** SAM3 上执行完全相同的协议，将交付物从"SAM2 有这么多源于 memory 的失败"升级为*"模型代际演进实际消除了多少源于 memory 的失败，又有多少未能消除。"* 这一成果量级显著提升，且 `arXiv:2512.22624` 开源的 zoo 降低了对照方法的适配成本。该实验已作为 E7 获得算力资助，而非推迟至未来工作。

---

## 5. 数据集与工具

| 资源 | 承担角色 | 备注 |
|---|---|---|
| `github.com/facebookresearch/sam2` `[S5-verified]` | 研究主体；video predictor + memory bank | 用于挂载手术 hooks 的 fork 代码 |
| LVOS v2 — `github.com/LingyiHongfd/LVOS` `[S5-verified]` | 主要采集来源，140 个 val 视频 | 密集 GT，长周期视频 |
| `lvos-evaluation` `[S5-verified]` | J&F 评分工具 | |
| **DiDi** — `go.vicos.si/didi`, 链接自 DAM4SAM `[S5-verified]` | 干扰物提纯采集来源 | **无镜像 —— 首日必须确认访问权限** |
| SA-V val | 若产出量不足时的备选扩展数据源 | |
| SAM3 tracking zoo (经由 `arXiv:2512.22624`) `[S6-verified]` | E7 代际实验臂 | HF 门禁审批 |

---

## 6. 评审员可能引用的文献及对应回应位置

| 可能的引用文献 | 攻击角度 | 回应方案与位置 |
|---|---|---|
| `arXiv:2512.22624` | "SAM 跟踪器的 memory 设计已被系统性研究过。" | 坚持分解优先的立论；既有工作均未开展带有可逆性拆分与外部有效性检验的 oracle 手术。`reviewer_attacks.md` A3。 |
| CL-MC (`arXiv:2602.19380`) | "Memory 重置早已是已发表的修复方案。" | P2 精确测量该差距，预注册要求达到 ≥10 分优势且置信区间排除 0。 |
| SAM3 / `arXiv:2511.16719` | "你们研究的是上一代模型。" | E7 SAM3 实验臂已获得算力资助。 |
| SAM2RL (`arXiv:2507.08548`) | "理论上界已经存在。" | 基于不同原理（优化算法 vs oracle 计时）。两者一致构成相互印证，我们将执行交叉验证。 |
| 持续学习领域的评审员 | "删除近期状态是数十年前的启发式方法。" | 该方法对应 `reset` 实验臂，击败它是预注册的硬性要求。 |

---

## 7. 待结清的验证债务

1. SAMITE、HiM2SAM 和 AS-SAM2 是**通过** `arXiv:2512.22624` 与 `arXiv:2606.24449` 为我们所知。在将其中任何一项列入冻结对照集之前，必须直接核验原始文献与代码开源状态 —— 无法运行的对照方法比从未命名的对照方法危害更大。
2. `arXiv:2606.24449`（SENTRY）与 `arXiv:2602.19380`（CL-MC）仅在**摘要层面**进行了阅读。
3. SAM2RL 的 "+4.91%" 数据属于该团队在自设环境下的 `EVIDENCE`。它用于支撑研究动机；不能直接作为基准数字复用。
4. `KNOWN FACT` **本方案包中的任何跟踪指标数字均非由我们亲自测得。**
