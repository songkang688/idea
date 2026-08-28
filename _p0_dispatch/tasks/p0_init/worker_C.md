# P0 INITIALIZE WINDOWS — Worker C (Workspace Planner) Plan

- **task_id:** p0_init
- **role:** worker_C_workspace_planner
- **agent:** Agent C — independent cloud sub-agent (planning only; creates NO WindowsN directory, locks NO window id)
- **repository:** https://github.com/songkang688/idea (default branch `main`)
- **worker branch:** `cursor/p0-init-worker-c-ce9b` (based on `main` @ `990f3ebc75d7ab03a8960cf0d1e5621cbb29194a`)
- **plan written at:** 2026-08-28T17:10:50Z (UTC)

---

## 1. Evidence — what I actually inspected (KNOWN FACT)

All statements below were verified directly in this workspace at plan time. No fabricated citations, git results, or directories.

### 1.1 Fetch freshness

- `git fetch origin --prune` executed at ~2026-08-28T17:09Z, **exit code 0** (real result). The fetch pulled new refs including `origin/cursor/windows9-p0-init-3045`, `windows10-p0-init-26ec`, `windows11-p0-init-c0c1`, `windows12-p0-init-a095`, plus updates to several stage1/windows branches. This plan is NOT based on a stale snapshot.

### 1.2 `main` state

- `main` == `origin/main` == `990f3eb` "Initial commit". Working tree clean.
- `main` contains **only** a root `README.md` (8 bytes, content `# fnyuan`). **No Windows directory exists on `main`.**

### 1.3 Windows directories across ALL origin heads (systematic `git ls-tree` scan of every remote branch)

| Top-level dir | Evidence branch |
|---|---|
| `Windows2/` | `origin/cursor/research-idea-evolution-windows2-c2c9`, `windows2-stage1-agent-{a,b,c}-*` |
| `Windows4/` | `origin/cursor/windows4-research-idea-evolution-2962` |
| `Windows6/` | `origin/cursor/windows6-research-idea-evolution-b55d` |
| `Windows8/` | `origin/cursor/windows8-research-idea-evolution-cd91` |
| `Windows9/` | `origin/cursor/windows9-p0-init-3045` |
| `Windows10/` | `origin/cursor/windows10-p0-init-26ec` |
| `Windows11/` | `origin/cursor/windows11-p0-init-c0c1` |
| `Windows12/` | `origin/cursor/windows12-p0-init-a095` |

- Not found as top-level dirs on any head: `Windows1`, `Windows3` (its branch `cursor/idea-evolution-windows3-b534` used `staging/` instead), `Windows5`, `Windows7`, and anything ≥ `Windows13`.
- **Max N observed on origin heads = 12.**

### 1.4 Prior P0-init conventions (read from Windows9–Windows12 branches)

Every prior P0-init branch committed exactly this tree (verified via `git ls-tree -r`):

```
WindowsN/README.md
WindowsN/_state/agent_log.md
WindowsN/_state/ideas_master.jsonl        (committed as EMPTY 0-byte file — verified for Windows9/11/12)
WindowsN/_state/research_ledger.md
WindowsN/_state/research_state.json
WindowsN/artifacts/.gitkeep
WindowsN/final_ideas/.gitkeep
WindowsN/selection_history/.gitkeep
```

- **No prior init committed `_state/window.lock.json`** — it is a new addition in this round's spec; scheme proposed in §3.6.
- `research_state.json` convention (from Windows12): keys `windows_id`, `windows_path`, `repository`, `branch`, `base_branch`, `created_at`, `supervisor`, `current_stage`, `target_pipeline`, `total_ideas`, `survivors`, `final_target`, `status`, plus `numbering` (scan evidence), `git_safety` (pre-init HEAD, push verification), `ideas_index`, `current_ranking`, `agent_slots`, `evidence_policy`.
- README convention: window identity header, KNOWN-FACT numbering scan, research priorities (VFM / multimodal / PEFT / SAM / segmentation / detection first priority), pipeline line, status table, next-step (P1) pointer.
- Commit style of prior inits: an init commit followed by a "record verified push SHA" commit; never force-push; never touch other Windows dirs or root README.

---

## 2. Proposed directory structure (to be created by the supervisor at P0 execution, NOT by this worker)

```
Windows{N}/                          # N decided at lock time; my suggestion: 13 (see §4)
├── README.md                        # window identity, scope, pipeline, status table
├── _state/                          # machine + human state, single source of truth
│   ├── research_state.json          # canonical machine state (see §3.2)
│   ├── ideas_master.jsonl           # append-only idea registry, 1 JSON object/line (see §3.3)
│   ├── research_ledger.md           # human-readable ledger: scope, priorities, stage gates (see §3.4)
│   ├── agent_log.md                 # chronological agent/dispatch log with FACT labels (see §3.5)
│   └── window.lock.json             # window-id lock record; created UNLOCKED at init (see §3.6)
├── selection_history/               # per-stage funnel evidence (see §3.7)
│   └── .gitkeep
├── final_ideas/                     # the 3 surviving Research Packages (populated at P5/P6)
│   └── .gitkeep
└── artifacts/                       # code, configs, diagrams, toy outputs referenced by ideas
    └── .gitkeep
```

