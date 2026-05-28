pysrc.meta_learning.context_encoder
===================================

.. py:module:: pysrc.meta_learning.context_encoder


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.context_encoder.REGIME_EMBEDDING_DIM
   pysrc.meta_learning.context_encoder.HIDDEN_DIM
   pysrc.meta_learning.context_encoder.NUM_REGIME_CLASSES
   pysrc.meta_learning.context_encoder.CONTEXT_ENCODER_DEFAULT_INPUT_DIM


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.context_encoder.ContextEncoderPretrainSummary
   pysrc.meta_learning.context_encoder.ContextEncoder


Module Contents
---------------

.. py:data:: REGIME_EMBEDDING_DIM
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: HIDDEN_DIM
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: NUM_REGIME_CLASSES
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: CONTEXT_ENCODER_DEFAULT_INPUT_DIM
   :type:  Final[int]
   :value: Ellipsis


.. py:class:: ContextEncoderPretrainSummary

   .. py:attribute:: initial_loss
      :type:  float
      :value: Ellipsis



   .. py:attribute:: final_loss
      :type:  float
      :value: Ellipsis



   .. py:attribute:: epochs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_examples
      :type:  int
      :value: Ellipsis



.. py:class:: ContextEncoder(input_dim = ..., *, seed = ..., device = ...)

   .. py:method:: input_dim()


   .. py:method:: is_frozen()


   .. py:method:: freeze()


   .. py:method:: unfreeze()


   .. py:method:: encode(input)


   .. py:method:: pretrain_classifier(examples, *, epochs = ..., lr = ..., batch_size = ..., seed = ...)


