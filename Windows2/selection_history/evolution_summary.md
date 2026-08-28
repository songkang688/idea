# Evolution summary (Windows2)

## Stage 1 — CLOSED (count)

| Batch | IDs | n | Path |
| --- | --- | --- | --- |
| A | W2-A-0001–0352 | 352 | `Windows2/_wip/stage1_agent_A/` |
| B | W2-B-0001–0345 | 345 | `Windows2/_wip/stage1_agent_B/` |
| C | W2-C-0001–0345 | 345 | `Windows2/_wip/stage1_agent_C/` |
| **Total** | | **1042** | |

No more Stage-1 generation unless an auditor finds a missing scientific cluster.

## Stage 2/3 — IN PROGRESS (per-batch, then merge)

- D: C catalog (running)
- E: B catalog (running)
- F: A catalog (dispatching)

After all three score files exist: supervisor merges to ~200 with protected exceptions, then Stage 3 continues only on the merged 200 (or mutate survivors).

## Cross-batch merge notes

- Prompt variance: A-0001, B-0042, C-0011
- Metric/label noise: A-0151/0198, C-0046/0057
- SAM/SA-1B prior + contamination: A-0017/0206/0301, C-0082
- Transfer/shift: B-0226/0200, C-0081, A-0245
