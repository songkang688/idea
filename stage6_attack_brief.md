# Stage 6 — Research Group Battle: ATTACK PASS on the Supervisor-Locked Top 5

**Role:** Skeptical PI + Reviewer #2 + Reproducibility Reviewer + Implementer (Cloud Sub-Agent P) → Supervisor Windows7.
**Branch:** `cursor/stage6-attack-pass-top5-cca8`.
**Inputs read this session (all fetched from origin and verified present):**

| Source | Branch | Files |
|---|---|---|
| Cluster A stage 3/4/5 | `origin/cursor/stage5-cluster-a-engineering-ed30` | `stage5_cluster_A_engineering.md`, `stage5_cluster_A_top.md`, `stage5_cluster_A_roi.csv`, `stage4_cluster_A_attacks.md`, `stage4_cluster_A_keep.md`, `stage3_cluster_A_priorwork.md` |
| Cluster B stage 5 | `origin/cursor/stage5-cluster-b-engineering-a00b` | `stage5_cluster_B_engineering.md`, `stage5_cluster_B_top.md`, `stage5_cluster_B_roi.csv` |
| Cluster B stage 4 | `origin/cursor/stage4-cluster-b-reviewer2-b25a` | `stage4_cluster_B_attacks.md`, `stage4_cluster_B_keep.md` |
| Cluster C stage 5 | `origin/cursor/stage5-cluster-c-engineering-2eff` | `stage5_cluster_C_engineering.md`, `stage5_cluster_C_top.md`, `stage5_cluster_C_roi.csv` |
| Cluster C stage 4 | `origin/cursor/stage4-cluster-c-reviewer2-c1be` | `stage4_cluster_C_attacks.md`, `stage4_cluster_C_keep.md` |

**Provenance note for the record:** the Stage-4 B/C branches are not listed by a default `git branch -r` on a fresh clone (shallow branch listing); they exist on origin and fetch cleanly by name. Future stages should fetch them explicitly rather than concluding the attack lineage is missing.

**Fresh prior-work sweep (this session, 2026-08-28):** five targeted searches were run (SAM2/SAM3 memory interventions; FSS wrong-support/benchmark-bias; frequency-resolved boundary/aliasing analysis; synthetic-lesion blending artifacts; multimodal rehearsal/forgetting mechanisms). Findings are folded into each idea below. **Headline: no outright fatal scoop was found for any of the five. But two ideas (A-0017, A-0061) are now heavily crowded by 2025–2026 publications the Stage-5 files do not cite, one idea (B-0212) has a domain-validity engineering flaw in its central instrument as specified, and one idea (C-0090) has a recipe-level hidden assumption that alters its control arm. My verdicts: 2 KEEP (with mandatory conditions), 3 PIVOT, 0 KILL.** I am explicitly *not* choosing the final 3; this is an attack brief with updated beliefs for the group battle.

**Where I dissent from Stage 5:** I do not accept the Stage-5 ROI ordering as it stands. A-0017's 9.0 was priced before SAM3's release cascade was fully absorbed; on today's evidence I'd price it ≈7.5 unless the SAM3 arm is added. B-0212's 8 assumes its middle ladder rungs work on CT, which is unverified and in my judgment likely broken as specified. B-0121 and A-0061 remain the best value per GPU-hour, in that order.

---

## 1. A-0017 — SAM2 causal memory surgery (validated upper-bound diagnostic)

**Source:** `origin/cursor/stage5-cluster-a-engineering-ed30` · Stage-5 ROI 9.0 · ~80–120 GPU-h, zero training.

### Fatal flaws (candidates)

