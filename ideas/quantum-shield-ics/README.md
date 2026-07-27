<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

[ 🇫🇷 Version Française ](./README.fr.md)

# Quantum-Shield ICS

> **Executive Summary:** Development of a hardened “Bump-in-the-Wire” hardware appliance (PQC proxy) for industry (DIN rail, fanless) and/or ultra-optimized cryptographic acceleration firmware. This system physically inserts itself in front of vulnerable PLCs, intercepts traditional network traffic, and establishes an encrypted tunnel resistant to quantum attacks (using for example a Kyber/Dilithium hybrid optimized for embedded) with a central orchestrator. It encapsulates the data without disrupting the native ICS protocol (Modbus, DNP3, OPC UA).

![Type: Model](https://img.shields.io/badge/Model-B2B-blue)
![Target: 100k ARR](https://img.shields.io/badge/ARR_Target-100k%E2%82%AC-green)
![Score: Pending](https://img.shields.io/badge/Composite_Score-Pending-yellow)

---

## 1. Visual Overview & Wow Effect

```mermaid
graph TD
    %% Problem vs Solution or Architecture Diagram
    Problem["Current State"] --> Solution["Quantum-Shield ICS State"]
```

## 2. Contrarian Thesis (Peter Thiel Style)

**Popular Belief:** General AI solutions can solve this problem.

**Hidden Truth:** A SaaS or LLM API can do absolutely nothing for isolated on-premise equipment, often air-gapped or on closed OT (Operational Technology) networks. Classic software solutions (standard PQC VPNs) require computing resources that PLCs from the 90s/2000s simply do not have. This is a low-level integration problem (OSI network layers 2 to 4) coupled with deterministic (real-time) latency constraints.

## 3. Problem & Target Market

**Business Model:** B2B

**Target Audience:** Operators of Vital Infrastructure (OIV), electricity network managers, water treatment plants, heavy manufacturing industry. The budget is held by the CISO/Industrial CISO and the Chief Operations Officer (COO).

**Urgent Pain Point:** Industrial control systems (ICS/SCADA) use traditional encryption protocols (RSA, ECC) to secure communications. These systems have lifespans of 15 to 30 years and are extremely difficult to update. The “Harvest Now, Decrypt Later” (HNDL) threat threatens critical data exchanged today. Within a few years, quantum computers will break these ciphers. Replacing all SCADA hardware costs billions, and the NIST-standardized Post-Quantum Cryptography (PQC) algorithms are too heavy (in CPU and key/signature size) to run natively on old programmable logic controllers (PLCs).

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

**Moat (Defensibility):** Hardware development requires high CAPEX and time (CE/UL/IEC 62443 industrial certification). The acceptance by manufacturers of placing a third-party "black box" in their critical control loop is a major commercial challenge. Dependence on final developments in NIST and ANSSI standards.

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
