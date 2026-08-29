# Stage 2 Review — Batches A1+B1 (Reviewer: science-question + feasibility bias)

Bias declared: prefer falsifiable hypotheses with a 1-GPU-day killer experiment. Kill engineering-only pipelines and crowded UDA/AL/semi-sup recipes unless they challenge an assumption. Single pass, no web.

Kept: 80/240 (50 from A1, 30 from B1). No new IDs.

## Keep (max 80)

| ID | 1-line reason | Novelty | Feasibility | Protect? |
|---|---|---|---|---|
| A1-002 | Sharp falsifiable patch-grid aliasing claim; FFT test runs in hours | 4 | 5 | - |
| A1-004 | Topology-level failure (genus>0); trivially cheap, decisive test | 4 | 5 | - |
| A1-006 | Free OOD signal from ignored IoU head; calibration sweep is 1 GPU-day | 3 | 5 | - |
| A1-007 | Non-monotonic negative-click behavior is a falsifiable interaction bug | 3 | 5 | - |
| A1-008 | Scale sweet-spot tied to SA-1B statistics; cheap sweep, mechanistic link | 3 | 5 | - |
| A1-016 | Memory averaging tied to controllable rotation phase; clean synthetic design | 4 | 4 | - |
| A1-017 | Failure pinned to explicit architecture constant; sharp cutoff prediction | 4 | 5 | - |
| A1-018 | Frame-0 prompting convention never tested; one sweep falsifies | 3 | 5 | - |
| A1-020 | Collapse tied to displacement not FPS; strong quantitative claim | 3 | 5 | - |
| A1-021 | Validates free per-frame uncertainty output; AUROC test cheap | 3 | 5 | - |
| A1-022 | Memory contamination dynamics; single-frame injection is decisive | 3 | 5 | - |
| A1-024 | One-ratio failure predictor; re-binning existing benchmarks, near-zero cost | 3 | 5 | - |
| A1-025 | Matched-noise design causally separates modality noise from anatomy | 4 | 4 | - |
| A1-027 | Names a representational gap (split/merge) with concrete behavioral prediction | 4 | 4 | P |
| A1-030 | Internal representations as robustness reserve; probe cheap, readout fix implied | 4 | 4 | P |
| A1-032 | 1-D physics search vs fine-tuning reflex; killer cheap baseline | 3 | 5 | - |
| A1-034 | Preprocessing-vs-LoRA falsification; challenges fine-tune-first culture | 3 | 5 | - |
| A1-038 | Anatomical smoothness as label-free quality proxy; simple correlation test | 3 | 5 | - |
| A1-039 | Prompt-slice policy for volumetric SAM2; cheap sweep, obvious payoff | 3 | 5 | - |
| A1-040 | Clinically dangerous bias tied to one controllable variable (edge width) | 4 | 4 | - |
| A1-043 | Reframes medical domain shift as label-convention shift; testable with dual-annotated data | 4 | 3 | P |
| A1-044 | Cost-ordered remedies (stain norm vs LoRA); assumption-challenging, 1 day | 3 | 5 | - |
| A1-046 | Attacks the mask ontology itself for volumetric media | 4 | 3 | P |
| A1-047 | Do foundation features encode density at all? Linear probe settles it | 4 | 4 | - |
| A1-048 | First prompt-variance quantification on amorphous media; grid eval only | 3 | 5 | - |
| A1-051 | Mechanistic alpha-edge vs luminance-edge response; controlled feature probe | 4 | 4 | - |
| A1-054 | Annotation ceiling bounds meaningful smoke progress; cheap meta-result | 4 | 4 | - |
| A1-059 | Boundary/interior error decoupling on glass; redirects fix design | 3 | 5 | - |
| A1-061 | Nuisance-to-signal inversion (highlights as prompts); trivial to test | 3 | 5 | - |
| A1-063 | Physics-violation (parallax feature mismatch) as transparency signal, training-free | 4 | 3 | P |
| A1-066 | Counterintuitive supervision claim with mechanism; small fine-tune decides | 4 | 4 | - |
| A1-068 | Single-variable causal study (fill level); an afternoon of photos | 3 | 5 | - |
| A1-071 | Sharp jitter-budget threshold defines weakest usable detector | 3 | 5 | - |
| A1-073 | Hard resolution floor vs box-fill null; stops wasted fine-tunes | 3 | 5 | - |
| A1-082 | Single-forward-pass domain-gap meter; falsifiable across 8 domains | 4 | 4 | P |
| A1-083 | Boundary-first degradation law across all corruptions; one sweep | 3 | 5 | - |
| A1-084 | Causal polarity hypothesis; two forward passes falsify it | 3 | 5 | - |
| A1-085 | Aerial gap = scale mismatch claim; resize sweep kills or confirms | 3 | 5 | - |
| A1-088 | Cue-conflict methodology ported to promptable segmentation; cheap | 3 | 5 | - |
| A1-094 | Model-intrinsic difficulty score from prompt geometry; cross-model validation feasible | 4 | 4 | P |
| A1-096 | Acquisition-policy head-to-head nobody ran; pure simulation | 3 | 5 | - |
| A1-099 | Worst-case prompt robustness = new threat model; black-box search cheap | 4 | 5 | P |
| A1-101 | Latent granularity control knob; monotonicity claim dies in one sweep | 4 | 5 | - |
| A1-104 | Non-commutativity permutation test; statefulness exposed cheaply | 3 | 5 | - |
| A1-105 | Grounds all interactive evaluation in real user behavior | 4 | 3 | P |
| A1-106 | Task-dependent instability law; falsifiable with a small seed grid | 4 | 4 | - |
| A1-108 | Interface-contract drift statistic; explains PEFT failure mode mechanistically | 4 | 4 | P |
| A1-110 | Debunk: instability as optimization artifact; cheap grid, saves field effort | 3 | 5 | - |
| A1-113 | Early-warning diagnostic with measurable lead time; falsifiable | 4 | 4 | - |
| A1-118 | Prompt-marginalized evaluation attacks a field-wide blind spot | 4 | 5 | P |
| B1-011 | Negative result reframing AL under modern inits; cheap loop | 4 | 5 | - |
| B1-017 | Causal attack on CAM context bias via co-occurrence masking | 4 | 4 | P |
| B1-024 | Noise is boundary-structured, not symmetric: estimate then exploit | 4 | 4 | P |
| B1-025 | Re-benchmarks semi-sup canon under VFM init; assumption test, not recipe | 3 | 5 | - |
| B1-027 | Ingredient ranking identifies the load-bearing component | 3 | 5 | - |
| B1-028 | Controlled contamination curve kills the in-domain-unlabeled assumption | 4 | 4 | - |
| B1-032 | Redundancy claim, one ablation; trims method complexity honestly | 3 | 5 | - |
| B1-033 | Predictive diagnostic: labeled-only ECE forecasts semi-sup gain | 4 | 4 | P |
| B1-036 | Non-iterative alternative to self-training; 10x cheaper if true | 3 | 4 | - |
| B1-038 | Objective-to-boundary probe; cheap comparative science | 3 | 5 | - |
| B1-041 | Pre-hoc dense-readiness scalar; timely given register findings | 4 | 4 | - |
| B1-046 | Granularity-transfer law; falsifiable peak-location claim | 3 | 4 | - |
| B1-047 | Position-shortcut audit could invalidate probe-based literature | 4 | 4 | P |
| B1-051 | Compute-matched honest baseline vs generative-synthesis hype | 3 | 5 | - |
| B1-056 | Counterfactual backgrounds; causal test of context dependence | 4 | 4 | - |
| B1-059 | Hidden calibration cost of synthetic data; piggybacks existing sweep | 4 | 4 | - |
| B1-061 | Decomposes UDA gains into a cheap style component; assumption killer | 4 | 5 | - |
| B1-065 | Adapt-or-don't decision diagnostic; falsifiable correlation | 4 | 4 | P |
| B1-069 | Additivity factorial: are cheap tricks subsumed? 2x2 in a day | 3 | 5 | - |
| B1-074 | Support variance > method variance would reorient the FSS field | 4 | 5 | - |
| B1-079 | Background-shortcut audit of FSS benchmarks | 4 | 4 | P |
| B1-083 | Visual ICL brittleness audit; unmeasured sensitivity axis | 3 | 4 | - |
| B1-094 | Intrinsic-dimension audit of learned prompts; PCA is free | 3 | 5 | - |
| B1-097 | Linear-correctability hypothesis for CLIP dense misalignment; crisp | 4 | 5 | P |
| B1-107 | Counterfactual proof of language-prior hallucination in dense output | 4 | 4 | P |
| B1-109 | Spectral diagnostic predicting fine-tune necessity per backbone | 4 | 4 | - |
| B1-110 | Layer-resolved mismatch map with an actionable freeze rule | 3 | 5 | - |
| B1-111 | Label-free scalar (feature TV) predicting boundary quality rank | 4 | 4 | P |
| B1-112 | Attributes thin-structure deficit to tokenization; decisive decoder swap | 3 | 4 | - |
| B1-116 | Physics-vs-convention conflict; two-normalization test settles it | 3 | 5 | - |

