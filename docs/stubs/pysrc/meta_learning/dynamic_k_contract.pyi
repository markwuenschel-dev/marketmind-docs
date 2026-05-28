from typing import Any

"""
MLN-04 Dynamic-K fixed-slot masking contract — single source of truth for Phase II signal surfaces.

Meta-learning paths use a **fixed 64-slot** signal vector. Active signals occupy catalog-assigned
slots; inactive slots are masked. Governed code must not use variable-width heads or silent slot
reuse.

``signal_set_version`` (string) increments whenever the active signal set changes; it must appear on
MetaTask-era artifacts and replay surfaces so membership revisions remain comparable.

**Slot identity (today)** — Integer ``slot_index`` is assigned only by :class:`pysrc.registry.signal_catalog.SignalCatalog`
at registration (monotonic, idempotent for the same ``spec_hash``, immutable thereafter). A governed
MetaTask carries a length-64 ``signal_ids`` / ``signal_mask``: index ``i`` is the catalog slot (or
empty string with mask False when inactive).

**``signal_set_version``** — Opaque string label for the active signal-set revision; any change to
which signals are admitted to the set must bump it so replay and gating can bind to the correct
historical membership.

**Closure** — This module is the single semantic source for Dynamic-K validation. MLN-04 is
*enforceable* for paths that construct tasks via :func:`pysrc.meta_learning.task_generator.build_meta_task`,
emit MLN-06 triples via :mod:`pysrc.meta.phase2_artifact_contract`, and register signals through
:class:`~pysrc.registry.signal_catalog.SignalCatalog`. A full program “MLN-04 closed” claim still
requires an audit that no remaining governed shortcut builds variable-width signal tensors without
going through these surfaces (out of scope for this change set).
"""

MAX_SIGNALS: Final[int] = ...
EMPTY_SLOT_ID: Final[str] = ...
CONTRACT_VERSION: Final[str] = ...
def validate_signal_set_version(value: str | None) -> str: ...
def validate_signal_slots(*, slot_indices: Sequence[int], max_signals: int = ...) -> None: ...
def build_fixed_slot_mask(*, max_signals: int = ...) -> tuple[tuple[str, ...], tuple[bool, ...]]: ...
def build_fixed_slot_surface_from_sparse_slots(slot_to_signal_id: Mapping[int, str], *, max_signals: int = ...) -> tuple[tuple[str, ...], tuple[bool, ...]]: ...
def validate_active_k_vs_mask(*, signal_mask: Sequence[bool], active_k: int) -> None: ...
def validate_fixed_slot_task_surface(*, signal_ids: tuple[str, ...], signal_mask: tuple[bool, ...], active_k: int | None = ..., max_signals: int = ...) -> None: ...
