# Stage 1 raw ideas batch X

Count: 10

### IDEA-X-0001
- Idea: Exclusion-region prompting: Amorphous targets need prompts that specify what is NOT the target.
- Problem: Amorphous targets need prompts that specify what is NOT the target.
- Hypothesis: Exclusion-region prompts raise NSD on smoke/infiltrative tumor without encoder FT, and do not help COCO objects.
- Important: Prompt semantics, not weights.
- Novel: Closest work only compares point vs box.
- MinExp: Paint a negative ring around smoke; compare to GT-box SAM.
- Risk: Users will not draw rings.
- Cluster: Exclusion-region prompting

### IDEA-X-0002
- Idea: Density decoder on frozen SAM: Replace binary mask decoder with density regression head on frozen embeddings.
- Problem: Replace binary mask decoder with density regression head on frozen embeddings.
- Hypothesis: Frozen SAM tokens + 1x1 conv density head beats prompted SAM on smoke IoU after matching annotation time.
- Important: Objectness decoder is the bug.
- Novel: Fire SAM2 papers still use binary masks.
- MinExp: Train 1x1 head on 200 smoke frames.
- Risk: Density GT is itself ambiguous.
- Cluster: Density decoder on frozen SAM

### IDEA-X-0003
- Idea: IoU-token reject option: Use SAM IoU head as a selective-prediction gate.
- Problem: Use SAM IoU head as a selective-prediction gate.
- Hypothesis: Thresholding IoU tokens raises risk-coverage Dice more than Med-SA of equal extra params on amorphous tests.
- Important: Calibration as method.
- Novel: Production blogs mention the score; papers rarely use risk-coverage.
- MinExp: Plot risk-coverage on Trans10K and a smoke set.
- Risk: IoU head may be uninformative.
- Cluster: IoU-token reject option

### IDEA-X-0004
- Idea: Spectral LoRA audit: FFT of (LoRA-adapted − frozen) feature maps.
- Problem: FFT of (LoRA-adapted − frozen) feature maps.
- Hypothesis: >80% energy of LoRA delta is below a spatial-frequency cutoff that cannot represent 1-px boundaries.
- Important: Explains why LoRA matches Dice not NSD.
- Novel: LoRA-MedSAM reports Dice only.
- MinExp: One GPU: save feature deltas on 64 images, FFT.
- Risk: Need careful layer choice.
- Cluster: Spectral LoRA audit

### IDEA-X-0005
- Idea: Equal-annotation-minute bakeoff: nnU-Net vs SAM-PEFT vs linear probe under fixed labeling minutes.
- Problem: nnU-Net vs SAM-PEFT vs linear probe under fixed labeling minutes.
- Hypothesis: VFM advantage disappears at 30–120 annotation minutes on a new organ.
- Important: Compute/label fairness.
- Novel: Papers compare to fully trained nnU-Net.
- MinExp: Time a rater; train all three.
- Risk: Human timing noisy.
- Cluster: Equal-annotation-minute bakeoff

### IDEA-X-0006
- Idea: Prompt-tightness confound: Re-run SAM prompt papers with boxes jittered to matched tightness.
- Problem: Re-run SAM prompt papers with boxes jittered to matched tightness.
- Hypothesis: Published point-vs-box gaps shrink >50% after tightness matching.
- Important: Confounder.
- Novel: Fire SAM2 uses strategic boxes without tightness control.
- MinExp: Jitter boxes to target IoU.
- Risk: GT boxes already tight.
- Cluster: Prompt-tightness confound

### IDEA-X-0007
- Idea: Replay for promptability: Mix 1% synthetic click-segmentation while medical PEFT.
- Problem: Mix 1% synthetic click-segmentation while medical PEFT.
- Hypothesis: Replay preserves COCO-prompt mIoU with <1 Dice drop on the medical target.
- Important: Forgetting of the interface.
- Novel: Med-SA claims PEFT avoids forgetting without measuring promptable zero-shot.
- MinExp: COCO-proxy 200 images + LoRA.
- Risk: Synthetic clicks not SA-1B.
- Cluster: Replay for promptability

### IDEA-X-0008
- Idea: Rater-as-model: Train on rater A, test on rater B.
- Problem: Train on rater A, test on rater B.
- Hypothesis: VFM PEFT gains vanish under rater shift while nnU-Net does too; 'foundation' is not more rater-robust.
- Important: Aleatoric cap.
- Novel: LIDC multi-rater exists but unused as the test.
- MinExp: LIDC 4 raters.
- Risk: May be a known ceiling.
- Cluster: Rater-as-model

### IDEA-X-0009
- Idea: Patch/lesion diameter law: Failure probability ~ f(lesion_diameter / patch_size).
- Problem: Failure probability ~ f(lesion_diameter / patch_size).
- Hypothesis: A simple scaling law predicts SAM failure better than domain tags.
- Important: Mechanism.
- Novel: 2412.04243 uses tree-likeness/texture; diameter/patch is simpler.
- MinExp: Bin errors by diameter/patch.
- Risk: May be too simple for reviewers.
- Cluster: Patch/lesion diameter law

### IDEA-X-0010
- Idea: Language does not group pixels: CLIP/VLM text features improve class presence AUC but not mask NSD when the visual grouper is frozen.
- Problem: CLIP/VLM text features improve class presence AUC but not mask NSD when the visual grouper is frozen.
- Hypothesis: Multimodal supervision is recognition not segmentation.
- Important: VLM-for-dense hype.
- Novel: Open-vocab seg papers entangle both.
- MinExp: Freeze grouper; swap text.
- Risk: Hard to freeze fairly.
- Cluster: Language does not group pixels
