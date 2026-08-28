# Local VFM/PEFT/SAM pool (Windows1 supervisor backup)

Epistemic status: all Core Hypotheses are HYPOTHESIS. No experimental numbers. Generated to guarantee ≥1000 after two cloud timeouts.

Format: ID | idea | hyp | minExp | cluster | risk

## SAM / promptable segmentation
VFM-0001 | SAM mask quality is dominated by decoder prompt tokens, not image-encoder semantics | Holding encoder frozen and resampling prompts explains more IoU variance than swapping encoders | Fix encoder; sweep click jitter vs encoder swap on same images | SAM | encoder-swap compute
VFM-0002 | Equivalent human prompts (3 jittered clicks) induce IoU variance larger than reported SOTA gaps | Prompt-robustness std exceeds method gaps on COCO/LVIS | 50 images × 20 click samples | SAM | dataset bias
VFM-0003 | Box prompts leak dataset box-convention (tight vs padded) into SAM masks | Training-convention mismatch flips SAM ranking vs click prompts | Dual-convention boxes on same objects | SAM | annotation cost
VFM-0004 | SAM "zero-shot" is mostly boundary completion of a class-agnostic objectness prior | Class-name-conditioned errors persist after removing all class heads | Compare SAM vs class-agnostic objectness on out-of-taxonomy stuff | SAM | definition of stuff
VFM-0005 | Multi-mask ambiguity in SAM is uncalibrated: IoU token does not track true multi-hypothesis entropy | IoU token vs annotator multimodality correlation is near 0 | Multi-rater images; rank correlation | SAM | rater access
VFM-0006 | SAM2 memory bank treats identity persistence as appearance matching and fails under state change | Memory attention drops when object state changes at matched appearance distance | Controlled video with state edits | SAM2 | video GT
VFM-0007 | SAM2 error cascades are predictable from first-frame prompt entropy | First-frame multi-mask entropy predicts occlusion-recovery failure | Correlate; intervene with extra clicks | SAM2 | causal claim
VFM-0008 | Automatic mask generation grid density interacts with object size so AMG rankings are density artifacts | Re-ranking under matched masks-per-object reverses AMG method order | Sweep grid; size-stratify | SAM | compute
VFM-0009 | Negative clicks are not set-subtraction in embedding space | Linear subtraction of negative-click tokens does not equal observed mask change | Probe decoder with constructed tokens | SAM | access to internals
VFM-0010 | Promptable segmenters implement "nearest closed contour" not "named entity" | Text-free SAM beats grounded-SAM on unnamed blobs; reverse on named rare objects | Paired unnamed/named stimuli | SAM | stimulus design
VFM-0011 | Fine-tuning SAM on one dataset destroys prompt-geometry generalization more than class generalization | After FT, click-vs-box consistency collapses more than class mIoU | Measure both | PEFT | confound class vs prompt
VFM-0012 | Decoder-only FT beats full FT for SAM under distribution shift because encoder features are already generic | Decoder-only ≥ full FT on OOD; opposite on ID | ID/OOD split | PEFT | already published suspicion
VFM-0013 | LoRA on SAM image encoder mostly recodes dataset texture, not prompt alignment | LoRA SVD energy concentrates in early blocks correlating with texture probes | Blockwise probes | PEFT | interpretability noise
VFM-0014 | Rank-8 LoRA saturates SAM dense FT; higher rank fits label noise | Rank vs ID-gain/OOD-drop curves cross | Rank sweep | PEFT | noise model
VFM-0015 | Multi-task LoRA merge on SAM is destructive specifically for thin structures | Merged adapters drop connectivity more than Dice | Topology metrics | PEFT | metric choice
VFM-0016 | Prompt-tuning SAM is a dataset key not a concept key | Learned prompts fail when class names stay, images shift | Cross-dataset prompt transfer | PROMPT | class overlap
VFM-0017 | SAM hallucinates completed objects behind occlusion more than humans when local evidence is masked | Counterfactual hole-fill vs human amodal | Amodal GT | SAM | amodal labels
VFM-0018 | Text-prompted SAM variants are bag-of-words at mask level | Scrambled referring phrases keep masks | Phrase scramble | VLM | already in NLP
VFM-0019 | Grounding-SAM failures are localization of the noun, not the modifier | Swap modifiers; mask stays on noun | Controlled captions | VLM | dataset
VFM-0020 | SAM fine-tunes to polygon vertex statistics of the FT set | Predicted contour angle histogram matches train tool | Tool-forensics | EVAL | subtle

## PEFT / forgetting / efficiency myths
VFM-0021 | PEFT "parameter efficiency" is actually regularization; matched-regularization full FT equals LoRA | Full FT with LoRA-equivalent effective capacity matches | Capacity-matched FT | PEFT | how to match capacity
VFM-0022 | Catastrophic forgetting in dense FT is class-frequency weighted, not uniform | Forgetting vs train frequency power law | Plot; intervene on sampling | FORGET | long-tail confound
VFM-0023 | Frozen-encoder + linear head is limited by bilinear readout of patch mixing, not semantics | Learned 3x3 on tokens closes most frozen gap | Tiny mixer vs full FT | VFM | already similar
VFM-0024 | BitFit on ViT mainly adapts LayerNorm scale to target contrast, not task semantics | LN-only vs contrast-normalized data | Ablate | PEFT | too simple
VFM-0025 | Adapter layers become dataset routers: identical adapters on two datasets do not commute | Swap adapters across datasets; collapse | Swap test | PEFT | training noise
VFM-0026 | QLoRA quantization error is absorbed into the segmentation head as boundary jitter, not class error | Error decomposition under 4/8-bit | Metrics split | PEFT | hw variance
VFM-0027 | Continual PEFT on sequential datasets yields lower joint mIoU than single mixed LoRA at same steps | Head-to-head | Continual bench | FORGET | protocol
VFM-0028 | "We only train 1% params" papers hide that the trainable 1% is the entire decision-relevant subspace | Random 1% vs PEFT 1% | Random-mask FT | PEFT | already some NLP
VFM-0029 | Gradient checkpointing vs PEFT: memory-equivalent full FT beats LoRA on OOD | Memory-matched full FT | Engineering | PEFT | engineering not science
VFM-0030 | DoRA vs LoRA gains vanish at matched hyperparameter budget | Nested CV equal budget | Sweep | PEFT | negative result hard to publish

