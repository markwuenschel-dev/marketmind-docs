from typing import Any

"""
Canonical OTel telemetry surface for MarketMind.

Uses the default no-op tracer when no exporter is configured.
Exporter configuration is operator responsibility at runtime.
Do not import opentelemetry-sdk in production code.
"""

SPAN_DATAVIEW_AS_OF: Any
SPAN_OP_EXECUTE: Any
SPAN_GATE_EVALUATE: Any
SPAN_BUNDLE_PROMOTE: Any
SPAN_ATTR_UNKNOWN: Any
tracer: Any
