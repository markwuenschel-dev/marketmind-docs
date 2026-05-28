# Version History

This file serves as the project's release ledger and architecture evolution.

---

## Version Index

### 7.x — Adjusted-data allocator research, W3 clean-surface routing, and Phase II broad reset

- **7.7.0-draft** — Broad Phase II reset after the first narrow W4-B learned-router diagnostic failed. Records W4-B as `FAILED_NARROW_DIAGNOSTIC`, opens P2-MAP → P2-MATRIX → P2-NARROW → P2-PORTFOLIO, and documents multi-family model/signal/target/rule breadth before survivor portfolio expression.
- **7.6.0-draft** — Companion-document realignment after W3 closure. Records W3-A through W3-D outcomes, corrects router language to recent-winner child-policy selector, opens **W4-A — Router Opportunity Audit** before portfolio expression, and adds the W3-D row-level emission governance lesson.
- **7.5.0-draft** — Companion-document reset after adjusted Polygon/Massive W3-A routing run. Renames legacy `W2-v3M` work to **W3-A — Clean-Surface Allocator Routing Prototype**, records W2 as closed benchmark/data-quality phase, records adjusted-panel evidence, and sets **W3-AH Harness Audit** as the immediate next step.
- **7.4.0** — Repo-bloat reduction, storage-governance update, W2-v1 fixture baseline-floor evidence.
- **7.3.21** — W1 diagnostic-only reclassification and W2/W3/W4 scope-separated forward lanes.

Older detailed release entries remain in archived release files or prior `VERSION.md` history.

---

## Version 7.7.0-draft (2026-05-26)

Changelog for broad Phase II architecture reset after the first narrow W4-B learned-router diagnostic failed.
Version: 7.7.0-draft (W4-B failed narrowly; broad Phase II map/matrix/narrow/portfolio funnel is active)

### Major themes

- **W4-B classified:** The first narrow learned-router prototype is recorded as `FAILED_NARROW_DIAGNOSTIC`, not as a final rejection of broad routing. The selected model was Elastic Net; learned-router test utility was 115.063 versus best standalone child utility 131.387.
- **Gate inconsistency documented:** W4-A artifacts retained `w4b_gate.open=false` from the original row-oracle uplift rule, while the later date-level override made that rule diagnostic-only. The ledger now treats this as a sequencing inconsistency, not a primary-measurement failure.
- **Broad reset opened:** Active Phase II work is now **P2-MAP → P2-MATRIX → P2-NARROW → P2-PORTFOLIO**. Portfolio expression is reserved for controlled survivors.
- **Model and signal breadth recorded:** The docs now require Ridge, Elastic Net, Bayesian Ridge, Bayesian LASSO / sparse Bayesian proxy, Group LASSO, Sparse Group LASSO, PCR / PLS, XGBoost, Random Forest / ExtraTrees, quantile regression, contextual bandit, and mixture-of-experts coverage, with MAML / Reptile-style adaptation later-stage only.
- **Target and rule breadth recorded:** Router targets now include child utility regression, child utility distribution, pairwise child-vs-best-child advantage, override probability, abstain probability, and regime classifier plus policy map. Decision rules now include free routing, default-to-best-child override, confidence-bound override, Thompson-style sampling, risk-adjusted expected utility, and drawdown-aware selection.
- **Input scope expanded:** TA child, regime/liquidity/volatility, cross-asset, macro, sentiment/news, crypto-specific, and alternative-data features are documented. Missing PIT-safe inputs must be marked blocked, not silently omitted.

### Companion document versions

| Document | New version |
|---|---:|
| README.md | 7.7.0-draft |
| WhitePaper.md | 7.7.0-draft |
| ImplementationPlan.md | 6.8.0-draft |
| TechnicalRoadmap.md | 1.7.0-draft |
| MetaLearningCore.md | 1.6.0-draft |
| MetaLearningArchitectureVision.md | 1.6.0-draft |
| PhaseIIArtifactContract.md | 1.3.0-draft |
| PhaseIIResearchExecutionPlaybook.md | 1.3.0-draft |
| ResolutionLedger.md | 1.3.0-draft |
| ThresholdGovernanceRegister.md | 1.2.0-draft |
| VERSION.md | 7.7.0-draft |

### Artifact contract additions

Draft broad Phase II artifact surfaces are now documented:

```text
architecture_map
candidate_matrix
model_family_registry
signal_family_registry
surface_market_registry
narrowing_report
survivor_manifest
portfolio_expression_report
```

New broad-reset classification values:

```text
FAILED_NARROW_DIAGNOSTIC
BROAD_MATRIX_OPEN
NARROWED_OUT_BASELINE
NARROWED_OUT_ROBUSTNESS
SURVIVOR_READY_FOR_PORTFOLIO
```

