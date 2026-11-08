# alltrader

`alltrader` is an open-source, evidence-first trading research and agent framework. It turns a market idea into a traceable workflow:

`source -> rule -> minimum backtest -> failure conditions -> evidence grade -> versioned skill`

The project begins with paper research and reproducible evaluation. It does not place live orders by default and does not provide investment advice.

## Current status

**Stage:** discovery / Phase 0 complete, Phase 1 intake pending.

The repository includes the Phase 0 ecosystem scan in [`docs/research/phase0-report.md`](docs/research/phase0-report.md). The first implementation milestone is source inventory, clustering, sampling, and a cost estimate before any full transcription or live integration.

## Principles

- Evidence before conclusions; unknowns stay marked `TBD`.
- Every strategy claim must expose inputs, triggers, filters, sizing, exits, and failure conditions.
- Backtests must state sample period, benchmark, costs, slippage assumptions, and limitations.
- Paper trading is the default; production or live-trading changes require explicit confirmation.
- Credentials and local runtime state stay outside Git.

## Quick start

Requires Python 3.11+.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e ".[dev]"
pytest
python -m alltrader --help
```

## Repository map

- `src/alltrader/` — package and CLI entry point.
- `tests/` — fast smoke tests.
- `docs/project/` — durable project decisions, release policy, and handoff records.
- `docs/research/` — evidence-bounded research inputs and reports.
- `.github/` — CI, issue forms, and review templates.

Operations deployment notes are not applicable to this offline, paper-first initialization; any future runtime deployment must add `docs/ops/` before that milestone.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md), and [`docs/project/release-policy.md`](docs/project/release-policy.md). By contributing, you agree to license contributions under Apache-2.0.

## License

Apache-2.0. See [`LICENSE`](LICENSE).

> This project is for research and education. It is not financial advice, an offer, or a guarantee of future performance.