Rationale: identical to the Windows9–12 convention (maximizes cross-window tooling compatibility), plus the newly specified `window.lock.json`. Empty dirs are kept in git via `.gitkeep`, matching prior inits.

## 3. Initialization scheme per file

### 3.1 `Windows{N}/README.md`

Initialize with (following Windows11/12 template):

1. Title: `# Windows{N} — Autonomous Research Idea Evolution`.
2. Identity block: windows id, creation date (UTC), supervisor, repo, branch, status `initialized`, statement "本轮只写入 `Windows{N}/`；编号锁定后不得改号".
3. **KNOWN FACT numbering scan block**: re-run the origin-heads scan at execution time and record it (do NOT copy my table blindly — see §4 collision caveat).
4. Goal: from 1000+ raw ideas, via falsifiable filtering, produce **3** executable Research Packages; ban architecture-stitching pseudo-novelty.
5. Research priorities (first: VFM, multimodal/VLM, LLM fine-tuning, PEFT/LoRA/Adapter, SAM family, image/medical segmentation, smoke/fire/transparent-ambiguous segmentation, detection; second: medical VFM, DA, few/zero-shot, prompt learning, weak/semi/self-supervised, synthetic data, representation learning, dense-prediction VLM, robustness/calibration/uncertainty, cross-domain).
6. Pipeline line: `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`.
7. Status table: Stage=Stage 1, total_ideas=0, survivors=0, final_target=3, status=initialized.
8. Next step: P1 Stage 1 mass idea exploration; placeholder must not be written as completed research.

### 3.2 `Windows{N}/_state/research_state.json`

Single canonical machine state. Initialize with:

```json
{
  "windows_id": "Windows{N}",
  "windows_path": "Windows{N}",
  "repository": "https://github.com/songkang688/idea",
  "branch": "<init branch>",
  "base_branch": "main",
  "created_at": "<UTC ISO-8601 at execution>",
  "supervisor": "Windows{N}",
  "current_stage": "Stage 1",
  "target_pipeline": "1000+ -> 200 -> 50 -> 20 -> 5 -> 3",
  "stage_targets": {"stage1_generate": "1000+", "stage2_screen": 200, "stage3_deepen": 50,
                    "stage4_attack": 20, "stage5_finalists": 5, "stage6_packages": 3},
  "total_ideas": 0,
  "survivors": 0,
  "final_target": 3,
  "status": "initialized",
  "numbering": { "scan_scope": ["worktree_top_level", "origin_heads"],
                 "existing_windows_found": ["<fill from execution-time scan with per-id evidence>"],
                 "max_n": "<observed>", "this_round": "Windows{N}",
                 "overwrite_check": "<must pass before any mkdir>" },
  "git_safety": { "pre_init_branch": "main", "pre_init_head": "<sha>",
                  "working_tree_at_pre_init": "clean", "force_push": false,
                  "init_commit": null, "push_status": "pending", "push_failure_reason": null },
  "ideas_index": [],
  "current_ranking": [],
  "evidence_policy": { "labels": ["KNOWN FACT", "VERIFIED PRIOR WORK", "EVIDENCE", "HYPOTHESIS",
                                   "MODEL SPECULATION", "EXPECTED RESULT", "ACTUAL EXPERIMENTAL RESULT"],
                        "forbid_fiction": ["paper_or_citation", "benchmark_number", "dataset_information",
                                            "claimed_ran_experiments", "experimental_results", "false_git_push_success"] }
}
```

`push_status` starts `pending` and is only flipped to `verified_success` after the pusher confirms the remote SHA (matches Windows9–12 practice of a follow-up "record verified push" commit).

### 3.3 `Windows{N}/_state/ideas_master.jsonl`

Initialize as an **empty 0-byte file** (verified convention of Windows9/11/12). Append-only; one JSON object per idea. Proposed per-line schema (documented in the ledger, not enforced by the empty file):
`{"id": "W{N}-I####", "title", "stage_entered", "stage_current", "status": "alive|killed|merged", "source_agent", "one_liner", "falsifiable_hypothesis", "kill_reason": null, "artifact_paths": [], "created_at"}`.

### 3.4 `Windows{N}/_state/research_ledger.md`

Initialize with: round identity block (windows id, path, repo, branch, created_at, supervisor); research scope + two-tier priorities; pipeline `1000+ -> 200 -> 50 -> 20 -> 5 -> 3` with a stage-gate table (stage, target count, entry/exit criteria, evidence file under `selection_history/`); evidence-label policy; empty "Stage 1 ledger" section ready for appends.

