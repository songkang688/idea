# Stage 3 — Adversarial Prior-Art Killsheet, Attack Set 2

**Role:** adversarial prior-art researcher. Default assumption: the idea is already published.
**Sources attacked:** survivor texts from `stage2-batch-a-review-a57f`, `stage2-batch-b-review-f04c`, `stage2-batch-c-review-0cdb`, `stage2-ab-merge-80a1`, plus the 12 auditor revives from `stage2-meta-audit-dbae`.
**Attack set:** 44 listed ids + 12 auditor revives = **56 ideas**.
**Method:** targeted literature search per idea (arXiv, CVPR/ICCV/ECCV/NeurIPS/MICCAI open access, journals). Every citation below was verified against a live source during this pass. No invented citations; where a recalled paper could not be re-verified with a URL, it was dropped or cited by title+venue only and the verdict weakened accordingly.

**Verdict key:** KILL = core claim already published; MUTATE = phenomenon/tooling published, a stated delta survives — reposition required; KEEP = no blocking prior found.

## Scoreboard

| Verdict | Count |
|---|---|
| KILL | 17 |
| MUTATE | 38 |
| KEEP | 1 |
| **Total** | **56** |

Kills: A-0118, A-0301, A-0313, A-0328, A-0336, B-0064, B-0081, B-0121, B-0129, B-0132, B-0177, B-0223, C-0072, C-0149, C-0249, C-0261, C-0332.
Keep: C-0206.

---

## Batch A

