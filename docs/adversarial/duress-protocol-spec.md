# Duress Protocol Specification

**Date:** 2026-03-28
**Status:** DRAFT
**Classification:** RESTRICTED — distribution limited to authorized personnel only
**Scope:** Operational specification for duress protocol architecture in environments where operator coercion is a credible threat. This document governs the design, implementation, monitoring, response, and recovery functions for all operating environments covered by this repository.

> **Safety-critical document.** Any change to this specification requires the two-person review process defined in `CONTRIBUTING.md`. See also: CACE principle — changing anything changes everything.

---

## 1 — Purpose

This specification defines the duress protocol architecture applicable to operating environments where an operator may be coerced, threatened, or otherwise compelled to act against authorized intent. It translates Policy Statement 5 (POL-OR-01) into operational requirements and provides the normative basis for duress protocol instances created from `templates/duress-protocol/TEMPLATE-duress-protocol.md`.

A duress protocol is a pre-committed, trained, and tested set of mechanisms that allow an operator under coercion to:

1. Signal their state covertly without alerting the coercing party.
2. Trigger authority containment without interrupting apparent workflow.
3. Transfer control to a supporting function that can respond appropriately.
4. Create an auditable evidence record of the event.

Duress protocols are **not improvised during incidents**. All signal mechanisms, monitoring assignments, response procedures, and containment actions must be defined, trained, and exercised before operational use. An untested duress protocol is considered non-functional per Policy Statement 10.

Duress events are logged using the schema at `schemas/duress-event.schema.json` with records stored in `data/registers/duress-event-register.yaml`.

---

## 2 — Threat model for operator duress

The following threat categories are in scope for duress protocol design. Each category requires that the signal and response architecture be robust against an adversary who may be present, observing, or monitoring the operator at time of signal transmission.

| Threat category | Description | Adversary visibility |
|---|---|---|
| Physical coercion | Operator is physically restrained, threatened with violence, or subject to direct physical control | Adversary typically co-located or on camera |
| Psychological pressure | Sustained intimidation, threats, or manipulation to compel action without physical contact | Adversary may be remote; may monitor communications |
| Threat to family or associates | Operator is coerced by credible threat to a third party rather than to self | Adversary may not be physically present |
| Blackmail or compromise | Operator is coerced via threatened disclosure of sensitive personal information | Adversary operating covertly; may monitor digital channels |
| Insider coercion | A colleague, supervisor, or insider with legitimate access pressures the operator to act beyond authorized scope | Adversary has plausible access to communications and context |
| Identity fraud | A third party impersonates a supervisor, authority, or system to compel action | Operator may be deceived rather than coerced — same signal architecture applies |

**Out of scope:** Operator self-degradation (H-state events — see `docs/resilience/h-state-table.md`) and technical system compromise without human coercion (see threat model in `docs/adversarial/`). Where it is ambiguous whether a situation constitutes duress or H-state degradation, treat as duress until resolved.

**Confidence notes:** Physical coercion and insider threat patterns are documented in critical-infrastructure security literature [F,80]. Threat-to-family and blackmail patterns are established in insider-threat behavioral frameworks [F,75]. The specific signal architecture is an operationalisation [I,70] — validate by exercise before operational reliance.

---

## 3 — Signal architecture

### 3.1 General requirements

All signal types must meet the following requirements before operational use:

1. **Pre-established:** The signal mechanism, meaning, and receiving function are defined before any operational scenario.
2. **Trained:** All operators and receiving personnel have trained on the specific signal. Training must be documented.
3. **Tested:** The full signal-to-response chain has been exercised under realistic conditions (exercise type ET-1 per `docs/exercise/exercise-program.md`). A signal that has not been exercised is considered untested and must not be relied upon operationally.
4. **Non-guessable:** The specific signal must not be deducible by an adversary with general knowledge of the operating environment or communication patterns.
5. **Observable-normal:** The signal must appear, to an uninvolved observer, as routine activity within the operator's normal work pattern.

