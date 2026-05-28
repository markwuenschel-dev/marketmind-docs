from typing import Any

"""
Benchmark: measure SlotMask construction and active-index lookup throughput.
"""

def bench_slot_mask(total_slots: int = ..., k: int = ..., n_iterations: int = ...) -> dict[str, float]: ...
