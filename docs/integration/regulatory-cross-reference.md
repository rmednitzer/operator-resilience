# Regulatory Cross-Reference

**Date:** 2026-03-28
**Status:** DRAFT
**Scope:** Indicative mapping of operator-resilience controls to EU, NATO, and international regulatory requirements. Applicability depends on sector, entity classification, and deployment context.

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
| Seveso III (Dir. 2012/18/EU) | Upper/lower-tier hazardous substance establishments | Substance thresholds per Annex I |
| EU Working Time Directive (Dir. 2003/88/EC) | All employment contexts, on-call operators | Applies to operator duty scheduling and rest requirements |
| CRA (Reg. 2024/2847) | Products with digital elements placed on EU market | Product scope; application date 2027-12-11 |
| GDPR (Reg. 2016/679) | All EU-based organisations processing personal data | Decision logs and H-state assessments may contain personal/health data |
| MIL-STD-882E | Defence/military systems | Contract or policy requirement |
| DoD Directive 3000.09 | Autonomous weapon systems | US DoD context |
| NATO STANAG 4670 / ATP-3.3.7 | UAS operator training (NATO members) | For UAS operations requiring NATO interoperability |
| NATO STANAG 7201 | Human engineering test and evaluation | Applied to systems development for NATO entities |
| NATO HFM-322 | Meaningful human control in AI-based systems | Policy framework for NATO defence applications |

> **Confidence notes:** All EU regulation numbers, dates, and article references verified against official EUR-Lex text [F,90]. NATO standards based on STO publications [S,80]. All dates current as of 2026-03-28.

## 2 — EU AI Act (Regulation 2024/1689)

Entry into force: 1 August 2024. Staggered application: Chapters I–II from 2 February 2025; Chapter V (GPAI) from 2 August 2025; high-risk system regime from 2 August 2026; Annex I Section B systems from 2 August 2027.

### Art. 9 — Risk management system

| AI Act provision | Repository control | Alignment |
|---|---|---|
| Art. 9(2): continuous iterative risk management | Exercise program with defined cadences; post-event review loop; CACE principle | Direct |
| Art. 9(5)(c): training to deployers | Exercise types; cybersecurity training mapping | Supportive |

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

## 3 — NIS2 (Directive 2022/2555)

Transposition deadline 2024-10-17. Applies to essential and important entities in scope sectors (Annexes I–II).

### Art. 21 — Cybersecurity risk-management measures

| NIS2 provision | Actual text | Repository control | Alignment |
|---|---|---|---|
| Art. 21(2)(a) | "policies on risk analysis and information system security" | Policy stmts 1–4; OADC as a security policy governing operator authority | Direct |
| Art. 21(2)(b) | "incident handling" | Policy stmts 7–9; mandatory handoff; post-event review | Direct |
| Art. 21(2)(c) | "business continuity, such as backup management and disaster recovery, and crisis management" | Safe-state specification; handoff protocol; operator-absent safe state | Partial — crisis management addressed; backup/disaster recovery out of scope |
| Art. 21(2)(f) | "policies and procedures to assess the effectiveness of cybersecurity risk-management measures" | Exercise program with acceptance criteria; controls not exercised assumed non-functional | Direct |
| Art. 21(2)(g) | "basic cyber hygiene practices and cybersecurity training" | Exercise program; duress protocol training; epistemic check training | Partial — cybersecurity training addressed; basic cyber hygiene broader than operator resilience |
| Art. 21(2)(i) | "human resources security, access control policies and asset management" | OADC system enforcement (two-person auth, session timeout, time-of-day awareness); roles and responsibilities | Direct — OADC enforces access control degradation; HR security via return-to-duty protocol |
| Art. 21(2)(j) | "multi-factor authentication or continuous authentication solutions, secured voice, video and text communications" | OADC: communication from unverified authority → hold and authenticate via second channel; incident comms security (closed-loop protocol) | Partial — authentication and comms security addressed at protocol level |

### Art. 23 — Reporting of incidents

