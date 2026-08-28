# Windows13 Research Ledger

Append-only ledger of pipeline events for Windows13. Newest entries at the bottom.

| # | UTC time | Stage | Event | Evidence label | Detail |
|---|---|---|---|---|---|
| 1 | 2026-08-28T17:30:52Z | P0 | Pre-mkdir race-guard re-fetch + re-scan of all origin heads | KNOWN FACT | `git fetch origin --prune`; Windows13 absent everywhere; zero window.lock.json on any origin head; occupied numbers {2,3,4,6,8,9,10,11,12}; no bump needed |
| 2 | 2026-08-28T17:31:30Z | P0 | Windows13 tree created and locked (window.lock.json locked=true, defined_by=P0) | KNOWN FACT | Per canonical decision.json on origin/cursor/p0-init-consolidator-9302; init branch cursor/windows13-p0-init-implementation-d93f |
| 3 | 2026-08-28T17:32:40Z | P0 | Init commit pushed and verified on origin | KNOWN FACT | Commit 38641a7a5813ed06b9b80c560e227ef382f76502; `git ls-remote` returned matching SHA for refs/heads/cursor/windows13-p0-init-implementation-d93f; post-push re-fetch scan found no competing Windows13 claim on any other origin branch |
