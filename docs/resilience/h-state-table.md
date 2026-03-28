# H-State Table: Human Mode-State Hierarchy

**Date:** 2026-03-28
**Scope:** Formal definition of the H-state hierarchy (H-0 to H-4): taxonomy, observable indicators, decision authority limits, support requirements, assessment methods, detection heuristics, handoff triggers, and team mode-state.
**Status:** DRAFT
**Referenced by:** README.md; POL-OR-01 statement 7; `docs/contracts/oadc.md` §2 (self-reported degradation, circadian, epistemic markers); `docs/epistemics/belief-provenance.md` §8, §10

---

## 1 — Purpose

The H-state hierarchy is the formal, pre-committed classification of operator cognitive capacity. It serves the same architectural function for the human operator that a degraded-mode hierarchy serves for a technical system: it defines named states, the transitions between them, and the authority constraints and support obligations that apply at each state.

The H-state is not a performance assessment or a disciplinary classification. It is a governance instrument. Its purpose is to ensure that operator authority is calibrated to actual capacity — before a consequential decision, not after an adverse outcome.

---

## 2 — H-state hierarchy overview

H-states range from H-0 (full cognitive capacity) to H-4 (incapacitated). The hierarchy is analogous to a system degraded-mode hierarchy, where each descending state represents reduced capability, narrowed authority, and increased external support requirements.

```
H-0  Full capacity          ──┐
H-1  Mildly degraded          │  Operational — reduced authority
H-2  Moderately degraded      │  Operational with mandatory support
H-3  Severely degraded      ──┤  Non-operational — mandatory handoff
H-4  Incapacitated          ──┘  Non-operational — mandatory handoff; safe state if no alternate
```

**Key structural properties:**

1. H-states are discrete, not continuous. The taxonomy forces explicit classification rather than a gradual slide that conceals degradation.
2. Transitions are governed by observable indicators, not by operator self-assessment alone.
3. Authority narrows monotonically from H-0 to H-4. It does not expand during an incident without returning to H-0 via recovery criteria.
4. The hierarchy applies to individual operators. Team mode-state is a separate derived concept (§9).

---

## 3 — Full H-state taxonomy

### H-0 — Full Capacity

| Attribute | Definition |
|-----------|------------|
| **Name** | Full Capacity |
| **Description** | Operator is rested, alert, informed, and operating within normal OADC parameters. No active degradation condition applies. |
| **Observable indicators** | Appropriate response latency; coherent verbal output; self-consistent decision log; no errors in routine checks; peer assessment: no concerns; meets return-to-duty criteria if returning from H-2+. |
| **Decision authority limits** | Full authority per OADC role definition. Standard logging and second-person rules apply for high-consequence actions as defined in the active OADC instance. |
| **Required support measures** | None beyond standard operational procedures. |
| **Recovery criteria** | N/A — this is the baseline. |

---

### H-1 — Mildly Degraded

| Attribute | Definition |
|-----------|------------|
| **Name** | Mildly Degraded |
| **Description** | Operator is experiencing minor cognitive or physical degradation. Performance is within operational bounds for routine tasks but reduced for complex, novel, or high-tempo decisions. |
| **Observable indicators** | Increased response latency; slightly reduced precision in verbal or written outputs; self-reported: mild fatigue, early hunger, minor distraction, beginning of circadian trough; peer: noticeable but not alarming change from baseline; minor anomaly in decision log review (e.g., omitted field, imprecise formulation). |
| **Decision authority limits** | Full authority for routine actions. For high-consequence or irreversible actions: second-person review recommended; log confidence explicitly. Novel authority (actions not covered by pre-committed decision trees) subject to supervisor awareness. |
| **Required support measures** | Peer awareness; scheduled rest or handoff if H-1 condition is expected to persist > N hours (per active OADC instance). |
| **Recovery criteria** | Adequate rest (per OADC rest minimum); food/hydration if physiologically indicated; re-engagement with environment; self-declaration or peer confirmation. No formal return-to-duty protocol required for H-1 → H-0. |

---

### H-2 — Moderately Degraded

