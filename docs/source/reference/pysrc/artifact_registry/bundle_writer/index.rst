pysrc.artifact_registry.bundle_writer
=====================================

.. py:module:: pysrc.artifact_registry.bundle_writer


Attributes
----------

.. autoapisummary::

   pysrc.artifact_registry.bundle_writer.BUNDLE_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   pysrc.artifact_registry.bundle_writer.BundleWriter


Module Contents
---------------

.. py:data:: BUNDLE_SCHEMA_VERSION
   :type:  Any

.. py:class:: BundleWriter(output_dir, *, cas = ..., run_registry = ..., run_id = ...)

   .. py:attribute:: SCHEMA_VERSION
      :type:  Any


   .. py:method:: write_plan(plan_hash, config_hash, as_of_time, config)


   .. py:method:: write_env_fingerprint()


   .. py:method:: write_dataset_manifest(dataset_id, symbols, row_count, time_range, *, pit_compliant = ..., knowledge_time_column = ..., content_hash = ..., download_timestamp = ..., content_hash_expected = ...)


   .. py:method:: write_preprocessing_report(steps, timings, warnings)


   .. py:method:: write_splits_manifest(splits, split_method, purge_window, embargo_window)


   .. py:method:: write_stat_validity_report(report)


   .. py:method:: write_screening_report(payload)


   .. py:method:: write_cleaning_plan(payload)


   .. py:method:: write_cleaning_report(payload)


   .. py:method:: missing_required()


   .. py:method:: compute_config_hash()


   .. py:method:: write_bundle_manifest()


   .. py:method:: read_plan()


   .. py:method:: read_env_fingerprint()


   .. py:method:: read_dataset_manifest()


   .. py:method:: read_preprocessing_report()


   .. py:method:: read_splits_manifest()


