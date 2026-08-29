# Idea_01 —— 实验卡片

> **下面每张卡片的状态都是 NOT RUN**，只有 E0 例外——它跑在合成
> 数据上，且只能验证测试台。Windows6 的 **ACTUAL RESULTS 为零**。
> 每个预算都是 **HYPOTHESIS**。每个被预测的趋势都是 **EXPECTED RESULT**。

## 本文件使用的认知标签

`EXPECTED` = 预先注册的假设性趋势。`ACTUAL` = 用真实权重在真实数据上跑出来的
数字 —— **一个都没有**。凡今天某张卡片会打印数字的，那些数字都来自一个合成
phantom 加一个"阈值 + 连通域"的替身，而脚本会在运行时说明这一点。

## 卡片索引与执行顺序

| 卡片 | 名称 | 它裁决哪道门 | 预算（HYPOTHESIS） | 状态 |
|---|---|---|---|---|
| **E0** | 测试台验证（合成，CPU） | 测量工具能用吗？ | 约 0，CPU 数秒 | **已跑 —— 测试台 PASS** |
| **E1** | **KILLER**：相关性臂，单个窗 | H1 | 约 2 GPU-h | NOT RUN |
| **E2** | 窗扫描 × AMG 网格 | H3 | 约 8–20 GPU-h | NOT RUN |
| **E3** | **残余义务**：强度 vs 纹理反事实 | H2 | 约 2–4 GPU-h | NOT RUN |
| **E4** | COCO 特异性对照 | H4 | 约 2 GPU-h | NOT RUN |
| **E5** | SAM2 泛化性（可选） | 范围界定 | 约 4–8 GPU-h | NOT RUN |
| **E6** | 失败案例定性检查 | 呈现方式 | 约 1 GPU-h | NOT RUN |

顺序为 E0 → E1 → E2 → E3 → E4，E5/E6 可选。**E1 通过后 E2 与 E3 可以
并行跑**；它们不共享任何状态。E4 必须等 E3，因为去控制一个还没挣到机制的
效应的特异性是没有意义的。

---

## E0 —— 测试台验证（合成，CPU）—— 状态：已跑，PASS

**目的。** 在花掉一个 GPU-hour 之前，先证明测量工具没坏。
这张卡片**不能确认科学结论**；它只能让测试台不通过。

**输入。** `data.synthetic_ct` —— 一个分段常数的 HU phantom（空气 / 脂肪 /
软组织 / 肝 / 骨等平台值）加上叠加纹理，并通过一对有记录的 W/L 做窗宽窗位。
不用真实数据，不用权重。

**运行。**

```bash
python Idea_01/src/run_smoke.py --seed 0
python -m unittest discover -s Idea_01/tests
```

**指标。** 全部三个预先注册的指标（见 `proposal.md` §15）加两个
基数诊断量。

**判定阈值（FACT，原始规则）：** *"If even on synthetic blobs
AMG-mock does not beat SLIC, the **implementation** is wrong — fix before real
SAM."*。这条被字面实现了：当强度基线未能在三个指标上都胜过 `slic_lite` 时，
`run_smoke.py` 以非零状态退出。

**分叉。** FAIL → 修实现。这永远不是一个科学结论。PASS → 进入 E1。

**这张卡片在 W6-T3 期间抓到的两个测试台缺陷**（之所以记录，是因为这恰恰
就是 E0 存在的意义，而且两者各自都会静默地废掉一条假设）：

1. **AMG 替身当时是在分位数上做阈值的**，而分位数对任何单调强度重映射
   都不变。于是 H2 的强度臂*按构造*就会得到完美的 1.000 自一致度，
   永远不可能被扰动。修法是改用在做过窗宽窗位的图像上的绝对阈值；
   由 `test_amg_mock_is_not_invariant_to_monotone_remap` 守住。
2. **Hungarian IoU 当时是按 |A| 归一化的**，这把匹配质量与"嵌套 AMG 清单
   对上 k 类划分"之间的基数差异混为一谈。对于结构上相似的掩码集合，
   它报出的一致度只有约 0.03。修法是改按 `min(|A|,|B|)` 归一化，
   并把 `cardinality_ratio` 与 `coverage_iou` 分开报告。

**E0 不能说明什么。** 关于 SAM 什么都不能说明，关于 H2 也什么都不能说明 ——
那个替身在逐像素噪声下会碎裂，其原因与 objectness 无关，因此它在纹理臂上的
行为没有信息量。`run_smoke.py` 会把这条告诫紧挨着数字打印出来。

---

## E1 —— KILLER：相关性臂，单个窗 —— 状态：NOT RUN

**目的。** 用尽可能便宜的方式裁决 H1。

