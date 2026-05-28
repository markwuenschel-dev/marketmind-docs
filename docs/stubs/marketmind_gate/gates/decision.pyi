from typing import Any

"""
Decision artifact emission (gate_decision.json and promotion_event.json).

Per spec §13:
- gate_decision.json is always emitted
- promotion_event.json is emitted only on PASS in promote mode
- gate_decision_hash is computed excluding timestamp for determinism
"""

def build_gate_decision(result: str, gate_policy_hash: str, errors: list[GateError], artifact_refs: list[ArtifactRef]) -> dict[str, Any]: ...
def build_promotion_event(gate_policy_hash: str, gate_decision_hash: str, identity: dict[str, Any], transfer_report: dict[str, Any], artifact_refs: list[ArtifactRef]) -> dict[str, Any]: ...
def emit_gate_decision(bundle_dir: Path, decision: dict[str, Any]) -> Path: ...
def emit_promotion_event(bundle_dir: Path, event: dict[str, Any]) -> Path: ...
