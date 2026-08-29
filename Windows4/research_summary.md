# Windows4 研究总结

**KNOWN：** SAM 是一个可提示的分割器（Kirillov et al., ICCV 2023）；医学／烟雾／火焰方向的适配已经很拥挤；Gu et al.（arXiv:2404.09957）已经做过医学 SAM 上"仅解码器 vs 编码器 PEFT"的对比；RClicks/BREPS 已经攻击过 oracle 提示；HalluSegBench 抢先做掉了 VLM inpaint 幻觉那个旗舰选题。

**HYPOTHESIS（Idea_01）：** 对于 thing 类物体，紧致框内部的图像证据对 SAM 取得高 Dice *并非*必要条件。

**HYPOTHESIS（Idea_02）：** 在域内 Dice 被调平的前提下，混合提示微调能保住单一协议微调会丢掉的零样本提示技能。

**HYPOTHESIS（Idea_03）：** 为 alpha matting 训练的编码器在真实烟雾上的迁移效果优于为 COCO 式二值掩码训练的编码器，且在 matting 指标下模型排名会翻转。

`Idea_*/experiments.md` 里的所有数字都是 **EXPECTED**，此处从未实测。
