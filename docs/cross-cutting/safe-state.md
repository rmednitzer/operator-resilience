# Safe State Specification

**Date:** 2026-03-28
**Scope:** Defines operator-absent safe state: triggers, specification framework, testing requirements, return procedure, and context-specific examples. Establishes the normative definition required by Policy Statement 6.
**Status:** DRAFT
**Referenced by:** POL-OR-01 statement 6; `docs/resilience/h-state-table.md` §H-3, §H-4; `docs/exercise/exercise-program.md` §10; README.md §Cognitive resilience, §Getting started

---

## 1 — Purpose

This document defines the safe state: the pre-committed system state that preserves safety when operator authority is unavailable, impaired below the OADC threshold, or actively contained due to a duress or integrity event.

The safe state is not an emergency stop in the simple sense. It is a governance instrument. It answers three pre-committed questions:

1. **What does the system do** when no qualified operator is available?
2. **What does the system stop doing** to prevent uncontrolled action?
3. **Who can authorize the system to leave** the safe state, and under what conditions?

Policy Statement 6 requires that safe states be defined, documented, and **tested** before operational use. A safe-state specification that has not been exercised per `docs/exercise/exercise-program.md` §10 is not considered validated.

---

## 2 — Definition

> **Safe state:** The pre-committed, explicitly specified system operating mode entered when the system cannot confirm the availability of an operator who meets the active OADC requirements for the operating environment. In safe state, the system performs only those actions explicitly authorized for operator-absent operation, halts all others, maintains monitoring, and awaits authorized exit.

The safe state is:

- **Pre-committed.** It is defined in advance, not improvised during an incident. Its definition requires safety/security lead sign-off.
- **Bounded.** It has a defined maximum duration before escalation is required.
- **Auditable.** All events during safe state are captured as evidence.
- **Authorized-exit only.** Exit from safe state requires explicit authorization by personnel meeting defined criteria — not simply the next available person.

---

## 3 — Safe-state triggers

The following conditions shall trigger transition to safe state. Triggers are not discretionary: when a trigger condition is confirmed, the transition to safe state is mandatory unless a qualified alternate operator is already confirmed available and assuming authority.

| Trigger | Condition | Source |
|---------|-----------|--------|
| H-3/H-4 with no alternate | Operator assessed at H-3 or H-4 and no alternate meeting OADC requirements is confirmed available | `docs/resilience/h-state-table.md` §H-3, §H-4 |
| OADC not met, no alternate | Mandatory handoff condition reached and no valid handoff recipient is available within the OADC escalation window | `docs/contracts/oadc.md` §2 |
| Duress containment | Duress protocol authority containment has been invoked and no second operator meeting OADC requirements has been confirmed clear of the duress condition | `docs/adversarial/` duress protocol |
| Operator absent — unplanned | Operator cannot be reached within the defined response window and no alternate has been briefed and confirmed | Per OADC instance parameter |
| System-declared safe state | Automated monitoring detects OADC trigger condition (passive monitoring interval exceeded, session timeout, missed watchdog) and escalation to a human operator fails within the defined window | Per OADC system enforcement layer |
| Explicit declaration | Safety/security lead or incident commander explicitly declares safe state for the environment | Authority: safety/security lead or IC |

**Trigger confirmation:** Before transitioning, the confirming party shall record the trigger type, timestamp, and basis for determination. In automated triggers, the system shall log the trigger condition and timestamp without human involvement.

---

## 4 — Safe-state specification framework

Each operating environment must have a safe-state specification defined before operational use. The specification follows the framework below. It is environment-specific: there is no universal safe state. Generic defaults are unsafe defaults.

The specification template is located at `templates/` (see §4.7 for authoring guidance). The safe-state specification for each environment is referenced in its OADC instance (`data/registers/oadc-register.yaml`).

### 4.1 Actions the system takes (active safe-state behaviors)

