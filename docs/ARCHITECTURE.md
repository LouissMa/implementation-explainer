# Architecture

## Overview

This repository packages a reusable AI engineering skill named `implementation-explainer`.
The skill instructs an AI coding assistant to pair code changes with human-friendly explanations and persistent project documentation updates.
The repository also includes an installation utility so the skill can be copied into a user-defined local skills directory.

## Modules

### README.md
- Explains what the project is, how to install it, and how to use it.

### README.zh-CN.md
- Provides a Chinese version of the repository overview, installation guide, and usage instructions.

### skill/implementation-explainer/SKILL.md
- Defines the trigger metadata and the main operational rules for the skill.

### skill/implementation-explainer/references/documentation-rules.md
- Holds supporting guidance that expands on changelog, architecture, and explanation quality expectations.

### scripts/install_skill.py
- Copies the skill from the repository into a target local skills directory.

### scripts/validate_project.py
- Verifies that required files exist, temporary test folders are absent, and core documentation markers are present.

### docs/CHANGELOG.md
- Stores append-only implementation history for this repository.

### docs/ARCHITECTURE.md
- Stores the structural overview and data flow for the repository.

### docs/RELEASE_CHECKLIST.md
- Provides a manual pre-release checklist for open source publishing.

## Data Flow

Maintainer updates repository files -> validation script checks required files and release hygiene -> skill instructions are stored in `skill/implementation-explainer` -> installer copies the skill into the user's chosen skills directory -> an AI coding assistant loads the installed skill when a task matches its description -> the assistant follows the skill to implement changes, explain them, and update project docs.
