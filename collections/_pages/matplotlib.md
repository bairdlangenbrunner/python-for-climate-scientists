---
permalink: /matplotlib/index.html
title: matplotlib
layout: page
order: 4
---

<div class="container mx-auto mt-2">
{% assign sorted_coding_pages = site.matplotlib | sort:"order" %}
{% for post in sorted_coding_pages %}
  {% include post-block-no-date.html %}
{% endfor %}
</div>
