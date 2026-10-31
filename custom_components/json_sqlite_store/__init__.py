"""Bootstrap setup for the json_sqlite_store integration."""

from __future__ import annotations

from collections.abc import Mapping

from homeassistant.core import HomeAssistant

from .models import JsonSqliteStoreConfigEntry, JsonSqliteStoreRuntimeData
from .services import async_register_services


async def async_setup(hass: HomeAssistant, config: Mapping[str, object]) -> bool:
    """Set up the integration domain and register service actions once."""
    await async_register_services(hass)
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: JsonSqliteStoreConfigEntry,
) -> bool:
    """Set up a config entry with typed runtime data for future state."""
    entry.runtime_data = JsonSqliteStoreRuntimeData(entry_id=entry.entry_id)
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: JsonSqliteStoreConfigEntry,
) -> bool:
    """Unload a config entry while keeping globally registered actions."""
    _ = hass
    _ = entry
    return True