## VFM representation mismatch
VFM-0031 | CLIP patch features are bag-of-local-textures; DINOv2 has more part geometry; gap predicts dense transfer | Probe geometry vs texture; correlate with dense rank | Frozen probes | VFM | probe validity
VFM-0032 | Language-aligned VFMs underperform dense tasks exactly where names are coarse (stuff, materials) | Stuff/thing gap vs noun specificity | Correlate | VLM | ontology
VFM-0033 | MAE-pretrained features win boundaries, CLIP wins categories; fusion papers hide this split | Metric-decomposed comparison | Eval only | VFM | eval paper risk
VFM-0034 | VFM positional embeddings encode crop statistics of pretraining, hurting small objects at image border | Border vs center small-AP after PE interpolation | Measure | VFM | many notes exist
VFM-0035 | Register tokens in DINOv2-with-registers steal high-norm patches that were the only small-object signal | Ablate registers; small-object recall | Ablation | VFM | architecture-specific
VFM-0036 | SigLIP spatial maps are smoother than CLIP; smoothness predicts worse instance separation | Instance-sep vs map TV | Correlate | VLM | correlational
VFM-0037 | Open-vocab segmenters fail on post-cutoff brand names more than on rare-but-old object names | Temporal holdout vocab | Build list | VLM | leakage
VFM-0038 | VFM dense upsamplers invent high-frequency boundaries not in encoder | Mask encoder patches; residual boundary energy | Intervention | VFM | method-specific
VFM-0039 | Feature pyramid on VFM is mostly bilinear zoom; learned laterals add little under shift | Freeze laterals | Ablate | VFM | known suspicion
VFM-0040 | Alignment between image-text cosine and pixel-text cosine is weak; this gap IS the open-vocab dense problem | Measure two cosines | Diagnostic | VLM | maybe known

## Fine-tuning instability
VFM-0041 | Dense FT loss spikes coincide with boundary-token norm blowup, not class-token | Token-wise norms vs loss | Log internals | FT | access
VFM-0042 | Learning-rate / resolution coupling: recipes from 224 pretrain are silently wrong at 1024 FT | Cross of lr × res | Sweep | FT | compute
VFM-0043 | Mixup on dense labels creates phantom classes at overlaps that VFMs memorize | Disable mixup; OOD cal improves | Ablate | FT | common practice
VFM-0044 | EMA of weights hides instability; EMA-off rankings reshuffle SOTA | Train w/o EMA | Compute | EVAL | expensive
VFM-0045 | Few-epoch high-lr FT of VFM is equivalent to last-layer recentering plus mild feature warp | Compare to recentering baseline | Cheap | FT | too reductionist
VFM-0046 | Seed variance of SAM-FT exceeds published 1% Dice gains on small medical sets | 10 seeds | Compute | EVAL | expensive
VFM-0047 | Early-stopping on ID val selects the checkpoint with maximum shortcut use | Compare ID-early vs OOD-best | Dual val | FT | need OOD
VFM-0048 | Gradient conflict between CE and boundary losses is the real reason "hybrid losses" look unstable | Measure cosine of grads | Log | FT | known-ish

## Evaluation / leakage / VFM claims
VFM-0049 | SA-1B overlapping images leak into "zero-shot" COCO eval via near-duplicates | Duplicate search | Search | EVAL | legal/data
VFM-0050 | VFM papers report oracle multi-mask selection; user-click simulation collapses the gap | Simulated user | Protocol | EVAL | simulation fidelity
VFM-0051 | "Zero-shot SAM beats UNet" comparisons use weaker UNet recipes than 2015-2020 SOTA | Re-run strong UNet | Compute | EVAL | unglamorous
VFM-0052 | Promptable models overfit to evaluator click policies | Two labs' clickers disagree on ranking | Human study | EVAL | cost
VFM-0053 | Open-vocab mIoU is dominated by synonym mapping tables not visual skill | Shuffle synonym tables | Ablate mapping | EVAL | hidden tables
VFM-0054 | Using CLIP to filter training data for CLIP-based segmenters is circular contamination | Remove CLIP-filtered data | Retrain | EVAL | compute
VFM-0055 | Benchmark images appear in VFM web pretraining; membership inference on encoders | MI attacks | Privacy methods | EVAL | inconclusive MI
VFM-0056 | Reported SAM medical gains are annotation-time savings not accuracy; accuracy ties UNet at equal clicks | Equal-effort protocol | Human time | MED | already some papers

## Detection + VFM
VFM-0057 | Open-vocab detectors are caption-frequency predictors more than visual rare-object detectors | Correlate AP with web freq at matched visual difficulty | Need difficulty model | DET | hard control
VFM-0058 | Region-text matching fails on attribute binding not region proposals | Swap attributes in two-object scenes | Controlled | VLM | dataset
VFM-0059 | VFM backbones + old detection heads: all "gains" are resolution and training length | Match res and steps | Ablate | DET | negative
VFM-0060 | NMS thresholds transferred from COCO silently kill open-vocab long-tail | Per-class thr vs global | Eval | DET | simple

