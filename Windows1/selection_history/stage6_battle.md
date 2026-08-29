# Stage 6 —— 最终对抗（battle），5 → 3（Windows1）

## 这是一份事后重建记录（RETROSPECTIVE RECONSTRUCTION）

**Stage 6 发生时未留下即时记录。** 本文件撰写于 Final 3 已锁定、打包并合并至 `main` *之后*。它是从留存文档汇编而成，而非现场会议的逐字稿。

**KNOWN FACT —— Stage 6 确实发生过。** 三处独立证据：

1. `Windows1/README.md`："**Stage 6 locked** method + medical-safety characterization + medical uncertainty method."
2. `Windows1/research_summary.md` 漏斗表："Stage 6 \| **Final 3** \| A RetainSAM, B LesionSuppress, D DisagreeShift."
3. `Windows1/selection_history/reviewer_summary.md` 记录了三项点名的 Stage-6 分歧，若无 Stage-6 环节这些分歧不可能存在。

**KNOWN FACT —— 不存在 Stage-6 原始记录。** `research_ledger/` 中不包含 `stage6_*` 文件，在本次回填之前 `Windows1/selection_history/` 中亦不存在。Stage 1–5 的每份击杀表都保留了；5 → 3 的裁决却没有。

**本文件的性质。** *结果*（哪三个胜出，以及各自锁定的证伪条件）属于 KNOWN FACT，字面引自 `README.md` 与 `research_summary.md`。*论证推理*依据 `reviewer_summary.md`、`evolution_summary.md`、`eliminated_ideas_summary.md`、`research_ledger/meta_audit.md`、`research_ledger/stage4_reviewer2.md`、`research_ledger/stage5_0276.md` 以及 `research_ledger/cheap_killers_0252_0046.md` 重建。凡上述文档沉默之处，本文件如实说明而不填补空缺。

认知标签依据 `Windows1/README.md`：KNOWN FACT, EVIDENCE, HYPOTHESIS, MODEL SPECULATION,
EXPECTED RESULT, ACTUAL EXPERIMENTAL RESULT。

**此处没有任何内容属于 ACTUAL EXPERIMENTAL RESULT。** `research_summary.md`："We have **not** trained models or measured Dice/mIoU/τ in this round."。`README.md`："**No numbers in this archive are measured by us.**"。下方每个阈值、门禁与成本均为预先注册的 HYPOTHESIS 或 HYPOTHESIS 估计值。

**输入集合说明。** 记录未明确指明究竟哪五个候选进入了 Stage 6；见 `stage5_top5.md` §4。最能站得住脚的读法是 Constrained SAM-FT、0085-M、0074-M、0276-M 与 0252，而 0250 / Frozen-tuned n\* / 交互式评测合并项在锁定前夕或锁定时死亡。本文件对有据可查的胜出者与亚军进行裁决，不对落选对的成员构成作硬性断言。

---

## 1. 锁定的投资组合及其形态成因

**KNOWN FACT。** `README.md` 直接陈述了组合规则："Stage 6 locked **method + medical-safety characterization + medical uncertainty method**."。

| 候选代号 | 目录 | 名称 | 组合角色 |
|---|---|---|---|
| **A** | `Idea_01` | RetainSAM | **方法**论文 —— 且为 #1 推荐 |
| **B** | `Idea_02` | LesionSuppress | **医学安全表征研究** |
| **D** | `Idea_03` | DisagreeShift | **医学不确定性方法** |

`evolution_summary.md` 给出了该组合形态的原因："**Meta-audit:** portfolio was over-indexed on eval science; medical/physics ideas had been over-killed by adjacency. **Final 3 restores method + two medical.**"。见 §4b —— 这是一个深思熟虑的纠偏，而非个人偏好。

`reviewer_summary.md` 陈述了 supervisor 自己对锁定的总结："Supervisor locked A/B/D to keep **one method, one safety spec, one uncertainty method**, and because RetainSAM's kill test is the **cheapest portfolio de-risk**."。

**代号字母 C 下落不明。** 名单运行为 A, B, D，整个归档中无 C。`NO RECORDED REASON — 需人工确认`；亦记录于 `FUNNEL_DEVIATION.md` §4-F。

**关于整份名单的结构性事实（KNOWN FACT）。** `reviewer_summary.md`："Stage-4: **no idea earned unconditional KEEP**. All finalists are **KEEP-IF-EXPERIMENT**."。因此 Final 3 不是三个已被批准的项目；它们是三个附带预先注册死亡方式的条件性下注。这正是 §2 围绕 death 条件而非优势展开组织的原因。

---

## 2. 三位胜出者

每个条目给出锁定的理由、该想法必须履行的约束性义务，以及它死亡的条件。**所有三组条件均字面抄录自 `README.md`、`research_summary.md` 以及各 Idea 的 `README.md` 文件而非重新措辞**，因为这些是本轮锁定的承诺，意译会削弱其效力。

---

### 2a. Idea_01 —— RetainSAM（代号 A，#1 推荐）

世系谱系：`VFM-0263` + `VFM-0274` → Stage-3 MUTATE → 评审组 P12 → Stage-5 工程师 Top-5 #1。

**一句话假设**（来自 `README.md`）："在**可提示性保留约束**下在目标领域微调 SAM，并要求该方法在提示行为 Pareto 前沿上**严格支配 WiSE-FT 插值**。"

