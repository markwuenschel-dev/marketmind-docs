from typing import Any

"""
Assembles stat_validity_report.json from DSR, minTRL, bootstrap CI,
and validator-supplied PBO output. Wires into gate.py via the public
run_validity_report() function.

Output schema (Appendix H, v1):
{
    "schema_version": "v1",
    "sharpe_ratio": 1.23,
    "dsr": {"value": 0.87, "p_value": 0.02, "n_trials": 5},
    "min_trl": {"years_needed": 2.1, "years_available": 5.0},
    "bootstrap_ci": {
        "lower_95": 0.41, "upper_95": 2.05,
        "lower_99": 0.12, "upper_99": 2.34,
        "n_resamples": 10000
    },
    "pbo": {"value": 0.22, "gate_result": "PASS"},
    "gate_result": "PASS"   # PASS | WARN | FAIL
}
"""

LOG: Any
def run_validity_report(returns: Any, *, n_trials: int = ..., periods_per_year: int = ..., benchmark_sr: float = ..., n_resamples: int = ..., block_size: Optional[int] = ..., random_state: int = ..., output_path: Optional[Union[str, pathlib.Path]] = ..., pbo_result: Mapping[str, Any] | None = ...) -> Dict[str, Any]: ...