Existing W4 portfolio expression labels remain the final survivor-expression labels.

### Behavioral changes

No runtime behavior changes are claimed by this documentation update.

### Breaking changes

Narrative docs no longer describe W4 portfolio expression as the immediate next step for all W2/W3 candidates. The current sequence is broad map, broad candidate matrix, controlled narrowing, then portfolio expression for survivors.

### Deferred

- DOCX regeneration and strict SemVer release packaging.
- Runtime implementation of the broad Phase II matrix and narrowing artifacts.
- Portfolio expression for any candidate not classified `SURVIVOR_READY_FOR_PORTFOLIO`.
- Later-stage MAML / Reptile-style adaptation.
- GATE-II closure, execution-ready rollout, paper/live/broker paths.

---

## Version 7.6.0-draft (2026-05-21)

Changelog for companion-document realignment after W3 closure and W4 kickoff.
Version: 7.6.0-draft (W3 closed; W4 portfolio expression is the active next lane)

### Major themes

- **W3 closed:** W3-A through W3-C recorded as closed lanes; W3-D recorded as `STOPPED_DEFERRED` / `INCONCLUSIVE` due to replay-validation failure. `RES-W3B-FROZEN-LINEAGE-CORRECTION` adopts the locally reproducible regenerated W3-B Surface B value (131.386685) because the prior 153.148530 ledger value is not artifact-backed in the current workspace.
- **W4 opened:** **W4 — Portfolio-Level Allocator Expression** is the active next lane. Current work is portfolio survivability (sizing, costs, turnover, liquidity/capacity, concentration, drawdown), not more W3 work, W3-D replay debugging, liquidity-penalty tuning, or router patching.
- **Router language corrected:** The W3 router is documented as a **recent-winner child-policy selector**, not a learned meta-router. W3-B validated child-policy signal, not independent router skill. Learned routing is deferred to a separately scoped W5+ lane conditional on W4 outcome and a credible oracle gap.
- **W3-D governance lesson:** Row-level selected decisions must be emitted at run time; post-hoc reconstruction drift invalidated the W3-D mechanism audit. Artifact Contract and Playbook updated accordingly.
- **Strategic interpretation locked:** W3 found real but fragile child-policy signal. W3 did not prove tradable alpha. W3 did not prove independent router skill. The recent-winner router is a weak baseline only.
- **W4-A date-level override:** `RES-W4A-DATE-LEVEL-OPPORTUNITY-OVERRIDE` demotes row-oracle uplift to diagnostic-only so W4-B can open for date/context-level learned-router prototypes when primary measurement is valid.

### Recorded W3 outcomes (key values)

| Lane | Status | Headline |
|---|---|---|
| W3-A | `CLOSED_REPAIRED_BASELINE` | Surface repair worked; best child strong (111.415); router weak (32.388) |
| W3-B | `CLOSED_TA_RESULT_CONCENTRATED` | pandas-ta improved child layer; lineage-corrected Surface B 131.387; Surface D 9.501 |
| W3-C | `CLOSED_W3C_NO_RECOVERY` | Liquidity score-time penalty damaged B (0.5955 retention); Surface B 91.199; Surface D 9.068 (D worsened slightly / no recovery) |
| W3-D | `STOPPED_DEFERRED` | INCONCLUSIVE — replay drift invalidated audit; do not resume before W4 |
| W4 | `OPEN_NEXT` | Portfolio-level allocator expression |

### Companion document versions

| Document | New version |
|---|---:|
| README.md | 7.6.0-draft |
| WhitePaper.md | 7.6.0-draft |
| ImplementationPlan.md | 6.7.0-draft |
| TechnicalRoadmap.md | 1.6.0-draft |
| MetaLearningCore.md | 1.5.0-draft |
| MetaLearningArchitectureVision.md | 1.5.0-draft |
| PhaseIIArtifactContract.md | 1.2.0-draft |
| PhaseIIResearchExecutionPlaybook.md | 1.2.0-draft |
| ResolutionLedger.md | 1.2.0-draft |
| VERSION.md | 7.6.0-draft |

### Documentation corrections (7.6.0-draft review fixes)

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | W3-C dashboard row: Surface D wording corrected from "D unchanged" to "D worsened slightly / no recovery" |
| `docs/src/ResolutionLedger.md` | W3-D artifact path standardized to `artifacts/phase_ii/w3_d_surface_d_failure/...` |
| `docs/src/ResolutionLedger.md` | Added RES-W3B-FROZEN-LINEAGE-CORRECTION: prior Surface B 153.148530 is not artifact-backed locally; regenerated 131.386685 lineage is canonical for W4-A parity |
| `docs/src/PhaseIIArtifactContract.md` | W4-A provenance must disclose lineage correction source and legacy frozen value when corrected W3-B anchors are used |
| `docs/src/TechnicalRoadmap.md` | W4 pandas-ta guidance tightened: carry forward W3-B candidate outputs; use frozen KEEP/INVERT/DROP decisions only if W4 must recompute child-policy scores |
| `docs/src/WhitePaper.md` | §4 reframed so W4 portfolio survivability is the current thesis; meta-learning and learned routing explicitly conditional on W4 + oracle gap (W5+) |

