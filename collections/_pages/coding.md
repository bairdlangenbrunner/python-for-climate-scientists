---
permalink: /coding/index.html
layout: page
title: coding
order: 3
---

```
Coming soon...
```

<!--
{% for item in site.pages %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <p><a href="{{ item.url }}">{{ item.title }}</a></p>
{% endfor %}

layout: category_index
title: Writing
permalink: /writing/
category_name: writing
-->

{% for item in site.coding %}
 <!-- <h2>{{ item.title }}</h2>-->
  <!--<p>{{ item.description }}</p>-->
  <h2><a href="{{ item.url }}">{{ item.title }}</a></h2>
  <p>{{ item.description }}</p>
{% endfor %}
