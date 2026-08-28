# Stage 1 ingest — SEG slice (Windows1)

Source agent: bc-45a638f2-6677-5cef-9014-227b460e4747
Status: SUCCESS. 365 ideas SEG-0001–SEG-0365. Claims are HYPOTHESIS unless tagged.

## Counts
- BOUND 25, SMALL 20, AMORPH 25, MED 30, SHIFT 25, FSZS 20, PROMPT 20
- WEAK 25, SYNTH 20, UNC 25, TAIL 15, ANNOT 20, VLM 20, EVAL 25, DET 20, ROBUST 15, AMBIG 15

## Top 30 keepers (priority for Stage 2)
SEG-0002 noise floor of human boundary jitter
SEG-0019 evidence-free boundary hallucination via local masking
SEG-0027 small-object AP is label-noise-bound
SEG-0033 context-to-object evidence ratio vs size → hallucination
SEG-0046 smoke as optical-density regression not binary mask
SEG-0049 transparent objects as refraction warp discontinuities
SEG-0054 pre-visibility smoke from temporal flicker spectra
SEG-0071 model-expert agreement vs expert-expert; style-fitting
SEG-0074 infiltration probability fields vs contours
SEG-0077 scanner-fingerprint predicts site drop
SEG-0081 silent-failure via anatomical plausibility vs softmax
SEG-0085 lesion-suppression by denoising/SR pipelines
SEG-0100 counterfactual pathology insertion sensitivity atlases
SEG-0101 interventional domain-gap factor decomposition
SEG-0103 UDA go/no-go statistic
SEG-0113 deployment contract: predict mIoU from unlabeled stream
SEG-0125 self-training error-amplification law from round 1
SEG-0136 per-class few-shot scaling laws from one shot
SEG-0185 frozen dense probes predict fine-tune rank at ~1% compute
SEG-0191 factorial photorealism vs layout realism for synth data
SEG-0193 generated-data contamination of test sets
SEG-0211 region-level calibration replacing pixel ECE
SEG-0215 conformal mask sets with correct exchangeable unit
SEG-0252 model-in-the-loop label ecology / convention amplification
SEG-0265 validated label-error discovery instrument
SEG-0275 temporal-holdout open-vocab (post-cutoff names)
SEG-0292 adjudicated relabeling → benchmark noise ceilings
SEG-0309 seed/checkpoint variance vs published gaps
SEG-0318 missing-annotation rates; PU-calibrated detection
SEG-0338 temporal instability as label-free error detector

## Protected high-risk (do not kill early)
SEG-0046, 0049, 0054, 0071, 0074, 0100, 0103, 0185, 0193, 0252, 0275, 0292, 0353

## Next uncertainty (supervisor)
Need independent VFM and ASM pools (≥1000 total). Then adversarial prior-work on keepers.
Need Stage 2 scores on SEG keepers while other pools generate.
