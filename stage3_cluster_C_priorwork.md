# Stage 3 — Cluster C Prior-Work Audit (Adversarial Prior-Work Hunter, Sub-Agent I)

**Supervisor:** Windows7 · **Input:** 85 Stage-2 Cluster C survivors · **Default stance:** "this idea has probably already been done."

**Method:** Every survivor was web/arXiv-searched. Papers listed below were found in search; where search failed or confidence in a citation is limited, this is stated explicitly and novelty confidence is lowered. Cross-checked against Cluster A and Cluster B Stage-2 survivor lists for internal duplication.

**Outcome:** 10 KEEP · 8 MUTATE · 67 KILL (C-0279 folded into C-0276 as part of its keep scope).

---

## C-0002 — Text embeddings are just an arbitrary linear classifier for open-vocab segmentation

- **Decision:** MUTATE
- **Closest Prior Works:** Hoffer et al., "Fix your classifier: the marginal value of training the last weight layer" (ICLR 2018) — fixed/random classifiers match trained ones; open-vocab segmentation evaluation critiques showing seen-class dominance (e.g., analyses accompanying OVSeg/SAN-style papers reporting seen vs unseen splits).
- **Existing Work Did:** Established for classification that a fixed random-orthogonal final layer loses almost nothing; OV-seg papers report seen/unseen splits but do not run the random-classifier control.
- **Exact Difference:** The random-orthogonal / shuffled-embedding control has not been published for open-vocabulary dense prediction, where softmax-over-pixels competition changes dynamics.
- **Remaining Novelty:** The control experiment itself, plus decomposing reported OV-seg gains into "text geometry" vs "any-fixed-classifier" components.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Hoffer et al. 2018 ("this is a known control, just re-run"); any OV-seg paper with strong unseen-class gains (would argue geometry demonstrably matters).
- **Reason:** The bare claim is a transplant of a known classification result; but the OV-dense version is genuinely unrun. MUTATED: fold into a resolution-matched, orthogonal-classifier-controlled audit of what OV-seg text towers contribute on *seen* classes specifically (see mutations file, M1).

## C-0004 — LLM decoding actively destroys spatial information in pixel-grounded VLMs

- **Decision:** KILL
- **Closest Prior Works:** F-LMM: "Grounding Frozen Large Multimodal Models" (Wu et al., 2024) — frozen LLM attention already contains grounding signal usable for masks; LISA (Lai et al., CVPR 2024) and follow-ups probing where grounding lives; layer-wise probing literature for MLLMs.
- **Existing Work Did:** Showed frozen instruction-tuned LLMs retain rich spatial/grounding information deep in the stack (F-LMM extracts masks from frozen attention), directly undermining "decoding destroys spatial info."
- **Exact Difference:** The idea's specific layer-sweep (mask head every 4th layer) is not published as such.
- **Remaining Novelty:** Only the exact sweep plot; the headline hypothesis is already contradicted in sign by F-LMM-style results.
- **Novelty Confidence:** High (that the claim is at risk).
- **Reviewer Attack Papers:** F-LMM; LISA; VLM probing papers showing deep layers remain localizable.
- **Reason:** Core hypothesis likely false given existing evidence; the residual (a layer-index curve) is an ablation, not a paper.

## C-0005 — One high-resolution forward pass explains most "language-guided" dense gains

- **Decision:** KILL
- **Closest Prior Works:** "Scaling on Scales (S²)" (Shi et al., 2024) — resolution scaling rivals model scaling for VLMs; MM1 (McKinzie et al., 2024) — image resolution is the single largest design factor; resolution ablations standard in OV-seg papers.
- **Existing Work Did:** Quantified that resolution dominates many multimodal gains; dense-prediction papers routinely ablate resolution/TTA.
- **Exact Difference:** A cross-paper resolution-matched audit specifically of "language-guided" segmentation pipelines is not published as a standalone study.
- **Remaining Novelty:** Thin — an audit whose likely conclusion ("resolution matters a lot") is already community knowledge with citations.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** S²; MM1.
- **Reason:** The mechanism is established; an audit repackaging it will be rejected as known. The valuable orthogonal-control content is folded into the C-0002 mutation (M1).

## C-0007 — Prompt engineering for segmentation is logit calibration in disguise

- **Decision:** KILL
- **Closest Prior Works:** Allingham et al., "A Simple Zero-Shot Prompt Weighting Technique to Improve Prompt Ensembling" (ICML 2023); Menon et al., "Long-tail learning via logit adjustment" (ICLR 2021); CoOp (Zhou et al., IJCV 2022) — learned prompts as continuous re-weighting.
- **Existing Work Did:** Showed prompt ensembles act largely through re-weighting/calibration of class logits in zero-shot classification; logit adjustment is a mature tool.
- **Exact Difference:** The pixel-softmax (spatial competition) version of the decomposition is not explicitly published.
- **Remaining Novelty:** Small: the same decomposition with a spatial softmax; strong prior that the answer transfers unchanged from classification.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Allingham et al. 2023; CoOp.
- **Reason:** The classification result is close enough that reviewers will see this as a port, not a finding.

## C-0009 — Patchification aliasing, not attention, bounds VLM boundary quality

- **Decision:** KILL
- **Closest Prior Works:** Zhang, "Making Convolutional Networks Shift-Invariant Again" (ICML 2019) — anti-aliasing; Xiao et al., "Early Convolutions Help Transformers See Better" (NeurIPS 2021) — conv stem vs patchify stem; FlexiViT (Beyer et al., CVPR 2023) — patch-size effects.
- **Existing Work Did:** Established that patchify stems are suboptimal and that anti-aliasing/conv stems change ViT behavior; patch-size/boundary interactions studied via FlexiViT-style resizing.
- **Exact Difference:** The specific boundary-F-score-vs-interior-mIoU dissociation under an anti-aliased stem at equal token count is not published.
- **Remaining Novelty:** A plausible ablation, but requires retraining CLIP from scratch to test, and the conceptual claim (stem hurts boundaries) is anticipated by Xiao et al.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Xiao et al. 2021; Zhang 2019.
- **Reason:** High compute for a result whose direction is already suggested by prior stem studies; kill on cost/novelty ratio.

## C-0014 — Self-attention "surgery" methods for CLIP segmentation equal Gaussian smoothing

- **Decision:** MUTATE
- **Closest Prior Works:** NACLIP (Hajimiri et al., 2024) — inserts a Gaussian-kernel neighborhood prior into CLIP attention for training-free segmentation; SCLIP (Wang et al., 2024); GEM (Bousselham et al., CVPR 2024); CLIP Surgery (Li et al., 2023).
- **Existing Work Did:** NACLIP already shows a Gaussian spatial prior inside attention is competitive — i.e., half the hypothesis is published as a *method*, not as a debunk.
- **Exact Difference:** No paper runs the embarrassing-baseline comparison: a *post-hoc* tuned Gaussian/bilateral filter on vanilla CLIP similarity maps, tuning-budget-matched against the attention-surgery family.
- **Remaining Novelty:** The matched-budget equivalence test across the whole surgery family (SCLIP/GEM/CLIP-Surgery/NACLIP) with a filter baseline.
- **Novelty Confidence:** Medium (NACLIP is dangerously close; framing must be "equivalence audit," not "Gaussian prior works").
- **Reviewer Attack Papers:** NACLIP ("we already showed the Gaussian prior — inside attention"); GEM ("our gains exceed any smoothing").
- **Reason:** MUTATED to the precise untested remainder: tuning-budget-matched post-hoc filter equivalence audit (M2). As a plain claim it would be scooped by NACLIP.

## C-0022 — Feature upsampling choice matters more than backbone choice

- **Decision:** KILL
- **Closest Prior Works:** FeatUp (Fu et al., ICLR 2024) — model-agnostic feature upsampling, benchmarked across backbones; LoftUp (2024/2025) and successor upsamplers with cross-backbone comparisons.
- **Existing Work Did:** Benchmarked upsamplers across multiple backbones and tasks; showed large boundary-quality effects from upsampling choice.
- **Exact Difference:** The formal ANOVA/variance-decomposition framing (upsampler main effect vs backbone main effect) is not published.
- **Remaining Novelty:** Just the statistical framing over an experiment grid that substantively exists in FeatUp-lineage papers.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** FeatUp; LoftUp.
- **Reason:** The grid is essentially published; re-running it for an ANOVA is incremental packaging.

## C-0028 — In-batch concept co-occurrence, not loss design, creates dense alignment

