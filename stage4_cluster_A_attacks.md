# Stage 4 — Cluster A Reviewer #2 Attack Report

**Reviewer #2 (Cloud Sub-Agent J) → Supervisor Windows7.**
**Input:** 17 Stage-3 Cluster A survivors (`stage3_cluster_A_keep.md`, branch `cursor/stage3-cluster-a-priorwork-b0e5`), original texts (`stage1_cluster_A_ideas.md`, branch `cursor/stage1-cluster-a-ideas-e2b2`), mutations (`stage3_cluster_A_mutations.md`). Cross-checked against Cluster B keep list (branch `cursor/stage3-cluster-b-priorwork-5dcc`) and Cluster C keep list (branch `cursor/stage3-cluster-c-priorwork-f96e`) — no surviving overlaps; adjacencies noted per idea.

**Protocol:** Each idea was treated as a *submitted paper* and attacked to kill across the axes: novelty, significance, motivation, hidden assumption, confounder, missing baseline, dataset bias, weak metric, unfair comparison, extra params/data/compute, cherry picking, generalization, weak causal evidence, trivial alternative explanation, reproducibility, scalability, practical relevance, paper story. Then a Defense pass: an idea survives **only if a concrete, realistic experiment refutes its strongest attack**. If the core attack cannot be answered by an experiment (because it is definitional, ontological, or a reframing that concedes the data), the idea is killed regardless of how pretty the measurement is.

**Outcome: 17 → 7 SURVIVE, 10 KILLED.**

| Verdict | IDs |
|---|---|
| SURVIVE (7) | A-0002, A-0017, A-0061, A-0062, A-0107, A-0178, A-0271 |
| KILL (10) | A-0003, A-0016, A-0032, A-0068, A-0078, A-0128, A-0134, A-0136, A-0227, A-0314 |

---

# SURVIVORS

---

## A-0002 — Positional-encoding aliasing causes point-prompt instability → **SURVIVE**

### Attacks

1. **Hidden assumption / weak causal evidence (STRONGEST).** The paper's headline mechanism assumes SAM's prompt encoder has a "positional-embedding frequency grid." It does not. SAM encodes click coordinates with *random Fourier features* (`PositionEmbeddingRandom`: a fixed Gaussian frequency matrix through sin/cos) — a continuous encoding with a broad spectrum, not a grid. There IS a 16-px grating in the system, but it belongs to the *image path*: the 16-px patch tokenization and the 64×64 dense PE the decoder attends over. So when the Fourier analysis of flip maps finds periodicity (it will), the paper cannot attribute it to the prompt encoder: at least three architectural gratings (patch grid, dense image PE, prompt RFF spectrum) predict overlapping structure. The proposed evidence — "flip maps are periodic" — is consistent with all three; the causal claim names one.
2. **Practical relevance.** RClicks-style measurements show real users' click variation is tens of pixels; the phenomenon under study lives at sub-8-px scale. Even if the mechanism is nailed, no human-facing behavior changes. "Guides where robustness work should focus" is a hope, not a consequence.
3. **Unfair comparison / extra training.** The intervention arm ("retrain the prompt encoder with smoothed positional features") confounds anti-aliasing with retraining itself: any fine-tuning regularizes and can smooth flip maps. Without a matched control retrain (same steps, original PE), the intervention proves nothing about aliasing.
4. **Weak metric.** "Flip" requires an arbitrary IoU-change threshold; flip rates are threshold-sensitive and object-ambiguity-heterogeneous, so pooled spectra mix mechanisms.
5. **Novelty pincer.** Stable-SAM already attributes instability to decoder attention drift and ships a fix; TETRIS/RClicks already characterize instability. Reviewer: "a third paper on click instability needs to change a decision, not add a spectrum."

### Defense pass

The attribution attack (1) is refutable by a **white-box, training-free intervention** that the attack itself overlooks: the RFF matrix is a known, fixed, manipulable object, and in SAM's code the point-embedding path can be modified *independently* of the dense image PE (`_embed_points` vs `get_dense_pe`), even though they share the module. Bandlimiting only the prompt-side RFF at inference isolates the prompt-encoder channel with zero retraining — killing attack 3 as well (no retraining involved). White-box access also means the RFF spectrum is known *exactly*, so the two competing hypotheses (RFF-caused vs patch-grid-caused) make *quantitatively different predictions* for the flip-map spectrum — a discriminating test, not a consistency check. Attack 2 is answered by moving the consequence from humans to machines: SAM's automatic mask generation (AMG) prompts on a fixed 32×32 grid, so grid-phase-dependent instability directly moves recall in the field's most-used auto-annotation mode.

### The experiment that shuts the reviewer up

On ≥500 objects, compute sub-pixel flip maps and their 2-D spectra. Then: (a) **path-specific spectral surgery** — attenuate the top-frequency rows of the point-path RFF matrix at inference only, with an equal-energy random-row attenuation control; (b) compare measured flip-map spectra against the *predicted* spectra under the RFF hypothesis (known matrix) vs the 16-px grid hypothesis; (c) **AMG grid-phase test** — shift the 32×32 prompt grid by half a period and measure mask-recall change. Pass = flip periodicity and rate track the point-path RFF manipulation (not the control), and grid-phase shifts move AMG recall measurably. Fail (flips insensitive to RFF surgery) = mechanism falsified — publishable as a clean negative that redirects to the patch grid.

