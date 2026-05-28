pysrc.models.informer_model
===========================

.. py:module:: pysrc.models.informer_model


Classes
-------

.. autoapisummary::

   pysrc.models.informer_model.ProbSparseAttention
   pysrc.models.informer_model.InformerModel


Functions
---------

.. autoapisummary::

   pysrc.models.informer_model.build_informer


Module Contents
---------------

.. py:class:: ProbSparseAttention(d_model, n_heads)

   Bases: :py:obj:`tf.keras.layers.Layer`


   .. py:method:: call(inputs)


.. py:class:: InformerModel(input_dim, output_dim, seq_len, pred_len, d_model = ..., n_heads = ..., e_layers = ...)

   Bases: :py:obj:`tf.keras.Model`


   .. py:method:: call(inputs)


.. py:function:: build_informer(input_dim, output_dim, seq_len, pred_len)

