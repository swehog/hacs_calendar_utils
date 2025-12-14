"""The Calendar Utils service."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .config_flow import CalendarUtilsConfigFlow
from .const import DOMAIN
from .services import async_setup_services

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Track states and offer events for calendars."""    
    await async_setup_services(hass)
    return True


async def async_setup_entry(
    hass: HomeAssistant, entry: CalendarUtilsConfigFlow
) -> bool:
    """Set up Calendar Utils from a config entry."""
    return True


async def async_unload_entry(
    hass: HomeAssistant, entry: CalendarUtilsConfigFlow
) -> bool:
    """Unload a config entry."""
    return True


async def async_remove_entry(
    hass: HomeAssistant, entry: CalendarUtilsConfigFlow
) -> None:
    """Handle removal of an entry."""
