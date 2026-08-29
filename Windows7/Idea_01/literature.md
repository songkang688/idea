# Idea_01 — Literature

**Provenance tags.** `[S5-verified]` = existence-verified by the Stage-5 engineer's searches on
2026-08-28. `[S6-verified]` = surfaced or re-checked during the Stage-6 adversarial pass.
`[inherited]` = carried from the Stage-3/4 ledger without independent re-verification in Stage 5/6.

> **Rule applied throughout this file.** No paper is listed that was not found in the Windows7
> Stage-1→6 sessions. Where only an abstract was read, the entry says so. We do not cite results we
> have not seen, and we do not invent venue/year pairs. Anything below marked `[inherited]` should
> be re-verified before it enters a submission's bibliography.

---

## 1. The mitigation literature — our motivation, and our main attack surface

These papers exist *because* the field believes support quality and class bias matter. None of them
measures how much accuracy survives destroying the support.

| Work | What it actually did | Relation to us |
|---|---|---|
| **BAM** — Lang et al., CVPR 2022 (Oral). `github.com/chunbolang/BAM` `[S5-verified]` | Identifies base-class bias in FSS and adds a base-learner branch to suppress it. | The strongest "this is known" attack (A6). But BAM measures its *fix*, on its own model. We measure the residual across a panel, with a null model. It is also *in* our panel. |
| **TBS** — AAAI 2024 `[inherited]` | Mitigation for foreground/background bias. | Treatment, not assay. Re-verify before citing. |
| **AENet** — ECCV 2024 `[inherited]` | Mitigation in the same family. | Same. Re-verify before citing. |
| **Iterative modulation** — CVPR 2024 `[inherited]` | Support-query interaction refinement. | Same lane. Re-verify. |
| **Support dilution** — `arXiv:2501.13529` `[S6-verified, abstract]` | Perturbs/dilutes support quality as a method-building device. | Closest in *operation*, opposite in *purpose*: they degrade support to build robustness; we destroy it to measure a share. |
| **SADe** — `arXiv:2607.24706` `[S6-verified, abstract]` | Support-aware method in the same lane. | Same distinction. |

**Why the whole column collapses into one sentence for the paper.** Every one of these is a
*treatment*. We are the *diagnostic assay*. The field has been prescribing medicine without ever
measuring how much disease there is.

---

## 2. The validity literature — our unexpected ally

| Work | Finding | Why it matters to us |
|---|---|---|
| **Open-V line** (recorded as X2 in `stage6_defense_brief.md`) `[S6-verified]` | FSS numbers can shift by **up to 37 points** through preprocessing-space mismatch between repositories. Also reports that support contribution *increases as foundation-model text priors weaken* on label-disjoint vocabularies. | Two gifts. (1) It makes absolute FSS numbers untrustworthy, which makes our *ratio* statistic strictly more valuable — retention does not require reproducing anyone's number. (2) Read backwards, "support matters less when the prior is strong" is our hypothesis observed by an unrelated group from the opposite direction. Cite as scaffold; it makes our premise non-speculative rather than contrarian. |

This is also why `experiments.md` E5 (native vs shared evaluator) is funded: it converts a
methodological attack (A5) into the paper's second headline at zero marginal compute, because we
must re-run every checkpoint anyway.

---

## 3. The audited panel

All existence-verified during Stage 5 (2026-08-28). `KNOWN FACT` **Existence-verified is not
fitness-verified** — the day-1 gate (E0) re-downloads and hashes everything.

| Method | Repo / source | Family | Risk |
|---|---|---|---|
| PFENet | `github.com/dvlab-research/PFENet` `[S5-verified]` | specialist | low — 8 pretrained models |
| HSNet | `github.com/juhongm999/hsnet` `[S5-verified]` | specialist | **Google Drive checkpoints — link rot** |
| BAM | `github.com/chunbolang/BAM` `[S5-verified]` | specialist | **OneDrive checkpoints — link rot** |
| Matcher | `github.com/aim-uofa/Matcher`, ICLR 2024 `[S5-verified]` | foundation, training-free | low |
| PerSAM | `github.com/ZrrSkywalker/Personalize-SAM` `[S5-verified]` | foundation, training-free | low |
| FSSAM | `github.com/Sam1224/FSSAM`, ICML 2025 `[S5-verified]` | foundation, SAM2-based | low |
| SegGPT | HF `SegGptForImageSegmentation` `[S5-verified]` | foundation | low |
| SAM / SAM2 | `facebookresearch` official `[S5-verified]` | — (Floor-A) | low |
| **SAM3-exemplar** | official release, HF-gated `[S6-verified]` | foundation | **added at Stage 6** — access must be requested day 1 |

---

## 4. SAM3 and the significance clock

`EVIDENCE` SAM3 released Nov 2025 (`arXiv:2511.16719`); SAM 3.1 Mar 2026 `[S6-verified]`. SAM3
performs exemplar-prompted concept segmentation — and an image exemplar **is** a support.

This produced the single most important Stage-6 correction to this project (attack A1): a
specialist-centric audit of 2020–2022 models risks indicting a museum. The fix is cheap and is
already folded into the design — add a SAM3-exemplar arm and make **foundation-era retention the
co-headline**, with the specialists demoted to a historical control. The interesting 2026 question
is not whether PFENet used its support; it is whether SAM3 does.

---

## 5. Datasets

| Dataset | Role | Note |
|---|---|---|
| PASCAL-5i (VOC2012 + SBD) | standard FSS | `S3` stratum is thin here |
| COCO-20i (COCO 2014) | **primary `S3` carrier** | instance annotations give strata for free |
| LVIS-92i | high multi-object density | as used by Matcher `[S5-verified]` |
| FSS-1000 | `S4` degenerate control | single centred object *by construction* — the point |
| MSD / AMOS CT slices | generalisation probe | training-free methods only |

Licences: VOC/SBD/COCO/LVIS/FSS-1000 are standard research licences. No annotation budget, no
credentialed data, no API spend.

---

## 6. What a reviewer will cite against us, and where the answer lives

| Likely citation | The attack | Answer |
|---|---|---|
| BAM (CVPR 2022 Oral) | "Base-class and foreground bias is known." | `proposal.md` §7 + §22/A6: known as a *treatment target*, never measured as a share against a null model, never stratified. |
| TBS / AENet 2024 wave | "The community already fixed this." | Same. Their existence is our motivation section; a fix does not report the size of what it fixed across a panel. |
| SAM3 / `arXiv:2511.16719` | "You audited obsolete models." | §22/A1: SAM3-exemplar arm, foundation-era co-headline. |
| Metrics/evaluation-reform literature | "Another eval paper." | The deliverable is an artifact — a distractor-enriched split with frozen episode and counterfactual lists — not an opinion. |

---

## 7. Open verification debt

Carried forward honestly rather than hidden:

1. TBS (AAAI 2024), AENet (ECCV 2024) and the CVPR 2024 iterative-modulation entry are
   `[inherited]` — **re-verify venue, year and content before they enter a bibliography.**
2. `arXiv:2501.13529` and `arXiv:2607.24706` were read at **abstract level only**.
3. The Open-V / X2 "37 points" figure is `EVIDENCE` reported by that group, not measured by us, and
   should be quoted with attribution and a re-read of the primary source.
