pysrc.meta_learning.contracts.encoder_contracts
===============================================

.. py:module:: pysrc.meta_learning.contracts.encoder_contracts


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.contracts.encoder_contracts.TASK_EPISODE_ENCODER_FEATURE_SCHEMA_VERSION
   pysrc.meta_learning.contracts.encoder_contracts.TASK_EPISODE_BOUNDARY_FLAG_ORDER
   pysrc.meta_learning.contracts.encoder_contracts.TASK_EPISODE_ENCODER_FEATURE_NAMES


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.contracts.encoder_contracts.EncoderInputContract
   pysrc.meta_learning.contracts.encoder_contracts.EncoderOutputContract
   pysrc.meta_learning.contracts.encoder_contracts.ContextEncoderProtocol


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.contracts.encoder_contracts.build_task_episode_encoder_input


Module Contents
---------------

.. py:data:: TASK_EPISODE_ENCODER_FEATURE_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: TASK_EPISODE_BOUNDARY_FLAG_ORDER
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: TASK_EPISODE_ENCODER_FEATURE_NAMES
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:class:: EncoderInputContract

   .. py:attribute:: regime_features
      :type:  np.ndarray[Any, Any]
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: signal_set_version
      :type:  int
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



.. py:class:: EncoderOutputContract

   .. py:attribute:: regime_embedding
      :type:  np.ndarray[Any, np.dtype[np.float32]]
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



.. py:function:: build_task_episode_encoder_input(*, regime_label, pit_boundary, signal_set_version)

.. py:class:: ContextEncoderProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: encode(input)


   .. py:method:: is_frozen()


