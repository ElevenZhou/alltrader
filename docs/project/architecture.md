# Architecture

## Initial layers

1. **Sources** — books, interviews, public records, datasets, and documented provider inputs with provenance metadata.
2. **Method contracts** — structured inputs, triggers, filters, sizing, exits, invalidation, and evidence grade.
3. **Research agents** — role-specific analysis that emits the common contract.
4. **Evaluation** — deterministic fixtures, minimum backtests, benchmark/cost/slippage disclosures, and failure analysis.
5. **Paper ledger** — simulated decisions and outcomes; no broker side effects by default.
6. **Review boundary** — explicit approval before any production or live-trading adapter is enabled.

The package skeleton intentionally contains no external provider or broker integration yet.
