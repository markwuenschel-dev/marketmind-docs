invariants
==========

.. py:module:: invariants


Exceptions
----------

.. autoapisummary::

   invariants.InvariantViolation


Functions
---------

.. autoapisummary::

   invariants.assert_fill_timestamps_within_window
   invariants.assert_position_cash_directionality


Module Contents
---------------

.. py:exception:: InvariantViolation

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: assert_fill_timestamps_within_window(fills, start, end)

.. py:function:: assert_position_cash_directionality(before_cash, after_cash, fills)

