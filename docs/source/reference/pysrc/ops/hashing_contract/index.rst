pysrc.ops.hashing_contract
==========================

.. py:module:: pysrc.ops.hashing_contract


Attributes
----------

.. autoapisummary::

   pysrc.ops.hashing_contract.HASH_EXCLUSIONS
   pysrc.ops.hashing_contract.hash_for_identity
   pysrc.ops.hashing_contract.hash_for_dedup
   pysrc.ops.hashing_contract.compute_content_hash
   pysrc.ops.hashing_contract.compute_plan_hash
   pysrc.ops.hashing_contract.get_code_identity
   pysrc.ops.hashing_contract.compute_env_hash
   pysrc.ops.hashing_contract.compute_data_version_hash


Exceptions
----------

.. autoapisummary::

   pysrc.ops.hashing_contract.HashingContractViolation


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing_contract.HashRef
   pysrc.ops.hashing_contract.QuantizationPolicy
   pysrc.ops.hashing_contract.CodeIdentity
   pysrc.ops.hashing_contract.DataManifestEntry
   pysrc.ops.hashing_contract.DataManifest
   pysrc.ops.hashing_contract.HashingContract


Functions
---------

.. autoapisummary::

   pysrc.ops.hashing_contract.to_gate_content_hash


Module Contents
---------------

.. py:exception:: HashingContractViolation

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:class:: HashRef

   .. py:attribute:: domain
      :type:  str
      :value: Ellipsis



   .. py:attribute:: algo
      :type:  str
      :value: Ellipsis



   .. py:attribute:: hex_digest
      :type:  str
      :value: Ellipsis



   .. py:method:: parse(value)


.. py:function:: to_gate_content_hash(attest)

.. py:class:: QuantizationPolicy

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


   .. py:attribute:: Q_NONE
      :type:  Any


   .. py:attribute:: Q_ROUND8
      :type:  Any


   .. py:attribute:: Q_ROUND6
      :type:  Any


   .. py:attribute:: Q_INT
      :type:  Any


.. py:data:: HASH_EXCLUSIONS
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:class:: CodeIdentity

   .. py:attribute:: commit_sha
      :type:  str
      :value: Ellipsis



   .. py:attribute:: is_dirty
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: dirty_patch_hash
      :type:  bytes | None
      :value: Ellipsis



   .. py:method:: to_hash_input()


.. py:class:: DataManifestEntry

   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: date_start
      :type:  date
      :value: Ellipsis



   .. py:attribute:: date_end
      :type:  date
      :value: Ellipsis



   .. py:attribute:: vendor
      :type:  str
      :value: Ellipsis



   .. py:attribute:: vendor_snapshot_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



.. py:class:: DataManifest

   .. py:attribute:: entries
      :type:  tuple[DataManifestEntry, Ellipsis]
      :value: Ellipsis



.. py:class:: HashingContract

   .. py:method:: hash_for_identity()


   .. py:method:: hash_for_dedup()


   .. py:method:: hash_sha256()


   .. py:method:: format_float(value, policy)


   .. py:method:: check_banned_values(obj, path = ...)


   .. py:method:: strip_exclusions(obj)


   .. py:method:: apply_quantization(obj, policies)


   .. py:method:: canonicalize_json(obj)


   .. py:method:: compute_content_hash(artifact, quantization_policies = ...)


   .. py:method:: compute_plan_hash(strategy_id, hyperparams, feature_config, code_hash, env_hash, data_version_hash, hyperparam_policies = ...)


   .. py:method:: get_code_identity()


   .. py:method:: compute_env_hash(lockfile_hash, cuda_version = ..., cudnn_version = ..., tensorrt_version = ..., blas_backend = ..., blas_version = ...)


   .. py:method:: compute_data_version_hash(manifest)


.. py:data:: hash_for_identity
   :type:  Any

.. py:data:: hash_for_dedup
   :type:  Any

.. py:data:: compute_content_hash
   :type:  Any

.. py:data:: compute_plan_hash
   :type:  Any

.. py:data:: get_code_identity
   :type:  Any

.. py:data:: compute_env_hash
   :type:  Any

.. py:data:: compute_data_version_hash
   :type:  Any

