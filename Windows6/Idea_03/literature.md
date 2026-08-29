# Idea_03 —— 文献（只收已核实的条目）

**取材规则。** 这里的条目只有在它已经存在于本文件的原始版本中或
`selection_history/literature_anchors.md` 中时才可以出现在这里 —— 即只有当
某个 Stage-3/4 agent 真的做过网页检索时才收。没有任何一条是凭记忆添加的。
凡论证需要某个引用、而它无法与那些来源核对上的地方，该位置写的是
`CITATION NEEDED — 待人工核验`，而不是一个猜出来的引用。

---

## A. 核心 —— 把这些当作攻击点来引，而不是当作背景

| 论文 | 年份 | 会议／ID | 关系 |
|---|---|---|---|
| **MDGD** | 2025 | EMNLP Findings | 指令微调下的视觉遗忘。**正是这篇论文在 Stage 3 杀掉了我们的通用标题。** 它必须被明确且尽早引用："MDGD 确立了该现象；我们追问是哪个阶段付出的代价，以及 backbone 是否仍然包含框。" 仅仅在相关工作中提一句会被读成无知 |
| **TWIST & SCOUT** | 2025 | ICCV | 接地（grounding） / 无遗忘微调。提出了一种**修复方案**。一个有效的修复方案并不能告诉你到底是哪个阶段付出的代价，这正是我们要填补的空缺 |
| RL-finetuned VLM robustness | 2026 | arXiv 2602.12506 | 邻近且**最近**。动笔前必须立即重新核对是否被抢先 —— 足够新，以至于 v2 版本就可能包含这一结果 |
| LLaVA / LLaVA-RLHF 系列 | 2023–24 | — | **在许可允许条件下的**候选 checkpoint 对。使用前须经 GATE-B 核实 |

## B. 空缺，以及支持它的证据有多强

**FACT，原样照引自原始文件：**

> Stage 3: stage-isolated localization curve was **NOT FOUND** as a standalone
> paper (EVIDENCE GAP, conf ~0.5).

**这是一项由"空缺"定义的新颖性主张，文件应该直说。**
证据是一次检索没有找到这篇论文 —— **信心约 0.5**，Windows6 Final 3 中
最低的 —— 而不是说这篇论文不可能存在。`stage3_DE_top10.json.md` 独立记录了
E-009 为 **0.55**，并附备注 *"matched checkpoint localization tax still open"*，
而 `Windows6/README.md` 把 Idea_03 标为 *"highest concurrent-work risk"*。

空缺会在没有任何人做错任何事的情况下被填上。`proposal.md` §26.1 将其视为
排期约束，而不是一句免责声明。

## C. 投稿前需要人工核验的位置

| 用在何处 | 位置 |
|---|---|
| Qwen-VL / Qwen-VL-Chat（实验计划中点名的候选对） | `CITATION NEEDED — 待人工核验` |
| RefCOCO / 指代表达基准 | `CITATION NEEDED — 待人工核验` |
| DPO（H3 工具，卡片 E4） | `CITATION NEEDED — 待人工核验` |
| LoRA | `CITATION NEEDED — 待人工核验` |
| 语法受限解码（评测模式 2） | `CITATION NEEDED — 待人工核验` |
| 冻结表征的线性探针（H2 工具） | `CITATION NEEDED — 待人工核验` |
| 语言模型中的对齐税（一般现象） | `CITATION NEEDED — 待人工核验` |
| VLM 的 RLHF / 指令微调，作为一般参考 | `CITATION NEEDED — 待人工核验` |

最后两条最重要：这篇论文主张的是*定位特异性*的对齐税，评审会期望把它置于
通用的对齐税文献中。填上那些空缺是投稿的阻塞项，不是可有可无的修饰。
它们被有意留空 —— 一个凭记忆重建、看起来合理的 bibtex 条目比一个看得见的
空洞更糟，因为空洞会被去核查。

## D. 核心引用在论证中的用法

- **MDGD** 出现在摘要、§8 新颖性、§9 差异化以及 `reviewer_attacks.md` A1 中。
  它是本 package 中最承重的单一引用，而且是对我们*不利*方向承重的。
- **TWIST & SCOUT** 被引用来划清"诊断 vs 修复"的界线。绝不能把它描述为
  "相关接地工作"；它是证明社区已经认为这项代价值得花工程去规避的最强证据。
- **arXiv 2602.12506** 作为邻近工作被引用，并在动笔前重新核对。
- **LLaVA / LLaVA-RLHF** 仅作为 checkpoint 对候选被引用，并始终附带 GATE-B
  限定条件。

## E. 有意不引用的工作

一般的 VLM 能力基准与排行榜论文。这是一项关于测得的代价*源自何处*的诊断，
不是关于模型质量的主张，列出一堆基准会暗示 `proposal.md` §23 已排除的横向对比主张。
同样，提出新接地架构的论文也属于范围之外：研究对象是一套测量协议，不是一种方法。