### 3.5 `Windows{N}/_state/agent_log.md`

Initialize with: `# Windows{N} Agent Log` and a first entry `## <date> — P0 Initialize Windows` containing: git pre-check FACTs (branch, HEAD SHA, clean/dirty), the execution-time numbering scan result, sub-agent dispatch table (wave, roles, real results — including failures verbatim, per Windows11 convention), and the numbering decision. Every subsequent dispatch/merge appends chronologically; never rewrite history.

### 3.6 `Windows{N}/_state/window.lock.json` (new this round — not present in Windows9–12)

Created at init in **UNLOCKED** state, because per task rules this planner must not lock the window id. The supervisor flips it after the final execution-time re-scan:

```json
{
  "windows_id": null,
  "locked": false,
  "locked_by": null,
  "locked_at": null,
  "lock_scope": "window_numbering",
  "numbering_scan": { "scanned_at": null,
                       "scan_scope": ["worktree_top_level", "origin_heads"],
                       "max_n_observed": null,
                       "ids_found": [],
                       "suggested_by_workers": {"worker_C": "Windows13"} },
  "rule": "Supervisor must re-run fetch+scan immediately before locking; locked windows_id must not exist as a top-level dir on any origin head, and must never change afterwards."
}
```

### 3.7 `selection_history/` (funnel evidence, mapped to pipeline)

Empty at init (`.gitkeep` only). Populated per stage, following Windows4/Windows6 precedent (`stage1_pool/*.jsonl`, `stage2_top200.md`, `supervisor_log.md` etc.):

| Stage transition | Target | Evidence file(s) to add later |
|---|---|---|
| Stage 1 generate | 1000+ raw ideas | `stage1_pool/*.jsonl` (per-agent shards), `stage1_supervisor_seed*.md` |
| Stage 2 screen | 1000+ → 200 | `stage2_top200.md` + `stage2_top200_ids.txt` + review shards |
| Stage 3 deepen | 200 → 50 | `stage3_top50.md` + per-idea deepening notes |
| Stage 4 attack | 50 → 20 | `stage4_top20.md` + reviewer-attack records |
| Stage 5 finalists | 20 → 5 | `stage5_top5.md` + kill matrix |
| Stage 6 packages | 5 → 3 | `stage6_final3.md`; packages materialize under `final_ideas/` |

### 3.8 `final_ideas/` and `artifacts/`

Empty at init (`.gitkeep`). `final_ideas/` later holds the 3 Research Packages (per Windows8 package precedent: `proposal.md`, `literature.md`, `experiments.md`, `roadmap.md`, `reviewer_attacks.md`, `src/`, `configs/`, `diagrams/`, `references/`). `artifacts/` holds shared code/toy outputs referenced from ideas; anything non-textual or heavy should be summarized as text reports.

## 4. Suggested Windows id (SUGGESTION ONLY — not locked by this worker)

**Suggestion: `Windows13`.**

- Basis (KNOWN FACT from §1.3): max N on all origin heads after a fresh fetch = **12**; `Windows13` appears nowhere (no dir, no branch name). Template `Windows{max_n+1}` ⇒ 13. Creating it cannot overwrite any prior research.
- **Collision caveat (HYPOTHESIS):** Windows9–12 were all created today by concurrent runs, so other in-flight initializers may also compute 13. The locker MUST re-fetch and re-scan immediately before locking, and if `Windows13` has appeared, move to the smallest unused N > 13. Gap-filling with 1/3/5/7 is NOT recommended: prior rounds left those gaps deliberately and reusing them risks aliasing with historical discussion of those ids.

## 5. Suggested commit message for the actual initialization commit

`Research Idea Evolution - Windows13 - Initialization` (replace `13` if the locked id differs). Note: prior inits used a different style ("Initialize WindowsN research workspace (P0)"), but the dispatcher's specified template takes precedence.

## 6. Git safety rules for the initializer

Never force-push; never modify root `README.md`, other `Windows*` dirs, or `_p0_dispatch/` shards of other workers; base off fresh `origin/main`; record real push results (verify remote SHA) before writing `push_status: verified_success`.

## 7. Unresolved items

1. Final WindowsN cannot be guaranteed by this worker — concurrent inits today make 13 collision-prone; must be re-scanned at lock time.
2. `window.lock.json` has no prior in-repo precedent; my §3.6 schema needs judge/supervisor ratification.
3. Whether `selection_history/` stage subfolders are pre-created at init or lazily at each stage — prior windows created them lazily; I propose lazy (init keeps only `.gitkeep`).
4. Root `README.md` on `main` is a bare placeholder (`# fnyuan`); out of scope for P0 per prior convention, flagged for a future housekeeping decision.
