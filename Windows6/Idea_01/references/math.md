# 数学定义（Idea_01）

三个预先注册的指标与两个诊断量的定义。
实现在 `src/amgclust/metrics.py`；下文断言的每一条性质都有
`tests/test_smoke.py` 中的测试覆盖。

这些经典构造的正式引用为
`CITATION NEEDED — 待人工核验`（见 `literature.md` §C）—— 没有一条能与
`selection_history/literature_anchors.md` 核对上，而凭记忆重建的 bibtex
条目比留一个看得见的空洞更糟。

## 记号

\(\mathcal{A}\) 是 AMG 的掩码清单，\(\mathcal{B}\) 是某个基线掩码集合。
AMG 返回的是**嵌套、互相重叠**的掩码；聚类器返回的是 \(k\) 类的一个
**划分**。这两种对象形状不同，下文的大部分小心都是为了不让这种
差异伪装成（不）一致。

## 1. Hungarian IoU —— 匹配对的质量

\[
\mathrm{IoU}_{\mathrm{hung}}(\mathcal{A},\mathcal{B})
=\frac{1}{\min(|\mathcal{A}|,|\mathcal{B}|)}
\sum_{(A,B)\in \pi^{\star}} \mathrm{IoU}(A,B),
\qquad
\pi^{\star}=\arg\max_{\pi \text{ one-to-one}} \sum_{(A,B)\in\pi}\mathrm{IoU}(A,B)
\]

精确求解。有 `scipy.optimize.linear_sum_assignment` 时用它，
否则用纯 numpy 的 \(O(n^3)\) 增广路求解器 —— 因此即便只有 numpy，
这个指标也是最优解而不是贪心解。

**为什么分母是 \(\min(|\mathcal{A}|,|\mathcal{B}|)\) 而不是 \(|\mathcal{A}|\)。**
最初的原型除以的是 \(|\mathcal{A}|\)，这会把基数差异折进一致性分数里：当
 \(|\mathcal{A}|\approx 50\) 个嵌套 AMG 掩码对上 \(k=8\) 个聚类时，最多只有
8 对能匹配，其余 42 个贡献零，于是一个结构上完美的子集匹配算出来只有
约 0.03。在 W6-T3 期间于合成 phantom 上实测，发生的正是这件事。基数
不匹配是一个真实差异 —— 所以它被显式报告（§4），而不是被夹带进一致性
数字里。

**为什么不用贪心。** 贪心匹配先取局部最优的一对，可能被迫留下很差的
残余，于是一个过分割的方法可以靠匹配*顺序*拿到好分数。
`test_hungarian_beats_greedy_on_a_trap` 把这一点钉住了。

性质：\(\mathrm{IoU}_{\mathrm{hung}}(\mathcal{A},\mathcal{A})=1\)；
互不相交的集合得 0。

## 2. Adjusted Rand Index —— 划分一致性

先把每个掩码集合画成一张像素标签图，然后在列联表
\(n_{ij}\) 上计算（行和为 \(a_i\)，列和为 \(b_j\)，共 \(N\) 个像素）：

\[
\mathrm{ARI}=
\frac{\sum_{ij}\binom{n_{ij}}{2}-\Big[\sum_i\binom{a_i}{2}\sum_j\binom{b_j}{2}\Big]\big/\binom{N}{2}}
{\tfrac{1}{2}\Big[\sum_i\binom{a_i}{2}+\sum_j\binom{b_j}{2}\Big]-\Big[\sum_i\binom{a_i}{2}\sum_j\binom{b_j}{2}\Big]\big/\binom{N}{2}}
\]

已做随机性校正：标签完全相同时为 1，相互独立时约为 0。两者都有测试钉住。

**绘制规则。** 重叠处归属于**更小的**掩码
（`masks_to_label_map` 按从大到小绘制，因此更小的掩码落在上层），
否则一个嵌套的 AMG 子掩码会被它自己的父掩码擦掉，标签图就会歪曲
清单的实际构成。标签 0 表示未分配。

