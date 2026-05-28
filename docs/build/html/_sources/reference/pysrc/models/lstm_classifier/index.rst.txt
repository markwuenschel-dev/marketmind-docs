pysrc.models.lstm_classifier
============================

.. py:module:: pysrc.models.lstm_classifier


Attributes
----------

.. autoapisummary::

   pysrc.models.lstm_classifier.log


Classes
-------

.. autoapisummary::

   pysrc.models.lstm_classifier.ClassifierConfig
   pysrc.models.lstm_classifier.LSTMClassifier


Module Contents
---------------

.. py:data:: log
   :type:  Any

.. py:class:: ClassifierConfig

   Bases: :py:obj:`LSTMConfig`


   .. py:attribute:: num_classes
      :type:  int
      :value: Ellipsis



   .. py:attribute:: projection_dim
      :type:  Optional[int]
      :value: Ellipsis



   .. py:attribute:: pooling_type
      :type:  Optional[str]
      :value: Ellipsis



   .. py:method:: from_marketmind(overrides = ...)


.. py:class:: LSTMClassifier(config = ...)

   Bases: :py:obj:`nn.Module`


   .. py:method:: num_parameters(trainable_only = ...)


   .. py:method:: forward(x, lengths = ...)


   .. py:method:: predict_proba(x, lengths = ...)


   .. py:method:: save(path)


   .. py:method:: from_pretrained(path, map_location = ...)


