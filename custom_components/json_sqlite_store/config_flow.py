"""Config flow for json_sqlite_store."""

from __future__ import annotations

from typing import Any

from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlowResult

from .const import DOMAIN


class JsonSqliteStoreConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Expose an explicit bootstrap-only config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Abort user setup until persistence and validation are implemented."""
        _ = user_input
        return self.async_abort(reason="not_implemented")
