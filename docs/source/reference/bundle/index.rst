bundle
======

.. py:module:: bundle


Attributes
----------

.. autoapisummary::

   bundle.BUNDLE_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   bundle.PlanRecord
   bundle.EnvFingerprintRecord
   bundle.DatasetManifestRecord
   bundle.PreprocessingReportRecord
   bundle.SplitRecord
   bundle.SplitsManifestRecord
   bundle.RunBundle


Module Contents
---------------

.. py:data:: BUNDLE_SCHEMA_VERSION
   :type:  Any

.. py:class:: PlanRecord

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: plan_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: as_of_time
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: EnvFingerprintRecord

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: python_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: platform
      :type:  str
      :value: Ellipsis



   .. py:attribute:: git_sha
      :type:  str
      :value: Ellipsis



   .. py:attribute:: deps
      :type:  dict[str, str]
      :value: Ellipsis



.. py:class:: DatasetManifestRecord

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dataset_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: symbols
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: row_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: time_range
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:attribute:: pit_compliant
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: knowledge_time_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: content_hash
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: download_timestamp
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: content_hash_expected
      :type:  str | None
      :value: Ellipsis



.. py:class:: PreprocessingReportRecord

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: timings
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: warnings
      :type:  list[str]
      :value: Ellipsis



.. py:class:: SplitRecord

   .. py:attribute:: train_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: train_end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: test_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: test_end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold
      :type:  int
      :value: Ellipsis



.. py:class:: SplitsManifestRecord

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: split_method
      :type:  str
      :value: Ellipsis



   .. py:attribute:: purge_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: splits
      :type:  list[dict[str, Any]]
      :value: Ellipsis



.. py:class:: RunBundle

   .. py:attribute:: plan
      :type:  PlanRecord
      :value: Ellipsis



   .. py:attribute:: env_fingerprint
      :type:  EnvFingerprintRecord
      :value: Ellipsis



   .. py:attribute:: dataset_manifest
      :type:  DatasetManifestRecord
      :value: Ellipsis



   .. py:attribute:: preprocessing_report
      :type:  PreprocessingReportRecord
      :value: Ellipsis



   .. py:attribute:: splits_manifest
      :type:  SplitsManifestRecord
      :value: Ellipsis



