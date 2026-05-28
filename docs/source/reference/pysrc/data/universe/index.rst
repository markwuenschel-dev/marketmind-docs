pysrc.data.universe
===================

.. py:module:: pysrc.data.universe


Classes
-------

.. autoapisummary::

   pysrc.data.universe.MembershipReasonCode
   pysrc.data.universe.Universe


Module Contents
---------------

.. py:class:: MembershipReasonCode

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


   .. py:attribute:: FIXTURE_SEED
      :type:  Any


   .. py:attribute:: GOVERNED
      :type:  Any


   .. py:attribute:: MANUAL
      :type:  Any


   .. py:attribute:: RELIST
      :type:  Any


.. py:class:: Universe

   .. py:method:: register(symbol, list_date, *, reason_code = ...)


   .. py:method:: delist(symbol, delist_date, *, reason_code = ...)


   .. py:method:: has_listing(symbol)


   .. py:method:: effective_state_at(symbol, as_of_date)


   .. py:method:: members_as_of(as_of_date)


