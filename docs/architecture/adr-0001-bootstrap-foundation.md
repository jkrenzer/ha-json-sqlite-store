# ADR-0001: Bootstrap foundation for json_sqlite_store

## Status

Draft

## Context

The repository needs a reproducible development environment and an honest Home Assistant
integration scaffold before persistence and entity features can be implemented.

## Decision

- Use Poetry non-package mode with committed lockfile.
- Use Ruff + strict mypy + pre-commit as initial quality gates.
- Create a bootstrap-only integration that registers future action names but rejects execution.
- Provide quality-scale seed data from Home Assistant's official scaffold template.

## Consequences

- Development is reproducible and typed from day one.
- The integration communicates unimplemented state clearly.
- Follow-up phases can add persistence/actions/entities without reworking the base tooling.