## Additional SAM/VFM scientific questions (compact)
VFM-0061 | Click location on holes vs rims of rings diagnoses whether SAM uses topology | Ring stimuli | Synthetic | SAM | toy
VFM-0062 | SAM ignores interior holes unless negatively clicked even when holes are named | Hole objects | Dataset | SAM | labels
VFM-0063 | Image encoder attention distance shrinks during dense FT, explaining forgetting of large context | Attention stats | Log | FORGET | correlational
VFM-0064 | Teacher-student on SAM AMG labels amplifies grid artifacts | Distill AMG | Train | SAM | circular
VFM-0065 | MaskIoU head can be replaced by a geometric compactness prior with <1% drop | Replace head | Ablate | SAM | negative
VFM-0066 | SAM's 3 masks correspond to part/object/stuff granularity more than uncertainty | Map to granularity labels | PACO | SAM | maybe known
VFM-0067 | Text-to-mask models cannot negate ("all but the dog") at pixel precision | Negation split | Build | VLM | some referring benches
VFM-0068 | Visual prompt (scribble) transfers across SAM and HQ-SAM better than learned text prompts | Cross-model | Test | PROMPT |
VFM-0069 | HQ-SAM extra tokens overfit to HQSeg-44K camera aesthetic | Aesthetic-shift test | Data | SAM |
VFM-0067b skip
VFM-0070 | Parameter-free test-time prompt ensembling beats weight FT for 1-5 shot dense adaptation | TTA vs FT | Few-shot | PEFT |
VFM-0071 | LoRA dropout is implicit mix of adapters; gains are ensemble not rank | Explicit ensemble of rank-1 | Ablate | PEFT |
VFM-0072 | Visual instruction tuning for dense tasks overfits to template language | Template shift | Test | VLM |
VFM-0073 | Region-level CLIP is not compositional: "red cube on blue" fails crossed | Controlled CLEVR-like | Synth | VLM |
VFM-0074 | Dense caption supervision hurts pure semantic segmentation via object-centric bias | Caption vs mask pretrain | Train | VLM |
VFM-0075 | SAM used as pseudo-labeler for student models transfers SAM's objectness prior, not GT ontology | Ontology disagreement | Measure | SYNTH |
VFM-0076 | Foundation-model uncertainty is peaked on textures never seen, not on semantic novelty | Texture vs semantic OOD | Split | UNC |
VFM-0077 | Batch-norm vs RMSNorm in VFM FT: BN reintroduces dataset fingerprint | Site ID from BN stats | Probe | FT |
VFM-0078 | Resolution-continuous VFMs still have a preferred Nyquist; off-grid objects drop | Scale sweep | Eval | SMALL |
VFM-0079 | Token merging for efficient VFM kills small objects first; reported mIoU hides it | Size-stratify after ToMe | Eval | SMALL |
VFM-0080 | Using SAM to evaluate other models (pseudo-GT) creates a SAM-shaped leaderboard | Swap evaluator | Meta-eval | EVAL |
VFM-0081 | Cross-attention from text to patches in Grounded-SAM is almost uniform on stuff classes | Attention entropy | Log | VLM |
VFM-0082 | Fine-grained classes in open-vocab seg are decided by color words in the name | Ablate color adjectives | Names | VLM |
VFM-0083 | PEFT on detection + segmentation joint training harms both vs two specialists | Joint vs specialist | Train | PEFT |
VFM-0084 | "Universal" segmentation heads cannot represent both amodal and modal without a switch token | Switch vs two heads | Train | AMBIG |
VFM-0085 | Video VFMs' temporal attention is recency-biased; long occlusion is not truly memorized | Occlusion length sweep | Video | SAM2 |
VFM-0086 | Frame-drop augmentation during SAM2 train is not equivalent to real occlusion physics | Real vs synthetic occlusion | Data | SAM2 |
VFM-0087 | Language-free class-agnostic objectness of DINOv2 already explains most "open-vocab" gains when k-meansed | k-means DINOv2 vs OV methods | Cheap | VFM |
VFM-0088 | Concept bottleneck on VFM features predicts which classes can never be separated | Linear CAV overlap | Diag | VFM |
VFM-0089 | Adversarial patches against SAM transfer to HQ-SAM and SAM2 more than to UNets | Transfer matrix | Attack eval defensive | ROBUST |
VFM-0090 | Watermarked stock photos in pretraining create a detectable "stock-photo prior" in SAM | Stock vs amateur photos | Split | EVAL |
VFM-0091 | PEFT merge of medical + natural adapters is worse than natural-only on medical OOD | Merge test | Train | PEFT |
VFM-0092 | Classifier-free guidance analog for mask decoders increases hallucination of complete objects | Guidance sweep | Train | SAM |
VFM-0093 | Dense VFMs fail calibration exactly after the epoch ID mIoU peaks | Dual curves | Log | UNC |
VFM-0094 | Using LLM to generate class definitions for OV seg mainly adds dataset-specific synonyms | LLM defs vs WordNet | Ablate | VLM |
VFM-0095 | Point-prompt invariance training reduces peak IoU more than it reduces prompt variance — frontier unknown | Pareto | Train | SAM |
VFM-0096 | Encoder distillation from SAM to small CNN preserves AMG grid bias | Distill | Train | SAM |
VFM-0097 | Multi-image SAM (one-shot personalization) memorizes instance texture not category | Texture swap | Test | FSZS |
VFM-0098 | "Semantic SAM" granularity tokens are ordinal, not a true tree; tree-inconsistent outputs | Tree audit | Eval | AMBIG |
VFM-0099 | VLM segmenters' person masks encode social-group priors from captions | Demographic audit | Ethics | VLM |
VFM-0100 | Cheap killer: 20-image prompt-jitter study before any SAM-FT paper is submitted | Protocol | Meta | EVAL |

