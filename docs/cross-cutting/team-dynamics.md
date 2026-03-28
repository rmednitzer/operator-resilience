# Team Dynamics and Collective Cognitive Governance

**Date:** 2026-03-28
**Scope:** Team-level cognitive governance controls. Collective cognitive failure modes, challenge-and-response protocol, team mode-state, cross-organizational shared operating contracts, and information state synchronization.
**Status:** DRAFT
**Referenced by:** `docs/contracts/oadc.md`; `policies/POL-OR-01-operator-governance.md`; `docs/exercise/exercise-program.md` (ET-6)

---

> **Notation guide — used throughout this document and the repository**
>
> | Tag | Meaning |
> |-----|---------|
> | `[F,nn]` | Verified fact; confidence nn% |
> | `[I,nn]` | Inference from available evidence; confidence nn% |
> | `[S,nn]` | Assumption, heuristic, or unresolved uncertainty; confidence nn% |
>
> `nn` ∈ {50, 70, 80, 90}
>
> **If confidence < 70%:** document what checks would raise it to ≥ 70%; proceed only with safe, reversible partial actions until the threshold is met.

---

## 1 — Purpose

Operator resilience controls defined elsewhere in this repository (H-state table, OADC, epistemic model) are primarily framed for the individual operator. When operators work in teams, additional failure modes emerge that individual controls do not address: teams can collectively suppress dissent, share degraded situational awareness, diffuse accountability, and gradient-suppress legitimate challenges.

This document defines the governance layer that applies when multiple operators share authority over a system or outcome. It is not a replacement for individual controls — it is an additional layer that addresses the failure modes that emerge at the team level.

The framework is adapted from aviation Crew Resource Management (CRM), which has the most mature body of evidence for team cognitive governance in safety-critical operations `[F,85]`.

---

## 2 — Collective cognitive failure modes

| Mode | Definition | Indicators | OADC / governance mitigations |
|------|-----------|------------|-------------------------------|
| **Groupthink** | Team suppresses internal dissent to maintain harmony or consensus. No one challenges a flawed shared plan. | No challenges logged despite high-stakes decision; unanimity achieved unusually quickly; members express private doubt but not public challenge; plan quality degrades as team cohesion increases under stress. | Challenge-and-response protocol (§3) is mandatory, not optional. Decision log must record challenges and responses. Absence of any challenge in a high-stakes event is a finding in post-event review. |
| **Information asymmetry** | Team members have materially different situational awareness. Decisions are made on a false consensus — members believe they share a picture that they do not. | Members give divergent descriptions of current state at sync points; handoffs produce confusion; contradictory actions from different team members. | Mandatory information state synchronization at sync points (§6). Each member explicitly states current understanding with epistemic tags; divergences are reconciled before decisions. |
| **Authority diffusion** | No individual takes clear responsibility because "someone else" holds authority. Decision paralysis or unjustified delegation results. | No decision is made despite conditions requiring one; multiple members each wait for another to act; accountability unclear in post-event review. | Team mode-state declaration (§4) names a specific decision authority for each action domain. Absence of declared authority is itself a trigger for incident commander intervention. |
| **Shared OOTL** | The entire team simultaneously degrades into passive monitoring. No team member has active situational awareness. | All team members have been in monitoring-only mode for > `passive_monitoring_interval`; no member can pass a state-check; team collectively treats automation as sufficient without active validation. | Team OOTL is a OADC condition trigger for the team as a whole. State-check requirement applies collectively: at least one team member must pass a state-check before any team member intervenes. |
| **Authority gradient suppression** | A junior team member will not challenge a senior regardless of the evidence. The senior's assessment is accepted without scrutiny. | Junior members defer visibly; challenges never come from members with lower rank or tenure; senior errors propagate without correction. | Challenge-and-response protocol (§3) applies regardless of rank. The protocol is mandatory; a junior operator's obligation to challenge is not dischargeable by deference. |
| **Collective epistemic overconfidence** | The team collectively rates confidence higher than warranted due to social reinforcement of shared beliefs. Each member's confidence rises because they observe others sharing the same view. | Team confidence is systematically higher than individual members' private assessments; no member surfaces the key `[S]` beliefs; post-event review reveals the team "knew" less than they believed. | Information state synchronization (§6) requires explicit `[F]/[I]/[S]` tagging at sync points. A divergence of > 1 confidence level between any two members on a key belief requires reconciliation. |

---

## 3 — Challenge-and-response protocol

This protocol is adapted from aviation CRM challenge-and-response procedures `[F,85]`. It governs how team members raise and respond to concerns about consequential decisions.

### 3.1 — Obligation to challenge

Any team member is **obligated** — not merely permitted — to challenge a consequential decision that appears to:

- Violate active OADC constraints for any team member involved.
- Apply a belief tagged `[S]` or with confidence < 70% as if it were established fact.
- Contradict a safety principle or hard constraint known to the challenger.
- Involve an authority gradient suppression dynamic (§2, row 5).

