# Stage 3 — Cluster B Prior-Work Killsheet

Adversarial prior-work hunt (Cloud Sub-Agent H) over the 86 Stage-2 Cluster B survivors (12 PROTECTED + 74 KEEP).
Default stance: "this idea has probably already been done." Every survivor was checked against web/arXiv search
results from this session or against literature verified in earlier passes. No invented papers; where no direct
prior work was found despite searching, the entry says so and novelty confidence is stated accordingly.

**Verdict totals: 66 KILL / 6 MUTATE / 14 KEEP.** Protected status did not shield ideas from direct prior-work hits
(7 of 12 PROTECTED killed).

Legend per entry — Closest prior works | What existing work did | Exact difference | Remaining novelty |
Novelty confidence | Reviewer attack papers | Verdict + reason.

---

## MedSeg

### B-0002 — Centerline flow field for tubular structures — KILL
- Closest prior: clDice (Shit et al., CVPR 2021); GraphMorph and related centerline/graph-based vessel extraction lines; flow-field/direction-field tubular tracking literature.
- Existing work did: topology-aware losses on centerlines; direction-field and graph-based extraction of vessels/airways; centerline-supervised training.
- Exact difference: idea proposes flow-field regression toward centerlines as primary output; prior work already regresses direction/distance fields and centerline heatmaps.
- Remaining novelty: none load-bearing; representation variants of an established family.
- Novelty confidence: high (that it is NOT novel).
- Reviewer attack: clDice; centerline distance-transform regression papers.
- Verdict: KILL — tubular flow/direction-field representations are an established, crowded family.

### B-0003 — Held-out-rater evaluation for probabilistic segmentation — KILL
- Closest prior: Probabilistic U-Net (Kohl et al., NeurIPS 2018) and successors; QUBIQ multi-rater challenge; multi-annotator modeling literature.
- Existing work did: mature modeling of inter-rater ambiguity; evaluation against rater distributions (GED, sample diversity).
- Exact difference: only the evaluation protocol (fit to k−1 raters, test on held-out rater) is new; the modeling is not.
- Remaining novelty: a protocol delta, publishable at most as a short evaluation note.
- Novelty confidence: high (not enough novelty).
- Reviewer attack: Prob U-Net line; QUBIQ.
- Verdict: KILL — evaluation-protocol delta on a mature subfield.

### B-0004 — Train against biomarker (volume) loss — KILL
- Closest prior: Bertels et al. 2020 (volume bias of soft-Dice, theoretical + empirical); volume/biomarker-supervised training losses in medical DL.
- Existing work did: characterized Dice-induced volume bias; trained with volume-aware and biomarker-aware objectives.
- Exact difference: idea's diagnosis and remedy both published.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: Bertels et al. 2020.
- Verdict: KILL — direct hit on both halves of the idea.

### B-0007 (PROTECTED) — Laterality-aware flipping — MUTATE
- Closest prior: horizontal-flip augmentation is universal practice; "don't mirror lateralized structures" is community folklore; no controlled published audit found (searched; SEARCH for a direct audit FAILED).
- Existing work did: augmentation surveys list flipping; some lateralized-task papers quietly disable it; nobody quantifies the damage.
- Exact difference: the fix is folklore, but the quantitative damage audit (which tasks, how much, which failure modes) is unpublished.
- Remaining novelty: the audit + a when-to-flip decision rule, not the fix.
- Novelty confidence: medium (audit appears open, but low ceiling as a full paper).
- Reviewer attack: any augmentation-ablation paper ("we already ablate flips").
- Verdict: MUTATE — reframe as a quantitative cross-task audit of mirroring damage on lateralized anatomy with a decision rule (see mutations file).

### B-0014 — Test-retest consistency loss — KILL
- Closest prior: scan-rescan repeatability studies of DL segmentation (Medical Physics 2024 line); consistency-regularization training on repeat scans/augmented views.
- Existing work did: measured scan-rescan variability of models; trained with consistency objectives across perturbed inputs.
- Exact difference: applying consistency loss specifically to physical rescans is a data-source variant of published consistency regularization.
- Remaining novelty: marginal.
- Novelty confidence: high.
- Reviewer attack: repeatability + consistency-regularization literature.
- Verdict: KILL — combination of two mature ingredients.

### B-0017 (PROTECTED) — Decision-theoretic thresholding for Dice — KILL
- Closest prior: RankSEG (Dai & Li, JMLR 2023) — Bayes-optimal segmentation rules for Dice/IoU.
- Existing work did: derived and implemented Bayes-optimal decision rules for Dice-type metrics, closing exactly the theory-practice gap the idea targets.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: RankSEG.
- Verdict: KILL — solved by prior work.

### B-0023 — Dual-stream global context vs distal false positives — KILL
- Closest prior: DeepMedic dual-pathway (normal-res + downsampled context; Kamnitsas et al., MedIA 2017); nnU-Net low-res→high-res cascade (Isensee et al., Nature Methods 2021).
- Existing work did: exactly the proposed architecture family (global low-res context stream + local high-res stream) as standard practice.
- Exact difference: only the distal-false-positive metric/audit is new; the remedy is a 2017 architecture.
- Remaining novelty: a small evaluation metric contribution.
- Novelty confidence: high.
- Reviewer attack: DeepMedic; nnU-Net cascade.
- Verdict: KILL — proposed fix predates the idea by nearly a decade.

### B-0027 — Repair-network for interactive 3D correction — KILL
- Closest prior: RITM (Sofiiuk et al., 2022) — iterative training with previous-mask input, clicks sampled from error regions, explicit external-mask correction mode; DeepEdit (Diaz-Pinto et al., 2022) for 3D medical.
- Existing work did: trained feedforward models on (previous mask, correction clicks) → repaired mask, including initializing from an external inaccurate mask and correcting it; 3D medical variant exists.
- Exact difference: sampling errors from a specific frozen model's failure modes and reporting clicks-to-acceptability instead of Dice.
- Remaining novelty: training-distribution tweak + metric tweak; incremental.
- Novelty confidence: high (not novel enough).
- Reviewer attack: RITM Fig. 1 (mask-correction mode); DeepEdit.
- Verdict: KILL — core mechanism published; remaining deltas are minor.

## MedFM

### B-0032 — Axis-separated medical scaling laws — KILL
- Closest prior: BioVFM-21M scaling/diversity study; data-scaling-law studies for radiology foundation models.
- Existing work did: scaling studies already separating data volume vs diversity effects in medical FM pretraining.
- Exact difference: the resolution axis is less explored, but the headline question (patients vs scans vs diversity) is being answered.
- Remaining novelty: partial (resolution axis), not enough to carry the idea.
- Novelty confidence: high.
- Reviewer attack: BioVFM-21M; radiology FM scaling-law papers.
- Verdict: KILL — actively mined territory.

