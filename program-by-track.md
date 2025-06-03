---
layout: page  
title: Program by Track
description: A list of all works to be presented at NIME2025
permalink: /program-by-track/
---

<h2>Papers:</h2>

<ul>
{% assign works = site.data.proceedings | where: "track", "paper" %}
{% for paper in works %}
{% capture proceeding_entry_url %}{{ paper.id | datapage_url: "proceedings" | relative_url }}{% endcapture %}

  <li>
    <a href="{{ proceeding_entry_url }}"><strong>{{ paper.title }}</strong></a><br>
    by {{ paper.authors }}<br>
  </li>
{% endfor %}
</ul>

<h2>Music:</h2>

<ul>
{% assign works = site.data.proceedings | where: "track", "music" %}
{% for paper in works %}
{% capture proceeding_entry_url %}{{ paper.id | datapage_url: "proceedings" | relative_url }}{% endcapture %}

  <li>
    <a href="{{ proceeding_entry_url }}"><strong>{{ paper.title }}</strong></a><br>
    by {{ paper.authors }}<br>
  </li>
{% endfor %}
</ul>

<h2>Workshops:</h2>

<ul>
{% assign works = site.data.proceedings | where: "track", "workshop" %}
{% for paper in works %}
{% capture proceeding_entry_url %}{{ paper.id | datapage_url: "proceedings" | relative_url }}{% endcapture %}

  <li>
    <a href="{{ proceeding_entry_url }}"><strong>{{ paper.title }}</strong></a><br>
    by {{ paper.authors }}<br>
  </li>
{% endfor %}
</ul>
