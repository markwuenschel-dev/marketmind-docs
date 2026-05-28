pysrc.pipeline.stages.market_data.corporate_actions
===================================================

.. py:module:: pysrc.pipeline.stages.market_data.corporate_actions


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.corporate_actions.RAW_PRICE_COLUMNS
   pysrc.pipeline.stages.market_data.corporate_actions.RAW_VOLUME_COLUMN
   pysrc.pipeline.stages.market_data.corporate_actions.ADJUSTED_RETURN_PRICE_COLUMN
   pysrc.pipeline.stages.market_data.corporate_actions.FORWARD_LABEL_PRICE_COLUMN
   pysrc.pipeline.stages.market_data.corporate_actions.FILTER_PRICE_COLUMN
   pysrc.pipeline.stages.market_data.corporate_actions.LIQUIDITY_VOLUME_COLUMN


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.corporate_actions.CorporateActionAdjustmentError


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.corporate_actions.CorporateActionAdjustmentConfig


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.corporate_actions.build_adjusted_ohlcv_panel


Module Contents
---------------

.. py:data:: RAW_PRICE_COLUMNS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: RAW_VOLUME_COLUMN
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ADJUSTED_RETURN_PRICE_COLUMN
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: FORWARD_LABEL_PRICE_COLUMN
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: FILTER_PRICE_COLUMN
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: LIQUIDITY_VOLUME_COLUMN
   :type:  Final[str]
   :value: Ellipsis


.. py:exception:: CorporateActionAdjustmentError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:class:: CorporateActionAdjustmentConfig

   .. py:attribute:: extreme_return_threshold
      :type:  float
      :value: Ellipsis



.. py:function:: build_adjusted_ohlcv_panel(bars, *, splits, dividends, config = ...)