Define explicitly what the system **does** upon entering safe state. Include:

- Automated notifications (who is notified, via what channel, within what time)
- State preservation actions (capturing current state snapshot, flushing pending transactions in a defined manner)
- Escalation triggers (if safe state persists beyond the maximum duration, who is paged and by what mechanism)
- Monitoring continuity (see §4.3)

*Example entries: "Alert on-call secondary via PagerDuty within 60 seconds," "Flush pending write queue to persistent storage," "Log safe-state entry event with timestamp and trigger reason."*

### 4.2 Actions the system stops (halted behaviors)

Define explicitly what the system **ceases** upon entering safe state. These are the actions that require a qualified operator to authorize and that must not proceed autonomously. Be specific and exhaustive — omissions are gaps.

- Autonomous or semi-autonomous actions that modify system state beyond a defined scope
- Outbound communications or commands to external systems requiring operator-intent validation
- Scheduled maintenance or change windows that require human oversight

*Example entries: "No automated deployments to production," "No autonomous scaling actions above defined thresholds," "No OT setpoint changes."*

### 4.3 Monitoring that continues

Define what monitoring, logging, and telemetry **continues** in safe state. Monitoring continuity is a non-negotiable requirement: the safe state must not create an evidence gap.

- Health and performance telemetry
- Security event logging
- Duress or physical security monitoring (if applicable)
- External system interface monitoring (to detect conditions that would allow return from safe state)

### 4.4 Exit authorization

Define who can authorize exit from safe state and what conditions must be met.

| Exit authorization element | Requirement |
|---------------------------|-------------|
| Authorized roles | Named roles (not individuals) with authority to authorize exit. Minimum: safety/security lead or a qualified operator confirmed at H-0 or H-1 per a return-to-duty check. |
| Confirmation of OADC compliance | Authorizing party must confirm that the incoming operator meets all active OADC requirements for the environment. |
| Second-person confirmation | Where the duress trigger was active: a second person confirms the incoming operator is clear of the duress condition. |
| Exit log entry | Exit from safe state shall be logged with the authorizing party, timestamp, basis for authorization, and incoming operator identity. |

### 4.5 Maximum duration before escalation

Define the maximum time the system shall remain in safe state before a mandatory escalation event (notification to senior authority, invocation of business continuity procedures, or controlled shutdown).

- This value is environment-specific and depends on the consequence profile of continued operation without a qualified operator.
- The maximum duration for escalation must be defined in the safe-state specification — not left as "as long as necessary."

*Guidance: For high-consequence IT/SRE environments, a typical maximum before mandatory escalation is 30–60 minutes. For OT/ICS, this may be shorter depending on process criticality. For autonomous platforms with an operator-absent fallback mode, the maximum may be defined by mission parameters.*

### 4.6 Evidence capture during safe state

All events during safe state are evidence. The specification shall define:

- Logging destination and format (must be accessible post-event; WORM or hash-chained preferred)
- Events to be logged (trigger, transition, all monitoring alerts, exit attempt, authorized exit)
- Responsible party for retrieving and retaining evidence (default: safety/security lead)

### 4.7 Authoring the safe-state specification

When authoring a safe-state specification for a new operating environment:

1. Identify the OADC instance governing the environment (`data/registers/oadc-register.yaml`).
2. Complete each section of this framework (§4.1–§4.6) for that environment.
3. Document the specification as a sub-section of the OADC instance documentation or as a standalone referenced document.
4. Submit for review by the safety/security lead.
5. Schedule a `safe-state-test` exercise (ET-7) per `docs/exercise/exercise-program.md` §10 before operational use.
6. After the safe-state test passes, reference the exercise record (EXR-nnn) in the specification as validation evidence.

---

## 5 — Safe-state testing requirements

A safe-state specification that has not been tested is not validated. Policy Statement 6 requires that safe states be tested before operational use.

