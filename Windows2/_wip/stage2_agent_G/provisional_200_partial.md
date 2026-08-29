# Provisional B ∪ C Portfolio (Agent G) — partial 200, batch A slots reserved

Agent G (merger + feasibility auditor; **not PI, no final-3, batch A not seen**). Date: 2026-08-28.
Built from Agent D's 107 batch-C keeps + Agent E's 77 batch-B keeps (= 184 units), after the collision merges in `collisions.md` and the artifact verdicts in `feasibility_census.md`.

## Headline accounting

| Category | B | C | Total |
|---|---|---|---|
| **LOCK** (would keep even after batch A) | 18 | 32 | **50** |
| **FLEX** (competes with batch A survivors) | 46 | 25 | **71** |
| Portfolio slots (LOCK + FLEX) | 64 | 57 | **121** |
| MERGED (parasites — named arms of hosts, no slot) | 5 | 18 | 23 |
| **DROP** (from the 184) | 8 | 32 | **40** |
| Check: 121 + 23 + 40 | 77 | 107 | 184 ✓ |

Policy compliance:
- **Target ~110–140 from B∪C:** 121 slots → leaves **79 slots** for batch A in the future 200.
- **C eval-audit cap ~60% (D's policy):** of C's 57 slots, 33 are eval-audit/re-analysis/reproducibility class and 24 are mechanism/causal-probe/constructive-artifact class → **57.9% eval-audit ≤ cap**. (Before capping, D's keep-set ran ~70% eval-audit; the cap was met mainly by merging redundant audits into hosts rather than by killing protected ideas.)
- **E's cheap mechanism bets protected:** B-0114, B-0001, B-0074, B-0104 all LOCK (plus B-0304, B-0323, B-0164, B-0169, B-0194, B-0227, B-0263).
- Every MERGE and DROP is reversible; parasites are named at their hosts.

Tags: [E]=eval-audit/re-analysis class (counts against C cap), [M]=mechanism/causal probe, [A]=constructive artifact/method, (P)=carries a D/E protection tag, (¢)=cheap (inference-only or ≤ days), ($)=compute- or annotation-heavy, (⏰)=urgency flag from D/E.

---

## LOCK — 50 ideas (would keep even after batch A)

### C-batch LOCK (32)

| ID (hosts ←parasites) | Class | Why locked |
|---|---|---|
| C-0302 ←0070,0065,0284 | [E](¢) | Rigor-infrastructure flagship: MDE/power tables + claims re-analysis + seed-count standard. D bet #1; census CONFIRM. |
| C-0309 ←0328 | [A](¢) | IRT for detection benchmarks + 1k short test + misfit↔annotation-error audit. D bet #2; census CONFIRM (30+ zoo models). |
| C-0136 ←B-0033 | [E] | Seed variance vs published-delta census — the field's missing constant; hosts the pretraining-stage arm (compute-partner-conditional). D bet #3, survived attack clean. |
| C-0311 ←0064,0042,0282 | [A](¢) | Metrology-grade uncertainty budget for COCO AP, now hosting its own components (bootstrap axis, noise-derived IoU threshold, framework variance). D bet #4. |
| C-0344 | [E](P)(¢) | Instruction-A/B labeling-protocol experiment; census confirms the artifact is unclaimed (no released multi-annotator box data). D bet #5. |
| C-0338 ←0071 | [E](P)(¢) | Human small-object ceiling; hosts the SOTA-vs-ceiling arm. Census UPGRADE (LVIS double annotations public) + mandatory Label Convergence positioning. D bet #6. |
| C-0260 | [E] | Benchmark monoculture cross-dataset rank study — the reusable audit artifact of batch C. D bet #7. |
| C-0276 ←0255 | [E](P)(¢) | Tail-progress illusion + head-class utility arm. Census PARTIAL on third-party checkpoints; survives as family host with retrain fallback. D bet #8. |
| C-0256 ←0261 | [E](P)(¢) | Size-frequency confound + tail-definition arm; same host logic. D bet #9. |
| C-0306 | [M](P)(⏰) | Conformal coverage destroyed by NMS + coverage-preserving suppression — genuine formal novelty, field moving fast. D bet #10. |
| C-0057 | [E](¢) | Missing-annotation tax law (differential, anti-quality). Census UPGRADE via COCO-ReM. D bet #11. |
| C-0011 ←B-0042 | [E](¢)(⏰) | Vocabulary-noise vs leaderboard margins: OVD templates + OVS synonyms in one paper. D bet #12 + E top-20 #20 merged. |
| C-0326 | [E](¢) | Powered adjudication of residual COCO errors (share that is GT problems). Census UPGRADE (ReM error inventory). D bet #13. |
| C-0327 | [E]($) | 2015 architecture + 2026 recipe: attribute a decade of progress. D bet #14. |
| C-0283 | [E]($) | Stale-baselines decay audit under papers' own budgets. D bet #15. |
| C-0285 | [E]($) | Shadow tuning: give the baseline the method's search budget; pre-registered. D bet #16. |
| C-0226 ←0248,0231 | [E](¢) | GT-controlled SR truthfulness: recovered info vs hallucination, asymmetry, object-destruction arms. D bet #17. |
| C-0150 ←0221 | [E](¢) | UDA reckoning: 50 labeled images + foundation-backbone gap-closure, one paper two instruments. D bet #18. |
| C-0287 | [E](P)($) | Ablation sign-flip rates under reseeding; bounded compute, wholesale consequence. D bet #19. |
| C-0259 | [E]($) | Dense "label everything nameable" re-annotation: salience bias / FP population. D bet #20. |
| C-0046 ←0080 | [E](¢) | Annotation-noise band CIs (+tightness-drift arm). Census UPGRADE — double-annotation input now free. |
| C-0007 | [E](¢) | Tiny-object annotation-noise floor; shares infrastructure with 0338/0344; census confirms unclaimed. |
| C-0279 ←0001,0020 | [E](¢)(⏰) | Exposure-vs-rarity program (re-stratification + frequency regression + invented-names causal arm); mandatory Udandarao positioning. |
| C-0159 | [E] | Detection AL replication at realistic batch sizes — survived attack with High confidence; expensive-labeling stakes. |
| C-0122 ←0264 | [E](¢) | Train-test duplication census + tail-duplicate stratification arm. Certain-yield. |
| C-0298 | [E](P)(¢) | Hash-audit of circulating benchmark variants; cheap forensic long-shot, scandal tail. |
| C-0158 | [M](¢) | NMS as calibration destroyer (winner's-curse mechanism); prior work only calibrates post-NMS. |
| C-0308 | [M](P)(¢) | Machine psychophysics staircases for detectors; top-decile originality, inference-scale. |
| C-0135 | [M](P)(¢) | Co-occurrence overrides appearance — protected causal probe; absorbs 0222/0268-C context ideas. |
| C-0341 | [M](P)(¢) | Batch cross-talk exploit — original attack surface, cheap to demonstrate/refute. |
| C-0055 | [A](P)($) | Fresh i.i.d. COCO test set — the single most informative missing artifact; HRHR protected. |
| C-0043 | [E](¢) | Size-stratified Dice reliability on multi-annotator medical data; batch C's only MICCAI-facing anchor (census PARTIAL on LIDC/QUBIQ re-verification, known-public). |

### B-batch LOCK (18)

| ID | Class | Why locked |
|---|---|---|
| B-0114 | [M](P)(¢) | VPT tokens as trainable registers; frozen-random-token control is an afternoon and every outcome publishes. E bet #1; census CONFIRM (DINOv2 ±reg pairs + official VPT code). **Mission-protected.** |
| B-0001 | [M](P)(¢) | Register-norm maps as free per-pixel uncertainty; survived attack on the hottest artifact literature. E bet #2. **Mission-protected.** |
| B-0304 | [M] | Language quantizes shape space (morph discontinuities); psychophysics-grade, multi-pipeline controls. E bet #3. |
| B-0074 | [M](¢) | Modality-gap collapse dynamics predict zero-shot loss; statics crowded, dynamics empty. E bet #4. **Mission-protected.** |
| B-0323 | [M] | Mention-bias imprint on decodability, SSL-normalized + caption-intervention causal arm. E bet #5. |
| B-0104 | [M] | Invariance-inheritance ceiling of PEFT; mechanism + failure predictor. E bet #6. **Mission-protected.** |
| B-0307 | [M]($) | Causal matched-data test of language-alignment cost to 3D; compute-partner-conditional but highest scientific ceiling of the geometry family. E bet #7. |
| B-0332 | [M](⏰) | Artifact-swap causal test of visual CoT faithfulness; fastest-decaying novelty — execute early, re-search first. E bet #8. |
| B-0268 | [E](⏰) | Generated-image contamination of benchmarks + ranking distortion; clean-baseline window closing. E bet #9. |
| B-0213 ←0200 | [E](P) | Resolution × probe-capacity protocol-confound audit; which published VFM conclusions invert. E bet #10. |
| B-0226 | [M] | Shift-budget curves frozen-vs-tuned for dense prediction; functional form + crossover stability. E bet #11. |
| B-0101 | [M] | Task-indexed required-rank law (accuracy vs captured spectral mass). E bet #12. |
| B-0194 | [M](P)(¢) | Segmentation sycophancy: confidence rises with prompts, accuracy doesn't. E bet #14. |
| B-0169 | [M](P)(¢) | Negative-click dose-response; clean response surface, felt daily, never measured. E bet #15. |
| B-0164 | [M](P)(¢) | Savings/relearning paradigm for VFM forgetting; measures what retention probes miss, near-free. E bet #16. |
| B-0227 | [M](P)(¢) | Cleaner labels transfer worse — contrarian noise-ladder test, decisive either way. E bet #17. |
| B-0263 | [M](P)(¢) | Procedural corruptions beat realistic generated ones; structure-preservation mechanism. E bet #18. |
| B-0286 | [M](¢) | Site-of-origin decodability: natural VFMs more site-invariant than medical FMs. E bet #19. |

---

## FLEX — 71 ideas (compete with batch A survivors)

### C-batch FLEX (25)

Tier-A survivors (17): C-0193 [M](¢) threshold drift under mild shift · C-0078 [E]($) AP vs downstream utility · C-0115 [E]($) quality-vs-quantity exchange rate · C-0119 [M](¢) transform rank-stability predicts AP · C-0145 [E](¢) vocabulary interference · C-0178 [E]($) synthetic vs real corruption (protected capture budget) · C-0190 [M](¢) flicker as free uncertainty (census: regenerate predictions) · C-0208 [E] label conventions are a domain (hosts 0014/0134) · C-0212 [M] night is an ISP artifact · C-0258 [A]($) fairness benchmark with proper uncertainty (kept over dropped 0252 — one annotation-heavy fairness artifact, not two) · C-0269 [E](¢) CLIP-filtered curation bias · C-0277 [M](P)($) end-to-end bias tracing (HRHR) · C-0300 [E] reproduction-gap meta-analysis (hosts 0304-C) · C-0303 [M](P)(¢) tuning-tax on generalization (inference-only, disagreement-prone) · C-0319 [M](P)($) weak-to-strong in dense prediction (HRHR) · C-0321 [A] behavioral contracts for detector updates · C-0345 [E](⏰) foundation-model test-set exposure.

Tier-B survivors (8): C-0013 [M](P)(¢) small objects detected from context · C-0116 [M](¢) ghost-rate benchmark (strict inpainting controls) · C-0125 [M](¢) stride-grid box snapping · C-0290 ←0296 [E](¢) determinism / silent-variables audit (hosts 0288/0289/0296) · C-0329 [M](P)(¢) vestigial RPN · C-0332 [M](P)(¢) cropping test (global context) · C-0333 [M](¢) silhouettes almost suffice · C-0340 [M](P)(¢) resolution is object pixel count.

### B-batch FLEX (46)

vfm_failure (5): B-0013 [M](P)(¢) sub-patch inverse scaling · B-0018 [M](P)(¢) thin-structure Nyquist law · B-0023 [M] LVLM acuity battery (correlated with C-0308, keep both) · B-0025 [M](P) attention maps epiphenomenal? (DP) · B-0026 [M] nameability predicts dense errors.

vlm_dense_failure (5): B-0036 [E] relation flip-consistency · B-0054 [M](P)(¢) multiplicative multi-hop error law · B-0062 [M](P)(¢) size adjectives read as pixels · B-0064 [M](¢) part-whole containment violations (PACO) · B-0068 [M](P)(¢) shadows/holes/reflections grounding failure.

finetune_instability (3): B-0077 [M](P)(¢) inverted layer-wise LR decay · B-0092 [M](P)($) inverse stability scaling (CI, 3-point ladder) · B-0098 ←0095 [M] LoRA≈rescaled-LR boundary question (hosts displacement-budget control).

peft_limits (3): B-0108 [M] PEFT/full-FT calibration sign flip under shift · B-0118 [E] PEFT hides subgroup gaps · B-0133 [M](P)(¢) LoRA memorizes more per-parameter (CI; mandatory pre-execution lit re-check).

catastrophic_forgetting (4): B-0137 [M](¢) beneficial forgetting · B-0154 [M] head-capacity → backbone-forgetting curve (non-monotone version) · B-0157 [E](¢) template staleness inflates forgetting estimates · B-0163 [E] forgetting-audit bias (ID vs OOD probes, dose-response).

prompt_sensitivity (2): B-0168 [M](P)(¢) template gains are mostly calibration · B-0182 [M](P) scale increases prompt sensitivity on rare classes.

representation_mismatch (5): B-0196 [E] equivariance-deficit transfer predictor · B-0203 [E] post-upsampler residual decomposition (FeatUp-aware) · B-0208 [M](P)(¢) occupancy-threshold recall law · B-0215 [M] text-aligned subspace vs complement · B-0222 [M] video pretraining repairs equivariance (timely).

crossdomain_frozen_vs_tuned (4): B-0234 ←0112 [M]($) frozen-vs-tuned 2D phase boundary (hosts LoRA-crossover arm) · B-0241 [M] style-vs-content double dissociation · B-0243 [M](¢) nameability boundary for text-steered adaptation · B-0252 [M](P) interpolation-frontier kinks (HRHR).

synthetic_adaptation (4): B-0254 [E] generated-data calibration tax (AUGCAL-aware, diffusion-era scope) · B-0264 [M](P)($) synthetic medical privacy laundering (HRHR) · B-0275 [E](¢) boundary-F1 as collapse canary · B-0278 [M](P) spectral-coverage criterion (HRHR).

medical_vfm_science (4): B-0282 [M](P)(¢) orientation invariance destroys laterality · B-0284 [M](P)(¢) lesion-size/stride law + feasibility calculator · B-0293 [E]($$) matched-budget medical-pretraining attribution (**compute-partner-conditional**, else fold residual into B-0286) · B-0303 [M] fine-tuning degrades ROC tails at matched AUC.

language_geometry (4): B-0305 [M](P)($) Whorfian spatial imprint (HRHR) · B-0317 [M](P)($) MIL identifiability theory (HRHR; needs theory collaborator) · B-0325 [M](¢) text-only counterfactual decomposition of spatial errors · B-0326 [M] basic-level naming sets segmentation granularity.

agentic (3): B-0329 [E] agent confidence vs tool-output quality · B-0338 [E](⏰) web-agent benchmark contamination via retrieval blinding · B-0342 [M](¢) question-substitution drift.

---

## MERGED — 23 parasites (named arms; no slots; reversible)

C-side (18): 0001→0279 · 0020→0279 · 0042→0311 · 0064→0311 · 0065→0302 · 0070→0302 · 0071→0338 · 0080→0046 · 0221→0150 · 0231→0226 · 0248→0226 · 0255→0276 · 0261→0256 · 0264→0122 · 0282→0311 · 0284→0302 · 0296→0290 · 0328→0309.
B-side (5): 0033→C-0136 · 0042→C-0011 · 0095→0098 · 0112→0234 · 0200→0213.

## DROP — 40 (from 184; all reversible, reasons recorded)

### C drops (32)

From Tier A (14):
- **C-0040** — few-shot episodic variance: narrow, shrinking subfield; the variance-vs-deltas move is better carried by 0136/0302.
- **C-0149** — compute-matched UQ audit: crowded UQ space + training cost; calibration ground covered by 0158 (mechanism) and 0302 (significance).
- **C-0188** — multi-view consistency: same "free signal" family as 0190/0119; weakest third instrument, licensed-data friction.
- **C-0206** — feature-distance metrics don't predict AP drop: AutoEval/accuracy-on-the-line adjacency crowds it; 0119 keeps the constructive half.
- **C-0236** — SR as test-time compute: satellite of 0226; allocation question with low ceiling once 0226 hosts the accounting.
- **C-0252** — geo-stratified test set: one annotation-heavy fairness artifact is enough; 0258 kept (adds the uncertainty angle that ties to the rigor family).
- **C-0253** — granularity knob: **census downgrade** (needs many third-party per-class predictions; PARTIAL checkpoints); weaker sibling of 0256's confound cut.
- **C-0254** — long-tail methods vs real deployment tails: **census MISSING** (no public deployment-tail artifact).
- **C-0271** — instance-weighted averaging audit: **census downgrade** (same cache dependence); convention audit partially absorbed by 0311's budget.
- **C-0291** — reporting census with teeth: ground covered by 0300 + 0302; three meta-census slots would be reviewer-fatigue bait.
- **C-0292** — ten tricks under matched compute: training-audit family already 4 deep (0283/0285/0287/0327); most compute-expensive of the five and least sharp.
- **C-0299** — do improvements stack: same family, highest compute, interference matrix partially recoverable inside 0285/0292-style designs later.
- **C-0305** — random-config null for components: nearest to NAS random-search literature (D flagged mandatory positioning); weakest survivor of the rigor family.
- **C-0330** — augmentation is just data: third of the training-science trio; 0327 carries the flagship claim, budget-correlated family trimmed.

From Tier B (18): C-0148 (video vs frame+tracker: shrinking area), C-0154 (self-training threshold leakage: folds conceptually into 0285's tuning-fairness program if revived), C-0201 (syn2real decomposition: 0208+0212 cover the sharpest axes), C-0228 (diffusion label noise: B-0254/B-0275 carry the generated-data harms cluster), C-0241 (restoration ranking disagreement: 0226 hosts restoration truthfulness), C-0243 (img2img box drift: same cluster, weaker), C-0245 (video SR: niche), C-0251 (framing bias: protected but weakest counter-intuitive probe; 0135/0013 keep the class), C-0266 (taxonomy misalignment: absorbed in spirit by 0208), C-0267 (benchmark aging: 0345/0122 carry temporal-validity), C-0272 (difficulty-distribution mismatch: 0260 covers ranking-generality), C-0273 (generator stereotypes: B-0254 hosts generated-data bias), C-0294 (checkpoint-selection inflation: absorbed in spirit by 0302's claims audit), C-0310 (design-based sampling: 0258+0055 carry the sampling-artifact load), C-0312 (optimal ablation design: nice-to-have methodology, low urgency), C-0334 (NMS-free wins are tuning artifacts: adversarial re-tuning covered by 0285's design; NMS ground held by 0158/0306), C-0335 (label assignment at scale: perishable null), C-0339 (only rank matters: 0158 explains the mechanism more sharply).

### B drops (8)
- **B-0005** — attention-entropy resolution collapse: mid-strength causal story; 0013/0018 carry the resolution family.
- **B-0043** — attribute-object prototype snapping: weakest of the dense-compositionality keeps; 0062/0064 sharper.
- **B-0078** — first-100-steps prognosis: 50-run cost for a correlational signal; 0074 is the stronger dynamics bet.
- **B-0087** — post-spike calibration scars: fragile natural-experiment design; instability family kept via 0077/0092/0098.
- **B-0105** — prompt-tuning off-manifold: mechanism arm (0128) was already killed; 0104/0101 carry PEFT limits.
- **B-0145** — calibration forgets first (dense port): E's own attack demoted it (LLM/CL ordering published); domain-swap residual too thin against the cap.
- **B-0172** — auxiliary-text response curves: mutated into a reconciliation study of ITACLIP's contradiction; weakest surviving prompt idea.
- **B-0339** — agentic-vs-scale crossover predictor: hottest contested space, novelty decaying fastest (E: "dead in a year without pre-registration"); portfolio keeps 0329/0332/0338/0342 in agentic.

---

## Notes for the PI

1. **Where batch A should land:** the 79 reserved slots naturally fill from A's SAM/medical/ambiguous-segmentation territory, which this portfolio deliberately under-covers (medical: 6 slots; SAM-prompt mechanics: 3). Expect A to collide mainly with FLEX clusters listed in `AGENT_REPORT.md` §2.
2. **Execution-order urgencies (independent of A):** B-0332, B-0268, C-0306, C-0011(+B-0042), C-0345 all sit on fast-moving fronts; D/E both said re-attack immediately before proposal writing.
3. **Bundle sizes:** several LOCK hosts are now multi-arm papers (0302, 0311, 0226, 0279, 0338). If the PI prefers thinner papers, the parasites are the natural fission points — slot accounting is unaffected either way.
