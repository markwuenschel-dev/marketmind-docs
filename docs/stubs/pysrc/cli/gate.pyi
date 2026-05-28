from typing import Any

"""
Gate CLI for validating run bundles per Appendix D contract (v5.1).

Normative gate-oriented delivery intent: Programming Guidelines §6.2 (capabilities must
expose measurable evidence for promotion).

This module implements the Gate CLI that validates run bundles against
the specifications in Appendix C (bundle structure) and Appendix D 
(gate contract) of the MarketMind Implementation Plan v5.1.

Usage (per Appendix D.1):
    marketmind-gate check --bundle /path/to/run_bundle_v1 --output /path/to/gate_result.json
    
    # Also supports shorthand:
    python -m pysrc.cli.gate check ./run_bundle_001/
    python -m pysrc.cli.gate validate ./run_bundle_001/

Exit Codes (per Appendix D.1):
    0 = all gates PASS
    1 = one or more gates FAIL (validation failures)
    2 = invalid input (missing bundle, malformed JSON, unknown schema version)
    3 = internal error (unexpected exception)

Output:
    gate_result.json written to --output path (or bundle/gate_result.json by default)
    Human logs go to stderr; machine-readable output is gate_result.json
"""

GATE_SCHEMA_VERSION: Any
GATE_CLI_VERSION: Any
class ExitCode(Enum):
    PASS: Any
    FAIL: Any
    INVALID_INPUT: Any
    INTERNAL_ERROR: Any
class GateResult(Enum):
    PASS: Any
    FAIL: Any
class ReasonCode(Enum):
    VALID: Any
    UNKNOWN_SCHEMA_VERSION: Any
    MISSING_SCHEMA_VERSION: Any
    INVALID_SCHEMA_VERSION: Any
    MISSING_FILE: Any
    MALFORMED_JSON: Any
    INVALID_STRUCTURE: Any
    MISSING_PLAN_HASH: Any
    HASH_MISMATCH: Any
    MISSING_REQUIRED_FIELD: Any
    INVALID_SPLITS: Any
    LEAKAGE_DETECTED: Any
    PURGE_VIOLATION: Any
    EMBARGO_VIOLATION: Any
    INVALID_CONFIG: Any
    STAT_VALIDITY_INVALID_STRUCTURE: Any
    STAT_VALIDITY_GATE_FAIL: Any
    COST_ASSUMPTION_MISSING: Any
    COST_GATE_REJECTED: Any
    ZERO_COST_ASSUMED: Any
    EXECUTION_ASSUMPTIONS_INVALID_STRUCTURE: Any
    PIT_NON_COMPLIANT: Any
    MISSING_KNOWLEDGE_TIME_COLUMN: Any
    CONTENT_HASH_MISMATCH: Any
    STALE_DOWNLOAD_WARNING: Any
    INVALID_DETERMINISM_TIER: Any
    INVALID_REPRODUCIBILITY_METADATA: Any
INVALID_INPUT_REASON_CODES: Any
class GateCheck:
    gate_id: str = ...
    result: str = ...
    reason_code: str = ...
    message: str = ...
    evidence: dict[str, Any] = ...
    def to_dict(self: Any) -> dict[str, Any]: ...
class GateReport:
    schema_version: str = ...
    bundle_path: str = ...
    timestamp: str = ...
    overall_result: str = ...
    gates: list[dict[str, Any]] = ...
    metadata: dict[str, Any] = ...
    def add_check(self: Any, check: GateCheck) -> None: ...
    def to_dict(self: Any) -> dict[str, Any]: ...
    def to_json(self: Any, path: Path) -> None: ...
def resolve_gate_output_path(output_path: Optional[Path], bundle_path: Path) -> Path: ...
def write_gate_report(report: GateReport, output_path: Optional[Path], bundle_path: Path) -> Path: ...
def emit_gate_failure_report(bundle_path: Path, *, gate_id: str, reason_code: str, message: str, evidence: Optional[dict[str, Any]] = ..., output_path: Optional[Path] = ...) -> GateReport: ...
REQUIRED_BUNDLE_FILES: Any
OPTIONAL_BUNDLE_FILES: Any
PLAN_REQUIRED_FIELDS: Any
ENV_REQUIRED_FIELDS: Any
DATASET_REQUIRED_FIELDS: Any
PREPROCESSING_REQUIRED_FIELDS: Any
SPLITS_REQUIRED_FIELDS: Any
def validate_bundle_exists(bundle_path: Path, report: GateReport) -> bool: ...
def validate_required_files(bundle_path: Path, report: GateReport) -> dict[str, bool]: ...
def validate_plan_identity(bundle_path: Path, report: GateReport, expected_plan_hash: Optional[str] = ...) -> bool: ...
def validate_env_fingerprint(bundle_path: Path, report: GateReport) -> bool: ...
def validate_dataset_manifest(bundle_path: Path, report: GateReport) -> bool: ...
class DataLineageGate:
    def __init__(self: Any, *, max_download_age_days: int = ...) -> None: ...
    def validate(self: Any, bundle_path: Path, report: GateReport) -> bool: ...
DATA_LINEAGE_GATE: Any
def validate_preprocessing_report(bundle_path: Path, report: GateReport) -> bool: ...
def validate_splits_manifest(bundle_path: Path, report: GateReport) -> bool: ...
def validate_leakage_invariants(bundle_path: Path, report: GateReport) -> bool: ...
def validate_splits_integrity(bundle_path: Path, report: GateReport) -> bool: ...
STAT_VALIDITY_REQUIRED_KEYS: Any
STAT_VALIDITY_GATE_VALUES: Any
STAT_VALIDITY_STRUCTURED_SECTIONS: Any
def validate_stat_validity_report(bundle_path: Path, report: GateReport) -> None: ...
EXECUTION_ASSUMPTIONS_REQUIRED_KEYS: Any
EXECUTION_ASSUMPTIONS_COST_KEYS: Any
def validate_execution_assumptions(bundle_path: Path, report: GateReport) -> None: ...
def validate_bundle(bundle_path: Path, output_path: Optional[Path] = ..., expected_plan_hash: Optional[str] = ...) -> tuple[GateReport, ExitCode]: ...
def main(argv: list[str] | None = ...) -> int: ...
