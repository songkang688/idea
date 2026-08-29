# Stage 1 Supervisor Seed Catalog (S-series)

Generated 2026-08-28 by Windows4 PI. Status: **HYPOTHESIS catalog**, not experimental results.
Format is compact by design. IDs: `S-001`…  
Forbidden filler (module-stack, backbone-swap, “apply X to medical”) was excluded.

## Cluster map (seed)

- `SAM_PROMPT` S-001–S-040
- `SAM_MEDICAL_GAP` S-041–S-070
- `SAM2_MEMORY` S-071–S-095
- `SMOKE_ALPHA` S-096–S-125
- `FIRE_CONFOUND` S-126–S-140
- `PEFT_DENSE` S-141–S-175
- `FORGETTING` S-176–S-195
- `EVAL_LEAK` S-196–S-220
- `VLM_DENSE` S-221–S-245
- `DET_SHIFT` S-246–S-265
- `SYNTH_DA` S-266–S-285
- `ASSUMPTION` S-286–S-310
- `CALIB` S-311–S-325
- `FEWSHOT` S-326–S-340
- `NEG_RESULT` S-341–S-360

Protect (high-risk/high-reward): S-007, S-018, S-052, S-079, S-103, S-148, S-183, S-205, S-228, S-292, S-318, S-347
Cheap falsify: S-003, S-012, S-044, S-074, S-099, S-128, S-145, S-199, S-247, S-288

