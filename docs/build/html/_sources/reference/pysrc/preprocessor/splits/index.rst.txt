pysrc.preprocessor.splits
=========================

.. py:module:: pysrc.preprocessor.splits


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.splits.SPLITS_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.splits.SplitBoundary
   pysrc.preprocessor.splits.SplitResult
   pysrc.preprocessor.splits.SplitsManifest
   pysrc.preprocessor.splits.TimeSeriesSplitter
   pysrc.preprocessor.splits.PurgedKFold


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.splits.validate_no_leakage
   pysrc.preprocessor.splits.create_splits_manifest


Module Contents
---------------

.. py:data:: SPLITS_SCHEMA_VERSION
   :type:  Any

.. py:class:: SplitBoundary

   .. py:attribute:: fold_id
      :type:  int
      :value: Ellipsis



   .. py:attribute:: train_start
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: train_end
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: test_start
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: test_end
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: train_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: test_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: purged_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargoed_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: non_contiguous_train
      :type:  bool
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:class:: SplitResult

   .. py:attribute:: train_df
      :type:  pl.DataFrame
      :value: Ellipsis



   .. py:attribute:: test_df
      :type:  pl.DataFrame
      :value: Ellipsis



   .. py:attribute:: boundary
      :type:  SplitBoundary
      :value: Ellipsis



   .. py:method:: train_indices()


   .. py:method:: test_indices()


   .. py:method:: assert_no_leakage(timestamp_col = ..., key_cols = ...)


.. py:class:: SplitsManifest

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: split_method
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_splits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: purge_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_train_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: test_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: total_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: time_range_start
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: time_range_end
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: splits
      :type:  list[dict]
      :value: Ellipsis



   .. py:attribute:: warnings
      :type:  list[str]
      :value: Ellipsis



   .. py:method:: to_dict()


   .. py:method:: to_json(path)


   .. py:method:: from_json(path)


.. py:class:: TimeSeriesSplitter(n_splits = ..., test_size = ..., min_train_size = ..., purge_window_days = ..., timestamp_col = ...)

   .. py:method:: split(df)


   .. py:method:: get_manifest(df)


.. py:class:: PurgedKFold(n_splits = ..., purge_window_days = ..., embargo_window_days = ..., timestamp_col = ...)

   .. py:method:: split(df)


.. py:function:: validate_no_leakage(train_df, test_df, timestamp_col = ..., purge_window_days = ..., embargo_window_days = ..., key_cols = ...)

.. py:function:: create_splits_manifest(df, splitter, output_path = ...)

