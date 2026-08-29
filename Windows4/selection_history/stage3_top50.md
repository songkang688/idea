# Stage 3 → 约 50 个存活假设 (Windows4)

日期：2026-08-28。经对抗性先前工作搜索 (3 位独立刺客评审) 之后。
认知状态：**REVIEW JUDGMENT**。`stage3_kill_*.md` 中的引用均由对应代理声称已通过网络验证；Stage 4 仍须将最接近的工作视为攻击面。

## 记分板 (Scoreboard)

| File | KILL | MUTATE | SURVIVE |
|------|------|--------|---------|
| `stage3_kill_sam_eval.md` | 9 clusters | 3 | 3 |
| `stage3_kill_medical_smoke.md` | 15 IDs | 8 | 5 |
| `stage3_kill_peft_vlm.md` | 7 clusters | 6 | 5 |

承重淘汰项：RClicks/BREPS 覆盖了 oracle-prompt / human-click / prompt-distribution / box-jitter；Gu et al. 2404.09957 覆盖了仅微调解码器的 MedSAM 及大量 PEFT 复现工作；MedSAM-2 / Dong et al. 覆盖了 SAM2 视作视频的提示切片设想；ProFSAM 覆盖了 detector+SAM2 火灾检测；Label Convergence / COCO-ReM 覆盖了仅以噪声下限为主题的论文。

## Stage-4 攻击列表 (合并后的唯一样本论文，约 24 篇；展开分支后约 50 行)

### SURVIVE (旗舰设想)

1. **P14** S-014/S-604 — 紧致框内消融*图像* token；提示保持固定。(SAM 真正具备视觉感知 vs 框到掩码插值器)
2. **P101** A1-101 — 将提示嵌入范数作为免训练的粒度调节旋钮 (与 GraCo 的差异)
3. **P079** S-079 — 探测 SAM2 记忆机制：位置坍缩 vs 外观坍缩
4. **P103** S-103 — 人像抠图预训练 → 烟雾迁移 (迁移学习，而非 SAM 包装器)
5. **P063** A1-063 + A1-067 — 特征流 / 特征扭曲 vs 光学折射 (玻璃)
6. **P060** A1-060 — 针对玻璃的深度边缘自动提示 (需要 RGB 边缘对照控制)
7. **P065** C1-065 + C1-061 — 提示类型行为遗忘 + 多掩码多样性坍缩
8. **P177** S-177 + C1-062 — 遗忘发生位点：解码器 vs 编码器，分层拼接
9. **P107** A1-107 — Attention-LoRA vs MLP-LoRA 错误类型分离
10. **P107v** B1-107 — 图像修复消除目标；幽灵密集掩码 (VLM 幻觉)
11. **P079f** B1-079 — FSS 背景置换作弊
12. **P051** B1-051 — 在对齐 GPU 学时下 Copy-paste vs 扩散模型

### MUTATE (仍留在候选池中)

13. **P096** S-096 + S-102 — 烟雾评测指标反转 (Dice vs alpha/上限)，而非又一个分割模型
14. **P044** S-044/A1-034 — 超声/CT 上的去斑/窗宽调整 vs LoRA (预处理证伪对照)
15. **P042** S-042 — 各向异性混淆因素 vs “医疗 3D” (而非一个新的 SAM2)
16. **P040** A1-040 — 边界扩散性欠分割定律
17. **P007** S-007 — 测试阶段提示演化的评分器有效性 (而非反 SAMPOT 的口号)
18. **P004** A1-004 — 孔洞：先验 vs COCO 惯例 vs 后处理
19. **P031** C1-031 + C1-025/037 — 全微调导致 IoU 头与掩码质量失步；校准/鲁棒性前沿
20. **P052** S-052 — 变异为小样本量下的目标性先验损害 (而非泛泛的基础模型损害)
21. **P110** C1-110 — 附加于 P065 的报告协议，而非独立的基准套件论文
22. **P108** A1-108/C1-067 — 漂移统计量*预测*随后的 zero-shot 性能下降
23. **P228** S-228 — 频率受控的 VLM 先验 vs 非典型外观 (密集预测)
24. **P061u** B1-061 — 并入析因风格 × 自训练 (而非 FDA 混编)
25. **P082** C1-082 + S-183 — 阈值假象 + 低可塑性把关者 (优先运行，可能会击毙遗忘主线)
26. **P001** C1-001 — SA-1B 近似重复项审计 (把关项；众数结局 = 无显著差异 null)

### 从 Top-50 中剔除的项目 (仅作规范清理)

Oracle boxes, simulated clicks, MedSAM decoder-only, SAM2 prompt-slice, smoke-as-instance ontology, time-to-alarm, dose-volume, partial-volume-as-alpha, random-LoRA-as-paper, AL-dead-under-DINOv2, CLIP linear map, channel-lift, patch-grid aliasing。

## 下一步

Stage 4 Reviewer #2：逐一拒绝 P14–P061u，除非有切实可行的实验能够平息质疑。
