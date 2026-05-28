pysrc.data.pit_config
=====================

.. py:module:: pysrc.data.pit_config


Classes
-------

.. autoapisummary::

   pysrc.data.pit_config.FillPolicy
   pysrc.data.pit_config.MissingPolicy
   pysrc.data.pit_config.ResolvedFieldConfig
   pysrc.data.pit_config.FieldTTLConfig


Functions
---------

.. autoapisummary::

   pysrc.data.pit_config.resolve_field_config


Module Contents
---------------

.. py:class:: FillPolicy

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


   .. py:attribute:: FORWARD
      :type:  Any


   .. py:attribute:: REJECT
      :type:  Any


.. py:class:: MissingPolicy

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


   .. py:attribute:: WARN
      :type:  Any


   .. py:attribute:: FAIL
      :type:  Any


.. py:class:: ResolvedFieldConfig

   .. py:attribute:: ttl_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fill_policy
      :type:  FillPolicy
      :value: Ellipsis



   .. py:attribute:: missing_policy
      :type:  MissingPolicy
      :value: Ellipsis



.. py:class:: FieldTTLConfig

   .. py:attribute:: default_config
      :type:  ResolvedFieldConfig
      :value: Ellipsis



   .. py:attribute:: field_configs
      :type:  Dict[str, ResolvedFieldConfig]
      :value: Ellipsis



   .. py:attribute:: namespace_configs
      :type:  Dict[str, ResolvedFieldConfig]
      :value: Ellipsis



   .. py:method:: resolve_field_config(field_name)


.. py:function:: resolve_field_config(field_name, config)

