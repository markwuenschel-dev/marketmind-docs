pysrc.tuning.api.errors
=======================

.. py:module:: pysrc.tuning.api.errors


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.api.errors.APIError
   pysrc.tuning.api.errors.JobNotFoundError
   pysrc.tuning.api.errors.InvalidRequestError
   pysrc.tuning.api.errors.GateFailedError


Functions
---------

.. autoapisummary::

   pysrc.tuning.api.errors.map_domain_error


Module Contents
---------------

.. py:exception:: APIError(detail, status_code = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: status_code
      :type:  int
      :value: Ellipsis



   .. py:attribute:: detail
      :type:  str
      :value: Ellipsis



.. py:exception:: JobNotFoundError(detail)

   Bases: :py:obj:`APIError`


   Common base class for all non-exit exceptions.


   .. py:attribute:: status_code
      :type:  Any


.. py:exception:: InvalidRequestError(detail)

   Bases: :py:obj:`APIError`


   Common base class for all non-exit exceptions.


   .. py:attribute:: status_code
      :type:  Any


.. py:exception:: GateFailedError(detail)

   Bases: :py:obj:`APIError`


   Common base class for all non-exit exceptions.


   .. py:attribute:: status_code
      :type:  Any


.. py:function:: map_domain_error(exc)

