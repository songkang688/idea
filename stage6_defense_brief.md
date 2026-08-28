# Stage 6 — Defense + Upside Pass on the Global Top 5

**Panel:** Domain Expert panel (Cloud Sub-Agent Q) — Foundation Model Expert (FM), Segmentation
Expert (SEG), Medical Imaging Expert (MED), Methodology Reviewer (METH) → Supervisor Windows7.
**Branch:** `cursor/stage6-defense-top5-2995`
**Inputs fetched and read in full this session:**

| Source | Branch |
|---|---|
| `stage5_cluster_A_engineering.md`, `stage5_cluster_A_top.md`, `stage5_cluster_A_roi.csv`, `stage4_cluster_A_attacks.md` | `origin/cursor/stage5-cluster-a-engineering-ed30` |
| `stage5_cluster_B_engineering.md`, `stage5_cluster_B_top.md`, `stage5_cluster_B_roi.csv` | `origin/cursor/stage5-cluster-b-engineering-a00b` |
| `stage5_cluster_C_engineering.md`, `stage5_cluster_C_top.md`, `stage5_cluster_C_roi.csv` | `origin/cursor/stage5-cluster-c-engineering-2eff` |
| `stage4_cluster_B_attacks.md` | `origin/cursor/stage4-cluster-b-reviewer2-b25a` |
| `stage4_cluster_C_attacks.md` | `origin/cursor/stage4-cluster-c-reviewer2-c1be` |

**Charter.** For each Top-5 idea: steelman it (strongest surviving claim, venue case, hidden
upside found by literature search), then state where the four experts still disagree — without
manufacturing consensus. Votes are recorded per expert, not averaged into agreement.

**Voting rule.** Each expert votes ADVANCE / BORDERLINE / DROP independently. The panel vote is
the panel's collective recommendation, which is *not* a majority function: where a single expert
holds a decisive objection the panel vote reflects it, and the dissent is recorded verbatim in
`stage6_expert_votes.csv`. Two ideas below carry live dissent against the panel vote.

**Provenance discipline.** All literature below was retrieved by web search this session
(2026-08-28). Retrieval returned titles, abstracts, and substantial body text; it did not include
full replication of every reported number. Claims are labelled `[verified-abstract]` where the
statement comes from an abstract or body excerpt read this session, and `[inherited]` where it
carries from Stage-3/4/5 documents. No result below is presented as measured by us. Several cited
preprints are recent and unrefereed; where a citation is load-bearing for a vote, that is flagged.

---

## 0. Cross-cutting findings from the literature pass

Five findings from this session's searches cut across multiple ideas and drive several of the vote
changes below. They are stated once here and referenced by section.

**(X1) SAM3 shipped, and it changed the memory policy.** `arXiv:2512.22624` (*Rethinking Memory
Design in SAM-Based Visual Object Tracking*) states that SAM3 "employs stronger visual
representations and a more conservative memory update strategy, retaining only frames where the
target object is confidently present," and concludes that "progress in SAM-based tracking is
increasingly bottlenecked by memory design rather than backbone capacity alone." It reimplements
SAM2-era memory policies under SAM3 across ten benchmarks and releases code
(`github.com/HamadYA/SAM3_Tracking_Zoo`). [verified-abstract, unrefereed preprint]
→ Reshapes **A-0017** (§1): large upside, real framing-encroachment risk.

**(X2) FSS evaluation has an independent, unrelated validity failure.** `arXiv:2606.09474`
(Open-V, training-free generalized FSS built on SAM3 Promptable Concept Segmentation + CLIP)
reports identifying "a reproducibility confound in foundation-model segmentation, demonstrating
that preprocessing and evaluation-space mismatches can silently distort reported performance,"
with a correction improving PASCAL-5i by more than 37 points; and reports 78.4/77.5/77.9
base/novel/harmonic mIoU on PASCAL-5i 1-shot, "+17.7 HM" over the strongest trained baseline,
with no GFSS-specific training. [verified-abstract, unrefereed preprint]
→ Reshapes **B-0121** (§2): a second free headline, and a significance-decay threat.

**(X3) The segmentation training objective is itself low-frequency-dominated.**
`arXiv:2012.14123` (*Spectral Analysis for Semantic Segmentation*) reports that cross-entropy
decomposes into frequency components dominated by the low-frequency content of segmentation maps,
that the IoU score is closely related to CE in that decomposition, and that Boundary-IoU is
*also* mainly contributed by low-frequency components. [verified-abstract]
→ Supplies **A-0061** (§3) with a loss-side mechanism for the training-limited world, upgrading it
from a datasheet to a mechanism paper.

**(X4) The field's synthetic-data hygiene metrics are documented as broken, and appetite for a
replacement is high.** `arXiv:2606.25128` reports that FID "does not reliably track downstream
utility" and that human realism ratings do not either (BELDE-K rated 3.42 realism → 58.3 F1;
BELDE-CA-NV rated 3.09 → 66.2 F1). `arXiv:2605.22467` (SADGE) states that to its knowledge "there
exists no studies that evaluate which similarity metric is the best downstream predictor," and
reports Pearson r = 0.879 / Spearman ρ = 0.768 across 15 dataset-level variants for a fused
appearance+geometry metric — dataset-level, correlational, content-varying. [verified-abstract]
→ Both strengthens and scope-limits **B-0212** (§4).

