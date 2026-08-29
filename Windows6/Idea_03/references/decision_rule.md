# The O1/O2/O3 decision rule (Idea_03)

The pre-registered rule that converts measurements into the paper's claim.
Implemented as `pipeline.classify_outcome` — a pure function with no model
access, so it is unit-testable and releasable. Readers can apply it to their own
numbers.

Formal citations for the underlying methods (constrained decoding, linear
probing, DPO) are `CITATION NEEDED — 待人工核验`; see `literature.md` §C.

## 1. Measured quantities

All gaps are **base minus chat**; positive means the chat checkpoint is worse.

| Symbol | Definition | Confound still present |
|---|---|---|
| \(g_{\mathrm{free}}\) | Free-form IoU gap | Prose wrapper, parsing, decoding policy |
| \(g_{\mathrm{con}}\) | Grammar-constrained IoU gap | Decoding policy |
| \(g_{\mathrm{lik}}\) | Likelihood rank-acc@1 gap | **None generative** |
| \(g_{\mathrm{probe}}\) | \((\mathrm{MAE}_{\mathrm{chat}} - \mathrm{MAE}_{\mathrm{base}})/s\), image-scale normalised | Probe capacity, layer choice |

\(g_{\mathrm{lik}}\) is the only one that survives removal of generation, which
is why it is the only one the rule treats as decisive.

## 2. The rule

With pre-registered tolerance \(\tau = 0.02\):

\[
\text{outcome}=
\begin{cases}
\textbf{refuse} & g_{\mathrm{lik}} \text{ not measured}\\[2pt]
\textbf{format (O1)} & g_{\mathrm{lik}} \le \tau \ \wedge\ (g_{\mathrm{free}} > \tau \vee g_{\mathrm{con}} > \tau)\\[2pt]
\textbf{none} & g_{\mathrm{lik}} \le \tau \ \wedge\ g_{\mathrm{free}} \le \tau \ \wedge\ g_{\mathrm{con}} \le \tau\\[2pt]
\textbf{representation (O3)} & g_{\mathrm{lik}} > \tau \ \wedge\ g_{\mathrm{probe}} > \tau\\[2pt]
\textbf{policy (O2)} & g_{\mathrm{lik}} > \tau \ \wedge\ g_{\mathrm{probe}} \le \tau
\end{cases}
\]

## 3. Why the refusal branch exists

Without \(g_{\mathrm{lik}}\), a free-form or constrained gap cannot be separated
from the format confound. Reporting a "tax" from generation alone is the easiest
way to publish a wrong result here, and it is the exact failure the
pre-registered kill rule targets: *"Kill if H1 fails under constrained decoding
(formatting confound)."*

So `classify_outcome` raises rather than guessing. The discipline is in the
code, not only in the prose, because prose does not run.

## 4. Validation: the round trip

`data.make_pair` can plant any of the four answers — `none`, `format`,
`policy`, `representation` — by degrading different parts of the simulated
chat model:

| Planted mode | What is degraded | Expected signature |
|---|---|---|
| `none` | nothing | all gaps ≈ 0 |
| `format` | free-form wrapper only | \(g_{\mathrm{free}} > 0\), \(g_{\mathrm{lik}} \approx 0\) |
| `policy` | decoder estimate; tokens intact | \(g_{\mathrm{lik}} > 0\), \(g_{\mathrm{probe}} \approx 0\) |
| `representation` | visual tokens too | \(g_{\mathrm{lik}} > 0\), \(g_{\mathrm{probe}} > 0\) |

`run_smoke.py` plants each in turn and exits non-zero unless all four
round-trip. A decision function that cannot recover a planted answer must not be
pointed at a real one. **This validates the ruler, not the object measured.**

## 5. Metric definitions

**IoU.** Standard intersection over union on axis-aligned boxes. `parse_box`
normalises inverted corners so a model emitting `x2 y2 x1 y1` is not scored as a
localisation failure.

**Parse-failure rate.** Fraction of outputs containing fewer than four numbers.
Reported **separately, always**. `mean_iou` offers `count_failures=True` (failures
as 0) and `False` (parseable only); **the difference between them is the format
tax, quantified**. Folding failures into the mean is what makes a chat model look
unable to localise when it is merely talking.

**Rank acc@1.** Fraction of examples where the gold box outranks all \(k \le 16\)
distractors. Distractors are **shared** between checkpoints — otherwise a
likelihood gap could reflect an easier candidate set rather than a better model.

**Probe MAE.** Mean absolute coordinate error of a ridge-regularised linear map
from frozen visual tokens to box, fit on a train split and evaluated held out.

## 6. Why the probe is ridged

With a small train split and correlated token dimensions, an **unregularised**
least-squares fit can recover a box from noise. It would then report
"representation intact" for a checkpoint whose representation was destroyed —
biasing the rule towards **O2** exactly when **O3** is true, which is the more
consequential finding. The bias column is never penalised. `reviewer_attacks.md`
C3 requires reporting a penalty sweep so the conclusion is visibly not a
function of one hyperparameter.

## 7. Known incompleteness

- **Layer choice.** \(g_{\mathrm{probe}}\) is measured at one depth. Card E3
  sweeps layers; a gap at one layer only downgrades the claim to a sweep report.
- **Probe capacity.** Absence of *linear* decodability is not absence of
  information. If a linear probe drops and an MLP probe does not, the finding is
  *"present but not linearly accessible"* — distinct from O3 and reported as
  such, not folded into it.
- **\(\tau\) is a single global tolerance.** A per-metric tolerance would be
  better justified; 0.02 is pre-registered for all four gaps and applied
  uniformly so it cannot be tuned per outcome.