## More VFM (0101-0200) — failures, PEFT, detection, multimodal dense
VFM-0101 | SAM box prompt is secretly a crop-and-segment model; boxes larger than object add no context use | Expand boxes; interior mask unchanged | Intervention | SAM |
VFM-0102 | Click polarity inversion (pos/neg swap) is not antisymmetric in decoder | Swap; residual | Probe | SAM |
VFM-0103 | Mask-to-prompt inversion: recovered clicks cluster at annotation vertices | Invert | Forensic | EVAL |
VFM-0104 | SAM fails when object is defined by function not appearance (empty vs full mug as different) | Affordance split | Data | VLM |
VFM-0105 | Fine-tuning on masks with holes teaches SAM to fill holes | Hole-preserving FT | Train | SAM |
VFM-0106 | Image-encoder last-block CLS is unused in SAM; using it as global gate helps shift | Add gate | Train | SAM |
VFM-0107 | Relative vs absolute positional encodings in SAM explain scale brittleness | Swap PE | Train | SAM |
VFM-0108 | Prompt dropout during FT is the only PEFT that preserves interactivity | Compare dropouts | Train | PEFT |
VFM-0109 | LoRA on Q vs V in SAM decoder have opposite effects on over/under-seg | Split LoRA | Train | PEFT |
VFM-0110 | SAM AMG NMS is the real hyperparameter of "zero-shot"; papers underreport it | Sweep NMS | Eval | EVAL |
VFM-0111 | Class-agnostic vs class-aware FT of SAM: class-aware kills novel classes faster than PEFT rank predicts | Novel split | Train | FORGET |
VFM-0112 | Knowledge distillation from SAM to UNet succeeds only on object-like classes, not stuff | Split metrics | Train | SYNTH |
VFM-0113 | VFM linear-probe mIoU is a better FT predictor than ImageNet acc for dense tasks | Correlate | Diag | EVAL |
VFM-0114 | Multi-scale test-time for VFMs is not scale-equivariant; it's a mixture of specialists | Per-scale unique errors | Eval | EVAL |
VFM-0115 | Text embeddings of class lists are not permutation invariant in OV segmenters | Shuffle class list | Eval | VLM |
VFM-0116 | Softmax over class texts creates a closed set; true open-set needs calibrated reject | Reject eval | Eval | VLM |
VFM-0117 | Region-proposal + CLIP scoring fails when proposal ontology ≠ CLIP ontology | Ontology map | Diag | DET |
VFM-0118 | VFM detection on aerial images fails due to pretraining yaw distribution not GSD | Rotate pretrain stats | Diag | SHIFT |
VFM-0119 | Grounding DINO query overload: extra queries steal from small objects | Query count vs size AP | Sweep | DET |
VFM-0120 | Language-conditioned queries ignore spatial prepositions ("left of") | Prep split | Eval | VLM |
VFM-0121 | PEFT of Grounding-DINO on one vocabulary silently harms others via shared text tower | Other-vocab eval | Train | FORGET |
VFM-0122 | Frozen CLIP text tower + tuned image = one-way mismatch; tuning text destroys zero-shot | Which tower | Train | PEFT |
VFM-0123 | Visual chain-of-thought for dense tasks is verbalized post-hoc not causal | Intervention on CoT | Causal | VLM |
VFM-0124 | Multi-modal PEFT (image+text adapters) overfits to caption style of FT set | Style shift | Train | PEFT |
VFM-0125 | SAM2 object IDs swap under crossing with similar texture, not under crossing with similar motion | Factorial video | Data | SAM2 |
VFM-0126 | Memory attention in SAM2 is closer to last-N frames than to learned importance | Truncate memory | Ablate | SAM2 |
VFM-0127 | Using optical flow to skip SAM2 frames hides error on spinning objects | Spin split | Eval | SAM2 |
VFM-0128 | Video object segmentation GT is more consistent than SAM2 because annotators use identity stories | Human protocol | Study | EVAL |
VFM-0129 | Fine-tuning SAM2 on short clips harms long-clip occlusion recovery | Length split | Train | FORGET |
VFM-0130 | Image SAM vs first-frame SAM2 inconsistency is a free error detector | Disagree map | Diag | UNC |
VFM-0131 | Parameter-efficient video adapters should be temporal-only; spatial LoRA overfits cameras | Split adapters | Train | PEFT |
VFM-0132 | VFM for depth+seg joint: depth head steals high-frequency from seg | Grad conflict | Log | FT |
VFM-0133 | Normal maps from VFMs are the missing cue for transparent objects, not RGB SAM | Fuse normals | Test | AMORPH |
VFM-0134 | Diffusion features (SD) beat DINOv2 on materials, lose on object identity | Split eval | Diag | VFM |
VFM-0135 | Using T2I inversion as dense features leaks the inversion prompt into masks | Prompt leak | Test | VLM |
VFM-0136 | SD-segmentation papers win by extra synthetic data not by diffusion features | Data-matched CNN | Control | SYNTH |
VFM-0137 | VFM + CRF / dense CRF revival: classical pairwise closes more gap than extra adapter rank | CRF vs LoRA | Cheap | PEFT |
VFM-0138 | Test-time training on a single image with SAM consistency is a stronger adapter than LoRA-from-1-image | TTT vs 1-shot LoRA | Cheap | PEFT |
VFM-0139 | Entropy minimization TTA on OV segmenters collapses to majority stuff class | Watch collapse | Diag | SHIFT |
VFM-0140 | Prototype memory of FT classes in VFM is overwritable by 50 images of a new domain | Interference | Train | FORGET |
VFM-0141 | Random spatial jitter of text embeddings models prompt uncertainty better than learned variance | Cheap baseline | Eval | UNC |
VFM-0142 | Pixel-text matching scores are uncalibrated across image area (center bias) | Spatial cal | Eval | UNC |
VFM-0143 | VFM dense eval on 512px hides that production is 4K; ranking flips at 4K | Res sweep | Eval | EVAL |
VFM-0144 | Tile-and-merge for VFMs creates seam objects counted as instances | Seam audit | Eval | SMALL |
VFM-0145 | Using ChatGPT to write class lists for ADE20K-OV is a hidden contribution | Ablate list | Eval | EVAL |
VFM-0146 | Hierarchical class lists vs flat: hierarchy helps rare, hurts mutually exclusive parts | Two lists | Eval | TAIL |
VFM-0147 | SAM does not saturate human click efficiency: optimal next-click ≠ uncertainty sampling | Compare policies | Study | PROMPT |
VFM-0148 | Learned click policy trained on SAM fails on other promptable models | Transfer | Eval | PROMPT |
VFM-0149 | Box+click fusion in SAM is not information-additive | Mutual info | Probe | SAM |
VFM-0150 | Extreme aspect-ratio objects (snakes, tools) fail because of square PE and square AMG | AR-stratify | Eval | SMALL |
VFM-0151 | Color-blind SAM: grayscale FT should not drop if geometry is the claim | Gray eval | Eval | SAM |
VFM-0152 | Infrared/thermal zero-shot SAM fails as texture prior not as domain gap | Texture-matched RGB | Diag | SHIFT |
VFM-0153 | SAR vs optical: SAM objectness is optical-shadow based | Shadow ablation | Diag | SHIFT |
VFM-0154 | Medical SAM papers should report click-count-matched Dice vs nnU-Net | Protocol | Meta | MED |
VFM-0155 | Slice-wise SAM on 3D volumes ignores through-plane consistency more than 2D UNets trained with 3 slices | Compare | Train | MED |
VFM-0156 | LoRA on medical SAM overfits hospital more than anatomy | Site vs organ split | Train | MED |
VFM-0157 | Promptable 3D: a single 3D click is under-specified along the beam; that ambiguity is ignored | Ambiguity study | MED | 
VFM-0158 | VFM features + classic random forest on pixels is a strong baseline papers omit | RF baseline | Cheap | EVAL |
VFM-0159 | Self-training with SAM pseudo-labels on domain B is worse than lightweight FT of a small model on 20 labels | Budget match | Train | WEAK |
VFM-0160 | Active learning with VFM uncertainty samples aesthetics not errors | Aesthetic correlate | Diag | ANNOT |
VFM-0161 | Human-in-the-loop SAM labeling converges to SAM's ontology within 3 generations | Generation study | Costly | ANNOT | HRHR
VFM-0162 | Inter-annotator agreement rises after SAM assistance while accuracy vs gold falls | Gold panel | Study | ANNOT |
VFM-0163 | Correction of SAM is biased to boundary nibble not instance add/delete | Edit taxonomy | Log | ANNOT |
VFM-0164 | VFM pretraining data cutoff vs eval dataset collection date should be mandatory reporting | Policy | Meta | EVAL |
VFM-0165 | Membership of ADE/COCO images in LAION can be bounded with dedup, not guessed | Dedup | Data | EVAL |
VFM-0166 | Parameter-efficient FT should be compared at equal wall-clock not equal trainable params | Protocol | Meta | PEFT |
VFM-0167 | GPU-poor labs using PEFT may still lose to full FT on a bigger GPU; PEFT papers should report both | Report | Meta | PEFT |
VFM-0168 | Gradient accumulation vs true large batch in VFM FT changes boundary quality | Compare | Train | FT |
VFM-0169 | Mixed precision on mask losses underflows thin structure weights | fp16 vs fp32 | Train | FT |
VFM-0170 | Class-balanced losses on OV-seg fight the text-tower prior and increase hallucination | Measure | Train | VLM |
VFM-0171 | Using background "stuff" texts as negatives is a secret ingredient | Ablate | Train | VLM |
VFM-0172 | Temperature of CLIP cosine in dense heads is under-tuned; 0.01 vs 0.07 flips rankings | Sweep T | Eval | EVAL |
VFM-0173 | Multi-label pixels (overlap) are forced exclusive in most VFM heads; that choice is the paper | Multi-hot | Train | AMBIG |
VFM-0174 | Partial labels from bounding boxes + SAM fill-in create a SAM-shaped student | Teacher identity | Diag | WEAK |
VFM-0175 | Cross-image attention for few-shot VFM overfits support background | BG swap | Test | FSZS |
VFM-0176 | In-context visual prompts (SegGPT style) fail when support and query cameras differ more than when classes differ | Factorial | Test | FSZS |
VFM-0177 | In-context color mapping is the actual mechanism of some "generalist" painters | Recolor support | Test | FSZS |
VFM-0178 | Generalist models' task tokens encode output resolution conventions more than task semantics | Swap tokens | Probe | VFM |
VFM-0179 | Unified detection+seg models hide that one task's best ckpt is not the other's | Pareto ckpt | Train | EVAL |
VFM-0180 | Instruction-tuned dense VLMs refuse out-of-policy prompts more than they err | Refusal vs error | Eval | VLM |
VFM-0181 | Visual pointing in VLMs is a different skill from segmentation; papers conflate | Split bench | Eval | VLM |
VFM-0182 | Pixel grounding heatmaps are not masks; converting via threshold is a hidden method | Thr sweep | Eval | EVAL |
VFM-0183 | Chain-of-region reasoning (detect then seg) error compounds superlinearly | Pipeline vs joint | Eval | DET |
VFM-0184 | Using LLM planners to pick SAM prompts is brittle to synonymy | Synonym | Eval | AGENT |
VFM-0185 | Agent loops that re-prompt SAM until consistency stop at local minima of blob compactness | Analyze stops | Diag | AGENT |
VFM-0186 | Tool-using VLMs never call negative clicks; that policy gap is most of interactive deficit | Log tools | Diag | AGENT |
VFM-0187 | Reward models for mask quality trained on IoU disagree with human preference on thin objects | Human study | Study | EVAL |
VFM-0188 | RLHF on segmenters increases over-smoothing | Measure curvature | Train | FT |
VFM-0189 | Direct preference optimization on masks needs pairwise edits not full masks | Protocol | Train | FT |
VFM-0190 | Synthetic preferences from GPT-4V for masks encode GPT's jpeg aesthetic | Shift to RAW | Test | SYNTH |
VFM-0191 | VFM robustness to compression is non-monotonic at codec switch points | Codec sweep | Eval | ROBUST |
VFM-0192 | Adversarial prompts (universal click constellations) exist for SAM | Search | Security | SAM |
VFM-0193 | Universal adversarial image patches that make SAM return empty everywhere | Patch | Security | SAM |
VFM-0194 | Defenses that blur kill thin structures more than they stop patches | Tradeoff | Security | ROBUST |
VFM-0195 | Certified robustness for masks at region level is empty in VFM papers | Note | Meta | ROBUST |
VFM-0196 | Calibration of SAM IoU token vs actual IoU is dataset-specific; a single isotonic map fails OOD | Recal | UNC | 
VFM-0197 | Selective segmentation using IoU-token reject beats MC-dropout on SAM | Compare | UNC |
VFM-0198 | Ensemble of SAM variants disagrees on holes and contacts not on interiors | Disagreement map | UNC |
VFM-0199 | Cheap killer experiment for most SAM-FT papers: prompt-jitter std vs claimed gain | Protocol | Meta | EVAL |
VFM-0200 | Most "novel SAM adapter" papers would fail this jitter test | Prediction | Meta | EVAL |

