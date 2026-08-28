# Revive Recommendations — Agent L (Stage 6)

Specific IDs the PI should pull back from the kill/drop/tier-2 piles, with the cheapest test that settles each.
Ordered by expected value. "Revive" means: give it a named slot or a named arm in the 200/50 fold — not automatic Top-20 entry.
Recommendations only; the PI decides. Evidence labels as in `audit.md`.

## 1. C-0334 — NMS-free wins are tuning artifacts (REVIVE as named arm of C-0285)

- **Status:** D-protected (revived by D with explicit reasoning), dropped by G in the Tier-B cut with the note "adversarial
  re-tuning covered by 0285's design" — one of four protected-idea overrides G said **require PI sign-off**, which was never recorded.
- **Why the drop is wrong (EVIDENCE):** D's revival note is specific and correct — DETR-line ablations tune the *proposed*
  model's components, not the classical baseline's post-processing. C-0285 (shadow tuning) is about giving baselines the
  method's *search budget* generally; nothing in the 0285 write-up names the NMS/post-processing axis. The claimed subsumption
  is an accounting convenience.
- **Cheapest test:** take one published NMS-free vs NMS comparison; re-tune only the classical baseline's post-processing
  (NMS threshold, score threshold, top-k) on val with a modest budget; report the gap shrinkage. 1–2 GPU-days, inference-heavy.
- **Risk:** genuinely subsumable if 0285's protocol is written to include post-processing as a tunable — then formalize that
  in 0285's design doc and record the sign-off. Either way, close the governance hole.

## 2. A-0199 — context-completion hallucination (REVIVE J's mutation with a bigger claim than J granted)

- **Status:** framing killed by J via HalluSegBench (arXiv 2506.21546) + HII-DPO (arXiv 2602.10425); "sliver" survives.
- **Why the kill is over-broad (EVIDENCE, both papers verified live):** both scooping papers target **VLMs** (referring-
  segmentation VLMs; captioning + DPO alignment). Neither runs the causal, training-data-grounded version: classical
  segmenters with fully known training corpora, hallucination rate as a **dose-response function of mined co-occurrence
  strength**. VLM papers cannot run this — they do not know their training data. That is not a sliver; it is the
  scientifically stronger half of the original idea.
- **Cheapest test:** mine object co-occurrence stats from ADE20K/COCO-Stuff train sets; build editing-based counterfactuals
  (inpaint the target out, per J's own "editing beats curation" note); measure hallucinated-pixel rate vs co-occurrence
  decile for 3 off-the-shelf segmenters. ~2 GPU-days.
- **Condition:** must cite both VLM papers as the motivating phenomenon and position as the mechanism/dose-response paper.

## 3. A-0028 — SAM2 teleport test: appearance vs location tracking (PROMOTE from invisible-keep to fold candidate)

- **Status:** never killed — F kept it and called it "among the best of C02" (ROI 5, feasibility 5, cheap-falsify,
  counter-intuitive) — but it missed F's top-20, so it was never Reviewer-2 attacked and appears in no supervisor ledger.
  The entire SAM2/video-memory cluster has zero visibility above tier-2 (audit Finding 7).
- **Why revive:** it is the portfolio's cheapest orphaned high-scorer, it is the only candidate that covers the SAM-video
  direction, and its psychology-transplant design (teleport probes) is exactly the genre D/E protected elsewhere
  (C-0308, B-0023). Consistency demands it get an attack, not oblivion.
- **Cheapest test:** it *is* the cheap test — one GPU-day: prompt SAM2 on frame 0, teleport the object (cut-paste or
  curated cuts), measure whether the mask follows appearance or location under temporal sparsity. Pre-register the
  either-outcome interpretation. Requires a Reviewer-2 pass first (it never had one).

## 4. C-0082-mut — SAM failure-prediction law from computable image properties (RE-SLOT the mutation)

- **Status:** D revived it as a mutation ("a validated failure-prediction law... is a different and open contribution"),
  but mutations hold no slot, so it silently exited the portfolio (G confirmed: "not in this portfolio").
- **Why revive:** batch A is SAM-centric and the emerging gravity has A-0206 (SAM forensics) but no SAM *capability-boundary*
  science. A validated failure predictor is the constructive complement to the audit cluster and pairs with A-0021
  (uncertainty-signal AUROC, tier-2) as shared infrastructure.
- **Cheapest test:** inference-only — regress SAM/SAM2 failure (IoU < τ) on computable image properties (contrast, clutter,
  boundary complexity, object scale) across 5 public domain-shifted datasets; validate the fitted law on 2 held-out domains.
- **Condition:** fresh scoop-check on SAM-failure-atlas literature first (D flagged the family as fast-moving).

## 5. A-0090 — time-to-detect for smoke (REVIVE as the evaluation layer of A-0100)

- **Status:** tier-2; F explicitly asked for this revival ("revive as the evaluation layer for any C04 keep").
- **Why revive:** A-0100 (leakage audit) alone leaves the smoke/fire direction as pure debunk; adding the TTD reframing
  turns the same paper into audit + constructive metric proposal — the exact audit-to-artifact conversion the portfolio
  lacks (audit Finding 3).
- **Cheapest test:** re-score existing public smoke-detection model outputs on video benchmarks with a TTD metric; no
  training. Days.

## 6. B-0033 — pretraining-seed variance arm of C-0136 (PROTECT THE ARM from H's kill)

- **Status:** E kept it under DP protection; G merged it into C-0136 as a named compute-partner-conditional arm and stated
  the protection "cannot be silently dropped without PI sign-off"; H then KILLED it outright ("no funder" for flagship scale).
- **Why the arm should survive the kill:** H's argument (ViT-S variance does not license flagship-scale claims) is correct
  against the *standalone paper*, and is exactly why G had already demoted it to a conditional arm. Killing the arm too
  deletes the only pretraining-stage variance data point the field has, at a ViT-S price. A bounded pilot with pre-registered
  scope ("we bound seed variance at small scale; we make no flagship claims") is honest and cheap-ish.
- **Cheapest test:** 5-seed ViT-S SSL pretrain at ImageNet-100 scale → dense-task variance components. Only with partner
  compute; otherwise keep the arm dormant-but-named. Do not let a Stage-4 verdict silently override a Stage-2 protection
  plus a Stage-2.5 merge contract — that is a governance regression regardless of the science.

## 7. A-0203 — masks no prompt can produce (SAM expressivity) (REVIVE from tier-2 if any SAM cluster slot survives K/I)

- **Status:** tier-2; F's own revive list #10 ("inherits 0017's motivation with a formal, un-scooped core" after the
  WACV 2026 kill of 0017).
