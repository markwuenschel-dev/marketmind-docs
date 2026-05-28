"""Sync public docs from a sibling MarketMind checkout.

The docs repository publishes a curated surface:

* canonical companion Markdown from ``MarketMind/docs/src``;
* ``VERSION.md`` from the MarketMind root;
* sanitized API stubs generated from current import packages.

This script deliberately does not mirror the full ``MarketMind/docs`` tree,
which contains internal research notes, archives, generated ledgers, and
working artifacts.
"""
from __future__ import annotations

import argparse
import ast
import filecmp
import hashlib
import json
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_SOURCE = REPO_ROOT / "docs" / "source"
REFERENCE_ROOT = DOCS_SOURCE / "reference"
STUBS_ROOT = REPO_ROOT / "docs" / "stubs"
SNAPSHOT_PATH = DOCS_SOURCE / "_marketmind_snapshot.json"


COMPANION_FILES = [
    "README.md",
    "WhitePaper.md",
    "ImplementationPlan.md",
    "TechnicalRoadmap.md",
    "MetaLearningCore.md",
    "MetaLearningArchitectureVision.md",
    "ResolutionLedger.md",
    "ThresholdGovernanceRegister.md",
    "DataGovernanceCharter.md",
    "PhaseIIArtifactContract.md",
    "PhaseIIResearchExecutionPlaybook.md",
    "FormattingSpec.md",
    "Risk_and_Execution_Realism_Protocol.md",
    "Signal_Governance_Protocol.md",
    "Signal_Reliability_Schema.md",
    "Task_Validity_Pilot_Report_Canonical.md",
    "trainer_entry_decision_package.md",
]

LEGACY_REDIRECTS = {
    "risk_protocol.md": (
        "Risk and Execution Realism Protocol",
        "Risk_and_Execution_Realism_Protocol.md",
    ),
    "signal_generation_protocol.md": (
        "Signal Governance Protocol",
        "Signal_Governance_Protocol.md",
    ),
    "signal_reliability_schema_v0_1_1.md": (
        "Signal Reliability Schema",
        "Signal_Reliability_Schema.md",
    ),
    "task_validity_pilot_report.md": (
        "Task Validity Pilot Report",
        "Task_Validity_Pilot_Report_Canonical.md",
    ),
}

API_ROOTS = [
    ("pysrc", "pysrc"),
    ("marketmind_gate", "marketmind_gate"),
    ("marketmind_cuml_backend/marketmind_cuml", "marketmind_cuml"),
    ("marketmind_cupy_backend/marketmind_cupy", "marketmind_cupy"),
    ("marketmind_polars_backend/marketmind_polars", "marketmind_polars"),
    ("marketmind_torch_backend/marketmind_torch", "marketmind_torch"),
    ("marketmind_xgboost_backend/marketmind_xgboost", "marketmind_xgboost"),
]

SKIP_DIRS = {
    "__pycache__",
    ".git",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "artifacts",
    "tests",
}


@dataclass
class SyncStats:
    copied: int = 0
    unchanged: int = 0
    redirects: int = 0
    stubs: int = 0
    removed_reference_entries: int = 0
    would_change: int = 0



def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()



def _sha256_text(path: Path) -> str:
    # Snapshot checks should detect content drift, not platform line-ending
    # normalization from Git checkouts on Windows/Linux runners.
    with path.open("r", encoding="utf-8", newline=None) as f:
        text = f.read()
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def snapshot_payload() -> dict[str, object]:
    files = ["VERSION.md", "docs/source/index.md", "docs/source/reference/index.rst"]
    files.extend(f"docs/source/{name}" for name in COMPANION_FILES)
    files.extend(f"docs/source/{name}" for name in LEGACY_REDIRECTS)
    return {
        "schema": 1,
        "files": {
            name: _sha256_text(REPO_ROOT / name)
            for name in sorted(files)
            if (REPO_ROOT / name).is_file()
        },
        "api_roots": [package for _, package in API_ROOTS],
    }


def write_snapshot(stats: SyncStats, check: bool) -> None:
    text = json.dumps(snapshot_payload(), indent=2, sort_keys=True) + "\n"
    _write_if_changed(SNAPSHOT_PATH, text, stats, check)


