# Regulatory Cross-Reference

**Date:** 2026-03-23
**Status:** DRAFT
**Scope:** Indicative mapping of operator-resilience controls to EU and international regulatory requirements. Applicability depends on sector, entity classification, and deployment context.

---

## 1 — Applicability scoping

This repository governs operator authority across IT/SRE, OT/ICS, autonomous platforms, and military/first-responder contexts. Not all regulations apply in all contexts. The table below indicates which regulations are conditionally relevant by deployment sector.

| Regulation | Sector scope | Conditional on |
|------------|-------------|----------------|
| EU AI Act (Reg. 2024/1689) | Any deployer of high-risk AI systems | System classified as high-risk per Annex III |
| NIS2 (Dir. 2022/2555) | Essential and important entities in scope sectors | Entity meets size/sector thresholds per Arts. 2–3 |
| CER (Dir. 2022/2557) | Critical entities designated by Member States | Entity identified per Art. 6 |
| DORA (Reg. 2022/2554) | Financial entities | Entity in scope per Art. 2 |
| Machinery Reg. (Reg. 2023/1230) | OT/ICS with machinery products | Machinery placed on market after 2027-01-20 |
| Seveso III (Dir. 2012/18/EU) | Upper/lower-tier establishments handling hazardous substances | Substance thresholds per Annex I |
| MIL-STD-882E | Defence/military systems | Contract or policy requirement |
| DoD Directive 3000.09 | Autonomous weapon systems | US DoD context |

> **Note:** Seveso III and Machinery Regulation are referenced for scoping completeness. Their article-level text was not machine-verified in this analysis. Claims below marked [S] are based on regulatory knowledge, not primary-text retrieval.

## 2 — EU AI Act (Regulation 2024/1689)

Effective 2024-08-01; human oversight obligations apply from 2026-08-02.

### Art. 14 — Human oversight

Full title: "Human oversight." Applies to high-risk AI systems under Chapter III, Section 2.

| AI Act provision | Repository control | Alignment |
|---|---|---|
| Art. 14(1): systems designed for effective oversight by natural persons | OADC §1 (Purpose): operator authority as a governed boundary | Direct — OADC formalises what "effective oversight" means operationally |
| Art. 14(2): prevent/minimise risks to health, safety, fundamental rights | Policy stmt 1–2: no authority without OADC; parameters set in advance | Direct |
| Art. 14(4)(a): understand capacities/limitations, monitor, detect anomalies | Epistemic provenance model; SA framework; pre-decision check | Direct — belief provenance and confidence gating address this |
| Art. 14(4)(b): remain aware of automation bias | OADC condition: extended passive monitoring (OOTL); H-state detection | Direct — OOTL degradation is an operationalisation of automation bias awareness |
| Art. 14(4)(c): correctly interpret system output | Epistemic check: assumptions [F]/[I]/[S], confidence gating | Supportive — interpretation aids via provenance tagging |
| Art. 14(4)(d): decide not to use, override, or reverse system output | OADC: operator retains authority within contract bounds; contestation resistance | Direct — OADC preserves override authority, bounded by degradation state |
| Art. 14(4)(e): intervene or interrupt; halt in safe state | Safe-state specification (§6); emergency stop analogy | Direct — operator-absent safe state is the implementation mechanism |
| Art. 14(5): two-person verification for biometric identification | OADC: two-person rule under contested environment and high-consequence actions | Structural analogy — OADC applies two-person rule more broadly |

### Art. 26 — Obligations of deployers of high-risk AI systems

| AI Act provision | Repository control | Alignment |
|---|---|---|
| Art. 26(2): assign human oversight to persons with necessary competence, training, and authority | Roles and responsibilities (§30–36); exercise program; return-to-duty protocol | Direct — the OADC framework operationalises "necessary authority" as a degradation-aware contract |
| Art. 26(5): monitor operation; inform provider of risks; suspend use | H-state monitoring; mandatory handoff at H-3/H-4; safe-state entry | Supportive |
| Art. 26(6): keep automatically generated logs ≥ 6 months | Policy stmt 8: all trigger events logged as evidence with timestamps | Direct — evidence retention requirement |

### Art. 9 — Risk management system

| AI Act provision | Repository control | Alignment |
|---|---|---|
| Art. 9(2): continuous iterative risk management through lifecycle | Exercise program with defined cadences; post-event review loop; CACE principle | Direct |
| Art. 9(5)(c): training to deployers | Exercise types; cybersecurity training mapping | Supportive |

## 3 — NIS2 (Directive 2022/2555)

Transposition deadline 2024-10-17. Applies to essential and important entities.

### Art. 21 — Cybersecurity risk-management measures

| NIS2 provision | Actual text | Repository control | Alignment |
|---|---|---|---|
| Art. 21(2)(a) | "policies on risk analysis and information system security" | Policy stmts 1–4; OADC as a security policy governing operator authority | Direct |
| Art. 21(2)(b) | "incident handling" | Policy stmts 7–9; mandatory handoff; post-event review | Direct |
| Art. 21(2)(c) | "business continuity, such as backup management and disaster recovery, and crisis management" | Safe-state specification; handoff protocol; operator-absent safe state | Partial — crisis management is addressed; backup/disaster recovery is out of scope for this repo |
| Art. 21(2)(f) | "policies and procedures to assess the effectiveness of cybersecurity risk-management measures" | Exercise program with acceptance criteria; controls not exercised assumed non-functional | Direct |
| Art. 21(2)(g) | "basic cyber hygiene practices and cybersecurity training" | Exercise program; duress protocol training; epistemic check training | Partial — cybersecurity training addressed; basic cyber hygiene is broader than operator resilience |
| Art. 21(2)(i) | "human resources security, access control policies and asset management" | OADC system enforcement (two-person auth, session timeout, time-of-day awareness); roles and responsibilities | Direct — OADC enforces access control degradation; HR security via return-to-duty protocol |
| Art. 21(2)(j) | "multi-factor authentication or continuous authentication solutions, secured voice, video and text communications and secured emergency communication systems" | OADC: communication from unverified authority → hold and authenticate via second channel; incident comms security (closed-loop protocol) | Partial — authentication and comms security addressed at protocol level |

