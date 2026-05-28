pysrc.pipeline.stages.cleaning.core.providers
=============================================

.. py:module:: pysrc.pipeline.stages.cleaning.core.providers


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.providers.GovernedColumns
   pysrc.pipeline.stages.cleaning.core.providers.GovernedColumnProvider
   pysrc.pipeline.stages.cleaning.core.providers.FailClosedProvider


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.providers.default_cleaning_providers


Module Contents
---------------

.. py:class:: GovernedColumns

   .. py:attribute:: frame
      :type:  pl.DataFrame
      :value: Ellipsis



   .. py:attribute:: lineage
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: warnings
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



.. py:class:: GovernedColumnProvider

   Bases: :py:obj:`Protocol`


   .. py:attribute:: provider_name
      :type:  str
      :value: Ellipsis



   .. py:method:: materialize(df, *, context, params)


.. py:class:: FailClosedProvider(provider_name)

   .. py:method:: materialize(df, *, context, params)


.. py:function:: default_cleaning_providers()

