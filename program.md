---
layout: page  
title: Program
description: The program of events for NIME2025.
permalink: /program/
---
{: .info-box}
The program and website are still under construction, as we are waiting for additional materials to be uploaded by authors. This means some information may not be up to date.
Please check the website again later. Thank you for your understanding.


{% assign sorted_sessions = site.data.sessions | sort: "date" %}

{% comment %}
<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.17/index.global.min.js'></script>
{% endcomment %}
<script src='{% link assets/imports/fullcalendar@6.1.17/index.global.min.js %}'></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    let sessionsData = {{ sorted_sessions | jsonify }};
    let firstEventDate = sessionsData[0]["start"]
    <!-- TODO: loop over the array and set url property to the session page. -->
    console.log(sessionsData)
    eventColours = ["#2e312d","#7e7a72","#8f95a5","#97a7b6","#565b68","#5f6e62","#b69255","#bd5c6f"]
    for (i in sessionsData) {
        let sessionId = sessionsData[i]["id"]
        let sessionType = sessionsData[i]["type"]
        sessionsData[i]["url"] = `{{ site.baseurl }}/sessions/${sessionId}.html`
        if (sessionType == "admin") {
          sessionsData[i]["backgroundColor"] = eventColours[0]
          sessionsData[i]["borderColor"] = eventColours[0]
        } else if (sessionType == "papers") {
          sessionsData[i]["backgroundColor"] = eventColours[1]
          sessionsData[i]["borderColor"] = eventColours[1]
        } else if (sessionType == "posters") {
          sessionsData[i]["backgroundColor"] = eventColours[2]
          sessionsData[i]["borderColor"] = eventColours[2]
        } else if (sessionType == "installations") {
          sessionsData[i]["backgroundColor"] = eventColours[3]
          sessionsData[i]["borderColor"] = eventColours[3]
        } else if (sessionType == "concert") {
          sessionsData[i]["backgroundColor"] = eventColours[4]
          sessionsData[i]["borderColor"] = eventColours[4]
        } else if (sessionType == "workshops") {
          sessionsData[i]["backgroundColor"] = eventColours[5]
          sessionsData[i]["borderColor"] = eventColours[5]
        } else if (sessionType == "plenary") {
          sessionsData[i]["backgroundColor"] = eventColours[6]
          sessionsData[i]["borderColor"] = eventColours[6]
        }
    }
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        themeSystem: 'bootstrap5',
        timeZone: 'AEST',
        initialView: 'timeGridWeek',
        events: sessionsData,
        initialDate: firstEventDate,
        slotEventOverlap: false,
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
