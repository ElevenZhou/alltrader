# Agent Instructions for alltrader

## Project contract

- Read `AI_PROJECT_HANDOFF.md` before making changes and update it after meaningful work.
- Keep evidence, assumptions, and verified behavior separate. Use `TBD` when a fact is unknown.
- Do not add credentials, broker tokens, private datasets, or local runtime state to Git.
- The default mode is paper research. Any production, live-trading, deployment, spending, or external notification change requires explicit user confirmation.
- Preserve unrelated files and changes. Inspect `git status --short --branch` before staging.

## Validation

Run `pytest` and `python -m alltrader --help` before declaring the skeleton healthy. Keep docs and changelog aligned with milestone changes.
