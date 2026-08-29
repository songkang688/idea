# O1/O2/O3 决策规则（Idea_03）

这条预先注册的规则负责把测量值转化为论文的主张。
实现为 `pipeline.classify_outcome` —— 一个不访问模型的纯函数，
因此可做单元测试、也可对外发布。读者可以把它套用到自己的数字上。

底层方法（受限解码、线性探针、DPO）的正式引用为
`CITATION NEEDED — 待人工核验`；见 `literature.md` §C。

## 1. 被测量的量

所有差距都是**base 减 chat**；为正表示 chat checkpoint 更差。

| 符号 | 定义 | 仍然存在的混淆因素 |
|---|---|---|
| \(g_{\mathrm{free}}\) | 自由生成下的 IoU 差距 | 文风包装、解析、解码策略 |
| \(g_{\mathrm{con}}\) | 语法受限下的 IoU 差距 | 解码策略 |
| \(g_{\mathrm{lik}}\) | 似然排序 acc@1 的差距 | **没有任何生成相关的混淆** |
| \(g_{\mathrm{probe}}\) | \((\mathrm{MAE}_{\mathrm{chat}} - \mathrm{MAE}_{\mathrm{base}})/s\)，按图像尺度归一化 | 探针容量、层的选择 |

\(g_{\mathrm{lik}}\) 是唯一在去掉生成环节后仍然成立的量，
这正是规则只把它当作决定性依据的原因。

## 2. 规则

取预先注册的容差 \(\tau = 0.02\)：

\[
\text{outcome}=
\begin{cases}
\textbf{refuse} & g_{\mathrm{lik}} \text{ 未被测量}\\[2pt]
\textbf{format (O1)} & g_{\mathrm{lik}} \le \tau \ \wedge\ (g_{\mathrm{free}} > \tau \vee g_{\mathrm{con}} > \tau)\\[2pt]
\textbf{none} & g_{\mathrm{lik}} \le \tau \ \wedge\ g_{\mathrm{free}} \le \tau \ \wedge\ g_{\mathrm{con}} \le \tau\\[2pt]
\textbf{representation (O3)} & g_{\mathrm{lik}} > \tau \ \wedge\ g_{\mathrm{probe}} > \tau\\[2pt]
\textbf{policy (O2)} & g_{\mathrm{lik}} > \tau \ \wedge\ g_{\mathrm{probe}} \le \tau
\end{cases}
\]

## 3. 为什么要有 refuse 这一支

没有 \(g_{\mathrm{lik}}\)，自由生成或受限生成得到的差距就无法与格式
混淆因素分离。只凭生成结果去报告一项"税"，是在这里发表错误结果最
容易的途径，而它正是那条预先注册的 kill 规则所针对的失效：
*"Kill if H1 fails under constrained decoding (formatting confound)."*

所以 `classify_outcome` 选择抛异常而不是猜。这份纪律在代码里，
不只在正文里，因为正文不会被执行。

## 4. 验证：往返测试

`data.make_pair` 可以通过降级被模拟的 chat 模型的不同部分，来植入四种
答案中的任意一种 —— `none`、`format`、`policy`、`representation`：

| 植入的模式 | 被降级的部分 | 预期特征 |
|---|---|---|
| `none` | 什么都不降 | 所有差距 ≈ 0 |
| `format` | 只降自由生成的文风包装 | \(g_{\mathrm{free}} > 0\)，\(g_{\mathrm{lik}} \approx 0\) |
| `policy` | 降解码器估计；token 完好 | \(g_{\mathrm{lik}} > 0\)，\(g_{\mathrm{probe}} \approx 0\) |
| `representation` | 视觉 token 也降 | \(g_{\mathrm{lik}} > 0\)，\(g_{\mathrm{probe}} > 0\) |

`run_smoke.py` 会逐个植入，若四种都不能往返还原就以非零状态退出。
一个连植入的答案都还原不出来的决策函数，绝不能拿去对准一个真实答案。
**这验证的是尺子，不是被测量的对象。**

## 5. 指标定义

**IoU。** 轴对齐框上的标准交并比。`parse_box` 会把颠倒的角点归一化，
使一个输出 `x2 y2 x1 y1` 的模型不会被当成定位失败来打分。

**解析失败率。** 输出中数字少于四个的比例。**始终单独报告**。
`mean_iou` 提供 `count_failures=True`（把失败当作 0）与
`False`（只统计可解析的）两种模式；**两者之差就是被量化出来的格式税**。
把解析失败折进均值里，正是让一个只是话多的 chat 模型看起来"不会定位"的原因。

**Rank acc@1。** 金标框排名高于全部 \(k \le 16\) 个干扰项的样本比例。
干扰项在两个 checkpoint 之间是**共享的** —— 否则似然差距可能反映的是
候选集更容易，而不是模型更好。

**探针 MAE。** 从冻结视觉 token 到框的 ridge 正则线性映射的坐标平均绝对
误差，在训练划分上拟合、在留出集上评测。

## 6. 探针为什么要加 ridge 正则

在训练划分很小、token 维度之间又相关的情况下，**不加正则**的最小二乘
拟合可以从噪声里还原出一个框。那样它就会对一个表征已被破坏的
checkpoint 报告"表征完好" —— 恰恰在 **O3** 为真时把规则偏向 **O2**，
而 O3 才是后果更重的那个发现。偏置列从不受惩罚。`reviewer_attacks.md`
的 C3 要求报告一次惩罚系数扫描，使结论可见地不依赖于单个超参数。

## 7. 已知的不完备之处

- **层的选择。** \(g_{\mathrm{probe}}\) 只在一个深度上测量。卡片 E3 会
  扫描各层；如果只在某一层出现差距，主张就降级为一份扫描报告。
- **探针容量。** 没有*线性*可解码性并不等于没有信息。如果线性探针下降
  而 MLP 探针没有下降，那么这个发现是
  *"信息仍在，但不再线性可及"* —— 它与 O3 不同，应如实这样报告，
  不得被折进 O3 里。
- **\(\tau\) 是一个全局单一容差。** 按指标分别设定容差在论证上会更站得住；
  0.02 是对全部四个差距预先注册的，且统一施加，因此它不可能被按结果调参。
