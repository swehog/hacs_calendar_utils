"""Get events service for Calendar Utils."""

from homeassistant.components.calendar import (
    CONF_EVENT,
    CalendarEntity,
    _validate_timespan,
)
from homeassistant.core import ServiceCall, ServiceResponse

from ..const import (
    EVENT_END,
    EVENT_END_DATE,
    EVENT_END_DATETIME,
    EVENT_IN,
    EVENT_RECURRENCE_ID,
    EVENT_RECURRENCE_RANGE,
    EVENT_START,
    EVENT_START_DATE,
    EVENT_START_DATETIME,
    EVENT_TIME_FIELDS,
    EVENT_UID,
)
from .helpers import get_calendar_entities


async def _handle_update_event_by_uid(call: ServiceCall) -> ServiceResponse:
    calendar = get_calendar_entities(call)[0]
    return await _async_update_event_service(calendar, call)


async def _async_update_event_service(
    entity: CalendarEntity, call: ServiceCall
) -> None:
    """Update an event in calendar."""
    params = {
        "event": {
            k: v
            for k, v in call.data.items()
            if k
            not in [*EVENT_TIME_FIELDS, EVENT_RECURRENCE_ID, EVENT_RECURRENCE_RANGE]
        },
        EVENT_UID: call.data.get(EVENT_UID, ""),
        EVENT_RECURRENCE_ID: call.data.get(EVENT_RECURRENCE_ID),
        EVENT_RECURRENCE_RANGE: call.data.get(EVENT_RECURRENCE_RANGE),
    }
    if any(
        [
            call.data.get(EVENT_IN),
            all([call.data.get(EVENT_START_DATE), call.data.get(EVENT_END_DATE)]),
            all(
                [call.data.get(EVENT_START_DATETIME), call.data.get(EVENT_END_DATETIME)]
            ),
        ]
    ):
        (start, end) = _validate_timespan(call.data)
        params[CONF_EVENT] = {
            **params[CONF_EVENT],
            EVENT_START: start,
            EVENT_END: end,
        }
    await entity.async_update_event(**params)
