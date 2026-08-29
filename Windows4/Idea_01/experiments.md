# SeeingInside — 实验卡片（Experiment Cards）

此处引用的所有阈值均已冻结在 `configs/default.yaml` 中（τ1 = 0.05 Dice，ρ = 0.85 persistence，τ2 = 0.05 tracking delta，τ3 = 0.90 NRF，global kill = 0.15 Dice）。`src/config.py` 会拒绝任何在运行时覆盖阈值的操作。标签说明：
EXPECTED RESULT = 预注册预测；ACTUAL EXPERIMENTAL RESULT = 具有溯源记录的实际测量结果。**本文件中唯一的 ACTUAL 结果为 E0 测试脚手架的冒烟测试（存根模型、合成数据）。尚未运行任何真实的 SAM。此处的内容均不能作为支持关于 SAM 的科学主张的依据。**

---

## E0 — 决策逻辑验证（存根模型，合成数据） — 状态：RUN, PASSED

**核心问题。** 测试脚手架能否仅依据预注册的合取条件（pre-registered conjunction），将已知的插值器正确分类为 "interpolator"，并将已知的查询像素的模型正确分类为 "seeing"？

**设计。** 60 个合成实例（2×2 分层：对比度 contrast {低 0.06, 高 0.35} × 实心度 solidity {高, 低}），两个存根模型：`BoxFillBaseline`（负对照 — 一个字面意义上的 box→mask 插值器）和 `OracleThresholdBaseline`（正对照 — 在边界框内运行 Otsu 阈值分割，因而确实会查询像素）。实验条件：intact（完整）、object-out（精确合成背景 + Telea-inpaint 变体）、object-swap（目标替换）、sham-inpaint（虚假修复对照）、patch-shuffle（次要探针）、matched-noise（次要探针）。零假设模型：box-fill、凸性匹配填充（convexity-matched fill）、学习型 box→mask 回归器（8.3 万参数，在不相交的随机种子范围上训练，见 `src/train.py`）。

**通过准则（在 `src/eval.py::e0_assertions` 中预注册）：**
box-fill 存根 → 在所有分层中均判定为 "interpolator"；oracle 存根 → 在 ≥ 1 个分层中判定为 "seeing"。

**ACTUAL EXPERIMENTAL RESULT（冒烟测试；产物提交于 `artifacts/e0_smoke/{summary.md,verdicts.json,results.csv}`；复现命令：`python -m src.train --config configs/default.yaml && python -m src.eval --config configs/default.yaml`）：**

| model :: stratum | n | Dice intact | CSG | persist. | trackΔ | NRF | verdict |
|---|---|---|---|---|---|---|---|
| boxfill_stub :: high-contrast/high-solidity | 15 | 0.880 | 0.000 | 1.000 | −0.116 | 1.122 | interpolator |
| boxfill_stub :: high-contrast/low-solidity | 15 | 0.819 | 0.000 | 1.000 | −0.171 | 1.089 | interpolator |
| boxfill_stub :: low-contrast/high-solidity | 15 | 0.870 | 0.000 | 1.000 | −0.121 | 1.133 | interpolator |
| boxfill_stub :: low-contrast/low-solidity | 15 | 0.807 | 0.000 | 1.000 | −0.185 | 1.122 | interpolator |
| oracle_threshold_stub :: high-contrast/high-solidity | 15 | 1.000 | 0.414 | 0.586 | +0.157 | 0.988 | seeing |
| oracle_threshold_stub :: high-contrast/low-solidity | 15 | 1.000 | 0.405 | 0.595 | +0.153 | 0.893 | seeing |
| oracle_threshold_stub :: low-contrast/high-solidity | 15 | 0.746 | 0.177 | 0.664 | −0.199 | 1.324 | seeing |
| oracle_threshold_stub :: low-contrast/low-solidity | 15 | 0.769 | 0.153 | 0.784 | −0.127 | 1.169 | seeing |

E0 检查项：`boxfill_stub_all_interpolator = PASS`，`oracle_stub_seeing_somewhere = PASS`，**E0_PASS = PASS**。

**解读（关于测试脚手架本身，而非关于 SAM）：** 这两个对照模型完全按照设计实现了分离 —— 插值器的特征模式为（CSG = 0，persistence = 1，tracking 失败，NRF ≥ 1），而观察像素（seeing）的特征模式为（较大的 CSG，较低的 persistence，高对比度下 tracking 为正）。请注意，oracle 的 tracking delta 在低对比度分层中转为负值 —— 这真实地预演了为何最终结论必须由合取条件（conjunction）判定，而非由单一指标判定。同时注意 box-fill 存根的 NRF > 1：利用 GT 信息的凸性匹配零假设打败了单纯的矩形填充，这正如理论所预期。

**启发性细节（ACTUAL，冒烟测试）：** oracle 的第一个实现采用了 "foreground = minority side" 的极性规则，在*紧密*边界框内得分 Dice ≈ 0，因为在紧密框中目标占大多数 —— 后来修正为采用边缘环（border-ring）作为背景参考。在此记录这一点，是因为它正是可能在无形中破坏 E1 的那类脚手架 bug；E0 捕获了它，这正是 E0 的职责所在。

---

## E1 — 杀手级实验（KILLER）：流形内反事实 vs 无图像零假设，医学优先 — 状态：NOT RUN

**核心问题。** RQ1/RQ2：在固定紧密边界框的情况下，SAM 的掩码有多大程度依赖于图像证据？无图像零假设模型能够达到评测协议 Dice 的多大比例？

