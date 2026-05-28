pysrc.validation.task_validity
==============================

.. py:module:: pysrc.validation.task_validity


Attributes
----------

.. autoapisummary::

   pysrc.validation.task_validity.DIAGNOSTIC_VERSION
   pysrc.validation.task_validity.TASK_VALIDITY_INPUTS
   pysrc.validation.task_validity.SCHEMA_RELATIVE_PATH
   pysrc.validation.task_validity.JsonScalar
   pysrc.validation.task_validity.JsonValue
   pysrc.validation.task_validity.JsonObject


Classes
-------

.. autoapisummary::

   pysrc.validation.task_validity.TaskValidityCheck
   pysrc.validation.task_validity.TaskValidityReport


Functions
---------

.. autoapisummary::

   pysrc.validation.task_validity.validate_task
   pysrc.validation.task_validity.check_task_non_exchangeability
   pysrc.validation.task_validity.check_leakage_geometry
   pysrc.validation.task_validity.check_episode_construction_validity


Module Contents
---------------

.. py:data:: DIAGNOSTIC_VERSION
   :type:  Any

.. py:data:: TASK_VALIDITY_INPUTS
   :type:  Any

.. py:data:: SCHEMA_RELATIVE_PATH
   :type:  Any

.. py:type:: JsonScalar
   :canonical: ...


.. py:type:: JsonValue
   :canonical: ...


.. py:type:: JsonObject
   :canonical: ...


.. py:class:: TaskValidityCheck

   .. py:attribute:: check_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: check_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: evidence
      :type:  JsonObject
      :value: Ellipsis



   .. py:method:: to_json_dict()


.. py:class:: TaskValidityReport

   .. py:attribute:: bundle_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: checks
      :type:  tuple[TaskValidityCheck, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: all_pass
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: diagnostic_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp
      :type:  str
      :value: Ellipsis



   .. py:method:: to_json_dict()


.. py:function:: validate_task(bundle_path)

.. py:function:: check_task_non_exchangeability(bundle_path)

.. py:function:: check_leakage_geometry(bundle_path)

.. py:function:: check_episode_construction_validity(bundle_path)

