# Exercise Program

**Date:** 2026-03-28
**Scope:** Defines the operator-resilience exercise program: purpose, exercise types, cadences, acceptance criteria, evidence capture, failure response, initial sequence, and post-exercise review requirements.
**Status:** DRAFT
**Referenced by:** README.md §Getting started step 7; POL-OR-01 statements 5, 7, 10; `schemas/exercise-record.schema.json`

---

## 1 — Purpose

This document defines the exercise program that validates operator-resilience controls defined in this repository. Exercises are the primary mechanism for converting governance artifacts (OADC instances, duress protocols, safe-state specifications, decision trees, H-state assessment methods) from documented intent into demonstrated capability.

Exercise records are captured using `templates/exercise/TEMPLATE-exercise-record.md` and stored as canonical YAML in `data/registers/exercise-register.yaml` per the schema at `schemas/exercise-record.schema.json`.

---

## 2 — Program philosophy

**Principle 7 of this repository: Exercise or it does not exist.**

A governance artifact that has never been exercised provides no assurance. The OADC defines how authority degrades — but if operators have never practiced working within those constraints, the contract will collapse under pressure. Duress protocols define covert signals — but if signals have never been practiced, they will not be executed correctly under real coercion. Safe-state procedures define what the system does in the absence of a qualified operator — but if the transition has never been tested, it will fail at the worst moment.

This program operationalizes Policy Statement 10: *Controls not exercised within their cadence are assumed non-functional.* An unexercised control is not merely unvalidated — it is, for governance purposes, absent.

**Consequence:** Program managers and safety leads must track exercise cadence as actively as they track system maintenance schedules. An exercise overdue by more than one cadence cycle shall be documented as a control gap and reported in the next post-event review or program review.

---

## 3 — Exercise types

The following seven exercise types are defined. Each is described in a dedicated section below.

| ID | Exercise type | Minimum cadence | Key governance control validated |
|----|---------------|-----------------|----------------------------------|
| ET-1 | `duress-drill` | Annually | Duress protocol execution; covert signal; authority containment |
| ET-2 | `social-engineering-red-team` | Semi-annually | Social engineering resistance; identity verification; skeptical decision-making |
| ET-3 | `oadc-threshold-validation` | Program start + after any OADC change | OADC parameter correctness; operator familiarity with constraints |
| ET-4 | `epistemic-check-drill` | Quarterly | Pre-decision epistemic check; confidence gating; evidence tagging |
| ET-5 | `decision-tree-walkthrough` | Annually | Pre-committed decision tree completeness; operator ability to execute under time pressure |
| ET-6 | `team-state-sync` | Semi-annually | Team mode-state awareness; information asymmetry detection; challenge-and-response protocol |
| ET-7 | `safe-state-test` | Program start + after any safe-state change | Safe-state trigger; transition execution; return authorization |

---

## 4 — ET-1: Duress drill

### 4.1 Description and objective

A duress drill exercises the full duress protocol: covert signal transmission, authority containment, escalation, and recovery. The objective is to verify that all participating operators can correctly execute the duress protocol without behavioral cues visible to an uninvolved observer, and that authority containment activates within the required time.

Duress drills shall be conducted without prior notification of the specific time or scenario to at least one participant playing the role of the coerced operator.

### 4.2 Minimum cadence

Annually. Environments with a higher threat profile (adversarial operator targeting is a credible concern) should exercise semi-annually.

### 4.3 Required participants

- At least one operator designated to play the coerced-operator role (may be pre-informed of role, not of timing)
- At least one supervisor or incident commander
- Exercise facilitator (not a participant in the operational scenario)
- Representative from the buddy-pair if buddy-pairs are defined in the active OADC instance

### 4.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| Covert signal transmitted within scenario timeline | ≤ 60 seconds after duress cue presented |
| Signal recognized and authority containment initiated by supervisor | ≤ 120 seconds after signal |
| No overt behavioral indicator of signal visible to simulated coercer | Observed by facilitator: pass/fail |
| Escalation contacts notified (simulated) within protocol timeline | Per duress protocol definition |
| Operator can debrief the protocol steps from memory | All critical steps stated |

