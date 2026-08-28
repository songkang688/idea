"""Linear probe interface. Does not ship pretrained weights or fake scores."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ProbeSpec:
    encoder_name: str
    frozen: bool = True
    note: str = "User plugs torch encoder; this repo does not invent accuracies."
