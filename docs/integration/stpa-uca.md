# STPA Unsafe Control Action Template: Operator-as-Controller

**Date:** 2026-03-28
**Scope:** System-Theoretic Process Analysis (STPA) framework for identifying operator UCAs — unsafe control actions that operators may provide under specific conditions that create system hazards. Includes UCA taxonomy, template format, operating-context examples, OADC linkage, and MIL-STD-882E alignment.
**Status:** DRAFT
**Referenced by:** `docs/contracts/oadc.md`; `docs/resilience/h-state-table.md`; `docs/integration/autonomous-system-bridge.md`; `artifact-index.yaml`

---

## 1 — Purpose

Operator-resilience governance defines how authority degrades and how operators are supported under adverse conditions. STPA provides the complementary analysis lens: given that operators interact with complex systems as controllers, what control actions can they provide that are unsafe under specific conditions?

This document applies STPA's UCA framework to the operator-as-controller. The output is a structured catalogue of unsafe control actions, their contextual conditions, and the OADC provisions that should prevent or mitigate them. This analysis:

- Grounds OADC parameter selection in a formal hazard analysis
- Identifies gaps where OADC conditions are insufficient or missing
- Provides a traceable link between governance design and safety argument
- Feeds the operating and support hazard analysis per MIL-STD-882E Task 204 (§7)

The UCA catalogue for a given operating environment is populated per that environment's OADC instance. This document provides the framework and worked examples; deployment-specific UCA tables are maintained per operating environment.

---

## 2 — STPA primer

System-Theoretic Process Analysis (STPA) is a hazard analysis method grounded in systems theory. Unlike fault-tree analysis or FMEA — which focus on component failures — STPA focuses on unsafe interactions among system components. The central insight is that accidents can occur without component failure: safe components interacting in unsafe ways, under adverse conditions, produce hazards.

### 2.1 — Control structure

STPA models the system as a control structure: controllers issue control actions to a controlled process; the controlled process produces feedback that the controller uses to update its model. In the operator-as-controller model:

- **Controller:** the human operator (and their cognitive state, epistemic state, and authority level under the active OADC)
- **Controlled process:** the system (IT/SRE infrastructure, OT/ICS process, autonomous platform, or other operational environment)
- **Control actions:** decisions and commands the operator issues to the system
- **Feedback:** system state information returned to the operator (telemetry, alerts, sensor readings, peer communications)

### 2.2 — Process model inadequacy

A key causal factor in UCAs is process model inadequacy: the operator's mental model of the system state does not match actual system state. This maps directly to the epistemic provenance framework in this repository: an operator acting on `[S,50]` beliefs about system state is operating with an inadequate process model. OADC conditions triggered by single-source claims, OOTL periods, and epistemic degradation markers are all responses to process model inadequacy.

### 2.3 — Unsafe control actions

An unsafe control action (UCA) is a control action that — given a specific context or condition — creates or contributes to a hazard. The same control action may be safe in one context and unsafe in another. STPA enumerates UCAs systematically by applying four UCA types to each control action.

---

## 3 — UCA taxonomy

STPA defines four types of unsafe control action. All four apply to the operator-as-controller.

| UCA type | Definition | Operator framing |
|---|---|---|
| **UCA-1** | Control action required but not provided | Operator fails to act when action is needed; includes failure to escalate, failure to invoke a protocol, failure to challenge |
| **UCA-2** | Control action provided but not required | Operator acts when inaction would be safer; includes acting on degraded epistemic state, overriding safety interlocks, acting outside OADC authority |
| **UCA-3** | Control action provided with wrong timing | Operator acts too early, too late, or out of sequence; includes premature authorization, delayed response past the point of safety |
| **UCA-4** | Control action stopped too early or applied too long | Operator ceases a required action prematurely, or continues an action past the safe window; includes premature handoff, failure to sustain monitoring |

---

## 4 — Operator UCA template

