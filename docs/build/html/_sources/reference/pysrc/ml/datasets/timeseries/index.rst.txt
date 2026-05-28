pysrc.ml.datasets.timeseries
============================

.. py:module:: pysrc.ml.datasets.timeseries


Attributes
----------

.. autoapisummary::

   pysrc.ml.datasets.timeseries.T


Classes
-------

.. autoapisummary::

   pysrc.ml.datasets.timeseries.SampleWindow
   pysrc.ml.datasets.timeseries.WindowConfig
   pysrc.ml.datasets.timeseries.DatasetBuilder


Module Contents
---------------

.. py:data:: T
   :type:  Any

.. py:class:: SampleWindow

   Bases: :py:obj:`Protocol`


   .. py:attribute:: lookback
      :type:  int
      :value: Ellipsis



   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: step
      :type:  int
      :value: Ellipsis



.. py:class:: WindowConfig

   .. py:attribute:: lookback
      :type:  int
      :value: Ellipsis



   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: step
      :type:  int
      :value: Ellipsis



.. py:class:: DatasetBuilder

   Bases: :py:obj:`ABC`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   .. py:method:: build(data, config, *, as_of = ...)


