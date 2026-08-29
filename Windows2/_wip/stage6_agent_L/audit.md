# Stage-6 Meta-Review Audit — Agent L (temporary deputy PI / auditor)

Role: adversarial audit of the Windows2 pipeline (supervisor + agents A–K) before the Top-5 lock.
I do NOT pick the final 3. I read all Stage-1/2/4 outputs and the supervisor ledgers; I modified none of them.
Every finding is labeled **EVIDENCE** (verifiable in-repo text or a live-searched URL fetched this session) or **HYPOTHESIS** (my inference).
All URLs below were returned by live web search during this audit. No invented papers.

---

## Finding 1 — The #1 gravity well's "afternoon pilot" was already run in 2022, by the original VPT paper

**EVIDENCE.** The pipeline's most-protected idea, B-0114 ("VPT tokens as trainable registers"), was sold by Agent E as
"the frozen-random-token control is an afternoon; every outcome... is publishable" (E report, bet #1), was mission-protected
by the supervisor, and its pilot was listed as E's #1 information request ("If random tokens reproduce ≥30% of VPT's gain,
0114 becomes the batch's flagship... if 0%, 0114 drops to mid-list").

The original VPT paper (Jia et al., ECCV 2022, https://arxiv.org/abs/2203.12119) already ran this control. Its ablation
(Fig. 11) compares **Prompt-Fixed** (prompts appended but kept frozen during fine-tuning — i.e., frozen random tokens) against
Prompt-Learned and Linear, and concludes: *"updating prompt embeddings (Prompt-Learned) offers significant gains, while
Prompt-Fixed yields comparable results w.r.t. Linear... the final performance of VPT is mainly contributed by the learned
prompt embeddings instead of the enlarged sequence length."*

By E's own pre-registered decision rule ("if 0%, drops to mid-list"), B-0114 should have dropped to mid-list in Stage 2 —
the ≈0% answer has been in print since 2022. Agent H's Reviewer-2 attack cited the VPT paper in its fresh-hits list but did
not surface this specific ablation; H's 4-arm redesign (attention-bias arm, register-equipped backbones, dense tasks) is what
actually keeps the idea alive, because VPT's ablation was classification-only (VTAB) and register effects matter for dense
prediction. **The mechanism paper survives; the flagship sales pitch does not.**

**HYPOTHESIS.** Five agents (E, G's census, the supervisor's ledger, H, and the PI notes) repeated the "afternoon pilot"
framing without anyone re-reading the original paper's ablation section — a compounding-citation echo, the exact failure
mode this pipeline was built to catch in *other people's* papers.

Additional freshness pressure on the same idea (**EVIDENCE**): the register-mechanism space is being formalized fast —
"A Unifying View of Attention Sinks" (https://arxiv.org/html/2606.08105v1) splits register function into NOP vs broadcast
mechanisms with concrete diagnostics on DINOv2-reg, and "Do All Vision Transformers Need Registers?" (cited by H,
https://arxiv.org/html/2603.25803) reassesses across architectures. A B-0114 execution that does not adopt the NOP/broadcast
diagnostic axes will look coarse at review time.

## Finding 2 — A-0061, the only "bare SURVIVE" in batch A, is not bare

**EVIDENCE.** Agent J granted A-0061 (topology lost at checkpoint-selection time, not training time) the batch's only
unconditional SURVIVE, writing "no fresh competitor (the field keeps building topology losses, which is the point)."
Live search this session found:

- **HyperTopo-Adapters** (arXiv, Jan 2026, https://arxiv.org/html/2601.06067v1) explicitly introduces "a **min-PD within
  top-K Dice rule for checkpoint selection**" — i.e., topology-aware checkpoint selection is already being prototyped and
  published. The paper presupposes exactly A-0061's phenomenon (Dice-based selection discards topology) and ships a fix.
  It is a small single-author study on one Kaggle leaf-lesion dataset — not a scoop of A-0061's systematic multi-seed,
  multi-benchmark quantification — but it kills the "nobody has looked at selection" framing.
- **Pitfalls of topology-aware image segmentation** (arXiv 2412.14619, https://arxiv.org/html/2412.14619) audits topology
  evaluation practice (Betti number vs Betti matching errors, aggregation pitfalls) and issues reporting recommendations.
  A-0061's measurement instrument must be built on Betti-matching (not raw Betti numbers) or reviewers armed with this
  paper will discount the readout.

**Verdict correction:** A-0061 should be re-classed from bare SURVIVE to SURVIVE-WITH-MANDATORY-POSITIONING (cite
2601.06067 as proof-of-appetite, adopt 2412.14619's metric guidance). The window is still open, but it is a
this-cycle window, not a comfortable one. The supervisor's ledger currently lists A-0061 as "the only un-gated A survive" —
that line is now stale.

## Finding 3 — Supervisor bias: the eval-science cap is cosmetic, and the emerging gravity ignores the supervisor's own merge accounting

**EVIDENCE.**
- Agent D self-reported ~70% eval-science in his keeps and recommended a cap "~60% of C's contribution." The supervisor
  adopted 60% — a cap barely below the measured skew, applied **only to batch C's slots**, and met "mainly by merging
  redundant audits into hosts rather than by killing protected ideas" (G report). C's 57 slots still carry 33 eval-audit
  units, and 18 merged parasites mean C's *content* is ~75 idea-units in 57 slots — the cap compressed the accounting,
  not the science.
- Agent F self-reported **amplifying** the same skew in batch A ("metric-audit 40 [of 75 keeps], forensic 18... I amplified it").
- The supervisor's "Emerging finalist gravity" (research_summary.md) is A-0061, A-0206, B-0114, B-0001 — three
  audit/forensics papers and one mechanism paper whose current best form is itself an attribution audit. **Zero batch-C ideas
  appear in the gravity list even though C holds 32 of the 50 LOCK slots.** Either the supervisor implicitly distrusts the
  C portfolio he just ratified, or the gravity list was formed before K's attack on C and is premature. Both readings are
  bad process: the gravity list is shaping execution priorities (execution-order urgency, pilot dispatch) ahead of the
  evidence.
- The supervisor's protection policies (cheap-to-falsify, "protect cheap mechanism experiments") select one-dimensionally
  for cheap decisive measurements. H measured the consequence: "ideas whose killer experiment costs under ~2 GPU-weeks had
  roughly a 1-in-3 chance of having been executed by someone else within ~12 months." Cheapness is being priced as pure
  upside when it is also the scoop-hazard variable.

**HYPOTHESIS.** The pipeline's fitness function (falsifiable + cheap + decisive + survives adversarial review) is
structurally equivalent to "fund audits." Constructive ideas fail "decisive" (methods can lose honestly), so they die at
every stage at a higher rate than their field value warrants. If not corrected at the Top-5 lock, the final portfolio will
be an evaluation-science monoculture wearing four different costumes — see `portfolio_risk.md`.

## Finding 4 — Reviewer echo chamber is real, measurable, and one-directional

**EVIDENCE.**
- H: 29 attacks → **0 bare SURVIVE**; J: 23 attacks → 1 bare SURVIVE, **0 kills** ("Zero KILLs on a mandate to kill").
  Both converged on the same verdict shape (SURVIVE-IF-EXPERIMENT / mutation-with-named-control). Both self-reported it.
- D, E, F, H, J all celebrate the identical virtues (cheap, decisive, falsifiable, either-outcome-publishes) and use the
  same kill weapons across batches (RClicks kills B-0175 *and* A-0201; Surgical Fine-Tuning kills B-0236 *and* A-0332;
  Udandarao kills B-0037 and re-frames C-0279). Cross-batch consistency is good; but it also means one blind spot is
  replicated five times. No reviewer in the chain ever argued *for* ambition against defensibility.
- The same inferential template — "protocol/noise variance exceeds published effect sizes" — appears at least 8 times
  across surviving ideas from all three batches (C-0136, C-0302, C-0311, C-0011+B-0042, A-0198, A-0215-mut, B-0157, B-0033-arm,
  A-0071/0322). Stage-1 Agent A even flagged this himself ("'X is partly annotation noise' template overuse... a correlated
  block of ideas devalues together"). The reviewers pruned duplicates *within* the template but never priced the
  template-level common-mode risk — if one strong "noise bounds progress" umbrella paper appears (Label Convergence,
  arXiv 2409.09412, WACV 2025, is already 80% of the way there — verified live:
  https://openaccess.thecvf.com/content/WACV2025/html/Tschirschwitz_Label_Convergence_Defining_an_Upper_Performance_Bound_in_Object_Recognition_WACV_2025_paper.html),
  the entire block ages overnight.

**HYPOTHESIS.** All agents share one base model and one prompt culture. The observed "independent convergence" of D/E/F/H/J
on measurement papers is partially self-similarity, not five independent validations. Treat inter-agent agreement as ~2
effective independent opinions, not 5, when computing confidence in any verdict.

## Finding 5 — Kill-evidence spot-check: citations are real; two frame-kills are over-broad

I live-verified a sample of load-bearing kill citations. Results:

| Claimed kill evidence | Verified? | Assessment |
|---|---|---|
| HalluSegBench, arXiv 2506.21546 (kills A-0199 framing) | **REAL** — https://arxiv.org/abs/2506.21546 | Over-broad: benchmark targets **segmentation VLMs** (referring/reasoning expressions), not classical segmenters. See below. |
| HII-DPO, arXiv 2602.10425 (kills A-0199 framing) | **REAL** — https://arxiv.org/html/2602.10425v1 | Over-broad: it is a **captioning/description hallucination** (VLM, DPO alignment) paper, not segmentation. |
| On the Faithfulness of Visual Thinking, arXiv 2510.23482 (kills B-0332) | **REAL** — https://arxiv.org/abs/2510.23482 | Kill is **sound**: visual-vs-textual intervention experiment is exactly B-0332's design, executed with a training fix. Largest legitimate casualty. |
| Label Convergence, arXiv 2409.09412 (demotes C-0071) | **REAL** — WACV 2025, URL above | Demotion sound; also raises template-level risk (Finding 4). |
| VPT ablation (relevant to B-0114) | **REAL** — https://arxiv.org/abs/2203.12119 | Missed by the pipeline in the *other* direction (Finding 1). |
| Vision Transformers Need Registers / SINDER (context for B-0001) | **REAL** — https://arxiv.org/abs/2309.16588, https://arxiv.org/abs/2407.16826 | H's attack on B-0001 checks out; H's note "no paper found selling the norm map as per-pixel uncertainty" independently reproduced by my search. B-0001's window is open. |

**The A-0199 over-kill (EVIDENCE):** both scooping papers are VLM-side. A-0199's original core — classical segmentation
networks (with fully known training data) hallucinating scene-typical objects, with a **dose-response law against mined
training co-occurrence statistics** — is not what either paper does. J granted this as a "sliver"; on the verified
abstracts it is more than a sliver: it is the causal, training-data-grounded version that the VLM papers cannot run
(they don't know their models' training data). J's own cross-cutting note ("curation-based causal designs lose to
editing-based ones") supplies the fix: use inpainting/editing counterfactuals, measure hallucinated-pixel rate vs
co-occurrence strength. See `revive.md` #2.

**A-0206 (SAM fingerprint) novelty spot-check (EVIDENCE):** live search found a dense generated-**image** attribution
literature (e.g., ManiFPT-style fingerprints; model-genealogy clustering from outputs alone, arXiv 2608.15652,
https://arxiv.org/html/2608.15652v1) but **no paper on mask-space provenance/fingerprinting of SAM-assisted annotations**.
The window is open; the adjacent image-attribution toolbox is simultaneously A-0206's method shelf and its "why is this
different" review question. J's controlled-provenance-corpus gate remains the right call. Urgency is real.

## Finding 6 — Process faults the PI should fix before Stage 7

**EVIDENCE.**
1. **J worked from a stale checkout.** J's report states `PI_TO_I.md` "does not exist anywhere in the repo (verified after
   pulling latest origin)" — the file exists on this branch and predates J's commit range (it now also contains post-hoc
   H/J digests). J therefore never saw the PI's instruction to "prefer F's mutated forms" for 13 IDs. Impact appears low
   (J rebuilt targets from F's files), but the coordination channel failed silently.
2. **G overrode four D-protected ideas without the PI sign-off G itself said was required** (C-0251, C-0334, C-0253,
   C-0271: "require PI sign-off to become final"). No sign-off is recorded anywhere in the ledgers. C-0334 is a
   substantive loss (see `revive.md` #1).
3. **Cross-batch ID collisions are an accident waiting to happen.** A-0175 (printed-shape metrology, alive, pilot-gated)
   vs B-0175 (RClicks kill, dead) — the PI's own note "0175 (if still in shortlist)" is ambiguous without a batch prefix.
   The eliminated-list in `evolution_summary.md` is prefixed correctly today; one unprefixed ledger edit could revive a
   corpse or kill a survivor.
4. **The supervisor's ledger asserts verdicts ahead of evidence.** "Emerging finalist gravity" was written while I (fold)
   and K (Reviewer-2 on C) are still running; C-side candidates structurally cannot appear in it. Gravity lists published
   mid-pipeline anchor later agents (including me — I audited them first because the ledger told me to).
5. **Verification asymmetry.** ~120 of the B∪C portfolio keeps were never live-searched (G's own admission; D attacked
   19/107, E 26/77). The kill lists were re-checked harder than the keep lists. The most dangerous unverified keeps are
   the LOCKs G named: C-0122, C-0193, C-0308, B-0164, B-0286 — none has ever faced a dedicated search.

## Finding 7 — Missing research directions (what the funnel structurally could not produce)

**EVIDENCE** (from cluster maps and slot accounting): the Stage-1 territory split (A: SAM/segmentation-failure;
B: VFM/PEFT/VLM; C: detection/eval) plus the kill gradients produced a portfolio with:
- **Medical FM science: ~6 slots**, of which the flagship causal question (B-0293 matched-budget attribution) is
  compute-partner-conditional and B-0286 is a MUTATE. Batch A's medical survivors (0061, 0074, 0075, 0331) are
  MICCAI-facing metrology, not FM science. If the compute partner does not materialize, the portfolio's answer to the
  single hottest funding question in the area ("do medical FMs beat natural FMs + readouts?") is *nothing*.
- **Smoke/fire: one slot** (A-0100 leakage audit — a debunk). The constructive framing F himself wanted revived
  (A-0090 time-to-detect as the evaluation layer) is tier-2. A-0097 (shimmer) is kept but invisible in gravity.
- **SAM2/video memory science: zero visibility.** F called A-0028 (teleport test: does SAM2 track appearance or location?)
  "among the best of C02," scored it ROI 5 / feasibility 5 / cheap-falsify — and then left it out of the top-20, so it was
  never Reviewer-2 attacked and appears in no ledger. The entire video-memory cluster (25+ Stage-1 ideas) has no
  representative above tier-2 visibility. This is the pipeline's clearest orphaned-cheap-win.
- **3D/geometry: effectively zero** (B-0307 staged behind a probe; nothing else). **Embodied/robotics, streaming/online
  perception, efficiency science: zero by construction** — no Stage-1 agent owned them. The supervisor chose the
  territory split; the gap is a supervisor artifact, not an idea-quality verdict.
- **Geographic/fairness coverage was actively traded away**: G dropped C-0252 (geo-stratified test set) keeping one
  fairness artifact (C-0258), and A's own report flags the "Anglophone/web-data lens" as unhedged.

**HYPOTHESIS.** None of these gaps can be fixed by reviving individual IDs; they need either a deliberate Top-20 quota
(medical-executable, one constructive, one video) or an explicit written decision to abandon the direction. The worst
outcome is the current implicit abandonment, which will be re-discovered as a "surprising gap" at proposal-writing time.

## Finding 8 — Correlated-bet clusters that would make a Top-3 look like one paper in three costumes

See `portfolio_risk.md` for the full AC simulation. Summary of the cluster math (**EVIDENCE** for memberships, **HYPOTHESIS**
for the joint-risk estimates):
- **Register/token-artifact micro-field:** B-0114 + B-0001 share one literature, one confound family (background/norm
  entanglement), one obsolescence event (register-equipped backbones becoming universal — already flagged by H for both).
  These are one bet, not two.
- **"Hidden defect in standard practice" genre:** A-0061 (checkpoint selection), A-0206 (annotation provenance),
  B-0001 (artifact maps), plus the whole measurement cluster. A Top-3 drawn from current gravity is 3 diagnosis papers,
  0 fixes.
- **Cheapness as common-mode scoop risk:** all four gravity ideas are ≤2 GPU-weeks. Applying H's measured ~1/3-per-year
  scoop hazard independently, P(at least one of three cheap finalists scooped within 12 months) ≈ 1 − (2/3)³ ≈ 70%.
  Execution speed is not optional at these price points.
- **Shared unbuilt dependency:** six batch-A survivors need the noise/convention/quality/ambiguity annotation taxonomy
  (J's re-annotation-arbiter cluster). The supervisor's ledger acknowledges the cap; the taxonomy itself is still
  unowned — it is the hidden foundational paper, and also the single point of failure.