Signal mechanisms are documented per-environment in the duress protocol instance (`templates/duress-protocol/TEMPLATE-duress-protocol.md`). The specific signals are not recorded in this specification — details are distributed only to authorized personnel within each protocol instance.

### 3.2 Verbal duress signal

The verbal duress signal is a word or phrase embedded in otherwise-routine communication (voice, written, or chat). Requirements:

- Designed to appear as a natural element of the operational communication context.
- Must not contain terminology that would alert an adversary monitoring the communication.
- Safe word / challenge word pair: the receiving function may challenge, and the operator responds with the safe word, confirming the signal was intentional rather than accidental.
- Distinct from safe-passage or all-clear signals; these serve opposite purposes and must not be confusable.
- Must be rotated on a schedule defined in the protocol instance — at minimum annually, and immediately following any duress event or suspected compromise.

Verbal signals apply in voice, written, and asynchronous-text communication contexts.

### 3.3 Digital duress signal

The digital duress signal is an action within a monitored system that appears to an observer as routine but triggers a covert alert. Requirements:

- Implemented as a canary credential, a designated low-profile action, or a specific system input sequence.
- The alert triggered must be delivered to the receiving function via a channel the coercing party cannot observe or interrupt.
- The system response to the signal must be indistinguishable from a normal workflow step to anyone observing the operator's screen or terminal.
- Digital signals are the preferred primary mechanism in remote, distributed, or predominantly digital operating environments.

### 3.4 Physical duress signal

The physical duress signal is a hand position, posture, or object placement used in co-located scenarios. Requirements:

- Applicable **only** where at least one receiving-function member is physically co-located or has direct visual access to the operator.
- Must be a natural movement or position that does not appear distressed, unusual, or signaling to an uninvolved observer.
- Must be documented in the protocol instance with a diagram or unambiguous written description.
- **Not applicable** in fully remote operating contexts.

### 3.5 Signal integrity and key management

- Specific signal mechanisms are classified within the scope of each deployed protocol instance.
- Signal details are distributed only to personnel in the receiving function and the designated backup.
- A compromised signal (suspected or confirmed) must be replaced immediately; the replacement must be trained and exercised before the control is considered restored.
- Signal mechanisms must be rotated at minimum annually and after any duress event.

---

## 4 — Monitoring and receiving function

### 4.1 Receiving function assignment

Each operating environment's duress protocol instance must designate:

| Role | Requirement |
|---|---|
| Primary monitor | Named role or team responsible for signal monitoring during operational hours |
| Backup monitor | Named alternate; active when primary is unavailable |
| Escalation contact | Security team or designated authority to contact when signal is received |
| Out-of-hours coverage | Procedure for signals received outside primary monitoring hours |

The receiving function must have trained on the specific signals for the environments they monitor. Training records must be maintained.

### 4.2 Monitoring hours

Duress monitoring must match the operational coverage of the environment:

- **24/7 environments** (e.g., production SRE on-call, OT control rooms): continuous monitoring, 24 hours per day, 7 days per week.
- **Specified-hours environments:** monitoring during defined operational hours with an on-call escalation path for signals received outside those hours.
- **No coverage gap permitted:** if the primary monitor becomes unavailable, the backup monitor assumes coverage before the primary stands down.

### 4.3 Escalation on no-acknowledgment

If a duress signal is received and acknowledgment cannot be sent within the protocol-defined window, or if operator contact is lost after a signal has been registered, the receiving function escalates to the security team immediately without waiting for the timeout window to expire.

---

## 5 — Immediate response on signal receipt

When a duress signal is received and validated, the receiving function executes the following steps in order. All steps must be completed within the time limits defined in the protocol instance. Steps 5.1 through 5.4 must be achievable without any visible change in the operator's environment.

### 5.1 Covert acknowledgment

The receiving function sends a covert acknowledgment to the operator using a pre-established mechanism that confirms receipt without alerting the coercing party.

- The acknowledgment must be delivered via a channel the coercing party cannot monitor.
- The acknowledgment must not alter the operator's visible workflow or screen state in a way that an observer would notice.
- If acknowledgment cannot be delivered covertly, it is withheld — operator safety takes priority over confirmation of receipt.
- Acknowledgment must be sent within the window defined in the protocol instance (typically ≤ 120 seconds).