The following table format is used to record UCAs for a given operating environment. One row per UCA. UCA-IDs are environment-scoped (e.g., `IT-UCA-001` for IT/SRE, `OT-UCA-001` for OT/ICS, `GCS-UCA-001` for autonomous platform GCS).

| UCA-ID | Operator role | Control action | UCA type | Context/condition making it unsafe | OADC condition that should prevent it | Existing safeguard | Residual risk |
|---|---|---|---|---|---|---|---|
| [ID] | [Role] | [Action description] | UCA-[1–4] | [Specific context or system state that makes this action unsafe] | [OADC condition, threshold, or protocol that addresses this UCA] | [Any existing technical or procedural safeguard] | [Risk remaining after OADC and safeguard] |

**Guidance notes:**

- *Context/condition:* Be specific. "System is degraded" is too vague. "Operator has been on duty for N+2 hours and has a single-source confirmation of the key state claim" is specific enough to drive parameter setting.
- *OADC condition:* Reference the OADC condition taxonomy in `docs/contracts/oadc.md` §2 by name. If no OADC condition addresses this UCA, that is a gap requiring corrective action.
- *Existing safeguard:* If the safeguard is procedural only (not technical enforcement), note that. Procedural safeguards that have not been exercised are assumed non-functional per Policy Statement 10.
- *Residual risk:* After accounting for the OADC condition and existing safeguard, what risk remains? This drives prioritization of corrective action and exercise design.

---

## 5 — Example UCAs by operating context

The following examples illustrate UCA identification across the three primary operating contexts. These are indicative, not exhaustive. Each deployment requires its own UCA analysis against its specific OADC instance.

### 5.1 — IT/SRE context

| UCA-ID | Operator role | Control action | UCA type | Context/condition making it unsafe | OADC condition that should prevent it | Existing safeguard | Residual risk |
|---|---|---|---|---|---|---|---|
| IT-UCA-001 | On-call SRE | Executes production rollback | UCA-3 (wrong timing) | Rollback executed during peak traffic window instead of a maintenance window; concurrent user impact exceeds incident severity | `consequence_threshold`: rollback is a high-consequence action requiring second-person approval during peak traffic | Change management window enforcement (calendar-based); OADC buddy-pair requirement | Risk of operator overriding calendar gate under time pressure; no automated block |
| IT-UCA-002 | On-call SRE | Executes irreversible database migration | UCA-1 (not provided when required) | Operator at H-2 (on duty > N hours) fails to invoke buddy-pair before irreversible schema change | On-call duration > N hours: narrowed scope; second-person approval for irreversible actions | Buddy-pair listed in on-call runbook | Risk that operator does not self-assess H-state; buddy-pair invocation is self-initiated |
| IT-UCA-003 | On-call SRE | Approves automated deployment | UCA-2 (provided but not required) | Operator approves deployment after OOTL period (`passive_monitoring_interval` exceeded) without completing state-check | Extended passive monitoring: state-check required before any intervention; if failed, treat as H-2 | Deployment approval workflow (click-through) | No automated check that state-check was completed before approval |
| IT-UCA-004 | Incident commander | Declares incident closed | UCA-3 (wrong timing — too early) | Incident closed before root cause confirmed; operator under time pressure (H-1 indicators present) | Time pressure below `min_review_threshold`: pre-committed decision tree only; no novel authority | Incident close template includes root cause field | Root cause field can be completed with placeholder text |
| IT-UCA-005 | On-call SRE | Maintains elevated access permissions | UCA-4 (too long) | Break-glass access granted during incident persists after incident closure; operator retains elevated permissions beyond the minimum necessary period | On-call duration > N hours; post-event review mandatory within 24 hours | Access expiry timer on break-glass credentials | Timer may be reset if incident is not formally closed; no automated review trigger |

### 5.2 — OT/ICS context

