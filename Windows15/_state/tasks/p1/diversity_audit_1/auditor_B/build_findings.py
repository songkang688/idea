#!/usr/bin/env python3
"""Auditor B (P1 diversity audit 1): build findings.json from ideas_master.jsonl.

Read-only on ideas_master.jsonl; writes only into auditor_B/.
All idea_id lists are validated against the master before writing.
"""
import json
from collections import Counter

MASTER = "Windows15/_state/ideas_master.jsonl"
OUT = "Windows15/_state/tasks/p1/diversity_audit_1/auditor_B/findings.json"
JB = "Windows15/_state/tasks/p1/batch_001/judge_B/verdict.jsonl"

with open(MASTER) as f:
    master = {json.loads(l)["idea_id"]: json.loads(l) for l in f if l.strip()}
assert len(master) == 271

with open(JB) as f:
    jb = {json.loads(l)["idea_id"]: json.loads(l) for l in f if l.strip()}
jb_flagged_surviving = sorted(i for i, r in jb.items() if r["permutation_flag"] and i in master)

P = "W15-B001-"

tier1 = [
    (P + "A-100", "router_assembly",
     "Nearest-centroid LoRA routing over frozen features. Standard embedding-gating engineering; the premise (domain linear separability) is assumed true and the deliverable is a deployment assembly, not a finding."),
    (P + "A-052", "known_method_transplant",
     "k-center / core-set active learning applied verbatim to SAM-LoRA. 'Coverage selection beats random' is the original core-set claim; no segmentation-specific mechanism is load-bearing."),
    (P + "A-084", "known_method_transplant",
     "Self-consistency test-time adaptation (TENT/MEMO family) bolted onto SAM. The only scientific content (inconsistency localizes errors) is explicitly borrowed from A-009."),
    (P + "C-028", "module_a_plus_b",
     "Motion-sparsity router dispatching to specialist media models. Module A+B assembly; the two-sided motion signature is asserted, and the deliverable is the router."),
    (P + "A-056", "workflow_assembly",
     "SAM-proposes / human-verifies annotation workflow. Cost-efficiency workflow permutation; its falsifiable core (error incoherence unlearnable at low rank) already lives in A-053."),
    (P + "A-060", "known_method_transplant",
     "Query-by-committee active learning with SAM's multimask heads as the committee. The AL race is the deliverable; the informational claim belongs to the A-061/A-089 family."),
]

tier1_5 = [
    (P + "B-097", "training_recipe_permutation",
     "Agreement-ordered curriculum for multi-organ training. The 'transferable boundary policy' mechanism is under-specified and hard to isolate from generic curriculum effects; as written the payoff is a curriculum recipe."),
    (P + "A-096", "known_method_transplant",
     "Label-free adaptation via inter-slice consistency training. Self-supervised-consistency family applied to SAM+CT; the 'beats 10-20-image supervised LoRA' benchmark race is the load-bearing claim."),
    (P + "B-098", "training_recipe_permutation",
     "Gradient-surgery (PCGrad/CAGrad family) for multi-organ interference. The directional-conflict diagnostic is real science; the headline payoff 'conflict-aware update surgery outperforms any reweighting' is a method permutation."),
    (P + "C-087", "pretraining_swap",
     "Matting-vs-segmentation pretraining swap. Comparative objective permutation whose inductive-bias attribution is confounded by corpus content unless the binarized-label control is made primary."),
    (P + "A-064", "component_permutation",
     "Adapt-the-uncertainty-pathway-only. A value-proposition permutation over which component to retrain; needs decomposition into measurable calibration-transfer claims before Stage 2."),
]

