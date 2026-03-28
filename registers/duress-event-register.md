# Duress Event Register

Generated from `data/registers/duress-event-register.yaml` by `scripts/generate_register_views.py`. Do not edit manually.

Records duress events (real and exercise) and authority containment actions.

## Column schema

| Column | Description |
|--------|-------------|
| DUR-ID | Unique identifier: `DUR-nnn` |
| Event class | `real` / `exercise` |
| Signal type | `verbal` / `digital` / `physical` |
| Operator-ID | Operator who triggered or was subject to event |
| Detected by | Who or what detected the duress condition |
| Authority containment | Whether authority containment was applied |
| Review ref | `REV-nnn` reference to post-event review |
| Status | `draft` / `active` / `retired` |

## Entries

| DUR-ID | Class | Signal | Operator-ID | Detected by | Containment | Review ref | Status |
|--------|-------|--------|-------------|-------------|-------------|------------|--------|
| — | — | — | — | — | — | — | — |
