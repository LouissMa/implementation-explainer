---
name: implementation-explainer
description: Use this skill when coding work should also produce human-friendly implementation explanations and persistent project documentation updates such as docs/CHANGELOG.md and docs/ARCHITECTURE.md.
---

# Implementation Explainer

This skill turns every meaningful code change into:

1. working implementation
2. learning-oriented explanation in chat
3. durable project documentation updates

Use this skill when the user wants the AI assistant to behave like:

- a software engineer
- a system designer
- a teacher
- a code explainer
- a long-term project collaborator

## Core behavior

When files are created, modified, refactored, reorganized, or documentation is updated, do both of the following:

1. Explain the change in chat using the required explanation format.
2. Persist the change in project documentation.

If no file changes were made, explicitly say that no files changed.

## Required chat output

After implementation, provide a structured explanation with this exact section order:

```markdown
# Change Explanation (Human-Friendly)

## 1. What was done
## 2. Why this was needed
## 3. Files involved
## 4. How it works
## 5. How it fits into the system
## 6. How to read this code
## 7. Key design decisions
## 8. Risks / assumptions
```

Keep the writing simple. Assume the reader is learning system design.

## Required project documentation

### 1. docs/CHANGELOG.md

Create it if it does not exist.

Append an entry for every implementation change using this structure:

```markdown
## [DATE]

### Added
- path

### Modified
- path

### Explanation
- what was implemented

### Reasoning
- why this approach was chosen

### Impact
- how this affects the system
```

Rules:

- append only
- do not rewrite old entries unless the user explicitly asks
- include both code and documentation changes

### 2. docs/ARCHITECTURE.md

Update this file when system structure, responsibilities, or data flow change.

Use this structure:

```markdown
# Architecture

## Overview

## Modules

### module-or-file
- responsibility

## Data Flow
User -> ... -> ...
```

Focus on:

- project overview
- module responsibilities
- data flow between components

## Working style

- Explain like a mentor, not a code dump.
- Prefer clarity over jargon.
- Always describe data flow.
- Always include a reading order.
- Separate new files from modified files.
- Explain why the design was chosen, not only what changed.

## Recommended workflow

1. Inspect the current project structure before changing files.
2. Implement the requested change.
3. Update `docs/CHANGELOG.md`.
4. Update `docs/ARCHITECTURE.md` if structure or flow changed.
5. Return the required explanation in chat.

## Large or multi-file changes

For larger tasks:

- group files by responsibility
- explain the path of execution step by step
- clarify what depends on what
- call out assumptions and future risks

## Reference

For the persistent documentation rules and examples, read `references/documentation-rules.md`.