**(X5) MLLM forgetting is now openly contested, with the content side gaining ground.**
`arXiv:2603.14493` (*Fine-tuning MLLMs Without Forgetting Is Easier Than You Think*) argues the
"perceived threat of catastrophic forgetting has been overstated," attributes the residual failure
to task-specific overfitting on in-distribution-image/out-of-distribution-text settings, and fixes
it with data-hybrid mixing — reporting that "the effect is not just 'more data,' but specifically
task diversity mitigating overfitting." Separately, modality gradient conflict is now formally
defined (`arXiv:2512.03125`, Definition 1) and measured (`arXiv:2606.17296` Pareto LoRA:
"modality-specific gradients can differ by orders of magnitude across various tasks and layers").
[verified-abstract, two unrefereed preprints]
→ Both the strongest upside and the strongest threat to **C-0090** (§5).

---

## 1. A-0017 — SAM2 causal memory surgery
**Origin:** `origin/cursor/stage5-cluster-a-engineering-ed30` · Stage-5 ROI 9.0 · ≈80–120 GPU-h · zero training

### Strongest scientific remaining claim

Not "resetting the tracker helps." The claim that survives Stage-4/5 attrition is narrower and
harder:

> The reversible fraction of *organic* long-video tracking failure under oracle-timed targeted
> deletion of post-error memory entries is a **validated decomposition instrument**. Validation is
> external and preregistered: the per-sequence reversible fraction predicts the per-sequence J&F
> gains of independent, training-free prevention methods. Targeted deletion must additionally beat
> full reset by ≥10 points, which is what establishes that pre-error memories are load-bearing and
> that the operation is a decomposition rather than a restart.

The load-bearing novelty has narrowed since Stage 4. P1 (deletion recovers a lot) is now close to
consensus in the literature — at least six papers assert that FIFO/confidence-driven memory writes
cause error accumulation (SAMURAI, SAM2Long, DAM4SAM, SAMITE, HiM2SAM, SENTRY, per
`arXiv:2512.22624` and `arXiv:2606.24449`). The paper now rests on **P2 (targeted > reset)** and
**P3 (predictive validity)**. The panel considers this a *sharpening*, not a weakening: P2 and P3
are the two legs nobody else has run.

### Why a top venue might accept

The subfield has produced roughly eight competing memory policies in two years with no common
yardstick for how much headroom any of them captures. `arXiv:2512.22624` says the field is
"bottlenecked by memory design"; `arXiv:2507.08548` (SAM2RL) demonstrates by RL-overfitting a
per-video memory policy that hand-crafted rules leave substantial performance on the table
(reported +4.91% tracking quality over SAM2, beating SAMURAI and DAM4SAM in their setup) and then
observes that even the overfit policy "still fails to achieve optimal performance, suggesting the
limit of the memory bank capacity." That is a field asking, in print, for exactly the
decomposition A-0017 produces: how much of the remaining gap is memory-borne and how much is
representational. A headroom table with an external validity test is the natural reference
artifact for that question.

### Hidden upside (found this session)

1. **A second, independent, non-oracle ceiling is already public.** SAM2RL's per-video optimized
   memory policy is an upper bound obtained by optimization rather than by oracle timing. Running
   A-0017's surgery on the same sequences lets the two ceilings be cross-validated. Two
   independently derived ceilings that agree would neutralize the oracle-dependence attack far
   more convincingly than the framing argument Stage 4 used, and the marginal cost is one public
   repo and a shared sequence list.
2. **A generational headroom law instead of a SAM2 post-mortem.** Because SAM3's memory policy is
   explicitly more conservative (X1), running the identical protocol on SAM2.1 and SAM3 converts
   the deliverable from "SAM2 has this much memory-borne failure" into "here is how much
   memory-borne failure a model-generation change actually removed, and how much it did not." That
   is a materially larger paper, and `arXiv:2512.22624` has released the SAM3 tracking zoo that
   makes the comparator ports cheap.
3. **The predictive-validity leg gains statistical power for free.** Stage 5 designed P3 around two
   comparators (SAMURAI, DAM4SAM). The training-free comparator pool is now at least six —
   SAM2Long, SAMITE, HiM2SAM, SENTRY (`arXiv:2606.24449`), AS-SAM2 (TCSVT 2026, code promised).
   With five or six independent methods, "reversible fraction predicts prevention gains" stops
   being an anecdote about two wrappers and becomes a claim about the mechanism class.

### Remaining expert disagreements

1. **FM vs SEG — is a SAM2.1-only paper viable?** FM holds that the SAM3 arm must be *core*, not an
   extension: with SAM3 public and the memory-transfer zoo released, a SAM2.1-only diagnostic
   reads retrospective by submission. SEG holds that adding SAM3 doubles the harvest cost and
   risks the paper becoming a two-model survey instead of one decisive decomposition, and that the
   protocol's value is method-independent. Unresolved.
2. **MED dissents on scope.** Every dataset in the design (LVOS v2, DiDi, optional SA-V) is natural
   video. Medical video — echocardiography, endoscopy, surgical tool tracking — is where SAM2
   memory failure is clinically load-bearing, and none of it appears. MED's position is that this
   is a VOT paper in a portfolio that has declared a medical-imaging axis, and that a single
   medical-video arm would change its portfolio value more than any additional natural-video
   stratum. Not resolved by the panel; recorded as a design condition, not a kill.
3. **METH on the P3 threshold.** The correlation is over sequences, so n is adequate, but with five
   or six comparators the design as written ("SAMURAI *and* DAM4SAM at r > 0.6") permits post-hoc
   selection of which comparator carries the headline. METH requires the preregistration to fix a
   *combined* statistic — e.g. the minimum r across a named comparator set must exceed the
   threshold — before any comparator is run. FM considers this over-tight given comparator quality
   varies. Unresolved.