### A-0041 — Does chain-of-thought causally change grounding?
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [LISA: Reasoning Segmentation via Large Language Model (arXiv 2308.00692)](https://arxiv.org/abs/2308.00692) — defined reasoning segmentation and the reasoning→mask pipeline. [CoReS: Orchestrating the Dance of Reasoning and Segmentation (ECCV 2024, arXiv 2404.05673)](https://arxiv.org/abs/2404.05673) — chains-of-reasoning explicitly steering segmentation. [Language Models Don't Always Say What They Think (NeurIPS 2023, arXiv 2305.04388)](https://arxiv.org/abs/2305.04388) — showed CoT explanations are systematically unfaithful to the actual computation, with intervention methodology.
- **What they did:** built reasoning-segmentation systems and, separately, established CoT unfaithfulness for text tasks via perturbation/bias interventions.
- **Exact difference:** nobody has run the faithfulness interventions with the *mask* as the dependent variable — editing/corrupting the emitted rationale and measuring whether the segmentation changes.
- **Remaining novelty:** causal faithfulness test for reasoning segmentation (rationale-swap, rationale-ablation, counterfactual-rationale → ΔIoU); a "decorative CoT" result would undercut LISA-style claims.
- **Mutation:** frame strictly as CoT-faithfulness-for-dense-output, importing the Turpin intervention toolkit; report per-model decorativeness scores.

### A-0058 — LoRA amplifies spurious correlations
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [LoRA Users Beware: A Few Spurious Tokens Can Manipulate Your Finetuned Model (arXiv 2506.11402)](https://arxiv.org/abs/2506.11402) — LoRA latches onto injected spurious tokens; reliance is proportional to rank under light injection and *non-monotonic* overall. [LoRA vs Full Fine-tuning: An Illusion of Equivalence (arXiv 2410.21228)](https://arxiv.org/abs/2410.21228) — LoRA introduces "intruder dimensions" absent in full fine-tuning.
- **What they did:** established that PEFT encourages shortcut solutions in LLMs, including the rank dependence this idea predicted.
- **Exact difference:** all evidence is text classification with *injected* tokens; no study of naturally occurring visual spurious cues (co-occurrence, texture, position) in dense prediction, and no LoRA-vs-full comparison on segmentation shortcut reliance.
- **Remaining novelty:** the vision/segmentation instantiation with natural confounds and worst-group mask metrics; whether the SSTI rank non-monotonicity transfers to visual shortcuts.
- **Mutation:** position as the dense-vision replication/extension of SSTI: natural spurious cues, rank sweep, worst-group IoU, LoRA vs full FT vs linear probing.

### A-0067 — One dial: the encoder/decoder LR ratio
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [ULMFiT: Universal Language Model Fine-tuning (arXiv 1801.06146)](https://arxiv.org/abs/1801.06146) — discriminative (per-layer) learning rates as a core fine-tuning tool. [Revisiting Few-sample BERT Fine-tuning (arXiv 2006.05987)](https://arxiv.org/abs/2006.05987) — layer-wise LR decay and re-initialization effects studied systematically. [Surgical Fine-Tuning Improves Adaptation to Distribution Shifts (ICLR 2023, arXiv 2210.11466)](https://arxiv.org/abs/2210.11466) — which blocks to tune depends on shift type.
- **What they did:** established layer-dependent learning rates and block-selective tuning as first-class fine-tuning dials.
- **Exact difference:** no controlled study isolating the *single* encoder:decoder LR ratio for pretrained-encoder segmentation, mapping the ratio→outcome curve across data scales and shift types, or showing it subsumes freeze/full-FT as endpoints.
- **Remaining novelty:** the one-dial claim (freeze and full-FT as limits of one hyperparameter), the ratio-vs-dataset-size law, and a default recommendation for the field.
- **Mutation:** frame as "the missing fine-tuning law": ratio sweep × data scale × shift type, with ULMFiT/surgical-FT as the baselines it unifies.

### A-0089 — Forgetting hysteresis: suppression, not erasure
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs (arXiv 2505.16831)](https://arxiv.org/abs/2505.16831) — showed "forgotten" behavior is often suppressed not erased; minimal relearning restores it; introduced representation-level reversibility diagnostics (PCA/CKA/Fisher).
- **What they did:** systematized suppression-vs-erasure and relearning-based probes for LLM unlearning.
- **Exact difference:** their setting is deliberate unlearning in LLMs; A-0089 concerns *incidental* domain forgetting during vision fine-tuning, and proposes hysteresis loops (forget→relearn cycles, path dependence, loop area) as the quantitative signature for dense models.
- **Remaining novelty:** hysteresis-loop formalization for catastrophic forgetting in segmentation; whether relearning cost predicts representational erasure in vision encoders.
- **Mutation:** port the reversibility toolkit to vision fine-tuning; headline metric = loop area (relearn epochs vs forget epochs) across PEFT/full-FT.

### A-0118 — Models hallucinate surgically removed organs
**Verdict: KILL** (confidence: high)
- **Kill cite:** [HALOS: Hallucination-free Organ Segmentation after Organ Resection Surgery (IPMI 2023, arXiv 2303.07717)](https://arxiv.org/abs/2303.07717).
- **What they did:** documented exactly this failure — segmentation models predicting organs that were surgically resected — on post-nephrectomy/splenectomy cohorts, and built a classifier-conditioned model to fix it.
- **Exact difference:** essentially none on the core observation and the safety framing; only broader model coverage (SAM-era FMs) would be new.
- **Remaining novelty:** marginal — a wider audit of *foundation* models on resection cohorts.
- **Confidence:** high.

### A-0123 — Fire segmenters are color detectors
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [Fire detection in video sequences using a generic color model (Çelik & Demirel, Fire Safety Journal 2009)](https://doi.org/10.1016/j.firesaf.2008.05.005) — canonical color-rule fire detection (YCbCr rules, up to 99% detection, explicitly tested against fire-like colored regions); color as the dominant cue is baked into the field, and CNN-era fire detectors inherit red-object false alarms.
- **What they did:** built color-centric detectors and observed fire-colored false alarms anecdotally.
- **Exact difference:** no controlled *causal* hue-intervention study on modern fire segmentation models (rotate hue of fire/non-fire regions, measure mask response), no decomposition of color vs texture vs temporal contribution.
- **Remaining novelty:** the intervention protocol and a quantified "color dependence index" for deployed fire segmenters; counterfactual training fix.
- **Mutation:** run hue/saturation interventions and gray-world counterfactuals on public fire-seg checkpoints; report causal color reliance and its correlation with false-alarm rates on fire-colored distractors.

### A-0125 — Turbulence spectra as a label-free smoke signal
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Wavelet based real-time smoke detection in video (Töreyin, Dedeoğlu & Çetin, EUSIPCO 2005)](https://www.eurasip.org/Proceedings/Eusipco/Eusipco2005/defevent/papers/cr1133.pdf) and [Contour based smoke detection in video using wavelets (EUSIPCO 2006)](https://www.eurasip.org/Proceedings/Eusipco/Eusipco2006/papers/1568987463.pdf) — high-frequency wavelet/flicker temporal signatures of smoke (incl. HMM-modeled boundary flicker) used for detection; the classical smoke-video literature routinely exploits turbulence statistics.
- **What they did:** hand-crafted spectral/temporal features distinguishing smoke's turbulent dynamics from rigid motion.
- **Exact difference:** classical works used ad-hoc wavelet energies, not Kolmogorov-style turbulence spectra as a *physics-anchored, label-free training signal* for modern segmenters; no self-supervision from spectral slope constraints exists.
- **Remaining novelty:** physics-derived spectral prior as an auxiliary loss / pseudo-label source; test whether it reduces labeled-data needs and false alarms on non-turbulent look-alikes.
- **Mutation:** position against the wavelet-era baselines explicitly; claim = turbulence-spectrum consistency as self-supervision, evaluated on label-scarce smoke segmentation.

### A-0154 — Camouflage failure: attentional or perceptual?
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Can SAM Segment Anything? When SAM Meets Camouflaged Object Detection (arXiv 2304.04709)](https://arxiv.org/abs/2304.04709) — documented SAM's poor COD performance. [SAM-Adapter: Adapting SAM in Underperformed Scenes (arXiv 2304.09148)](https://arxiv.org/abs/2304.09148) — adapters fix much of the COD gap.
- **What they did:** established the failure and engineering remedies.
- **Exact difference:** neither decomposes the failure into *attentional* (can't find it: everything-mode misses object) vs *perceptual* (can't delineate it: oracle-point prompt still yields bad mask) components.
- **Remaining novelty:** the oracle-prompt decomposition protocol and its verdict on where camouflage breaks promptable models; implications differ (prompt-generation vs representation fixes).
- **Mutation:** run everything-mode vs oracle-click vs oracle-box on COD10K across SAM/SAM2/HQ-SAM; publish the attentional:perceptual failure ratio per dataset.

### A-0161 — The patch-quantization floor: decoder-invariance test
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Subobject-level Image Tokenization (arXiv 2402.14327)](https://arxiv.org/abs/2402.14327) — adaptive segment-based tokenization replacing fixed patches. [Phase Marginalization for Patch-Grid Instability in Vision Transformers (arXiv 2606.08132)](https://arxiv.org/abs/2606.08132) — patch grid formalized as a nuisance for dense prediction.
- **What they did:** built alternatives to fixed patchification and showed grid-phase effects on dense outputs.
- **Exact difference:** no one has measured a *decoder-invariant floor*: showing boundary error saturates identically across decoder capacities, isolating the tokenizer as the binding constraint.
- **Remaining novelty:** the invariance experiment (sweep decoder capacity at fixed ViT tokenization; floor persists) and the resulting quantization law vs patch size.
- **Mutation:** publish the floor curve (boundary F-score vs patch size, invariant to decoder), positioned as the causal complement to subobject tokenization.

### A-0176 — Benchmark JPEG already deleted the small objects
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [First Gradually, Then Suddenly: Understanding the Impact of Image Compression on Object Detection (Sensors 2022)](https://doi.org/10.3390/s22031104) — AP-small declines steepest under JPEG; small objects most affected. [Lost in Compression (CVPRW 2022, arXiv 2205.08002)](https://arxiv.org/abs/2205.08002) — tiny/small objects most compression-sensitive; retraining on compressed data partially recovers.
- **What they did:** quantified compression→detection degradation as a function of object size, at inference and training time.
- **Exact difference:** both treat compression as a *deployment* variable; neither audits benchmark *construction* — i.e., that canonical datasets were JPEG'd before annotation, so small-object ground truth and the reachable ceiling are already corrupted.
- **Remaining novelty:** forensic audit of benchmark provenance (quantization tables, artifact energy at annotation scale), estimate of the information ceiling benchmarks impose on small-object methods.
- **Mutation:** shift claim from "JPEG hurts detection" (published) to "JPEG is an unacknowledged benchmark-construction confounder"; validate on raw-capture control data.

### A-0313 — Resolution beats small-object architecture remedies
**Verdict: KILL** (confidence: medium-high)
- **Kill cite:** [An Analysis of Scale Invariance in Object Detection — SNIP (CVPR 2018, arXiv 1711.08189)](https://arxiv.org/abs/1711.08189) plus [Slicing Aided Hyper Inference — SAHI (arXiv 2202.06934)](https://arxiv.org/abs/2202.06934).
- **What they did:** SNIP showed scale/resolution handling dominates small-object accuracy and that training at the right scale beats architectural tweaks; SAHI showed generic resolution-effective slicing yields large small-object gains across detectors without architecture change. The compression literature above shows the same monotone resolution/detail dependence.
- **Exact difference:** the survivor's framing ("controlled budget-matched comparison: upscaling vs dedicated small-object modules") is a cleaner experiment, but the field's conclusion — effective resolution is the dominant factor and simple scale remedies beat bespoke modules — is already established and widely replicated.
- **Remaining novelty:** only the compute-matched bookkeeping; a survey-grade contribution, not a discovery.
- **Confidence:** medium-high.

### A-0336 — Human floors and ceilings for segmentation benchmarks
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Panoptic Segmentation (Kirillov et al., CVPR 2019, arXiv 1801.00868)](https://arxiv.org/abs/1801.00868) plus [Why rankings of biomedical image analysis competitions should be interpreted with care (Nature Communications 2018)](https://www.nature.com/articles/s41467-018-07619-7).
- **What they did:** Kirillov et al. measured *human consistency* on the panoptic benchmarks (human-vs-human PQ on Cityscapes/ADE20k/Vistas) and compared machines against it — precisely the human floor/ceiling protocol; Maier-Hein et al. showed benchmark rankings are dominated by annotation/design noise.
- **Exact difference:** extending the same protocol to more segmentation benchmarks is coverage, not a new question.
- **Remaining novelty:** marginal (breadth only).
- **Confidence:** high.

### R1 / A-0278 — Mask-MAE prior from unpaired mask archives *(auditor revive)*
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [Anatomically Constrained Neural Networks — ACNN (arXiv 1705.08302)](https://arxiv.org/abs/1705.08302) — learned shape priors (mask autoencoders) regularizing segmentation. [Anatomical Priors for Image Segmentation via Post-Processing with Denoising Autoencoders (MICCAI 2019, arXiv 1906.02343)](https://arxiv.org/abs/1906.02343) — Post-DAE line: DAEs trained on *unpaired* masks fix implausible predictions post hoc.
- **What they did:** trained autoencoder priors on segmentation-mask corpora and used them as regularizers/post-processors, including from unpaired masks.
- **Exact difference:** existing priors are single-anatomy, small-scale, task-specific; no *foundation-style* masked-autoencoder pretrained across pooled heterogeneous mask archives (multi-organ, multi-domain, natural+medical), and no test of the structured-vs-unstructured interaction hypothesis (which downstream tasks benefit).
- **Remaining novelty:** scale + cross-domain pooling + the falsifiable claim that mask-space statistics transfer across anatomies/domains; enabling hypothesis independently testable (auditor's revive rationale holds).
- **Mutation:** explicitly position as "foundation prior in label space" vs ACNN/Post-DAE baselines; ablate pooled vs per-domain pretraining.

### R4 / A-0052 — Bias-variance decomposition of PEFT vs full fine-tuning *(auditor revive)*
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [LoRA vs Full Fine-tuning: An Illusion of Equivalence (arXiv 2410.21228)](https://arxiv.org/abs/2410.21228) — structural differences between LoRA and full-FT solutions. [LoRA Learns Less and Forgets Less (arXiv 2405.09673)](https://arxiv.org/abs/2405.09673) — LoRA as a stronger regularizer: lower target-domain gains, lower forgetting.
- **What they did:** characterized LoRA's constraint qualitatively (learns-less/forgets-less; intruder dimensions) — implicitly a bias-variance story, never measured as one.
- **Exact difference:** no seed-level bias-variance *decomposition* (variance over seeds/data resamples vs systematic bias) for PEFT vs full FT, no crossover-point estimation vs dataset size, nothing on segmentation.
- **Remaining novelty:** the explicit decomposition and the predicted variance-dominated regime where LoRA wins; unifying theory under B-0114/B-0248/B-0306 (auditor's rationale).
- **Mutation:** run the decomposition on 2-3 segmentation tasks × data scales; deliver the crossover law.

### R10 / A-0096 — The small-lesion sensitivity law *(auditor revive)*
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Segment anything model for medical images? (Medical Image Analysis 2024, arXiv 2304.14660)](https://arxiv.org/abs/2304.14660) — large-scale SAM evaluation including size-stratified failure on small/complex structures. [Frozen Foundation-Model Embeddings Discard Small-Lesion Signal in Chest Radiography (arXiv 2606.11606)](https://arxiv.org/abs/2606.11606) — mechanism: small-lesion signal lost at global aggregation, recoverable from patch tokens.
- **What they did:** established that FMs underperform on small structures and localized one mechanism (pooling).
- **Exact difference:** no *comparative law*: sensitivity-vs-size curves for FM families vs specialist nnU-Nets at matched aggregate Dice, sigmoid-midpoint (size at 50% sensitivity) as the comparison statistic.
- **Remaining novelty:** the matched-Dice size-response comparison and its clinical triage implication (which model class to deploy for small-lesion tasks).
- **Mutation:** deliver midpoint-shift curves across ≥3 lesion tasks; connect to the 2606.11606 pooling mechanism as explanans.

### R7 / A-0124 — The smoke/fog/steam/cloud/dust confusion benchmark *(auditor revive)*
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [FIgLib & SmokeyNet: Dataset and Deep Learning Model for Real-Time Wildland Fire Smoke Detection (arXiv 2112.08598)](https://arxiv.org/abs/2112.08598) — wildfire smoke benchmark; documents cloud/fog false positives and uses temporal models to suppress them.
- **What they did:** built smoke-vs-background benchmarks where confusable aerosols appear as noise, not as a controlled taxonomy.
- **Exact difference:** no benchmark with *labeled five-way aerosol classes* (smoke/fog/steam/cloud/dust), no human frame-vs-clip information analysis establishing whether single-frame separation is even possible.
- **Remaining novelty:** the taxonomy benchmark + the human information-floor experiment; directly quantifies the false-alarm question under every smoke-detection deployment.
- **Mutation:** none beyond gating on curation feasibility (auditor already flagged); keep the human frame/clip study as the headline.

### R11 / A-0301 — Continual adaptation under cyclically returning domains *(auditor revive)*
**Verdict: KILL** (confidence: high)
- **Kill cite:** [ReservoirTTA: Prolonged Test-time Adaptation for Evolving and Recurring Domains (arXiv 2505.14511)](https://arxiv.org/abs/2505.14511), building on [Continual Test-Time Domain Adaptation — CoTTA (CVPR 2022, arXiv 2203.13591)](https://arxiv.org/abs/2203.13591).
- **What they did:** ReservoirTTA explicitly evaluates *recurring* domain sequences, documents re-adaptation cost/thrashing, and solves it with a reservoir of domain-specialized models achieving near-zero cost on domain return — the exact protocol and the fix this idea proposed to study.
- **Exact difference:** none material; segmentation is included in TTA benchmarks of this line.
- **Remaining novelty:** marginal protocol variants only.
- **Confidence:** high.

### R8 / A-0328 — Simulated-click protocol validity for interactive segmentation *(auditor revive)*
**Verdict: KILL** (confidence: high)
- **Kill cite:** [RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation (NeurIPS 2024, arXiv 2410.11722)](https://arxiv.org/abs/2410.11722).
- **What they did:** collected large-scale *real user clicks*, compared against standard simulated-click protocols, showed benchmark rankings shift under realistic clicks — the protocol-validity study itself, model generation included.
- **Exact difference:** only residual: coupling with this program's own logged clicks (B-0089/B-0193). That is replication, not a new question.
- **Remaining novelty:** marginal.
- **Confidence:** high.

---

## Batch B

### B-0017 — The missing-negative problem in transparent-object benchmarks
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Segmenting Transparent Objects in the Wild — Trans10K (ECCV 2020, arXiv 2003.13948)](https://arxiv.org/abs/2003.13948) — the standard transparent-object benchmark (positives-focused). [Don't Hit Me! Glass Detection in Real-World Scenes (CVPR 2020)](https://openaccess.thecvf.com/content_CVPR_2020/html/Mei_Dont_Hit_Me_Glass_Detection_in_Real-World_Scenes_CVPR_2020_paper.html) — glass detection benchmark; discusses ambiguity but negatives are incidental.
- **What they did:** built transparent/glass benchmarks dominated by images containing the target class.
- **Exact difference:** no systematic audit of *negative-image composition* (glass-free scenes with glass-like cues: reflections, frames, screens) and its effect on reported precision; no hard-negative test suite.
- **Remaining novelty:** quantify false-positive rates of published models on curated hard negatives; show benchmark precision is inflated by missing negatives.
- **Mutation:** deliver a negative-suite addendum to Trans10K/GDD and a precision-correction table for published SOTA.

### B-0041 — Frequency-band attribution of SAM's medical-domain failures *(stage-1 text)*
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [FDA: Fourier Domain Adaptation for Semantic Segmentation (CVPR 2020, arXiv 2004.05498)](https://arxiv.org/abs/2004.05498) — amplitude-spectrum swapping as a domain-shift manipulation. [A Fourier Perspective on Model Robustness (NeurIPS 2019, arXiv 1906.08988)](https://arxiv.org/abs/1906.08988) — frequency-band sensitivity analysis of model failures.
- **What they did:** established both the manipulation (amplitude swap) and the analysis style (band-limited perturbation sensitivity).
- **Exact difference:** no work applies band-wise attribution to *SAM's* natural→medical failure specifically, decomposing how much of the gap is low-frequency amplitude statistics vs mid/high-band structure.
- **Remaining novelty:** the attribution result and its actionable consequence (if low-band: cheap spectral alignment recovers SAM without fine-tuning).
- **Mutation:** run FDA-style band swaps between natural/medical domains on frozen SAM; report recovered-Dice-per-band curves.

### B-0047 — Shift-absorption depth *(stage-1 text)*
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [Surgical Fine-Tuning Improves Adaptation to Distribution Shifts (ICLR 2023, arXiv 2210.11466)](https://arxiv.org/abs/2210.11466) — best block to fine-tune depends on shift type (input-level → early layers, output-level → late layers).
- **What they did:** established the shift-type ↔ layer-depth correspondence for classification and proposed auto-selection criteria.
- **Exact difference:** classification only; no dense-prediction version, no *measurement of where shift is absorbed* (per-block representation drift during full FT) as opposed to where tuning works, no label-convention shifts (annotation-style differences), which are unique to segmentation.
- **Remaining novelty:** drift-based absorption-depth measurement for segmentation, including convention shifts; predictive test (drift profile → best PEFT placement).
- **Mutation:** position as the dense/mechanistic sequel to surgical FT; label-convention shift is the novel axis.

### B-0064 — Does classical UDA add anything on top of frozen foundation features?
**Verdict: KILL** (confidence: high)
- **Kill cite:** [What is the Added Value of UDA in the VFM Era? (CVPRW 2025, arXiv 2504.18190)](https://arxiv.org/abs/2504.18190), with [Exploring the Benefits of Vision Foundation Models for Unsupervised Domain Adaptation (CVPRW 2024)](https://openaccess.thecvf.com/content/CVPR2024W/2WFM/html/Englert_Exploring_the_Benefits_of_Vision_Foundation_Models_for_Unsupervised_Domain_CVPRW_2024_paper).
- **What they did:** measured exactly this: UDA's increment over source-only fine-tuning of VFMs across synth-to-real and real-to-real segmentation; found the gain shrinks from +8 to +2 mIoU with strong source data and vanishes with diverse real sources.
- **Exact difference:** none material — the question, the models, the task, and the mixed conclusion are all published.
- **Remaining novelty:** marginal (other tasks/modalities).
- **Confidence:** high.

### B-0083 — Prompt-protocol sensitivity: do medical-SAM rankings depend on the click recipe?
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [Segment anything model for medical images? (MedIA 2024, arXiv 2304.14660)](https://arxiv.org/abs/2304.14660) — large-scale evaluation across prompt modes showing performance depends heavily on prompt type/quality. [RClicks (arXiv 2410.11722)](https://arxiv.org/abs/2410.11722) — model rankings shift under realistic vs simulated clicks (natural images). [BREPS (AAAI 2026, arXiv 2601.15123)](https://arxiv.org/abs/2601.15123) — per-user prompt variability changes segmentation quality substantially, incl. medical data.
- **What they did:** established prompt-dependence of absolute performance and (RClicks) ranking instability for natural-image interactive segmentation.
- **Exact difference:** no study of whether published *medical-SAM leaderboard rankings* (MedSAM vs SAM-Med2D vs …) invert under alternative click/box recipes; medical papers each fix one protocol.
- **Remaining novelty:** cross-protocol ranking-stability audit specifically for the medical SAM-variant literature; recipe-standardization recommendation.
- **Mutation:** re-evaluate the top medical SAM variants under a protocol grid; report Kendall-τ of rankings across recipes.

### B-0084 — Out-of-domain calibration of SAM's mask-quality head
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [EvanySeg (arXiv 2409.14874)](https://arxiv.org/abs/2409.14874) — motivated by SAM's predicted-IoU being unreliable on medical data; trains an external quality model instead. [SAM-U: Multi-box prompts triggered uncertainty estimation (arXiv 2307.04973)](https://arxiv.org/abs/2307.04973) — distrusts SAM confidence OOD, adds prompt-ensemble uncertainty.
- **What they did:** noted/worked around IoU-head unreliability; built substitutes.
- **Exact difference:** no direct *calibration study* of the IoU head itself as a function of domain shift (reliability diagrams, ECE vs shift magnitude, failure taxonomy of the head).
- **Remaining novelty:** the quantified calibration-decay law and cheap recalibration (temperature/conformal) as a baseline against verifier models.
- **Mutation:** deliver "IoU-head calibration across 10 domains + conformal fix"; position as the diagnostic EvanySeg presumes.

### B-0104 — Wrong-prompt behavior: does SAM fail loudly or silently?
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Segment Anything Is Not Always Perfect (arXiv 2304.05750)](https://arxiv.org/abs/2304.05750) — failure survey across real-world conditions incl. prompt issues. [Stable Segment Anything Model (arXiv 2311.15776)](https://arxiv.org/abs/2311.15776) — systematic study of *low-quality* (misplaced/loose) prompts and a stabilization fix. [BREPS (arXiv 2601.15123)](https://arxiv.org/abs/2601.15123) — adversarial/natural box perturbations.
- **What they did:** characterized geometric prompt degradation (shifted/loose boxes, wrong scale).
- **Exact difference:** semantic prompt errors (prompt indicates the *wrong object/class*, ambiguous referent) and the loud-vs-silent question — does confidence flag the error — are not studied.
- **Remaining novelty:** semantic-error taxonomy × confidence behavior; silent-failure rate as a deployment safety number.
- **Mutation:** build wrong-referent prompt suites; report P(confident|wrong-object) across SAM variants; tie to B-0084 calibration.

### B-0114 — Seed variance of PEFT fine-tuning versus reported effect sizes
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping (arXiv 2002.06305)](https://arxiv.org/abs/2002.06305) — seed variance rivals method deltas in NLP fine-tuning. [On the Stability of Fine-tuning BERT (arXiv 2006.04884)](https://arxiv.org/abs/2006.04884) — instability diagnosis and remedies.
- **What they did:** established seed-variance-vs-effect-size critique for NLP full fine-tuning.
- **Exact difference:** no equivalent audit for *PEFT on dense prediction*: is LoRA's seed variance smaller (regularization) or larger (lottery of low-rank subspace)? Are published medical-PEFT deltas within seed noise?
- **Remaining novelty:** variance decomposition (seed/data-order/rank-init) for segmentation PEFT + re-analysis of published effect sizes against the measured noise floor.
- **Mutation:** couple with revived A-0052 (same runs serve both); deliver a "minimum detectable effect" table for the field.

### B-0120 — Are SAM's multimask candidates a valid uncertainty sample?
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Segment Anything (arXiv 2304.02643)](https://arxiv.org/abs/2304.02643) — multimask output *designed* for ambiguity. [SAM-U (arXiv 2307.04973)](https://arxiv.org/abs/2307.04973) — prompt-ensemble uncertainty from SAM outputs. [Probabilistic U-Net (NeurIPS 2018, arXiv 1806.05034)](https://arxiv.org/abs/1806.05034) — gold-standard framework for matching predicted mask distributions to *multi-rater* distributions (GED metric).
- **What they did:** built the candidate mechanism and distributional evaluation methodology; nobody has connected them.
- **Exact difference:** no test of whether SAM's 3 candidates approximate rater distributions (coverage, diversity calibration, GED vs Prob-U-Net) on multi-annotator datasets.
- **Remaining novelty:** the validity verdict — practitioners currently use multimask spread as uncertainty without evidence.
- **Mutation:** evaluate on LIDC/QUBIQ-style multi-rater data with GED/coverage; compare to Prob-U-Net and prompt-ensembles.

### B-0121 — Representation profiles: what SAM, DINOv2, CLIP encode for dense tasks *(stage-1 text)*
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Probing the 3D Awareness of Visual Foundation Models (CVPR 2024, arXiv 2404.08636)](https://arxiv.org/abs/2404.08636); [Battle of the Backbones (NeurIPS 2023, arXiv 2310.19909)](https://arxiv.org/abs/2310.19909); [AM-RADIO: Agglomerative Vision Foundation Model (CVPR 2024, arXiv 2312.06709)](https://arxiv.org/abs/2312.06709).
- **What they did:** systematically probed SAM/DINOv2/CLIP (and more) with standardized dense-task batteries (depth, correspondence, segmentation, detection), characterized per-model representational biases, and (RADIO) quantified complementary strengths while distilling them into one backbone.
- **Exact difference:** the proposed "probing battery whose profile distance predicts downstream fit" is the same measurement program; predictive-transfer claims are incremental given Battle-of-Backbones' breadth.
- **Remaining novelty:** marginal (a formal profile→task-fit regression).
- **Confidence:** high.

### B-0129 — Small-structure failure: information absent or decoder-limited?
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Frozen Foundation-Model Embeddings Discard Small-Lesion Signal in Chest Radiography (arXiv 2606.11606)](https://arxiv.org/abs/2606.11606).
- **What they did:** exactly this decomposition: probed five frozen ViT FMs; showed global (CLS/mean-pool) embeddings sit at chance for small-scale signal while *patch-local probes recover AUC ≈ 1.0 from the same forward pass* — i.e., information present, aggregation/decoder-limited — across 3 cohorts and real small lesions.
- **Exact difference:** B-0129 wanted the same probe for segmentation decoders; the information-vs-readout verdict is already delivered, chest-X-ray classification framing notwithstanding.
- **Remaining novelty:** thin — replicating on segmentation decoders specifically.
- **Confidence:** high.

### B-0132 — Layer-wise localization decay in VLMs
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Blind to Position, Biased in Language (arXiv 2509.23098)](https://arxiv.org/abs/2509.23098); [Mechanisms of Object Localization in Vision-Language Models (arXiv 2605.19792)](https://arxiv.org/abs/2605.19792); [Grounding Isn't Knowing (arXiv 2608.23074)](https://arxiv.org/abs/2608.23074).
- **What they did:** layer-wise probing of spatial/localization information in VLM stacks: final-layer embeddings prioritize global alignment and lose positional sensitivity; mid-layers retain spatial maps (exploitable for zero-shot RIS, +1–7 mIoU); token/layer/head-level accounts of where localization lives and decays.
- **Exact difference:** the survivor's probe-per-layer decay curve is published in multiple model families.
- **Remaining novelty:** marginal.
- **Confidence:** high.

### B-0186 — Does generative augmentation cover the tail it promises to fix?
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Is synthetic data from generative models ready for image recognition? (ICLR 2023, arXiv 2210.07574)](https://arxiv.org/abs/2210.07574) — systematic audit of when synthetic data helps, incl. data-scarce regimes. [Effective Data Augmentation With Diffusion Models (ICLR 2024, arXiv 2302.07944)](https://arxiv.org/abs/2302.07944) — diffusion augmentation evaluated for semantic diversity beyond simple transforms.
- **What they did:** audited utility of generative augmentation for recognition, including few-shot/rare settings.
- **Exact difference:** no *coverage* audit for segmentation tails: does the generator actually produce the rare morphologies (measured in feature space against held-out tail cases), or does it resample the head with cosmetic variation?
- **Remaining novelty:** tail-coverage metrics (feature-space recall of held-out rare modes) and the predicted negative result for off-the-shelf diffusion in medical segmentation.
- **Mutation:** deliver coverage-vs-benefit analysis: show per-mode synthetic recall predicts per-mode Dice gain.

### B-0189 — The inpainting fingerprint: do models learn the lesion or the paste?
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [What makes fake images detectable? (ECCV 2020, arXiv 2008.10588)](https://arxiv.org/abs/2008.10588) and [Leveraging Frequency Analysis for Deep Fake Image Recognition (ICML 2020, arXiv 2003.08685)](https://arxiv.org/abs/2003.08685) — generative pipelines leave detectable spectral/local artifacts. [Towards Universal Fake Image Detectors (CVPR 2023, arXiv 2302.10174)](https://arxiv.org/abs/2302.10174) — such artifacts generalize across generators.
- **What they did:** established that generated/inpainted content carries learnable fingerprints.
- **Exact difference:** no one has tested whether *medical models trained on inpainting-augmented lesions* learn the fingerprint instead of pathology — i.e., shortcut contamination of the augmentation itself (a training-data hazard, not a forensics task).
- **Remaining novelty:** the contamination experiment: train on inpainted lesions, test on real; probe with fingerprint-only stimuli (inpainting artifact without lesion); quantify shortcut share.
- **Mutation:** frame as augmentation-safety audit; deliverable = artifact-detectability threshold below which inpainting augmentation is safe.

### B-0217 — The box-to-mask error transfer function
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [BREPS (AAAI 2026, arXiv 2601.15123)](https://arxiv.org/abs/2601.15123) — robustness of SAM-likes to natural/adversarial box perturbations, real-user boxes. [PP-SAM (arXiv 2405.16740)](https://arxiv.org/abs/2405.16740) — training with perturbed boxes for robustness. [RoBox-SAM (arXiv 2407.21284)](https://arxiv.org/abs/2407.21284) — refining low-quality boxes.
- **What they did:** measured and mitigated box-prompt sensitivity with generic perturbation models.
- **Exact difference:** no *detector-matched* treatment: characterizing the actual error distribution of upstream detectors (per class/size/domain) and deriving the composed detect→segment transfer function; existing work perturbs uniformly or adversarially.
- **Remaining novelty:** the transfer-function formalism + training with detector-realistic noise; predicts end-to-end pipeline accuracy from detector metrics.
- **Mutation:** fit box-error distributions of common detectors; show composed-error prediction and detector-matched fine-tuning beating PP-SAM's uniform jitter.

### B-0223 — Assigner-induced bias against elongated objects
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Slender Object Detection: Diagnoses and Improvements (arXiv 2011.08529)](https://arxiv.org/abs/2011.08529).
- **What they did:** diagnosed precisely this: standard detectors' label assignment/anchor–IoU machinery systematically fails on high-aspect-ratio ("slender") objects; quantified the bias and proposed assigner/feature fixes.
- **Exact difference:** the survivor adds instance segmentation phrasing; the mechanism, diagnosis, and remedies are published.
- **Remaining novelty:** marginal (mask-AP re-run of the same diagnosis).
- **Confidence:** high.

### B-0248 — Does PEFT protect zero-shot generality? The retention-adaptation frontier
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [Fine-tuning can cripple your foundation model (arXiv 2308.13320)](https://arxiv.org/abs/2308.13320) — concept forgetting under fine-tuning; preservation methods. [LoRA Learns Less and Forgets Less (arXiv 2405.09673)](https://arxiv.org/abs/2405.09673) — the retention-adaptation trade-off measured for LoRA vs full FT (LLMs). [Robust fine-tuning of zero-shot models — WiSE-FT (CVPR 2022, arXiv 2109.01903)](https://arxiv.org/abs/2109.01903) — interpolation traces the frontier for CLIP classification.
- **What they did:** mapped retention-vs-adaptation for classification/LLMs; established interpolation baselines.
- **Exact difference:** no frontier for *promptable segmentation* (does LoRA-adapted SAM keep zero-shot promptability on unseen domains?) and no method×rank×data-scale frontier chart for dense tasks.
- **Remaining novelty:** the dense/promptable frontier and whether WiSE-FT-style interpolation dominates PEFT there too.
- **Mutation:** deliver the frontier plot for SAM variants; test interpolation as the baseline to beat.

### B-0306 — Less rank, more accuracy: the low-rank advantage on tiny datasets
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [LoRA Learns Less and Forgets Less (arXiv 2405.09673)](https://arxiv.org/abs/2405.09673) — rank effects on capacity/regularization. [The Expressive Power of Low-Rank Adaptation (arXiv 2310.17513)](https://arxiv.org/abs/2310.17513) — theory of rank-limited expressivity. [SAMed (arXiv 2304.13785)](https://arxiv.org/abs/2304.13785) — low-rank SAM adaptation on limited medical data as standard practice.
- **What they did:** rank ablations exist scattered across papers; theory bounds expressivity; practice already favors low rank on small data.
- **Exact difference:** no systematic rank×dataset-size law for segmentation showing a *crossover* (low rank wins below a data threshold) with variance-based explanation.
- **Remaining novelty:** the empirical law + its use for rank selection without validation sweeps; ties to A-0052's decomposition.
- **Mutation:** merge with A-0052/B-0114 into a single PEFT-statistics program (auditor's merge list already suggests this).

### B-0318 — Differentiable scattering: a physics head for volumetric smoke
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [Global Transport for Fluid Reconstruction with Learned Self-Supervision (CVPR 2021, arXiv 2104.06031)](https://arxiv.org/abs/2104.06031) — differentiable-rendering-based volumetric smoke density reconstruction from sparse views with learned self-supervision (ScalarFlow line).
- **What they did:** reconstructed 3D smoke density fields from images via differentiable transport/rendering in lab/capture settings.
- **Exact difference:** optimization-per-scene multi-view lab capture vs the survivor's *feed-forward network supervised only by 2D wildfire segmentation masks* through a differentiable scattering renderer, targeting single-view in-the-wild quantification.
- **Remaining novelty:** amortized single-image mask-supervised volumetric estimation for wildfire smoke; enabling hypothesis (mask silhouettes constrain density enough) is falsifiable.
- **Mutation:** position against Global Transport as the per-scene upper bound; validate on ScalarFlow-style captures before wildfire imagery.

### B-0320 — Positive-unlabeled statistics for everything-mode auto-labeling
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [Object Detection as a Positive-Unlabeled Problem (BMVC 2020, arXiv 2002.04672)](https://arxiv.org/abs/2002.04672) — PU formulation for detection under incomplete labels.
- **What they did:** established PU losses/corrections for detection with missing annotations.
- **Exact difference:** no PU treatment of *SAM everything-mode auto-labeling* pipelines (unprompted mask proposals as a contaminated positive set; estimating class priors and correcting downstream training).
- **Remaining novelty:** PU-corrected auto-label training and bias bounds for FM-generated pseudo-masks; contamination-rate estimator per domain.
- **Mutation:** deliver the estimator + corrected-training recipe; evaluate against naive auto-label baselines on 2-3 domains.

### R9 / B-0033 — Tail open-vocabulary failure is linguistic, not visual *(auditor revive)*
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [LaMI-DETR: Open-Vocabulary Detection with Language Model Instruction (ECCV 2024, arXiv 2407.11335)](https://arxiv.org/abs/2407.11335) — LLM-derived concept information fixes tail OV failures (implies linguistic bottleneck). [No "Zero-Shot" Without Exponential Data (arXiv 2404.04125)](https://arxiv.org/abs/2404.04125) — pretraining concept *frequency* drives zero-shot performance.
- **What they did:** showed language-side interventions help and frequency explains tails — but as method papers/correlational analyses.
- **Exact difference:** no *causal decomposition* isolating linguistic vs visual causes via text-only interventions (synonym substitution, definition prompts, embedding surgery) at matched visual input, for dense prediction.
- **Remaining novelty:** the attribution experiment and its portfolio consequence: if linguistic, tail fixes are cheap text-side; if visual, they are not.
- **Mutation:** run text-side-only intervention grid on OV segmentation tails; report % of tail gap closed without touching vision.

### R3 / B-0081 — Which segmentation metric predicts downstream clinical measurement error? *(auditor revive)*
**Verdict: KILL** (confidence: medium-high)
- **Kill cite:** [Are we using appropriate segmentation metrics? (Kofler et al., arXiv 2103.06205)](https://arxiv.org/abs/2103.06205) + [Metrics Reloaded: recommendations for image analysis validation (arXiv 2206.01653)](https://arxiv.org/abs/2206.01653), backed by the radiotherapy auto-contouring literature correlating geometric metrics with downstream clinical/dosimetric quantities (e.g., Vaassen et al., Physics and Imaging in Radiation Oncology 2020, which introduced surface-Dice/added-path-length precisely because Dice correlates poorly with the clinically consumed quantity).
- **What they did:** the metric→clinical-utility validity question is an active, well-populated literature: metric-vs-expert-judgment correlation (Kofler), task-aware metric selection frameworks (Metrics Reloaded), and metric-vs-dosimetric/workload studies in radiotherapy showing weak geometric-clinical correlation.
- **Exact difference:** the survivor's specific derived measurements (volume, RECIST diameter, ejection fraction) beyond dose are variations on a published theme with known conclusions (correlation is metric- and task-dependent, Dice insufficient).
- **Remaining novelty:** incremental breadth.
- **Confidence:** medium-high.

### R12 / B-0098 — Independent verifier vs self-confidence for failure prediction *(auditor revive)*
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [EvanySeg (arXiv 2409.14874)](https://arxiv.org/abs/2409.14874) — independent companion model scoring segmentation quality without GT. Reverse Classification Accuracy (Valindria et al., IEEE TMI 2017) — earlier GT-free performance prediction.
- **What they did:** built independent verifiers and showed they predict quality.
- **Exact difference:** no controlled comparison of verifier vs the segmenter's *own confidence* under matched conditions, no cross-domain/cross-model generalization stress test of verifiers, no attribution of *what* the verifier sees that self-confidence misses.
- **Remaining novelty:** the comparative science (when does an external verifier beat calibrated self-confidence, and why) — the auditor's "make the science explicit" revive rationale stands.
- **Mutation:** benchmark EvanySeg-style verifiers vs temperature-scaled/conformal self-confidence across shifted domains; add feature-attribution analysis.

### R2 / B-0177 — Restain-and-register IHC as molecular ground truth for H&E *(auditor revive)*
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Epithelium segmentation using deep learning in H&E-stained prostate specimens with immunohistochemistry as reference standard (Scientific Reports 2019)](https://www.nature.com/articles/s41598-018-37257-4).
- **What they did:** the full proposed pipeline, in 2019: destain/restain 102 sections with IHC markers, co-register H&E↔IHC, derive objective epithelium ground truth from IHC via color deconvolution, train H&E segmentation on it, show external generalization. A sizeable follow-on literature extends this restain-register-train paradigm to other markers/tissues.
- **Exact difference:** the survivor's remaining delta (registration-noise-aware losses) is an engineering refinement of a published paradigm.
- **Remaining novelty:** thin.
- **Confidence:** high.

### R6 / B-0286 — Subgroup regression under fine-tuning *(auditor revive)*
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [Robust fine-tuning of zero-shot models — WiSE-FT (arXiv 2109.01903)](https://arxiv.org/abs/2109.01903) — fine-tuning trades robustness for target accuracy; interpolation mitigates. [FairTune: Optimizing PEFT for Fairness in Medical Image Analysis (ICLR 2024, arXiv 2310.05055)](https://arxiv.org/abs/2310.05055) — PEFT configuration affects subgroup fairness in medical imaging.
- **What they did:** established average-vs-subgroup tension in fine-tuning and fairness-aware PEFT for medical *classification*.
- **Exact difference:** no systematic audit of subgroup *regression* (who gets worse when the average improves) for dense medical segmentation, across adaptation methods, with per-subgroup mask metrics.
- **Remaining novelty:** the regression audit + reporting standard (subgroup-regression disclosure for adaptation papers); dense-task fairness data barely exists.
- **Mutation:** audit 3-4 public medical segmentation fine-tunes with demographic metadata; report worst-subgroup ΔDice vs average ΔDice.

### R5 / B-0300 — Objectness erosion: continued SSL pretraining hurts promptable segmentation *(auditor revive)*
**Verdict: MUTATE** (confidence: high)
- **Closest prior:** [Exploring Structural Degradation in Dense Representations for SSL (NeurIPS 2025, arXiv 2510.17299)](https://arxiv.org/abs/2510.17299) — Self-supervised Dense Degradation: longer SSL training degrades dense performance across 16 methods; detection/regularization proposed. [DINOv3 (arXiv 2508.10104)](https://arxiv.org/abs/2508.10104) — names dense-feature degradation over long schedules a known unsolved issue; Gram anchoring fix.
- **What they did:** established the phenomenon (continued SSL erodes dense features) and mitigations, for generic SSL pretraining.
- **Exact difference:** not studied for *promptable* models (SAM-style) under continued *domain-adaptive* pretraining — where the casualty is promptability/objectness (everything-mode recall, prompt response) rather than linear-probe mIoU.
- **Remaining novelty:** the recipe-conflict result for domain-adapting SAM-likes (medical SSL continue-pretrain → objectness erosion), with SDD/Gram-anchoring as candidate fixes to test.
- **Mutation:** measure everything-mode recall + prompt fidelity along continued-pretraining trajectories on medical corpora; test DSE/Gram-anchoring as protectors.

---

## Batch C

### C-0061 — Global leakage in CLIP patch tokens
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [ClearCLIP (ECCV 2024, arXiv 2407.12442)](https://arxiv.org/abs/2407.12442) — showed CLIP's contrastive training emphasizes global feature directions in patch/residual streams, degrading dense inference; architectural decomposition fix. [Vision Transformers Need Registers (arXiv 2309.16588)](https://arxiv.org/abs/2309.16588) — patch tokens repurposed as carriers of global information (artifacts).
- **What they did:** established the phenomenon qualitatively/architecturally and fixed it heuristically.
- **Exact difference:** no *quantitative information-theoretic* measurement (MI between patch token and global label vs local content) as a per-model "leakage index," nor its use to predict dense-task transfer.
- **Remaining novelty:** the leakage-quantification methodology and cross-model leakage league table (CLIP vs DINOv2 vs SAM).
- **Mutation:** deliver the MI-based leakage estimator; validate it predicts ClearCLIP-style fix gains per model.

### C-0067 — Prompt-averaged leaderboards for open-vocab segmentation
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [CLIP (arXiv 2103.00020)](https://arxiv.org/abs/2103.00020) — prompt templates/ensembling as standard practice. [Waffling around for Performance (ICCV 2023, arXiv 2306.07282)](https://arxiv.org/abs/2306.07282) — prompt/synonym ensembling analyzed; random words rival curated prompts.
- **What they did:** established prompt sensitivity and ensembling for classification-style zero-shot scoring.
- **Exact difference:** no leaderboard-repair treatment for *open-vocab segmentation*: treating class-name choice as measurement noise, reporting prompt-averaged means with CIs, and testing whether published rankings survive.
- **Remaining novelty:** the ranking-stability result under synonym resampling for dense benchmarks; a reporting-standard fix.
- **Mutation:** re-score 5-6 OV-seg methods under synonym distributions; report CI-overlapped rank flips; merges naturally with B-0083 (protocol sensitivity).

### C-0072 — Text-only baseline audit for referring segmentation
**Verdict: KILL** (confidence: medium-high)
- **Kill cite:** [Visual Referring Expression Recognition: What Do Systems Actually Learn? (NAACL 2018, arXiv 1805.11818)](https://arxiv.org/abs/1805.11818) + [Cops-Ref (CVPR 2020, arXiv 2003.00403)](https://arxiv.org/abs/2003.00403).
- **What they did:** Cirik et al. ran degenerate-input baselines on referring benchmarks (image-only ignoring the expression beats random by large margins; models unaffected by syntax destruction), exposing exactly the language/dataset-prior exploitability this idea targets; Cops-Ref and successors (e.g., Ref-Adv) built benchmarks specifically to defeat these shortcuts, citing the bias findings as motivation.
- **Exact difference:** the survivor's variant (text-only mask predictability for *segmentation* rather than box selection) is a metric-level twist on a settled audit; the field already moved to constructing harder benchmarks.
- **Remaining novelty:** thin.
- **Confidence:** medium-high.

### C-0149 — Clinical-safety probe for laterality
**Verdict: KILL** (confidence: medium)
- **Kill cite:** [Deep learning models for radiography body-part and chest projection/orientation classification (European Radiology 2025)](https://doi.org/10.1007/s00330-025-12053-7) + [Quality Assurance of Chest X-ray Images with Deep Learning (Applied Sciences 2023)](https://doi.org/10.3390/app13042067); VLM side: [Visual Spatial Reasoning (TACL 2023, arXiv 2205.00363)](https://arxiv.org/abs/2205.00363).
- **What they did:** medical QA systems detect orientation/left-right reversal at AUC ≈ 1.00 on hundreds of thousands of radiographs (laterality information is present and trivially decodable); VSR documented left/right relational failures in vision-language models on natural images.
- **Exact difference:** the survivor's residue is probing *foundation-model embeddings* specifically; but the two published poles (signal trivially decodable by supervised probes; relational left/right confusions in VLM heads) bracket the answer, making the probe confirmatory.
- **Remaining novelty:** thin — a linear-probe replication on medical FM embeddings.
- **Confidence:** medium.

### C-0205 — Boundary error budget (aleatoric / protocol / model)
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? (NeurIPS 2017, arXiv 1703.04977)](https://arxiv.org/abs/1703.04977) — aleatoric/epistemic decomposition. Rädsch et al., "Labelling instructions matter in biomedical image analysis" (Nature Machine Intelligence 2023) — annotation-protocol variance as a first-class error source. [Maier-Hein et al. 2018](https://www.nature.com/articles/s41467-018-07619-7) — observer effects dominate rankings.
- **What they did:** established the components separately (aleatoric uncertainty; protocol effects; observer variance).
- **Exact difference:** no unified *boundary-specific three-way budget* with a reusable estimation protocol (multi-rater + protocol-controlled re-annotation + model ensembles) yielding per-dataset error shares.
- **Remaining novelty:** the decomposition methodology and its headline: what fraction of reported boundary error is actually model-attributable.
- **Mutation:** pilot on 2 datasets with existing multi-rater labels; publish budget pie charts + estimator code.

### C-0206 — Physics floor for boundary error
**Verdict: KEEP** (confidence: medium-high)
- **Closest prior:** partial-volume-effect literature (e.g., Soret, Bacharach & Buvat, "Partial-volume effect in PET tumor imaging," Journal of Nuclear Medicine 2007) — PVE/PSF limits on quantification are canonical physics; resolution limits on boundary localization are folklore in medical imaging.
- **What they did:** characterized PVE for *quantification* (uptake, volumes), not as a computable per-dataset lower bound on segmentation boundary metrics.
- **Exact difference:** no published computable "physics floor" (PSF + slice thickness + reconstruction kernel → bound on achievable HD/surface-Dice) against which leaderboard proximity can be judged; no demonstration that top methods have plateaued at the floor.
- **Remaining novelty:** the bound construction, per-benchmark floor tables, and plateau verdicts — a decision tool for whether further method work is physically pointless.
- **Confidence:** medium-high (searches for a direct floor formalization came up empty).

### C-0249 — Losses under multimodal (discrete-hypothesis) ground truth
**Verdict: KILL** (confidence: medium-high)
- **Kill cite:** [Probabilistic U-Net (NeurIPS 2018, arXiv 1806.05034)](https://arxiv.org/abs/1806.05034) + [Stochastic Segmentation Networks (NeurIPS 2020, arXiv 2006.06015)](https://arxiv.org/abs/2006.06015).
- **What they did:** built the multimodal-ground-truth problem into the core framing: pixel-wise losses trained on ambiguous/multi-rater data collapse to averages matching no rater; both papers demonstrate the failure (incl. discrete hypothesis splits, e.g. LIDC lesion in/out) and model the full mask distribution instead, with distribution-matching metrics (GED).
- **Exact difference:** the survivor's "stress-test the losses" is the diagnostic half of what these papers demonstrated en route to their models.
- **Remaining novelty:** marginal (a cleaner taxonomy of discrete vs continuous ambiguity).
- **Confidence:** medium-high.

### C-0261 — Grid-phase sensitivity of ViT segmentation
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Phase Marginalization for Patch-Grid Instability in Vision Transformers (arXiv 2606.08132)](https://arxiv.org/abs/2606.08132) + [Making Vision Transformers Truly Shift-Equivariant (arXiv 2305.16316)](https://arxiv.org/abs/2305.16316).
- **What they did:** formalized patch-grid phase as a measurable nuisance for dense ViT prediction, measured phase-dependent output instability (segmentation/depth/matching), and proposed marginalization; the shift-equivariance line had already quantified ViT output sensitivity to sub-patch shifts and rebuilt modules to remove it.
- **Exact difference:** the proposed measurement (performance oscillation vs boundary-grid alignment) is the nuisance these papers measure and correct.
- **Remaining novelty:** marginal (benchmark-noise bookkeeping).
- **Confidence:** high.

### C-0300 — Attributing nnU-Net's dominance
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [nnU-Net Revisited: A Call for Rigorous Validation (MICCAI 2024, arXiv 2404.09556)](https://arxiv.org/abs/2404.09556) — most claimed architectural advances vanish under correct nnU-Net configuration; configuration/validation dominates. [Lightweight image segmentation for echocardiography (arXiv 2509.03631)](https://arxiv.org/abs/2509.03631) — explicit component-wise nnU-Net ablation (augmentation, deep supervision, normalization drive performance) on cardiac ultrasound.
- **What they did:** demonstrated configuration > architecture and ran single-domain component ablations.
- **Exact difference:** no *multi-task factorial attribution* separating preprocessing/normalization stack vs self-configuration heuristics vs architecture across the medical-segmentation task spectrum.
- **Remaining novelty:** the cross-task attribution table ("copy the preprocessing, skip the rest"?) — partially preempted and shrinking.
- **Mutation:** narrow to the unexplored factor: port nnU-Net's preprocessing stack alone onto non-nnU-Net models across ≥5 tasks; measure recovered share of the gap.

### C-0321 — Re-annotation noise floor vs leaderboard gaps
**Verdict: MUTATE** (confidence: medium-high)
- **Closest prior:** [Why rankings of biomedical image analysis competitions should be interpreted with care (Nature Communications 2018)](https://www.nature.com/articles/s41467-018-07619-7) — rankings not robust to observer/annotation choices; observer swaps flip ranks.
- **What they did:** established ranking fragility including annotation-observer sensitivity, at challenge scale.
- **Exact difference:** no cheap *standardized protocol* (≈50 images × 3 raters) that computes a per-benchmark noise floor and certifies whether specific published leaderboard gaps exceed it; Maier-Hein shows the problem, doesn't ship the routine audit.
- **Remaining novelty:** the protocol + floor certificates for currently cited leaderboards (natural-image ones included, where multi-rater data is rarer).
- **Mutation:** deliver the audit kit and apply it to 3 heavily cited benchmarks; report which SOTA gaps are sub-floor.

### C-0326 — Slice-order checkerboard test for "3D" models
**Verdict: MUTATE** (confidence: medium)
- **Closest prior:** [What Makes a Video a Video: Analyzing Temporal Information in Video Understanding Models and Datasets (CVPR 2018)](https://openaccess.thecvf.com/content_cvpr_2018/html/Huang_What_Makes_a_CVPR_2018_paper.html) — the direct methodological ancestor: ablate/shuffle temporal structure to test whether video models actually use it (often they don't).
- **What they did:** established order-destruction as the canonical test for claimed sequential-context use, in video.
- **Exact difference:** never applied to volumetric medical models; the "functionally 2.5D" verdict for specific 3D architectures is unpublished.
- **Remaining novelty:** the empirical answer for 3D medical segmentation (which claimed-volumetric models notice slice permutation), plus its implication for compute budgets.
- **Mutation:** frame explicitly as the medical instantiation of Huang et al.: permutation/reversal/interleave suite across nnU-Net-3D, Swin-UNETR-class models; report volumetric-sensitivity scores against 2.5D baselines.

### C-0332 — Mask-the-lesion occlusion audit
**Verdict: KILL** (confidence: high)
- **Kill cite:** [Mask of Truth: Model Sensitivity to Unexpected Regions of Medical Images (arXiv 2412.04030)](https://arxiv.org/abs/2412.04030) + [RoentMod: synthetic chest X-ray modification to identify and correct shortcuts (npj Digital Medicine 2026)](https://doi.org/10.1038/s41746-026-02497-6).
- **What they did:** Mask of Truth runs exactly this audit — mask the clinically relevant region, show models still classify above chance (sometimes *better* without the ROI), across chest X-ray and fundus tasks, with SHAP/embedding analysis and a radiologist control; RoentMod does the counterfactual add/remove-finding version at scale and fixes models with it.
- **Exact difference:** the survivor proposed the same occlusion control "applied systematically to detection papers" — the methodology, findings, and even the remediation are published.
- **Remaining novelty:** marginal (breadth across more papers).
- **Confidence:** high.

---

## Returns

### Counts
- **KILL: 17** — A-0118, A-0301, A-0313, A-0328, A-0336, B-0064, B-0081, B-0121, B-0129, B-0132, B-0177, B-0223, C-0072, C-0149, C-0249, C-0261, C-0332
- **MUTATE: 38**
- **KEEP: 1** — C-0206

### 10 strongest survivors (KEEP or high-value MUTATE)
1. **C-0206** — physics floor for boundary error (only clean KEEP; computable bound, no prior formalization found).
2. **B-0318** — mask-supervised feed-forward volumetric smoke (Global Transport is per-scene multi-view; the amortized single-view claim is open).
3. **A-0278** — pooled cross-domain mask-MAE prior (ACNN/Post-DAE are single-anatomy; foundation-scale label-space prior untested).
4. **B-0300** — objectness erosion in promptable models under domain-adaptive continued pretraining (SDD/DINOv3 prove the generic phenomenon, not the SAM-recipe conflict).
5. **A-0052 + B-0114 + B-0306** (merged PEFT-statistics program) — seed-level bias-variance decomposition and crossover law for dense PEFT.
6. **B-0286** — subgroup regression audit for dense medical fine-tuning (fairness literature is classification-only).
7. **B-0217** — detector-matched box-to-mask error transfer function (BREPS/PP-SAM perturb generically).
8. **A-0041** — CoT-faithfulness with the mask as dependent variable (Turpin-style interventions unapplied to dense outputs).
9. **B-0033** — text-only causal decomposition of tail open-vocabulary failure.
10. **A-0124** — five-way confusable-aerosol benchmark with human frame-vs-clip floors.

### 10 killed, with the killing paper
| Idea | Killed by |
|---|---|
| A-0118 hallucinated removed organs | [HALOS (IPMI 2023, arXiv 2303.07717)](https://arxiv.org/abs/2303.07717) |
| A-0301 cyclic-domain re-adaptation | [ReservoirTTA (arXiv 2505.14511)](https://arxiv.org/abs/2505.14511) |
| A-0328 simulated-click validity | [RClicks (NeurIPS 2024, arXiv 2410.11722)](https://arxiv.org/abs/2410.11722) |
| A-0336 human floors/ceilings | [Panoptic Segmentation (arXiv 1801.00868)](https://arxiv.org/abs/1801.00868) |
| B-0064 UDA vs frozen VFM features | [What is the Added Value of UDA in the VFM Era? (arXiv 2504.18190)](https://arxiv.org/abs/2504.18190) |
| B-0129 info-absent vs decoder-limited | [Frozen FM Embeddings Discard Small-Lesion Signal (arXiv 2606.11606)](https://arxiv.org/abs/2606.11606) |
| B-0132 layer-wise localization decay | [Blind to Position, Biased in Language (arXiv 2509.23098)](https://arxiv.org/abs/2509.23098) |
| B-0177 restain-register IHC ground truth | [Bulten et al. (Scientific Reports 2019)](https://www.nature.com/articles/s41598-018-37257-4) |
| B-0223 assigner bias vs elongated objects | [Slender Object Detection (arXiv 2011.08529)](https://arxiv.org/abs/2011.08529) |
| C-0261 grid-phase sensitivity | [Phase Marginalization for Patch-Grid Instability (arXiv 2606.08132)](https://arxiv.org/abs/2606.08132) |

(Also killed: A-0313 by SNIP/SAHI; B-0081 by Kofler/Metrics-Reloaded + radiotherapy metric-utility literature; B-0121 by Probing-3D-Awareness/Battle-of-Backbones/AM-RADIO; C-0072 by Cirik et al. 2018; C-0149 by European Radiology 2025 orientation/laterality QA; C-0249 by Probabilistic U-Net/SSN; C-0332 by Mask of Truth.)

*End of Stage-3 prior-art attack, set 2.*
