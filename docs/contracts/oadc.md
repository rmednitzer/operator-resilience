# Operator Authority Degradation Contract (OADC)

**Date:** 2026-03-28
**Scope:** Formal definition of how operator authority narrows as conditions degrade. Covers condition taxonomy, detection methods, authority responses, recovery conditions, and system enforcement requirements.
**Status:** DRAFT

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

An Operator Authority Degradation Contract (OADC) is the explicit, pre-committed agreement about how operator authority changes when conditions change. It is analogous to a system degraded-mode hierarchy — where system capability is formally reduced as conditions worsen — but applied to the human operator.

RBAC (Role-Based Access Control) defines what an operator *can* do. The OADC defines what an operator *should* do, under what conditions, and what happens when those conditions change. The OADC exists because RBAC does not degrade with fatigue, does not account for epistemic state, and does not resist social engineering.

## 2 — OADC condition taxonomy

| Condition | Detection method | Authority response | Recovery condition |
|---|---|---|---|
| On-call duration > N hours | Time since shift start | Narrow scope; second-person approval for irreversible actions | Handoff; minimum rest before re-assuming authority |
| Incident duration > T hours | Time since declaration | Mandatory buddy-pair; scheduled handoff | Incident closed or formal handoff |
| Single information source for key claim | Decision log review | Cannot authorize high-consequence action on single source | Second independent source confirms |
| Time pressure below minimum review threshold | Time between alert and required decision | Pre-committed decision tree only; no novel authority | Time pressure relieved |
| Communication from unverified authority | Source authentication check | Hold; authenticate before acting | Identity confirmed via second channel |
| Operator self-reports degradation | Explicit declaration | Authority transfers to alternate | Cleared by return-to-duty protocol |
| Epistemic degradation markers detected | Peer observation or automated | Narrow authority; peer validation for all decisions | Markers resolve; supervisor confirmation |
| Contested operating environment | Declared by incident commander or security | Two-person rule for all consequential actions | Environment declared safe |
| Extended passive monitoring (OOTL) | Time since last active control input or successful state-check | State-check required before any intervention; if failed, treat as H-2 | Active engagement re-established; state-check passed |
| Circadian low (02:00–06:00 local, or woken from sleep) | Time of day; operator status | Treat as one H-state worse than observed; second-person for irreversible | Alert > 30 minutes and state-check passed |
| Organizational stress | Declared by management or security | Tighten contract for all operators: lower thresholds for two-person rule | Stress condition formally lifted |

> **H-state cross-reference:** H-states (H-0 to H-4) are the formal operator mode-state hierarchy used throughout this document. H-0 = full cognitive capacity; H-4 = incapacitated. Full taxonomy, indicators, and authority limits are defined in `docs/resilience/h-state-table.md`. "Treat as one H-state worse" means: the observed state H-n is treated as H-(n+1) for all authority decisions; H-4 does not degrade further.

## 3 — Parameters

OADC parameters are set per operating environment **in advance**, not improvised during an incident:

- `N` — maximum on-call duty hours before authority narrows (environment-specific; typically 8–12 hours). The range 8–12 hours is an indicative baseline, not a hard limit. Environments subject to stricter regulatory requirements (e.g., EASA Part-ORO.FTL for aviation, EU Working Time Directive for EU operators) must use the stricter applicable limit. Each OADC instance shall record which regulatory framework governs its `N` value to support audit traceability.
- `T` — maximum incident duration hours before buddy-pair mandatory (environment-specific; typically 4–8 hours). As with `N`, this is a baseline range; stricter regulatory limits take precedence. Each OADC instance shall record the governing framework if a regulation constrains this value.
- `min_review_threshold` — minimum time in seconds between alert and required decision before pre-committed tree applies
- `consequence_threshold` — classification boundary between standard and high-consequence actions
- `passive_monitoring_interval` — maximum minutes of passive monitoring before state-check required (default: 30). This default is based on literature on out-of-the-loop (OOTL) degradation [S,75]; validate against your specific operational context and adjust per occupational health assessment.
- `circadian_window` — local time range for circadian adjustment (default: 02:00–06:00). This default is grounded in human circadian biology literature [F,85]. Programmes with non-standard shift patterns (e.g., rotating shifts, maritime watches) should adjust per occupational health assessment rather than using the default.

## 4 — System enforcement

Where technically feasible, the system should enforce OADC constraints, not rely solely on operator self-restraint:

- Two-person authentication gates for actions requiring second-person approval
- Session timeout or activity check for passive monitoring duration
- Time-of-day awareness in authorization workflows
- Logging of all OADC trigger events as evidence

Where technical enforcement is not feasible, procedural compensating controls must be documented and validated before operational use. Validation shall be performed via exercise type: `oadc-threshold-validation`.

**Audit log integrity:** The OADC event log must be append-only. It must not be modifiable by the operator whose condition or action is being logged. Where technical append-only enforcement is not feasible, this requirement becomes a procedural compensating control subject to the above.

## 5 — OADC instances

OADC instances are defined per operating environment and stored as canonical YAML in `data/registers/oadc-register.yaml`. Each instance specifies the parameter values for a specific context (e.g., production SRE on-call, OT control room, autonomous platform GCS operator).

## 6 — Confidence notes

- The OADC concept is novel and has not been validated in field use [S,70]. The framework has been cross-referenced against NATO HFM-322, EU AI Act Art. 14, and ISO 10075 series for structural alignment, which raises confidence in the framework design from the initial estimate. Field validation with tabletop exercises and real incident review remains required before operational reliance. If confidence in local parameter settings is < 70%: define the exercise program that would raise it; do not depend on untested OADC thresholds for safety-critical decisions.
- Circadian effects on performance are well-established [F,90]; the specific window and "one H-state worse" heuristic are estimates [S,75].
- Organizational stress as a trigger is documented in insider threat literature [F,80]; the OADC response is an inference [I,70].