4. **METH on the word "upper bound."** The ceiling is oracle-conditioned and must be labelled
   "oracle-timed ceiling" throughout, with the t_r ± δ dose-response promoted from ablation to main
   result so readers can see how the ceiling degrades as the oracle weakens. SEG agrees; FM thinks
   this is presentational. Effectively resolved in METH's favour.
5. **Framing encroachment, not scooping.** All four experts agree `arXiv:2512.22624` has not run
   oracle surgery or a reversibility decomposition. FM and METH disagree about how much that
   matters: FM says the "systematic memory-centric study" real estate is now occupied and the pitch
   must be decomposition-first; METH says the distinction is clean enough to survive review on the
   preregistered legs alone.

### Vote

FM **ADVANCE** · SEG **ADVANCE** · MED **BORDERLINE** · METH **ADVANCE**
**Panel: ADVANCE to Final 3.** Highest-value idea in the slate; the literature moved in its
favour on upside more than against it on novelty.

---

## 2. B-0121 — Wrong-support counterfactual FSS audit
**Origin:** `origin/cursor/stage5-cluster-b-engineering-a00b` · Stage-5 ROI 9 · ≈5 A100-days · zero training

### Strongest scientific remaining claim

> The support-independent share of reported few-shot segmentation accuracy, measured per method ×
> per benchmark × per query-complexity stratum against a support-free objectness floor, with the
> distractor-present stratum preregistered as primary. The headline quantity is **retention**
> (IoU_wrong / IoU_correct) — a within-method ratio, and therefore robust to the absolute-number
> irreproducibility that X2 shows is endemic in this literature.

That last property is worth more than Stage 5 realised. The audit's primary statistic does not
depend on reproducing anyone's published number.

### Why a top venue might accept

No counterfactual audit of this kind exists; the mitigation literature (TBS AAAI 2024, AENet ECCV
2024, CVPR 2024 iterative modulation [inherited]; support-dilution work at `arXiv:2501.13529`;
SADe at `arXiv:2607.24706` [verified-abstract]) exists *because* everyone believes support quality
matters, yet nobody has measured how much accuracy survives its total destruction. Add X2: an
unrelated group has just shown that FSS numbers can be silently distorted by 37 points through
preprocessing-space mismatch. A paper that re-runs the whole method panel through one pinned
harness and reports a support-sensitivity score plus a distractor-enriched split is the natural
response, and the artifact outlives whichever model generation is current.

### Hidden upside (found this session)

1. **A second headline at zero marginal cost.** B-0121 must re-run every checkpoint anyway. Doing
   so under both a single shared evaluator and each repo's native evaluator — already listed in
   the design's robustness section — turns X2's preprocessing confound into a reported per-method
   discrepancy table. Two independent validity failures in one paper is a substantially stronger
   submission than either alone.
2. **Partial independent corroboration of the mechanism.** Open-V reports that support
   contribution "increases as foundation-model text priors weaken on label-disjoint vocabularies"
   (X2). Read the other way: when the prior is strong, the support contributes little. That is
   B-0121's hypothesis, observed from the opposite direction by an unrelated group. Cite as
   scaffold; it makes the premise non-speculative.
3. **A far stronger support-free floor is now available.** The design's floor is SAM automatic mask
   generation, largest/most-central mask. SAM3 Promptable Concept Segmentation, and the frozen
   DINOv3-feature one-shot matcher noted as a CVPR 2026 oral in the in-context-segmentation
   survey, are much harder floors. If a modern training-free floor already matches specialist FSS
   methods on the distractor stratum, killer-leg (b) becomes damning without any wrong-support
   argument at all — the audit gets a second, independent route to its conclusion.

### Quiet killers

- **Significance decay is now the leading threat and it worsened since Stage 4.** The specialist
  leaderboard B-0121 proposes to reorder (PFENet / HSNet / BAM) is being obsoleted in public: X2
  reports +17.7 HM over the strongest *trained* baseline from a training-free pipeline. A reviewer
  can reasonably ask why anyone needs a sensitivity-adjusted ranking of methods that will not be
  competitive at publication time.
- **The panel's answer requires a design change, not a rebuttal.** The method panel must be
  re-centred so that training-free foundation matchers (Matcher, PerSAM, SegGPT, FSSAM, SAM3-PCS,
  a DINOv3 matcher) are *primary* and the specialist meta-learners are the historical arm. This
  shifts the expected answer: those methods are explicitly support-driven, so retention may be
  low, pushing the paper toward the certification branch — the honest but least headline-dense
  outcome. The panel accepts this as a genuine reduction in expected upside, not a formality.
- **The benchmark-degeneracy attack partially survives.** FSS-1000 is degenerate by construction
  and PASCAL-5i is predominantly single-object; the COCO-20i / LVIS-92i distractor strata are the
  only real test, and stratifying shrinks the effective episode count where the claim lives.

### Remaining expert disagreements

1. **FM vs SEG on subject-matter decay.** FM: as designed, this audits a subfield being replaced,
   and only the re-centred panel makes it current. SEG: retention is a mechanism measurement that
   applies to any support-conditioned model including SAM3-PCS, so the audit is generation-proof —
   the specialist arm is history, not the point. Unresolved; both accept the re-centring, they
   disagree on whether it was already implied.
