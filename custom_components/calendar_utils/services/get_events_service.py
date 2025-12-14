"""Get events service for Calendar Utils."""

from collections.abc import Iterable
import dataclasses
from typing import Any

from homeassistant.components.calendar import CalendarEntity, _event_dict_factory
from homeassistant.core import ServiceCall, ServiceResponse
from homeassistant.util import dt as dt_util
from homeassistant.util.json import JsonValueType

from ..const import (
    EVENT_DURATION,
    EVENT_END_DATETIME,
    EVENT_START_DATETIME,
    LIST_EVENT_FIELDS,
)
from .helpers import get_calendar_entities


async def _handle_get_events(call: ServiceCall) -> ServiceResponse:
    calendars = get_calendar_entities(call)
    events = []
    for calendar in calendars:
        events = [*events, *[{**x, "calendar_entity": calendar.entity_id} for x in await _async_get_events_service(calendar, call)]]
    return {"events": events}


def _list_events_dict_factory(
    obj: Iterable[tuple[str, Any]],
) -> dict[str, JsonValueType]:
    """Convert CalendarEvent dataclass items to dictionary of attributes."""
    return {
        name: value
        for name, value in _event_dict_factory(obj).items()
        if name in LIST_EVENT_FIELDS and value is not None
    }


async def _async_get_events_service(
    calendar: CalendarEntity, service_call: ServiceCall
) -> list:
    """List events on a calendar during a time range."""
    start = service_call.data.get(EVENT_START_DATETIME, dt_util.now())
    if EVENT_DURATION in service_call.data:
        end = start + service_call.data[EVENT_DURATION]
    else:
        end = service_call.data[EVENT_END_DATETIME]

    calendar_event_list = await calendar.async_get_events(
        calendar.hass, dt_util.as_local(start), dt_util.as_local(end)
    )
    return [
        dataclasses.asdict(event, dict_factory=_list_events_dict_factory)
        for event in calendar_event_list
    ]
