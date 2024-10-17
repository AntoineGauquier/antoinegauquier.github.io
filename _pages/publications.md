---
layout: page
permalink: /publications/
title: Publications
description: Here is a list of my publications. It might not be up to date: please visit my <a href='https://dblp.org/pid/352/3990.html'>DBLP page</a> or my <a href='https://scholar.google.com/citations?user=yAAqUcoAAAAJ'>Google Scholar</a> page for latest information.
nav: true
nav_order: 1
years: [2025, 2024, 2023, 2022, 2021]
---

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
