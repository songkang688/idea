# Stage 4 — Cluster C: Reviewer #2 Attack Report

**Role:** Reviewer #2 (Cloud Sub-Agent L) → Supervisor Windows7
**Input:** 18 Stage-3 Cluster C survivors (10 KEEP + 8 MUTATE) from `origin/cursor/stage3-cluster-c-priorwork-f96e`; Stage-1 originals from `origin/cursor/stage1-cluster-c-ideas-8c7f`; A/B Stage-3 keep lists skimmed for overlap.
**Stance:** Each idea is treated as a *submitted paper*. I reject as hard as possible. An idea survives only if a realistic experiment exists that would shut me up. Per instruction, I am extra harsh on (a) analysis-only papers with no actionable implication and (b) "we ran an audit" papers with no causal lever.

**Outcome: 7 SURVIVE · 11 KILL.**

Every pure evaluation-audit in the list is dead (C-0276, C-0320, C-0332, M1/C-0002, M2/C-0014, M5/C-0099). Every survivor has an interventional lever the experimenter controls (batch composition, rehearsal content, counterfactual edits, acquisition function, data-vs-task arm assignment, planted bias + retraining depth, ISP re-rendering) and a decision that changes depending on the result.

---

# PART 1 — Stage-3 KEEPs (K1–K10)

## K1. C-0028 — In-batch concept co-occurrence, not loss design, creates dense alignment

**Reviewer #2 attacks:**

1. **"Retrieval stays equal" is a hope, not a design property.** Curating batches by noun overlap *is* hard-negative mining. NegCLIP (Yuksekgonul et al. 2023) and the hard-negative literature show batch hardness moves retrieval and compositionality. If retrieval moves in your curated run — and it will — your "dense-specific mechanism" collapses into "hard negatives improve everything," which is published. Your headline depends on an equality you cannot enforce, only observe.
2. **Uncontrollable loss-geometry confound.** Curated batches shift the in-batch similarity distribution; the learnable temperature and the gradient signal-to-noise both adapt. Two runs at "identical loss/data/steps" are not matched in effective learning signal. Any segmentation delta can be attributed to effective-hardness differences rather than to co-occurrence per se.
3. **Uninformative null at your scale.** Emergent zero-shot segmentation in CLIP-small on 20M captions is marginal to begin with. A null ("curation doesn't create dense alignment") is fully explained by "you are below the emergence scale," so the experiment is asymmetric: the positive is confounded (attack 1–2), the negative is vacuous.
4. **JEST proximity.** DeepMind already showed batch composition is a first-order training variable (Evans et al. 2024). Your delta is "we measured segmentation instead of retrieval" — a reviewer will call that a metric swap on a published lever.

**The experiment that shuts me up (exists, realistic):** A three-arm dose-response design at CLIP-B/32 scale: (i) random batches, (ii) noun-overlap-curated batches, (iii) **hardness-matched control** — batches curated to the same in-batch similarity/hardness distribution as (ii) via caption-embedding similarity but *without* shared-noun co-occurrence. Report retrieval and dense metrics jointly across a curation-strength sweep, ≥3 seeds. If segmentation moves in (ii) but not in (iii) at matched hardness and matched retrieval, the co-occurrence mechanism is isolated from generic hard-negative effects — that answers attacks 1, 2, and 4 simultaneously; the dose-response curve answers 3 (a graded response cannot be a threshold artifact). Feasible on academic compute (CLIP-small, ~20M pairs per arm).

**Verdict: SURVIVE.** Causal training lever, free-to-deploy implication (batch curation as a dial for dense ability), and the hardness-matched control is a real, runnable design that defuses the fatal confound.

---

## K2. C-0090 — Text-batch rehearsal works by gradient rebalancing, not by content

**Reviewer #2 attacks:**

1. **"Matched gradient scale" is underdefined to the point of unfalsifiability.** Matched how — global norm, per-layer, per-module, per-step? Random-token batches produce categorically different gradient structure (attention entropy, embedding-row usage) than natural text at any global norm. Whatever matching you pick, I claim the other one; the headline hides an intractable matching problem.
2. **Pseudo-rehearsal is 30 years old.** Robins (1995) showed random-input pseudo-rehearsal mitigates catastrophic forgetting. If random text works, a reviewer says Robins predicted it; if it doesn't, the curated-content camp is confirmed. Where is the new mechanism space?
3. **The likely outcome is the mushy middle.** Your own risk note concedes it: random text preserves fluency but not knowledge. "Content matters for some capabilities, gradient balance for others" kills the clean headline and, with it, the claimed actionable implication (stop curating rehearsal data) — nobody stops curating on a partial result.
4. **Crowded adjacent mechanism.** Modality gradient-conflict work already frames multimodal forgetting as an optimization-balance problem; you may be re-deriving their conclusion with a weaker instrument.

