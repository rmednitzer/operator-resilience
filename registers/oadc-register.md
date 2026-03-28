# OADC Register

Generated from `data/registers/oadc-register.yaml` by `scripts/generate_register_views.py`. Do not edit manually.

Tracks Operator Authority Degradation Contract instances per operating environment.

## Column schema

| Column | Description |
|--------|-------------|
| OADC-ID | Unique identifier: `OADC-nnn` |
| Environment | Operating environment this OADC applies to |
| Max duty hours | `N` — maximum on-call hours before authority narrows |
| Max incident hours | `T` — maximum incident hours before buddy-pair mandatory |
| Min review threshold (s) | Minimum seconds between alert and decision |
| Passive monitoring interval (min) | Maximum minutes of passive monitoring before state-check |
| Status | `draft` / `active` / `retired` |

## Entries

| OADC-ID | Environment | Max duty (h) | Max incident (h) | Min review (s) | Passive interval (min) | Status |
|---------|-------------|--------------|-------------------|----------------|------------------------|--------|
| — | — | — | — | — | — | — |
