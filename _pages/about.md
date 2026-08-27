---
layout: about
title: about
permalink: /
subtitle: Senior Researcher, <a href='https://www.kimm.re.kr'>Korea Institute of Machinery and Materials (KIMM)</a>

description: Senior Researcher at KIMM leading AI data center cooling R&D (DLC, immersion, jet impingement), with 10+ years in electronics cooling, two-phase heat transfer, and engineering software development.

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false

selected_papers: true
social: true

announcements:
  enabled: false
  scrollable: true
  limit: 5

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

{% assign proceedings = site.data.resume.publications | where_exp: "p", "p.publisher contains 'Proceedings'" %}
{% assign n_proc = proceedings | size %}
{% assign n_journal = site.data.resume.publications | size | minus: n_proc %}
{% assign n_patents = site.data.resume.certificates | where: "issuer", "Korean Intellectual Property Office" | size %}
{% assign n_us = site.data.resume.certificates | where: "issuer", "United States Patent and Trademark Office" | size %}
{% assign n_sw = site.data.resume.certificates | where: "issuer", "Korea Copyright Commission" | size %}
{% assign n_tt = site.data.resume.volunteer | size %}

I am a Senior Researcher at the [Heat Pump Research Center](https://www.kimm.re.kr), Korea Institute of Machinery and Materials (KIMM), leading **AI data center cooling** R&D (direct liquid cooling, immersion, jet impingement) as PI and project lead. My 10+ years in electronics cooling and two-phase heat transfer began with pulsating heat pipes at [KAIST](https://www.kaist.ac.kr) (Ph.D. 2021, advised by [Prof. Sung Jin Kim](https://scholar.google.com/citations?user=1YqQxnkAAAAJ)).

I combine hands-on experimental expertise, from cryogenic (-220°C) liquid-hydrogen heat exchangers to 100 MPa high-pressure testing, with production-grade engineering software development (Python, FastAPI, React Native). Lab-to-market record: **{{ n_tt }} technology transfers** to industry, **{{ n_patents }} domestic + {{ n_us }} U.S. patents**, **{{ n_journal }} journal papers**, and **{{ n_sw }} registered software programs** ([academic CV](/assets/pdf/cv_academic.pdf)).

My research focuses on **thermal engineering** with applications in:

- **Data center cooling** — immersion cooling, direct liquid cooling (DLC), jet-impingement cooling for next-generation high-power servers
- **High-heat-flux electronics cooling** — CPU/GPU cold plate design, focused cooling for next-generation chips
- **Heat exchangers** — Printed Circuit Heat Exchangers (PCHE) for cryogenic liquid hydrogen, compact heat exchanger design & optimization
- **Heat pump systems** — chemisorption/adsorption heat pumps, high-temperature heat pumps (300°C class)
- **Low GWP refrigerant systems** — next-generation eco-friendly refrigerant development, VLE measurement, equation of state development
- **Two-phase heat transfer** — boiling, evaporation, pulsating heat pipes, vapor chambers, flow visualization
- **Cryogenic heat transfer** — liquid hydrogen vaporizer design, supercritical fluid heat transfer