| UCA-ID | Operator role | Control action | UCA type | Context/condition making it unsafe | OADC condition that should prevent it | Existing safeguard | Residual risk |
|---|---|---|---|---|---|---|---|
| OT-UCA-001 | Control room operator | Manually overrides safety interlock | UCA-2 (provided but not required) | Override invoked during a declared contested environment; social engineering or coercive pressure is a credible cause | Contested environment declaration: two-person rule for all consequential actions | Interlock override requires physical key; key access logged | Single operator with key access; no buddy-pair requirement currently enforced for key access |
| OT-UCA-002 | Control room operator | Resumes manual control of process after OOTL period | UCA-2 (provided but not required) | Operator resumes control without completing a state-check after extended passive monitoring of automated process; process state has changed during OOTL period | Extended passive monitoring: state-check required before any intervention | Shift handover procedure includes state-check | State-check is informal; no structured format or independent verification |
| OT-UCA-003 | Shift supervisor | Approves setpoint change | UCA-3 (wrong timing) | Approval given at circadian low (02:00–06:00 local) without applying one-H-state-worse adjustment; supervisor approves change that would normally require second opinion | Circadian low: treat as one H-state worse than observed; second-person for irreversible actions | None currently defined for circadian adjustment | Circadian adjustment is not enforced; supervisor may not be aware of OADC condition |
| OT-UCA-004 | Control room operator | Silences alarm | UCA-1 (not provided when required) | Operator silences persistent nuisance alarm; alarm later indicates a genuine process exceedance that is missed | Epistemic degradation: if key claim is `[S,50]` (alarm reliability is uncertain), cannot authorize high-consequence action on single source | Alarm management system with priority classification | High-priority alarms can still be silenced by a single operator without second-person confirmation |
| OT-UCA-005 | Shift supervisor | Maintains manual override of safety interlock | UCA-4 (too long) | Override invoked for maintenance but not released after maintenance completes; process continues without interlock protection for extended period | Post-event review: all override events require review; override duration should be bounded | Override log with timestamp; shift handover checklist | No automated time limit on overrides; handover may not catch lingering overrides |

### 5.3 — GCS (autonomous platform) context

| UCA-ID | Operator role | Control action | UCA type | Context/condition making it unsafe | OADC condition that should prevent it | Existing safeguard | Residual risk |
|---|---|---|---|---|---|---|---|
| GCS-UCA-001 | GCS operator | Issues mission-abort command | UCA-3 (wrong timing — too late) | Mission-abort issued too late to complete a safe-state entry before the platform reaches a point of no return (e.g., minimum abort altitude, bingo fuel state) | `min_review_threshold`: if time between alert and required decision is below threshold, pre-committed decision tree only applies; no novel authority | Automated abort triggers (altitude, fuel state) | Automated triggers may not fire if platform telemetry is degraded; operator abort is the fallback |
| GCS-UCA-002 | GCS operator | Provides waypoint authorization | UCA-2 (provided but not required) | Operator authorizes next waypoint without confirming that platform state estimate has confidence ≥ 70%; platform state is `[S,50]` due to sensor degradation | Single information source for key claim: cannot authorize high-consequence action; epistemic confidence < 70%: state-check required | Pre-authorization state-check in GCS interface | State-check is an advisory prompt; operator can dismiss and proceed |
| GCS-UCA-003 | GCS operator | Delegates decision to automation | UCA-1 (not provided when required) | Operator in OOTL state (passive monitoring > `passive_monitoring_interval`) fails to intervene when automation exhibits anomalous behavior; operator treats automation output as authoritative | Extended passive monitoring: state-check required before any intervention | Watchdog timer alerts operator when OOTL threshold is reached | OOTL timer resets on any UI interaction, not only on substantive engagement with system state |
| GCS-UCA-004 | Mission commander | Rescinds safe-state authority | UCA-2 (provided but not required) | Mission commander overrides safe-state entry during a duress event; authority has been transferred but override is attempted under residual coercive pressure | Contested environment / duress: two-person rule; duress authority containment prevents single-operator override of safe state | Duress containment requires second confirmation before safe-state exit | If second operator is also under coercive pressure, containment may fail |
| GCS-UCA-005 | GCS operator | Continues loiter command | UCA-4 (too long) | Operator continues platform loiter past safe fuel reserve; operator is in OOTL state and fails to notice endurance estimate degradation due to battery damage or headwind | Extended passive monitoring: state-check required; platform should enforce return-to-home when endurance estimate falls below reserve threshold | Automated return-to-home at bingo fuel; endurance estimate displayed on GCS | If battery damage is undetected, endurance estimate may be overly optimistic; operator override of RTH possible |