1. **The predictive-validity leg (P3) can pass for a trivial reason — this is the strongest attack and it is new.** P3 requires per-sequence reversible fraction to predict SAMURAI/DAM4SAM per-sequence J&F gains at r > 0.6. But reversible fraction and prevention-method gains are *both* downstream of generic sequence difficulty (distractor density, occlusion count, failure count, no-op recovery rate). A raw Pearson/Spearman r > 0.6 is exactly what a shared-difficulty confound produces with no instrument validity at all. As preregistered in the Stage-5 design, the killer experiment's pass criterion does not distinguish "the instrument measures the memory-borne share" from "hard sequences are hard for everyone." The instrument-validation claim — the very thing that separated this from "reset the tracker" in Stage 4 — is not established by the preregistered statistic.
2. **"Targeted deletion keeps pre-error memories" is not the clean intervention the design assumes.** SAM2's memory attention consumes the most recent N non-conditioning frames with recency-indexed temporal position encodings plus object pointers. Deleting post-error entries forces pre-error entries into recency slots they never occupied in training — the surgered configuration is off-distribution for the memory attention, independent of the *content* of those memories. Part of any targeted-vs-reset gap (P2's ≥10 points) may be a temporal-encoding artifact, in either direction. The design's random-deletion control does not isolate this.
3. **Significance decay is no longer hypothetical — SAM3 shipped.** SAM3 released Nov 2025 (arXiv:2511.16719), SAM 3.1 in Mar 2026; the SAM3 tracker inherits the SAM2 memory-bank architecture. Worse, arXiv:2512.22624 ("Rethinking Memory Design in SAM-Based Visual Object Tracking," Dec 2025, with a public SAM3 tracking zoo) already: (a) systematically analyzes SAM2-era memory mechanisms, (b) reimplements them within SAM3, (c) evaluates across ten benchmarks, and (d) proposes a unified short-term/long-term hybrid memory. It is a design study, not a causal surgery decomposition — the reversible/irreversible split with predictive validation is still unclaimed — but the "memory is the bottleneck of SAM-family tracking" headline is being written by others *now*, on the current model generation. A SAM2.1-only surgery paper in late 2026 reads as archaeology. Also note the reset-style repair idea is being independently published in applied venues (CL-MC, arXiv:2602.19380: detector-triggered memory overwrite for SAM2 drift) — the "surgery = reset heuristic" attack from Stage 4 now has a citable fix-paper making the targeted-vs-reset gap load-bearing for the entire contribution.

### Hidden assumptions

- Failure harvesting yields ≥200 *usable* organic failures from LVOS v2 val (140 videos) + DiDi with GT reappearance frames. Yield is unverified; the ambiguous-reappearance stratum could dominate.
- The per-frame memory dict in SAM2's inference state is separable per object and replay from an arbitrary t_r is bit-faithful (the design assumes deterministic replay; SAM2's video predictor caches must be handled carefully or the no-op arm won't reproduce the original failure).
- SAMURAI/DAM4SAM per-sequence gains are stable enough (single-run, no seeds — both are deterministic wrappers, but harvesting protocol differences between our failure set and their eval protocol may inject noise into the regression).

### Implementer blockers

- **DiDi dataset access:** hosted at go.vicos.si (academic distribution, linked from DAM4SAM). Availability/license OK to assume but must be confirmed day 1; there is no mirror.
- Memory-surgery hooks: ~300 LOC as claimed is plausible, but the temporal-position re-indexing issue (flaw 2) means the honest version needs an extra sham arm — small additional engineering.
- VRAM/compute fine (1× A100-40GB). No annotation, no training. Weakest blocker profile of the five on paper — *if* the SAM3 arm is skipped; adding SAM3 means porting surgery hooks to a second codebase (~1–2 weeks engineering, checkpoints gated behind HF authentication).

### Reproducibility risks

- Low on data/code; moderate on protocol: the failure-harvesting definition (IoU<0.1 for k frames after ≥0.5) has multiple free parameters that determine the entire corpus; the sweep is in the design but the headline number will be parameter-sensitive. The released failure corpus + surgery toolkit mitigates.

### Updated belief: **PIVOT**

Keep the instrument; the killer experiment as preregistered is not sufficient. Mandatory changes: (1) P3 becomes a *difficulty-partialed* validity test — reversible fraction must predict prevention gains after controlling for no-op recovery, failure count, and distractor density (preregister partial r > 0.4, or a nested-model comparison); (2) add a temporal-encoding sham arm (delete post-error entries but re-insert count-matched pre-error duplicates at the same recency slots) to bound the encoding artifact; (3) add a SAM3-tracker replication arm or accept a one-generation-stale scope with an explicit argument (the SAM2-inherited tracker in SAM3 is the argument — make it, with a pilot).

### Decisive experiment that would change my mind

