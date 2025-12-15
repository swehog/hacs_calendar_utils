"""Get events service for Calendar Utils."""

import datetime

from homeassistant.components.calendar import async_create_event
from homeassistant.core import ServiceCall, ServiceResponse
from homeassistant.util import dt as dt_util

from ..const import (
    EVENT_DESCRIPTION,
    EVENT_END_DATE,
    EVENT_END_DATETIME,
    EVENT_LOCATION,
    EVENT_START_DATE,
    EVENT_START_DATETIME,
    EVENT_SUMMARY,
)
from .get_events_service import _handle_get_events
from .helpers import get_calendar_entities


async def _handle_ensure_event_exists(call: ServiceCall) -> ServiceResponse:
    """Handle the ensure_event_exists service call."""
    if await _check_event_exists(call):
        return {}
    calendar = get_calendar_entities(call)[0]
    return await async_create_event(calendar, call)


async def _check_event_exists(call: ServiceCall) -> bool:
    """Check if an event already exists in the calendar."""

    def _dt(val):
        if isinstance(val, str):
            val = dt_util.parse_datetime(val)
        if isinstance(val, datetime.date):
            val = datetime.datetime.combine(val, datetime.time())
        return val.replace(tzinfo=None) if val else None

    data = call.data
    events = (await _handle_get_events(call)).get("events", [])
    matchers = [
        # key, event_value, data_value
        (EVENT_SUMMARY, lambda e: e.get(EVENT_SUMMARY), lambda d: d),
        (EVENT_START_DATETIME, lambda e: _dt(e.get("start")), _dt),
        (EVENT_END_DATETIME, lambda e: _dt(e.get("end")), _dt),
        (EVENT_START_DATE, lambda e: _dt(e.get("start")), _dt),
        (EVENT_END_DATE, lambda e: _dt(e.get("end")), _dt),
        (EVENT_LOCATION, lambda e: e.get(EVENT_LOCATION), lambda d: d),
        (EVENT_DESCRIPTION, lambda e: e.get(EVENT_DESCRIPTION), lambda d: d),
    ]
    for event in events:
        if all(
            data.get(key) is None or event_value(event) == data_value(data[key])
            for key, event_value, data_value in matchers
        ):
            return True
    return False