## VFM 0201-0280
VFM-0201 | Encoder features of SAM are closer to MAE than to CLIP; language fusion is a late graft | CKA | Diag | VFM |
VFM-0202 | Late-grafted language cannot recover spatial binding lost in contrastive pooling | Binding tests | Eval | VLM |
VFM-0203 | Patch size 14 vs 16 vs 8: small-object AP change exceeds typical adapter gains | Sweep patch | Train | SMALL |
VFM-0204 | Register-token high-norm artifacts correlate with AMG false positives | Correlate | Diag | SAM |
VFM-0205 | Removing high-norm patches as in DINOv2 papers would change SAM AMG | Intervention | Diag | SAM |
VFM-0206 | Fine-tune SAM with boundary-only loss: interior class accuracy barely drops | Loss | Train | BOUND |
VFM-0207 | Interior vs boundary parameter split: most LoRA params serve interiors | Split | Diag | PEFT |
VFM-0208 | Sparse expert adapters per class in SAM do not beat one adapter plus classifier | MoE vs one | Train | PEFT |
VFM-0209 | Hypernet-generated adapters from class text overfit to text style | Style | Train | VLM |
VFM-0210 | Cache-based FT (tip-adapter style) for seg needs spatial caches; global cache is a dummy | Spatial vs global | Train | PEFT |
VFM-0211 | Prompt ensembling of class synonyms helps OV-seg only for web-frequent classes | Freq split | Eval | TAIL |
VFM-0212 | Visual-only synonyms (canonical photos) beat text synonyms for rare classes | Photo vs text | Eval | TAIL |
VFM-0213 | One canonical photo as prototype + DINOv2 beats many OV-seg methods on tail | Baseline | Cheap | TAIL |
VFM-0214 | This baseline is missing in related-work tables | Meta | Meta | EVAL |
VFM-0215 | Cross-dataset OV-seg rankings invert when class name language is translated | Translate | Eval | VLM |
VFM-0216 | Tokenization of rare class names in CLIP BPE is the tail problem | Merge tokens | Diag | TAIL |
VFM-0217 | Hyphenated vs spaced class names flip masks | Name variants | Eval | EVAL |
VFM-0218 | Dataset class definitions (ADE vs COCO stuff) disagree more than model variants | Ontology | Eval | EVAL |
VFM-0219 | Model rankings are ontology-contingent | Merge/split classes | Eval | EVAL |
VFM-0220 | VFM for change detection uses shortcuts of shadow time-of-day | Shadow | Diag | SHIFT |
VFM-0221 | Bi-temporal VFMs ignore registration error; reported F1 is registration quality | Perturb reg | Eval | SHIFT |
VFM-0222 | Depth foundation models' errors are the leading cause of "3D SAM" failures | Oracle depth | Diag | SAM |
VFM-0223 | Lifting 2D SAM to 3D via depth copies 2D topology errors into 3D | Audit | Diag | SAM |
VFM-0224 | Gaussian-splat segmentation papers inherit SAM errors then claim 3D novelty | Ablate SAM | Eval | EVAL |
VFM-0225 | Interactive 3D Gaussian seg should be compared to lifted-SAM at equal clicks | Protocol | Eval | EVAL |
VFM-0226 | Radiance-field semantic heads overfit to training views' SAM labels | Held-out view | Eval | SYNTH |
VFM-0227 | Novel-view semantic consistency is a better metric than train-view mIoU for NeRF-seg | Metric | Eval | EVAL |
VFM-0228 | VFM + NeRF is mostly a labeling tool; contribution is engineering | Opinion-as-hyp: oracle labels close gap | Control | EVAL |
VFM-0229 | MobileSAM accuracy drop is almost entirely encoder; decoder copy is fine | Swap encoder | Diag | SAM |
VFM-0230 | Distilled SAM encoders lose hole-awareness first | Hole split | Eval | SAM |
VFM-0231 | Edge-device SAM latency claims omit AMG grid cost which dominates | Profile | Meta | EVAL |
VFM-0232 | Quantized SAM 8-bit: class-agnostic quality holds, prompt-IoU token breaks | Split metrics | Eval | PEFT |
VFM-0233 | Speculative decoding analog for mask tokens is meaningless; masks are not autoregressive | Note | Meta | SAM |
VFM-0234 | Autoregressive mask transformers fail thin structures due to raster order | Order ablate | Train | BOUND |
VFM-0235 | Random-order mask AR vs raster: topology gap | Train | BOUND |
VFM-0236 | Discrete codec of masks (VQ) sets a topology noise floor | Measure | Diag | BOUND |
VFM-0237 | MaskGIT-style parallel mask decode vs SAM decoder: which has better prompt-consistency | Compare | Train | SAM |
VFM-0238 | Consistency models for masks: few-step vs quality on boundaries | Sweep | Train | BOUND |
VFM-0239 | Diffusion-based interactive seg is slower and not more prompt-robust than SAM | Head-to-head | Train | SAM |
VFM-0240 | If true, diffusion-seg papers need a new claim beyond quality | Meta | Meta | EVAL |
VFM-0241 | Flow-matching on signed-distance fields is a better mask generator than RGB diffusion | Compare | Train | BOUND |
VFM-0242 | SDF vs raster supervision gap is larger than architecture gap | Control | Train | BOUND |
VFM-0243 | VFM classification accuracy on crops from GT boxes predicts detection AP better than full-image acc | Correlate | Diag | DET |
VFM-0244 | Open-vocab AP50 vs AP75 gap is localization of unnamed objects | Decompose | Eval | DET |
VFM-0245 | Named entity localization vs common noun: two different VLM skills | Split | Eval | VLM |
VFM-0246 | Proper names in OV detection are web-image retrieval not detection | Retrieval baseline | Cheap | DET |
VFM-0247 | Logo/brand detection with VFMs is trademark-data leakage | Leak tests | Eval | EVAL |
VFM-0248 | Watermarked logos in pretraining inflate brand AP | Brand split | Eval | EVAL |
VFM-0249 | Fairness: VFM person segmentation quality vs Fitzpatrick skin type in ADE/COCO | Audit | Ethics | VLM |
VFM-0250 | Crowded-scene person AMG over-merges dark clothing more | Stratify | Eval | DET |
VFM-0251 | Occlusion order from VFMs is mostly vertical position prior | Scramble y | Diag | VFM |
VFM-0252 | Amodal SAM papers may be recovering this prior | Test | EVAL |
VFM-0253 | Layered decomposition vs amodal masks: different tasks papers mix | Taxonomy | Meta | AMBIG |
VFM-0254 | Transparency vs amodal vs occlusion: three-task diagnostic suite missing | Suite | Eval | AMORPH |
VFM-0255 | VFM on smoke: objectness prior actively hurts (smoke is not an object) | Compare objectness off | Diag | AMORPH |
VFM-0256 | SAM on smoke produces blob envelopes; optical density ignored | Density eval | Eval | AMORPH |
VFM-0257 | Fire is detected as bright blob; reflected firelight is a systematic FP of VFMs | Split | Eval | AMORPH |
VFM-0258 | Thermal+RGB VFM fusion regret under dirty lens on one modality | Corrupt one | Eval | ROBUST |
VFM-0259 | VFM video models on smoke plumes lose identity because plumes violate object permanence | Plume IDs | Eval | AMORPH |
VFM-0260 | A plume tracker should not use SAM2 memory as-is | Baseline | Method | AMORPH |
VFM-0261 | PEFT-for-smoke on SAM destroys natural-object promptability | Measure both | Train | FORGET |
VFM-0262 | Domain-adaptive SAM should report retained SA-1B quality as a constraint | Protocol | Meta | PEFT |
VFM-0263 | Constrained FT: maximize target Dice s.t. SA-1B drop < ε | Pareto | Train | PEFT |
VFM-0264 | This constraint is the true PEFT objective for foundation models | Hyp | Meta | PEFT |
VFM-0265 | Unconstrained medical SAM-FT is a different (smaller) model that should not use the SAM name | Rhetoric-as-eval: user study of promptability | Study | MED |
VFM-0266 | Zero-conv ControlNet-style for masks: is it just another decoder FT? | Parameter map | Diag | PEFT |
VFM-0267 | Side-tuning vs LoRA vs decoder-FT: three names, one Pareto front | Unify sweep | Train | PEFT |
VFM-0268 | Publish the Pareto not the named method | Meta | Meta | EVAL |
VFM-0269 | Hyperparameter search compute in PEFT papers exceeds the claimed savings | Account | Meta | EVAL |
VFM-0270 | A 2-hour full-FT baseline with cosine lr often beats 2-day PEFT search | Replication | Train | PEFT |
VFM-0271 | Claim: community assumption "PEFT is strictly cheaper" is false for dense tasks | Hyp | Meta | ASM |
VFM-0272 | Cheap experiment: time-to-target-mIoU not param count | Protocol | Meta | PEFT |
VFM-0273 | Knowledge retention benchmarks for dense FT do not exist; ImageNet-after-FT is the wrong proxy | Proxy invalid | Eval | FORGET |
VFM-0274 | Retain SA-1B AMG quality + COCO FT as the dual objective | Bench | Eval | FORGET |
VFM-0275 | Replay of 1% SA-1B beats EWC on this dual objective | Compare | Train | FORGET |
VFM-0276 | EWC on ViT is mis-specified because Fisher is not diagonal in attention | Theory | Diag | FORGET |
VFM-0277 | LoRA merge arithmetic for "add medical, subtract natural" does not work on masks | Edit | Train | PEFT |
VFM-0278 | Task vectors for segmentation are not linear in weight space | Linearity test | Train | PEFT |
VFM-0279 | If non-linear, task-arithmetic papers overclaim for dense | Meta | Meta | PEFT |
VFM-0280 | Killer: three-task vector additivity on COCO/ADE/Cityscapes | Cheap-ish | Train | PEFT |