### 5.2 Security team alert

Immediately on acknowledgment (or in parallel if time-critical), the receiving function alerts the security team via the escalation path defined in the protocol instance. The alert includes:

- Operator identity (or role identifier)
- Environment identifier
- Signal type received
- Timestamp
- Operator's last known location or connection context
- Any contextual information that could assist response

This alert is confidential and must not be communicated via any channel the coercing party may monitor.

### 5.3 Evidence capture initiation

Immediately on signal receipt, automated evidence capture is initiated:

- Session recording (screen capture or equivalent) initiated for the operator's active session, if not already running.
- Logging level elevated to capture all actions at full fidelity.
- Chain-of-custody record created with timestamp of signal receipt and identity of the receiving-function member who received it.
- Evidence capture runs continuously until the duress event is formally resolved (§7).

Evidence logs during a duress event must be write-protected and cannot be modified or deleted by the operator under duress. This is a technical control requirement; see §6 below.

### 5.4 Authority transfer preparation

In parallel with steps 5.2 and 5.3, the receiving function prepares for authority transfer:

- Identifies the designated alternate operator for the environment.
- Pre-positions the alternate for immediate authority assumption.
- Reviews the environment's pre-committed decision tree (where applicable) to identify in-progress actions that must be completed, halted, or handed off.
- Does not initiate the formal transfer until containment measures in §5.5 are in place.

### 5.5 OADC contested environment condition invocation

On duress signal receipt, the OADC contested-environment condition is invoked immediately:

> "Contested operating environment — Declared by incident commander or security → Two-person rule for all consequential actions" (`docs/contracts/oadc.md` §2)

This invocation does not require a formal declaration from the incident commander when triggered by a duress signal. The receiving function invokes the condition on behalf of the security team. All authority consequences of the contested-environment condition apply from this point forward.

---

## 6 — Authority containment

Authority containment reduces the operator's decision authority to the minimum necessary to maintain apparent normal operations while preventing consequential harm. Containment is applied immediately upon OADC contested-environment invocation and remains in effect until formal resolution (§7).

### 6.1 Two-person rule for all consequential actions

All actions that meet the `consequence_threshold` defined in the OADC instance require second-person approval from the designated alternate or security authority. The second-person approver must not be accessible to or influenced by the coercing party.

Where second-person approval cannot be obtained covertly, the operator delays the consequential action until approval is available, applying the safe reversible partial action principle (see `docs/epistemics/belief-provenance.md`).

### 6.2 Session scope restriction

The operator's system session is scoped to the minimum permissions required for the current task. Where technically feasible:

- Elevated or privileged sessions are suspended.
- Actions outside the current task scope are blocked at the system level.
- New connections or session escalations require out-of-band approval from the security team.

### 6.3 Pre-committed decision tree only — no novel authority

Under authority containment, the operator follows the pre-committed decision tree for the current operating scenario. No novel authority is exercised:

- No new resource allocations beyond pre-approved bounds.
- No irreversible actions without second-person approval.
- No communications with external parties outside the established operational pattern without covert security-team approval.

Any request for novel authority while containment is active is treated as a possible escalation indicator and reported to the security team immediately.

### 6.4 Time-boxing and forced handoff

Authority containment has a maximum duration before forced handoff is mandatory. The time limit is defined in the protocol instance. Default maximum: 60 minutes from duress signal receipt to forced authority transfer.

If the duress condition has not been resolved within the time-box limit:

1. Authority transfer to the alternate operator is executed.
2. The operator's session is closed or placed in read-only mode.
3. The operator is stood down from operational duties for the duration of the event.
4. A welfare check is initiated (§7.1).

The time-box limit may be extended by the security authority for operational continuity reasons with documented justification. No extension beyond 120 minutes without formal security team sign-off.

---

## 7 — Evidence integrity during duress

Evidence captured during a duress event must maintain a verifiable chain of custody from signal receipt through post-event review.

