# 淘汰设想总结 (高层概览)

拥挤的灭杀区：以 MedSAM/adapter/LoRA-on-SAM 作为核心贡献；detector-box→SAM2 火灾检测 (ProFSAM)；正交 LoRA 持续学习 (InfLoRA)；oracle-box 评测类论文 (RClicks/BREPS)；仅微调解码器 (Gu et al.)；SAM2 中间切片协议 (Ma/Dong)；SAM alpha 预测头 (Matting Anything)；随机 LoRA 扰动 (VeRA)；CLIP 线性密集特征图 (SCLIP)；VLM 修复幻觉旗舰设想 (HalluSegBench)。

全程严禁的伪新颖性：模块堆叠、更换骨干网络、“apply X to medical”、添加额外的注意力机制。
