# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this repository — including weaknesses in governance artifacts, schema definitions, or validation logic — please report it responsibly.

**Do not open a public issue for security vulnerabilities.**

Instead, use [GitHub Private Vulnerability Reporting](https://github.com/rmednitzer/operator-resilience/security/advisories/new) to submit a report directly. This ensures the issue is triaged privately before any public disclosure.

## Scope

This repository contains governance-as-code artifacts for operator authority, cognition, and resilience. Security concerns include:

- **Schema vulnerabilities:** Flaws in JSON Schemas that could allow invalid or dangerous register entries to pass validation.
- **Validation bypasses:** Weaknesses in `scripts/validate_repo.py` that could miss broken or malicious content.
- **Policy weaknesses:** Defects in OADC definitions, duress protocols, or safe-state specifications that could create unsafe operating conditions.
- **Integrity issues:** Tampering vectors for canonical registers or evidence artifacts.

## Supported Versions

Only the latest version on the `main` branch is actively maintained.

## Response Timeline

- **Acknowledgment:** Within 5 business days of report submission.
- **Assessment:** Initial triage and severity classification within 10 business days.
- **Resolution:** Safety-critical issues are prioritized and follow the safety-critical change process defined in [CONTRIBUTING.md](../CONTRIBUTING.md).
