from typing import Any

"""
Promotable-path scaffold for `meta_validity_report.json` (Phase II-0B; non-promotable until MLN-06).

Phase II-0B scaffold emitters are **not** governed MLN-06 evidence. For the canonical fail-closed
triple (``task_manifest.json`` / ``meta_validity_report.json`` / ``execution_assumptions.json``)
with artifact identity, enforcement-derived PIT compliance, and **MLN-03** ``confidence_calibration``
/ECE surface, use ``pysrc.meta.phase2_artifact_contract.emit_phase2_artifacts`` only.

Field parity vs MLN-06 ``_validate_meta_minimum``: this scaffold carries the Phase II measurement
slots (including ``confidence_calibration`` via :func:`insufficient_confidence_calibration_block`)
with explicit ``unavailable`` / INSUFFICIENT semantics. It intentionally **does not** emit
``pit_boundary``, ``signal_ids_hash``, ``signal_surface``, or triple identity
(``run_id`` / ``artifact_version`` / ``timestamp``); those bind only on the governed emission path.

Research / empirical runs use ``meta_validity_report_research.json`` (separate schema); that lane
is not promotable and is not checked by :mod:`marketmind_gate.gates.meta_learner_scaffold`.
"""

SCHEMA_VERSION: Final[str] = ...
OVERALL_SCAFFOLD: Final[str] = ...
def build_meta_validity_report_document(*, run_identity: Phase2ScaffoldRunIdentity, register_path: Path | None = ...) -> dict[str, Any]: ...
def emit_meta_validity_report(output_path: Path, *, seed: int) -> dict[str, Any]: ...
