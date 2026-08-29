# Literature Anchors (real papers only — for later novelty attack)

Status: **KNOWN / EVIDENCE from public papers**. Not a claim that Windows4 experiments exist.

## SAM / medical / prompt sensitivity

- Kirillov et al., *Segment Anything*, ICCV 2023 / arXiv:2304.02643. Foundation promptable segmenter.
- Ravi et al., *SAM 2: Segment Anything in Images and Videos*, 2024.
- Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024. Evidence: prompt-type sensitivity; box often better than point; fine-tune helps; instability across datasets.
- He et al., arXiv:2304.09324. Zero-shot SAM vs medical specialists; worse on small / low-contrast / 3D.
- Ma & Wang, MedSAM (fine-tune SAM on medical). Large Dice lift vs vanilla SAM — **so “fine-tune SAM on medical” is NOT novel**.
- Wu et al., Medical SAM Adapter — adapter PEFT for SAM in medical. **“Add adapters to SAM for medical” is crowded.**
- SAMPOT, arXiv:2310.17128. Task-driven prompt location evolution. **Prompt optimization at test time is not empty.**
- Yao et al. 2023 FNPC: prompt-perturbation uncertainty + FN/FP control on noisy ultrasound (training-free).

## SAM2 medical

- MedSAM-2 (arXiv:2408.00874): treat 2D/3D as video; self-sorting memory bank; one-prompt across images.
- BioSAM-2 (arXiv:2408.03286): SAM-2 not directly usable; domain gap + no semantic class association.
- Zhang survey arXiv:2408.12889: SAM2 medical video closer than 3D radiology; still domain gap.

## Smoke / fire / transparent

- ProFSAM / Ugwu & Zhang, arXiv:2510.21782: SAM2 + detector boxes for fire; **detector-prompted SAM2 for fire is taken**.
- Density-aware progressive smoke segmentation using SAM for background (Pattern Recognition; “Generate-Transfer-Evolve”). **SAM-as-background-prior for smoke is taken; density labels still weak.**

## PEFT / forgetting (vision)

- Hu et al., LoRA, ICLR 2022.
- InfLoRA, CVPR 2024: orthogonal subspace to reduce new-task interference.
- DualLoRA / replay-free continual LoRA with dynamic memory (arXiv:2411.00623).
- Implication for Windows4: **“orthogonal LoRA for CL” is taken**. Remaining questions are more likely *dense prediction* (segmentation decoder forgetting), *promptable* models, or *when PEFT hurts zero-shot*.

## Supervisor implication (HYPOTHESIS, not fact)

Crowded kill-zones (need a sharper question than “adapt SAM”):
1. Fine-tune SAM/SAM2 on medical
2. Adapter / LoRA on SAM
3. Detector boxes → SAM2 for fire
4. Orthogonal LoRA for classification CL

Open-looking wedges to stress-test in Stage 3 (still may die):
1. **Mask disagreement as a scientific object** (prompt/model aleatoric structure), not as a post-hoc trick
2. **When foundation-model adaptation degrades out-of-prompt or out-of-domain calibration**
3. **Semantic-less SAM2 memory vs class-consistent medical tracking** (MedSAM-2 exists — need a *different* hypothesis)
4. **Semi-transparent / density-continuous labels** as evaluation, not another SAM wrapper
5. **PEFT interference in mask decoders / prompt encoders**, not classifier heads
