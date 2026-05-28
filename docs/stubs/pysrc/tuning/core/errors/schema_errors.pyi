from typing import Any

"""
Typed schema validation errors for config and IR objects.
"""

class SchemaError(ValueError):
    ...
class ConfigSchemaError(SchemaError):
    ...
class IRSchemaError(SchemaError):
    ...
