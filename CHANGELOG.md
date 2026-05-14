# Changelog

> **Status**: draft
> **Last reviewed**: 2026-05-14

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This repository is documentation rather than a versioned product; material
changes are dated rather than versioned.

## [Unreleased]

### Added

- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).
- `NOTICE` declaring MIT licence and the DPIA precondition for EU
  operational use.
- `REUSE.toml` and `LICENSES/MIT.txt` for REUSE 3.3 compliance at the
  aggregate level. Per-file SPDX retrofit deferred (see `LIMITATIONS.md` L6).
- `STATUS.md` recording document maturity per section.
- `LIMITATIONS.md` recording the known limits (L1 self-report reliance,
  L2 duress protocols not field-validated, L3 DPIA blocking with no
  template committed, L4 exercise cadence not enforced, L5 external-
  reader gate pending, L6 REUSE per-file retrofit, L7 companion-repo
  integration not jointly exercised).
- `GOVERNANCE.md` recording single-maintainer governance, the safety-
  critical change discipline, and the contributor pathway.
- `EXTERNAL-READER-PROTOCOL.md` defining the qualified-human-reader gate,
  with questions adapted to the OADC / H-state / duress / exercise domain.
- `.github/workflows/scorecard.yml` for OpenSSF Scorecard.
- `.github/workflows/dco.yml` enforcing DCO sign-off.
- `.github/workflows/reuse.yml` verifying REUSE 3.3 compliance.

### Changed

- None in this entry beyond additions.

### Notes

This addition imports governance discipline from the `platform-blueprint`
repository's May 2026 open-source-foundation audit cycle. It does not touch
content under `docs/`, `data/`, `registers/`, `policies/`, `schemas/`,
`templates/`, or `checklists/`.
