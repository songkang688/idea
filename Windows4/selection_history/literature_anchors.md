# 文献锚点 (仅限真实论文 — 用于后续新颖性攻击)

状态：**KNOWN / EVIDENCE from public papers**。并非声称 Windows4 实验已经存在。

## SAM / 医疗 / 提示敏感性

- Kirillov et al., *Segment Anything*, ICCV 2023 / arXiv:2304.02643. 基础可提示分割模型。
- Ravi et al., *SAM 2: Segment Anything in Images and Videos*, 2024.
- Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024. 证据：提示类型敏感性；框提示通常优于点提示；微调有帮助；在跨数据集上表现不稳定。
- He et al., arXiv:2304.09324. Zero-shot SAM 与医疗专用模型的对比；在小目标 / 低对比度 / 3D 数据上表现较差。
- Ma & Wang, MedSAM (在医学图像上微调 SAM)。相比原生 SAM 带来大幅 Dice 提升 —— **因此 “fine-tune SAM on medical” 并非新颖设想**。
- Wu et al., Medical SAM Adapter —— 用于医学 SAM 的 Adapter PEFT。**“Add adapters to SAM for medical” 已非常拥挤。**
- SAMPOT, arXiv:2310.17128. 任务驱动的提示位置演化。**测试阶段的提示优化领域并非空白。**
- Yao et al. 2023 FNPC: 提示扰动不确定性 + 噪声超声图像上的 FN/FP 控制 (无需训练)。

## SAM2 医疗应用

- MedSAM-2 (arXiv:2408.00874): 将 2D/3D 视为视频处理；自排序记忆库；跨图像单提示。
- BioSAM-2 (arXiv:2408.03286): SAM-2 无法直接使用；存在领域差距 + 缺少语义类别关联。
- Zhang survey arXiv:2408.12889: SAM2 医疗视频相比 3D 放射影像更接近；仍存在领域差距。

## 烟雾 / 火灾 / 透明物体

- ProFSAM / Ugwu & Zhang, arXiv:2510.21782: SAM2 + 检测框用于火灾；**detector-prompted SAM2 for fire 设想已被占用**。
- Density-aware progressive smoke segmentation using SAM for background (Pattern Recognition; “Generate-Transfer-Evolve”). **SAM-as-background-prior for smoke 设想已被占用；密度标签仍然薄弱。**

## PEFT / 遗忘 (视觉领域)

- Hu et al., LoRA, ICLR 2022.
- InfLoRA, CVPR 2024: 正交子空间以减少新任务干扰。
- DualLoRA / replay-free continual LoRA with dynamic memory (arXiv:2411.00623).
- 对 Windows4 的启示：**“orthogonal LoRA for CL” 设想已被占用**。剩余更有价值的问题可能在于 *dense prediction*（分割解码器遗忘）、*promptable* 模型，或者 *when PEFT hurts zero-shot*。

## 主管启示 (HYPOTHESIS, not fact)

拥挤的灭杀区 (需要比 “adapt SAM” 更犀利的问题)：
1. 在医学图像上微调 SAM/SAM2
2. 在 SAM 上应用 Adapter / LoRA
3. 检测框 → SAM2 用于火灾
4. 用于分类持续学习的正交 LoRA

在 Stage 3 中值得进行压力测试的潜在突破切入点 (仍可能被淘汰)：
1. **将掩码分歧作为科学研究对象** (提示/模型偶然不确定性结构)，而非作为事后处理技巧
2. **基础模型自适应何时会恶化提示域外或分布外的校准能力**
3. **无语义 SAM2 记忆机制 vs 类别一致的医学跟踪** (MedSAM-2 已存在 —— 需要提出*不同*的假设)
4. **半透明 / 连续密度标签** 作为评估手段，而非又一个 SAM 包装器
5. **Mask 解码器 / 提示编码器中的 PEFT 干扰**，而非分类器头部