**The experiment that shuts me up (exists, realistic):** Five arms at fixed token budget — {no rehearsal, curated mix, random web text, shuffled-token text, single repeated document} — on a LLaVA-1.5-class fine-tune, with **capability-stratified evaluation pre-registered** (fluency/perplexity vs. knowledge vs. reasoning vs. instruction-following) and gradient-norm telemetry per module. Against attack 1: report results under *two* pre-registered matching conventions (global-norm and per-layer) — if the conclusion is invariant to the convention, the matching objection dies. Against attack 3: the stratified design *is* the answer — "you need only X% real text, and only for knowledge retention" is a quantitative, directly cost-cutting recipe even in the mushy middle. Against attack 2: Robins never ran the multimodal gradient-interference regime nor content-stratified retention; cite and subsume. Cheap (fine-tuning runs only, no pretraining).

**Verdict: SURVIVE.** A causal lever (rehearsal composition), a decisive cheap design, and — critically — even the partial outcome yields an actionable recipe with real cost implications.

---

## K3. C-0093 — Dimensional collapse doesn't hurt transfer

**Reviewer #2 attacks:**

1. **You intervene on the wrong variable.** Rank levers (projector bottlenecks, decorrelation strengths) act on the *projector/embedding* space; transfer is evaluated on *backbone* features, whose spectrum your bottleneck may barely touch. The anti-collapse camp answers every flat curve with "you never collapsed the representation that matters." The construct-validity hole is structural, and the idea's own risk note admits the levers are confounded ("may affect quality through other channels").
2. **The escape hatch is built into the hypothesis.** "Transfer is flat *except at extreme collapse*" — so any observed harm is reclassified as "extreme," and any flatness as support. Without a pre-committed quantitative boundary the claim is unfalsifiable, and no principled boundary exists.
3. **The fatal one — nobody's practice depends on the causal claim.** This is an analysis-only paper aimed at a *motivational story*. RankMe (Garrido et al. 2023) claims prediction, not causation — and prediction is what practitioners use it for (label-free hyperparameter selection). VICReg-family regularizers are justified in their own papers by end-task gains, not by rank metrics. So even a perfect execution — flat transfer across an order of magnitude of rank — retires **no method, no metric, no workflow**. It corrects rhetoric. Per this stage's instructions, that is precisely the paper I must kill.
4. **Partial dissociations are already in the literature.** MIM models transfer excellently from low-effective-rank-ish features (Park et al. 2023 territory); the correlational story already has published counterexamples, further deflating the surprise.

**Could any experiment shut me up?** Only by rescuing actionability: demonstrating that RankMe-guided model selection *actively picks worse checkpoints* in a realistic workflow. But that contradicts RankMe's own validated selection results, so the rescue experiment is expected to fail. Multiple independent rank levers (bottleneck + decorrelation + explicit spectral projection on backbone features) fix attack 1 at real cost, but attacks 2 and 3 stand regardless of the result.

**Verdict: KILL.** Analysis-only; no decision changes in either outcome.

---

## K4. C-0128 — Generative editing enables causal measurement of context reliance in segmentation

**Reviewer #2 attacks:**

1. **Artifact leakage is worst-case for dense models.** Diffusion inversion/insertion leaves low-level fingerprints; segmentation networks respond to every pixel. Your "context reliance" score may be an *artifact reliance* score. And the proposed "artifact-only control edits" are ill-defined: there is no edit that carries the artifacts of a semantic change without the semantic change.
2. **The instrument is editor-dependent — so it isn't an instrument.** The editor inpaints context-consistent content (shadows, reflections, co-occurring textures): a "removal" doesn't remove context, it substitutes the *generator's prior* over the same context. Different editors yield different scores; a measurement that depends on the measuring device's training data is not a measurement.
3. **The robustness-linkage arm is a 20-point correlation.** Correlating class context-scores with cross-dataset transfer drops over 20 classes is hopelessly underpowered and confounded by class frequency, object scale, and annotation convention.
4. **Prior-work squeeze.** Counterfactual-editing evaluations exist for classifiers; occlusion/cut-paste context studies exist for dense tasks (Rosenfeld et al. 2018). A reviewer frames your contribution as "instrument swap plus a score."

**The experiment that shuts me up (exists, realistic):** Three mandatory validity legs. (i) **Null-edit calibration:** invert-and-reconstruct every image with *no* semantic change; the per-model response to null edits is the artifact noise floor, and all context effects must be reported as excess over it. (ii) **Cross-editor invariance:** compute the score with ≥2 unrelated editing systems; report per-class score agreement — invariance is evidence the score measures the scene, not the editor. (iii) **Physical anchor:** a real-photo counterfactual subset — video frames where objects naturally enter/leave an otherwise-static scene provide genuine paired present/absent context at zero generative artifact; validate the synthetic score against the real-pair score on the overlapping classes. Then scale the robustness linkage to 100+ classes across 3 datasets with frequency/scale partialled out. All three legs are runnable with existing tools and data; leg (iii) is the one no artifact objection survives.

