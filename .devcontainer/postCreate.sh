#!/usr/bin/env bash
set -euo pipefail

poetry --version
poetry check --lock
poetry install --sync --with dev,test --no-root
