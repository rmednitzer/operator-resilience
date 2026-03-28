# Post-Event Review Process

**Date:** 2026-03-28
**Scope:** Process specification for post-event review and learning loop closure. Defines trigger conditions, review deadlines, review objectives, record format, authority requirements, corrective action tracking, and pattern analysis. The execution checklist is at `checklists/post-event-review.md`; this document is the authoritative process specification.
**Status:** DRAFT
**Referenced by:** `policies/POL-OR-01-operator-governance.md` statement 9; `schemas/review-record.schema.json`; `docs/cross-cutting/return-to-duty.md`; `docs/exercise/exercise-program.md`

---

## 1 — Purpose

The post-event review is the primary learning-loop mechanism for operator-resilience governance. Every event that exercises the OADC or resilience controls must produce a review record that closes the learning loop. Without this record, the event yields no governance value: the program cannot determine whether controls fired correctly, whether thresholds were calibrated appropriately, or whether corrective action is needed.

The review serves a dual function:

1. **Operational learning:** reconstruct what happened, assess whether the governance controls performed as designed, and identify corrective actions.
2. **Operator welfare:** for events involving H-3/H-4 or duress, explicitly confirm that the affected operator's welfare has been addressed before returning them to full duty.

A review record is not complete until corrective actions have been verified closed and evidence has been retained in the evidence pipeline. Partial completion does not satisfy Policy Statement 9.

---

## 2 — Trigger conditions and review deadlines

The following events mandate a post-event review. Deadlines are calendar hours unless noted.

| Trigger condition | Review deadline | Notes |
|---|---|---|
| H-3 or H-4 operator event | 24 hours | Clock starts at time of H-state assessment |
| Duress event (real, not drill) | 48 hours | Clock starts at time of duress resolution |
| OADC threshold trigger | 72 hours | Clock starts at time the trigger condition was logged |
| Break-glass exception | 72 hours | Clock starts at time the exception was invoked |
| Exercise completion | 5 business days | Clock starts at exercise close |
| Pattern recurrence (same trigger type, same operator or environment, within 90 days) | Immediate flag | Flag to safety/security lead; escalation review initiated within 24 hours |

**Pattern recurrence definition:** The same trigger type (e.g., `h-state-h3`, `duress-event`, `break-glass`) occurring for the same operator or within the same operating environment within a 90-day rolling window. Pattern recurrence does not restart the 90-day window; it requires immediate escalation regardless of when the prior events were reviewed.

**Deadline extension:** A review lead may request a single extension of up to 24 hours for any deadline other than pattern recurrence. The extension must be logged with reason and approved by the safety/security lead before the original deadline passes. Extensions do not apply to H-3/H-4 events or pattern recurrence flags.

---

## 3 — Review objectives

Each post-event review shall address the following objectives. Not all objectives apply to every event type; inapplicable objectives shall be explicitly noted as N/A in the review record.

### 3.1 Event timeline reconstruction

Reconstruct the event timeline from decision logs, system logs, and evidence captured during the event. The timeline shall identify:
- The sequence of conditions that led to the OADC or resilience control being exercised
- The point at which each governance control activated (or should have activated)
- Actions taken by the operator, supervisor, and system enforcement layer
- Any gaps in the evidence record that limit reconstruction fidelity

### 3.2 OADC condition assessment

Assess whether the OADC fired correctly:
- Did the trigger condition activate at the right time? (Neither too early nor too late given the evidence available.)
- Was the authority response proportionate to the condition? (Neither over-restricting nor under-restricting operator authority.)
- Was the system enforcement layer consistent with the OADC definition?

If the OADC condition assessment reveals a calibration issue, document it as a potential parameter adjustment — see §6.

### 3.3 Threshold accuracy assessment

Assess whether the OADC parameter values (N, T, `min_review_threshold`, `consequence_threshold`, `passive_monitoring_interval`, `circadian_window`) were appropriate for the operating context. Any parameter adjustment recommendation must be documented and processed through the safety-critical change procedure (`docs/contracts/oadc.md` §3; `CONTRIBUTING.md`).

