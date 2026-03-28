#!/usr/bin/env python3
"""Generate Markdown register views from canonical YAML sources."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data' / 'registers'
REGISTER_DIR = ROOT / 'registers'


def load_yaml(name: str):
    with open(DATA_DIR / name, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def emdash(value):
    if value in (None, '', [], {}):
        return '—'
    return value


def join_list(values):
    return ', '.join(str(v) for v in values) if values else '—'


def render_oadc(data):
    entries = data.get('entries', [])
    rows = []
    for e in entries:
        params = e.get('parameters', {})
        rows.append(
            f"| {e['id']} | {e.get('environment', '—')} "
            f"| {params.get('max_duty_hours', '—')} "
            f"| {params.get('max_incident_hours', '—')} "
            f"| {params.get('min_review_threshold_seconds', '—')} "
            f"| {params.get('passive_monitoring_interval_minutes', '—')} "
            f"| {e['status']} |"
        )
    body = '\n'.join(rows) if rows else '| — | — | — | — | — | — | — |'
    return f'''# OADC Register

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
{body}
'''


def render_h_state_events(data):
    entries = data.get('entries', [])
    rows = []
    for e in entries:
        rows.append(
            f"| {e['id']} | {e.get('operator_id', '—')} "
            f"| {e.get('from_state', '—')} | {e.get('to_state', '—')} "
            f"| {e.get('trigger', '—')} | {e.get('assessment_method', '—')} "
            f"| {e['status']} |"
        )
    body = '\n'.join(rows) if rows else '| — | — | — | — | — | — | — |'
    return f'''# H-State Event Register

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
{body}
'''


def render_duress_events(data):
    entries = data.get('entries', [])
    rows = []
    for e in entries:
        rows.append(
            f"| {e['id']} | {e.get('event_class', '—')} "
            f"| {e.get('signal_type', '—')} | {e.get('operator_id', '—')} "
            f"| {e.get('detected_by', '—')} "
            f"| {e.get('authority_containment_applied', '—')} "
            f"| {emdash(e.get('review_ref'))} | {e['status']} |"
        )
    body = '\n'.join(rows) if rows else '| — | — | — | — | — | — | — | — |'
    return f'''# Duress Event Register

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
{body}
'''


def render_exercises(data):
    entries = data.get('entries', [])
    rows = []
    for e in entries:
        rows.append(
            f"| {e['id']} | {e.get('exercise_type', '—')} "
            f"| {e.get('date', '—')} | {e.get('facilitator', '—')} "
            f"| {e.get('acceptance_criteria_met', '—')} | {e['status']} |"
        )
    body = '\n'.join(rows) if rows else '| — | — | — | — | — | — |'
    return f'''# Exercise Register

Generated from `data/registers/exercise-register.yaml` by `scripts/generate_register_views.py`. Do not edit manually.

Records exercise execution and results against the exercise program.

## Column schema

| Column | Description |
|--------|-------------|
| EXR-ID | Unique identifier: `EXR-nnn` |
| Exercise type | duress-drill / social-engineering-red-team / oadc-threshold-validation / epistemic-check-drill / decision-tree-walkthrough / team-state-sync / safe-state-test |
| Date | Date of exercise execution |
| Facilitator | Person who facilitated the exercise |
| Acceptance criteria met | `true` / `false` |
| Status | `draft` / `active` / `retired` |

## Entries

| EXR-ID | Type | Date | Facilitator | Criteria met | Status |
|--------|------|------|-------------|--------------|--------|
{body}
'''


def render_reviews(data):
    entries = data.get('entries', [])
    rows = []
    for e in entries:
        rows.append(
            f"| {e['id']} | {e.get('event_type', '—')} "
            f"| {e.get('event_ref', '—')} | {e.get('review_date', '—')} "
            f"| {e.get('review_lead', '—')} | {e['status']} |"
        )
    body = '\n'.join(rows) if rows else '| — | — | — | — | — | — |'
    return f'''# Review Register

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
{body}
'''


RENDERERS = {
    'oadc-register.md': lambda: render_oadc(load_yaml('oadc-register.yaml')),
    'h-state-event-register.md': lambda: render_h_state_events(load_yaml('h-state-event-register.yaml')),
    'duress-event-register.md': lambda: render_duress_events(load_yaml('duress-event-register.yaml')),
    'exercise-register.md': lambda: render_exercises(load_yaml('exercise-register.yaml')),
    'review-register.md': lambda: render_reviews(load_yaml('review-register.yaml')),
}


def render_all(write: bool = True):
    rendered = {}
    for filename, fn in RENDERERS.items():
        content = fn().rstrip() + '\n'
        rendered[filename] = content
        if write:
            (REGISTER_DIR / filename).write_text(content, encoding='utf-8')
    return rendered


if __name__ == '__main__':
    write = '--check' not in sys.argv
    REGISTER_DIR.mkdir(exist_ok=True)
    result = render_all(write=write)
    if write:
        for name in result:
            print(f'  Generated: registers/{name}')
