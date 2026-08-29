# Idea_02 — Event-disjoint is not camera-disjoint (Windows6 / F-043)

> **Epistemic status of this entire document.** Nothing here has been run.
> Every quantity is **HYPOTHESIS** or **EXPECTED RESULT**. `Windows6/README.md`
> records *"no smoke mAP"*; `proposal.md`'s original text stated *"We have not
> trained a detector here."* That is still true. Citations are **VERIFIED PRIOR
> WORK** only where they already appear in
> `selection_history/literature_anchors.md` or `literature.md`; every other
> slot reads `CITATION NEEDED — 待人工核验`.
>
> **GATE-A is OPEN.** It has never been verified that camera metadata exists on
> any public smoke/fire set. Idea_02's own first stop rule is *"Kill if no
> camera metadata."* See §14 and `stage6_battle.md` §5.

## 1. Title & identifiers

| Field | Value |
|---|---|
| Working title | *Event-Disjoint Is Not Camera-Disjoint: Measuring Smoke Benchmark Inflation* |
| Windows6 ID | `Idea_02` |
| Stage-1 origin | `F-043` (`stage1_pool/F_001_080.jsonl`, seed `smoke`, mutation `cheaper`) |
| Stage-3 record | `camera-id-leakage-smoke`, `continue: keep`, `novelty_confidence: 0.55` |
| Stage-4 record | `camera-ID-smoke`, `continue: survive`, `advance: true` |
| Auditor | protected keep (`auditor_overlay.md`) |
| Selection status | Final 3, **PROVISIONAL** — `stage6_battle.md` §5, blocked on GATE-A |
| Paper type | dataset audit / benchmark |

## 2. One-sentence claim

**HYPOTHESIS.** Published smoke/fire detection scores are inflated by cameras
shared between train and test; **event-disjoint splitting — the current best
practice — does not remove this**, and the residual can be shown to be
background *memorisation* rather than geographic domain shift by scoring empty
frames from seen versus unseen cameras.

## 3. Abstract

**HYPOTHESIS, not measured.** Wildfire-detection CCTV datasets frequently share
cameras across train and validation splits. A Voxel51 audit of Pyro-SDIS
reported large numbers of near-duplicates attributable to shared-camera
familiarity — **as a blog diagnosis, with no retrained mAP delta** (**VERIFIED
PRIOR WORK**, recorded as such in `literature.md`). PYRONEAR-2025 addresses the
problem with **event-disjoint** splits (**VERIFIED PRIOR WORK**, arXiv
2402.05349). We claim event-disjoint is a partial fix: holding out whole
episodes still leaves the same towers, and thus the same backgrounds, on both
sides. Reviewer #2 let this through conditionally: it survives only if we
measure random versus event-disjoint versus camera-disjoint with confidence
intervals **and** run a background-memorisation probe. **No detector has been
trained; no mAP is claimed.**

## 4. Background & motivation

A wildfire tower sees the same ridgeline every day. A detector trained on that
tower can reach high benchmark scores by learning *this ridgeline plus smoke
looks like this* rather than *smoke looks like this*. Two things make the field
vulnerable:

1. **Frames are cheap and episodes are rare.** Datasets are built by sampling
   many frames from few fire events at few towers, so the effective sample size
   is far below the frame count.
2. **The obvious fix is already deployed and looks sufficient.** Event-disjoint
   splitting removes the most visible leak — the same plume on both sides — and
   is therefore easy to mistake for a complete fix.

**SPECULATION (the stakes, not a finding).** If H1–H4 hold, published
smoke-detection numbers are not comparable across papers that used different
split policies, and the operational estimate a fire agency would rely on is
optimistic by an unquantified margin.

**Why the framing is narrow.** "Datasets leak" is not a paper. The contribution
is **quantified inflation plus a confounder split** — geography versus
memorisation.

## 5. Problem statement & research questions

A corpus has three nested groupings: **camera** ⊃ **event** ⊃ **frame**. Three
split protocols break different amounts of it:

| Protocol | Breaks event grouping | Breaks camera grouping |
|---|---|---|
| random | no | no |
| event-disjoint | yes | **no** |
| camera-disjoint | yes | yes |

