# operator-resilience

Governance-as-code for operator authority, cognition, and resilience under adversarial, degraded, and high-stress conditions.

## Purpose

Operators — human controllers of IT, OT, autonomous, and safety-critical systems — face the same pressures that degrade any safety-critical function: they can be targeted, misled, exhausted, or coerced. Standard sociotechnical design assumes the operator is acting in good faith, with accurate information, under manageable cognitive load. This repository governs the conditions where those assumptions break: the operator's information is wrong, stale, or adversarially manipulated; the operator is coerced, deceived, or under psychological pressure; cognitive capacity has degraded below the threshold the control structure assumes; the operating contract is contested, violated, or attacked; the operator is acting against organizational interests; or the team's collective cognition has failed.

The core problem is the operator–authority–auditability triangle. High operator authority enables fast response but expands the unsupervised decision space. Tight procedural controls reduce error but slow response and create brittleness. Continuous auditability enables accountability but adds cognitive load. This repository treats the operator as a governed boundary — with formal authority contracts, epistemic integrity requirements, degradation modes, and evidence capture — analogous to how cyber-physical systems treat their physical control boundaries.

## What is in the repository

**Operator epistemics.** Belief provenance model mapping to Endsley's three-level situational awareness framework. Operator information intake as a trust boundary with source authentication, freshness, cross-validation, authority, and consistency checks. Epistemic degradation markers including out-of-the-loop (OOTL) degradation. Pre-decision epistemic check with assumptions, constraints, unknowns, and confidence gating.

**Operating contracts.** Operator Authority Degradation Contract (OADC) — a formal table defining how operator authority narrows as conditions degrade, covering duty duration, incident duration, single-source claims, time pressure, unverified authority, self-reported degradation, epistemic markers, contested environments, passive monitoring (OOTL), circadian effects, and organizational stress. Contract contestation resistance patterns. Meta-contract governance. Verification integrity requirements.

**Cognitive resilience.** Human mode-state table (H-0 to H-4) analogous to system degraded-mode hierarchies. Proactive and reactive degradation detection. Stress-adapted decision aids with pre-committed decision trees. Mandatory handoff protocol. CACE (Changing Anything Changes Everything) for operator state changes.

**Adversarial operator targeting.** Threat model covering social engineering, duress, information manipulation, fatigue exploitation, and relationship exploitation. Insider threat controls at the operating-contract layer. Duress protocols with covert signaling, authority containment, and recovery. Incident communications security with closed-loop (readback/hearback) protocol. Information integrity verification.

**Team dynamics.** Collective cognitive failure modes: groupthink, information asymmetry, authority diffusion. Challenge-and-response protocol adapted from aviation CRM (Crew Resource Management). Team mode-state. Cross-organizational shared operating contracts.

**Exercise and validation.** Seven exercise types with cadences, acceptance criteria, and evidence capture. Post-event review and learning loop with defined triggers and review timelines. Return-to-duty protocol with structured readiness checks.

**System integration.** STPA (System-Theoretic Process Analysis) UCA (unsafe control action) template for operator-as-controller. Operator-absent safe state specifications per operating context. Autonomous-system bridge mapping OADC to authority hierarchies, H-state to system modes, and epistemic state to connectivity state.

**Regulatory cross-reference.** Indicative mapping to EU AI Act Art. 14, NIS2 Art. 21, MIL-STD-882E, DoD Directive 3000.09.

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

## Integration interfaces

This repository is standalone. It does not depend on any specific platform, safety, or autonomous-system governance framework. It integrates with adjacent governance layers through defined interfaces:

- **Evidence pipeline:** Decision logs, OADC trigger events, exercise records, and post-event reviews produce evidence artifacts. These integrate with whatever evidence store your environment uses (WORM storage, signed artifacts, hash-chained audit logs). Retention tiers are defined in the governance policy; the transport mechanism is environment-specific.
- **Hazard analysis:** Operator UCAs (unsafe control actions) from the STPA integration section feed into whatever hazard register your environment maintains. The STPA UCA template is self-contained.
- **Authority models:** Where the operator controls a system with a formal authority hierarchy (authority levels, delegation contracts, connectivity-state machines), the OADC links to it through the autonomous-system bridge. The mapping is defined per deployment, not hard-coded.
- **IAM enforcement:** OADC constraints (two-person approval, session restrictions, time-bounded access) are technically enforced through whatever IAM system your environment uses. This repo defines the contract; IAM enforces it.

## Getting started

1. Read `docs/epistemics/belief-provenance.md` — understand the epistemic model
2. Read `docs/contracts/oadc.md` — understand how operator authority degrades
3. Adapt `policies/POL-OR-01-operator-governance.md` to your organization
4. Populate `data/registers/oadc-register.yaml` with environment-specific OADC instances
5. Build templates: decision log, duress protocol, exercise program
6. Run `make validate` before review or merge
7. Execute initial exercises per `docs/exercise/exercise-program.md`

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review process, commit conventions, and branch model.

## License

[MIT](LICENSE)
