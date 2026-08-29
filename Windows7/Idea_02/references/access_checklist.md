# Idea_02 — Day-1 Access Checklist

**Status: TEMPLATE. Nothing below has been confirmed.**

This project has one hard external dependency with no fallback, so access is checked before any
engineering.

## Hard dependency

| Resource | Host | Status | Confirmed on |
|---|---|---|---|
| **DiDi** (distractor-distilled VOS set) | `go.vicos.si/didi`, linked from DAM4SAM | ☐ | |

`KNOWN FACT` There is no mirror. If DiDi is unavailable, the harvest descopes to LVOS v2 + SA-V val
and the paper reports the distractor-density gap explicitly rather than pretending the corpus is
equivalent.

## Repositories (pin by commit, not branch)

| Repo | Role | Cloned | Commit SHA | Smoke test |
|---|---|---|---|---|
| `facebookresearch/sam2` | subject; surgery hooks fork from here | ☐ | | ☐ |
| `yangchris11/samurai` | comparator | ☐ | | ☐ |
| `jovanavidenovic/DAM4SAM` | comparator + DiDi | ☐ | | ☐ |
| `Mark12Ding/SAM2Long` | comparator | ☐ | | ☐ |
| `LingyiHongfd/LVOS` | data | ☐ | | ☐ |
| `LingyiHongfd/lvos-evaluation` | J&F scoring | ☐ | | ☐ |

## Gated

| Resource | Requested | Granted | Note |
|---|---|---|---|
| SAM3 tracking zoo (via `arXiv:2512.22624`) | ☐ | ☐ | lead time is the risk, not download size |
| SAM3 / SAM 3.1 checkpoints | ☐ | ☐ | HF-gated |

Request on day 1 even though E7 does not run until week 4.

## Comparator verification debt

`SAMITE`, `HiM2SAM`, `SENTRY` and `AS-SAM2` are currently known to us **only through**
`arXiv:2512.22624` and `arXiv:2606.24449`. Before any of them enters the frozen comparator set in
`configs/preregistration.yaml`, verify directly:

| Candidate | Primary source read | Code released | Runs on our sequences | Added to frozen set |
|---|---|---|---|---|
| SAMITE | ☐ | ☐ | ☐ | ☐ |
| HiM2SAM | ☐ | ☐ | ☐ | ☐ |
| SENTRY | ☐ | ☐ | ☐ | ☐ |
| AS-SAM2 | ☐ | ☐ (code promised) | ☐ | ☐ |

A comparator that cannot actually be run is worse than one that was never named: the frozen set is
scored by its **minimum** partial correlation, so an unrunnable entry would either force an
amendment or silently weaken the claim.

## E0 gate

| Check | Status |
|---|---|
| SAM2.1 VOS pass reproduces published LVOS behaviour qualitatively | ☐ |
| `no_op` replay from `t_r` reproduces the original failure bit-for-bit across 5 repeats | ☐ |
| Bank copy is faithful (signature stable) | ☐ |
| Sham surgery at random non-failure times does **not** change tracking | ☐ |

Decision: ______  Date: ______
