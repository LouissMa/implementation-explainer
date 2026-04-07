from __future__ import annotations

from pathlib import Path
import sys


REQUIRED_FILES = [
    Path("README.md"),
    Path("LICENSE"),
    Path("skill/implementation-explainer/SKILL.md"),
    Path("skill/implementation-explainer/references/documentation-rules.md"),
    Path("scripts/install_skill.py"),
    Path("docs/CHANGELOG.md"),
    Path("docs/ARCHITECTURE.md"),
]

FORBIDDEN_PATHS = [
    Path(".ai-skills-test"),
    Path(".codex-test"),
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (repo_root / relative_path).exists():
            errors.append(f"Missing required file: {relative_path}")

    for relative_path in FORBIDDEN_PATHS:
        if (repo_root / relative_path).exists():
            errors.append(f"Temporary directory should not be committed: {relative_path}")

    skill_file = repo_root / "skill/implementation-explainer/SKILL.md"
    if skill_file.exists():
        skill_text = skill_file.read_text(encoding="utf-8")
        required_sections = [
            "## Core behavior",
            "## Required chat output",
            "## Required project documentation",
            "## Recommended workflow",
        ]
        for section in required_sections:
            if section not in skill_text:
                errors.append(f"Missing required section in SKILL.md: {section}")

    readme_file = repo_root / "README.md"
    if readme_file.exists():
        readme_text = readme_file.read_text(encoding="utf-8")
        readme_checks = [
            "## Install",
            "## Use",
            "## Current capabilities",
            "python scripts/validate_project.py",
        ]
        for marker in readme_checks:
            if marker not in readme_text:
                errors.append(f"README.md is missing: {marker}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
