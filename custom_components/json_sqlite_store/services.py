"""Home Assistant service registration for json_sqlite_store actions."""

from __future__ import annotations

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import HomeAssistantError

from .const import (
    DOMAIN,
    NOT_IMPLEMENTED_REASON,
    SERVICE_ATOMIC_UPDATE,
    SERVICE_READ,
    SERVICE_REMOVE,
    SERVICE_WRITE,
)


async def async_register_services(hass: HomeAssistant) -> None:
    """Register integration services once during domain setup."""
    if hass.services.has_service(DOMAIN, SERVICE_READ):
        return

    hass.services.async_register(DOMAIN, SERVICE_READ, _handle_unimplemented_service)
    hass.services.async_register(DOMAIN, SERVICE_WRITE, _handle_unimplemented_service)
    hass.services.async_register(DOMAIN, SERVICE_REMOVE, _handle_unimplemented_service)
    hass.services.async_register(
        DOMAIN, SERVICE_ATOMIC_UPDATE, _handle_unimplemented_service
    )


async def _handle_unimplemented_service(call: ServiceCall) -> None:
    """Reject bootstrap-phase service calls with an explicit error."""
    _ = call
    message = (
        "json_sqlite_store bootstrap scaffold only; "
        "persistence actions are not implemented yet"
    )
    raise HomeAssistantError(f"{message} ({NOT_IMPLEMENTED_REASON})")
