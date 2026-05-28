pysrc.meta_learning.encoder_coherence_diagnostics
=================================================

.. py:module:: pysrc.meta_learning.encoder_coherence_diagnostics


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.encoder_coherence_diagnostics.CROSS_COSINE_RATIO_EPS
   pysrc.meta_learning.encoder_coherence_diagnostics.ENCODER_COHERENCE_REPORT_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.encoder_coherence_diagnostics.EncoderCoherenceDiagnostics


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.encoder_coherence_diagnostics.compute_encoder_coherence_diagnostics
   pysrc.meta_learning.encoder_coherence_diagnostics.build_encoder_coherence_report_payload
   pysrc.meta_learning.encoder_coherence_diagnostics.write_encoder_coherence_report
   pysrc.meta_learning.encoder_coherence_diagnostics.encoder_coherence_report_from_arrays


Module Contents
---------------

.. py:data:: CROSS_COSINE_RATIO_EPS
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: ENCODER_COHERENCE_REPORT_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: EncoderCoherenceDiagnostics

   .. py:attribute:: within_cosine
      :type:  float
      :value: Ellipsis



   .. py:attribute:: cross_cosine
      :type:  float
      :value: Ellipsis



   .. py:attribute:: separation_ratio
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: separation_ratio_note
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: silhouette_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: class_counts
      :type:  dict[str, int]
      :value: Ellipsis



.. py:function:: compute_encoder_coherence_diagnostics(embeddings, labels)

.. py:function:: build_encoder_coherence_report_payload(diagnostics, *, embedding_dim, n_tasks, producer, seed, notes, artifact_role = ...)

.. py:function:: write_encoder_coherence_report(path, payload)

.. py:function:: encoder_coherence_report_from_arrays(embeddings, labels, *, producer, seed, notes)

