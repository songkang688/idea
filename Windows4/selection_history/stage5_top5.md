# Stage 5 → Top-5 (Windows4)

日期：2026-08-29 (UTC)。**补录记录** —— 参见 §0。

认知状态：**BOOKKEEPING / REVIEW JUDGMENT。** 本文件不作任何新的裁决。它仅转录
本目录中已有记录中的 20 → 5 步骤。

下文使用的证据标签：
**FACT** (可在本仓库文件或已发布的开源代码/数据集卡片中验证) ·
**VERIFIED PRIOR WORK** (沿用自 `stage3_kill_*.md` / `stage4_r2_set*.md` 的引用，已在相应文件中验证，本次未重新验证) · **HYPOTHESIS** · **SPECULATION** · **EXPECTED RESULT** · **ACTUAL RESULT**。
这些标签对应于 `supervisor_log.md § Epistemic labels in force` 的映射关系为：
KNOWN FACT → FACT, EVIDENCE → VERIFIED PRIOR WORK, MODEL SPECULATION → SPECULATION,
ACTUAL EXPERIMENTAL RESULT → ACTUAL RESULT；HYPOTHESIS 和 EXPECTED RESULT 保持不变。

> **本文件中未出现任何 ACTUAL RESULT。** `README.md` 中说明本轮运行的状态为
> "no experimental numbers were measured in this run"，且 `Idea_01/artifacts/e0_smoke/` 是
> "**stub-backend harness check** (boxfill/oracle stubs on synthetic data), **not** a SAM/COCO result"。
> 下文引用的所有数值均为从 Stage-4 文件中复制的*预注册阈值或预算估计*，绝非实际测量值。(FACT)

任何无法追溯至具体文件的内容均标记为 **INFERRED** 并附带其所依据的句子。

---

## 0. 本文件存在的原因 (出处来源)

**FACT。** `evolution_summary.md` 中记录的漏斗流程为 1080+ → 200 → 50 → 20 → 5 → 3
("Stage 5–6: Top 5 then battle notes → lock 3")。除 Stage 5 外，每一级都有独立文件：
Top-5 此前写在 `stage4_top20.md` *内部*，作为子节 `## Top 5 (Stage 5)`。

本文件将该子节提取为独立的审计记录，并为 Stage-4 的全部 20 个席位附加已记录在案的执行要求与处置结果。**本文件不更改任何裁决。**
`stage4_top20.md` 和 `stage6_battle.md` 未被修改；Final 3 及 `Idea_0{1,2,3}/` 保持原样。
在已有文件之间存在分歧之处，分歧已在 §6 中列出以供人工裁决，而非在此处自行解决。

---

## 1. 输入与输出数量统计

| | 数量 | 来源 |
|---|---|---|
| **输入** | **20 个席位** | `stage4_top20.md`，标题："WEAK ACCEPT / SILENCED (20 slots; 19 unique + P082 as gate not a paper)" |
| **输出** | **5 个条目** | `stage4_top20.md`，`## Top 5 (Stage 5)` |

**FACT — 席位运算。** 5 个输出条目共消耗了 20 个输入席位中的 **6** 个，因为 Top-5
条目 3 为合并项："P103+P096 AlphaSmoke (transfer + metric protocol)"，且 P103 和 P096 分别位列
Top-20 的第 6 名和第 4 名。因此 **有 14 个席位未作为独立的 Top-5 条目晋级**，
而非 15 个。§4 列举了全部 14 个席位。(简单的减法 20 − 5 = 15 重复计算了 P103/P096 的合并)。

**FACT — P082 不是论文席位。** `stage4_top20.md` 将其标记为 "P082 as gate not a paper"，其
具约束力的执行要求为 "Run first on released ckpts"。它作为把关项被纳入 Top-5 条目 2 之中
("P065 PromptAmnesia (gated by P082)")，因此在 20 个席位中，19 个为候选论文，1 个为把关项。

---

## 2. Top-5

顺序与内容均字面照录自 `stage4_top20.md § Top 5 (Stage 5)`。(FACT)

