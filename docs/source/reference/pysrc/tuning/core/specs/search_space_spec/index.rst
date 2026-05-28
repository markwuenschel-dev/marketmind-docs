pysrc.tuning.core.specs.search_space_spec
=========================================

.. py:module:: pysrc.tuning.core.specs.search_space_spec


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.specs.search_space_spec.DimensionSpec
   pysrc.tuning.core.specs.search_space_spec.SearchSpaceSpec


Module Contents
---------------

.. py:class:: DimensionSpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: kind
      :type:  Literal['real', 'int', 'categorical', 'log_real']
      :value: Ellipsis



   .. py:attribute:: low
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: high
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: choices
      :type:  tuple[Any, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: prior
      :type:  Literal['uniform', 'log-uniform']
      :value: Ellipsis



.. py:class:: SearchSpaceSpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: model_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: spec_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dimensions
      :type:  tuple[DimensionSpec, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: fixed
      :type:  dict[str, Any]
      :value: Ellipsis



