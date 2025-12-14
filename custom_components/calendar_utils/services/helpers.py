"""Helpers for Calendar Utils."""

from homeassistant.components.calendar import CalendarEntity
from homeassistant.core import ServiceCall
from homeassistant.exceptions import ServiceValidationError

from ..const import CALENDAR_DOMAIN


def get_calendar_entities(call: ServiceCall) -> list[CalendarEntity]:
    """Get calendar entity from ServiceCall."""
    entity_ids = call.data["entity_id"]
    calendars = [
        calendar
        for calendar in call.hass.data.get(CALENDAR_DOMAIN, object).entities
        if calendar.entity_id in entity_ids
    ]
    if len(calendars) < 1:
        raise ServiceValidationError("No matching calendars found")
    return calendars

