from typing import Any

"""
WorkRouter: routes task IRs to the appropriate executor based on resource tags.
"""

class WorkRouter:
    def route(self: Any, task_id: str, resource_tags: dict[str, str]) -> str: ...
