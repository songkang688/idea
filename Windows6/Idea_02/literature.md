# Idea_02 — Literature (verified entries only)

**Sourcing rule.** An entry appears here only if it already exists in
`selection_history/literature_anchors.md` or in the original version of this
file — i.e. only if a Stage-3/4 agent actually web-searched it. Nothing was
added from memory. Where the argument needs a reference that could not be
verified against those sources, the slot reads
`CITATION NEEDED — 待人工核验` rather than a guessed citation.

> **The single most important rule in this package, carried forward verbatim
> from the original file:**
>
> > **Do not cite a peer-reviewed mAP inflation number we did not compute.**
>
> No inflation number appears anywhere in Idea_02. Windows6 has no smoke mAP.

---

## A. Core — the work this project is positioned against

| Work | Year | ID | Relation |
|---|---|---|---|
| PYRONEAR-2025 | 2024/25 | arXiv 2402.05349 | **Both the closest work and the target.** Introduces event-disjoint splits and pHash dedup. H2 claims event-disjoint leaves a residual camera leak, so this paper defines the bar we must clear |
| Voxel51 Pyro-SDIS audit | 2026 | blog | Diagnosed shared-camera near-duplicates. **A diagnosis, with no retrained mAP** — recorded that way in the original file and repeated in `proposal.md` §9. The gap we fill is the retraining and the confounder split |

**Stage-3 remaining novelty (FACT, verbatim):** *"Peer-reviewed inflation
quantification across smoke/fire benches."* Novelty confidence **0.55**.

## B. Candidate corpora

| Work | Status | Note |
|---|---|---|
| SmokeFrames / Nemo | listed in the original file, IDs unverified | Prior sets. Standing warning carried forward: **check camera IDs before use** |
| FIgLib | `CITATION NEEDED — 待人工核验` | Named in the experiment plan as a second-dataset candidate |

**Every corpus needs its own GATE-A inventory** (`experiments.md` E-A) before it
can be used. Being listed here is not evidence that camera IDs exist.

## C. Slots that need human verification before submission

| Needed for | Slot |
|---|---|
| FIgLib dataset | `CITATION NEEDED — 待人工核验` |
| SmokeFrames | `CITATION NEEDED — 待人工核验` |
| Nemo | `CITATION NEEDED — 待人工核验` |
| YOLOv8 / YOLOv8-nano | `CITATION NEEDED — 待人工核验` |
| pHash / perceptual hashing (E4) | `CITATION NEEDED — 待人工核验` |
| Average precision protocol for image-level detection | `CITATION NEEDED — 待人工核验` |
| Cluster bootstrap for correlated observations | `CITATION NEEDED — 待人工核验` |
| Group-aware cross-validation / leakage in ML benchmarks generally | `CITATION NEEDED — 待人工核验` |

The last one matters more than it looks: split leakage is a general
methodological literature, and a reviewer will expect the paper to place itself
in it. Filling that slot is a submission blocker, not a nicety.

## D. Borrowed from the shared anchors

| Work | Year | Venue | Why it is relevant here |
|---|---|---|---|
| Metrics Reloaded | 2024 | Nature Methods | Metric-selection discipline. Cited because the sibling idea `F-022` was **killed** on metric grounds; the same reflex applies to any audit paper that reports a metric property rather than a finding |

## E. How the core citations are used in the argument

- **PYRONEAR-2025** is cited three times over, for three different jobs: as the
  source of the event-disjoint protocol, as the corpus candidate, and as the
  standard H2 argues is insufficient. It must never be cited as though it were
  merely related work — it is the thing being tested.
- **The Voxel51 audit** is cited only as a diagnosis, always with the
  qualification that it reported no retrained mAP. Citing it as evidence of an
  inflation magnitude would be exactly the error the standing rule forbids.
- **Metrics Reloaded** is cited defensively in the metrics section.

## F. Deliberately not cited

General wildfire-detection method papers (new architectures for smoke
detection). They are not the subject: this is an audit of evaluation protocol,
not a comparison of detectors. Citing a pile of them would imply we are claiming
their numbers are wrong by a specific amount, which `proposal.md` §23 explicitly
rules out — we do not have those authors' models.
