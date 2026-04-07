# Release Checklist

Use this checklist before pushing the project to GitHub or cutting a release.

## Repository hygiene

- Confirm there are no temporary test directories such as `.ai-skills-test/` or `.codex-test/`
- Confirm local-only notes, secrets, and machine-specific paths are not present
- Confirm the repository contains only the files intended for open source release

## Documentation

- Read `README.md` from top to bottom and confirm a new user can understand the project
- Confirm installation instructions match the current installer behavior
- Confirm `docs/CHANGELOG.md` has an entry for the latest change
- Confirm `docs/ARCHITECTURE.md` still matches the current repository structure

## Validation

- Run `python scripts/validate_project.py`
- Run `python scripts/install_skill.py --target-dir .ai-skills-test/implementation-explainer`
- Confirm the installed output contains `SKILL.md` and `references/documentation-rules.md`

## Release readiness

- Confirm the license is correct
- Confirm the skill name and description are stable enough for public reuse
- Confirm example wording is tool-agnostic and suitable for different AI coding assistants
- Create the GitHub repository and push the code
