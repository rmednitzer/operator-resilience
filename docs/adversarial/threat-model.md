# Adversarial Threat Model — Operator Targeting

**Date:** 2026-03-28
**Status:** DRAFT
**Scope:** Threat taxonomy, actor profiles, attack chain analysis, and control mapping for adversarial targeting of human operators. Covers social engineering, duress, information manipulation, fatigue exploitation, relationship exploitation, and insider threat. Insider threat controls at the operating-contract layer.
**Referenced by:** `docs/adversarial/duress-protocol-spec.md`; `docs/contracts/oadc.md`; `docs/epistemics/belief-provenance.md`

> **Safety-critical document.** Any change to this threat model that affects OADC conditions, duress protocol scope, or insider threat controls requires the two-person review process defined in `CONTRIBUTING.md`. See also: CACE principle — changing anything changes everything.

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

This document defines the adversarial threat model for operator targeting in environments governed by the operator-resilience framework. It catalogues the threat actors, vectors, objectives, and impacts relevant to operators who hold authority over consequential decisions, and maps those threats to the repository controls designed to detect, constrain, or recover from them.

The threat model serves three functions:

1. **Design rationale:** Explains why specific controls (OADC conditions, duress protocol, epistemic checks, buddy-pair) exist and what threat they address.
2. **Exercise basis:** Provides the adversarial scenario catalogue for exercise design per `docs/exercise/exercise-program.md`.
3. **Gap analysis anchor:** When new controls are proposed or existing controls are weakened, this model is the reference for assessing whether coverage degrades.

This document does not contain classified threat intelligence or environment-specific attack specifics. Those belong in the per-environment operational threat assessment, referenced from the OADC instance for that environment.

---

## 2 — Threat taxonomy

The following threat categories are in scope. Each category is defined by its vector, adversarial objective, targeted control layer, and potential impact on operational outcomes.

| # | Threat category | Threat actor | Vector | Adversarial objective | Target | Impact |
|---|----------------|-------------|--------|----------------------|--------|--------|
| T-1 | Social engineering | External adversary; compromised insider | Phishing, pretexting, vishing, authority impersonation | Manipulate operator beliefs or decisions via deception | Epistemic integrity; operator authority | Unauthorized high-consequence action authorized by deceived operator |
| T-2 | Duress | External adversary; organized threat actor | Physical coercion, psychological intimidation, threat to associates | Compel authorized operator to act against organizational intent | Operator autonomy; OADC authority constraints | Hostile-controlled authorized action executed by legitimate operator |
| T-3 | Information manipulation | External adversary; insider | Injection of false, stale, or selectively omitted data into operator's information environment | Corrupt situational awareness (SA Level 1/2/3) before a consequential decision | Perception layer; comprehension layer; belief provenance | Confident wrong decision executed with apparent epistemic justification |
| T-4 | Fatigue exploitation | External adversary; insider | Deliberate timing attacks, sleep disruption, sustained cognitive load to exhaust operator | Degrade operator cognitive capacity below OADC authority guardrails | H-state (cognitive capacity); OADC duty limits | Degraded authority guardrails exercised by a cognitively impaired operator |
| T-5 | Relationship exploitation | External adversary; insider | Misuse of legitimate organizational relationships — supervisor authority, peer trust, vendor relationships — to bypass OADC controls | Obtain operator compliance without triggering verification steps | Authority verification; buddy-pair integrity | Unjustified authority expansion authorized through social authority rather than OADC conditions |
| T-6 | Insider threat | Operator; authorized insider | Intentional violation of OADC constraints; exploitation of legitimate authority access for unauthorized objectives | Achieve an unauthorized outcome while appearing to operate within normal bounds | All control layers simultaneously | All impact categories; uniquely difficult to detect because the actor has legitimate access and context knowledge |

### 2.1 — Scope notes

**T-2 (Duress)** is addressed in detail in `docs/adversarial/duress-protocol-spec.md`. This document provides the threat model context; the duress-protocol-spec provides the operational architecture. Where it is ambiguous whether a situation is T-2 duress or T-4 fatigue exploitation, treat as T-2 until resolved.

