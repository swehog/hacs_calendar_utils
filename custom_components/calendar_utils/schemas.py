"""Schemas for Calendar Util component."""

from typing import Final

import voluptuous as vol

from homeassistant.components.calendar import (
    MIN_NEW_EVENT_DURATION,
    _as_local_timezone,
    _empty_as_none,
    _has_consistent_timezone,
    _has_min_duration,
    _has_positive_interval,
)
from homeassistant.helpers import config_validation as cv

from .const import (
    EVENT_DESCRIPTION,
    EVENT_DURATION,
    EVENT_END_DATE,
    EVENT_END_DATETIME,
    EVENT_IN,
    EVENT_IN_DAYS,
    EVENT_IN_WEEKS,
    EVENT_LOCATION,
    EVENT_RECURRENCE_ID,
    EVENT_RECURRENCE_RANGE,
    EVENT_START_DATE,
    EVENT_START_DATETIME,
    EVENT_SUMMARY,
    EVENT_TYPES,
    EVENT_UID,
)

ENSURE_EVENT_EXISTS_SCHEMA = vol.All(
    cv.has_at_least_one_key(EVENT_START_DATE, EVENT_START_DATETIME, EVENT_IN),
    cv.has_at_most_one_key(EVENT_START_DATE, EVENT_START_DATETIME, EVENT_IN),
    cv.make_entity_service_schema(
        {
            vol.Required(EVENT_SUMMARY): cv.string,
            vol.Optional(EVENT_DESCRIPTION, default=""): cv.string,
            vol.Optional(EVENT_LOCATION): cv.string,
            vol.Inclusive(
                EVENT_START_DATE, "dates", "Start and end dates must both be specified"
            ): cv.date,
            vol.Inclusive(
                EVENT_END_DATE, "dates", "Start and end dates must both be specified"
            ): cv.date,
            vol.Inclusive(
                EVENT_START_DATETIME,
                "datetimes",
                "Start and end datetimes must both be specified",
            ): cv.datetime,
            vol.Inclusive(
                EVENT_END_DATETIME,
                "datetimes",
                "Start and end datetimes must both be specified",
            ): cv.datetime,
            vol.Optional(EVENT_IN): vol.Schema(
                {
                    vol.Exclusive(EVENT_IN_DAYS, EVENT_TYPES): cv.positive_int,
                    vol.Exclusive(EVENT_IN_WEEKS, EVENT_TYPES): cv.positive_int,
                }
            ),
        },
    ),
    _has_consistent_timezone(EVENT_START_DATETIME, EVENT_END_DATETIME),
    _as_local_timezone(EVENT_START_DATETIME, EVENT_END_DATETIME),
    _has_min_duration(EVENT_START_DATE, EVENT_END_DATE, MIN_NEW_EVENT_DURATION),
    _has_min_duration(EVENT_START_DATETIME, EVENT_END_DATETIME, MIN_NEW_EVENT_DURATION),
)
DELETE_EVENT_BY_UID_SERVICE_SCHEMA: Final = vol.All(
    cv.make_entity_service_schema(
        {
            vol.Required(EVENT_UID): cv.string,
            vol.Optional(EVENT_RECURRENCE_ID): vol.Any(
                vol.All(cv.string, _empty_as_none), None
            ),
            vol.Optional(EVENT_RECURRENCE_RANGE): cv.string,
        }
    )
)
UPDATE_EVENT_BY_UID_SERVICE_SCHEMA = vol.All(
    cv.make_entity_service_schema(
        {
            vol.Required(EVENT_UID): cv.string,
            vol.Optional(EVENT_SUMMARY): cv.string,
            vol.Optional(EVENT_DESCRIPTION): cv.string,
            vol.Optional(EVENT_LOCATION): cv.string,
            vol.Inclusive(
                EVENT_START_DATE, "dates", "Start and end dates must both be specified"
            ): cv.date,
            vol.Inclusive(
                EVENT_END_DATE, "dates", "Start and end dates must both be specified"
            ): cv.date,
            vol.Inclusive(
                EVENT_START_DATETIME,
                "datetimes",
                "Start and end datetimes must both be specified",
            ): cv.datetime,
            vol.Inclusive(
                EVENT_END_DATETIME,
                "datetimes",
                "Start and end datetimes must both be specified",
            ): cv.datetime,
            vol.Optional(EVENT_IN): vol.Schema(
                {
                    vol.Exclusive(EVENT_IN_DAYS, EVENT_TYPES): cv.positive_int,
                    vol.Exclusive(EVENT_IN_WEEKS, EVENT_TYPES): cv.positive_int,
                }
            ),
            vol.Optional(EVENT_RECURRENCE_ID): vol.Any(
                vol.All(cv.string, _empty_as_none), None
            ),
            vol.Optional(EVENT_RECURRENCE_RANGE): cv.string,
        }
    ),
    _has_consistent_timezone(EVENT_START_DATETIME, EVENT_END_DATETIME),
    _as_local_timezone(EVENT_START_DATETIME, EVENT_END_DATETIME),
    _has_min_duration(EVENT_START_DATE, EVENT_END_DATE, MIN_NEW_EVENT_DURATION),
    _has_min_duration(EVENT_START_DATETIME, EVENT_END_DATETIME, MIN_NEW_EVENT_DURATION),
)
GET_EVENTS_SERVICE_SCHEMA: Final = vol.All(
    cv.has_at_least_one_key(EVENT_END_DATETIME, EVENT_DURATION),
    cv.has_at_most_one_key(EVENT_END_DATETIME, EVENT_DURATION),
    cv.make_entity_service_schema(
        {
            vol.Optional(EVENT_START_DATETIME): cv.datetime,
            vol.Optional(EVENT_END_DATETIME): cv.datetime,
            vol.Optional(EVENT_DURATION): vol.All(
                cv.time_period, cv.positive_timedelta
            ),
        }
    ),
    _has_positive_interval(EVENT_START_DATETIME, EVENT_END_DATETIME, EVENT_DURATION),
)
