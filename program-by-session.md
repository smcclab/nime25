---
layout: page  
title: Program by Session
description: A list of all works to be presented at NIME2025 by session.
permalink: /program-by-session/
---

{% assign sorted_sessions = site.data.sessions | sort: "start" %}

<h2>Sessions</h2>

{% for session in sorted_sessions %}
{% if session.type != "admin" and session.type != "plenary" %}
  {% capture session_url %}{{ session.id | datapage_url: "sessions" | relative_url }}{% endcapture %}
  {% assign session_papers = site.data.proceedings | where: "session_code", session.id %}
  <h5><a href="{{ session_url }}">{{ session.title }}{% if session.subtitle %}: {{ session.subtitle }}{% endif %}</a></h5>
  <h6>{{ session.type | capitalize }} Session {% if session.video_url %}(<a href="{{ session.video_url }}">Video Link</a>){% endif %}</h6>
  <p>
    <strong>Date:</strong> {{ session.date }}<br>
    <strong>Location:</strong> {{ session.location }}<br>
    <strong>Chair:</strong> {{ session.chair }}
  </p>

  <ol>
    {% for paper in session_papers %}
    {% capture proceeding_entry_url %}{{ paper.id | datapage_url: "proceedings" | relative_url }}{% endcapture %}
      <li>
        ({{ paper.id }}) <a href="{{ proceeding_entry_url }}"><strong>{{ paper.title }}</strong></a>  ({{paper.duration}} minutes{% if paper.format == "poster"%}, {{ paper.presence }}{% endif %})
        by {{ paper.authors }}
      </li>
    {% endfor %}
  </ol>
{% endif %}
{% endfor %}
