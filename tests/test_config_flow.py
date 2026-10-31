from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from custom_components.json_sqlite_store.const import DOMAIN


async def test_user_flow_aborts_until_implemented(
    hass: HomeAssistant, enable_custom_integrations: None
) -> None:
    _ = enable_custom_integrations
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_USER},
    )

    assert result["type"] == "abort"
    assert result["reason"] == "not_implemented"