### B-0035 (PROTECTED) — Train-test contamination audit — KILL
- Closest prior: contamination/leakage audits in medical imaging (WSI patient-level leakage studies; CT benchmark overlap audits; MedVLM data-leakage analyses).
- Existing work did: quantified patient- and study-level leakage across public medical benchmarks and its inflation of reported performance.
- Exact difference: broader scope only.
- Remaining novelty: incremental breadth.
- Novelty confidence: high.
- Reviewer attack: existing leakage audits.
- Verdict: KILL — audit genre already exists for this domain.

### B-0037 — Task-diversity scaling for in-context segmentation — KILL
- Closest prior: UniverSeg (Butoi et al., ICCV 2023) — trained on 53 datasets, with explicit ablations showing held-out performance scales with number/diversity of training tasks and task augmentation (+7.7 Dice); SegGPT/Painter.
- Existing work did: demonstrated that task diversity (not just volume) drives in-context generalization in medical segmentation, including dataset-count ablations.
- Exact difference: fitting a formal "task-diversity scaling law" with volume held fixed; UniverSeg's ablations already establish the qualitative claim.
- Remaining novelty: curve-fitting formalization of a demonstrated effect.
- Novelty confidence: high (core finding is published).
- Reviewer attack: UniverSeg Sec. on task quantity/diversity.
- Verdict: KILL — hypothesis already substantiated by the model the idea would need to build.

### B-0038 — Shift-type × adapter-placement law for 3D transformers — KILL
- Closest prior: Surgical fine-tuning (Lee et al., ICLR 2023) — shift-type → layer-block correspondence for classification; pathology FM adaptation benchmark (Comput Biol Med 2025) comparing linear/partial/full/LoRA placements across 20 datasets; PEFT-for-medical benchmarks.
- Existing work did: established the exact hypothesis (appearance shift → early layers, task shift → later layers) for classification; benchmarked placement variants on medical FMs.
- Exact difference: controlled factorial in dense 3D; outcome is predictable from the classification result.
- Remaining novelty: confirmatory port with low surprise value.
- Novelty confidence: high (not novel enough).
- Reviewer attack: Lee et al. 2023; medical PEFT benchmarks.
- Verdict: KILL — the "law" already exists; 3D dense is a porting exercise.

### B-0040 — Memorization/MIA in MIM medical FMs — KILL
- Closest prior: membership-inference attacks against masked image modeling (Li et al., 2024); healthcare FM memorization studies.
- Existing work did: published MIA against MIM-pretrained models; quantified memorization in medical FMs.
- Exact difference: rare-patient focus is a subgroup analysis of published attacks.
- Remaining novelty: subgroup analysis only.
- Novelty confidence: high.
- Reviewer attack: MIM-MIA papers.
- Verdict: KILL — attack class and domain both covered.

### B-0050 — Frozen dense-probing benchmark, ranking flips — KILL
- Closest prior: Benchmarking Pathology Foundation Models (Comput Biol Med 2025) — 4 FMs × 20 datasets × 5 adaptation methods with win-rate rankings incl. linear probing vs full FT vs PEFT; eva (kaiko.ai) frozen-feature pathology evaluation framework; Battle of the Backbones (NeurIPS 2023).
- Existing work did: systematically compared FM rankings across probing and fine-tuning regimes; frozen-feature evaluation harnesses exist and are used for FM leaderboards.
- Exact difference: dense (segmentation) probes rather than classification heads; ranking-flip framing.
- Remaining novelty: dense-probe variant of an existing benchmark genre.
- Novelty confidence: high (not enough).
- Reviewer attack: pathology FM benchmark; eva; BoB.
- Verdict: KILL — benchmark genre established; delta too thin.

### B-0057 — Dedup/diversity-pruning of medical pretraining corpora — KILL
- Closest prior: "Less is More" (Comput Biol Med 2024) — hash-based CT slice dedup for contrastive pretraining, 9× faster with BETTER downstream AUC; OptiDEL V-information data-effective pretraining (2024); semantic-redundancy removal for chest X-rays (Comput Med Imaging Graph 2024).
- Existing work did: exactly the proposed measurement — pruning redundant slices from medical pretraining corpora matches/exceeds full-corpus downstream performance at a fraction of cost.
- Exact difference: scale and the transferable-pruning-score claim; the redundancy discount itself is measured.
- Remaining novelty: marginal scale-up.
- Novelty confidence: high.
- Reviewer attack: Less is More; OptiDEL.
- Verdict: KILL — headline result already published, including the counterintuitive "better, not just cheaper."

### B-0058 (PROTECTED) — MoE routing as free pathology detector — KEEP
- Closest prior: V-MoE (Riquelme et al., NeurIPS 2021) routing analyses; MoE interpretability studies; AnomalyMoE / UniMMAD (2025) which *engineer* MoE for anomaly detection.
- Existing work did: analyzed what vision-MoE experts specialize in (mostly semantic/positional clustering); built supervised MoE anomaly detectors.
- Exact difference: nobody has tested whether *unsupervised* routing in a generically pretrained medical MoE FM spontaneously separates normal from pathological tissue — routing as an emergent, zero-cost abnormality signal.
- Remaining novelty: the emergent-capability question and the free-anomaly-signal evaluation protocol.
- Novelty confidence: medium (adjacent MoE-for-AD work is appearing fast; the emergence question itself unclaimed).
- Reviewer attack: AnomalyMoE ("you could have just trained the router"); V-MoE routing analyses.
- Verdict: KEEP — emergent-routing hypothesis remains open and cheap to falsify.

## AmbigSeg

### B-0061 — Smoke as alpha-matte/density regression — KILL
- Closest prior: smoke density estimation networks (W-Net line); SYN70K synthetic smoke-density dataset; dual-channel smoke density CNNs.
- Existing work did: formulated smoke as per-pixel density/opacity regression with synthetic supervision.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: SYN70K-based density regression papers.
- Verdict: KILL — the reformulation exists.

