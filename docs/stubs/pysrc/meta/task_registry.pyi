from typing import Any

"""
MLC-0 · Promotable append-only :class:`TaskRegistry`.

Canonical path resolution (MLC-0 Step 1)
----------------------------------------

``MetaLearningCore.md`` §5.5 specifies ``py/meta/task_registry.py``.  The
repo's Python root is ``pysrc/``; therefore the canonical in-repo path
is ``pysrc/meta/task_registry.py``.

Contract authority
------------------

Implements :class:`pysrc.meta_learning.contracts.task_registry.TaskRegistryProtocol`
(OI-22 stub).  The protocol is the authoritative interface surface; this
module is the promotable concrete implementation.

Semantics
---------

- **Append-only.**  Once a task is registered it cannot be mutated or
  removed.  Re-use of a ``(regime_id, t0)`` stable key raises
  :class:`TaskRegistryDuplicateError`.  Duplicate ``task_id`` values
  raise the same exception.
- **Durable backend.**  A :class:`DurableTaskStore` protocol lets the
  registry persist each appended task to disk.  The default in-repo
  backend is :class:`JsonLinesDurableStore` — a minimal JSON-Lines
  append-only writer sufficient to make the interface stable for
  downstream MLC-1..MLC-3.  In-memory registry behaviour is fully
  covered even when no durable backend is attached (``None`` ⇒
  in-memory-only, audited via log message on append).
- **Logging.**  Every successful append emits a structured log record
  via :mod:`pysrc.ops.mm_logkit` so that operators can tail registry
  activity without opaque silence.

Out of scope (per MLC-0 brief §7)
---------------------------------

- ``task_manifest.json`` emission.
- CAS-backed durable store with cross-run replay guarantees (MLC-6).
- Governed ``build_meta_task`` constructor (MLC-2).
"""

LOG: Any
class DurableTaskStore(Protocol):
    def persist(self: Any, task_id: str, record: dict[str, Any]) -> None: ...
    def iter_records(self: Any) -> Iterator[dict[str, Any]]: ...
class NullDurableStore:
    def persist(self: Any, task_id: str, record: dict[str, Any]) -> None: ...
    def iter_records(self: Any) -> Iterator[dict[str, Any]]: ...
class JsonLinesDurableStore:
    def __init__(self: Any, path: str | os.PathLike[str]) -> None: ...
    def path(self: Any) -> Path: ...
    def persist(self: Any, task_id: str, record: dict[str, Any]) -> None: ...
    def iter_records(self: Any) -> Iterator[dict[str, Any]]: ...
class TaskRegistry(TaskRegistryProtocol):
    CONTRACT_VERSION: ClassVar[str] = ...
    def __init__(self: Any, durable_store: DurableTaskStore | None = ...) -> None: ...
    def append(self: Any, task: MetaTask) -> None: ...
    def get(self: Any, task_id: str) -> MetaTask: ...
    def get_by_stable(self: Any, *, regime_id: str, t0: str) -> MetaTask: ...
    def contains_stable(self: Any, *, regime_id: str, t0: str) -> bool: ...
    def query(self: Any, regime_id: str | None = ..., since: str | None = ...) -> list[MetaTask]: ...
    def iter_stable_keys(self: Any) -> Iterable[tuple[str, str]]: ...
    def durable_store(self: Any) -> DurableTaskStore: ...
