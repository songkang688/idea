# Stage-2 Kills — Batch B (Agent E)

**268 of 345 killed.** Full one-line justification for every kill is in the table below;
the same text is in `scores.jsonl` (`note` field). Kills are cheap to reverse: any of these
can be revived by the PI if new information lands (see `AGENT_REPORT.md` for the 10 I nearly revived myself).

## Kill taxonomy (why ideas died)

1. **Already published (largest category).** The core claim exists in 2022–2026 literature —
   e.g. 0002 (CLIP dense info readout-accessible: MaskCLIP/SCLIP/NACLIP), 0136 (forgetting =
   recoverable rotation: Davari et al. CVPR'22), 0175 (interactive-seg click-policy artifacts:
   RClicks NeurIPS'24), 0197 (transferability estimation: LEEP/LogME/TransRate), 0279
   (modality-resolved medical sufficiency map: DINOv3-medical benchmark arXiv 2509.06467).
2. **Dominated by a sibling.** Same family, weaker version — the family's best member is kept
   and the rest die (e.g. much of the 0095–0133 PEFT-mechanics family collapses into 0095/0098/0101/0104).
3. **Engineering, not science.** A method/benchmark proposal with no falsifiable claim about the world.
4. **Confounded by design.** The stated experiment cannot isolate the claimed cause (frequent in
   language-geometry and medical clusters where visual difficulty confounds supervision effects).
5. **Underpowered for a PhD-year.** Requires pretraining sweeps or annotation budgets far beyond
   a single-investigator year, with no cheap pilot that de-risks it.
6. **Descriptive with no lever.** Even a clean positive result would not change what anyone builds
   or believes.

## Full kill table (268)

### vfm_failure (27 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0002 | 3.79 | MaskCLIP/SCLIP/NACLIP already showed CLIP dense info is readout-accessible; core claim published |
| W2-B-0003 | 3.79 | object-centric SSL bias on stuff classes is folk knowledge + partially documented; incremental |
| W2-B-0004 | 3.5 | feature spectra vs boundary quality; resolution confounds likely dominate; weak causal story |
| W2-B-0006 | 3.57 | CKA layer-pair fusion; ensemble-engineering flavored, CKA-task link weak |
| W2-B-0007 | 3.71 | background reliance of CLIP known (context bias lit); dense link incremental |
| W2-B-0008 | 3.93 | near-miss: patch-hubness of sigmoid vs softmax loss is cute but data confound (CLIP vs SigLIP) hard to kill |
| W2-B-0009 | 3.36 | LVLM counting bottleneck at projector already actively published 2024-25 (connector information-loss papers) |
| W2-B-0010 | 3.93 | near-miss: text-hub false positives plausible + cheap, but hubness lit crowds novelty; fold into 0042 family |
| W2-B-0011 | 3.64 | rotation-vs-translation equivariance anisotropy; equivariance audits exist; mid significance |
| W2-B-0012 | 3.5 | token-routing ablation; attention-rank proxy weak; interpretability-crowded |
| W2-B-0014 | 3.64 | near-miss: DINO version thin-structure regression is timely (v3) but bundles data/recipe changes; documentation not mechanism |
| W2-B-0015 | 3.64 | near-miss: depth-from-PE decomposition fun, but shuffled stimuli break scene statistics; confound-heavy |
| W2-B-0016 | 3.57 | shape-bias-predicts-transfer heavily mined (Geirhos lineage); correlation study on public zoo |
| W2-B-0017 | 3.86 | modality-gap caps dense alignment; fold into 0074 attack family; gap lit crowded |
| W2-B-0019 | 3.07 | color-augmentation invariance destroying hue info published (What Should Not Be Contrastive, etc.) |
| W2-B-0020 | 3.71 | per-class best layer; probing-lit adjacent; oracle gap likely small and noisy |
| W2-B-0021 | 3.5 | corruption phase transitions; cliff likely benchmark artifact; weak theory |
| W2-B-0022 | 3.79 | near-miss: context-bleed radius metric is neat but composites unrealistic; revive if boundary-error prediction needed |
| W2-B-0024 | 3.14 | curation-as-hidden-supervision needs matched uncurated checkpoints = pretraining budget; infeasible here |
| W2-B-0027 | 3.79 | merge into 0001: norm-vs-entropy uncertainty is the applied half of the same experiment |
| W2-B-0028 | 3.07 | pretraining scale-histogram imprint; corpus access limited; proxy corpora weaken claim |
| W2-B-0029 | 3.71 | near-miss: center-periphery gradient cheap and cute; photographer-bias confound; revive as sanity audit |
| W2-B-0030 | 3.64 | fusion-gains-are-resolution: fold into 0213 which generalizes the confound |
| W2-B-0031 | 3.5 | inference-time register manipulation already explored (test-time registers, 2025); marginal residual |
| W2-B-0032 | 3.57 | bag-of-patches CLIP; adjacent to bag-of-words CLIP lit; PE-protocol dependence |
| W2-B-0034 | 3.29 | illumination vs local noise brittleness; perturbation-magnitude matching is ill-posed |
| W2-B-0035 | 3.93 | near-miss: ToMe boundary-straddle safety score practical; efficiency-crowd will re-derive; low ceiling |

### vlm_dense_failure (28 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0037 | 3.43 | concept-frequency predicts zero-shot performance already published (Udandarao et al. 2024); dense port incremental |
| W2-B-0038 | 3.57 | negation blindness known (GRES no-target, NegBench); confidence angle small residual |
| W2-B-0039 | 3.5 | co-occurrence-prior hallucination in LVLMs published (POPE follow-ups); placement-model twist minor |
| W2-B-0040 | 3.5 | near-miss: enumeration-binding deficit; counting-mechanism lit is hot 2024-25, likely scooped in part |
| W2-B-0041 | 3.57 | near-miss: early-layer spatial info overwritten later; LVLM layer-probing lit growing fast; verify before revival |
| W2-B-0044 | 3.57 | near-miss: polysemy disambiguation in dense pathway; curation cost vs payoff mid |
| W2-B-0045 | 3.64 | clause ablation utilization; Cirik et al. showed RES ignores language; fold into 0036 |
| W2-B-0046 | 3.29 | edge-anchoring bias; camouflage eval exists; supervised baselines share bias |
| W2-B-0047 | 3.5 | stage-decomposed open-vocab errors; solid engineering audit, low surprise |
| W2-B-0048 | 3.57 | near-miss: reflections/depictions confusion is fun; phrasing-dependence makes ground truth mushy |
| W2-B-0049 | 3.5 | typographic attacks ported to RES; attack lit saturated; predictable result |
| W2-B-0050 | 3.57 | plural morphology ignored; cheap but thin; one-table paper |
| W2-B-0051 | 3.5 | viewer-vs-object-centric frames; spatial-frame lit exists (Whats-up etc.); dense port incremental |
| W2-B-0052 | 3.57 | amodal instruction blindness; expected null (no amodal training data); documentation value only |
| W2-B-0053 | 3.86 | near-miss: rare-class miscalibration; calibration angle better covered by 0180/0145; fold |
| W2-B-0055 | 3.29 | first-mention rollout bias; attribution-method-dependent; fragile |
| W2-B-0056 | 3.71 | near-miss: specificity monotonicity violation; length confounds; fold into 0042/0178 paraphrase family |
| W2-B-0057 | 3.64 | hallucination-rate to seg-FP correlation; correlational one-pager |
| W2-B-0058 | 3.57 | near-miss: color-term snapping vs World-Color-Survey; charming psychophysics; calibration burden high |
| W2-B-0059 | 3.43 | distractor scaling slopes; difficulty curves exist in RES analyses |
| W2-B-0060 | 3.71 | template sensitivity dense vs global; covered better by 0168 decomposition |
| W2-B-0061 | 3.5 | cross-lingual RES; multilingual grounding studied; translation confounds |
| W2-B-0063 | 3.43 | verification>localization gap exploited by existing tool-use/search pipelines; framing not enough |
| W2-B-0065 | 3.36 | action grounding via pose priors; typicality estimation circular |
| W2-B-0066 | 3.64 | open-vocab thing bias vs stuff; caption-mention explanation known direction |
| W2-B-0067 | 3.57 | caption-ground cycle consistency; cycle-consistency well-mined; correlated-error blind spot acknowledged but fatal |
| W2-B-0069 | 3.5 | interior-vs-boundary error anatomy VLM vs CNN; descriptive taxonomy, low ceiling |
| W2-B-0070 | 3.43 | politeness padding degrades grounding; LLM-side prompt-format effects known; port |

### finetune_instability (23 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0071 | 3.36 | attention-entropy collapse tied to instability already published (Zhai et al. ICML23); FT-localization residual small |
| W2-B-0072 | 3.36 | warmup-masks-instability; survivorship analysis needs many runs; payoff unclear |
| W2-B-0073 | 3.43 | seed variance in LN gains + transplants; neat but niche; fold into 0087/0092 program |
| W2-B-0075 | 3.14 | data-order variance + coherence curriculum; curriculum lit crowded; cost offsets benefit |
| W2-B-0076 | 3.14 | bf16 softmax rows at outlier tokens; plausible but divergence too rare to power the study |
| W2-B-0079 | 3.57 | near-miss HRHR: grokking in dense FT; 50x-horizon compute for plausible null; revive with cheap backbone if PI wants a moonshot |
| W2-B-0080 | 3.43 | EMA=interpolation-to-init; adjacent to soups/WiSE-FT algebra; low surprise |
| W2-B-0081 | 3.21 | sharpness transfer pretraining->FT; reparameterization-sensitive measures undermine it |
| W2-B-0082 | 3.43 | LN-freeze warmup; optimizer-recipe engineering; subsumed by warmup practice |
| W2-B-0083 | 3.43 | minority-class gradient spikes; long-tail training lit covers caps/clipping variants |
| W2-B-0084 | 3.36 | anisotropic damage in task subspace; LP-FT theory adjacent; confirmatory |
| W2-B-0085 | 3.0 | decay-toward-init is L2-SP (2018) / trust-region FT; already published, cited widely |
| W2-B-0086 | 3.29 | PE transient on resolution change; narrow; modern PEs sidestep |
| W2-B-0088 | 3.21 | non-monotonic augmentation destabilization; 10-seed sweeps x levels expensive for a curve |
| W2-B-0089 | 3.5 | Adam second-moment warm start; optimizer-trick space; low science content |
| W2-B-0090 | 3.36 | multi-task interference asymmetry; MTL gradient-conflict lit heavy |
| W2-B-0091 | 3.21 | effective-rank early stopping; rank-collapse lit adjacent; predictor likely task-brittle |
| W2-B-0093 | 3.36 | text-side spike precursors in CLIP FT; niche instrumentation study |
| W2-B-0094 | 3.64 | near-miss CI: SAM harms dense-feature reuse; accuracy-matching fiddly; revive if flatness-vs-transfer heats up |
| W2-B-0096 | 3.64 | checkpoint averaging blurs boundaries; small effect risk; metric-noise-bound |
| W2-B-0097 | 3.43 | basin-exit barrier story conflicts with Neyshabur et al. (FT stays in basin); partially published terrain |
| W2-B-0099 | 3.79 | near-miss: boundary-noise as instability driver; practical; fold into 0087 program as an ablation arm |
| W2-B-0100 | 3.86 | near-miss DP: hardware nondeterminism noise floor; service paper; Zhuang et al. covered classification; seg residual thin |

### peft_limits (27 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0102 | 3.14 | intruder dimensions = Shuttleworth et al. 2024 (LoRA vs full FT: illusion of equivalence); published |
| W2-B-0103 | 3.5 | MLP-vs-attention LoRA placement; placement sweeps exist across PEFT papers |
| W2-B-0106 | 4.07 | near-miss CF: BitFit=moment-matching closed form; elegant but BitFit relevance fading; revive as workshop-scale test |
| W2-B-0107 | 3.36 | adapter bottleneck information loss; probing-accessibility caveat weakens; predictable |
| W2-B-0109 | 3.5 | merge-then-quantize damage; QA-LoRA already motivated by exactly this incompatibility |
| W2-B-0110 | 3.5 | IA3 multipliers as interpretability probe; sparsity may be parameterization artifact |
| W2-B-0111 | 3.5 | LoRA-dropout=interpolation; cute algebra, low stakes |
| W2-B-0113 | 3.71 | near-miss: rank scales with boundary density; law-like but boundary density proxies difficulty; fold into 0101 |
| W2-B-0115 | 3.29 | LoRA LR scaling rules; LoRA+/muP-style analyses already circulating |
| W2-B-0116 | 3.43 | one-pass placement diagnostic; engineering utility, thin science |
| W2-B-0117 | 3.43 | sequential vs merged LoRA interference; continual-PEFT lit crowding |
| W2-B-0119 | 3.64 | CoOp drift to seen-class neighborhood; base-new tradeoff heavily mined (CoCoOp lineage) |
| W2-B-0120 | 3.5 | text-side vs vision-side LoRA transfer; useful ablation, not a thesis |
| W2-B-0121 | 3.79 | near-miss CF: linear adapters suffice -> adaptation=subspace realignment; revive as an arm inside 0101 |
| W2-B-0122 | 3.71 | near-miss: readout-dependent forgetting reversal; important caveat; fold into 0163 measurement-reform program |
| W2-B-0123 | 3.5 | quantized-backbone LoRA boundary damage; niche deployment note |
| W2-B-0124 | 3.43 | LoRA composition subspace overlap; task-arithmetic lit dense |
| W2-B-0125 | 3.21 | PEFT hyperparameter transfer across scales; muP-adjacent; sweep-heavy |
| W2-B-0126 | 3.64 | divergence-onset predicts LoRA gap; fold into 0098 attack family as secondary prediction |
| W2-B-0127 | 3.64 | near-miss: PEFT-vs-full phase diagram; fold into 0234 (same boundary, frozen-vs-tuned axis is more general) |
| W2-B-0128 | 3.79 | prompt gradient attenuation; mechanism arm of 0105; not standalone |
| W2-B-0129 | 3.36 | LoRA-library routing failure; systems paper; oracle-vs-learned gap expected |
| W2-B-0130 | 3.57 | near-miss DP: structured-LoRA variants collapse under matched budgets; valuable but re-implementation slog invites disputes |
| W2-B-0131 | 3.79 | near-miss CF: IA3 breaks norm-based OOD detectors; safety regression note; single-table finding |
| W2-B-0132 | 3.64 | stem-only adaptation for low-level shift; fold into 0253 input-side sufficiency boundary |
| W2-B-0134 | 3.29 | LoRA ensembles lack diversity; LoRA-ensemble papers 2023-24 already probe this |
| W2-B-0135 | 3.5 | pre-attention vs post-MLP dissociation; clean story unlikely to survive deep stacks |

### catastrophic_forgetting (24 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0136 | 4.0 | ATTACKED->KILL: Davari et al. CVPR22 (Probing Representation Forgetting) + accessibility-collapse line already show forgetting is largely readout-recoverable rotation, not erasure; core claim published. Mutation (dense emergent-ability erasure in VFMs) folded into 0122/0163 territory. |
| W2-B-0138 | 3.36 | similarity-ordered forgetting; interference-vs-similarity mapped since Ramasesh 2020 |
| W2-B-0139 | 3.71 | near-miss: global-before-local forgetting order; fold into 0145+0163 chronology program |
| W2-B-0140 | 3.43 | retrieval-first cascade; same chronology program; not standalone |
| W2-B-0141 | 3.43 | disjoint-class distillation; method tweak |
| W2-B-0142 | 3.5 | weight-delta vs function dissociation; known in spirit (null-space moves); confirmatory |
| W2-B-0143 | 3.57 | near-miss: interpolation recovers classification not dense abilities; fold into 0252 kink program |
| W2-B-0144 | 3.57 | frozen-but-broken text tower; joint-space drift story adjacent to modality-gap family; fold into 0074 |
| W2-B-0146 | 3.5 | small LR postpones not prevents; dose-response framing nice but folds into 0146~0163 measurement program |
| W2-B-0147 | 3.29 | task-order forgetting asymmetry; CL task-order lit exists |
| W2-B-0148 | 3.57 | near-miss: PEFT damage expressed downstream of frozen layers; patching artifacts risk; revive for mechanistic follow-up |
| W2-B-0149 | 3.21 | generative replay threshold; replay lit saturated |
| W2-B-0150 | 3.43 | robustness forgotten faster than accuracy; plausible, folds into 0163 OOD-probe reform |
| W2-B-0151 | 3.14 | OCR-loss changes text-region segmentation; narrow phenotype |
| W2-B-0152 | 3.5 | near-miss: abrupt emergent-ability collapse; ultra-dense checkpointing cost; metric-thresholding artifact risk |
| W2-B-0153 | 3.5 | near-miss DP: Fisher-on-proxy misprotection; useful negative for EWC-on-VFM; revive if PI wants a debunk arm |
| W2-B-0155 | 3.43 | SSL-anchor vs distillation; method bake-off |
| W2-B-0156 | 3.93 | near-miss CF: re-grafting patch-embed recovers zero-shot; single-experiment gem; fold as arm of 0165/0252 or revive |
| W2-B-0158 | 3.57 | beneficial-forgetting class subset; fold into 0137 (same thesis, weaker instrument) |
| W2-B-0159 | 3.43 | U-shaped forgetting vs data size; schedule-matching subtleties eat the effect |
| W2-B-0160 | 3.0 | sparse-mask zero-forgetting adaptation; supermask/lottery CL lit already dense |
| W2-B-0161 | 3.43 | detection forgetting lives in queries; component study, DETR-specific |
| W2-B-0162 | 3.43 | protect class-selective neurons; unit-protection lit exists, distributed-representation objection strong |
| W2-B-0165 | 3.36 | per-layer interpolation fingerprints; layer-wise merging papers circulating; fold into 0252 |

### prompt_sensitivity (25 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0166 | 3.71 | near-miss: jitter-variance predicts user disagreement; RClicks-adjacent; fold into 0175 verdict |
| W2-B-0167 | 3.5 | point-order invariance violation; trivially true/false per architecture; audit note |
| W2-B-0170 | 3.57 | prompt-perturbation variance as uncertainty; TTA/ensemble uncertainty adjacent; engineering |
| W2-B-0171 | 3.5 | learned prompts fail under shift; CoOp-robustness studied; reversal framing minor |
| W2-B-0173 | 3.57 | box-tightness calibration; practical knob, thin science |
| W2-B-0174 | 3.14 | prompt position effects; encoder-dependent minutiae |
| W2-B-0175 | 3.86 | ATTACKED->KILL: RClicks (NeurIPS 2024) + TETRIS already demonstrate interactive-seg rankings flip under click-policy changes; exact claim published. |
| W2-B-0176 | 3.29 | prompt transfer tracks data overlap; open-model grid exists but result low-stakes |
| W2-B-0177 | 3.14 | inverted-U prompt length; curve-fitting exercise |
| W2-B-0178 | 3.5 | paraphrase-inequivalence gap; fold into 0042 synonym program (same instrument, text side) |
| W2-B-0179 | 3.5 | part-whole click ambiguity resolved by dataset priors; fold into 0326 basic-level program |
| W2-B-0180 | 4.0 | near-miss CF: calibration differs by prompt modality; single-table; revive as arm of 0194/0145 calibration suite |
| W2-B-0181 | 3.64 | near-miss: visual marks act globally not locally; red-circle lit adjacent; mechanism study worth revisiting |
| W2-B-0183 | 3.64 | adversarial point configurations; attack-surface catalog; absurdity metric contestable |
| W2-B-0184 | 3.5 | ensemble aggregation level; smoothing analysis predictable |
| W2-B-0185 | 3.64 | near-miss: refinement oscillation dynamics; Jacobian predictor speculative; user adaptation breaks loop realism |
| W2-B-0186 | 3.36 | morphosyntax leaks into masks; cute, frequency confounds, thin |
| W2-B-0187 | 3.64 | near-miss DP: prompt tuning as bug-mining; definitional fight over bug-vs-alignment; revive if eval-reform push |
| W2-B-0188 | 3.14 | real-user prompt distributions reorder rankings; RClicks does clicks; text side folds into 0042 |
| W2-B-0189 | 3.36 | prompt-dropout robustness frontier; training-recipe paper |
| W2-B-0190 | 3.36 | prompt-embedding arithmetic regions; composition lit crowded |
| W2-B-0191 | 3.21 | click pragmatics differ by training data; needs controlled retraining; fold into 0326 |
| W2-B-0192 | 3.57 | near-miss: topology-early boundary-late prompt processing; architecture-fragmented; mechanistic follow-up material |
| W2-B-0193 | 3.5 | language tax on dense outputs; fold with 0061; translation confounds |
| W2-B-0195 | 3.64 | near-miss: default-mask saliency prior predicts prompt effort; neat descriptive study; revive for HCI venue |

### representation_mismatch (23 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0197 | 3.43 | adaptation-cost prediction = transferability-estimation lit (LEEP/LogME/TransRate); published family |
| W2-B-0198 | 3.5 | attention-carries-localization; MaskCLIP value-readout and SCLIP already exploit this |
| W2-B-0199 | 3.79 | near-miss: spectral split semantics-low/boundary-high; fold into 0208+0210 geometry program |
| W2-B-0201 | 3.36 | invariance-cost table needs matched SSL pretraining runs; compute-infeasible; direction covered by Xiao et al. |
| W2-B-0202 | 3.57 | near-miss: local dimensional collapse metric; estimator noise at small neighborhoods; fold into 0219/0210 |
| W2-B-0204 | 3.5 | SNR maps things-vs-stuff; fold into 0003 verdict (same phenomenon, new metric) |
| W2-B-0205 | 3.86 | near-miss CF: k-NN sufficiency bounds; dimensionality curse; revive as methodology note if PI needs protocol paper |
| W2-B-0206 | 3.36 | objective-mixing geometry frontier; requires pretraining grid; infeasible in scope |
| W2-B-0207 | 3.29 | requirements-x-invariances matrix; framework paper without a sharp falsifier |
| W2-B-0209 | 3.57 | quantization-hurts-regression; fold into 0304 (morphs are the cleaner instrument) |
| W2-B-0210 | 3.93 | near-miss: oversmoothness ratio predicts boundary displacement; strong law candidate; revive if 0208 saturates |
| W2-B-0211 | 3.43 | attention-sink starves patches; register-lit adjacent; fold into 0001 family |
| W2-B-0212 | 4.07 | near-miss CF: whitening reveals dense info; single-intervention study; revive as an arm of 0200 |
| W2-B-0214 | 3.14 | hard-negative metric distortion; recipe metadata unavailable; controlled retraining needed |
| W2-B-0216 | 3.29 | instance-discrimination preserves part structure; supervised-collapse story known (neural collapse lineage) |
| W2-B-0217 | 3.57 | PE-dependency ratio; off-distribution ablation; narrow |
| W2-B-0218 | 3.5 | peak layer shifts with resolution; interaction footnote |
| W2-B-0219 | 3.5 | boundary pixels in low-margin no-mans-land; fold into 0210/0208 |
| W2-B-0220 | 3.64 | channel-magnitude rebalancing; quick trick, thin theory |
| W2-B-0221 | 3.86 | near-miss: correspondence and semantics as orthogonal axes; Probing-3D-Awareness partially shows dissociation; residual = model cards |
| W2-B-0223 | 3.64 | near-miss DP: readout-data ceiling convergence; asymptote extrapolation contestable; revive if PI wants the null-killer |
| W2-B-0224 | 3.14 | registers improve patch purity; register paper + follow-ups already show cleaner maps; confirmatory |
| W2-B-0225 | 3.43 | near-miss: cosine-vs-metric geometry mismatch; conceptually rich, instrument fuzzy; fold into 0304/0209 |

### crossdomain_frozen_vs_tuned (22 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0228 | 3.64 | near-miss: 2x2 factorial features-vs-readout; fold into 0234 phase-diagram program |
| W2-B-0229 | 3.29 | augmentation-corruption overlap predicts robustness = Mintun et al. 2021; published |
| W2-B-0230 | 3.36 | readout-only TTA risk-adjusted dominance; TTA lit has T3A/TENT comparisons; incremental |
| W2-B-0231 | 3.64 | near-miss: gap-metric paradox (predicts tuned not frozen); interesting; fold into 0234 as diagnostic |
| W2-B-0232 | 3.29 | shape channels erased first; population-level channel claims fragile |
| W2-B-0233 | 3.57 | near-miss: tuning as equity regression; important but region-stratified dense benchmarks scarce; revive with annotation budget |
| W2-B-0235 | 3.29 | multi-source conflict threshold; semantic complementarity confound |
| W2-B-0236 | 3.0 | shift-type-to-depth correspondence = Surgical Fine-Tuning (Lee et al. ICLR23); published |
| W2-B-0237 | 3.36 | RGB->IR stats matching; domain-specific engineering note |
| W2-B-0238 | 3.5 | near-miss: path-dependence/hysteresis of sequential tuning; replay likely erases; costly permutation design |
| W2-B-0239 | 3.71 | near-miss: accuracy-on-the-line breaks for boundary metrics; agreement-lit adjacent; revive if OOD-dense benchmarks materialize |
| W2-B-0240 | 3.43 | robustness repurchase cost curve; framing nice, folds into 0226 budget program |
| W2-B-0242 | 3.57 | near-miss: annotation-convention gap masquerades as domain gap; re-annotation cost; revive with 0154/0293 if PI funds annotation |
| W2-B-0244 | 3.79 | near-miss: cross-family frozen ensembles beat tuned OOD; FLOP-matching contestable; engineering flavor |
| W2-B-0245 | 3.57 | frozen/tuned per-input routing; oracle-gap systems paper |
| W2-B-0246 | 3.64 | calibration transfers for frozen not tuned; fold into 0108 calibration-shift program |
| W2-B-0247 | 3.5 | low-shot tail erosion; long-tail few-shot lit covers pieces |
| W2-B-0248 | 3.57 | feature-space augmentation substitutes pixel randomization; method paper |
| W2-B-0249 | 3.36 | near-miss: linear-vs-step aging frozen/tuned; time-stamped archive access is the blocker; revive with data partner |
| W2-B-0250 | 3.29 | bias trajectory predicts sim-to-real gap; cue-conflict porting; incremental |
| W2-B-0251 | 3.86 | near-miss: optimal layer moves earlier with gap; cheap law; fold into 0234/0196 as secondary prediction |
| W2-B-0253 | 3.93 | near-miss CF: input-transform sufficiency boundary; strong but overlaps 0243/0132; keep one input-side flagship (0243) |

### synthetic_adaptation (19 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0255 | 3.57 | near-miss: generator-VFM circularity; overlap estimation coarse for closed models; revive with open-lineage pairs |
| W2-B-0256 | 3.71 | near-miss: rare-class synthetic split verdict (recall up, boundary down); fold into 0254 decomposition |
| W2-B-0257 | 3.43 | fingerprint reliance decomposition; detection lit heavy; content-matched filtering hard |
| W2-B-0258 | 3.36 | per-class fidelity predicts gain; predictable regression study |
| W2-B-0259 | 3.14 | real-fraction mixing law; synthetic-image scaling laws (Fan et al. CVPR24) cover the terrain |
| W2-B-0260 | 3.57 | near-miss: caption-prior dense hallucinations from generated data; amplification isolation is delicate; revive as arm of 0254 |
| W2-B-0261 | 3.43 | perfect-synthetic vs noisy-real frontier; annotation-noise realism hard to control |
| W2-B-0262 | 3.5 | near-miss: self-filtering bias amplification; multi-round compute; fold into 0275 collapse-canary loop |
| W2-B-0265 | 3.43 | near-miss: geometric-consistency probes degrade after synthetic adaptation; probe validity burden; fold into 0273 |
| W2-B-0266 | 3.29 | low guidance beats high for training data; known in synthetic-data-for-classification lit (Azizi, Fan) |
| W2-B-0267 | 3.43 | near-miss: exchange rate non-monotonic across generator generations; version bundling confound; revive with coverage controls |
| W2-B-0269 | 3.36 | closed-loop prompt tuning brittleness; niche composite of 0187+0262 |
| W2-B-0270 | 3.29 | boundary-hard composites 10x value; copy-paste augmentation lit strong; value-density claim incremental |
| W2-B-0271 | 3.57 | generation route inherits nameability boundary; fold into 0243 (same boundary, second instrument) |
| W2-B-0272 | 3.57 | likelihood-stratified sampling repairs calibration; fold into 0254 as the fix arm |
| W2-B-0273 | 3.29 | near-miss: impossible-anatomy tolerance; vivid but violation construction delicate; revive with radiologist partner |
| W2-B-0274 | 3.5 | copy-paste vs diffusion matched budget; fold into 0263 (same question, corruption side) |
| W2-B-0276 | 3.71 | near-miss: low-rank PEFT immune to fingerprint shortcuts; capacity-shortcut law; revive as arm of 0254/0257 |
| W2-B-0277 | 3.5 | pseudo-label boundary-bias heredity; fold into 0275 loop program |

### medical_vfm_science (20 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0279 | 3.93 | ATTACKED->KILL: 'Does DINOv3 Set a New Medical Vision Standard?' (arXiv 2509.06467) + DINOv2-for-radiology (arXiv 2312.02366) + frozen-feature CT/CXR benchmarks already deliver the modality-resolved sufficiency map (DINOv3 strong except WSI/EM/PET). Residual matched-budget causal question lives in 0293. |
| W2-B-0280 | 3.43 | invariance-vs-findings audit; fold into 0279 (sufficiency map subsumes) + 0282 laterality instrument |
| W2-B-0281 | 3.71 | near-miss CF: HU-decodability loss; crisp; revive as arm of 0279 CT stratum |
| W2-B-0283 | 3.5 | burned-in text hijacks medical VLMs; shortcut lit (Zech, DeGrave) + typographic attacks make this predictable; document-only value |
| W2-B-0285 | 3.5 | prevalence-shift miscalibration; prior-shift correction lit mature; residual framing thin |
| W2-B-0287 | 3.43 | near-miss: hedged report language shifts thresholds; matched-evidence construction hard; revive with longitudinal data |
| W2-B-0288 | 3.5 | near-miss: anatomy completion vs evidence; rare-case data access blocks; revive with surgical-partner dataset |
| W2-B-0289 | 3.43 | stain invariance vs stain-defined identity; histopath augmentation debates cover much |
| W2-B-0290 | 3.29 | slice-continuity metric; 2.5D/3D consistency lit exists |
| W2-B-0291 | 3.29 | modality-distance forgetting law; composite of 0138+0291; measurement burden |
| W2-B-0292 | 3.57 | near-miss: severity-correlated label noise breaks noise-robust methods; adjudicated ground truth scarce; revive with consensus-panel data |
| W2-B-0294 | 3.07 | uncertainty vs inter-reader disagreement; comparisons published in medical segmentation lit |
| W2-B-0295 | 3.14 | rare-disease site overfit under PEFT; multi-site rare data access prohibitive |
| W2-B-0296 | 2.86 | Dice-dosimetric divergence documented in radiotherapy lit (Vaassen et al. lineage); tool exists |
| W2-B-0297 | 3.36 | near-miss: scanner-update step drift natural experiment; PACS metadata access is the blocker; revive with hospital partner |
| W2-B-0298 | 3.43 | near-miss: template-frequency predicts hallucinated findings; report-corpus access needed; fold into 0287/0298 family |
| W2-B-0299 | 3.29 | medical-vs-natural SSL geometry convergence; requires matched pretraining; infeasible |
| W2-B-0300 | 3.21 | patient-level leakage inflation known (Bussola et al.); rank-reordering quantification residual small |
| W2-B-0301 | 3.14 | federated LoRA subspace misalignment; federated-PEFT lit growing fast |
| W2-B-0302 | 2.79 | counterfactual lesion editing attribution; medical-counterfactual lit exists; editing-artifact circularity |

### language_geometry_alignment (18 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0306 | 3.5 | boundary-vocabulary poverty; corpus-level correlation confounded; 0321/0323 are sharper instruments |
| W2-B-0308 | 3.79 | near-miss: numerosity many-ceiling; subitizing lit in VLMs emerging; fold into counting family or revive |
| W2-B-0309 | 3.57 | nameable shapes better represented; fold into 0026 (region-level flagship of nameability family) |
| W2-B-0310 | 3.36 | preposition subspace is textual convention; embedding-arithmetic negative; thin |
| W2-B-0311 | 3.5 | canonical-view over-canonicalization; caption viewpoint statistics indirect |
| W2-B-0312 | 3.64 | near-miss: binding failure via chimeras; binding-problem-in-VLM papers emerging 2024-25; verify before revival |
| W2-B-0313 | 3.43 | caption diversity vs feature variance; frequency confound; correlational |
| W2-B-0314 | 3.71 | near-miss CF: negative-space blindness (holes/gaps); delightful; keep 0068 as the system-level version; revive for probe-level follow-up |
| W2-B-0315 | 3.36 | support relations undecodable; physical-reasoning benchmarks cover adjacent ground |
| W2-B-0316 | 3.43 | near-miss: describability vs saliency two-regime; eye-tracking+captioning data juggling; revive for cogsci venue |
| W2-B-0318 | 3.86 | near-miss: superlative operation-vs-representation dissociation; decodability-vs-usability framing good; fold into 0325 |
| W2-B-0319 | 3.43 | property-word frequency curve; Udandarao-style frequency-performance known; residual angle thin |
| W2-B-0320 | 3.43 | caption-style geometry dial; requires matched pretraining runs; infeasible in scope |
| W2-B-0321 | 3.64 | near-miss: texture-codability deficit; needs naming-norm collection; 0323 is the cheaper flagship; revive with norms in hand |
| W2-B-0322 | 3.57 | occlusion-language depth-order supervision; subtle stratification; low ceiling |
| W2-B-0324 | 3.14 | synonym splitting needs known training captions; open dense-alignment reproductions only; niche |
| W2-B-0327 | 3.5 | categorical prior resists geometric re-learning; fold into 0307 as dynamics arm |
| W2-B-0328 | 3.5 | near-miss: within-image supervision-density gradients; grounding-model circularity; revive with human-annotated captions |

### agentic_vision_hypotheses (12 kills)

| ID | Mean | Kill reason |
|---|---|---|
| W2-B-0330 | 3.57 | acuity-gated zoom; V*/visual-search lit close; fold into 0023 acuity program |
| W2-B-0331 | 3.86 | near-miss: self-verification correlated errors; LLM self-preference lit ports; quantification residual; revive if 0332 survives |
| W2-B-0333 | 3.57 | near-miss: debate amplifies priors on ambiguous images; debate-critique lit emerging; verify before revival |
| W2-B-0334 | 3.36 | name-based tool routing; cute audit, scaffold-sensitive |
| W2-B-0335 | 3.36 | uncertainty-guided querying floor; active-learning lit covers |
| W2-B-0336 | 3.36 | retrieval poisoning threshold; RAG-robustness ports |
| W2-B-0337 | 3.21 | tool-boundary quantization errors; instrumentation-heavy, narrow |
| W2-B-0340 | 3.57 | near-miss: calibration dies at tool interfaces; pairs with 0329; fold as its mechanism arm |
| W2-B-0341 | 3.29 | external visual scratchpads = Visual Sketchpad / Whiteboard-of-Thought (2024); published; load-factorized residual only |
| W2-B-0343 | 3.5 | self-training boundary drift; fold into 0275 (same canary, agent loop instance) |
| W2-B-0344 | 3.71 | near-miss: delegation metacognition; prompt-sensitivity of delegation behavior weakens; revive if 0329 program expands |
| W2-B-0345 | 3.43 | GUI-natural grounding transfer; GUI-grounding lit exploding 2024-26; transfer studies already appearing |

