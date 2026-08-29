# Math (Idea_01)

Definitions for the three pre-registered metrics and the two diagnostics.
Implemented in `src/amgclust/metrics.py`; every property asserted below is
covered by a test in `tests/test_smoke.py`.

Formal citations for these classical constructions are
`CITATION NEEDED — 待人工核验` (see `literature.md` §C) — none could be verified
against `selection_history/literature_anchors.md`, and a bibtex entry
reconstructed from memory is worse than a visible hole.

## Notation

\(\mathcal{A}\) is the AMG mask inventory, \(\mathcal{B}\) a baseline mask set.
AMG returns **nested, overlapping** masks; clusterers return a **partition** of
\(k\) classes. The two objects have different shapes, and most of the care
below is about not letting that difference masquerade as (dis)agreement.

## 1. Hungarian IoU — matched-pair quality

\[
\mathrm{IoU}_{\mathrm{hung}}(\mathcal{A},\mathcal{B})
=\frac{1}{\min(|\mathcal{A}|,|\mathcal{B}|)}
\sum_{(A,B)\in \pi^{\star}} \mathrm{IoU}(A,B),
\qquad
\pi^{\star}=\arg\max_{\pi \text{ one-to-one}} \sum_{(A,B)\in\pi}\mathrm{IoU}(A,B)
\]

Solved exactly. `scipy.optimize.linear_sum_assignment` when available,
otherwise a pure-numpy \(O(n^3)\) augmenting-path solver — so the metric is
optimal, not greedy, with numpy alone.

**Why \(\min(|\mathcal{A}|,|\mathcal{B}|)\) and not \(|\mathcal{A}|\).** The
original prototype divided by \(|\mathcal{A}|\), which folds the cardinality gap
into the agreement score: with \(|\mathcal{A}|\approx 50\) nested AMG masks
against \(k=8\) clusters, at most 8 pairs can match and the other 42 contribute
zero, so a structurally perfect subset match reports ≈0.03. Measured on the
synthetic phantom during W6-T3, that is exactly what happened. Cardinality
mismatch is a real difference — so it is reported explicitly (§4) rather than
smuggled into the agreement number.

**Why not greedy.** Greedy matching takes the locally best pair first and can
be forced into a bad remainder, so an over-segmenting method can score well by
matching *order*. `test_hungarian_beats_greedy_on_a_trap` pins this.

Properties: \(\mathrm{IoU}_{\mathrm{hung}}(\mathcal{A},\mathcal{A})=1\);
disjoint sets give 0.

## 2. Adjusted Rand Index — partition agreement

Paint each mask set into a pixel label map, then over the contingency table
\(n_{ij}\) with row sums \(a_i\), column sums \(b_j\), \(N\) pixels:

\[
\mathrm{ARI}=
\frac{\sum_{ij}\binom{n_{ij}}{2}-\Big[\sum_i\binom{a_i}{2}\sum_j\binom{b_j}{2}\Big]\big/\binom{N}{2}}
{\tfrac{1}{2}\Big[\sum_i\binom{a_i}{2}+\sum_j\binom{b_j}{2}\Big]-\Big[\sum_i\binom{a_i}{2}\sum_j\binom{b_j}{2}\Big]\big/\binom{N}{2}}
\]

Chance-corrected: 1 for identical labellings, ≈0 for independent ones. Both
pinned by tests.

**Painting rule.** Overlaps resolve to the **smaller** mask
(`masks_to_label_map` paints largest-first so smaller masks land on top),
otherwise a nested AMG child is erased by its own parent and the label map
misrepresents the inventory. Label 0 means unassigned.

## 3. Boundary-F — contour placement

Boundary pixels are those whose 4-neighbourhood contains a different label.
With tolerance \(\tau\) pixels (default 2), and \(\delta_\tau\) a dilation:

\[
P=\frac{|\,\partial\mathcal{A}\cap\delta_\tau(\partial\mathcal{B})\,|}{|\partial\mathcal{A}|},\quad
R=\frac{|\,\partial\mathcal{B}\cap\delta_\tau(\partial\mathcal{A})\,|}{|\partial\mathcal{B}|},\quad
F=\frac{2PR}{P+R}
\]

**EXPECTED (`proposal.md` §19):** this will be the least discriminative of the
three, because intensity clusterers and superpixels both place edges at
high-gradient locations. It is reported anyway. A pre-registered metric that
turns out uninformative is reported as uninformative, not dropped.

## 4. Diagnostics — reported, not hypothesis-bearing

**Coverage IoU** (directional, many-to-one — the original set formula):

\[
\mathrm{IoU}_{\mathrm{cov}}(\mathcal{A},\mathcal{B})=\frac{1}{|\mathcal{A}|}\sum_{A\in\mathcal{A}}\max_{B\in\mathcal{B}}\mathrm{IoU}(A,B)
\]

Asks "is every AMG mask explained by *some* cluster?" rather than "do the sets
pair up?". Not symmetric:
\(\mathrm{IoU}_{\mathrm{cov}}(\mathcal{A},\mathcal{B})\neq\mathrm{IoU}_{\mathrm{cov}}(\mathcal{B},\mathcal{A})\).

**Cardinality ratio** \(|\mathcal{A}|/|\mathcal{B}|\). Reported on every row so
no reader can mistake a counting artifact for agreement.

## 5. Interventions

**Intensity remap.** \(f\) strictly monotone on \([\,\min I,\max I\,]\); the
default is a gamma map on the normalised range. Monotonicity implies the
*ordering* of pixel values is preserved, hence edge **locations** survive even
though contrast is redistributed. `check_remap_is_monotone` verifies it on the
realised output rather than trusting the parameterisation, and
`intensity_remap` raises on \(\gamma \le 0\).

**Texture shuffle.** On each \(t\times t\) tile \(T\): permute the residual
\(T-\bar{T}\) and add \(\bar{T}\) back, so \(\bar{T}\) is preserved exactly.
`check_shuffle_preserves_tile_means` verifies it to 1e-9. That check is what
licenses calling the arm "intensity-preserving"; without it any AMG response
could be an intensity response.

**Read-out.** With \(s_{\bullet}=\mathrm{IoU}_{\mathrm{hung}}(\mathcal{A}_{\text{orig}},\mathcal{A}_{\bullet})\),
the mechanistic claim needs \(s_{\mathrm{int}} \ll s_{\mathrm{tex}}\).

**Known incompleteness (C1 in `reviewer_attacks.md`).** The two arms are not
matched on high-frequency energy: shuffling a residual raises it, and
region-growing methods fragment under noise for reasons unrelated to
objectness. The tile-size sweep \(t\in\{4,8,16\}\) detects the failure — a
direction flip voids the arm — but does not *remove* the confound. A
noise-matched design would be stronger and is not currently specified.

## 6. No trained loss

There is no training anywhere in Idea_01. Clustering is k-means / multi-Otsu /
GMM on scalar HU (or the windowed 8-bit image); SLIC is joint
\((x, y, \text{intensity})\) k-means. Nothing is fit to a label.
