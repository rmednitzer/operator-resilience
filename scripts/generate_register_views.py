#!/usr/bin/env python3
"""Generate Markdown register views from canonical YAML sources."""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data' / 'registers'
REGISTER_DIR = ROOT / 'registers'


def load_yaml(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_view(yaml_path: Path):
    data = load_yaml(yaml_path)
    name = yaml_path.stem
    entries = data.get('entries', []) if data else []

    md_path = REGISTER_DIR / f'{name}.md'
    lines = [
        f'# {name.replace("-", " ").title()}',
        '',
        f'**Generated view — do not edit directly.** Edit `data/registers/{yaml_path.name}` instead.',
        '',
    ]

    if not entries:
        lines.append('*No entries.*')
    else:
        # Auto-detect columns from first entry
        keys = list(entries[0].keys())
        lines.append('| ' + ' | '.join(keys) + ' |')
        lines.append('|' + '|'.join(['---'] * len(keys)) + '|')
        for entry in entries:
            row = '| ' + ' | '.join(str(entry.get(k, '')) for k in keys) + ' |'
            lines.append(row)

    md_path.write_text('\n'.join(lines) + '\n')
    print(f'  Generated: {md_path.relative_to(ROOT)}')


def main():
    REGISTER_DIR.mkdir(exist_ok=True)
    print('Generating register views...')
    for yaml_file in sorted(DATA_DIR.glob('*.yaml')):
        generate_view(yaml_file)
    print('Done.')


if __name__ == '__main__':
    main()
