# Stage 1 — Batch C: Original Research Ideas (IDEA-C-0001 … IDEA-C-0340)

PI: Windows5 · Autonomous Research Idea Evolution, Stage 1, Batch C.
Scope: distinct from SAM-centric and dataset-centric batches. No "A+B modules", no "use transformer", no "new attention", no "apply SAM to X" without a new hypothesis. Every idea states a falsifiable core hypothesis and a minimal experiment. No results are claimed; no papers are cited by invented findings.

Clusters:
- C1 PEFT failure & when full fine-tuning is necessary (0001–0030)
- C2 Catastrophic forgetting in sequential medical/domain adaptation (0031–0060)
- C3 VLMs for dense prediction: alignment vs localization mismatch (0061–0090)
- C4 Prompt learning pathologies (0091–0118)
- C5 Weak/semi/self-supervised segmentation: scientific gaps (0119–0148)
- C6 Medical vision foundation models: what they still cannot do (0149–0178)
- C7 Object detection vs segmentation representation conflict (0179–0204)
- C8 Boundary quality as a scientific problem (0205–0232)
- C9 Ambiguous labels / inter-rater disagreement as signal (0233–0260)
- C10 Foundation-model tokenization / resolution / memory artifacts (0261–0288)
- C11 Community beliefs that may be false (0289–0314)
- C12 Cheap experiments to overturn implicit assumptions (0315–0340)

---

## C1. PEFT failure and when full fine-tuning is actually necessary (IDEA-C-0001 … 0030)

### IDEA-C-0001
- **One-sentence idea:** Predict PEFT failure from the spectral structure of the weight update that full fine-tuning would make.
- **Problem:** LoRA-style methods sometimes match full fine-tuning (FT) and sometimes fail badly, with no accepted pre-hoc predictor of which regime a task falls into.
- **Core Hypothesis (falsifiable):** PEFT underperforms full FT precisely when the singular-value spectrum of (W_FT − W_pre) is heavy-tailed (effective rank above the adapter rank); tasks with rapidly decaying spectra show no gap.
- **Why Important:** Would turn "try LoRA and hope" into a measurable decision rule, saving compute and preventing silent under-adaptation in clinical deployments.
- **Why Possibly Novel:** Intrinsic-dimension arguments exist for *why LoRA works*; a systematic, task-level *failure predictor* validated across dense and classification tasks is missing.
- **Minimal Experiment:** Fully fine-tune a ViT-B on ~10 diverse tasks (natural + medical, dense + classification), compute per-layer update spectra, correlate spectral decay rate with the LoRA-vs-FT gap at matched budgets.
- **Main Risk:** The update spectrum may itself depend on optimizer/regularization choices, making the predictor unstable across training recipes.

### IDEA-C-0002
- **One-sentence idea:** Test whether PEFT fails when the domain shift lives in low-level image statistics rather than semantics.
- **Problem:** PEFT methods concentrate capacity in mid/late transformer blocks, but modality shifts (e.g., RGB→ultrasound) are dominated by early-layer, frequency-domain changes.
- **Core Hypothesis (falsifiable):** The PEFT-vs-full-FT gap correlates with the fraction of domain shift energy in low-level statistics (measurable via frequency-band discriminability between source and target); adding a fully trainable input stem eliminates the gap for such tasks.
- **Why Important:** Explains a large class of medical PEFT failures with a measurable cause and a two-line fix.
- **Why Possibly Novel:** "Where the shift lives" is rarely quantified; PEFT papers treat tasks as interchangeable points on benchmark tables.
- **Minimal Experiment:** Construct shift ladders (color jitter → speckle noise → modality change), run LoRA vs LoRA+trainable-stem vs full FT, regress the gap against a frequency-shift index.
- **Main Risk:** Low-level and semantic shift are correlated in real data, confounding the regression.

### IDEA-C-0003
- **One-sentence idea:** Locate PEFT's blind spot by adapting attention-only vs MLP-only and mapping which task families need which.
- **Problem:** LoRA is conventionally applied to attention projections, but there is no causal account of which sublayers must change for which transfer types.
- **Core Hypothesis (falsifiable):** Domain shifts that preserve object identity but change appearance require MLP adaptation; shifts that change label granularity require attention adaptation; applying LoRA to the wrong family produces most observed PEFT failures.
- **Why Important:** Sublayer placement is a free hyperparameter choice; a validated placement rule would improve every PEFT deployment at zero cost.
- **Why Possibly Novel:** Placement ablations exist but are reported as leaderboard rows, not as a tested causal taxonomy tied to shift type.
- **Minimal Experiment:** Build a 2×2 of shift types (appearance vs granularity) × adapter placement (attention vs MLP) on controlled datasets; test the predicted interaction effect.
- **Main Risk:** The taxonomy may be model-scale dependent and not transfer from ViT-B to larger backbones.

### IDEA-C-0004
- **One-sentence idea:** Use the linear-probe-to-full-FT gap as a cheap pre-hoc predictor of the PEFT plateau.
- **Problem:** Practitioners cannot tell in advance whether frozen features suffice, PEFT suffices, or full FT is needed.
- **Core Hypothesis (falsifiable):** PEFT final accuracy is a predictable affine function of linear-probe accuracy and full-FT accuracy (PEFT ≈ α·probe + (1−α)·FT with task-independent α per PEFT method); tasks violating this reveal a distinct "feature-absent" regime.
- **Why Important:** A two-hour linear probe would forecast whether a multi-day full FT is necessary.
- **Why Possibly Novel:** Probe accuracy is used as a representation metric, not as a quantitative interpolant for PEFT outcome prediction.
- **Minimal Experiment:** On 15 tasks, fit the affine model on half, predict PEFT accuracy on the other half; report prediction error vs a naive baseline.
- **Main Risk:** α may vary with adapter rank and data size, requiring a fuller (but still cheap) predictor.

### IDEA-C-0005
- **One-sentence idea:** Show that PEFT systematically fails under label-space granularity shift (coarse pretraining classes → fine-grained target subclasses).
- **Problem:** PEFT evaluations use label spaces roughly matched in granularity to pretraining; fine-grained medical subtyping may need feature axes that adapters cannot create.
- **Core Hypothesis (falsifiable):** At matched data, the PEFT-vs-FT gap grows monotonically with target granularity (measured as sibling-class similarity in the pretrained feature space); beyond a similarity threshold, no adapter rank closes the gap.
- **Why Important:** Fine-grained distinctions (tumor subtypes, fibrosis grades) are exactly where medical AI must work.
- **Why Possibly Novel:** Granularity is not treated as an axis in PEFT literature; failure is misattributed to data scarcity.
- **Minimal Experiment:** Take hierarchical datasets (e.g., fine-grained natural categories, tumor grading), evaluate LoRA at ranks 4–256 vs full FT across hierarchy levels, plot gap vs pretrained sibling similarity.
- **Main Risk:** Fine-grained tasks confound granularity with fewer samples per class; needs sample-matched subsets.

### IDEA-C-0006
- **One-sentence idea:** Use bias-only tuning as a diagnostic instrument: if BitFit ≈ LoRA on a task, the task is "feature reweighting", not "re-representation".
- **Problem:** There is no operational way to classify transfer tasks by the kind of change they demand from a network.
- **Core Hypothesis (falsifiable):** Tasks split into two empirical clusters — those where bias-only ≈ LoRA ≈ full FT (reweighting tasks) and those where each step adds large gains (re-representation tasks) — and cluster membership predicts OOD robustness of the adapted model.
- **Why Important:** Provides a cheap task-typing tool that predicts how much adaptation machinery a deployment needs.
- **Why Possibly Novel:** BitFit is treated as a weak baseline, not as a measurement device with interpretive value.
- **Minimal Experiment:** Run BitFit/LoRA/full-FT across ~20 tasks, cluster the gap profiles, test whether cluster identity predicts robustness under a held-out shift.
- **Main Risk:** The dichotomy may be a continuum, weakening the diagnostic story (though the continuum itself would be a finding).

### IDEA-C-0007
- **One-sentence idea:** Test whether PEFT structurally underfits the tail of long-tailed class distributions relative to full FT.
- **Problem:** Adapter capacity is shared across classes; rare classes may lose the competition for low-rank directions.
- **Core Hypothesis (falsifiable):** At equal head accuracy, PEFT models show systematically lower tail-class recall than full FT, and the deficit grows as adapter rank shrinks; the effect disappears when adapters are given class-frequency-balanced gradients.
- **Why Important:** Rare findings are the clinically critical ones; a hidden tail penalty from PEFT would be a deployment hazard.
- **Why Possibly Novel:** PEFT papers report mean accuracy; the interaction between adapter rank and class frequency is essentially unexamined.
- **Minimal Experiment:** Long-tailed classification/segmentation datasets; sweep LoRA rank; plot per-class recall vs class frequency for PEFT vs FT at matched mean accuracy.
- **Main Risk:** Tail effects are noisy; needs multiple seeds and careful confidence intervals.

### IDEA-C-0008
- **One-sentence idea:** Establish that tuning only normalization parameters recovers most cross-scanner medical shift, defining a "cheap-shift" equivalence class.
- **Problem:** Cross-scanner/protocol shifts may be largely affine feature perturbations, but the community deploys heavyweight adaptation regardless.
- **Core Hypothesis (falsifiable):** For intensity/protocol shifts (same anatomy, same task), norm-only tuning achieves ≥90% of the full-FT gain; for population shifts it achieves <50%, providing a two-sided test of shift type.
- **Why Important:** Norm-only adaptation is orders of magnitude cheaper and safer to certify than full FT in clinical settings.
- **Why Possibly Novel:** Norm-tuning results exist scattered; the claim that gain-fraction *classifies the shift* is a new, testable framing.
- **Minimal Experiment:** Multi-site MRI/CT segmentation with known shift provenance; compare norm-only vs LoRA vs full FT; verify the predicted gain-fraction split.
- **Main Risk:** Real site shifts mix intensity and population components, blurring the classification boundary.

### IDEA-C-0009
- **One-sentence idea:** Estimate the minimal sufficient LoRA rank from a few steps of full fine-tuning via the effective rank of early gradients.
- **Problem:** Rank selection is by grid search; under-ranked adapters silently underfit.
- **Core Hypothesis (falsifiable):** The effective rank of the accumulated full-FT gradient over the first ~100 steps predicts (within a factor of 2) the smallest LoRA rank that reaches 95% of full-FT accuracy.
- **Why Important:** Converts rank selection from expensive sweeps to a one-shot measurement.
- **Why Possibly Novel:** Gradient-spectrum analyses exist for optimization theory, but not as a practical rank-selection instrument validated across tasks.
- **Minimal Experiment:** On 12 tasks, compute early-gradient effective rank, then run rank sweeps to find the true minimal rank; report predictive accuracy.
- **Main Risk:** Early gradients may reflect head warmup rather than backbone change, requiring a head-frozen measurement window.

### IDEA-C-0010
- **One-sentence idea:** Quantify a calibration penalty of PEFT: adapters match accuracy but produce worse-calibrated uncertainty than full FT.
- **Problem:** Adaptation quality is judged by accuracy; clinical use depends on calibration, which PEFT may distort differently than FT.
- **Core Hypothesis (falsifiable):** At matched accuracy, LoRA-adapted models have higher ECE and worse selective-prediction curves than full-FT models on the target domain, because low-rank updates warp the logit geometry anisotropically.
- **Why Important:** If true, PEFT models need mandatory recalibration before deployment — a concrete, checkable guideline.
- **Why Possibly Novel:** PEFT-vs-FT comparisons on uncertainty quality are almost absent; the logit-geometry mechanism is a new falsifiable claim.
- **Minimal Experiment:** Match LoRA and full-FT accuracy on 8 tasks (early-stop the better one), compare ECE/NLL/selective risk; test whether temperature scaling closes the gap (mechanism check).
- **Main Risk:** Accuracy matching by early stopping introduces its own calibration confound; needs multiple matching protocols.

### IDEA-C-0011
- **One-sentence idea:** Adjudicate whether PEFT failures are capacity failures or optimization failures by giving PEFT unbounded compute.
- **Problem:** When LoRA lags full FT, papers conclude "insufficient capacity", but LoRA also changes optimization geometry.
- **Core Hypothesis (falsifiable):** For a substantial fraction of "PEFT-hard" tasks, LoRA at fixed rank closes the gap given 5–10× training length with tuned schedules — implying optimization, not capacity, is the binding constraint.
- **Why Important:** The remedy differs completely (better schedules vs higher rank/full FT); current practice may waste capacity to fix an optimization problem.
- **Why Possibly Novel:** Compute-unbounded PEFT training is rarely run because it defeats PEFT's selling point — but as *science* it isolates the mechanism.
- **Minimal Experiment:** Pick 6 tasks with reported LoRA gaps; train LoRA 10× longer with LR re-sweeps; classify each task as capacity- or optimization-limited.
- **Main Risk:** Very long adapter training may overfit small target sets, conflating a third failure mode.

### IDEA-C-0012
- **One-sentence idea:** Predict destructive interference when composing multiple LoRAs from the overlap of their update subspaces.
- **Problem:** Merged/composed adapters degrade unpredictably; there is no accepted pre-merge compatibility test.
- **Core Hypothesis (falsifiable):** Post-merge degradation is a monotone function of principal-angle overlap between adapter subspaces (weighted by singular values); orthogonal adapters compose near-losslessly.
- **Why Important:** Adapter libraries and model-editing pipelines need a compatibility metric before merging becomes standard practice.
- **Why Possibly Novel:** Merging heuristics exist; a validated quantitative interference law with prediction intervals does not.
- **Minimal Experiment:** Train ~20 task adapters on one backbone, merge all pairs, regress pairwise performance drop on subspace overlap; test prediction on held-out triples.
- **Main Risk:** Interference may be layer-heterogeneous, requiring per-layer rather than global overlap measures.

### IDEA-C-0013
- **One-sentence idea:** Show that dense prediction tasks need early-layer adaptation while classification needs late-layer adaptation, explaining PEFT's dense-task weakness.
- **Problem:** PEFT defaults were tuned on classification; dense tasks (segmentation, depth) may fail because the adapted layers are simply the wrong ones.
- **Core Hypothesis (falsifiable):** Layer-restricted LoRA shows opposite depth profiles for dense vs classification tasks (dense: early layers matter most; classification: late layers), and reallocating a fixed parameter budget by task type closes most of the dense-task PEFT gap.
- **Why Important:** A budget reallocation rule is free and would immediately improve PEFT for segmentation.
- **Why Possibly Novel:** Layer-wise PEFT ablations exist per-paper; the cross-task-type *inversion* claim is specific and testable.
- **Minimal Experiment:** Sweep LoRA over layer windows (1–4, 5–8, 9–12) on ADE20K-style segmentation vs classification with the same backbone; compare depth profiles and budget-reallocated variants.
- **Main Risk:** Decoder capacity may mask encoder-layer effects in segmentation; needs a fixed lightweight decoder.

### IDEA-C-0014
- **One-sentence idea:** Measure gradient anti-alignment between a new dense decoder and frozen backbone features as a mechanistic marker for "full FT necessary".
- **Problem:** With a frozen backbone, decoder gradients that *would* flow into the backbone are discarded; if they systematically oppose the frozen features' geometry, no decoder can compensate.
- **Core Hypothesis (falsifiable):** The cosine between (discarded) backbone gradients and the top principal directions of frozen features predicts the frozen-vs-FT gap across tasks; strong anti-alignment ⇒ large gap.
- **Why Important:** Provides a one-forward-backward-pass instrument for deciding whether to unfreeze.
- **Why Possibly Novel:** Gradient-feature alignment has been studied in training dynamics, not as a freeze/unfreeze decision instrument for dense tasks.
- **Minimal Experiment:** For 10 dense tasks, compute the alignment score with a frozen backbone, then measure the actual frozen-vs-FT gap; report rank correlation.
- **Main Risk:** Single-snapshot gradients may be too noisy; may need short-horizon accumulation, still cheap.

### IDEA-C-0015
- **One-sentence idea:** Chart the robustness–plasticity frontier: PEFT preserves pretrained OOD robustness that full FT destroys, and the trade-off is quantifiable per task.
- **Problem:** Full FT wins in-domain but can catastrophically lose the backbone's distributional robustness; the exchange rate is not measured.
- **Core Hypothesis (falsifiable):** For every in-domain point gained by full FT over LoRA, a predictable multiple is lost on a fixed OOD suite; the exchange rate is stable within task families, enabling principled method choice.
- **Why Important:** Deployment decisions (hospital A only vs national rollout) need exactly this exchange rate.
- **Why Possibly Novel:** Robustness-of-fine-tuning is studied for full FT (e.g., weight interpolation); a systematic PEFT-vs-FT exchange-rate law is not established.
- **Minimal Experiment:** Adapt one backbone to 8 tasks with LoRA and FT; evaluate both on matched OOD variants; fit and cross-validate the exchange-rate model.
- **Main Risk:** "OOD" suites are heterogeneous; the exchange rate may not be stable across shift types (which would itself be informative).

### IDEA-C-0016
- **One-sentence idea:** Test whether PEFT specifically fails at small-lesion sensitivity because the required update lives in high-frequency spatial features.
- **Problem:** Aggregate Dice hides that adaptation methods may differ most on the smallest, most clinically important structures.
- **Core Hypothesis (falsifiable):** The LoRA-vs-FT sensitivity gap grows as lesion size shrinks (log-linear in lesion diameter), and injecting adapters into the patch-embedding/early conv stem removes the size dependence.
- **Why Important:** Small-lesion detection is the highest-stakes regime in oncology screening.
- **Why Possibly Novel:** Size-stratified analysis of PEFT is essentially absent; the frequency-localization mechanism gives it a testable cause.
- **Minimal Experiment:** Lesion segmentation dataset stratified by diameter; LoRA (standard vs +stem) vs full FT; plot per-stratum sensitivity.
- **Main Risk:** Small lesions have noisy ground truth; annotation error may dominate the measured gap.

### IDEA-C-0017
- **One-sentence idea:** Build a failure taxonomy showing prompt-tuning and weight-space PEFT fail on *disjoint* task families.
- **Problem:** Token-level (prompt) and weight-level (LoRA) PEFT are treated as interchangeable, but they act on different objects (input distribution vs function).
- **Core Hypothesis (falsifiable):** There exist task families where prompt tuning succeeds and LoRA fails (context re-weighting tasks) and vice versa (feature synthesis tasks), and a simple probe distinguishes them in advance.
- **Why Important:** Method selection currently follows fashion; a validated taxonomy replaces it with measurement.
- **Why Possibly Novel:** Head-to-head PEFT comparisons exist as tables; the *double dissociation* claim with a pre-hoc predictor is new.
- **Minimal Experiment:** Assemble 16 tasks spanning the two hypothesized families; run both methods at matched budgets; test for the predicted dissociation pattern.
- **Main Risk:** Both methods may fail/succeed together on most real tasks, leaving too few dissociating cases.

### IDEA-C-0018
- **One-sentence idea:** Characterize the silent failure of PEFT on CNN-era medical backbones caused by frozen BatchNorm statistics.
- **Problem:** Adapters added to CNNs typically leave running BN statistics frozen at source values, which can dominate the adaptation problem yet is rarely audited.
- **Core Hypothesis (falsifiable):** Across cross-domain medical tasks, recomputing BN statistics on target data accounts for the majority of the total achievable PEFT gain in CNN backbones, and PEFT-without-BN-update sometimes *underperforms* zero-shot.
- **Why Important:** Thousands of deployed medical models are CNN-based; a checklist-level fix could recover large silent losses.
- **Why Possibly Novel:** BN-stat adaptation is known in test-time adaptation but not audited as a confound inside PEFT comparisons.
- **Minimal Experiment:** On 6 cross-site tasks with ResNet/U-Net backbones: zero-shot vs BN-stats-only vs adapter-only vs adapter+BN; decompose the gains.
- **Main Risk:** Findings may not extend to norm-free or GroupNorm architectures (scope limitation, not fatal).

### IDEA-C-0019
- **One-sentence idea:** Test whether PEFT cannot shift a backbone's "resolution prior" — tasks needing a larger effective receptive field require adapting positional components.
- **Problem:** Some transfers (e.g., 224px-pretrained → high-res pathology) require rescaling spatial context, which low-rank weight updates may be structurally unable to do.
- **Core Hypothesis (falsifiable):** When target tasks require an effective receptive field beyond the pretrained regime, LoRA on QKV/MLP fails, but making position embeddings and patch stride trainable (tiny parameter count) closes the gap — a specific, checkable localization of the failure.
- **Why Important:** Resolution mismatch is ubiquitous in medical and remote-sensing transfer.
- **Why Possibly Novel:** Effective-receptive-field analysis has not been connected to PEFT parameterization choices.
- **Minimal Experiment:** Synthetic long-range dependency tasks + high-res pathology segmentation; compare LoRA vs LoRA+positional-tuning vs full FT; measure ERF before/after.
- **Main Risk:** ERF estimation is itself noisy; conclusions need multiple ERF metrics.

### IDEA-C-0020
- **One-sentence idea:** Show that adapting the input stem plus PEFT elsewhere equals full FT for out-of-modality transfer (the "input stem hypothesis").
- **Problem:** RGB-pretrained backbones transferred to ultrasound/OCT/X-ray may fail primarily at the first nonlinearity, not in deep semantics.
- **Core Hypothesis (falsifiable):** For cross-modality transfer, full FT of only the patch-embedding/stem (≤1% of parameters) plus standard LoRA reaches ≥95% of full-FT performance; omitting the stem caps performance regardless of adapter rank.
- **Why Important:** Gives a near-free recipe for the hardest transfer setting in medical imaging.
- **Why Possibly Novel:** Stem-retraining is folklore in scattered repos; a controlled multi-modality validation with the rank-independence claim is missing.
- **Minimal Experiment:** RGB backbone → {ultrasound, OCT, dermoscopy, CXR} tasks; factorial {stem trainable?} × {LoRA rank}; test the predicted ceiling effect.
- **Main Risk:** Some modalities may also need late-layer semantic change (e.g., speckle-defined textures), diluting the claim.

### IDEA-C-0021
- **One-sentence idea:** Measure whether LoRA solutions sit in systematically sharper minima than full-FT solutions, explaining OOD fragility.
- **Problem:** PEFT constrains the solution manifold; the geometry of reachable minima and its consequences are unmeasured.
- **Core Hypothesis (falsifiable):** At matched in-domain accuracy, LoRA solutions have higher loss-landscape sharpness (SAM-style worst-case and Hessian trace) than full-FT solutions, and sharpness differences predict the OOD gap between them.
- **Why Important:** Would connect PEFT's constraint to a concrete generalization mechanism and motivate flatness-aware adapter training.
- **Why Possibly Novel:** Sharpness is studied for training-from-scratch and full FT; the constrained-manifold (adapter) case is unexplored.
- **Minimal Experiment:** 8 tasks × {LoRA, FT}, measure sharpness and OOD accuracy; test mediation (does sharpness statistically explain the OOD gap?).
- **Main Risk:** Sharpness metrics are reparameterization-sensitive; need scale-invariant variants and convergent evidence.

### IDEA-C-0022
- **One-sentence idea:** Fit and test a scaling law for the data-size crossover point where full FT overtakes PEFT.
- **Problem:** "PEFT for small data, FT for big data" is folklore without a quantitative form.
- **Core Hypothesis (falsifiable):** The crossover sample size N* follows a power law in backbone size and task distance (measured by zero-shot transfer accuracy), predictable within 2× across held-out tasks.
- **Why Important:** N* is exactly the number a practitioner needs; a validated law replaces expensive dual training runs.
- **Why Possibly Novel:** Scaling laws exist for pretraining; the PEFT/FT crossover has not been treated as a scaling-law object.
- **Minimal Experiment:** 6 tasks × 6 data sizes × {LoRA, FT} × 2 backbone sizes; fit the crossover law on 4 tasks, predict on 2.
- **Main Risk:** Crossovers may be shallow (near-equal curves), making N* ill-conditioned to estimate.

### IDEA-C-0023
- **One-sentence idea:** Test the hypothesis that PEFT cannot *unlearn* — tasks requiring suppression of misleading pretrained features need full FT.
- **Problem:** Some transfers require actively removing a pretrained cue (e.g., texture bias harmful for modality X); additive low-rank updates may be poor at suppression.
- **Core Hypothesis (falsifiable):** On tasks constructed so that a known pretrained cue is anti-correlated with the target label, the LoRA-vs-FT gap is large and grows with the cue's pretrained salience, while on cue-neutral controls the gap vanishes.
- **Why Important:** Identifies a principled class of "must-full-FT" problems, including shortcut-ridden medical datasets.
- **Why Possibly Novel:** PEFT is analyzed as *adding* capability; the asymmetry between adding and suppressing has not been isolated experimentally.
- **Minimal Experiment:** Cue-conflict datasets (texture vs shape; scanner artifact vs pathology) with controllable correlation; measure gap vs cue salience.
- **Main Risk:** Constructed cue conflicts may exaggerate effects relative to natural datasets; needs one natural validation case.

### IDEA-C-0024
- **One-sentence idea:** Quantify systematic drift when sequentially merging LoRAs over time versus sequential full FT.
- **Problem:** Production systems accumulate adapter updates; whether errors compound differently than in sequential full FT is unknown.
- **Core Hypothesis (falsifiable):** Iterated merge-then-train LoRA cycles diverge from the sequential-FT trajectory at a measurable, superlinear rate in the number of cycles, dominated by accumulating null-space error.
- **Why Important:** Continuous deployment with adapters is becoming default practice without a drift model.
- **Why Possibly Novel:** Single-merge studies exist; iterated-cycle drift dynamics have not been characterized.
- **Minimal Experiment:** 10 sequential adaptation rounds on a domain sequence; track divergence (function-space distance on probe sets) between LoRA-merge and full-FT trajectories.
- **Main Risk:** Divergence may be benign (different but equally good solutions); must measure task metrics, not just distance.

### IDEA-C-0025
- **One-sentence idea:** Test whether PEFT fails harder on regression-style dense outputs (distance maps, depth) than on classification-style dense outputs at matched difficulty.
- **Problem:** PEFT evaluations are dominated by categorical outputs; continuous structured outputs stress different parts of the representation.
- **Core Hypothesis (falsifiable):** At matched task difficulty (equal full-FT headroom over frozen features), the PEFT gap is systematically larger for continuous dense outputs, because low-rank updates preserve decision boundaries better than metric structure.
- **Why Important:** Distance/thickness/flow maps are central to medical quantification; a modality-of-output effect would redirect PEFT method design.
- **Why Possibly Novel:** Output-type as a moderator of PEFT success is an unasked question.
- **Minimal Experiment:** Same images, paired tasks (segmentation vs signed-distance regression to the same structures); LoRA vs FT; compare normalized gaps.
- **Main Risk:** Difficulty matching across output types is nontrivial; requires the frozen/FT-headroom normalization to be convincing.

### IDEA-C-0026
- **One-sentence idea:** Show PEFT routes adaptation through class-token pathways, starving patch-token computation that dense tasks require.
- **Problem:** If adapters preferentially modify computation serving the [CLS] readout, dense tasks inherit an unadapted patch stream.
- **Core Hypothesis (falsifiable):** Attribution of LoRA update effects (via activation patching) shows disproportionate change in CLS-mediated paths vs patch-patch paths; constraining adapters to patch-token pathways improves dense transfer at the same budget.
- **Why Important:** Mechanistic account of the widely observed "PEFT is weaker for segmentation" pattern, with an actionable fix.
- **Why Possibly Novel:** Path-level attribution of *adapter* updates (rather than full models) is new territory.
- **Minimal Experiment:** Patch-vs-CLS path patching on adapted ViTs for classification vs segmentation tasks; then pathway-constrained adapter training.
- **Main Risk:** Path attribution in ViTs is approximate; results must replicate across attribution methods.

### IDEA-C-0027
- **One-sentence idea:** Test whether Fisher-guided *sparse layer selection* (full FT of few layers) dominates low-rank adaptation at equal parameter budgets.
- **Problem:** The community equates "parameter-efficient" with "low-rank", but sparse-in-layers full-rank updates are an unexplored competing structure.
- **Core Hypothesis (falsifiable):** At matched trainable-parameter counts, Fisher-ranked layer unfreezing beats LoRA on tasks previously labeled "PEFT-hard", implying rank — not parameter count — causes those failures.
- **Why Important:** Reframes the PEFT design space and offers a drop-in alternative when LoRA fails.
- **Why Possibly Novel:** Layer-freezing baselines exist, but a budget-matched, Fisher-guided head-to-head aimed at the *failure* regime is missing.
- **Minimal Experiment:** 10 tasks including known LoRA failures; match budgets exactly; compare LoRA vs top-k Fisher layers vs random-k layers.
- **Main Risk:** Fisher estimates on small target data are noisy; random-k control guards against this.

### IDEA-C-0028
- **One-sentence idea:** Determine whether PEFT prevents the acquisition of genuinely new invariances (e.g., stain invariance in pathology) versus reusing pretrained ones.
- **Problem:** Adaptation may require new invariance groups absent from pretraining; whether adapters can install invariances is untested.
- **Core Hypothesis (falsifiable):** Measured invariance (feature sensitivity to controlled nuisance transforms) after LoRA remains near pretrained levels even when the task rewards invariance, while full FT measurably installs it; the invariance deficit predicts the performance gap.
- **Why Important:** Invariance acquisition is the essence of domain robustness; if PEFT cannot do it, its role in medical adaptation must be bounded.
- **Why Possibly Novel:** Invariance is used to explain pretraining, not as a differential test between adaptation methods.
- **Minimal Experiment:** Pathology stain-transfer setup with controllable stain nuisance; measure feature invariance and task accuracy for LoRA/FT across ranks.
- **Main Risk:** Invariance can be implemented in the head rather than features; must probe multiple depths.

### IDEA-C-0029
- **One-sentence idea:** Build a pre-registered "PEFT-hard" benchmark suite where each task is included because a specific mechanistic predictor says PEFT should fail.
- **Problem:** PEFT benchmarks sample convenience tasks; failures are anecdotal and mechanisms untested.
- **Core Hypothesis (falsifiable):** Tasks selected by the predictors (update-rank, shift-frequency, granularity, unlearning-demand) show ≥3× larger PEFT-vs-FT gaps than matched control tasks — validating the predictors as a set.
- **Why Important:** Converts scattered failure anecdotes into a falsifiable, reusable scientific instrument for the field.
- **Why Possibly Novel:** No existing benchmark is constructed *from failure hypotheses* rather than task popularity.
- **Minimal Experiment:** 8 predicted-hard + 8 matched-control tasks; pre-register predictions; run LoRA/FT; score predictor accuracy.
- **Main Risk:** Predictors may be correlated, making it hard to attribute which mechanism drives each failure.

### IDEA-C-0030
- **One-sentence idea:** Test whether PEFT-adapted models lose the ability to be *further* adapted (adaptation begets rigidity).
- **Problem:** Real systems adapt repeatedly; whether a LoRA-adapted model is a worse starting point than an FT-adapted one for the *next* adaptation is unknown.
- **Core Hypothesis (falsifiable):** Second-stage adaptation from a merged-LoRA checkpoint yields systematically lower final performance than from a full-FT checkpoint of equal first-stage accuracy, due to spectrum concentration in the merged update.
- **Why Important:** Sequential adaptability is a hidden cost dimension missing from all PEFT comparisons.
- **Why Possibly Novel:** "Adaptability of adapted models" as a measured quantity appears unstudied.
- **Minimal Experiment:** Two-hop transfer chains (source→A→B) with all four method combinations at hop 1/hop 2; compare final-hop performance.
- **Main Risk:** Effects may be small relative to task-pair variance; needs many chains for power.

---

## C2. Catastrophic forgetting in sequential medical/domain adaptation (IDEA-C-0031 … 0060)

### IDEA-C-0031
- **One-sentence idea:** Test whether forgetting in sequential medical adaptation is size-asymmetric: small structures are forgotten first.
- **Problem:** Forgetting is reported as a single scalar (mean Dice drop), hiding which anatomy loses function.
- **Core Hypothesis (falsifiable):** After adaptation to a new domain, per-structure forgetting is inversely related to structure size (log-linear), because small-structure representations occupy fewer, more easily overwritten feature directions.
- **Why Important:** Small structures (lesions, nerves) are the safety-critical ones; a size-forgetting law would change how continual medical systems are monitored.
- **Why Possibly Novel:** Forgetting has been decomposed by task and class frequency, but not by object scale in dense prediction.
- **Minimal Experiment:** Multi-organ segmentation, sequential fine-tuning across 3 sites; plot per-organ Dice drop vs mean organ volume, control for class frequency.
- **Main Risk:** Size correlates with boundary-to-area ratio and difficulty; needs partial correlation analysis.

### IDEA-C-0032
- **One-sentence idea:** Show that cross-scanner forgetting is largely normalization-statistics drift, reversible by restoring norm parameters alone.
- **Problem:** Forgetting is treated as loss of semantic weights, but for scanner shifts the damage may sit in a handful of affine parameters.
- **Core Hypothesis (falsifiable):** Restoring only the old domain's normalization parameters/statistics (keeping all other adapted weights) recovers ≥70% of the forgotten performance for scanner-type shifts, and <20% for anatomy/population shifts.
- **Why Important:** Would enable near-free multi-scanner deployment via per-site norm banks instead of heavyweight continual learning.
- **Why Possibly Novel:** Norm-swap is used in domain adaptation; using recovery-fraction to *classify the mechanism of forgetting* is new.
- **Minimal Experiment:** Sequential A→B scanner adaptation; measure old-domain recovery from norm-restoration vs full-checkpoint restoration; repeat for a population shift as control.
- **Main Risk:** Interaction terms (weights co-adapted to new norms) may make partial restoration incoherent.

### IDEA-C-0033
- **One-sentence idea:** Determine which exemplars matter for replay: boundary-hard exemplars versus random ones at a fixed 1% memory budget.
- **Problem:** Replay buffers are filled by uniform sampling by default; what information forgetting actually destroys is not used to select memory.
- **Core Hypothesis (falsifiable):** At equal buffer size, exemplars selected for high boundary uncertainty in the old domain reduce forgetting of boundary metrics significantly more than random selection, with no loss on region metrics — implying forgetting concentrates at decision boundaries in input space.
- **Why Important:** Memory is the binding constraint (privacy, storage) in medical continual learning; selection principles multiply its value.
- **Why Possibly Novel:** Exemplar selection is studied for classification diversity; a boundary-information account for dense tasks is untested.
- **Minimal Experiment:** Sequential two-site segmentation with 1% replay; compare random vs boundary-hard vs coverage-based selection on region and boundary metrics.
- **Main Risk:** Boundary-hard exemplars may simply be label-noisy ones, helping for the wrong reason; needs noise audit.

### IDEA-C-0034
- **One-sentence idea:** Decompose forgetting into feature loss vs readout loss by probing frozen features of forgotten models.
- **Problem:** "The model forgot task A" conflates destroyed representations with a re-pointed decoder/head.
- **Core Hypothesis (falsifiable):** After standard sequential adaptation, a linear/light probe on the adapted backbone recovers most old-task performance (readout forgetting), except under modality change where features are genuinely destroyed — two regimes separable by probe-recovery fraction.
- **Why Important:** The remedy differs completely: cheap head re-tuning vs expensive representation protection.
- **Why Possibly Novel:** Probe-based forgetting decomposition exists for classification; regime mapping across realistic medical shift types does not.
- **Minimal Experiment:** Sequential adaptation across site/protocol/modality shifts; at each step probe old-task performance from frozen features; map recovery fraction by shift type.
- **Main Risk:** Probe capacity choice changes conclusions; needs a probe-capacity sweep.

### IDEA-C-0035
- **One-sentence idea:** Show domain-incremental and class-incremental medical adaptation forget via different mechanisms and respond to different remedies.
- **Problem:** Continual-learning methods are benchmarked interchangeably across scenario types, presuming one underlying phenomenon.
- **Core Hypothesis (falsifiable):** Regularization methods (EWC-like) mitigate domain-incremental forgetting but not class-incremental forgetting at matched severity, while replay shows the reverse asymmetry — a double dissociation.
- **Why Important:** Hospitals face both scenarios (new scanners; new target structures); method choice should follow mechanism.
- **Why Possibly Novel:** The dissociation claim is sharper than existing scenario comparisons, and untested in dense medical tasks.
- **Minimal Experiment:** Same dataset re-split into domain-incremental and class-incremental sequences of matched difficulty; cross the two method families; test the interaction.
- **Main Risk:** "Matched severity" across scenario types is hard to define; requires a calibration pilot.

### IDEA-C-0036
- **One-sentence idea:** Validate gradient-conflict between old and new tasks as a pre-hoc predictor of forgetting magnitude.
- **Problem:** Forgetting is measured post-hoc; deployments need a forecast before committing to adaptation.
- **Core Hypothesis (falsifiable):** The cosine between new-task gradients and old-task gradients (measured over one epoch, old data or proxies) predicts final old-task performance drop with rank correlation ≥0.7 across task pairs.
- **Why Important:** A cheap forecast enables gating: adapt freely when conflict is low, deploy protection when high.
- **Why Possibly Novel:** Gradient conflict is used *inside* multi-task methods; as a standalone forgetting forecaster across medical domain sequences it is unvalidated.
- **Minimal Experiment:** 20 ordered domain pairs; measure early gradient conflict, run adaptation, correlate with realized forgetting.
- **Main Risk:** Conflict may evolve during training, making early measurement unrepresentative; test multiple horizons.

### IDEA-C-0037
- **One-sentence idea:** Characterize two-phase forgetting dynamics: fast decoder forgetting followed by slow encoder forgetting.
- **Problem:** Forgetting curves are reported at sequence end; the temporal structure — which components degrade when — is unknown.
- **Core Hypothesis (falsifiable):** Old-task performance decays as a sum of two exponentials whose fast component is eliminated by freezing the decoder and slow component by freezing the encoder — identifying the anatomical locus of each phase.
- **Why Important:** Monitoring and intervention timing (when to snapshot, when to rehearse) should follow the dynamics.
- **Why Possibly Novel:** Component-resolved forgetting *dynamics* (not endpoints) are unmeasured in dense prediction.
- **Minimal Experiment:** Dense checkpointing during adaptation; old-task evaluation per checkpoint; fit two-timescale model; verify with component-freezing interventions.
- **Main Risk:** Dynamics may be optimizer-dependent (Adam vs SGD), requiring replication across optimizers.

### IDEA-C-0038
- **One-sentence idea:** Test whether EWC-style methods fail in medical adaptation because small-data Fisher estimates are mostly noise.
- **Problem:** Importance-weighted regularization underperforms in medical continual learning; the standard explanation (method weakness) may actually be estimator failure.
- **Core Hypothesis (falsifiable):** With an oracle Fisher (estimated on the full old dataset), EWC closes most of its gap to replay; with realistic small retained sets, Fisher rank-correlates poorly with true parameter importance — locating the failure in estimation, not the principle.
- **Why Important:** Rescues (or definitively buries) a whole method family for privacy-constrained settings where replay is prohibited.
- **Why Possibly Novel:** The estimator-vs-principle decomposition for EWC in dense medical tasks has not been performed.
- **Minimal Experiment:** Vary Fisher-estimation set size from 10 to full dataset; measure forgetting vs estimation quality; compare with importance from held-out ablation.
- **Main Risk:** Even oracle Fisher may fail for dense tasks (diagonal approximation), which needs a block-diagonal control.

### IDEA-C-0039
- **One-sentence idea:** Quantify how generative pseudo-replay biases rare-pathology performance worse than the forgetting it prevents.
- **Problem:** Generative replay is promoted as privacy-preserving, but generators underfit rare findings, so replayed distributions are systematically distorted.
- **Core Hypothesis (falsifiable):** Pseudo-replay preserves mean old-domain Dice but *reduces* rare-class old-domain sensitivity below the no-replay baseline, because the generator's mode coverage acts as a rare-class filter.
- **Why Important:** A method adopted for safety reasons may be quietly unsafe for exactly the rare cases that matter.
- **Why Possibly Novel:** Generative-replay evaluations report means; tail-stratified harm has not been demonstrated or ruled out.
- **Minimal Experiment:** Sequential adaptation with generative replay vs no replay vs real replay; stratify old-domain evaluation by class frequency; measure tail sensitivity.
- **Main Risk:** Result may be generator-specific; needs at least two generator families (GAN, diffusion).

### IDEA-C-0040
- **One-sentence idea:** Distinguish erasure from retrieval failure: how much "forgotten" performance returns with a tiny rewinding set.
- **Problem:** Forgetting metrics cannot tell whether knowledge is destroyed or merely inaccessible under the shifted parameterization.
- **Core Hypothesis (falsifiable):** For most site-shift sequences, re-exposure to ≤20 old-domain images restores ≥80% of lost performance in a few steps (retrieval failure), while modality-shift sequences show slow, data-hungry recovery (erasure) — a measurable dichotomy with different protection implications.
- **Why Important:** If forgetting is mostly retrieval failure, cheap "reminder" protocols beat expensive continual-learning machinery.
- **Why Possibly Novel:** Rapid-recovery ("rewinding") curves as a forgetting taxonomy are established in neuroscience but not in medical CL.
- **Minimal Experiment:** After each adaptation step, fine-tune on k∈{5,20,100} old images; plot recovery vs k across shift types.
- **Main Risk:** Recovery speed confounds with learning-rate settings; requires LR-matched controls.

### IDEA-C-0041
- **One-sentence idea:** Test whether domain ordering (curriculum over shift magnitude) changes total forgetting in a predictable direction.
- **Problem:** Deployment order of adaptations is often controllable, yet no evidence-based ordering principle exists.
- **Core Hypothesis (falsifiable):** Sequences ordered by increasing shift magnitude (measured by feature-space divergence) produce lower total forgetting than decreasing or random orders, because early small shifts consolidate shared structure.
- **Why Important:** Ordering is a free intervention for multi-site rollouts.
- **Why Possibly Novel:** Task-order effects are known in classification CL; shift-magnitude-based ordering for medical dense tasks is untested.
- **Minimal Experiment:** 4 domains, all 24 orderings (or a balanced subset), fixed budget; regress total forgetting on ordering statistics.
- **Main Risk:** Ordering effects may be small relative to inter-seed variance; needs power analysis first.

### IDEA-C-0042
- **One-sentence idea:** Establish calibration forgetting as an early-warning signal that precedes accuracy forgetting.
- **Problem:** Monitoring continual systems via accuracy detects damage late; earlier-moving indicators are unknown.
- **Core Hypothesis (falsifiable):** During sequential adaptation, old-domain ECE degrades measurably earlier (in steps) than old-domain Dice, and the lead time is consistent enough to trigger protective interventions.
- **Why Important:** Provides a deployable canary metric for clinical continual learning governance.
- **Why Possibly Novel:** Calibration under continual learning is barely studied; its use as a *leading indicator* is new.
- **Minimal Experiment:** Dense checkpointing; track old-domain ECE and Dice trajectories; measure lead-lag across 10 runs.
- **Main Risk:** ECE estimation noise on small old-domain sets may swamp the lead signal.

### IDEA-C-0043
- **One-sentence idea:** Compare forgetting under real temporal hospital drift versus artificial dataset splits used in benchmarks.
- **Problem:** CL benchmarks simulate domain sequences by dataset concatenation; real clinical drift (gradual protocol/population change) may produce different forgetting profiles.
- **Core Hypothesis (falsifiable):** Under real time-ordered data from one institution, forgetting is smaller but more selective (concentrated on protocol-linked classes) than under artificial domain-switch benchmarks matched for total shift.
- **Why Important:** If benchmark forgetting is qualitatively wrong, the field is optimizing methods for a phenomenon that does not occur in deployment.
- **Why Possibly Novel:** Time-ordered medical CL evaluations are rare; direct artificial-vs-real profile comparison appears absent.
- **Minimal Experiment:** One public dataset with acquisition dates; train time-ordered vs shuffled-domain-switch; compare forgetting structure at matched divergence.
- **Main Risk:** Access to date-annotated public data is limited; may need to combine 2–3 datasets.

### IDEA-C-0044
- **One-sentence idea:** Test whether modality-incremental forgetting (CT→MR→US) concentrates in early layers — the opposite of the classification-CL picture.
- **Problem:** CL theory built on natural-image classification claims later layers are more plastic and forgetful; modality shifts stress early layers instead.
- **Core Hypothesis (falsifiable):** Layer-wise representational drift (CKA between pre/post checkpoints) under modality-incremental sequences peaks in early layers, and early-layer parameter isolation (per-modality stems) removes most forgetting — inverting standard depth-of-forgetting findings.
- **Why Important:** Correct depth targeting makes parameter-isolation methods far cheaper.
- **Why Possibly Novel:** Depth profile of forgetting has not been mapped for modality-incremental dense tasks.
- **Minimal Experiment:** CT→MR→US segmentation sequence; per-layer CKA drift + per-depth isolation interventions; compare with a class-incremental control.
- **Main Risk:** CKA drift is an imperfect proxy for functional forgetting; complement with layer-swapping tests.

### IDEA-C-0045
- **One-sentence idea:** Quantify silent router failure in per-domain-adapter architectures when confronted with unseen domains.
- **Problem:** LoRA-per-domain with a domain router "solves" forgetting, but the router becomes the new single point of failure — its OOD behavior is unaudited.
- **Core Hypothesis (falsifiable):** For inputs from unseen sites, router misassignment rates exceed 30% while router confidence remains high, and misrouted predictions are worse than a domain-agnostic fallback — a measurable safety inversion.
- **Why Important:** Adapter-bank deployments are proliferating; their failure mode analysis lags far behind.
- **Why Possibly Novel:** Router OOD calibration in continual medical systems has not been measured.
- **Minimal Experiment:** Train 4-site adapter bank + router; evaluate routing and end-task performance on 2 held-out sites vs a single jointly-trained model.
- **Main Risk:** Result depends on router design; needs 2–3 router types (feature-stats, learned classifier, retrieval).

### IDEA-C-0046
- **One-sentence idea:** Use a self-supervised loss on unlabeled old-domain images as a label-free anti-forgetting regularizer.
- **Problem:** Replay needs labels or generators; but unlabeled old-domain images are often retainable when labels/PHI-linked masks are not.
- **Core Hypothesis (falsifiable):** Maintaining an SSL objective (e.g., masked reconstruction) on retained unlabeled old-domain images during new-domain training preserves old-task Dice within 2 points of labeled replay at equal buffer size — implying most forgetting is representational, not decision-level.
- **Why Important:** Unlabeled retention is a dramatically easier governance ask than labeled retention in hospitals.
- **Why Possibly Novel:** SSL-as-rehearsal has been sketched for classification; a quantitative equivalence test against labeled replay for medical segmentation is missing.
- **Minimal Experiment:** Two-site sequence; compare {nothing, SSL-rehearsal, labeled replay} at matched image budgets.
- **Main Risk:** If forgetting is decision-level (see 0034), SSL rehearsal will fail — which is itself the diagnostic point.

### IDEA-C-0047
- **One-sentence idea:** Establish a long-tail forgetting law: rare classes are forgotten first and disproportionately.
- **Problem:** Mean forgetting metrics mask frequency-dependent damage that matters most clinically.
- **Core Hypothesis (falsifiable):** Per-class forgetting is a decreasing function of old-domain class frequency with a stable functional form across datasets, allowing forecast of rare-class damage from the frequency histogram alone.
- **Why Important:** Enables pre-hoc risk assessment: given a new adaptation, predict which findings degrade before touching a single patient.
- **Why Possibly Novel:** Frequency-stratified forgetting has anecdotes but no cross-dataset law with predictive validation.
- **Minimal Experiment:** 5 datasets with long-tailed masks; sequential adaptation; fit the frequency-forgetting curve on 3, predict on 2.
- **Main Risk:** Frequency confounds with size and difficulty; requires multivariate control.

### IDEA-C-0048
- **One-sentence idea:** Compare forgetting between BatchNorm and GroupNorm/LayerNorm architectures as a designed determinant, not an incidental one.
- **Problem:** Normalization choice changes what information is stored in statistics vs weights, plausibly changing forgetting pathways — untested directly.
- **Core Hypothesis (falsifiable):** At matched initial accuracy, BN models forget more under distribution shift sequences (statistics corruption) but recover faster with norm restoration, while GN/LN models forget less but recover more slowly — a testable trade-off.
- **Why Important:** Normalization is a free architectural choice at design time; forgetting behavior should inform it.
- **Why Possibly Novel:** Normalization is controlled as a nuisance in CL papers, never treated as the object of study.
- **Minimal Experiment:** Same U-Net/ViT with BN vs GN vs LN; identical sequences; measure forgetting and restoration curves.
- **Main Risk:** Matching initial accuracy across norm types requires tuning that may itself bias plasticity.

### IDEA-C-0049
- **One-sentence idea:** Measure the transient "stability gap" at domain-switch moments and its clinical significance even when final accuracy recovers.
- **Problem:** Continual systems are evaluated at sequence end; the transient collapse right after a switch happens *during live deployment*.
- **Core Hypothesis (falsifiable):** In standard sequential adaptation, old-domain performance exhibits a transient drop whose depth × duration (patient-exposure integral) exceeds the final forgetting by a large factor, and slow-start learning-rate schedules shrink it at no final-accuracy cost.
- **Why Important:** Reframes CL evaluation around patient exposure during transitions — the operationally relevant quantity.
- **Why Possibly Novel:** The stability gap is documented in classification CL; its exposure-integral framing and mitigation for medical dense tasks are not.
- **Minimal Experiment:** High-frequency evaluation during switches; compute exposure integrals; test warmup interventions.
- **Main Risk:** High-frequency evaluation is compute-heavy; subsample evaluation sets carefully.

### IDEA-C-0050
- **One-sentence idea:** Benchmark sequential-checkpoint weight averaging as a nearly-free anti-forgetting baseline that may beat dedicated CL methods.
- **Problem:** CL literature compares against weak naive baselines; simple weight averaging across domain checkpoints is rarely in the comparison set.
- **Core Hypothesis (falsifiable):** Uniform or Fisher-weighted averaging of per-domain fine-tuned checkpoints attains lower average forgetting than EWC and matches modest replay on cross-site medical segmentation — at zero training-time overhead.
- **Why Important:** If a trivial baseline wins, the field's method complexity is unjustified, and deployment guidance changes immediately.
- **Why Possibly Novel:** Model soups are known for robustness; positioning and rigorously testing them as a *continual-learning baseline* in medical dense prediction is largely unexplored.
- **Minimal Experiment:** 4-domain sequence; compare naive sequential, EWC, 1% replay, and checkpoint averaging on average accuracy/forgetting.
- **Main Risk:** Averaging fails when domains induce non-linearly-connected minima (e.g., modality shifts); scope must be honestly reported.

### IDEA-C-0051
- **One-sentence idea:** Show that prompt/PEFT-based continual learning avoids forgetting but also forfeits positive backward transfer.
- **Problem:** Parameter-isolated CL is sold on "no forgetting", but consolidation benefits (later tasks improving earlier ones) may be structurally impossible.
- **Core Hypothesis (falsifiable):** Across medical domain sequences, isolated-adapter CL exhibits backward transfer statistically indistinguishable from zero, while full-parameter sequential FT with replay shows measurable positive backward transfer on related domains — a trade-off currently priced at zero.
- **Why Important:** If backward transfer is real and valuable, isolation methods are silently leaving performance on the table.
- **Why Possibly Novel:** Backward transfer in medical CL is rarely even reported; the isolation-vs-consolidation dichotomy is untested.
- **Minimal Experiment:** Related-domain sequences (same anatomy, different scanners); measure backward transfer matrices for isolated vs shared-parameter methods.
- **Main Risk:** Positive backward transfer may be rare in practice, making the comparison moot (also a publishable null).

### IDEA-C-0052
- **One-sentence idea:** Test whether representational similarity metrics (CKA) actually predict functional forgetting — or systematically mislead.
- **Problem:** CL analyses increasingly use CKA drift as a forgetting proxy without validating it against task-level damage.
- **Core Hypothesis (falsifiable):** Across layers and sequences, CKA drift explains <30% of variance in per-class functional forgetting, and cases of high-CKA-drift-with-no-forgetting (benign reparameterization) are common — invalidating CKA as a monitoring metric.
- **Why Important:** Wrong proxies drive wrong method development; the field needs to know if its favorite lens is distorted.
- **Why Possibly Novel:** Proxy-validation studies for CL metrics are essentially absent.
- **Minimal Experiment:** Instrumented sequences with per-checkpoint CKA and per-class metrics; regress and hunt for dissociation cases.
- **Main Risk:** Result may depend on CKA variant (linear/RBF, batch construction); test several.

### IDEA-C-0053
- **One-sentence idea:** Test whether forgetting-inducing updates live in a low-dimensional subspace that can be projected out during new-domain training.
- **Problem:** Full-space regularization (penalize all weight motion) over-constrains plasticity; maybe only a few directions do the damage.
- **Core Hypothesis (falsifiable):** Projecting new-task gradients off the top-k principal directions of old-task gradient covariance (small k) removes most forgetting while retaining ≥90% of new-task gains — establishing low-dimensionality of interference in medical dense tasks.
- **Why Important:** Would replace scalar regularization trade-offs with a targeted, nearly-free intervention.
- **Why Possibly Novel:** Gradient-projection CL exists for small classification setups; the dimensionality question and its validation on realistic medical segmentation are open.
- **Minimal Experiment:** Two-domain sequences; sweep k; plot forgetting and plasticity vs k to find the claimed knee.
- **Main Risk:** Old-gradient covariance requires stored old data or proxies; privacy-compatible estimation must be shown.

### IDEA-C-0054
- **One-sentence idea:** Measure how much old-domain function is preserved by distilling the old model into the new one using only new-domain images.
- **Problem:** Data-free preservation via distillation on *new* inputs assumes new images exercise old behaviors — an assumption never quantified.
- **Core Hypothesis (falsifiable):** The fraction of old-domain performance preserved by new-data distillation is predicted by the feature-space coverage of the old domain by new-domain images; below a coverage threshold, distillation preserves style but not decision behavior.
- **Why Important:** Data-free CL is the only legally comfortable option in many hospitals; its real preservation power needs numbers.
- **Why Possibly Novel:** Coverage-conditioned analysis of data-free distillation is missing; current papers report single aggregate scores.
- **Minimal Experiment:** Vary domain-pair overlap systematically; distill on new-domain only; regress preservation on measured coverage.
- **Main Risk:** Coverage metrics in feature space may not capture decision-relevant coverage; use multiple coverage definitions.

### IDEA-C-0055
- **One-sentence idea:** Show that a single global stability-plasticity coefficient is wrong: optimal regularization strength varies by orders of magnitude across layers.
- **Problem:** CL methods use one λ for the whole network, implicitly assuming uniform interference across depth.
- **Core Hypothesis (falsifiable):** Per-layer λ optimization (even a coarse 3-level scheme: stem/middle/head) beats the best global λ by a margin larger than the gap between competing CL methods — implying tuning granularity matters more than method identity.
- **Why Important:** Redirects effort from new penalty designs to allocation of a fixed penalty budget.
- **Why Possibly Novel:** Per-layer regularization exists in scattered forms; the claim that it dominates method choice is a sharp, checkable statement.
- **Minimal Experiment:** EWC/L2 variants with global vs 3-level vs per-layer λ on two sequences; compare against method-swap deltas.
- **Main Risk:** Per-layer tuning has more hyperparameters; must use equal tuning budgets to be fair.

### IDEA-C-0056
- **One-sentence idea:** Quantify cumulative "TTA drift": continuously running test-time adaptation in deployment causes progressive forgetting.
- **Problem:** TTA methods (entropy minimization, statistics updates) are evaluated per-batch; deployed continuously, their updates compound without any consolidation mechanism.
- **Core Hypothesis (falsifiable):** Under a realistic stream (site mixture with rare-case bursts), continuous TTA degrades monotonically on a frozen reference set, with drift rate proportional to stream non-stationarity; periodic parameter resets trade recent-gain for drift elimination at a measurable exchange rate.
- **Why Important:** TTA is being deployed as a safety feature while possibly being a slow poison; the field needs the drift law.
- **Why Possibly Novel:** Lifelong/continual TTA is nascent; a quantitative drift model tied to stream statistics for medical imaging does not exist.
- **Minimal Experiment:** Simulate 100k-image streams with controlled non-stationarity; run TENT-style TTA continuously; track reference-set performance and fit drift-rate model.
- **Main Risk:** Drift may be method-specific; needs 3 TTA families to claim generality.

### IDEA-C-0057
- **One-sentence idea:** Disentangle true representational forgetting from annotation-protocol mismatch when measuring cross-site "forgetting".
- **Problem:** Old-site performance drops after adaptation may partly reflect that the new site's *label style* was learned — a labeling artifact, not knowledge loss.
- **Core Hypothesis (falsifiable):** Re-annotating a small old-site subset under the new site's protocol reduces measured "forgetting" by a substantial fraction (>30%) in protocol-divergent dataset pairs, and by ~0% in protocol-matched pairs.
- **Why Important:** If a chunk of reported forgetting is protocol artifact, the CL literature overestimates the phenomenon it studies.
- **Why Possibly Novel:** Label-protocol confounds in forgetting measurement have not been isolated experimentally.
- **Minimal Experiment:** Two dataset pairs (protocol-matched, protocol-divergent); re-annotate 50 old images per pair under the new protocol; recompute forgetting.
- **Main Risk:** Re-annotation is costly and needs clinician time; keep subsets minimal and targeted.

### IDEA-C-0058
- **One-sentence idea:** Test whether forgetting hits pathology-specific features harder than shared-anatomy features during cross-domain adaptation.
- **Problem:** Anatomy is common across domains, pathology expression is domain/protocol-entangled; forgetting may selectively destroy the latter.
- **Core Hypothesis (falsifiable):** After adaptation, probes for anatomical structure on old-domain images retain near-baseline accuracy while probes for pathology presence degrade substantially — and this asymmetry predicts which downstream tasks are safe to adapt.
- **Why Important:** Gives a content-level (not class-level) account of what continual medical systems lose first.
- **Why Possibly Novel:** Anatomy-vs-pathology decomposition of forgetting is a new measurement axis.
- **Minimal Experiment:** Joint anatomy+pathology labels on old domain; probe both from checkpoints along an adaptation trajectory; compare decay rates.
- **Main Risk:** Pathology probes are harder tasks a priori; must normalize by initial probe headroom.

### IDEA-C-0059
- **One-sentence idea:** Evaluate public-data proxies (same modality, different institution) as privacy-preserving replay for private old domains.
- **Problem:** True replay is often prohibited; whether public look-alike data can stand in for private old-domain data is an empirical question nobody has quantified.
- **Core Hypothesis (falsifiable):** Replay with public proxy data recovers a fraction of true-replay benefit proportional to proxy-to-old feature-distribution overlap, exceeding 70% of true replay for well-matched proxies — enabling a practical selection criterion for proxy datasets.
- **Why Important:** Turns an ad-hoc trick into a measurable, defensible privacy-preserving protocol.
- **Why Possibly Novel:** Proxy-replay exists as folklore; the overlap-conditioned quantitative treatment does not.
- **Minimal Experiment:** Private/public pairs across 3 modalities; replay with proxies of varying measured overlap; fit benefit-vs-overlap curve.
- **Main Risk:** Public proxies may leak the *test* distribution (contamination); needs contamination audit.

### IDEA-C-0060
- **One-sentence idea:** Characterize when adaptation to a new domain *improves* the old domain (positive backward transfer) in medical imaging.
- **Problem:** CL research is organized entirely around preventing loss, ignoring that some adaptations should help old domains (e.g., learning noise robustness).
- **Core Hypothesis (falsifiable):** Positive backward transfer occurs systematically when the new domain is a degraded version of the old (noise, lower dose, motion) and never when it is laterally shifted (different anatomy prevalence) — a predictable sign rule based on shift geometry.
- **Why Important:** A sign-prediction rule would let deployments schedule beneficial adaptations aggressively and gate harmful ones.
- **Why Possibly Novel:** Systematic characterization of *when* backward transfer is positive appears absent in medical CL.
- **Minimal Experiment:** Construct degradation-shift and lateral-shift pairs from the same base dataset; measure backward transfer sign and magnitude across 10 pairs.
- **Main Risk:** Constructed shifts may not represent real site differences; validate on at least one natural pair.

---

## C3. VLMs for dense prediction: alignment vs localization mismatch (IDEA-C-0061 … 0090)

### IDEA-C-0061
- **One-sentence idea:** Quantify "global leakage": how much of each CLIP patch token's content is image-level semantics rather than local content.
- **Problem:** Contrastive image-text training optimizes a global objective; patch tokens may become carriers of global information, corrupting their use for dense prediction.
- **Core Hypothesis (falsifiable):** Mutual information between a patch token and the image-level label exceeds that between the token and its own receptive-field content in late CLIP layers, and the leakage ratio predicts zero-shot segmentation failure per layer.
- **Why Important:** Explains, mechanistically, why naive dense readouts from CLIP fail — and where (which layer) to read instead.
- **Why Possibly Novel:** Global-vs-local content of patch tokens has been gestured at (attention visualizations) but not measured information-theoretically or linked predictively to dense-task performance.
- **Minimal Experiment:** Probe patch tokens for (a) global label and (b) local patch identity across layers; correlate the leakage ratio with per-layer zero-shot segmentation quality.
- **Main Risk:** MI estimation on high-dim features is hard; use classifier-based bounds and report sensitivity.

### IDEA-C-0062
- **One-sentence idea:** Measure how alignment training collapses the spatial variance of patch-text similarity maps across training checkpoints.
- **Problem:** If alignment progressively homogenizes patch-text similarity across space, localization ability is destroyed *by the objective itself*, not by architecture.
- **Core Hypothesis (falsifiable):** Spatial entropy of patch-text similarity maps decreases monotonically with contrastive training progress while retrieval accuracy increases — a measurable trade-off curve with a knee that defines the best dense-task checkpoint (not the final one).
- **Why Important:** Suggests dense practitioners should use intermediate checkpoints — a zero-cost improvement if the curve exists.
- **Why Possibly Novel:** Checkpoint-time analysis of localization decay in VLM training has not been published; open training runs (e.g., OpenCLIP checkpoints) make it feasible.
- **Minimal Experiment:** Evaluate public intermediate OpenCLIP checkpoints for retrieval vs unsupervised segmentation quality; plot the trade-off.
- **Main Risk:** Public checkpoint grids may be too sparse near the knee.

### IDEA-C-0063
- **One-sentence idea:** Show that VLM dense grounding fails on spatial-relational language ("left kidney", "above the carina") because alignment is effectively bag-of-words.
- **Problem:** Open-vocabulary segmentation is evaluated on category names; clinical language is relational, and contrastive text encoders may discard word order and relations.
- **Core Hypothesis (falsifiable):** On a controlled benchmark where target masks differ only by spatial relation words, CLIP-derived dense models perform at chance, while their performance on category words is preserved — localizing the failure to relational composition, not vision.
- **Why Important:** Relational grounding is a prerequisite for clinically usable language-driven segmentation.
- **Why Possibly Novel:** Bag-of-words behavior is documented for retrieval; its specific consequence for *dense* prediction with a controlled mask-level benchmark is not.
- **Minimal Experiment:** Synthetic + curated real images with paired relational prompts; evaluate several open-vocab segmenters; compare relational vs categorical accuracy.
- **Main Risk:** Chance-level definition requires careful prompt controls (swap tests) to avoid trivial confounds.

### IDEA-C-0064
- **One-sentence idea:** Quantify the object-centric bias of VLM-based segmenters: amorphous "stuff" and diffuse pathology are systematically worse than countable "things".
- **Problem:** Caption data describes objects; diffuse regions (edema, infiltrates, "background" tissue) are under-described, plausibly creating a class-type performance cliff.
- **Core Hypothesis (falsifiable):** Across open-vocab segmenters, performance gap between things and stuff classes (matched for pixel frequency and boundary complexity) exceeds the gap attributable to those confounds, and the residual gap correlates with caption-mention statistics of each class in pretraining corpora.
- **Why Important:** Diffuse abnormality is a huge fraction of medical findings; a structural VLM bias against it must be measured before medical adoption.
- **Why Possibly Novel:** Things-vs-stuff is a known split, but its causal attribution to caption statistics with confound matching is untested.
- **Minimal Experiment:** Confound-matched class pairs on panoptic datasets; regress residual gap on caption-frequency statistics from public corpora (LAION word counts).
- **Main Risk:** Confound matching (frequency, boundary complexity) is imperfect; requires several matching schemes.

### IDEA-C-0065
- **One-sentence idea:** Establish a layer-selection law: which VLM layer to read for dense tasks as a function of alignment strength and task granularity.
- **Problem:** Everyone knows "last layer is bad for localization" anecdotally; there is no quantitative rule for choosing the readout layer without downstream validation.
- **Core Hypothesis (falsifiable):** The optimal readout layer index (fraction of depth) is a stable function of task granularity (target object scale) across VLM sizes and datasets, predictable within ±1 layer from two cheap measurements (leakage ratio and spatial-frequency of targets).
- **Why Important:** Removes a hidden hyperparameter that silently varies across papers, confounding comparisons.
- **Why Possibly Novel:** Layer-choice is treated as per-paper tuning; a predictive law with cross-model validation would be new.
- **Minimal Experiment:** Grid of {4 VLMs × 6 dense tasks × all layers}; fit the law on half, predict optimal layer on the rest.
- **Main Risk:** Interactions with decoder capacity may blur layer optima; use fixed linear decoders.

### IDEA-C-0066
- **One-sentence idea:** Detect and pre-emptively mask ViT artifact/high-norm tokens that corrupt dense predictions from VLM features.
- **Problem:** High-norm "register-like" artifact tokens appear in large ViTs and act as global information hubs at arbitrary spatial positions, poisoning dense readouts at those positions.
- **Core Hypothesis (falsifiable):** Artifact-token locations are predictable from input statistics (low-information patches) before the forward pass; masking/replacing their features improves dense metrics specifically at those locations without retraining, with effect size proportional to artifact-token density.
- **Why Important:** A train-free patch to a known corruption source in every frozen-VLM dense pipeline.
- **Why Possibly Novel:** Artifact tokens are documented; a *pre-hoc predictor* plus a train-free dense-task correction and its quantitative accounting are not.
- **Minimal Experiment:** Identify high-norm tokens across images, train a tiny predictor from raw patches, apply masking correction, measure localized metric gains.
- **Main Risk:** In heavily artifact-dependent models, masking may harm global context; needs per-model dose-response analysis.

### IDEA-C-0067
- **One-sentence idea:** Treat class-name prompt sensitivity as measurement noise and re-estimate open-vocab segmentation leaderboards with prompt-averaged confidence intervals.
- **Problem:** Zero-shot dense results swing wildly with synonym choice ("sofa" vs "couch"), yet leaderboards report single-prompt point estimates.
- **Core Hypothesis (falsifiable):** Across published open-vocab segmenters, the within-method variance across reasonable prompt paraphrases exceeds the between-method differences for a substantial fraction of benchmark class pairs — meaning many reported rankings are prompt artifacts.
- **Why Important:** If rankings are noise, the field's progress narrative in open-vocab dense prediction needs statistical repair.
- **Why Possibly Novel:** Prompt sensitivity is known for classification; a formal noise-model treatment of *dense benchmark rankings* is absent.
- **Minimal Experiment:** 5 public methods × 20 prompt paraphrase sets × 2 benchmarks; variance decomposition of scores; report which claimed gaps survive.
- **Main Risk:** Choosing "reasonable paraphrases" is subjective; use multiple paraphrase sources including model-generated and human ones.

### IDEA-C-0068
- **One-sentence idea:** Measure the conservation trade-off: dense-alignment fine-tuning of VLMs degrades their zero-shot global classification predictably.
- **Problem:** Methods that re-align VLMs for segmentation report dense gains without reporting global-ability losses; whether a conservation-like trade-off exists is unknown.
- **Core Hypothesis (falsifiable):** Across dense-adaptation methods, zero-shot classification loss is a monotone function of dense-localization gain at fixed data/compute, with a method-independent frontier — i.e., no current method escapes the trade-off, only moves along it.
- **Why Important:** A frontier, if real, sets expectations and redirects research toward frontier-shifting rather than point-claiming.
- **Why Possibly Novel:** The dense-vs-global trade-off has not been mapped as a frontier across methods.
- **Minimal Experiment:** 6 dense-adaptation recipes on the same VLM; measure (dense gain, global loss) pairs; test frontier collapse across methods.
- **Main Risk:** Methods differ in data/compute; strict matching is essential and laborious.

### IDEA-C-0069
- **One-sentence idea:** Isolate whether VLM localization ability comes from data co-occurrence statistics rather than architecture, using fully controlled synthetic pretraining.
- **Problem:** Debates about which VLM architecture localizes better are confounded by uncontrolled pretraining data.
- **Core Hypothesis (falsifiable):** Training identical architectures on synthetic image-caption corpora with controlled object-word co-occurrence shows that localization emerges only when captions are spatially discriminative (mention subsets of objects), regardless of architecture family — data statistics dominate architecture for grounding.
- **Why Important:** Would refocus grounding research from architectural tweaks to caption-data curation.
- **Why Possibly Novel:** Controlled-corpus causal studies of grounding emergence at meaningful scale are missing.
- **Minimal Experiment:** Synthetic multi-object scenes; caption policies varying spatial discriminativeness; small CLIP-style training; measure emergent patch-text grounding.
- **Main Risk:** Synthetic-scale findings may not extrapolate; anchor with one targeted real-data ablation (caption filtering).

### IDEA-C-0070
- **One-sentence idea:** Audit open-vocabulary segmentation benchmarks for class-name contamination with pretraining captions by re-evaluating under renamed ontologies.
- **Problem:** "Open-vocabulary" success may be memorized name-image associations; renaming classes to unusual but precise synonyms tests true generalization.
- **Core Hypothesis (falsifiable):** Replacing benchmark class names with rare synonyms/descriptions (validated as understandable via text-encoder similarity to originals) drops open-vocab segmenters substantially more than it drops human-anchored expectations, and the drop correlates with the original name's caption frequency.
- **Why Important:** Distinguishes vocabulary generalization from vocabulary memorization — the field's central claim.
- **Why Possibly Novel:** Name-frequency-conditioned re-evaluation of *dense* open-vocab claims appears undone.
- **Minimal Experiment:** Build renamed ontologies for 2 benchmarks; evaluate 5 methods; regress performance drop on LAION name frequency.
- **Main Risk:** Rare synonyms may be genuinely ambiguous; filter with human validation of prompt clarity.

### IDEA-C-0071
- **One-sentence idea:** Audit translation and shift equivariance of VLM dense readouts caused by absolute position embeddings.
- **Problem:** Dense predictions should move with content; VLM patch features entangle absolute position, producing inconsistent segmentations under small image shifts.
- **Core Hypothesis (falsifiable):** Sub-patch translations of the input change VLM-based segmentations far more than CNN baselines (measured by prediction self-consistency), and the inconsistency concentrates at positions where position-embedding norm dominates content norm.
- **Why Important:** Prediction instability under trivial transforms is a deployment hazard and an unmeasured error source in benchmarks.
- **Why Possibly Novel:** Shift-equivariance audits exist for CNNs (aliasing); a systematic VLM/ViT dense-readout audit tied to positional-embedding dominance is missing.
- **Minimal Experiment:** Shift battery (0–16px) on frozen-VLM segmenters vs CNNs; consistency metrics; per-position attribution to positional embeddings.
- **Main Risk:** Resampling artifacts from shifting confound the measurement; use integer shifts with crop-consistent evaluation.

### IDEA-C-0072
- **One-sentence idea:** Build a text-only baseline audit for referring segmentation: how often is the mask predictable without looking at the image?
- **Problem:** Referring-expression datasets contain language priors ("the sky", "the left man") that let models score without genuine cross-modal grounding.
- **Core Hypothesis (falsifiable):** A model given only the text (plus dataset-level mask statistics) achieves a nontrivial fraction of reported referring-segmentation performance, and per-sample text-predictability correlates with where published models succeed — indicating prior exploitation rather than grounding.
- **Why Important:** Cleans the evidence base for a subfield whose central claim is cross-modal grounding.
- **Why Possibly Novel:** Language-prior audits exist for VQA; the dense/referring-mask analogue with per-sample analysis is not established.
- **Minimal Experiment:** Train text→mask-prior model on referring benchmarks; stratify published-model performance by text-predictability; report the grounded remainder.
- **Main Risk:** Defining the text-only baseline's allowed knowledge (image size? typical layouts?) needs care to avoid straw-manning either direction.

### IDEA-C-0073
- **One-sentence idea:** Test whether the missing granularity in VLM grounding is phrase-level: word- and sentence-level alignment exist, phrase-to-region binding does not.
- **Problem:** Dense VLM failures are described as "weak alignment", but alignment may be strong at the wrong linguistic granularity.
- **Core Hypothesis (falsifiable):** Probes show high word-level and sentence-level image alignment but near-chance phrase-to-region binding (e.g., "red cup left of book" → correct region) in contrastively trained VLMs; models with explicit region supervision show a discontinuous jump specifically at phrase level.
- **Why Important:** Localizes the representational deficit, telling method designers exactly which alignment level needs new supervision.
- **Why Possibly Novel:** Granularity-resolved alignment probing (word/phrase/sentence × global/region/pixel) as a systematic matrix has not been reported.
- **Minimal Experiment:** Construct the granularity×spatial-level probing matrix on 4 VLMs using controlled scenes; locate the deficit cell(s).
- **Main Risk:** Probe design may leak shortcuts; use swap-controls at every level.

### IDEA-C-0074
- **One-sentence idea:** Characterize the size-dependent dilation/erosion bias of VLM attention/similarity maps used as pseudo-masks.
- **Problem:** Attention-derived pseudo-masks systematically overshoot small objects and undershoot large ones (or vice versa), injecting structured bias into downstream weakly-supervised training.
- **Core Hypothesis (falsifiable):** The signed boundary offset of similarity-map pseudo-masks is a smooth monotone function of object scale (per model), and correcting with the fitted per-scale offset improves downstream weak supervision more than global threshold tuning.
- **Why Important:** Pseudo-mask pipelines inherit this bias invisibly; a measurable bias law makes it correctable.
- **Why Possibly Novel:** Threshold sensitivity is known; a *scale-conditional signed bias law* with downstream correction is not.
- **Minimal Experiment:** Measure signed offsets vs object scale across 3 VLMs on labeled data; fit correction; retrain a weakly-supervised segmenter with corrected pseudo-masks.
- **Main Risk:** Bias may depend on class and context, not just scale; check residual structure.

### IDEA-C-0075
- **One-sentence idea:** Determine where cross-modal fusion becomes necessary for localization by ablating interaction depth in a controlled two-tower→fusion continuum.
- **Problem:** Two-tower VLMs are efficient but assumed weak at localization; the necessary depth/placement of cross-modal interaction has not been isolated.
- **Core Hypothesis (falsifiable):** For referring/dense tasks, a single late fusion layer recovers most of the gap to deep-fusion models, but only if it operates at high spatial resolution — resolution of interaction, not depth, is the binding factor.
- **Why Important:** Would let efficient two-tower models serve dense tasks with a minimal, principled modification.
- **Why Possibly Novel:** Depth-of-fusion ablations exist; separating interaction *depth* from interaction *resolution* as competing explanations is untested.
- **Minimal Experiment:** Train a fusion-continuum model family (interaction layer position × feature resolution at interaction) at fixed compute; map the performance surface.
- **Main Risk:** Compute-fair comparison across the continuum is nontrivial; needs strict FLOP accounting.

### IDEA-C-0076
- **One-sentence idea:** Show that report-supervised medical VLMs align to reporting style — including pervasive negations — and that negation breaks their dense grounding.
- **Problem:** Radiology reports frequently assert absence ("no consolidation"); contrastive alignment on such text may create pathological associations between absence-words and normal anatomy.
- **Core Hypothesis (falsifiable):** In report-pretrained medical VLMs, similarity maps for "no X" prompts activate the same regions as "X" prompts (negation blindness), and the degree of blindness predicts failure of the model's pseudo-mask quality on pathology classes with high negation frequency in reports.
- **Why Important:** Negation is not an edge case in clinical text; if it corrupts grounding, medical VLM supervision needs restructuring.
- **Why Possibly Novel:** Negation blindness is known for general CLIP retrieval; its dense/grounding consequence in *medical* report-trained models, tied to report negation statistics, is unexamined.
- **Minimal Experiment:** Compare similarity maps for affirmed vs negated findings on labeled CXR data; correlate per-class blindness with negation frequency in public report corpora.
- **Main Risk:** Public report-image data is limited; MIMIC-CXR class coverage constrains generality.

### IDEA-C-0077
- **One-sentence idea:** Test whether patch-text similarity is dominated by texture rather than shape using cue-conflict stimuli for VLMs.
- **Problem:** Dense open-vocab prediction requires shape-respecting features; if patch-text similarity tracks texture, boundaries will systematically follow texture edges instead of object contours.
- **Core Hypothesis (falsifiable):** On texture-shape cue-conflict images, VLM patch-text similarity assigns regions by texture at a rate significantly above shape assignment, exceeding the texture bias of supervised segmentation networks — and this bias predicts real boundary errors at material transitions.
- **Why Important:** A quantified texture bias in VLM dense readouts would explain a class of boundary failures and motivate shape-aware alignment objectives.
- **Why Possibly Novel:** Texture-vs-shape bias is established for classifiers; the dense, patch-level VLM variant with links to real boundary errors is new.
- **Minimal Experiment:** Cue-conflict silhouettes with swapped textures; measure patch-level assignment rates across VLMs; correlate with boundary error on natural images at texture transitions.
- **Main Risk:** Cue-conflict stimuli are unnatural; the natural-image correlation step is essential to avoid over-claiming.

### IDEA-C-0078
- **One-sentence idea:** Test whether decoders trained on frozen CLIP features learn to *invert* the alignment direction — actively removing text-aligned components to recover spatial detail.
- **Problem:** Frozen-VLM segmentation pipelines work better than raw similarity readouts; what the trained decoder actually does to the features is unknown.
- **Core Hypothesis (falsifiable):** The decoder's learned input transformation systematically down-projects the directions most aligned with text embeddings (measurable via projection analysis), and constraining the decoder to preserve those directions reproduces the raw-readout failures — proving decoders succeed by undoing alignment.
- **Why Important:** If decoders fight the alignment, the pipeline is self-contradictory, motivating feature surgery before decoding rather than heavier decoders.
- **Why Possibly Novel:** Mechanistic analysis of what dense decoders do to frozen VLM features has not been reported.
- **Minimal Experiment:** Train linear/light decoders on frozen CLIP; compute alignment of suppressed vs amplified subspaces with text-embedding span; run the constrained-decoder control.
- **Main Risk:** Subspace analyses can be basis-dependent; use multiple decompositions (PCA, CCA against text space).

### IDEA-C-0079
- **One-sentence idea:** Test the single-scalar hypothesis: contrastive temperature during VLM training controls downstream localization sharpness.
- **Problem:** Temperature shapes the softness of the contrastive distribution and hence how much intra-image discrimination the model must retain — a possibly dominant, cheap-to-vary factor for dense usability.
- **Core Hypothesis (falsifiable):** VLMs trained identically except for temperature show monotone differences in patch-level discriminability and zero-shot segmentation quality, with an optimal dense-task temperature distinctly lower than the retrieval-optimal one.
- **Why Important:** One scalar at pretraining time could partially reconcile the alignment-localization conflict — the cheapest possible intervention.
- **Why Possibly Novel:** Temperature is studied for retrieval performance; its causal effect on dense usability is unmeasured.
- **Minimal Experiment:** Small-scale CLIP training sweep over temperature (5 values, fixed data/compute); evaluate retrieval and dense readout quality per checkpoint.
- **Main Risk:** Small-scale training may not reproduce large-scale temperature dynamics; state scale limits clearly.

### IDEA-C-0080
- **One-sentence idea:** Predict open-vocab segmentation confusion structure from caption co-occurrence graphs: classes that co-occur in captions cannot be separated at boundaries.
- **Problem:** VLM segmenters blur boundaries between habitually co-mentioned classes (rider/bicycle, sea/beach); this may be a direct imprint of caption statistics.
- **Core Hypothesis (falsifiable):** Pairwise boundary confusion between classes in VLM-based segmenters is predicted by caption co-occurrence PMI (controlling for visual similarity), and pretraining with co-occurrence-decorrelated captions measurably reduces exactly those confusions.
- **Why Important:** Establishes a data-statistics→error-structure causal chain, enabling targeted data fixes instead of blind scaling.
- **Why Possibly Novel:** Co-occurrence is blamed informally; a quantitative confusion-prediction model plus an interventional data experiment is new.
- **Minimal Experiment:** Compute PMI from public caption corpora; regress benchmark boundary-confusion matrices on PMI; run a small interventional pretraining with rebalanced captions.
- **Main Risk:** Visual similarity control is hard; use supervised-model confusion as the visual-similarity covariate.

### IDEA-C-0081
- **One-sentence idea:** Re-evaluate zero-shot semantic segmentation per-class to test whether "open-vocabulary generalization" is carried by a handful of frequent classes.
- **Problem:** Mean IoU aggregates hide whether rare/unseen-class performance is meaningfully above trivial baselines.
- **Core Hypothesis (falsifiable):** For current open-vocab segmenters, removing the top-quartile most caption-frequent classes drops mean performance to near trivial-baseline levels, implying negligible true generalization to genuinely rare vocabulary.
- **Why Important:** The field's headline capability claim rests on aggregate numbers; a per-class audit either grounds or corrects it.
- **Why Possibly Novel:** Frequency-stratified audits of dense zero-shot claims (with trivial-baseline anchoring) are not standard and largely unreported.
- **Minimal Experiment:** Stratify 3 benchmarks by caption frequency; evaluate 5 methods per stratum against prior-based trivial baselines.
- **Main Risk:** Caption-frequency estimates are corpus-dependent; use two corpora and report agreement.

### IDEA-C-0082
- **One-sentence idea:** Benchmark structured spatial-language instructions ("the second lesion from the apex") to test whether VLM segmenters can bind order, count, and anatomy.
- **Problem:** Clinical instructions are structured and referential; current dense VLMs are tested only on categorical or simple referring phrases.
- **Core Hypothesis (falsifiable):** On a benchmark of ordinal/counting/anatomy-relative expressions with unambiguous ground truth, current language-driven segmenters perform at or near chance, while their categorical performance on the same images is high — a specific compositional deficit, not a vision deficit.
- **Why Important:** Defines the concrete capability gap between demo-level and clinically usable language-driven segmentation.
- **Why Possibly Novel:** Ordinal/counting grounding for *dense* outputs has no dedicated benchmark or systematic measurement.
- **Minimal Experiment:** Build 500-item structured-expression set on public lesion datasets; evaluate 4 systems; report per-construction accuracy.
- **Main Risk:** Ground-truth for ordinal references requires careful, unambiguous construction rules.

### IDEA-C-0083
- **One-sentence idea:** Measure radial performance bias in dense VLM predictions induced by position-embedding interpolation from low-res pretraining.
- **Problem:** VLMs pretrained at 224px are deployed at higher resolutions via position-embedding interpolation; the resulting spatial distortion field and its dense-task cost are uncharacterized.
- **Core Hypothesis (falsifiable):** Dense-task error increases systematically with distance from image center (or another spatial pattern determined by the interpolation scheme), the bias grows with the train/test resolution ratio, and 2D-aware re-parameterization of position embeddings flattens it.
- **Why Important:** A predictable spatial error field means benchmark results depend on where objects sit — an unrecognized confound.
- **Why Possibly Novel:** Interpolation is treated as solved plumbing; its spatially-resolved error signature has not been mapped.
- **Minimal Experiment:** Evaluate frozen-VLM segmenters at 2–4× pretraining resolution; compute error-vs-position fields; compare interpolation schemes.
- **Main Risk:** Object-location statistics in benchmarks are non-uniform; use position-controlled synthetic overlays for confirmation.

### IDEA-C-0084
- **One-sentence idea:** Measure the complementarity of self-supervised (DINO-like) and language-aligned features for dense tasks via oracle-fusion bounds.
- **Problem:** The community argues SSL vs VLM features for dense prediction; whether their *errors* are complementary (fusion-worthy) or redundant is unquantified.
- **Core Hypothesis (falsifiable):** Per-pixel error overlap between SSL-feature and VLM-feature segmenters is far below chance-overlap expectation, and an oracle switching between them bounds ≥X points of headroom — quantifying (before any method-building) whether fusion research is worth pursuing.
- **Why Important:** Oracle bounds decide investment: if errors are redundant, fusion papers chase noise.
- **Why Possibly Novel:** Error-overlap/oracle analysis between these two feature families for dense tasks has not been published.
- **Minimal Experiment:** Same decoder on DINOv2 vs CLIP features across 4 dense tasks; per-pixel error correlation and oracle-fusion bound computation.
- **Main Risk:** Oracle bounds overestimate realizable gains; frame strictly as upper bounds.

### IDEA-C-0085
- **One-sentence idea:** Test whether alignment training destroys instance discrimination — making VLM features class-separable but instance-blind, breaking panoptic use.
- **Problem:** Open-vocab panoptic methods struggle to separate same-class instances; the deficit may be a direct consequence of class-level contrastive alignment.
- **Core Hypothesis (falsifiable):** Within-class instance discriminability of patch features (can a probe tell instance A from B?) is significantly lower in VLMs than in SSL models of matched scale, and the deficit predicts instance-merging errors of downstream panoptic heads.
- **Why Important:** Identifies a representational ceiling for VLM-based panoptic/instance segmentation that decoders cannot fix.
- **Why Possibly Novel:** Class-separability of VLM features is celebrated; their instance-level information content is unmeasured.
- **Minimal Experiment:** Instance-discrimination probes on multi-instance images across VLM/SSL models; correlate probe scores with panoptic instance-merge error rates.
- **Main Risk:** Instance info may exist nonlinearly; use probes of graded capacity.

### IDEA-C-0086
- **One-sentence idea:** Test a data-centric law: caption spatial density (distinct region-word bindings per image) in pretraining predicts downstream grounding quality.
- **Problem:** Grounding improvements are attributed to architectures while the underlying data property — how many regions captions actually describe — is unmeasured and uncontrolled.
- **Core Hypothesis (falsifiable):** At fixed data scale and architecture, pretraining on caption subsets stratified by region-binding density yields monotonically better dense grounding, with effect size exceeding typical architecture deltas.
- **Why Important:** Would redirect grounding effort to measurable data curation with predictable returns.
- **Why Possibly Novel:** Caption *density* (not caption length or quality) as the controlled variable in a causal pretraining experiment is new.
- **Minimal Experiment:** Estimate binding density on a public corpus (via a grounding model as annotator), create matched-scale strata, train small VLMs per stratum, evaluate dense grounding.
- **Main Risk:** Density estimation uses a model, risking circularity; validate the annotator on gold grounding data first.

### IDEA-C-0087
- **One-sentence idea:** Stress-test grounding of quantified and qualified expressions ("small nodule", "multiple opacities") in medical VLMs.
- **Problem:** Clinical language routinely qualifies size and multiplicity; whether medical VLMs bind qualifiers to correct regions is unknown.
- **Core Hypothesis (falsifiable):** Medical VLM similarity maps are invariant to size/multiplicity qualifiers (maps for "small X" ≈ "large X" even when both variants exist in the image), demonstrating qualifier-blindness measurable as map divergence below a null threshold.
- **Why Important:** Qualifier-blind grounding produces clinically wrong retrievals and pseudo-labels while looking plausible.
- **Why Possibly Novel:** Systematic qualifier-sensitivity measurement for dense medical grounding has not been reported.
- **Minimal Experiment:** Images containing both small and large instances of a finding; compare qualifier-conditioned similarity maps against instance-size ground truth.
- **Main Risk:** Few public datasets have per-instance size labels; may need semi-automatic construction with radiologist spot-checks.

### IDEA-C-0088
- **One-sentence idea:** Test whether subword fragmentation of rare medical terms breaks text-side alignment, and whether vocabulary surgery repairs dense grounding.
- **Problem:** Medical terms ("pneumoperitoneum") fragment into meaningless subwords in general tokenizers; the text embedding may fail before vision is even consulted.
- **Core Hypothesis (falsifiable):** Grounding quality per medical term correlates with its tokenization fragmentation (token count / semantic coherence of pieces), and adding whole-word embeddings (initialized from definition text) for the worst terms improves their dense grounding without retraining the vision tower.
- **Why Important:** A text-side, training-light fix for a systematic failure affecting exactly the rare terminology medicine cares about.
- **Why Possibly Novel:** Tokenization effects are studied in NLP; their propagation into *dense visual grounding* and the vocabulary-surgery remedy are untested.
- **Minimal Experiment:** Rank medical terms by fragmentation; measure grounding vs fragmentation; run vocabulary-surgery intervention on bottom decile.
- **Main Risk:** Fragmentation correlates with term rarity in pretraining; disentangle via matched-frequency term pairs.

### IDEA-C-0089
- **One-sentence idea:** Test the "latent localization" hypothesis: VLMs contain unused boundary information recoverable by lightweight probes but invisible to zero-shot readouts.
- **Problem:** Zero-shot dense readouts may understate what VLMs know; the gap between contained and expressed spatial information is unmeasured.
- **Core Hypothesis (falsifiable):** Linear probes on frozen VLM patch features predict boundary presence/orientation far above the zero-shot similarity readout's implicit boundary quality, and the probe-vs-readout gap quantifies recoverable headroom that correlates with gains from readout-improvement methods.
- **Why Important:** Separates "the information isn't there" from "the readout is bad" — the two call for entirely different research programs.
- **Why Possibly Novel:** Probing for boundary geometry (not class identity) in VLM features, framed as an information-vs-readout audit, is new.
- **Minimal Experiment:** Boundary-orientation probes on frozen features across layers; compare against zero-shot readout boundary quality; validate headroom against published readout-fix methods.
- **Main Risk:** Probe capacity must be strictly controlled to keep the "contained information" claim honest.

### IDEA-C-0090
- **One-sentence idea:** Decompose what text prompts actually do in dense VLM prediction: prior shift vs evidence integration.
- **Problem:** Changing the prompt changes the mask, but it is unknown whether prompts act as Bayesian priors (rescaling class propensities) or genuinely alter per-pixel evidence processing.
- **Core Hypothesis (falsifiable):** For frozen-VLM segmenters, prompt changes are almost fully reproducible by a per-class scalar reweighting of fixed per-pixel scores (prior-shift model, R²>0.9); departures from the prior-shift model localize to few classes/regions, identifying where prompts carry real evidence.
- **Why Important:** If prompts are just priors, prompt engineering for dense tasks is calibration in disguise — better done explicitly and safely.
- **Why Possibly Novel:** The prior-vs-likelihood decomposition of prompt effects in dense prediction has not been formalized or measured.
- **Minimal Experiment:** Fit the scalar-reweighting model across prompt families on 3 benchmarks; quantify residuals and their spatial structure.
- **Main Risk:** Interaction effects between prompts and image content may be modest but real; report effect sizes, not just model fit.

---

## C4. Prompt learning pathologies (IDEA-C-0091 … 0118)

### IDEA-C-0091
- **One-sentence idea:** Show that learned soft prompts are dataset fingerprints: the training dataset is identifiable from the prompt vector alone.
- **Problem:** CoOp-style prompts are interpreted as "task semantics", but they may primarily encode dataset-specific statistics (style, class priors, acquisition quirks).
- **Core Hypothesis (falsifiable):** A classifier over learned prompt vectors identifies the source dataset with high accuracy even across matched-task datasets (same classes, different collection), and the fingerprint strength anti-correlates with the prompt's cross-dataset transfer.
- **Why Important:** If prompts are fingerprints, prompt reuse across sites is unsafe and reported "generalizable prompts" claims need re-reading.
- **Why Possibly Novel:** Prompts have been probed for word-similarity, not for dataset-identity information content.
- **Minimal Experiment:** Train prompts on 6 dataset pairs with shared label spaces; train dataset-ID classifier on prompt vectors; correlate ID-accuracy with transfer drop.
- **Main Risk:** Few matched-task dataset pairs exist; may need constructed splits with documented differences.

### IDEA-C-0092
- **One-sentence idea:** Demonstrate that under class imbalance, prompt learning converges to encoding class-frequency priors rather than class semantics.
- **Problem:** Prompt vectors have tiny capacity; the cheapest loss reduction under imbalance is prior-matching, which silently replaces semantic learning.
- **Core Hypothesis (falsifiable):** On imbalanced datasets, ablating the learned prompt to a fitted bias-only logit adjustment reproduces most of its gain; on balanced datasets it does not — quantifying how much of prompt learning is prior-fitting as a function of imbalance.
- **Why Important:** Many reported prompt-learning gains on realistic (imbalanced) data may be re-derivable by one-line logit adjustment.
- **Why Possibly Novel:** The equivalence test between learned prompts and explicit prior-correction has not been run.
- **Minimal Experiment:** Imbalance-ratio sweep; compare CoOp vs zero-shot+logit-adjustment at each ratio; report the explained fraction.
- **Main Risk:** Prompts may fit priors *and* semantics jointly; decomposition needs the balanced-data control to anchor.

### IDEA-C-0093
- **One-sentence idea:** Audit the "nearest-word interpretation" of soft prompts and establish an honest interpretability protocol.
- **Problem:** Papers interpret learned prompts by nearest vocabulary neighbors, but soft vectors live off the token manifold and nearest words may be meaningless decorations.
- **Core Hypothesis (falsifiable):** Replacing learned prompt vectors with their nearest-word projections collapses performance toward zero-shot levels, and nearest-word identity is unstable across seeds achieving identical accuracy — jointly demonstrating that nearest-word stories are not explanations.
- **Why Important:** Cleans up a widespread interpretive malpractice and forces better tools.
- **Why Possibly Novel:** The two-pronged falsification (projection-collapse + seed-instability) has not been applied systematically.
- **Minimal Experiment:** 10 tasks × 5 seeds: measure projection performance drop and cross-seed nearest-word agreement; propose function-space (not token-space) prompt comparison as the protocol.
- **Main Risk:** Some prompts may genuinely sit near meaningful tokens; report the distribution, not a universal claim.

### IDEA-C-0094
- **One-sentence idea:** Run a seed-variance meta-analysis of prompt-learning literature: how many reported gains exceed seed noise?
- **Problem:** Prompt tuning has few parameters but high optimization variance; papers report single-seed or best-seed numbers on few-shot splits.
- **Core Hypothesis (falsifiable):** Re-running representative prompt-learning methods with ≥10 seeds and multiple few-shot draws shows that a substantial fraction of published between-method gaps fall inside the joint seed+split noise band.
- **Why Important:** If method rankings are noise, the subfield's guidance to practitioners is unreliable.
- **Why Possibly Novel:** Rigorous variance accounting (seed × split × hyperparameter) for the prompt-learning benchmark canon has not been published.
- **Minimal Experiment:** 5 canonical methods × 11 datasets × 10 seeds × 5 few-shot draws with authors' code; hierarchical variance decomposition.
- **Main Risk:** Compute-heavy though individually cheap runs; prioritize the most-cited comparisons.

### IDEA-C-0095
- **One-sentence idea:** Test whether the celebrated base-new class trade-off in prompt learning is a regularization artifact rather than a generalization property.
- **Problem:** Base-class gains vs new-class drops are theorized as overfitting-to-seen-classes; but simple regularization knobs (early stopping, weight decay to zero-shot) may trace the same trade-off curve.
- **Core Hypothesis (falsifiable):** The base-new frontier of specialized methods is matched by vanilla CoOp with a single regularization strength swept — implying published "solutions" move along, not above, an easily accessible curve.
- **Why Important:** Deflates or validates a large branch of prompt-learning method development with one controlled sweep.
- **Why Possibly Novel:** Frontier-equivalence testing (methods vs one-knob baseline) has not been performed for base-new claims.
- **Minimal Experiment:** Sweep regularization-to-zero-shot strength for vanilla prompts; overlay published methods' (base, new) points against the swept frontier.
- **Main Risk:** Some methods may genuinely exceed the frontier; the experiment is decisive either way but must tune the baseline honestly.

### IDEA-C-0096
- **One-sentence idea:** Map the prompt-length scaling curve and test for a sharp capacity phase transition.
- **Problem:** Prompt length is set by convention (4–16 tokens) without understanding whether it acts as smooth capacity or exhibits thresholds tied to task structure.
- **Core Hypothesis (falsifiable):** Accuracy vs prompt length shows a task-dependent knee at a length predictable from the number of class-discriminative attributes (estimated independently), beyond which added tokens contribute only optimization noise.
- **Why Important:** Turns an arbitrary hyperparameter into a measurable quantity tied to task structure.
- **Why Possibly Novel:** Length ablations exist as single curves; a predictive theory of the knee's location does not.
- **Minimal Experiment:** Length sweeps (1–64) across tasks with independently estimated attribute complexity; test knee-location prediction.
- **Main Risk:** "Attribute complexity" estimation is soft; use multiple operationalizations.

### IDEA-C-0097
- **One-sentence idea:** Quantify how much prompt tuning exploits the template distribution of CLIP's pretraining captions rather than task semantics.
- **Problem:** CLIP saw specific caption syntax ("a photo of a…"); learned prompts may succeed partly by regressing toward high-density caption manifolds.
- **Core Hypothesis (falsifiable):** Learned prompt embeddings move measurably toward the pretraining caption-embedding density (estimable from public corpora), and constraining prompts away from that manifold costs accuracy even at fixed norm — evidencing template-manifold exploitation.
- **Why Important:** Explains prompt fragility across text encoders and grounds prompt transfer failures in data statistics.
- **Why Possibly Novel:** The caption-manifold-attraction hypothesis has not been formulated or tested.
- **Minimal Experiment:** Estimate caption-embedding density from LAION text; track prompt trajectory density during training; run manifold-constrained control training.
- **Main Risk:** Density estimation in embedding space is delicate; use multiple estimators (kNN distance, normalizing flows).

### IDEA-C-0098
- **One-sentence idea:** Test whether pixel-space visual prompts work by perturbing normalization statistics rather than by injecting semantics.
- **Problem:** Visual prompting (learned border/patch perturbations) reports surprising gains with an unclear mechanism.
- **Core Hypothesis (falsifiable):** Matching only the induced shift in per-layer activation statistics (via norm-parameter adjustment, no pixel prompt) reproduces the majority of visual-prompt gains; residual gains concentrate in tasks with spatially structured prompts — splitting the mechanism into statistics-shift + spatial-injection components.
- **Why Important:** Mechanism clarity decides whether visual prompting is a real interface or an obfuscated normalization trick.
- **Why Possibly Novel:** No published decomposition separates the statistical from the spatial function of visual prompts.
- **Minimal Experiment:** For each visual-prompt result, fit the norm-matched control; report explained fraction per task; analyze residual spatial structure.
- **Main Risk:** Activation-statistic matching is approximate; verify with layer-wise distributional distances.

### IDEA-C-0099
- **One-sentence idea:** Detect shortcut capture in medical prompt tuning: prompts that encode acquisition-context cues ("portable radiograph" implies ICU implies disease prior).
- **Problem:** Medical image-text models embed acquisition context that correlates with outcomes; prompt tuning may lock onto these shortcuts invisibly.
- **Core Hypothesis (falsifiable):** Prompts tuned on medical classification shift the decision boundary along acquisition-context directions (measurable by counterfactual context edits changing predictions more than pathology edits), and context-stratified evaluation shows the gains vanish within strata.
- **Why Important:** Shortcut-loaded prompts would pass benchmarks and fail clinically — a certification-relevant failure.
- **Why Possibly Novel:** Shortcut analysis exists for medical CNNs; the prompt-tuning attack surface is unexamined.
- **Minimal Experiment:** Tune prompts on CXR tasks; run counterfactual context-vs-pathology sensitivity tests; stratified re-evaluation by device/position markers.
- **Main Risk:** Counterfactual context edits must be realistic; use paired natural data where possible.

### IDEA-C-0100
- **One-sentence idea:** Characterize multi-task prompt interference: co-resident prompts in one deployment degrade each other through text-encoder nonlinearity.
- **Problem:** Deployments stack prompts for many tasks/classes; whether prompt sets interact destructively via shared encoder context is unknown.
- **Core Hypothesis (falsifiable):** Accuracy of a prompt evaluated within a large prompt set (shared class-name context, softmax competition) is systematically lower than in isolation, with degradation predicted by inter-prompt embedding similarity — an interference law for prompt libraries.
- **Why Important:** Prompt libraries are the deployment reality; per-prompt papers measure a setting that does not exist in production.
- **Why Possibly Novel:** Set-context effects on prompt performance have not been isolated or modeled.
- **Minimal Experiment:** Evaluate prompts in isolation vs sets of 10/100/1000; regress degradation on pairwise similarity; test orthogonality-regularized training as mitigation.
- **Main Risk:** Softmax-set effects are partly trivial (more competitors); separate calibration effects from representational interference.

### IDEA-C-0101
- **One-sentence idea:** Test whether test-time prompt tuning is functionally equivalent to entropy minimization plus temperature calibration.
- **Problem:** TPT-style methods report zero-shot gains, but their objective (confidence maximization over augmentations) may reduce to well-known calibration adjustments.
- **Core Hypothesis (falsifiable):** A closed-form per-sample temperature/prior adjustment fitted to the same augmentation ensemble reproduces the bulk of TPT's gains at a fraction of compute; TPT's residual advantage concentrates on samples where it changes the argmax, which are disproportionately errors.
- **Why Important:** If true, an expensive test-time optimization is replaceable by an analytic step — and its residual behavior is harmful.
- **Why Possibly Novel:** The equivalence-and-residual decomposition of TPT has not been reported.
- **Minimal Experiment:** Reimplement TPT; compare with augmentation-ensemble + temperature/prior fitting; analyze argmax-changing samples separately.
- **Main Risk:** Multiple TPT variants exist; test the 2–3 most-cited to support generality.

### IDEA-C-0102
- **One-sentence idea:** Decompose prompt-ensembling gains into variance reduction vs genuine complementary information.
- **Problem:** Averaging many prompt templates helps, attributed vaguely to "diverse views"; the statistical mechanism is untested.
- **Core Hypothesis (falsifiable):** Prompt-ensemble gains are predicted by a bias-variance decomposition in logit space (gains ≈ variance reduction term), and constructed ensembles with matched variance but zero semantic diversity achieve the same gains — refuting the complementary-information story for most tasks.
- **Why Important:** Correct mechanism ⇒ correct practice: variance reduction is achievable more cheaply than template curation.
- **Why Possibly Novel:** Nobody has run the matched-variance null ensemble control.
- **Minimal Experiment:** Build semantic-diverse vs noise-matched ensembles; compare gains; verify decomposition predictions across datasets.
- **Main Risk:** Some tasks may show real complementarity; the decomposition framework should detect and localize them (a feature, not a bug).

### IDEA-C-0103
- **One-sentence idea:** Test whether gradient-optimized prompts are adversarial-like objects: high performance, near-zero robustness to embedding perturbation.
- **Problem:** Prompt optimization searches a high-dimensional continuous space with a frozen model — the same setting that produces adversarial examples.
- **Core Hypothesis (falsifiable):** Learned prompts lose disproportionately more accuracy under small random embedding perturbations than hand-written prompts matched for accuracy, and sit in measurably sharper loss regions of text-embedding space — behaving like adversarial directions rather than semantic ones.
- **Why Important:** Sharp prompts imply fragility to text-encoder updates and quantization — practical deployment hazards.
- **Why Possibly Novel:** Loss geometry of learned prompts (vs natural prompts) has not been characterized.
- **Minimal Experiment:** Perturbation-robustness curves and sharpness measures for learned vs natural prompts across tasks; test correlation with cross-encoder-version transfer.
- **Main Risk:** Norm-matching between learned and natural prompt perturbations must be careful to avoid unfair comparisons.

### IDEA-C-0104
- **One-sentence idea:** Build a transferability matrix of learned prompts across backbones and test what actually predicts transfer: architecture, size, or training data.
- **Problem:** Prompts are assumed backbone-bound, yet occasional transfer successes are reported without a predictive account.
- **Core Hypothesis (falsifiable):** Prompt transfer between VLMs correlates strongly with pretraining-data overlap (proxied by shared retrieval behavior) and weakly with architecture/scale similarity — data lineage, not architecture, determines prompt portability.
- **Why Important:** Portability rules would let prompt libraries survive model upgrades — or prove they never will.
- **Why Possibly Novel:** A systematic cross-model prompt-transfer study with lineage covariates does not exist.
- **Minimal Experiment:** 6 VLMs (varying data/architecture) × 8 tasks; full transfer matrix; regress transfer on lineage vs architecture covariates.
- **Main Risk:** Data lineage of proprietary models is opaque; restrict to models with documented corpora.

### IDEA-C-0105
- **One-sentence idea:** Measure whether input-conditional prompts actually condition: effective conditioning may collapse to an unconditional prompt plus small noise.
- **Problem:** Conditional prompt methods (meta-nets generating prompts per image) claim adaptive behavior; the realized conditioning strength is unmeasured.
- **Core Hypothesis (falsifiable):** For trained conditional-prompt models, the variance of generated prompts across inputs explains little of their output variance (ablating conditioning to the mean prompt changes accuracy marginally), except on tasks with explicit context shift — quantifying when conditioning is real.
- **Why Important:** If conditioning is cosmetic, simpler unconditional methods should be preferred and the "adaptive" narrative retired.
- **Why Possibly Novel:** Conditioning-strength audits of these architectures have not been published.
- **Minimal Experiment:** Mean-prompt ablation plus prompt-variance analysis on the canonical conditional-prompt models across their own benchmarks.
- **Main Risk:** Conditioning may matter only on rare samples; report tail-focused metrics, not just means.

### IDEA-C-0106
- **One-sentence idea:** Test whether a single global prompt is structurally unable to encode spatial priors, and where per-region prompting phase-transitions dense performance.
- **Problem:** Prompt tuning for dense tasks uses one prompt per class; spatially varying priors (organ location, laterality) cannot fit in a global vector.
- **Core Hypothesis (falsifiable):** Dense-task gains from prompts saturate at a low ceiling with global prompts, and introducing coarse spatial prompt maps (k×k grids of prompts) produces a discontinuous improvement precisely on classes with strong location priors — measurable as an interaction between prompt-spatiality and class location-entropy.
- **Why Important:** Diagnoses a structural limit of the dominant prompting interface for segmentation.
- **Why Possibly Novel:** Spatially indexed prompt capacity as the binding constraint has not been isolated.
- **Minimal Experiment:** Global vs 2×2 vs 4×4 prompt grids on organ segmentation; per-class gains vs location-entropy; test the predicted interaction.
- **Main Risk:** Spatial prompts add parameters; include parameter-matched non-spatial controls.

### IDEA-C-0107
- **One-sentence idea:** Test whether task arithmetic works in prompt space: are prompt deltas composable, low-rank, and transferable like weight-space task vectors?
- **Problem:** Task-vector arithmetic is established for weights; whether the far smaller prompt space supports analogous algebra is unknown and practically valuable.
- **Core Hypothesis (falsifiable):** Prompt deltas for related tasks combine additively (compositional accuracy within a small margin of jointly trained prompts) if and only if their text-encoder Jacobians commute approximately — giving a testable condition for prompt algebra validity.
- **Why Important:** Composable prompts would enable zero-training task mixing in deployed VLM systems.
- **Why Possibly Novel:** Task arithmetic has not been formulated or conditioned in prompt space.
- **Minimal Experiment:** Train prompts for task pairs and their unions; test additive composition; measure Jacobian commutativity as the moderator.
- **Main Risk:** Text-encoder nonlinearity may break additivity everywhere, yielding a strong null (still useful).

### IDEA-C-0108
- **One-sentence idea:** Compare calibration damage: prompt tuning vs LoRA at matched accuracy on the same VLM.
- **Problem:** Adaptation methods differ in how they warp confidence; clinical and selective-prediction use requires knowing which interface corrupts calibration least.
- **Core Hypothesis (falsifiable):** At matched target accuracy, prompt tuning distorts calibration more than LoRA (higher ECE, worse risk-coverage curves), because it operates through the softmax-competing text-embedding geometry rather than function-space updates.
- **Why Important:** Method selection guidance for risk-sensitive deployments is currently absent.
- **Why Possibly Novel:** Calibration as the primary endpoint of a prompt-vs-LoRA comparison has not been studied.
- **Minimal Experiment:** 8 tasks × {CoOp, LoRA} accuracy-matched; full uncertainty-quality battery incl. OOD inputs; mechanism check via embedding-geometry analysis.
- **Main Risk:** Accuracy matching protocol influences calibration; use several matching schemes as sensitivity analysis.

### IDEA-C-0109
- **One-sentence idea:** Test whether discrete (hard) prompt search matches soft prompts at equal compute — locating soft prompting's advantage in optimization convenience, not expressivity.
- **Problem:** Soft prompts are assumed more expressive than discrete token sequences; the comparison is never compute-fair because discrete search is under-invested.
- **Core Hypothesis (falsifiable):** With equal search compute (evolutionary/gradient-guided discrete search), hard prompts reach within a small margin of soft prompts on most classification tasks — and transfer *better* across encoder versions, reversing the practical recommendation for long-lived systems.
- **Why Important:** Hard prompts are auditable, portable, and safe to log — decisive properties for regulated settings if the accuracy cost is small.
- **Why Possibly Novel:** A compute-matched hard-vs-soft comparison with cross-version transfer as an endpoint has not been done.
- **Minimal Experiment:** Matched-compute hard vs soft prompt optimization on 10 tasks; measure accuracy and transfer to an updated encoder checkpoint.
- **Main Risk:** Discrete search implementations vary widely; use 2 search algorithms to avoid straw-manning.

### IDEA-C-0110
- **One-sentence idea:** Audit prompt-learning benchmarks for validation-set leakage: hyperparameters tuned on test-adjacent splits inflate reported gains.
- **Problem:** Few-shot prompt-learning protocols frequently tune on validation splits statistically indistinguishable from test, breaking the low-shot premise.
- **Core Hypothesis (falsifiable):** Re-running canonical methods under strict low-shot protocols (validation drawn only from the same few shots) shrinks reported gains substantially and reorders methods, with simpler methods gaining rank.
- **Why Important:** Protocol integrity determines whether the field's few-shot claims mean anything for true low-data settings.
- **Why Possibly Novel:** A systematic leakage audit of the prompt-learning evaluation canon has not been published.
- **Minimal Experiment:** 6 methods × 11 datasets under original vs strict protocols; quantify gain shrinkage and rank changes.
- **Main Risk:** Strict protocols raise variance; needs many few-shot draws for stable conclusions.

### IDEA-C-0111
- **One-sentence idea:** Show prompts memorize class-name tokens: renaming classes at test breaks tuned prompts disproportionately relative to zero-shot.
- **Problem:** Learned context prompts wrap class-name tokens; whether they build name-specific circuits (fragile) or name-independent context (robust) is unknown.
- **Core Hypothesis (falsifiable):** Substituting synonyms for class names at test time degrades tuned-prompt performance by a larger factor than zero-shot performance, demonstrating that tuning binds context to specific name tokens rather than to concepts.
- **Why Important:** Name-binding fragility breaks prompt reuse across ontologies — routine in medicine where terminologies vary by site.
- **Why Possibly Novel:** Synonym-substitution stress tests for *tuned* prompts (with zero-shot as the control) are not standard.
- **Minimal Experiment:** Synonym test sets for 8 datasets; compare degradation ratios tuned vs zero-shot; correlate with training epochs (binding dynamics).
- **Main Risk:** Synonym quality varies; validate synonym sets via human/encoder agreement checks.

### IDEA-C-0112
- **One-sentence idea:** Test whether initialization dominates method identity in prompt learning: domain-informed initialization beats method innovations at matched budgets.
- **Problem:** Methods differ simultaneously in objectives, architectures, and initializations; initialization may be the load-bearing component.
- **Core Hypothesis (falsifiable):** Across published prompt-learning methods, replacing each method's initialization with a strong domain-informed one (embedding of a curated natural-language task description) compresses between-method differences below significance — initialization explains more variance than method.
- **Why Important:** Would redirect the subfield from architecture innovation to initialization engineering, which is cheaper and more portable.
- **Why Possibly Novel:** Variance attribution across the (method × initialization) grid has not been reported.
- **Minimal Experiment:** 5 methods × 4 initializations × 8 datasets; two-way ANOVA on outcomes; report variance shares.
- **Main Risk:** Interaction effects may be real (some methods need specific inits); the factorial design captures this.

### IDEA-C-0113
- **One-sentence idea:** Document "prompt collapse": class prompts converging toward each other during long training, silently destroying fine-grained discrimination.
- **Problem:** Prompt training monitors accuracy, not the geometry of the prompt set; converging prompts would degrade exactly the confusable classes while aggregate metrics look stable.
- **Core Hypothesis (falsifiable):** Pairwise similarity among class-prompt embeddings increases with training beyond a task-dependent point, and its rise predicts (precedes) the decline of confusable-pair accuracy — establishing collapse as a monitorable pathology with an early-warning signal.
- **Why Important:** Adds a cheap training-time diagnostic preventing silent fine-grained degradation.
- **Why Possibly Novel:** Prompt-set geometry dynamics during training have not been tracked or linked to per-pair outcomes.
- **Minimal Experiment:** Long prompt training on fine-grained datasets; log prompt-similarity trajectories and per-pair accuracy; test the lead-lag relation and a similarity-penalty fix.
- **Main Risk:** Collapse may be benign reparameterization in some encoders; the per-pair accuracy linkage is the decisive test.

### IDEA-C-0114
- **One-sentence idea:** Test grounding invariance: does elaborate instruate-style prompting (reasoning-flavored text) change *where* medical VLMs look, or only what they say?
- **Problem:** Verbose reasoning prompts improve text outputs in multimodal systems; whether they alter visual evidence use for dense/grounding tasks is unknown.
- **Core Hypothesis (falsifiable):** Across prompt elaborations, the visual attribution maps (occlusion-based) of grounded predictions remain statistically unchanged while output phrasing varies — prompts modulate the language head, not visual grounding — measurable as attribution-map invariance.
- **Why Important:** If grounding is prompt-invariant, prompt engineering cannot fix localization errors, bounding a popular hope.
- **Why Possibly Novel:** Attribution-invariance testing under prompt elaboration has not been formalized for grounded medical tasks.
- **Minimal Experiment:** 5 prompt-elaboration levels on grounded report/segmentation tasks; occlusion-attribution similarity across levels vs across images (null distribution).
- **Main Risk:** Attribution methods are noisy; use two independent attribution techniques.

### IDEA-C-0115
- **One-sentence idea:** Quantify negation blindness of prompt interfaces ("not X", "without X") and identify the minimal training signal that fixes it.
- **Problem:** Contrastive text encoders famously ignore negation; prompt-based deployments inherit this silently in filters, retrieval, and pseudo-labeling.
- **Core Hypothesis (falsifiable):** Negated prompts produce embeddings within a small distance of affirmative counterparts (behavioral equivalence), and a small hard-negative fine-tune (thousands of contrastive negation pairs) fixes the metric without harming standard benchmarks — bounding the *cost* of the fix, not just documenting the flaw.
- **Why Important:** Negation handling is a gating requirement for medical language interfaces ("segment lesions, excluding calcifications").
- **Why Possibly Novel:** Documentation exists; the minimal-fix cost curve (how little data suffices) does not.
- **Minimal Experiment:** Negation behavioral battery pre/post hard-negative tuning at data budgets {1k, 10k, 100k pairs}; measure fix vs side-effect curves.
- **Main Risk:** Fixing negation may distort embedding geometry elsewhere; the side-effect battery is essential.

### IDEA-C-0116
- **One-sentence idea:** Compare noise amplification: prompt tuning vs linear probing under label noise.
- **Problem:** Few-shot data is often noisily labeled (especially medical); how the prompt interface propagates label noise relative to standard heads is unknown.
- **Core Hypothesis (falsifiable):** At matched clean-data accuracy, prompt tuning degrades faster with symmetric and class-conditional label noise than linear probing, because noisy gradients move shared text-context affecting all classes — a coupling absent in independent linear heads.
- **Why Important:** Practical guidance for the common noisy-few-shot regime, plus a mechanistic account of prompt coupling.
- **Why Possibly Novel:** Noise-robustness comparisons across adaptation interfaces (prompt vs probe vs adapter) are missing.
- **Minimal Experiment:** Noise-rate sweeps (0–40%) × {CoOp, linear probe, LoRA} on 6 datasets; degradation-slope comparison; coupling test via per-class noise injection.
- **Main Risk:** Results may vary with shots; run at 4/16/64 shots.

### IDEA-C-0117
- **One-sentence idea:** Decompose forgetting in prompt-pool continual learning: the pool doesn't forget, the query function does.
- **Problem:** Prompt-pool methods claim rehearsal-free continual learning; but the learned query-to-prompt matching is itself trained continually and may silently degrade.
- **Core Hypothesis (falsifiable):** In prompt-pool CL, end-task forgetting is dominated by query-function drift (retrieving wrong prompts for old tasks) rather than prompt-content change — demonstrable by oracle-routing evaluation which recovers most lost performance.
- **Why Important:** The field's rehearsal-free story hides where the forgetting moved; fixing the right component requires locating it.
- **Why Possibly Novel:** Oracle-routing decomposition of prompt-pool forgetting has not been reported.
- **Minimal Experiment:** Standard prompt-pool CL benchmarks; at each stage evaluate with learned vs oracle routing; attribute forgetting shares.
- **Main Risk:** Oracle routing definitions vary (task-ID vs best-prompt); report both.

### IDEA-C-0118
- **One-sentence idea:** Test provenance of textual-inversion-style medical concept prompts: do they encode pathology or scanner/site artifacts?
- **Problem:** Learning a pseudo-token for a medical concept from site-specific examples may capture acquisition fingerprints rather than the concept.
- **Core Hypothesis (falsifiable):** Concept prompts learned at site A retrieve/segment concept-positive cases at site B at rates far below within-site performance, while retrieving site-A *negative* images above chance — direct evidence the token encodes site, and a cross-site training fix restores concept transfer.
- **Why Important:** Concept tokens are being proposed for rare-finding search and labeling; provenance validity is a precondition.
- **Why Possibly Novel:** Cross-site provenance testing of learned visual-concept tokens in medicine is absent.
- **Minimal Experiment:** Learn concept tokens on single-site data; evaluate cross-site retrieval and same-site-negative retrieval; retrain with multi-site examples as the fix condition.
- **Main Risk:** Requires multi-site data with shared concept labels; a few public multi-site sets qualify.

---

## C5. Weak/semi/self-supervised segmentation: scientific gaps (IDEA-C-0119 … 0148)

### IDEA-C-0119
- **One-sentence idea:** Model pseudo-label confirmation bias as a spatial diffusion process: errors nucleate at boundaries and propagate outward at a measurable rate.
- **Problem:** Self-training error accumulation is described qualitatively; its spatial dynamics (where errors start, how fast they spread) are unmodeled.
- **Core Hypothesis (falsifiable):** Across self-training rounds, the spatial distribution of new pseudo-label errors is concentrated within a band around previous-round errors, with a stable per-round expansion rate that predicts final degradation from round-1 measurements.
- **Why Important:** A predictive error-dynamics model would let practitioners set stopping rounds and spatial filtering rules from early observations.
- **Why Possibly Novel:** Confirmation bias in segmentation self-training has no spatiotemporal quantitative model.
- **Minimal Experiment:** Instrumented self-training on 3 datasets with held-out truth; track per-round error masks; fit and validate the expansion model.
- **Main Risk:** Dynamics may differ across loss functions; replicate under CE and Dice objectives.

### IDEA-C-0120
- **One-sentence idea:** Test whether semi-supervised segmentation gains vanish when the labeled subset is chosen well, making method choice second-order to labeled-set selection.
- **Problem:** SSL-segmentation papers randomly sample labeled subsets; informed selection (coverage of appearance modes) may dwarf the method effect they study.
- **Core Hypothesis (falsifiable):** With a labeled subset selected by unsupervised coverage maximization, the supervised-only baseline closes most of the gap to state-of-the-art semi-supervised methods at 5–10% label fractions — variance explained by selection exceeds that explained by method.
- **Why Important:** If selection dominates, the field's effort allocation (new consistency losses vs data selection) is inverted.
- **Why Possibly Novel:** Head-to-head variance attribution between selection policy and semi-supervised method is missing.
- **Minimal Experiment:** {random, coverage-selected} × {supervised-only, 2 SSL methods} on 3 benchmarks; two-way analysis of gains.
- **Main Risk:** Coverage selection needs unlabeled features; use generic SSL features to avoid circularity.

### IDEA-C-0121
- **One-sentence idea:** Test whether consistency regularization works via implicit boundary smoothing rather than the cluster assumption it cites.
- **Problem:** The mechanism of consistency training in segmentation is asserted (decision boundaries in low-density regions) but never separated from a mundane alternative: averaging over perturbations smooths predicted boundaries.
- **Core Hypothesis (falsifiable):** Replacing consistency training with explicit boundary-smoothing regularization (no unlabeled data) reproduces a large fraction of its gains on standard benchmarks; the residual unlabeled-data benefit concentrates on images whose appearance is far from labeled examples — separating smoothing from information gain.
- **Why Important:** Correct mechanism changes what unlabeled data is worth collecting and how methods should be built.
- **Why Possibly Novel:** The smoothing-equivalence control experiment has not been run for dense consistency methods.
- **Minimal Experiment:** Match consistency methods against label-only smoothing controls; stratify residual gains by appearance distance to labeled set.
- **Main Risk:** Designing a fair smoothing control requires care (strength matching via boundary-jitter statistics).

### IDEA-C-0122
- **One-sentence idea:** Establish a placement law for scribble supervision: performance is predicted by scribble distance-to-boundary statistics, not scribble quantity.
- **Problem:** Scribble-supervised methods are compared on fixed scribble sets, confounding annotation geometry with method quality.
- **Core Hypothesis (falsifiable):** Across datasets and methods, segmentation quality is a stable function of the scribble set's distance-to-boundary distribution (near-boundary scribbles are worth several× interior ones per pixel), enabling annotation protocols optimized by the law.
- **Why Important:** Annotation budget rules grounded in a validated law would change how scribble data is collected everywhere.
- **Why Possibly Novel:** Scribble geometry as the controlled variable (rather than method) has not been systematically studied.
- **Minimal Experiment:** Synthetic scribble generators sweeping distance-to-boundary distributions on 3 datasets × 2 methods; fit and cross-validate the law.
- **Main Risk:** Interaction with structure size may complicate a single law; model it explicitly.

### IDEA-C-0123
- **One-sentence idea:** Build a taxonomy of CAM-hard classes: image-level weak supervision fails predictably for classes defined by absence, texture, or extent.
- **Problem:** Class-activation-based weak segmentation is evaluated in aggregate; which class *types* it structurally cannot localize is undocumented.
- **Core Hypothesis (falsifiable):** Classes whose evidence is (a) absence of structure, (b) global texture change, or (c) spatial extent rather than presence, show CAM localization near chance regardless of classifier accuracy — and the taxonomy predicts failure on unseen datasets from class descriptions alone.
- **Why Important:** Medical findings frequently fall in exactly these types (atrophy, diffuse disease); users need to know weak supervision cannot start there.
- **Why Possibly Novel:** CAM failure anecdotes exist; a predictive class-type taxonomy validated across datasets does not.
- **Minimal Experiment:** Categorize classes across 6 datasets by evidence type; measure CAM localization per type; test out-of-sample prediction of the taxonomy.
- **Main Risk:** Class-type annotation is subjective; use multiple raters and report agreement.

### IDEA-C-0124
- **One-sentence idea:** Show that self-training converges toward a single annotator style, collapsing the inter-rater variance present in the initial labels.
- **Problem:** Pseudo-labels are generated by a model trained on multi-rater-influenced data; iterating may systematically homogenize label style, losing calibrated ambiguity.
- **Core Hypothesis (falsifiable):** Across self-training rounds, the distributional spread of predictions on ambiguous regions (where raters disagree) shrinks monotonically toward one mode, and the final model's rater-likelihood is high for one rater and low for others — measurable style collapse absent in the supervised baseline.
- **Why Important:** Semi-supervised pipelines may silently discard exactly the ambiguity information medicine needs to keep.
- **Why Possibly Novel:** Interaction between self-training dynamics and multi-rater label structure is unstudied.
- **Minimal Experiment:** Multi-rater dataset; run self-training; track per-round prediction spread on disagreement regions and per-rater likelihoods.
- **Main Risk:** Requires multi-rater ground truth; several public sets (prostate, lung nodule) qualify.

### IDEA-C-0125
- **One-sentence idea:** Locate where SSL-pretraining gains for segmentation actually live: encoder representation vs training dynamics (initialization effects on optimization).
- **Problem:** MAE/DINO pretraining improves segmentation, attributed to "better features"; but gains may come from optimization benefits (better-conditioned initialization) that vanish with longer schedules.
- **Core Hypothesis (falsifiable):** With sufficiently long, well-tuned downstream training, the gap between SSL-pretrained and random-init encoders shrinks substantially on large labeled sets but persists on small ones — and frozen-feature probes show the persistent part is representational while the vanishing part is dynamical.
- **Why Important:** Correct attribution determines whether the field should invest in pretraining or in downstream optimization for label-rich domains.
- **Why Possibly Novel:** The dynamics-vs-representation decomposition with schedule-controlled experiments is rarely done for dense tasks.
- **Minimal Experiment:** {SSL-init, random-init} × {short, 5× long schedules} × {small, large labeled sets}; frozen-probe analysis alongside.
- **Main Risk:** "Sufficiently long" is expensive; bound with compute-matched analysis.

### IDEA-C-0126
- **One-sentence idea:** Break semi-supervised segmentation with realistic unlabeled pools: measure the OOD-contamination rate at which methods fall below supervised-only.
- **Problem:** Benchmarks draw unlabeled data from the same distribution as labeled; real unlabeled pools contain other anatomy, protocols, and artifacts.
- **Core Hypothesis (falsifiable):** Standard semi-supervised methods degrade below the supervised-only baseline at modest contamination rates (10–30% out-of-task images), with degradation driven by confident-wrong pseudo-labels on OOD inputs — and a simple unlabeled-data filter restores robustness.
- **Why Important:** Defines the operating envelope of semi-supervised segmentation for real deployments where curation is imperfect.
- **Why Possibly Novel:** Contamination dose-response curves for dense SSL are essentially unreported.
- **Minimal Experiment:** Contamination sweeps (0–50%) with controlled OOD types × 3 methods; identify breakdown thresholds and test filtering.
- **Main Risk:** OOD-type choice affects thresholds; use 3 contamination families (other anatomy, other modality, corrupted).

### IDEA-C-0127
- **One-sentence idea:** Show that the "low-data regime" simulated by subsampling big datasets misrepresents true small-cohort learning, breaking method rankings.
- **Problem:** Papers simulate scarcity as 5% of a large dataset — preserving class coverage and appearance diversity that genuine small cohorts lack.
- **Core Hypothesis (falsifiable):** Method rankings established on subsampled-scarcity benchmarks reorder significantly on true small cohorts (single-site, consecutive patients), because subsampling preserves diversity that specific methods exploit — measurable as a ranking-correlation breakdown.
- **Why Important:** The field's low-data conclusions guide exactly the users (small clinics, rare diseases) that the evaluation misrepresents.
- **Why Possibly Novel:** Direct subsampled-vs-genuine scarcity comparisons with ranking analysis are missing.
- **Minimal Experiment:** Match label counts between subsampled large datasets and genuinely small cohorts; run 5 methods; compare rankings and interaction structure.
- **Main Risk:** Genuine small cohorts differ in many ways; use several to average over idiosyncrasies.

### IDEA-C-0128
- **One-sentence idea:** Demonstrate that report-derived weak labels carry *correlated* noise that violates the independence assumptions of noisy-label learning methods.
- **Problem:** Text-mined labels inherit reporting biases (satisfaction of search, protocol-driven attention) producing errors correlated with patient context — while noisy-label methods assume (class-)conditional independence.
- **Core Hypothesis (falsifiable):** Error patterns of report-derived labels are predictable from context covariates (view, department, report length) far above chance, and noisy-label methods built on independence assumptions underperform simple context-stratified reweighting on such data.
- **Why Important:** Most large medical weak-label corpora are report-derived; using mismatched noise models corrupts everything downstream.
- **Why Possibly Novel:** The correlated-noise structure of report-mined labels has not been measured or exploited.
- **Minimal Experiment:** Audit label errors against expert re-reads on a public report-labeled set; model error-context dependence; compare noise-handling methods.
- **Main Risk:** Expert re-reads are costly; sample-efficient stratified auditing needed.

### IDEA-C-0129
- **One-sentence idea:** Test whether anatomical plausibility of mixing augmentations matters: CutMix across incompatible anatomy vs anatomy-aware mixing in semi-supervised medical segmentation.
- **Problem:** Mixing augmentations create anatomically impossible images; the community assumes networks don't care, without direct evidence in dense medical tasks.
- **Core Hypothesis (falsifiable):** At matched mixing rates, anatomy-preserving mixing (swaps between corresponding regions) and naive CutMix produce equal in-domain gains, but naive mixing degrades OOD robustness and boundary calibration — the implausibility cost appears off-distribution, explaining why in-domain benchmarks miss it.
- **Why Important:** Augmentation design in medical SSL rests on this untested assumption.
- **Why Possibly Novel:** The in-domain-vs-OOD split of augmentation-plausibility effects is a new measurement target.
- **Minimal Experiment:** {naive, anatomy-aware} mixing × 2 SSL methods; evaluate in-domain, cross-site, and boundary calibration.
- **Main Risk:** Anatomy-aware mixing implementations vary; keep the mechanism minimal (registered-region swaps).

### IDEA-C-0130
- **One-sentence idea:** Build an early-detection metric for entropy-minimization class collapse in unbalanced segmentation.
- **Problem:** Entropy-based objectives silently drive minority classes to extinction; collapse is discovered only at final evaluation.
- **Core Hypothesis (falsifiable):** The per-class trajectory of predicted-pixel share exhibits a detectable inflection (accelerating decline) several hundred steps before minority-class Dice collapses, yielding an online alarm with high precision/recall against ground-truth collapses.
- **Why Important:** Deployable safeguard for the most common failure of confidence-based semi-supervised training.
- **Why Possibly Novel:** Collapse is known; a validated online early-warning statistic is not.
- **Minimal Experiment:** Instrument entropy-min training across imbalance levels; label collapse events; evaluate alarm lead time and error rates.
- **Main Risk:** Alarms tuned on some datasets may misfire on others; cross-dataset validation is required.

### IDEA-C-0131
- **One-sentence idea:** Derive and test a rule linking mean-teacher EMA rate to dataset size and label fraction, replacing the universal 0.999 default.
- **Problem:** The teacher momentum default is inherited across papers regardless of setting; its interaction with data scale is unexamined.
- **Core Hypothesis (falsifiable):** The optimal EMA rate varies systematically with labeled-set size and epoch length (effective updates per epoch), following a predictable relation; using the fitted rule beats the default by a margin comparable to recent method innovations.
- **Why Important:** A free hyperparameter rule with method-scale impact would recalibrate baseline strength across the literature.
- **Why Possibly Novel:** EMA-rate scaling relations for dense SSL have not been characterized.
- **Minimal Experiment:** EMA-rate grids across {3 datasets × 3 label fractions}; fit the relation; validate on 2 held-out settings.
- **Main Risk:** The relation may be architecture-dependent; verify on CNN and transformer backbones.

### IDEA-C-0132
- **One-sentence idea:** Quantify the positional shortcut in pixel-level contrastive SSL on spatially registered medical images.
- **Problem:** Medical volumes are roughly aligned; pixel contrastive objectives can minimize loss by encoding position rather than appearance semantics.
- **Core Hypothesis (falsifiable):** Features from pixel-contrastive SSL on registered data predict spatial coordinates far better than appearance-matched controls, and their downstream transfer drops disproportionately on unregistered/abnormal cases — with registration-breaking augmentation closing both gaps.
- **Why Important:** A silent shortcut in the standard recipe for medical dense SSL would explain fragile transfer to pathological anatomy.
- **Why Possibly Novel:** The registration-induced positional shortcut has not been isolated or dosed.
- **Minimal Experiment:** Train pixel-contrastive SSL with/without registration-breaking transforms; probe features for coordinates; compare transfer on aligned vs distorted anatomy.
- **Main Risk:** Position and anatomy are inherently correlated; the dose-response design (graded registration breaking) addresses this.

### IDEA-C-0133
- **One-sentence idea:** Audit baseline inflation in semi-supervised segmentation: how much of reported gains disappear against supervised baselines with modern augmentation and schedules?
- **Problem:** SSL methods are compared to supervised baselines trained with the *method's* budget but dated recipes, inflating apparent unlabeled-data value.
- **Core Hypothesis (falsifiable):** Upgrading supervised-only baselines (augmentation, longer schedules, tuned regularization) at matched compute absorbs a large share of reported semi-supervised gains across canonical benchmarks, and the surviving gains concentrate at the lowest label fractions.
- **Why Important:** Establishes the *real* value of unlabeled data — the number practitioners actually need.
- **Why Possibly Novel:** Compute-matched baseline-modernization audits exist for classification, not for dense medical SSL benchmarks.
- **Minimal Experiment:** Reproduce 4 canonical comparisons; upgrade baselines under equal compute; report surviving gain by label fraction.
- **Main Risk:** "Modern recipe" choices could be accused of cherry-picking; pre-register the baseline recipe.

### IDEA-C-0134
- **One-sentence idea:** Prove the necessity of per-class dynamic pseudo-label thresholds: fixed confidence cutoffs freeze minority-class recall by construction.
- **Problem:** Global confidence thresholds select easy majority-class pixels; the resulting training distribution locks minority classes out of the self-training loop.
- **Core Hypothesis (falsifiable):** Under fixed thresholds, minority-class pseudo-label inclusion rate stays near zero across rounds regardless of true model competence (verifiable with oracle labels), while per-class quantile thresholds restore inclusion and final recall — the failure is mechanical, not representational.
- **Why Important:** A mechanical failure mode implies a mandatory protocol change, not an optional trick.
- **Why Possibly Novel:** The oracle-verified "mechanical lockout" framing distinguishes this from existing adaptive-threshold papers that only report end metrics.
- **Minimal Experiment:** Instrument inclusion rates and oracle-verified competence per class per round under fixed vs quantile thresholds.
- **Main Risk:** Quantile thresholds admit noisier labels; measure the noise-inclusion trade-off explicitly.

### IDEA-C-0135
- **One-sentence idea:** Estimate an empirical information bound: how much boundary accuracy is achievable in principle from image-level labels alone?
- **Problem:** Weakly supervised segmentation chases boundary quality without knowing whether the supervision even contains the necessary information.
- **Core Hypothesis (falsifiable):** Boundary accuracy achievable from image-level supervision saturates at a level predictable from class-evidence localization statistics (how spatially concentrated the class evidence is), and current methods already operate near that ceiling for concentrated-evidence classes — meaning further gains require different supervision, not better methods.
- **Why Important:** Distinguishes method-limited from information-limited regimes, preventing wasted effort.
- **Why Possibly Novel:** Empirical supervision-information ceilings for weak segmentation have not been estimated.
- **Minimal Experiment:** Train oracle-assisted estimators (upper-bound probes given image labels + features) across class types; compare current methods against the estimated ceilings.
- **Main Risk:** Ceiling estimation is itself model-limited; report as lower bounds on the true ceiling with convergence checks.

### IDEA-C-0136
- **One-sentence idea:** Measure whether augmentation-constructed "views" satisfy co-training's independence requirement — and how view correlation caps gains.
- **Problem:** Co-training theory requires conditionally independent views; deep SSL replaces them with augmentations of one image, correlation unquantified.
- **Core Hypothesis (falsifiable):** The error-correlation between co-trained heads on shared inputs predicts the method's gain across settings (higher correlation, lower gain) with a threshold above which co-training adds nothing — connecting practice back to the theory it invokes.
- **Why Important:** Provides a measurable design criterion (decorrelate views) instead of blind augmentation stacking.
- **Why Possibly Novel:** View-correlation as a quantitative moderator of co-training gains in dense tasks is untested.
- **Minimal Experiment:** Vary view construction (augmentation families, modalities, feature dropouts); measure error correlation and gains; fit the moderation curve.
- **Main Risk:** Error correlation is outcome-entangled; use held-out probe tasks for the correlation measurement.

### IDEA-C-0137
- **One-sentence idea:** Show that "barely-supervised" (one labeled volume) segmentation success is carried by implicit registration, and collapses on unregistered anatomy.
- **Problem:** Single-volume supervision methods report strong results on well-aligned datasets (cardiac, abdominal atlases); the role of implicit spatial alignment is unacknowledged.
- **Core Hypothesis (falsifiable):** Performance of barely-supervised methods degrades toward failure as test-time anatomical alignment with the labeled volume decreases (measured by registration residual), while many-label baselines degrade far less — alignment, not method ingenuity, is the active ingredient.
- **Why Important:** Corrects the perceived readiness of extreme-low-label methods for pathological, poorly aligned real-world anatomy.
- **Why Possibly Novel:** Alignment-stratified evaluation of barely-supervised claims has not been reported.
- **Minimal Experiment:** Stratify test cases by registration residual to the labeled volume; compare degradation slopes across supervision levels.
- **Main Risk:** Registration residual is imperfectly measurable on pathological cases — use multiple registration methods.

### IDEA-C-0138
- **One-sentence idea:** Measure scanner-fingerprint content of medical SSL features and its causal effect on cross-site generalization.
- **Problem:** SSL objectives reward any discriminative signal, including scanner/site fingerprints irrelevant or harmful for anatomy tasks.
- **Core Hypothesis (falsifiable):** Scanner identity is linearly decodable from medical SSL features at high accuracy; adversarially removing that subspace at probe time costs little in-domain but improves cross-site transfer — establishing fingerprints as causal baggage, not benign correlates.
- **Why Important:** Pretraining data pooling across sites is standard; knowing it bakes in fingerprints (and that they're removable) changes pipeline design.
- **Why Possibly Novel:** Fingerprint decoding exists for supervised nets; the SSL-pretraining version with causal-removal testing does not.
- **Minimal Experiment:** SSL on pooled multi-site data; scanner probes; subspace-removal intervention; in-domain vs cross-site evaluation.
- **Main Risk:** Fingerprint and anatomy-relevant signal may share subspaces; graded removal quantifies the entanglement.

### IDEA-C-0139
- **One-sentence idea:** Audit click-model realism in interactive segmentation: simulated user clicks used in training/evaluation diverge from real clinician behavior.
- **Problem:** Interactive methods are trained and ranked with synthetic click policies (center-of-error clicks); real users click by different, unrecorded heuristics.
- **Core Hypothesis (falsifiable):** Real-clinician click distributions differ measurably from standard simulators (location relative to boundaries/errors, timing/ordering), and method rankings under real clicks differ from simulator rankings — the simulator is a wrong instrument for the leaderboard it powers.
- **Why Important:** The entire interactive-segmentation evaluation stack rests on click simulators nobody has validated.
- **Why Possibly Novel:** Human-click datasets and simulator-validity analysis for medical interactive segmentation are essentially nonexistent.
- **Minimal Experiment:** Collect real click logs from a small clinician study on public data; compare distributions to simulators; re-rank 4 methods under replayed real clicks.
- **Main Risk:** Small human studies have limited coverage; focus on ranking-stability claims rather than absolute numbers.

### IDEA-C-0140
- **One-sentence idea:** Quantify the boundary bias that superpixel-based weak supervision inherits from its superpixel algorithm.
- **Problem:** Superpixels are used to propagate sparse labels; their boundary adherence characteristics (color-edge preference, compactness priors) imprint on the learned model unexamined.
- **Core Hypothesis (falsifiable):** Models trained with superpixel-propagated labels reproduce the superpixel algorithm's signature boundary errors (measurable as correlation between superpixel-boundary error fields and model-boundary error fields on held-out truth), and switching superpixel algorithms transfers the corresponding signature.
- **Why Important:** An inherited, correctable bias in a widely used weak-supervision pipeline should be documented and dosed.
- **Why Possibly Novel:** Bias inheritance from label-propagation machinery has not been isolated as an object of study.
- **Minimal Experiment:** Train with labels propagated by 3 superpixel algorithms; compare model error fields against each algorithm's known bias pattern.
- **Main Risk:** Model training may partially wash out the bias; the cross-algorithm signature transfer is the decisive test.

### IDEA-C-0141
- **One-sentence idea:** Run a bake-off: model uncertainty estimates vs a trivial distance-to-boundary heuristic for weighting pseudo-labels.
- **Problem:** Sophisticated uncertainty machinery (MC dropout, ensembles) is used to weight pseudo-labels, but boundary distance may capture most of the usable signal at zero cost.
- **Core Hypothesis (falsifiable):** For pseudo-label weighting in segmentation self-training, the signed-distance-to-predicted-boundary heuristic matches or exceeds MC-dropout and matches ensembles within noise on final performance — implying current uncertainty use is an expensive proxy for geometry.
- **Why Important:** Removes a costly component from standard pipelines, or proves its worth properly for the first time.
- **Why Possibly Novel:** The trivial-geometric-control comparison is absent from the uncertainty-weighted self-training literature.
- **Minimal Experiment:** {distance heuristic, MC dropout, deep ensemble, softmax entropy} as weighting schemes × 3 datasets; matched budgets; final-metric comparison.
- **Main Risk:** Interaction with calibration quality may vary by architecture; include two backbones.

### IDEA-C-0142
- **One-sentence idea:** Test whether simple temporal label propagation beats sophisticated consistency losses for semi-supervised segmentation of temporal medical data.
- **Problem:** For video/4D data (echo, cine-MR), papers apply generic image-based SSL machinery while the temporal structure offers near-free supervision via propagation.
- **Core Hypothesis (falsifiable):** Registration/tracking-based label propagation from sparse labeled frames outperforms state-of-the-art consistency-based SSL at equal label budgets on temporal medical benchmarks — structure exploitation beats generic regularization where structure exists.
- **Why Important:** Redirects effort in temporal medical SSL toward the exploitable physics of the data.
- **Why Possibly Novel:** Direct head-to-head of propagation vs modern consistency SSL at matched budgets is missing.
- **Minimal Experiment:** Echo/cine benchmarks; label 1 frame per sequence; compare propagation, consistency-SSL, and their union.
- **Main Risk:** Propagation fails under large motion/topology change; report stratified by motion magnitude.

### IDEA-C-0143
- **One-sentence idea:** Test whether label-efficient methods change the slope or only the intercept of the labeled-data learning curve.
- **Problem:** Methods claim to "reduce annotation needs by N×", implying slope changes, but most evaluations report isolated points, not curves.
- **Core Hypothesis (falsifiable):** Fitting power-law learning curves across label fractions shows that semi/weak/self-supervised methods shift the intercept (constant multiplier) but leave the exponent statistically unchanged — implying their advantage shrinks at scale and "N× savings" claims are point-estimate artifacts.
- **Why Important:** The slope-vs-intercept distinction determines whether label-efficiency methods matter for well-funded projects or only tiny ones.
- **Why Possibly Novel:** Learning-curve-exponent analysis is standard in scaling literature but unapplied to label-efficiency claims in segmentation.
- **Minimal Experiment:** 4 methods × 6 label fractions × 3 datasets; fit curves; test exponent equality statistically.
- **Main Risk:** Curve fitting needs many points at low fractions where variance is high; use repeated draws.

### IDEA-C-0144
- **One-sentence idea:** Measure gradient conflict between dense (pixel-level) and global (image-level) SSL objectives when combined, and its downstream cost.
- **Problem:** Modern recipes sum dense and global self-supervised losses assuming synergy; the objectives may compete for representation capacity.
- **Core Hypothesis (falsifiable):** Gradient cosine between dense and global SSL objectives is systematically negative in mid-to-late layers, and the conflict magnitude predicts which downstream task family (dense vs global) the combined model sacrifices — enabling principled loss balancing per intended use.
- **Why Important:** Recipe design currently ignores an internal competition that may explain inconsistent transfer results.
- **Why Possibly Novel:** Inter-objective gradient-conflict analysis within SSL combinations is unreported.
- **Minimal Experiment:** Instrument combined SSL training; log per-layer gradient conflict; correlate with downstream dense/global transfer across balancing weights.
- **Main Risk:** Gradient cosine is a coarse conflict measure; corroborate with interpolation-based interference tests.

### IDEA-C-0145
- **One-sentence idea:** Re-evaluate active learning for segmentation under a standardized, empirically grounded annotation-cost model.
- **Problem:** Region-based AL papers count "labeled regions" or pixels, using cost accounting that ignores real annotation-time structure (setup, navigation, boundary tracing time).
- **Core Hypothesis (falsifiable):** Under a time-based cost model fitted to real annotation sessions, the ranking of acquisition strategies changes substantially, and several published region-AL gains reverse sign — the gains were artifacts of the cost metric, not the acquisition intelligence.
- **Why Important:** AL guidance directly allocates expensive clinician time; the wrong cost model wastes exactly what it claims to save.
- **Why Possibly Novel:** Fitted time-cost re-evaluation of the segmentation-AL literature has not been performed.
- **Minimal Experiment:** Fit a cost model from a small timed annotation study; re-simulate published AL comparisons under it; report ranking changes.
- **Main Risk:** Cost models vary by tool/anatomy; publish the model and sensitivity analysis alongside.

### IDEA-C-0146
- **One-sentence idea:** Quantify the damage of treating unannotated organs as background in partially labeled datasets, and validate the positive-unlabeled correction.
- **Problem:** Multi-source medical training pools datasets with different labeled organ subsets; absent labels are silently treated as negatives, teaching systematic suppression.
- **Core Hypothesis (falsifiable):** Models trained on pooled partial labels show organ-specific sensitivity deficits proportional to how often each organ appears unannotated in the pool, and a positive-unlabeled loss correction recovers most of the deficit — a quantitative dose-response law of annotation missingness.
- **Why Important:** Pooling partially labeled data is the field's main scaling strategy; its central artifact deserves a law, not anecdotes.
- **Why Possibly Novel:** The dose-response formulation (deficit vs missingness rate) with PU-correction validation is new for this setting.
- **Minimal Experiment:** Construct pools with controlled missingness rates per organ; measure sensitivity deficits; apply PU losses; fit the law.
- **Main Risk:** Organ difficulty confounds missingness effects; use within-organ missingness manipulation.

### IDEA-C-0147
- **One-sentence idea:** Probe whether medical SSL features encode anatomical invariants (bilateral symmetry, topology, ordering) or only local texture statistics.
- **Problem:** SSL is claimed to learn "anatomy"; what structural knowledge the features actually contain is untested at the level of anatomical laws.
- **Core Hypothesis (falsifiable):** Probes for anatomical invariants (left-right correspondence, superior-inferior ordering, organ adjacency) perform near chance on standard medical SSL features while local-texture probes excel — SSL learns appearance, not anatomy — and adding cheap invariant-supervision closes specific probe gaps.
- **Why Important:** Grounds or deflates the "anatomical foundation model" narrative with direct measurements.
- **Why Possibly Novel:** Anatomical-invariant probing batteries do not exist.
- **Minimal Experiment:** Build the probe battery on labeled anatomy; evaluate 4 SSL models; run the invariant-supervision intervention on one.
- **Main Risk:** Probe design may under-elicit nonlinear knowledge; include graded-capacity probes.

### IDEA-C-0148
- **One-sentence idea:** Adjudicate why EMA teachers beat their students: temporal ensembling as implicit flat-minima search vs noise averaging.
- **Problem:** The teacher-exceeds-student phenomenon is universal in mean-teacher SSL but unexplained; two candidate mechanisms make different predictions.
- **Core Hypothesis (falsifiable):** If flatness is the mechanism, teacher advantage correlates with sharpness gap and survives label-noise-free settings; if noise-averaging, the advantage vanishes with full-batch training and clean labels — the 2×2 experiment (noise × batch regime) separates them.
- **Why Important:** The mechanism dictates when to trust the teacher (deployment choice) and how to design better averaging schemes.
- **Why Possibly Novel:** Mechanistic adjudication of the teacher-student gap has not been done for dense prediction.
- **Minimal Experiment:** Mean-teacher training across the 2×2 design; measure teacher-student gaps, sharpness, and prediction-noise statistics.
- **Main Risk:** Mechanisms may coexist with setting-dependent weights; the design quantifies their shares rather than forcing a binary.

---

## C6. Medical vision foundation models: what they still cannot do (IDEA-C-0149 … 0178)

### IDEA-C-0149
- **One-sentence idea:** Run a clinical-safety probe for laterality: can medical foundation models reliably represent left vs right?
- **Problem:** Wrong-side errors are "never events" clinically; whether FM representations distinguish laterality (beyond image-flip statistics) is unverified.
- **Core Hypothesis (falsifiable):** Probes for anatomical laterality on FM features perform well on canonical orientations but collapse under flipped or marker-removed images — the models encode orientation conventions, not laterality — measurable as a flip-consistency failure rate.
- **Why Important:** Laterality is a minimal bar for clinical text generation, retrieval, and reporting built on FM features.
- **Why Possibly Novel:** Laterality has not been treated as a standalone capability audit for medical FMs.
- **Minimal Experiment:** Laterality probes on {canonical, flipped, marker-ablated} images across 4 FMs; report consistency matrices.
- **Main Risk:** Datasets embed laterality markers; careful ablation of burned-in annotations is required.

### IDEA-C-0150
- **One-sentence idea:** Measure the pairwise-reasoning gap: FMs cannot compare two scans (change detection) even when they analyze each well individually.
- **Problem:** Longitudinal comparison is a core radiology act; FM architectures and pretraining see single images, and their comparison ability is untested.
- **Core Hypothesis (falsifiable):** On controlled change-detection tasks (synthetic and registered-pair real data), FM-based pipelines perform near chance for changes below a large magnitude, while trivially trained siamese baselines succeed — a structural, not scale, deficiency.
- **Why Important:** Defines a capability boundary directly blocking the most common clinical use case (interval change).
- **Why Possibly Novel:** Change-detection audits of medical FMs with controlled magnitude ladders do not exist.
- **Minimal Experiment:** Construct change ladders (lesion growth steps) on registered pairs; evaluate FM zero/few-shot vs small siamese supervised baseline.
- **Main Risk:** Registration errors mimic change; use synthetic insertions with verified realism as the controlled arm.

### IDEA-C-0151
- **One-sentence idea:** Test whether FMs lost metric scale: physical-size estimation fails because pretraining pipelines discard pixel spacing.
- **Problem:** Clinical decisions hinge on millimeters, but FM preprocessing resizes images, destroying the mapping between pixels and physical units.
- **Core Hypothesis (falsifiable):** FM features cannot support size estimation beyond relative-within-image judgments (probes fail to predict physical size across images with varying spacing), and injecting spacing as a side input at probe time restores accuracy — the information is destroyed, not unused.
- **Why Important:** Measurement is half of radiology; a metric-blind foundation cannot support it.
- **Why Possibly Novel:** Metric-scale capability audits for medical FMs are absent.
- **Minimal Experiment:** Physical-size probes across mixed-spacing datasets with/without spacing injection; compare against spacing-aware baselines.
- **Main Risk:** Some anatomy provides internal scale references; control by cross-anatomy evaluation.

### IDEA-C-0152
- **One-sentence idea:** Fit the prevalence-performance power law for medical FMs and locate the rare-disease floor.
- **Problem:** FM marketing implies coverage of the long tail; the quantitative relation between condition prevalence in pretraining and downstream capability is unmeasured.
- **Core Hypothesis (falsifiable):** Zero/few-shot performance across conditions follows a power law in estimated pretraining prevalence with a floor at effective-chance for conditions below a threshold prevalence — the floor's location quantifies the tail FMs actually cover.
- **Why Important:** Tells rare-disease researchers whether FMs are a starting point or a distraction.
- **Why Possibly Novel:** Prevalence-conditioned capability curves for medical FMs have not been published.
- **Minimal Experiment:** Estimate condition frequencies in public pretraining corpora; evaluate FMs across a prevalence-spanning condition set; fit the law.
- **Main Risk:** Prevalence estimation in opaque corpora is rough; use rank-based analyses robust to estimation error.

### IDEA-C-0153
- **One-sentence idea:** Prove where 3D context is necessary by slice-shuffling controls: which tasks do 2D-slice FMs solve without true volumetric reasoning?
- **Problem:** 2D FMs applied slice-wise score well on 3D benchmarks, obscuring whether volumetric context matters and where.
- **Core Hypothesis (falsifiable):** For a defined subset of tasks (e.g., structures defined by cross-slice continuity), performance collapses when inter-slice order is shuffled at inference, while for most benchmark-dominant tasks it does not — partitioning benchmarks into genuinely-3D and effectively-2D components.
- **Why Important:** Clarifies what 3D-native architectures must justify themselves on, and cleans up misleading benchmark aggregates.
- **Why Possibly Novel:** Order-destruction controls as a benchmark-partitioning instrument are not in use.
- **Minimal Experiment:** Slice-shuffle and slice-reverse interventions across 6 volumetric tasks; classify tasks by degradation.
- **Main Risk:** Shuffling may break trivial stitching heuristics rather than reasoning; add graded local shuffles.

### IDEA-C-0154
- **One-sentence idea:** Test cross-modality patient identity: can FMs recognize that a CT and MR belong to the same anatomy/patient?
- **Problem:** Multimodal patient reasoning requires modality-invariant anatomical representation; FM feature spaces may be modality-partitioned.
- **Core Hypothesis (falsifiable):** Cross-modality patient-matching from FM embeddings performs near chance without paired fine-tuning, while within-modality matching is nearly perfect — the representation is modality-first, anatomy-second, quantifiable as a matching-gap ratio.
- **Why Important:** Bounds current FMs' usefulness for multimodal fusion, retrieval, and longitudinal multimodal records.
- **Why Possibly Novel:** Cross-modality identity as an FM capability metric is unproposed.
- **Minimal Experiment:** Paired CT/MR public datasets; embedding-based matching within and across modalities across 4 FMs.
- **Main Risk:** Paired public data is scarce; registration-derived pseudo-pairs can extend coverage.

### IDEA-C-0155
- **One-sentence idea:** Enumerate the counting deficit: FM-based pipelines fail structure counting (ribs, vertebrae, lesions) beyond small numbers.
- **Problem:** Counting requires individuation and enumeration — capabilities plausibly absent from representation-centric pretraining — yet clinical tasks (rib fractures, metastasis counts) demand them.
- **Core Hypothesis (falsifiable):** FM zero/few-shot counting accuracy decays sharply with true count (near chance beyond ~4), errors follow individuation failures (merged/repeated instances) rather than detection misses, and scale (bigger FMs) does not repair the decay curve's shape.
- **Why Important:** Counting is a discrete capability gap that scaling narratives claim will close; a shape-invariant deficit would refute that.
- **Why Possibly Novel:** Count-stratified error decomposition for medical FMs does not exist.
- **Minimal Experiment:** Counting battery across count ranges on public data; error typology (merge/repeat/miss); scale comparison across FM sizes.
- **Main Risk:** Prompting/readout choices affect counting; use several readout protocols to isolate the representational claim.

### IDEA-C-0156
- **One-sentence idea:** Audit demographic shortcut leakage: FM embeddings encode age/sex/race and inject them into downstream clinical predictions.
- **Problem:** FMs trained on hospital archives encode demographics; downstream fine-tunes may silently convert them into shortcut features with fairness and validity consequences.
- **Core Hypothesis (falsifiable):** Demographics are decodable from FM embeddings at high accuracy; downstream task heads use those directions (ablating them changes predictions differentially by subgroup); and shortcut usage grows when task labels correlate with demographics in the fine-tuning set — a measurable causal pathway, not just correlation.
- **Why Important:** Regulatory and ethical stakes are high, and the FM layer centralizes the risk across every downstream application.
- **Why Possibly Novel:** Demographic decodability is known for specific supervised models; the FM-as-shortcut-carrier causal chain is unestablished.
- **Minimal Experiment:** Decode demographics from 4 FMs; subspace-ablation intervention on downstream tasks; correlation-manipulated fine-tuning sets to test the growth prediction.
- **Main Risk:** Subspace ablation may remove legitimate clinical signal correlated with demographics; report the trade-off surface honestly.

### IDEA-C-0157
- **One-sentence idea:** Build an OOD-pathology stress suite showing medical FMs are overconfident precisely on findings absent from pretraining.
- **Problem:** FM uncertainty behavior on truly novel pathology (rare presentations, new devices, post-surgical anatomy) is the deployment-relevant unknown.
- **Core Hypothesis (falsifiable):** On curated never-seen-category cases, FM-based classifiers/segmenters produce confidence indistinguishable from in-distribution cases (AUROC of confidence-based OOD detection near 0.5), and this failure is worse than in supervised task-specific models trained with standard augmentation.
- **Why Important:** "Foundation" implies breadth; unflagged novelty is the failure mode breadth claims hide.
- **Why Possibly Novel:** OOD-confidence audits specific to *pathology novelty* (not modality shift) are missing for medical FMs.
- **Minimal Experiment:** Assemble novelty suite from public rare-finding cases; measure confidence separability across FMs vs supervised baselines.
- **Main Risk:** "Never-seen" is unverifiable for opaque corpora; use post-cutoff or synthetic-but-validated findings.

### IDEA-C-0158
- **One-sentence idea:** Chart the device-confusion matrix: FMs conflate medical devices (tubes, implants, leads) with pathology and vice versa.
- **Problem:** ICU and post-operative images are full of devices; FM behavior on device-pathology disambiguation is anecdotal.
- **Core Hypothesis (falsifiable):** FM zero/few-shot predictions show systematic device-pathology confusions (device presence raises pathology scores beyond the true correlation in labels), and confusion strength tracks device-pathology co-occurrence in pretraining-like corpora — a data-imprint signature.
- **Why Important:** Device-rich patients are the sickest patients; confusions there are maximally harmful.
- **Why Possibly Novel:** A quantitative device-pathology confusion audit with data-statistics attribution is not available.
- **Minimal Experiment:** Device-annotated public CXR sets; measure score shifts under device presence at fixed pathology; compare against label co-occurrence.
- **Main Risk:** True clinical correlation between devices and disease exists; the comparison against label-level correlation is the essential control.

### IDEA-C-0159
- **One-sentence idea:** Perform dataset archaeology: FM performance decays with acquisition-era gap between pretraining and deployment data.
- **Problem:** Imaging technology drifts (detectors, reconstruction kernels, dose protocols); FM robustness to temporal protocol drift is unmeasured.
- **Core Hypothesis (falsifiable):** Holding task fixed, FM performance on era-stratified test data declines with temporal distance from the pretraining corpus's era distribution, at a rate exceeding supervised models trained on era-diverse data — quantifying an FM shelf-life.
- **Why Important:** Deployment planning needs decay rates, not snapshots; "train once" claims depend on this number.
- **Why Possibly Novel:** Era-stratified FM evaluation (acquisition-date as the axis) has not been done.
- **Minimal Experiment:** Public datasets with acquisition metadata spanning ≥10 years; era-stratified evaluation of 3 FMs vs supervised controls.
- **Main Risk:** Era confounds with institution and population; multi-source era strata mitigate this.

### IDEA-C-0160
- **One-sentence idea:** Evaluate abstention quality: medical FMs cannot say "I don't know" where it matters.
- **Problem:** Selective prediction (deferring hard cases to humans) is the realistic deployment mode, yet FM evaluation reports accuracy, not risk-coverage behavior.
- **Core Hypothesis (falsifiable):** At clinically relevant coverage levels (e.g., defer 20%), FM-based systems achieve risk reductions far below what their accuracy would suggest under calibrated confidence — and below task-specific models — because FM confidence ranks errors poorly on medical inputs.
- **Why Important:** A model that can't route its own failures to humans is unusable in safety-critical workflows regardless of average accuracy.
- **Why Possibly Novel:** Risk-coverage-first evaluation of medical FMs is not standard practice.
- **Minimal Experiment:** Risk-coverage curves for 4 FMs vs supervised baselines across 5 tasks; decompose failures into ranking vs calibration deficits.
- **Main Risk:** Confidence extraction from FMs varies by interface; standardize several extraction protocols.

### IDEA-C-0161
- **One-sentence idea:** Audit anatomical-topology violation rates in FM segmentation outputs versus task-specific models.
- **Problem:** Anatomically impossible outputs (disconnected organs, nested structures inverted) reveal absent structural priors; FM rates are unquantified.
- **Core Hypothesis (falsifiable):** Generalist FM segmenters produce topology violations at multiples of task-specific model rates, violations concentrate on low-contrast boundaries, and rates are unchanged by scale within available FM families — priors come from task specialization, not scale.
- **Why Important:** Topology violations are automatic red flags for clinical review; their prevalence measures readiness beyond Dice.
- **Why Possibly Novel:** Topology-violation auditing as an FM capability metric is unestablished.
- **Minimal Experiment:** Violation battery (connectivity, containment, adjacency) over FM vs specialist outputs on multi-organ benchmarks.
- **Main Risk:** Ground-truth topology rules need clinical validation; start with uncontroversial invariants.

### IDEA-C-0162
- **One-sentence idea:** Test whether report-supervised FMs learn the distribution of *reported* findings, systematically missing unreported incidentals.
- **Problem:** Reports document what radiologists chose to mention; findings outside the clinical question (incidentals) are under-reported, biasing FM supervision.
- **Core Hypothesis (falsifiable):** On images with expert re-reads that recover unreported findings, report-trained FMs detect reported-type findings well but miss unreported-type ones at rates predicted by reporting-frequency statistics — the model inherits the reporting policy, not the visual truth.
- **Why Important:** Incidental findings are a major clinical value proposition for AI; an FM structurally blind to them fails the pitch.
- **Why Possibly Novel:** The reported-vs-present distinction has not been operationalized as an FM evaluation axis.
- **Minimal Experiment:** Re-read a stratified image sample to establish present-but-unreported findings; measure FM sensitivity by reportedness stratum.
- **Main Risk:** Re-read cost; mitigate with targeted sampling where reporting gaps are known to concentrate.

### IDEA-C-0163
- **One-sentence idea:** Benchmark compositional pathology: FMs fail images containing co-occurring diseases whose features interact.
- **Problem:** Real patients have multiple conditions; FM evaluation is dominated by single-finding benchmarks.
- **Core Hypothesis (falsifiable):** FM detection of finding A degrades measurably in the presence of finding B (beyond occlusion/overlap geometry), with degradation predicted by the rarity of the (A,B) combination in pretraining-like corpora — compositional generalization fails where combinations are unseen.
- **Why Important:** Multi-morbidity is the norm in the sickest patients; single-finding metrics overstate readiness.
- **Why Possibly Novel:** Pairwise-interaction degradation matrices for medical FMs have not been constructed.
- **Minimal Experiment:** Multi-label datasets; estimate interaction effects on per-finding sensitivity; regress against combination frequency.
- **Main Risk:** Confounding by severity (multi-disease patients are sicker); include severity covariates.

### IDEA-C-0164
- **One-sentence idea:** Determine the effective resolution ceiling of medical FMs: which subtle findings live below what the representation can carry?
- **Problem:** Micro-findings (microcalcifications, early interstitial change) may fall below FM effective spatial bandwidth after tokenization and pooling — the field lacks a frequency-resolved capability map.
- **Core Hypothesis (falsifiable):** FM feature sensitivity to controlled high-frequency perturbations cuts off at a measurable spatial frequency per model, and clinical findings whose discriminative energy lies above the cutoff show near-chance FM performance regardless of fine-tuning — a physics-style capability bound.
- **Why Important:** Tells users which clinical problems FMs cannot address at any data budget, before they try.
- **Why Possibly Novel:** Frequency-response characterization of medical FM representations is not in the literature.
- **Minimal Experiment:** Bandpass perturbation sensitivity analysis per FM; align finding types by discriminative-frequency content; test the predicted performance cliff.
- **Main Risk:** Fine-tuning may partially reopen bandwidth; test the bound both frozen and fine-tuned.

### IDEA-C-0165
- **One-sentence idea:** Re-evaluate few-shot medical FM claims under strict patient-level, site-level splits.
- **Problem:** Few-shot medical results often use image-level splits, letting patient and site identity leak between support and query sets.
- **Core Hypothesis (falsifiable):** Under strict patient- and site-disjoint few-shot protocols, reported FM few-shot performance drops substantially, and the drop is largest for methods with the strongest published claims — leakage, not capability, differentiates current leaderboards.
- **Why Important:** Few-shot capability is the FM value proposition for rare conditions; the evidence base must survive proper splits.
- **Why Possibly Novel:** A systematic leakage-corrected re-evaluation across the medical FM few-shot canon is missing.
- **Minimal Experiment:** Re-run canonical few-shot evaluations with corrected splits across 3 FMs; quantify per-claim shrinkage.
- **Main Risk:** Some datasets lack patient identifiers; restrict to those with verifiable metadata.

### IDEA-C-0166
- **One-sentence idea:** Stress-test FMs against physics-based artifacts (motion, metal, beam hardening) versus supervised models trained with artifact augmentation.
- **Problem:** Web-scale pretraining sees curated images; clinical streams contain physics artifacts that supervised pipelines explicitly augment for.
- **Core Hypothesis (falsifiable):** Under a graded physics-artifact battery, FM performance degrades faster than artifact-augmented supervised baselines, and FM degradation is unpredictable from clean-data performance — breadth of pretraining does not substitute for physics-targeted robustness.
- **Why Important:** Artifacts are daily reality; robustness rankings on clean benchmarks may invert in practice.
- **Why Possibly Novel:** Physics-artifact dose-response comparisons FM-vs-specialist are not published.
- **Minimal Experiment:** Simulate graded artifacts with validated physics models; evaluate 3 FMs vs augmented baselines; compare degradation slopes.
- **Main Risk:** Simulated artifacts must be validated against real artifact cases to support conclusions.

### IDEA-C-0167
- **One-sentence idea:** Audit the geometry of medical FM latent spaces: modality-clustered embeddings that block unified cross-modal retrieval.
- **Problem:** Unified medical retrieval (find similar cases across CT/MR/X-ray) presumes a shared semantic space; actual FM embedding geometry may be partitioned by modality before semantics.
- **Core Hypothesis (falsifiable):** In current medical FMs, modality explains more embedding variance than diagnosis (variance decomposition), and cross-modal semantic retrieval fails below usable precision, while within-modality retrieval succeeds — the space is modality-first, quantified by a decomposition ratio that predicts retrieval behavior.
- **Why Important:** Retrieval is the most deployable FM application; its geometric precondition should be verified, not assumed.
- **Why Possibly Novel:** Variance-decomposition audits of medical FM embedding spaces are not standard.
- **Minimal Experiment:** Multi-modality labeled corpora; variance decomposition + retrieval evaluation across 4 FMs.
- **Main Risk:** Diagnosis labels are coarse; use hierarchical labels to fairly measure semantic structure.

### IDEA-C-0168
- **One-sentence idea:** Define and measure intra-scan consistency: FMs segment the same structure inconsistently across adjacent slices/frames.
- **Problem:** Slice-wise FM inference produces volumetrically incoherent outputs; the inconsistency itself is an unmeasured error source distinct from per-slice accuracy.
- **Core Hypothesis (falsifiable):** FM per-slice segmentations of the same structure vary across adjacent slices beyond anatomical change rates (measurable against smooth ground-truth interpolation), inconsistency predicts volumetry error better than per-slice Dice does, and simple temporal conditioning removes most of it.
- **Why Important:** Volumetry — the quantitative output clinicians use — is corrupted by exactly this inconsistency, invisible to standard metrics.
- **Why Possibly Novel:** Consistency-vs-accuracy decomposition for slice-wise FM inference has not been formalized.
- **Minimal Experiment:** Adjacent-slice variation statistics vs anatomical-change nulls; correlate with volumetry error; test conditioning fixes.
- **Main Risk:** Distinguishing model inconsistency from true anatomical variation requires careful null construction.

### IDEA-C-0169
- **One-sentence idea:** Measure grounded hallucination rates of vision-FM+LLM medical pipelines: fluent findings with no image evidence.
- **Problem:** Multimodal report generators produce plausible text; how often assertions lack any visual grounding — and which pipeline stage injects them — is unquantified.
- **Core Hypothesis (falsifiable):** A measurable fraction of generated positive findings have no supporting image evidence under occlusion testing (removing the referenced region leaves the assertion unchanged), and hallucination rate is dominated by the language prior (scales with finding frequency in report corpora) rather than by the vision encoder.
- **Why Important:** Grounded hallucination is the specific failure that makes generated reports dangerous rather than merely imperfect.
- **Why Possibly Novel:** Occlusion-verified hallucination attribution (vision vs language stage) has not been systematized for medical pipelines.
- **Minimal Experiment:** Occlusion-based grounding tests on generated reports; regress hallucination rates on corpus frequency; stage-swap experiments for attribution.
- **Main Risk:** Occlusion tests can miss diffuse evidence; complement with evidence-localization annotation on a subsample.

### IDEA-C-0170
- **One-sentence idea:** Detect test-set contamination in medical FM evaluations via memorization probes and near-duplicate archaeology.
- **Problem:** Medical datasets are re-packaged and re-hosted; FM pretraining corpora may contain benchmark test images, silently inflating evaluations.
- **Core Hypothesis (falsifiable):** Memorization probes (reconstruction quality, embedding-space near-duplicate detection against public benchmark tests) identify contaminated items in FM training reach, and FM performance on contaminated items exceeds matched clean items by a measurable margin — direct evidence of inflated benchmarks.
- **Why Important:** Contamination undermines every downstream comparison; medicine's small benchmark pool makes it acutely likely.
- **Why Possibly Novel:** Contamination forensics is developed for LLMs; medical-imaging FM analogues are nascent to absent.
- **Minimal Experiment:** Near-duplicate scans of benchmark test sets against declared/open pretraining corpora; contaminated-vs-clean performance comparison on matched pairs.
- **Main Risk:** Opaque corpora limit direct verification; behavioral memorization probes provide the indirect arm.

### IDEA-C-0171
- **One-sentence idea:** Quantify age-extrapolation failure: adult-pretrained FMs on pediatric imaging.
- **Problem:** Pediatric anatomy differs systematically (ossification, proportions, pathology spectrum); FM behavior under age extrapolation is anecdotal.
- **Core Hypothesis (falsifiable):** FM performance declines monotonically with distance from the adult age distribution, with failure concentrated on age-dependent structures (growth plates, thymus), and few-shot pediatric adaptation recovers less than an equivalently sized from-scratch pediatric baseline on those structures — the adult prior actively interferes.
- **Why Important:** Pediatric imaging is underserved; knowing whether adult FMs help or harm is a prerequisite for responsible use.
- **Why Possibly Novel:** Age-stratified FM audits with interference testing are unavailable.
- **Minimal Experiment:** Age-stratified evaluation on public pediatric sets; structure-level analysis; adaptation-vs-scratch comparison at matched budgets.
- **Main Risk:** Public pediatric data is limited; focus on modalities with available cohorts (pediatric CXR, bone age sets).

### IDEA-C-0172
- **One-sentence idea:** Map contrast-phase sensitivity: FM segmentation silently assumes portal-venous CT and degrades across phases.
- **Problem:** CT appearance varies drastically with contrast phase; FM training-data phase composition is unknown and its effect unmeasured.
- **Core Hypothesis (falsifiable):** FM segmentation/detection quality varies across contrast phases far more than specialist models trained phase-diversely, with a peak matching the dominant public-data phase — and phase is recoverable from FM embeddings, confirming the imprint.
- **Why Important:** Phase mismatch is a silent everyday deployment condition; a phase-sensitivity map is directly actionable.
- **Why Possibly Novel:** Phase-stratified FM evaluation has not been reported.
- **Minimal Experiment:** Multi-phase public CT sets; per-phase performance profiles for 3 FMs vs baselines; embedding-phase decoding.
- **Main Risk:** Phase labels are inconsistent in public metadata; verify with automated phase classification.

### IDEA-C-0173
- **One-sentence idea:** Measure salience suppression: FMs detect the most prominent lesion and systematically under-report additional ones.
- **Problem:** Multi-lesion sensitivity is clinically vital (staging, metastasis counts); representation-level "winner-take-most" behavior would cap it independent of thresholds.
- **Core Hypothesis (falsifiable):** Per-lesion detection probability conditioned on lesion properties drops significantly when a more salient lesion is present in the same image (versus matched single-lesion controls), the suppression strengthens with salience gap, and it persists across detection thresholds — a representational, not calibration, effect.
- **Why Important:** Missing the second lesion changes staging and treatment; aggregate sensitivity metrics hide this failure specifically.
- **Why Possibly Novel:** Conditional (context-dependent) per-lesion sensitivity analysis for FMs has not been performed.
- **Minimal Experiment:** Multi-lesion datasets plus synthetic-insertion controls; estimate conditional detection curves vs salience gap.
- **Main Risk:** Natural multi-lesion images differ in many ways; synthetic insertion provides the controlled arm and must pass realism checks.

### IDEA-C-0174
- **One-sentence idea:** Test whether multimodal fine-tuning of FMs with clinical variables actually integrates them or reduces them to output bias terms.
- **Problem:** Adding labs/demographics to image FMs claims "multimodal reasoning"; the realized computation may be an additive prior shift with no image-conditional interaction.
- **Core Hypothesis (falsifiable):** For most fine-tuned image+clinical models, predictions are reproducible by (image-only score) + (clinical-only score) with near-zero interaction terms (measured by functional ANOVA), and genuine interactions appear only with architectures forcing feature-level fusion trained on interaction-requiring tasks.
- **Why Important:** Purchasing multimodal complexity for an additive effect is waste; and clinical claims of "integrated reasoning" need verification.
- **Why Possibly Novel:** Interaction-decomposition audits of medical multimodal models are rare to nonexistent.
- **Minimal Experiment:** Functional decomposition of 4 published-style multimodal setups; synthetic interaction-requiring tasks as positive controls.
- **Main Risk:** Real tasks may genuinely lack interactions; the positive-control tasks distinguish "model can't" from "task doesn't need".

### IDEA-C-0175
- **One-sentence idea:** Quantify static-image bias of FMs on surgical/endoscopic video: failure on temporally defined events and deformable anatomy.
- **Problem:** Surgical AI needs temporal understanding (phase transitions, bleeding onset, tool-tissue interaction); image-FM features may be fundamentally static descriptors.
- **Core Hypothesis (falsifiable):** FM-feature-based models match specialist video models on appearance-defined recognition but fall to near chance on events defined only by motion patterns (with appearance controlled), and the gap is unclosed by frame-stacking inputs — temporal structure is absent from, not just unused by, the representation.
- **Why Important:** Defines whether surgical AI can build on general FMs or requires video-native pretraining.
- **Why Possibly Novel:** Appearance-controlled motion-only evaluations for FM features are not established.
- **Minimal Experiment:** Construct appearance-matched motion-defined event tasks from public surgical video; FM-feature vs video-model comparison.
- **Main Risk:** Constructing truly appearance-controlled tasks is delicate; use synthetic motion manipulation as verification.

### IDEA-C-0176
- **One-sentence idea:** Measure cross-site feature-space divergence when the same FM is fine-tuned independently at multiple sites.
- **Problem:** The "shared foundation" vision assumes site-adapted descendants remain interoperable (for federated analytics, model merging, shared downstream heads); divergence dynamics are unmeasured.
- **Core Hypothesis (falsifiable):** Independently fine-tuned FM descendants diverge in feature space at a rate driven by site-data distance, breaking cross-site head transfer after modest fine-tuning, while anchor-regularized fine-tuning preserves interoperability at negligible in-site cost — divergence is preventable but not by default.
- **Why Important:** Multi-site medical AI infrastructure implicitly depends on interoperability that nobody is checking.
- **Why Possibly Novel:** Interoperability decay of FM descendants as a measured phenomenon is new.
- **Minimal Experiment:** Fine-tune one FM at 4 simulated sites; track cross-site head-transfer and representation alignment over fine-tuning; test anchor regularization.
- **Main Risk:** Simulated sites may understate real heterogeneity; include at least one genuinely multi-site public dataset.

### IDEA-C-0177
- **One-sentence idea:** Audit the clinical-metric gap: generalist FMs match specialists on Dice while losing on the measures clinicians consume (volumetry, diameters, boundary-derived indices).
- **Problem:** Benchmark parity on overlap metrics is taken as clinical parity; derived clinical measurements weight errors differently.
- **Core Hypothesis (falsifiable):** At matched Dice, FM segmentations produce significantly larger errors in derived clinical quantities (volumes, RECIST-style diameters, wall thickness) than specialist models, because FM errors are spatially structured (boundary-biased, inconsistency-prone) in ways Dice averages away.
- **Why Important:** Adoption decisions cite Dice parity; if clinical measures diverge, those decisions are misinformed at the last mile.
- **Why Possibly Novel:** Matched-Dice comparisons on derived clinical endpoints have not been systematically reported.
- **Minimal Experiment:** Dice-matched FM/specialist output pairs; compute clinical-measure error distributions; identify the responsible error structure.
- **Main Risk:** Dice matching requires careful pairing protocols; use multiple matching schemes.

### IDEA-C-0178
- **One-sentence idea:** Map the accuracy-latency frontier for FM vs distilled task models under realistic clinical latency budgets.
- **Problem:** Clinical integration imposes hard latency/compute ceilings (intra-procedure guidance, PACS throughput); where FMs sit relative to distilled specialists on the joint frontier is undocumented.
- **Core Hypothesis (falsifiable):** For fixed clinical latency budgets, distilled task-specific models dominate FM inference on the accuracy-latency frontier across most tasks, and the FM advantage survives only in ultra-low-label regimes — quantifying exactly when FM inference (vs FM-as-teacher) is justified in production.
- **Why Important:** Separates the FM's value as a *teacher* from its value as a *deployed inference engine* — a distinction procurement decisions currently blur.
- **Why Possibly Novel:** Systematic frontier mapping with the teacher-vs-engine framing is absent from medical FM literature.
- **Minimal Experiment:** Distill 3 FMs into small task models across 5 tasks; plot joint frontiers across label budgets and latency ceilings.
- **Main Risk:** Distillation quality depends on recipes; use standardized well-tuned distillation to avoid understating FMs.

---

## C7. Object detection vs segmentation representation conflict (IDEA-C-0179 … 0204)

### IDEA-C-0179
- **One-sentence idea:** Measure the equivariance conflict: box regression rewards translation-sensitive features while mask prediction demands equivariance, and shared backbones must compromise.
- **Problem:** Multi-task det+seg models share features between objectives with opposing symmetry requirements; the compromise has never been measured as such.
- **Core Hypothesis (falsifiable):** Backbone feature equivariance (response shift under input shift) in jointly trained models sits between the values of detection-only and segmentation-only twins, and its position on that axis predicts which task the joint model sacrifices — equivariance is the contested resource.
- **Why Important:** Gives multi-task architecture design a measurable target instead of blind head balancing.
- **Why Possibly Novel:** Equivariance as the quantified locus of det/seg conflict has not been proposed or tested.
- **Minimal Experiment:** Train {det-only, seg-only, joint} triplets; measure layer-wise equivariance; correlate with per-task performance deltas.
- **Main Risk:** Equivariance metrics are implementation-sensitive; use two independent measures.

### IDEA-C-0180
- **One-sentence idea:** Decompose detection-pretraining transfer to segmentation: better object recall, worse boundary accuracy.
- **Problem:** Detection pretraining is a common segmentation initialization; its transfer is reported as a single number that may hide opposing effects.
- **Core Hypothesis (falsifiable):** Compared to classification or SSL pretraining at matched scale, detection pretraining improves object-level recall of downstream segmentation while measurably degrading boundary metrics — a signed decomposition stable across datasets.
- **Why Important:** Initialization choice should depend on whether the application is finding things or delineating them; current lore conflates the two.
- **Why Possibly Novel:** Recall-vs-boundary decomposition of pretraining transfer is not reported in the literature.
- **Minimal Experiment:** {detection, classification, SSL} pretraining × 4 segmentation datasets; report object recall and boundary F-score separately.
- **Main Risk:** Matched-scale pretraining checkpoints are hard to source; may need controlled pretraining runs.

### IDEA-C-0181
- **One-sentence idea:** Stress-test query-based (DETR-family) models on adjacent same-class instances: query competition collapses shared boundaries.
- **Problem:** Query-based instance segmentation may fail predictably where two same-class objects touch, since queries compete for overlapping evidence.
- **Core Hypothesis (falsifiable):** Instance-boundary error between touching same-class objects grows with instance-embedding similarity between the involved queries, exceeds the equivalent error in bottom-up (embedding-clustering) methods at matched overall AP, and is unaffected by NMS-style post-processing — a paradigm-level, not tuning-level, failure.
- **Why Important:** Touching instances are the norm in cells, crowds, and organs; paradigm choice should follow this measurement.
- **Why Possibly Novel:** Adjacency-conditioned error analysis comparing paradigms at matched AP is missing.
- **Minimal Experiment:** Adjacency-stratified evaluation on cell/crowd datasets across query-based vs bottom-up models; query-similarity correlation analysis.
- **Main Risk:** Matched-AP comparison requires careful model selection; use multiple checkpoints per paradigm.

### IDEA-C-0182
- **One-sentence idea:** Chart the duplicate-suppression vs boundary-quality trade-off in NMS-free instance segmentation.
- **Problem:** End-to-end set-prediction losses that suppress duplicates may simultaneously discourage precise boundaries on overlapping instances — two properties currently tuned blindly with one loss weight.
- **Core Hypothesis (falsifiable):** Sweeping the duplicate-suppression strength traces a monotone trade-off curve between duplicate rate and overlapping-instance boundary accuracy, whose slope steepens with instance overlap density — a law that predicts per-dataset optimal operating points.
- **Why Important:** Makes an invisible tuning trade-off explicit and dataset-predictable.
- **Why Possibly Novel:** The suppression-boundary trade-off has not been isolated as a measurable curve.
- **Minimal Experiment:** Matching-cost/loss-weight sweeps on datasets ordered by overlap density; trace curves; validate the slope-density relation.
- **Main Risk:** Loss components interact non-monotonically in some implementations; replicate across two codebases.

### IDEA-C-0183
- **One-sentence idea:** Build a representation-mismatch taxonomy for elongated and curved structures where center-based detection representations fail.
- **Problem:** Center/anchor representations presume compact objects; vessels, catheters, and fracture lines violate the presumption, but the failure is folklore rather than measurement.
- **Core Hypothesis (falsifiable):** Detection quality of center-based representations declines predictably with object elongation and curvature (controlling for area and contrast), with a failure threshold where the geometric center leaves the object mask — while boundary/mask-first representations show no such threshold.
- **Why Important:** Medical structures are disproportionately elongated; representation choice should be driven by measured geometry, not COCO habits.
- **Why Possibly Novel:** Elongation/curvature-conditioned failure curves across representation families have not been published.
- **Minimal Experiment:** Synthetic geometry ladders + vessel/catheter datasets; evaluate representation families across the geometry axes.
- **Main Risk:** Real elongated structures also differ in context; the synthetic arm isolates geometry.

### IDEA-C-0184
- **One-sentence idea:** Map layer-wise gradient conflict between box and mask losses to locate where det/seg representations actually diverge.
- **Problem:** Joint det+seg training conflicts are managed by loss weights without knowing which layers host the disagreement.
- **Core Hypothesis (falsifiable):** Gradient cosine between box and mask objectives is positive in early layers and turns systematically negative at a consistent relative depth across architectures — and splitting the network into shared/task-specific parts exactly at the measured divergence point beats standard split heuristics at equal parameters.
- **Why Important:** Converts multi-task architecture search into a one-measurement design rule.
- **Why Possibly Novel:** Depth-resolved conflict measurement used prescriptively for split placement is untested.
- **Minimal Experiment:** Instrument joint training across 3 architectures; locate conflict depth; train split-at-measured-depth vs conventional variants.
- **Main Risk:** Conflict depth may drift during training; track its dynamics before prescribing static splits.

### IDEA-C-0185
- **One-sentence idea:** Derive the analytic boundary-accuracy ceiling imposed by ROI-pooling quantization and test how close real models sit to it.
- **Problem:** ROI-based mask heads resample features at fixed grids (e.g., 28×28), imposing a computable upper bound on boundary precision that is never compared against actual performance.
- **Core Hypothesis (falsifiable):** Per-object boundary error of ROI-based methods is lower-bounded by a derivable function of object size and ROI grid resolution; measured errors sit near the bound for large objects (grid-limited regime) and far above it for small ones (feature-limited regime) — cleanly splitting error sources.
- **Why Important:** Tells method developers when to spend on higher-resolution heads vs better features — currently guessed.
- **Why Possibly Novel:** The bound is simple to derive but its empirical regime-splitting use is absent from the literature.
- **Minimal Experiment:** Derive the bound; evaluate ROI-based models size-stratified against it on COCO-style and medical data.
- **Main Risk:** Sub-grid information can beat naive bounds via learned interpolation; formalize the bound to accommodate this.

### IDEA-C-0186
- **One-sentence idea:** Probe what shared det/seg features encode per pixel: offset-to-center (detection-flavored) vs offset-to-boundary (segmentation-flavored) information.
- **Problem:** "Representation conflict" remains abstract; a concrete information-content comparison at the pixel level would ground it.
- **Core Hypothesis (falsifiable):** Features from detection-trained backbones support accurate offset-to-center probes but poor offset-to-boundary probes, segmentation-trained backbones show the reverse, and joint models exhibit intermediate profiles whose balance predicts their task trade-off — information content, measured directly, explains the conflict.
- **Why Important:** Moves the det/seg conflict discussion from speculation to per-pixel measurable quantities.
- **Why Possibly Novel:** Geometric-offset probing as a representation-content instrument is not established.
- **Minimal Experiment:** Train offset probes on frozen features from {det, seg, joint} backbones; compare probe error profiles and correlate with task metrics.
- **Main Risk:** Probes measure linear accessibility, not existence; include small nonlinear probes as sensitivity analysis.

### IDEA-C-0187
- **One-sentence idea:** Test the amodal-modal conflict: detectors learn amodal object extent while segmentation learns visible (modal) extent, corrupting shared features under occlusion.
- **Problem:** Boxes routinely cover occluded object parts, masks never do; joint training feeds features contradictory supervision precisely on occluded regions.
- **Core Hypothesis (falsifiable):** In occlusion-stratified evaluation, joint det+seg models show a characteristic error signature absent in single-task twins — mask over-extension into occluded regions and box under-coverage — with magnitude proportional to occlusion rate in training data.
- **Why Important:** Occlusion is pervasive; a supervision-contradiction account would explain a known but unattributed error pattern.
- **Why Possibly Novel:** The amodal-modal supervision contradiction has not been isolated experimentally.
- **Minimal Experiment:** Occlusion-controlled synthetic scenes + occlusion-annotated real data; compare error signatures across single vs joint training.
- **Main Risk:** Real occlusion annotation is scarce; the synthetic arm carries the controlled burden.

### IDEA-C-0188
- **One-sentence idea:** Test asymmetric cross-task transfer: mask supervision improves small-object detection, but box supervision does not improve small-object segmentation.
- **Problem:** Cross-task auxiliary supervision is applied symmetrically by habit; the information asymmetry (masks strictly refine boxes) predicts asymmetric benefits nobody has verified.
- **Core Hypothesis (falsifiable):** Adding mask supervision to a detector improves small-object AP significantly, while adding box supervision to a segmenter leaves small-object boundary and region metrics unchanged — an asymmetry stable across scales and datasets.
- **Why Important:** Annotation budgeting (masks cost more) should be informed by which direction of transfer actually pays.
- **Why Possibly Novel:** The directional-transfer question with size stratification has not been cleanly answered.
- **Minimal Experiment:** 2×2 auxiliary-supervision design at matched annotation budgets on COCO-style and medical data; size-stratified reporting.
- **Main Risk:** Budget matching between boxes and masks requires a defensible cost model; publish it with sensitivity analysis.

### IDEA-C-0189
- **One-sentence idea:** Detect anchor-prior imprinting: aspect-ratio biases from anchor-based pretraining persist in backbones after conversion to segmentation.
- **Problem:** Backbones pretrained inside anchor-based detectors internalize the anchor set's geometry priors; whether these survive re-purposing is unknown.
- **Core Hypothesis (falsifiable):** Segmentation models initialized from anchor-based detection backbones show measurable performance periodicity across object aspect ratios aligned with the pretraining anchor set — a fingerprint absent with anchor-free or classification initialization, decaying only with long fine-tuning.
- **Why Important:** Silent geometric priors from initialization would confound cross-paper comparisons and dataset transfers.
- **Why Possibly Novel:** Anchor-set fingerprinting in downstream models has not been demonstrated.
- **Minimal Experiment:** Fine-tune segmentation from {anchor-based, anchor-free, classification} initializations; evaluate across binned aspect ratios; test alignment with anchor sets.
- **Main Risk:** Aspect-ratio effects are subtle; needs large per-bin sample sizes and seed replication.

### IDEA-C-0190
- **One-sentence idea:** Show that competing instance-segmentation paradigms differ almost entirely on boundary pixels — and agree elsewhere.
- **Problem:** Paradigm debates (top-down vs bottom-up vs query-based) cite aggregate AP, obscuring where the paradigms actually behave differently.
- **Core Hypothesis (falsifiable):** Per-pixel agreement analysis shows inter-paradigm disagreement concentrates within a thin boundary band (with interior agreement near ceiling), implying paradigm choice is a boundary-handling choice — and boundary-band metrics reorder the paradigm ranking relative to AP.
- **Why Important:** Refocuses paradigm research on the pixels where paradigms differ, and questions AP as the deciding metric.
- **Why Possibly Novel:** Cross-paradigm spatial agreement decomposition has not been published.
- **Minimal Experiment:** Matched-AP model triplets; per-pixel agreement/disagreement maps; boundary-band metric re-ranking.
- **Main Risk:** Matched-AP triplets constrain model availability; train controlled versions where needed.

### IDEA-C-0191
- **One-sentence idea:** Test whether the panoptic things/stuff division of labor is actually a spatial-frequency division: things heads handle high-frequency evidence, stuff heads low-frequency.
- **Problem:** Panoptic architectures split things and stuff processing on semantic grounds; the split may functionally be a frequency decomposition — a testable reinterpretation with design consequences.
- **Core Hypothesis (falsifiable):** Frequency-band ablation of inputs degrades things-branch performance predominantly under high-frequency removal and stuff-branch under low-frequency removal, and an explicit frequency-split architecture (no semantic split) matches panoptic baselines — semantics is a proxy for frequency.
- **Why Important:** If frequency is the real axis, simpler and more general architectures follow.
- **Why Possibly Novel:** The frequency reinterpretation of panoptic architecture has not been proposed or tested.
- **Minimal Experiment:** Band-limited input ablations on panoptic models; build and evaluate the frequency-split control architecture.
- **Main Risk:** Things/stuff differ in more than frequency (countability, shape priors); partial support is the likely and still informative outcome.

### IDEA-C-0192
- **One-sentence idea:** Show mask-classification architectures secretly perform detection: their queries have box-like receptive behavior, inheriting detection's failure modes.
- **Problem:** Mask-classification (query-decoder) segmentation is presented as a departure from detection, but its queries may functionally re-implement boxes — importing crowding and duplicate pathologies unacknowledged.
- **Core Hypothesis (falsifiable):** Query attention footprints in mask-classification models are compact and box-approximable (high IoU between attention support and fitted boxes), and the models exhibit detection-typical failures (crowding misses, duplicate-merge errors) at rates predicted by the box-approximability score.
- **Why Important:** Correct lineage understanding predicts failure modes and prevents re-discovering detection fixes under new names.
- **Why Possibly Novel:** The functional-equivalence audit between queries and boxes has not been carried out.
- **Minimal Experiment:** Attention-footprint analysis on trained mask-classification models; failure-mode battery comparison against detectors and FCN-style models.
- **Main Risk:** Footprint compactness varies across layers/heads; aggregate carefully with per-query analysis.

### IDEA-C-0193
- **One-sentence idea:** Quantify how mask-AP's loose IoU thresholds shaped the field toward region-accurate, boundary-sloppy representations — and re-rank methods under boundary-sensitive matching.
- **Problem:** Instance benchmarks match predictions at IoU thresholds insensitive to boundary detail; years of method selection may have optimized representations for exactly this insensitivity.
- **Core Hypothesis (falsifiable):** Re-evaluating the historical method sequence under boundary-weighted matching shows progress flat or negative over periods where standard mask-AP improved — the community optimized the metric, not delineation — with method rank reshuffles concentrated among region-based approaches.
- **Why Important:** A metric-induced blind spot spanning years of research deserves direct documentation and a corrected leaderboard.
- **Why Possibly Novel:** Longitudinal metric-bias archaeology on the instance-segmentation canon has not been done.
- **Minimal Experiment:** Evaluate ~15 historical checkpoints under standard vs boundary-sensitive AP; plot both progress curves.
- **Main Risk:** Public checkpoints vary in training data details; restrict comparisons to documented-comparable models.

### IDEA-C-0194
- **One-sentence idea:** Compare how classification granularity binds to boxes vs masks in open-vocabulary transfer: coarse language hurts masks more than boxes.
- **Problem:** Open-vocab detection and segmentation reuse the same language embeddings, but boxes need only coarse "what+where" while masks need class-conditioned boundary decisions — a granularity mismatch with unknown consequences.
- **Core Hypothesis (falsifiable):** As class-name granularity coarsens (specific→generic prompts), open-vocab segmentation boundary quality degrades faster than detection localization quality on the same models and images — language granularity is a binding constraint for masks specifically.
- **Why Important:** Tells open-vocab system builders where prompt/ontology investment pays: masks, not boxes.
- **Why Possibly Novel:** Granularity-differential analysis between the two output types is unexplored.
- **Minimal Experiment:** Granularity ladders of prompts on joint open-vocab det+seg models; compare degradation slopes of box vs mask metrics.
- **Main Risk:** Box and mask metrics aren't directly commensurable; use within-metric normalized degradation.

### IDEA-C-0195
- **One-sentence idea:** Construct the crowding phase diagram: where counting-by-detection and counting-by-segmentation diverge, and which is right.
- **Problem:** Structure counting uses either detectors or segmentation-plus-connected-components; their divergence under crowding is unquantified, leaving practitioners without a selection rule.
- **Core Hypothesis (falsifiable):** Count error of detection-based methods grows with instance density primarily via misses (undercounting), segmentation-based via merges (undercounting) and splits (overcounting), producing a phase diagram in (density, size-variance) space with a predictable crossover boundary between which approach is more accurate.
- **Why Important:** Counting is a common clinical endpoint (follicles, cells, nodules); an evidence-based selection rule is directly usable.
- **Why Possibly Novel:** The comparative error-mechanism phase diagram has not been mapped.
- **Minimal Experiment:** Synthetic density/size-variance grids + real cell and nodule data; fit and validate the phase boundary.
- **Main Risk:** Synthetic-to-real transfer of the boundary needs the real-data validation arm to carry weight.

### IDEA-C-0196
- **One-sentence idea:** Show that deriving lesion detection from segmentation post-processing destroys calibrated lesion-level confidence, and quantify the decision cost.
- **Problem:** Medical pipelines often segment then extract lesions by connected components, assigning ad-hoc confidences (max/mean pixel score) whose decision-theoretic quality is unexamined.
- **Core Hypothesis (falsifiable):** Lesion-level confidences derived from pixel scores are systematically miscalibrated (size-dependent bias: large lesions overconfident) and rank lesions worse than detection-native confidence at matched localization quality, measurably degrading downstream triage decisions at fixed review budgets.
- **Why Important:** Lesion-level operating points drive clinical review workflows; broken confidence silently corrupts them.
- **Why Possibly Novel:** The pixel-to-lesion confidence conversion problem is unformalized and unmeasured.
- **Minimal Experiment:** Compare lesion-confidence schemes (pixel-derived variants vs detection-native) on lesion benchmarks; calibration and triage-simulation analysis.
- **Main Risk:** Triage simulation assumptions matter; use several review-budget models.

### IDEA-C-0197
- **One-sentence idea:** Derive the theoretical mask-quality ceiling achievable from box supervision alone, and flag box-supervised methods that exceed it as exploiting dataset regularities.
- **Problem:** Box-supervised segmentation methods report ever-better masks; without an information-theoretic reference, it's unclear what part is inference and what part is dataset-prior exploitation.
- **Core Hypothesis (falsifiable):** A computable per-class ceiling (best mask recoverable from box + class shape prior estimated on held-out classes) bounds legitimate box-supervised quality; methods exceeding it on seen classes drop below it on held-out classes — revealing prior memorization masquerading as weak-supervision inference.
- **Why Important:** Separates transferable methodology from dataset-specific fitting in a crowded subfield.
- **Why Possibly Novel:** Ceiling-referenced auditing of box-supervised segmentation has not been proposed.
- **Minimal Experiment:** Estimate ceilings per class; evaluate 5 box-supervised methods on seen vs held-out class splits against ceilings.
- **Main Risk:** Ceiling estimation depends on the shape-prior model class; report ceilings under multiple prior strengths.

### IDEA-C-0198
- **One-sentence idea:** Measure the true cost of head-sharing: the multi-task det+seg Pareto frontier vs separate models at matched total compute.
- **Problem:** Joint det+seg models are justified by efficiency, but loss-weight scalarization may be unable to reach frontier points that two specialized models (splitting the same compute) achieve trivially.
- **Core Hypothesis (falsifiable):** Across loss-weight sweeps, the joint-model Pareto frontier is dominated in a measurable region by compute-split separate models, with the dominated region growing as task-conflict (gradient cosine) increases — sharing has a quantifiable, conflict-predicted price.
- **Why Important:** Deployment architecture choices need the actual price of sharing, not the assumption that it's free.
- **Why Possibly Novel:** Compute-matched frontier comparisons between joint and split det+seg systems are absent.
- **Minimal Experiment:** Dense loss-weight sweeps for joint models vs compute-split pairs on 3 datasets; frontier comparison; conflict-moderation analysis.
- **Main Risk:** Compute matching must include memory/throughput realities, not just FLOPs; report multiple cost accountings.

### IDEA-C-0199
- **One-sentence idea:** Decompose temporal errors in video instance tasks: detection-style tracking preserves identity while mask boundaries drift — two independent error processes.
- **Problem:** Video instance segmentation metrics blend identity errors and boundary errors, obscuring that they may accumulate on different timescales via different mechanisms.
- **Core Hypothesis (falsifiable):** Identity errors accumulate as rare discrete events (switch-point statistics) while boundary errors drift continuously (random-walk-like growth between re-anchoring events), and the two processes are statistically independent — implying separate remedies and separate metrics.
- **Why Important:** A correct error model redirects video-segmentation research toward the actually binding process per application.
- **Why Possibly Novel:** The two-process decomposition with independence testing has not been formalized for video segmentation.
- **Minimal Experiment:** Long-sequence evaluation with per-frame identity and boundary error time series; fit and test the two-process model across methods.
- **Main Risk:** Some architectures couple the processes (mask-driven tracking); the analysis should detect coupling as a finding, not a failure.

### IDEA-C-0200
- **One-sentence idea:** Test whether center+offset representations continuously interpolate the det/seg conflict — a single knob trading box-like and mask-like behavior.
- **Problem:** Center-based dense prediction (predict center + offsets to boundary) sits between paradigms, but whether it *smoothly* spans the trade-off space is unknown.
- **Core Hypothesis (falsifiable):** Varying the offset-field resolution/supervision density in center+offset models traces a continuous path in the (localization robustness, boundary accuracy) plane connecting detector-like and segmenter-like operating points — establishing a unifying representational continuum.
- **Why Important:** A verified continuum would replace paradigm debates with operating-point selection.
- **Why Possibly Novel:** The interpolation claim has never been explicitly tested.
- **Minimal Experiment:** Sweep offset supervision density in a fixed architecture; plot trajectories in the two-metric plane against paradigm endpoints.
- **Main Risk:** The path may be non-monotone or dominated; that outcome equally resolves the question.

### IDEA-C-0201
- **One-sentence idea:** Test distillation direction asymmetry: segmentation models teach detection better than detectors teach segmentation.
- **Problem:** Cross-task distillation direction is chosen by availability, not evidence; the information asymmetry between masks and boxes predicts a preferred direction.
- **Core Hypothesis (falsifiable):** At matched teacher quality, seg→det feature distillation improves detection more than det→seg improves segmentation (normalized by single-task headroom), because mask-trained features contain box-relevant information but not conversely — the probe-measurable information content (cf. offset probes) predicts the transfer asymmetry.
- **Why Important:** Practical guidance for the common situation of having one strong model and needing the other task.
- **Why Possibly Novel:** Direction-asymmetry in cross-task distillation has not been measured or explained.
- **Minimal Experiment:** Symmetric distillation grid (2 directions × 3 datasets) with headroom normalization; link to feature-information probes.
- **Main Risk:** Teacher-quality matching across tasks is nontrivial; use multiple matching criteria.

### IDEA-C-0202
- **One-sentence idea:** Treat FPN level allocation as a measurable resolution-budget conflict: detection wants coarse levels, segmentation wants fine ones, and the optimum is predictable from object statistics.
- **Problem:** Feature-pyramid design (which levels feed which head) is inherited from detection conventions; its interaction with segmentation needs is unoptimized and unexplained.
- **Core Hypothesis (falsifiable):** Per-task performance as a function of allocated pyramid levels follows each task's object-scale × boundary-detail statistics, and a closed-form allocation rule from dataset statistics matches exhaustive allocation search — the conflict is a predictable resource-allocation problem.
- **Why Important:** Replaces convention-driven architecture reuse with a two-statistic design calculation.
- **Why Possibly Novel:** Pyramid allocation as a statistics-predictable optimization has not been formulated.
- **Minimal Experiment:** Allocation grid search on 4 datasets with diverse object statistics; fit the predictive rule; validate on 2 held-out datasets.
- **Main Risk:** Modern architectures blur level boundaries (deformable attention); scope the claim to explicit-pyramid designs.

### IDEA-C-0203
- **One-sentence idea:** Trace duplicate-instance hallucination in query-based models to training dynamics of the matching loss — and predict which queries will duplicate.
- **Problem:** Query-based models occasionally emit near-duplicate instances; the phenomenon is treated as noise rather than a predictable consequence of bipartite-matching training.
- **Core Hypothesis (falsifiable):** Queries that duplicate at inference share identifiable training signatures (unstable matching assignments across epochs, high assignment-entropy), and an assignment-stability regularizer reduces duplication without harming recall — the pathology is a measurable training-dynamics artifact.
- **Why Important:** Duplicates corrupt counting and downstream measurement; a mechanistic account enables prevention rather than post-hoc filtering.
- **Why Possibly Novel:** Matching-dynamics forensics linking training instability to inference duplication is unexplored.
- **Minimal Experiment:** Log per-query matching trajectories during training; correlate with inference duplication; test the stability regularizer.
- **Main Risk:** Duplication is rare per image; requires large-scale evaluation for statistical power.

### IDEA-C-0204
- **One-sentence idea:** Test whether sliding-window 3D segmentation loses whole-object evidence that detection-style global context retains — on large lesions exceeding window size.
- **Problem:** 3D medical segmentation processes fixed windows for memory reasons; objects larger than the window are never seen whole, unlike in detection-style whole-volume approaches.
- **Core Hypothesis (falsifiable):** Segmentation error on lesions larger than the inference window grows discontinuously at the window-size threshold (controlling for lesion size effects below it), and providing coarse whole-volume context (low-res global pass) removes the discontinuity — proving a window-induced, not size-induced, failure.
- **Why Important:** Large lesions are high-stakes cases; a systematic window artifact on them would be an important hidden failure of standard pipelines.
- **Why Possibly Novel:** The window-threshold discontinuity has not been isolated from general size effects.
- **Minimal Experiment:** Size-stratified evaluation across window sizes on lesion datasets; regression-discontinuity analysis at window thresholds; global-context intervention.
- **Main Risk:** Large lesions are rare; pool across datasets and use synthetic enlargement as a supplementary arm.

---

## C8. Boundary quality as a scientific problem (IDEA-C-0205 … 0232)

### IDEA-C-0205
- **One-sentence idea:** Decompose segmentation boundary error into image-aleatoric, annotation-protocol, and model-bias components with a reusable methodology.
- **Problem:** Boundary error is reported as one number, conflating irreducible image ambiguity, labeling convention, and actual model deficiency — making cross-paper progress claims uninterpretable.
- **Core Hypothesis (falsifiable):** The three components are separable using (a) multi-rater data for protocol variance, (b) local image-gradient statistics for aleatoric floor, and (c) residual for model bias — and across modern models, the model-bias component is a minority share of total boundary error on standard benchmarks.
- **Why Important:** If most boundary error is not model-caused, boundary-method research is optimizing an already-saturated component.
- **Why Possibly Novel:** Boundary-error budget accounting as a formal decomposition has not been established.
- **Minimal Experiment:** Multi-rater datasets; estimate the three components for 5 models; report error budgets and their stability.
- **Main Risk:** Component identifiability requires assumptions; validate with synthetic data where components are known.

### IDEA-C-0206
- **One-sentence idea:** Measure the physics floor: partial-volume effects and slice thickness define a computable lower bound on boundary error in medical imaging.
- **Problem:** Boundary metrics are compared to zero as the implicit ideal, though imaging physics makes sub-PSF boundary localization information-theoretically limited.
- **Core Hypothesis (falsifiable):** A floor computed from point-spread function and voxel anisotropy predicts the plateau of boundary accuracy across models and datasets; models at the floor cannot be distinguished by boundary metrics, and reported "improvements" below the floor are noise.
- **Why Important:** Establishes when boundary progress is real versus metrological illusion — a calibration the field lacks.
- **Why Possibly Novel:** Physics-derived boundary-metric floors are not part of segmentation evaluation practice.
- **Minimal Experiment:** Derive floors for public CT/MR datasets from acquisition metadata; compare model boundary errors and inter-model gaps against floors.
- **Main Risk:** PSF metadata is incomplete for some datasets; estimate empirically from edge profiles where missing.

### IDEA-C-0207
- **One-sentence idea:** Fit separate scaling laws for region vs boundary accuracy versus training-set size — boundaries learn slower.
- **Problem:** Data-scaling studies use overlap metrics; whether boundary quality follows the same data-return curve is unknown, with direct consequences for annotation investment.
- **Core Hypothesis (falsifiable):** Boundary-metric learning curves have systematically smaller exponents than region-metric curves on the same runs — meaning data scaling closes region gaps faster than boundary gaps, and boundary-targeted supervision has rising relative value with scale.
- **Why Important:** Annotation strategy (more images vs better boundaries per image) should follow the measured exponents.
- **Why Possibly Novel:** Metric-resolved scaling exponents for segmentation are unreported.
- **Minimal Experiment:** Data-size sweeps on 4 datasets; fit power laws per metric family; test exponent differences statistically.
- **Main Risk:** Boundary metrics are noisier, complicating exponent estimation; use large test sets and repeated draws.

### IDEA-C-0208
- **One-sentence idea:** Derive and verify the systematic inward/outward boundary bias induced by cross-entropy training under class imbalance.
- **Problem:** Boundary placement bias is observed anecdotally (models "shrink" rare structures) but lacks an analytic account tied to the loss.
- **Core Hypothesis (falsifiable):** The stationary decision boundary under pixel-wise CE sits at a posterior threshold displaced from the true boundary by a computable function of local class prior and label noise — predicting per-structure signed bias that matches measured displacement fields across datasets.
- **Why Important:** A predictable, correctable bias affecting every CE-trained segmenter — including volumetry used clinically.
- **Why Possibly Novel:** The quantitative displacement prediction and its empirical verification are missing from the literature.
- **Minimal Experiment:** Derive the displacement formula; measure signed boundary displacement across structures with varying priors; compare prediction to measurement.
- **Main Risk:** Real training deviates from the stationary analysis (augmentation, schedules); test robustness across recipes.

### IDEA-C-0209
- **One-sentence idea:** Recalibrate softmax confidence into calibrated boundary-distance estimates — models encode distance, but nonlinearly and miscalibrated.
- **Problem:** Practitioners read boundary uncertainty from softmax values, an uncalibrated proxy whose actual relation to distance-from-true-boundary is uncharacterized.
- **Core Hypothesis (falsifiable):** The mapping from logit margin to true boundary distance is monotone but strongly model- and structure-dependent; fitting it on small calibration sets yields distance predictions with quantified error, enabling confidence bands on boundary position that empirically cover at nominal rates.
- **Why Important:** Calibrated boundary-position uncertainty is what surgical planning and radiotherapy margins actually need.
- **Why Possibly Novel:** Boundary-distance calibration (as opposed to class-probability calibration) is an unformalized problem.
- **Minimal Experiment:** Fit margin→distance maps per model/structure; validate coverage of derived confidence bands on held-out data.
- **Main Risk:** The mapping may be context-dependent within structures; assess spatial homogeneity explicitly.

### IDEA-C-0210
- **One-sentence idea:** Redo method comparison statistics accounting for spatial autocorrelation of boundary errors — standard tests overstate significance.
- **Problem:** Boundary-error comparisons treat per-pixel or per-case errors as independent; boundary errors are strongly spatially autocorrelated, shrinking effective sample sizes.
- **Core Hypothesis (falsifiable):** Applying autocorrelation-corrected inference (effective-N adjustment, block bootstrap along boundaries) to published-style comparisons removes statistical significance from a substantial fraction of boundary-metric "wins" while leaving region-metric conclusions largely intact.
- **Why Important:** The field's boundary-improvement claims rest on inference that may be systematically anti-conservative.
- **Why Possibly Novel:** Spatial-statistics rigor has not been imported into segmentation benchmarking.
- **Minimal Experiment:** Measure boundary-error autocorrelation lengths; re-run 10 representative comparisons with corrected inference; report surviving claims.
- **Main Risk:** Correction methods have their own assumptions; use two independent correction approaches.

### IDEA-C-0211
- **One-sentence idea:** Compare model and human boundary completion on low-contrast gaps: models under-complete boundaries humans confidently interpolate.
- **Problem:** Where image evidence vanishes (low contrast, occlusion), humans complete boundaries using Gestalt/shape priors; whether and where models do the same is unmeasured.
- **Core Hypothesis (falsifiable):** On a stimulus battery of graded evidence gaps, human raters place boundaries with high inter-rater consistency far beyond the evidence-supported region, while model boundaries collapse toward evidence edges — a completion gap that shape-prior training signals (but not more data) reduces.
- **Why Important:** Boundary completion is a defined capability with clinical relevance (infiltrating tumor margins) — worth isolating from generic accuracy.
- **Why Possibly Novel:** Psychophysics-style completion comparison between raters and segmentation models has not been performed.
- **Minimal Experiment:** Graded-gap stimuli (natural and constructed); human annotation study vs model outputs; completion-distance metrics.
- **Main Risk:** Human completion may reflect convention rather than perception; use consistency across independent raters as the anchor.

### IDEA-C-0212
- **One-sentence idea:** Detect annotation-tool fingerprints in ground-truth boundaries and quantify their effect on benchmark comparisons.
- **Problem:** Polygon tools, brushes, and level-set-assisted tools each impose characteristic boundary statistics (vertex spacing, curvature spectra, smoothness) that become part of "ground truth" invisibly.
- **Core Hypothesis (falsifiable):** The annotation tool is identifiable from boundary statistics alone at high accuracy, models trained on one tool's labels score systematically higher against same-tool test labels (tool-matching bonus), and part of cross-dataset "generalization gaps" is tool mismatch rather than image-domain shift.
- **Why Important:** A hidden variable contaminating every cross-dataset boundary comparison should be measured and corrected for.
- **Why Possibly Novel:** Tool forensics on segmentation ground truth appears entirely unexplored.
- **Minimal Experiment:** Train tool classifiers on datasets with documented tooling; measure the tool-matching bonus via cross-tool re-annotation of a subset.
- **Main Risk:** Tool metadata is rarely documented; requires targeted small re-annotation studies.

### IDEA-C-0213
- **One-sentence idea:** Test whether boundary skill is a transferable model property or task-specific: cross-task rank correlation of boundary vs region performance.
- **Problem:** Method rankings implicitly assume "good at boundaries" generalizes; boundary quality may instead be brittle and anatomy-specific in ways region quality is not.
- **Core Hypothesis (falsifiable):** Across model×task grids, region-metric rankings correlate strongly between tasks while boundary-metric rankings correlate weakly — boundary skill is decoupled and non-transferable, invalidating single-benchmark boundary claims.
- **Why Important:** Determines whether boundary-focused methods should be trusted beyond the datasets they were shown on.
- **Why Possibly Novel:** The transferability structure of boundary skill has not been measured.
- **Minimal Experiment:** 8 models × 6 tasks; compute inter-task rank correlations per metric family; compare correlation structures.
- **Main Risk:** Model pools must be diverse enough to avoid restriction-of-range artifacts in correlations.

### IDEA-C-0214
- **One-sentence idea:** Extract sub-pixel boundary estimates from logit gradients: models know boundary positions more precisely than their argmax masks express.
- **Problem:** Standard mask extraction discretizes at pixel resolution, discarding the continuous structure of the network's output field around boundaries.
- **Core Hypothesis (falsifiable):** Sub-pixel boundary localization derived from the logit field's zero-crossing interpolation beats argmax-mask boundaries against high-resolution reference truth by a consistent margin — demonstrating recoverable precision that standard evaluation and deployment throw away.
- **Why Important:** Free precision for volumetry and margins, plus a reframing: boundary quality is partly a readout problem, not a learning problem.
- **Why Possibly Novel:** Sub-pixel readout of segmentation networks against super-resolution ground truth has not been systematically evaluated.
- **Minimal Experiment:** Datasets with high-res reference (downsample-for-input protocol); compare argmax vs interpolated zero-crossing boundaries.
- **Main Risk:** Downsample-based reference protocols may favor interpolation methods artificially; complement with genuinely higher-resolution rescans where available.

### IDEA-C-0215
- **One-sentence idea:** Test a universal law: the optimal boundary-loss band width scales as a constant fraction of object scale across datasets and architectures.
- **Problem:** Boundary-weighted losses fix band width in pixels by convention; whether an object-relative universal constant governs the optimum is unknown.
- **Core Hypothesis (falsifiable):** Sweeping band width normalized by per-object scale reveals optima at a stable fraction (within a narrow interval) across structures, datasets, and two architectures — while pixel-fixed bands are systematically suboptimal for datasets with heterogeneous object sizes.
- **Why Important:** Replaces a per-dataset hyperparameter with a principled scale-adaptive rule benefiting every boundary-loss user.
- **Why Possibly Novel:** Scale-normalized band-width analysis has not been reported.
- **Minimal Experiment:** Band-width sweeps (absolute and scale-normalized) across 4 datasets × 2 architectures; locate and compare optima.
- **Main Risk:** Optima may be shallow, weakening the law; report curvature of the optimum, not just its location.

### IDEA-C-0216
- **One-sentence idea:** Reframe distance-based losses as risk-profile reshapers: they change boundary-error *distributions* (taming tails) more than means.
- **Problem:** Distance-transform losses are marketed as boundary-accuracy improvers, but their measured mean gains are inconsistent; their real effect may be distributional.
- **Core Hypothesis (falsifiable):** Across matched trainings, distance-based losses leave mean boundary error statistically unchanged while significantly shrinking the upper tail (95th/99th percentile errors, Hausdorff-type events) — a risk-profile change invisible to mean-based evaluation but decisive for safety-oriented use.
- **Why Important:** Correctly characterizes what these widely used losses buy, aligning method choice with application risk tolerance.
- **Why Possibly Novel:** Distribution-level (rather than mean-level) analysis of loss effects is absent from the loss-function literature.
- **Minimal Experiment:** Matched trainings {CE/Dice vs +distance losses} × 4 datasets; compare full boundary-error distributions with tail-focused statistics.
- **Main Risk:** Tail statistics need large test sets; pool per-boundary-point errors with autocorrelation-aware inference (cf. 0210).

### IDEA-C-0217
- **One-sentence idea:** Audit 3D anisotropy: through-plane boundary errors dominate total error and are invisible to the 2D/in-plane metrics most papers report.
- **Problem:** Anisotropic voxels (thick slices) make through-plane boundaries physically and statistically different, yet evaluation practice aggregates directions or evaluates in-plane only.
- **Core Hypothesis (falsifiable):** Direction-decomposed boundary error shows through-plane components several times larger than in-plane across standard 3D benchmarks, method rankings differ between directions, and published "boundary improvements" concentrate in the in-plane component — the dominant error direction is the least improved.
- **Why Important:** Volumetry and margin errors are driven by the dominant component; the field may be optimizing the minor one.
- **Why Possibly Novel:** Direction-decomposed boundary evaluation is not standard and rankings under it are unreported.
- **Minimal Experiment:** Decompose boundary errors by direction for 6 methods on anisotropic benchmarks; compare component rankings.
- **Main Risk:** Ground truth itself is less reliable through-plane; incorporate rater-variance floors per direction.

### IDEA-C-0218
- **One-sentence idea:** Perform bias-variance decomposition of boundary displacement fields: model boundary errors are directional and consistent, not random.
- **Problem:** Boundary error metrics are unsigned magnitudes, hiding whether models systematically displace boundaries (bias) or scatter around truth (variance) — different problems with different fixes.
- **Core Hypothesis (falsifiable):** Across seeds, per-location mean displacement (bias field) accounts for the majority of squared boundary error in trained segmenters, bias fields are reproducible across architectures (image-driven), and simple post-hoc bias-field correction improves boundaries more than typical loss innovations.
- **Why Important:** If boundary error is mostly reproducible bias, it is correctable — a cheap large win the unsigned-metric convention has hidden.
- **Why Possibly Novel:** Signed, seed-resolved displacement decomposition has not been applied to segmentation boundaries.
- **Minimal Experiment:** Multi-seed trainings; estimate bias/variance fields on held-out data; test bias-correction transfer across seeds and models.
- **Main Risk:** Bias fields may be dataset-specific (annotation-driven); the architecture-reproducibility test distinguishes image- from label-driven bias.

### IDEA-C-0219
- **One-sentence idea:** Do decoder forensics: upsampling-path design leaves detectable signatures in predicted boundary statistics, independent of accuracy.
- **Problem:** Bilinear, transposed-conv, and pixel-shuffle decoders impose different spectral artifacts on output boundaries; these signatures confound boundary-metric comparisons between methods that differ in decoders incidentally.
- **Core Hypothesis (falsifiable):** The decoder type is identifiable from boundary curvature/frequency statistics of predictions alone at high accuracy, and part of inter-method boundary-metric differences is explained by decoder signature compatibility with each dataset's annotation smoothness — a nuisance factor separable from real delineation skill.
- **Why Important:** Disentangles architectural artifact from genuine boundary competence in every comparison involving different decoders.
- **Why Possibly Novel:** Output-forensics of decoder families is unexplored.
- **Minimal Experiment:** Train decoder-varied but otherwise identical models; classify decoder from outputs; regress metric differences on signature-annotation compatibility.
- **Main Risk:** Signatures may fade with deep supervision or refinement; report conditions of detectability.

### IDEA-C-0220
- **One-sentence idea:** Build a clinician-grounded boundary metric from pairwise acceptability preferences, and test where it diverges from geometric metrics.
- **Problem:** Boundary metrics (HD, ASSD, boundary-IoU) are geometric conveniences; whether they order segmentations the way expert users do is unvalidated.
- **Core Hypothesis (falsifiable):** A preference model fitted to clinician pairwise judgments of boundary acceptability disagrees with geometric-metric orderings on a substantial fraction of pairs, with disagreements structured (clinicians tolerate smooth global offsets, punish local excursions into critical tissue) — and the fitted metric re-ranks published methods.
- **Why Important:** If metrics disagree with users on what "better boundaries" means, the optimization target of an entire literature is misaligned.
- **Why Possibly Novel:** Preference-learning-based validation of boundary metrics has not been conducted.
- **Minimal Experiment:** Collect ~2k pairwise clinician judgments on segmentation pairs; fit preference model; analyze divergence structure and re-rank methods.
- **Main Risk:** Clinician preferences vary by specialty/task; scope to one clinical task first and report rater agreement.

### IDEA-C-0221
- **One-sentence idea:** Quantify the topology-geometry trade-off: enforcing topological correctness measurably worsens local boundary accuracy.
- **Problem:** Topology-preserving losses/postprocessing are adopted assuming free coexistence with geometric accuracy; the two objectives may compete on exactly the ambiguous pixels.
- **Core Hypothesis (falsifiable):** Across topology-enforcement strengths, boundary accuracy near topology-critical regions (thin connections, near-touching structures) degrades monotonically as violations decrease — a quantifiable frontier whose slope varies by anatomy, enabling application-specific operating-point choice rather than binary adoption.
- **Why Important:** Both properties matter clinically in different tasks; the trade-off must be priced, not assumed away.
- **Why Possibly Novel:** The frontier between topological and geometric fidelity has not been traced.
- **Minimal Experiment:** Strength sweeps of two topology methods on vessel/organ data; measure violations vs local boundary error near critical regions.
- **Main Risk:** Topology metrics are coarse; use multiple (Betti errors, connectivity-aware scores) for robustness.

### IDEA-C-0222
- **One-sentence idea:** Measure each architecture's "boundary bandwidth": the curvature frequency above which predicted boundaries low-pass filter the truth.
- **Problem:** Predicted boundaries look smoother than real anatomy, but the cutoff — and its architectural determinants — has never been quantified.
- **Core Hypothesis (falsifiable):** The transfer function from true to predicted boundary curvature spectra shows a stable per-architecture cutoff frequency, determined primarily by output-path resolution (not encoder capacity), and matching curvature spectra to task requirements predicts which anatomies each architecture fails (spiculated vs smooth structures).
- **Why Important:** Provides a physics-style specification sheet for segmentation architectures, replacing anecdotal architecture folklore.
- **Why Possibly Novel:** Spectral transfer-function analysis of boundary reproduction is new to the field.
- **Minimal Experiment:** Estimate curvature-spectrum transfer functions for 6 architectures on shared data; ablate output-path resolution; validate the anatomy-failure prediction.
- **Main Risk:** Annotation smoothing contaminates "true" spectra; use high-confidence sub-corpora and synthetic shapes.

### IDEA-C-0223
- **One-sentence idea:** Estimate the model-free refinement bound: how much boundary error is recoverable from the image alone, post-hoc, without touching the model.
- **Problem:** Boundary refinement modules are proposed continually; nobody has established how much refinement headroom exists in principle given only the image and an initial mask.
- **Core Hypothesis (falsifiable):** An oracle-guided classical refinement (active contour with oracle parameters per case) quantifies the image-supported recoverable error; real refinement methods capture a small fraction of it, and the headroom concentrates in a characteristic contrast/curvature regime — mapping where refinement research can and cannot pay.
- **Why Important:** Bounds the value of an entire methods genre and locates where its opportunities actually are.
- **Why Possibly Novel:** Oracle-bound accounting for boundary refinement has not been reported.
- **Minimal Experiment:** Oracle-parameter refinement sweeps on model outputs across datasets; compare to published refinement gains; map headroom vs local image statistics.
- **Main Risk:** Oracle bounds depend on the refinement family chosen; use two distinct families (contour-based, graph-based).

### IDEA-C-0224
- **One-sentence idea:** Create a physical-truth boundary calibration set via high-resolution rescans/phantoms to anchor all boundary metrics to reality.
- **Problem:** Boundary metrics are computed against annotations, whose own error is unknown at the sub-voxel scale where methods now compete — the field lacks any physically grounded reference.
- **Core Hypothesis (falsifiable):** Against physically grounded references (high-res rescans of the same anatomy, imaging phantoms with known geometry), annotation-referenced boundary metrics misestimate true error by amounts comparable to inter-method differences — meaning current boundary leaderboards partially rank agreement-with-annotation-style, not accuracy.
- **Why Important:** A small physical-truth anchor set would recalibrate boundary evaluation field-wide.
- **Why Possibly Novel:** Physically grounded boundary references are absent from segmentation benchmarking.
- **Minimal Experiment:** Acquire/assemble phantom scans and paired low/high-resolution acquisitions; compare annotation-referenced vs physical-referenced error for several models.
- **Main Risk:** Phantoms lack biological boundary complexity; combine with paired-resolution human data to span realism.

### IDEA-C-0225
- **One-sentence idea:** Represent boundary uncertainty as distributions over curves rather than pixel-wise heatmaps — and show heatmaps mislead on connected structures.
- **Problem:** Pixel-wise uncertainty cannot express correlated boundary hypotheses ("the whole edge is shifted left" vs "each pixel independently uncertain"), yet downstream consumers interpret it as if it could.
- **Core Hypothesis (falsifiable):** For structures with correlated ambiguity, curve-space uncertainty (samples of coherent boundary hypotheses) yields calibrated interval estimates for derived quantities (area, diameter) where pixel-wise heatmap propagation is provably and measurably miscalibrated — the representation, not the estimator, is the bottleneck.
- **Why Important:** Downstream clinical quantities need correlated uncertainty; the field's default representation cannot carry it.
- **Why Possibly Novel:** Curve-space vs pixel-space uncertainty as a formal comparison with calibration endpoints is new.
- **Minimal Experiment:** Multi-rater data with correlated ambiguity; fit both representations; compare calibration of derived-quantity intervals.
- **Main Risk:** Curve-space modeling is technically heavier; keep to simple boundary-offset process models for the comparison.

### IDEA-C-0226
- **One-sentence idea:** Test the hard-mask artifact hypothesis: training on binarized masks (versus soft anti-aliased ones) instills a measurable boundary bias.
- **Problem:** Ground-truth masks are stored binarized, discarding the partial-volume reality at boundaries; models may inherit a quantization artifact as learned behavior.
- **Core Hypothesis (falsifiable):** Models trained on soft (anti-aliased/partial-volume) boundary labels show reduced systematic displacement bias and better sub-pixel readout quality (cf. 0214) than hard-label twins at identical data and architecture — the binarization step itself causes part of boundary bias.
- **Why Important:** A costless data-representation change (keep soft labels) could improve every boundary-sensitive application.
- **Why Possibly Novel:** The binarization step is universal and unexamined as a bias source.
- **Minimal Experiment:** Generate soft labels from high-res annotations by principled downsampling; train hard vs soft twins; compare bias fields and sub-pixel accuracy.
- **Main Risk:** Soft-label generation choices could drive results; test two generation protocols.

### IDEA-C-0227
- **One-sentence idea:** Separate Hausdorff-distance failures into their own taxonomy: single-point outliers have different causes than diffuse boundary error and need different research.
- **Problem:** HD is driven by the single worst point; methods "improving HD" may be fixing rare artifact-driven excursions, not boundaries — two phenomena conflated by one metric.
- **Core Hypothesis (falsifiable):** Case-level analysis shows HD events (large excursions) are attributable to identifiable causes (artifacts, ambiguous anatomy, label errors) statistically distinct from the drivers of mean boundary error, and methods that improve HD do so predominantly by suppressing one cause class — supporting metric and method segregation by failure type.
- **Why Important:** Merged failure types produce methods that fix the wrong thing and evaluations that reward it.
- **Why Possibly Novel:** Causal taxonomy of HD events has not been constructed.
- **Minimal Experiment:** Annotate causes of the worst-point events across models/datasets; compare cause distributions against mean-error drivers; re-analyze published HD improvements by cause.
- **Main Risk:** Cause annotation is judgment-laden; use multiple raters and explicit criteria.

### IDEA-C-0228
- **One-sentence idea:** Factor-analyze segmentation quality: how many independent dimensions exist beyond Dice, and which metrics span them?
- **Problem:** Dozens of metrics are reported ad hoc; their correlation structure at fixed overall quality — the true dimensionality of "segmentation quality" — is unknown.
- **Core Hypothesis (falsifiable):** Across large model×case matrices, metric variation at fixed Dice is captured by a small number of interpretable factors (boundary fidelity, topology, size bias, outlier propensity), stable across datasets — enabling a minimal sufficient metric panel and exposing which published metrics are redundant.
- **Why Important:** A validated low-dimensional quality space would standardize evaluation and stop metric proliferation.
- **Why Possibly Novel:** Psychometric-style factor analysis of segmentation metrics has not been performed.
- **Minimal Experiment:** Compute 20 metrics for many model-case pairs across 5 datasets; factor analysis with cross-dataset stability testing.
- **Main Risk:** Factor structure may be task-dependent; report invariant core vs task-specific factors.

### IDEA-C-0229
- **One-sentence idea:** Demonstrate that evaluation-resolution choices change boundary-metric method rankings, and propose resolution-invariant boundary evaluation.
- **Problem:** Boundary metrics are computed at whatever resolution the pipeline uses (native, resampled, model-output); this nuisance parameter's effect on conclusions is unquantified.
- **Core Hypothesis (falsifiable):** Recomputing boundary metrics across evaluation resolutions flips method rankings in a nontrivial fraction of published-style comparisons, with flips concentrated among methods differing in output resolution — while a proposed resolution-normalized protocol yields stable rankings.
- **Why Important:** An invisible pipeline choice that flips conclusions must be standardized before boundary comparisons are meaningful.
- **Why Possibly Novel:** Evaluation-resolution sensitivity analysis for segmentation metrics is unreported.
- **Minimal Experiment:** Re-evaluate 8 method pairs across 4 evaluation resolutions; count ranking flips; validate the normalized protocol's stability.
- **Main Risk:** "Correct" reference resolution is itself contestable; anchor to physical units where metadata permits.

### IDEA-C-0230
- **One-sentence idea:** Derive the implicit boundary prior of each common segmentation loss (CE, Dice, Tversky, boundary losses) and verify the predicted boundary behaviors empirically.
- **Problem:** Losses are chosen by benchmark performance without theory of what boundary each loss asks for at optimum under realistic ambiguity.
- **Core Hypothesis (falsifiable):** Each loss's optimal decision boundary under a local ambiguity model is derivable in closed form (posterior thresholds, size-biased displacements), and trained models' measured boundary placements match their loss's predicted stationary behavior — losses are boundary priors in disguise, predictably so.
- **Why Important:** Converts loss selection from folklore to specification: choose the loss whose stationary boundary matches the clinical need.
- **Why Possibly Novel:** Stationary-boundary analysis across the common loss family with empirical verification is missing.
- **Minimal Experiment:** Derive stationary conditions; train loss-varied twins on controlled-ambiguity synthetic and real data; compare placements to predictions.
- **Main Risk:** Optimization may not reach stationary behavior; measure convergence toward predictions across training length.

### IDEA-C-0231
- **One-sentence idea:** Test whether iterative boundary-refinement gains concentrate on annotation-noisy boundaries — fitting label style rather than recovering true anatomy.
- **Problem:** Recurrent/iterative refinement reports boundary gains against annotations; if gains concentrate where annotations are themselves unreliable, refinement may be learning annotation habits.
- **Core Hypothesis (falsifiable):** Stratifying test boundaries by annotation reliability (multi-rater agreement) shows refinement gains concentrated in low-reliability strata and vanishing in high-reliability strata — the opposite pattern from genuine accuracy improvements, which a physical-reference arm (cf. 0224) can confirm.
- **Why Important:** Distinguishes real delineation progress from style-fitting in a popular methods family.
- **Why Possibly Novel:** Reliability-stratified attribution of refinement gains has not been done.
- **Minimal Experiment:** Multi-rater test sets; stratified gain analysis for 3 refinement methods; physical-reference spot check.
- **Main Risk:** Low-agreement regions are also genuinely harder; the physical-reference arm arbitrates.

### IDEA-C-0232
- **One-sentence idea:** Map the nonlinear sensitivity from boundary perturbations to downstream clinical endpoints (volume, radiomics, RECIST) — where boundary accuracy actually matters.
- **Problem:** Boundary research assumes uniform value of boundary accuracy; downstream clinical quantities weight boundary errors nonuniformly and nonlinearly, unmapped to date.
- **Core Hypothesis (falsifiable):** Controlled boundary perturbation experiments yield sensitivity maps showing that clinical-endpoint error is dominated by specific boundary regions and error modes (e.g., low-curvature offsets dominate volume error; high-curvature regions dominate radiomic texture features) — enabling endpoint-targeted boundary optimization and evaluation.
- **Why Important:** Aligns boundary research investment with clinical consequence — some boundary errors don't matter, others matter enormously.
- **Why Possibly Novel:** Systematic perturbation-to-endpoint sensitivity mapping is absent from the literature.
- **Minimal Experiment:** Parametrized boundary perturbations on ground-truth masks; compute endpoint error surfaces across perturbation modes; validate on real model errors.
- **Main Risk:** Perturbation parameterizations may miss real error modes; seed with measured model bias fields (cf. 0218).

---

## C9. Ambiguous labels / inter-rater disagreement as signal, not noise (IDEA-C-0233 … 0260)

### IDEA-C-0233
- **One-sentence idea:** Validate inter-rater disagreement maps as a free error oracle: where raters disagree predicts where models fail.
- **Problem:** Model error prediction (quality control) is built from model internals; the annotation process itself may already contain the best error predictor, unused.
- **Core Hypothesis (falsifiable):** Spatial rater-disagreement maps predict held-out model error maps with accuracy exceeding model-confidence-based error predictors, across architectures — implying model errors are dominated by intrinsic case ambiguity rather than model idiosyncrasy.
- **Why Important:** Would give deployment QC a model-independent error forecaster and reframe error analysis around case difficulty.
- **Why Possibly Novel:** Disagreement as a quantitative error-forecasting instrument (benchmarked against confidence methods) has not been established.
- **Minimal Experiment:** Multi-rater datasets; compare disagreement maps vs confidence/ensemble error predictors for several models; report predictive AUCs.
- **Main Risk:** Circularity if models were trained on the same raters' styles; use rater-disjoint training/evaluation splits.

### IDEA-C-0234
- **One-sentence idea:** Quantify consensus harm: training on majority-vote/STAPLE labels destroys clinically relevant ambiguity information relative to training on raw rater sets.
- **Problem:** Consensus fusion is the default preprocessing for multi-rater data, presumed harmless noise reduction; it may erase exactly the distributional signal risk-aware applications need.
- **Core Hypothesis (falsifiable):** Models trained on raw multi-rater labels (as distributions) match consensus-trained models on consensus metrics while being substantially better calibrated to the rater distribution on ambiguous regions — the consensus step is where ambiguity information dies, measurably.
- **Why Important:** A default preprocessing choice with hidden costs affects nearly all multi-annotated medical datasets.
- **Why Possibly Novel:** The information cost of consensus fusion, isolated as a training-data intervention, is rarely measured directly.
- **Minimal Experiment:** Train on {consensus, raw multi-rater} from identical images; evaluate consensus accuracy and rater-distribution likelihood on held-out multi-rater data.
- **Main Risk:** Raw multi-rater training methods vary; use 2–3 established schemes to detach the claim from method specifics.

### IDEA-C-0235
- **One-sentence idea:** Decompose rater disagreement into systematic style offsets versus genuine ambiguity using mixed-effects modeling — recovering hidden agreement.
- **Problem:** All disagreement is treated as ambiguity; but raters may agree on the structure while differing by consistent personal offsets (tight vs generous delineation), a separable component.
- **Core Hypothesis (falsifiable):** A mixed-effects model (rater-specific boundary offset fields + shared ambiguity term) explains a majority of inter-rater variance on typical datasets, and style-corrected labels show substantially higher effective agreement — most "ambiguity" is removable style.
- **Why Important:** Changes the interpretation of multi-rater data everywhere: variance budgets, achievable-performance ceilings, and label fusion should all use style-corrected quantities.
- **Why Possibly Novel:** Formal style/ambiguity decomposition of segmentation disagreement is not standard practice.
- **Minimal Experiment:** Fit the decomposition on multi-rater datasets; report variance shares; validate style terms by cross-structure prediction of each rater's offsets.
- **Main Risk:** Style may be context-dependent (structure-specific); model hierarchical style terms.

### IDEA-C-0236
- **One-sentence idea:** Test rater-as-transformation modeling against rater-as-noise modeling with held-out raters as the referee.
- **Problem:** Multi-annotator learning methods split into two philosophies (raters transform a latent truth vs raters add noise); no clean comparison predicts *unseen* raters — the test both philosophies should face.
- **Core Hypothesis (falsifiable):** Transformation-based models generalize to held-out raters (predicting their labels from few examples) substantially better than noise-based models, demonstrating raters are structured functions, not noise sources — with the gap largest for boundary placement and smallest for detection decisions.
- **Why Important:** The correct rater model determines label fusion, uncertainty estimation, and annotation-budget design.
- **Why Possibly Novel:** Held-out-rater generalization as the adjudicating benchmark between the philosophies has not been run.
- **Minimal Experiment:** Datasets with ≥5 raters; train each model family on rater subsets; evaluate label prediction for held-out raters.
- **Main Risk:** Few datasets have enough raters; nodule and prostate collections are the feasible substrate.

### IDEA-C-0237
- **One-sentence idea:** Show ambiguity is predictable from the image alone: train ambiguity predictors without any disagreement labels, from image statistics.
- **Problem:** Obtaining multi-rater data is expensive; if ambiguity is image-determined (low contrast, partial volume, atypical morphology), it can be forecast from single-rater data plus image features.
- **Core Hypothesis (falsifiable):** An ambiguity predictor trained only on image-derived features (no disagreement supervision, using proxies like local gradient structure and model-family variance) predicts held-out multi-rater disagreement maps with high fidelity — ambiguity is an image property, and expensive multi-rater collection is partly replaceable.
- **Why Important:** Would extend ambiguity-aware methods to the vast majority of datasets that have single raters.
- **Why Possibly Novel:** Disagreement-free ambiguity forecasting with multi-rater validation has not been demonstrated.
- **Minimal Experiment:** Build image-feature ambiguity predictors on single-rater data; validate against real disagreement maps on multi-rater test sets.
- **Main Risk:** Ambiguity has non-image components (protocol, ontology); measure the predictable share honestly.

### IDEA-C-0238
- **One-sentence idea:** Re-rank segmentation models by likelihood of the annotator *distribution* instead of distance to consensus — and see whether leaderboards survive.
- **Problem:** Benchmarks score proximity to a synthetic consensus that no annotator produced; a model matching the true distribution of expert opinion may score worse than one matching the artifact.
- **Core Hypothesis (falsifiable):** Ranking models by held-out rater-distribution likelihood reorders consensus-based leaderboards substantially, and the reordering favors models that preserve prediction diversity on ambiguous regions — the current metric selects against faithful ambiguity representation.
- **Why Important:** Metric misalignment at the leaderboard level shapes the whole field's optimization target.
- **Why Possibly Novel:** Distribution-likelihood re-ranking of existing benchmarks has not been published.
- **Minimal Experiment:** Multi-rater test sets; compute both rankings for 10 models; analyze reordering structure.
- **Main Risk:** Likelihood computation requires distributional model choices; use several scoring rules (energy distance, GED) for robustness.

### IDEA-C-0239
- **One-sentence idea:** Determine the minimal number of raters needed for aleatoric-uncertainty training to match the full rater distribution — a rater-budget law.
- **Problem:** Probabilistic segmentation is often trained on one rater's labels with a noise model, hoping to recover population ambiguity; how many real raters that shortcut is worth is unknown.
- **Core Hypothesis (falsifiable):** Distribution-matching quality (against many-rater ground truth) grows with training-rater count following a saturating curve with most gain by 3–4 raters, while single-rater noise-model training plateaus significantly below the 2-rater level — quantifying what synthetic noise cannot buy.
- **Why Important:** Directly prices annotation strategy: how many opinions to purchase per image for uncertainty-quality targets.
- **Why Possibly Novel:** The rater-count dose-response curve for distributional segmentation quality has not been mapped.
- **Minimal Experiment:** Subsample rater counts from many-rater datasets; train distributional models per count; evaluate against full distribution.
- **Main Risk:** Curves may differ by ambiguity level; stratify results by case difficulty.

### IDEA-C-0240
- **One-sentence idea:** Test whether acquisition physics predicts rater disagreement: ambiguity concentrates where SNR/resolution physics says information is absent.
- **Problem:** Disagreement is discussed psychologically (training, style); its physical determinants — where the image genuinely underdetermines the boundary — are unquantified.
- **Core Hypothesis (falsifiable):** Local physics-derived information measures (SNR, PSF-relative structure size, contrast-to-noise) predict rater disagreement maps across modalities with substantial fidelity, and physics-predicted ambiguity transfers zero-shot across datasets of the same modality — disagreement is largely physics, not personality.
- **Why Important:** Physics-grounded ambiguity is computable for free on any image, enabling principled uncertainty floors and annotation triage.
- **Why Possibly Novel:** Physics-to-disagreement predictive modeling has not been attempted systematically.
- **Minimal Experiment:** Compute physics maps for multi-rater datasets; regress disagreement on physics features; test cross-dataset transfer.
- **Main Risk:** Physics metadata is incomplete in public data; estimate physical parameters from images where needed.

### IDEA-C-0241
- **One-sentence idea:** Test whether training on disagreement improves *calibration transfer* to new domains more than it improves accuracy.
- **Problem:** Ambiguity-aware training is usually evaluated on in-domain distribution matching; its most valuable effect may be exporting honest uncertainty to shifted domains.
- **Core Hypothesis (falsifiable):** Models trained with rater-distribution supervision maintain calibration under domain shift substantially better than consensus-trained models at equal in-domain accuracy — ambiguity supervision teaches transferable epistemic humility, measurable as cross-domain calibration gap.
- **Why Important:** Cross-domain calibration is the deployment-critical property; identifying disagreement data as its source would change data-collection priorities.
- **Why Possibly Novel:** The disagreement-training × domain-shift interaction on calibration has not been isolated.
- **Minimal Experiment:** {consensus, distribution}-trained twins evaluated on shifted test sets; compare calibration degradation curves.
- **Main Risk:** Domain shift also changes true ambiguity structure; include multi-rater data in at least one shifted domain.

### IDEA-C-0242
- **One-sentence idea:** Audit self-reported annotation confidence against actual rater consistency — do annotators know when they're unreliable?
- **Problem:** Some pipelines collect per-annotation confidence ratings and weight labels by them, assuming meta-cognitive accuracy nobody has verified for segmentation.
- **Core Hypothesis (falsifiable):** Self-reported confidence correlates weakly with measured intra-rater consistency (test-retest) and inter-rater agreement at the region level, and confidence-weighted label fusion consequently fails to beat unweighted fusion — the meta-annotation is close to uninformative.
- **Why Important:** Confidence collection costs annotator time and is used in fusion; if uninformative, both practices should stop.
- **Why Possibly Novel:** Meta-cognitive validity of annotation confidence in dense labeling is untested.
- **Minimal Experiment:** Collection protocol with confidence ratings plus blinded re-annotation for consistency measurement; correlation and fusion-benefit analysis.
- **Main Risk:** Confidence elicitation design affects validity; test two elicitation formats.

### IDEA-C-0243
- **One-sentence idea:** Decompose what probabilistic segmentation models actually learned: global style modes versus local ambiguity — testing the mode-collapse suspicion.
- **Problem:** Latent-variable segmentation models (Prob U-Net lineage) produce diverse samples, but the diversity may encode global rater-style dimensions while missing independent local ambiguities.
- **Core Hypothesis (falsifiable):** Analysis of trained latent spaces shows sample variation concentrated in few global modes (style-like, spatially coherent offsets) with local ambiguity variance far below the rater distribution's — a structured mode collapse invisible to standard GED evaluation but exposed by locality-resolved diversity metrics.
- **Why Important:** If the flagship ambiguity models represent the wrong kind of ambiguity, downstream risk estimates inherit the distortion.
- **Why Possibly Novel:** Locality-resolved diversity auditing of probabilistic segmentation models has not been performed.
- **Minimal Experiment:** Trained models on multi-rater benchmarks; latent traversal and spatial-covariance analysis of samples vs rater sets; propose locality-resolved metrics.
- **Main Risk:** Findings may vary across model variants; audit 3 architectures before concluding.

### IDEA-C-0244
- **One-sentence idea:** Test agreement-based curricula: training on high-agreement pixels first improves final performance on ambiguous regions.
- **Problem:** Training treats all labeled pixels equally from step one; learning contested labels early may entrench noise-fitting, but nobody has ordered supervision by agreement.
- **Core Hypothesis (falsifiable):** A curriculum that phases in low-agreement pixels late (or reweights by agreement schedule) improves final rater-distribution likelihood and boundary calibration relative to uniform training at matched budgets — disagreement structure is useful *scheduling* information, not just target information.
- **Why Important:** A free training-schedule improvement applicable wherever multi-rater (or predicted-ambiguity, cf. 0237) maps exist.
- **Why Possibly Novel:** Agreement-ordered curricula for dense prediction appear untested.
- **Minimal Experiment:** {uniform, agreement-curriculum, reverse-curriculum} on multi-rater datasets; evaluate distribution likelihood and calibration.
- **Main Risk:** Curriculum effects are often small and schedule-sensitive; pre-register schedules and use multiple seeds.

### IDEA-C-0245
- **One-sentence idea:** Introduce tolerance-aware metrics: ignore errors inside the rater-variance band, and test how method rankings change.
- **Problem:** Metrics penalize deviations from a single reference even where experts themselves span a band; methods may be ranked by their fit to arbitrary within-band positions.
- **Core Hypothesis (falsifiable):** Recomputing benchmark comparisons with rater-variance tolerance bands (errors within the band count as zero) collapses a substantial fraction of published method gaps and reorders rankings — the surviving differences identify methods with genuine beyond-ambiguity improvements.
- **Why Important:** Distinguishes real progress from within-ambiguity noise fitting across the whole evaluation literature.
- **Why Possibly Novel:** Tolerance-band evaluation grounded in measured rater variance is not standard, and its effect on rankings is undocumented.
- **Minimal Experiment:** Construct tolerance bands from multi-rater data; re-evaluate 10 method comparisons with and without bands; quantify ranking stability.
- **Main Risk:** Bands require multi-rater data per benchmark; transfer physics-predicted bands (cf. 0240) where absent, with validation.

### IDEA-C-0246
- **One-sentence idea:** Expose the synthetic-rater fallacy: augmenting one rater's labels does not reproduce real disagreement structure.
- **Problem:** Papers simulate multi-rater data by perturbing single-rater labels (morphological jitter, boundary noise); methods validated on such simulations may fail on real disagreement.
- **Core Hypothesis (falsifiable):** Real rater disagreement differs from standard simulations in measurable structure (spatial correlation length, style consistency across images, dependence on image content), and ambiguity-modeling methods ranked on simulated raters reorder substantially when evaluated on real multi-rater data — simulation validity fails where it matters.
- **Why Important:** A validity audit protecting the ambiguity-modeling literature from building on artifacts.
- **Why Possibly Novel:** Simulation-vs-real disagreement structural comparison with method re-ranking has not been published.
- **Minimal Experiment:** Fit structural statistics on real vs simulated rater sets; re-rank 4 methods across both; document divergences.
- **Main Risk:** Some simulation schemes may pass; the outcome is a validated simulator specification either way.

### IDEA-C-0247
- **One-sentence idea:** Measure how much disagreement is ontology mismatch: raters disagree on class definitions, not pixels — and explicit ontology resolution recovers it.
- **Problem:** Disagreement statistics blend boundary ambiguity with definitional divergence (does "tumor" include necrotic core? peritumoral edema?), which is fixable by specification rather than modeling.
- **Core Hypothesis (falsifiable):** Re-annotation with an explicit, adjudicated ontology reduces inter-rater disagreement by a large measurable fraction on definition-sensitive structures and by little on definition-stable ones — quantifying the recoverable-by-specification share of "ambiguity" the field currently models as noise.
- **Why Important:** The cheapest path to better labels may be documentation, not algorithms; the share should be known per task.
- **Why Possibly Novel:** Definitional-vs-perceptual disagreement decomposition via controlled re-annotation is rarely if ever quantified.
- **Minimal Experiment:** Two-phase annotation study (free protocol vs explicit ontology) on definition-sensitive and stable structures; disagreement change analysis.
- **Main Risk:** Ontology writing itself takes expert consensus effort; scope to 2–3 structures.

### IDEA-C-0248
- **One-sentence idea:** Identify expertise signatures: expert-vs-novice disagreement has distinct spatial structure usable to weight crowd-sourced labels without identity labels.
- **Problem:** Crowd labeling mixes skill levels; existing quality weighting uses agreement with majority, which punishes correct minority experts on hard cases.
- **Core Hypothesis (falsifiable):** Expert and novice raters differ in reproducible spatial signatures (error concentration at high-curvature boundaries, handling of low-contrast regions, consistency across similar cases), and an unsupervised signature-based skill estimator outperforms majority-agreement weighting in recovering expert consensus on hard cases.
- **Why Important:** Better skill inference upgrades every crowd-sourced medical labeling effort, especially on the difficult cases where majority weighting fails.
- **Why Possibly Novel:** Spatial-signature-based skill inference (rather than agreement-based) is undeveloped for segmentation.
- **Minimal Experiment:** Datasets with known rater expertise; learn signatures; evaluate blinded skill recovery and fusion quality on hard-case subsets.
- **Main Risk:** Expertise-labeled multi-rater data is scarce; may need a small controlled annotation study.

### IDEA-C-0249
- **One-sentence idea:** Stress-test losses under multimodal ground truth: standard objectives assume unimodal truth and fail predictably when raters split between discrete hypotheses.
- **Problem:** When ambiguity is discrete (vessel branches left or right; lesion is one structure or two), the rater distribution is multimodal — and pixel-wise losses trained on it converge to averages that match no rater.
- **Core Hypothesis (falsifiable):** On constructed and natural multimodal-truth cases, models trained with standard losses produce anatomically invalid averaged solutions at high rates, while distribution-aware training preserves modes — with the invalid-average rate predictable from the modes' spatial separation.
- **Why Important:** Averaged solutions are silently absurd (blended branches, phantom bridges) and clinically dangerous; the failure condition should be characterized, not anecdotal.
- **Why Possibly Novel:** Multimodality as a formal failure condition of segmentation losses has not been characterized with predictive structure.
- **Minimal Experiment:** Construct mode-separation ladders (synthetic + curated real); measure invalid-average rates across losses and distribution-aware alternatives.
- **Main Risk:** Detecting "anatomically invalid" needs task-specific validity rules; start with objective topological criteria.

### IDEA-C-0250
- **One-sentence idea:** Test whether down-weighting ambiguous pixels helps in-domain but hurts out-of-domain — ambiguous regions carry domain-general information.
- **Problem:** A common trick discounts high-disagreement pixels during training as noise; those regions may be where models learn robust, transferable boundary reasoning.
- **Core Hypothesis (falsifiable):** Ambiguity-down-weighted training improves in-domain consensus metrics but degrades cross-domain transfer relative to uniform training — an in/out-of-domain sign flip demonstrating that "noisy" pixels were carrying generalizable signal.
- **Why Important:** A widespread practice may be quietly trading robustness for benchmark points; the trade-off deserves documentation.
- **Why Possibly Novel:** The transfer consequence of ambiguity down-weighting has not been examined.
- **Minimal Experiment:** {uniform, down-weighted} twins × 3 datasets; in-domain vs cross-domain evaluation; interaction test.
- **Main Risk:** Effect may vary with shift type; test both appearance and population shifts.

### IDEA-C-0251
- **One-sentence idea:** Perform annotation forensics on session dynamics: rater fatigue and drift measurably change boundary quality within annotation sessions.
- **Problem:** Ground truth is treated as time-invariant, but annotation happens in long sessions where attention, calibration, and criteria drift — a structured noise source nobody models.
- **Core Hypothesis (falsifiable):** Within-session annotation order predicts measurable changes in boundary statistics (smoothness, tightness, detail level) and agreement with other raters, and order-aware label correction improves downstream training relative to order-blind use — session dynamics are a recoverable label-noise component.
- **Why Important:** If session position is a noise factor, both dataset construction (session design) and label modeling should account for it — a fully preventable quality loss.
- **Why Possibly Novel:** Temporal annotation-session analysis for segmentation quality is essentially unexplored.
- **Minimal Experiment:** Datasets or new collections with annotation timestamps; regress label statistics on session position; test order-aware corrections.
- **Main Risk:** Timestamped annotation data is rare; a small purpose-run annotation study may be required.

### IDEA-C-0252
- **One-sentence idea:** Show that adjudicated consensus is statistically a new rater — group processes create label distributions unlike any individual's.
- **Problem:** Consensus meetings (panel adjudication) are presumed to yield "better truth"; group dynamics (anchoring, seniority deference) may instead produce a distinct style whose properties are unknown.
- **Core Hypothesis (falsifiable):** Adjudicated labels differ from all individual raters and from their statistical fusion in measurable, consistent directions (e.g., systematically tighter boundaries, fewer marked ambiguities), and models trained on adjudicated vs fused labels behave differently on ambiguous regions — adjudication is a labeling intervention with its own signature, not a noise reducer.
- **Why Important:** Many gold-standard datasets are adjudicated; understanding what adjudication does to label statistics matters for interpreting everything trained on them.
- **Why Possibly Novel:** Statistical characterization of adjudication as a process (vs fusion) appears absent.
- **Minimal Experiment:** Datasets retaining both individual and adjudicated labels; systematic difference analysis; twin-training comparison.
- **Main Risk:** Suitable datasets retaining pre-adjudication labels are uncommon; partner datasets or small studies may be needed.

### IDEA-C-0253
- **One-sentence idea:** Quantify how well test-time augmentation disagreement aligns with human disagreement — a free surrogate for ambiguity maps.
- **Problem:** Multi-rater maps are expensive; prediction variability under input transforms is free, but its correspondence to human ambiguity is asserted rather than measured.
- **Core Hypothesis (falsifiable):** Spatial correlation between TTA-disagreement maps and real rater-disagreement maps is substantial but structured: high where ambiguity is appearance-driven, near zero where it is definitional — yielding a validated map of when the free surrogate is trustworthy.
- **Why Important:** A validated surrogate would extend every disagreement-based technique (0233, 0244, 0245) to single-rater datasets at zero annotation cost.
- **Why Possibly Novel:** The TTA-vs-human disagreement correspondence has not been quantitatively mapped and conditioned.
- **Minimal Experiment:** Compute both maps on multi-rater benchmarks; correlation analysis stratified by ambiguity type (cf. 0247's decomposition).
- **Main Risk:** Correspondence may be model-dependent; evaluate across 3 architectures.

### IDEA-C-0254
- **One-sentence idea:** Develop annotation budget theory: concentrate multi-rater spending on boundary bands and get full-distribution information at a fraction of cost.
- **Problem:** Multi-rater annotation multiplies cost over entire images although raters agree on most interior pixels — the informative disagreement lives in thin bands.
- **Core Hypothesis (falsifiable):** A protocol collecting single-rater interiors plus multi-rater boundary bands recovers the full-image rater-distribution information (validated against complete multi-rater data) at a small fraction of annotation time, with negligible loss in downstream ambiguity-model quality.
- **Why Important:** Makes ambiguity-aware datasets affordable, unlocking distributional methods for routine collection.
- **Why Possibly Novel:** Spatially targeted multi-rater budgeting with information-recovery validation has not been formalized.
- **Minimal Experiment:** Simulate the protocol by masking existing multi-rater data; measure information recovery and downstream model equivalence; validate timing with a small annotation study.
- **Main Risk:** Band placement requires an initial boundary estimate; test sensitivity to its quality.

### IDEA-C-0255
- **One-sentence idea:** Compute model-rater agreement matrices to discover whose style each trained model actually learned — and what determines the allegiance.
- **Problem:** Models trained on merged multi-source labels end up closer to some raters than others, with unknown determinants (data volume? order? style simplicity?) and unexamined consequences.
- **Core Hypothesis (falsifiable):** Trained models cluster tightly with specific raters rather than the consensus centroid, allegiance is predicted primarily by rater label volume and style smoothness (simpler styles are preferentially learned), and allegiance is manipulable by reweighting — style capture is lawful and controllable.
- **Why Important:** Reveals a hidden dimension of every trained segmenter (whose opinion it encodes) with fairness and consistency implications across deployments.
- **Why Possibly Novel:** Model-rater allegiance as a measured, predicted, and controlled phenomenon is new.
- **Minimal Experiment:** Train on multi-rater mixtures with controlled volumes/styles; compute agreement matrices; test the predictive and control claims.
- **Main Risk:** Confounds between rater volume and case difficulty; controlled mixture construction addresses this.

### IDEA-C-0256
- **One-sentence idea:** Validate rater-conditioned segmentation: a model that reproduces *individual* raters on demand, tested as a rater simulator.
- **Problem:** Personalization claims exist, but no one has rigorously tested whether conditioning on rater identity yields outputs statistically indistinguishable from that rater's real annotations.
- **Core Hypothesis (falsifiable):** Rater-conditioned models pass discrimination tests (classifiers cannot distinguish real vs simulated annotations of a given rater beyond chance on held-out cases) for style-dominant raters, but fail for raters whose behavior depends on private knowledge — mapping the limits of rater simulation.
- **Why Important:** Valid rater simulators would enable annotation cost reduction, disagreement forecasting, and consistency auditing; invalid ones should be documented before adoption.
- **Why Possibly Novel:** Adversarial-discrimination validation of rater simulation has not been applied.
- **Minimal Experiment:** Train conditioned models on multi-rater data; run discrimination tests per rater; characterize pass/fail correlates.
- **Main Risk:** Discrimination tests need enough per-rater data; select datasets accordingly.

### IDEA-C-0257
- **One-sentence idea:** Model ordinal ambiguity in grading tasks as biological continuum information: adjacent-grade disagreement predicts outcomes better than forced consensus grades.
- **Problem:** Tumor/severity grading treats inter-rater disagreement as error and forces consensus, though adjacent-grade splits may encode genuine biological intermediacy with prognostic content.
- **Core Hypothesis (falsifiable):** In datasets with outcomes, the rater-grade distribution (e.g., 2-vs-3 split ratios) adds prognostic value beyond the consensus grade, and models trained to predict grade distributions outperform consensus-grade models on outcome prediction — disagreement carries clinical signal that consensus destroys.
- **Why Important:** Would change grading-label practice from consensus-forcing to distribution-preserving, with direct clinical value.
- **Why Possibly Novel:** Disagreement-as-prognostic-signal has scattered clinical hints but no ML formalization and test.
- **Minimal Experiment:** Public grading datasets with outcomes; compare prognostic models using consensus vs distributional grade targets.
- **Main Risk:** Outcome-linked multi-rater grading data is limited; pathology collections are the most feasible.

### IDEA-C-0258
- **One-sentence idea:** Bake-off disagreement against confident-learning for label-error detection: which finds real annotation errors better?
- **Problem:** Label-error detection uses model-loss-based methods (confident learning) on single labels; where multi-rater data exists, disagreement offers an independent detector — the two have never been directly compared on verified errors.
- **Core Hypothesis (falsifiable):** On datasets with seeded and expert-verified natural label errors, rater disagreement detects definitional and boundary errors better, while loss-based methods detect slips (wrong structure, missed instance) better — complementary detectors whose union dominates either, with a characterized division of labor.
- **Why Important:** Label auditing is becoming standard practice; an evidence-based detector selection guide is directly usable.
- **Why Possibly Novel:** Head-to-head detector comparison on verified segmentation label errors has not been published.
- **Minimal Experiment:** Seed error types into multi-rater datasets plus verify natural errors; run both detector families; per-type detection analysis.
- **Main Risk:** Seeded errors may not represent natural ones; the verified-natural arm is essential.

### IDEA-C-0259
- **One-sentence idea:** Audit the "within inter-rater variability" safety argument: models inside the variance band can still be systematically biased in ways no rater is.
- **Problem:** Regulatory and paper claims argue safety by showing model-vs-truth differences comparable to rater-vs-rater differences — an argument that ignores error *structure*.
- **Core Hypothesis (falsifiable):** Models can match rater-level error magnitude while exhibiting bias structures absent from any rater (consistent directional volumetry bias, systematic subgroup-dependent errors), constructible in practice and detectable only by structure-aware analysis — the magnitude-based safety argument is formally insufficient and empirically violated by real models.
- **Why Important:** This argument pattern underlies clearance claims; demonstrating its insufficiency with real cases would raise the evidential bar field-wide.
- **Why Possibly Novel:** A formal and empirical critique of the variability-band safety argument has not been assembled.
- **Minimal Experiment:** For several benchmark models within rater-variance bands, test for structural biases (directional, subgroup, correlated-across-cases) that rater sets lack.
- **Main Risk:** Findings could be misread as blanket anti-model claims; frame precisely around argument sufficiency.

### IDEA-C-0260
- **One-sentence idea:** Build a rater embedding space: disagreement patterns transfer across tasks, so a rater's behavior on one structure predicts their behavior on others.
- **Problem:** Each annotation project treats rater behavior as unknown; if rater style is a stable trait expressible in a low-dimensional space, it is estimable once and reusable across tasks.
- **Core Hypothesis (falsifiable):** Rater embeddings fitted on one set of structures predict pairwise disagreement patterns and style offsets on held-out structures significantly above baseline — rater style is low-dimensional and task-transferable, enabling style-corrected fusion for new tasks from historical rater data.
- **Why Important:** Institutional annotation programs could maintain rater profiles that improve every subsequent labeling project's fusion and budgeting.
- **Why Possibly Novel:** Cross-task rater-style transfer has not been quantified.
- **Minimal Experiment:** Multi-structure multi-rater datasets; fit embeddings per rater on structure subset A; predict disagreement statistics on subset B.
- **Main Risk:** Style may be structure-specific for some raters; the embedding residual quantifies this honestly.

---

## C10. Foundation-model tokenization / resolution / memory artifacts (IDEA-C-0261 … 0288)

### IDEA-C-0261
- **One-sentence idea:** Measure grid-phase sensitivity: segmentation quality oscillates with the alignment between object boundaries and the ViT patch grid.
- **Problem:** Patchification imposes a fixed 14/16-pixel lattice; whether performance depends periodically on where boundaries fall within a patch is unmeasured — and it would constitute an unacknowledged noise source in every ViT benchmark result.
- **Core Hypothesis (falsifiable):** Sub-patch translations of the input produce periodic IoU oscillations with period equal to patch size, amplitude largest for thin structures, and negligible in CNN baselines — quantifying an aliasing artifact intrinsic to patch tokenization.
- **Why Important:** A periodic artifact means results depend on arbitrary image framing; it also motivates anti-aliased or shifted-ensemble inference with predictable gains.
- **Why Possibly Novel:** Grid-phase performance analysis for ViT dense prediction has not been reported.
- **Minimal Experiment:** Evaluate ViT and CNN segmenters under 0–16px translation sweeps; Fourier-analyze the score-vs-shift curves; stratify by structure width.
- **Main Risk:** Translation requires padding/cropping care to avoid confounding content changes.

### IDEA-C-0262
- **One-sentence idea:** Map the systematic spatial distortion field introduced by position-embedding interpolation at inference resolutions above pretraining.
- **Problem:** High-res inference interpolates learned position embeddings, treating it as harmless; the induced spatial error structure has never been charted.
- **Core Hypothesis (falsifiable):** Dense-prediction error at upscaled resolutions exhibits a reproducible spatial pattern (radial or grid-structured, per interpolation scheme) that grows with the resolution ratio, is absent at native resolution, and is reduced by resolution-aware embedding schemes — a measurable, correctable artifact.
- **Why Important:** High-res inference from low-res-pretrained backbones is universal practice in dense prediction; its spatial cost should be known.
- **Why Possibly Novel:** Spatially resolved characterization of interpolation error (as opposed to aggregate score drops) is missing.
- **Minimal Experiment:** Position-controlled synthetic targets plus natural data at 1–4× resolution ratios; per-position error maps across interpolation schemes.
- **Main Risk:** Confounds with object-scale change at higher resolution; the synthetic position-controlled arm isolates the embedding effect.

### IDEA-C-0263
- **One-sentence idea:** Predict where ViT artifact (high-norm) tokens will appear from input statistics, before the forward pass.
- **Problem:** Large ViTs repurpose low-information patches as computation scratchpads (high-norm tokens), corrupting local features at unpredictable-seeming positions.
- **Core Hypothesis (falsifiable):** Artifact-token locations are predictable from cheap local input statistics (patch variance, similarity to neighbors) with high accuracy across models, implying the model selects scratch locations by input information content — enabling pre-hoc detection and targeted feature repair for dense tasks.
- **Why Important:** Converts a documented curiosity into an operational tool: know in advance which feature positions to distrust.
- **Why Possibly Novel:** Pre-forward prediction of artifact locations and its use for dense-task repair have not been shown.
- **Minimal Experiment:** Collect artifact positions across models/images; train the statistics-based predictor; evaluate dense-task gains from predicted-position repair.
- **Main Risk:** Register-token-trained models may relocate artifacts; test across model generations.

### IDEA-C-0264
- **One-sentence idea:** Audit thin-structure information survival through patch embedding: what is destroyed at tokenization versus recoverable downstream.
- **Problem:** Structures thinner than the patch stride (vessels, wires, fissures) may lose identity at the very first layer, bounding all downstream processing — but the loss has not been isolated from later-stage limitations.
- **Core Hypothesis (falsifiable):** Probes on post-embedding tokens show thin-structure detectability dropping sharply below a width threshold tied to stride and embedding filters, this threshold propagates unchanged to final-layer features (nothing downstream recovers it), and sub-stride convolutional stems shift the threshold predictably — the bottleneck is the tokenizer.
- **Why Important:** Identifies which anatomy classes are structurally unreachable for given tokenizer settings, before training anything.
- **Why Possibly Novel:** Layer-of-loss attribution for thin structures (tokenizer vs downstream) has not been established.
- **Minimal Experiment:** Width-ladder synthetic structures + vessel data; probe detectability at embedding and final layers across stem designs.
- **Main Risk:** Learned embeddings differ across pretrained models; test several checkpoints to separate architecture from weights.

### IDEA-C-0265
- **One-sentence idea:** Detect and quantify window-boundary seams in dense predictions from windowed-attention architectures.
- **Problem:** Window-partitioned attention (Swin-style) processes space in blocks; whether block borders leave statistical seams in dense outputs — and whether shifted windows fully remove them — is untested.
- **Core Hypothesis (falsifiable):** Prediction error and feature statistics show measurable discontinuities aligned with window boundaries (detectable by seam-alignment statistics against random-offset nulls), reduced but not eliminated by window shifting, and absent in global-attention twins — a quantifiable architectural artifact.
- **Why Important:** Seam artifacts bias boundary placement at architecture-determined positions — an error source no benchmark currently accounts for.
- **Why Possibly Novel:** Seam-statistics auditing of windowed architectures has not been published.
- **Minimal Experiment:** Aggregate error fields in window-relative coordinates across many images; test alignment significance; compare architectures.
- **Main Risk:** Effects may be small at convergence; use high-powered aggregation across large test sets.

### IDEA-C-0266
- **One-sentence idea:** Fit the error-accumulation law of memory-based video segmentation: how propagated errors grow with sequence length and what resets them.
- **Problem:** Streaming/memory architectures for video segmentation drift over long sequences, but the drift's functional form and its dependence on memory design are uncharacterized — deployments cannot predict when re-initialization is needed.
- **Core Hypothesis (falsifiable):** Mask error grows with frames-since-anchor following a characteristic curve (linear vs saturating) whose parameters are set by memory capacity and update rules, with occlusion events acting as measurable shock terms — yielding a validated re-anchoring policy (when to ask for a new prompt/frame) from the fitted law.
- **Why Important:** Long-video medical and surgical use requires drift budgets and re-anchoring schedules grounded in measurement.
- **Why Possibly Novel:** Drift-law fitting with event decomposition for memory-based segmentation has not been formalized.
- **Minimal Experiment:** Long-sequence evaluation across memory architectures; fit growth curves; validate re-anchoring policies derived from them.
- **Main Risk:** Public long-sequence densely annotated video is limited; use semi-automatic ground truth with verification.

### IDEA-C-0267
- **One-sentence idea:** Audit token-pruning/merging efficiency methods for boundary bias: dropped tokens are disproportionately boundary tokens.
- **Problem:** Token reduction methods select "redundant" tokens by similarity/attention criteria that plausibly sacrifice exactly the high-information boundary regions dense tasks need — evaluated so far mostly on classification.
- **Core Hypothesis (falsifiable):** Under standard token-merging/pruning, the retained-token spatial distribution systematically under-represents object boundaries, dense-task degradation concentrates in boundary metrics (region metrics nearly unaffected), and boundary-aware retention criteria recover most of the loss at equal token budgets.
- **Why Important:** Efficiency methods are being adopted for dense inference with classification-based evidence; their dense-task cost structure should be exposed first.
- **Why Possibly Novel:** Spatially resolved auditing of token-reduction for dense prediction is missing.
- **Minimal Experiment:** Apply 3 token-reduction methods to segmentation models; map retained-token distributions vs boundaries; metric-decomposed degradation analysis.
- **Main Risk:** Method-specific behaviors may diverge; the audit framework itself is the durable contribution.

### IDEA-C-0268
- **One-sentence idea:** Test cross-image contamination in packed native-resolution training (NaViT-style): do packed images leak into each other's representations?
- **Problem:** Packing multiple images into one sequence relies on attention masking; imperfections (shared normalization statistics, positional interactions, implementation subtleties) could leak information across packed images, corrupting both training statistics and evaluation.
- **Core Hypothesis (falsifiable):** Controlled probes (predicting properties of image B from tokens of image A within a pack) detect above-chance leakage in packed training pipelines, leakage scales with pack density, and its removal (stricter isolation) measurably changes learned features — quantifying an unexamined artifact of a spreading practice.
- **Why Important:** Packing is becoming default for efficiency; silent leakage would distort pretraining and any evaluation using packed inference.
- **Why Possibly Novel:** Leakage auditing for packed-sequence vision training has not been reported.
- **Minimal Experiment:** Train small packed vs isolated models; run cross-image probes; compare feature and downstream behavior.
- **Main Risk:** Leakage may be implementation-specific; audit at least two independent codebases.

### IDEA-C-0269
- **One-sentence idea:** Test whether anti-aliased patchification (strided-conv tokenizers violate Nyquist) changes ViT texture bias and dense robustness.
- **Problem:** Patch embedding is a stride-16 convolution — a textbook aliasing operation — yet aliasing's contribution to ViT behavior (texture sensitivity, shift instability) has not been isolated at the tokenizer.
- **Core Hypothesis (falsifiable):** Adding proper low-pass filtering before patch sampling (fixed, non-learned) reduces measured shift inconsistency and high-frequency texture reliance of ViT features at equal accuracy, with the largest dense-task gains on high-frequency-content domains (pathology, bone) — aliasing at tokenization is a causal contributor to known ViT pathologies.
- **Why Important:** A one-layer, principled fix testable against multiple documented artifacts (0261, 0071) at once.
- **Why Possibly Novel:** Anti-aliasing is studied for CNN downsampling; the ViT-tokenizer version with dense endpoints is essentially untested.
- **Minimal Experiment:** Train twin ViTs {standard, anti-aliased tokenizer} at modest scale; run shift-consistency, cue-conflict, and dense-task batteries.
- **Main Risk:** Retraining requirement limits scale; complement with fine-tuning-only conversions of existing checkpoints.

### IDEA-C-0270
- **One-sentence idea:** Map how high-resolution fine-tuning redistributes effective receptive fields non-uniformly across layers — and what that predicts about which tasks benefit.
- **Problem:** "Fine-tune at higher resolution" is standard advice with unknown internal consequences: which layers adapt their spatial scope, and why do some tasks gain while others don't?
- **Core Hypothesis (falsifiable):** Under high-res fine-tuning, ERF growth concentrates in specific layer bands (late attention layers) while early layers stay fixed, and the per-task benefit of high-res fine-tuning is predicted by whether the task's required context falls in the adapted band — an internal-change account with predictive power.
- **Why Important:** Converts a costly folk practice into a predictable intervention: measure the task's context requirement, know whether high-res fine-tuning will pay.
- **Why Possibly Novel:** Layer-resolved ERF dynamics under resolution transfer have not been mapped.
- **Minimal Experiment:** ERF measurement per layer before/after high-res fine-tuning across models; correlate task benefits with context-requirement estimates.
- **Main Risk:** ERF measures are noisy; use gradient-based and occlusion-based estimates jointly.

### IDEA-C-0271
- **One-sentence idea:** Develop the dense-readout theory of pooling choices: CLS-token vs mean pooling during pretraining determines what spatial information survives into patch tokens.
- **Problem:** Pretraining readout (CLS vs pooled) shapes gradient flow into patch tokens differently, plausibly controlling their dense-task usability — an architecture choice never analyzed for its dense consequences.
- **Core Hypothesis (falsifiable):** Models pretrained with mean pooling retain measurably more locally discriminative patch information than CLS-trained twins at equal global accuracy (probe-verified), and the difference predicts frozen-feature dense-task performance — a pretraining-design rule for dense-friendly backbones.
- **Why Important:** A zero-cost pretraining choice with lasting dense-task consequences should be an informed decision, not a default.
- **Why Possibly Novel:** Controlled CLS-vs-pooling twins evaluated for dense information content are not in the literature.
- **Minimal Experiment:** Pretrain twin models differing only in readout; probe patch-token local information; evaluate frozen dense transfer.
- **Main Risk:** Requires controlled pretraining; modest scale acceptable since the claim is comparative.

### IDEA-C-0272
- **One-sentence idea:** Characterize task-dependent quantization sensitivity: low-bit inference damages dense predictions at boundaries first, and more than classification.
- **Problem:** Quantization is validated on classification accuracy and adopted wholesale for dense models; the spatial structure of quantization damage is unknown.
- **Core Hypothesis (falsifiable):** Under int8/int4 quantization, dense-task degradation concentrates in boundary bands and small structures (region interiors robust), the boundary damage exceeds matched classification damage at equal bit-width, and sensitivity localizes to specific layers (normalization-adjacent, high-dynamic-range) — yielding a dense-task-specific quantization recipe.
- **Why Important:** Edge deployment of medical segmentation increasingly relies on quantization validated for the wrong task family.
- **Why Possibly Novel:** Spatially resolved quantization-damage analysis for dense prediction is unreported.
- **Minimal Experiment:** Quantize segmentation models at graded bit-widths; boundary-band vs interior metric decomposition; layer-sensitivity scan.
- **Main Risk:** Results vary with quantization scheme; test PTQ and QAT variants.

### IDEA-C-0273
- **One-sentence idea:** Audit window-position bias in sliding-window inference: prediction quality varies systematically between window centers and edges, hidden by overlap blending.
- **Problem:** 3D/high-res pipelines predict in overlapping windows and blend; the blend obscures whether voxels near window edges receive systematically worse predictions — and whether blending weights are anywhere near optimal.
- **Core Hypothesis (falsifiable):** Per-voxel error conditioned on within-window position shows a reproducible center-to-edge quality gradient (context truncation effect), Gaussian blending under-corrects it, and empirically fitted position-dependent weights improve final accuracy at zero model change — a free, measurable pipeline win.
- **Why Important:** Sliding-window inference is universal in medical segmentation; its internal quality structure has never been audited.
- **Why Possibly Novel:** Window-relative error profiling and empirical blend optimization are absent from standard practice.
- **Minimal Experiment:** Log per-voxel error in window coordinates across datasets/models; fit optimal blend weights; validate gains.
- **Main Risk:** Gradients may be architecture-specific; profile CNN and transformer backbones separately.

### IDEA-C-0274
- **One-sentence idea:** Test spacing-aware 3D tokenization: matching token shape to voxel anisotropy beats isotropic-cube tokenization at equal token budgets.
- **Problem:** 3D transformers tokenize with isotropic cubes although medical voxels are strongly anisotropic (e.g., 0.7×0.7×5 mm) — the token grid mismatches the data's information geometry.
- **Core Hypothesis (falsifiable):** Tokenizers whose token aspect ratio tracks physical voxel spacing outperform isotropic tokenization at matched token counts, with the advantage proportional to anisotropy ratio and concentrated in through-plane boundary accuracy — information-per-token, not token count, is the binding resource.
- **Why Important:** A principled tokenizer-design rule for all 3D medical transformers, currently set by convention.
- **Why Possibly Novel:** Physical-spacing-conditioned tokenization has not been isolated as a controlled variable.
- **Minimal Experiment:** Token-shape grids across datasets of varying anisotropy at fixed budgets; through-plane-resolved evaluation.
- **Main Risk:** Interacts with resampling choices upstream; hold resampling fixed and report the pipeline dependence.

### IDEA-C-0275
- **One-sentence idea:** Estimate the information capacity of memory tokens in streaming vision models and test whether long-video forgetting is capacity saturation.
- **Problem:** Streaming architectures compress history into fixed memory tokens; degradation on long videos is observed but not attributed — capacity limit, interference, or drift?
- **Core Hypothesis (falsifiable):** Recoverable historical information (probed from memory tokens) saturates at a measurable capacity in object-count/appearance bits, forgetting onset in long videos coincides with reaching that capacity (manipulable by scene complexity), and increasing memory tokens shifts onset predictably — saturation, not drift, is the binding mechanism.
- **Why Important:** Correct attribution dictates the fix: bigger memory vs better update rules vs periodic re-anchoring.
- **Why Possibly Novel:** Information-capacity probing of vision memory mechanisms with onset prediction is new.
- **Minimal Experiment:** Controlled synthetic video with parameterized scene complexity; memory probes over time; onset-vs-capacity analysis across memory sizes.
- **Main Risk:** Synthetic complexity may not map to real scenes; validate onset predictions on natural long videos.

### IDEA-C-0276
- **One-sentence idea:** Test whether learned feature-upsampling methods add image information or merely impose learned priors — hallucinating plausible but ungrounded boundary detail.
- **Problem:** Feature up-samplers (FeatUp-style) sharpen coarse backbone features impressively; whether the added detail reflects the specific image or dataset-prior interpolation is unresolved and consequential for medical use.
- **Core Hypothesis (falsifiable):** On stimuli where local image evidence contradicts dataset priors (constructed boundary displacements), learned up-samplers place detail according to priors rather than evidence at a measurable rate, while evidence-guided baselines (bilateral/guided filtering) follow the image — the sharpness is partly hallucination, quantifiable per method.
- **Why Important:** Prior-driven boundary detail in medical pipelines is a silent fabrication risk exactly where it looks most convincing.
- **Why Possibly Novel:** Evidence-vs-prior adjudication tests for feature upsampling have not been designed or run.
- **Minimal Experiment:** Construct evidence-prior conflict stimuli; compare upsampler outputs against both hypotheses; quantify hallucination rates per method.
- **Main Risk:** Constructed conflicts must remain realistic; use physically plausible boundary manipulations.

### IDEA-C-0277
- **One-sentence idea:** Determine the role of attention sinks in spatial tasks: does the first-token/artifact sink protect or degrade dense predictions?
- **Problem:** Attention-sink behavior (mass parked on specific tokens) is characterized for LLMs; vision-transformer dense tasks may depend on sinks differently — removal could either free capacity or destabilize attention.
- **Core Hypothesis (falsifiable):** Manipulating sink availability (providing/blocking dedicated sink tokens) causes systematic changes in dense-prediction quality with a consistent sign across architectures, and per-head analysis identifies which attention heads need sinks — settling whether sinks are parasitic or load-bearing for spatial computation.
- **Why Important:** Sink handling is now a design decision (register tokens, attention modifications); dense-task guidance is absent.
- **Why Possibly Novel:** Causal sink manipulation with dense-task endpoints has not been reported.
- **Minimal Experiment:** Sink-availability interventions on segmentation ViTs (train-time and inference-time); dense metric and attention-pattern analysis.
- **Main Risk:** Train-time and inference-time manipulations may disagree; report both regimes explicitly.

### IDEA-C-0278
- **One-sentence idea:** Fit patch-size scaling laws for dense tasks: error versus patch size follows task-specific exponents predictable from object-size distributions.
- **Problem:** Patch size is chosen from a small conventional menu (8/14/16/32) without a quantitative model of its task-dependent cost — despite being the strongest single lever on dense-task compute.
- **Core Hypothesis (falsifiable):** Dense-task error follows a power law in patch size whose exponent is predicted by the dataset's object-size and boundary-density statistics, enabling per-task selection of the compute-optimal patch size from data statistics alone — validated by held-out task prediction.
- **Why Important:** Would replace convention with a two-statistic design calculation covering the field's most consequential resolution choice.
- **Why Possibly Novel:** Patch-size scaling behavior for dense tasks has not been fitted or connected to dataset statistics.
- **Minimal Experiment:** Patch-size sweeps (8–32) across 6 dense tasks at controlled compute; fit exponents; test prediction on 2 held-out tasks.
- **Main Risk:** Patch size interacts with pretraining availability; use consistently pretrained or from-scratch model families.

### IDEA-C-0279
- **One-sentence idea:** Probe resolution-conditional behavior: multi-scale-trained models secretly infer input resolution and switch strategies, breaking scale-invariance assumptions.
- **Problem:** Multi-resolution training is assumed to produce scale-robust single strategies; models may instead learn resolution detection plus resolution-specific behaviors — with different failure modes at unseen resolutions.
- **Core Hypothesis (falsifiable):** Input resolution is decodable from intermediate features of multi-scale-trained models with high accuracy, behavioral signatures (boundary style, context usage) cluster by resolution rather than varying continuously, and performance at interpolated (untrained) resolutions dips below both neighbors — strategy switching, not invariance.
- **Why Important:** Deployment at arbitrary resolutions relies on interpolation behavior that strategy-switching models don't have.
- **Why Possibly Novel:** Resolution-strategy probing of multi-scale training is unexplored.
- **Minimal Experiment:** Resolution probes on features; behavioral clustering across a fine resolution grid including untrained values; dip detection.
- **Main Risk:** Resolution decodability alone is weak evidence; the untrained-resolution dip is the decisive prediction.

### IDEA-C-0280
- **One-sentence idea:** Benchmark dense-prediction extrapolation to larger images as a function of position-encoding type — relative encodings should extrapolate, absolute should fail; does reality comply?
- **Problem:** Position-encoding folklore (relative extrapolates better) comes from language modeling; dense visual prediction stresses encodings differently (2D structure, boundary precision) and lacks a dedicated extrapolation benchmark.
- **Core Hypothesis (falsifiable):** On a controlled dense-extrapolation suite (train small, test large), encoding families separate cleanly, but the ordering deviates from language-modeling folklore in measurable ways (e.g., learned-absolute with 2D-aware interpolation outperforming naive relative variants for boundary precision) — vision needs its own extrapolation rules.
- **Why Important:** Position-encoding choices for vision are currently justified by NLP evidence; dense tasks deserve direct measurement.
- **Why Possibly Novel:** A dedicated dense-task extrapolation benchmark across encoding families does not exist.
- **Minimal Experiment:** Train matched models with 5 encoding types at fixed resolution; evaluate at 1–4× sizes on synthetic and natural dense tasks.
- **Main Risk:** Encoding implementations differ in auxiliary details; keep every other component frozen.

### IDEA-C-0281
- **One-sentence idea:** Audit stage-wise aliasing in hierarchical vision transformers: each downsampling stage re-introduces CNN-style shift instability that global-attention models avoid.
- **Problem:** Hierarchical designs (patch merging, strided reductions) repeat the aliasing operation multiple times; the accumulated shiftability cost across stages, and its dense-task consequence, is unmeasured.
- **Core Hypothesis (falsifiable):** Shift-consistency of features degrades multiplicatively across downsampling stages (measurable per stage), hierarchical models show worse dense-prediction shift stability than isotropic ViTs at matched accuracy, and per-stage anti-aliasing recovers most of the gap — aliasing compounds through the hierarchy.
- **Why Important:** Hierarchies dominate dense-prediction backbones; their stability cost structure should inform the hierarchy-vs-isotropic choice.
- **Why Possibly Novel:** Stage-resolved aliasing accounting in vision transformers is not in the literature.
- **Minimal Experiment:** Per-stage shift-consistency measurement across architectures; anti-aliased variants; dense stability comparison.
- **Main Risk:** Stage effects entangle with capacity differences; use surgically modified twins.

### IDEA-C-0282
- **One-sentence idea:** Test the attention-entropy-collapse × object-size interaction: very long token sequences degrade small-object segmentation specifically.
- **Problem:** Scaling to many tokens (high-res, 3D) changes attention distributions (entropy collapse, sharpening on few tokens); the spatial consequence — which objects lose representation — is unknown.
- **Core Hypothesis (falsifiable):** As token count grows, attention entropy over spatial tokens falls, and per-object segmentation quality declines with the object's token share (small objects first), with entropy-regularized attention selectively restoring small-object performance — a mechanism linking sequence scaling to a specific dense failure.
- **Why Important:** High-resolution scaling is marketed as uniformly better; a small-object penalty would be a crucial caveat for lesion-scale medical work.
- **Why Possibly Novel:** The sequence-length × object-size interaction has not been isolated.
- **Minimal Experiment:** Token-count sweeps (resolution/cropping controlled) with size-stratified evaluation; attention-entropy logging; regularization intervention.
- **Main Risk:** Token count covaries with resolution benefits; careful controls (fixed physical resolution, varying context) required.

### IDEA-C-0283
- **One-sentence idea:** Quantify tile-boundary artifacts in whole-slide pathology segmentation: tiling creates false structure at predictable positions.
- **Problem:** Gigapixel slides are processed in tiles; stitched outputs may contain systematic discontinuities and context-truncation errors at tile borders that aggregate metrics conceal — and that downstream spatial analyses (tumor-margin measurement) then consume as if real.
- **Core Hypothesis (falsifiable):** Error and prediction-discontinuity statistics are significantly elevated at tile boundaries relative to matched interior positions, artifacts propagate into derived spatial biomarkers at measurable rates, and context-overlap scheduling reduces them with a computable overlap-cost trade-off curve.
- **Why Important:** Computational pathology's spatial biomarkers inherit unexamined tiling artifacts; the field needs the artifact budget and the overlap-cost curve.
- **Why Possibly Novel:** Tile-artifact quantification with biomarker propagation analysis is not established practice.
- **Minimal Experiment:** Tile-relative error profiling on WSI benchmarks; biomarker sensitivity analysis; overlap-sweep cost curves.
- **Main Risk:** Ground truth on WSIs is itself tile-annotated sometimes; select datasets with continuous annotation.

### IDEA-C-0284
- **One-sentence idea:** Establish the codebook-boundary bound: discrete visual tokenizers (VQ) cap achievable boundary precision by their codebook's spatial granularity.
- **Problem:** Generative and unified models increasingly use discrete visual tokens for dense outputs; the quantization's ceiling on boundary accuracy is undetermined — is the codebook or the transformer the bottleneck?
- **Core Hypothesis (falsifiable):** Oracle decoding (best achievable mask expressible in the token space) shows a boundary-precision ceiling determined by codebook size and token spatial footprint, real models sit close to that ceiling (transformer is not the bottleneck), and codebook interventions move end performance as the bound predicts.
- **Why Important:** Tells unified-model designers whether dense-task investment belongs in the tokenizer or the sequence model — currently guessed.
- **Why Possibly Novel:** Oracle-ceiling accounting for discrete-token dense prediction has not been performed.
- **Minimal Experiment:** Compute oracle mask reconstructions through VQ token spaces at varied codebook configurations; compare against trained-model outputs.
- **Main Risk:** Oracle decoding is combinatorial; use per-token greedy oracles as certified approximations.

### IDEA-C-0285
- **One-sentence idea:** Detect orientation priors baked into position embeddings: pretraining orientation statistics create flip/rotation performance asymmetries downstream.
- **Problem:** Pretraining corpora have canonical orientations (upright faces, horizons, supine anatomy); learned positional structures may encode them, silently penalizing differently oriented inputs even after fine-tuning.
- **Core Hypothesis (falsifiable):** Models show reproducible performance asymmetries under input flips/rotations that persist after orientation-balanced fine-tuning, the asymmetry localizes to position-embedding interactions (removable by embedding re-symmetrization, not by more data), and asymmetry direction matches pretraining orientation statistics — a data-history fingerprint in the geometry pipeline.
- **Why Important:** Medical images arrive in varied orientations; hidden orientation priors are a portability hazard with a localized, fixable cause.
- **Why Possibly Novel:** Attribution of orientation asymmetry to positional components (vs features) has not been carried out.
- **Minimal Experiment:** Orientation battery across models; embedding-symmetrization intervention vs fine-tuning control; asymmetry-statistics comparison.
- **Main Risk:** Content features also carry orientation bias; the intervention comparison isolates the positional share.

### IDEA-C-0286
- **One-sentence idea:** Trace the masking-ratio → boundary-sharpness trade-off: masked-image pretraining teaches inpainting-smooth features whose boundary cost scales with mask ratio.
- **Problem:** MAE-style pretraining ratio is tuned for global transfer; reconstruction-from-context plausibly rewards spatial smoothing whose dense-task cost is unexamined.
- **Core Hypothesis (falsifiable):** Backbone features' boundary sharpness (probe-measured edge localization) decreases monotonically with pretraining mask ratio at equal global transfer quality, downstream segmentation boundary metrics follow the same ordering, and low-ratio or boundary-aware masking recovers sharpness — mask ratio is a hidden boundary-quality knob.
- **Why Important:** A single pretraining scalar with systematic dense consequences should be set knowingly, per intended use.
- **Why Possibly Novel:** Mask-ratio effects on boundary-specific feature properties have not been isolated.
- **Minimal Experiment:** Pretrain ratio-sweep twins at modest scale; edge-localization probes; downstream boundary-metric comparison.
- **Main Risk:** Requires controlled pretraining; modest scale suffices for the comparative claim.

### IDEA-C-0287
- **One-sentence idea:** Quantify numerics as a benchmark variance source: low-precision attention implementations change dense outputs near boundaries at rates comparable to reported method gains.
- **Problem:** FlashAttention variants, bf16/fp16 choices, and kernel fusion alter floating-point summation orders; dense predictions near decision boundaries can flip, yet numerics is never reported or controlled in benchmarks.
- **Core Hypothesis (falsifiable):** Across numerics configurations (kernels, precisions, batch nondeterminism), per-pixel prediction flips concentrate near boundaries and accumulate to metric differences overlapping the magnitude of typical published improvements on fine-grained boundary metrics — numerics is an unacknowledged term in the field's error budget.
- **Why Important:** If numerics-induced variance rivals claimed gains, reporting standards must change (fixed-numerics evaluation or variance disclosure).
- **Why Possibly Novel:** Numerics-variance accounting for dense-prediction benchmarks has not been published.
- **Minimal Experiment:** Evaluate fixed checkpoints under a numerics-configuration grid; flip-map analysis; compare variance to published deltas.
- **Main Risk:** Findings depend on hardware generation; report across two GPU families.

### IDEA-C-0288
- **One-sentence idea:** Stress-test aspect-ratio squashing: resizing non-square images to square inputs systematically distorts anisotropic-structure segmentation.
- **Problem:** Square-input pipelines squash images with arbitrary aspect ratios, anisotropically deforming structures; the segmentation cost of this deformation — versus padding or native-aspect processing — is untested folklore in both directions.
- **Core Hypothesis (falsifiable):** Squash-trained models show orientation-dependent boundary errors on elongated structures that padding-trained twins lack, the error grows with deviation from the dataset's median aspect ratio, and inference-time aspect mismatch (train squash, test different ratios) produces predictable systematic shape bias in outputs — deformation is learned as if real.
- **Why Important:** Aspect handling is a silent preprocessing choice in every pipeline; its geometric cost should be measured, especially for medical shape/size quantification.
- **Why Possibly Novel:** Controlled squash-vs-padding twins with shape-bias endpoints have not been reported.
- **Minimal Experiment:** Twin trainings across aspect-handling policies; orientation- and aspect-stratified boundary evaluation; output shape-bias measurement.
- **Main Risk:** Padding changes effective resolution and batch statistics; match compute and content scale carefully.

---

## C11. Community beliefs that may be false (testable) (IDEA-C-0289 … 0314)

### IDEA-C-0289
- **One-sentence idea:** Test non-monotonicity of pretraining scale for medical transfer: curated small pretraining can beat web-scale for specific modalities.
- **Problem:** "More pretraining data always helps downstream medical tasks" guides model selection, but distribution mismatch may make web-scale pretraining actively dilutive for some modalities.
- **Core Hypothesis (falsifiable):** For at least some modality/task pairs (e.g., ultrasound, OCT), models pretrained on smaller curated in-domain-adjacent corpora outperform web-scale-pretrained models of matched architecture after identical fine-tuning — and the crossover is predicted by a measurable domain-distance statistic.
- **Why Important:** Model-selection defaults ("take the biggest") drive real medical projects; documented exceptions with a predictor would change practice.
- **Why Possibly Novel:** Scale-vs-curation crossovers with a validated pre-hoc predictor have not been mapped for medical transfer.
- **Minimal Experiment:** {web-scale, curated-medium, in-domain-small} pretrained backbones × 8 medical tasks with matched fine-tuning; crossover analysis against domain-distance measures.
- **Main Risk:** Matched-architecture checkpoints across pretraining regimes are scarce; some controlled pretraining required.

### IDEA-C-0290
- **One-sentence idea:** Test whether Dice loss is actually necessary for imbalanced segmentation, or whether tuned weighted cross-entropy matches it.
- **Problem:** "Use Dice loss for imbalance" is near-universal advice, potentially established against under-tuned CE baselines and perpetuated by citation.
- **Core Hypothesis (falsifiable):** With properly tuned class weights and learning-rate schedules, weighted CE matches Dice-family losses on region metrics across imbalance levels, while showing different (sometimes better) boundary and calibration behavior — the belief reflects tuning asymmetry, not loss superiority.
- **Why Important:** Loss folklore shapes thousands of experiments; a corrected account also recovers CE's superior probabilistic properties where usable.
- **Why Possibly Novel:** A tuning-equalized, multi-metric adjudication of the CE-vs-Dice belief is missing despite the topic's ubiquity.
- **Minimal Experiment:** Imbalance-graded datasets × {tuned WCE, Dice, compound} with equal tuning budgets; multi-metric comparison with variance accounting.
- **Main Risk:** "Properly tuned" invites dispute; pre-register tuning protocols and budgets.

### IDEA-C-0291
- **One-sentence idea:** Re-test "ImageNet pretraining is obsolete for medical imaging" under modern augmentation and training recipes.
- **Problem:** The belief that natural-image pretraining is useless or harmful for medical tasks stems from studies with dated recipes; modern training may change the verdict in either direction.
- **Core Hypothesis (falsifiable):** With current augmentation/schedules, ImageNet initialization still provides significant gains over random initialization for small medical datasets and remains competitive with in-domain SSL at moderate data scale — with the advantage vanishing at a measurable dataset-size threshold.
- **Why Important:** Initialization advice determines infrastructure choices across medical ML; it should track current training practice, not historical experiments.
- **Why Possibly Novel:** Recipe-modernized re-evaluation of this widely repeated claim, with the threshold estimate, is absent.
- **Minimal Experiment:** {random, ImageNet, in-domain SSL} inits × dataset-size ladders × modern recipes on 6 medical tasks.
- **Main Risk:** Conclusions may be architecture-specific; include CNN and ViT backbones.

### IDEA-C-0292
- **One-sentence idea:** Test whether "transformers need more data than CNNs" for segmentation survives equalized augmentation and training length.
- **Problem:** The data-hunger belief for ViTs came from early classification comparisons with unequal regularization; segmentation-specific evidence with modern equalized recipes is thin.
- **Core Hypothesis (falsifiable):** At matched augmentation strength, schedule length, and parameter count, ViT and CNN segmenters show statistically indistinguishable data-efficiency curves on medical segmentation — the believed gap is a recipe artifact, or it survives and is quantified properly for the first time.
- **Why Important:** Architecture selection for data-poor medical settings leans on this belief; either outcome is directly actionable.
- **Why Possibly Novel:** Data-efficiency curves under strictly equalized training for dense medical tasks have not been published.
- **Minimal Experiment:** Data-fraction sweeps × {ViT, CNN} at matched budgets/regularization on 4 datasets; curve comparison with uncertainty.
- **Main Risk:** True matching is hard (inductive-bias differences interact with augmentation); document all equalization choices.

### IDEA-C-0293
- **One-sentence idea:** Characterize when test-time augmentation hurts: TTA degrades calibration and boundary sharpness even while improving mean Dice.
- **Problem:** "TTA always helps" is default practice; averaging over transforms plausibly blurs boundaries and distorts confidence in ways aggregate metrics hide.
- **Core Hypothesis (falsifiable):** TTA improves region overlap on average but systematically degrades boundary-localization sharpness and produces overconfident-smooth probability fields (worse boundary calibration), with the harm growing with transform-set aggressiveness — a quantified cost side of a believed-free technique.
- **Why Important:** TTA is deployed clinically as a free win; its structured costs belong in the decision.
- **Why Possibly Novel:** The metric-decomposed cost analysis of TTA for segmentation has not been reported.
- **Minimal Experiment:** TTA transform-set sweeps across models/datasets; region, boundary, and calibration metric decomposition.
- **Main Risk:** TTA implementations vary (logit vs label averaging); test both aggregation modes.

### IDEA-C-0294
- **One-sentence idea:** Test whether large batches are actually necessary for dense contrastive SSL, or whether the belief transferred wrongly from classification.
- **Problem:** "Contrastive needs big batches" came from instance-level classification objectives; dense variants harvest thousands of negatives per image, changing the arithmetic entirely.
- **Core Hypothesis (falsifiable):** Dense contrastive pretraining at small batch sizes (with per-image negative pools) matches large-batch versions on downstream segmentation transfer at equal compute — the batch-size requirement is objective-specific, and the community's constraint is spurious for dense SSL.
- **Why Important:** The big-batch belief gates who can do SSL research (hardware barrier); removing it for dense objectives democratizes the area.
- **Why Possibly Novel:** Batch-size requirement analysis specific to dense contrastive objectives is not established.
- **Minimal Experiment:** Batch-size sweeps for dense contrastive pretraining at fixed compute; downstream transfer comparison.
- **Main Risk:** Optimizer interactions with batch size need care; tune learning rates per batch size.

### IDEA-C-0295
- **One-sentence idea:** Build the taxonomy of when full 3D actually beats 2.5D: structures with in-plane definition may gain nothing from volumetric context.
- **Problem:** "3D is better than 2.5D" is asserted globally, but the advantage plausibly depends on whether the structure's identity requires cross-slice evidence — an unmapped moderator.
- **Core Hypothesis (falsifiable):** Across structures, the 3D-vs-2.5D gap is predicted by a computable cross-slice-information statistic (how much adjacent slices change per-pixel label posterior); structures below a threshold show no significant 3D advantage at matched compute — yielding a per-structure architecture-selection rule.
- **Why Important:** 3D costs memory, data, and training stability; spending it only where the taxonomy says it pays is directly valuable.
- **Why Possibly Novel:** A predictive moderator analysis (not another aggregate comparison) of the 3D question is missing.
- **Minimal Experiment:** {3D, 2.5D, 2D} at matched compute across structures spanning the statistic; test the threshold prediction.
- **Main Risk:** Compute matching across dimensionalities is contested; report multiple matching conventions.

### IDEA-C-0296
- **One-sentence idea:** Test whether deep supervision's benefit is mostly an implicit warmup/conditioning effect reproducible by tuned schedules alone.
- **Problem:** Deep supervision is standard in medical segmentation architectures; its mechanism is unexamined, and its gains may duplicate what modern schedule tuning already provides.
- **Core Hypothesis (falsifiable):** With well-tuned warmup and layer-wise learning-rate schedules, removing deep supervision changes final performance insignificantly across architectures/datasets — its historical gains were optimization-conditioning, now redundant; residual benefits, if any, localize to very deep or low-data regimes.
- **Why Important:** Deep supervision complicates architectures and losses; if redundant, simplification is free.
- **Why Possibly Novel:** Mechanism-controlled ablation of deep supervision against tuned-schedule baselines has not been run.
- **Minimal Experiment:** {deep supervision, none} × {default, tuned schedules} factorial on 4 setups; interaction analysis.
- **Main Risk:** Benefits may appear only in specific regimes; the factorial design maps them rather than averaging over them.

### IDEA-C-0297
- **One-sentence idea:** Test the ensemble folklore: at fixed compute, seed ensembles of the best architecture may beat diverse-architecture ensembles.
- **Problem:** "Diversity beats replication" guides ensemble construction, but diverse ensembles include weaker members; the diversity-vs-quality trade at fixed total compute is unresolved for segmentation.
- **Core Hypothesis (falsifiable):** At matched total training compute, homogeneous seed ensembles of the strongest architecture match or beat heterogeneous ensembles on accuracy, while heterogeneous ensembles win on OOD robustness — the belief is half-true, and which half matters depends on deployment.
- **Why Important:** Ensembling is the default competition/clinical-safety tool; construction rules should follow measurement.
- **Why Possibly Novel:** Compute-normalized homogeneous-vs-heterogeneous comparison with the ID/OOD split is not established for dense tasks.
- **Minimal Experiment:** Ensemble grids at fixed compute × {ID, shifted} evaluation on 3 datasets.
- **Main Risk:** Results depend on the architecture pool's quality spread; report sensitivity to pool composition.

### IDEA-C-0298
- **One-sentence idea:** Re-analyze domain randomization for cross-site robustness with risk-sensitive statistics: mean gains may hide worst-site losses.
- **Problem:** Aggressive appearance randomization is reported to improve average cross-site generalization; if it trades worst-case sites for mean gains, safety-relevant conclusions invert.
- **Core Hypothesis (falsifiable):** Across multi-site evaluations, randomization-trained models improve site-average metrics while a measurable fraction of individual sites degrade below the non-randomized baseline — and the degraded sites share identifiable characteristics (appearance already far from the randomization envelope).
- **Why Important:** Clinical robustness claims should be worst-case-aware; mean-based evidence may be endorsing a harmful trade.
- **Why Possibly Novel:** Risk-sensitive (per-site distributional) re-analysis of domain randomization is not standard.
- **Minimal Experiment:** {randomized, standard} training × many-site evaluation; per-site distribution analysis; characterize degraded sites.
- **Main Risk:** Needs genuinely many-site data; combine public multi-site collections.

### IDEA-C-0299
- **One-sentence idea:** Test whether pseudo-labeling actually needs confidence thresholds, or whether noise-tolerant losses make thresholds redundant folklore.
- **Problem:** Threshold selection is treated as essential to self-training; robust-loss theory suggests unfiltered pseudo-labels with appropriate losses might match it without the hyperparameter.
- **Core Hypothesis (falsifiable):** Self-training with no filtering but noise-robust objectives (e.g., generalized CE variants) matches threshold-tuned pipelines across datasets — thresholds compensate for loss fragility rather than being fundamental, removing a sensitive hyperparameter from the standard recipe.
- **Why Important:** Threshold sensitivity is a major reproducibility pain in semi-supervised work; eliminating it simplifies the whole recipe space.
- **Why Possibly Novel:** The threshold-vs-robust-loss substitution has not been tested head-to-head in segmentation self-training.
- **Minimal Experiment:** {thresholded CE, unfiltered robust losses} × 4 datasets × label fractions; matched tuning budgets.
- **Main Risk:** Robust losses have their own hyperparameters; count total tuning cost honestly.

### IDEA-C-0300
- **One-sentence idea:** Attribute nnU-Net's dominance: is it the self-configuring architecture or simply the preprocessing/normalization stack?
- **Problem:** nnU-Net's success is culturally attributed to holistic self-configuration; component-level attribution would tell the field which parts to copy — but has not been done systematically.
- **Core Hypothesis (falsifiable):** Transplanting only nnU-Net's preprocessing/intensity-normalization/resampling stack onto generic baselines recovers the majority of its advantage across tasks, while its architecture choices contribute a minor share — the field under-invests in preprocessing because attribution is missing.
- **Why Important:** Correct credit assignment redirects replication effort to the components that matter.
- **Why Possibly Novel:** Full factorial component attribution of the nnU-Net stack has not been published.
- **Minimal Experiment:** Factorial transplant of {preprocessing, augmentation, architecture, postprocessing} components onto plain baselines across 5 tasks.
- **Main Risk:** Components interact; factorial (not one-at-a-time) design is essential and costlier.

### IDEA-C-0301
- **One-sentence idea:** Measure the true frozen-backbone ceiling for dense prediction with properly engineered multi-layer readouts.
- **Problem:** "Frozen backbones can't do dense prediction well" justifies universal fine-tuning; the claim is largely tested with naive single-layer readouts.
- **Core Hypothesis (falsifiable):** With multi-layer feature aggregation and modest decoders, frozen modern backbones close most of the gap to full fine-tuning on standard segmentation benchmarks — the believed necessity of fine-tuning reflects readout under-engineering, with the residual gap concentrated in domain-shifted settings.
- **Why Important:** Frozen deployment enables shared backbones, cheap certification, and multi-task serving; its real ceiling should be known.
- **Why Possibly Novel:** A systematic frozen-ceiling measurement with strong readouts across backbones is missing.
- **Minimal Experiment:** Readout-capacity sweeps on frozen backbones vs fine-tuning across 6 dense tasks; gap decomposition by domain distance.
- **Main Risk:** "Modest decoder" boundaries need pre-registration to avoid moving goalposts.

### IDEA-C-0302
- **One-sentence idea:** Test the label-preservation dogma of augmentation: mild label-violating transforms may act as beneficial regularization.
- **Problem:** Augmentation design demands label-preserving transforms; small violations (elastic deformations that slightly alter true boundaries) are avoided on principle rather than evidence.
- **Core Hypothesis (falsifiable):** Augmentations with controlled small label violation (boundary displacement below rater variance) improve generalization over strictly label-preserving sets at matched diversity — a "safe violation budget" exists, sized by the ambiguity band, invalidating the strict-preservation rule.
- **Why Important:** Widens the usable augmentation space, particularly for medical deformation augmentation where strict preservation is impossible anyway.
- **Why Possibly Novel:** The violation-budget framing with rater-variance calibration is untested.
- **Minimal Experiment:** Violation-magnitude ladders (relative to measured rater variance) across datasets; generalization comparison at matched augmentation diversity.
- **Main Risk:** Violation interacts with evaluation labels' own noise; use tolerance-aware metrics (cf. 0245).

### IDEA-C-0303
- **One-sentence idea:** Test task-alignment folklore in pretraining: does segmentation pretraining actually transfer better to segmentation than classification pretraining at matched data?
- **Problem:** "Pretrain on the same task type" sounds self-evident and guides costly dataset construction, but matched-data evidence is surprisingly thin — classification pretraining sees more diverse supervision per image.
- **Core Hypothesis (falsifiable):** At matched pretraining data scale and compute, classification-pretrained backbones transfer to segmentation within a small margin of segmentation-pretrained ones (or better on boundary metrics, given richer image-level diversity) — task-format alignment matters less than believed, and data diversity dominates.
- **Why Important:** Task-aligned pretraining datasets (dense labels) are enormously expensive; if alignment buys little, resources should go to scale/diversity.
- **Why Possibly Novel:** Strictly matched-data task-format comparisons for dense transfer are rare to absent.
- **Minimal Experiment:** Controlled pretraining {classification, segmentation} on the same images at matched compute; transfer battery across 6 dense tasks.
- **Main Risk:** Label quality differs inherently between formats; document and bound the asymmetry.

### IDEA-C-0304
- **One-sentence idea:** Systematically re-measure whether published "boundary losses" improve boundary metrics — or mostly move Dice.
- **Problem:** Losses marketed as boundary-improving are often validated on overlap metrics; whether they deliver on their named promise across settings is unverified at scale.
- **Core Hypothesis (falsifiable):** Re-evaluating the boundary-loss family under a standardized multi-metric protocol shows a substantial fraction improving region metrics without significant boundary-metric gains (and some degrading boundary calibration) — the naming implies a mechanism the evidence doesn't support.
- **Why Important:** Method selection for boundary-critical applications currently trusts names and abstracts; a verification study re-grounds it.
- **Why Possibly Novel:** A standardized cross-loss boundary-metric verification with proper statistics (cf. 0210) has not been performed.
- **Minimal Experiment:** 8 boundary-family losses × 4 datasets under one protocol with autocorrelation-corrected inference; promise-vs-delivery table.
- **Main Risk:** Implementations vary; use authors' code where available, documented reimplementations otherwise.

### IDEA-C-0305
- **One-sentence idea:** Adjudicate resampling vs reweighting for class imbalance: theoretically equivalent in the limit, empirically split by batch statistics — find the actual mechanism.
- **Problem:** "Imbalance requires oversampling" vs "reweighting suffices" both circulate; their equivalence breaks under mini-batching and normalization layers in ways nobody has pinned down for segmentation.
- **Core Hypothesis (falsifiable):** Resampling and reweighting produce equivalent results with GroupNorm and full-batch-like statistics, but diverge systematically with BatchNorm (resampling changes normalization statistics, reweighting doesn't) — the folklore disagreement reduces to a normalization interaction, testable by architecture swap.
- **Why Important:** Resolves a perennial practice dispute with a mechanism, giving architecture-conditional advice.
- **Why Possibly Novel:** The normalization-interaction explanation of the resampling/reweighting split is unformalized.
- **Minimal Experiment:** {resample, reweight} × {BN, GN} factorial across imbalance levels; interaction test on segmentation quality per class.
- **Main Risk:** Other batch-composition effects (gradient noise) contribute; include gradient-statistics logging for attribution.

### IDEA-C-0306
- **One-sentence idea:** Test whether higher input resolution always helps small-structure segmentation — or whether a per-structure optimum exists beyond which noise dominates.
- **Problem:** "More resolution helps small objects" drives compute escalation; beyond the acquisition's information content, upsampling adds interpolation artifacts and noise sensitivity with unknown net effect.
- **Core Hypothesis (falsifiable):** Per-structure performance versus input resolution is non-monotone with an optimum predicted by the structure's physical size relative to acquisition resolution — beyond it, added resolution measurably hurts through noise amplification and receptive-field dilution.
- **Why Important:** Resolution is the biggest compute knob; per-structure optima would replace escalation with calculation.
- **Why Possibly Novel:** Non-monotonicity of the resolution curve with physical-size prediction has not been documented.
- **Minimal Experiment:** Resolution ladders on structures spanning physical sizes; locate optima; test the predictive rule.
- **Main Risk:** Resolution interacts with model receptive field; sweep both jointly at controlled compute.

### IDEA-C-0307
- **One-sentence idea:** Audit multi-task learning's "shared knowledge" claims: do MTL gains survive against single-task baselines with matched total compute and tuning?
- **Problem:** MTL papers compare against single-task baselines trained with less collective care; the claimed knowledge transfer may be resource asymmetry.
- **Core Hypothesis (falsifiable):** Under strict matching (total compute including tuning, data access), most published-style MTL configurations show gains statistically indistinguishable from zero on the primary tasks, with genuine transfer confined to identifiably related task pairs (measurable representation overlap) — sharpening MTL's valid scope.
- **Why Important:** MTL adds engineering complexity everywhere it's adopted; its real conditions of benefit should be established.
- **Why Possibly Novel:** Compute-and-tuning-matched MTL audits across dense-task combinations are missing.
- **Minimal Experiment:** MTL vs matched single-task baselines across task-pair relatedness ladder; gains vs relatedness analysis.
- **Main Risk:** Matching conventions are contested; report several and pre-register the primary one.

### IDEA-C-0308
- **One-sentence idea:** Test the robustness belief for SSL features on dense tasks: corruption-type-resolved comparison against supervised features.
- **Problem:** "SSL features are more robust than supervised" generalizes classification-era findings; dense tasks and specific corruption families (blur vs noise vs geometric) may reverse it.
- **Core Hypothesis (falsifiable):** Corruption-resolved dense-task evaluation shows an interaction: SSL features are more robust to appearance corruptions but less robust to geometric/structural corruptions than supervised twins — the aggregate belief hides a structured split relevant to deployment threat models.
- **Why Important:** Robustness claims inform backbone choice for safety-critical dense applications; the resolved version is the actionable one.
- **Why Possibly Novel:** Corruption-family-resolved SSL-vs-supervised comparison for dense prediction is unreported.
- **Minimal Experiment:** {SSL, supervised} matched backbones × corruption battery × 3 dense tasks; interaction analysis.
- **Main Risk:** Matched-training twins are essential; use publicly documented pairs or train controlled ones.

### IDEA-C-0309
- **One-sentence idea:** Test whether generative-model data augmentation adds information beyond what cheaper distribution-smoothing augmentation provides.
- **Problem:** GAN/diffusion-synthesized training data reports gains attributed to "new information"; the gains may reduce to distributional smoothing achievable by aggressive classical augmentation at negligible cost.
- **Core Hypothesis (falsifiable):** At matched effective-diversity levels (measured in feature space), classical augmentation pipelines match synthetic-data gains for in-domain performance, with synthetic data's unique contribution confined to explicitly compositional novelty (rare class combinations) — a boundary between hype and value, measured.
- **Why Important:** Synthetic-data pipelines are costly and introduce fidelity risks; knowing what they uniquely buy prevents misallocation.
- **Why Possibly Novel:** Diversity-matched adjudication between synthetic and classical augmentation has not been performed.
- **Minimal Experiment:** Match feature-space diversity across augmentation regimes; compare gains overall and on compositional-novelty subsets.
- **Main Risk:** Diversity matching metric choices matter; use several and report agreement.

### IDEA-C-0310
- **One-sentence idea:** Measure what distillation actually transfers in segmentation: soft labels carry the teacher's spatially correlated error structure along with its "dark knowledge".
- **Problem:** Distillation is treated as transferring beneficial class-similarity information; in dense tasks the teacher's systematic boundary biases (cf. 0218) are part of the signal, and their inheritance is unexamined.
- **Core Hypothesis (falsifiable):** Student boundary-bias fields correlate strongly with teacher bias fields (far above independently trained controls), inherited bias persists even when students surpass teachers on aggregate metrics, and bias-corrected teacher outputs (0218's correction) produce measurably better students — distillation transfers error structure, correctably.
- **Why Important:** Distillation is the deployment path for foundation models (cf. 0178); inherited systematic bias would propagate silently into clinical tools.
- **Why Possibly Novel:** Error-structure inheritance analysis in dense distillation is missing.
- **Minimal Experiment:** Teacher/student bias-field correlation analysis across distillation setups; bias-corrected-teacher intervention.
- **Main Risk:** Bias-field estimation needs multi-seed teachers; compute-heavy but tractable.

### IDEA-C-0311
- **One-sentence idea:** Test whether early stopping on validation Dice silently sacrifices boundary quality that continues improving after Dice plateaus.
- **Problem:** Standard practice stops training when val-Dice plateaus; if metric families converge at different speeds (cf. 0207), the convention systematically truncates boundary learning.
- **Core Hypothesis (falsifiable):** Boundary metrics continue improving significantly after val-Dice plateau in a substantial fraction of training runs, so Dice-based stopping leaves consistent boundary performance unbanked — and multi-metric stopping criteria capture it at negligible cost.
- **Why Important:** A universal training convention may be systematically shaving boundary quality off every published model.
- **Why Possibly Novel:** Metric-resolved post-plateau training dynamics have not been documented.
- **Minimal Experiment:** Extended trainings past Dice plateau across datasets/architectures; metric-family trajectory analysis; stopping-rule comparison.
- **Main Risk:** Post-plateau boundary gains may overfit annotation style; validate on multi-rater or physical-reference subsets.

### IDEA-C-0312
- **One-sentence idea:** Test attention-map explanations for dense models: perturbation-based faithfulness audits of the claim that attention shows "what the segmenter used".
- **Problem:** Papers and clinical demos present attention maps as explanations of segmentation decisions; faithfulness testing has focused on classification, leaving the dense-task version an assumed property.
- **Core Hypothesis (falsifiable):** Perturbing image regions ranked important by attention changes segmentation outputs no more than perturbing matched-salience control regions for a large fraction of cases — attention maps in dense models fail standard faithfulness tests, and gradient-free alternatives (occlusion attribution) diverge from them substantially.
- **Why Important:** Unfaithful explanations in clinical interfaces are worse than none — they manufacture unwarranted trust.
- **Why Possibly Novel:** Dense-prediction-specific faithfulness auditing of attention explanations is missing.
- **Minimal Experiment:** Faithfulness battery (deletion/insertion, controlled perturbation) on attention vs occlusion attributions across dense models.
- **Main Risk:** Faithfulness metrics have known pathologies; use multiple complementary tests.

### IDEA-C-0313
- **One-sentence idea:** Test the patch-training equivalence belief: patch-based training equals full-image training "if patches are large enough" — or does global context leak in measurably even for local structures?
- **Problem:** Memory constraints make patch training universal in 3D; the equivalence assumption defines the field's default pipeline but has not been tested against full-context training at matched effective batch statistics.
- **Core Hypothesis (falsifiable):** Full-context-trained models outperform patch-trained twins on structures whose segmentation benefits from beyond-patch context (measurable by context-ablation probes), even when patches nominally contain the whole structure — global statistics (organ position, patient-level intensity landmarks) contribute measurably, quantifying the real cost of patch training.
- **Why Important:** If the equivalence fails, memory-saving architectures with global context paths deserve systematic priority.
- **Why Possibly Novel:** Controlled patch-vs-full-context twins with context-attribution analysis are rare due to memory limits — now feasible at moderate resolutions.
- **Minimal Experiment:** Patch-size ladders through full-image training at matched compute on downsampled 3D data; structure-level gap analysis with context probes.
- **Main Risk:** Full-context training changes batch composition; equalize update counts and effective batch statistics carefully.

### IDEA-C-0314
- **One-sentence idea:** Test whether "better pretraining benchmarks predict better downstream medical performance" — the transfer-prediction belief underlying model selection.
- **Problem:** Practitioners select backbones by ImageNet/general-benchmark scores, assuming rank correlation with medical downstream performance; the correlation's actual strength for dense medical tasks is unquantified.
- **Core Hypothesis (falsifiable):** Across a broad backbone pool, general-benchmark rank explains only a minor fraction of variance in medical dense-task rank, with systematic inversions for specific families — and a cheap in-domain probe (frozen-feature linear segmentation on 100 images) predicts downstream rank far better, replacing the belief with a usable instrument.
- **Why Important:** Backbone selection is every project's first decision; an evidence-based selector beats benchmark folklore.
- **Why Possibly Novel:** Transfer-rank-correlation studies exist for natural-image classification; the dense medical version with a validated cheap predictor does not.
- **Minimal Experiment:** 15 backbones × 6 medical dense tasks; correlate general-benchmark vs probe-based predictors with realized ranks.
- **Main Risk:** Backbone pools confound architecture/data/scale; report partial correlations by family.

---

## C12. Cheap experiments that could overturn a popular paper's implicit assumption (IDEA-C-0315 … 0340)

### IDEA-C-0315
- **One-sentence idea:** Run the scramble test on published "global context" modules: shuffle distant image regions and see if the module's benefit survives.
- **Problem:** Many papers attribute gains to long-range context aggregation; if performance is unchanged when distant content is scrambled, the module's stated mechanism is not what it does.
- **Core Hypothesis (falsifiable):** For a substantial fraction of published context modules, the accuracy gain over local baselines persists under distant-region scrambling — the gains come from added capacity/regularization, not from the long-range information the papers credit.
- **Why Important:** Mechanism misattribution compounds across the literature; a cheap universal test cleans it.
- **Why Possibly Novel:** Scramble-based mechanism verification has not been applied systematically to context-module claims.
- **Minimal Experiment:** Take 5 public context-module models; evaluate with block-scrambled inputs (preserving local windows); compare gain retention against local-only baselines.
- **Main Risk:** Scrambling introduces edge artifacts; use soft-blended scrambles and artifact controls.

### IDEA-C-0316
- **One-sentence idea:** Replace learned prompts with random-but-frozen vectors of matched norm: if accuracy holds, prompt "learning" is mostly capacity, not semantics.
- **Problem:** Prompt-tuning papers imply prompts encode task semantics; the null hypothesis — any extra trainable-then-frozen directions plus the head recalibration suffice — is never run.
- **Core Hypothesis (falsifiable):** Freezing prompts at random initialization while training only the same lightweight components the method trains recovers a large fraction of reported gains on standard benchmarks — bounding the semantic content of learned prompts from above.
- **Why Important:** A one-afternoon control that recalibrates interpretation of an entire method family.
- **Why Possibly Novel:** The random-frozen-prompt control is conspicuously absent from the literature.
- **Minimal Experiment:** Rerun 3 canonical prompt methods with random-frozen prompts across their benchmarks; gain-retention table.
- **Main Risk:** Method variants differ in what else is trained; match trainable components exactly per method.

### IDEA-C-0317
- **One-sentence idea:** Train on 8× downsampled masks and evaluate at full resolution: measure how insensitive standard benchmarks are to boundary detail.
- **Problem:** Benchmarks implicitly claim to measure delineation quality; if coarse-mask training barely moves scores, the benchmark's sensitivity to what papers optimize is an illusion.
- **Core Hypothesis (falsifiable):** Models trained on heavily downsampled labels lose only a small fraction of standard-metric performance on popular benchmarks — quantifying each benchmark's boundary-information ceiling and flagging where "boundary improvements" cannot even register.
- **Why Important:** A one-day experiment producing a sensitivity certificate for every benchmark it touches.
- **Why Possibly Novel:** Label-degradation sensitivity audits of benchmarks are not standard practice.
- **Minimal Experiment:** Train identical models with {1×, 4×, 8×} downsampled labels on 4 benchmarks; score-vs-degradation curves per metric.
- **Main Risk:** Downsampling protocol choices matter; use two label-degradation schemes.

### IDEA-C-0318
- **One-sentence idea:** Build the image-free baseline: predict segmentation from dataset priors alone (mean shape atlas, position statistics) and report what benchmarks reward without vision.
- **Problem:** Benchmarks with strong positional regularities (registered anatomy) may award high scores to prior-only predictions, inflating all reported numbers by an unmeasured floor.
- **Core Hypothesis (falsifiable):** Prior-only predictors achieve substantial fractions of published model scores on registered medical benchmarks (and much less on unregistered ones) — establishing per-benchmark prior floors that method comparisons should subtract.
- **Why Important:** Method deltas mean different things above different floors; the floors take hours to compute and are never reported.
- **Why Possibly Novel:** Prior-floor accounting is occasionally gestured at but not systematically published for the benchmark canon.
- **Minimal Experiment:** Fit atlas/position-prior predictors on 6 benchmarks; report floor scores alongside leaderboard ranges.
- **Main Risk:** Prior model strength is a free parameter; report a ladder from trivial to strong priors.

### IDEA-C-0319
- **One-sentence idea:** Pretrain on a single medical volume and measure how much of "large-scale SSL pretraining" benefit survives.
- **Problem:** Medical SSL papers credit corpus scale for downstream gains; if one volume's augmentation-expanded pretraining captures most of the benefit, the mechanism is low-level statistics adaptation, not diverse-corpus knowledge.
- **Core Hypothesis (falsifiable):** Single-volume SSL pretraining recovers a large fraction of the downstream gap between random initialization and full-corpus SSL for same-modality tasks — the scale narrative overstates what corpus diversity contributes at current task difficulty.
- **Why Important:** Redirects data-collection investment and reframes what medical SSL currently learns.
- **Why Possibly Novel:** Single-instance pretraining controls exist for natural images but not as an audit of medical SSL scale claims.
- **Minimal Experiment:** {random, 1-volume SSL, full-corpus SSL} inits × 4 downstream tasks at matched pretraining compute.
- **Main Risk:** Result may vary by modality richness; run on 2 modalities before generalizing.

### IDEA-C-0320
- **One-sentence idea:** Swap decoders between two published methods and check whether reported superiority travels with the component the paper credits.
- **Problem:** Papers attribute gains to their novel encoder/module while decoders and training details differ simultaneously; component-swap tests of attribution are almost never run by anyone.
- **Core Hypothesis (falsifiable):** In a sample of published method pairs, cross-transplanting decoders (or training recipes) transfers a large share of the performance difference — the credited component is not the causal one in a measurable fraction of cases.
- **Why Important:** Attribution errors propagate into what the community builds next; swap tests are cheap and decisive.
- **Why Possibly Novel:** Systematic component-swap auditing of published comparisons has not been undertaken.
- **Minimal Experiment:** 4 method pairs with public code; factorial component swaps; variance attribution to components.
- **Main Risk:** Some components are entangled; choose pairs with clean interfaces.

### IDEA-C-0321
- **One-sentence idea:** Re-annotate 50 test images with 3 raters and check whether benchmark leaderboard gaps exceed the annotation noise floor.
- **Problem:** Leaderboard differences are interpreted as method quality without knowing the test labels' own uncertainty — a floor obtainable for the cost of a small annotation study.
- **Core Hypothesis (falsifiable):** For popular benchmarks, the score fluctuation induced by substituting equally valid alternative annotations exceeds a large fraction of the top-10 leaderboard spread — many ranked differences are label-noise artifacts, quantifiably.
- **Why Important:** A few-hundred-dollar experiment that recalibrates how much attention leaderboard deltas deserve.
- **Why Possibly Novel:** Annotation-noise floors for specific popular leaderboards are not published.
- **Minimal Experiment:** Triple-annotate 50-image test subsets on 2 benchmarks; recompute top-model scores against each annotation; compare spread to leaderboard gaps.
- **Main Risk:** Subset sampling variance; choose stratified subsets and report confidence intervals.

### IDEA-C-0322
- **One-sentence idea:** Apply a segmentation logit lens: read out predictions from earlier layers and identify classes for which network depth adds nothing.
- **Problem:** Deep decoders are justified as necessary computation; per-class depth-of-computation profiles would test how much of the network each decision actually uses — cheap to measure, never reported.
- **Core Hypothesis (falsifiable):** For a substantial set of classes (large, high-contrast structures), early-layer readouts match final predictions almost exactly, with depth contributing only for identifiable hard classes — quantifying per-class computational depth and exposing over-provisioned architectures.
- **Why Important:** Enables principled early-exit designs and challenges depth claims with direct measurement.
- **Why Possibly Novel:** Layer-wise readout analysis (standard in LLM interpretability) is essentially unapplied to segmentation.
- **Minimal Experiment:** Train linear readouts per layer on frozen trained segmenters; per-class agreement-with-final profiles across datasets.
- **Main Risk:** Readout training adds its own capacity; keep readouts strictly linear and matched.

### IDEA-C-0323
- **One-sentence idea:** Run channel-ablation sparsity probes: how few channels does a trained segmenter actually use per class?
- **Problem:** Wide networks are presumed to use their representational budget; if a handful of channels suffices per class, "rich representation" claims and width choices deserve revision.
- **Core Hypothesis (falsifiable):** Greedy channel selection preserves per-class segmentation within a small margin using under 10% of final-layer channels for most classes, with channel sets largely disjoint across classes — trained segmenters are extremely sparse per decision, measurably.
- **Why Important:** Direct implications for pruning, interpretability, and width scaling — from an experiment that needs no training.
- **Why Possibly Novel:** Per-class channel-sufficiency profiles for segmentation are unreported.
- **Minimal Experiment:** Greedy per-class channel ablation on trained models across architectures; sufficiency curves and overlap analysis.
- **Main Risk:** Greedy selection is suboptimal; corroborate with L0-style selection on a subset.

### IDEA-C-0324
- **One-sentence idea:** Institute the frozen-random-encoder control: train only the decoder on an untrained backbone and report how small the gap to full methods is.
- **Problem:** Papers demonstrate gains over other trained methods but never over the degenerate control that isolates how much the encoder's learned content matters on that benchmark.
- **Core Hypothesis (falsifiable):** On several popular benchmarks, random-frozen-encoder models with trained decoders reach within a strikingly small margin of published methods — exposing benchmarks where architectural priors plus decoder capacity, not learned representations, carry the score.
- **Why Important:** A mandatory-control proposal backed by measurements would recalibrate claimed contributions field-wide.
- **Why Possibly Novel:** Random-feature controls are known in theory circles but unreported as benchmark audits.
- **Minimal Experiment:** Random-frozen vs pretrained-frozen vs full-FT on 6 benchmarks with identical decoders; gap accounting.
- **Main Risk:** Decoder capacity choice drives the control's strength; sweep decoder sizes transparently.

### IDEA-C-0325
- **One-sentence idea:** Test histogram matching as a domain-adaptation baseline: if intensity alignment closes most of the cross-site gap, complex DA methods are solving an already-solved problem.
- **Problem:** Domain-adaptation papers for medical imaging rarely include the cheapest classical baseline — per-image intensity histogram alignment — leaving their headroom claims unanchored.
- **Core Hypothesis (falsifiable):** Histogram matching (plus nothing) recovers a majority of the cross-site performance drop on standard medical DA benchmarks, and published DA methods' gains shrink to marginal once applied on top of it — the benchmarks primarily measure intensity shift.
- **Why Important:** An hour-long baseline that potentially reframes an entire benchmark literature's difficulty claims.
- **Why Possibly Novel:** The baseline is old; its systematic accounting against the modern DA literature is missing.
- **Minimal Experiment:** Histogram-matching preprocessing on 4 DA benchmarks; compare against published DA gains with and without it.
- **Main Risk:** Matching can harm pathological-intensity cases; report per-case distributions, not just means.

### IDEA-C-0326
- **One-sentence idea:** Run the slice-order checkerboard test on "3D" models: feed volumes with permuted slice order and see whether claimed volumetric reasoning notices.
- **Problem:** 3D architectures claim volumetric context use; if predictions are unchanged under slice permutation, the models are functionally 2.5D and the papers' mechanism claims fail.
- **Core Hypothesis (falsifiable):** A measurable fraction of published 3D models show near-identical performance under local slice permutations — their receptive fields or learned features do not exploit inter-slice order, contradicting the stated rationale for their 3D design.
- **Why Important:** Zero-training mechanism verification for a whole architecture class.
- **Why Possibly Novel:** Order-destruction testing of 3D segmentation models has not been reported systematically.
- **Minimal Experiment:** Local and global slice-permutation batteries on 6 public 3D models; degradation profiles vs claimed 3D mechanisms.
- **Main Risk:** Some tasks genuinely need no order information; pair with tasks where order provably matters (cf. 0153).

### IDEA-C-0327
- **One-sentence idea:** Measure the one-epoch fraction: how much of fine-tuning's total gain arrives in the first epoch — and whether adaptation research studies the wrong regime.
- **Problem:** Adaptation methods are developed on long schedules; if most movement happens almost immediately, the interesting dynamics (and the right regularizers) live in a regime papers neither study nor report.
- **Core Hypothesis (falsifiable):** Across standard adaptation setups, the first epoch captures the large majority of the final gain, method differences within the long tail are minor compared to differences in first-epoch behavior, and early-regime-targeted design outperforms tail-targeted design at matched budgets.
- **Why Important:** Redirects adaptation research attention to where the change actually happens; also yields immediate compute savings.
- **Why Possibly Novel:** Gain-arrival-time accounting across adaptation literature has not been compiled.
- **Minimal Experiment:** Dense-checkpoint adaptation runs across 8 setups; gain-vs-time curves; method-difference attribution by phase.
- **Main Risk:** Learning-rate schedules confound arrival dynamics; replicate under multiple schedules.

### IDEA-C-0328
- **One-sentence idea:** Run embedding-based near-duplicate detection between train and test splits of popular benchmarks — a cheap contamination audit with potentially large consequences.
- **Problem:** Benchmark splits constructed years ago (sometimes from overlapping sources) may contain near-duplicates or same-patient leakage that inflates all published results on them.
- **Core Hypothesis (falsifiable):** Automated near-duplicate and same-patient detection finds nontrivial contamination in at least some widely used benchmarks, and re-scoring published-style models on decontaminated test sets measurably shrinks and reorders reported performance.
- **Why Important:** Everything downstream of a contaminated benchmark is miscalibrated; the audit costs a day per benchmark.
- **Why Possibly Novel:** Systematic contamination audits are common in NLP now but rare for medical-imaging benchmarks.
- **Minimal Experiment:** Embedding-NN plus metadata analysis on 5 benchmarks; contamination reports; decontaminated re-scoring of public models.
- **Main Risk:** Near-duplicate thresholds need care to avoid false positives; verify flagged pairs manually.

### IDEA-C-0329
- **One-sentence idea:** Replace the VLM text encoder's output with class-mean image embeddings: if open-vocab segmentation is unchanged, "language" contributes nothing beyond class indexing.
- **Problem:** Open-vocabulary methods credit language understanding; the null — text embeddings function merely as arbitrary class anchors learnable from images alone — is never tested.
- **Core Hypothesis (falsifiable):** Substituting text embeddings with image-derived class prototypes (mean embeddings of a handful of examples) preserves most open-vocab segmentation performance on seen-vocabulary classes, with genuine language value confined to zero-example classes — bounding the linguistic contribution precisely.
- **Why Important:** Clarifies what "language-driven" methods actually use language for — with one embedding-swap experiment.
- **Why Possibly Novel:** The prototype-substitution control is absent from the open-vocab dense literature.
- **Minimal Experiment:** Embedding-swap evaluation on 4 open-vocab segmenters; seen vs zero-example class analysis.
- **Main Risk:** Prototype quality depends on example count; sweep from 1 to 100 examples.

### IDEA-C-0330
- **One-sentence idea:** Establish the noise floor for boundary metrics: does trivial input noise change boundary F-scores by more than published method gaps?
- **Problem:** Fine-grained boundary metrics may be so sensitive to irrelevant perturbations that reported inter-method differences fall inside the noise band — testable in an afternoon.
- **Core Hypothesis (falsifiable):** Imperceptible input perturbations (mild noise, one-pixel shifts, JPEG cycles) change boundary-metric scores of fixed models by amounts overlapping a substantial fraction of published method-to-method gaps — establishing per-benchmark minimum meaningful differences that many claims fail.
- **Why Important:** Minimum-meaningful-difference thresholds are standard in clinical measurement and absent in segmentation benchmarking.
- **Why Possibly Novel:** Perturbation-derived noise floors for dense metrics have not been published.
- **Minimal Experiment:** Perturbation batteries on fixed checkpoints across benchmarks; score-variation distributions vs literature gap distributions.
- **Main Risk:** Perturbation realism choices affect floors; use several conservative perturbation families.

### IDEA-C-0331
- **One-sentence idea:** Train with consistently permuted class names/semantics to measure how much models use semantic priors versus pure shape/appearance statistics.
- **Problem:** Claims that models leverage semantic structure (class relationships, plausible layouts) are rarely separated from the null that they learn arbitrary label-to-appearance mappings.
- **Core Hypothesis (falsifiable):** Models trained with permuted label semantics (consistent but meaningless class assignments) match normally trained models on standard benchmarks — current architectures and datasets do not reward semantic structure — while explicitly semantic methods (label-relation losses) show measurable permutation sensitivity, verifying the instrument.
- **Why Important:** Separates marketing ("understands anatomy") from mechanism with a training-label permutation.
- **Why Possibly Novel:** Semantic-permutation controls are unreported for dense prediction.
- **Minimal Experiment:** {normal, permuted} training × standard and semantics-exploiting methods; permutation-sensitivity comparison.
- **Main Risk:** Some semantic structure enters via pretrained weights; include from-scratch arms.

### IDEA-C-0332
- **One-sentence idea:** Apply the mask-the-lesion test systematically to medical detection papers: does the detector still fire on surrounding context when the finding itself is erased?
- **Problem:** Reported detection performance may ride on contextual shortcuts (position, co-occurring devices, patient habitus); the direct occlusion control is quick and rarely reported.
- **Core Hypothesis (falsifiable):** For a measurable fraction of published-style medical detectors, inpainting the lesion region leaves detection confidence above the decision threshold on many cases — a context-shortcut prevalence estimate per model and dataset that reframes their claimed sensitivity.
- **Why Important:** Context-firing detectors fail exactly on atypical presentations; the prevalence number belongs next to every reported AUC.
- **Why Possibly Novel:** Systematic occlusion-audit results across medical detection models are not published.
- **Minimal Experiment:** Lesion inpainting on positive cases across 5 public detectors; confidence-retention distributions; per-dataset shortcut prevalence.
- **Main Risk:** Inpainting artifacts can themselves trigger detectors; validate with artifact-only controls.

### IDEA-C-0333
- **One-sentence idea:** Re-run headline comparisons with 5 seeds and report distributions: estimate what fraction of recent single-seed SOTA claims survive.
- **Problem:** Dense-prediction papers frequently report single-run point estimates; seed variance for these pipelines is unpublished, so claim reliability is unknown at the field level.
- **Core Hypothesis (falsifiable):** Multi-seed replication of a representative sample of recent comparisons shows that a substantial fraction of claimed improvements lie within the seed-variance band — with variance itself varying enough across setups that single-seed reporting is demonstrably insufficient practice.
- **Why Important:** A field-level reliability estimate that costs only re-runs of public code — and provides the variance tables everyone should be citing.
- **Why Possibly Novel:** Seed-variance meta-analysis exists for RL and classification; the dense-prediction version does not.
- **Minimal Experiment:** 10 recent public-code comparisons × 5 seeds; distribution overlap analysis; publish variance reference tables.
- **Main Risk:** Sample selection bias; pre-register the paper-sampling rule.

### IDEA-C-0334
- **One-sentence idea:** Test zero-shot resolution transfer: evaluate published models at 2× their training resolution and watch the ranking reshuffle.
- **Problem:** Method rankings are established at fixed training resolutions; deployment uses whatever resolution arrives — if rankings don't survive resolution transfer, benchmark conclusions are conditional in an unreported way.
- **Core Hypothesis (falsifiable):** Under 2× resolution evaluation without fine-tuning, method rankings on popular benchmarks change substantially, with architectural families (hierarchical vs isotropic, CNN vs ViT) reordering predictably by their resolution-generalization mechanisms — resolution overfitting is a hidden, measurable property of current leaderboards.
- **Why Important:** One inference sweep exposes whether leaderboards predict deployment behavior across the most common test-time variation.
- **Why Possibly Novel:** Resolution-transfer stress testing of the benchmark canon has not been done.
- **Minimal Experiment:** Evaluate 10 public models at {1×, 1.5×, 2×} resolutions on 3 benchmarks; ranking-stability analysis.
- **Main Risk:** Some pipelines internally resize; instrument to guarantee true resolution change.

### IDEA-C-0335
- **One-sentence idea:** Fit a linear probe on final-layer features for the exact segmentation task: if it matches the full decoder, decoder complexity is unjustified on that benchmark.
- **Problem:** Elaborate decoders are presented as necessary; the linear-sufficiency control quantifying what the encoder already finished computing is almost never run.
- **Core Hypothesis (falsifiable):** For many trained encoder-decoder segmenters, a linear per-pixel readout on final encoder features recovers most of the full decoder's performance — decoder complexity contributes marginally on those benchmarks, and its real function (upsampling logistics vs computation) is exposed by the gap structure.
- **Why Important:** Cheap architectural accountability: measure before adding decoder machinery.
- **Why Possibly Novel:** Linear-sufficiency audits of dense decoders are unreported.
- **Minimal Experiment:** Linear probes on frozen encoders of 6 trained models; probe-vs-decoder gap decomposition by class and boundary band.
- **Main Risk:** Upsampling handling for linear probes must be standardized; use fixed bilinear protocols.

### IDEA-C-0336
- **One-sentence idea:** Diff loss implementations across frameworks: quantify how much "the same loss" differs between popular libraries and whether it exceeds paper gains.
- **Problem:** Dice/CE/boundary losses have subtly different implementations (smoothing constants, batch reduction, ignore-label handling) across frameworks; papers compare numbers across this hidden variation.
- **Core Hypothesis (falsifiable):** Training identical models with nominally identical losses from different frameworks produces performance differences comparable to a nontrivial fraction of published method gains — implementation choice is an unacknowledged experimental factor requiring disclosure.
- **Why Important:** A reproducibility microscope: names in papers do not identify the object trained.
- **Why Possibly Novel:** Cross-framework loss-equivalence measurement has not been published.
- **Minimal Experiment:** Matrix of {3 losses × 3 frameworks} on fixed data/architecture; difference distributions vs literature gaps.
- **Main Risk:** Other framework differences leak in; isolate loss modules into one training stack.

### IDEA-C-0337
- **One-sentence idea:** Test augmentation-normalization ordering: applying augmentation before versus after intensity normalization changes results more than method deltas.
- **Problem:** The order of augmentation and normalization silently varies across codebases (changing the effective augmentation distribution), and is never reported as an experimental factor.
- **Core Hypothesis (falsifiable):** Order permutations of standard medical pipelines (intensity augmentation vs z-score normalization) produce performance differences on par with published method-to-method gaps on the same benchmarks — an invisible pipeline choice with method-scale impact.
- **Why Important:** If ordering rivals method effects, papers comparing across codebases compare pipelines, not methods.
- **Why Possibly Novel:** Ordering-effect quantification for medical preprocessing pipelines is unreported.
- **Minimal Experiment:** {order A, order B} × 3 augmentation stacks × 3 datasets on fixed architecture; effect-size comparison.
- **Main Risk:** Effects may be augmentation-specific; report per-transform decomposition.

### IDEA-C-0338
- **One-sentence idea:** Zero out skip connections at inference in trained U-Nets to measure, per class, how much the architecture's signature feature is actually used.
- **Problem:** Skip connections define the U-Net paradigm and justify countless variants; their realized contribution per class and per metric in trained models is asserted, not measured.
- **Core Hypothesis (falsifiable):** Inference-time skip ablation degrades boundary metrics severely but leaves region metrics for large structures largely intact, with per-class skip reliance predictable from structure scale — the paradigm's signature component serves a narrower function than its centrality suggests, quantifiably.
- **Why Important:** Grounds architecture-variant research (skip attention, skip fusion modules) in a measurement of what skips actually carry.
- **Why Possibly Novel:** Systematic inference-time skip-ablation profiles are unreported.
- **Minimal Experiment:** Per-level and combined skip ablation on trained U-Nets across datasets; class- and metric-resolved degradation maps.
- **Main Risk:** Ablation at inference is off-distribution for the decoder; complement with skip-noise injection as a graded probe.

### IDEA-C-0339
- **One-sentence idea:** Evaluate methods against 1-pixel morphological perturbations of ground truth: if rankings flip, benchmarks measure annotation-style matching, not accuracy.
- **Problem:** If dilating or eroding all test masks by one pixel reorders method rankings, methods differ mainly in their systematic offset relative to an arbitrary annotation convention — a possibility never checked.
- **Core Hypothesis (falsifiable):** On boundary-sensitive metrics, single-pixel ground-truth morphology changes flip a substantial fraction of pairwise method rankings on popular benchmarks — published boundary superiority claims are largely claims about matching the annotation convention's tightness, and offset-calibrated evaluation removes the flips.
- **Why Important:** An hour-long test that separates delineation skill from convention matching across any leaderboard.
- **Why Possibly Novel:** Ground-truth-perturbation ranking-stability tests are not part of benchmarking practice.
- **Minimal Experiment:** Re-score 10 public models against {erode-1, original, dilate-1} test masks; pairwise ranking-flip statistics; offset-calibration correction.
- **Main Risk:** Some anatomy makes 1-pixel morphology ill-defined (thin structures); handle with topology-aware perturbation.

### IDEA-C-0340
- **One-sentence idea:** Perform compute-matched re-comparison: give baselines the proposed method's full compute (including hyperparameter search) and measure surviving gains for a sample of papers.
- **Problem:** Proposed methods receive development-time tuning that baselines never get; the implicit assumption — reported gaps reflect methods, not budget asymmetry — is the field's most consequential untested claim.
- **Core Hypothesis (falsifiable):** When baselines receive equal total compute (training plus documented search budget), a substantial fraction of sampled published gaps shrink below significance — with shrinkage predicted by the original paper's search-budget asymmetry, quantifying the field's systematic method-inflation factor.
- **Why Important:** Produces the correction coefficient everyone suspects exists; changes how reviewers and readers should discount reported gains.
- **Why Possibly Novel:** Budget-matched meta-replication with an inflation-factor estimate has not been executed for dense prediction.
- **Minimal Experiment:** Sample 8 recent comparisons with public code; re-tune baselines under matched budgets; surviving-gain analysis with pre-registered protocol.
- **Main Risk:** Budget accounting from papers is incomplete; use conservative (favor-the-paper) budget estimates.

---

*End of Batch C: 340 ideas (IDEA-C-0001 … IDEA-C-0340).*