**输入。** 来自 TotalSegmentator 或 MSD 的 **100** 张 CT 切片
（数据集论文的引用为 `CITATION NEEDED — 待人工核验`），软组织／腹部
窗（W/L 400/40），切片清单**在开跑之前预先注册**。

> **关于样本量的 FACT。** 记录曾自相矛盾：`README.md`
> 和最初的 killer 清单写 50，Stage-5 工程化区块写 100。
> `stage6_battle.md` §4.7 记录了这处矛盾，§6 通过取较大值予以裁定。
> 本 package 各处统一使用 **100**。

**各臂。** SAM ViT-B AMG（`points_per_side = 32`）对比 k-means（k ∈ {8,16,32}）、
multi-Otsu、GMM 以及 SLIC。

**指标。** Hungarian IoU、ARI、boundary-F @ ±2 px —— 三个全报，永远全报 ——
再加 `coverage_iou` 与 `cardinality_ratio` 作为诊断量。采用逐切片配对
比较；在切片上做 bootstrap 置信区间。

**判定阈值。**

| 观察结果 | 动作 |
|---|---|
| 最好的强度基线在**三个**指标上都 > SLIC，且置信区间不含 0 | **继续**进入 E2 与 E3 |
| 各指标结论混杂 | **继续但打标记**；到 E2 时 H1 必须在三个指标上都成立，否则该主张就是依赖指标的 |
| SLIC ≥ 每一个强度基线 | **KILL** 整个项目 |

**预算。** 约 2 GPU-h（**HYPOTHESIS**，来自 `evolution_summary.md`）。

**需要留意的失效模式。** 如果 AMG 每张切片返回数十个掩码而聚类器返回
`k` 个，`cardinality_ratio` 就会很大。这是预期之内的，如实报告，
不做修正抹平。

---

## E2 —— 窗扫描 × AMG 网格 —— 状态：NOT RUN

**目的。** 裁决 H3：E1 观察到的效应是 CT 的性质，还是某一个
预处理选择的性质？这是 Reviewer #2 的第 1 号攻击，不满足就是致命的。

**输入。** 同样那 100 张切片。窗：腹部（400/40）、骨（2000/400）、
肺（1500/−600），或有记录的等价设置。AMG `points_per_side` ∈ {16, 32}。
k ∈ {8, 16, 32}。

**指标。** 同 E1，逐单元格计算。报告**完整的** 3 × 2 × 3 网格；不为省版面
省略任何单元格。

**判定阈值。**

| 观察结果 | 动作 |
|---|---|
| H1 的方向在 3 个窗中的 ≥2 个**且** ≥2 组 AMG 设置上成立 | **继续** |
| 恰好在 1 个窗上成立 | **PIVOT** —— 论文改成"窗宽窗位制造出表面上的 objectness"，那是一个真实但不同的发现 |
| 在网格如实呈现之后 0 个窗成立 | **KILL** |

**EXPECTED（未经测量）。** 在肺窗下差距会收窄，因为那里空气／组织的
对比度强到大多数方法都会一致。在那里差距收窄不算失败；在那里差距
*反转*才是警报。

**预算。** 约 8–20 GPU-h（**HYPOTHESIS**）。

---

## E3 —— 残余义务：强度 vs 纹理反事实 —— 状态：NOT RUN

> **这张卡片就是 Reviewer #2 附加的、有约束力的残余义务，原文照引自
> `stage4_reviewer2_cheap5.jsonl`：**
>
> > `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`
>
> 本 package 里没有别的东西能履行它。没有 E3，这个贡献就是一篇
> evaluation note（另见下方那处未解决的严重性冲突）。

**目的。** 裁决 H2 —— 那个把相关性转化为机制的双重解离。

### 臂 A —— 强度重映射（改变强度，冻结边）

1. 计算做过窗宽窗位的切片的 Sobel 梯度支撑，并**把它冻结为参照**，
   这样边的位移可以被测量而不是被假定。
2. 对组织内部的 HU 施加一个**严格单调**的重映射
   （`interventions.intensity_remap`，`gamma` 在 {0.4, 0.5, 0.7, 1.4} 上扫描）。
3. **有效性门禁：** `check_remap_is_monotone` 必须通过。一个非单调映射
   会创造或摧毁边，从而让这条臂与它本应固定住的东西发生混淆。
   代码会抛异常而不是返回数字。
4. 重跑 AMG。测量它与未受干预的 AMG 掩码集合之间的自一致度。

### 臂 B —— 纹理置乱（改变纹理，冻结局部强度）

1. 把切片切成小块（`shuffle_tile` 在 {4, 8, 16} 上扫描）。
2. 在每个小块内部置换高频残差，同时保持该块均值不变
   （`interventions.texture_shuffle`）。
