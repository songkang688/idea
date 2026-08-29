# 演化总结（Windows1）

## 流程

由自主 PI 带领最多 3 个云端子 agent（`claude-fable-5-thinking-xhigh`）运行。两次 Stage-1 350 条想法的云端运行**超时**；supervisor 在本地撰写了 VFM/ASM 池并重新派发了 180 条想法的批次。Stage-2 评审员最初受阻（云端工作区缺少想法文本），随后载入完整的 SEG 清单得以恢复。

## 生成 → 变异 → 击杀亮点

- **按原样击杀：** 二值烟雾作为新颖性；水印可学习性；LogME 式稠密探针；无标签 mIoU 预测作为产品化方案；最坏情况有效 SAM 点击（TETRIS）；oracle 点击 vs 人类（RClicks）；LoRA SVD 截断（PARA）；ViT 高范数 token（registers）；复制尖峰虚高曲线；印刷掩码注入作为主打想法；冻结/微调描述性曲线；线性 CLIP→DINOv2 作为主打（柏拉图表征假说 / CLIP-DINOiser）。
- **变异并保留：** 约束 SAM 微调必须胜过 WiSE-FT；病灶抑制放弃"普适"主张；分歧场使用对次序敏感的指标而非 ECE 评测。
- **曾受保护但在 Stage 6 被裁减：** SEG-0276-M 形状先验 α（Reviewer #2 喜欢它；在评测席位竞争中输给了医学影响力）；SEG-0252 标签生态学（存在廉价的 ρ_H·ρ_M 设计；存在外部效度循环性）；0046-M 透射率（抠图 / SMOKE5K AAAI 2022）。
- **元审计（Meta-audit）：** 投资组合曾过度偏向评测科学；医学／物理想法因邻近性被过度击杀。Final 3 恢复为一个方法 + 两个医学。

## 孕育了 Final 3 的簇

- SAM / PEFT / 遗忘 / 双重目标（VFM-0263/0274，Stage-5 #1）
- 增强管线的医学安全性（SEG-0085-M）
- 跨偏移的多标注者不确定性（SEG-0074-M；最初的浸润-vs-病理形态被 RAPSODI/ProsRegNet/校准类论文 KILL 掉）

---

## 附录 —— 2026-08-29 选题历史事后回填（retrospective）

此线之上的所有内容均为原始 Windows1 记录，**未作修改**。本附录是在
Final 3 锁定、打包并合并至 `main` 之后追加的。它**不重新打开任何选题决策**，
也不改变 `Windows1/README.md` 或 `Windows1/research_summary.md` 中的任何结论。

### 为什么需要它

属于*记录*层面的两处缺陷，而非交付物缺陷。首先，按阶段的漏斗文件从未位于
`Windows1/` 目录下 —— 它们是仓库根目录 `research_ledger/` 中的 12 个文件，因此从
`Windows1/` 开始阅读的读者无法对任何阶段进行审计。其次，Stage 6 完全没有落成文字：
产生 Final 3 的 5 → 3 裁决没有留下原始记录，尽管此前每个阶段都保留了击杀清单。

### 添加到本目录的文件

| 文件 | 目的 |
|---|---|
| `LEDGER_INDEX.md` | 针对根目录 12 个 `research_ledger/` 文件的归属与位置索引：各自涵盖哪个阶段、属于 Windows1 的证据、以及为何保留在根目录。 |
| `FUNNEL_DEVIATION.md` | 标准链路（1000+ → 200 → 50 → 20 → 5 → 3）与 Windows1 实际运行路径（1065 → 约 84 → 约 20 → 12 → 8 → 5 → 3）的逐级对比，含来源与差异列表。 |
| `stage3_survivors.md` | Stage-3 存活者名单，由两份击杀清单反推得出（20 SEG + 13 VFM 决策单元 → 24 存活者）。 |
| `stage4_candidates.md` | 全部 12 个 Stage-4 提案，以及**已找回的** Reviewer #2 评审组记录。 |
| `stage5_top5.md` | 记录在案的 Top-8、工程师的 Top-5、supervisor 的修正，以及调和后的候选集合。 |
| `stage6_battle.md` | 事后 5 → 3 记录：三位胜出者及其约束性义务和 death 条件、亚军的复活条件，以及记录在案的冲突。 |

### Stage 4 评审组：已找回

