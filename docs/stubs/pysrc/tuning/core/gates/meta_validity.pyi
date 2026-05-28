from typing import Any

"""
Meta-validity gate: check candidate consistency with meta-learning priors.
"""

def passes_meta_gate(candidate_score: float, memory: ExperimentMemory, space_hash: str, percentile: float = ...) -> bool: ...