The 50-failure pilot with all of: targeted vs reset vs no-op vs temporal-sham, plus difficulty-partialed regression against SAMURAI and DAM4SAM. If targeted beats reset AND sham by ≥10 pts and partial-r > 0.4 survives difficulty controls at pilot scale, I withdraw flaws 1–2 and this becomes the strongest KEEP of the five. If targeted ≈ sham, the instrument story collapses to memory-recency mechanics and I move to KILL.

### Unresolved disagreements I expect

- Whether the oracle-timed upper bound is decision-relevant to anyone shipping trackers (Stage-4 answered "score prevention methods against the ceiling"; a deployment-minded expert will still object no deployment has the oracle).
- Whether to pay the SAM3 porting cost now or publish fast on SAM2.1 before arXiv:2512.22624's lineage extends to causal decompositions — a genuine race-vs-rigor tradeoff the group must settle.
- Whether my temporal-encoding concern is overblown (a defender will note the conditioning-frame memory has no recency encoding and object pointers dominate re-detection; nobody knows — which is the point of the sham arm).

---

## 2. B-0121 — Wrong-support counterfactual audit of few-shot segmentation

**Source:** `origin/cursor/stage5-cluster-b-engineering-a00b` (stage 4 on `origin/cursor/stage4-cluster-b-reviewer2-b25a`) · Stage-5 ROI 9 · ≤5 A100-days, zero training.

### Fatal flaws (candidates)

1. **Post-SAM3 significance decay of the audited population.** The audit panel is PFENet/HSNet/BAM (2020–2022 specialists) plus foundation matchers. SAM3 (Nov 2025) performs exemplar-prompted concept segmentation at 75–80% of human on SA-Co — image exemplars *are* supports. If the specialist-FSS era is over, "the specialist leaderboard is partly saliency" indicts a museum. This does not kill the audit (the validity methodology and the foundation-matcher retention numbers keep it alive) but it moves the headline: the interesting 2026 question is whether *foundation-era* support-conditioned methods (Matcher, PerSAM, SegGPT, FSSAM, SAM3-exemplar) actually use the support. The Stage-5 design has these methods but frames specialists as the headline. Wrong emphasis, cheap to fix.
2. **The killer's leg (b) is hostage to the floor choice.** "Correct-support accuracy indistinguishable from the support-free objectness floor" uses SAM AMG largest/most-central mask as the floor. SAM AMG is a very strong class-agnostic segmenter; a weak classical SOD floor could flip leg (b)'s verdict on the same data. The conclusion "few-shot learning fully accounted for by the prior" is then an artifact of which prior you granted the floor. Both floors are in the design but the killer criterion binds to one — underspecified in a way that will be litigated.
3. **Wrong-class support sampling is not exchangeable across queries.** "Classes verified absent from Q" on COCO-20i correlates the available wrong classes with query content (co-occurrence structure); support-mask area matching within ±50% is loose. Retention differences across strata could partly reflect wrong-support sampling artifacts. Needs a preregistered sampling scheme (fixed wrong-class pools per fold, near/far-class split — the ablation exists; promote it to the main design).

### Hidden assumptions

- Retention = IoU_wrong/IoU_correct is unstable where IoU_correct is small; episode-level filtering (IoU_correct > threshold) must be preregistered or it becomes an analyst degree of freedom.
- Each repo's episode sampler and evaluation protocol differ; the design's "official per-repo eval vs one shared evaluator" robustness check is load-bearing, not optional — publish the shared episode lists.
- 1,000 episodes/fold × strata gives adequate power for the distractor-present stratum (the stratum could be thin on PASCAL-5i; COCO/LVIS carry it).

### Implementer blockers

- **Checkpoint link rot is the #1 practical risk:** BAM (OneDrive), HSNet (Google Drive) — these links break routinely. Day-1 task: download and re-hash every checkpoint before any commitment. PFENet, Matcher, PerSAM, FSSAM, SegGPT (HF) are safer.
- Seven small support-injection wrappers: real but trivial. SAM3-exemplar arm adds HF-gated checkpoint access — cheap.
- No annotation, no training, no license issues (VOC/SBD/COCO/LVIS/FSS-1000 all standard research licenses).

### Reproducibility risks

- Lowest of the five. Public checkpoints + fixed episode lists + released distractor-enriched split = near-fully reproducible. Residual: wrong-support draws must ship as fixed lists, not seeds.

### Updated belief: **KEEP**

