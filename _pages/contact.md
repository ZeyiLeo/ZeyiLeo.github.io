---
layout: page
title: contact
permalink: /contact/
description: Contact ZY LEE for conversations across healthcare, communication, AI literacy, entrepreneurship, and interdisciplinary collaboration.
hide_header: true
nav: true
nav_order: 6
---

<section class="leo-page-hero leo-page-hero-editorial">
  <p class="leo-kicker">Contact</p>
  <h1>Start with a clear reason to talk.</h1>
  <p>I am open to thoughtful conversations around healthcare education, public health communication, AI literacy, social innovation, entrepreneurship, and interdisciplinary collaboration.</p>
</section>

<div class="leo-contact-grid">
  <a class="leo-contact-card" href="mailto:{{ site.email }}">
    <span>Email</span>
    <h2>{{ site.email }}</h2>
    <p>Best for project, research, collaboration, and speaking-related conversations.</p>
  </a>
  <a class="leo-contact-card" href="https://www.linkedin.com/in/{{ site.linkedin_username }}/">
    <span>LinkedIn</span>
    <h2>ZY LEE</h2>
    <p>Professional updates, education context, and public-facing work.</p>
  </a>
  <a class="leo-contact-card" href="https://instagram.com/{{ site.instagram_id }}">
    <span>Instagram</span>
    <h2>@{{ site.instagram_id }}</h2>
    <p>More personal visual updates and behind-the-scenes moments.</p>
  </a>
  {% if site.xiaohongshu_url %}
  <a class="leo-contact-card" href="{{ site.xiaohongshu_url }}">
    <span>小红书</span>
    <h2>RedNote</h2>
    <p>Chinese-language updates, notes, and everyday perspective.</p>
  </a>
  {% endif %}
  <a class="leo-contact-card" href="https://github.com/{{ site.github_username }}">
    <span>GitHub</span>
    <h2>{{ site.github_username }}</h2>
    <p>Website, digital systems, and technical learning trail.</p>
  </a>
</div>