Partial pass (at least 3 of 5 criteria met with no critical failures on signal transmission and recognition) shall be documented as a conditional pass with corrective actions required before the control is considered validated.

### 4.5 Evidence to capture

- Exercise record (EXR-nnn) per `schemas/exercise-record.schema.json`
- Facilitator observation notes (timestamped)
- Scenario description
- Pass/fail against each criterion
- Debrief notes including operator self-assessment

### 4.6 Failure response

If acceptance criteria are not met:

1. Document findings in exercise record; mark `acceptance_criteria_met: false`
2. Identify root cause: training gap, protocol design flaw, or scenario design issue
3. If root cause is protocol design: open a corrective action against the duress protocol template; treat the duress control as non-functional until re-exercised
4. Reschedule corrective exercise within 60 days
5. Notify safety/security lead

---

## 5 — ET-2: Social engineering red team

### 5.1 Description and objective

A social-engineering red-team exercise presents operators with realistic attempts to manipulate them into taking unauthorized actions, disclosing sensitive information, or bypassing OADC constraints. The objective is to verify that operators apply skeptical decision-making, identity verification, and the challenge-and-response protocol defined in `docs/adversarial/`.

Scenarios may include: impersonation of legitimate authority, urgency framing designed to suppress review, false OADC override claims, and staged communications channel compromises.

### 5.2 Minimum cadence

Semi-annually. Scenarios should vary between runs; operators should not know the specific scenario in advance.

### 5.3 Required participants

- One or more operators under evaluation (should not know the exercise is in progress)
- Red team (may be internal or external; must be briefed on OADC constraints and social engineering vectors)
- Exercise facilitator and safety observer (ensures no real system impact)
- Safety/security lead review post-exercise

### 5.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| Operator applies identity verification before acting on instruction from unverified authority | Pass for ≥ 90% of scenarios presented |
| Operator does not take irreversible action on single unverified instruction under time pressure | Pass for 100% of high-consequence scenarios |
| Operator logs or reports suspicious contact | Pass for ≥ 80% of scenarios presented |
| Operator correctly invokes challenge-and-response protocol when warranted | Pass for ≥ 80% of applicable scenarios |

A critical failure (irreversible high-consequence action taken on unverified instruction) requires immediate corrective action and re-exercise within 30 days.

### 5.5 Evidence to capture

- Exercise record (EXR-nnn)
- Red team scenario scripts (retained confidentially by facilitator)
- Per-scenario pass/fail assessment
- Operator debrief summary
- Red team findings report

### 5.6 Failure response

If acceptance criteria are not met:

1. Document in exercise record; mark `acceptance_criteria_met: false`
2. Conduct individual coaching for operators who failed critical scenarios
3. If systemic failure (>50% of participants fail the same scenario type): escalate to safety/security lead and review social engineering training material
4. Re-exercise within 30 days (targeted, focused on failure scenarios)

---

## 6 — ET-3: OADC threshold validation

### 6.1 Description and objective

An OADC threshold-validation exercise walks operators through each parameter in the active OADC instance for their environment, verifying that parameter values are operationally correct, that operators can correctly identify when a threshold is crossed, and that the authority response is executable as defined. This exercise is part design review, part operator familiarization.

The objective is to catch parameter errors (unrealistic thresholds, missing conditions), operator unfamiliarity with constraints, and gaps between the documented OADC and the technical enforcement layer.

### 6.2 Minimum cadence

At program start (before operational use of any OADC instance). Re-exercise after any change to a canonical OADC instance in `data/registers/oadc-register.yaml`. Any change to an OADC definition is a safety-critical change per the repository policy and requires this exercise as part of the change validation.

### 6.3 Required participants

- All operators governed by the OADC instance under review
- Safety/security lead or designee
- System administrator (where OADC has a technical enforcement layer)
- Exercise facilitator

