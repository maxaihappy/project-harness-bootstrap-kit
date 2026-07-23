"""AST-based architecture boundary checker."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.11+
    import tomli as tomllib  # type: ignore[no-redef]


@dataclass(frozen=True)
class Violation:
    file: Path
    import_name: str
    rule: str
    remediation: str


def _load_policy(path: Path) -> dict[str, Any]:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def _domain_for_file(file_path: Path, policy: dict[str, Any]) -> str | None:
    rel = file_path.as_posix()
    for domain, domain_path in policy.get("product_domains", {}).items():
        prefix = f"{domain_path.rstrip('/')}/"
        if rel.startswith(prefix) or rel == domain_path.rstrip("/"):
            return domain
    return None


def _is_harness_file(file_path: Path, policy: dict[str, Any]) -> bool:
    rel = file_path.as_posix()
    for harness_path in policy.get("harness", {}).get("paths", []):
        prefix = f"{harness_path.rstrip('/')}/"
        if rel.startswith(prefix) or rel == harness_path.rstrip("/"):
            return True
    return False


def _iter_python_files(root: Path, scan_paths: list[str], exclude_globs: list[str]) -> list[Path]:
    files: list[Path] = []
    for scan_path in scan_paths:
        base = root / scan_path
        if not base.exists():
            continue
        for path in base.rglob("*.py"):
            rel = path.relative_to(root).as_posix()
            if any(Path(rel).match(pattern) for pattern in exclude_globs):
                continue
            files.append(path.relative_to(root))
    return sorted(files)


def _extract_imports(source: str) -> set[str]:
    tree = ast.parse(source)
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    return imports


def check_file(file_path: Path, policy: dict[str, Any], root: Path) -> list[Violation]:
    rel = file_path if not file_path.is_absolute() else file_path.relative_to(root)
    rel_posix = rel.as_posix()
    source = (root / rel).read_text(encoding="utf-8")
    imports = _extract_imports(source)
    violations: list[Violation] = []

    domain = _domain_for_file(rel, policy)
    contracts_path = policy.get("contracts", {}).get("path", "packages/contracts").rstrip("/")

    if domain:
        for other_domain, other_path in policy.get("product_domains", {}).items():
            if other_domain == domain:
                continue
            other_root = other_path.rstrip("/").split("/")[-1]
            if other_root in imports:
                violations.append(
                    Violation(
                        file=rel,
                        import_name=other_root,
                        rule="product_domains_must_not_cross_import",
                        remediation=(
                            f"Remove direct import of '{other_root}' from product domain "
                            f"'{domain}'. Depend on contracts or escalate via ADR."
                        ),
                    )
                )

    if _is_harness_file(rel, policy):
        for domain_path in policy.get("product_domains", {}).values():
            domain_root = domain_path.rstrip("/").split("/")[-1]
            if domain_root in imports and domain_root != contracts_path.split("/")[-1]:
                violations.append(
                    Violation(
                        file=rel,
                        import_name=domain_root,
                        rule="harness_must_not_import_product_domains",
                        remediation=(
                            f"Harness file '{rel_posix}' must not import product domain "
                            f"'{domain_root}'."
                        ),
                    )
                )

    for category, cfg in policy.get("restricted_imports", {}).items():
        modules = set(cfg.get("modules", []))
        approved_paths = [p.rstrip("/") for p in cfg.get("approved_paths", [])]
        for module_name in imports:
            if module_name not in modules:
                continue
            allowed = any(
                rel_posix.startswith(f"{approved}/") or rel_posix == approved
                for approved in approved_paths
            )
            if not allowed:
                violations.append(
                    Violation(
                        file=rel,
                        import_name=module_name,
                        rule=f"restricted_import:{category}",
                        remediation=(
                            f"Import '{module_name}' is restricted to approved adapter paths "
                            f"for '{category}'. Update architecture policy and ADR to add a path, "
                            f"or remove the import from '{rel_posix}'."
                        ),
                    )
                )

    return violations


def check_policy(policy_path: Path, root: Path | None = None) -> list[Violation]:
    root = root or policy_path.parent
    policy = _load_policy(policy_path)
    scan_cfg = policy.get("scan", {})
    files = _iter_python_files(
        root,
        scan_cfg.get("paths", []),
        scan_cfg.get("exclude_globs", []),
    )
    violations: list[Violation] = []
    for file_path in files:
        violations.extend(check_file(file_path, policy, root))
    return violations
