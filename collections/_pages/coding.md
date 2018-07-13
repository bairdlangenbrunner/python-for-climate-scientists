---
permalink: /coding/index.html
title: coding tips
layout: page
order: 2
---

<!--<div class="container col-9 mt-2">-->
<div class="container mx-auto">
    {% for post in site.coding %}
    {% include post-block-no-date.html %}
    {% endfor %}
</div>
