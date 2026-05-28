from typing import Any

"""
Verify the frozen RG-09 reference anchor bundle.

The reference is intentionally a frozen strict-H3 artifact bundle, not the
Phase II allocator incumbent comparison baseline.
"""

JsonScalar: TypeAlias = ...
JsonValue: TypeAlias = ...
JsonObject: TypeAlias = ...
REPO_ROOT: Any
BUNDLE_PATH: Any
MANIFEST_PATH: Any
HASH_EXCLUDED_FILES: Any
REQUIRED_BUNDLE_FILES: Any
PINNED_MANIFEST_VALUES: JsonObject = ...
def main() -> int: ...
def compute_reference_hash(bundle_path: Path) -> str: ...
