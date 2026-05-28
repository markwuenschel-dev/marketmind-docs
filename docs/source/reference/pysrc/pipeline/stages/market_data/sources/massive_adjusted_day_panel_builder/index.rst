pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder
============================================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.DEFAULT_RAW_ROOT
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.DEFAULT_CORPORATE_ACTIONS_ROOT
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.DEFAULT_OUTPUT_ROOT
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.MANIFEST_SCHEMA_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.BUILDER_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.SOURCE_ID
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.LOG


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.AdjustedPanelBuildError


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.AdjustedPanelBuildConfig
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.AdjustedPanelFileResult


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.build_adjusted_daily_panels
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.write_manifest
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.parse_args
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.configure_logging
   pysrc.pipeline.stages.market_data.sources.massive_adjusted_day_panel_builder.main


Module Contents
---------------

.. py:data:: DEFAULT_RAW_ROOT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: DEFAULT_CORPORATE_ACTIONS_ROOT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: DEFAULT_OUTPUT_ROOT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: MANIFEST_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: BUILDER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SOURCE_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: LOG
   :type:  Any

.. py:class:: AdjustedPanelBuildConfig

   .. py:attribute:: start_date
      :type:  date
      :value: Ellipsis



   .. py:attribute:: end_date
      :type:  date
      :value: Ellipsis



   .. py:attribute:: raw_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: corporate_actions_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: output_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: splits_path
      :type:  Path | None
      :value: Ellipsis



   .. py:attribute:: dividends_path
      :type:  Path | None
      :value: Ellipsis



   .. py:attribute:: overwrite
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: verbose
      :type:  bool
      :value: Ellipsis



.. py:class:: AdjustedPanelFileResult

   .. py:attribute:: trade_date
      :type:  str
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



.. py:exception:: AdjustedPanelBuildError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: build_adjusted_daily_panels(config)

.. py:function:: write_manifest(config, results)

.. py:function:: parse_args(argv)

.. py:function:: configure_logging(verbose)

.. py:function:: main(argv)

