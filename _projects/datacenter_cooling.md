---
layout: page
title: Data Center Cooling
description: Immersion cooling and direct liquid cooling for next-generation high-heat-density servers
img: assets/img/datacenter.jpg
importance: 1
category: current
---

## Overview

The rapid expansion of AI/ML workloads has pushed chip thermal design power beyond 1000 W per device, rendering conventional air cooling insufficient for modern hyperscale and edge data centers. Power Usage Effectiveness (PUE) has become a critical metric, and liquid-based cooling strategies are now essential to sustaining computational density growth. This research develops and validates advanced liquid cooling technologies—immersion cooling, direct liquid cooling, and waste heat recovery—to address these thermal challenges.

## Research Areas

### Jet-Enhanced Immersion Cooling

Since 2025 (PI), this project focuses on jet-impingement immersion cooling for next-generation high-heat-density servers. Pressurized dielectric fluid jets are directed at chip surfaces within an immersion tank, significantly enhancing local heat transfer coefficients compared to passive single-phase or two-phase immersion. Custom test rigs operate with real CPU and GPU server hardware under controlled stress-test conditions to characterize thermal performance and stability.

### Direct Liquid Cooling (DLC)

Since 2026 (Lead), this project develops direct-to-chip (DTC) cold plate cooling for the dominant heat sources in AI servers: CPUs and GPUs. Both single-phase and two-phase DTC modes are developed and tested, with system targets of **300 kW per rack** and **3 kW per chip**. Research covers thermal interface material (TIM) selection and optimization, micro-channel cold plate geometry, and system-level coolant loop design, holding junction temperatures within safe operating limits while minimizing coolant flow rate and pump power.

### Two-Phase Cold Plate Design Guidelines

Since 2026 (PI), funded by the UST Next-Generation Leader Development Program, this project trains a Ph.D. student while resolving where conventional boiling correlations stop predicting two-phase cold plate performance as channels shrink from mini- to micro-scale. Low-GWP refrigerants (R1233zd(E), R1234ze(E), R1234yf) are tested on the same rig, and a visualization test section, with a transparent cover replacing the manifold side only, shows the internal flow in the transition range. Thermal resistance, pressure drop, and outlet quality are reduced to design-selection criteria for fin geometry, flow distribution, and refrigerant choice.

### Waste Heat Utilization

Since 2025 (Lead), this project turns the low-grade heat rejected by data center cooling loops, typically around 50 °C, back into useful energy. The primary route is **adsorption** cooling: an adsorption chiller driven by that waste heat produces chilled water, recycling the rejected heat back into the cooling supply. Where an application calls for heat rather than cooling, the same stream is instead temperature-boosted and delivered as space or process heating. Active thermal management strategies maintain stable coolant supply temperatures while maximizing recoverable heat quantity and quality, with integration into building HVAC systems as a key design target.

## Key Achievements

- Designed and fabricated immersion cooling test rigs for server-level systems (1U/2U form factors)
- Demonstrated reduced PUE through integrated liquid cooling and waste heat recovery loops
- Designed direct liquid cooling (DLC) cold plates for high-heat chips (CPU/GPU/RAM/SSD)
- Developed high-heat chip stress test apparatus for repeatable thermal performance characterization
- Conducted dielectric fluid-based thermal performance testing across multiple fluid candidates
- Benchmarked immersion cooling against air cooling for battery pack thermal management

## Related Publications

{% bibliography --query @*[key=kim2023kci_battery] %}

## Related Patents

- **Immersion Cooling Device** (2024) — Patent on immersion tank and jet-impingement hardware design
- **Immersion Cooling HVAC System and Method** (2022) — Patent on integrating immersion cooling with building HVAC for waste heat recovery
- **Immersion Cooling System for Data Centers** (2024) — Patent on a dielectric fluid loop with multiple storage tanks and valve-controlled connecting lines between the immersion chamber and the cooler
- **Fire-Suppression Cooling System for Data Centers** (2024) — Patent on using the immersion dielectric fluid to suppress fires in air-cooled and immersion-cooled data center halls
- **Multi-Thermal Management Device and Method for Immersion Cooling Tanks** (2024) — Patent on two-stage cooling of the tank working fluid, first against a heat-use loop and then a cooler, with a bypass line back to the tank

## Collaborators

- KIMM Heat Pump Research Center

## Funding

This research is supported by government-funded projects through national R&D programs targeting next-generation thermal management and energy-efficient data center infrastructure.