### Current evidence references

| Artifact | Role |
|---|---|
| `artifacts/phase_ii/w3_b_pandas_ta/...` | W3-B pandas-ta child policies, router, summary |
| `artifacts/phase_ii/w3_c_liquidity_child/...` | W3-C liquidity-aware child penalty results |
| `artifacts/phase_ii/w3_d_surface_d_failure/...` | W3-D audit JSON + summary (INCONCLUSIVE) |
| `adjusted_panel_inventory.json` | Adjusted-data inventory |
| `surface_summary.json` | W3-A surface definitions and row counts |
| `child_policy_report.json` | Child-policy metrics by surface |
| `w2_v3m_router_report.json` | Legacy-named W3-A router report |
| `w2_v3m_summary.md` | Legacy-named W3-A summary |

### Behavioral changes

No runtime behavior changes are claimed by this documentation update.

### Breaking changes

Narrative docs no longer treat W3 as active work or the recent-winner router as a learned meta-router. W3-D artifact references use `w3_d_surface_d_failure` as the canonical path name.

### Deferred

- W3-D replay-fidelity debugging and mechanism audit resumption (blocked until W4; requires run-time `selected_decisions.parquet` emission).
- Recent-winner router extension or patching.
- W5+ learned routing (conditional on W4 portfolio survivability and demonstrated oracle gap).
- GATE-II closure, execution-ready rollout, paper/live/broker paths.

---

## Version 7.5.0-draft (2026-05-09)

Changelog for companion-document reset after the adjusted Polygon/Massive clean-surface routing run.

### Major themes

- **Current work renamed:** legacy `W2-v3M` is now treated as **W3-A — Clean-Surface Allocator Routing Prototype**.
- **W2 phase closed conceptually:** W2 established the benchmark and exposed the artifact-driven XGBoost result; current work is no longer W2.
- **Adjusted data recorded:** Polygon/Massive US Stocks SIP adjusted daily panel, 2021-05-10 through 2025-12-31, 12,700,323 rows, 19,291 instruments, 1,168 trading days.
- **W3-A result recorded:** Surface B clean result is negative for current child policies; Surface C shows residual signal but simpler policies beat the router; Surface A remains diagnostic because it still exposes artifact-like/concentrated utility.
- **Interpretation made provisional:** the negative clean-surface result is not accepted as final signal failure until W3-AH audits labels, score direction, top-k orientation, filter semantics, and child-policy score paths.
- **Next work:** W3-AH Harness Audit, followed by W3-B Signal / Child-Policy Repair only if the audit clears the harness.
- **Governance language reduced:** prototype research requires experiment hygiene and reproducible artifacts, not production-style promotion language.

### Companion document versions

| Document | New version |
|---|---:|
| README.md | 7.5.0-draft |
| ImplementationPlan.md | 6.6.0-draft |
| TechnicalRoadmap.md | 1.5.0-draft |
| MetaLearningCore.md | 1.4.0-draft |
| MetaLearningArchitectureVision.md | 1.4.0-draft |
| PhaseIIArtifactContract.md | 1.1.0-draft |
| PhaseIIResearchExecutionPlaybook.md | 1.1.0-draft |
| ResolutionLedger.md | 1.1.0-draft |
| VERSION.md | 7.5.0-draft |

### Current evidence references

| Artifact | Role |
|---|---|
| `adjusted_panel_inventory.json` | adjusted-data inventory |
| `surface_summary.json` | surface definitions and row counts |
| `child_policy_report.json` | child-policy metrics by surface |
| `w2_v3m_router_report.json` | legacy-named W3-A router report |
| `w2_v3m_summary.md` | legacy-named W3-A summary |

### Behavioral changes

No runtime behavior changes are claimed by this documentation update.

### Breaking changes

The docs intentionally stop treating W2 as the active current lane. Existing artifact paths may still contain `w2_v3m` for compatibility, but narrative docs should refer to that experiment as W3-A.

### Deferred

- W3-AH harness audit implementation.
- W3-B signal and child-policy repair.
- Any advanced meta-learning/router expansion.
- Any paper/live/broker/execution path.

---

## Prior release note

For full historical detail before 7.5.0-draft, use the previous `VERSION.md` or archived release documents. This replacement keeps the current docs focused on the active research state rather than carrying every old ledger entry forward.
