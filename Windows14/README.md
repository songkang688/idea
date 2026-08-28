# Windows14 — Research Idea Evolution Workspace

Canonical research window **Windows14** (windows_number=14), defined and locked by **P0 INITIALIZE WINDOWS**.

- **Repository**: https://github.com/songkang688/idea
- **Init branch**: `cursor/windows14-p0-init-implementation-46a8`
- **Pipeline**: `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`
- **Status**: initialized (Stage 1 pending)
- **Lock**: `Windows14/_state/window.lock.json` (`locked=true`, `defined_by="P0"`, written inside the init commit)
- **Canonical decision**: `_state/tasks/p0/windows_init/decision.json` (Wave B consolidator, branch `cursor/p0-windows-init-consolidator-9906`)

## Layout

| Path | Purpose |
|---|---|
| `_state/research_state.json` | Canonical machine-readable window state |
| `_state/window.lock.json` | Authoritative window lock (windows_id/number/path, locked=true) |
| `_state/ideas_master.jsonl` | Master idea list, one JSON object per line (empty at init) |
| `_state/research_ledger.md` | Append-only ledger of pipeline events |
| `_state/agent_log.md` | Append-only per-agent action log |
| `selection_history/` | Per-stage selection evidence |
| `final_ideas/` | Final surviving ideas (target: 3) |
| `artifacts/` | Supporting artifacts |

## Numbering evidence (at init, 2026-08-28T17:43:55Z pre-mkdir re-fetch)

Occupied windows on origin refs (branches and PR heads): 2, 3 (legacy `staging/Windows3_supervisor/`), 4, 6, 8, 9, 10, 11, 12, 13 (locked), 16 (locked). Numbers 1, 5, 7 are burned gaps — never gap-fill. Windows15 is claimed by a sibling pipeline via judged verdict (no directory yet) — never take. Windows14 was absent from every origin tip at both the pre-mkdir and pre-lock re-fetch scans, so the decided `Windows14` was used without a bump.

## Rules

- Do not modify other `Windows*` trees from this window.
- Never force-push. Record real push results only.
- All JSON must pass `python3 -m json.tool` before commit.
- No invented experiments, citations, benchmarks, or results — evidence labels per `research_state.json` `evidence_policy`.
