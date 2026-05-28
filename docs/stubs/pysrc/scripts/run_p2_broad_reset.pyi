from typing import Any

"""
Master entry point for the full P2 broad-reset pipeline.

Usage (default — requires W4-A supervision artifact on disk):
    python scripts/run_p2_broad_reset.py

Usage (smoke / CI):
    python scripts/run_p2_broad_reset.py --smoke-test

Usage (override supervision path):
    python scripts/run_p2_broad_reset.py --data-path \
        artifacts/phase_ii/w4_a_router_opportunity/datasets/w3b_ta/surface_b/router_supervision_rows.parquet
"""

def main() -> int: ...