## VFM 0281-0350
VFM-0281 | Cityscapes FT destroys ADE stuff more than ADE things | Split | FORGET |
VFM-0282 | Stuff forgetting is boundary-definition drift not feature wipe | Diag | FORGET |
VFM-0283 | Things forgetting is rare-class wipe | Diag | FORGET |
VFM-0284 | Two forgetting mechanisms need two remedies | Hyp | FORGET |
VFM-0285 | Replay stuff labels, not thing labels, for urban FT | Intervene | FORGET |
VFM-0286 | VFMs' texture bias (Geirhos) still holds at mask level | Cue conflict | ROBUST |
VFM-0287 | Shape-biased training of VFMs improves occlusion, hurts materials | Tradeoff | ROBUST |
VFM-0288 | Material segmentation is the anti-shape task; unified models compromise both | Pareto | VFM |
VFM-0289 | A two-expert VFM (shape vs material) beats unified at equal FLOPs | Train | VFM |
VFM-0290 | Mixture-of-experts routing by local texture statistics | Method | VFM |
VFM-0291 | Routing is just a learned boundary vs interior split | Reduction | VFM |
VFM-0292 | Test that reduction before selling MoE | Protocol | EVAL |
VFM-0293 | Vision-language dense models fail counting in masks (3 apples → 1 blob) | Count split | VLM |
VFM-0294 | Counting error is NMS/instance head not the VLM backbone | Oracle instances | Diag | DET |
VFM-0295 | Referring to "the second person from the left" is still unsolved at pixel level | Bench | VLM |
VFM-0296 | Spatial prepositions in pixel grounding are photograph-composition priors | Flip image | Diag | VLM |
VFM-0297 | Mirror-flip should invert left/right refs; if not, prior is not spatial | Test | VLM |
VFM-0298 | Many OV-seg wins disappear on flipped images | Eval | EVAL |
VFM-0299 | Data-aug with flips during OV-seg FT breaks left/right language | Tradeoff | VLM |
VFM-0300 | Need a chirality-preserving training recipe | Method | VLM |
VFM-0301 | Dense captioning as pretrain: does it help segmentation more than detection? | Split | VLM |
VFM-0302 | If it helps detection more, the signal is box-like not mask-like | Hyp | VLM |
VFM-0303 | Box-supervised VFM segmenters cannot beat SAM without box-to-mask models that ARE SAM | Circular | WEAK |
VFM-0304 | Papers that use SAM to generate GT then beat SAM are teacher-student, not new science | Policy | EVAL |
VFM-0305 | Require student-without-teacher-architecture-copy comparisons | Protocol | EVAL |
VFM-0306 | Pseudo-label noise from SAM is spatially correlated; noise-robust losses assuming iid fail | Noise model | WEAK |
VFM-0307 | Spatially correlated noise needs CRFs or CRF-like, not generalized cross entropy | Compare | WEAK |
VFM-0308 | VFM self-training on unlabeled web images without ontology control drifts to SA-1B ontology | Measure drift | WEAK |
VFM-0309 | Ontology drift is the hidden cost of "unlabeled data is free" | Hyp | ASM |
VFM-0310 | Label a probe set with frozen ontology; track KL of predicted class mix | Protocol | EVAL |
VFM-0311 | CLIP temperature annealing during dense FT is undocumented and decisive | Ablate | FT |
VFM-0312 | Learning the temperature per class is a long-tail method in disguise | Diag | TAIL |
VFM-0313 | Per-class temperature is equivalent to logit adjustment | Theory | TAIL |
VFM-0314 | Cite Menon & Williamson; stop renaming | Meta | EVAL |
VFM-0315 | Many "novel losses for OV-seg" ≈ logit adjustment + CAM | Reduction | EVAL |
VFM-0316 | Reduction test suite for OV-seg losses | Protocol | EVAL |
VFM-0317 | VFM for video instance: identity switches cost more in applications than mAP | Utility | DET |
VFM-0318 | Report identity switches per minute as mandatory | Protocol | EVAL |
VFM-0319 | SAM2 papers under-report ID switches on crowds | Audit | EVAL |
VFM-0320 | Crowd ID switches vs texture-similarity curve | Measure | SAM2 |
VFM-0321 | Re-id features from person-ReID beat SAM2 memory on crowds | Baseline | SAM2 |
VFM-0322 | Missing baseline: DeepSORT-classics + SAM | Cheap | EVAL |
VFM-0323 | If DeepSORT+SAM wins, SAM2 memory is not the contribution | Hyp | EVAL |
VFM-0324 | Contribution may be joint trainability not accuracy | Honest claim | META |
VFM-0325 | Joint trainability is engineering; say so | Meta | META |
VFM-0326 | Scientific question leftover: when does joint memory beat modular ReID? | Regime map | SAM2 |
VFM-0327 | Regime = crowd density × occlusion duration × appearance change | Map | SAM2 |
VFM-0328 | Publish the regime map not a SOTA table | Meta | EVAL |
VFM-0329 | VFM optical flow vs RAFT: where do VFMs win? | Split | VFM |
VFM-0330 | If only on semantics-heavy regions, they lose on textureless motion | Hyp | VFM |
VFM-0331 | Combine: VFM on stuff, RAFT on things | Method | VFM |
VFM-0332 | Test before a new architecture | Protocol | EVAL |
VFM-0333 | Super-resolution before SAM: ranking of SR nets by SAM-IoU ≠ PSNR ranking | Correlate | EVAL |
VFM-0334 | SR that wins PSNR suppresses small lesions (link SEG-0085) | Measure | MED |
VFM-0335 | Task-driven SR for segmentation vs photoreal SR | Compare | SYNTH |
VFM-0336 | Photoreal SR is the wrong pre-process for measurement tasks | Hyp | ASM |
VFM-0337 | Measurement-preserving SR is an inverse-problem with a task loss | Method | MED |
VFM-0338 | VFM as perceptual loss for SR causes SAM-shaped reconstructions | Diag | SYNTH |
VFM-0339 | Circular: SAM-loss SR then eval with SAM | Forbid | EVAL |
VFM-0340 | Independent eval model required | Protocol | EVAL |
VFM-0341 | Restoration (derain/dehaze) before dense VFMs: sometimes hurts by removing cues | Factorial | ROBUST |
VFM-0342 | Dehaze removes smoke signal; never preprocess smoke with dehaze | Safety | AMORPH |
VFM-0343 | Community pipeline "enhance then detect" is unsafe for smoke/fire | Hyp | ASM |
VFM-0344 | Killer: enhance-then-detect vs detect-on-raw for fire datasets | Cheap | AMORPH |
VFM-0345 | VFM low-light enhancement hallucinates structure that detectors treat as objects | Insert dark + enhance | ROBUST |
VFM-0346 | Nighttime detection FPs after enhancement are enhancement artifacts | Typology | DET |
VFM-0347 | Raw-domain VFM (not sRGB) for night | Method | SHIFT |
VFM-0348 | Almost no public raw+mask datasets; that's the bottleneck not the model | Meta | DATA |
VFM-0349 | A small raw+mask set is higher ROI than another SAM adapter | Hyp | ASM |
VFM-0350 | Stop condition for VFM-adapter papers: fail jitter test or fail raw-vs-sRGB or fail dual-objective retain SA-1B | Policy | META |

Local VFM count: 350 (VFM-0001–0350, skip 0069 duplicate numbering). Supervisor will dedup against cloud batch.