**T-3 (Information manipulation)** targets the operator's information trust boundary as defined in `docs/epistemics/belief-provenance.md` §6. The five trust checks (source authentication, freshness, cross-validation, authority, consistency) are the primary epistemic controls against this threat.

**T-6 (Insider threat)** is not a separate attack vector but a threat actor class that can exploit any of T-1 through T-5. Its distinctiveness is that the actor bypasses perimeter controls by definition, making operating-contract controls the primary mitigation layer.

---

## 3 — Threat actor profiles

| Actor class | Description | Distinguishing characteristic | Primary threats exploited |
|-------------|-------------|-------------------------------|--------------------------|
| External adversary | Individual or organized group without authorized access to the operating environment | Cannot directly access systems; must route through operators; most likely to use T-1, T-2, T-3 | T-1, T-2, T-3 |
| Insider | Operator or authorized personnel acting contrary to organizational intent for personal gain, ideology, or grievance | Has legitimate access and contextual knowledge; can bypass perimeter controls; OADC constraints are the primary check | T-5, T-6 |
| Compromised insider | Operator or authorized personnel acting under external direction, blackmail, or control — not acting on personal volition | Appears as normal insider behavior; may resist detection because actor may attempt to comply minimally while signaling duress | T-2, T-6 (externally directed) |
| Opportunistic insider | Insider who exploits a situational gap (fatigue, reduced oversight, organizational stress) without sustained intent | Does not require sophisticated planning; relies on degraded control environment; most likely during high-tempo or high-stress periods | T-4, T-5, T-6 |

---

## 4 — Attack chain analysis

Adversarial targeting rarely relies on a single vector. The following chains describe documented combinations that produce compressed decision spaces or impaired operators.

### 4.1 — Fatigue exploitation + social engineering + time pressure

**Chain:** Adversary identifies a high-tempo period or deliberately generates sustained cognitive load (e.g., via automated alert flooding) to degrade operator H-state. Once operator is at H-2 or above, adversary applies social engineering during a fabricated time-pressure window.

**Effect:** Operator is cognitively impaired (H-2+), epistemic confidence is inflated due to fatigue anchoring, and the artificial time pressure eliminates the minimum review threshold. The compressed decision space prevents the operator from completing the pre-decision epistemic check.

**OADC conditions triggered:** On-call duration; epistemic degradation markers; time pressure below minimum review threshold.

**Primary controls:** H-state monitoring; OADC time-pressure condition; pre-decision epistemic check (abbreviated form); buddy-pair for consequential decisions.

### 4.2 — Information manipulation + authority impersonation + urgency

**Chain:** Adversary injects false or selectively omitted data into operator's information environment (corrupting SA Level 1 perception), then impersonates a supervisor or authority figure to issue an instruction consistent with the manipulated picture, claiming urgency to prevent cross-validation.

**Effect:** Operator holds a false `[F]` belief derived from manipulated perception, receives an authority-claiming instruction, and is discouraged from applying trust boundary checks. The instruction appears both situationally coherent and organizationally authorized.

**OADC conditions triggered:** Communication from unverified authority; single information source for key claim; time pressure below minimum review threshold.

**Primary controls:** Source authentication check; second-channel identity verification; single-source OADC condition; closed-loop communications protocol (see `docs/adversarial/comms-security.md`).

### 4.3 — Relationship exploitation + organizational stress

**Chain:** During a declared organizational stress period (elevated workload, restructuring, incident surge), an insider or social engineer exploits informal authority relationships — a senior colleague, a trusted vendor contact, a cross-team lead — to request authority expansion or a procedural bypass. The request is framed as expedient given the stress context.

**Effect:** Operator grants authority or procedural exception through a legitimate-appearing relationship channel. The OADC constraint is bypassed without triggering formal escalation because the request came from a known, trusted source within normal organizational patterns.

