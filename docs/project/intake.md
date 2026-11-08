# Project Intake

## Mandatory to start

- Project name: `alltrader`
- Project code: `ALLTRADER`
- Goal in one sentence: Build an open-source, evidence-first trading research and agent framework that converts sourced methods into auditable rules and reproducible paper backtests.
- Target user or internal consumer: Researchers and developers building paper-trading or educational market-analysis agents.
- Initial scope: Project governance, evidence/provenance records, strategy-contract design, paper research, and reproducible backtest interfaces.
- Explicit exclusions: Live order execution, financial advice, guaranteed returns, credential handling, and full transcription of the source corpus before sampling and budgeting.
- First acceptance criteria: Public repository exists; README and governance files are present; package smoke test passes; Phase 0 report is included; no secrets are tracked.
- Current stage: `discovery`
- Reference objects: Existing Phase 0 report in `docs/research/phase0-report.md`; reference projects are listed there with evidence labels.

## Recommended

- Repository setup mode: `new`
- Remote URL: `https://github.com/ElevenZhou/alltrader`
- Deadline or review date: `TBD` — project owner decision needed.
- Target platforms and runtime versions: Python 3.11+ on Windows/Linux/macOS; verify in Phase 1.
- Technical preferences and constraints: Keep adapters modular; preserve provenance; use open licenses after dependency review.
- Dependencies and external services: `TBD` — provider and model selection is a Phase 1 decision.
- Design or competitor references: TradingAgents, FinRobot, Qlib, FinRL-X, Vibe-Trading; see Phase 0 report.
- Environment matrix: `local` and `paper`; production is out of scope for this milestone.
- Deployment target and rollback expectation: `TBD`; no deployment in the initialization milestone.
- Test strategy: Fast unit/smoke tests first; deterministic fixtures before external data tests.
- Budget/cost limit: `TBD` — source ingestion and model/API budget needs owner decision.
- Known risks and open questions: Data licenses, look-ahead bias, survivorship bias, reproducibility, model cost, and evidence quality.
