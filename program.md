---
layout: page  
title: Program
description: The program of events for NIME2025.
permalink: /program/
---

{: .info-box}
A list of all accepted papers, music, and workshops is listed [here by track]({% link program-by-track.md %}) and [here by session]({% link program-by-session.md %}).


{% assign sorted_sessions = site.data.sessions | sort: "start" %}

{% comment %}
<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.17/index.global.min.js'></script>
{% endcomment %}
<script src='https://cdn.jsdelivr.net/npm/moment@2.29.4/min/moment.min.js'></script>
<script src='https://cdn.jsdelivr.net/npm/moment-timezone@0.5.40/builds/moment-timezone-with-data.min.js'></script>
<script src='{% link assets/imports/fullcalendar@6.1.17/index.global.min.js %}'></script>
<script src='https://cdn.jsdelivr.net/npm/@fullcalendar/moment-timezone@6.1.17/index.global.min.js'></script>
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
        // timeZone: 'local',
        initialView: 'timeGridFourDay',
        views: {
          timeGridFourDay: {
            type: 'timeGrid',
            duration: { days: 4 }
          }
        },
        events: sessionsData,
        initialDate: firstEventDate,
        slotEventOverlap: false,
        nowIndicator: true,
                eventContent: function(arg) {
              const title = arg.event.title;
              const subtitle = arg.event.extendedProps.subtitle;
              return {
                html:`
                  <div class="fc-event-title">
                    ${title}
                    ${subtitle ? `<div class="fc-event-subtitle" style="font-size: 0.85em; color:rgb(255, 255, 255);">${subtitle}</div>` : ''}
                  </div>
                  `
              };
            }
    });
    calendar.render();
    const timezoneSelector = document.getElementById('timezone-selector');
    const timezoneDisplay = document.getElementById('current-timezone-display');
    // Function to populate timezone options
    async function populateTimezones() {
        try {
            const response = await fetch('{% link assets/timezones.json %}');
            const timezones = await response.json();
            // Clear existing options except the first two (local and UTC)
            const existingOptions = timezoneSelector.querySelectorAll('option');
            for (let i = 2; i < existingOptions.length; i++) {
                existingOptions[i].remove();
            }
            // Add Australia/Canberra as the first option after local and UTC
            const canberraOption = document.createElement('option');
            canberraOption.value = 'Australia/Canberra';
            canberraOption.textContent = 'Australia / Canberra (Default)';
            canberraOption.selected = true; // Set as selected by default
            timezoneSelector.appendChild(canberraOption);
            // Add timezone options
            timezones.forEach(timezone => {
                const option = document.createElement('option');
                option.value = timezone;
                // Create a more readable display name
                const displayName = timezone.replace(/\//g, ' / ').replace(/_/g, ' ');
                option.textContent = displayName;
                timezoneSelector.appendChild(option);
            });
            console.log(`Added ${timezones.length} timezone options`);
        } catch (error) {
            console.error('Failed to load timezones:', error);
        }
    }
    // Load timezones when page loads
    populateTimezones();
    // Add the event listener
    timezoneSelector.addEventListener('change', function() {
        const selectedTimezone = this.value;
        updateTimezone(selectedTimezone);
    });
    // Function to update the timezone display
    function updateTimezone(timezone) {
        calendar.setOption('timeZone', timezone);
        calendar.render();
        if (!timezoneDisplay) return;
        let displayText = 'Calendar Timezone: ';
        if (timezone === 'local') {
            displayText += 'Local Time';
        } else if (timezone === 'UTC') {
            displayText += 'UTC';
        } else {
            // Format timezone name for display
            displayText += timezone.replace(/\//g, ' / ').replace(/_/g, ' ');
        }
        // Optional: Add current time in selected timezone
        try {
            const now = new Date();
            const timeString = now.toLocaleTimeString('en-US', {
                timeZone: timezone === 'local' ? undefined : timezone,
                hour12: false,
                hour: '2-digit',
                minute: '2-digit'
            });
            displayText += ` (${timeString})`;
        } catch (error) {
            // If timezone is invalid, just show the timezone name
            console.warn('Invalid timezone for time display:', timezone);
        }
        timezoneDisplay.textContent = displayText;
    }
    // Initialize display on page load
    updateTimezone('Australia/Canberra');
  });
</script>

<div>
  Timezone:
  <select id='timezone-selector'>
    <option value='local'>local</option>
    <option value='UTC'>UTC</option>
  </select>
  <span id='current-timezone-display' style='margin-left: 10px; font-weight: bold; color: #666;'>
        Current: Local Time
  </span>
</div>

<div id='calendar'></div>

<h2>Sessions</h2>


<div class="row row-cols-1 row-cols-md-3 row-cols-sm-2 g-4">
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