| Attribute | Definition |
|-----------|------------|
| **Name** | Moderately Degraded |
| **Description** | Operator capacity is materially impaired. Complex and novel decision-making is unreliable. Routine task execution may be intact but comprehension and projection (SA Levels 2–3) are degraded. Operator may not be the reliable judge of their own state. |
| **Observable indicators** | Noticeably increased error rate; delayed or incomplete responses to queries; difficulty recalling recent events; confirmation-seeking behavior; self-reported: significant fatigue, emotional distress, pain, or medication effect; failure of OOTL state-check; peer: clear performance decline, slurred speech, disorientation, fixation, or uncharacteristic affect; automated: missed watchdog checks, anomalous input patterns. |
| **Decision authority limits** | Narrowed authority: all high-consequence or irreversible decisions require second-person approval. Pre-committed decision trees only for time-pressured scenarios. Novel authority suspended. Operator shall not act as the sole second-person reviewer for another operator. |
| **Required support measures** | Active peer engagement; second-person approval for all consequential actions; supervisor notification; handoff planning initiated (not yet mandatory, but must be in progress); rest or medical assessment if physiologically indicated. |
| **Recovery criteria** | Minimum rest period per OADC instance; structured return-to-duty check (peer or supervisor assessment using return-to-duty template); re-establishment of OOTL state-check if applicable; explicit H-state upgrade declaration by assessor. |

---

### H-3 — Severely Degraded

| Attribute | Definition |
|-----------|------------|
| **Name** | Severely Degraded |
| **Description** | Operator cannot safely exercise consequential authority. Decision-making capacity is unreliable even for routine tasks. Operator is a risk factor, not a control. Mandatory handoff applies. |
| **Observable indicators** | Persistent errors in routine tasks; incoherent or inconsistent verbal output; significant disorientation or memory gaps; apparent inability to track system state; emotional dysregulation; self-reported: severe distress, inability to concentrate, inability to continue; peer: clear functional impairment — cannot complete checklist, cannot recall recent state, repeated misreads; automated: multiple consecutive anomalous actions or missed critical checks. |
| **Decision authority limits** | No independent authority. Operator shall not authorize any action. Handoff is mandatory. Operator may assist in information transfer to incoming operator but shall not be the decision-maker. |
| **Required support measures** | Immediate handoff to qualified alternate; supervisor notification; if no alternate available, system enters pre-defined safe state. Medical or welfare assessment depending on cause. Incident log entry mandatory with timestamp and initiating observations. |
| **Recovery criteria** | Structured return-to-duty protocol (full, not abbreviated); minimum rest and recovery period per OADC instance; supervisor sign-off required; H-state upgrade to H-1 or H-0 requires documented assessment — cannot self-report out of H-3. |

---

### H-4 — Incapacitated

| Attribute | Definition |
|-----------|------------|
| **Name** | Incapacitated |
| **Description** | Operator is unable to function. Incapacitation may be physical (injury, medical emergency, collapse), cognitive (acute crisis, severe impairment), or operational (duress — operator is present but acting under coercion). In duress cases, H-4 classification may not be externally visible; see `docs/adversarial/` for duress protocols. |
| **Observable indicators** | Operator unresponsive or unable to communicate; physically incapacitated; explicit duress signal received; missed critical response with no explanation; automated: no response to watchdog within defined interval. |
| **Decision authority limits** | No authority. Operator is not in the decision chain. |
| **Required support measures** | Immediate safe-state invocation if no qualified alternate is available; emergency services if medical cause; duress response protocol if coercion is indicated; supervisor or incident commander assumes authority transfer. All actions taken under H-4 conditions are logged as extraordinary authority events. |
| **Recovery criteria** | Full return-to-duty protocol; medical or security clearance as appropriate to cause; minimum H-0 assessment by two independent reviewers before return to consequential authority. Duress-origin H-4 requires security debrief before return. |

---

## 4 — H-state assessment methods

H-state assessment uses four methods. No single method is authoritative; convergent evidence from multiple methods increases classification reliability.

