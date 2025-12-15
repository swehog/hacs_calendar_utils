"""Constants for the Calendar Utils component."""

import logging
from typing import Final

from homeassistant.components.calendar import const

LOGGER = logging.getLogger(__name__)

DOMAIN: Final = "calendar_utils"
DEFAULT_NAME: Final = "Calendar Utils"

CALENDAR_DOMAIN = const.DOMAIN

# rfc5545 fields
EVENT_UID = const.EVENT_UID
EVENT_START = const.EVENT_START
EVENT_END = const.EVENT_END
EVENT_SUMMARY = const.EVENT_SUMMARY
EVENT_DESCRIPTION = const.EVENT_DESCRIPTION
EVENT_LOCATION = const.EVENT_LOCATION
EVENT_RECURRENCE_ID = const.EVENT_RECURRENCE_ID
EVENT_RECURRENCE_RANGE = const.EVENT_RECURRENCE_RANGE
EVENT_RRULE = const.EVENT_RRULE

# Service call fields
EVENT_START_DATE = const.EVENT_START_DATE
EVENT_END_DATE = const.EVENT_END_DATE
EVENT_START_DATETIME = const.EVENT_START_DATETIME
EVENT_END_DATETIME = const.EVENT_END_DATETIME
EVENT_IN = const.EVENT_IN
EVENT_IN_DAYS = const.EVENT_IN_DAYS
EVENT_IN_WEEKS = const.EVENT_IN_WEEKS
EVENT_TIME_FIELDS = const.EVENT_TIME_FIELDS
EVENT_TYPES = const.EVENT_TYPES
EVENT_DURATION = const.EVENT_DURATION

# Fields for the list events service
LIST_EVENT_FIELDS = {*const.LIST_EVENT_FIELDS, EVENT_UID}

# Services
ENSURE_EVENT_EXISTS_SERVICE = "ensure_event_exists"
DELETE_EVENT_BY_UID_SERVICE: Final = "delete_event_by_uid"
UPDATE_EVENT_BY_UID_SERVICE: Final = "update_event_by_uid"
GET_EVENTS_SERVICE: Final = "get_events"
