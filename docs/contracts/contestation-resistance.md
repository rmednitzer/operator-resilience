# OADC Contestation Resistance

**Date:** 2026-03-28
**Scope:** Mechanisms that make the Operator Authority Degradation Contract resistant to challenge by operators or adversaries. Covers contestation vectors, resistance patterns, meta-contract governance, and verification integrity requirements.
**Status:** DRAFT
**Referenced by:** README.md; `docs/cross-cutting/team-dynamics.md` §4.2

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

An OADC is only effective if it is consistently applied. Contestation resistance is the set of mechanisms that prevent operators, adversaries, or organizational pressure from successfully arguing that the OADC should not apply in a specific situation.

Contestation is not always adversarial. It frequently arises from well-intentioned operators who genuinely believe their situation is exceptional, that the threshold is miscalibrated, or that following the protocol would produce a worse outcome. These beliefs may occasionally be correct — which is precisely what makes them dangerous. The OADC's value lies not in its infallibility but in its resistance to being bypassed on the basis of in-the-moment judgment, which is structurally unreliable under exactly the conditions the OADC governs.

An OADC that can be argued away under pressure provides no protection under pressure.

---

## 2 — Contestation vectors

The following table defines the primary vectors by which an OADC may be contested and the structural reason each vector is dangerous.

| # | Vector | Description | Why it is dangerous |
|---|--------|-------------|---------------------|
| CV-1 | "This situation is exceptional" | Operator or third party argues that the current circumstances are outside the OADC's intended scope, warranting a suspension or exception. | Virtually every incident that triggers OADC constraints will feel exceptional to the operator in it. Allowing in-incident exception claims removes protection precisely when it is most needed. |
| CV-2 | "The threshold is wrong for this context" | Operator or peer argues that the specific parameter value (N, T, consequence_threshold) is inappropriate for the actual conditions. | May be a valid observation — but the correct response is a documented change process, not an in-incident override. |
| CV-3 | "I'm not actually degraded" | Operator self-assesses adequate capacity despite objective indicators or peer assessment to the contrary. | Self-assessment of adequacy is systematically unreliable under fatigue, stress, and OOTL conditions — the exact states the OADC detects. |
| CV-4 | "There's no time for protocol" | Time pressure is invoked to justify bypassing OADC controls. | Time pressure is a primary adversarial manipulation technique and a primary natural degradation trigger. It is also the condition under which pre-committed decision trees are most valuable. |
| CV-5 | "Management authorized an exception" | Claimed override authority from a manager or authority figure, without authenticated documentation. | Verbal-only authority claims are trivially fabricated and cannot be audited post-event. |
| CV-6 | "The system knows better than the OADC" | Automation bias: operator defers to automated system output in ways that erode the epistemic caution required by OADC conditions. | Automation bias causes operators to reduce their own situational awareness and epistemic checks, degrading exactly the capacities the OADC protects. |
| CV-7 | Social engineering of the OADC itself | Adversary convinces the operator that following the OADC would produce a harmful outcome, thus making protocol violation appear to be the correct action. | Most sophisticated vector. Exploits the operator's legitimate judgment to make the OADC the obstacle rather than the safeguard. |

---

## 3 — Resistance patterns

For each contestation vector, the following resistance patterns are pre-committed. They are not negotiable during an incident.

### 3.1 — CV-1: Exception resistance

**Mechanism:** OADC parameters are set in advance by qualified reviewers, not during incidents. No in-incident renegotiation of scope is valid.

**Implementation:**
- An operator who believes their situation is exceptional shall log that belief in the decision record with full epistemic tagging (`[I]` or `[S]`, with confidence and supporting evidence).
- The decision to apply the OADC is not subject to operator veto. The incident commander or safety lead may note the operator's concern for post-event review.
- All exception claims are reviewed post-event under REV-nnn (post-event review record; see `data/registers/` for canonical entries). If the exception was warranted, it informs an OADC parameter change via the safety-critical change process.
- "Exceptional" incidents that trigger contestation more than once in a review cycle are an indicator that the OADC parameters need revision — not that exception claims should be granted.

### 3.2 — CV-2: Parameter stability

**Mechanism:** OADC parameters cannot be changed under time pressure or during an active incident. Changes require the two-person safety-critical review process defined in `CONTRIBUTING.md`.

**Implementation:**
- Any proposed parameter change is logged as a change request in the register, not applied directly.
- Changes to OADC parameters are version-controlled; only the approved version is operative.
- A parameter concern raised during an incident is documented for post-event review and does not alter the operative OADC.
- Operators who believe a parameter is systematically wrong are encouraged to raise it through the formal review process. This is a healthy signal; informal overrides are not.

### 3.3 — CV-3: Objective indicator override

**Mechanism:** Self-report of degradation is always respected (an operator who says they are degraded is treated as degraded). Self-report of adequate capacity can be overridden by peer assessment or automated indicators.

