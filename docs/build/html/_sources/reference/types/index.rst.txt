types
=====

.. py:module:: types


Classes
-------

.. autoapisummary::

   types.ValidationStatus
   types.ArtifactRef
   types.RunBundleRef
   types.PitMeta
   types.MarketSlice
   types.Fill
   types.CostEstimate
   types.LedgerPosition
   types.LedgerSnapshot
   types.BacktestResult
   types.ValidationReport
   types.MarketDataPoint


Functions
---------

.. autoapisummary::

   types.to_primitive


Module Contents
---------------

.. py:class:: ValidationStatus

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


   .. py:attribute:: PASS
      :type:  Any


   .. py:attribute:: WARN
      :type:  Any


   .. py:attribute:: FAIL
      :type:  Any


.. py:class:: ArtifactRef

   .. py:attribute:: role
      :type:  str
      :value: Ellipsis



   .. py:attribute:: path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cas
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: attest
      :type:  str | None
      :value: Ellipsis



.. py:class:: RunBundleRef

   .. py:attribute:: bundle_path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: manifest_ref
      :type:  ArtifactRef | None
      :value: Ellipsis



.. py:class:: PitMeta

   .. py:attribute:: as_of
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: source
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: knowledge_cutoff
      :type:  str | None
      :value: Ellipsis



.. py:class:: MarketSlice

   .. py:attribute:: as_of
      :type:  str
      :value: Ellipsis



   .. py:attribute:: prices
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: features
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: pit_meta
      :type:  PitMeta | None
      :value: Ellipsis



.. py:class:: Fill

   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: quantity
      :type:  float
      :value: Ellipsis



   .. py:attribute:: price
      :type:  float
      :value: Ellipsis



   .. py:attribute:: side
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp
      :type:  str
      :value: Ellipsis



.. py:class:: CostEstimate

   .. py:attribute:: total_cost
      :type:  float
      :value: Ellipsis



   .. py:attribute:: components
      :type:  dict[str, float]
      :value: Ellipsis



.. py:class:: LedgerPosition

   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: quantity
      :type:  float
      :value: Ellipsis



   .. py:attribute:: average_price
      :type:  float
      :value: Ellipsis



.. py:class:: LedgerSnapshot

   .. py:attribute:: timestamp
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cash
      :type:  float
      :value: Ellipsis



   .. py:attribute:: positions
      :type:  list[LedgerPosition]
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: BacktestResult

   .. py:attribute:: metrics
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: artifacts
      :type:  dict[str, ArtifactRef]
      :value: Ellipsis



   .. py:attribute:: warnings
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: errors
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: fills
      :type:  list[Fill]
      :value: Ellipsis



   .. py:attribute:: ledger
      :type:  LedgerSnapshot | None
      :value: Ellipsis



.. py:class:: ValidationReport

   .. py:attribute:: status
      :type:  ValidationStatus
      :value: Ellipsis



   .. py:attribute:: reason_code
      :type:  str
      :value: Ellipsis



   .. py:attribute:: message
      :type:  str
      :value: Ellipsis



   .. py:attribute:: artifacts
      :type:  dict[str, ArtifactRef]
      :value: Ellipsis



.. py:class:: MarketDataPoint

   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp
      :type:  str
      :value: Ellipsis



   .. py:attribute:: value
      :type:  float
      :value: Ellipsis



   .. py:attribute:: field_name
      :type:  str
      :value: Ellipsis



.. py:function:: to_primitive(value)

