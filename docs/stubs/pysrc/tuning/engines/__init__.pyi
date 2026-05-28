from typing import Any

"""
Engine registration for the tuning subsystem.

Importing this package registers all four canonical engines with EngineRegistry
using their ``run`` functions directly.  Re-registration is safe because
``EngineRegistry.register()`` silently replaces existing entries, which
overrides the lazy-loader stubs that ``pysrc.tuning.registry`` installs at
module-initialisation time.

The four engines are:
- "grid"   — exhaustive Cartesian enumeration (no optional deps)
- "random" — uniform random sampling (no optional deps)
- "bayes"  — Gaussian-process Bayesian optimisation (requires scikit-optimize)
- "optuna" — TPE Bayesian optimisation (requires optuna)

Optional-dependency engines raise ``EngineNotAvailableError`` at *call time*
(not at import time) if their dependencies are missing, so importing this
package never fails due to missing skopt or optuna.
"""

...
