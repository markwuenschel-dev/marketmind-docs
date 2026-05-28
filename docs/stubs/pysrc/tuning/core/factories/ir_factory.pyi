from typing import Any

"""
IRFactory: build IR objects from Spec objects.
"""

def build_ir_metadata(spec: TuningJobSpec) -> IRMetadata: ...
def build_search_ir(job_spec: TuningJobSpec, space_spec: SearchSpaceSpec) -> SearchIR: ...
