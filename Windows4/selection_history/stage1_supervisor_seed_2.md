# Stage 1 Supervisor Seed Catalog continued (S-361–S-720)

Mutations, splits, and adjacent-field ideas. Still hypotheses, not results.

| ID | OneLiner | Problem | Hypothesis | WhyNovel | MinExp | Risk | Cluster |
| S-361 | SAM predicted-IoU ranking ≠ true-IoU ranking | Selection | Spearman ρ << 1 on medical | Document | 200 imgs | Low | SAM_PROMPT |
| S-362 | Best of 3 SAM masks vs predicted best | Decode | Oracle multi-mask gap is the real headroom | Upper bound | 1 set | Low | SAM_PROMPT |
| S-363 | Click on edge vs center for thin structures | Protocol | Edge clicks win on vessels | Geometry | 1 | Low | SAM_PROMPT |
| S-364 | Box aspect penalty in prompt PE | Method? | Prefer not a module: measure failure vs aspect | Measure | 1 | Low | SAM_PROMPT |
| S-365 | Prompt-conditioned dropout at test | TTA | Random prompt dropout ensemble | Cheap | 1 | Incremental | SAM_PROMPT |
| S-366 | SAM on super-resolved inputs | SR as preprocess | SR helps small lesions more than FT | Preprocess | 1 | Crowded SR | SAM_PROMPT |
| S-367 | SAM on restored (denoised) CT | Restore | Denoise > LoRA | Pre | 1 | Incremental | SAM_PROMPT |
| S-368 | JPEG quality as hidden domain | Robust | Web-scraped fire videos | Sweep q | 1 | Low | ROBUST |
| S-369 | Motion blur vs SAM2 memory | Video | Blur kills memory more than spatial | Slice | 1 | Low | SAM2_MEMORY |
| S-370 | Compression artifacts as ‘texture objects’ | Failure | SAM snaps to blocks | JPEG | 1 | Low | SAM_PROMPT |
| S-371 | Defocus as transparent-like edges | Unify | Defocused objects behave like alpha | Camera | 1 | Speculative | SMOKE_ALPHA |
| S-372 | Rain streaks as linear transparent objects | Adjacent |  | 1 | Incremental | SMOKE_ALPHA |
| S-373 | Glass facade segmentation vs smoke | Unify | Same metrics | Trans10k | Medium | SMOKE_ALPHA |
| S-374 | Water caustics | Failure | SAM on underwater | 1 | Niche | SAM_PROMPT |
| S-375 | Camouflage vs smoke: texture vs alpha | Taxonomy | Different failures | COD + smoke | Medium | ASSUMPTION |
| S-376 | Shadow vs smoke | Confound |  | 1 | Low | SMOKE_ALPHA |
| S-377 | Steam vs smoke | Taxonomy | Kitchen vs fire | 1 | Data | SMOKE_ALPHA |
| S-378 | Dust vs smoke | Taxonomy |  | 1 | Data | SMOKE_ALPHA |
| S-379 | Condensation on lens | Sensor |  | 1 | Niche | ROBUST |
| S-380 | Rolling shutter on flames | Sensor |  | 1 | Niche | FIRE_CONFOUND |
| S-381 | HDR vs SDR fire | Sensor |  | 1 | Data | FIRE_CONFOUND |
| S-382 | Auto-exposure pumping | Video |  | 1 | Low | FIRE_CONFOUND |
| S-383 | White-balance as domain | Color |  | 1 | Low | DET_SHIFT |
| S-384 | ISP pipeline mismatch phone vs SLR | Domain |  | 1 | Data | DET_SHIFT |
| S-385 | Super-resolution of smoke density | Inverse | Ill-posed | Synthetic | High | SMOKE_ALPHA |
| S-386 | Blind deconvolution then segment | Pipeline |  | 1 | Old | SAM_PROMPT |
| S-387 | Learn to window CT with Dice reward | Preprocess | vs fixed window | 1 | Incremental | SAM_MEDICAL_GAP |
| S-388 | Per-patient window as prompt | Prompt | Window vector into SAM | 1 | Novel-ish | SAM_MEDICAL_GAP |
| S-389 | DICOM tags as side information | Meta | Slice loc, kVp | 1 | Data | SAM_MEDICAL_GAP |
| S-390 | Scanner vendor adversarial validation | Domain |  | 1 | Data | SAM_MEDICAL_GAP |
| S-391 | Protocol (contrast vs noncon) | Domain |  | 1 | Data | SAM_MEDICAL_GAP |
| S-392 | Pediatric vs adult scale | Shift |  | 1 | Data | SAM_MEDICAL_GAP |
| S-393 | Implanted devices as OOD | Robust |  | 1 | Niche | SAM_MEDICAL_GAP |
| S-394 | Motion artifact MRI | Robust |  | 1 | Data | SAM_MEDICAL_GAP |
| S-395 | Partial volume as alpha matting | Unify | CT partial volume = alpha | 1 | Interesting | SMOKE_ALPHA |
| S-396 | Super-pixel prompts | Prompt | SLIC region as mask prompt | 1 | Incremental | SAM_PROMPT |
| S-397 | Extreme learning: 1-pixel prompt | Limit |  | 1 | Easy | SAM_PROMPT |
| S-398 | Whole-image box prompt | Limit | Equals saliency | 1 | Easy | SAM_PROMPT |
| S-399 | Random box prior as baseline for SAM | Baseline |  | 1 | Easy | SAM_PROMPT |
| S-400 | Distance transform as extra channel | Input |  | 1 | Old | SAM_PROMPT |
| S-401 | Edge map concatenation | Input |  | 1 | Old | SAM_PROMPT |
| S-402 | Do not concatenate: test if SAM already uses edges | Ablate | Sobel in vs out | 1 | Easy | ASSUMPTION |
| S-403 | Frequency-domain filtering before SAM | Pre | High-pass vs low | 1 | Easy | SAM_PROMPT |
| S-404 | Color jitter FT vs frozen | Robust |  | 1 | Easy | PEFT_DENSE |
| S-405 | MixStyle at test | TTA |  | 1 | Crowded | SYNTH_DA |
| S-406 | Batch-norm stats from target | TTA |  | 1 | Old | SYNTH_DA |
| S-407 | Prompt stats from target (box size histogram) | TTA |  | 1 | Novel-ish | SAM_PROMPT |
| S-408 | Self-consistency of SAM under flip | TTA | Flip-average | 1 | Easy | SAM_PROMPT |
| S-409 | Rotation 90 invariance of SAM | Equiv |  | 1 | Easy | SAM_PROMPT |
| S-410 | Scale pyramid SAM | TTA |  | 1 | Incremental | SAM_PROMPT |
| S-411 | SAM on tiles with overlap consensus | Large images | Pathology | 1 | Eng | SAM_MEDICAL_GAP |
| S-412 | WSI gigapixel prompt protocol | Problem |  | 1 | Data | SAM_MEDICAL_GAP |
| S-413 | Cell overlapping as mutex | Problem |  | 1 | Cellpose exists | SAM_MEDICAL_GAP |
| S-414 | Stain normalization as prompt | Pre |  | 1 | Old | SAM_MEDICAL_GAP |
| S-415 | IHC vs H&E domain | Shift |  | 1 | Data | SAM_MEDICAL_GAP |
| S-416 | Frozen pathology VFM + SAM decoder | Hybrid | UNI features into SAM | Heavy | Crowded | SAM_MEDICAL_GAP |
| S-417 | Do not fuse: linear probe UNI vs SAM | Baseline |  | 1 | Easy | ASSUMPTION |
| S-418 | Radiology report to box then SAM | Pipeline |  | 1 | Crowded | VLM_DENSE |
| S-419 | Report negation handling | Language |  | 1 | Important | VLM_DENSE |
| S-420 | Laterality errors in VLM-SAM | Safety |  | 1 | Important | VLM_DENSE |
| S-421 | Measurement tokens (mm) in prompts | Language |  | 1 | Interesting | VLM_DENSE |
| S-422 | Count questions vs masks | Task |  | 1 | Adjacent | VLM_DENSE |
| S-423 | Visual question on mask quality | Eval |  | 1 | Risky | VLM_DENSE |
| S-424 | LLM writes experiment configs | Meta | Out of scope unless failure study | — | Low ROI | NEG_RESULT |
| S-425 | Agent annotator vs human time | HCI |  | Cost | Soft | FEWSHOT |
| S-426 | Active learning with prompt disagreement | AL |  | 1 | Incremental | SAM_PROMPT |
| S-427 | Batch AL vs sequential clicks | AL |  | 1 | Crowded | FEWSHOT |
| S-428 | Core-set in SAM embedding | AL |  | 1 | Crowded | FEWSHOT |
| S-429 | Forget AL on OOD hospitals | AL |  | 1 | Interesting | FORGETTING |
| S-430 | Label smoothing on masks | Train |  | 1 | Old | PEFT_DENSE |
| S-431 | Boundary-weighted Dice vs uniform | Loss | Not ‘new loss paper’: test if SAM FT needs it | 1 | Easy | ASSUMPTION |
| S-432 | Cross-entropy on logits vs Dice on SAM FT | Loss |  | 1 | Easy | PEFT_DENSE |
| S-433 | Focal loss for thin smoke | Loss | Only if density bins | 1 | Incremental | SMOKE_ALPHA |
| S-434 | Tversky for fire recall | Loss |  | 1 | Old | FIRE_CONFOUND |
| S-435 | Do not invent loss: reweight density bins | Data |  | 1 | Better | SMOKE_ALPHA |
| S-436 | Curriculum from thick to thin smoke | Train |  | 1 | Incremental | SMOKE_ALPHA |
| S-437 | Curriculum from large to small organs | Train |  | 1 | Old | SAM_MEDICAL_GAP |
| S-438 | Anti-curriculum: hard first | Train |  | 1 | Easy | ASSUMPTION |
| S-439 | SAM pseudo-labels as curriculum teacher | Distill | Crowded | Search | Crowded | SYNTH_DA |
| S-440 | Confidence thresholding of pseudo | Distill |  | 1 | Old | SYNTH_DA |
| S-441 | Co-training two prompt types | Semi |  | 1 | Incremental | SAM_PROMPT |
| S-442 | Mean-teacher on SAM decoder | Semi |  | 1 | Old | PEFT_DENSE |
| S-443 | Consistency under prompt jitter as SSL | SSL |  | 1 | Novel-ish | SAM_PROMPT |
| S-444 | MAE-pretrained encoder vs SAM encoder for UNet | Rep |  | Compute | Crowded | PEFT_DENSE |
| S-445 | DINOv2 vs SAM encoder for dense | Rep |  | 1 | Crowded | PEFT_DENSE |
| S-446 | Which frozen encoder for tiny n | Regime |  | Curve | Important | ASSUMPTION |
| S-447 | Patch size 14 vs 16 on small lesions | Arch |  | 1 | Incremental | SAM_MEDICAL_GAP |
| S-448 | Windowed attention vs global for WSI | Arch |  | Heavy | Crowded | SAM_MEDICAL_GAP |
| S-449 | Mamba vs ViT: only if failure of ViT identified | Arch | Need failure first | — | Pseudo-risk | NEG_RESULT |
| S-450 | Do not replace backbone without question | Kill | — | — | Kill | NEG_RESULT |
| S-451 | Token merging speed vs small-object recall | Efficient |  | 1 | Eng | DET_SHIFT |
| S-452 | Pruning SAM MLP | Efficient |  | 1 | Eng | PEFT_DENSE |
| S-453 | Distill SAM2 to Tiny for fire with matched prompts | Distill | Fair | 1 | Crowded | FIRE_CONFOUND |
| S-454 | On-device windowing + tiny UNet vs MobileSAM | Deploy |  | 1 | Eng | FIRE_CONFOUND |
| S-455 | Energy consumption metric | Deploy |  | 1 | Soft | EVAL_LEAK |
| S-456 | Latency percentiles not mean | Deploy |  | 1 | Eng | EVAL_LEAK |
| S-457 | Batch size 1 vs 8 Dice difference | Protocol | BN | 1 | Easy | EVAL_LEAK |
| S-458 | Mixed precision mask diffs | Repro |  | 1 | Eng | EVAL_LEAK |
| S-459 | Non-determinism of SAM CUDA | Repro |  | 1 | Eng | EVAL_LEAK |
| S-460 | Checkpoint averaging of LoRA | Train |  | 1 | Incremental | PEFT_DENSE |
| S-461 | Early stopping on calibration not Dice | Train |  | 1 | Interesting | CALIB |
| S-462 | Early stopping on OOD hospital | Train |  | 1 | Important | SAM_MEDICAL_GAP |
| S-463 | Model soups of prompt-type specialists | Soup |  | 1 | Incremental | SAM_PROMPT |
| S-464 | Task vectors for organs | Arithmetic |  | 1 | Crowded | PEFT_DENSE |
| S-465 | Negating a bad LoRA direction | Edit |  | 1 | Speculative | PEFT_DENSE |
| S-466 | Repair FT with old-task prompts | Repair |  | 1 | Incremental | FORGETTING |
| S-467 | Elastic weight on prompt encoder only | EWC |  | 1 | Incremental | FORGETTING |
| S-468 | Pack multiple organs as multi-prompt batch | Train |  | 1 | Eng | SAM_MEDICAL_GAP |
| S-469 | Class-balanced sampling vs patient-balanced | Train |  | 1 | Important | EVAL_LEAK |
| S-470 | Over-sample thin smoke frames | Train |  | 1 | Easy | SMOKE_ALPHA |
| S-471 | Temporal striding as augmentation | Video |  | 1 | Easy | SAM2_MEMORY |
| S-472 | Reverse video training | Video |  | 1 | Easy | SAM2_MEMORY |
| S-473 | Speed jitter of fire videos | Video |  | 1 | Easy | FIRE_CONFOUND |
| S-474 | Frame duplication as cheat | Eval | Detect duplicated frames in test | Audit | Social | EVAL_LEAK |
| S-475 | Train/test clip overlap in fire datasets | Leak | Hash | 1 | Social | EVAL_LEAK |
| S-476 | YouTube fire dataset license | Social |  | — | Soft | EVAL_LEAK |
| S-477 | Geographic bias of wildfire datasets | Bias |  | Meta | Soft | EVAL_LEAK |
| S-478 | Skin tone / scene bias in smoke cameras | Bias |  | 1 | Soft | EVAL_LEAK |
| S-479 | Sex/age performance gaps in organs | Fair |  | 1 | Important | SAM_MEDICAL_GAP |
| S-480 | Scanner-size hospital confounding | Causal |  | 1 | Hard | SAM_MEDICAL_GAP |
| S-481 | Shortcut: ruler in X-ray | Spurious |  | 1 | Known class | SAM_MEDICAL_GAP |
| S-482 | Shortcut: hospital overlay text | Spurious |  | 1 | Known | VLM_DENSE |
| S-483 | Shortcut: chest tube implies pathology | Spurious |  | 1 | Known | SAM_MEDICAL_GAP |
| S-484 | Shortcut: red saturation implies fire | Spurious |  | 1 | Easy | FIRE_CONFOUND |
| S-485 | Shortcut: sky implies not fire | Spurious |  | 1 | Easy | FIRE_CONFOUND |
| S-486 | Counterfactual overlay of red without fire | Causal |  | 1 | Easy | FIRE_CONFOUND |
| S-487 | Gray-world fire images | Causal |  | 1 | Easy | FIRE_CONFOUND |
| S-488 | Remove color: grayscale SAM on fire | Causal |  | 1 | Easy | FIRE_CONFOUND |
| S-489 | Grayscale smoke: color unnecessary? | Causal |  | 1 | Easy | SMOKE_ALPHA |
| S-490 | Optical flow only smoke detector | Baseline |  | 1 | Old | SMOKE_ALPHA |
| S-491 | Change detection baseline | Baseline |  | 1 | Old | SMOKE_ALPHA |
| S-492 | GMM background | Baseline |  | 1 | Old | SMOKE_ALPHA |
| S-493 | Report old baselines or reject | Social |  | — | Social | EVAL_LEAK |
| S-494 | nnU-Net as mandatory medical baseline | Social |  | 1 | Social | SAM_MEDICAL_GAP |
| S-495 | Cellpose as mandatory cell baseline | Social |  | 1 | Social | SAM_MEDICAL_GAP |
| S-496 | Mask R-CNN as fire baseline | Social |  | 1 | Social | FIRE_CONFOUND |
| S-497 | DeepLab stuff baseline for smoke | Social |  | 1 | Social | SMOKE_ALPHA |
| S-498 | CRF postprocess as baseline | Social |  | 1 | Old | SAM_PROMPT |
| S-499 | GrabCut as interactive baseline | Social |  | 1 | Old | SAM_PROMPT |
| S-500 | SIOX / watershed | Social |  | 1 | Old | SAM_PROMPT |
| S-501 | Human time-matched GrabCut vs SAM | HCI |  | Cost | Important | SAM_PROMPT |
| S-502 | Novice vs expert prompts | HCI |  | Cost | Important | SAM_PROMPT |
| S-503 | Prompt tutorial effect | HCI |  | Cost | Soft | SAM_PROMPT |
| S-504 | Fatigue over 100 cases | HCI |  | Cost | Soft | SAM_PROMPT |
| S-505 | Trust calibration of SAM IoU-token | HCI |  | Cost | CALIB | CALIB |
| S-506 | Automation bias: accept wrong SAM | HCI |  | Cost | Safety | SAM_MEDICAL_GAP |
| S-507 | Second reader with SAM | Clinical |  | Heavy | Soft | SAM_MEDICAL_GAP |
| S-508 | CAD trial endpoints ≠ Dice | Clinical |  | Soft | Soft | EVAL_LEAK |
| S-509 | Contouring time in radiotherapy | App |  | Cost | Soft | SAM_MEDICAL_GAP |
| S-510 | Intra-observer variability as target | Metric | Model within human band | 1 | Important | EVAL_LEAK |
| S-511 | Surface Dice radiotherapy default | Metric |  | 1 | Known | EVAL_LEAK |
| S-512 | Dose-volume on predicted vs GT | Downstream |  | Heavy | Important | SAM_MEDICAL_GAP |
| S-513 | Segmentation error that does not change dose | Downstream |  | Heavy | Important | SAM_MEDICAL_GAP |
| S-514 | Detection mAP that does not change alarm | Downstream |  | 1 | Important | FIRE_CONFOUND |
| S-515 | Tracking MOTA vs fire spread estimate | Downstream |  | 1 | Interesting | FIRE_CONFOUND |
| S-516 | 3D volume error vs slice Dice | Downstream |  | 1 | Known | SAM_MEDICAL_GAP |
| S-517 | Hausdorff 95 sensitive to one pixel | Metric |  | 1 | Known | EVAL_LEAK |
| S-518 | Normalized surface Dice threshold 2mm | Metric |  | 1 | Known | EVAL_LEAK |
| S-519 | Panoptic quality for multi-organ | Metric |  | 1 | Known | EVAL_LEAK |
| S-520 | PQ for fire instances | Metric |  | 1 | Incremental | FIRE_CONFOUND |
| S-521 | Boundary IoU for glass | Metric |  | 1 | Known | SMOKE_ALPHA |
| S-522 | MAD / MSE for alpha | Metric |  | 1 | Known | SMOKE_ALPHA |
| S-523 | Gradient error for alpha | Metric |  | 1 | Known | SMOKE_ALPHA |
| S-524 | Connectivity of smoke masks | Metric |  | 1 | Interesting | SMOKE_ALPHA |
| S-525 | Topology (Betti) of vessels | Metric |  | 1 | Crowded | SAM_MEDICAL_GAP |
| S-526 | Centerline Dice for catheters | Metric |  | 1 | Known | SAM_MEDICAL_GAP |
| S-527 | SAM fails topology more than UNet | Claim |  | 1 | Testable | SAM_MEDICAL_GAP |
| S-528 | Post-hoc topology fix vs extra modules | Simple |  | 1 | Old | SAM_MEDICAL_GAP |
| S-529 | Connected-component filter as baseline | Simple |  | 1 | Easy | SAM_PROMPT |
| S-530 | Hole filling ruins nested objects | Failure |  | 1 | Easy | SAM_PROMPT |
| S-531 | Nested tumor-in-organ protocol | Protocol | Two prompts | 1 | Important | SAM_MEDICAL_GAP |
| S-532 | Hierarchical SAM: organ then lesion | Pipeline |  | 1 | Incremental | SAM_MEDICAL_GAP |
| S-533 | Condition lesion prompt on organ mask | Prompt |  | 1 | Incremental | SAM_PROMPT |
| S-534 | Mutex loss between organ and lesion | Train | If FT | 1 | Old | PEFT_DENSE |
| S-535 | Atlas prior vs SAM | Classical |  | 1 | Old | SAM_MEDICAL_GAP |
| S-536 | Registration then atlas vs promptable | Compare |  | 1 | Old | SAM_MEDICAL_GAP |
| S-537 | SAM to initialize level-set | Hybrid |  | 1 | Old | SAM_PROMPT |
| S-538 | Do hybrid only if SAM residual is high-frequency | Test |  | 1 | Interesting | SAM_PROMPT |
| S-539 | Residual analysis of SAM errors | Science | Spectral of error | 1 | Important | SAM_PROMPT |
| S-540 | Error modes taxonomy atlas | Science | Cluster errors | 1 | Important | SAM_PROMPT |
| S-541 | Per-dataset error fingerprints | Science |  | Meta | Social | EVAL_LEAK |
| S-542 | Predict SAM failure from image stats | Routing | Then send to specialist | 1 | Incremental | SAM_PROMPT |
| S-543 | Router to nnU-Net vs SAM | System |  | 1 | Eng | SAM_MEDICAL_GAP |
| S-544 | Cheap detector of ‘stuff vs thing’ | Router |  | 1 | Interesting | SMOKE_ALPHA |
| S-545 | Thing model on smoke is a category error | Claim |  | 1 | Conceptual | SMOKE_ALPHA |
| S-546 | Stuff model on instruments fails | Dual |  | 1 | Easy | DET_SHIFT |
| S-547 | Panoptic fire+smoke jointly | Task |  | Data | Ambitious | FIRE_CONFOUND |
| S-548 | Shared encoder two heads not novelty unless conflict shown | Kill | Show gradient conflict first | 1 | Science | PEFT_DENSE |
| S-549 | Gradient conflict fire vs smoke | Measure |  | 1 | Testable | PEFT_DENSE |
| S-550 | Multi-task helps calibration | Claim |  | 1 | Testable | CALIB |
| S-551 | Multi-task hurts rare class | Claim |  | 1 | Easy | DET_SHIFT |
| S-552 | Auxiliary depth for smoke | If RGB-D |  | Data | Data | SMOKE_ALPHA |
| S-553 | Stereo smoke | Sensor |  | Data | Hardware | SMOKE_ALPHA |
| S-554 | LiDAR + camera fire | Sensor |  | Data | Hardware | FIRE_CONFOUND |
| S-555 | Hyperspectral smoke | Sensor |  | Data | Hardware | SMOKE_ALPHA |
| S-556 | Cheap RGB-only vs sensor: ROI | Question | When RGB enough | Soft | Soft | ASSUMPTION |
| S-557 | Thermal-only fire segmentation | Sensor |  | 1 | Data | FIRE_CONFOUND |
| S-558 | Align thermal-RGB as the problem | DA |  | 1 | Crowded | SYNTH_DA |
| S-559 | Unpaired thermal-RGB cycle is crowded | Kill | Need new question | — | Kill | SYNTH_DA |
| S-560 | Event cameras for flicker | Sensor |  | Data | Niche | FIRE_CONFOUND |
| S-561 | Audio crackle + video | Multi |  | Data | Adjacent | FIRE_CONFOUND |
| S-562 | Smell sensors out of scope | Kill | — | — | Kill | NEG_RESULT |
| S-563 | Satellite wildfire vs ground cameras | Scale | Different science | Split | Social | FIRE_CONFOUND |
| S-564 | SAM on satellite smoke plumes | Scale |  | 1 | Data | SMOKE_ALPHA |
| S-565 | Resolution gap 10m vs 1cm | Problem |  | 1 | Soft | SMOKE_ALPHA |
| S-566 | Cloud vs smoke in satellite | Confound |  | 1 | Known remote sensing | SMOKE_ALPHA |
| S-567 | Do not claim CV novelty if RS literature has it | Search | Mandatory Stage 3 | — | Process | EVAL_LEAK |
| S-568 | Underwater smoke analog: turbidity | Unify |  | 1 | Speculative | SMOKE_ALPHA |
| S-569 | Fog driving datasets vs wildfire smoke | Transfer |  | 1 | Testable | SMOKE_ALPHA |
| S-570 | BDD fog models on wildfire | Transfer |  | 1 | Easy | SMOKE_ALPHA |
| S-571 | Adverse weather benchmarks miss fire | Gap |  | Meta | Soft | EVAL_LEAK |
| S-572 | Transparent product inspection | Industry |  | 1 | Data | SMOKE_ALPHA |
| S-573 | Plastic wrap on food | Industry |  | 1 | Niche | SMOKE_ALPHA |
| S-574 | Cell culture media meniscus | Science |  | 1 | Niche | SAM_MEDICAL_GAP |
| S-575 | Ultrasound gel artifacts | Failure |  | 1 | Niche | SAM_MEDICAL_GAP |
| S-576 | Specular highlights as false fire | Failure |  | 1 | Easy | FIRE_CONFOUND |
| S-577 | Neon signs as false fire | Failure |  | 1 | Easy | FIRE_CONFOUND |
| S-578 | Sunsets as false fire | Failure |  | 1 | Easy | FIRE_CONFOUND |
| S-579 | Welding as out-of-scope fire | Taxonomy |  | 1 | Soft | FIRE_CONFOUND |
| S-580 | Birthday candles vs disaster fire | Taxonomy |  | 1 | Soft | FIRE_CONFOUND |
| S-581 | Dataset definition is the contribution | Claim |  | Data | Social | EVAL_LEAK |
| S-582 | New dataset only if old metrics fail | Rule |  | — | Process | EVAL_LEAK |
| S-583 | Re-annotate smoke with alpha | Data | High value | Cost | Cost | SMOKE_ALPHA |
| S-584 | Re-annotate SAM-medical with patient splits | Data |  | Cost | Social | SAM_MEDICAL_GAP |
| S-585 | Multi-rater smoke release | Data |  | Cost | Important | SMOKE_ALPHA |
| S-586 | Prompt traces release | Data | Clicks logged | Cost | Important | SAM_PROMPT |
| S-587 | Failure-case zoo as paper | Science |  | Cost | Social | SAM_PROMPT |
| S-588 | Reproducibility pack > 0.5% Dice | Social |  | — | Social | EVAL_LEAK |
| S-589 | Negative results venue strategy | Social |  | — | Soft | NEG_RESULT |
| S-590 | Assumption-challenging is a paper type | Social |  | — | Soft | ASSUMPTION |
| S-591 | Measurement paper: prompt sensitivity law | Science | Fit scaling | 1 | Important | SAM_PROMPT |
| S-592 | Scaling law of FT images vs Dice | Science |  | Compute | Crowded | PEFT_DENSE |
| S-593 | Scaling law of LoRA rank vs forget | Science |  | 2 tasks | Interesting | FORGETTING |
| S-594 | Scaling law of memory length vs 3D Dice | Science |  | 1 | Easy | SAM2_MEMORY |
| S-595 | Scaling law of box tightness vs Dice | Science |  | 1 | Easy | SAM_PROMPT |
| S-596 | Power-law of object area vs Dice | Science |  | Meta | Important | SAM_PROMPT |
| S-597 | Contrast vs Dice law | Science |  | Meta | Important | SAM_MEDICAL_GAP |
| S-598 | Boundary length vs Dice | Science |  | 1 | Easy | SAM_PROMPT |
| S-599 | Fractal dimension of tumors vs SAM fail | Science |  | 1 | Speculative | SAM_MEDICAL_GAP |
| S-600 | Texture entropy vs point-prompt fail | Science |  | 1 | Repeat S-002 | SAM_PROMPT |
| S-601 | Mutate S-002: entropy in Fourier | Science |  | 1 | Incremental | SAM_PROMPT |
| S-602 | Mutate S-007: scorer = SAM IoU-token | Circular | Will overfit | 1 | Easy | SAM_PROMPT |
| S-603 | Mutate S-007: scorer = radiologist mini-model | Distill |  | 1 | Data | SAM_PROMPT |
| S-604 | Mutate S-014: shuffle patches inside box | Causal |  | 1 | Interesting | SAM_PROMPT |
| S-605 | Mutate S-014: shuffle outside box | Causal |  | 1 | Interesting | SAM_PROMPT |
| S-606 | Mutate S-041: FT 50 decoder steps only | Extreme |  | 1 | Easy | SAM_MEDICAL_GAP |
| S-607 | Mutate S-046: sequential vs mixed modalities | CL |  | 1 | Important | FORGETTING |
| S-608 | Mutate S-052: n=10,20,50,100 curves | Regime |  | 1 | Important | ASSUMPTION |
| S-609 | Mutate S-058: forgetting of which COCO classes | Slice |  | 1 | Interesting | FORGETTING |
| S-610 | Mutate S-073: random vs reversed order | 3D |  | 1 | Easy | SAM2_MEMORY |
| S-611 | Mutate S-079: probe memory for organ id | Probe |  | 1 | Interesting | SAM2_MEMORY |
| S-612 | Mutate S-096: rank corr of 8 metrics | Meta |  | 1 | Important | EVAL_LEAK |
| S-613 | Mutate S-103: portrait matting → glass | Transfer |  | 1 | Testable | SMOKE_ALPHA |
| S-614 | Mutate S-141: which COCO classes survive PEFT | Slice |  | 1 | Important | PEFT_DENSE |
| S-615 | Mutate S-148: random LoRA scaled to same norm | Control |  | 1 | High risk | PEFT_DENSE |
| S-616 | Mutate S-164: train for selective net risk | Objective |  | 1 | Interesting | CALIB |
| S-617 | Mutate S-176: order points then boxes | Order |  | 1 | Easy | FORGETTING |
| S-618 | Mutate S-199: include HD95, NSD, PQ | Matrix |  | 1 | Easy | EVAL_LEAK |
| S-619 | Mutate S-228: rare vs typical disease photos | Slice |  | 1 | Data | VLM_DENSE |
| S-620 | Mutate S-240: synthetic negation sentences | NLP |  | 1 | Easy | VLM_DENSE |
| S-621 | Mutate S-288: OOD = other organ | Split |  | 1 | Easy | ASSUMPTION |
| S-622 | Mutate S-288: OOD = other hospital | Split |  | 1 | Important | ASSUMPTION |
| S-623 | Mutate S-292: from-scratch ViT on one organ | Heavy |  | Compute | High risk | ASSUMPTION |
| S-624 | Mutate S-318: plot Dice-ECE Pareto | Tradeoff |  | 1 | Important | CALIB |
| S-625 | Mutate S-342: memory off vs ablate occlusion | Ablate |  | 1 | Easy | SAM2_MEMORY |
| S-626 | Mutate S-347: prompt evolution on smoke | Domain |  | 1 | Easy | SMOKE_ALPHA |
| S-627 | Split S-015: fire vs smoke vs stain vs haze | Taxonomy |  | 1 | Conceptual | ASSUMPTION |
| S-628 | Split S-054: point on tumor vs box on tumor | Prompt |  | 1 | Easy | SAM_MEDICAL_GAP |
| S-629 | Split S-099: white vs black vs industrial smoke | Color |  | 1 | Data | SMOKE_ALPHA |
| S-630 | Split S-126: indoor vs wildfire vs vehicle | Scene |  | 1 | Data | FIRE_CONFOUND |
| S-631 | Merge S-003+S-060: oracle prompt protocol paper | Eval |  | Meta | Social | EVAL_LEAK |
| S-632 | Merge S-096+S-199: metric-reversal paper | Eval |  | Meta | Important | EVAL_LEAK |
| S-633 | Merge S-141+S-058: PEFT tax on zero-shot | PEFT |  | 1 | Important | PEFT_DENSE |
| S-634 | Merge S-176+S-006: protocol forgetting | CL |  | 1 | Important | FORGETTING |
| S-635 | Merge S-079+S-073: memory content vs order | Memory |  | 1 | Important | SAM2_MEMORY |
| S-636 | Revive ‘simple color model’ as required baseline | Social |  | 1 | Social | SMOKE_ALPHA |
| S-637 | Revive GrabCut time-matched | Social |  | Cost | Social | SAM_PROMPT |
| S-638 | Kill S-149 QLoRA unless VRAM story | Kill | — | — | Kill | PEFT_DENSE |
| S-639 | Kill S-424 LLM experiment agent | Kill | — | — | Kill | NEG_RESULT |
| S-640 | Kill S-449 Mamba without failure | Kill | — | — | Kill | NEG_RESULT |
| S-641 | Kill S-450 backbone swap | Kill | — | — | Kill | NEG_RESULT |
| S-642 | Kill S-559 unpaired CycleGAN | Kill | — | — | Kill | SYNTH_DA |
| S-643 | Kill S-562 smell | Kill | — | — | Kill | NEG_RESULT |
| S-644 | Protect S-014 image-ablation-in-box | Protect | — | — | Protect | SAM_PROMPT |
| S-645 | Protect S-052 pretrain harm small n | Protect | — | — | Protect | ASSUMPTION |
| S-646 | Protect S-148 random LoRA | Protect | — | — | Protect | PEFT_DENSE |
| S-647 | Protect S-183 low plasticity | Protect | — | — | Protect | FORGETTING |
| S-648 | Protect S-228 VLM prior harm | Protect | — | — | Protect | VLM_DENSE |
| S-649 | Protect S-292 scratch SAM-like | Protect | — | — | Protect | ASSUMPTION |
| S-650 | Protect S-318 FT calibration tax | Protect | — | — | Protect | CALIB |
| S-651 | Protect S-347 prompt evolution harm | Protect | — | — | Protect | SAM_PROMPT |
| S-652 | Protect S-395 partial volume as alpha | Protect | — | — | Protect | SMOKE_ALPHA |
| S-653 | Protect S-513 dose-insensitive errors | Protect | — | — | Protect | SAM_MEDICAL_GAP |
| S-654 | Protect S-539 residual spectrum | Protect | — | — | Protect | SAM_PROMPT |
| S-655 | Protect S-604 patch shuffle causal | Protect | — | — | Protect | SAM_PROMPT |
| S-656 | Cheap: S-408 flip consistency | Cheap |  | 1 | Cheap | SAM_PROMPT |
| S-657 | Cheap: S-409 rotation | Cheap |  | 1 | Cheap | SAM_PROMPT |
| S-658 | Cheap: S-488 grayscale fire | Cheap |  | 1 | Cheap | FIRE_CONFOUND |
| S-659 | Cheap: S-489 grayscale smoke | Cheap |  | 1 | Cheap | SMOKE_ALPHA |
| S-660 | Cheap: S-293 memory off | Cheap |  | 1 | Cheap | SAM2_MEMORY |
| S-661 | Cheap: S-287 extra points | Cheap |  | 1 | Cheap | SAM_PROMPT |
| S-662 | Cheap: S-294 box vs point by contrast | Cheap |  | 1 | Cheap | SAM_PROMPT |
| S-663 | Cheap: S-298 IoU-token ECE | Cheap |  | 1 | Cheap | CALIB |
| S-664 | Cheap: S-356 random boxes | Cheap |  | 1 | Cheap | SAM_PROMPT |
| S-665 | Cheap: S-353 click saturation | Cheap |  | 1 | Cheap | SAM_PROMPT |
| S-666 | Representation: SAM token PCA of organs | Rep |  | 1 | Easy | SAM_MEDICAL_GAP |
| S-667 | Representation: CKA encoder medical vs SA-1B | Rep |  | Compute | Interesting | SAM_MEDICAL_GAP |
| S-668 | Representation: decoder cross-attn maps | Rep |  | 1 | Easy | SAM_PROMPT |
| S-669 | Representation: memory bank CKA across patients | Rep |  | 1 | Interesting | SAM2_MEMORY |
| S-670 | Representation: LoRA subspace overlap organs | Rep |  | 1 | Interesting | PEFT_DENSE |
| S-671 | Representation: CLIP vs SAM space alignment | Rep |  | 1 | Crowded | VLM_DENSE |
| S-672 | Representation: smoke vs cloud in CLIP | Rep |  | 1 | Easy | VLM_DENSE |
| S-673 | Representation: fire in CLIP is ‘orange’ | Rep |  | 1 | Easy | VLM_DENSE |
| S-674 | Representation: medical CLIP still natural-image clustered | Rep |  | 1 | Testable | VLM_DENSE |
| S-675 | Representation: mask token vs image token RSA | Rep |  | 1 | Interesting | SAM_PROMPT |
| S-676 | Optimization: AdamW vs SGD on SAM FT | Opt |  | 1 | Easy | PEFT_DENSE |
| S-677 | Optimization: cosine vs constant | Opt |  | 1 | Easy | PEFT_DENSE |
| S-678 | Optimization: warmup necessity | Opt |  | 1 | Easy | PEFT_DENSE |
| S-679 | Optimization: gradient clipping on decoder | Opt |  | 1 | Easy | PEFT_DENSE |
| S-680 | Optimization: loss scale fp16 | Opt |  | 1 | Eng | PEFT_DENSE |
| S-681 | Data: duplicate patients across public sets | Leak |  | Hash | Social | EVAL_LEAK |
| S-682 | Data: MSD vs BTCV overlap | Leak |  | Audit | Social | EVAL_LEAK |
| S-683 | Data: fire videos from same YouTube channel | Leak |  | Audit | Social | EVAL_LEAK |
| S-684 | Data: smoke pics from same factory | Leak |  | Audit | Social | EVAL_LEAK |
| S-685 | Data: SA-1B in training of compared FMs | Leak |  | Meta | Social | EVAL_LEAK |
| S-686 | Legal: SAM weights license in clinic | Social |  | — | Soft | EVAL_LEAK |
| S-687 | Legal: medical data in FT | Social |  | — | Soft | EVAL_LEAK |
| S-688 | Privacy: memorization of rare tattoos in SAM | Safety |  | Hard | Hard | EVAL_LEAK |
| S-689 | Privacy: membership of medical FT | Safety |  | 1 | Heavy | EVAL_LEAK |
| S-690 | Safety: SAM on adversarial patches — eval corruptions only | Robust | Common corruptions not exploits | 1 | Process | ROBUST |
| S-691 | Robust: Gaussian noise | Robust |  | 1 | Easy | ROBUST |
| S-692 | Robust: contrast | Robust |  | 1 | Easy | ROBUST |
| S-693 | Robust: fog corruption vs real smoke | Robust |  | 1 | Interesting | SMOKE_ALPHA |
| S-694 | Robust: motion blur | Robust |  | 1 | Easy | ROBUST |
| S-695 | Robust: elastic transform | Robust |  | 1 | Easy | ROBUST |
| S-696 | Robust: histogram shift | Robust |  | 1 | Easy | ROBUST |
| S-697 | Robust: tile dropout | Robust |  | 1 | Easy | ROBUST |
| S-698 | Robust: prompt dropout | Robust |  | 1 | Easy | SAM_PROMPT |
| S-699 | Robust: missing slices in CT | Robust |  | 1 | Easy | SAM2_MEMORY |
| S-700 | Robust: shuffled slice subset | Robust |  | 1 | Easy | SAM2_MEMORY |
| S-701 | Generalization: unseen organ | Gen |  | 1 | Easy | SAM_MEDICAL_GAP |
| S-702 | Generalization: unseen modality | Gen |  | 1 | Easy | SAM_MEDICAL_GAP |
| S-703 | Generalization: unseen fire scene | Gen |  | 1 | Easy | FIRE_CONFOUND |
| S-704 | Generalization: unseen camera | Gen |  | 1 | Easy | DET_SHIFT |
| S-705 | Generalization: unseen density range | Gen |  | 1 | Data | SMOKE_ALPHA |
| S-706 | Generalization: unseen prompt protocol | Gen |  | 1 | Easy | SAM_PROMPT |
| S-707 | Generalization: unseen time of day | Gen |  | 1 | Easy | FIRE_CONFOUND |
| S-708 | Generalization: unseen season wildfire | Gen |  | 1 | Data | FIRE_CONFOUND |
| S-709 | Generalization: unseen hospital | Gen |  | 1 | Important | SAM_MEDICAL_GAP |
| S-710 | Generalization: unseen species (vet) | Gen |  | 1 | Niche | SAM_MEDICAL_GAP |
| S-711 | Generalization: unseen age pediatric | Gen |  | 1 | Data | SAM_MEDICAL_GAP |
| S-712 | Failure analysis template: 50 images qualitative | Process | Required Stage 5 | — | Process | EVAL_LEAK |
| S-713 | Stop condition: if oracle-box SAM < UNet by 0.2 Dice, kill SAM-FT story | Process |  | 1 | Process | SAM_MEDICAL_GAP |
| S-714 | Stop: if metric reversal, change paper type to eval | Process |  | 1 | Process | EVAL_LEAK |
| S-715 | Stop: if closest paper is MedSAM+adapter, mutate or kill | Process |  | — | Process | SAM_MEDICAL_GAP |
| S-716 | Stop: if ProFSAM already did detector+SAM2 fire | Process |  | — | Process | FIRE_CONFOUND |
| S-717 | Stop: if InfLoRA already did orthogonal LoRA on cls, require dense evidence | Process |  | — | Process | PEFT_DENSE |
| S-718 | Next wave should add 280+ independent ideas from agents | Process |  | — | Process | META |
| S-719 | Auditor should check echo chamber around SAM | Process |  | — | Process | META |
| S-720 | Supervisor bias: over-weighting eval papers vs methods | Process | Flag for auditor | — | Process | META |