- **Why revive:** if A-0206 stays a finalist, the SAM cluster needs a second, uncorrelated instrument; 0203's
  prompt-inversion design (optimize prompts to reach held-out GT masks; measure the unreachable set) is capability science,
  not forensics, so it does not stack on the audit genre.
- **Cheapest test:** gradient-based prompt inversion against ~1k held-out GT masks across 3 datasets; report unreachable-mask
  rate and its structure. ~1 GPU-week.

## 8. B-0079 — grokking in dense fine-tuning (REVIVE only if the PI wants one true moonshot)

- **Status:** E near-miss kill ("50x-horizon compute for plausible null; revive with cheap backbone if PI wants a moonshot").
- **Why listed:** the Top-5 currently contains zero long-shot discovery bets (audit Finding 4: the reviewer gradient
  eliminated ambition). If the PI wants one, this is the cheapest-bounded one E named.
- **Cheapest test:** tiny ViT + one dense task + sub-sampled data + 20x-horizon training with dense checkpointing.
  ~1 GPU-week, pre-registered null criteria.

## 9. A-0065 — clinician clicks vs simulated clicks (REVIVE conditional on a MICCAI venue decision)

- **Status:** tier-2; F: "RClicks-style work covers natural images; revive if a MICCAI-track slot exists."
- **Why revive:** the medical-executable quota (audit Finding 7) is thin; this is the cheapest clinical-facing entry that
  is *not* blocked on data-access miracles, and the RClicks precedent proves the genre's citability.
- **Cheapest test:** 2 clinicians × 30 cases pilot on public data (e.g., LIDC nodules) replaying clicks against 2 interactive
  models; measure the sim-vs-real ranking flip. Annotation-hours, no training.

## 10. C-0251 / C-0253 / C-0271 — adjudicate G's remaining protected-idea overrides (governance, not advocacy)

- **Status:** all three were D-protected and dropped/demoted by G with "requires PI sign-off" — sign-off absent.
- **Recommendation:** I do not push to revive any on the merits (G's reasons are defensible: sibling coverage, census
  downgrades). But the sign-off must be recorded, or the protection mechanism is dead letter and every future protection
  claim in this pipeline is theater. Ten minutes of PI time; do it before the Top-5 lock.

---

## Explicitly NOT revived (checked and endorsed as dead)

- **B-0332** (visual CoT theater) — the scooping paper (arXiv 2510.23482, verified live) runs the exact intervention with
  a training fix on top. H's "largest casualty" call is correct.
- **B-0136, B-0175, B-0279, A-0017, A-0051, B-0133, B-0042-as-host** — kill citations spot-checked or internally consistent;
  no grounds found to reopen.
- **A-0215 headline** — J's mutation (COCO vs Sama-COCO zero-annotation version) is the right surviving form; the
  commissioned-corpus original stays dead on cost-benefit.
