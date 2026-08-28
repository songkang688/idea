# P0 Wave A — Worker C: Workspace Planner (Stage P0 — Initialize Windows)

- **Task:** `p0_windows_init` — propose an initialization PLAN for the next Windows directory
- **Dispatcher identity:** `Windows14` (X=Windows14 — PARENT PROCESS NAME ONLY; not automatically the Windows directory id)
- **Repo:** https://github.com/songkang688/idea (remote `origin`)
- **Inspected at:** 2026-08-28 ~17:14 UTC
- **Method:** `git fetch origin --prune` from a stale local clone (local `main` had only the root commit), then inspected remote refs with `git ls-tree -r`, `git show`, and `git log --all` across all 21 `origin/*` heads.
- **Scope compliance:** This worker did **not** create any `WindowsN/` directory, did **not** write a canonical `research_state.json` for a real WindowsN, and did **not** write or lock `windows_id`. Plan only.

---

## 1. Evidence: existing Windows* layouts (KNOWN FACT unless labeled otherwise)

Prior Windows trees exist — the "no prior Windows tree" fallback does **not** apply. All Windows content lives on unmerged `cursor/*` branches; `origin/main` is a single root commit (`990f3eb`) containing only `README.md`.

### 1.1 Modern P0-init layout (Windows9, Windows10, Windows11, Windows12)

Four branches (`origin/cursor/windows9-p0-init-3045`, `.../windows10-p0-init-26ec`, `.../windows11-p0-init-c0c1`, `.../windows12-p0-init-a095`) share an identical initialization tree (verified byte-for-byte on path names via `git ls-tree -r`):

```
WindowsN/
├── README.md
├── _state/
│   ├── agent_log.md
│   ├── ideas_master.jsonl        (empty at init)
│   ├── research_ledger.md
│   └── research_state.json
├── artifacts/.gitkeep
├── final_ideas/.gitkeep
└── selection_history/.gitkeep
```

### 1.2 Older / mature layouts (context, not the init template)

- **Windows6** (`origin/cursor/windows6-research-idea-evolution-b55d`): `Windows6/README.md`, `research_summary.md`, `selection_history/stage1_pool/*.jsonl`, `selection_history/{evolution_summary.md, supervisor_log.md}` — shows `selection_history/` is where stage pools and evolution records accumulate.
- **Windows8** (`origin/cursor/windows8-research-idea-evolution-cd91`): completed pipeline; ends with `Windows8/Idea_01..03/` research packages (proposal.md, literature.md, experiments.md, reviewer_attacks.md, roadmap.md, src/, configs/, outputs/) — shows the final deliverable shape that `final_ideas/` is meant to hold in the modern layout.
- **Windows2/Windows4**: top-level `WindowsN/` dirs with stage catalogs and ledgers; predate the `_state/` convention.
- **Windows3 anomaly:** exists only as `staging/Windows3_supervisor/` on `origin/cursor/idea-evolution-windows3-b534` — never a top-level `Windows3/`. Treat as a deviation NOT to repeat.

### 1.3 State-file content conventions (from Windows12, the most recent init)

- `research_state.json` — machine-readable canonical state: `windows_id`, `windows_path`, `repository`, `branch`, `base_branch`, `created_at`, `supervisor`, `current_stage`, `target_pipeline`, `total_ideas`, `survivors`, `final_target`, `status`, plus `numbering` (scan evidence + decision), `git_safety` (pre-init HEAD, init commit, verified push SHA, `push_failure_reason`), `ideas_index`, `current_ranking`, `agent_slots`, `evidence_policy` (claim labels + forbidden fabrications).
- `research_ledger.md` — human-readable ledger: identity block, research scope/priorities, science values (prefer falsifiable hypotheses / failure modes; downweight "Module A + Module B" pseudo-novelty), evidence rules, numbering decision table, current stage, next stage.
- `agent_log.md` — chronological P0 action log: git pre-check, numbering scan, sub-agent dispatch table (including failures with real error strings), actions, overwrite check.
- `ideas_master.jsonl` — empty at init; one JSON object per idea later.
- **WARNING (KNOWN FACT):** `Windows11/_state/research_state.json` is **invalid JSON** (`"wave": 1b` — unquoted non-numeric literal, fails `json.load`). The new WindowsN plan below requires JSON validity checks before commit.

### 1.4 Commit message conventions (KNOWN FACT, from `git log --all`)

Two observed families:

1. P0 init commits (Windows9–12): `Initialize WindowsN research workspace (P0)` (+ follow-up `Record verified WindowsN P0 push SHA`).
2. Stage-work commits (Windows2/3/4/6/8): `Research Idea Evolution - WindowsN - <action>` (note: Windows 6/8 wrote `Windows 6` with a space; Windows2/3/4 wrote `Windows2` without — no-space form is the majority and preferred).

### 1.5 Lock-file convention

**KNOWN FACT:** No `window.lock.json` exists on any scanned ref, and no prior `research_state.json` contains `window_locked` / `window_defined_by` / `window_definition_status` fields. The lock file/schema in §5 is a **new mechanism introduced by this pipeline**, not an observed prior convention.

