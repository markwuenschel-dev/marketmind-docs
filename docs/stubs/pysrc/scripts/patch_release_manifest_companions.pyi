from typing import Any

"""
Fill ``companions`` in docs/releases/<version>.yml for validate-manifest and extract-suite.

Companion **lists** follow the same rules as ``devtools/docs/docmodel/extract.py``:
``CANONICAL_COMPANION_ORDER`` minus self (see ``test_companion_order_canonical_minus_self``).
Do not add FormattingSpec, WhitePaper, or charter/playbook doc_ids to title-page companion
lines — extract rejects those patterns.

Uses ruamel.yaml round-trip to preserve comments.
"""

def main(argv: list[str] | None = ...) -> int: ...
