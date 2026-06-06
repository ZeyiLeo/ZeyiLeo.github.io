---
layout: page
title: projects
permalink: /projects/
description: Dedicated project pages across healthcare, research, public health, communication, education, entrepreneurship, and digital work.
nav: true
nav_order: 2
display_categories: [research, public-health, global-health, communication, education, entrepreneurship, digital]
horizontal: false
---

<div class="leo-page-hero leo-page-hero-compact">
  <p class="leo-kicker">Project archive</p>
  <h1>Each project gets its own room now.</h1>
  <p>This archive is organised as a set of case pages, not a pile of titles. Each page combines personal photos, official context, role framing, and reflection, because apparently a project should explain what actually happened.</p>
</div>

<div class="leo-visual-grid">
  <a class="leo-visual-card" href="{{ '/projects/orbis-glaucoma/' | relative_url }}"><img src="{{ '/assets/img/projects/orbis-glaucoma/cover.jpg' | relative_url }}" alt="Glaucoma project"><span>Public health</span></a>
  <a class="leo-visual-card" href="{{ '/projects/nursing-forum/' | relative_url }}"><img src="{{ '/assets/img/projects/nursing-forum/cover.jpg' | relative_url }}" alt="Nursing forum"><span>Event</span></a>
  <a class="leo-visual-card" href="{{ '/projects/china-latam-salon/' | relative_url }}"><img src="{{ '/assets/img/projects/china-latam-salon/cover.jpg' | relative_url }}" alt="China Latin America salon"><span>Speaking</span></a>
  <a class="leo-visual-card" href="{{ '/projects/hku-infoday/' | relative_url }}"><img src="{{ '/assets/img/projects/hku-infoday/cover.jpg' | relative_url }}" alt="HKU Info Day"><span>Ambassador</span></a>
</div>

<div class="leo-tag-list leo-filter-note">
  <span>Research</span>
  <span>Public health</span>
  <span>Global health</span>
  <span>Communication</span>
  <span>Education</span>
  <span>Entrepreneurship</span>
  <span>Digital</span>
</div>

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="grid">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}
{% else %}
{% assign sorted_projects = site.projects | sort: "importance" %}
{% if page.horizontal %}
  <div class="container"><div class="row row-cols-2">{% for project in sorted_projects %}{% include projects_horizontal.liquid %}{% endfor %}</div></div>
{% else %}
  <div class="grid">{% for project in sorted_projects %}{% include projects.liquid %}{% endfor %}</div>
{% endif %}
{% endif %}
</div>