**Verdict: SURVIVE.** Cheap, white-box, causal; both outcomes settle a mechanism question two prior papers only gestured at.

---

## A-0017 (M1) — Causal memory surgery for SAM2 (upper-bound diagnostic) → **SURVIVE**

### Attacks

1. **Trivial alternative explanation (STRONGEST).** "Targeted deletion of post-error memory entries" is, operationally, *resetting the tracker* — the oldest baseline in tracking. Practitioners already know restarting SAM2 at reappearance fixes lock-in; SAMURAI and DAM4SAM's published gains already lower-bound the memory-borne failure share. The paper adds a number to a question the fix papers answered by fixing.
2. **Oracle dependence.** Deletion timing uses ground-truth reappearance — a strong oracle (the idea concedes this). The "upper bound" is an upper bound *given an oracle no deployment has*.
3. **Cherry picking / dataset bias.** "Collect 200 organic failures" invites selection toward sequences where reappearance is unambiguous and reset trivially works; the reversible fraction is then inflated by construction.
4. **Scooping risk / significance decay.** SAM2-memory is a crowded, fast-moving subfield; memory-ablation diagnostics are an obvious next step for the SAM2Long/SAMURAI lineage. A diagnostic arriving after the fixes reads as a post-mortem.

### Defense pass

Attack 1 conflates a *repair heuristic* with a *decomposition instrument*. A reset is a fix; the paper's product is a per-sequence measurement — the memory-borne (reversible) vs representation-borne (irreversible) share of organic failure — whose validity is independently checkable: if the per-sequence reversible fraction *predicts* the per-sequence gains of two independent prevention methods, the diagnostic is measuring something real that end-to-end scores don't expose. That predictive-validity test is concrete, cheap, and preregistrable, and it distinguishes this from "restart the tracker." Attack 2 is absorbed by the framing: an oracle-timed upper bound is exactly what you want to score prevention methods against (how much of the achievable ceiling does SAMURAI capture?). Attack 3 is answered by a fixed failure-harvesting protocol (all failures on LVOS/VOTS long-video suites, no manual curation) plus reporting the ambiguous-reappearance stratum separately.

### The experiment that shuts the reviewer up

On **all** organic SAM2 failures harvested by a fixed protocol from LVOS+VOTS (≥200), run three arms at GT reappearance: (i) targeted deletion (remove post-error entries, keep pre-error object memories), (ii) full reset to conditioning-frame memory only (the "trivial baseline"), (iii) no-op. Report reversible fractions per arm; if (i) > (ii), pre-error memories are load-bearing and surgery ≠ reset. Then the preregistered kill-shot: per-sequence reversible fraction must predict per-sequence gains of SAMURAI and DAM4SAM with r > 0.6. If it doesn't predict, the diagnostic is dead and the paper says so.

**Verdict: SURVIVE.** The predictive-validity leg converts a reset heuristic into a validated decomposition instrument the fix papers don't provide.

---

## A-0061 — Boundary Nyquist limit set by decoder resolution → **SURVIVE**

### Attacks

1. **Triviality / motivation (STRONGEST-a).** Nyquist is a theorem. A mask decoded at 256×256 cannot represent contour frequencies above its sampling rate; measuring that a band-limited system is band-limited requires no experiment. The "boundary Nyquist constant" is computable from the architecture spec sheet.
2. **Dataset bias / weak metric (STRONGEST-b).** Ground-truth contours in COCO/LVIS are polygon annotations — themselves low-pass, with tool-dependent vertex budgets. "Model error at high contour frequencies" measured against polygonal GT quantifies annotation style, not model failure. The instrument reads its own reference noise at exactly the frequencies of interest.
3. **Weak metric (technical).** Contour Fourier descriptors need closed simple contours; masks with holes/multiple components break the parametrization; arc-length vs image-plane frequency ambiguity invites analyst degrees of freedom.
4. **Significance.** HQ-SAM already indicted and fixed the low-res mask pathway empirically. Designers know resolution matters. What decision changes?

### Defense pass

Attack 1 concedes the upper bound but not the operating point — and the operating point is the entire finding. The theorem fixes where error *must* begin; it says nothing about where it *does* begin. If the empirical cutoff sits at the architectural limit, decoders are sampling-limited and raising decoder resolution buys boundary quality (validates the HQ direction, gives a design dial). If the cutoff sits well below the limit, decoders are training/data-limited and resolution increases are wasted — falsifying the field's default fix. Either outcome is decision-changing, and the theorem cannot tell you which world you're in. Attack 2 is fully answerable by choosing references whose bandwidth exceeds the models': synthetic parametric stimuli (star/blob families with controlled curvature spectra, anti-aliased rendering — perfectly known GT) plus DIS-5K/ThinObject-grade fine masks. Attack 3: synthetic stimuli are single closed contours by construction; natural-data analysis restricted to simple-topology instances.

### The experiment that shuts the reviewer up