| ID | OneLiner | Problem | Hypothesis | WhyNovel | MinExp | Risk | Cluster |
| S-001 | SAM IoU variance is a prompt geometry effect, not domain gap | Medical SAM papers mix prompt noise with domain shift | Tight-box vs loose-box IoU delta explains more variance than CT vs natural-image encoder distance | Isolates a confound most SAM-medical tables hide | Same 200 images: GT box ±0/4/8/16px vs frozen SAM; ANOVA domain vs prompt-scale | Already implicit in MedIA 2024; may be a note not a paper | SAM_PROMPT |
| S-002 | Point prompts fail because of interior texture, not centroid error | Point-prompt SAM is unstable | Interior entropy around the point predicts failure better than point-to-centroid distance | Reframes “need better points” as “need texture-aware prompts” | Correlate local entropy vs Dice on SAM point prompts | Entropy proxy too crude | SAM_PROMPT |
| S-003 | Box-prompt SAM is secretly a detector-quality benchmark | SAM boxes from GT inflate foundation-model claims | Replacing GT boxes with a weak detector collapses SAM Dice more than swapping ViT-B/H | Attacks unfair GT-box evaluation | COCO/medical: GT-box vs YOLO-box prompts, freeze SAM | Known to careful readers | SAM_PROMPT |
| S-004 | Multi-mask ambiguity is unused supervision | SAM outputs 3 masks; papers take argmax | Selecting by mask-IoU disagreement, not predicted IoU, better matches human intent on nested objects | Uses SAM’s native ambiguity as a signal | Nested-object subset of SA-1B/COCO; compare selection rules | Nested labels scarce | SAM_PROMPT |
| S-005 | Negative points are not symmetric to positive points | Interactive papers treat +/− clicks equally | A negative click reduces FP more than a positive click raises TP, at equal budget | Asymmetric interaction cost | Click simulation on Cityscapes/medical | May be dataset-specific | SAM_PROMPT |
| S-006 | Prompt encoder overfits click protocol | Fine-tuned SAM on points fails on boxes | After point-only FT, box-prompt Dice drops below frozen SAM | Documents protocol overfitting of PEFT | Med dataset: FT points-only, eval boxes | MedSAM already mixes prompts | SAM_PROMPT |
| S-007 | Test-time prompt search overfits the image scorer | SAMPOT-style prompt moves need a proxy score | Unsupervised scorers (CRF, NCut) move prompts toward high-contrast blobs, not the clinical target | Attacks “training-free prompt evolution” | Lung X-ray: SAMPOT vs random walk vs GT-target | Scorer choice cherry-pick | SAM_PROMPT |
| S-008 | Grid ‘everything’ mode measures objectness prior, not segmentation skill | Everything-mode leaderboards | Everything recall of small lesions tracks object-size histogram, not model quality | Evaluation critique | Plot recall vs area deciles | May be obvious | SAM_PROMPT |
| S-009 | SAM predicted IoU is miscalibrated on transparent edges | IoU token used as confidence | ECE of IoU-token vs true IoU is worse on alpha-blended boundaries than opaque | New calibration slice | Synthetic alpha overlays on COCO | Synthetic not real smoke | SAM_PROMPT |
| S-010 | Click location from detector centers is a systematic bias | Auto-prompt pipelines | Detector-center points land on occluders; using box-interior farthest-from-edge is better | Prompt placement science | Fire/smoke + YOLO centers vs erosion-center | Detector dependent | SAM_PROMPT |
| S-011 | Prompt jitter as cheap aleatoric estimate | Uncertainty in SAM is rare | Pixel-wise vote over N box jitters predicts errors better than SAM logits | Training-free uncertainty | Compare jitter-vote vs logit entropy vs error maps | Overlaps FNPC 2023 | SAM_PROMPT |
| S-012 | One extra negative click beats adapter training on FP | PEFT vs interaction | On FP-heavy ultrasound, 1 negative click > Medical-SAM-Adapter with no extra data | Challenges adapter papers’ practical claim | Same 50 images: 1 click vs adapter ckpt | Unfair if adapter not reproduced | SAM_PROMPT |
| S-013 | Prompt type should be instance-adaptive | Papers pick one prompt type | A cheap classifier of (area, contrast, compactness) can choose point vs box vs mask | Meta-prompt policy | Train 1k-image policy, freeze SAM | Policy overfits dataset | SAM_PROMPT |
| S-014 | Mask decoder ignores image on strong boxes | SAM may be a box-to-mask interpolator | Ablating image embeddings inside the box barely changes Dice when boxes are tight | Tests if SAM is “seeing” | Zero image tokens in box; measure Dice | Implementation tricky | SAM_PROMPT |
| S-015 | SAM fails when object is not an ‘object’ | Smoke/fire/stain | Objectness-trained mask decoder cannot represent stuff-like density fields | Problem formulation | Stuff vs thing split; SAM vs dense CRF | “Stuff” known | SAM_PROMPT |
| S-016 | Human prompt noise ≠ random noise | Prompt robustness tests use Gaussian jitter | Radiologist click noise is boundary-seeking; Gaussian jitter overstates robustness | Better noise model | Collect 10 annotators × 20 images | Small user study | SAM_PROMPT |
| S-017 | Multi-object prompts interfere inside decoder | Two boxes in one forward | Joint decoding of two instances changes each mask vs separate forwards | Documents interference | COCO pairs | May be minor | SAM_PROMPT |
| S-018 | SAM’s three masks encode scale, not semantics | Ambiguity interpretation | The 3 masks are nested scale levels more often than distinct objects | Changes how we use multi-mask | Nesting IoU among 3 outputs | Dataset dependent | SAM_PROMPT |
| S-019 | Coarse boxes help more than fine boxes on low contrast | “Tighter is better” assumption | On low-contrast tumors, +20px boxes beat GT-tight boxes | Counter-intuitive prompt | Reproduce He et al. split by contrast | May replicate known | SAM_PROMPT |
| S-020 | Prompt-conditioned features are not causal | Attribution | Interchanging prompt tokens between two objects swaps masks more than swapping image crops | Causal test of prompt dominance | Token swap experiment | Engineering | SAM_PROMPT |
| S-021 | Automatic mask NMS hides duplicate-mode collapse | Everything mode metrics | High everything-AP with low unique-mask entropy means collapse not coverage | Metric | Entropy of mask embeddings | Obscure | SAM_PROMPT |
| S-022 | Iterative clicks saturate because decoder is Markov-1 | Multi-round SAM | Round t mask depends only on last mask+click, ignoring click history beyond 1 | Memoryless interaction | Ablate history encoding | Architecture specific | SAM_PROMPT |
| S-023 | Box prompts leak GT area into SAM | Fairness | Dice vs box-area correlation is as high as Dice vs image features | Confounder | Partial correlation | Reviewers may shrug | SAM_PROMPT |
| S-024 | Extreme aspect-ratio boxes break positional encodings | Failure mode | Thin elongated instruments fail more than area-matched compact organs | Geometry | Tools vs organs, area-matched | Niche | SAM_PROMPT |
| S-025 | SAM ‘stability’ filter discards clinically rare shapes | SA-1B training | Stability-filtered pretraining under-represents amoeboid tumors | Data filter critique | Compare stability scores vs tumor irregularity | Hard to prove | SAM_PROMPT |
| S-026 | Point prompts on 3D projected to 2D are inconsistent | Volumetric interaction | Same 3D click projects to conflicting 2D SAM masks across adjacent slices | 3D prompt physics | CT slice neighborhood | MedSAM-2 related | SAM_PROMPT |
| S-027 | Prompt encoder capacity is unused | PEFT placement | Tuning only prompt encoder matches full decoder FT on box-prompt Dice | Localization of adaptation | LoRA on prompt vs decoder vs encoder | Negative possible | SAM_PROMPT |
| S-028 | Language prompts to SAM via CLIP are a bottleneck of CLIP, not SAM | Grounded SAM | Errors on rare medical terms track CLIP zero-shot, not SAM mask quality | Blame assignment | Swap CLIP vs BioMedCLIP, freeze SAM | Grounded-SAM papers exist | SAM_PROMPT |
| S-029 | Dense positional prompt (scribble) ≠ sparse | Interaction | Equal-length scribbles beat N points with same pixel budget | Budgeted interaction | Scribble vs points | Classic interactive seg | SAM_PROMPT |
| S-030 | SAM fails when GT is a region without an edge | Edge prior | Gradient magnitude at GT boundary predicts SAM Dice better than intensity mean | Edge dependence | Scatter plots | Known qualitatively | SAM_PROMPT |
| S-031 | Confidence-based auto-prompt from detector is miscalibrated | AutoSAM pipelines | Detector conf ≠ SAM success; using detector *size* is better | Recalibrate auto-prompt | Rank correlation | Incremental | SAM_PROMPT |
| S-032 | Mask-prompt refinement overfits previous error type | Iterative masks | Feeding SAM its own mask increases recall but destroys precision on smoke | Error recycling | Smoke video | Specific | SAM_PROMPT |
| S-033 | Dual-prompt conflict is informative | + and − close together | High conflict predicts annotator disagreement better than model entropy | Human uncertainty | Multi-annotator set | Data | SAM_PROMPT |
| S-034 | SAM box prompt is translation-covariant but not scale-covariant | Equivariance | Shift box: mask shifts; scale box 1.2×: mask quality drops nonlinearly | Geometric prior | Synthetic affine | Narrow | SAM_PROMPT |
| S-035 | Empty-prompt semantic SAM is a different model | Semantic-SAM vs SAM | Papers mixing both overclaim ‘SAM’ | Taxonomy | Re-eval with true empty vs prompted | Review issue | SAM_PROMPT |
| S-036 | Prompt dropout during FT is required for protocol robustness | FT recipe | Randomly dropping prompt type in training preserves cross-prompt Dice | Simple recipe paper | Ablate dropout | Maybe unpublished but small | SAM_PROMPT |
| S-037 | SAM decoder temperature changes object count | Decoding | Raising mask-token temperature splits one object into many | Controllable granularity | Sweep temp | Hacky | SAM_PROMPT |
| S-038 | Users click on semantically salient not geometric centers | HCI | Gaze/click maps mismatch erosion centers on medical images | Human prompt model | Small eye-track or click log | Cost | SAM_PROMPT |
| S-039 | Negative region prompts beat negative points for stuff | Stuff segmentation | Box-shaped negative region suppresses background better for smoke | Prompt geometry for stuff | Smoke | Incremental | SAM_PROMPT |
| S-040 | SAM’s image encoder is over-credited vs prompt | Credit assignment | Linear probe on encoder vs full SAM with random prompts | Where skill lives | Probe vs prompted | Known for some FMs | SAM_PROMPT |
| S-041 | Medical domain gap is decoder-local | “Need medical pretrain” | Freezing encoder, FT decoder 1 epoch closes most of MedSAM gap on 2D organs | Challenges full FT | Split FT | May fail on tiny lesions | SAM_MEDICAL_GAP |
| S-042 | 3D gap is anisotropy not ‘medical’ | 3D SAM fails | Resampling CT to isotropic 1mm lifts SAM more than medical FT | Confounder | nnU-Net-style resample | Partial | SAM_MEDICAL_GAP |
| S-043 | Small-target SAM failure is prompt occupancy | Small organs | Dice vs (object pixels / box pixels) collapses across modalities | Scale law | Multi-dataset scatter | Simple | SAM_MEDICAL_GAP |
| S-044 | Ultrasound speckle fools SAM more than domain | US vs CT | Denoising US (NLM) lifts frozen SAM more than LoRA | Preprocess > PEFT | 1 dataset | May not generalize | SAM_MEDICAL_GAP |
| S-045 | Intensity windowing is a hidden prompt | CT/MR | Window/level choice moves SAM Dice as much as point vs box | Hidden hyperparam | Sweep windows | Known to clinicians | SAM_MEDICAL_GAP |
| S-046 | Multi-modal medical FT causes negative transfer | One MedSAM for all | FT on CT drops X-ray Dice below frozen SAM | Negative transfer | Leave-one-modality | MedSAM may already mix carefully | SAM_MEDICAL_GAP |
| S-047 | Laterality and anatomical labels are not in SAM | Semantic-less | SAM cannot distinguish left/right kidney without extra classifier | Limits of promptable | Paired kidneys | Obvious? still under-discussed | SAM_MEDICAL_GAP |
| S-048 | Weak boundaries in MR are a loss-mismatch | Dice on fuzzy | Boundary-F1 and Dice disagree on which model is best for SAM vs UNet | Metric | Rank reversal | Classic | SAM_MEDICAL_GAP |
| S-049 | SAM helps annotation time only for large organs | Human-in-loop claim | Time-study: SAM saves time iff object area > threshold | Practical | 5 raters | HCI cost | SAM_MEDICAL_GAP |
| S-050 | Adapter papers compare to weak 2D UNets | Unfair baselines | vs nnU-Net 3D, adapters lose | Baseline honesty | One public MSD task | Compute | SAM_MEDICAL_GAP |
| S-051 | Pseudo-3D slice-wise SAM disagrees across axes | Axial vs sagittal | Majority-vote across 3 orientations is a stronger baseline than new adapters | Cheap ensemble | MSD | Engineering | SAM_MEDICAL_GAP |
| S-052 | Foundation features hurt when labels are sparse small lesions | Pretrain harm | ImageNet/SAM init < random init on tiny polyp with n=50 | Counter to FM gospel | Small-n curve | Controversial | SAM_MEDICAL_GAP |
| S-053 | Colorization-like appearance gap vs geometry gap | Domain | Histogram matching closes RGB-medical gap more than style GAN | Simple DA | Endoscopy | Old DA | SAM_MEDICAL_GAP |
| S-054 | SAM objectness fights organ-internal partitions | Multi-instance organs | Liver tumor inside liver: SAM prefers whole liver given a tumor point | Hierarchical objects | LiTS | Known failure | SAM_MEDICAL_GAP |
| S-055 | Clinical ‘target’ ≠ connected component | Pathology | SAM cannot represent disconnected tumor burden as one prompt | Problem | BraTS disconnected | Formulation | SAM_MEDICAL_GAP |
| S-056 | Slice thickness shift > scanner shift | Domain | Changing slice thickness drops Dice more than vendor change | Which shift matters | Public CT with metadata | Metadata missing | SAM_MEDICAL_GAP |
| S-057 | SAM GT-box eval is not a clinical protocol | Protocol | Radiologists do not draw tight boxes; simulated noisy boxes needed | Eval | Noise model | Soft | SAM_MEDICAL_GAP |
| S-058 | Fine-tuning SAM destroys zero-shot on natural images | Forgetting | Med FT drops COCO everything-AP a lot | Document cost of MedSAM | Before/after | Expected | SAM_MEDICAL_GAP |
| S-059 | Class-agnostic SAM + tiny classifier beats semantic FT | Decomposition | Frozen SAM masks + linear class head vs full semantic FT | Simplicity | 2D organs | May lose SOTA | SAM_MEDICAL_GAP |
| S-060 | Promptable models are evaluated with oracle prompts | Oracle | Using last-year’s detector as prompt is the true baseline | Protocol | Replace GT box | Social | SAM_MEDICAL_GAP |
| S-061 | MRI contrast phase is a domain, not a modality | Domain taxonomy | Arterial vs delayed phase shift > CT vs MR for liver | Finer domains | Public liver | Data | SAM_MEDICAL_GAP |
| S-062 | SAM fails on metal artifacts in a spatially local way | Robustness | Artifact-masked metrics change method ranking | Eval | CT with implants | Niche | SAM_MEDICAL_GAP |
| S-063 | 2.5D prompts (same point on ±k slices) beat 3D models at low n | Data efficiency | Multi-slice same-prompt SAM > 3D UNet at n<20 | Efficiency | Learning curve | Not SOTA at scale | SAM_MEDICAL_GAP |
| S-064 | Medical ‘fine-tune SAM’ papers share one trick: more masks | Meta | Gains correlate with #FT images not method | Meta-analysis | 20 papers’ tables | Incomplete reporting | SAM_MEDICAL_GAP |
| S-065 | Pathology stains are a color-equivariance test | Stain | Macenko stain-norm lifts frozen SAM more than LoRA | Preprocess | Camelyon | Known DA | SAM_MEDICAL_GAP |
| S-066 | SAM cannot count | Instance | Instance F1 of SAM everything on cells is poor vs Cellpose | Cell domain | Public cells | Cellpose exists | SAM_MEDICAL_GAP |
| S-067 | Overlap organs need mutex constraints SAM lacks | Anatomy | Adding mutex CRF postprocess beats extra adapters | Simple | Multi-organ | Old | SAM_MEDICAL_GAP |
| S-068 | Patient-level split leakage in SAM-medical papers | Leak | Image-level splits inflate FT gains | Re-split | One public set | Social | SAM_MEDICAL_GAP |
| S-069 | Interactive SAM vs nnU-Net is category error | Comparison | Interactive vs automatic should be compared at equal human time | Protocol | Time-matched | Hard | SAM_MEDICAL_GAP |
| S-070 | Foundation medical models still need task heads that SAM lacks | VFM vs SAM | UNI/Virchow features + decoder beat MedSAM on pathology | Which FM | One task | Moving target | SAM_MEDICAL_GAP |
| S-071 | SAM2 memory is appearance-tracking not identity | Video | Identity switches under similar-looking organs | Memory content | Surgical video | Known VOS | SAM2_MEMORY |
| S-072 | Memory bank recency bias | SAM2 | Older slice of a 3D CT is dropped; disease that appears then disappears is lost | 3D as video | Long CT | MedSAM-2 self-sort exists | SAM2_MEMORY |
| S-073 | Unordered medical slices break SAM2 time prior | Assumption | Shuffling slice order changes Dice a lot for vanilla SAM2, not for a bag memory | Time prior | Shuffle test | MedSAM-2 related | SAM2_MEMORY |
| S-074 | One-prompt-all-slices overclaims if anatomy drifts | One-prompt | Prompt on slice 0 fails after 30 slices more than a new point | Drift | Plot Dice vs Δslice | Simple | SAM2_MEMORY |
| S-075 | Memory attention is a confounder of compute | Efficiency | Reducing memory tokens 4× may not drop medical Dice | Distill compute | Ablate memory size | Engineering | SAM2_MEMORY |
| S-076 | SAM2 occlusion head is unused in 3D | Architecture | Occlusion score does not predict disappearing tumors | Head misuse | Correlate | Negative likely | SAM2_MEMORY |
| S-077 | Surgical smoke is an occlusion process SAM2 can model | Dual use | Treat smoke as occluder of instruments, not as the object | Reframe | Endoscopy | Data | SAM2_MEMORY |
| S-078 | Bidirectional memory beats causal for CT | 3D | Forward+backward SAM2 pass > causal | Simple | MSD | Compute 2× | SAM2_MEMORY |
| S-079 | Memory embeddings collapse to position not appearance | Representation | Linear probe of memory: slice index >> appearance | Collapse | Probe | Speculative | SAM2_MEMORY |
| S-080 | Prompt on first frame is a privileged protocol | Video eval | Random-frame prompt drops more than model gaps | Protocol | SA-V subset | Social | SAM2_MEMORY |
| S-081 | SAM2 vs SAM on static medical: memory off | Ablation | Disabling memory on 2D should match SAM; if not, training artifact | Sanity | 2D stills | May match | SAM2_MEMORY |
| S-082 | Long-video fire: memory of flame texture overfits last second | Fire video | Memory reset every k frames beats full memory | Temporal | Fire clips | ProFSAM adjacent | SAM2_MEMORY |
| S-083 | Cross-patient memory is leakage | Personalized | Using previous patient’s memory bank as init is wrong but may lift Dice | Leak test | Swap banks | Ethical | SAM2_MEMORY |
| S-084 | Semantic memory vs visual memory | Open problem | Class token in memory would stop kidney/liver switch | Method | Tiny add-on | Novelty vs MedSAM-2 | SAM2_MEMORY |
| S-085 | Frame-rate mismatch | Video | Subsampling frames changes SAM2 more than resolution | Protocol | Sweep fps | Narrow | SAM2_MEMORY |
| S-086 | SAM2 masklet tracking as annotation tool | Practical | Track-then-correct time vs slice-wise SAM | HCI | 3D annot | Study cost | SAM2_MEMORY |
| S-087 | Memory quality correlates with camera motion not object | Ego | IMU/motion magnitude predicts SAM2 failure | Sensor | Endoscopy | Data | SAM2_MEMORY |
| S-088 | Multi-object memory interference | Decoder | Two objects’ memories mix; sequential single-object tracking is stronger baseline | Interference | DAVIS | Known VOS | SAM2_MEMORY |
| S-089 | 3D spacing as fake time | Physics | Using z-mm as dt vs index as dt changes tracking | Physics | CT | Subtle | SAM2_MEMORY |
| S-090 | SAM2 inherits SAM prompt sensitivity temporally | Amplify | Early prompt error grows exponentially vs slice | Error growth | Plot | Simple | SAM2_MEMORY |
| S-091 | Fine-tune memory attention only | PEFT locus | LoRA on memory attn > image encoder for 3D organs | Where to adapt | Ablation | Incremental | SAM2_MEMORY |
| S-092 | Forget-gate for pathology skip-lesion | Method | Learned skip of non-informative slices | Method | CT | Overlaps self-sort | SAM2_MEMORY |
| S-093 | Evaluation must freeze prompt schedule | Fairness | Papers differ on when they re-prompt | Protocol | Re-eval | Social | SAM2_MEMORY |
| S-094 | Audio/physio sync as extra memory | Multimodal | ECG-gated cardiac SAM2 | New | Public cardiac | Heavy | SAM2_MEMORY |
| S-095 | SAM2 objectness still thing-like | Stuff video | Smoke plumes fragment into many masklets | Stuff | Smoke video | Expected | SAM2_MEMORY |
| S-096 | Binary Dice is the wrong smoke metric | Evaluation | Ranking of models reverses under alpha-MAE vs Dice | Metric paper | Synthetic alpha + real | Need alpha GT | SMOKE_ALPHA |
| S-097 | Smoke is a density field not an instance | Problem | Instance-SAM cannot represent overlapping plumes | Formulation | Overlapping synthetic | Conceptual | SMOKE_ALPHA |
| S-098 | Background prototype methods bake in static camera | DenSiSeg-like | Camera motion kills background prototype | Failure | Handheld smoke | May already fail | SMOKE_ALPHA |
| S-099 | Color deconvolution beats SAM on white smoke | Simple baseline | Physics color model > FM on many smoke sets | Counter FM | Public smoke | May lose on wildfire | SMOKE_ALPHA |
| S-100 | Temporal median background is a missing baseline | Eval | Median-bg + threshold vs deep models | Baseline honesty | Fixed-cam | Old | SMOKE_ALPHA |
| S-101 | SAM edges snap to high-contrast non-smoke | Failure | Trees/clouds steal the mask | Failure atlas | Qualitative+metric | Known | SMOKE_ALPHA |
| S-102 | Semi-transparent GT disagreement is the ceiling | Human | Inter-rater Dice on smoke < many paper gains | Ceiling | 3 raters | Cost | SMOKE_ALPHA |
| S-103 | Train on alpha matting data, test on smoke | Transfer | Transfer from portrait matting helps smoke more than COCO | Adjacent field | 1 FT | Domain | SMOKE_ALPHA |
| S-104 | Optical flow of smoke is not brightness constancy | Physics | Flow losses hurt smoke; photometric warp is invalid | Physics | Ablate flow | Negative | SMOKE_ALPHA |
| S-105 | Fire-as-prompt for smoke | Causal | Segmenting fire first to constrain smoke origin helps | Physics | Pipeline | Confound detector | SMOKE_ALPHA |
| S-106 | Wavelength / NIR is the real solution | Sensor | RGB methods overclaim; NIR channel is a better idea | Problem | If dataset exists | Data | SMOKE_ALPHA |
| S-107 | Synthetic CFD smoke for sim2real | Synthetic | Domain-random CFD > GAN smoke | Sim2real | Small real test | Heavy | SMOKE_ALPHA |
| S-108 | Fog/haze models ≠ smoke | Assumption | Defog networks fail on smoke; they should | Negative | Off-the-shelf dehaze | Easy | SMOKE_ALPHA |
| S-109 | Early-warning needs detection of thin smoke not IoU | Task | AP at 10% density > mIoU correlates with alarm time | Task | Time-to-detect | Labels | SMOKE_ALPHA |
| S-110 | Video memory of SAM2 fragments plumes | SAM2 | Re-merge masklets by color histogram | Method | Video | Incremental | SMOKE_ALPHA |
| S-111 | Uncertainty should be high in alpha 0.2–0.8 band | Calibration | Error concentrated in mid-alpha | Eval | Density GT | Labels | SMOKE_ALPHA |
| S-112 | Crowdsourced binary masks are biased thick | Data | Annotators over-paint smoke; models learn fat masks | Data | Compare to matting GT | Data | SMOKE_ALPHA |
| S-113 | Night fire glare is specular not smoke | Failure | Glare-specific eval slice | Eval | Night set | Niche | SMOKE_ALPHA |
| S-114 | Transparent industrial objects share math with smoke | Unify | Alpha + refraction vs alpha-only | Unify | Trans10k + smoke | Ambitious | SMOKE_ALPHA |
| S-115 | Polarization cameras | Sensor | Polarization lifts transparent glass more than extra LoRA | Sensor vs model | If data | Data | SMOKE_ALPHA |
| S-116 | Boundary band metrics | Eval | Score only the 10px blend band | Metric | Recompute papers | Social | SMOKE_ALPHA |
| S-117 | Smoke as residual to inpainted background | Method | Inpaint-then-subtract vs segment | Alternative | Fixed cam | Classic | SMOKE_ALPHA |
| S-118 | Weather confound | Shift | Rain/fog in wildfire videos dominate errors | Slice | Metadata | Data | SMOKE_ALPHA |
| S-119 | Class imbalance of thin vs thick | Long-tail | Models ignore thin; resample density bins | Train | Histogram | Incremental | SMOKE_ALPHA |
| S-120 | Human false negatives on thin smoke | Ceiling | Models ‘beat’ humans on thin if GT is conservative | Caution | Audit GT | Social | SMOKE_ALPHA |
| S-121 | Multi-view smoke 3D density | 3D | 2D IoU is ill-posed; need tomography-like | Problem | Multi-cam | Hardware | SMOKE_ALPHA |
| S-122 | Text prompt ‘smoke’ in Grounded-SAM is CLIP prior | VLM | CLIP ‘smoke’ matches clouds | Failure | Cloud vs smoke set | Expected | SMOKE_ALPHA |
| S-123 | Legal/forensic needs calibrated density not mask | App | Calibration plots missing in papers | Gap | ECE | Soft | SMOKE_ALPHA |
| S-124 | Distillation from SAM background prior without SAM at test | Deploy | Student without SAM | Distill | FPS | Incremental | SMOKE_ALPHA |
| S-125 | Adversarial white overlays fool smoke detectors | Robust | Tiny white patches | Security | Attack? **eval-only** white-box not requested; use public corruptions | Stay with corruptions not exploits | SMOKE_ALPHA |
| S-126 | Fire segmentation papers are detector-prompted SAM2 | Attribution | Gains vanish if detector AP is matched across methods | Kill novelty of ProFSAM-like | Swap detectors | Crowded | FIRE_CONFOUND |
| S-127 | Flame flicker temporal energy is a free feature | Physics | Bandpass temporal filter is a strong baseline | Baseline | Video | Old | FIRE_CONFOUND |
| S-128 | Color space HSV threshold still competitive | Baseline | Report it or ranking is dishonest | Honesty | Public fire | Social | FIRE_CONFOUND |
| S-129 | Smoke occlusion of fire is a detection not segmentation issue | Task mix | Recall of occluded fire vs mask quality | Split metrics | Video | Simple | FIRE_CONFOUND |
| S-130 | Night vs day domain | Shift | Separate leaderboards | Eval | Split | Simple | FIRE_CONFOUND |
| S-131 | Synthetic fire from games | Sim2real | Game engines overfit orange sprites | Negative | Train game test real | Easy | FIRE_CONFOUND |
| S-132 | Thermal IR is a privileged modality | Sensor | RGB SOTA claims vs IR available | Fairness | Dual cam | Data | FIRE_CONFOUND |
| S-133 | Instance vs stuff fire | Problem | Many cores vs one blob | Formulation | Dataset | Labels | FIRE_CONFOUND |
| S-134 | Safety metric: time-to-alarm | Task | mIoU uncorrelated | Task | Event labels | Data | FIRE_CONFOUND |
| S-135 | MobileSAM2 fire drop is prompt not capacity | Distill | Same prompts, measure | Ablate | Public | Incremental | FIRE_CONFOUND |
| S-136 | Wildfire vs indoor fire is different science | Taxonomy | Do not pool | Split | Two sets | Social | FIRE_CONFOUND |
| S-137 | Reflection on water/windows | Failure | Fire reflections | Slice | Qual | Niche | FIRE_CONFOUND |
| S-138 | Annotator delay vs model latency | Deploy | Human GT is late | Protocol | Video | Soft | FIRE_CONFOUND |
| S-139 | Flame boundary is physically indefinite | Ceiling | Inter-rater on flame edge | Ceiling | Raters | Cost | FIRE_CONFOUND |
| S-140 | Using SAM2 memory on fire tracks the brightest blob | Failure | Brightest-blob tracker baseline | Baseline | Video | Simple | FIRE_CONFOUND |
| S-141 | LoRA on SAM encoder destroys promptability | PEFT harm | After LoRA-seg, zero-shot box Dice on unseen category drops | Document harm | COCO holdout classes | Important | PEFT_DENSE |
| S-142 | Rank-1 LoRA is enough for decoder, not encoder | Rank | Sweep rank per block type | Map | 1 dataset | Incremental | PEFT_DENSE |
| S-143 | DoRA vs LoRA on mask IoU not GLUE | Metric | Dense IoU ranking ≠ NLP ranking | Transfer of PEFT papers | Head-to-head | Compute | PEFT_DENSE |
| S-144 | Adapter location: after LN vs inside attn | Micro | Dense tasks prefer different insertion than cls | Replication | Grid | Crowded PEFT | PEFT_DENSE |
| S-145 | Full FT of ViT-B decoder-only matches ViT-H LoRA | Scale | Size vs PEFT | Pareto | 2 sizes | Compute | PEFT_DENSE |
| S-146 | PEFT on frozen SAM vs train UNet from scratch at n=100 | Data regime | Crossover n | Curve | Public | Important | PEFT_DENSE |
| S-147 | Gradient conflict between prompt-encoder LoRA and decoder LoRA | Conflict | PCGrad vs naive | Opt | 1 task | Incremental | PEFT_DENSE |
| S-148 | PEFT updates the shortcut around the scientific signal | Lottery | Random LoRA directions with same rank almost match trained LoRA on seg | Shock | Random vs trained | High risk of negative | PEFT_DENSE |
| S-149 | QLoRA for SAM is an engineering paper unless VRAM is the question | Scope | Only if 24GB vs 8GB is the story | Deploy | Quantize | Low science | PEFT_DENSE |
| S-150 | Layer-wise learning rates beat extra adapters | Opt | Simple | Sweep | 1 task | Maybe known | PEFT_DENSE |
| S-151 | BitFit (bias-only) on SAM decoder | Extreme PEFT | How far | Measure | 1 task | May fail | PEFT_DENSE |
| S-152 | Prompt-tuning pixels vs prompt-tuning tokens | Prompt | Visual prompt vs SAM prompt tokens | Compare | 1 task | Crowded VPT | PEFT_DENSE |
| S-153 | LoRA merge then eval vs keep adapter | Deploy | Merge error on mask | Measure | 1 | Engineering | PEFT_DENSE |
| S-154 | Multi-tenant LoRA for hospitals | Interference | Two LoRAs sequential vs parallel | CL | 2 datasets | InfLoRA exists for cls | PEFT_DENSE |
| S-155 | Segmentation LoRA should be spatial | Hypothesis | Token-wise LoRA (per-patch rank) beats global | Method | Tiny | Novelty risk | PEFT_DENSE |
| S-156 | Encoder LoRA reduces robustness to intensity window | Side effect | Measure | Window sweep | 1 | Interesting | PEFT_DENSE |
| S-157 | PEFT selection via NAS is overkill | ROI | Random search of insertion matches NAS | Negative | Small NAS | Compute | PEFT_DENSE |
| S-158 | Knowledge distillation + PEFT double counts | Confound | Distill-only vs PEFT-only vs both | Ablate | 1 | Social | PEFT_DENSE |
| S-159 | SAM PEFT papers hide training resolution | Protocol | 1024 vs 512 explains gaps | Re-run | 1 | Social | PEFT_DENSE |
| S-160 | Classifier PEFT results do not transfer to dense | Claim | Reproduce InfLoRA on ADE20K not ImageNet-CL | Transfer | ADE | Compute | PEFT_DENSE |
| S-161 | LoRA on Q but not V changes localization | Mech | Ablate matrices | Mechanistic | 1 | Incremental | PEFT_DENSE |
| S-162 | Spectral alignment of LoRA updates with forgetting | Theory | Overlap of singular vectors vs Dice drop on old task | Measure | 2 tasks | Speculative | PEFT_DENSE |
| S-163 | Adapter fusion arithmetic on masks | Arithmetic | Task analogical: tumor LoRA + style LoRA | Wild | 2 | May fail | PEFT_DENSE |
| S-164 | PEFT for calibration not Dice | Objective | Train LoRA to minimize ECE of masks | Different goal | 1 | Novel-ish | PEFT_DENSE |
| S-165 | Frozen encoder + learned prompt is enough iff objects are COCO-like | Regime | Plot vs objectness | Curve | Multi | Soft | PEFT_DENSE |
| S-166 | Hypernet LoRA from dataset stats | Meta | Predict LoRA from mean/std image | Extreme | Many tasks | High risk | PEFT_DENSE |
| S-167 | PEFT vs test-time adaptation | TTA | TENT on SAM vs LoRA | Compare | 1 shift | Crowded TTA | PEFT_DENSE |
| S-168 | Safety: LoRA can inject spurious correlations | Spurious | Hospital-marker shortcut | Audit | 1 | Important | PEFT_DENSE |
| S-169 | Parameter count vs trainable FLOPs | Honesty | Report both | Protocol | — | Social | PEFT_DENSE |
| S-170 | Shared LoRA across SAM and CLIP | Multimodal | Joint PEFT | Method | 1 | Heavy | PEFT_DENSE |
| S-171 | Early-exit PEFT | Efficient | Exit decoder layers | Method | 1 | Eng | PEFT_DENSE |
| S-172 | LoRA dropout as regularizer for small medical n | Small-n | Helps | Sweep | 1 | Incremental | PEFT_DENSE |
| S-173 | Orthogonal LoRA vs replay for *dense* CL | Vs InfLoRA | Replay of 50 masks beats InfLoRA on ADE | Challenge | CL | InfLoRA crowded | PEFT_DENSE |
| S-174 | PEFT initialization with SVD of full-FT delta | Init | Better than Gaussian | Recipe | 1 | Known variants | PEFT_DENSE |
| S-175 | When PEFT is worse than linear probe on frozen masks | Regime | Frozen SAM everything + probe | Baseline | 1 | Important | PEFT_DENSE |
| S-176 | Mask decoder forgets old prompt types | CL | Train boxes then points: point Dice crash | Protocol CL | 1 | Concrete | FORGETTING |
| S-177 | Encoder does not forget; decoder does | Locus | Freeze encoder during task 2 | Ablate | 2 tasks | Clear | FORGETTING |
| S-178 | Replay of prompts not images | Replay | Store 100 prompt-mask pairs | Cheap | 2 tasks | Novel-ish | FORGETTING |
| S-179 | SAM everything-mode AP as canary of forgetting | Canary | Monitor during medical FT | Tool | 1 | Simple | FORGETTING |
| S-180 | EWC on LoRA A/B | Regularize | Vs InfLoRA on seg | Head-to-head | 2 | Paper exists for cls | FORGETTING |
| S-181 | Task-agnostic inference without oracle task id | Realistic CL | Drop if needs task id | Protocol | — | Social | FORGETTING |
| S-182 | Forgetting is calibration first, Dice second | Order | ECE breaks before Dice | Measure | 2 | Interesting | FORGETTING |
| S-183 | Plasticity of SAM is already low; forgetting overstated | Claim | Task2 gain tiny so ‘forgetting’ is noise | Re-eval | 2 | Contrarian | FORGETTING |
| S-184 | Sequential organs in same modality | CL | Liver then spleen | Practical | MSD | Data | FORGETTING |
| S-185 | Attention drift in SAM decoder | Mech | Rollout change vs Dice drop | Measure | 2 | ARCL-ViT adjacent | FORGETTING |
| S-186 | Co-training old synthetic prompts | Replay | Generate old-style boxes | Method | 2 | Incremental | FORGETTING |
| S-187 | Forgetting of negatives: FP rise | Error type | Old task FPs | Slice | 2 | Simple | FORGETTING |
| S-188 | Consolidation sleep: extra epochs on mix | Recipe |  | 1 | Incremental | FORGETTING |
| S-189 | Multi-hospital sequential | Real | Sites A then B | Data | Privacy | FORGETTING |
| S-190 | VLM captioner FT forgetting of grounding | Multimodal | After caption FT, grounding drops | Measure | 1 | Adjacent | FORGETTING |
| S-191 | SAM2 memory FT forgetting of first-frame prompt skill | Video |  | 1 | Incremental | FORGETTING |
| S-192 | Measure forgetting in parameter space vs function space | Theory | Same | 2 | Speculative | FORGETTING |
| S-193 | Distillation from frozen teacher SAM during FT | LwF | Classic | 1 | Old | FORGETTING |
| S-194 | Whether LoRA rank **increases** forgetting | Rank | Higher rank more forget | Sweep | 2 | Testable | FORGETTING |
| S-195 | Output-space orthogonal gradients for masks | Method | Project mask grads | 2 | Vs InfLoRA | FORGETTING |
| S-196 | Test-set overlap with SA-1B | Leak | Near-duplicate search | Search | COCO/SA | Compute | EVAL_LEAK |
| S-197 | Medical datasets recycled across 50 SAM papers | Leak | Same 10 datasets | Meta | List | Social | EVAL_LEAK |
| S-198 | Dice on small objects is a size metric | Metric | Report Dice vs size bins always | Protocol | — | Known | EVAL_LEAK |
| S-199 | Rank reversal under NSD vs Dice | Boundary | SAM vs UNet swap | Recompute | 1 | Strong | EVAL_LEAK |
| S-200 | Oracle box mIoU as illegal metric for automatic methods | Protocol | Ban it | Re-eval | — | Social | EVAL_LEAK |
| S-201 | Video eval with GT first-frame is semi-oracle | Protocol | Also random frame | Re-eval | — | Social | EVAL_LEAK |
| S-202 | Preprocessing pipelines unpublished | Repro | Intensity window hidden | Audit | 5 papers | Social | EVAL_LEAK |
| S-203 | Seed variance > method gap | Stats | 3 seeds | Rerun | 1 | Social | EVAL_LEAK |
| S-204 | Patient vs slice averaging | Stats | Changes significance | Recompute | 1 | Known | EVAL_LEAK |
| S-205 | Leaderboard climbing via TTA not method | Confound | Disable TTA | Ablate | 1 | Social | EVAL_LEAK |
| S-206 | ImageNet-pretrained encoders on medical still win due to residual learning not features | Claim | Random encoder + long train | Compute | Heavy | EVAL_LEAK |
| S-207 | SAM papers use different prompt jitter | Protocol | Standardize | Re-eval | — | Social | EVAL_LEAK |
| S-208 | mAP for detection of fire with tiny objects | Metric | AP_S missing | Report | 1 | Simple | EVAL_LEAK |
| S-209 | Calibration never reported | Gap | Add ECE | 1 | Simple | EVAL_LEAK |
| S-210 | Human ceiling missing | Gap |  | 1 | Cost | EVAL_LEAK |
| S-211 | Cross-dataset instead of cross-val on same | General |  | 1 | Social | EVAL_LEAK |
| S-212 | Compute-matched baselines | Fair |  | 1 | Social | EVAL_LEAK |
| S-213 | Code not matching paper prompts | Repro |  | 1 | Social | EVAL_LEAK |
| S-214 | Statistical tests uncorrected | Stats |  | Meta | Social | EVAL_LEAK |
| S-215 | Synthetic test sets overfit generators | Leak | New generator | 1 | Incremental | EVAL_LEAK |
| S-216 | Video FPS vs accuracy Pareto missing | Deploy |  | 1 | Eng | EVAL_LEAK |
| S-217 | Privacy leakage of FT SAM via inversion | Safety | Membership | 1 | Heavy | EVAL_LEAK |
| S-218 | Dataset license prevents comparison | Social |  | — | Soft | EVAL_LEAK |
| S-219 | Annotation guidelines unpublished | Data |  | Audit | Cost | EVAL_LEAK |
| S-220 | ‘SOTA’ on 20-image test | Size |  | Meta | Social | EVAL_LEAK |
| S-221 | CLIP heatmaps are not masks | VLM | Thresholded CAM vs SAM | Compare | 1 | Known | VLM_DENSE |
| S-222 | Referring expression seg fails on density language | Language | ‘thin smoke’ vs ‘smoke’ | Slice | 1 | Interesting | VLM_DENSE |
| S-223 | LLaVA describes but cannot point | Grounding |  | 1 | Known | VLM_DENSE |
| S-224 | Dense captions as extra GT | Supervision |  | 1 | Data | VLM_DENSE |
| S-225 | Medical reports misalign with pixel GT | Misalign | Report-trained VLM worse for masks | Measure | 1 | Important | VLM_DENSE |
| S-226 | Open-vocab seg is detector+SAM in disguise | Attribution |  | Swap | 1 | Kill novelty | VLM_DENSE |
| S-227 | Text prompt sensitivity analogous to click sensitivity | Unify |  | Jitter text | 1 | Nice | VLM_DENSE |
| S-228 | VLM priors fight rare disease appearance | Harm | Text prior reduces recall of atypical | Slice | 1 | Important | VLM_DENSE |
| S-229 | Multilingual prompts for medical | Lang |  | 1 | Incremental | VLM_DENSE |
| S-230 | Chain-of-thought does not help pixels | Negative |  | 1 | Easy | VLM_DENSE |
| S-231 | Region-level contrastive vs pixel | Rep |  | 1 | Crowded | VLM_DENSE |
| S-232 | Grounding DINO boxes as SAM prompts: error propagation | Cascade |  | 1 | Known | VLM_DENSE |
| S-233 | Concept bottleneck masks | XAI |  | 1 | Heavy | VLM_DENSE |
| S-234 | VLM as evaluator of masks | Eval |  | 1 | Risky circular | VLM_DENSE |
| S-235 | Synthetic referring expressions | Data |  | 1 | Incremental | VLM_DENSE |
| S-236 | Hallucinated objects in empty scans | Safety |  | 1 | Important | VLM_DENSE |
| S-237 | Temperature of text encoder changes mask size | Decoding |  | 1 | Curious | VLM_DENSE |
| S-238 | Shared vs separate vision towers | Arch |  | 1 | Crowded | VLM_DENSE |
| S-239 | OCR tokens on medical films | Extra |  | 1 | Data | VLM_DENSE |
| S-240 | Negation in reports (‘no pneumothorax’) | Language |  | 1 | Important | VLM_DENSE |
| S-241 | Region-reward RL for masks | RL |  | Heavy | High risk | VLM_DENSE |
| S-242 | CLIP surgical instrument names | Domain lex |  | 1 | Incremental | VLM_DENSE |
| S-243 | Dense prediction needs pixel-aligned VLMs | Claim | SigLIP vs CLIP | 1 | Crowded | VLM_DENSE |
| S-244 | Teacher VLM labels for SAM FT | Distill |  | 1 | Incremental | VLM_DENSE |
| S-245 | Evaluate on instructions not classes | Protocol |  | 1 | Soft | VLM_DENSE |
| S-246 | Detection of transparent objects is localization of refraction | Problem | Box IoU poor; propose refraction maps |  | Trans10k | Hard | DET_SHIFT |
| S-247 | Small-object AP dominated by resize | Protocol | Tiled inference baseline |  | 1 | Known | DET_SHIFT |
| S-248 | Open-vocab detectors fail on smoke as ‘object’ | Vocab |  | 1 | Expected | DET_SHIFT |
| S-249 | Anchor-free vs SAM prompt boxes | Relation |  | 1 | Incremental | DET_SHIFT |
| S-250 | Domain shift in fire is lighting not shape | Shift |  | 1 | Testable | DET_SHIFT |
| S-251 | Co-occurrence priors: fire implies smoke | Bias |  | 1 | Interesting | DET_SHIFT |
| S-252 | Detector calibration vs downstream SAM | Cascade |  | 1 | Simple | DET_SHIFT |
| S-253 | Semi-supervised detector with SAM pseudo | Loop | Confirm not novel vs papers | Search later | Crowded | DET_SHIFT |
| S-254 | Video detection ID switches | Track |  | 1 | Known | DET_SHIFT |
| S-255 | Copy-paste aug hurts transparent | Aug |  | 1 | Testable | DET_SHIFT |
| S-256 | Weakly supervised bags of frames | Weak |  | 1 | Crowded | DET_SHIFT |
| S-257 | Long-tail instruments in surgery | Tail |  | 1 | Data | DET_SHIFT |
| S-258 | Camera-motion compensation first | Pre |  | 1 | Old | DET_SHIFT |
| S-259 | Label smoothing on fire boxes | Train |  | 1 | Tiny | DET_SHIFT |
| S-260 | Cross-camera retrieval vs detect | Task |  | 1 | Adjacent | DET_SHIFT |
| S-261 | Synthetic rare events | Data |  | 1 | Incremental | DET_SHIFT |
| S-262 | NMS as a scientific choice for overlapping fire | NMS | Soft-NMS | 1 | Old | DET_SHIFT |
| S-263 | Open-set fire vs glare | OOD |  | 1 | Important | DET_SHIFT |
| S-264 | Temporal consistency regularizer | Train |  | 1 | Crowded | DET_SHIFT |
| S-265 | Human false-alarm cost metric | Task |  | 1 | Soft | DET_SHIFT |
| S-266 | Synthetic medical without physics fails | Sim2real |  | 1 | Known | SYNTH_DA |
| S-267 | Diffusion-generated tumors shortcut textures | Shortcut |  | 1 | Important | SYNTH_DA |
| S-268 | GAN smoke lacks multi-scale turbulence | Physics |  | 1 | Testable | SYNTH_DA |
| S-269 | Copy-paste lesions ignore lighting | Aug |  | 1 | Known | SYNTH_DA |
| S-270 | Domain randomization of window/level | CT |  | 1 | Simple | SYNTH_DA |
| S-271 | Text-to-image medical is unsafe eval | Ethics |  | — | Social | SYNTH_DA |
| S-272 | Synthetic labels are too consistent vs human | Gap | Add label noise | 1 | Interesting | SYNTH_DA |
| S-273 | Sim2real for transparent via rendering | Graphics |  | Heavy | Data | SYNTH_DA |
| S-274 | Style transfer as DA is dead? | Negative | Recheck 2024 | 1 | Maybe | SYNTH_DA |
| S-275 | MixUp in mask space vs image | Aug |  | 1 | Incremental | SYNTH_DA |
| S-276 | Synthetic prompts (boxes) for SAM FT | Data |  | 1 | Simple | SYNTH_DA |
| S-277 | Unreal engine fire vs real | Gap |  | 1 | Easy | SYNTH_DA |
| S-278 | Diffusion inversion for tumor counterfactuals | Causal |  | Heavy | Risky | SYNTH_DA |
| S-279 | Domain labels as nuisance | IRM |  | 1 | Crowded | SYNTH_DA |
| S-280 | Test-time histogram matching | TTA |  | 1 | Old | SYNTH_DA |
| S-281 | Self-train with SAM everything | Pseudo | Confirm crowded | Search | Crowded | SYNTH_DA |
| S-282 | Cross-modality paired MRI-CT | DA |  | Data | Known | SYNTH_DA |
| S-283 | Physics-informed intensity | CT |  | 1 | Speculative | SYNTH_DA |
| S-284 | Synthetic rare laterality errors | Safety |  | 1 | Interesting | SYNTH_DA |
| S-285 | Generator memorization of train tumors | Leak |  | 1 | Important | SYNTH_DA |
| S-286 | Bigger SAM always better on medical? | Assumption | ViT-H vs B on small n reverse | Curve | Compute | ASSUMPTION |
| S-287 | More prompts always better? | Assumption | Too many points confuse | Sweep | Easy | ASSUMPTION |
| S-288 | Fine-tuning always helps? | Assumption | FT hurts OOD | Split | Easy | ASSUMPTION |
| S-289 | Foundation model > specialist at low n | Assumption | Opposite on tiny lesions | Curve | Important | ASSUMPTION |
| S-290 | Dice improvements of 1% are clinical | Assumption | Survey clinicians | Qual | Soft | ASSUMPTION |
| S-291 | Promptable is more usable | Assumption | Time-motion study | HCI | Cost | ASSUMPTION |
| S-292 | Pretraining on SA-1B is necessary for SAM-like | Assumption | Train small from scratch on medical | Heavy | High risk | ASSUMPTION |
| S-293 | Memory in SAM2 always helps 3D | Assumption | Ablate | Easy | ASSUMPTION |
| S-294 | Box > point always | Assumption | Contrast slice reverse | Easy | ASSUMPTION |
| S-295 | Uncertainty = error | Assumption | Correlate | Easy | ASSUMPTION |
| S-296 | Ensemble always calibrates | Assumption |  | Easy | ASSUMPTION |
| S-297 | Attention maps explain | Assumption |  | Easy | ASSUMPTION |
| S-298 | IoU token is confidence | Assumption | ECE | Easy | ASSUMPTION |
| S-299 | Medical adapters transfer across organs | Assumption |  | Easy | ASSUMPTION |
| S-300 | Zero-shot SAM is fair without prompts | Assumption |  | Social | ASSUMPTION |
| S-301 | FPS on A100 matters for clinic | Assumption | Edge device | Eng | ASSUMPTION |
| S-302 | More augmentation always helps SAM FT | Assumption |  | Easy | ASSUMPTION |
| S-303 | Class-agnostic is enough for clinic | Assumption |  | Soft | ASSUMPTION |
| S-304 | Video models for 3D CT | Assumption | vs true 3D | Compute | ASSUMPTION |
| S-305 | Synthetic data scales unbounded | Assumption | Curve saturates |  | ASSUMPTION |
| S-306 | VLM can replace annotators | Assumption |  | Cost | ASSUMPTION |
| S-307 | PEFT matches full FT | Assumption | Dense tasks | Compute | ASSUMPTION |
| S-308 | Bigger prompts (text) help dense | Assumption |  | Easy | ASSUMPTION |
| S-309 | Night-time fire is just a domain | Assumption | Different physics | Soft | ASSUMPTION |
| S-310 | Human GT is gold | Assumption | Inter-rater | Cost | ASSUMPTION |
| S-311 | Mask logits are not probabilities | Calib | Temperature per prompt type | 1 | Simple | CALIB |
| S-312 | Pixel-ECE vs region-ECE | Metric | Rank reverse | 1 | Interesting | CALIB |
| S-313 | Selective prediction on SAM | Reject | Abstain low IoU-token | 1 | Incremental | CALIB |
| S-314 | Prompt disagreement as calibration | Method |  | 1 | Vs FNPC | CALIB |
| S-315 | Domain-wise temperature | TTA |  | 1 | Old | CALIB |
| S-316 | Overconfident small objects | Slice |  | 1 | Simple | CALIB |
| S-317 | Underconfident transparent edges | Slice |  | 1 | Simple | CALIB |
| S-318 | Fine-tuning worsens calibration more than Dice | Tradeoff |  | 1 | Important | CALIB |
| S-319 | MC-dropout on decoder only | UQ |  | 1 | Old | CALIB |
| S-320 | Ensembles of prompt types | UQ |  | 1 | Simple | CALIB |
| S-321 | Spatial calibration maps | Eval |  | 1 | Incremental | CALIB |
| S-322 | Clinical decision curve vs Dice | Metric |  | 1 | Soft | CALIB |
| S-323 | OOD smoke vs cloud | OOD |  | 1 | Important | CALIB |
| S-324 | SAM2 occlusion score as uncertainty | Reuse |  | 1 | Simple | CALIB |
| S-325 | Label noise vs model uncertainty | Decompose |  | 1 | Hard | CALIB |
| S-326 | 1-shot SAM is 1-box not 1-image | Clarify |  | Protocol | Social | FEWSHOT |
| S-327 | Prototype in mask-embedding space | Method |  | 1 | Crowded | FEWSHOT |
| S-328 | Fine-tune decoder on 5 images overfits windows | Overfit |  | 1 | Simple | FEWSHOT |
| S-329 | In-context visual prompts (SegGPT-style) vs SAM | Compare |  | 1 | Crowded | FEWSHOT |
| S-330 | Few-shot smoke with density bins not images | Protocol |  | 1 | Interesting | FEWSHOT |
| S-331 | Unlabeled pool matters more than shots | Active |  | 1 | Crowded | FEWSHOT |
| S-332 | Cross-organ few-shot negative transfer |  |  | 1 | Testable | FEWSHOT |
| S-333 | Text as the extra shot | VLM |  | 1 | Crowded | FEWSHOT |
| S-334 | Geometric augmentations as extra shots |  |  | 1 | Simple | FEWSHOT |
| S-335 | Few-shot evaluation variance huge | Stats |  | 1 | Social | FEWSHOT |
| S-336 | Frozen SAM + kNN of crops | Baseline |  | 1 | Simple | FEWSHOT |
| S-337 | Part-based few-shot for instruments |  |  | 1 | Incremental | FEWSHOT |
| S-338 | 0-shot medical is prompt-shot | Taxonomy |  | Social | FEWSHOT |
| S-339 | Meta-learn prompt encoder only |  |  | Heavy | Crowded | FEWSHOT |
| S-340 | Patient-shot vs image-shot | Split |  | 1 | Important | FEWSHOT |
| S-341 | Publish: FT SAM hurts another hospital | Negative |  | 1 | Social | NEG_RESULT |
| S-342 | Publish: SAM2 memory off is better on CT | Negative |  | 1 | Easy | NEG_RESULT |
| S-343 | Publish: LoRA rank 64 < rank 4 on n=30 | Negative |  | 1 | Easy | NEG_RESULT |
| S-344 | Publish: Grounded-SAM worse than detector | Negative |  | 1 | Easy | NEG_RESULT |
| S-345 | Publish: extra synthetic data drops real Dice | Negative |  | 1 | Important | NEG_RESULT |
| S-346 | Publish: ViT-H < UNet on tiny polyps | Negative |  | 1 | Important | NEG_RESULT |
| S-347 | Publish: prompt evolution lowers clinical Dice | Negative |  | 1 | Vs SAMPOT | NEG_RESULT |
| S-348 | Publish: uncertainty does not catch errors | Negative |  | 1 | Easy | NEG_RESULT |
| S-349 | Publish: TTA makes smoke worse | Negative |  | 1 | Easy | NEG_RESULT |
| S-350 | Publish: CLIP text hurts rare findings | Negative |  | 1 | Important | NEG_RESULT |
| S-351 | Publish: 3D-as-video < 2.5D UNet | Negative |  | Compute | NEG_RESULT |
| S-352 | Publish: adapters ≈ decoder FT | Negative |  | 1 | Social | NEG_RESULT |
| S-353 | Publish: more clicks saturate at 3 | Negative |  | 1 | Easy | NEG_RESULT |
| S-354 | Publish: IR fire models don’t transfer to RGB | Negative |  | 1 | Easy | NEG_RESULT |
| S-355 | Publish: matting metrics reverse SOTA | Negative |  | 1 | Metric | NEG_RESULT |
| S-356 | Publish: random boxes as prompts surprisingly strong | Negative |  | 1 | Curious | NEG_RESULT |
| S-357 | Publish: SAM everything useless for stuff | Negative |  | 1 | Expected | NEG_RESULT |
| S-358 | Publish: calibration temperature from val fails OOD | Negative |  | 1 | Easy | NEG_RESULT |
| S-359 | Publish: ensemble of 2 SAMs not worth 2× | Negative |  | 1 | Easy | NEG_RESULT |
| S-360 | Publish: BioMedCLIP vs CLIP: no mask gain | Negative |  | 1 | Testable | NEG_RESULT |