| # | ID(s) | 代号 | 科学问题 (单行概括) | 继承自 `stage4_top20.md` 的具约束力要求 | 遗留至 Stage 6 的未解决风险 |
|---|-------|----------|--------------------------------|-----------------------------------------------------|--------------------------------------|
| 1 | P14 | **SeeingInside** | Does SAM actually use image evidence *inside* a tight box, or is it a box→mask interpolator? | "On-manifold inpaint/swap + box→mask nulls" | Off-manifold/positional-leakage 攻击仅在反事实保持 on-manifold 时才能得到解答；"null everyone already believes" 的收益不对称性 |
| 2 | P065 (+ P082 gate, + P177 absorbed) | **PromptAmnesia** | Does domain PEFT destroy prompt-type skills (points/negatives/multimask) at matched in-domain Dice? | "Mixed-prompt FT column"; gate P082 "Run first on released ckpts" | P082 可能会击溃整条主线；coverage-vs-forgetting 混淆；shared-grid poisoning；"matched gain" 是一个未完全具体化的约定 |
| 3 | P103 + P096 | **AlphaSmoke** | Does matting pretraining beat segmentation pretraining on *real smoke*, and do binary rankings reverse under alpha metrics? | P103: "Binarized-matting arm; real-smoke primary". P096: "Measured-alpha real arm" | Synthetic-alpha 循环论证；matting ≈ matting-binarized 将击毙该机制；mMse 列可能推翻指标反转；measured-alpha 采集属于数据/标注风险 |
| 4 | P063 | **RefractionFeatures** | Does frozen-ViT feature displacement through glass track optically predicted refraction warp? | "A1-067 first; IOR=1 twins" | Sub-patch blindness vs. pixel-correspondence null；Trans10K/GDD 为单图基准，因此需要重新拍摄或新采集数据；渲染成本更高 |
| 5 | P079 | **MemoryProbe** | Does SAM2's memory encode position/order rather than appearance? | "Subtract explicit time encodings" | SAM2-analysis 方向的实时抢发风险；在自然体数据中位置与外观固有相关；记忆阶段的 *delta* 才是核心主张，而非原始可解码性 |

> **命名注意 (FACT)。** `P079` (S-079，SAM2 记忆探测，Set A) 与 `P079f` (B1-079，FSS
> 背景置换，Set C) 为不同项目。P079 晋级；P079f 未晋级 (§4)。

### 2.1 各条目详细情况

每个段落先给出具约束力要求及其出处，随后给出风险及其出处。科学问题的措辞
在存在 Final-3 代号时取自 `README.md § This round's three Ideas`，针对 P063/P079 则取自
`stage3_top50.md § Stage-4 attack list`。(FACT)

