errors
======

.. py:module:: errors


Exceptions
----------

.. autoapisummary::

   errors.BacktestingContractError
   errors.DeterminismTierMissingError
   errors.PitUnsafeInputError
   errors.OptionalDependencyMissingError
   errors.NotImplementedLaneError
   errors.UnknownIdError


Module Contents
---------------

.. py:exception:: BacktestingContractError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: DeterminismTierMissingError

   Bases: :py:obj:`BacktestingContractError`


   Unspecified run-time error.


.. py:exception:: PitUnsafeInputError

   Bases: :py:obj:`BacktestingContractError`


   Unspecified run-time error.


.. py:exception:: OptionalDependencyMissingError

   Bases: :py:obj:`BacktestingContractError`


   Unspecified run-time error.


.. py:exception:: NotImplementedLaneError

   Bases: :py:obj:`BacktestingContractError`


   Unspecified run-time error.


.. py:exception:: UnknownIdError

   Bases: :py:obj:`BacktestingContractError`


   Unspecified run-time error.


   .. py:attribute:: component_kind
      :type:  str
      :value: Ellipsis



   .. py:attribute:: requested_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: available_ids
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: hint
      :type:  str
      :value: Ellipsis



