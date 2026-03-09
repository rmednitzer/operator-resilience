#!/usr/bin/env python3
"""Repository validator for operator-resilience."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ARTIFACT_INDEX = ROOT / 'artifact-index.yaml'
SCHEMA_DIR = ROOT / 'schemas'
DATA_DIR = ROOT / 'data' / 'registers'

MD_LINK_RE = re.compile(r'\[(?:[^\]]*)\]\(([^)]+)\)')

errors: list[str] = []
warnings: list[str] = []


def load_yaml(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


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
            load_json(schema_file)
        except json.JSONDecodeError as e:
            errors.append(f'INVALID JSON in {schema_file.name}: {e}')


def check_markdown_links():
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = path.read_text()
        for match in MD_LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f'BROKEN LINK: {path.relative_to(ROOT)} -> {target}')


def check_register_yaml():
    for yaml_file in DATA_DIR.glob('*.yaml'):
        try:
            data = load_yaml(yaml_file)
            if data is None:
                warnings.append(f'EMPTY register: {yaml_file.name}')
        except yaml.YAMLError as e:
            errors.append(f'INVALID YAML in {yaml_file.name}: {e}')


def main():
    print('Validating operator-resilience repository...')
    check_artifact_index()
    check_schemas()
    check_markdown_links()
    check_register_yaml()

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