### 1.6 Sibling shard evidence (VERIFIED PRIOR WORK — fetched ref)

`origin/cursor/p0-init-repo-inspector-1ccf` carries a Wave A "worker_A repository inspector" shard under a **different** dispatch layout (`_p0_dispatch/tasks/p0_init/`, parent-requested suffix `-05a0`). It independently found max Windows number = 12 and recommended 13 (explicitly "NOT a lock"). This confirms at least one other concurrent P0 dispatch is active — a numbering race is a live risk.

---

## 2. Numbering analysis for the new WindowsN (decision belongs to Wave B judge / P0 Final, not this worker)

- **KNOWN FACT:** Windows numbers occupied on scanned refs: 2, 3 (staging anomaly), 4, 6, 8, 9, 10, 11, 12. Max = 12. Neither `Windows13` nor `Windows14` appears in any tree or commit message on any fetched ref (checked 2026-08-28 ~17:13 UTC).
- **KNOWN FACT (precedent):** Windows12's recorded `numbering_decision`: the supervisor's given identity name ("Windows12") was frozen as the directory id even though the sequential template said Windows11, explicitly to honor identity and avoid racing concurrent inits. Windows11's init used identity == sequential (both said 11), so it does not discriminate between rules.
- **Candidates:**
  - `Windows13` — sequential template `Windows{max_n+1}`. Risk: sibling dispatch's worker_A already recommended 13; highest collision probability among concurrent runs.
  - `Windows14` — dispatcher identity name; free on all scanned refs; follows the Windows12 identity-if-free precedent; lower collision risk.
- **RECOMMENDATION (HYPOTHESIS — for the judge, not a lock):** Prefer **Windows14** (identity-if-free precedent + concurrency safety), with **Windows13** as fallback if the judge rules identity-based numbering non-canonical. Whichever is chosen, P0 Final MUST re-run `git fetch origin --prune` immediately before locking and re-verify the chosen `WindowsN` is absent from every `origin/*` head (overwrite check), exactly as Windows12's `overwrite_check` did.

Everything below uses the placeholder `WindowsN` deliberately.

---

## 3. Proposed directory structure for the new WindowsN

Matches the Windows9–12 convention (§1.1), plus the new lock file (§5):

```
WindowsN/
├── README.md                      # identity, numbering evidence, research scope, pipeline, status table, next step
├── _state/
│   ├── research_state.json        # canonical machine state (schema per Windows12 + lock fields of §5)
│   ├── ideas_master.jsonl         # empty at init; one JSON object per idea thereafter
│   ├── research_ledger.md         # human-readable ledger: scope, priorities, evidence rules, decisions
│   ├── agent_log.md               # chronological action/dispatch log incl. real sub-agent errors
│   └── window.lock.json           # NEW — window identity lock (schema in §5); written only by P0 Final
├── selection_history/             # stage pools, keep/kill lists, evolution summaries (.gitkeep at init)
├── final_ideas/                   # final research packages, Windows8 Idea_01..03 shape (.gitkeep at init)
└── artifacts/                     # supporting artifacts: configs, scripts, outputs (.gitkeep at init)
```

Placement and git rules (from observed convention):

- `WindowsN/` is **top-level** in the repo (do not repeat the Windows3 `staging/` anomaly).
- Created on a dedicated branch off `main` @ `990f3eb`, e.g. `cursor/windowsN-p0-init-<suffix>`; never force-push; nothing merged to `main` to date.
- Only files under `WindowsN/` (and, for this dispatch, `_state/tasks/`) may be touched; other Windows trees and root `README.md` are read-only.
- Empty dirs are anchored with `.gitkeep`.
- All `.json` state files MUST pass a JSON validity check (e.g. `python3 -m json.tool`) before commit — motivated by the Windows11 malformed-JSON defect (§1.3).

### Initial content of each state file

- `README.md` — identity block (WindowsN, creation date, supervisor, repo, branch, status=initialized), KNOWN-FACT numbering scan summary, research scope/priorities, pipeline field (§4), status table (total_ideas=0, survivors=0, final_target=3), next step = P1/Stage 1.
- `_state/research_state.json` — Windows12 schema (§1.3) with `status: "initialized"`, `total_ideas: 0`, empty `ideas_index`/`current_ranking`, real `git_safety` values, plus the §5 lock fields once P0 Final locks.
- `_state/ideas_master.jsonl` — created empty.
- `_state/research_ledger.md` — scope, priorities, science values, evidence rules, numbering-decision table.
- `_state/agent_log.md` — P0 log started with git pre-check and numbering scan entries.
- `_state/window.lock.json` — §5; written by P0 Final only, never by Wave A workers.

---

## 4. Proposed pipeline field

```
1000+ -> 200 -> 50 -> 20 -> 5 -> 3
```

Stored as `target_pipeline` in `research_state.json` and rendered in README/ledger. **KNOWN FACT:** identical string to Windows12's `target_pipeline` and the pipeline lines of the Windows9–11 inits — this proposal introduces no deviation.

---

## 5. Proposed lock schema — `_state/window.lock.json` (DOCUMENTATION ONLY; live lock NOT written by this worker)

