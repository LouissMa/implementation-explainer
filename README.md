# Implementation Explainer Skill

An open-source AI engineering skill package that turns code changes into three outputs:

1. implementation
2. human-friendly explanation
3. persistent project documentation

This skill is designed for teams that want AI coding help without losing architectural clarity or team memory over time.

## What it does

When the skill is used, the AI assistant should:

- explain code changes in chat in a teaching-oriented format
- update `docs/CHANGELOG.md` after file changes
- update `docs/ARCHITECTURE.md` when structure or data flow changes
- describe execution flow, dependencies, and system fit
- provide a recommended reading order for learners

## Repository layout

```text
implementation-explainer/
|-- README.md
|-- LICENSE
|-- .gitignore
|-- skill/
|   `-- implementation-explainer/
|       |-- SKILL.md
|       `-- references/
|           `-- documentation-rules.md
|-- scripts/
|   |-- install_skill.py
|   `-- validate_project.py
`-- docs/
    |-- ARCHITECTURE.md
    |-- CHANGELOG.md
    `-- RELEASE_CHECKLIST.md
```

## Install

### Option 1: install with Python

```bash
python scripts/install_skill.py
```

By default this copies the skill into:

- Windows: `%USERPROFILE%\\.ai-skills\\implementation-explainer`
- macOS/Linux: `$HOME/.ai-skills/implementation-explainer`

### Option 2: install to a custom target directory

```bash
python scripts/install_skill.py --target-dir /path/to/skills/implementation-explainer
```

## Use

After installation, add the `implementation-explainer` skill to your AI coding workflow when you want:

- code plus explanation
- enforced changelog updates
- architecture memory
- learning-oriented change walkthroughs

## Recommended GitHub setup

1. Create a new GitHub repository from this folder.
2. Push the repository.
3. Version future skill changes with tags or releases.
4. Share the repo URL so others can clone and install it with the included script.

## Validation before open source release

Run the built-in project validation:

```bash
python scripts/validate_project.py
```

Then run a clean installation check:

```bash
python scripts/install_skill.py --target-dir .ai-skills-test/implementation-explainer
```

For a final manual review, use [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

## Why this exists

AI coding is much more useful when it also leaves behind:

- clear rationale
- architecture knowledge
- onboarding-friendly explanations
- durable project memory

This skill makes those behaviors explicit and repeatable.

## Current capabilities

Today this skill can:

- enforce a structured post-change explanation in chat
- require `docs/CHANGELOG.md` updates after implementation work
- require `docs/ARCHITECTURE.md` updates when structure or data flow changes
- separate new files from modified files in explanations
- explain execution flow, module interaction, and system fit
- provide a learner-friendly reading order
- capture design decisions, risks, and assumptions
- package the skill in a reusable repository with an install script