Conditions (all cheap): (1) add SAM3-exemplar-prompt arm and make foundation-era retention co-headline; (2) preregister both floors and report leg (b) against each; (3) fixed wrong-support lists with near/far-class stratification promoted into the killer; (4) day-1 checkpoint archival.

### Decisive experiment that would change my mind

The MVE as designed (PFENet+BAM+Matcher, PASCAL-5i f0 + COCO-20i f0, ~1 A100-day) with one addition: run FSSAM or SAM3-exemplar in the same pass. If *all* methods including foundation-era ones collapse below 20% retention everywhere including the degenerate strata, the certification negative is real but the paper drops to eval-track significance and I'd argue to demote it behind an alternate. If any modern method retains >35% on distractor-present strata, this is the cheapest headline of the five.

### Unresolved disagreements I expect

- Whether the certification negative (everything collapses appropriately) is a top-venue paper or a workshop note — the Stage-5 file asserts the former; I am unconvinced, and the group should price that branch honestly.
- Whether auditing specialists at all is worth panel slots vs an all-foundation panel.
- Whether the medical transfer probe (Matcher/PerSAM/SegGPT on CT one-shot episodes) belongs in scope or dilutes.

---

## 3. A-0061 — Boundary Nyquist: cutoff at, or far below, the decoder's sampling limit

**Source:** `origin/cursor/stage5-cluster-a-engineering-ed30` · Stage-5 ROI 8.5 · 10–20 GPU-h, inference-only.

### Fatal flaws (candidates)

1. **The two-world dichotomy is ill-posed as preregistered: there is a third world the oracle cannot see.** The killer's cutoff-ratio table divides the empirical cutoff by "the oracle bound obtained by passing GT through each decoder's own *output grid*." But SAM-family models impose at least three upstream band limits before the decoder's output grid: the longest-side-1024 input resize, the 16-px patch tokenization (64×64 token grid), and the 256² logit path. The 64² token grid is *coarser* than the 256² output grid. A measured ratio ≪ 1 against the output-grid oracle — the design's "training-limited" verdict, and its headline — is equally consistent with "encoder-token-grid-limited," which recommends a *completely different* engineering lever (input resolution / patch size, not decoder training). The preregistered verdict table mis-attributes in exactly the branch the authors expect to land. This is fixable and cheap, but as written the killer experiment's interpretation is wrong.
2. **The lane is more crowded than Stage 3/4 recorded.** arXiv:2403.09065 ("When Semantic Segmentation Meets Frequency Aliasing") already: computes per-architecture equivalent Nyquist frequencies, defines an aliasing score, quantitatively links boundary hard-pixels to aliasing, and ships de-aliasing fixes; AAAI 2026 ("Revisiting Downsampling…") and CVPR 2026 (CROWn, 3D medical) extend the line. These are image-space, encoder-side analyses — the contour-frequency transfer function against the decoder's operating point is still unclaimed, and the synthetic-exact-GT suite is still unique. But "first frequency-resolved boundary-error analysis" is no longer available as framing, and reviewers from that line will demand a direct comparison (does the cutoff-ratio table say anything the aliasing score doesn't?).
3. **P2 (octave-shift under resolution doubling) is only cleanly testable within a model family that exposes multiple output resolutions — mostly it isn't.** Across-model comparisons confound resolution with training recipe; the design concedes generalization risk but the octave prediction is one of only three preregistered predictions. Its effective scope is HQ-SAM's dual paths plus resized Mask2Former variants; that's thin support for a "design law."

### Hidden assumptions

- A knee exists (segmented regression R² ≥ 0.8) rather than a smooth roll-off — stop condition covers this honestly.
- Marching-squares contour extraction at the logit grid does not itself alias; threshold choice interacts with contour frequency (ablation exists; keep it).
- Elliptic-Fourier harmonic index is comparable across object scales only after arc-length normalization; cutoff must be reported in cycles/pixel with scale strata, or cross-model comparisons silently compare object sizes.
- Textured composite stimuli are in-distribution enough that failures are boundary-frequency failures, not detection failures (the 1-click IoU > 0.9 gate covers, but only at low frequency).

### Implementer blockers

- Nearly none: all checkpoints public, DIS-5K academic license, pyefd/skimage/surface-distance standard, single GPU. The stimulus generator (~500 LOC) plus the oracle ladder is the whole build. Cheapest of the five by an order of magnitude.

