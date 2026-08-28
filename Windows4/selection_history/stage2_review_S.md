# Stage 2 Review — S-series (1000→200), Reviewer bias: novelty assassin

Scope: S-001..S-720 from `Windows4/selection_history/stage1_supervisor_seed.md` and `stage1_supervisor_seed_2.md`.
Kill priority: module-stacking, "apply X to medical", backbone/loss swaps, SAM-adapter/MedSAM/ProFSAM/InfLoRA clone lanes.
Protect priority: cheap-to-falsify probes and high-risk/high-reward scientific questions.
Meta entries (S-638–S-665 kill/protect/cheap pointers, S-712–S-720 process) were resolved to their underlying IDs and not kept as separate ideas.

## Keep (max 90)

| ID | 1-line reason | Novelty 1-5 | ROI 1-5 | Protect? (Y/N) |
|---|---|---|---|---|
| S-001 | Isolates prompt-geometry confound hiding inside "domain gap" claims | 4 | 5 | N |
| S-002 | Reframes point-prompt failure as interior texture; one-correlation falsifier | 3 | 4 | N |
| S-003 | GT-box eval exposed as detector benchmark; cheap re-eval kills inflated FM claims | 3 | 5 | Y |
| S-004 | Uses SAM's native 3-mask ambiguity as free supervision instead of argmax | 4 | 3 | N |
| S-005 | Asymmetric value of negative vs positive clicks; new interaction science | 4 | 4 | N |
| S-007 | Kills "training-free prompt evolution" if unsupervised scorer chases contrast blobs | 4 | 4 | Y |
| S-012 | One negative click vs adapter checkpoint: brutal cheap falsification of PEFT claims | 4 | 5 | Y |
| S-014 | Causal test of whether SAM even looks at the image inside tight boxes | 5 | 4 | Y |
| S-016 | Human click noise is boundary-seeking, not Gaussian; fixes all robustness protocols | 4 | 3 | N |
| S-018 | Three masks encode nested scale, not semantics; changes multi-mask usage everywhere | 4 | 4 | Y |
| S-019 | Loose boxes beat tight boxes on low contrast; counter-intuitive and cheap | 3 | 4 | N |
| S-041 | Decoder-local domain gap undercuts the full-FT MedSAM narrative in one split-FT | 4 | 5 | N |
| S-042 | Anisotropy, not "medical", explains 3D failure; one resampling experiment | 4 | 5 | N |
| S-043 | Prompt-occupancy scale law unifies small-target failures across modalities | 4 | 4 | N |
| S-044 | NLM denoising beats LoRA on ultrasound: preprocess > PEFT falsifier | 3 | 5 | Y |
| S-045 | Window/level is a hidden prompt hyperparameter as big as prompt type | 3 | 4 | N |
| S-046 | Negative transfer in one-MedSAM-for-all; leave-one-modality design | 3 | 4 | N |
| S-052 | Foundation features can hurt at tiny n; contrarian, high-reward learning curve | 5 | 4 | Y |
| S-054 | Objectness prior vs nested anatomy (tumor-in-liver): crisp failure law | 3 | 4 | N |
| S-056 | Slice-thickness shift beats vendor shift; reorders domain-adaptation priorities | 4 | 4 | N |
| S-064 | Meta-analysis: reported gains track #FT images, not method; deflates a whole genre | 4 | 4 | N |
| S-068 | Patient-level split leakage audit; cheap and deflates FT gains fieldwide | 3 | 5 | N |
| S-072 | Memory recency bias loses reappearing disease; concrete 3D-as-video flaw | 4 | 4 | N |
| S-073 | Slice-shuffle test of SAM2's temporal prior; one-afternoon falsifier | 3 | 4 | N |
| S-074 | One-prompt-all-slices drift curve; cheap falsifier of one-prompt claims | 3 | 5 | Y |
| S-079 | Memory embeddings collapse to position, not appearance; representation science | 5 | 3 | Y |
| S-081 | Memory-off sanity check separates training artifact from architecture claim | 3 | 4 | N |
| S-083 | Cross-patient memory bank as leakage; nobody checks this | 4 | 4 | N |
| S-090 | Temporal amplification law of an early prompt error; one plot | 3 | 4 | N |
| S-096 | Dice vs alpha-MAE ranking reversal; foundation for all smoke evaluation | 4 | 5 | N |
| S-097 | Smoke as density field, not instance: genuine problem reformulation | 4 | 4 | N |
| S-099 | Physics color model beats FM on white smoke; cheap anti-hype baseline | 3 | 5 | Y |
| S-102 | Inter-rater ceiling below published deltas kills incremental smoke papers | 4 | 4 | N |
| S-103 | Portrait matting → smoke transfer; adjacent-field bet worth protecting | 4 | 4 | Y |
| S-104 | Brightness constancy is physically invalid for smoke flow; publishable negative | 4 | 3 | N |
| S-108 | Off-the-shelf dehaze must fail on smoke; fast decisive negative | 3 | 4 | N |
| S-109 | Time-to-detect thin smoke vs mIoU: task redefinition for early warning | 4 | 4 | N |
| S-112 | Annotators over-paint smoke; models inherit fat masks — dataset bias with matting-GT check | 4 | 4 | N |
| S-126 | Matching detector AP dissolves ProFSAM-style "novelty"; assassination experiment | 4 | 5 | N |
| S-128 | HSV threshold still competitive; honesty baseline every fire paper must face | 2 | 4 | Y |
| S-134 | Time-to-alarm decorrelates from mIoU; the metric that actually matters | 4 | 4 | N |
| S-141 | LoRA destroys zero-shot promptability: the unmeasured PEFT tax | 4 | 5 | N |
| S-146 | PEFT-vs-scratch-UNet crossover n; the decision curve practitioners need | 3 | 5 | N |
| S-148 | Random LoRA directions ≈ trained LoRA would gut the PEFT literature | 5 | 4 | Y |
| S-162 | Singular-vector overlap of LoRA updates predicts forgetting; cheap theory probe | 4 | 3 | N |
| S-168 | LoRA can inject hospital-marker shortcuts; safety audit with teeth | 4 | 4 | N |
| S-175 | Regime where linear probe on frozen masks beats PEFT; deflating baseline | 3 | 4 | N |
| S-176 | Prompt-protocol forgetting (boxes→points): a CL axis nobody measures | 4 | 4 | N |
| S-177 | Forgetting localizes to decoder; one freeze ablation settles it | 4 | 4 | N |
| S-178 | Replay 100 prompt-mask pairs instead of images; cheap and new for dense CL | 4 | 4 | N |
| S-182 | Calibration collapses before Dice during forgetting; new ordering result | 4 | 4 | N |
| S-183 | If plasticity is tiny, "forgetting" is noise; contrarian re-eval of a subfield | 5 | 4 | Y |
| S-194 | Does higher rank increase forgetting: clean, decisive sweep | 3 | 4 | N |
| S-196 | SA-1B near-duplicate contamination of test sets; leakage with fieldwide impact | 3 | 4 | N |
| S-199 | NSD vs Dice rank reversal on SAM vs UNet; cheap falsifier of leaderboards | 3 | 5 | Y |
| S-203 | Seed variance exceeds method gap; stats hygiene that kills paper deltas | 3 | 4 | N |
| S-205 | TTA-confounded leaderboard climbing; disable-TTA ablation | 3 | 4 | Y |
| S-222 | Density language ("thin smoke") breaks referring segmentation; new slice | 4 | 4 | N |
| S-225 | Report-pixel misalignment harms mask learning; important measured claim | 4 | 4 | N |
| S-228 | Text priors suppress atypical disease presentations; high-stakes safety science | 5 | 4 | Y |
| S-236 | Hallucinated findings in empty scans; safety slice with clinical consequence | 4 | 4 | N |
| S-240 | Negation ("no pneumothorax") breaks VLM-driven segmentation | 4 | 4 | N |
| S-250 | Fire domain shift is lighting, not shape; testable decomposition | 3 | 4 | N |
| S-263 | Open-set fire vs glare OOD; the deployment failure that matters | 3 | 4 | N |
| S-267 | Diffusion-generated tumors leave texture shortcuts models exploit | 4 | 4 | N |
| S-285 | Generator memorization leaks train tumors into "synthetic" data | 4 | 4 | N |
| S-286 | ViT-H vs ViT-B reversal at small n; cheap assumption breaker | 3 | 4 | N |
| S-288 | Fine-tuning hurts OOD; the cheapest assumption test in the pool | 3 | 5 | Y |
| S-292 | Is SA-1B pretraining necessary at all? scratch SAM-like moonshot | 5 | 3 | Y |
| S-311 | Mask logits are not probabilities; per-prompt-type temperature | 3 | 4 | N |
| S-312 | Pixel-ECE vs region-ECE rank reversal; calibration metric science | 4 | 4 | N |
| S-318 | FT calibration tax exceeds Dice gain; protected tradeoff result | 4 | 5 | Y |
| S-323 | Smoke vs cloud OOD calibration; the false-alarm axis | 3 | 4 | N |
| S-330 | Few-shot smoke measured in density bins, not images; protocol invention | 4 | 3 | N |
| S-340 | Patient-shot vs image-shot; fixes few-shot medical evaluation | 4 | 4 | N |
| S-345 | Extra synthetic data drops real Dice; important publishable negative | 3 | 4 | N |
| S-347 | Prompt evolution lowers clinical Dice; protected anti-SAMPOT negative | 4 | 4 | Y |
| S-361 | Predicted-IoU vs true-IoU ranking mismatch; cheap selection audit | 3 | 4 | N |
| S-362 | Oracle multi-mask gap bounds the real headroom of decode tricks | 3 | 4 | N |
| S-395 | CT partial volume IS alpha matting; genuine cross-domain unification | 5 | 3 | Y |
| S-488 | Grayscale fire: one causal test of the color shortcut | 3 | 4 | N |
| S-501 | Time-matched GrabCut vs SAM; deflates usability claims with human time | 4 | 4 | N |
| S-510 | Model within intra-observer band as success criterion; recalibrates the field | 4 | 4 | N |
| S-513 | Segmentation errors that don't change dose; clinical relevance over Dice | 5 | 4 | Y |
| S-527 | SAM fails topology more than UNet; sharp testable claim | 3 | 4 | N |
| S-539 | Spectral residual analysis of SAM errors; error science, not error patching | 4 | 4 | Y |
| S-540 | Error-mode taxonomy atlas; infrastructure the SAM literature lacks | 3 | 4 | N |
| S-591 | Prompt-sensitivity scaling law; measurement paper with lasting value | 4 | 5 | N |
| S-604 | Patch-shuffle inside the box; cheapest causal probe of SAM "seeing" | 4 | 4 | Y |
| S-693 | Fog corruption vs real smoke: validity test of every robustness proxy | 3 | 4 | N |

