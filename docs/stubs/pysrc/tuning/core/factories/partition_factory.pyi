from typing import Any

"""
PartitionFactory: build PartitionPlan from a TuningJobSpec + date range.
"""

def build_partition_plan(job_spec: TuningJobSpec, validation_spec: ValidationSpec, symbols: tuple[str, ...], start: datetime, end: datetime) -> PartitionPlan: ...
