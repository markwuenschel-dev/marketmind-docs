pysrc.meta.task_generator
=========================

.. py:module:: pysrc.meta.task_generator


Attributes
----------

.. autoapisummary::

   pysrc.meta.task_generator.LOG
   pysrc.meta.task_generator.Frequency


Classes
-------

.. autoapisummary::

   pysrc.meta.task_generator.DataViewLike
   pysrc.meta.task_generator.EpisodeConstructionError
   pysrc.meta.task_generator.TaskGeneratorConfig


Functions
---------

.. autoapisummary::

   pysrc.meta.task_generator.build_meta_task


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: Frequency
   :type:  Any

.. py:class:: DataViewLike

   Bases: :py:obj:`Protocol`


   .. py:method:: as_of(symbols, fields, knowledge_date)


.. py:class:: EpisodeConstructionError

   Bases: :py:obj:`DataPreconditionError`


.. py:class:: TaskGeneratorConfig

   .. py:attribute:: episode_timestamps
      :type:  Sequence[datetime | date | str | pd.Timestamp]
      :value: Ellipsis



   .. py:attribute:: symbols
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: fields
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: n_support
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_query
      :type:  int
      :value: Ellipsis



   .. py:attribute:: purge_window
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: embargo_window
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: frequency
      :type:  Frequency
      :value: Ellipsis



   .. py:attribute:: bar_interval
      :type:  pd.Timedelta
      :value: Ellipsis



   .. py:attribute:: encoder_input
      :type:  EncoderInputContract | None
      :value: Ellipsis



.. py:function:: build_meta_task(data_view, regime_label, signal_ids, signal_mask, signal_set_version, encoder, horizon, config)

