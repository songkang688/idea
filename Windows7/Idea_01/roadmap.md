# Idea_01 — Implementation Roadmap

Zero training, zero annotation, single A100. The schedule is gated, not calendar-driven: each gate
can kill the project cheaply.

---

## Day 1 — E0, the gate that protects everything

The first experiment is **not** the MVE. It is checkpoint archival, because the project's single
biggest practical risk is that a 2022 paper's OneDrive link died.

- [ ] Download **BAM** (OneDrive) and **HSNet** (Google Drive) first — highest rot risk.
- [ ] Then PFENet, Matcher, PerSAM, FSSAM, SegGPT, SAM/SAM2.
- [ ] SHA-256 everything, mirror to internal storage, record in
      `references/checkpoint_manifest.md`.
- [ ] Request **SAM3** HuggingFace access (gated; lead time is the risk, not the download).
- [ ] Verify each repo runs one forward pass on one episode.

**Gate.** Fewer than 4 methods with verified checkpoints ⇒ the panel is too thin to support a
leaderboard claim. Release the harness and stop. If a checkpoint is unobtainable the panel shrinks
and the paper says so; we do not silently substitute a re-implementation.

---

## Day 2–3 — Harness and pre-registration

- [ ] Support-injection wrappers for PFENet, BAM, Matcher (~tens of lines each against the
      `FSSAdapter` protocol; per-repo preprocessing is deliberately preserved).
- [ ] Assign strata `S1`–`S4` from instance annotations. Publish per-stratum counts.
- [ ] Generate and **freeze** the wrong-support lists (`make_wrong_support_lists.py`) as static
      files, not seeds.
- [ ] Commit `configs/preregistration.yaml` — strata, `τ`, `K`, floors, primary estimator, and the
      killer decision rule verbatim.

**This commit happens before a single inference runs.** It is the artifact that makes every later
number interpretable.

---

## Day 3–5 — E1, the MVE (~1 A100-day)

PFENet + BAM + Matcher + one foundation-era method, PASCAL-5i fold 0 and COCO-20i fold 0.

**Go** if any method retains `R > 0.35` on any stratum, or specialist-vs-foundation retention
differs by >15 points.
**No-go** if all retentions `< 0.2` everywhere including PASCAL `S1`.

---

## Week 2 — E2/E3/E4, the killer experiment (~3.3 A100-days)

- [ ] Full panel × both benchmarks × all folds × all strata × 3 episode-sampling seeds.
- [ ] Floor battery: Floor-A (SAM AMG, strong) and Floor-B (saliency, weak), reported separately.
- [ ] Near vs far wrong-support split.
- [ ] Apply the pre-registered killer rule on `S3`.

---

## Week 3 — E5/E6/E7 and the artifact (~1.2 A100-days)

- [ ] **E5** native vs shared evaluator → the per-method discrepancy table (second headline).
- [ ] **E6** FSS-1000 `S4` degenerate control.
- [ ] **E7** medical transfer probe on MSD/AMOS, training-free methods only.
- [ ] Release the **distractor-enriched split**: episode lists, wrong-support lists, both floors'
      predictions, SHA-256 manifest.

---

## Week 4 — Write

- [ ] Sensitivity-adjusted leaderboard, Kendall τ, position changes.
- [ ] τ-sensitivity curve published regardless of what it shows.
- [ ] Paper draft; artifact packaging.

---

## Branch points

| Observation | Action |
|---|---|
| MVE go-condition fires | continue to Week 2 |
| `S4` high, `S3` low | **pivot to benchmark paper** — the split becomes the deliverable |
| all retentions `< 0.2` everywhere | **pivot to certification note** (weakest branch, priced as such) |
| <4 verified checkpoints at E0 | **kill** |
| 8 A100-days spent | ship with whatever methods ran |

---

## Explicitly out of scope

Building a fix. The moment this becomes a method paper it re-opens every attack the audit design
closes — extra parameters, unfair comparison, unmotivated architecture. Support sensitivity as a
training signal is listed as a future extension (`proposal.md` §26) and stays there.