2. **Is the certification branch top-venue publishable?** METH: yes — the first counterfactual
   audit of a field's core claim is a contribution whichever way it lands, and the fixed
   distractor split is a standing artifact. FM: a null audit of an obsolescing subfield is a
   workshop paper. Directly unresolved, and it is the single biggest disagreement about this idea.
3. **MED wants the medical arm promoted.** One-shot organ segmentation from a single annotated
   reference is a real clinical workflow; MED holds that the abdominal-CT probe currently filed
   under "generalization" carries more weight than another COCO stratum and should be a core arm.
   SEG resists on scope-creep grounds. Unresolved.
4. **METH on evaluator plurality.** The dual-evaluator protocol must move from robustness to
   primary given X2. No expert dissents; recorded as a mandatory design delta.

### Vote

FM **BORDERLINE** (→ADVANCE conditional on re-centring the panel) · SEG **ADVANCE** ·
MED **BORDERLINE** · METH **ADVANCE**
**Panel: ADVANCE to Final 3, conditional on the method-panel re-centring.** The condition is not
cosmetic: without it the panel's own FM expert would not advance it.

---

## 3. A-0061 — Boundary Nyquist cutoff-ratio
**Origin:** `origin/cursor/stage5-cluster-a-engineering-ed30` · Stage-5 ROI 8.5 · ≈10–20 GPU-h · zero training

### Strongest scientific remaining claim

> The **cutoff-to-oracle ratio table**: for ≥4 decoder architectures at ≥3 output resolutions,
> the empirical contour-frequency error cutoff divided by the cutoff of an oracle reference
> obtained by passing ground-truth masks through each decoder's own output grid with no model in
> the loop. Ratio ≈ 1 everywhere ⇒ sampling-limited, and decoder resolution is a real design dial.
> Ratio ≪ 1 ⇒ training-limited, and resolution increases alone are wasted. Measured against
> synthetic parametric contours with exact analytic ground truth, so the annotation-bandwidth
> attack is dead by construction.

### Why a top venue might accept

Cheapest decisive experiment in the entire portfolio (10–20 GPU-h, no training, no annotation);
both outcomes redirect engineering budgets that are currently being spent on faith; and the
frequency-aliasing literature that exists is all *encoder-side*. `arXiv:2403.09065` (*When
Semantic Segmentation Meets Frequency Aliasing*) and the AAAI 2026 Gaussian/Gabor follow-up
(`10.1609/aaai.v40i9.37713`) analyse aliasing introduced by *feature-map downsampling* in
semantic-segmentation CNNs and propose de-aliasing filters; neither measures the *output-side
contour bandwidth of a promptable mask decoder* against its own sampling bound. The vacuum is
specific and real.

### Hidden upside (found this session — the largest single upside in the slate)

1. **X3 supplies a loss-side mechanism for the training-limited hypothesis.** If cross-entropy,
   IoU, *and* Boundary-IoU are all dominated by the low-frequency content of segmentation maps
   (`arXiv:2012.14123`), then a decoder trained under those objectives has almost no gradient
   pressure to resolve high contour frequencies — which predicts the cutoff should sit *below* the
   sampling bound. A-0061 can therefore graduate from "we measured an operating point" to "we
   measured an operating point and it matches the frequency content of the objective that produced
   it," and can test the prediction directly by comparing cutoffs across models trained with
   boundary-weighted versus standard losses. That is a mechanism paper, and it is a substantially
   higher ceiling than Stage 5 assigned.
2. **Precedent that frequency-domain measurement converts into gains.** `arXiv:2403.09065` reports
   that replacing an empirically-set low-pass cutoff with an analytically derived equivalent
   Nyquist frequency improved UPerNet-R50 from 78.1 to 79.3 mIoU (79.7 with FreqMix), beating
   AdaBlur at 78.9. Reviewers have seen this class of argument pay off, which lowers the burden on
   A-0061's "so what."
3. **The oracle grid-resampling baseline is a reusable instrument.** It is pure numpy, model-free,
   and applicable to any dense predictor. Its citation surface extends past whichever verdict the
   paper reaches.

### Quiet killers

- **HQ-SAM's own published delta points against the expected headline.** `arXiv:2306.01567` reports
  DIS mBIoU improving 52.8 → 70.4 with the HQ output token and high-resolution feature path
  [verified-abstract]. A 17.6-point boundary jump from a resolution/feature intervention is prima
  facie evidence that the output-side feature path *is* binding — i.e. evidence for the
  sampling-limited world and against the "resolution is wasted" headline the Stage-5 file expects.
  The design already carries "HQ sharpens below the cutoff" as the alternative reading, so this is
  not fatal; but the panel records that the *expected direction is in tension with published
  numbers from the paper's own test case*, and Stage 5 did not note this.
- **Adjacency density.** A reviewer fluent in the aliasing literature will ask what is new beyond
  "Nyquist applies to masks." The four-part answer (output-side not feature-side; promptable
  decoders; ratio against a model-free oracle; the training-vs-sampling dichotomy) is defensible
  but must be in the abstract, not the discussion.
- **If the empirical cutoff simply equals the analytically predicted Nyquist**, the operating-point
  finding collapses back toward Stage-4 attack #1 ("the theorem needs no experiment") — now
  empirically rather than rhetorically.
- **Knee identifiability (P1) is a live measurement risk**; the roll-off-slope fallback is a
  weaker headline than the design implies.

### Remaining expert disagreements

