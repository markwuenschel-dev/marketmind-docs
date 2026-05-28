pysrc.meta.seed_policy
======================

.. py:module:: pysrc.meta.seed_policy


Attributes
----------

.. autoapisummary::

   pysrc.meta.seed_policy.RUN_IDENTITY_SCHEMA
   pysrc.meta.seed_policy.SEED_LINEAGE_SCHEMA
   pysrc.meta.seed_policy.RUN_ID_SALT
   pysrc.meta.seed_policy.DERIVED_SEED_MESSAGE_PREFIX
   pysrc.meta.seed_policy.ALLOWED_SEED_NAMESPACES


Classes
-------

.. autoapisummary::

   pysrc.meta.seed_policy.Phase2ScaffoldRunIdentity
   pysrc.meta.seed_policy.Phase2DerivedSeed
   pysrc.meta.seed_policy.Phase2SeedLineage


Functions
---------

.. autoapisummary::

   pysrc.meta.seed_policy.derive_run_id
   pysrc.meta.seed_policy.scaffold_int_seed_from_content_tag
   pysrc.meta.seed_policy.build_run_identity
   pysrc.meta.seed_policy.run_seed_root_from_int
   pysrc.meta.seed_policy.derive_phase2_seed
   pysrc.meta.seed_policy.build_seed_lineage


Module Contents
---------------

.. py:data:: RUN_IDENTITY_SCHEMA
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SEED_LINEAGE_SCHEMA
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: RUN_ID_SALT
   :type:  Final[bytes]
   :value: Ellipsis


.. py:data:: DERIVED_SEED_MESSAGE_PREFIX
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALLOWED_SEED_NAMESPACES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:class:: Phase2ScaffoldRunIdentity

   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:method:: to_block()


.. py:function:: derive_run_id(seed)

.. py:function:: scaffold_int_seed_from_content_tag(tag)

.. py:function:: build_run_identity(seed)

.. py:class:: Phase2DerivedSeed

   .. py:attribute:: namespace
      :type:  str
      :value: Ellipsis



   .. py:attribute:: context_string
      :type:  str
      :value: Ellipsis



   .. py:attribute:: derived_seed_hex
      :type:  str
      :value: Ellipsis



   .. py:attribute:: uint64_seed
      :type:  int
      :value: Ellipsis



   .. py:method:: to_block()


.. py:class:: Phase2SeedLineage

   .. py:attribute:: run_seed_root
      :type:  str
      :value: Ellipsis



   .. py:attribute:: derived_seeds
      :type:  tuple[Phase2DerivedSeed, Ellipsis]
      :value: Ellipsis



   .. py:method:: to_block()


.. py:function:: run_seed_root_from_int(seed)

.. py:function:: derive_phase2_seed(*, run_seed_root, namespace, context_string)

.. py:function:: build_seed_lineage(*, run_seed_root, derivations)

