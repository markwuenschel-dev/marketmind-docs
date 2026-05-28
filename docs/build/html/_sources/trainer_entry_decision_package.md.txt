# Trainer-entry decision package (MLC-3)

**Purpose:** Single governed surface that freezes trainer **premises** for implementation start: inner-loop **K**, default **algorithm**, **proxy-loss** commitment, and **Tier-1 entry waivers**. This is not GATE-II closure, not allocator promotion, and not proof of net uplift.

**Companion baseline:** Resolution Ledger v1.0.72 · Implementation Plan v6.5.28 · `VERSION.md` 7.3.20  
**Machine-readable:** [`artifacts/phase_ii/trainer_entry/trainer_entry_decision.json`](../../artifacts/phase_ii/trainer_entry/trainer_entry_decision.json)  
**RG-11 evidence:** [`rg11_k_budget_closeout.md`](rg11_k_budget_closeout.md)

---

## 1. Committed inner-loop K

- **K = 5** gradient steps per task (support set only for adaptation steps).  
- **Justification:** documented Phase II research-stage sweep and literature alignment in [`rg11_k_budget_closeout.md`](rg11_k_budget_closeout.md).  
- **Re-evaluation:** empirical comparison on K ∈ {1, 3, 5} remains a post-implementation obligation; it does not block the initial config default.

## 2. Committed default algorithm

- **Default:** `reptile` (Reptile / first-order meta-update on adapted-vs-meta parameter deltas).  
- **Config alternatives:** `anil` and `fomaml` may appear as frozen-config enum values for explicit ablation runs; the **default training lane** and reference tests target **reptile** until superseded by a later governed package.

## 3. Committed proxy loss (outer / inner training signal)

- **Family:** differentiable **ranking surrogate** (listwise or pairwise formulation) chosen to align optimization with **query-set Spearman IC** improvement, per Design Lock 4 / §0.3 claim 4 in [`MetaLearningCore.md`](MetaLearningCore.md).  
- **Exact implementation** (tensor shape, tie handling, optional pairwise vs listwise) is owned by MLC-3 code; this package commits the **objective class**, not a specific library call.  
- **Numerical Pearson alignment floor** (> 0.6 in Appendix A.2) remains a **Tier-1 empirical gate for promotion paths**, not a coding-start blocker (see waivers below).

## 4. Tier-1 waivers (implementation entry only)

One governed waiver is recorded in JSON as **`T1W-MLC3-ENTRY-001`**: Appendix A.2 Tier-1 rows may stay empirically **Open** in [`MetaLearningCore.md`](MetaLearningCore.md) while MLC-3 **implementation** proceeds. **Numerical Tier-1 closure remains mandatory** for language that implies trainer promotion, shadow entry, or GATE-II passage.

## 5. Explicit non-claims

- Does **not** close **GATE-II**.  
- Does **not** authorize **allocator promotion** or execution-serious rollout.  
- Does **not** strengthen **AQ-09** beyond existing **regime_embedding** conditioning-only policy.

## 6. Execution handoff

After this package and `mlc3_preflight_record.md` are merged, implement MLC-3 per **[`MLC3_Coding_Brief.md`](MLC3_Coding_Brief.md)**.