1. **SEG vs FM on durability vs currency.** SEG argues this is the most durable idea in the slate:
   architecture-indexed measurements do not rot when the next checkpoint ships, and the stimulus
   suite is a lasting artifact. FM argues the decoders in the table (SAM, HQ-SAM, SAM2,
   Mask2Former) are the 2023–2024 generation, that SAM3-class concept decoders are where the field
   is, and that boundary quality is increasingly being bought with fine-mask training data — which
   would make "training-limited" a foregone conclusion rather than a finding. Unresolved.
2. **MED is the strongest advocate, and wants a medical arm.** Boundary/thin-structure bandwidth is
   the binding constraint in vessel, airway and lesion-margin segmentation; the synthetic contour
   suite ports directly and the verdict would transfer to medical decoder design immediately. MED
   wants one medical arm (DIS-style fine masks → a vessel or lesion-margin set) in the core, not
   as generalization. SEG agrees it is cheap; FM is neutral.
3. **METH on analyst degrees of freedom.** The softest spot is not the models, it is the contour
   parametrization: arc-length versus image-plane frequency, and the choice of pre- versus
   post-upsampling extraction stage. METH requires the frequency convention frozen in
   preregistration with *both* conventions reported, and objects that "knee via segmented
   regression R² ≥ 0.8" is a fit-quality gate masquerading as an effect size. SEG accepts; no
   dissent.
4. **Whether the HQ-SAM tension is a strength or a warning.** METH: it is a strength — the design
   has a preregistered alternative reading, so the experiment is genuinely two-sided. FM: it is a
   warning — if the likely answer is "sampling-limited," the paper's headline becomes "HQ-SAM was
   right," which is a validation rather than a redirect. Unresolved.

### Vote

FM **BORDERLINE** · SEG **ADVANCE** · MED **ADVANCE** · METH **ADVANCE**
**Panel: ADVANCE to Final 3.** Best upside-per-GPU-hour in the slate, and X3 raised its ceiling
more than any other single finding this session.

---

## 4. B-0212 — Blending-artifact → transfer-gap law
**Origin:** `origin/cursor/stage5-cluster-b-engineering-a00b` · Stage-5 ROI 8 · ≈40–45 A100-days · ~30 training runs

### Strongest scientific remaining claim

> At **fixed generator and fixed content**, compositing-artifact detectability (probe AUROC on
> boundary patches) orders the real-set DSC of segmenters trained on the composites; and
> re-injecting the measured seam residual into the best-blended arm reopens ≥50% of the ladder's
> real-DSC spread. The forward leg establishes the ordering; the reverse leg establishes that the
> artifact is *used*, not merely present.

The fixed-content construction is the asset. Everything adjacent in the literature is
content-varying and correlational.

### Why a top venue might accept

It is the only design in the slate that answers both of its Stage-4 attacks structurally rather
than argumentatively: the generator-quality confound is removed by holding content and generator
fixed across rungs, and "detectable ≠ used" is answered by a reverse intervention. The stack is
entirely public (SyntheticTumors, DiffTumor, libcom). The deliverable — report your synthesis
pipeline's probe AUROC — is adoptable the week the paper appears.

### Hidden upside (found this session)

1. **X4 establishes strong, current venue appetite for exactly this question, and a head-to-head
   table is nearly free.** SADGE explicitly claims no prior work evaluates which similarity metric
   best predicts downstream utility, and the EO benchmarking paper shows FID and human realism
   both fail to track utility. B-0212 can add a cheap arm scoring FID, DINO/DINOv3 similarity, and
   a SADGE-style fused metric on the *same* fixed-content ladder. If a cheap boundary-artifact
   probe outperforms generic distributional metrics in the regime where compositing is the only
   free variable, that is a very attractive table and it costs inference only.
2. **The 2026 fix wave is uncontrolled partial evidence that the law exists.** SRA-Seg
   (`arXiv:2602.02944`) adopts "soft edge blending to create smooth anatomical transitions ...
   eliminating the hard boundaries from traditional copy-paste augmentation" and reports downstream
   gains; the *Texture-Shape Dilemma* paper (`arXiv:2603.00985`) formally names "boundary aliasing,"
   builds a gradient-shielded boundary buffer, and reports that naive high-frequency texture
   injection collapses pretraining performance from 56% to 40% and downstream from 83% to 80%
   [verified-abstract]. Practitioners are already paying a design cost for this belief with no
   measured dose-response anywhere. B-0212 prices what those fixes buy.
3. **The injection leg has independent precedent.** The 56%→40% collapse above is an
   artifact-injection result in all but name, which makes B-0212's reverse leg a credible
   manipulation rather than a speculative one.

### Quiet killers

- **The same fix wave that demoted B-0222 applies here.** By publication, soft/harmonized blending
  may be default practice, which makes the hard-cut-paste rung a straw arm and shifts the headline
  from "blending matters" to "here is the dose-response and the hygiene number." That is a real
  demotion of the pitch, even though the ladder retains its value.
- **SADGE's central finding caps the hygiene-metric claim.** If neither appearance nor geometry
  alone predicts transfer and only their nonlinear interplay does, a single-axis boundary probe
  should be expected to generalize poorly *outside* the fixed-content regime. The law is then valid
  "when compositing is the only variable" — scientifically clean, but a narrower deliverable than
  "report your pipeline's probe AUROC."
- **A control the design is missing.** The seam residual and the label-mask edge are geometrically
  coincident. The design has no arm that perturbs the *label* boundary while leaving the image
  fixed. Without it, "the segmenter keys on the seam" is not fully separated from "the segmenter
  keys on a label-boundary regularity that co-varies with the seam." The panel regards this as a
  genuine gap, not a quibble.
