"""Get events service for Calendar Utils."""

from homeassistant.components.calendar import CalendarEntity
from homeassistant.core import ServiceCall, ServiceResponse

from ..const import EVENT_RECURRENCE_ID, EVENT_RECURRENCE_RANGE, EVENT_UID
from .helpers import get_calendar_entities


async def _handle_delete_event_by_uid(call: ServiceCall) -> ServiceResponse:
    calendar = get_calendar_entities(call)[0]
    return await _async_delete_event_service(calendar, call)


async def _async_delete_event_service(
    entity: CalendarEntity, call: ServiceCall
) -> None:
    """Delete an event from calendar."""
    await entity.async_delete_event(
        uid=call.data.get(EVENT_UID, ""),
        recurrence_id=call.data.get(EVENT_RECURRENCE_ID),
        recurrence_range=call.data.get(EVENT_RECURRENCE_RANGE),
    )
