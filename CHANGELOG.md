# Changelog

> **Status**: draft
> **Last reviewed**: 2026-05-14

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This repository is documentation rather than a versioned product; material
changes are dated rather than versioned.

## [Unreleased]

### Added

- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).
- `NOTICE` declaring the Apache License 2.0, the DPIA precondition for EU
  operational use, and the maintainer contact email.
- `REUSE.toml` and `LICENSES/Apache-2.0.txt` for REUSE 3.3 compliance at
  the aggregate level. Per-file SPDX retrofit deferred (see
  `LIMITATIONS.md` L6).
- `LICENSES/CC-BY-4.0.txt` covering the verbatim Contributor Covenant 2.1
  text in `CODE_OF_CONDUCT.md` (Contributor Covenant is CC-BY-4.0).
- `STATUS.md` recording document maturity per section, with an
  `n/a (canonical text)` row class for files that are verbatim canonical
  upstream text and are therefore exempt from the external-reader gate.
- `LIMITATIONS.md` recording the known limits (L1 self-report reliance,
  L2 duress protocols not field-validated, L3 DPIA blocking with no
  template committed, L4 exercise cadence not enforced, L5 external-
  reader gate pending, L6 REUSE per-file retrofit, L7 companion-repo
  integration not jointly exercised, L8 DCO workflow deferral, L9
  outstanding scaffolding clarity).
- `GOVERNANCE.md` recording single-maintainer governance, the safety-
  critical change discipline, and the contributor pathway.
- `EXTERNAL-READER-PROTOCOL.md` defining the qualified-human-reader gate,
  with questions adapted to the OADC / H-state / duress / exercise domain.
- `.github/workflows/scorecard.yml` for OpenSSF Scorecard.
- `.github/workflows/dco.yml` enforcing DCO sign-off (currently configured
  `on: workflow_dispatch` only, pending the L8 follow-up).
- `.github/workflows/reuse.yml` verifying REUSE 3.3 compliance.

### Changed

- Licence declaration corrected from MIT to Apache-2.0 across `NOTICE`,
  `REUSE.toml`, `GOVERNANCE.md`, `CHANGELOG.md`, and CI workflow SPDX
  headers. `LICENSES/MIT.txt` was replaced by `LICENSES/Apache-2.0.txt`
  matching the canonical `LICENSE` file.
- `.github/workflows/dco.yml` reconfigured to `on: workflow_dispatch` only
  (no `pull_request` trigger) to avoid blocking on the bootstrap commit's
  Signed-off-by email mismatch; see `LIMITATIONS.md` L8 for the
  follow-up plan.
- `.github/workflows/scorecard.yml` trigger surface confirmed correct
  (no `pull_request` trigger; the workflow runs on `branch_protection_rule`,
  scheduled cron, and `push` to `main`).
- `NOTICE` extended with the maintainer contact email so external
  reporters have a direct address rather than only a documentation path.
- `STATUS.md` adds an `n/a (canonical text)` row class for files that are
  verbatim canonical upstream text (the licence files, `NOTICE`,
  `CODE_OF_CONDUCT.md`) and exempts those files from the external-reader
  gate. `CLAUDE.md` remains `stable`.
- `GOVERNANCE.md` security-disclosure SLA aligned with `.github/SECURITY.md`
  (acknowledgment within 5 business days; initial triage and severity
  classification within 10 business days), replacing the previous
  7-calendar-day commitment.
- `GOVERNANCE.md` softens the CODEOWNERS-as-owner claim to "primary
  reviewer; CODEOWNERS may be expanded".
- `CODE_OF_CONDUCT.md` Enforcement section now lists a direct email
  (`r.mednitzer@outlook.com`) rather than chaining through
  `.github/SECURITY.md` and `NOTICE`.

### Notes

This addition imports governance discipline from the `platform-blueprint`
repository's May 2026 open-source-foundation audit cycle. It does not touch
content under `docs/`, `data/`, `registers/`, `policies/`, `schemas/`,
`templates/`, or `checklists/`.