| Method | Description | When it applies | Limitations |
|--------|-------------|-----------------|-------------|
| **Self-report** | Operator declares their own H-state at shift start, during handoff, or upon awareness of degradation. | Always required as a baseline; mandatory at shift start and after any OADC trigger event. | Self-reporting is unreliable at H-2 and above — impaired operators systematically underreport degradation. Self-report is necessary but not sufficient above H-1. |
| **Peer observation** | A second operator or supervisor observes performance, communication, and behavior and compares against individual baseline and observable indicators. | Active operations; handoff check; any time an indicator is observed. A challenge from a peer must be logged and cannot be dismissed without documented rationale. | Requires trained assessors; social pressure may suppress challenge; effective only when observers are not also degraded. |
| **Supervisor assessment** | Formal assessment by a supervisor or team lead, typically in response to a peer challenge or after an OADC trigger event. | H-2 suspected; H-3 confirmation; return-to-duty from H-3 or H-4; after significant OADC trigger events. | Supervisor availability may be limited during high-tempo incidents; supervisors may have authority relationships that create assessment bias. |
| **Automated detection** | System-level monitoring of operator interaction patterns, response latency, watchdog compliance, or state-check results. | Where technically implemented in the operating platform. | Covers behavioral indicators only; cannot detect cognitive-state indicators not expressed in system interaction; false positives and negatives must be calibrated per environment. |

### 4.1 — Assessment conflict resolution

When assessment methods conflict (e.g., self-report = H-0, peer observation = H-2 indicators), apply the **most conservative classification**. The operator shall not override a peer or supervisor H-state classification by self-report alone. Disagreements shall be escalated to supervisor and logged.

---

## 5 — Proactive vs. reactive detection

| Detection mode | Description | Objective |
|----------------|-------------|-----------|
| **Proactive** | Scheduled H-state checks at defined intervals (shift start, handoff, circadian window entry, post-N-hours); OADC-condition monitoring (duty clock, passive monitoring clock); regular peer observation during operations. | Detect degradation before it is expressed in consequential decisions. |
| **Reactive** | H-state assessment triggered by observed anomaly, missed check, performance failure, OADC condition trigger, or explicit challenge. | Contain the impact of degradation already expressed. |

**Preferred regime:** Proactive detection dominates. Reactive detection is a fallback, not the primary mechanism. An organization that relies primarily on reactive detection has a degraded safety posture.

Proactive check cadence is set per active OADC instance based on operating context (e.g., on-call SRE: check at shift start and every 4 hours during extended incident; OT control room: per shift-change protocol; autonomous platform GCS: before and after any extended OOTL monitoring period).

---

## 6 — "One H-state worse" heuristic

**Definition:** Under defined amplifying conditions, the effective H-state for authority-limiting purposes is treated as one level worse than the observed H-state. This accounts for known performance multipliers that are difficult to directly observe but are statistically established.

**Formal rule:**
- If an amplifying condition is active, treat the observed H-state as H-(n+1) for all authority-limiting purposes.
- **This heuristic does NOT elevate H-4 to a higher state.** H-4 is the ceiling; there is no H-5. The practical effect at H-4 is that the incapacitation classification is reinforced, not changed.

| Observed H-state | With amplifying condition | Effective H-state |
|------------------|--------------------------|-------------------|
| H-0 | Yes | H-1 |
| H-1 | Yes | H-2 |
| H-2 | Yes | H-3 |
| H-3 | Yes | H-4 |
| H-4 | Yes | H-4 (no escalation beyond incapacitated) |

**Defined amplifying conditions** (per `docs/contracts/oadc.md` §2):

- **Circadian low:** Operator is in the circadian performance trough (default window: 02:00–06:00 local time), or was woken from sleep within the last 30 minutes.
- **Extended incident duration:** Incident has exceeded the OADC `T` parameter (typically 4–8 hours) and operator has been continuously engaged.
- **Organizational stress condition active:** Declared by management or security.

Multiple simultaneous amplifying conditions do not stack beyond one increment (the rule is "+1", not "+N per condition"). If two amplifying conditions are active simultaneously, the effective H-state is still H-(n+1), not H-(n+2). However, the combination of conditions shall be noted in the H-state log and the recovery criteria shall require that both conditions resolve before H-state upgrade.