**Verdict: SURVIVE.** It has a causal instrument (interventions on inputs), a per-class actionable output (which classes need context-decorrelation during training), and a concrete validation path that answers the artifact objection with physics instead of promises.

---

## K5. C-0229 — Multi-task pretraining's benefit is the data, not the tasks

**Reviewer #2 attacks:**

1. **The pooled-image control may not be constructible where it matters.** Real multi-task corpora have disjoint per-task label types; "single-task on pooled images" needs one task's labels on all images. Pseudo-labeling smuggles a teacher into the control arm; restricting to fully-labeled corpora shrinks you to COCO/synthetic scale, and the celebrated claims you're deflating (4M, Florence) live 100× above you.
2. **Matched compute is a war you can't win.** Multi-task arms spend capacity on heads/task tokens; every compute-matching convention advantages one arm, and whichever arm loses, its camp will claim under-training. This exact fight has burned prior comparison papers.
3. **The likely result is the known middle.** Task synergy for related pairs and interference elsewhere is Standley et al. (2020). Your deflationary headline needs a near-total null for task diversity, which is a priori implausible — depth supervision demonstrably teaches geometry that classification labels don't.
4. **Scale-transfer objection.** Whatever decomposition you measure at COCO scale, the multi-task-pretraining camp answers "emergent task synergy at web scale," and you cannot follow them there.

**The experiment that shuts me up (exists, realistic):** Run the decomposition where the control is *exact*: fully multi-labeled corpora — COCO (boxes, masks, captions, keypoints) and a fully-annotated synthetic corpus (e.g., Hypersim: depth, normals, semantics on identical images). Arms: {multi-task on pooled images, each single task on pooled images, each single task on own-subset images}, ≥2 compute-matching conventions reported side by side (attack 2 becomes a robustness table instead of a war), transfer evaluated on held-out tasks/datasets. The deliverable is not the deflationary headline but the **decomposition number**: what fraction of the multi-task advantage survives when image diversity is equalized. That number does not exist in the literature at any scale (Stage-3 search confirmed), and it directly prices the field's core cost decision — buy more label types or more images. Scale-transfer (attack 4) is answered by a two-point scale sweep (COCO-scale and a 10× pooled web-image arm with one task) showing the decomposition's direction is stable.

**Verdict: SURVIVE.** Arm assignment is a genuine causal lever; the fully-labeled-corpus design makes the control exact rather than approximate; either direction of the decomposition changes a real investment decision.

---

## K6. C-0276 — The many ADE20Ks: split drift breaks cross-paper comparability

**Reviewer #2 attacks:**

1. **This is the purest "we ran an audit" in the batch — no hypothesis is at risk.** Everyone already believes protocol drift exists; you measure its size. Large spread → "we suspected as much"; small spread → a boring null. No model-level claim, no mechanism, no lever on any system except the field's manners. The instructed extra-harsh criterion applies with full force.
2. **Attribution requires a within-framework factorial, which dissolves the headline.** Cross-framework deltas bundle dozens of divergences. To attribute drift to specific conventions you must run a factorial over conventions inside one framework — at which point "6 frameworks" is decoration and the factorial is the protocol ablation individual papers already run piecemeal.
3. **"Exceeds claimed SOTA deltas" needs a literature-mining arm with cherry-picking risk.** The comparison target (distribution of claimed improvements) is itself a contested measurement; reviewers will attack the denominator.
4. **Venue mismatch.** Even executed perfectly, this is datasets-and-benchmarks infrastructure or a reproducibility-track artifact — a checksummed eval harness plus a correction table. As a main-track submission, Reviewer #2 writes "valuable engineering, not a research finding," and is right.

**Could any experiment shut me up?** No — the problem is not experimental risk (execution is easy and the result is certain to be nonzero); the problem is that no experiment can install a causal lever or a decision that changes. "The field should standardize" is a call to action, not a finding. The strongest version (fixed-checkpoint factorial + correction table) is exactly the hygiene appendix another paper should carry.

**Verdict: KILL.** Route the fixed-checkpoint protocol harness into the surviving evaluation-heavy projects (C-0310, C-0302 both need protocol-controlled evaluation) as infrastructure; do not spend a paper slot on it.

---

## K7. C-0302 — Last-layer group-robustness fixes fail on spatially entangled bias

**Reviewer #2 attacks:**

1. **Predicted failure is suspiciously safe — strawman risk.** DFR (Kirichenko et al. 2023) claimed last-layer sufficiency for *classification*. Nobody published the claim for dense prediction; refuting an unclaimed extension invites "who said otherwise?" If the paper's spine is "a 1×1-conv readout can't fix pixel-level bias," a reviewer calls it obvious and moves on.
2. **Planted bias is a caricature.** "Class A always on background B" is a 100%-correlation cartoon; natural dense bias is graded co-occurrence. Results on the cartoon move nobody.
3. **The constructive arm risks being a hyperparameter sweep.** "Which layer suffices" without a transferable principle is a per-dataset knob.
4. **Adjacent prior.** Shortcut learning in dense medical segmentation (e.g., treatment-artifact shortcuts) is documented; a reviewer will claim the phenomenon is known qualitatively.

