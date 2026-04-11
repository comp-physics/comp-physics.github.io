---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

## Research

Our group builds numerical methods, computational models, and open-source software for problems in defense, energy, and medicine — optimized for the world's largest supercomputers. See <a href="{{ site.url }}{{ site.baseurl }}/papers">our papers</a> for the full picture.

<div class="research-grid">

{% for theme in site.data.research.themes %}
<div class="research-card">
{% if theme.thumb %}<img src="{{ site.url }}{{ site.baseurl }}{{ theme.thumb }}" class="research-thumb" alt="{{ theme.alt | default: theme.title }}" loading="lazy">{% endif %}
<div class="research-body">
<h4 class="research-title">{{ theme.title }}</h4>
<p class="research-desc">{{ theme.summary }}</p>
<ul class="research-bullets">
{% for b in theme.bullets %}
<li>{{ b }}</li>
{% endfor %}
</ul>
<div class="research-footer" markdown="0">
{% if theme.papers %}<span class="research-pubs"><i class="fas fa-file-alt"></i> {% for key in theme.papers %}<a href="{{ site.url }}{{ site.baseurl }}/papers/#{{ key }}">{{ key }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</span>{% endif %}
{% if theme.links %}<div class="research-links">{% for link in theme.links %}<a href="{{ link.url }}" target="_blank" rel="noopener noreferrer" class="research-link"><i class="fab fa-github"></i> {{ link.text }}</a>{% endfor %}</div>{% endif %}
</div>
</div>
</div>
{% endfor %}

</div>
