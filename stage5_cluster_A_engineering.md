# Stage 5 — Cluster A Experimental Engineering (all 7 Stage-4 survivors)

**Experimental Engineer (Cloud Sub-Agent M) → Supervisor Windows7.**
**Input:** `stage4_cluster_A_keep.md` / `stage4_cluster_A_attacks.md` (branch `cursor/stage4-cluster-a-reviewer2-f1fa`), Stage-3 keeps/mutations (branch `cursor/stage3-cluster-a-priorwork-b0e5`), Stage-1 originals (branch `cursor/stage1-cluster-a-ideas-e2b2`). Cross-checked against Cluster B keeps (`cursor/stage4-cluster-b-reviewer2-b25a`) and Cluster C keeps (`cursor/stage4-cluster-c-reviewer2-c1be`) — none of the killer experiments below duplicate B/C killer experiments (B = evaluation-validity + synthetic-data + supervision-mining; C = training-mechanism causal tests + measurement instruments; A's seven are all SAM-family mechanism/diagnostic studies).

All cited codebases are real repositories verified by search this session. GPU estimates assume A100-40GB-class hardware unless noted; all wall-clock figures are compute runtimes, not schedules.

Ranking and nominees: `stage5_cluster_A_top.md`. ROI table: `stage5_cluster_A_roi.csv`.

---

## A-0002 — Point-prompt instability: spectral surgery on the prompt encoder's random Fourier features

**Research Question.** Is SAM's sub-pixel click-flip instability spectrally attributable to the prompt encoder's random-Fourier-feature (RFF) positional encoding (`PositionEmbeddingRandom`), as opposed to the 16-px patch grid / 64×64 dense image PE — and does the answer carry a machine-prompting consequence via AMG's fixed 32×32 prompt grid?

**Core Hypothesis.** Flip-map periodicity and flip rate are causally driven by the high-frequency rows of the point-path RFF matrix. Attenuating those rows at inference (image path untouched) reduces flips; the flip-map spectrum matches the exactly-known RFF spectrum rather than the 16-px grid comb.

**Falsifiable Prediction.**
- P1: Bandlimiting the top-20% |ω| rows of the point-path RFF reduces flip rate by ≥30% relative, while an equal-energy random-row attenuation control reduces it by <10%.
- P2: Measured 2-D flip spectra favor the RFF-predicted spectrum over the 16-px-grid comb in a preregistered model comparison (evidence ratio ≥3:1 on ≥70% of objects).
- P3: Shifting AMG's 32×32 prompt grid by a half period (8 px) changes per-image instance recall by ≥1 point on ≥20% of images.

**Method.**
1. Flip maps: for each object, cache the image embedding once, then replay the 4M-param decoder over a sub-pixel click grid (e.g., 0.25-px steps over a 16×16-px window around anchor clicks; anchors from mask centroid and from the RClicks clickability model). Flip = IoU between masks of neighboring clicks < 1−τ, τ swept {0.1…0.5}.
2. Spectral analysis: 2-D Fourier transform of flip indicator maps; fit two competing spectral models — (a) predicted from SAM's known Gaussian RFF matrix, (b) 16-px grid comb — via Whittle likelihood / AIC.
3. Path-specific spectral surgery: modify a *copy* of `PositionEmbeddingRandom` used only by `_embed_points` (the `get_dense_pe` image path keeps the original matrix), attenuating the top-k frequency rows. Control: attenuate random rows matched in total spectral energy. Zero retraining — this kills the Stage-4 retraining-confound attack by construction.
4. AMG grid-phase test: shift the point grid produced by `build_all_layer_point_grids` by sub-period offsets up to (8, 8) px; measure GT-instance recall and mask-set stability across phases.

**Architecture.** Stock SAM ViT-B/L/H. No new modules; surgery is a ~150-LOC runtime wrapper around the prompt encoder.

**Training.** None (inference-only by design).

**Loss.** N/A. Statistics: bootstrap CIs over objects for flip-rate deltas; Whittle-likelihood spectral model comparison.

**Data.** COCO_MVal (800 instances), DAVIS (345), TETRIS (2,531) — all packaged by the RClicks distribution; ≥500 objects sampled stratified by size and boundary complexity. AMG arm: COCO val2017 (2–5k images) + LVIS v1 val.

**Preprocessing.** Standard SAM longest-side-1024 resize. Clicks kept as floats end-to-end (SAM normalizes coordinates continuously; verify no int cast in the harness). Ambiguity covariate recorded per object (multimask spread, distance-to-boundary of anchor).

**Baselines.** (a) Equal-energy random-row attenuation (primary causal control); (b) input-image Gaussian blur matched to the same flip-rate reduction (trivial-smoothing account); (c) multimask-oracle selection (ambiguity account); (d) qualitative comparison with Stable-SAM's decoder-side account.

**Metrics.** Flip rate per object; 2-D flip-spectrum power at predicted frequencies; spectral evidence ratio; AMG recall and cross-phase mask-set stability (mean best-match IoU); guardrail: 1-click mIoU under surgery within ±0.3 of stock.

**Implementation Strategy.** Fork `segment-anything`; implement `SpectralSurgeryPromptEncoder`; batch thousands of decoder calls per cached embedding (decoder throughput makes the sweep cheap); analysis in numpy/scipy. First milestone: flip maps + spectra on 50 objects, ViT-B, all three surgery arms.

**Reusable codebases (verified real).**
- github.com/facebookresearch/segment-anything (`PositionEmbeddingRandom`, `_embed_points`, `SamAutomaticMaskGenerator`)
- github.com/emb-ai/rclicks (realistic click model; TETRIS/COCO_MVal/DAVIS packaging; eval harness)
- github.com/SysCV/sam-hq, github.com/ChaoningZhang/MobileSAM, github.com/facebookresearch/sam2 (fleet replication arms)

**GPU/VRAM/time estimate.** 1× A100-40GB (a 24GB 4090 suffices). Embedding cache for 500 images ≈ 0.1 GPU-h. Decoder sweeps: 500 objects × ~4k sub-pixel clicks × 7 arms ≈ 14M decoder calls ≈ 25 GPU-h. AMG phase arm: 2k images × 6 phases × ~15 s (ViT-H) ≈ 50 GPU-h (ViT-B: ~15 GPU-h). Total ≈ 80–100 GPU-h; peak VRAM ≤ 16 GB fp16.

**MVE (minimum viable experiment).** 50 objects, ViT-B, τ=0.3, three arms (top-k RFF, random-row control, no-op): does flip rate move under RFF surgery and not under the control? ≈ 4 GPU-h. Go/no-go before anything else.

**Full experiment.** ≥500 objects × ViT-B/L/H × 7 arms × τ-sweep; spectral model comparison; AMG phase test on COCO+LVIS; fleet replication (SAM-HQ, MobileSAM — shared decoder lineage; SAM2 image mode — different encoder).

**Ablation.** Attenuation strength (top-k ∈ {5,10,20,40}% of rows; factors {0, 0.25, 0.5}); τ; anchor policy (centroid vs RClicks vs uniform); object-size strata; positive-click count (1 vs 3).

**Control.** Equal-energy random-row attenuation; blur-matched input control; determinism check (decoder replay is deterministic, so the flip-map noise floor is ≈0 — any spectral structure is signal).

**Robustness.** Multimask on/off; two input resolutions (the 16-px-grid hypothesis predicts the flip period scales with patch size; the RFF hypothesis predicts it does not — an extra discriminating lever).

**Generalization.** Fleet table: RFF-attributable flip share across SAM B/L/H, SAM-HQ, MobileSAM, EfficientSAM, SAM2 — does the mechanism track prompt-encoder lineage or decoder lineage?

**Failure analysis.** If surgery does nothing: stratify flips by ambiguity covariates (ambiguity-driven account); test whether spectra match the patch-grid comb instead → publishable redirect ("instability lives in the image path"). If the blur control matches surgery: generic smoothing, mechanism not specific — report as such.

**Expected Result (HYPOTHESIS, not measured).** RFF surgery cuts flip rate 30–60% on ambiguity-controlled objects at <0.5 mIoU cost; spectra favor the RFF model; AMG half-period shifts move per-image recall 1–3 points on 20–40% of images — prompt-encoding aliasing established as a real, fixable mechanism with an auto-annotation consequence.

**Negative interpretation.** Insensitivity to point-path surgery + patch-grid-matching spectra = clean attribution negative that redirects robustness work to image tokenization and kills the prompt-encoder folklore. Neither spectral model fitting = ambiguity-dominated flips; report as a bounded nuisance with the released flip-map toolkit.

**Stop condition.** MVE shows <5% relative flip-rate delta under maximal safe surgery AND inconclusive spectral comparison (evidence ratio <3:1) → stop; publish short negative note + toolkit.

**Killer Experiment.** One inference-only battery on the same ≥500 objects: (i) point-path-only RFF bandlimit vs (ii) equal-energy random-row control vs (iii) quantitative spectral predictions of both hypotheses (known RFF matrix vs 16-px comb), plus (iv) the AMG half-period phase shift. Simultaneously tests causality (i vs ii), attribution (iii), and consequence (iv) in ≈30 GPU-h.

**Research ROI: 8.0 / 10.** Cheapest full-causal design in the cluster; both outcomes settle an attribution question two prior papers gestured at; main discount: phenomenon significance is mid-tier even with the AMG hook.

---

## A-0017 — Causal memory surgery for SAM2: a validated upper-bound diagnostic

**Research Question.** How much of organic SAM2 long-video tracking failure is memory-borne (reversible by targeted deletion of post-error memory entries) vs representation-borne — and does the per-sequence reversible fraction predict the per-sequence gains of independent prevention methods (SAMURAI, DAM4SAM)?

**Core Hypothesis.** A large fraction of organic failures is reversible under oracle-timed targeted deletion; targeted deletion beats a full reset (pre-error memories are load-bearing); and the reversible fraction predicts prevention-method gains — establishing surgery as a decomposition instrument, not a repair heuristic.

**Falsifiable Prediction.**
- P1: Targeted-deletion recovery rate exceeds no-op by ≥30 points on protocol-harvested failures.
- P2: Targeted deletion beats full-reset-to-conditioning-frame by ≥10 points of recovery (otherwise "surgery" collapses into "reset").
- P3 (preregistered kill-shot): per-sequence reversible fraction predicts per-sequence J&F gains of SAMURAI *and* DAM4SAM with r > 0.6.

**Method.**
1. Failure harvesting (fixed protocol, zero curation): run SAM2.1 (Hiera-B+ and Hiera-L) semi-supervised VOS over LVOS v2 val (140 videos) + DiDi (distractor-distilled set from the DAM4SAM release). Failure event = per-frame IoU < 0.1 for ≥ k consecutive annotated frames after having been ≥ 0.5 earlier (k preregistered). All failures enter; ambiguous-reappearance cases form a preregistered stratum reported separately (kills the cherry-picking attack).
2. Surgery arms at the GT recovery-opportunity frame t_r: (i) **targeted deletion** — remove memory entries written after failure onset, keep the permanently retained conditioning-frame memory and pre-error object memories; (ii) **full reset** — conditioning-frame memory only (the trivial baseline); (iii) **no-op**. Replay from t_r; recovery = IoU ≥ 0.5 within w frames, sustained.
3. Memory-attention analysis (absorbs killed A-0016): log cross-attention mass from current-frame queries to each memory entry before/after surgery — quantifies competition between retained good memory and post-error entries.
4. Predictive validity: run SAMURAI and DAM4SAM (both training-free SAM2.1 wrappers) on the same sequences; regress their per-sequence gains on the reversible fraction.

**Architecture.** Stock SAM2.1 checkpoints. Surgery = a `MemorySurgeon` wrapper (~300 LOC) exposing delete/keep operations over the video predictor's per-frame memory-bank state (memory features + object pointers). No weights touched.

**Training.** None.

**Loss.** N/A.

**Data.** LVOS v2 val (public dense GT, long-term), DiDi (go.vicos.si/didi, linked from the DAM4SAM repo); optional SA-V val scale-out. GT reappearance frames from dense annotations.

**Preprocessing.** Standard SAM2 VOS protocol; LVOS handled with the `--track_object_appearing_later_in_video` convention documented in SAM2/SAM2Long tooling.

**Baselines.** No-op (natural recovery); full reset (the reviewer's "decades-old heuristic" arm); count-matched random-entry deletion (specificity of *which* entries); SAMURAI/DAM4SAM as comparators for validity, not competitors.

**Metrics.** Recovery rate per arm; time-to-recovery; post-recovery J&F (lvos-evaluation toolkit); per-sequence reversible fraction; predictive-validity r (Pearson + Spearman, bootstrap CIs); attention-mass shift pre/post surgery; ambiguity-stratified everything.

**Implementation Strategy.** Fork `sam2`; implement surgery hooks over the inference-state memory dict; harvesting + replay harness; comparator repos used as released (both are SAM2.1-based and training-free, so per-sequence gains are directly attributable to memory handling).

**Reusable codebases (verified real).**
- github.com/facebookresearch/sam2 (video predictor, memory bank)
- github.com/yangchris11/samurai (motion-aware memory selection, training-free)
- github.com/jovanavidenovic/DAM4SAM (distractor-aware memory + DiDi dataset)
- github.com/Mark12Ding/SAM2Long (optional third comparator: training-free memory tree)
- github.com/LingyiHongfd/LVOS + github.com/LingyiHongfd/lvos-evaluation (data + J&F scoring)

**GPU/VRAM/time estimate.** 1× A100-40GB. Harvest pass ≈ 320 videos ≈ 12 GPU-h (Hiera-L). Surgery replays: ≥200 failures × 3–4 arms × partial replays ≈ 25 GPU-h. Comparator passes (SAMURAI + DAM4SAM + optional SAM2Long) ≈ 35 GPU-h. Attention logging ≈ +20%. Total ≈ 80–120 GPU-h; peak VRAM ≈ 16–24 GB.

**MVE.** 20 harvested failures, Hiera-B+, three arms: does the surgery machinery replay correctly and produce a targeted-vs-reset gap? ≈ 8 GPU-h once hooks exist.

**Full experiment.** ≥200 failures across LVOS v2 + DiDi; all arms; both backbones; predictive-validity regression; ambiguity strata; memory-attention analysis; headroom table (share of the surgical ceiling each prevention method captures).

**Ablation.** Deletion scope (all post-error vs recent-k vs object-pointers-only vs spatial-features-only); surgery timing t_r ± δ (dose-response in oracle strength — quantifies how strong the oracle needs to be); recovery window w.

**Control.** Count-matched random-entry deletion; sham surgery at random non-failure times (must not change tracking — harness validity); replay determinism check.

**Robustness.** Failure-definition sweep (IoU<0.1 vs <0.3; k); backbone size; with/without ambiguous stratum; SAM2 vs SAM2.1 checkpoints.

**Generalization.** Does the diagnostic transfer to SAM2Long (its memory tree should reduce the memory-borne share if its mechanism story is right)? Optional EfficientTAM replication.

**Failure analysis.** Classify irreversible failures: re-detection failure (no multimask proposal overlaps GT at t_r) vs mis-association (locked distractor outvotes retained memory) via the attention logs — does conditioning-frame attention collapse (interference) or persist-but-outvoted (competition)?

**Expected Result (HYPOTHESIS, not measured).** Reversible fraction 40–70%; targeted beats reset by ≥10 points; reversible fraction predicts SAMURAI/DAM4SAM per-sequence gains at r ≈ 0.6–0.75; prevention methods capture only 50–70% of the surgical ceiling — the field gets its first validated upper-bound diagnostic and a measured headroom number.

**Negative interpretation.** Targeted ≈ reset → the decomposition collapses to "reset works"; still bounds the memory-borne share, published as a diagnostic post-mortem. r < 0.3 → the instrument does not measure what prevention methods exploit; preregistered negative published with the harvested failure corpus + surgery toolkit (both reusable). High no-op recovery → SAM2.1's natural recovery is underrated; benchmark finding.

**Stop condition.** After a 50-failure pilot: targeted-vs-reset gap < 3 points AND pilot predictive validity r < 0.2 → stop before comparator passes; release corpus + tooling as a tech note.

**Killer Experiment.** The preregistered two-part shot on ≥200 organic failures: (1) three-arm surgery — targeted must beat both no-op (≥30 pts) and full reset (≥10 pts); (2) reversible fraction must predict per-sequence gains of two independent prevention methods at r > 0.6. Either miss kills the instrument claim; both passing makes it the reference diagnostic for the SAM2-memory subfield. ≈ 60 GPU-h.

**Research ROI: 9.0 / 10.** Zero training, hottest model family, decisive preregistered validity test, informative in every branch; main discount: scooping risk in a fast-moving subfield.

---

## A-0061 — Boundary Nyquist: is the empirical cutoff at, or far below, the decoder's sampling limit?

**Research Question.** Where in contour-frequency space does segmentation boundary error concentrate, and does the empirical cutoff sit at each decoder's theoretical sampling limit (sampling-limited regime) or well below it (training-limited regime)?

**Core Hypothesis.** Decoders have a measurable contour-frequency cutoff; for SAM-family decoders the cutoff sits ≥1 octave below the architectural Nyquist — i.e., they are training/data-limited at boundaries, so raising decoder resolution alone buys little.

**Falsifiable Prediction.**
- P1: Error-energy-vs-contour-frequency curves show an identifiable knee per model (segmented regression R² ≥ 0.8 on synthetic stimuli).
- P2: Sampling-limited world: cutoff shifts ≈1 octave when output resolution doubles across models/paths. Training-limited world: cutoff insensitive to resolution and similar across architectures. The two worlds are mutually exclusive and both measurable.
- P3: HQ-SAM's high-res token path either raises the cutoff by the predicted octave or sharpens *below* the SAM cutoff — directly scoring the HQ line's mechanism.

**Method.**
1. Synthetic parametric contour suite (~3k stimuli): star/blob families r(θ) = r₀(1 + Σ aₖcos(kθ+φₖ)) with controlled curvature spectra up to k=128, plus band-passed-noise blobs; anti-aliased rendering at 2048² with textured fg/bg composites; analytic GT contours (in-distribution sanity gate: 1-click IoU > 0.9 on low-frequency versions).
2. Prompt each model (box + center click); extract predicted contours at the native logit resolution (marching squares before binarize-and-upsample) and after the standard pipeline — locating where frequency content is destroyed.
3. Per-harmonic error transfer function: error energy per Fourier-descriptor harmonic between predicted and GT radial functions; effective-order analysis (order at which truncated GT best matches the prediction).
4. Natural-data arm: DIS-5K fine masks (reference bandwidth exceeds the models'), simple-topology instances only; arc-length windowed spectral analysis.
5. Compare empirical cutoffs to each architecture's theoretical limit: SAM 256²-logit path (64² tokens → two transposed convs), HQ-SAM HQ-token path, SAM2 image mode, Mask2Former Swin-L (1/4-res pixel embedding).

**Architecture.** Stock checkpoints only: SAM ViT-B/L/H, SAM-HQ, SAM2 Hiera-L, Mask2Former Swin-L (COCO instance). No new modules. (Optional non-core extension: shallow decoder retrain at two resolutions if the training-limited verdict lands and confirmation is wanted.)

**Training.** None in the core design.

**Loss.** N/A.

**Data.** Synthetic suite (released as an artifact); DIS-5K (5,470 images, eval-only); ThinObject-5K optional. COCO polygons explicitly excluded from references (annotation-bandwidth attack).

**Preprocessing.** Stimuli rendered 2048² → per-model native input; natural images via standard per-model pipelines; contour extraction with skimage marching squares; topology filter for the natural arm.

**Baselines.**
- **Oracle grid-resampling (the crux):** GT masks passed through each decoder's own output grid (downsample to logit resolution, upsample back) — the pure sampling bound with no model in the loop.
- Human re-annotation floor on a 100-stimulus subset (measurable-frequency ceiling of the reference).
- Theoretical Nyquist per spec sheet.

**Metrics.** Per-harmonic error energy; cutoff frequency (knee via segmented regression); cutoff-to-Nyquist ratio per model; octave-shift test across resolutions; boundary-F and NSD anchors (deepmind surface-distance).

**Implementation Strategy.** Stimulus generator (~500 LOC numpy/shapely); pyefd for elliptic Fourier descriptors; thin per-model inference wrappers; all analysis CPU-side. The oracle baseline is pure numpy and should be built first — it defines the reference table every model is scored against.

**Reusable codebases (verified real).**
- github.com/facebookresearch/segment-anything, github.com/SysCV/sam-hq, github.com/facebookresearch/sam2, github.com/facebookresearch/Mask2Former
- github.com/xuebinqin/DIS (DIS5K fine-GT)
- github.com/hbldh/pyefd (elliptic Fourier descriptors)
- github.com/deepmind/surface-distance (NSD anchor metric)

**GPU/VRAM/time estimate.** Cheapest of the seven: 4+ model families × ~8.5k images × 1–2 prompts ≈ **10–20 GPU-h total** on one A100 (or a 4090); peak VRAM ≤ 16 GB. Analysis is CPU-bound (hours). Optional retrain extension: +100 GPU-h, excluded from core.

**MVE.** 300 synthetic stimuli, SAM ViT-B vs HQ-SAM: are knees identifiable (R² ≥ 0.8) and do the two models differ? ≈ 2 GPU-h.

**Full experiment.** Full stimulus grid × all models/checkpoint sizes; DIS-5K arm; oracle-resampling reference; cutoff-vs-Nyquist table; octave-prediction test; pre- vs post-upsampling contour comparison.

**Ablation.** Stimulus contrast/texture; prompt type (box vs click vs GT-mask query); logit threshold; contour-extraction stage; object scale (5–50% image occupancy).

**Control.** Oracle grid-resampling; human floor; anti-aliased vs aliased stimulus rendering (renderer-artifact check).

**Robustness.** Cutoff stability across stimulus families (stars vs noise-blobs vs DIS natural); across seeds/φ; across checkpoint size within a family.

**Generalization.** Does the cutoff-to-Nyquist ratio transfer to a held-out decoder family (EfficientSAM decoder; Mask2Former R50 vs Swin)? Architecture law vs recipe accident.

**Failure analysis.** No clean knee → fit roll-off slopes and compare slopes across resolutions instead. Synthetic/natural disagreement → decompose by texture strength (evidence-limited, not decoder-limited). Frequency-resolved error maps published regardless.

**Expected Result (HYPOTHESIS, not measured).** SAM-family cutoffs sit 1–2 octaves below the 256²-path Nyquist and do not shift with output resolution; HQ-SAM sharpens below the cutoff rather than raising it → headline: promptable decoders are training-limited at boundaries and resolution increases alone are wasted — falsifying the field's default fix.

**Negative interpretation.** Cutoff at the limit, shifting per octave → decoders are sampling-limited, the HQ direction is validated and resolution becomes a quantified design dial — equally decision-changing. Mixed regimes → per-architecture datasheet; still the first frequency-resolved decoder comparison.

**Stop condition.** MVE knees unidentifiable (R² < 0.6 across stimulus families) after contour-extraction fixes → the transfer-function abstraction is wrong for these models; stop and release the stimulus suite as an evaluation benchmark.

**Killer Experiment.** The **cutoff-ratio table**: empirical cutoff ÷ oracle-grid-resampling cutoff, one number per model across ≥4 architectures at ≥3 output resolutions. Ratio ≈ 1 everywhere = sampling-limited; ratio ≪ 1 = training-limited. The entire verdict compresses into one measured table at ≈15 GPU-h.

**Research ROI: 8.5 / 10.** Near-zero compute, exact synthetic ground truth kills the annotation-bias attack by construction, and *both* outcomes redirect decoder-design budgets. Discount: "design law" claims need the cross-model generalization to hold.

---

## A-0062 — Sigma-stratified re-scoring of the HQ boundary line against multi-annotator soft references

**Research Question.** Do HQ-SAM-style boundary gains survive when scored within boundary arcs where human annotators agree (low inter-annotator sigma), or do they concentrate below the human boundary-resolution floor where no reference can verify them?

**Core Hypothesis.** A substantial share of the HQ line's hard-label metric gains lives in high-sigma arcs (unverifiable-in-principle); consensus-arc gains are real but materially smaller than reported.

**Falsifiable Prediction.**
- P1: HQ-vs-SAM boundary-F gain in the lowest-sigma tercile shrinks ≥40% relative to the hard-GT gain — or persists, in which case the audit *validates* the HQ line (both outcomes preregistered as content).
- P2 (instrument calibration): synthetically injected boundary improvements of 1 px are detected with ≥80% power by the soft-reference pipeline.
- P3: NSD-with-tolerance and soft-reference scoring disagree on at least one method-pair ranking (otherwise the audit is redundant with the Metrics Reloaded recommendation).

**Method.**
1. References: 300 objects spanning boundary complexity (sampled from DIS-5K, LVIS-quality COCO instances, ThinObject) × 5 annotators tracing boundaries under one fixed written protocol; plus LIDC-IDRI (4 radiologist contours per nodule, free) as a no-collection-cost anchor.
2. Soft-reference construction: per-arc annotator correspondence via curvature-aware closest-point/DTW matching → per-arc inter-annotator sigma + soft boundary probability.
3. Re-score SAM, HQ-SAM, SAM2, and ≥2 HQ-line successors against (a) hard single-annotator GT, (b) soft references, (c) NSD-τ with τ set from measured sigma.
4. Stratify gains by local sigma tercile — conditioning on reference precision equalizes attenuation across methods, which is the refutation of the Stage-4 regression-attenuation attack.
5. Power calibration: warp predictions toward GT by known δ ∈ {0.5, 1, 2} px on random arcs; measure the pipeline's detection rate.

**Architecture.** None new. **Training.** None. **Loss.** N/A.

**Data.** As above; annotation budget 1,500 object-traces. LIDC-IDRI accessed via pylidc.

**Preprocessing.** Annotator screening on calibration objects; intra-rater duplicates for consistency measurement; arc correspondence QC.

**Baselines.** Hard-GT scoring (status quo); NSD-τ (Metrics Reloaded / MONAI implementation); tolerance-band boundary-F at multiple τ.

**Metrics.** Boundary-F per sigma stratum; gain-shrinkage %; detection-power curves; ranking stability (Kendall τ) across scoring families; inter- vs intra-rater sigma.

**Implementation Strategy.** CVAT (or Label Studio) instance for collection; scoring on MetricsReloaded + deepmind/surface-distance; prediction generation via sam-hq/sam2 wrappers; injection calibration is pure numpy warping. Build and validate the *entire* pipeline on LIDC before spending any collection budget.

**Reusable codebases (verified real).**
- github.com/Project-MONAI/MetricsReloaded (metric implementations incl. NSD)
- github.com/deepmind/surface-distance (surface Dice at tolerance)
- github.com/pylidc/pylidc (LIDC-IDRI multi-rater access)
- github.com/cvat-ai/cvat or github.com/HumanSignal/label-studio (annotation tooling)
- github.com/SysCV/sam-hq, github.com/facebookresearch/segment-anything, github.com/facebookresearch/sam2

**GPU/VRAM/time estimate.** Compute trivial: ~6 checkpoints × 300 objects ≈ 2–5 GPU-h, VRAM ≤ 16 GB. The real cost is annotation: 1,500 careful boundary traces ≈ 250–400 annotator-hours ≈ **$4–8k** crowdsourced (or in-house equivalent). Annotation collection is the pacing item.

**MVE.** Zero-collection pilot on LIDC-IDRI (4 raters, free): run sigma stratification + injected-improvement power calibration on 200 nodules with SAM/HQ-SAM/MedSAM-style prompts. ≈ 2 GPU-h. Proceed to natural-image collection only if power ≥ 80% at 1 px with 4 raters.

**Full experiment.** 300 natural objects × 5 annotators; full method battery; three scoring families; stratified gain decomposition; power calibration; ranking-consequence analysis.

**Ablation.** Annotator count 2→5 (how many raters a valid audit needs — a deliverable in itself); instruction-variant arm on 50 objects (protocol-bias check); stratum granularity.

**Control.** Injected-known-improvement calibration (core); intra-rater duplicates; GT-scored-as-prediction ceiling check.

**Robustness.** Shrinkage stability across object classes, sigma-estimation method (DTW vs normal projection), and boundary-metric family.

**Generalization.** Does the shrinkage profile transfer between natural (DIS/COCO) and medical (LIDC) domains?

**Failure analysis.** Arc-level sigma unstable → fall back to object-level sigma strata. Low-sigma stratum nearly empty → the human boundary floor is coarser than assumed; quantify and publish that instead.

**Expected Result (HYPOTHESIS, not measured).** 30–60% of the HQ line's hard-GT boundary-F gain concentrates in the high-sigma tercile; consensus-stratum gains are real but ≈half of reported; NSD-τ under-resolves the distinction → practice recommendation: sigma-stratified soft scoring for boundary claims.

**Negative interpretation.** Gains persist in consensus arcs → the audit validates the HQ line against the gaming suspicion with a better instrument (positive replication, publishable). Power calibration fails → soft references lack sensitivity at the relevant scale; a methods cautionary note that itself corrects Metrics Reloaded-adjacent practice.

**Stop condition.** LIDC MVE: injected 1-px improvements undetectable at ≥80% power with 4 raters → instrument underpowered; stop before spending the annotation budget.

**Killer Experiment.** Sigma-stratified gain decomposition WITH in-pipeline power calibration: within annotator-consensus (low-sigma) arcs, is the HQ-vs-SAM gain above the pipeline's measured detection threshold? A yes/no read that is immune to the attenuation attack because attenuation is conditioned out and sensitivity is measured, not assumed.

**Research ROI: 6.5 / 10.** Decisive design and cheap compute, but external annotation cost/logistics dominate, and the global portfolio already carries two Cluster-B evaluation-validity nominees competing for the same lane.

---

## A-0107 — PEFT forgetting: readout or representation? The four-way swap matrix with serving-cost teeth

**Research Question.** After domain PEFT on SAM, is zero-shot forgetting a decoder-readout phenomenon (recoverable by restoring the original 4M-param decoder) rather than encoder feature destruction — and can one adapted encoder pass serve both a domain decoder and the original zero-shot decoder at ~1× encoder cost?

**Core Hypothesis.** At low LoRA rank, decoder reset recovers ≥70% of lost zero-shot performance at ≤20% domain-gain cost; the dual-decoder configuration ships both capabilities from a single encoder pass (encoder = >95% of inference FLOPs, so this halves serving cost vs adapter toggling).

**Falsifiable Prediction.**
- P1: Recoverable fraction ≥ 70% at r=4, monotonically decreasing with rank.
- P2: {tuned encoder + original decoder} zero-shot mIoU within 5 points of stock SAM on the zero-shot suite.
- P3: Dual-decoder serving: ≥95% of both capabilities at ~1.05× encoder FLOPs vs 2× for toggling.
- P4 (negative branch is content): swap incoherence (>20-pt zero-shot collapse) falsifies the LP-FT feature-vs-head account for prompt-conditioned decoders.

**Method.** Five diverse domains (fixes the Stage-4 generalization attack): Synapse/BTCV multi-organ CT, Kvasir-SEG polyp, ISIC skin lesion, COD10K camouflage, LoveDA/DeepGlobe remote sensing. LoRA r ∈ {4,16,64} on encoder (plus enc+dec arm); after each run evaluate all four {original, tuned} × {encoder-adapters, decoder} combinations on the domain test set and a zero-shot suite (COCO val + LVIS val point/box protocol + SA-1B 1k-image holdout). Then benchmark the single-encoder dual-decoder configuration against adapter toggling at matched latency/FLOPs.

**Architecture.** SAM ViT-B primary; ViT-H replication on 2 domains. LoRA per SAMed; decoder = SAM's stock two-way transformer (4M params — cheap to duplicate).

**Training.** ~30 ViT-B runs (5 domains × 3 ranks × 2 adapter scopes) + 4 ViT-H runs; SAMed-style recipe (AdamW, warmup, box+point prompt sampling).

**Loss.** SAM fine-tuning convention: 20·focal + dice + MSE on the IoU head.

**Data.** Domain sets above (all public, used by the cited PEFT repos); zero-shot: COCO val2017, LVIS v1 val, SA-1B holdout shard.

**Preprocessing.** Per-repo standards; one unified prompt-sampling harness shared by domain and zero-shot evals (protocol parity).

**Baselines.** Adapter toggling (2× encoder passes — the "keep both models" baseline); LP-FT-style decoder-first tuning; full fine-tune on one domain (forgetting reference); optional CA-SAM-style continual method.

**Metrics.** Domain Dice/mIoU; zero-shot mIoU@1-click, mIoU@box, AMG AR; recoverable fraction = (Z_swap − Z_tuned)/(Z_orig − Z_tuned); co-adaptation share; serving table (FLOPs, latency, VRAM per capability).

**Implementation Strategy.** Base training on SAMed (LoRA-SAM, Synapse recipe) + SAM-Adapter-PyTorch (camouflage/polyp configs) + Medical-SAM-Adapter (LoRA mode); zero-shot eval harness on segment-anything + RClicks click protocol; serving bench with torch profiler. The swap itself is checkpoint surgery — trivial once evals exist.

**Reusable codebases (verified real).**
- github.com/hitachinsk/SAMed (LoRA on SAM encoder+decoder, Synapse)
- github.com/KidsWithTokens/Medical-SAM-Adapter (adapter + LoRA modes, LIDC/BTCV loaders)
- github.com/tianrun-chen/SAM-Adapter-PyTorch (COD10K camouflage, Kvasir polyp)
- github.com/huggingface/peft (LoRA plumbing)
- github.com/luca-medeiros/lightning-sam (training-loop reference)
- github.com/facebookresearch/segment-anything; github.com/emb-ai/rclicks (zero-shot protocol)

**GPU/VRAM/time estimate.** ViT-B LoRA run ≈ 6–12 GPU-h → 30 runs ≈ 250 GPU-h; ViT-H arm ≈ 120 GPU-h (wants 80GB or gradient checkpointing on 40GB); evals ≈ 60 GPU-h. **Total ≈ 400–450 GPU-h**, 1–2× A100. Peak VRAM: ViT-B ~24 GB @ bs8/1024²; ViT-H ~70 GB unchunked.

**MVE.** One domain (Kvasir), r=4, ViT-B: train, run the 4-way swap, measure recoverable fraction and — critically — swap coherence (the existential risk named in Stage 4). ≈ 10 GPU-h.

**Full experiment.** Full matrix + rank dose-response + dual-decoder serving benchmark + 5-domain generality + ViT-H replication.

**Ablation.** Rank sweep (core); adapter placement (block subsets); decoder-LoRA vs decoder-full; eval prompt type; domain-data scale.

**Control.** Control retrain: LoRA of identical length on a domain-sized SA-1B subset (does *any* same-length tuning drift zero-shot?); 3 seeds on the MVE domain; orig×orig sanity cells.

**Robustness.** Recoverable-fraction stability across prompt types, eval suites, and domains (medical vs camouflage vs remote sensing).

**Generalization.** Spot-check transfer of the readout account to SAM2 image mode and EfficientSAM (different decoder initialization).

**Failure analysis.** On swap incoherence: localize co-adaptation (prompt-token vs mask-token pathways) and measure layerwise encoder CKA drift; brief decoder re-alignment probe (2k steps, frozen tuned encoder) to distinguish rotation-style misalignment from genuine feature loss.

**Expected Result (HYPOTHESIS, not measured).** Recoverable fraction 60–85% at r=4 falling to 30–50% at r=64; dual-decoder within 1 point of toggling per capability at ~1.05× encoder cost — a component-resolved forgetting account for promptable models plus a deployable serving result.

**Negative interpretation.** Coherent swaps but low recovery → forgetting is genuinely representational even at low rank; falsifies LP-FT transfer to promptable decoders and motivates encoder-side continual methods (content, as Stage 4 argued). Incoherent swaps → co-adaptation share is the finding; dual-decoder needs joint training; report the measured share.

**Stop condition.** MVE: {tuned-enc + orig-dec} collapses >30 points AND the 2k-step re-alignment probe cannot restore coherence → the swap instrument is void; stop and publish the co-adaptation tech note.

**Killer Experiment.** The deployment table across 5 domains: one adapted encoder pass feeding two 4M-param decoders vs adapter toggling, at matched FLOPs — {domain Dice, zero-shot mIoU, cost} per configuration. Preserving ≥95% of both capabilities at ~half the toggling cost gives the readout claim product teeth; failing falsifies the LP-FT account for promptable models. Decisive read ≈ 40 GPU-h after training.

**Research ROI: 7.0 / 10.** Both branches carry content and the serving angle is genuinely deployable; discounted for real training cost (~450 GPU-h) and instantiation-adjacent novelty pressure.

---

## A-0178 — Artifact tokens cause prompt-localized failures: causality via test-time register toggling

**Research Question.** Do high-norm artifact tokens in deployed promptable encoders cause excess click-prompt failure at their image locations — demonstrable by toggling test-time registers (no retraining, no new trained parameters) at identical pixels?

**Core Hypothesis.** On artifact-positive encoders, clicks landing on artifact patches fail more than matched off-artifact clicks, and the excess collapses when register neurons' outlier activations are shifted into a test-time register token.

**Falsifiable Prediction.**
- P0 (gate): ≥2 of 7 fleet models exhibit artifact tokens (final-block token norms > preregistered outlier criterion, spatially sparse).
- P1: On-artifact click failure exceeds matched off-artifact failure by ≥5 points absolute.
- P2: The test-time register toggle removes ≥70% of the excess at identical pixels, while a sham toggle (random non-register neurons, count/energy-matched) removes <20%.
- P3: Dose-response — excess failure monotone in artifact-norm percentile (Spearman ρ > 0.5).

**Method.**
1. **Day-1 fleet norm audit (go/no-go):** token-norm maps over 1k COCO + 1k SA-1B images for SAM ViT-B/L/H, SAM2 Hiera-B+/L, EfficientSAM-S, MobileSAM, and a DINOv2-L-based promptable pipeline (known-positive control). Publish the audit table regardless — which promptable encoders have artifacts at all is itself new.
2. On artifact-positive models: identify register neurons (sparse neurons driving outlier norms, per the test-time-registers method) and implement the zero-init register token + activation-shift hooks for that encoder.
3. Paired within-pixel design: same images, same click pixels; registers off vs on; clicks sampled on artifact patches and on covariate-matched off-artifact patches (local feature norm, distance-to-object, background class — secondary analysis only; the toggle is the primary causal instrument). Failure = IoU < 0.5 vs the intended object's GT, plus NoC@90 excess in a multi-click arm.
4. Dose-response by artifact-norm percentile; user-realism arm with RClicks clicks; AMG arm (do 32×32 grid points landing on artifacts yield spurious/missing masks?).

**Architecture.** Stock checkpoints + test-time register machinery (hooks + one zero-init token; zero trained parameters — this kills the extra-capacity attack).

**Training.** None. **Loss.** N/A.

**Data.** COCO val2017 + LVIS v1 val (dense instance GT for failure grading); SA-1B 1k shard (in-distribution audit); TETRIS/RClicks for realistic clicks.

**Preprocessing.** Block-wise token-norm extraction hooks; preregistered artifact criterion following Darcet et al.'s definitions (high-norm outliers emerging in later blocks of large models).

**Baselines.** Covariate-matched location analysis (secondary); DINOv2-pipeline positive control; input-perturbation control (blur/JPEG — does any perturbation move failures equally?).

**Metrics.** Per-model audit statistics (artifact prevalence, norm distributions, emergence layer); on/off-artifact failure rates; excess after toggle vs sham; dose-response ρ; guardrail: aggregate mIoU under registers unchanged or improved.

**Implementation Strategy.** Port the test-time-registers `HookManager` to SAM's ViT (MAE-style) and SAM2's Hiera (the repo ships CLIP and DINOv2 implementations and documents the extension recipe: identify register neurons, add zero-init token, shift outlier activations). Click-failure harness adapted from RClicks. Audit first; port only for gate-positive models.

**Reusable codebases (verified real).**
- github.com/nickjiang2378/test-time-registers (register-neuron identification + test-time register implementation, NeurIPS'25)
- github.com/facebookresearch/dinov2 (registers reference models, positive control)
- github.com/facebookresearch/segment-anything, github.com/facebookresearch/sam2, github.com/yformer/EfficientSAM, github.com/ChaoningZhang/MobileSAM (the fleet)
- github.com/emb-ai/rclicks (click sampling + failure harness)

**GPU/VRAM/time estimate.** Audit: 7 models × 2k images ≈ 3–5 GPU-h. Register-neuron identification: ≈10 GPU-h per positive model. Paired click study: encoder passes double (registers alter the encoder pass): ~2 × 5k images × per-model cost + cheap decoder sweeps ≈ 40–60 GPU-h across positive models. **Total ≤ 100 GPU-h**; peak VRAM ≤ 24 GB. Engineering (the Hiera/SAM-ViT port) is the dominant cost, not compute.

**MVE.** THE GATE: fleet norm audit on 7 models × 200 images ≈ 1 GPU-h. Kill/proceed decision with a publishable table either way.

**Full experiment.** Positive models × paired toggle design × dose-response × RClicks realism arm × AMG artifact-grid arm; negative models reported as scope boundaries.

**Ablation.** Register count; intervention layer set; neuron-selection threshold; click type (single positive vs positive+negative).

**Control.** Sham toggle (random matched neurons — excess must persist); matched-location secondary analysis; aggregate-quality guardrail.

**Robustness.** Failure-threshold sweep; object-size strata; per-dataset replication (COCO vs LVIS vs SA-1B holdout).

**Generalization.** Scope table across encoder lineages (supervised ViT vs MAE-init vs Hiera vs distilled): where the phenomenon exists and where the causal excess exists — boundaries are findings, not gaps.

**Failure analysis.** Gate-positive but no excess failure → decoder routes around artifacts; analyze decoder cross-attention mass on artifact tokens (an interesting robustness null). Excess exists but toggle doesn't remove it → confounded by low-information background; downgrade to correlational report with the matched analysis primary.

**Expected Result (HYPOTHESIS, not measured).** SAM's MAE-lineage ViT shows weak/no artifacts (consistent with Darcet et al.), but SAM2-Hiera and/or EfficientSAM and the DINOv2 pipeline show them; on positives: 5–15-point on-artifact excess failure, 70–90% removed by the toggle, clean dose-response — the first causal chain from the celebrated registers anomaly to user-visible promptable failure.

**Negative interpretation.** Gate empty across the fleet → honest one-audit-cost stop; the audit note ("the deployed promptable fleet is artifact-free; the registers concern does not transfer") is itself a useful scope result. Toggle-null on positives → promptable decoders are robust to encoder artifacts; robustness finding.

**Stop condition.** P0 fails on all 7 models → stop after the audit note. Or excess < 2 points on every positive model → stop after a correlational tech report.

**Killer Experiment.** The paired within-pixel toggle on artifact-positive models: identical images, identical click pixels, test-time registers on/off, sham-neuron toggle as control — on-artifact excess failure must collapse under the real toggle and persist under the sham. Causality with no matching argument, ≈20 GPU-h on the positive models.

**Research ROI: 7.5 / 10.** Rare clean causal instrument and a headline bridge from interpretability to product; discounted for the existential gate (SAM's MAE lineage may void the flagship model) and nontrivial porting engineering.

---

## A-0271 — SA-1B pipeline fingerprints: filter-ablated relabeling and student inheritance

**Research Question.** Which mask-statistic signatures does each documented SA-1B auto-labeling filter stage create (predicted-IoU ≥ 0.88, stability ≥ 0.95, NMS), and which signatures do matched students inherit — including complexity *ceilings* under prompts exceeding training support?

**Core Hypothesis.** Each filter stage leaves an attributable signature on same-image relabels (e.g., the stability filter suppresses high-curvature/thin masks; the IoU filter truncates the complexity tail); students reproduce their label arm's signatures on held-out images; full-stack students pin to training-complexity ceilings on out-of-support prompts while human-label students do not.

**Falsifiable Prediction.**
- P1: Filter ablations shift mask statistics on identical images (preregistered effect sizes; e.g., removing the stability filter fattens the high-curvature tail, KS p < 0.01).
- P2: A classifier over mask statistics identifies a student's label arm on held-out images at AUC > 0.7.
- P3 (ceiling): the full-stack student's attainable mask complexity (95th-pct curvature energy) on high-complexity held-out objects pins at its training ceiling; the human-arm student tracks GT complexity.
- P4: At least one signature is *amplified* (student stronger than its labels) — an inheritance dynamic mere label-copying doesn't predict.

**Method.**
1. Five label arms on identical images (30–50k COCO train2017 images with LVIS-quality human masks): human GT; full public SAM AMG stack at defaults; −stability (`stability_score_thresh=0`); −IoU (`pred_iou_thresh=0`); −NMS (`box_nms_thresh=1.0`). Same images, same teacher, same everything except one filter per arm → content/ontology confounds vanish by construction (the Stage-4 refutation).
2. Signature statistics per arm: elliptic-Fourier curvature spectra, curvature energy, isoperimetric complexity, size-complexity joint distributions, component/hole counts; computed on IoU-matched instance pairs across arms to hold content fixed.
3. Train five matched promptable students (ViT-S encoder + SAM decoder, identical MAE-pretrained init, identical recipe; arms differ only in masks).
4. Evaluate: signature reproduction on held-out COCO val; the ceiling test on DIS-5K/ThinObject high-complexity objects with box prompts; standard quality metrics per arm.

**Architecture.** Teacher: SAM ViT-H AMG (public stack). Students: EfficientSAM-S-style (ViT-S + stock SAM decoder), one fixed init.

**Training.** 5 student runs, identical hyperparameters (bs 64, ~90k iters, point+box prompt sampling).

**Loss.** SAM convention: 20·focal + dice + MSE (IoU head).

**Data.** COCO train2017 subset with LVIS annotations as the human arm (higher-fidelity polygons); held-out COCO val; DIS-5K + ThinObject-5K as complexity probes; SA-1B 1k shard for reference statistics.

**Preprocessing.** Per-arm AMG runs; shared mask-to-prompt sampling seeds; cross-arm instance matching (IoU-matched pairs) for signature comparison.

**Baselines.** Human-arm student (anchor); teacher SAM itself (does the student inherit more or less than the teacher expresses?); seed replicate of the full-stack arm (within-arm noise floor).

**Metrics.** Signature statistics + arm-classifier AUC; ceiling statistics; per-filter attribution table; student quality (mIoU@click/box, boundary-F) per arm.

**Implementation Strategy.** Relabeling: `SamAutomaticMaskGenerator` with per-arm parameters (all three filters are constructor arguments — verified in the repo). Student training: lightning-sam fork extended to point prompts and multimask. Statistics: pyefd + skimage. The label-arm statistics (step 2) are computed BEFORE any student training — they are the cheap decisive gate.

**Reusable codebases (verified real).**
- github.com/facebookresearch/segment-anything (the public auto-label stack with exposed `pred_iou_thresh`, `stability_score_thresh`, `box_nms_thresh`)
- github.com/luca-medeiros/lightning-sam (SAM fine-tuning loop base)
- github.com/yformer/EfficientSAM (ViT-S promptable student reference/init)
- github.com/czg1225/SlimSAM (small-SAM training reference)
- github.com/cocodataset/cocoapi, github.com/lvis-dataset/lvis-api
- github.com/hbldh/pyefd; github.com/xuebinqin/DIS

**GPU/VRAM/time estimate.** The expensive one. Relabeling: 30k images × 4 AMG arms × ~12 s (ViT-H, fp16) ≈ 400 GPU-h (ViT-L or sparser grid halves this). Students: 5 × ~70 GPU-h ≈ 350 GPU-h (≈2 days per arm on an 8×A100 node at bs64). Evals ≈ 30 GPU-h. **Total ≈ 700–1,100 GPU-h**; peak VRAM 30–40 GB/GPU for student training.

**MVE.** Relabel 2k images under all 5 arms (~25 GPU-h) and compute label-arm signature deltas ONLY — no training. If filter ablations don't detectably shift mask statistics on matched content, the inheritance question is moot and the project stops at ~3% of full cost.

**Full experiment.** 30–50k images × 5 arms × matched students; signature-reproduction + amplification analysis; the ceiling test; per-filter attribution table.

**Ablation.** Threshold dose-response (stability ∈ {0.90, 0.95, 0.98}) beyond on/off; student capacity (ViT-Ti vs ViT-S); data scale (10k vs 50k) for signature-strength scaling.

**Control.** Seed replicate of one arm (noise floor); IoU-matched cross-arm pairing (content held fixed); shared prompt-sampling seeds.

**Robustness.** Attribution agreement across statistic families (EFD vs polygon-vertex vs curvature-energy); AMG grid density (32² vs 64²).

**Generalization.** Swap teacher to SAM2 image-mode AMG on a 5k-image subset: are the filter signatures pipeline-general or teacher-specific?

**Failure analysis.** Students converge across arms despite label differences → the student architecture/optimization prior, not the labels, sets the ceiling — an important negative for the model-collapse discourse; decompose by object size/class before concluding.

**Expected Result (HYPOTHESIS, not measured).** The stability filter is the dominant complexity-ceiling creator (2–3× thinning of the high-curvature tail); students reproduce arm signatures at AUC 0.75–0.9 and pin to ceilings on out-of-support prompts; NMS affects multiplicity/granularity, not curvature — an actionable filter-attribution table for every group building SA-1B-style corpora.

**Negative interpretation.** Label arms differ but students converge → data fingerprints don't survive training at this scale; publishes as "student priors dominate label statistics," directly relevant to model-collapse claims. Label arms don't differ → SA-1B's distinctive statistics come from content/ontology, not filters; the premise dies at MVE for ~25 GPU-h.

**Stop condition.** MVE label-arm deltas below preregistered effect sizes → stop before any student training.

**Killer Experiment.** The ceiling extrapolation test on matched content: prompt the full-stack-arm student and the human-arm student on identical held-out high-complexity objects (DIS-5K); if the full-stack student's attainable complexity pins at its training ceiling while the human-arm student tracks GT, label-copying cannot explain it — a filter-induced capability ceiling demonstrated causally.

**Research ROI: 6.0 / 10.** Highest strategic relevance (auto-labeling era) and a clean causal design, but ~1,000 GPU-h and five training runs make it the most expensive survivor; the MVE gate mitigates but does not remove the cost risk.

---

# Ranking (see `stage5_cluster_A_top.md` for nominee detail)

| Rank | ID | ROI | Decision |
|---|---|---|---|
| 1 | A-0017 | 9.0 | **KEEP — nominee** |
| 2 | A-0061 | 8.5 | **KEEP — nominee** |
| 3 | A-0002 | 8.0 | **KEEP — conditional third (cheap + exceptional)** |
| 4 | A-0178 | 7.5 | DROP (existential gate risk: MAE-lineage may void flagship model) |
| 5 | A-0107 | 7.0 | DROP (450 GPU-h training budget for instantiation-adjacent novelty) |
| 6 | A-0062 | 6.5 | DROP (annotation cost/logistics; validity lane crowded by Cluster-B nominees) |
| 7 | A-0271 | 6.0 | DROP (≈1,000 GPU-h; keep the 25-GPU-h MVE as a cheap option) |
