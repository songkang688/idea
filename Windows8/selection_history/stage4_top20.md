# stage4_top20.md
count=19

- IDEA-X-0001 | IDEA-X-0001 | hand | mixed | Exclusion-region prompting: Amorphous targets need prompts that specify what is NOT the target.
- IDEA-X-0002 | IDEA-X-0002 | hand | mixed | Density decoder on frozen SAM: Replace binary mask decoder with density regression head on frozen embeddings.
- IDEA-X-0003 | IDEA-X-0003 | hand | mixed | IoU-token reject option: Use SAM IoU head as a selective-prediction gate.
- IDEA-X-0004 | IDEA-X-0004 | hand | mixed | Spectral LoRA audit: FFT of (LoRA-adapted − frozen) feature maps.
- IDEA-X-0005 | IDEA-X-0005 | hand | mixed | Equal-annotation-minute bakeoff: nnU-Net vs SAM-PEFT vs linear probe under fixed labeling minutes.
- IDEA-X-0006 | IDEA-X-0006 | hand | mixed | Prompt-tightness confound: Re-run SAM prompt papers with boxes jittered to matched tightness.
- IDEA-X-0007 | IDEA-X-0007 | hand | mixed | Replay for promptability: Mix 1% synthetic click-segmentation while medical PEFT.
- IDEA-X-0008 | IDEA-X-0008 | hand | mixed | Rater-as-model: Train on rater A, test on rater B.
- IDEA-X-0009 | IDEA-X-0009 | hand | mixed | Patch/lesion diameter law: Failure probability ~ f(lesion_diameter / patch_size).
- IDEA-X-0010 | IDEA-X-0010 | hand | mixed | Language does not group pixels: CLIP/VLM text features improve class presence AUC but not mask NSD when the visual grouper is frozen.
- IDEA-A-0001 | SAM-OBJECTNESS | invert | natural-COCO-objects | SAM-OBJECTNESS on natural-COCO-objects: SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features.
- IDEA-A-0022 | SAM-TEXTURE | invert | natural-COCO-objects | SAM-TEXTURE on natural-COCO-objects: SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity.
- IDEA-A-0043 | SAM-PROMPT-GEOM | invert | natural-COCO-objects | SAM-PROMPT-GEOM on natural-COCO-objects: Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a unive
- IDEA-A-0064 | SAM-IOU-CAL | invert | natural-COCO-objects | SAM-IOU-CAL on natural-COCO-objects: SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks.
- IDEA-A-0085 | SAM-NEGCLICK | invert | natural-COCO-objects | SAM-NEGCLICK on natural-COCO-objects: Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support.
- IDEA-A-0106 | SAM-MULTIMASK | invert | natural-COCO-objects | SAM-MULTIMASK on natural-COCO-objects: Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO.
- IDEA-A-0127 | SAM2-MEMORY | invert | natural-COCO-objects | SAM2-MEMORY on natural-COCO-objects: SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes.
- IDEA-A-0169 | HQ-BOUNDARY | invert | natural-COCO-objects | HQ-BOUNDARY on natural-COCO-objects: HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries.
- IDEA-A-0190 | FT-FORGET | invert | natural-COCO-objects | FT-FORGET on natural-COCO-objects: Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities.