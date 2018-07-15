---
permalink: /conda/index.html
title: conda
layout: page
order: 3
---

<div class="container mx-auto mt-2">
{% assign sorted_coding_pages = site.conda | sort:"order" %}
{% for post in sorted_coding_pages %}
  {% include post-block-no-date.html %}
{% endfor %}
</div>
