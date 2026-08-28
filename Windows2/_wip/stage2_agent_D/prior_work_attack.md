# Adversarial Prior-Work Attack — Batch C High-ROI Set

Agent D (Reviewer + Novelty Assassin). Date: 2026-08-28.

Default belief applied throughout: **"this idea was already done."** Every entry below started from an attempt to kill the idea with real literature found via web search. No citations are invented; where I could not verify a paper, I say so. Epistemic labels: **KNOWN** (verified from retrieved sources), **EVIDENCE** (retrieved source supports but does not settle), **HYPOTHESIS** (my inference).

Coverage: the 15 mandatory IDs from the C report, plus 4 ideas I personally rank at or above them (W2-C-0306, 0309, 0326, 0338/0344 treated jointly where noted).

Verdict tally (mandatory 15): **SURVIVE 7 / MUTATE 8 / KILL 0**. Extras: SURVIVE 4, MUTATE 1.

---

## 1. W2-C-0046 — Annotation-noise-propagated confidence intervals for COCO AP

**Closest prior works**
- *Benchmarking Object Detectors with COCO: A New Path Forward* (COCO-ReM), V. Jain et al., ECCV 2024. https://arxiv.org/abs/2403.18819 — KNOWN: re-annotated COCO masks (imprecise boundaries, non-exhaustive instances, mislabels); evaluating 50 detectors on COCO-ReM **changes model rankings** vs COCO-2017.
- *Accounting for Variance in Machine Learning Benchmarks*, X. Bouthillier et al., MLSys 2021. https://proceedings.mlsys.org/paper_files/paper/2021/hash/0184b0cd3cfb185989f858a1d9f5c1eb-Abstract.html — KNOWN: models the full benchmark variance budget (data sampling, init, HPO) for classification-style tasks; shows conclusions often driven by arbitrary factors.
- Practitioner-level bootstrap-CI tooling for detection exists (e.g., the open-source ConfidenceIntervals toolkit by L. Ferrer & P. Riera, https://github.com/luferrer/ConfidenceIntervals) — EVIDENCE that sampling-error CIs are commodity.

**What they did:** COCO-ReM fixed the annotations and showed ranking changes; Bouthillier et al. built a variance budget without an annotation-noise component; bootstrap tools give sampling CIs only.

**Exact difference:** Nobody propagates *annotation noise* (double-annotation disagreement distributions) into a CI on COCO AP and then audits published deltas against that interval. COCO-ReM shows the effect exists but offers a corrected dataset, not an uncertainty calculus.

**Remaining novelty:** The propagation machinery + claim-level audit ("X% of published COCO improvements are within the annotation-noise band"). Medium-sized but real.

**Novelty confidence:** **Medium.**

**Reviewer #2 attack:** "COCO-ReM already showed annotation errors change rankings; your CIs are just a reformulation" + Bouthillier citation for the variance-budget idea.

**Verdict: MUTATE.**
**Mutated one-liner:** *The annotation-noise band of COCO AP: propagating double-annotation disagreement into confidence intervals that published deltas must clear.*
**New hypothesis:** When annotation noise measured on double-annotated subsets is propagated into COCO AP intervals, a large fraction of recent published method-over-baseline deltas falls inside the interval, and the fraction is largest for AP-small and highest-IoU strata.

---

## 2. W2-C-0136 — Seed variance vs published deltas: how much of the detection leaderboard is luck

**Closest prior works**
- *Accounting for Variance in Machine Learning Benchmarks*, Bouthillier et al., MLSys 2021 (URL above). KNOWN: multi-source variance study across five deep-learning tasks; recommends randomizing many sources; classification-centric.
- *torch.manual_seed(3407) is all you need*, D. Picard, arXiv:2109.08203, 2021. KNOWN genre: seed sensitivity of ImageNet-scale classification.
- *Randomness Is the Root of All Evil: More Reliable Evaluation of Deep Active Learning*, Y. Ji et al., WACV 2023. https://openaccess.thecvf.com/content/WACV2023/papers/Ji_Randomness_Is_the_Root_of_All_Evil_More_Reliable_Evaluation_WACV_2023_paper.pdf — KNOWN: randomness taxonomy, AL-focused.

**What they did:** Established seed/HPO variance magnitudes for classification, RL, AL; recommended reporting standards. None measured seed variance of standard *detection* training pipelines, and none compared the variance distribution against the *distribution of published method deltas* in detection.

**Exact difference:** The detection instantiation and the leaderboard-luck comparison (variance vs. a census of claimed deltas) are both missing.

**Remaining novelty:** High — the field's most-cited "detection deltas are ~0.2–0.5 AP" folk claim has no published variance backing.

**Novelty confidence:** **High.**

**Reviewer #2 attack:** "Bouthillier et al. already told us variance matters; this is a task-specific replication." Rebuttal is the delta-census pairing and detection-specific variance components (BN, data-loader order, NMS ties).

**Verdict: SURVIVE.**

---

## 3. W2-C-0283 — Stale baselines: how much of reported detection progress is baseline decay

**Closest prior works**
- *A Metric Learning Reality Check*, K. Musgrave, S. Belongie, S.-N. Lim, ECCV 2020. https://arxiv.org/abs/2003.08505 — KNOWN: with fair tuning and a level playing field, 2006–2019 metric-learning methods perform near-identically; claimed progress largely evaporates.
- *Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches*, M. Ferrari Dacrema, P. Cremonesi, D. Jannach, RecSys 2019 (verified via citation in Musgrave's reference list). KNOWN: most neural recsys methods lose to tuned simple baselines.

**What they did:** Re-ran baselines with honest tuning in metric learning and recommender systems; found progress narratives collapse.

**Exact difference:** The genre exists and is famous — but no one has run it on *object detection* papers (re-train 20 papers' baselines under the papers' own tuning budgets). Detection has unique confounds (schedules, resolution, NMS settings) that make the audit non-trivial and non-derivative.

**Remaining novelty:** The detection instantiation + the "baseline decay rate" quantification over time.

**Novelty confidence:** **Medium-High** (genre precedent both legitimizes and erodes).

**Reviewer #2 attack:** "Musgrave et al. and Dacrema et al. already established this pattern; nothing new conceptually." Pre-registered paper selection and a decay-over-time model are the differentiators.

**Verdict: SURVIVE** (mandatory positioning against both precedents).

---

## 4. W2-C-0328 — A 1k-image subset ranks detectors as well as the full benchmark

**Closest prior works**
- *tinyBenchmarks: evaluating LLMs with fewer examples*, F. Maia Polo et al., ICML 2024. https://arxiv.org/abs/2402.14992 — KNOWN: IRT-based selection of ~100 anchor examples reproduces LLM benchmark scores within ~2%.
- *Anchor Points: Benchmarking Models with Much Fewer Examples*, R. Vivek et al. (EACL 2024; verified via citation inside tinyBenchmarks). KNOWN: clustering model-confidence patterns to pick representative examples.
- *How Reliable is Language Model Micro-Benchmarking?*, arXiv 2510.08730 — KNOWN: micro-benchmarks fail to resolve models closer than ~3.5 points; a warning for smallest subsets.

**What they did:** Built subset-selection machinery for LLM/classification benchmarks with IRT and clustering; quantified reliability limits.

**Exact difference:** No detection version exists. Detection adds structure the LLM work lacks (per-image multi-instance outcomes, size/density strata) — but the intellectual move is imported wholesale.

**Remaining novelty:** Low as a standalone; real as the applied half of an IRT-for-detection paper (W2-C-0309).

**Novelty confidence:** **Low-Medium.**

**Reviewer #2 attack:** "This is tinyBenchmarks for COCO" — nearly unanswerable if submitted standalone.

**Verdict: MUTATE.**
**Mutated one-liner:** *Merge into W2-C-0309: an IRT model of COCO that yields ability scores, misfit-item audits, and — as one application — a 1k-image short test.*
**New hypothesis:** An IRT model fitted to per-instance outcomes of 30 public detectors compresses COCO ranking into a 1k-image short test (rank r > 0.95) *and* flags misfit items that are disproportionately annotation errors (checkable against COCO-ReM).

---

## 5. W2-C-0032 — AP-rare on LVIS is statistically unstable at current test sizes

**Closest prior works**
- *LVIS: A Dataset for Large Vocabulary Instance Segmentation*, A. Gupta, P. Dollár, R. Girshick, CVPR 2019. https://arxiv.org/abs/1908.03195 — KNOWN: the LVIS paper itself refuses to release per-category AP because "there will be few examples ... which makes per-category AP unstable," and shows AP drifting with evaluation-set size.
- *Evaluating Large-Vocabulary Object Detectors: The Devil is in the Details*, A. Dave, P. Dollár, D. Ramanan, A. Kirillov, R. Girshick, arXiv:2102.01066, 2021. https://arxiv.org/abs/2102.01066 — KNOWN: the detections-per-image cap makes AP-rare sensitive to cross-category score ranking; +2.9 AP-rare from a ranking policy change alone, "roughly the magnitude achieved by a typical new method published at CVPR."

**What they did:** Documented AP-rare fragility mechanisms (sample size, detection caps, cross-category ranking) and proposed AP-Fixed/AP-Pool.

**Exact difference:** The instability is KNOWN; what's missing is the *significance audit of published long-tail claims* against bootstrap distributions of AP-rare — i.e., turning the known instability into a verdict on the literature.

**Remaining novelty:** Only the audit framing.

**Novelty confidence:** **Low** for the phenomenon, **Medium** for the audit.

**Reviewer #2 attack:** Direct citation of Dave et al. 2021 — "the devil-in-the-details paper already showed AP-rare gains are artifacts of evaluation details."

**Verdict: MUTATE.**
**Mutated one-liner:** *The AP-rare significance audit: bootstrap minimum-detectable-effects for LVIS tail metrics vs. every published long-tail delta since 2020.*
**New hypothesis:** A majority of published AP-rare improvements on LVIS are smaller than the bootstrap minimum detectable effect at their evaluation size, and the fraction is higher for papers that also gained under the Dave et al. ranking-policy artifact.

---

## 6. W2-C-0226 — Does super-resolution help detection or just fool metrics

**Closest prior works**
- *Task-Driven Super Resolution: Object Detection in Low-resolution Images*, M. Haris, G. Shakhnarovich, N. Ukita, arXiv:1803.11316 (2018). https://arxiv.org/abs/1803.11316 — KNOWN: SR trained with detection loss improves low-res detection; assumes SR helps and optimizes it.
- *Better to Follow, Follow to Be Better: Feature Super-Resolution for Small Object Detection*, J. Noh et al., ICCV 2019. https://openaccess.thecvf.com/content_ICCV_2019/papers/Noh_Better_to_Follow_Follow_to_Be_Better_Towards_Precise_Supervision_ICCV_2019_paper.pdf — KNOWN: feature-level SR gains for small objects.
- *Small Object Detection Leveraging on Simultaneous Super-resolution*, Hong et al., 2021 (skyearth.org PDF) and *Feature-Driven Super-Resolution for Object Detection*, arXiv:2004.00554 — KNOWN: more of the SR-helps-detection genre.

**What they did:** A whole literature reports SR→detection gains, almost always measured against annotations made on (or transferred to) the degraded/original imagery — none separates *recovered true information* from *hallucinated structure that happens to move the metric*.

**Exact difference:** The controlled protocol (start from true HR with GT, downsample, SR back, score SR-input detections against HR ground truth, decompose deltas into recovered vs hallucinated) does not appear in the retrieved literature.

**Remaining novelty:** The accounting protocol and the hallucination decomposition. This also hosts 0227/0230/0248 as sub-analyses.

**Novelty confidence:** **Medium-High** for the protocol; the headline "SR sometimes helps" is KNOWN and cannot be the claim.

**Reviewer #2 attack:** "SR-for-detection is a well-studied area with positive results (Haris et al.; Noh et al.) — what is new?" Must answer: none of them can distinguish truth from hallucination because none had HR ground truth in the loop.

**Verdict: MUTATE.**
**Mutated one-liner:** *Ground-truth-controlled accounting of SR for detection: how much of the AP gain is recovered information vs metric-fooling hallucination.*
**New hypothesis:** Under the HR-controlled protocol, a substantial share of the measured AP gain from generative SR models comes from detections with no support in the true HR image (hallucinations), and the share grows with generative prior strength while classical SR shows near-zero hallucination share.

---

## 7. W2-C-0082 — Mapping where SAM zero-shot actually works: a falsification atlas

**Closest prior works**
- *SAM Struggles in Concealed Scenes — Empirical Study on "Segment Anything"*, G.-P. Ji et al., Science China Information Sciences, 2023. https://arxiv.org/abs/2304.06022 — KNOWN: SAM fails on camouflage, industrial defects, medical lesions.
- *SAM-Adapter: Adapting Segment Anything in Underperformed Scenes*, T. Chen et al., ICCV Workshops 2023. https://openaccess.thecvf.com/content/ICCV2023W/VCL/papers/Chen_SAM-Adapter_Adapting_Segment_Anything_in_Underperformed_Scenes_ICCVW_2023_paper.pdf — KNOWN: quantifies SAM deficits on camouflage/shadow and fixes with adapters.
- *Comprehensively Evaluate SAM and SAM 2 ... Context-Dependent Concepts*, arXiv:2412.01240, 2024. https://arxiv.org/abs/2412.01240 — KNOWN: 11 context-dependent concepts, 2D/3D/video, prompt-robustness testing.
- *How to build the best medical image segmentation algorithm using foundation models*, arXiv:2404.09957, 2024 — KNOWN: exhaustive SAM-in-medical empirical study.

**What they did:** Collectively, the "where SAM fails" atlas already exists piecewise and is converging on comprehensive (the 2412.01240 evaluation is close to exactly this idea).

**Exact difference:** Only a *quantitative failure-prediction law* (predicting SAM failure from measurable image/object properties — contrast, boundary strength, texture similarity — validated out-of-domain) would go beyond the existing catalogues.

**Remaining novelty:** Low for the atlas; medium for a validated failure-prediction model.

**Novelty confidence:** **Low** (atlas), **Medium** (prediction law).

**Reviewer #2 attack:** Cites 2412.01240 and the concealed-scenes line: "this comprehensive evaluation already exists."

**Verdict: MUTATE.**
**Mutated one-liner:** *From atlas to law: a measurable-property model that predicts SAM/SAM-2 zero-shot failure before running the model, validated across unseen domains.*
**New hypothesis:** A small set of computable image/object properties (local contrast, boundary gradient energy, foreground-background texture similarity, object scale) predicts SAM zero-shot IoU with useful accuracy, transfers across domains, and outperforms domain labels as a failure predictor.

---

## 8. W2-C-0081 — Does better classification pretraining actually help dense tasks: a rank-correlation audit

**Closest prior works**
- *Battle of the Backbones*, M. Goldblum et al., NeurIPS 2023 Datasets & Benchmarks. https://arxiv.org/abs/2310.19909 — KNOWN: >1500 runs comparing pretrained backbones across classification, detection, segmentation, OOD, retrieval; cross-task Spearman correlations typically ρ > 0.8.
- *Do Better ImageNet Models Transfer Better?*, S. Kornblith, J. Shlens, Q. Le, CVPR 2019 (verified via BoB's discussion). KNOWN: near-linear ImageNet→downstream classification transfer.

**What they did:** BoB is a direct collision: it measures exactly the cross-task rank-correlation this idea proposes, finds it high, at scale, at a D&B venue.

**Exact difference:** BoB compares *different* backbones (architectures/pretraining mixes) — it does not run the *within-family, compute-matched* decorrelation test (same architecture, ordered classification checkpoints, does the ordering survive dense-task finetuning?), and it does not stratify by object size/density where dense tasks diverge most.

**Remaining novelty:** Only the within-family causal version.

**Novelty confidence:** **Low** as stated; **Medium** after mutation.

**Reviewer #2 attack:** "Battle of the Backbones already answered this with 1500 runs; ρ > 0.8."

**Verdict: MUTATE.**
**Mutated one-liner:** *Within one architecture family at matched compute, does classification-checkpoint quality still order detection performance — and where does the ordering break (size/density strata)?*
**New hypothesis:** Within-family rank correlation between ImageNet accuracy and COCO AP is much weaker than BoB's cross-family correlation, and inverts for AP-small, indicating classification pretraining quality is a poor selector once architecture is held fixed.

---

## 9. W2-C-0003 — Oracle-NMS ceiling: how much of crowded-scene error is suppression, not detection

**Closest prior works**
- *Learning Non-Maximum Suppression*, J. Hosang, R. Benenson, B. Schiele, CVPR 2017. https://openaccess.thecvf.com/content_cvpr_2017/papers/Hosang_Learning_Non-Maximum_Suppression_CVPR_2017_paper.pdf — KNOWN: NMS trade-off analysis in crowded scenes; learned Gnet beats tuned greedy NMS especially under heavy occlusion.
- *A convnet for non-maximum suppression*, J. Hosang et al., arXiv:1511.06437 — KNOWN: cites oracle analyses ("perfect NMS") indicating **NMS accounts for ~a quarter of the remaining detection problem**; oracle with perfect masks reaches 90% AR vs ~60% for greedy.
- *Sequential Context Encoding for Duplicate Removal*, L. Qi et al., NeurIPS 2018. https://arxiv.org/abs/1810.08770 — KNOWN: score-oracle and IoU-oracle duplicate-removal experiments show 10+ point headroom.
- *CrowdHuman*, S. Shao et al., arXiv:1805.00123, 2018 — KNOWN: NMS-threshold sensitivity in crowds is a founding motivation of the benchmark.

**What they did:** Oracle-suppression headroom analyses exist from 2015–2018 and motivated the learned-NMS and NMS-free lines.

**Exact difference:** All oracle analyses predate the DETR/NMS-free era and modern crowd benchmarks; nobody has re-decomposed crowded-scene error into suppression-vs-detection shares *for modern architectures including NMS-free ones* (where "suppression error" becomes query-competition error).

**Remaining novelty:** The modern re-decomposition only.

**Novelty confidence:** **Low** as stated; **Medium** after mutation.

**Reviewer #2 attack:** "Hosang et al. established the oracle-NMS ceiling years ago; DETR removed NMS anyway."

**Verdict: MUTATE.**
**Mutated one-liner:** *Re-run the oracle-suppression decomposition in the NMS-free era: does query competition in DETR-family models reproduce the same crowded-scene ceiling greedy NMS had?*
**New hypothesis:** On CrowdHuman, NMS-free models recover only part of the oracle-suppression headroom identified in the greedy-NMS era; the residual is attributable to query competition and is measurable by an analogous oracle substitution on assignment.

---

## 10. W2-C-0158 — Temperature scaling does not survive NMS: post-processing breaks calibration

**Closest prior works**
- *Multivariate Confidence Calibration for Object Detection*, F. Küppers, J. Kronenberger, A. Shantia, A. Haselhoff, CVPR Workshops 2020. https://openaccess.thecvf.com/content_CVPRW_2020/papers/w20/Kuppers_Multivariate_Confidence_Calibration_for_Object_Detection_CVPRW_2020_paper.pdf — KNOWN: detection calibration framework (D-ECE), position/scale-dependent calibration, applied to detector outputs.
- *Confidence Calibration for Object Detection and Segmentation*, Küppers et al., book chapter, 2022. https://doi.org/10.1007/978-3-031-01233-4_8 — KNOWN: detectors are intrinsically miscalibrated; extends scaling methods to detection.

**What they did:** Calibrate detector confidences *after* the standard pipeline (post-NMS detections), extending temperature/Platt/beta scaling with box features.

**Exact difference:** The retrieved literature calibrates post-NMS outputs; nobody isolates *NMS itself as a calibration-destroying transformation* — i.e., calibrate pre-NMS scores, pass through NMS, measure the induced miscalibration, and characterize the mechanism (selection bias of max-score survivors, a winner's-curse effect). HYPOTHESIS: the survivor-selection bias makes even perfectly calibrated pre-NMS scores overconfident post-NMS.

**Remaining novelty:** The mechanism study; zero-compute from cached candidates.

**Novelty confidence:** **Medium-High.**

**Reviewer #2 attack:** "Küppers et al. already calibrate detections; just calibrate after NMS and the problem is gone." Answer: post-hoc recalibration treats the symptom; the paper explains and quantifies the cause, which matters for any pipeline consuming pre-NMS scores.

**Verdict: SURVIVE.**

---

## 11. W2-C-0159 — Active learning for detection fails at realistic batch sizes: a multi-codebase replication

**Closest prior works**
- *Navigating the Pitfalls of Active Learning Evaluation*, C. Lüth et al., NeurIPS 2023. https://papers.nips.cc/paper_files/paper/2023/file/1ed4723f12853cbd02aecb8160f5e0c9-Paper-Conference.pdf — KNOWN: systematic AL-evaluation pitfalls (starting budget, query size, weak random baselines, HPO); *classification only*.
- *Randomness Is the Root of All Evil*, Y. Ji et al., WACV 2023 (URL above) — KNOWN: AL conclusions flip under randomness; classification.
- *Towards Robust and Reproducible Active Learning Using Neural Networks*, P. Munjal et al., CVPR 2022 (verified via citations in Lüth et al.) — KNOWN: strong tuned random baselines erase many AL gains; classification.
- *Streamlining the Development of Active Learning Methods in Real-World Object Detection*, arXiv:2508.19906 — KNOWN: notes AL-for-detection rankings vary across validation sets; proposes a proxy metric, not a replication audit.

**What they did:** Demolished AL evaluation practices for classification; detection AL papers keep publishing gains without equivalent scrutiny.

**Exact difference:** No multi-codebase replication of *detection* AL methods under realistic batch sizes and honest random baselines exists in the retrieved literature.

**Remaining novelty:** High — a straight transplant of a proven audit design into an unaudited subfield with expensive-labeling stakes.

**Novelty confidence:** **High** (for detection specifically).

**Reviewer #2 attack:** "Lüth et al. already did this" — answerable: they explicitly scope to classification; detection AL has different acquisition units (boxes vs images) and cost models.

**Verdict: SURVIVE.**

---

## 12. W2-C-0057 — Missing annotations punish better detectors: the unlabeled-object tax

**Closest prior works**
- *Object Detection as a Positive-Unlabeled Problem*, Y. Yang, K. Liang, L. Carin, BMVC 2020. https://arxiv.org/abs/2002.04672 — KNOWN: missing labels harm *training*; PU loss mitigates.
- *TIDE*, D. Bolya et al., ECCV 2020. https://arxiv.org/abs/2008.08115 — KNOWN: many of the most confident "background errors" are misannotated GT (50/100 for Mask R-CNN).
- *COCO-ReM*, ECCV 2024 (URL above) — KNOWN: exhaustive re-annotation changes model rankings; sharper-mask models were being penalized.
- *LVIS*, CVPR 2019 — KNOWN: federated/non-exhaustive annotation design exists precisely because exhaustive labeling is infeasible.

**What they did:** Established that missing annotations exist, harm training, and corrupt evaluation in aggregate.

**Exact difference:** The *differential* claim — that missing annotations penalize better models more (their correct extra detections score as FPs), so the evaluation error is anti-correlated with true quality and compresses/reorders leaderboards — has not been isolated with a controlled deletion design (synthetically remove annotations at known rates, measure per-model AP distortion as a function of model quality).

**Remaining novelty:** The controlled differential-effect design and the leaderboard-distortion estimate. COCO-ReM's ranking changes are EVIDENCE the effect is real, which de-risks the study while leaving the quantitative law unclaimed.

**Novelty confidence:** **Medium-High.**

**Reviewer #2 attack:** "COCO-ReM already showed rankings change with better annotations." Answer: they built a dataset; this measures the *law* (distortion vs missing-rate vs model quality), which generalizes beyond COCO.

**Verdict: SURVIVE.**

---

## 13. W2-C-0011 — Prompt-engineering variance exceeds architecture deltas in open-vocab detection

**Closest prior works**
- *Prompt Sensitivity in Vision-Language Grounding*, arXiv:2604.17126 (2026) — KNOWN: semantically equivalent prompts select different boxes in a DETR+CLIP grounding pipeline; instability is structured; small-scale (263 images, person class).
- *OV3D-Bench*, arXiv:2608.17110 (2026) — KNOWN: prompt-template robustness probes (CV% across 15 templates) for open-vocabulary *monocular 3D* detection; overdetailed prompts hurt all encoders.
- *The Devil is in the Fine-Grained Details*, L. Bianchi et al., CVPR 2024 — KNOWN: OVD evaluation weaknesses on fine-grained vocabularies.
- *OVDEval*, AAAI 2024 — KNOWN: OVD benchmark with hard negatives; NMS-AP metric fix.

**What they did:** Documented prompt sensitivity phenomena in grounding and 3D-OVD; built better OVD benchmarks. None ran the specific comparison: prompt-template variance vs *published architecture-to-architecture deltas* on the standard 2D OVD leaderboards (OV-COCO/OV-LVIS).

**Exact difference:** The leaderboard-relevance framing — "your +1.5 AP-novel is smaller than the spread induced by prompt choices your paper didn't report" — is unclaimed for 2D OVD.

**Remaining novelty:** The variance-vs-delta comparison across the actual method population; inference-only.

**Novelty confidence:** **Medium** (phenomenon known; comparison unclaimed; field moving fast — execute soon).

**Reviewer #2 attack:** Cites 2604.17126/OV3D-Bench: "prompt sensitivity is known." Answer: known ≠ quantified against the leaderboard's claimed margins on the benchmarks where methods are actually ranked.

**Verdict: SURVIVE** (with urgency flag).

---

## 14. W2-C-0116 — Detectors that see ghosts: hallucinated detections of removed objects

**Closest prior works**
- *The Elephant in the Room*, A. Rosenfeld, R. Zemel, J. Tsotsos, arXiv:1808.03305, 2018. https://arxiv.org/abs/1808.03305 — KNOWN: object *transplanting* causes non-local detection failures; context effects on detection are established.
- Context-dependence literature descending from it (co-occurrence reliance) — KNOWN in general terms.

**What they did:** Added objects and moved objects; showed non-local interference and context reliance. They did **not** remove objects via inpainting and measure *hallucinated re-detections* of the removed object from residual context.

**Exact difference:** Ghost-rate measurement (detector fires on an object that is no longer there, at the location its context predicts) is the inverse experiment; requires strict inpainting-artifact controls (matched inpainting of background regions as the null).

**Remaining novelty:** The ghost-rate benchmark and per-class context-dependence scores it yields.

**Novelty confidence:** **Medium** — the conceptual neighborhood is occupied; the specific instrument and quantity are not.

**Reviewer #2 attack:** "This is Elephant-in-the-Room with inpainting; context reliance is known." Also: "your ghosts are inpainting artifacts." The matched-background-inpainting control must be bulletproof.

**Verdict: MUTATE.**
**Mutated one-liner:** *Ghost-rate: a controlled removal benchmark measuring how often detectors re-detect objects that context predicts but pixels no longer support.*
**New hypothesis:** Ghost-rate is nonzero for all modern detectors, is largest for strongly context-bound classes (tie, keyboard, mouse), and correlates with co-occurrence statistics of the training set rather than with detector AP — making it an independent reliability axis.

---

## 15. W2-C-0327 — 2015 architecture, 2026 recipe: how much detection progress is training practice

**Closest prior works**
- *ResNet strikes back: An improved training procedure in timm*, R. Wightman, H. Touvron, H. Jégou, arXiv:2110.00476, 2021. https://arxiv.org/abs/2110.00476 — KNOWN: vanilla ResNet-50 hits 80.4% ImageNet top-1 with a modern recipe (vs 75–76% legacy), demonstrating recipe-share of classification progress is large.

**What they did:** The classification version, thoroughly. Detection-side, partial recipe-modernization exists inside various papers (longer schedules, stronger augmentation in baselines) but no dedicated attribution study re-training Faster R-CNN-class architectures under a curated modern recipe against matched modern architectures. (I did not find a detection equivalent in the searches; EVIDENCE of absence, not proof.)

**Exact difference:** The detection instantiation, plus detection-specific recipe dimensions (multi-scale training, large-scale jitter, pretrained-init provenance, longer schedules) whose contributions can be itemized.

**Remaining novelty:** High-value replication-with-extension; the classification precedent makes a large effect likely, which is the interesting outcome either way.

**Novelty confidence:** **Medium-High.**

**Reviewer #2 attack:** "ResNet-strikes-back for detection; derivative." Answer: attribution of a *decade of detection progress* is a field-level number nobody has produced; derivative genre, non-derivative conclusion.

**Verdict: SURVIVE.**

---

## Extra attacks — ideas I rank at/above parts of the mandatory list

### E1. W2-C-0306 — Coverage-preserving suppression: conformal prediction meets NMS

**Closest prior works**
- *Conformal Object Detection by Sequential Risk Control*, arXiv:2505.24038 (2025) — KNOWN: conformal OD pipeline that explicitly treats NMS "as part of the OD model itself," calibrating thresholds *after* suppression.
- *Probabilistic Object Detection with Conformal Prediction*, arXiv:2605.07549 (2026) — KNOWN: scaled/unscaled CP for detection on KITTI/BDD/CODA; NMS again upstream and untouched.

**What they did:** Built conformal guarantees on top of the post-NMS detection list. Both retrieved papers *assume* NMS and condition on its output.

**Exact difference:** Nobody measures the coverage that NMS destroys (true objects whose only covering candidates get suppressed) or designs suppression to preserve candidate-set coverage. The idea attacks the step the existing literature explicitly brackets out.

**Remaining novelty:** High and formal: a coverage-aware suppression rule with provable set-size/coverage trade-off.

**Novelty confidence:** **High** (but the area is moving fast — 2 conformal-OD papers in 12 months; execute soon).

**Reviewer #2 attack:** "Sequential Risk Control already gives guarantees despite NMS." Answer: their guarantee is on the post-NMS list — objects suppressed before calibration are invisible to their risk control; we quantify exactly that blind spot.

**Verdict: SURVIVE.**

### E2. W2-C-0309 — Item response theory for detection benchmarks

**Closest prior works:** tinyBenchmarks (ICML 2024) and Anchor Points (EACL 2024) — KNOWN, IRT/clustering for LLM benchmark compression; *Evaluation Examples Are Not Equally Informative* (P. Rodriguez et al., ACL 2021; known IRT-leaderboard line in NLP — not re-verified this session, flagged accordingly).
**Exact difference:** No IRT treatment of detection benchmarks; detection outcome matrices (per-instance TP/FN across models) plus misfit-item auditing against known annotation errors (COCO-ReM cross-check) is new territory.
**Remaining novelty:** Medium-high; the instantiation carries real new content (what "difficulty" and "discrimination" mean for instances; misfit ↔ annotation error).
**Novelty confidence:** **Medium-High.**
**Reviewer #2 attack:** "IRT for benchmarks is done (NLP)." Mandatory positioning; absorb W2-C-0328 as the application.
**Verdict: SURVIVE** (as host paper for 0328).

### E3. W2-C-0326 — Half the remaining COCO errors are not model errors

**Closest prior works:** TIDE (ECCV 2020) — KNOWN: of the top-100 most confident Mask R-CNN errors, ~30% (localization) to ~66% ("both") were misannotations; COCO-ReM (ECCV 2024) — KNOWN: systematic annotation repair changes rankings; ObjectLab (arXiv:2309.00832) — KNOWN: automated mislabel detection using model predictions.
**Exact difference:** TIDE sampled *top-confidence errors of one 2020 model*; no one has run a powered, two-annotator adjudication of a *stratified sample of all residual errors of a SOTA detector at deployment thresholds*, yielding a defensible field-level share.
**Remaining novelty:** The unbiased-share estimate; surprise value eroded, citation value intact.
**Novelty confidence:** **Medium** (phenomenon firmly KNOWN; the clean number is not).
**Reviewer #2 attack:** "TIDE already showed this in 2020."
**Verdict: SURVIVE** (barely; the design must emphasize stratified sampling + modern SOTA + inter-annotator protocol, and cite TIDE in the first paragraph).

### E4. W2-C-0338 / W2-C-0344 — The small-object ceiling is human, not machine / Instructions beat annotators

**Closest prior works:** *Can We Trust Bounding Box Annotations for Object Detection?*, J. Murrugarra-Llerena et al., CVPR Workshops 2022 — KNOWN: sub-pixel annotation discrepancies materially distort AP for small objects; recommends multi-annotator datasets. Krippendorff's-alpha annotation-quality methodology (arXiv:1912.10107) — KNOWN. Crowdsourcing instruction-clarity work (FIND-RESOLVE-LABEL, Frontiers in AI 2022) — KNOWN in HCI, image-labeling context.
**Exact difference:** (0338) No published human-re-annotation vs model agreement curves *by object size* locating the size floor where human-GT agreement equals model-GT agreement. (0344) Instruction effects on labels are studied in NLP/HCI crowdsourcing; no A/B instruction experiment measuring the effect on *detection GT and downstream AP of a fixed model* vs within-arm inter-annotator variance.
**Remaining novelty:** High for both; they share annotation infrastructure and could be one two-experiment paper on the epistemology of detection ground truth.
**Novelty confidence:** **High** (0338), **High** (0344).
**Reviewer #2 attack:** (0338) "Everyone knows tiny-object labels are noisy" — answer: knowing ≠ locating the falsifiability floor. (0344) "Crowdsourcing literature did instructions" — answer: not for detection GT, and never with model-AP deltas as the endpoint.
**Verdict: SURVIVE (both).**

---

## Summary table

| ID | Verdict | Novelty conf. | One-line disposition |
|----|---------|---------------|----------------------|
| W2-C-0046 | MUTATE | Med | Reframe as annotation-noise band + claims audit (COCO-ReM adjacency) |
| W2-C-0136 | SURVIVE | High | Detection seed-variance vs published-delta census is unclaimed |
| W2-C-0283 | SURVIVE | Med-High | Genre proven elsewhere; detection instantiation open |
| W2-C-0328 | MUTATE | Low-Med | Fold into 0309 (tinyBenchmarks collision) |
| W2-C-0032 | MUTATE | Low/Med | Instability known (LVIS, Dave et al.); survive only as significance audit |
| W2-C-0226 | MUTATE | Med-High | GT-controlled hallucination accounting is the surviving core |
| W2-C-0082 | MUTATE | Low/Med | Atlas exists; survive only as failure-prediction law |
| W2-C-0081 | MUTATE | Low/Med | BoB collision; survive only as within-family causal test |
| W2-C-0003 | MUTATE | Low/Med | Oracle analyses old; survive as NMS-free-era re-decomposition |
| W2-C-0158 | SURVIVE | Med-High | NMS as calibration destroyer unstudied (prior work calibrates post-NMS) |
| W2-C-0159 | SURVIVE | High | AL-audit precedents are classification-only |
| W2-C-0057 | SURVIVE | Med-High | Differential (anti-quality) effect unisolated; COCO-ReM de-risks |
| W2-C-0011 | SURVIVE | Med | Phenomenon known, leaderboard-margin comparison unclaimed; urgent |
| W2-C-0116 | MUTATE | Med | Elephant-in-the-Room adjacency; survive as ghost-rate with artifact controls |
| W2-C-0327 | SURVIVE | Med-High | ResNet-strikes-back precedent proves genre, not the detection number |
| W2-C-0306 (extra) | SURVIVE | High | Conformal-OD papers bracket NMS out; attack that step; urgent |
| W2-C-0309 (extra) | SURVIVE | Med-High | IRT-for-benchmarks exists in NLP; detection instantiation open |
| W2-C-0326 (extra) | SURVIVE | Med | TIDE showed the phenomenon; powered share estimate missing |
| W2-C-0338/0344 (extra) | SURVIVE | High | Ground-truth epistemology experiments unclaimed for detection |

Mandatory-15 counts: **7 SURVIVE, 8 MUTATE, 0 KILL.** No mandatory idea died outright, but five of the eight mutations were forced by direct collisions (BoB, Dave et al., tinyBenchmarks, SAM-evaluation literature, oracle-NMS line) that the batch-C one-liners did not acknowledge.