### 6.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| All OADC parameters reviewed against operational context | 100% of parameters covered |
| No parameter identified as operationally incorrect or infeasible | Zero open parameter disputes after review |
| Operators can correctly identify the authority response for each condition | ≥ 80% of operators score 100% on verbal scenario check |
| Technical enforcement layer matches documented OADC constraints | Zero discrepancies between document and system behavior |
| OADC instance updated if any parameter change required | Completed before sign-off |

### 6.5 Evidence to capture

- Exercise record (EXR-nnn)
- Per-parameter review table (condition, parameter value, operational correctness assessment)
- Operator scenario-check results
- Technical enforcement verification log
- List of any parameter changes made as a result

### 6.6 Failure response

If acceptance criteria are not met:

1. Document in exercise record; mark `acceptance_criteria_met: false`
2. Suspend operational use of the OADC instance for high-consequence environments until the exercise is passed
3. Correct parameter errors; re-exercise the specific failed items within 14 days
4. Notify safety/security lead of any parameter change made

---

## 7 — ET-4: Epistemic check drill

### 7.1 Description and objective

An epistemic check drill presents operators with a realistic decision scenario and requires them to complete a full pre-decision epistemic check: identify assumptions (tagged [F], [I], [S]), constraints, unknowns, and confidence level. The objective is to verify that operators apply the epistemic model from `docs/epistemics/belief-provenance.md` correctly under time pressure.

Scenarios shall include at least one case where stated confidence is below 70% (requiring the operator to identify what checks would raise it) and at least one case involving a single-source claim.

### 7.2 Minimum cadence

Quarterly.

### 7.3 Required participants

- All operators subject to the epistemic check requirement
- Exercise facilitator
- At least one assessor familiar with the belief-provenance model

### 7.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| Operator correctly tags all stated claims as [F], [I], or [S] | ≥ 80% of claims tagged correctly |
| Operator correctly applies confidence gating when confidence < 70% | 100% of applicable scenarios |
| Operator identifies at least one check to raise confidence when below threshold | 100% of sub-70% scenarios |
| Operator limits to safe, reversible partial action when confidence < 70% | 100% of applicable scenarios |
| Decision log is complete and internally consistent | Assessed by facilitator: pass/fail |

### 7.5 Evidence to capture

- Exercise record (EXR-nnn)
- Completed decision log from exercise scenario
- Assessor evaluation notes per criterion
- Any debrief findings on systematic tagging errors

### 7.6 Failure response

If acceptance criteria are not met:

1. Document in exercise record; mark `acceptance_criteria_met: false`
2. Identify specific failure pattern: incorrect tagging, failure to gate on confidence, or incomplete log
3. Provide targeted refresher on the belief-provenance model
4. Re-exercise within 30 days; targeted on failed scenario types
5. If systemic failure across multiple operators: review decision log training and accessibility of template

---

## 8 — ET-5: Decision-tree walkthrough

### 8.1 Description and objective

A decision-tree walkthrough exercises the pre-committed decision trees defined for time-pressured scenarios in the operator's environment. Operators are presented with a scenario that triggers a decision tree and must walk through it within the specified time constraint. The objective is to verify that the tree covers the scenario, that operators can navigate it under pressure, and that the outcome is operationally correct.

### 8.2 Minimum cadence

Annually. Re-exercise after any update to a pre-committed decision tree.

### 8.3 Required participants

- All operators who may execute the decision tree in operational conditions
- Exercise facilitator with stopwatch (time pressure is a required element)
- At least one subject matter expert who can assess correctness of tree navigation

### 8.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| Operator reaches correct terminal node for each scenario | 100% of scenarios |
| Operator completes tree within time pressure constraint | ≥ 80% of operators within specified time |
| No ambiguity or dead-end encountered in tree navigation | Zero unresolved ambiguities (tree design defect, not operator error) |
| Operator can identify the authority constraint applying to each terminal node | ≥ 80% of operators |

Tree design defects identified during the exercise shall be corrective actions against the decision tree document, not scored as operator failures.

### 8.5 Evidence to capture

- Exercise record (EXR-nnn)
- Per-scenario navigation log (nodes traversed, time taken)
- List of any tree design issues identified
- Facilitator assessment per criterion

