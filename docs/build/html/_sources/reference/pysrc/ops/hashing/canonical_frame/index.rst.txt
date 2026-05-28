pysrc.ops.hashing.canonical_frame
=================================

.. py:module:: pysrc.ops.hashing.canonical_frame


Attributes
----------

.. autoapisummary::

   pysrc.ops.hashing.canonical_frame.CANONICAL_FRAME_CI_EVIDENCE
   pysrc.ops.hashing.canonical_frame.CANONICAL_FRAME_CI_STATUS
   pysrc.ops.hashing.canonical_frame.CANONICAL_FRAME_CI_STATUS_VALUE
   pysrc.ops.hashing.canonical_frame.CANONICAL_FRAME_CI_EVIDENCE_DICT


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.canonical_frame.CanonicalFrameCIStatus
   pysrc.ops.hashing.canonical_frame.CanonicalFrameCIEvidence


Functions
---------

.. autoapisummary::

   pysrc.ops.hashing.canonical_frame.load_canonical_frame_ci_evidence


Module Contents
---------------

.. py:class:: CanonicalFrameCIStatus

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


   .. py:attribute:: UNCERTIFIED
      :type:  Any


   .. py:attribute:: PYTHON_ONLY_D2
      :type:  Any


   .. py:attribute:: CROSSLANG_D2_CERTIFIED
      :type:  Any


   .. py:attribute:: CROSSLANG_D3_CERTIFIED
      :type:  Any


.. py:class:: CanonicalFrameCIEvidence

   .. py:attribute:: python_certified
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: golden_vectors_present
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: cross_language_certified
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: d3_primitives_promoted
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: notes
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:method:: status()


   .. py:method:: to_dict()


.. py:function:: load_canonical_frame_ci_evidence(path = ...)

.. py:data:: CANONICAL_FRAME_CI_EVIDENCE
   :type:  Any

.. py:data:: CANONICAL_FRAME_CI_STATUS
   :type:  Any

.. py:data:: CANONICAL_FRAME_CI_STATUS_VALUE
   :type:  Any

.. py:data:: CANONICAL_FRAME_CI_EVIDENCE_DICT
   :type:  Any

