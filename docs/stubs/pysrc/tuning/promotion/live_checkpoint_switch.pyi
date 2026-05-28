from typing import Any

"""
LiveCheckpointSwitch: atomically swap the active model checkpoint in the live system.
"""

def switch_live_checkpoint(job_id: str, from_artifact_hash: str, to_artifact_hash: str, context: dict[str, Any]) -> None: ...
