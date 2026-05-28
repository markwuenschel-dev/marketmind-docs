pysrc.meta.allocator_benchmark.features
=======================================

.. py:module:: pysrc.meta.allocator_benchmark.features


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.features.INSTRUMENT_NUMERIC_FEATURES
   pysrc.meta.allocator_benchmark.features.INSTRUMENT_CATEGORICAL_FEATURES
   pysrc.meta.allocator_benchmark.features.SIGNAL_NUMERIC_FEATURES
   pysrc.meta.allocator_benchmark.features.SIGNAL_CATEGORICAL_FEATURES


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.features.build_instrument_feature_table
   pysrc.meta.allocator_benchmark.features.build_signal_feature_table
   pysrc.meta.allocator_benchmark.features.instrument_feature_numeric_columns
   pysrc.meta.allocator_benchmark.features.instrument_feature_categorical_columns
   pysrc.meta.allocator_benchmark.features.signal_feature_numeric_columns
   pysrc.meta.allocator_benchmark.features.signal_feature_categorical_columns


Module Contents
---------------

.. py:data:: INSTRUMENT_NUMERIC_FEATURES
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: INSTRUMENT_CATEGORICAL_FEATURES
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: SIGNAL_NUMERIC_FEATURES
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: SIGNAL_CATEGORICAL_FEATURES
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:function:: build_instrument_feature_table(signal_rows, config = ...)

.. py:function:: build_signal_feature_table(signal_rows)

.. py:function:: instrument_feature_numeric_columns()

.. py:function:: instrument_feature_categorical_columns()

.. py:function:: signal_feature_numeric_columns()

.. py:function:: signal_feature_categorical_columns()

