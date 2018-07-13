---
permalink: /coding/index.html
title: coding tips
layout: page
order: 2
---

<!--<div class="container col-9 mt-2">-->
<div class="container mx-auto">
<ul>
    {% for post in site.coding %}
    <li class="h0 li-post-block" type="square">{% include post-block-no-date.html %}</li>
    {% endfor %}
</ul>
</div>