### Reproducibility risks

- Low. Synthetic suite with analytic GT is released; everything else is stock checkpoints. Residual: analysis pipeline (knee-fitting) has analyst degrees of freedom — preregister the segmented-regression spec.

### Updated belief: **PIVOT**

Same experiment, corrected attribution: (1) replace the single output-grid oracle with an **oracle ladder** — GT resampled through each candidate band limit (1024 input resize; 64² token grid; 256² logit grid; final upsample) — so the cutoff-ratio table names the *binding stage* per model rather than a binary sampling-vs-training verdict; (2) reposition against the aliasing-score line explicitly (contour-space vs image-space; decoder operating point vs encoder downsampling) and include their aliasing score as a comparison covariate; (3) demote P2 to the model pairs where within-family resolution variation actually exists.

### Decisive experiment that would change my mind

The MVE (300 stimuli, SAM ViT-B vs HQ-SAM, ~2 GPU-h) *with the oracle ladder*. If empirical cutoffs pin to the 64² token-grid oracle across models, the paper becomes "promptable decoders are encoder-sampling-limited" — still decision-changing, different lever, and my flaw 1 becomes the finding. If cutoffs sit below every oracle rung, the training-limited verdict is then genuinely supported and I withdraw the objection. If no knees exist, kill at ~2 GPU-h as designed.

### Unresolved disagreements I expect

- Whether the contour-frequency formalism adds decisions beyond boundary-F-at-tolerance plus the existing aliasing score (I say yes with the oracle ladder, marginal without it; others will say no).
- Whether "design law" framing should be dropped entirely for an honest per-architecture datasheet (cheaper claim, easier reviews, smaller headline).
- Whether DIS-5K natural-arm disagreement with synthetic results would sink or merely scope the claims.

---

## 4. B-0212 — Blending-artifact detectability → synthetic-to-real transfer-gap law

**Source:** `origin/cursor/stage5-cluster-b-engineering-a00b` (stage 4 on `origin/cursor/stage4-cluster-b-reviewer2-b25a`) · Stage-5 ROI 8 · ~40–45 A100-days full, MVE ~6.

### Fatal flaws (candidates)

1. **The central instrument is out-of-domain as engineered: libcom's harmonization/scoring models are RGB natural-image networks being pointed at CT.** Arms (iv) learned harmonization (PCTNet) and the off-the-shelf detectability proxies (BargainNet harmony score, MadisNet inharmonious localization) are trained on natural-image composites. Applied slice-wise to single-channel HU-windowed CT, they are as likely to inject their own artifacts (inter-slice inconsistency, intensity distortions) as to remove seams. The ladder's rungs are then not monotone in "compositing quality" — they are different flavors of out-of-domain corruption, and the "law" is fit across an x-axis with no construct validity. The Stage-5 "[verified this session]" tags verified repo *existence*, not domain applicability — a verification-theater failure the Reproducibility Reviewer must flag.
2. **The probe's AUROC may have no usable spread across arms, for a reason unrelated to the law.** The probe classifies composite-vs-real boundary patches. At fixed content the *procedural lesion texture* differs from real lesions everywhere, not just at seams; the probe can hit AUROC ≥ 0.95 on every arm off texture alone, compressing the x-axis to nothing. The pre-MVE sanity gate (arm-i AUROC > 0.9) does not test spread. A texture-controlled probe (composite-vs-composite across arms, or real-lesion-cut-paste rungs) is needed for the x-axis to exist.
3. **The killer's statistics are underpowered as preregistered.** Spearman ρ ≤ −0.8 across 5 arms is n=5; one adjacent-rank flip destroys it. Real-tumor DSC on LiTS/MSD Task03 is notoriously seed-noisy (several DSC points across seeds is normal for liver tumors); 3 seeds per arm may not stabilize arm ordering. The design counts "3 seeds → 15+ points," but seeds within an arm are not independent draws of the arm effect — the effective n for the law is 5 (or 6 with the generative rung it excludes). Either add rungs (≥7–8) or preregister a weaker, defensible criterion (monotonicity + effect size with CIs, not a point ρ threshold).

### Hidden assumptions

