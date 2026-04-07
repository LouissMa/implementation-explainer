# Documentation Rules

This reference supports the `implementation-explainer` skill.

## Intent

The goal is not only to finish the code change, but to preserve understanding for future humans and future AI sessions.

## What to record in CHANGELOG.md

Each entry should capture:

- what files were added
- what files were modified
- what the implementation introduced
- why the approach was chosen
- what impact the change has on the system

Good changelog entries are short, concrete, and focused on system effects rather than commit-style noise.

## What to record in ARCHITECTURE.md

Update architecture when any of the following change:

- new module or directory added
- responsibilities moved between files
- data flow changed
- new integration point introduced
- new installation or packaging path introduced

Do not update architecture for tiny wording-only changes unless they affect understanding.

## Explanation quality bar

A strong explanation should help a learner answer:

1. What changed?
2. Why here?
3. What calls what?
4. Where does data start and end?
5. What should I read first?

## Reading order guidance

When choosing a reading order:

- start with the highest-level entry point
- then show the main behavior file
- finish with supporting references or utilities

## Suggested tone

- simple
- direct
- system-oriented
- teaching-first