- **RQ1.** How much does measured performance drop from random to
  camera-disjoint?
- **RQ2.** Does event-disjoint land at the camera-disjoint level, or between?
- **RQ3.** Do frozen features carry camera identity at all?
- **RQ4.** Is any residual gap *memorisation* of backgrounds, or a *geographic*
  distribution shift?

RQ4 is the one that decides whether this is a paper (§10).

## 6. Hypotheses (pre-registered)

- **H1.** Camera-disjoint AP < random-split AP by more than the seed standard
  deviation.
- **H2.** Event-disjoint AP ≠ camera-disjoint AP — a residual same-camera
  different-event leak survives current best practice.
- **H3.** A linear probe on frozen backbone features predicts camera ID above
  chance, **evaluated event-disjoint** (§15).
- **H4.** Empty (no-smoke) frames from **train** cameras draw a higher false
  positive rate or higher confidence than empty frames from unseen cameras.

## 7. Key insight

**Empty frames are the instrument.** They contain no plume, so a seen-versus-
unseen camera gap on negatives cannot be explained by plume-appearance domain
shift. It has to be the background. That single design choice is what converts
"camera-disjoint scores lower" — which a reviewer will read as domain shift, and
therefore as unsurprising — into a claim about memorisation.

The second insight is structural: the three protocols must be **shown** to
differ, not merely named. `splits.camera_overlap` and `splits.event_overlap`
report the overlap counts for every protocol, and the self-checks assert that
event-disjoint still shares cameras. If that were ever false on a real dataset,
H2 would be unfalsifiable there and the pivot in §20 fires.

## 8. Novelty statement

**VERIFIED PRIOR WORK.** PYRONEAR-2025 (arXiv 2402.05349) introduces
event-disjoint splits and pHash deduplication. The Voxel51 Pyro-SDIS audit
diagnosed shared-camera near-duplication — **in a blog post, with no retrained
mAP**.

**The gap.** Nobody has (a) retrained under all three protocols and reported the
deltas with event-clustered CIs, or (b) separated geography from memorisation
with an empty-frame probe. Stage-3 remaining novelty, verbatim: *"Peer-reviewed
inflation quantification across smoke/fire benches."*

**FACT — a standing constraint from `literature.md`:** *"Do not cite a
peer-reviewed mAP inflation number we did not compute."* No number of that kind
appears anywhere in this package.

## 9. Relation to prior work (differentiation)

| Prior work | Status | What it establishes | Why it does not pre-empt us |
|---|---|---|---|
| PYRONEAR-2025, arXiv 2402.05349 | **VERIFIED PRIOR WORK** | Event-disjoint splits, pHash dedup | Simultaneously the closest work and the target. It fixes the episode leak; H2 says the camera leak survives it |
| Voxel51 Pyro-SDIS audit, 2026 blog | **VERIFIED PRIOR WORK** | Shared-camera near-duplicates | A diagnosis without a retrained delta. We retrain and quantify, and we add the confounder split it does not attempt |
| SmokeFrames / Nemo | **VERIFIED PRIOR WORK** (listed, unverified IDs) | Earlier smoke corpora | Candidate second dataset. `literature.md` flags *"check camera IDs before use"* |
| FIgLib | `CITATION NEEDED — 待人工核验` | Candidate corpus | Named in the experiment plan; citation unverified |
| pHash / perceptual hashing | `CITATION NEEDED — 待人工核验` | Dedup instrument | Used in E4 |
| YOLOv8-nano | `CITATION NEEDED — 待人工核验` | The detector | Tooling, not a claim |

## 10. Significance — who is wrong if we are right

- **If H1 + H2 + H4 hold:** cross-paper comparison in smoke detection is
  invalid without a stated split policy, and event-disjoint is insufficient as
  a standard. Actionable: a camera-aware re-split of public benchmarks.
- **If H1 + H2 hold but H4 fails:** we have measured domain shift, which is
  expected and not news. `proposal.md`'s original text is blunt about this:
  *"Fatal if we only report camera-disjoint drop without H4."*
- **If H2 fails** (event-disjoint ≈ camera-disjoint): PYRONEAR already solved
  it, and the honest output is a short confirmation that current practice is
  adequate — worth writing, but not this paper.

## 11. Method overview

