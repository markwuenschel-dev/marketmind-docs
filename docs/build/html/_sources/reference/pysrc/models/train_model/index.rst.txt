pysrc.models.train_model
========================

.. py:module:: pysrc.models.train_model


Classes
-------

.. autoapisummary::

   pysrc.models.train_model.TrainConfig
   pysrc.models.train_model.ModelTrainer


Module Contents
---------------

.. py:class:: TrainConfig

   .. py:attribute:: epochs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: batch_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: learning_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: early_stop_patience
      :type:  int
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



.. py:class:: ModelTrainer

   Bases: :py:obj:`ABC`


   .. py:method:: train(model, config, *, on_epoch = ...)


