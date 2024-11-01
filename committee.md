---
layout: page  
title: Conference Committee
description: The organising committee and their roles.
permalink: /committee/
---

<div class="container mt-5">  
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
    {% for member in site.data.committee %}
      <div class="col">
        <div class="card h-100">
          {% if member.im %}
            <img src="{{ member.im | relative_url }}" class="card-img-top" alt="{{ member.name }}">
          {% endif %}
          <div class="card-body">
            <h5 class="card-title">
              {% if member.url %}
                <a href="{{ member.url }}" target="_blank" rel="noopener noreferrer">{{ member.name }}</a>
              {% else %}
                {{ member.name }}
              {% endif %}
            </h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ member.role }}</h6>
            <p class="card-text">{{ member.aff }}</p>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
