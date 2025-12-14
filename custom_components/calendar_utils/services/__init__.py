"""Services for Calendar Utils."""

from homeassistant.core import HomeAssistant, SupportsResponse

from ..const import (
    DELETE_EVENT_BY_UID_SERVICE,
    DOMAIN,
    GET_EVENTS_SERVICE,
    UPDATE_EVENT_BY_UID_SERVICE,
)
from ..schemas import (
    DELETE_EVENT_BY_UID_SERVICE_SCHEMA,
    GET_EVENTS_SERVICE_SCHEMA,
    UPDATE_EVENT_BY_UID_SERVICE_SCHEMA,
)
from .delete_event_by_uid_service import _handle_delete_event_by_uid
from .get_events_service import _handle_get_events
from .update_event_by_uid_service import _handle_update_event_by_uid


async def async_setup_services(hass: HomeAssistant) -> None:
    """Setup services for Calendar Utils."""
    hass.services.async_register(
        domain=DOMAIN,
        service=DELETE_EVENT_BY_UID_SERVICE,
        schema=DELETE_EVENT_BY_UID_SERVICE_SCHEMA,
        service_func=_handle_delete_event_by_uid
    )
    hass.services.async_register(
        domain=DOMAIN,
        service=UPDATE_EVENT_BY_UID_SERVICE,
        schema=UPDATE_EVENT_BY_UID_SERVICE_SCHEMA,
        service_func=_handle_update_event_by_uid
    )
    hass.services.async_register(
        domain=DOMAIN,
        service=GET_EVENTS_SERVICE,
        schema=GET_EVENTS_SERVICE_SCHEMA,
        service_func=_handle_get_events,
        supports_response=SupportsResponse.ONLY
    )
