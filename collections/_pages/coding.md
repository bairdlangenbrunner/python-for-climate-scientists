---
permalink: /coding/index.html
layout: page
order: 2
---

<!--
{% for item in site.pages %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <p><a href="{{ item.url }}">{{ item.title }}</a></p>
{% endfor %}
-->

{% assign sorted_pages = site.coding | sort:"order" %}
{% for item in sorted_pages %}
 <!-- <h2>{{ item.title }}</h2>-->
  <!--<p>{{ item.description }}</p>-->
  <h2><a href="{{ item.url }}">{{ item.title }}</a></h2>
  <h2 class="no-underline h4 bold">{{ item.date | date: "%B, %Y" }}</h2>
  <p>{{ item.description }}</p>
{% endfor %}
