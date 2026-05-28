pysrc.meta_learning.inference_boundary
======================================

.. py:module:: pysrc.meta_learning.inference_boundary


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.inference_boundary.CONTRACT_VERSION
   pysrc.meta_learning.inference_boundary.TrainingOutcome


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.inference_boundary.ParameterRole
   pysrc.meta_learning.inference_boundary.ExecutionPath
   pysrc.meta_learning.inference_boundary.RolloutStage
   pysrc.meta_learning.inference_boundary.ThetaDayPrimeCheckpointRef


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.inference_boundary.rollout_stage_assumes_frozen_live_checkpoint
   pysrc.meta_learning.inference_boundary.validate_parameter_roles
   pysrc.meta_learning.inference_boundary.validate_frozen_inference_request
   pysrc.meta_learning.inference_boundary.assert_no_live_gradients
   pysrc.meta_learning.inference_boundary.ensure_training_only_task_prime
   pysrc.meta_learning.inference_boundary.promote_theta_day_prime
   pysrc.meta_learning.inference_boundary.rollback_theta_day_prime
   pysrc.meta_learning.inference_boundary.build_inference_boundary_audit_block
   pysrc.meta_learning.inference_boundary.validate_inference_boundary_audit_block


Module Contents
---------------

.. py:data:: CONTRACT_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: ParameterRole

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


   .. py:attribute:: THETA_META
      :type:  Any


   .. py:attribute:: THETA_TASK_PRIME
      :type:  Any


   .. py:attribute:: THETA_DAY_PRIME
      :type:  Any


.. py:class:: ExecutionPath

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


   .. py:attribute:: LIVE_INFERENCE
      :type:  Any


   .. py:attribute:: TRAINING
      :type:  Any


.. py:class:: RolloutStage

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


   .. py:attribute:: SHADOW
      :type:  Any


   .. py:attribute:: CAPPED_BLEND
      :type:  Any


   .. py:attribute:: FULL_PROMOTION
      :type:  Any


.. py:data:: TrainingOutcome
   :type:  Any

.. py:function:: rollout_stage_assumes_frozen_live_checkpoint(stage)

.. py:class:: ThetaDayPrimeCheckpointRef

   .. py:attribute:: checkpoint_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: artifact_role
      :type:  ParameterRole
      :value: Ellipsis



.. py:function:: validate_parameter_roles(*, checkpoint_role, expected)

.. py:function:: validate_frozen_inference_request(*, execution_path, checkpoint_role, allows_gradients)

.. py:function:: assert_no_live_gradients(*, execution_path, allows_gradients)

.. py:function:: ensure_training_only_task_prime(*, checkpoint_role, execution_path)

.. py:function:: promote_theta_day_prime(*, current_live, candidate, gate_passed, nightly_training_succeeded)

.. py:function:: rollback_theta_day_prime(*, current_live, rollback_target)

.. py:function:: build_inference_boundary_audit_block(*, previous_live_theta_day_prime_ref, live_theta_day_prime_ref, rollback_theta_day_prime_ref, theta_meta_ref, training_outcome, rollout_stage = ...)

.. py:function:: validate_inference_boundary_audit_block(block)

