# Belief Provenance and Epistemic Integrity

**Date:** 2026-03-28
**Scope:** Operator epistemic model — belief tagging, confidence gating, situational awareness mapping, trust boundaries, and pre-decision checks for consequential decisions.
**Status:** DRAFT
**Referenced by:** README.md §1; POL-OR-01 statement 3; `docs/contracts/oadc.md` §2 (epistemic degradation condition)

---

## 1 — Purpose

Operator decisions are only as reliable as the beliefs underlying them. This document defines the epistemic model governing how operators tag, assess, and act on beliefs during consequential decision-making. It establishes the provenance notation, confidence scale, gating rules, situational awareness mapping, and trust boundary checks that apply to all high-consequence decisions.

The model does not require philosophical precision. It requires traceable, actionable belief labeling that survives post-event review and supports second-person validation.

---

## 2 — Evidence tagging

Every belief used in a consequential decision shall be tagged with its provenance class at the point of use (decision log, verbal declaration, briefing record).

| Tag | Class | Definition |
|-----|-------|------------|
| `[F]` | Verified fact | Directly observed or confirmed from a trusted, authenticated source with no material inference gap. The operator can state the source, the timestamp, and the verification method. |
| `[I]` | Inference | Derived from one or more `[F]` inputs by reasoning, correlation, or pattern recognition. The inference chain is traceable but not directly confirmed. |
| `[S]` | Assumption / heuristic / unresolved assumption | Held without verified support, based on experience, prior pattern, or organizational default. Includes any belief the operator cannot trace to a specific `[F]` or sound `[I]` chain. |

### 2.1 — Tag assignment rules

1. When in doubt, tag the more conservative class (`[S]` over `[I]`, `[I]` over `[F]`).
2. A chain is only as strong as its weakest link: if any input to an inference is `[S]`, the inference is also `[S]` unless independently verified.
3. `[F]` does not mean infallible — it means the source was authenticated and the data was fresh at the time of tagging. A stale `[F]` degrades to `[I]` when it exceeds the freshness threshold for that information type.
4. Tags apply to discrete beliefs, not to the decision as a whole.

---

## 3 — Confidence levels

Confidence is an operator-declared estimate of correctness probability, quantized to the set `{50, 70, 80, 90}`. Continuous confidence ratings are not used; quantization forces explicit calibration and resists false precision.

| Level | Operational meaning | Typical provenance mix |
|-------|---------------------|------------------------|
| `50` | Coin-flip — operator has a position but cannot justify it above chance. High probability of material error. | Predominantly `[S]`; no corroborating `[F]`. |
| `70` | Working hypothesis — the position is defensible but has known gaps or single-source dependence. Proceed with caution and reversibility. | Mix of `[I]` and `[S]`; some `[F]` support. |
| `80` | Confident — multiple independent sources or a solid inference chain. Known unknowns are bounded. | Predominantly `[F]` and `[I]`; limited `[S]`. |
| `90` | High confidence — convergent `[F]` evidence from independent sources. Material surprise would require deliberate deception or sensor failure. | Almost entirely `[F]`; inference chain is short and well-validated. |

Confidence above `90` is not a valid rating. If an operator believes certainty is absolute, that belief itself is a calibration failure.

### 3.1 — Confidence expression format

Confidence is expressed as a tag suffix: `[F,90]`, `[I,70]`, `[S,50]`. In verbal or written decision logs, the operator states: provenance tag, confidence level, and the key uncertainty or check that would change it.

Example: *"Assumption: the upstream feed is live and unmanipulated [S,65]. Check: heartbeat timestamp and hash verification. If < 70% without that check, partial action only."*

---

## 4 — Confidence gating

**Rule:** If decision confidence is below 70%, the operator shall not proceed with irreversible or high-consequence action.

| Confidence | Required action before proceeding |
|------------|-----------------------------------|
| `≥ 80` | Standard pre-decision check; log beliefs and proceed. |
| `= 70` | State checks required: identify what would raise confidence. Proceed with safe, reversible partial action only. Log the gap explicitly. |
| `< 70` | Halt irreversible action. State checks required. Proceed only with safe, reversible partial action. Escalate if checks cannot be completed. |
| `= 50` | Do not proceed with any consequential action. Escalate or invoke safe state. |

"Safe reversible partial action" means an action whose effect can be fully undone, which does not foreclose subsequent options, and whose scope is narrowed to the lowest-consequence intervention available given current knowledge.

### 4.1 — Checks required at confidence < 70%

When confidence is below threshold, the operator shall:

1. Identify the specific beliefs driving the confidence deficit (tag them `[S]` or `[I]`).
2. State the check(s) that would upgrade each belief (e.g., independent source confirmation, heartbeat validation, peer review).
3. Declare whether those checks can be completed before the decision deadline.
4. If checks can be completed: complete them; re-assess confidence; log result.
5. If checks cannot be completed: proceed only with safe reversible partial; escalate; invoke OADC conditions as applicable (see §8).

---

## 5 — Endsley's situational awareness model and belief mapping

Belief provenance maps directly to Endsley's three-level Situational Awareness (SA) model. Failures at each level produce characteristic error patterns that the tagging system helps detect.