## Kill 15 with reasons

| ID | Reason |
|---|---|
| A1-012 | Engineering deployment artifact; overlap-blending is already standard practice, no scientific claim survives it |
| A1-026 | Compute-quality stride ablation; incremental engineering, no assumption challenged |
| A1-035 | Pipeline recipe (atlas+SAM); registration fails exactly where it matters (pathology); no hypothesis about the model |
| A1-057 | Application pipeline; no falsifiable claim beyond "composition works"; site-specific confounds |
| A1-064 | Sensor-bound engineering fusion; polarization data scarcity blocks the killer experiment |
| A1-078 | Crowded SAM-as-teacher weak-supervision recipe space; gain attribution muddy |
| A1-089 | Template-redundant with A1-032/034/044 (physics-preprocessing-vs-LoRA); weakest feasibility of the family (needs depth) |
| A1-092 | Rides the crowded model-merging bandwagon; interference results are seed-noisy, recipe not question |
| A1-100 | Engineering-only learned prompter; auto-prompting well trodden, likely overfits source conventions |
| B1-002 | Crowded cost-aware AL; proxy-vs-real-time gap undermines the only novel part |
| B1-008 | Region-level AL is a well-mined literature; no assumption challenged |
| B1-013 | CAM+SAM seed refinement is an already-crowded WSSS recipe space |
| B1-026 | Adaptive class thresholds are established (FlexMatch lineage); recipe transplant, not a question |
| B1-067 | Stochastic weight restoration already exists in continual-TTA (CoTTA); incremental |
| B1-120 | Report-mined CXR supervision is a very crowded area; report noise dominates and idea offers no new lever |

## 10 high-disagreement / protect

| ID | Why I protect it despite expected kill votes |
|---|---|
| A1-046 | GT-scarcity will draw kills, but it challenges the binary-mask ontology itself — a real assumption, not a recipe |
| A1-063 | Two-view requirement narrows scope, but physics-violation-as-detection-signal is genuinely new science |
| A1-043 | Dual-annotated data is scarce, but reframing medical domain shift as label-convention shift could redirect the subfield |
| A1-105 | Needs a (small) user study, but it grounds the entire interactive-segmentation evaluation literature in reality |
| A1-118 | Will be dismissed as "just evaluation"; it attacks a blind spot every SAM-variant paper shares |
| A1-099 | May look gimmicky; it defines worst-case prompt robustness, a missing threat model with a cheap search |
| B1-047 | Audit may seem niche; if positional leakage is real, many dense-probe results are inflated |
| B1-079 | Compositing-artifact risk is real, but a confirmed background shortcut breaks FSS benchmarks as evidence |
| B1-107 | Inpainting traces are a confound, but it is the only causal test of language-prior hallucination in dense prediction here |
| B1-033 | Correlational and possibly spurious — but a validated predictive diagnostic for semi-sup gain is rarer and more useful than another method |
