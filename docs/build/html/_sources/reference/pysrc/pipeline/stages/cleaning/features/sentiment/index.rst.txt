pysrc.pipeline.stages.cleaning.features.sentiment
=================================================

.. py:module:: pysrc.pipeline.stages.cleaning.features.sentiment


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.features.sentiment.SentimentParams
   pysrc.pipeline.stages.cleaning.features.sentiment.VaderSentimentParams
   pysrc.pipeline.stages.cleaning.features.sentiment.VaderSentimentStep
   pysrc.pipeline.stages.cleaning.features.sentiment.FinbertSentimentParams
   pysrc.pipeline.stages.cleaning.features.sentiment.FinbertSentimentStep


Module Contents
---------------

.. py:class:: SentimentParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: provider_key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: output_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: text_column
      :type:  str
      :value: Ellipsis



.. py:class:: VaderSentimentParams

   Bases: :py:obj:`SentimentParams`


   .. py:attribute:: provider_key
      :type:  str
      :value: Ellipsis



.. py:class:: VaderSentimentStep

   Bases: :py:obj:`_ProviderSentimentStep`


.. py:class:: FinbertSentimentParams

   Bases: :py:obj:`SentimentParams`


   .. py:attribute:: provider_key
      :type:  str
      :value: Ellipsis



.. py:class:: FinbertSentimentStep

   Bases: :py:obj:`_ProviderSentimentStep`


