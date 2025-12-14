"""Config flow for the Calendar Utils component."""

from typing import Any

from homeassistant import config_entries

from .const import DEFAULT_NAME, DOMAIN


class CalendarUtilsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Calendar Utils config flow."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Handle a flow initialized by the user."""
        if user_input is not None:
            return self.async_create_entry(title=DEFAULT_NAME, data={})
        return self.async_show_form(step_id="user")