### B-0062 — Physically calibrated smoke transmittance ground truth — KEEP (absorbs B-0069 as evaluation arm)
- Closest prior: A2I2-Haze (2022) — real controlled smoke with laser transmissometer haze-density ground truth (point measurements, 625 nm) for detection/dehazing evaluation; SmokeBench (2025) paired smoke/smoke-free surveillance images; Hawkins et al. 2005-line acquisition of participating media in graphics (laser-scanned density volumes).
- Existing work did: scene-level or point-wise physical smoke measurements synchronized with imagery; paired clean/smoky captures; graphics-grade volumetric smoke scanning without a CV benchmark.
- Exact difference: no dataset provides *per-pixel transmittance maps* recovered radiometrically from calibrated patterned backgrounds, i.e., dense physically meaningful alpha ground truth usable to train and validate opacity regression, plus transfer tests to natural backgrounds.
- Remaining novelty: dense per-pixel physical GT + benchmark-validity chain (metric validated against transmissometer and human judgment — folded-in B-0069 arm).
- Novelty confidence: medium-high (verified: closest datasets stop at point measurements or unpaired masks).
- Reviewer attack: A2I2-Haze ("physical GT exists"); rebuttal: theirs is scene-level scalar density, not per-pixel maps.
- Verdict: KEEP — the dense physical-GT capture is genuinely unbuilt and unblocks the whole measurement chain.

### B-0069 — Metric-vs-human validation for fuzzy masks — MUTATE (fold into B-0062)
- Closest prior: soft/boundary metric proposals (boundary IoU etc.); no smoke-specific metric-vs-human validation found (SEARCH for direct prior FAILED).
- Existing work did: proposed fuzzy-boundary metrics without validating against human judgment or physical truth.
- Exact difference: validation study is open but too thin standalone.
- Remaining novelty: as the evaluation arm of B-0062 (validate candidate metrics against physical transmittance + human quality judgments).
- Novelty confidence: medium.
- Reviewer attack: boundary-metric papers claiming sufficiency.
- Verdict: MUTATE — merged into B-0062 as its benchmark-validity arm.

### B-0074 (PROTECTED) — Dehazing as zero-shot smoke segmenter — KILL
- Closest prior: Transmission-BVM and related transmission-guided smoke/haze segmentation using dark-channel/transmission priors.
- Existing work did: used dehazing transmission estimates directly as smoke segmentation/detection signals.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: Transmission-BVM.
- Verdict: KILL — the zero-shot bridge is published.

### B-0078 — Fire-confuser benchmark with HDR — MUTATE
- Closest prior: FIgLib + SmokeyNet wildfire benchmarks (RGB, tone-mapped); RAW/HDR-vision literature showing processed images destroy radiometric evidence; no fire-confuser RAW/HDR benchmark found (SEARCH FAILED for direct prior).
- Existing work did: RGB fire/smoke benchmarks with confuser classes; separately, RAW-domain detection showing pipeline losses.
- Exact difference: the *sensor-pipeline hypothesis* (tone-mapping destroys the radiometric evidence that separates fire from sunset/fog confusers; RAW/HDR recovers it) is untested.
- Remaining novelty: hypothesis-driven RAW/HDR fire-confuser study.
- Novelty confidence: medium.
- Reviewer attack: SmokeyNet ("confusers already benchmarked in RGB").
- Verdict: MUTATE — sharpened to the sensor-pipeline hypothesis (see mutations file).

### B-0084 — Ultrasound shadow-aware segmentation — KILL
- Closest prior: ultrasound confidence maps (Karamalis/Hellier line); shadow-aware segmentation and shadow-detection papers incl. recent MICCAI work.
- Existing work did: estimated acoustic shadow/confidence and integrated it into segmentation.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: confidence-map literature.
- Verdict: KILL — well-established.

### B-0085 — Before/during smoke pairs — KILL
- Closest prior: classical background subtraction for smoke; FIgLib temporal baselines; SmokeBench (2025) paired smoke/smoke-free frames.
- Existing work did: paired/temporal smoke data and change-based detection.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: SmokeBench; background-subtraction smoke detection.
- Verdict: KILL.

### B-0090 — Latency-vs-false-alarm smoke detection — KILL
- Closest prior: SmokeyNet/FIgLib with time-to-detect (TTD) metrics.
- Existing work did: optimized and reported latency-vs-false-alarm operating points for wildfire smoke.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: SmokeyNet.
- Verdict: KILL.

## DomShift

### B-0091 — Label-free TTA model selection — KILL
- Closest prior: On Pitfalls of Test-Time Adaptation (Zhao et al., ICLR 2023); SND selection criterion; AutoEval/label-free accuracy estimation literature.
- Existing work did: showed TTA hyperparameter/model selection without labels is the core failure mode and proposed surrogates.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: Zhao et al. 2023.
- Verdict: KILL.

### B-0093 — BN adaptation under covariate vs label shift — KILL
- Closest prior: NOTE (NeurIPS 2022), LAME (CVPR 2022), SAR (ICLR 2023), DELTA (ICLR 2023).
- Existing work did: diagnosed and fixed BN-adaptation failure under label-shift/temporal correlation — the exact conflation the idea targets.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: NOTE/LAME/DELTA.
- Verdict: KILL.

### B-0095 — Cross-site performance decomposition — KILL
- Closest prior: MRI harmonization literature; traveling-subject studies quantifying scanner vs population effects.
- Existing work did: decomposed cross-site variance with traveling phantoms/subjects and statistical harmonization.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: traveling-subject harmonization studies.
- Verdict: KILL.

### B-0096 — Shift-type → adaptation-locus law — KILL
- Closest prior: Surgical fine-tuning (Lee et al., ICLR 2023).
- Existing work did: established the shift-type → layer correspondence.
- Exact difference: redundant with B-0038 (also killed) and with Lee et al.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: Lee et al. 2023.
- Verdict: KILL.

### B-0103 — TTT auxiliary-loss coupling audit — KILL
- Closest prior: TTT (Sun et al., ICML 2020); TTT++ (Liu et al., NeurIPS 2021) analyzing when auxiliary tasks help.
- Existing work did: analyzed auxiliary-task/main-task coupling conditions for test-time training.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: TTT++.
- Verdict: KILL.

### B-0105 — Physics-derived CT kernel mappings — KILL
- Closest prior: CNN-based reconstruction-kernel conversion; sinogram-domain harmonization.
- Existing work did: learned and physics-based kernel-to-kernel image conversion for CT harmonization.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: kernel-conversion literature.
- Verdict: KILL.

### B-0107 (PROTECTED) — Streaming TTA audit (batch-size-1, online) — KILL
- Closest prior: online/continual TTA evaluations; single-image TTA studies in medical segmentation; TTA-failure analyses under realistic streams.
- Existing work did: evaluated TTA in online BS=1 and continual regimes, documenting collapse modes.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: continual-TTA evaluation papers.
- Verdict: KILL.