| Requirement | Implementation |
|---|---|
| Log immutability | Evidence logs are written to a write-protected or append-only store inaccessible to the operator under duress |
| Chain of custody | Each evidence record includes: timestamp, receiving-function member identity, action that generated the record, hash of previous record (append-only chain) |
| Scope | All operator actions from signal receipt through event resolution, plus the 30 minutes preceding signal receipt where technically retrievable |
| Integrity verification | Hash verification run at event resolution; any gap or inconsistency escalated to the security team before post-event review |
| Access restriction | Evidence records accessible only to: security team, designated post-event reviewer, and authorized legal/HR function |

Evidence records may contain sensitive personal data. Access controls and retention policies must comply with the DPIA completed per §10.

---

## 8 — Recovery procedure

Recovery is initiated only after the coercing condition has been eliminated or neutralized. The security team confirms clearance before any recovery step is executed.

### 8.1 Formal welfare check

Before any return to operational duties, a formal welfare check must be conducted by a designated welfare officer or supervisor:

- Confirms the operator is safe and free from coercion.
- Identifies any immediate support needs (medical, psychological, practical).
- Documents outcome as input to the post-event review record.

The welfare check is confidential and not shared with operational management without operator consent, except where required by legal obligation.

### 8.2 Return-to-duty protocol

Before the operator resumes authority in any operating environment, the return-to-duty protocol (`templates/return-to-duty/TEMPLATE-return-to-duty.md`) must be completed. A duress event is a mandatory trigger for return-to-duty assessment regardless of H-state at the time of the event.

The return-to-duty assessment must determine:

- Whether the operator's H-state is H-0 or H-1 (full or near-full capacity).
- Whether any actions taken under duress require remediation.
- Whether the operator requires additional support before resuming full authority.

Return to authority is not automatic. It requires explicit sign-off from the return-to-duty assessor and the safety/security lead.

### 8.3 Evidence review

The security team reviews all evidence captured during the duress event:

- Verifies chain-of-custody integrity (§7).
- Identifies any consequential actions taken under duress that may require remediation or notification.
- Packages evidence for post-event review (§8.4).

### 8.4 Post-event review

A post-event review (REV) is mandatory following every duress event — real or exercise. The record is stored in `data/registers/review-register.yaml` per `schemas/review-record.schema.json`.

The REV must address:

- Timeline reconstruction: signal to containment to resolution.
- Protocol effectiveness: did each step work as designed? What failed or was slower than required?
- Evidence completeness: was the evidence chain intact?
- Operator welfare: what was the operator's experience? What would have changed the outcome?
- Corrective actions: any protocol, training, or technical defects identified.

The duress event record (`DUR-nnn`) in the register must reference the completed REV record (`REV-nnn`) in its `review_ref` field.

---

## 9 — Exercise requirements

Duress protocols must be exercised on the cadence defined in `docs/exercise/exercise-program.md`. Summary:

| Exercise type | Cadence | Acceptance criteria (summary) |
|---|---|---|
| ET-1: `duress-drill` | Annually (minimum) | Signal transmitted ≤ 60 s; containment initiated ≤ 120 s; no visible behavioral indicator to simulated coercer; escalation contacts notified per protocol; operator can debrief all critical steps |

Full acceptance criteria for ET-1 are defined in `docs/exercise/exercise-program.md` §4.

**A duress control that has not been exercised within its cadence is assumed non-functional** per Policy Statement 10 (POL-OR-01). Where the last recorded ET-1 exercise is more than 12 months old, the duress control for that environment must be marked non-functional until re-exercised.

Duress drills must be conducted without prior notification of the specific time or scenario to at least one participant playing the role of the coerced operator. Pre-announced drills are insufficient as the sole exercise record.

---

## 10 — GDPR considerations

Duress events and authority-containment logs contain personal data and may contain sensitive personal data within the meaning of GDPR (Regulation 2016/679). The following considerations apply to all EU-context deployments.

### 10.1 Data categories in scope

