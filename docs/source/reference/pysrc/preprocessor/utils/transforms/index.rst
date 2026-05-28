pysrc.preprocessor.utils.transforms
===================================

.. py:module:: pysrc.preprocessor.utils.transforms


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.transforms.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.transforms.Transform
   pysrc.preprocessor.utils.transforms.CompositeTransform
   pysrc.preprocessor.utils.transforms.NormalizeTransform
   pysrc.preprocessor.utils.transforms.BollingerTransform
   pysrc.preprocessor.utils.transforms.LogTransform
   pysrc.preprocessor.utils.transforms.MinMaxScaleTransform
   pysrc.preprocessor.utils.transforms.ToTorchTransform
   pysrc.preprocessor.utils.transforms.TransformFactory


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.transforms.profile_transform
   pysrc.preprocessor.utils.transforms.feature_engineer_chain


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: Transform(fn, backend = ...)

   Bases: :py:obj:`ABC`


   .. py:method:: apply(df)


   .. py:method:: validate(df)


.. py:class:: CompositeTransform(fn, backend = ...)

   Bases: :py:obj:`Transform`


   .. py:method:: validate(df)


.. py:function:: profile_transform(func)

.. py:class:: NormalizeTransform(col, mean = ..., std = ...)

   Bases: :py:obj:`Transform`


   .. py:method:: apply(df)


   .. py:method:: validate(df)


.. py:class:: BollingerTransform(col, window = ..., num_std = ..., output_cols = ...)

   Bases: :py:obj:`Transform`


   .. py:method:: apply(df)


   .. py:method:: validate(df)


.. py:class:: LogTransform(col, base = ..., eps = ...)

   Bases: :py:obj:`Transform`


   .. py:method:: apply(df)


   .. py:method:: validate(df)


.. py:class:: MinMaxScaleTransform(col, min_val = ..., max_val = ..., eps = ...)

   Bases: :py:obj:`Transform`


   .. py:method:: apply(df)


   .. py:method:: validate(df)


.. py:class:: ToTorchTransform(cols, dtypes = ..., include_lengths = ...)

   Bases: :py:obj:`Transform`


   .. py:method:: validate(df)


.. py:class:: TransformFactory

   .. py:method:: register(name, builder)


   .. py:method:: build(name, **kwargs)


   .. py:method:: compose(*names, **kwargs)


   .. py:method:: auto_register_from_exprs()


.. py:function:: feature_engineer_chain(cols)

