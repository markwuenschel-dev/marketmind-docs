protocols
=========

.. py:module:: protocols


Classes
-------

.. autoapisummary::

   protocols.AsOfView
   protocols.BacktestArtifactStore
   protocols.BacktestEngine
   protocols.ExecutionModel
   protocols.CostModel
   protocols.Ledger
   protocols.BacktestValidator
   protocols.BacktestSuiteOrchestrator


Module Contents
---------------

.. py:class:: AsOfView

   Bases: :py:obj:`Protocol`


   .. py:method:: as_of(ts)


   .. py:method:: pit_meta()


.. py:class:: BacktestArtifactStore

   Bases: :py:obj:`Protocol`


   .. py:method:: put_json(role, payload)


   .. py:method:: put_bytes(role, payload, media_type)


   .. py:method:: get_json(ref)


.. py:class:: BacktestEngine

   Bases: :py:obj:`Protocol`


   .. py:method:: run(plan, data, store)


.. py:class:: ExecutionModel

   Bases: :py:obj:`Protocol`


   .. py:method:: simulate(orders, ctx)


.. py:class:: CostModel

   Bases: :py:obj:`Protocol`


   .. py:method:: estimate(fills, ctx)


.. py:class:: Ledger

   Bases: :py:obj:`Protocol`


   .. py:method:: apply(fills, corporate_actions)


.. py:class:: BacktestValidator

   Bases: :py:obj:`Protocol`


   .. py:method:: validate(result, ctx, store)


.. py:class:: BacktestSuiteOrchestrator

   Bases: :py:obj:`Protocol`


   .. py:method:: execute(suite_plan)


