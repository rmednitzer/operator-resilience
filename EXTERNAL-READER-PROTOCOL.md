# External-reader protocol

> **Status**: draft
> **Last reviewed**: 2026-05-14

The external-reader test is the gate before any document in this repository
is promoted from `draft` to `stable` per `STATUS.md`. It also gates major
refactors of the OADC, H-state table, duress protocol, or the operating
contract.

## Purpose

The repository is authored by a maintainer and AI assistants operating
under `CLAUDE.md` and `.github/copilot-instructions.md`. Both are inside
the framing the repository expresses. An external reader, with no prior
context, can identify whether the operator-as-controller framing, the OADC,
the H-state hierarchy, the duress protocol, and the regulatory cross-
reference are comprehensible and trustworthy from cold read.

## When the test runs

- **Pre-promotion**: before any document moves from `draft` to `stable`.
- **Major refactor**: any change to OADC, H-state table, duress protocol,
  autonomous-system bridge, or operating contract.
- **Recurring**: at minimum every 12 months.

## Who qualifies as external reader

The reader must be:

- not the maintainer;
- not currently part of the maintainer's day-to-day operations or
  human-factors peer group;
- competent in at least one of: human-factors engineering for safety-
  critical operations (HF/E qualification, aviation CRM background, OT/ICS
  control-room experience, or equivalent); incident response and post-event
  review practice; security operations (SOC, IR, threat hunting); or
  occupational mental-health practice in high-stress environments;
- willing to read with sufficient time and attention.

Readers without HF/E qualification may still serve if they bring deep IR or
SecOps practice; the questions are framed to surface both lenses.

The reader's identity and findings remain confidential to the maintainer
unless the reader consents to attribution.

## What the reader is asked

1. **Structure**. From `README.md` and `STATUS.md`, can you predict what is
   in the repository and where to find it?
2. **Audience**. Is the operator-as-controller framing applicable to the
   operational environments you know (IT/SRE, OT/ICS, autonomous-platform
   GCS, or others)?
3. **Epistemics**. Read `docs/epistemics/belief-provenance.md`. Is the `[F]`
   / `[I]` / `[S]` tagging with confidence levels usable in real-time
   decision logging without imposing unsustainable cognitive overhead?
4. **OADC**. Read `docs/contracts/oadc.md`. Are the authority-degradation
   rows actionable? Could a control-room operator be trained on this in a
   one-day session?
5. **H-state table**. Read `docs/resilience/h-state-table.md`. Are the
   observable indicators per state distinguishable in practice? Would
   peer-assessment be reliable enough to trigger the rows it specifies?
6. **Duress protocol**. Read `docs/adversarial/duress-protocol-spec.md`.
   Is the verbal / digital / physical signal architecture covert enough to
   survive the threat model? Is the authority containment specific enough
   to be enforced by an IAM system?
7. **Exercise programme**. Read `docs/exercise/exercise-program.md`. Are
   the ET-1..ET-7 types distinct enough? Do the cadences feel realistic
   for the team sizes the repository targets?
8. **Adversarial threat model**. Pick one threat vector (social engineering,
   duress, information manipulation, fatigue exploitation, relationship
   exploitation, insider). Does the attack chain feel real? Are the OADC
   control mappings load-bearing?
9. **Regulatory cross-reference**. The DPIA blocking requirement is
   declared in `docs/integration/regulatory-cross-reference.md` §9.5. Is
   the framing tight enough that an adopter would not mistake the
   repository for a DPIA substitute?
10. **Trust**. Would you trust this repository as one input among several
    when designing or assessing an operator-resilience programme? Why or
    why not?

The reader may raise concerns not covered by the questions.

## Pass criteria

The test passes when the reader's answers support:

- structure and audience are comprehensible from cold read;
- the operator-as-controller framing is applicable to at least one
  operational environment the reader knows;
- the OADC and H-state semantics are trainable and operable;
- the duress protocol is implementable;
- the regulatory cross-reference is honest;
- the reader's trust answer is positive or conditionally positive.

## Fail response

If the test fails, the maintainer:

1. Records the findings.
2. Categorises as structural / substantive / opinion.
3. Remediates structural findings before re-running.

## How findings are recorded

Responses are recorded under `docs/reviews/` or in the maintainer's evidence
repository.

## Maintainer's obligations to the reader

- compensate the reader's time appropriately;
- not press the reader to soften negative findings;
- not retaliate against honest negative findings;
- thank the reader in `CHANGELOG.md` with consent.

## Limitations

This protocol is a maintainer's discipline, not a substitute for:

- clinical assessment by qualified occupational practitioners;
- safety-of-the-intended-functionality (SOTIF) assessment for any
  autonomous-platform integration;
- DPIA by a qualified Data Protection Officer for any operational use
  involving personal data;
- legal review by qualified counsel for reliance on the regulatory
  cross-reference in a real engagement.
