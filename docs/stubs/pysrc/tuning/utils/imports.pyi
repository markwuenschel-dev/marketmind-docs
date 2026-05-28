from typing import Any

"""
Safe optional-import helper with actionable error messages.

Provides a single call site for guarded imports so missing extras surface clearly.
"""

def require_import(module: str, pip_name: str) -> types.ModuleType: ...