1. Inventory camera IDs (**GATE-A**, §14). No IDs, no project.
2. Build the three splits; report camera and event overlap for each.
3. Equal-N, class-ratio-matched test sides so the comparison is fair.
4. Train the detector, 3 seeds per protocol.
5. Report AP and FAR@recall with **event-clustered** bootstrap CIs.
6. Camera-ID probe on frozen features, evaluated event-disjoint.
7. Empty-frame FPR, seen versus unseen cameras.
8. pHash dedup rerun to separate duplicate frames from camera signature.

Implementation: `src/camsplit/`. The split protocols, overlap accounting,
metrics, probe and H4 comparison all run today on a synthetic corpus.

## 12. Instruments

| Instrument | What it isolates | Guard |
|---|---|---|
| **Empty-frame FPR** (H4) | Background memorisation, with plume appearance removed by construction | Detector trained on non-empty frames only, so all empties are held out |
| **Camera-ID probe** (H3) | Whether the representation carries camera identity | Evaluated **event-disjoint**; see §15 |
| **Equal-N matching** | Removes size and class-balance differences between protocols | Raises rather than shipping an unmatched comparison |
| **Event-clustered bootstrap** | Honest CIs under within-event correlation | Resamples events, never frames |
| **pHash dedup rerun** | Separates duplicate frames from camera signature | E4 |

## 13. Null models & baselines

| Role | Method | Purpose |
|---|---|---|
| Upper reference | Random split | The inflated number the field reports |
| Current practice | Event-disjoint split | The thing H2 attacks |
| Honest reference | Camera-disjoint split | The number we argue for |
| Probe control | ImageNet-pretrained backbone never trained on smoke | If it also predicts camera ID, the signal is generic scene identity rather than something the smoke detector learned |
| Negative control | Corpus with `camera_signature = 0` | Everything downstream must come out null. Pinned by a self-check |

## 14. Datasets — and the gate that blocks everything

| Data | Role | Status |
|---|---|---|
| PYRONEAR-2025 | Primary candidate | arXiv 2402.05349 (**VERIFIED PRIOR WORK**). **Camera-ID availability UNVERIFIED** |
| FIgLib | Second dataset candidate | `CITATION NEEDED — 待人工核验`. Camera-ID availability unverified |
| SmokeFrames / Nemo | Fallbacks | `literature.md`: *"check camera IDs before use"* |
| Synthetic corpus (`data.make_corpus`) | Harness validation only | Ships here |

> ### GATE-A — the precondition that keeps Idea_02 provisional
>
> **FACT.** `experiments.md` step 1 has always read *"Inventory camera IDs on
> one public set (PYRONEAR or FIgLib **if IDs exist**)"*, and the first stop
> rule is *"**Kill** if no camera metadata."* No Windows6 artifact records that
> this check was ever performed.
>
> | Outcome | Consequence |
> |---|---|
> | ≥10 cameras with usable IDs | Gate passes; proceed to E1 |
> | 1–9 cameras | Documented pivot to event-disjoint only — **which forfeits H2**, the distinguishing claim. Idea_02 must be re-argued for its Final-3 slot |
> | No camera metadata anywhere | **Idea_02 is killed** by its own stop rule |
>
> This costs hours and no GPU. It is card **E-A** and it runs first.

## 15. Metrics & statistical analysis

**Primary:** image-level **AP** and **FAR@recall**. IoU is secondary — the
operational question for a tower is "how many false alarms at the recall we must
hit", not "how tight is the box".

**CIs: cluster bootstrap over events, never over frames.** Consecutive frames of
one plume from one tower are heavily correlated; a frame-level bootstrap treats
them as independent and reports an interval several times too narrow. That is
the specific way an audit like this overstates its own confidence, so the code
only offers the clustered version.

**The probe must be evaluated event-disjoint.** On a random split the probe can
name the camera by recognising the fire *episode* rather than the tower, which
measures event memorisation and inflates H3 for the wrong reason. **Measured
during W6-T3 on the synthetic corpus:** with the camera signature switched off
entirely, a random-split probe still beat chance by ≈0.17 through shared events
alone. Two self-checks pin this — one asserts the event-disjoint control is near
chance, the other asserts the random-split version *is* confounded, so the rule
cannot be quietly dropped.