### 3.4 System enforcement assessment

Assess whether technical controls activated correctly:
- Did audit logging capture the trigger event with timestamp and rationale?
- Did two-person authentication gates function as specified?
- Did session timeouts or activity checks perform within tolerance?
- Were any enforcement gaps identified (controls that should have activated but did not)?

### 3.5 Handoff quality assessment

Applies when a handoff occurred during the event. Assess:
- Was context transfer complete? (System state, open risks, recent changes.)
- Did the receiving operator understand the current OADC conditions?
- Were there any information gaps that affected the event outcome?

### 3.6 Operator welfare assessment

**Mandatory for H-3/H-4 and duress events.**

- Has the affected operator's welfare been addressed (physical and psychological)?
- Has return-to-duty protocol been initiated per `docs/cross-cutting/return-to-duty.md`?
- Are there any welfare concerns that require follow-up outside the scope of this review?

Welfare findings are not included in the evidence pipeline shared beyond the review participants unless the operator consents or disclosure is required by applicable regulation or law.

### 3.7 Corrective action identification

Identify all corrective actions arising from the review. For each action: describe the issue, assign an owner, set a deadline, and define the verification method. See §6 for tracking requirements.

### 3.8 Pattern detection

Compare this event to previous review records:
- Does this event match the trigger type, context, or failure mode of any prior event?
- If this is the third or more event of the same type within 90 days: escalate per §2 (pattern recurrence) and §7.

---

## 4 — Review record format

Review records are stored as canonical YAML in `data/registers/review-register.yaml` (once established) per the schema at `schemas/review-record.schema.json`. Each record is identified by a sequential `REV-nnn` ID.

### 4.1 Schema field mapping

| Schema field | Content |
|---|---|
| `id` | `REV-nnn` — assigned sequentially |
| `object_type` | `review_record` |
| `event_type` | One of: `oadc-trigger`, `duress-event`, `social-engineering-attempt`, `break-glass`, `h-state-h3`, `h-state-h4`, `team-degradation` |
| `event_date` | Date of the triggering event (ISO 8601) |
| `review_date` | Date review was completed (ISO 8601) |
| `review_lead` | Name of review lead |
| `event_ref` | Cross-reference to the source event record (e.g., `HSE-001`, `DUR-001`, `EXR-001`) |
| `corrective_actions` | Array of corrective action objects: `action`, `owner`, `deadline` |
| `parameter_adjustments` | Boolean: `true` if any OADC parameter adjustment is recommended |
| `sign_off` | Array of sign-off objects: `role`, `name`, `date` |

### 4.2 Evidence retention

The review record is the summary artifact. Supporting evidence (decision logs, system logs, timeline reconstruction, observer notes) shall be retained in the evidence pipeline per the applicable data retention policy. The review record shall reference where supporting evidence is stored.

**Data protection:** Where review records contain personal data (including H-state assessments, which may constitute health-related data), retention and access controls must comply with the applicable data-protection framework as identified in the DPIA required by Policy Statement 11.

---

## 5 — Review authority and independence

### 5.1 Review lead

The review lead is responsible for conducting the review, completing the review record, and presenting findings to the safety/security lead for sign-off.

**For all events:** Review lead is the safety/security lead or a reviewer designated by the safety/security lead.

**For H-3/H-4 and duress events:** The review lead must be independent of the event under review. Specifically:
- The review lead shall not be the operator whose H-state or duress condition is being reviewed.
- The review lead shall not be the direct supervisor of that operator.
- Where both of the above conditions eliminate all available reviewers, the safety/security lead shall designate an external reviewer.

### 5.2 Sign-off

The safety/security lead must sign all review records. Where the safety/security lead is the operator under review, an independent reviewer designated by management shall sign instead.

Sign-off confirms:
- The review was conducted and objectives addressed
- Corrective actions are assigned with owners and deadlines
- The record is complete and ready for retention in the evidence pipeline

### 5.3 Participant access

Review participants have access to evidence relevant to their role in the review. The full review record (including welfare findings, if any) is accessible only to review participants and the safety/security lead unless disclosure is otherwise required.

