from typing import Any

"""
MarketMind application package ``py``.

This top-level name matches the on-disk layout (``py/pipeline``, ``py/cli``, …).
Pytest still imports the legacy PyPI ``py`` distribution for ``pysrc.path.local``;
we merge that library's ``path`` (and ``iniconfig`` if present) into this module
when the vendor package is installed (see dev dependency ``py`` in ``pyproject.toml``).
"""

...