The obligation exists regardless of the challenger's rank, tenure, or relationship to the decision-maker. Silence in the face of a known concern is a protocol violation.

### 3.2 — Challenge format

A challenge shall state three elements:

1. **Observation:** What the challenger sees or knows. ("I see [X].")
2. **Concern:** Why it is relevant to the current decision. ("I'm concerned [Y].")
3. **Requested action:** What the challenger is asking the decision-maker to do. ("I request [Z].")

**Example (SRE context):** *"I see the on-call clock shows 14 hours on duty. I'm concerned we've exceeded the OADC N-threshold and any change we make now requires second-person approval. I request we pause and confirm who is acting as second person before proceeding."*

**Example (OT context):** *"I see the pressure reading at sensor 3 is inconsistent with sensor 1. I'm concerned we have a single-source situation for the key process claim. I request we treat this as `[I,70]` until we can cross-validate, and not authorize the valve change on this basis alone."*

The format is designed to be low-friction and non-confrontational. It states facts and concerns rather than assertions about intent or competence.

### 3.3 — Response obligation

The challenged operator must, within the time available:

1. **Acknowledge the challenge verbally** (or in writing, if the communication medium requires it). Silence is not a valid response.
2. **Take one of three actions:**
   - **Modify the decision** to address the concern — and state that they are doing so.
   - **Provide counter-reasoning** — explain why the challenge does not change the decision, with reference to evidence. ("I acknowledge the concern; the reason I'm proceeding is [R], which addresses [Y] because [explanation].")
   - **Invoke the escalation path** — if the challenge cannot be resolved between the two parties.

Counter-reasoning that does not engage with the substance of the challenge is not a valid response. "I've made my decision" is not counter-reasoning.

### 3.4 — Escalation path

If the challenged operator does not respond adequately:

1. **Challenger repeats the challenge** using the same format, explicitly noting it is a second challenge.
2. **Escalate to supervisor** (if available and accessible in the time available).
3. **Escalate to incident commander.**
4. **If no escalation is available or effective:** the challenger declares that they cannot concur with the action and logs this as a dissent record in the decision log. The decision-maker proceeds on their own authority, with the dissent on record.
5. **If the action is imminently safety-critical and no escalation succeeds:** invoke safe state per `docs/cross-cutting/safe-state.md`.

The escalation path is time-aware: under time-pressure conditions (OADC §2), escalation to supervisor and incident commander may need to occur simultaneously rather than sequentially.

### 3.5 — Protection against authority gradient

The challenge-and-response protocol applies regardless of rank or seniority. Specifically:

- A junior operator can challenge a senior using the same format and with the same expectations of response.
- A senior operator cannot simply override a challenge without documented reasoning. "I outrank you" is not counter-reasoning.
- If a senior operator consistently fails to respond to legitimate challenges from junior operators, this pattern is documented in post-event review and constitutes an authority gradient suppression indicator.

The obligation to respond to a challenge is not a threat to senior authority — it is a structural check that senior authority is being exercised on the basis of evidence rather than rank.

### 3.6 — Evidence requirements

Challenges and responses shall be logged in the decision log or event record with:

- Timestamp and identifier of the challenger.
- The three challenge elements (observation, concern, requested action).
- The response type (modify, counter-reasoning, escalation) and content.
- Resolution (decision modified, decision stood with reasoning, escalation invoked).

Absence of challenge logs in a high-stakes event is a finding in post-event review — not neutral evidence.

---

## 4 — Team mode-state

### 4.1 — Definition

The team mode-state is the H-state level at which the team as a whole is treated for authority and constraint purposes. It is derived from individual H-states but is more conservative.

**Computation:**

1. Identify all team members with active authority over the decision domain.
2. The team mode-state is the lowest (most degraded) individual H-state among those members.
3. Apply collective degradation modifiers (§4.2) if triggered.

The team mode-state governs the authority constraints for team-level decisions, regardless of which individual operator takes the action. An H-0 operator acting within a team whose mode-state is H-2 operates under H-2 constraints for team-level decisions.

### 4.2 — Collective degradation modifiers

The team mode-state is further degraded by the following conditions:

| Condition | Modifier |
|-----------|----------|
| Two H-1 operators sharing a buddy-pair | Pair operates as H-1, not H-0. Buddy-pair provides support but does not upgrade the team mode-state. |
| > 50% of the team is at H-2 or below | Declare team-level OADC constraint tightening (incident commander tightening authority per `docs/contracts/contestation-resistance.md` §4.4 — tightening only, not loosening). All team members operate under H-2 constraints regardless of individual state. |
| Shared OOTL detected (§2, row 4) | Treat team mode-state as one level worse until at least one team member passes a state-check. |
| Team sync point missed — information state not synchronized (§6) | Flag as information asymmetry condition. Do not proceed with high-consequence action until reconciliation is complete. |

### 4.3 — Declaration

The incident commander or safety lead declares the team mode-state and logs it with:

