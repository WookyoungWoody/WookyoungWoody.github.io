---
layout: page
title: Engineering Software
description: Thermal performance prediction tools and cross-platform apps
img: assets/img/software.jpg
importance: 4
category: tools
---

## Engineering Software Development

My software work bridges academic research and practical engineering, translating heat transfer models and thermodynamic correlations into accessible tools for field engineers and researchers. All programs below have been formally registered with the Korea Copyright Commission.

---

### Thermophysical Property App (iOS/Android)

A cross-platform mobile application for real-time thermophysical property lookup, built with React Native and powered by CoolProp/REFPROP via JavaScript/WASM compilation. Designed for field engineers who need instant access to refrigerant and working-fluid properties without a laptop. Active development as PI since 2025.

---

### PCHE Thermal Design Suite

A collection of registered software tools for printed circuit heat exchanger (PCHE) analysis and sizing:

- **PCHE Thickness Design Program** (C-2024-052179) — structural sizing under high-pressure conditions
- **100 kg/hr Hydrogen PCHE Design Program** (C-2025-056891) — tailored for hydrogen liquefaction applications
- **Lab-Scale Heat Exchanger Analysis Program** (C-2023-056463) — experimental data post-processing and correlation fitting
- **Heat Exchanger HTC Uncertainty Analysis Program** (C-2023-059071) — propagation of measurement uncertainty to heat transfer coefficients

The suite uses a Python/FastAPI backend with a React frontend, employing an effectiveness-NTU iterative solver for multi-stream design.

---

### Heat Pump Cycle Design

High-temperature heat pump cycle design program (C-2024-038691). Enables system-level sizing and optimization of industrial heat pump cycles, integrating property lookups with thermodynamic cycle analysis.

---

### Vapor Chamber Analysis

Vapor chamber performance analysis program (C-2024-041200). Models wick structure, capillary limit, and thermal resistance for vapor chamber thermal spreaders used in electronics cooling applications.

---

### Adsorption Cooling Simulation

Adsorption cooling simulation program (C-2025-034652). Simulates adsorption/desorption cycle dynamics for waste-heat-driven cooling systems, including transient bed temperature and COP prediction.

---

### Fin-Tube Heat Exchanger Design

Fin-tube heat exchanger design program (C-2024-038692). Automates rating and sizing of fin-tube coils using empirical correlations for air-side and refrigerant-side heat transfer.

---

## Technology Stack

| Layer | Technologies |
|---|---|
| Backend | Python, FastAPI, CoolProp, REFPROP |
| Frontend | React, React Native |
| Numerical | Effectiveness-NTU, thermal network modeling |
| AI/ML | PyTorch, JAX, Physics-Informed Neural Networks, LLM agents |
| DevOps | Git/GitHub, Linux, CMake, Docker |

---

## Registered Software (Korea Copyright Commission)

| Program | Registration No. | Year |
|---|---|---|
| Lab-Scale Heat Exchanger Analysis | C-2023-056463 | 2023 |
| HTC Uncertainty Analysis | C-2023-059071 | 2023 |
| High-Temp Heat Pump Cycle Design | C-2024-038691 | 2024 |
| Fin-Tube HX Design | C-2024-038692 | 2024 |
| Vapor Chamber Performance Analysis | C-2024-041200 | 2024 |
| PCHE Thickness Design | C-2024-052179 | 2024 |
| 100 kg/hr Hydrogen PCHE Design | C-2025-056891 | 2025 |
| Adsorption Cooling Simulation | C-2025-034652 | 2025 |

---

## Related Technology Transfers

- **Heat Pipe and Vapor Chamber Structural Design for Electronics Cooling** — fabrication-ready design methodology transferred to industry partners
- **Micro-Channel Bonding and Fabrication Techniques for Heat Exchangers** — joining and sealing processes for PCHE and micro-channel devices

