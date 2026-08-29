# Stage 5 → Top-5（Windows1）—— 重建，且记录未明确指明最终五个

状态：**事后重建。**

`Windows1/research_summary.md` 将 Stage 5 描述为 "**8 engineered, then 5**"。其中的 8 在总账中有明确枚举并在下方精确复现。**但其中的 5 没有。** 本归档中没有任何文件指明哪五个候选进入了 Stage 6。

因此本文件执行两项独立的工作，并保持界限清晰：

- §1–§3 记录*确实*被写下来的内容：Top-8、工程师的 Top-5、supervisor 的修正，以及廉价 killer 设计。
- §4 将其调和为面向 Stage 6 的候选集，并**将记录未锁定的每一行标记为 `AMBIGUOUS — 需人工确认`**，而非擅自挑出五个作为既成事实。

来源：`research_ledger/meta_audit.md`、`research_ledger/stage5_killers.md`、
`research_ledger/stage5_0276.md`、`research_ledger/cheap_killers_0252_0046.md`、
`Windows1/selection_history/eliminated_ideas_summary.md`、
`Windows1/selection_history/reviewer_summary.md`、`Windows1/selection_history/evolution_summary.md`。

认知标签依据 `Windows1/README.md`。下方所有成本与门禁皆为 HYPOTHESIS 或设计规范。
**本轮中不存在 ACTUAL EXPERIMENTAL RESULT** —— `research_summary.md`："We have **not** trained models or measured Dice/mIoU/τ in this round."。

---

## 1. 那 8 个 —— 来自 `meta_audit.md` 的 "Updated working Top-8"

完全按原样的成员构成与顺序，附带该文件自身的表头警示 "(not final 3)"。

| # | 候选者 | 出处 | 是否推进通过 Stage 5？ |
|---|---|---|---|
| 1 | 约束 SAM-FT 双重目标（方法） | VFM-0263/0274，评审组 P12 | **是 → Idea_01 RetainSAM** |
| 2 | 冻结／微调交叉定律（Frozen/tuned crossover law） | A0121，Stage-3 MUTATE；从未进入 R2 评审组 | **否** —— 被裁减，原因有记录 |
| 3 | 0046-M 针对透明类别的透射率 vs 二值化 | Stage-3 KILL，被本次审计复活 | **否** —— 被裁减，原因有记录 |
| 4 | 0085-M 病灶抑制定律 | 评审组 P8 | **是 → Idea_02 LesionSuppress** |
| 5 | 0074-M 观察者间校准迁移 vs 精度迁移 | Stage-3 KILL，被本次审计作为收敛变异复活 | **是 → Idea_03 DisagreeShift** |
| 6 | 0252 标签生态学 + 干预 | 评审组 P1，被 R2 廉价 killer 规则淘汰，被本次审计恢复 | **否** —— Stage-6 被裁减 |
| 7 | 最坏情况／oracle 点击交互式评测合并 | A0022 + A0168，皆为 Stage-3 KILL，被本次审计合并 | **否** —— Stage-6 被裁减 |
| 8 | 0275 + 评测污染合并（一个评测席位） | 评审组 P3 + 对被击杀 P10 的抢救 | **否** —— 被裁减 |

同一文件中附加的一条长期指令："**Protect 0276 shape-prior law and 0240 context sampling as benches.**"。注意这里*保护了* 0276 但未给其 Top-8 席位 —— §3 表明该疏漏随后必须被更正。

### 为什么 Top-8 与 R2 Top-7 大相径庭

`meta_audit.md` 是对*投资组合*的审计，而非对提案的重新评审，它有意推翻了之前的若干裁决。记录在案的裁定：

- **ACCEPTS**："评测过度索引；0285 从 SURVIVE 中裁减；将 0275 与污染合并；将最坏情况点击与 oracle 点击泄漏合并；将 0046 作为透射率 vs 二值假设复活（非'立论论文'）；将 0074 仅作为分歧场的跨染色校准复活（Stage3 杀掉了原始病理概率图）；0113 仅作为空间误差结构预测复活。"
- **REJECTS**："将 0074 原始版本视为被错误击杀 —— 原始形态**确实**已被发表（RAPSODI/校准）。**仅变异形态存活。**"
- **PARTIAL**："约束 SAM-FT 双重目标具有方法形态，但**可能缺乏新颖性**；需要 VFM 保留项的 Stage3。"

因此八个中有三个属于 Stage-3 击杀项的*复活*（0046-M, 0074-M，以及 A0022+A0168 合并），且八个中包含最终的 #1 推荐（带着明确的新颖性疑虑）。与 Reviewer #2 的清单间冲突逐项列于 `stage4_candidates.md` §5b。

---

## 2. 工程师的 Top-5 —— `stage5_killers.md`

原文："Engineer Top-5: (1) Constrained SAM-FT (2) Frozen/tuned n\* (3) 0085-M lesion suppression (4) 0074-M calibration-under-shift (5) Interactive eval merge."

被工程师裁减的项及其成文理由："0046-M (**真值稀缺**), 0252 (**模拟中软击杀**), 0275 contamination (**工程化／混淆因素**)."

因此工程师通过裁减 #3、#6 和 #8 将 Top-8 压缩为五个 —— 且由于他依据的是 Top-8，他完全没有审视过 SEG-0276-M。

---

## 3. Supervisor 修正 —— 0276-M 发生遗漏

引自 `stage5_killers.md` 原文："**SUPERVISOR CORRECTION: 0276-M shape-prior field was omitted from this Stage-5 prompt** (R2 ranked it #1, inference-only killer). **Must add back before locking Top-5.**"

随后该文件给出了一个包含五项的 "Likely final-3 pool"，那**不是**工程师的 Top-5：

1. Constrained SAM-FT
2. 0085-M lesion suppression
3. 0276-M prior-shape interpolation (待设计)
4. 0252 若存在廉价 killer
5. 仅当不属于归档 package 的"纯基准论文"时的交互式评测

**KNOWN FACT —— 这两份五项清单存在冲突。** 工程师的 Top-5 包含 `Frozen/tuned n*` 与 `0074-M`，遗漏了 `0276-M` 与 `0252`；"likely final-3 pool" 遗漏了 `Frozen/tuned n*` 与 `0074-M`，包含了 `0276-M` 与 `0252`。由于 `0074-M` 最终成为了 **Idea_03**，"likely final-3 pool" 同样无法作为实际生效的 Stage-5 五项清单。两份清单均非那最终五个。这是 Stage-5 集合无法找回的核心原因，记录于 `FUNNEL_DEVIATION.md` §4-E。

---

## 4. 调和后的 Stage-6 候选集

依据成文产物，最能站得住脚的读法是：进入 Stage 6 实际裁决的五个候选为 **Constrained SAM-FT (Idea_01)、0085-M (Idea_02)、0074-M (Idea_03)、0276-M（亚军）以及 0252**。由于没有任何单一文件确凿证实该集合，所有未被各 Idea package 锁定的条目均标为 `AMBIGUOUS — 需人工确认`。
