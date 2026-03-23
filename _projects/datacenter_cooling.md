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

Cold plate systems are designed and tested for all major heat-generating components: CPUs, GPUs, RAM modules, and SSDs. Research includes thermal interface material (TIM) selection and optimization, micro-channel cold plate geometry, and system-level coolant loop design. The goal is to achieve component junction temperatures within safe operating limits while minimizing coolant flow rate and pump power.

### Waste Heat Utilization

Since 2025 (Lead), this project investigates recovering the thermal energy rejected by immersion cooling systems for beneficial reuse—space heating, process heat, or absorption cooling. Active thermal management strategies are developed to maintain stable coolant supply temperatures while maximizing recoverable heat quantity and quality. Integration with building HVAC systems is a key design target.

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

## Collaborators

- KIMM Heat Pump Research Center

## Funding

This research is supported by government-funded projects through national R&D programs targeting next-generation thermal management and energy-efficient data center infrastructure.

