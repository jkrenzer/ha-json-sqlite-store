# ha-json-sqlite-store

Bootstrap repository for the Home Assistant `json_sqlite_store` integration.

## Current scope

This repository currently delivers foundation tooling and a minimal, honest
integration scaffold. It does **not** yet implement persistence, entities, real
actions, migrations, or
backup orchestration.

## Product target (future phases)

- Persist arbitrary JSON context in one integration-owned SQLite database.
- Keep one independent document per storage config entry.
- Use Python `sqlite3` with a dedicated owning worker thread and atomic transactions.
- Enforce WAL + `synchronous=FULL`, revision checks, commit-before-acknowledgement, migrations,
  and consistent backups.
- Never block Home Assistant's event loop.
- Optionally expose projected JSON values as `sensor`/`binary_sensor` subentries when projected
  values change.
- Provide future actions for read/write/remove/atomic update with explicit
  `input_format=native|json` and `output_format=native|json`.

## Baseline verification

- Home Assistant `2026.10.4` requires Python `>=3.14.2` (PyPI metadata).
- `pytest-homeassistant-custom-component` `0.13.205` requires Python `>=3.12`.
- The testable baseline is adjusted to Home Assistant `2025.1.4` on Python
  `3.12` because `pytest-homeassistant-custom-component` currently pins Home
  Assistant `2025.1.4`.
- Devcontainer image availability was validated for `python:3.12.8-bookworm`.

## Development

```bash
poetry run poe bootstrap
poetry run poe lint
poetry run poe typecheck
poetry run poe test
poetry run poe docs
poetry run poe hooks
```

## Deferred implementation phases

1. Models/contracts for commands and conflict-aware responses.
2. SQLite worker lifecycle, durability guarantees, and migration strategy.
3. Home Assistant actions, config flow completion, and backup/deletion policy wiring.
4. Sensor/binary_sensor projection views and update semantics.
5. HACS distribution hardening and release automation.

## Durability and backup policy (planned)

- Writes will acknowledge only after transaction commit.
- DB-level durability will use WAL and `synchronous=FULL`.
- Backups will be consistent and migration-aware before schema upgrades.
- Deletion policy will support explicit document removal by config entry scope.

## HACS-first roadmap

This integration is HACS-first and intended to mature through field use before any Home Assistant
Core consideration.

## Known blockers

- Direct access to the Home Assistant contributor quality-scale reference site
  is blocked in this environment, so exemption rationale is tracked in docs and
  seeded from the official scaffold template sourced via
  `home-assistant/core`.
- HACS validation tooling is deferred until repository metadata and packaging reach deployable
  readiness.

## License

The repository currently contains Apache-2.0 licensing text. Confirm final
license choice before first public release.
