# Incident Communications Security

**Date:** 2026-03-28
**Status:** DRAFT
**Scope:** Secure incident communication protocols for contested, degraded, or high-stress operating conditions. Covers closed-loop (readback/hearback) protocol, channel authentication, out-of-band verification, compromised communications handling, and evidence requirements.
**Referenced by:** `docs/adversarial/threat-model.md`

---

> **Notation guide**
>
> | Tag | Meaning |
> |-----|---------|
> | `[F,nn]` | Verified fact; confidence nn% |
> | `[I,nn]` | Inference from available evidence; confidence nn% |
> | `[S,nn]` | Assumption, heuristic, or unresolved uncertainty; confidence nn% |
>
> `nn` ∈ {50, 70, 80, 90}

---

## 1 — Purpose

This document defines the communications security requirements for incident operations. It specifies the closed-loop protocol, channel authentication procedures, out-of-band verification triggers, compromised communications handling, and decision-log evidence requirements applicable to all high-consequence communications in environments governed by this framework.

Communications security during incidents is not primarily a cryptographic problem — it is a human reliability problem. Under high stress, time pressure, and cognitive load, operators are statistically less vigilant about identity verification, less likely to challenge unusual instructions, and more susceptible to authority spoofing and urgency manipulation `[F,85]`. This document addresses those failure modes.

---

## 2 — The core problem

Incident communications are a primary attack surface for information manipulation (threat T-3) and authority impersonation (threat T-1) as defined in `docs/adversarial/threat-model.md`. The following structural vulnerabilities make incident comms specifically attractive to adversaries:

| Vulnerability | Mechanism | Adversarial exploitation |
|--------------|-----------|--------------------------|
| Stress-impaired verification | Under high cognitive load, operators skip or abbreviate identity and authority checks | Adversary times instruction delivery to coincide with peak incident stress |
| Urgency bias | Time-pressured operators accept instructions with reduced scrutiny to maintain operational tempo | Adversary introduces artificial urgency to compress the verification window below the OADC minimum review threshold |
| Authority gradient | Operators are trained to respond to supervisor/authority instructions; challenging authority feels costly under stress | Adversary impersonates a supervisor or authority figure; operator's social deference overrides verification instinct |
| Channel ambiguity | During incidents, communications arrive via multiple channels (phone, chat, radio, email); channel provenance is easily confused | Adversary routes instruction via a familiar channel or mimics channel characteristics of a trusted source |
| Cognitive overload | Sustained incident workload degrades vigilance and working memory; operators may not notice or recall having verified identity | Adversary exploits degraded vigilance at H-2+ to pass an unverified instruction through the decision chain |

---

## 3 — Closed-loop (readback/hearback) protocol

### 3.1 — Definition

The closed-loop protocol is a three-step communication sequence that ensures critical information is received, understood, and confirmed before action is taken:

1. **Transmit:** Sender transmits the instruction, order, or information.
2. **Readback:** Receiver reads back the key element of the message — the critical content, not a paraphrase.
3. **Confirm or correct:** Sender explicitly confirms the readback is accurate, or corrects it and repeats from step 1. The message is **not acted on** until the loop is closed by sender confirmation.

The requirement is sender confirmation of receiver readback, not receiver acknowledgment of receipt. "Roger" or "understood" without explicit sender confirmation does not close the loop.

### 3.2 — Provenance

The closed-loop protocol is adapted from aviation standard operating procedure (ICAO Annex 2 / PANS-ATM Doc 4444) for ATC-pilot communications `[F,90]`. It is widely applied in aviation, maritime, nuclear plant operations, and military command. Its adaptation here to IT/SRE, OT/ICS, and autonomous platform operations is an inference from those domain applications `[I,80]`.

### 3.3 — Mandatory triggers

The closed-loop protocol is mandatory for all communications in the following categories:

| Category | Rationale |
|----------|-----------|
| All high-consequence decisions communicated verbally or via chat | Ensures the consequential instruction is precisely understood and confirmed before action |
| All authority delegations | Ensures the receiving operator understands the exact scope and limits of delegated authority |
| All system-state change authorizations | Ensures the authorized state change is unambiguous before execution |
| All duress-signal acknowledgments | Ensures the monitoring function's acknowledgment reaches the signaling operator precisely and is confirmed — incomplete closure here leaves the operator without confirmed support activation |

### 3.4 — Protocol variants by channel

