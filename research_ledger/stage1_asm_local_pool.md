# Local assumption-breaking pool (Windows1 supervisor backup)

All hypotheses are HYPOTHESIS. Assumptions attacked are community defaults, not proven false.

ASM-0001 | More pretraining data always helps dense transfer | After a compute point, extra web data hurts stuff/material mIoU | Subsample pretrain | SCALE | more data always helps | compute
ASM-0002 | Frozen VFM + probe is a lower bound on FT; sometimes it is an upper bound on OOD | Frozen > FT on OOD | ID/OOD | FT | FT always wins | 
ASM-0003 | Calibration tracks accuracy during dense FT | After peak accuracy, ECE worsens while mIoU flat | Dual curves | UNC | cal follows acc |
ASM-0004 | Prompts are cheaper than weights under shift | Under camera shift, prompts break first | Shift split | PROMPT | prompts robust |
ASM-0005 | Synthetic data is free generalization | Synth pretrain increases ID, decreases real-tail | Tail split | SYNTH | synth free |
ASM-0006 | Parameter count of LoRA equals regularization strength not capacity | Matched L2 full FT = LoRA | Control | PEFT | PEFT special |
ASM-0007 | mIoU gains < annotation-noise floor are unpublished noise | Relabel; gap vanishes | Relabel | EVAL | SOTA real |
ASM-0008 | Test-time augmentation is not free: it changes the effective prior | TTA vs prior shift | Eval | EVAL | TTA harmless |
ASM-0009 | Self-training always helps with confident pseudo-labels | Round-1 confidence predicts later drop | Law | WEAK | ST helps |
ASM-0010 | Domain-adversarial alignment helps dense prediction | Under prior shift it hurts rare classes | Split | SHIFT | DANN helps |
ASM-0011 | Multi-task dense learning is synergistic | Pareto: specialists win at equal FLOPs | Compare | MTL | MTL free lunch |
ASM-0012 | Bigger ViT always better for small objects | Small-object AP peaks at medium model | Size curve | SMALL | bigger better |
ASM-0013 | High-res FT is strictly better | Beyond Nyquist of labels, high-res fits annotator jitter | Res sweep | BOUND | high-res better |
ASM-0014 | ImageNet accuracy predicts dense transfer | Rank correlation near 0 among VFMs | Correlate | VFM | IN1k proxy |
ASM-0015 | Linear probing is fair comparison of representations | Probe architecture choice reshuffles rank | Probe suite | EVAL | linear fair |
ASM-0016 | Attention maps explain segmentation | Attention ≠ gradient attribution for masks | Compare | XAI | attention explain |
ASM-0017 | Uncertainty = softmax entropy | Entropy high on boundaries even when correct | Decompose | UNC | entropy=unc |
ASM-0018 | OOD detection for seg is solved by max softmax | Fails on near-OOD weather | Split | UNC | MSP works |
ASM-0019 | Adversarial training helps real robustness | Helps Linf, hurts rain/fog | Split | ROBUST | AT general |
ASM-0020 | Extra loss terms are the path to better boundaries | Data/labels beat losses at matched budget | Budget | BOUND | new loss |
ASM-0021 | Pretraining on classification then dense is optimal order | Reverse order competitive | Order | FT | curriculum obvious |
ASM-0022 | Masked autoencoding is better pretrain for dense than contrastive | Depends on stuff vs things | Split | VFM | MAE dense king |
ASM-0023 | Contrastive is better for open-vocab | Holds only with text; visual contrastive ≠ CLIP | Split | VLM | CLIP unique |
ASM-0024 | Scaling laws from LLM apply to dense mIoU | mIoU saturates; boundary metrics keep scaling | Curves | SCALE | LLM laws transfer |
ASM-0025 | Chinchilla-optimal for dense is same as classif | Dense wants more data less params | Fit | SCALE | same compute opt |
ASM-0026 | Zero-shot means no target labels; using target class names is zero-shot | Name-only is a form of labels | Philosophy-exp: hide names | VLM | zero-shot language |
ASM-0027 | Open-vocab models generalize to new concepts not new names of old concepts | Temporal holdout true new | Holdout | VLM | OV=new concepts |
ASM-0028 | SAM is class-agnostic therefore unbiased | Objectness prior is a class of biases | Audit | SAM | class-agnostic fair |
ASM-0029 | Human-level Dice means solved | Downstream harm can still be large | Utility | MED | Dice=done |
ASM-0030 | Expert GT is a point | Experts are distributions | Multi-rater | AMBIG | GT unique |
ASM-0031 | Consensus GT is better supervision than sampling raters | Sampling raters calibrates better | Train | ANNOT | consensus best |
ASM-0032 | More annotators per image always better | Coverage of more images wins for some classes | Regime | ANNOT | more raters |
ASM-0033 | Active learning beats random at matched labels | Often fails with VFMs as feature extractors | Replay | ANNOT | AL works |
ASM-0034 | Hard examples are useful | Hard-by-loss are label errors | Relabel hard | ANNOT | hard mining |
ASM-0035 | Long-tail methods help rare visual concepts | They help rare names | Name vs visual | TAIL | tail=rare look |
ASM-0036 | Reweighting = resampling for seg | Context statistics break equality | Compare | TAIL | equiv |
ASM-0037 | Class-balanced sampling is safe | Distorts co-occurrence context | Measure | TAIL | CB safe |
ASM-0038 | Copy-paste is harmless context | Implausible paste hurts some classes | Plausibility | SYNTH | copy-paste free |
ASM-0039 | Photorealism of synth is what transfers | Layout realism wins factorial | Factorial | SYNTH | photo needed |
ASM-0040 | Domain randomization width should be max | Optimal width ≈ target variance | Fit | SYNTH | max DR |
ASM-0041 | GAN/diffusion images as extra real | Contamination + artifact learning | Audit | SYNTH | gen=real |
ASM-0042 | Watermarks don't affect downstream | Watermarks become features | Probe | SYNTH | wm invisible |
ASM-0043 | Foundation models don't memorize train images | Size-conditioned MI succeeds for small objects | MI | PRIV | no mem |
ASM-0044 | Privacy of seg models is high because outputs are masks | Masks leak identity (faces) | Attack | PRIV | masks safe |
ASM-0045 | Differential privacy + dense FT is impossible at useful Dice | Tradeoff curve | Train | PRIV | DP useless |
ASM-0046 | Fairness doesn't apply to non-person classes | Person-adjacent objects (wheelchair) inherit | Audit | ETH | only faces |
ASM-0047 | Benchmarks measure the task | They measure the label convention | Convention swap | EVAL | bench=task |
ASM-0048 | mIoU is application-relevant | Weakly correlated with downstream | Correlate | EVAL | mIoU utility |
ASM-0049 | AP50 is enough for detection | AP50 hides localization that apps need | App | DET | AP50 enough |
ASM-0050 | One test set forever is fine | Adaptive overfitting | Fresh probe | EVAL | static test |
ASM-0051 | Public leaderboards are scientific | They are optimizers | Holdout | EVAL | lb science |
ASM-0052 | Multi-seed is overkill | Published gaps < seed std | 10 seeds | EVAL | 1 seed ok |
ASM-0053 | Faster methods can use more TTA at test; fair compare is equal compute | Equal-compute eval | Eval | EVAL | architecture fair |
ASM-0054 | Train recipes should be copied from papers | Under-tuned baselines | Retune | EVAL | paper recipe |
ASM-0055 | nnU-Net is a medical ceiling | VFM+clicks change the problem not the ceiling | Protocol | MED | nnUNet done |
ASM-0056 | SAM beats UNet in medical | At equal interaction/time, often not | Equal effort | MED | SAM medical SOTA |
ASM-0057 | 2D SAM on slices is OK for 3D | Through-plane errors dominate | 3D metric | MED | 2D enough |
ASM-0058 | Dice on small lesions is interpretable | Volume error is the clinical quantity | Volume | MED | Dice clinical |
ASM-0059 | Preprocess (denoise) then seg is safer | Denoise suppresses lesions | Insert lesions | MED | enhance first |
ASM-0060 | Super-resolution helps small lesions | Invents and deletes | Typology | MED | SR helps |
ASM-0061 | Harmonization solves scanner gap | Residual geometric/protocol gap | Decompose | MED | harm enough |
ASM-0062 | Site-as-domain is the right DA unit | Protocol/sequence is | Relabel domains | MED | site=domain |
ASM-0063 | External validation on one site is generalization | Need many sites | Multi | MED | 1 external |
ASM-0064 | Model-expert Dice > inter-expert means superhuman | It means style matching | Annotator ID probe | MED | superhuman |
ASM-0065 | Uncertainty maps help clinicians | Wrong viz can increase anchoring | RCT viz | MED | unc helpful |
ASM-0066 | Assistive AI reduces time | Time shifts to verification | Time study | MED | time save |
ASM-0067 | Automation bias is small with experts | Seeded errors adopted | Seed | MED | experts immune |
ASM-0068 | Topology-preserving losses fix anatomy | They hide uncertainty | Cal | MED | topo loss |
ASM-0069 | Atlas priors are outdated | They still beat extra CNN depth on rare anatomy | Compare | MED | no atlas |
ASM-0070 | Weak labels from reports are free | Alignment noise dominates | Noise | MED | reports free |
ASM-0071 | Self-sup on unlabeled hospital data always helps | Helps the hospital's fingerprint | Site ID | MED | SSL medical |
ASM-0072 | Federated learning is required | Careful replay of public + small local wins | Compare | MED | must FL |
ASM-0073 | 3D models always beat 2.5D | Depends on slice thickness | Sweep | MED | 3D better |
ASM-0074 | Anisotropic voxels should be resampled isotropic | Resample destroys z-info | Compare | MED | iso always |
ASM-0075 | HU windowing is just viz | Window choice is a hyperparameter that flips method rank | Sweep | MED | window trivial |
ASM-0076 | MRI intensity augmentation solves vendor gap | Vendor gap is coil/geometry too | Factor | MED | inten aug |
ASM-0077 | nnU-Net fingerprint is optimal | Fingerprint + VFM backbone untested fairly | Fair | MED | fingerprint done |
ASM-0078 | Medical datasets too small for transformers | With PEFT, size is not the issue; labels are | PEFT | MED | ViT data hungry |
ASM-0079 | Public medical sets represent deployment | Selection bias to easy cases | Hard-case audit | MED | public=deploy |
ASM-0080 | Binary lesion vs background is the task | Clinical task is infiltrative fields | Histo | MED | binary tumor |
ASM-0081 | Smoke is a segmentation problem | It is a density field | Density | AMORPH | smoke=object |
ASM-0082 | Fire is a bright-color problem | Reflection vs emission confusion | Physics | AMORPH | fire=orange |
ASM-0083 | Binary smoke masks are comparable across papers | Thresholds differ | Level-set | AMORPH | binary ok |
ASM-0084 | Synthetic smoke transfers if photoreal | Turbulence stats matter more | Factor | AMORPH | photo smoke |
ASM-0085 | RGB is enough for transparency | Warp/polarization/caustics needed | Cue | AMORPH | RGB glass |
ASM-0086 | IoU of glass predicts grasping | Often not | Grasp | AMORPH | IoU grasp |
ASM-0087 | Dehaze then detect smoke | Dehaze removes smoke | Pipeline | AMORPH | enhance first |
ASM-0088 | Video smoke ID can use SAM2 | Plumes violate object permanence | Track | AMORPH | SAM2 universal |
ASM-0089 | Night smoke is just low light | Illumination physics differs | Day/night | AMORPH | night=dark |
ASM-0090 | Cloud vs smoke needs appearance CNN | Source attachment / motion | Cue | AMORPH | appearance enough |
ASM-0091 | Early warning from stills | Flicker spectra in pre-visible | Temporal | AMORPH | stills enough |
ASM-0092 | Detection mAP captures fire safety | Time-to-detect and FP-cost dominate | Utility | AMORPH | mAP safety |
ASM-0093 | More FP is OK if recall high for fire | Operator flooding | Human | AMORPH | recall-only |
ASM-0094 | Multi-sensor fusion is always better | Fusion regret under one-sensor dirt | Corrupt | ROBUST | fusion better |
ASM-0095 | UAV smoke datasets represent wildfire ops | Altitude/GSD mismatch | Meta | AMORPH | UAV=ops |
ASM-0096 | Segmentation of plumes is well-posed | Instance ID ill-posed | Lineage | AMORPH | well-posed |
ASM-0097 | Human smoke GT is gold | Humans disagree near visibility threshold | Psycho | AMORPH | human gold |
ASM-0098 | Optical flow helps smoke | Flow on translucent is wrong | Measure | AMORPH | flow helps |
ASM-0099 | Background subtraction is obsolete | Strong baseline at cameras | Replay | AMORPH | BG dead |
ASM-0100 | Deep models beat physics features for smoke | Physics features win pre-visible | Split | AMORPH | DL dominates |
ASM-0101 | UDA is safe if entropy falls | Entropy fall can be collapse | Watch | SHIFT | entropy ok |
ASM-0102 | Source-free DA is strictly harder | Sometimes easier (no negative transfer) | Compare | SHIFT | SFDA harder |
ASM-0103 | More source domains always help | Need mixture weights | Mix | SHIFT | more sources |
ASM-0104 | Feature alignment should be global | Spatial domainness varies | Map | SHIFT | global align |
ASM-0105 | Sim2real is a texture problem | Layout may dominate | 2x2 | SHIFT | texture gap |
ASM-0106 | Weather robustness composes | Fog+rain superadditive fail | Compose | SHIFT | compose |
ASM-0107 | Night is low brightness | Glare/bloom bind | Decompose | SHIFT | night=dark |
ASM-0108 | Fine-tuning kills robustness monotonically | Robustness dies at a specific layer/time | Track | ROBUST | monotonic |
ASM-0109 | ImageNet-C predicts real corruptions | Rank correlation weak for seg | Validate | ROBUST | C=real |
ASM-0110 | Adversarial patches in digital = physical | Print-capture gap | Physical | ROBUST | digital=phys |
ASM-0111 | Certified robustness impossible for seg | Region-level cert possible | Method | ROBUST | impossible |
ASM-0112 | TTA adapts to any shift | Fails on label-policy shift | Split | SHIFT | TTA universal |
ASM-0113 | BN adaptation is enough for sensor shift | Head-only thr/NMS may be enough for det | Head | SHIFT | BN enough |
ASM-0114 | If head-only recovers AP, DA papers overclaim | Protocol | DET | DA needed |
ASM-0115 | Continual DA without forgetting ID | Pareto | SHIFT | can have both |
ASM-0116 | Unlabeled target is free of label policy | Policy shift hidden | Dual annot | SHIFT | unlabeled pure |
ASM-0117 | Open-set DA can reject unknowns | Dense unknown is a region problem | Bench | SHIFT | reject works |
ASM-0118 | Gradual drift ≈ many small DA steps | Hysteresis | Drift | SHIFT | no hysteresis |
ASM-0119 | Predict mIoU without labels is impossible | Deployment contract possible | Method | SHIFT | impossible |
ASM-0120 | Go/no-go for UDA can be predicted | Round-0 stats | Method | SHIFT | must try UDA |
ASM-0121 | Few-shot seg measures algorithm | Measures support image choice | Support | FSZS | method>
ASM-0122 | FSS episodes are i.i.d. | Context leakage | Rebuild | FSZS | i.i.d. |
ASM-0123 | Novel classes are novel | Semantic leak from base | Score | FSZS | novel |
ASM-0124 | 1-shot scaling predicts 5-shot | Nonlinear | Fit | FSZS | power law |
ASM-0125 | Prototype mean is OK | Fails on articulated | Split | FSZS | mean proto |
ASM-0126 | FSS can ignore absence | False masks on absence | Absence | FSZS | always present |
ASM-0127 | Stuff few-shot = thing few-shot | Different | Split | FSZS | same |
ASM-0128 | In-context visual prompts = FSS | Camera-shift sensitive | Factor | FSZS | same |
ASM-0129 | Color matching is not the mechanism | Recolor test | Test | FSZS | not color |
ASM-0130 | Human 1-shot uses shape | Models use texture | Cue | FSZS | same as human |
ASM-0131 | Click prompts information-equal across classes | Class-dependent | Measure | PROMPT | equal |
ASM-0132 | More clicks always help | Non-monotonic | Measure | PROMPT | monotonic |
ASM-0133 | Optimal click = uncertainty | Optimal ≠ unc | Policy | PROMPT | unc sampling |
ASM-0134 | Text prompts compose | Fail AND/NOT | Algebra | PROMPT | compose |
ASM-0135 | Learned prompts transfer | Encode dataset | Transfer | PROMPT | transfer |
ASM-0136 | Prompt robustness free with jitter train | Peak IoU tradeoff | Pareto | PROMPT | free robust |
ASM-0137 | Self-reported uncertainty faithful | Unfaithful maps | Compare | PROMPT | faithful |
ASM-0138 | Cross-model prompts transfer | Similarity-limited | Matrix | PROMPT | portable |
ASM-0139 | Granularity can be implicit | Needs explicit token | Token | PROMPT | implicit |
ASM-0140 | Seconds of effort not counted | Should be primary | Protocol | PROMPT | IoU only |
ASM-0141 | Weak supervision is strictly worse than full | Per-dollar sometimes better | Budget | WEAK | full better |
ASM-0142 | CAM failures unpredictable | Predict from PMI | Forecast | WEAK | unpredictable |
ASM-0143 | Points at center are best | Extremities better some classes | Place | WEAK | center |
ASM-0144 | Scribbles topology irrelevant | Topology is the bits | Length | WEAK | topology free |
ASM-0145 | SSL objectives equal for dense | Boundary preservation differs | Probe | WEAK | SSL equal |
ASM-0146 | Consistency = entropy min | Separate effects | Ablate | WEAK | same |
ASM-0147 | Unlabeled order irrelevant | Curriculum exists | Order | WEAK | order free |
ASM-0148 | Contamination of unlabeled with unknown classes rare | Dose-response | Mix | WEAK | clean unlabeled |
ASM-0149 | Motion boundaries = semantic | Class-conditional fail | Atlas | WEAK | motion=sem |
ASM-0150 | Depth edges = semantic edges | Validity map needed | Map | WEAK | depth=sem |
ASM-0151 | Captions contain localization | Bits per construction vary | Measure | WEAK | captions global |
ASM-0152 | Object discovery finds objects | Finds textures | Intervene | WEAK | objects |
ASM-0153 | Count-only cannot yield instances | Identifiable with objectness | Theory | WEAK | impossible |
ASM-0154 | Semi-sup adds value after strong pretrain | Interaction | Account | WEAK | always adds |
ASM-0155 | One labeled 3D slice enough | Failure predictable | Model | WEAK | always enough |
ASM-0156 | Dense contrastive works on uncurated | Curation interaction | Data | WEAK | uncurated ok |
ASM-0157 | Evaluation metrics cannot be gamed | Adversarial metric | Attack | EVAL | ungameable |
ASM-0158 | Protocol details don't matter | Res/TTA/tile flip rank | Audit | EVAL | protocol free |
ASM-0159 | Threshold 0.5 is OK | Per-class thr leakage | Audit | EVAL | 0.5 |
ASM-0160 | Unknown regions can be ignored | Convention artifacts | Standard | EVAL | ignore unk |
ASM-0161 | Catastrophic per-image fail rare if mIoU high | Report fail rate | Metric | EVAL | mIoU enough |
ASM-0162 | Near-duplicates don't inflate | Capacity-dependent | Dedup | EVAL | no leak |
ASM-0163 | Human quality = IoU | Psychometric | Study | EVAL | IoU human |
ASM-0164 | Combined det+seg metrics obvious | Axioms fail | Derive | EVAL | obvious |
ASM-0165 | Prevalence doesn't affect | Surfaces | Reweight | EVAL | prev free |
ASM-0166 | Cross-dataset optional | Mandatory | Matrix | EVAL | optional |
ASM-0167 | Underpowered comparisons OK | Power calc | Tool | EVAL | n=1 ok |
ASM-0168 | Modal/amodal mix OK | Cost | Flags | EVAL | mix ok |
ASM-0169 | Temporal consistency not needed | Flicker | Metric | EVAL | stills enough |
ASM-0170 | Hardness-stratify optional | Default | Report | EVAL | average ok |
ASM-0171 | Provenance irrelevant | Correlate | Datasheet | EVAL | provenance free |
ASM-0172 | Benchmarks predict apps | Criterion validity | Study | EVAL | bench=app |
ASM-0173 | Benchmarks don't age | Drift | Age | EVAL | eternal |
ASM-0174 | Continuous IoU matching unnecessary | Ranking changes | Compare | EVAL | 0.5 IoU |
ASM-0175 | Shared failure taxonomy unnecessary | Accumulation fails | Protocol | EVAL | ad hoc ok |
ASM-0176 | Seed variance < method gap | Often not | Multi-seed | EVAL | seed small |
ASM-0177 | Verified-absence splits unnecessary | FP hidden | Split | EVAL | presence only |
ASM-0178 | Anti-benchmarks unfair | Shared blind spots real | Collect | EVAL | i.i.d. test |
ASM-0179 | Pixel ECE is calibration | Spatial correlation | Region ECE | UNC | pixel ECE |
ASM-0180 | Aleatoric/epistemic split valid | Interventional suite | Test | UNC | split real |
ASM-0181 | Ensemble always helps | Spatial accounting | Where | UNC | ensemble free |
ASM-0182 | Reweighting doesn't affect cal | Predictable miscal | Law | UNC | cal orthogonal |
ASM-0183 | Model unc = human disagreement | Often not | Correlate | UNC | unc=disagree |
ASM-0184 | Selective seg solved by pixel reject | Need regions | Frontier | UNC | pixel reject |
ASM-0185 | Pipeline can ignore unc interface | Minimal interface | Prop | UNC | drop unc |
ASM-0186 | TTA unc = ensemble unc | Different error types | Compare | UNC | same |
ASM-0187 | Cal not transferable | Maybe more than acc | FT | UNC | cal dies |
ASM-0188 | Global temperature enough | Spatial maps | Compare | UNC | global T |
ASM-0189 | Scalar volumes from masks OK | Need coverage | Repeat scan | UNC | scalar ok |
ASM-0190 | Anomaly scores universal | Type-specific | Factorial | UNC | one score |
ASM-0191 | Unc viz obvious | Human-factors | RCT | UNC | any viz |
ASM-0192 | Single-pass epistemic OK | Envelope limited | Map | UNC | deep ens unneeded |
ASM-0193 | Seg posterior is pixelwise indep | Displacement + existence | Factor | UNC | iid pixels |
ASM-0194 | Unc under attack same | Aware attacks | Split | UNC | attack-agnostic |
ASM-0195 | Recalibration vs retrain: retrain wins | Data-efficiency | Shift | UNC | always retrain |
ASM-0196 | Geometric critics useless | Image-blind alarms work | Test | UNC | need image |
ASM-0197 | Conformal pixel coverage = instance coverage | Unit wrong | Plots | UNC | pixel conformal |
ASM-0198 | Boundary distance ECE unnecessary | Dominant miscal | Decompose | UNC | uniform ECE |
ASM-0199 | VoI eval of unc unnecessary | Proper scores enough | Decision | UNC | proper enough |
ASM-0200 | Clean unc bench impossible | Constructed ambiguity | Bench | UNC | only real data |
ASM-0201 | Rare class fail = not enough data | Three mechanisms | Decompose | TAIL | just data |
ASM-0202 | Context always helps tail | Superlinear collapse if ablated | Ablate | TAIL | context good |
ASM-0203 | Tail confusions random | Feature borrowing graph | Graph | TAIL | random |
ASM-0204 | All rares equal | Easy-rare vs confusable | Split | TAIL | one tail |
ASM-0205 | Open-vocab solves tail | Web freq predicts | Freq | TAIL | OV solves |
ASM-0206 | Tail not a privacy issue | MI on tail | MI | TAIL | no privacy |
ASM-0207 | Flat softmax OK | Hierarchical coarsen | Compare | TAIL | flat |
ASM-0208 | Continual tail arrival ignored | Realistic process | Sim | TAIL | static |
ASM-0209 | Compositional rare = atomic rare | Factor | Split | TAIL | same |
ASM-0210 | Groups = classes | Worst-region conditions | Discover | TAIL | class groups |
ASM-0211 | Synthetic tail placement OK | Implausible harms | Place | TAIL | placement free |
ASM-0212 | Per-class thr tuning OK | Leakage | Audit | TAIL | tune thr |
ASM-0213 | State-tail = class-tail | Matched-freq states worse | Compare | TAIL | states easier |
ASM-0214 | Annotation tool irrelevant | Tool is a domain | Matrix | ANNOT | tool free |
ASM-0215 | Model-in-loop labels stable | Ecology drift | Generations | ANNOT | stable |
ASM-0216 | Reviewers catch model errors | Anchoring | Seed | ANNOT | catch |
ASM-0217 | Label noise is iid | Spatial corr biases boundaries | Model | ANNOT | iid noise |
ASM-0218 | AL should optimize images | Optimize seconds | Time | ANNOT | n images |
ASM-0219 | Need gold to rate annotators | Geometry stats suffice | Gold-free | ANNOT | need gold |
ASM-0220 | Prose guidelines enough | Executable specs | Compare | ANNOT | prose |
ASM-0221 | Relabel vs new labels: always new | Crossover law | Law | ANNOT | always new |
ASM-0222 | Label versions don't confound SOTA | Cross-year | Audit | ANNOT | no confound |
ASM-0223 | Annotator fatigue negligible | Time curves | Log | ANNOT | no fatigue |
ASM-0224 | Forced choice OK | Unsure regions | Compare | ANNOT | forced |
ASM-0225 | Verify-then-fix always slower | Threshold exists | Find | ANNOT | slower |
ASM-0226 | Class extent universal | Cultural variation | Geo | ANNOT | universal |
ASM-0227 | Label error discovery unvalidated | Need P/R of instrument | Validate | ANNOT | any detector |
ASM-0228 | Speech editing worse | Timed compare | Time | ANNOT | speech bad |
ASM-0229 | Box conventions homogeneous | Clusters in data | Cluster | ANNOT | one convention |
ASM-0230 | Instance merge noise rare | Merge-tolerant targets | Train | ANNOT | rare |
ASM-0231 | 3D annotation UX irrelevant | Geometry-dependent times | Time | ANNOT | UX free |
ASM-0232 | Pay by time optimal | Value-price | Market | ANNOT | time-pay |
ASM-0233 | VLM frozen features enough spatially | Ceiling | Probe | VLM | frozen enough |
ASM-0234 | Referring is one skill | Negation/count/ordinal split | Phenomena | VLM | one skill |
ASM-0235 | Captions = many masks | Exchange rate | Bits | VLM | captions dense |
ASM-0236 | Absent objects not a problem | False presence | Bench | VLM | always present |
ASM-0237 | Cutoff vocab unnecessary | LLM analog needed | Holdout | VLM | names eternal |
ASM-0238 | Language doesn't override pixels | Canonical shape drag | Counterfactual | VLM | vision first |
ASM-0239 | Attributes bind | Crossed distractors | Bind | VLM | bind |
ASM-0240 | Round-trip consistency useless | Label-free quality | Metric | VLM | useless |
ASM-0241 | English-only OV OK | Pixel multilingual parity | Lang | VLM | EN enough |
ASM-0242 | Left/right is spatial | Frame of reference | FoR | VLM | obvious left |
ASM-0243 | Scope of "the" obvious | Operators | Scope | VLM | obvious |
ASM-0244 | Prompt eng < FT always | Regime map | Map | VLM | FT wins |
ASM-0245 | Concept surgery clean | Collateral | Edit | VLM | clean |
ASM-0246 | All phrases groundable | Predict groundability | Cal | VLM | all ground |
ASM-0247 | No prompt injection on images | Typographic | Attack | VLM | no inject |
ASM-0248 | Paragraph grounding independent | Pixel explained once | Joint | VLM | independent |
ASM-0249 | Affordances from language | Vs geometry | Compare | VLM | language enough |
ASM-0250 | No demographic issue in dense | Audit person queries | Fair | VLM | no issue |
ASM-0251 | Caption noise types equal | Typed corruption | Which | VLM | equal noise |
ASM-0252 | Distill OV lossless | Freq-resolved compression | Curves | VLM | lossless |
ASM-0253 | Duplicate det = NMS | Pairwise test | Method | DET | NMS enough |
ASM-0254 | One confidence score enough | Factorize | Downstream | DET | one score |
ASM-0255 | Missing annotations rare | Measure + PU | Rate | DET | complete GT |
ASM-0256 | Visible=amodal boxes mix OK | Occlusion tradeoff | Split | DET | mix |
ASM-0257 | Fragmentation is model fail | Occluder geometry law | Envelope | DET | model |
ASM-0258 | Objectness is learned magic | Psychophysics probes | Stimuli | DET | magic |
ASM-0259 | AP-optimized detectors count well | Undercount | Count | DET | AP counts |
ASM-0260 | Query detectors unlimited instances | Saturation | Sweep | DET | unlimited |
ASM-0261 | Latency irrelevant to IoU | Moving objects | Lag | DET | still IoU |
ASM-0262 | Context always helps det | Poisoning reach | Range | DET | context good |
ASM-0263 | FP clusters model-specific | Shared blind spots | Multi-model | DET | specific |
ASM-0264 | Strict AP diffs real | Jitter floor | Floor | DET | real diffs |
ASM-0265 | Objectness not transferable | OW transfer | Transfer | DET | not transfer |
ASM-0266 | Need labels to recalibrate det | Track persistence | Unsup | DET | need labels |
ASM-0267 | Box representation irrelevant | App-cost orientation | Cost | DET | boxes equal |
ASM-0268 | Difficulty is model-specific | Predict unseen detector misses | Model | DET | specific |
ASM-0269 | Fleet cameras independent | Cross-cam health | Metric | DET | independent |
ASM-0270 | Equal compute per image fair | Difficulty-gated | Waste | DET | equal compute |
ASM-0271 | Label space given | Utility-driven ontology | Optimize | DET | ontology given |
ASM-0272 | Thresholds transfer under shift | Shape of scores | Re-est | DET | thr transfer |
ASM-0273 | LLM agents with SAM are robust | Synonym brittle | Test | AGENT | robust |
ASM-0274 | Agent loops improve monotonically | Compactness local min | Analyze | AGENT | monotonic |
ASM-0275 | Agents use negative clicks | They don't | Log | AGENT | full toolkit |
ASM-0276 | CoT causal for dense | Post-hoc | Intervene | AGENT | CoT causal |
ASM-0277 | Reward IoU = human pref | Thin objects disagree | Study | AGENT | IoU=pref |
ASM-0278 | RLHF helps masks | Over-smooth | Measure | AGENT | RLHF good |
ASM-0279 | GPT-4V prefs are visual gold | JPEG aesthetic | RAW | AGENT | GPT gold |
ASM-0280 | Tool-use error is backbone | Policy gap | Log | AGENT | backbone |
ASM-0281 | Diffusion features > VFM for dense | Data-matched control | Control | DIFF | diff better |
ASM-0282 | Inversion prompt doesn't leak | Leak test | Test | DIFF | no leak |
ASM-0283 | Few-step mask diffusion enough | Boundary quality | Sweep | DIFF | few-step |
ASM-0284 | AR mask models fine | Raster kills topology | Order | DIFF | AR fine |
ASM-0285 | VQ mask codecs lossless enough | Topology floor | Measure | DIFF | lossless |
ASM-0286 | ControlNet-seg ≠ decoder FT | Param map | Diag | DIFF | different |
ASM-0287 | T2I as infinite data | Contamination | Audit | DIFF | infinite clean |
ASM-0288 | Geometry of T2I images OK | Critic filter | Filter | DIFF | geom ok |
ASM-0289 | Preference SD for masks OK | Aesthetic | Shift | DIFF | pref ok |
ASM-0290 | NeRF-seg novelty is 3D | Inherited 2D SAM error | Ablate | NERF | 3D novelty |
ASM-0291 | Train-view mIoU enough for NeRF-seg | Novel-view consistency | Metric | NERF | train view |
ASM-0292 | Depth oracle wouldn't help 3D SAM | Oracle depth | Diag | NERF | depth fine |
ASM-0293 | Gaussian seg ≠ lifted SAM | Equal click compare | Protocol | NERF | different |
ASM-0294 | Registration error negligible in change det | Perturb | Eval | CHANGE | reg perfect |
ASM-0295 | Change det uses semantics | Shadow time shortcut | Shadow | CHANGE | semantics |
ASM-0296 | Joint depth+seg synergistic | Grad steal | Log | MTL | synergy |
ASM-0297 | Unified task tokens semantic | Encode resolution | Swap | MTL | semantic |
ASM-0298 | Generalist > specialist equal FLOPs | Pareto | Compare | MTL | generalist |
ASM-0299 | In-context painter is generalist intelligence | Color map mechanism | Recolor | FSZS | intelligence |
ASM-0300 | Instruction-tuned dense VLM errs | Often refuses | Refuse vs err | VLM | err |
ASM-0301 | Pointing = segmentation | Split bench | Split | VLM | same |
ASM-0302 | Heatmap = mask | Threshold hidden | Sweep | VLM | same |
ASM-0303 | Detect-then-seg compounding linear | Superlinear | Pipeline | DET | linear |
ASM-0304 | Left/right survives flip | Should invert | Flip | VLM | survives |
ASM-0305 | Flip aug harmless for OV | Breaks chirality | Tradeoff | VLM | harmless |
ASM-0306 | Bigger text encoder always helps dense | Spatial binding lost in pooling | Binding | VLM | bigger text |
ASM-0307 | Late language fusion enough | Binding needs early | Stage | VLM | late ok |
ASM-0308 | CKA(SAM,MAE) high so language graft easy | Binding still fails | Test | VLM | easy graft |
ASM-0309 | Patch size irrelevant vs adapters | Patch > adapter gain on small obj | Sweep | SMALL | patch free |
ASM-0310 | High-norm tokens ignorable | Affect AMG FP | Intervene | SAM | ignorable |
ASM-0311 | MobileSAM drop is decoder | Encoder | Swap | SAM | decoder |
ASM-0312 | Distill preserves holes | Loses holes first | Split | SAM | preserves |
ASM-0313 | Quantization uniform degrade | IoU token breaks first | Split | SAM | uniform |
ASM-0314 | AMG cost negligible | Dominates latency | Profile | SAM | negligible |
ASM-0315 | NMS of AMG not a hyperparam | It is the method | Sweep | SAM | not hp |
ASM-0316 | Oracle multi-mask reporting OK | User sim collapses gap | Sim | SAM | oracle ok |
ASM-0317 | Clicker policy doesn't matter | Lab ranking flip | Study | SAM | policy free |
ASM-0318 | SAM medical papers comparable | Unequal effort | Protocol | SAM | comparable |
ASM-0319 | Keep SAM name after unconstrained FT | Promptability gone | User | SAM | still SAM |
ASM-0320 | Dual objective retain SA-1B unnecessary | Constraint is the point | Pareto | SAM | unnecessary |
ASM-0321 | Replay unnecessary vs EWC | Replay wins dense | Compare | FORGET | EWC enough |
ASM-0322 | Task vectors linear for seg | Non-linear | Test | PEFT | linear |
ASM-0323 | Merge medical+natural adapters OK | Worse OOD | Merge | PEFT | merge ok |
ASM-0324 | Time-to-mIoU = param count | Wall-clock needed | Protocol | PEFT | params=cost |
ASM-0325 | PEFT search cheaper than full FT | Search > FT | Account | PEFT | PEFT cheaper |
ASM-0326 | 2h full FT cannot beat 2d PEFT | Often can | Replicate | PEFT | cannot |
ASM-0327 | Named PEFT methods distinct | One Pareto | Unify | PEFT | distinct |
ASM-0328 | Side-tuning ≠ LoRA ≠ decoder-FT | Same front | Sweep | PEFT | different |
ASM-0329 | Hypernet adapters from text OK | Overfit style | Style | PEFT | ok |
ASM-0330 | MoE adapters needed | One adapter + clf enough | Compare | PEFT | MoE needed |
ASM-0331 | Cache adapters global OK | Need spatial | Compare | PEFT | global ok |
ASM-0332 | LoRA on Q = LoRA on V | Opposite over/under | Split | PEFT | same |
ASM-0333 | Rank more always better | Fits noise | Curve | PEFT | more rank |
ASM-0334 | Multi-task LoRA merge mild | Thin structures die | Topology | PEFT | mild |
ASM-0335 | Random 1% params = PEFT 1% | PEFT chooses subspace | Random | PEFT | any 1% |
ASM-0336 | Memory-matched full FT < LoRA | Full FT wins OOD | Match | PEFT | LoRA better |
ASM-0337 | DoRA > LoRA at equal search | Gap vanishes | Nested | PEFT | DoRA better |
ASM-0338 | BitFit learns semantics | Learns contrast | Ablate | PEFT | semantics |
ASM-0339 | Adapters commute across datasets | Don't | Swap | PEFT | commute |
ASM-0340 | QLoRA error class-level | Boundary jitter | Decompose | PEFT | class-level |
ASM-0341 | Continual PEFT = mixed LoRA | Mixed wins | Compare | PEFT | equal |
ASM-0342 | Decoder-only SAM FT < full ID | Decoder ≥ full OOD | Split | PEFT | decoder worse |
ASM-0343 | Prompt-tune = concept | Dataset key | Transfer | PEFT | concept |
ASM-0344 | Forgetting uniform | Frequency-weighted | Law | FORGET | uniform |
ASM-0345 | Attention distance stable in FT | Shrinks | Log | FORGET | stable |
ASM-0346 | Stuff vs thing forgetting same | Two mechanisms | Split | FORGET | same |
ASM-0347 | Replay things not stuff | Opposite | Intervene | FORGET | things |
ASM-0348 | ImageNet-after-FT proxies dense retain | Invalid | Proxy | FORGET | valid proxy |
ASM-0349 | Fisher diagonal OK for ViT EWC | Mis-specified | Theory | FORGET | OK |
ASM-0350 | Community should stop SAM-adapter papers that fail prompt-jitter vs gain test | Policy | META | adapters progress |

Local ASM count: 350. Dedup later against cloud and SEG.
