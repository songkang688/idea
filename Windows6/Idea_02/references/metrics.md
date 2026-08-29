# Metrics & split protocol (Idea_02)

Definitions for the metrics and the three split protocols. Implemented in
`src/camsplit/`; every property asserted below is covered by a self-check in
`tests/test_smoke.py`.

Formal citations for these constructions are `CITATION NEEDED — 待人工核验`
(see `literature.md` §C) — none could be verified against
`selection_history/literature_anchors.md`, and a bibtex entry reconstructed
from memory is worse than a visible hole.

## 1. The three protocols, defined by what they break

A corpus has nested groupings **camera** ⊃ **event** ⊃ **frame**. Write
\(C(i)\) for the camera of frame \(i\) and \(E(i)\) for its event. A split is a
partition \((\mathcal{T}, \mathcal{V})\) of frame indices.

| Protocol | Constraint |
|---|---|
| random | none beyond \(\mathcal{T}\cap\mathcal{V}=\emptyset\) |
| event-disjoint | \(E(\mathcal{T}) \cap E(\mathcal{V}) = \emptyset\) |
| camera-disjoint | \(C(\mathcal{T}) \cap C(\mathcal{V}) = \emptyset\) |

**Camera-disjoint implies event-disjoint; the converse does not hold.** That
asymmetry is the entire hypothesis. `camera_overlap` and `event_overlap` report
\(|C(\mathcal{T})\cap C(\mathcal{V})|\) and \(|E(\mathcal{T})\cap E(\mathcal{V})|\)
so the difference is checkable rather than assertable, and
`test_event_disjoint_STILL_shares_cameras` fails if a refactor ever collapses
the two protocols into one.

**Empty frames** carry \(E(i) = -1\) and are excluded from event-overlap
counting. They follow their camera's majority side under event-disjoint
splitting so the negative pool stays usable for H4.

## 2. Equal-N, ratio-matched comparison

Protocols produce test sets of different size and class balance, so a raw AP
difference conflates leakage with the comparison itself. `match_equal_n`
subsamples the test side towards the training-set positive ratio within
`tolerance` (default 0.02), and **raises** when it cannot — an unmatched
comparison produces no number rather than a misleading one.

## 3. Average precision

With scores \(s_i\) and labels \(y_i \in \{0,1\}\), sort descending and
accumulate
\(\mathrm{AP} = \sum_k P(k)\,\big[R(k) - R(k-1)\big]\)
over the step-wise precision–recall curve. Returns `nan` when there are no
positives — not 0, which would be indistinguishable from a real failure.

## 4. FAR at fixed recall

Take the threshold where recall first reaches \(r\) (default 0.8) and report
\(\mathrm{FAR} = \mathrm{FP}/N_{\text{neg}}\) there. Returns `nan` when \(r\) is
unreachable, rather than silently substituting the nearest operating point.

**Why FAR is primary alongside AP.** The operational question for a wildfire
tower is *how many false alarms at the recall we are required to hit*, not how
tight the box is. `proposal.md` §15 makes IoU secondary for this reason.

## 5. Cluster bootstrap over events

Resample **whole events** with replacement, recompute the statistic, take
percentile bounds.

**Why not frames.** Consecutive frames of one plume from one tower are heavily
correlated. A frame-level bootstrap treats \(n\) correlated frames as \(n\)
independent observations and reports an interval roughly \(\sqrt{n_{\text{eff}}/n}\)
too narrow — the specific way an audit like this overstates its own confidence.
`cluster_bootstrap_ci` offers no frame-level option, so the wrong version is not
available to reach for.

Returns `(nan, nan)` with fewer than two clusters: a bootstrap over one cluster
is not a bootstrap.

## 6. The camera-ID probe

Multinomial logistic regression on frozen features, reported as
`accuracy`, `chance` (majority-class rate) and `margin = accuracy − chance`.

**Two constraints on the split, both load-bearing:**

1. **Train and evaluate within training cameras.** Asking a classifier to name a
   camera it never saw is meaningless, so camera-disjoint indices are the wrong
   input.
2. **Evaluate event-disjoint.** On a random split the probe can name the camera
   by recognising the *episode* shared across the split. **Measured during
   W6-T3:** with the camera signature switched off entirely, a random-split
   probe still beat chance by ≈0.17 — pure event leakage. Two self-checks pin
   this, one asserting the event-disjoint control is near chance and one
   asserting the random-split version *is* confounded.

## 7. The empty-frame gap (H4)

\(\Delta = \mathrm{FPR}_{\text{seen cameras}} - \mathrm{FPR}_{\text{unseen cameras}}\)
over frames containing no smoke.

**Two protocol details, both got wrong first:**

1. The detector trains on **non-empty frames only**, so every empty frame is
   held out and both sides are scored under identical conditions.
2. Empty frames are partitioned by whether their **camera** was seen in
   training, regardless of which side of the split they fell on. Restricting to
   the test side puts every empty frame on the unseen side under a
   camera-disjoint split, which produced a `nan` seen-camera FPR when this was
   first written.

\(\Delta\) is `nan` when the split shares every camera. That is a real
limitation of random and event-disjoint protocols, not a bug: **H4 only exists
under camera-disjoint splitting.**

## 8. No trained loss of our own

`TinyDetector` is logistic regression on frame features — a placeholder so the
split machinery has something to score with. It has no convolution, no image
input and no localisation, which is why the package reports image-level AP and
never mAP. The real detector (`train_real_detector`) raises
`NotImplementedError`. **Windows6 has no smoke mAP.**
