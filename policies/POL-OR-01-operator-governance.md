# POL-OR-01: Operator Governance Policy

**Version:** 1.0 DRAFT
**Owner:** Safety/Security Lead
**Approved by:** [Name and date — requires management sign-off]
**Review cycle:** Annual + after any OADC-triggering incident or duress event
**Classification:** Internal

## Purpose

Establish the governance framework for operator authority, epistemic integrity, cognitive resilience, and adversarial defense across all operating environments where human operators make or approve consequential decisions.

## Scope

All operators in roles where their decisions can cause or fail to prevent a high-consequence outcome. Applies to IT/SRE on-call operators, OT/ICS operators, autonomous system supervisors, incident commanders, and any personnel in the decision chain for safety-critical, security-critical, or regulatory-significant actions.

## Policy statements

1. No operator shall exercise authority over consequential actions without a valid Operator Authority Degradation Contract (OADC) defined for their operating environment.
2. OADC parameters (duty duration limits, minimum review thresholds, buddy-pair triggers) shall be defined in advance, not during incidents.
3. All high-consequence decisions shall be logged using the pre-decision epistemic check format: assumptions (tagged [F], [I], or [S]), constraints, unknowns, and confidence level.
4. If decision confidence is below 70%, the operator shall state what checks would raise it and proceed only with safe, reversible partial actions.
5. Duress protocols shall be pre-established, trained, and tested (minimum annual) for all operating environments where coercion is a credible threat.
6. When no operator meeting OADC requirements is available, the system shall enter a pre-defined operator-absent safe state. Safe states must be defined, documented, and tested before operational use.
7. Operator degradation to H-3 or H-4 triggers mandatory handoff. If no alternate is available, the system enters safe state.
8. All OADC trigger events, break-glass exceptions, duress signals, and H-state assessments are logged as evidence with timestamps and rationale.
9. Post-event review is mandatory within defined timelines for all OADC triggers, duress events, break-glass exceptions, and H-3/H-4 events.
10. Exercise programs shall validate operator-resilience controls on the cadences defined in the exercise program. Controls not exercised within their cadence are assumed non-functional.

## Roles and responsibilities

- **Safety/Security Lead:** Policy owner; approve OADC definitions; post-event review authority
- **Incident Commander:** Declare contested environment; invoke team-level OADC constraints
- **Operator:** Execute duties within OADC constraints; self-report degradation; log decisions
- **Supervisor/Peer:** Assess H-state; conduct return-to-duty checks; participate in buddy-pair
- **Exercise Facilitator:** Design, conduct, and evaluate exercises; maintain exercise records

## Compliance mapping

| Requirement | Source |
|-------------|--------|
| Human oversight of high-risk AI | EU AI Act Art. 14 |
| Incident handling and response | NIS2 Art. 21(2)(b) |
| Crisis management | NIS2 Art. 21(2)(c) |
| Cybersecurity awareness and training | NIS2 Art. 21(2)(g) |
| Risk management and security policies | NIS2 Art. 21(2)(a) |
| Accountability and logging | MIL-STD-882E Task 401 |
| Meaningful human control | DoD Directive 3000.09 |

## Review log

| Date | Version | Approved by | Notes |
|------|---------|-------------|-------|
| YYYY-MM-DD | 1.0 DRAFT | — | Initial draft |
