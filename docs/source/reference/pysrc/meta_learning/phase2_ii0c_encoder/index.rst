pysrc.meta_learning.phase2_ii0c_encoder
=======================================

.. py:module:: pysrc.meta_learning.phase2_ii0c_encoder


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_encoder.II0C_ENCODER_SCHEMA_VERSION
   pysrc.meta_learning.phase2_ii0c_encoder.II0C_ENCODER_REPORT_SCHEMA_VERSION
   pysrc.meta_learning.phase2_ii0c_encoder.II0C_ENCODER_VERSION
   pysrc.meta_learning.phase2_ii0c_encoder.II0C_ENCODER_EMBEDDING_DIM


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_encoder.Phase2II0CEncoderConfig
   pysrc.meta_learning.phase2_ii0c_encoder.II0CEncoderTaskOutput
   pysrc.meta_learning.phase2_ii0c_encoder.II0CEncoderStub


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_encoder.build_phase2_ii0c_encoder_metadata


Module Contents
---------------

.. py:data:: II0C_ENCODER_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: II0C_ENCODER_REPORT_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: II0C_ENCODER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: II0C_ENCODER_EMBEDDING_DIM
   :type:  Final[int]
   :value: Ellipsis


.. py:class:: Phase2II0CEncoderConfig

   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embedding_dim
      :type:  int
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: encoder_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: report_schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: ablation_flags
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: scaffold_only
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: reference_only
      :type:  bool
      :value: Ellipsis



.. py:class:: II0CEncoderTaskOutput

   .. py:attribute:: embedding
      :type:  tuple[float, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: II0CEncoderStub(config = ...)

   .. py:method:: config()


   .. py:method:: is_frozen()


   .. py:method:: encode_task(task)


   .. py:method:: encode(input)


   .. py:method:: build_metadata(*, input, output = ...)


.. py:function:: build_phase2_ii0c_encoder_metadata(*, input, output = ..., config = ...)