---

## 6 — Corrective action tracking

### 6.1 Assignment requirements

Each corrective action identified in a review shall be recorded in the review record with:
- **Action description:** what must be done
- **Owner:** name of the individual responsible for completing the action
- **Deadline:** calendar date by which the action must be completed and verified
- **Verification method:** how closure will be confirmed (e.g., re-exercise, configuration change audit, updated documentation)

### 6.2 Safety-critical corrective actions

Corrective actions that require modifying OADC parameters, safe-state specifications, duress protocols, or H-state thresholds are safety-critical changes. They must be processed through the safety-critical change procedure defined in `CONTRIBUTING.md` §Safety-critical changes, including:
- Joint review by safety/security lead and independent reviewer
- Impact analysis (CACE assessment)
- Documented blast radius assessment
- Two-person review sign-off

### 6.3 Tracking until closure

Open corrective actions are tracked in the evidence pipeline until verified closed. The review record is updated to reflect closure of each action. A review record with open corrective actions past their deadline is an escalation trigger: the safety/security lead shall be notified and the overdue action reported in the next program review.

---

## 7 — Pattern analysis and escalation

### 7.1 Aggregate analysis

Post-event reviews are analyzed in aggregate at minimum annually as part of the program review. The annual analysis shall:
- Identify recurring trigger types and failure modes across the review record corpus
- Assess whether corrective actions have collectively reduced recurrence
- Identify structural gaps (OADC design, training, environmental factors) requiring program-level response

### 7.2 Recurrence escalation

Three or more events of the same type within any 90-day rolling window — for the same operator or the same operating environment — shall trigger an escalation review. The escalation review:
- Is conducted by the safety/security lead and at least one independent reviewer
- Must identify whether the recurrence is attributable to an individual factor, a systemic OADC design issue, a training gap, or an environmental factor
- Produces a program-level corrective action targeting the structural cause

### 7.3 Structural pattern response

If the escalation review (§7.2) or annual analysis identifies a structural pattern, the response must address root cause, not individual events. Structural responses may include:
- Revision of OADC parameters (safety-critical change required)
- Redesign of the exercise program to target the identified gap
- Environmental or organizational change recommendation escalated to management
- Revision of the governance document that failed to prevent recurrence

---

## 8 — Learning loop closure

A post-event review record is **complete** only when all of the following conditions are satisfied:

1. All review objectives (§3) have been addressed or explicitly marked N/A with rationale.
2. All corrective actions are assigned with owners and deadlines.
3. The safety/security lead has signed the review record.
4. All corrective actions have been verified closed (or, if not yet due, tracked in the evidence pipeline).
5. The review record and supporting evidence have been retained in the evidence pipeline.

An event for which the review record is not complete within the applicable deadline is a governance gap. It shall be flagged to the safety/security lead and included in the next program review. Incomplete review records do not constitute closure of the learning loop.

---

## Relationship to execution checklist

The checklist at `checklists/post-event-review.md` is the execution tool used during an active review. It is not the authoritative process specification. This document governs. Where the checklist and this document conflict, this document takes precedence and the discrepancy is itself a corrective action to be resolved.

---

## Confidence notes

- The review deadlines in §2 (24 h, 48 h, 72 h, 5 business days) are governance engineering estimates `[S,70]`; no single published standard prescribes review windows across this range of trigger types. Validate against operating-environment regulatory requirements and organizational capacity.
- The 90-day rolling window for pattern recurrence is a governance threshold `[I,70]` derived from incident-recurrence principles; adjust per operational experience and safety/security lead assessment.
- The requirement for review-lead independence from the affected operator (§5.1) is a well-established principle in safety investigation practice `[F,85]`.
- The single 24-hour deadline extension mechanism is an administrative design choice `[S,65]`; environments with complex multi-site operations may need a more structured extension framework.
- The three-event recurrence escalation threshold (§7.2) is an engineering estimate `[S,70]`; calibrate against operating-environment incident volume and organizational risk tolerance.
