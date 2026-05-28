from typing import Any

"""
URI resolution for artifact loading.

Supported URI schemes (v1):
- Relative paths (resolved from bundle_dir)
- Absolute file paths
- file:// URIs

S3/GCS/HTTP is deferred to v2 per spec §6.3.
"""

def resolve_uri(uri: str, bundle_dir: Path) -> bytes: ...
def resolve_uri_to_path(uri: str, bundle_dir: Path) -> Path: ...