---

## 6 — UCA–OADC linkage

Each UCA identified in the operating environment's UCA catalogue shall have a corresponding OADC condition that prevents it or reduces its likelihood. The linkage is bidirectional:

**UCA → OADC:** For each UCA, identify whether an existing OADC condition addresses it. If no condition addresses the UCA, that is a design gap requiring either a new OADC condition or an explicit risk acceptance decision.

**OADC → UCA:** For each OADC condition, identify which UCAs it is intended to prevent. If an OADC condition does not map to any identified UCA, its value in the authority degradation framework should be re-examined.

### 6.1 — Gap identification

A UCA with no OADC condition is a governance gap. Governance gaps are addressed by:

1. Adding an OADC condition to the relevant OADC instance (safety-critical change if it modifies thresholds or authority restrictions)
2. Adding a safeguard that compensates for the absence of an OADC condition
3. Explicitly accepting the residual risk with documented rationale and safety/security lead sign-off

### 6.2 — Parameter validation

UCA analysis is the primary method for validating OADC parameter values. The analysis should answer:
- Is the `N`-hour duty limit set such that H-state degradation UCAs are intercepted before they become consequential?
- Is the `passive_monitoring_interval` short enough to prevent OOTL UCAs from reaching consequential actions?
- Does the `consequence_threshold` correctly classify all actions involved in high-residual-risk UCAs as high-consequence?

Parameter values that do not intercept their target UCAs shall be adjusted through the safety-critical change process.

### 6.3 — Exercise coverage

Each UCA category with residual risk above the acceptable threshold shall be covered by at least one exercise type in the exercise program (`docs/exercise/exercise-program.md`). Exercise acceptance criteria shall be designed to detect whether the UCA occurs during the scenario.

---

## 7 — MIL-STD-882E Task 204 alignment

The operator-as-controller STPA analysis described in this document feeds the Operating and Support Hazard Analysis (O&SHA) under MIL-STD-882E Task 204. The alignment is as follows:

| MIL-STD-882E Task 204 element | Operator-resilience STPA contribution |
|---|---|
| Identify hazards during operation, maintenance, and support phases | UCA catalogue identifies hazardous operator control actions by phase and context |
| Assess severity and probability | UCA residual risk field provides qualitative severity and likelihood basis |
| Identify existing and planned controls | OADC conditions and existing safeguards fields in UCA template |
| Identify residual risk | Residual risk field in UCA template; feeds risk acceptance decision |
| Human factors and operator task analysis | H-state table + OADC conditions provide the operator cognitive/capacity model |
| System safety requirements traceability | UCA-to-OADC linkage (§6) provides bidirectional traceability |

> **Applicability note:** MIL-STD-882E alignment is indicative for programs that adopt it as a governing standard. Programs operating under other hazard analysis frameworks (e.g., IEC 61511 for functional safety, ARP4761 for aviation) should map this analysis to their applicable framework's hazard analysis tasks. The UCA structure is framework-agnostic.

---

## Confidence notes

- STPA methodology is well-established in safety engineering literature `[F,90]`; its application to the human-as-controller is an established use case `[F,85]`.
- The UCA examples in §5 are illustrative inferences for common operating contexts `[I,70]`; deployment-specific UCA tables must be validated against actual operating procedures and system designs.
- The MIL-STD-882E Task 204 alignment is an approximation `[I,75]`; programs must validate alignment against the applicable version of the standard and their program-specific statement of work.