auditor_additions = [
    (P + "B-012", "training_recipe_permutation",
     "Per-structure early stopping. Staged-learning (interior-early / boundary-noise-late) hypothesis is genuine; the vehicle is a stopping-schedule recipe."),
    (P + "B-037", "architecture_swap",
     "Native-grid anisotropy-aware operators vs resample-then-segment. Information-destruction hypothesis is genuine; the vehicle is an operator swap."),
    (P + "B-047", "architecture_swap",
     "Per-site label heads vs pooled training. Label-shift-masquerading-as-image-shift is a real finding; the vehicle is a multi-head architecture permutation."),
    (P + "C-003", "head_swap",
     "Matting-style head on a mask-trained backbone. The probing claim (internal soft-density estimate survives until the binarizing head) is genuine; the vehicle is a head swap."),
    (P + "C-075", "output_space_permutation",
     "Nested iso-density level-set output head. Held-out-strictness generalization is a real prediction; the vehicle is an output-head redesign."),
    (P + "C-076", "known_method_transplant",
     "Distribution-over-masks modeling (Probabilistic-U-Net family) for ambiguous boundaries. Established method family; the residual novelty is the likelihood-based evaluation reranking claim."),
]

template_families = {
    "adapt_only_component": {
        "skeleton": "domain gap lives in {component}; tuning only {component} matches LoRA",
        "idea_ids": [P + s for s in
                     ["A-008", "A-015", "A-016", "A-032", "A-064", "A-081", "A-082", "A-083"]],
    },
    "frozen_signal_as_free_sensor": {
        "skeleton": "{frozen-model byproduct signal} is a free {sensor/label/detector} for {quantity}",
        "idea_ids": [P + s for s in
                     ["A-009", "A-050", "A-061", "A-062", "A-066", "A-067",
                      "C-011", "C-030", "C-031", "C-034", "C-057", "C-060", "C-062", "C-063"]],
    },
    "metric_audit_reranking": {
        "skeleton": "metric/benchmark artifact X hides Y; re-evaluation flips published rankings",
        "idea_ids": [P + s for s in
                     ["A-068", "A-069", "A-070", "A-071", "A-073", "A-074", "A-075",
                      "B-013", "B-015", "B-016", "B-017", "B-018", "B-020", "B-021", "B-022", "B-023",
                      "C-039", "C-041", "C-044", "C-045", "C-046", "C-047", "C-048"]],
    },
    "annotator_artifact_inheritance": {
        "skeleton": "models learn the annotator/protocol artifact, not the anatomy/medium",
        "idea_ids": [P + s for s in
                     ["A-036", "A-039", "A-041",
                      "B-002", "B-003", "B-004", "B-008", "B-010", "B-011", "B-073",
                      "C-001", "C-004", "C-015", "C-016"]],
    },
}

# Validate every referenced idea exists in the master.
for lst in (tier1, tier1_5, auditor_additions):
    for iid, _, _ in lst:
        assert iid in master, iid
for fam in template_families.values():
    for iid in fam["idea_ids"]:
        assert iid in master, iid

tier1_ids = [i for i, _, _ in tier1]
tier1_5_ids = [i for i, _, _ in tier1_5]
addition_ids = [i for i, _, _ in auditor_additions]
assert not set(addition_ids) & set(jb_flagged_surviving)

surface_ids = sorted(set(jb_flagged_surviving) | set(addition_ids))
assert set(tier1_ids) <= set(surface_ids) and set(tier1_5_ids) <= set(surface_ids)

n = len(master)
mut_gate = sorted(i for i, r in master.items() if r.get("mutation_required"))
assert set(mut_gate) == set(tier1_ids)

territory_counts = Counter(r["territory"] for r in master.values())
t01_peft_orbit_clusters = ["peft_mechanism", "counterintuitive_peft", "capability_erosion",
                           "data_efficiency", "peft_lifecycle"]
t01_orbit = sum(1 for r in master.values()
                if r["territory"].startswith("T01") and r["cluster"] in t01_peft_orbit_clusters)

