---
layout: page  
title: Program
permalink: /program/
---

<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.15/index.global.min.js'></script>
<script>


  document.addEventListener('DOMContentLoaded', function() {
    let sessionsData = {{ site.data.sessions | jsonify }};
    <!-- TODO: loop over the array and set url property to the session page. -->

    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      timeZone: 'AEST',
      initialView: 'timeGridWeek',
      events: sessionsData,
    });
    calendar.render();

    <!-- experiments with the session data... -->
    console.log(sessionsData)
    var event = calendar.getEventById('research1')
    console.log(event)

    var start = event.start // a property (a Date object)
    console.log(start.toISOString()) // "2018-09-01T00:00:00.000Z"
  });
</script>
<div id='calendar'></div>

<h2>Sessions</h2>

{% assign sorted_sessions = site.data.sessions | sort: "date" %}

<div class="row row-cols-1 row-cols-md-2 g-4">
  {% for session in sorted_sessions %}
    {% capture session_url %}{{ session.id | datapage_url: "sessions" | relative_url }}{% endcapture %}
    <div class="col">
      <div class="card h-100">
        {% if session.image_url %}
          <img src="{{ session.image_url | relative_url }}" class="card-img-top" alt="{{ session.title }}">
        {% endif %}
        <div class="card-body">
          <h5 class="card-title">
            <a href="{{ session_url }}" class="text-decoration-none text-dark">{{ session.title }}</a>
          </h5>
          <h6 class="card-subtitle mb-2 text-muted">{{ session.type | capitalize }} Session</h6>
          <p class="card-text">
            <strong>Date:</strong> {{ session.date | date: "%A, %B %d, %Y" }}<br>
            <strong>Time:</strong> {{ session.date | date: "%I:%M %p" }} AEST<br>
            <strong>Location:</strong> {{ session.location }}<br>
            <strong>Chair:</strong> {{ session.chair }}
          </p>
        </div>
        <div class="card-footer">
          <a href="{{ session_url }}" class="btn btn-outline-secondary">Details</a>
          {% if session.video_url %}
            <a href="{{ session.video_url }}" class="btn btn-outline-secondary" target="_blank">Video</a>
          {% endif %}
        </div>
      </div>
    </div>
  {% endfor %}
</div>
