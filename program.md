---
layout: page  
title: Program
permalink: /program/
---


{% assign sorted_sessions = site.data.sessions | sort: "date" %}

<div class="row row-cols-1 row-cols-md-2 g-4">
  {% for session in sorted_sessions %}
    <div class="col">
      <div class="card h-100">
        {% if session.image_url %}
          <img src="{{ session.image_url | relative_url }}" class="card-img-top" alt="{{ session.title }}">
        {% endif %}
        <div class="card-body">
          <h5 class="card-title">{{ session.title }}</h5>
          <h6 class="card-subtitle mb-2 text-muted">{{ session.type | capitalize }} Session</h6>
          <p class="card-text">
            <strong>Date:</strong> {{ session.date | date: "%A, %B %d, %Y" }}<br>
            <strong>Time:</strong> {{ session.date | date: "%I:%M %p" }} AEST<br>
            <strong>Location:</strong> {{ session.location }}<br>
            <strong>Chair:</strong> {{ session.chair }}
          </p>
        </div>
        {% if session.youtube_link %}
          <div class="card-footer">
            <a href="{{ session.youtube_link }}" class="btn btn-primary" target="_blank">Watch on YouTube</a>
          </div>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>
