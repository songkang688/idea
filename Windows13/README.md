# Windows13 — Research Idea Evolution Workspace

Canonical research window **Windows13** (windows_number=13), defined and locked by **P0 INITIALIZE WINDOWS**.

- **Repository**: https://github.com/songkang688/idea
- **Init branch**: `cursor/windows13-p0-init-implementation-d93f`
- **Pipeline**: `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`
- **Status**: initialized (Stage 1 pending)
- **Lock**: `Windows13/_state/window.lock.json` (`locked=true`, `defined_by="P0"`, written inside the init commit)
- **Canonical decision**: `_p0_dispatch/tasks/p0_init/decision.json` (Wave B consolidator, branch `cursor/p0-init-consolidator-9302`)

## Layout

| Path | Purpose |
|---|---|
| `_state/research_state.json` | Canonical machine-readable window state |
| `_state/window.lock.json` | Authoritative window lock (windows_id/number/path, locked=true) |
| `_state/ideas_master.jsonl` | Master idea list, one JSON object per line (empty at init) |
| `_state/research_ledger.md` | Append-only ledger of pipeline events |
| `_state/agent_log.md` | Append-only per-agent action log |
| `selection_history/` | Per-stage selection evidence (lazy, per-stage files) |
| `final_ideas/` | Final surviving ideas (target: 3) |
| `artifacts/` | Supporting artifacts |

## Numbering evidence (at init, 2026-08-28T17:30:52Z re-fetch)

Occupied windows on origin heads: 2, 3 (legacy `staging/Windows3_supervisor`), 4, 6, 8, 9, 10, 11, 12. Numbers 1, 5, 7 are burned gaps — never gap-fill. Windows13 was absent from every origin tip (trees, branch names, commit messages) and zero `window.lock.json` files existed anywhere, so the decided `Windows13` was used without a bump.

## Rules

- Do not modify other `Windows*` trees from this window.
- Never force-push. Record real push results only.
- All JSON must pass `python3 -m json.tool` before commit.
- No invented experiments, citations, benchmarks, or results — evidence labels per `research_state.json` `evidence_policy`.