### Recital 79

NIS2 Recital 79 explicitly calls for "human resources security" and "appropriate access control policies" as part of cybersecurity risk management. The OADC is an operationalisation of access control that degrades with operator state — a refinement beyond static RBAC.

## 4 — CER (Directive 2022/2557)

Critical Entities Resilience Directive. Transposition deadline 2024-10-17.

### Art. 13 — Resilience measures of critical entities

| CER provision | Repository control | Alignment |
|---|---|---|
| Art. 13(1)(c): respond to, resist and mitigate incidents; risk and crisis management procedures | OADC condition taxonomy; crisis management via safe-state and handoff | Direct |
| Art. 13(1)(e): adequate employee security management — categories of personnel exercising critical functions, access rights, background checks, training | Roles and responsibilities; OADC applies to "all operators in roles where their decisions can cause or fail to prevent a high-consequence outcome"; exercise program | Direct — OADC categorises operator authority by criticality |
| Art. 13(1)(f): raise awareness among relevant personnel; training, exercises | Exercise program (seven types with cadences); acceptance criteria | Direct |
| Art. 13(2): resilience plan or equivalent documents | This repository as a whole constitutes the resilience plan for operator governance | Structural |

### Art. 14 — Background checks

CER Art. 14 permits critical entities to request background checks for personnel in critical functions, subject to proportionality and Member State implementation. This is conditionally relevant — applicable where operators are designated as exercising critical functions under CER.

## 5 — DORA (Regulation 2022/2554)

Digital Operational Resilience Act. Applicable from 2025-01-17. Financial sector only.

### Art. 11 — Response and recovery

| DORA provision | Repository control | Alignment |
|---|---|---|
| Art. 11(2)(e): communication and crisis management actions | OADC: incident comms security; closed-loop protocol | Supportive |
| Art. 11(6)(a): test ICT business continuity plans yearly | Exercise program: annual cadence minimum for all control types | Direct alignment on testing cadence |
| Art. 11(7): crisis management function | OADC condition: organisational stress; incident commander role | Structural analogy |

## 6 — Machinery Regulation (Regulation 2023/1230)

Applies from 2027-01-20. Relevant for OT/ICS contexts.

| Provision | Repository control | Alignment |
|---|---|---|
| Annex III §1.2.4.3: Emergency stop [S] | Safe-state specification; OADC §6 | Structural — safe state maps to emergency stop / safe halt |
| Annex III §1.1.6: Ergonomics, operator fatigue, mental overload [S] | H-state table; circadian adjustment; OADC duty duration limits | Direct — OADC operationalises operator capacity constraints |
| Recital 12: advanced machinery less dependent on human operators | OOTL degradation; autonomous-system bridge | Contextual |

## 7 — Gaps and recommendations

### Controls with no current EU regulatory mapping

| Repository control | Potential EU basis | Status |
|---|---|---|
| Duress protocols | No specific EU article; general duty of care under national employment law; insider threat dimension under CER Art. 13(1)(e) | Gap — consider scoping note |
| Epistemic provenance model ([F]/[I]/[S] tagging) | Novel; no direct regulatory requirement. Supports AI Act Art. 14(4)(a)–(c) and NIS2 Art. 21(2)(a) in practice | Exceeds requirements |
| CACE principle | No direct regulatory basis; operational design principle | Exceeds requirements |
| Contestation resistance | No direct regulatory basis; governance-hardening measure | Exceeds requirements |

### Regulations not yet mapped but potentially relevant

| Regulation | Relevance | Action |
|---|---|---|
| Seveso III (Dir. 2012/18/EU) | Upper/lower-tier establishments: safety management systems, operator competence requirements | Investigate if OT/ICS scope includes Seveso establishments |
| Cyber Resilience Act (Reg. 2024/2847) | Products with digital elements: vulnerability handling, incident reporting | Relevant if operator controls embedded digital products |
| GDPR (Reg. 2016/679) | Decision logs may contain personal data; H-state assessments are health-adjacent data | Data protection impact assessment recommended for deployments |

## 8 — Confidence notes

- EU AI Act Art. 14 mapping: verified against primary text [F,90].
- NIS2 Art. 21(2) sub-paragraph mappings: verified against primary text [F,90].
- CER Art. 13 and Art. 14 mappings: verified against primary text [F,90].
- DORA Art. 11 mapping: verified against primary text [F,85].
- Machinery Regulation Annex III references: based on regulatory knowledge, not machine-verified [S,75].
- Seveso III: not verified; regulation not available in tool database [S,60].
- All mappings are indicative. Formal legal assessment required per deployment context.

## 9 — Methodology

This cross-reference was produced by:
1. Extracting all regulatory claims from `policies/POL-OR-01-operator-governance.md` and `README.md`
2. Retrieving full article text from EU regulation database for AI Act Arts. 9, 14, 26; NIS2 Art. 21; CER Arts. 13–14; DORA Art. 11
3. Searching across all available EU regulations for terms relevant to operator governance (human oversight, operator authority, crisis management, personnel security, safe state, duress)
4. Comparing claimed descriptions against actual legislative text
5. Identifying missing mappings by regulatory relevance to repository scope

Cross-reference date: 2026-03-23. Regulations current as of database state at time of analysis.
