# Signal Governance Protocol

Consolidated governance surface for signal admission, promotion, retirement, expansion, and alternative-data admissibility.

**Derived from:** `signal_generation_protocol.md`, `signal_universe_expansion_policy.md`, and `alt_data_admissibility.md`  
**Intent:** Replace overlapping policy surfaces with one canonical protocol while preserving the original distinctions between eligibility, admission, promotion, and active-curriculum status.

---

## 1. Purpose

This protocol defines how candidate signals enter, remain in, and leave the governed signal universe, and how non-standard data sources become eligible for governed evaluation.

It consolidates three previously separate concerns:

1. signal admission / promotion / retirement,
2. signal-universe expansion from the narrow governed base,
3. alternative-data admissibility preconditions.

This protocol is intentionally strict about state transitions. A source becoming evaluation-eligible is not the same thing as a signal being admitted. Admission is not the same thing as promotion. Promotion is not the same thing as broadening the signal factory at scale.

---

## 2. Current Governed Base

**Active governed signals:**

- `momentum_xsec`
- `momentum_tsmom`
- `momentum_dual`
- `stat_arb_pairs`

The current base is narrow by design. Breadth expansion without governance controls degrades multiple-testing discipline, redundancy control, and decay visibility.

This document governs how that base may grow. It does not imply that broader breadth is already present, underway, or approved for Phase II.

---

## 3. State Model

Every signal exists in one of the following governed states.

### 3.1 Evaluation-Eligible Source

A data source has cleared the admissibility preconditions in Section 8 and may be used in governed evaluation runs.

**Important:** evaluation-eligible source is a source state, not a signal state.

### 3.2 Admitted Signal

A signal has satisfied the structural admission requirements in Section 4 and is registered in `SignalCatalog` with `active: false`.

### 3.3 Promoted Signal

A signal has passed the promotion and expansion gate in Section 6 and is explicitly moved to `active: true`.

### 3.4 Retired Signal

A signal is removed from active curriculum participation but remains in `SignalCatalog` with replay-traceable identity.

**Invariant:** no silent transitions. Admission, promotion, and retirement are explicit governance actions.

---

## 4. Signal Admission Requirements

A signal may not enter `SignalCatalog` or appear in any training task unless all of the following are satisfied.

| Requirement | Rule |
|---|---|
| Signal ABC | Must implement the governed Signal ABC with all required fields |
| SignalCatalog registration | Must receive a stable `signal_id` and `slot_index` |
| PIT-safe feature path | All features must be computed through governed `_OP_REGISTRY` ops over `DataView.as_of(T)` inputs |
| Screening evidence | Admission must emit `screening_report.json` through the governed path |
| Statistical validity | Must pass the canonical `stat_validity_report.json` gate |
| No dual execution path | Governed feature computation may not rely on direct `_FEATURE_OPS` execution |

Admission is a structural and governance check. It is not proof that the signal belongs in active curriculum.

---

## 5. Signal Identity and Provenance

| Field | Rule |
|---|---|
| `signal_id` | Canonical stable identifier. Never reused. |
| `slot_index` | Stable integer key. Assigned at registration. Never reused after retirement. |
| `signal_set_version` | Increments whenever the active signal set changes. Must be carried on replay and task surfaces. |

Additional identity rules:

- historical `slot_index` mappings must remain reconstructible for every `signal_set_version`,
- re-registering an existing `signal_id` is idempotent and must not mint a new `slot_index`,
- any change to `slot_index` assignment rules requires an ADR.

---

## 6. Promotion and Expansion Gate

A signal may move from admitted to active curriculum status only after satisfying all of the following.

### 6.1 Walk-Forward Statistical Validity

The candidate must clear all required evidence on the same governed evaluation bundle, split surface, and cost assumptions:

- Harvey t on walk-forward out-of-sample IC,
- DSR accounting for testing multiplicity,
- PBO under CPCV.

Passing Harvey t alone is insufficient.

### 6.2 Diversity Gate

Mean pairwise IC correlation between the candidate and each currently active signal must stay below the governed redundancy threshold.

A near-duplicate is rejected as redundant even if its standalone statistics look good.

### 6.3 Decay Policy

Promotion requires a documented decay-monitoring policy:

- metric,
- evaluation window,
- retirement trigger.

A signal without a decay policy is not promotable.

### 6.4 Multiple-Testing Budget

The expansion batch must record the total number of signals tested.

