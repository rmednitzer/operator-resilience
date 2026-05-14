# Known limitations

> **Status**: draft
> **Last reviewed**: 2026-05-14

This document is the counterpart to the stated-purpose paragraph in
`README.md`. Where `README.md` describes what the repository is, this
document describes what it is not, and what work would be required to
change that.

Naming a limit is not the same as scheduling a fix. Some limits are
deliberate scope decisions that match the repository's identity as a
governance-as-code artefact set for operator authority and cognitive
resilience, not as a deployed operational programme. Naming them is part
of the assurance posture.

## L1. H-state and OADC assessment relies on operator self-report

**Current state.** `docs/resilience/h-state-table.md` and
`docs/contracts/oadc.md` define observable indicators per H-state, decision
authority limits, and assessment methods. Assessment in the current
specification is structured (pre-decision check, mandatory handoff
protocol, post-event review), but ultimately relies on operator and
peer self-report. Biometric integration (heart-rate variability, eye
tracking, EEG), physiological monitoring, or actigraphy is not committed.

**Implication.** The H-state assessment is as accurate as the operator's
introspective ability and the team's challenge-and-response discipline.
Under severe degradation or active deception, self-report is unreliable.
The duress protocol (`docs/adversarial/duress-protocol-spec.md`) addresses
the active-deception case for declared duress; covert cognitive
compromise without operator awareness remains a gap.

**What would close it.** Biometric integration as an optional augmentation
is a scope-shift. The privacy and consent regime (GDPR Art. 6, 9, 32, 35;
Working Time Directive 2003/88/EC) makes this non-trivial. A DPIA-blocked
integration with separate ethical review is the only defensible path.

**Intended scope.** Tier 1 framing in this PR. Biometric augmentation is
an open scope decision, not committed work.

## L2. Duress protocols are normative patterns, not field-validated

**Current state.** `docs/adversarial/duress-protocol-spec.md` specifies
signal architecture (verbal / digital / physical), authority containment,
evidence integrity, and recovery. The exercise programme in
`docs/exercise/exercise-program.md` (ET-1..ET-7) defines validation
activities. The patterns are derived from aviation CRM, hostage-
negotiation practice, and tactical communications doctrine. They have not
been validated against the specific deployment environments the repository
speaks to (SRE / IT operations rooms, OT / ICS control rooms, autonomous-
platform GCS).

**Implication.** Adopting organisations should treat the duress protocol as
a reference specification subject to exercise validation in their
environment before declaring it operational. ET-6 (duress drill) is
the direct validation activity.

**What would close it.** Out of scope for the repository (validation must
happen in adopting deployments). The exercise programme structures the
validation activity; the validation itself is the adopter's responsibility.

**Intended scope.** No close-out planned. Limit named for honest framing.

## L3. DPIA is a precondition; no DPIA template is committed

**Current state.** `docs/integration/regulatory-cross-reference.md` §9.5
declares that a Data Protection Impact Assessment under GDPR Article 35 is
a blocking precondition for operational use in EU contexts. The repository
does not commit a DPIA template adapted to the OADC / H-state / duress
processing.

**Implication.** Adopters must either commission a DPIA from a qualified
DPO or adapt a generic DPIA template to the specific processing surface
(operator identification, cognitive-state markers, duress events, exercise
records, post-event review records).

**What would close it.**

- Tier 2 (focused follow-up): a DPIA template under `templates/dpia/` with
  the processing surface, lawful basis options, recipient categories,
  retention reasoning, and risk assessment scaffolded.
- Tier 3: a worked DPIA for a reference deployment scenario.

**Intended scope.** Tier 2 is a candidate for a separate PR.

## L4. Exercise programme cadence is not enforced

**Current state.** `docs/exercise/exercise-program.md` defines seven
exercise types with target cadences. `data/registers/exercise-register.yaml`
records execution. There is no CI check that any given exercise type's
last execution respects the cadence the type declares.

**Implication.** A reader cannot tell, in CI, whether an exercise type is
overdue. Cadence discipline depends on adopter operational rigour.

**What would close it.** A small CI script that reads
`exercise-register.yaml`, computes overdue exercises per ET type, and
flags them. Similar in spirit to drift-watch in `platform-blueprint`.

**Intended scope.** Tier 2 (focused follow-up).