## Kill examples (20)

| ID | kill reason |
|---|---|
| S-050 | Adapter-vs-nnU-Net compute war inside crowded MedSAM-adapter turf; no new question |
| S-084 | "Add class token to memory" = module patch squarely in the MedSAM-2 lane |
| S-091 | LoRA-placement ablation; incremental PEFT cartography |
| S-092 | Learned slice-skip gate duplicates MedSAM-2 self-sorting memory |
| S-110 | Re-merge masklets by color histogram; band-aid module, not a hypothesis |
| S-143 | DoRA vs LoRA bake-off; crowded PEFT benchmarking with no scientific claim |
| S-144 | Adapter insertion-point grid; pure hyperparameter survey |
| S-149 | QLoRA for SAM; engineering, self-admitted low science |
| S-152 | Visual-prompt vs token-prompt comparison; VPT space saturated |
| S-154 | Multi-tenant LoRA; InfLoRA clone with a hospital veneer |
| S-160 | Reproduce InfLoRA on ADE20K; reproduction, not discovery |
| S-170 | Shared LoRA across SAM and CLIP; heavy module stacking |
| S-173 | Orthogonal LoRA vs replay; InfLoRA-adjacent crowded lane |
| S-193 | LwF distillation during FT; classic method re-applied |
| S-253 | SAM pseudo-labels for semi-supervised detection; self-flagged crowded loop |
| S-281 | Self-train with SAM everything; crowded pseudo-labeling |
| S-327 | Prototype in mask-embedding space; few-shot boilerplate |
| S-366 | Super-resolution as preprocess; "apply SR to X" |
| S-416 | UNI features into SAM decoder; foundation-model gluing = module stack |
| S-445 | DINOv2 vs SAM encoder bake-off; backbone swap without an identified failure |

## Protected despite low mean score (10)

| ID | why |
|---|---|
| S-014 | Implementation is fiddly and result may be null, but a positive rewrites what "SAM segments" means |
| S-052 | Controversial and likely to draw fire, yet a confirmed pretrain-harm regime changes small-data practice |
| S-079 | Speculative probe with weak priors, but positional collapse of memory would explain many SAM2-3D failures at once |
| S-103 | Transfer may simply fail across domains, but matting→smoke is the only adjacent-field bet in the pool with a mechanism |
| S-148 | High probability of a messy outcome; if random LoRA matches trained, the PEFT literature loses its floor |
| S-183 | Contrarian claim that scores poorly on feasibility optics, but deflating "forgetting" is worth more than ten CL methods |
| S-292 | Heavy compute, likely underpowered — still the only idea that tests the field's central pretraining dogma |
| S-395 | Sounds like a metaphor, scores low on minimal-experiment clarity, but unifying partial volume with alpha matting imports a mature toolbox |
| S-513 | Requires dose pipelines most labs lack, yet decouples Dice from clinical harm — the highest-leverage eval idea here |
| S-604 | Cheap oddball causal test that mean scoring undervalues; directly arbitrates the S-014 question at near-zero cost |