- Timestamp.
- Basis for the declaration (individual H-states, collective modifier if applied).
- Effective authority constraints resulting from the team mode-state.
- Planned reassessment point or condition for reassessment.

Team mode-state declarations are append-only log entries. They can be updated (with new entry and rationale) but not revoked retroactively.

---

## 5 — Cross-organizational shared operating contracts

### 5.1 — When this applies

When operators from different organizations share authority over the same system, process, or outcome — joint operations, multi-agency incidents, coalition environments, shared services arrangements — a shared OADC must be established before operations commence.

Operating without a shared OADC in a multi-organizational context is equivalent to operating without an OADC at all: authority limits are undefined at the boundaries, and contestation cannot be evaluated against any agreed standard.

### 5.2 — Shared OADC requirements

Before commencing joint operations:

1. All participating organizations must agree on a shared OADC in writing.
2. Shared parameters are the **more restrictive** of each organization's own OADC values. If Organization A's N-threshold is 10 hours and Organization B's is 8 hours, the shared OADC uses 8 hours.
3. Where organizations have no pre-existing OADC, the most conservative known value for the parameter type is used as the default.
4. Pre-committed decision trees must account for cross-organizational actions and their authority requirements.
5. The shared OADC is stored in the register with identifiers for all participating organizations.

### 5.3 — Authority boundaries

- Each operator retains their own organization's authority limits. Cross-organizational authority cannot be granted unilaterally by one organization.
- Cross-organizational consequential actions (actions that affect the other organization's system, assets, or personnel) require:
  - Explicit delegation documented in writing before or at the point of the action.
  - A buddy-pair that includes at least one operator from each organization.
- Delegation cannot be self-granted. An operator from Organization A cannot grant themselves authority over Organization B's assets without explicit authorization from an authority in Organization B.

### 5.4 — Contestation in shared OADC context

The shared OADC has the same contestation resistance as an organization-specific OADC. Specifically:

- Neither organization can unilaterally modify the shared OADC parameters during the joint operation.
- A claimed exception by one organization's operator does not become valid because the other organization's operator does not object. Silence is not consent.
- If organizations disagree about OADC application, the escalation path goes to the designated joint incident commander or the most senior authority from each organization jointly.
- Post-event review of the shared OADC is conducted jointly, with representatives from all participating organizations.

---

## 6 — Information state synchronization

### 6.1 — Shared situational awareness requirement

Teams must maintain shared SA throughout joint operations. SA gaps between team members are a precondition for information asymmetry (§2, row 2) and authority diffusion (§2, row 3).

The following events require an explicit state synchronization:

- Handoff from one operator to another (any role, any organization).
- Role change within the same operator (e.g., moving from tactical to coordination role).
- Re-engagement after any period of reduced involvement (OOTL condition or passive monitoring).
- Entry of a new team member or organizational representative.
- Scheduled team sync points (defined in the operational plan).

### 6.2 — State synchronization format

At each sync point, each team member with active authority states:

1. **Current system state:** their understanding of the key facts driving the current decision context.
2. **Epistemic tags:** the provenance and confidence of their key beliefs (`[F,nn]`, `[I,nn]`, `[S,nn]`).
3. **Known gaps:** what they do not know that is relevant to current decisions.

Divergences between team members' stated understanding are reconciled before any high-consequence decision. Reconciliation means: the divergence is explicitly examined, the best-available assessment is reached jointly, and the resolution is logged.

**Divergence threshold:** A difference of > 1 confidence level on a shared key belief between any two team members requires explicit reconciliation. Example: Member A holds `[I,80]` for the same belief Member B holds as `[S,50]` — this divergence must be addressed.

### 6.3 — Relationship to exercise program

The team-state-sync exercise (ET-6) validates this capability. It tests whether teams can:

- Execute the state synchronization format correctly under operational conditions.
- Identify and reconcile information asymmetries within the sync point.
- Maintain shared SA through a simulated sequence of handoffs and role changes.

Controls not validated by exercise within their cadence are assumed non-functional per `policies/POL-OR-01-operator-governance.md` stmt 10.

---

## 7 — Confidence notes

- Aviation CRM evidence for challenge-and-response effectiveness is well-established `[F,85]`. Transfer to non-aviation domains is an inference with moderate confidence `[I,75]`; domain-specific validation is required before operational reliance.
- Groupthink is well-documented in social psychology and organizational behavior `[F,90]`; its specific indicators in operational contexts are inferred from the general literature `[I,75]`.
- The "50% of team at H-2" threshold for team-level OADC tightening (§4.2) is a governance estimate, not an empirically derived threshold `[S,65]`. It should be calibrated to the specific operating environment and validated by exercise.
- Shared OOTL as a team-level condition is documented in automation research in aviation and process control `[F,80]`; the collective state-check requirement is derived by analogy `[I,75]`.
- Cross-organizational shared OADC requirements (§5) are inferred from multi-agency incident management principles (ICS/NIMS) and coalition operations doctrine `[I,70]`. No direct validation source.
