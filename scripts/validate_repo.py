#!/usr/bin/env python3
"""Repository validator for operator-resilience."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
ARTIFACT_INDEX = ROOT / 'artifact-index.yaml'
SCHEMA_DIR = ROOT / 'schemas'
DATA_DIR = ROOT / 'data' / 'registers'
REGISTER_DIR = ROOT / 'registers'

MD_LINK_RE = re.compile(r'\[(?:[^\]]*)\]\(([^)]+)\)')

errors: List[str] = []
warnings: List[str] = []

REGISTER_SCHEMAS = {
    'oadc-register.yaml': 'oadc-entry.schema.json',
    'h-state-event-register.yaml': 'h-state-event.schema.json',
    'duress-event-register.yaml': 'duress-event.schema.json',
    'exercise-register.yaml': 'exercise-record.schema.json',
    'review-register.yaml': 'review-record.schema.json',
}


def load_yaml(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_schema_store() -> Dict[str, object]:
    store: Dict[str, object] = {}
    for path in SCHEMA_DIR.glob('*.json'):
        schema = load_json(path)
        store[path.name] = schema
        if '$id' in schema:
            store[schema['$id']] = schema
    return store


def resolve_local_refs(obj, store):
    """Resolve local $ref pointers so Draft202012Validator can validate."""
    if isinstance(obj, dict):
        if "$ref" in obj and not obj["$ref"].startswith("http"):
            target = store.get(obj["$ref"])
            if target is None:
                return obj
            merged = resolve_local_refs(target, store)
            extras = {k: resolve_local_refs(v, store) for k, v in obj.items() if k != "$ref"}
            if isinstance(merged, dict):
                out = dict(merged)
                for key, val in extras.items():
                    if key == "required" and isinstance(out.get(key), list) and isinstance(val, list):
                        seen = set(out[key])
                        out[key] = out[key] + [v for v in val if v not in seen]
                    elif key == "properties" and isinstance(out.get(key), dict) and isinstance(val, dict):
                        out[key] = {**out[key], **val}
                    else:
                        out[key] = val
                return out
            return merged
        return {k: resolve_local_refs(v, store) for k, v in obj.items()}
    if isinstance(obj, list):
        return [resolve_local_refs(v, store) for v in obj]
    return obj


def check_artifact_index():
    idx = load_yaml(ARTIFACT_INDEX)
    seen = set()
    for entry in idx.get('artifacts', []):
        path = entry['path']
        if path in seen:
            errors.append(f'DUPLICATE artifact-index entry: {path}')
        seen.add(path)
        if not (ROOT / path).exists():
            errors.append(f'MISSING artifact: {path}')


def check_schemas():
    for schema_file in SCHEMA_DIR.glob('*.json'):
        try:
            schema = load_json(schema_file)
            for ref in _find_refs(schema):
                if ref.startswith('http'):
                    continue
                target = schema_file.parent / ref
                if not target.exists():
                    errors.append(f'BROKEN $ref in {schema_file.name}: {ref}')
        except json.JSONDecodeError as e:
            errors.append(f'INVALID JSON in {schema_file.name}: {e}')


def _find_refs(obj):
    if isinstance(obj, dict):
        if '$ref' in obj:
            yield obj['$ref']
        for value in obj.values():
            yield from _find_refs(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from _find_refs(value)


def check_markdown_links():
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        for match in MD_LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f'BROKEN LINK: {path.relative_to(ROOT)} -> {target}')


def check_yaml_against_schema():
    """Validate register entries against their JSON Schemas."""
    store = build_schema_store()
    for yaml_name, schema_name in REGISTER_SCHEMAS.items():
        path = DATA_DIR / yaml_name
        if not path.exists():
            errors.append(f'MISSING canonical register: data/registers/{yaml_name}')
            continue
        document = load_yaml(path) or {}
        entries = document.get('entries', [])
        if not isinstance(entries, list):
            errors.append(f'Invalid entries list in data/registers/{yaml_name}')
            continue
        if not entries:
            continue
        schema = resolve_local_refs(store[schema_name], store)
        validator = Draft202012Validator(schema)
        for idx, entry in enumerate(entries):
            for err in sorted(validator.iter_errors(entry), key=lambda e: list(e.path)):
                loc = '.'.join(str(p) for p in err.path) or '<root>'
                errors.append(
                    f'SCHEMA {yaml_name} entry {idx} '
                    f'({entry.get("id", "unknown")}): {loc}: {err.message}'
                )


def index_entries() -> Dict[str, Dict[str, object]]:
    """Build a map of all register entry IDs to their data."""
    result: Dict[str, Dict[str, object]] = {}
    for yaml_name in REGISTER_SCHEMAS:
        path = DATA_DIR / yaml_name
        if not path.exists():
            continue
        document = load_yaml(path) or {}
        for entry in document.get('entries', []):
            entry_id = entry.get('id')
            if entry_id in result:
                errors.append(f'DUPLICATE register entry id: {entry_id}')
            result[entry_id] = entry
    return result


def check_cross_references():
    """Validate cross-references between register entries."""
    idx = index_entries()
    reviews = (load_yaml(DATA_DIR / 'review-register.yaml') or {}).get('entries', [])

    for rev in reviews:
        event_ref = rev.get('event_ref')
        if event_ref and event_ref not in idx:
            errors.append(
                f'{rev["id"]} event_ref references non-existent entry {event_ref}'
            )

    duress_events = (load_yaml(DATA_DIR / 'duress-event-register.yaml') or {}).get('entries', [])
    for dur in duress_events:
        review_ref = dur.get('review_ref')
        if review_ref and review_ref not in idx:
            errors.append(
                f'{dur["id"]} review_ref references non-existent entry {review_ref}'
            )


def check_generated_registers():
    """Detect render drift between canonical YAML and committed Markdown views."""
    sys.path.insert(0, str(ROOT / 'scripts'))
    import generate_register_views

    rendered = generate_register_views.render_all(write=False)
    for filename, content in rendered.items():
        target = REGISTER_DIR / filename
        actual = target.read_text(encoding='utf-8') if target.exists() else None
        if actual != content:
            errors.append(
                f'RENDER DRIFT: registers/{filename} is out of date; '
                f'run make render'
            )


def main():
    print('Validating operator-resilience repository...')
    check_artifact_index()
    check_schemas()
    check_yaml_against_schema()
    check_cross_references()
    check_markdown_links()
    check_generated_registers()

    for w in warnings:
        print(f'  WARN: {w}')
    for e in errors:
        print(f'  ERROR: {e}')

    if errors:
        print(f'\nVALIDATION FAILED: {len(errors)} error(s), {len(warnings)} warning(s)')
        sys.exit(1)
    else:
        print(f'\nVALIDATION PASSED: {len(warnings)} warning(s)')
        sys.exit(0)


if __name__ == '__main__':
    main()