| Channel | Protocol variant | Completion criterion |
|---------|-----------------|----------------------|
| Voice (radio, telephone, in-person) | Explicit verbal readback of key element; sender states "correct" or corrects | Sender has verbally confirmed readback accuracy |
| Text / chat | Receiver explicitly quotes or states the key element in a confirmation reply; sender replies with confirmation | Sender has replied confirming the stated key element |
| System action | Two-person confirmation gate: requester specifies the action; approver states the action back and confirms before executing | System records both requester instruction and approver confirmation (where technically feasible) |
| Email / asynchronous | Receiver acknowledges with explicit restatement of key element and required action; sender confirms | Sender confirmation received before receiver takes action |

### 3.5 — Protocol exemptions

The closed-loop protocol may be abbreviated **only** when both of the following conditions are met:

1. The communication is low-consequence by the active OADC definition (below the `consequence_threshold` parameter).
2. The communication is between two parties with a confirmed shared situational picture (both parties have passed a state-check within the OADC `passive_monitoring_interval`).

Abbreviation means that the readback step may be shortened to a key-word confirmation rather than full element restatement. The sender confirmation step is never optional.

---

## 4 — Channel authentication

Before acting on any communication, the operator shall verify four properties of the communication. These checks apply regardless of how familiar the source appears.

| Property | Check | Required verification method |
|----------|-------|------------------------------|
| **Identity** | Is this the person they claim to be? | Known-voice recognition plus challenge/response, or second-channel confirmation if identity is uncertain. Do not rely on caller ID, display name, or channel origination alone. |
| **Authority** | Is this person authorized to issue this instruction under the current OADC conditions? | Cross-reference the instruction against the active OADC instance. Instructions that would require authority expansion, exception, or override must be treated as an OADC "unverified authority" condition until the authority chain is confirmed. |
| **Freshness** | Is this instruction current? Is it a replay of an earlier instruction now out of context? | Confirm instruction timestamp or context reference. Instructions without a clear operational context anchor shall be treated as potentially stale or replayed. |
| **Consistency** | Does this instruction align with the established situational picture? | Cross-check against the last confirmed state. Instructions that are inconsistent with the established picture without explanation shall trigger a belief consistency check per `docs/epistemics/belief-provenance.md` §6. |

A communication that fails any two or more of these checks shall not be acted on until the failing checks are resolved. The OADC "communication from unverified authority" condition applies.

---

## 5 — Out-of-band verification

### 5.1 — When out-of-band verification is required

The operator shall escalate to a second, independent channel for identity confirmation before acting when any of the following conditions apply:

- The instruction would require the operator to **expand authority** beyond the current OADC-authorized scope.
- The instruction would require an **irreversible action** and the identity check is not already confirmed at high confidence.
- The instruction would **override a safety control** or OADC constraint.
- Identity cannot be confirmed via the primary channel alone (e.g., unfamiliar voice, no challenge/response established, unusual communication pattern).
- Any of the channel authentication checks in §4 fail.

### 5.2 — Out-of-band verification procedure

1. Do not act on the instruction while verification is pending. Inform the source that verification is required before action can proceed.
2. Contact the claimed sender via a pre-established, independent channel (not a channel that could be controlled by the same adversary if the primary channel is compromised).
3. Use a pre-established challenge/response or identifying information exchange that was agreed outside the current incident context.
4. Log the verification outcome, channel used, and challenge/response method in the decision log.
5. If verification cannot be completed within the operational timeframe, treat as an OADC "communication from unverified authority" condition and escalate.

### 5.3 — Out-of-band channel requirements

Pre-established out-of-band channels shall be defined in the operating environment's OADC instance and duress protocol before operational use. An out-of-band channel that is improvised during an incident cannot be trusted, because it may itself be under adversarial control.

---

## 6 — Compromised communications handling

If the primary communications channel is suspected to be compromised (intercepted, manipulated, or under adversarial monitoring or control):

1. **Cease acting on instructions received via the suspected channel** until the compromise status is resolved.
2. **Fall back to the pre-established alternate channel** defined in the OADC instance or duress protocol for this environment. If no alternate channel is defined, escalate immediately.
3. **Declare channel compromise to the incident commander.** Channel compromise is an OADC "contested operating environment" condition trigger.
4. **Log the compromise event** with timestamp, indicators of compromise observed, and actions taken.
5. **Do not attempt to diagnose the compromise** via the suspected channel — doing so may alert the adversary or provide additional exploitation opportunity.

Indicators that may suggest channel compromise include: unexpected changes in communication patterns from a known source, instructions that contradict the established situational picture without explanation, unusual message routing or relay, instructions that apply urgency pressure specifically to prevent cross-channel verification, and channel metadata inconsistencies (e.g., caller ID mismatch, timestamp anomalies).

