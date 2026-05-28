pysrc.scripts.generate_rg09_fixture
===================================

.. py:module:: pysrc.scripts.generate_rg09_fixture


Attributes
----------

.. autoapisummary::

   pysrc.scripts.generate_rg09_fixture.LOG
   pysrc.scripts.generate_rg09_fixture.AMENDMENT
   pysrc.scripts.generate_rg09_fixture.FIXTURE_FILENAME_V1
   pysrc.scripts.generate_rg09_fixture.FIXTURE_FILENAME_V2
   pysrc.scripts.generate_rg09_fixture.SUMMARY_FILENAME
   pysrc.scripts.generate_rg09_fixture.METADATA_FILENAME
   pysrc.scripts.generate_rg09_fixture.FIXTURE_FILENAME
   pysrc.scripts.generate_rg09_fixture.SUMMARY_CLASS_ORDER
   pysrc.scripts.generate_rg09_fixture.CANONICAL_COLUMNS
   pysrc.scripts.generate_rg09_fixture.FIXTURE_COLUMNS
   pysrc.scripts.generate_rg09_fixture.REQUIRED_INPUT_COLUMNS
   pysrc.scripts.generate_rg09_fixture.FloatArray


Classes
-------

.. autoapisummary::

   pysrc.scripts.generate_rg09_fixture.MultiManifestSettings
   pysrc.scripts.generate_rg09_fixture.FixtureSegmentSpec
   pysrc.scripts.generate_rg09_fixture.MetaTaskSizingParams


Functions
---------

.. autoapisummary::

   pysrc.scripts.generate_rg09_fixture.load_bocpd_config
   pysrc.scripts.generate_rg09_fixture.stagger_multi_instrument_timestamps
   pysrc.scripts.generate_rg09_fixture.validate_rg09_fixture_fold_geometry
   pysrc.scripts.generate_rg09_fixture.load_multi_manifest
   pysrc.scripts.generate_rg09_fixture.generate_fixture
   pysrc.scripts.generate_rg09_fixture.generate_fixture_multi
   pysrc.scripts.generate_rg09_fixture.main


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: AMENDMENT
   :type:  Any

.. py:data:: FIXTURE_FILENAME_V1
   :type:  Any

.. py:data:: FIXTURE_FILENAME_V2
   :type:  Any

.. py:data:: SUMMARY_FILENAME
   :type:  Any

.. py:data:: METADATA_FILENAME
   :type:  Any

.. py:data:: FIXTURE_FILENAME
   :type:  Any

.. py:data:: SUMMARY_CLASS_ORDER
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: CANONICAL_COLUMNS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: FIXTURE_COLUMNS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: REQUIRED_INPUT_COLUMNS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: FloatArray
   :type:  Any

.. py:class:: MultiManifestSettings

   .. py:attribute:: uniform_calendar_day_index
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: calendar_overlap_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: apply_diversification_perturbation
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: temporal_folds
      :type:  int
      :value: Ellipsis



.. py:class:: FixtureSegmentSpec

   .. py:attribute:: entity_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: input_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: date_start
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: date_end
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: close_scale
      :type:  float
      :value: Ellipsis



.. py:class:: MetaTaskSizingParams

   .. py:attribute:: n_support
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_query
      :type:  int
      :value: Ellipsis



   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo
      :type:  int
      :value: Ellipsis



   .. py:method:: l_min()


.. py:function:: load_bocpd_config(path, *, repo_root)

.. py:function:: stagger_multi_instrument_timestamps(rows, *, entity_ids_sorted)

.. py:function:: validate_rg09_fixture_fold_geometry(fixture_frame, fold_construction, *, temporal_folds, min_entities_per_fold = ..., max_entity_share = ...)

.. py:function:: load_multi_manifest(path, *, repo_root)

.. py:function:: generate_fixture(*, input_path, config_path, output_dir, entity_id)

.. py:function:: generate_fixture_multi(*, segments, config_path, output_dir, source_dataset_id = ..., multi_settings = ...)

.. py:function:: main(input_path, config_path, output_dir, entity_id, multi_manifest_path)