Parametric synthetic contour suite (controlled curvature spectra) + DIS-5K natural fine-GT. For decoders spanning ≥3 output resolutions (SAM 256² path, HQ-SAM's high-res token path, SAM2, Mask2Former), measure error-energy vs contour frequency; locate the empirical cutoff; compare against each architecture's theoretical Nyquist. The decisive contrasts: (a) cutoff position relative to theory (sampling-limited vs training-limited); (b) cross-model prediction — when decoder resolution doubles, does the cutoff move by the predicted octave? (c) HQ-SAM arm ties into A-0062: did the HQ line raise the cutoff, or sharpen below it? A cutoff that tracks architecture across models is a design law; a cutoff that doesn't is a training-recipe finding. Both refute "no experiment needed."

**Verdict: SURVIVE.** The theorem-vs-operating-point distinction plus synthetic references dissolve both lead attacks; cheap, model-comparative, either-way informative.

---

## A-0062 — HQ-boundary gains vs. soft multi-annotator ground truth → **SURVIVE**

### Attacks

1. **Statistical artifact / weak causal evidence (STRONGEST).** Replacing hard GT with a 5-annotator soft reference adds reference noise. Reference noise attenuates *every* method's measured gain (regression attenuation). Observed "gain shrinkage" under soft references is therefore the predicted artifact of a lower-power metric — not evidence that HQ gains were metric gaming. The paper's headline quantity confounds attenuation with gaming, and cannot separate them as designed.
2. **Null-result risk / paper story.** HQ-SAM's improvements are visually undeniable in side-by-sides (zipper artifacts, hair strands). The likely outcome is "gains shrink by X% but persist," a calibration of a known truth — publishable only if X is startling.
3. **Extra data / feasibility.** 5 annotators × 300 objects of careful boundary tracing is slow and expensive; annotator instructions bias softness (idea's own risk). Reviewers will ask why existing multi-rater resources don't suffice — and if they do, this is "just re-scoring."
4. **Prior-work rebuttal.** Metrics Reloaded: "use NSD with a tolerance τ and annotation imprecision is handled" — the paper must show tolerance metrics and soft references disagree in ranking consequences, or it's redundant with a Nature Methods recommendation.

### Defense pass

Attack 1 — the real threat — has a clean experimental refutation: **stratify by local inter-annotator sigma**. Partition boundary arcs into strata by local annotator disagreement; compare SAM-vs-HQ gains *within* strata. Within a stratum, reference precision is conditioned on, so attenuation is equalized across methods; if HQ's advantage concentrates in high-sigma arcs (below the human-resolution floor), the gain is unverifiable-in-principle — the gaming claim, demonstrated rather than asserted. If the advantage persists in low-sigma arcs where annotators agree, the gains are real and the audit *validates* the HQ line (also a finding; kills attack 2, since either outcome now carries content). Add a **metric-power calibration control**: inject known synthetic localization improvements into predictions and verify the soft-reference pipeline detects them at the claimed sensitivity — directly measuring, not hand-waving, the attenuation attack. Attack 4 is handled by including NSD-with-tolerance as a comparison arm. Attack 3: 1,500 object-annotations is a modest crowdsourcing budget; LIDC-IDRI provides a free multi-rater medical anchor.

### The experiment that shuts the reviewer up

Collect 5-annotator boundaries on 300 objects spanning boundary complexity; re-score SAM, HQ-SAM, and ≥2 successors against (a) hard single-annotator GT, (b) soft references, (c) NSD-τ. Report gain shrinkage **per inter-annotator-sigma stratum**, with the synthetic-injection power calibration. Claim stands iff HQ gains concentrate where humans cannot verify them; claim reverses iff gains survive in the annotator-consensus band.

**Verdict: SURVIVE.** The sigma-stratified design plus injected-improvement calibration converts the strongest attack into a measured quantity.

---

## A-0107 — PEFT forgetting is a readout phenomenon, recoverable by decoder reset → **SURVIVE**

### Attacks

1. **Novelty (STRONGEST-a).** Kumar et al. (ICLR 2022) established the feature-distortion vs. head decomposition (LP-FT) for classification; Biderman et al. measured LoRA forgetting. This is an instantiation on a new model class, and instantiations die at top venues.
2. **Pseudo-problem (STRONGEST-b).** With PEFT the base model is preserved *by construction* — LoRA adapters toggle off. Nobody who cares about zero-shot ability needs a decomposition; they keep the base weights, which they already have. "Dual-decoder deployment solves forgetting" is operationally "keep both models," which is not a discovery.
3. **Hidden assumption.** The swap arms assume {tuned encoder-adapters + original decoder} is a coherent model. Encoder adapters and decoder co-adapt during PEFT; the swap may produce garbage, making the "recoverable fraction" measurement void (idea's own risk).
4. **Generalization.** "5 domains" — if all are medical (the standard SAM-PEFT setting), the readout-locality claim may be a medical-shift artifact, not a property of PEFT.

### Defense pass

Attack 2 has a quantitative rebuttal the attack misses: toggling adapters serves the two capabilities *alternately at 2× encoder cost* — SAM's encoder is >95% of inference FLOPs (ViT-H ≈ 632M params vs ≈ 4M decoder), so adapters-off requires a second full encoder pass per image. The four-way matrix tests something economically different: whether **one** adapted encoder pass can feed **two** 4M-param decoders (tuned = domain, original = zero-shot) simultaneously. If yes, both capabilities ship at ~1× encoder cost with explicit tool-level decoder selection (no domain router needed — the user's tool choice picks the decoder). That is a deployment result "keep both models" does not give you. Attack 1: LP-FT's linear-probe result does not transfer trivially to a prompt-conditioned two-way transformer decoder; the transfer *is* the open question, and a negative answer (swap incoherence, attack 3) refutes LP-FT's account for promptable models — also a finding. Attack 3 is thus not a bug: co-adaptation share is a measured outcome of the matrix, not a failure mode of it. Attack 4: fix domains as 3 medical + camouflage + agriculture/remote-sensing.

### The experiment that shuts the reviewer up

PEFT (LoRA r∈{4,16,64}) on 5 diverse domains; evaluate all four {original, tuned}×{encoder-adapters, decoder} combinations on domain and zero-shot suites (SA-1B holdout + COCO/LVIS points-and-boxes). Deliverables: (a) recoverable-by-decoder-reset fraction of zero-shot loss per domain per rank; (b) the deployment table — domain Dice and zero-shot mIoU of the single-encoder dual-decoder configuration vs adapters-toggling at matched latency/FLOPs; (c) co-adaptation share as rank grows. Pass = decoder reset recovers ≥70% zero-shot at ≤20% domain-gain cost at low rank; fail = readout account falsified for promptable models — publishable either way against the LP-FT prior.

**Verdict: SURVIVE.** The serving-cost asymmetry (95% encoder / 5% decoder) gives the decomposition real deployment teeth, and both matrix outcomes carry content.

---

## A-0178 — Artifact tokens cause prompt-localized segmentation failures → **SURVIVE**

### Attacks

1. **Hidden assumption / applicability (STRONGEST).** The entire study presumes SAM-family encoders exhibit high-norm artifact tokens. The registers phenomenon is documented in DINOv2, OpenCLIP, and supervised ViTs — and Darcet et al. explicitly note MAE-lineage models show weak-to-no artifacts. SAM's encoder is MAE-initialized. If SAM lacks artifact tokens, the paper is void on arrival; SAM2's Hiera is untested territory.
2. **Confounder.** Artifact tokens emerge on low-information, redundant background patches — precisely where click prompts fail anyway (ambiguous prompts on textureless regions). "Clicks on artifact patches fail more" may reduce to "clicks on boring backgrounds fail more." Location-matching on "similar patches" is exactly the kind of matching argument reviewers never believe.
3. **Significance.** Registers already improve aggregate dense metrics; the marginal contribution is localizing *which* failures they fix. A "prompt-hazard map" is a niche product artifact.
4. **Extra params.** Register retrofitting adds tokens/params — an unfair comparison if the fix arm has extra capacity.

### Defense pass

Attack 1 is answered by a **preregistered day-1 gate, widened across the deployed fleet**: norm-map audits cost minutes per model; run them on SAM ViT-B/L/H, SAM2 Hiera, EfficientSAM, MobileSAM, and DINOv2-backed promptable pipelines. The registers literature makes it near-certain *some* deployed promptable encoders exhibit artifacts; the study proceeds on those, and the audit table (which promptable encoders have artifacts at all) is itself a contribution the registers line never produced. If the gate comes up empty across the fleet, the project stops at a one-week cost — an acceptable, honest kill condition. Attack 2 — the matching objection — is dissolved by *intervention instead of matching*: test-time register retrofitting (arXiv:2506.08010) shifts artifact activations into register slots **without retraining and without new trained parameters** (also killing attack 4), toggling the anomaly off at *identical pixel locations in identical images*. Excess failure that disappears under the toggle, at the same pixels, needs no matching argument. Attack 3: connecting a celebrated representation anomaly to user-visible, prompt-conditioned failure is exactly the interpretability-to-product chain the registers papers lack.

### The experiment that shuts the reviewer up

(1) Fleet-wide norm audit (gate). (2) On artifact-positive models: paired within-location design — click-prompt failure rate on artifact patches vs off, then the same images/pixels with test-time registers enabled. Causality = the on-artifact excess failure (reported with location-matched controls as a secondary analysis) drops to baseline under the toggle. (3) Dose-response: excess failure vs artifact-token norm percentile. Report per-model; include the negative models as scope boundaries.

**Verdict: SURVIVE.** The retrofit toggle is a rare clean causal instrument; the gate converts the applicability risk into a cheap, honest go/no-go.

---

## A-0271 — SA-1B pipeline fingerprints and their inheritance → **SURVIVE**

### Attacks

1. **Circularity / triviality (STRONGEST).** Models trained on machine-generated labels reproduce those labels' statistics — this is what supervised learning does. "Students copy the label distribution" is definitional; dressing it as "fingerprint inheritance" is branding. The model-collapse literature already owns the recursion-risk story.
2. **Confounder (content/ontology).** SA-1B's mask statistics differ from COCO's because of *documented design choices* — multi-granularity masks (parts + objects + stuff), licensed high-res photography, privacy blurring — not hidden pipeline artifacts. Curvature-spectrum differences between datasets will be dominated by ontology, and calling the difference a "generator signature" is unfalsifiable as stated.
3. **Extra compute.** Matched-model training on assisted vs. manual data is multiple segmentation-model trainings; reviewers will ask whether the budget bought an answer or an anecdote.
4. **Practical relevance.** Suppose inheritance is confirmed — what changes? SA-1B is already built; SAM is already trained.

### Defense pass

Attacks 1 and 2 share a refutation: **hold images fixed and ablate the pipeline's filters**. The SAM auto-labeling stack is public and runnable; its filter stages are documented (predicted-IoU ≥ 0.88, stability thresholding, NMS, size filters). Relabel the *same* COCO/LVIS images under filter variants {full stack, −stability, −IoU-threshold, −NMS} plus human labels; train matched students per arm. Content and ontology confounds vanish (same images, same teacher, same mask-granularity instructions); what remains attributable to each filter stage is by construction a *pipeline* fingerprint, not a dataset-design difference. Circularity is refuted because the claim is no longer "students copy labels" but *which specific statistics transfer, at what strength, attributable to which documented filter* — including the sharpest sub-claim: complexity **ceilings** (do students fail to produce high-curvature masks even when prompted on objects whose true masks exceed the training-complexity support — an extrapolation failure that mere label-copying doesn't predict and that no one has measured). Attack 3: students are small promptable models (ViT-S scale), five training arms at COCO scale — a university-lab budget. Attack 4: the deliverable is a *measurement instrument plus causal filter attribution* — direct guidance for every group currently building SA-1B-style auto-labeled corpora (which filters to relax and what each costs in inherited ceiling).

### The experiment that shuts the reviewer up

Same-image, filter-ablated relabeling: five label arms on identical COCO/LVIS images (human; full SAM stack; three single-filter ablations). Train matched ViT-S promptable students per arm. Measure: (a) signature statistics (curvature spectra, complexity ceilings, boundary-smoothness distributions) per label arm — which statistic each filter stage creates; (b) student reproduction of each signature on held-out images, incl. amplification vs attenuation; (c) the ceiling test — prompted on held-out high-complexity objects, does the full-stack student's max attainable mask complexity pin to the training ceiling while the human-label student's does not?

**Verdict: SURVIVE.** The filter-ablation design converts an unfalsifiable "fingerprint" story into a causal, stage-attributed measurement on matched content.

---

# KILLED

---

## A-0003 — Prompt-order sensitivity of multi-click prompting → **KILL**

### Attacks

1. **Triviality by construction (FATAL).** SAM's iterative prompting is a stateful process: each click is applied against the low-res mask prior produced by the previous ones. That output depends on input order is *definitionally guaranteed* by the architecture — the last click always operates on a different state. The paper's only contribution is a magnitude, and magnitude-of-an-obvious-effect papers need shocking magnitudes.
2. **Motivation collapse.** The benchmark-validity story fails on inspection: interactive protocols standardize the click *policy* (simulated user clicks the largest error region), not click *sets* — so "same set, different order" is a counterfactual no benchmark or user ever instantiates. Real users' order is error-driven; permuting a fixed set is off-policy.
3. **Weak causal evidence.** The "mediation test" (ablate the inter-step mask prior) changes the model's operating mode — SAM was trained with the prior — so the ablation confounds mediation with distribution shift.
4. **Missing baseline.** Effect size must be compared against click-*position* sensitivity (TETRIS); if order effects are second-order to position effects (likely), this is a nuisance-parameter paper.

### Defense pass (failed)

The only rescue is re-scoping to *policy-consistent* order variation (multiple realistic error-driven orders from RClicks-style user models → annotation irreproducibility). But that experiment still measures a magnitude of an architecturally guaranteed effect, and its interesting outcome (large spread) is indistinguishable in consequence from position-sensitivity results already published. No experiment converts "obvious by construction, off-policy as measured" into a finding. **KILL.**

---

## A-0016 — Forgetting curve of SAM2's memory bank → **KILL**

### Attacks

1. **The mystery is in the source code (FATAL).** The idea's central dichotomy — exponential interference vs. step-like slot eviction — is not an empirical question. SAM2's memory bank is a documented FIFO of the N most recent frames plus a *permanently retained* conditioning frame. Eviction is deterministic and readable in the code; the "decay law" for recent-frame memory is architecture-determined before any experiment runs.
2. **Redundancy with a stronger survivor.** The genuinely open remainder — why re-ID fails after long occlusion *despite* the permanently retained prompt-frame memory (competition/interference between retained good memory and recent bad entries) — is precisely what A-0017's deletion intervention measures, causally, on organic failures rather than synthetic occlusions.
3. **Dataset bias.** Synthetic parametric occlusions don't capture appearance change during real occlusions (idea's own risk); the fitted "decay law" would describe the synthetic generator.
4. **Significance decay.** SAM2Long/SAMURAI/DAM4SAM already fixed memory scheduling; a descriptive decay curve arriving after the fixes is a post-mortem.

