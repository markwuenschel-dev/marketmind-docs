pysrc.meta.rg09_power_analysis
==============================

.. py:module:: pysrc.meta.rg09_power_analysis


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_power_analysis.PRODUCER_VERSION
   pysrc.meta.rg09_power_analysis.SCHEMA_VERSION
   pysrc.meta.rg09_power_analysis.MANIFEST_SCHEMA_VERSION
   pysrc.meta.rg09_power_analysis.ARTIFACT_CLASS
   pysrc.meta.rg09_power_analysis.EPISODE_SCENARIOS
   pysrc.meta.rg09_power_analysis.INSTRUMENT_SCENARIOS
   pysrc.meta.rg09_power_analysis.TARGET_POWER_LEVELS
   pysrc.meta.rg09_power_analysis.Z_95_ONE_SIDED
   pysrc.meta.rg09_power_analysis.MAX_EPISODE_TARGET_SEARCH
   pysrc.meta.rg09_power_analysis.MAX_REASONABLE_INSTRUMENTS
   pysrc.meta.rg09_power_analysis.DEFAULT_GATE_SPEC
   pysrc.meta.rg09_power_analysis.DEFAULT_BASELINE_CONFIG
   pysrc.meta.rg09_power_analysis.DEFAULT_FIXTURE_CONFIG
   pysrc.meta.rg09_power_analysis.DEFAULT_POWER_A_COMPARISON_DOC
   pysrc.meta.rg09_power_analysis.DEFAULT_MULTI_FIXTURE_MANIFEST
   pysrc.meta.rg09_power_analysis.REQUIRED_RUN_FILENAMES
   pysrc.meta.rg09_power_analysis.ALLOWED_RECOMMENDATIONS
   pysrc.meta.rg09_power_analysis.FAMILY_ORDER


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_power_analysis.RG09PowerAnalysisResult


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_power_analysis.run_rg09_power_analysis


Module Contents
---------------

.. py:data:: PRODUCER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MANIFEST_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ARTIFACT_CLASS
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: EPISODE_SCENARIOS
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:data:: INSTRUMENT_SCENARIOS
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:data:: TARGET_POWER_LEVELS
   :type:  Final[tuple[tuple[str, float], Ellipsis]]
   :value: Ellipsis


.. py:data:: Z_95_ONE_SIDED
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: MAX_EPISODE_TARGET_SEARCH
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: MAX_REASONABLE_INSTRUMENTS
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: DEFAULT_GATE_SPEC
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DEFAULT_BASELINE_CONFIG
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DEFAULT_FIXTURE_CONFIG
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DEFAULT_POWER_A_COMPARISON_DOC
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DEFAULT_MULTI_FIXTURE_MANIFEST
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REQUIRED_RUN_FILENAMES
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: ALLOWED_RECOMMENDATIONS
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: FAMILY_ORDER
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:class:: RG09PowerAnalysisResult

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: advisory_recommendation
      :type:  str
      :value: Ellipsis



.. py:function:: run_rg09_power_analysis(*, baseline_run_dir, comparison_run_dirs, output_dir, gate_spec_path = ..., baseline_config_path = ..., comparison_config_paths = ..., fixture_config_path = ..., power_comparison_doc_path = ..., multi_fixture_manifest_path = ...)

