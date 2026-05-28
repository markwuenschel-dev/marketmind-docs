pysrc.autotune.api
==================

.. py:module:: pysrc.autotune.api


Attributes
----------

.. autoapisummary::

   pysrc.autotune.api.T


Classes
-------

.. autoapisummary::

   pysrc.autotune.api.AutotuneConfig
   pysrc.autotune.api.ObjectiveFn
   pysrc.autotune.api.AutotuneAPI


Module Contents
---------------

.. py:data:: T
   :type:  Any

.. py:class:: AutotuneConfig

   .. py:attribute:: strategy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: max_iterations
      :type:  int
      :value: Ellipsis



   .. py:attribute:: parallel_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: early_stopping
      :type:  bool
      :value: Ellipsis



.. py:class:: ObjectiveFn

   Bases: :py:obj:`Protocol`


.. py:class:: AutotuneAPI

   Bases: :py:obj:`ABC`


   .. py:method:: search(objective, space, config, *, callbacks = ...)


   .. py:method:: resume(run_id)


