pysrc.data.frames.dataframe_helpers
===================================

.. py:module:: pysrc.data.frames.dataframe_helpers


Attributes
----------

.. autoapisummary::

   pysrc.data.frames.dataframe_helpers.logger
   pysrc.data.frames.dataframe_helpers.metrics
   pysrc.data.frames.dataframe_helpers.tracing
   pysrc.data.frames.dataframe_helpers.pl
   pysrc.data.frames.dataframe_helpers.pd
   pysrc.data.frames.dataframe_helpers.ASYNC_RESOLVE_TIMEOUT
   pysrc.data.frames.dataframe_helpers.MAX_CONCAT_FRAMES
   pysrc.data.frames.dataframe_helpers.DATETIME_PARSE_STRICT
   pysrc.data.frames.dataframe_helpers.NORMALIZE_MAX_WORKERS
   pysrc.data.frames.dataframe_helpers.TO_POLARS_ALLOW_LOOSE_CONSTRUCT


Functions
---------

.. autoapisummary::

   pysrc.data.frames.dataframe_helpers.to_polars
   pysrc.data.frames.dataframe_helpers.ensure_datetime_col
   pysrc.data.frames.dataframe_helpers.infer_ticker_col
   pysrc.data.frames.dataframe_helpers.normalize_fetched


Module Contents
---------------

.. py:data:: logger
   :type:  BoundLogger
   :value: Ellipsis


.. py:data:: metrics
   :type:  Any

.. py:data:: tracing
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:data:: pd
   :type:  Any

.. py:data:: ASYNC_RESOLVE_TIMEOUT
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: MAX_CONCAT_FRAMES
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: DATETIME_PARSE_STRICT
   :type:  Final[bool]
   :value: Ellipsis


.. py:data:: NORMALIZE_MAX_WORKERS
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: TO_POLARS_ALLOW_LOOSE_CONSTRUCT
   :type:  Final[bool]
   :value: Ellipsis


.. py:function:: to_polars(df)

.. py:function:: ensure_datetime_col(df, date_col = ...)

.. py:function:: infer_ticker_col(df)

.. py:function:: normalize_fetched(obj)

