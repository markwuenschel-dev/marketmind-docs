# Task Validity Pilot Report

Canonical pilot-design and evidence-report surface for task leakage safety and non-exchangeability.

**Derived from:** `task_validity_pilot_report.md`  
**Intent:** Keep this document separate because it is an evidence/report surface rather than a general governance protocol.

---

## 1. Purpose

This report records whether MarketMind tasks are leakage-safe and non-exchangeable enough to justify trainer commitment.

Until populated with actual run results, this document remains a pilot-design shell rather than evidence of passage.

Publication of the design does not imply trainer commitment.

---

## 2. Questions the Pilot Must Answer

### 2.1 Support / Query Boundaries

Are support and query boundaries leakage-safe under the planned task geometry?

The pilot should evaluate:

- purge gap equal to label horizon `H`,
- embargo behavior,
- admissibility rules,
- fit-on-support-only preprocessing in leakage audit.

### 2.2 Non-Exchangeability

Do regime-indexed tasks behave as non-exchangeable learning units rather than interchangeable windows?

The pilot should include:

- statistical evidence,
- structural separability evidence,
- functional evidence,
- comparison against required null families.

### 2.3 Null Collapse

Do the null distributions collapse relative to real episodes as expected?

Required null families include:

- shuffled labels,
- shuffled regime assignments,
- exchangeable windows.

### 2.4 Hidden Assumptions

Are unresolved assumptions still preventing honest trainer commitment?

This includes:

- threshold placeholders,
- task-identity assumptions,
- boundary-confidence policy,
- crisis-labeling assumptions,
- explicit kill criteria and fail codes.

---

## 3. Minimum Evidence When the Harness Runs

A populated report should include at least:

- leakage-geometry diagnostics,
- non-exchangeability results across the required evidence families,
- baseline comparison notes where relevant,
- explicit handling of unresolved provisional thresholds,
- an explicit recommendation: proceed, narrow, or stop.

---

## 4. Threshold and Assumption Crosswalk

The report should map provisional thresholds to their governing assumption IDs rather than allowing free-floating placeholders.

Typical topics include:

- permutation p-value / structural ratio / Harvey t,
- embargo,
- support and query row counts,
- label confidence,
- episode and transition counts,
- dwell time,
- crisis-severity projection.

Numeric defaults should live in a versioned config artifact rather than silently hardening into architecture constants here.

---

## 5. Low-Confidence Boundary Policy

For the v1 pilot, low-confidence boundary episodes are hard-excluded.

That exclusion policy is fixed for the pilot surface. Calibration of the boundary-confidence threshold itself may remain provisional elsewhere, but this report should not treat the exclusion rule as a casual tuning knob.

---

## 6. Phase Relationship

| Phase | Ownership |
|---|---|
| Phase I-G | Pilot design, gate specification, replay-fixture and proof-burden documentation |
| Phase II-0 | Reproducible harness, gate execution, and population of actual results |
| Phase II | Trainer commitment only if the gate result truly unlocks it |

This document is separate because it is the evidence/report surface that later phases populate.

---

## 7. Governing References

A fully adopted version of this report should continue to point to:

- the RG-09 gate specification,
- the pilot config artifact,
- the replay-fixture specification,
- the determinism-boundary contract.

Those references remain important because this report is an evidence consumer, not the owner of all underlying semantics.