## L5. External-reader gate has not been executed

**Current state.** `EXTERNAL-READER-PROTOCOL.md` defines the gate. The
qualified reader competence required (human factors / safety-critical
operations / IR practice) is narrow. The gate has not been executed.

**Implication.** No document is at `stable`. The reader pool is specialised.

**What would close it.** Identification of a qualified external reader,
execution of the ten-question protocol, recording of findings, remediation,
promotion in `STATUS.md`.

**Intended scope.** Open.

## L6. REUSE per-file SPDX retrofit not landed

**Current state.** REUSE 3.3 compliance is asserted at the repository level
via `REUSE.toml` and `LICENSES/Apache-2.0.txt`; CI verifies via
`.github/workflows/reuse.yml`. Existing files do not carry per-file SPDX
headers; the aggregate annotation carries the licence assertion.

**Implication.** REUSE-compliant at aggregate level. Sufficient under REUSE
3.3.

**What would close it.** Retrofit PR adding SPDX headers to every authored
file.

**Intended scope.** Tier 2 (deferred follow-up).

## L7. Companion-repository integration (autonomous-platform-assurance) is interface-level

**Current state.** The autonomous-system bridge in
`docs/integration/autonomous-system-bridge.md` defines the mapping between
OADC state and authority permission set, H-state and system operating
mode, epistemic state and connectivity state. The mapping is normative and
the AL-0..AL-8 taxonomy in the companion repository is normative; the joint
mapping has not been exercised end-to-end.

**Implication.** Co-deployment of this repository with
`autonomous-platform-assurance` requires an integration test (exercise) to
validate that operator-side and platform-side state machines compose as
the bridge claims.

**What would close it.** A joint exercise scenario authored in both
repositories. Out of scope for either alone.

**Intended scope.** No close-out planned in this PR.

## L8. DCO workflow deferred to follow-up PR

**Current state.** The bootstrap commit on this branch carries a
`Signed-off-by` email that does not match the author email recognised by
the `tim-actions/dco` action, so the DCO workflow cannot pass on the
bootstrap commit. To avoid blocking the licence-alignment work, the DCO
workflow is configured `on: workflow_dispatch` only; it does not run on
pull requests.

**Implication.** DCO sign-off discipline is preserved by maintainer
discipline as recorded in `GOVERNANCE.md` and `CONTRIBUTING.md`, but the
CI gate is currently advisory rather than enforced.

**What would close it.** A follow-up PR that (a) rewrites the bootstrap
commit's sign-off email to match the author email, or otherwise reconciles
the two; (b) restores `on: pull_request` for `.github/workflows/dco.yml`;
(c) enables branch protection requiring the DCO check on `main`.

**Intended scope.** Tier 2 (focused follow-up PR).

## L9. Outstanding scaffolding clarity items

**Current state.** Several scaffolding clarity items remain after the
licence-alignment round:

- `.github/CODEOWNERS` does not yet cover all new paths added in the
  open-source-foundation bootstrap (notably the workflow files under
  `.github/workflows/`, `LICENSES/`, `REUSE.toml`, `GOVERNANCE.md`,
  `LIMITATIONS.md`, `STATUS.md`, `EXTERNAL-READER-PROTOCOL.md`,
  `CODE_OF_CONDUCT.md`).
- Per-file SPDX headers are still aggregate-only (see L6).

**Implication.** Path-targeted review routing via CODEOWNERS is incomplete;
at single-maintainer scale this is cosmetic, but it will matter when the
contributor base grows.

**What would close it.** A scaffolding-clarity follow-up PR that extends
CODEOWNERS to cover the new paths and lands the L6 SPDX retrofit.

**Intended scope.** Tier 2 (focused follow-up PR).

## How to read this document

- If you are using the repository as a reading map for operator-resilience
  programme design: L1 and L2 are framing limits; the depth is the
  deliverable.
- If you are using the repository as a starting point for an operational
  programme in the EU: L3 (DPIA) is a blocking limit before deployment.
- If you are using the repository as a substitute for occupational
  health, clinical guidance, or legal advice: it is not one.

## Updating this document

Limits are reviewed under the same cadence as `STATUS.md` and
`CHANGELOG.md`. When a limit is closed, the entry is moved to a `Closed
limits` section at the end of this document.
