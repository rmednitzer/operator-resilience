# H-State Event Register

Generated from `data/registers/h-state-event-register.yaml` by `scripts/generate_register_views.py`. Do not edit manually.

Records operator mode-state transitions and assessments.

## Column schema

| Column | Description |
|--------|-------------|
| HSE-ID | Unique identifier: `HSE-nnn` |
| Operator-ID | Operator identifier |
| From state | H-state before transition (H-0 through H-4) |
| To state | H-state after transition (H-0 through H-4) |
| Trigger | What caused the transition |
| Assessment method | self-report / peer-observation / automated / supervisor-assessment |
| Status | `draft` / `active` / `retired` |

## Entries

| HSE-ID | Operator-ID | From | To | Trigger | Assessment method | Status |
|--------|-------------|------|----|---------|-------------------|--------|
| — | — | — | — | — | — | — |
