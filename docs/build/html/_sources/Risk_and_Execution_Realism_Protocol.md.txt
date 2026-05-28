# Risk and Execution Realism Protocol

Consolidated boundary for allocator-to-risk semantics and Phase III paper-trading realism expectations.

**Derived from:** `risk_protocol.md` and `paper_trade_sim_spec.md`  
**Intent:** Keep the RiskFn contract separate from allocator validation, while demoting paper-trading realism notes from standalone doctrine to an appendix on future execution realism.

---

## 1. Purpose

This document defines:

1. what RiskFn may consume and do in Phase II,
2. what remains outside RiskFn and belongs to II-D or later execution layers,
3. the realism dimensions a future paper-trading simulation must respect so that research evidence is not confused with live readiness.

The key boundary is simple:

- RiskFn processes allocator output.
- II-D conditions that output for deployable capital expression.
- execution-realism infrastructure belongs later and remains conditional.

---

## 2. Allocator Output Surface

### 2.1 Permitted Inputs to RiskFn

- `allocation_weights` — simplex over active signals, produced by `meta_policy.py`
- `confidence_scalar` — scalar in [0, 1], produced by `meta_policy.py`

### 2.2 Informational Only

- `regime_class` — may be used for reporting and curriculum context, but must not alter sizing in Phase II

### 2.3 Explicitly Not Consumed by RiskFn in Phase II

- raw signal scores,
- feature vectors,
- any upstream model internals,
- `theta_meta`,
- `theta_task_prime`,
- inner-loop or trainer outputs.

**Rule:** RiskFn consumes the allocator's terminal surface, not its internal state.

---

## 3. Permitted Phase II Action

RiskFn's single governed Phase II action is post-sizing exposure attenuation via `confidence_scalar`.

```text
live_position = base_position × confidence_scalar
```

Where:

- `base_position` is the output of `SizingFn` applied to `allocation_weights`,
- `confidence_scalar ∈ [0, 1]`.

Full abstention corresponds to `confidence_scalar = 0`.

### 3.1 Hard Constraints

- RiskFn may only reduce exposure from base size.
- Levering above base size is not permitted in Phase II.
- `confidence_scalar` must not become a signal-selection gate without an ADR.
- RiskFn must not introduce opaque adjustments without a traceable audit path.

### 3.2 Allowable Uncertainty Controls

Sizing, participation, turnover, and abstention controls may be informed by `confidence_scalar` as long as all such controls remain exposure-reducing rather than exposure-increasing.

---

## 4. What RiskFn Does Not Own

The following remain outside RiskFn and belong to II-D or later deployment conditioning:

- turnover-budgeted target generation,
- liquidity and capacity scaling,
- drawdown and regime-conditioned overlays,
- structured constraints such as neutrality, CVaR, borrow or funding limits, and participation limits.

### 4.1 Why This Split Matters

A recurring failure mode is confusing deployment-layer conditioning wins for allocator validation.

If II-D overlays improve outcomes, that is evidence that deployment conditioning is doing useful work. It is not evidence that the allocator itself earned promotion.

This separation is load-bearing and should stay explicit.

---

## 5. Phase Scope Boundary

| Phase | RiskFn scope |
|---|---|
| Phase II | Interface boundary + post-sizing attenuation only |
| Phase III | Execution-serious calibration, operator enforcement, borrow/funding treatment, participation limits, fuller impact integration |

Phase II may define the boundary without implying Phase III realism is already built.

---

## 6. Auditability Requirements

RiskFn must emit a traceable sizing record per session, including:

- `confidence_scalar` as received,
- mean attenuation factor across active positions,
- most recent calibration ECE,
- reliability or calibration provenance reference,
- abstention events with reason codes.

These fields belong on governed evidence surfaces for Phase II runs.

---

## 7. Provisional Thresholds

The following remain evidence-owned rather than frozen constants:

- ECE recalibration trigger,
- mean `confidence_scalar` alert floor,
- rolling IC correlation floor for `confidence_scalar`,
- attenuation-curve parameterization.

No threshold here should silently become hard policy without governed resolution.

---

## Appendix A — Paper-Trading Simulation Requirements

This appendix captures the realism dimensions a future paper-trading simulation should satisfy. It is intentionally not a production contract yet.

### A.1 Purpose

Paper-trading simulation exists to reduce the gap between governed research evidence and deployable execution claims.

It does **not** imply broker integration, live routing, or allocator promotion.

### A.2 Required Realism Dimensions

A future simulation design should address at least:

- latency and partial fills,
- fees and slippage,
- borrow and short constraints where relevant,
- corporate actions,
- session boundaries and stale-quote handling.

### A.3 Utility After Frictions

Decision quality must be evaluated after the friction model is applied.

Utility should be measured on post-friction paths so that paper alpha is not overstated relative to deployable edge.

### A.4 Explicit Out of Scope

This appendix does not cover:

- live or paper broker API integration,
- credentials or routing,
- promotable allocator semantics,
- any claim that Phase II is execution-ready.

### A.5 Phase Placement

Full paper-trading productization belongs to Phase III and remains conditional on prior governance and validation gates.

That conditionality is part of the protocol, not a footnote.
