from typing import Any

"""
MLN-05 frozen inference boundary — single source of truth for live vs training parameter roles.

Companion suite / Resolution Ledger normative lock: **live inference** uses a **frozen**
``theta_day_prime`` checkpoint only; **no gradients** and **no intraday mutation** of that object on
the live path. **theta_meta** is nightly meta-initialization; **theta_task_prime** is ephemeral,
training-only inner-loop state and must **not** be promoted to serving.

**What is live:** only a **gate-passed**, **promoted** ``theta_day_prime`` artifact reference.

**What stays offline-only:** gradient computation, ``theta_task_prime`` materialization, and
``theta_meta`` updates occur only on training / nightly paths — never on live execution.

**Closure:** MLN-05 is operationally enforceable where call sites use these helpers. A full program
closure still requires wiring every allocator/trainer entrypoint; this module is the canonical
contract those surfaces must import.
"""

CONTRACT_VERSION: Final[str] = ...
class ParameterRole(str, Enum):
    THETA_META: Any
    THETA_TASK_PRIME: Any
    THETA_DAY_PRIME: Any
class ExecutionPath(str, Enum):
    LIVE_INFERENCE: Any
    TRAINING: Any
class RolloutStage(str, Enum):
    SHADOW: Any
    CAPPED_BLEND: Any
    FULL_PROMOTION: Any
TrainingOutcome: Any
def rollout_stage_assumes_frozen_live_checkpoint(stage: RolloutStage | str) -> bool: ...
class ThetaDayPrimeCheckpointRef:
    checkpoint_id: str = ...
    artifact_role: ParameterRole = ...
def validate_parameter_roles(*, checkpoint_role: ParameterRole, expected: ParameterRole) -> None: ...
def validate_frozen_inference_request(*, execution_path: ExecutionPath, checkpoint_role: ParameterRole, allows_gradients: bool) -> None: ...
def assert_no_live_gradients(*, execution_path: ExecutionPath, allows_gradients: bool) -> None: ...
def ensure_training_only_task_prime(*, checkpoint_role: ParameterRole, execution_path: ExecutionPath) -> None: ...
def promote_theta_day_prime(*, current_live: ThetaDayPrimeCheckpointRef, candidate: ThetaDayPrimeCheckpointRef, gate_passed: bool, nightly_training_succeeded: bool) -> tuple[ThetaDayPrimeCheckpointRef, ThetaDayPrimeCheckpointRef | None]: ...
def rollback_theta_day_prime(*, current_live: ThetaDayPrimeCheckpointRef, rollback_target: ThetaDayPrimeCheckpointRef) -> ThetaDayPrimeCheckpointRef: ...
def build_inference_boundary_audit_block(*, previous_live_theta_day_prime_ref: str, live_theta_day_prime_ref: str, rollback_theta_day_prime_ref: str, theta_meta_ref: str | None, training_outcome: TrainingOutcome, rollout_stage: RolloutStage | str | None = ...) -> dict[str, Any]: ...
def validate_inference_boundary_audit_block(block: Mapping[str, Any]) -> None: ...
