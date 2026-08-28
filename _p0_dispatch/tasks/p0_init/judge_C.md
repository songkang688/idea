# P0 Wave B — Judge C: Conventions / Init-Plan Verdict

- **Task:** `p0_init` — Wave B judge shard C (conventions + directory/file init scheme)
- **Role:** `judge_C_conventions`
- **Repo:** https://github.com/songkang688/idea
- **Judged at:** 2026-08-28T17:18Z (UTC)
- **Method:** Independent fresh scan (`git fetch origin --prune` twice: ~17:16Z and ~17:17Z), full `git ls-tree` of every `origin/*` head, `git log --all` commit-message scan, content grep for `Windows13`/lock fields across all refs, plus review of all three Wave A shards.
- **Scope compliance:** This judge did NOT create any `WindowsN/` directory, did NOT write `decision.json`, and did NOT write `window.lock.json`. Recommendation only.

---

## 1. VERDICT — Window identity for THIS run

| Field | Value |
|---|---|
| `windows_id` | **`Windows13`** |
| `windows_number` | **`13`** |
| `windows_path` | **`Windows13`** (repo-root top-level dir, no trailing slash, no `staging/` nesting) |

### Basis (fresh scan, not worker echo)

**KNOWN FACT (scan at 2026-08-28T17:17:52Z, after second `git fetch origin --prune`):**

- Top-level `WindowsN/` dirs on origin heads: **Windows2, Windows4, Windows6, Windows8, Windows9, Windows10, Windows11, Windows12**.
- `Windows3` exists only as nested `staging/Windows3_supervisor/` on `origin/cursor/idea-evolution-windows3-b534` and `origin/cursor/w3s1-cluster-b-7ea7` — number 3 counts as OCCUPIED; the staging layout is a legacy anomaly NOT to be repeated.
- `origin/main` is a single root commit (`990f3eb`) containing only `README.md`; no WindowsN has ever existed on main.
- Max occupied number = **12** (`Windows12/` on `origin/cursor/windows12-p0-init-a095`, created 2026-08-28T16:57:10Z).
- `Windows13` appears in **zero** trees, **zero** commit messages (`git log --all` grep count = 0), and **zero** branch names on any fetched ref.
- Numbers 1, 5, 7 never existed on any ref; monotonic-max+1 convention (documented in Windows9–12 numbering blocks) forbids gap-filling.

**Convergence:** All three Wave A workers independently recommended 13 (worker_A `recommended_new_windows_number: 13`, worker_B `recommended_new_windows_number: 13`, worker_C `suggested_windows_id: "Windows13"`). My fresh scan confirms 13 is still free ~6 minutes after their scans.

**New race evidence (post-Wave-A, KNOWN FACT):** During my judging window a new branch appeared: `origin/cursor/p0-windows-init-worker-c-f747` — a Wave A worker from a **sibling P0 dispatch whose dispatcher identity is "Windows14"**. That shard explicitly cites this run's worker_A recommendation of 13 and recommends its own run take **Windows14** precisely to avoid colliding with our 13. This lowers (but does not eliminate) collision risk on 13. Unlike Windows12, THIS run has no human identity-freeze instruction, so sequential max+1 = 13 is correct; there is no basis to jump to a higher identity number.

**Mandatory guard for Implementation Agent:** re-run `git fetch origin --prune` and re-scan all origin heads IMMEDIATELY before creating the tree. If `Windows13` has been claimed in the interim, bump to the smallest unused N > 13 that is absent from every origin head (note the sibling dispatch has signaled intent to claim 14 — if 13 is taken, verify 14 before considering it, else 15…). Never gap-fill 1/5/7 and never reuse 3.

---

## 2. VERDICT — Directory / file init scheme

Follow the Windows9–12 P0-init scaffold (verified identical across all four branches) **plus** the new `window.lock.json` mandated this round. Exact tree Implementation Agent must create:

```
Windows13/
├── README.md
├── _state/
│   ├── research_state.json      # canonical machine state incl. NEW lock fields (§3)
│   ├── window.lock.json         # NEW this round — written locked=true at init (§4)
│   ├── ideas_master.jsonl       # empty 0-byte file at init (Windows9/11/12 convention)
│   ├── research_ledger.md       # identity block, scope/priorities, stage-gate table, evidence policy
│   └── agent_log.md             # append-only P0 action log: git pre-check, scan, dispatch table w/ real errors
├── selection_history/
│   └── .gitkeep                 # stage evidence added lazily per stage (Windows4/6 precedent)
├── final_ideas/
│   └── .gitkeep                 # later: 3 Research Packages (Windows8 Idea_01..03 shape)
└── artifacts/
    └── .gitkeep                 # shared code/configs/toy outputs; binaries summarized as text
```

Rules: touch ONLY `Windows13/` (plus `_p0_dispatch/` bookkeeping); never modify root `README.md`, other `Windows*` trees, or other agents' shards; never force-push; base off freshly fetched `origin/main`.

**JSON validity gate (new, evidence-driven):** `Windows11/_state/research_state.json` on `origin/cursor/windows11-p0-init-c0c1` is **invalid JSON** (unquoted literal `"wave": 1b`, fails `json.load`). Implementation MUST validate every `.json` file (e.g. `python3 -m json.tool`) before committing.

---

## 3. VERDICT — `research_state.json` contents