### 8.6 Failure response

If acceptance criteria are not met:

1. Document in exercise record; mark `acceptance_criteria_met: false`
2. Distinguish operator errors from tree design defects
3. If tree design defect: open corrective action; update tree; re-exercise after update
4. If operator error: provide targeted practice; re-exercise within 60 days
5. Treat the affected decision tree as non-operational under time pressure until re-exercised

---

## 9 — ET-6: Team state sync

### 9.1 Description and objective

A team state sync exercise tests the team's ability to maintain a shared operating picture, detect information asymmetry, and apply the challenge-and-response protocol. Operators are placed in a scenario where they receive deliberately inconsistent information, and the team must identify and resolve the inconsistency without groupthink or authority diffusion.

The objective is to validate the team-level governance defined in `docs/cross-cutting/` and the team mode-state concept from `docs/resilience/h-state-table.md`.

### 9.2 Minimum cadence

Semi-annually.

### 9.3 Required participants

- Full operational team (or representative cross-section)
- Exercise facilitator (injects information asymmetry via briefing isolation)
- Observer tracking individual and team behavior

### 9.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| Team identifies the injected information asymmetry without facilitator prompt | Within scenario window |
| At least one team member invokes challenge-and-response protocol | Pass/fail |
| No groupthink outcome (team reaches consensus based on incorrect shared assumption) | Pass/fail |
| Authority diffusion does not occur (a decision owner is clearly identified for all consequential actions) | Pass/fail |
| Information asymmetry is resolved by cross-validation, not by deferring to seniority alone | Pass/fail |

### 9.5 Evidence to capture

- Exercise record (EXR-nnn)
- Observer notes (timestamped)
- Scenario design document (retained by facilitator)
- Team debrief summary
- Pass/fail per criterion with rationale

### 9.6 Failure response

If acceptance criteria are not met:

1. Document in exercise record; mark `acceptance_criteria_met: false`
2. Identify which failure mode occurred (groupthink, asymmetry not detected, authority diffusion)
3. Conduct team debrief; reinforce challenge-and-response protocol norms
4. If pattern of groupthink or authority diffusion: escalate to safety/security lead for team dynamics review
5. Re-exercise within 60 days

---

## 10 — ET-7: Safe state test

### 10.1 Description and objective

A safe-state test exercises the full safe-state transition: triggering the transition, verifying that all defined system actions execute correctly, verifying that prohibited actions are halted, verifying that monitoring continues, and verifying that the exit procedure requires appropriate authorization. The objective is to validate `docs/cross-cutting/safe-state.md` and the associated per-environment safe-state specification.

Safe-state tests shall be conducted in a non-production environment unless the production safe state can be triggered without operational impact (e.g., a passive-mode state). The test must be as representative of the actual transition as operationally feasible.

### 10.2 Minimum cadence

At program start (before operational use of any system governed by an OADC). Re-exercise after any change to the safe-state specification for an environment. Safe-state changes are safety-critical changes per the repository policy.

### 10.3 Required participants

- Safety/security lead or designee
- System administrator (production equivalent environment)
- At least one operator who would authorize exit from safe state in operational conditions
- Exercise facilitator

### 10.4 Acceptance criteria

| Criterion | Threshold |
|-----------|-----------|
| Safe-state transition triggers correctly from each defined trigger condition | 100% of trigger types tested |
| All defined "system stops doing" actions halt within the specified timeout | 100% |
| All defined "system continues doing" monitoring actions remain active | 100% |
| Unauthorized exit attempt is rejected | 100% of test cases |
| Authorized exit requires correct credentials and approval | 100% of test cases |
| Evidence capture during safe state is confirmed | Pass/fail |

### 10.5 Evidence to capture

- Exercise record (EXR-nnn)
- Per-trigger test log (trigger presented, actual behavior, expected behavior, pass/fail)
- Exit authorization test log
- Monitoring continuity confirmation
- Any discrepancy between documented safe-state specification and observed behavior

### 10.6 Failure response

If acceptance criteria are not met:

1. Document in exercise record; mark `acceptance_criteria_met: false`
2. Treat the environment as not cleared for operational use until the safe-state test passes
3. Identify whether the failure is a specification error or a system configuration error
4. Correct the defect; re-exercise within 14 days
5. Notify safety/security lead; document as a pre-operational finding

---

## 11 — Initial exercise sequence

When standing up the exercise program for the first time, execute exercises in the following order. This sequence ensures that foundational controls are validated before dependent controls.

| Step | Exercise type | Rationale |
|------|---------------|-----------|
| 1 | `oadc-threshold-validation` (ET-3) | Validate that OADC parameters are correct before any other exercise depends on them |
| 2 | `safe-state-test` (ET-7) | Validate safe-state transition before operating with a live OADC; required before operational use |
| 3 | `epistemic-check-drill` (ET-4) | Establish baseline epistemic discipline; required for all subsequent scenario-based exercises |
| 4 | `decision-tree-walkthrough` (ET-5) | Validate pre-committed decision trees before they are relied upon in drills or operations |
| 5 | `duress-drill` (ET-1) | Exercise duress protocol now that basic operator competencies are confirmed |
| 6 | `team-state-sync` (ET-6) | Exercise team-level controls after individual controls are confirmed |
| 7 | `social-engineering-red-team` (ET-2) | Conduct red team after operators have practiced foundational protocols |

All seven exercises must be completed before the program is considered active. The program start date is the date the final initial exercise record is signed.

---

## 12 — Post-exercise review requirements

Every exercise produces an exercise record (EXR-nnn). Beyond the record, the following review requirements apply:

1. **Immediate debrief:** Conducted on the same day as the exercise. Cover what happened, what the acceptance criteria outcome was, and immediate observations. Do not allow cooling-off to obscure real-time findings.

2. **Corrective action tracking:** All corrective actions identified during the exercise shall be entered into the exercise record and assigned owners and due dates. Actions not resolved before the next exercise of the same type shall be reviewed during that exercise.

3. **Policy or protocol defect escalation:** If a finding identifies a defect in a governance document (OADC, duress protocol, safe-state specification, decision tree), open a corrective action against that document through the standard change process. Safety-critical changes require two-person review per the repository policy.

4. **Program-level review:** The aggregate of all exercise records is reviewed at least annually (or following any safety-critical event) by the safety/security lead to identify trends, systemic gaps, and cadence compliance status.

5. **Cadence compliance reporting:** The exercise facilitator or program manager maintains a cadence tracking log. Any control that has not been exercised within its cadence shall be flagged as assumed non-functional per Policy Statement 10 and reported in the program-level review.

---

## 13 — Cadence summary table

| Exercise type | Minimum cadence | Trigger conditions | Overdue threshold |
|---------------|-----------------|-------------------|-------------------|
| `duress-drill` | Annually | Annual calendar | > 12 months since last pass |
| `social-engineering-red-team` | Semi-annually | Semi-annual calendar | > 6 months since last pass |
| `oadc-threshold-validation` | Program start + OADC change | Program initialization; any commit to `data/registers/oadc-register.yaml` | Not completed within 30 days of OADC change |
| `epistemic-check-drill` | Quarterly | Quarterly calendar | > 3 months since last pass |
| `decision-tree-walkthrough` | Annually | Annual calendar; decision tree update | > 12 months since last pass, or tree updated without re-exercise |
| `team-state-sync` | Semi-annually | Semi-annual calendar | > 6 months since last pass |
| `safe-state-test` | Program start + safe-state change | Program initialization; any safe-state specification change | Not completed within 30 days of safe-state change |

---

## 14 — Confidence notes

- Exercise acceptance criteria are a governance baseline, not a performance benchmark [I,75]. Environments with higher consequence profiles should raise thresholds.
- The initial sequence ordering reflects logical dependency; empirical validation of the sequence is pending field use [S,65].
- Cadence values are minimum bounds derived from practice in analogous programs (aviation CRM, nuclear operator qualification, red team cadences) [I,70]; adjust based on threat profile and operational tempo.