### Defense pass (failed)

The defensible core (memory-competition mechanism, attention-weight analysis between prompt-frame and recent entries) is real but is a strict subset of what A-0017's causal surgery delivers with a cleaner instrument and organic failures. Two survivors on SAM2 memory is one too many under Reviewer #2 quota; the observational one dies. **KILL — merged into A-0017's scope (memory-attention analysis absorbed as a secondary analysis there).**

---

## A-0032 — Exhaustivity misses concentrate far from the concept prototype → **KILL**

### Attacks

1. **Circularity (FATAL).** A miss is a below-threshold model score; scores are functions of the model's embeddings; instances far from the concept prototype *in the model's own embedding space* get low scores by construction. "Misses are far from the prototype" is within epsilon of "low-scoring instances are missed" — definitional, not a discovery. To be non-circular the paper must show prototype distance predicts misses *incrementally beyond the model's own confidence*, or transfers across models — at which point it is an incremental-AUC exercise.
2. **Practical relevance.** The promised payoff (predictable misses → targeted human verification) is already delivered by the scores every pipeline has: lowering the threshold surfaces exactly the borderline instances. No new lever.
3. **Dataset bias.** The study needs exhaustive GT. LVIS is *federated* — explicitly not exhaustive per image; exhaustivity holds only for sampled category-image pairs. SA-Co's negatives help, but the miss-structure analysis inherits whatever exhaustivity gaps the reference has, and misses-of-the-annotators masquerade as model hits/misses.
4. **Known adjacent result.** Long-tail literature already established that atypical (far-from-prototype) instances are recognized worse — for classification and detection. The segmentation instantiation adds task furniture, not insight.