**1 — P14 SeeingInside。** *执行要求：* `stage4_top20.md` 排名 1 —— "On-manifold inpaint/swap + box→mask
nulls"。`stage4_r2_setA.md § P14` 明确了四个部分："(a) make **on-manifold natural
counterfactuals** the primary intervention — diffusion-inpaint the object out (or swap in a different
object) with the box held fixed; (b) demote embedding-zeroing / S-604 patch-shuffle to secondary
convergence checks; (c) add the prompt-only and learned box→mask nulls, matched per instance on
convexity; (d) make low-contrast medical the primary endpoint"。Set A 同样记录了仅凭原始实验手段将失败："The original S-014 embedding-zeroing instrument alone: REJECT." (FACT)
*风险：* Set A 提出的收益不对称攻击 —— "if Dice collapses, the result is the null everyone already
believes ('SAM sees')" —— 是任何重新设计都无法消除的上限。(FACT) Set A 给出的 WEAK ACCEPT
的前提是 "conditional on the redesign **and the P107v merge**"；合并的后半部分在下游被否决
(`stage4_top20.md` REJECT 了 "P107v-as-flagship (HalluSegBench scoop)"；`stage6_battle.md`："Supervisor:
**do not merge**")。**INFERRED：** 因此 P14 进入 Stage 6 时，其 Stage-4 存活条件中的一项条款已被明确按字面置为不可满足；这一判断基于上述两句引用，属于记录层面的观察，而非重新裁决。此外，Set A 的执行要求 (d) 将低对比度医疗作为 *primary* 终点，而 `README.md § Most recommended` 则归功于 Idea_01 "does not
require medical FT compute" —— **INFERRED** 这两者仅在医疗终点为仅评测 (不进行微调) 时兼容；已在 §6 中标记。

**2 — P065 PromptAmnesia，由 P082 把关。** *执行要求：* `stage4_top20.md` 排名 2 —— "Mixed-prompt FT
column"；排名 8 P082 —— "Run first on released ckpts"。`stage4_r2_setB.md § P065`："The forgetting claim
survives **only if the prompt-type ordering persists inside the mixed-prompt column** — that column
isolates forgetting from coverage; the box-only column alone proves nothing"，以及 "Verdict: WEAK
ACCEPT. Flagship of the thread, but the paper is the mixed-prompt column and the oracle-gap
decomposition; without them it is SAM-Med2D's table re-plotted." (FACT)
*风险：* `stage6_battle.md § Decisive experiments` 第 1 项 —— "P082 noise-floor envelope (1–2 GPU-days) —
if 'forgetting' is thresholding, **pivot Idea_02**"。(FACT) Set B 提出的跨论文攻击 1 和 2 对该条目仍然成立："**Shared-grid poisoning.** P065, P177, P031, P082 all reuse one fine-tuning
checkpoint grid … a single recipe flaw … contaminates four papers at once"，以及 "**'Matched gain' is a
single point of failure.**" (FACT) `README.md` 补充了拥挤度上限："crowded by CA-SAM/Gu et al.
unless the mixed-prompt column is the paper"。(FACT / 引文属 VERIFIED PRIOR WORK)

**3 — P103 + P096 AlphaSmoke。** *执行要求：* `stage4_top20.md` 排名 6 P103 —— "Binarized-matting arm;
real-smoke primary"；排名 4 P096 —— "Measured-alpha real arm"。`stage4_r2_setA.md § P103` 确定了四分支设计 "{COCO-seg, matting, matting-binarized, scratch} at matched fine-tune budgets …
**primary endpoint on real smoke**"，且 `stage4_r2_setC.md § P096` 将 measured-alpha 分支与 mMse 列均定为 "**binding**"："Without the measured-alpha arm, attack 3 stands and the verdict
flips to REJECT." (FACT)
*风险：* 该条目附带两个预注册的淘汰条件。Set A："If matting ≈
matting-binarized, the soft-boundary mechanism is dead even if the transfer helps — report that and
stop." Set C："show whether mMse against *binary* GT rank-correlates with alpha-MAE against *alpha* GT.
If it does (τ > 0.8) … pillar 1 dies — pre-registered kill condition." (FACT —— 阈值为预注册阈值，**非**实际测量值。)`README.md`："R2 requires a measured-alpha arm and real-smoke
primary; data/annotation risk is higher"。(FACT) Set A 指出的残留循环论证攻击也在设计上依然存在：alpha GT "exists only where smoke was synthetically composited … or subjectively annotated"
(Set C 攻击 3)。(FACT)

**4 — P063 RefractionFeatures。** *执行要求：* `stage4_top20.md` 排名 3 —— "A1-067 first; IOR=1 twins"。
`stage4_r2_setA.md § P063`："**Can an experiment shut me up? YES — if the program is reordered.** …
Mitsuba scenes with an IOR sweep including IOR = 1.0 twins … regress per-patch feature displacement on
predicted optical warp **with pixel-correspondence R² as the printed null**"，以及 "A1-063 as standalone
flagship: REJECT." (FACT)
*风险：* sub-patch 压缩问题尚未解决 —— "refraction warps through common glassware are frequently
sub-patch (<16 px), invisible to patch-quantized ViT features, so R²≈0 there is a resolution artifact,
not absent physics; supra-patch warps are trackable by raw pixel correspondence"。此外还有数据风险："Trans10K/GDD are single-image benchmarks, so the two-frame method needs re-shot or newly captured
data"。(FACT) `stage6_battle.md` 记录了使其成为备选方案的成本/上限权衡："glass physics
has higher ceiling and heavier rendering cost"。(FACT)

**5 — P079 MemoryProbe。** *执行要求：* `stage4_top20.md` 排名 5 —— "Subtract explicit time encodings"。
`stage4_r2_setA.md § P079`："**Verdict: WEAK ACCEPT**, conditional on (a) and (b) being mandatory"，其中 (a) 为 "regress out the known temporal encodings, probe the residual"，(b) 为 "report the
position:appearance information ratio at encoder vs memory — the *delta* is the claim"。"The headline as
originally designed: REJECT." (FACT)
*风险：* Set A 提示存在实时抢发风险 —— "Scoop risk is live (the SAM2-analysis line, arXiv:2503.00042)"
(依据 Set A 的引用规范属 VERIFIED PRIOR WORK；本次未重新验证) —— 以及在自然数据上任何探测手段都无法消除的辨识问题："in videos and volumes, position and
appearance are strongly correlated … linear probes on correlated nuisances identify nothing without
decorrelation"。(FACT)

---

## 3. 晋级的规则依据

**FACT。** `evaluation_rubric.md` 严禁用平均分排序 ("Do **not** rank by mean score. Use a
decision rule.")，并提供了 Stage-4 文件据以论证的两张列表：

- *存活规则 (Survival rules)：* "High-risk, high-upside with a cheap Killer Experiment"；"Simple counter-intuitive
  hypothesis"；"Extreme reviewer disagreement"；"Can be killed in <1 GPU-day"。
- *淘汰规则 (Kill rules)：* "Core novelty is 'new module'"；"Hypothesis is not falsifiable"；"Killer experiment
  requires a new foundation-model pretrain"；"Closest prior work already ran the same experiment
  (Stage 3)"；"Reviewer #2 attack cannot be answered by an experiment (Stage 4)"。
- *ROI：* 维度 14，"Research ROI = (upside × falsifiability) / (compute × calendar friction)"。

**FACT。** 进入 Stage 5 的席位中没有任何一个是被*淘汰规则*刷掉的 —— 全部 20 个席位此前均已通过 Stage 4 的 "survival iff a realistic experiment would silence the attack" 门槛。因此 20 → 5 步骤是一次**配额/ROI 排序**，§4 中的原因相应地归为已记录在案的三类：
(a) Stage-4 文件中的明确剔除或降优先级指令；(b) Stage-4 文件中的明确上限/降级陈述 ("not a flagship", "demotes to a note", "one figure")；
(c) Stage-6 裁决中将该席位合并归入某个存活项。§4 中的每一行都标注了适用的类别，以便读者能够区分何处存在明确的剔除记录，何处仅存在上限陈述。

---

## 4. 20 → 5：未晋级的 14 个席位的处置情况

排名为 `stage4_top20.md` 中的 Top-20 排名。**处置结果 (Disposition)** 区分了 *absorbed* (被吸收：仍在 Final-3 研究包中获得资助)、*gate* (把关项：运行实验但不作为独立论文)、*demoted* (降级：作为子分支/附录/伴随性研究保留) 以及 *deferred* (搁置：通过 Stage 4 但未获得 Stage-5 席位)。**依据类别 (Basis kind)** 对应 §3 中的 (a)/(b)/(c)。

| Rank | ID | 处置结果 | 记录在案的原因 | 依据类别 |
|------|-----|-------------|-----------------|-------|
| 7 | P177 | **Absorbed** (被吸收入 Top-5 条目 2) | `stage6_battle.md` 锁定了 "**Idea_02 PromptAmnesia (P065/P082/P177)**" —— P177 在 PromptAmnesia 研究包内获得资助，未被砍掉。`stage4_r2_setB.md § P177` 此前已否定了其独立地位："The freeze ablation alone (S-177) is one figure and remains REJECT as a standalone; it lives only as an arm inside this design"，并将其置于评测复用链条的末端："P082 first … then P065 → P031 → P177"。 | (c) + (b) |
| 8 | P082 | **Gate** (把关项，非论文席位) | 其地位已在 `stage4_top20.md` 自身的分节标题中确定 —— "20 slots; 19 unique + **P082 as gate not a paper**" —— 且其排名第 8 的执行要求为 "Run first on released ckpts"。`stage4_r2_setB.md § P082`："**WEAK ACCEPT — and it must run FIRST** … it is the gatekeeper that decides whether P065/P177 are measuring signal"，并记录了自毁性分支："if the audit finds forgetting *does* exceed the noise floor, this 'paper' is a confirmation note." 作为 "gated by P082" 纳入 Top-5 条目 2，并作为第 1 项列入 `stage6_battle.md § Decisive experiments`。 | (a) |
| 9 | P107 | **Demoted** (降级为条目 2 的消融实验章节) | `stage6_battle.md § Unresolved disagreements`："P065 vs P107 for PEFT slot: P107 is more 'constructive mechanism' but smaller blast radius. **P065 is the PEFT paper**; P107 is an ablation chapter." `stage4_r2_setB.md § P107` 补充了其若单独成文所必须承担的不可协商条件："the decoupled-metric requirement is non-negotiable — with raw boundary-F this is unpublishable regardless of outcome." | (c) |
| 10 | P044 | **Deferred** (搁置 —— 明确受预算上限限制) | `stage4_r2_setB.md § P044`："The significance attack stands as a ceiling: this is a strong short paper or workshop headliner, not a main-track flagship; **Stage 5 should budget it accordingly and must not let it absorb resources from P065/P082.**" 这是直接针对 Stage 5 的指令，要求不要在其上耗费旗舰席位。 | (a) |
| 11 | P042 | **Deferred** (搁置) | **NO RECORDED REASON — 需要人工确认。** P042 拥有 `stage4_r2_setC.md` 中最强的裁决级别 ("SILENCED", 置信度 Med-High, 在 *What no experiment can fix* 下注明 "Nothing structural")，且在 Set C 的 "Compute ranking of survivors (cheapest first): P042, P096, P079f, P228, P040" 中名列**第一**。因此依据 `evaluation_rubric.md` 的 ROI 标准，它本应是一个强有力的候选者，然而在 `selection_history/` 的任何文件中均未说明为何其未获得 Top-5 席位；`stage6_battle.md` 完全未提及它。*记录在案但已得到回应*的攻击 (属于背景上下文，**非**剔除原因)："Hygiene-as-paper" 以及 "'Fraction of the gap' is ill-posed"。 | none |
| 12 | P031 | **Demoted** (降级为条目 2 的实验格/附录) | `stage4_r2_setB.md § P031`："**WEAK ACCEPT**, with the explicit warning that **the modal outcome is a recipe footnote**"，仅存活于 "{IoU-loss on, zero-shot, recalibrated}" 实验格中，且 "If the easy fix kills the desync, report the kill inside P082's deflation frame; **do not stretch it into a paper.**" 它在共享网格评测顺序中也处于中间位置 ("P065 → P031 → P177")，因此无法排在条目 2 之前。`stage4_r2_setB.md § P110` 此外将 P110 的图表导入 "P065/P031 appendices"。 | (a) + (b) |
| 13 | P079f | **Deferred** (搁置) | `stage4_r2_setC.md § P079f`, *What no experiment can fix*："If the effect exists but is fully absorbed by the 2024 fixes, the paper **demotes to a benchmark-hygiene note**. Acceptable risk." 先前工作的压力被记录为险些触发 Stage-3 淘汰规则：Zhu et al. CVPR 2024 和 TBS AAAI 2024 意味着 "the 'shortcut' you reveal is the motivation section of two 2024 method papers" (VERIFIED PRIOR WORK)。Set C 仅通过收窄交付目标才得以使其存活，且四项对照实验具有约束力。 | (b) |
| 14 | P051 | **Deferred** (搁置 —— 明确不予资助) | `stage4_r2_setC.md § Notes for the supervisor` 3："**The two training-heavy survivors should not both be funded; P051's shelf-life risk makes P061u the safer of the two if forced to choose.**" 成本记录："~40–80 training runs … **borderline against the rubric's 'weeks not years'**" —— 即违背了 `evaluation_rubric.md` 维度 5/6 和 ROI 规则。*What no experiment can fix：* "Shelf life." | (a) |
| 15 | P040 | **Deferred** (搁置) | `stage4_r2_setC.md § P040`, *What no experiment can fix*："If the two-factor sweep shows width effects are fully absorbed by contrast, no framing rescues a standalone paper — that outcome is **one figure inside the medical-eval thread**. The submission must be built so that this demotion path is explicit." 裁决结果带有条件 ("SILENCED-IF-MUTATED")，核心攻击针对已发表的 GLM 提出了 "**'Quantified lore'**" 质疑 (VERIFIED PRIOR WORK)。 | (b) |
| 16 | P052 | **Deferred** (搁置 —— 重新划定范围) | `stage4_r2_setB.md § P052`："**WEAK ACCEPT — re-scoped.** Mandatory: retitle the claim to the measurable interaction … '**objectness prior**' may appear as interpretation, **never as the result**"，仅在 "despite the fragile chain" 的情况下保持在线上。一个标题核心词被删除的席位无法支撑 Top-5 条目。 | (b) |
| 17 | P228 | **Deferred** (搁置 —— 伴随角色) | `stage4_r2_setC.md § P228`："SILENCED-IF-MUTATED — within-model prompt-manipulation design binding; cross-model 'vision-only vs VLM' comparisons excluded from the headline"，以及 "**Pairs naturally with the demoted P107v residue**"。其 Top-20 执行要求已将其限定于单一目标："BiomedParse; not B1-107"。记录在案的残留风险："If the prompt-causal share is ~0 … it re-enters Udandarao's shadow." | (b) |
| 18 | P101 | **Deferred** (搁置 —— 首选剔除项) | 语料库中最强烈的明确剔除记录。`stage4_r2_setA.md § P101`："**WEAK ACCEPT** — lowest tier; **first to cut if the 20-slot quota binds.** Without the matched-area baseline table: REJECT." 以及 § *Consequences for the pool* 1："cut my accepts in this order: **P101 first**, P103 second"。核心攻击：该标题成果 "close to guaranteed by construction" (注意力温度，而非粒度编码)。 | (a) |
| 19 | P061u | **Deferred** (搁置 —— 否定旗舰地位) | `stage4_r2_setC.md § P061u`, *What no experiment can fix*："**This can never be a flagship** — the ceiling is a solid, well-controlled attribution study at a second-tier venue or a strong workshop-to-main pipeline." 成本："~50–80 GPU-days total. Heavy but within one-lab feasibility" —— 在 ROI 衡量下输给了仅需评测的存活项。 | (a) + (b) |
| 20 | P177-arm | **Demoted** (降级 —— 从未作为独立论文) | 该席位在 `stage4_top20.md` 本身中就被定义为非独立席位：其排名 20 的一句话概括为 "Freeze-encoder figure only"，其具约束力的要求仅为短语 "**Not standalone**"。意见一致：`stage4_r2_setB.md § P177` —— "The freeze ablation alone (S-177) is one figure and remains REJECT as a standalone." | (a) |

### 4.1 数量统计

**FACT。** 上表 14 行 + 5 个 Top-5 条目消耗的 6 个席位 = 20 个输入席位。按处置分类：
absorbed 1 项 (P177)，gate 1 项 (P082)，demoted 3 项 (P107, P031, P177-arm)，deferred 9 项 (P044, P042, P079f,
P051, P040, P052, P228, P101, P061u)。恰好有**一项**没有记录在案的原因：**P042** (rank 11)。

### 4.2 从未进入 Stage 5 的席位

**FACT，** 为保证漏斗记录完整性：`stage4_top20.md § REJECT (out)` 列出了 "P060, P001, P004, P007, P110,
P108, P107v-as-flagship (HalluSegBench scoop)"。这些在 Stage 4 已被砍掉，不属于这 20 个席位，
在此不重新讨论。`stage4_r2_setA.md` 保留 P001 "as hygiene gate"；`stage4_r2_setB.md`
将 P110 的报告图表并入 "P065/P031 appendices"，并将 P108 的漂移统计量记录 "as a free
covariate in the grid"。

---

## 5. 与 Stage 6 的衔接

仅作转录。Stage 6 的裁决记录在 `stage6_battle.md` 中；本处不作任何重新裁决。

**FACT。** 在 Top-5 中，有 3 项成为 Final 3，2 项作为备选方案：

| Top-5 # | ID(s) | 结果 | 成果包 |
|---|---|---|---|
| 1 | P14 | **Final 3** — 推荐 #1 | `Idea_01/` SeeingInside |
| 2 | P065 (+P082 gate, +P177) | **Final 3** | `Idea_02/` PromptAmnesia |
| 3 | P103 + P096 | **Final 3** | `Idea_03/` AlphaSmoke |
| 4 | P063 | **Backup** (备选) | — |
| 5 | P079 | **Backup** (备选) | — |

`stage4_top20.md § Final 3` 说明了锁定项与备选触发条件："See `stage6_battle.md`. Locked:
… **Idea_01 SeeingInside (P14)** — recommended #1 · **Idea_02 PromptAmnesia (P065/P082/P177)** ·
**Idea_03 AlphaSmoke (P103/P096)**"，以及 "P063/P079 are first backups if a killer experiment dies in
week 1." `README.md § This round's three Ideas` 与此一致。(FACT)

**FACT。** `stage6_battle.md` 记录了决定第三个席位与 PEFT 席位的两项裁决：
"**Third slot = AlphaSmoke.** P063 is backup" 以及 "**P065 is the PEFT paper**; P107 is an ablation
chapter" —— 并明确保留了一项未解决的分歧：Set A "wants P14 merged with P107v; Set C
**scooped P107v** (HalluSegBench). Supervisor: **do not merge**."

**FACT。** Final 3 的执行顺序已在 `stage6_battle.md § Decisive experiments that
remain (must run in this order)` 中确定：P082 噪声下限包络，随后是 P14 框内流形上图像修复 (on-manifold inpaint)，再后是 P103 线性探测 / 微型头部 (linear-probe / tiny-head)。`README.md § Next experiment to run (this week)` 与之一致。

**FACT。** 根据 `README.md`，所有三个成果包均处于 "**ready to start killer experiments**" 状态；尚未运行任何 killer experiment。备选方案的激活以 "in week 1" 内的失败为触发条件，该情况尚未发生，故无法在此记录。

---

## 6. 与 `stage4_top20.md` 的一致性

**本节声明 (FACT)。** 本文件为提取件而非修订件：其成员组成、排序、ID、代号以及合并结构与 `stage4_top20.md § Top 5 (Stage 5)` 中的 5 个条目完全相同，顺序一致。下表对它们进行了逐项对比。

| # | `stage4_top20.md § Top 5 (Stage 5)` | 本文件 §2 | 是否完全一致？ |
|---|---|---|---|
| 1 | "P14 SeeingInside" | P14 SeeingInside | yes |
| 2 | "P065 PromptAmnesia (gated by P082)" | P065 PromptAmnesia, P082 gate | yes |
| 3 | "P103+P096 AlphaSmoke (transfer + metric protocol)" | P103 + P096 AlphaSmoke | yes |
| 4 | "P063 RefractionFeatures" | P063 RefractionFeatures | yes |
| 5 | "P079 MemoryProbe" | P079 MemoryProbe | yes |

**Top-5 内容无任何差异。** 以下各项均为编写本文件时发现的*关于现有语料库的观察*。列出这些内容供人工裁决，且**均未采取操作**：未修改任何现有文件，未改变任何裁决结果，且 `Idea_0{1,2,3}/` 保持原样。

1. **席位运算，15 vs 14。** 从 20 减去 5 容易让人以为有 15 个未晋级席位；真实数字为 14 个，因为 Top-5 条目 3 合并了两个席位 (P103 第 6 名 + P096 第 4 名)。记录于 §1 和 §4.1。没有文件出错；只是合并容易算错。(FACT)
2. **Top-5 顺序 ≠ Top-20 排名顺序。** `stage4_top20.md` 将 P063 排在第 3、P096 排在第 4、P079 排在第 5、P103 排在第 6，但其 Top-5 子节将它们排列为 P14, P065, P103+P096, P063, P079 —— AlphaSmoke 从第 4/6 名上升到第 3 位。`stage6_battle.md` 提供了依据 ("smoke transfer has public data and a one-week killer. **Third slot = AlphaSmoke.**")，因此这是有据可查的重新排序而非前后矛盾，但这两种顺序不是同一张列表，读者比对时会注意到。(FACT)
3. **Set A 的剔除顺序 vs P103 的结果。** `stage4_r2_setA.md` 指示 "cut my accepts in this order: P101 first, **P103 second**"，然而 P103 晋级到 Top-5 并作为 `Idea_03/` 进入 Final 3。Set A 的指示限定于 "if the global 20-slot quota binds"，而 `stage6_battle.md` 针对第三个席位给出了推翻该指示的明确理由，因此两者是可以调和的 —— 但这种调和从未在任何地方以书面形式写明。**标记供人工确认。** (引文属 FACT；调和解释**INFERRED**自 "if the global 20-slot quota binds" 加上 "Third slot = AlphaSmoke"。)
4. **P042 没有记录在案的 Stage-5 原因。** 参见 §4 排名 11。它拥有 Set C 最高级别的裁决结果以及最低计算成本排名，因此它在 Top-5 中的缺席在 `selection_history/` 的任何文件中均未得到解释。**需要人工确认** —— 要么存在未记录在案的原因，要么该席位系被疏漏遗忘。(无记录在案的原因属 FACT。)
5. **一项遗留的 Stage-5 执行要求似乎尚未履行。**
   `stage4_r2_setC.md § Notes for the supervisor` 1 说明："The stage3_top50 flagship list needs the corresponding edit at Stage 5" —— 因为 P107v 的旗舰地位已被撤销。`stage3_top50.md` 在 "### SURVIVE (flagship)" 下仍列有 "10. **P107v** B1-107 — Inpaint-object-out; phantom dense masks (VLM hallucination)"。`stage4_top20.md` 和 `reviewer_summary.md` 确实记录了该撤销，因此结论在其他任何地方都毫无疑问；仅 Stage-3 文件未及时更新。**本处未作修改** (本任务仅限于创建本文件)。**标记供人工处理。** (FACT)
6. **P14 的医疗终点要求 vs README 中的计算量声明。**
   `stage4_r2_setA.md § P14` 执行要求 (d) 为 "make low-contrast medical the primary endpoint"，而 `README.md § Why not the others as #1` 则归功于 Idea_01 "does not require medical FT compute"。**INFERRED：** 当且仅当医疗终点仅用于评估时两者兼容；这两句话从未明确说明这一点。**标记供人工确认。** (INFERRED，依据该两句引用。)
7. **P14 的 Set-A 存活条件按字面仅可部分满足。**
   Set A 的 WEAK ACCEPT 是 "conditional on the redesign **and the P107v merge**"；在 P107v 被拒绝作为旗舰后，该合并随后被禁止 (`stage6_battle.md`："Supervisor: **do not merge**")。重新设计条款依然有效，即 `stage4_top20.md` 排名 1 所编码的内容；合并条款则失效。记录于此，以防后续读者将失效条款视为未满足的执行要求。(引文属 FACT；**INFERRED** 该条款系失效而非待履行。)

**本文件建立后的漏斗完整性 (FACT)。** 1080+ → `stage1_*.md` · 200 → `stage2_top200.md` +
`stage2_top200_ids.txt` · 50 → `stage3_top50.md` · 20 → `stage4_top20.md` · **5 → 本文件** ·
3 → `stage6_battle.md`。至此，`evolution_summary.md` 中漏斗的每一级均有了独立的记录文件。
