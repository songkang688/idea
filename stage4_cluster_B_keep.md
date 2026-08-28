# Stage 4 — Cluster B Keep List (7 survivors)

Reviewer #2 (Cloud Sub-Agent K) attack round over the 20 Stage-3 Cluster B decision units (14 KEEP + 6
mutations, M2 pre-folded into B-0062). Standard: reject as hard as possible; **keep only if a realistic
experiment shuts the reviewer up.** Full attacks in `stage4_cluster_B_attacks.md`; kills in
`stage4_cluster_B_killed.md`.

Each survivor: the strongest attack Reviewer #2 could mount, and the experiment that answers it.

---

## 1. B-0112 (+ M4/B-0159 merged) — Convention-shift program: formalization, label-free-audit detector, convention tokens

- **Strongest attack:** "Your 'label-free' detector needs target annotations to compute disagreement, and your
  simulated margin-erosion conventions are strawmen — real convention differences are entangled with site
  appearance shift, so the detector misfires exactly where it matters. Castro et al. already named the
  phenomenon; separately, your convention tokens are just dataset tokens with a new name."
- **Shutting-up experiment:** build *real* convention variants at zero annotation cost from nested label
  hierarchies on identical images (e.g., enhancing-tumor vs tumor-core vs whole-tumor definitions), plus one
  bounded controlled relabeling under two written guidelines. Pre-registered three-way test on identical
  images: (a) adaptation methods harm under pure convention shift, help under pure covariate shift;
  (b) detector separates the regimes at stated AUROC (claim scoped to dataset audits); (c) tokens trained on
  controlled relabelings recover the convention axis and interpolate monotonically under blinded rater
  judgment. Identical-image construction removes the appearance confound by design.
- **Why merged:** taxonomy/detector and token method are each too thin alone; together the validation chain
  (formal definition → detector → controllable representation) closes.

## 2. B-0121 (PROTECTED) — Wrong-support counterfactual audit of few-shot segmentation

- **Strongest attack:** "Foreground bias is documented (Lang et al. CVPR 2022) and a 2024 mitigation wave
  already exists (TBS, AENet — searched this session); worse, on single-object benchmarks a wrong support is
  uninformative, so your audit measures benchmark degeneracy, not model pathology. Evaluation-only, workshop
  scale."
- **Shutting-up experiment:** N public FSS checkpoints × matched wrong-class supports; report
  support-sensitivity scores *stratified by query complexity* (single- vs multi-object, distractor
  present/absent), separating benchmark degeneracy from model insensitivity — indicting each on separate
  counts. Days of compute, zero training. No published counterfactual audit exists (searched); if the score
  reorders the leaderboard, it becomes a mandatory reported number; if all methods collapse appropriately,
  the field's validity is certified — an informative negative only the audit provides.

## 3. B-0212 — Blending-artifact detectability → synthetic-to-real transfer-gap law

- **Strongest attack:** "Your correlation is confounded: better generators improve realism and blending
  together, so 'detectability predicts the gap' is generator quality in a trench coat. And a probe detecting
  artifacts doesn't prove the lesion model uses them."
- **Shutting-up experiment:** the causal ladder — hold generator and image content fixed, vary *only*
  compositing (cut-paste → Poisson → harmonization → adversarial anti-artifact blending); show probe-AUROC
  ordering predicts real-set performance ordering at fixed content. Then the reverse intervention: inject
  artifacts into otherwise-identical composites and watch the gap reopen — direct evidence of shortcut *use*,
  not just artifact existence. Deliverable the field adopts: report probe-AUROC as a hygiene number for any
  synthesis pipeline.

## 4. B-0222 — Thin-structure fidelity floor of latent diffusion + downstream penalty

- **Strongest attack:** "The field already believes latent compression kills thin structures and is engineering
  around it (MedVAE; sparsity-preserving vessel VAEs — searched this session); your floor is a number for a
  moving target, and your own risk statement admits you can't separate generation failure from conditioning
  failure."