## 3. Boundary-F —— 轮廓位置

边界像素定义为其 4 邻域中含有不同标签的像素。
取容差 \(\tau\) 像素（默认 2），\(\delta_\tau\) 为膨胀算子：

\[
P=\frac{|\,\partial\mathcal{A}\cap\delta_\tau(\partial\mathcal{B})\,|}{|\partial\mathcal{A}|},\quad
R=\frac{|\,\partial\mathcal{B}\cap\delta_\tau(\partial\mathcal{A})\,|}{|\partial\mathcal{B}|},\quad
F=\frac{2PR}{P+R}
\]

**EXPECTED（`proposal.md` §19）：** 它会是三个指标中区分力最弱的一个，
因为强度聚类器和超像素都会把边放在高梯度位置上。但仍然照样报告。
一个预先注册的指标如果结果证明没有信息量，就如实报告它没有信息量，
而不是把它删掉。

## 4. 诊断量 —— 只报告，不承载假设

**Coverage IoU**（有方向的多对一 —— 即最初那个集合公式）：

\[
\mathrm{IoU}_{\mathrm{cov}}(\mathcal{A},\mathcal{B})=\frac{1}{|\mathcal{A}|}\sum_{A\in\mathcal{A}}\max_{B\in\mathcal{B}}\mathrm{IoU}(A,B)
\]

它问的是"每个 AMG 掩码是否都能被*某个*聚类解释？"，而不是"两个集合能否
配成对？"。它不对称：
\(\mathrm{IoU}_{\mathrm{cov}}(\mathcal{A},\mathcal{B})\neq\mathrm{IoU}_{\mathrm{cov}}(\mathcal{B},\mathcal{A})\)。

**基数比** \(|\mathcal{A}|/|\mathcal{B}|\)。每一行都报告，这样任何读者都不会
把一个计数假象误认为一致性。

## 5. 干预

**强度重映射。** \(f\) 在 \([\,\min I,\max I\,]\) 上严格单调；默认是在
归一化区间上的 gamma 映射。单调性意味着像素值的*次序*被保持，
因此即便对比度被重新分配，边的**位置**依然存留。
`check_remap_is_monotone` 是在实际输出上核验这一点，而不是信任参数化，
并且 \(\gamma \le 0\) 时 `intensity_remap` 会抛异常。

**纹理置乱。** 在每个 \(t\times t\) 的小块 \(T\) 上：置换残差
\(T-\bar{T}\) 再把 \(\bar{T}\) 加回去，因此 \(\bar{T}\) 被精确保持。
`check_shuffle_preserves_tile_means` 以 1e-9 的精度核验它。正是这项检查
才让我们有资格把这条臂称为"保持强度不变"；没有它，任何 AMG 的响应
都可能其实是对强度的响应。

**读出方式。** 令 \(s_{\bullet}=\mathrm{IoU}_{\mathrm{hung}}(\mathcal{A}_{\text{orig}},\mathcal{A}_{\bullet})\)，
机制性主张需要 \(s_{\mathrm{int}} \ll s_{\mathrm{tex}}\)。

**已知的不完备之处（`reviewer_attacks.md` 中的 C1）。** 两条臂在高频能量上
并未对齐：置乱残差会提高高频能量，而区域增长类方法在噪声下会碎裂，
其原因与 objectness 无关。小块尺寸扫描 \(t\in\{4,8,16\}\) 能检测出这种
失效 —— 方向反转即判该臂无效 —— 但并不*消除*这个混淆因素。一个
噪声对齐的设计会更有力，而目前尚未规定这样的设计。

## 6. 没有被训练的损失函数

Idea_01 里任何地方都没有训练。聚类是在标量 HU（或做过窗宽窗位的
8 位图像）上做 k-means / multi-Otsu / GMM；SLIC 是在联合空间
\((x, y, \text{intensity})\) 上做 k-means。没有任何东西是拟合标签得到的。
