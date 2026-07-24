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

EXECUTABLE_EXTENSIONS = {
    ".py",
    ".pyi",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".sh",
}


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
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module)
            for alias in node.names:
                if alias.name != "*":
                    imports.add(f"{node.module}.{alias.name}")
    return imports


def _module_matches_prefix(module_name: str, restricted: str) -> bool:
    return module_name == restricted or module_name.startswith(f"{restricted}.")


def _domain_module_names(domain_path: str) -> set[str]:
    root_name = domain_path.rstrip("/").split("/")[-1]
    return {root_name}


def _import_references_domain(import_name: str, domain_path: str) -> bool:
    for domain_name in _domain_module_names(domain_path):
        if _module_matches_prefix(import_name, domain_name):
            return True
    return False


def _is_restricted_import(import_name: str, restricted_modules: list[str]) -> str | None:
    for restricted in restricted_modules:
        if _module_matches_prefix(import_name, restricted):
            return restricted
    return None


def check_file(file_path: Path, policy: dict[str, Any], root: Path) -> list[Violation]:
    rel = file_path if not file_path.is_absolute() else file_path.relative_to(root)
    rel_posix = rel.as_posix()
    source = (root / rel).read_text(encoding="utf-8")
    imports = _extract_imports(source)
    violations: list[Violation] = []

    domain = _domain_for_file(rel, policy)
    contracts_path = policy.get("contracts", {}).get("path", "packages/contracts").rstrip("/")
    contracts_name = contracts_path.split("/")[-1]

    if domain:
        for other_domain, other_path in policy.get("product_domains", {}).items():
            if other_domain == domain:
                continue
            for import_name in imports:
                if _import_references_domain(import_name, other_path):
                    violations.append(
                        Violation(
                            file=rel,
                            import_name=import_name,
                            rule="product_domains_must_not_cross_import",
                            remediation=(
                                f"Remove direct import of '{import_name}' from product domain "
                                f"'{domain}'. Depend on contracts or escalate via ADR."
                            ),
                        )
                    )

    if _is_harness_file(rel, policy):
        for domain_path in policy.get("product_domains", {}).values():
            domain_name = domain_path.rstrip("/").split("/")[-1]
            if domain_name == contracts_name:
                continue
            for import_name in imports:
                if _import_references_domain(import_name, domain_path):
                    violations.append(
                        Violation(
                            file=rel,
                            import_name=import_name,
                            rule="harness_must_not_import_product_domains",
                            remediation=(
                                f"Harness file '{rel_posix}' must not import product domain "
                                f"'{domain_name}' via '{import_name}'."
                            ),
                        )
                    )

    for category, cfg in policy.get("restricted_imports", {}).items():
        restricted_modules = cfg.get("modules", [])
        approved_paths = [p.rstrip("/") for p in cfg.get("approved_paths", [])]
        for import_name in imports:
            matched = _is_restricted_import(import_name, restricted_modules)
            if matched is None:
                continue
            allowed = any(
                rel_posix.startswith(f"{approved}/") or rel_posix == approved
                for approved in approved_paths
            )
            if not allowed:
                violations.append(
                    Violation(
                        file=rel,
                        import_name=import_name,
                        rule=f"restricted_import:{category}",
                        remediation=(
                            f"Import '{import_name}' matches restricted module '{matched}' for "
                            f"'{category}'. Update architecture policy and ADR to add an approved "
                            f"path, or remove the import from '{rel_posix}'."
                        ),
                    )
                )

    return violations


def check_placeholder_directories(policy: dict[str, Any], root: Path) -> list[Violation]:
    placeholder_cfg = policy.get("placeholder_only", {})
    placeholder_paths = placeholder_cfg.get("paths", [])
    extensions = set(placeholder_cfg.get("executable_extensions", sorted(EXECUTABLE_EXTENSIONS)))
    violations: list[Violation] = []

    for placeholder_path in placeholder_paths:
        base = root / placeholder_path
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(root)
            rel_posix = rel.as_posix()
            if path.name == "README.md":
                continue
            if path.suffix in extensions:
                violations.append(
                    Violation(
                        file=rel,
                        import_name=path.suffix,
                        rule="placeholder_only_no_executable_source",
                        remediation=(
                            f"Placeholder directory '{placeholder_path}' must not contain "
                            f"executable source files during H0. Remove '{rel_posix}' or move it "
                            f"outside the placeholder boundary."
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
    violations.extend(check_placeholder_directories(policy, root))
    return violations
