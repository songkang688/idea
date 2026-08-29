# Reviewer Attacks & Responses — C-0306

Sources: Stage-4 K's reviewer-2 attack (`stage4_agent_K/reviewer2_attacks.md` §27 — EVIDENCE,
includes the mandated freshness re-search), Stage-2 D's attack (§E1), Stage-6 O/Q battle records,
plus this package's own red-team. Each attack gets: the strongest form, our response, and the
residual risk we accept. Summary table at the end.

---

## A1. "The step you attack is already handled or deletable" (K's harshest rejection)

**Attack.** "Two conformal-OD papers give guarantees despite NMS (SeqCRC arXiv:2505.24038 calibrates
after it; arXiv:2605.07549 leaves it upstream), and IoU-aware calibration (WACV 2024,
doi:10.1109/wacv57701.2024.00478) removes NMS entirely. So the step is either handled downstream or
deletable. Who needs coverage-preserving *suppression*?"

**Response.** (i) SeqCRC's guarantee *conditions on the post-NMS list*: an object whose covering
candidates were all suppressed never enters the event space. That is a formally valid guarantee about
a different population — and the size of the excluded population is unmeasured. Our E1 measures it;
our Proposition 1 shows post-NMS calibration returns q̂ = +∞ (nominal unachievable at any threshold)
once blind+miss > α, so "handled downstream" is arithmetically false in exactly the strata where
suppression bites. (ii) "Deletable" concedes our premise — that NMS is the problem — and replaces it
with an output contract (many boxes, implicit duplication modeling) whose coverage/set-size economics
WACV 2024 never characterizes. It is our mandated baseline; H2 is falsifiable against it, and if it
dominates the frontier we pre-registered the pivot (characterization result) and will say so.

**Residual risk.** If the gate fails (blind ≈ 1% everywhere), A1 wins on the merits — by design we
then ship the measurement note instead of the method (that outcome is priced in, not fatal).

## A2. "Downstream users don't want candidate sets, they want detections" (K's leftover)

**Attack.** "A coverage-preserving *set* with duplicates is not a detection output. Your method's
output is unusable, so the practical story leaks."

**Response.** Consumability is a headline metric, not an afterthought: duplicates-per-covered-GT and
set size at matched coverage are in every E4/E5 table. CPS at r = 1 keeps exactly one representative
per spatial cluster — an NMS-shaped output — and in the synthetic demo (MEASURED, synthetic;
mechanism only) cut duplicates/GT ~2.4× vs keep-all at ~half the set size. Also symmetrical: the
WACV-2024 no-NMS alternative asks deployments to accept the *same* many-box contract, and DETR-family
outputs are top-k sets too. If CPS's duplicate rate at nominal coverage exceeds plain NMS's by an
unacceptable factor on real data, E5 will show it and the claim scopes down honestly.

**Residual risk.** "Bounded duplicate rate" on real data is a HYPOTHESIS until E5 runs.

## A3. "Crowded-scene NMS failure is old news" (conceded by K, qualitatively)

**Attack.** "Soft-NMS (2017), Adaptive-NMS (2019), CrowdDet (2020) — recall loss from NMS in crowds
is a decade of literature. You rebranded a known failure as 'coverage destroyed'."

**Response.** Cited in paragraph one, and the distinction is load-bearing: that line measures
AP/miss-rate consequences and proposes score-shaping fixes with **no guarantee semantics**. New here:
(a) the blind-spot rate *with respect to calibrated prediction sets* — a quantity that does not exist
outside the conformal framing; (b) the achievability certificate (a statement AP cannot express);
(c) a suppression rule whose output provably retains a distribution-free guarantee. This is why K's
verdict makes the formal bound non-optional: without Theorem 1 the paper would indeed collapse into
A3. With it, the crowded-NMS literature becomes our motivation section, not our competitor.

**Residual risk.** A reviewer may still price the measurement as incremental if the gate opens only
marginally (2–5%); SCOPE-STOP handles that with a narrower paper.

## A4. "Your own kill criterion says this may be a footnote"

**Attack.** "You admit blind rate might be ~1% everywhere. Why fund/review a maybe?"

**Response.** Because the maybe costs 2–4 GPU-days and both branches publish (measurement note = the
first quantified license for the field's post-NMS conditioning concession; it will be cited by every
conformal-OD paper that makes the concession). Gate-first ordering is the design's virtue: no method
is built on an unmeasured premise. Pre-registration of the materiality threshold means the reader
never depends on our enthusiasm.

**Residual risk.** None beyond the priced gate outcome; this attack argues for the design.

## A5. "Exchangeability is violated — objects in an image are correlated"

**Attack.** "Your guarantee treats pooled GT objects as exchangeable; within-image correlation breaks
finite-sample validity at the object level. The guarantee is not what the abstract will claim."

**Response.** Stated in the math section (proposal §10), not hidden: identical concession to the
existing conformal-OD literature (SeqCRC pools objects too). Pre-committed robustness arm: image-level
exchangeable unit (scene-max nonconformity) run alongside; if the two disagree materially, image-level
becomes primary (pre-registered in E6). All CIs use image-level cluster bootstrap. Note the *blind
spot itself* is calibration-free — a counting fact about NMS — so H1 does not depend on
exchangeability at all; only the pipeline-coverage comparisons do.

