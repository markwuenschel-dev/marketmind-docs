pysrc.ops.hashing.equality
==========================

.. py:module:: pysrc.ops.hashing.equality


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.equality.EqualityEvidence


Functions
---------

.. autoapisummary::

   pysrc.ops.hashing.equality.requires_equality_fallback
   pysrc.ops.hashing.equality.assert_ref_compatibility
   pysrc.ops.hashing.equality.verify_payload_equality
   pysrc.ops.hashing.equality.verify_aux_check
   pysrc.ops.hashing.equality.verify_cache_hit
   pysrc.ops.hashing.equality.validate_evidence_policy


Module Contents
---------------

.. py:class:: EqualityEvidence

   .. py:attribute:: payload_bytes
      :type:  bytes | None
      :value: Ellipsis



   .. py:attribute:: aux_check
      :type:  bytes | None
      :value: Ellipsis



   .. py:attribute:: payload_length
      :type:  int | None
      :value: Ellipsis



.. py:function:: requires_equality_fallback(purpose)

.. py:function:: assert_ref_compatibility(stored_ref, observed_ref)

.. py:function:: verify_payload_equality(stored_payload, observed_payload)

.. py:function:: verify_aux_check(stored_aux_check, observed_aux_check)

.. py:function:: verify_cache_hit(*, purpose, stored_ref, observed_ref, stored_evidence = ..., observed_evidence = ...)

.. py:function:: validate_evidence_policy(purpose, persistence_tier, evidence)