- **Decision:** KEEP
- **Closest Prior Works:** JEST, "Data curation via joint example selection" (Evans et al., DeepMind 2024) — batch-level joint selection accelerates contrastive learning; hard-negative mining literature for CLIP retrieval (e.g., NegCLIP, Yuksekgonul et al. 2023); SLIP/FILIP-style dense-alignment losses.
- **Existing Work Did:** JEST shows batch composition matters enormously for *learning efficiency and retrieval quality*; dense-alignment papers change the *loss*, not the batch statistics; nobody isolates batch co-occurrence as the causal source of emergent patch-level grounding.
- **Exact Difference:** No controlled pair of runs (random vs noun-overlap-curated batches, identical loss/data/steps) measuring emergent zero-shot *segmentation* while holding retrieval fixed.
- **Remaining Novelty:** A causal mechanism claim about where dense alignment comes from — orthogonal to the loss-design literature, and testable at CLIP-small scale.
- **Novelty Confidence:** Medium-high (search found no direct hit; adjacent-but-distinct JEST is the main risk).
- **Reviewer Attack Papers:** JEST ("batch curation is ours" — rebut: they optimize learnability, never measure dense grounding); FILIP/SLIP ("loss design does create dense alignment" — rebut: that's the comparison arm).
- **Reason:** Precise untested causal mechanism with a clean two-run experiment; survives the harsh test.

## C-0029 — Frozen linear-probe mIoU rank-predicts full fine-tuning outcomes

- **Decision:** KILL
- **Closest Prior Works:** Large-scale probe-vs-finetune correlation study (IJCV 2025, found in search: linear probing predicts fine-tuning transferability across backbones/tasks); transferability-estimation literature (LogME, LEEP).
- **Existing Work Did:** Measured probe→finetune rank correlation at scale, including dense tasks; transferability metrics predict fine-tuning outcomes cheaply.
- **Exact Difference:** Marginal — restricting to mIoU adds nothing conceptual.
- **Remaining Novelty:** None meaningful. Also overlaps Cluster B survivor B-0050 (same probe-predictivity territory) — cross-cluster duplicate.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** LogME (You et al., ICML 2021); LEEP (Nguyen et al., ICML 2020).
- **Reason:** Directly done + internal duplication with B-0050.

## C-0033 — Projector architecture debates reduce to token count

- **Decision:** KILL
- **Closest Prior Works:** MM1 (McKinzie et al., 2024) — connector type is nearly irrelevant; token count and resolution dominate; Cambrian-1 (Tong et al., 2024) — systematic connector ablations.
- **Existing Work Did:** Ran exactly this ablation family at scale and stated the conclusion the idea proposes.
- **Exact Difference:** None of substance.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** MM1; Cambrian-1.
- **Reason:** Literally answered in well-known papers.

## C-0036 — Unfreezing the vision encoder mostly re-fits normalization statistics

- **Decision:** KILL
- **Closest Prior Works:** "Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning" (Zhao et al., 2023) — LN-only tuning recovers most of full tuning; BitFit (Ben Zaken et al., ACL 2022) — bias-only tuning.
- **Existing Work Did:** Showed norm/bias-only tuning captures most fine-tuning benefit in MLLMs — the constructive version of this exact claim.
- **Exact Difference:** The idea's "decomposition" framing (what fraction of full unfreezing is explained by norms) is a re-analysis of a published result.
- **Remaining Novelty:** Negligible.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Zhao et al. 2023; BitFit.
- **Reason:** Existing LN-tuning results already quantify the phenomenon.

## C-0039 — VLMs inherit CLIP's bag-of-words bottleneck through the projector

- **Decision:** KILL
- **Closest Prior Works:** "Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs" (Tong et al., CVPR 2024) — CLIP-blind pairs propagate into MLLM failures; ARO benchmark (Yuksekgonul et al., ICLR 2023) — bag-of-words behavior of CLIP.
- **Existing Work Did:** Established the encoder→VLM failure inheritance pipeline and the bag-of-words diagnosis, including mitigation via mixture-of-encoders.
- **Exact Difference:** Only the specific "through the projector" localization; Eyes Wide Shut already implicates the encoder representation.
- **Remaining Novelty:** Marginal localization detail.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Eyes Wide Shut; ARO.
- **Reason:** Inheritance result is published and highly cited; crowded area.

## C-0047 — Patch serialization order shapes VLM spatial reasoning

- **Decision:** MUTATE
- **Closest Prior Works:** Naseer et al., "Intriguing Properties of Vision Transformers" (NeurIPS 2021) — patch-permutation robustness of ViTs; Kamath et al., "What's 'up' with vision-language models?" (EMNLP 2023) — VLMs fail systematically on spatial relations; positional-encoding ablation literature.
- **Existing Work Did:** Documented VLM spatial-relation failures and ViT order robustness separately; nobody connects serialization order (raster scan) to the *directional structure* of VLM spatial-reasoning errors.
- **Exact Difference:** No published test of whether left/right vs above/below asymmetries in VLM errors track the 1D serialization direction, nor column-major/boustrophedon retraining controls.
- **Remaining Novelty:** The directional-asymmetry prediction is crisp, cheap to test on frozen models (error asymmetry audit) with an optional small retrain.
- **Novelty Confidence:** Medium (search failed to find a direct serialization-direction study; adjacent literature is large).
- **Reviewer Attack Papers:** Kamath et al. 2023 ("spatial failures are known" — rebut: not their dependence on token order); Naseer et al. ("ViTs are order-robust" — rebut: that's classification, not relational reasoning through an LLM).
- **Reason:** MUTATED to the directional-asymmetry version (M3); the generic "order matters" claim would be attacked as known folklore.

## C-0051 — Bigger LLMs can make perception worse

- **Decision:** KILL
- **Closest Prior Works:** MM1 / Cambrian-1 / InternVL scaling ablations — perception benchmarks improve monotonically with LLM scale under matched vision towers; Cluster A survivor A-0200 (same inverse-scaling-for-perception territory).
- **Existing Work Did:** Published scaling curves contradicting the headline direction under standard training; inverse-scaling claims require careful confound control that the idea does not specify.
- **Exact Difference:** The idea adds no mechanism beyond what A-0200 already carries in this pipeline.
- **Remaining Novelty:** None locally — duplicate of a retained A-cluster idea plus evidence against.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** MM1; InternVL scaling reports.
- **Reason:** Internal duplication (A-0200) + contradicting scaling evidence. One pipeline slot for this claim is enough.

## C-0058 — VLM digit errors in OCR are tokenizer artifacts, not perception failures

- **Decision:** KILL
- **Closest Prior Works:** Singh & Strouse, "Tokenization counts: the impact of tokenization on arithmetic in frontier LLMs" (2024); VLM OCR/number-reading failure analyses in document-VQA literature.
- **Existing Work Did:** Established digit-tokenization artifacts in LLM number handling; VLM OCR benchmarks decompose recognition vs reasoning errors.
- **Exact Difference:** The vision-side attribution experiment (same image, digit-grouping-varied prompts) is a small twist.
- **Remaining Novelty:** An afternoon-scale ablation; not a paper spine.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Singh & Strouse 2024.
- **Reason:** Mechanism established in LLM literature; the VLM port is minor.

## C-0060 — Cross-model projector transplants test the universal-geometry claim

- **Decision:** KILL
- **Closest Prior Works:** "The Platonic Representation Hypothesis" (Huh et al., ICML 2024); model stitching (Lenc & Vedaldi, CVPR 2015; Bansal et al., NeurIPS 2021); relative-representation zero-shot stitching (Moschella et al., ICLR 2023).
- **Existing Work Did:** Stitching across independently trained networks is a mature methodology; representation-alignment claims tested extensively, including cross-modal.
- **Exact Difference:** Applying stitching to VLM projectors specifically.
- **Remaining Novelty:** Instantiation-level only.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Bansal et al. 2021; Moschella et al. 2023.
- **Reason:** Direct methodology transplant into a crowded alignment debate.

## C-0064 — Forgetting is embedding drift, not body rewiring

- **Decision:** KILL
- **Closest Prior Works:** Luo et al., "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning" (2023); "LoRA Learns Less and Forgets Less" (Biderman et al., TMLR 2024); mechanistic forgetting decompositions found in search implicating attention layers rather than embeddings.
- **Existing Work Did:** Decomposed where fine-tuning damage lives (layer-wise/module-wise); evidence points away from the embedding-drift-only story.
- **Exact Difference:** The specific "freeze embeddings and forgetting disappears" test is a small delta over module-wise freezing studies that already exist.
- **Remaining Novelty:** Low; the sign of existing evidence is against the hypothesis.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Biderman et al. 2024; module-freezing ablation papers.
- **Reason:** Module-attribution of forgetting is actively studied; the embedding-only claim is likely false and the control is a known technique.

## C-0068 — Fresh optimizer state, not full-rank updates, causes early fine-tuning damage

- **Decision:** MUTATE
- **Closest Prior Works:** Ash & Adams, "On Warm-Starting Neural Network Training" (NeurIPS 2020); Adam-instability analyses (Molybog et al., 2023); LoRA-vs-full-FT forgetting comparisons (Biderman et al., 2024).
- **Existing Work Did:** Warm-starting studied for continued *pre*-training/generalization; Adam second-moment transients implicated in instability; LoRA/full-FT forgetting gap attributed to update rank.
- **Exact Difference:** No published experiment attributes early fine-tuning *forgetting* to fresh optimizer moments vs update rank by warm-starting Adam states at matched schedules — a confound sitting inside the LoRA-forgets-less narrative.
- **Remaining Novelty:** A precise, cheap confound-isolation: fresh-Adam vs transplanted-Adam vs LoRA at matched effective LR; if optimizer transients explain part of the LoRA gap, that revises a widely cited conclusion.
- **Novelty Confidence:** Medium (instructed to be extra harsh on LoRA-forgetting; kept only because this exact control is absent from the papers found).
- **Reviewer Attack Papers:** Biderman et al. 2024 ("rank is the story"); Ash & Adams ("warm-starting is ours" — rebut: different phenomenon and objective).
- **Reason:** MUTATED to the optimizer-transient-vs-rank confound test (M4). As stated originally it reads as a LoRA-forgetting rehash; the mutation names the exact untested control.

## C-0069 — Norm-layer gradients are the spike amplifier

- **Decision:** KILL
- **Closest Prior Works:** Wortsman et al., "Small-scale proxies for large-scale Transformer training instabilities" (ICLR 2024); Molybog et al., "A Theory on Adam Instability in Large-Scale Machine Learning" (2023); qk-layernorm and logit-growth analyses.
- **Existing Work Did:** Localized spike mechanisms (attention-logit growth, Adam epsilon effects, norm-layer interactions) and validated mitigations at proxy scale.
- **Exact Difference:** Attribution specifically to norm-layer gradient amplification is largely contained in the qk-norm/logit-growth findings.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Wortsman et al. 2024.
- **Reason:** Spike-mechanism literature is well-developed and covers the proposed mechanism.

## C-0074 — Instability is noise around a good trajectory: the EMA test

- **Decision:** KILL
- **Closest Prior Works:** Busbridge et al., "How to Scale Your EMA" (NeurIPS 2023); EMA-as-stabilizer results throughout SSL and diffusion training; Wortsman et al. 2024 instability toolkit.
- **Existing Work Did:** EMA's smoothing of unstable trajectories is established practice with quantitative studies.
- **Exact Difference:** Using EMA as a *diagnostic* (does the EMA iterate sail through spikes?) rather than a fix — a framing twist.
- **Remaining Novelty:** Framing only.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Busbridge et al. 2023.
- **Reason:** Anyone training large models already knows/uses this; no publishable surprise.

## C-0076 — A critical window governs when vision encoders can be safely unfrozen

- **Decision:** KILL
- **Closest Prior Works:** VILA (Lin et al., CVPR 2024) — unfreezing-schedule ablations; Prismatic VLMs (Karamcheti et al., ICML 2024) — systematic freeze/unfreeze design-space study.
- **Existing Work Did:** Published the freeze/unfreeze timing ablations across VLM training stages.
- **Exact Difference:** "Critical window" narrative over the same axis.
- **Remaining Novelty:** None beyond terminology.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Prismatic VLMs; VILA.
- **Reason:** Design-space papers already swept this.

## C-0077 — Cleaner pretraining data makes models harder to fine-tune

- **Decision:** KILL
- **Closest Prior Works:** DataComp (Gadre et al., NeurIPS 2023) — curation improves downstream including fine-tuned transfer; data-filtering scaling studies.
- **Existing Work Did:** Extensive filtered-vs-raw pretraining comparisons; fine-tuning results do not support "cleaner is worse."
- **Exact Difference:** The idea predicts the opposite sign of what large public benchmarks show.
- **Remaining Novelty:** Would need a narrow regime where it holds; none identified.
- **Novelty Confidence:** High (against).
- **Reviewer Attack Papers:** DataComp.
- **Reason:** Contradicted by scale evidence; speculative contrarianism without a mechanism.

## C-0090 — Text-batch rehearsal works by gradient rebalancing, not by content

- **Decision:** KEEP
- **Closest Prior Works:** VLM training recipes mixing text-only data to preserve LLM ability (LLaVA-1.5/VILA-style data mixes; text-rehearsal notes in MLLM papers); modality-gradient-conflict analyses in multimodal training.
- **Existing Work Did:** Established *that* text-only rehearsal reduces LLM-skill forgetting in VLM training; treated the mechanism as content replay.
- **Exact Difference:** No published control replacing rehearsal text with content-free/shuffled/random-token batches at matched gradient scale to separate "content replay" from "gradient rebalancing."
- **Remaining Novelty:** A single decisive control experiment with a mechanism payoff (if random-token batches work, rehearsal-data curation is wasted effort).
- **Novelty Confidence:** Medium-high (search found no such control).
- **Reviewer Attack Papers:** VILA ("we ablated data mixes" — rebut: mixes vary content, never content-free gradient-matched controls); continual-learning rehearsal literature ("replay is understood" — rebut: not in the multimodal gradient-interference regime).
- **Reason:** Cheap, decisive, mechanism-revealing; survives harsh review because the control genuinely is absent.

## C-0091 — Linear probes measure separability, not usability

- **Decision:** KILL
- **Closest Prior Works:** Probe-vs-finetune correlation study (IJCV 2025, found in search); "What Do Self-Supervised ViTs Learn?" (Park et al., ICLR 2023) probing analyses; transferability-estimation literature.
- **Existing Work Did:** Quantified where probe rankings do and don't predict downstream usability.
- **Exact Difference:** Rhetorical framing only.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** IJCV 2025 study; LogME.
- **Reason:** Same territory as C-0029; both die to the same literature.

## C-0093 — Dimensional collapse doesn't hurt transfer

- **Decision:** KEEP
- **Closest Prior Works:** Jing et al., "Understanding Dimensional Collapse in Contrastive Self-supervised Learning" (ICLR 2022); RankMe (Garrido et al., ICML 2023) — effective-rank correlates with downstream performance; whitening/decorrelation SSL methods (VICReg, W-MSE).
- **Existing Work Did:** Established the collapse phenomenon and *correlational* rank-performance links; methods papers add anti-collapse terms and report gains.
- **Exact Difference:** No *interventional* study that artificially induces controlled dimensional collapse (fixed projection to k dims during training) and measures transfer — the causal arrow (collapse → worse transfer) is assumed, not tested.
- **Remaining Novelty:** Controlled causal test of a load-bearing assumption behind a family of SSL regularizers; a null result would be a genuine correction.
- **Novelty Confidence:** Medium-high (RankMe is correlational; search found no interventional collapse study).
- **Reviewer Attack Papers:** RankMe ("rank predicts performance" — rebut: prediction ≠ causation); Jing et al. ("collapse is bad" — rebut: shown by construction in toy settings, not by intervention at scale).
- **Reason:** Assumption-audit with clean intervention; passes the harsh bar.

## C-0095 — Pretraining pooling choice silently shapes patch-token quality

- **Decision:** KILL
- **Closest Prior Works:** Beyer et al., "Better plain ViT baselines for ImageNet-1k" (2022) — GAP vs CLS; Darcet et al., "Vision Transformers Need Registers" (ICLR 2024) — token-role artifacts shaped by training; pooling ablations in CLIP variants (e.g., attentional pooling in SigLIP/CoCa lineage).
- **Existing Work Did:** Compared pooling choices and documented their effect on token statistics and dense quality.
- **Exact Difference:** A dedicated patch-token-quality-vs-pooling study is mostly assembled across existing ablations.
- **Remaining Novelty:** Consolidation value only. Also brushes the crowded "registers" territory flagged for extra harshness.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Darcet et al. 2024; Beyer et al. 2022.
- **Reason:** Crowded register/pooling space; no precise untested remainder.

## C-0096 — MIM features hide their value from linear probes in high frequencies

- **Decision:** KILL
- **Closest Prior Works:** Park et al., "What Do Self-Supervised Vision Transformers Learn?" (ICLR 2023) — CL vs MIM spectral/behavioral differences and probe-vs-finetune gaps.
- **Existing Work Did:** Provided exactly the frequency-based explanation for why MIM underperforms on linear probes but wins after fine-tuning.
- **Exact Difference:** None substantive.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Park et al. 2023.
- **Reason:** Direct prior hit.

## C-0099 — Whitening erases most claimed differences between SSL methods

- **Decision:** MUTATE
- **Closest Prior Works:** W-MSE (Ermolov et al., ICML 2021); Garrido et al., "On the duality between contrastive and non-contrastive self-supervised learning" (ICLR 2023) — method families closer than advertised; standardized SSL benchmarks (solo-learn) showing small gaps under matched recipes.
- **Existing Work Did:** Showed contrastive/non-contrastive duality theoretically and small empirical gaps under matched training; whitening used as a *method component*, not as a post-hoc equalizer.
- **Exact Difference:** No study applies post-hoc feature whitening across N published SSL checkpoints and measures how much of the reported inter-method spread survives — attributing claimed differences to second-moment bookkeeping.
- **Remaining Novelty:** Cheap (frozen checkpoints + one linear-algebra step), quantifies how much of the SSL leaderboard is covariance conditioning; harsh instruction on SSL confounds acknowledged — this is a *confound-measuring* proposal, not another method.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Garrido et al. 2023 ("families are equivalent anyway"); solo-learn benchmark ("matched recipes already shrink gaps").
- **Reason:** MUTATED to the post-hoc whitening audit at matched evaluation budget (M5); crisper and cheaper than the original framing.

## C-0103 — Supervised pretraining matches SSL at equal data scale

- **Decision:** KILL
- **Closest Prior Works:** Goldblum et al., "Battle of the Backbones" (NeurIPS 2023) — large controlled backbone comparison including supervised vs SSL; explicitly flagged as a crowded scale-confound area in task instructions.
- **Existing Work Did:** Ran the broad controlled comparison; supervised backbones remain competitive.
- **Exact Difference:** Equal-data-scale insistence is a re-run with one more control.
- **Remaining Novelty:** Incremental control on a heavily studied comparison.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Battle of the Backbones.
- **Reason:** Instructed harsh zone (SSL-vs-supervised confounds); no precise untested remainder.

## C-0109 — Frozen features know tail classes that probes can't see

- **Decision:** KILL
- **Closest Prior Works:** Kang et al., "Decoupling Representation and Classifier for Long-Tailed Recognition" (ICLR 2020) — representations are fine, classifiers are the long-tail bottleneck; classifier-retraining (cRT/LWS) results.
- **Existing Work Did:** Demonstrated precisely that frozen features contain tail knowledge that standard classifier training fails to expose.
- **Exact Difference:** kNN-vs-probe gap as tail detector is a minor variation.
- **Remaining Novelty:** None meaningful.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Kang et al. 2020.
- **Reason:** Canonical prior work says exactly this.

## C-0113 — Trained heads barely beat random projections on good backbones

- **Decision:** KILL
- **Closest Prior Works:** Hoffer et al., "Fix your classifier" (ICLR 2018); random-feature/reservoir literature; frozen-random-head results in SSL evaluation protocols.
- **Existing Work Did:** Established fixed/random final layers lose little on strong features.
- **Exact Difference:** Applying to modern foundation backbones.
- **Remaining Novelty:** Instantiation only.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Hoffer et al. 2018.
- **Reason:** Known result; foundation-model rerun is not a contribution.

## C-0118 — Keep the projector for fine-grained transfer

- **Decision:** KILL
- **Closest Prior Works:** Bordes et al., "Guillotine Regularization: Why removing layers is needed to improve generalization in self-supervised learning" (TMLR 2023) — systematic study of which head/projector layers to keep per downstream task.
- **Existing Work Did:** Directly studied projector-keeping vs cutting across transfer conditions, including when keeping projector layers helps.
- **Exact Difference:** Fine-grained-transfer emphasis is a subset of their analysis.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Bordes et al. 2023.
- **Reason:** Direct prior hit.

## C-0123 — The honest generative-vs-discriminative pretraining comparison for dense tasks

- **Decision:** KILL
- **Closest Prior Works:** A 2026 controlled generative-vs-discriminative pretraining comparison found in search (arXiv 2608.13183); Brempong et al., "Denoising Pretraining for Semantic Segmentation" (CVPRW 2022); diffusion-features-for-segmentation lineage (e.g., DDPM-Seg, Baranchuk et al. 2022).
- **Existing Work Did:** Ran compute/data-matched generative-vs-discriminative comparisons on dense tasks; diffusion-feature papers benchmark against discriminative backbones.
- **Exact Difference:** Little remains once the 2026 controlled study is on the table.
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** Medium-high (recent hit found in search; older lineage independently corroborates crowdedness).
- **Reviewer Attack Papers:** arXiv 2608.13183; Baranchuk et al. 2022.
- **Reason:** The "honest comparison" has now been run.

## C-0125 — Denoising destroys evidence that recognition models secretly use

- **Decision:** KILL
- **Closest Prior Works:** Diamond et al., "Dirty Pixels: Towards End-to-End Image Processing and Perception" (SIGGRAPH 2021); Liu et al., "When Image Denoising Meets High-Level Vision Tasks" (IJCAI 2018).
- **Existing Work Did:** Showed denoising optimized for humans hurts downstream recognition and that joint optimization recovers it — the same evidence-destruction thesis.
- **Exact Difference:** Modern-backbone rerun.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Dirty Pixels.
- **Reason:** Thesis published twice over.

## C-0126 — Diffusion data augmentation works by rebalancing, not by new information

- **Decision:** KILL
- **Closest Prior Works:** Azizi et al., "Synthetic Data from Diffusion Models Improves ImageNet Classification" (2023); Fill-Up / long-tail diffusion-augmentation papers (2023–24) that compare against reweighting/resampling baselines; "Scaling Laws of Synthetic Images" (Fan et al., 2024).
- **Existing Work Did:** Long-tail diffusion-augmentation papers already include rebalancing baselines and claim gains beyond them; synthetic-data scaling studies quantify information content limits.
- **Exact Difference:** The idea's null hypothesis is the baseline row of existing tables.
- **Remaining Novelty:** Only if existing baselines were systematically mis-tuned — no evidence gathered for that.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Fill-Up-style long-tail papers; Azizi et al.
- **Reason:** The controlled comparison exists in multiple papers' baseline rows.

## C-0128 — Generative editing enables causal measurement of context reliance in segmentation

- **Decision:** KEEP
- **Closest Prior Works:** Choi et al., "Exploiting Hierarchical Context on a Large Database of Object Categories" / object-out-of-context lineage; cut-paste context studies (e.g., Rosenfeld et al., "The Elephant in the Room," 2018); counterfactual diffusion-editing evaluations for classifiers (2023–24).
- **Existing Work Did:** Demonstrated context reliance qualitatively (elephant-in-the-room) and via unrealistic cut-paste; counterfactual editing evals exist for classification.
- **Exact Difference:** No published *quantitative per-class context-reliance score* for segmentation built from photorealistic inversion-based counterfactual edits, and no test linking that score to distribution-shift robustness.
- **Remaining Novelty:** Turns an anecdote into a measurable, model-comparable quantity with a robustness-prediction payoff.
- **Novelty Confidence:** Medium-high (search found classification-side counterfactual evals but not the dense, score-producing version).
- **Reviewer Attack Papers:** Rosenfeld et al. 2018 ("context reliance is known" — rebut: known ≠ measured per-class with realistic edits); diffusion-editing eval papers ("we did counterfactual evals" — rebut: classification, not dense, no robustness linkage).
- **Reason:** Precise measurement gap with a causal tool that now exists; survives harsh review.

## C-0129 — The leakage laws of attention-supervised synthetic masks

- **Decision:** KILL
- **Closest Prior Works:** DiffuMask (Wu et al., ICCV 2023); Dataset Diffusion (Nguyen et al., NeurIPS 2023); MaskFactory (2024).
- **Existing Work Did:** Built and analyzed attention-derived synthetic masks, including quality/noise characterization and downstream training laws.
- **Exact Difference:** "Leakage law" formalization over an actively mined vein.
- **Remaining Novelty:** Marginal formalization.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** DiffuMask; Dataset Diffusion.
- **Reason:** Fast-moving applied area; law-fitting over existing pipelines is incremental.

## C-0145 — "SR helps small-object detection" is resolution mismatch in disguise

- **Decision:** KILL
- **Closest Prior Works:** Haris et al., "Task-Driven Super Resolution: Object Detection in Low-Resolution Images" (2018/2021); small-object-detection SR surveys with input-resolution-controlled comparisons.
- **Existing Work Did:** Studied SR-for-detection with resolution controls; the mismatch explanation is discussed in the task-driven SR literature.
- **Exact Difference:** A sharper audit framing, no new mechanism.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Haris et al.
- **Reason:** Debunk target insufficiently alive; controls exist in prior work.

## C-0148 — A mode-coverage statistic predicts when synthetic data helps

- **Decision:** KILL
- **Closest Prior Works:** Kynkäänniemi et al., "Improved Precision and Recall Metric for Assessing Generative Models" (NeurIPS 2019); "Scaling Laws of Synthetic Images for Model Training" (Fan et al., 2024); density/coverage metrics (Naeem et al., ICML 2020).
- **Existing Work Did:** Built coverage/diversity metrics for generators and connected synthetic-data utility to distributional properties and scale.
- **Exact Difference:** Regressing downstream gain on coverage is a natural next step someone in that literature has likely run in ablations; no clean remainder identified.
- **Remaining Novelty:** Low-medium; predictive-statistic packaging.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Naeem et al. 2020; Fan et al. 2024.
- **Reason:** Metric-exists + scaling-study-exists squeeze the gap to a regression exercise.

## C-0154 — Ground truth becomes a function of the annotating model's prompt

- **Decision:** KILL
- **Closest Prior Works:** Sclar et al., "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" (ICLR 2024); LLM-annotator reliability studies (2023–25) documenting prompt-dependent label distributions; Cluster B survivor B-0269 (same territory, already retained there).
- **Existing Work Did:** Established strong prompt sensitivity of LLM outputs including annotation settings.
- **Exact Difference:** Downstream-benchmark-drift framing; largely covered by B-0269 in this pipeline.
- **Remaining Novelty:** None locally (duplicate).
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Sclar et al. 2024.
- **Reason:** Cross-cluster duplicate + established sensitivity literature.

## C-0157 — Rationales don't make labels better — they make errors findable

- **Decision:** KILL
- **Closest Prior Works:** Zaidan & Eisner, "Modeling Annotators: annotator rationales" lineage (EMNLP 2008); modern LLM-annotation studies evaluating rationale effects on label quality and verification efficiency (2023–25 search hits).
- **Existing Work Did:** Studied rationales for annotation quality and for auditing/verification workflows.
- **Exact Difference:** The specific quality-vs-findability dissociation is a re-framing of measured effects in existing rationale-annotation studies.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Rationale-annotation literature.
- **Reason:** Verification-value of rationales is documented; the dissociation framing alone won't carry a paper.

## C-0158 — Uncertainty sampling poisons active learning when the LLM is the annotator

- **Decision:** MUTATE
- **Closest Prior Works:** FreeAL (Xiao et al., EMNLP 2023) — human-free active learning with LLM annotators; active learning with noisy oracles (classic and 2023–24 revivals); "difficulty correlation" observations in LLM-annotation papers.
- **Existing Work Did:** Combined AL with LLM annotation and studied noisy-oracle AL generically; noted LLM labels are worse on hard items.
- **Exact Difference:** No work isolates the *correlated-noise mechanism*: uncertainty sampling selects exactly the items where the LLM annotator's error rate spikes, making the acquisition function anti-correlated with label quality — with a decorrelation fix.
- **Remaining Novelty:** Mechanism + fix (acquisition functions penalized by predicted annotator error), testable on standard AL benchmarks with LLM labels.
- **Novelty Confidence:** Medium (search found adjacent observations, not the mechanism study).
- **Reviewer Attack Papers:** FreeAL ("AL+LLM is ours" — rebut: they don't analyze acquisition/noise correlation); noisy-oracle AL ("known setting" — rebut: assumes noise independent of acquisition).
- **Reason:** MUTATED to the correlated-noise mechanism + decorrelated acquisition (M6); the headline claim alone is too close to noisy-oracle AL.

## C-0159 — Noisy-label theory fails on LLM-generated labels

- **Decision:** KILL
- **Closest Prior Works:** NoiseBench (Rücker et al., 2024) — real (incl. LLM) noise breaks noise-robust methods benchmarked on synthetic noise; iterative-refinement calibration on LLM-generated noisy labels (2025 search hit).
- **Existing Work Did:** Demonstrated exactly that class-conditional noise assumptions fail on LLM-generated labels and that standard noisy-label methods degrade.
- **Exact Difference:** None substantive.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** NoiseBench.
- **Reason:** Direct prior hit.

## C-0170 — Self-generated benchmarks are systematically too easy

- **Decision:** KILL
- **Closest Prior Works:** "What Has Been Lost with Synthetic Evaluation?" (2025 search hit) — synthetic benchmarks are easier/less discriminative; Panickssery et al., "LLM Evaluators Recognize and Favor Their Own Generations" (NeurIPS 2024).
- **Existing Work Did:** Measured difficulty/validity loss in LLM-generated evaluation sets and self-preference effects.
- **Exact Difference:** Marginal.
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** The 2025 synthetic-evaluation study.
- **Reason:** The audit exists.

## C-0179 — Benchmarks annotated by generation N favor generation N+1 of the same family

- **Decision:** KILL
- **Closest Prior Works:** "Preference Leakage: A Contamination Problem in LLM-as-a-Judge" (2025); Panickssery et al. 2024 (self-recognition/self-preference).
- **Existing Work Did:** Established family-favoring contamination in LLM-judged/annotated evaluation, including cross-generation effects.
- **Exact Difference:** Generation-N→N+1 wording.
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Preference Leakage.
- **Reason:** Contamination direction already published.

## C-0188 — Deployed segmenters change answers with batch composition

- **Decision:** KILL
- **Closest Prior Works:** Nado et al., "Evaluating Prediction-Time Batch Normalization for Robustness under Covariate Shift" (2020); test-time-adaptation transduction critiques (realistic TTA evaluation papers, 2023); batch-dependence of BN-based models is textbook.
- **Existing Work Did:** Documented and exploited prediction-time batch-statistic dependence extensively.
- **Exact Difference:** Framing as a deployment/consistency audit.
- **Remaining Novelty:** Low; modern segmenters increasingly use GN/LN, shrinking the phenomenon.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Nado et al. 2020.
- **Reason:** Known mechanism, shrinking relevance.

## C-0190 — The model zoo is converging on identical errors

- **Decision:** KILL
- **Closest Prior Works:** "Great Models Think Alike and this Undermines AI Oversight" (Goel et al., 2025) — model-similarity/error-correlation rising with capability; "Correlated Errors in Large Language Models" (2025 search hit); error-consistency literature (Geirhos et al., 2020).
- **Existing Work Did:** Measured cross-model error correlation and its growth, including oversight implications.
- **Exact Difference:** Vision-model-zoo instantiation; Geirhos et al. already did error consistency for vision.
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Goel et al. 2025; Geirhos et al. 2020.
- **Reason:** Both LLM and vision versions exist.

## C-0193 — Easy pixels resolve early: prediction depth for dense tasks

- **Decision:** KILL
- **Closest Prior Works:** Liu et al., "Anytime Dense Prediction with Confidence Adaptivity" (ICLR 2022); multi-exit semantic segmentation architectures; prediction-depth (Baldock et al., NeurIPS 2021) for classification.
- **Existing Work Did:** Built early-exit dense predictors exploiting exactly the easy-pixels-resolve-early structure; prediction-depth formalized for classification.
- **Exact Difference:** Porting the prediction-depth *metric* to dense tasks where the phenomenon is already engineering practice.
- **Remaining Novelty:** Metric port only.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Anytime Dense Prediction.
- **Reason:** Phenomenon already productized in the literature.

## C-0200 — Some random initializations are just better — everywhere

- **Decision:** KILL
- **Closest Prior Works:** Dodge et al., "Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping" (2020); Picard, "torch.manual_seed(3407) is all you need" (2021) — seed-quality distributions; lottery-tickets lineage for init quality.
- **Existing Work Did:** Measured seed-quality variance and cross-task consistency of good seeds/inits.
- **Exact Difference:** "Everywhere" universality claim; prior evidence is mixed and the experiment is a seed sweep.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Dodge et al. 2020.
- **Reason:** Seed-quality studies exist; universality version is compute-heavy with weak payoff.

## C-0204 — Loss spikes that help: post-spike generalization improvements

- **Decision:** KILL
- **Closest Prior Works:** Edge-of-stability literature (Cohen et al., ICLR 2021) — instability intertwined with progress; search hits on instability-induced flatness bias and "can stability be detrimental" analyses (2023–24).
- **Existing Work Did:** Connected instability episodes to curvature reduction and sometimes-better minima — the beneficial-spike story.
- **Exact Difference:** Spike-level event-study framing.
- **Remaining Novelty:** Low-medium; mechanism already argued in EoS lineage.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Cohen et al. 2021 lineage.
- **Reason:** EoS literature owns this mechanism.

## C-0207 — Positional embeddings store photographer bias

- **Decision:** KILL
- **Closest Prior Works:** Position-bias analyses for ViTs found in search (position-SHAP-style attribution; CVPR-era "position bias in vision transformer classifiers" work); center-bias/photographer-bias dataset studies (e.g., dataset-bias classics, Torralba & Efros 2011).
- **Existing Work Did:** Attributed prediction variance to positional embeddings and documented spatial priors learned from photographer-biased data.
- **Exact Difference:** Consolidating both into one causal story; components published separately.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** Medium (exact strongest-prior identification uncertain; both halves independently confirmed in search).
- **Reviewer Attack Papers:** ViT position-bias papers; Torralba & Efros 2011.
- **Reason:** Both ingredients exist; the join is an ablation.

## C-0210 — Batch size is an ID/OOD trade-off dial at fixed validation loss

- **Decision:** KILL
- **Closest Prior Works:** Keskar et al., "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima" (ICLR 2017); Smith et al., "Don't Decay the Learning Rate, Increase the Batch Size" (ICLR 2018); flat-minima→OOD-robustness studies (e.g., SAM-robustness analyses).
- **Existing Work Did:** Mapped batch-size→sharpness→generalization; sharpness→OOD links studied.
- **Exact Difference:** Fixing validation loss while varying batch size is a control refinement on a decade-old axis.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Keskar et al.; SAM lineage.
- **Reason:** Mature axis; refinement won't survive review.

## C-0214 — ImageNet-21k pretraining gains come from images, not from extra classes

- **Decision:** KILL
- **Closest Prior Works:** Ridnik et al., "ImageNet-21K Pretraining for the Masses" (NeurIPS 2021 D&B); label-granularity transfer studies found in search (granularity manipulations with images held fixed, reporting label structure *does* matter).
- **Existing Work Did:** Ran image-count vs label-set manipulations; evidence indicates label granularity contributes beyond image count — against the idea's null.
- **Exact Difference:** Idea's proposed control largely executed with the opposite conclusion.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Granularity studies; Ridnik et al.
- **Reason:** Experiment run; sign unfavorable.

## C-0219 — Zero-shot beats few-shot more often than the field admits

- **Decision:** KILL
- **Closest Prior Works:** CLIP (Radford et al., 2021) — zero-shot beats few-shot linear probes up to ~16 shots (in-paper figure); ELEVATER benchmark (Li et al., NeurIPS 2022) — systematic zero/few-shot comparisons.
- **Existing Work Did:** Documented the zero>few-shot crossover publicly and benchmarked it broadly.
- **Exact Difference:** "The field admits" framing; the data is in famous figures.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** CLIP paper Figure; ELEVATER.
- **Reason:** In the most-cited figure of the area.

## C-0229 — Multi-task pretraining's benefit is the data, not the tasks

- **Decision:** KEEP
- **Closest Prior Works:** Multi-task vision pretraining systems (Uni-Perceiver, Florence, 4M, Painter/SegGPT lineage); multi-task-learning theory on task interference/transfer (e.g., Standley et al., ICML 2020, "Which Tasks Should Be Learned Together"); data-scaling studies.
- **Existing Work Did:** Built multi-task pretrainers and compared task combinations; compared against single-task baselines — but almost always confounding task diversity with *image-set* diversity.
- **Exact Difference:** No published pooled-image control: same union of images, one task vs many tasks, at matched compute — isolating "task supervision diversity" from "data diversity."
- **Remaining Novelty:** A missing control under a major training paradigm; either outcome is informative (tasks matter vs data pooling suffices).
- **Novelty Confidence:** Medium-high (search found no pooled-image-controlled comparison at pretraining scale).
- **Reviewer Attack Papers:** Standley et al. ("task-relationship studies exist" — rebut: fixed data per task, not pooled-image control); 4M ("we ablate modalities" — rebut: not the data-vs-task decomposition).
- **Reason:** Genuine missing control, feasible at small scale; keeps.

## C-0240 — The "frozen backbone preserves robustness" doctrine mismeasures robustness

- **Decision:** KILL
- **Closest Prior Works:** Kumar et al., "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution" (LP-FT, ICLR 2022); Lee et al., "Surgical Fine-Tuning Improves Adaptation to Distribution Shifts" (ICLR 2023); WiSE-FT (Wortsman et al., 2022).
- **Existing Work Did:** Mapped exactly when freezing helps/hurts OOD, with mechanism (feature distortion) and fixes (interpolation, surgical tuning).
- **Exact Difference:** "Mismeasurement" re-framing over a mapped condition space.
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** LP-FT; WiSE-FT.
- **Reason:** Condition-dependence thoroughly published.

## C-0247 — MAE pretraining on small domain datasets is worthless

- **Decision:** KILL
- **Closest Prior Works:** Medical-imaging MAE studies (2022–24) showing in-domain masked pretraining on modest datasets *helps* (e.g., MAE for CXR/CT reports found in search); small-data SSL benchmarks.
- **Existing Work Did:** Ran in-domain MAE on small/medium domain corpora with positive results, contradicting the headline.
- **Exact Difference:** The idea predicts a null that existing domain studies already falsify in several domains.
- **Remaining Novelty:** Possibly domain-size thresholds — but that's a scaling appendix, not a paper.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Medical MAE studies.
- **Reason:** Contradicted; harsh default applies.

## C-0248 — Ensemble robustness doesn't survive distillation

- **Decision:** KILL
- **Closest Prior Works:** Tran et al., "Hydra: Preserving Ensemble Diversity in Model Distillation" (2020); Malinin et al., "Ensemble Distribution Distillation" (ICLR 2020); Nam et al., "Diversity Matters When Learning From Ensembles" (NeurIPS 2021).
- **Existing Work Did:** Identified exactly what is lost distilling ensembles (diversity/epistemic uncertainty/robustness) and proposed remedies.
- **Exact Difference:** Robustness-specific accounting is embedded in this literature.
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Ensemble Distribution Distillation; Hydra.
- **Reason:** A whole subliterature answers this.

## C-0251 — More than two views adds nothing to contrastive learning

- **Decision:** KILL
- **Closest Prior Works:** Shidani et al., "Poly-View Contrastive Learning" (ICLR 2024) — multi-view objectives, finds more views change efficiency/quality trade-offs; SwAV multi-crop (Caron et al., 2020) — extra views demonstrably help.
- **Existing Work Did:** Ran the many-views experiments; results contradict "adds nothing."
- **Exact Difference:** None that survives multi-crop's decade of deployment.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Poly-View Contrastive Learning; SwAV.
- **Reason:** Directly contradicted.

## C-0262 — Mixup's calibration benefit doesn't survive temperature scaling

- **Decision:** KILL
- **Closest Prior Works:** Wang et al., "On the Pitfall of Mixup for Uncertainty Calibration" (CVPR 2023); Zhang et al., "When and How Mixup Improves Calibration" (ICML 2022).
- **Existing Work Did:** Analyzed mixup-calibration interactions in detail, including post-hoc recalibration comparisons.
- **Exact Difference:** The temperature-scaling-matched comparison is inside these papers' scope.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Both above.
- **Reason:** Direct prior hits.

## C-0265 — Chain-of-thought does not improve VLM perception

- **Decision:** KILL
- **Closest Prior Works:** Sprague et al., "To CoT or not to CoT?" (2024) — CoT helps math/symbolic, not most other tasks; 2025–26 VLM-reasoning studies found in search showing CoT fails to improve (or hurts) perception-heavy benchmarks.
- **Existing Work Did:** Meta-analyzed CoT benefits by task type; VLM-specific null/negative results published in the flagged crowded zone.
- **Exact Difference:** None sufficient — instructed extra-harsh zone (CoT for vision).
- **Remaining Novelty:** None sufficient.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Sprague et al. 2024; VLM CoT-perception studies.
- **Reason:** Crowded, actively published null; harsh kill.

## C-0270 — Confidence thresholding of pseudo-labels is no better than random keeping

- **Decision:** KILL
- **Closest Prior Works:** FlexMatch (Zhang et al., NeurIPS 2021) / FreeMatch (2023) — thresholding analyzed and improved; "rethinking confidence thresholds in pseudo-labeling" analyses found in search (2023–25).
- **Existing Work Did:** Dissected threshold behavior extensively; random-keeping baselines appear in ablations; thresholding demonstrably beats random in standard regimes.
- **Exact Difference:** The idea's null contradicts widely replicated ablations.
- **Remaining Novelty:** None.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** FlexMatch; FreeMatch.
- **Reason:** Contradicted by a mature literature.

## C-0274 — Exact-name matching punishes correct open-vocabulary predictions

- **Decision:** KILL
- **Closest Prior Works:** TPAMI 2025 open-vocabulary segmentation evaluation critique found in search (semantic-similarity-aware metrics replacing exact matching); soft-matching evaluation proposals in OV-detection.
- **Existing Work Did:** Diagnosed exact-match penalties and proposed similarity-aware metrics.
- **Exact Difference:** None sufficient.
- **Remaining Novelty:** None.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** The TPAMI 2025 metric critique.
- **Reason:** Fix already proposed in a journal venue.

## C-0276 — The many ADE20Ks: split drift breaks cross-paper comparability (absorbs C-0279)

- **Decision:** KEEP
- **Closest Prior Works:** Reproducibility critiques in detection/segmentation (e.g., protocol-sensitivity notes in mmsegmentation/detectron model zoos); "papers with different val protocols" complaints in benchmark retrospectives; no dedicated audit found — SEARCH FOUND NO DIRECT PRIOR.
- **Existing Work Did:** Anecdotal/issue-tracker documentation of framework and split drift; no fixed-checkpoint cross-framework quantification.
- **Exact Difference:** No published study runs *identical checkpoints* through N frameworks/protocol variants (splits, resizing, TTA, class mappings) and quantifies the mIoU spread against typical claimed SOTA deltas.
- **Remaining Novelty:** A quantified comparability budget for the field's most-used dense benchmarks; C-0279's inference-protocol decomposition folded in as one axis of the audit.
- **Novelty Confidence:** Medium (absence-of-prior is the finding; low-risk to execute, high citation utility).
- **Reviewer Attack Papers:** Model-zoo documentation ("known informally" — rebut: informal ≠ quantified with checkpoints held fixed).
- **Reason:** Clean measurement gap, cheap, decision-relevant for every segmentation paper; keeps with C-0279 merged.

## C-0279 — How much of SOTA is inference protocol?

- **Decision:** KILL (folded into C-0276)
- **Closest Prior Works:** TTA/multi-scale ablations inside segmentation papers; the C-0276 audit space.
- **Existing Work Did:** Individual papers ablate their own protocol knobs.
- **Exact Difference:** As a standalone it duplicates C-0276's protocol axis.
- **Remaining Novelty:** Lives on inside C-0276.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Any segmentation paper's TTA table.
- **Reason:** Merged, not independently kept.

## C-0285 — "Zero-shot" cross-dataset evaluation hides target tuning

- **Decision:** KILL
- **Closest Prior Works:** Musgrave et al., "Unsupervised Domain Adaptation: A Reality Check" (2021); UDA model-selection critiques (target-label leakage in checkpoint selection); benchmark-hygiene retrospectives.
- **Existing Work Did:** Exposed target-tuning leakage in adjacent transfer settings with the same audit logic.
- **Exact Difference:** OV/"zero-shot" instantiation of an executed critique pattern.
- **Remaining Novelty:** Low-medium.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Musgrave et al.
- **Reason:** Audit template exists; port is incremental.

## C-0293 — Rare-class sample sizes make many mIoU gains statistically void

- **Decision:** KILL
- **Closest Prior Works:** "Confidence Intervals Uncovered" (MICCAI 2024) — CI retrofitting shows many claimed gains insignificant; segmentation-metric statistical-power analyses; Cluster B survivor B-0274 and Cluster A survivor A-0152 (same significance-audit territory).
- **Existing Work Did:** Retrofitted uncertainty onto published segmentation results; demonstrated widespread non-significance.
- **Exact Difference:** Rare-class emphasis is a subsection of that program; duplicated inside this pipeline by A/B keeps.
- **Remaining Novelty:** None locally.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Confidence Intervals Uncovered.
- **Reason:** Done in medical imaging + internal duplication.

## C-0300 — The field's false-discovery rate is measurable

- **Decision:** KILL
- **Closest Prior Works:** Raff, "A Step Toward Quantifying Independently Reproducible Machine Learning Research" (NeurIPS 2019); reproducibility-challenge reports; replication meta-studies.
- **Existing Work Did:** Quantified reproduction rates over hundreds of papers — the FDR estimate in practice.
- **Exact Difference:** Statistical re-labeling of an executed program.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Raff 2019.
- **Reason:** Program exists with data.

## C-0302 — Last-layer group-robustness fixes fail on spatially entangled bias

- **Decision:** KEEP
- **Closest Prior Works:** Kirichenko et al., "Last Layer Re-Training is Sufficient for Robustness to Spurious Correlations" (DFR, ICLR 2023); group-robustness methods (GroupDRO, JTT) — all classification; spurious-correlation segmentation studies are sparse.
- **Existing Work Did:** Established last-layer sufficiency for *classification* group robustness on benchmark spurious correlations.
- **Exact Difference:** No test of DFR-style fixes on *dense prediction* where bias is spatially entangled with the target (e.g., class-context co-location), and last-layer surgery cannot re-route spatial features.
- **Remaining Novelty:** A predicted failure mode of a celebrated simple fix, in a setting (segmentation) where the fix's assumption (feature sufficiency) plausibly breaks; constructive follow-up (which layer suffices for dense robustness).
- **Novelty Confidence:** Medium-high (search found no dense-prediction DFR evaluation).
- **Reviewer Attack Papers:** DFR ("sufficiency shown" — rebut: classification only); GroupDRO lineage ("methods exist" — rebut: not the last-layer-sufficiency question for dense tasks).
- **Reason:** Precise, falsifiable gap off a high-profile result; keeps.

## C-0310 — The camera ISP is a bigger domain axis than the weather

- **Decision:** KEEP
- **Closest Prior Works:** Buckler et al., "Reconfiguring the Imaging Pipeline for Computer Vision" (ICCV 2017); raw-vs-processed robustness studies; sensor/ISP domain-shift observations in autonomous-driving datasets; weather-robustness benchmarks (ACDC, ImageNet-C weather subsets).
- **Existing Work Did:** Showed ISP stages affect vision accuracy/energy (Buckler) and that sensor differences shift domains; weather axes benchmarked exhaustively — but no head-to-head magnitude comparison.
- **Exact Difference:** No controlled ISP-parameter grid (demosaic/denoise/tone-map/sharpen sweeps on RAW) benchmarked against weather-shift magnitude on the same scenes and models.
- **Remaining Novelty:** Quantified ranking of a hidden, controllable domain axis vs the field's favorite visible one; directly actionable (ISP randomization as augmentation).
- **Novelty Confidence:** Medium-high (search found components, not the comparison).
- **Reviewer Attack Papers:** Buckler et al. ("ISP effects known" — rebut: efficiency focus, no domain-magnitude comparison); ACDC ("weather is the benchmark" — rebut: that's the comparison arm).
- **Reason:** Concrete missing quantification with RAW datasets now available; keeps.

## C-0312 — Corruption doesn't just lower accuracy — it biases predictions toward priors

- **Decision:** KILL
- **Closest Prior Works:** Ovadia et al., "Can You Trust Your Model's Uncertainty?" (NeurIPS 2019) — prediction-distribution behavior under shift; TENT (Wang et al., ICLR 2021) and entropy analyses documenting prior-collapse under corruption; class-bias-under-shift observations in TTA literature.
- **Existing Work Did:** Documented systematic prediction-distribution distortion (not just accuracy loss) under corruption, motivating entropy/prior-correction methods.
- **Exact Difference:** Prior-collapse direction is observed in existing TTA analyses.
- **Remaining Novelty:** Low-medium; a cleaner quantification, but the phenomenon is named.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Ovadia et al.; TTA prior-correction papers.
- **Reason:** Phenomenon published within the TTA program.

## C-0320 — Mild shifts compound super-linearly

- **Decision:** KEEP
- **Closest Prior Works:** ImageNet-C̄ and corruption-composition studies (limited pairwise compositions in robustness suites); "3D Common Corruptions" (Kar et al., CVPR 2022); shift-composition observations scattered in robustness papers — SEARCH FOUND NO systematic composition-law study on natural shift axes.
- **Existing Work Did:** Benchmarked single-axis severities exhaustively; occasional two-corruption compositions without a predictive model.
- **Exact Difference:** No published test of whether error under combined mild shifts (weather × sensor × geography) exceeds the additive/independent-failure prediction from single-axis errors, i.e., no composition law.
- **Remaining Novelty:** A quantitative composition model with deployment relevance (real shifts arrive combined); falsifiable either way.
- **Novelty Confidence:** Medium (absence after search; risk that a robustness suite includes this in an appendix somewhere).
- **Reviewer Attack Papers:** 3D Common Corruptions ("realistic corruption suites exist" — rebut: no composition law fitted); ImageNet-C ("severity scaling is ours" — rebut: single-axis only).
- **Reason:** Precise untested quantitative claim over cheap frozen-model evaluation; keeps.

## C-0325 — Pixel metrics hide instance-level robustness collapse

- **Decision:** KILL
- **Closest Prior Works:** Fine-grained segmentation-metric critiques found in search (region/instance-aware mIoU variants, boundary metrics; "trying harder pays off"-style robustness metric analyses); panoptic-quality literature separating instance effects.
- **Existing Work Did:** Built instance-sensitive metrics and documented pixel-metric blind spots under degradation.
- **Exact Difference:** Robustness-specific re-run of a metric critique with existing tools.
- **Remaining Novelty:** Low-medium.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** Panoptic quality (Kirillov et al., 2019); instance-aware metric papers.
- **Reason:** Metric machinery exists; applying it under corruption is an evaluation exercise.

## C-0330 — Abstention fails exactly when it's needed

- **Decision:** KILL
- **Closest Prior Works:** Kamath et al., "Selective Question Answering under Domain Shift" (ACL 2020); selective-classification-under-shift studies (e.g., Fisch et al.; "selective classification can magnify disparities," Jones et al. 2021).
- **Existing Work Did:** Demonstrated selective-prediction confidence failure under exactly the shifts where abstention is needed.
- **Exact Difference:** Vision re-instantiation.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Kamath et al. 2020.
- **Reason:** Thesis established cross-domain.

## C-0332 — Does "accuracy on the line" survive dense prediction?

- **Decision:** KEEP
- **Closest Prior Works:** Miller et al., "Accuracy on the Line" (ICML 2021) — classification; Baek et al., "Agreement-on-the-Line" (NeurIPS 2022); scattered detection/segmentation ID-OOD correlation points inside robustness papers — no dedicated dense-task test found.
- **Existing Work Did:** Established the linear ID→OOD trend for classification and agreement-based estimation; the phenomenon is foundational to robustness-benchmark interpretation.
- **Exact Difference:** No systematic test on dense structured tasks where errors are spatially correlated and metrics are set-based (mIoU/PQ); no analysis of which pixel subpopulations break linearity.
- **Remaining Novelty:** Scope test of a foundational empirical law + residual-structure analysis (boundary vs interior, rare vs common classes); either outcome matters for OOD-performance prediction in deployment.
- **Novelty Confidence:** Medium-high (search found classification/detection points, not a dense-task study).
- **Reviewer Attack Papers:** Miller et al. ("the law is ours" — rebut: scope test is the contribution); Baek et al. ("agreement generalizes" — rebut: untested for structured outputs).
- **Reason:** Cheap frozen-model study answering whether a load-bearing law extends; keeps.

## C-0334 — One spectral-bias number behind texture bias, shortcuts, and adversarial fragility

- **Decision:** KILL
- **Closest Prior Works:** Geirhos et al., texture bias (ICLR 2019); Yin et al., "A Fourier Perspective on Model Robustness" (NeurIPS 2019); Wang et al., "What Do Neural Networks Learn in Image Classification? A Frequency Shortcut Perspective" (ICCV 2023).
- **Existing Work Did:** Established each pairwise frequency link (texture↔frequency, robustness↔frequency, shortcuts↔frequency).
- **Exact Difference:** The single-latent-factor unification claim; likely too strong, and disconfirming it is a weak paper.
- **Remaining Novelty:** Unification framing only.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** All three above.
- **Reason:** Pairwise links owned; unification is high-risk/low-reward.

## C-0338 — Visual composition follows the data's co-occurrence statistics — a quantitative law

- **Decision:** KILL
- **Closest Prior Works:** Udandarao et al., "No 'Zero-Shot' Without Exponential Data: Pretraining Concept Frequency Determines Multimodal Model Performance" (NeurIPS 2024); pretraining co-occurrence→performance analyses found in search.
- **Existing Work Did:** Fitted quantitative frequency→capability laws for multimodal models, including compositional probes.
- **Exact Difference:** Co-occurrence (pairwise) vs frequency (unary) statistics — partially covered in follow-ups.
- **Remaining Novelty:** Marginal increment on an active quantitative program.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** Udandarao et al. 2024.
- **Reason:** The law-fitting program exists and is fast-moving.

## C-0343 — Neural collapse is an epiphenomenon

- **Decision:** KILL
- **Closest Prior Works:** Search hits arguing collapse is not necessary for generalization (flatness-vs-collapse dissociation analyses, 2023–24); Papyan/Han/Donoho lineage and its many critical follow-ups; "neural collapse in the wild" studies.
- **Existing Work Did:** Both directions (collapse matters / collapse is incidental) already argued with experiments; instructed extra-harsh zone.
- **Exact Difference:** None sufficient.
- **Remaining Novelty:** None sufficient in a saturated debate.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Neural-collapse critique papers 2023–24.
- **Reason:** Crowded zone, harsh default; kill.

## C-0348 — Underspecification grows with scale

- **Decision:** KILL
- **Closest Prior Works:** D'Amour et al., "Underspecification Presents Challenges for Credibility in Modern Machine Learning" (JMLR 2022); seed-variance-at-scale follow-ups.
- **Existing Work Did:** Defined and measured underspecification across pipelines; scale trends examined in follow-ups.
- **Exact Difference:** The scale-trend question is a natural follow-up the originating group is best-positioned to run; compute-heavy for an outsider.
- **Remaining Novelty:** Low-medium at unaffordable cost.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** D'Amour et al.
- **Reason:** Cost/ownership; incremental over the defining paper.

## C-0349 — Much of the "domain gap" is an annotation-convention gap

- **Decision:** KILL
- **Closest Prior Works:** Cross-dataset label-inconsistency studies (label errors: Northcutt et al., NeurIPS 2021; taxonomy-mapping work in MSeg, Lambert et al., CVPR 2020); Cluster A survivor A-0194 and Cluster B survivors B-0112/B-0159 (same annotation-convention territory).
- **Existing Work Did:** MSeg explicitly measured and fixed cross-dataset annotation-convention mismatch to enable joint training — the constructive version of this claim.
- **Exact Difference:** Attribution accounting (what fraction of "domain gap" is convention) — but triply duplicated inside this pipeline.
- **Remaining Novelty:** None locally.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** MSeg.
- **Reason:** Internal duplication ×3 + MSeg prior.

## C-0355 — Head-class data improves tail-class generalization

- **Decision:** MUTATE
- **Closest Prior Works:** Liu et al., OLTR (CVPR 2019) — head→tail knowledge transfer; Kang et al. 2020 (decoupling); long-tail transfer/feature-sharing analyses (e.g., "learning to model the tail," Wang et al. 2017).
- **Existing Work Did:** Established that head-class data shapes features that tail classes reuse; built methods exploiting it.
- **Exact Difference:** No published *annotation-budget allocation* analysis: the marginal value of the next head label for tail performance, the crossover point where head labels beat tail labels, and a pre-computable predictor (feature-sharing score) of that crossover.
- **Remaining Novelty:** Decision-relevant economics of labeling with a predictive moderator — distinct from method papers.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** OLTR/Kang ("transfer is known" — rebut: existence ≠ marginal-allocation curve); active-learning literature ("budget allocation is ours" — rebut: class-targeted head-vs-tail allocation with sharing moderator is absent).
- **Reason:** MUTATED to the allocation-crossover + moderator version (M7); the bare transfer claim is old news.

## C-0360 — A resolution ceiling law for fine-grained transfer

- **Decision:** KILL
- **Closest Prior Works:** Patchification/resolution scaling-law study found in search (2025; pixel/patch-size scaling laws incl. fine-grained effects); FlexiViT (Beyer et al., 2023); FixRes (Touvron et al., 2019).
- **Existing Work Did:** Fitted resolution/patch scaling curves including saturation ("ceiling") behavior on transfer tasks.
- **Exact Difference:** Fine-grained-transfer-specific curve extraction.
- **Remaining Novelty:** Low.
- **Novelty Confidence:** Medium-high.
- **Reviewer Attack Papers:** The patchification scaling-law study; FixRes.
- **Reason:** Ceiling behavior already in published curves.

## C-0361 — Agent-run replication at literature scale

- **Decision:** KILL
- **Closest Prior Works:** PaperBench (OpenAI, 2025); CORE-Bench (Siegel et al., 2024); agent-replication competitions and AI-scientist evaluation suites.
- **Existing Work Did:** Built the benchmarks and ran agent-based replication of papers at increasing scale — an established, resourced subfield.
- **Exact Difference:** "Literature scale" ambition; the infrastructure race is owned by large labs.
- **Remaining Novelty:** None available to this pipeline.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** PaperBench; CORE-Bench.
- **Reason:** Active subfield with dedicated teams.

## C-0365 — Which pre-deep-learning ideas revive on foundation features?

- **Decision:** MUTATE
- **Closest Prior Works:** Dense-CRF-on-modern-features results (declining benefit documented across segmentation generations); classical-component revivals (e.g., nearest-neighbor inference on DINOv2, superpixel-assisted SAM variants); no *systematic* revival audit found.
- **Existing Work Did:** Individual revivals tested ad hoc; no predictive framework for *which* classical priors help on which foundation features.
- **Exact Difference:** The generic survey ("try old things on new features") is unfocused; the missing piece is a *failure-mode-matched* prediction: classical components encode priors (boundary snapping, spatial smoothness, geometric verification) that help exactly where the foundation model's measured failure modes leave those priors unmet.
- **Remaining Novelty:** A testable matching principle rather than a grab-bag survey; each confirmed/refuted match is informative.
- **Novelty Confidence:** Medium.
- **Reviewer Attack Papers:** CRF-decline results ("classical priors stopped helping" — rebut: that's one prior on one model family; the principle predicts when they resume helping); SAM-variant papers ("we already combine superpixels" — rebut: ad hoc, not prediction-driven).
- **Reason:** MUTATED to failure-mode-matched revival prediction (M8); the survey version would be rejected as unfocused.

## C-0372 — Adversarial collaboration as a research protocol for vision disputes

- **Decision:** KILL
- **Closest Prior Works:** Adversarial-collaboration methodology in psychology/economics (Kahneman-associated protocols; registered adversarial replications); ML reproducibility-challenge infrastructure.
- **Existing Work Did:** Developed and validated the protocol in other empirical fields; ML meta-science borrows it occasionally.
- **Exact Difference:** Applying to vision disputes is community organizing, not a research result this pipeline can produce.
- **Remaining Novelty:** Not a paper; a workshop proposal.
- **Novelty Confidence:** High.
- **Reviewer Attack Papers:** Meta-science methodology literature.
- **Reason:** Out of scope for an experimental-paper pipeline.

---

## Tally

| Decision | Count | IDs |
|---|---|---|
| KEEP | 10 | C-0028, C-0090, C-0093, C-0128, C-0229, C-0276 (absorbs C-0279), C-0302, C-0310, C-0320, C-0332 |
| MUTATE | 8 | C-0002, C-0014, C-0047, C-0068, C-0099, C-0158, C-0355, C-0365 |
| KILL | 67 | all remaining survivors (incl. C-0279 folded into C-0276) |

Surviving total (KEEP + MUTATE): **18** — within the 16–18 target.

Cross-cluster duplicates killed: C-0029 (↔B-0050), C-0051 (↔A-0200), C-0154 (↔B-0269), C-0293 (↔B-0274, A-0152), C-0349 (↔A-0194, B-0112, B-0159).

Instructed harsh zones enforced: CLIP registers (C-0095 killed), LoRA/fine-tuning forgetting (C-0064 killed; C-0068 kept only as a mutated precise control), CoT for vision (C-0265 killed), neural collapse (C-0343 killed), SSL-vs-supervised scale confounds (C-0103 killed; C-0099 kept only as a mutated confound-audit).
