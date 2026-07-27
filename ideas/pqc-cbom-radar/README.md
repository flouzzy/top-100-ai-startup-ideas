<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

[ 🇫🇷 Version Française ](./README.fr.md)

# PQC CBOM Radar

> **Executive Summary:** A static and dynamic binary analysis engine (Deep Binary Analysis) capable of generating a CBOM (Cryptographic Bill of Materials). The tool decompiles machine code and legacy firmware to detect calls to obsolete cryptographic libraries via heuristics and flow analysis, generating an accurate mapping without requiring the original source code.

![Type: Model](https://img.shields.io/badge/Model-B2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-Pending-yellow)

---

## 1. Visual Overview & Wow Effect

```mermaid
graph TD
    %% Problem vs Solution or Architecture Diagram
    Problem["Current State"] --> Solution["PQC CBOM Radar State"]
```

## 2. Contrarian Thesis (Peter Thiel Style)

**Popular Belief:** General AI solutions can solve this problem.

**Hidden Truth:** The analysis must be done on-premise (Air-Gapped) on critical industrial systems (OT) or compiled code (without source code). A traditional LLM or cloud scanner cannot analyze complex binaries, nor decipher proprietary firmware in ARM or MIPS. The IP and cryptographic data are far too sensitive to send over a third-party API.

## 3. Problem & Target Market

**Business Model:** B2B

**Target Audience:** CISO (Chief Information Security Officers) and critical infrastructure managers (Energy, Defense, Finance).

**Urgent Pain Point:** National security agencies (ANSSI, CISA, NSA) are mandating a migration to post-quantum cryptography (PQC) before 2030 to counter the “Store Now, Decrypt Later” threat. However, large companies do not know where their vulnerable keys and algorithms (RSA, ECC) are hidden in millions of lines of legacy code, industrial firmware and undocumented embedded systems. The inability to map these dependencies exposes these infrastructures to the risks of non-compliance and massive hacking.

## 4. Technical Architecture & Infrastructure

```mermaid
sequenceDiagram
    %% Sequence diagram or system flow
    User->>System: Action
    System-->>User: Response
```

## 5. Business Model & Financial Viability

| Metric                 | Value                           |
| ---------------------- | ------------------------------- |
| Pricing Structure      | SaaS subscription               |
| 12-Month Target        | 10 customers                    |
| Revenue Formula        | 10 clients \* 10k€/year = 100k€ |
| Estimated Gross Margin | 80%                             |

## 6. Distribution Engine & Moat

**Acquisition Strategy:** B2B direct sales

**Moat (Defensibility):** Extreme technical complexity of multi-architecture decompilation. Very long sales cycles (12 to 24 months) typical of critical infrastructure and governments. Dependence on definitive standardization of PQC algorithms by NIST.

## 7. Detailed Evaluation Grid

| Criterion                   | VC Score (/100) | Market Score (/100) |
| --------------------------- | --------------- | ------------------- |
| Thesis & Monopoly / Urgency | -- / 25         | -- / 25             |
| Moat / LLM Immunity         | -- / 25         | -- / 25             |
| Scalability / UX Friction   | -- / 25         | -- / 25             |
| Unit Economics / ROI        | -- / 25         | -- / 25             |
| **TOTAL**                   | **-- / 100**    | **-- / 100**        |

> **VC Verdict:** Pending evaluation.

> **Market Verdict:** Pending evaluation.