- The seam residual ("mean difference between arm-i and arm-iv boundary patches") is a content-independent, injectable signature; injecting it along GT boundaries of *real* test images leaks GT localization into the attribution test — a positive seam-following result must be shown not to be an injected-saliency artifact (random-curve control exists; make it the primary contrast).
- DiffTumor's STEP3 recipe shortened to 1,000 epochs preserves arm ordering (calibrated at MVE — fine).
- The 2017 Cut-Paste-and-Learn transfer claim is the right foil; the 2026 fix wave (below) partially concedes the premise.

### New prior work (this session)

- **SRA-Seg (arXiv:2602.02944, Feb 2026):** soft edge blending + feature alignment, explicitly motivated by hard copy-paste boundaries in medical synthesis. **TumorGen (arXiv:2505.24687):** boundary-aware tumor synthesis. **Texture-Shape Dilemma (arXiv:2603.00985, Mar 2026):** formally names "boundary aliasing" in synthetic 3D medical pretraining. None measures a detectability→gap law at fixed content, and none runs reverse injection — the causal claim is still unclaimed. But the field is *fixing* blending artifacts at publication speed; by submission time "blending artifacts hurt transfer" will be folklore-with-fixes, and only the quantitative law + hygiene number clears the novelty bar. The scoop clock on this idea is the fastest of the five.

### Implementer blockers

- CT-native compositing engineering (3D Poisson blending, inter-slice-consistent feathering) to replace/augment libcom rungs: real work, ~2–3 weeks, and it *is* the fix for flaw 1.
- LiTS license (competition terms, no redistribution of derived images without care), MSD CC-BY-SA, DiffTumor HF assets fine. nnU-Net/MONAI training infra standard but the 30-run grid is the second-largest compute of the five.
- Probe/segmenter pipelines straightforward.

### Reproducibility risks

- Moderate: the compositing ladder itself must be released (composited volumes or exact recipes + seeds), else nothing replicates; LiTS redistribution terms complicate releasing composites — plan for recipe+code release with regeneration scripts.

### Updated belief: **PIVOT**

The causal skeleton (fixed content, vary compositing only, reverse injection) is the right design and remains unclaimed. Mandatory changes before any GPU: (1) replace the ladder's middle rungs with CT-native compositing (3D Poisson, feathering schedules, DiffTumor's own blending stages) and demote RGB-harmonizer arms to an exploratory appendix; (2) add a texture-controlled probe so the x-axis measures seams, not synthetic texture; (3) re-preregister the law criterion for n-of-arms reality (≥7 rungs, monotonicity + CI-backed effect size instead of point ρ ≤ −0.8); (4) MVE gate unchanged (flat real-DSC across arms kills cheaply).

### Decisive experiment that would change my mind

A ~1 A100-day pre-MVE: build arm (i) and one CT-native blended arm, train the probe both ways (composite-vs-real AND composite-vs-composite), and measure probe AUROC spread + slice-consistency of the blended volumes. If CT-native blending yields a probe spread ≥ 0.15 AUROC with visually/quantitatively sane volumes, my flaws 1–2 dissolve and this is a KEEP at nominee strength. If the spread is < 0.05, the x-axis doesn't exist and I move to KILL regardless of the folklore.

### Unresolved disagreements I expect