- **Cost.** At ~960–1,080 GPU-h it is roughly 50× A-0061, 8× A-0017, and 8× B-0121, with ~30
  training runs. Only C-0090 is more expensive.

### Remaining expert disagreements

1. **MED vs FM, and this is the sharpest split in the slate.** MED: this is the highest-value
   medical contribution in the portfolio — synthetic-lesion pipelines are proliferating in
   radiology, no one reports a hygiene number, the anchoring datasets are standard, and the result
   transfers to any organ. FM: it is a domain-specific measurement paper whose mechanism is a
   special case of documented shortcut learning, landing in a crowded and fast-moving lane at
   20–50× the compute of A-0061. FM is DROP-leaning. Not resolved.
2. **SEG's missing-control objection.** SEG will not vote ADVANCE without the label-jitter arm
   (perturb mask boundary, hold image fixed). MED considers the arm cheap and agrees to add it;
   SEG's vote remains BORDERLINE until it exists in the design.
3. **METH on the word "law."** METH rates this structurally the best causal design of the five —
   fixed content by construction, forward and reverse interventions, preregistered ρ threshold,
   a sanity gate before spend, a cheap null branch. But ρ ≤ −0.8 over 5 arms × 3 seeds = 15 points
   is thin for a "law"; METH requires the ladder's *slope with confidence intervals* as the primary
   statistic and the word "law" struck from the title. No dissent.
4. **Whether the hygiene number survives its own scope limit.** MED: a probe valid at fixed content
   is exactly what a pipeline-hygiene check needs, because a pipeline *is* fixed content. FM: a
   metric that only works when you already control the generator is not a hygiene metric, it is an
   ablation. Unresolved and consequential — it is the difference between an adopted artifact and a
   measurement.

### Vote

FM **BORDERLINE** (DROP-leaning) · SEG **BORDERLINE** · MED **ADVANCE** · METH **ADVANCE**
**Panel: BORDERLINE — designated runner-up.** Best causal architecture in the slate; loses the
third slot on cost-per-decision and on the fix-wave/scope-limit erosion of its most adoptable
deliverable. First promotion if any Final-3 idea dies at its gate.

---

## 5. C-0090 — Text rehearsal = gradient rebalancing
**Origin:** `origin/cursor/stage5-cluster-c-engineering-2eff` · Stage-5 ROI (rank 1 in C) · ≈2,450 A100-h · 15+ full fine-tunes

### Strongest scientific remaining claim

> The **content-free rehearsal grid**. At fixed token budget and under two preregistered
> gradient-matching conventions, how much of curated rehearsal's capability-stratified retention
> benefit survives when content is progressively destroyed: curated → random web → token-shuffled
> → a single repeated document. The A3 (shuffled) and A4 (single-doc) arms are the real
> contribution: they dissect diversity from lexical statistics from syntax, which no adjacent paper
> does.

### Why a top venue might accept

It is a direct, controlled, cheap-per-run intervention on a question the field is currently arguing
about in print, and all three outcome branches change a training recipe.

### Hidden upside (found this session)

1. **The idea is now the decisive experiment for a *named, live* disagreement — much stronger than
   testing folklore.** X5: `arXiv:2603.14493` argues forgetting is overstated and that the operative
   variable is *task diversity*, explicitly not volume — an observational, content-side claim with
   no content-free control and no gradient matching. C-0090's A2/A3/A4 arms are precisely the
   controls that claim lacks. Being the arbiter of a stated dispute is a considerably better pitch
   than the Stage-5 framing.
2. **The mechanism now has a formal vocabulary and independent measurements.** Modality gradient
   conflict is defined formally (`arXiv:2512.03125`, Def. 1) and Pareto LoRA reports
   modality-specific gradients differing "by orders of magnitude across various tasks and layers"
   (`arXiv:2606.17296`). This does two things: it gives a positive result a ready theoretical frame,
   and it tells us which of C-0090's two matching conventions is defensible — given documented
   per-layer disparity, **per-layer matching should be the preregistered primary** and global-norm
   the secondary. Stage 5 left them symmetric.
3. **A positive result has an unusually crisp deployable consequence:** replace curated rehearsal
   corpora with a degenerate text stream or a direct gradient-balance term, and delete a recurring
   data-curation cost line.

### Quiet killers

- **Power is the top risk and X5 made it worse.** If forgetting is largely avoidable through
  regularization and low learning rates, the A1−A0 gap (curated rehearsal minus none) in a
  well-tuned LLaVA-1.5 recipe may be small. C-0090's own abort gate — seed-σ exceeding half the
  A1−A0 gap — is exactly the failure mode the new literature predicts. This is the single most
  likely way the program ends, and it ends after roughly 1,000 A100-h.
- **The mushy middle is now the *predicted* outcome rather than a risk.** If diversity specifically
  matters (X5), then A4 < A2 < A1 and content effects exist. C-0090 then lands on the
  stratified-recipe branch, which the Stage-5 design honestly labels but which is its weakest
  headline.
- **Cost.** 2,450 A100-h is the largest in the slate: ~2.5× B-0212, ~20× A-0017, ~150× A-0061. On
  cost-per-decision it is the worst of the five by a wide margin.
- **Base-model currency.** LLaVA-1.5-7B is an old base for 2026. A reviewer will ask whether the
  result holds for a current MLLM, and the honest answer is unknown and unaffordable here.
