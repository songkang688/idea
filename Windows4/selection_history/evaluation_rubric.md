# Stage 2+ 评估标准 (Windows4)

**切勿**按平均分排序。采用决策规则。

## 评估维度 (除特别注明外为 1–5 分)

1. Novelty (科学上的新颖性，而非架构层面的新颖性)
2. Significance (如果我们是对的，推翻了谁的观点？)
3. Scientific question clarity (科学问题的清晰度)
4. Technical soundness (技术合理性)
5. Feasibility (可行性：单个实验室，几周而非几年)
6. Compute (计算量：越低则 ROI 越好)
7. Dataset availability (数据集可用性)
8. Baseline availability (基线可用性)
9. Likelihood already published (已被发表的可能性：越高越差)
10. Experimental clarity / falsifiability (实验清晰度 / 可证伪性)
11. Venue potential (CVPR/ICCV/ECCV/MICCAI)，体现为*故事质量*，而非追求名气
12. Risk (风险)
13. Upside (潜在收益)
14. Research ROI = (upside × falsifiability) / (compute × calendar friction)

## 存活规则 (保护设想避免因平均分过低而被误杀)

- 高风险、高收益且具备低成本 Killer Experiment
- 简洁的反直觉假设
- 评审员之间存在极大分歧
- 可在 <1 GPU-day 内被证伪/击毙

## 淘汰规则 (Kill rules)

- 核心新颖性为 “new module”
- 假设不可证伪
- Killer experiment 需要重新预训练基础模型
- 最接近的先前工作已经运行过相同的实验 (Stage 3)
- Reviewer #2 的攻击无法通过实验予以回应 (Stage 4)

## Stage 3 立场

默认假设：**this idea has already been done.** 代理致力于扼杀新颖性，而非夸赞新颖性。
若存在部分重叠：**mutate**（变异设想），切勿自动扼杀。

## Stage 4 立场

默认假设：**reject the paper.** 存活的充要条件是有可行的实验能够平息质疑。
