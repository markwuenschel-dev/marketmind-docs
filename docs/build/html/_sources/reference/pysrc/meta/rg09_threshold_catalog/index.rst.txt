pysrc.meta.rg09_threshold_catalog
=================================

.. py:module:: pysrc.meta.rg09_threshold_catalog


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_threshold_catalog.VALIDATE_NOTE
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V01
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V02
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V03
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V04
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V05
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V06
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V07
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V08
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V09
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V10
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V11
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V12
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V13
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V14
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V15
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V16
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V17
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V18
   pysrc.meta.rg09_threshold_catalog.THR_RG09_V19
   pysrc.meta.rg09_threshold_catalog.RG09_CONFIG_THRESHOLD_SPECS
   pysrc.meta.rg09_threshold_catalog.RG09_CONFIGURED_THRESHOLD_PRECHECK_SPECS


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_threshold_catalog.RG09ThresholdFieldSpec


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_threshold_catalog.threshold_value_record
   pysrc.meta.rg09_threshold_catalog.provisional_threshold_record


Module Contents
---------------

.. py:data:: VALIDATE_NOTE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V02
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V03
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V04
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V05
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V06
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V07
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V08
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V09
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V10
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V11
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V12
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V13
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V14
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V15
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V16
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V17
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V18
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_RG09_V19
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: RG09ThresholdFieldSpec

   .. py:attribute:: threshold_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gate_critical
      :type:  bool
      :value: Ellipsis



.. py:data:: RG09_CONFIG_THRESHOLD_SPECS
   :type:  Final[dict[str, RG09ThresholdFieldSpec]]
   :value: Ellipsis


.. py:data:: RG09_CONFIGURED_THRESHOLD_PRECHECK_SPECS
   :type:  Final[dict[str, ConfiguredThresholdSpec]]
   :value: Ellipsis


.. py:function:: threshold_value_record(value, threshold_id, *, state = ...)

.. py:function:: provisional_threshold_record(value, threshold_id, *, state = ...)