| NIS2 provision | Repository control | Alignment |
|---|---|---|
| Art. 23(4)(a): early warning within 24 hours of becoming aware of significant incident | OADC trigger events and evidence logs produce timestamped data that supports early-warning reports | Supportive — this repo provides the evidence; external notification to competent authorities is the deploying organisation's responsibility |
| Art. 23(4)(b): incident notification without undue delay, within 72 hours | Post-event review; decision logs; H-state assessment records | Supportive — evidence pipeline provides structured data for incident notification; the notification procedure itself is out of scope |

**Recital 79:** Explicitly calls for "human resources security" and "appropriate access control policies" as part of cybersecurity risk management. The OADC is an operationalisation of access control that degrades with operator state — a refinement beyond static RBAC.

## 4 — CER (Directive 2022/2557)

Critical Entities Resilience Directive. Transposition deadline 2024-10-17.

### Art. 13 — Resilience measures of critical entities

| CER provision | Repository control | Alignment |
|---|---|---|
| Art. 13(1)(c): respond to, resist and mitigate incidents; risk and crisis management procedures | OADC condition taxonomy; crisis management via safe-state and handoff | Direct |
| Art. 13(1)(e): adequate employee security management — categories of personnel exercising critical functions, access rights, background checks, training | Roles and responsibilities; OADC applies to "all operators in roles where their decisions can cause or fail to prevent a high-consequence outcome"; exercise program | Direct — OADC categorises operator authority by criticality |
| Art. 13(1)(f): raise awareness among relevant personnel; training, exercises | Exercise program (seven types with cadences); acceptance criteria | Direct |
| Art. 13(2): resilience plan or equivalent documents | This repository as a whole constitutes the resilience plan for operator governance | Structural |

### Art. 14 — Background checks for critical function personnel

CER Art. 14 permits critical entities to request background checks for personnel in critical functions, subject to proportionality and Member State implementation. **Conditional** — applicable where operators are designated as exercising critical functions under CER.

## 5 — DORA (Regulation 2022/2554)

Digital Operational Resilience Act. Application date: 17 January 2025. Financial sector only.

### Art. 11 — Response and recovery

| DORA provision | Repository control | Alignment |
|---|---|---|
| Art. 11(2)(e): communication and crisis management actions | OADC: incident comms security; closed-loop protocol | Supportive |
| Art. 11(6)(a): test ICT business continuity plans yearly | Exercise program: annual cadence minimum for all control types | Direct alignment on testing cadence |
| Art. 11(7): crisis management function | OADC condition: organisational stress; incident commander role | Structural analogy |

## 6 — Machinery Regulation (Regulation 2023/1230)

Applies from 2027-01-20. Relevant for OT/ICS contexts. Military and police machinery excluded (Art. 2(2)(l)).

| Provision | Repository control | Alignment |
|---|---|---|
| Annex III §1.2.4.3: Emergency stop [F,90] | Safe-state specification; OADC §6 | Structural — safe state maps to emergency stop / safe halt |
| Annex III §1.1.6: Ergonomics, operator fatigue, mental overload [F,90] | H-state table; circadian adjustment; OADC duty duration limits | Direct — OADC operationalises operator capacity constraints |

## 7 — EU Working Time Directive (Directive 2003/88/EC)

Establishes minimum daily rest (11 hours), weekly rest (24 hours), maximum weekly working time (48 hours), and night-work limits. Directly affects operator duty scheduling for control rooms and extended on-call operations.

| Provision | Repository control | Alignment |
|---|---|---|
| Art. 3: minimum 11 hours daily rest | OADC condition: on-call duration > N hours; minimum rest before re-assuming authority | Direct |
| Art. 5: minimum 24 hours weekly rest | Policy stmt 2: OADC parameters set in advance, including duty rotation | Supportive |
| Art. 6: maximum 48 hours per week averaged | OADC: on-call limits (typically 8–12 hours per shift) | Direct — schedule design must respect this ceiling |
| Art. 8: special protections for night work (22:00–06:00 or 23:00–07:00) | OADC condition: circadian low (02:00–06:00); treat as one H-state worse | Direct — night-work fatigue is operationalised as H-state degradation |

**Note:** On-call time at the workplace counts as working time per CJEU case law. Sector-specific derogations (aviation, maritime, rail) may apply; verify in deployment context.

## 8 — CRA (Regulation 2024/2847)

Cyber Resilience Act. Entry into force: December 2024. Main application date: 2027-12-11. Article 14 vulnerability reporting: 2026-09-11. CAB provisions: 2026-06-11.

