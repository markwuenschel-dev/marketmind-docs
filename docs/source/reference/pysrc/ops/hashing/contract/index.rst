pysrc.ops.hashing.contract
==========================

.. py:module:: pysrc.ops.hashing.contract


Exceptions
----------

.. autoapisummary::

   pysrc.ops.hashing.contract.HashContractViolation
   pysrc.ops.hashing.contract.CanonicalValueRejected


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.contract.DTier
   pysrc.ops.hashing.contract.PersistenceTier
   pysrc.ops.hashing.contract.AlgoId
   pysrc.ops.hashing.contract.DomainPrefix
   pysrc.ops.hashing.contract.HashPurposeMetadata
   pysrc.ops.hashing.contract.HashPurpose
   pysrc.ops.hashing.contract.SystemInvariant


Module Contents
---------------

.. py:class:: DTier

   Bases: :py:obj:`enum.IntEnum`


   .. py:attribute:: NONE
      :type:  Any


   .. py:attribute:: TOPOLOGICAL
      :type:  Any


   .. py:attribute:: SEMANTIC
      :type:  Any


   .. py:attribute:: BITWISE
      :type:  Any


.. py:class:: PersistenceTier

   Bases: :py:obj:`enum.Enum`


   .. py:attribute:: IMMUTABLE_CAS
      :type:  Any


   .. py:attribute:: DISTRIBUTED
      :type:  Any


   .. py:attribute:: LOCAL_PERSISTENT
      :type:  Any


   .. py:attribute:: EPHEMERAL
      :type:  Any


.. py:class:: AlgoId

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: BLAKE3_256
      :type:  Any


   .. py:attribute:: SHA256_JCS
      :type:  Any


   .. py:attribute:: XXH3_128
      :type:  Any


   .. py:attribute:: XXH3_64
      :type:  Any


   .. py:attribute:: SIP24
      :type:  Any


   .. py:attribute:: HMAC_SHA256
      :type:  Any


   .. py:attribute:: SIMHASH_128
      :type:  Any


   .. py:attribute:: MINHASH_128
      :type:  Any


   .. py:attribute:: RABIN_63
      :type:  Any


.. py:class:: DomainPrefix

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: CAS
      :type:  Any


   .. py:attribute:: MERKLE
      :type:  Any


   .. py:attribute:: AUDIT
      :type:  Any


   .. py:attribute:: ATTEST
      :type:  Any


   .. py:attribute:: CACHE
      :type:  Any


   .. py:attribute:: DIST
      :type:  Any


   .. py:attribute:: FRAME
      :type:  Any


   .. py:attribute:: SEED
      :type:  Any


   .. py:attribute:: LSH
      :type:  Any


   .. py:attribute:: ROLLING
      :type:  Any


.. py:class:: HashPurposeMetadata

   .. py:attribute:: algo_id
      :type:  AlgoId
      :value: Ellipsis



   .. py:attribute:: d_tier
      :type:  DTier
      :value: Ellipsis



   .. py:attribute:: persistence_tier
      :type:  PersistenceTier
      :value: Ellipsis



   .. py:attribute:: domain_prefix
      :type:  DomainPrefix
      :value: Ellipsis



   .. py:attribute:: algo_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: canonicalizer_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: canonicalizer_version
      :type:  str
      :value: Ellipsis



.. py:class:: HashPurpose

   Bases: :py:obj:`enum.Enum`


   .. py:attribute:: CAS_ARTIFACT_ID
      :type:  Any


   .. py:attribute:: MERKLE_NODE_HASH
      :type:  Any


   .. py:attribute:: AUDIT_LOG_DIGEST
      :type:  Any


   .. py:attribute:: GATE_ATTESTATION
      :type:  Any


   .. py:attribute:: DISTRIBUTED_CACHE_KEY
      :type:  Any


   .. py:attribute:: LOCAL_PERSISTENT_CACHE_KEY
      :type:  Any


   .. py:attribute:: DATAFRAME_FINGERPRINT_FAST
      :type:  Any


   .. py:attribute:: EPHEMERAL_MAP_KEY
      :type:  Any


   .. py:attribute:: HASHDOS_TABLE_KEY
      :type:  Any


   .. py:attribute:: UNTRUSTED_INPUT_EPHEMERAL_KEY
      :type:  Any


   .. py:attribute:: SEED_DERIVATION
      :type:  Any


   .. py:attribute:: LSH_VECTOR_SIMHASH
      :type:  Any


   .. py:attribute:: LSH_SET_MINHASH
      :type:  Any


   .. py:attribute:: ROLLING_WINDOW_FINGERPRINT
      :type:  Any


   .. py:attribute:: CHUNK_BOUNDARY_DETECTION
      :type:  Any


   .. py:method:: meta()


   .. py:method:: requires_d3()


   .. py:method:: is_persistent()


   .. py:method:: is_ahm_forbidden()


.. py:class:: SystemInvariant

   Bases: :py:obj:`enum.Enum`


   .. py:attribute:: CANONICAL_UTF8
      :type:  Any


   .. py:attribute:: CANONICAL_BIG_ENDIAN
      :type:  Any


   .. py:attribute:: IEEE754_NORMALIZED
      :type:  Any


   .. py:attribute:: DOMAIN_SEPARATED_PREIMAGE
      :type:  Any


   .. py:attribute:: NO_RUNTIME_LAYOUT_DEPENDENCE
      :type:  Any


   .. py:attribute:: GOLDEN_VECTOR_REQUIRED
      :type:  Any


   .. py:attribute:: D3_BITWISE_REQUIRED
      :type:  Any


.. py:exception:: HashContractViolation(invariant, detail)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: CanonicalValueRejected(field, value, reason)

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