**OADC conditions triggered:** Organizational stress; communication from unverified authority (if the relationship is not within the operator's formal authority chain).

**Primary controls:** OADC organizational stress tightening; decision log requirement; buddy-pair for authority expansion requests; out-of-band verification for any instruction requiring authority expansion.

### 4.4 — Insider + passive monitoring + OOTL exploitation

**Chain:** An insider with legitimate access waits for or induces an extended passive monitoring period (OOTL), then takes or authorizes a consequential action while the monitoring operator's situational awareness is degraded and the insider's activity appears within normal operational parameters.

**Effect:** The action is taken during a window when the nominal oversight operator lacks the SA to detect the anomaly. Audit log review may be the only detection path.

**OADC conditions triggered:** Extended passive monitoring (OOTL); insider threat indicators.

**Primary controls:** Passive monitoring interval enforcement; state-check before intervention; append-only audit log; passive monitoring detection (behavioral indicator).

---

## 5 — Controls summary

The following table maps each threat category to the repository controls that address it. Controls are evaluated by primary coverage (directly constrains or detects the threat) and supporting coverage (reduces the threat's effectiveness or increases detection probability).

| Threat | OADC conditions | Duress protocol | Epistemic checks | H-state monitoring | Buddy-pair / two-person rule | Decision logging |
|--------|----------------|-----------------|------------------|-------------------|------------------------------|-----------------|
| T-1 Social engineering | Unverified authority; single source; time pressure | Indirect — signal if coerced by social pressure | Source authentication; cross-validation; trust boundary checks | Elevated H-state increases susceptibility | Second person validates belief tags and authority claim | Logs authority claim and epistemic state at decision point |
| T-2 Duress | Contested environment; unverified authority | **Primary control** — full signal/response architecture | Epistemic integrity check by monitoring function | H-state monitoring by monitoring function | Monitoring function role | Duress event record (schema: `schemas/duress-event.schema.json`) |
| T-3 Information manipulation | Single source; epistemic degradation | — | **Primary control** — five trust checks; belief re-tagging | H-2+ increases vulnerability to false `[F]` tagging | Second source requirement; peer review of key beliefs | Logs belief provenance used at decision point |
| T-4 Fatigue exploitation | On-call duration; circadian low; epistemic degradation | — | Confidence gating; pre-decision check | **Primary control** — H-state thresholds; authority narrowing | Buddy-pair mandatory at H-2+; OADC duty limits | Logs H-state at decision point |
| T-5 Relationship exploitation | Organizational stress; unverified authority | — | Authority trust check | — | **Primary control** — two-person rule for authority expansion; out-of-band verification | Logs authority source and verification method |
| T-6 Insider threat | All OADC conditions simultaneously | Coercion detection path | Peer review of belief tags; anomalous confidence patterns | Peer H-state assessment | **Primary control** — two-person rule; buddy-pair | **Primary control** — append-only audit log; passive monitoring detection |

---

## 6 — Detection indicators

### 6.1 — Behavioral indicators of active adversarial pressure

The following behavioral patterns in an operator may indicate active adversarial targeting. These indicators do not confirm adversarial action; they elevate suspicion and trigger verification steps.

| Indicator | Associated threat | Response |
|-----------|------------------|----------|
| Operator appears stressed, evasive, or unusually compliant during communications | T-2 Duress | Verify using pre-established duress protocol; check for duress signal; do not confront adversary |
| Operator bypasses or resists completing the pre-decision epistemic check | T-3, T-6 | Buddy-pair intervention; log and escalate |
| Operator makes unusual authority expansion requests, especially under time pressure | T-1, T-5 | Out-of-band authority verification; OADC organizational stress check |
| Operator is resistant to buddy-pair or second-person validation | T-6 | Escalate to supervisor; log; treat as insider threat indicator |
| Operator's stated beliefs do not align with observable system state | T-3, T-4 | State-check; re-tag beliefs; assess H-state |
| Operator is unusually fatigued outside declared H-state | T-4 | H-state reassessment; apply OADC duty limits |
| Operator references an authority or instruction the monitoring function cannot independently verify | T-1, T-5 | OADC unverified authority condition; second-channel verification |

### 6.2 — Epistemic indicators

| Indicator | Associated threat | Response |
|-----------|------------------|----------|
| Key belief is `[F]`-tagged but source is unverified or the single-source condition applies | T-3 | Re-tag as `[I]`; apply single-source OADC condition |
| Unusual urgency or time pressure coincides with an authority claim | T-1, T-3 | Invoke time-pressure OADC condition; demand minimum review time; out-of-band verification |
| Authority claims cannot be verified through the normal chain | T-1, T-5 | Hold action; authenticate via second channel; log the claim |
| Multiple trust boundary checks fail simultaneously for the same information | T-3 | Epistemic integrity alert per `docs/epistemics/belief-provenance.md` §6.1; widen OADC constraints |
| Anomalous source pattern — information arriving via non-standard channel or unusual relay | T-3 | Source authentication check; freshness check; escalate if unresolvable |
| Operator's confidence level is inconsistent with belief provenance tag quality | T-4, T-3 | Pre-decision check; second-person review of belief tags |

---

## 7 — Insider threat specifics

Insider threat is the highest-residual-risk category because the actor has legitimate credentials, contextual knowledge, and plausible cover for most actions. The operating-contract layer (OADC plus decision logging) is the primary mitigation.

### 7.1 — OADC controls constraining insider actions

| Control | Mechanism | Insider threat constraint |
|---------|-----------|--------------------------|
| Two-person rule | No single operator can authorize a high-consequence action unilaterally when the condition is active | Requires insider to compromise or coerce a second person, significantly raising the cost and detectability of the attack |
| Decision logging (append-only) | All consequential decisions are logged with belief provenance, authority source, and timestamp; log is not modifiable by the acting operator | Creates an auditable trail that survives even if the insider attempts post-hoc rationalization; append-only requirement prevents log tampering |
| Second-source requirement | Single-source OADC condition prevents high-consequence authorization without independent corroboration | Requires insider to manipulate two independent information sources, increasing complexity and detectability |
| Passive monitoring detection | Behavioral indicator: insider takes or authorizes action during an OOTL window when oversight is degraded | System enforcement of passive monitoring interval surfaces OOTL windows; state-check requirement before intervention reduces exploitation window |

### 7.2 — Behavioral indicators specific to insider threat

| Indicator | Significance |
|-----------|-------------|
| Sudden or unexplained authority expansion requests | Insider seeking to widen scope of authorized action before taking the target action |
| Bypassing or resisting the decision log | Insider attempting to avoid creating an auditable record |
| Resistance to buddy-pair or second-person validation | Insider aware that a second person would detect or block the action |
| Pattern of testing procedural limits without clear operational necessity | Reconnaissance of control gaps |
| Action taken during OOTL window or circadian low when oversight is statistically reduced | Exploitation of degraded oversight environment |
| Unusual interest in another operator's OADC constraints or H-state | Potential identification of exploitation window |

### 7.3 — CER Art. 13(1)(e) alignment

The insider threat controls specified in this section support alignment with CER Art. 13(1)(e) requirements for personnel security and access rights management for personnel exercising critical functions. Indicative mapping — applicability depends on entity classification and sector. See `docs/integration/regulatory-cross-reference.md` for detailed analysis.

| CER Art. 13(1)(e) element | Repository control |
|---------------------------|-------------------|
| Personnel security measures for critical-function personnel | OADC constraints; two-person rule; buddy-pair |
| Access rights management | OADC authority limits per condition; system enforcement requirements (`docs/contracts/oadc.md` §4) |
| Background checks for critical-function personnel | Conditional — see `docs/integration/regulatory-cross-reference.md`; CER Art. 14 governs |
| Monitoring and oversight of critical-function personnel | Decision logging; passive monitoring detection; H-state monitoring |

---

## 8 — Confidence notes

- Threat categories T-1 through T-6 are derived from established security frameworks (MITRE ATT&CK for Enterprise, insider threat behavioral frameworks, NATO information operations doctrine) `[F,80]`. The mapping to operator authority and OADC controls is a structural inference from those frameworks `[I,75]`.
- Specific attack chains in §4 are inferences applied to autonomous-platform and OT/ICS operator contexts; limited published field data exists for these specific combinations `[I,70]`. Validate through adversarial tabletop exercises before operational reliance.
- Behavioral and epistemic indicators in §6 are derived from organizational security literature and CRM/human factors research `[I,70]`. They are not diagnostic — they are triggers for verification steps.
- Insider threat controls (§7) are grounded in critical-infrastructure insider threat frameworks `[F,80]`; the OADC-layer operationalization is an inference `[I,70]`.
