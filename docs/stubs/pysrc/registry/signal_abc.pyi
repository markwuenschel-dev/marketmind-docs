from typing import Any

"""
MLC-0 · Signal ABC with ``signal_embedding`` field.

Canonical path resolution (MLC-0 Step 1)
----------------------------------------

``MetaLearningCore.md`` §5.5 specifies ``py/registry/signal_abc.py``.
The in-repo Python root is ``pysrc/``; canonical path is therefore
``pysrc/registry/signal_abc.py``.

What this module adds
---------------------

Introduces :class:`SignalABC`, an abstract base class that formalizes
the in-repo signal interface and declares the
``signal_embedding: Optional[np.ndarray] = None`` field required by the
MLC-0 brief.

Relation to the existing :class:`pysrc.registry.signal_catalog.SignalProtocol`
is intentionally loose: the Protocol remains the structural type used by
:class:`pysrc.registry.signal_catalog.SignalCatalog` for registration,
and :class:`SignalABC` is the nominal base for implementers that want
explicit ABC inheritance.  :class:`SignalABC` is a ``SignalProtocol`` by
construction (it defines the same attributes), so both paths remain
compatible.

Phase II MLC-1 will populate ``signal_embedding`` once
``context_encoder.py`` is online.  Until then the field must remain
``None`` on every concrete signal.
"""

class SignalABC(ABC):
    signal_embedding: Optional[NDArray[np.floating[Any]]] = ...
    def slot_index(self: Any) -> int: ...
