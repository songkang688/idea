# Idea_03 — Literature (verified entries only)

**Sourcing rule.** An entry appears here only if it already existed in the
original version of this file or in
`selection_history/literature_anchors.md` — i.e. only if a Stage-3/4 agent
actually web-searched it. Nothing was added from memory. Where the argument
needs a reference that could not be verified against those sources, the slot
reads `CITATION NEEDED — 待人工核验` rather than a guessed citation.

---

## A. Core — cite these as attacks, not as background

| Paper | Year | Venue / ID | Relation |
|---|---|---|---|
| **MDGD** | 2025 | EMNLP Findings | Visual forgetting under instruction tuning. **This is the paper that killed our generic headline at Stage 3.** It must be cited explicitly and early: "MDGD establishes the phenomenon; we ask which stage pays and whether the backbone still contains the box." A related-work mention reads as ignorance |
| **TWIST & SCOUT** | 2025 | ICCV | Grounding / forget-free tuning. Proposes a **fix**. A fix that works does not tell you which stage paid, which is the gap we occupy |
| RL-finetuned VLM robustness | 2026 | arXiv 2602.12506 | Adjacent and **recent**. Must be re-checked for scoop immediately before writing — recent enough that a v2 could contain this result |
| LLaVA / LLaVA-RLHF families | 2023–24 | — | Candidate checkpoint pairs **if licences allow**. Subject to GATE-B verification before use |

## B. The gap, and how strong the evidence for it is

**FACT, verbatim from the original file:**

> Stage 3: stage-isolated localization curve was **NOT FOUND** as a standalone
> paper (EVIDENCE GAP, conf ~0.5).

**This is an absence-defined novelty claim and the file should say so plainly.**
The evidence is that a search did not find the paper — **confidence ~0.5**, the
lowest of the Windows6 Final 3 — not that the paper cannot exist.
`stage3_DE_top10.json.md` independently records E-009 at **0.55** with the note
*"matched checkpoint localization tax still open"*, and `Windows6/README.md`
marks Idea_03 *"highest concurrent-work risk"*.

Absences close without anyone doing anything wrong. `proposal.md` §26.1 treats
this as a scheduling constraint rather than a caveat.

## C. Slots that need human verification before submission

| Needed for | Slot |
|---|---|
| Qwen-VL / Qwen-VL-Chat (candidate pair named in the experiment plan) | `CITATION NEEDED — 待人工核验` |
| RefCOCO / referring-expression benchmark | `CITATION NEEDED — 待人工核验` |
| DPO (the H3 instrument, card E4) | `CITATION NEEDED — 待人工核验` |
| LoRA | `CITATION NEEDED — 待人工核验` |
| Grammar-constrained decoding (eval mode 2) | `CITATION NEEDED — 待人工核验` |
| Linear probing of frozen representations (the H2 instrument) | `CITATION NEEDED — 待人工核验` |
| Alignment tax in language models (the general phenomenon) | `CITATION NEEDED — 待人工核验` |
| RLHF / instruction tuning for VLMs, as a general reference | `CITATION NEEDED — 待人工核验` |

The last two matter most: this paper claims a *localization-specific* alignment
tax, and a reviewer will expect it placed within the general alignment-tax
literature. Filling those slots is a submission blocker, not a nicety. They are
left empty on purpose — a plausible-looking bibtex entry reconstructed from
memory is worse than a visible hole, because the hole gets checked.

## D. How the core citations are used in the argument

- **MDGD** appears in the abstract, in §8 novelty, in §9 differentiation, and in
  `reviewer_attacks.md` A1. It is the single most load-bearing citation in the
  package, and it is load-bearing *against* us.
- **TWIST & SCOUT** is cited to draw the diagnose-versus-fix line. It must not
  be described as "related grounding work"; it is the strongest evidence that
  the community already considers this cost worth engineering around.
- **arXiv 2602.12506** is cited as adjacency and re-checked before writing.
- **LLaVA / LLaVA-RLHF** is cited only as a checkpoint-pair candidate, always
  with the GATE-B qualification attached.

## E. Deliberately not cited

General VLM capability benchmarks and leaderboard papers. This is a diagnosis of
*where* a measured cost originates, not a claim about model quality, and citing
a pile of benchmarks would imply a comparative claim `proposal.md` §23 rules
out. Similarly, papers proposing new grounding architectures are out of scope:
the subject is a measurement protocol, not a method.
