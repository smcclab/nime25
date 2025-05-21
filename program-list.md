---
layout: page  
title: Program List
description: A list of all works to be presented at NIME2025
permalink: /program-list/
---

{% assign works = site.data.proceedings %}


<h2>Works:</h2>

<ul>
{% for paper in works %}
{% capture proceeding_entry_url %}{{ paper.id | datapage_url: "proceedings" | relative_url }}{% endcapture %}

  <li>
    <a href="{{ proceeding_entry_url }}"><strong>{{ paper.title }}</strong></a><br>
    by {{ paper.authors }}<br>
  </li>
{% endfor %}
</ul>