**The experiment that shuts me up (exists, realistic — and the outcome is genuinely open):** The rescue is the **dissociation design**: identical images, identical planted correlation, two readouts — a classification head and a dense head. DFR fixes the classifier; does it fix the segmenter? This is *not* foreordained: DFR's thesis is that core features are learned despite the bias and only the readout is contaminated. A per-pixel 1×1 readout re-weights channel evidence *locally* — if local evidence is intact, last-layer reweighting could genuinely recover worst-group IoU. Either outcome is informative: recovery extends a celebrated cheap fix to dense tasks; failure localizes bias in spatial feature *mixing* and dissociates the two task modes on the same images (attack 1 dies — the dissociation, not the failure, is the finding). Add: a correlation-strength dial (attack 2 → dose-response on graded bias), one natural-bias dataset (e.g., context-entangled classes in Cityscapes/ADE), and a **retraining-depth curve** (retrain top-k blocks on balanced data) yielding a "debiasing depth" quantity comparable across bias types — the transferable, actionable deliverable that answers attack 3. All cheap: planted-bias datasets and head retraining.

**Verdict: SURVIVE.** Controlled causal levers (bias strength, retraining depth), a genuinely open outcome on a high-profile result, and a constructive quantity practitioners can use.

---

## K8. C-0310 — The camera ISP is a bigger domain axis than the weather

**Reviewer #2 attacks:**

1. **The headline comparison is apples-to-oranges by construction.** "ISP shift within realistic device ranges" vs. "moderate weather" — both ranges are author-chosen. I can make either axis win by widening its range. Without a principled common scale the headline is unfalsifiable, and "bigger than the weather" is marketing.
2. **The data may not exist.** RAW captures with dense labels are nearly absent (PASCALRAW is small and detection-only). Label transfer from processed frames imports its own artifacts into the ground truth. The core experiment may be infeasible at credible scale.
3. **The actionable arm is partially owned.** Rawgment (Yoshimura et al., CVPR 2023) already does noise-accounted RAW-domain augmentation through the ISP and shows large robustness gains — "ISP randomization as augmentation" will be reviewed as Rawgment's sibling. Cross-sensor domain gap is also a documented phenomenon in AV datasets; a reviewer says you renamed it.
4. **Effect concentration claim (texture-defined classes) is an untested rider** that widens the attack surface without strengthening the spine.

