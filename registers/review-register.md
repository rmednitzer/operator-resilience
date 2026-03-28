# Review Register

Generated from `data/registers/review-register.yaml` by `scripts/generate_register_views.py`. Do not edit manually.

Records post-event reviews per trigger deadlines defined in `docs/cross-cutting/post-event-review.md`.

## Column schema

| Column | Description |
|--------|-------------|
| REV-ID | Unique identifier: `REV-nnn` |
| Event type | oadc-trigger / duress-event / social-engineering-attempt / break-glass / h-state-h3 / h-state-h4 / team-degradation |
| Event ref | Reference to triggering event (HSE-nnn / DUR-nnn / EXR-nnn) |
| Review date | Date of review completion |
| Review lead | Person who led the review |
| Status | `draft` / `active` / `retired` |

## Entries

| REV-ID | Event type | Event ref | Review date | Review lead | Status |
|--------|------------|-----------|-------------|-------------|--------|
| — | — | — | — | — | — |
