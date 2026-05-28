marketmind_gate.policy.loader
=============================

.. py:module:: marketmind_gate.policy.loader


Classes
-------

.. autoapisummary::

   marketmind_gate.policy.loader.PolicyConfig


Functions
---------

.. autoapisummary::

   marketmind_gate.policy.loader.load_policy


Module Contents
---------------

.. py:class:: PolicyConfig

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: score_policy_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: required_artifacts
      :type:  dict[str, list[str]]
      :value: Ellipsis



   .. py:attribute:: comparability
      :type:  dict[str, list[str]]
      :value: Ellipsis



   .. py:attribute:: thresholds
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: gate_policy_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: raw_data
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:function:: load_policy(policy_path, schemas_dir)

