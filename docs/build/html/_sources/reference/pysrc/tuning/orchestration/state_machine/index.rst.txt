pysrc.tuning.orchestration.state_machine
========================================

.. py:module:: pysrc.tuning.orchestration.state_machine


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.orchestration.state_machine.InvalidTransitionError


Classes
-------

.. autoapisummary::

   pysrc.tuning.orchestration.state_machine.JobState
   pysrc.tuning.orchestration.state_machine.JobStateMachine


Module Contents
---------------

.. py:class:: JobState

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


   .. py:attribute:: REGISTERING
      :type:  Any


   .. py:attribute:: RUNNING
      :type:  Any


   .. py:attribute:: COMPLETE
      :type:  Any


   .. py:attribute:: FAILED
      :type:  Any


   .. py:attribute:: CANCELLED
      :type:  Any


.. py:exception:: InvalidTransitionError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:class:: JobStateMachine(job_id)

   .. py:method:: state()


   .. py:method:: transition(to)