3. **有效性门禁：** `check_shuffle_preserves_tile_means` 必须以 1e-9 的精度通过。
   正是这项检查才让我们有资格把这条臂称为"保持强度不变"；没有它，
   任何 AMG 的响应都可能其实是对强度的响应。
4. 重跑 AMG。测量它与未受干预的 AMG 掩码集合之间的自一致度。

### 读出方式

设 \(s_{\mathrm{int}}\) 与 \(s_{\mathrm{tex}}\) 为两个自一致度
（1.0 = 该干预什么都没改变）。

| 观察结果 | 解释 | 动作 |
|---|---|---|
| \(s_{\mathrm{int}} \ll s_{\mathrm{tex}}\)，且在 ≥2 个窗和 ≥2 组 AMG 设置上成立 | AMG 跟随强度，忽略纹理 | **继续** —— 机制性论文 |
| \(s_{\mathrm{int}} \approx s_{\mathrm{tex}}\) | 没有解离 | **降级**为 evaluation note —— 见下 |
| \(s_{\mathrm{int}} > s_{\mathrm{tex}}\) | AMG 跟随纹理，而不是强度 | **KILL** 该假设；报告负结果 |
| 方向随 `shuffle_tile` 翻转 | 这条臂测的是 tile 尺寸，不是纹理 | **无结果**；重新设计测量工具 |
| 任一有效性门禁未通过 | 测量工具坏了 | **无结果**；先修，不要报告 |

**同样有约束力（Stage-5 门禁，FACT）：** 若结果显示 AMG 与真值的接近程度
超过它与 k-means 的接近程度，**并且**纹理置乱把 AMG 扰动得很厉害，
则 **STOP**。这个组合说明 AMG 在做解剖结构，而该假设干脆就是错的。

**动笔前尚未解决（FACT，`stage6_battle.md` §4.4）。** Stage-4 的
记录说 H2 失败意味着 *"else evaluation note"*（降级）；而本
package 自己的 `reviewer_attacks.md` 说的是 *"If we cannot run the causal arm, do
not submit"*（扣下不发）。没有任何产物说明以哪一方为准。**动笔之前定下来，
不要边写边定。**

**预算。** 约 2–4 GPU-h（**HYPOTHESIS**）。

---

## E4 —— COCO 特异性对照 —— 状态：NOT RUN

**目的。** 裁决 H4。Reviewer #2 的先手防范已记录在 Stage-5
工程化区块中：*"same protocol on COCO; clustering equivalence must be
**CT-specific**."*

**输入。** 一个 COCO 子集（`CITATION NEEDED — 待人工核验`），转换为
单通道强度图，使协议是完全相同的而不只是类比的。

**指标。** 与 E1 完全相同。

**判定阈值。**

| 观察结果 | 动作 |
|---|---|
| COCO 上的差距远小于 CT 上的差距 | **继续** —— 该效应是 CT 特异的 |
| COCO 上复现出了 CT 上的差距 | **杀掉"CT 特异性"这一主张。** 最多只是一条关于 AMG 在单通道图像上的一般性注记；那篇 CT 论文并不存在 |

**为什么这比看起来更重要。** 没有 E4，评审可以说这个结果讲的是灰度图像
的一般规律。而那条反驳会在决定接收的关键时间已经花掉之后才落下来，
所以 E4 是一份便宜的保险。

**预算。** 约 2 GPU-h（**HYPOTHESIS**）。

---

## E5 —— SAM2 泛化性（可选）—— 状态：NOT RUN

用 SAM2 重跑 E1 与 E3。只有当两个模型都显示出解离时，才**继续**使用
"foundation segmenters"这种表述；否则明确把主张的范围限定在 SAM ViT-B，
并在标题里说明。相关评测背景：
arXiv 2408.11210（**VERIFIED PRIOR WORK**）。预算约 4–8 GPU-h（**HYPOTHESIS**）。

## E6 —— 失败案例定性检查 —— 状态：NOT RUN

金属伪影、增强扫描、极低剂量切片。不承载假设；它存在的意义是让论文
既展示等价性在哪里成立、也展示它在哪里失效。预算约 1 GPU-h（**HYPOTHESIS**）。

---

## 横切规则

1. **在 E1 之前预先注册切片清单。** 看到结果之后再挑切片，会把后续每一张
   卡片都变成对偏见的确认。
2. **每张卡片都报三个指标。** 任何卡片都不得只报其中一部分。
3. **有效性门禁未通过时不产出任何数字。** `counterfactual_profile`
   会抛异常而不是返回值；这是有意为之。
4. **预算都是 HYPOTHESIS。** `~2 GPU-h` 这个数字来自
   `evolution_summary.md`，是估计，永远不是测量。
5. **任何卡片都不得把 EXPECTED 改标为 ACTUAL。** 只有用真实权重在真实数据上
   跑出来的数字才成为 ACTUAL，而目前还不存在这样的数字。