---

## 7 — Mandatory handoff trigger

**Rule:** H-3 or H-4 classification triggers mandatory handoff. This is a non-negotiable authority transfer, not a discretionary measure.

### 7.1 — Handoff sequence

1. H-3 or H-4 determined by any valid assessment method.
2. Supervisor or incident commander notified immediately.
3. Handoff to qualified alternate operator initiated — target: complete within the time defined by the active OADC instance.
4. Degraded operator provides information transfer only — no decision authority during handoff.
5. If handoff is complete: degraded operator is removed from decision chain; enters rest or medical assessment.
6. If no qualified alternate is available: system enters pre-defined operator-absent safe state. The safe state is invoked, not negotiated.

### 7.2 — No-alternate safe state

The operator-absent safe state shall be defined, documented, and tested for each operating environment before operational use. A safe state that has not been tested is not a safe state — it is an untested assumption.

The safe state definition is held in the operating environment's OADC instance (see `data/registers/oadc-register.yaml`).

### 7.3 — Authority during safe state

During operator-absent safe state, no individual operator has authority to escalate actions beyond the safe-state envelope without:
- Confirmed identity via two-factor authentication.
- Explicit break-glass authorization logged with rationale.
- Post-event review mandatory within 24 hours.

---

## 8 — CACE principle: Changing Anything Changes Everything

**Definition:** In a tightly coupled sociotechnical system, a change in one variable can propagate in non-obvious ways to affect others. For operator H-state management, CACE applies to H-state transitions.

**Application to H-state transitions:**

When an operator's H-state changes, the following downstream effects shall be explicitly assessed:

| What changes | Downstream effect to assess |
|---|---|
| Operator H-state degrades (H-0 → H-2+) | Does this affect the team's collective capacity? Does the remaining team now have single-person coverage for a role that requires two-person? Does the decision authority structure still function? |
| Operator H-state recovers (H-3 → H-0) | Is the returning operator current? Is OOTL state-check required? Does their re-entry change team dynamics or authority distribution? |
| Handoff occurs | Does the incoming operator understand the current epistemic picture? Are all active OADC conditions communicated? Has the trust boundary been re-assessed for the new operator's information intake? |
| Amplifying condition activates | All operators in the affected scope have their effective H-state incremented. Does this create a team-level H-state problem? |

**CACE requirement:** Before finalizing an H-state transition that narrows authority or triggers a handoff, the operator or supervisor shall verbally or textually affirm: "What else does this change?" The answer shall be logged.

---

## 9 — Team mode-state

A team's collective cognitive capacity is not simply the sum of individual H-states. Teams can degrade collectively in ways not visible in any single operator's H-state assessment.

**Team mode-state definition:** The team mode-state is the effective H-state of the team as a decision-making unit. It is derived from but not equal to the individual H-states.

| Condition | Team mode-state implication |
|---|---|
| Any member at H-3 or H-4 | Team operates one qualified member short; workload redistributed; team effective capacity increases toward team H-1 or H-2. |
| Majority of team at H-2 | Team mode-state is H-2 regardless of any H-0 individuals present; group comprehension failure risk is elevated. |
| All members at H-1 | Team mode-state is H-1; no compensating diversity; pre-committed decision trees mandatory for any high-consequence decision. |
| Collective stress event (e.g., extended incident, organizational crisis) | Treat team as one H-state worse than individual assessments (same amplifying condition logic as §6). |
| Information asymmetry within team | Not an H-state, but triggers epistemic degradation condition in OADC; pre-decision checks mandatory until symmetric. |

**Collective failure modes:** Teams are specifically vulnerable to groupthink (false consensus at H-2+), authority diffusion (no one believes they are the decision-maker), and information asymmetry (members operating on different epistemic pictures). These are not captured by individual H-state assessment; they require team-level observation.

---

## 10 — Stress-adapted decision aids

