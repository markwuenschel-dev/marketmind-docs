from typing import Any

"""
Typed point-in-time boundary errors.
"""

class PITError(ValueError):
    ...
class PITBoundaryError(PITError):
    ...
class PITLeakageError(PITError):
    ...