### Defense pass (failed)

The rescue experiment (partial out model confidence; test cross-model transfer of miss maps) is realistic but its best outcome is "embedding distance adds a few AUC points over confidence" — a marginal-increment result serving a payoff (verification targeting) that confidence alone already serves. The strongest attack concedes nothing to any feasible experiment. **KILL.**

---

## A-0068 (M2) — Training-free audit of latent alpha-matte information in logits → **KILL**

### Attacks

1. **Trivial alternative explanation (FATAL).** A probabilistic segmenter's soft output approximates P(pixel labeled foreground). On translucent matter, annotator labeling rates track alpha. Therefore logit-alpha correlation is *ordinary ambiguity calibration* — the expected behavior of any well-trained classifier under ambiguous labels — rebranded as "latent matting information." The two accounts make identical predictions on every proposed measurement; no experiment separates them because they are the same quantity under different names. The framing dies even if every number comes out as hypothesized.
2. **Weak metric.** "Rank correlation after partialling out distance-to-boundary" is statistically treacherous: alpha and logits are both strongly monotone in distance from the object core; residualizing a dominant smooth confounder leaves noise-dominated residuals, and ρ>0.3 on residuals is an arbitrary bar. Also: distance to *which* boundary (predicted or GT)? Each choice biases a different direction.
3. **Second leg is expected.** Boundary-placement variance higher on translucent than opaque regions — predicted by every account (annotators vary there too); confirms ambiguity, not representation structure.
4. **Dataset bias.** Alpha-matte GT (Composition-1k etc.) is largely composited imagery with artificial edge statistics; "free signal" measured there may not exist on real translucency.
5. **Practical irrelevance.** Trained matting heads (MAM) are small and work; nobody will consume raw-logit mattes. If the free signal exists at ρ≈0.3, it is too weak to use; if strong, MAM already harvests it.

