from typing import Any

"""
GateProtocol: interface for statistical promotion gates.
"""

class GateProtocol(Protocol):
    def evaluate(self: Any, candidate_id: str, scores: dict[str, float]) -> bool: ...
    def reason(self: Any, candidate_id: str, scores: dict[str, float]) -> str: ...
