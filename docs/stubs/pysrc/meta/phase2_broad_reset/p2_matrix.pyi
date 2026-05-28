from typing import Any

"""
P2-MATRIX: Generate candidate router specs from registries.

Reads P2-MAP surface_market_registry when present; does not train models.
"""

LOG: Any
W4B_FORBIDDEN_FEATURES: Any
DEFAULT_INPUT_SURFACE: Any
def load_model_registry(output_dir: Path) -> list[ModelFamilyEntry]: ...
def load_surface_registry(output_dir: Path) -> SurfaceMarketRegistry | None: ...
def resolve_matrix_input_surface(config: P2Config, output_dir: Path) -> tuple[str, str]: ...
def generate_candidate_matrix(config: P2Config | None = ..., output_dir: Path | None = ...) -> CandidateMatrix: ...
