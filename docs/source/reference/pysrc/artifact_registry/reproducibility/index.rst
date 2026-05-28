pysrc.artifact_registry.reproducibility
=======================================

.. py:module:: pysrc.artifact_registry.reproducibility


Attributes
----------

.. autoapisummary::

   pysrc.artifact_registry.reproducibility.DETERMINISM_TIER_VALUES


Functions
---------

.. autoapisummary::

   pysrc.artifact_registry.reproducibility.validate_plan_reproducibility_fields
   pysrc.artifact_registry.reproducibility.collect_bundle_reproducibility_echo
   pysrc.artifact_registry.reproducibility.json_artifact_lineage_fields


Module Contents
---------------

.. py:data:: DETERMINISM_TIER_VALUES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:function:: validate_plan_reproducibility_fields(plan)

.. py:function:: collect_bundle_reproducibility_echo(bundle_path)

.. py:function:: json_artifact_lineage_fields(*, cas_id, attest_id = ..., schema_version = ..., determinism_tier = ...)

