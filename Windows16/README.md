# Windows16 — Research Idea Evolution

Canonical research window **Windows16** for the Research Idea Evolution pipeline in
`github.com/songkang688/idea`.

## Window identity (locked)

| Field | Value |
|---|---|
| windows_id | `Windows16` |
| windows_number | `16` |
| windows_path | `Windows16` |
| window_locked | `true` |
| window_defined_by | `P0` |
| window_definition_status | `canonical` |

The number 16 was decided by the P0 Wave B Numbering Consolidator
(`_state/tasks/P0/wave_B/decision.json`, decided 2026-08-28T17:31:00Z) and re-verified
free on all fresh origin refs immediately before this directory was created
(fetch + full-ref scan at 2026-08-28T17:34Z–17:36Z). No bump was required.
Numbers 13/14/15 are spent or staked by sibling pipelines; 2/3/4/6/8/9/10/11/12 are
occupied on unmerged branches; 1/5/7 are never-used gaps that must not be back-filled.

## Pipeline

Idea evolution funnel:

```
1000+ ideas -> 200 -> 50 -> 20 -> 5 -> 3 final ideas
```

| Stage | Survivors |
|---|---|
| Stage 1 — generation | 1000+ |
| Stage 2 — first screening | 200 |
| Stage 3 — second screening | 50 |
| Stage 4 — deep evaluation | 20 |
| Stage 5 — finalist selection | 5 |
| Stage 6 — final ideas | 3 |

## Layout

```
Windows16/
├── README.md                     # this file
├── _state/
│   ├── research_state.json       # canonical machine-readable window + pipeline state
│   ├── window.lock.json          # hard numbering lock (locked=true, defined_by=P0)
│   ├── ideas_master.jsonl        # master idea list, one JSON object per line
│   ├── research_ledger.md        # human-readable ledger of pipeline decisions
│   └── agent_log.md              # agent action log
├── selection_history/            # per-stage selection snapshots
├── final_ideas/                  # the 3 surviving final ideas
└── artifacts/                    # supporting artifacts and evidence
```

## Rules

- This window is **locked**: no agent may renumber, move, or repurpose `Windows16/`.
- Do not modify other `WindowsN/` trees from work performed inside this window.
- All evidence in this window must carry explicit labels
  (KNOWN FACT / VERIFIED PRIOR WORK / EVIDENCE / HYPOTHESIS / MODEL SPECULATION /
  EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT).
- Never fabricate citations, benchmark numbers, datasets, experimental results, or
  git push successes.
