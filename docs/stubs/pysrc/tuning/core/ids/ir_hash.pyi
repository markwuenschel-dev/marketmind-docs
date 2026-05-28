from typing import Any

"""
Stable hash for IR objects; serialises to JSON via dataclasses.asdict.
"""

def hash_ir(ir: Any) -> str: ...