| SA Level | Definition | Belief provenance relevance | Failure mode |
|----------|------------|----------------------------|--------------|
| **Level 1 — Perception** | Detection and observation of relevant environmental elements: sensor data, alarms, reports, readings. | Source of `[F]` beliefs. If perception is corrupted (adversarial signal, stale sensor, false alarm), `[F]` tags are incorrectly assigned — the foundational failure. | Missing or false alarms; sensor lag; information not reaching the operator; adversarial signal injection. |
| **Level 2 — Comprehension** | Integration and interpretation of perceived elements into a coherent picture of current state. | Source of `[I]` beliefs. Comprehension involves pattern recognition and mental model application. Erodes under fatigue (H-2+), OOTL monitoring, and cognitive load. | Incorrect diagnosis; ignored anomaly; confirmation bias; model fixation. |
| **Level 3 — Projection** | Anticipation of future states and events based on current picture. | Source of most `[S]` beliefs used in planning. Projection is inherently inferential. Errors here often drive premature or excessive action. | Over-confident forecast; failure to account for adversarial intent; incorrect extrapolation. |

### 5.1 — SA degradation and provenance shift

Under stress, fatigue, or OOTL monitoring conditions, the quality of beliefs at each level degrades predictably:

- Level 1 degradation: `[F]` beliefs are based on stale or unverified data → should be re-tagged `[I]`.
- Level 2 degradation: `[I]` inference chains lengthen or incorporate unchecked assumptions → should be re-tagged `[S]`.
- Level 3 degradation: projection confidence inflates even as inputs degrade (a well-documented stress and fatigue effect).

The pre-decision epistemic check (§7) is designed to surface these degradations before consequential action.

---

## 6 — Operator information trust boundary

Operator information intake is treated as a trust boundary analogous to a system's external-data ingestion boundary. Information crossing this boundary shall be assessed against five trust checks.

| Trust check | Description | Failure indicator |
|-------------|-------------|-------------------|
| **Source authentication** | Is the origin of the information verified? Can the operator identify who or what produced it, via what channel, with what credential or relationship? | Unsigned message; unverified caller; unfamiliar relay. |
| **Freshness** | Is the information current enough for the decision at hand? Does it carry a timestamp? Does the timestamp fall within the freshness threshold for this information type? | Missing timestamp; stale reading; no heartbeat. |
| **Cross-validation** | Does at least one independent source corroborate the key claim? Independence means different physical path, different organizational origin, or different measurement modality. | Single-source claim for a high-consequence decision; consistent only because derived from the same upstream. |
| **Authority** | Is the source authorized to make or report this kind of claim? Does the organizational or technical authority chain support the information's scope? | Lateral authority claim; source outside normal reporting chain; escalation bypass. |
| **Consistency** | Is the information consistent with the prior established picture? If inconsistent, is there a credible explanation? | Unexplained step-change; conflicts with independent source without acknowledged reason. |

A belief derived from information that fails two or more trust checks shall be tagged `[S]` regardless of how it was originally received. A belief derived from information failing one trust check shall be tagged at most `[I]`.

### 6.1 — Adversarial trust boundary violations

Information manipulation is a documented adversarial tactic against operators. The trust boundary framework is specifically designed to detect:

- Injection of false `[F]` signals (passing source authentication and freshness checks while failing cross-validation).
- Authority spoofing (failing source authentication or authority checks).
- Urgency manipulation (artificial time pressure to force decisions before cross-validation can occur — triggering the OADC time-pressure condition).

If an operator detects a pattern of trust boundary failures across multiple checks, this constitutes an epistemic integrity alert. Escalate and widen the OADC authority constraints per `docs/contracts/oadc.md` §2.

---

## 7 — Pre-decision epistemic check

Before any high-consequence decision, the operator shall complete and log a pre-decision epistemic check. This check is the primary mechanism for surfacing epistemic degradation before action.

### 7.1 — Pre-decision check format

```
Pre-Decision Epistemic Check
-----------------------------
Decision: [one-sentence description of the action being authorized]
Timestamp: [ISO 8601]
Operator: [identifier]

Assumptions:
  1. [Belief statement] [Tag, Confidence]
  2. [Belief statement] [Tag, Confidence]
  ...

Constraints:
  - [Hard constraint that must be true for this action to be safe]
  - ...

Unknowns:
  - [What is not known that would materially change the decision]
  - ...

Confidence: [Aggregate — use the minimum across consequential beliefs]

Gate:
  [ ] Confidence >= 70% — proceed with care.
  [ ] Confidence < 70% — state checks, safe reversible partial only.
  [ ] Confidence = 50% — halt; escalate.

Checks to raise confidence (if below 70%):
  - [Check description and expected result]

Second-person reviewer (if required by OADC): [identifier]
```

### 7.2 — Mandatory pre-decision check triggers

A pre-decision epistemic check is mandatory when any of the following apply:

- The decision is classified as high-consequence per the active OADC instance.
- The operator is at H-2 or above.
- Any key belief is tagged `[S]` or carries confidence ≤ 70%.
- The OADC single-source condition, epistemic degradation condition, or OOTL condition is active.
- The decision involves irreversible action.

