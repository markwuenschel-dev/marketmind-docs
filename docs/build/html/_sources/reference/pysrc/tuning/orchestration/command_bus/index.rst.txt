pysrc.tuning.orchestration.command_bus
======================================

.. py:module:: pysrc.tuning.orchestration.command_bus


Attributes
----------

.. autoapisummary::

   pysrc.tuning.orchestration.command_bus.Handler


Classes
-------

.. autoapisummary::

   pysrc.tuning.orchestration.command_bus.Command
   pysrc.tuning.orchestration.command_bus.CommandBus


Module Contents
---------------

.. py:class:: Command

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: payload
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:data:: Handler
   :type:  Any

.. py:class:: CommandBus

   .. py:method:: register(command_name, handler)


   .. py:method:: dispatch(command)