**Chance level** is the majority-class rate, reported next to every probe
accuracy. With unbalanced cameras, raw accuracy flatters.

## 16. Killer experiment (run first)

Card **E-A** (GATE-A, no GPU) then card **E1**: PYRONEAR subsample, YOLOv8n,
1 seed × 3 protocols, plus the probe and empty-frame FPR. **≈10 GPU-h
(HYPOTHESIS**, from `evolution_summary.md`; not a measurement).

## 17. Full experimental program

| Card | Content | Budget (HYPOTHESIS) |
|---|---|---|
| E0 | Synthetic harness validation, CPU | ~0 |
| **E-A** | **GATE-A camera inventory** | 0 — no GPU |
| E1 | Killer: 1 seed × 3 protocols + probe + empty-frame FPR | ≈10 GPU-h |
| E2 | 3 seeds, full CIs | ≈30 GPU-h |
| E3 | Probe control on an ImageNet backbone | ≈1 GPU-h |
| E4 | pHash dedup rerun | ≈10 GPU-h |
| E5 | Second dataset | ≈30 GPU-h |

## 18. Ablations & controls

- **Seed ablation:** 3 seeds minimum; H1 requires a gap larger than seed std.
- **Equal-N / class-ratio matching:** on and off, to show the gap is not a
  comparison artifact.
- **Probe backbone ablation:** detector backbone versus ImageNet backbone (E3).
- **Dedup ablation:** with and without pHash (E4).
- **Camera-count sensitivity:** subsample cameras to check the gap is not
  driven by one unusual tower.
- **Negative control:** zero camera signature must null everything.

## 19. Expected results (all EXPECTED RESULT — nothing measured)

- **EXPECTED.** AP ordering random > event-disjoint > camera-disjoint.
- **EXPECTED.** The event-disjoint → camera-disjoint drop is smaller than the
  random → event-disjoint drop, but non-zero. H2 needs only non-zero.
- **EXPECTED.** The camera-ID probe beats chance comfortably; this is the
  easiest of the four to satisfy and therefore the weakest evidence.
- **EXPECTED.** H4 is the hardest. Empty-frame FPR gaps are small, and the
  synthetic harness produced ≈0 gap — a property of a linear stand-in on planted
  features, and **not** a prediction about real data.

## 20. Falsifiability & kill conditions

| Trigger | Action |
|---|---|
| No camera metadata on any usable public set | **KILL** (GATE-A) |
| Camera-disjoint drop vanishes under event-disjoint | **KILL** — PYRONEAR solved it |
| Camera-ID probe at chance, event-disjoint | **KILL** H3 |
| Only one tiny camera set available | **KILL** |
| Cameras < 10 | **PIVOT** to event-disjoint only; forfeits H2 |
| random ≈ camera-disjoint within seed noise **and** probe ≈ chance **and** no empty-FPR gap | **STOP** — confirm with 2 more seeds first |
| Gap fully explained by pHash duplicates | **DOWNGRADE** to a near-duplicate audit — restates the blog with numbers |
| Equal-N matching cannot be achieved | **No result** for that cell; the code raises |

### 20.1 There is no recorded soft landing

**FACT.** Unlike Idea_01, the Stage-4 record gives this idea **no downgrade
clause** — the residual is a requirement, not an *"else …"*. The only documented
fallback is the <10-camera pivot, which forfeits H2. `proposal.md`'s own
language for a missing H4 is *"Fatal"*, not "reduced scope".
`stage6_battle.md` §2.2 recorded the honest reading: **Idea_02 is a full paper
or a kill.** Plan accordingly — do not expect to salvage a partial result.

## 21. Confounders & mitigations

| Confounder | Mitigation |
|---|---|
| Camera = geography (the big one) | Empty-frame probe (H4) |
| Event memorisation masquerading as camera signature | Probe evaluated event-disjoint; both directions pinned by self-checks |
| Duplicate frames rather than camera signature | pHash dedup rerun (E4) |
| Test-set size / class balance differs per protocol | Equal-N, ratio-matched, and the code raises if unachievable |
| Within-event correlation inflating confidence | Event-clustered bootstrap |
| One unusual tower drives everything | Camera-count sensitivity ablation |
| Probe measures generic scene identity | ImageNet control backbone (E3) |

