from typing import Any

class MechanicalValidator:
    def validate(self: Any, result: Any, ctx: dict[str, Any], store: Any) -> ValidationReport: ...