Testing is conducted via the `safe-state-test` exercise type (ET-7) defined in `docs/exercise/exercise-program.md` §10. Key requirements:

- **Trigger coverage:** The test must exercise each defined trigger condition, not a single representative trigger. Different trigger types may result in different transition paths.
- **Environment fidelity:** The test shall be conducted in a production-equivalent environment. Where production testing is not feasible, document the fidelity gap and its implications.
- **Exit authorization test:** The test shall include at least one unauthorized exit attempt and one authorized exit attempt.
- **Evidence capture test:** The test shall confirm that evidence capture functions correctly during safe state, not only during the transition.
- **Re-test triggers:** Any change to the safe-state specification requires a re-test before the changed specification is considered validated. Safe-state specification changes are safety-critical changes per the repository policy.

---

## 6 — Return from safe state

Return from safe state is not automatic. It requires explicit authorization. The following conditions and procedure apply.

### 6.1 Conditions for return

All of the following must be confirmed before exit from safe state is authorized:

1. A qualified operator has been identified who meets all active OADC requirements for the environment.
2. If the trigger was H-3/H-4: the incoming operator has completed the return-to-duty protocol per `templates/return-to-duty/TEMPLATE-return-to-duty.md`, or is a different operator who has not been through a degradation event.
3. If the trigger was duress containment: a second person (not the incoming operator) confirms the incoming operator is clear of the duress condition.
4. If the trigger was a system-declared safe state due to OADC parameter breach: the condition triggering the breach has been resolved (e.g., new operator assuming authority, rest completed).
5. The authorizing party has recorded the exit authorization (see §4.4).

### 6.2 Return procedure

1. Confirm all conditions in §6.1 are met.
2. Conduct a state briefing: the incoming operator reviews the state snapshot captured at safe-state entry and any changes during the safe-state period.
3. Verify that the operator's epistemic check can be completed with confidence ≥ 70% before any consequential action is taken.
4. Log exit from safe state: authorizing party, timestamp, incoming operator identity, basis for authorization.
5. The incoming operator assumes authority; the safe state is exited.

**First action post-exit:** The incoming operator's first consequential action after returning from safe state shall be logged with explicit reference to the safe-state event (EXR-nnn or event timestamp). This creates traceability between the safe-state event and subsequent decisions.

---

## 7 — Context-specific examples

The following examples illustrate safe-state specifications for three common operational contexts. These are illustrative, not exhaustive. Each deployment must define its own specification per the framework in §4.

### 7.1 IT/SRE on-call environment

**Trigger scenario:** On-call SRE assessed at H-3 (severely degraded, end of 16-hour incident) with no backup available within 30 minutes.

| Framework element | Example specification |
|-------------------|-----------------------|
| Actions taken | Alert secondary on-call (pager escalation); create timestamped incident snapshot; notify incident commander |
| Actions halted | No automated deployments; no manual production database writes; no firewall rule changes; no DNS changes |
| Monitoring continues | Full observability stack (metrics, logs, traces); alert routing remains active; synthetic monitoring continues |
| Exit authorization | Secondary on-call confirms H-0/H-1 and has reviewed incident snapshot; IC signs off |
| Maximum duration | 60 minutes before incident commander and VP Engineering are notified; 2 hours before business continuity invocation |
| Evidence capture | PagerDuty timeline; incident log entries; WORM audit log of all automated actions during safe state |

### 7.2 OT/ICS control room

**Trigger scenario:** Control room operator incapacitated (H-4); no qualified relief operator available; process is in steady-state but approaching a planned transition in 45 minutes.

