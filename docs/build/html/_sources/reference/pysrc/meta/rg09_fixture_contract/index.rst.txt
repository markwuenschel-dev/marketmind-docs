pysrc.meta.rg09_fixture_contract
================================

.. py:module:: pysrc.meta.rg09_fixture_contract


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_fixture_contract.CORRECTED_MULTI_INSTRUMENT_SCOPE
   pysrc.meta.rg09_fixture_contract.INDEPENDENT_INSTRUMENTS_POLICY
   pysrc.meta.rg09_fixture_contract.CALENDAR_TIME_METHOD
   pysrc.meta.rg09_fixture_contract.TRADING_DAY_ORDINAL_COLUMN


Exceptions
----------

.. autoapisummary::

   pysrc.meta.rg09_fixture_contract.RG09FixtureGeometryContractError


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_fixture_contract.RG09FoldTimeRange
   pysrc.meta.rg09_fixture_contract.RG09CorrectedFoldConstruction
   pysrc.meta.rg09_fixture_contract.RG09CorrectedFixtureGeometryContract
   pysrc.meta.rg09_fixture_contract.RG09MultiManifestGeometryPolicy


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_fixture_contract.is_governed_multi_instrument_summary
   pysrc.meta.rg09_fixture_contract.requires_corrected_geometry_contract
   pysrc.meta.rg09_fixture_contract.parse_corrected_fixture_geometry_contract
   pysrc.meta.rg09_fixture_contract.parse_multi_manifest_geometry_policy
   pysrc.meta.rg09_fixture_contract.validate_corrected_contract_matches_manifest


Module Contents
---------------

.. py:data:: CORRECTED_MULTI_INSTRUMENT_SCOPE
   :type:  Any

.. py:data:: INDEPENDENT_INSTRUMENTS_POLICY
   :type:  Any

.. py:data:: CALENDAR_TIME_METHOD
   :type:  Any

.. py:data:: TRADING_DAY_ORDINAL_COLUMN
   :type:  Any

.. py:exception:: RG09FixtureGeometryContractError(message, *, breaches)

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:class:: RG09FoldTimeRange

   .. py:attribute:: fold_id
      :type:  int
      :value: Ellipsis



   .. py:attribute:: date_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: date_end
      :type:  str
      :value: Ellipsis



   .. py:method:: to_pair()


.. py:class:: RG09CorrectedFoldConstruction

   .. py:attribute:: method
      :type:  str
      :value: Ellipsis



   .. py:attribute:: uniform_calendar_day_index
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: temporal_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: time_ranges
      :type:  tuple[RG09FoldTimeRange, Ellipsis]
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:class:: RG09CorrectedFixtureGeometryContract

   .. py:attribute:: fixture_scope
      :type:  str
      :value: Ellipsis



   .. py:attribute:: entity_ids
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: uniform_calendar_day_index
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: calendar_overlap_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold_construction
      :type:  RG09CorrectedFoldConstruction
      :value: Ellipsis



   .. py:method:: to_summary_fields()


.. py:class:: RG09MultiManifestGeometryPolicy

   .. py:attribute:: uniform_calendar_day_index
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: calendar_overlap_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: temporal_folds
      :type:  int
      :value: Ellipsis



.. py:function:: is_governed_multi_instrument_summary(summary)

.. py:function:: requires_corrected_geometry_contract(summary)

.. py:function:: parse_corrected_fixture_geometry_contract(summary, *, available_columns = ...)

.. py:function:: parse_multi_manifest_geometry_policy(manifest)

.. py:function:: validate_corrected_contract_matches_manifest(contract, manifest_policy)

