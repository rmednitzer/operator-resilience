# Return-to-Duty Protocol

**Date:** 2026-03-28
**Scope:** Process specification for return of an operator to full OADC authority after removal from duty due to H-state degradation, duress event, break-glass exception, or voluntary self-report. Defines conditions, protocol steps, documentation requirements, and re-entry restrictions.
**Status:** DRAFT
**Referenced by:** `policies/POL-OR-01-operator-governance.md` statement 7; `docs/cross-cutting/post-event-review.md` §3.6; `docs/resilience/h-state-table.md`; `templates/return-to-duty/TEMPLATE-return-to-duty.md`

---

## 1 — Purpose

An operator who has been removed from duty — whether due to an assessed H-3 or H-4 condition, a duress event authority transfer, a break-glass exception, or a voluntary or supervisor-assessed H-state self-report — does not automatically return to full OADC authority when the immediate condition resolves. Return to duty requires a structured protocol that confirms the operator is genuinely ready to resume full authority, not merely that the triggering event has passed.

This document defines that protocol. The template for conducting return-to-duty assessments is at `templates/return-to-duty/TEMPLATE-return-to-duty.md`. This document governs the process; the template is the execution tool.

**Relationship to safe state:** An operator under return-to-duty protocol is not available as a valid OADC authority for the operating environment. If no other qualified operator is available, the system remains in or transitions to safe state per `docs/cross-cutting/safe-state.md` until return-to-duty is confirmed.

---

## 2 — Return-to-duty triggers

Return-to-duty protocol is initiated by any event that removed the operator from full OADC authority:

| Trigger | Authority impact |
|---|---|
| H-3 assessment (operator or supervisor) | Mandatory handoff; operator removed from independent authority |
| H-4 assessment | Operator incapacitated; removed from all authority |
| Duress event — authority transfer invoked | Operator authority contained during duress condition |
| Break-glass exception invoked | Operator authority reviewed; return requires review sign-off |
| Voluntary self-report of H-state degradation | Operator has reported incapacity; authority transfer per OADC |
| Supervisor-assessed H-state degradation | Supervisor has assessed the operator below OADC threshold |

**Note on break-glass exceptions:** A break-glass exception does not always remove the operator from duty, but when it signals a potential condition affecting operator integrity or capacity, return-to-duty protocol applies. The post-event review (§5) determines whether a break-glass exception requires return-to-duty. When in doubt, apply the protocol.

---

## 3 — Return-to-duty protocol steps

### Step 1: Minimum rest/recovery period

Before a structured readiness check may be conducted, the operator must complete the minimum rest or recovery period appropriate to the trigger event. Rest periods are mandatory minimums; the assessor may extend them based on the structured check findings.

| Trigger condition | Minimum rest/recovery requirement |
|---|---|
| H-1 → return to H-0 | No mandatory rest period; informal peer check sufficient (see Step 2a) |
| H-2 → return to H-0 | No mandatory rest period; structured check required (see Step 2b) |
| H-3 → return to active duty | 8-hour minimum rest before structured check may begin |
| H-4 → return to active duty | Medical clearance or occupational health assessment required; structured check follows clearance |
| Duress event | 30-minute minimum delay after duress formally resolved (see Step 2d) |
| Break-glass exception | No mandatory rest; structured check required; return requires post-event review sign-off |

The 8-hour minimum for H-3 is a baseline derived from fatigue recovery literature `[S,70]`. Operating environments subject to stricter regulatory duty-rest requirements (e.g., aviation Part-ORO.FTL) must use the stricter applicable limit. Each OADC instance should record the governing framework if a regulation constrains rest periods.

The H-4 → medical clearance requirement applies when the H-4 condition was due to acute incapacitation (medical, psychological, or physical). For H-4 triggered solely by a short-duration acute event (e.g., confirmed temporary sensory impairment that has resolved), the supervisor may determine that a structured check without occupational health referral is sufficient, provided this determination is documented in the return-to-duty record with explicit rationale.

### Step 2: Structured readiness check

A structured readiness check is conducted by a supervisor or designated peer using `templates/return-to-duty/TEMPLATE-return-to-duty.md`. The check addresses four domains:

**a. Informal peer check (H-1 → H-0 only)**

Where the trigger was mild H-1 degradation (fatigue advisory, minor performance degradation, no authority restriction invoked), an informal check by a peer or supervisor is sufficient. The peer shall confirm:
- Operator presents as alert and engaged
- Operator can describe current system state without prompting
- No welfare concerns requiring follow-up

Informal peer check findings are logged as a brief note referencing the triggering event. No full return-to-duty record is required.

**b. Structured readiness check domains (H-2 and above, break-glass, duress)**

