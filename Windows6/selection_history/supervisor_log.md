# Windows6 Supervisor Log

Last updated: 2026-08-28 (UTC)
Current stage: **Stage 1 — Massive Idea Exploration** (agents in flight)

## Numbering

Inspected remotes:

- `origin/cursor/research-idea-evolution-windows2-c2c9` → `Windows2/`
- `origin/cursor/idea-evolution-windows3-b534` → `staging/` (Windows3 supervisor ledger)
- `origin/cursor/windows4-research-idea-evolution-2962` → `Windows4/`

User assigned this supervisor **Windows6**. Create `Windows6/`, never overwrite other Windows trees.

## Dispatch log

| Time (UTC) | Action |
|------------|--------|
| 2026-08-28 | Dispatched 3 cloud agents (`claude-fable-5-thinking-xhigh`) for Stage 1 clusters A/B/C, 350 ideas each. |

## Policy

Max 3 concurrent sub-agents. Next jobs after Stage 1 returns:

1. Merge + dedupe + mutate (Supervisor)
2. Independent Reviewer scoring 1000→200
3. Meta-Auditor (echo chamber / false novelty / revive high-risk)
4. Prior-work adversarial search 200→50
5. Reviewer #2 attack 50→20
6. Experimental engineering 20→5
7. Research group battle 5→3
8. Full research packages + git archive

Kill: module stacking, “apply X to medical”, loss-swap, backbone-swap, attention-add with no scientific question.

Protect: high-risk high-reward, cheap-to-falsify, reviewer-disagreement, counter-intuitive simple hypotheses.
