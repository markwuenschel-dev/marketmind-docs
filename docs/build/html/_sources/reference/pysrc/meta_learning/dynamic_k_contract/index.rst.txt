pysrc.meta_learning.dynamic_k_contract
======================================

.. py:module:: pysrc.meta_learning.dynamic_k_contract


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.dynamic_k_contract.MAX_SIGNALS
   pysrc.meta_learning.dynamic_k_contract.EMPTY_SLOT_ID
   pysrc.meta_learning.dynamic_k_contract.CONTRACT_VERSION


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.dynamic_k_contract.validate_signal_set_version
   pysrc.meta_learning.dynamic_k_contract.validate_signal_slots
   pysrc.meta_learning.dynamic_k_contract.build_fixed_slot_mask
   pysrc.meta_learning.dynamic_k_contract.build_fixed_slot_surface_from_sparse_slots
   pysrc.meta_learning.dynamic_k_contract.validate_active_k_vs_mask
   pysrc.meta_learning.dynamic_k_contract.validate_fixed_slot_task_surface


Module Contents
---------------

.. py:data:: MAX_SIGNALS
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: EMPTY_SLOT_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CONTRACT_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:function:: validate_signal_set_version(value)

.. py:function:: validate_signal_slots(*, slot_indices, max_signals = ...)

.. py:function:: build_fixed_slot_mask(*, max_signals = ...)

.. py:function:: build_fixed_slot_surface_from_sparse_slots(slot_to_signal_id, *, max_signals = ...)

.. py:function:: validate_active_k_vs_mask(*, signal_mask, active_k)

.. py:function:: validate_fixed_slot_task_surface(*, signal_ids, signal_mask, active_k = ..., max_signals = ...)