To be written only by P0 Final/Init after a fresh fetch + overwrite check. Required fields:

```json
{
  "windows_id": "WindowsN",
  "windows_number": N,
  "windows_path": "WindowsN",
  "window_locked": true,
  "window_defined_by": "P0",
  "window_definition_status": "canonical"
}
```

Field semantics:

| Field | Type | Meaning |
|---|---|---|
| `windows_id` | string | Canonical window identity, e.g. `"Windows14"`; must equal the top-level directory name |
| `windows_number` | integer | Numeric N, e.g. `14`; must match the digits of `windows_id` |
| `windows_path` | string | Repo-root-relative directory path, e.g. `"Windows14"` (top-level; no `staging/` nesting) |
| `window_locked` | boolean | MUST be `true` once written; later stages MUST NOT renumber the window |
| `window_defined_by` | string | MUST be `"P0"` — only Stage P0 may define window identity |
| `window_definition_status` | string | MUST be `"canonical"` — marks this the single source of truth over any conflicting mention |

Recommended (optional) additions for auditability, mirroring Windows12's `git_safety`/`numbering` practice: `locked_at` (UTC ISO-8601), `locked_by` (dispatcher/process name, e.g. `"Windows14"`), `base_branch`, `init_branch`, `init_commit`, `numbering_evidence` (occupied numbers + scan timestamp). The same six required fields SHOULD also be mirrored into `research_state.json` so both files agree.

**KNOWN FACT:** No prior branch contains this file or these fields (§1.5); this schema is new with this pipeline, not an inherited convention.

---

## 6. Proposed commit message

For the WindowsN initialization commit (as mandated for this plan):

```
Research Idea Evolution - WindowsN - Initialization
```

with `WindowsN` replaced by the locked id (e.g. `Research Idea Evolution - Windows14 - Initialization`). **KNOWN FACT:** this follows the majority stage-work family `Research Idea Evolution - WindowsN - <action>` (no space before N, per Windows2/3/4; Windows 6/8 used a space — do not copy). Prior P0 inits (Windows9–12) used `Initialize WindowsN research workspace (P0)` instead; if the judge prefers strict init-family continuity that is the alternative, but this plan proposes the mandated `Research Idea Evolution - WindowsN - Initialization`.

---

## 7. Claim classification

| # | Claim | Label |
|---|---|---|
| 1 | Local `main` = single root commit `990f3eb` (README.md only); fetch performed before all scans | KNOWN FACT (observed in this clone after `git fetch origin --prune`) |
| 2 | Windows9–12 share the layout in §1.1 (README, `_state/` × 4 files, 3 `.gitkeep` dirs) | KNOWN FACT (`git ls-tree -r` on the four fetched branch heads) |
| 3 | Windows2/4/6/8 are top-level dirs; Windows3 exists only as `staging/Windows3_supervisor/` | KNOWN FACT (tree scans of fetched refs) |
| 4 | Occupied numbers {2,3,4,6,8,9,10,11,12}; max = 12; Windows13/Windows14 absent from all scanned refs | KNOWN FACT (tree + commit-message scan at ~17:13 UTC; race window remains after that timestamp) |
| 5 | Windows12 froze the identity name over the sequential template | VERIFIED PRIOR WORK (recorded `numbering_decision` in Windows12's `research_state.json`) |
| 6 | Windows11's `research_state.json` is invalid JSON | KNOWN FACT (`json.load` fails: `"wave": 1b`, line 114) |
| 7 | A sibling dispatch's worker_A recommended Windows13 | VERIFIED PRIOR WORK (shard on `origin/cursor/p0-init-repo-inspector-1ccf`) |
| 8 | No `window.lock.json` or lock fields exist on any prior ref | KNOWN FACT (regex scan of every remote branch tree + the four `research_state.json` files) |
| 9 | Concurrent P0 runs may claim 13/14 after my scan timestamp | HYPOTHESIS (motivated by claims 4, 5, 7; Windows9–12 branch tips span 16:50–16:59 UTC today) |
| 10 | Windows14 is the better primary candidate; Windows13 the fallback | HYPOTHESIS / RECOMMENDATION (judgment from claims 4, 5, 7, 9 — not a lock, judge decides) |
| 11 | Pipeline string matches Windows12's `target_pipeline` verbatim | KNOWN FACT (`git show` of the file) |
| 12 | Commit-message families in §1.4 | KNOWN FACT (`git log --all --format=%s`) |

No citations to external papers, benchmarks, or datasets are made anywhere in this plan; none were needed and none were fabricated.

---

## 8. Handoff to Wave B judge

Open items this worker could not resolve (also listed in `worker_C.done.json`):

1. Final N selection (13 vs 14) and the mandatory lock-time re-fetch + overwrite check.
2. Commit-message family choice: mandated `Research Idea Evolution - WindowsN - Initialization` vs observed init family `Initialize WindowsN research workspace (P0)` (§6 proposes the former).
3. Whether the six lock fields live only in `window.lock.json` or are also mirrored into `research_state.json` (this plan recommends mirroring).
