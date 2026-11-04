---
layout: page
title: projects
permalink: /projects/
description: Current and completed research projects, with my role, period, and research area for each.
nav: true
nav_order: 3
---

<div class="project-portfolio">

{% include projects/counts.liquid %}

{% include projects/role_legend.liquid %}

<section id="current-projects" class="pp-section">
<h2 class="pp-heading">Current projects</h2>
{% include projects/list.liquid mode="current" empty_text="No current projects." %}
</section>

<section id="research-areas" class="pp-section">
<h2 class="pp-heading">Research areas</h2>
{% include projects/research_areas.liquid %}
</section>

<section id="project-timeline" class="pp-section">
<h2 class="pp-heading">Timeline</h2>
{% include projects/timeline.liquid %}
</section>

<section id="completed-section" class="pp-section">
{% include projects/completed.liquid %}
</section>

<p class="pp-footer">Publications, patents, and the full record are in the <a href="{{ '/cv/#projects' | relative_url }}">CV</a>.</p>

</div>
