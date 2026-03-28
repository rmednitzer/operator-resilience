# Autonomous System Bridge

**Date:** 2026-03-28
**Scope:** Formal interface definition between operator-resilience governance and platform-side authority governance. Maps OADC state to authority permission sets, H-state to system operating modes, and epistemic state to connectivity state. These mappings are deployment-specific and defined per OADC instance.
**Status:** DRAFT
**Referenced by:** `docs/contracts/oadc.md`; `docs/resilience/h-state-table.md`; `docs/epistemics/belief-provenance.md`; `docs/integration/stpa-uca.md`; `artifact-index.yaml`
**Companion repository:** [autonomous-platform-assurance](https://github.com/rmednitzer/autonomous-platform-assurance) (authority levels AL-0 to AL-8)

---

## 1 — Purpose

Operator-resilience governance (this repository) and platform authority governance (autonomous-platform-assurance) are maintained separately. Neither side hard-codes the other. The autonomous system bridge is the formal interface that maps the two.

Without the bridge, a platform that degrades an operator to H-2 does not know what that means for its own operating mode. An OADC condition that restricts operator authority does not automatically translate to a restriction on what the platform will execute. The bridge makes those translations explicit and pre-committed.

**What the bridge does:**

1. Maps OADC operator authority state → platform authority permission set (what the platform may execute)
2. Maps operator H-state → platform system operating mode (how the platform behaves given the operator's assessed capacity)
3. Maps operator epistemic state → platform connectivity state (whether the platform treats the operator as "connected" — with adequate situational awareness — or not)

**What the bridge does not do:**

- It does not prescribe how the platform enforces these mappings; enforcement is governed by autonomous-platform-assurance.
- It does not replace per-environment OADC instances; the bridge provides the mapping structure, which is then populated per deployment.
- It does not govern the platform's own degraded-mode hierarchy independently of the operator; platform-only failures are addressed in autonomous-platform-assurance.

---

## 2 — The three mappings

### 2.1 — Mapping A: OADC state → authority permission set

When OADC conditions narrow operator authority, the platform must understand which operations are restricted. The authority permission set is the platform-side representation of operator authority: it specifies which platform operations the operator is authorized to initiate, confirm, or veto, given the current OADC conditions.

The mapping is one-directional: OADC conditions constrain the permission set; the permission set never expands beyond what the OADC allows. The platform may have additional constraints that further restrict the permission set, but it shall not grant permissions the OADC has withdrawn.

**Indicative mapping table (populated per OADC instance):**

| OADC condition (from `docs/contracts/oadc.md` §2) | Authority permission set | Notes |
|---|---|---|
| No active OADC condition (H-0, all thresholds nominal) | Full authority: operator may initiate, confirm, or veto any authorized platform action | Baseline state |
| Single information source for key claim | Can confirm but cannot initiate high-consequence actions on single-source basis | Requires second independent source before high-consequence initiation |
| On-call duration > N hours (H-1 range) | Full authority for standard actions; second-person required for irreversible high-consequence actions | Buddy-pair must be confirmed before irreversible action proceeds |
| Buddy-pair required condition active | No solo irreversible actions; all high-consequence actions require co-authorization | Platform gate: co-authorization token from second operator required |
| H-2 (extended duration, two or more degradation conditions) | Monitoring and advisory only; no unilateral initiation of new actions; all actions require supervisor confirmation | Platform should present advisory mode to operator; all action requests queued for supervisor |
| H-3 or H-4, alternate available | Authority transferred to alternate; operator has no platform authority until return-to-duty confirmed | Platform revokes operator session authority; alternate's session becomes authoritative |
| H-3/H-4 or any authority transfer, no alternate | Operator-absent safe state; no operator platform authority | Platform transitions to safe state per `docs/cross-cutting/safe-state.md` |
| Contested environment declared | Two-person rule for all consequential actions; no single-operator high-consequence authority | Platform gate: all consequential actions require dual authorization |
| Duress event: authority containment invoked | Operator authority contained; platform executes authority transfer to confirmed-clear alternate | Platform receives containment signal; operator's ability to issue consequential commands suspended |
| Extended passive monitoring > `passive_monitoring_interval` | State-check required before any intervention; no new actions until state-check passed | Platform prompts state-check; blocks new action initiation until check confirmed |

### 2.2 — Mapping B: H-state → system operating mode

The platform's operating mode should reflect the operator's assessed H-state. This mapping specifies how the platform's autonomous behaviors, confirmation requirements, and action authorities change as the operator's capacity changes.

This is not simply a matter of what the operator requests. The platform shall operate in the mode appropriate to the operator's assessed H-state — even if the operator requests a more capable mode — because an operator at H-2 is not in a state to reliably self-assess their capacity to supervise the more capable mode.

**Indicative mapping table (populated per OADC instance):**

| Operator H-state | Platform system operating mode | Platform behavior |
|---|---|---|
| H-0 (full capacity) | **Full operation** | Platform executes all authorized actions as directed; operator has full authority within OADC permission set |
| H-1 (mild degradation: fatigue advisory, minor performance indicators) | **Full operation + advisory** | Platform provides additional confirmation prompts for high-consequence actions; logs H-1 advisory in audit trail; no restriction on authority |
| H-2 (moderate degradation: sustained duty > N, multiple conditions, two or more OADC conditions) | **Supervised operation** | All autonomous actions require explicit per-action operator confirmation; platform does not proceed on prior authorization; novel actions queued for supervisor endorsement |
| H-3 (severe degradation: mandatory handoff condition) | **Autonomous hold** | Platform holds current state; suspends all new mission or action initiation; continues existing committed actions only if pre-authorized as safe-to-complete; awaits confirmed alternate or safe-state transition |
| H-4 (incapacitated) or no qualified alternate | **Operator-absent safe state** | Platform enters safe state per `docs/cross-cutting/safe-state.md`; no new operator-directed actions until return-to-duty and authority restoration confirmed |

> **Transition direction:** H-state degradation transitions (H-0 → H-4) take effect immediately upon assessment. H-state upgrade transitions (H-4 → H-0) take effect only after return-to-duty protocol is complete and the H-state upgrade declaration has been issued per `docs/cross-cutting/return-to-duty.md` §3 Step 2c.

### 2.3 — Mapping C: Epistemic state → connectivity state

The epistemic state mapping addresses a specific failure mode: an operator who is nominally on duty (H-0, no OADC conditions triggered) but whose situational awareness of the current system state is below the threshold needed to make safe decisions. This is the out-of-the-loop (OOTL) problem.

The connectivity state captures whether the operator is meaningfully "connected" — has adequate situational awareness — or "disconnected" — has insufficient situational awareness to safely authorize novel actions.

**Connectivity states:**

| Connectivity state | Definition | Platform behavior |
|---|---|---|
| **Connected** | Operator's epistemic confidence in current system state ≥ 70%; state-check passed within `passive_monitoring_interval`; no single-source constraints on key state claims | Platform proceeds with authorized actions; operator authority at current OADC permission level |
| **State-check required** | Operator's epistemic confidence in current system state < 70% on one or more key claims; or `passive_monitoring_interval` exceeded since last active engagement; or single-source constraint active | Platform prompts state-check before proceeding with any novel action; existing committed actions may continue if safe to do so; new actions blocked until state-check completed and confidence ≥ 70% confirmed |
| **Disconnected (safe state)** | State-check failed: operator cannot confirm current system state to ≥ 70% confidence; or OOTL condition confirmed and no alternate available; or operator confirmed in extended OOTL | Platform treats operator as effectively absent; transitions to supervised operation (if a supervisor is available to confirm actions) or autonomous hold; if no qualified authority available, safe state per §2.2 H-4 row |

**Epistemic confidence threshold:** The 70% threshold is the standard from `docs/epistemics/belief-provenance.md` and `docs/contracts/oadc.md`. Below 70%: state checks are required; safe, reversible partial actions only. This is the same threshold applied to operator decision-making; the bridge applies it to platform behavior.

**State-check mechanism:** The state-check is a structured operator-platform interaction in which the operator demonstrates active situational awareness. The mechanism is deployment-specific; the bridge requires that:
- The check is not dismissible without positive engagement
- The check result is logged in the audit trail with timestamp
- A failed check is treated as the "disconnected" state, not as a conditional pass

---

## 3 — Mapping tables: implementation guidance

### 3.1 — Deployment-specific population

The mapping tables in §2 are indicative. Each deployment must populate them specifically for its operating environment, OADC instance, and platform capability set. The deployment-specific mapping is an annex to the OADC instance for that environment (referenced in `data/registers/oadc-register.yaml`).

When populating the mapping tables, the following must be specified explicitly:
- Which OADC conditions are detectable by the platform (vs. requiring human assessment input)
- What the platform-side mechanism is for each permission restriction (technical gate, logged advisory, or procedural compensating control)
- What authorization is required to transition out of each restricted mode
- How conflicting signals are resolved (e.g., H-state assessed at H-2 but no OADC threshold triggered formally)

### 3.2 — Platform enforcement

How the platform enforces these mappings is governed by autonomous-platform-assurance (see §5). The bridge specifies what must be enforced; autonomous-platform-assurance specifies how. A platform that cannot technically enforce a mapping must document that as a compensating control gap, with procedural compensating controls subject to exercise validation.

### 3.3 — Change management

The mapping tables must be reviewed and re-validated whenever:
- The OADC instance for the operating environment changes (any parameter modification)
- The platform authority hierarchy in autonomous-platform-assurance changes
- An exercise or post-event review identifies a mapping failure (actual or simulated)

Changes to mapping tables that affect authority permissions or system modes are safety-critical changes. They require the process defined in `CONTRIBUTING.md` §Safety-critical changes and the review requirements for OADC modifications.

### 3.4 — Audit logging

All mode transitions driven by OADC-to-platform mapping events shall be logged in the platform audit trail:
- Trigger event (OADC condition, H-state assessment, epistemic state change)
- Mode transition: from → to
- Timestamp (UTC)
- Authorization source (human assessment, automated detection, supervisor confirmation)

These log entries constitute OADC trigger event records for the purposes of Policy Statement 8 and post-event review triggers.

---

## 4 — Authority level cross-reference

The autonomous-platform-assurance companion repository defines platform authority levels AL-0 through AL-8. The bridge maps between operator H-state and OADC conditions (this repository's constructs) and platform authority levels (companion repository's constructs).

**Indicative cross-reference (deployment-specific alignment required):**

| Operator state | This repository | Companion repo authority level (indicative) |
|---|---|---|
| H-0, no OADC conditions | Full authority | AL-0 to AL-2 (full operator authority range) |
| H-1 / advisory conditions | Full authority + advisory mode | AL-2 to AL-3 |
| H-2 / supervised operation | Supervised; no solo irreversible | AL-4 to AL-5 |
| H-3 / autonomous hold | No new initiation | AL-6 |
| H-4 or absent / safe state | Operator-absent | AL-7 to AL-8 (autonomous safe state) |

> These cross-references are indicative inferences `[I,65]`; the actual AL mapping depends on the companion repository's current authority level definitions. Deployments must establish alignment explicitly by reviewing both repositories and documenting the agreed mapping.

---

## 5 — Cross-reference: companion repository

The autonomous-platform-assurance repository governs:
- Platform authority level definitions (AL-0 to AL-8) and transition conditions
- Platform-side enforcement mechanisms for authority restrictions
- Platform self-assessment and health monitoring
- Autonomous safe-state entry and exit procedures at the platform level

The operator-resilience bridge mappings (§2) are the interface contract. Neither repository governs the other unilaterally; changes affecting the interface require coordinated review of both sides.

Repository: [autonomous-platform-assurance](https://github.com/rmednitzer/autonomous-platform-assurance)

---

## Confidence notes

- The three-mapping structure is a design inference `[I,75]`; its adequacy for a given operating environment requires validation via UCA analysis (`docs/integration/stpa-uca.md`) and exercise.
- The AL cross-reference in §4 is indicative `[I,65]`; the companion repository definitions are authoritative for the AL-side of the mapping.
- Epistemic state as a platform-observable condition requires platform-side sensing or structured operator input; the assumption that this is technically feasible is `[S,70]` and must be confirmed per deployment.