**Applicability:** Only where autonomous platform or subsystem is a product with digital elements placed on the EU market and not excluded by sectoral carve-outs.

| Requirement area | Repository control | Alignment |
|---|---|---|
| Secure-by-design properties | Hostile-environment security controls, secure update, anti-tamper | Supportive (if platform is in-scope product) |
| Vulnerability handling | Incident-response checklist and evidence requirements | Supportive — incident response logs feed evidence pipeline |
| Technical documentation | Threat register, architecture docs, and generated registers | Supportive — supports conformity demonstration |

**Gap:** CRA applicability is programme-specific and must be evaluated by the deploying organisation's product compliance lead before EU market placement.

## 9 — GDPR (Regulation 2016/679)

Applies to all organisations processing personal data of EU residents.

| Requirement area | Repository control | Alignment |
|---|---|---|
| Art. 4(1): definition of personal data | Decision logs may contain operator identifiers; H-state assessments may contain health-adjacent data | Conditional — GDPR applies to identified and identifiable natural persons; even pseudonymised decision logs are personal data if re-identification is reasonably possible |
| Art. 6: lawful basis for processing | Policy stmt 3: epistemic checks require logging assumptions and confidence; lawful basis must be established per GDPR Art. 6 | Direct — operator authority and H-state data processing require legal basis (likely Art. 6(1)(f) legitimate interest or Art. 6(1)(c) legal obligation, depending on sector) |
| Art. 9: special categories of personal data | H-state assessments (fatigue, cognitive state) are health-adjacent data | Conditional — H-state data may qualify as health data under Art. 4(15); if so, Art. 9(2) exemption required (e.g. Art. 9(2)(b) employment obligations or Art. 9(2)(g) substantial public interest) |
| Art. 32: security of processing | OADC enforcement and evidence integrity controls | Supportive — technical and organisational measures for confidentiality, integrity, availability |

**Gap:** Formal DPIA (Data Protection Impact Assessment) required for operator decision logs and H-state registers before operational deployment. Not addressed in this repository.

## 10 — Seveso III (Directive 2012/18/EU)

Applies to upper-tier and lower-tier establishments handling hazardous substances above threshold quantities.

| Requirement area | Repository control | Alignment |
|---|---|---|
| Art. 8: Major-Accident Prevention Policy (MAPP) and Safety Management System | This repository; OADC and exercise program constitute operator-level governance | Partial — repo covers operator governance; MAPP is broader |
| Art. 10: Safety report (upper-tier) | Post-event review; incident documentation | Supportive — evidence pipeline feeds safety case |
| Art. 12: Emergency plans | Duress protocols; safe-state specification | Supportive — safe halt is part of emergency response |

**Note:** Applicability conditional on whether operator controls critical functions in Seveso establishments. If applicable, this repo's controls operationalise Seveso's "human reliability" requirements.

## 11 — MIL-STD-882E (System Safety Standard)

Standard for system safety in defence/military contexts.

| Requirement area | Repository control | Alignment |
|---|---|---|
| Task 204: Operating and support hazard analysis | STPA-informed hazard analysis for operator-as-controller | Direct |
| Task 301: Safety verification (includes hazard tracking, risk acceptance records) | Exercise program; post-event review; evidence pipeline | Direct — control verification requires exercise and review |
| Task 401: Safety assessment [**Correction:** previously mislabelled in this repo as "accountability/logging"] | Mission safety case; hazard register; evidence pipeline | Direct — documents that safety controls are adequately implemented |
| General requirement: Documentation and traceability | Decision logs; OADC trigger logs; H-state assessment records | Direct — operator-resilience controls produce traceable evidence |

**Note:** Change 1 issued 27 September 2023. Verify current edition for specific requirements.

## 12 — DoD Directive 3000.09 (Autonomy in Weapon Systems)

Updated January 2023.

| Requirement area | Repository control | Alignment |
|---|---|---|
| **Appropriate levels of human judgment over the use of force** [**Correction:** Directive uses this term, not "meaningful human control" — that terminology derives from academic/policy discourse; see NATO HFM-322 below for the broader MHC framework] | OADC: operator authority hierarchy with degradation conditions | Direct |
| Transparency and explainability of autonomous-system decisions | Epistemic provenance model ([F]/[I]/[S] tagging); decision logs | Direct |
| Auditability and accountability | All OADC triggers and decisions logged as evidence | Direct |

