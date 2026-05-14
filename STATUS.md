# Document status

> **Status**: draft
> **Last reviewed**: 2026-05-14

Maturity taxonomy per `CLAUDE.md`:

- **planned**: structure exists, content not authored
- **draft**: content exists, not validated against external-reader gate
- **stable**: passed external-reader gate, within review cadence

All authored content in this repository is at `draft`. Promotion to `stable`
is conditional on running the protocol per `EXTERNAL-READER-PROTOCOL.md`.

## Content sections (per README)

| Section | Path | Status | Last reviewed |
|---|---|---|---|
| Operator epistemics | `docs/epistemics/belief-provenance.md` | draft | 2026-05-14 |
| OADC operating contract | `docs/contracts/oadc.md` | draft | 2026-05-14 |
| Contestation resistance | `docs/contracts/contestation-resistance.md` | draft | 2026-05-14 |
| H-state table (H-0..H-4) | `docs/resilience/h-state-table.md` | draft | 2026-05-14 |
| Operator-absent safe state | `docs/cross-cutting/safe-state.md` | draft | 2026-05-14 |
| Threat model (adversarial operator targeting) | `docs/adversarial/threat-model.md` | draft | 2026-05-14 |
| Duress protocol spec | `docs/adversarial/duress-protocol-spec.md` | draft | 2026-05-14 |
| Comms security | `docs/adversarial/comms-security.md` | draft | 2026-05-14 |
| Team dynamics | `docs/cross-cutting/team-dynamics.md` | draft | 2026-05-14 |
| Exercise programme | `docs/exercise/exercise-program.md` | draft | 2026-05-14 |
| Post-event review | `docs/cross-cutting/post-event-review.md` | draft | 2026-05-14 |
| Return-to-duty | `docs/cross-cutting/return-to-duty.md` | draft | 2026-05-14 |
| STPA UCA template (operator-as-controller) | `docs/integration/stpa-uca.md` | draft | 2026-05-14 |
| Autonomous-system bridge | `docs/integration/autonomous-system-bridge.md` | draft | 2026-05-14 |
| Regulatory cross-reference | `docs/integration/regulatory-cross-reference.md` | draft | 2026-05-14 |
| Policies (POL-OR-01..) | `policies/` | draft | 2026-05-14 |
| Canonical registers (YAML) | `data/registers/` | draft | 2026-05-14 |
| Generated register views | `registers/` | draft | 2026-05-14 |
| Schemas | `schemas/` | draft | 2026-05-14 |
| Templates | `templates/` | draft | 2026-05-14 |
| Checklists | `checklists/` | draft | 2026-05-14 |
| Artifact classification index | `artifact-index.yaml` | draft | 2026-05-14 |

## Repository scaffolding

| Document | Status | Last reviewed |
|---|---|---|
| `README.md` | draft | 2026-05-14 |
| `CLAUDE.md` | stable | 2026-05-14 |
| `CONTRIBUTING.md` | draft | 2026-05-14 |
| `.github/SECURITY.md` | draft | 2026-05-14 |
| `CODE_OF_CONDUCT.md` | draft | 2026-05-14 |
| `GOVERNANCE.md` | draft | 2026-05-14 |
| `LIMITATIONS.md` | draft | 2026-05-14 |
| `EXTERNAL-READER-PROTOCOL.md` | draft | 2026-05-14 |
| `STATUS.md` | draft | 2026-05-14 |
| `CHANGELOG.md` | draft | 2026-05-14 |
| `NOTICE` | stable | 2026-05-14 |
| `LICENSE` | stable | 2026-05-14 |
| `REUSE.toml` | draft | 2026-05-14 |
| `LICENSES/MIT.txt` | stable | 2026-05-14 |
| `.github/workflows/validate.yml` | draft | 2026-05-14 |
| `.github/workflows/scorecard.yml` | draft | 2026-05-14 |
| `.github/workflows/dco.yml` | draft | 2026-05-14 |
| `.github/workflows/reuse.yml` | draft | 2026-05-14 |
| `.github/CODEOWNERS` | draft | 2026-05-14 |
| `.github/pull_request_template.md` | draft | 2026-05-14 |
| `.github/ISSUE_TEMPLATE/*` | draft | 2026-05-14 |
| `.github/dependabot.yml` | draft | 2026-05-14 |
| `.github/copilot-instructions.md` | draft | 2026-05-14 |
| `.githooks/*` | draft | 2026-05-14 |

## Updating this document

When a document is touched, update its `Last reviewed` cell in this file and
the top-of-file `> **Last reviewed**:` blockquote in the document itself, and
record material changes in `CHANGELOG.md`.