**The experiment that shuts me up (exists, realistic):** Kill the incommensurability with **real-distribution anchoring**: (i) ISP axis = render identical RAW frames through N *actual* pipelines (dcraw/RawTherapee profiles, phone SDK pipelines, automotive ISP configurations) — the spread across real devices, not an author-chosen grid; (ii) weather axis = real paired conditions (ACDC clear↔fog/rain/snow on matched scenes). Then "typical cross-device shift vs. typical clear→adverse shift" is a comparison between two *empirical* distributions, and the headline is falsifiable. Data: RAW driving/scene sets exist (e.g., RAW variants of driving captures, PASCALRAW, new capture at modest scale); dense labels via annotation of the *shared underlying scene* (label once per RAW frame, valid across all renders — the intervention never moves a pixel, only re-renders it; this is the design's quiet strength: ground truth is exactly invariant across the treatment). Against attack 3: Rawgment optimizes low-light recognition robustness via noise-aware augmentation; it never measures the ISP axis *as a domain-shift magnitude* nor compares it to weather — cite it as the augmentation baseline in the training arm.

**Verdict: SURVIVE.** True intervention (re-rendering), label-invariant treatment, deployment-critical actionable output (which axis to budget robustness engineering against; ISP randomization arm with Rawgment as baseline). Mandatory condition: real-device anchoring; without it, kill on attack 1.

---

## K9. C-0320 — Mild shifts compound super-linearly

**Reviewer #2 attacks:**

1. **"Super-linear" is a units artifact until proven otherwise.** Accuracy is bounded; losses near ceiling/floor cannot compose additively *by arithmetic*. In error-rate, log-odds, or independent-failure space the same data can look sub-linear, additive, or super-linear. This is the classic additive-vs-multiplicative interaction trap (epidemiology fought it for decades, without resolution). Every choice of scale I dislike, I attack; the paper has no principled defense because none exists.
2. **The null is the likely outcome and it is worthless.** If composition is approximately independent-multiplicative — the boring default that bounded-metric arithmetic predicts — the paper is a null with no lever. If it's super-linear, the actionable consequence is "benchmarks should include compositions," i.e., a benchmark proposal: an audit conclusion without a causal lever, squarely in the instructed extra-harsh zone.
3. **The mechanism arm is hand-waving.** "Super-linearity grows with reliance on a fragile feature family, identifiable via frequency analysis" — frequency analysis as mechanism is the weakest tool in the robustness drawer, and the claim has no intervention attached.
4. **Prior-work adjacency.** 3D Common Corruptions composes corruptions realistically; Mintun et al. (2021) studies corruption-augmentation interaction structure; robustness suites report combined conditions in appendices. The "no composition law exists" novelty claim survives only until one appendix table surfaces.
5. **Frozen-model evaluation only.** Nothing in the design touches a model. Even a confirmed composition law describes; it does not enable.

**Could any experiment shut me up?** A pre-registered functional form on a defensible scale (excess over independent-failure baseline) plus a *mechanistic intervention* (train models with known fragile-feature reliance and show predicted super-linearity) would answer attacks 1 and 3 — but at that point the paper has become a different, training-heavy project, and the deliverable is still a descriptive law whose consumer is a benchmark designer. The composition question is real but it is an appendix to someone else's robustness paper, not a spine.

**Verdict: KILL.** Analysis-only, scale-dependent headline, no causal lever; the strongest fix converts it into a paper this pipeline isn't proposing.

---

## K10. C-0332 — Does "accuracy on the line" survive dense prediction?

**Reviewer #2 attacks:**

1. **Scope-test audit with no lever.** Run N models, fit lines — nothing is intervened on. If linear: "the law generalizes," nothing changes anywhere. If nonlinear: the field shrugs — mIoU is a nonlinear aggregate of per-class ratios, so deviations from linearity are plausibly *Jensen's-inequality arithmetic*, not a robustness phenomenon. The paper risks discovering that averages of ratios don't behave like ratios of averages.
2. **The model panel can't support the fit.** Miller et al. had hundreds of diverse classifiers; public segmenters number a few dozen and share backbones, pretraining data, and codebases. Trend fits over ~30 correlated points are fragile, and training a controlled panel (the idea's own fallback) is exactly the expensive arm the cheap-study pitch was supposed to avoid.
3. **The operational need is already served.** Predicting segmentation performance without ground truth is a mature medical-imaging subfield — Reverse Classification Accuracy (Valindria et al., IEEE TMI 2017) and its conformal successors estimate per-case segmentation quality under shift. The deployment-gating use case has a per-image tool; a population-level line is a weaker instrument for the same decision.
4. **The constructive escape is speculative.** A corrected estimator from residual structure (boundary-vs-interior, per-class lines) *might* fall out; the proposal doesn't design for it, and without it the paper is a scope-annotation on someone else's law.

**Could any experiment shut me up?** Only the constructive version: demonstrate a *working* OOD-mIoU estimator for dense tasks that beats agreement-on-the-line and RCA baselines. That is a different paper (an estimation-method paper), and its feasibility is unknown from here. The scope test alone — the actual proposal — ends in either "law holds" (nothing changes) or "law breaks" (attributable to metric arithmetic; nothing changes). Per the extra-harsh instruction on audits, this dies.

**Verdict: KILL.**

---

# PART 2 — Stage-3 MUTATEs (M1–M8)

## M1. C-0002 — Orthogonal-classifier + resolution-matched audit of OV-seg text towers on seen classes

**Reviewer #2 attacks:**

1. **The target claim is not load-bearing.** OV-seg papers use text towers as an *open-set interface*, not as a seen-class booster; the careful ones already separate seen/unseen tables. Show me the paper that claims semantic text geometry drives *seen-class* mIoU — without receipts, this audit refutes a claim nobody staked.
2. **Both outcomes are nulls.** Random-orthogonal collapses on seen classes → the field's implicit assumption confirmed, nothing learned (the mutation's own kill condition concedes this). Random-orthogonal recovers seen-class mIoU → OV-seg authors reply, correctly, "the text tower's value is that a *new* class costs one text embedding; your control cannot even be applied to an unseen class without retraining." The utility argument is untouched by the seen-class decomposition.
3. **Known-control transplant.** Hoffer et al. (2018) established fixed/random classifiers lose little on seen classes. Porting the control to pixel-softmax is an instantiation; "the dynamics might differ under spatial competition" is a hope, not a hypothesis with a mechanism.
4. **Analysis-only.** No training recipe, no method, no deployment decision changes — a decomposition table is the entire deliverable.

**Could any experiment shut me up?** No. The execution is easy and clean, and that is the problem — a perfectly executed audit of a non-load-bearing claim. The one interesting cell (shuffled text embeddings *hurting* via wrong semantic neighbors) is an ablation row, not a paper.

**Verdict: KILL.**

---

## M2. C-0014 — Tuning-budget-matched post-hoc filter equivalence audit of attention surgery

**Reviewer #2 attacks:**

