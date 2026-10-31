from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.json_sqlite_store import (
    async_setup,
    async_setup_entry,
    async_unload_entry,
)
from custom_components.json_sqlite_store.const import DOMAIN, SERVICE_READ


async def test_async_setup_registers_services_once(hass: HomeAssistant) -> None:
    assert await async_setup(hass, {})
    assert hass.services.has_service(DOMAIN, SERVICE_READ)

    assert await async_setup(hass, {})


async def test_setup_entry_sets_runtime_data_and_unloads(
    hass: HomeAssistant,
) -> None:
    config_entry = MockConfigEntry(domain=DOMAIN)

    assert await async_setup_entry(hass, config_entry)
    assert config_entry.runtime_data.entry_id == config_entry.entry_id
    assert await async_unload_entry(hass, config_entry)


async def test_read_service_reports_unimplemented(hass: HomeAssistant) -> None:
    assert await async_setup(hass, {})

    try:
        await hass.services.async_call(DOMAIN, SERVICE_READ, {}, blocking=True)
    except HomeAssistantError as err:
        assert "bootstrap scaffold" in str(err)
    else:
        raise AssertionError("Expected HomeAssistantError for bootstrap service call")
