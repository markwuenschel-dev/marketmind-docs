pysrc.tuning.live.event_router
==============================

.. py:module:: pysrc.tuning.live.event_router


Attributes
----------

.. autoapisummary::

   pysrc.tuning.live.event_router.Handler


Classes
-------

.. autoapisummary::

   pysrc.tuning.live.event_router.TuningEvent
   pysrc.tuning.live.event_router.EventRouter


Module Contents
---------------

.. py:class:: TuningEvent

   .. py:attribute:: kind
      :type:  str
      :value: Ellipsis



   .. py:attribute:: payload
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:data:: Handler
   :type:  Any

.. py:class:: EventRouter

   .. py:method:: register(kind, handler)


   .. py:method:: route(event)


