# Contributing

## Setup

1. Open in the provided devcontainer (or use Python 3.12 locally).
2. Run `poetry run poe bootstrap`.
3. Run `poetry run poe check` before opening changes.

## Quality gates

- Ruff is the only formatter/linter.
- Mypy runs in strict mode with the Pydantic plugin.
- Tests include Home Assistant bootstrap behavior and SQLite capability checks.
- Pre-commit hooks must pass.

## Non-goals for bootstrap

Do not add fake persistence behavior, fake passing release automation, or broad
placeholder module forests. Keep changes focused and honest about unimplemented
features.
