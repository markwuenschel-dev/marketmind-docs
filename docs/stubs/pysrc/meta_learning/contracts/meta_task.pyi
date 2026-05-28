from typing import Any

"""
MetaTask contract — canonical implementation is in :mod:`pysrc.meta_learning.task_generator` (MLN-01).
"""

class TaskGeneratorProtocol(Protocol):
    def build(self: Any, **kwargs: Any) -> MetaTask: ...
