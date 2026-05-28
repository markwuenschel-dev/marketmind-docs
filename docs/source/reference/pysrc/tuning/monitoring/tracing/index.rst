pysrc.tuning.monitoring.tracing
===============================

.. py:module:: pysrc.tuning.monitoring.tracing


Classes
-------

.. autoapisummary::

   pysrc.tuning.monitoring.tracing.Span


Functions
---------

.. autoapisummary::

   pysrc.tuning.monitoring.tracing.trace


Module Contents
---------------

.. py:class:: Span

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: start_ns
      :type:  int
      :value: Ellipsis



   .. py:attribute:: end_ns
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: tags
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: finish()


   .. py:method:: duration_ms()


.. py:function:: trace(name, tags = ...)

