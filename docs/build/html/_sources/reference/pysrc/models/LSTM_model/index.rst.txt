pysrc.models.LSTM_model
=======================

.. py:module:: pysrc.models.LSTM_model


Attributes
----------

.. autoapisummary::

   pysrc.models.LSTM_model.log


Classes
-------

.. autoapisummary::

   pysrc.models.LSTM_model.LSTMConfig
   pysrc.models.LSTM_model.BucketBatchSampler
   pysrc.models.LSTM_model.SharedDropout
   pysrc.models.LSTM_model.NormLSTMCell
   pysrc.models.LSTM_model.NormLSTM
   pysrc.models.LSTM_model.BidirectionalNormLSTM
   pysrc.models.LSTM_model.LSTMBlock
   pysrc.models.LSTM_model.Model


Functions
---------

.. autoapisummary::

   pysrc.models.LSTM_model.collate_fn


Module Contents
---------------

.. py:data:: log
   :type:  Any

.. py:class:: LSTMConfig

   .. py:attribute:: input_dim
      :type:  int
      :value: Ellipsis



   .. py:attribute:: units
      :type:  int
      :value: Ellipsis



   .. py:attribute:: num_layers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: zoneout_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: input_dropout_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: dropout
      :type:  float
      :value: Ellipsis



   .. py:attribute:: bidirectional
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: return_sequences
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: residual
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: pooling_type
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: use_custom_cell
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  Optional[int]
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:class:: BucketBatchSampler(dataset, batch_size, boundaries)

   Bases: :py:obj:`Sampler`\ [\ :py:obj:`List`\ [\ :py:obj:`int`\ ]\ ]


.. py:function:: collate_fn(batch)

.. py:class:: SharedDropout(p)

   Bases: :py:obj:`nn.Module`


   .. py:method:: train(mode = ...)


   .. py:method:: forward(x)


.. py:class:: NormLSTMCell(inp, hid, zoneout)

   Bases: :py:obj:`nn.Module`


   .. py:method:: forward(x, state)


.. py:class:: NormLSTM(inp, hid, zoneout, *, return_seq)

   Bases: :py:obj:`nn.Module`


   .. py:method:: forward(x, lengths = ...)


.. py:class:: BidirectionalNormLSTM(inp, hid, zoneout, *, return_seq)

   Bases: :py:obj:`nn.Module`


   .. py:method:: forward(x, lengths = ...)


.. py:class:: LSTMBlock(cfg)

   Bases: :py:obj:`nn.Module`


   .. py:method:: forward(x, lengths = ...)


   .. py:method:: get_config()


   .. py:method:: from_config(config)


.. py:class:: Model(cfg)

   Bases: :py:obj:`nn.Module`


   .. py:method:: forward(x, lengths = ...)


