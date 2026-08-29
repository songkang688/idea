#!/usr/bin/env python3
"""Assemble ideas.jsonl from cluster part files, validate, and render ideas.md.

Validation: JSON parse per line, unique sequential IDs, required fields present,
mutate_from references exist, near-duplicate one-liner check (token Jaccard).
"""
import json
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ["id", "one_liner", "problem", "core_hypothesis", "why_important",
            "why_possibly_novel", "minimal_experiment", "main_risk", "cluster"]

def main():
    ideas = []
    for path in sorted(glob.glob(os.path.join(HERE, "parts", "c*.jsonl"))):
        with open(path) as f:
            for ln, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    sys.exit(f"JSON error {path}:{ln}: {e}")
                for field in REQUIRED:
                    if field not in obj or not obj[field]:
                        sys.exit(f"Missing field '{field}' in {path}:{ln} ({obj.get('id')})")
                ideas.append(obj)

    ids = [i["id"] for i in ideas]
    assert len(ids) == len(set(ids)), "duplicate ids"
    expected = [f"W2-A-{n:04d}" for n in range(1, len(ideas) + 1)]
    assert ids == expected, f"ids not sequential: first mismatch {next((a, b) for a, b in zip(ids, expected) if a != b)}"
    id_set = set(ids)
    for i in ideas:
        mf = i.get("mutate_from")
        if mf is not None:
            assert mf in id_set, f"{i['id']} mutate_from missing parent {mf}"
            assert mf < i["id"], f"{i['id']} mutate_from must reference earlier id"

    # near-duplicate one-liner check (token Jaccard > 0.65 flagged)
    def toks(s):
        return set(w.lower().strip(".,:;()'\"") for w in s.split() if len(w) > 3)
    flagged = []
    tk = [toks(i["one_liner"]) for i in ideas]
    for a in range(len(ideas)):
        for b in range(a + 1, len(ideas)):
            inter = len(tk[a] & tk[b])
            union = len(tk[a] | tk[b]) or 1
            if inter / union > 0.65:
                flagged.append((ids[a], ids[b], round(inter / union, 2)))
    if flagged:
        print("NEAR-DUP FLAGS:")
        for f in flagged:
            print("  ", f)

    with open(os.path.join(HERE, "ideas.jsonl"), "w") as f:
        for i in ideas:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")

    clusters = {}
    for i in ideas:
        clusters.setdefault(i["cluster"], []).append(i)

    with open(os.path.join(HERE, "ideas.md"), "w") as f:
        f.write("# Windows2 Stage 1 - Agent A Idea Catalog (SAM / segmentation science)\n\n")
        f.write(f"Total ideas: **{len(ideas)}**. Fields per idea: problem, falsifiable core hypothesis, ")
        f.write("importance, novelty status, minimal (cheapest) experiment, main risk, cluster, optional parent.\n\n")
        f.write("Epistemic labels used inside entries: **KNOWN** (established prior work I am confident exists), ")
        f.write("**HYPOTHESIS** (falsifiable claim proposed here), **SPECULATION** (weaker conjecture), ")
        f.write("**UNVERIFIED - needs lit search** (novelty not yet checked against literature; no citation invented).\n\n")
        f.write("## Table of contents\n\n")
        for c in sorted(clusters):
            f.write(f"- [{c}](#{c.lower()}) ({len(clusters[c])} ideas: {clusters[c][0]['id']}..{clusters[c][-1]['id']})\n")
        f.write("\n---\n\n")
        for c in sorted(clusters):
            f.write(f"## {c}\n\n")
            for i in clusters[c]:
                f.write(f"### {i['id']} - {i['one_liner']}\n\n")
                f.write(f"- **Problem:** {i['problem']}\n")
                f.write(f"- **Core hypothesis (falsifiable):** {i['core_hypothesis']}\n")
                f.write(f"- **Why important:** {i['why_important']}\n")
                f.write(f"- **Why possibly novel:** {i['why_possibly_novel']}\n")
                f.write(f"- **Minimal experiment:** {i['minimal_experiment']}\n")
                f.write(f"- **Main risk:** {i['main_risk']}\n")
                if i.get("mutate_from"):
                    f.write(f"- **Mutated from:** {i['mutate_from']}\n")
                f.write("\n")
    print(f"OK: {len(ideas)} ideas, {len(clusters)} clusters")
    for c in sorted(clusters):
        print(f"  {c}: {len(clusters[c])}")

if __name__ == "__main__":
    main()
