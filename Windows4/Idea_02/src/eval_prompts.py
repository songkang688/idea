"""Prompt-type eval stub: records protocol, does not invent SAM Dice."""
from __future__ import annotations
import json

PROTOCOLS = ("box", "point", "negative", "multimask_diversity")

def empty_table():
    return {k: {"dice": None, "n": 0, "epistemic": "NOT_RUN"} for k in PROTOCOLS}

if __name__ == "__main__":
    print(json.dumps(empty_table(), indent=2))