At H-2 and above, novel decision-making — reasoning through a problem type not previously encountered in training — is unreliable. Pre-committed decision trees address this by providing pre-reasoned decision paths that do not require working memory or novel inference under stress.

**Requirements for pre-committed decision aids:**

1. Decision trees shall be defined for all high-consequence decision types in the operating environment.
2. They shall be accessible without system access (printed or offline-capable).
3. They shall be validated with tabletop exercises at H-2 simulation before operational reliance.
4. At H-2 or above, operators shall use the pre-committed tree and shall not substitute novel reasoning unless the tree explicitly provides for an unseen-condition branch.
5. If no applicable tree exists for the situation, the operator shall treat this as a confidence < 70% condition: halt irreversible action; escalate; invoke safe state if necessary.

Reference: exercise program (`docs/exercise/`) for exercise types that validate decision aid effectiveness.

---

## 11 — Relationship to OADC conditions

| OADC condition | H-state interaction |
|---|---|
| **Self-reported degradation** | Operator declares H-1 or H-2. This triggers the corresponding authority constraints per §3. Self-report is the floor — peer or supervisor may classify higher. |
| **Epistemic degradation markers detected** | Consistent with H-2 indicators. Peer or supervisor shall assess H-state; do not allow operator to continue without assessment. |
| **Extended passive monitoring (OOTL)** | OOTL state-check failure maps to H-2 for authority purposes until active engagement re-established. See `docs/epistemics/belief-provenance.md` §8. |
| **Circadian low** | Amplifying condition; apply one-H-state-worse heuristic per §6. |
| **Organizational stress** | Amplifying condition; apply one-H-state-worse heuristic per §6. |
| **Incident duration > T hours** | Amplifying condition for all operators engaged throughout. Apply one-H-state-worse heuristic per §6. Mandatory buddy-pair per OADC §2 is concurrent, not a substitute for H-state management. |

---

## 12 — Summary matrix

| H-state | Name | Independent authority | Second-person required | Handoff | Safe state invoked | Recovery protocol |
|---------|------|----------------------|----------------------|---------|-------------------|-------------------|
| **H-0** | Full Capacity | Yes — full per OADC role | For high-consequence per OADC | No | No | N/A |
| **H-1** | Mildly Degraded | Yes — routine actions | Recommended for high-consequence; required per OADC instance | No (plan if persistent) | No | Self-declaration; peer confirmation |
| **H-2** | Moderately Degraded | No — all consequential require second-person | Yes — mandatory for all consequential actions | Plan in progress | No | Structured return-to-duty check; assessor sign-off |
| **H-3** | Severely Degraded | No | No independent authority | **Mandatory** | If no alternate available | Full return-to-duty protocol; supervisor sign-off |
| **H-4** | Incapacitated | No | No independent authority | **Mandatory** | If no alternate available | Full return-to-duty; medical/security clearance; two-reviewer sign-off |

### 12.1 — One-H-state-worse amplified matrix

Effective H-state when an amplifying condition (circadian low, extended incident, organizational stress) is active:

| Observed | Effective (amplified) | Effective name |
|----------|----------------------|----------------|
| H-0 | H-1 | Mildly Degraded |
| H-1 | H-2 | Moderately Degraded |
| H-2 | H-3 | Severely Degraded |
| H-3 | H-4 | Incapacitated |
| H-4 | H-4 | Incapacitated (ceiling) |

---

## 13 — Confidence notes on this document

- The H-0 to H-4 naming convention and threshold definitions are governance constructs derived from aviation degraded-mode hierarchies and military readiness levels `[I,75]`. They have not been validated in field use in this specific form. Validate via tabletop exercise and incident review.
- Observable indicators are derived from fatigue and cognitive load research literature `[I,80]`. Specific thresholds are calibrated estimates `[S,70]`.
- The "one-H-state-worse" circadian heuristic is grounded in established circadian performance research `[F,90]`; the specific H-state increment is a governance approximation `[S,75]`.
- Team mode-state is an inference from group cognition and CRM research `[I,70]`. Collective failure mode taxonomy draws on aviation and nuclear CRM `[I,80]`.