### Defense pass (failed)

Attack 1 is a reframing that concedes the data — the fatal category. There is no observable that distinguishes "latent matting capability" from "calibrated ambiguity," so no experiment can shut the reviewer up. **KILL.**

---

## A-0078 — Do distilled students inherit teacher click-fragility maps? → **KILL**

### Attacks

1. **Structural confound (FATAL).** The deployed models the claim is about make the measurement circular twice over: (a) MobileSAM *reuses SAM's mask decoder verbatim* — and click fragility is substantially decoder-mediated (Stable-SAM's own attribution) — so teacher-student fragility correlation is partially guaranteed by shared weights; (b) students train on SA-1B, whose masks are *SAM-generated* — teacher pathologies arrive through the labels regardless of any distillation signal. With public checkpoints, r(teacher, student) is uninterpretable.
2. **Impossible controls.** "Independently trained architecture-matched controls" for a promptable ViT at comparable scale on non-SAM-derived labels do not exist and cannot be trained at matched capability; any purpose-trained control differs in data, scale, and recipe — reintroducing the confound the control was meant to break.
3. **Expected result.** Distillation is *designed* to copy the teacher's function, errors included. "Students inherit teacher behavior" is the mechanism working as specified; the interesting version (selective pathology filtering during distillation) is a different, untested method paper.
4. **Weak metric.** Fragility maps are high-variance measurements; correlation thresholds (r>0.5 vs r<0.2) are arbitrary, and measurement noise attenuates everything toward unresolvable middle ground.

### Defense pass (failed)

