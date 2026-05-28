pysrc.pipeline.stages.market_data.sources
=========================================

.. py:module:: pysrc.pipeline.stages.market_data.sources


Submodules
----------

.. toctree::
   :maxdepth: 1

   /reference/pysrc/pipeline/stages/market_data/sources/alpha_vantage/index
   /reference/pysrc/pipeline/stages/market_data/sources/alternative/index
   /reference/pysrc/pipeline/stages/market_data/sources/alternative_data/index
   /reference/pysrc/pipeline/stages/market_data/sources/base/index
   /reference/pysrc/pipeline/stages/market_data/sources/coingecko/index
   /reference/pysrc/pipeline/stages/market_data/sources/contracts/index
   /reference/pysrc/pipeline/stages/market_data/sources/data_loader/index
   /reference/pysrc/pipeline/stages/market_data/sources/file/index
   /reference/pysrc/pipeline/stages/market_data/sources/fred/index
   /reference/pysrc/pipeline/stages/market_data/sources/fundamental_data/index
   /reference/pysrc/pipeline/stages/market_data/sources/ibkr/index
   /reference/pysrc/pipeline/stages/market_data/sources/influxdb/index
   /reference/pysrc/pipeline/stages/market_data/sources/market_data/index
   /reference/pysrc/pipeline/stages/market_data/sources/massive_adjusted_day_panel_builder/index
   /reference/pysrc/pipeline/stages/market_data/sources/massive_corporate_actions_loader/index
   /reference/pysrc/pipeline/stages/market_data/sources/massive_day_aggs_loader/index
   /reference/pysrc/pipeline/stages/market_data/sources/quandl/index
   /reference/pysrc/pipeline/stages/market_data/sources/runtime/index
   /reference/pysrc/pipeline/stages/market_data/sources/yahoo_fetcher/index


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.DataSource


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.register_source
   pysrc.pipeline.stages.market_data.sources.get_registry


Package Contents
----------------

.. py:function:: register_source(name)

.. py:function:: get_registry()

.. py:class:: DataSource

   .. py:method:: get_historical(*args, **kwargs)
      :async:



