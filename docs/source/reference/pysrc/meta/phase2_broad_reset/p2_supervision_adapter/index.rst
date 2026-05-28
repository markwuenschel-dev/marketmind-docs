pysrc.meta.phase2_broad_reset.p2_supervision_adapter
====================================================

.. py:module:: pysrc.meta.phase2_broad_reset.p2_supervision_adapter


Attributes
----------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_supervision_adapter.Grain


Classes
-------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_supervision_adapter.NarrowSupervisionFrame


Functions
---------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_supervision_adapter.generate_synthetic_router_supervision
   pysrc.meta.phase2_broad_reset.p2_supervision_adapter.cast_child_policy_ids
   pysrc.meta.phase2_broad_reset.p2_supervision_adapter.extract_allowed_feature_names
   pysrc.meta.phase2_broad_reset.p2_supervision_adapter.load_narrow_supervision_frame


Module Contents
---------------

.. py:data:: Grain
   :type:  Any

.. py:class:: NarrowSupervisionFrame

   .. py:attribute:: frame
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: child_policy_ids
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: feature_names
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: target_columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: source_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: grain
      :type:  Grain
      :value: Ellipsis



   .. py:attribute:: provenance
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:function:: generate_synthetic_router_supervision(n_rows = ..., n_features = ..., n_children = ..., random_seed = ...)

.. py:function:: cast_child_policy_ids(date_frame)

.. py:function:: extract_allowed_feature_names(date_frame)

.. py:function:: load_narrow_supervision_frame(config)