| Domain | Assessment |
|---|---|
| **Operator welfare** | Is the operator physically and psychologically ready to resume duty? Any ongoing welfare concerns? |
| **Cognitive state** | Can the operator articulate the current state of systems under their authority? (Verbal state-check: operator states current system state unprompted; assessor verifies accuracy against independent source.) |
| **OADC awareness** | Is the operator aware of all active OADC conditions for the operating environment? Can they state the current constraints? |
| **Situational awareness** | Has the operator been briefed on all changes since removal from duty? Is the operator's situational awareness current and accurate? |

A structured readiness check requires the operator to pass all four domains. Conditional pass (operator passes with caveats, e.g., buddy-pair required for first shift) is permitted where the assessor documents the condition and its duration explicitly. Failure in any domain: return-to-duty is not authorized; re-check after further recovery.

**c. H-state upgrade declaration**

Following a successful structured readiness check, the assessor makes an explicit declaration:

> *"I assess [Operator name] as upgraded to H-[n] as of [timestamp]. This assessment is based on the structured readiness check conducted under [triggering event reference]."*

The declaration is logged in the return-to-duty record with:
- Assessor identity and role
- Timestamp (UTC)
- Target H-state (H-0 for full authority; H-1 if conditions persist that warrant advisory status)
- Any conditions on return (e.g., buddy-pair for the first shift, restricted action scope)

The H-state upgrade declaration is the formal mechanism by which authority is restored. Without this declaration, the operator does not hold OADC authority, regardless of the passage of time.

**d. Duress event: additional requirements**

For duress events, the following apply in addition to the structured readiness check:

- **Independent welfare check:** A welfare check by an independent party — not the security team managing the duress containment — must be completed before the structured readiness check begins. The purpose is to confirm the operator is no longer under coercive pressure and that any psychological effects of the duress are assessed.
- **Minimum delay:** A minimum of 30 minutes after the duress condition is formally resolved must elapse before the operator re-assumes authority. This delay allows decompression and ensures the operator is not returning to duty under residual coercive influence.
- **Authority re-assumption confirmation:** The return-to-duty record must explicitly confirm that the duress containment has been lifted by the security team before authority is restored.

### Step 3: Post-event review initiation

Return-to-duty initiates the corresponding post-event review if it has not already been initiated. The return-to-duty record shall cross-reference the post-event review record (or note that the post-event review is pending) per `docs/cross-cutting/post-event-review.md`.

---

## 4 — Documentation

### 4.1 Return-to-duty record

A return-to-duty record is created for every trigger event at H-2 or above, every duress event, and every break-glass exception. Informal peer checks (H-1) require only a brief log note.

The record is completed using `templates/return-to-duty/TEMPLATE-return-to-duty.md` and stored in the evidence pipeline. It must include:
- Operator identity and role
- Triggering event reference (e.g., `HSE-001`, `DUR-001`)
- Stand-down period: start time, duration, minimum required
- Structured readiness check findings for each domain
- H-state upgrade declaration: assessor identity, timestamp, target H-state, conditions
- Post-event review cross-reference

### 4.2 Evidence pipeline retention

Return-to-duty records are retained in the evidence pipeline per the applicable data retention policy. H-state assessments contained within these records may constitute health-related personal data; access must comply with the applicable data-protection framework and the DPIA required by Policy Statement 11.

### 4.3 Cross-referencing

Return-to-duty records shall cross-reference:
- The triggering event record (H-state event, duress event, or break-glass log entry)
- The post-event review record (or pending reference)
- The active OADC instance specifying the applicable parameters

---

## 5 — Re-entry restrictions

An operator who has been removed from duty for the same condition (same trigger type, same H-state assessment basis, or recurring duress) **three times within any 90-day rolling window** shall not return to duty under standard return-to-duty protocol. Instead:

- The pattern is flagged as a recurrence event per `docs/cross-cutting/post-event-review.md` §2
- An assessment by the safety/security lead is required before authority is restored
- The assessment shall consider whether the operator's operating environment, role scope, or support structure requires modification
- Return to duty is conditional on the safety/security lead's assessment and may include: permanent buddy-pair requirement, modified duty scope, adjusted OADC parameters for the environment, or referral to occupational health

Re-entry restrictions do not prevent the operator from performing duties that fall outside their OADC authority scope. They restrict re-assumption of the authority that was the subject of the removal.

---

## Confidence notes

- The 8-hour H-3 rest minimum is derived from occupational fatigue literature `[S,70]`; validate against operating-environment regulatory requirements and occupational health assessment.
- The 30-minute post-duress delay is an engineering estimate `[S,65]`; no published standard governs minimum decompression time after coercive events in this operational context. Environments with access to occupational psychology should establish an evidence-based minimum.
- The three-recurrence-in-90-days re-entry restriction is a governance threshold `[I,70]` derived from pattern-of-behavior principles; adjust per operational experience and safety/security lead assessment.
