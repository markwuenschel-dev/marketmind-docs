pysrc.tuning.monitoring.alerts
==============================

.. py:module:: pysrc.tuning.monitoring.alerts


Classes
-------

.. autoapisummary::

   pysrc.tuning.monitoring.alerts.AlertSeverity
   pysrc.tuning.monitoring.alerts.Alert


Functions
---------

.. autoapisummary::

   pysrc.tuning.monitoring.alerts.emit_alert


Module Contents
---------------

.. py:class:: AlertSeverity

   Bases: :py:obj:`str`, :py:obj:`Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: INFO
      :type:  Any


   .. py:attribute:: WARNING
      :type:  Any


   .. py:attribute:: CRITICAL
      :type:  Any


.. py:class:: Alert

   .. py:attribute:: severity
      :type:  AlertSeverity
      :value: Ellipsis



   .. py:attribute:: title
      :type:  str
      :value: Ellipsis



   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: details
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: emitted_at
      :type:  datetime
      :value: Ellipsis



.. py:function:: emit_alert(alert)