**Note:** The distinction matters: DoD Directive 3000.09 uses "appropriate levels of human judgment"; the broader policy concept of "meaningful human control" (used in NATO HFM-322, CCW discussions, and academic literature) is a related but distinct governance framework.

## 13 — NATO STANAG 4670 / ATP-3.3.7 (UAS Operator Training Standards)

Joint Unmanned Aircraft System Minimum Training Standards (JUMTS).

| Requirement area | Repository control | Alignment |
|---|---|---|
| Minimum training requirements for UAS operators and pilots | Exercise program; return-to-duty protocol; competency checks | Direct — operator qualification must meet STANAG 4670 if NATO interoperability required |
| Training content (systems knowledge, emergency procedures, decision-making under stress) | Duress protocols; exercise types; stress-adapted decision aids | Supportive |

**Applicability:** Conditional on NATO interoperability requirement. Ratification status varies by Member State as of March 2026.

## 14 — NATO STANAG 7201 (Human Engineering Test and Evaluation Procedures)

NATO standard for human engineering test and evaluation in systems development.

| Requirement area | Repository control | Alignment |
|---|---|---|
| Systematic evaluation of human-system interfaces | HAT assurance; pre-incident readiness checklist | Direct — OADC and H-state controls must be validated through structured evaluation |
| Error analysis and critical task analysis | Decision logs; post-event review; STPA-informed hazard analysis | Supportive |
| Cognitive workload assessment | H-state table; OADC duty duration limits | Direct — mental workload degradation is operationalised in H-state taxonomy |

## 15 — NATO HFM-322 (Meaningful Human Control in AI-Based Systems)

NATO STO HFM-322 workshop series and task group outputs (2025–2026).

| Requirement area | Repository control | Alignment |
|---|---|---|
| Framework for meaningful human control (MHC) in AI-based systems | OADC as the operationalisation of MHC at the operator level | Direct — MHC requires authority contracts, override capability, monitoring, and auditability — all present in OADC |
| Human factors in AI governance | H-state table; epistemic provenance; stress-adapted decision aids | Direct |
| Accountability and transparency | Decision logs; evidence pipeline; post-event review | Direct |

**Note:** HFM-322 complements DoD 3000.09 by providing human-factors depth to the "appropriate levels of human judgment" requirement. The repo's OADC is aligned with both frameworks.

## 16 — ISO 10075 Series (Ergonomic Principles Related to Mental Workload)

International standard for mental workload in work systems.

| Part | Relevance | Alignment |
|------|-----------|-----------|
| ISO 10075-1:2017 (General concepts and terms) | Defines mental workload, mental fatigue, mental strain | Core to H-state assessment taxonomy |
| ISO 10075-2:2024 (Design principles) | Design guidance to reduce mental overload; explicitly covers robotics and autonomous systems | Directly relevant to OADC design and H-state degradation triggers |
| ISO 10075-3:2004 (Measurement and assessment) | Methods for assessing mental workload in operational tasks | Applicable to exercise program evaluation and H-state validation |

**Alignment:** The H-state table (H-0 to H-4) is an operationalisation of mental-workload levels per ISO 10075.

## 17 — ISO 11064 Series (Ergonomic Design of Control Centres)

International standard for control-centre design for safety-critical systems.

| Part | Relevance | Alignment |
|------|-----------|-----------|
| ISO 11064-1:2024 (Principles and design process) | Principles for human-centred control-centre design | Applicable to GCS design for autonomous platforms |
| ISO 11064-2:2024 (Environmental conditions) | Physical environment design (lighting, noise, climate) | Relevant to operator fatigue management |
| ISO 11064-3:2024 (Display systems) | Information presentation and human-machine interfaces | Relevant to epistemic integrity and decision support |
| ISO 11064-5:2024 (Workstation design) | Ergonomic design of control-station workplaces | Supportive for sustained operations |

**Alignment:** The repo's operator-absent safe state and pre-incident readiness checklist assume GCS design aligned with ISO 11064.

## 18 — IEC 62443 Series (Industrial Cybersecurity for IACS)