Base fields follow the Windows12 schema (most recent valid precedent): `repository`, `branch`, `base_branch`, `created_at` (UTC ISO-8601), `supervisor`, `current_stage: "Stage 1"`, `total_ideas: 0`, `survivors: 0`, `final_target: 3`, `status: "initialized"`, `numbering` (execution-time scan evidence + overwrite check), `git_safety` (pre-init HEAD, `force_push: false`, real push status only after remote SHA verification), `ideas_index: []`, `current_ranking: []`, `evidence_policy` (labels + forbid_fiction list).

**Lock fields P0 must eventually write** (NEW — no prior `research_state.json` on any ref contains them; verified by grep across all origin heads):

```json
{
  "windows_id": "Windows13",
  "windows_number": 13,
  "windows_path": "Windows13",
  "window_locked": true,
  "window_defined_by": "P0",
  "window_definition_status": "canonical"
}
```

**Pipeline field (exact string, matches Windows9–12 `target_pipeline`):**

```
"target_pipeline": "1000+ -> 200 -> 50 -> 20 -> 5 -> 3"
```

(Funnel stages: Stage 1 generate 1000+ → Stage 2 screen 200 → Stage 3 deepen 50 → Stage 4 attack 20 → Stage 5 finalists 5 → Stage 6 packages 3.)

---

## 4. VERDICT — `window.lock.json`

- **Path:** `Windows13/_state/window.lock.json` (inside `_state/`, the established single-source-of-truth dir).
- **No precedent exists** on any ref (verified: zero `*lock*` files in any branch tip outside `_p0_dispatch/` shards) — this file is a new mechanism; the dispatcher schema is authoritative.
- **Required fields:**

```json
{
  "windows_id": "Windows13",
  "windows_number": 13,
  "windows_path": "Windows13",
  "repository": "https://github.com/songkang688/idea",
  "branch": "<implementation agent's actual init branch>",
  "created_at": "<UTC ISO-8601 at init commit time>",
  "locked": true,
  "defined_by": "P0"
}
```

- **Write `locked: true` in the init commit itself**, immediately after the final re-fetch + re-scan passes the overwrite check. Do NOT use worker C's two-phase "create unlocked, flip later" design (see contradiction C1).
- Optional audit additions (harmless, mirror Windows12 practice): `locked_at`, `base_branch`, `init_commit`, `numbering_evidence`. Required dispatcher fields take precedence on any name clash.

---

## 5. VERDICT — Commit message

Implementation Agent's init commit MUST be exactly:

```
Research Idea Evolution - Windows13 - Initialization
```

**KNOWN FACT:** two commit-message families exist in history: (1) `Research Idea Evolution - WindowsN - <action>` (Windows2/3/4/6/8 — the dominant family; Windows2/3/4 use no space before N, Windows 6/8 inserted a space — do not copy the spaced form), and (2) `Initialize WindowsN research workspace (P0)` (Windows9–12 inits, each followed by a `Record verified WindowsN P0 push SHA` commit). The dispatcher template is mandatory and aligns with family (1). A follow-up commit recording the verified push SHA (family-2 second-commit practice) is permitted and recommended; the init commit message itself is fixed.

---

## 6. Contradictions & resolutions vs Wave A workers

| # | Contradiction | Resolution |
|---|---|---|
| C1 | **worker_C** proposes `window.lock.json` created UNLOCKED (`windows_id: null, locked: false`, fields `locked_by`/`locked_at`), flipped later by supervisor | **OVERRULED.** Dispatcher requires `locked=true`, `defined_by="P0"`, and identity fields at P0. P0 *is* the locker; a committed-unlocked window invites a sibling run to claim the same number. Write locked=true in the init commit after the final re-scan. Worker C's audit extras may be kept as optional additions only. |
| C2 | **worker_C** `numbering_scan.windows_ids_absent` lists `Windows3` as absent (top-level scan), while **worker_A/worker_B** count 3 as occupied (staging form) | **Workers A/B correct.** Number 3 is occupied for numbering purposes (staging/Windows3_supervisor evidence); worker_C's own `windows3_note` acknowledges this — its "absent" entry is a scan-scope artifact, not a real disagreement, and worker_C also refuses gap-filling. No numbering impact: all agree next = 13. |
| C3 | Commit-style tension: Windows9–12 precedent `Initialize WindowsN research workspace (P0)` vs dispatcher template | **Dispatcher template wins** (`Research Idea Evolution - Windows13 - Initialization`); it also matches the dominant family. Worker_C already reached the same conclusion. |
| C4 | **worker_A** flags branch-suffix deviation (parent requested `-05a0`, VM enforced `-1ccf`) | Informational only; no impact on identity or scheme. This judge's VM likewise enforces suffix `-f02e`. |
| C5 | **Post-Wave-A evidence workers could not see:** sibling P0 dispatch (identity "Windows14") pushed `origin/cursor/p0-windows-init-worker-c-f747` at ~17:14Z recommending its run take Windows14 and deferring 13 to this run | Confirms workers' race warnings were justified and current. Keeps 13 as our correct claim; mandatory final re-fetch guard stands. |
| C6 | None of the workers' schemas include `windows_number` (int) — Windows9–12 `research_state.json` also lack it | Dispatcher schema adds it; include `windows_number: 13` in both `research_state.json` and `window.lock.json`. |

**No contradiction on the core verdict:** all three workers and this judge's independent scan converge on **Windows13**.

---

## 7. Handoff

- `recommended_next_task_type`: **`wave_b_consolidator`** — consolidate judge shards, write `decision.json`, then Implementation Agent creates `Windows13/` per §2–§5 (with the final re-fetch guard of §1).
