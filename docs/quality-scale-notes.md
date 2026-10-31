# Quality scale notes

The initial `quality_scale.yaml` was seeded from Home Assistant's official
scaffold template at:
`home-assistant/core/script/scaffold/templates/integration/integration/quality_scale.yaml`.

## Bootstrap exemptions

Bootstrap scope intentionally excludes entities, discovery, devices, and web
session integrations. Rules tied to those capabilities are marked `exempt`
until those capabilities exist.

Rules still in active bootstrap scope (`action-setup`, `runtime-data`,
`config-flow`, strict typing, and setup tests) are marked `done` and have
supporting code/tests in this repository.

## Review follow-up

When persistence and entity features land, re-evaluate each `exempt` rule and
convert to `todo` or `done` with evidence.