These indicators are not diagnostic on their own. They are triggers for heightened scrutiny and the out-of-band verification procedure in §5.

---

## 7 — Evidence requirements for high-consequence communications

Decision logs must capture the following for all high-consequence communications. This requirement extends the decision log format in `templates/decision-log/TEMPLATE-decision-log-entry.md`.

| Field | Description |
|-------|-------------|
| Communication source | Who issued the communication (identifier, role) |
| Channel | The channel used (voice, chat, email, system gate, etc.) |
| Authentication method | Which identity check was applied and the outcome |
| Authority verification | Whether authority was confirmed against the active OADC; how |
| Readback outcome | Whether the closed-loop protocol was completed; if not, why |
| Out-of-band verification | Whether OOB verification was performed; channel and outcome |
| Timestamp | ISO 8601 timestamp of the communication and of the closed-loop confirmation |

This evidence record supports post-event review and provides the audit trail required to detect communications-layer manipulation in retrospect.

---

## 8 — Relationship to OADC conditions

The following OADC conditions in `docs/contracts/oadc.md` §2 interact directly with communications security:

| OADC condition | Communications security relevance |
|----------------|----------------------------------|
| **Communication from unverified authority** | This condition is triggered whenever the channel authentication checks in §4 cannot be completed. The OADC response (hold; authenticate before acting; second-channel verification) is operationalized by the procedures in §5 of this document. |
| **Contested operating environment** | When this condition is declared, the two-person rule applies to all consequential actions. Communications security requirements are tightened: all instructions require out-of-band verification regardless of apparent source familiarity. Channel compromise handling (§6) is activated. |
| **Time pressure below minimum review threshold** | Time pressure applied to a communication that also fails one or more channel authentication checks is a strong adversarial indicator. The pre-committed decision tree applies; no novel authority is authorized; the closed-loop protocol is non-negotiable regardless of time pressure. |

---

## 9 — Relationship to belief provenance

The epistemic status of a communication received but not verified follows the tagging rules in `docs/epistemics/belief-provenance.md` §2:

| Communication status | Belief provenance tag | Rationale |
|---------------------|----------------------|-----------|
| Received but source not authenticated | `[S]` | No verified trust-boundary basis; treat as assumption |
| Received, source authentication confirmed, closed loop completed | `[F]` (if source is authenticated and content is fresh) | Authentication and readback confirm source and content; belief can be treated as verified |
| Received, closed loop completed, but source authentication is partial or single-channel only | `[I]` | Loop closes content accuracy but does not fully resolve identity; inference rather than verified fact |
| Received via suspected-compromised channel | `[S,50]` | All channel-derived beliefs degraded to assumption; treat as adversarial until resolved |

This mapping ensures that communications that have not completed the verification process do not enter the decision chain as `[F]` beliefs, which would inflate operator confidence beyond what the epistemic basis supports.

---

## 10 — NIS2 Art. 21(2)(j) alignment

This document and the procedures it defines support alignment with NIS2 Art. 21(2)(j), which requires the use of secured voice, video and text communications as part of the cybersecurity risk management measures for in-scope entities. Indicative mapping — applicability depends on entity classification, sector, and national transposition. See `docs/integration/regulatory-cross-reference.md` for detailed analysis.

| NIS2 Art. 21(2)(j) element | Repository control |
|----------------------------|-------------------|
| Secured voice communications | Closed-loop protocol (§3); out-of-band verification (§5); channel compromise handling (§6) |
| Secured text communications | Closed-loop protocol text variant (§3.4); channel authentication checks (§4) |
| Secured video communications | Channel authentication checks (§4); out-of-band verification (§5) |
| Communications integrity during incidents | Decision log evidence requirements (§7); belief provenance tagging (§9) |

---

## 11 — Confidence notes

- The closed-loop / readback-hearback protocol is a well-established aviation standard operating procedure with extensive validation evidence in aviation, maritime, and nuclear domains `[F,90]`. Its adaptation to IT/SRE and OT/ICS incident communications is an inference from those applications `[I,80]`.
- The human factors vulnerabilities described in §2 (stress-impaired verification, urgency bias, authority gradient) are documented in CRM, incident command, and adversarial social engineering research `[F,85]`.
- The channel authentication framework (§4) and out-of-band verification triggers (§5) are inferences from cybersecurity identity verification and communications security practice applied to the operator context `[I,75]`.
- Specific thresholds and triggers (e.g., when exactly to invoke OOB verification) are operationally calibrated estimates `[S,70]`. Validate and adjust per operating environment through tabletop exercises before operational reliance.
