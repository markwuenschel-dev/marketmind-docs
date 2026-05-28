# MarketMind README

<!-- MM:BEGIN:TITLEPAGE -->
Version 7.7.0-draft · May 2026 · Proprietary

Companion documents: Implementation Plan v6.8.0-draft · Technical Roadmap v1.7.0-draft · Meta-Learning Core v1.6.0-draft · Meta-Learning Architecture Vision v1.6.0-draft · Resolution Ledger v1.3.0-draft · Threshold Governance Register v1.2.0-draft · VERSION.md 7.7.0-draft
<!-- MM:END:TITLEPAGE -->

<!-- MM:BEGIN:DOCBODY -->

## Table of Contents

- [1. Overview](#1-overview)
  - [1.1 North Star](#11-north-star)
  - [1.2 What Exists Today](#12-what-exists-today)
  - [1.3 What Is Still Experimental](#13-what-is-still-experimental)
- [2. Working Pipeline](#2-working-pipeline)
- [3. System Skeleton](#3-system-skeleton)
  - [3.1 Current Architecture](#31-current-architecture)
  - [3.2 Proposed Meta-Learning Runtime](#32-proposed-meta-learning-runtime)
  - [3.3 Why the Allocator Is Not Yet the Product](#33-why-the-allocator-is-not-yet-the-product)
- [4. Architecture Overview](#4-architecture-overview)
  - [4.1 Key Architectural Ideas](#41-key-architectural-ideas)
  - [4.2 Operational Guarantees](#42-operational-guarantees)
  - [4.3 Validation-First Meta-Learning Framing](#43-validation-first-meta-learning-framing)
- [5. Getting Started](#5-getting-started)
  - [5.1 Run the Current Pipeline](#51-run-the-current-pipeline)
  - [5.2 Common Tasks](#52-common-tasks)
  - [5.3 Main Source Areas](#53-main-source-areas)
  - [5.4 Practical Repo Truth](#54-practical-repo-truth)
- [6. Quality, Testing, and Governance](#6-quality-testing-and-governance)
  - [6.1 Testing Standards](#61-testing-standards)
  - [6.2 Promotion Mindset](#62-promotion-mindset)
- [7. Companion Documents](#7-companion-documents)
- [8. Canonical Release Ledger](#8-canonical-release-ledger)

# 1. Overview

MarketMind is a production-minded algorithmic trading research and execution system built around one durable thesis: markets are non-stationary, so long-lived edge depends on learning when weak, diverse signals are conditionally usable, when they should be ignored or abstained from, and how selected signals should be expressed as regimes shift.

The current platform already provides the governed substrate required to test that thesis honestly: point-in-time data handling, leakage-aware validation, deterministic artifacts, statistical gatekeeping, and canonical bundle provenance. What it does **not** yet provide is a promoted adaptive allocator, a closed **GATE-II** path, execution-ready deployment, or live-approved adaptive control. The current Phase II direction is a broad architecture map, multi-family candidate matrix, controlled narrowing, and portfolio expression for survivors.

This distinction matters. MarketMind is not trying to win by hand-waving around “AI for trading.” It is trying to build a system that can:

- produce auditable research artifacts,
- reject weak or non-reproducible results,
- preserve point-in-time correctness,
- and only promote more adaptive machinery when it actually beats simpler alternatives under realistic constraints.

The companion documents frame the project around a few core questions:

- **Canonical thesis:** a governed adaptive alpha system may learn when weak signals are usable, when they should be ignored or abstained from, and how selected signals should be expressed under regime, cost, uncertainty, and execution constraints.
- **Null hypothesis:** a simpler regime-conditioned baseline can match or exceed any adaptive mechanism once cost, robustness, and operational burden are counted.
- **Core decomposition:** `Research Substrate -> Architecture Map -> Candidate Matrix -> Controlled Narrowing -> Survivor Portfolio Expression`
- **Five claims to prove:** task non-exchangeability, adaptation usefulness, encoder coherence, proxy alignment, and continual robustness, with signal usability and abstention quality treated as first-class empirical objects.
- **Promotion boundary:** allocator-level promotion is considered only after W2-or-later evidence beats the relevant baseline and satisfies the required empirical acceptance criteria.
- **Kill boundary:** the adaptive-learning path is narrowed or abandoned if simpler governed systems win or the required evidence does not materialize.

That gives the repo a cleaner identity: the current product is the governed research substrate, while adaptive allocation and expression remain governed research targets rather than earned product claims.

## 1.1 North Star

The long-term system vision now has five primitives:

| Primitive | Role | Current State |
|---|---|---|
| Signal Factory | Governed engine that creates, catalogs, screens, promotes, and retires candidate signals and strategy slices | Partially implemented through `StrategyRegistry`, SignalCatalog substrate, screening artifacts, and governed strategy slices |
| Signal Usability Layer | Governed layer that learns whether signals are usable, unusable, or should be abstained from under current context and frictions | Research target only; diagnostic framing is introduced ahead of W2 via W2-SU |
| Candidate Matrix | Broad model / signal / target / decision-rule grid across PIT-safe surfaces | Active Phase II reset |
| Controlled Narrowing | Predeclared filtering by uplift, robustness, leakage, concentration, liquidity, cost, drawdown, and falsification | Active Phase II reset |
| Expression Layer | Governed conversion of survivor intent into constrained capital expression under cost, uncertainty, and execution realism | Conditional on `SURVIVOR_READY_FOR_PORTFOLIO` |

Those primitives still define the system skeleton, but they no longer imply implementation maturity. Only the substrate portions that truly exist today are described as delivered.

## 1.2 What Exists Today

The implemented platform is strongest where research truthfulness matters most. MarketMind already has:

- a canonical bundle-producing orchestration path,
- point-in-time-safe data access on the governed path,
- governed feature execution through a canonical planner / executor route,
- artifact registry identity and run-state management,
- completed non-promotable Phase II-0 governance, artifact-contract, and pilot-harness foundations,
- bounded MLC evidence harnesses for task validity, trainer behavior, proxy alignment, and continual-learning diagnostics,
- W1, W2, W2-SU, and W3 research evidence that is useful but explicitly non-promotable,
- an open broad Phase II reset that maps architecture breadth, builds a candidate matrix, narrows candidates under predeclared checks, and reserves portfolio expression for survivors,
- governed strategy slices such as `stat_arb_pairs` and momentum work,
- screening, statistical-validity, and execution-assumptions artifact surfaces,
- leakage-aware tests, determinism discipline, and CI gates,
- and companion documents that separate current truth from future intent.

In other words, the repo already has serious infrastructure. What is missing is not basic engineering hygiene. What is missing is the evidence required to justify governed adaptive selection and, only later, a more ambitious allocator.

## 1.3 What Is Still Experimental

Several important ideas are intentionally still treated as unearned:

- the meta-learning allocator itself,
- the signal-usability layer and abstention logic as promotable governed machinery,
- encoder-driven task adaptation,
- advanced uncertainty-aware routing behavior,
- execution-serious deployment layers,
- and broad signal-factory automation at scale.

The project is deliberately structured so those remain future-facing until the evidence says otherwise.

The forward lane separation is:

```text
W1/W2/W3 closed evidence -> W4-A diagnostic -> W4-B failed narrow diagnostic -> P2-MAP -> P2-MATRIX -> P2-NARROW -> P2-PORTFOLIO for survivors
```

`W2-SU` remains signal-level and diagnostic-only. W4-B did not prove broad routing failure; it proved the first narrow learned-router attempt did not beat the best standalone child. No allocator superiority, allocator rejection, or **GATE-II** readiness follows from that diagnostic.

Phase II-0 remains a completed non-promotable governance and pilot-harness foundation. It improves auditability and fail-closed behavior, but it does not authorize trainer commitment, allocator promotion, broker wiring, paper trading, or execution-serious rollout.

# 2. Working Pipeline

The current governed platform is already useful because a single command can produce an auditable bundle:

```bash
python -m pysrc.bridge.java_entry tests/fixtures/sample_spy.csv --fast-sma 5 --slow-sma 10
```

Representative outputs include:

- `plan.json` for run configuration and plan identity
- `env_fingerprint.json` for interpreter, git, system, and dependency evidence
- `dataset_manifest.json` for data provenance and lineage
- `cleaning_plan.json` for normalized governed cleaning specs, step identity, determinism tier, and registry fingerprint
- `cleaning_report.json` for executed cleaning steps, mutation summaries, validation outcomes, and fallback events
- `preprocessing_report.json` for pipeline diagnostics
- `splits_manifest.json` for train/test split details
- `gate_result.json` for PASS / FAIL reasoning

That is a meaningful product surface by itself. The platform can already emit evidence-rich bundles, not just backtest output.

From Phase II-0 forward, pilot runs may emit scaffolded `task_manifest.json` and `meta_validity_report.json`. Governed `meta_validity_report` paths may include a **`confidence_calibration`** block (attenuation default; fail-closed validation). From Phase II onward, those artifacts become part of the promotable gate path whenever the meta-learning stack is exercised.

# 3. System Skeleton

## 3.1 Current Architecture

Today, the real platform is best summarized as:

```mermaid
flowchart LR
    A[Sources] --> B[PIT-safe adapters]
    B --> C[Canonical feature planner / executor]
    C --> D[Backtesting engines]
    D --> E[Statistical and governance gates]
    E --> F[Canonical bundles]
    F --> G[Artifact Registry]
    F --> H[RunRegistry]
```

That path is the trusted substrate on which later adaptive-learning work must be built. It is already meaningful on its own because it enforces lineage, policy, and current-state truthfulness.

## 3.2 Proposed Meta-Learning Runtime

If the empirical program succeeds, the intended runtime shape becomes:

```mermaid
flowchart TD
    A[DataView.as_of(T)] --> B[Feature ops + regime context]
    B --> C[Context encoder]
    C --> D[regime_embedding z]
    D --> E[Signal library / active slot mask]
    E --> F[Model / target / decision-rule matrix]
    F --> G[Controlled narrowing]
    G --> H[Survivor manifest]
    H --> I[Portfolio expression]
    I --> J[Risk and execution layers]
```

Several points matter here:

- `MetaTask` is the canonical learning unit, not “strategy” or “signal.”
- `regime_id` is the primary high-granularity task identity, while `regime_class` is the coarser projection used for curriculum and reporting.
- `theta_meta`, `theta_task_prime`, and `theta_day_prime` are distinct lifecycle objects and should not be collapsed casually in prose or code.
- Dynamic signal coverage uses fixed-slot masking so replay, gating, and promotion remain comparable.
- `confidence_scalar` defaults to post-sizing attenuation rather than magical control over the whole system.

## 3.3 Why the Allocator Is Not Yet the Product

The allocator is the intended product candidate, but not the current product reality.

Today’s value is the governed research substrate:

- it can produce trustworthy bundles,
- it can prevent obvious leakage and provenance failures,
- it can enforce policy on governed strategy slices,
- and it can tell the team whether a future allocator actually deserves promotion.

That “tell the truth before scaling up” posture is one of MarketMind’s core differentiators.

# 4. Architecture Overview

## 4.1 Key Architectural Ideas

Several platform ideas remain important even before the adaptive-learning stack exists:

- **Registry-driven plugin pipelines.** Cleaning, feature, strategy, and validation surfaces are composed through typed registries rather than ad hoc wiring.
- **Single front-door orchestration.** `py.pipeline.orchestrator` owns governed run order, identity, manifests, and artifact stitching while stage packages own their own execution runtimes.
- **Functional core / imperative shell.** Strategy logic and feature transforms are pushed toward pure computation while I/O, clocks, broker interaction, and mutable execution state stay outside that core.
- **Canonical IR pipeline.** The long-term target remains a staged pipeline from MarketData → Features → Alpha → Targets → Orders → Fills → Ledger.
- **Artifact provenance.** Canonical hashing and immutable artifact identity ensure promotion claims can be reconstructed and audited.
- **Multi-fidelity validation.** Lower-cost research paths should graduate to higher-fidelity evaluation only when transfer evidence justifies it.

## 4.2 Operational Guarantees

These guarantees remain non-negotiable regardless of the final allocator:

- **Point-in-time correctness:** all mutable data access must respect `DataView.as_of(T)`.
- **Determinism tiers:** governance-sensitive outputs require explicit determinism contracts.
- **Artifact provenance:** promoted runs must be reconstructible from canonical bundle artifacts.
- **Statistical rigor:** DSR, PBO, Harvey-style evidence, and Anti-Goodhart discipline are part of the promotion story.
- **No silent fallbacks:** failures on governed paths should fail closed with actionable diagnostics.

## 4.3 Validation-First Meta-Learning Framing

The proposed adaptive-learning design is not just “adaptive weighting with fancier names.” It changes the unit of learning and therefore the type of evidence required:

- tasks are regime-bounded episodes with support / query semantics,
- encoder quality becomes a first-class validation topic,
- inner-loop gain must be demonstrated rather than assumed,
- proxy alignment must be tested because the training loss is not identical to the reporting metric,
- and continual-learning controls must preserve robustness rather than merely enable frequent updates.

# 5. Getting Started

## 5.1 Run the Current Pipeline

```bash
python -m pysrc.bridge.java_entry tests/fixtures/sample_spy.csv --fast-sma 5 --slow-sma 10
```

## 5.2 Common Tasks

```bash
pytest tests/python/
```

```bash
mypy pysrc/
```

```bash
python -m pysrc.cli.gate validate <bundle_dir>
```

## 5.3 Main Source Areas

| Path | Purpose |
|---|---|
| `pysrc/artifact_registry/` | Canonical CAS storage and RunRegistry |
| `pysrc/backtesting/` | Engines, validation, storage/report seams |
| `pysrc/cli/` | Gate CLI and related entrypoints |
| `pysrc/pipeline/` | Canonical orchestration and stage execution |
| `pysrc/preprocessor/` | Canonical preprocessing contracts, planner / executor surfaces, and governed compatibility shims |
| `pysrc/registry/` | SignalCatalog and screening/report substrate |
| `pysrc/strategies/` | Governed strategy implementations and registry surfaces |
| `tests/python/` | Unit, integration, and property tests |
| `docs/src/` | Markdown source for the companion suite |

## 5.4 Practical Repo Truth

The codebase is substantially more mature than an “experimental trading repo” description would suggest. There is already real work in:

- strategy registration and governed bundle production,
- artifact registry identity and run state management,
- splits, purge / embargo discipline, and leakage-focused property testing,
- statistical validity and execution assumptions on the canonical gate path,
- and the beginning of governed signal-identity infrastructure through SignalCatalog and `slot_index`.

The main missing pieces are not basic engineering hygiene. They are the broad Phase II matrix, controlled survivor evidence, portfolio-expression evidence for survivors, broader execution scope, and the evidence required to justify any of those expansions.

# 6. Quality, Testing, and Governance

## 6.1 Testing Standards

- New tests must carry determinism tier markers (`d0`–`d3`).
- Randomized tests must use the deterministic seed fixture rather than ad hoc seeding.
- The suite expects strict typing, precise exception handling, and no debug `print()` in production code.
- Governance-sensitive outputs should aim for D0 or clearly justified D1 / D2 behavior depending on artifact type.

## 6.2 Promotion Mindset

MarketMind’s governance model is built around a few recurring questions:

1. Is the artifact or model **truthful** about current implementation state?
2. Is the result **reproducible** from canonical inputs and artifacts?
3. Has it **beaten the relevant baseline** under realistic constraints rather than by narrative force?
4. If it fails, do the artifacts make rollback or kill decisions straightforward?

That mindset applies equally to runtime code, gate policy, and documentation.

# 7. Companion Documents

This README is the suite entrypoint, not the full specification.

- **README.md** — suite entrypoint, practical repo truth, current-state framing, and navigation
- **Implementation Plan** — executable implementation path, deliverables, and gate structure
- **Technical Roadmap** — strategic build order and dependency-aware roadmap
- **Meta-Learning Core** — empirical validation program and acceptance hierarchy
- **Meta-Learning Architecture Vision** — runtime shape, interfaces, and validation-gated defaults
- **Resolution Ledger** — workflow state, normative locks, and decision tracking
- **Threshold Governance Register** — threshold identity, validation state, and enforcement discipline

<!-- MM:BEGIN:DOCMAP -->

| Document | Version | Role |
|---|---:|---|
| README.md | 7.7.0-draft | Suite overview, current status, and navigation |
| Implementation Plan | 6.8.0-draft | Executable implementation path, deliverables, and phase gates |
| Technical Roadmap | 1.7.0-draft | Strategic build order and dependency-aware roadmap |
| Meta-Learning Core | 1.6.0-draft | Research supplement defining task schema, model matrix, controlled narrowing, and acceptance criteria |
| Meta-Learning Architecture Vision | 1.6.0-draft | High-level architectural vision and system framing |
| Resolution Ledger | 1.3.0-draft | Resolution ledger and workflow state dashboard |
| Threshold Governance Register | 1.2.0-draft | Threshold identity, validation state, and enforcement discipline |
| VERSION.md | 7.7.0-draft | Canonical release ledger |

<!-- MM:END:DOCMAP -->

# 8. Canonical Release Ledger

Release history and release manifests live in `VERSION.md` and `docs/releases/`. This README stays focused on current system behavior and companion-document roles.

<!-- MM:END:DOCBODY -->
