# Signal Reliability Schema

Condensed schema contract for per-signal trustworthiness metadata.

**Derived from:** `signal_reliability_schema_v0_1_1.md`  
**Intent:** Preserve the actual schema boundary and behavioral rules, while removing ledger-style implementation inventory and excess companion prose from the schema document itself.

---

## 1. Purpose

The Signal Reliability Layer is a per-signal, per-timestamp metadata stream describing how trustworthy a signal's output is under current conditions.

It is not a return forecast.

It does not replace `confidence_scalar`.

It sits one level below allocator confidence: signal reliability is per-signal evidence; `confidence_scalar` remains the allocator-level post-sizing attenuation term.

---

## 2. Scored Object

The scored object is a tradeable signal output occupying an active `SignalCatalog` slot.

Concretely, each record is keyed by:

- `signal_id`,
- `slot_index`,
- `as_of`,
- `signal_set_version`.

This layer scores signals, not tasks, not regime labels, and not encoder coherence.

---

## 3. Producer and Placement

The exact producer is implementation-defined, but the contract assumes the following shape:

1. context or regime state is computed,
2. per-signal historical evidence is assembled,
3. a reliability scorer emits per-signal dimensions,
4. the allocator may optionally consume those dimensions,
5. governed artifacts emit the resulting report.

The reliability layer is downstream of context encoding and parallel to, or just upstream of, the allocator.

It is not part of the inner loop.

---

## 4. Advisory-Only Default

Phase II default semantics are advisory.

Signal reliability:

- may be emitted as metadata,
- may be consumed as optional allocator input,
- must not hard-drop signals by default,
- must not be promoted to hard gating without explicit evidence and an ADR.

This preserves consistency with the `confidence_scalar` contract.

---

## 5. Fast-State Schema

One `SignalReliabilityState` record is emitted per active signal per evaluation timestamp.

### 5.1 Required Identity Fields

- `signal_id: str`
- `slot_index: int`
- `as_of: datetime`
- `signal_set_version: int`
- `schema_version: str`

### 5.2 Required Reliability Dimensions

All dimensions are floats in `[0, 1]` with **higher = more reliable** polarity.

- `persistence`
- `slippage_sensitivity`
- `crowding_sensitivity`
- `turnover_burden`
- `regime_fragility`
- `crisis_retention`
- `signal_disagreement`
- `state_dependency`

### 5.3 Aggregate and Evidence Fields

- `reliability_score`
- `evidence_flags`
- `evidence_coverage`

### 5.4 Missing-Evidence Rule

If a dimension cannot be computed, it must fall back to a documented prior.

Default prior: `0.5`.

`evidence_coverage` must reflect how much of the record comes from actual evidence rather than prior values.

---

## 6. Slow-State Schema

One `SignalReliabilityCalibration` record is emitted per signal per calibration window.

### 6.1 Required Fields

- `signal_id`
- `slot_index`
- `calibration_window_start`
- `calibration_window_end`
- `fit_version`
- `signal_set_version`
- `schema_version`
- `dimension_weights`
- `weighting_method`
- `mean_reliability_by_regime`
- `reliability_ic_correlation`
- `calibration_task_count`
- `calibration_bar_count`
- `pit_boundary`

### 6.2 Optional Fields

- `persistence_half_life_bars`
- `crowding_proxy_source`
- `decay_rate_estimate`

The slow state exists to make weighting, fit provenance, and calibration quality inspectable.

---

## 7. Run-Level Artifact

The canonical emitted artifact is `signal_reliability_report.json`.

It should contain:

- top-level run identity,
- `as_of`,
- `signal_set_version`,
- all fast-state records for the run,
- a summary block,
- a calibration reference block.

The report belongs on the governed bundle path and should be content-addressable like other governed artifacts.

---

## 8. Relationship to Existing Contracts

### 8.1 `confidence_scalar`

`confidence_scalar` is allocator-level.

Signal reliability is per-signal.

Signal reliability may feed allocator confidence. It does not replace it.

### 8.2 `signal_embedding`

`signal_embedding` is about signal identity.

Signal reliability is about signal state under current conditions.

These are orthogonal concerns.

### 8.3 Regime or Context State

Regime or context state may be an input to dimensions such as fragility, crisis retention, or state dependency.

That does not make regime state itself the scored object.

### 8.4 Dynamic-K

Records are emitted only for active signals.

Retired or masked slots do not receive new fast-state records.

Historical calibration history should remain replayable.

---

## 9. Promotion Rule

The reliability layer is promoted from diagnostic-only metadata to allocator-consumed input only through ablation evidence.

### 9.1 Baseline Comparison

Treatment: allocator with reliability input  
Control: allocator without reliability input

### 9.2 Primary Test

Net walk-forward performance after costs on the same evaluation surface used by the allocator program.

### 9.3 Non-Degradation Constraints

Promotion must not degrade:

- crisis behavior,
- drawdown profile,
- confidence calibration.

### 9.4 Failure Outcome

If there is no net benefit, the reliability layer remains diagnostic-only.

That is not a schema failure. It is an honest program outcome.

---

## 10. Phase Placement

This is a Phase II support contract.

It resolves the data shape and behavioral semantics early so implementation can proceed without ambiguity, but it does not by itself authorize allocator changes, gating changes, or promotion claims.