---

## 8 — Out-of-the-loop (OOTL) degradation

Out-of-the-loop degradation occurs when an operator in passive monitoring mode loses active engagement with the system state. It is a structural SA failure, not a performance failure — it is an expected consequence of passive monitoring architecture.

### 8.1 — Mechanism

| Duration of passive monitoring | Expected SA degradation |
|-------------------------------|-------------------------|
| < 15 minutes | Level 1 perception generally intact; Level 2 comprehension begins to drift if no events occur. |
| 15–30 minutes | Level 2 comprehension significantly degraded; mental model of current state is stale. Level 3 projection is based on an outdated baseline. |
| > 30 minutes (OADC default threshold) | Level 2/3 effectively invalid. State-check required before any intervention. |

### 8.2 — OOTL state-check requirement

Per `docs/contracts/oadc.md` §2 (passive monitoring condition): after exceeding the `passive_monitoring_interval` parameter, the operator shall complete a state-check before any intervention. If the state-check fails (operator cannot correctly describe current system state within defined tolerance), treat as H-2 regardless of other indicators.

A state-check consists of:

1. Operator verbally or textually states the current system state (key parameters, active alarms, last known transitions).
2. State is compared against actual system state by a second person or automated system check.
3. Discrepancies beyond threshold = state-check failure.

### 8.3 — OOTL and belief re-tagging

After OOTL, all Level 2 and Level 3 beliefs the operator holds about current system state shall be re-tagged:

- `[F]` → `[I]` (observed facts are now potentially stale).
- `[I]` → `[S]` (inferences are based on a potentially outdated picture).

Re-tagging propagates through the confidence reassessment before the operator acts.

---

## 9 — Belief revision triggers

Anchoring — the cognitive tendency to under-update beliefs in response to new evidence — is a documented failure mode under stress and time pressure. The following triggers require explicit belief revision:

| Trigger | Required action |
|---------|-----------------|
| New information that contradicts a `[F]` belief | Re-evaluate source: is the new information authenticated? Which source has higher trust-boundary score? Do not anchor. |
| Anomaly unexplained by current mental model | Declare the anomaly; do not absorb it silently. Widen `[S]` scope; lower aggregate confidence if not resolved. |
| Time elapsed beyond freshness threshold | Re-tag affected `[F]` beliefs as `[I]`; re-assess confidence. |
| OOTL state-check discrepancy | Full belief reset for affected subsystem; treat as H-2 until picture is re-established. |
| Second-person reviewer disagrees | Pause action; surface disagreement explicitly; resolve before proceeding. Do not override peer challenge without logging the rationale. |
| Peer observation of epistemic degradation markers | Accept the challenge; re-run pre-decision check. |

### 9.1 — Anchoring risk conditions

Anchoring risk is elevated under:

- Time pressure (OADC time-pressure condition active).
- H-2 or above (fatigue and stress both increase anchoring susceptibility).
- Confirmation events following a prior `[S]` belief (single confirming data point does not upgrade `[S]` to `[F]` without source authentication and independence).
- Extended incident duration (cognitive investment in prior diagnosis increases anchoring).

Under these conditions, the second-person reviewer has explicit authority to challenge belief tags and confidence levels.

---

## 10 — Relationship to OADC conditions

The OADC conditions in `docs/contracts/oadc.md` §2 that directly interact with the epistemic model:

| OADC condition | Epistemic model interaction |
|----------------|----------------------------|
| **Single information source for key claim** | Trust-boundary cross-validation check fails. Key belief shall not exceed `[I,70]`. High-consequence action prohibited until second independent source confirms. |
| **Epistemic degradation markers detected** | Aggregate decision confidence shall be re-assessed. Pre-decision check mandatory for any consequential action. Authority narrowed; peer validation required. |
| **Extended passive monitoring (OOTL)** | All current-state beliefs re-tagged per §8.3. State-check required before intervention. If state-check fails, treat as H-2. |
| **Circadian low** | Performance on Level 2 comprehension and Level 3 projection is statistically degraded. Confidence levels shall not be inflated to compensate for circadian effects. Apply one-H-state-worse heuristic (see `docs/resilience/h-state-table.md`). |
| **Time pressure below minimum review threshold** | Pre-committed decision tree only; no novel authority. Belief provenance check is abbreviated to: is any key constraint violated? If yes, halt. |

---

## 11 — Confidence notes on this document

- The evidence-tagging model is operationally derived and draws on aviation CRM, military decision-making under uncertainty, and naturalistic decision-making research `[I,75]`. It has not been validated in field use in this specific form. Validate with tabletop exercises before operational reliance.
- The Endsley SA framework mapping is well-established in human factors literature `[F,90]`; its application to operator authority degradation is an inference `[I,80]`.
- The trust boundary framework is an inference from cybersecurity supply-chain trust models applied to human information intake `[I,70]`.
- The OOTL freshness thresholds (15/30 minutes) are estimates based on aviation research; the correct threshold is environment-dependent `[S,65]`. Set `passive_monitoring_interval` per OADC instance for the specific operating context.