- **Adjacency crowding.** Representation mixing (`2026.findings-acl.1210`), Locate-then-Merge
  (EMNLP Findings 2025), LLaVA-MoLE, MoDE, Pareto LoRA, BALGRAD, and the CoLLAs continual-learning
  study (PMLR v330 / `arXiv:2410.19925`) all claim part of the "why multimodal forgetting happens"
  question. None runs the content-free grid; but the lane is saturated with mechanism claimants.

### Remaining expert disagreements

1. **FM is the sole advocate, and holds the strongest portfolio argument against dropping it.** FM:
   this is the only Top-5 idea whose subject is a frontier model class, the only one whose result
   changes what large labs do, and the only *training*-mechanism study in the slate. Dropping it
   leaves a Final 3 composed entirely of inference-only diagnostics. FM votes ADVANCE and dissents
   from the panel vote.
2. **METH's two structural objections.** (a) The decision rule — balance-effect ≥ 80% of
   [Ret(A1) − Ret(A0)] — is a ratio of differences and is unstable when the denominator is small,
   which X5 predicts it will be. METH requires a preregistered *minimum detectable* A1−A0 gap,
   evaluated before the 15 arms rather than after the first 6, and the ratio uninterpreted below
   it. (b) "If conclusions diverge across conventions, the divergence *is* the finding" is
   unfalsifiable-adjacent: every outcome becomes a result. METH requires a single preregistered
   primary convention (per-layer, per upside item 2). FM considers (b) an over-reading of an honest
   contingency plan. Unresolved.
3. **SEG on topical fit.** The portfolio is a segmentation and medical-imaging portfolio; C-0090 is
   a language-retention study on a VLM whose vision-language evaluation is a sanity check, not a
   contribution. SEG treats its presence as a diversification decision rather than a scientific
   one, and votes BORDERLINE-to-DROP.
4. **MED votes DROP outright.** No medical content, no transferable medical decision, and at 2,450
   A100-h it consumes more compute than A-0017 + A-0061 + B-0121 combined (~210–260 GPU-h) for a
   payoff outside the portfolio's declared domain.

### Vote

FM **ADVANCE** (dissenting) · SEG **BORDERLINE** (DROP-leaning) · MED **DROP** · METH **BORDERLINE**
**Panel: DROP from the Final 3** — with FM's dissent recorded, not resolved.

### Alternate promoted in its place

**M5 / B-0362 — decision-flip-rate audit of published SOTA deltas**, gated on the zero-GPU desk
survey (≥15 auditable published pairs) *before* it occupies a slot.

Reasons:

1. **Its non-vacuity evidence strengthened materially this session, and it is now the best-evidenced
   premise among the alternates.** The 2026 systematic review of AI for RECIST-based response
   assessment (`Cancers 18(5):808`) finds the evidence base "sparse" — four eligible studies — and
   reports a pipeline at DSC 0.85 achieving decision classification accuracy of 0.74, *below* an
   attending radiologist's 0.77, with only moderate agreement to the manual reference (κ = 0.60);
   nnU-Net RECIST measurement agreement is reported at κ 0.67–0.81. The iRECIST feasibility study
   (`EJR 2026, 10.1016/j.ejrad.2026.113057`) reports interobserver agreement moving from κ = 0.34
   to κ = 0.67 with AI assistance. [verified-abstract] A high-Dice model landing at moderate
   decision agreement is the exact dissociation M5 is built to quantify, and it is now documented
   from two independent directions.
2. **Cost discipline.** Inference-only, ~8–10 A100-days, versus C-0090's ~102 A100-day-equivalents.
   The desk survey that gates it costs zero GPU.
3. **It restores the medical-decision axis that C-0090 does not serve**, and its calibration curve
   (ΔDSC → expected decision flips) is a standing deliverable in both outcome branches.

**Honest cost of this substitution, recorded rather than smoothed over:** M5 is an
evaluation-validity paper, and the Supervisor's stated preference ranks train/evaluate-changing
work above audits. Promoting M5 makes the slate three inference-only diagnostics plus one audit.
The panel's position is that C-0090's *expected* outcome (small denominator, stratified middle)
does not deliver a training-recipe change either, at ~250× M5's GPU cost — but FM's objection that
this trades a possible mechanism result for a certain audit result is legitimate and is not
resolved here.

**Fallback if the desk survey fails (<15 auditable pairs):** promote **A-0178** (artifact tokens →
prompt-localized failures). Its existential gate costs ~1 GPU-hour, and this session's search
confirms the instrument is real and unused in this setting: test-time registers is NeurIPS 2025
(`arXiv:2506.08010`), has been extended to VLMs, and `arXiv:2605.05206` reports the outlier
phenomenon is "substantially more severe" in SigLIP2 with no trained registers available — while
nobody has audited SAM or SAM2's Hiera. That same paper also reports that "simply masking
high-norm tokens does not improve performance," which sharpens A-0178's mechanism story (the
problem is corrupted local patch semantics, not extreme values) and makes the register-toggle the
right instrument rather than an arbitrary one.

---

## 6. Alternates — brief assessment

