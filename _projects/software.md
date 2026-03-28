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

### KIMMPROP — Thermophysical Property App

<div style="display:flex; align-items:flex-start; gap:2rem; flex-wrap:wrap; margin-bottom:1rem;">
  <div style="flex:1; min-width:220px;">
    <p>
      A cross-platform mobile application for real-time thermophysical property lookup, built with React Native and powered by CoolProp/REFPROP via JavaScript/WASM compilation. Designed for field engineers who need instant access to refrigerant and working-fluid properties without a laptop.
    </p>
    <p>Available on iOS and Android. Active development as PI since 2025.</p>
    <div style="display:flex; gap:0.75rem; flex-wrap:wrap; margin-top:1rem;">
      <a href="https://apps.apple.com/kr/app/kimmprop/id6745596456" target="_blank" rel="noopener"
         style="display:inline-flex; align-items:center; gap:0.4rem; background:#000; color:#fff; padding:0.5rem 1rem; border-radius:8px; text-decoration:none; font-size:0.9rem; font-weight:600;">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 814 1000" fill="white"><path d="M788.1 340.9c-5.8 4.5-108.2 62.2-108.2 190.5 0 148.4 130.3 200.9 134.2 202.2-.6 3.2-20.7 71.9-68.7 141.9-42.8 61.6-87.5 123.1-155.5 123.1s-85.5-39.5-164-39.5c-76 0-103.7 40.8-165.9 40.8s-105-57.8-155.5-127.4C46 790.7 0 663 0 541.8c0-207.5 135.4-317.1 268.1-317.1 36.5-2.1 71.9 13.9 97.2 23.8 23.5 8.5 91.1 33.3 100.8 33.3 18.1 0 72.9-19.2 103.7-33.3 17.4-7.4 52.2-21.2 85.6-20.9l-0.4 0.3zm-170.3-171.8c36.5-43.9 94.1-79.5 152-79.5 6.5 54.9-19.4 109.8-54.9 148.4-36.5 38.5-89.9 72.5-147.8 67.7-7.4-52.2 19.4-107.1 50.7-136.6z"/></svg>
        App Store
      </a>
      <a href="https://play.google.com/store/apps/details?id=com.kimmprop_v03&pcampaignid=web_share" target="_blank" rel="noopener"
         style="display:inline-flex; align-items:center; gap:0.4rem; background:#01875f; color:#fff; padding:0.5rem 1rem; border-radius:8px; text-decoration:none; font-size:0.9rem; font-weight:600;">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" fill="white"><path d="M325.3 234.3L104.6 13l280.8 161.2-60.1 60.1zM47 0C34 6.8 25.3 19.2 25.3 35.3v441.3c0 16.1 8.7 28.5 21.7 35.3l2.7 1.5 247.2-247v-5.8L47 0zm432 218.9L373.1 167 311.7 228.5l61.5 61.5 105.7-60.8c-12.9-7.7-12.9-27.4 0-10.3zM104.6 499l280.8-161.2-60.1-60.1L104.6 499z"/></svg>
        Google Play
      </a>
    </div>
  </div>
  <div style="display:flex; gap:1.5rem; flex-wrap:wrap;">
    <div style="text-align:center;">
      <img src="/assets/img/kimmprop_ios_qr.png" alt="KIMMPROP iOS QR Code" width="130" height="130" style="border:1px solid #ddd; border-radius:4px; display:block; margin:0 auto 0.3rem;">
      <small style="color:#666; font-size:0.75rem;">Scan for iOS</small>
    </div>
    <div style="text-align:center;">
      <img src="/assets/img/kimmprop_android_qr.png" alt="KIMMPROP Android QR Code" width="130" height="130" style="border:1px solid #ddd; border-radius:4px; display:block; margin:0 auto 0.3rem;">
      <small style="color:#666; font-size:0.75rem;">Scan for Android</small>
    </div>
  </div>
</div>

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