A controlled rescue exists — train small students on human-labeled COCO with vs. without an added SAM-distillation term, measuring whether the distillation term *imports* SAM's fragility map — and it genuinely isolates the distillation channel. But its verdict applies to purpose-built toy students, not to MobileSAM/EfficientSAM (which remain confounded by shared decoders and teacher-generated labels), and its headline in the best case is "distillation transfers behavior," which reviewers will read as the definition of distillation. The claim about *deployed* models cannot be rescued by any experiment on trainable ones. **KILL.**

---

## A-0128 (M3) — Trajectory calibration of interactive confidence → **KILL**

### Attacks

1. **Missing trivial baseline (FATAL).** The practical payoff (repairing stopping rules) must beat **mask-delta stopping** — stop when successive masks stop changing — which reads no confidence, needs no calibration, is already common practice, and *directly observes* the plateau that the proposed per-model correction tries to infer from a miscalibrated signal. There is no a priori reason corrected confidence beats delta stopping; the paper's practical leg survives only on a favorable coin flip against a zero-cost baseline.
2. **Expected mechanism.** Predicted-IoU inflation with click count is unsurprising: the IoU head was trained on iterative-sampling trajectories where quality *does* rise with clicks; at user plateaus the head is off-distribution. "Auxiliary head extrapolates its training correlation" is textbook, not a finding.
3. **Motivation thinness.** The claim that deployed stopping rules consume predicted IoU needs citations that mostly don't exist; interactive tools stop on user satisfaction or click budgets.
4. **Simulator realism.** RClicks itself showed simulated clickers misestimate real behavior; trajectory statistics fitted on simulated sessions may not transfer to human sessions — the correction constant could be a simulator artifact (partially acknowledged).

### Defense pass (failed)

The defense would be a head-to-head where corrected confidence beats mask-delta stopping at equal final quality. Nothing in the mechanism suggests it should: mask-delta measures the plateau directly; confidence measures it through a miscalibrated proxy plus a fitted correction. When survival requires winning an unfavorable coin flip against a trivial baseline, Reviewer #2 kills. The residual scientific claim (IoU-head inflation exists) is expected behavior, quantified. **KILL.**

---

## A-0134 (M4) — The absence option: emptiness calibration for geometric prompts → **KILL**

### Attacks

1. **Ontological invalidity (FATAL).** Under SAM's actual contract — class-agnostic, any-granularity promptable segmentation — "the prompt hits nothing" has no ground truth on natural images: every click lands on *some* maskable region at *some* granularity (stuff, texture, part); every box contains *something*. SAM returning a sky segment for a background click is correct behavior, not a false positive. The benchmark's "empty" labels would encode the authors' object ontology, and models would be scored on agreement with that ontology, not on a competence.
2. **Owned turf wherever emptiness IS definable.** In the pipelines where "empty" is well-defined the rejection signal already has an owner: concept prompts → SAM3's trained presence head; detector/grounding-box pipelines → the detector's own confidence, objectness scores, and standard CLIP crop-verification; medical wrong-box → Cluster B survivor B-0350 (ceded in Stage 3). The idea has been squeezed into exactly the region where its target is undefined.
3. **Trivial-baseline exposure.** A "null token fine-tune" trained on synthetic empty prompts (random background boxes) learns box-objectness statistics — reinventing an off-the-shelf objectness/RPN score. The benchmark must show SAM-internal signals beat external objectness baselines; if the baseline wins, the contribution evaporates.
4. **Deployed counter-evidence.** SA-1B itself was built by filtering SAM outputs with predicted-IoU + stability thresholds — the existing signals demonstrably suffice at scale for the headline application (auto-annotation contamination control). "Far from calibrated" ≠ "not usable at a fixed threshold."
5. **Salami trajectory.** This is the idea's second narrowing (Stage 3 amputated concept scope after SAM3). A paper that survives only by retreating to ever-smaller undefended territory is a red flag in itself.

### Defense pass (failed)

The candidate defense — demonstrate high inter-annotator agreement on emptiness labels, proving the concept is measurable — plausibly works for wrong-box families but not for background clicks and texture boxes, which are the families that distinguish this from B-0350/SAM3/detector-confidence turf. What remains defensible (wrong boxes) lands on owned ground with strong cheap baselines. No experiment simultaneously defends the definable scope and the novel scope. **KILL.**

---

## A-0136 — Token-occupancy law for small-object failure → **KILL**

### Attacks

1. **Broken instrument (FATAL).** Within a fixed model at fixed input resolution, token occupancy is *exactly proportional* to pixel area — decoupling requires varying input resolution. But SAM at off-native resolutions is out-of-distribution (trained at 1024², interpolated positional embeddings), so quality collapse under resolution variation tracks resolution-OOD, not occupancy. The instrument that creates the decoupling also creates the confound; normalizing by large-object performance at each resolution only partially repairs it, because resolution-OOD interacts with object scale (small objects suffer interpolation artifacts disproportionately).
2. **Confirmatory delta.** SOHES and Segmenter patch-size ablations already show mask quality tracks patch size more than resolution — the token story is implied by published ablations; this paper sharpens a conclusion the field already acts on.
3. **"Law" overclaim.** Failure will be gradual (2–4-token objects are also poor); "collapse pins to <1 token" is a threshold narrative fitted to a smooth curve, and reviewers will re-describe the same data as "small things are hard, in token units."
4. **Practical relevance.** The actionable consequence — zoom in on small objects — is already universal practice (crop-and-zoom re-prompting, SAHI-style tiling, HQ high-res paths). No decision changes.