| Framework element | Example specification |
|-------------------|-----------------------|
| Actions taken | Automatic hold at current setpoints; alert shift supervisor and plant manager; log process state snapshot; activate passive alarm monitoring |
| Actions halted | No setpoint changes; no batch starts; no valve commands beyond safety interlock responses; planned transition suspended |
| Monitoring continues | All process instrumentation; safety interlock system; environmental monitoring; physical security |
| Exit authorization | Shift supervisor confirms qualified relief operator (H-0) at console; relief operator completes state briefing from control room log |
| Maximum duration | 30 minutes before plant manager is directly engaged; 90 minutes before controlled process shutdown initiated per emergency operating procedure |
| Evidence capture | DCS historian continues recording; alarm log; shift log entries; physical access log for control room |

*Note: OT/ICS safe states interact with physical process safety and regulatory requirements (see §8). The governance specification does not replace the process safety case — it governs the operator authority layer within it.*

### 7.3 Autonomous platform — ground control station (GCS)

**Trigger scenario:** GCS operator degrades to H-2 in disconnected-link environment; OADC requires H-0/H-1 for authority over autonomous replanning; no alternate GCS operator available.

| Framework element | Example specification |
|-------------------|-----------------------|
| Actions taken | Platform transitions to pre-committed autonomous safe behavior (defined in authority-level specification); GCS logs authority suspension event; alert mission commander |
| Actions halted | No operator-initiated replanning commands accepted; no authority-level escalation commands accepted from GCS |
| Monitoring continues | Telemetry (when link permits); platform health monitoring; geofence monitoring; return-to-home condition monitoring |
| Exit authorization | Mission commander confirms alternate GCS operator at H-0; alternate completes link-state and platform-state briefing; mission commander authorizes authority reinstatement |
| Maximum duration | Per mission parameters; typically 15 minutes for persistent surveillance, defined differently for time-critical missions |
| Evidence capture | Flight data recorder (platform-side); GCS command log; link quality log during safe-state period |

*Note: The autonomous platform safe state links to the authority-level hierarchy defined in the companion repository `autonomous-platform-assurance`. The OADC governs the operator side; the platform authority hierarchy governs the platform side.*

---

## 8 — Regulatory and standards context

The following indicative references are relevant. Applicability depends on sector, jurisdiction, entity classification, and deployment context. See `docs/integration/regulatory-cross-reference.md` for article-level analysis.

| Reference | Indicative relevance to safe state |
|-----------|-------------------------------------|
| EU AI Act Art. 14(4)(e) | High-risk AI systems shall be designed so that the natural person responsible for oversight can "halt the system" — the safe state provides the operator-absent analog of this halt capability |
| EU AI Act Art. 14(4)(a) | Capability to fully understand the system's capacities and limitations — safe-state specification requires this understanding to be documented |
| Machinery Regulation 2023/1230 Annex III §1.2.4.3 | Emergency stop function requirements — safe state is the operator-governance complement to the physical emergency stop requirement |
| IEC 62443 (OT/ICS) | Security requirements for industrial automation and control; safe state interacts with the security requirements for operator interfaces and authority delegation |
| MIL-STD-882E | Safety-critical system design — operator-absent safe state is a direct application of the "safe state upon failure" design principle |
| DoD Directive 3000.09 | Autonomous weapons: appropriate human judgment required; operator-absent state directly in scope |
| ISO 10075 | Mental workload requirements — safe state is triggered by conditions that ISO 10075 identifies as impairing operator capacity |

**Interpretive note:** These references are indicative, not exhaustive, and their precise applicability to any given deployment requires legal and regulatory analysis. Do not treat this table as a compliance determination.

---

## 9 — Confidence notes

- The safe-state framework is derived from analogous practices in aviation (TOGA, go-around commitment), nuclear (licensed operator absence), and autonomous systems (RTH/RTS) [I,75]. Direct validation in IT/SRE and OT contexts is limited; treat as a governance baseline pending operational refinement.
- Maximum duration thresholds in §7 are illustrative and must be set per environment based on consequence analysis [S,65]. Do not use illustrative values operationally.
- The EU AI Act and Machinery Regulation references reflect the regulatory state as of the document date; verify current versions before compliance reliance [F,80 as of 2026-03-28].
