"""Shared entity base module reserved for future sensor platforms."""

from __future__ import annotations

from homeassistant.helpers.entity import Entity


class JsonSqliteStoreEntity(Entity):
    """Common future base entity for json_sqlite_store platforms."""