## 22. Reviewer #2 compliance matrix (binding)

| Attack | Binding obligation | Where satisfied |
|---|---|---|
| Novelty: the blog already diagnosed this | Retrain and quantify | E1/E2 |
| Confounder: camera = geography | Empty-frame memorisation probe | H4, §7 |
| Tiny camera N | Multiple folds + CIs | E2, §15 |
| PYRONEAR already "fixed" splits | Show event-disjoint ≠ camera-disjoint | H2, §5 |
| Noisy mAP | 3 seeds, report FAR | §15, E2 |

**Residual obligation (FACT, verbatim):** *"Need event-disjoint vs
camera-disjoint gap plus empty-frame memorization probe."* Both conjuncts are
cards E1 and E2; neither is optional.

## 23. Scope boundaries

- **Not** a new detector, architecture or augmentation.
- **Not** a claim that any specific published number is wrong by a specific
  amount — we do not have those authors' models.
- **Not** a re-derivation of the Voxel51 blog. Duplicates are the *confound*
  (E4), not the finding.
- **Not** a fire-risk or deployment claim.

## 24. Compute & resource budget

**All HYPOTHESIS.** Day-1 ≈10 GPU-h (`evolution_summary.md`). Full program with
3 seeds and a second dataset ≈80 GPU-h. GATE-A and E0 need no GPU at all.

This is the **most expensive** of the Windows6 Final 3 per unit of evidence,
because it is the only one requiring training rather than evaluation. That is
another reason GATE-A must close before anything is spent.

## 25. Reproducibility & release plan

- Seeds fixed via `config.set_seed`, returning an explicit `Generator`.
- **The split code is the deliverable.** Release the camera-aware re-split
  indices so others can reproduce the protocol on the same public data.
- `Split.__post_init__` raises on overlapping train/test indices — a silently
  overlapping split would invalidate everything downstream.
- `tests/test_smoke.py`: 24 self-checks, numpy only.
- Release: split indices, probe code, per-seed metric tables. No imagery
  redistributed.

## 26. Risks & mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| GATE-A fails — no camera metadata | **Fatal** | Check first; costs hours |
| <10 cameras | High | Pivot documented, but H2 is lost |
| H4 null → paper collapses to domain shift | High | No mitigation exists. §20.1: full paper or kill |
| Only one dataset has IDs | Medium | Honest scope; single-dataset audit is weaker but publishable if H4 holds |
| Reviewers read it as "datasets leak, we know" | Medium | Framing discipline: the contribution is the confounder split |

## 27. Ethical & data considerations

Public wildfire-detection corpora under their own licences. Camera IDs are
infrastructure identifiers, not personal data, but tower locations can be
sensitive: publish camera IDs as **opaque indices**, never as coordinates. No
imagery is redistributed — only split indices and derived metrics. The finding,
if it holds, is a caution to benchmark authors; it must not be presented as
evidence that any deployed system is unsafe.

## 28. Deliverables & decision tree

**Deliverables.** Dataset-audit paper; the camera-aware re-split; the probe and
empty-frame protocol as reusable code.

```
E-A GATE-A  ──no camera metadata──> KILL
   │<10 cameras──> PIVOT (event-disjoint only; H2 forfeited; re-argue slot)
   │≥10 cameras
E0 harness  ──structure wrong──> fix (never a scientific conclusion)
   │pass
E1 killer   ──event-disjoint ≈ camera-disjoint──> KILL (PYRONEAR solved it)
   │         ──probe at chance──> KILL H3
   │H1+H2 hold
E2 3 seeds  ──gap inside seed noise──> STOP
   │
E4 dedup    ──gap is all duplicates──> DOWNGRADE to a near-duplicate audit
   │gap survives
   └─> audit paper. E5 second dataset strengthens; E3 probe control is cheap insurance.
```

**Candidate titles.** *Event-Disjoint Is Not Camera-Disjoint: Measuring Smoke
Benchmark Inflation* · *What Do Wildfire Detectors Memorize — Plumes or
Towers?* · *A Camera-Aware Re-split of Public Smoke Benchmarks*
