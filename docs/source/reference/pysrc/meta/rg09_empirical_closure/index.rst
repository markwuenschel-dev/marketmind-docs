pysrc.meta.rg09_empirical_closure
=================================

.. py:module:: pysrc.meta.rg09_empirical_closure


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_empirical_closure.LOG
   pysrc.meta.rg09_empirical_closure.EMPIRICAL_PRODUCER_VERSION
   pysrc.meta.rg09_empirical_closure.META_VALIDITY_SCHEMA
   pysrc.meta.rg09_empirical_closure.TASK_MANIFEST_RESEARCH_SCHEMA
   pysrc.meta.rg09_empirical_closure.TASK_MANIFEST_RESEARCH_FILENAME
   pysrc.meta.rg09_empirical_closure.META_VALIDITY_RESEARCH_FILENAME
   pysrc.meta.rg09_empirical_closure.EMPIRICAL_WRAPPER_MANIFEST_FILENAME
   pysrc.meta.rg09_empirical_closure.BOCPD_REGIME_COLUMN
   pysrc.meta.rg09_empirical_closure.ALLOWED_SUCCESSOR_IDS
   pysrc.meta.rg09_empirical_closure.SUCCESSOR_BLOCK_ALLOWED_KEYS
   pysrc.meta.rg09_empirical_closure.DEFAULT_SUCCESSOR_HYPOTHESES


Exceptions
----------

.. autoapisummary::

   pysrc.meta.rg09_empirical_closure.RG09EmpiricalClosureError


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_empirical_closure.RG09EmpiricalClosureResult


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_empirical_closure.projection_rule_version_from_bundle_summary
   pysrc.meta.rg09_empirical_closure.load_run_config_overlay
   pysrc.meta.rg09_empirical_closure.validate_successor_hypotheses_overlay
   pysrc.meta.rg09_empirical_closure.run_rg09_empirical_closure


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: EMPIRICAL_PRODUCER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: META_VALIDITY_SCHEMA
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: TASK_MANIFEST_RESEARCH_SCHEMA
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: TASK_MANIFEST_RESEARCH_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: META_VALIDITY_RESEARCH_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: EMPIRICAL_WRAPPER_MANIFEST_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: BOCPD_REGIME_COLUMN
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALLOWED_SUCCESSOR_IDS
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: SUCCESSOR_BLOCK_ALLOWED_KEYS
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: DEFAULT_SUCCESSOR_HYPOTHESES
   :type:  Final[dict[str, Any]]
   :value: Ellipsis


.. py:function:: projection_rule_version_from_bundle_summary(summary)

.. py:class:: RG09EmpiricalClosureResult

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: base_decision
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: fail_closed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: fail_codes
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



.. py:exception:: RG09EmpiricalClosureError(message, *, fail_codes)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:function:: load_run_config_overlay(config_path)

.. py:function:: validate_successor_hypotheses_overlay(overlay)

.. py:function:: run_rg09_empirical_closure(*, fixture_path, fixture_summary_path, fixture_metadata_path, config_path, output_dir, boundary_recovery = ...)

