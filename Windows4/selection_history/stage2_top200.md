# Stage 2 → Top-200 候选池 (Windows4)

日期：2026-08-28。认知状态：**REVIEW JUDGMENT**，非实验事实。

来源：
- S 保留 90 项 ([Stage2 reviewer novelty](bc-8d9055cc-7185-56e7-9375-4b6a9fa5eeda))
- A1+B1 保留 80 项 ([Stage2 reviewer A1B1](bc-616dd955-2a7d-5b08-a53b-5ea8d7531a29))
- C1 保留 50 项 + 10 项复活 ([Stage2 reviewer C1 audit](bc-20f7911c-f82e-5689-8138-448cf5a6f2c1))

原始去重并集 = 225 项。剔除审计员已折叠合并至规范孪生设想的 25 行。**候选池大小：200 项。**

审计员警告 (已采纳)：跨批次*收敛属于相关的种子输出，而非独立复现*。Stage 3 将重复项视为单个假设处理。

## 剔除项 (已折叠合并，未丢失)

S-001→C1-038; S-016→C1-003; S-146→C1-057; S-196→C1-001; S-203→C1-060; S-286→C1-087; S-318→C1-025; S-361→C1-026; A1-006→C1-026; A1-008→C1-039; A1-015→A1-083; A1-026 (eng); A1-012 (eng, AB-killed but had leaked); A1-094→C1-038; B1-086→C1-057; C1-013 tooling-only; 以及 C1 审计折叠列表中列出的另外 9 个孪生项。

## Stage 3 的聚类主线 (约 50 个假设；ID 为代表项)

1. Oracle-prompt protocol — S-003, C1-115, A1-118
2. Tight-box image ablation — S-014, S-604
3. Nested-scale multimask — S-018, C1-061, A1-003
4. Negative-click asymmetry / paradox — S-005, A1-007, A1-062
5. Prompt-evolution scorer failure — S-007, S-347
6. Decoder-local medical gap — S-041, A1-034, S-044
7. Anisotropy vs “medical” 3D — S-042, A1-039
8. Pretrain-harm small-n — S-052, C1-087
9. Nested anatomy objectness — S-054, A1-040
10. Patient-split leakage — S-068, C1-004 (C1-004 作为已知事实被淘汰；保留 S-068 作为实验)
11. SAM2 shuffle / memory-off / recency — S-073, S-079, S-081, A1-017
12. One-prompt drift — S-074, A1-018
13. Smoke as alpha / metric reversal — S-096, S-097, A1-046, A1-055
14. Smoke inter-rater ceiling — S-102, A1-054, C1-016
15. Matting→smoke transfer — S-103
16. Detector-matched fire SAM — S-126, A1-071
17. Time-to-alarm vs mIoU — S-109, S-134
18. PEFT tax on promptability — S-141, C1-097, C1-065
19. Random-LoRA null — S-148
20. Protocol forgetting — S-176, C1-065, A1-109
21. Forgetting locus decoder — S-177, C1-062
22. Plasticity too small — S-183, C1-082
23. FT calibration tax — C1-025, C1-031, C1-037
24. VLM prior harms rare disease — S-228, S-240, B1-107
25. Human vs simulated clicks — A1-105, C1-003, C1-111
26. Patch-grid aliasing — A1-002
27. Topology / holes prior — A1-004
28. Split/merge masklets — A1-027
29. Glass refraction / warp — A1-058, A1-063, A1-067
30. Scale floor ~16px — A1-073
31. Prompt-distribution eval — A1-118, A1-091
32. LoRA placement vs error type — A1-107
33. Encoder–decoder contract drift — A1-108, C1-067
34. AL dead under VFM init — B1-011, B1-025
35. Copy-paste ≥ generative — B1-051
36. Histogram matching explains UDA — B1-061
37. Support-set variance > method — B1-074
38. FSS background shortcut — B1-079
39. CLIP dense linear misalignment — B1-097
40. Feature TV vs boundary — B1-111
41. SA-1B leakage — C1-001
42. Annotator noise floor — C1-016
43. PEFT vs tuned full-FT — C1-053
44. Data-size PEFT crossover — C1-057
45. Gain–retention frontier — C1-110
46. Dose-insensitive contour error — S-513
47. Partial-volume as alpha — S-395
48. Channel-lift vs LoRA grayscale — A1-033 (复活)
49. Depth-edge auto-prompt glass — A1-060 (复活)
50. Embedding-scale granularity knob — A1-101 (复活)

## 完整 200 个 ID

参见 `stage2_top200_ids.txt`。
