marketmind_gate.errors
======================

.. py:module:: marketmind_gate.errors


Exceptions
----------

.. autoapisummary::

   marketmind_gate.errors.GateRunnerError
   marketmind_gate.errors.SchemaValidationError
   marketmind_gate.errors.HashMismatchError
   marketmind_gate.errors.URIResolutionError
   marketmind_gate.errors.UnsupportedURISchemeError
   marketmind_gate.errors.MissingLockError
   marketmind_gate.errors.IncomparableError
   marketmind_gate.errors.RankDeltaMismatchError
   marketmind_gate.errors.KValuesMismatchError
   marketmind_gate.errors.BindingInvalidError
   marketmind_gate.errors.ThresholdViolationError
   marketmind_gate.errors.MissingRequiredArtifactError
   marketmind_gate.errors.ConfigurationError


Classes
-------

.. autoapisummary::

   marketmind_gate.errors.GateError


Module Contents
---------------

.. py:class:: GateError

   .. py:attribute:: code
      :type:  str
      :value: Ellipsis



   .. py:attribute:: message
      :type:  str
      :value: Ellipsis



   .. py:attribute:: severity
      :type:  str
      :value: Ellipsis



   .. py:attribute:: file
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: uri
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: schema_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:exception:: GateRunnerError(error)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: SchemaValidationError(message, *, file = ..., path = ..., schema_path = ..., context = ...)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: HashMismatchError(*, uri, path = ..., declared_hash, computed_hash)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: URIResolutionError(uri, reason)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: UnsupportedURISchemeError(uri, scheme)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: MissingLockError(lock, lane)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: IncomparableError(lock, value_a, value_b)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: RankDeltaMismatchError(*, candidate_key, index, lane_a_rank, lane_b_rank, declared_delta, computed_delta)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: KValuesMismatchError(*, declared_ks, referenced_ks, missing_declarations = ..., missing_metrics = ...)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: BindingInvalidError(message, *, mode, has_plan_hash_a, has_plan_hash_b, has_run_ids)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: ThresholdViolationError(*, metric_name, actual, expected_min = ..., expected_max = ...)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: MissingRequiredArtifactError(artifact_type, mode)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


.. py:exception:: ConfigurationError(message, *, context = ...)

   Bases: :py:obj:`GateRunnerError`


   Common base class for all non-exit exceptions.


