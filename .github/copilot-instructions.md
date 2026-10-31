# Copilot instructions

- Keep this repository at bootstrap scope until persistence, flows, and entities are implemented.
- Do not introduce fake action behavior; unimplemented actions must fail clearly.
- Preserve strict typing and Ruff compliance on every change.
- Keep Home Assistant event loop non-blocking by moving SQLite IO onto dedicated worker threads.
- Prefer narrow, test-backed changes and document blockers rather than guessing.
