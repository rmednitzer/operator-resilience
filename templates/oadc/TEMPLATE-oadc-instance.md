# TEMPLATE: OADC Instance

**OADC ID:** OADC-nnn
**Environment:** [e.g., Production SRE on-call / OT control room / GCS operator]
**Date:** YYYY-MM-DD
**Status:** DRAFT

## Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Max duty hours (N) | [hours] | [why this value] |
| Max incident hours (T) | [hours] | [why this value] |
| Min review threshold | [seconds] | [why this value] |
| Passive monitoring interval | [minutes, default: 30] | [rationale] |
| Circadian window | [HH:MM–HH:MM local, default: 02:00–06:00] | [rationale] |
| Consequence threshold | [definition] | [what qualifies as high-consequence] |

## Conditions

[Copy and customize the OADC condition table from docs/contracts/oadc.md for this environment]

## System enforcement

[How are constraints technically enforced? Which are procedural-only?]

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Safety/Security Lead | | | |
| Management | | | |