**设计（提案 §16）。** 500 个低对比度医学图像实例（MedSAM 协议数据集，冻结列表，对比度最低的两个十分位数）+ 500 个 COCO 实例（分层）× 条件 {intact（完整）, object-out（扩散模型修复去除目标）, object-swap（目标替换）, sham-inpaint（虚假修复）, box-fill, convexity-matched（凸性匹配）, prompt-only（仅 prompt）, learned-null（学习型零假设）} × padding {0, 4, 8, 16 px}。冻结的 SAM ViT-H 为主要模型，ViT-B 用于复现。后端：`OfficialSAMWrapper`；prompt-only 通过带有同批次均值 embedding 的 `PromptOnlySAMNull` 实现（`compute_mean_embedding`）。

**预注册判定结果。**
- GLOBAL KILL（约束性，Stage-3）：如果在*每一个*分层中中位数 CSG > 0.15 → 表明 SAM 具有观察能力；主张破灭；撰写负面结果简报（negative note）；升级备用方案（见 `roadmap.md`）。
- INSTRUMENT KILL：若 sham-inpaint 的 |ΔDice| > τ1/2 → 回退为仅使用 swap（swap-only）；若扩散模型与经典修复工具在判定结论上不一致 → 报告工具失效（instrument failure），终止实验。
- H1 SUCCESS：在低对比度医学图像分层中满足插值器合取条件。
- PIVOT-1：在医学图像上普遍出现 NRF > 1 → 重新调整范围为评测协议退化审计（protocol-degeneracy audit）。

**EXPECTED RESULT（预测，非实证）：** H1 — 在低对比度医学图像中表现为插值器机制（interpolator regime）；在高对比度 COCO 上表现为视觉观察机制（seeing regime）。EXPECTED：prompt-only SAM 会输出具有非微不足道 Dice 分数的框状掩码（位置支架数值，使 R2 attack iii 变得可测量）。

**成本。** ≈ 30k 次 SAM 前向传播 + 2k 次 inpainting + <1 GPU 小时的零假设训练 ≈ 2–3 GPU-days。

---

## E2 — 次要收敛性检验（流形外，已降级） — 状态：NOT RUN

Patch-shuffle（S-604）、内部 embedding 均值替换（`predict_with_interior_mean_embedding`，S-014 软化版）、匹配噪声内部填充 —— 实例与 E1 相同。定位：仅用于判定合取条件中的 c4 一致性行；绝不作为核心宣传点（根据约束性 R2 义务）。EXPECTED：相对于流形内反事实，流形外探针会夸大对图像的依赖性（MODEL SPECULATION，在提案 §19 中已明确标注）。Kill 条件：无 —— E2 不能否决主张，仅用于注解主要/次要探针之间的差异。

---

## E3 — 机制分布图（Regime Map） — 状态：NOT RUN

在对比度 × 实心度 × 尺寸构成的空间上的 CSG/persistence/NRF 曲面；包含数据集固定效应的预注册回归分析（提案 §15）。EXPECTED：随着对比度下降和实心度上升，NRF 会上升（单调性已预注册；若不满足则作为可报告的意外发现，而非隐瞒）。

---

## E4 — Prompt 与消融解耦 — 状态：NOT RUN

(a) 固定消融区域下的 padding 扫描；(b) 固定 padding 下的消融膨胀扫描 {4, 8, 16 px}；(c) 宽松/现实边界框分支；(d) 点 prompt 分支。解答 R2 提出的 padding 混淆问题；EXPECTED：NRF 随着 padding 增加和边界框变宽松而降低；点 prompt 对图像证据的依赖性 ≫ 边界框 prompt 对图像证据的依赖性。Kill 条件：如果 (a) 和 (b) 之间存在极强的交互作用导致在主要 padding 下 CSG 无法解释，则针对每个 padding 重新推导 E1 结论并以族（family）的形式报告。

---

## E5 — 模型泛化性 — 状态：NOT RUN

ViT-B/L/H、MedSAM checkpoint、(可选) SAM-2 图像模式。EXPECTED：经过边界框微调的 MedSAM 表现出比 base SAM 更高的 NRF（方向依据来自 arXiv:2606.04705 关于边界框几何先验的证据）。无论何种结果均予以报告。

---

## E6 — 实验工具稳健性 — 状态：NOT RUN

在全量数据集上引入第二种扩散 inpainter + 经典算法（Telea/NS）分支；生成判定级别的吻合矩阵。Kill 条件：跨工具判定不一致 → 宣布工具失效（此即大规模执行的 E1 INSTRUMENT-KILL）。

---

## E7 — 证据追踪梯度 — 状态：NOT RUN

替换内容梯度：同类替换（same-class swap） / 异类替换（other-class swap） / 仅纹理填充（texture-only fill）。EXPECTED：如果 SAM 读取内容，追踪得分将沿梯度单调下降；若沿梯度在零假设水平保持平坦追踪，则是最强的插值器特征。用于为论文的定性图表集提供素材。

---

## 溯源规则（Provenance Rules）

1. 任何数字唯有存在于已提交的 `artifacts/*/results.csv`（逐实例）+ `verdicts.json`（聚合）中时，方可写入 `proposal.md` 或最终论文。
2. EXPECTED → ACTUAL 的标签转换必须与产物提交在同一次 commit 中完成。
3. 存根后端的输出永久隔离在 E0 中，绝不与真实 SAM 输出合并（`model` 列 + 后端字段可确保混淆能被检测出来）。