| Data element | GDPR classification |
|---|---|
| Operator identity linked to duress event record | Personal data — Art. 4(1) |
| H-state at time of event | Health-adjacent data — conditionally special-category data under Art. 4(15) + Art. 9(1) |
| Evidence logs of operator actions during duress | Personal data — Art. 4(1); may include behavioral health indicators |
| Welfare check record | Sensitive — may contain medical or psychological information |
| Return-to-duty assessment | Personal data; may contain health-adjacent H-state data |

### 10.2 Lawful basis

| Data element | Recommended lawful basis |
|---|---|
| Operational duress logs (non-health) | Art. 6(1)(f) legitimate interest (security and safety of systems and personnel) — subject to balancing test; or Art. 6(1)(c) legal obligation where applicable regulatory or employment law applies |
| Health-adjacent H-state data | Art. 9(2)(b) employment law or collective agreement; or Art. 9(2)(g) substantial public interest — sector-dependent |

The deploying organization's Data Protection Officer (DPO) must confirm the applicable lawful basis before operational deployment.

### 10.3 DPIA requirement

Processing of duress event records and operator H-state data during a duress event constitutes systematic evaluation of natural persons (GDPR Art. 35(3)(a)) and may involve health-adjacent special-category data (Art. 35(3)(b)). **A DPIA under Art. 35 is required before operational deployment in any EU context.** This is a blocking pre-deployment requirement.

See `docs/integration/regulatory-cross-reference.md` §9.5 for detailed DPIA requirements.

### 10.4 Retention

Duress event records must be retained for the period required by applicable law and the deploying organization's data retention policy. Minimum retention: the period required for post-event review completion and any associated legal or regulatory proceedings. Maximum retention: defined in the DPIA.

Welfare check records are subject to stricter retention limits. The DPO must define retention separately for this data category.

### 10.5 Access restriction

Access to duress event records, evidence logs, and welfare check records must be restricted to the minimum necessary personnel (security team, post-event reviewer, authorized legal/HR function). Access logs must be maintained.

---

## 11 — Relationship to other repository controls

| Document | Relationship |
|---|---|
| `docs/contracts/oadc.md` | Duress signal invokes OADC contested-environment condition (§2); authority containment implements OADC two-person rule |
| `docs/resilience/h-state-table.md` | Duress event may co-occur with H-state degradation; H-state assessment is part of return-to-duty |
| `docs/cross-cutting/safe-state.md` | If duress results in operator unavailability and no alternate is ready, system enters operator-absent safe state |
| `docs/exercise/exercise-program.md` | ET-1 (`duress-drill`) exercises this protocol annually; acceptance criteria in §4 |
| `templates/duress-protocol/TEMPLATE-duress-protocol.md` | Per-environment protocol instances created from this template; this spec is the normative framework |
| `schemas/duress-event.schema.json` | Schema for `DUR-nnn` records in `data/registers/duress-event-register.yaml` |
| `templates/return-to-duty/TEMPLATE-return-to-duty.md` | Return-to-duty protocol triggered by every duress event |
| `policies/POL-OR-01-operator-governance.md` | Policy Statement 5 is the policy basis for this specification |
| `docs/integration/regulatory-cross-reference.md` | GDPR DPIA (§9.5); CER Art. 13(1)(e); NIS2 Art. 21(2)(i) provide regulatory grounding |

---

## 12 — Classification and distribution

**Classification:** RESTRICTED

This document describes duress signal architecture, authority containment mechanisms, and evidence capture procedures that, if disclosed to unauthorized parties, could enable an adversary to defeat the controls it describes. Distribution is limited to:

- Safety/security lead and designated deputy
- Operators in operating environments with an active duress protocol
- Exercise facilitators conducting ET-1 drills
- Post-event reviewers assigned to duress event reviews
- Legal and HR functions requiring access for specific post-event proceedings

This document must not be stored on systems accessible to general staff or referenced in publicly accessible documentation except by title and path. Specific signal mechanisms are **not** recorded in this specification — they are recorded only in per-environment protocol instances and distributed only to the receiving function and designated backup.