findings = {
    "task_id": "p1_diversity_audit_1_B",
    "auditor": "auditor_B",
    "audit_focus": "SAM+X / LoRA+X / loss+X / architecture-permutation pseudo-innovation",
    "windows_path": "Windows15",
    "input": {
        "file": "Windows15/_state/ideas_master.jsonl",
        "branch": "origin/cursor/p1-wave-b-batch001-consolidator-7c96",
        "head_sha": "b8d60bce42ab0a9f0f7b35278454d65d59f01331",
        "ideas_reviewed": n,
    },
    "method": (
        "Independent full-text re-read of all 271 accepted ideas (title + core_hypothesis). "
        "Three-tier grading: tier1 = permutation archetype dominates and the stated hypothesis is thin, "
        "borrowed, or lives in another idea (must be rewritten before Stage-2 promotion); "
        "tier1_5 = archetype-forward, a genuine diagnostic exists but the permutation payoff is still the "
        "load-bearing claim (re-center before Stage 2); tier2_surface = any idea whose vehicle is a "
        "method/recipe/component permutation even when a genuine falsifiable hypothesis rides it (kept; "
        "tracked for portfolio balance). Cross-checked post-hoc against judge_B's in-batch "
        "permutation_flag rubric for calibration; tier assignments were made independently."
    ),
    "fraction_estimates": {
        "tier1_archetype_dominant": {
            "count": len(tier1_ids), "fraction": round(len(tier1_ids) / n, 4),
            "note": "All 6 already carry mutation_required from batch_001 consolidation; the gate held. None should be promoted as written."
        },
        "tier1_plus_tier1_5": {
            "count": len(tier1_ids) + len(tier1_5_ids),
            "fraction": round((len(tier1_ids) + len(tier1_5_ids)) / n, 4),
            "note": "Adds 5 archetype-forward ideas judge_B flag-kept where the permutation payoff (not the diagnostic) is still the headline claim."
        },
        "tier2_full_permutation_surface": {
            "count": len(surface_ids), "fraction": round(len(surface_ids) / n, 4),
            "note": "37 surviving judge_B permutation flags plus 6 auditor-B additions (B-012, B-037, B-047, C-003, C-075, C-076). Most are redeemed by a real hypothesis; tracked for balance, not for removal."
        },
        "clean_of_archetype": {
            "count": n - len(surface_ids), "fraction": round((n - len(surface_ids)) / n, 4),
            "note": "The corpus is unusually hypothesis-first; naked SAM+X/LoRA+X/loss+X pseudo-innovation is rare."
        },
    },
    "worst_offenders_ranked": [
        {"rank": k + 1, "idea_id": iid, "archetype": arch, "tier": tier, "rationale": why}
        for k, (tier, (iid, arch, why)) in enumerate(
            [("tier1", t) for t in tier1] + [("tier1_5", t) for t in tier1_5])
    ],
    "auditor_additions_to_permutation_surface": [
        {"idea_id": iid, "archetype": arch, "tier": "tier2_surface", "rationale": why}
        for iid, arch, why in auditor_additions
    ],
    "judge_B_cross_check": {
        "in_batch_flags": 40,
        "flags_surviving_into_master": len(jb_flagged_surviving),
        "flags_removed_as_duplicates": ["W15-B001-A-063", "W15-B001-A-093", "W15-B001-C-078"],
        "mutation_required_in_master": mut_gate,
        "agreement": "Auditor B independently converged on the same 6 mutation-required ideas as archetype-dominant and confirms judge_B's flag-but-keep calls, with 5 upgrades to tier1_5 and 6 additions to the surface list.",
        "surviving_flag_ids": jb_flagged_surviving,
    },
    "template_families_diversity_risk": {
        "note": (
            "Not pseudo-innovation (each instance has genuine content), but four claim skeletons are "
            "heavily repeated; at the 1000+ -> 200 Stage-2 cut these families should compete internally, "
            "not each send every member forward."
        ),
        "families": {
            name: {"skeleton": fam["skeleton"], "count": len(fam["idea_ids"]),
                   "idea_ids": fam["idea_ids"]}
            for name, fam in template_families.items()
        },
    },
    "territory_balance": {
        "counts": dict(territory_counts),
        "note": (
            f"Territory-level balance is fine (93/89/89). The imbalance is method-orbit concentration inside T01: "
            f"{t01_orbit}/93 T01 ideas orbit LoRA/PEFT mechanics (clusters: {', '.join(t01_peft_orbit_clusters)})."
        ),
    },
    "underweighted_territories_and_axes": [
        {"axis": "Language/text-prompted and VLM-grounded segmentation",
         "current_coverage": "~2 ideas (B-086, C-032)",
         "suggestion": "Proceed with planned T05; require mechanism-level claims about grounding, not CLIP+SAM assemblies."},
        {"axis": "Video / temporal / streaming segmentation outside smoke (memory architectures, temporal consistency science)",
         "current_coverage": "T03 temporal_dynamics only (7 ideas, all media-specific)",
         "suggestion": "Add a video-segmentation territory or sub-quota; SAM-2-style memory behavior is untouched."},
        {"axis": "Security, adversarial robustness, spoofing",
         "current_coverage": "1 idea (C-099)",
         "suggestion": "Explicit sub-quota in T06 failure mining."},
        {"axis": "Efficiency, distillation, compute/data scaling laws",
         "current_coverage": "~2 ideas (A-091; A-079 tangentially)",
         "suggestion": "Underweighted relative to the field; scaling-law-style measurement ideas fit the corpus's metrology strength."},
        {"axis": "Continual / lifelong deployment (adapter lifecycle, sequential domains)",
         "current_coverage": "3 ideas (peft_lifecycle)",
         "suggestion": "Thin for a deployment-relevant axis; extend beyond LoRA bookkeeping."},
        {"axis": "Fairness / equity / population bias",
         "current_coverage": "2 ideas (B-079, B-091; B-049 tangentially)",
         "suggestion": "Medical territory especially warrants demographic-stratification hypotheses."},
        {"axis": "Theory: identifiability, sample complexity, formal limits",
         "current_coverage": "3 ideas, all T03 physics-identifiability (C-019, C-020, C-027)",
         "suggestion": "No formal-analysis ideas exist in T01/T02; invite information-theoretic or PAC-style claims."},
        {"axis": "Interactive segmentation / human factors outside the medical territory",
         "current_coverage": "T02 human_ai_interaction (7); T01 has only A-005/A-029 touching interaction",
         "suggestion": "Interaction science generalizes; port the T02 question style to T01/T03."},
        {"axis": "Instance/panoptic/amodal problem formulation outside media",
         "current_coverage": "C-046, A-033 only",
         "suggestion": "Formulation-level ontology questions proved fertile in T03; apply to solid-object territories."},
    ],
    "recommendations_for_generators": [
        "Add a negative-control requirement to the generation contract: each idea must state the control or dissociation that separates its mechanism claim from 'the new combination just works better'.",
        "Cap per-batch instances of a single claim skeleton (suggest max 5) at generation time; the four families listed here reached 8-23 instances each.",
        "For any idea whose minimal experiment is 'method A vs method B on benchmark C', require the predicted mechanism signature that would distinguish the win from generic capacity/tuning effects (per A-068's own finding).",
        "Enforce the existing mutation_required gate: the 6 tier1 ideas must be reformulated per judge_B salvage notes before Stage-2 promotion; tier1_5 ideas should have their diagnostic promoted to the headline claim at the same checkpoint.",
    ],
    "canonical_files_modified": [],
    "created_at": "2026-08-28T19:55:00Z",
}

with open(OUT, "w") as f:
    json.dump(findings, f, indent=2)
    f.write("\n")
print("wrote", OUT)
print("tier1", len(tier1_ids), "tier1_5", len(tier1_5_ids), "surface", len(surface_ids))
