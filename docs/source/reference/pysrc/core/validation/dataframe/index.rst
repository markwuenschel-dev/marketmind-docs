pysrc.core.validation.dataframe
===============================

.. py:module:: pysrc.core.validation.dataframe


Attributes
----------

.. autoapisummary::

   pysrc.core.validation.dataframe.F
   pysrc.core.validation.dataframe.torch
   pysrc.core.validation.dataframe.pl
   pysrc.core.validation.dataframe.dd
   pysrc.core.validation.dataframe.cudf
   pysrc.core.validation.dataframe.cp
   pysrc.core.validation.dataframe.NS
   pysrc.core.validation.dataframe.ValidatorCallable


Classes
-------

.. autoapisummary::

   pysrc.core.validation.dataframe.SeriesLike
   pysrc.core.validation.dataframe.DataFrameLike
   pysrc.core.validation.dataframe.TensorLike
   pysrc.core.validation.dataframe.Validator
   pysrc.core.validation.dataframe.CustomSeriesValidator


Functions
---------

.. autoapisummary::

   pysrc.core.validation.dataframe.validate_dataframe
   pysrc.core.validation.dataframe.lazy_validate_ohlcv
   pysrc.core.validation.dataframe.ensure_numeric
   pysrc.core.validation.dataframe.register_validator
   pysrc.core.validation.dataframe.compose_validators
   pysrc.core.validation.dataframe.all_of
   pysrc.core.validation.dataframe.any_of
   pysrc.core.validation.dataframe.validate_series
   pysrc.core.validation.dataframe.validate_ohlcv
   pysrc.core.validation.dataframe.validate_stream_chunk
   pysrc.core.validation.dataframe.validate_data_for_training
   pysrc.core.validation.dataframe.validate_symbol
   pysrc.core.validation.dataframe.validate_date
   pysrc.core.validation.dataframe.validate_tensor
   pysrc.core.validation.dataframe.validate_file_data


Module Contents
---------------

.. py:data:: F
   :type:  Any

.. py:data:: torch
   :type:  Any
   :value: Ellipsis


.. py:data:: pl
   :type:  Any
   :value: Ellipsis


.. py:data:: dd
   :type:  Any
   :value: Ellipsis


.. py:data:: cudf
   :type:  Any
   :value: Ellipsis


.. py:data:: cp
   :type:  Any
   :value: Ellipsis


.. py:data:: NS
   :type:  Any

.. py:function:: validate_dataframe(df, *, required_cols = ..., allow_lazy = ...)

.. py:function:: lazy_validate_ohlcv(df)

.. py:function:: ensure_numeric(df, cols)

.. py:class:: SeriesLike

   Bases: :py:obj:`Protocol`


   .. py:method:: is_empty()


   .. py:method:: null_count()


   .. py:method:: len()


.. py:class:: DataFrameLike

   Bases: :py:obj:`Protocol`


   .. py:method:: is_empty()


   .. py:method:: columns()


   .. py:method:: schema()


.. py:class:: TensorLike

   Bases: :py:obj:`Protocol`


   .. py:method:: ndim()


   .. py:method:: numel()


   .. py:method:: is_floating_point()


   .. py:method:: is_complex()


   .. py:method:: isnan()


   .. py:method:: isinf()


   .. py:method:: any()


.. py:class:: Validator

   Bases: :py:obj:`ABC`


   .. py:method:: validate(data)


.. py:function:: register_validator(data_type)

.. py:data:: ValidatorCallable
   :type:  Any

.. py:function:: compose_validators(*validators)

.. py:function:: all_of(validators)

.. py:function:: any_of(validators)

.. py:function:: validate_series(series, name = ...)

.. py:function:: validate_ohlcv(df)

.. py:function:: validate_stream_chunk(chunk)

.. py:function:: validate_data_for_training(df)

.. py:function:: validate_symbol(symbol)

.. py:function:: validate_date(date)

.. py:function:: validate_tensor(tensor, *, ndim = ..., min_dims = ..., name = ...)

.. py:class:: CustomSeriesValidator(min_length = ...)

   Bases: :py:obj:`Validator`


   .. py:method:: validate(data)


.. py:function:: validate_file_data(data, format)