### B-0112 — Label-consistent convention-shift taxonomy — KEEP
- Closest prior: dataset-shift taxonomies (Quiñonero-Candela et al. 2009); Castro et al., Nature Comms 2020 (causality in medical imaging; names annotation-policy differences as a shift source); multi-rater convention variability (LIDC).
- Existing work did: named annotation/convention shift as a phenomenon; never formalized it as a distinct shift class or built a label-free detector for it.
- Exact difference: formal definition, prevalence measurement across public dataset pairs, and a label-free convention-shift detector do not exist.
- Remaining novelty: formalization + detector + prevalence audit.
- Novelty confidence: medium-high (verified absence of a direct treatment; concept is scattered in discussion sections).
- Reviewer attack: Castro et al. ("already named"); rebuttal: named ≠ formalized/measured/detectable.
- Verdict: KEEP.

## FewZero

### B-0121 (PROTECTED) — FSS foreground-bias / wrong-support counterfactual audit — KEEP
- Closest prior: Learning What Not to Segment (Lang et al., CVPR 2022) — base-class bias in FSS; foreground-prior analyses in FSS.
- Existing work did: documented base-class bias and background confusion; proposed fixes.
- Exact difference: no published *counterfactual wrong-support audit* (feed deliberately mismatched supports, measure how much of FSS accuracy survives — i.e., how much "few-shot" is actually support-independent foreground prior).
- Remaining novelty: the counterfactual protocol and its headline number.
- Novelty confidence: medium-high (searched; direct audit not found).
- Reviewer attack: Lang et al. ("bias known"); rebuttal: magnitude and support-independence never measured.
- Verdict: KEEP.

### B-0123 — Verifiably-novel-class benchmark — KILL
- Closest prior: No "Zero-Shot" Without Exponential Data (Udandarao et al., NeurIPS 2024) + Let It Wag! benchmark (290 rare concepts).
- Existing work did: showed zero-shot performance is log-linear in pretraining concept frequency — i.e., "zero-shot" is retrieval of pretrained concepts — and built the rare-concept benchmark demonstrating the drop.
- Exact difference: dense segmentation and "verifiably absent" (vs merely rare) classes.
- Remaining novelty: a dense-task port of an established finding.
- Novelty confidence: high (core claim published).
- Reviewer attack: Udandarao et al. 2024.
- Verdict: KILL — the field already has the number and the benchmark.

### B-0124 — Support-set selection variance / active support selection — KILL
- Closest prior: active/representative support-selection methods for FSS; episode-variance reporting practices.
- Existing work did: proposed selecting informative supports; documented high per-episode variance.
- Exact difference: variance-decomposition framing only.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: active support-selection papers.
- Verdict: KILL.

### B-0128 — Recognition-vs-delineation decomposition for FSS — KILL
- Closest prior: Panoptic Quality = Recognition Quality × Segmentation Quality (Kirillov et al., CVPR 2019); TIDE error decomposition (Bolya et al., ECCV 2020).
- Existing work did: the exact decomposition concept (recognition vs boundary quality) as standard metrics/toolkits in adjacent dense tasks.
- Exact difference: running PQ/TIDE-style analysis on FSS outputs.
- Remaining novelty: an analysis exercise with existing tools.
- Novelty confidence: high (not enough).
- Reviewer attack: PQ; TIDE.
- Verdict: KILL — decomposition machinery already exists; applying it is not a paper-carrying contribution.

### B-0131 — CD-FSS feature-vs-matcher attribution via swaps — KILL
- Closest prior: DATO (CVPR 2025) — names feature sensitivity and matching-process sensitivity as the two interdependent CD-FSS failure sources and fixes both; The Devil is in Low-Level Features for CD-FSS (CVPR 2025); CD-FSS benchmark (Lei et al., ECCV 2022) with layer-wise fine-tuning ablations.
- Existing work did: attributed CD-FSS failure to feature vs matching components with ablations, and built methods on that diagnosis.
- Exact difference: a cleaner 2×2 factorial; the qualitative attribution already drives current SOTA designs.
- Remaining novelty: methodological tidiness only.
- Novelty confidence: high.
- Reviewer attack: DATO; Devil-in-low-level-features.
- Verdict: KILL.

### B-0133 — Role-class (relational) few-shot segmentation — KILL
- Closest prior: affordance grounding: AGD20K (Luo et al., CVPR 2022); One-Shot Open Affordance Learning (Li et al., CVPR 2024); AffordanceLLM (2024); WorldAfford (2024).
- Existing work did: dense prediction of functional/role regions ("graspable handle", "sittable surface") across appearance-diverse objects, incl. one-shot and open-vocabulary settings; "damaged part" is covered by anomaly-detection literature.
- Exact difference: benchmark packaging; the capability class the idea claims is "unclaimed" is an active subfield.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: AGD20K + OOAL.
- Verdict: KILL — affordance grounding is this idea under another name.

### B-0143 — When does test-time fine-tuning help FSS (regime map) — KILL
- Closest prior: IFA (Nie et al., CVPR 2024) — establishes necessity of fine-tuning in CD-FSS and its overfitting risk; transductive CD-FSS fine-tuning (arXiv 2211.14745); TFI partial-fine-tuning (Lei et al., ECCV 2022, incl. layer-level ablations).
- Existing work did: answered the core question (fine-tuning helps under domain gap, overfits at low shots, parameter-subset matters) across multiple papers.
- Exact difference: a consolidated three-factor grid; the regime boundaries are qualitatively known.
- Remaining novelty: consolidation study.
- Novelty confidence: high (not enough).
- Reviewer attack: IFA; TFI.
- Verdict: KILL.

### B-0145 — Text for recognition, shots for convention — KILL
- Closest prior: CLIPSeg (Lüddecke & Ecker, CVPR 2022) — joint text+visual prompting for segmentation; kept ideas B-0112/B-0159 own the convention axis.
- Existing work did: hybrid text/visual-prompt segmentation architectures.
- Exact difference: the explicit recognition/convention division of labor is unformulated, but its substance is covered by the kept convention-shift program (B-0112 + B-0159 mutation).
- Remaining novelty: redundant within this portfolio.
- Novelty confidence: medium.
- Reviewer attack: CLIPSeg.
- Verdict: KILL — folded conceptually into B-0112/B-0159; keeping it separately would double-count one insight.

## Prompt

### B-0151 — What soft prompts encode — KILL
- Closest prior: CoOp/CoCoOp (Zhou et al., 2022) incl. nearest-word projections of learned contexts and base-class overfitting analyses; subsequent prompt-analysis papers.
- Existing work did: projected learned prompts to nearest tokens; documented dataset-specific bias and generalization failure.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: CoOp/CoCoOp.
- Verdict: KILL.