DSR and Harvey t must reference the true cumulative testing burden. Budget gaming through artificial batch splitting is not permitted.

### 6.5 Phase Scope

Phase II may admit and promote signals one at a time with full individual justification.

Phase IV is the first phase allowed to become signal-factory-serious.

---

## 7. Retirement Rules

A signal must be retired if any of the following occur:

- it fails the statistical validity gate on three or more consecutive governed runs,
- its feature implementation is found to violate PIT-safe DataView discipline,
- a governance review determines that its admission evidence was incorrect.

### 7.1 Retirement Procedure

1. Set `retired: true` in `SignalCatalog`
2. Record the rationale in a governance surface
3. Increment `signal_set_version`
4. Never reuse `slot_index`

Decay monitoring is not automatic retirement. Retirement requires explicit governance action.

---

## 8. Alternative-Data Admissibility

This section governs when a non-standard data source becomes eligible for governed evaluation.

### 8.1 Covered Source Types

Alternative data includes any source beyond the current governed price / volume / market-microstructure stack, including:

- non-tabular structured data,
- event-driven data,
- alternative tabular data,
- macro or non-market tabular data from non-price sources.

### 8.2 PIT Requirements

Every source must satisfy all of the following:

- every record carries `available_at`,
- historical evaluation uses only records with `available_at <= decision_ts`,
- access occurs through `DataView.as_of(T)` or a governed equivalent,
- historical vintages are preserved for revised datasets.

A pipeline that conflates event time with availability time is inadmissible.

### 8.3 Provenance Requirements

Every source must have:

- a stable versioned source identifier,
- content-addressable governed snapshots,
- lineage back to the governed DataView path,
- documented terms-of-use clearance before evaluation work begins.

### 8.4 Replay Requirements

Every governed run using alternative data must be replayable:

- deterministic replay with the same inputs,
- frozen state for query-time-dependent sources,
- versioned fixture for the evaluation window.

Fixture production is a precondition for evaluation, not a post-hoc convenience.

### 8.5 Event-Driven Sources

Event-driven data is not currently admissible.

Admitting event-driven data requires additional contract work covering:

- asynchronous event ordering with PIT semantics,
- idempotent processing guarantees,
- irregular time-series handling,
- a governed entry path compatible with `DataView.as_of(T)`.

This remains later-phase work.

### 8.6 Admissibility Decision Tree

A source is evaluation-eligible only if all of the following are true:

1. terms of use documented and cleared,
2. `available_at` timestamping confirmed,
3. PIT access path exists,
4. vintage preservation confirmed or not applicable,
5. deterministic replay fixture producible,
6. content-addressable snapshot feasible,
7. source identifier stable and versioned.

Clearing this section makes the source eligible for governed evaluation only. It does not admit a signal and does not promote anything to active curriculum.

---

## 9. Relationship Between Source Admissibility and Signal Promotion

The governing order is:

1. source admissibility,
2. signal admission,
3. promotion / expansion review.

That means:

- a source that fails admissibility may not enter governed evaluation,
- a source that clears admissibility still does not admit a signal,
- a signal built on an admissible source still must satisfy the structural admission gate,
- a structurally admitted signal still must satisfy the promotion / expansion gate before becoming active.

This ordering is the main reason these surfaces are now consolidated: the dependency chain is real and should live in one place.

---

## 10. What Is Not an Expansion Event

The following do not trigger the promotion / expansion gate by themselves:

- hyperparameter tuning of an existing signal that does not change `signal_id`,
- feature-op changes that do not change `signal_id`,
- alternative-data source review by itself.

If a change alters `signal_id`, it is a new signal candidate and re-enters the full governed path from the beginning.

---

## 11. Phase Boundaries

| Phase | Allowed scope |
|---|---|
| Phase II | Per-signal governed admission and promotion, one at a time |
| Phase III | No special breadth authority implied |
| Phase IV | Signal-factory-serious breadth, automation, and lifecycle controls |

The narrow governed base remains the current truth. Breadth at scale is later-phase work under explicit constraints.

---

## 12. Canonical Outputs and References

This protocol assumes the following governed evidence surfaces exist where relevant:

- `screening_report.json`
- `stat_validity_report.json`
- `SignalCatalog`
- `signal_id`
- `slot_index`
- `signal_set_version`

A future adoption pass can replace legacy cross-links by pointing companion documents to this consolidated protocol.