### Defense pass (failed)

The partial defenses are real: upscale-blur is a *conservative* instrument (recovery under information-free upsampling strongly implicates tokenization), and large-object normalization bounds the OOD effect. But they narrow, rather than remove, the fatal confound — and the destination is a sharpened version of a conclusion (tokens, not pixels) that patch-ablation literature already implies and practice already exploits. Under quota, a confounded instrument pointed at a confirmatory target loses its slot. **KILL.**

---

## A-0227 — Is SAM's multimask diversity calibrated to ambiguity? → **KILL**

### Attacks

1. **Strawman by design (FATAL).** SAM's three mask outputs are *trained* as whole/part/subpart hypotheses (min-over-heads loss; the design intent is documented in the SAM paper). The paper's headline hypothesis — "diversity is a fixed part-whole template rather than input-adaptive uncertainty" — is the spec sheet, restated as a discovery. The audit's negative result is pre-ordained by the architecture's documentation; the positive result (spread tracks ambiguity despite template training) is close to impossible.
2. **Motivation thinness.** The victim practice — "downstream pipelines use multimask spread as uncertainty" — is a scattering of convenience heuristics, not a load-bearing literature. Invalidating a practice few rely on is low-stakes.
3. **Expensive reference, weak metric.** Human-interpretation entropy requires multi-annotator prompt-conditioned ambiguity annotation (costly, noisy), correlated against IoU-based diversity metrics that miss semantic diversity (idea's own risk). A weak-reference-vs-weak-metric correlation supports no strong conclusion in either direction.
4. **Adjacent occupancy.** A-SAM already replaced SAM's ambiguity handling assuming its inadequacy; Cluster B's B-0361 holds the cross-domain ambiguity-transfer question. The remaining slot for "audit the deployed model's spread" is thin.

### Defense pass (failed)

For an audit to matter, either outcome must carry content. Here the negative is documented design intent and the positive is architecturally foreclosed. No experimental design changes that asymmetry. **KILL.**

---

## A-0314 (M5) — Linear property axes in mask decoders → **KILL**

### Attacks

1. **Squeezed between knob and metric (FATAL).** Split the four target properties: (a) dilate/erode — controlled *today* by shifting the logit binarization threshold; (b) boundary tightness — controlled by logit smoothing/sharpening; (c) granularity — controlled by SAM's own multimask selection; (d) attachment inclusion — the one property without an output-space knob, and also the one without an automatic evaluation metric (attachment GT is subjective; PACO part annotations cover a sliver). Every property with a metric has a trivial training-free baseline the steering method must beat; the property without a baseline lacks the metric to demonstrate anything. The paper has nowhere to stand.
2. **Reframed, still exposed.** Stage 3 already demoted the control interface to a corollary, making "the decoder has linear property axes" the headline. But SAM's decoder is two transformer blocks plus an upsampler; approximately-linear directions in a shallow module's activation space is an expected, modest interpretability note — not a paper-carrying mechanistic discovery.
3. **Pair-construction circularity.** Contrastive activation pairs for "tight vs loose" must be *generated* by some existing knob (threshold shifts, prompt edits, multimask picks) — so extracted directions inherit the generating knob's structure, and "steering reproduces the knob" is the expected outcome, with entangled off-target drift as the failure mode (idea's own risk).
4. **Field fatigue.** Activation-steering transfer papers face elevated novelty bars; ACL/NeurIPS steering lines make "steering, but dense outputs" read as technique tourism without a task win.

### Defense pass (failed)

The best available defense — evaluate on PACO for attachment GT and show steering beats threshold/prompt baselines somewhere — is a narrow, dataset-limited foothold supporting a corollary the paper already demoted. If steering only matches trivial knobs where metrics exist and can't be scored where they don't, no realistic experiment refutes attack 1. **KILL.**

---

# Portfolio check (post-attack)

Survivor spread: prompt-mechanism 1 (A-0002), SAM2 memory 1 (A-0017, absorbing A-0016's attention analysis), boundary 2 (A-0061 architecture law, A-0062 evaluation validity), PEFT/forgetting 1 (A-0107), representation-internals 1 (A-0178), data-centric 1 (A-0271).

Cross-cluster adjacencies (non-overlapping, noted for the supervisor):
- A-0062 (soft multi-annotator boundary re-scoring) is thematically adjacent to B-0112 (annotation-convention shift) and C-0276 (protocol-drift audit) — three distinct validity instruments; no shared claims.
- A-0107 (component-resolved PEFT forgetting) complements C-0068/M4 (optimizer-transient forgetting) — different mechanisms, different model classes.
- A-0271 (auto-label fingerprints) complements B-0230 (synthetic-image advantage decomposition) — labels vs images; no overlap.

Kill discipline note: every kill above names a fatal attack that no realistic experiment refutes (definitional/ontological/reframing attacks, structurally confounded instruments, or trivial baselines with unfavorable priors). Ideas whose strongest attack was answerable by a concrete experiment were kept even where novelty pressure was high (A-0107, A-0002).
