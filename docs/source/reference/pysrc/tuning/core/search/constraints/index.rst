pysrc.tuning.core.search.constraints
====================================

.. py:module:: pysrc.tuning.core.search.constraints


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.core.search.constraints.ConstraintViolationError


Functions
---------

.. autoapisummary::

   pysrc.tuning.core.search.constraints.check_bounds
   pysrc.tuning.core.search.constraints.check_no_nan
   pysrc.tuning.core.search.constraints.validate_params


Module Contents
---------------

.. py:exception:: ConstraintViolationError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: check_bounds(name, value, low, high)

.. py:function:: check_no_nan(params)

.. py:function:: validate_params(params, bounds_map)

