# Agent L Report — Stage-6 Meta-Reviewer / Auditor (temporary deputy PI)

Role: adversarial audit of the whole Windows2 pipeline before the Top-5 lock. I do not pick the final 3.
Inputs: research_summary.md, selection_history/*, PI_TO_I.md, stage1 A/B/C reports, stage2 D/E/F/G full outputs
(reports, kills, shortlists, collisions, census, provisional-200), stage4 H/J full outputs. stage2_agent_I and
stage4_agent_K did not exist at audit time. Six live web-search batches were run to verify load-bearing citations and
attack the emerging finalists; every URL in my files was returned by live search this session. No files outside
`Windows2/_wip/stage6_agent_L/` were modified.

Deliverables: `audit.md` (8 findings, EVIDENCE/HYPOTHESIS-labeled), `revive.md` (10 revival actions with cheapest tests),
`portfolio_risk.md` (AC simulation + correlation matrix + lock constraints), this report.

## Headline verdicts

- **Citation integrity: GOOD.** Every kill citation I spot-checked is real (HalluSegBench, HII-DPO, Faithfulness-of-
  Visual-Thinking, Label Convergence, RClicks-era kills, registers/SINDER). Nobody invented papers. Two kills are
  over-broad in scope, not in existence.
- **Novelty vigilance: ASYMMETRIC.** Kills were checked hard; keeps were not. The two top gravity wells both have
  fresh adjacent literature the pipeline missed (details in audit.md Findings 1–2).
- **Portfolio shape: DANGEROUS.** Current gravity = ~2 effective independent bets wearing 4 costumes, all audits or
  audit-adjacent, all cheap enough to carry H's measured ~1/3-per-year scoop hazard.

## The 10 recommendations the PI must act on before locking the Top 5

1. **Downgrade A-0061 from "bare SURVIVE" to "SURVIVE with mandatory positioning."** A Jan-2026 paper
   (arXiv 2601.06067) already ships a topology-aware checkpoint-selection rule ("min-PD within top-K Dice"), and
   arXiv 2412.14619 prescribes the metrics (Betti matching, no dimension aggregation). The systematic multi-seed
   quantification is still open — but the ledger's "only un-gated A survive" line is stale. Fix the ledger.
2. **Strike the "afternoon pilot" framing of B-0114 everywhere.** The original VPT paper (arXiv 2203.12119, Fig. 11)
   already ran the frozen-prompt control: Prompt-Fixed ≈ Linear, gains come from learned embeddings. By E's own
   pre-registered rule this drops naive-0114 to mid-list. Commit only to H's 4-arm mechanism design, restricted to
   dense tasks and register-free vs register-equipped backbones, and adopt the NOP-vs-broadcast diagnostics
   (arXiv 2606.08105) or reviewers will.
3. **Cap the register/token-artifact micro-field at one slot in the Top 5.** B-0114 and B-0001 share one literature,
   one confound family, and one obsolescence event. Pick one; make the other a named arm.
4. **Enforce a constructive quota at the lock:** at least one of the Top 3 (two of the Top 5) must ship a method or
   usable artifact (C-0306, C-0309, A-0163 are LOCK-ready candidates). Current gravity is 4 diagnoses, 0 fixes;
   `portfolio_risk.md` gives the AC read.
5. **Attach execution-start deadlines to every cheap finalist.** Anything ≤2 GPU-weeks starts within one quarter or
   forfeits its slot. H measured the decay rate; B-0332 is what portfolio-storage does to cheap ideas.
6. **Process the revive list (`revive.md`).** Highest-value: C-0334 (protected-override never signed off),
   A-0199-mut (both scooping papers are VLM-side; the training-data-grounded dose-response version is bigger than the
   "sliver" J granted), A-0028 (SAM2 teleport — F's "best of C02" that fell through the top-20 crack and was never
   attacked), C-0082-mut (SAM failure law lost its slot in the merge machinery).
7. **Record the four missing PI sign-offs on G's protected-idea overrides** (C-0334, C-0251, C-0253, C-0271). If the
   protection mechanism can be silently overridden, every protection tag in this pipeline is theater. Also arbitrate
   the B-0033 conflict: a Stage-4 kill currently overrides a Stage-2 DP protection + Stage-2.5 merge contract with no
   adjudication.
8. **Decide the venue mix before the Top 5, in writing.** Three of four gravity wells are NeurIPS-D&B/analysis-track
   papers; F and D both said the ranking inverts under a CVPR-method-track objective. The Top 5 follows from the venue
   decision; locking in the reverse order guarantees a re-litigation at writing time.
9. **Close the coverage gaps deliberately, or abandon them in writing:** (a) medical FM science is one unfunded
   compute-partner away from empty — secure the partner or promote a medical-executable candidate (A-0075 post-pilot,
   A-0065); (b) SAM2/video has zero representation above tier-2 — give A-0028 a Reviewer-2 pass; (c) smoke/fire is
   debunk-only — merge A-0090's TTD metric into A-0100. Implicit abandonment is the only wrong choice.
10. **Correct for the echo chamber in confidence accounting.** D/E/F/H/J share one base model and one prompt culture;
    their convergence on "quantification-with-controls" is partly self-similarity (H: 0 bare SURVIVEs in 29; J: 0 kills
    in 23 — both self-flagged). Treat five agreeing agents as ~2 independent opinions. Concretely: before the lock,
    commission one deliberately contrarian pass with an inverted mandate ("argue the most ambitious surviving claim UP;
    find the constructive paper hiding in each audit") over the Top 10, and require K's C-batch attack plus I's fold to
    land before any gravity list is treated as ordering.

## Self-audit (biases of this audit)

- I attacked the supervisor's gravity wells hardest because the ledger told me they matter — the same anchoring I
  criticize in Finding 6.4. Ideas outside the gravity list got proportionally less search effort; C-batch keeps got
  almost none (K's job, still running).
- My web verification sampled ~12 load-bearing citations out of hundreds; "citation integrity: GOOD" extrapolates from
  that sample. The unsearched ~120 keeps (G's admission) remain the largest unverified surface, and my audit did not
  close it.
- My scoop-probability arithmetic (≈70% for three cheap finalists in a year) assumes independence and H's base rate;
  both are rough. Treat it as an order-of-magnitude argument for deadlines, not a forecast.
- I am the same base model as the agents I audited. Findings that required noticing what five prior agents missed
  (VPT Fig. 11, arXiv 2601.06067) came from live search, not superior judgment — which is itself the strongest
  argument for recommendation 5's re-search gates.

## Compliance

- All writes confined to `Windows2/_wip/stage6_agent_L/`. No other agent's file was modified; ledger corrections are
  recommended in text, not applied.
- No final-3 selected; no idea scored; revive list is advisory.
- After this report I return to the ordinary pool.