- Whether the generative in-fill rung (DiffTumor diffusion) belongs inside the law: the field's dominant pipeline is generative in-fill, and a law fitted only on paste-composites will be attacked as answering yesterday's pipeline. Keeping it "outside the law" (as designed) is honest but shrinks relevance; including it re-opens the generator confound Stage 4 killed. No clean answer; the group must choose which criticism to eat.
- Whether the hygiene-number deliverable (probe AUROC per pipeline) needs the law at all — an implementer faction will argue to ship the audit and skip the 30-run causal grid.
- Medical-venue vs CV-venue positioning (affects how fatal flaw 3's statistics read).

---

## 5. C-0090 — Text rehearsal works by gradient rebalancing, not content

**Source:** `origin/cursor/stage5-cluster-c-engineering-2eff` (stage 4 on `origin/cursor/stage4-cluster-c-reviewer2-c1be`) · Stage-5 ROI rank 1 · ~2.3–2.45K A100-h.

### Fatal flaws (candidates)

1. **The control arm contradicts the "exact published recipe" premise: LLaVA-1.5's 665K mix already contains text-only rehearsal.** The published llava_v1_5_mix665k includes a ShareGPT text-only slice (~40K conversations). So (a) the "base run reproduces LLaVA-1.5" and (b) "A0 = no rehearsal on the published recipe" cannot both hold: A0 requires stripping ShareGPT from the mix (a recipe deviation that changes the multimodal data distribution too), and A1 "curated" partially duplicates what the recipe already does natively. As written, the design's forgetting floor is ill-defined, its arms are not interventions on a fixed base, and the measured A1−A0 gap will differ from the field's mental model of "LLaVA-1.5 + rehearsal." Fixable by redefining the base as the text-stripped mix with token-budget re-matching across arms — but that must be preregistered, and it shrinks the claim's direct applicability to "the published recipe."
2. **Two of four capability strata have unusable retention denominators.** Retention(c) = score/score(Vicuna-7B base). Vicuna-7B is near-floor on GSM8K and weak on IFEval; ratios with tiny denominators are noise amplifiers, and the decision rule ("≥3 of 4 language capabilities under both conventions") can flip on that noise. The abort gate watches seed variance on A0/A1 only — it does not gate per-stratum denominator adequacy. Reasoning/instruction-following strata need either absolute-delta co-primary metrics or a base model that actually has the capability.
3. **The mechanism space is being colonized in real time.** This session found: Dynamic Gradient Guidance (arXiv:2511.15164, Nov 2025 — forgetting recast as missing-gradient approximation on LLaVA), MoDE (NeurIPS 2025 — modality gradient conflict formalized with first-order theory), and the published version of the closest prior (Srivastava et al., PMLR v330, 2026 — 5 CL methods on LLaVA linguistic forgetting, real-data rehearsal only). Still **no content-free-control study** — A2/A3/A4 remain unclaimed — but the "it's optimization balance, not data" conclusion is being approached from the gradient-methods side. Residual scoop window: plausibly months. The design's own mitigation ("15 fine-tunes from done") is real but requires actually starting.

### Hidden assumptions

- Forgetting at 1-epoch LLaVA-1.5-7B scale is large enough to support an 80%-of-gap decision rule (prior work reports up to ~15% degradation — but that includes the strata with bad denominators; per-stratum power is unverified until the first 6 runs).
- Gradient-norm matching is achievable without destabilizing training (scaling C4 losses to match curated-mix gradient norms changes effective LR on the language tower; divergence between conventions is declared "a finding," which is honest but risks an unpublishable middle).
- The shuffled-token arm (A3) is tokenizer-valid (permuted C4 tokens produce sequences whose gradient statistics are the intended "unigram-preserving" control rather than degenerate attention patterns — worth a 1-run pilot before committing 3 seeds).
- Single model family/scale suffices for a "stop paying for curation" headline. Reviewers will demand a second family (prismatic-vlms is named as fallback harness — promote a 2-arm replication there, A0/A1/A2 × 1 seed, into the core design).

### Implementer blockers

- Compute is the largest of the five (~2.3–2.45K A100-h on 8×A100-80GB); no annotation/API spend.
- Licensing: Vicuna-7B (LLaMA-2 community license) fine for research; C4 (ODC-BY) fine; **ShareGPT provenance is legally murky** (scraped user conversations) — it's in the published recipe so usage is defensible-by-precedent, but a careful group notes it.
- LLaVA repo is in maintenance mode; deepspeed configs may need version pinning (known ecosystem friction, ~days not weeks).

### Reproducibility risks

- Moderate-low: all components public; the pre-registration artifact (frozen eval YAMLs committed before arm runs) is good practice the other four should copy. Residual: 8×A100 deepspeed runs are hardware-config-sensitive; publish exact configs + loss curves.

### Updated belief: **KEEP**

Conditions: (1) redefine arms against a preregistered text-stripped base mix with explicit token-budget accounting (fixes flaw 1) and report the published-recipe run as a reference point, not an arm; (2) per-stratum power/denominator gates — absolute deltas co-primary with ratios; GSM8K/IFEval strata may be replaced (e.g., ARC-C + TruthfulQA-style knowledge split) if the pilot shows floor effects; (3) 1-run A3 sanity pilot before seeding; (4) add a 3-run cross-family replication (prismatic) of A0/A1/A2. None of these change the killer's identity; all change its interpretability. Start soon — this idea's value decays with the scoop clock.

### Decisive experiment that would change my mind

The first 6 runs (A0/A1/A2 × 2 seeds, text-stripped base) with per-stratum power analysis. If the A1−A0 gap on knowledge+fluency strata is < 2× seed σ, the phenomenon is too small at this scale and the design's own kill clause fires (<1K A100-h spent) — I'd then argue against the 13B escalation and for reallocating to C-0028. If the gap is well-powered and A2 lands anywhere clearly (≥80% or ≈A0), every branch is a paper and this is the highest-ceiling KEEP of the five.

### Unresolved disagreements I expect

- Whether the mushy-middle branch ("X% real text, only for knowledge") is genuinely a practice-change paper or a shrug with a table — Stage 4 called it actionable; I lean actionable *only if* the mixture-sweep runs (A2/A1 at {1,5,10}%) are funded.
- Whether Robins-1995 subsumption ("pseudo-rehearsal predicted this") survives review even with the multimodal/capability-stratified delta — a battle of framing, unresolvable pre-data.
- Whether 2.3K A100-h here beats the same budget on C-0028's decision triple (portfolio-level fight; both are C-cluster training-mechanism tests, and the group holds only so many nodes).

---

## Cross-cutting findings

1. **SAM3 is the elephant.** Three of five ideas (A-0017 hard, B-0121 medium, A-0061 soft) have significance now conditioned on the SAM3 release cascade that postdates the Stage-1–4 lineage. Every SAM-family idea must state its SAM3 position explicitly at Stage 6, or the portfolio publishes into a superseded ecosystem.
2. **"Verified this session" tags in Stage-5 files verified existence, not fitness.** B-0212's libcom-on-CT is the worst case; the group should adopt "existence-verified" vs "fitness-verified" as distinct tags from Stage 7 on.
3. **No fatal scoop anywhere — but two scoop clocks are running fast** (B-0212's fix wave; C-0090's gradient-mechanism colonization). If the supervisor sequences execution, those two go first among survivors of the battle.
4. **Statistical preregistration quality is uneven:** A-0017's raw-r validity test and B-0212's n=5 ρ threshold are both statistics that can pass/fail for reasons unrelated to their claims. The PIVOTs above are mostly "same experiment, defensible statistics."
5. **Alternates, if the battle kills a Top-5 member:** first calls by lane — if A-0017 dies → **A-0002** (same SAM-mechanism lane, ~30 GPU-h killer, no existential dependency on SAM3); if B-0212 dies → **M5/B-0362** (desk-survey-gated, near-zero GPU) with **B-0112 Leg-1** as backup; if C-0090 dies → **C-0028** (flagship-grade but 5.2K A100-h) or **C-0302** (cheap, narrow); **A-0178** only behind its 1-GPU-h fleet-audit gate; **C-0028** is also the natural upgrade if the group wants a second training-mechanism slot regardless.

## Verdict table

| # | ID | Idea | Stage-5 ROI | Stage-6 belief | Single most dangerous objection |
|---|----|------|-------------|----------------|--------------------------------|
| 1 | A-0017 | SAM2 causal memory surgery | 9.0 | **PIVOT** | Predictive-validity r>0.6 passes via shared difficulty confound — the instrument gets "validated" without measuring anything causal |
| 2 | B-0121 | Wrong-support FSS audit | 9 | **KEEP** | Post-SAM3, a specialist-centric audit indicts a museum; the panel emphasis must move to foundation-era methods |
| 3 | A-0061 | Boundary Nyquist cutoff-ratio | 8.5 | **PIVOT** | The single output-grid oracle can't separate "training-limited" from encoder-token-grid-limited — the preregistered headline mis-attributes in its expected branch |
| 4 | B-0212 | Blending-artifact → transfer-gap law | 8 | **PIVOT** | The ladder's middle rungs (RGB harmonizers on CT) and texture-confounded probe mean the law's x-axis may not exist as engineered |
| 5 | C-0090 | Text rehearsal = gradient rebalancing | rank 1 | **KEEP** | LLaVA-1.5's mix already contains text rehearsal — the "no-rehearsal floor on the published recipe" is self-contradictory as specified |

*No fake consensus: the PIVOT/KEEP calls above are my updated beliefs under attack, with the decisive experiments that would flip each one stated inline. Nothing here pre-empts the group battle or the Supervisor's final 3.*
