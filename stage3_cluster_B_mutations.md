# Stage 3 — Cluster B Mutations (6)

Ideas whose original claim was killed or wounded by prior work but which contain a salvageable, sharper question.
Each mutation states: original claim, what killed/wounded it, the mutated claim, and why the mutation survives the
same attack.

## M1 — B-0007 (PROTECTED) → "Mirror-Cost": a quantitative audit of laterality damage from naive flipping
- Original: laterality-aware flipping augmentation for lateralized anatomy.
- Wounded by: the fix is community folklore; every practitioner "knows" not to mirror lateralized structures, so a method paper is unpublishable.
- Mutation: drop the method. Run the first controlled cross-task audit of what naive horizontal flipping actually costs on lateralized structures (which tasks, how much Dice/volume bias, which failure modes), and publish a when-to-flip decision rule keyed to measurable task properties.
- Survives because: the folklore has no published number; audits of silent-default augmentations have precedent value; falsifiable cheaply on public datasets.

## M2 — B-0069 → folded into B-0062 as the benchmark-validity arm
- Original: validate fuzzy-boundary metrics against human quality judgments of smoke/fire masks.
- Wounded by: standalone metric-validation studies are thin, and without physical ground truth the human judgment is itself unanchored.
- Mutation: becomes the evaluation arm of B-0062 — candidate soft-boundary metrics are validated jointly against (a) physically recovered per-pixel transmittance and (b) human judgments, so metric validity is anchored to physics.
- Survives because: as part of B-0062 it inherits the physical ground truth that makes the validation meaningful.

## M3 — B-0078 → "Tone-mapping destroys fire evidence": the sensor-pipeline hypothesis
- Original: fire-confuser benchmark with HDR captures.
- Wounded by: RGB confuser benchmarks already exist (FIgLib/SmokeyNet line); "another benchmark" is not a contribution.
- Mutation: test the specific hypothesis that camera tone-mapping destroys the radiometric evidence separating fire from confusers (sunset, fog, reflections), by capturing paired RAW/HDR + tone-mapped data of fires and confusers and measuring the classification/segmentation gap recoverable from RAW.
- Survives because: it is a falsifiable physics claim about *why* confusers confuse, not another dataset; RAW-vision literature supplies method but has never touched fire detection (search found no direct prior).

## M4 — B-0159 → Convention tokens with interpolation and controlled-relabeling validation
- Original: learned tokens encoding annotation conventions.
- Wounded by: dataset-conditioning tokens exist in adjacent literatures; unvalidated "convention" semantics would be attacked as relabeled dataset tokens.
- Mutation: the claim becomes the *validation*: convention tokens are real iff (a) interpolating between two conventions' tokens produces masks that raters place between the conventions, and (b) tokens trained on controlled relabelings (same images, differing only in written convention) recover the convention axis. Pairs with B-0112's convention-shift formalization.
- Survives because: the controlled-relabeling ground truth is the missing ingredient no prior token work has; B-0112+B-0159 together form one defensible program.

## M5 — B-0362 → Decision-flip-rate audit of published SOTA deltas
- Original: measure correlation between segmentation metrics and downstream decisions.
- Wounded by: Metrics Reloaded (Maier-Hein et al., Nature Methods 2024) already provides metric-pitfall guidance; a general "metrics can mislead" paper is redundant.
- Mutation: take N published SOTA-claiming deltas from recent segmentation papers; recompute each under distinct legitimate decision-rule families (clinical volume thresholds, boundary-tolerance rules, detection-style rules); report the fraction of published claims that flip. A meta-scientific audit with a single headline number.
- Survives because: Metrics Reloaded gives guidance, not an audit of the published literature's fragility; the flip rate is new, decision-relevant evidence.

## M6 — B-0366 → Calibrated human-in-the-loop annotation-collapse simulation
- Original: simulate multi-generation dataset ecosystems where models train on model-assisted annotations.
- Wounded by: generative model-collapse dynamics are published (Shumailov et al., Nature 2024); an uncalibrated simulation would be dismissed as speculation. Its intended empirical arm (B-0244, measuring anchoring) was itself killed — OSAIRIS (Clinical Oncology 2025) already measured planted-error catch rates in hospital practice.
- Mutation: use the *published* anchoring/catch-rate measurements (OSAIRIS: 72-88% error mitigation) as calibration parameters for a multi-generation simulation of the annotation flywheel (model → assisted labels → retrained model), characterizing drift/collapse regimes and the blind-case ratio needed to stabilize the ecosystem.
- Survives because: human-verified loops are qualitatively different from generative self-consumption (the correction rate bounds the dynamics), the calibration data now exists in the literature, and no one has connected the two.
