# Idea_01 — Literature (verified entries only)

**Sourcing rule for this file.** An entry may appear here only if it already
exists in `selection_history/literature_anchors.md` or in the original version
of this file — i.e. only if a Stage-3/4 agent actually web-searched it. Nothing
was added from memory. Where the argument needs a reference that could not be
verified against those two sources, the slot reads
`CITATION NEEDED — 待人工核验` rather than a guessed citation.

**We do not claim to have re-run anyone's tables.** Every entry is **VERIFIED
PRIOR WORK** in the sense "recorded as searched and used to kill or mutate an
idea", not "replicated".

---

## A. Core — the gap this project occupies

| Paper | Year | Venue / ID | Relation |
|---|---|---|---|
| Segment Anything | 2023 | ICCV | Defines AMG, the object of study |
| SAM2 CT review | 2024 | arXiv 2408.11210 | Black-box CT evaluation. Filed in `literature_anchors.md` under *"Remaining-novelty targets"* precisely because it is **not** an AMG-vs-clustering test |
| SAM/SAM2 low-contrast CT | 2024 | arXiv 2408.04212 | **Closest adjacency.** Establishes intensity/window dependence; cited by Reviewer #2. Shows sensitivity, not equivalence, and runs no texture control |

**Gap (FACT, carried forward verbatim from the original file):** *"no AMG vs
k-means Hungarian/ARI study with texture-vs-intensity counterfactuals."*
Stage-3 novelty confidence **0.6** — the highest in Windows6.

## B. Constrains what we may claim

| Paper | Year | Venue / ID | Constraint it imposes |
|---|---|---|---|
| HQ-SAM | 2023 | NeurIPS, arXiv 2306.01567 | Mask-quality refinement. Standing constraint: **we do not claim filter = HQ-SAM.** That framing belonged to the adjacent `F-012`, which `stage2_ABCF_summary.md` forbids restating |
| SAMRefiner | 2025 | arXiv 2502.06756 | Same family; refinement is not mechanism |
| MedSAM-related CT notes | 2024 | arXiv 2408.03322 | Benchmark context, cited by Reviewer #2 as MedSAM framing |
| MedSAM TTA without parametric updates | 2025 | arXiv 2504.02008 | Adaptation context. Out of scope per `proposal.md` §23 — adaptation is not our subject |
| Metrics Reloaded | 2024 | Nature Methods | Metric-selection discipline. **The paper that killed sibling idea `F-022`** for reporting a near-definitional property. Standing warning against the same mistake here |

## C. Slots that need human verification before submission

None of these could be verified against `literature_anchors.md` or the original
`literature.md`, so none is cited with a year, venue or ID.

| Needed for | Slot |
|---|---|
| SLIC superpixels (the spatial control, §13) | `CITATION NEEDED — 待人工核验` |
| Otsu / multi-Otsu thresholding | `CITATION NEEDED — 待人工核验` |
| Adjusted Rand Index (Hubert & Arabie or equivalent) | `CITATION NEEDED — 待人工核验` |
| Hungarian / Kuhn–Munkres assignment | `CITATION NEEDED — 待人工核验` |
| Boundary-F / contour F-measure protocol | `CITATION NEEDED — 待人工核验` |
| TotalSegmentator dataset | `CITATION NEEDED — 待人工核验` |
| Medical Segmentation Decathlon (MSD) | `CITATION NEEDED — 待人工核验` |
| COCO (E4 control) | `CITATION NEEDED — 待人工核验` |

These are all standard and almost certainly easy to fill. They are left empty
on purpose: a plausible-looking bibtex entry reconstructed from memory is worse
than a visible hole, because the hole gets checked and the entry does not.

## D. Deliberately NOT cited, and why

| Work | Why it is excluded |
|---|---|
| SAM-U (arXiv 2307.04973), UR-SAM (arXiv 2311.10529) | Prompt-jitter uncertainty. Used in Stage 3 to **kill** `prompt-jitter-uncertainty`; unrelated to our mechanism claim |
| RITM (arXiv 2102.06583), Stable Segment Anything (ICLR 2025) | Interactive-click behaviour. Killed the `multiclick-nonmonotonic` idea; not our subject |
| LN-TTA (WACV 2026), IGTTA (IEEE TMI 2025) | Test-time adaptation; killed `F-014` |
| KiTS23 (arXiv 2309.02001), Randomized Histogram Matching (arXiv 2104.14032) | Intensity-alignment domain adaptation; killed `histogram-matching-da`. Adjacent to our intensity theme but a different question — they *fix* intensity shift, we *diagnose* intensity dependence |
| LoRA vs Full Fine-tuning (arXiv 2410.21228) | PEFT; killed `lora-effective-rank`. Different cluster |
| Mehrtash et al. (IEEE TMI 2020) | Dice-vs-CE calibration; killed `dice-vs-ce-calibration` |

Listing these matters: a reviewer who sees the SAM-uncertainty literature
uncited may assume ignorance. It was searched and deliberately excluded.

## E. How each core citation is used in the argument

- **arXiv 2408.04212** is the paper that makes our hypothesis plausible *and*
  the one that most nearly pre-empts it. `proposal.md` §9 states the difference
  explicitly: it demonstrates window sensitivity; it does not test equivalence
  against a clusterer and it runs no intensity/texture dissociation.
- **arXiv 2408.11210** is cited to establish that CT evaluation of SAM-family
  models is black-box — which is exactly the gap a mechanistic study fills.
- **Segment Anything (ICCV 2023)** is cited only for the AMG definition. We
  make no claim about SAM's design intent.
- **Metrics Reloaded** is cited defensively, in the metric-selection section,
  because the sibling idea died on that ground.
- **HQ-SAM / SAMRefiner** are cited to fence off the `F-012` framing.
