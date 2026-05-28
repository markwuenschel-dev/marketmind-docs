pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader
==========================================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.MASSIVE_API_BASE
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.DEFAULT_OUTPUT_ROOT
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.LOADER_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.MANIFEST_SCHEMA_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.SOURCE_ID
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.ActionKind
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.LOG


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.CorporateActionsLoaderError
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.CorporateActionsCredentialsError
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.CorporateActionsFetchError


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.CorporateActionsConfig
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.CorporateActionsFileResult


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.normalize_split_records
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.normalize_dividend_records
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.fetch_corporate_actions
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.write_corporate_actions
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.write_manifest
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.run
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.parse_args
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.configure_logging
   pysrc.pipeline.stages.market_data.sources.massive_corporate_actions_loader.main


Module Contents
---------------

.. py:data:: MASSIVE_API_BASE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DEFAULT_OUTPUT_ROOT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: LOADER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MANIFEST_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SOURCE_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ActionKind
   :type:  Any

.. py:data:: LOG
   :type:  Any

.. py:exception:: CorporateActionsLoaderError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: CorporateActionsCredentialsError

   Bases: :py:obj:`CorporateActionsLoaderError`


   Common base class for all non-exit exceptions.


.. py:exception:: CorporateActionsFetchError

   Bases: :py:obj:`CorporateActionsLoaderError`


   Common base class for all non-exit exceptions.


.. py:class:: CorporateActionsConfig

   .. py:attribute:: start_date
      :type:  date
      :value: Ellipsis



   .. py:attribute:: end_date
      :type:  date
      :value: Ellipsis



   .. py:attribute:: output_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: actions
      :type:  tuple[ActionKind, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: tickers
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: api_key_env
      :type:  str
      :value: Ellipsis



   .. py:attribute:: limit
      :type:  int
      :value: Ellipsis



   .. py:attribute:: verbose
      :type:  bool
      :value: Ellipsis



.. py:class:: CorporateActionsFileResult

   .. py:attribute:: action
      :type:  ActionKind
      :value: Ellipsis



   .. py:attribute:: path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: content_blake2b
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  str
      :value: Ellipsis



   .. py:attribute:: duration_seconds
      :type:  float
      :value: Ellipsis



.. py:function:: normalize_split_records(records)

.. py:function:: normalize_dividend_records(records)

.. py:function:: fetch_corporate_actions(config)

.. py:function:: write_corporate_actions(config, frames)

.. py:function:: write_manifest(config, results)

.. py:function:: run(config)

.. py:function:: parse_args(argv)

.. py:function:: configure_logging(verbose)

.. py:function:: main(argv)

