# Calendar Utils

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/swehog/hacs_calendar_utils)](https://github.com/swehog/hacs_calendar_utils/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![License](https://img.shields.io/github/license/swehog/hacs_calendar_utils)](https://github.com/swehog/hacs_calendar_utils/blob/master/LICENSE.md)

**Calendar Utils** is a custom Home Assistant component that complements the core Calendar integration without replacing it. It operates under its own domain, `calendar_utils`, and adds service-level calendar functionality that is not available in the built-in integration.

The core Calendar integration does not expose event UIDs through its services. As a result, it is not possible to reliably update or delete specific calendar events from automations or scripts.

Calendar Utils fills this gap by exposing additional services that make event UIDs available at the service level, while allowing existing calendar integrations to continue operating normally.

> **Note:** Calendar Utils has only been tested with the **Local Calendar** integration. Other calendar integrations may work but are not tested.

## Services

### `calendar_utils.ensure_event_exists`
Makes sure a calendar event exists by creating it when no matching event is found.
When a matching event is present, no action is taken.
Only one calendar can be targeted per service call.

### `calendar_utils.get_events`
Retrieves events from one or multiple calendars and includes their UIDs (when supported by the calendar provider).
This service may return multiple events and is typically used to discover the UID required for further operations.

### `calendar_utils.delete_event_by_uid`
Deletes a single calendar event identified by its UID.
Only one event can be deleted per service call, and only one calendar can be targeted at a time.

### `calendar_utils.update_event_by_uid`
Updates a single calendar event identified by its UID.
Only one event can be updated per service call, and only one calendar can be targeted at a time.

## Typical workflow

1. Call `calendar_utils.get_events` to retrieve events and their UIDs.
2. Select the desired event UID.
3. Call `calendar_utils.delete_event_by_uid` or `calendar_utils.update_event_by_uid` with that UID.

## YAML Examples

### Ensure Event Exists (create event if it does not exists)
```yaml
action: calendar_utils.ensure_event_exists
target:
  entity_id: calendar.my_calendar
data:
  summary: 'Event Title'
  start_date: '2025-12-14'
  end_date: '2025-12-15'
```

### Get Events from one calendar
```yaml
action: calendar_utils.get_events
target:
  entity_id: calendar.my_calendar
data:
  start_date: '2025-12-13'
  end_date: '2025-12-14'
```

### Get Events from multiple calendars
```yaml
action: calendar_utils.get_events
target:
  entity_id:
    - calendar.my_calendar
    - calendar.my_other_calendar
data:
  start_date: '2025-12-13'
  end_date: '2025-12-14'
```

### Delete an Event by UID
```yaml
action: calendar_utils.delete_event_by_uid
target:
  entity_id: calendar.my_calendar
data:
  uid: '12345-abcdef-67890'
```

### Update an Event by UID
> **Note:** `start_date(_time)` and `end_date(_time)` are currently required, even if unchanged.
```yaml
action: calendar_utils.update_event_by_uid
target:
  entity_id: calendar.my_calendar
data:
  uid: '12345-abcdef-67890'
  summary: 'Updated Event Title'
  start_date: '2025-12-13'
  end_date: '2025-12-13'
```

## Installation via HACS
1. Add this repository to HACS under **Custom Repositories** (Category: Integration).
2. Install Calendar Utils (in HACS).
3. Restart Home Assistant.
4. Add integration to Home Assistant.
5. The new services under `calendar_utils` are now available.


## Acknowledgements
A big thank you to the developers of **Home Assistant** and its **Calendar integration**.

> **Note:** Some code in this component may have been directly copied or modified from the core Calendar integration.
