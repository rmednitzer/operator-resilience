# Governance

> **Status**: draft
> **Last reviewed**: 2026-05-14

This document records the governance of `operator-resilience` at the
current single-maintainer scale. It is honest about what the governance is
and is not, so external contributors can calibrate expectations.

## Maintainer authority

The repository has one maintainer. The maintainer is named in `NOTICE` and
is the owner under `.github/CODEOWNERS`. The maintainer holds final
authority on:

- merging pull requests into `main`;
- approval of changes to `CLAUDE.md` and `.github/copilot-instructions.md`;
- approval of changes to the OADC operating contract
  (`docs/contracts/oadc.md`), the H-state table
  (`docs/resilience/h-state-table.md`), the duress protocol spec
  (`docs/adversarial/duress-protocol-spec.md`), and the autonomous-system
  bridge;
- approval of new policies, registers, or schema changes;
- approval of branch-protection changes and CI workflow changes;
- coordination of the external-reader cadence per
  `EXTERNAL-READER-PROTOCOL.md`.

## Decision-making

At single-maintainer scale, decisions are recorded as artefacts:

- `CLAUDE.md` and `.github/copilot-instructions.md` for operating-contract
  decisions;
- `STATUS.md` for document maturity decisions;
- `CHANGELOG.md` for material change records;
- `LIMITATIONS.md` for declared limits;
- pull request descriptions and commit messages for change rationale.

Contributors who disagree with a decision can open an issue, cite evidence,
and propose an alternative.

## Safety-critical change discipline

Changes affecting OADC, H-state, duress protocols, or the autonomous-system
bridge receive additional scrutiny:

- substantive content additions must be opened as an issue first;
- the issue must reference the standards or empirical work the change
  draws from (aviation CRM, hostage-negotiation literature, NATO HFM-322,
  ISO 10075, etc.);
- review cadence is slower; expect days, not hours.

## Contributor pathway

External contributors are welcome under the discipline encoded in
`CONTRIBUTING.md` and `CLAUDE.md`:

1. Read `CLAUDE.md` and `CONTRIBUTING.md`.
2. Open an issue for substantive content additions.
3. Submit a PR with DCO sign-off.
4. Respond to maintainer review.

## Escalation

Disputes that cannot be resolved in issues escalate to email to the
maintainer at the address in `NOTICE`. There is no committee, no board,
no foundation.

## Code of conduct

The Contributor Covenant 2.1 governs project-space behaviour. See
`CODE_OF_CONDUCT.md`. The maintainer is the enforcement contact.

## Security policy

`.github/SECURITY.md` governs security-relevant disclosure (GitHub's
standard `.github/SECURITY.md` placement applies). The maintainer is the
recipient.

## Sustainability commitments

At the current scale the maintainer commits to:

- responding to security disclosures within 7 calendar days;
- recording material changes in `CHANGELOG.md`;
- preserving the operating contract's discipline.

The maintainer does not commit to:

- a fixed release cadence;
- an SLA on non-security issues;
- indefinite maintainership.

## License

The repository content is licensed under the MIT License. By contributing
you certify under the Developer Certificate of Origin and license your
contribution under the same MIT terms.

## Updating this document

Material changes to governance are recorded in `CHANGELOG.md`.