**Implementation:**
- If peer observation or automated indicators conflict with operator self-assessment of adequate capacity, the more conservative assessment governs.
- The operator may request a formal state-check to challenge a peer assessment, but during the assessment period, the conservative constraint applies.
- This asymmetry is intentional: false positives (treating a capable operator as degraded) impose operational cost but are recoverable. False negatives (treating a degraded operator as capable) may be catastrophic.
- An operator who disputes a peer assessment shall log the dispute; it is reviewed post-event. Repeated disagreements between operator self-assessment and peer assessment are an indicator for review of assessment criteria and possible return-to-duty evaluation.

### 3.4 — CV-4: Time pressure resistance

**Mechanism:** Under the OADC time-pressure condition (decision required in less than `min_review_threshold` seconds), only pre-committed decision trees are available. Novel authority is not available under time pressure.

**Implementation:**
- Pre-committed decision trees are defined per operating environment before operational use and stored with the OADC instance.
- An operator cannot authorize a novel high-consequence action that is not in the pre-committed tree during a time-pressure condition.
- If the required action is not in the tree, the default action is the safe state or the most conservative available option.
- Time pressure invoked by a third party (CV-4 combined with CV-5 or CV-7) constitutes a duress indicator per `docs/adversarial/duress-protocol-spec.md`.

### 3.5 — CV-5: Override authority validation

**Mechanism:** All claimed management or authority exceptions must be authenticated via a second channel, logged with rationale, and reviewed post-event. Verbal-only overrides are not valid.

**Implementation:**
- The authentication requirement is: the overriding authority is confirmed via a channel independent of the one used to communicate the override request (e.g., if the request arrived by phone, authentication uses a separate callback to a registered number or a pre-established authentication protocol).
- The log entry for an override must include: identity of the claimed overriding authority, channel used for request, channel used for authentication, stated rationale, timestamp, and operator identifier.
- All overrides are reviewed post-event under REV-nnn, regardless of outcome.
- An override that cannot be authenticated at time of request is treated as non-valid. The operator continues under the existing OADC constraints.

### 3.6 — CV-6: Automation bias guardrail

**Mechanism:** Automated system outputs are subject to the same epistemic trust boundary checks as any other information source. OOTL monitoring requirements and state-check requirements apply regardless of automation level.

**Implementation:**
- Before acting on an automated recommendation for a high-consequence action, the operator completes an epistemic trust boundary check per `docs/epistemics/belief-provenance.md` §6.
- System-provided assessments are tagged `[I]` unless the operator can independently verify the underlying data. They do not automatically achieve `[F]` status.
- OOTL monitoring interval applies to automation-supervised operations. Passive handover to an automated system does not reset the operator's OOTL clock for SA purposes.
- State-check is required before any manual intervention following an automation-supervised period exceeding `passive_monitoring_interval`.

### 3.7 — CV-7: Contract integrity

**Mechanism:** The OADC definition and its conditions are not modifiable by the operator who is subject to them. The OADC is an external constraint, not a self-regulation agreement.

**Implementation:**
- If an operator is convinced that following the OADC will produce a harmful outcome, they shall: log the concern with full epistemic tagging, escalate to the incident commander or safety lead, and continue operating under OADC constraints until a second person with override authority (CV-5 validated) authorizes a specific deviation.
- The second person providing override authorization is themselves subject to their own OADC. They cannot override their own constraints.
- An argument that "the OADC is wrong in this case" is treated as a potential social engineering indicator and logged as such. Post-event review assesses whether it was legitimate or adversarial.
- If an operator acts in violation of the OADC based on a social engineering attack, the post-event review documents this as an OADC control failure, not as an individual performance failure. The control failure informs hardening of the resistance pattern.

---

## 4 — Meta-contract governance

The meta-contract defines the governance rules for the OADC contract itself — who can define it, change it, and what constraints are inviolable.

### 4.1 — Who can define an OADC

An OADC instance may be created only by the safety/security lead with management approval. Creation requires:

1. Identification of the operating environment and operator roles to which it applies.
2. Parameter value justification (N, T, min_review_threshold, consequence_threshold, passive_monitoring_interval, circadian_window) with supporting evidence or documented rationale.
3. Definition of pre-committed decision trees for all time-pressure conditions.
4. Identification of the governing regulatory framework for each parameter where applicable (per `docs/contracts/oadc.md` §3).
5. Exercise validation plan — the exercise type and cadence that will validate the OADC parameters before and after operational use.

### 4.2 — Who can change an OADC

Changes to any OADC parameter require the same two-person safety-critical change process that created it:

- Safety/security lead review and independent reviewer sign-off.
- Impact analysis: CACE (changing anything changes everything) — what other artifacts, parameters, or exercise criteria are affected?
- Documented blast radius assessment.
- Version increment and entry in the OADC register.

