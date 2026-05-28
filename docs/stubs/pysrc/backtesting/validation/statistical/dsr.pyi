from typing import Any

"""
Deflated Sharpe Ratio (DSR), Minimum Track Record Length (minTRL),
and block-bootstrap Sharpe confidence intervals.

References:
    Bailey & López de Prado (2014) "The Deflated Sharpe Ratio: Correcting
    for Selection Bias, Backtest Overfitting, and Non-Normality"
"""

LOG: Any
pl: Any
class DSRError(BaseError):
    ...
class DSRDataError(DSRError):
    ...
class DSRComputationError(DSRError):
    ...
def compute_dsr(returns: Any, n_trials: int = ..., periods_per_year: int = ..., benchmark_sr: float = ...) -> Dict[str, Any]: ...
def compute_min_trl(returns: Any, target_confidence: float = ..., benchmark_sr: float = ..., periods_per_year: int = ...) -> Dict[str, Any]: ...
def compute_bootstrap_ci(returns: Any, n_resamples: int = ..., block_size: Optional[int] = ..., periods_per_year: int = ..., ci_levels: tuple[float, ...] = ..., random_state: int = ...) -> Dict[str, Any]: ...