**锁定理由** —— `README.md` 原文："It is the only method-building project in the final three, it has the cheapest decisive falsifier (WiSE-FT must be beaten), and a failure still leaves a reusable promptability-retention benchmark."

**约束性义务。** 必须严格支配 WiSE-FT 插值前沿 —— 不能持平，不能平手。`research_summary.md` 锁定假设 1："A promptability-constrained SAM fine-tune **strictly dominates** the WiSE-FT interpolation Pareto on (target Dice, generic k-click mIoU). **Falsified if interpolation matches or beats it.**"。支配必须在 **≥ 2 个工作点** 上成立（`README.md` 步骤 5；`Idea_01/README.md` H1）。

**Death 条件（kill 开关）。** `README.md`："**Kill Idea_01** if constrained FT does not strictly dominate interpolation at **≥2 operating points**" —— 且依据推荐章节，"If WiSE-FT already traces the Pareto front, **kill Idea_01 in week 1** and **promote Idea_03 to #1**."。

`Idea_01/README.md` 增加了第二个独立的证伪条件：
- "**Kill H1** if the interpolation polyline is not strictly dominated."
- "**Kill H2** if naive FT already stays within ε — the problem does not exist for that domain (then try a farther domain before killing the project)."
- 停／走规则："**Kill method:** no Pareto domination on 2/2 target domains."

**记录在案的继承疑虑。** 两位独立评审人在锁定*之前*就标记了新颖性的脆弱性，而锁定依然进行，以 kill 开关作为缓解手段：
- `meta_audit.md` **PARTIAL**："constrained SAM-FT dual objective is method-shaped but **may lack novelty**; needs Stage3 of VFM keepers."
- 评审组 P12 剩余致命缺陷："**High probability the interpolation baseline matches, leaving no paper.**"
- `stage3_vfm_kills.md`："Constrained SAM-FT only survives if it beats WiSE-FT interpolation and ships a retention protocol."

**死亡后的抢救方案。** `Idea_01/README.md` §20："If WiSE-FT matches: publish the **promptability-retention suite** and the negative result ('interpolation is enough'). That is still a paper, but not *this* method paper. Pivot to Idea_03 as #1."。

---

### 2b. Idea_02 —— LesionSuppress（代号 B）

世系谱系：`SEG-0085` → Stage-3 MUTATE → 评审组 P8 → `meta_audit.md` Top-8 #4 → Stage-5 工程师 Top-5 #3。

**一句话假设**（来自 `README.md`）："深度图像增强算子会**抑制小病灶**，且该抑制表现为尺寸、对比度与算子强度的剂量响应函数；**合成病灶抑制率可预测真实漏诊率增量**。"

**锁定理由** —— `README.md` 原文："High clinical impact and a clean falsification protocol; even if universality fails across all pipelines, the per-pipeline safety curve remains valuable."

**约束性义务。** 必须在合成抑制率与真实 LIDC 小结节漏诊率之间交付肯定的秩相关（Kendall τ > 0）。`research_summary.md` 锁定假设 2："Kendall τ between synthetic-bin suppression rates and real LIDC small-nodule miss-rate deltas is **> 0 with CI excluding 0**."。

**Death 条件。** `README.md`："**Kill Idea_02** if synthetic suppression rate does not rank-correlate with real LIDC small-nodule detection drops (**Kendall τ CI includes 0**)."。

`Idea_02/README.md` 与 `experiments.md`：
- "**Kill if τ CI includes 0 or any bin sign-flip vs prediction of H2.**"
- 若 τ ~ 0：合成插入模型是论文的混淆因素 —— 停止声称安全规范。

---

### 2c. Idea_03 —— DisagreeShift（代号 D）

世系谱系：`SEG-0074` → Stage-3 KILL → `meta_audit.md` 复活变异形态（Top-8 #5）→ Stage-5 工程师 Top-5 #4。

**一句话假设**（来自 `README.md`）："在标注者分歧上训练的分割概率场在扫描仪或染色偏移下交付**更优的稀疏化误差（AURC）**，相比硬标签加温度缩放（temperature scaling）；单一标量校准无法在分布偏移下对像素进行重新排序。"

**锁定理由** —— `README.md` 原文："It addresses an open problem in uncertainty quantification for medical imaging (disagreement vs calibration), provides a strong baseline comparison, and was revived with a sharper falsifier."

**约束性义务。** 必须在稀疏化 AURC 上击败源域拟合的温度缩放（TS）—— 不仅是持平。`research_summary.md` 锁定假设 3："Disagreement-trained segmentation probability fields yield **lower sparsification error / better AURC** than hard labels + temperature scaling under domain shift. **Falsified if TS matches AURC on the target domain.**"。

**Death 条件。** `README.md`："**Kill Idea_03** if temperature scaling matches soft-label AURC on the primary shift (TS is a scalar, so matching AURC means disagreement training provided no spatial ranking benefit)."。

`Idea_03/experiments.md`：
- "Kill: soft AURC not better than hard+TS by a pre-registered margin (e.g. 5% relative) with overlapping CIs."
- "Control: uniform label smoothing vs rater-frequency f. If uniform matches, kill (not disagreement, just smoothness)."