Changes proposed during or immediately after an incident are not operative until the review process is complete. The operative version at incident time is the version in effect before the incident.

### 4.3 — What cannot be changed mid-incident

The following OADC elements are frozen once an incident is declared and cannot be changed until the incident is closed and the formal review process completes:

- `N` — on-call duty hour limit
- `T` — incident duration buddy-pair trigger
- `consequence_threshold` — high-consequence action classification boundary
- `min_review_threshold` — minimum time before time-pressure condition activates
- `passive_monitoring_interval` — maximum minutes before OOTL state-check required
- `circadian_window` — local time range for circadian adjustment
- Buddy-pair trigger conditions
- Pre-committed decision tree content

### 4.4 — What can be adjusted in-incident (tightening only)

The incident commander may **tighten** (but not loosen) OADC constraints in-incident if the environment deteriorates beyond the parameters that were current when the OADC was set. For team-level applications of this authority (e.g., when > 50% of the team is at H-2 or below), see `docs/cross-cutting/team-dynamics.md` §4.2.

- Lower the effective `N` or `T` threshold (treat as if more time has elapsed than has).
- Expand the set of actions requiring second-person approval.
- Declare organizational stress condition, triggering OADC §2 organizational stress row.
- Require buddy-pair at a lower H-state than specified.

All in-incident tightenings are logged with rationale, timestamped, and reviewed post-event. They do not constitute a permanent parameter change.

### 4.5 — Version control

Each OADC instance is version-controlled in `data/registers/oadc-register.yaml`. Version fields:

- `version` — incremented on any parameter change.
- `effective_date` — date the version became operative.
- `superseded_date` — date the version was replaced (blank if current).
- `change_rationale` — brief description of what changed and why.

Only the current approved version (no `superseded_date`) is operative. Historical versions are retained for audit.

---

## 5 — Verification integrity requirements

### 5.1 — Append-only decision log

The decision log is the primary evidentiary record of OADC compliance. It must be:

- **Append-only:** existing entries cannot be amended, deleted, or overwritten.
- **Operator-isolated:** the log must not be modifiable by the operator whose condition or action is being logged. Where technical append-only enforcement is not feasible, this becomes a procedural compensating control (two-person custody of log media, or signed entries).
- **Corrections:** if a log entry is factually incorrect, a separate correction record is appended (with timestamp, identifier of the correcting party, nature of the correction, and reason). The original entry is never removed.

### 5.2 — Evidence timestamping and hash verification

Evidence produced during an OADC condition (state-checks, pre-decision checks, peer assessments, override records) must be:

- **Timestamped** to ISO 8601 precision at the point of creation.
- **Hash-verifiable** where technically feasible: a cryptographic hash of the record is computed at creation and stored separately, enabling detection of post-hoc modification.
- **Attributed:** each record carries the identifier of the operator who produced it.

Where hash verification is not technically feasible, the compensating control is physical or procedural custody: the record is stored in a medium or system that the operator under OADC constraint cannot access unilaterally.

### 5.3 — Post-event contestation review

Every post-event review (REV-nnn) shall include a contestation section:

1. **Did any contestation attempt occur?** (CV-1 through CV-7, or other)
2. **How was it handled?** (resistance pattern applied, deviation, or failure to apply)
3. **Was the contestation legitimate?** (informed parameter review, or manipulation)
4. **What hardening is indicated?** (resistance pattern update, training, parameter review, or no action)

Absence of a contestation review in a post-event record is itself a finding.

### 5.4 — OADC as its own evidence

The OADC structure provides its own verification trail:

- All trigger events are logged (OADC §2 trigger conditions are loggable at point of activation).
- If a trigger was contested, the log shows the contest and its resolution.
- If no contest is logged for an incident where OADC conditions were active, that absence is notable but not necessarily indicative — it may mean the controls worked without friction.
- An OADC trigger that was not logged at all is a control gap requiring investigation.

---

## 6 — Confidence notes

- The contestation resistance framework is inferred from operational security literature, CRM research, and insider threat governance `[I,70]`. It has not been validated in field use in this form. Validate with red-team exercises (exercise type: `oadc-contestation-test`) before operational reliance.
- The claim that self-assessment of adequate capacity is systematically unreliable under fatigue and stress is well-supported in human factors literature `[F,85]`. The asymmetric override rule (§3.3) is derived from this finding `[I,80]`.
- The social engineering vector (CV-7) is documented in adversarial manipulation research `[F,80]`; the specific resistance mechanism (escalation plus contract integrity) is an inference from analogous CRM and security controls `[I,70]`.
- Hash verification as a compensating control for log integrity is standard practice in digital forensics `[F,90]`; its applicability in non-technical environments depends on deployment context `[I,75]`.