**Residual risk.** Object-level claims may need the weaker "approximately valid" phrasing in the
final paper; coverage headline then quotes the image-level unit.

## A6. "Your synthetic numbers are tuned to show the effect"

**Attack.** "The generator was constructed so the blind spot appears. The prototype tables are
propaganda."

**Response.** Correct, and the package says so itself in every table (MEASURED (synthetic), tuned so
*both* K-regimes are visible — including the footnote regime where NMS is harmless). Synthetic
numbers validate machinery (e.g., the exact theorem check, the q̂ = +∞ certificate behaviour) and are
quarantined; no real-data claim exists in this package, and E0 numbers are barred from the paper's
results sections (experiments.md, statistical discipline).

**Residual risk.** None if discipline holds; the discipline is written into the protocol.

## A7. "CPS is a shell game: calibrate stricter, spend the slack"

**Attack.** "τ_cal = τ + (1−κ) just buys slack that suppression spends. A tuned score threshold +
vanilla NMS could trace the same coverage/size curve without your theorem."

**Response.** The trivial threshold-sweep anchor is in the baseline set (E4) precisely to test this.
Two answers: (a) empirical — the frontier plot either shows separation or it doesn't, per stratum, and
we publish it either way; (b) formal — no threshold can recover a blind object (coverage 0 in the
surviving pool), so once blind+miss > α, *every* threshold+NMS pipeline is capped below nominal
(Prop. 1) while CPS provably reaches it. The difference is qualitative in exactly the strata where the
gate opened. What a tuned threshold CAN match is the sparse regime — where we make no method claim.

**Residual risk.** In intermediate strata (blind+miss ≲ α) CPS's advantage is quantitative, not
qualitative; the frontier decides, and might be tight.

## A8. "You will be scooped before camera-ready" (K: urgency confirmed)

**Attack.** "Two conformal-OD papers in ~12 months; a third is expected within months and may contain
your measurement or a coverage-aware suppression rule."

**Response.** Priced as binding process rules (proposal §25): freshness re-search at proposal freeze,
experiment freeze, and quarterly (queries logged in literature.md §7); execution stop-loss (seat
converts to kill if not started within the quarter — Q); two-quarter total clock (K). The gate is
days-cheap and runs first, making the measurement ours almost immediately after a start decision. If
a print lands with the suppression rule but not the measurement, the measurement note + certificate
still stands (smaller paper, still first on the quantity).

**Residual risk.** Real and irreducible — this is the portfolio's fastest clock (Q: "the conformal-OD
field is moving on a months-scale clock and can print first").

## A9. "GT quality in crowded datasets contaminates the blind/miss split" (self-red-team)

**Attack.** "CrowdHuman/LVIS have missing and inconsistent annotations; your 'blind' verdicts depend
on trusting GT boxes in exactly the scenes where GT is least trustworthy."

**Response.** E1-S sensitivity protocol: ignore/crowd-region exclusion, exhaustive-annotation-only
LVIS categories, and the conditional blind|detected form (robust to missing GT since it conditions on
a pre-NMS covering candidate existing). Pre-registered tripwire: if a gate cell crosses the
materiality boundary between variants, the conditional table governs and the discrepancy is reported.
We deliberately do not import the GT-epistemology program (that is C-0338's seat).

**Residual risk.** A hostile reviewer can still demand a small manual audit of blind-flagged objects;
budgeted as an optional Week-2 half-day (visual panel of ~100 sampled blind cases — which is also
Fig. 1's qualitative material).

## A10. "Per-detector guarantees don't compare across detectors" (self-red-team)

**Attack.** "Scores are uncalibrated across models; your cross-detector frontier pools
incomparables."

**Response.** Validity never pools: q̂ is per-detector by construction. Cross-detector material is
presented as per-detector panels; no pooled-score statistic appears anywhere in the protocol
(proposal §19.7).

**Residual risk.** Minimal; presentation discipline.

---

## Summary table

| # | Attack | Strongest source | Response asset | Residual risk |
|---|---|---|---|---|
| A1 | handled downstream / deletable | K | E1 + Prop. 1 + mandated WACV-2024 baseline (E4) | gate may fail → note branch |
| A2 | sets aren't detections | K leftover | E5 consumability + r=1 CPS + duplicates metric | real-data duplicate rate unknown |
| A3 | crowded-NMS is old news | K (conceded) | conformal framing + certificate + Theorem 1 | marginal-gate pricing |
| A4 | maybe a footnote | self/K | gate-first economics; both branches publish | none (priced) |
| A5 | exchangeability | self/field | §10 caveat; image-level arm; cluster bootstrap; H1 calibration-free | weaker object-level phrasing |
| A6 | synthetic tuned | self | MEASURED(synthetic) quarantine; E0 barred from results | none if discipline holds |
| A7 | τ_cal shell game | self | threshold-sweep anchor + Prop. 1 qualitative separation | tight frontier in mid strata |
| A8 | scooped | K/Q | freeze/quarterly re-search; stop-loss clocks; gate-first | irreducible, fastest clock |
| A9 | crowded GT quality | self | E1-S sensitivity + conditional form + tripwire | manual-audit demand |
| A10 | cross-detector pooling | self | per-detector q̂ and panels | minimal |
