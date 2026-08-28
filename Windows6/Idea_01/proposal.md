# Idea_01 proposal

## 1. Executive summary

**One-liner:** On CT, SAM AMG may be doing intensity clustering, not semantic objectness.

**Abstract (HYPOTHESIS, not measured):** Foundation promptable segmenters are used as automatic proposal generators on CT. Prior evaluations show SAM/SAM2 are sensitive to windowing and weak on low-contrast CT (KNOWN FACT from literature, e.g. SAM2 CT reviews). That is consistent with, but does not prove, a stronger claim: AMG’s mask inventory is approximately equivalent to clustering in HU (or windowed 8-bit) space. We specify a **pre-registered equivalence test** plus **causal counterfactuals** that Reviewer #2 required: edge-preserving intensity remaps vs intensity-preserving texture randomization. **No experimental numbers are claimed.**

## 2. Motivation

If AMG ≈ k-means on CT, then (i) papers that treat AMG as semantic pseudo-labels are injecting intensity superpixels; (ii) MedSAM-style adaptation may be fighting the wrong failure; (iii) a 1-line classical baseline belongs on every SAM-CT paper.

## 3. Problem

Let \(I\) be a CT slice after a documented window/level map \(W\). AMG produces a set of binary masks \(\mathcal{M}_{\mathrm{AMG}}\). A clustering method \(C\) (k-means, GMM, multi-Otsu) produces \(\mathcal{M}_C\). Superpixels \(S\) (SLIC) produce \(\mathcal{M}_S\).

**Question:** Is \(\mathcal{M}_{\mathrm{AMG}}\) closer to \(\mathcal{M}_C\) than to \(\mathcal{M}_S\), and does it **track** intensity-only interventions?

## 4. Core hypothesis

**H1:** After a fixed clinical window, Hungarian-matched mean IoU(\(\mathcal{M}_{\mathrm{AMG}},\mathcal{M}_{kmeans}\)) > IoU(\(\mathcal{M}_{\mathrm{AMG}},\mathcal{M}_{\mathrm{SLIC}}\)) on a pre-registered CT subset.

**H2 (causal):** An edge-preserving intensity remap changes AMG more than an intensity-preserving texture shuffle (same edge map).

**H3:** The H1 gap is stable across an AMG hyperparameter grid and 2–3 windows. If it is not, the finding is a **setting artifact** → kill or mutate.

## 5. Key insight

Windowing is a monotone intensity map. If we do not sweep windows, “AMG ≈ clustering” can be **manufactured by preprocessing** (Reviewer #2). The paper is the **counterfactual**, not the correlation.

## 6. Novelty (precise)

Closest work **evaluates** SAM on CT (Dice vs organs, window sensitivity). We did **not** find an equivalence test of AMG vs HU clustering with causal intensity/texture arms (EVIDENCE: Stage 3 assassin, novelty_conf ~0.6; Reviewer #2: survive only with those arms).

Difference: mechanism + pre-registered multi-metric agreement, not “SAM is bad on CT.”

## 7–28.

See `literature.md`, `experiments.md`, `reviewer_attacks.md`, `roadmap.md`, `diagrams/`, `src/`.