International standard for operational-technology cybersecurity.

| Requirement area | Repository control | Alignment |
|---|---|---|
| Zone-based architecture and defence-in-depth | OADC enforcement via technical controls (two-person auth gates, session timeout) | Supportive — OADC provides human-level access control that complements technical zones |
| Security levels (SL) allocation | Exercise program validates controls on defined cadences; untested controls assumed non-functional | Supportive — operational validation aligns with IEC 62443 SL methodology |
| Incident response | Post-event review; duress protocols; H-state assessment | Supportive |

**Note:** IEC 62443 is referenced in autonomous-platform-assurance for UGVs with industrial comms. The operator-resilience repo's human-side controls complement IEC 62443's technology-side controls.

## 19 — Gaps and recommendations

### Controls with no direct EU regulatory mapping

| Repository control | Potential EU basis | Status |
|---|---|---|
| Duress protocols | No specific EU article; general duty of care under employment law; insider threat dimension under CER Art. 13(1)(e) | Gap — consider scoping note in CER context |
| Epistemic provenance model ([F]/[I]/[S] tagging) | Supports AI Act Art. 14(4)(a)–(c) in practice; no standalone requirement | Exceeds requirements — best practice |
| CACE (Changing Anything Changes Everything) principle | No direct regulatory basis; operational design principle | Exceeds requirements — architectural hardening |
| Contestation resistance | No direct regulatory basis; governance-hardening measure | Exceeds requirements — novel control |

### Regulations relevant to operator governance but programme-scope dependent

| Regulation | Relevance | Action |
|---|---|---|
| **EU Product Liability Directive (Dir. 2024/2853)** | Disclosure-of-evidence and presumption-of-defectiveness provisions require robust field-evidence chains (relevant if operator decisions affect product liability exposure). Unlike Machinery Reg and AI Act, PLD has no explicit military/defence exclusion. | Conditional — programme legal team must assess if operator decisions trigger PLD Art. 7 defectiveness analysis; military products may still be in scope |
| **EASA Regulation 965/2012 (Part-ORO.FTL)** | Fatigue risk management for aircrew on commercial operations; prescribes daily rest, weekly rest, and duty-time limits stricter than EU Working Time Directive | Conditional — applies if autonomous platform operates under EASA certification with human crew |
| **ISO 27001/27002** | Information security management systems; baseline for security-control frameworks | Recommended — OADC enforces access control degradation, complementary to ISO 27001 ISMS |
| **ISO 9241-210:2019** | Human-centred design for interactive systems | Recommended for HAT interface design validation |
| **EU Dual-Use Regulation (Reg. 2021/821)** | Export controls on technology and software; applies to derived governance deliverables intended for transfer outside EU | Conditional — programme export-compliance authority must assess each derived deliverable |

## 20 — Methodology and confidence

This cross-reference was produced by:

1. Extracting regulatory claims from all governance documents in the operator-resilience repository
2. Retrieving full article text from EUR-Lex for EU regulations (verified against official consolidated texts)
3. Searching for operator-governance-relevant standards (NATO STANAGs, ISO/IEC, MIL-STD-882E, DoD Directive 3000.09)
4. Comparing claimed descriptions against authoritative sources
5. Identifying missing mappings by relevance to operator governance in European and NATO contexts
6. Verifying all dates, article numbers, and regulatory numbers against official sources [F,90] where retrieved from primary text

**Confidence notes:**
- EU AI Act, NIS2, CER, DORA, CRA, PLD, Machinery Reg, GDPR, Seveso III: verified against EUR-Lex consolidated texts [F,90]
- EU Working Time Directive: verified against EUR-Lex [F,90]
- NATO STANAGs, HFM-322: based on STO and NATO standardisation office publications [S,80]
- MIL-STD-882E Task 401 characterisation: corrected from "accountability/logging" to "Safety assessment"; Change 1 (September 2023) noted [F,90]
- DoD Directive 3000.09: verified; terminology corrected from "meaningful human control" to "appropriate levels of human judgment over the use of force" [F,90]
- ISO standards: confirmed current editions and relevance [F,85]
- IEC 62443: confirmed as OT cybersecurity baseline [F,85]

**Cross-reference date:** 2026-03-28. All regulations current as of this date.