def check_snapshot() -> int:
    if not SNAPSHOT_PATH.is_file():
        print(f"Missing snapshot manifest: {SNAPSHOT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    payload = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    failures = 0
    for rel, expected in sorted(payload.get("files", {}).items()):
        path = REPO_ROOT / rel
        if not path.is_file():
            print(f"DRIFT missing snapshotted file: {rel}", file=sys.stderr)
            failures += 1
            continue
        actual = _sha256_text(path)
        if actual != expected:
            print(f"DRIFT snapshotted file changed: {rel}", file=sys.stderr)
            failures += 1
    if (STUBS_ROOT / "srcPy").exists():
        print("DRIFT stale docs/stubs/srcPy still exists", file=sys.stderr)
        failures += 1
    if (REFERENCE_ROOT / "srcPy").exists():
        print("DRIFT stale docs/source/reference/srcPy still exists", file=sys.stderr)
        failures += 1
    return 1 if failures else 0

def _copy_if_changed(src: Path, dst: Path, stats: SyncStats, check: bool) -> None:
    if dst.exists() and filecmp.cmp(src, dst, shallow=False):
        stats.unchanged += 1
        return
    if check:
        stats.would_change += 1
        print(f"DRIFT {dst.relative_to(REPO_ROOT)} differs from {src}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    stats.copied += 1


def _write_if_changed(path: Path, text: str, stats: SyncStats | None = None, check: bool = False) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    if check:
        if stats is not None:
            stats.would_change += 1
        print(f"DRIFT {path.relative_to(REPO_ROOT)} would be regenerated")
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def sync_companion_docs(marketmind_root: Path, stats: SyncStats, check: bool) -> None:
    src_root = marketmind_root / "docs" / "src"
    if not src_root.is_dir():
        raise FileNotFoundError(f"Missing MarketMind docs source: {src_root}")

    _copy_if_changed(marketmind_root / "VERSION.md", REPO_ROOT / "VERSION.md", stats, check)

    for name in COMPANION_FILES:
        src = src_root / name
        if not src.is_file():
            raise FileNotFoundError(f"Missing canonical companion doc: {src}")
        _copy_if_changed(src, DOCS_SOURCE / name, stats, check)

    for legacy_name, (title, target) in LEGACY_REDIRECTS.items():
        changed = _write_if_changed(
            DOCS_SOURCE / legacy_name,
            (
                f"# {title}\n\n"
                f"This compatibility page has moved to "
                f"[{target}](./{target}).\n"
            ),
            stats,
            check,
        )
        if changed and not check:
            stats.redirects += 1


def index_text() -> str:
    return """# MarketMind Documentation

Read the Docs for `marketmind-docs` publishes the public documentation surface mirrored from the current `MarketMind` repository. Companion Markdown under `docs/source/` is copied from `MarketMind/docs/src/`; `VERSION.md` is copied from the MarketMind repository root.

The current companion suite records the Phase II broad reset after W3/W4 diagnostics, including the P2-MAP -> P2-MATRIX -> P2-NARROW -> P2-PORTFOLIO funnel and the supporting artifact, signal, threshold, and trainer-entry governance documents.

Older governance/legal pages, contributor guidance, tutorials, and compatibility pages remain published where useful, but they are not treated as canonical `MarketMind/docs/src` mirrors unless listed in the companion suite below.

## Published Sections

### Overview

- [README / Technical Overview](README.md)
- [White Paper](WhitePaper.md)
- [Release History](CHANGELOG.md)

### Current Companion Suite

- [Implementation Plan](ImplementationPlan.md)
- [Technical Roadmap](TechnicalRoadmap.md)
- [Meta-Learning Core](MetaLearningCore.md)
- [Meta-Learning Architecture Vision](MetaLearningArchitectureVision.md)
- [Resolution Ledger](ResolutionLedger.md)
- [Trainer Entry Decision Package](trainer_entry_decision_package.md)

### Governance / Phase II Controls

- [Threshold Governance Register](ThresholdGovernanceRegister.md)
- [Data Governance Charter](DataGovernanceCharter.md)
- [Phase II Artifact Contract](PhaseIIArtifactContract.md)
- [Phase II Research Execution Playbook](PhaseIIResearchExecutionPlaybook.md)

### Protocols and Appendices

- [Risk and Execution Realism Protocol](Risk_and_Execution_Realism_Protocol.md)
- [Signal Governance Protocol](Signal_Governance_Protocol.md)
- [Signal Reliability Schema](Signal_Reliability_Schema.md)
- [Task Validity Pilot Report](Task_Validity_Pilot_Report_Canonical.md)
- [Formatting Spec](FormattingSpec.md)

### Governance and Legal

- [Governance](GOVERNANCE.md)
- [Model Card](MODEL_CARD.md)
- [Privacy Policy](PRIVACY_POLICY.md)
- [Risk Disclosure](RISK_DISCLOSURE.md)
- [Reproducibility](REPRODUCIBILITY.md)
- [Security Policy](SECURITY.md)
- [License](LICENSE.md)

### Contributor and Engineering Guidance

- [Programming Guidelines](contributors/coding_standards.md)

### Reference

- [API Reference](reference/index.rst)

```{toctree}
:hidden:
:maxdepth: 2
:caption: Overview

README / Technical Overview <README.md>
White Paper <WhitePaper.md>
Release History <CHANGELOG.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Current Companion Suite

Implementation Plan <ImplementationPlan.md>
Technical Roadmap <TechnicalRoadmap.md>
Meta-Learning Core <MetaLearningCore.md>
Meta-Learning Architecture Vision <MetaLearningArchitectureVision.md>
Resolution Ledger <ResolutionLedger.md>
Trainer Entry Decision Package <trainer_entry_decision_package.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Governance / Phase II Controls

Threshold Governance Register <ThresholdGovernanceRegister.md>
Data Governance Charter <DataGovernanceCharter.md>
Phase II Artifact Contract <PhaseIIArtifactContract.md>
Phase II Research Execution Playbook <PhaseIIResearchExecutionPlaybook.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Protocols and Appendices

Risk and Execution Realism Protocol <Risk_and_Execution_Realism_Protocol.md>
Signal Governance Protocol <Signal_Governance_Protocol.md>
Signal Reliability Schema <Signal_Reliability_Schema.md>
Task Validity Pilot Report <Task_Validity_Pilot_Report_Canonical.md>
Formatting Spec <FormattingSpec.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Governance and Legal

Governance <GOVERNANCE.md>
Model Card <MODEL_CARD.md>
Privacy Policy <PRIVACY_POLICY.md>
Risk Disclosure <RISK_DISCLOSURE.md>
Reproducibility <REPRODUCIBILITY.md>
Security Policy <SECURITY.md>
License <LICENSE.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Contributor and Engineering Docs

Programming Guidelines <contributors/coding_standards.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Reference

reference/index
```
"""


def reference_index_text() -> str:
    return """API Reference
=============

This page contains auto-generated API reference documentation for the current
MarketMind Python package surface.

.. toctree::
   :titlesonly:

   /reference/pysrc/index
   /reference/marketmind_gate/index
   /reference/marketmind_cuml/index
   /reference/marketmind_cupy/index
   /reference/marketmind_polars/index
   /reference/marketmind_torch/index
   /reference/marketmind_xgboost/index

.. note::

   Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_
   from sanitized stubs generated by ``scripts/sync_from_marketmind.py``.
"""


def write_static_docs(stats: SyncStats, check: bool) -> None:
    _write_if_changed(DOCS_SOURCE / "index.md", index_text(), stats, check)
    _write_if_changed(REFERENCE_ROOT / "index.rst", reference_index_text(), stats, check)


def reset_generated_reference(stats: SyncStats, check: bool) -> None:
    REFERENCE_ROOT.mkdir(parents=True, exist_ok=True)
    for child in REFERENCE_ROOT.iterdir():
        if child.name == "index.rst":
            continue
        if check:
            stats.would_change += 1
            print(f"DRIFT stale generated reference entry would be removed: {child.relative_to(REPO_ROOT)}")
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
        stats.removed_reference_entries += 1


def _annotation(node: ast.AST | None) -> str:
    if node is None:
        return "Any"
    try:
        return ast.unparse(node)
    except Exception:
        return "Any"


def _arg(arg: ast.arg, has_default: bool = False, prefix: str = "") -> str:
    text = f"{prefix}{arg.arg}: {_annotation(arg.annotation)}"
    if has_default:
        text += " = ..."
    return text


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    args = node.args
    parts: list[str] = []
    positional = list(args.posonlyargs) + list(args.args)
    defaults = [False] * (len(positional) - len(args.defaults)) + [True] * len(args.defaults)
    for arg, has_default in zip(positional, defaults):
        parts.append(_arg(arg, has_default))
    if args.vararg:
        parts.append(_arg(args.vararg, prefix="*"))
    elif args.kwonlyargs:
        parts.append("*")
    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        parts.append(_arg(arg, default is not None))
    if args.kwarg:
        parts.append(_arg(args.kwarg, prefix="**"))
    returns = _annotation(node.returns)
    return f"({', '.join(parts)}) -> {returns}"


def _public(name: str) -> bool:
    return not name.startswith("_") or name == "__init__"


def _class_stub(node: ast.ClassDef) -> list[str]:
    bases = ", ".join(_annotation(base) for base in node.bases)
    header = f"class {node.name}"
    if bases:
        header += f"({bases})"
    header += ":"
    lines = [header]
    body: list[str] = []
    for item in node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and _public(item.name):
            prefix = "async " if isinstance(item, ast.AsyncFunctionDef) else ""
            body.append(f"    {prefix}def {item.name}{_signature(item)}: ...")
        elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name) and _public(item.target.id):
            body.append(f"    {item.target.id}: {_annotation(item.annotation)} = ...")
        elif isinstance(item, ast.Assign):
            for target in item.targets:
                if isinstance(target, ast.Name) and _public(target.id):
                    body.append(f"    {target.id}: Any")
    lines.extend(body or ["    ..."])
    return lines


def _module_stub(src: Path) -> str:
    try:
        tree = ast.parse(src.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return "from typing import Any\n\n...\n"

    lines = ["from typing import Any", ""]
    doc = ast.get_docstring(tree)
    if doc:
        lines.extend(['"""', doc.replace('"""', r'\"\"\"'), '"""', ""])

    exported = False
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and _public(node.name):
            prefix = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
            lines.append(f"{prefix}def {node.name}{_signature(node)}: ...")
            exported = True
        elif isinstance(node, ast.ClassDef) and _public(node.name):
            lines.extend(_class_stub(node))
            exported = True
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and _public(node.target.id):
            lines.append(f"{node.target.id}: {_annotation(node.annotation)} = ...")
            exported = True
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and _public(target.id):
                    lines.append(f"{target.id}: Any")
                    exported = True
    if not exported:
        lines.append("...")
    return "\n".join(lines).rstrip() + "\n"


def _iter_py_files(root: Path):
    for path in sorted(root.rglob("*.py")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def generate_stubs(marketmind_root: Path, stats: SyncStats, check: bool) -> None:
    if check:
        return
    if STUBS_ROOT.exists():
        shutil.rmtree(STUBS_ROOT)
    STUBS_ROOT.mkdir(parents=True)

    for source_rel, package_name in API_ROOTS:
        source_root = marketmind_root / source_rel
        if not source_root.is_dir():
            raise FileNotFoundError(f"Missing API source root: {source_root}")
        package_stub_root = STUBS_ROOT / package_name
        for src in _iter_py_files(source_root):
            rel = src.relative_to(source_root)
            dst = package_stub_root / rel.with_suffix(".pyi")
            _write_if_changed(dst, _module_stub(src))
            stats.stubs += 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "marketmind_root",
        nargs="?",
        default="../MarketMind",
        help="Path to the sibling MarketMind checkout.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report companion-doc drift against a MarketMind checkout without writing files.",
    )
    parser.add_argument(
        "--check-snapshot",
        action="store_true",
        help="Verify the checked-in snapshot manifest against current docs files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.check_snapshot:
        return check_snapshot()

    marketmind_root = Path(args.marketmind_root).expanduser().resolve()
    stats = SyncStats()

    sync_companion_docs(marketmind_root, stats, args.check)
    write_static_docs(stats, args.check)
    reset_generated_reference(stats, args.check)
    generate_stubs(marketmind_root, stats, args.check)
    if not args.check:
        write_snapshot(stats, False)

    print("MarketMind docs sync complete")
    print(f"  source: {marketmind_root}")
    print(f"  copied/updated docs: {stats.copied}")
    print(f"  unchanged docs: {stats.unchanged}")
    print(f"  compatibility pages updated: {stats.redirects}")
    print(f"  stale reference entries removed: {stats.removed_reference_entries}")
    print(f"  stubs generated: {stats.stubs}")
    if args.check and stats.would_change:
        print(f"  drift entries: {stats.would_change}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
