# Operator Resilience

Governance-as-code for operator authority, cognition, and resilience under adversarial, degraded, and high-stress conditions.

## Purpose

Operators — human controllers of IT, OT, autonomous, and safety-critical systems — face the same pressures that degrade any safety-critical function: they can be targeted, misled, exhausted, or coerced. Standard sociotechnical design assumes the operator is acting in good faith, with accurate information, under manageable cognitive load. This repository governs the conditions where those assumptions break: the operator's information is wrong, stale, or adversarially manipulated; the operator is coerced, deceived, or under psychological pressure; cognitive capacity has degraded below the threshold the control structure assumes; the operating contract is contested, violated, or attacked; the operator is acting against organizational interests; or the team's collective cognition has failed.

The core problem is the operator–authority–auditability triangle. High operator authority enables fast response but expands the unsupervised decision space. Tight procedural controls reduce error but slow response and create brittleness. Continuous auditability enables accountability but adds cognitive load. This repository treats the operator as a governed boundary — with formal authority contracts, epistemic integrity requirements, degradation modes, and evidence capture — analogous to how cyber-physical systems treat their physical control boundaries.

## What is in the repository

**Operator epistemics** — [`docs/epistemics/belief-provenance.md`](docs/epistemics/belief-provenance.md). Belief provenance model mapping to Endsley's three-level situational awareness framework. Operator information intake as a trust boundary with source authentication, freshness, cross-validation, authority, and consistency checks. Evidence tagging (`[F]`/`[I]`/`[S]`) with confidence levels `{50, 65, 70, 75, 80, 85, 90}` and confidence gating. Epistemic degradation markers including out-of-the-loop (OOTL) degradation. Pre-decision epistemic check format.

**Operating contracts** — [`docs/contracts/oadc.md`](docs/contracts/oadc.md) · [`docs/contracts/contestation-resistance.md`](docs/contracts/contestation-resistance.md). Operator Authority Degradation Contract (OADC) — a formal table defining how operator authority narrows as conditions degrade, covering duty duration, incident duration, single-source claims, time pressure, unverified authority, self-reported degradation, epistemic markers, contested environments, passive monitoring (OOTL), circadian effects, and organizational stress. Contract contestation resistance patterns. Meta-contract governance. Verification integrity requirements.

**Cognitive resilience** — [`docs/resilience/h-state-table.md`](docs/resilience/h-state-table.md) · [`docs/cross-cutting/safe-state.md`](docs/cross-cutting/safe-state.md). Human mode-state table (H-0 to H-4) with full taxonomy: observable indicators, decision authority limits, support requirements, and recovery criteria per state. Assessment methods, proactive and reactive degradation detection, mandatory handoff protocol, CACE (Changing Anything Changes Everything) for operator state changes, team mode-state. Operator-absent safe state specification framework.

**Adversarial operator targeting** — [`docs/adversarial/threat-model.md`](docs/adversarial/threat-model.md) · [`docs/adversarial/duress-protocol-spec.md`](docs/adversarial/duress-protocol-spec.md) · [`docs/adversarial/comms-security.md`](docs/adversarial/comms-security.md). Threat model covering social engineering, duress, information manipulation, fatigue exploitation, relationship exploitation, and insider threat — with attack chain analysis and OADC control mappings. Duress protocol specification: signal architecture (verbal/digital/physical), authority containment, evidence integrity, recovery. Incident communications security: closed-loop (readback/hearback) protocol, channel authentication, compromised-channel handling.

**Team dynamics** — [`docs/cross-cutting/team-dynamics.md`](docs/cross-cutting/team-dynamics.md). Collective cognitive failure modes: groupthink, information asymmetry, authority diffusion, shared OOTL, authority gradient suppression, collective epistemic overconfidence. Mandatory challenge-and-response protocol adapted from aviation CRM. Team mode-state derivation. Cross-organizational shared operating contracts.

**Exercise and validation** — [`docs/exercise/exercise-program.md`](docs/exercise/exercise-program.md) · [`docs/cross-cutting/post-event-review.md`](docs/cross-cutting/post-event-review.md) · [`docs/cross-cutting/return-to-duty.md`](docs/cross-cutting/return-to-duty.md). Seven exercise types (ET-1–ET-7) with cadences, acceptance criteria, evidence capture, and failure responses. Post-event review: trigger deadlines, review objectives, independence requirements, corrective action tracking, pattern escalation, learning loop closure. Return-to-duty protocol: H-state-differentiated recovery requirements, structured readiness check, H-state upgrade declaration.

