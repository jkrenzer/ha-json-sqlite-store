"""Custom exceptions for the json_sqlite_store integration."""

from homeassistant.exceptions import HomeAssistantError


class JsonSqliteStoreError(HomeAssistantError):
    """Base integration error for persistence and action failures."""