| ID | Panel read | Promotion priority |
|---|---|---|
| **M5 / B-0362** | Premise evidence strengthened most this session (Cancers 18(5):808; EJR 2026). Inference-only. Gated on a zero-GPU desk survey. | **1st — promoted** (gate first) |
| **A-0178** | 1-GPU-hour existential gate; instrument confirmed live and unapplied to SAM-family (`2506.08010`, `2605.05206`). Gate-empty outcome is a publishable scope note. | **2nd — fallback** |
| **C-0302** | Cheap (~600 GPU-h), genuinely open dissociation; DFR's own critics already show it "remains susceptible to spurious correlations" in medical data (`arXiv:2308.00473`), which strengthens the premise. Narrow subcommunity. | 3rd |
| **A-0002** | Cleanest causal design of the A cluster and ~30 GPU-h for the killer battery, but Stage 5's own significance ceiling assessment stands and nothing this session raised it. | 4th |
| **C-0028** | Largest practice-change surface if it lands, but 5,300 A100-h — *more* than C-0090. Promoting it as a cost-motivated replacement would be incoherent. JEST (`arXiv:2406.17711`) still owns the batch-composition lever; the dense measurement remains unclaimed. | 5th — not viable this cycle on cost |

---

## 7. Recommended Final 3 + runner-up

**Final 3**

| Rank | ID | Program | Compute | Training runs |
|---|---|---|---|---|
| 1 | **A-0017** | SAM2 (+SAM3) causal memory surgery, validated decomposition instrument | ≈80–120 GPU-h | 0 |
| 2 | **B-0121** | Wrong-support counterfactual FSS audit, panel re-centred on foundation matchers | ≈120 GPU-h | 0 |
| 3 | **A-0061** | Boundary Nyquist cutoff-to-oracle ratio table | ≈10–20 GPU-h | 0 |

**Total: ≈210–260 GPU-h, zero training runs, zero annotation budget.** For comparison, the dropped
C-0090 alone is ≈2,450 A100-h.

**Runner-up: B-0212** (blending-artifact → transfer-gap ladder, ≈960–1,080 GPU-h). First promotion
if any Final-3 idea fails its gate. Requires the label-jitter control arm added before execution.

**Mandatory design deltas before execution**

- **A-0017:** SAM3 arm in the core design, not an extension (X1); comparator set expanded to ≥4
  training-free methods with a preregistered *combined* validity statistic; "oracle-timed ceiling"
  language throughout; t_r ± δ dose-response promoted to a main result; SAM2RL cross-ceiling
  comparison added.
- **B-0121:** method panel re-centred so training-free foundation matchers (incl. a SAM3-PCS floor)
  are primary and specialists are the historical arm; dual-evaluator protocol (shared + per-repo)
  promoted from robustness to primary, per X2.
- **A-0061:** contour-frequency convention frozen in preregistration with both arc-length and
  image-plane conventions reported; the X3 loss-frequency prediction added as an explicit
  hypothesis with a boundary-weighted-loss comparison arm; one medical fine-structure arm added.
- **B-0212** (if promoted): label-jitter control arm; head-to-head against FID / DINOv3-similarity /
  SADGE-style fused metrics on the same fixed-content ladder; ladder slope with CIs as the primary
  statistic; "law" struck from the framing.
- **M5** (promoted alternate): desk survey run to completion before the slot is committed.

---

## 8. Unresolved disagreements — carried forward, not closed

These are recorded because they are genuine and the panel did not reach agreement. Each is a
decision the Supervisor should make explicitly rather than inherit.

1. **The Final 3 contains zero training runs.** SEG and METH consider this the slate's greatest
   strength: three cheap, decisive, inference-only measurements with preregistered kill conditions
   and both-branch informativeness. FM considers it a portfolio failure — a slate of diagnostics
   with no method contribution and no frontier-model work, which is a weaker position than the
   compute totals suggest. This is the most consequential open disagreement in this document.
2. **Whether C-0090 should have been dropped.** FM dissents from the panel vote. FM's argument is
   that a possible mechanism result on a frontier model class is worth more than a certain audit
   result, and that X5's live dispute makes C-0090 *more* timely, not less. MED's counter is that
   it consumes ten times the Final 3's total compute for a payoff outside the portfolio's declared
   domain. Both positions are on the record; the panel vote follows MED and METH.
3. **Whether B-0121's certification branch is top-venue publishable.** METH yes, FM no. This
   determines whether B-0121 is a high-variance bet or a safe one, and the panel could not settle
   it.
4. **Whether A-0061's likely answer is "sampling-limited."** If the HQ-SAM 52.8 → 70.4 DIS mBIoU
   delta is telling us the output feature path binds, A-0061's headline becomes a validation of the
   HQ line rather than a redirect. METH regards a genuinely two-sided experiment as the point; FM
   regards a validation headline as a materially smaller paper. Unresolved.
5. **Whether B-0212's probe is a hygiene metric or an ablation.** MED: a pipeline is fixed content,
   so a fixed-content-valid probe is exactly right. FM: a metric requiring you to already control
   the generator is not a hygiene check. This decides whether B-0212's most adoptable deliverable
   survives, and it is unresolved.
6. **The medical axis of the Final 3 is thin.** MED's votes on A-0017 and B-0121 are BORDERLINE
   specifically because the medical arms sit in "generalization" sections. If the Supervisor wants
   a genuine medical axis, either those arms are promoted to core (cheap) or B-0212 takes the third
   slot over A-0061 (expensive). The panel did not make this call.
7. **Framing encroachment on A-0017.** `arXiv:2512.22624` occupies the "systematic memory-centric
   study" position without running the decomposition. FM treats this as a mandatory repositioning;
   METH treats it as citable adjacent work. Unresolved, low stakes.

---

**Branch:** `cursor/stage6-defense-top5-2995`
**Artifacts:** `stage6_defense_brief.md` (this file), `stage6_expert_votes.csv`
