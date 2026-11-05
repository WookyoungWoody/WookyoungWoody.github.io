---
layout: page
title: PCHE for Liquid Hydrogen
description: Printed Circuit Heat Exchanger design and testing for cryogenic applications
img: assets/img/pche.jpg
importance: 2
category: current
---

{% include projects/thrust_projects.liquid thrust="hydrogen" level="h3" %}

## Compact Heat Exchanger for Liquid Hydrogen

The global hydrogen economy requires reliable cryogenic infrastructure for transporting and utilizing liquid hydrogen (LH2) at -253°C. Printed Circuit Heat Exchangers (PCHEs), fabricated by photo-chemically etching micro-channels into metal plates and diffusion bonding them into a monolithic block, are well suited for these extreme conditions due to their high surface area density, mechanical integrity under high pressure, and compact form factor. This project develops PCHE design technology for LH2 vaporization and supply systems, with design targets of operation down to -220°C at pressures up to 100 MPa.

---

### Research Areas

#### PCHE Design for LH2 Vaporizer

This project focuses on developing lab-scale PCHEs for liquid hydrogen supply systems. Design work centers on SUS 316L stainless steel plates with multiple semicircular and straight channel configurations, optimized for thermal performance under cryogenic conditions. Cryogenic test facilities capable of supercritical hydrogen and nitrogen operation have been constructed for performance characterization. Nitrogen tests have reached -185°C at 21 MPa; -220°C and 100 MPa remain design targets.

#### Freezing Phenomena Investigation

When a liquid heat-source fluid (for example, glycol water) vaporizes a cryogenic fluid such as liquid hydrogen, the heat-source liquid can freeze in the PCHE hot channels, blocking flow and degrading performance. This research identifies the freezing conditions and the operating conditions that avoid them. In lab-scale tests, liquid nitrogen flows in the cold channels and glycol water in the hot channels, and a contour map of the cold-to-hot mass flow rate ratio defines the region where freezing is avoided. Conjugate heat transfer analysis complements the experiments, which have produced validated datasets for model development.

#### PCHE Design Software

A Python-based PCHE performance prediction tool has been developed and officially registered as software intellectual property. The solver implements the effectiveness-NTU method with custom Nusselt number correlations derived from experimental data, enabling rapid design iteration for cryogenic heat exchanger configurations. Registered software: C-2024-052179, C-2023-056463, C-2025-056891.

---

### Key Achievements

- Lab-scale PCHE design using SUS 316L plates with semicircular and straight channel geometries
- Thermal resistance models and Nusselt number correlations validated for cryogenic conditions
- Freezing conditions of the heat-source liquid identified, with a cold/hot mass flow rate ratio map that avoids freezing
- Cryogenic test facility for supercritical hydrogen and nitrogen designed and built; nitrogen tests to -185°C at 21 MPa
- 700 bar structural design and 2000 bar pressure test facility operation
- PCHE diffusion bonding fabrication process established
- Python-based PCHE design software developed and registered (3 software registrations)

---

{% include projects/thrust_transfers.liquid thrust="hydrogen" level="h3" %}

### Related Publications

<div class="publications">

{% bibliography --query @*[key=kim2026pche_scaleup], @*[key=kim2025freezing], @*[key=kim2024icec], @*[key=kim2024kci_pche_freezing], @*[key=sohn2022kci_pche_icing] %}

</div>

---

### Related Patents

- Heat exchanger with anti-freezing capability (1): KR Patent (2023)
- Heat exchanger with anti-freezing capability (2): KR Patent (2023)
- Heat exchanger thermal performance testing apparatus: KR Patent (2023)
- Tray structure for heat exchanger: KR Patent (2022)
- Micro-channel reactor: KR Patent (2023)

---

### Funding

This project is supported by government-funded hydrogen economy programs under the Korean Ministry of Science and ICT and the Ministry of Trade, Industry and Energy, as part of national initiatives to advance hydrogen infrastructure technology.