完整的 Reviewer #2 评审组记录已被找到并建立索引。`research_ledger/stage4_reviewer2.md` 声称
该评审组位于分支 `cursor/reviewer2-stage4-kill-panel-5733` "（云端工作树，**非本仓库**）" ——
**该括号内的陈述是错误的。** 该分支就在本仓库中，且该评审组记录
（`research_ledger/stage4_reviewer2_kill_panel.md`，21,207 字节，标题为 "Stage 4 — Reviewer #2 Kill
Panel (Windows1 PI)"）已从中找回：包含 12 个提案 P1–P12，每个均附带拒稿理由、隐含假设、
混淆因素、缺失基线、平凡替代方案、封嘴实验以及裁决。其 Top-7 与 `stage4_reviewer2.md` 中的总结行完全吻合。

三个兄弟分支 `cursor/stage4-cluster-{a,b,c}-reviewer2-*` 亦经过检查，**不属于** Windows1：
它们以 "Supervisor Windows7" 为抬头，使用与 Windows1 不相交的 `A-`/`B-`/`C-` ID 命名空间，
涵盖无关的主题。它们之所以携带 `Windows1/` 与 `research_ledger/`，仅仅是因为它们是从已经合并了 Windows1 的提交切出的。

### 确认无法找回的内容

- **Stage-6 会议记录。** 未留存任何逐字稿、投票或逐候选人打分。`stage6_battle.md`
  明确标为事后补记，且依据 `README.md`、`reviewer_summary.md`、本文件、
  `meta_audit.md`、`stage4_reviewer2.md`、`stage5_0276.md` 以及 `cheap_killers_0252_0046.md` 构建。
  三处独立证据（包括上方 `reviewer_summary.md` 中记录的三项分歧）证实 Stage 6 确实*发生过*。
- **究竟哪五个候选进入了 Stage 6。** 四个是确定的（Constrained SAM-FT, 0085-M, 0074-M,
  0276-M），0252 几乎确定，但工程师的 Top-5 与 `stage5_killers.md` 中的"可能进入 final-3 的池子"
  是两份不同的 5 项清单，两者都无法作为实际执行的那份。
- **VFM/ASM 池未进行 Stage-2 评审。** 上文提到的 Stage-2 阻塞仅针对 SEG 清单得到了解决；
  `stage2_seg_review.md` 结尾写道 "Global 1000 not yet complete: waiting VFM + ASM pools"，
  且从未写出该清单。一项后果是：Idea_01 的祖先（VFM-0263/0274）在 Stage 3 进入时没有经过 Stage-2 打分。
- **五个 Stage-1 池中三个的完整想法文本。** SEG-0001…0365、VFM-A 180 与 ASM-A 180 仅以
  精简摘要形式存在。`eliminated_ideas_summary.md` 中引用的 `/workspace/research_ledger/` 路径
  曾是一个云端工作树；只有两个本地 350 想法池被提交了。
- **在 Stage 4 之前消失的十个 Stage-3 存活者**（SEG-0019, 0054, 0031, 0122; A0051, A0028,
  A0166, A0073, A0021, A0109），均标为 `NO RECORDED REASON — 需人工确认`。
- **字母代号 "C"。** Final 3 被标为 A/B/D；整个归档中任何地方都没有出现 "C"。

### 提交人工裁决的问题（此处不作修正）

- `reviewer_summary.md` 中的 Stage-2 各组计数（31/8/14/4）与 `research_ledger/stage2_seg_review.md`
  中的 ID 列表（23/6/15/4，相加等于其自身 "Named-48" 表头）不符。仅 KILL 计数一致。
- `stage3_vfm_kills.md` 写着 `A0263`，但 A 命名空间仅容纳 180 条想法；其实际指代为 `VFM-0263`。
- `0274` 存在歧义：`SEG-0274` 在 Stage 2 被 KILL，而 `VFM-0274` 是 Idea_01 的祖先。

### 遵守的约束

`research_ledger/` **未被**修改、移动或重命名 —— 全部 12 个 blob 哈希值保持不变，将其保留在根目录的
理由见 `LEDGER_INDEX.md` §4。`Windows1/Idea_01|02|03/` 下的任何文件均未被触碰，包括三个 52 字节的
`proposal.md` 指针（它们是指向各 package `README.md` 的有意指针，而非残缺存根）。`Windows1/README.md`
与 `Windows1/research_summary.md` 保持不变。全文使用 `README.md` 中的认知标签（KNOWN FACT /
EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT）；
**新文件中没有数字被标注为 ACTUAL EXPERIMENTAL RESULT**，因为本轮没有运行任何实验。`stage2_seg_review.md`
中的警示 —— "Scores are REVIEWER JUDGMENT not facts" 以及 "Do not treat Pub=L as verified novelty" ——
得到了遵守：回填记录了各项决策及其成文理由，而未将评审员的打分重申为科学发现。
