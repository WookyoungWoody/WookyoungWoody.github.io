---
layout: page
title: PCHE for Liquid Hydrogen
description: Printed Circuit Heat Exchanger design and testing for cryogenic applications
img: assets/img/pche.jpg
importance: 2
category: current
---

## Compact Heat Exchanger for Liquid Hydrogen

The global hydrogen economy requires reliable cryogenic infrastructure for transporting and utilizing liquid hydrogen (LH2) at -253°C. Printed Circuit Heat Exchangers (PCHEs) — fabricated by photo-chemically etching micro-channels into metal plates and diffusion bonding them into a monolithic block — are well suited for these extreme conditions due to their high surface area density, mechanical integrity under high pressure, and compact form factor. This project develops PCHE design technology for LH2 vaporization and supply systems, targeting operation below -200°C at pressures up to 100 MPa.

---

### Research Areas

#### PCHE Design for LH2 Vaporizer

This lead project (2021–2025) focuses on developing lab-scale PCHEs for liquid hydrogen supply systems. Design work centers on SUS 316L stainless steel plates with multiple semicircular and straight channel configurations, optimized for thermal performance under cryogenic conditions. Experimental test facilities capable of operating with supercritical hydrogen and nitrogen have been constructed and validated for performance characterization across a wide range of operating conditions.

#### Freezing Phenomena Investigation

At sub-critical temperatures, residual moisture or nitrogen contamination can freeze within PCHE micro-channels, blocking flow and degrading performance. This research investigates the onset conditions for freezing (down to -220°C), develops anti-freezing channel design strategies, and performs conjugate heat transfer analysis to characterize icing behavior. Experimental campaigns on custom-built cryogenic test rigs have produced validated datasets for model development.

#### PCHE Design Software

A Python-based PCHE performance prediction tool has been developed and officially registered as software intellectual property. The solver implements the effectiveness-NTU method with custom Nusselt number correlations derived from experimental data, enabling rapid design iteration for cryogenic heat exchanger configurations. Registered software: C-2024-052179, C-2023-056463, C-2025-056891.

---

### Key Achievements

- Lab-scale PCHE design using SUS 316L plates with semicircular and straight channel geometries
- Thermal resistance models and Nusselt number correlations validated for cryogenic conditions
- Freezing onset conditions characterized experimentally down to -220°C
- Supercritical hydrogen and nitrogen test facility designed and operated
- 700 bar structural design and 2000 bar pressure test facility operation
- PCHE diffusion bonding fabrication process established
- Python-based PCHE design software developed and registered (3 software registrations)

---

### Related Publications

{% bibliography --query @*[key=kim2025freezing] %}
{% bibliography --query @*[key=kim2024icec] %}
{% bibliography --query @*[key=kim2024kci_pche_freezing] %}
{% bibliography --query @*[key=sohn2022kci_pche_icing] %}

---

### Related Patents

- Heat exchanger with anti-freezing capability (1) — KR Patent (2023)
- Heat exchanger with anti-freezing capability (2) — KR Patent (2023)
- Heat exchanger thermal performance testing apparatus — KR Patent (2023)
- Tray structure for heat exchanger — KR Patent (2022)
- Micro-channel reactor — KR Patent (2023)

---

### Collaborators

- Korea Institute of Machinery and Materials (KIMM)
- Industry partners in the domestic hydrogen supply chain

---

### Funding

This project is supported by government-funded hydrogen economy programs under the Korean Ministry of Science and ICT and the Ministry of Trade, Industry and Energy, as part of national initiatives to advance hydrogen infrastructure technology.