### B-0154 — Prompt-position sensitivity of promptable segmenters — KILL
- Closest prior: SAM robustness studies (stability score in SAM's own pipeline; SAM-U and prompt-perturbation uncertainty works).
- Existing work did: measured and exploited click/box perturbation sensitivity.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: SAM stability-score machinery.
- Verdict: KILL.

### B-0159 — Convention tokens — MUTATE
- Closest prior: prompt-conditioning on datasets/styles; no direct "delineation-convention token with interpolation + controlled relabeling validation" found (SEARCH FAILED for direct prior).
- Existing work did: dataset-conditioning tokens exist in generative and segmentation contexts; convention semantics untested.
- Exact difference: learning tokens that encode annotation conventions, validated by convention interpolation and controlled relabeling.
- Remaining novelty: the convention-axis conditioning + validation protocol; pairs with B-0112.
- Novelty confidence: medium.
- Reviewer attack: dataset-token conditioning papers.
- Verdict: MUTATE — sharpened scope (see mutations file).

### B-0164 — Uncertainty-eliciting prompts — KILL
- Closest prior: calibrated prompt tuning for classification.
- Existing work did: prompt-based calibration for CLIP classification.
- Exact difference: port to segmentation; too niche.
- Remaining novelty: thin.
- Novelty confidence: medium-high.
- Reviewer attack: calibrated prompt-tuning line.
- Verdict: KILL.

### B-0167 — Textual inversion for domain jargon — KILL
- Closest prior: textual-inversion-based open-vocabulary detection/segmentation (2025-2026 papers verified in earlier pass).
- Existing work did: learned pseudo-words for rare/domain concepts and used them for open-vocab dense prediction.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: textual-inversion OVD/OVS papers.
- Verdict: KILL.

### B-0177 (PROTECTED) — Validation-free prompt-overfitting detection — KILL
- Closest prior: SubPT (Ma et al., 2023) and related prompt-overfitting analyses/mitigations.
- Existing work did: characterized prompt-tuning overfitting mechanisms and proposed regularizers.
- Exact difference: validation-free detector variant; mechanism space already mapped.
- Remaining novelty: thin.
- Novelty confidence: medium-high.
- Reviewer attack: SubPT.
- Verdict: KILL.

## WSSL

### B-0182 — Pseudo-label error heritability — KILL
- Closest prior: confirmation-bias literature in self-training (GIST/RIST; ST++; FST).
- Existing work did: characterized and mitigated inherited pseudo-label errors across generations.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: ST++/FST.
- Verdict: KILL.

### B-0189 — Scribble-supervision cost curve — KILL
- Closest prior: ScribblePrompt (Wong et al., ECCV 2024) and scribble-supervision benchmarks.
- Existing work did: measured scribble-effort vs accuracy trade-offs.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: ScribblePrompt.
- Verdict: KILL.

### B-0193 — Speckle-native self-supervision for ultrasound — KEEP
- Closest prior: USCL and ultrasound contrastive pretraining; self-supervised despeckling; physics-informed ultrasound DL.
- Existing work did: generic SSL on ultrasound frames; despeckling as a *denoising target*, not a pretext signal.
- Exact difference: using speckle statistics (correlation, Rayleigh/Nakagami parameters) as the pretext task itself — pretraining that exploits rather than removes the modality's noise physics — is unpublished (searched in earlier pass; direct prior not found).
- Remaining novelty: speckle-statistics pretext family + comparison against generic SSL.
- Novelty confidence: medium (SEARCH found only adjacent work).
- Reviewer attack: despeckling-SSL papers ("speckle already used"); rebuttal: used as noise to remove, not signal to predict.
- Verdict: KEEP.

### B-0196 (PROTECTED) — Labeled-split variance in semi-supervised learning — KILL
- Closest prior: Realistic Evaluation of Deep SSL Algorithms (Oliver et al., NeurIPS 2018) and follow-up SSL-evaluation audits.
- Existing work did: demonstrated split/seed variance and evaluation pathologies in SSL benchmarking.
- Exact difference: segmentation-specific rerun.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: Oliver et al.
- Verdict: KILL.

### B-0197 — Anatomically impossible mixing augmentations — KILL
- Closest prior: Bidirectional Copy-Paste (Bai et al., CVPR 2023); CutMix ablations in medical SSL.
- Existing work did: showed anatomically impossible mixes *help* medical semi-supervised segmentation.
- Exact difference: the idea's hypothesis is already answered (in the direction opposite to its intuition).
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: BCP.
- Verdict: KILL.

### B-0201 — Co-training with genuinely independent views — KILL
- Closest prior: Blum & Mitchell 1998 (view-independence theory); Deep Co-Training (Qiao et al., ECCV 2018).
- Existing work did: theory and practice of view independence in co-training.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: co-training theory line.
- Verdict: KILL.

### B-0207 — Factorial dissection of noisy-student — KILL
- Closest prior: Noisy Student (Xie et al., CVPR 2020) ablations; UniMatch (Yang et al., CVPR 2023) for dense SSL.
- Existing work did: ablated the noise/iteration/size components; dense-task variants exist.
- Exact difference: fuller factorial only.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: original ablations.
- Verdict: KILL.

## Synth

### B-0212 — Blending-artifact shortcut in pasted/inpainted lesions — KEEP
- Closest prior: Cut, Paste and Learn (Dwibedi et al., ICCV 2017) — blending mode matters for detectors; TumorCP (MICCAI 2021); Poisson-blending mitigation papers; diffusion-inpainting lesion synthesis claiming fewer artifacts.
- Existing work did: observed qualitatively that blending artifacts affect learning and proposed smoother compositing.
- Exact difference: no published *quantitative law* linking artifact detectability (by a probe classifier) to the synthetic→real transfer gap, nor an artifact-detectability audit of current medical lesion-synthesis pipelines.
- Remaining novelty: detectability→transfer-gap curve + audit + artifact-hardened compositing recipe.
- Novelty confidence: medium-high (verified: mitigation exists, measurement does not).
- Reviewer attack: Dwibedi et al. ("blending known to matter"); rebuttal: known ≠ quantified as a predictive law.
- Verdict: KEEP.

### B-0213 — Real-synthetic exchange rate — KILL
- Closest prior: Scaling Laws of Synthetic Images (Fan et al., CVPR 2024); Beyond Real Data: Synthetic Data through the Lens of Regularization (2025, incl. segmentation experiments and optimal synthetic-to-real ratios); LLM synthetic-data scaling studies (EMNLP 2025); mixing-ratio studies across scales (2025).
- Existing work did: measured marginal value of synthetic vs real samples, diminishing returns, optimal mixing ratios, and scale dependence — the exchange-rate question in several guises.
- Exact difference: dense-task-specific exchange-rate table + proxy prediction; the concept and headline findings are published.
- Remaining novelty: incremental consolidation.
- Novelty confidence: high (crowded).
- Reviewer attack: Fan et al.; Beyond Real Data.
- Verdict: KILL.

### B-0214 — Utility-predictive metric for synthetic dense-task data — KILL
- Closest prior: Training-Free Metrics for Synthetic Object Detection Data (CCDM, 2026); SDQM (synthetic dataset quality metric for detection); Do Generative Metrics Predict YOLO Performance? (2026); Benchmarking Data-Quality Metrics vs Human Judgment vs Land-Cover Segmentation Performance (2026).
- Existing work did: exactly the proposed program — showed FID fails to predict downstream dense-task utility and built/validated task-anchored composite metrics correlated with mAP/F1, including a segmentation case.
- Exact difference: marginal (metric variants).
- Remaining novelty: none load-bearing.
- Novelty confidence: high.
- Reviewer attack: CCDM; SDQM.
- Verdict: KILL — the race is already being run.

### B-0222 — Thin-structure fidelity floor of latent diffusion — KEEP
- Closest prior: MedVAE (2025) and analyses of VAE/latent compression losing fine detail; frequency-aware autoencoders (FA-VAE); qualitative complaints about thin-structure loss in LDM-generated medical images.
- Existing work did: documented that latent compression degrades fine details and proposed better autoencoders.
- Exact difference: no *quantified fidelity floor* as a function of structure width/latent downsampling, and no measurement of the downstream segmentation-training penalty attributable to that floor (pixel- vs latent-space generation, matched compute).
- Remaining novelty: the floor curve + downstream causal test + practical when-to-use-pixel-space rule.
- Novelty confidence: medium-high.
- Reviewer attack: MedVAE ("compression loss known"); rebuttal: known qualitatively, never measured as a floor with downstream consequences.
- Verdict: KEEP.

### B-0223 — When can synthetic validation be trusted — KILL
- Closest prior: Synthetic Data for Model Selection (Shoshan et al., ICML 2023) — rank-preservation measurement + theory (Spearman vs total-variation bound); Efficacy of Synthetic Data as a Benchmark (2024, NLP).
- Existing work did: directly measured whether synthetic validation preserves model rankings, when it fails, and tied it to generator quality.
- Exact difference: dense-prediction rerun with decision-granularity breakdown.
- Remaining novelty: a port.
- Novelty confidence: high (core question answered).
- Reviewer attack: Shoshan et al.
- Verdict: KILL.

### B-0230 (PROTECTED) — Label-cleanliness vs image-distribution decomposition — KEEP
- Closest prior: SENSE / What Makes Synthetic Data Effective in Image Segmentation (2026) — notes generative labels are NOT clean (generative instability) and fixes assignment; Beyond Real Data (2025); EO data-quality benchmark (2026).
- Existing work did: studied synthetic-real gaps and label-noise handling separately; nobody ran the confound-breaking experiment (inject human-matched label noise into synthetic labels; clean real labels) to price label perfection.
- Exact difference: the decomposition experiment itself is unrun in any domain we could find (SEARCH for direct prior FAILED).
- Remaining novelty: the decomposition design + investment guidance (generation vs annotation QC).
- Novelty confidence: medium-high.
- Reviewer attack: SENSE ("synthetic labels aren't clean anyway"); rebuttal: that strengthens the need to measure the label-quality axis explicitly, and rendered/simulated pipelines DO have clean labels.
- Verdict: KEEP.

### B-0235 — Generator blind-spot maps — KILL
- Closest prior: Seeing What a GAN Cannot Generate (Bau et al., ICCV 2019).
- Existing work did: systematically mapped what generators omit.
- Exact difference: modern-generator rerun + data-collection guidance.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: Bau et al.
- Verdict: KILL.

## AnnotEff

### B-0241 — Cost-honest active-learning benchmark — KILL
- Closest prior: Parting with Illusions about Deep Active Learning (Mittal et al.); Towards Robust and Reproducible Active Learning (Munjal et al., CVPR 2022).
- Existing work did: exposed AL evaluation pathologies incl. cost accounting and baseline strength.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: Mittal/Munjal.
- Verdict: KILL.

### B-0244 — Automation bias in model-assisted annotation — KILL
- Closest prior: OSAIRIS hospital deployment study (Clinical Oncology 2025) — "mystery shopping" experiment with deliberately planted auto-contour errors, measuring clinician catch rates (72-88%); RCR Auto-contouring in Radiotherapy guidance (2024) on automation/anchoring bias; JACMP 2025 prostate AI-contouring automation-bias study.
- Existing work did: the exact planted-error inheritance measurement the idea proposes, plus clinical guidance on blind-review mitigation.
- Exact difference: scale and crossover design only.
- Remaining novelty: incremental replication.
- Novelty confidence: high.
- Reviewer attack: OSAIRIS.
- Verdict: KILL — minimal experiment already run in a hospital. (Its measured anchoring rates become calibration input for the B-0366 mutation.)

### B-0247 — STAPLE under correlated rater biases — KILL
- Closest prior: correlated-annotator fusion models in crowdsourcing literature (beyond independent-rater Dawid-Skene/STAPLE assumptions).
- Existing work did: modeled rater correlation in label aggregation.
- Exact difference: segmentation-specific port.
- Remaining novelty: thin.
- Novelty confidence: medium-high.
- Reviewer attack: correlated crowdsourcing models.
- Verdict: KILL.

### B-0255 — Simulated vs real users in interactive segmentation — KILL
- Cross-cluster duplicate of A-0211 (kept in Cluster A's pipeline).
- Verdict: KILL — dedup.

### B-0261 — Micro-verification as supervision channel — KILL
- Closest prior: We Don't Need No Bounding-Boxes (Papadopoulos et al., CVPR 2016) — training detectors from yes/no human verification only, 6-9× cheaper, near-fully-supervised quality.
- Existing work did: established binary verification as a primary supervision channel with iterative retraining.
- Exact difference: boundary-segment questions + IRT aggregation is a port to segmentation.
- Remaining novelty: porting exercise.
- Novelty confidence: high (not enough).
- Reviewer attack: Papadopoulos et al.
- Verdict: KILL.

### B-0269 — Guideline wording as experimental variable — KILL
- Closest prior: Don't Blame the Annotator: Bias Already Starts in the Annotation Instructions (Parmar et al., EACL 2023); FIND-RESOLVE-LABEL guideline-clarification workflow (2021).
- Existing work did: demonstrated instruction bias systematically shifts collected labels and model conclusions (NLP); built guideline-refinement workflows.
- Exact difference: dense-label variance decomposition; the phenomenon and its measurement paradigm are published.
- Remaining novelty: domain port.
- Novelty confidence: medium-high (port only).
- Reviewer attack: Parmar et al.
- Verdict: KILL.

## LongTail

### B-0271 — Three-axis imbalance decomposition — KILL
- Closest prior: The Devil is in Classification (Wang et al., ECCV 2020) — already reports LVIS results on BOTH image-centric bins (APr/c/f) and instance-centric bins (AP1-4), explicitly noting the axes diverge (e.g., "rare" classes with hundreds of instances); Seesaw Loss; small-object (pixel-area) segmentation literature.
- Existing work did: separated image-frequency from instance-count in evaluation; area imbalance handled by its own literature.
- Exact difference: controlled axis-isolated dataset construction + remedy-prediction validation remain unrun, but two of three axes are already distinguished in print.
- Remaining novelty: partial; not enough against the quota.
- Novelty confidence: medium (the isolation experiment is open, the conceptual distinction is not).
- Reviewer attack: Devil-in-Classification Table 1.
- Verdict: KILL — the distinction is published; remaining delta is a controlled rerun.

### B-0272 (PROTECTED) — Crop-level rebalancing — KILL
- Closest prior: proposal/crop-level resampling (bi-level sampling in SimCal, ECCV 2020) and pixel-exposure balancing techniques.
- Existing work did: rebalanced below image level (proposal/object level) exactly as proposed.
- Exact difference: exposure audit framing only.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: SimCal bi-level sampling.
- Verdict: KILL.

### B-0274 — Statistical power in long-tail benchmarks — KILL
- Cross-cluster duplicate of C-0293.
- Verdict: KILL — dedup.

### B-0275 — Decoupled training for dense long-tail — KILL
- Closest prior: Decoupling representation and classifier (Kang et al., ICLR 2020); BAGS (Li et al., CVPR 2020) porting decoupling to detection/instance segmentation.
- Existing work did: ported decoupled training to dense prediction.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: BAGS.
- Verdict: KILL.

### B-0285 — Rare anatomical variants as long-tail benchmark — KEEP
- Closest prior: MOOD medical out-of-distribution challenge (Zimmerer et al.); case-report literature on anatomical variants; long-tail medical classification benchmarks.
- Existing work did: medical OOD/anomaly benchmarks target pathology or synthetic corruptions, not named anatomical variants (situs inversus, accessory organs, vessel-branching variants) as a curated segmentation long tail.
- Exact difference: no benchmark measures segmentation robustness across cataloged anatomical variants with per-variant frequency annotations (searched in earlier pass; direct prior not found).
- Remaining novelty: variant-stratified benchmark + failure taxonomy.
- Novelty confidence: medium.
- Reviewer attack: MOOD ("OOD already benchmarked"); rebuttal: variants are in-distribution humans, not OOD artifacts — distinct failure class.
- Verdict: KEEP.

### B-0292 — Compositional long-tail dense prediction — KILL
- Closest prior: compositional zero-shot learning literature; PACO parts-and-attributes dense benchmark (Ramanathan et al., CVPR 2023).
- Existing work did: dense part/attribute composition benchmarks.
- Exact difference: none material.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: PACO.
- Verdict: KILL.

## CrossDom

### B-0302 — 2D→3D weight-inflation science — KILL
- Closest prior: I3D inflation (Carreira & Zisserman, CVPR 2017); ACS convolutions (Yang et al., 2021); Med3D and 2D-to-3D transfer studies.
- Existing work did: established and analyzed 2D→3D transfer mechanisms.
- Exact difference: fuller factorial only.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: ACS convolutions.
- Verdict: KILL.

### B-0306 — Histopathology scanner-gap decomposition — KILL
- Closest prior: stain-normalization literature; multi-scanner variation studies in computational pathology.
- Existing work did: decomposed and mitigated scanner/stain variation.
- Exact difference: none material.
- Remaining novelty: none.
- Novelty confidence: high.
- Reviewer attack: stain/scanner studies.
- Verdict: KILL.

### B-0313 — Transferability oracle for dense tasks — KILL
- Closest prior: Transferability Estimation for Semantic Segmentation Task (arXiv 2109.15242, OTCE-seg via pixel sampling); Efficient Prediction of Model Transferability in Semantic Segmentation Tasks (ICIP 2023; 0.718 Spearman vs realized transfer, 67× cheaper); LogME/LEEP/H-score for classification.
- Existing work did: extended transferability metrics to segmentation and validated correlation with realized transfer across dataset pairs.
- Exact difference: larger pair set + region/boundary dual outcomes; core capability exists.
- Remaining novelty: benchmark enlargement.
- Novelty confidence: high (not enough).
- Reviewer attack: ICIP 2023 paper.
- Verdict: KILL.

### B-0319 — Anomaly-segmentation universality (industrial ↔ medical) — KILL
- Closest prior: AnomalyCLIP (Zhou et al., ICLR 2024) — trained on industrial MVTec AD, zero-shot generalizes to 17 datasets spanning industrial AND medical (brain MRI, skin, colon); AdaptCLIP (2025); MVFA (CVPR 2024, industrial→medical AD adaptation); ACD-CLIP (2025); BMAD benchmark.
- Existing work did: demonstrated exactly the shared "deviation-from-normality" core transferring between industrial and medical domains, repeatedly.
- Exact difference: joint-training shared/specific ablation; the universality hypothesis is already substantially confirmed.
- Remaining novelty: an ablation on a confirmed hypothesis.
- Novelty confidence: high.
- Reviewer attack: AnomalyCLIP.
- Verdict: KILL.

### B-0327 — Universal-model audit & cartography — KILL
- Closest prior: SAM out-of-domain performance audits ("Segment Anything Is Not Always Perfect" and the medical/camouflage/etc. evaluation wave).
- Existing work did: mapped where SAM-class models fail across dozens of domains.
- Exact difference: cartography packaging.
- Remaining novelty: thin.
- Novelty confidence: high.
- Reviewer attack: SAM audit wave.
- Verdict: KILL.

### B-0328 — Annotation-vs-distance law for porting — KILL
- Closest prior: label-budget/fine-tuning-curve studies for cross-domain transfer.
- Existing work did: measured labels-needed vs domain-gap trade-offs.
- Exact difference: none material.
- Remaining novelty: thin.
- Novelty confidence: medium-high.
- Reviewer attack: budget-curve studies.
- Verdict: KILL.

## VLM / Multimodal / Meta

### B-0331 — Negation mining as spatial negative supervision — KEEP
- Closest prior: CheXpert labeler (Irvin et al., AAAI 2019) — negation extraction from reports for classification labels; RadGraph relation extraction; report-supervised segmentation works using positive findings.
- Existing work did: extracted negations for image-level labels; used reports for positive localization supervision.
- Exact difference: converting report negations ("no pleural effusion") into *spatial* negative supervision via atlas/anatomy grounding for segmentation training is unpublished (searched in earlier pass; direct prior not found).
- Remaining novelty: negation→region grounding pipeline + negative-supervision training objective.
- Novelty confidence: medium-high.
- Reviewer attack: CheXpert ("negation mining exists"); rebuttal: image-level vs spatially grounded supervision.
- Verdict: KEEP.

### B-0344 — Radiotherapy dose maps as segmentation supervision — KEEP
- Closest prior: OpenKBP (Babier et al., 2021) and dose-prediction networks (contours → dose).
- Existing work did: learned the forward mapping (anatomy+contours → dose); dose data exists at scale in clinical archives.
- Exact difference: inverting the channel — using delivered/planned dose maps as weak supervision to recover target/OAR contours — is unpublished (searched in earlier pass; direct prior not found).
- Remaining novelty: the inverse-supervision formulation and its identifiability analysis.
- Novelty confidence: medium (physics/planning constraints may make inversion ill-posed; that risk is stated in the idea).
- Reviewer attack: OpenKBP ("mapping known"); rebuttal: forward ≠ inverse, and nobody trains segmenters from dose.
- Verdict: KEEP.

### B-0350 — Suggestion-induced hallucination in medical segmentation — KEEP
- Closest prior: POPE (Li et al., EMNLP 2023) object-hallucination probing; CARES (NeurIPS 2024) medical VLM trustworthiness incl. sycophancy-style failures; VLM leading-question studies.
- Existing work did: measured hallucination/sycophancy for classification/VQA; medical trustworthiness benchmarks exist without a segmentation/grounding arm.
- Exact difference: suggestion-injection protocol for *segmentation* ("segment the tumor" when none exists; measure conjured masks) plus mitigation via negative supervision (links to B-0331) is unpublished (searched in earlier pass).
- Remaining novelty: segmentation-grounded suggestion-hallucination benchmark + mitigation.
- Novelty confidence: medium-high.
- Reviewer attack: CARES ("medical sycophancy measured"); rebuttal: VQA-level, not dense/grounded.
- Verdict: KEEP.

### B-0353 (PROTECTED) — Doppler audio as vessel supervision — KEEP
- Closest prior: AVSBench audio-visual segmentation (Zhou et al., ECCV 2022); ML on Doppler spectrograms for diagnosis; no work pairing Doppler audio with B-mode imagery as segmentation supervision found (SEARCH FAILED for direct prior — treated as genuine gap, high risk).
- Existing work did: audio-visual segmentation in natural video; Doppler signal classification.
- Exact difference: using the physically-coupled Doppler audio stream as free spatial supervision for vessel segmentation is untouched.
- Remaining novelty: entire formulation.
- Novelty confidence: medium (novelty high, feasibility risk high — data pairing is the bottleneck).
- Reviewer attack: AVSBench ("audio-visual seg exists"); rebuttal: natural-scene sound ≠ physiologically coupled Doppler.
- Verdict: KEEP — high-risk/high-novelty slot.

### B-0360 — Grounding-capability taxonomy for medical VLMs — KILL
- Closest prior: medical VLM grounding evaluations; overlaps kept entries B-0350/B-0331.
- Verdict: KILL — redundant within portfolio; taxonomy alone is survey-grade.

### B-0361 — Ambiguity handling as transferable skill — KEEP
- Closest prior: probabilistic segmentation (Prob U-Net line); cross-domain calibration/uncertainty-transfer studies for classification; no direct test of whether ambiguity-handling transfers across dense domains found (SEARCH FAILED for direct prior).
- Existing work did: modeled ambiguity within domains; studied calibration transfer for classifiers.
- Exact difference: hypothesis that ambiguity-handling machinery (not features) transfers across unrelated dense domains is untested.
- Remaining novelty: cross-domain ambiguity-transfer experiment design.
- Novelty confidence: medium-low (search failure may reflect terminology mismatch; flagged honestly).
- Reviewer attack: Prob U-Net line ("just fine-tune it").
- Verdict: KEEP — cheap decisive experiment; genuine open question as far as we could verify.

### B-0362 — Metric-decision correlation — MUTATE
- Closest prior: Metrics Reloaded (Maier-Hein et al., Nature Methods 2024); metric-pitfall literature.
- Existing work did: cataloged metric pitfalls and selection guidance; did not measure how often *published SOTA deltas* flip decisions under alternative legitimate metric/decision-rule families.
- Exact difference: decision-flip-rate audit of published results.
- Remaining novelty: the flip-rate audit.
- Novelty confidence: medium-high.
- Reviewer attack: Metrics Reloaded ("guidance exists").
- Verdict: MUTATE — sharpened to the flip-rate audit (see mutations file).

### B-0366 — Multi-generation annotation-ecosystem simulation — MUTATE
- Closest prior: model-collapse literature (Shumailov et al., Nature 2024) for generative self-consumption; OSAIRIS (2025) provides empirically measured human anchoring/catch rates.
- Existing work did: collapse dynamics for generative loops WITHOUT humans; single-generation automation-bias measurements.
- Exact difference: multi-generation dynamics of the human-verified annotation flywheel (model → assisted labels → retrained model), with anchoring rates calibrated from published measurements, is unmodeled.
- Remaining novelty: the calibrated ecosystem simulation + intervention analysis (blind-case ratios needed to prevent drift).
- Novelty confidence: medium-high.
- Reviewer attack: Shumailov et al. ("collapse known"); rebuttal: human-in-the-loop correction changes the dynamics qualitatively — that is the object of study.
- Verdict: MUTATE — reframed around calibrated human-in-the-loop collapse dynamics (see mutations file).

---

## Cross-check against Cluster A / C survivors
- B-0255 killed as duplicate of A-0211 (simulated vs real interactive users).
- B-0274 killed as duplicate of C-0293 (statistical power in benchmarks).
- B-0362 mutation scoped to *published-delta flip rates* to avoid overlap with C-cluster metric-guidance entries.
- B-0366 mutation scoped to annotation-ecosystem (human-verified) dynamics, distinct from A-0272's generative-only collapse angle.
