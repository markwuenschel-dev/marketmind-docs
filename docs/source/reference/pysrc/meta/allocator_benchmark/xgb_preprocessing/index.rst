pysrc.meta.allocator_benchmark.xgb_preprocessing
================================================

.. py:module:: pysrc.meta.allocator_benchmark.xgb_preprocessing


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.xgb_preprocessing.UNKNOWN_CATEGORY
   pysrc.meta.allocator_benchmark.xgb_preprocessing.UNKNOWN_CATEGORY_CODE
   pysrc.meta.allocator_benchmark.xgb_preprocessing.W2XGBPreprocessing


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.xgb_preprocessing.W2XGBPreprocessingState


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.xgb_preprocessing.fit_preprocessing_on_train
   pysrc.meta.allocator_benchmark.xgb_preprocessing.apply_preprocessing


Module Contents
---------------

.. py:data:: UNKNOWN_CATEGORY
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: UNKNOWN_CATEGORY_CODE
   :type:  Final[int]
   :value: Ellipsis


.. py:class:: W2XGBPreprocessingState

   .. py:attribute:: numeric_fill_values
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: categorical_vocabulary
      :type:  dict[str, dict[str, int]]
      :value: Ellipsis



   .. py:method:: categorical_index_maps()


.. py:data:: W2XGBPreprocessing
   :type:  Any

.. py:function:: fit_preprocessing_on_train(feature_table, numeric_columns, categorical_columns, split_column = ...)

.. py:function:: apply_preprocessing(feature_table, state, numeric_columns, categorical_columns)

