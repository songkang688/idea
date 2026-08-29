# Reviewer summary (Windows2)

## Agent D — batch C (detection/eval)

- Files: `Windows2/_wip/stage2_agent_D/`
- Keep 107 (Tier A 79, Tier B 28), mutate 58, kill 180
- Mandatory-15 prior-work: SURVIVE 7 / MUTATE 8 / KILL 0
- Bias: ~70% eval-science; cap before merging into 200
- Blocking uncertainty: cached-prediction availability

## Agent E — batch B (VFM/PEFT)

- Files: `Windows2/_wip/stage2_agent_E/` (already on this branch)
- Keep 77 / kill 268
- Mandatory-15: SURVIVE 6 / MUTATE 7 / KILL 2 (0136, 0175)
- Bias: dynamics/causal upgrades of known static findings; light on artifact papers
- Blocking uncertainty: afternoon VPT-random-token pilot; CoT intervention shelf-life

## Agent F — batch A

- Files: `Windows2/_wip/stage2_agent_F/`
- Keep **75** (Tier A 17 / B 31 / C 21 / protected 6); kill 51; borderline 226
- Prior-work 28: KILL 0017, 0051; 15 MUTATE; 11 SURVIVE
- Flagships if they survive merge: A-0206 SAM fingerprint, A-0163 stuff-band ontology, A-0150 scale-relative GT, A-0145 COD findability bias

## Supervisor policy for 200-cut (draft)

1. Prefer mutated forms after literature collisions, not original one-liners.
2. Cap C eval-audits (~60% of C's slots).
3. Protect cheap mechanism experiments from B even if C scores higher on "significance."
4. Kill correlated duplicates across batches (keep one host idea + named mutations).
5. Do not average scores across D and E — different calibrations.
