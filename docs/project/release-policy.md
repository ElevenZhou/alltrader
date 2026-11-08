# Release and Change Policy

- Releases are tagged from `main` only after CI passes on the supported Python matrix.
- Every release must update `CHANGELOG.md` and record known limitations.
- Research or strategy changes must identify data sources, license terms, sample period, benchmark, costs, slippage assumptions, and failure conditions.
- No live-trading adapter, production deployment, credential change, or external notification is part of a release unless explicitly approved and recorded.
- The project currently has no automated release publishing; tags and GitHub release notes are manual until a later milestone.