1. **Low-stakes target.** Training-free CLIP segmentation is a benchmark micro-genre; nobody deploys it. Even total victory — "a tuned bilateral filter matches SCLIP/GEM/CLIP-Surgery/NACLIP" — deflates a handful of analysis sections in a niche. The instructed harshness on audits without levers applies: the deliverable is a matched-budget table.
2. **NACLIP half-owns the result.** The Gaussian prior is already published *as a method inside attention*; "post-hoc vs. in-attention" is a fine distinction that a reviewer collapses to "known, with extra steps."
3. **Equivalence is statistically treacherous.** The claim needs pre-registered equivalence margins (TOST-style) per benchmark; underpowered per-dataset differences will be spun by both camps, and boundary metrics (the mutation's own risk note) likely break the equivalence — at which point the headline becomes "smoothing matches on mIoU but not boundaries," i.e., *the surgery papers were right where it matters*.
4. **Moving target.** The surgery family grows by three methods a year; by review time, "you didn't test X" is a free rejection.

**Could any experiment shut me up?** The design is cheap and clean (reimplement 3–4 methods, matched validation budget, paired bootstrap) — but cheapness isn't the bar. The best case is a hygiene result ("report smoothing-matched baselines") for a subfield with no deployment surface. Kill on stakes.

**Verdict: KILL.**

---

## M3. C-0047 — Directional asymmetry in VLM spatial reasoning tracks raster serialization

**Reviewer #2 attacks:**

1. **The frozen audit (step 1, the "cheap kill") cannot control its confounds.** Horizontal-vs-vertical accuracy gaps can come from text priors (left/right token frequency), photographic image statistics (horizontal layouts dominate), benchmark annotation habits, or aspect-ratio handling. "Controlling for relation-frequency priors in training text" is impossible for models whose training text is closed. Kamath et al.'s per-relation tables may already show the asymmetry — making step 1 a re-read of published numbers with an unverifiable causal gloss.
2. **The causal arm has a built-in escape hatch.** "Small VLM retrain with column-major serialization" — if the asymmetry doesn't flip, the authors say "scale too small," and no budget this pipeline commands closes that door. An experiment whose null is always excusable is not a kill condition.
3. **The lever is aging out from under the paper.** Qwen2-VL-class models use 2D/multimodal RoPE; LLaVA-NeXT-class models use tiled encodings. Raster-order token locality is an architectural cohort, not a standing property; by publication the finding annotates last year's models.
4. **Stakes.** Even fully confirmed, the design implication is "consider serialization order in 1D-PE VLMs" — a free dial on a shrinking architecture class.

**Could any experiment shut me up?** Partially, and credit where due: the strongest version is elegant — freeze LLM and encoder, train *only the projector* under raster/column/Hilbert orders (adapter training is genuinely cheap), evaluate on synthetic scenes with template-symmetric prompts. Same LLM across arms kills the text-prior confound. But attack 2 stands (adapter-scale nulls are excusable), and attacks 3–4 cap the payoff at a footnote for a receding architecture cohort. Against the survivors it's competing with, it loses the slot.

**Verdict: KILL** (closest call among the kills; revive only if the frozen audit in step 1 shows a large, replicated asymmetry that survives synthetic-scene controls — that free evidence would change the calculus).

---

## M4. C-0068 — Adam-moment transplant isolates optimizer transients from update rank in fine-tuning forgetting

**Reviewer #2 attacks:**

1. **The transplant is plausibly LR hygiene in disguise.** Transplanted second moments shrink early effective steps — so does a tuned warmup. The design's own arm 3 (per-parameter LR mimicking the preconditioner) *is* the transplant by another name; if arms 2 and 3 coincide, the finding reduces to "smaller early steps forget less," which is standard practice, and Biderman et al. tuned their schedules. The paper must prove the per-parameter *structure* of the moments matters beyond their magnitude — an arm the proposal doesn't contain.
2. **The zone is instructed-harsh and actively mined.** Continual-pretraining work (LR rewarming, optimizer-state resumption — Ibrahim et al. 2024 lineage) already quantifies fresh-vs-warm optimizer effects on forgetting in adjacent settings; the LoRA-vs-full-FT forgetting literature updates quarterly. Scoop risk is maximal and the residual delta ("attribute a *fraction* of the gap") shrinks monthly.
3. **The expected result is a mushy fraction.** "Transplanted moments close 20% of the gap" changes no one's method choice; LoRA is used for memory reasons anyway, so even a large fraction doesn't alter practice. Actionability is thin.
4. **Their own kill condition (closes ≈0%) is a null in a crowded zone** — unpublishable.

**Could any experiment shut me up?** Yes, one control would do it: a **shuffled-transplant arm** (second-moment magnitudes permuted across parameters within layers, preserving the global step-size distribution). Structured ≫ shuffled at matched global scale would prove a genuine per-parameter mechanism beyond LR hygiene. But even with that arm, attacks 2–3 stand: the best case revises the *decomposition* of a narrative inside a fast-moving literature this pipeline was explicitly told to treat harshly, with no practice change downstream.

**Verdict: KILL.**

---

## M5. C-0099 — Post-hoc whitening audit across published SSL checkpoints

**Reviewer #2 attacks:**

1. **The checkpoint zoo cannot support the conclusion.** Published checkpoints differ in data, epochs, architectures, and augmentations; whatever spread whitening removes or leaves, attribution to "method family" is impossible. The controlled version of this question — matched recipes — is solo-learn's territory, and it already found small gaps. The audit measures zoo variance and calls it insight.
2. **Both outcomes are dead ends.** Spread shrinks → "linear-probe protocol sensitivity is known" (probe-hyperparameter papers exist); spread survives → null. There is no branch where a decision changes: SSL methods justify themselves by fine-tuning and task suites, where a post-hoc whitening of frozen probes is irrelevant.
3. **Whitening on transfer data is a leak.** Estimating the whitening transform on the evaluation distribution is mild test-time adaptation; the "pure bookkeeping" framing quietly changes the evaluation question.
4. **Analysis-only, no lever, afternoon-scale.** The extra-harsh criterion was written for this paper.

**Could any experiment shut me up?** No. The clean version requires matched-recipe retraining (already published, small gaps) and the cheap version is unattributable (attack 1). There is no experimental path to a defensible, decision-changing claim.

**Verdict: KILL.** Easiest kill in the batch.

---

## M6. C-0158 — Correlated-noise mechanism: uncertainty sampling selects LLM-annotator failures; decorrelated acquisition fixes it

**Reviewer #2 attacks:**

1. **"Why do active learning at all?"** LLM labels are cheap; the realistic pipeline is annotate-everything-then-filter, which makes acquisition order irrelevant and your setting an optimization of a non-binding constraint. This is the deepest attack — it targets the premise, not the execution.
2. **Half the mechanism is folklore.** That hard items are hard for both learner and LLM annotator is intuitive and partially documented (Stage-3 search found adjacent observations). The correlation study alone is a workshop poster.
3. **The fix has a circularity problem.** "Acquisition penalized by predicted annotator error" needs an annotator-error predictor without ground truth — itself an open calibration problem. If you can predict LLM error reliably, you've solved a bigger problem than AL.
4. **Generality risk.** The effect size rides on the learner-annotator difficulty correlation, which varies across task/annotator pairs; the expected deliverable is a mixed grid with hedged conclusions.

**The experiment that shuts me up (exists, realistic):** (i) Against attack 1 — pick settings where the budget genuinely binds: *dense* annotation by VLM agents (per-item mask generation at real compute cost) and frontier-model annotation at scale; in both, per-item cost is real money and acquisition order matters. This is also this cluster's LLM-ANNOT charter, so the setting is native, not contrived. (ii) The mechanism study is cheap and decisive: ground-truthed pools, measure the item-level correlation between learner uncertainty and annotator error directly — a number, not an argument. (iii) Against attack 3 — instantiate the error predictor with self-consistency/ensemble disagreement of the annotator (no ground truth needed), and include the honest baseline the deep attack implies: **random acquisition** and **annotate-everything + noise-robust training** at matched total cost. If decorrelated acquisition beats both at fixed budget across 3 text + 1 vision datasets, the mechanism and the fix stand; if annotate-everything wins, publish that as the finding (it, too, changes practice — it says AL+LLM pipelines should be dismantled).

**Verdict: SURVIVE.** It is the rare entry with a mechanism, a lever (the acquisition function), a cheap decisive first measurement, and a design where *every* branch — including the premise-killing one — yields an actionable conclusion for a pipeline pattern people actually run.

---

## M7. C-0355 — Annotation-budget crossover: when the next head-class label beats a tail-class label, predicted by a feature-sharing score

**Reviewer #2 attacks:**

1. **The crossover likely lives where nobody operates.** At benchmark scales, head classes sit deep in diminishing returns (log-linear data scaling); the marginal head label's value for tail performance is ≈0. The regime where head labels beat tail labels — if it exists — is the tiny-budget regime, of no consequence to real annotation campaigns. The expected deliverable: "a crossover exists in a contrived corner."
2. **Anachronism — the predictor dissolves the problem it predicts.** The feature-sharing score is computed on a foundation backbone. But if you have a foundation backbone, tail recognition is a few-shot/frozen-feature problem and the head-vs-tail allocation economics change completely. The setting is stranded between eras: allocation matters for from-scratch training (rare), while the instrument presumes pretrained features (which void the question).
3. **Simulated markets aren't markets.** ImageNet-LT-style benchmarks are subsampling artifacts; "buying labels" sweeps there map to no real annotation decision.
4. **Statistical cost.** Crossover-point estimation needs many runs per (budget, allocation) cell; the grid is expensive and the estimated quantity fragile.

**Could any experiment shut me up?** Only a real annotation domain (medical, wildlife) with genuine from-scratch or domain-pretrained constraints — a heavy, partnership-dependent project this pipeline can't guarantee, and even there attack 2 recurs as foundation models penetrate those domains. The underlying transfer science is owned (OLTR, Kang et al.); the economics layer is stranded.

**Verdict: KILL.**

---

## M8. C-0365 — Failure-mode-matched revival: unmet classical priors predict which pre-DL components help which foundation model

**Reviewer #2 attacks:**

1. **The "principle" is unfalsifiably flexible at n=12.** Failure profiles (boundary error, smoothness violations, geometric consistency) and component priors are matched *qualitatively*; with a 3-model × 4-component grid, scoring 8–9/12 by common sense (CRF helps where boundaries are bad — who knew?) is near-guaranteed, and the authors grade their own predictions. Twelve cells cannot establish a principle; they can only decorate one.
2. **The effect budget is inside the noise.** CRF-decline results show classical post-processing gains on strong models are fractions of a point. The paper proposes to predict the *sign* of ~0.3-mIoU effects — an ill-conditioned target where implementation quality (the idea's own risk: fair tuning of classical components) dwarfs the signal.
3. **Practice has a dominating alternative.** Where a prior is unmet, the field fine-tunes or distills a better decoder; bolting on a tuned 2009 component is dominated in accuracy-per-engineering-hour. Even a validated matching principle changes few decisions.
4. **The survey ghost lingers.** Stage 3 mutated this from an unfocused survey; the mutation kept the grid and added a rubric. The rubric is the weak part.

**Could any experiment shut me up?** Scale (more components, models, datasets, pre-registered quantitative predictions) fixes attack 1 in principle, but attack 2 caps the value: you'd be pre-registering predictions about effects the size of evaluation noise. No realistic experiment makes small effects large.

**Verdict: KILL.**

---

# Summary

| # | ID | Stage-3 status | Reviewer #2 verdict | Deciding factor |
|---|----|----|----|----|
| K1 | C-0028 | KEEP | **SURVIVE** | Hardness-matched control isolates the mechanism; training lever |
| K2 | C-0090 | KEEP | **SURVIVE** | Stratified content-free controls; even partial result is a cost-cutting recipe |
| K3 | C-0093 | KEEP | KILL | Analysis-only; no metric, method, or workflow depends on the causal claim |
| K4 | C-0128 | KEEP | **SURVIVE** | Null-edit calibration + cross-editor invariance + real-photo anchor validate the instrument |
| K5 | C-0229 | KEEP | **SURVIVE** | Exact pooled-image control on fully-labeled corpora; prices a real investment decision |
| K6 | C-0276 | KEEP | KILL | Pure audit, no causal lever; route harness into surviving projects |
| K7 | C-0302 | KEEP | **SURVIVE** | Classification-vs-dense dissociation on identical images; debiasing-depth deliverable |
| K8 | C-0310 | KEEP | **SURVIVE** | Real-device anchoring makes the headline falsifiable; label-invariant intervention |
| K9 | C-0320 | KEEP | KILL | Composition "law" is a units artifact; frozen-model audit, no lever |
| K10 | C-0332 | KEEP | KILL | Scope-test audit; likely rediscovers metric arithmetic; RCA serves the use case |
| M1 | C-0002 | MUTATE | KILL | Target claim not load-bearing; both outcomes are nulls |
| M2 | C-0014 | MUTATE | KILL | Low-stakes niche; NACLIP half-owns it; equivalence statistically treacherous |
| M3 | C-0047 | MUTATE | KILL | Escapable null; lever aging out (2D-PE VLMs); closest call |
| M4 | C-0068 | MUTATE | KILL | Plausibly LR hygiene in disguise; instructed-harsh crowded zone |
| M5 | C-0099 | MUTATE | KILL | Checkpoint zoo can't support attribution; both outcomes dead ends |
| M6 | C-0158 | MUTATE | **SURVIVE** | Mechanism + fix + binding-budget settings; every branch actionable |
| M7 | C-0355 | MUTATE | KILL | Crossover lives where nobody operates; predictor dissolves its own question |
| M8 | C-0365 | MUTATE | KILL | n=12 rubric can't establish a principle; effects inside noise |

**Survivors (7):** C-0028, C-0090, C-0128, C-0158(M6), C-0229, C-0302, C-0310.

**Cross-cluster overlap check (A/B keeps skimmed):** no survivor collides with A-cluster keeps (SAM/promptable-segmentation program) or B-cluster keeps (medical program). Nearest neighbors, noted for the portfolio: C-0128's counterfactual-editing instrument is methodologically adjacent to B-0121's counterfactual wrong-support audit (different target, different task); C-0310's sensor-physics thesis rhymes with B-0062/B-0193's "use the sensor physics" spine (different modality, complementary); C-0158 shares the LLM-annotation zone with B-0230/B-0350 but attacks acquisition, not data decomposition or hallucination. No consolidation needed.
