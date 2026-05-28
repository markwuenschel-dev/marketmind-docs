from typing import Any

"""
Warm-start utilities: inject prior experiment results into the search state.
"""

def inject_prior_trials(ir: SearchIR, prior_trials: tuple[Trial, ...]) -> SearchIR: ...
