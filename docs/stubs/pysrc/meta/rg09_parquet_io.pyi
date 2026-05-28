from typing import Any

"""
Parquet helpers for RG-09 fixtures.

Prefer ``fastparquet`` when importable so Windows/conda stacks with a broken
``pyarrow`` native DLL can still run the harness (set ``MARKETMIND_RG09_PARQUET_ENGINE``
to ``pyarrow`` or ``fastparquet`` explicitly).
"""

ParquetEngine: Any
def read_rg09_fixture_parquet(path: Path) -> pd.DataFrame: ...
def write_rg09_fixture_parquet(frame: pd.DataFrame, path: Path, *, index: bool = ...) -> None: ...
def write_rg09_fixture_parquet_bytes(frame: pd.DataFrame, *, index: bool = ...) -> bytes: ...