- **Shutting-up experiment:** ship a *protocol*, not a constant. Autoencoder round-trip arm (encode-decode real
  images containing calibrated-width structures — no generation, no conditioning) cleanly isolates compression
  fidelity; survival-vs-width curves across k autoencoders × downsampling factors give every current and future
  generator a datasheet number. Close with matched-compute pixel- vs latent-space training on a real
  thin-structure task, showing recall deficit tracks the measured floor — converting community belief into a
  when-to-use-pixel-space decision rule.

## 5. B-0230 (PROTECTED) — Label-cleanliness vs image-distribution decomposition of synthetic data

- **Strongest attack:** "Your premise is false for the dominant pipeline — generative synthetic labels are NOT
  clean (SENSE documents generative instability) — and your 'human-matched' noise model determines the headline
  number: garbage calibration in, garbage decomposition out."
- **Shutting-up experiment:** scope claims to pipelines where labels ARE clean by construction
  (rendered/simulated data — a huge real segment); calibrate noise injection from *measured* multi-annotator
  disagreement on public multi-rater data rather than parametric assumptions; run the pre-registered 4-arm grid
  {real, synth, synth+matched-noise labels, real+consensus-cleaned labels} across data scales × ≥2 tasks, and
  report decomposition-vs-noise-model sensitivity as a first-class result. Clean falsification: if noise
  injection doesn't move synthetic utility, "it's the images" — equally decision-relevant for the
  generation-vs-annotation-QC investment question.

## 6. B-0331 — Report negations as spatially grounded negative supervision

- **Strongest attack:** "Organ-scale negatives from 'no pneumothorax' are nearly information-free — any decent
  model already predicts negative there; your FP reduction is trivial prior-tightening obtainable from a
  class-frequency prior without reading a single report. And atlas misgrounding poisons labels exactly in
  deviant-anatomy cases."
- **Shutting-up experiment:** information-content controls on public report+image data at MIMIC-CXR scale:
  negation negatives vs (a) matched class-prior baseline (same negative mass, no reports) and (b)
  permuted-report negatives (negations from other patients). Gain over both controls is per-patient
  information — the exact quantity the attack denies. FP deltas reported per finding class stratified by
  negation frequency; poisoning bounded via conservative margins + sensitivity sweep. If negation negatives
  don't beat the matched-prior control, the idea is dead — decisive either way.

## 7. M5 (from B-0362) — Decision-flip-rate audit of published SOTA deltas

- **Strongest attack:** "The flip rate is an artifact of rule selection — thresholds near the operating point
  flip everything, lax rules flip nothing — and you can't get the checkpoints anyway, so your sample is biased
  toward reproducible pipelines."
- **Shutting-up experiment:** pre-register decision-rule families drawn *verbatim* from clinical/operational
  guidelines (RECIST 1.1 categories, dose-volume constraints, deployed alarm thresholds) before computing any
  flip; report the flip rate as a surface over the rule grid with sensitivity analysis, not one number; audit
  only public-checkpoint pairs and report the auditable fraction as a reproducibility finding in itself.
  Supporting evidence found this session: automated-vs-manual RECIST studies show category agreement of only
  κ 0.67–0.81 even at DSC ≈0.85, and AI assistance shifted reader scores across progression boundaries in up to
  37.5% of cases — decision-level disagreement is demonstrably large, and no published-delta flip audit exists.

---

## Portfolio shape after Stage 4

- **Evaluation-validity axis:** B-0121 (FSS audit), M5 (decision-flip audit) — both pure-analysis,
  headline-number papers.
- **Synthetic-data science axis:** B-0212 (compositing shortcut), B-0222 (fidelity floor), B-0230 (value
  decomposition) — three separable measurement papers with causal arms.
- **Supervision-mining axis:** B-0331 (negation negatives) — archive-scale free supervision with decisive
  controls.
- **Convention program:** B-0112+M4 — the one methods-flavored survivor, protected by its controlled-relabeling
  validation design.
- Protected survivors: B-0121, B-0230. Protected kills: B-0058, B-0353 (protection not honored where the attack
  is fatal — consistent with Stage-3 precedent).
