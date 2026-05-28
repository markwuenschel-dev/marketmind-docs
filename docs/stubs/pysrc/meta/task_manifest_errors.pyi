from typing import Any

"""
Typed errors for governed task-manifest emission.
"""

class TaskManifestError(ValueError):
    ...
class TaskManifestFieldError(TaskManifestError):
    ...
class TaskManifestHashError(TaskManifestError):
    ...
class TaskManifestIdentityError(TaskManifestError):
    ...