**System integration** — [`docs/integration/stpa-uca.md`](docs/integration/stpa-uca.md) · [`docs/integration/autonomous-system-bridge.md`](docs/integration/autonomous-system-bridge.md). STPA UCA template for operator-as-controller: four UCA types with worked examples (IT/SRE, OT/ICS, GCS) and UCA–OADC linkage. Autonomous-system bridge: OADC state → authority permission set, H-state → system operating mode, epistemic state → connectivity state.

**Regulatory cross-reference** — [`docs/integration/regulatory-cross-reference.md`](docs/integration/regulatory-cross-reference.md). Indicative mapping to EU AI Act Arts. 9, 14, 26; NIS2 Arts. 21, 23; CER Arts. 13–14; DORA Art. 11; Machinery Reg. 2023/1230; EU Working Time Directive 2003/88/EC; CRA 2024/2847 (with applicability decision tree); GDPR Arts. 6, 9, 32, 35 (with DPIA blocking requirement); Seveso III; MIL-STD-882E; DoD Directive 3000.09; NATO STANAG 4670, STANAG 7201, HFM-322; ISO 10075, ISO 11064; IEC 62443.

## Canonical data model

The canonical source of truth for registers is machine-readable YAML under `data/registers/`. The Markdown files in `registers/` are generated views.

Current canonical registers:
- `data/registers/oadc-register.yaml` — Operator Authority Degradation Contract instances
- `data/registers/h-state-event-register.yaml` — H-state assessment events
- `data/registers/duress-event-register.yaml` — Duress events (real and exercise)
- `data/registers/exercise-register.yaml` — Exercise execution records
- `data/registers/review-register.yaml` — Post-event review records

## Design principles

1. **Correctness > Safety > Auditability > Completeness > Speed**
2. **Authority is a contract, not a setting.**
3. **Hostile is the default assumption.**
4. **Degrade gracefully, halt safely.**
5. **Auditability survives the event.**
6. **Operator performance is a safety-critical function.**
7. **Exercise or it does not exist.**
8. **The schema is authoritative.** Human-readable tables are rendered outputs, not the primary data plane.

## Companion repository

This repository is standalone and environment-agnostic but complements the following governance repo by the same owner:

- [`autonomous-platform-assurance`](https://github.com/rmednitzer/autonomous-platform-assurance): platform authority hierarchy (AL-0 to AL-8), CDIL operation, hostile-environment security, disconnected key management, and mission safety. The OADC governs the operator side of the authority boundary; AL governs the platform side.

## Integration interfaces

This repository integrates with adjacent governance layers through defined interfaces:

- **Evidence pipeline:** Decision logs, OADC trigger events, exercise records, and post-event reviews produce evidence artifacts. These integrate with whatever evidence store your environment uses (WORM storage, signed artifacts, hash-chained audit logs). Retention tiers are defined in the governance policy; the transport mechanism is environment-specific.
- **Hazard analysis:** Operator UCAs (unsafe control actions) from the STPA integration section feed into whatever hazard register your environment maintains. The STPA UCA template is self-contained.
- **Authority models:** Where the operator controls a system with a formal authority hierarchy (authority levels, delegation contracts, connectivity-state machines), the OADC links to it through the autonomous-system bridge. The mapping is defined per deployment, not hard-coded.
- **IAM enforcement:** OADC constraints (two-person approval, session restrictions, time-bounded access) are technically enforced through whatever IAM system your environment uses. This repo defines the contract; IAM enforces it.

## Getting started

1. Read [`docs/epistemics/belief-provenance.md`](docs/epistemics/belief-provenance.md) — understand the epistemic model and `[F]/[I]/[S]` tagging
2. Read [`docs/contracts/oadc.md`](docs/contracts/oadc.md) — understand how operator authority degrades
3. Read [`docs/resilience/h-state-table.md`](docs/resilience/h-state-table.md) — understand the H-0–H-4 human mode-state hierarchy
4. Adapt [`policies/POL-OR-01-operator-governance.md`](policies/POL-OR-01-operator-governance.md) to your organization
5. Complete a DPIA before operational use in EU contexts — see [`docs/integration/regulatory-cross-reference.md`](docs/integration/regulatory-cross-reference.md) §9.5
6. Populate `data/registers/oadc-register.yaml` with environment-specific OADC instances using the template at `templates/oadc/TEMPLATE-oadc-instance.md`
7. Define per-environment safe states per [`docs/cross-cutting/safe-state.md`](docs/cross-cutting/safe-state.md)
8. Establish duress protocols per [`docs/adversarial/duress-protocol-spec.md`](docs/adversarial/duress-protocol-spec.md) for applicable environments
9. Run `make validate` before review or merge
10. Execute initial exercises per [`docs/exercise/exercise-program.md`](docs/exercise/exercise-program.md) — start with ET-3 (OADC validation) and ET-7 (safe-state test)

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review process, commit conventions, and branch model.

## License

[MIT](LICENSE)
